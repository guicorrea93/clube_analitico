"""Edições da 1ª divisão venezuelana (ven-1): uma por título, como na lista de campeões da RSSSF (venezchamp.html), que conta 106
títulos desde 1920/21.

- 1921-1956: era amadora (a temporada 1920/21 é a edição "1921", como na Wikipédia), um campeão por ano; os anos sem
  página da RSSSF (1922, 1924, 1931, 1938, 1939, 1949, 1950) entram só com campeão e vice.
- 1957-1986: era profissional, um campeão por ano (Apertura, Clausura, liguillas e finais são fases).
- 1986/87 a 2014/15: calendário europeu ("1986/87").
- 2015: Torneo de Adecuación (Zamora). A RSSSF o conta como título; a Wikipédia em inglês não ("não foi uma temporada
  completa"). Entra como edição, como na lista da RSSSF (decisão registrada no relatório).
- 2016-2025: um campeão por ano (Apertura e Clausura com final entre os vencedores).
Ficam de fora a 2ª e a 3ª divisões, a Copa Venezuela (salvo quando era a 1ª fase da temporada: 1993/94 a 1995/96 e
2000/01), as outras copas (Copa Caracas, Liga Mayor, de las Naciones, Cuatricentenario, Valencia, de Campeones,
Bicentenario) e os playoffs da Sudamericana e da Conmebol.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). Página venezYY (ou venezAAAA de 2010 em diante): a do ano; nas temporadas
  europeias, a do ano em que terminam (venez87 = 1986/87). A página venez2016 traz o Adecuación 2015 e a temporada 2016.
- espn: datas dos jogos que vêm da ESPN (2025: a RSSSF só tem as tabelas).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "ven-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Copa (Venezuela|Caracas|Liga Mayor|de las Naciones|Cuatricentenario|Valencia|de Campeones|Bicentenario)|"
              r"Copa Sudamericana Playoff|Copa Conmebol Playoff|Second Level|Segunda Divisi|Tercera Divisi|Third Level|"
              r"Torneo de Promoci|Promotion/Relegation|Torneo Ascenso|Torneo de Aspirantes|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1921", "1986/87", "2015"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: str | None = None                                       # (não usado)
    hist: str = ""                                                # (não usado)
    ogol: int | None = None                                       # (não usado)
    espn: tuple[str, str] | None = None                           # datas dos jogos que vêm da ESPN
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""                                           # o que falta nos jogos (entra na observação)

    @property
    def pontos_vitoria(self) -> int:
        """2 por vitória até 1994/95; 3 a partir de 1995/96."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _pagina(ano_fim: int) -> str:
    return f"venez{ano_fim % 100:02d}" if ano_fim < 2010 else f"venez{ano_fim}"


_SEM_PAGINA = "sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)"
# trechos explícitos: a página tem outra competição no meio ou duas edições
_TRECHOS: dict[str, list[tuple[str, int, int | None]]] = {
    "1994/95": [("venez95", 0, 536)],          # a "Copa Venezuela Final Round" (linha 172) é a final do Apertura
    "2011/12": [("venez2012", 17, 80)],        # só as tabelas; a Copa Venezuela 2011 vem logo depois
    "2015": [("venez2016", 26, 397)],          # Torneo Adecuación 2015
    "2016": [("venez2016", 410, 1167)],
}
_FASES_ANO: dict[str, list[tuple[str, str]]] = {
    # 1960: os dois turnos são fases com tabela própria, com desempate no 2º e final entre os vencedores
    "1960": [(r"^First round$", ""), (r"^Second round$", "Segunda fase"), (r"^Second round Playoff$", "Desempate da segunda fase")],
    # 1994/95: Apertura (Copa Venezuela), Torneo Iniciación (grupos), Torneo Nacional (grupos) e Torneo Finalización (o título)
    "1994/95": [(r"^Torneo Nacional$", "Segunda fase"), (r"^Torneo Finalizaci[oó]n$", "Fase final")],
}
_POUCOS = ("a página da RSSSF traz só parte dos jogos da liga (ou nenhum) e não tem a tabela completa: entram os jogos que ela "
           "tem; os das copas da mesma página (Copa Venezuela, Copa IND, Copa del Distrito Federal...) ficam de fora")
# era amadora: só 1940, 1955 e 1956 têm todos os jogos na RSSSF
_INCOMPLETA: dict[str, str] = {
    **{str(a): _POUCOS for a in range(1921, 1955) if a != 1940},
    "1994/95": "o Torneo Iniciación (1ª fase da liga) só tem as tabelas dos grupos na RSSSF; 5 jogos do Apertura (Copa Venezuela) "
               "estão como empate sem placar (\"drw\") e ficam de fora",
    "1993/94": "a 1ª fase (Apertura, a Copa Venezuela) só tem as tabelas dos grupos na RSSSF, e 8 jogos da liga estão sem placar",
}
# 2010/11: o Clausura 2011 tem rodadas sem placar na RSSSF; 2011/12: a página só tem as tabelas
_ESPN = {"2010/11": ("2011-01-01", "2011-05-31"), "2011/12": ("2011-07-01", "2012-06-30"), "2025": ("2025-01-01", "2025-12-31")}
_ESPN_FASES = {"2010/11": [("2011-01-01", "Clausura")], "2011/12": [("2011-07-01", "Apertura"), ("2012-01-01", "Clausura")],
               # 2025: fase regular, liguillas (maio-junho; a partir de 17 de outubro); as finais vêm da página
               "2025": [("2025-01-01", "Apertura"), ("2025-05-01", "Liguillas do Apertura"), ("2025-07-01", "Clausura"),
                        ("2025-10-10", "Liguillas do Clausura")]}

EDICOES: list[Edicao] = []
_PAGINAS = {p.stem for p in (PASTA_DADOS / "rsssf").glob("venez*.html")}

for _a in range(1921, 1957):   # era amadora
    _pg = _pagina(_a)
    _t = str(_a)
    EDICOES.append(_e(_t, _a, _a, _TRECHOS.get(_t, [(_pg, 0, None)] if _pg in _PAGINAS else []),
                      f"Campeonato Nacional de Fútbol {_a}" + (" (1920/21)" if _a == 1921 else ""),
                      obs="" if _pg in _PAGINAS else _SEM_PAGINA, incompleta=_INCOMPLETA.get(_t, "") if _pg in _PAGINAS else ""))
for _a in range(1957, 1987):   # profissional, ano fechado
    _t = str(_a)
    EDICOES.append(_e(_t, _a, _a, _TRECHOS.get(_t, [(_pagina(_a), 0, None)]), f"Primera División de Venezuela {_a}",
                      fases=list(_FASES_ANO.get(_t, [])), incompleta=_INCOMPLETA.get(_t, "")))
for _a in range(1986, 2015):   # calendário europeu
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    EDICOES.append(_e(_t, _a, _a + 1, _TRECHOS.get(_t, [(_pagina(_a + 1), 0, None)]), f"Primera División de Venezuela {_t}",
                      fases=list(_FASES_ANO.get(_t, [])), espn=_ESPN.get(_t), espn_fases=_ESPN_FASES.get(_t, []),
                      incompleta=_INCOMPLETA.get(_t, "")))
for _a in range(2015, 2026):
    _t = str(_a)
    _nome = "Torneo de Adecuación 2015" if _a == 2015 else (f"Liga FUTVE {_a}" if _a >= 2017 else f"Primera División de Venezuela {_a}")
    EDICOES.append(_e(_t, _a, _a, _TRECHOS.get(_t, [(_pagina(_a), 0, None)]), _nome, fases=list(_FASES_ANO.get(_t, [])),
                      espn=_ESPN.get(_t), espn_fases=_ESPN_FASES.get(_t, []), incompleta=_INCOMPLETA.get(_t, "")))
