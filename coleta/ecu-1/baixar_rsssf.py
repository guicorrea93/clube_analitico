"""Baixa as páginas da RSSSF da 1ª divisão equatoriana para data/coleta/ecu-1/rsssf/.

A RSSSF tem a lista de campeões (ecuachamp.html), a lista de tabelas finais (ecuahist.html), os artilheiros
(ecuatops.html) e uma página por temporada, ligadas a partir das duas primeiras.

Uso: python coleta/ecu-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "ecu-1" / "rsssf"
BASE = "https://www.rsssf.org/tablese/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["ecuachamp.html", "ecuahist.html"]:
        b = pegar(BASE + p, PASTA / p)
        print(p, "ok" if b else "404", flush=True)
        t = (b or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(ecua?d?o?r?\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["ecuatops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
