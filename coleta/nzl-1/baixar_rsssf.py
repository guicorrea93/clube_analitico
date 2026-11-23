"""Baixa as páginas da RSSSF da Nova Zelândia para data/coleta/nzl-1/rsssf/ (lista de campeões, histórico e uma página
por ano da liga nacional, 1970-2025). Não baixa de novo o que já tem.

Uso: python coleta/nzl-1/baixar_rsssf.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
DEST = RAIZ / "data" / "coleta" / "nzl-1" / "rsssf"
PAGINAS = (["nzchamp.html", "nzhist.html", "nzcuphist.html"]
           + [f"nz{a % 100:02d}.html" for a in range(1970, 2010)]
           + [f"nz{a}.html" for a in range(2010, 2026)] + ["nz2021a.html"])


def main() -> None:
    for p in PAGINAS:
        b = pegar("https://www.rsssf.org/tablesn/" + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
