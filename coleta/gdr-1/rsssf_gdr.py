"""Leitor das páginas da RSSSF de cada temporada da Alemanha Oriental (tablesd/ddr50.html ... ddr91.html).

Só a primeira seção (a Oberliga): "ROUND N", linha de data ("28/ 8/1971") e linhas de jogo
("1. FC Lokomotive Leipzig   2:0 FC Vorwärts Frankfurt/Oder", com nota entre colchetes às vezes), até a "FINAL TABLE"
(" 1. 1. FC Magdeburg ....... 38   26   17 -  4 -  5   48: 23 +25"). Depois vêm a DDR-Liga e a copa, que ficam de fora.

Uso: ler(arq) -> {"jogos": [{rodada, data, nm, nv, gm, gv, nota}], "tabela": [{posicao, nome, pontos, jogos, vitorias,
empates, derrotas, gols_pro, gols_contra, resto}], "notas": [...]}.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

# placar "2:0"; jogo dado fora de campo: "X:0" ou "0-X" (vitória para o lado do X, gols 0:0)
JOGO = re.compile(r"^(\S.*?)\s{2,}(\d+|X)\s*[:-]\s*(\d+|X)\s*((?:1\.\s*)?[^\s\d:].*?)\s*(\[.*?\]?)?\s*$")
JOGO_1ESPACO = re.compile(r"^(\S.*?)\s(\d+|X)\s*[:-]\s*(\d+|X)\s*((?:1\.\s*)?[^\s\d:].*?)\s*(\[.*?\]?)?\s*$")
DATA = re.compile(r"^\s*(\d{1,2})/\s*(\d{1,2})/(\d{4})\s*$")
LINHA = re.compile(r"^\s*(\d+)?\.?\s+(\S.*?)\s*\.{2,}\s*(-?\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s*-\s*(\d+)\s+(\d+)\s*:\s*(\d+)(.*)$")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def ler(arq: Path) -> dict:
    jogos, tabela, notas = [], [], []
    rodada = data = None
    estado = "antes"
    for l in texto(arq).split("\n"):
        s = l.strip()
        if estado == "antes":
            if re.search(r"(?i)OBERLIGA", s):
                estado = "jogos"
            continue
        if estado == "jogos":
            m = re.match(r"(?i)^ROUND\s+(\d+)", s)
            if m:
                rodada = int(m.group(1))
                continue
            m = DATA.match(s)
            if m:
                data = f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
                continue
            if re.search(r"(?i)FINAL TABLE", s):
                estado = "tabela"
                continue
            m = JOGO.match(s) or JOGO_1ESPACO.match(s)
            if m and re.search(r"\s-\s|\[", m.group(1)):   # "A  -  B [abandoned ...]": jogo sem placar, vira nota
                m = None
            if m and rodada is not None:
                dado = "X" in (m.group(2), m.group(3))
                jogos.append({"rodada": rodada, "data": data, "nm": m.group(1).strip(), "nv": re.sub(r"\s*\[.*$", "", m.group(4)).strip(),
                              "gm": 0 if dado else int(m.group(2)), "gv": 0 if dado else int(m.group(3)),
                              "vencedor": ("m" if m.group(2) == "X" else "v") if dado else None,
                              "nota": (m.group(5) or "").strip("[] ")})
            elif s and rodada is not None and not re.match(r"^[-=*]+$", s):
                notas.append(s)
            continue
        if estado == "tabela":
            m = LINHA.match(l)
            if m:
                tabela.append({"posicao": int(m.group(1)) if m.group(1) else None, "nome": m.group(2).strip(),
                               "pontos": int(m.group(3)), "jogos": int(m.group(4)), "vitorias": int(m.group(5)),
                               "empates": int(m.group(6)), "derrotas": int(m.group(7)), "gols_pro": int(m.group(8)),
                               "gols_contra": int(m.group(9)), "resto": m.group(10).strip()})
                continue
            if tabela and (re.search(r"(?i)TOP-?SCORERS|DDR-LIGA|LIGA|POKAL|CUP", s) and not s.startswith("-")):
                break
            if s and tabela and not s.startswith("-"):
                notas.append(s)
    return {"jogos": jogos, "tabela": tabela, "notas": notas}
