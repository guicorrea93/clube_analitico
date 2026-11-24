"""Edições da 1ª divisão da Nova Caledônia (ncl-1): uma por título, como na lista de campeões da RSSSF (newcalchamp.html), de
1950 a 2026. Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo:
- começa em 1950 (1933 e 1934-1949 ficam de fora); 1955 (sem campeão) e 2024 (abandonada, a federação não declarou campeão)
  não entram;
- 1963 e 1964: Club Sportif Militaire (RSSSF atual; a versão antiga, copiada por Wikipédia e ogol, dava USC e JS Vallée du Tir);
- até 2001 entra só a fase nacional (as ligas das províncias eram competições regionais à parte); de 2002 a 2011 a liga da
  Grande Terre entra como 1ª fase ("Fase regional", grupo "Grande Terre") e o campeão das ilhas entra direto no playoff (o
  torneio das ilhas fica de fora); de 2012 em diante, a Super Ligue única.

O que a RSSSF traz:
- 1950-1988: só o campeão (a final na lista em 1964, 1971, 1977 e 1978; página com a final em 1984 e o mata-mata em 1985);
- 1989-1996: campeão, vice e 3º (em parte dos anos);
- 1997-2001: mata-mata nacional (1997 e 1998 em parte; 1999-2001 completo);
- 2002-2011: liga da Grande Terre e o playoff/mata-mata nacional (2005/06 e 2009 sem playoff: o campeão da Grande Terre);
- 2012-2026: Super Ligue (2020 com playoff do título; 2025 com grupos e mata-mata).

Pontuação: 4 por vitória, 2 por empate e 1 por derrota (a RSSSF anota desde 1999). Temporadas que cruzam o ano: 2002/03 a 2008/09.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "comum-oceania"))
import rsssf_oce  # noqa: E402

SLUG = "ncl-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

UNICA = "Fase única"
REGIONAL = "Fase regional"
REBAIX = "Grupo do rebaixamento"
GRUPOS = "Fase de grupos"
TITULO = "Playoff do título"
ELIM = "Rodada preliminar"
QUARTAS = "Quartas de final"
SEMI = "Semifinal"
TERCEIRO = "Disputa do 3º lugar"
FINAL = "Final"
GT = "Grande Terre"


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


_421 = (4, 2, 1)
_PARCIAL = "a página da RSSSF traz só parte dos jogos do mata-mata"
# temporada -> (trechos, pontuação, observação, incompleta, acumula)
_PAGINAS: dict[str, tuple] = {
    "1984": ([("newcal84", 14, 18, FINAL, "")], None),
    "1985": ([("newcal85", 15, 19, ELIM, ""), ("newcal85", 19, 23, SEMI, ""), ("newcal85", 23, 27, FINAL, "")], None),
    "1997": ([("newcal97", 19, 22, SEMI, ""), ("newcal97", 22, 26, FINAL, "")], None, "", _PARCIAL),
    "1998": ([("newcal98", 15, 19, SEMI, ""), ("newcal98", 19, 22, FINAL, "")], None),
    "1999": ([("newcal99", 99, 115, QUARTAS, ""), ("newcal99", 115, 125, SEMI, ""), ("newcal99", 125, 129, FINAL, "")], _421),
    "2000": ([("newcal00", 20, 34, QUARTAS, ""), ("newcal00", 34, 46, SEMI, ""), ("newcal00", 46, 50, FINAL, "")], _421),
    "2001": ([("newcal01", 33, 46, QUARTAS, ""), ("newcal01", 46, 59, SEMI, ""), ("newcal01", 59, 63, FINAL, "")], _421),
    "2002": ([("newcal02", 37, 170, REGIONAL, GT), ("newcal02", 20, 33, SEMI, ""), ("newcal02", 33, 37, FINAL, "")], _421),
    "2002/03": ([("newcal03", 46, 228, REGIONAL, GT), ("newcal03", 21, 31, SEMI, ""), ("newcal03", 31, 46, FINAL, "")], _421),
    "2003/04": ([("newcal04", 37, 249, REGIONAL, GT), ("newcal04", 20, 32, SEMI, ""), ("newcal04", 32, 37, FINAL, "")], _421),
    "2004/05": ([("newcal05", 50, 308, REGIONAL, GT), ("newcal05", 23, 33, SEMI, ""), ("newcal05", 33, 50, FINAL, "")], _421),
    "2005/06": ([("newcal06", 14, 146, UNICA, "")], _421, "não houve playoff nacional: o campeão da Grande Terre é o campeão"),
    "2006/07": ([("newcal07", 56, 186, REGIONAL, GT), ("newcal07", 186, 272, REBAIX, GT), ("newcal07", 12, 56, TITULO, "")], _421,
                "", "", True),
    "2007/08": ([("newcal08", 76, 274, REGIONAL, GT), ("newcal08", 274, 340, REBAIX, GT), ("newcal08", 14, 74, TITULO, "")], _421,
                "no grupo do rebaixamento da Grande Terre os clubes levam um bônus da fase regular"),
    "2008/09": ([("newcal09", 89, 333, REGIONAL, GT), ("newcal09", 333, 387, REBAIX, GT), ("newcal09", 14, 87, TITULO, "")], _421),
    "2009": ([("newcal2009", 31, 246, UNICA, "")], _421, "não houve playoff nacional: o campeão da Super Ligue (Grande Terre) "
             "é o campeão (o calendário passou a ser o ano civil)"),
    "2010": ([("newcal2010", 124, 335, REGIONAL, GT), ("newcal2010", 26, 124, TITULO, "")], _421),
    "2011": ([("newcal2011", 102, 273, REGIONAL, GT), ("newcal2011", 24, 102, TITULO, "")], _421),
    "2020": ([("newcal2020", 29, 158, UNICA, ""), ("newcal2020", 158, 190, TITULO, "")], _421),
    "2025": ([("newcal2025", 25, 144, GRUPOS, ""), ("newcal2025", 144, 150, ELIM, ""), ("newcal2025", 150, 159, QUARTAS, ""),
              ("newcal2025", 159, 163, SEMI, ""), ("newcal2025", 163, 166, TERCEIRO, ""), ("newcal2025", 166, 173, FINAL, "")], _421,
             "a liga voltou em maio de 2025, depois de um ano parada pelos distúrbios civis, num formato adaptado (grupos e mata-mata)"),
}
_FIM_SL = re.compile(r"^(Promotion/Relegation|Coupe de Cal|Grande Terre - Promotion|Championnat des [IÎ]les|Promotion d'Honneur|OFC)",
                     re.I)


def _super_ligue(ano: int) -> tuple[str, int, int]:
    """Trecho da Super Ligue numa página de 2012 em diante: do 2º título "Super Ligue <ano>" (o 1º é o índice) até a próxima
    competição."""
    pg = f"newcal{ano}"
    ls = rsssf_oce.texto(PASTA_DADOS / "rsssf" / f"{pg}.html")
    tit = [i for i, l in enumerate(ls) if l.strip() == f"Super Ligue {ano}"]
    ini = tit[1] if len(tit) > 1 else tit[0]
    fim = next((i for i, l in enumerate(ls) if i > ini and _FIM_SL.match(l.strip())), len(ls))
    return pg, ini, fim


def _lista() -> list[tuple[str, str]]:
    """(temporada, linha) da lista de campeões da RSSSF, de 1950 em diante, sem os anos sem campeão."""
    out = []
    for l in rsssf_oce.texto(PASTA_DADOS / "rsssf" / "newcalchamp.html"):
        m = re.match(r"^\[?\*?\]?\s*(\d{4}(?:/\d{2})?)\s+(\S.*)$", l)
        if m and int(m.group(1)[:4]) >= 1950 and not re.search(r"not awarded|unknown|abandoned", l):
            out.append((m.group(1), l))
    return out


EDICOES: list[Edicao] = []
for _t, _l in _lista():
    _i = int(_t[:4])
    _f = _i + 1 if "/" in _t else _i
    _nome = ("Championnat territorial" if _i < 2002 else "Division d'Honneur (Grande Terre) e Championnat de Nouvelle-Calédonie"
             if _i < 2007 else "Super Ligue" + (" (Grande Terre) e Championnat de Nouvelle-Calédonie" if _i < 2012 else "")) + f" {_t}"
    if _t in _PAGINAS:
        _x = _PAGINAS[_t]
        EDICOES.append(Edicao(_t, _i, _f, _nome, _x[0], _x[1], *(_x[2:] + ("", "", False)[len(_x) - 2:])))
    elif _i >= 2012:
        EDICOES.append(Edicao(_t, _i, _f, _nome, [(*_super_ligue(_i), UNICA, "")], _421))
    else:
        EDICOES.append(Edicao(_t, _i, _f, _nome, [], None, obs="só o campeão na lista da RSSSF"))
