"""Importa jogos do Brasileiro 1987 conforme classificacao oficial local.

Modelagem adotada:
- Módulo Verde/Copa União completo: 16 clubes, primeira fase, semifinais e final.
- Final CBF entre os dois classificados do Módulo Amarelo: Guarani x Sport e
  Sport x Guarani. A própria RSSSF registra esses jogos como prováveis e explica
  que Flamengo/Internacional não disputaram o cruzamento imposto pela CBF.

Isso preserva a classificação final já existente no banco: Sport, Guarani,
Flamengo, Internacional e os demais 14 clubes do Módulo Verde.
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

YEAR = 1987
SOURCE = "https://www.rsssf.org/tablesb/braz87.html"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1987_partidas.csv"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "goias": "Goias",
    "vasco": "Vasco",
})

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
          "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}

DATE_RE = re.compile(r"^(\d{1,2})/([a-z]{3})/(\d{2})$", re.I)
ROUND_RE = re.compile(r"^ROUND\s+(\d+)", re.I)
SCORE_RE = re.compile(r"^([A-ZÀ-ÿ0-9 -]+?)\s+(\d+)\s+x\s+([A-ZÀ-ÿ0-9 -]+?)\s+(\d+)\s*$")


def clean_team(value: str) -> str:
    return canonical_name(value.strip())


def ymd(day, mon: str, year2: str) -> str:
    year = 1900 + int(year2)
    return f"{year}-{MONTHS[mon.lower()]:02d}-{int(day):02d}"


def parse_score_line(line: str):
    m = SCORE_RE.match(line.strip())
    if not m:
        return None
    return clean_team(m.group(1)), int(m.group(2)), clean_team(m.group(3)), int(m.group(4))


def parse_first_phase(text: str) -> list[Game]:
    block = text[text.find("FIRST PHASE"):text.find("SEMIFINALS")]
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
            current_date = ymd(dm.group(1), dm.group(2), dm.group(3))
            continue
        if s.startswith(("Goal", "Goals", "Overtime", "TEAM", "FINAL TABLE", "GROUP", "SECOND STAGE", "FIRST STAGE", "QUALIFIED")):
            continue
        parsed = parse_score_line(s)
        if not parsed:
            continue
        mand, gm, vis, gv = parsed
        game_no += 1
        games.append(Game(YEAR, "Primeira fase", 1, "liga", current_round, game_no, current_date,
                          mand, vis, gm, gv, SOURCE, "Módulo Verde/Copa União."))
    if len(games) != 120:
        raise SystemExit(f"1987 Primeira fase: esperava 120 jogos, encontrei {len(games)}")
    return games


def parse_knockout(text: str, start: str, end: str, fase: str, ordem: int, expected: int) -> list[Game]:
    block = text[text.find(start):text.find(end) if end else len(text)]
    games: list[Game] = []
    current_date = None
    jogo_por_par: dict[tuple[str, str], int] = {}
    for line in block.split("\n"):
        s = line.strip()
        dm = DATE_RE.match(s)
        if dm:
            current_date = ymd(dm.group(1), dm.group(2), dm.group(3))
            continue
        if s.startswith("Overtime:"):
            parsed_ot = parse_score_line(s.replace("Overtime:", "").strip())
            if parsed_ot and games:
                last = games[-1]
                _mand, gm_ot, _vis, gv_ot = parsed_ot
                games[-1] = replace(last, gm=last.gm + gm_ot, gv=last.gv + gv_ot,
                                    observacao=f"{last.observacao} Prorrogacao: {gm_ot}-{gv_ot}.".strip())
            continue
        parsed = parse_score_line(s)
        if not parsed:
            continue
        mand, gm, vis, gv = parsed
        key = tuple(sorted((mand, vis)))
        jogo_por_par[key] = jogo_por_par.get(key, 0) + 1
        games.append(Game(YEAR, fase, ordem, "mata_mata", None, jogo_por_par[key], current_date,
                          mand, vis, gm, gv, SOURCE, "Módulo Verde/Copa União."))
    if len(games) != expected:
        raise SystemExit(f"1987 {fase}: esperava {expected} jogos, encontrei {len(games)}")
    return games


def parse_1987() -> tuple[list[str], list[Game]]:
    text = read_pre(ROOT / "data" / "rsssf_braz87.html")
    games = parse_first_phase(text)
    games += parse_knockout(text, "SEMIFINALS", "FINAL\n", "Semifinal", 2, 4)
    games += parse_knockout(text, "FINAL\n", "CR Flamengo were", "Final Copa Uniao", 3, 2)
    games += [
        Game(YEAR, "Final CBF", 4, "mata_mata", None, 1, None, "Guarani", "Sport", 0, 0, SOURCE,
             "Final CBF entre campeoes do Modulo Amarelo; RSSSF registra placar como provavel."),
        Game(YEAR, "Final CBF", 4, "mata_mata", None, 1, None, "Sport", "Guarani", 1, 0, SOURCE,
             "Final CBF entre campeoes do Modulo Amarelo; Sport campeao oficial pela CBF."),
    ]
    participants = sorted({g.mandante for g in games} | {g.visitante for g in games})
    if len(participants) != 18:
        raise SystemExit(f"1987: esperava 18 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 128:
        raise SystemExit(f"1987: esperava 128 jogos, encontrei {len(games)}")
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
    participants, games = parse_1987()
    import_year(participants, games)
    write_audit(games)
    print(f"1987: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
