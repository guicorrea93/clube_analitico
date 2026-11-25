"""Copa Colombia (col-copa): copa nacional da Dimayor. Quarta das sete copas da América do Sul (decisões do Guilherme de
24/11/2026 em coleta/comum-sulamerica/copas-nacionais.md): contagem da Wikipédia em espanhol, que conta 1950-51, 1952-53,
1956-57 (cancelada, sem campeão) e 2008-2025; não conta 1951-52 (rodadas da de 1952-53), 1963 (troféu comemorativo), 1981 e
1989 (torneios dentro da liga). As antigas entram com aviso: a RSSSF (colcuphist.html) só traz os jogos dos clubes de
Medellín e a final.

Fontes (um importador comum: coleta/comum-sulamerica/copa_rsssf.py):
- RSSSF: colcuphist.html (antigas; em data/coleta/col-copa/rsssf/) e a seção da copa nas páginas do ano do col-1 (col08 ...
  col2025): 2008-2010, 2018 e 2020-2023 completas; nos outros anos só o mata-mata (2011 e 2012, das quartas em diante;
  2013-2017 e 2019, das oitavas; 2024 e 2025, das oitavas);
- Wikipédia em espanhol ("Copa Colombia <ano>", em data/coleta/col-copa/wikipedia/; wiki_copa.py) para o que falta: a fase
  de grupos de 2011-2017 e 2019, as oitavas de 2011 e 2012, as fases I a III de 2024 e a 1ª fase de 2025;
- campeão conferido com a Wikipédia em espanhol ("Copa Colombia").

Uso: python coleta/col-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from datetime import timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "col-1"))
import autores  # noqa: E402  (o do col-1)
import ler_rsssf  # noqa: E402  (o do col-1: páginas em data/coleta/col-1/rsssf)
import rsssf_sul  # noqa: E402
import wiki_copa  # noqa: E402
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, espn_arquivos, importar  # noqa: E402

SLUG = "col-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"
HIST = RAIZ / "data" / "coleta" / SLUG / "rsssf" / "colcuphist.html"


def linhas(pagina: str) -> tuple[str, ...]:
    return tuple(rsssf_sul.texto(HIST)) if pagina == "colcuphist" else ler_rsssf.linhas(pagina)


# ordem geral das fases (a última é a final); os títulos de cada formato estão nas listas por edição, abaixo
FASES = [
    (r"^Fase I\b(?!I)", "Fase I"), (r"^Fase II\b(?!I)", "Fase II"), (r"^Fase III", "Fase III"),
    (r"^NUNCA$", "Fase de grupos"),
    (r"^NUNCA$", "Primeira fase"), (r"^NUNCA$", "Segunda fase"), (r"^NUNCA$", "Segunda fase (repescagem)"),
    (r"^NUNCA$", "Terceira fase"), (r"^NUNCA$", "Terceira fase (repescagem)"), (r"^NUNCA$", "Quarta fase (repescagem)"),
    (r"^1/8 Finals", "Oitavas de final"), (r"^Quarterfinals", "Quartas de final"), (r"^Semifinals", "Semifinal"),
    (r"^Final\b(?! Tables?)", "Final"),
]
_MATA = [(r"^1/8 Finals", "Oitavas de final"), (r"^Quarterfinals", "Quartas de final"), (r"^Semifinals", "Semifinal"),
         (r"^Final\b(?! Tables?)", "Final")]
F_ANTIGA = [(r"^Round 1\b", "Primeira fase"), (r"^Round 2 - Winners", "Segunda fase"),
            (r"^Round 2 - Losers", "Segunda fase (repescagem)"), (r"^Round 3 - Losers", "Terceira fase (repescagem)"),
            (r"^Round 4 - Losers", "Quarta fase (repescagem)"), (r"^Final\b", "Final")]
F_2008 = [(r"^First Phase", "Fase de grupos"), (r"^Second Phase", "Segunda fase"), (r"^Third Phase", "Terceira fase")] + _MATA
F_GRUPOS = [(r"^Group Stage", "Fase de grupos"), (r"^Knockout Stage", "Oitavas de final")] + _MATA   # 2013-2019
F_2018 = [(r"^Fase I\b(?!I)", "Fase I"), (r"^Fase II\b(?!I)", "Fase II"), (r"^Fase III", "Fase III")] + _MATA
F_2020 = [(r"^Round 1\b", "Primeira fase"), (r"^Round 2\b", "Segunda fase"), (r"^Round 3\b", "Terceira fase")] + _MATA


def _trecho(ano: int) -> tuple[str, int, int]:
    """Da última "Copa Colombia/Postobón/Águila" da página (as outras são o índice) até a "Primera B" ou a lista do fim."""
    pagina = f"col{ano % 100:02d}" if ano < 2010 else f"col{ano}"
    ls = linhas(pagina)
    ini = [i for i, l in enumerate(ls) if re.match(r"^Copa (Colombia|Postob|[ÁA]guila|BetPlay)", l.strip())][-1]
    fim = next(i for i in range(ini + 1, len(ls)) if re.match(r"^(Primera B|list of champions|About this document)", ls[i].strip()))
    return pagina, ini, fim


def _hist(titulo: str) -> tuple[str, int, int]:
    ls = linhas("colcuphist")
    ini = next(i for i, l in enumerate(ls) if l.strip() == titulo and i > 80)
    fim = next(i for i in range(ini + 1, len(ls)) if re.match(r"^(19\d\d(-\d\d)?)$", ls[i].strip()))
    return "colcuphist", ini, fim


_GRUPOS_WIKI = {2011: "linhas", 2012: "linhas", 2013: "linhas", 2014: "linhas", 2015: "modelo", 2016: "modelo",
                2017: "modelo", 2019: "modelo"}


def _extras(ano: int):
    """Jogos da Wikipédia que a RSSSF não tem, por ano."""
    def f():
        js = []
        if _GRUPOS_WIKI.get(ano) == "linhas":
            js += wiki_copa.grupos(ano)
        elif _GRUPOS_WIKI.get(ano) == "modelo":
            js += wiki_copa.wiki(ano, {"Fase de grupos"})
        if ano in (2011, 2012):
            js += wiki_copa.wiki(ano, {"Oitavas de final"})
        if ano == 2024:
            js += wiki_copa.llaves(ano, {"Fase I": "Fase I", "Fase II": "Fase II", "Fase III": "Fase III"})
        if ano == 2025:
            for j in wiki_copa.wiki(ano, {"Primera fase"}):
                j.fase = "Fase de grupos"
                js.append(j)
        return js
    return f if ano in _GRUPOS_WIKI or ano in (2011, 2012, 2024, 2025) else None


_AVISO = ("edição antiga reconhecida pela Wikipédia (a Dimayor a reconheceu em 2020 e a pôs em dúvida em 12/2025); a RSSSF só "
          "traz os jogos dos clubes de Medellín e a final")
EDICOES = [
    EdicaoCopa("1950-51", 1950, 1951, "Copa Colombia 1950-51", [_hist("1950-51")], fases=F_ANTIGA, obs=_AVISO),
    EdicaoCopa("1952-53", 1952, 1953, "Copa Colombia 1952-53", [_hist("1952-53")], fases=F_ANTIGA,
               obs=_AVISO + "; a final de volta foi dada por W.O. ao Millonarios segundo a Wikipédia (a RSSSF dá 3-0)"),
    EdicaoCopa("1956-57", 1956, 1957, "Copa Colombia 1956-57", [], fases=F_ANTIGA,
               obs="cancelada: o torneio final de 6 clubes nunca foi jogado (sem campeão); " + _AVISO.split(";")[0]),
]
for _a in range(2008, 2026):
    _f = F_2008 if _a <= 2010 else F_2018 if _a == 2018 else F_2020 if 2020 <= _a <= 2023 else F_GRUPOS
    EDICOES.append(EdicaoCopa(str(_a), _a, _a + (1 if _a == 2020 else 0), f"Copa Colombia {_a}", [_trecho(_a)], fases=_f,
                              extras=_extras(_a), fase_padrao="Fase de grupos" if _a <= 2010 else "",
                              obs="final em fevereiro de 2021 (a RSSSF a chama de 2020/21)" if _a == 2020 else ""))

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Colombia", "nome_curto": "Copa Colombia", "tipo": "copa", "nivel": None, "pais": "COL",
    "pais_nome": "Colômbia", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Colombia",
    "menu_painel": "Colômbia · Copa Colombia", "do_painel": "da Copa Colombia", "o_painel": "a Copa Colombia",
    "observacao": "Copa nacional da Dimayor (Primera A e Primera B) de 2008 em diante; as edições de 1950-51, 1952-53 e "
                  "1956-57 (cancelada) entram pela contagem da Wikipédia, com jogos parciais."}

# Wikipédia em espanhol, "Copa Colombia" (Historial)
CAMPEOES_WIKI = {"1950-51": "Boca Juniors de Cali", "1952-53": "Millonarios", "2008": "La Equidad", "2009": "Santa Fe",
                 "2010": "Deportivo Cali", "2011": "Millonarios", "2012": "Atlético Nacional", "2013": "Atlético Nacional",
                 "2014": "Deportes Tolima", "2015": "Junior", "2016": "Atlético Nacional", "2017": "Junior",
                 "2018": "Atlético Nacional", "2019": "Independiente Medellín", "2020": "Independiente Medellín",
                 "2021": "Atlético Nacional", "2022": "Millonarios", "2023": "Atlético Nacional", "2024": "Atlético Nacional",
                 "2025": "Atlético Nacional"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesc/{pagina}.html",
            # D5b: data, hora, estádio, cidade e público da ESPN (col.copa); Colômbia UTC-5, sem horário de verão
            espn=espn_arquivos(SLUG, "col.copa"), espn_corrige=True, fuso=lambda utc: utc - timedelta(hours=5))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
