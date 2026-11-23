"""Edições da 1ª divisão uruguaia (uru-1): uma por torneio que deu título de campeão uruguaio.

Lista de títulos: RSSSF (uruchamp.html), conferida com a Wikipédia. Os cismas de 1923 e 1924 dão duas edições cada
(AUF e FUF, a liga dissidente), como a RSSSF conta ("consideramos os dois campeonatos de igual valor"); 1926 é o Torneo del
Consejo Provisorio, que reuniu as duas ligas. Sem edição: 1904 e 1930 (não houve campeonato) e 1925 (AUF e FUF não
terminaram). 1948 entra sem campeão (abandonado na greve dos jogadores, com a tabela do abandono).

De 1932 a 2025 há um campeão por ano (ou temporada, de 2005/06 a 2015/16, no calendário europeu): Apertura, Intermedio e
Clausura não dão título de campeão uruguaio e entram como fases da edição, com os desempates e finais de cada um, a tabela
anual e as finais do campeonato. Ficam de fora as liguillas pré-Libertadores, o Torneo Integración (1994), o Torneo Nacional
(1996), a Copa Artigas, o Torneo Permanencia (2001-2002), o Reclasificatorio (2004) e os jogos de promoção contra clubes da
2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final
  None: até o primeiro título de outra competição (FIM_PADRAO). 1932-1959, 1965 e 1994 em diante (a página de 1969
  traz só 18 das 20 rodadas e nenhum jogo da fase de campeonato: 1969 vem da Wikipédia).
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1900, 1901, 1905, 1908, 1916, 1960-1964 e
  1966-1974.
- sem nenhuma das duas (1902-1931 fora esses anos, 1975-1993): edição sem jogos, só com a tabela final da RSSSF
  (uruhist.html) e o campeão. Os jogos desses anos não estão em nenhuma fonte pública que achamos (relatório).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "uru-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(?:Uruguay )?(Second Level|Second Division|Primera B\b|Segunda Divisi|Third Level|Division Extra|Intermedia\b|"
              r"Liguilla|Torneo Integraci|Torneo Nacional|Torneo Permanencia|Reclasificatorio|Copa (Artigas|AUF|de la Liga)|"
              r"Promotion|About this document|list of)")


@dataclass
class Edicao:
    temporada: str                      # "1923 FUF", "1960", "2005/06"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""             # como está em uruchamp.html ("" = o da lista pelo ano)
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, nome da fase), além do padrão
    nomes: dict[str, str] = field(default_factory=dict)          # grafia -> clube, quando a regra geral erra nesta edição
    soma_de: list[str] = field(default_factory=list)              # (não usado no Uruguai; mantido para o código comum)
    wiki: int | None = None             # ano da página da Wikipédia em espanhol com os jogos
    hist: str = ""                      # rótulo da tabela no uruhist.html quando o ano tem duas ("AUF", "FUF")

    @property
    def pontos_vitoria(self) -> int:
        """2 pontos até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


_WIKI = {1900, 1901, 1905, 1908, 1916, *range(1960, 1965), *range(1966, 1975)}
_RSSSF = {*range(1932, 1960), 1965, *range(1994, 2005)}


def _liga(a: int) -> str:
    if a <= 1907:
        return "Uruguay Association Foot-ball League"
    if a <= 1914:
        return "Liga Uruguaya de Football"
    return "Asociación Uruguaya de Football" if a <= 1931 else "Asociación Uruguaya de Fútbol"


EDICOES: list[Edicao] = []
for _a in range(1900, 2005):
    if _a in (1904, 1925, 1930):
        continue
    if _a in (1923, 1924):
        for _l, _nl in (("AUF", "Asociación Uruguaya de Football"), ("FUF", "Federación Uruguaya de Football")):
            EDICOES.append(_e(f"{_a} {_l}", _a, _a, [], f"{_nl} – Campeonato {_a}", hist=_l,
                              obs="cisma do futebol uruguaio (1922-1925): a FUF foi fundada por Peñarol e Central depois de "
                                  "expulsos da AUF; as duas ligas tiveram campeonato" if _l == "FUF" else ""))
        continue
    _tr = [(f"uru{_a % 100:02d}", 0, None)] if _a in _RSSSF else []
    _nome = ("Torneo del Consejo Provisorio 1926" if _a == 1926 else
             f"{_liga(_a)} – Campeonato {_a}" if _a <= 1931 else f"Campeonato Uruguayo de Primera División {_a}")
    EDICOES.append(_e(str(_a), _a, _a, _tr, _nome, wiki=_a if _a in _WIKI else None))

_POR = {e.temporada: e for e in EDICOES}
# páginas com outra competição no meio do trecho da 1ª divisão: as linhas de cada pedaço
_POR["1996"].trechos = [("uru96", 0, 400), ("uru96", 411, 425)]          # promoção no meio; depois, a final; Torneo Nacional fica fora
_POR["1994"].trechos = [("uru94", 0, 322)]                                 # o "Relegation Playoff" é contra o Racing, da 2ª divisão
_POR["1948"].obs = "campeonato abandonado na 10ª rodada pela greve dos jogadores; sem campeão (RSSSF)"
_POR["1926"].obs = ("torneio de unificação depois da dissolução da FUF, com clubes das duas ligas (RSSSF); título não "
                    "reconhecido pela AUF: edição sem campeão (D-09)")
for _t in ("1923 FUF", "1924 FUF"):   # D-09: a AUF não reconhece os títulos da FUF; D-25 f: clubes da FUF à parte dos da AUF
    _POR[_t].obs += "; título não reconhecido pela AUF: edição sem campeão (D-09)"
    _POR[_t].nomes = {"Atlético Wanderers": "Atlético Wanderers", "Lito": "Lito (FUF)", "Charley": "Charley (FUF)"}
_POR["1947"].obs = (_POR["1947"].obs + "; " if _POR["1947"].obs else "") + "sem vice: o triangular pelo 2º lugar não terminou (D-22 c)"

EDICOES += [
    _e("2005", 2005, 2005, [("uru05", 0, None)], "Campeonato Uruguayo de Primera División 2005 – Torneo Uruguay Especial",
       obs="torneio de transição para o calendário europeu; o Defensor não jogou a final e o título ficou com o Nacional"),
]
for _a in range(2005, 2016):
    _p = f"uru{(_a + 1) % 100:02d}" if _a < 2009 else f"uru{_a + 1}"
    _tr = [(_p, 0, None)]
    if _a == 2005:
        _tr = [("uru06", 0, 522), ("uru06", 535, None)]   # promoção do fim de 2005 no meio da página
    EDICOES.append(_e(f"{_a}/{(_a + 1) % 100:02d}", _a, _a + 1, _tr, f"Campeonato Uruguayo de Primera División {_a}/{(_a + 1) % 100:02d}"))
EDICOES.append(_e("2016", 2016, 2016, [("uru2016a", 0, None)], "Campeonato Uruguayo de Primera División 2016 – Torneo de Transición",
                  obs="torneio de transição de volta ao calendário anual (turno único)"))
for _a in range(2017, 2026):
    EDICOES.append(_e(str(_a), _a, _a + 1 if _a == 2020 else _a, [(f"uru{_a}", 0, None)], f"Campeonato Uruguayo de Primera División {_a}",
                      obs="temporada esticada até abril de 2021 pela pandemia (a RSSSF chama de 2020/21)" if _a == 2020 else ""))
