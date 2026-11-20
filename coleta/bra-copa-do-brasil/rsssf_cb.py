"""Leitura das páginas da Copa do Brasil da RSSSF Brasil (data/coleta/bra-copa-do-brasil/rsssfbrasil/cbr{ano}.htm).

Usa o leitor comum (coleta/comum/rsssf.py) e, antes dele, corrige o texto de cada página que foge do
desenho comum (CORRECOES, com o motivo). A conferência compara cada tabela publicada com a soma dos jogos lidos.

Uso: python coleta/bra-copa-do-brasil/rsssf_cb.py [ano ...]     (sem ano: todas; com um ano, lista as divergências)
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
rsssf.MODELO = "cbr{ano}.htm"

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


_PK = (r"^\s+PK: (\d+-\d+)\s*(\S.*)?$", "  [pen \\1]\n\\2", "pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO B')")
NUMERADO = re.compile(r"^\s*(?:\d+\s+)?(?P<a>[^\d\s\[(][^\[]*?)\s+(?:-|x)\s+(?P<b>[^\d\s\[(][^\[]*?)\s{2,}"
                      r"(?P<s1>\d+\s*-\s*\d+|n/p|w\.?o\.?)\s*\((?P<d1>\d{1,2}/\d{1,2})\)"
                      r"(?:\s+(?P<s2>\d+\s*-\s*\d+|n/p|w\.?o\.?)\s*(?:\((?P<d2>\d{1,2}/\d{1,2})\))?)?\s*(?P<resto>.*)$", re.I)


def _numerados(ano: int, primeiro_manda_ida: bool = True):
    """Confronto numa linha só: "4 ASA (AL) - Brasiliense (DF)   1-1 (04/02)   0-3 (03/03)   [5-3 pen]" (2000, 2002 a 2018 e as
    fases finais de 1989 a 1999). Os placares são do ponto de vista do primeiro, que manda a ida; "n/p" = volta não jogada
    (eliminado na ida por 2 gols fora, desde 2001). Vira um jogo por linha, com a data de cada um; as linhas de autores
    logo abaixo ("[Cuca e Kita]", "[Edinho]") vão para a ida e a volta, nessa ordem."""
    def f(t: str) -> str:
        linhas, saida, i = t.split("\n"), [], 0
        while i < len(linhas):
            m = NUMERADO.match(linhas[i])
            if not m:
                saida.append(linhas[i]); i += 1
                continue
            a, b = m["a"].strip(), m["b"].strip()
            nota = m["resto"].strip()
            autores, j = [], i + 1
            while j < len(linhas) and re.match(r"^\s*\[[^\]]*\]\s*$", linhas[j]) and not re.match(r"^\s*\[\w{3} \d", linhas[j]):
                autores.append(linhas[j].strip()); j += 1
            def data(d):
                dd, mm = d.split("/")
                return f"{int(dd):02d}/{int(mm):02d}/{ano}"
            if not primeiro_manda_ida:   # 2015-2016: o primeiro da linha manda a volta (placares sempre do ponto de vista dele)
                a, b = b, a
                m = {**m.groupdict(), "s1": "-".join(re.sub(r"\s", "", m["s1"]).split("-")[::-1]) if "-" in m["s1"] else m["s1"],
                     "s2": "-".join(re.sub(r"\s", "", m["s2"]).split("-")[::-1]) if m["s2"] and "-" in m["s2"] else m["s2"]}
                nota = rsssf.inverter_pen(nota)
            s1 = re.sub(r"\s", "", m["s1"])
            if re.fullmatch(r"\d+-\d+", s1):
                saida += [data(m["d1"]), f"{a}  {s1}  {b}", autores[0] if autores else ""]
            elif s1.lower().startswith("w"):
                saida += [data(m["d1"]), f"{a}  awd  {b}  [walkover]"]
            s2 = re.sub(r"\s", "", m["s2"] or "")
            if re.fullmatch(r"\d+-\d+", s2):
                x, y = s2.split("-")
                pen = rsssf.inverter_pen(nota) if "pen" in nota.lower() else ""
                saida += [data(m["d2"]) if m["d2"] else "", f"{b}  {y}-{x}  {a}  {pen}".rstrip(), autores[1] if len(autores) > 1 else ""]
            elif s1 and re.fullmatch(r"\d+-\d+", s1) and "pen" in nota.lower():   # jogo único decidido nos pênaltis
                saida[-2] = saida[-2] + f"  {nota}"
            i = j
        return "\n".join(saida)
    return f


MESES_PT = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6, "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}
COLCHETE = re.compile(r"^\[(?P<d>\d{1,2}) (?P<m>[a-z]{3}) (?P<a>\d{2})\]\s+(?P<h>\d{1,2}:\d{2})\s+(?P<man>\S.*?)\s{2,}(?P<g>\d+-\d+)\s+"
                      r"(?P<vis>\S.*?)(?:\s{2,}PK:\s*(?P<pk>\d+-\d+))?\s{2,}(?P<est>\S.*?)(?:\s{2,}\[(?P<gols>.*)\])?\s*$")


def _colchete(t: str) -> str:
    """2020 a 2023: "[09 mar 21]  19:15 Mandante-UF  0-1 Visitante-UF  Estádio-Cidade-UF  [autores]". Vira o formato de
    planilha que o leitor comum já conhece ("09/mar/21  19:15 Estádio  Mandante  0-1 Visitante  autores")."""
    saida = []
    for l in t.split("\n"):
        m = COLCHETE.match(l.strip())
        if m:
            pen = f"  [pen {m['pk']}]" if m["pk"] else ""   # "PK: 3-5" entre o visitante e o estádio
            l = f"{m['d']}/{m['m']}/{m['a']}  {m['h']} {m['est']}  {m['man']}  {m['g']} {m['vis']}  {m['gols'] or ''}{pen}".rstrip()
        saida.append(l)
    return "\n".join(saida)


LINHA_2024 = re.compile(r"^\s*(?P<h>\d{1,2}:\d{2})\s+(?P<est>\S.*?)\s{2,}(?P<man>\S.*?)\s{2,}(?P<g>\d+-\d+)\s+(?P<vis>\S.*?)(?:\s{2,}(?P<gols>.*))?\s*$")


def _2024(t: str) -> str:
    """2024: a data vem numa linha ("[fev 20]") e o jogo em outra ("16:30 Estádio/Cidade  Mandante-UF  1-0  Visitante-UF  autores"),
    com os autores no formato "13' (9-Diego da Silva); 59' (9-Fulano), 68' (...)pk" (";" separa mandante e visitante; "pk" =
    pênalti; "ct" = contra). Vira o formato de planilha, com os autores como o leitor de planilha espera ("Nome 13' (1ºT)")."""
    saida, data = [], None
    for l in t.split("\n"):
        md = re.match(r"^\s*\[(?P<m>[a-z]{3}) (?P<d>\d{1,2})\]\s*$", l)
        if md and md["m"] in MESES_PT:
            data = f"{int(md['d']):02d}/{md['m']}/24"
            continue
        m = LINHA_2024.match(l)
        if m and data:
            lados = []
            for parte in (m["gols"] or "").split(";"):
                itens = []
                for g in re.finditer(r"(?P<min>\d{1,3})'(?:\+(?P<ac>\d{1,2}))?\s*\(\d+-(?P<nome>[^)]+)\)\s*(?P<marca>pk|ct|og)?", parte, re.I):
                    minuto = f"{g['min']}+{g['ac']}" if g["ac"] else g["min"]
                    contra = "[og] " if (g["marca"] or "").lower() in ("ct", "og") else ""
                    itens.append(f"{contra}{g['nome'].strip()} {minuto}' (1ºT)")
                lados.append(", ".join(itens))
            gols = " |  ".join(lados) if len(lados) == 2 else (lados[0] if lados else "")
            l = f"{data}  {m['h']} {m['est']}  {m['man']}  {m['g']} {m['vis']}  {gols}".rstrip()
        saida.append(l)
    return "\n".join(saida)


def _sem_seletiva(t: str) -> str:
    """2001 e 2003: a página começa com uma seletiva estadual (Espírito Santo; Paraná x Coritiba), que não é Copa do Brasil:
    sai tudo do título da seletiva até o "First Round" da Copa."""
    i = t.find("Qualifying")
    j = t.find("\nFirst Round", i)
    return t[:t.rfind("\n", 0, i)] + t[j:] if 0 <= i < j else t


rsssf.CORRECOES.update({
    **{f"cbr{a}.htm": [(r"(\d+-\d+)\s+n/p\s+(?=\S)", r"\1  ", "volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida"),
                       (_numerados(a, a not in (2015, 2016)), None, "confrontos numerados numa linha só, com as datas da ida e da volta"
                        + ("; nesta edição o primeiro da linha manda a volta (ogol e autores confirmam)" if a in (2015, 2016) else ""))]
       for a in range(1989, 2019)},
    **{f"cbr{a}.htm": [(_colchete, None, "jogos com a data entre colchetes e o estádio depois do visitante")] for a in range(2020, 2024)},
    "cbr2024.htm": [(_2024, None, "data em linha própria e autores separados por ';' (mandante; visitante)")],
})

# em todas as páginas: "Grêmio (RS)" e "Grêmio(RS)" são a mesma grafia (1991 usa as duas)
for _a in range(1989, 2026):
    rsssf.CORRECOES[f"cbr{_a}.htm"] = [(r"(?<=[A-Za-zÀ-ú.]) \(([A-Z]{2})\)", r"(\1)", "espaço antes do '(UF)' tirado")] + \
        rsssf.CORRECOES.get(f"cbr{_a}.htm", [])

# correções de uma página só: vão antes das gerais da mesma página
for _arq, _lista in {
    "cbr1989.htm": [(r"^Semifinals(?=\S)", "Semifinals\n", "título 'Semifinals' colado no primeiro confronto da fase")],
    "cbr2000.htm": [(r"^(\s*)[A-H] (?=\S.*\d+-\d+)", r"\1", "oitavas com uma letra na frente de cada jogo ('E ABC (RN)  3-3  Palmeiras (SP)')")],
    "cbr2001.htm": [(_sem_seletiva, None, "seletiva do Espírito Santo no começo da página (não é Copa do Brasil)")],
    "cbr2003.htm": [(_sem_seletiva, None, "jogo seletivo Paraná x Coritiba no começo da página (não é Copa do Brasil)")],
}.items():
    rsssf.CORRECOES[_arq] = _lista + rsssf.CORRECOES.get(_arq, [])


def _grupo_limpo(g: str) -> str:
    """'Group APosTeamPTS...', 'GRUPO A', 'GROUP 01' -> 'Grupo A', 'Grupo 1'; 'GRUPO ÚNICO' fica."""
    m = re.match(r"^(?:group|grupo)\s+([A-Z]\d{1,2}|[A-Z]|\d{1,2})(?![a-z])", g.strip(), re.I)   # "A01" (2021) também
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
