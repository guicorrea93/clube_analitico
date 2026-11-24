"""Baixa as páginas da RSSSF da 1ª divisão mexicana para data/coleta/mex-1/rsssf/: a lista de campeões (mexchamp.html), as
páginas que ela liga (temporadas, histórico) e as de nome conhecido que ela não liga (artilheiros).

Uso: python coleta/mex-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "mex-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesm/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "mexchamp.html", PASTA / "mexchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p.split("#")[0] for p in re.findall(r'href="?(mex[a-z0-9-]*\.html)', t, re.I)} | {"mextops.html"}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
