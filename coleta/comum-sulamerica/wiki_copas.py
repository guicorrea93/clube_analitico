"""Jogos das copas nacionais na Wikipédia em espanhol, para as fases que a RSSSF não traz (pendência D5, 24/11/2026).

Formato lido aqui (as páginas guardadas em data/coleta/<slug>/wikipedia/es_<edição>.txt):
- tabela com uma célula por linha, uma linha de tabela por jogo (Copa Chile 2013-14, 2014-15, 2015, 2022...):
  "|3 de julio" / "|[[Estadio ...|Nelson Oyarzún]]" / "| align="right" |Ñublense" / "|[url 1 - 3]" / "| align="left" |Temuco".
  O placar é a célula "N - N"; o mandante, a célula com texto antes dela; o visitante, a de depois. A data é a célula
  "3 de julio" (vale para as linhas de baixo com "rowspan"); o grupo, o título "=== Grupo N ===" em vigor.
  "0 - 3|Secretaría" (abbr) e o placar com † ou "Secretaría" viram W.O. (placar dado); "(3 - 2 p.)" são os pênaltis.

Os jogos levam texto "wiki-es_<edição>:<linha>" (o importador comum das copas põe a fonte "Wikipédia (es)").
"""
from __future__ import annotations

import re
from pathlib import Path

from rsssf_sul import Jogo

MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9,
         "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
_PLACAR = re.compile(r"^(\d{1,2})\s*[-–:]\s*(\d{1,2})\b")


def limpa(c: str) -> str:
    """Texto de uma célula, sem atributos, links, imagens, notas, modelos de bandeira e negrito."""
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(</ref>|$)", "", c)
    c = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]", "", c, flags=re.I)
    c = re.sub(r"\{\{[Bb]andera[^{}]*\}\}|\{\{flagbdr[^{}]*\}\}|\{\{Wayback[^{}]*\}\}|\{\{[Ee]nlace roto\|1=", "", c)
    c = re.sub(r"\{\{abbr\|([^|{}]*)\|[^{}]*\}\}", r"\1 (W.O.)", c)   # "{{abbr|0 - 3|Secretaría}}": placar dado
    c = re.sub(r"\{\{small\|([^{}]*)\}\}", r"\1", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\[https?://\S+\s+([^\]]*)\]?", r"\1", c)   # placar dentro de link externo
    c = re.sub(r"https?://\S+", "", c)
    c = re.sub(r"^\s*(?:(?:style|align|bgcolor|rowspan|colspan|width|class)\s*=\s*\"?[^|\"]*\"?\s*)+\|(?!\|)", "", c)
    c = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>|'''?|\}\}|\{\{", "", c)
    return re.sub(r"\s+", " ", c).strip(" |")


def _data(txt: str, anos: tuple[int, int]) -> str | None:
    """"3 de julio" ou "3 de julio de 2013"; sem ano, o 1º ano da edição para os meses a partir de julho... e o 2º para
    os outros, quando a edição cruza o ano (a1 > a0)."""
    m = re.search(r"(\d{1,2}) de ([a-zé]+)(?: de (\d{4}))?", txt.lower())
    if not m or m.group(2) not in MESES:
        return None
    mes = MESES[m.group(2)]
    a0, a1 = anos
    ano = int(m.group(3)) if m.group(3) else (a0 if a1 == a0 or mes >= 7 else a1)
    return f"{ano}-{mes:02d}-{int(m.group(1)):02d}"


def partidos(arquivo: Path, chave: str, fase: str, secoes: dict[str, str] | None = None) -> list[Jogo]:
    """Jogos dos modelos {{Partido|fecha=|local=|resultado=|visita=|estadio=|ciudad=|asistencia=}} (páginas "Anexo:Tercera
    fase de la Copa Chile 2022"...). `secoes` ({regex do título: fase}) troca a fase pelo título em vigor. "2:1 (0:0)" é
    o placar com o intervalo; "1:1 (4:3 p.)" ou o campo "penaltis" dão os pênaltis."""
    ls = ler(arquivo)
    saida: list[Jogo] = []
    fase_v, grupo, i = fase, "", 0
    while i < len(ls):
        s = ls[i].strip()
        if m := re.match(r"^=+\s*(.*?)\s*=+$", s):
            if secoes:   # fase pelo título; None = seção que fica de fora (a RSSSF já traz)
                fase_v = next((f for rx, f in secoes.items() if re.search(rx, m.group(1), re.I)), fase_v)
            if mg := re.match(r"(?i)(?:grupo|zona)\s+(.+)$", m.group(1)):
                grupo = mg.group(1).strip()
        if not s.startswith("{{Partido"):
            i += 1
            continue
        ini, campos, nivel = i, {}, 0
        while i < len(ls):
            t = ls[i]
            nivel += t.count("{{") - t.count("}}")
            if mc := re.match(r"^\s*\|\s*(\w+)\s*=\s*(.*)$", t):
                campos[mc.group(1).lower()] = mc.group(2)
            i += 1
            if nivel <= 0:
                break
        res = limpa(campos.get("resultado", ""))
        mp = re.match(r"^(\d{1,2})\s*[:\-–]\s*(\d{1,2})", res)
        casa, fora = limpa(campos.get("local", "")), limpa(campos.get("visita", ""))
        if not mp or not casa or not fora or fase_v is None:
            continue
        pen_txt = campos.get("penaltis", "") or ""
        pen = (re.search(r"(\d{1,2})\s*[:\-–]\s*(\d{1,2})", limpa(pen_txt)) if pen_txt.strip() else
               re.search(r"\((\d{1,2})\s*[:\-–]\s*(\d{1,2})\s*(?:p|pen)", res))
        if not pen and ("penaltis1" in campos or "penaltis2" in campos):   # cobrança a cobrança: conta os {{pengol}}
            pm, pv = (campos.get(k, "").lower().count("{{pengol") for k in ("penaltis1", "penaltis2"))
            pen = re.match(r"(\d+):(\d+)", f"{pm}:{pv}")
        dt = re.search(r"\{\{fecha\|(\d{1,2})\|(\d{1,2})\|(\d{4})", campos.get("fecha", ""))
        data = f"{dt.group(3)}-{int(dt.group(2)):02d}-{int(dt.group(1)):02d}" if dt else _data(limpa(campos.get("fecha", "")), (0, 0))
        wo = bool(re.search(r"(?i)secretar|w\.?o\.?|walk", res + campos.get("resultado", "")))
        saida.append(Jogo(linha=ini, mandante=casa, visitante=fora, gm=int(mp.group(1)), gv=int(mp.group(2)), data=data,
                          fase=fase_v, grupo=grupo, pen_m=int(pen.group(1)) if pen else None, pen_v=int(pen.group(2)) if pen else None,
                          especial="wo" if wo else "", nota=f"awarded {mp.group(1)}-{mp.group(2)}" if wo else "",
                          local=limpa(campos.get("estadio", "")) or None, texto=f"wiki-es_{chave}:{ini}"))
    return saida


def tabela_modulo(arquivo: Path, chave: str, secao_ini: str, secao_fim: str, fase: str) -> list[Jogo]:
    """Jogos dos grupos no módulo {{#invoke:Football table|main ...}}: "|nombre_MET=[[...|Metropolitanos]]" e a matriz
    "|partido_MET_CAR=2-1" (MET em casa). Sem data; o grupo é o título "=== Grupo A ===" (ou "Zona A") em vigor."""
    ls = ler(arquivo)
    saida: list[Jogo] = []
    dentro, grupo, nomes = False, "", {}
    for i, l in enumerate(ls):
        s = l.strip()
        if m := re.match(r"^(=+)\s*(.*?)\s*=+$", s):
            tit = m.group(2)
            if re.search(secao_ini, tit, re.I):
                dentro = True
            elif dentro and re.search(secao_fim, tit, re.I):
                dentro = False
            if mg := re.match(r"(?i)(?:grupo|zona)\s+([A-Z0-9]{1,2})\b", tit):
                grupo, nomes = mg.group(1).upper(), {}
            continue
        if not dentro:
            continue
        for mn in re.finditer(r"\|\s*nombre_(\w+?)\s*=\s*(.*?)(?=\s*\|\s*\w+_\w+\s*=|$)", s):
            nomes[mn.group(1)] = limpa(mn.group(2))
        for mp in re.finditer(r"\|\s*partido_(\w+?)_(\w+?)\s*=\s*(\d{1,2})\s*[-–]\s*(\d{1,2})", s):
            a, b = nomes.get(mp.group(1)), nomes.get(mp.group(2))
            if a and b:
                saida.append(Jogo(linha=i, mandante=a, visitante=b, gm=int(mp.group(3)), gv=int(mp.group(4)), fase=fase,
                                  grupo=grupo, texto=f"wiki-es_{chave}:{i}"))
    return saida


def ler(arquivo: Path) -> list[str]:
    return arquivo.read_text(encoding="utf-8").splitlines()


def tabela_jogos(arquivo: Path, chave: str, secao_ini: str, secao_fim: str, fase: str, anos: tuple[int, int],
                 grupos: bool = True) -> list[Jogo]:
    """Jogos das tabelas de uma célula por linha entre o título `secao_ini` e o `secao_fim` (regex do texto do título)."""
    ls = ler(arquivo)
    saida: list[Jogo] = []
    dentro, grupo, data_rowspan = False, "", None
    celulas: list[tuple[int, str]] = []

    def fecha():
        nonlocal celulas, data_rowspan
        cel = [(k, limpa(c)) for k, c in celulas]
        celulas = []
        if not dentro:
            return
        datas = [d for _, c in cel if (d := _data(c, anos))]
        if datas:
            data_rowspan = datas[0]
        for n, (k, c) in enumerate(cel):
            if not (mp := _PLACAR.match(c)):
                continue
            antes = [x for _, x in cel[:n] if x and not _data(x, anos) and not re.fullmatch(r"[\d:hs. ]+", x)]
            depois = [x for _, x in cel[n + 1:] if x]
            if not antes or not depois:
                return
            casa, fora = antes[-1], depois[0]
            fora = re.sub(r"\s*[†‡]\s*$", "", fora)
            casa = re.sub(r"\s*[†‡]\s*$", "", casa)
            pen = re.search(r"\((\d{1,2})\s*[-–:]\s*(\d{1,2})\s*(?:p|pen)", c)
            wo = "W.O." in c or "Secretar" in c
            gm, gv, nota = int(mp.group(1)), int(mp.group(2)), ""
            # "1 - 0 (0 - 3)": jogado 1-0, placar dado 0-3 (Copa Chile 2014-15, perda de pontos por excesso de estrangeiros)
            if (dado := re.match(r"^\d{1,2}\s*[-–]\s*\d{1,2}\s*\((\d{1,2})\s*[-–]\s*(\d{1,2})\)(?!\s*(?:p|pen))", c)):
                wo, nota = True, f"awarded {dado.group(1)}-{dado.group(2)} (jogado {gm}-{gv}; placar dado fora de campo)"
            elif wo:
                nota = f"awarded {gm}-{gv}"
            saida.append(Jogo(linha=k, mandante=casa, visitante=fora, gm=gm, gv=gv,
                              data=datas[0] if datas else data_rowspan, fase=fase, grupo=grupo if grupos else "",
                              pen_m=int(pen.group(1)) if pen else None, pen_v=int(pen.group(2)) if pen else None,
                              especial="wo" if wo else "", nota=nota, texto=f"wiki-es_{chave}:{k}"))
            return

    for i, l in enumerate(ls):
        s = l.strip()
        if m := re.match(r"^(=+)\s*(.*?)\s*=+$", s):
            fecha()
            tit = m.group(2)
            if re.search(secao_ini, tit, re.I):
                dentro = True
            elif dentro and re.search(secao_fim, tit, re.I):
                dentro = False
            if mg := re.match(r"(?i)grupo\s+([A-Z0-9]{1,2})\b", tit):
                grupo = mg.group(1).upper()
            continue
        if s.startswith("|-") or s.startswith("|}") or s.startswith("{|"):
            fecha()
            continue
        if not dentro:
            continue
        if s.startswith("|") and not s.startswith("|+"):
            celulas += [(i, c) for c in re.split(r"\|\|", s[1:])]
        elif s.startswith("!"):
            continue
        elif celulas and s:   # célula que continua na linha de baixo (link quebrado)
            celulas[-1] = (celulas[-1][0], celulas[-1][1] + " " + s)
    fecha()
    return saida
