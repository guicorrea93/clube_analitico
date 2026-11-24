"""Leitor das tabelas finais da RSSSF para a Bélgica (tablesb/belghist.html, 1895/96 a 2007/08).

A página tem um bloco por temporada ("Season 1895-1896"), com uma ou mais tabelas: a da 1ª divisão primeiro ("Coupe de
Championnat", "Division I", "Premier Division", "First Division"; de 1898/99 a 1903/04, "First Division A" e "B" e o
"Final Tour"), depois as das divisões de baixo. Linhas no formato J V **D** E GP GC Pts (vitórias, derrotas, empates:
"[Tables in W-L-D format]"); de 2006/07 em diante, J V E D. Posição dividida: a linha vem sem número (fica a de
cima). Algumas linhas trazem só a posição e o nome (tabela não conhecida).

Uso como biblioteca: ler(arq) -> {ano de início: [{"titulo", "linhas": [{posicao, nome, jogos, vitorias, empates, derrotas,
gols_pro, gols_contra, pontos}], "notas": [...]}]}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LINHA = re.compile(r"^\s*(\d+)?\s+(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s*(.*)$")
SO_NOME = re.compile(r"^\s*(\d+)\s+(\S.*?)\s*$")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def ler(arq: Path) -> dict[int, list[dict]]:
    t = texto(arq)
    partes = re.split(r"\n\s*Season (\d{4})-(\d{4})\s*\n", t)
    res: dict[int, list[dict]] = {}
    for i in range(1, len(partes), 3):
        a, corpo = int(partes[i]), partes[i + 2]
        tabelas: list[dict] = []
        titulo, atual = None, None
        for l in corpo.split("\n"):
            m = LINHA.match(l)
            if m:
                pos, nome, j, v, d, e, gp, gc, p, resto = m.groups()
                if a >= 2006:   # a partir de 2006/07 a página usa V E D
                    d, e = e, d
                if pos is None:   # posição dividida com a linha de cima
                    pos = atual["linhas"][-1]["posicao"] if atual and atual["linhas"] else 0
                if atual is None:
                    atual = {"titulo": titulo, "linhas": [], "notas": []}
                    tabelas.append(atual)
                atual["linhas"].append({"posicao": int(pos), "nome": nome.strip().rstrip("*").strip(), "jogos": int(j),
                                        "vitorias": int(v), "derrotas": int(d), "empates": int(e), "gols_pro": int(gp),
                                        "gols_contra": int(gc), "pontos": int(p), "resto": resto.strip()})
                continue
            m = SO_NOME.match(l)
            if m and not re.search(r"\d\s*-\s*\d", l) and len(m.group(2)) < 40:
                if atual is None:
                    atual = {"titulo": titulo, "linhas": [], "notas": []}
                    tabelas.append(atual)
                atual["linhas"].append({"posicao": int(m.group(1)), "nome": m.group(2).strip().rstrip("*").strip(),
                                        "jogos": None, "vitorias": None, "derrotas": None, "empates": None,
                                        "gols_pro": None, "gols_contra": None, "pontos": None, "resto": ""})
                continue
            s = l.strip()
            if not s:
                continue
            if atual is not None and atual["linhas"] and not re.match(r"^\d", s):
                atual = None   # acabou a tabela
            if atual is None and not re.match(r"(?i)^(remarks?|\(|\*|source|nb|at the end|for the|olympia|skill)", s) \
                    and len(s) < 70 and not re.search(r"\d+-\d+$", s):
                titulo = s
            if tabelas:
                tabelas[-1]["notas"].append(s)
        res[a] = tabelas
    return res
