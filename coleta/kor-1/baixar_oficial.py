"""Baixa do site oficial da K League (www.kleague.com) a linha do tempo de cada jogo da K League 1 de 2013 a 2025
(/api/ddf/match/matchInfo.do): gols (com o código e o nome do jogador), assistências, cartões, substituições, com o tempo
e o minuto. Em coreano e em inglês (a língua vem da sessão: /changeLang.do), porque o nome em inglês é o único jeito de
escrever os estrangeiros. A lista de jogos é a do calendário (data/coleta/kor-1/portal/calendario_<ano>.json, que de 2013
em diante vem do próprio site oficial). A API não responde para os anos anteriores (erro 500): 1983-2012 vêm do portal.

Guardado comprimido em data/cache/kleague-asia/oficial/<ano>_<meetSeq>_<gameId>_<ko|en>.json.gz (fora do git).

Uso: python coleta/kor-1/baixar_oficial.py [ano ...]
"""
from __future__ import annotations

import gzip
import http.cookiejar
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from competicoes import eh_primeira  # noqa: E402

RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "kleague-asia" / "oficial"
CAL = RAIZ / "data" / "coleta" / "kor-1" / "portal"
BASE = "https://www.kleague.com"
ESPERA = 0.4


def sessao(lingua: str):
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    op.addheaders = [("User-Agent", "Mozilla/5.0 (clube-analitico; projeto pessoal de estatisticas)")]
    op.open(BASE + "/", timeout=60).read()
    if lingua == "en":
        op.open(urllib.request.Request(BASE + "/changeLang.do", data=b"", method="POST"), timeout=60).read()
    return op


def pegar(op, j: dict, lingua: str) -> None:
    arq = CACHE / f"{j['ano']}_{j['meet_seq']}_{j['game_id']}_{lingua}.json.gz"
    if arq.exists():
        return
    u = BASE + "/api/ddf/match/matchInfo.do?" + urllib.parse.urlencode({"year": j["ano"], "meetSeq": j["meet_seq"],
                                                                       "gameId": j["game_id"]})
    for t in range(6):
        time.sleep(ESPERA)
        try:
            b = op.open(u, timeout=60).read()
            if json.loads(b).get("resultCode") == "200":
                break
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError):
            pass
        time.sleep(5 * (t + 1))
    else:
        print("AVISO: sem linha do tempo:", j, lingua, flush=True)
        return
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_bytes(gzip.compress(b))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sessoes = {"ko": sessao("ko"), "en": sessao("en")}
    for ano in [int(a) for a in sys.argv[1:]] or range(2013, 2026):
        js = [j for j in json.loads((CAL / f"calendario_{ano}.json").read_text(encoding="utf-8")) if eh_primeira(j)]
        for j in js:
            for lingua, op in sessoes.items():
                pegar(op, j, lingua)
        print(ano, len(js), "jogos ok", flush=True)
