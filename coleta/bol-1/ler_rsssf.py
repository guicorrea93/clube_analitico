"""Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/bol-1/rsssf/) com o leitor comum (rsssf_sul); nas edições
sem página, só as tabelas (a seção do ano em bolhist.html). Os jogos da Wikipédia em espanhol (1950, 1953, 1990, 1991 e as
fases finais de outros anos) vêm de wikipedia_jogos.py.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/bol-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import rsssf_sul  # noqa: E402

from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira que casa vale); vale para todas as edições
# fim de título de fase de liga: a linha inteira (a nota que quebra a linha, "...qualified for" / "Octogonal Final.", não vale)
_FIM = r"\s*:?\s*(\[[^\]]*\])?$"
FASES = [
    (r"^(Relegation (Group|Round|Liguilla|Table)|Liguilla (de |del |por el )?(No )?Descenso|Hexagonal (por|para) el no descenso"
     r"( de categor[ií]a)?|Cuadrangular del No-Descenso|Liguilla No Descenso)" + _FIM, "Grupo do rebaixamento"),
    (r"^(Liguillas|Liguilla Pre Libertadores|Cuadrangular (Libertadores|Pre-Conmebol)|Hexagonal para Copa Libertadores( de America)?|"
     r"Liguilla [ABC] \(.*\))" + _FIM, "Liguillas"),
    (r"^Hexagonal 2" + _FIM, "Hexagonal 2"),
    (r"^(Championship (Group|Round|Liguilla)|Liguilla Final|Final Liguilla|Final (Group|Round|Stage|Phase)|Hexagonal Final|"
     r"Hexagonal Clausura|Hexagonal 1|Cuadrangular [Ff]inal|Octogonal Final|Liguilla)" + _FIM, "Fase final"),
    (r"^Playoff \(in [A-Z]\w+\)" + _FIM, "Desempate da segunda fase"),   # 1977: desempate do grupo da 2ª fase
    (r"^(First Stage|First Phase|Phase 1|Regular (Season|Stage)|Primera Etapa)( \((First Stage|Torneo Apertura|Apertura)\))?" + _FIM, ""),
    (r"^(Second (Stage|Phase)|Segunda Etapa|Octogonal)( \(Second Stage\))?" + _FIM, "Segunda fase"),
    (r"^((Third|Thirth) (Stage|Phase)|Tercera Etapa)( \(Third Stage\))?" + _FIM, "Terceira fase"),
    (r"^(Round of 16|Octavos de final|1/8 Finals)\b", "Oitavas de final"),
    (r"^(Quarter[- ]?finals?|Cuartos de final)\b", "Quartas de final"),
    (r"^(Semi[- ]?finals?)\b", "Semifinal"),
    (r"^(Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|Aggregate|Tables|Round|Liguilla))|Championship (Final|Match)|"
     r"Finals$)", "Final"),
    (r"^Definition of (the )?champions?" + _FIM, "Final"),   # 1980: melhor de três pelo título, com "Round 1/2/3"
    (r"^Extra match for definition of runners-up", "Desempate do 2º lugar"),
    (r"^Extra seri(e|es) for relegation", "Desempate do rebaixamento"),
    # "Championship Playoff" (2020-2024): a final entre os vencedores das duas etapas, como o "Championship Final" de 2014
    (r"^((Apertura|Clausura) )?Championship [Pp]layoffs?" + _FIM, "Final"),
    (r"^(Apertura|Clausura) Final" + _FIM, "Final"),
    (r"^(Playoff|Decisive Match)" + _FIM, "Desempate do título"),   # 3º jogo da final (2004 Clausura, 2018 Apertura)
    (r"^(First place playoff|Extra match|Desempate)", "Desempate do título"),
    (r"^Ronda Final" + _FIM, "Fase final"),
    (r"^Definition of (runners?[- ]up|third place)" + _FIM, "Desempate do 2º lugar"),
    (r"^(Playoff (for|to decide) [Ss]econd [Pp]lace|Second [Pp]lace (Playoffs?|Matches)|Third Place (Playoffs?|Matches)|"
     r"Fourth Place (Playoffs?|Matches))", "Desempate do 2º lugar"),
    (r"^(Playoff Descenso|Relegation [Pp]lay-?offs?)", "Desempate do rebaixamento"),
]

# título que abre o campeonato numa página que começa por outra competição
INICIO = r"^NUNCA$"

# torneios dentro da edição anual: a fase dos jogos vira o torneio ("Apertura"; "Final do Apertura")
TORNEIOS: list[tuple[str, str]] = [
    # ("Torneo Apertura 2007 (Torneo Alberto L...)", "Torneo Clausura 2024": o ano e o apelido do torneio podem vir depois)
    (r"^(Torneo |First Stage \(Torneo |First Stage \()?Apertura( \d{4})?( \(.*)?\)?$", "Apertura"),
    (r"^(Torneo |Second Stage \(Torneo |Second Stage \()?Clausura( \d{4})?( \(.*)?\)?$", "Clausura"),
]
# título que volta ao campeonato (fim do torneio em vigor)
# (vale a linha inteira: ler_rsssf._torneios junta _FIM)
FECHA = (r"^(Aggregate( Table)?|Agreggate( Table)?|Combined Table|Overall Table|Tabla Anual|Playoffs?|Championship (Playoff|Final|Match)|"
         r"Finals?|Liguilla Final|Final Liguilla|Hexagonal Final|Cuadrangular final|Second Stage|Playoff Stage|"
         r"Relegation Group|Relegation Table|Hexagonal (por|para) .*|Liguilla de no descenso)")

# grupos marcados por título ("Liguilla B (5,7,9,11 of first stage)", "Group A")
_GRUPO = r"^(?:Grupo|Group|Liguilla)\s+[“\"]?([A-Z])\b(?!\s*\()"

# páginas de colunas fixas: (início da coluna do visitante, início da coluna do placar)
COLUNAS: dict[str, tuple[int, int]] = {}


_CP437 = str.maketrans({"‚": "é", "¢": "ó", "¡": "í", "£": "ú", "¤": "ñ", "": "é", "¢": "ó"})


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    # travessão no placar ("2–0") em parte das páginas: vira hífen
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_sul.texto(PASTA / f"{pagina}.html")]
    # páginas com acentos da página de código 437 ("Am‚rica", "Cat¢lica"): voltam ao acento
    ls = [l.translate(_CP437) for l in ls]
    # a página de 2011/12 está em UTF-16: cada letra vem com um caractere nulo
    ls = [l.replace("\x00", "") for l in ls]
    if pagina == "bolhist":   # "16    8  5  3   (40-32)  21": gols entre parênteses; vira "16 8 5 3 40-32 21"
        ls = [re.sub(r"\(\s*(\d+)\s*-\s*(\d+)\s*\)", r"\1-\2", l) for l in ls]
    if pagina in COLUNAS:
        a, b = COLUNAS[pagina]
        for k, l in enumerate(ls):
            if len(l) > b and re.search(r"\s\d{1,2}-\d{1,2}\s*$", l) and l[a - 1] == " " and l[a] != " " and not rsssf_sul.linha_tabela(l):
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
            viu_jogo = bool(rsssf_sul._jogo(ls[i])) or bool(_CELULAS.search(ls[i]))
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


def _vitoria_dada(x: rsssf_sul.Jogo) -> None:
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
    quem = [w for w in rsssf_sul.chave(m.group(3)).split() if len(w) > 3]   # "Santa Cruz" x "Real Sta Cruz"; "Gaubira"
    parece = lambda nome: any(SequenceMatcher(None, a, b).ratio() >= 0.75 for a in quem
                              for b in rsssf_sul.chave(nome).split() if len(b) > 3)
    casa, fora = parece(x.mandante), parece(x.visitante)
    if casa == fora:
        return
    if m.group(1):
        x.gm, x.gv = int(m.group(1)), int(m.group(2))
    elif x.gm is None and (mo := re.search(r"originally (\d{1,2})\s*-\s*(\d{1,2})", x.nota, re.I)):
        x.gm, x.gv = int(mo.group(1)), int(mo.group(2))
    x.gm_of = x.gv_of = None
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


def ler(e: Edicao) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
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
        j, t = rsssf_sul.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for x in [x for x in j if x.linha in voltas]:
            casa, fora, gm, gv = voltas[x.linha]
            j.append(rsssf_sul.Jogo(x.linha, casa, fora, gm, gv, None, None, x.secao, x.fase, x.grupo, "",
                                    "ida e volta numa linha só; mando da volta presumido", None, texto=x.texto))
            x.nota = (x.nota + "; ida e volta numa linha só").strip("; ")
        for linha, casa, fora, gm, gv, dado in cruz:   # fase e grupo: os da tabela que vem logo depois da tabela de confrontos
            tab = next((x for x in t if x.linha > linha), None)
            x = rsssf_sul.Jogo(linha, casa, fora, gm, gv, None, None, "", tab.fase if tab else "", tab.grupo if tab else "",
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
        tabelas += rsssf_sul.ler([""] * ini + list(ls[ini:fim]), e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.wiki is not None:
        import wikipedia_jogos
        jogos += wikipedia_jogos.jogos(e.wiki)
    if externos:   # a ESPN também traz os jogos finais que a página tem: dela, só os jogos de antes do primeiro da página
        corte = min((x.data for x in jogos if x.data), default="9999")
        externos = [x for x in externos if x.data < corte]
        from clubes_bol import clube
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
    """bolchamp.html: [(temporada, campeão, vice)]. Seções: liga de La Paz (de 1950 em diante), Torneo Integrado, Certamen
    Nacional Mixto ("1957/58" = "1957 Mixto") e Torneo Nacional. "Ap", "Cl", "Ad" depois do ano são Apertura, Clausura e
    Adecuación; a linha sem ano ("        Cl The Strongest") é do ano de cima. O vice só vem até 1976."""
    saida, ano, secao = [], None, ""
    for l in linhas("bolchamp"):
        s = l.strip()
        if s.startswith("Number of Championships"):
            break   # depois vem o campeonato amador de seleções provinciais ("Torneo Nacional de Fútbol")
        if re.match(r"^(La Paz League|Torneo Integrado|Certamen Nacional Mixto|Torneo Nacional|Number of)", s):
            secao = s
            continue
        m = re.match(r"^(\d{4}(?:/\d{2})?)?(?:-\d)?\s+(?:(Ap|Cl|Ad)\s+)?(\S.*?)(?:\s{2,}(\S.*?))?\s*(\[\*\])?$", l)
        if not m or not s or re.search(r"no competition|abandoned|^\d{4}\s*$", s) or secao.startswith("Number"):
            continue
        if m.group(1):
            ano = m.group(1)
        if not ano or not 1950 <= int(ano[:4]) <= 2025 or (not m.group(1) and not m.group(2)):
            continue
        t = "1957 Mixto" if secao.startswith("Certamen") else ano
        if m.group(2):
            t = f"{ano} " + {"Ap": "Apertura", "Cl": "Clausura", "Ad": "Adecuación"}[m.group(2)]
        if re.match(r"^\d{4} (Apertura|Clausura|Adecuación)$", t) and int(ano) in (2011, 2012, 2013, 2014, 2015, 2016):
            t = f"{ano}/{(int(ano) + 1) % 100:02d}" + t[4:]   # (a lista escreve "2011/12 Ad"; a linha sem ano herda)
        campeao = re.sub(r"\s*\[.*?\]\s*$", "", m.group(3)).strip()
        if campeao:
            vice = (m.group(4) or "").strip()
            saida.append((t, campeao, "" if vice.startswith("[") else vice))
    return saida


def campeoes() -> dict[str, str]:
    return {t: c for t, c, _ in _lista()}


def vices() -> dict[str, str]:
    return {t: v for t, _, v in _lista() if v}


def secao_do_ano(ano: int) -> tuple[str, int, int] | None:
    """(Não usado: todas as edições têm página própria.)"""
    return None


def tabela_parcial(ano: int) -> rsssf_sul.Tabela | None:
    """(Não usado: as tabelas do Equador são completas.)"""
    return None


def espn_jogos(ini: str, fim: str) -> list[rsssf_sul.Jogo]:
    """Jogos encerrados da ESPN (liga bol.1) entre as datas, no horário da Bolívia (UTC-4) (texto "espn:<id>")."""
    saida = []
    for a in range(int(ini[:4]), int(fim[:4]) + 1):
        f = PASTA_DADOS / "espn" / f"bol1_{a}.json"
        for g in json.loads(f.read_text(encoding="utf-8")) if f.exists() else []:
            d = (datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=4)).date().isoformat()
            if not ini <= d <= fim or g["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL") or g["gols_mandante"] in (None, ""):
                continue
            saida.append(rsssf_sul.Jogo(linha=len(saida), mandante=g["mandante"], visitante=g["visitante"],
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
