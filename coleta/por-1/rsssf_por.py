"""Leitor do arquivo histórico da RSSSF portuguesa (tablesp/porthist193435.html ... porthist200405.html).

Cada página tem a "Final Table" (posição, nome em 21 colunas, jogos, V, E, D, gols pró- contra, pontos e depois casa e
fora) e a "Cross Table" (matriz de resultados, linhas e colunas na ordem da tabela final; "X" na diagonal).

Uso como biblioteca: ler(arq) -> {"tabela": [{posicao, nome, jogos, ...}], "matriz": {(mandante, visitante): (g, g)},
                                  "notas": [...]}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

TABELA = re.compile(r"^\s*(\d+)\s(.+?)\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)-\s*(\d+)\s+(-?\d+)\b")
COLUNAS_TROCADAS = {"porthist199091.html": (13, 14)}
CELULA = re.compile(r"X|\d+-\d+|-{1,3}|[A-Za-z/]{1,4}\*?")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def ler(arq: Path) -> dict:
    t = texto(arq)
    i_tab, i_cruz = t.find("Final Table"), t.find("Cross Table")
    fim_cruz = t.find("Accumulated Table", i_cruz) if i_cruz >= 0 else -1
    tabela = []
    for l in t[i_tab:i_cruz if i_cruz > 0 else len(t)].split("\n"):
        m = TABELA.match(l)
        if m:
            pos, nome, j, v, e, d, gp, gc, p = m.groups()
            tabela.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc), "pontos": int(p)})
    # a coluna k da matriz é o clube da k-ésima linha (em 1977/78 as linhas 8 e 9 vêm com os números trocados; a ordem das
    # linhas é a que vale). Em 1990/91 as colunas 13 e 14 vêm trocadas (Gil Vicente e Famalicão): com a troca, os 380
    # placares batem com o ogol; sem ela, 30 não batem
    matriz, avisos, linhas = {}, [], []
    if i_cruz >= 0:
        for l in t[i_cruz:fim_cruz if fim_cruz > 0 else len(t)].split("\n"):
            m = re.match(r"^\s*(\d+)\s(.{20,22}?)\s+((?:X|\d+-\d+|-|\s|[A-Za-z/*])+)$", l)
            if m and 1 <= int(m.group(1)) <= len(tabela):
                linhas.append((m.group(2).strip(), CELULA.findall(m.group(3)), l.strip()))
        troca = COLUNAS_TROCADAS.get(arq.name)
        for i, (nm, cels, l) in enumerate(linhas):
            if len(cels) != len(tabela):
                avisos.append(f"linha {i + 1} da matriz com {len(cels)} células ({len(tabela)} clubes): {l}")
                continue
            if troca and i + 1 not in troca:   # nas linhas dos dois clubes o "X" já está no lugar certo
                x, y = troca[0] - 1, troca[1] - 1
                cels[x], cels[y] = cels[y], cels[x]
            for k, c in enumerate(cels):
                g = re.match(r"^(\d+)-(\d+)$", c)
                if g and k != i and k < len(linhas):
                    matriz[(nm, linhas[k][0])] = (int(g.group(1)), int(g.group(2)))
    resto = t[fim_cruz if fim_cruz > 0 else len(t):]
    notas = [l.strip() for l in t[i_tab:fim_cruz if fim_cruz > 0 else len(t)].split("\n")
             if re.search(r"(?i)awarded|deducted|forfeit|annulled|abandoned|points? (?:deduct|penalt)|not played|\bNB\b|\bNote", l)]
    return {"tabela": tabela, "matriz": matriz, "notas": notas, "avisos": avisos, "tem_acumulada": bool(resto)}
