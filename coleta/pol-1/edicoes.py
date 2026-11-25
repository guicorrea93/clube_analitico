"""Temporadas do campeonato polonês (pol-1), de 1921 a 2025/26.

Escopo (Guilherme, 25/11/2026): os 98 títulos que a federação (PZPN) reconhece, os mesmos da lista da RSSSF
(polchamp.html). Ficam de fora 1920 (abandonado pela guerra com a União Soviética), 1924 (não disputado), 1939
(interrompido pela guerra, sem campeão) e as ligas municipais de 1940 a 1945.

Eras:
  1921-1926, 1946 e 1947  torneio final entre os campeões regionais;
  1927-1938, 1948-1962    liga em ano civil (1962: só a primavera, na passagem para o calendário de outono-primavera);
  1962/63 em diante       liga de outono a primavera.

A chave de cada temporada é o rótulo ("1938", "1962", "1962/63"), porque "1962" (primavera) e "1962/63" começam no mesmo
ano.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "pol-1"
CACHE = RAIZ / "data" / "cache"
TORNEIOS = ["1921", "1922", "1923", "1925", "1926", "1946", "1947"]
TEMPORADAS = ["1921", "1922", "1923", "1925", "1926"] + [str(a) for a in range(1927, 1939)] + ["1946", "1947"] \
    + [str(a) for a in range(1948, 1963)] + [f"{a}/{str(a + 1)[-2:]}" for a in range(1962, 2026)]
OGOL_DESDE = "1962/63"


def ano_inicio(t: str) -> int:
    return int(t[:4])


def ano_fim(t: str) -> int:
    return int(t[:4]) + (1 if "/" in t else 0)


def nome_oficial(t: str) -> str:
    if t in TORNEIOS:
        return "Mistrzostwa Polski (torneio final)"
    return "Liga" if ano_inicio(t) <= 1938 else "I liga" if ano_inicio(t) <= 2007 else "Ekstraklasa"


def wiki_titulo(t: str) -> str:
    if t in TORNEIOS:
        return f"{t} Polish Football Championship"
    if "/" not in t:
        return f"{t} Ekstraklasa"
    a = ano_inicio(t)
    return f"{a}–{a + 1 if (a + 1) % 100 == 0 else str(a + 1)[-2:]} Ekstraklasa"


def rsssf_urls(t: str) -> list[str]:
    """Até 2000/01, a página das tabelas finais (polhist.html, baixada sempre); depois, uma página por temporada, pelo
    ano final: 2 dígitos até 2008/09 (pol02.html = 2001/02) e 4 depois (pol2010.html = 2009/10)."""
    if "/" not in t or ano_inicio(t) <= 2000:
        return []
    f = ano_fim(t)
    if f <= 2009:
        return [f"https://www.rsssf.org/tablesp/pol{str(f)[-2:]}.html"]
    return [f"https://www.rsssf.org/tablesp/pol{f}.html"]
