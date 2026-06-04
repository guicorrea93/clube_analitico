"""Importa fases, participantes e jogos do Brasileiro 1991.

Regulamento (RSSSF braz91): 20 clubes, turno unico (190 jogos), 4 melhores as
semifinais (ida/volta) e final (ida/volta). 2 pontos por vitoria. Sao Paulo
campeao (1-0 no agregado sobre o Bragantino). Detalhe: na 17a rodada,
Fluminense x Botafogo foi dado 1-0 pelo tribunal (abandonado em 0-0).
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

YEAR = 1991
SOURCE = "https://www.rsssf.org/tablesb/braz91.html"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1991_partidas.csv"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "atletico mineiro": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "atletico paranaense": "Athletico-PR",
    "botafogo": "Botafogo-RJ",
    "bragantino": "Bragantino",
    "goias": "Goias",
    "gremio": "Gremio",
    "nautico": "Nautico",
    "sao paulo": "Sao Paulo",
    "vasco da gama": "Vasco",
    "vitoria": "Vitoria",
})

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

SCORE_RE = re.compile(r"^(.+?)\s{2,}(\d+)-(\d+)\s{2,}(.+?)\s*$")
AWD_RE = re.compile(r"^(.+?)\s{2,}awd\s{2,}(.+?)\s{2,}\[awarded\s+(\d+)-(\d+)", re.I)
ROUND_RE = re.compile(r"^Round\s+(\d+)")
DATE_RE = re.compile(r"^\[(\w{3})\s+(\d{1,2})\]")
AGG_RE = re.compile(r"^(.+?)\s{2,}(\d+)-(\d+)\s+(\d+)-(\d+)\s{2,}(.+?)\s*$")
AGG_DATE_RE = re.compile(r"\[(\w{3})\s+(\d{1,2})\s+and\s+(?:(\w{3})\s+)?(\d{1,2})\]")


def clean_team(value: str) -> str:
    """Corta lixo de notas a direita (separadas por 2+ espacos) e canoniza."""
    head = re.split(r"\s{2,}", value.strip())[0]
    return canonical_name(head)


def ymd(month: str, day) -> str:
    return f"{YEAR}-{MONTHS[month]:02d}-{int(day):02d}"


def parse_first_phase(text: str) -> list[Game]:
    block = text[text.find("First Phase"):text.find("\nTable")]
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.split("\n"):
        rm = ROUND_RE.match(line.strip())
        if rm:
            current_round = int(rm.group(1))
            current_date = None
            continue
        dm = DATE_RE.match(line.strip())
        if dm:
            current_date = ymd(dm.group(1), dm.group(2))
            continue
        awd = AWD_RE.match(line)
        if awd:
            game_no += 1
            games.append(Game(YEAR, "Primeira fase", 1, "liga", current_round, game_no, current_date,
                              clean_team(awd.group(1)), clean_team(awd.group(2)),
                              int(awd.group(3)), int(awd.group(4)), SOURCE,
                              "Resultado dado pelo tribunal (jogo abandonado em 0-0 no 1o tempo por invasao de campo)"))
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game(YEAR, "Primeira fase", 1, "liga", current_round, game_no, current_date,
                          clean_team(m.group(1)), clean_team(m.group(4)),
                          int(m.group(2)), int(m.group(3)), SOURCE, ""))
    if len(games) != 190:
        raise SystemExit(f"1991 Primeira fase: esperava 190 jogos, encontrei {len(games)}")
    return games


def parse_two_legs(block: str, fase: str, ordem: int, expected: int) -> list[Game]:
    games: list[Game] = []
    dates: list[str] = []
    jogo = 0
    for line in block.split("\n"):
        dm = AGG_DATE_RE.search(line)
        if dm:
            m1, d1, m2, d2 = dm.group(1), dm.group(2), dm.group(3) or dm.group(1), dm.group(4)
            dates = [ymd(m1, d1), ymd(m2, d2)]
            continue
        m = AGG_RE.match(line)
        if not m:
            continue
        jogo += 1
        team_a, team_b = clean_team(m.group(1)), clean_team(m.group(6))
        a1, b1, a2, b2 = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[0] if dates else None, team_a, team_b, a1, b1, SOURCE, ""))
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[1] if len(dates) > 1 else None, team_b, team_a, b2, a2, SOURCE, ""))
    if len(games) != expected:
        raise SystemExit(f"1991 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1991() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz91.html")
    games = parse_first_phase(text)
    games += parse_two_legs(text[text.find("Semifinals"):text.find("\nFinal")], "Semifinal", 2, 4)
    games += parse_two_legs(text[text.find("\nFinal"):], "Final", 3, 2)

    participants = sorted({g.mandante for g in games[:190]} | {g.visitante for g in games[:190]})
    if len(participants) != 20:
        raise SystemExit(f"1991: esperava 20 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 196:
        raise SystemExit(f"1991: esperava 196 jogos, encontrei {len(games)}")
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
    participants, games = parse_1991()
    import_year(participants, games)
    write_audit(games)
    print(f"1991: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
