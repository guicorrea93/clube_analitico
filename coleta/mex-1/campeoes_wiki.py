"""Lista de campeões da Wikipédia em inglês ("List of Mexican football champions", seção "Liga MX champions", 1943/44 em
diante), segunda fonte do campeão e do vice.

Página guardada em data/coleta/mex-1/wikipedia/en_campeoes.txt (baixar_wikipedia.py). Cada linha da tabela é um bloco entre
"|-": "|7||[[1949–50 Mexican Primera División season|1949–50]]||'''[[C.D. Veracruz|Veracruz]]'''||resultado||vice||...".
O campeão é a célula em negrito; o vice, a primeira célula depois dele que não é resultado (a coluna do resultado às vezes
falta, por causa do "rowspan"). Os rótulos viram os nomes das edições: "1949–50" -> "1949/50", "Mex–1970" -> "1970 México 70",
"Prode–1985" -> "1985 Prode 85", "Mex–1986" -> "1986 México 86", "Inv–1996" -> "1996 Invierno", "Ver–1997" -> "1997 Verano",
"Ape–2002" -> "2002 Apertura", "Cla–2003" -> "2003 Clausura", "Bic–2010" -> "2010 Clausura", "Guard–2020" -> "2020 Apertura",
"Guard–2021" -> "2021 Clausura".

Uso: campeoes() -> {temporada: campeão}; vices() -> {temporada: vice}; artilheiros() -> {} (a lista não tem)
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "mex-1" / "wikipedia" / "en_campeoes.txt"
_TORNEIO = {"Inv": "Invierno", "Ver": "Verano", "Ape": "Apertura", "Cla": "Clausura", "Bic": "Clausura"}


def _texto(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\{\{efn[^{}]*\}\}|\{\{flagicon[^{}]*\}\}|\{\{small\|[^{}]*\}\}", "", c)
    c = re.sub(r"\{\{nowrap\|([^{}]*)\}\}", r"\1", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"^\s*(rowspan|colspan|style)=[^|]*\|", "", c)
    return c.replace("'''", "").strip(" '")


def _temporada(rot: str) -> str | None:
    rot = _texto(rot)
    if m := re.fullmatch(r"(\d{4})–(\d{2})", rot):
        return f"{m.group(1)}/{m.group(2)}"
    if m := re.fullmatch(r"(Mex|Prode)–(\d{4})", rot):
        return {"1970": "1970 México 70", "1985": "1985 Prode 85", "1986": "1986 México 86"}[m.group(2)]
    if m := re.fullmatch(r"(Inv|Ver|Ape|Cla|Bic)–(\d{4})", rot):
        return f"{m.group(2)} {_TORNEIO[m.group(1)]}"
    if m := re.fullmatch(r"Guard–(\d{4})", rot):
        return f"{m.group(1)} {'Apertura' if m.group(1) == '2020' else 'Clausura'}"
    return None


def _resultado(c: str) -> bool:
    s = _texto(c)
    return not s or bool(re.search(r"\d\s*–\s*\d|Round-robin|Final group|^\(|t\.b\.", s)) or "small|" in c and not re.search(r"\[\[", c)


@lru_cache(maxsize=None)
def _linhas() -> dict[str, tuple[str, str]]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("==Liga MX champions=="):t.find("==Ascenso MX champions==")]
    saida: dict[str, tuple[str, str]] = {}
    for bloco in t.split("\n|-")[1:]:
        m = re.match(r"\s*\|\s*\d+\s*\|\|(.*)", bloco, re.S)
        if not m:
            continue
        cel = re.split(r"\|\|", m.group(1).replace("\n", " "))
        temp = _temporada(cel[0])
        if not temp:
            continue
        k = next((i for i, c in enumerate(cel) if "'''" in c), None)
        if k is None:   # torneio sem campeão ("Unfinished tournament", Clausura 2020)
            continue
        vice = next((_texto(c) for c in cel[k + 1:] if not _resultado(c)), "")
        saida[temp] = (_texto(cel[k]), re.sub(r"\s*(<br>|\|\}).*$", "", vice))   # (fim da tabela colado no último vice)
    return saida


def artilheiros() -> dict[str, list[tuple[str, str, int]]]:
    return {}


def campeoes() -> dict[str, str]:
    return {t: c for t, (c, _) in _linhas().items()}


def vices() -> dict[str, str]:
    return {t: v for t, (_, v) in _linhas().items()}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from edicoes import EDICOES
    c, v = campeoes(), vices()
    print(len(c), "faltam:", [e.temporada for e in EDICOES if e.temporada not in c and e.ano_inicio >= 1943])
    print("sobram:", [k for k in c if k not in {e.temporada for e in EDICOES}])
    for k in ["1943/44", "1945/46", "1970 México 70", "1985 Prode 85", "1996 Invierno", "2010 Clausura", "2020 Apertura", "2026 Clausura"]:
        print(k, c.get(k), "|", v.get(k))
