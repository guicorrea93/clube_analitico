"""Edições da 1ª divisão de Fiji (fij-1): a liga das associações dos distritos ("League Championship", hoje Fiji Premier
League), uma por ano, como na lista de campeões da RSSSF (fijichamp.html), de 1977 a 2026. Escopo aprovado pelo Guilherme
em 24/11/2026, depois de pesquisa a fundo:
- RSSSF e Wikipédia batem em todos os anos; 2003 = Ba (a federação deu o título em 2006: os Olympians, 1º na tabela, já não
  existiam); 2010 = Ba (o título dado ao Lautoka no tribunal foi revogado);
- ficam de fora o Inter-District Championship, o National Club Championship, a Club Franchise League (2004/05-2006), as copas
  (Battle of the Giants, FACT, Champion vs Champion), a 2ª divisão e as repescagens com ela.

O que a RSSSF traz da liga:
- 1977-1982, 1987, 1989-1992, 1995, 1996: só o campeão (às vezes o vice: "Runners-Up");
- 1983-1986, 1988, 1993, 1994, 1997: a tabela final (1993 só a ordem), sem jogos;
- 1998 em diante: as rodadas e a tabela (2005, 2007 e 2008 com grupo do título e grupo do rebaixamento; 2011 e 2012 só a
  tabela: os jogos de 2011 vêm do ogol, conferidos com ela; o de 2012 não fecha e fica de fora).

Pontuação: 2 por vitória até 1986 (conta das tabelas), 3 a partir de 1988 (1987 sem tabela).

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

SLUG = "fij-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

UNICA = "Fase única"
LIGA = "Fase regular"
GRUPOS = "Fase de grupos"
TITULO = "Grupo do título"
REBAIX = "Grupo do rebaixamento"


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


def _pg(a: int) -> str:
    return f"fiji{a % 100:02d}" if a < 2010 else f"fiji{a}"


# início da liga na página: o título (o 2º, quando o 1º é o índice do topo)
_INI = re.compile(r"^(Super Premier League \(First|Pepsi Football League \(First|NewWorld National Football League|Fiji Sun/Weet-Bix|"
                  r"National Football League$|Galaxy Premier League$|Premier League$|Fiji National League 1983|National Soccer League|"
                  r"Premier Division$|Coca Cola Fijian National League)")
_FIM = re.compile(r"^(Promotion/Relegation|Premier League \(Second|Premier Division|Senior (League|Division)|Galaxy Senior League|"
                  r"Cup Tournaments|Fiji Cups?|Fiji Bitter|National Club Championship|Interdistrict|Inter[- ]?[Dd]istrict|INTERDISTRICT|"
                  r"Battle of|FACT|Champion|.*District Club Championship|.*Local League|Super Premier League$|Regional Leagues|"
                  r"Club Championship|Inter Club|OFC Champions League|South Pacific Games|Fiji Football Association Club|Lautoka Super Premier|Suva Super Premier)")


def _trecho(a: int) -> tuple[str, int, int]:
    pg = _pg(a)
    ls = rsssf_oce.texto(PASTA_DADOS / "rsssf" / f"{pg}.html")
    tit = [i for i, l in enumerate(ls) if i > 9 and _INI.match(l.strip())]
    # o índice do topo repete os títulos: vale o primeiro título seguido (logo abaixo) de tabela ou de rodada
    ini = next(i for i in tit if any(re.match(r"^((Final )?Table|Round 1\b|Regular|Pool|NB)", x.strip()) for x in ls[i + 1:i + 12]))
    fim = next((i for i, l in enumerate(ls) if i > ini + 2 and _FIM.match(l.strip())
                and not l.strip().startswith(ls[ini].strip()[:12])), len(ls))
    return pg, ini, fim


_PAGINAS: dict[int, list] = {
    1983: [("fiji83", 12, 29, UNICA, "")], 1984: [("fiji84", 12, 25, UNICA, "")], 1985: [("fiji85", 12, 25, UNICA, "")],
    1986: [("fiji86", 12, 26, UNICA, "")], 1988: [("fiji88", 13, 27, UNICA, "")], 1994: [("fiji94", 12, 34, UNICA, "")],
    1997: [("fiji97", 13, 28, UNICA, "")],
    2003: [("fiji03", 12, 170, UNICA, ""), ("fiji03", 264, 305, UNICA, "")],   # os Jogos do Pacífico Sul no meio da página
    2005: [("fiji05", 107, 236, GRUPOS, ""), ("fiji05", 236, 340, TITULO, ""), ("fiji05", 340, 397, REBAIX, "")],
    2007: [("fiji07", 14, 136, LIGA, ""), ("fiji07", 136, 257, TITULO, ""), ("fiji07", 257, 315, REBAIX, "")],
    2008: [("fiji08", 12, 212, LIGA, ""), ("fiji08", 212, 337, TITULO, ""), ("fiji08", 337, 402, REBAIX, "")],
}
# 1998-2004: as páginas trazem só parte dos jogos (as tabelas são "based on known results" ou a final publicada, sem todos os
# jogos que a formam)
_PARCIAL = {a: "a página da RSSSF traz só parte dos jogos (a tabela é a publicada)" for a in range(1998, 2005)}
_SEM_PAGINA = {1977, 1978, 1979, 1980, 1981, 1982, 1987, 1989, 1990, 1991, 1992, 1993, 1995, 1996}

EDICOES: list[Edicao] = []
for _a in range(1977, 2027):
    _nome = f"National Football League {_a}" if _a < 2015 else f"Fiji Premier League {_a}"
    _pts = (2, 1, 0) if _a <= 1986 else (3, 1, 0) if _a >= 1988 else None
    if _a in _SEM_PAGINA:
        EDICOES.append(Edicao(str(_a), _a, _a, _nome, [], None, obs="só o campeão na RSSSF"))
    elif _a in _PAGINAS:
        EDICOES.append(Edicao(str(_a), _a, _a, _nome, _PAGINAS[_a], _pts,
                              obs="grupos, depois o Super 6 (título) e o Pepsi 4 (rebaixamento)" if _a == 2005 else "",
                              incompleta=_PARCIAL.get(_a, "") if _a >= 1998 else "só a tabela final na RSSSF"))
    else:
        EDICOES.append(Edicao(str(_a), _a, _a, _nome, [(*_trecho(_a), UNICA, "")], _pts,
                              incompleta=_PARCIAL.get(_a, "") or ("a RSSSF só tem a tabela; o calendário do ogol diverge dela em 7 "
                                                                   "clubes e falta um jogo, por isso não entra" if _a == 2012 else "")))
