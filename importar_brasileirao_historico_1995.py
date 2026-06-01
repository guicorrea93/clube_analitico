"""Importa fases, participantes e jogos do Brasileiro 1995."""
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

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1995_partidas.csv"
SOURCE = "https://www.rsssf.org/tablesb/braz95.html"

CANONICAL.update({
    "atletico": "Atletico-MG",
    "atletico mg": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "criciuma": "Criciuma",
    "inter": "Internacional",
    "inter rs": "Internacional",
    "internacional": "Internacional",
    "paysandu": "Paysandu",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
    "sport pe": "Sport",
    "u s joao": "Uniao Sao Joao",
    "uniao s joao": "Uniao Sao Joao",
    "uniao sao joao": "Uniao Sao Joao",
})

GAME_RE = re.compile(r"^(?:\s*(\d{4})\s+)?\s*([A-Z0-9 .()]+?)\s+(\d+)\s*[xX]\s*(\d+)\s+([A-Z0-9 .()]+?)\s*$")
DATE_RE = re.compile(r"^(\d{2})/(\d{2})/(\d{2})\s+")


def parse_compact_date(token: str) -> str:
    return f"1995-{int(token[2:4]):02d}-{int(token[:2]):02d}"


def parse_slash_date(line: str) -> str | None:
    m = DATE_RE.match(line.strip())
    if not m:
        return None
    return f"19{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"


def team_name(value: str) -> str:
    clean = value.strip()
    clean = clean.replace(".", " ")
    clean = re.sub(r"\s+", " ", clean)
    clean = clean.replace("(MG)", " MG").replace("(RS)", " RS").replace("(PE)", " PE")
    return canonical_name(clean)


def parse_phase_games(block: str, fase: str, ordem: int, fase_tipo: str, expected: int, note: str = "") -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.splitlines():
        round_m = re.search(r"(?:Round|RODADA:)\s+(\d+)", line, flags=re.I)
        if round_m:
            current_round = int(round_m.group(1))
            continue
        slash_date = parse_slash_date(line)
        if slash_date:
            current_date = slash_date
            continue
        m = GAME_RE.match(line)
        if not m:
            continue
        game_no += 1
        game_date = parse_compact_date(m.group(1)) if m.group(1) else current_date
        games.append(Game(1995, fase, ordem, fase_tipo, current_round, game_no, game_date, team_name(m.group(2)), team_name(m.group(5)), int(m.group(3)), int(m.group(4)), SOURCE, note))
    if len(games) != expected:
        raise SystemExit(f"1995 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1995() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz95.html")
    serie_a = text[:text.find("Brazil 1995 Second Division")]

    first_block = serie_a[:serie_a.find("GROUP A")]
    second_block = serie_a[serie_a.find("SEGUNDO TURNO") : serie_a.find("TABELA DE CLASSIFICACAO - SEGUNDO TURNO")]
    finals_block = serie_a[serie_a.find("SEMIFINAIS E FINAL") :]

    games: list[Game] = []
    games += parse_phase_games(first_block, "Primeiro turno", 1, "liga", 132)
    games += parse_phase_games(second_block, "Segundo turno", 2, "liga", 144)
    finals = parse_phase_games(finals_block, "Semifinal", 3, "mata_mata", 6)
    semifinal_games = [replace(g, fase="Semifinal", fase_ordem=3, jogo=1 if i < 2 else 2) for i, g in enumerate(finals[:4])]
    semifinal_games = [replace(g, observacao="Botafogo e Santos classificados por melhor campanha") for g in semifinal_games]
    final_games = [replace(g, fase="Final", fase_ordem=4, jogo=1) for g in finals[4:]]
    games += semifinal_games + final_games

    participants = sorted({g.mandante for g in games[:276]} | {g.visitante for g in games[:276]})
    if len(participants) != 24:
        raise SystemExit(f"1995: esperava 24 participantes, encontrei {len(participants)}")
    if len(games) != 282:
        raise SystemExit(f"1995: esperava 282 jogos, encontrei {len(games)}")
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = 1995 AND competicao_nome = 'Campeonato Brasileiro'").fetchone()
        if not row:
            raise SystemExit("Edicao nacional 1995 nao encontrada.")
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
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 1995, ?, ?)", (edicao_id, club_id(club), SOURCE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 1995, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 1995, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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
    participants, games = parse_1995()
    import_year(participants, games)
    write_audit(games)
    print(f"1995: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
