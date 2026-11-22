"""Temporadas da 1ª divisão portuguesa (por-1), do Campeonato da Liga (1934/35) em diante.

1934/35 a 1937/38: Campeonato da Liga, experimental (o campeão nacional ainda saía do Campeonato de Portugal, em mata-mata);
os títulos dessa fase são contados hoje entre os da 1ª divisão (RSSSF, lista de campeões: 92 títulos desde 1934/35).
1938/39 em diante: Campeonato Nacional da 1ª Divisão, depois Primeira Liga.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "por-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = list(range(1934, 2026))


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a < 1938:
        return "Campeonato da Liga"
    return "Primeira Divisão" if a < 1999 else "Primeira Liga"


def wiki_titulo(a: int) -> str:
    """Título da Wikipédia em inglês; a API segue o redirecionamento ("1938–39 Primeira Liga" -> "1938–39 Primeira Divisão")."""
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} Primeira Liga"


def rsssf_url(a: int) -> str:
    """1934/35 a 2004/05: arquivo histórico (porthist193435.html: tabela final e matriz de resultados). Depois, uma página
    por temporada, pelo ano final: port06.html = 2005/06 ... port09.html; port2010.html = 2009/10."""
    if a <= 2004:
        return f"https://www.rsssf.org/tablesp/porthist{a}{str(a + 1)[-2:]}.html"
    f = a + 1
    return f"https://www.rsssf.org/tablesp/port{str(f)[-2:] if f < 2010 else f}.html"
