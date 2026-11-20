"""Leitura das páginas da Série C da RSSSF Brasil (data/coleta/bra-serie-c/rsssfbrasil/br{ano}l3.htm).

Usa o leitor comum (coleta/comum/rsssf.py) e, antes dele, corrige o texto de cada página que foge do
desenho comum. Cada correção traz o motivo. A conferência compara cada tabela publicada com a soma
dos jogos lidos.

Uso: python coleta/bra-serie-c/rsssf_c.py [ano ...]     (sem ano: todas; com um ano, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from edicoes import ANOS, PASTA_DADOS  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "br{ano}l3.htm"


def _1981(t: str) -> str:
    """1981: a 1ª fase vem em duas colunas (ida | volta, cada uma com a sua data), a 2ª fase em confrontos
    numa linha só ("1 Itumbiara (GO) - Dom Bosco (MT)  1-3 (21/03)  1-1 (26/03)", placares do ponto de vista
    do primeiro, que manda a ida) e a final só em ficha técnica ("JOGO DE IDA"). Vira uma linha por jogo."""
    linhas, saida, i = t.split("\n"), [], 0
    while i < len(linhas):
        l = linhas[i]
        if re.match(r"^\s*1st leg\s+2nd leg", l):   # bloco em duas colunas
            datas = re.findall(r"\d{2}/\d{2}/\d{4}", linhas[i + 1])
            col1, col2, i = [], [], i + 2
            while i < len(linhas) and re.search(r"\d-\d", linhas[i]):
                a, b = re.split(r"\s{5,}", linhas[i].strip(), maxsplit=1)
                col1.append(a); col2.append(re.sub(r"\s*\(\d\)\s*$", "", b))
                i += 1
            saida += [datas[0], *col1, "", datas[1], *col2, ""]
            continue
        m = re.match(r"^\s*\(1\) Tie-Break Matches - (\d{2}/\d{2}/\d{4})", l)
        if m:
            saida += ["", m[1]]
            i += 1
            continue
        m = re.match(r"^\s*\d\s+(.+?)\s+\([A-Z]{2}\)\s+-\s+(.+?)\s+\([A-Z]{2}\)\s+(\d)-(\d)\s+\((\d\d/\d\d)\)\s+(\d)-(\d)\s+\((\d\d/\d\d)\)", l)
        if m:   # confronto da 2ª fase: ida no campo do primeiro; volta no do segundo, com o placar invertido
            a, b = m[1], m[2]
            g1 = linhas[i + 1].strip() if i + 1 < len(linhas) and linhas[i + 1].strip().startswith("[") else ""
            g2 = linhas[i + 2].strip() if g1 and i + 2 < len(linhas) and linhas[i + 2].strip().startswith("[") else ""
            saida += [f"{m[5]}/1981", f"{a} {m[3]}-{m[4]} {b}", g1 if g1.strip("[] ;") else "",
                      f"{m[8]}/1981", f"{b} {m[7]}-{m[6]} {a}", g2 if g2.strip("[] ;") else ""]
            i += 1 + bool(g1) + bool(g2)
            continue
        if re.match(r"^\s*(JOGO DE (IDA|VOLTA)|Local:|Juiz:|Público:)", l):
            i += 1
            continue
        m = re.match(r"^\s*(\d{1,2}) (Abril|Maio) 1981\s*$", l)
        if m:
            saida.append(f"{int(m[1]):02d}/{4 if m[2] == 'Abril' else 5:02d}/1981")
            i += 1
            continue
        m = re.match(r"^\s*Gols?: (.*?)\]?\s*$", l)
        if m:
            saida.append(f"[{m[1].replace(' e ', ', ')}]")
            i += 1
            continue
        saida.append(re.sub(r"\((\d-\d) on penalties\)", r"[\1 on penalties]", l.replace("Second Round", "Second Phase")))
        i += 1
    return "\n".join(saida)


def _1990(t: str) -> str:
    """1990: a página quebrou as linhas no meio do jogo ("[Oct 03] Caxias" / "2-1 União Bandeirante") e no meio
    dos autores ("Gols: Edelvan 22', Sabará 39';" / "Silmar 31'"); a data às vezes cola no nome ("[Sep 30]Campo
    Grande") ou tem "?" ("[Oct ?]"). Junta as linhas, separa a data e põe os autores entre colchetes."""
    linhas = [l.rstrip() for l in t.split("\n")]
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        l = re.sub(r"^(\s*\[[A-Z][a-z]{2} [\d?]{1,2}\])(?=\S)", r"\1 ", linhas[i])
        l = re.sub(r"^\s*\[[A-Z][a-z]{2} \?\]\s*", "[unknown]\n", l)
        eh_jogo = re.match(r"^\s*(\[[A-Z][a-z]{2} \d{1,2}\]\s*)?\S.*\s\d-\d\s+\S", l)
        comeca = re.match(r"^\s*\[[A-Z][a-z]{2} \d{1,2}\]\s+\S", l) or re.match(r"^\s*[A-Z][\w ]+?\s+\d-\d\s*$", l)
        if comeca and not eh_jogo:   # jogo partido: junta com as próximas linhas até ter mandante, placar e visitante
            j = i + 1
            while j < len(linhas) and not re.match(r"^\s*\S.*\s\d-\d\s+\S", l):
                if linhas[j].strip():
                    l = l + " " + linhas[j].strip()
                j += 1
            i = j
            saida.append(l)
            continue
        m = re.match(r"^\s*Gols?:\s*(.*)$", l)
        if m:   # autores, com as continuações (linhas que não são data, jogo, tabela nem título)
            g, j = m[1], i + 1
            while j < len(linhas) and linhas[j].strip() and not re.match(r"^\s*(\[|Table|Group|\d-|Gol)", linhas[j]):
                g += " " + linhas[j].strip()
                j += 1
            saida.append(f"  [{g.strip()}]")
            i = j
            continue
        saida.append(l)
        i += 1
    return "\n".join(saida)


CONFRONTO = re.compile(r"^\s*(?P<a>[^\d\s\[][^\d\[]*?)\s{2,}(?P<b>[^\d\s\[][^\d\[]*?)\s{2,}(?P<a1>\d{1,2})-(?P<b1>\d{1,2})\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})"
                       r"\s*(?P<nota>\[(?!\w{3} \d)[^\]]*\])?\s*(?P<data>\[\w{3} \d{1,2}(?: and (?:\w{3} )?\d{1,2})?\])?\s*(?P<resto>.*)$")


def _confrontos(t: str) -> str:
    """Mata-mata em "Mandante  Visitante  1-0  0-2  [pen 4-3]  [oct 22 and 30]": os dois placares do ponto de vista do
    primeiro, que manda a ida (a página avisa: "Team in left plays first leg at home"). Vira um jogo por linha; a data
    própria do confronto, quando há, vai na frente de cada jogo. O que sobra na linha (o título da fase seguinte) desce."""
    saida = []
    for l in t.split("\n"):
        m = CONFRONTO.match(l)
        if not m or re.match(r"^\s*(table|team|pos)\b", l, re.I):
            saida.append(l)
            continue
        d1 = d2 = ""
        if m["data"]:
            md = re.match(r"\[(\w{3}) (\d{1,2})(?: and (?:(\w{3}) )?(\d{1,2}))?\]", m["data"])
            d1 = f"[{md[1]} {md[2]}] "
            d2 = f"[{md[3] or md[1]} {md[4]}] " if md[4] else d1
        saida += [f"{d1}{m['a'].strip()}  {m['a1']}-{m['b1']}  {m['b'].strip()}",
                  f"{d2}{m['b'].strip()}  {m['b2']}-{m['a2']}  {m['a'].strip()}  {rsssf.inverter_pen(m['nota'] or '')}".rstrip()]
        if m["resto"].strip():
            saida.append(m["resto"].strip())
    return "\n".join(saida)


CONFRONTO_1995 = re.compile(r"(?P<a>[A-Za-zÀ-ú][A-Za-zÀ-ú .'\-]*?(?:\([A-Z]{2}\)|\(PELOTAS\)\([A-Z]{2}\))?)(?:\(\*\))? X "
                            r"(?P<b>[A-Za-zÀ-ú][A-Za-zÀ-ú .'\-]*?(?:\([A-Z]{2}\)|\(PELOTAS\)\([A-Z]{2}\))?)(?:\(\*\))?\s*(?:\((?P<d0>\d{4})\))?\s+"
                            r"(?P<a1>\d{1,2}|W[O0])-(?P<b1>\d{1,2}|W[O0])\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})(?:\s*\((?P<d2>\d{4})\))?(?:\s*\((?P<p>\d+-\d+)\)\s*PEN)?")


def _1995(t: str) -> str:
    """1995: a 2ª e a 3ª fases vêm em confrontos colados uns nos outros ("NACIONAL(AM)(*) X ATLETICO RORAIMA(RR)
    4-0 0-0 (3009)"), com os dois placares do ponto de vista do primeiro, que manda a ida; "(*)" marca quem passou.
    Vira um jogo por linha, com as datas do cabeçalho (24/9 e 1/10; 8/10 e 15/10). Também corrige erros de digitação
    da página que a tabela do grupo desmente: "Coríntians 3x1 3x1 Santa Cruz-PB" (placar repetido) e "Ypranga"."""
    t = t.replace("Coríntians 3x1 3x1 Santa Cruz-PB", "Coríntians 3x1 Santa Cruz-PB").replace("Ypranga", "Ypiranga")
    # a nota do jogo Caxias x Avaí (interrompido por neblina) vem picada no meio dos confrontos seguintes
    for pedaco in ("[1st leg interrupted due to fog at the", "end of 1st half (when score was 1-0)", "and concluded at 25/09]"):
        t = t.replace(pedaco, "  ")
    i, j = t.find("SERIE C  - - SECOND PHASE"), t.find("SERIE C  - - FOURTH PHASE")
    if i < 0 or j < 0:
        return t
    bloco = t[i:j]
    k = bloco.find("SERIE C  - - THIRD PHASE")
    saida = []
    for nome_fase, parte, datas in (("Second Phase", bloco[:k], ("24/09/1995", "01/10/1995")), ("Third Phase", bloco[k:], ("08/10/1995", "15/10/1995"))):
        saida += ["", nome_fase, ""]
        for m in CONFRONTO_1995.finditer(parte.replace("\n", "  ")):
            a, b = m["a"].strip(), m["b"].strip()
            d1 = f"{m['d0'][:2]}/{m['d0'][2:]}/1995" if m["d0"] else datas[0]
            d2 = f"{m['d2'][:2]}/{m['d2'][2:]}/1995" if m["d2"] else datas[1]
            if m["a1"].startswith("W") or m["b1"].startswith("W"):   # "0-W0": W.O. na ida, a favor de quem tem o "W"
                saida += [d1, f"{a} awd {b} [walkover awarded {'0-1' if m['b1'].startswith('W') else '1-0'}]"]
            else:
                saida += [d1, f"{a} {m['a1']}x{m['b1']} {b}"]
            saida += [d2, f"{b} {m['b2']}x{m['a2']} {a}" + (f" [{rsssf.inverter_pen('pen ' + m['p'])}]" if m["p"] else "")]
    return t[:i] + "\n".join(saida) + "\n\n" + t[j:]


def _1999(t: str) -> str:
    """1999: antes da Série C, a página traz as seletivas estaduais (RS, PR, MG, PB, PE, PI), que não são Série C."""
    i, j = t.find("State qualifying tournaments"), t.find("Brazil Third Division 1999")
    return t[:i] + t[j:] if 0 <= i < j else t


rsssf.CORRECOES.update({
    "br2003l3.htm": [(r"^Goytacaz\s+1-0\s+abd\s+Americano\s+\[.*$",
                      "Goytacaz  1-0  Americano\nAmericano  abd  Goytacaz  [abandoned at 61' (Goytacaz with less than 7 players), Americano winning 1-0]",
                      "confronto em linha só, com a volta abandonada ('abd'): vira dois jogos; o placar da volta vem do ogol")],
    "br1999l3.htm": [(_1999, None, "seletivas estaduais no começo da página (não são jogos da Série C)")],
    "br1996l3.htm": [(r"^(\s*GAS\s+2-3\s+)GAS\b", "\\1Baré",
                      "grupo 2: 'GAS 2-3 GAS' é GAS 2-3 Baré (o ogol e a tabela do grupo confirmam)")],
    "br2015l3.htm": [(r"^\s+PK: (\d+-\d+)\s*(\S.*)?$", "  [pen \\1]\n\\2",
                      "pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO H')")],
    "br2024l3.htm": [(r"(\S)  +(\d{1,2}-[A-ZÀ-Ú][^\d\n]+\s+\d+\s+19\s)", "\\1\n\\2",
                      "linhas da tabela da 1ª fase coladas umas nas outras ('... 43  11-Figueirense  24  19 ...')"),
                     (r"(/São João del Rei|/João Pessoa) (?=\S)", "\\1  ",
                      "estádio de nome longo colado no nome do mandante ('.../São João del Rei Athletic')")],
    "br1995l3.htm": [(_1995, None, "2ª e 3ª fases em confrontos colados; placar repetido e nome com erro de digitação")],
    "br1994l3.htm": [(r"^Maruinense(\s+)Vitória(\s+)0-0", r"Maruinense\g<1>Vitória-ES\g<2>0-0",
                      "oitavas: o 'Vitória' sem estado é o Vitória-ES (o Vitória-PE caiu para o ABC na mesma fase)"),
                     (_confrontos, None, "mata-mata com os dois jogos do confronto numa linha só")],
    "br1990l3.htm": [(_1990, None, "linhas de jogo e de autores partidas no meio; data colada no nome")],
    "br1981l3.htm": [(_1981, None, "duas colunas, confrontos numa linha e final só em ficha técnica")],
})


def _grupo_limpo(g: str) -> str:
    """'Group APosTeamPTS...', 'GRUPO A', 'GROUP 01' -> 'Grupo A', 'Grupo 1'; 'GRUPO ÚNICO' fica."""
    m = re.match(r"^(?:group|grupo)\s+([A-Z]|\d{1,2})(?![a-z])", g.strip(), re.I)
    if not m:
        return g.strip()
    x = m.group(1).upper()
    return f"Grupo {int(x) if x.isdigit() else x}"


def atribuir_grupos(jogos: list, tabelas: list) -> None:
    """Nas páginas em que cada rodada traz os jogos de todos os grupos (2013 em diante), o grupo de cada jogo
    sai das tabelas da fase: o jogo vai para o grupo em que estão os dois clubes."""
    for tb in tabelas:
        tb.grupo = _grupo_limpo(tb.grupo)
    for j in jogos:
        j.grupo = _grupo_limpo(j.grupo)
    for fase in {j.fase for j in jogos}:
        tbs = [tb for tb in tabelas if tb.fase == fase and tb.grupo and tb.linhas]
        if len({tb.grupo for tb in tbs}) == 1 and not any(j.grupo for j in jogos if j.fase == fase):
            for j in jogos:   # fase com uma tabela só (a final de 2018 e 2025, "Group I"): os jogos são desse grupo
                if j.fase == fase:
                    j.grupo = tbs[0].grupo
            continue
        if len({tb.grupo for tb in tbs}) < 2:
            continue
        do_jogo = [j for j in jogos if j.fase == fase]
        nomes = {x for j in do_jogo for x in (j.mandante, j.visitante)}
        grupo_de: dict[str, str] = {}
        for tb in tbs:
            for nt, nj in rsssf.casar([r["nome"] for r in tb.linhas], nomes).items():
                grupo_de[nj] = tb.grupo
        for j in do_jogo:
            gm, gv = grupo_de.get(j.mandante), grupo_de.get(j.visitante)
            if gm and gm == gv:
                j.grupo = gm


def ler(ano: int):
    jogos, tabelas = rsssf.ler(ano)
    atribuir_grupos(jogos, tabelas)
    return jogos, tabelas


def conferir(ano: int):
    jogos, tabelas = ler(ano)
    return jogos, tabelas, rsssf.conferir(jogos, tabelas)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = [int(a) for a in sys.argv[1:]] or ANOS
    for a in anos:
        jogos, tabelas, erros = conferir(a)
        print(f"{a}: {len(jogos)} jogos, {len(tabelas)} tabelas ({sum(len(t.linhas) for t in tabelas)} linhas), {len(erros)} divergências")
        if len(anos) == 1:
            fases = {}
            for j in jogos:
                fases.setdefault((j.fase, j.grupo), 0)
                fases[(j.fase, j.grupo)] += 1
            for (f, g), n in fases.items():
                print(f"   {f} / {g or '-'}: {n}")
            for e in erros[:80]:
                print("   !", e)
