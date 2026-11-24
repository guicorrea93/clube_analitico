"""Baixa da Wikipédia em inglês a lista de campeões sul-coreanos ("List of South Korean football champions": campeão e
vice de cada ano) e a lista dos artilheiros da K League ("K League Top Scorer Award"), para
data/coleta/kor-1/wikipedia/: segunda fonte do campeão, do vice e do artilheiro.

Uso: python coleta/kor-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "kor-1" / "wikipedia"
PAGINAS = {"en_campeoes": "List_of_South_Korean_football_champions", "en_artilheiros": "K_League_Top_Scorer_Award"}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome, titulo in PAGINAS.items():
        b = pegar(f"https://en.wikipedia.org/w/index.php?title={titulo}&action=raw", PASTA / f"{nome}.txt", espera=1.0)
        print(nome, "404" if b is None else f"{len(b)} bytes", flush=True)
