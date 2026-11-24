"""Baixa as páginas da RSSSF da 1ª divisão sul-coreana para data/coleta/kor-1/rsssf/: a lista de campeões (skorchamp.html),
as tabelas finais (skorhist.html) e uma página por temporada (skor83.html ... skor99.html, skor2000.html ...; a RSSSF usa
os dois jeitos de escrever o ano, e nem todo ano tem página). As páginas trazem as tabelas (base da conferência) e, em
alguns anos, a tabela de confrontos.

Uso: python coleta/kor-1/baixar_rsssf.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "kor-1" / "rsssf"
BASE = "https://www.rsssf.org/tabless/"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in ("skorchamp.html", "skorhist.html"):
        pegar(BASE + p, PASTA / p)
    for ano in range(1983, 2026):
        achou = None
        for nome in (f"skor{ano % 100:02d}.html", f"skor{ano}.html"):
            if pegar(BASE + nome, PASTA / nome):
                achou = nome
                break
        print(ano, achou or "sem página", flush=True)
