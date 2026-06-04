"""Importa jogos do Brasileiro 1986 no recorte de 48 clubes usado no projeto.

A RSSSF lista tambem grupos inferiores/regionais. O banco local e a
classificacao final ja existente usam 48 clubes: os grupos A-D da primeira
fase e os quatro vencedores dos grupos E-H que entram na segunda fase
(Treze, Central, Internacional-SP e Criciuma).
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

YEAR = 1986
SOURCE = "https://www.rsssf.org/tablesb/braz86.html"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1986_partidas.csv"

CANONICAL.update({
    "america rj": "America-RJ",
    "atletico go": "Atletico-GO",
    "atletico pr": "Athletico-PR",
    "botafogo rj": "Botafogo-RJ",
    "botafogo pb": "Botafogo-PB",
    "comercial": "Comercial-MS",
    "fluminense rj": "Fluminense",
    "internacional rs": "Internacional",
    "internacional sp": "Inter de Limeira",
    "nacional": "Nacional-AM",
    "operario ms": "Operário-MS",
    "operario mt": "Operário-MT",
    "rio branco es": "Rio Branco-ES",
    "vasco da gama": "Vasco",
})

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

DATE_RE = re.compile(r"^\[(\w{3})\s+(\d{1,2})(?:\s+and\s+(?:(\w{3})\s+)?(\d{1,2})/(\d{2,4}))?\]", re.I)
ROUND_RE = re.compile(r"^Round\s+(\d+)", re.I)
SCORE_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(.+?)(?:\s+\[.*)?$")
AWD_RE = re.compile(r"^(.+?)\s+awd\s+(.+?)\s+\[victory awarded", re.I)
TWO_LEG_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)(?:\s+\[aet\s+(\d+)-(\d+)(?:,\s*pen\s+(\d+)-(\d+))?\])?\s*$", re.I)


def clean_team(value: str) -> str:
    raw = value.strip()
    if raw.startswith("Oper") and raw.endswith("-MS"):
        return "Operário-MS"
    if raw.startswith("Oper") and raw.endswith("-MT"):
        return "Operário-MT"
    if "utico" in raw:
        return "Nautico"
    return canonical_name(raw)


def ymd(month: str, day, year: int | None = None) -> str:
    mon = MONTHS[month[:3].title()]
    if year is None:
        year = 1987 if mon <= 2 else YEAR
    if year < 100:
        year += 1900
    return f"{year}-{mon:02d}-{int(day):02d}"


def parse_games_block(block: str, fase: str, ordem: int, fase_tipo: str, expected: int) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.split("\n"):
        s = line.strip()
        if not s or line.startswith(" ") or re.match(r"^\d+-", s):
            continue
        rm = ROUND_RE.match(s)
        if rm:
            current_round = int(rm.group(1))
            current_date = None
            continue
        dm = DATE_RE.match(s)
        if dm:
            current_date = ymd(dm.group(1), dm.group(2))
            continue
        if s.startswith(("Table", "Group", "Participants", "TEAM", "Central won", "Vasco da Gama protested", "It then decided", "but ")):
            continue
        awd = AWD_RE.match(s)
        if awd:
            game_no += 1
            games.append(Game(YEAR, fase, ordem, fase_tipo, current_round, game_no, current_date,
                              clean_team(awd.group(1)), clean_team(awd.group(2)), 1, 0, SOURCE,
                              "Resultado atribuido por W.O.; placar tratado como 1-0 para fechar a tabela oficial."))
            continue
        m = SCORE_RE.match(s)
        if not m:
            continue
        game_no += 1
        games.append(Game(YEAR, fase, ordem, fase_tipo, current_round, game_no, current_date,
                          clean_team(m.group(1)), clean_team(m.group(4)),
                          int(m.group(2)), int(m.group(3)), SOURCE, ""))
    if len(games) != expected:
        raise SystemExit(f"1986 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_two_legs(block: str, fase: str, ordem: int, expected: int) -> list[Game]:
    games: list[Game] = []
    dates: list[str] = []
    jogo = 0
    for line in block.split("\n"):
        s = line.strip()
        dm = DATE_RE.search(s)
        if dm:
            m1, d1, m2, d2, yy = dm.group(1), dm.group(2), dm.group(3) or dm.group(1), dm.group(4), dm.group(5)
            dates = [ymd(m1, d1, int(yy) if yy else None), ymd(m2, d2, int(yy) if yy else None)] if d2 else [ymd(m1, d1, int(yy) if yy else None)]
            continue
        m = TWO_LEG_RE.match(s)
        if not m:
            continue
        jogo += 1
        team_a, team_b = clean_team(m.group(1)), clean_team(m.group(6))
        a1, b1, a2, b2 = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
        obs2 = ""
        if m.group(7):
            a2, b2 = int(m.group(7)), int(m.group(8))
            obs2 = f"Prorrogacao: {a2}-{b2}."
            if m.group(9):
                obs2 += f" Penaltis: {m.group(9)}-{m.group(10)}."
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[0] if dates else None,
                          team_a, team_b, a1, b1, SOURCE, ""))
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[1] if len(dates) > 1 else None,
                          team_b, team_a, b2, a2, SOURCE, obs2))
    if len(games) != expected:
        raise SystemExit(f"1986 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1986() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz86.html")
    first = text[text.find("First Phase"):text.find("Group E")]
    second = text[text.find("Second Phase"):text.find("Third Phase")]
    third = text[text.find("Third Phase"):text.find("Quarterfinals")]
    quarters = text[text.find("Quarterfinals"):text.find("Semifinals")]
    semis = text[text.find("Semifinals"):text.find("Final\n")]
    final = text[text.find("Final\n"):text.find("Final Table")]

    games = parse_games_block(first, "Primeira fase", 1, "grupo", 220)
    games += parse_games_block(second, "Segunda fase", 2, "grupo", 288)
    games += parse_two_legs(third, "Terceira fase", 3, 16)
    games += parse_two_legs(quarters, "Quartas de final", 4, 8)
    games += parse_two_legs(semis, "Semifinal", 5, 4)
    games += parse_two_legs(final, "Final", 6, 2)
    participants = sorted({g.mandante for g in games} | {g.visitante for g in games})
    if len(participants) != 48:
        raise SystemExit(f"1986: esperava 48 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 538:
        raise SystemExit(f"1986: esperava 538 jogos, encontrei {len(games)}")
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
    participants, games = parse_1986()
    import_year(participants, games)
    write_audit(games)
    print(f"1986: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
