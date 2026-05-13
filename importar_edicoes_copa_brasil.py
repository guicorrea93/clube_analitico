"""Enriquece a base da Copa do Brasil com metadados por edicao.

Baixa/usa wikitextos das paginas anuais (1989-2025) e popula objetos novos:
- copa_brasil_edicao_info: datas, participantes, jogos, gols, artilheiro
- copa_brasil_participante: clubes classificados por edicao quando a pagina
  possui secao "Qualified teams"

Este script nao altera tabelas do Brasileirao Serie A.
"""
from __future__ import annotations

import re
import sqlite3
import time
import unicodedata
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

from importar_finais_copa_brasil import ALIASES, DB, ROOT, SOURCE_URL, clean_wiki, clube_id, key


RAW_DIR = ROOT / "data" / "copa_brasil_edicoes"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def canon(value: str) -> str:
    cleaned = clean_wiki(value)
    cleaned = re.sub(r"\{\{Flag\|[^}]+\}\}", "", cleaned)
    cleaned = re.sub(r"\{\{nowrap\|([^}]+)\}\}", r"\1", cleaned)
    cleaned = re.sub(r"\{\{small\|([^}]+)\}\}", r"\1", cleaned)
    cleaned = re.sub(r"\([^)]*title\)", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return ALIASES.get(key(cleaned), cleaned)


def fetch_raw(ano: int) -> str:
    path = RAW_DIR / f"{ano}.wiki"
    if path.exists() and path.stat().st_size > 1000:
        return path.read_text(encoding="utf-8")
    title = quote(f"{ano} Copa do Brasil")
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    req = Request(url, headers={"User-Agent": "clube-analitico-codex/1.0"})
    with urlopen(req, timeout=30) as resp:
        text = resp.read().decode("utf-8")
    path.write_text(text, encoding="utf-8")
    time.sleep(0.25)
    return text


def parse_infobox(text: str) -> dict:
    info = {}
    m = re.search(r"\{\{infobox football tournament season(?P<body>.*?)(?:\n\}\}|\n\|prev_season)", text, flags=re.I | re.S)
    body = m.group("body") if m else text[:2500]
    fields = {
        "dates": "datas",
        "num_teams": "num_times",
        "matches": "jogos",
        "goals": "gols",
        "scoring_leader": "artilheiro",
        "champions": "campeao_info",
        "runner-up": "vice_info",
        "player": "melhor_jogador",
        "goalkeeper": "melhor_goleiro",
    }
    for src, dst in fields.items():
        mm = re.search(rf"\|\s*{re.escape(src)}\s*=\s*(.+)", body)
        if not mm:
            continue
        val = mm.group(1).strip()
        val = re.sub(r"\{\{nowrap\|([^}]+)\}\}", r"\1", val)
        val = re.sub(r"\{\{small\|([^}]+)\}\}", r"\1", val)
        val = clean_wiki(val)
        val = re.sub(r"\([^)]*\d+(?:st|nd|rd|th)? title[^)]*\)", "", val).strip()
        info[dst] = val
    for k in ("num_times", "jogos", "gols"):
        if k in info:
            n = re.search(r"\d+", info[k].replace(",", ""))
            info[k] = int(n.group(0)) if n else None
    return info


def parse_qualified_teams(text: str) -> list[dict]:
    m = re.search(r"==\s*Qualified teams\s*==(?P<body>.*?)(?:\n==[^=])", text, flags=re.I | re.S)
    if not m:
        return []
    body = m.group("body").splitlines()
    rows = []
    association = ""
    current = []

    def flush(row_lines: list[str]) -> None:
        nonlocal association
        cells = []
        for ln in row_lines:
            s = ln.strip()
            if not s.startswith("|") or s.startswith("|-"):
                continue
            s = s.lstrip("|").strip()
            # Wikitables often keep several cells on the same row separated by ||.
            # Treating the full row as one cell pollutes club names with qualification text.
            cells.extend([p.strip() for p in re.split(r"\s*\|\|\s*", s) if p.strip()])
        if not cells:
            return
        if "{{Flag|" in cells[0] or "{{flag|" in cells[0]:
            assoc_raw = re.sub(r"<br>.*", "", cells[0], flags=re.I)
            association = re.sub(r".*\{\{[Ff]lag\|([^}]+)\}\}.*", r"\1", assoc_raw).strip()
            team_cell = cells[1] if len(cells) > 1 else ""
            qual_cell = cells[2] if len(cells) > 2 else ""
        else:
            team_cell = cells[0]
            qual_cell = cells[1] if len(cells) > 1 else ""
        if "[[" not in team_cell or "berth" in key(team_cell):
            return
        team = canon(team_cell)
        team_key = key(team)
        polluted_terms = (
            "berth", "champion", "champions", "runner", "runners", "place",
            "placed", "ranking", "qualified", "not already qualified",
            "campeonato", "championship", "copa", "best placed",
        )
        if not team or len(team) > 45 or any(term in team_key for term in polluted_terms):
            return
        qual = clean_wiki(qual_cell)
        rows.append({
            "clube": team,
            "associacao": association,
            "criterio": qual,
            "entra_terceira_fase": "'''" in team_cell or "'''" in qual_cell,
        })

    for line in body:
        if line.strip().startswith("|-"):
            flush(current)
            current = []
        else:
            current.append(line)
    flush(current)
    # dedup preservando ordem
    seen = set()
    out = []
    for r in rows:
        k = key(r["clube"])
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS copa_brasil_edicao_info (
        ano INTEGER PRIMARY KEY REFERENCES copa_brasil_edicao(ano),
        datas TEXT,
        num_times INTEGER,
        jogos INTEGER,
        gols INTEGER,
        artilheiro TEXT,
        campeao_info TEXT,
        vice_info TEXT,
        melhor_jogador TEXT,
        melhor_goleiro TEXT,
        fonte_url TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS copa_brasil_participante (
        ano INTEGER NOT NULL REFERENCES copa_brasil_edicao(ano),
        clube_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
        associacao TEXT,
        criterio_classificacao TEXT,
        entra_terceira_fase INTEGER NOT NULL DEFAULT 0,
        fonte_url TEXT NOT NULL,
        PRIMARY KEY (ano, clube_id)
    );

    DROP VIEW IF EXISTS vw_copa_brasil_edicoes_completas;
    CREATE VIEW vw_copa_brasil_edicoes_completas AS
    SELECT
        e.ano,
        e.nome,
        i.datas,
        i.num_times,
        i.jogos,
        i.gols,
        i.artilheiro,
        f.campeao,
        f.vice,
        f.gols_campeao,
        f.gols_vice,
        f.criterio_decisao,
        (SELECT COUNT(*) FROM copa_brasil_participante p WHERE p.ano = e.ano) AS participantes_mapeados,
        e.fonte_url
    FROM copa_brasil_edicao e
    LEFT JOIN copa_brasil_edicao_info i ON i.ano = e.ano
    LEFT JOIN vw_copa_brasil_finais f ON f.ano = e.ano;

    DROP VIEW IF EXISTS vw_copa_brasil_participantes;
    CREATE VIEW vw_copa_brasil_participantes AS
    SELECT
        p.ano,
        c.nome AS clube,
        c.uf,
        p.associacao,
        p.criterio_classificacao,
        p.entra_terceira_fase,
        p.fonte_url
    FROM copa_brasil_participante p
    JOIN dim_clube c ON c.clube_id = p.clube_id;
    """)


def main() -> None:
    con = sqlite3.connect(DB)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        ensure_schema(con)
        con.execute("DELETE FROM copa_brasil_participante")
        con.execute("DELETE FROM copa_brasil_edicao_info")
        imported_info = 0
        imported_part = 0
        for ano in range(1989, 2026):
            text = fetch_raw(ano)
            url = f"https://en.wikipedia.org/wiki/{ano}_Copa_do_Brasil"
            info = parse_infobox(text)
            con.execute("""
                INSERT OR REPLACE INTO copa_brasil_edicao_info
                (ano, datas, num_times, jogos, gols, artilheiro, campeao_info, vice_info, melhor_jogador, melhor_goleiro, fonte_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ano, info.get("datas"), info.get("num_times"), info.get("jogos"), info.get("gols"),
                info.get("artilheiro"), info.get("campeao_info"), info.get("vice_info"),
                info.get("melhor_jogador"), info.get("melhor_goleiro"), url,
            ))
            imported_info += 1
            for row in parse_qualified_teams(text):
                cid = clube_id(con, row["clube"])
                con.execute("""
                    INSERT OR REPLACE INTO copa_brasil_participante
                    (ano, clube_id, associacao, criterio_classificacao, entra_terceira_fase, fonte_url)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (ano, cid, row["associacao"], row["criterio"], int(row["entra_terceira_fase"]), url))
                imported_part += 1
        con.commit()
        print(f"OK: {imported_info} edicoes enriquecidas; {imported_part} participantes mapeados.")
    finally:
        con.close()


if __name__ == "__main__":
    main()

