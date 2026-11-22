"""Lista de campeões da Wikipédia em inglês (página "FBF División Profesional", seção "List of champions"), segunda fonte
do campeão e do vice.

Página guardada em data/coleta/bol-1/wikipedia/en_campeoes.txt (baixar_wikipedia.py). Cada linha da tabela é um bloco entre
"|-": "| {{center|N}} || colspan=2| [[1950 Bolivian Primera División|1950]] || campeão || vice || técnico || artilheiro";
nos anos com dois torneios, o ano numa linha ("rowspan=2| 2003 || Apertura || ...") e só o torneio na seguinte
("| {{center|54}} || Clausura || ..."). As temporadas da Wikipédia viram as da RSSSF (edicoes.py):
"2005–06 Apertura" = "2005 Apertura", "2005–06 Clausura" = "2006 Apertura", "2006 Segundo Torneo" = "2006 Clausura",
"2011 Adecuación" = "2011/12 Adecuación", "2016–17 2017 Apertura" = "2016/17 Adecuación", "2020 Apertura" = "2020";
a segunda linha de 1957 (seção "Torneo Nacional Mixto") é "1957 Mixto".

Uso: campeoes() -> {temporada: campeão}; vices() -> {temporada: vice}
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "bol-1" / "wikipedia" / "en_campeoes.txt"
TROCA = {"2005/06 Apertura": "2005 Apertura", "2005/06 Clausura": "2006 Apertura", "2006 Segundo Torneo": "2006 Clausura",
         "2011 Adecuación": "2011/12 Adecuación", "2016/17 2016 Apertura": "2016/17 Apertura",
         "2016/17 2017 Apertura": "2016/17 Adecuación", "2016/17 2017 Clausura": "2016/17 Clausura", "2020 Apertura": "2020"}


def _texto(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\{\{flagicon[^{}]*\}\}|\{\{small\|[^{}]*\}\}|\{\{center\|([^{}]*)\}\}", lambda m: m.group(1) or "", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"^\s*(rowspan|colspan|style|bgcolor)=[^|]*\|", "", c)
    return c.strip(" '")


def _artilheiros(c: str) -> list[tuple[str, str, int]]:
    """Célula do artilheiro: "{{flagicon|ARG}} Juan Pinnola ([[Club Always Ready|Always Ready]]; 21 goals)<br> ..."."""
    saida = []
    for parte in re.split(r"<br\s*/?>", c):
        s = _texto(parte)
        if m := re.match(r"^(.+?)\s*\((.+?);\s*(\d+) goals?\)", s):
            saida.append((m.group(1).strip(), m.group(2).strip(), int(m.group(3))))
    return saida


_TOPS: dict[str, list[tuple[str, str, int]]] = {}


@lru_cache(maxsize=None)
def _linhas() -> dict[str, tuple[str, str]]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("==List of champions=="):t.find("==Titles by club==")]
    saida: dict[str, tuple[str, str]] = {}
    ano, secao = None, ""
    for bloco in t.split("\n|-")[1:]:
        if m := re.search(r'colspan="7"\s*\|(.+)', bloco):
            secao = m.group(1)
        brutas = [c for c in re.split(r"\|\||\n\|", bloco.replace("\n!", "\n|")) if _texto(c)]
        cel = [_texto(c) for c in brutas]
        if not cel or not re.fullmatch(r"\d+", cel[0]):
            continue   # cabeçalho de seção ou torneio sem campeão (2020 Clausura, 2022 Clausura)
        cel = cel[1:]
        if re.fullmatch(r"\d{4}(–\d{2})?", cel[0]):
            ano = cel[0].replace("–", "/")
            cel = cel[1:]
        if re.fullmatch(r"(\d{4} )?(Apertura|Clausura|Adecuación|Segundo Torneo)", cel[0]):
            temporada = f"{ano} {cel[0]}"
            cel = cel[1:]
        else:
            temporada = ano
        if temporada == "1957" and "Mixto" in secao:
            temporada = "1957 Mixto"
        temporada = TROCA.get(temporada, re.sub(r"^(\d{4})/(\d{2}) ", r"\1/\2 ", temporada))
        if len(cel) >= 2 and temporada:
            saida[temporada] = (cel[0], cel[1])
            _TOPS[temporada] = _artilheiros(brutas[-1]) if len(cel) >= 3 else []
    return saida


def artilheiros() -> dict[str, list[tuple[str, str, int]]]:
    """{temporada: [(jogador, clube como na página, gols)]}, da coluna "Leading goalscorer(s)"."""
    _linhas()
    return {t: v for t, v in _TOPS.items() if v}


def campeoes() -> dict[str, str]:
    return {t: c for t, (c, _) in _linhas().items()}


def vices() -> dict[str, str]:
    return {t: v for t, (_, v) in _linhas().items()}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from edicoes import EDICOES
    c = campeoes()
    print(len(c), "faltam:", [e.temporada for e in EDICOES if e.temporada not in c])
    print("sobram:", [k for k in c if k not in {e.temporada for e in EDICOES}])
