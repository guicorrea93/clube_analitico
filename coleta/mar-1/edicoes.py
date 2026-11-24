"""Edições da 1ª divisão marroquina (mar-1): o campeonato do Marrocos de 1915/16 a 2025/26.

Lista de campeões: RSSSF (marochamp.html, 39 títulos de 1915/16 a 1954/55 e 70 desde 1956/57), conferida com a Wikipédia em
inglês. A era colonial entra (pesquisa de 24/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md): a federação
marroquina conta esses títulos (o site da FRMF, em 2015: "18º título do WAC desde 1948", 5 antes de 1956), e RSSSF,
Wikipédia e os clubes também. Era o campeonato do Marrocos inteiro: da USFSA até 1921/22 e da Liga do Marrocos (LMFA) de
1922/23 a 1954/55, às vezes em liga única, às vezes em ligas regionais com mata-mata nacional.
Ficam de fora: a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos, que ninguém conta no palmarès), 1955/56
(sem competição), as copas (Coupe du Sultan, Coupe Colonial, Coupe du Trône...) e a 2ª divisão. 1942/43 foi abandonado em
novembro de 1942 (desembarque aliado) e entra sem campeão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro; linha final None: até o primeiro
  título de outra competição (FIM_PADRAO). Página maroAA (ou maroAAAA desde 2010 e nos anos 1910): a do ano em que a
  temporada termina (maro96 = 1995/96); maro3944 traz de 1938/39 a 1944/45.
- matriz: tabela de confrontos da página (1956/57 a 1967/68, 1980/81, 1989/90, 1990/91), lida por ler_rsssf.matriz().
- ogol: o calendário do ogol é a base nos anos em que a RSSSF só tem a tabela.
- tabelas: trechos lidos só pelas tabelas.
- parcial: trecho de uma classificação incompleta (só posição, ou posição e pontos), lida por ler_rsssf.parcial().
Pontos: 3-2-1 (vitória, empate, derrota) até 1994/95, como as tabelas da RSSSF contam; 3-1-0 desde 1995/96. Antes de
1933/34 as páginas não dizem.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "mar-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Coupe\b|Cup\b|Throne|Promotion|Barrage|Pr[ée]-Honneur|Second (Level|Division)|GNF ?(II|2)\b|Botola ?2|"
              r"Ligue Nationale Amateur|Championnat Fez|Morocco Cup|[XVI]+[a-z]* edition of|Division 2\b|Topscorers?\b|Top ?scorers|list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1948/49"
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
    espn: tuple[str, str] | None = None                           # (não usado: a ESPN não tem a liga marroquina)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)
    matriz: str | None = None                                     # página com a tabela de confrontos
    parcial: tuple[str, int, int] | None = None                   # (página, linha inicial, linha final)
    cancelada: str = ""
    incompleta: str = ""

    @property
    def pontos(self) -> tuple[int, int, int]:
        """(vitória, empate, derrota): 3-2-1 até 1994/95; 3-1-0 desde 1995/96."""
        return (3, 1, 0) if self.ano_inicio >= 1995 else (3, 2, 1)

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
    return f"maro{ano_fim}" if ano_fim < 1920 or ano_fim >= 2010 else f"maro{ano_fim % 100:02d}"


COLONIAL = "Championnat du Maroc (Ligue du Maroc de Football Association)"
NACIONAL = "Championnat National de 1ère Division"
SEM_PAGINA = "sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)"

EDICOES: list[Edicao] = []
for _a in range(1915, 2026):
    if _a == 1955:
        continue
    _t = _temp(_a)
    EDICOES.append(_e(_t, _a, _a + 1, [], COLONIAL if _a < 1956 else NACIONAL))
_POR = {e.temporada: e for e in EDICOES}

# ------------------------------------------------------------------------------------------------ era colonial
_POR["1915/16"].nome_oficial = _POR["1916/17"].nome_oficial = "Championnat officiel de l'USFSA"
for _t in ("1917/18", "1918/19", "1919/20", "1920/21", "1921/22"):
    _POR[_t].nome_oficial = "Championnat officiel de l'USFSA"
_POR["1915/16"].parcial = ("maro1916", 18, 28)
_POR["1915/16"].obs = "a RSSSF traz só a ordem final (sem jogos nem pontos)"
_POR["1916/17"].trechos = [("maro1917", 14, 46)]
_POR["1916/17"].incompleta = "jogos incompletos (só os resultados conhecidos e a final)"
for _t in ("1917/18", "1918/19", "1919/20", "1920/21", "1921/22", "1923/24", "1925/26", "1926/27", "1927/28"):
    _POR[_t].obs = SEM_PAGINA
_POR["1922/23"].trechos = [("maro23", 13, None)]
_POR["1922/23"].incompleta = "jogos incompletos (ligas regionais sem jogos; só as semifinais e a final)"
_POR["1924/25"].trechos = [("maro25", 13, None)]
_POR["1924/25"].incompleta = "jogos incompletos (ligas regionais sem jogos; só a final)"
_POR["1928/29"].trechos = [("maro29", 13, None)]
_POR["1928/29"].incompleta = "jogos incompletos (só a final)"
_POR["1929/30"].trechos = [("maro30", 13, None)]
_POR["1929/30"].incompleta = "jogos incompletos (ligas regionais com poucos jogos; o mata-mata final completo)"
_POR["1930/31"].trechos = [("maro31", 13, None)]
_POR["1930/31"].incompleta = "jogos incompletos (só o mata-mata final)"
_POR["1931/32"].trechos = [("maro32", 13, None)]
_POR["1931/32"].incompleta = "jogos incompletos (dois grupos com os resultados conhecidos e a final)"
_POR["1932/33"].trechos = [("maro33", 13, None)]
_POR["1932/33"].parcial = ("maro33", 63, 73)
_POR["1932/33"].incompleta = "jogos incompletos (resultados conhecidos; classificação em 20/02 com jogos e pontos)"
for _a in range(1933, 1938):
    _POR[_temp(_a)].trechos = [(pagina(_a + 1), 13, None)]
# maro3944: de 1938/39 a 1944/45 numa página só
_POR["1938/39"].trechos = [("maro3944", 13, 187)]
_POR["1939/40"].trechos = [("maro3944", 195, 253)]
_POR["1940/41"].trechos = [("maro3944", 270, 323)]
_POR["1941/42"].trechos = [("maro3944", 373, 526)]
_POR["1943/44"].trechos = [("maro3944", 575, 666)]
_POR["1944/45"].trechos = [("maro3944", 687, 819)]
for _t in ("1939/40", "1940/41", "1943/44", "1944/45"):
    _POR[_t].incompleta = "jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)"
_POR["1942/43"].cancelada = ("temporada não terminada: abandonada em novembro de 1942, com o desembarque aliado no Marrocos; "
                             "no lugar dela houve a Coupe de la Guerre (a US Marocaine ganhou), que não conta como título")
_POR["1945/46"].trechos = [("maro46", 12, None)]
_POR["1945/46"].incompleta = "jogos incompletos (ligas regionais quase sem jogos; o mata-mata nacional completo)"
for _a in (1946, 1947):
    _POR[_temp(_a)].trechos = [(pagina(_a + 1), 12, None)]
_POR["1948/49"].trechos = [("maro49", 12, 132)]
_POR["1948/49"].parcial = ("maro49", 133, 147)
_POR["1948/49"].incompleta = "jogos incompletos (as rodadas que a página traz e outros jogos do WAC; classificação só com pontos)"
for _a, _ini, _fim in ((1949, 14, 28), (1950, 16, 30), (1951, 14, 21), (1952, 16, 30), (1953, 14, 17)):
    _POR[_temp(_a)].parcial = (pagina(_a + 1), _ini, _fim)
    _POR[_temp(_a)].obs = "a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)"
_POR["1954/55"].tabelas = [("maro55", 14, 30)]
_POR["1954/55"].obs = "a RSSSF traz a tabela publicada na época, que ela mesma diz estar \"cheia de absurdos\""
for _a in (1922, 1924, 1928, 1929, 1930, 1931, 1939, 1940, 1943, 1944, 1945):
    _POR[_temp(_a)].fases = [(r"^Ligue (du |de |Oriental)", ""), (r"^Playoffs?$", "Mata-mata final"),
                             (r"^Quarter-?finals?", "Quartas de final"), (r"^Semi-?finals?", "Semifinal"),
                             (r"^Final( Replay)?( \[|$)", "Final"), (r"^(Replay|Second Replay)", "Final")]
_POR["1935/36"].fases = [(r"^Final \[", "Final"), (r"^6th Place Playoff", "Desempate do 6º lugar")]
for _t in ("1936/37", "1937/38", "1946/47"):
    _POR[_t].fases = [(r"^Championship Playoff", "Desempate do título"), (r"^9th Place Playoff", "Desempate do 9º lugar")]

# ------------------------------------------------------------------------------------------------ desde 1956/57
# anos com tabela de confrontos na página da RSSSF (o leitor acha o cabeçalho sozinho)
_MATRIZ = set(range(1956, 1968)) | {1980, 1989, 1990}
_SEM_PAGINA_MOD = {1970, 1973, 1981}
# o ogol do Marrocos só tem jogos de 2004/05 em diante; antes, os anos sem tabela de confrontos ficam só com a tabela
for _a in range(1956, 2026):
    _x = _POR[_temp(_a)]
    if _a in _MATRIZ:
        _x.matriz = pagina(_a + 1)
        _x.tabelas = [(pagina(_a + 1), 0, None)]
    elif _a in _SEM_PAGINA_MOD:
        _x.obs = "a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista"
    elif _a < 1995:
        _x.tabelas = [(pagina(_a + 1), 0, None)]
        _x.obs = "a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano"
    elif _a in (2010, 2011, 2025):
        _x.ogol = _a
        _x.tabelas = [(pagina(_a + 1), 0, None)]
        _x.obs = "a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol"
    else:
        _x.trechos = [(pagina(_a + 1), 0, None)]

# nomes que dependem do ano
_POR["1995/96"].nomes = {"WAS Casablanca": "Wydad Casablanca"}   # erro de digitação da página (WA Casablanca)
_POR["1999/00"].nomes = {"Ittihad": "TAS Casablanca"}            # "TS Ittihad Ryadi" na tabela

# 1946/47: a lista de campeões da RSSSF dá o título à US Marocaine, 3ª colocada; a página da temporada mostra a USA Casablanca
# vencendo o desempate do título (3-0 sobre a ASPTT Casablanca), e a Wikipédia em inglês também dá a USA Casablanca
_POR["1946/47"].campeao_rsssf = "USA Casablanca"
_POR["1946/47"].obs = ("campeão: USA Casablanca, que venceu o desempate do título (página da temporada e Wikipédia); a lista de "
                       "campeões da RSSSF põe a US Marocaine, 3ª colocada (erro da lista)")
# 1999/00 e 2000/01: "KAC" sozinho é o Kawkab de Marrakech (o KAC Kénitra não estava na 1ª divisão)
_POR["1999/00"].nomes["KAC"] = "Kawkab Marrakech"
_POR["2000/01"].nomes = {"KAC": "Kawkab Marrakech"}
_POR["1996/97"].nomes = {"Fes": "Wydad Fès"}   # o MAS Fès não estava na 1ª divisão; "Fes" é o Wydad Fès (WAF)
# 1959/60: três clubes empatados em pontos; o triangular virou um jogo só (o Raja se recusou a jogar)
_POR["1959/60"].trechos = [("maro60", 37, 47)]
_POR["1959/60"].fases = [(r"^Championship Playoff", "Desempate do título")]
# 1993/94: a tabela só traz os pontos da maioria dos clubes
_POR["1993/94"].tabelas = []
_POR["1993/94"].parcial = ("maro94", 13, 31)
_POR["1993/94"].obs = "a RSSSF traz só a classificação, com os pontos (jogos, vitórias e gols só de alguns clubes)"
