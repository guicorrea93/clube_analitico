"""Importa fases, participantes e jogos do Brasileiro 1994."""
from __future__ import annotations

import csv
import re
import sqlite3
from dataclasses import replace

from importar_brasileirao_historico_1998_1999 import norm
from importar_brasileirao_historico_2000_2001 import CANONICAL, DB, ROOT, Game, canonical_name, create_tables, read_pre

AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1994_partidas.csv"
SOURCE = "https://www.rsssf.org/tablesb/braz94.html"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "criciuma": "Criciuma",
    "gremio": "Gremio",
    "nautico": "Nautico",
    "parana": "Parana",
    "remô": "Remo",
    "remo": "Remo",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
    "uniao s joao": "Uniao Sao Joao",
    "uniao sao joao": "Uniao Sao Joao",
    "vitoria ba": "Vitoria",
})

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
X_GAME_RE = re.compile(r"^(.+?)\s+(\d+)\s+x\s+(.+?)\s+(\d+)\s*$", re.I)
KO_GAME_RE = re.compile(r"^(.+?)\s+(\d+)\s+(.+?)\s+(\d+)(?:\s+.+)?$")


def parse_date(line: str) -> str | None:
    value = line.strip()
    m = re.match(r"^(\d{1,2})/([a-z]{3})/(\d{2})$", value, flags=re.I)
    if m:
        return f"19{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})", value)
    if m:
        return f"19{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    return None


def team_name(value: str) -> str:
    clean = value.strip()
    clean = clean.replace("(MG)", " MG")
    clean = clean.replace("-BA", " BA").replace("-SP", "")
    clean = re.sub(r"\s+", " ", clean)
    return canonical_name(clean)


def parse_group_games(block: str, default_phase: str, ordem: int, expected: int) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    current_phase = default_phase
    counters: dict[str, int] = {}
    for line in block.splitlines():
        round_m = re.match(r"ROUND\s+(\d+)", line, flags=re.I)
        if round_m:
            current_round = int(round_m.group(1))
            current_phase = default_phase
            continue
        if line.strip() == "QUALIFY":
            current_phase = "Repescagem"
            continue
        if re.match(r"GROUP", line.strip(), flags=re.I):
            current_phase = default_phase
            continue
        parsed_date = parse_date(line)
        if parsed_date:
            current_date = parsed_date
            continue
        m = X_GAME_RE.match(line.strip())
        if not m:
            continue
        counters[current_phase] = counters.get(current_phase, 0) + 1
        fase_ordem = 3 if current_phase == "Repescagem" else ordem
        games.append(Game(1994, current_phase, fase_ordem, "grupo", current_round, counters[current_phase], current_date, team_name(m.group(1)), team_name(m.group(3)), int(m.group(2)), int(m.group(4)), SOURCE, ""))
    if len(games) != expected:
        raise SystemExit(f"1994 {default_phase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_knockout(block: str, fase: str, ordem: int, expected: int) -> list[Game]:
    games: list[Game] = []
    current_date = None
    pair_ids: dict[tuple[str, str], int] = {}
    next_pair = 1
    for line in block.splitlines():
        parsed_date = parse_date(line)
        if parsed_date:
            current_date = parsed_date
            continue
        m = KO_GAME_RE.match(line.strip())
        if not m:
            continue
        home, away = team_name(m.group(1)), team_name(m.group(3))
        pair_key = tuple(sorted([norm(home), norm(away)]))
        if pair_key not in pair_ids:
            pair_ids[pair_key] = next_pair
            next_pair += 1
        games.append(Game(1994, fase, ordem, "mata_mata", None, pair_ids[pair_key], current_date, home, away, int(m.group(2)), int(m.group(4)), SOURCE, ""))
    if len(games) != expected:
        raise SystemExit(f"1994 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1994() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz94.html")
    serie_a = text[:text.find("Brazil 1994 Second Division")]

    first_block = serie_a[serie_a.find("FIRST STAGE") : serie_a.find("TABLES\nFirst stage")]
    second_block = serie_a[serie_a.find("SECOND STAGE") : serie_a.find("THIRD STAGE")]
    third_block = serie_a[serie_a.find("THIRD STAGE") : serie_a.find("FINAL TABLE - 1994")]

    games = parse_group_games(first_block, "Primeira fase", 1, 120)
    second_games = parse_group_games(second_block, "Segunda fase", 2, 176)
    games += second_games

    q_start = third_block.find("Quarter-finals")
    s_start = third_block.find("SEMIFINALS")
    f_start = third_block.find("FINALS", s_start + len("SEMIFINALS"))
    games += parse_knockout(third_block[q_start:s_start], "Quartas de final", 4, 8)
    games += parse_knockout(third_block[s_start:f_start], "Semifinal", 5, 4)
    games += parse_knockout(third_block[f_start:], "Final", 6, 2)

    participants = sorted({g.mandante for g in games[:120]} | {g.visitante for g in games[:120]})
    if len(participants) != 24:
        raise SystemExit(f"1994: esperava 24 participantes, encontrei {len(participants)}")
    if len(games) != 310:
        raise SystemExit(f"1994: esperava 310 jogos, encontrei {len(games)}")
    return participants, games


def import_year(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = 1994 AND competicao_nome = 'Campeonato Brasileiro'").fetchone()
        if not row:
            raise SystemExit("Edicao nacional 1994 nao encontrada.")
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
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 1994, ?, ?)", (edicao_id, club_id(club), SOURCE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 1994, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 1994, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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
    participants, games = parse_1994()
    import_year(participants, games)
    write_audit(games)
    print(f"1994: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
