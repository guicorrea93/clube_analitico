"""Edições da 1ª divisão camaronesa (cmr-1): o campeonato nacional, de 1961 a 2026 (hoje Elite One).

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): como a lista
de campeões da RSSSF (kamchamp.html, "since independence"), com uma edição só para o primeiro campeonato (a lista dá
"1960" e "1961", os dois com o Oryx, mas conta um título só; a página é a mesma, kam61, e a Wikipédia dá 1961). Ficam de
fora o campeonato territorial da era colonial (1936/37 a 1955/56) e as ligas do Camarões anglófono até 1972.

Temporadas como na lista da RSSSF (o rótulo muda: ano civil e duas temporadas se alternam).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela (ou só o topo dela).
- ogol: o calendário do ogol (liga-dos-camaroes), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "cmr-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: copa (o nome da copa não pode estar entre
# parênteses ou colchetes) ou outra divisão
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(Cup|Coupe|Cups|Super ?Cup|Troph[ée]e|Charity)\b|"
              r"(MTN )?Elite Two|Division (2|Two|II)\b|Second Level|Third Level|Promotion|Topscorers?\b|Top ?scorers|"
              r"list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1961", "1969/70"
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
    hist: str = ""                                                # (não usado em Camarões)
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


# temporadas da lista da RSSSF (sem o "1960", que é o mesmo campeonato de 1961) e a página de cada uma ("" = sem página)
_LISTA = ["1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1969/70", "1970/71", "1971/72",
          "1972/73", "1973/74", "1974/75", "1975/76", "1976/77", "1977/78", "1978/79", "1979/80", "1981", "1981/82",
          "1982/83", "1983/84", "1984/85", "1985/86", "1986/87", "1987/88", "1988/89", "1989/90", "1991", "1992", "1993",
          "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007",
          "2007/08", "2008/09", "2009/10", "2010/11", "2011/12", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
          "2019/20", "2020/21", "2022", "2022/23", "2023/24", "2024/25", "2026"]
_PAG = {"1961": "kam61", "1968": "kam68", "1978/79": "kam79", "1979/80": "kam80", "1981": "kam81", "1981/82": "kam82",
        "1982/83": "kam83", "1983/84": "kam84", "1985/86": "kam86", "1986/87": "kam87", "1987/88": "kam88",
        "1988/89": "kam89", "1989/90": "kam90", "1991": "kam91", "1993": "kam93"}
_PAG.update({str(a): f"kam{a % 100:02d}" for a in range(1994, 2008)})
_PAG.update({"2007/08": "kam08", "2008/09": "kam09", "2009/10": "kam2010", "2010/11": "kam2011", "2011/12": "kam2012"})
_PAG.update({str(a): f"kam{a}" for a in range(2013, 2020)})
_PAG.update({"2019/20": "kam2020", "2020/21": "kam2021", "2022": "kam2022", "2022/23": "kam2023", "2023/24": "kam2024",
             "2024/25": "kam2025", "2026": "kam2026"})


def _edicao(t: str) -> Edicao:
    a0 = int(t[:4])
    a1 = a0 + 1 if "/" in t else a0
    pg = _PAG.get(t, "")
    return Edicao(t, a0, a1, [(pg, 0, None)] if pg else [], "Championnat du Cameroun (Elite One)")


EDICOES: list[Edicao] = [_edicao(t) for t in _LISTA]
_POR = {e.temporada: e for e in EDICOES}
for _x in EDICOES:
    if not _x.trechos:
        _x.obs = "a RSSSF só traz o campeão"

# ------------------------------------------------------------------------------------------------ fonte de cada período
# até 1998 a RSSSF não traz os jogos: a tabela final, só o topo dela ("Top Final Table", sem números) ou só posição,
# jogos e pontos (classificação incompleta); 1968 e 1986/87 só o campeão; 1987/88, parte dos jogos (sem tabela)
_PARCIAL = {"1978/79": ("kam79", 14, 17), "1979/80": ("kam80", 15, 16), "1981": ("kam81", 15, 19),
            "1981/82": ("kam82", 15, 16), "1983/84": ("kam84", 16, 19), "1985/86": ("kam86", 14, 32),
            "1993": ("kam93", 14, 30), "1996": ("kam96", 14, 29)}
for _x in EDICOES:
    if _x.ano_inicio > 1998 or not _x.trechos:
        continue
    if _x.temporada in _PARCIAL:
        _x.trechos, _x.parcial = [], _PARCIAL[_x.temporada]
        _x.obs = "a RSSSF só traz a classificação incompleta (" + (
            "só os primeiros colocados)" if _x.ano_inicio < 1985 else "posição, jogos e pontos)")
    elif _x.temporada in ("1968", "1986/87"):
        _x.trechos = []
        _x.obs = "a RSSSF só traz o campeão"
    elif _x.temporada == "1987/88":
        _x.incompleta = "jogos incompletos (só os resultados que a página traz)"
    else:
        _x.tabelas, _x.trechos = _x.trechos, []
        _x.obs = "a RSSSF só traz a tabela final"
# 2024/25: só o Aigle Royal do Moungo jogou (a tabela dá "Aigle Royal (Moungo)"; os jogos, "Aigle Royal")
_POR["2024/25"].nomes = {"Aigle Royal": "Aigle Royal du Moungo"}

# ----------------------------------------------------------------------------------------------------- edições do ogol
# o ogol rotula pela data (o "2004/05" do ogol é o campeonato de 2005; o "2011", o de 2010/11...); 2013 a 2016 vêm vazios
_OGOL = {"2005": 1102, "2006": 2772, "2007": 2811, "2007/08": 2820, "2008/09": 4360, "2009/10": 12935, "2010/11": 75522,
         "2011/12": 75521, "2017": 125192, "2018": 125924, "2019": 133839, "2019/20": 157041, "2020/21": 159596,
         "2022": 163453, "2022/23": 170725, "2023/24": 181355, "2024/25": 193139, "2026": 212840}
for _t, _i in _OGOL.items():
    _POR[_t].ogol_id = _i
# 2010/11: a RSSSF só traz a tabela final; os jogos vêm do ogol
_POR["2010/11"].ogol, _POR["2010/11"].trechos = 75522, []
_POR["2010/11"].tabelas = [("kam2011", 0, None)]

# ---------------------------------------------------------------------------------------------------- sistema de pontos
# 2 pontos por vitória até 1987/88; 3 em 1988/89 e 1989/90 (a RSSSF anota "3 points for win"); 2 de novo de 1991 a 1994;
# 3 desde 1995 (contado nas tabelas da RSSSF)
for _x in EDICOES:
    if _x.ano_inicio < 1988 or 1991 <= _x.ano_inicio <= 1994:
        _x.sistema = (2, 1, 0)

# ---------------------------------------------------------------------------------------------------- jogos incompletos
for _t, _m in (("1999", "jogos incompletos (muitos jogos sem placar na página)"),
               ("2000", "jogos incompletos (falta a rodada 21: a página repete a 22 no lugar dela)"),
               ("2010/11", "jogos incompletos (sem os jogos do Union e do Caïman Douala, que o ogol não separa)")):
    _POR[_t].incompleta = _m

# --------------------------------------------------------------------------------------------------------------- fases
# 2020/21: a liga da LFPC parou na 1ª rodada; a edição é a "Ligue 2021", da FECAFOOT (linha 66 da página)
_POR["2020/21"].trechos = [("kam2021", 66, None)]
_POR["2022/23"].fases = [(r"^Playoff Stage", "Fase final")]
# 2004: dois grupos, depois a "Super Ligue Nationale" (título) e a "Ligue Nationale" (rebaixamento); a artilharia da
# Super Ligue (linha 654) encerraria o trecho antes da Ligue Nationale
_POR["2004"].trechos = [("kam04", 0, 654), ("kam04", 658, 834)]
_POR["2004"].fases = [(r"^Super Ligue Nationale", "Fase final"), (r"^Ligue Nationale", "Grupo do rebaixamento")]
# 2020/21 e 2022: mata-mata depois dos grupos
for _t in ("2020/21", "2022"):
    _POR[_t].fases = [(r"^Semifinals", "Semifinal"), (r"^Third Place Match", "Jogos de classificação"),
                      (r"^Relegation Playoff", "Desempate do rebaixamento")]
_POR["2022/23"].fases += [(r"^Relegation Playoff", "Desempate do rebaixamento")]
# 1961: a página só traz o campeão e os participantes
_POR["1961"].tabelas, _POR["1961"].obs = [], "a RSSSF só traz o campeão (e a lista dos 11 participantes)"
# 2019/20: "league abandoned on May 12; PWD de Bamenda declared champions, no relegation"
_POR["2019/20"].obs = ("abandonado em 12/05/2020 (pandemia de Covid-19); o PWD Bamenda foi declarado campeão, sem "
                       "rebaixamento")
