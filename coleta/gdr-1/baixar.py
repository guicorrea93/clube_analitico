"""Baixa as fontes do campeonato da Alemanha Oriental (gdr-1), 1948 a 1990/91.

Fontes (cada uma numa pasta de data/coleta/gdr-1/):
  rsssf  RSSSF: página de cada temporada (tablesd/ddr50.html ...), com rodada, data e placar de cada jogo; tabelas finais
         (ddrhist.html), lista de campeões (ddrchamp.html) e de artilheiros (ddrtops.html).
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final e matriz de resultados).

Uso: python coleta/gdr-1/baixar.py rsssf wiki
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import DADOS, TEMPORADAS, rsssf_pagina, wiki_titulo  # noqa: E402


def rsssf() -> None:
    for nome in [rsssf_pagina(a) for a in TEMPORADAS] + ["ddrhist.html", "ddrchamp.html", "ddrtops.html"]:
        d = pegar(f"https://www.rsssf.org/tablesd/{nome}", DADOS / "rsssf" / nome, espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in [wiki_titulo(a) for a in TEMPORADAS] + ["List of East German football champions"]:
        arq = pasta / f"{t}.wiki"
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt or '')}", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:
        globals()[nome]()
