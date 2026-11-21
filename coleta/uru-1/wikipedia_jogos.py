"""Jogos da Wikipédia em espanhol (data/coleta/uru-1/wikipedia/es_<ano>.txt), para os anos que a RSSSF não tem.

Lê as tabelas da seção "Fixture" (uma por rodada, "Fecha N", ou uma só com todos os jogos, com data e cancha) e, em 1916,
a "Tabla de resultados" (tabela cruzada: linha = mandante, coluna = visitante). Devolve os jogos na mesma estrutura do
leitor da RSSSF (rsssf_sul.Jogo), com texto "wiki-es_<ano>:<linha>".

Seções que entram: o campeonato (fase única), "Grupo A – Ronda de Campeonato" (fase final), "Grupo B – Ronda de Descenso"
(grupo do rebaixamento), o desempate do título e o da permanência. Ficam de fora o repechaje, a liguilla e as rondas de
ascenso, que juntam clubes da 2ª divisão ou não valem para o título.

Uso: jogos(ano) -> list[Jogo]; python coleta/uru-1/wikipedia_jogos.py <ano> (resumo)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from rsssf_sul import Jogo  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "uru-1" / "wikipedia"
MESES = {m: k for k, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
                                     "octubre", "noviembre", "diciembre"], 1)}


def _fase(titulos: list[str]) -> str | None:
    """Fase pela pilha de títulos de seção; None = fica de fora."""
    t = " / ".join(titulos).lower()
    if re.search(r"repechaje|liguilla|ascenso|clasificación a torneos|equipos clasificados", t):
        return None
    if "ronda de campeonato" in t or "fase de campeonato" in t:
        return "Fase final"
    if "ronda de descenso" in t:
        return "Grupo do rebaixamento"
    if "permanencia" in t:
        return "Desempate do rebaixamento"
    if "desempate" in t or re.search(r"(^|/ )final$", t):
        return "Desempate do título"
    return ""


def _limpa(c: str) -> str:
    c = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]|<ref[^>]*/>|<ref[^>]*>.*?(?:</ref>|$)", " ", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)         # [[alvo|texto]] -> texto
    c = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>", "", c)
    if "|" in c:                                                     # atributos da célula: "bgcolor=#D0E7FF|'''Danubio"
        c = c.split("|")[-1]
    return re.sub(r"\s+", " ", c.replace("'''", "").replace("''", "")).strip()


def _data(txt: str, ano: int) -> str | None:
    if m := re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", txt):
        return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    if (m := re.match(r"(\d{1,2}) de (\w+)", txt)) and m.group(2).lower() in MESES:
        return f"{ano}-{MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    return None


def _placar(txt: str) -> tuple[int | None, int | None, str] | None:
    t = txt.replace("–", "-").replace(":", "-")
    if m := re.match(r"^(\d{1,2})\s*-\s*(\d{1,2})", t):
        return int(m.group(1)), int(m.group(2)), ""
    if re.search(r"\bw\.?/?o\b", t, re.I):
        return None, None, "wo"
    return None


def jogos(ano: int) -> list[Jogo]:
    ls = (PASTA / f"es_{ano}.txt").read_text(encoding="utf-8").splitlines()
    saida: list[Jogo] = []
    titulos: list[str] = []
    em_fixture = em_cruzada = False
    nivel_fix = 0
    rodada = None
    cab: list[str] = []
    celulas: list[tuple[int, str, str]] = []
    colunas: list[str] = []          # tabela cruzada: times das colunas (ordem das linhas)
    linhas_cruz: list[tuple[int, str, list[str]]] = []

    def fecha_linha():
        if not em_fixture or not celulas or not cab or fase is None:
            return
        d = {cab[k]: v for k, (_, v, _) in enumerate(celulas) if k < len(cab)}
        loc, vis, res = d.get("local"), d.get("visitante"), d.get("resultado")
        p = _placar(res or "")
        if not loc or not vis or p is None:
            return
        gm, gv, esp = p
        nota = d.get("notas", "")
        if esp == "wo":   # o vencedor do W.O. vem em destaque (bgcolor)
            k_m, k_v = cab.index("local"), cab.index("visitante")
            esp = "wo_v" if "D0E7FF" in celulas[k_v][2] and "D0E7FF" not in celulas[k_m][2] else "wo_m"
        saida.append(Jogo(linha=celulas[0][0], mandante=loc, visitante=vis, gm=gm, gv=gv, rodada=rodada,
                          data=_data(d.get("fecha", ""), ano), fase=fase, especial=esp, nota=nota,
                          local=d.get("cancha") or d.get("estadio") or None, texto=f"wiki-es_{ano}:{celulas[0][0]}"))

    fase: str | None = ""
    tpl: dict[str, str] | None = None
    for i, l in enumerate(ls):
        s = l.strip()
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*$", s):
            nivel, tit = len(m.group(1)), m.group(2)
            if em_fixture and nivel > nivel_fix:   # "Primera vuelta" dentro do Fixture
                continue
            if tit.lower() == "fixture":           # o Fixture é filho da seção irmã de cima ("Grupo A"), salvo se ela
                em_fixture, nivel_fix = True, nivel   # fica de fora ("Equipos clasificados")
                titulos = titulos[:max(0, nivel - 1)]
                if titulos and _fase(titulos) is None:
                    titulos = titulos[:max(0, nivel - 2)]
            else:
                titulos = titulos[:max(0, nivel - 2)] + [tit]
                em_fixture = False
            em_cruzada = ano == 1916 and tit.lower() == "tabla de resultados"
            fase = _fase(titulos)
            continue
        # jogo avulso ({{Partidos ...}}), nos desempates
        if s.startswith("{{Partidos"):
            tpl = {"_linha": str(i)}
            continue
        if tpl is not None:
            if s.startswith("}}"):
                p = _placar(_limpa(tpl.get("resultado", "")))
                if fase is not None and p and tpl.get("local") and tpl.get("visita"):
                    k = int(tpl["_linha"])
                    saida.append(Jogo(linha=k, mandante=_limpa(tpl["local"]), visitante=_limpa(tpl["visita"]), gm=p[0], gv=p[1],
                                      data=_data(tpl.get("fecha", ""), ano), fase=fase or "Desempate do título",
                                      local=_limpa(tpl.get("estadio", "")) or None, texto=f"wiki-es_{ano}:{k}"))
                tpl = None
            elif mt := re.match(r"^\|\s*(\w+)\s*=\s*(.*)$", s):
                tpl[mt.group(1)] = mt.group(2)
            continue
        if em_cruzada:
            if s.startswith("|'''") or (s.startswith("|[[Archivo") and not linhas_cruz and "align=left" not in s):
                colunas.append(_limpa(s))
            elif "align=left" in s:
                linhas_cruz.append((i, _limpa(s), []))
            elif s.startswith("!") and linhas_cruz:
                linhas_cruz[-1][2].append(s[1:].strip())
            continue
        if not em_fixture:
            continue
        if s.startswith("!") and "colspan" in s:
            rm = re.search(r"Fecha\s+(\d+)", s)
            rodada = int(rm.group(1)) if rm else None
            cab = []
        elif s.startswith("!"):
            cab.append(_limpa(s[1:]).lower())
        elif s.startswith("|-") or s.startswith("|}"):
            fecha_linha()
            celulas = []
        elif s.startswith("|"):
            for c in s[1:].split("||"):
                celulas.append((i, _limpa(c), c))
    if em_cruzada or linhas_cruz:
        for k, (i, mand, res) in enumerate(linhas_cruz):
            for c, r in enumerate(res):
                p = _placar(r)
                if c == k or p is None:
                    continue
                saida.append(Jogo(linha=i, mandante=mand, visitante=linhas_cruz[c][1], gm=p[0], gv=p[1], fase="",
                                  texto=f"wiki-es_{ano}:{i}"))
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:]:
        js = jogos(int(a))
        fases = {}
        for j in js:
            fases[j.fase] = fases.get(j.fase, 0) + 1
        print(a, len(js), "jogos", fases, js[:2])
