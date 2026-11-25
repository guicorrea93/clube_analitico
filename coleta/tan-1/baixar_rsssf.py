"""Baixa as páginas da RSSSF da 1ª divisão tanzaniana para data/coleta/tan-1/rsssf/: a lista de campeões (tanzchamp.html)
e as páginas de temporada que ela liga desde a liga nacional (tanz65, tanz82 ... tanz99, tanz00 ... tanz09, tanz2010 ...
tanz2026). As da liga de Dar es Salaam (tanz29, tanz30, tanz32) e a temporada em andamento (tanz2027) ficam de fora.

Uso: python coleta/tan-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "tan-1" / "rsssf"
BASE = "https://www.rsssf.org/tablest/"
ULTIMA = 2026   # última temporada terminada (2025/26)


def no_escopo(pagina: str) -> bool:
    m = re.fullmatch(r"tanz(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    if len(n) == 4:
        return n.startswith("20") and int(n) <= ULTIMA
    return len(n) == 2 and (n.startswith("0") or int(n) >= 65)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "tanzchamp.html", PASTA / "tanzchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(tanz\d+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
