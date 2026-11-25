"""Temporadas do campeonato norueguês (nor-1), de 1937/38 a 2025.

Escopo (Guilherme, 25/11/2026): os 79 títulos de liga que a federação (NFF) reconhece, os mesmos da lista da RSSSF
(noochamp.html). Ficam de fora a Prøveligaen de 1914-16 (liga de teste), 1939/40 (interrompida pela guerra), 1940-1947
(sem campeonato) e a copa (o "campeão norueguês" até 1937 era o vencedor da copa: fase 2, nor-copa). 2026 entra quando
a temporada terminar.

Eras:
  1937/38, 1938/39, 1947/48  Norgesserien: 11 grupos regionais e mata-mata entre os primeiros;
  1948/49-1960/61            Hovedserien: dois grupos de 8 e final entre os primeiros;
  1961/62                    Hovedserien de um ano e meio, grupo único (passagem para o ano civil; não há "1962");
  1963 em diante             ano civil (1. divisjon, Tippeligaen desde 1991, Eliteserien desde 2017).

A chave de cada temporada é o rótulo ("1937/38", "1963").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "nor-1"
CACHE = RAIZ / "data" / "cache"
NORGESSERIEN = ["1937/38", "1938/39", "1947/48"]
TEMPORADAS = NORGESSERIEN + [f"{a}/{str(a + 1)[-2:]}" for a in range(1948, 1962)] + [str(a) for a in range(1963, 2026)]
OGOL_DESDE = "1961/62"


def ano_inicio(t: str) -> int:
    return int(t[:4])


def ano_fim(t: str) -> int:
    return int(t[:4]) + (1 if "/" in t else 0)


def nome_oficial(t: str) -> str:
    a = ano_inicio(t)
    if t in NORGESSERIEN:
        return "Norgesserien"
    if "/" in t:
        return "Hovedserien"
    return "1. divisjon" if a <= 1990 else "Tippeligaen" if a <= 2016 else "Eliteserien"


def wiki_titulo(t: str) -> str:
    a = ano_inicio(t)
    if t in NORGESSERIEN:
        return f"{a}–{str(a + 1)[-2:]} Norgesserien"
    if "/" in t:
        return f"{a}–{str(a + 1)[-2:]} Hovedserien"
    return f"{a} Norwegian First Division" if a <= 1990 else f"{a} Tippeligaen" if a <= 2016 else f"{a} Eliteserien"


def wiki_no_titulo(t: str) -> str:
    """Artigo da Wikipédia em norueguês (só para a Norgesserien, que tem algumas matrizes dos grupos)."""
    a = ano_inicio(t)
    return f"Norgesserien {a}–{str(a + 1)[-2:]}"


def rsssf_urls(t: str) -> list[str]:
    """Página da temporada na RSSSF: 2 dígitos até 2009 (noo08.html), 4 depois (noo2010.html); as duas formas são
    tentadas no baixar."""
    if "/" in t:
        return []
    a = ano_inicio(t)
    return [f"https://www.rsssf.org/tablesn/noo{str(a)[-2:]}.html", f"https://www.rsssf.org/tablesn/noo{a}.html"]
