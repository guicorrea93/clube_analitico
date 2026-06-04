"""Importa fases, participantes e jogos do Brasileiro 1988.

Fonte principal: RSSSF braz88. A competicao teve 24 clubes, fase inicial com
dois estagios e pênaltis apos empates (3 pts vitoria, 2 pts vencedor dos
penaltis, 1 pt perdedor dos penaltis), seguida por quartas, semifinais e final
em ida/volta sem regra de penaltis. Bahia campeao sobre o Internacional.

Nota de curadoria: a RSSSF omite Atletico-PR 0-0 Corinthians (pen. 6-5), de
1988-10-02. O jogo foi incluido por fechamento da tabela final e cruzamento com
o calendario do Corinthians no oGol/Futebol Nacional.
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

YEAR = 1988
SOURCE = "https://www.rsssf.org/tablesb/braz88.html"
SOURCE_AUX = "https://www.ogol.com.br/equipe/corinthians/todos-os-jogos?epoca_id=117&type=season"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1988_partidas.csv"

CANONICAL.update({
    "america": "America-RJ",
    "america rj": "America-RJ",
    "atletico mg": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "bangu": "Bangu",
    "criciuma": "Criciuma",
    "vasco da gama": "Vasco",
    "vitoria": "Vitoria",
})

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

SCORE_RE = re.compile(r"^(.+?)\s+(\d+)\s*-\s*(\d+)\s+(.+?)(?:\s+\[pen\s+(\d+)\s*-\s*(\d+)\])?\s*$", re.I)
ROUND_RE = re.compile(r"^Round\s+(\d+)", re.I)
DATE_RE = re.compile(r"^\[(\w{3})\s+(\d{1,2})\]")
KO_DATE_RE = re.compile(r"\[(\w{3})\s+(\d{1,2})\s+and\s+(?:(\w{3})\s+)?(\d{1,2})/(\d{4})\]")
KO_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)(?:\s+\[aet\s+(\d+)-(\d+)\])?\s*$", re.I)


def clean_team(value: str) -> str:
    head = re.split(r"\s{2,}", value.strip())[0]
    return canonical_name(head)


def ymd(month: str, day, year: int = YEAR) -> str:
    return f"{year}-{MONTHS[month]:02d}-{int(day):02d}"


def parse_first_phase(text: str) -> list[Game]:
    block = text[text.find("First Phase"):text.find("Quarterfinals")]
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.split("\n"):
        s = line.strip()
        if not s or line.startswith(" ") or re.match(r"^\d+-", s):
            continue
        if s.startswith(("-", "*", "Note", "Table", "Group", "First", "Second", "Teams", "Final")):
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
        m = SCORE_RE.match(s)
        if not m:
            continue
        obs = f"Penaltis: {m.group(5)}-{m.group(6)}" if m.group(5) else ""
        game_no += 1
        games.append(Game(YEAR, "Primeira fase", 1, "liga", current_round, game_no, current_date,
                          clean_team(m.group(1)), clean_team(m.group(4)),
                          int(m.group(2)), int(m.group(3)), SOURCE, obs))

    games.append(Game(YEAR, "Primeira fase", 1, "liga", 6, len(games) + 1, "1988-10-02",
                      "Athletico-PR", "Corinthians", 0, 0, SOURCE_AUX,
                      "Jogo ausente na RSSSF; incluido por fechamento da tabela final. Penaltis: 6-5"))
    games.sort(key=lambda g: (g.rodada or 999, g.data or "", g.jogo or 999))
    games = [replace(g, jogo=i + 1) for i, g in enumerate(games)]
    if len(games) != 276:
        raise SystemExit(f"1988 Primeira fase: esperava 276 jogos, encontrei {len(games)}")
    return games


def parse_two_legs(block: str, fase: str, ordem: int, expected: int) -> list[Game]:
    games: list[Game] = []
    dates: list[str] = []
    jogo = 0
    for line in block.split("\n"):
        s = line.strip()
        dm = KO_DATE_RE.search(s)
        if dm:
            m1, d1, m2, d2, year = dm.group(1), dm.group(2), dm.group(3) or dm.group(1), dm.group(4), int(dm.group(5))
            dates = [ymd(m1, d1, year), ymd(m2, d2, year)]
            continue
        m = KO_RE.match(s)
        if not m:
            continue
        jogo += 1
        team_a, team_b = clean_team(m.group(1)), clean_team(m.group(6))
        a1, b1, a2, b2 = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
        obs2 = ""
        if m.group(7):
            a2 += int(m.group(7))
            b2 += int(m.group(8))
            obs2 = f"Prorrogacao: {m.group(7)}-{m.group(8)} para {team_a}."
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[0] if dates else None,
                          team_a, team_b, a1, b1, SOURCE, ""))
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo, dates[1] if len(dates) > 1 else None,
                          team_b, team_a, b2, a2, SOURCE, obs2))
    if len(games) != expected:
        raise SystemExit(f"1988 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1988() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz88.html")
    games = parse_first_phase(text)
    games += parse_two_legs(text[text.find("Quarterfinals"):text.find("Semifinals")], "Quartas de final", 2, 8)
    games += parse_two_legs(text[text.find("Semifinals"):text.find("Finals")], "Semifinal", 3, 4)
    games += parse_two_legs(text[text.find("Finals"):], "Final", 4, 2)
    participants = sorted({g.mandante for g in games[:276]} | {g.visitante for g in games[:276]})
    if len(participants) != 24:
        raise SystemExit(f"1988: esperava 24 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 290:
        raise SystemExit(f"1988: esperava 290 jogos, encontrei {len(games)}")
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
    participants, games = parse_1988()
    import_year(participants, games)
    write_audit(games)
    print(f"1988: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
