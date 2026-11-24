"""Baixa os calendários do ogol da liga de Fiji ("Liga Ilhas Fiji", competição 590) para data/cache/ogol-fij-1/ e grava o resumo
dos jogos em data/coleta/fij-1/ogol/<temporada>.json. As edições de 2009 a 2026 (as anteriores trazem só o campeão; algumas
recentes vêm vazias). Servem para os escudos (agente 1) e para a data dos jogos.

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html.

Uso: python coleta/fij-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-fij-1"
DEST = RAIZ / "data" / "coleta" / "fij-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-ilhas-fiji/590/edicoes)
EDICOES = {"2009": 6303, "2010": 32121, "2011": 65089, "2012": 46961, "2013": 65023, "2014": 69888, "2015": 81909, "2016": 103868,
           "2017": 125431, "2018": 127535, "2019": 140513, "2020": 147726, "2021": 154087, "2022": 175516, "2023": 180867,
           "2024": 183087, "2025": 195558, "2026": 214708}


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
