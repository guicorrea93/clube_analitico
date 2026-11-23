"""Autores dos gols na ficha de um jogo do ogol (https://www.ogol.com.br/jogo.php?id=N), para os jogos em que a ESPN falta ou
não fecha com o placar (revisão DE-010).

No cabeçalho da ficha, "match-header-scorers right" traz os gols do mandante e "match-header-scorers left" os do visitante
(o gol contra fica no lado que ganhou o gol, marcado "(g.c.)"; pênalti, "(g.p.)"): "<a ...>Claudio Pizarro</a> <span
class="time"> 3'</span>".

Uso como biblioteca: gols(html) -> [(lado "m"/"v", jogador, minuto, acréscimo, tipo)]
"""
from __future__ import annotations

import html
import re


def gols(texto: str) -> list[tuple]:
    res = []
    for classe, lado in (("right", "m"), ("left", "v")):
        m = re.search(rf'<div class="match-header-scorers {classe}">(.*?)</div>', texto, re.S)
        if not m:
            continue
        for nome, tempo in re.findall(r'<a [^>]*>([^<]+)</a>\s*<span class="time">([^<]*)</span>', m.group(1)):
            for t in re.split(r",\s*", tempo.strip()):   # o mesmo jogador com mais de um gol: "12', 45'"
                mm = re.match(r"(\d+)(?:\+(\d+))?'?\s*(\(.*?\))?", t.strip())
                if not mm:
                    continue
                marca = (mm.group(3) or "").lower()
                tipo = "contra" if "g.c" in marca else "penalti" if "g.p" in marca or "pen" in marca else "normal"
                res.append((lado, html.unescape(nome).strip(), int(mm.group(1)), int(mm.group(2)) if mm.group(2) else None, tipo))
    return res
