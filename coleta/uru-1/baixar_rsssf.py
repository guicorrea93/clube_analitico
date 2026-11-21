"""Baixa as páginas da RSSSF da 1ª divisão uruguaia para data/coleta/uru-1/rsssf/.

A RSSSF tem as tabelas finais de 1900 a 2000 numa página só (uruhist.html), a lista de campeões (uruchamp.html), os
artilheiros (urutops.html) e uma página por temporada com os jogos: uru32 a uru59 (1932-1959), uru65, uru69, uru83 a
uru99 (1983-1999), uru00 a uru09 (2000-2009) e uru2010 em diante. As outras temporadas não têm página de jogos.

Uso: python coleta/uru-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "uru-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesu/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temporadas: set[str] = set()
    for p in ["uruchamp.html", "uruhist.html"]:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(uru\d{2,4}[a-z]?\.html)', t, re.I))
    for p in ["urutops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
