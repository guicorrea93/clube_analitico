"""Baixa os jogos da Série B na ESPN (2010 em diante) para data/serie_b/espn/serie_b_{ano}.json.

A API do placar da ESPN (liga "bra.2") só responde um dia por vez, então o script
percorre a janela de cada temporada dia a dia. De cada jogo guarda: data e hora,
mandante e visitante (nome e id da ESPN), placar, situação, estádio, público e os
lances (gols e cartões com minuto, jogador e clube).

Uso: python serie_b/espn.py [ano ...]     (sem ano: 2010 a 2025; ano já baixado é pulado, --de-novo baixa outra vez)
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "data" / "serie_b" / "espn"
URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/bra.2/scoreboard?dates={dia}"
UA = {"User-Agent": "Mozilla/5.0 (clube-analitico; projeto pessoal)"}
# janela de cada temporada (2020 foi de agosto de 2020 a janeiro de 2021, pela pandemia)
JANELA = {2020: (date(2020, 7, 15), date(2021, 2, 28))}


def pegar(dia: date) -> dict:
    for tentativa in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(URL.format(dia=dia.strftime("%Y%m%d")), headers=UA), timeout=40) as r:
                return json.loads(r.read())
        except (urllib.error.URLError, TimeoutError) as e:
            if tentativa == 4:
                raise
            time.sleep(5 * (tentativa + 1))
    return {}


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


def baixar(ano: int) -> list[dict]:
    ini, fim = JANELA.get(ano, (date(ano, 3, 15), date(ano, 12, 31)))
    jogos, vistos, dia = [], set(), ini
    while dia <= fim:
        for ev in pegar(dia).get("events", []):
            if ev["id"] not in vistos:
                vistos.add(ev["id"]); jogos.append(resumir(ev))
        dia += timedelta(days=1)
        time.sleep(0.15)
    return sorted(jogos, key=lambda j: j["data_hora"])


if __name__ == "__main__":
    PASTA.mkdir(parents=True, exist_ok=True)
    de_novo = "--de-novo" in sys.argv
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(range(2010, 2026))
    for ano in anos:
        destino = PASTA / f"serie_b_{ano}.json"
        if destino.exists() and not de_novo:
            continue
        jogos = baixar(ano)
        destino.write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano}: {len(jogos)} jogos, {sum(j['situacao'] == 'STATUS_FULL_TIME' for j in jogos)} encerrados", flush=True)
