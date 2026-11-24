"""Baixa as páginas da RSSSF da 1ª divisão da Guatemala para data/coleta/gua-1/rsssf/: a lista de campeões (guatchamp.html), as
páginas que ela liga e as temporadas de nome conhecido (guatAA.html, guatAAAA.html).

Uso: python coleta/gua-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "gua-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesg/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "guatchamp.html", PASTA / "guatchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p.split("#")[0] for p in re.findall(r'href="?(guat?[a-z0-9-]*\.html)', t, re.I) if "wom" not in p}
    paginas |= {f"guat{a % 100:02d}.html" if a < 2010 else f"guat{a}.html" for a in range(1943, 2027)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
