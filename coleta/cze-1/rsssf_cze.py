"""Leitor das páginas de temporada da RSSSF para a Tchéquia (tablest/tsjeYY.html e tsjeYYYY.html).

A página traz a tabela final ("Final Table:"; desde 2022/23 uma por fase: "Regular Stage", "Skupina o Titul",
"Skupina o Záchranu") e os jogos rodada a rodada:

    Round 1
    [Aug 14]
    Sparta       5-1 Brno
    Plzen        0-2 Slavia

com os nomes curtos dos clubes. Nas páginas mais recentes vêm também a Copa e as divisões de baixo, depois da liga; a
leitura para na primeira seção que não é da 1ª divisão.

Uso como biblioteca:
  texto(arq) -> texto sem HTML
  jogos(texto, ano) -> [{"rodada", "data" (AAAA-MM-DD ou None), "m", "v", "gm", "gv", "resto"}]
  tabelas(texto) -> [[linha da tabela, ...], ...] (uma lista por "Final Table")
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "gre-1"))   # leitor de tabela do grego, sem passar na frente dos módulos daqui
from rsssf_gre import tabela  # noqa: E402

MESES = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
JOGO = re.compile(r"^(\S.*?)\s+(\d+)-(\d+)\s+(\S.*?)\s*(\[.*\]|\(.*\))?\s*$")
FIM_LIGA = re.compile(r"(?i)^\s*(cup|pohár|národní liga|2\. liga|druhá liga|čfl|msfl|second level|topscorers?|top scorers)\b")


def texto(arq: Path) -> str:
    b = arq.read_bytes()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        t = b.decode("latin-1")
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "")


def jogos(t: str, ano: int) -> list[dict]:
    res, rodada, data = [], None, None
    em_rodadas = False
    for l in t.split("\n"):
        s = l.strip()
        if not s:
            continue
        m = re.match(r"(?i)^round\s+(\d+)\b", s)
        if m:
            rodada, data, em_rodadas = int(m.group(1)), None, True
            continue
        if em_rodadas and FIM_LIGA.match(s):
            break
        m = re.match(r"^\[([A-Za-z]{3})\w*\s+(\d{1,2})\]$", s)
        if m and em_rodadas:
            mes = MESES.get(m.group(1).lower())
            data = f"{ano + (1 if mes and mes < 7 else 0)}-{mes:02d}-{int(m.group(2)):02d}" if mes else None
            continue
        if not em_rodadas or rodada is None:
            continue
        if res and l.startswith(" ") and (s.startswith("[") or (res[-1].get("gols_txt") and not res[-1]["gols_txt"].endswith("]"))):
            res[-1]["gols_txt"] = (res[-1].get("gols_txt", "") + " " + s).strip()   # autores dos gols do jogo de cima
            continue
        m = JOGO.match(l)
        if m and not re.match(r"^\s*\d+\.", l):
            res.append({"rodada": rodada, "data": data, "m": m.group(1).strip(), "v": m.group(4).strip(),
                        "gm": int(m.group(2)), "gv": int(m.group(3)), "resto": (m.group(5) or "").strip()})
    return res


def autores(txt: str, gm: int, gv: int) -> tuple[list, list] | None:
    """"[P.Horvath 45pen, T.Janotka 80og; P.Sultes 64, T.Janotka 79]" -> (gols do mandante, gols do visitante), cada gol
    (jogador, minuto, acréscimo, tipo); o que vem antes do ";" é do mandante. Sem ";", é de quem marcou (o outro lado fez 0).
    None se a conta não fecha com o placar."""
    corpo = re.sub(r"^\[|\]$", "", txt.strip()).strip()
    lados = [x.strip() for x in corpo.split(";")]
    if len(lados) == 1:
        if gm and gv:
            return None
        lados = [lados[0], ""] if gm else ["", lados[0]]
    if len(lados) != 2:
        return None
    res = []
    for lado in lados:
        gols, nome = [], None
        for tok in [x.strip() for x in lado.split(",") if x.strip()]:
            m = re.match(r"^(.*?)\s*(\d+)(?:\+(\d*))?\s*(pen|p|og|o\.g\.)?\.?$", tok, re.I)
            if not m:   # jogador sem minuto ("J. Svach")
                if not re.match(r"^[^\d\[\]]+$", tok):
                    return None
                gols.append((tok.strip(), None, None, "normal"))
                continue
            if m.group(1):
                nome = m.group(1).strip()
            if not nome:
                return None
            tipo = {"pen": "penalti", "p": "penalti", "og": "contra", "o.g.": "contra"}.get((m.group(4) or "").lower(), "normal")
            gols.append((nome, int(m.group(2)), int(m.group(3)) if m.group(3) else None, tipo))
        res.append(gols)
    if (len(res[0]), len(res[1])) != (gm, gv):
        return None
    return res[0], res[1]


LINHA_TAB = re.compile(r"^\s*(\d+)\.\s*((?:\d\.\s*)?[^\W\d].*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)(.*)$")


def tabelas(t: str) -> list[list[dict]]:
    """Uma lista por tabela ("Final Table:" ou só "Table:"). Linha "J V E D GP-GC Pts"; o nome pode começar com número
    ("13.1. FK Příbram")."""
    partes = re.split(r"(?im)^\s*(?:final\s+)?table\s*:?\s*$", t)
    res = []
    for p in partes[1:]:
        linhas = []
        for l in p.split("\n"):
            m = LINHA_TAB.match(l)
            if not m:
                if linhas and l.strip() and not re.match(r"^\s*[-=\s]+$", l) and not l.startswith(" "):
                    break   # acabou a tabela
                continue
            pos, nome, j, v, e, d, gp, gc, pts, resto = m.groups()
            if linhas and int(pos) < linhas[-1]["posicao"]:
                break
            linhas.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc), "pontos": int(pts),
                           "resto": resto.strip()})
        if linhas:
            res.append(linhas)
    return res
