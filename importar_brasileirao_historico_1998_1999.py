"""Importa fases, participantes e jogos do Brasileiro 1998 e 1999."""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import replace
from pathlib import Path

from importar_brasileirao_historico_2000_2001 import (
    AUDIT_CSV as _AUDIT_OLD,
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

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1998_1999_partidas.csv"

CANONICAL.update({
    "america": "America-MG",
    "america mg": "America-MG",
    "bragantino": "Bragantino",
    "brangantino": "Bragantino",
    "criciuma": "Criciuma",
    "uniao sao joao": "União São João",
    "uniao s joao": "União São João",
})


def norm(value: str) -> str:
    from importar_brasileirao_historico_2000_2001 import key
    return key(value)


def clean_team(value: str) -> str:
    return re.sub(r"\s{2,}.*$", "", value).strip()


def parse_league(text: str, year: int, source: str, expected: int) -> tuple[list[str], list[Game]]:
    participants = parse_table_participants(text[text.find("Table") : text.find("Round 1")], expected=expected)
    start = text.find("Round 1")
    end = text.find("\nTable", start)
    block = text[start:end]
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.splitlines():
        round_m = re.match(r"Round\s+(\d+)(?:\s+\[(.*?)\])?", line)
        if round_m:
            current_round = int(round_m.group(1))
            current_date = parse_date_token(round_m.group(2).split(",")[0], year) if round_m.group(2) else None
            continue
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), year)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        abd_m = re.match(r"^(.+?)\s+abd\s+(.+?)\s+\[abandoned at\s+(\d+)-(\d+)", line)
        if abd_m:
            game_no += 1
            games.append(Game(year, "Primeira fase", 1, "liga", current_round, game_no, current_date, canonical_name(abd_m.group(1)), canonical_name(abd_m.group(2)), int(abd_m.group(3)), int(abd_m.group(4)), source, "abandoned; result apparently stood"))
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game(year, "Primeira fase", 1, "liga", current_round, game_no, current_date, canonical_name(clean_team(m.group(1))), canonical_name(clean_team(m.group(4))), int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    expected_games = expected * (expected - 1) // 2
    if len(games) != expected_games:
        raise SystemExit(f"{year}: esperava {expected_games} jogos na primeira fase, encontrei {len(games)}")
    return participants, games


def section(text: str, start_marker: str, end_marker: str | None = None) -> str:
    start = re.search(start_marker, text, flags=re.M)
    if not start:
        raise SystemExit(f"Secao nao encontrada: {start_marker}")
    if end_marker:
        end = re.search(end_marker, text[start.end():], flags=re.M)
        return text[start.start(): start.end() + end.start()] if end else text[start.start():]
    return text[start.start():]


def parse_best_of_series(block: str, year: int, source: str, fase: str, ordem: int) -> list[Game]:
    games: list[Game] = []
    current_date = None
    pair_ids: dict[tuple[str, str], int] = {}
    next_pair = 1
    for line in block.splitlines():
        leg_m = re.match(r"(First|Second|Third) Legs?\s*(?:\[(.*?)\])?", line.strip())
        if leg_m:
            current_date = parse_date_token(leg_m.group(2), year) if leg_m.group(2) else current_date
            continue
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), year)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        home, away = canonical_name(m.group(1)), canonical_name(m.group(4))
        pair_key = tuple(sorted([norm(home), norm(away)]))
        if pair_key not in pair_ids:
            pair_ids[pair_key] = next_pair
            next_pair += 1
        games.append(Game(year, fase, ordem, "mata_mata", None, pair_ids[pair_key], current_date, home, away, int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    return games


def parse_1999() -> tuple[list[str], list[Game]]:
    year = 1999
    source = "https://www.rsssf.org/tablesb/braz99.html"
    text = read_pre(ROOT / "data" / "rsssf_braz99.html")
    participants, games = parse_league(text, year, source, 22)
    play = section(text, r"^Championship Playoff", r"^M.dias de rebaixamento")
    games += parse_best_of_series(section(play, r"^First Round", r"^Second Round"), year, source, "Quartas de final", 2)
    games += parse_best_of_series(section(play, r"^Second Round", r"^Final$"), year, source, "Semifinal", 3)
    games += parse_best_of_series(section(play, r"^Final$", None), year, source, "Final", 4)
    if len(games) != 250:
        raise SystemExit(f"1999: esperava 250 jogos, encontrei {len(games)}")
    return participants, games


def parse_1998() -> tuple[list[str], list[Game]]:
    year = 1998
    source = "https://www.rsssf.org/tablesb/braz98.html"
    text = read_pre(ROOT / "data" / "rsssf_braz98.html")
    participants, games = parse_league(text, year, source, 24)
    play = section(text, r"^Championship Playoff", r"^Topscorers")
    games += parse_best_of_series(section(play, r"^Quarterfinals", r"^Semifinals"), year, source, "Quartas de final", 2)
    games += parse_best_of_series(section(play, r"^Semifinals", r"^Final$"), year, source, "Semifinal", 3)
    games += parse_best_of_series(section(play, r"^Final$", None), year, source, "Final", 4)
    if len(games) != 297:
        raise SystemExit(f"1998: esperava 297 jogos, encontrei {len(games)}")
    return participants, games


def import_year(year: int, participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = ? AND competicao_nome = 'Campeonato Brasileiro'", (year,)).fetchone()
        if not row:
            raise SystemExit(f"Edicao nacional {year} nao encontrada.")
        edicao_id = row[0]
        rows = con.execute("SELECT clube_id, nome FROM dim_clube").fetchall()
        by_name = {name: cid for cid, name in rows}
        by_key = {norm(name): (cid, name) for cid, name in rows}

        def club_id(name: str) -> int:
            if name in by_name:
                return by_name[name]
            k = norm(name)
            if k in by_key:
                return by_key[k][0]
            raise SystemExit(f"Clube nao encontrado em dim_clube: {name}")

        def canonical_db_name(name: str) -> str:
            if name in by_name:
                return name
            k = norm(name)
            if k in by_key:
                return by_key[k][1]
            return name

        participants = sorted({canonical_db_name(c) for c in participants})
        games = [replace(g, mandante=canonical_db_name(g.mandante), visitante=canonical_db_name(g.visitante)) for g in games]

        con.execute("DELETE FROM fato_partida_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM dim_fase_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM fato_participante_nacional_historico WHERE edicao_nacional_id = ?", (edicao_id,))
        for club in participants:
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, ?, ?, ?)", (edicao_id, year, club_id(club), games[0].fonte))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, ?, ?, ?, ?)", (edicao_id, year, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, year, fase_ids[g.fase], g.rodada, g.jogo, g.data, club_id(g.mandante), club_id(g.visitante), g.gm, g.gv, g.fonte, g.observacao),
            )
        con.commit()
    finally:
        con.close()


def write_audit(all_games: list[Game]) -> None:
    with AUDIT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["temporada", "fase", "rodada", "jogo", "data", "mandante", "placar", "visitante", "observacao", "fonte"]
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        writer.writeheader()
        for g in all_games:
            writer.writerow({"temporada": g.temporada, "fase": g.fase, "rodada": g.rodada or "", "jogo": g.jogo or "", "data": g.data or "", "mandante": g.mandante, "placar": f"{g.gm}-{g.gv}", "visitante": g.visitante, "observacao": g.observacao, "fonte": g.fonte})


def main() -> None:
    all_games = []
    for year, parser in [(1998, parse_1998), (1999, parse_1999)]:
        participants, games = parser()
        import_year(year, participants, games)
        all_games.extend(games)
        print(f"{year}: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    write_audit(all_games)
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
