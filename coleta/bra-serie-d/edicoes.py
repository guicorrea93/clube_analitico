"""Edições da Série D: anos, nomes oficiais e campeões (conferidos em duas fontes).

A Série D existe desde 2009. Lista de edições: RSSSF Brasil (br4camp.htm, até 2023) e Wikipédia em português
("Campeonato Brasileiro de Futebol - Série D"): 17 edições, de 2009 a 2025.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-serie-d"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

ANOS = list(range(2009, 2027))

NOME_OFICIAL: dict[int, str] = {}
NOME_PADRAO = "Campeonato Brasileiro Série D"
