"""Importa fases, participantes e jogos do Brasileiro 1992."""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import replace

from importar_brasileirao_historico_1998_1999 import norm
from importar_brasileirao_historico_2000_2001 import CANONICAL, DB, ROOT, Game, canonical_name, create_tables, read_pre

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1992_partidas.csv"
SOURCE = "https://www.rsssf.org/tablesb/braz92.html"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "botafogo": "Botafogo-RJ",
    "goias": "Goias",
    "nautico": "Nautico",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
})

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
GAME_RE = re.compile(r"^(.+?)\s+(\d+)\s+x\s+(.+?)\s+(\d+)\s*$", re.I)


def parse_date(line: str) -> str | None:
    m = re.match(r"^(\d{1,2})/([a-z]{3})/(\d{2})$", line.strip(), flags=re.I)
    if not m:
        return None
    return f"19{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"


def team_name(value: str) -> str:
    clean = value.strip()
    return canonical_name(re.sub(r"\s+", " ", clean))


def parse_games(block: str, fase: str, ordem: int, fase_tipo: str, expected: int) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.splitlines():
        round_m = re.match(r"ROUND\s+(\d+)", line, flags=re.I)
        if round_m:
            current_round = int(round_m.group(1))
            continue
        parsed_date = parse_date(line)
        if parsed_date:
            current_date = parsed_date
            continue
        m = GAME_RE.match(line.strip())
        if not m:
            continue
        game_no += 1
        games.append(Game(1992, fase, ordem, fase_tipo, current_round, game_no, current_date, team_name(m.group(1)), team_name(m.group(3)), int(m.group(2)), int(m.group(4)), SOURCE, ""))
    if len(games) != expected:
        raise SystemExit(f"1992 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1992() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz92.html")
    first_start = text.find("FIRST PHASE")
    first_end = text.find("FINAL TABLE - FIRST PHASE")
    second_start = text.find("SECOND PHASE", first_end)
    second_end = text.find("FINAL TABLE - SECOND PHASE")
    finals_start = text.find("FINALS", second_end)
    finals_end = text.find("CR FLAMENGO", finals_start)

    games: list[Game] = []
    games += parse_games(text[first_start:first_end], "Primeira fase", 1, "liga", 190)
    games += parse_games(text[second_start:second_end], "Segunda fase", 2, "grupo", 24)
    games += parse_games(text[finals_start:finals_end], "Final", 3, "mata_mata", 2)

    participants = sorted({g.mandante for g in games[:190]} | {g.visitante for g in games[:190]})
    if len(participants) != 20:
        raise SystemExit(f"1992: esperava 20 participantes, encontrei {len(participants)}")
    if len(games) != 216:
        raise SystemExit(f"1992: esperava 216 jogos, encontrei {len(games)}")
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = 1992 AND competicao_nome = 'Campeonato Brasileiro'").fetchone()
        if not row:
            raise SystemExit("Edicao nacional 1992 nao encontrada.")
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
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 1992, ?, ?)", (edicao_id, club_id(club), SOURCE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 1992, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 1992, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, fase_ids[g.fase], g.rodada, g.jogo, g.data, club_id(g.mandante), club_id(g.visitante), g.gm, g.gv, g.fonte, g.observacao),
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
    participants, games = parse_1992()
    import_year(participants, games)
    write_audit(games)
    print(f"1992: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
