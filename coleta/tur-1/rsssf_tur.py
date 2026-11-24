"""Leitor da página de tabelas finais da RSSSF para a Turquia (tablest/turkhist.html), de 1959 a 1996/97.

Cada temporada começa numa linha só com o ano ("1959", "1959-60") e traz uma ou mais tabelas (Red Group, White Group,
Play-off Group, Classification Group), cada uma com a linha de cabeçalho "G W D L F A P" (e "3P" de 1987/88 em diante:
os pontos com 3 por vitória, que valem; "P" é a conta antiga). Linhas de jogo ("A - B 1-0") ficam em `notas`.

Uso: ler(arq) -> {ano: [{"titulo", "linhas": [{posicao, nome, jogos, vitorias, empates, derrotas, gols_pro, gols_contra,
pontos, resto}], "notas"}]}, com ano = ano inicial (1959 -> 1958, a chave de edicoes.py).
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ANO = re.compile(r"^\s*(\d{4})(?:-(\d{2}))?\s*$")
LINHA = re.compile(r"^\s*(\d+)?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)(?:\s+(-?\d+))?\s*(.*?)\s*$")


def texto(arq: Path) -> str:
    """Texto sem HTML. A lista de artilheiros (turktops.html) vem em UTF-16; as outras páginas, em UTF-8."""
    b = arq.read_bytes()
    t = b.decode("utf-16") if b[:2] in (b"\xff\xfe", b"\xfe\xff") else b.decode("utf-8", "replace")
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "")


def ler(arq: Path) -> dict[int, list[dict]]:
    res: dict[int, list[dict]] = {}
    ano, titulo, atual, tres, ultima = None, None, None, False, ""
    for l in texto(arq).split("\n"):
        m = ANO.match(l)
        if m:
            a = int(m.group(1))
            ano = 1958 if (a == 1959 and not m.group(2)) else a if m.group(2) else None
            if ano is not None and ano < 1958:
                ano = None
            atual = None
            if ano is not None:
                res.setdefault(ano, [])
            continue
        if ano is None:
            continue
        if l.strip().startswith("List of champions"):
            ano = None
            continue
        if re.match(r"^\s*G\s+W\s+D\s+L\s+F\s+A\s+P", l):
            tres = "3P" in l
            atual = {"titulo": ultima.strip() or None, "linhas": [], "notas": []}
            res[ano].append(atual)
            continue
        if atual is None:
            if l.strip():
                ultima = l
            continue
        m = LINHA.match(l.replace("\t", " "))
        if m and not re.search(r"\s-\s", m.group(2)):
            nome = re.sub(r"\s*\((?:[CLN]|L, C|C, L)\)\s*$", "", m.group(2)).strip()
            p2, p3 = int(m.group(9)), m.group(10)
            atual["linhas"].append({
                "posicao": int(m.group(1)) if m.group(1) else None, "nome": nome, "jogos": int(m.group(3)),
                "vitorias": int(m.group(4)), "empates": int(m.group(5)), "derrotas": int(m.group(6)),
                "gols_pro": int(m.group(7)), "gols_contra": int(m.group(8)),
                "pontos": int(p3) if tres and p3 is not None else p2, "resto": m.group(11)})
            continue
        if re.match(r"^\s*-{5,}", l):
            continue
        if l.strip():
            atual["notas"].append(l.strip())
            ultima = l
            if not atual["linhas"] or len(atual["notas"]) > 0:
                pass
        if not l.strip() and atual["linhas"]:
            ultima = ""
    return res
