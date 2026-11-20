"""Baixa o calendário de cada edição da Série D no ogol para data/coleta/bra-serie-d/ogol/serie_d_{ano}.json.

Os códigos das edições vêm da lista de edições da página "brasileirao-serie-d" do ogol.

Uso: python coleta/bra-serie-d/baixar_ogol.py [ano ...]
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
CACHE = RAIZ / "data" / "cache" / "ogol_serie_d"
EDICOES = {
    2025: 195774, 2024: 185065, 2023: 173642, 2022: 162353, 2021: 154528, 2020: 146096, 2019: 131833, 2018: 122830,
    2017: 104759, 2016: 97700, 2015: 87524, 2014: 69548, 2013: 58344, 2012: 47394, 2011: 23482, 2010: 15013, 2009: 7827,
}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or sorted(EDICOES, reverse=True):
        assert ano in ANOS
        js = calendario(EDICOES[ano], CACHE, f"calendario_{ano}")
        (PASTA / f"serie_d_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada, fases {sorted({j['fase'] for j in js})[:8]}", flush=True)
