"""Edições da 1ª divisão tunisiana (tun-1): o campeonato da Tunísia de 1907 a 2025/26.

Lista de campeões: RSSSF (tunchamp.html), conferida com a Wikipédia em inglês ("List of Tunisian football champions", que
conta desde 1907). A era colonial entra (pesquisa de 24/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md): a
contagem oficial usada na Tunísia inclui esses títulos (o "34º título" do Espérance em 2024/25 só fecha com o de 1941/42;
o "14º" do Club Africain em 2025/26, com os de 1946/47 e 1947/48). Até 1920/21 era o campeonato da USFSA; de 1921/22 a
1954/55, da Liga da Tunísia, quase sempre com campeões regionais e uma final.
Ficam de fora as temporadas sem competição (1909/10, 1914/15 a 1918/19, 1939/40, 1940/41, 1942/43, 1943/44), as copas e a
2ª divisão. 1951/52 foi abandonado (agitação política de janeiro de 1952) e entra sem campeão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página tunAA (ou tunAAAA nos anos 1900-1910 e desde 2009): a do
  ano em que a temporada termina (tun97 = 1996/97; tun09 = 1908/09; tun2009 = 2008/09).
- hist: a tabela final vem da lista de tabelas finais da RSSSF (tunhist.html, 1955/56 a 2002/03), seção da temporada.
- matriz: tabela de confrontos da página da temporada (lida por ler_rsssf.matriz()).
- ogol: o calendário do ogol é a base nos anos em que a RSSSF só tem a tabela.
Pontos: 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0
desde 1995/96, como as tabelas da RSSSF contam.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "tun-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Coupe\b|Cups?\b|Cup Tournaments|Tunisi(a|an) Cup|Promotion|Barrage|Second (Level|Division)|Ligue Professionnelle 2|"
              r"Ligue (II|III|2|3)\b|Nationale B|Division 2\b|Third level|S[ée]rie 2|Topscorers?\b|Top ?scorers|"
              r"list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1907", "1948/49"
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
    hist: str = ""                                                # "tunhist": tabela da lista de tabelas finais
    ogol: int | None = None
    espn: tuple[str, str] | None = None                           # (não usado: a ESPN não tem a liga tunisiana)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)
    matriz: str | None = None
    parcial: tuple[str, int, int] | None = None
    cancelada: str = ""
    incompleta: str = ""

    @property
    def pontos(self) -> tuple[int, int, int]:
        a = self.ano_inicio
        if a >= 1995:
            return (3, 1, 0)
        if a >= 1992:
            return (2, 1, 0)
        if a >= 1986:
            return (4, 2, 1)
        return (3, 2, 1)

    @property
    def pontos_vitoria(self) -> int:
        return self.pontos[0]

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.ogol is None and self.matriz is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _temp(a: int) -> str:
    return f"{a}/{(a + 1) % 100:02d}"


def pagina(ano_fim: int) -> str:
    return f"tun{ano_fim}" if ano_fim < 1920 or ano_fim >= 2009 else f"tun{ano_fim % 100:02d}"


COLONIAL = "Championnat de Tunisie (Ligue de Tunisie de Football)"
USFSA = "Championnat de Tunisie (USFSA)"
NACIONAL = "Championnat National de Tunisie"
SEM_PAGINA = "sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)"
_SEM_COMPETICAO = {1909, 1914, 1915, 1916, 1917, 1918, 1939, 1940, 1942, 1943}

EDICOES: list[Edicao] = [_e("1907", 1907, 1907, [], USFSA)]
for _a in range(1908, 2026):
    if _a in _SEM_COMPETICAO:
        continue
    EDICOES.append(_e(_temp(_a), _a, _a + 1, [], USFSA if _a < 1921 else COLONIAL if _a < 1955 else NACIONAL))
_POR = {e.temporada: e for e in EDICOES}

# ------------------------------------------------------------------------------------------------ era colonial
_PAGINAS_COLONIAIS = {"1907": "tun1907", "1908/09": "tun09", "1910/11": "tun1911", "1913/14": "tun1914",
                      "1919/20": "tun1920", "1927/28": "tun28", "1931/32": "tun32", "1933/34": "tun34",
                      "1938/39": "tun39", "1949/50": "tun50", "1951/52": "tun52", "1952/53": "tun53"}
for _e2 in EDICOES:
    if _e2.ano_inicio >= 1955:
        break
    pg = _PAGINAS_COLONIAIS.get(_e2.temporada)
    if pg:
        _e2.trechos = [(pg, 12, None)]
        _e2.incompleta = "jogos incompletos (só a final do campeonato)"
    else:
        _e2.obs = SEM_PAGINA
_POR["1919/20"].trechos = []
_POR["1919/20"].obs = "a RSSSF traz só o campeão da Série 1 (e jogos da Série 2, a 2ª divisão)"
_POR["1919/20"].incompleta = ""
_POR["1927/28"].trechos = []
_POR["1927/28"].obs = "a RSSSF traz só o campeão (a tabela da página é da 3ª divisão)"
_POR["1927/28"].incompleta = ""
_POR["1949/50"].incompleta = "jogos incompletos (só os resultados conhecidos)"
_POR["1951/52"].trechos = []
_POR["1951/52"].incompleta = ""
_POR["1951/52"].tabelas = [("tun52", 12, 30)]
_POR["1951/52"].cancelada = ("temporada não terminada: abandonada em janeiro de 1952 pela agitação política; nenhum título "
                             "foi dado e todos os clubes ficaram na 1ª divisão (a tabela é a do abandono)")
_POR["1952/53"].incompleta = "jogos incompletos (cinco grupos regionais sem jogos; só o mata-mata final)"
_POR["1952/53"].obs = "campeonato boicotado pelos clubes nacionalistas e muçulmanos"
for _t in ("1907", "1908/09", "1910/11", "1913/14", "1931/32", "1933/34", "1938/39", "1952/53"):
    _POR[_t].fases = [(r"^(National |Championship |Série 2 )?Final", "Final"), (r"^(Semifinals?|1/2)", "Semifinal"),
                      (r"^Playoff", "Quartas de final"), (r"^First Leg|^Second Leg", "Final")]

# ------------------------------------------------------------------------------------------------ desde 1955/56
# tabela de confrontos na página da temporada
_MATRIZ = {1968, 1970, 1977, 1980, 1982, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995}
for _a in range(1955, 2026):
    _x = _POR[_temp(_a)]
    if _a < 2003:
        _x.hist = "tunhist"
    if _a in _MATRIZ:
        _x.matriz = pagina(_a + 1)
    elif _a < 1996:
        _x.obs = "a RSSSF traz só a tabela final (lista de tabelas finais)"
    elif _a == 2025:
        _x.ogol = _a
        _x.tabelas = [(pagina(_a + 1), 0, None)]
        _x.obs = "a RSSSF só traz as tabelas: os jogos vêm do calendário do ogol"
    else:
        _x.trechos = [(pagina(_a + 1), 0, None)]

# nomes que dependem do ano
_POR["1949/50"].nomes = {"ES": "Espérance de Tunis"}   # "Known Results": o Étoile é "ES Sahel"; "ES" é o Espérance
# 2021/22: o "16th Place Playoff" (semifinal e final com data) decide quem cai, não o título ("Final Table" não entra)
_POR["2021/22"].fases = [(r"^(Semi)?[Ff]inal \[", "Desempate do rebaixamento")]
# 2023/24: o "Relegation Playoff" é um jogo só (AS Solimane x AS Marsa, 15º e 16º do grupo do rebaixamento)
_POR["2023/24"].fases = [(r"^Relegation Play-?off", "Desempate do rebaixamento")]
