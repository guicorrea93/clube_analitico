"""Edições da 1ª divisão paraguaia (par-1): uma por torneio que deu título de campeão paraguaio.

Lista de títulos: RSSSF (parachamp.html), conferida com a Wikipédia. De 1906 a 2007 um campeão por ano (sem campeonato em
1908, 1922 e 1932-1934); de 1996 a 2007 o Apertura e o Clausura são fases da edição anual, com a final entre os vencedores.
De 2008 em diante, Apertura e Clausura dão título cada um: uma edição por torneio. Ficam de fora a Copa Paraguay, a
Intermedia (2ª divisão), as liguillas e os jogos de promoção.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO). 1960-1967, 1981 e 1996 em diante.
- sem jogos (1906-1959, 1968-1980, 1982-1995): nenhuma fonte pública tem os jogos completos (pesquisa no relatório). Decisão
  do Guilherme (21/11/2026): a edição entra só com o campeão, o vice e a tabela parcial (posição e pontos) quando a RSSSF a
  traz (parahist.html e as páginas de 1968-1995); os jogos soltos que a RSSSF conhece ("Known Results") ficam de fora.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "par-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Intermedia|Divisi[oó]n Intermedia|Torneo Intermedia|Primera de Ascenso|Segunda de Ascenso|Segunda Divisi|"
              r"Copa Paraguay|Copa Sudamericana|Playoff for Copa|Relegation|Promedio|Promotion|Second Level|list of|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1950", "2003", "2008 Apertura"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: str | None = None                                       # (não usado)
    hist: str = ""                                                # (não usado)
    ogol: int | None = None                                       # (não usado: o ogol só tem jogos de 2005 em diante)
    espn: tuple[str, str] | None = None                           # (não usado)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # trecho com a tabela parcial (posição e pontos), sem jogos

    @property
    def pontos_vitoria(self) -> int:
        """2 pontos até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


_COM_JOGOS = {*range(1960, 1968), 1981}
_PAGINAS = {1943, 1945, 1955, *range(1960, 1971), *range(1981, 1996)}   # anos com página própria antes de 1996
EDICOES: list[Edicao] = []
for _a in range(1906, 1996):
    if _a in (1908, 1922, 1932, 1933, 1934):
        continue
    _nome = (f"Liga Paraguaya de Fútbol – Campeonato {_a}" if _a <= 1934 else f"Campeonato Paraguayo de Primera División {_a}")
    _pg = f"para{_a % 100:02d}" if _a in _PAGINAS else "parahist"
    if _a in _COM_JOGOS:
        EDICOES.append(_e(str(_a), _a, _a, [(_pg, 0, None)], _nome))
    else:
        EDICOES.append(_e(str(_a), _a, _a, [], _nome, tabelas=[(_pg, 0, None)] if _a in _PAGINAS else [],
                          obs="sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela "
                              "parcial)"))

# 1996-2007: Apertura e Clausura são fases da edição anual
_ANUAL = {1996: (12, 402), 1997: (12, 487), 1998: (12, 461), 1999: (12, 424), 2000: (0, 535), 2001: (12, 406), 2002: (12, 569),
          2003: (12, 580), 2004: (12, 637), 2005: (12, 662), 2006: (12, 816), 2007: (12, 748)}
_FASES_AC = [(r"(?i)^(Torneo |First Stage \()?Apertura", "Apertura"), (r"(?i)^(Torneo |Second Stage \()?Clausura(?! Championship)", "Clausura")]
_FASES_AC.append((r"(?i)^Liguilla$", "Liguilla"))   # liguilla que fecha o Apertura/Clausura (1998...)
for _a, (_i, _f) in _ANUAL.items():
    _tr = [(f"para{_a % 100:02d}", _i, _f)]
    if _a == 2005:
        _tr.append(("para05", 953, 971))   # a final do campeonato vem depois do playoff da Sudamericana
    EDICOES.append(_e(str(_a), _a, _a, _tr, f"Campeonato Paraguayo de Primera División {_a}", fases=list(_FASES_AC)))

# 2008 em diante: Apertura e Clausura são edições
_AC = {2008: (15, 271, 718), 2009: (12, 460, 915), 2010: (26, 469, 899), 2011: (22, 424, 835), 2012: (22, 425, 834),
       2013: (22, 433, 861), 2014: (22, 450, 875), 2015: (20, 452, 910), 2016: (22, 463, 905), 2017: (22, 447, 871),
       2018: (24, 466, 904), 2019: (24, 481, 919), 2020: (20, 465, 745), 2021: (22, 343, 670), 2022: (22, 459, 891),
       2023: (22, 466, 909), 2024: (22, 449, 861), 2025: (22, 433, 868)}
for _a, (_ap, _cl, _fim) in _AC.items():
    _pg = f"para{_a % 100:02d}" if _a < 2010 else f"para{_a}"
    EDICOES.append(_e(f"{_a} Apertura", _a, _a, [(_pg, _ap, _cl)], f"Campeonato Paraguayo de Primera División {_a} – Apertura"))
    EDICOES.append(_e(f"{_a} Clausura", _a, _a, [(_pg, _cl, _fim)], f"Campeonato Paraguayo de Primera División {_a} – Clausura"))
