"""Baixa as páginas da RSSSF da 1ª divisão ganesa para data/coleta/gha-1/rsssf/: a lista de campeões (ghachamp.html) e
as páginas de temporada que ela liga desde 1958 (gha58 ... gha99, gha00 ... gha09, gha2010 ... gha2026) e a lista de
tabelas finais de 1959 a 1987 (ghahist.html). As de 1953 e 1956 (Liga de Accra, campeonato não oficial) ficam de fora.

Uso: python coleta/gha-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "gha-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesg/"


def no_escopo(pagina: str) -> bool:
    if pagina == "ghahist.html":
        return True
    m = re.fullmatch(r"gha(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    return len(n) == 4 and n.startswith("20") or len(n) == 2 and (n.startswith("0") or int(n) >= 58)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "ghachamp.html", PASTA / "ghachamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(gha\w+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
