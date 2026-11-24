"""Lê os jogos de cada edição da 1ª divisão da Costa Rica nas páginas da RSSSF (data/coleta/crc-1/rsssf/) com o leitor comum
(rsssf_concacaf); as tabelas com o leitor próprio (tabelas_texto). Os jogos que a página não tem vêm da ESPN (espn_jogos).

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/crc-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
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
    (r"^(Repechaje|Reclasificaci[oó]n|Play-?off for .*|Extra match.*|Desempate.*|Playoff)( \[.*\])?" + _FIM, "Desempate do título"),
    (r"^(Quarter-?finals?|Cuartos de final)( \[.*\])?" + _FIM, "Quartas de final"),
    (r"^(Semi-?finals?|Semifinales)( \[.*\])?" + _FIM, "Semifinal"),
    (r"^(Grand Final|Gran Final|Final|Finals|Final \(.*\)|Championship Final|National Final|Championship Playoff)( \[.*\])?" + _FIM,
     "Final"),
    (r"^(Cuadrangular(es)? (Permanencia|por el descenso|de descenso).*|Relegation (Group|Round|Playoff).*)" + _FIM, "Grupo do rebaixamento"),
    (r"^(Semifinal Stage|Cuadrangulares por el T[ií]tulo|Cuadrangulares)( \[.*\])?" + _FIM, "Fase final"),
    (r"^(Second Phase)( \[.*\])?" + _FIM, "Segunda fase"),
    (r"^(Pentagonal( Final)?|Cuadrangular( Final)?|Hexagonal( Final)?|Triangular( Final)?|Final Round|Final Stage|Liguilla|"
     r"Championship (Round|Group)|Second Stage|Segunda Fase|Playoff Stage)( \[.*\])?" + _FIM, "Fase final"),
    (r"^(First Stage|Regular Stage|Primera Fase|Regular Season)( \[.*\])?" + _FIM, ""),
]

# título que abre o campeonato numa página que começa por outra competição (os trechos já dizem onde começa)
INICIO = r"^NUNCA$"

# torneios dentro da edição (não há: cada torneio do ano é uma edição)
TORNEIOS: list[tuple[str, str]] = [(r"^Apertura( \d{4})?( \(.*\))?:?$", "Apertura"), (r"^Clausura( \d{4})?( \(.*\))?:?$", "Clausura")]
FECHA = r"^(Aggregate Table|Overall Table|Tabla Acumulada|National Final|Grand Final|Gran Final|Final \(.*\)|Championship Playoff|Second Phase|Cuadrangular.*)"

# grupos marcados por título ("Group A", "Grupo 1")
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
    # "San Jose  0-0 Dallas  (27,779) (Dallas wins shootout 2-1)" (MLS 1996-1999): empate decidido nos pênaltis
    def _shootout(m):
        l, quem, a, b = m.string, m.group(1), int(m.group(2)), int(m.group(3))
        mm = re.match(r"^(\S.*?)\s+\d{1,2}-\d{1,2}\s+(\S.*?)\s{2,}", l + "  ")
        casa = mm and chave(quem).split()[0] in chave(mm.group(1))
        return f"[{a}-{b} pen]" if casa else f"[{b}-{a} pen]"
    ls = [re.sub(r"\(([A-Z][\w .'/]*?) wins? (?:the )?shootout,? (\d{1,2})-(\d{1,2})\)", _shootout, l) for l in ls]
    # "Belen  1-1 Saprissa (Saprissa 4-2 pen)" (1996/97: empate decidido nos pênaltis): vira a nota "[x-y pen]" na ordem do jogo
    def _pen_nome(m):
        casa, gm, gv, fora, quem, a, b = m.groups()
        if a is None:
            return f"{casa}  {gm}-{gv}  {fora}  [won on penalties by {quem}]"
        venceu_casa = chave(quem).split()[0] in chave(casa)
        pm, pv = (a, b) if venceu_casa else (b, a)
        return f"{casa}  {gm}-{gv}  {fora}  [{pm}-{pv} pen]"
    ls = [re.sub(r"^(\S.*?)\s+(\d{1,2})-(\d{1,2})\s+(\S.*?)\s*\(([^()]*?)\s+(?:(\d{1,2})-(\d{1,2})\s+)?(?:on\s+)?pen\)\s*$",
                 _pen_nome, l) for l in ls]
    # depois do título dos playoffs, "Round 1" / "Round One" é a 1ª fase dos playoffs (não uma rodada da fase regular)
    po = False
    for k, l in enumerate(ls):
        s = l.strip()
        if re.fullmatch(r"(Championship Playoffs?|MLS Cup Playoffs?|Playoffs?:?)", s):
            po = True
        elif re.fullmatch(r"(Regular Season.*|Final Tables.*)", s):
            po = False
        elif po and re.match(r"^Round (1|One)\b", s):
            ls[k] = "Playoff First Round" + s[len(s.split()[0]) + len(s.split()[1]) + 1:]
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


_COLUNA = {"g": "j", "gp": "j", "m": "j", "pld": "j", "w": "v", "t": "e", "d": "e", "l": "d", "ws": "ws", "sw": "ws", "sow": "ws",
           "ls": "ls", "sl": "ls", "sol": "ls", "gf": "gp", "ga": "gc", "pts": "pts", "points": "pts", "bp": "bp"}


def _cabecalho(s: str) -> list[str] | None:
    """Colunas numéricas de um cabeçalho de tabela ("GP  W  WS  LS  L  GF  GA  Pts", "G W T L GF GA PTS % Att.")."""
    toks = [x.lower().strip(".:") for x in s.split()]
    cols = [_COLUNA[x] for x in toks if x in _COLUNA]
    return cols if {"j", "v", "d"} <= set(cols) and ("pts" in cols or "gp" in cols) else None


_PADRAO = ["j", "v", "e", "d", "gp", "gc", "pts"]


def tabelas_texto(pagina: str, ini: int, fim: int) -> list[rsssf_concacaf.Tabela]:
    """Tabelas do trecho, pelo cabeçalho de cada uma; sem cabeçalho, J V E D GP GC P (com "57-35"). O empate inclui as vitórias e
    as derrotas nos pênaltis (WS, LS: o jogo foi empate). Nome colado no número ("Philadelphia Field Club24") e linha sem gols
    (ASL 1932: "6  3  2  1   8") também valem. O subtítulo logo acima ("Eastern Division") vira o grupo."""
    ls = linhas(pagina)
    saida, tab, cols, grupo = [], None, _PADRAO, ""
    for i in range(ini, min(fim, len(ls))):
        s = ls[i].rstrip()
        if not s.strip():
            tab = None
            continue
        c = _cabecalho(s)
        if c:
            cols, tab = c, None
            continue
        st = s.strip()
        corpo = re.sub(r"^\s*\d{1,2}\s*\.\s*", "", s).strip()
        corpo = re.split(r"\s\.\d{3}\b|\s\d\.\d{2}\b", corpo)[0]          # aproveitamento e público
        corpo = re.sub(r"(\d{1,3})\s*-\s*(\d{1,3})", r"\1 \2", corpo)   # "57-35"
        m = re.match(r"^([A-Za-zÀ-ÿ&'’./()\- ]*?[A-Za-zÀ-ÿ.)])\s*((?:\d{1,3}\s*){4,12})(.*)$", corpo)
        if not m or re.match(r"^(Round|Bye|Playoff|CHAMPION|Semi|Final|Div|Conf|Soccer Bowl)", st, re.I):
            if not re.match(r"^[-=_\s]+$", st):
                tab = None
                if len(st) < 45 and not re.search(r"\d", st):
                    grupo = re.sub(r"\s*:$", "", st)
            continue
        nums = [int(x) for x in m.group(2).split()]
        cs = cols
        if len(nums) == len(cs) - 2 and "gp" in cs and "gc" in cs:   # sem gols
            cs = [x for x in cs if x not in ("gp", "gc")]
        elif len(nums) > len(cs):
            nums = nums[:len(cs)]
        if len(nums) != len(cs):
            continue
        r = dict(zip(cs, nums))
        e_ = r.get("e", 0) + r.get("ws", 0) + r.get("ls", 0)
        if r["v"] + e_ + r["d"] != r["j"]:
            continue
        nome = re.sub(r"\s+", " ", m.group(1)).strip(" .")
        if re.match(r"^(no|team|pos|gp|g)$", nome, re.I) or len(nome) < 2:
            continue
        mc = re.search(r"\[([^\]]+)\]", m.group(3) or "")
        linha = {"pos": None, "nome": nome, "cidade": mc.group(1) if mc else None, "j": r["j"], "v": r["v"], "e": e_, "d": r["d"],
                 "gp": r.get("gp"), "gc": r.get("gc"), "pts": r.get("pts"), "obs": (m.group(3) or "").strip()}
        if re.search(r"head-to-head", grupo, re.I):   # confronto entre os canadenses (2020): não é classificação
            continue
        if tab is None:
            tab = rsssf_concacaf.Tabela(i, grupo, "", grupo=grupo)
            saida.append(tab)
        tab.linhas.append(linha)
    return saida


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
        # jogo abandonado e completado depois ("abd" e, dias depois, o mesmo jogo com "[remaining 50']"): fica só a continuação
        for x in [x for x in j if x.especial == "abd"]:
            if any(y.mandante == x.mandante and y.visitante == x.visitante and re.search(r"remaining", y.nota, re.I) and y.linha > x.linha
                   for y in j):
                j.remove(x)
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
        for x in tabelas_texto(pagina, ini, fim):   # a tabela fica no torneio do ano em que está (Apertura, Clausura)
            x.fase = _fase("", tor.get(x.linha, ""))
            tabelas.append(x)
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final
        tabelas += tabelas_texto(pagina, ini, fim)
    if e.wiki is not None:
        import wikipedia_jogos
        jogos += wikipedia_jogos.jogos(e.wiki)
    if externos:   # a ESPN também traz jogos que a página tem: dela, só os que a página não tem (mesmo par até 3 dias antes ou depois)
        from clubes_crc import clube
        par = lambda x: frozenset((clube(x.mandante, e.ano_inicio), clube(x.visitante, e.ano_inicio)))
        dia = lambda d: datetime.strptime(d[:10], "%Y-%m-%d")
        na_pagina = [(par(x), dia(x.data)) for x in jogos if x.data]
        corte = min((x.data for x in jogos if x.data and x.fase), default=None)   # a fase final é a da página
        if corte:
            externos = [x for x in externos if x.data < corte]
        else:   # a fase final da página sem data: saem da ESPN os últimos jogos que são confrontos dela
            pares_po = {par(x) for x in jogos if x.fase}
            externos.sort(key=lambda x: x.data)
            while externos and pares_po and par(externos[-1]) in pares_po:
                externos.pop()
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


def _lista() -> list[tuple[str, str, str]]:
    """coschamp.html: [(temporada, campeão, vice)] nos nomes das edições: "1921", "1986/87"; 1961 com "[Asofútbol]" e
    "[Federación]"; de 2007/08 em diante "[Ap.]" (Apertura do 1º ano) e "[Cl.]" (Clausura do 2º). Colunas fixas (campeão a
    partir da 8ª, vice a partir da 40ª)."""
    saida, temp = [], None
    for l in linhas("coschamp"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(\S.*?)\s*$", l)
        if not m or not re.match(r"^(\d{4}|\s{8}\S)", l):
            continue
        if m.group(1):
            temp = m.group(1)
        if not temp or re.search(r"not played", l):
            continue
        camp, vice = l[8:40].strip(), re.sub(r"\s*\[.*$", "", l[40:]).strip()
        vice = re.sub(r"\s*\(.*?\)\s*$", "", vice)
        tag = re.search(r"\[(Ap\.|Cl\.|Asof[úu]tbol|Federaci[óo]n)\]", l)
        t_ = temp
        if tag and tag.group(1) == "Ap.":
            t_ = f"{temp[:4]} Apertura"
        elif tag and tag.group(1) == "Cl.":
            t_ = f"{int(temp[:4]) + 1} Clausura"
        elif tag:
            t_ = f"{temp} {'Asofútbol' if tag.group(1).startswith('Asof') else 'Federación'}"
        saida.append((t_, camp, vice))
    return saida


def vices_texto(e: Edicao) -> str:
    """(Não usado: a lista de campeões da Costa Rica traz o vice.)"""
    return ""


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
    """Horário da Costa Rica (UTC-6)."""
    from zoneinfo import ZoneInfo
    return -utc.astimezone(ZoneInfo("America/Costa_Rica")).utcoffset()


def espn_jogos(ini: str, fim: str) -> list[rsssf_concacaf.Jogo]:
    """Jogos encerrados da ESPN (liga crc.1) entre as datas, no horário da Costa Rica (texto "espn:<id>")."""
    saida = []
    for a in range(int(ini[:4]), int(fim[:4]) + 1):
        f = PASTA_DADOS / "espn" / f"crc1_{a}.json"
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
