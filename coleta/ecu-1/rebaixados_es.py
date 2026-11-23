"""Rebaixados por ano pela Wikipédia em espanhol (página "Serie A de Ecuador", tabela "Ascensos y descensos", guardada em
data/coleta/ecu-1/wikipedia/es_serie_a.txt), coluna "Descendidos" (EC-004).

Cada ano vai para a edição do ano (2005: o Clausura, a última do ano). De 1970 a 1981 a queda era no meio do ano (fim da
1ª etapa) e fica na mesma edição, com observação (D-18 a).

Uso: rebaixados() -> {temporada: [clube como na página]}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "ecu-1" / "wikipedia" / "es_serie_a.txt"


def rebaixados() -> dict[str, list[str]]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("Ascensos y descensos")
    t = t[t.find("{|", i):t.find("\n|}", i)]
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    saida: dict[str, list[str]] = {}
    for r in t.split("\n|-")[1:]:
        cel = r.split("||")
        m = re.search(r"(\d{4})", cel[0]) if cel else None
        if not m or len(cel) < 3:
            continue
        ano = m.group(1)
        temp = "2005 Clausura" if ano == "2005" else ano
        nomes = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", cel[2])
        if nomes:
            saida[temp] = [n.strip() for n in nomes if not n.startswith("Archivo:")]
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in rebaixados().items():
        print(k, v)
