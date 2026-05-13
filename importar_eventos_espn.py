from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import unicodedata
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


DB_PATH = Path("db/brasileirao.db")
EVENTS_CSV = Path("data/espn_eventos_2006_2020.csv")
ERRORS_CSV = Path("data/espn_eventos_2006_2020_erros.csv")
BR_TZ = timezone(timedelta(hours=-3))
ESPN_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/bra.1/scoreboard?dates={start}-{end}&limit=700"


TEAM_ALIASES = {
    "america mg": "America-MG",
    "america (mg)": "America-MG",
    "america mineiro": "America-MG",
    "america rn": "America-RN",
    "athletico pr": "Athletico-PR",
    "athletico paranaense": "Athletico-PR",
    "atletico go": "Atletico-GO",
    "atletico goianiense": "Atletico-GO",
    "atletico mg": "Atletico-MG",
    "atletico mineiro": "Atletico-MG",
    "atletico paranaense": "Athletico-PR",
    "avai": "Avai",
    "bahia": "Bahia",
    "barueri": "Barueri",
    "botafogo": "Botafogo-RJ",
    "bragantino": "Bragantino",
    "ceara": "Ceara",
    "chapecoense": "Chapecoense",
    "criciuma": "Criciuma",
    "corinthians": "Corinthians",
    "coritiba": "Coritiba",
    "cruzeiro": "Cruzeiro",
    "csa": "CSA",
    "figueirense": "Figueirense",
    "flamengo": "Flamengo",
    "fluminense": "Fluminense",
    "fortaleza": "Fortaleza",
    "goias": "Goias",
    "gremio": "Gremio",
    "gremio barueri": "Barueri",
    "gremio prudente": "Gremio Prudente",
    "guarani": "Guarani",
    "guarani sp": "Guarani",
    "internacional": "Internacional",
    "ipatinga": "Ipatinga",
    "joinville": "Joinville",
    "juventude": "Juventude",
    "nautico": "Nautico",
    "palmeiras": "Palmeiras",
    "parana": "Parana",
    "ponte preta": "Ponte Preta",
    "portuguesa": "Portuguesa",
    "red bull bragantino": "Bragantino",
    "santa cruz": "Santa Cruz",
    "santo andre": "Santo Andre",
    "esporte clube santo andre": "Santo Andre",
    "santos": "Santos",
    "sao caetano": "Sao Caetano",
    "sao paulo": "Sao Paulo",
    "sport": "Sport",
    "sport recife": "Sport",
    "vasco": "Vasco",
    "vasco da gama": "Vasco",
    "vitoria": "Vitoria",
}

POSITION_GROUPS = {
    "G": "Goleiro",
    "GK": "Goleiro",
    "D": "Zagueiro",
    "DF": "Zagueiro",
    "CD": "Zagueiro",
    "CB": "Zagueiro",
    "RB": "Zagueiro",
    "LB": "Zagueiro",
    "RWB": "Zagueiro",
    "LWB": "Zagueiro",
    "M": "Meio-campo",
    "MF": "Meio-campo",
    "DM": "Meio-campo",
    "CM": "Meio-campo",
    "RM": "Meio-campo",
    "LM": "Meio-campo",
    "AM": "Meio-campo",
    "F": "Atacante",
    "FW": "Atacante",
    "CF": "Atacante",
    "ST": "Atacante",
    "RW": "Atacante",
    "LW": "Atacante",
}


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(text.lower().replace("-", " ").split())


def canonical_team(name: str, season: int) -> str:
    key = normalize(name)
    if season == 2010 and key in {"barueri", "gremio barueri"}:
        return "Gremio Prudente"
    return TEAM_ALIASES.get(key, name)


def local_date(iso_datetime: str) -> str:
    dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
    return dt.astimezone(BR_TZ).strftime("%Y-%m-%d")


def parse_minute(display_value: str | None, seconds: float | int | None) -> int | None:
    if display_value:
        value = display_value.replace("'", "").strip()
        if "+" in value:
            base, extra = value.split("+", 1)
            try:
                return int(base) + int(extra)
            except ValueError:
                pass
        try:
            return int(value)
        except ValueError:
            pass
    if seconds is None:
        return None
    return max(1, round(float(seconds) / 60))


def position_group(position: str | None) -> str | None:
    if not position:
        return None
    code = position.split("-", 1)[0].strip().upper()
    if code == "SUB":
        return None
    return POSITION_GROUPS.get(code)


def goal_type(detail: dict) -> str:
    text = normalize((detail.get("type") or {}).get("text", ""))
    if detail.get("ownGoal") or "own goal" in text:
        return "Gol Contra"
    if detail.get("penaltyKick") or "penalty" in text:
        return "Penalti"
    if "free kick" in text:
        return "Falta"
    return "Normal"


def season_dates(cur: sqlite3.Cursor, season: int) -> tuple[str, str]:
    start, end = cur.execute(
        "SELECT MIN(data), MAX(data) FROM fato_partida WHERE temporada_id = ?",
        (season,),
    ).fetchone()
    if not start or not end:
        raise ValueError(f"temporada sem partidas no banco: {season}")
    return start.replace("-", ""), end.replace("-", "")


def fetch_scoreboard(start: str, end: str) -> dict:
    request = urllib.request.Request(
        ESPN_URL.format(start=start, end=end),
        headers={"User-Agent": "Mozilla/5.0 clube-analitico"},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def load_matches(cur: sqlite3.Cursor, season: int) -> list[dict]:
    rows = cur.execute(
        """
        SELECT p.partida_id, p.rodada, p.data, hm.nome, aw.nome,
               p.gols_mandante, p.gols_visitante
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        WHERE p.temporada_id = ?
        """,
        (season,),
    ).fetchall()
    return [
        {
            "key": (data, mandante, visitante, gols_mandante, gols_visitante),
            "date": datetime.strptime(data, "%Y-%m-%d").date(),
            "home": mandante,
            "away": visitante,
            "home_goals": gols_mandante,
            "away_goals": gols_visitante,
            "partida_id": partida_id,
            "rodada": rodada,
        }
        for partida_id, rodada, data, mandante, visitante, gols_mandante, gols_visitante in rows
    ]


def find_match(matches: list[dict], key: tuple[str, str, str, int, int]) -> tuple[dict | None, str]:
    event_date_s, home, away, home_goals, away_goals = key
    event_date = datetime.strptime(event_date_s, "%Y-%m-%d").date()
    exact = [m for m in matches if m["key"] == key]
    if len(exact) == 1:
        return exact[0], "exact"

    same_day_teams = [m for m in matches if m["key"][0] == event_date_s and m["home"] == home and m["away"] == away]
    if len(same_day_teams) == 1:
        return same_day_teams[0], "same_day_teams"

    same_day_swapped = [
        m for m in matches
        if m["key"][0] == event_date_s and m["home"] == away and m["away"] == home
        and m["home_goals"] == away_goals and m["away_goals"] == home_goals
    ]
    if len(same_day_swapped) == 1:
        return same_day_swapped[0], "same_day_swapped"

    near_teams_score = [
        m for m in matches
        if m["home"] == home and m["away"] == away
        and m["home_goals"] == home_goals and m["away_goals"] == away_goals
        and abs((m["date"] - event_date).days) <= 14
    ]
    if len(near_teams_score) == 1:
        return near_teams_score[0], "near_teams_score"

    near_teams = [
        m for m in matches
        if m["home"] == home and m["away"] == away
        and abs((m["date"] - event_date).days) <= 14
    ]
    if len(near_teams) == 1:
        return near_teams[0], "near_teams"
    return None, "not_found"


def athlete_name(athlete: dict, club_name: str, kind: str) -> str:
    player_name = (athlete.get("displayName") or "").strip()
    if player_name:
        return player_name
    return f"Nao informado {kind} ({club_name})"


def extract_season(cur: sqlite3.Cursor, season: int) -> tuple[list[dict], list[dict]]:
    start, end = season_dates(cur, season)
    scoreboard = fetch_scoreboard(start, end)
    matches = load_matches(cur, season)
    events: list[dict] = []
    errors: list[dict] = []
    event_ids = set()

    for event in scoreboard.get("events", []):
        event_ids.add(event.get("id"))
        comp = (event.get("competitions") or [{}])[0]
        competitors = comp.get("competitors") or []
        by_home_away = {c.get("homeAway"): c for c in competitors}
        home = by_home_away.get("home")
        away = by_home_away.get("away")
        if not home or not away:
            errors.append({"temporada": season, "source_event_id": event.get("id"), "erro": "sem mandante/visitante"})
            continue

        home_name = canonical_team(home["team"]["displayName"], season)
        away_name = canonical_team(away["team"]["displayName"], season)
        relevant_details = [
            detail for detail in (comp.get("details") or [])
            if detail.get("scoringPlay") or detail.get("yellowCard") or detail.get("redCard")
        ]
        if not relevant_details:
            continue

        key = (
            local_date(comp["date"]),
            home_name,
            away_name,
            int(home["score"]),
            int(away["score"]),
        )
        match, match_method = find_match(matches, key)
        if match is None:
            errors.append({"temporada": season, "source_event_id": event.get("id"), "erro": f"partida nao encontrada: {key}"})
            continue

        team_id_to_name = {
            str(home["team"]["id"]): home_name,
            str(away["team"]["id"]): away_name,
        }
        for detail in relevant_details:
            is_goal = bool(detail.get("scoringPlay"))
            is_card = bool(detail.get("yellowCard") or detail.get("redCard"))
            if not (is_goal or is_card):
                continue
            athletes = detail.get("athletesInvolved") or []
            athlete = athletes[0] if athletes else {}
            team_id = str((detail.get("team") or athlete.get("team") or {}).get("id"))
            club_name = team_id_to_name.get(team_id)
            if not club_name:
                errors.append({"temporada": season, "source_event_id": event.get("id"), "erro": f"aviso: evento sem clube mapeado: {team_id}"})
                continue

            raw_position = athlete.get("position")
            clock = detail.get("clock") or {}
            row = {
                "source": "ESPN",
                "source_event_id": event.get("id"),
                "source_url": f"https://www.espn.com/soccer/match/_/gameId/{event.get('id')}",
                "partida_id": match["partida_id"],
                "temporada_id": season,
                "rodada": match["rodada"],
                "data": key[0],
                "match_method": match_method,
                "clube": club_name,
                "jogador": athlete_name(athlete, club_name, "evento"),
                "posicao_espn": raw_position,
                "posicao": position_group(raw_position),
                "minuto": parse_minute(clock.get("displayValue"), clock.get("value")),
                "num_camisa": athlete.get("jersey"),
            }
            if is_goal:
                row.update({"evento": "gol", "tipo": goal_type(detail)})
                events.append(row)
            if is_card:
                row = dict(row)
                row.update({"evento": "cartao", "tipo": "Vermelho" if detail.get("redCard") else "Amarelo"})
                events.append(row)

    expected = cur.execute("SELECT COUNT(*) FROM fato_partida WHERE temporada_id = ?", (season,)).fetchone()[0]
    if len(event_ids) != expected:
        errors.append({"temporada": season, "source_event_id": "", "erro": f"aviso: quantidade inesperada de jogos ESPN: {len(event_ids)} de {expected}"})
    return events, errors


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def ensure_dimensions(cur: sqlite3.Cursor, events: list[dict]) -> tuple[dict, dict, dict]:
    club_map = dict(cur.execute("SELECT nome, clube_id FROM dim_clube").fetchall())
    for event in events:
        if event["posicao"]:
            cur.execute("INSERT OR IGNORE INTO dim_posicao (nome) VALUES (?)", (event["posicao"],))
    pos_map = dict(cur.execute("SELECT nome, posicao_id FROM dim_posicao").fetchall())

    for event in events:
        pos_id = pos_map.get(event["posicao"])
        cur.execute(
            "INSERT OR IGNORE INTO dim_jogador (nome, posicao_id) VALUES (?, ?)",
            (event["jogador"], pos_id),
        )
        if pos_id:
            cur.execute(
                "UPDATE dim_jogador SET posicao_id = COALESCE(posicao_id, ?) WHERE nome = ?",
                (pos_id, event["jogador"]),
            )
    player_map = dict(cur.execute("SELECT nome, jogador_id FROM dim_jogador").fetchall())
    return club_map, pos_map, player_map


def import_events(
    cur: sqlite3.Cursor,
    events: list[dict],
    goal_seasons: list[int],
    card_seasons: list[int],
) -> None:
    club_map, pos_map, player_map = ensure_dimensions(cur, events)
    for season in goal_seasons:
        cur.execute("DELETE FROM fato_gol WHERE temporada_id = ?", (season,))
    for season in card_seasons:
        cur.execute("DELETE FROM fato_cartao WHERE temporada_id = ?", (season,))

    goal_rows = []
    card_rows = []
    for event in events:
        common = (
            event["partida_id"],
            event["temporada_id"],
            event["rodada"],
            club_map[event["clube"]],
            player_map[event["jogador"]],
        )
        if event["evento"] == "gol" and event["temporada_id"] in goal_seasons:
            goal_rows.append((*common, event["minuto"], event["tipo"]))
        elif event["evento"] == "cartao" and event["temporada_id"] in card_seasons:
            card_rows.append((*common, pos_map.get(event["posicao"]), event["tipo"], event["minuto"], event["num_camisa"]))

    cur.executemany(
        "INSERT INTO fato_gol (partida_id, temporada_id, rodada, clube_id, jogador_id, minuto, tipo) VALUES (?, ?, ?, ?, ?, ?, ?)",
        goal_rows,
    )
    cur.executemany(
        """
        INSERT INTO fato_cartao (
            partida_id, temporada_id, rodada, clube_id, jogador_id,
            posicao_id, tipo, minuto, num_camisa
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        card_rows,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Importa gols e cartoes da Serie A via ESPN.")
    parser.add_argument("--start", type=int, default=2006)
    parser.add_argument("--end", type=int, default=2020)
    parser.add_argument("--replace-goals-through", type=int, default=2013)
    parser.add_argument("--apply", action="store_true", help="grava no banco")
    args = parser.parse_args()
    seasons = list(range(args.start, args.end + 1))

    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        all_events: list[dict] = []
        all_errors: list[dict] = []
        for season in seasons:
            events, errors = extract_season(cur, season)
            all_events.extend(events)
            all_errors.extend(errors)
            goals = sum(1 for e in events if e["evento"] == "gol")
            cards = sum(1 for e in events if e["evento"] == "cartao")
            print(f"{season}: gols={goals} cartoes={cards} erros={len(errors)}")

        event_fields = [
            "source", "source_event_id", "source_url", "partida_id", "temporada_id",
            "rodada", "data", "match_method", "evento", "clube", "jogador", "posicao_espn",
            "posicao", "tipo", "minuto", "num_camisa",
        ]
        write_csv(EVENTS_CSV, all_events, event_fields)
        write_csv(ERRORS_CSV, all_errors, ["temporada", "source_event_id", "erro"])

        goals = sum(1 for e in all_events if e["evento"] == "gol")
        cards = sum(1 for e in all_events if e["evento"] == "cartao")
        no_player = sum(1 for e in all_events if e["jogador"].startswith("Nao informado"))
        no_position_cards = sum(1 for e in all_events if e["evento"] == "cartao" and not e["posicao"])
        print(f"total_gols={goals} total_cartoes={cards}")
        print(f"sem_jogador={no_player} cartoes_sem_posicao={no_position_cards}")
        print(f"csv_eventos={EVENTS_CSV}")
        print(f"csv_erros={ERRORS_CSV}")

        fatal_errors = [e for e in all_errors if not e["erro"].startswith("aviso:")]
        if fatal_errors:
            print("modo=erro_sem_aplicar")
            return 1

        if args.apply:
            goal_seasons = [s for s in seasons if s <= args.replace_goals_through]
            card_seasons = seasons
            with con:
                import_events(cur, all_events, goal_seasons, card_seasons)
            print(f"temporadas_gols_substituidas={goal_seasons}")
            print(f"temporadas_cartoes_substituidas={card_seasons}")
            print("modo=aplicado")
        else:
            print("modo=dry-run")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
