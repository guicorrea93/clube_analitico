"""Baixa os calendários do ogol da liga de Papua-Nova Guiné ("Liga Papua-Nova Guiné", competição 2828) para
data/cache/ogol-png-1/ e grava o resumo dos jogos em data/coleta/png-1/ogol/<temporada>.json. Só as edições de 2013 em diante
(as anteriores não têm jogos no ogol; 2021 não entra). No ogol o rótulo da edição às vezes é o ano seguinte ou o anterior: o
mapa abaixo foi conferido pelos clubes e pelo campeão. Servem para os escudos (agente 1) e para a data dos jogos.

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html.

Uso: python coleta/png-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-png-1"
DEST = RAIZ / "data" / "coleta" / "png-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-papua-nova-guine/2828/edicoes)
EDICOES = {"2013": 78223, "2014": 77900, "2015": 84563, "2015/16": 95555, "2018": 125254, "2019": 142045, "2019/20": 160457,
           "2022": 175518, "2023": 188345, "2024": 209787, "2025": 203761, "2026": 219433}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    DEST.mkdir(parents=True, exist_ok=True)
    for t, ed in EDICOES.items():
        if sys.argv[1:] and t not in sys.argv[1:]:
            continue
        jogos = ogol.calendario(ed, CACHE, f"calendario_{t[:4]}")
        (DEST / f"{t.replace('/', '-')}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=1), encoding="utf-8")
        print(t, ed, len(jogos), flush=True)


if __name__ == "__main__":
    main()
