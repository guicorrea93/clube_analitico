"""Importa fases, participantes e jogos do Brasileiro 1989.

Fonte principal: RSSSF braz89. O bloco de 1st LEVEL contem a Serie A; a mesma
pagina tambem traz a 2a divisao, por isso o parser corta antes de "CAMPEONATO
BRASILEIRO 1989".

Regulamento resumido: 22 clubes; primeira fase em dois grupos de 11 (8
classificados por grupo); segunda fase com 16 clubes em dois grupos cruzados,
com Sao Paulo e Vasco indo a final; torneio de rebaixamento entre 5 clubes
apos a eliminacao do Coritiba; final decidida em jogo unico porque o Vasco
entrou com ponto bonus e venceu o Sao Paulo por 1-0. 2 pontos por vitoria.

Notas de curadoria:
- A fonte RSSSF lista "Bahia 0-0 Vitoria" na 1a rodada do torneio de
  rebaixamento, mas a tabela final e fontes cruzadas de jogos apontam
  "Bahia 0-0 Guarani".
- A fonte RSSSF omite "Guarani 0-0 Athletico-PR" em 1989-11-22; o jogo e
  necessario para fechar a tabela do torneio de rebaixamento e aparece em
  fontes cruzadas de calendario do Guarani.
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

YEAR = 1989
SOURCE = "https://www.rsssf.org/tablesb/braz89.html"
SOURCE_AUX = "https://rsssfbrasil.com/tablesae/br1989.htm"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_1989_partidas.csv"

CANONICAL.update({
    "atletico mg": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "botafogo": "Botafogo-RJ",
    "internacional sp": "Inter de Limeira",
    "internacional rs": "Internacional",
    "nautico": "Nautico",
    "vasco da gama": "Vasco",
    "vitoria": "Vitoria",
})

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

SCORE_RE = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(.+?)\s*$")
AWARDED_RE = re.compile(r"^(.+?)\s+dns\s+(.+?)\s+\[awarded\s+(\d+)-(\d+)", re.I)
ROUND_RE = re.compile(r"^Round\s+(\d+)", re.I)
DATE_RE = re.compile(r"^\[(\w{3})\s+(\d{1,2})\]")


def clean_team(value: str) -> str:
    head = re.split(r"\s{2,}", value.strip())[0]
    return canonical_name(head)


def ymd(month: str, day) -> str:
    return f"{YEAR}-{MONTHS[month]:02d}-{int(day):02d}"


def read_serie_a_text() -> str:
    text = read_pre(ROOT / "data" / "rsssf_braz89.html")
    end = text.find("CAMPEONATO BRASILEIRO 1989")
    if end == -1:
        raise SystemExit("1989: nao encontrei corte antes da 2a divisao.")
    return text[:end]


def parse_games_block(block: str, fase: str, ordem: int, fase_tipo: str) -> list[Game]:
    games: list[Game] = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.split("\n"):
        s = line.strip()
        if not s:
            continue
        if re.match(r"^\d+-", s):
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
        if line.startswith(" "):
            continue
        awd = AWARDED_RE.match(s)
        if awd:
            game_no += 1
            games.append(Game(YEAR, fase, ordem, fase_tipo, current_round, game_no, current_date,
                              clean_team(awd.group(1)), clean_team(awd.group(2)),
                              int(awd.group(3)), int(awd.group(4)), SOURCE,
                              "Resultado atribuido por W.O.; Coritiba nao compareceu e foi eliminado."))
            continue
        m = SCORE_RE.match(s)
        if not m:
            continue
        mand, vis = clean_team(m.group(1)), clean_team(m.group(4))
        obs = ""
        if fase == "Torneio de rebaixamento" and current_round == 1 and mand == "Bahia" and vis == "Vitoria" and m.group(2) == "0" and m.group(3) == "0":
            vis = "Guarani"
            obs = "Fonte RSSSF traz Vitoria por engano; corrigido para Guarani por cruzamento com tabela final e calendarios externos."
        game_no += 1
        games.append(Game(YEAR, fase, ordem, fase_tipo, current_round, game_no, current_date,
                          mand, vis, int(m.group(2)), int(m.group(3)), SOURCE, obs))
    return games


def parse_final(block: str) -> list[Game]:
    current_date = None
    for line in block.split("\n"):
        s = line.strip()
        dm = DATE_RE.match(s)
        if dm:
            current_date = ymd(dm.group(1), dm.group(2))
            continue
        m = SCORE_RE.match(s)
        if m:
            return [Game(YEAR, "Final", 4, "mata_mata", None, 1, current_date,
                         clean_team(m.group(1)), clean_team(m.group(4)),
                         int(m.group(2)), int(m.group(3)), SOURCE,
                         "Final em jogo unico; Vasco entrou com ponto bonus e foi campeao ao vencer.")]
    raise SystemExit("1989 Final: placar nao encontrado.")


def parse_1989() -> tuple[list[str], list[Game]]:
    text = read_serie_a_text()
    first = text[text.find("First Phase"):text.find("Second Phase")]
    second = text[text.find("Second Phase"):text.find("Relegation Tournament")]
    releg = text[text.find("Relegation Tournament"):text.find("<strong>Final")]
    final = text[text.find("<strong>Final"):]

    games = parse_games_block(first, "Primeira fase", 1, "grupo")
    games += parse_games_block(second, "Segunda fase", 2, "grupo")
    releg_games = parse_games_block(releg, "Torneio de rebaixamento", 3, "grupo")
    releg_games.append(Game(YEAR, "Torneio de rebaixamento", 3, "grupo", 5, len(releg_games) + 1, "1989-11-22",
                            "Guarani", "Athletico-PR", 0, 0, SOURCE_AUX,
                            "Jogo ausente no bloco RSSSF principal; incluido por cruzamento com tabela final e calendario externo."))
    games += releg_games
    games += parse_final(final)

    expected = {"Primeira fase": 110, "Segunda fase": 64, "Torneio de rebaixamento": 20, "Final": 1}
    for fase, qtd in expected.items():
        found = sum(1 for g in games if g.fase == fase)
        if found != qtd:
            raise SystemExit(f"1989 {fase}: esperava {qtd} jogos, encontrei {found}")
    participants = sorted({g.mandante for g in games} | {g.visitante for g in games})
    if len(participants) != 22:
        raise SystemExit(f"1989: esperava 22 participantes, encontrei {len(participants)}: {participants}")
    if len(games) != 195:
        raise SystemExit(f"1989: esperava 195 jogos, encontrei {len(games)}")
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
    participants, games = parse_1989()
    import_year(participants, games)
    write_audit(games)
    print(f"1989: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
