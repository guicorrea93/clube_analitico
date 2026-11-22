"""Leitor das tabelas finais da RSSSF escocesa de 1890/91 a 1998/99 (tabless/scothist.html).

Cada temporada começa com um título ("Scottish League 1890/91", "Scottish League Division One 1935/36", "Scottish League
'A' Division 1946/47", "Scottish League Premier Division 1975/76", "Scottish Premier League 1998/99") e traz só a tabela
da 1ª divisão, com casa e fora separados:

     1. Rangers              36 15  2  1 38 12  8  6  4 22 12  54 +36

(posição, nome, jogos, V E D GP GC em casa, V E D GP GC fora, pontos e, às vezes, saldo). Clubes empatados vêm sem número
de posição: herdam a do anterior.

Uso como biblioteca: ler(arq) -> {ano_inicio: [{posicao, nome, jogos, vitorias, empates, derrotas, gols_pro, gols_contra,
                                              pontos}]}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

TITULO = re.compile(r"^\s*Scottish (?:League|Premier League)[^\n]*?(\d{4})/\d{2}\s*$")
LINHA = re.compile(r"^\s*(\d+\.)?\s+(\S.*?)\s+(\d+)" + r"\s+(\d+)" * 10 + r"\s+(-?\d+)\b")


def texto(arq: Path) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")
    # erros de leitura óptica na própria RSSSF, nos números das tabelas: "3o" e "lo" (30, 10), "l8" (18), "i" (1), "o" (0),
    # "Z," (2). Só pedaços inteiros feitos desses caracteres, que não aparecem em nome de clube
    trad = str.maketrans({"l": "1", "i": "1", "o": "0", "O": "0", "Z": "2", ",": ""})
    return re.sub(r"(?<= )(?=[0-9lioOZ,]*[lioOZ,])[0-9lioOZ,]{1,3}(?= )", lambda m: m.group(0).translate(trad), t)


def ler(arq: Path) -> dict[int, list[dict]]:
    res: dict[int, list[dict]] = {}
    ano, pos = None, 0
    for l in texto(arq).split("\n"):
        m = TITULO.match(l)
        if m:
            ano, pos = int(m.group(1)), 0
            res.setdefault(ano, [])
            continue
        m = LINHA.match(l)
        if ano is None or not m:
            continue
        g = [int(x) for x in m.groups()[2:]]
        j, hv, he, hd, hgp, hgc, av, ae, ad, agp, agc, p = g
        # a linha vale mesmo que V-E-D não somem os jogos (erro de digitação da RSSSF, como o Queen of the South de 1937/38):
        # a conferência com os jogos aponta
        if m.group(1):
            pos = int(m.group(1)[:-1])
        res[ano].append({"posicao": pos, "nome": m.group(2).strip(), "jogos": j, "vitorias": hv + av, "empates": he + ae,
                         "derrotas": hd + ad, "gols_pro": hgp + agp, "gols_contra": hgc + agc, "pontos": p})
    return res
