"""Baixa as páginas da RSSSF da Nova Caledônia para data/coleta/ncl-1/rsssf/ (lista de campeões, lista de finais da copa e
as páginas por temporada que a lista liga). Não baixa de novo o que já tem.

Uso: python coleta/ncl-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "ncl-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesn/"


def main() -> None:
    lista = pegar(BASE + "newcalchamp.html", DEST / "newcalchamp.html", espera=2.0) or b""
    paginas = sorted(set(re.findall(r'href="(newcal[^"#/]+\.html)"', lista.decode("latin-1"))) - {"newcalchamp.html"})
    for p in ["newcalcuphist.html"] + paginas:
        b = pegar(BASE + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
