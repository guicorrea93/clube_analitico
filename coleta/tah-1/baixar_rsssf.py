"""Baixa as páginas da RSSSF do Taiti para data/coleta/tah-1/rsssf/ (lista de campeões e as páginas por temporada que ela
liga: 1968-1971, 1985 e 1999 em diante). Não baixa de novo o que já tem.

Uso: python coleta/tah-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "tah-1" / "rsssf"
BASE = "https://www.rsssf.org/tablest/"


def main() -> None:
    lista = pegar(BASE + "tahitichamp.html", DEST / "tahitichamp.html", espera=2.0) or b""
    paginas = sorted(set(re.findall(r'href="(tahiti[^"#]+\.html)"', lista.decode("latin-1"))))
    for p in ["tahiticuphist.html"] + paginas:
        b = pegar(BASE + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
