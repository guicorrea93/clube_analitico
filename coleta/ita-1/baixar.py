"""Baixa as fontes da 1ª divisão italiana (ita-1), 1929/30 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/ita-1/):
  esd    engsoccerdata (GitHub jalapic/engsoccerdata, GPL >= 2): todos os jogos da 1ª divisão, 1929/30-2024/25.
         Bruto em data/cache/engsoccerdata-europa/.
  fd     football-data.co.uk, I1.csv de 1993/94 a 2025/26: placar, hora, árbitro, estatísticas e cartões por time.
  rsssf  RSSSF (Maurizio Mariani e outros): uma página por temporada, com as rodadas e a tabela final.
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final, punições), lista de campeões e Capocannoniere.
  ogol   ogol: calendário de cada edição (rodada oficial e código de cada clube). Páginas em data/cache/ogol-ita-1/.
  espn   ESPN (liga ita.1), 2001/02 em diante: hora, estádio, público, gols e cartões com minuto.

Uso: python coleta/ita-1/baixar.py esd fd rsssf wiki ogol espn
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
    pegar("https://raw.githubusercontent.com/jalapic/engsoccerdata/master/data-raw/italy.csv", bruto / "italy.csv")
    pasta = DADOS / "engsoccerdata"
    pasta.mkdir(parents=True, exist_ok=True)
    with (bruto / "italy.csv").open(encoding="utf-8") as f, (pasta / "italy_tier1.csv").open("w", encoding="utf-8", newline="") as g:
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
        d = pegar(f"https://www.football-data.co.uk/mmz4281/{cod}/I1.csv", DADOS / "football-data" / f"I1_{cod}.csv", espera=1.5)
        print(f"football-data {cod}: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    for url in dict.fromkeys(rsssf_url(a) for a in TEMPORADAS):
        nome = url.rsplit("/", 1)[1]
        d = pegar(url, DADOS / "rsssf" / nome, espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    titulos = [wiki_titulo(a) for a in TEMPORADAS] + ["List of Italian football champions", "Capocannoniere"]
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
    # temporadas recentes: a tabela fica num modelo à parte ("{{2024–25 Serie A table}}"), guardado como "<título> (tabela).wiki"
    for a in TEMPORADAS:
        t = wiki_titulo(a)
        arq = pasta / f"{t} (tabela).wiki"
        if arq.exists() or not (pasta / f"{t}.wiki").exists():
            continue
        m = re.search(r"\{\{(\d{4}[–-]\d{2} Serie A table)\}\}", (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        if not m:   # o nome do modelo pode vir com hífen ("{{2022-23 Serie A table}}")
            continue
        txt = wikitexto("en", f"Template:{m.group(1)}", espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
            print(f"wiki Template:{t} table: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1929-1960": só essas temporadas (para rodar várias frentes em paralelo)."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-ita-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = {int(n[:4]): i for i, n in edicoes("campeonato-italiano", cache)}
    (pasta / "edicoes.json").write_text(json.dumps({temporada(a): eds[a] for a in sorted(eds)}, indent=0), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    for a in sorted((a for a in TEMPORADAS if int(ini) <= a <= int(fim)), reverse=True):
        arq = pasta / f"ita1_{a}.json"
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
        arq = pasta / f"ita1_{a}.json"
        if arq.exists():
            continue
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        lista = set()
        with (DADOS / "football-data" / f"I1_{cod}.csv").open(encoding="utf-8-sig", errors="replace") as f:
            for x in csv.DictReader(f):
                if not x.get("Date"):
                    continue
                d, m, y = x["Date"].split("/")
                y = int(y) + (2000 if len(y) == 2 else 0)
                lista.add(date(y, int(m), int(d)))
        js = dias("ita.1", sorted(lista), CACHE / "espn-europa")
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"espn {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['lances'])} com lances", flush=True)


def wikiit() -> None:
    """Wikipédia em italiano: artigo de cada temporada ("Serie A 1963-1964"; 1945/46: "Divisione Nazionale 1945-1946"),
    para os jogos-desempate (seção "Spareggi"). Em data/coleta/ita-1/wikipedia-it/."""
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia-it"
    pasta.mkdir(parents=True, exist_ok=True)
    for a in TEMPORADAS:
        t = f"{'Divisione Nazionale' if a == 1945 else 'Serie A'} {a}-{a + 1}"
        arq = pasta / f"{t}.wiki"
        if arq.exists():
            continue
        txt = wikitexto("it", t, espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
        print(f"wiki it {t}: {len(txt or '')}", flush=True)


ARTIGOS_ANTIGOS = [
    "Campionato Italiano di Football 1898", "Campionato Italiano di Football 1899", "Campionato Italiano di Football 1900",
    "Campionato Italiano di Football 1901", "Campionato Italiano di Football 1902", "Campionato Italiano di Football 1903",
    "Prima Categoria 1904", "Prima Categoria 1905", "Prima Categoria 1906", "Prima Categoria 1907",
    "Campionato Italiano di Prima Categoria 1908", "Campionato Federale di Prima Categoria 1908",
    "Campionato Federale di Prima Categoria 1909", "Campionato Italiano di Prima Categoria 1909",
    "Prima Categoria 1909-1910", "Prima Categoria 1910-1911", "Prima Categoria 1911-1912", "Prima Categoria 1912-1913",
    "Prima Categoria 1913-1914", "Prima Categoria 1914-1915", "Prima Categoria 1919-1920", "Prima Categoria 1920-1921",
    "Prima Categoria 1921-1922", "Prima Divisione 1921-1922", "Prima Divisione 1922-1923", "Prima Divisione 1923-1924",
    "Prima Divisione 1924-1925", "Prima Divisione 1925-1926", "Divisione Nazionale 1926-1927",
    "Divisione Nazionale 1927-1928", "Divisione Nazionale 1928-1929", "Albo d'oro del campionato italiano di calcio",
]


def antigo() -> None:
    """Era antiga (1898 a 1928/29, IT-017): artigos da Wikipédia em italiano (classificações, "Tabellone" e "Calendario"
    de cada grupo) em data/coleta/ita-1/wikipedia-it-antigo/; RSSSF (italhist98-25.html, ital24.html ... ital29.html,
    italchamp.html) em data/coleta/ita-1/rsssf-antigo/."""
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia-it-antigo"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in ARTIGOS_ANTIGOS:
        arq = pasta / f"{t.replace(chr(39), '_')}.wiki"
        if arq.exists():
            continue
        txt = wikitexto("it", t, espera=1.5)
        if txt:
            arq.write_text(txt, encoding="utf-8")
        print(f"wiki it {t}: {len(txt or '')}", flush=True)
    for nome in ["italhist98-25", "ital24", "ital25", "ital26", "ital27", "ital28", "ital29", "italchamp"]:
        d = pegar(f"https://www.rsssf.org/tablesi/{nome}.html", DADOS / "rsssf-antigo" / f"{nome}.html", espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:   # "ogol=1929-1960" passa a faixa de temporadas
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
