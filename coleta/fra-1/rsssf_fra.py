"""Leitor da RSSSF francesa (tablesf/franfullhist.html): matrizes de resultados e tabelas finais de 1932/33 a 1997/98.

Cada temporada começa com " 1932-1933". Dentro dela, uma ou mais matrizes (1932/33 tem os grupos A e B) com o nome
do clube em maiúsculas no começo da linha, e as tabelas finais ("  1 OL. LILLOIS   18  14- 0- 4  28   41- 23 ...":
posição, nome, jogos, V- E- D, pontos, gols pró- contra, e depois casa e fora).

Uso como biblioteca: ler(arq) -> {1932: {"tabelas": [[{...}, ...], ...], "matrizes": [{(mandante, visitante): (g, g)}],
                                          "notas": [...]}}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

# o nome ocupa 14 colunas e às vezes encosta nos jogos ("PARIS ST.GERM.38  13-12-13")
TABELA = re.compile(r"^\s*(\d+)\s+(\S.*?)\s*(\d+)\s+(\d+)-\s*(\d+)-\s*(\d+)\s+(-?\d+)\s+(\d+)-\s*(\d+)")
CELULA = r"(?:\*\*\*|\d+-\d+|---|[A-Za-z]{1,4}|\s{3})"


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def _matrizes(linhas: list[str]) -> list[dict]:
    res, atual, nomes, celulas = [], None, [], []

    def fecha():
        if nomes:
            m = {}
            for i, (nm, cs) in enumerate(zip(nomes, celulas)):
                for j, c in enumerate(cs):
                    g = re.match(r"^(\d+)-(\d+)$", c)
                    if g and j < len(nomes) and j != i:
                        m[(nm, nomes[j])] = (int(g.group(1)), int(g.group(2)))
            res.append(m)
    for l in linhas:
        m = re.match(r"^\s(\S.{13,15}?)\s{1,}((?:\*\*\*|\d+-\d+|-|\s)+)$", l)
        if m and "***" in l or (m and nomes and re.search(r"\d+-\d+", m.group(2))):
            nomes.append(m.group(1).strip())
            celulas.append(re.findall(r"\*\*\*|\d+-\d+|(?<=\s)-(?=\s|$)", m.group(2)))
        elif nomes and not l.strip():
            fecha()
            nomes, celulas = [], []
    fecha()
    return res


def ler(arq: Path) -> dict[int, dict]:
    t = texto(arq)
    partes = re.split(r"\n\s*(\d{4})-(\d{4})\s*\n", t)
    res: dict[int, dict] = {}
    for k in range(1, len(partes) - 2, 3):
        ano, corpo = int(partes[k]), partes[k + 2]
        linhas = corpo.split("\n")
        tabelas, atual = [], []
        for l in linhas:
            m = TABELA.match(l)
            if m:
                pos, nome, j, v, e, d, p, gp, gc = m.groups()
                atual.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                              "derrotas": int(d), "pontos": int(p), "gols_pro": int(gp), "gols_contra": int(gc)})
            elif atual and not re.match(r"^\s*$", l):
                tabelas.append(atual)
                atual = []
        if atual:
            tabelas.append(atual)
        res[ano] = {"tabelas": tabelas, "matrizes": _matrizes(linhas),
                    "notas": [l.strip() for l in linhas if re.search(r"changed into|forfait|deducted|penalty|points", l)]}
    return res
