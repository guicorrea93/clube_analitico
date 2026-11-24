"""Temporadas da 1ª divisão grega (gre-1), do primeiro campeonato reconhecido pela federação (1927/28) em diante.

Até 1958/59 o campeonato nacional (Panhellenic Championship) reunia os campeões das ligas regionais (Atenas, Pireu,
Salônica e, depois, outras) numa fase final; desde 1959/60, liga nacional (Alpha Ethniki; Super League desde 2006/07).
O campeonato SEGAS (1905/06 a 1911/12) e as ligas regionais de antes de 1927 não são reconhecidos pela federação.

Sem campeonato (lista de campeões da RSSSF, grkchamp.html): 1928/29, 1934/35, 1940/41 a 1944/45 (guerra), 1949/50 e
1951/52.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "gre-1"
CACHE = RAIZ / "data" / "cache"
NAO_DISPUTADAS = {1928, 1934, 1940, 1941, 1942, 1943, 1944, 1949, 1951}
TEMPORADAS = [a for a in range(1927, 2026) if a not in NAO_DISPUTADAS]
ANTIGAS = [a for a in TEMPORADAS if a <= 1958]       # fase final entre campeões regionais
LIGA = [a for a in TEMPORADAS if a >= 1959]          # liga nacional
OGOL_DESDE = 1993                                    # antes, o ogol só tem o campeão (sem jogos)


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 1958:
        return "Panhellenic Championship"
    return "Alpha Ethniki" if a <= 2005 else "Super League Greece"


def wiki_titulo(a: int) -> str:
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} {nome_oficial(a)}"


def rsssf_urls(a: int) -> list[str]:
    """Página da temporada na RSSSF, pelo ano final: 2 dígitos até 2008/09 (grk99.html = 1998/99) e 4 depois
    (grk2010.html = 2009/10); existe desde 1968/69 (matriz, tabela, artilheiros). Antes, só as páginas gerais:
    grkprehist.html (até 1958/59) e grkhist.html (1959/60 a 1998/99, matriz até 1980/81 e tabela), baixadas sempre.
    Devolve as candidatas, na ordem."""
    if a < 1968:
        return []
    f = a + 1
    return [f"https://www.rsssf.org/tablesg/grk{str(f)[-2:]}.html", f"https://www.rsssf.org/tablesg/grk{f}.html"]
