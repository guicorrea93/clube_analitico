"""Baixa os calendários do ogol da liga neozelandesa (2004/05 a 2025) para data/cache/ogol-nzl-1/ e grava o resumo dos jogos
em data/coleta/nzl-1/ogol/<temporada>.json. As edições de 1970-71 a 2002-03 do ogol só têm o campeão (não são baixadas).

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html (o agente 1 usa para os escudos).

Uso: python coleta/nzl-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-nzl-1"
DEST = RAIZ / "data" / "coleta" / "nzl-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-nova-zelandia/459/edicoes)
EDICOES = {"2004/05": 27465, "2005/06": 27464, "2006/07": 27463, "2007/08": 27462, "2008/09": 4152, "2009/10": 11008,
           "2010/11": 23827, "2011/12": 27461, "2012/13": 49173, "2013/14": 65113, "2014/15": 74449, "2015/16": 92166,
           "2016/17": 99607, "2017/18": 115326, "2018/19": 127731, "2019/20": 147025, "2020/21": 150387, "2022": 175517,
           "2023": 178865, "2024": 190753, "2025": 203071}


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
