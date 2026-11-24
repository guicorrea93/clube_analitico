"""Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/mex-1/rsssf/) com o leitor comum (rsssf_concacaf); os jogos
que a página não tem vêm da ESPN (espn_jogos).

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/mex-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
sys.path.insert(0, str(AQUI))
import rsssf_concacaf  # noqa: E402
from rsssf_concacaf import chave  # noqa: E402

from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira que casa vale); vale para todas as edições
# fim de título de fase: a linha inteira (a nota que quebra a linha não vale)
_FIM = r"\s*:?\s*(\[[^\]]*\])?$"
FASES = [
    (r"^(Relegation [Pp]lay-?offs?( series)?|Relegation Playoff|Playoff Descenso|Relegation (Final|Semi-?finals?|Second Legs?))" + _FIM,
     "Playoff do rebaixamento"),
    (r"^Championship [Pp]layoffs?\s+Semi-?finals?" + _FIM, "Semifinal"),
    (r"^Playoff match for the second place" + _FIM, "Desempate do 2º lugar"),
    (r"^(Reclasificaci[oó]n( \(over one leg\))?|Repechaje( Round| \(Qualifying Playoffs?\))?|Qualifying (Round|Playoff) \((Repechaje|Repesca)\)|"
     r"Preliminary Round \(Repechaje\)( \(over one leg\))?|Qualifying Playoffs?)" + _FIM, "Repescagem"),
    (r"^(Quarterfinal (stage|Group Stage)( \(round robin\))?)" + _FIM, "Quadrangulares das quartas"),
    (r"^(Semifinal (Group|Stage)( Phase| Stage)?|Semifinal Group Phase)" + _FIM, "Grupos semifinais"),
    (r"^(Quarter[- ]?finals?)" + _FIM, "Quartas de final"),
    (r"^(Semi[- ]?finals?)" + _FIM, "Semifinal"),
    (r"^(Final (Group|Round|Phase|Stage))" + _FIM, "Grupo final"),
    (r"^(Championship )?Finals?" + _FIM, "Final"),
    (r"^(Playoff( series| match)?|Extra match|Title Playoff|Tie-?breaker|Decisive Match|Second playoff|Second replay|"
     r"1st Playoff|2nd Playoff)" + _FIM, "Desempate do título"),
    (r"^(Championship [Pp]layoffs?|Playoffs?( \(Liguilla\))?|Liguilla|Playoff Stage)" + _FIM, "Liguilla"),
    (r"^(First (Phase|Stage)|Regular [Ss]eason.*|(\d{4}[-/]\d{2} )?Regular Season.*|Regular Stage)" + _FIM, ""),
    (r"^(Second (Phase|Stage))" + _FIM, "Segunda fase"),
]

# título que abre o campeonato numa página que começa por outra competição (os trechos já dizem onde começa)
INICIO = r"^NUNCA$"

# torneios dentro da edição (não há: cada torneio do ano é uma edição)
TORNEIOS: list[tuple[str, str]] = []
FECHA = r"^NUNCA$"

# grupos marcados por título ("Group A", "Grupo 1"); "Championship Group" / "Consolation Group" (México 70)
_GRUPO = r"^(?:Grupo|Group)\s+[“\"]?([A-Z0-9]\w*)\b(?!\s*\()"

# páginas de colunas fixas: (início da coluna do visitante, início da coluna do placar)
COLUNAS: dict[str, tuple[int, int]] = {}


_CP437 = str.maketrans({"‚": "é", "¢": "ó", "¡": "í", "£": "ú", "¤": "ñ", "": "é", "¢": "ó"})


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    # travessão no placar ("2–0") em parte das páginas: vira hífen
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_concacaf.texto(PASTA / f"{pagina}.html")]
    # páginas com acentos da página de código 437 ("Am‚rica", "Cat¢lica"): voltam ao acento
    ls = [l.translate(_CP437) for l in ls]
    # a página de 2011/12 está em UTF-16: cada letra vem com um caractere nulo
    ls = [l.replace("\x00", "") for l in ls]
    # "Club México  unk Morelos": resultado desconhecido (fica de fora); "Asturias  –  Tranvías [Asturias won]": venceu sem
    # placar conhecido -> W.O. para quem venceu (como a tabela conta)
    ls = [re.sub(r"^(\S.*?)\s+-\s+(\S.*?)\s+\[(.+?) won\]\s*$",
                 lambda m: f"{m.group(1)}  {'w-l' if chave(m.group(3)).split()[0] in chave(m.group(1)) else 'l-w'}  {m.group(2)}"
                 if chave(m.group(3)).split()[0] in chave(m.group(1)) + ' ' + chave(m.group(2)) else m.group(0), l) for l in ls]
    # "Penalty shootout:" seguido das cobranças, uma por linha ("Antonio Taboada   1-0  Juan Pablo Rodriguez  1-1"): o bloco
    # inteiro sai (a disputa já está na nota do jogo)
    ls, k = list(ls), 0
    while k < len(ls):
        if re.match(r"^\s*Penalty shoot-?outs?:?\s*$", ls[k], re.I):
            ls[k], k, viu = "", k + 1, False
            while k < len(ls) and (ls[k].strip() or not viu):
                viu = viu or bool(ls[k].strip())
                ls[k], k = "", k + 1
        k += 1
    # depois de "Relegation playoffs", os títulos "Semifinals" / "Final" são do playoff do rebaixamento, não do título
    rebaix = False
    for k, l in enumerate(ls):
        s = l.strip()
        if re.match(r"^Relegation [Pp]lay-?offs?\b", s):
            rebaix = True
        elif re.match(r"^(Championship|Liguilla|Playoffs?\b|Copa |Changes|Campe)", s):
            rebaix = False
        elif rebaix and re.fullmatch(r"(Semi-?finals?|Finals?|Second Legs?)(\s*\[.*\])?:?", s):
            ls[k] = "Relegation " + s
    # "[suspended at 87' by pitch invasion; result stood]": o placar valeu; não é jogo suspenso que se repetiu depois (o leitor
    # comum marcaria como abandonado ao achar o mesmo par mais adiante, na liguilla)
    ls = [l.replace("suspended", "stopped").replace("abandoned at", "stopped at")
          if re.search(r"result (stood|stands)|score (stood|stands)", l) else l for l in ls]
    # "A.D.O.   -  San Sebastián [... awarded match to San Sebastián 0-1*]": jogo sem placar decidido fora de campo
    ls = [re.sub(r"^(\S.*?\S)\s+-\s+(\S.*?\[[^\]]*award)", r"\1  awd  \2", l) for l in ls]
    # gols depois de cada nome ("Guadalajara 4 León 0": México 70 inteiro, a última rodada de 1995/96...): volta ao formato de
    # sempre
    if True:
        ls = [re.sub(r"^([A-ZÁÉÍÓÚ][^\d\[]*?)\s+(\d{1,2})\s+([A-ZÁÉÍÓÚ][^\d\[]*?)\s+(\d{1,2})(\s+\[.*\]|\s+\(.*\))?\s*$",
                     r"\1  \2-\4  \3\5", l) for l in ls]
    # placar do 1º tempo entre parênteses logo depois do placar ("Reforma AC   3-1 (1-0) British Popo", 1910/11): sai
    ls = [re.sub(r"(\s\d{1,2}-\d{1,2})\s+\(\d{1,2}-\d{1,2}\)\s+(?=[A-Z])", r"\1  ", l) for l in ls]
    # tabelas com a coluna de saldo com sinal ("21  12  +9  10"): o sinal sai (o leitor comum confere o saldo)
    ls = [re.sub(r"(?<=\d)(\s+)[+-](\d{1,3})(?=\s+\d{1,3}\b)", r"\1\2", l) if re.match(r"^\s*\d{1,2}\.\s", l) else l for l in ls]
    # "Championship Group" / "Consolation Group" (México 70): grupos da segunda fase
    ls = [re.sub(r"^(Championship|Consolation) Group\b", lambda m: f"Group {'Campeonato' if m.group(1) == 'Championship' else 'Consolação'}", l)
          for l in ls]
    if pagina in COLUNAS:
        a, b = COLUNAS[pagina]
        for k, l in enumerate(ls):
            if len(l) > b and re.search(r"\s\d{1,2}-\d{1,2}\s*$", l) and l[a - 1] == " " and l[a] != " " and not rsssf_concacaf.linha_tabela(l):
                ls[k] = f"{l[:a].rstrip()}  {l[a:b].rstrip()}  {l[b:].strip()}"
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    return tuple(ls)


def fim_padrao(ls: tuple[str, ...], ini: int) -> int:
    """Primeira linha, depois do primeiro jogo do trecho, que abre outra competição."""
    viu_jogo = False
    for i in range(ini, len(ls)):
        s = ls[i].strip()
        if not viu_jogo:
            viu_jogo = bool(rsssf_concacaf._jogo(ls[i])) or bool(_CELULAS.search(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


_CELULA = r"(?:[xX]{3}|\d{1,2}[-*]\d{1,2}|---)"
_CELULAS = re.compile(rf"^(?P<nome>\S.*?|)\s+(?P<cel>{_CELULA}(?:\s+{_CELULA}){{1,}})\s*$")


_IDA_VOLTA = re.compile(r"^(\S.*?)\s+(\d{1,2})-(\d{1,2})\s+(\d{1,2})-(\d{1,2})\s+([^\d\s\[].*?)(\s+\[.*)?\s*\.?\s*$")


def confrontos(ls: list[str], ini: int, fim: int) -> tuple[list[tuple[int, str, str, int, int, bool]], set[int]]:
    """Tabelas de confrontos do trecho: [(linha, mandante, visitante, gm, gv, dado)] e as linhas que fazem parte delas.
    Cabeçalho "Cross-Table", linha de siglas e uma linha por clube (mandante) com uma célula por adversário, na ordem das
    linhas (a diagonal é "xxx"). Linha sem nome: segundo turno do clube de cima, em casa de novo. "0*2": placar dado fora
    de campo (dado=True)."""
    jogos, usadas = [], set()
    i = ini
    while i < fim:
        if not re.match(r"^\s*Cross-?Table", ls[i], re.I):
            i += 1
            continue
        usadas.add(i)
        if len(ls[i].split()) > 1:   # "Crosstable        Bol Des Wil Ori SJo": as siglas na mesma linha do título
            k = i + 1
        else:
            k = i + 1
            while k < fim and not ls[k].strip():
                k += 1
            usadas.add(k)   # linha das siglas
            k += 1
        linhas_m: list[tuple[int, str, list[str]]] = []
        while k < fim and (m := _CELULAS.match(ls[k].replace("\t", "    "))):
            nome = m.group("nome").strip() or (linhas_m[-1][1] if linhas_m else "")
            linhas_m.append((k, nome, m.group("cel").split()))
            usadas.add(k)
            k += 1
        clubes = list(dict.fromkeys(n for _, n, _ in linhas_m))
        for linha, casa, cels in linhas_m:
            assert len(cels) == len(clubes), f"tabela de confrontos com {len(cels)} colunas e {len(clubes)} clubes: linha {linha}"
            for fora, c in zip(clubes, cels):
                if (mm := re.fullmatch(r"(\d{1,2})([-*])(\d{1,2})", c)) and fora != casa:
                    jogos.append((linha, casa, fora, int(mm.group(1)), int(mm.group(3)), mm.group(2) == "*"))
        i = k
    return jogos, usadas


def _torneios(ls: tuple[str, ...], ini: int, fim: int, fases: list[tuple[str, str]]
              ) -> tuple[dict[int, str], dict[int, str], dict[int, bool], dict[int, str]]:
    """Por linha: o torneio em vigor ("" = campeonato), o grupo marcado em título, se a fase de mata-mata lida antes ficou
    velha (título de fase anterior ao começo do torneio em vigor) e a fase do último título."""
    torneio, grupo, fase = "", "", ""
    ini_t, ult_fase = -1, -1
    por_linha, grupos, velha, ult = {}, {}, {}, {}
    for i in range(ini, fim):
        s = ls[i].strip()
        if re.match(FECHA + _FIM, s, re.I):   # a linha inteira (não a nota "...qualify for / Hexagonal Final.")
            torneio, grupo, ini_t = "", "", i
        else:
            for rx, nome in TORNEIOS:
                if re.match(rx, s, re.I):
                    torneio, grupo, ini_t = nome, "", i
                    break
        if (f := next((nome for rx, nome in fases if re.search(rx, s, re.I)), None)) is not None:
            ult_fase, grupo, fase = i, "", f   # fase nova: o grupo da fase anterior não vale mais
        if m := re.match(_GRUPO, s):
            grupo = m.group(1)
        por_linha[i], grupos[i], velha[i], ult[i] = torneio, grupo, ult_fase < ini_t, fase
    return por_linha, grupos, velha, ult


def _vitoria_dada(x: rsssf_concacaf.Jogo) -> None:
    """"[awarded 3-0 win to Barcelona because ...]": pontos para um lado. Vira W.O. (wo_m/wo_v) com o placar de campo, como a
    tabela conta."""
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(\d{1,2})\s*-\s*(\d{1,2}) to \w", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))
        return
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(?:\(\*+\))?\s*\[?\s*(\d{1,2})\s*-\s*(\d{1,2})\s*\]", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))
        return
    if re.search(r"award(ed)? of (a )?win to .{2,40}? annulled", x.nota, re.I):   # a decisão caiu: vale o placar de campo
        x.especial = "" if x.gm is not None else x.especial
        return
    # "[awarded to Santa Cruz (originally 0-0) as ...]" (1999): pontos para um lado, gols do campo
    m = re.search(r"(?:awarded (?:(\d{1,2})\s*-\s*(\d{1,2}) )?(?:a )?win to|win awarded to|(?<!points )awarded to(?= [^(]{2,30}\(originally))\s+(.+?)"
                  r"(?:\s+(?:as|because|since|for|after|due|with)\b|\s*\(|[;,.\]]|$)", x.nota, re.I)
    if not m:
        return
    from difflib import SequenceMatcher
    quem = [w for w in rsssf_concacaf.chave(m.group(3)).split() if len(w) > 3]   # "Santa Cruz" x "Real Sta Cruz"; "Gaubira"
    parece = lambda nome: any(SequenceMatcher(None, a, b).ratio() >= 0.75 for a in quem
                              for b in rsssf_concacaf.chave(nome).split() if len(b) > 3)
    casa, fora = parece(x.mandante), parece(x.visitante)
    if casa == fora:
        return
    if m.group(1):
        x.gm, x.gv = int(m.group(1)), int(m.group(2))
    elif x.gm is None and (mo := re.search(r"originally (\d{1,2})\s*-\s*(\d{1,2})", x.nota, re.I)):
        x.gm, x.gv = int(mo.group(1)), int(mo.group(2))
    x.gm_of = x.gv_of = None
    x.especial = "wo_m" if casa else "wo_v"


def _dado_a(x: rsssf_concacaf.Jogo) -> None:
    """"[postponed and then awarded to San Pedro]", "[match awarded to Reforma]", "[awarded match to San Sebastián 0-1]": jogo
    decidido fora de campo a favor de um lado. Com placar na nota, o leitor comum já pôs o placar oficial; sem placar, vira
    W.O. (vitória sem gols, como a tabela conta)."""
    if x.especial not in ("awd", "") or x.gm_of is not None or x.gm is not None:
        return
    m = re.search(r"awarded (?:the )?(?:match |game |points )?to ([^\]\d;,(]+)", x.nota, re.I)
    if not m:
        return
    quem = [w for w in chave(m.group(1)).split() if len(w) > 2 and w not in ("club", "the")]
    casa = any(w in chave(x.mandante).split() for w in quem)
    fora = any(w in chave(x.visitante).split() for w in quem)
    if casa != fora:
        x.especial = "wo_m" if casa else "wo_v"


def _fase(base: str, torneio: str) -> str:
    if not torneio:
        return base
    if base == "":
        return torneio
    if base in ("Final", "Desempate do título"):
        return f"Final do {torneio}"
    if base in ("Semifinal", "Quartas de final", "Oitavas de final", "Fase final", "Segunda fase", "Liguillas",
                "Grupo do rebaixamento"):   # 1995-2002: fases do Apertura e do Clausura do ano
        return f"{base} do {torneio}"
    return base


# fases em que o título "Liguilla B" / "Group A" marca o grupo dos jogos e das tabelas que vêm depois
COM_GRUPO = ("", "Apertura", "Clausura", "Finalización", "Liguillas", "Fase final", "Segunda fase", "Terceira fase",
             "Grupo do rebaixamento")


def ler(e: Edicao) -> tuple[list[rsssf_concacaf.Jogo], list[rsssf_concacaf.Tabela]]:
    jogos, tabelas = [], []
    externos = espn_jogos(*e.espn) if e.espn is not None else []
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
        if ini == 0:   # a página abre com outra competição: o campeonato começa no título dele
            ini = next((i for i, l in enumerate(ls) if re.match(INICIO, l.strip())), 0)
        fim = fim if fim is not None else fim_padrao(ls, ini)
        cruz, usadas = confrontos(list(ls), ini, fim)
        # ida e volta numa linha só ("Oriente Petrolero  1-0 0-4 Bolívar"): os gols do primeiro clube vêm primeiro nos dois
        # placares; a volta é na casa do segundo (presumido). A linha vira a ida, e a volta entra como jogo à parte
        voltas = {}
        trecho = [""] * ini
        for i, l in enumerate(ls[ini:fim], ini):
            if i in usadas:
                trecho.append("")
            elif m := _IDA_VOLTA.match(l):
                trecho.append(f"{m.group(1)}  {m.group(2)}-{m.group(3)}  {m.group(6)}{m.group(7) or ''}")
                voltas[i] = (m.group(6), m.group(1), int(m.group(5)), int(m.group(4)))
            else:
                trecho.append(l)
        j, t = rsssf_concacaf.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for x in [x for x in j if x.linha in voltas]:
            casa, fora, gm, gv = voltas[x.linha]
            j.append(rsssf_concacaf.Jogo(x.linha, casa, fora, gm, gv, None, None, x.secao, x.fase, x.grupo, "",
                                    "ida e volta numa linha só; mando da volta presumido", None, texto=x.texto))
            x.nota = (x.nota + "; ida e volta numa linha só").strip("; ")
        for linha, casa, fora, gm, gv, dado in cruz:   # fase e grupo: os da tabela que vem logo depois da tabela de confrontos
            tab = next((x for x in t if x.linha > linha), None)
            x = rsssf_concacaf.Jogo(linha, casa, fora, gm, gv, None, None, "", tab.fase if tab else "", tab.grupo if tab else "",
                               "", "", None, texto=ls[linha].strip())
            if dado:   # placar dado fora de campo; o de campo, quando a nota da página diz, entra em explicacoes.CORRIGE
                x.gm = x.gv = None
                x.gm_of, x.gv_of, x.especial = gm, gv, "awd"
            j.append(x)
        j.sort(key=lambda x: x.linha)
        tor, gru, velha, ult = _torneios(ls, ini, fim, e.fases + FASES)
        if re.search(r"(Apertura|Clausura|Adecuación)$", e.temporada):   # a edição já é o torneio: o título não vira fase
            tor = {}
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            _vitoria_dada(x)
            _dado_a(x)
            if not x.fase and ult.get(x.linha, "").startswith("Desempate"):
                x.fase = ult[x.linha]   # desempate com "Round 1", "Round 2": o leitor comum volta à fase de liga a cada rodada
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            if not x.grupo and gru.get(x.linha) and x.fase in COM_GRUPO:
                x.grupo = gru[x.linha]
        for x in t:
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            x.grupo = x.grupo or (gru.get(x.linha, "") if x.fase in COM_GRUPO else "")
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final
        ls = linhas(pagina)
        tabelas += rsssf_concacaf.ler([""] * ini + list(ls[ini:fim]), e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.wiki is not None:
        import wikipedia_jogos
        jogos += wikipedia_jogos.jogos(e.wiki)
    if externos:   # a ESPN também traz jogos que a página tem: dela, só os que a página não tem (mesmo par até 3 dias antes ou depois)
        from clubes_mex import clube
        par = lambda x: frozenset((clube(x.mandante, e.ano_inicio), clube(x.visitante, e.ano_inicio)))
        dia = lambda d: datetime.strptime(d[:10], "%Y-%m-%d")
        na_pagina = [(par(x), dia(x.data)) for x in jogos if x.data]
        externos = [x for x in externos if not any(p == par(x) and abs((d - dia(x.data)).days) <= 3 for p, d in na_pagina)]
        for x in externos:
            for d0, f in e.espn_fases:
                if x.data >= d0 and f != "*":
                    x.fase = f
                elif x.data >= d0:   # a fase da tabela da página que tem os dois clubes (Hexagonal 1 e 2, rebaixamento)
                    dupla = {clube(x.mandante, e.ano_inicio), clube(x.visitante, e.ano_inicio)}
                    t = next((t for t in tabelas if t.fase and dupla <= {clube(r["nome"], e.ano_inicio) for r in t.linhas}), None)
                    x.fase = t.fase if t else x.fase
        jogos = externos + jogos
    return jogos, tabelas


_TORNEIO_LISTA = {"Winter": "Invierno", "Summer": "Verano", "Apert.": "Apertura", "Claus.": "Clausura"}


def _lista() -> list[tuple[str, str, str]]:
    """mexchamp.html: [(temporada, campeão, vice)] nos nomes das edições ("1920/21 Liga Nacional", "1970 México 70",
    "1996 Invierno", "2003 Clausura"). Colunas fixas: campeão e vice começam onde o cabeçalho diz (era amadora: colunas 9 e
    41; profissional: 9 e 28). Temporada cancelada ("cancelled", "abandoned") fica sem campeão."""
    saida = []
    ls = linhas("mexchamp")
    col_c, col_v = 9, 41
    temp = None
    for l in ls:
        if l.startswith("SEASON") and "RUNNER-UP" in l:
            col_c, col_v = l.index("CHAMPION"), l.index("RUNNER-UP")
            continue
        m = re.match(r"^(\d{4})-(\d{2})\s*$", l)
        if m:   # "1996-97" sozinho: os torneios vêm nas linhas de baixo
            temp = int(m.group(1))
            continue
        m = re.match(r"^\s*(Winter|Summer|Apert\.|Claus\.)\s", l)
        if m and temp:
            tor = _TORNEIO_LISTA[m.group(1)]
            ano = temp if tor in ("Invierno", "Apertura") else temp + 1
            t_ = f"{ano} {tor}"
        elif m := re.match(r"^(\d{4})-(\d{2})\s", l):
            t_ = f"{m.group(1)}/{m.group(2)}"
            temp = None
        elif m := re.match(r"^(M[ée]xico 70|Prode 85|M[ée]xico 86)\s", l):
            t_ = {"Prode 85": "1985 Prode 85"}.get(m.group(1), "1970 México 70" if "70" in m.group(1) else "1986 México 86")
        elif re.match(r"^\s{9}\S", l) and saida and re.search(r"\(Liga (Mexicana|Nacional)\)", l):
            t_ = saida[-1][0].split()[0]   # 2ª liga do mesmo ano (1920-21, 1921-22)
        else:
            continue
        camp = l[col_c:col_v].strip()
        vice = l[col_v:col_v + (19 if col_v < 30 else 32)].strip()
        if re.search(r"cancelled|abandoned", camp, re.I):
            saida.append((t_, "", ""))
            continue
        if (mm := re.search(r"\(Liga (Mexicana|Nacional)\)", camp)):
            t_ = f"{t_.split()[0]} Liga {mm.group(1)}"
        camp = re.sub(r"\s*\(.*?\)|\s*\(\d\)", "", camp).strip()
        saida.append((t_, camp, re.sub(r"\s*\(\d\)", "", vice).strip()))
    return saida


def campeoes() -> dict[str, str]:
    return {t: c for t, c, _ in _lista()}


def vices() -> dict[str, str]:
    return {t: v for t, _, v in _lista() if v}


def secao_do_ano(ano: int) -> tuple[str, int, int] | None:
    """(Não usado: todas as edições têm página própria.)"""
    return None


def tabela_parcial(ano: int) -> rsssf_concacaf.Tabela | None:
    """(Não usado.)"""
    return None


def _fuso(utc: datetime) -> timedelta:
    """Cidade do México (horário de verão até 2022): diferença para o UTC."""
    from zoneinfo import ZoneInfo
    return -utc.astimezone(ZoneInfo("America/Mexico_City")).utcoffset()


def espn_jogos(ini: str, fim: str) -> list[rsssf_concacaf.Jogo]:
    """Jogos encerrados da ESPN (liga mex.1) entre as datas, no horário da Cidade do México (texto "espn:<id>")."""
    saida = []
    for a in range(int(ini[:4]), int(fim[:4]) + 1):
        f = PASTA_DADOS / "espn" / f"mex1_{a}.json"
        for g in json.loads(f.read_text(encoding="utf-8")) if f.exists() else []:
            utc = datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00"))
            d = (utc - _fuso(utc)).date().isoformat()
            if not ini <= d <= fim or g["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL") or g["gols_mandante"] in (None, ""):
                continue
            saida.append(rsssf_concacaf.Jogo(linha=len(saida), mandante=g["mandante"], visitante=g["visitante"],
                                        gm=int(g["gols_mandante"]), gv=int(g["gols_visitante"]), data=d, texto=f"espn:{g['id']}"))
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = set(sys.argv[1:])
    for e in EDICOES:
        if alvo and e.temporada not in alvo:
            continue
        js, ts = ler(e)
        fases = {}
        for j in js:
            fases[j.fase] = fases.get(j.fase, 0) + 1
        print(f"{e.temporada:14s} {len(js):4d} jogos  {len(ts):2d} tabelas  fases {fases}")
