"""Importa fases, participantes e jogos do Brasileiro 1990.

Regulamento (RSSSF braz90): 20 clubes em 2 grupos de 10, disputados em 2
estagios (1o estagio = jogos contra o outro grupo; 2o estagio = jogos contra o
proprio grupo). Combinado, e um turno unico de 190 jogos. Vencedores de grupo
de cada estagio + 4 melhores campanhas vao as quartas (ida/volta), depois semi
e final (ida/volta). 2 pontos por vitoria. Corinthians campeao (2-0 no agregado
sobre o Sao Paulo).

Detalhes da fonte: ha um typo "INERNACIONAL-SP" (= Inter de Limeira) e dois
clubes distintos chamados Internacional (RS = Internacional; SP = Inter de
Limeira). Sao Jose desta edicao e o "Sao Jose-SP".
"""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import replace

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

YEAR = 1990
SOURCE = "https://www.rsssf.org/tablesb/braz90.html"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1990_partidas.csv"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "bragantino": "Bragantino",
    "goias": "Goias",
    "gremio": "Gremio",
    "inernacional sp": "Inter de Limeira",   # typo da fonte
    "internacional sp": "Inter de Limeira",
    "internacional rs": "Internacional",
    "nautico": "Nautico",
    "sao jose": "Sao Jose-SP",
    "sao paulo": "Sao Paulo",
    "vasco": "Vasco",
    "vitoria": "Vitoria",
})

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
          "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}

GAME_RE = re.compile(r"^(.+?)\s+(\d+)\s+x\s+(.+?)\s+(\d+)\s*$")
DATE_RE = re.compile(r"^(\d{1,2})/([a-z]{3})/(\d{2})$", re.I)
ROUND_RE = re.compile(r"^ROUND\s+(\d+)", re.I)

KO_SECTIONS = {"QUARTERFINALS": ("Quartas de final", 2), "SEMIFINALS": ("Semifinal", 3), "FINALS": ("Final", 4)}


def clean_team(value: str) -> str:
    head = re.split(r"\s{2,}", value.strip())[0]
    return canonical_name(head)


def ymd(day, mon: str) -> str:
    return f"{YEAR}-{MONTHS[mon.lower()]:02d}-{int(day):02d}"


def parse_first_phase(text: str) -> list[Game]:
    block = text[text.find("FIRST STAGE"):text.find("QUARTERFINALS")]
    games: list[Game] = []
    offset = 0
    current_round = None
    current_date = None
    game_no = 0
    for line in block.split("\n"):
        s = line.strip()
        if s == "FIRST STAGE":
            offset = 0
            continue
        if s == "SECOND STAGE":
            offset = 10
            continue
        rm = ROUND_RE.match(s)
        if rm:
            current_round = int(rm.group(1)) + offset
            continue
        dm = DATE_RE.match(s)
        if dm:
            current_date = ymd(dm.group(1), dm.group(2))
            continue
        m = GAME_RE.match(s)
        if not m:
            continue
        game_no += 1
        games.append(Game(YEAR, "Primeira fase", 1, "liga", current_round, game_no, current_date,
                          clean_team(m.group(1)), clean_team(m.group(3)),
                          int(m.group(2)), int(m.group(4)), SOURCE, ""))
    if len(games) != 190:
        raise SystemExit(f"1990 Primeira fase: esperava 190 jogos, encontrei {len(games)}")
    return games


def parse_knockout(text: str) -> list[Game]:
    block = text[text.find("QUARTERFINALS"):]
    games: list[Game] = []
    fase = None
    ordem = None
    current_date = None
    jogo_por_par: dict[tuple, int] = {}
    contador: dict[str, int] = {}
    for line in block.split("\n"):
        s = line.strip()
        if s in KO_SECTIONS:
            fase, ordem = KO_SECTIONS[s]
            continue
        if s in ("FIRST LEG", "SECOND LEG"):
            continue
        dm = DATE_RE.match(s)
        if dm:
            current_date = ymd(dm.group(1), dm.group(2))
            continue
        m = GAME_RE.match(s)
        if not m or fase is None:
            continue
        t1, g1, t2, g2 = clean_team(m.group(1)), int(m.group(2)), clean_team(m.group(3)), int(m.group(4))
        chave = (fase, frozenset((t1, t2)))
        if chave not in jogo_por_par:
            contador[fase] = contador.get(fase, 0) + 1
            jogo_por_par[chave] = contador[fase]
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo_por_par[chave], current_date, t1, t2, g1, g2, SOURCE, ""))
    contagem = {f: sum(1 for g in games if g.fase == f) for f in ("Quartas de final", "Semifinal", "Final")}
    if contagem != {"Quartas de final": 8, "Semifinal": 4, "Final": 2}:
        raise SystemExit(f"1990 mata-mata: contagem inesperada {contagem}")
    return games


def parse_1990() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz90.html")
    text = text[:text.find("SEGUNDA DIVIS")]  # corta a Serie B
    games = parse_first_phase(text)
    games += parse_knockout(text)

    participants = sorted({g.mandante for g in games[:190]} | {g.visitante for g in games[:190]})
    if len(participants) != 20:
        raise SystemExit(f"1990: esperava 20 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 204:
        raise SystemExit(f"1990: esperava 204 jogos, encontrei {len(games)}")
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute(
            "SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = ? AND competicao_nome = 'Campeonato Brasileiro'",
            (YEAR,),
        ).fetchone()
        if not row:
            raise SystemExit(f"Edicao nacional {YEAR} nao encontrada.")
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

        def club_id(name: str) -> int:
            name = canonical_db_name(name)
            if name in by_name:
                return by_name[name]
            raise SystemExit(f"Clube nao encontrado em dim_clube: {name}")

        participants = sorted({canonical_db_name(c) for c in participants})
        games = [replace(g, mandante=canonical_db_name(g.mandante), visitante=canonical_db_name(g.visitante)) for g in games]

        con.execute("DELETE FROM fato_partida_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM dim_fase_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM fato_participante_nacional_historico WHERE edicao_nacional_id = ?", (edicao_id,))
        for club in participants:
            con.execute(
                "INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, ?, ?, ?)",
                (edicao_id, YEAR, club_id(club), SOURCE),
            )
        fase_ids: dict[str, int] = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute(
                    "INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, ?, ?, ?, ?)",
                    (edicao_id, YEAR, g.fase_ordem, g.fase, g.fase_tipo),
                )
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, YEAR, fase_ids[g.fase], g.rodada, g.jogo, g.data, club_id(g.mandante), club_id(g.visitante), g.gm, g.gv, g.fonte, g.observacao),
            )
        con.commit()
    finally:
        con.close()


def write_audit(games: list[Game]) -> None:
    with AUDIT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["temporada", "fase", "rodada", "jogo", "data", "mandante", "placar", "visitante", "observacao", "fonte"]
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        writer.writeheader()
        for g in games:
            writer.writerow({"temporada": g.temporada, "fase": g.fase, "rodada": g.rodada or "", "jogo": g.jogo or "", "data": g.data or "", "mandante": g.mandante, "placar": f"{g.gm}-{g.gv}", "visitante": g.visitante, "observacao": g.observacao, "fonte": g.fonte})


def main() -> None:
    participants, games = parse_1990()
    import_year(participants, games)
    write_audit(games)
    print(f"1990: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
