"""Temporadas da 1ª divisão escocesa (sco-1), da criação da Scottish Football League (1890/91) em diante.

Sem 1939/40 a 1945/46: o campeonato de 1939/40 foi abandonado depois de 5 rodadas, com a guerra, e os seguintes foram
ligas regionais de guerra, não reconhecidas (como no Inglês).
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "sco-1"
CACHE = RAIZ / "data" / "cache"
GUERRA = set(range(1939, 1946))
TEMPORADAS = [a for a in range(1890, 2026) if a not in GUERRA]


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 1892:
        return "Scottish Football League"
    if a <= 1974:
        return "Scottish Division One"
    if a <= 1997:
        return "Scottish Premier Division"
    return "Scottish Premier League" if a <= 2012 else "Scottish Premiership"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} {nome_oficial(a)}"


def rsssf_url(a: int) -> str:
    """Até 1998/99: a página com todas as tabelas finais (scothist.html). Depois, uma página por temporada, pelo ano final:
    scot00.html = 1999/2000 ... scot09.html; scot2010.html = 2009/10."""
    if a <= 1998:
        return "https://www.rsssf.org/tabless/scothist.html"
    f = a + 1
    return f"https://www.rsssf.org/tabless/scot{str(f)[-2:] if f < 2010 else f}.html"
