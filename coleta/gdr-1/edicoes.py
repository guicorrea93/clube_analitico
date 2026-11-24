"""Temporadas do campeonato da Alemanha Oriental (gdr-1): o campeonato da zona soviética (1948 e 1949, mata-mata entre os
campeões estaduais) e a DDR-Oberliga, de 1949/50 a 1990/91 (a última, como NOFV-Oberliga, já com a reunificação).

Chave de cada temporada = ano inicial, como nas outras ligas; a Oberliga seguiu o ano civil de 1956 a 1960 (chave =
o próprio ano, rótulo "1956"), depois de uma rodada de transição no segundo semestre de 1955 (Übergangsrunde, sem título
oficial; chave 1955, rótulo "1955"). A temporada longa de 1961/62 fechou a volta ao calendário de outono-primavera.
Os campeonatos de 1948 e 1949 têm chave 1947 e 1948 (rótulos "1948" e "1949").

Decisão do Guilherme (D-05b, 22/11/2026): competição à parte, `gdr-1`; a federação alemã (DFB) não conta esses títulos
como alemães.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "gdr-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = [1947, 1948] + list(range(1949, 1955)) + [1955, 1956, 1957, 1958, 1959, 1960] + list(range(1961, 1991))
ANO_CIVIL = {1955, 1956, 1957, 1958, 1959, 1960}


def temporada(a: int) -> str:
    if a in (1947, 1948):
        return str(a + 1)
    if a in ANO_CIVIL:
        return str(a)
    return f"{a}/{str(a + 1)[-2:]}"


def rsssf_pagina(a: int) -> str:
    """ddr48.html = 1948; ddr50.html = 1949/50; ddr55a.html = transição de 1955; ddr56.html = 1956; ddr62.html =
    1961/62; ddr91.html = 1990/91."""
    if a in (1947, 1948):
        return f"ddr{str(a + 1)[-2:]}.html"
    if a == 1955:
        return "ddr55a.html"
    if a in ANO_CIVIL:
        return f"ddr{str(a)[-2:]}.html"
    return f"ddr{str(a + 1)[-2:]}.html"


def wiki_titulo(a: int) -> str:
    if a in (1947, 1948):
        return f"{a + 1} Ostzonenmeisterschaft"
    if a == 1955:
        return "1955 DDR-Oberliga"
    if a in ANO_CIVIL:
        return f"{a} DDR-Oberliga"
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"
    return f"{t} {'NOFV-Oberliga' if a == 1990 else 'DDR-Oberliga'}"
