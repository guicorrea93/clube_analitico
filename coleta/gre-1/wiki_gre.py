"""Leitor dos artigos da Wikipédia (en) da Grécia: fichas {{football box}} / {{footballbox}} (data, placar, local, árbitro,
gols) por seção, {{OneLegResult|A||placar|B}}, matrizes de resultados ({{#invoke:sports results}}, também dentro da Sports
table) e tabelas. Cópia do leitor da era antiga turca (coleta/tur-1/wiki_antigo.py), com "footballbox" sem espaço.

Cada jogo traz o caminho de seções (== Round 1 ==, === Istanbul Group ===) e, para cada clube, o nome visível e o alvo
do link ([[Beşiktaş J.K.|Beşiktaş]] -> "Beşiktaş J.K."), que ajuda a identificar o clube.

Uso: ler(texto) -> {"jogos": [...], "tabelas": [...]}.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-europa"))
from wiki_tabela import _fecha, _partes, limpar, resultados, tabelas  # noqa: E402

MESES = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september",
                                     "october", "november", "december"], 1)}


def alvo(s: str) -> str | None:
    m = re.search(r"\[\[([^\]|]+)", s or "")
    return m.group(1).strip() if m else None


def secao_em(texto: str):
    """Função posição -> caminho de títulos de seção."""
    marcas = [(m.start(), len(m.group(1)), limpar(m.group(2))) for m in re.finditer(r"^(=+)\s*(.*?)\s*=+\s*$", texto, re.M)]

    def caminho(pos: int) -> list[str]:
        pilha = []
        for p, nivel, titulo in marcas:
            if p > pos:
                break
            pilha = [x for x in pilha if x[0] < nivel] + [(nivel, titulo)]
        return [t for _, t in pilha]
    return caminho


def _placar(s: str):
    s = limpar(s)
    m = re.search(r"(\d+)\s*[–-]\s*(\d+)", s)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), s[m.end():].strip()


def _gols(s: str) -> list[tuple[str, int | None]]:
    res = []
    for m in re.finditer(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]\s*((?:\{\{goal[^}]*\}\}\s*)+)|([A-ZÀ-Ý][^{}\n]*?)\s*((?:\{\{goal[^}]*\}\}\s*)+)",
                         s or "", re.I):
        nome = (m.group(1) or m.group(3) or "").strip()
        for g in re.findall(r"\{\{goal\|?([^}]*)\}\}", m.group(2) or m.group(4) or "", re.I):
            for mi in (re.findall(r"\d+", g) or [None]):
                res.append((nome, int(mi) if mi else None))
    return res


def ler(texto: str) -> dict:
    caminho = secao_em(texto)
    jogos, tabs = [], []
    for m in re.finditer(r"\{\{\s*football ?box", texto, flags=re.I):
        corpo = texto[m.start() + 2:_fecha(texto, m.start()) - 2]
        p = {}
        for x in _partes(corpo)[1:]:
            k, _, v = x.partition("=")
            p[k.strip().lower()] = v.strip()
        sc = _placar(p.get("score", ""))
        if not sc:
            continue
        d = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", limpar(p.get("date", "")))
        data = f"{d.group(3)}-{MESES.get(d.group(2).lower(), 0):02d}-{int(d.group(1)):02d}" if d and d.group(2).lower() in MESES else None
        jogos.append({"secao": caminho(m.start()), "data": data, "nm": limpar(p.get("team1", "")), "nv": limpar(p.get("team2", "")),
                      "tm": alvo(p.get("team1", "")), "tv": alvo(p.get("team2", "")), "gm": sc[0], "gv": sc[1], "extra": sc[2],
                      "local": limpar(p.get("location", "")) or None, "estadio": limpar(p.get("stadium", "")) or None,
                      "arbitro": limpar(p.get("referee", "")) or None, "gols_m": _gols(p.get("goals1", "")),
                      "gols_v": _gols(p.get("goals2", "")), "fonte": "ficha"})
    for m in re.finditer(r"\{\{\s*OneLegResult\s*\|", texto):
        corpo = texto[m.start() + 2:_fecha(texto, m.start()) - 2]
        ps = _partes(corpo)
        if len(ps) < 5:
            continue
        sc = _placar(ps[3])
        if not sc:
            continue
        jogos.append({"secao": caminho(m.start()), "data": None, "nm": limpar(ps[1]), "nv": limpar(ps[4]), "tm": alvo(ps[1]),
                      "tv": alvo(ps[4]), "gm": sc[0], "gv": sc[1], "extra": sc[2], "local": None, "estadio": None,
                      "arbitro": None, "gols_m": [], "gols_v": [], "fonte": "eliminatoria"})
    # matrizes (a da Millî Küme e as dos grupos finais, dentro da Sports table)
    texto_m = re.sub(r"(?i)#invoke:\s*sports table", "#invoke:sports results", texto)
    pos = [mm.start() for mm in re.finditer(r"\{\{\s*#invoke:\s*sports results\s*\|", texto_m, flags=re.I)]
    for g in resultados(texto_m):
        # posição do bloco: o primeiro bloco que tem o primeiro par de códigos
        c1, c2 = next(iter(g["jogos"]))
        p0 = next((p for p in pos if f"match_{c1}_{c2}" in texto_m[p:_fecha(texto_m, p)]), 0)
        bloco = texto_m[p0:_fecha(texto_m, p0)]
        alvos = dict(re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)", bloco))
        for (a, b), pl in g["jogos"].items():
            for gm, gv in pl:
                jogos.append({"secao": caminho(p0), "data": None, "nm": g["nomes"].get(a, a), "nv": g["nomes"].get(b, b),
                              "tm": alvos.get(a), "tv": alvos.get(b), "gm": gm, "gv": gv, "extra": "", "local": None,
                              "estadio": None, "arbitro": None, "gols_m": [], "gols_v": [], "fonte": "matriz"})
    for tb in tabelas(texto):
        tabs.append(tb)
    return {"jogos": jogos, "tabelas": tabs}
