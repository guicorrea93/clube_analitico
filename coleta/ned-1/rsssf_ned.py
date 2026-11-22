"""Leitor das páginas da RSSSF holandesa no formato antigo (tablesn/ned57.html ... por volta de 2000/01).

Cada página traz a matriz de resultados da Eredivisie ("   Sparta         1-2  1-1 ... ***", linhas e colunas na mesma
ordem, "***" na diagonal) e a tabela final ("  1 Ajax          34  22- 5- 7  49   64- 40 ...": posição, nome, jogos,
V- E- D, pontos, gols pró- contra, e depois casa e fora). Páginas antigas trazem também a Eerste e a Tweede Divisie:
vale o primeiro bloco de cada tipo, que é o da Eredivisie.

As páginas novas ("  1.PSV (Eindhoven)   34 27  6  1  89-18  87") ficam com o leitor genérico `tabela_rsssf` do
importador.

Uso como biblioteca: ler(arq) -> {"tabela": [{posicao, nome, jogos, ...}], "matriz": {(mandante, visitante): (g, g)},
                                  "avisos": [...]}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

# o nome ocupa 14 colunas e às vezes encosta nos jogos ("A.D.O.Den Haag34   9- 7-18 ...")
TABELA = re.compile(r"^\s*(\d+)\s+(\S.*?)\s*(\d+)\s+(\d+)-\s*(\d+)-\s*(\d+)\s+(-?\d+)\s+(\d+)-\s*(\d+)")
# idem na matriz ("   R.B.C. Roosend.1-3  2-3 ...")
LINHA_MATRIZ = re.compile(r"^\s{1,4}(\S.{0,15}?)\s*((?:\*\*\*|\d+-\d+|-{1,3}|\s)+)$")
CELULA = re.compile(r"\*\*\*|\d+-\d+|-{1,3}")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def ler(arq: Path) -> dict:
    linhas = texto(arq).split("\n")
    tabela: list[dict] = []
    for l in linhas:
        m = TABELA.match(l)
        if m:
            pos, nome, j, v, e, d, p, gp, gc = m.groups()
            if tabela and int(pos) <= tabela[-1]["posicao"]:
                break   # começou outra tabela (Eerste Divisie)
            tabela.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "pontos": int(p), "gols_pro": int(gp), "gols_contra": int(gc)})
        elif tabela and not l.strip():
            break
    bloco: list[tuple[str, list[str], str]] = []
    for l in linhas:
        m = LINHA_MATRIZ.match(l)
        if m and ("***" in l or (bloco and re.search(r"\d+-\d+", m.group(2)))):
            bloco.append((m.group(1).strip(), CELULA.findall(m.group(2)), l.strip()))
        elif bloco:
            break   # vale o primeiro bloco (Eredivisie)
    matriz, avisos = {}, []
    nomes = [b[0] for b in bloco]
    for i, (nm, cels, l) in enumerate(bloco):
        if len(cels) != len(bloco):
            avisos.append(f"linha {i + 1} da matriz com {len(cels)} células ({len(bloco)} clubes): {l}")
            continue
        for k, c in enumerate(cels):
            g = re.match(r"^(\d+)-(\d+)$", c)
            if g and k != i:
                matriz[(nm, nomes[k])] = (int(g.group(1)), int(g.group(2)))
    return {"tabela": tabela, "matriz": matriz, "avisos": avisos}
