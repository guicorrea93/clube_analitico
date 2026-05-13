"""Importa dados historicos da Copa do Brasil para tabelas novas no SQLite.

Fonte principal: List of Copa do Brasil winners (Wikipedia, wikitexto baixado
em data/copa_brasil_winners.wiki). O script preserva toda a estrutura atual do
Brasileirao e recria apenas objetos com prefixo copa_brasil_*.
"""
from __future__ import annotations

import re
import sqlite3
import unicodedata
from pathlib import Path


ROOT = Path(__file__).parent
DB = ROOT / "db" / "brasileirao.db"
WIKI = ROOT / "data" / "copa_brasil_winners.wiki"
SOURCE_URL = "https://en.wikipedia.org/wiki/List_of_Copa_do_Brasil_winners"


ALIASES = {
    "athletico paranaense": "Athletico-PR",
    "atletico paranaense": "Athletico-PR",
    "athletico pr": "Athletico-PR",
    "atletico pr": "Athletico-PR",
    "atletico mineiro": "Atletico-MG",
    "atletico mg": "Atletico-MG",
    "atletico minero": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "botafogo rj": "Botafogo-RJ",
    "coritiba foot ball club": "Coritiba",
    "cruzeiro esporte clube": "Cruzeiro",
    "gremio foot ball porto alegrense": "Gremio",
    "gremio": "Gremio",
    "goias esporte clube": "Goias",
    "flamengo": "Flamengo",
    "fluminense football club": "Fluminense",
    "internacional": "Internacional",
    "sport club internacional": "Internacional",
    "sport recife": "Sport",
    "sport club do recife": "Sport",
    "sao paulo": "Sao Paulo",
    "sao paulo fc": "Sao Paulo",
    "sao paulo futebol clube": "Sao Paulo",
    "santos": "Santos",
    "santos fc": "Santos",
    "vasco da gama": "Vasco",
    "criciuma": "Criciuma",
    "vitoria": "Vitoria",
    "ceara": "Ceara",
    "paulista": "Paulista",
    "santo andre": "Santo Andre",
    "juventude": "Juventude",
    "brasiliense": "Brasiliense",
    "figueirense": "Figueirense",
    "corinthians": "Corinthians",
    "palmeiras": "Palmeiras",
}


UF = {
    "Athletico-PR": "PR",
    "Atletico-MG": "MG",
    "Botafogo-RJ": "RJ",
    "Brasiliense": "DF",
    "Ceara": "CE",
    "Corinthians": "SP",
    "Coritiba": "PR",
    "Criciuma": "SC",
    "Cruzeiro": "MG",
    "Figueirense": "SC",
    "Flamengo": "RJ",
    "Fluminense": "RJ",
    "Goias": "GO",
    "Gremio": "RS",
    "Internacional": "RS",
    "Juventude": "RS",
    "Palmeiras": "SP",
    "Paulista": "SP",
    "Santo Andre": "SP",
    "Santos": "SP",
    "Sao Paulo": "SP",
    "Sport": "PE",
    "Vasco": "RJ",
    "Vitoria": "BA",
}


def key(value: object) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_wiki(value: str) -> str:
    text = value.strip().lstrip("|").strip()
    if re.match(r"^(colspan|rowspan|align|bgcolor|style|width)\b", text) and "|" in text:
        text = text.split("|", 1)[1].strip()
    text = text.replace("&ndash;", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"\{\{flagicon\|[^}]+\}\}", "", text)
    text = text.replace("'''", "")
    text = re.sub(r"\[\[[^|\]]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def canon_clube(value: str) -> str:
    cleaned = clean_wiki(value)
    return ALIASES.get(key(cleaned), cleaned)


def parse_score(value: str) -> tuple[int, int]:
    text = clean_wiki(value)
    m = re.search(r"(\d+)\s*-\s*(\d+)", text)
    if not m:
        raise ValueError(f"Placar invalido: {value!r}")
    return int(m.group(1)), int(m.group(2))


def parse_decisao(text: str) -> str:
    low = key(text)
    if "pen" in low:
        return "penaltis"
    if "away goals" in low:
        return "gols_fora"
    if "goal difference" in low:
        return "saldo_gols"
    if "points" in low:
        return "pontos"
    return "outro"


def parse_wiki() -> list[dict]:
    if not WIKI.exists():
        raise SystemExit(f"Arquivo fonte nao encontrado: {WIKI}")
    lines = WIKI.read_text(encoding="utf-8").splitlines()
    editions: list[dict] = []
    i = 0
    while i < len(lines):
        m = re.search(r"\[\[(\d{4}) Copa do Brasil\|(\d{4})\]\]", lines[i])
        if not m:
            i += 1
            continue
        ano = int(m.group(2))
        if ano > 2025:
            break

        def read_leg(start: int) -> tuple[dict, int]:
            j = start
            while j < len(lines) and not lines[j].startswith("|{{flagicon"):
                j += 1
            home = canon_clube(lines[j + 1])
            gm, gv = parse_score(lines[j + 2])
            away = canon_clube(lines[j + 3])
            venue = clean_wiki(lines[j + 5]) if j + 5 < len(lines) else ""
            location = clean_wiki(lines[j + 6]) if j + 6 < len(lines) else ""
            return {
                "mandante": home,
                "visitante": away,
                "gm": gm,
                "gv": gv,
                "estadio": venue,
                "local": location,
            }, j + 7

        leg1, nxt = read_leg(i + 1)
        leg2, nxt = read_leg(nxt)
        result_line = ""
        while nxt < len(lines):
            txt = clean_wiki(lines[nxt])
            if " won " in txt or " won on " in txt:
                result_line = txt
                break
            nxt += 1
        campeao_raw = result_line.split(" won", 1)[0].split(",")[-1].strip()
        campeao = canon_clube(campeao_raw)
        finalists = {leg1["mandante"], leg1["visitante"], leg2["mandante"], leg2["visitante"]}
        vice = next((c for c in finalists if c != campeao), "")
        gm_agg = 0
        gv_agg = 0
        for leg in (leg1, leg2):
            if leg["mandante"] == campeao:
                gm_agg += leg["gm"]
                gv_agg += leg["gv"]
            elif leg["visitante"] == campeao:
                gm_agg += leg["gv"]
                gv_agg += leg["gm"]

        editions.append({
            "ano": ano,
            "campeao": campeao,
            "vice": vice,
            "gols_campeao": gm_agg,
            "gols_vice": gv_agg,
            "criterio": parse_decisao(result_line),
            "resumo_decisao": result_line,
            "leg1": leg1,
            "leg2": leg2,
        })
        i = nxt + 1
    return editions


def clube_id(con: sqlite3.Connection, nome: str) -> int:
    row = con.execute("SELECT clube_id FROM dim_clube WHERE nome = ?", (nome,)).fetchone()
    if row:
        return int(row[0])
    con.execute("INSERT INTO dim_clube(nome, uf) VALUES (?, ?)", (nome, UF.get(nome, "")))
    return int(con.execute("SELECT last_insert_rowid()").fetchone()[0])


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS copa_brasil_edicao (
        ano INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        formato TEXT,
        fonte_url TEXT NOT NULL,
        observacao TEXT
    );

    CREATE TABLE IF NOT EXISTS copa_brasil_final (
        ano INTEGER PRIMARY KEY REFERENCES copa_brasil_edicao(ano),
        campeao_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        vice_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        gols_campeao INTEGER NOT NULL,
        gols_vice INTEGER NOT NULL,
        criterio_decisao TEXT,
        resumo_decisao TEXT,
        fonte_url TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS copa_brasil_final_partida (
        ano INTEGER NOT NULL REFERENCES copa_brasil_edicao(ano),
        jogo INTEGER NOT NULL,
        mandante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        visitante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        gols_mandante INTEGER NOT NULL,
        gols_visitante INTEGER NOT NULL,
        estadio TEXT,
        local TEXT,
        fonte_url TEXT NOT NULL,
        PRIMARY KEY (ano, jogo)
    );

    DROP VIEW IF EXISTS vw_copa_brasil_finais;
    CREATE VIEW vw_copa_brasil_finais AS
    SELECT
        f.ano,
        c.nome AS campeao,
        c.uf AS uf_campeao,
        v.nome AS vice,
        v.uf AS uf_vice,
        f.gols_campeao,
        f.gols_vice,
        f.criterio_decisao,
        f.resumo_decisao,
        f.fonte_url
    FROM copa_brasil_final f
    JOIN dim_clube c ON c.clube_id = f.campeao_id
    JOIN dim_clube v ON v.clube_id = f.vice_id;

    DROP VIEW IF EXISTS vw_copa_brasil_partidas_finais;
    CREATE VIEW vw_copa_brasil_partidas_finais AS
    SELECT
        p.ano,
        p.jogo,
        m.nome AS mandante,
        m.uf AS uf_mandante,
        p.gols_mandante,
        p.gols_visitante,
        vi.nome AS visitante,
        vi.uf AS uf_visitante,
        p.estadio,
        p.local,
        p.fonte_url
    FROM copa_brasil_final_partida p
    JOIN dim_clube m ON m.clube_id = p.mandante_id
    JOIN dim_clube vi ON vi.clube_id = p.visitante_id;

    DROP VIEW IF EXISTS vw_copa_brasil_desempenho_clube;
    CREATE VIEW vw_copa_brasil_desempenho_clube AS
    WITH clubes AS (
        SELECT campeao_id AS clube_id, 1 AS titulos, 0 AS vices, ano FROM copa_brasil_final
        UNION ALL
        SELECT vice_id AS clube_id, 0 AS titulos, 1 AS vices, ano FROM copa_brasil_final
    )
    SELECT
        c.clube_id,
        c.nome AS clube,
        c.uf,
        SUM(titulos) AS titulos,
        SUM(vices) AS vices,
        COUNT(*) AS finais,
        MIN(ano) AS primeira_final,
        MAX(ano) AS ultima_final
    FROM clubes x
    JOIN dim_clube c ON c.clube_id = x.clube_id
    GROUP BY c.clube_id, c.nome, c.uf;

    DROP VIEW IF EXISTS vw_copa_brasil_titulos_por_uf;
    CREATE VIEW vw_copa_brasil_titulos_por_uf AS
    SELECT c.uf, COUNT(*) AS titulos
    FROM copa_brasil_final f
    JOIN dim_clube c ON c.clube_id = f.campeao_id
    GROUP BY c.uf;
    """)


def main() -> None:
    editions = parse_wiki()
    if not editions:
        raise SystemExit("Nenhuma edicao encontrada na fonte.")
    con = sqlite3.connect(DB)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        ensure_schema(con)
        con.execute("DELETE FROM copa_brasil_final_partida")
        con.execute("DELETE FROM copa_brasil_final")
        con.execute("DELETE FROM copa_brasil_edicao")
        for ed in editions:
            con.execute(
                "INSERT INTO copa_brasil_edicao(ano, nome, formato, fonte_url, observacao) VALUES (?, ?, ?, ?, ?)",
                (ed["ano"], f"Copa do Brasil {ed['ano']}", "mata-mata; final ida e volta", SOURCE_URL, ""),
            )
            campeao_id = clube_id(con, ed["campeao"])
            vice_id = clube_id(con, ed["vice"])
            con.execute("""
                INSERT INTO copa_brasil_final
                (ano, campeao_id, vice_id, gols_campeao, gols_vice, criterio_decisao, resumo_decisao, fonte_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ed["ano"], campeao_id, vice_id, ed["gols_campeao"], ed["gols_vice"],
                ed["criterio"], ed["resumo_decisao"], SOURCE_URL,
            ))
            for jogo, leg_key in enumerate(("leg1", "leg2"), start=1):
                leg = ed[leg_key]
                con.execute("""
                    INSERT INTO copa_brasil_final_partida
                    (ano, jogo, mandante_id, visitante_id, gols_mandante, gols_visitante, estadio, local, fonte_url)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    ed["ano"], jogo, clube_id(con, leg["mandante"]), clube_id(con, leg["visitante"]),
                    leg["gm"], leg["gv"], leg["estadio"], leg["local"], SOURCE_URL,
                ))
        con.commit()
        print(f"OK: {len(editions)} edicoes da Copa do Brasil importadas ({editions[0]['ano']}-{editions[-1]['ano']}).")
    finally:
        con.close()


if __name__ == "__main__":
    main()
