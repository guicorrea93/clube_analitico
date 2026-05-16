from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sqlite3
import time
import unicodedata
import urllib.request
from dataclasses import dataclass
from pathlib import Path


DB_PATH = Path("db/brasileirao.db")
CACHE_DIR = Path("data/cache/ogol")
AUDIT_CSV = Path("data/ogol_gols_divergentes_auditoria.csv")
ADMIN_RESULTS_FILE = Path("data/partidas_resultado_administrativo.csv")

BASE = "https://www.ogol.com.br"
HEADERS = {"User-Agent": "Mozilla/5.0 clube-analitico"}

EDITION_IDS = {
    2003: 2489,
    2004: 457,
    2005: 865,
    2006: 1247,
    2007: 1425,
    2008: 2003,
    2009: 5268,
    2010: 13881,
    2011: 21248,
    2013: 56933,
}

TEAM_ALIASES = {
    "america rn": "America-RN",
    "america mineiro": "America-MG",
    "america mg": "America-MG",
    "atletico goianiense": "Atletico-GO",
    "atletico mg": "Atletico-MG",
    "atletico mineiro": "Atletico-MG",
    "atletico paranaense": "Athletico-PR",
    "athletico paranaense": "Athletico-PR",
    "avai": "Avai",
    "avai fc": "Avai",
    "botafogo": "Botafogo-RJ",
    "botafogo rj": "Botafogo-RJ",
    "bragantino": "Bragantino",
    "brasiliense": "Brasiliense",
    "ceara": "Ceara",
    "corinthians": "Corinthians",
    "coritiba": "Coritiba",
    "criciuma": "Criciuma",
    "cruzeiro": "Cruzeiro",
    "figueirense": "Figueirense",
    "flamengo": "Flamengo",
    "fluminense": "Fluminense",
    "goias": "Goias",
    "gremio barueri": "Gremio Prudente",
    "gremio": "Gremio",
    "gremio prudente": "Gremio Prudente",
    "guarani": "Guarani",
    "internacional": "Internacional",
    "ipatinga": "Ipatinga",
    "juventude": "Juventude",
    "nautico": "Nautico",
    "parana": "Parana",
    "paysandu": "Paysandu",
    "ponte preta": "Ponte Preta",
    "portuguesa": "Portuguesa",
    "santa cruz": "Santa Cruz",
    "santos": "Santos",
    "sao caetano": "Sao Caetano",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
    "vitoria": "Vitoria",
    "vasco": "Vasco",
}


@dataclass
class Match:
    partida_id: int
    temporada_id: int
    rodada: int
    data: str
    mandante: str
    visitante: str
    gols_mandante: int
    gols_visitante: int
    gols_banco: int


@dataclass
class OgolGame:
    source_id: str
    source_url: str
    data: str
    mandante: str
    visitante: str
    gols_mandante: int
    gols_visitante: int


def normalize(value: str) -> str:
    text = html.unescape(value or "")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).lower()
    return " ".join(text.split())


def canonical_team(value: str) -> str:
    key = normalize(value)
    return TEAM_ALIASES.get(key, html.unescape(value).strip())


def clean_text(value: str) -> str:
    value = re.sub(r"<script.*?</script>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<style.*?</style>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fetch(url: str, cache_name: str, refresh: bool = False) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / cache_name
    if path.exists() and not refresh:
        return path.read_text(encoding="utf-8", errors="ignore")
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=45) as response:
                raw = response.read()
                charset = response.headers.get_content_charset() or "utf-8"
                text = raw.decode(charset, "ignore")
            break
        except Exception as exc:
            last_error = exc
            time.sleep(1.0 + attempt)
    else:
        raise RuntimeError(f"falha ao baixar {url}: {last_error}")
    path.write_text(text, encoding="utf-8")
    time.sleep(0.6)
    return text


def load_admin_result_ids() -> set[int]:
    if not ADMIN_RESULTS_FILE.exists():
        return set()
    with ADMIN_RESULTS_FILE.open(encoding="utf-8-sig", newline="") as f:
        return {int(row["partida_id"]) for row in csv.DictReader(f) if row.get("partida_id")}


def load_goal_mismatches(con: sqlite3.Connection) -> list[Match]:
    con.row_factory = sqlite3.Row
    admin_result_ids = load_admin_result_ids()
    rows = con.execute(
        """
        SELECT p.partida_id, p.temporada_id, p.rodada, p.data,
               hm.nome AS mandante, aw.nome AS visitante,
               p.gols_mandante, p.gols_visitante,
               COUNT(g.gol_id) AS gols_banco
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        LEFT JOIN fato_gol g ON g.partida_id = p.partida_id
        GROUP BY p.partida_id
        HAVING (p.gols_mandante + p.gols_visitante) <> COUNT(g.gol_id)
        ORDER BY p.temporada_id, p.rodada, p.data, p.partida_id
        """
    ).fetchall()
    return [Match(**dict(row)) for row in rows if int(row["partida_id"]) not in admin_result_ids]


def parse_calendar(season: int, refresh: bool = False) -> list[OgolGame]:
    edition_id = EDITION_IDS[season]
    out: list[OgolGame] = []
    seen: set[str] = set()
    for page in range(1, 15):
        url = f"{BASE}/edicao/-/{edition_id}/calendario?page={page}"
        text = fetch(url, f"calendario_{season}_{edition_id}_p{page}.html", refresh)
        before = len(seen)
        for row in re.findall(r"<tr\b.*?</tr>", text, flags=re.S | re.I):
            if "/jogo/" not in row:
                continue
            link = re.search(r'href="(/jogo/(\d{4}-\d{2}-\d{2})-[^"]+/(\d+))"', row)
            if not link:
                continue
            source_id = link.group(3)
            if source_id in seen:
                continue
            teams = re.findall(r'<td class="[^"]*\btext\b[^"]*"[^>]*>.*?<a [^>]*>(.*?)</a>', row, flags=re.S | re.I)
            score = re.search(r'>(\d+)-(\d+)<', row)
            if len(teams) < 2 or not score:
                continue
            seen.add(source_id)
            out.append(
                OgolGame(
                    source_id=source_id,
                    source_url=f"{BASE}{link.group(1)}",
                    data=link.group(2),
                    mandante=canonical_team(clean_text(teams[0])),
                    visitante=canonical_team(clean_text(teams[1])),
                    gols_mandante=int(score.group(1)),
                    gols_visitante=int(score.group(2)),
                )
            )
        if len(seen) == before:
            break
    return out


def find_ogol_game(match: Match, calendar: list[OgolGame]) -> tuple[OgolGame | None, str]:
    same_teams = [
        game
        for game in calendar
        if game.mandante == match.mandante and game.visitante == match.visitante
    ]
    if not same_teams:
        return None, "partida nao encontrada no calendario ogol"
    exact = [game for game in same_teams if game.data == match.data]
    if len(exact) == 1:
        return exact[0], "exact"
    same_score = [
        game
        for game in same_teams
        if (game.gols_mandante, game.gols_visitante) == (match.gols_mandante, match.gols_visitante)
    ]
    if len(same_score) == 1:
        return same_score[0], "same_score"
    if len(same_teams) == 1:
        return same_teams[0], "same_teams"
    return None, f"ambigua: {len(same_teams)} jogos com mesmos times"


def extract_jsonld_game(text: str) -> dict:
    for block in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, flags=re.S | re.I):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if data.get("@type") == "SportsEvent":
            return data
    return {}


def parse_game_header(text: str, fallback: OgolGame) -> OgolGame:
    data = extract_jsonld_game(text)
    name = html.unescape(data.get("name", ""))
    score = re.search(r"\b(\d+)-(\d+)\b", name)
    start = data.get("startDate", "")
    home = data.get("homeTeam", {}).get("name", fallback.mandante)
    away = data.get("awayTeam", {}).get("name", fallback.visitante)
    return OgolGame(
        source_id=fallback.source_id,
        source_url=fallback.source_url,
        data=start[:10] if re.match(r"\d{4}-\d{2}-\d{2}", start) else fallback.data,
        mandante=canonical_team(home),
        visitante=canonical_team(away),
        gols_mandante=int(score.group(1)) if score else fallback.gols_mandante,
        gols_visitante=int(score.group(2)) if score else fallback.gols_visitante,
    )


def parse_goal_minutes(events_html: str) -> list[int]:
    goals: list[int] = []
    for match in re.finditer(r'<span[^>]+title="Gols"[^>]*>.*?</span>\s*<div>(.*?)</div>', events_html, flags=re.S | re.I):
        for minute in re.findall(r"(\d+)(?:\+\d+)?\s*'", html.unescape(match.group(1))):
            value = int(minute)
            if value < 200:
                goals.append(value)
    return goals


def parse_goals_from_report(text: str, header: OgolGame) -> list[dict]:
    report_match = re.search(r'<div id="game_report".*?</div><div class="box">', text, flags=re.S | re.I)
    if not report_match:
        report_match = re.search(r'<div id="game_report".*?</div></div><div class="card-data', text, flags=re.S | re.I)
    if not report_match:
        return []
    report = report_match.group(0)
    cols = re.findall(r'<div class="zz-tpl-col is-6 fl-c">(.*?)(?=<div class="zz-tpl-col is-6 fl-c">|</div><div class="zz-tpl-row game_report">)', report, flags=re.S | re.I)
    goals: list[dict] = []
    for idx, col in enumerate(cols[:2]):
        club = header.mandante if idx == 0 else header.visitante
        for player in re.findall(r'<div class="player[^"]*.*?</div></div></div>', col, flags=re.S | re.I):
            name_match = re.search(r'<div class="text"><a [^>]*>(.*?)</a></div>', player, flags=re.S | re.I)
            events_match = re.search(r'<div class="events">(.*?)</div></div>$', player, flags=re.S | re.I)
            if not name_match or not events_match:
                continue
            minutes = parse_goal_minutes(events_match.group(1))
            for minute in minutes:
                goals.append(
                    {
                        "source_id": header.source_id,
                        "source_url": header.source_url,
                        "clube": club,
                        "jogador": clean_text(name_match.group(1)),
                        "minuto": minute,
                        "tipo": "Normal",
                    }
                )
    return goals


def parse_goals_from_summary(text: str, header: OgolGame) -> list[dict]:
    goals = []
    # No cabeçalho do ogol, "right" é o mandante e "left" é o visitante.
    for side, club in (("right", header.mandante), ("left", header.visitante)):
        block_match = re.search(
            rf'<div class="match-header-scorers {side}">\s*(.*?)\s*</div>',
            text,
            flags=re.S | re.I,
        )
        if not block_match:
            continue
        for player, minutes_text in re.findall(
            r'<a href="/jogador/[^"]+">(.*?)</a>\s*<span class="time">\s*([^<]+)</span>',
            block_match.group(1),
            flags=re.S | re.I,
        ):
            for minute in re.findall(r"(\d+)(?:\+\d+)?\s*'", html.unescape(minutes_text)):
                value = int(minute)
                if value >= 200:
                    continue
                goals.append(
                    {
                        "source_id": header.source_id,
                        "source_url": header.source_url,
                        "clube": club,
                        "jogador": clean_text(player),
                        "minuto": value,
                        "tipo": "Normal",
                    }
                )
    return goals


def parse_ogol_match(game: OgolGame, refresh: bool = False) -> tuple[OgolGame, list[dict]]:
    text = fetch(game.source_url, f"jogo_{game.source_id}.html", refresh)
    header = parse_game_header(text, game)
    goals = parse_goals_from_summary(text, header)
    if not goals:
        goals = parse_goals_from_report(text, header)
    return header, goals


def get_id(cur: sqlite3.Cursor, table: str, id_col: str, name: str) -> int:
    row = cur.execute(f"SELECT {id_col} FROM {table} WHERE nome = ?", (name,)).fetchone()
    if row:
        return int(row[0])
    cur.execute(f"INSERT INTO {table} (nome) VALUES (?)", (name,))
    return int(cur.lastrowid)


def apply_goals(con: sqlite3.Connection, match: Match, goals: list[dict]) -> None:
    cur = con.cursor()
    club_ids = {row[1]: row[0] for row in cur.execute("SELECT clube_id, nome FROM dim_clube")}
    cur.execute("DELETE FROM fato_gol WHERE partida_id = ?", (match.partida_id,))
    for goal in goals:
        club_id = club_ids[goal["clube"]]
        player_id = get_id(cur, "dim_jogador", "jogador_id", goal["jogador"])
        cur.execute(
            """
            INSERT INTO fato_gol (partida_id, temporada_id, rodada, clube_id, jogador_id, minuto, tipo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (match.partida_id, match.temporada_id, match.rodada, club_id, player_id, goal["minuto"], goal["tipo"]),
        )


def write_audit(rows: list[dict], path: Path = AUDIT_CSV) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "status", "acao", "partida_id", "temporada", "rodada", "data_banco", "data_ogol",
        "mandante", "visitante", "placar_banco", "placar_ogol", "gols_banco",
        "gols_ogol", "match_method", "source_id", "source_url", "detalhe",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Aplica apenas casos status=ok.")
    parser.add_argument("--refresh", action="store_true", help="Ignora cache local do ogol.")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    con = sqlite3.connect(DB_PATH)
    matches = load_goal_mismatches(con)
    if args.limit:
        matches = matches[: args.limit]
    seasons = sorted({match.temporada_id for match in matches if match.temporada_id in EDITION_IDS})
    calendars = {season: parse_calendar(season, args.refresh) for season in seasons}

    audit: list[dict] = []
    applied = 0
    for match in matches:
        if match.temporada_id not in calendars:
            audit.append({
                "status": "erro", "acao": "ignorar", "partida_id": match.partida_id,
                "temporada": match.temporada_id, "rodada": match.rodada,
                "data_banco": match.data, "data_ogol": "", "mandante": match.mandante,
                "visitante": match.visitante,
                "placar_banco": f"{match.gols_mandante}-{match.gols_visitante}",
                "placar_ogol": "", "gols_banco": match.gols_banco, "gols_ogol": "",
                "match_method": "", "source_id": "", "source_url": "",
                "detalhe": "temporada sem id de edicao ogol configurado",
            })
            continue
        game, method = find_ogol_game(match, calendars[match.temporada_id])
        if not game:
            audit.append({
                "status": "erro", "acao": "pesquisar_manual", "partida_id": match.partida_id,
                "temporada": match.temporada_id, "rodada": match.rodada,
                "data_banco": match.data, "data_ogol": "", "mandante": match.mandante,
                "visitante": match.visitante,
                "placar_banco": f"{match.gols_mandante}-{match.gols_visitante}",
                "placar_ogol": "", "gols_banco": match.gols_banco, "gols_ogol": "",
                "match_method": method, "source_id": "", "source_url": "",
                "detalhe": method,
            })
            continue
        header, goals = parse_ogol_match(game, args.refresh)
        placar_banco = (match.gols_mandante, match.gols_visitante)
        placar_ogol = (header.gols_mandante, header.gols_visitante)
        expected_goals = sum(placar_ogol)
        source_goal_count = len(goals)
        status = "ok" if placar_banco == placar_ogol and source_goal_count == expected_goals else "conflito"
        action = "aplicar_gols" if status == "ok" else "revisar"
        detail = "; ".join(f"{g['clube']} - {g['jogador']} {g['minuto']}'" for g in goals)
        audit.append({
            "status": status, "acao": action, "partida_id": match.partida_id,
            "temporada": match.temporada_id, "rodada": match.rodada,
            "data_banco": match.data, "data_ogol": header.data, "mandante": match.mandante,
            "visitante": match.visitante,
            "placar_banco": f"{match.gols_mandante}-{match.gols_visitante}",
            "placar_ogol": f"{header.gols_mandante}-{header.gols_visitante}",
            "gols_banco": match.gols_banco, "gols_ogol": source_goal_count,
            "match_method": method, "source_id": header.source_id, "source_url": header.source_url,
            "detalhe": detail or "sem gols extraidos",
        })
        if args.apply and status == "ok":
            apply_goals(con, match, goals)
            applied += 1

    if args.apply:
        con.commit()
    con.close()
    write_audit(audit)
    counts: dict[str, int] = {}
    for row in audit:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print(f"auditoria={AUDIT_CSV}")
    print(f"partidas={len(audit)} status={counts} aplicadas={applied}")
    print("modo=aplicado" if args.apply else "modo=dry-run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
