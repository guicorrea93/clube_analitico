"""Baixa as fontes da 1ª divisão tcheca (cze-1), 1993/94 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/cze-1/):
  ogol   ogol (zerozero): calendário de cada edição, base dos jogos (rodada oficial, placar e código de cada clube).
         Páginas em data/cache/ogol-cze-1/.
  rsssf  RSSSF: página de cada temporada (tabela final, artilheiros), lista de campeões (tsjechamp.html) e de
         artilheiros (tsjetops.html).
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final, matriz, punições, grupos), com os modelos de tabela.
Sem football-data, engsoccerdata nem ESPN para a Tchéquia.

Uso: python coleta/cze-1/baixar.py ogol rsssf wiki
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import CACHE, DADOS, TEMPORADAS, rsssf_urls, temporada, wiki_titulo  # noqa: E402


def rsssf() -> None:
    for n in ("tsjechamp", "tsjetops"):
        d = pegar(f"https://www.rsssf.org/tablest/{n}.html", DADOS / "rsssf" / f"{n}.html", espera=2.0)
        print(f"rsssf {n}: {len(d or b'')} bytes", flush=True)
    for a in TEMPORADAS:
        for url in rsssf_urls(a):   # a 1ª candidata que existir
            nome = url.rsplit("/", 1)[1]
            d = pegar(url, DADOS / "rsssf" / nome, espera=2.0)
            if d:
                print(f"rsssf {temporada(a)} {nome}: {len(d)} bytes", flush=True)
                break
        else:
            print(f"rsssf {temporada(a)}: nenhuma página", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in [wiki_titulo(a) for a in TEMPORADAS] + ["List of Czech football champions"]:
        arq = pasta / (t.replace("/", "_") + ".wiki")
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=1.5)
        if txt is None:
            print(f"wiki: não achei '{t}'", flush=True)
            continue
        arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt)}", flush=True)
    # tabelas em modelos à parte; a 1ª em "<título> (tabela).wiki", as outras em "(tabela 2)", ...
    for a in TEMPORADAS:
        t = wiki_titulo(a)
        if not (pasta / f"{t}.wiki").exists():
            continue
        modelos = re.findall(r"\{\{(\d{4}[–-]\d{2,4} [A-Za-z' -]+? (?:table|results))\}\}",
                             (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        for i, mod in enumerate(dict.fromkeys(modelos), 1):
            arq = pasta / (f"{t} (tabela).wiki" if i == 1 else f"{t} (tabela {i}).wiki")
            if arq.exists():
                continue
            txt = wikitexto("en", f"Template:{mod}", espera=1.5)
            if txt:
                arq.write_text(txt, encoding="utf-8")
                print(f"wiki Template:{mod}: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1993-2005": só essas temporadas (para rodar várias frentes em paralelo)."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-cze-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = {int(n[:4]): i for i, n in edicoes("liga-checa", cache)}
    (pasta / "edicoes.json").write_text(json.dumps({temporada(a): eds[a] for a in sorted(eds)}, indent=0), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    # 2026/27 (em andamento): só para saber quem caiu em 2025/26 (clubes da temporada seguinte)
    for a in sorted((a for a in TEMPORADAS + [TEMPORADAS[-1] + 1] if int(ini) <= a <= int(fim)), reverse=True):
        arq = pasta / f"cze1_{a}.json"
        if arq.exists():
            continue
        js = calendario(eds[a], a, cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:   # "ogol=1993-2005" passa a faixa de temporadas
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
