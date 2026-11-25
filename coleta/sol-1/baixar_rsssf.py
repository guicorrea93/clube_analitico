"""Baixa as páginas da RSSSF das Ilhas Salomão para data/coleta/sol-1/rsssf/ (lista de campeões, lista de fundação dos clubes
e as páginas por temporada). O nome da página é o ano em que a temporada termina (solom2016 = 2015/16, solom2017 = 2016);
não existe solom2014. Não baixa de novo o que já tem.

Uso: python coleta/sol-1/baixar_rsssf.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "sol-1" / "rsssf"
BASE = "https://www.rsssf.org/tabless/"
PAGINAS = (["solomchamp.html", "solomfound.html"] + [f"solom{a:02d}.html" for a in range(2, 10)]
           + [f"solom{a}.html" for a in range(2010, 2027) if a != 2014] + ["solom2023a.html"])


def main() -> None:
    for p in PAGINAS:
        b = pegar(BASE + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
