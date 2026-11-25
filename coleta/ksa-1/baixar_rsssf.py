"""Baixa as páginas da RSSSF da 1ª divisão saudita para data/coleta/ksa-1/rsssf/: a lista de campeões (sauchamp.html), a
história da Copa do Rei (saucuphist.html: os jogos de 1957 a 1974, quando a "His Majesty's League" era esse torneio) e
uma página por temporada (sau75.html ... sau99.html, sau00.html ... sau09.html, sau2010.html ...; o nome é o ano em que
a temporada termina). Até 1998/99 as páginas trazem quase só a tabela final; de 1999/00 em diante, os jogos com autores.

Uso: python coleta/ksa-1/baixar_rsssf.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "ksa-1" / "rsssf"
BASE = "https://www.rsssf.org/tabless/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in ("sauchamp.html", "saucuphist.html"):
        print(p, "ok" if pegar(BASE + p, PASTA / p) else "sem página", flush=True)
    for fim in range(1975, 2027):
        achou = None
        for nome in (f"sau{fim % 100:02d}.html", f"sau{fim}.html"):
            if pegar(BASE + nome, PASTA / nome, espera=1.0):
                achou = nome
                break
        print(fim, achou or "sem página", flush=True)
