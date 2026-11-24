"""Jogos da Copa Colombia na Wikipédia em espanhol ("Copa Colombia <ano>", guardadas em data/coleta/col-copa/wikipedia/es_<ano>.txt),
para o que a RSSSF não tem (só as tabelas dos grupos, ou só do mata-mata em diante):

- grupos(ano): fase de grupos em linhas "Local || placar || Visitante" (2011-2014), com a data e a "Fecha N" das linhas
  de cima e o grupo do título "=== Grupo A ===";
- llaves(ano, secoes): fases de ida e volta em tabela de llaves (Fecha, Local ida, Global, Local vuelta, Ida, Vuelta; 2024):
  a ida é A x B e a volta B x A; os dois placares vêm do ponto de vista de A (Fortaleza 3:1 e 0:3 contra o Pereira = 3:4);
- wiki(ano, fases): os do leitor do col-1 (coleta/col-1/wikipedia_jogos.py: modelos {{Partido}} e listas), só das fases
  pedidas (grupos de 2015-2017, 2019 e a 1ª fase de 2025).

Os jogos levam texto "wiki-es_<ano>:<linha>" (o importador comum põe a fonte "Wikipédia (es)").
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PASTA = AQUI.parent.parent / "data" / "coleta" / "col-copa" / "wikipedia"
sys.path.insert(1, str(AQUI.parent / "col-1"))
import wikipedia_jogos  # noqa: E402  (o do col-1)
from rsssf_sul import Jogo  # noqa: E402

MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9,
         "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
_PLACAR = re.compile(r"^(\d{1,2})\s*[:\-–]\s*(\d{1,2})$")


def _limpa(c: str) -> str:
    """Célula sem atributos ("bgcolor=#D0E7FF|'''1: 1" -> "1: 1"), notas, links, bandeiras e negrito."""
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\{\{[Rr]efn\|.*?\}\}|\{\{[Bb]andera2?\|[^{}]*\}\}|\{\{nowrap\|", "", c)   # notas {{Refn|...}} (2012)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", c)   # placar dentro de link externo (2014)
    c = re.sub(r"^\s*(?:[a-z\-]+\s*=\s*\"?[^|\"]*\"?\s*)+\|(?!\|)", "", c)   # atributos antes do 1º "|"
    c = re.sub(r"<[^>]+>|'''?|\}\}", "", c)
    return re.sub(r"\s+", " ", c).strip(" |")


def _data(txt: str, ano: int) -> str | None:
    """"13 de febrero", "6/7 de marzo" (o 1º dia)."""
    m = re.match(r"^(\d{1,2})(?:/\d{1,2})? de ([a-zé]+)", txt.strip().lower())
    if m and m.group(2) in MESES:
        return f"{ano}-{MESES[m.group(2)]:02d}-{int(m.group(1)):02d}"
    return None


def _ls(ano: int) -> list[str]:
    return (PASTA / f"es_{ano}.txt").read_text(encoding="utf-8").splitlines()


def grupos(ano: int) -> list[Jogo]:
    ls = _ls(ano)
    saida: list[Jogo] = []
    dentro, grupo, data, rodada = False, "", None, None
    for i, l in enumerate(ls):
        s = l.strip()
        if m := re.match(r"^(=+)\s*(.*?)\s*=+$", s):
            n, tit = len(m.group(1)), m.group(2)
            if n == 2:
                dentro = bool(re.search(r"(?i)fase de grupos|primera fase", tit))
                grupo = ""
            elif mg := re.match(r"(?i)grupo ([A-Z])\b", tit):
                grupo, data, rodada = mg.group(1).upper(), None, None
            elif n == 3:
                grupo = ""
            continue
        if not dentro or not grupo or not s.startswith("|") or s.startswith(("|-", "|}", "|+")):
            continue
        if mf := re.search(r"\|\s*Fecha (\d+)\]\]", s):
            rodada = int(mf.group(1))
            continue
        cel = [_limpa(c) for c in s[1:].split("||")]
        if len(cel) == 1 and (d := _data(cel[0], ano)):
            data = d
            continue
        for k in range(len(cel) - 2):
            mp = re.match(r"^(\d{1,2})\s*[:\-–]\s*(\d{1,2})(\s*\(?W\.?\s*O\.?\)?)?$", cel[k + 1])
            if mp and cel[k] and cel[k + 2] and not cel[k][:1].isdigit() and not cel[k + 2][:1].isdigit():
                wo = bool(mp.group(3))   # "0: 3 (W.O.)": placar dado
                saida.append(Jogo(linha=i, mandante=cel[k], visitante=cel[k + 2], gm=int(mp.group(1)), gv=int(mp.group(2)),
                                  rodada=rodada, data=data, fase="Fase de grupos", grupo=grupo, texto=f"wiki-es_{ano}:{i}",
                                  especial="wo" if wo else "", nota=f"awarded {mp.group(1)}-{mp.group(2)}" if wo else ""))
    return saida


def llaves(ano: int, secoes: dict[str, str]) -> list[Jogo]:
    """Tabelas de llaves das seções pedidas ({"Fase I": "Fase I", ...}: título da seção -> nome da fase)."""
    ls = _ls(ano)
    saida: list[Jogo] = []
    fase = None
    celulas: list[tuple[int, str]] = []

    def fecha_linha():
        nonlocal celulas
        cel = [c for _, c in celulas]
        if fase and len(cel) >= 6 and (g := re.match(r"^(\d{1,2})\s*[:\-–]\s*(\d{1,2})", cel[2])) and (ida := _PLACAR.match(cel[4])) and (
                vta := _PLACAR.match(cel[5])) and cel[1] and cel[3]:
            if dd := re.match(r"(\d{1,2}) y (\d{1,2}) de ([a-zé]+)", cel[0].lower()):   # "7 y 20 de marzo"
                d1, d2 = _data(f"{dd.group(1)} de {dd.group(3)}", ano), _data(f"{dd.group(2)} de {dd.group(3)}", ano)
            else:   # "22 de febrero y 14 de marzo"
                datas = re.findall(r"(\d{1,2}) de ([a-zé]+)", cel[0].lower())
                d1 = _data(f"{datas[0][0]} de {datas[0][1]}", ano) if datas else None
                d2 = _data(f"{datas[-1][0]} de {datas[-1][1]}", ano) if len(datas) > 1 else None
            pen = re.search(r"\((\d{1,2})\s*[:\-–]\s*(\d{1,2})\s*(?:p|pen)", " ".join(cel), re.I)
            k = celulas[0][0]
            saida.append(Jogo(linha=k, mandante=cel[1], visitante=cel[3], gm=int(ida.group(1)), gv=int(ida.group(2)), data=d1,
                              fase=fase, texto=f"wiki-es_{ano}:{k}"))
            saida.append(Jogo(linha=k, mandante=cel[3], visitante=cel[1], gm=int(vta.group(2)), gv=int(vta.group(1)), data=d2,
                              fase=fase, pen_m=int(pen.group(2)) if pen else None, pen_v=int(pen.group(1)) if pen else None,
                              texto=f"wiki-es_{ano}:{k}"))
        celulas = []

    for i, l in enumerate(ls):
        s = l.strip()
        if m := re.match(r"^(=+)\s*(.*?)\s*=+$", s):
            fecha_linha()
            fase = secoes.get(m.group(2).strip())
            continue
        if s.startswith("|-") or s.startswith("|}") or s.startswith("{|"):
            fecha_linha()
            continue
        if fase and s.startswith(("|", "!")):
            celulas += [(i, _limpa(c)) for c in re.split(r"\|\||!!", s[1:])]
    fecha_linha()
    return saida


def wiki(ano: int, fases: set[str]) -> list[Jogo]:
    """Jogos do leitor do col-1 nas fases pedidas ("Fase de grupos", "Primera fase"...)."""
    wikipedia_jogos.PASTA = PASTA
    js = [j for j in wikipedia_jogos.jogos(str(ano)) if j.fase in fases]
    for j in js:
        j.texto = re.sub(r"^wiki-es_\w+:", f"wiki-es_{ano}:", j.texto)
    return js
