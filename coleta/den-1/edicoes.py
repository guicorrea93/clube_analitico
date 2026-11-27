"""Temporadas do campeonato dinamarquês (den-1), de 1912/13 a 2025/26.

Escopo (Guilherme, 25/11/2026): os 112 títulos que a federação (DBU) reconhece, os mesmos da lista da RSSSF
(denchamp.html). Ficam de fora o campeonato de Copenhague de 1889 a 1912 (regional), 1914/15 (suspenso pela guerra),
1927/28 (terminou sem campeão) e 2026/27 (em andamento).

Eras:
  1912/13-1926/27  Landsfodboldturneringen: o campeão de Copenhague contra o vencedor do mata-mata das províncias;
  1928/29-1939/40  Danmarksturneringen (liga);
  1940/41-1944/45  torneio da guerra: 3 séries regionais e mata-mata;
  1945/46-1956/57  liga de outono a primavera (1956/57 com um ano e meio, em três turnos);
  1958-1990        ano civil; 1991 só a primavera (primeira Superliga);
  1991/92 em diante outono a primavera.

A chave de cada temporada é o rótulo ("1912/13", "1958", "1991", "1991/92").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "den-1"
CACHE = RAIZ / "data" / "cache"


def _par(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


LANDS = [_par(a) for a in range(1912, 1927) if a != 1914]
LIGA_ANTIGA = [_par(a) for a in range(1928, 1940)]
GUERRA = [_par(a) for a in range(1940, 1945)]
TEMPORADAS = LANDS + LIGA_ANTIGA + GUERRA + [_par(a) for a in range(1945, 1957)] + [str(a) for a in range(1958, 1992)] \
    + [_par(a) for a in range(1991, 2026)]
OGOL_DESDE = "1991/92"


def ano_inicio(t: str) -> int:
    return int(t[:4])


def ano_fim(t: str) -> int:
    return int(t[:4]) + (1 if "/" in t else 0)


def nome_oficial(t: str) -> str:
    a = ano_inicio(t)
    if t in LANDS:
        return "Landsfodboldturneringen"
    if t in LIGA_ANTIGA:
        return "Danmarksturneringen"
    if t in GUERRA:
        return "Danmarksmesterskabsturneringen (torneio da guerra)"
    if a < 1991:
        return "1. division"
    return "Superligaen"


def wiki_titulo(t: str) -> str:
    a = ano_inicio(t)
    par = f"{a}–{str(a + 1)[-2:] if (a + 1) % 100 else a + 1}"
    if t in LANDS:
        return f"{par} Danish National Football Tournament"
    if t in LIGA_ANTIGA:
        return f"{par} Danish Championship League"
    if t in GUERRA:
        return f"{par} Danish War Tournament"
    if "/" not in t:
        return f"{a} Danish 1st Division" if a <= 1990 else f"{a} Danish Superliga"
    return f"{par} Danish 1st Division" if a <= 1956 else f"{par} Danish Superliga"


def rsssf_urls(t: str) -> list[str]:
    """Página da temporada na RSSSF desde a Superliga, pelo ano final (den2026.html = 2025/26); 2 ou 4 dígitos."""
    if ano_inicio(t) < 1991 or t == "1991":
        return []
    f = ano_fim(t)
    return [f"https://www.rsssf.org/tablesd/den{str(f)[-2:]}.html", f"https://www.rsssf.org/tablesd/den{f}.html"]
