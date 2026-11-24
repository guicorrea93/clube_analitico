"""Baixa o wikitexto da Wikipédia em inglês sobre a liga do Taiti para data/coleta/tah-1/wikipedia/: a página da liga
(lista de campeões) e as páginas de temporada que existirem (2005/06 a 2026/27).

Uso: python coleta/tah-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from wikipedia import wikitexto  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "tah-1" / "wikipedia"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    DEST.mkdir(parents=True, exist_ok=True)
    titulos = {"liga": ("en", "Tahiti Ligue 1"), "liga-fr": ("fr", "Championnat de Tahiti de football")}
    for a in range(2005, 2027):
        titulos[f"{a}-{(a + 1) % 100:02d}"] = ("en", f"{a}–{(a + 1) % 100:02d} Tahiti Ligue 1")
    for chave, (lingua, titulo) in titulos.items():
        arq = DEST / f"{chave}.wiki"
        if arq.exists():
            continue
        txt = wikitexto(lingua, titulo)
        print(chave, titulo, "-" if txt is None else len(txt), flush=True)
        if txt:
            arq.write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main()
