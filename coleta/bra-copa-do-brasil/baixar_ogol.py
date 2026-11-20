"""Baixa o calendário de cada edição da Copa do Brasil no ogol para data/coleta/bra-copa-do-brasil/ogol/copa_brasil_{ano}.json.

Os códigos das edições vêm da lista de edições da página "copa-do-brasil" do ogol.

Uso: python coleta/bra-copa-do-brasil/baixar_ogol.py [ano ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from ogol import calendario  # noqa: E402
from edicoes import ANOS, PASTA_DADOS, RAIZ  # noqa: E402

PASTA = PASTA_DADOS / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol_copa_brasil"
EDICOES = {
    2025: 195104, 2024: 183035, 2023: 172209, 2022: 161682, 2021: 153672, 2020: 140824, 2019: 130357, 2018: 120540,
    2017: 102810, 2016: 93524, 2015: 75366, 2014: 66292, 2013: 54588, 2012: 39492, 2011: 19734, 2010: 12696,
    2009: 4626, 2008: 2238, 2007: 11038, 2006: 11027, 2005: 10988, 2004: 10967, 2003: 10845, 2002: 6560,
    2001: 6462, 2000: 6399, 1999: 4674, 1998: 4658, 1997: 4640, 1996: 4627, 1995: 4497, 1994: 4492,
    1993: 4476, 1992: 4381, 1991: 4379, 1990: 4378, 1989: 4374,
}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or sorted(EDICOES, reverse=True):
        assert ano in ANOS
        js = calendario(EDICOES[ano], CACHE, f"calendario_{ano}")
        (PASTA / f"copa_brasil_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada, fases {sorted({j['fase'] for j in js})[:8]}", flush=True)
