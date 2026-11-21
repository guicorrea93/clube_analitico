"""Baixa as fontes da 1ª divisão inglesa (eng-1), 1888/89 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/eng-1/):
  esd    engsoccerdata (GitHub jalapic/engsoccerdata, GPL >= 2): todos os jogos da 1ª divisão, 1888-2024
         (faltam 2022/23 e 2025/26); punições de pontos (deductions.csv). Bruto em data/cache/engsoccerdata-europa/.
  fd     football-data.co.uk, E0.csv de 1993/94 a 2025/26: placar, hora, árbitro, estatísticas e cartões por time.
  rsssf  RSSSF (engpaul/FLA/<temporada>.html, Paul Felton e Barry Spencer): tabela final publicada, 1888/89-2006/07.
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final, punições, artilheiros) e lista de campeões.
  ogol   ogol: calendário de cada edição (rodada oficial e código de cada clube). Páginas em data/cache/ogol-eng-1/.
  espn   ESPN (liga eng.1), 2001/02 em diante: hora, estádio, público, gols e cartões com minuto.

Uso: python coleta/eng-1/baixar.py esd fd rsssf wiki ogol espn
"""
from __future__ import annotations

import csv
import json
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import CACHE, DADOS, GUERRA, TEMPORADAS, temporada, wiki_titulo  # noqa: E402


def esd() -> None:
    bruto = CACHE / "engsoccerdata-europa"
    for f in ("england.csv", "deductions.csv", "teamnames.csv"):
        pegar(f"https://raw.githubusercontent.com/jalapic/engsoccerdata/master/data-raw/{f}", bruto / f)
    pasta = DADOS / "engsoccerdata"
    pasta.mkdir(parents=True, exist_ok=True)
    with (bruto / "england.csv").open(encoding="utf-8") as f, (pasta / "england_tier1.csv").open("w", encoding="utf-8", newline="") as g:
        r = csv.DictReader(f)
        w = csv.DictWriter(g, fieldnames=r.fieldnames)
        w.writeheader()
        n = 0
        for x in r:
            if x["tier"] == "1":
                w.writerow(x); n += 1
    with (bruto / "deductions.csv").open(encoding="utf-8") as f, (pasta / "deductions.csv").open("w", encoding="utf-8", newline="") as g:
        g.write(f.read())
    print(f"engsoccerdata: {n} jogos da 1ª divisão")


def fd() -> None:
    for a in range(1993, 2026):
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        d = pegar(f"https://www.football-data.co.uk/mmz4281/{cod}/E0.csv", DADOS / "football-data" / f"E0_{cod}.csv", espera=1.5)
        print(f"football-data {cod}: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    for a in range(1888, 2007):
        if a in GUERRA:
            continue
        t = f"{a}-{str(a + 1)[-2:]}"
        d = pegar(f"https://www.rsssf.org/engpaul/FLA/{t}.html", DADOS / "rsssf" / f"{t}.html", espera=2.0)
        print(f"rsssf {t}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    titulos = [wiki_titulo(a) for a in TEMPORADAS] + [
        "List of English football champions", "List of English football first tier top scorers"]
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


def ogol(faixa: str | None = None) -> None:
    """faixa "1888-1914": só essas temporadas (para rodar várias frentes em paralelo)."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-eng-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = {int(n[:4]): i for i, n in edicoes("premier-league", cache)}
    (pasta / "edicoes.json").write_text(json.dumps({temporada(a): eds[a] for a in sorted(eds)}, indent=0), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    for a in sorted((a for a in TEMPORADAS if int(ini) <= a <= int(fim)), reverse=True):
        arq = pasta / f"eng1_{a}.json"
        if arq.exists():
            continue
        js = calendario(eds[a], a, cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


def espn() -> None:
    from espn import dias
    pasta = DADOS / "espn"
    pasta.mkdir(parents=True, exist_ok=True)
    # dias de jogo pelos CSV do football-data (todas as temporadas da ESPN estão lá), mais o dia seguinte
    # (jogo à noite pode cair no dia seguinte no fuso da ESPN)
    for a in range(2001, 2026):
        arq = pasta / f"eng1_{a}.json"
        if arq.exists():
            continue
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        lista = set()
        with (DADOS / "football-data" / f"E0_{cod}.csv").open(encoding="utf-8-sig", errors="replace") as f:
            for x in csv.DictReader(f):
                if not x.get("Date"):
                    continue
                d, m, y = x["Date"].split("/")
                y = int(y) + (2000 if len(y) == 2 else 0)
                lista.add(date(y, int(m), int(d)))
        js = dias("eng.1", sorted(lista), CACHE / "espn-europa")
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"espn {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['lances'])} com lances", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:   # "ogol=1888-1914" passa a faixa de temporadas
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
