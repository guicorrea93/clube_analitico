"""Edições da Copa do Brasil: anos e nomes oficiais.

A Copa do Brasil existe desde 1989 (a Taça Brasil, de 1959 a 1968, já está no banco como Série A).
Lista de edições e campeões: RSSSF Brasil (cbrcamp.htm) e Wikipédia em português ("Copa do Brasil de Futebol"):
37 edições, de 1989 a 2025.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-copa-do-brasil"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

ANOS = list(range(1989, 2026))

NOME_OFICIAL: dict[int, str] = {}
NOME_PADRAO = "Copa do Brasil"
