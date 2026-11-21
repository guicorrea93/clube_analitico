"""Temporadas da 1ª divisão alemã (ger-1): a Bundesliga, de 1963/64 em diante."""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "ger-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = list(range(1963, 2025))


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "Bundesliga"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} Bundesliga"


def rsssf_url(a: int) -> str:
    """Uma página por temporada, pelo ano final: duit64.html = 1963/64 ... duit09.html = 2008/09; duit2010.html = 2009/10."""
    f = a + 1
    return f"https://www.rsssf.org/tablesd/duit{str(f)[-2:] if f < 2010 else f}.html"
