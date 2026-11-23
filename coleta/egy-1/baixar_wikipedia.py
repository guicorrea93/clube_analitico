"""Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Egyptian Premier League", lista de campeões) e o de
cada temporada ("1974–75 Egyptian Premier League"), para data/coleta/egy-1/wikipedia/. Os artigos de temporada trazem a
tabela final (a maioria tirada do site do Dr. Tarek Said, um dos autores das páginas da RSSSF): é a terceira fonte quando a
tabela da RSSSF e os jogos não fecham.

Uso: python coleta/egy-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
from edicoes import EDICOES, PASTA_DADOS  # noqa: E402
from wikipedia import wikitexto  # noqa: E402

PASTA = PASTA_DADOS / "wikipedia"


def arquivo(temporada: str) -> Path:
    return PASTA / f"en_{temporada.replace('/', '-')}.txt"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    if not (PASTA / "en_liga.txt").exists():
        (PASTA / "en_liga.txt").write_text(wikitexto("en", "Egyptian Premier League") or "", encoding="utf-8")
    for e in EDICOES:
        arq = arquivo(e.temporada)
        if arq.exists():
            continue
        titulo = f"{e.ano_inicio}–{str(e.ano_fim)[-2:]} Egyptian Premier League"
        w = wikitexto("en", titulo)
        arq.write_text(w or "", encoding="utf-8")
        print(e.temporada, "ok" if w else "não existe", flush=True)
