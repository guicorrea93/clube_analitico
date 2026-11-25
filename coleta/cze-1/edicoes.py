"""Temporadas da 1ª divisão tcheca (cze-1): a liga da República Tcheca, desde a separação da Tchecoslováquia (1993/94).

A liga tchecoslovaca (1925-1993) e a liga do Protetorado da Boêmia e Morávia (1938/39-1943/44) ficam na competição da
Tchecoslováquia, à parte (decisão do Guilherme, 25/11/2026).
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "cze-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = list(range(1993, 2026))
GRUPOS_DESDE = 2022   # fase regular e grupos (título, Europa, rebaixamento)


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "1. liga" if a <= 1996 else "Gambrinus liga" if a <= 2013 else "Fortuna liga" if a <= 2023 else "Chance liga"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} Czech First League"


def rsssf_urls(a: int) -> list[str]:
    """Página da temporada na RSSSF, pelo ano final: 2 dígitos até 2008/09 (tsje94.html = 1993/94) e 4 depois
    (tsje2010.html = 2009/10). Devolve as candidatas, na ordem."""
    f = a + 1
    if a <= 2008:   # "tsje22.html" existe e não é 2021/22: os 2 dígitos só valem até 2008/09
        return [f"https://www.rsssf.org/tablest/tsje{str(f)[-2:]}.html"]
    return [f"https://www.rsssf.org/tablest/tsje{f}.html"]
