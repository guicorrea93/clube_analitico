"""Baixa as páginas do Campeonato Paranaense da RSSSF Brasil para data/coleta/bra-pr-1/rsssfbrasil/.

prcamp.htm (campeões, com o link de cada ano), prtops.htm (artilheiros, se houver) e pr{ano}.htm, uma por ano
(1919 a 2025). Página já baixada não é baixada de novo.

Uso: python coleta/bra-pr-1/baixar_rsssf.py
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
BASE = "https://rsssfbrasil.com/tablesfq/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for arq in ("prcamp.htm", "prtops.htm"):
        print(arq, pegar(BASE + arq, PASTA / arq, espera=2.0) is not None, flush=True)
    camp = (PASTA / "prcamp.htm").read_bytes().decode("latin-1")
    paginas = sorted(set(re.findall(r'href="(pr\d{4}[a-z]*\.htm)"', camp)))
    for arq in paginas:
        dados = pegar(BASE + arq, PASTA / arq, espera=2.0)
        print(arq, "sem página" if dados is None else f"{len(dados)} bytes", flush=True)
