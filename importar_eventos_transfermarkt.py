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
AUDIT_CSV = Path("data/transfermarkt_eventos_2003_2006.csv")
ERRORS_CSV = Path("data/transfermarkt_eventos_2003_2006_erros.csv")
BASE = "https://www.transfermarkt.com.br"
HEADERS = {"User-Agent": "Mozilla/5.0 clube-analitico"}


TEAM_ALIASES = {
    "aa ponte preta": "Ponte Preta",
    "ad sao caetano": "Sao Caetano",
    "america fc rn": "America-RN",
    "america mineiro": "America-MG",
    "america mg": "America-MG",
    "athletico paranaense": "Athletico-PR",
    "atletico goianiense": "Atletico-GO",
    "atletico mineiro": "Atletico-MG",
    "avai fc": "Avai",
    "botafogo fr": "Botafogo-RJ",
    "brasiliense fc": "Brasiliense",
    "ca paranaense": "Athletico-PR",
    "ceara sc": "Ceara",
    "clube atletico paranaense": "Athletico-PR",
    "cr flamengo": "Flamengo",
    "cr vasco da gama": "Vasco",
    "criciuma ec": "Criciuma",
    "coritiba fc": "Coritiba",
    "cruzeiro ec": "Cruzeiro",
    "ec bahia": "Bahia",
    "ec juventude": "Juventude",
    "ec santo andre": "Santo Andre",
    "ec vitoria": "Vitoria",
    "figueirense fc": "Figueirense",
    "fluminense fc": "Fluminense",
    "fortaleza ec": "Fortaleza",
    "goias ec": "Goias",
    "gremio fbpa": "Gremio",
    "gremio prudente": "Gremio Prudente",
    "guarani fc": "Guarani",
    "ipatinga fc": "Ipatinga",
    "joinville ec": "Joinville",
    "nautico": "Nautico",
    "parana clube": "Parana",
    "paysandu sc": "Paysandu",
    "portuguesa": "Portuguesa",
    "santa cruz fc": "Santa Cruz",
    "santos fc": "Santos",
    "sao caetano": "Sao Caetano",
    "sao paulo fc": "Sao Paulo",
    "sc corinthians": "Corinthians",
    "sc internacional": "Internacional",
    "sc recife": "Sport",
    "se palmeiras": "Palmeiras",
    "sport recife": "Sport",
}


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(text.lower().replace("-", " ").split())


def canonical_team(value: str) -> str:
    return TEAM_ALIASES.get(normalize(html.unescape(value)), html.unescape(value).strip())


def fetch_text(url: str, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=45) as response:
                return response.read().decode("utf-8", "ignore")
        except Exception as exc:
            last_error = exc
            time.sleep(0.5 + attempt)
    raise RuntimeError(f"falha ao baixar {url}: {last_error}")


def season_rounds(cur: sqlite3.Cursor, season: int) -> list[int]:
    return [
        int(r[0])
        for r in cur.execute(
            "SELECT DISTINCT rodada FROM fato_partida WHERE temporada_id = ? ORDER BY rodada",
            (season,),
        ).fetchall()
    ]


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


def sprite_minute(fragment: str) -> int | None:
    match = re.search(r"background-position:\s*-([0-9]+)px\s*-([0-9]+)px", fragment)
    if not match:
        return None
    x = int(match.group(1))
    y = int(match.group(2))
    step = 36 if "sb-sprite-uhr-klein" in fragment else 42
    minute = (y // step) * 10 + (x // step) + 1
    return minute if minute <= 120 else None


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def goal_type(text: str) -> str:
    key = normalize(text)
    if "gol contra" in key:
        return "Gol Contra"
    if "penalti" in key or "penalty" in key:
        return "Penalti"
    if "falta" in key:
        return "Falta"
    return "Normal"


def parse_header(text: str, season: int, round_: int, match_id: str) -> tuple[dict | None, dict | None]:
    date_match = re.search(r"datum/(\d{4}-\d{2}-\d{2})", text)
    score_match = re.search(r'<div class="sb-endstand">\s*([0-9]+):([0-9]+)', text)
    teams = re.findall(r'<a title="([^"]+)" class="sb-vereinslink"', text)
    if len(teams) < 2:
        teams = re.findall(r'class="sb-vereinslink" href="[^"]+"><img[^>]+title="([^"]+)"', text)
    if not date_match or not score_match or len(teams) < 2:
        return None, {"temporada": season, "rodada": round_, "match_id": match_id, "erro": "cabecalho incompleto"}
    return {
        "source_match_id": match_id,
        "source_url": f"{BASE}/spielbericht/index/spielbericht/{match_id}",
        "temporada_id": season,
        "rodada": round_,
        "data": date_match.group(1),
        "mandante": canonical_team(teams[0]),
        "visitante": canonical_team(teams[1]),
        "gols_mandante": int(score_match.group(1)),
        "gols_visitante": int(score_match.group(2)),
    }, None


def section_between(text: str, start_id: str, end_ids: list[str]) -> str:
    start = text.find(f'id="{start_id}"')
    if start < 0:
        return ""
    end_positions = [text.find(f'id="{end_id}"', start + 1) for end_id in end_ids]
    end_positions = [pos for pos in end_positions if pos > start]
    end = min(end_positions) if end_positions else len(text)
    return text[start:end]


def parse_event_items(section: str) -> list[str]:
    return re.findall(r'(<li class="sb-aktion-[^"]+">.*?</li>)', section, flags=re.S)


def parse_goals(text: str, header: dict) -> list[dict]:
    section = section_between(text, "sb-tore", ["sb-wechsel", "sb-karten"])
    rows = []
    for item in parse_event_items(section):
        player = re.search(r'<a title="([^"]+)" class="wichtig"', item)
        club = re.search(r'<div class="sb-aktion-wappen">.*?<a title="([^"]+)"', item, flags=re.S)
        score = re.search(r"<b>([0-9]+:[0-9]+)</b>", item)
        if not player or not club or not score:
            continue
        desc = clean_text(re.search(r'<div class="sb-aktion-aktion">(.*?)</div>', item, flags=re.S).group(1))
        rows.append({
            **header,
            "evento": "gol",
            "clube": canonical_team(club.group(1)),
            "jogador": html.unescape(player.group(1)).strip(),
            "tipo": goal_type(desc),
            "minuto": sprite_minute(item),
            "placar_evento": score.group(1),
            "num_camisa": "",
        })
    return rows


def parse_cards(text: str, header: dict) -> list[dict]:
    section = section_between(text, "sb-karten", ["sb-sonstige", "sb-verletzungen"])
    rows = []
    for item in parse_event_items(section):
        player = re.search(r'<a title="([^"]+)" class="wichtig"', item)
        club = re.search(r'<div class="sb-aktion-wappen">.*?<a title="([^"]+)"', item, flags=re.S)
        if not player or not club:
            continue
        item_norm = normalize(item)
        if "sb gelbrot" in item_norm or "cartao amarelo vermelho" in item_norm:
            card_type = "Vermelho"
        elif "sb rot" in item_norm or "cartao vermelho" in item_norm:
            card_type = "Vermelho"
        else:
            card_type = "Amarelo"
        rows.append({
            **header,
            "evento": "cartao",
            "clube": canonical_team(club.group(1)),
            "jogador": html.unescape(player.group(1)).strip(),
            "tipo": card_type,
            "minuto": sprite_minute(item),
            "placar_evento": "",
            "num_camisa": "",
        })
    return rows


def parse_match(match_id: str, season: int, round_: int) -> tuple[list[dict], list[dict]]:
    text = fetch_text(f"{BASE}/spielbericht/index/spielbericht/{match_id}")
    header, error = parse_header(text, season, round_, match_id)
    if error:
        return [], [error]
    assert header is not None
    return parse_goals(text, header) + parse_cards(text, header), []


def load_match_map(cur: sqlite3.Cursor, season: int) -> dict[tuple, dict]:
    rows = cur.execute(
        """
        SELECT p.partida_id, p.data, hm.nome, aw.nome, p.gols_mandante, p.gols_visitante, p.rodada
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        WHERE p.temporada_id = ?
        """,
        (season,),
    ).fetchall()
    return {
        (data, mandante, visitante, gm, gv): {
            "partida_id": partida_id,
            "rodada": rodada,
            "data": datetime.strptime(data, "%Y-%m-%d").date(),
            "mandante": mandante,
            "visitante": visitante,
            "gols_mandante": gm,
            "gols_visitante": gv,
        }
        for partida_id, data, mandante, visitante, gm, gv, rodada in rows
    }


def find_match(match_map: dict[tuple, dict], row: dict) -> tuple[dict | None, str]:
    key = (row["data"], row["mandante"], row["visitante"], row["gols_mandante"], row["gols_visitante"])
    exact = match_map.get(key)
    if exact:
        return exact, "exact"
    event_date = datetime.strptime(row["data"], "%Y-%m-%d").date()
    near_score = [
        m for m in match_map.values()
        if m["mandante"] == row["mandante"]
        and m["visitante"] == row["visitante"]
        and m["gols_mandante"] == row["gols_mandante"]
        and m["gols_visitante"] == row["gols_visitante"]
        and abs((m["data"] - event_date).days) <= 2
    ]
    if len(near_score) == 1:
        return near_score[0], "near_score"
    return None, "not_found"


def attach_partidas(cur: sqlite3.Cursor, rows: list[dict]) -> tuple[list[dict], list[dict]]:
    maps: dict[int, dict] = {}
    ok, errors = [], []
    for row in rows:
        season = int(row["temporada_id"])
        maps.setdefault(season, load_match_map(cur, season))
        match, method = find_match(maps[season], row)
        if not match:
            key = (row["data"], row["mandante"], row["visitante"], row["gols_mandante"], row["gols_visitante"])
            errors.append({"temporada": season, "rodada": row["rodada"], "match_id": row["source_match_id"], "erro": f"partida nao encontrada: {key}"})
            continue
        row["partida_id"] = match["partida_id"]
        row["rodada"] = match["rodada"]
        row["match_method"] = method
        ok.append(row)
    return ok, errors


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fields)
        writer.writeheader()
        writer.writerows(rows)


def apply_rows(cur: sqlite3.Cursor, rows: list[dict], goal_seasons: set[int], card_seasons: set[int]) -> None:
    for row in rows:
        cur.execute("INSERT OR IGNORE INTO dim_jogador (nome, posicao_id) VALUES (?, NULL)", (row["jogador"],))
    player_map = dict(cur.execute("SELECT nome, jogador_id FROM dim_jogador").fetchall())
    club_map = dict(cur.execute("SELECT nome, clube_id FROM dim_clube").fetchall())

    for season in goal_seasons:
        cur.execute("DELETE FROM fato_gol WHERE temporada_id = ?", (season,))
    for season in card_seasons:
        cur.execute("DELETE FROM fato_cartao WHERE temporada_id = ?", (season,))

    goals = []
    cards = []
    for row in rows:
        common = (row["partida_id"], row["temporada_id"], row["rodada"], club_map[row["clube"]], player_map[row["jogador"]])
        if row["evento"] == "gol" and row["temporada_id"] in goal_seasons:
            goals.append((*common, row["minuto"], row["tipo"]))
        if row["evento"] == "cartao" and row["temporada_id"] in card_seasons:
            cards.append((*common, None, row["tipo"], row["minuto"], row["num_camisa"] or None))
    cur.executemany(
        "INSERT INTO fato_gol (partida_id, temporada_id, rodada, clube_id, jogador_id, minuto, tipo) VALUES (?, ?, ?, ?, ?, ?, ?)",
        goals,
    )
    cur.executemany(
        "INSERT INTO fato_cartao (partida_id, temporada_id, rodada, clube_id, jogador_id, posicao_id, tipo, minuto, num_camisa) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        cards,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Importa eventos antigos via Transfermarkt.")
    parser.add_argument("--start", type=int, default=2003)
    parser.add_argument("--end", type=int, default=2006)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--allow-partial", action="store_true", help="aplica linhas validas mesmo com erros auditados")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        jobs = []
        for season in range(args.start, args.end + 1):
            for round_ in season_rounds(cur, season):
                for match_id in schedule_ids(season, round_):
                    jobs.append((season, round_, match_id))
            print(f"{season}: partidas_transfermarkt={sum(1 for s, _, _ in jobs if s == season)}")

        parsed, errors = [], []
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(parse_match, mid, season, round_): (season, round_, mid) for season, round_, mid in jobs}
            for i, future in enumerate(as_completed(futures), start=1):
                season, round_, mid = futures[future]
                try:
                    rows, row_errors = future.result()
                except Exception as exc:
                    rows = []
                    row_errors = [{"temporada": season, "rodada": round_, "match_id": mid, "erro": f"falha download/parser: {exc}"}]
                parsed.extend(rows)
                errors.extend(row_errors)
                if i % 250 == 0:
                    print(f"processadas={i}/{len(jobs)}")

        rows, match_errors = attach_partidas(cur, parsed)
        errors.extend(match_errors)
        fields = [
            "source_match_id", "source_url", "partida_id", "temporada_id", "rodada", "data",
            "mandante", "visitante", "gols_mandante", "gols_visitante", "evento", "clube",
            "jogador", "tipo", "minuto", "placar_evento", "num_camisa", "match_method",
        ]
        write_csv(AUDIT_CSV, sorted(rows, key=lambda r: (r["temporada_id"], r["rodada"], r["partida_id"], r["evento"])), fields)
        write_csv(ERRORS_CSV, errors, ["temporada", "rodada", "match_id", "erro"])

        goals = sum(1 for r in rows if r["evento"] == "gol")
        cards = sum(1 for r in rows if r["evento"] == "cartao")
        print(f"eventos_validos={len(rows)} gols={goals} cartoes={cards} erros={len(errors)}")
        print(f"csv_auditoria={AUDIT_CSV}")
        print(f"csv_erros={ERRORS_CSV}")
        if errors and not args.allow_partial:
            print("modo=erro_sem_aplicar")
            return 1
        if args.apply:
            goal_seasons = {2003, 2004, 2005}
            card_seasons = {2003, 2004, 2005, 2006}
            with con:
                apply_rows(cur, rows, goal_seasons, card_seasons)
            print(f"temporadas_gols_substituidas={sorted(goal_seasons)}")
            print(f"temporadas_cartoes_substituidas={sorted(card_seasons)}")
            print("modo=aplicado")
        else:
            print("modo=dry-run")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
