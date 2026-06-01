"""Importa fases, participantes e jogos do Brasileiro 1996."""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import replace

from importar_brasileirao_historico_1998_1999 import clean_team, norm
from importar_brasileirao_historico_2000_2001 import (
    CANONICAL,
    DB,
    ROOT,
    Game,
    SCORE_RE,
    canonical_name,
    create_tables,
    parse_date_token,
    parse_table_participants,
    read_pre,
)

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1996_partidas.csv"
SOURCE = "https://www.rsssf.org/tablesb/braz96.html"

CANONICAL.update({
    "atletico mineiro": "Atletico-MG",
    "atletico paranaense": "Athletico-PR",
    "atletico pr": "Athletico-PR",
    "botafogo": "Botafogo-RJ",
    "criciuma": "Criciuma",
    "gremio": "Gremio",
    "parana": "Parana",
    "sao paulo": "Sao Paulo",
    "sport club recife": "Sport",
})


def parse_rounds(block: str) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.splitlines():
        round_m = re.match(r"Round\s+(\d+)(?:\s+\[(.*?)\])?", line)
        if round_m:
            current_round = int(round_m.group(1))
            current_date = parse_date_token(round_m.group(2).split(",")[0], 1996) if round_m.group(2) else None
            continue
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), 1996)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game(1996, "Primeira fase", 1, "liga", current_round, game_no, current_date, canonical_name(clean_team(m.group(1))), canonical_name(clean_team(m.group(4))), int(m.group(2)), int(m.group(3)), SOURCE, m.group(5) or ""))
    return games


def date_from_header(header: str, leg: int) -> str | None:
    m = re.search(r"1st leg ([A-Z][a-z]{2} \d{1,2})(?:,\d{1,2})?; 2nd leg ([A-Z][a-z]{2} \d{1,2})(?:, [A-Z][a-z]{2} \d{1,2})?", header)
    if not m:
        return None
    token = m.group(1 if leg == 1 else 2)
    return parse_date_token(token, 1996)


def parse_two_leg_compact(block: str, fase: str, ordem: int, criterion_note: str = "") -> list[Game]:
    games: list[Game] = []
    header = block.splitlines()[0] if block.splitlines() else ""
    first_date = date_from_header(header, 1)
    second_date = date_from_header(header, 2)
    pair_no = 0
    pattern = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)\s*$")
    for line in block.splitlines()[1:]:
        if not line.strip():
            continue
        m = pattern.match(line)
        if not m:
            continue
        pair_no += 1
        team_a = canonical_name(clean_team(m.group(1)))
        team_b = canonical_name(clean_team(m.group(6)))
        obs = criterion_note if criterion_note else ""
        games.append(Game(1996, fase, ordem, "mata_mata", None, pair_no, first_date, team_a, team_b, int(m.group(2)), int(m.group(3)), SOURCE, obs))
        games.append(Game(1996, fase, ordem, "mata_mata", None, pair_no, second_date, team_b, team_a, int(m.group(5)), int(m.group(4)), SOURCE, obs))
    return games


def section(text: str, start_marker: str, end_marker: str | None = None) -> str:
    start = re.search(start_marker, text, flags=re.M)
    if not start:
        raise SystemExit(f"Secao nao encontrada: {start_marker}")
    if not end_marker:
        return text[start.start():]
    end = re.search(end_marker, text[start.end():], flags=re.M)
    return text[start.start(): start.end() + end.start()] if end else text[start.start():]


def parse_1996() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz96.html")
    first_start = text.find("Round 1")
    first_end = text.find("\nTable:", first_start)
    first_games = parse_rounds(text[first_start:first_end])
    if len(first_games) != 276:
        raise SystemExit(f"1996: esperava 276 jogos na primeira fase, encontrei {len(first_games)}")
    participants = sorted({g.mandante for g in first_games} | {g.visitante for g in first_games})
    if len(participants) != 24:
        raise SystemExit(f"1996: esperava 24 participantes, encontrei {len(participants)}")

    play = text[text.find("Quarterfinals") : text.find("Scorers")]
    games = first_games
    games += parse_two_leg_compact(section(play, r"^Quarterfinals", r"^Semifinals"), "Quartas de final", 2)
    games += parse_two_leg_compact(section(play, r"^Semifinals", r"^FINAL"), "Semifinal", 3)
    games += parse_two_leg_compact(section(play, r"^FINAL", None), "Final", 4, "Gremio campeao por melhor campanha")
    if len(games) != 290:
        raise SystemExit(f"1996: esperava 290 jogos, encontrei {len(games)}")
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = 1996 AND competicao_nome = 'Campeonato Brasileiro'").fetchone()
        if not row:
            raise SystemExit("Edicao nacional 1996 nao encontrada.")
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
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 1996, ?, ?)", (edicao_id, club_id(club), SOURCE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 1996, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 1996, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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
    participants, games = parse_1996()
    import_year(participants, games)
    write_audit(games)
    print(f"1996: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
