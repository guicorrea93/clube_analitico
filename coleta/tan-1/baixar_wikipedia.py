"""Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Tanzanian Premier League") e o de cada temporada
("2006 Tanzanian Premier League", "2023–24 Tanzanian Premier League"), para data/coleta/tan-1/wikipedia/. Os artigos de
temporada trazem a tabela final: é a terceira fonte quando a tabela da RSSSF e os jogos não fecham.

Os artigos são pedidos em lote (até 50 títulos por pedido, com os redirecionamentos), para não esbarrar no limite de ritmo.

Uso: python coleta/tan-1/baixar_wikipedia.py
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
from wikipedia import UA, wikitexto  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "tan-1" / "wikipedia"


def arquivo(temporada: str) -> Path:
    return PASTA / f"en_{temporada.replace('/', '-')}.txt"


def lote(titulos: list[str]) -> dict[str, str]:
    """{título pedido: wikitexto} dos que existem (seguindo os redirecionamentos)."""
    q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                                "titles": "|".join(titulos), "redirects": 1, "format": "json", "formatversion": 2})
    for tentativa in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://en.wikipedia.org/w/api.php?{q}", headers=UA),
                                        timeout=60) as r:
                dados = json.loads(r.read())["query"]
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativa == 5:
                raise
            time.sleep(30 * (tentativa + 1))
    volta = {}
    for x in dados.get("normalized", []) + dados.get("redirects", []):
        volta[x["to"]] = volta.get(x["from"], x["from"])
    saida = {}
    for pag in dados.get("pages", []):
        if pag.get("missing") or not pag.get("revisions"):
            continue
        original = pag["title"]
        while original in volta:
            original = volta[original]
        saida[original] = pag["revisions"][0]["slots"]["main"]["content"]
    time.sleep(3)
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for nome, titulo in (("liga", "Tanzanian Premier League"),):
        if not arquivo(nome).exists():
            arquivo(nome).write_text(wikitexto("en", titulo) or "", encoding="utf-8")
    pedidos = {}
    from edicoes import EDICOES
    ligas = ("Tanzanian Premier League", "Tanzania Premier League", "Ligi Kuu Tanzania Bara")
    for e in EDICOES:
        if e.ano_inicio == e.ano_fim:
            rotulos = [str(e.ano_inicio)]
        else:
            yy = str(e.ano_fim)[-2:]
            rotulos = [f"{e.ano_inicio}–{yy}", f"{e.ano_inicio}–{e.ano_fim}"]
        for r in rotulos:
            for liga in ligas:
                pedidos[f"{r} {liga}"] = e.temporada
    achados: dict[str, str] = {}
    titulos = list(pedidos)
    for k in range(0, len(titulos), 50):
        for t, w in lote(titulos[k:k + 50]).items():
            achados.setdefault(pedidos[t], w)
    liga = arquivo("liga").read_text(encoding="utf-8")
    for temp in sorted(set(pedidos.values())):
        # artigo de temporada que redireciona para o artigo da liga (tabela de todos os tempos): fica vazio
        w = achados.get(temp, "")
        arquivo(temp).write_text("" if w == liga else w, encoding="utf-8")
    print(len(achados), "de", len(set(pedidos.values())), "temporadas com artigo;", "faltam:",
          sorted(set(pedidos.values()) - set(achados)))
