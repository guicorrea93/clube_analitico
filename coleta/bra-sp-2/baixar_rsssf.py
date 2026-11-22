"""Baixa as páginas da 2ª divisão paulista da RSSSF Brasil para data/coleta/bra-sp-2/rsssfbrasil/.

sp2camp.htm (campeões, com o link de cada ano que tem página), sp2list.htm (participantes), sp2tops.htm (artilheiros)
e sp{ano}l2.htm, uma por ano. Página já baixada não é baixada de novo.

Uso: python coleta/bra-sp-2/baixar_rsssf.py
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
BASE = "https://rsssfbrasil.com/tablessz/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for arq in ("sp2camp.htm", "sp2list.htm", "sp2tops.htm"):
        print(arq, pegar(BASE + arq, PASTA / arq, espera=2.0) is not None, flush=True)
    camp = (PASTA / "sp2camp.htm").read_bytes().decode("latin-1")
    anos = sorted(set(re.findall(r"sp(\d{4})l2\.htm", camp)))
    for a in anos:
        dados = pegar(BASE + f"sp{a}l2.htm", PASTA / f"sp{a}l2.htm", espera=2.0)
        print(f"sp{a}l2.htm", "sem página" if dados is None else f"{len(dados)} bytes", flush=True)
