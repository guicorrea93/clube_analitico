"""Edições do Campeonato Paulista Série A2 (2ª divisão, `bra-sp-2`): temporadas, anos e nomes oficiais.

O ogol tem uma edição da 2ª divisão para cada ano de 1916 a 2026 (competição "campeonato-paulista-a2", código 562).
A RSSSF Brasil (sp2camp.htm) separa a fase amadora (1906-1946, só a lista de campeões) da profissional (1947 em diante,
com uma página de jogos por ano em quase todos os anos: sp{ano}l2.htm).
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-sp-2"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1916, 2027)]
LIGAS: dict[int, tuple] = {}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


# nome oficial por época (lista de campeões da 2ª divisão na RSSSF Brasil, sp2camp.htm)
_NOMES = [(1916, 1916, "Seção B (LPF)"), (1917, 1927, "Segunda Divisão (APEA)"), (1928, 1934, "Primeira Divisão (APEA)"),
          (1935, 1937, "Divisão Intermediária"), (1938, 1940, "Divisão Intermediária (LPF)"), (1941, 1959, "Segunda Divisão"),
          (1960, 1976, "Primeira Divisão"), (1977, 1979, "Divisão Intermediária"), (1980, 1986, "Segunda Divisão"),
          (1987, 1990, "Divisão Especial"), (1991, 1993, "Divisão Intermediária"), (1994, 2100, "Série A2")]


def nome_oficial(temporada: str) -> str:
    a = ano_de(temporada)
    nome = next(n for i, f, n in _NOMES if i <= a <= f)
    return f"Campeonato Paulista {nome}"


# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Paulista Série A2"
