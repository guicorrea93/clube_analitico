"""Baixa as páginas do Campeonato Mineiro da RSSSF Brasil para data/coleta/bra-mg-1/rsssfbrasil/.

mgcamp.htm (campeões, com o link de cada ano), mgtops.htm (artilheiros, se houver) e mg{ano}.htm, uma por ano
(mg1926l.htm, mg1932l.htm e mg1932a.htm com a letra da liga). Página já baixada não é baixada de novo.

Uso: python coleta/bra-mg-1/baixar_rsssf.py
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
    for arq in ("mgcamp.htm", "mgtops.htm"):
        print(arq, pegar(BASE + arq, PASTA / arq, espera=2.0) is not None, flush=True)
    camp = (PASTA / "mgcamp.htm").read_bytes().decode("latin-1")
    paginas = sorted(set(re.findall(r'href="(mg\d{4}[a-z]?\.htm)"', camp)))
    for arq in paginas:
        dados = pegar(BASE + arq, PASTA / arq, espera=2.0)
        print(arq, "sem página" if dados is None else f"{len(dados)} bytes", flush=True)
