"""Temporadas da 1ª divisão italiana (ita-1), da criação da Serie A em grupo único (1929/30) em diante."""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "ita-1"
CACHE = RAIZ / "data" / "cache"
# sem campeonato oficial: 1943/44 (Campionato Alta Italia, não reconhecido) e 1944/45 (Segunda Guerra)
GUERRA = {1943, 1944}
TEMPORADAS = [a for a in range(1929, 2025) if a not in GUERRA]
DIVISIONE = 1945   # 1945/46: Divisione Nazionale (grupos Norte e Centro-Sul e grupo final)


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "Divisione Nazionale" if a == DIVISIONE else "Serie A"


def wiki_titulo(a: int) -> str:
    if a == DIVISIONE:
        return "1945–46 Italian Football Championship"
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} Serie A"


def rsssf_url(a: int) -> str:
    """Uma página por temporada, pelo ano final: ital30.html = 1929/30 ... ital09.html = 2008/09; ital2010.html = 2009/10."""
    f = a + 1
    return f"https://www.rsssf.org/tablesi/ital{str(f)[-2:] if f < 2010 else f}.html"
