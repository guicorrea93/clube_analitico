"""Edições do Campeonato Paulista (1ª divisão, `bra-sp-1`): temporadas, anos e nomes oficiais.

1902 a 2025. Nos anos de ligas rivais a federação reconhece os dois títulos, e cada torneio vira uma edição com
temporada própria ("1913 LPF", "1913 APEA"): 1913-1916 (LPF e APEA), 1926-1929 (APEA e LAF) e 1935-1936 (LPF e APEA).
Fontes da lista: RSSSF Brasil (spcamp.htm) e ogol (edições "paulista-a1-1913-lpf" etc.).
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-sp-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

LIGAS = {1913: ("LPF", "APEA"), 1914: ("LPF", "APEA"), 1915: ("LPF", "APEA"), 1916: ("LPF", "APEA"),
         1926: ("APEA", "LAF"), 1927: ("APEA", "LAF"), 1928: ("APEA", "LAF"), 1929: ("APEA", "LAF"),
         1935: ("LPF", "APEA"), 1936: ("LPF", "APEA")}
TEMPORADAS = [f"{a} {l}" for a in range(1902, 2026) for l in LIGAS.get(a, ("",))]
TEMPORADAS = [t.strip() for t in TEMPORADAS]


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


# nome oficial por época (FPF): "Campeonato Paulista" até 1993; "Série A1" de 1994 em diante
def nome_oficial(temporada: str) -> str:
    a, liga = ano_de(temporada), liga_de(temporada)
    if liga:
        return f"Campeonato Paulista ({liga})"
    return "Campeonato Paulista Série A1" if a >= 1994 else "Campeonato Paulista"


# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Paulista"
