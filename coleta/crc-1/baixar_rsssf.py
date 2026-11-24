"""Baixa as páginas da RSSSF da 1ª divisão da Costa Rica para data/coleta/crc-1/rsssf/: a lista de campeões (coschamp.html),
as páginas que ela liga (temporadas cosAA.html e cosAAAA.html, tabela histórica) e as temporadas de nome conhecido.

Uso: python coleta/crc-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "crc-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesc/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "coschamp.html", PASTA / "coschamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(cos[a-z0-9-]*\.html)', t, re.I) if "wom" not in p and not p.startswith("cos2champ")}
    paginas |= {f"cos{a % 100:02d}.html" if a < 2010 else f"cos{a}.html" for a in range(1921, 2027)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
