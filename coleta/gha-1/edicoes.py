"""Edições da 1ª divisão ganesa (gha-1): a liga nacional, de 1958 a 2025/26 (hoje Ghana Premier League).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): como a lista
de campeões da RSSSF (ghachamp.html), sem o campeonato não oficial de 1956 (a RSSSF não conta) e sem a "competição
especial" do Comitê de Normalização de 2019 (não foi liga; a imprensa não a conta: o título de 2021/22 foi o "25º" do
Asante Kotoko). 2018 e 2019/20 foram abandonados e entram sem campeão.

Temporadas como na lista da RSSSF (o rótulo muda: ano civil, duas temporadas, de novo ano civil). "2004/05" é a página
gha04 (temporada de 2004, decidida num jogo em abril de 2005) e "2005" é a gha05 ("Ghana 2005/06").

Fontes dos jogos por edição:
- hist: a tabela final vem da lista de tabelas finais da RSSSF (ghahist.html, 1958 a 2000), seção da temporada.
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-ganesa), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "gha-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: copa (o nome da copa não pode estar entre
# parênteses ou colchetes) ou outra divisão
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(Cup|Cups|Top Four|Top 4|Super ?Cup|Charity|Shield)\b|"
              r"Division (One|Two|1|2)\b|Second Level|Third Level|Promotion|Topscorers?\b|Top ?scorers|"
              r"list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1958", "1959/60"
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
    hist: str = ""                                                # "ghahist": tabela da lista de tabelas finais
    ogol: int | None = None
    espn: tuple[str, str] | None = None                           # (não usado)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)
    matriz: str | None = None
    parcial: tuple[str, int, int] | None = None
    cancelada: str = ""
    incompleta: str = ""
    sistema: tuple[int, int, int] = (3, 1, 0)
    ogol_id: int | None = None                                    # edição do ogol (conferência)

    @property
    def pontos(self) -> tuple[int, int, int]:
        return self.sistema

    @property
    def pontos_vitoria(self) -> int:
        return self.pontos[0]

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.ogol is None and self.matriz is None


# temporada -> página da RSSSF com os jogos ("" = só a lista de tabelas finais)
_PAGINAS: dict[str, str] = {}
for _t in ["1958", "1959/60", "1960/61", "1961/62", "1962/63", "1963/64", "1964/65", "1966"] + \
          [str(a) for a in range(1967, 1988)] + [f"{a}/{(a + 1) % 100:02d}" for a in range(1988, 1997)]:
    _PAGINAS[_t] = ""
_PAGINAS.update({"1997/98": "gha98", "1999": "gha99", "2000": "gha00", "2001": "gha01", "2002": "gha02", "2003": "gha03",
                 "2004/05": "gha04", "2005": "gha05", "2006/07": "gha07", "2007/08": "gha08", "2008/09": "gha09"})
_PAGINAS.update({f"{a}/{(a + 1) % 100:02d}": f"gha{a + 1}" for a in range(2009, 2014)})
_PAGINAS.update({"2015": "gha2015", "2016": "gha2016", "2017": "gha2017", "2018": "gha2018"})
_PAGINAS.update({f"{a}/{(a + 1) % 100:02d}": f"gha{a + 1}" for a in range(2019, 2026)})


def _edicao(t: str, pagina: str) -> Edicao:
    a0 = int(t[:4])
    a1 = a0 + 1 if "/" in t else a0
    return Edicao(t, a0, a1, [(pagina, 0, None)] if pagina else [], "Ghana Premier League")


EDICOES: list[Edicao] = [_edicao(t, pg) for t, pg in _PAGINAS.items()]
_POR = {e.temporada: e for e in EDICOES}
for _x in EDICOES:
    if _x.ano_inicio <= 2000:
        _x.hist = "ghahist"   # tabela final da lista (até 2000)
    if not _x.trechos:
        _x.obs = "a RSSSF só traz a tabela final (lista de tabelas finais)"
# a lista de tabelas finais só tem as tabelas até 1987; de 1989/90 a 1996/97 a tabela vem da página do ano; 1988/89 não
# tem tabela ("Final table missing"): só o campeão
for _a in range(1988, 1997):
    _x = _POR[f"{_a}/{(_a + 1) % 100:02d}"]
    _x.hist = ""
    if _a >= 1989:
        _x.tabelas = [(f"gha{(_a + 1) % 100:02d}", 0, None)]
        _x.obs = "a RSSSF só traz a tabela final"
    else:
        _x.obs = "a RSSSF só traz o campeão (\"Final table missing\")"
for _a in (1997, 1999, 2000):
    _POR[f"{_a}/98" if _a == 1997 else str(_a)].hist = ""   # a seção da lista só remete à página do ano
# 2003: "Final(?) Table:" não é fase
_POR["2003"].fases = [(r"^Final\(\?\) Table", "")]
# 1989/90: a tabela só traz posição, jogos e pontos (e cinco clubes sem posição nem números)
_POR["1989/90"].tabelas = []
_POR["1989/90"].parcial = ("gha90", 16, 32)
_POR["1989/90"].obs = "a RSSSF só traz a classificação incompleta (posição, jogos e pontos)"

# edição do ogol de cada temporada (mesmo rótulo; o ogol só tem jogos de 2008/09 a 2010/11 e de 2015 em diante)
_arq = PASTA_DADOS / "ogol" / "edicoes.json"
if _arq.exists():
    import json
    _ids = {ed["nome"]: ed["id"] for ed in json.loads(_arq.read_text(encoding="utf-8"))}
    for _x in EDICOES:
        if _x.ano_inicio >= 2008:
            _x.ogol_id = _ids.get(_x.temporada)
# 2010/11: a RSSSF só tem parte dos jogos; o ogol tem a temporada inteira
_x = _POR["2010/11"]
_x.ogol = _x.ogol_id
_x.tabelas, _x.trechos = _x.trechos, []
_x.obs = "os jogos vêm do calendário do ogol (a RSSSF só traz parte deles)"
# 1997/98 e 2006/07: a RSSSF só traz parte dos jogos e o ogol não tem esses anos
for _t in ("1997/98", "2006/07"):
    _POR[_t].incompleta = "jogos incompletos (só os resultados que a página traz)"
# 2011/12: a página só tem a tabela (e o ogol não tem os jogos)
_x = _POR["2011/12"]
_x.tabelas, _x.trechos = _x.trechos, []
_x.obs = "a RSSSF só traz a tabela final"
# temporadas abandonadas: sem campeão
_POR["2018"].cancelada = ("temporada abandonada pelo escândalo de corrupção na federação ganesa (\"competition abandoned "
                          "following corruption scandal within GFA\"); a tabela é a do abandono")
_POR["2019/20"].cancelada = "temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono"
# pontos: 2-1-0 até 1993/94 (fora 1989/90, que as tabelas contam com 3 por vitória: o Asante Kotoko fez 78 em 30 jogos);
# 3-1-0 desde 1994/95
for _x in EDICOES:
    if _x.ano_inicio <= 1993 and _x.temporada != "1989/90":
        _x.sistema = (2, 1, 0)
# 2017: a liga termina antes da 2ª divisão regional ("Central Regional Division 2", linha 442)
_POR["2017"].trechos = [("gha2017", 0, 442)]
# 2004/05: dois grupos, jogo do título ("Championship Playoff", abril de 2005), 3º lugar e desempate do rebaixamento
_POR["2004/05"].fases = [(r"^Championship Play-?off", "Final"), (r"^Relegation Play-?off", "Desempate do rebaixamento")]
