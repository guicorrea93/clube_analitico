"""Baixa da Wikipédia em inglês a lista de campeões mexicanos ("List of Mexican football champions", era amadora e
profissional, com vice) para data/coleta/mex-1/wikipedia/en_campeoes.txt, segunda fonte do campeão e do vice.

Uso: python coleta/mex-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "mex-1" / "wikipedia"
URL_EN = "https://en.wikipedia.org/w/index.php?title=List_of_Mexican_football_champions&action=raw"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    b = pegar(URL_EN, PASTA / "en_campeoes.txt", espera=1.0)
    print("en_campeoes", "404" if b is None else f"{len(b)} bytes", flush=True)
