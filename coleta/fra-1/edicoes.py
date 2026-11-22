"""Temporadas da 1ª divisão francesa (fra-1), da criação do campeonato profissional (1932/33) em diante."""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "fra-1"
CACHE = RAIZ / "data" / "cache"
# sem campeonato oficial: 1939/40 a 1944/45 (campeonatos de guerra, não reconhecidos)
GUERRA = set(range(1939, 1945))
TEMPORADAS = [a for a in range(1932, 2026) if a not in GUERRA]


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "Ligue 1" if a >= 2002 else "Division 1"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    if a >= 2002:
        return f"{t} Ligue 1"
    return f"{t} French Division 1"


def rsssf_url(a: int) -> str:
    """Uma página por temporada, pelo ano final: fran95.html = 1994/95 ... fran09.html = 2008/09; fran2010.html = 2009/10."""
    f = a + 1
    return f"https://www.rsssf.org/tablesf/fran{str(f)[-2:] if f < 2010 else f}.html"
