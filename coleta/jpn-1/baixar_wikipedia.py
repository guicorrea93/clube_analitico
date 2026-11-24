"""Baixa da Wikipédia em inglês as listas de campeões japoneses ("List of Japanese football champions", com a JSL e a
J1, e "J1 League") para data/coleta/jpn-1/wikipedia/, segunda fonte do campeão e do vice.

Uso: python coleta/jpn-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "jpn-1" / "wikipedia"
PAGINAS = {"en_campeoes": "List_of_Japanese_football_champions", "en_j1": "J1_League",
           "en_jsl": "Japan_Soccer_League"}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome, titulo in PAGINAS.items():
        b = pegar(f"https://en.wikipedia.org/w/index.php?title={titulo}&action=raw", PASTA / f"{nome}.txt", espera=1.0)
        print(nome, "404" if b is None else f"{len(b)} bytes", flush=True)
