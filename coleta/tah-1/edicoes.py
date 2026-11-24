"""Edições da 1ª divisão do Taiti (tah-1): uma por título, como na lista de campeões da RSSSF (tahitichamp.html), de 1948 a
2025/26. Escopo aprovado pelo Guilherme em 24/11/2026:
- começa em 1948 (a lista oficial); a RSSSF dá o ano em que a temporada termina: "1999" é 1998/99, e assim por diante; antes
  de 1999 fica o ano da lista;
- até 2025/26 (a última terminada);
- em 1956, 1957 e 1961 vale a RSSSF (a Wikipédia diverge, mas copia uma versão antiga da própria RSSSF);
- entram a fase regular, o playoff do título (com o campeão de Mooréa, quando havia) e o grupo do rebaixamento; ficam de
  fora copas, 2ª e 3ª divisões, ligas das outras ilhas e as séries de acesso/rebaixamento com clubes da 2ª divisão
  ("Promotion/Relegation Playoff", "Playin").

O que a RSSSF traz:
- 1948-1967, 1972-1984, 1985 e 1986-1998: só o campeão (e o vice em 1990, 1992 e 1995-1998);
- 1968: 5 resultados e a classificação sem números; 1969-1971: as 14 rodadas e a tabela;
- 1998/99 a 2004/05: parte dos jogos (muitos só "venceu"/"perdeu", sem placar) e tabelas, às vezes parciais;
- 2005/06 a 2025/26: as rodadas e as tabelas (2010/11 e 2011/12: só as tabelas; 2009/10: o playoff numa seção à parte).

Pontuação (conferida pela conta das tabelas): 3-2-1 (vitória, empate, derrota) em 1969-1971 e 2007/08; 3-1-0 de 1998/99 a
2002/03; 4-2-1 em 2003/04-2006/07 e de 2008/09 em diante. Há pontos-bônus (vencedor da fase regular, obrigações com
treinadores, árbitros e categorias de base) e pontos tirados: ficam no ajuste da classificação.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "tah-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

UNICA = "Fase única"
LIGA = "Fase regular"
TITULO = "Playoff do título"
REBAIX = "Grupo do rebaixamento"
SEMI = "Semifinal"
FINAL = "Final"


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    nome_oficial: str
    trechos: list[tuple[str, int, int, str, str]]
    pontos: tuple[int, int, int] | None     # (vitória, empate, derrota); None = não se sabe
    obs: str = ""
    incompleta: str = ""
    acumula: bool = False                   # tabelas do playoff somam a fase regular


def temporada(ano_lista: int) -> tuple[str, int, int]:
    """Ano da lista da RSSSF -> (temporada, ano de início, ano de fim). A partir de 1999 a temporada cruza o ano."""
    if ano_lista >= 1999:
        return f"{ano_lista - 1}/{ano_lista % 100:02d}", ano_lista - 1, ano_lista
    return str(ano_lista), ano_lista, ano_lista


_P = {"3-2-1": (3, 2, 1), "3-1-0": (3, 1, 0), "4-2-1": (4, 2, 1)}
_PARCIAL = ("a página da RSSSF traz só parte dos jogos (muitos só com \"venceu\"/\"perdeu\", sem placar, que ficam de fora) e "
            "tabelas às vezes parciais")
# ano da lista -> (trechos, pontuação, observação, incompleta, acumula)
_PAGINAS: dict[int, tuple] = {
    1968: ([("tahiti68", 12, 44, UNICA, "")], None, "", "só 5 resultados e a classificação sem números (Journal de Tahiti)"),
    1969: ([("tahiti69", 30, 180, UNICA, "")], "3-2-1"),
    1970: ([("tahiti70", 32, 189, UNICA, "")], "3-2-1"),
    1971: ([("tahiti71", 28, 181, UNICA, "")], "3-2-1"),
    1999: ([("tahiti99", 13, 31, UNICA, "")], "3-1-0", "", _PARCIAL),
    2000: ([("tahiti00", 12, 98, UNICA, "")], "3-1-0", "", _PARCIAL),
    2001: ([("tahiti01", 12, 108, UNICA, "")], "3-1-0", "", _PARCIAL),
    2002: ([("tahiti02", 13, 102, LIGA, ""), ("tahiti02", 102, 147, TITULO, ""), ("tahiti02", 147, 159, REBAIX, "")], "3-1-0",
           "o Juventus abandonou o campeonato no meio da temporada", _PARCIAL, True),
    2003: ([("tahiti03", 15, 200, LIGA, ""), ("tahiti03", 200, 292, TITULO, ""), ("tahiti03", 292, 387, REBAIX, "")], "3-1-0",
           "", _PARCIAL, True),
    2004: ([("tahiti04", 15, 169, LIGA, ""), ("tahiti04", 169, 212, TITULO, ""), ("tahiti04", 212, 255, REBAIX, "")], "4-2-1",
           "", _PARCIAL),
    2005: ([("tahiti05", 14, 42, LIGA, ""), ("tahiti05", 42, 83, TITULO, ""), ("tahiti05", 83, 119, REBAIX, "")], "4-2-1",
           "", _PARCIAL),
    2006: ([("tahiti06", 12, 213, LIGA, ""), ("tahiti06", 213, 300, TITULO, ""), ("tahiti06", 300, 353, REBAIX, "")], "4-2-1"),
    2007: ([("tahiti07", 12, 203, LIGA, ""), ("tahiti07", 203, 281, TITULO, ""), ("tahiti07", 281, 341, REBAIX, "")], "4-2-1"),
    2008: ([("tahiti08", 12, 281, LIGA, ""), ("tahiti08", 281, 356, TITULO, ""), ("tahiti08", 356, 421, REBAIX, "")], "3-2-1"),
    2009: ([("tahiti09", 16, 259, LIGA, ""), ("tahiti09", 259, 459, TITULO, "")], "4-2-1",
           "a seleção sub-20 do Taiti (\"Tahiti U-20\") jogou a fase regular no lugar de um clube"),
    2010: ([("tahiti2010", 37, 265, LIGA, ""), ("tahiti2010", 639, 778, TITULO, "")], "4-2-1"),
    2011: ([("tahiti2011", 29, 238, LIGA, ""), ("tahiti2011", 238, 257, TITULO, "")], "4-2-1", "",
           "o playoff do título só tem a tabela na RSSSF"),
    2012: ([("tahiti2012", 29, 46, LIGA, ""), ("tahiti2012", 46, 63, TITULO, "")], "4-2-1", "",
           "a RSSSF só tem as tabelas da fase regular e do playoff do título"),
    2013: ([("tahiti2013", 33, 186, LIGA, ""), ("tahiti2013", 186, 280, TITULO, "")], "4-2-1"),
    2014: ([("tahiti2014", 33, 159, LIGA, ""), ("tahiti2014", 159, 255, TITULO, "")], "4-2-1"),
    2015: ([("tahiti2015", 35, 154, LIGA, ""), ("tahiti2015", 154, 242, TITULO, "")], "4-2-1"),
    2016: ([("tahiti2016", 33, 241, LIGA, ""), ("tahiti2016", 241, 247, SEMI, ""), ("tahiti2016", 247, 251, FINAL, "")], "4-2-1"),
    2017: ([("tahiti2017", 33, 305, LIGA, ""), ("tahiti2017", 305, 311, SEMI, ""), ("tahiti2017", 311, 318, FINAL, "")], "4-2-1"),
    2018: ([("tahiti2018", 32, 314, UNICA, "")], "4-2-1"),
    2019: ([("tahiti2019", 30, 323, UNICA, "")], "4-2-1"),
    2020: ([("tahiti2020", 28, 248, UNICA, "")], "4-2-1",
           "temporada interrompida pela covid-19; o AS Pirae, 1º da tabela, foi declarado campeão"),
    2021: ([("tahiti2021", 42, 235, LIGA, ""), ("tahiti2021", 235, 321, TITULO, ""), ("tahiti2021", 321, 410, REBAIX, "")], "4-2-1",
           "covid-19: turno único na fase regular, depois os playoffs"),
    2022: ([("tahiti2022", 36, 315, UNICA, "")], "4-2-1"),
    2023: ([("tahiti2023", 36, 185, LIGA, ""), ("tahiti2023", 185, 278, TITULO, ""), ("tahiti2023", 278, 373, REBAIX, "")], "4-2-1"),
    2024: ([("tahiti2024", 39, 188, LIGA, ""), ("tahiti2024", 188, 277, TITULO, ""), ("tahiti2024", 277, 375, REBAIX, "")], "4-2-1"),
    2025: ([("tahiti2025", 34, 339, UNICA, "")], "4-2-1"),
    2026: ([("tahiti2026", 37, 152, LIGA, ""), ("tahiti2026", 152, 291, TITULO, ""), ("tahiti2026", 291, 410, REBAIX, "")], "4-2-1"),
}

EDICOES: list[Edicao] = []
for _a in range(1948, 2027):
    _t, _i, _f = temporada(_a)
    _nome = ("Division d'Honneur" if _a < 2004 else "Division Fédérale" if _a < 2009 else "Ligue 1") + f" {_t}"
    _x = _PAGINAS.get(_a)
    if _x is None:
        EDICOES.append(Edicao(_t, _i, _f, _nome, [], None, obs="só o campeão na lista da RSSSF" + (
            " (e o vice, AS Pirae)" if _a in (1990, 1992, 1995, 1996, 1997, 1998) else "")))
        continue
    _tr, _pts = _x[0], _P.get(_x[1]) if _x[1] else None
    EDICOES.append(Edicao(_t, _i, _f, _nome, _tr, _pts, *(_x[2:] + ("", "", False)[len(_x) - 2:])))
