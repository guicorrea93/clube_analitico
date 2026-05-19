from __future__ import annotations

import argparse
import csv
import html
import re
import sqlite3
import time
import urllib.request
from pathlib import Path

from importar_eventos_ogol import Match, clean_text, find_ogol_game, parse_calendar


DB_PATH = Path("db/brasileirao.db")
BASE_HEADERS = {"User-Agent": "Mozilla/5.0 clube-analitico"}


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers=BASE_HEADERS)
    with urllib.request.urlopen(req, timeout=45) as response:
        raw = response.read()
    head = raw[:10000].decode("ascii", "ignore")
    charset_match = re.search(r"charset=([a-zA-Z0-9_-]+)", head, flags=re.I)
    charset = charset_match.group(1) if charset_match else "utf-8"
    return raw.decode(charset, "replace")


def extract_trainers(text: str) -> tuple[str, str] | None:
    marker = '<div class="subtitle">Treinadores</div>'
    idx = text.find(marker)
    if idx < 0:
        return None
    block = text[idx : idx + 3500]
    links = re.findall(r'<a href="/treinador/[^"]+">([^<]+)</a>', block, flags=re.I)
    names = [clean_text(html.unescape(name)) for name in links if clean_text(html.unescape(name))]
    if len(names) < 2:
        return None
    return names[0], names[1]


def load_missing(cur: sqlite3.Cursor, start: int, end: int) -> list[Match]:
    cur.row_factory = sqlite3.Row
    rows = cur.execute(
        """
        SELECT p.partida_id, p.temporada_id, p.rodada, p.data,
               hm.nome AS mandante, aw.nome AS visitante,
               p.gols_mandante, p.gols_visitante, 0 AS gols_banco
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        WHERE p.temporada_id BETWEEN ? AND ?
          AND (p.tecnico_mand_id IS NULL OR p.tecnico_vis_id IS NULL)
        ORDER BY p.temporada_id, p.rodada, p.partida_id
        """,
        (start, end),
    ).fetchall()
    return [Match(**dict(row)) for row in rows]


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def apply_rows(cur: sqlite3.Cursor, rows: list[dict]) -> None:
    for row in rows:
        cur.execute("INSERT OR IGNORE INTO dim_tecnico (nome) VALUES (?)", (row["tecnico_mandante"],))
        cur.execute("INSERT OR IGNORE INTO dim_tecnico (nome) VALUES (?)", (row["tecnico_visitante"],))
    ids = dict(cur.execute("SELECT nome, tecnico_id FROM dim_tecnico").fetchall())
    for row in rows:
        cur.execute(
            """
            UPDATE fato_partida
            SET tecnico_mand_id = COALESCE(tecnico_mand_id, ?),
                tecnico_vis_id = COALESCE(tecnico_vis_id, ?)
            WHERE partida_id = ?
            """,
            (ids[row["tecnico_mandante"]], ids[row["tecnico_visitante"]], row["partida_id"]),
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Importa técnicos faltantes via ogol.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    audit_csv = Path(f"data/ogol_tecnicos_{args.start}_{args.end}.csv")
    errors_csv = Path(f"data/ogol_tecnicos_{args.start}_{args.end}_erros.csv")

    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        missing = load_missing(cur, args.start, args.end)
        calendars = {season: parse_calendar(season) for season in range(args.start, args.end + 1)}
        rows: list[dict] = []
        errors: list[dict] = []
        for match in missing:
            game, method = find_ogol_game(match, calendars[match.temporada_id])
            if not game:
                errors.append({"partida_id": match.partida_id, "temporada": match.temporada_id, "erro": method})
                continue
            text = fetch_text(game.source_url)
            trainers = extract_trainers(text)
            if not trainers:
                errors.append({
                    "partida_id": match.partida_id,
                    "temporada": match.temporada_id,
                    "erro": f"tecnicos nao encontrados: {game.source_url}",
                })
                continue
            rows.append({
                "status": "ok",
                "partida_id": match.partida_id,
                "temporada": match.temporada_id,
                "rodada": match.rodada,
                "data_banco": match.data,
                "data_ogol": game.data,
                "mandante": match.mandante,
                "visitante": match.visitante,
                "placar": f"{match.gols_mandante}-{match.gols_visitante}",
                "match_method": method,
                "source_url": game.source_url,
                "tecnico_mandante": trainers[0],
                "tecnico_visitante": trainers[1],
            })
            time.sleep(0.2)

        write_csv(audit_csv, rows, [
            "status", "partida_id", "temporada", "rodada", "data_banco", "data_ogol",
            "mandante", "visitante", "placar", "match_method", "source_url",
            "tecnico_mandante", "tecnico_visitante",
        ])
        write_csv(errors_csv, errors, ["partida_id", "temporada", "erro"])
        print(f"partidas_faltantes={len(missing)}")
        print(f"linhas_validas={len(rows)} erros={len(errors)}")
        print(f"csv_auditoria={audit_csv}")
        print(f"csv_erros={errors_csv}")
        if args.apply:
            with con:
                apply_rows(cur, rows)
            print("modo=aplicado")
        else:
            print("modo=dry-run")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
