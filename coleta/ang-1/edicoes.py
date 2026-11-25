"""Edições da 1ª divisão angolana (ang-1): o Girabola, de 1979 a 2025/26.

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): o Girabola
desde o primeiro, em 1979, como a federação o numera (2025/26 é o "XLVIII Girabola") e os clubes contam os títulos. A
temporada 2019/20, abandonada pela pandemia de Covid-19, entra sem campeão. Fica de fora o Campeonato Provincial da era
colonial (1941 a 1974; 1975 abandonado), que a federação não conta, e as copas (Taça e Supertaça).

Temporadas: ano civil de 1979 a 2018; duas metades de 2018/19 em diante (as páginas da RSSSF e o ogol rotulam igual).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a Taça, a Supertaça ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-angolana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "ang-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada: copa (o nome da copa não pode estar entre
# parênteses ou colchetes) ou outra divisão; os nomes de divisão não ignoram maiúsculas (notas corridas os citam)
FIM_PADRAO = (r"^(?![\d\s])(?:[^\[(]*\b(?-i:Ta[çc]a|Superta[çc]a|Cup|Super ?Cup|Segundona|Second Level|Second Division|"
              r"Divis[ãa]o de Honra|Provincial)\b|Topscorers?\b|Top ?scorers|Melhores marcadores|list of champions|"
              r"About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1979", "2018/19"
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
    hist: str = ""                                                # (não usado em Angola)
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


# temporadas e a página de cada uma
_LISTA = [str(a) for a in range(1979, 2019)] + [f"{a}/{(a + 1) % 100:02d}" for a in range(2018, 2026)]
_PAG = {str(a): f"ango{a % 100:02d}" for a in range(1979, 2010)}
_PAG.update({str(a): f"ango{a}" for a in range(2010, 2019)})
_PAG.update({f"{a - 1}/{a % 100:02d}": f"ango{a}" for a in range(2019, 2027)})


def _edicao(t: str) -> Edicao:
    a0 = int(t[:4])
    a1 = a0 + 1 if "/" in t else a0
    return Edicao(t, a0, a1, [(_PAG[t], 0, None)], "Girabola")


EDICOES: list[Edicao] = [_edicao(t) for t in _LISTA]
_POR = {e.temporada: e for e in EDICOES}

# ----------------------------------------------------------------------------------------------------- edições do ogol
# o ogol rotula como a RSSSF (ano civil até 2018, duas metades depois)
_ED_OGOL = {x["nome"]: x["id"] for x in json.loads((PASTA_DADOS / "ogol" / "edicoes.json").read_text(encoding="utf-8"))} \
    if (PASTA_DADOS / "ogol" / "edicoes.json").exists() else {}
for _x in EDICOES:
    _x.ogol_id = _ED_OGOL.get(_x.temporada)

# ---------------------------------------------------------------------------------------------------- sistema de pontos
# 2 pontos por vitória até 1994; 3 desde 1995 ("introduction of 3-1-0 point system in 1995", lista da RSSSF)
for _x in EDICOES:
    if _x.ano_inicio <= 1994:
        _x.sistema = (2, 1, 0)

# 2019/20: "championship suspended due to Covid-19 pandemic and abandoned on May 14"
_POR["2019/20"].cancelada = "abandonado em 14/05/2020 (pandemia de Covid-19), sem campeão"

# ------------------------------------------------------------------------------------------------ fonte de cada período
# 1981 a 1997: a RSSSF só traz a tabela final (1981 e 1982 têm uns poucos resultados soltos, que ficam de fora)
for _x in EDICOES:
    if 1981 <= _x.ano_inicio <= 1997:
        _x.tabelas, _x.trechos = _x.trechos, []
        _x.obs = "a RSSSF só traz a tabela final"
# 1979: quatro grupos de seis, fase final e final

# 1998: a página não traz todos os jogos (de 20 a 22 dos 28 de cada clube); a classificação é a tabela final
_POR["1998"].incompleta = "jogos incompletos (só os resultados que a página traz)"
# 2006: só uma Académica na liga, a do Soyo (Kwanda); os jogos a chamam só de "Académica"
_POR["2006"].nomes = {"Académica": "Académica do Soyo"}
