"""Placar diário da ESPN para uma liga (copiado de serie_b/espn.py, com a liga como parâmetro).

A API só responde um dia por vez. De cada jogo: data e hora (UTC), mandante e visitante (nome e id da ESPN),
placar, situação, estádio, cidade, público e os lances (gols e cartões), quando a liga tem.

Uso como biblioteca: baixar(liga, inicio, fim) -> list[dict]
"""
from __future__ import annotations

import json
from datetime import date, timedelta

from baixar import pegar

URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/{liga}/scoreboard?dates={dia}"


def resumir(ev: dict) -> dict:
    c = ev["competitions"][0]
    times = {x["homeAway"]: x for x in c["competitors"]}
    lado = {x["team"]["id"]: x["homeAway"] for x in c["competitors"]}
    lances = []
    for d in c.get("details", []):
        lances.append({
            "tipo": d.get("type", {}).get("text"), "minuto": d.get("clock", {}).get("displayValue"),
            "lado": lado.get(d.get("team", {}).get("id")), "gol": d.get("scoringPlay", False),
            "penalti": d.get("penaltyKick", False), "contra": d.get("ownGoal", False),
            "amarelo": d.get("yellowCard", False), "vermelho": d.get("redCard", False),
            "jogadores": [a.get("displayName") for a in d.get("athletesInvolved", [])],
        })
    return {
        "id": ev["id"], "data_hora": ev["date"], "situacao": ev["status"]["type"]["name"],
        "mandante": times["home"]["team"]["displayName"], "mandante_id": times["home"]["team"]["id"],
        "visitante": times["away"]["team"]["displayName"], "visitante_id": times["away"]["team"]["id"],
        "gols_mandante": times["home"].get("score"), "gols_visitante": times["away"].get("score"),
        "estadio": c.get("venue", {}).get("fullName"), "cidade": c.get("venue", {}).get("address", {}).get("city"),
        "publico": c.get("attendance"), "lances": lances,
    }


def baixar(liga: str, ini: date, fim: date) -> list[dict]:
    jogos, vistos, dia = [], set(), ini
    while dia <= fim:
        bruto = pegar(URL.format(liga=liga, dia=dia.strftime("%Y%m%d")), espera=0.2)
        for ev in json.loads(bruto or b"{}").get("events", []):
            if ev["id"] not in vistos:
                vistos.add(ev["id"]); jogos.append(resumir(ev))
        dia += timedelta(days=1)
    return sorted(jogos, key=lambda j: j["data_hora"])
