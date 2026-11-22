"""Baixa as páginas da RSSSF da 1ª divisão peruana para data/coleta/per-1/rsssf/.

A RSSSF tem a lista de campeões (peruchamp.html), a lista de tabelas finais (peruhist.html), os artilheiros
(perutops.html) e uma página por temporada: peru1912 a peru1921 (Liga Peruana), peru30 a peru42, alguns anos de 1968 a
1999, peru00 a peru09 e peru2010 em diante.

Uso: python coleta/per-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "per-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesp/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["peruchamp.html", "peruhist.html"]:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(peru\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["perutops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
