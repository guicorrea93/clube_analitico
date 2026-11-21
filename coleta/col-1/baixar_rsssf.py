"""Baixa as páginas da RSSSF da 1ª divisão colombiana para data/coleta/col-1/rsssf/.

A RSSSF tem a lista de campeões (colchamp.html) e uma página por temporada com os jogos: col48 a col99, col00 a col09 e
col2010 em diante (col1214 e col1819 são páginas extras de 2012-2014 e 2018-2019).

Uso: python coleta/col-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "col-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesc/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["colchamp.html"]:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(col\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["coltops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
