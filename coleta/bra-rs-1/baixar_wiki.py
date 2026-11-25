"""Baixa o código do artigo "Campeonato Gaúcho de Futebol" da Wikipédia em português para
data/coleta/bra-rs-1/wikipedia/pt_lista.txt (a lista de campeões ano a ano, segunda fonte do campeão).

Uso: python coleta/bra-rs-1/baixar_wiki.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import wikipedia  # noqa: E402
from edicoes import PASTA_DADOS  # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    pasta = PASTA_DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    t = wikipedia.wikitexto("pt", "Campeonato Gaúcho de Futebol")
    if t:
        (pasta / "pt_lista.txt").write_text(t, encoding="utf-8")
    print("pt_lista.txt", len(t or ""), "caracteres")
