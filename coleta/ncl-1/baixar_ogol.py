"""Baixa os calendários do ogol da liga da Nova Caledônia ("Liga Nova Caledônia", competição 756) para data/cache/ogol-ncl-1/ e grava o resumo
dos jogos em data/coleta/ncl-1/ogol/<temporada>.json. As edições de 2010 a 2026 (as anteriores trazem só o campeão; algumas
recentes vêm vazias). Servem para os escudos (agente 1) e para a data dos jogos.

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html.

Uso: python coleta/ncl-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-ncl-1"
DEST = RAIZ / "data" / "coleta" / "ncl-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-nova-caledonia/756/edicoes)
EDICOES = {"2010": 11037, "2011": 43459, "2012": 56905, "2013": 65146, "2014": 75923, "2015": 100717, "2016": 102609,
           "2017": 125435, "2018": 130099, "2019": 140544, "2020": 150605, "2021": 162396, "2022": 175549, "2023": 182577,
           "2025": 197974, "2026": 214718}


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
