"""Temporadas da 1ª divisão espanhola (esp-1)."""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "esp-1"
CACHE = RAIZ / "data" / "cache"
# sem liga: 1936/37-1938/39 (Guerra Civil)
GUERRA = {1936, 1937, 1938}
TEMPORADAS = [a for a in range(1928, 2026) if a not in GUERRA]


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    return "Primera División"


def wiki_titulo(a: int) -> str:
    if a == 1928:   # a primeira liga foi jogada só em 1929 (fevereiro a junho)
        return "1929 La Liga"
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    return f"{t} La Liga"


def rsssf_url(a: int) -> str:
    """Tabela final e matriz: arquivo por década até 1999/2000 (spanhist<aa><aa>.html, âncora da temporada);
    depois, um arquivo por temporada (span01.html = 2000/01 ... span09.html, span2010.html = 2009/10 ...)."""
    if a <= 1998:
        dec = {1928: "2839", 1939: "3949", 1949: "4959", 1959: "5969", 1969: "6979", 1979: "7989", 1989: "8999"}
        ini = max(k for k in dec if k <= a)
        return f"https://www.rsssf.org/tabless/spanhist{dec[ini]}.html"
    if a == 1999:
        return "https://www.rsssf.org/tabless/spanhist9909.html"
    f = a + 1
    return f"https://www.rsssf.org/tabless/span{str(f)[-2:] if f < 2010 else f}.html"
