"""Base comum dos importadores do Brasileiro antigo a partir de 1985 para tras.

Os anos 1983-1985 da RSSSF seguem o mesmo desenho: blocos de rodadas com
jogos "Time  a-b  Time", tabelas de classificacao entre eles e mata-mata em
ida e volta "Time  a-b  c-d  Time". Cada ano define so os cortes do texto
(marcadores de inicio e fim de cada fase), o tipo da fase e quantos jogos
espera; este modulo faz a leitura, confere contagens e participantes contra a
classificacao final ja existente no banco e grava as tabelas historicas.

Regras de leitura:
- linhas de tabela (" 1-Time ...", "1] Time ...") e de autores de gol
  ("  [Fulano; Beltrano]") sao ignoradas;
- datas "[Jan 26]" e "[Jul 24 and 28]" valem para os jogos seguintes;
- prorrogacao "[aet x-y]" em jogo unico: o placar gravado inclui a prorrogacao
  e a observacao guarda o tempo normal e os penaltis;
- em ida e volta, o segundo placar vem do ponto de vista do primeiro time.
"""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import dataclass, replace

from importar_brasileirao_historico_1998_1999 import norm
from importar_brasileirao_historico_2000_2001 import (
    CANONICAL,
    DB,
    ROOT,
    Game,
    canonical_name,
    create_tables,
    read_pre,
)

# Nomes da RSSSF de 1983-1985 que nao batem direto com dim_clube.
CANONICAL.update({
    "america rj": "America-RJ",
    "atletico go": "Atletico-GO",
    "atletico pr": "Athletico-PR",
    "botafogo rj": "Botafogo-RJ",
    "botafogo pb": "Botafogo-PB",
    "botafogo sp": "Botafogo-SP",
    "corinthiians": "Corinthians",  # erro de digitacao na RSSSF de 1981
    "flamengo rj": "Flamengo",
    "flamengo pi": "Flamengo-PI",
    "fluminense rj": "Fluminense",
    "internacional rs": "Internacional",
    "nacional": "Nacional-AM",
    "operario ms": "Operário-MS",
    "operario mt": "Operário-MT",
    "rio branco es": "Rio Branco-ES",
    "vasco da gama": "Vasco",
    # clubes menores, com o nome que a classificacao final do banco usa
    "america rn": "America-RN",
    "americano": "Americano-RJ",
    "auto esporte": "Auto Esporte-PI",
    "brasil": "Brasil de Pelotas",
    "brasilia": "Brasília EC",
    "campo grande": "Campo Grande-RJ",
    "colorado": "Colorado-PR",
    "comercial": "Comercial-MS",
    "desportiva": "Desportiva-ES",
    "ferroviaria": "Ferroviária-SP",
    "ferroviario": "Ferroviário-CE",
    "juventus": "Juventus-SP",
    "leonico": "Leônico-BA",
    "moto clube": "Moto Club",
    "pinheiros": "Pinheiros-PR",
    "rio negro": "Rio Negro-AM",
    "tiradentes": "Tiradentes-PI",
    "river": "River-PI",
    "sao jose": "São José-SP",
    "internacional sm": "Inter de Santa Maria",
    "internacional sp": "Inter de Limeira",
    "sao paulo sp": "Sao Paulo",
    "xv de novembro": "XV de Jaú",  # 1982: EC XV de Novembro (Jau)
    # em 1980-1985 so jogaram estes; conferir ao descer para anos anteriores
    "rio branco": "Rio Branco-ES",
    "vila nova": "Vila Nova-GO",
})

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

DATE_RE = re.compile(r"^\[(\w{3})\s+(\d{1,2})(?:\s+and\s+(?:(\w{3})\s+)?(\d{1,2}))?\]\s*$", re.I)
TABLE_RE = re.compile(r"^\d+\s*[-\]]")
SINGLE_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(.+?)(?:\s+\[(.*?)\]?)?\s*$")
TWO_LEG_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)(?:\s+\[(.*?)\]?)?\s*$")
AWD_RE = re.compile(r"^(.+?)\s+awd\s+(.+?)\s+\[(.*)$", re.I)
AWD_SCORE_RE = re.compile(r"awarded\s+(\d+)-(\d+)", re.I)
AET_RE = re.compile(r"aet\s+(\d+)-(\d+)", re.I)
PEN_RE = re.compile(r"pen\s+(\d+)-(\d+)", re.I)


@dataclass
class Fase:
    """Um corte do texto da RSSSF que vira uma fase no banco."""
    nome: str
    inicio: str          # marcador de inicio (primeira ocorrencia a partir do corte anterior)
    fim: str             # marcador de fim (primeira ocorrencia depois do inicio)
    tipo: str            # "grupo" | "liga" | "mata_mata"
    jogos: int           # jogos esperados
    ida_volta: bool = False


def clean_team(value: str) -> str:
    raw = re.sub(r"\s{2,}.*$", "", value.strip())
    if raw.startswith("Oper") and raw.endswith(("-MS", " MS")):
        return "Operário-MS"
    if raw.startswith("Oper") and raw.endswith(("-MT", " MT")):
        return "Operário-MT"
    if "utico" in raw:
        return "Nautico"
    return canonical_name(raw)


def ymd(year: int, month: str, day) -> str:
    return f"{year}-{MONTHS[month[:3].title()]:02d}-{int(day):02d}"


def _linhas_de_jogo(block: str):
    """Linhas nao vazias do bloco, sem espacos nas pontas."""
    for line in block.split("\n"):
        s = line.strip()
        if not s:
            continue
        yield s


def parse_single(block: str, year: int, fase: Fase, ordem: int, fonte: str) -> list[Game]:
    games: list[Game] = []
    data = None
    rodada = None
    for s in _linhas_de_jogo(block):
        rm = re.match(r"^Round\s+(\d+)", s, re.I)
        if rm:
            rodada, data = int(rm.group(1)), None
            continue
        dm = DATE_RE.match(s)
        if dm:
            data = ymd(year, dm.group(1), dm.group(2))
            continue
        if s.startswith("[") or TABLE_RE.match(s) or s.startswith("-"):
            continue
        awd = AWD_RE.match(s)
        if awd:
            # resultado dado no tribunal: "A awd B [awarded 0-1, orginally 1-0, ..."
            placar = AWD_SCORE_RE.search(awd.group(3))
            if not placar:
                raise SystemExit(f"{year} {fase.nome}: jogo 'awd' sem placar atribuido: {s}")
            games.append(Game(year, fase.nome, ordem, fase.tipo, rodada, len(games) + 1, data,
                              clean_team(awd.group(1)), clean_team(awd.group(2)),
                              int(placar.group(1)), int(placar.group(2)), fonte,
                              f"Resultado atribuido no tribunal: {awd.group(3).strip().rstrip(']')}"))
            continue
        m = SINGLE_RE.match(s)
        if not m:
            continue
        gm, gv = int(m.group(2)), int(m.group(3))
        nota = m.group(5) or ""
        obs = ""
        aet, pen = AET_RE.search(nota), PEN_RE.search(nota)
        if aet:
            obs = f"Tempo normal {gm}-{gv}; prorrogacao {aet.group(1)}-{aet.group(2)}."
            gm, gv = gm + int(aet.group(1)), gv + int(aet.group(2))
        if pen:
            obs = (obs + " " if obs else "") + f"Penaltis: {pen.group(1)}-{pen.group(2)}."
        games.append(Game(year, fase.nome, ordem, fase.tipo, rodada, len(games) + 1, data,
                          clean_team(m.group(1)), clean_team(m.group(4)), gm, gv, fonte, obs))
    return games


def parse_two_legs(block: str, year: int, fase: Fase, ordem: int, fonte: str) -> list[Game]:
    games: list[Game] = []
    datas: list[str] = []
    jogo = 0
    for s in _linhas_de_jogo(block):
        dm = DATE_RE.match(s)
        if dm:
            m1, d1, m2, d2 = dm.group(1), dm.group(2), dm.group(3) or dm.group(1), dm.group(4)
            datas = [ymd(year, m1, d1)] + ([ymd(year, m2, d2)] if d2 else [])
            continue
        if s.startswith("[") or TABLE_RE.match(s):
            continue
        m = TWO_LEG_RE.match(s)
        if not m:
            continue
        jogo += 1
        a, b = clean_team(m.group(1)), clean_team(m.group(6))
        a1, b1, a2, b2 = (int(m.group(i)) for i in (2, 3, 4, 5))
        nota = m.group(7) or ""
        obs2 = ""
        aet, pen = AET_RE.search(nota), PEN_RE.search(nota)
        if aet:
            a2, b2 = a2 + int(aet.group(1)), b2 + int(aet.group(2))
            obs2 = f"Prorrogacao: {aet.group(1)}-{aet.group(2)}."
        if pen:
            obs2 = (obs2 + " " if obs2 else "") + f"Penaltis: {pen.group(1)}-{pen.group(2)}."
        games.append(Game(year, fase.nome, ordem, "mata_mata", None, jogo, datas[0] if datas else None,
                          a, b, a1, b1, fonte, ""))
        games.append(Game(year, fase.nome, ordem, "mata_mata", None, jogo, datas[1] if len(datas) > 1 else None,
                          b, a, b2, a2, fonte, obs2))
    return games


def parse_ano(year: int, fonte: str, fases: list[Fase], corte_final: str = "Final Table") -> list[Game]:
    """Le o texto da RSSSF do ano, corta cada fase e confere a contagem de jogos."""
    text = read_pre(ROOT / "data" / f"rsssf_braz{year % 100:02d}.html")
    text = text[: text.find(corte_final)] if corte_final in text else text
    games: list[Game] = []
    pos = 0
    for ordem, fase in enumerate(fases, start=1):
        i = text.find(fase.inicio, pos)
        if i < 0:
            raise SystemExit(f"{year} {fase.nome}: marcador de inicio '{fase.inicio}' nao encontrado")
        j = text.find(fase.fim, i + len(fase.inicio)) if fase.fim else len(text)
        if j < 0:
            raise SystemExit(f"{year} {fase.nome}: marcador de fim '{fase.fim}' nao encontrado")
        bloco = text[i + len(fase.inicio):j]
        parser = parse_two_legs if fase.ida_volta else parse_single
        lidos = parser(bloco, year, fase, ordem, fonte)
        if len(lidos) != fase.jogos:
            raise SystemExit(f"{year} {fase.nome}: esperava {fase.jogos} jogos, encontrei {len(lidos)}")
        games += lidos
        pos = j
    return games


def import_year(year: int, fonte: str, games: list[Game]) -> list[str]:
    """Grava participantes, fases e partidas do ano. Os participantes tem de
    ser exatamente os clubes da classificacao final ja existente no banco."""
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute(
            "SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = ? AND competicao_nome = 'Campeonato Brasileiro'",
            (year,),
        ).fetchone()
        if not row:
            raise SystemExit(f"Edicao nacional {year} nao encontrada.")
        edicao_id = row[0]
        rows = con.execute("SELECT clube_id, nome FROM dim_clube").fetchall()
        by_name = {name: cid for cid, name in rows}
        by_key = {norm(name): (cid, name) for cid, name in rows}

        def canonical_db_name(name: str) -> str:
            if name in by_name:
                return name
            if norm(name) in by_key:
                return by_key[norm(name)][1]
            return name

        games = [replace(g, mandante=canonical_db_name(g.mandante), visitante=canonical_db_name(g.visitante)) for g in games]
        participants = sorted({g.mandante for g in games} | {g.visitante for g in games})
        faltam = [c for c in participants if c not in by_name]
        if faltam:
            raise SystemExit(f"{year}: clubes nao encontrados em dim_clube: {faltam}")

        oficiais = {r[0] for r in con.execute(
            "SELECT clube_id FROM fato_classificacao_final_nacional WHERE edicao_nacional_id = ?", (edicao_id,))}
        lidos = {by_name[c] for c in participants}
        if oficiais and lidos != oficiais:
            nomes = {cid: n for n, cid in by_name.items()}
            raise SystemExit(
                f"{year}: participantes diferentes da classificacao final.\n"
                f"  so nos jogos: {sorted(nomes[c] for c in lidos - oficiais)}\n"
                f"  so na classificacao: {sorted(nomes[c] for c in oficiais - lidos)}")

        con.execute("DELETE FROM fato_partida_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM dim_fase_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM fato_participante_nacional_historico WHERE edicao_nacional_id = ?", (edicao_id,))
        for club in participants:
            con.execute(
                "INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, ?, ?, ?)",
                (edicao_id, year, by_name[club], fonte),
            )
        fase_ids: dict[str, int] = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute(
                    "INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, ?, ?, ?, ?)",
                    (edicao_id, year, g.fase_ordem, g.fase, g.fase_tipo),
                )
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, year, fase_ids[g.fase], g.rodada, g.jogo, g.data, by_name[g.mandante], by_name[g.visitante], g.gm, g.gv, g.fonte, g.observacao),
            )
        con.commit()
        return participants
    finally:
        con.close()


def write_audit(year: int, games: list[Game]) -> str:
    path = ROOT / "data" / f"brasileirao_historico_{year}_partidas.csv"
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["temporada", "fase", "rodada", "jogo", "data", "mandante", "placar", "visitante", "observacao", "fonte"]
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        writer.writeheader()
        for g in games:
            writer.writerow({"temporada": g.temporada, "fase": g.fase, "rodada": g.rodada or "", "jogo": g.jogo or "", "data": g.data or "", "mandante": g.mandante, "placar": f"{g.gm}-{g.gv}", "visitante": g.visitante, "observacao": g.observacao, "fonte": g.fonte})
    return str(path.relative_to(ROOT))


def corrigir_placar(games: list[Game], fase: str, mandante: str, visitante: str,
                    gm: int, gv: int, observacao: str) -> list[Game]:
    """Troca o placar de um jogo lido errado da fonte (exatamente um jogo)."""
    alvo = [i for i, g in enumerate(games)
            if g.fase == fase and clean_team(mandante) == g.mandante and clean_team(visitante) == g.visitante]
    if len(alvo) != 1:
        raise SystemExit(f"correcao {fase} {mandante} x {visitante}: achei {len(alvo)} jogos")
    i = alvo[0]
    games[i] = replace(games[i], gm=gm, gv=gv, observacao=observacao)
    return games


def separar_jogo(games: list[Game], fase: str, mandante: str, placar: str, visitante: str,
                 nova_fase: str, observacao: str) -> list[Game]:
    """Tira um jogo da fase (ex.: desempate no meio de um grupo) e cria com ele
    uma fase propria de jogo unico logo depois; as fases seguintes andam uma
    posicao na ordem. O placar ("3-2") diferencia jogos repetidos."""
    gm, gv = (int(x) for x in placar.split("-"))
    alvo = [i for i, g in enumerate(games)
            if g.fase == fase and clean_team(mandante) == g.mandante and clean_team(visitante) == g.visitante
            and (g.gm, g.gv) == (gm, gv)]
    if len(alvo) != 1:
        raise SystemExit(f"separar {fase} {mandante} x {visitante}: achei {len(alvo)} jogos")
    ordem = games[alvo[0]].fase_ordem
    out = []
    for i, g in enumerate(games):
        if i == alvo[0]:
            out.append(replace(g, fase=nova_fase, fase_ordem=ordem + 1, fase_tipo="mata_mata",
                               rodada=None, jogo=1, observacao=observacao))
        elif g.fase_ordem > ordem:
            out.append(replace(g, fase_ordem=g.fase_ordem + 1))
        else:
            out.append(g)
    return out


def rodar(year: int, fonte: str, fases: list[Fase], total: int, ajustar=None) -> None:
    games = parse_ano(year, fonte, fases)
    if ajustar:
        games = ajustar(games)
    if len(games) != total:
        raise SystemExit(f"{year}: esperava {total} jogos, encontrei {len(games)}")
    participants = import_year(year, fonte, games)
    audit = write_audit(year, games)
    print(f"{year}: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {audit}")
