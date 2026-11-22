"""Baixa da Wikipédia em inglês a página da liga ("LigaPro Serie A", com a lista de campeões) para
data/coleta/ecu-1/wikipedia/en_campeoes.txt (wikitexto), segunda fonte do campeão e do vice.

Uso: python coleta/ecu-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "ecu-1" / "wikipedia"
URL_EN = "https://en.wikipedia.org/w/index.php?title=LigaPro_Serie_A&action=raw"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    b = pegar(URL_EN, PASTA / "en_campeoes.txt", espera=1.0)
    print("en_campeoes", "404" if b is None else f"{len(b)} bytes", flush=True)
