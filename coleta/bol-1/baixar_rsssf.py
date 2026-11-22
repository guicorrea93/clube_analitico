"""Baixa as páginas da RSSSF da 1ª divisão boliviana para data/coleta/bol-1/rsssf/.

A RSSSF tem a lista de campeões (bolchamp.html), a lista de tabelas finais de 1950 a 1990 (bolhist.html), os artilheiros
(boltops.html) e uma página por temporada (bol77, bol90 a bol99, bol00 a bol09, bol2010 em diante), ligadas a partir da
lista de campeões.

Uso: python coleta/bol-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "bol-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesb/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "bolchamp.html", PASTA / "bolchamp.html") or b"").decode("cp1252", "ignore")
    paginas = set(re.findall(r'href="?(bol[a-z]*\d*\.html)', t, re.I)) | {"bolhist.html", "boltops.html"}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
