"""Temporadas da 1ª divisão holandesa (ned-1): a Eredivisie, da criação (1956/57) em diante.

Antes, o campeão nacional saía de ligas regionais com uma fase final (1888/89 a 1953/54) e, em 1954/55 e 1955/56, da
Hoofdklasse profissional em grupos: ficam de fora (como no Alemão antes da Bundesliga), à espera de decisão do Guilherme.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "ned-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = list(range(1956, 2026))


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "Eredivisie"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} Eredivisie"


def rsssf_url(a: int) -> str:
    """Uma página por temporada, pelo ano final: ned57.html = 1956/57 ... ned09.html = 2008/09; ned2010.html = 2009/10."""
    f = a + 1
    return f"https://www.rsssf.org/tablesn/ned{str(f)[-2:] if f < 2010 else f}.html"
