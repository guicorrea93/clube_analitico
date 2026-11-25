"""Baixa as páginas da RSSSF da 1ª divisão camaronesa para data/coleta/cmr-1/rsssf/: a lista de campeões (kamchamp.html) e
as páginas de temporada que ela liga desde a independência (kam61 = o primeiro campeonato, kam68 ... kam99, kam00 ...
kam09, kam2010 ... kam2026). As da era colonial (kam50, kam51, kam56: campeonato territorial) ficam de fora.

Uso: python coleta/cmr-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "cmr-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesk/"


def no_escopo(pagina: str) -> bool:
    m = re.fullmatch(r"kam(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    return len(n) == 4 and n.startswith("20") or len(n) == 2 and (n.startswith("0") or int(n) >= 61)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "kamchamp.html", PASTA / "kamchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(kam\d+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
