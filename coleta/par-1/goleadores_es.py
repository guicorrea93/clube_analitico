"""Artilheiros pela coluna "Goleador" da tabela "Títulos de Liga por año" da Wikipédia em espanhol (página "Primera División
de Paraguay", guardada em data/coleta/par-1/wikipedia/es_principal.txt). A paratops da RSSSF acaba em 2011 e a contagem dos
gols com autor deixa edições sem artilheiro (PY-018); a mesma coluna confere os números da paratops (PY-019).

Uso: goleadores() -> {temporada: [(jogador, clube como na página, gols)]} ("1999"; "2014 Apertura")
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "par-1" / "wikipedia" / "es_principal.txt"


def _limpa(s: str) -> str:
    s = re.sub(r"\{\{[Bb]andera\|[^{}]*\}\}|<ref[^>]*/>|<ref[^>]*>.*?</ref>|\[\[Archivo:[^\]]*\]\]", "", s)
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    return re.sub(r"<[^>]+>|'''?", "", s).strip(" |")


def goleadores() -> dict[str, list[tuple[str, str, int]]]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("Títulos de Liga por año")
    t = t[i:t.find("\n|}", i)]
    saida: dict[str, list[tuple[str, str, int]]] = {}
    ano = None
    for bloco in t.split("\n|-"):
        bloco = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", bloco, flags=re.S)
        # o ano vem só na 1ª linha do ano (rowspan): "'''2014'''" ou "'''[[Campeonato Paraguayo de Fútbol 1935|1935]]'''"
        if m := re.search(r"'''\s*(?:\[\[[^\]|]*\|)?(\d{4})(?:\]\])?\s*'''", bloco):
            ano = int(m.group(1))
        if ano is None:
            continue
        tor = re.search(r"\[\[Torneo (Apertura|Clausura) \d{4}", bloco)
        temp = f"{ano} {tor.group(1)}" if ano >= 2008 and tor else str(ano)
        lista = []
        for parte in re.split(r"<br\s*/?>", bloco):
            parte = re.sub(r"\{\{[Bb]andera\|[^{}]*\}\}", "", parte)
            parte = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", parte)   # links antes: "(Asunción)" no nome do clube
            if mm := re.search(r"([^|\n]+?)\s+-\s+(\d{1,2})\s*(?:<small>)?\s*\((.+)\)\s*(?:</small>)?", parte):
                jog = _limpa(mm.group(1))
                if jog and not jog.isdigit():
                    lista.append((jog, _limpa(mm.group(3)), int(mm.group(2))))
        if lista:
            saida[temp] = lista
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in goleadores().items():
        print(k, v)
