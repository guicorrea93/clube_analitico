"""Baixa as páginas da RSSSF da 1ª divisão argelina para data/coleta/alg-1/rsssf/: a lista de campeões (algchamp.html) e as
páginas de temporada que ela liga desde a independência (alg63 = 1962/63 ... alg99, alg00 ... alg09, alg2010 ... alg2026).
As páginas da era colonial (alg1905, alg17, alg18, alg21 a alg59: ligas regionais) ficam de fora, como a era colonial.

Uso: python coleta/alg-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "alg-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesa/"


def depois_da_independencia(pagina: str) -> bool:
    m = re.fullmatch(r"alg(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    return len(n) == 4 and n.startswith("20") or len(n) == 2 and (n.startswith("0") or int(n) >= 63)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "algchamp.html", PASTA / "algchamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(alg\d+\.html)', t, re.I) if depois_da_independencia(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
