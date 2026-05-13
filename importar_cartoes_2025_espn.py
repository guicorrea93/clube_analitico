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
OUTPUT_CSV = Path("data/espn_cartoes_2025.csv")
SEASON = 2025
ESPN_SCOREBOARD_URL = (
    "https://site.api.espn.com/apis/site/v2/sports/soccer/bra.1/"
    "scoreboard?dates=20250329-20251207&limit=500"
)
BR_TZ = timezone(timedelta(hours=-3))

TEAM_ALIASES = {
    "atletico mg": "Atletico-MG",
    "atlético mg": "Atletico-MG",
    "botafogo": "Botafogo-RJ",
    "ceara": "Ceara",
    "ceará": "Ceara",
    "gremio": "Gremio",
    "grêmio": "Gremio",
    "red bull bragantino": "Bragantino",
    "bragantino": "Bragantino",
    "sao paulo": "Sao Paulo",
    "são paulo": "Sao Paulo",
    "vasco da gama": "Vasco",
    "vitoria": "Vitoria",
    "vitória": "Vitoria",
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


def canonical_team(name: str) -> str:
    key = normalize(name)
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


def fetch_scoreboard() -> dict:
    request = urllib.request.Request(
        ESPN_SCOREBOARD_URL,
        headers={"User-Agent": "Mozilla/5.0 clube-analitico"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def load_match_map(cur: sqlite3.Cursor) -> dict[tuple[str, str, str, int, int], dict]:
    rows = cur.execute(
        """
        SELECT p.partida_id, p.rodada, p.data, hm.nome, aw.nome,
               p.gols_mandante, p.gols_visitante
        FROM fato_partida p
        JOIN dim_clube hm ON hm.clube_id = p.mandante_id
        JOIN dim_clube aw ON aw.clube_id = p.visitante_id
        WHERE p.temporada_id = ?
        """,
        (SEASON,),
    ).fetchall()
    return {
        (data, mandante, visitante, gols_mandante, gols_visitante): {
            "partida_id": partida_id,
            "rodada": rodada,
        }
        for partida_id, rodada, data, mandante, visitante, gols_mandante, gols_visitante in rows
    }


def extract_cards(scoreboard: dict, match_map: dict[tuple[str, str, str, int, int], dict]) -> tuple[list[dict], list[str]]:
    cards: list[dict] = []
    errors: list[str] = []
    event_ids = set()

    for event in scoreboard.get("events", []):
        event_ids.add(event.get("id"))
        comp = (event.get("competitions") or [{}])[0]
        competitors = comp.get("competitors") or []
        by_home_away = {c.get("homeAway"): c for c in competitors}
        home = by_home_away.get("home")
        away = by_home_away.get("away")
        if not home or not away:
            errors.append(f"evento sem mandante/visitante: {event.get('id')}")
            continue

        home_name = canonical_team(home["team"]["displayName"])
        away_name = canonical_team(away["team"]["displayName"])
        match_key = (
            local_date(comp["date"]),
            home_name,
            away_name,
            int(home["score"]),
            int(away["score"]),
        )
        match = match_map.get(match_key)
        if match is None:
            errors.append(f"partida nao encontrada: {event.get('id')} {match_key}")
            continue

        team_id_to_name = {
            home["team"]["id"]: home_name,
            away["team"]["id"]: away_name,
        }
        for detail in comp.get("details") or []:
            if not (detail.get("yellowCard") or detail.get("redCard")):
                continue
            team_id = str((detail.get("team") or {}).get("id"))
            club_name = team_id_to_name.get(team_id)
            if not club_name:
                errors.append(f"cartao sem clube mapeado: {event.get('id')} {detail}")
                continue

            athletes = detail.get("athletesInvolved") or []
            athlete = athletes[0] if athletes else {}
            player_name = (athlete.get("displayName") or "").strip()
            if not player_name:
                player_name = f"Nao informado ({club_name})"
            raw_position = athlete.get("position")
            card_type = "Vermelho" if detail.get("redCard") else "Amarelo"
            clock = detail.get("clock") or {}
            minute = parse_minute(clock.get("displayValue"), clock.get("value"))
            cards.append(
                {
                    "source": "ESPN",
                    "source_event_id": event.get("id"),
                    "source_url": f"https://www.espn.com/soccer/match/_/gameId/{event.get('id')}",
                    "partida_id": match["partida_id"],
                    "temporada_id": SEASON,
                    "rodada": match["rodada"],
                    "data": match_key[0],
                    "clube": club_name,
                    "jogador": player_name,
                    "posicao_espn": raw_position,
                    "posicao": position_group(raw_position),
                    "tipo": card_type,
                    "minuto": minute,
                    "num_camisa": athlete.get("jersey"),
                }
            )

    if len(event_ids) != 380:
        errors.append(f"quantidade inesperada de jogos ESPN: {len(event_ids)}")
    return cards, errors


def write_audit_csv(cards: list[dict]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "source",
        "source_event_id",
        "source_url",
        "partida_id",
        "temporada_id",
        "rodada",
        "data",
        "clube",
        "jogador",
        "posicao_espn",
        "posicao",
        "tipo",
        "minuto",
        "num_camisa",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cards)


def import_cards(cur: sqlite3.Cursor, cards: list[dict]) -> None:
    club_map = dict(cur.execute("SELECT nome, clube_id FROM dim_clube").fetchall())
    pos_map = dict(cur.execute("SELECT nome, posicao_id FROM dim_posicao").fetchall())

    for card in cards:
        pos_name = card["posicao"]
        if pos_name:
            cur.execute("INSERT OR IGNORE INTO dim_posicao (nome) VALUES (?)", (pos_name,))
    pos_map = dict(cur.execute("SELECT nome, posicao_id FROM dim_posicao").fetchall())

    for card in cards:
        pos_id = pos_map.get(card["posicao"])
        cur.execute(
            "INSERT OR IGNORE INTO dim_jogador (nome, posicao_id) VALUES (?, ?)",
            (card["jogador"], pos_id),
        )
        if pos_id:
            cur.execute(
                "UPDATE dim_jogador SET posicao_id = COALESCE(posicao_id, ?) WHERE nome = ?",
                (pos_id, card["jogador"]),
            )

    player_map = dict(cur.execute("SELECT nome, jogador_id FROM dim_jogador").fetchall())
    cur.execute("DELETE FROM fato_cartao WHERE temporada_id = ?", (SEASON,))
    rows = []
    for card in cards:
        rows.append(
            (
                card["partida_id"],
                SEASON,
                card["rodada"],
                club_map[card["clube"]],
                player_map[card["jogador"]],
                pos_map.get(card["posicao"]),
                card["tipo"],
                card["minuto"],
                card["num_camisa"],
            )
        )
    cur.executemany(
        """
        INSERT INTO fato_cartao (
            partida_id, temporada_id, rodada, clube_id, jogador_id,
            posicao_id, tipo, minuto, num_camisa
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Importa cartoes da Serie A 2025 via ESPN.")
    parser.add_argument("--apply", action="store_true", help="grava os cartoes no banco")
    args = parser.parse_args()

    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        scoreboard = fetch_scoreboard()
        match_map = load_match_map(cur)
        cards, errors = extract_cards(scoreboard, match_map)
        write_audit_csv(cards)

        sem_jogador = sum(1 for c in cards if c["jogador"].startswith("Nao informado"))
        sem_posicao = sum(1 for c in cards if not c["posicao"])
        vermelhos = sum(1 for c in cards if c["tipo"] == "Vermelho")
        print(f"jogos_espn={len(scoreboard.get('events', []))}")
        print(f"cartoes_extraidos={len(cards)} amarelos={len(cards) - vermelhos} vermelhos={vermelhos}")
        print(f"sem_jogador={sem_jogador} sem_posicao={sem_posicao}")
        print(f"csv_auditoria={OUTPUT_CSV}")

        if errors:
            print("erros:")
            for error in errors[:20]:
                print(f"- {error}")
            if len(errors) > 20:
                print(f"- ... {len(errors) - 20} erros adicionais")
            return 1

        if args.apply:
            with con:
                import_cards(cur, cards)
            total_db = cur.execute(
                "SELECT COUNT(*) FROM fato_cartao WHERE temporada_id = ?",
                (SEASON,),
            ).fetchone()[0]
            print(f"cartoes_2025_no_banco={total_db}")
        else:
            print("modo=dry-run")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
