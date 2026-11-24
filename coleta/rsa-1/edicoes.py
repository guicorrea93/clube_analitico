"""Edições da 1ª divisão sul-africana (rsa-1): NPSL (1971 a 1984), NSL (1985 a 1995) e PSL (1996/97 a 2025/26).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): a linha do
futebol profissional que a RSSSF ("NPSL/NSL/PSL championships, 55, since 1971") e a imprensa contam (Mamelodi Sundowns 18,
Kaizer Chiefs 12, Orlando Pirates 10). Ficam de fora as ligas separadas por raça do apartheid (NFL dos brancos, 1959-1977;
SASL/FPL dos "coloured"), a NPSL que seguiu em paralelo depois de 1985, as NPSL amadoras de 1968 e 1969 e o torneio de
transição de 1996 ("Coca-Cola Challenge"), que ninguém conta como título.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página zafAA (ou zafAAAA desde 2009/10): a do ano (1971 a
  1996) ou do ano em que a temporada termina (zaf97 = 1996/97; zaf2010 = 2009/10). Linha inicial 0: logo depois do
  cabeçalho; linha final None: a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a RSSSF só tem a tabela final.
- ogol: o calendário do ogol (liga-sul-africana, desde 1996/97), quando a RSSSF não tem os jogos.
Pontos: 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995, como as tabelas da RSSSF contam.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "rsa-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: copa (o nome da copa não pode estar entre
# parênteses ou colchetes, como o "(African Champions Cup)" de uma linha da tabela) ou outra divisão
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(Cup|Cups|Super ?[Bb]owl|Top (Eight|8)|Knock-?out|Spectacular|Charity)\b|"
              r"FPL\b|NFL\b|Natal (Football|Premier) League|SASF\b|Transvaal Soccer|Challenge\b|National First Division|Vodacom League|Second (Level|Division)|2nd Division|"
              r"Promotion/Relegation|Topscorers?\b|Top ?scorers|Mamelodi squad|list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1971", "1996/97"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: int | None = None                                       # (não usado)
    hist: str = ""                                                # (não usado)
    ogol: int | None = None
    espn: tuple[str, str] | None = None                           # (não usado)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)
    matriz: str | None = None
    parcial: tuple[str, int, int] | None = None
    cancelada: str = ""
    incompleta: str = ""

    @property
    def pontos(self) -> tuple[int, int, int]:
        return (3, 1, 0) if self.ano_inicio >= 1995 else (2, 1, 0)

    @property
    def pontos_vitoria(self) -> int:
        return self.pontos[0]

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.ogol is None and self.matriz is None


def pagina(ano_fim: int) -> str:
    return f"zaf{ano_fim}" if ano_fim >= 2010 else f"zaf{ano_fim % 100:02d}"


def _nome(a: int) -> str:
    if a <= 1984:
        return "NPSL (National Professional Soccer League)"
    if a <= 1995:
        return "NSL (National Soccer League)"
    return "Premier Soccer League (Premiership)"


EDICOES: list[Edicao] = [Edicao(str(a), a, a, [(pagina(a), 0, None)], _nome(a)) for a in range(1971, 1996)]
EDICOES += [Edicao(f"{a}/{(a + 1) % 100:02d}", a, a + 1, [(pagina(a + 1), 0, None)], _nome(a)) for a in range(1996, 2026)]
_POR = {e.temporada: e for e in EDICOES}

# ------------------------------------------------------------------------------------------------ casos especiais
# 1971, 1974 e 1976: a NPSL vem depois da NFL (dos brancos) na página
_POR["1971"].trechos = [("zaf71", 130, None)]
_POR["1974"].trechos = [("zaf74", 160, None)]
_POR["1976"].trechos = [("zaf76", 87, None)]
# 1972, 1973, 1975 e 1977: a página só tem a NFL; da NPSL, só o campeão (lista de campeões)
for _t in ("1972", "1973", "1975", "1977"):
    _POR[_t].trechos = []
    _POR[_t].obs = "a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)"
# 1982: a NPSL termina antes da "Datsun Challenge 1982 (NPSL League Cup)" (linha 41)
_POR["1982"].trechos = [("zaf82", 0, 41)]

# fonte de cada período: até 1995 a RSSSF quase só tem a tabela final; 1987, 1992 e 1993 têm parte dos jogos; 1996/97
# (a página só tem parte da temporada) e 2025/26 (só a tabela) vêm do calendário do ogol
for _e3 in EDICOES:
    if _e3.ano_inicio <= 1995 and _e3.trechos and _e3.temporada not in ("1987", "1992", "1993"):
        _e3.tabelas, _e3.trechos = _e3.trechos, []
        _e3.obs = _e3.obs or "a RSSSF só traz a tabela final"
for _t in ("1987", "1992", "1993"):
    _POR[_t].incompleta = "jogos incompletos (só os resultados que a página traz)"
for _t in ("1996/97", "2025/26"):
    _x = _POR[_t]
    _x.ogol = _x.ano_inicio
    _x.tabelas, _x.trechos = _x.trechos, []
    _x.obs = "os jogos vêm do calendário do ogol (a RSSSF só traz " + ("parte deles" if _t == "1996/97" else "a tabela") + ")"
# 1996/97: o ogol só tem jogos de 2005/06 em diante; ficam os jogos que a página traz
_x = _POR["1996/97"]
_x.ogol, _x.trechos, _x.tabelas = None, [("zaf97", 0, None)], []
_x.incompleta = "jogos incompletos (só os resultados que a página traz)"
_x.obs = ""

# 1993: "Rangers" nos jogos é o Ratanang, que virou Chatsworth Rangers no meio da temporada (nota da página)
_POR["1993"].nomes = {"Rangers": "Chatsworth Rangers"}
# 2006/07: a liga termina antes do desempate de acesso com a 2ª divisão ("Mvela Golden League Platinum Playoffs", linha 681)
_POR["2006/07"].trechos = [("zaf07", 0, 681)]
