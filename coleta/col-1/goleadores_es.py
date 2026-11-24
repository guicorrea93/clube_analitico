"""Artilheiros pela tabela "Títulos por temporada" da Wikipédia em espanhol (página "Categoría Primera A", guardada em
data/coleta/col-1/wikipedia/es_primera_a.txt): colunas goleador e gols (CO-017). A coltops da RSSSF acaba em 2007; de 2008 em
diante a contagem dos gols com autor falha em várias edições. A tabela não traz o clube do goleador: o importar.py o tira dos
gols com autor da edição.

Uso: goleadores(desde=2008) -> {temporada: ([jogador, ...], gols)} ("2012 Apertura", "2012 Finalización")
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "col-1" / "wikipedia" / "es_primera_a.txt"


def _celulas(bloco: str) -> list[str]:
    return [l[1:].strip() for l in bloco.split("\n") if l.startswith("|") and not l.startswith(("|-", "|}"))]


def goleadores(desde: int = 2008) -> dict[str, tuple[list[str], int]]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("=== Títulos por temporada ===")
    t = t[i:t.find("\n== Palmarés", i)]
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    saida: dict[str, tuple[list[str], int]] = {}
    for bloco in t.split("\n|-")[1:]:
        cel = _celulas(bloco)
        if len(cel) < 8:
            continue
        m = re.search(r"\[\[Torneo (Apertura|Finalización) (\d{4})", cel[0])   # o link diz o torneio (2020 vem só "2020")
        if not m or int(m.group(2)) < desde:
            continue
        temp = f"{m.group(2)} {m.group(1)}"
        nomes = [rot or alvo for alvo, rot in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cel[6])]
        gols = re.search(r"\d+", cel[7])
        if nomes and gols:
            saida[temp] = ([re.sub(r"\s*\(.*?\)$", "", n).strip() for n in nomes], int(gols.group(0)))
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in goleadores().items():
        print(k, v)
