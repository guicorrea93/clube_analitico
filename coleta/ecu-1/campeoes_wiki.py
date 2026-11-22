"""Lista de campeões da Wikipédia em inglês (página "LigaPro Serie A", seção "Champions by year"), segunda fonte do campeão e
do vice.

Página guardada em data/coleta/ecu-1/wikipedia/en_campeoes.txt (wikitexto, baixado por baixar_wikipedia.py). Cada linha da
tabela é um bloco entre "|-": "| {{center|N}}", "|colspan=2|[[1957 Campeonato Ecuatoriano de Fútbol|1957]]" (em 2005, o ano numa
linha e "Apertura"/"Clausura" na seguinte), depois campeão, vice, 3º e artilheiro, uma célula por linha.

Uso: campeoes() -> {temporada: campeão}; vices() -> {temporada: vice}
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "ecu-1" / "wikipedia" / "en_campeoes.txt"


def _texto(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\{\{small\|[^{}]*\}\}|\{\{Ref label[^{}]*\}\}|\{\{flagicon[^{}]*\}\}", "", c)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", c)
    return (m.group(1) if m else re.sub(r"\{\{[^{}]*\}\}", "", c)).strip(" '|")


@lru_cache(maxsize=None)
def _linhas() -> dict[str, tuple[str, str]]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("==Champions by year=="):t.find("==Titles by club==")]
    saida = {}
    ano = None
    for bloco in t.split("\n|-")[1:]:
        cel = [l.strip() for l in bloco.splitlines()[1:] if l.strip().startswith("|")]
        if not cel or re.search(r"No championship", bloco, re.I):
            continue
        k = 1   # a 1ª célula é o número da edição
        if m := re.search(r"\|(\d{4})\]\]", cel[k]):
            ano = m.group(1)
            k += 1
        if m := re.search(r"#(Apertura|Clausura)\|", cel[k]):
            temporada = f"{ano} {m.group(1)}"
            k += 1
        else:
            temporada = ano
        if temporada and len(cel) > k + 1:
            saida[temporada] = (_texto(cel[k]), _texto(cel[k + 1]))
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
    print({k: (c[k], vices()[k]) for k in list(c)[:8]}, {k: (c[k], vices()[k]) for k in list(c)[-4:]})
