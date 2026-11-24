"""Edições da 1ª divisão dos EUA (usa-1): uma por título, como na lista de campeões da "Division I" da RSSSF
(tablesu/usachamp.html). Escopo decidido em 24/11/2026 (o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"):

- ASL I (American Soccer League, 1921/22 a 1932/33): 14 títulos, com as meias-temporadas de 1929 (outono), 1930 (outono) e
  1932 (primavera), como na lista da RSSSF. Só as tabelas (usadave/asli.html): a RSSSF não tem os jogos.
- 1967: duas ligas rivais, cada uma uma edição: United Soccer Association (a da FIFA; os times eram clubes europeus e
  sul-americanos jogando com nome de cidade americana) e NPSL (a "pirata"). Tabelas e campeão (usadave/nasl.html).
- NASL 1968-1984: tabelas e campeão (usadave/nasl.html); os playoffs só em texto ("X defeated Y 2-1"), na observação. As
  temporadas indoor ficam fora.
- 1985-1995: sem 1ª divisão (sem edição).
- MLS 1996-2025: jogos da RSSSF (tablesu/usaAA.html, usaAAAA.html de 2010 em diante) e da ESPN (2004, 2011, 2012 e 2025, que a
  RSSSF só tem nas tabelas); 1997 e 1998 só com as tabelas (nenhuma das fontes tem os jogos). O campeão é o da MLS Cup.
  A temporada 2026 entra depois da final (18/12/2026).
Ficam fora a ASL II (1933-1983), a International Soccer League (1960-1965, torneio de verão com clubes estrangeiros), as
ligas de 2º nível de 1985-1995 (APSL, A-League), a US Open Cup e a Leagues Cup.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "usa-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da MLS numa página de temporada
FIM_PADRAO = (r"^(.*Open Cup|USL\b|A-LEAGUE|A-League|USISL|APSL|Leagues Cup|NASL\b|North American Soccer League|"
              r"MLS Next Pro|MLS is Back|Second Division|.*\((2nd|3rd|4th) Division\)|.*\(Division [234]\)|Women|WPS|NWSL|WUSA|"
              r"About this document|list of champions)")


@dataclass
class Edicao:
    temporada: str
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
    ogol: int | None = None                                       # (não usado)
    espn: tuple[str, str] | None = None                           # datas dos jogos que vêm da ESPN
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""
    sem_campeao: str = ""
    liga: str = "MLS"                                              # ASL, USA, NPSL, NASL, MLS
    pontos_fora: str = ""                                          # pontuação fora do padrão (a tabela publicada vale)

    @property
    def pontos_vitoria(self) -> int:
        """2 por vitória na ASL e na United Soccer Association de 1967; 6 na NPSL e na NASL (com bônus por gol); 3 na MLS."""
        return {"ASL": 2, "USA": 2, "NPSL": 6, "NASL": 6}.get(self.liga, 3)

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


@lru_cache(maxsize=None)
def _texto(pagina: str) -> tuple[str, ...]:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
    import rsssf_concacaf
    return tuple(rsssf_concacaf.texto(PASTA_DADOS / "rsssf" / f"{pagina}.html"))


def _linha(pagina: str, rx: str, depois: int = 0) -> int:
    ls = _texto(pagina)
    for i in range(depois, len(ls)):
        if re.fullmatch(rx, ls[i].strip(), re.I):
            return i
    raise ValueError(f"{pagina}: título {rx!r} não achado")


EDICOES: list[Edicao] = []

# ---------------------------------------------------------------------------------------------------- ASL I (1921-1933)

_ASL = [("1921/22", 1921, 1922, r"1921/22"), ("1922/23", 1922, 1923, r"1922/23"), ("1923/24", 1923, 1924, r"1923/24"),
        ("1924/25", 1924, 1925, r"1924/25"), ("1925/26", 1925, 1926, r"1925/26"), ("1926/27", 1926, 1927, r"1926/27"),
        ("1927/28", 1927, 1928, r"1927/28"), ("1928/29", 1928, 1929, r"1928/29"), ("1929", 1929, 1929, r"1929 \(Fall\)"),
        ("1929/30", 1929, 1930, r"1929/30"), ("1930", 1930, 1930, r"1930 \(Fall\)"), ("1931", 1931, 1931, r"1931"),
        ("1932", 1932, 1932, r"1932 \(spring\)"), ("1932/33", 1932, 1933, r"1932-33")]
_ASL_OBS = {
    "1927/28": "dois turnos; o campeão saiu dos playoffs entre os primeiros (Boston Wonder Workers 4-2 New Bedford Whalers)",
    "1928/29": "dois turnos; a classificação é por aproveitamento",
    "1929": "meia-temporada de outono, suspensa em 9/10/1929 com o fim da \"soccer war\" (a ASL se juntou à Eastern Soccer League)",
    "1929/30": "disputada como Atlantic Coast League (a ASL e a Eastern Soccer League juntas)",
    "1930": "meia-temporada de outono",
    "1931": "primavera e outono de 1931; a lista de campeões da RSSSF a chama de 1930-31; final: New York Giants x New Bedford "
            "Whalers (8-3 e 6-0)",
    "1932": "meia-temporada de primavera, talvez incompleta (\"may be an incomplete set of standings\", RSSSF); sem gols na tabela",
    "1932/33": "só o 1º turno (outono de 1932) tem tabela; a liga foi refeita no verão de 1933 como a ASL II",
}
_cab = [_linha("asli", rx) for _, _, _, rx in _ASL] + [_linha("asli", r"About this document")]
for (_t, _a0, _a1, _), _i, _f in zip(_ASL, _cab, _cab[1:]):
    EDICOES.append(_e(_t, _a0, _a1, [], f"American Soccer League {_t}" if _t != "1929/30" else "Atlantic Coast League 1929/30",
                      tabelas=[("asli", _i, _f)], liga="ASL",
                      obs="; ".join(x for x in ("só a tabela: a RSSSF não tem os jogos da ASL I", _ASL_OBS.get(_t, "")) if x)))

# ---------------------------------------------------------------------------------------------------- 1967 e NASL

_ANOS = list(range(1967, 1985))
_cab = [_linha("nasl", str(a)) for a in _ANOS] + [_linha("nasl", r"About this document")]
for _a, _i, _f in zip(_ANOS, _cab, _cab[1:]):
    _ls = _texto("nasl")
    # a temporada indoor vem dentro da seção do ano: fica fora
    _fim = next((k for k in range(_i + 1, _f) if re.fullmatch(r"\s*(Indoor Season|\d{4}-\d{2} \(indoor\))\s*", _ls[k], re.I)), _f)
    if _a == 1967:
        _npsl = _linha("nasl", r"National Professional Soccer League \(NPSL\)", _i)
        _pts = "2 pontos por vitória e 1 por empate"
        EDICOES.append(_e("1967 USA", 1967, 1967, [], "United Soccer Association 1967", tabelas=[("nasl", _i, _npsl)], liga="USA",
                          obs="liga da FIFA; os times eram clubes europeus e sul-americanos com nome de cidade americana; só a "
                              "tabela e a final (Los Angeles Wolves 6-5 Washington Whips, prorrogação)"))
        EDICOES.append(_e("1967 NPSL", 1967, 1967, [], "National Professional Soccer League 1967", tabelas=[("nasl", _npsl, _fim)],
                          liga="NPSL", pontos_fora="6 por vitória, 3 por empate e 1 por gol (até 3 por jogo)",
                          obs="liga sem reconhecimento da FIFA (\"pirata\"); só a tabela e a final (Oakland Clippers x "
                              "Baltimore Bays, 0-1 e 4-1)"))
        continue
    _pts = ("6 por vitória, 3 por empate e 1 por gol (até 3 por jogo)" if _a <= 1974 else
            "6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo)")
    EDICOES.append(_e(str(_a), _a, _a, [], f"North American Soccer League {_a}", tabelas=[("nasl", _i, _fim)], liga="NASL",
                      pontos_fora=_pts, obs="só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)"))

# ---------------------------------------------------------------------------------------------------- MLS

# a RSSSF só tem as tabelas: os jogos vêm da ESPN (e os playoffs da página, quando ela tem)
_ESPN = {2004: ("2004-01-01", "2004-12-31"), 2011: ("2011-01-01", "2011-10-24"), 2012: ("2012-01-01", "2012-10-29"),
         2025: ("2025-01-01", "2025-10-19")}
_SO_TABELAS = {1997, 1998}
# 2004: os playoffs também vêm da ESPN (a fase pela data)
_ESPN_FASES = {2004: [("2004-10-20", "Semifinal de conferência"), ("2004-11-05", "Final de conferência"), ("2004-11-14", "Final")]}
_INICIO = r"(Regular Season|MAJOR LEAGUE SOCCER.*|Major League Soccer)"


def _pagina(a: int) -> str:
    return f"usa{a % 100:02d}" if a < 2010 else f"usa{a}"


for _a in range(1996, 2026):
    _pg = _pagina(_a)
    _ls = _texto(_pg)
    try:
        _i = _linha(_pg, r"Regular Season")
    except ValueError:
        _i = 0
    _f = next((k for k in range(_i + 1, len(_ls)) if re.match(FIM_PADRAO, _ls[k].strip()) and k > _i + 5), len(_ls))
    _shoot = "3 por vitória e 1 por vitória nos pênaltis (shootout, sem empates)" if _a <= 1999 else ""
    if _a in _SO_TABELAS:
        EDICOES.append(_e(str(_a), _a, _a, [], f"Major League Soccer {_a}", tabelas=[(_pg, _i, _f)], pontos_fora=_shoot,
                          obs="só a tabela: a RSSSF não tem os jogos deste ano e a ESPN começa em 2002"))
        continue
    if _a in _ESPN:
        _tr = [(_pg, _i, _f)] if _a != 2004 else []
        EDICOES.append(_e(str(_a), _a, _a, _tr, f"Major League Soccer {_a}", espn=_ESPN[_a], espn_fases=_ESPN_FASES.get(_a, []),
                          tabelas=[(_pg, _i, _f)] if _a == 2004 else [], pontos_fora=_shoot,
                          obs="fase regular da ESPN (a página da RSSSF só tem as tabelas)" if _a != 2004 else
                              "jogos da ESPN (a página da RSSSF só tem as tabelas)"))
        continue
    EDICOES.append(_e(str(_a), _a, _a, [(_pg, _i, _f)], f"Major League Soccer {_a}", pontos_fora=_shoot))
