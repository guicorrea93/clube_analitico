"""Baixa as páginas do Campeonato Carioca da RSSSF Brasil para data/coleta/bra-rj-1/rsssfbrasil/.

rjcamp.htm (campeões, com o link de cada ano), rjtops.htm (artilheiros), rjhist.htm (história) e rj{ano}.htm, uma por
ano (rj1979s.htm: o campeonato especial de 1979). Página já baixada não é baixada de novo.

Uso: python coleta/bra-rj-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from edicoes import PASTA_DADOS  # noqa: E402

PASTA = PASTA_DADOS / "rsssfbrasil"
BASE = "https://rsssfbrasil.com/tablesr/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for arq in ("rjcamp.htm", "rjtops.htm", "rjhist.htm"):
        print(arq, pegar(BASE + arq, PASTA / arq, espera=2.0) is not None, flush=True)
    camp = (PASTA / "rjcamp.htm").read_bytes().decode("latin-1")
    paginas = sorted(set(re.findall(r'href="(rj\d{4}s?\.htm)"', camp)))   # rj1978flu.htm é do campeonato do interior
    for arq in paginas:
        dados = pegar(BASE + arq, PASTA / arq, espera=2.0)
        print(arq, "sem página" if dados is None else f"{len(dados)} bytes", flush=True)
