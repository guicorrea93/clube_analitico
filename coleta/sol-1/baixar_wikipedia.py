"""Baixa o wikitexto da página "Solomon Islands S-League" da Wikipédia em inglês (lista de campeões) para
data/coleta/sol-1/wikipedia/liga.wiki. Segunda fonte do campeão.

Uso: python coleta/sol-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from wikipedia import wikitexto  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "sol-1" / "wikipedia"


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    arq = DEST / "liga.wiki"
    if not arq.exists():
        txt = wikitexto("en", "Solomon Islands S-League")
        if txt:
            arq.write_text(txt, encoding="utf-8")
    print(arq, arq.exists())


if __name__ == "__main__":
    main()
