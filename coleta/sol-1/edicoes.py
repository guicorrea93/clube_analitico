"""Edições da 1ª divisão das Ilhas Salomão (sol-1), uma por título, como na lista de campeões da RSSSF (solomchamp.html):
o campeonato nacional de clubes (National Club Championship, 2000 a 2009/10: torneio curto com os melhores de Honiara e os
campeões das províncias) e a Telekom S-League (2010/11 a 2024; "S-League" em 2025). Escopo aprovado pelo Guilherme em
25/11/2026, depois de pesquisa a fundo:
- fora: a liga de Honiara (1947-1999, regional, só campeões), a "S-League" de franquias de Honiara (2004 e 2005), a Solomon
  Cup e o Interprovincial (seleções de província), o Knockout Championship e os playoffs da OFC;
- 2000-2002 só com o campeão; 2004 só com a final (por W.O.); 2011/12 só a tabela; 2012/13 não houve; 2026 fica de fora até
  o título sair (depende de punições ainda pendentes na federação);
- 2015/16: campeão o Western United, que ganhou o playoff final (RSSSF); o Solomon Warriors, campeão pela Wikipédia, foi o
  1º da fase regular. 2017/18: o Solomon Warriors ganhou a fase regular e o playoff ("TSL Championship 2018").

A RSSSF nomeia a página pelo ano em que a temporada termina (solom2016 = 2015/16, solom2017 = 2016); a de 2006 (solom06) traz o
campeonato de fevereiro de 2006, que a lista chama de 2005/06. Pontuação 3-1-0.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "sol-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

UNICA = "Fase única"
LIGA = "Fase regular"
REGIONAL = "Fase regional"
GRUPOS = "Fase de grupos"
TITULO = "Grupo do título"
REBAIX = "Grupo do rebaixamento"
PLAYOFF_CONF = "Playoff da conferência"
QUARTAS = "Quartas de final"
SEMI = "Semifinal"
TERCEIRO = "Disputa do 3º lugar"
FINAL = "Final"


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    nome_oficial: str
    trechos: list[tuple[str, int, int, str, str]]
    pontos: tuple[int, int, int] | None
    obs: str = ""
    incompleta: str = ""
    acumula: bool = False


def _mm(pg: str, primeira: tuple[int, int, str], quartas: int | None, semi: int, ter: int | None, fin: int, fim: int) -> list:
    """1ª fase (grupos ou liga) e o mata-mata: quartas (se houver), semifinais, 3º lugar (se houver) e final."""
    tr = [(pg, primeira[0], primeira[1], primeira[2], "")]
    if quartas:
        tr.append((pg, quartas, semi, QUARTAS, ""))
    tr.append((pg, semi, ter or fin, SEMI, ""))
    if ter:
        tr.append((pg, ter, fin, TERCEIRO, ""))
    return tr + [(pg, fin, fim, FINAL, "")]


# (temporada, ano inicial, ano final, trechos, observação, edição incompleta)
_ED: list[tuple] = [
    ("2000", 2000, 2000, [], "só o campeão na RSSSF", ""),
    ("2001", 2001, 2001, [], "só o campeão na RSSSF", ""),
    ("2002", 2002, 2002, [], "só o campeão na RSSSF", ""),
    ("2003", 2003, 2003, _mm("solom03", (12, 49, GRUPOS), None, 49, 53, 56, 59), "em Yandina, em novembro", ""),
    ("2004", 2004, 2004, [("solom04", 27, 30, FINAL, "")],
     "a RSSSF dá os 9 inscritos (2 grupos) e a final, vencida por W.O.: o Makuru, de dono adventista, não joga aos sábados",
     "só a final na RSSSF"),
    ("2005/06", 2005, 2006, _mm("solom06", (12, 79, GRUPOS), None, 79, 86, 89, 95), "em Honiara, de 20/02 a 01/03/2006",
     "a página dá alguns jogos da fase de grupos sem placar (só \"drw\" ou \"bt\")"),
    ("2006/07", 2006, 2007, _mm("solom07", (12, 84, GRUPOS), None, 84, None, 88, 95), "em maio de 2007",
     "a página não traz o placar de 4 jogos da fase de grupos (as tabelas são parciais)"),
    ("2007/08", 2007, 2008, _mm("solom08", (12, 143, GRUPOS), None, 143, 149, 153, 175), "em junho de 2008", ""),
    ("2008/09", 2008, 2009, _mm("solom09", (12, 116, GRUPOS), None, 116, 122, 127, 132), "em junho de 2009", ""),
    ("2009/10", 2009, 2010, _mm("solom2010", (50, 142, GRUPOS), 142, 154, 158, 161, 167), "em maio de 2010", ""),
    ("2010/11", 2010, 2011, [("solom2011", 19, 179, UNICA, "")], "1ª Telekom S-League (fevereiro a maio de 2011)",
     "a página não traz o placar dos 4 jogos da 12ª rodada"),
    ("2011/12", 2011, 2012, [("solom2012", 17, 37, UNICA, "")], "", "a RSSSF só tem a tabela final"),
    ("2013/14", 2013, 2014, [("solom2013", 17, 217, UNICA, "")],
     "Marist desclassificado em 08/11 (não pagou a inscrição): os jogos do 1º turno viraram 0-3", ""),
    ("2014/15", 2014, 2015, [("solom2015", 17, 213, UNICA, "")], "", ""),
    ("2015/16", 2015, 2016, _mm("solom2016", (22, 217, LIGA), 217, 237, 243, 246, 253),
     "fase regular (1º o Solomon Warriors) e playoff dos 8 primeiros; o campeão é o do playoff (RSSSF; a Wikipédia dá o "
     "Solomon Warriors)",
     "o jogo de volta Western United x Real Kakamora (quartas) está na página sem placar (\"unk\", 2-1 no intervalo)"),
    ("2016", 2016, 2016, [("solom2017", 17, 234, UNICA, "")],
     "Koloale suspenso em 04/12 (\"non-compliance\"): os 5 jogos restantes viraram 0-3", ""),
    ("2017/18", 2017, 2018, _mm("solom2018", (26, 176, LIGA), 176, 199, 205, 208, 214),
     "fase regular (agosto a novembro de 2017) e o playoff dos 8 primeiros (\"TSL Championship\", março de 2018); o Solomon "
     "Warriors ganhou os dois", ""),
    ("2018", 2018, 2018, [("solom2019", 17, 171, UNICA, "")], "", ""),
    ("2019/20", 2019, 2020, [("solom2020", 17, 223, UNICA, "")], "", ""),
    ("2020/21", 2020, 2021, [("solom2021", 17, 321, UNICA, "")], "", ""),
    ("2021", 2021, 2021, [("solom2022", 19, 291, UNICA, "")], "", ""),
    ("2022/23", 2022, 2023, [("solom2023", 25, 307, UNICA, "")], "", ""),
    ("2023", 2023, 2023, [("solom2023a", 15, 303, UNICA, "")], "", ""),
    ("2024", 2024, 2024, [("solom2024", 15, 286, UNICA, "")], "", ""),
    ("2025", 2025, 2025, [("solom2025", 19, 299, UNICA, "")], "a liga passa a se chamar só \"S-League\"", ""),
]

EDICOES: list[Edicao] = []
for _t, _i, _f, _tr, _obs, _inc in _ED:
    _nome = ("National Club Championship " if _i < 2010 else "S-League " if _i >= 2025 else "Telekom S-League ") + _t
    EDICOES.append(Edicao(_t, _i, _f, _nome, _tr, (3, 1, 0) if _tr else None, obs=_obs, incompleta=_inc))
