"""Baixa as páginas da RSSSF da 1ª divisão de Honduras para data/coleta/hon-1/rsssf/: a lista de campeões (hondchamp.html),
as tabelas finais de 1965/66 a 1994/95 (hondhist.html) e as páginas que elas ligam (temporadas hondAA.html / hondAAAA.html).

Uso: python coleta/hon-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "hon-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesh/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    paginas = set()
    for ind in ("hondchamp.html", "hondhist.html"):
        t = (pegar(BASE + ind, PASTA / ind) or b"").decode("cp1252", "ignore")
        paginas |= {p.split("#")[0] for p in re.findall(r'href="?(hond?[a-z0-9-]*\.html)', t, re.I) if "wom" not in p}
    paginas |= {f"hond{a % 100:02d}.html" if a < 2010 else f"hond{a}.html" for a in range(1966, 2027)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
