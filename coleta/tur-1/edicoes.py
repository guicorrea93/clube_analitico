"""Temporadas da 1ª divisão turca (tur-1): a liga nacional, da criação (1959, Milli Lig) em diante.

Antes de 1959 não havia liga nacional: só ligas regionais (Istambul, Ancara, Esmirna), o campeonato em mata-mata entre
os campeões regionais (Turkish Football Championship, 1924-1951) e a Divisão Nacional (Milli Küme, 1937-1950, entre os
clubes de Istambul, Ancara e Esmirna). A federação conta os títulos do campeonato turco a partir de 1959; essas
competições antigas ficam de fora (possível era antiga, se o Guilherme pedir).

A 1ª temporada (1959) foi jogada de fevereiro a junho de 1959: fica com a chave 1958 (o ogol a chama "1958/59") e o
rótulo "1959".
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "tur-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = list(range(1958, 2026))


def temporada(a: int) -> str:
    if a == 1958:
        return "1959"
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 1962:
        return "Millî Lig"
    return "1. Lig" if a <= 2000 else "Süper Lig"


def wiki_titulo(a: int) -> str:
    if a == 1958:
        return "1959 Turkish National League"
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"   # "1999–2000"
    nome = "Turkish National League" if a <= 1962 else "1.Lig" if a <= 2000 else "Süper Lig"
    return f"{t} {nome}"
