"""Baixa as páginas da RSSSF da 1ª divisão argentina para data/coleta/arg-1/rsssf/.

A RSSSF tem um índice por década (arghist-*.html), com as tabelas finais, e uma página por temporada
(arg{aa}.html ou arg{aaaa}.html), com resultados. Baixa os índices, a lista de campeões (argchamp.html),
os artilheiros (argtops.html) e todas as páginas de temporada ligadas nos índices.

Uso: python coleta/arg-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "arg-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesa/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    idx = (pegar(BASE + "arghist.html", PASTA / "arghist.html") or b"").decode("cp1252", "ignore")
    paginas = sorted(set(re.findall(r'href="?(arghist-[^"#> ]+\.html)', idx, re.I)))
    temporadas: set[str] = set()
    for p in paginas:
        t = (pegar(BASE + p, PASTA / p) or b"").decode("cp1252", "ignore")
        temporadas |= set(re.findall(r'href="?(arg\d{2,4}[a-z]?\.html)', t, re.I))
    # 1901, 1902, 1921, 2009/10, 2025 e as copas de 1936 (Honor e Oro) não estão ligadas nos índices das temporadas
    temporadas |= {"arg1901.html", "arg1902.html", "arg21.html", "arg2010.html", "arg2025.html", "arg-hon36.html", "arg-oro36.html"}
    for p in ["argchamp.html", "argtops.html", *sorted(temporadas)]:
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
