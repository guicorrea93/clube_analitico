"""Tabelas ("Sports table") e matrizes de resultados ("Sports results") das páginas da Wikipédia em inglês das temporadas
(data/coleta/nzl-1/wikipedia/<temporada>.wiki, baixadas por baixar_wikipedia.py).

Cada bloco vem com o título de seção em que está ("Northern League results table"), para saber de que fase é.

Uso como biblioteca: tabelas(temporada) e resultados(temporada) -> [{secao, nomes: {sigla: nome}, ...}]
"""
from __future__ import annotations

import re
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "nzl-1" / "wikipedia"


def _arquivo(temporada: str) -> Path:
    return PASTA / f"{temporada.replace('/', '-')}.wiki"


def _blocos(txt: str, modulo: str) -> list[tuple[str, str]]:
    """[(título de seção, texto do bloco)] dos {{#invoke:<modulo>|main ...}} (chaves aninhadas contadas)."""
    out = []
    for m in re.finditer(r"\{\{#invoke:\s*" + modulo + r"\s*\|", txt, re.I):
        nivel, k = 0, m.start()
        while k < len(txt):
            if txt.startswith("{{", k):
                nivel, k = nivel + 1, k + 2
            elif txt.startswith("}}", k):
                nivel, k = nivel - 1, k + 2
                if nivel == 0:
                    break
            else:
                k += 1
        secoes = re.findall(r"^=+\s*(.*?)\s*=+\s*$", txt[:m.start()], re.M)
        out.append((secoes[-1] if secoes else "", txt[m.start():k]))
    return out


def _nome(v: str) -> str:
    v = re.sub(r"<ref[^>]*/>|<ref.*?</ref>|\{\{.*?\}\}|<[^>]+>", "", v, flags=re.S)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", v)
    return (m.group(1) if m else v).strip()


def _campos(bloco: str) -> dict[str, str]:
    bloco = re.sub(r"\{\{nowrap\|(.*?)\}\}", lambda m: m.group(1), bloco, flags=re.I)   # "{{nowrap|[[X|Y]]}}"
    bloco = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"[[\1]]", bloco)   # "[[Manurewa AFC|Manurewa]]": a barra separa campos
    return {m.group(1).strip(): m.group(2).strip() for m in re.finditer(r"\|\s*([A-Za-z0-9_ ]+?)\s*=\s*([^|\n]*(?:\[\[[^\]]*\]\][^|\n]*)*)", bloco)}


def tabelas(temporada: str) -> list[dict]:
    arq = _arquivo(temporada)
    if not arq.exists():
        return []
    out = []
    for secao, b in _blocos(arq.read_text(encoding="utf-8"), "Sports table"):
        c = _campos(b)
        ordem = [s.strip() for s in c.get("team_order", "").split(",") if s.strip()] or             [c[k] for k in sorted((k for k in c if re.fullmatch(r"team\d+", k)), key=lambda k: int(k[4:]))]
        linhas = []
        for pos, s in enumerate(ordem, 1):
            n = lambda k: int(re.sub(r"\D", "", c.get(f"{k}_{s}", "0")) or 0)
            v, e, d = n("win"), n("draw"), n("loss")
            linhas.append({"pos": pos, "sigla": s, "nome": _nome(c.get(f"name_{s}", s)), "j": v + e + d, "v": v, "e": e, "d": d,
                           "gp": n("gf"), "gc": n("ga"), "ajuste": int(c[f"adjust_points_{s}"]) if re.fullmatch(r"-?\d+", c.get(f"adjust_points_{s}", "")) else 0})
        out.append({"secao": secao, "linhas": linhas})
    return out


def resultados(temporada: str) -> list[dict]:
    """[{secao, jogos: [(mandante, visitante, gm, gv, texto da célula)]}] das matrizes de resultados."""
    arq = _arquivo(temporada)
    if not arq.exists():
        return []
    out = []
    for secao, b in _blocos(arq.read_text(encoding="utf-8"), "Sports results"):
        c = _campos(b)
        nomes = {k[5:]: _nome(v) for k, v in c.items() if k.startswith("name_")}
        jogos = []
        for k, v in c.items():
            m = re.match(r"match_(\w+?)_(\w+)$", k)
            if not m or m.group(1) not in nomes or m.group(2) not in nomes:
                continue
            cel = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", v, flags=re.S)
            mm = re.search(r"(\d{1,2})\s*[–\-−]\s*(\d{1,2})", re.sub(r"\[\[[^|\]]*\|", "", cel))
            if mm:
                jogos.append((nomes[m.group(1)], nomes[m.group(2)], int(mm.group(1)), int(mm.group(2)), cel.strip()))
        out.append({"secao": secao, "jogos": jogos})
    return out
