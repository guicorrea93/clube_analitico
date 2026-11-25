"""Baixa o placar diário da ESPN (liga ksa.1) para data/coleta/ksa-1/espn/ksa1_<fim>.json (<fim> = ano em que a temporada
termina). A ESPN só tem a liga saudita de 2022/23 em diante.

A API responde um dia por pedido; cada dia fica guardado em data/cache/espn-asia/ksa.1/<AAAAMMDD>.json. De cada jogo: data
e hora (UTC), times, placar, estádio, público e os lances (gols e cartões com minuto e jogador).

Uso: python coleta/ksa-1/baixar_espn.py [fim ...]
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402
from espn import URL, resumir  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "espn-asia" / "ksa.1"
PASTA = RAIZ / "data" / "coleta" / "ksa-1" / "espn"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for fim in [int(a) for a in sys.argv[1:]] or range(2023, 2027):
        jogos, vistos, dia = [], set(), date(fim - 1, 7, 1)
        while dia <= date(fim, 6, 30):
            bruto = pegar(URL.format(liga="ksa.1", dia=dia.strftime("%Y%m%d")), CACHE / f"{dia:%Y%m%d}.json", espera=0.25)
            for ev in json.loads(bruto or b"{}").get("events", []):
                if ev.get("id") and ev["id"] not in vistos:
                    vistos.add(ev["id"])
                    jogos.append(resumir(ev))
            dia += timedelta(days=1)
        jogos.sort(key=lambda j: j["data_hora"])
        (PASTA / f"ksa1_{fim}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(fim, len(jogos), "jogos", sum(1 for j in jogos if j["lances"]), "com lances", flush=True)
