"""Baixa o código do artigo "Campeonato Catarinense de Futebol Masculino" da Wikipédia em português para
data/coleta/bra-sc-1/wikipedia/pt_lista.txt (a lista de campeões ano a ano, segunda fonte do campeão).

Uso: python coleta/bra-sc-1/baixar_wiki.py
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
    t = wikipedia.wikitexto("pt", "Campeonato Catarinense de Futebol Masculino")
    if t:
        (pasta / "pt_lista.txt").write_text(t, encoding="utf-8")
    print("pt_lista.txt", len(t or ""), "caracteres")
    # a tabela de campeões do artigo é uma predefinição à parte
    t = wikipedia.wikitexto("pt", "Predefinição:Campeões do Campeonato Catarinense de Futebol")
    if t:
        (pasta / "pt_campeoes.txt").write_text(t, encoding="utf-8")
    print("pt_campeoes.txt", len(t or ""), "caracteres")
