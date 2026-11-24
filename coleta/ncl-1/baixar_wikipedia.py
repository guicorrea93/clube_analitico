"""Baixa o wikitexto da Wikipédia sobre a liga da Nova Caledônia para data/coleta/ncl-1/wikipedia/ (página da liga em inglês e
em francês, com a lista de campeões). Segunda fonte do campeão.

Uso: python coleta/ncl-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from wikipedia import wikitexto  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "ncl-1" / "wikipedia"
TITULOS = {"liga": ("en", "New Caledonia Super Ligue"), "liga-fr": ("fr", "Championnat de Nouvelle-Calédonie de football")}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    DEST.mkdir(parents=True, exist_ok=True)
    for chave, (lingua, titulo) in TITULOS.items():
        arq = DEST / f"{chave}.wiki"
        if not arq.exists():
            txt = wikitexto(lingua, titulo)
            print(chave, titulo, "-" if txt is None else len(txt), flush=True)
            if txt:
                arq.write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main()
