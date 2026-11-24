"""Temporadas da 1ª divisão belga (bel-1), da criação do campeonato (1895/96) em diante.

Sem campeonato (lista de campeões da RSSSF, belgchamp.html): 1914/15 a 1918/19 (Primeira Guerra Mundial), 1939/40 e
1940/41 (Segunda Guerra; as ligas foram abandonadas ou não houve) e 1944/45. As temporadas de 1941/42 a 1943/44, jogadas
na ocupação, são oficiais.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "bel-1"
CACHE = RAIZ / "data" / "cache"
GUERRA = set(range(1914, 1919)) | {1939, 1940, 1944}
TEMPORADAS = [a for a in range(1895, 2026) if a not in GUERRA]


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 2015:
        return "Belgian First Division"
    return "Belgian First Division A" if a <= 2021 else "Belgian Pro League"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} {nome_oficial(a)}"


def rsssf_url(a: int) -> str:
    """Até 2007/08: a página com todas as tabelas finais (belghist.html, colunas J V D E GP GC P). Depois, uma página
    por temporada, pelo ano final: belg2009.html = 2008/09."""
    if a <= 2007:
        return "https://www.rsssf.org/tablesb/belghist.html"
    return f"https://www.rsssf.org/tablesb/belg{a + 1}.html"
