"""Baixa as fontes do campeonato norueguês (nor-1), 1937/38 a 2025.

Fontes (cada uma numa pasta de data/coleta/nor-1/):
  ogol     ogol (zerozero): calendário de cada edição desde 1961/62 (antes o ogol só tem o campeão), base dos jogos.
           Páginas em data/cache/ogol-nor-1/. Inclui 2026 (para saber quem caiu em 2025).
  fd       football-data.co.uk, NOR.csv ("new"), desde 2012: placar e hora.
  rsssf    RSSSF: campeões (noochamp.html), artilheiros (nootops.html) e a página de cada temporada que existir.
  wiki     Wikipédia em inglês: artigo de cada temporada (tabelas, matriz, fichas), com os modelos.
  wiki_no  Wikipédia em norueguês: a Norgesserien (1937/38, 1938/39, 1947/48), com os modelos das tabelas dos grupos;
           traz a matriz de alguns grupos.
  espn     ESPN (liga nor.1): hora, estádio, público, gols e cartões, nas temporadas que ela cobre (dias de jogo pelo
           ogol). JSON bruto por dia em data/cache/espn-europa/nor.1/.

Uso: python coleta/nor-1/baixar.py ogol fd rsssf wiki wiki_no espn
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

from edicoes import CACHE, DADOS, NORGESSERIEN, OGOL_DESDE, TEMPORADAS, rsssf_urls, wiki_no_titulo, wiki_titulo  # noqa: E402


def fd() -> None:
    d = pegar("https://www.football-data.co.uk/new/NOR.csv", DADOS / "football-data" / "NOR.csv", espera=1.5)
    print(f"football-data NOR: {len((d or b'').splitlines()) - 1} linhas", flush=True)


def rsssf() -> None:
    for n in ("noochamp", "nootops"):
        d = pegar(f"https://www.rsssf.org/tablesn/{n}.html", DADOS / "rsssf" / f"{n}.html", espera=2.0)
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


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in TEMPORADAS:
        titulo = wiki_titulo(t)
        arq = pasta / f"{titulo}.wiki"
        if not arq.exists():
            txt = wikitexto("en", titulo, espera=2.0)
            if txt is None:
                print(f"wiki: não achei '{titulo}'", flush=True)
                continue
            arq.write_text(txt, encoding="utf-8")
            print(f"wiki {titulo}: {len(txt)}", flush=True)
        _modelos(pasta, "en", titulo, r"\{\{(\d{4}(?:[–-]\d{2,4})? [A-Za-z' .-]+? (?:table|results))\}\}")


def wiki_no() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia-no"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in NORGESSERIEN:
        titulo = wiki_no_titulo(t)
        arq = pasta / f"{titulo}.wiki"
        if not arq.exists():
            txt = wikitexto("no", titulo, espera=2.0)
            if txt is None:
                print(f"wiki no: não achei '{titulo}'", flush=True)
                continue
            arq.write_text(txt, encoding="utf-8")
            print(f"wiki no {titulo}: {len(txt)}", flush=True)
        _modelos(pasta, "no", titulo, r"\{\{(Norgesserien \d{4}-\d{2} [^{}|]*?tabell)\}\}")


def ogol(faixa: str | None = None) -> None:
    """faixa "1961-1990": só as temporadas que começam nesses anos."""
    from ogol import calendario, edicoes
    cache = CACHE / "ogol-nor-1"
    pasta = DADOS / "ogol"
    pasta.mkdir(parents=True, exist_ok=True)
    eds = dict((n, i) for i, n in edicoes("liga-norueguesa", cache))
    (pasta / "edicoes.json").write_text(json.dumps(eds, indent=0, ensure_ascii=False), encoding="utf-8")
    ini, _, fim = (faixa or "0-9999").partition("-")
    alvo = [t for t in TEMPORADAS if t >= OGOL_DESDE or "/" not in t] + ["2026"]
    for t in sorted((t for t in alvo if int(ini) <= int(t[:4]) <= int(fim)), reverse=True):
        arq = pasta / f"nor1_{t.replace('/', '-')}.json"
        if arq.exists():
            continue
        js = calendario(eds[t], int(t[:4]), cache)
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ogol {t}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada", flush=True)


def espn() -> None:
    """Dias de jogo pelo ogol (a ESPN só responde um dia por vez), mais o dia seguinte; de 2003 a 2025."""
    from espn import dias
    pasta = DADOS / "espn"
    pasta.mkdir(parents=True, exist_ok=True)
    for a in range(2003, 2026):
        arq = pasta / f"nor1_{a}.json"
        og = DADOS / "ogol" / f"nor1_{a}.json"
        if arq.exists() or not og.exists():
            continue
        lista = set()
        for j in json.loads(og.read_text(encoding="utf-8")):
            if j["data"]:
                d = date.fromisoformat(j["data"])
                lista |= {d, d + timedelta(days=1)}
        js = dias("nor.1", sorted(lista), CACHE / "espn-europa")
        arq.write_text(json.dumps(js, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"espn {a}: {len(js)} jogos, {sum(1 for j in js if j['lances'])} com lances", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:
        nome, _, arg = nome.partition("=")
        globals()[nome](*([arg] if arg else []))
