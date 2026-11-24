"""Baixa os calendários do ogol da liga do Taiti ("Liga Taiti", competição 752) para data/cache/ogol-tah-1/ e grava o resumo
dos jogos em data/coleta/tah-1/ogol/<temporada>.json. Só as edições em que o ogol tem jogos (as outras trazem só o campeão):
2012/13 e 2013/14 (o playoff do título), 2021/22 e 2023/24. Servem para os escudos (agente 1) e de conferência.

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html.

Uso: python coleta/tah-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-tah-1"
DEST = RAIZ / "data" / "coleta" / "tah-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-taiti/752/edicoes)
EDICOES = {"2012/13": 65261, "2013/14": 67186, "2021/22": 175521, "2023/24": 186757}


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
