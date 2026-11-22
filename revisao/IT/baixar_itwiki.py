"""Baixa as páginas de temporada da Wikipédia it (action=raw) para a revisão da ita-1.
Uso: python -I revisao/IT/baixar_itwiki.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import baixar

ANOS = [a for a in range(1929, 2026) if a not in (1943, 1944)]


def titulo(a):
    if a == 1945:
        return "Divisione_Nazionale_1945-1946"
    return f"Serie_A_{a}-{a + 1}"


def url(a):
    return f"https://it.wikipedia.org/w/index.php?title={titulo(a)}&action=raw"


if __name__ == "__main__":
    for a in ANOS:
        arq = baixar(url(a))
        tam = os.path.getsize(arq) if arq else 0
        print(a, tam, flush=True)
