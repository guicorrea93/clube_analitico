"""Baixa as páginas da RSSSF de Papua-Nova Guiné para data/coleta/png-1/rsssf/ (lista de campeões, lista de finais da copa e
as páginas por temporada que a lista liga). Não baixa de novo o que já tem.

Uso: python coleta/png-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from baixar import pegar  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "png-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesp/"


def main() -> None:
    lista = pegar(BASE + "pngchamp.html", DEST / "pngchamp.html", espera=2.0) or b""
    paginas = sorted(set(re.findall(r'href="(png[^"#/]+\.html)"', lista.decode("latin-1"))) - {"pngchamp.html"})
    # páginas da National Soccer League que a lista de campeões não liga (png2012a = NSL 2013; png2013 não tem a NSL)
    nsl = ["png08.html", "png09.html", "png2011.html", "png2012.html", "png2012a.html"] + [f"png{a}.html" for a in range(2014, 2027)]
    for p in ["pngcuphist.html"] + paginas + [x for x in nsl if x not in paginas]:
        b = pegar(BASE + p, DEST / p, espera=2.0)
        print(p, "-" if b is None else len(b), flush=True)


if __name__ == "__main__":
    main()
