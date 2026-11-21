"""Baixa da Wikipédia em espanhol o texto-fonte das páginas "Campeonato Uruguayo de Primera División <ano>" (1900 a 1993)
para data/coleta/uru-1/wikipedia/es_<ano>.txt. Elas trazem os jogos (seção "Fixture") dos anos que a RSSSF não tem:
1900, 1901, 1905, 1908, 1916 (tabela cruzada), 1960-1964, 1966-1968 e 1970-1974.

Uso: python coleta/uru-1/baixar_wikipedia.py [ano ...]
"""
from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "uru-1" / "wikipedia"
URL = "https://es.wikipedia.org/w/index.php?title={t}&action=raw"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for ano in [int(a) for a in sys.argv[1:]] or range(1900, 1994):
        t = urllib.parse.quote(f"Campeonato_Uruguayo_de_Primera_División_{ano}")
        b = pegar(URL.format(t=t), PASTA / f"es_{ano}.txt", espera=1.0)
        n = (b or b"").decode("utf-8", "ignore")
        print(ano, "404" if b is None else f"{len(n)} bytes, {n.count('Fixture')} fixture", flush=True)
