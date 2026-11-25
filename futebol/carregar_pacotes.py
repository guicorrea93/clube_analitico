"""Carrega no db/futebol.db os pacotes de competição do agente de coleta (data/coleta/<slug>/pacote/).

O formato do pacote está em docs/agente-coleta-COMECE-AQUI.md (seção 4). Roda no fim de
futebol/migrar_brasileirao.py (que apaga e refaz o banco) e também sozinho: apaga a competição do pacote e
grava de novo, sem mexer nas outras.

Clubes: o nome de exibição igual ao clube.nome do banco é o mesmo clube. O casamento é só pelo nome exato,
nunca pela chave sem acento: "Maringá" não é o "GE Maringá". Nome que não está no banco vira clube novo, com
estado, cidade e país. As grafias de cada fonte (nomes_fonte) vão para clube_nome e servem também para achar
o clube quando um arquivo do pacote traz o nome da fonte (ex.: artilheiros "Etti Jundiaí/SP").
No fim confere, por edição, jogos, gols, gols com autor e campeão contra o pacote.

Nome de exibição único no mundo: se o clube do pacote tem o nome de um clube de outro país já no banco, o
carregador para (NomeRepetido) e nada da competição é gravado.

Uso: python futebol/carregar_pacotes.py [slug ...]     (sem slug: todos os pacotes de data/coleta/)
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
import sys
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / "db" / "futebol.db"
COLETA = RAIZ / "data" / "coleta"
PAISES = {"BRA": ("Brasil", "CONMEBOL")}   # código FIFA -> (nome, confederação); o pacote completa com competicao.json e paises.csv


class NomeRepetido(Exception):
    """Nome de exibição que já é de um clube de outro país: o painel identifica o clube pelo nome."""


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())


def num(x: str):
    return int(x) if x not in (None, "") else None


def pacotes() -> list[str]:
    return sorted(p.parent.parent.name for p in COLETA.glob("*/pacote/competicao.json"))


def ler(pasta: Path, nome: str) -> list[dict]:
    f = pasta / nome
    return list(csv.DictReader(f.open(encoding="utf-8"))) if f.exists() else []


def apagar(b: sqlite3.Connection, cid: int) -> None:
    eds = f"SELECT edicao_id FROM edicao WHERE competicao_id = {cid}"
    pts = f"SELECT partida_id FROM partida WHERE edicao_id IN ({eds})"
    for t in ("gol", "cartao", "estatistica_partida"):
        b.execute(f"DELETE FROM {t} WHERE partida_id IN ({pts})")
    for t in ("partida", "fase", "classificacao_final", "classificacao_rodada", "tabela_publicada", "artilheiro"):
        b.execute(f"DELETE FROM {t} WHERE edicao_id IN ({eds})")
    b.execute(f"DELETE FROM edicao WHERE competicao_id = {cid}")
    b.execute(f"DELETE FROM competicao WHERE competicao_id = {cid}")


def carregar(b: sqlite3.Connection, slug: str) -> None:
    pasta = COLETA / slug / "pacote"
    comp = json.loads((pasta / "competicao.json").read_text(encoding="utf-8"))
    if "co_campeao_id" not in {c[1] for c in b.execute("PRAGMA table_info(edicao)")}:   # banco anterior à D-07
        b.execute("ALTER TABLE edicao ADD COLUMN co_campeao_id INTEGER REFERENCES clube(clube_id)")
    for col in ("pontos_empate", "pontos_derrota", "oficial"):   # banco anterior a 24/11 (pontuação 3-2-1, 4-2-1; D-10)
        if col not in {c[1] for c in b.execute("PRAGMA table_info(edicao)")}:
            b.execute(f"ALTER TABLE edicao ADD COLUMN {col} INTEGER")
    velho = b.execute("SELECT competicao_id FROM competicao WHERE slug = ?", (slug,)).fetchone()
    if velho:
        apagar(b, velho[0])
    paises = dict(PAISES)
    if comp.get("pais") and comp.get("pais_nome"):
        paises[comp["pais"]] = (comp["pais_nome"], comp.get("confederacao"))
    for r in ler(pasta, "paises.csv"):   # países dos clubes de fora (ex.: galeses na liga inglesa): codigo,nome,confederacao
        paises[r["codigo"]] = (r["nome"], r.get("confederacao") or None)
    def pais(codigo: str | None) -> int | None:
        if not codigo:
            return None
        r = b.execute("SELECT pais_id FROM pais WHERE codigo = ?", (codigo,)).fetchone()
        if r:
            return r[0]
        nome, conf = paises.get(codigo, (codigo, None))
        return b.execute("INSERT INTO pais (nome, codigo, confederacao) VALUES (?,?,?)", (nome, codigo, conf)).lastrowid
    cid = b.execute("""INSERT INTO competicao (slug, nome, nome_curto, tipo, nivel, pais_id, regiao, confederacao, observacao)
                       VALUES (?,?,?,?,?,?,?,?,?)""",
                    (slug, comp["nome"], comp.get("nome_curto"), comp["tipo"], comp.get("nivel"), pais(comp.get("pais")),
                     comp.get("regiao"), comp.get("confederacao"), comp.get("observacao"))).lastrowid

    # ---- clubes: mesmo nome de exibição = mesmo clube; o resto é novo
    clube: dict[str, int] = {}
    novos = 0
    repetidos = []
    for r in ler(pasta, "clubes.csv"):
        p = pais(r.get("pais") or comp.get("pais"))
        outro = b.execute("""SELECT pa.codigo FROM clube c LEFT JOIN pais pa USING (pais_id)
                             WHERE c.nome = ? AND c.pais_id IS NOT NULL AND c.pais_id <> ?""", (r["clube"], p)).fetchone()
        if outro:
            repetidos.append(f"{r['clube']} (já é de {outro[0]})")
            continue
        achou = b.execute("SELECT clube_id FROM clube WHERE nome = ? AND (pais_id = ? OR pais_id IS NULL)", (r["clube"], p)).fetchone()
        if achou:
            clube[r["clube"]] = achou[0]
            b.execute("UPDATE clube SET regiao = coalesce(regiao, ?), cidade = coalesce(cidade, ?) WHERE clube_id = ?",
                      (r.get("regiao") or None, r.get("cidade") or None, achou[0]))
        else:
            clube[r["clube"]] = b.execute("INSERT INTO clube (nome, pais_id, regiao, cidade) VALUES (?,?,?,?)",
                                          (r["clube"], p, r.get("regiao") or None, r.get("cidade") or None)).lastrowid
            novos += 1
        for item in filter(None, (r.get("nomes_fonte") or "").split("|")):
            fonte, resto = item.split(":", 1)
            nome_fonte, anos = resto.rsplit(":", 1) if ":" in resto else (resto, "")
            ns = re.findall(r"\d{4}", anos)   # "1997-1998", "1914 APEA-1916": só os anos
            b.execute("INSERT OR IGNORE INTO clube_nome VALUES (?,?,?,?,?,?)",
                      (clube[r["clube"]], nome_fonte, chave(nome_fonte), fonte, int(ns[0]) if ns else None, int(ns[-1]) if ns else None))
    if repetidos:
        b.rollback()
        raise NomeRepetido(f"{slug}: nome de clube que já existe em outro país (use um nome que diferencie, "
                           f"ex.: 'Liverpool de Montevideo'): " + ", ".join(repetidos))
    # nome da fonte -> clube (só os nomes que apontam para um clube só neste pacote)
    alvos: dict[str, set] = {}
    for r in ler(pasta, "clubes.csv"):
        for item in filter(None, (r.get("nomes_fonte") or "").split("|")):
            alvos.setdefault(item.split(":", 1)[1].rsplit(":", 1)[0], set()).add(clube[r["clube"]])
    sem_clube = Counter()
    def cl(nome: str) -> int | None:
        if not nome:
            return None
        if nome in clube:
            return clube[nome]
        if len(alvos.get(nome, ())) == 1:
            return next(iter(alvos[nome]))
        sem_clube[nome] += 1
        return None

    # ---- edições, fases, partidas
    ed: dict[str, int] = {}
    for r in ler(pasta, "edicoes.csv"):
        nome_of = r.get("nome_oficial") or None
        ed[r["temporada"]] = b.execute(
            """INSERT INTO edicao (competicao_id, temporada, ano_inicio, ano_fim, nome_oficial, chave, num_clubes, pontos_vitoria, pontos_empate,
                                   pontos_derrota, formato, campeao_id, vice_id, co_campeao_id, fontes, observacao, oficial)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (cid, r["temporada"], num(r["ano_inicio"]), num(r.get("ano_fim")), None if nome_of == comp["nome"] else nome_of, r["temporada"],
             num(r.get("num_clubes")), num(r.get("pontos_vitoria")), num(r.get("pontos_empate")), num(r.get("pontos_derrota")), r.get("formato") or None, cl(r.get("campeao")), cl(r.get("vice")),
             cl(r.get("co_campeao")), r.get("fontes") or None, r.get("observacao") or None,
             0 if (r.get("oficial") or "").strip().lower() in ("não", "nao", "0") else None)).lastrowid
    fase: dict[tuple, int] = {}
    for r in ler(pasta, "fases.csv"):
        fase[(r["temporada"], r["fase"])] = b.execute(
            "INSERT INTO fase (edicao_id, ordem, nome, tipo, num_grupos, formato_serie, criterio) VALUES (?,?,?,?,?,?,?)",
            (ed[r["temporada"]], num(r["ordem"]), r["fase"], r.get("tipo") or None, num(r.get("num_grupos")),
             r.get("formato_serie") or None, r.get("criterio") or None)).lastrowid
    partida: dict[str, int] = {}
    for r in ler(pasta, "partidas.csv"):
        partida[r["id"]] = b.execute(
            """INSERT INTO partida (edicao_id, fase_id, grupo, rodada, data, hora, mandante_id, visitante_id, gols_mandante, gols_visitante,
                                    penaltis_mandante, penaltis_visitante, resultado_especial, estadio, cidade, publico, gols_texto, fonte,
                                    fonte_id, observacao, arbitro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ed[r["temporada"]], fase[(r["temporada"], r["fase"])], r.get("grupo") or None, num(r.get("rodada")), r.get("data") or None,
             r.get("hora") or None, cl(r["mandante"]), cl(r["visitante"]), num(r["gols_mandante"]), num(r["gols_visitante"]),
             num(r.get("penaltis_mandante")), num(r.get("penaltis_visitante")), r.get("resultado_especial") or None, r.get("estadio") or None,
             r.get("cidade") or None, num(r.get("publico")), r.get("gols_texto") or None, r.get("fonte") or None, r.get("fonte_id") or None,
             r.get("observacao") or None, r.get("arbitro") or None)).lastrowid
    for r in ler(pasta, "gols.csv"):
        b.execute("INSERT INTO gol (partida_id, clube_id, jogador, minuto, acrescimo, tipo, fonte) VALUES (?,?,?,?,?,?,?)",
                  (partida[r["partida_id"]], cl(r["clube"]), r.get("jogador") or None, num(r.get("minuto")), num(r.get("acrescimo")),
                   r.get("tipo") or "normal", r.get("fonte") or None))
    for r in ler(pasta, "cartoes.csv"):
        b.execute("INSERT INTO cartao (partida_id, clube_id, jogador, minuto, acrescimo, cor, fonte) VALUES (?,?,?,?,?,?,?)",
                  (partida[r["partida_id"]], cl(r["clube"]), r.get("jogador") or None, num(r.get("minuto")), num(r.get("acrescimo")),
                   r.get("cor") or None, r.get("fonte") or None))

    # estatísticas de cada clube no jogo (estatisticas.csv: partida_id, clube e as colunas de estatistica_partida que tiver)
    colunas = ("chutes", "chutes_alvo", "posse", "passes", "precisao_passes", "faltas", "amarelos", "vermelhos", "impedimentos", "escanteios")
    for r in ler(pasta, "estatisticas.csv"):
        b.execute(f"INSERT OR REPLACE INTO estatistica_partida (partida_id, clube_id, {', '.join(colunas)}, fonte) VALUES ({','.join('?' * (len(colunas) + 3))})",
                  (partida[r["partida_id"]], cl(r["clube"]), *[float(r[c]) if c in ("posse", "precisao_passes") and r.get(c) else num(r.get(c)) for c in colunas],
                   r.get("fonte") or None))

    # ---- classificações, tabelas publicadas e artilheiros
    for r in ler(pasta, "classificacao_final.csv"):
        b.execute("INSERT INTO classificacao_final VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (ed[r["temporada"]], cl(r["clube"]), num(r["posicao"]), num(r.get("jogos")), num(r.get("vitorias")), num(r.get("empates")),
                   num(r.get("derrotas")), num(r.get("gols_pro")), num(r.get("gols_contra")), num(r.get("pontos")), num(r.get("ajuste_pontos")),
                   r.get("situacao") or None, r.get("fonte") or None, r.get("observacao") or None))
    # tabela rodada a rodada: uma por edição (pontos corridos). Temporada com a mesma rodada repetida para o mesmo clube
    # (uma tabela por fase) fica de fora, senão o painel a trataria como turno único
    rodadas = ler(pasta, "classificacao_rodada.csv")
    vezes = Counter((r["temporada"], r["rodada"], r["clube"]) for r in rodadas)
    por_fase = sorted({t for (t, _, _), n in vezes.items() if n > 1})
    if por_fase:
        print(f"   {slug}: tabela por rodada ignorada em {len(por_fase)} temporadas com mais de uma fase: {', '.join(por_fase[:8])}")
    for r in rodadas:
        if r["temporada"] in por_fase:
            continue
        b.execute("INSERT INTO classificacao_rodada VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                  (ed[r["temporada"]], num(r["rodada"]), cl(r["clube"]), num(r.get("posicao")), num(r.get("pontos")), num(r.get("jogos")),
                   num(r.get("vitorias")), num(r.get("empates")), num(r.get("derrotas")), num(r.get("gols_pro")), num(r.get("gols_contra")),
                   r.get("zona") or None))
    for r in ler(pasta, "tabelas_publicadas.csv"):
        b.execute("INSERT INTO tabela_publicada VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (ed[r["temporada"]], r.get("fase") or None, r.get("grupo") or None, num(r.get("posicao")),
                   cl(r["clube"]) if r.get("clube") else None, r.get("nome_fonte") or None, num(r.get("jogos")), num(r.get("vitorias")),
                   num(r.get("empates")), num(r.get("derrotas")), num(r.get("gols_pro")), num(r.get("gols_contra")), num(r.get("pontos")),
                   r.get("fonte") or None))
    for r in ler(pasta, "artilheiros.csv"):
        b.execute("INSERT INTO artilheiro VALUES (?,?,?,?,?)", (ed[r["temporada"]], r["jogador"], cl(r.get("clube")), num(r.get("gols")), r.get("fonte") or None))
    b.commit()
    conferir(b, slug, pasta, novos, sem_clube)


def conferir(b: sqlite3.Connection, slug: str, pasta: Path, novos: int, sem_clube: Counter) -> None:
    """Por edição: jogos, gols, gols com autor e campeão, banco contra pacote."""
    esperado: dict[str, list] = {}
    for r in ler(pasta, "partidas.csv"):
        e = esperado.setdefault(r["temporada"], [0, 0, 0])
        e[0] += 1
        e[1] += (num(r["gols_mandante"]) or 0) + (num(r["gols_visitante"]) or 0)
    temp_de = {r["id"]: r["temporada"] for r in ler(pasta, "partidas.csv")}
    for r in ler(pasta, "gols.csv"):
        esperado[temp_de[r["partida_id"]]][2] += 1
    campeao = {r["temporada"]: r["campeao"] for r in ler(pasta, "edicoes.csv")}
    erros = []
    for temp, eid, camp in b.execute("""SELECT e.temporada, e.edicao_id, cl.nome FROM edicao e JOIN competicao c USING (competicao_id)
                                        LEFT JOIN clube cl ON cl.clube_id = e.campeao_id WHERE c.slug = ?""", (slug,)).fetchall():
        j, g = b.execute("SELECT count(*), sum(coalesce(gols_mandante,0) + coalesce(gols_visitante,0)) FROM partida WHERE edicao_id = ?", (eid,)).fetchone()
        a = b.execute("SELECT count(*) FROM gol JOIN partida USING (partida_id) WHERE edicao_id = ?", (eid,)).fetchone()[0]
        if [j, g or 0, a] != esperado.get(temp, [0, 0, 0]) or camp != (campeao.get(temp) or None):   # edição sem campeão: vazio
            erros.append((temp, [j, g, a], esperado.get(temp), camp, campeao.get(temp)))
    sys.stdout.reconfigure(encoding="utf-8")
    n_ed, n_j = b.execute("""SELECT count(DISTINCT e.edicao_id), count(p.partida_id) FROM edicao e JOIN competicao c USING (competicao_id)
                             LEFT JOIN partida p USING (edicao_id) WHERE c.slug = ?""", (slug,)).fetchone()
    print(f"{slug}: {n_ed} edições, {n_j} jogos, {novos} clubes novos -> {'OK' if not erros and not sem_clube else 'CONFERIR'}")
    for e in erros:
        print("   diferente (temporada, banco [jogos, gols, autores], pacote, campeão no banco, no pacote):", e)
    if sem_clube:
        print("   nomes sem clube (ficaram vazios):", dict(sem_clube))


def main() -> None:
    b = sqlite3.connect(BANCO)
    b.execute("PRAGMA foreign_keys = ON")
    for slug in sys.argv[1:] or pacotes():
        carregar(b, slug)
    b.close()


if __name__ == "__main__":
    main()
