"""Baixa o calendário de cada edição da Série C no ogol para data/coleta/bra-serie-c/ogol/serie_c_{ano}.json.

Os códigos das edições vêm da lista de edições da página "brasileirao-serie-c" do ogol. O ogol também tem
"edições" em 1982-1987, 1991, 1993 e 2000, que não são Série C oficial (veja edicoes.py) e ficam de fora.

Uso: python coleta/bra-serie-c/baixar_ogol.py [ano ...]
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
CACHE = RAIZ / "data" / "cache" / "ogol_serie_c"
EDICOES = {
    2026: 210279, 2025: 195756, 2024: 184797, 2023: 173159, 2022: 162160, 2021: 154396, 2020: 142587, 2019: 131652, 2018: 122395,
    2017: 104430, 2016: 97042, 2015: 79958, 2014: 67635, 2013: 57439, 2012: 42650, 2011: 21920, 2010: 15004, 2009: 6246,
    2008: 2305, 2007: 1596, 2006: 23173, 2005: 23174, 2004: 23175, 2003: 23176, 2002: 23177, 2001: 23178, 1999: 23179,
    1998: 23180, 1997: 135681, 1996: 135596, 1995: 23183, 1994: 23184, 1992: 23185, 1990: 23186, 1988: 23187, 1981: 23188,
}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or sorted(EDICOES, reverse=True):
        assert ano in ANOS
        js = calendario(EDICOES[ano], CACHE, f"calendario_{ano}")
        (PASTA / f"serie_c_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada, fases {sorted({j['fase'] for j in js})[:8]}", flush=True)
