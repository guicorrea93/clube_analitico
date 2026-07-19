"""Gera base derivada de gols detalhados das Copas via StatsBomb Open Data."""
from __future__ import annotations

import csv
import json
import math
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data" / "worldcup_wikipedia"
OUT_JSON = DATA_DIR / "gols_detalhados_statsbomb.json"
OUT_CSV = DATA_DIR / "gols_detalhados_statsbomb.csv"
RAW_BASE = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"
COMPETITION_ID = 43
SEASONS = {
    2022: 106,
    2018: 3,
    1990: 55,
    1986: 54,
    1974: 51,
    1970: 272,
    1962: 270,
    1958: 269,
}

BODY_PART_PT = {
    "Head": "Cabeça",
    "Left Foot": "Pé esquerdo",
    "Right Foot": "Pé direito",
    "Other": "Outra parte do corpo",
}
SHOT_TYPE_PT = {
    "Open Play": "Bola rolando",
    "Penalty": "Pênalti",
    "Free Kick": "Falta",
    "Corner": "Escanteio",
    "Kick Off": "Saída de bola",
}
STAGE_PT = {
    "1st Group Stage": "Primeira fase",
    "Group Stage": "Fase de grupos",
    "Round of 16": "Oitavas de final",
    "Quarter-finals": "Quartas de final",
    "Semi-finals": "Semifinal",
    "3rd Place Final": "Terceiro lugar",
    "Final": "Final",
}
TEAM_PT = {
    "Argentina": "Argentina",
    "Australia": "Austrália",
    "Belgium": "Bélgica",
    "Brazil": "Brasil",
    "Cameroon": "Camarões",
    "Canada": "Canadá",
    "Colombia": "Colômbia",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croácia",
    "Czechoslovakia": "Tchecoslováquia",
    "Denmark": "Dinamarca",
    "Ecuador": "Equador",
    "Egypt": "Egito",
    "England": "Inglaterra",
    "France": "França",
    "German DR": "Alemanha Oriental",
    "Germany": "Alemanha",
    "Ghana": "Gana",
    "Iceland": "Islândia",
    "Iran": "Irã",
    "Italy": "Itália",
    "Japan": "Japão",
    "Mexico": "México",
    "Morocco": "Marrocos",
    "Netherlands": "Países Baixos",
    "Nigeria": "Nigéria",
    "Panama": "Panamá",
    "Peru": "Peru",
    "Poland": "Polônia",
    "Portugal": "Portugal",
    "Qatar": "Catar",
    "Romania": "Romênia",
    "Russia": "Rússia",
    "Saudi Arabia": "Arábia Saudita",
    "Senegal": "Senegal",
    "Serbia": "Sérvia",
    "South Korea": "Coreia do Sul",
    "Spain": "Espanha",
    "Sweden": "Suécia",
    "Switzerland": "Suíça",
    "Tunisia": "Tunísia",
    "United States": "Estados Unidos",
    "Uruguay": "Uruguai",
    "Wales": "País de Gales",
}
TECHNIQUE_PT = {
    "Normal": "Normal",
    "Volley": "Voleio",
    "Half Volley": "Meio voleio",
    "Lob": "Cobertura",
    "Backheel": "Letra/calcanhar",
    "Diving Header": "Peixinho",
    "Overhead Kick": "Bicicleta",
}
PLAY_PATTERN_PT = {
    "Regular Play": "Bola rolando",
    "From Corner": "Escanteio",
    "From Free Kick": "Falta",
    "From Throw In": "Lateral",
    "From Counter": "Contra-ataque",
    "From Goal Kick": "Tiro de meta",
    "From Keeper": "Reposição do goleiro",
    "From Kick Off": "Saída de bola",
    "Other": "Outra jogada",
}


def derive_situacao(shot_type: str, play_pattern: str) -> str:
    """Situacao do gol: Penalti/Falta/Escanteio/Contra-ataque/Bola rolando."""
    if shot_type == "Penalty":
        return "Pênalti"
    if shot_type == "Free Kick":
        return "Falta"
    return {
        "From Corner": "Escanteio",
        "From Free Kick": "Falta",
        "From Counter": "Contra-ataque",
    }.get(play_pattern, "Bola rolando")


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "clube-analitico-codex/1.0"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def safe_get_name(value: dict | None) -> str:
    return (value or {}).get("name", "") or ""


def team_name(value: dict | None, side: str = "") -> str:
    value = value or {}
    name = value.get("name") or value.get(f"{side}_team_name") or value.get("team_name") or ""
    return TEAM_PT.get(name, name)


def shot_distance_m(location: list | None) -> float | None:
    if not location or len(location) < 2:
        return None
    # StatsBomb usa campo 120x80. Aproxima para 105x68 m e mede ate o centro do gol.
    x_m = float(location[0]) * 105.0 / 120.0
    y_m = float(location[1]) * 68.0 / 80.0
    goal_x_m = 105.0
    goal_y_m = 34.0
    return round(math.hypot(goal_x_m - x_m, goal_y_m - y_m), 1)


def shot_zone(location: list | None, shot_type: str) -> str:
    if shot_type == "Penalty":
        return "Pênalti"
    if not location or len(location) < 2:
        return "Não informado"
    x, y = float(location[0]), float(location[1])
    if x >= 114 and 30 <= y <= 50:
        return "Pequena área"
    if x >= 102 and 18 <= y <= 62:
        return "Dentro da área"
    return "Fora da área"


def stage_name(match: dict) -> str:
    stage = safe_get_name(match.get("competition_stage")) or safe_get_name(match.get("match_status")) or ""
    return STAGE_PT.get(stage, stage)


def match_key(match: dict) -> str:
    return str(match.get("match_id") or "")


def opponent_for(team: str, match: dict) -> str:
    home = team_name(match.get("home_team"), "home")
    away = team_name(match.get("away_team"), "away")
    if team == home:
        return away
    if team == away:
        return home
    return ""


def is_goal_event(event: dict) -> bool:
    shot = event.get("shot") or {}
    return (
        event.get("period") != 5
        and safe_get_name(event.get("type")) == "Shot"
        and safe_get_name(shot.get("outcome")) == "Goal"
    )


def derive_goal(event: dict, match: dict, year: int) -> dict:
    shot = event.get("shot") or {}
    loc = event.get("location") or []
    end_loc = shot.get("end_location") or []
    team = team_name(event.get("team"))
    player = safe_get_name(event.get("player"))
    body = safe_get_name(shot.get("body_part"))
    shot_type = safe_get_name(shot.get("type"))
    technique = safe_get_name(shot.get("technique"))
    play_pattern = safe_get_name(event.get("play_pattern"))
    zone = shot_zone(loc, shot_type)
    return {
        "ano": year,
        "statsbomb_partida_id": match.get("match_id"),
        "data": match.get("match_date", ""),
        "fase": stage_name(match),
        "mandante": team_name(match.get("home_team"), "home"),
        "visitante": team_name(match.get("away_team"), "away"),
        "placar_mandante": match.get("home_score"),
        "placar_visitante": match.get("away_score"),
        "selecao": team,
        "adversario": opponent_for(team, match),
        "jogador": player,
        "minuto": event.get("minute"),
        "segundo": event.get("second"),
        "periodo": event.get("period"),
        "parte_corpo": body,
        "parte_corpo_pt": BODY_PART_PT.get(body, body or "Não informado"),
        "tipo_chute": shot_type,
        "tipo_chute_pt": SHOT_TYPE_PT.get(shot_type, shot_type or "Não informado"),
        "tecnica": technique,
        "tecnica_pt": TECHNIQUE_PT.get(technique, technique or "Não informado"),
        "padrao_jogada": play_pattern,
        "padrao_jogada_pt": PLAY_PATTERN_PT.get(play_pattern, play_pattern or "Não informado"),
        "situacao": derive_situacao(shot_type, play_pattern),
        "xg": round(float(shot.get("statsbomb_xg") or 0), 4),
        "x": loc[0] if len(loc) > 0 else None,
        "y": loc[1] if len(loc) > 1 else None,
        "fim_x": end_loc[0] if len(end_loc) > 0 else None,
        "fim_y": end_loc[1] if len(end_loc) > 1 else None,
        "fim_z": end_loc[2] if len(end_loc) > 2 else None,
        "zona": zone,
        "distancia_m": shot_distance_m(loc),
        "eh_penalti": shot_type == "Penalty",
        "eh_falta": shot_type == "Free Kick",
        "eh_cabeca": body == "Head",
        "eh_pe_direito": body == "Right Foot",
        "eh_pe_esquerdo": body == "Left Foot",
        "eh_fora_area": zone == "Fora da área",
        "eh_primeira": bool(shot.get("first_time")),
        "eh_gol_aberto": bool(shot.get("open_goal")),
        "eh_voleio": technique in {"Volley", "Half Volley"},
        "fonte": "StatsBomb Open Data",
    }


def collect_goals() -> list[dict]:
    goals: list[dict] = []
    for year, season_id in SEASONS.items():
        matches_url = f"{RAW_BASE}/matches/{COMPETITION_ID}/{season_id}.json"
        matches = fetch_json(matches_url)
        print(f"{year}: {len(matches)} partidas")
        for idx, match in enumerate(matches, 1):
            event_url = f"{RAW_BASE}/events/{match_key(match)}.json"
            try:
                events = fetch_json(event_url)
            except (urllib.error.URLError, TimeoutError) as exc:
                print(f"  falha em {match_key(match)}: {exc}")
                continue
            match_goals = [derive_goal(e, match, year) for e in events if is_goal_event(e)]
            goals.extend(match_goals)
            if idx % 16 == 0 or idx == len(matches):
                print(f"  {idx}/{len(matches)} partidas, {len(goals)} gols acumulados")
            time.sleep(0.03)
    return sorted(goals, key=lambda r: (r["ano"], r["data"], r["statsbomb_partida_id"], r["periodo"] or 0, r["minuto"] or 0, r["segundo"] or 0))


def write_outputs(goals: list[dict]) -> None:
    payload = {
        "fonte": {
            "nome": "StatsBomb Open Data",
            "url": "https://github.com/statsbomb/open-data",
            "observacao": "Base derivada de eventos de chute com desfecho gol nas Copas disponíveis no repositório aberto da StatsBomb.",
        },
        "cobertura": [{"ano": year, "competition_id": COMPETITION_ID, "season_id": sid} for year, sid in SEASONS.items()],
        "gols": goals,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = list(goals[0].keys()) if goals else []
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(goals)
    print(f"JSON: {OUT_JSON} ({len(goals)} gols)")
    print(f"CSV:  {OUT_CSV}")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    goals = collect_goals()
    write_outputs(goals)


if __name__ == "__main__":
    main()
