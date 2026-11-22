"""Baixa as páginas da RSSSF da 1ª divisão venezuelana para data/coleta/ven-1/rsssf/: a lista de campeões (venezchamp.html), as
páginas que ela liga (temporadas, tabelas finais, artilheiros) e as de nome conhecido que ela não liga.

Uso: python coleta/ven-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "ven-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesv/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "venezchamp.html", PASTA / "venezchamp.html") or b"").decode("cp1252", "ignore")
    paginas = set(re.findall(r'href="?(ven[a-z]*\d*\.html)', t, re.I)) | {"veneztops.html"}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
