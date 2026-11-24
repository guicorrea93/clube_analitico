"""Baixa as páginas da RSSSF da 1ª divisão dos EUA para data/coleta/usa-1/rsssf/: a lista de campeões da "Division I"
(tablesu/usachamp.html), a ASL I (usadave/asli.html), a NASL (usadave/nasl.html, com 1967) e as páginas por temporada da
MLS (tablesu/usaAA.html até 1999, usaAAAA.html depois), mais as que a lista liga.

Uso: python coleta/usa-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "usa-1" / "rsssf"
BASE = "https://www.rsssf.org/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "tablesu/usachamp.html", PASTA / "usachamp.html") or b"").decode("cp1252", "ignore")
    paginas = {"usadave/asli.html", "usadave/nasl.html", "usadave/usa67.html"}
    paginas |= {f"tablesu/usa{a % 100:02d}.html" if a < 2000 else f"tablesu/usa{a}.html" for a in range(1996, 2026)}
    paginas |= {("tablesu/" + p) for p in re.findall(r'href="?(usa[a-z0-9-]*\.html)', t, re.I)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / Path(p).name)
        print(p, "ok" if ok else "404", flush=True)
