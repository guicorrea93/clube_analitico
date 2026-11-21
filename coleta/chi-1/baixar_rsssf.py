"""Baixa as páginas da RSSSF da 1ª divisão chilena para data/coleta/chi-1/rsssf/.

A RSSSF tem a lista de campeões (chilechamp.html), as tabelas finais de 1933 a 1996 (chilehist.html) e uma página por
temporada com os jogos: chile33 a chile99 (sem 1984-1986, que só têm as copas chilecup84-86), chile00 a chile09 e
chile2010 em diante (chile2017a é a Transición 2017).

Uso: python coleta/chi-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "chi-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesc/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["chilechamp.html", "chilehist.html"]:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(chile(?:cup)?\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["chiletops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
