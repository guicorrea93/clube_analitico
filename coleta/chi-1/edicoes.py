"""Edições da 1ª divisão chilena (chi-1): uma por torneio que deu título de campeão chileno.

Lista de títulos: RSSSF (chilechamp.html), conferida com a Wikipédia. De 1933 a 1996 um campeão por ano; Apertura e
Clausura deram título cada um em 1997, de 2002 a 2009, 2011, 2012 e de 2013/14 a 2016/17 (uma edição por torneio, como no
arg-1); os torneios de Transición de 2013 e 2017 também. 2010 e de 2018 em diante, um campeão por ano ("2020" é a temporada
2020/21). Ficam de fora a Copa Chile, as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes da
2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO).
- ogol: os anos em que a RSSSF só tem a tabela final (1984 a 1995 e 2025): o calendário do ogol é a base (ogol_jogos).
- espn: (início, fim) das datas da fase de pontos corridos do Clausura 2011 e de 2012, que a página da RSSSF não traz
  (só os mata-matas).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "chi-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(?:\d{4}\s+)?(Second Division|Segunda Divisi|Primera B\b|Primera Divisi[oó]n B\b|Copa (Chile|de Chile|Polla|"
              r"Sudamericana|Libertadores|Carranza|Apertura)|Liguilla|Promotion|Pre-?Libertadores|COPA LIBERTADORES|"
              r"Playoff for Third|Campeonato Nacional de F|Campeonato de (Apertura|Clausura)|list of|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1955", "2002 Apertura", "2013 Transición", "2013/14 Clausura"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""             # como está em chilechamp.html ("" = o da lista pela temporada)
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, nome da fase), além do padrão
    nomes: dict[str, str] = field(default_factory=dict)          # grafia -> clube, quando a regra geral erra nesta edição
    soma_de: list[str] = field(default_factory=list)              # (não usado no Chile; mantido para o código comum)
    wiki: int | None = None             # (não usado no Chile)
    hist: str = ""                      # (não usado no Chile)
    ogol: int | None = None             # ano do calendário do ogol que é a base dos jogos
    espn: tuple[str, str] | None = None  # datas (AAAA-MM-DD) da fase de pontos corridos tirada da ESPN
    tabelas: list[tuple[str, int, int]] = field(default_factory=list)   # trechos lidos só pelas tabelas (sem jogos)

    @property
    def pontos_vitoria(self) -> int:
        """2 pontos até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.ogol is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _anual(a: int) -> Edicao:
    if 1984 <= a <= 1995:
        return _e(str(a), a, a, [], f"Campeonato Nacional de Primera División {a}", ogol=a,
                  obs="a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol")
    return _e(str(a), a, a, [(f"chile{a % 100:02d}", 0, None)], f"Campeonato Nacional de Primera División {a}")


EDICOES: list[Edicao] = [_anual(a) for a in range(1933, 1997)]
_POR = {e.temporada: e for e in EDICOES}
# 1968-1970: Metropolitano e Provincial (1ª fase), depois Nacional (título) e Promocional (rebaixamento)
for _a in (1968, 1969, 1970):
    _POR[str(_a)].fases = [(r"^Torneo Metropolitano", "Metropolitano"), (r"^Torneo Provincial", "Provincial"),
                           (r"^Torneo Promocional", "Promocional"), (r"^Torneo Nacional", "Nacional"),
                           (r"^Fifth Place Playoff", "Desempate do 5º lugar")]
_POR["1968"].fases += [(r"^Serie A$", "Promocional – Série A"), (r"^Serie B$", "Promocional – Série B")]
_POR["1933"].trechos = [("chile33", 34, None)]   # o "Campeonato de Apertura" do topo é a copa do começo do ano

# 1997: Apertura e Clausura
EDICOES += [
    _e("1997 Apertura", 1997, 1997, [("chile97", 0, 250)], "Campeonato Nacional de Primera División 1997 – Apertura"),
    _e("1997 Clausura", 1997, 1997, [("chile97", 250, 495)], "Campeonato Nacional de Primera División 1997 – Clausura"),
    _anual(1998), _anual(1999), _anual(2000), _anual(2001),
]
EDICOES[-2].trechos = [("chile00", 226, None)]
EDICOES[-3].fases = [(r"^Championship Playoff", "Fase final"), (r"^Relegation Playoff", "Grupo do rebaixamento")]   # 1999: octogonal final   # 2000: a página abre com a Copa Carranza e o Apertura (copa)
_TRECHOS_AC = {   # (Apertura, Clausura) por página
    2002: ([("chile02", 0, 539)], [("chile02", 590, 1085)]),
    2003: ([("chile03", 0, 559)], [("chile03", 645, 1200)]),
    2004: ([("chile04", 0, 659)], [("chile04", 770, 1388)]),
    2005: ([("chile05", 0, 682)], [("chile05", 692, 1353)]),
    2006: ([("chile06", 0, 670)], [("chile06", 670, 1313)]),
    2007: ([("chile07", 17, 663)], [("chile07", 676, 1418)]),
    2008: ([("chile08", 0, 690)], [("chile08", 690, 1359)]),
    2009: ([("chile09", 26, 510), ("chile09", 565, 612)], [("chile09", 612, 1180)]),   # playoff da Sudamericana no meio
    2011: ([("chile2011", 30, 594)], [("chile2011", 606, 697)]),
    2012: ([("chile2012", 25, 95)], [("chile2012", 95, 183)]),
}
for _a in range(2002, 2013):
    if _a == 2010:
        EDICOES.append(_e("2010", 2010, 2010, [("chile2010", 0, None)], "Campeonato Nacional de Primera División 2010"))
        continue
    _ta, _tc = _TRECHOS_AC[_a]
    EDICOES.append(_e(f"{_a} Apertura", _a, _a, _ta, f"Campeonato Nacional de Primera División {_a} – Apertura"))
    EDICOES.append(_e(f"{_a} Clausura", _a, _a, _tc, f"Campeonato Nacional de Primera División {_a} – Clausura"))
_POR = {e.temporada: e for e in EDICOES}
# Apertura e Clausura com mata-mata (2002 em diante): "First Round" é a oitava de final; "Qualifying Playoff", a repescagem
for _e2 in EDICOES:
    if _e2.ano_inicio >= 2002 and re.search(r"Apertura|Clausura", _e2.temporada):
        _e2.fases = [(r"^First Round", "Oitavas de final"), (r"^Qualifying Playoff", "Repechaje")]
# 2012: a página da RSSSF traz só os mata-matas; a fase de pontos corridos vem da ESPN
_POR["2011 Clausura"].espn = ("2011-07-01", "2011-12-31")
_POR["2011 Clausura"].obs = "a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN"
_POR["2012 Apertura"].espn = ("2012-01-01", "2012-06-30")
_POR["2012 Clausura"].espn = ("2012-07-01", "2012-12-31")
for _t in ("2012 Apertura", "2012 Clausura"):
    _POR[_t].obs = "a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN"

EDICOES.append(_e("2013 Transición", 2013, 2013, [("chile2013", 21, 323)], "Campeonato Nacional de Primera División 2013 – Torneo de Transición",
                  obs="torneio de transição para o calendário europeu"))
for _a, _pg, _ta, _tc in [(2013, "chile2014", (24, 314), (314, 608)), (2014, "chile2015", (24, 309), (330, 618)),
                          (2015, "chile2016", (24, 293), (293, 571)), (2016, "chile2017", (24, 270), (270, 510))]:
    _s = f"{_a}/{(_a + 1) % 100:02d}"
    EDICOES.append(_e(f"{_s} Apertura", _a, _a, [(_pg, *_ta)], f"Campeonato Nacional de Primera División {_s} – Apertura"))
    EDICOES.append(_e(f"{_s} Clausura", _a, _a + 1, [(_pg, *_tc)], f"Campeonato Nacional de Primera División {_s} – Clausura"))
EDICOES.append(_e("2017 Transición", 2017, 2017, [("chile2017a", 19, 270)], "Campeonato Nacional de Primera División 2017 – Torneo de Transición",
                  obs="torneio de transição de volta ao calendário anual"))
for _a in range(2018, 2025):
    EDICOES.append(_e(str(_a), _a, _a + 1 if _a == 2020 else _a, [(f"chile{_a}", 0, None)], f"Campeonato Nacional de Primera División {_a}",
                      obs="temporada esticada até fevereiro de 2021 pela pandemia (a RSSSF chama de 2020/21)" if _a == 2020 else
                      "campeonato encerrado na 24ª rodada pelos protestos de outubro de 2019; a ANFP declarou campeão o líder" if _a == 2019 else ""))
EDICOES.append(_e("2025", 2025, 2025, [], "Campeonato Nacional de Primera División 2025", ogol=2025, tabelas=[("chile2025", 19, 45)],
                  obs="a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol"))
