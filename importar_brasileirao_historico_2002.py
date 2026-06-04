"""Importa fases, participantes e jogos do Brasileiro de 2002."""
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
SOURCE = ROOT / "data" / "rsssf_braz02.html"
AUDIT_CSV = ROOT / "data" / "brasileirao_historico_2002_partidas.csv"
FONTE = "https://www.rsssf.org/tablesb/braz02.html"


def key(value: object) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


CANONICAL = {
    "atletico mg": "Atletico-MG", "atletico mineiro": "Atletico-MG",
    "atletico pr": "Athletico-PR", "atletico paranaense": "Athletico-PR",
    "athletico pr": "Athletico-PR", "bahia": "Bahia",
    "botafogo": "Botafogo-RJ", "botafogo rj": "Botafogo-RJ",
    "corinthians": "Corinthians", "coritiba": "Coritiba",
    "cruzeiro": "Cruzeiro", "figueirense": "Figueirense",
    "flamengo": "Flamengo", "fluminense": "Fluminense",
    "gama": "Gama", "goias": "Goias", "gremio": "Gremio",
    "guarani": "Guarani", "internacional": "Internacional",
    "juventude": "Juventude", "palmeiras": "Palmeiras",
    "parana": "Parana", "paysandu": "Paysandu",
    "ponte preta": "Ponte Preta", "portuguesa": "Portuguesa",
    "santos": "Santos", "sao caetano": "Sao Caetano",
    "sao paulo": "Sao Paulo", "vasco da gama": "Vasco",
    "vasco": "Vasco", "vitoria": "Vitoria",
}
MONTHS = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}


@dataclass
class Game:
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
    observacao: str = ""


def read_source() -> str:
    raw = SOURCE.read_text(encoding="latin-1")
    match = re.search(r"<pre>(.*?)</pre>", raw, flags=re.S | re.I)
    if not match:
        raise SystemExit("Bloco <pre> nao encontrado em data/rsssf_braz02.html")
    return html.unescape(match.group(1)).replace("\r\n", "\n")


def parse_date(token: str, year: int = 2002) -> str:
    month, day = token.split()
    return f"{year}-{MONTHS[month]}-{int(day):02d}"


def canonical_name(name: str) -> str:
    clean = re.sub(r"\s+\[.*?\]\s*$", "", name).strip()
    clean = clean.replace("Botafogo-RJ", "Botafogo")
    return CANONICAL.get(key(clean), clean)


def parse_participants(text: str) -> list[str]:
    block = text[text.find("Table") : text.find("Round 1")]
    clubs = []
    for line in block.splitlines():
        m = re.match(r"\s*\d+\.(.+?)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+-\d+\s+\d+", line)
        if m:
            clubs.append(canonical_name(m.group(1)))
    if len(clubs) != 26:
        raise SystemExit(f"Esperava 26 participantes em 2002, encontrei {len(clubs)}")
    return clubs


def parse_first_phase(text: str) -> list[Game]:
    start = text.find("Round 1")
    end = text.find("\nTable", start)
    block = text[start:end]
    games = []
    current_round = None
    current_date = None
    game_no = 0
    pattern = re.compile(r"^(.+?)\s{2,}(\d+)-(\d+)\s{2,}(.+?)(?:\s+\[(.*?)\])?\s*$")
    for line in block.splitlines():
        round_m = re.match(r"Round\s+(\d+)", line)
        if round_m:
            current_round = int(round_m.group(1))
            current_date = None
            continue
        date_m = re.match(r"\[(\w{3}\s+\d{1,2})\]", line.strip())
        if date_m:
            current_date = parse_date(date_m.group(1))
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = pattern.match(line)
        if not m:
            continue
        game_no += 1
        games.append(Game("Primeira fase", 1, "liga", current_round, game_no, current_date, canonical_name(m.group(1)), canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), m.group(5) or ""))
    if len(games) != 325:
        raise SystemExit(f"Esperava 325 jogos na primeira fase de 2002, encontrei {len(games)}")
    return games


def parse_playoffs(text: str) -> list[Game]:
    labels = [("Quarterfinals", "Quartas de final", 2), ("Semi-finals", "Semifinal", 3), ("Finals", "Final", 4)]
    games = []
    aggregate = re.compile(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)\s*$")
    for idx, (marker, fase, ordem) in enumerate(labels):
        start = text.find(marker)
        next_start = text.find(labels[idx + 1][0]) if idx + 1 < len(labels) else text.find("First Leg")
        block = text[start:next_start]
        dates = []
        jogo = 0
        for line in block.splitlines():
            date_m = re.match(r"\[(\w{3})\s+(\d{1,2})\s+and\s+(\d{1,2})\]", line.strip())
            if date_m:
                month = date_m.group(1)
                dates = [parse_date(f"{month} {date_m.group(2)}"), parse_date(f"{month} {date_m.group(3)}")]
                continue
            if line.startswith(" ") or not line.strip():
                continue
            m = aggregate.match(line)
            if not m:
                continue
            team_a = canonical_name(m.group(1))
            team_b = canonical_name(m.group(6))
            a1, b1, a2, b2 = [int(m.group(i)) for i in range(2, 6)]
            jogo += 1
            games.append(Game(fase, ordem, "mata_mata", None, jogo, dates[0] if dates else None, team_a, team_b, a1, b1))
            games.append(Game(fase, ordem, "mata_mata", None, jogo, dates[1] if len(dates) > 1 else None, team_b, team_a, b2, a2))
    if len(games) != 14:
        raise SystemExit(f"Esperava 14 jogos no mata-mata de 2002, encontrei {len(games)}")
    return games


def create_tables(con: sqlite3.Connection) -> None:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS fato_participante_nacional_historico (
        edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
        temporada_id INTEGER NOT NULL,
        clube_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        fonte TEXT,
        observacao TEXT,
        PRIMARY KEY (edicao_nacional_id, clube_id)
    );
    CREATE TABLE IF NOT EXISTS dim_fase_nacional_historica (
        fase_nacional_id INTEGER PRIMARY KEY AUTOINCREMENT,
        edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
        temporada_id INTEGER NOT NULL,
        fase_ordem INTEGER NOT NULL,
        fase_nome TEXT NOT NULL,
        fase_tipo TEXT,
        num_grupos INTEGER,
        formato_serie TEXT,
        criterio TEXT,
        observacao TEXT,
        UNIQUE (edicao_nacional_id, fase_nome)
    );
    CREATE TABLE IF NOT EXISTS fato_partida_nacional_historica (
        partida_hist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
        temporada_id INTEGER NOT NULL,
        fase_nacional_id INTEGER NOT NULL REFERENCES dim_fase_nacional_historica(fase_nacional_id),
        rodada INTEGER,
        jogo INTEGER,
        grupo TEXT,
        data TEXT,
        mandante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        visitante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        gols_mandante INTEGER NOT NULL,
        gols_visitante INTEGER NOT NULL,
        fonte TEXT,
        observacao TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_participante_hist_temp ON fato_participante_nacional_historico(temporada_id);
    CREATE INDEX IF NOT EXISTS idx_fase_hist_temp ON dim_fase_nacional_historica(temporada_id, fase_ordem);
    CREATE INDEX IF NOT EXISTS idx_partida_hist_temp ON fato_partida_nacional_historica(temporada_id, fase_nacional_id);
    CREATE INDEX IF NOT EXISTS idx_partida_hist_clubes ON fato_partida_nacional_historica(mandante_id, visitante_id);
    """)


def require_club(mapping: dict[str, int], name: str) -> int:
    if name not in mapping:
        raise SystemExit(f"Clube nao encontrado em dim_clube: {name}")
    return mapping[name]


def import_data(participants: list[str], games: list[Game]) -> None:
    con = sqlite3.connect(DB)
    try:
        create_tables(con)
        row = con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional WHERE temporada_id = 2002 AND competicao_nome = 'Campeonato Brasileiro'").fetchone()
        if not row:
            raise SystemExit("Edicao nacional 2002 nao encontrada. Importe a classificacao historica antes.")
        edicao_id = row[0]
        ids = {row[1]: row[0] for row in con.execute("SELECT clube_id, nome FROM dim_clube")}
        con.execute("DELETE FROM fato_partida_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM dim_fase_nacional_historica WHERE edicao_nacional_id = ?", (edicao_id,))
        con.execute("DELETE FROM fato_participante_nacional_historico WHERE edicao_nacional_id = ?", (edicao_id,))
        for club in participants:
            con.execute("INSERT INTO fato_participante_nacional_historico (edicao_nacional_id, temporada_id, clube_id, fonte) VALUES (?, 2002, ?, ?)", (edicao_id, require_club(ids, club), FONTE))
        fase_ids = {}
        for g in games:
            if g.fase not in fase_ids:
                con.execute("INSERT INTO dim_fase_nacional_historica (edicao_nacional_id, temporada_id, fase_ordem, fase_nome, fase_tipo) VALUES (?, 2002, ?, ?, ?)", (edicao_id, g.fase_ordem, g.fase, g.fase_tipo))
                fase_ids[g.fase] = con.execute("SELECT last_insert_rowid()").fetchone()[0]
            con.execute(
                "INSERT INTO fato_partida_nacional_historica (edicao_nacional_id, temporada_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, observacao) VALUES (?, 2002, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (edicao_id, fase_ids[g.fase], g.rodada, g.jogo, g.data, require_club(ids, g.mandante), require_club(ids, g.visitante), g.gm, g.gv, FONTE, g.observacao),
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
            writer.writerow({"temporada": 2002, "fase": g.fase, "rodada": g.rodada or "", "jogo": g.jogo or "", "data": g.data or "", "mandante": g.mandante, "placar": f"{g.gm}-{g.gv}", "visitante": g.visitante, "observacao": g.observacao, "fonte": FONTE})


def main() -> None:
    text = read_source()
    participants = parse_participants(text)
    games = parse_first_phase(text) + parse_playoffs(text)
    import_data(participants, games)
    write_audit(games)
    print("Importacao historica 2002 concluida")
    print(f"  participantes: {len(participants)}")
    print(f"  fases: {len({g.fase for g in games})}")
    print(f"  jogos: {len(games)}")
    print(f"  auditoria: {AUDIT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
