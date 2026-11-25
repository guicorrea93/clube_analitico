"""Baixa da Wikipédia em inglês a página da liga saudita ("Saudi Pro League": lista de campeões e vices desde 1957, como o
relatório oficial da federação de 2025) e a dos artilheiros ("List of Saudi Pro League top scorers"), para
data/coleta/ksa-1/wikipedia/: segunda fonte do campeão, do vice e do artilheiro.

Uso: python coleta/ksa-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "ksa-1" / "wikipedia"
PAGINAS = {"en_spl": "Saudi_Pro_League", "en_artilheiros": "List_of_Saudi_Pro_League_top_scorers"}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome, titulo in PAGINAS.items():
        b = pegar(f"https://en.wikipedia.org/w/index.php?title={titulo}&action=raw", PASTA / f"{nome}.txt", espera=1.0)
        print(nome, "404" if b is None else f"{len(b)} bytes", flush=True)
