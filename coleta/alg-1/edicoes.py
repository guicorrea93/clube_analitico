"""Edições da 1ª divisão argelina (alg-1): o campeonato nacional, de 1962/63 a 2025/26.

Lista de campeões: RSSSF (algchamp.html), conferida com a Wikipédia em inglês ("List of Algerian football champions").
Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): só desde a
independência, como a RSSSF ("64 títulos; desde a independência"), a Wikipédia e a contagem dos clubes. A era colonial
(ligas regionais de Argel, Orã e Constantine; "campeonato da Argélia" de 1957/58 a 1960/61) fica de fora, como as copas e
a 2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página algAA (ou algAAAA desde 2009/10): a do ano em que a
  temporada termina (alg63 = 1962/63; alg00 = 1999/00; alg2010 = 2009/10). Linha inicial 0: a 1ª divisão é a primeira
  seção depois do índice do topo; linha final None: vai até a seção seguinte do índice (ler_rsssf.secao()).
- ogol: o calendário do ogol, quando a RSSSF não tem os jogos.
Pontos: 3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95 e 3-1-0 desde 1995/96, como as
tabelas da RSSSF contam ("NB: 3-2-1 points system").
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "alg-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando nem a edição nem o índice dizem a linha final)
FIM_PADRAO = (r"^(Coupe\b|Cups?\b|Cup Tournaments|Algerian Cup|Promotion|Barrage|Second (Level|Division)|"
              r"Championnat (Nationale? )?(II|Division (2|II))\b|Ligue (II|2)\b|Division (2|II)\b|2[eè]me Division|Third level|"
              r"Topscorers?\b|Top ?scorers|list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1962/63"
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
    hist: str = ""                                                # (não usado na Argélia)
    ogol: int | None = None
    espn: tuple[str, str] | None = None                           # (não usado: a ESPN não tem a liga argelina)
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
        if a >= 1986:
            return (2, 1, 0)
        return (3, 2, 1)

    @property
    def pontos_vitoria(self) -> int:
        return self.pontos[0]

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.ogol is None and self.matriz is None


def _temp(a: int) -> str:
    return f"{a}/{(a + 1) % 100:02d}"


def pagina(ano_fim: int) -> str:
    return f"alg{ano_fim}" if ano_fim >= 2010 else f"alg{ano_fim % 100:02d}"


def _nome(a: int) -> str:
    if a <= 1963:
        return "Championnat d'Algérie (Critérium d'Honneur)"
    if a >= 2010:
        return "Ligue Professionnelle 1"
    if 1999 <= a <= 2001:
        return "Super Division"
    return "Championnat National de 1ère Division"


EDICOES: list[Edicao] = [Edicao(_temp(a), a, a + 1, [(pagina(a + 1), 0, None)], _nome(a)) for a in range(1962, 2026)]
_POR = {e.temporada: e for e in EDICOES}


# ------------------------------------------------------------------------------------------------ casos especiais
# 1962/63 e 1963/64: ligas regionais (Argel, Orã, Constantine) e a fase final ("Championship Playoff": semifinais, 3º lugar
# e final)
_MATA = [(r"^Semi-?finals?", "Semifinal"), (r"^Third Place", "Jogos de classificação"), (r"^Final\b(?! Table)", "Final")]
_POR["1962/63"].fases = list(_MATA)
_POR["1962/63"].incompleta = "jogos incompletos (só a 2ª fase das ligas regionais e a fase final)"
_POR["1962/63"].obs = ("a RSSSF não traz a 1ª fase das ligas regionais; a semifinal USM Alger 2-2 USM Annaba foi decidida "
                       "pelos escanteios (7-6)")
# 1963/64: os jogos de acesso à 1ª divisão do ano seguinte (linhas 821 a 839) ficam de fora; o "Playoff match" da Liga de
# Constantine (vencedores dos grupos Oeste e Leste) decide quem vai à fase final
_POR["1963/64"].trechos = [("alg64", 0, 821), ("alg64", 840, None)]
_POR["1963/64"].fases = [(r"^Playoff match$", "Desempate da Liga de Constantine")] + _MATA
_POR["1963/64"].incompleta = "jogos incompletos (resultados conhecidos das ligas regionais e a fase final)"
# 1997/98: dois grupos de 8, final ("Championship Final"), 3º lugar não jogado e desempates de rebaixamento (que não
# valeram: a 1ª divisão foi reorganizada e ninguém caiu)
_POR["1997/98"].fases = [(r"^Relegation Play-?off", "Desempate do rebaixamento"), (r"^Third Place", "Jogos de classificação")]
_POR["1997/98"].obs = ("ninguém caiu: a 1ª divisão de 1998/99 passou a dois grupos de 14 (os desempates de rebaixamento "
                       "não valeram)")
# 1998/99: dois grupos de 14 e a final ("Championship Playoff"); o "Arab Cup Playoff" (linha 937) não é do campeonato
_POR["1998/99"].trechos = [("alg99", 0, 937)]
_POR["1998/99"].fases = [(r"^Championship Play-?off", "Final")]
# 2019/20: parado em março de 2020 (Covid-19); a federação deu o título ao CR Belouizdad pela média de pontos por jogo
_POR["2019/20"].incompleta = "temporada interrompida (Covid-19)"
_POR["2019/20"].obs = ("parada em 15/03/2020 pela Covid-19; a federação declarou o CR Belouizdad campeão pela média de "
                       "pontos por jogo, sem rebaixamento")
# 1996/97: "US Constantine" (rodadas 15 e 22) é o US Chaouia (que fica sem esses dois jogos; o CS Constantine joga na mesma
# rodada)
_POR["1996/97"].nomes = {"US Constantine": "US Chaouia"}
