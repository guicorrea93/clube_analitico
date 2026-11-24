"""Baixa as fontes da 1ª divisão turca (tur-1), 1959 a 2025/26.

Fontes (cada uma numa pasta de data/coleta/tur-1/):
  ogol   ogol (zerozero): calendário de cada edição, base dos jogos (rodada oficial, placar e código de cada clube).
         Páginas em data/cache/ogol-tur-1/.
  esd    engsoccerdata (GitHub jalapic/engsoccerdata, GPL >= 2): 1ª divisão de 1994/95 em diante, só para conferência.
         Bruto em data/cache/engsoccerdata-europa/.
  fd     football-data.co.uk, T1.csv de 1994/95 a 2025/26: placar, hora, árbitro, estatísticas e cartões por time.
  rsssf  RSSSF: tabelas finais (turkhist.html), lista de campeões (turkchamp.html) e de artilheiros (turktops.html).
  wiki   Wikipédia em inglês: artigo de cada temporada (tabela final, punições), lista de campeões.
  espn   ESPN (liga tur.1): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

Uso: python coleta/tur-1/baixar.py ogol esd fd rsssf wiki espn
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

from edicoes import CACHE, DADOS, TEMPORADAS, temporada, wiki_titulo  # noqa: E402

FD = range(1994, 2026)


def esd() -> None:
    bruto = CACHE / "engsoccerdata-europa"
    pegar("https://raw.githubusercontent.com/jalapic/engsoccerdata/master/data-raw/turkey.csv", bruto / "turkey.csv")
    pasta = DADOS / "engsoccerdata"
    pasta.mkdir(parents=True, exist_ok=True)
    with (bruto / "turkey.csv").open(encoding="utf-8") as f, (pasta / "turkey_tier1.csv").open("w", encoding="utf-8", newline="") as g:
        r = csv.DictReader(f)
        w = csv.DictWriter(g, fieldnames=r.fieldnames)
        w.writeheader()
        n = 0
        for x in r:
            if x["tier"] == "1":
                w.writerow(x); n += 1
    print(f"engsoccerdata: {n} jogos da 1ª divisão")


def fd() -> None:
    for a in FD:
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        d = pegar(f"https://www.football-data.co.uk/mmz4281/{cod}/T1.csv", DADOS / "football-data" / f"T1_{cod}.csv", espera=1.5)
        print(f"football-data {cod}: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    urls = ["https://www.rsssf.org/tablest/turkhist.html", "https://www.rsssf.org/tablest/turkchamp.html",
            "https://www.rsssf.org/tablest/turktops.html"]
    for url in dict.fromkeys(urls):
        nome = url.rsplit("/", 1)[1]
        d = pegar(url, DADOS / "rsssf" / nome, espera=2.0)
        print(f"rsssf {nome}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    titulos = [wiki_titulo(a) for a in TEMPORADAS] + ["List of Turkish football champions"]
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
    # temporadas recentes: a tabela pode ficar num modelo à parte ("{{2024–25 Süper Lig table}}"); a 1ª em
    # "<título> (tabela).wiki", as outras em "(tabela 2)", ...
    for a in TEMPORADAS:
        t = wiki_titulo(a)
        if not (pasta / f"{t}.wiki").exists():
            continue
        modelos = re.findall(r"\{\{(\d{4}[–-]\d{2,4} (?:Süper Lig|1\.Lig|Turkish [A-Za-z ]+?)[A-Za-z' -]*? table)\}\}", (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        for i, mod in enumerate(dict.fromkeys(modelos), 1):
            arq = pasta / (f"{t} (tabela).wiki" if i == 1 else f"{t} (tabela {i}).wiki")
            if arq.exists():
                continue
            txt = wikitexto("en", f"Template:{mod}", espera=1.5)
            if txt:
                arq.write_text(txt, encoding="utf-8")
                print(f"wiki Template:{mod}: {len(txt)}", flush=True)


def ogol(faixa: str | None = None) -> None:
    """faixa "1958-1990": só essas temporadas (para rodar várias frentes em paralelo)."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-tur-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = {int(n[:4]): i for i, n in edicoes("campeonato-turco", cache)}
    (pasta / "edicoes.json").write_text(json.dumps({temporada(a): eds[a] for a in sorted(eds)}, indent=0), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    # 2026/27 (em andamento): só para saber quem caiu em 2025/26 (clubes da temporada seguinte)
    for a in sorted((a for a in TEMPORADAS + [TEMPORADAS[-1] + 1] if int(ini) <= a <= int(fim)), reverse=True):
        arq = pasta / f"tur1_{a}.json"
        if arq.exists():
            continue
        js = calendario(eds[a], a, cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


def espn() -> None:
    """Dias de jogo pelo football-data (a ESPN só responde um dia por vez), mais o dia seguinte."""
    from datetime import timedelta
    from espn import dias
    pasta = DADOS / "espn"
    pasta.mkdir(parents=True, exist_ok=True)
    for a in FD:
        arq = pasta / f"tur1_{a}.json"
        if arq.exists():
            continue
        lista = set()   # dias de jogo pelo football-data (independe do ogol, que demora a baixar)
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        arq_fd = DADOS / "football-data" / f"T1_{cod}.csv"
        if not arq_fd.exists():
            continue
        for x in csv.DictReader(arq_fd.open(encoding="utf-8-sig", errors="replace")):
            if not x.get("Date"):
                continue
            d_, m_, y_ = x["Date"].split("/")
            d = date(int(y_) + (2000 if len(y_) == 2 else 0), int(m_), int(d_))
            lista |= {d, d + timedelta(days=1)}
        js = dias("tur.1", sorted(lista), CACHE / "espn-europa")
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"espn {temporada(a)}: {len(js)} jogos, {sum(1 for j in js if j['lances'])} com lances", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:   # "ogol=1958-1990" passa a faixa de temporadas
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
