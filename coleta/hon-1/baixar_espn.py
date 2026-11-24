"""Baixa o placar diário da ESPN (liga hon.1) de 2004 a 2026 para data/coleta/hon-1/espn/hon1_<ano>.json.

A API responde um dia por pedido; cada dia fica guardado em data/cache/espn-concacaf/hon.1/<AAAAMMDD>.json
(rodar de novo não baixa outra vez). De cada jogo: data e hora (UTC), times, placar, estádio, cidade, público e os
lances (gols e cartões com minuto e jogador). A cobertura da ESPN para Honduras está no relatório.

Uso: python coleta/hon-1/baixar_espn.py [ano ...]
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402
from espn import URL, resumir  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "espn-concacaf" / "hon.1"
PASTA = RAIZ / "data" / "coleta" / "hon-1" / "espn"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or range(2004, 2027):
        jogos, vistos, dia = [], set(), date(ano, 1, 1)
        while dia <= date(ano, 12, 31):
            bruto = pegar(URL.format(liga="hon.1", dia=dia.strftime("%Y%m%d")), CACHE / f"{dia:%Y%m%d}.json", espera=0.25)
            for ev in json.loads(bruto or b"{}").get("events", []):
                if ev.get("id") and ev["id"] not in vistos:   # (há eventos sem id: ficam de fora)
                    vistos.add(ev["id"])
                    jogos.append(resumir(ev))
            dia += timedelta(days=1)
        jogos.sort(key=lambda j: j["data_hora"])
        (PASTA / f"hon1_{ano}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(ano, len(jogos), "jogos", sum(1 for j in jogos if j["lances"]), "com lances", flush=True)
