"""Leitor das páginas da RSSSF para a Grécia.

Três tipos de página:
- grkprehist.html (1905/06 a 1958/59): um bloco por temporada ("1930/31" sozinho na linha); a fase nacional vem depois
  de "National Championship", com matriz, lista de jogos com data ("18.5.1930 Pireas : Olympiakos S.F.P. - Aris A.S.
  5:0"), tabela e notas;
- grkhist.html (1959/60 a 1998/99): um bloco por temporada, com matriz (até 1980/81, exceto 1977/78 e 1978/79) e tabela;
- grkYY.html / grkYYYY.html (desde 1968/69): uma temporada, com matriz, notas, tabela, artilheiros.

Matriz: cabeçalho com códigos de 3 letras; linha "NN. Nome  XXX 1:0 2-2 (1) ...", a coluna i é o clube da linha i
(diagonal "XXX"). Célula "(n)", "{n}" ou "(*)": o placar está na nota (texto livre; o importador resolve cada uma) ("(1) Played in Trikala 0:1", "(1) Apollonas - Kastoria
awarded 2-0 (Original Score 0:0)"). Célula vazia ou "---": jogo não disputado.

Tabelas em dois formatos:
- "Pts J V-E-D GP:GC saldo" (" 1.Olympiakos S.F.P. Pireas   47  34  20- 7- 7  49:21 +28");
- "J V E D GP-GC Pts" (" 1. AEK Athinai   34  24  6  4  78-27  78").

Uso como biblioteca:
  blocos(arq) -> {temporada "1959/60": texto do bloco}
  matriz(texto) -> {"clubes": [nome por linha], "jogos": [{"i", "j", "gm", "gv", "nota", "wo"}], "notas": {n: texto}}
  tabela(texto) -> [{posicao, nome, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, resto}]
  datados(texto) -> [{"data", "cidade", "m", "v", "gm", "gv", "resto"}] (lista de jogos com data)
"""
from __future__ import annotations

import html
import re
from pathlib import Path

# o nome pode vir grudado no 1º placar ("9. Fostiras Tavr.1-5 1-0 ..."); "*" e "x" no placar = W.O. ("2-*", "x:2")
LINHA_MATRIZ = re.compile(r"^\s*(\d+)\s*\.\s*(\S.*?)\s*((?:XXX|xxx|\(\d+\)|\(\*\)|\{\d+\}|[\d*x]+\s*[:;-]\s*[\d*x]+|-{2,3}|\.\.\.)"
                          r"(?:\s+(?:XXX|xxx|\(\d+\)|\(\*\)|\{\d+\}|[\d*x]+\s*[:;-]\s*[\d*x]+|-{2,3}|\.\.\.))*)\s*$")
CELULA = re.compile(r"XXX|xxx|[({](\d+|\*)[)}]|([\d*x]+)\s*[:;-]\s*([\d*x]+)|-{2,3}|\.\.\.")
TAB_A = re.compile(r"^\s*(\d+)?\s*\.?\s*([A-Za-z].*?)\s+(-?\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s*-\s*(\d+)\s+(\d+)\s*:\s*(\d+)(.*)$")
TAB_B = re.compile(r"^\s*(\d+)?\s*\.?\s*([A-Za-z].*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)(.*)$")
DATADO = re.compile(r"^\s*(\d{1,2})\.(\d{1,2})\.(\d{4})\s+([^:]*?)\s*:\s*(\S.*?)\s+-\s+(\S.*?)\s+(\d+)\s*:\s*(\d+)(.*)$")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def blocos(arq: Path) -> dict[str, str]:
    t = texto(arq)
    partes = re.split(r"(?m)^\s*(\d{4}/\d{2})\s*$", t)
    res: dict[str, str] = {}
    for i in range(1, len(partes), 2):
        s = partes[i].strip()
        if s in res and len(res[s]) > len(partes[i + 1]):   # o índice do topo repete os rótulos
            continue
        res[s] = partes[i + 1]
    return res


def matriz(t: str) -> dict:
    linhas = []
    for l in t.split("\n"):
        m = LINHA_MATRIZ.match(l)
        if m and ("XXX" in m.group(3) or "xxx" in m.group(3)):
            linhas.append((int(m.group(1)), m.group(2).strip(), m.group(3)))
    notas = {n: txt.strip() for n, txt in re.findall(r"(?m)^\s*[({](\d+)[)}]\s*(.+(?:\n(?!\s*[({]\d+[)}]|\s*$).+)*)", t)}
    jogos, clubes = [], [nome for _, nome, _ in linhas]
    for i, (_, _, resto) in enumerate(linhas):
        cel = [c for c in CELULA.finditer(resto)]
        if len(cel) != len(linhas):
            raise ValueError(f"matriz: {len(cel)} células na linha de {clubes[i]} ({len(linhas)} clubes)")
        for j, c in enumerate(cel):
            if i == j:
                continue
            if c.group(1):
                jogos.append({"i": i, "j": j, "gm": None, "gv": None, "nota": c.group(1), "wo": False})
            elif c.group(2):
                wo = not (c.group(2).isdigit() and c.group(3).isdigit())   # "2-*", "x:2": W.O., placar 2-0
                gm = int(c.group(2)) if c.group(2).isdigit() else 0
                gv = int(c.group(3)) if c.group(3).isdigit() else 0
                jogos.append({"i": i, "j": j, "gm": gm, "gv": gv, "nota": None, "wo": wo})
    return {"clubes": clubes, "jogos": jogos, "notas": notas}


def tabela(t: str) -> list[dict]:
    res = []
    for l in t.split("\n"):
        m = TAB_A.match(l)
        if m:
            pos, nome, p, j, v, e, d, gp, gc, resto = m.groups()
        else:
            m = TAB_B.match(l)
            if not m:
                continue
            pos, nome, j, v, e, d, gp, gc, p, resto = m.groups()
        if "XXX" in l or "xxx" in l:
            continue
        if pos is None:   # posição dividida com a linha de cima
            pos = res[-1]["posicao"] if res else 0
        res.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                    "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc), "pontos": int(p),
                    "resto": resto.strip()})
    return res


def datados(t: str) -> list[dict]:
    res = []
    for l in t.split("\n"):
        m = DATADO.match(l)
        if m:
            d, mes, a, cidade, mand, vis, gm, gv, resto = m.groups()
            res.append({"data": f"{a}-{int(mes):02d}-{int(d):02d}", "cidade": cidade.strip(), "m": mand.strip(),
                        "v": vis.strip(), "gm": int(gm), "gv": int(gv), "resto": resto.strip()})
    return res
