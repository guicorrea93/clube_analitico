"""Importa fases, participantes e jogos do Brasileiro 2000 e 2001."""
from __future__ import annotations

import csv
import html
import re
import sqlite3
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "db" / "brasileirao.db"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_2000_2001_partidas.csv"


def key(value: object) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


CANONICAL = {
    "america": "America-MG",
    "america mg": "America-MG",
    "atletico mg": "Atletico-MG",
    "atletico pr": "Athletico-PR",
    "atletico paranaense": "Athletico-PR",
    "bahia": "Bahia",
    "botafogo": "Botafogo-RJ",
    "botafogo rj": "Botafogo-RJ",
    "botafogo sp": "Botafogo-SP",
    "corinthians": "Corinthians",
    "coritiba": "Coritiba",
    "cruzeiro": "Cruzeiro",
    "figueirense": "Figueirense",
    "flamengo": "Flamengo",
    "flamengo rj": "Flamengo",
    "fluminense": "Fluminense",
    "gama": "Gama",
    "goias": "Goias",
    "gremio": "Gremio",
    "guarani": "Guarani",
    "internacional": "Internacional",
    "internacional rs": "Internacional",
    "j malucelli": "J.Malucelli",
    "malutrom": "J.Malucelli",
    "juventude": "Juventude",
    "palmeiras": "Palmeiras",
    "parana": "Parana",
    "ponte preta": "Ponte Preta",
    "portuguesa": "Portuguesa",
    "remo": "Remo",
    "santa cruz": "Santa Cruz",
    "santos": "Santos",
    "sao caetano": "Sao Caetano",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
    "sport recife": "Sport",
    "vasco da gama": "Vasco",
    "vasco": "Vasco",
    "vitoria": "Vitoria",
}

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
SCORE_RE = re.compile(r"^(.+?)\s{1,}(\d+)-(\d+)\s{1,}(.+?)(?:\s+\[(.*?)\])?\s*$")


@dataclass
class Game:
    temporada: int
    fase: str
    fase_ordem: int
    fase_tipo: str
    rodada: int | None
    jogo: int | None
    data: str | None
    mandante: str
    visitante: str
    gm: int
    gv: int
    fonte: str
    observacao: str = ""


def read_pre(path: Path) -> str:
    raw = path.read_text(encoding="latin-1")
    match = re.search(r"<pre>(.*?)</pre>", raw, flags=re.S | re.I)
    if not match:
        raise SystemExit(f"Bloco <pre> nao encontrado em {path}")
    return html.unescape(match.group(1)).replace("\r\n", "\n")


def canonical_name(name: str) -> str:
    clean = re.sub(r"\s+\[.*?\]\s*$", "", name).strip()
    clean = re.sub(r"\s+\(.*?\)\s*$", "", clean).strip()
    clean = clean.replace("/", "-")
    return CANONICAL.get(key(clean), clean)


def parse_date_token(token: str, default_year: int) -> str:
    token = token.replace(",", "")
    parts = token.split()
    month, day = parts[0], int(parts[1])
    year = int(parts[2]) if len(parts) > 2 else default_year
    return f"{year}-{MONTHS[month]:02d}-{day:02d}"


def parse_table_participants(block: str, expected: int) -> list[str]:
    clubs = []
    for line in block.splitlines():
        m = re.match(r"\s*\d+\.(.+?)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s*-\s*\d+\s+\d+", line)
        if m:
            clubs.append(canonical_name(m.group(1)))
    if len(clubs) != expected:
        raise SystemExit(f"Esperava {expected} participantes, encontrei {len(clubs)}")
    return clubs


def parse_league_rounds(text: str, year: int, source: str, phase: str, expected: int) -> list[Game]:
    start = text.find("Round 1")
    end = text.find("\nTable", start)
    block = text[start:end]
    games = []
    current_round = None
    current_date = None
    game_no = 0
    for line in block.splitlines():
        round_m = re.match(r"Round\s+(\d+)", line)
        if round_m:
            current_round = int(round_m.group(1))
            current_date = None
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
        games.append(Game(year, phase, 1, "liga", current_round, game_no, current_date, canonical_name(m.group(1)), canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    if len(games) != expected:
        raise SystemExit(f"{year}: esperava {expected} jogos na primeira fase, encontrei {len(games)}")
    return games


def parse_blue_module_2000(text: str, source: str) -> tuple[list[str], list[Game]]:
    first_table = text.find("Table:", text.find("Blue Module"))
    first_date = re.search(r"^\[\w{3}\s+\d{1,2}", text[first_table:], flags=re.M)
    if not first_date:
        raise SystemExit("2000: primeira data do Modulo Azul nao encontrada")
    first_round = first_table + first_date.start()
    second_table = text.find("\nTable:", first_round)
    table_block = text[first_table:first_round]
    participants = parse_table_participants(table_block, 25)
    block = text[first_round:second_table]
    games = []
    current_date = None
    rodada = 0
    game_no = 0
    for line in block.splitlines():
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), 2000)
            rodada += 1
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game(2000, "Modulo Azul", 1, "liga", rodada, game_no, current_date, canonical_name(m.group(1)), canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    if len(games) != 300:
        raise SystemExit(f"2000: esperava 300 jogos no Modulo Azul, encontrei {len(games)}")
    return participants, games


def parse_single_match_section(block: str, year: int, source: str, fase: str, ordem: int) -> list[Game]:
    games = []
    current_date = None
    jogo = 0
    for line in block.splitlines():
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), year)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        jogo += 1
        games.append(Game(year, fase, ordem, "mata_mata", None, jogo, current_date, canonical_name(m.group(1)), canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    return games


def parse_aggregate_line_section(block: str, year: int, source: str, fase: str, ordem: int) -> list[Game]:
    dates = []
    games = []
    jogo = 0
    aggregate = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)\s*$")
    for line in block.splitlines():
        date_m = re.match(r"\[(\w{3})\s+(\d{1,2})\s+and\s+(\d{1,2})\]", line.strip())
        if date_m:
            month = date_m.group(1)
            dates = [parse_date_token(f"{month} {date_m.group(2)}", year), parse_date_token(f"{month} {date_m.group(3)}", year)]
            continue
        m = aggregate.match(line)
        if not m:
            continue
        jogo += 1
        team_a, team_b = canonical_name(m.group(1)), canonical_name(m.group(6))
        a1, b1, a2, b2 = [int(m.group(i)) for i in range(2, 6)]
        games.append(Game(year, fase, ordem, "mata_mata", None, jogo, dates[0] if dates else None, team_a, team_b, a1, b1, source))
        games.append(Game(year, fase, ordem, "mata_mata", None, jogo, dates[1] if len(dates) > 1 else None, team_b, team_a, b2, a2, source))
    return games


def parse_two_leg_blocks(block: str, year: int, source: str, fase: str, ordem: int) -> list[Game]:
    games = []
    current_date = None
    leg = 0
    jogo_by_leg = {1: 0, 2: 0}
    for line in block.splitlines():
        if re.match(r"First Legs?", line):
            leg = 1
            inline = re.search(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line)
            if inline:
                current_date = parse_date_token(inline.group(1), year)
            continue
        if re.match(r"Second Leg", line):
            leg = 2
            inline = re.search(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line)
            if inline:
                current_date = parse_date_token(inline.group(1), year)
            continue
        date_m = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if date_m:
            current_date = parse_date_token(date_m.group(1), year)
            continue
        if line.startswith(" ") or not line.strip() or " abd " in line or "aggregate winners" in line:
            continue
        m = SCORE_RE.match(line)
        if not m or leg not in (1, 2):
            continue
        jogo_by_leg[leg] += 1
        games.append(Game(year, fase, ordem, "mata_mata", None, jogo_by_leg[leg], current_date, canonical_name(m.group(1)), canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), source, m.group(5) or ""))
    return games


def parse_2001() -> tuple[list[str], list[Game]]:
    source = "https://www.rsssf.org/tablesb/braz01.html"
    text = read_pre(ROOT / "data" / "rsssf_braz01.html")
    participants = parse_table_participants(text[text.find("Table") : text.find("Round 1")], 28)
    games = parse_league_rounds(text, 2001, source, "Primeira fase", 378)
    qf = text[text.find("Quarterfinals") : text.find("Semifinals")]
    sf = text[text.find("Semifinals") : text.find("Finals")]
    fn = text[text.find("Finals") : text.find("First Leg")]
    games += parse_single_match_section(qf, 2001, source, "Quartas de final", 2)
    games += parse_single_match_section(sf, 2001, source, "Semifinal", 3)
    games += parse_aggregate_line_section(fn, 2001, source, "Final", 4)
    if len(games) != 386:
        raise SystemExit(f"2001: esperava 386 jogos, encontrei {len(games)}")
    return participants, games


def parse_2000() -> tuple[list[str], list[Game]]:
    source = "https://www.rsssf.org/tablesb/braz-joao00.html"
    text = read_pre(ROOT / "data" / "rsssf_braz_joao00.html")
    participants, games = parse_blue_module_2000(text, source)
    start = text.find("Championship Playoffs")
    end = text.find("Topscorers", start)
    block = text[start:end]
    marker_positions = {
        "1/8 Finals": re.search(r"^1/8 Finals", block, flags=re.M).start(),
        "Quarterfinals": re.search(r"^Quarterfinals", block, flags=re.M).start(),
        "Semifinals": re.search(r"^Semifinals", block, flags=re.M).start(),
        "Final": re.search(r"^Final$", block, flags=re.M).start(),
    }
    parts = [
        ("1/8 Finals", "Oitavas de final", 2, "Quarterfinals"),
        ("Quarterfinals", "Quartas de final", 3, "Semifinals"),
        ("Semifinals", "Semifinal", 4, "Final"),
        ("Final", "Final", 5, None),
    ]
    for marker, fase, ordem, next_marker in parts:
        s = marker_positions[marker]
        e = marker_positions[next_marker] if next_marker else len(block)
        games += parse_two_leg_blocks(block[s:e], 2000, source, fase, ordem)
    if len(games) != 330:
        raise SystemExit(f"2000: esperava 330 jogos, encontrei {len(games)}")
    participants = sorted(set(participants) | {g.mandante for g in games if g.fase != "Modulo Azul"} | {g.visitante for g in games if g.fase != "Modulo Azul"})
    return participants, games


def create_tables(con: sqlite3.Connection) -> None:
    from importar_brasileirao_historico_2002 import create_tables as create
    create(con)


def import_year(year: int, participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = ? AND competicao_nome = 'Campeonato Brasileiro'", (year,)).fetchone()
        if not row:
            raise SystemExit(f"Edicao nacional {year} nao encontrada.")
        edicao_id = row[0]
        ids = {row[1]: row[0] for row in con.execute("SELECT clube_id, nome FROM dim_clube")}
        missing = sorted({c for c in participants + [g.mandante for g in games] + [g.visitante for g in games] if c not in ids})
        if missing:
            raise SystemExit(f"Clubes nao encontrados em dim_clube: {missing}")
        con.execute("DELETE FROM fato_partida_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM dim_fase_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM fato_participante_nacional_historico WHERE edicao_nacional_id = ?", (edicao_id,))
        for club in participants:
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, ?, ?, ?)", (edicao_id, year, ids[club], games[0].fonte))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, ?, ?, ?, ?)", (edicao_id, year, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, year, fase_ids[g.fase], g.rodada, g.jogo, g.data, ids[g.mandante], ids[g.visitante], g.gm, g.gv, g.fonte, g.observacao),
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
    for year, parser in [(2000, parse_2000), (2001, parse_2001)]:
        participants, games = parser()
        import_year(year, participants, games)
        all_games.extend(games)
        print(f"{year}: {len(participants)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    write_audit(all_games)
    print(f"auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
