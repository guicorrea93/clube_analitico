"""Baixa as fontes do campeonato cipriota (cyp-1), 1934/35 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/cyp-1/):
  ogol     ogol (zerozero): calendário de cada edição desde 1995/96 (antes o ogol só tem o campeão; com jogos desde
           2000/01), base dos jogos. Páginas em data/cache/ogol-cyp-1/. Inclui 2026/27 (para saber quem caiu em 2025/26).
  rsssf    RSSSF: campeões (cypchamp.html), tabelas de 1931 a 1934 (cyphist.html), artilheiros (cyptops.html) e a página
           de cada temporada.
  wiki     Wikipédia em inglês: artigo de cada temporada (tabelas, matriz), com os modelos, em lotes (limite de ritmo).
Sem football-data e sem ESPN para Chipre.

Uso: python coleta/cyp-1/baixar.py ogol rsssf wiki
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import CACHE, DADOS, TEMPORADAS, rsssf_urls, wiki_titulo  # noqa: E402


def rsssf() -> None:
    for n in ("cypchamp", "cyphist", "cyptops"):
        d = pegar(f"https://www.rsssf.org/tablesc/{n}.html", DADOS / "rsssf" / f"{n}.html", espera=2.0)
        print(f"rsssf {n}: {len(d or b'')} bytes", flush=True)
    for t in TEMPORADAS:
        for url in rsssf_urls(t):
            d = pegar(url, DADOS / "rsssf" / url.rsplit("/", 1)[1], espera=2.0)
            if d:
                print(f"rsssf {t}: {url.rsplit('/', 1)[1]} {len(d)} bytes", flush=True)
                break


def _modelos(pasta: Path, lingua: str, titulo: str, padrao: str) -> None:
    from wikipedia import wikitexto
    txt = (pasta / f"{titulo}.wiki").read_text(encoding="utf-8")
    for i, mod in enumerate(dict.fromkeys(re.findall(padrao, txt)), 1):
        arq = pasta / f"{titulo} (tabela {i}).wiki"
        if arq.exists():
            continue
        x = wikitexto(lingua, f"Template:{mod}" if lingua == "en" else f"Mal:{mod}", espera=2.0)
        if x:
            arq.write_text(x, encoding="utf-8")
            print(f"wiki {lingua} Template:{mod}: {len(x)}", flush=True)


def _lote(titulos: list[str]) -> dict[str, str | None]:
    """Vários artigos num pedido só (a API aceita até 50 títulos); no 429, espera o que a Wikipédia pedir e tenta de
    novo, sem desistir cedo (o limite de ritmo vale por algumas horas depois de muitos pedidos)."""
    import time
    import urllib.error
    import urllib.parse
    import urllib.request
    q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                                "titles": "|".join(titulos), "redirects": 1, "format": "json", "formatversion": 2})
    ua = {"User-Agent": "clube-analitico/1.0 (projeto pessoal; estatisticas de futebol)"}
    for tentativa in range(40):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://en.wikipedia.org/w/api.php?{q}", headers=ua),
                                        timeout=60) as r:
                d = json.loads(r.read())["query"]
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativa == 39:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 60) + 30)
    nome = {x["from"]: x["to"] for x in d.get("normalized", []) + d.get("redirects", [])}
    paginas = {p["title"]: (None if p.get("missing") else p["revisions"][0]["slots"]["main"]["content"]) for p in d["pages"]}
    time.sleep(10)
    return {t: paginas.get(nome.get(nome.get(t, t), nome.get(t, t))) for t in titulos}


def wiki() -> None:
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    falta = [wiki_titulo(t) for t in TEMPORADAS if not (pasta / f"{wiki_titulo(t)}.wiki").exists()]
    for i in range(0, len(falta), 20):
        for titulo, txt in _lote(falta[i:i + 20]).items():
            if txt is None:
                print(f"wiki: não achei '{titulo}'", flush=True)
                continue
            (pasta / f"{titulo}.wiki").write_text(txt, encoding="utf-8")
            print(f"wiki {titulo}: {len(txt)}", flush=True)
    modelos = {}
    padrao = r"\{\{(\d{4}(?:[–-]\d{2,4})? [A-Za-z' .-]+? (?:table|results))\}\}"
    for t in TEMPORADAS:
        arq = pasta / f"{wiki_titulo(t)}.wiki"
        if arq.exists():
            for k, mod in enumerate(dict.fromkeys(re.findall(padrao, arq.read_text(encoding="utf-8"))), 1):
                destino = pasta / f"{wiki_titulo(t)} (tabela {k}).wiki"
                if not destino.exists():
                    modelos[f"Template:{mod}"] = destino
    nomes = list(modelos)
    for i in range(0, len(nomes), 20):
        for titulo, txt in _lote(nomes[i:i + 20]).items():
            if txt:
                modelos[titulo].write_text(txt, encoding="utf-8")
                print(f"wiki {titulo}: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1995-2005": só as temporadas que começam nesses anos."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-cyp-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = dict((n, i) for i, n in edicoes("liga-cipriota", cache))
    (pasta / "edicoes.json").write_text(json.dumps(eds, indent=0, ensure_ascii=False), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    alvo = [t for t in TEMPORADAS if t >= "1995/96"] + ["2026/27"]
    for t in sorted((t for t in alvo if int(ini) <= int(t[:4]) <= int(fim)), reverse=True):
        arq = pasta / f"cyp1_{t.replace('/', '-')}.json"
        if arq.exists() or t not in eds:
            if t not in eds:
                print(f"ogol: sem a edição {t}", flush=True)
            continue
        js = calendario(eds[t], int(t[:4]), cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {t}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
