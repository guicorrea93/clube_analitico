"""Baixa do site oficial da K League (www.kleague.com, /record/teamRank.do) a classificação final de cada ano
(a 1ª divisão): posição oficial (com a divisão em grupos), jogos, vitórias, empates, derrotas, gols e pontos de
cada clube, pelo código do clube. O site só tem os anos de 2003 em diante (antes devolve a tabela vazia).

Guardado em data/coleta/kor-1/oficial/tabela_<ano>.json.

Uso: python coleta/kor-1/baixar_tabelas.py [ano ...]
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PASTA = AQUI.parent.parent / "data" / "coleta" / "kor-1" / "oficial"
URL = "https://www.kleague.com/record/teamRank.do?leagueId=1&year={ano}&stadium=all&recordType=rank"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or range(1983, 2026):
        req = urllib.request.Request(URL.format(ano=ano), data=b"", method="POST",
                                     headers={"User-Agent": "Mozilla/5.0 (clube-analitico; projeto pessoal de estatisticas)"})
        d = json.loads(urllib.request.urlopen(req, timeout=60).read())["data"]
        if not d.get("teamRank"):
            print(ano, "sem tabela", flush=True)
            continue
        linhas = [{k: r.get(k) for k in ("rank", "teamId", "teamName", "gameCount", "winCnt", "tieCnt", "lossCnt", "gainGoal",
                                         "lossGoal", "gainPoint", "assignGameType")} for r in d["teamRank"]]
        (PASTA / f"tabela_{ano}.json").write_text(json.dumps({"dividida": d.get("isSplitRank"), "tabela": linhas},
                                                             ensure_ascii=False, indent=1), encoding="utf-8")
        print(ano, len(linhas), "clubes", flush=True)
        time.sleep(1)
