"""Artilheiros de 1900 a 1931 pela coluna "Goleador" da tabela "Títulos de liga por año" da Wikipédia em espanhol (página
"Primera División de Uruguay", guardada em data/coleta/uru-1/wikipedia/es_principal.txt). A urutops da RSSSF começa em
1932 (UY-018). A tabela segue a AUF: 1923 e 1924 são os campeonatos da AUF.

Uso: goleadores() -> {temporada: [(jogador, clube como na página, gols)]}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "uru-1" / "wikipedia" / "es_principal.txt"


def _limpa(s: str) -> str:
    s = re.sub(r"\{\{bandera\|[^{}]*\}\}|<ref[^>]*/>|<ref[^>]*>.*?</ref>|\[\[Archivo:[^\]]*\]\]", "", s)
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"^\s*align=\"?\w+\"?\s*\|", "", s)
    return re.sub(r"<[^>]+>|'''?", "", s).strip()


def goleadores(ate: int = 1931) -> dict[str, list[tuple[str, str, int]]]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("=== Títulos de liga por año"):]
    saida: dict[str, list[tuple[str, str, int]]] = {}
    for bloco in t.split("\n|-"):
        m = re.search(r"^\|\s*(?:align=center\|)?\s*\[\[[^\]|]*\|(\d{4})\]\]", bloco, re.M)
        if not m or int(m.group(1)) > ate:
            continue
        ano = m.group(1)
        temp = f"{ano} AUF" if ano in ("1923", "1924") else ano
        cel = [c for c in bloco.split("\n|") if re.search(r"\s-\s*\d{1,2}\s*(<small>)?\s*\(", c)]
        if not cel:
            continue
        lista = []
        for parte in re.split(r"<br\s*/?>", cel[0]):
            if mm := re.search(r"(.+?)\s+-\s+(\d{1,2})\s*(?:<small>)?\s*\((.+?)\)", parte):
                lista.append((_limpa(mm.group(1)), _limpa(mm.group(3)), int(mm.group(2))))
        if lista:
            saida[temp] = lista
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in goleadores().items():
        print(k, v)
