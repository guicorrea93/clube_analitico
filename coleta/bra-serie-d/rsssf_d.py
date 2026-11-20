"""Leitura das páginas da Série D da RSSSF Brasil (data/coleta/bra-serie-d/rsssfbrasil/br{ano}l4.htm).

Usa o leitor comum (coleta/comum/rsssf.py) e, antes dele, corrige o texto de cada página que foge do
desenho comum (CORRECOES, com o motivo). A conferência compara cada tabela publicada com a soma dos jogos lidos.

Uso: python coleta/bra-serie-d/rsssf_d.py [ano ...]     (sem ano: todas; com um ano, lista as divergências)
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
rsssf.MODELO = "br{ano}l4.htm"

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
rsssf.CORRECOES.update({
    "br2013l4.htm": [_PK], "br2014l4.htm": [_PK], "br2015l4.htm": [_PK], "br2023l4.htm": [_PK],
})


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
