"""Edições da 1ª divisão colombiana (col-1): uma por torneio que deu título de campeão colombiano.

Lista de títulos: RSSSF (colchamp.html), conferida com a Wikipédia. De 1948 a 2001 um campeão por ano (Apertura e
Finalización, de 1968 em diante, são fases da edição anual, com os quadrangulares, hexagonais e octogonais finais); 1989
não teve campeão (a fase final não foi jogada); 1995 foi a temporada de transição e 1995/96 e 1996/97 seguiram o calendário
europeu. De 2002 em diante, Apertura e Finalización dão título cada um: uma edição por torneio (em 2020 só houve o Apertura;
o Finalización foi cancelado). Ficam de fora a Copa Colombia, a Superliga, as liguillas e os jogos de promoção.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO). 1995/96 em diante.
- wiki: chave da página da Wikipédia em espanhol (wikipedia_jogos.py): 1948-1986, 1988-1990, 2011, 2012 e 2025.
- tabelas: trechos da RSSSF lidos só pelas tabelas (conferência e classificação dos anos da Wikipédia e dos anos sem jogos).
- sem jogos: 1987 e 1991-1995 (nenhuma fonte pública tem os jogos): tabela final e campeão.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "col-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Copa Colombia|Copa Postob|Primera B\b|Promotion|Relegation|Second Level|Segunda Divisi|Superliga|"
              r"Copa Sudamericana Playoff|Liguilla|Torneo I\b|list of|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1962", "1995/96", "2002 Apertura", "2002 Finalización"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""             # como está em colchamp.html ("" = o da lista pela temporada)
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, nome da fase), além do padrão
    nomes: dict[str, str] = field(default_factory=dict)          # grafia -> clube, quando a regra geral erra nesta edição
    soma_de: list[str] = field(default_factory=list)              # (não usado; mantido para o código comum)
    wiki: str | None = None             # chave da página da Wikipédia em espanhol com os jogos
    hist: str = ""                      # (não usado)
    ogol: int | None = None             # (não usado: o ogol não tem os jogos colombianos)
    espn: tuple[str, str] | None = None  # (não usado)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas

    @property
    def pontos_vitoria(self) -> int:
        """2 pontos até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


_SEM_WIKI = {1987, *range(1991, 1996)}
EDICOES: list[Edicao] = []
for _a in range(1948, 1996):
    EDICOES.append(_e(str(_a), _a, _a, [], f"Campeonato Profesional Colombiano {_a}",
                      wiki=None if _a in _SEM_WIKI else str(_a), tabelas=[(f"col{_a % 100:02d}", 0, None)]))
_POR = {e.temporada: e for e in EDICOES}
_POR["1989"].obs = "título não concedido: a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega (RSSSF)"
_POR["1995"].obs = "torneio de transição para o calendário europeu (Torneo Nivelación)"

EDICOES += [
    _e("1995/96", 1995, 1996, [("col96", 0, None)], "Campeonato Profesional Colombiano 1995/96 (Copa Mustang)"),
    _e("1996/97", 1996, 1997, [("col97", 0, None)], "Campeonato Profesional Colombiano 1996/97 (Copa Mustang)"),
]
for _a in range(1998, 2002):
    EDICOES.append(_e(str(_a), _a, _a, [(f"col{_a % 100:02d}", 0, None)], f"Campeonato Profesional Colombiano {_a}"))
_POR = {e.temporada: e for e in EDICOES}
# 1995/96 a 2001: os torneios do ano são fases da edição; o trecho para antes da 2ª divisão e do Torneo Adecuación 1997
_MUSTANG = [(r"^Copa Mustang II|^Second Stage \(Copa Mustang II\)", "Copa Mustang II"), (r"^Copa Mustang I\b", "Copa Mustang I"),
            (r"^Torneo Mustang II", "Torneo Mustang II"), (r"^Torneo Mustang I\b", "Torneo Mustang I"),
            (r"(?i)^(semifinal cuadrang|cuadrangulares semifinales|clausura cuadrangulares|cuadrangulares mustang)", "Quadrangulares semifinais"),
            (r"(?i)^cuadrangular final", "Quadrangular final"), (r"^Octogonal Final", "Octogonal final"),
            (r"^FINALISIMA", "Finalísima"), (r"^Torneo Apertura", "Apertura"), (r"^Torneo Finalizaci", "Finalización"),
            (r"^First Stage$", ""), (r"^Second Stage$", "Segunda fase"), (r"^Championship Final", "Final")]
for _t, _tr in (("1995/96", ("col96", 55, 974)), ("1996/97", ("col97", 36, 635)), ("1998", ("col98", 28, 917)),
                ("1999", ("col99", 29, 778)), ("2000", ("col00", 12, 1112)), ("2001", ("col01", 22, 1055))):
    _POR[_t].trechos = [_tr]
    _POR[_t].fases = list(_MUSTANG)

_AF = {   # (Apertura, Finalización): (linha inicial, linha final) na página do ano
    2002: ((12, 608), (608, 1256)), 2003: ((12, 571), (571, 1105)), 2004: ((12, 589), (589, 1131)),
    2005: ((12, 578), (578, None)), 2006: ((12, 479), (479, 844)), 2007: ((12, 584), (584, 967)),
    2008: ((12, 382), (382, 758)), 2009: ((12, 385), (385, 761)), 2010: ((24, 339), (339, 728)),
    2013: ((22, 429), (429, 839)), 2014: ((22, 368), (368, 773)), 2015: ((22, 418), (418, 830)),
    2016: ((22, 421), (421, 837)), 2017: ((22, 428), (428, 852)), 2018: ((24, 414), (414, 807)),
    2019: ((22, 475), (475, 924)), 2020: ((22, 435), None), 2021: ((22, 429), (429, 899)),
    2022: ((22, 488), (488, 965)), 2023: ((22, 500), (500, 972)), 2024: ((22, 479), (479, 950)),
}
# linhas das tabelas do Apertura e do Finalización nas páginas de 2011, 2012 e 2025 (os jogos vêm da Wikipédia)
_TAB_WIKI = {2011: ((24, 93), (93, 167)), 2012: ((24, 78), (78, 133)), 2025: ((22, 84), (84, 146))}
for _a in range(2002, 2026):
    _pg = f"col{_a % 100:02d}" if _a < 2010 else f"col{_a}"
    for _k, _t in enumerate(("Apertura", "Finalización")):
        _nome = f"Campeonato Profesional Colombiano {_a} – {_t}"
        if _a in (2011, 2012, 2025):   # a página da RSSSF traz só os mata-matas (2011, 2012) ou só as tabelas (2025)
            EDICOES.append(_e(f"{_a} {_t}", _a, _a, [], _nome, wiki=f"{_a} {_t}",
                              tabelas=[(_pg, *_TAB_WIKI[_a][_k])],
                              obs="jogos da Wikipédia em espanhol: a página da RSSSF " +
                                  ("só traz as tabelas" if _a == 2025 else "só traz os mata-matas")))
            continue
        _tr = _AF[_a][_k]
        if _tr is None:
            continue   # 2020: o Finalización foi cancelado
        EDICOES.append(_e(f"{_a} {_t}", _a, _a, [(_pg, *_tr)], _nome))
