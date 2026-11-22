"""Leitor da fase final do campeonato holandês antigo (RSSSF, tablesn/ned1898.html ... ned1954.html; ned55 e ned56 para as
temporadas profissionais de 1954/55 e 1955/56).

Cada página tem a seção "Championship Playoff": os campeões regionais ("Champions 1e Klasse West: HVV"), a matriz de
resultados ("  1. HVV   --- 2-0", "---" na diagonal, colunas na ordem das linhas) e a tabela ("  1. HVV  2  2  0  0  4  5- 2":
posição, nome, jogos, V, E, D, pontos, gols pró- contra), às vezes com o jogo de desempate na nota ("[*] Playoff: Hengelo -
RFC  4-3.").

Uso como biblioteca: fase_final(arq) -> {"campeoes_regionais": [...], "tabela": [...], "matriz": {(m, v): (g, g)},
                                         "notas": [...], "texto": str}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

TABELA = re.compile(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s+(\d+)\s*-\s*(\d+)")
LINHA_MATRIZ = re.compile(r"^\s*(\d+)\.\s*(\S.{0,16}?)\s+((?:---|\d+[-*]\d+|\s|x|n/p|-)+)$")
CELULA = re.compile(r"---|\d+[-*]\d+|n/p|x")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def fase_final(arq: Path) -> dict | None:
    t = texto(arq)
    i = [m.start() for m in re.finditer(r"\n\s*Championship Playoff\s*\n", t)]
    if len(i) < 2 and not i:
        return None
    ini = i[1] if len(i) > 1 else i[0]   # a primeira ocorrência é o índice do topo da página
    fim = min([p for p in (t.find("\nDistrict", ini + 30), t.find("\nEerste Klasse", ini + 30), t.find("\nHoofdklasse", ini + 30))
               if p > 0] or [len(t)])
    sec = t[ini:fim]
    campeoes = re.findall(r"Champions?[^:\n]*:\s*([^\n]+)", sec)
    linhas = sec.split("\n")
    matriz_linhas, tabela = [], []
    for l in linhas:
        m = TABELA.match(l)
        if m and not re.search(r"---", l):
            pos, nome, j, v, e, d, p, gp, gc = m.groups()
            tabela.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "pontos": int(p), "gols_pro": int(gp), "gols_contra": int(gc)})
            continue
        m = LINHA_MATRIZ.match(l)
        if m and "---" in l:
            matriz_linhas.append((m.group(2).strip(), CELULA.findall(m.group(3))))
    nomes = [n for n, _ in matriz_linhas]
    matriz = {}
    for i_, (nm, cels) in enumerate(matriz_linhas):
        for k, c in enumerate(cels):
            g = re.match(r"^(\d+)([-*])(\d+)$", c)
            if g and k != i_ and k < len(nomes):
                matriz[(nm, nomes[k])] = (int(g.group(1)), int(g.group(3)), g.group(2) == "*")   # "*": vitória dada (5*0)
    notas = [l.strip() for l in linhas if re.match(r"^\s*(\[\*\]|NB|Note)", l)]
    return {"campeoes_regionais": campeoes, "tabela": tabela, "matriz": matriz, "notas": notas, "texto": sec}
