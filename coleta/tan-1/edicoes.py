"""Edições da 1ª divisão tanzaniana (tan-1): a liga do continente (Tanganica), de 1965 a 2025/26 (hoje Ligi Kuu
Tanzania Bara, a "NBC Premier League").

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): a liga
nacional do continente desde 1965, com o campeão do continente em todos os anos. É a lista que a federação (TFF) e os
clubes contam (o título de 2024 foi o "30º" do Young Africans). Ficam de fora a liga de Dar es Salaam (1921 a 1964), a
"Union League" de 1982 a 2003 (o título entre os melhores do continente e de Zanzibar, que a lista da RSSSF dá como
campeão nesses anos), a liga de Zanzibar (membro associado da CAF, com liga própria) e as copas.

Temporadas: ano civil até 2007 (o "1995/96" e o "1996/97" das páginas da RSSSF são os campeonatos que a lista chama de
1996 e 1997); de 2007/08 em diante, duas metades (a lista chama 2007/08 de "2008").

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  Zanzibar, a Union League, uma copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-tanzaniana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "tan-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: Zanzibar e a Union League, copa (o nome da copa não
# pode estar entre parênteses ou colchetes) ou outra divisão
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(?-i:Cup|Cups|Super ?Cup|Charity|Shield|Second Level|Second Division|First Division|"
              r"Third Level)\b|\"?Zanzibar|\"?Islands? League|\"?Union League|National Play-?off|First League|"
              r"Second League|Championship League|Ligi Daraja|Ligi ya|Division (2|Two|II)\b|Promotion\b|Topscorers?\b|"
              r"Top ?scorers|list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1965", "2007/08"
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
    hist: str = ""                                                # (não usado na Tanzânia)
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


# temporadas (como a lista da RSSSF, com as de duas metades pelo nome) e a página de cada uma ("" = sem página)
_LISTA = [str(a) for a in range(1965, 2008)] + [f"{a}/{(a + 1) % 100:02d}" for a in range(2007, 2026)]
_PAG = {"1965": "tanz65", "1996": "tanz96", "1997": "tanz97", "1998": "tanz98", "1999": "tanz99"}
_PAG.update({str(a): f"tanz{a % 100:02d}" for a in range(1982, 1992)})
_PAG.update({str(a): f"tanz{a % 100:02d}" for a in range(2000, 2008)})
_PAG.update({"2007/08": "tanz08", "2008/09": "tanz09"})
_PAG.update({f"{a - 1}/{a % 100:02d}": f"tanz{a}" for a in range(2010, 2027)})


def _edicao(t: str) -> Edicao:
    a0 = int(t[:4])
    a1 = a0 + 1 if "/" in t else a0
    pg = _PAG.get(t, "")
    return Edicao(t, a0, a1, [(pg, 0, None)] if pg else [], "Ligi Kuu Tanzania Bara")


EDICOES: list[Edicao] = [_edicao(t) for t in _LISTA]
_POR = {e.temporada: e for e in EDICOES}
for _x in EDICOES:
    if not _x.trechos:
        _x.obs = "a RSSSF só traz o campeão"

# ------------------------------------------------------------------------------------------------ fonte de cada período
# até 1998 a RSSSF quase não traz jogos: os primeiros colocados (1965, 1983, 1995/96: classificação incompleta), a
# tabela (1985, 1986, 1987, 1989, 1996/97, 1998), a matriz de 1984 ou parte dos jogos (1988); 1982, 1990 e 1991 só têm
# um resultado ou a fase com Zanzibar (só o campeão)
_PARCIAL = {"1965": ("tanz65", 13, 16), "1983": ("tanz83", 13, 16), "1996": ("tanz96", 16, 20)}
for _t, _par in _PARCIAL.items():
    _POR[_t].trechos, _POR[_t].parcial = [], _par
    _POR[_t].obs = "a RSSSF só traz os primeiros colocados"
for _t in ("1982", "1990", "1991"):
    _POR[_t].trechos = []
    _POR[_t].obs = "a RSSSF só traz o campeão do continente"
for _t in ("1985", "1986", "1987", "1989", "1997", "1998"):
    _POR[_t].tabelas, _POR[_t].trechos = _POR[_t].trechos, []
    _POR[_t].obs = "a RSSSF só traz a tabela final"
_POR["1984"].tabelas, _POR["1984"].trechos, _POR["1984"].matriz = _POR["1984"].trechos, [], "tanz84"
_POR["1988"].incompleta = "jogos incompletos (só os resultados que a página traz)"

# 1999 a 2006: grupos e fase final ("Super Eight", "Mainland Championship Playoff") até 2004; liga única em 2005 e 2006
_POR["2000"].matriz = "tanz00"   # os grupos vêm em matrizes (matriz_grupos)
_POR["2000"].fases = [(r"^Super Eight", "Fase final")]
_POR["2001"].fases = [(r"^Mainland Championship Playoff", "Fase final")]
_POR["2002"].fases = [(r"^Group A Playoff", "Desempate do 2º lugar"), (r"^Second Stage", "Fase final")]
_POR["2003"].fases = [(r"^Super Eight", "Fase final")]
_POR["2004"].fases = [(r"^Super Eight", "Fase final")]

# ---------------------------------------------------------------------------------------------------- sistema de pontos
# 2 pontos por vitória até 1989 (pelas tabelas); 3 em 1996/97 e 1998 (pelas tabelas); entre 1990 e 1995/96 a página
# não traz pontos: 2 até 1995 e 3 desde 1995/96 (a FIFA passou aos 3 pontos em 1995)
for _x in EDICOES:
    if _x.ano_inicio <= 1995:
        _x.sistema = (2, 1, 0)
# 2007: mini-liga de transição (três grupos, o "Super Six" em dois grupos de três, lido como fase final sem grupo, e a
# final)
_POR["2007"].fases = [(r"^Final \[", "Final")]
_POR["2007"].obs = ("mini-liga de transição (\"Ligi Ndogo\") antes da mudança para temporadas de duas metades; a "
                    "final (Simba x Young Africans, 1-1 e pênaltis) deu as vagas da CAF de 2008")

# ----------------------------------------------------------------------------------------------------- edições do ogol
# o ogol rotula como a RSSSF; só tem jogos de 2007/08 em diante
import json as _json   # noqa: E402

_ED_OGOL = {x["nome"]: x["id"] for x in _json.loads((PASTA_DADOS / "ogol" / "edicoes.json").read_text(encoding="utf-8"))}
for _x in EDICOES:
    if _x.ano_inicio >= 2007 and _x.temporada in _ED_OGOL:
        _x.ogol_id = _ED_OGOL[_x.temporada]
# 2011/12: a RSSSF só traz a tabela final; os jogos vêm do ogol
_POR["2011/12"].ogol = _POR["2011/12"].ogol_id
_POR["2011/12"].tabelas, _POR["2011/12"].trechos = _POR["2011/12"].trechos, []

# ---------------------------------------------------------------------------------------------------- jogos incompletos
# 2000 a 2006: a página não tem todos os jogos (resultados que faltam, matrizes com células em branco, o "Super Eight" de
# 2004 só até a 6ª rodada); a classificação é a tabela da página
_INCOMPLETA = {
    "2000": "jogos incompletos (três jogos dos grupos sem resultado na página)",
    "2001": "jogos incompletos (faltam resultados da 1ª fase)",
    "2002": "jogos incompletos (faltam resultados da 1ª fase e três do \"Super 8\")",
    "2003": "jogos incompletos (faltam resultados da 1ª fase e gols do \"Super Eight\")",
    "2004": "jogos incompletos (faltam resultados da 1ª fase e do \"Super Eight\")",
    "2005": "jogos incompletos (só os resultados que a página traz)",
    "2006": "jogos incompletos (só os resultados que a página traz)",
}
for _t, _m in _INCOMPLETA.items():
    _POR[_t].incompleta = _m

# o "Relegation Playoff" (desde 2021/22) é desempate entre os dois que ficam logo acima da zona de queda e o 2º/3º da
# divisão de baixo, fora da tabela
for _x in EDICOES:
    if _x.ano_inicio >= 2021:
        _x.fases = _x.fases + [(r"^Relegation Play-?off", "Desempate do rebaixamento")]
