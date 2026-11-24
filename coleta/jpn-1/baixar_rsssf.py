"""Baixa as páginas da RSSSF da 1ª divisão japonesa para data/coleta/jpn-1/rsssf/: a lista de campeões (japchamp.html),
as páginas de temporada que ela liga (jap65.html a jap04.html, jpn05.html a jpn2025.html) e as de nome conhecido que ela
não liga (tabelas finais e artilheiros).

Uso: python coleta/jpn-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "jpn-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesj/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "japchamp.html", PASTA / "japchamp.html") or b"").decode("cp1252", "ignore")
    paginas = set(re.findall(r'href="?((?:jap|jpn)[a-z]*\d*\.html)', t, re.I)) | {"jap85.html", "japtops.html", "japhist.html"}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
