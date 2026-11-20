"""Edições da Série C: anos, nomes oficiais e campeões (conferidos em duas fontes).

Lista de edições: RSSSF Brasil (br3camp.htm) e Wikipédia em português ("Campeonato Brasileiro de
Futebol - Série C"). As duas trazem as mesmas 35 edições oficiais. Ficam de fora, como nas duas
fontes: 1987 (módulos Azul e Branco da Copa União; a CBF disse que nenhum módulo seria a 3ª divisão)
e 2000 (Módulo Verde e Branco da Copa João Havelange, equivalente à 3ª divisão, título não oficial).
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-serie-c"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

ANOS = [1981, 1988, 1990, 1992] + list(range(1994, 2000)) + list(range(2001, 2026))

# nome oficial de cada edição (Wikipédia pt / CBF)
NOME_OFICIAL = {1981: "Taça de Bronze"}
NOME_PADRAO = "Campeonato Brasileiro Série C"

# campeões pela RSSSF (br3camp.htm, até 2022; 2023 a 2025 pela página da edição), nome de exibição do pacote
CAMPEOES: dict[int, str] = {}
