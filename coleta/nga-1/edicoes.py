"""Edições da 1ª divisão nigeriana (nga-1): a liga nacional, de 1972 a 2025/26 (National League, Professional League em
1990, Premier League em 1993; hoje Nigeria Premier Football League, NPFL).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): desde a
criação da liga, em 1972, como a liga e a imprensa contam (o título de 2025/26 foi o "9º" do Rangers, igual ao Enyimba).
Fica de fora a "Amachree Gold Cup" de 1971 (torneio anterior à liga, que a RSSSF conta), as ligas regionais e as copas.
2018 e 2019/20 foram abandonados e entram sem campeão.

Temporadas como na lista de campeões da RSSSF (nigchamp.html): ano civil até 2007, 2007/08 a 2011/12, ano civil de 2013 a
2019, 2019/20 a 2021/22, 2023 ("Abridged League") e 2023/24 a 2025/26.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página do ano (nig72 = 1970 a 1979; nig88 = 1987 e 1988;
  nig00 ... nig07; nig08 = 2007/08; nig2010 = 2009/10; nig2023 = 2023). Linha inicial 0: logo depois do cabeçalho; linha
  final None: a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a RSSSF só tem a tabela final.
- ogol: o calendário do ogol (liga-nigeriana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "nga-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: copa (o nome da copa não pode estar entre
# parênteses ou colchetes) ou outra divisão
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(Cup|Cups|Super Four|Super ?8|Charity|Shield)\b|"
              r"Division (One|Two|1|2)\b|Nationwide League|Nigeria National League|Nigerian Amateur|Second Level|"
              r"Participants 2nd level|Third Level|Promotion Playoff|Topscorers?\b|Top ?scorers|list of champions|"
              r"About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1972", "2007/08"
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


def _nome(a: int) -> str:
    if a < 1990:
        return "Nigeria National League"
    if a < 1993:
        return "Nigerian Professional League"
    if a < 2012:
        return "Nigerian Premier League"
    return "Nigeria Professional Football League"


# temporada -> página da RSSSF ("" = sem página)
_PAGINAS: dict[str, str] = {str(a): "nig72" for a in range(1972, 1980)}
_PAGINAS.update({str(a): "" for a in (1980, 1981, 1982)})
_PAGINAS.update({"1983": "nig83", "1984": "nig84", "1985": "nig85", "1986": "nig86", "1987": "nig88", "1988": "nig88"})
_PAGINAS.update({str(a): f"nig{a % 100:02d}" for a in range(1989, 2008)})
_PAGINAS.update({"2007/08": "nig08", "2008/09": "nig09", "2009/10": "nig2010", "2010/11": "nig2011", "2011/12": "nig2012"})
_PAGINAS.update({str(a): f"nig{a}" for a in range(2013, 2020)})
_PAGINAS.update({"2019/20": "nig2020", "2020/21": "nig2021", "2021/22": "nig2022", "2023": "nig2023",
                 "2023/24": "nig2024", "2024/25": "nig2025", "2025/26": "nig2026"})


def _edicao(t: str, pagina: str) -> Edicao:
    a0 = int(t[:4])
    a1 = a0 + 1 if "/" in t else a0
    return Edicao(t, a0, a1, [(pagina, 0, None)] if pagina else [], _nome(a0))


EDICOES: list[Edicao] = [_edicao(t, pg) for t, pg in _PAGINAS.items()]
_POR = {e.temporada: e for e in EDICOES}

# ------------------------------------------------------------------------------------------------ fonte de cada período
# 1972: a tabela final (a página nig72 tem a década inteira); 1973 a 1988: a RSSSF só traz o campeão (nig72, nig83 a
# nig86 e nig88 têm só finais, jogos soltos ou tabelas parciais); 1989 a 1997: só a tabela final
_POR["1972"].trechos, _POR["1972"].tabelas = [], [("nig72", 60, 80)]
_POR["1972"].obs = "a RSSSF só traz a tabela final"
for _a in range(1973, 1989):
    _x = _POR[str(_a)]
    _x.trechos = []
    _x.obs = "a RSSSF só traz o campeão" + (" (sem página do ano)" if _a in (1980, 1981, 1982) else "")
for _a in range(1989, 1998):
    _x = _POR[str(_a)]
    _x.tabelas, _x.trechos = _x.trechos, []
    _x.obs = "a RSSSF só traz a tabela final"
# pontos: 2-1-0 até 1989; de 1990 a 1994, 3 por vitória, 2 por empate com gols e 1 por empate sem gols (o ponto a mais do
# empate com gols vai no ajuste_pontos); 3-1-0 desde 1995
for _x in EDICOES:
    if _x.ano_inicio <= 1989:
        _x.sistema = (2, 1, 0)
# 1990: a página só traz os participantes e o campeão (sem tabela)
_POR["1990"].tabelas = []
_POR["1990"].obs = "a RSSSF só traz o campeão (e a lista dos participantes)"

# edição do ogol de cada temporada: o ogol rotula as temporadas de ano civil pelo ano anterior ("2016/17" = 2017; "2022/23"
# = 2023, a "Abridged League") e só tem jogos de 2008/09 em diante
def _rotulo_ogol(t: str) -> str:
    return t if "/" in t else f"{int(t) - 1}/{t[2:]}"


_arq = PASTA_DADOS / "ogol" / "edicoes.json"
if _arq.exists():
    import json
    _ids = {ed["nome"]: ed["id"] for ed in json.loads(_arq.read_text(encoding="utf-8"))}
    for _x in EDICOES:
        if _x.ano_inicio >= 2008:
            _x.ogol_id = _ids.get(_rotulo_ogol(_x.temporada))
# 2009/10, 2010/11 e 2011/12: a RSSSF não tem os jogos (ou só metade): os jogos vêm do ogol
for _t in ("2009/10", "2010/11", "2011/12"):
    _x = _POR[_t]
    _x.ogol = _x.ogol_id
    _x.tabelas, _x.trechos = _x.trechos, []
    _x.obs = "os jogos vêm do calendário do ogol (a RSSSF só traz " + ("parte deles" if _t == "2010/11" else "a tabela") + ")"
# 1998 a 2003 e 2007/08: a RSSSF não traz todos os jogos e o ogol não tem esses anos
for _t in ("1998", "1999", "2000", "2001", "2002", "2003", "2007/08"):
    _POR[_t].incompleta = "jogos incompletos (só os resultados que a página traz)"
# 2011/12: o ogol escreve o Akwa United com caracteres invisíveis e outro nome ("Akwa Star..."); a tabela da RSSSF dá Akwa
# United
_POR["2011/12"].nomes = {"A\ufeffkwa S\ufefftar\u028c": "Akwa United"}

# fase final depois de dois grupos: "Super League" (2006, 2007) e "Playoff Stage" (2019; "Super Six" em 2023)
for _t in ("2006", "2007"):
    _POR[_t].fases = [(r"^Super League", "Fase final")]
for _t in ("2019", "2023"):
    _POR[_t].fases = [(r"^Playoff Stage", "Fase final")]
# temporadas abandonadas: sem campeão
_POR["2018"].cancelada = ("temporada abandonada pela crise interna da federação nigeriana (\"league abandoned following "
                          "internal crisis at Nigerian Football Federation\"); a tabela é a do abandono")
_POR["2019/20"].cancelada = ("temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono (pela média de "
                             "pontos por jogo)")
_POR["2019/20"].incompleta = "jogos incompletos (só os resultados que a página traz)"
