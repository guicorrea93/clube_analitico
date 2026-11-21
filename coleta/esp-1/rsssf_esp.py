"""Leitor das páginas da RSSSF sobre a liga espanhola (tabless/spanhist<década>.html e tabless/span<ano>.html).

Cada temporada começa com o título "Spain 1979/80". De cada uma: a tabela final ("Final Table:", a primeira da
seção, que é a da 1ª divisão), as notas ("[1] CD Málaga had 3 points deducted..."), a matriz de resultados
("Cross-Table", nos arquivos por década) e a lista de artilheiros ("Topscorers").

Uso como biblioteca: ler(arq) -> {1979: {"tabela": [...], "notas": [...], "matriz": {(mandante, visitante): (g, g)},
                                         "matriz_notas": {(mandante, visitante): "[1]"}, "artilheiros": [...]}}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LINHA = re.compile(r"^\s*(\d+|-)\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)(.*)$")
CELULA = r"(?:xxx|\d+-\d+|\[\d+\]|---|-)"


def texto(arq: Path) -> str:
    t = arq.read_bytes().decode("latin-1")
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "")


def _tabela(linhas: list[str]) -> tuple[list[dict], list[str], int]:
    tab, i = [], 0
    while i < len(linhas):
        l = linhas[i]
        m = LINHA.match(l)
        if m:
            pos, nome, j, v, e, d, gp, gc, p, resto = m.groups()
            pos_n = int(pos) if pos != "-" else (tab[-1]["posicao"] if tab else None)
            tab.append({"posicao": pos_n, "nome": nome.strip(), "maiusculas": nome.strip().isupper(), "jogos": int(j),
                        "vitorias": int(v), "empates": int(e), "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc),
                        "pontos": int(p), "resto": resto.strip()})
        elif tab and not l.strip():
            break
        elif tab and not re.match(r"^\s*-{5,}\s*$", l):
            break
        i += 1
    notas = []
    while i < len(linhas) and not re.match(r"^\s*(Cross-Table|Topscorers|Round|Jornada|League Champions)", linhas[i]):
        if re.match(r"^\s*\[\d+\]|^\s*NB", linhas[i]):
            notas.append(linhas[i].strip())
        elif notas and linhas[i].startswith("    ") and linhas[i].strip():
            notas[-1] += " " + linhas[i].strip()
        i += 1
    return tab, notas, i


def _matriz(linhas: list[str], n: int) -> tuple[dict, dict, list[str], list[str]]:
    nomes, celulas, avisos = [], [], []
    for l in linhas:
        m = re.match(rf"^\s*(\d+)\.\s*(\S.*?)\s+((?:{CELULA}\s*)+)$", l)
        if not m:
            if nomes and not l.strip():
                break
            continue
        nomes.append(m.group(2).strip())
        celulas.append(re.findall(CELULA, m.group(3)))
    matriz, notas = {}, {}
    for i, (nm, cs) in enumerate(zip(nomes, celulas)):
        if len(cs) != len(nomes):
            avisos.append(f"matriz: linha de {nm} com {len(cs)} células (esperado {len(nomes)})")
            continue
        for j, c in enumerate(cs):
            if i == j:
                continue
            g = re.match(r"^(\d+)-(\d+)$", c)
            if g:
                matriz[(nm, nomes[j])] = (int(g.group(1)), int(g.group(2)))
            else:
                notas[(nm, nomes[j])] = c
    return matriz, notas, nomes, avisos


def _artilheiros(linhas: list[str]) -> list[dict]:
    res = []
    for l in linhas:
        if not l.strip():
            if res:
                break
            continue
        m = re.match(r"^\s*(\S.*?)\s{2,}(\S.*?)\s+(\d+)\s*(?:\(.*\))?\s*$", l)
        if not m:
            if res:
                break
            continue
        res.append({"jogador": m.group(1).strip(), "clube": m.group(2).strip(), "gols": int(m.group(3))})
    return res


def ler(arq: Path) -> dict[int, dict]:
    t = texto(arq)
    partes = re.split(r"\n\s*Spain (\d{4})/(\d{2})\s*\n", t)
    res: dict[int, dict] = {}
    for k in range(1, len(partes) - 2, 3):
        ano, corpo = int(partes[k]), partes[k + 2]
        linhas = corpo.split("\n")
        ini = next((i for i, l in enumerate(linhas) if re.match(r"^\s*Final Table", l)), None)
        if ini is None:
            continue
        tab, notas, fim = _tabela(linhas[ini + 1:])
        if not tab:
            continue
        x = res.setdefault(ano, {"tabela": tab, "notas": notas, "matriz": {}, "matriz_notas": {}, "matriz_nomes": [],
                                  "artilheiros": [], "avisos": []})
        if x["tabela"] is not tab:   # o título aparece duas vezes nos arquivos por temporada: fica a primeira tabela
            continue
        resto = linhas[ini + 1 + fim:]
        cx = next((i for i, l in enumerate(resto) if re.match(r"^\s*Cross-Table", l)), None)
        if cx is not None:
            x["matriz"], x["matriz_notas"], x["matriz_nomes"], x["avisos"] = _matriz(resto[cx + 1:], len(tab))
            for i, l in enumerate(resto[cx + 1:]):   # notas da matriz ("[1] awarded 0-1 to ...")
                if re.match(r"^\s*(Topscorers|League Champions)", l):
                    break
                if re.match(r"^\s*\[\d+\]", l):
                    x["notas"].append("matriz " + l.strip())
                elif x["notas"] and l.startswith("    ") and l.strip() and x["notas"][-1].startswith("matriz"):
                    x["notas"][-1] += " " + l.strip()
        ts = next((i for i, l in enumerate(resto) if re.match(r"^\s*Top\s*scorers?", l, re.I)), None)
        if ts is not None:
            x["artilheiros"] = _artilheiros(resto[ts + 1:])
    return res
