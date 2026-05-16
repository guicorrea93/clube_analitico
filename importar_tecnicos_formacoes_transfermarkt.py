from __future__ import annotations

import argparse
import csv
import html
import re
import sqlite3
import time
import unicodedata
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path


DB_PATH = Path("db/brasileirao.db")
AUDIT_CSV = Path("data/transfermarkt_tecnicos_formacoes_2006_2013.csv")
ERRORS_CSV = Path("data/transfermarkt_tecnicos_formacoes_2006_2013_erros.csv")
BASE = "https://www.transfermarkt.com.br"
HEADERS = {"User-Agent": "Mozilla/5.0 clube-analitico"}


TEAM_ALIASES = {
    "america fc rn": "America-RN",
    "america mineiro": "America-MG",
    "america mg": "America-MG",
    "athletico paranaense": "Athletico-PR",
    "atletico goianiense": "Atletico-GO",
    "atletico mineiro": "Atletico-MG",
    "avai fc": "Avai",
    "botafogo fr": "Botafogo-RJ",
    "ca paranaense": "Athletico-PR",
    "clube atletico paranaense": "Athletico-PR",
    "ceara sc": "Ceara",
    "cr vasco da gama": "Vasco",
    "cr flamengo": "Flamengo",
    "criciuma ec": "Criciuma",
    "cruzeiro ec": "Cruzeiro",
    "ec bahia": "Bahia",
    "ec juventude": "Juventude",
    "ec santo andre": "Santo Andre",
    "ec vitoria": "Vitoria",
    "figueirense fc": "Figueirense",
    "fluminense fc": "Fluminense",
    "fortaleza ec": "Fortaleza",
    "goias ec": "Goias",
    "gremio barueri": "Barueri",
    "gremio fbpa": "Gremio",
    "gremio prudente": "Gremio Prudente",
    "guarani fc": "Guarani",
    "ipatinga fc": "Ipatinga",
    "joinville ec": "Joinville",
    "nautico": "Nautico",
    "parana clube": "Parana",
    "aa ponte preta": "Ponte Preta",
    "portuguesa": "Portuguesa",
    "santa cruz fc": "Santa Cruz",
    "santos fc": "Santos",
    "sao caetano": "Sao Caetano",
    "ad sao caetano": "Sao Caetano",
    "sao paulo fc": "Sao Paulo",
    "sc corinthians": "Corinthians",
    "sc internacional": "Internacional",
    "sc recife": "Sport",
    "sport recife": "Sport",
    "se palmeiras": "Palmeiras",
    "ser caxias": "Caxias",
    "coritiba fc": "Coritiba",
}


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace("ę", "e").replace("Ę", "E")
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text.lower())
    return " ".join(text.split())


def canonical_team(value: str, season: int) -> str:
    key = normalize(html.unescape(value))
    if season == 2007 and key == "america fc":
        return "America-RN"
    if season == 2010 and key in {"gremio barueri", "gremio barueri futebol ltda", "barueri"}:
        return "Gremio Prudente"
    if season == 2009 and key in {"gremio barueri", "gremio barueri futebol ltda"}:
        return "Barueri"
    return TEAM_ALIASES.get(key, html.unescape(value).strip())


def fetch_text(url: str, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=45) as response:
                return response.read().decode("utf-8", "ignore")
        except Exception as exc:  # pragma: no cover - network instability
            last_error = exc
            time.sleep(0.5 + attempt)
    raise RuntimeError(f"falha ao baixar {url}: {last_error}")


def season_rounds(cur: sqlite3.Cursor, season: int) -> list[int]:
    rows = cur.execute(
        "SELECT DISTINCT rodada FROM fato_partida WHERE temporada_id = ? ORDER BY rodada",
        (season,),
    ).fetchall()
    return [int(r[0]) for r in rows]


def missing_season_rounds(cur: sqlite3.Cursor, season: int) -> list[int]:
    rows = cur.execute(
        """
        SELECT DISTINCT rodada
        FROM fato_partida
        WHERE temporada_id = ?
          AND (
            tecnico_mand_id IS NULL
            OR tecnico_vis_id IS NULL
            OR formacao_mandante IS NULL
            OR formacao_mandante = ''
            OR formacao_visitante IS NULL
            OR formacao_visitante = ''
          )
        ORDER BY rodada
        """,
        (season,),
    ).fetchall()
    return [int(r[0]) for r in rows]


def schedule_ids(season: int, round_: int) -> list[str]:
    sid = season - 1
    url = f"{BASE}/campeonato-brasileiro-serie-a/spieltagtabelle/wettbewerb/BRA1?saison_id={sid}&spieltag={round_}"
    text = fetch_text(url)
    ids = re.findall(r"spielbericht/([0-9]+)", text)
    seen: set[str] = set()
    unique = []
    for match_id in ids:
        if match_id not in seen:
            unique.append(match_id)
            seen.add(match_id)
    return unique


def parse_match(match_id: str, season: int, round_: int) -> tuple[dict | None, dict | None]:
    url = f"{BASE}/spielbericht/index/spielbericht/{match_id}"
    text = fetch_text(url)

    date_match = re.search(r"datum/(\d{4}-\d{2}-\d{2})", text)
    score_match = re.search(r'<div class="sb-endstand">\s*([0-9]+):([0-9]+)', text)
    team_matches = re.findall(r'<a title="([^"]+)" class="sb-vereinslink"', text)
    if len(team_matches) < 2:
        team_matches = re.findall(r'class="sb-vereinslink" href="[^"]+"><img[^>]+title="([^"]+)"', text)

    formations = [html.unescape(x).strip() for x in re.findall(r"Onze inicial:\s*([^<]+)", text)]
    trainer_pattern = re.compile(
        r"""
        (?:<td[^>]*>\s*<b>Treinador</b>\s*</td>\s*<td[^>]*>\s*<a[^>]*>(?P<classic>[^<]+)</a>)
        |
        (?:<div>Treinador:</div>\s*</td>\s*<td[^>]*class="bench-table__td"[^>]*>\s*<a[^>]*>(?P<bench>[^<]+)</a>)
        """,
        re.S | re.X,
    )
    trainers = []
    for match in trainer_pattern.finditer(text):
        name = match.group("classic") or match.group("bench")
        if name:
            trainers.append(html.unescape(name).strip())

    if not date_match or not score_match or len(team_matches) < 2:
        return None, {"temporada": season, "rodada": round_, "match_id": match_id, "erro": "cabecalho incompleto"}
    if len(formations) < 2 and len(trainers) < 2:
        return None, {"temporada": season, "rodada": round_, "match_id": match_id, "erro": "sem tecnico/formacao"}

    row = {
        "source": "Transfermarkt",
        "source_match_id": match_id,
        "source_url": url,
        "temporada_id": season,
        "rodada": round_,
        "data": date_match.group(1),
        "mandante": canonical_team(team_matches[0], season),
        "visitante": canonical_team(team_matches[1], season),
        "gols_mandante": int(score_match.group(1)),
        "gols_visitante": int(score_match.group(2)),
        "formacao_mandante": formations[0] if len(formations) >= 2 else "",
        "formacao_visitante": formations[1] if len(formations) >= 2 else "",
        "tecnico_mandante": trainers[0] if len(trainers) >= 2 else "",
        "tecnico_visitante": trainers[1] if len(trainers) >= 2 else "",
    }
    return row, None


def load_match_map(cur: sqlite3.Cursor, season: int) -> dict[tuple, int]:
    rows = cur.execute(
        """
        SELECT p.partida_id, p.data, hm.nome, aw.nome, p.gols_mandante, p.gols_visitante
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        WHERE p.temporada_id = ?
        """,
        (season,),
    ).fetchall()
    return {
        (data, mandante, visitante, gm, gv): partida_id
        for partida_id, data, mandante, visitante, gm, gv in rows
    }


def attach_partida_ids(cur: sqlite3.Cursor, rows: list[dict]) -> tuple[list[dict], list[dict]]:
    ok: list[dict] = []
    errors: list[dict] = []
    maps: dict[int, dict[tuple, int]] = {}
    for row in rows:
        season = int(row["temporada_id"])
        maps.setdefault(season, load_match_map(cur, season))
        key = (
            row["data"],
            row["mandante"],
            row["visitante"],
            row["gols_mandante"],
            row["gols_visitante"],
        )
        partida_id = maps[season].get(key)
        if partida_id is None:
            errors.append({
                "temporada": season,
                "rodada": row["rodada"],
                "match_id": row["source_match_id"],
                "erro": f"partida nao encontrada: {key}",
            })
            continue
        row["partida_id"] = partida_id
        ok.append(row)
    return ok, errors


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def is_missing(value: object) -> bool:
    return value is None or str(value).strip() == ""


def apply_rows(cur: sqlite3.Cursor, rows: list[dict], only_missing: bool = False) -> None:
    for row in rows:
        if row["tecnico_mandante"]:
            cur.execute("INSERT OR IGNORE INTO dim_tecnico (nome) VALUES (?)", (row["tecnico_mandante"],))
        if row["tecnico_visitante"]:
            cur.execute("INSERT OR IGNORE INTO dim_tecnico (nome) VALUES (?)", (row["tecnico_visitante"],))
    tecnico_map = dict(cur.execute("SELECT nome, tecnico_id FROM dim_tecnico").fetchall())
    for row in rows:
        current = None
        if only_missing:
            current = cur.execute(
                """
                SELECT tecnico_mand_id, tecnico_vis_id, formacao_mandante, formacao_visitante
                FROM fato_partida
                WHERE partida_id = ?
                """,
                (row["partida_id"],),
            ).fetchone()
            if current is None:
                continue

        updates = []
        params = []
        if row["tecnico_mandante"] and (not only_missing or is_missing(current[0])):
            updates.append("tecnico_mand_id = ?")
            params.append(tecnico_map[row["tecnico_mandante"]])
        if row["tecnico_visitante"] and (not only_missing or is_missing(current[1])):
            updates.append("tecnico_vis_id = ?")
            params.append(tecnico_map[row["tecnico_visitante"]])
        if row["formacao_mandante"] and (not only_missing or is_missing(current[2])):
            updates.append("formacao_mandante = ?")
            params.append(row["formacao_mandante"])
        if row["formacao_visitante"] and (not only_missing or is_missing(current[3])):
            updates.append("formacao_visitante = ?")
            params.append(row["formacao_visitante"])
        if updates:
            params.append(row["partida_id"])
            cur.execute(f"UPDATE fato_partida SET {', '.join(updates)} WHERE partida_id = ?", params)


def main() -> int:
    parser = argparse.ArgumentParser(description="Importa tecnicos e formacoes via Transfermarkt.")
    parser.add_argument("--start", type=int, default=2006)
    parser.add_argument("--end", type=int, default=2013)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--allow-partial", action="store_true", help="aplica linhas validas mesmo com erros auditados")
    parser.add_argument("--only-missing", action="store_true", help="preenche apenas campos vazios no banco")
    parser.add_argument("--audit-csv", type=Path, default=None)
    parser.add_argument("--errors-csv", type=Path, default=None)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    audit_csv = args.audit_csv or Path(f"data/transfermarkt_tecnicos_formacoes_{args.start}_{args.end}.csv")
    errors_csv = args.errors_csv or Path(f"data/transfermarkt_tecnicos_formacoes_{args.start}_{args.end}_erros.csv")

    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        jobs: list[tuple[int, int, str]] = []
        for season in range(args.start, args.end + 1):
            rounds = missing_season_rounds(cur, season) if args.only_missing else season_rounds(cur, season)
            for round_ in rounds:
                ids = schedule_ids(season, round_)
                for match_id in ids:
                    jobs.append((season, round_, match_id))
            print(f"{season}: partidas_transfermarkt={sum(1 for s, _, _ in jobs if s == season)}")

        parsed: list[dict] = []
        errors: list[dict] = []
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(parse_match, match_id, season, round_): (season, round_, match_id)
                for season, round_, match_id in jobs
            }
            for i, future in enumerate(as_completed(futures), start=1):
                season, round_, match_id = futures[future]
                try:
                    row, error = future.result()
                except Exception as exc:  # pragma: no cover - network instability
                    row = None
                    error = {
                        "temporada": season,
                        "rodada": round_,
                        "match_id": match_id,
                        "erro": str(exc),
                    }
                if row:
                    parsed.append(row)
                if error:
                    errors.append(error)
                if i % 250 == 0:
                    print(f"processadas={i}/{len(jobs)}")

        rows, match_errors = attach_partida_ids(cur, parsed)
        errors.extend(match_errors)

        fields = [
            "source", "source_match_id", "source_url", "partida_id", "temporada_id", "rodada",
            "data", "mandante", "visitante", "gols_mandante", "gols_visitante",
            "formacao_mandante", "formacao_visitante", "tecnico_mandante", "tecnico_visitante",
        ]
        write_csv(audit_csv, sorted(rows, key=lambda r: (r["temporada_id"], r["rodada"], r["partida_id"])), fields)
        write_csv(errors_csv, errors, ["temporada", "rodada", "match_id", "erro"])

        print(f"linhas_validas={len(rows)} erros={len(errors)}")
        print(f"csv_auditoria={audit_csv}")
        print(f"csv_erros={errors_csv}")
        if errors and not args.allow_partial:
            print("modo=erro_sem_aplicar")
            return 1
        if args.apply:
            with con:
                apply_rows(cur, rows, only_missing=args.only_missing)
            print("modo=aplicado")
        else:
            print("modo=dry-run")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
