"""Baixa as páginas da RSSSF da 1ª divisão nigeriana para data/coleta/nga-1/rsssf/: a lista de campeões (nigchamp.html) e
as páginas de temporada que ela liga desde a liga nacional (nig72 = 1970 a 1979; nig83 ... nig99, nig00 ... nig09,
nig2010 ... nig2026). A nig31 (Liga de Lagos, 1931 a 1945) fica de fora, como o escopo.

Uso: python coleta/nga-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "nga-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesn/"


def no_escopo(pagina: str) -> bool:
    m = re.fullmatch(r"nig(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    return len(n) == 4 and n.startswith("20") or len(n) == 2 and (n.startswith("0") or int(n) >= 72)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "nigchamp.html", PASTA / "nigchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(nig\d+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
