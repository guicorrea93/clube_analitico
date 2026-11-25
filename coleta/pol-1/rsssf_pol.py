"""Leitor da RSSSF para a Polônia: polhist.html (1920 a 2000/01) e as páginas de temporada (pol02.html ... pol2026.html).

polhist.html está em ISO-8859-2 ("Wis³a" = Wisła). Um bloco por temporada ("Poland 1927", "Poland 1985/86"); dentro dele,
seções com título ("Southern Group", "Final Group", "Group 1", "division 1", "First round", "Final matches") e:
- tabelas com a matriz na mesma linha: "c  1 WISŁA KRAKÓW  26  40  19  2  5  95 32   x  3:0 4:1 ..." (marca, posição,
  nome, J, Pts, V, E, D, GP, GC e depois uma célula por adversário, na ordem das linhas; "x" na diagonal; "wo+" e "wo-"
  = vitória e derrota por W.O.);
- jogos avulsos: "Warta Poznań - Pogoń Lwów 1:1 (0:0)", "Burza Wrocław - Pocztowy KS Szczecin 1:2 aet"; ida e volta na
  mesma linha ("Odra Opole - ZAGŁĘBIE SOSNOWIEC   1:0   0:1": o 2º placar é do jogo de volta, com o mando invertido).

Uso como biblioteca:
  texto(arq) -> texto sem HTML (tenta UTF-8, depois ISO-8859-2)
  blocos(texto) -> {"1927": texto do bloco, ...}
  secoes(bloco) -> [{"titulo", "tabela": [linhas], "jogos": [jogos avulsos]}]
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LINHA = re.compile(r"^\s*([a-z>^*])?\s*(\d+)\s+(\S.*?)\s+(\d+)\s+(-?\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)(?:\s+(.*))?$")
CELULA = re.compile(r"^(x|wo[+-]|-+|\d+[:-]\d+)$")   # "0-5" (com hífen) aparece em 1925
AVULSO = re.compile(r"^\s*(\S.*?)\s+-\s+(\S.*?)\s+(\d+):(\d+)(?:\s*\(\d+:\d+\))?\s*(aet|a\.e\.t\.)?"
                    r"(?:\s+(\d+):(\d+)(?:\s*\(\d+:\d+\))?\s*(aet|a\.e\.t\.)?)?\s*(?:\(.*\))?\s*$", re.I)


def texto(arq: Path) -> str:
    b = arq.read_bytes()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        t = b.decode("iso-8859-2")
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "")


def blocos(t: str) -> dict[str, str]:
    partes = re.split(r"(?m)^Poland (\d{4}(?:/\d{2})?)\s*$", t)
    return {partes[i]: partes[i + 1] for i in range(1, len(partes), 2)}


def secoes(bloco: str) -> list[dict]:
    res, atual = [], {"titulo": "", "tabela": [], "jogos": []}
    for l in bloco.split("\n"):
        s = l.strip()
        if not s:
            continue
        m = LINHA.match(l)
        if m:
            marca, pos, nome, j, pts, v, e, d, gp, gc, resto = m.groups()
            cels = (resto or "").split()
            if cels and not all(CELULA.match(c) for c in cels):
                cels = []   # sobra de texto, não é matriz
            atual["tabela"].append({"marca": marca, "posicao": int(pos), "nome": nome.strip(), "jogos": int(j),
                                    "pontos": int(pts), "vitorias": int(v), "empates": int(e), "derrotas": int(d),
                                    "gols_pro": int(gp), "gols_contra": int(gc), "celulas": cels})
            continue
        if re.search(r"\bpl\s+pts\b", l):
            continue
        m = AVULSO.match(l)
        if m and not re.search(r"(?i)verified|originally|interrupted|games|matches|both", l):
            atual["jogos"].append({"m": m.group(1).strip(), "v": m.group(2).strip(), "gm": int(m.group(3)),
                                   "gv": int(m.group(4)), "aet": bool(m.group(5))})
            if m.group(6):   # ida e volta na mesma linha: o 2º jogo com o mando invertido
                atual["jogos"].append({"m": m.group(2).strip(), "v": m.group(1).strip(), "gm": int(m.group(7)),
                                       "gv": int(m.group(6)), "aet": bool(m.group(8))})
            continue
        # título de seção: linha curta, sem números de jogo, depois da qual vem tabela ou jogos
        if len(s) < 40 and not re.search(r"\d+:\d+|\d{2}\.\d{2}\.\d{4}|^\(|^Nb|^Topscorers|^Played", s) and \
                not re.match(r"^[A-ZĄĆĘŁŃÓŚŹŻ]?[a-ząćęłńóśźż]+\s+[A-ZĄĆĘŁŃÓŚŹŻ]{2,}", s):
            if atual["tabela"] or atual["jogos"]:
                res.append(atual)
            atual = {"titulo": s, "tabela": [], "jogos": []}
    if atual["tabela"] or atual["jogos"]:
        res.append(atual)
    return res


def jogos_da_matriz(tabela: list[dict]) -> list[dict]:
    """Jogos da matriz de uma tabela: célula da linha i, coluna k = linha i em casa contra a linha k."""
    res = []
    for i, x in enumerate(tabela):
        cel = x["celulas"]
        if len(cel) != len(tabela):
            continue
        for k, c in enumerate(cel):
            if k == i or c == "x" or set(c) == {"-"}:
                continue
            if c in ("wo+", "wo-"):
                res.append({"i": i, "k": k, "gm": 3 if c == "wo+" else 0, "gv": 0 if c == "wo+" else 3, "wo": True})
            else:
                g1, g2 = re.split(r"[:-]", c)
                res.append({"i": i, "k": k, "gm": int(g1), "gv": int(g2), "wo": False})
    return res
