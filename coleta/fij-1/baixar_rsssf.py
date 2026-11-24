"""Baixa as páginas da RSSSF de Fiji para data/coleta/fij-1/rsssf/ (lista de campeões, lista de finais da copa e
as páginas por temporada que a lista liga). Não baixa de novo o que já tem.

Uso: python coleta/fij-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "fij-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesf/"


def main() -> None:
    lista = pegar(BASE + "fijichamp.html", DEST / "fijichamp.html", espera=2.0) or b""
    paginas = sorted(set(re.findall(r'href="(fiji[^"#/]+\.html)"', lista.decode("latin-1"))) - {"fijichamp.html"})
    for p in ["fijicuphist.html"] + paginas:
        b = pegar(BASE + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
