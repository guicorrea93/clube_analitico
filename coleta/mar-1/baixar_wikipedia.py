"""Baixa da Wikipédia em inglês (wikitexto, pela API) a lista de campeões ("List of Moroccan football champions"), o artigo
da liga ("Botola Pro") e o de cada temporada desde 1956/57 ("1993–94 Botola"; nos anos recentes, "Botola Pro"), para
data/coleta/mar-1/wikipedia/. Os artigos de temporada trazem a tabela final: é a terceira fonte quando a tabela da RSSSF e
os jogos não fecham. Antes de 1956/57 não há artigos de temporada.

Os artigos são pedidos em lote (até 50 títulos por pedido, com os redirecionamentos), para não esbarrar no limite de ritmo.

Uso: python coleta/mar-1/baixar_wikipedia.py
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
from wikipedia import UA, wikitexto  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "mar-1" / "wikipedia"


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
    for nome, titulo in (("campeoes", "List of Moroccan football champions"), ("liga", "Botola Pro")):
        if not arquivo(nome).exists():
            arquivo(nome).write_text(wikitexto("en", titulo) or "", encoding="utf-8")
    pedidos = {}
    for a in range(1956, 2026):
        yy = str(a + 1)[-2:]
        for t in (f"{a}–{yy} Botola", f"{a}–{yy} Botola Pro", f"{a}–{yy} Botola Pro 1"):
            pedidos[t] = f"{a}/{yy}"
    achados: dict[str, str] = {}
    titulos = list(pedidos)
    for k in range(0, len(titulos), 50):
        for t, w in lote(titulos[k:k + 50]).items():
            achados.setdefault(pedidos[t], w)
    liga = arquivo("liga").read_text(encoding="utf-8")
    for temp in sorted(set(pedidos.values())):
        # "1972–73 Botola" e "1989–90 Botola" redirecionam para o artigo da liga, cuja tabela é a de todos os tempos: fica vazio
        w = achados.get(temp, "")
        arquivo(temp).write_text("" if w == liga else w, encoding="utf-8")
    print(len(achados), "de", len(set(pedidos.values())), "temporadas com artigo;", "faltam:",
          sorted(set(pedidos.values()) - set(achados)))
