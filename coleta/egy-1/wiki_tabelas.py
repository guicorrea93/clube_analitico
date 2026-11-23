"""Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/egy-1/wikipedia/en_<temporada>.txt).

É a terceira fonte quando a tabela da RSSSF e a soma dos jogos não fecham: os artigos dos anos antigos tiram a tabela do
site do Dr. Tarek Said (drtareksaid.net), um dos autores das páginas da RSSSF, em versão mais nova. Lê dois formatos:
- wikitable com uma célula por linha ("|{{center|22}}"), dos anos antigos;
- o modelo "Sports table" (win_XXX=, draw_XXX=, ...), dos anos recentes.

Uso como biblioteca: tabelas(temporada) -> [[{nome, j, v, e, d, gp, gc, pts}]] (uma lista por tabela do artigo)
"""
from __future__ import annotations

import re

from baixar_wikipedia import arquivo


def _limpa(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", c, flags=re.S)
    c = re.sub(r"\{\{(?:center|nowrap|small)\|([^{}]*)\}\}", r"\1", c)
    c = re.sub(r"\{\{[^{}]*\}\}", "", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", c)
    c = c.replace("'''", "").replace("''", "")
    c = re.sub(r"^\s*[a-z]+=\"[^\"]*\"\s*\|", "", c)   # atributos da célula (style="..." |)
    return re.sub(r"\s+", " ", c).strip()


def _wikitable(t: str) -> list[list[dict]]:
    saida = []
    for tab in re.findall(r"\{\|.*?\n\|\}", t, flags=re.S):
        linhas = []
        for r in tab.split("\n|-")[1:]:
            cel = [_limpa(c) for c in re.split(r"\n\||\|\|", r)[1:]]
            cel = [c for c in cel if c != ""]
            k = next((i for i, c in enumerate(cel) if re.search(r"[A-Za-z]{2}", c) and not re.fullmatch(r"\d+", c)), None)
            if k is None:
                continue
            nums = []
            for c in cel[k + 1:]:
                m = re.fullmatch(r"[+−-]?\d+", c.replace("−", "-"))
                if m:
                    nums.append(int(c.replace("−", "-")))
            if len(nums) < 7:
                continue
            j, v, e, d, gp, gc = nums[:6]
            pts = nums[7] if len(nums) >= 8 and nums[6] == gp - gc else nums[6]
            if v + e + d != j:
                continue
            nome = re.sub(r"(\s*\([A-Z]{1,3}\))+\s*$", "", cel[k]).strip()   # "(C)", "(R)", "(QR)"
            linhas.append({"nome": nome, "j": j, "v": v, "e": e, "d": d, "gp": gp, "gc": gc, "pts": pts})
        if len(linhas) >= 2:
            saida.append(linhas)
    return saida


def _sports_table(t: str) -> list[list[dict]]:
    saida = []
    for bloco in re.findall(r"\{\{\s*#invoke:\s*Sports table.*?\n\}\}", t, flags=re.S | re.I):
        ordem = re.search(r"\|\s*team_order\s*=\s*([^\n|]+)", bloco)
        if ordem:
            times = [x.strip() for x in ordem.group(1).split(",")]
        else:   # "|team1=AHL|name_AHL=..." (a ordem é a do número)
            times = [x for _, x in sorted((int(n), x) for n, x in re.findall(r"\|\s*team(\d+)\s*=\s*(\w+)", bloco))]
        val = lambda campo, x: int(m.group(1)) if (m := re.search(rf"\|\s*{campo}_{re.escape(x)}\s*=\s*(-?\d+)", bloco)) else 0
        linhas = []
        for x in times:
            nm = re.search(rf"\|\s*name_{re.escape(x)}\s*=\s*(\[\[[^\]]*\]\]|[^|\n]*)", bloco)
            nome = _limpa(nm.group(1)) if nm else x
            v, e, d, gp, gc = val("win", x), val("draw", x), val("loss", x), val("gf", x), val("ga", x)
            linhas.append({"nome": nome, "j": v + e + d, "v": v, "e": e, "d": d, "gp": gp, "gc": gc,
                           "pts": v * 3 + e + val("adjust_points", x)})
        if len(linhas) >= 2:
            saida.append(linhas)
    return saida


def tabelas(temporada: str) -> list[list[dict]]:
    arq = arquivo(temporada)
    t = arq.read_text(encoding="utf-8") if arq.exists() else ""
    return _sports_table(t) + _wikitable(t)


def _temporada(rot: str) -> str | None:
    m = re.search(r"(\d{4})[–-](\d{2,4})", rot)
    return f"{m.group(1)}/{m.group(2)[-2:]}" if m else None


def campeoes() -> dict[str, str]:
    """Artigo da liga, seção "List of seasons": temporada -> campeão ("" quando não houve: "Not played"/"Not finished")."""
    t = arquivo("liga").read_text(encoding="utf-8")
    t = t[t.find("==List of seasons=="):]
    t = t[:t.find("\n|}")]
    saida = {}
    for r in t.split("\n|-")[1:]:
        cel = [c for c in re.split(r"\n\||\|\|", r) if c.strip()]
        if len(cel) < 2 or not (temp := _temporada(cel[0])):
            continue
        txt = _limpa(cel[1])
        saida[temp] = "" if re.match(r"Not (played|finished)", txt, re.I) else re.sub(r"\s*\(\d+\)\s*$", "", txt)
    return saida


def artilheiros() -> dict[str, list[tuple[str, str, int]]]:
    """Artigo da liga, tabela de artilheiros: temporada -> [(jogador, clube como na Wikipédia, gols)]."""
    t = arquivo("liga").read_text(encoding="utf-8")
    saida: dict[str, list] = {}
    for r in t.split("\n|-"):
        if "flagicon" not in r:
            continue
        cel = [c for c in re.split(r"\n\||\|\|", r) if c.strip()]
        if len(cel) < 4 or not (temp := _temporada(cel[0])) or "Egyptian Premier League" not in cel[0]:
            continue
        jog, clu = _limpa(cel[1]), _limpa(cel[2])
        gols = re.search(r"(\d+)\s*$", _limpa(cel[3]))
        if jog and gols:
            saida.setdefault(temp, []).append((jog, clu, int(gols.group(1))))
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for temp in sys.argv[1:]:
        for tb in tabelas(temp):
            print(temp, len(tb), [(r["nome"], r["j"], r["gp"], r["gc"], r["pts"]) for r in tb][:4])
