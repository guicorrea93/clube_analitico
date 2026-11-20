"""Baixa as páginas da Série C da RSSSF Brasil para data/coleta/bra-serie-c/rsssfbrasil/.

br{ano}l3.htm (uma por edição), br3camp.htm (campeões) e br3tops.htm (artilheiros).
Página já baixada não é baixada de novo (--de-novo força).

Uso: python coleta/bra-serie-c/baixar_rsssf.py [ano ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from edicoes import ANOS, PASTA_DADOS  # noqa: E402

PASTA = PASTA_DADOS / "rsssfbrasil"
BASE = "https://rsssfbrasil.com/tablesae/"

if __name__ == "__main__":
    de_novo = "--de-novo" in sys.argv
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()] or ANOS
    arquivos = [f"br{a}l3.htm" for a in anos] + ([] if len(sys.argv) > 1 and not de_novo else ["br3camp.htm", "br3tops.htm"])
    for arq in arquivos:
        dados = pegar(BASE + arq, PASTA / arq, espera=2.0, de_novo=de_novo)
        print(arq, "sem página" if dados is None else f"{len(dados)} bytes", flush=True)
