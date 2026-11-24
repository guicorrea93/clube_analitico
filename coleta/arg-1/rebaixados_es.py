"""Rebaixados por temporada pela Wikipédia em espanhol (AR-021): "Anexo:Movilidad interdivisional en el fútbol argentino",
seção "En el profesionalismo" da Primera División (guardada em data/coleta/arg-1/wikipedia/es_movilidad_interdivisional.txt),
coluna "Descensos" (quem caiu no fim da temporada; "No hubo" = ninguém). Só a era profissional (1931 em diante).

O rótulo da temporada vem como "PD 1949", "PD 2010-11", "M 1970", "N 1976 / M 1977" (a queda era no Metropolitano), "SL
2017-18" ou "LPF 2021". Devolve (ano ou "AAAA-AA", "M" se é o Metropolitano): o importar.py põe cada clube na última edição
dessa temporada em que ele jogou.

Uso: rebaixados() -> {(temporada, metropolitano): [(nome, alvo do link)]}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "arg-1" / "wikipedia" / "es_movilidad_interdivisional.txt"


def rebaixados() -> dict[tuple[str, bool], list[tuple[str, str]]]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("==== En el profesionalismo ====")
    t = t[i:t.find("==== Promociones ====", i)]
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    saida: dict[tuple[str, bool], list[tuple[str, str]]] = {}
    for linha in t.split("\n|-")[1:]:
        corpo = linha.split("\n", 1)[1] if "\n" in linha else ""
        cel = re.split(r"\|\||\n\|", corpo.lstrip("|"))
        rotulos = re.findall(r"\|\s*(PD|M|N|SL|LPF) (\d{4}(?:-\d{2})?)\]\]", cel[0]) if cel else []
        if not rotulos or len(cel) < 3:
            continue
        pref, temp = next(((p, a) for p, a in rotulos if p == "M"), rotulos[-1])
        nomes = [(rot or alvo, alvo) for alvo, rot in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cel[2])
                 if not re.match(r"(Copa|Campeonato|Torneo|Anexo|Archivo)\b", alvo)]   # link de competição na nota
        saida[(temp, pref == "M")] = nomes
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in rebaixados().items():
        print(k, [n for n, _ in v])
