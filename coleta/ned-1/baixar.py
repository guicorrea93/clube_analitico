"""Baixa as fontes da 1ª divisão holandesa (ned-1), 1956/57 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/ned-1/):
  esd    engsoccerdata (GitHub jalapic/engsoccerdata, GPL >= 2): os jogos da Eredivisie, 1956/57-2024/25.
         Bruto em data/cache/engsoccerdata-europa/.
  fd     football-data.co.uk, N1.csv de 1993/94 a 2025/26: placar, hora, árbitro, estatísticas e cartões por time.
  rsssf  RSSSF: uma página por temporada, com a tabela final e a matriz de resultados.
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final, punições), lista de campeões e de artilheiros.
  ogol   ogol: calendário de cada edição (rodada oficial e código de cada clube). Páginas em data/cache/ogol-ned-1/.
  espn   ESPN (liga ned.1), 2001/02 em diante: hora, estádio, público, gols e cartões com minuto.

Uso: python coleta/ned-1/baixar.py esd fd rsssf wiki ogol espn
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import CACHE, DADOS, TEMPORADAS, rsssf_url, temporada, wiki_titulo  # noqa: E402


def esd() -> None:
    bruto = CACHE / "engsoccerdata-europa"
    pegar("https://raw.githubusercontent.com/jalapic/engsoccerdata/master/data-raw/holland.csv", bruto / "holland.csv")
    pasta = DADOS / "engsoccerdata"
    pasta.mkdir(parents=True, exist_ok=True)
    with (bruto / "holland.csv").open(encoding="utf-8") as f, (pasta / "holland_tier1.csv").open("w", encoding="utf-8", newline="") as g:
        r = csv.DictReader(f)
        w = csv.DictWriter(g, fieldnames=r.fieldnames)
        w.writeheader()
        n = 0
        for x in r:
            if x["tier"] == "1":
                w.writerow(x); n += 1
    print(f"engsoccerdata: {n} jogos da 1ª divisão")


def fd() -> None:
    for a in range(1993, 2026):
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        d = pegar(f"https://www.football-data.co.uk/mmz4281/{cod}/N1.csv", DADOS / "football-data" / f"N1_{cod}.csv", espera=1.5)
        print(f"football-data {cod}: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    urls = [rsssf_url(a) for a in TEMPORADAS] + ["https://www.rsssf.org/tablesn/nedchamp.html",
                                                 "https://www.rsssf.org/tablesn/nedtops.html"]   # campeões e artilheiros
    for url in dict.fromkeys(urls):
        nome = url.rsplit("/", 1)[1]
        d = pegar(url, DADOS / "rsssf" / nome, espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    titulos = [wiki_titulo(a) for a in TEMPORADAS] + ["List of Dutch football champions", "List of Eredivisie top scorers"]
    for t in titulos:
        arq = pasta / (t.replace("/", "_") + ".wiki")
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=1.5)
        if txt is None:
            print(f"wiki: não achei '{t}'", flush=True)
            continue
        arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt)}", flush=True)
    # temporadas recentes: a tabela fica num modelo à parte ("{{2024–25 Eredivisie table}}"), guardado como "<título> (tabela).wiki"
    for a in TEMPORADAS:
        t = wiki_titulo(a)
        arq = pasta / f"{t} (tabela).wiki"
        if arq.exists() or not (pasta / f"{t}.wiki").exists():
            continue
        m = re.search(r"\{\{(\d{4}[–-]\d{2} Eredivisie table)\}\}", (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        if not m:   # o nome do modelo pode vir com hífen ("{{2022-23 Eredivisie table}}")
            continue
        txt = wikitexto("en", f"Template:{m.group(1)}", espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
            print(f"wiki Template:{t} table: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1956-1990": só essas temporadas (para rodar várias frentes em paralelo)."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-ned-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = {int(n[:4]): i for i, n in edicoes("campeonato-holandes", cache)}
    (pasta / "edicoes.json").write_text(json.dumps({temporada(a): eds[a] for a in sorted(eds)}, indent=0), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    # 2026/27 (em andamento): só para saber quem caiu em 2025/26 (clubes da temporada seguinte)
    for a in sorted((a for a in TEMPORADAS + [TEMPORADAS[-1] + 1] if int(ini) <= a <= int(fim)), reverse=True):
        arq = pasta / f"ned1_{a}.json"
        if arq.exists():
            continue
        js = calendario(eds[a], a, cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


def espn() -> None:
    from espn import dias
    pasta = DADOS / "espn"
    pasta.mkdir(parents=True, exist_ok=True)
    # dias de jogo pelos CSV do football-data, mais o dia seguinte (jogo à noite pode cair no dia seguinte em UTC)
    for a in range(2001, 2026):
        arq = pasta / f"ned1_{a}.json"
        if arq.exists():
            continue
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        lista = set()
        with (DADOS / "football-data" / f"N1_{cod}.csv").open(encoding="utf-8-sig", errors="replace") as f:
            for x in csv.DictReader(f):
                if not x.get("Date"):
                    continue
                d, m, y = x["Date"].split("/")
                y = int(y) + (2000 if len(y) == 2 else 0)
                lista.add(date(y, int(m), int(d)))
        js = dias("ned.1", sorted(lista), CACHE / "espn-europa")
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"espn {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['lances'])} com lances", flush=True)



def antigo() -> None:
    """Era antiga (1888/89-1955/56, antes da Eredivisie): página da RSSSF de cada temporada (tablesn/ned1889.html ...
    ned1956.html, pelo ano final: fase final do título e ligas regionais, com matriz de resultados e tabela) e o artigo da
    Wikipédia em inglês ("1924–25 Netherlands Football League Championship"). Em data/coleta/ned-1/rsssf/ e wikipedia/."""
    from wikipedia import wikitexto
    for f in range(1889, 1957):
        nome = f"ned{f}.html"
        d = pegar(f"https://www.rsssf.org/tablesn/{nome}", DADOS / "rsssf" / nome, espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)
    pasta = DADOS / "wikipedia"
    for a in range(1888, 1956):
        t = f"{a}–{str(a + 1)[-2:] if (a + 1) % 100 else a + 1} Netherlands Football League Championship"
        arq = pasta / (t + ".wiki")
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt or '')}", flush=True)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:   # "ogol=1956-1990" passa a faixa de temporadas
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
