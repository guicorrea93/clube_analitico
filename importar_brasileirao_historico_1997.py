"""Importa fases, participantes e jogos do Brasileiro 1997."""
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

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1997_partidas.csv"
SOURCE = "https://www.rsssf.org/tablesb/braz97.html"

CANONICAL.update({
    "america rn": "America-RN",
    "america": "America-RN",
    "atletico mg": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "atletico paranaense": "Athletico-PR",
    "botafogo": "Botafogo-RJ",
    "criciuma": "Criciuma",
    "uniao sao joao": "União São João",
})


def parse_rounds(block: str, year: int, fase: str, fase_ordem: int, fase_tipo: str, start_game_no: int = 0) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = start_game_no
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
        m = SCORE_RE.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game(year, fase, fase_ordem, fase_tipo, current_round, game_no, current_date, canonical_name(clean_team(m.group(1))), canonical_name(clean_team(m.group(4))), int(m.group(2)), int(m.group(3)), SOURCE, m.group(5) or ""))
    return games


def parse_1997() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz97.html")
    participants = parse_table_participants(text[text.find("Table:") : text.find("Round 1")], expected=26)

    first_start = text.find("Round 1")
    first_end = text.find("\nTable:", first_start)
    first_games = parse_rounds(text[first_start:first_end], 1997, "Primeira fase", 1, "liga")
    if len(first_games) != 325:
        raise SystemExit(f"1997: esperava 325 jogos na primeira fase, encontrei {len(first_games)}")

    second_start = text.find("Second Stage:")
    final_start = text.find("Final [Dec", second_start)
    second_games = parse_rounds(text[second_start:final_start], 1997, "Grupo semifinal", 2, "grupo")
    if len(second_games) != 24:
        raise SystemExit(f"1997: esperava 24 jogos no grupo semifinal, encontrei {len(second_games)}")

    final_block = text[final_start:text.find("Topscorer", final_start)]
    final_games = parse_rounds("Round 1\n" + final_block, 1997, "Final", 3, "mata_mata")
    final_games = [replace(g, rodada=None, jogo=1, observacao=(g.observacao + "; " if g.observacao else "") + "Vasco campeao por melhor campanha") for g in final_games]
    if len(final_games) != 2:
        raise SystemExit(f"1997: esperava 2 jogos na final, encontrei {len(final_games)}")

    games = first_games + second_games + final_games
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    year = 1997
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = ? AND competicao_nome = 'Campeonato Brasileiro'", (year,)).fetchone()
        if not row:
            raise SystemExit("Edicao nacional 1997 nao encontrada.")
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
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 1997, ?, ?)", (edicao_id, club_id(club), SOURCE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 1997, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 1997, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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
    participants, games = parse_1997()
    import_year(participants, games)
    write_audit(games)
    print(f"1997: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
