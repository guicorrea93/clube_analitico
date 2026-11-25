"""Baixa as fontes do campeonato polonês (pol-1), 1921 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/pol-1/):
  ogol   ogol (zerozero): calendário de cada edição desde 1962/63 (antes o ogol só tem o campeão), base dos jogos.
         Páginas em data/cache/ogol-pol-1/.
  fd     football-data.co.uk, POL.csv ("new"), desde 2012/13: placar e hora.
  rsssf  RSSSF: tabelas finais e torneios de 1920 a 2000/01 (polhist.html), página de cada temporada depois, lista de
         campeões (polchamp.html) e de artilheiros (poltops.html).
  wiki   Wikipédia em inglês: artigo de cada temporada (matriz, tabela final, punições, fichas), com os modelos.
Sem ESPN para a Polônia.

Uso: python coleta/pol-1/baixar.py ogol fd rsssf wiki
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

from edicoes import CACHE, DADOS, OGOL_DESDE, TEMPORADAS, rsssf_urls, wiki_titulo  # noqa: E402


def fd() -> None:
    d = pegar("https://www.football-data.co.uk/new/POL.csv", DADOS / "football-data" / "POL.csv", espera=1.5)
    print(f"football-data POL: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    for n in ("polchamp", "polhist", "poltops"):
        d = pegar(f"https://www.rsssf.org/tablesp/{n}.html", DADOS / "rsssf" / f"{n}.html", espera=2.0)
        print(f"rsssf {n}: {len(d or b'')} bytes", flush=True)
    for t in TEMPORADAS:
        for url in rsssf_urls(t):
            d = pegar(url, DADOS / "rsssf" / url.rsplit("/", 1)[1], espera=2.0)
            print(f"rsssf {t}: {len(d or b'')} bytes" if d else f"rsssf {t}: nenhuma página", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in [wiki_titulo(x) for x in TEMPORADAS] + ["List of Polish football champions"]:
        arq = pasta / (t.replace("/", "_") + ".wiki")
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=3.0)
        if txt is None:
            print(f"wiki: não achei '{t}'", flush=True)
            continue
        arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt)}", flush=True)
    for x in TEMPORADAS:
        t = wiki_titulo(x)
        if not (pasta / f"{t}.wiki").exists():
            continue
        modelos = re.findall(r"\{\{(\d{4}(?:[–-]\d{2,4})? [A-Za-z' -]+? (?:table|results))\}\}",
                             (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        for i, mod in enumerate(dict.fromkeys(modelos), 1):
            arq = pasta / (f"{t} (tabela).wiki" if i == 1 else f"{t} (tabela {i}).wiki")
            if arq.exists():
                continue
            txt = wikitexto("en", f"Template:{mod}", espera=3.0)
            if txt:
                arq.write_text(txt, encoding="utf-8")
                print(f"wiki Template:{mod}: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1962-1990": só as temporadas que começam nesses anos."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-pol-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = dict((n, i) for i, n in edicoes("liga-polaca", cache))
    (pasta / "edicoes.json").write_text(json.dumps(eds, indent=0, ensure_ascii=False), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    alvo = [t for t in TEMPORADAS if "/" in t and t >= OGOL_DESDE] + ["2026/27"]
    for t in sorted((t for t in alvo if int(ini) <= int(t[:4]) <= int(fim)), reverse=True):
        arq = pasta / f"pol1_{t.replace('/', '-')}.json"
        if arq.exists():
            continue
        js = calendario(eds[t], int(t[:4]), cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {t}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
