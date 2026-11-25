"""Baixa os calendários do ogol da liga das Ilhas Salomão ("Liga Ilhas Salomão", competição 759) para
data/cache/ogol-sol-1/ e grava o resumo dos jogos em data/coleta/sol-1/ogol/<temporada>.json. No ogol o rótulo da edição
muitas vezes não é a temporada (ex.: "2012/13" = 2013/14, "2016/17" = 2017/18, "2020/21" = 2021): o mapa abaixo foi
conferido pelas datas e pelos clubes. Sem 2016, 2018 e 2020/21 no ogol; 2026 não entra. Servem para os escudos (agente 1)
e para a data dos jogos.

Arquivos do cache: calendario_<ano_inicio>_<id da edição>_p<página>.html.

Uso: python coleta/sol-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
import ogol  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "ogol-sol-1"
DEST = RAIZ / "data" / "coleta" / "sol-1" / "ogol"
# temporada -> id da edição no ogol (lista em https://www.ogol.com.br/competicao/liga-ilhas-salomao/759/edicoes)
EDICOES = {"2008/09": 11065, "2013/14": 69890, "2014/15": 82782, "2015/16": 95888, "2017/18": 120993, "2019/20": 142452,
           "2021": 162397, "2022/23": 175520, "2023": 183914, "2024": 187292, "2025": 203644}


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
