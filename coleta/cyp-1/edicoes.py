"""Temporadas do campeonato cipriota (cyp-1), de 1934/35 a 2025/26.

Escopo (Guilherme, 27/11/2026): os 86 títulos que a federação (CFA) reconhece, os mesmos da lista da RSSSF
(cypchamp.html). Ficam de fora os campeonatos não oficiais de 1931/32 a 1933/34, as temporadas sem campeão (1941/42 a
1943/44, guerra; 1958/59, não disputada; 1963/64, abandonada pelos conflitos na ilha; 2019/20, abandonada pela pandemia)
e 2026/27 (em andamento).

A chave de cada temporada é o rótulo ("1934/35").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "cyp-1"
CACHE = RAIZ / "data" / "cache"
SEM_CAMPEAO = {1941, 1942, 1943, 1958, 1963, 2019}
TEMPORADAS = [f"{a}/{str(a + 1)[-2:]}" for a in range(1934, 2026) if a not in SEM_CAMPEAO]
OGOL_DESDE = "2000/01"


def ano_inicio(t: str) -> int:
    return int(t[:4])


def ano_fim(t: str) -> int:
    return int(t[:4]) + 1


def nome_oficial(t: str) -> str:
    return "A' Katigoria"


def wiki_titulo(t: str) -> str:
    a = ano_inicio(t)
    return f"{a}–{str(a + 1)[-2:] if (a + 1) % 100 else a + 1} Cypriot First Division"


def rsssf_urls(t: str) -> list[str]:
    """Página da temporada na RSSSF, pelo ano final (cyp35.html = 1934/35); 2 ou 4 dígitos."""
    f = ano_fim(t)
    return [f"https://www.rsssf.org/tablesc/cyp{str(f)[-2:]}.html", f"https://www.rsssf.org/tablesc/cyp{f}.html"]
