"""Lista de campeões da Wikipédia em inglês (página "List of Peruvian football champions", seção "List of champions"),
segunda fonte do campeão e fonte do vice nos anos sem tabela (1912-1921).

Página guardada em data/coleta/per-1/wikipedia/en_campeoes.txt (wikitexto, baixado por baixar_wikipedia.py). Cada linha da
tabela: "| {{center|N}} || [[1926 Peruvian Primera División|1926]] || campeão || vice || 3º || ...". A Wikipédia numera
os títulos a partir de 1912: conta os da Liga Peruana de Football (1912-1921) como títulos nacionais.

Uso: campeoes() -> {temporada: campeão}; vices() -> {temporada: vice}
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "per-1" / "wikipedia" / "en_campeoes.txt"


def _texto(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\{\{small\|[^{}]*\}\}|\{\{Ref label[^{}]*\}\}", "", c)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", c)
    return (m.group(1) if m else re.sub(r"\{\{[^{}]*\}\}", "", c)).strip(" '")


@lru_cache(maxsize=None)
def _linhas() -> dict[str, tuple[str, str]]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("==List of champions=="):t.find("==Clubs==")]
    saida = {}
    for l in t.splitlines():
        cel = [c.strip() for c in l.lstrip("|").split("||")]
        if len(cel) < 4 or not (m := re.search(r"\|(\d{4})\]\]", cel[1])):
            continue
        if re.search(r"not played|no tournament", l, re.I):
            continue
        saida[m.group(1)] = (_texto(cel[2]), _texto(cel[3]))
    return saida


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
    print(len(c), [e.temporada for e in EDICOES if e.temporada not in c])
    print([k for k in c if k not in {e.temporada for e in EDICOES}])
    print({k: (c[k], vices()[k]) for k in list(c)[:12]})
