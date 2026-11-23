"""Rebaixados por ano pela Wikipédia em espanhol ("Anexo:Ascensos y descensos de la Categoría Primera A", guardado em
data/coleta/col-1/wikipedia/es_ascensos_descensos.txt), coluna "Descendido" (CO-007).

Cada ano vai para a última edição do ano no pacote: até 2001 a edição do ano ("1995/96", "1996/97" no calendário europeu);
de 2002 em diante, o Finalización. 1997: o Deportivo Pereira caiu no Torneo Adecuación (fora do pacote) e é marcado no
1996/97, com observação (D-18 b).

Uso: rebaixados() -> {temporada: [clube como na página]}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "col-1" / "wikipedia" / "es_ascensos_descensos.txt"


def _temporada(rot: str) -> str | None:
    if m := re.fullmatch(r"(\d{4})-(\d{2})", rot):
        return f"{m.group(1)}/{m.group(2)}"
    if not re.fullmatch(r"\d{4}", rot):
        return None
    a = int(rot)
    if a == 1997:
        return "1996/97"
    return f"{a} Finalización" if a >= 2002 else rot


def rebaixados() -> dict[str, list[str]]:
    t = ARQ.read_text(encoding="utf-8")
    saida: dict[str, list[str]] = {}
    for r in t.split("\n|-"):
        m = re.match(r"\s*\|\s*'''\[\[[^\]|]*\|(\d{4}(?:-\d{2})?)\]\]'''\s*\|\|(.*?)\|\|", r, re.S)
        if not m:
            continue
        temp = _temporada(m.group(1))
        nomes = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", m.group(2))
        if temp and nomes:
            saida.setdefault(temp, []).extend(n.strip() for n in nomes if not n.startswith("Archivo:"))
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in rebaixados().items():
        print(k, v)
