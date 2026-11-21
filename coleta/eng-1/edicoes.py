"""Temporadas da 1ª divisão inglesa (eng-1) e nomes oficiais de cada época."""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "eng-1"
CACHE = RAIZ / "data" / "cache"
# sem liga: 1915/16-1918/19 (1ª Guerra) e 1939/40-1945/46 (2ª Guerra; 1939/40 parou na 3ª rodada e foi anulada)
GUERRA = set(range(1915, 1919)) | set(range(1939, 1946))
TEMPORADAS = [a for a in range(1888, 2026) if a not in GUERRA]


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 1891:
        return "Football League"
    if a <= 1991:
        return "Football League First Division"
    if a <= 2006:
        return "FA Premier League"
    return "Premier League"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1899–1900"
    if a >= 2007:
        return f"{t} Premier League"
    if a >= 1992:
        return f"{t} FA Premier League"
    return f"{t} Football League"
