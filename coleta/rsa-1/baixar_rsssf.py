"""Baixa as páginas da RSSSF da 1ª divisão sul-africana para data/coleta/rsa-1/rsssf/: a lista de campeões (zafchamp.html)
e as páginas de temporada que ela liga desde 1971 (zaf71 ... zaf96 no ano civil; zaf97 = 1996/97 ... zaf99, zaf00 ...
zaf09, zaf2010 ... zaf2026). As de antes de 1971 (NFL dos brancos, ligas amadoras) ficam de fora, como o escopo.

Uso: python coleta/rsa-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "rsa-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesz/"


def no_escopo(pagina: str) -> bool:
    m = re.fullmatch(r"zaf(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    return len(n) == 4 and n.startswith("20") or len(n) == 2 and (n.startswith("0") or int(n) >= 71)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "zafchamp.html", PASTA / "zafchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(zaf\d+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
