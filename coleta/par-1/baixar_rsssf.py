"""Baixa as páginas da RSSSF da 1ª divisão paraguaia para data/coleta/par-1/rsssf/.

A RSSSF tem a lista de campeões (parachamp.html), a história da liga de 1906 a 1959 com as tabelas finais (parahist.html),
os artilheiros (paratops.html) e uma página por temporada: para43, para45, para55 e para60 a para99, para00 a para09 e
para2010 em diante.

Uso: python coleta/par-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "par-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesp/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["parachamp.html", "parahist.html"]:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(para\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["paratops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
