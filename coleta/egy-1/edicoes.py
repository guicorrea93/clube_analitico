"""Edições da 1ª divisão egípcia (egy-1): a liga nacional, de 1948/49 (a primeira, criada por decreto real) a 2025/26.

Lista de campeões: RSSSF (egychamp.html, 67 títulos desde 1948/49), conferida com a Wikipédia em inglês. Ficam de fora
(pesquisa de 23/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md):
- o campeonato da U.I.S.S.E. (1912/13 a 1914): mata-mata entre clubes das colônias estrangeiras, que a federação
  egípcia (1921) não reconhece;
- a Liga do Cairo (1922/23 a 1957/58) e as outras ligas regionais (Alexandria, Canal, Bahary);
- as temporadas não disputadas: 1951/52 (Olimpíada de 1952) e 1967/68 a 1970/71 (Guerra dos Seis Dias).
As temporadas começadas e não terminadas entram como edição sem campeão, com o motivo na observação: 1954/55, 1971/72,
1973/74, 1989/90, 2011/12 e 2012/13. A RSSSF chama de 1970/71 a temporada interrompida pela briga em Al-Ahly x Zamalek;
o jogo foi em 24/12/1971 (Kooora; Wikipédia em inglês): é a 1971/72. A 2012/13 é a "2013" da RSSSF (começou em
fevereiro de 2013).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_africa.texto); linha final
  None: até o primeiro título de outra competição (FIM_PADRAO). Página egyAA (ou egyAAAA de 2010 em diante): a do ano em
  que a temporada termina (egy98 = 1997/98).
- ogol: os anos em que a RSSSF só tem a tabela final (1964/65 a 1996/97, 2010/11, 2011/12 e 2025/26): o calendário do
  ogol é a base (ogol_jogos), e as tabelas da página (tabelas) são a conferência.
- tabelas: trechos lidos só pelas tabelas (sem jogos).
Antes de 1964/65, a RSSSF só tem a tabela final (e, em alguns anos, só os resultados do Al-Ahly, sem data nem mando:
ficam de fora, como os "Known Results" do par-1) e o ogol não tem jogos: a edição entra com a tabela.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "egy-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^((Egypt(ian)? )?(Super |League )?Cup\b|Egypt Super ?Cup|Second Level|Second Division|Third Level|Cairo League|"
              r"Topscorers?:|list of champions|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1948/49"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""             # como está em egychamp.html ("" = o da lista pela temporada)
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, nome da fase), além do padrão
    nomes: dict[str, str] = field(default_factory=dict)          # grafia -> clube, quando a regra geral erra nesta edição
    soma_de: list[str] = field(default_factory=list)              # (não usado; mantido para o código comum)
    wiki: int | None = None             # (não usado)
    hist: str = ""                      # (não usado)
    ogol: int | None = None             # ano_inicio do calendário do ogol que é a base dos jogos
    espn: tuple[str, str] | None = None  # (não usado: a ESPN não tem a liga egípcia)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas (sem jogos)
    cancelada: str = ""                 # motivo, quando a temporada não terminou (edição sem campeão)
    incompleta: str = ""                # o que falta nos jogos (entra no formato e na observação)

    @property
    def pontos_vitoria(self) -> int:
        """Como as tabelas da RSSSF contam: 2 pontos até 1985/86; 3 de 1986/87 a 1989/90; de novo 2 de 1990/91 a
        1993/94; 3 a partir de 1994/95."""
        return 3 if self.ano_inicio >= 1994 or 1986 <= self.ano_inicio <= 1989 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.ogol is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def pagina(ano_fim: int) -> str:
    return f"egy{ano_fim % 100:02d}" if ano_fim < 2010 else f"egy{ano_fim}"


def _temp(a: int) -> str:
    return f"{a}/{(a + 1) % 100:02d}"


NOME = "Egyptian Premier League"
_NAO_DISPUTADAS = {1951, 1967, 1968, 1969, 1970}
CANCELADAS = {
    1954: "temporada não terminada: o Al-Ahly brigou com a federação e saiu do campeonato; nenhum título foi dado",
    1971: "temporada não terminada: suspensa depois da briga e da invasão de campo em Al-Ahly x Zamalek (24/12/1971); "
          "nenhum título foi dado (a RSSSF chama esta temporada de 1970/71)",
    1973: "temporada não terminada: suspensa pela Guerra do Yom Kippur (outubro de 1973); no lugar dela houve a Copa "
          "Outubro, que não conta como título da liga",
    1989: "temporada não terminada: suspensa para a preparação da seleção para a Copa do Mundo de 1990; nenhum título foi dado",
    2011: "temporada abandonada em fevereiro de 2012, depois da tragédia do estádio de Port Said; nenhum título foi dado",
    2012: "temporada abandonada em julho de 2013 pela crise política; nenhum título foi dado (a RSSSF chama de 2013)",
}
# anos em que a RSSSF só tem a tabela final e o ogol tem os jogos
_OGOL = set(range(1964, 1997)) | {2010, 2011, 2025}
_SO_TABELA_OGOL_VAZIO = {1975}   # o ogol tem só 1 jogo; a RSSSF traz as tabelas dos grupos e a final

EDICOES: list[Edicao] = []
for _a in range(1948, 2026):
    if _a in _NAO_DISPUTADAS:
        continue
    _t = _temp(_a)
    _pg = pagina(_a + 1)
    if _a in (1954, 1971, 1973):   # não terminadas e sem nenhuma fonte de jogos ou tabela
        EDICOES.append(_e(_t, _a, _a + 1, [], NOME, cancelada=CANCELADAS[_a]))
        continue
    if _a == 1989:   # não terminada: a RSSSF não tem página; o ogol tem os jogos disputados
        EDICOES.append(_e(_t, _a, _a + 1, [], NOME, ogol=_a, cancelada=CANCELADAS[_a]))
        continue
    if _a == 2012:   # a página "egy2013" da RSSSF (temporada 2013)
        EDICOES.append(_e(_t, _a, _a + 1, [("egy2013", 0, None)], NOME, cancelada=CANCELADAS[_a]))
        continue
    if _a == 2011:   # abandonada: a RSSSF só tem a tabela no abandono; o ogol tem os jogos
        EDICOES.append(_e(_t, _a, _a + 1, [], NOME, ogol=_a, tabelas=[(_pg, 0, None)], cancelada=CANCELADAS[_a]))
        continue
    if _a < 1964 or _a in _SO_TABELA_OGOL_VAZIO:
        EDICOES.append(_e(_t, _a, _a + 1, [], NOME, tabelas=[(_pg, 0, None)]))
        continue
    if _a in _OGOL:
        EDICOES.append(_e(_t, _a, _a + 1, [], NOME, ogol=_a, tabelas=[(_pg, 0, None)],
                          obs="a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol"))
        continue
    EDICOES.append(_e(_t, _a, _a + 1, [(_pg, 0, None)], NOME))

_POR = {e.temporada: e for e in EDICOES}

# anos de só tabela em que a página da RSSSF traz também alguns jogos: entram, e a edição fica com "jogos incompletos"
_PARCIAIS = {
    "1948/49": ("jogos incompletos (só 6 jogos da liga e o desempate do 2º lugar)",
                [(r"^Second Place Match", "Desempate do 2º lugar")]),
    "1957/58": ("jogos incompletos (só a final entre os vencedores dos grupos)",
                [(r"^Championship Playoff", "Final")]),
    "1962/63": ("jogos incompletos (só o desempate do grupo B e o quadrangular final)", []),
    "1963/64": ("jogos incompletos (só a final entre os vencedores dos grupos)",
                [(r"^Championship Playoff", "Final")]),
    "1975/76": ("jogos incompletos (só a final entre os vencedores dos grupos)",
                [(r"^Championship Playoff", "Final")]),
}
# 2024/25: 1ª fase em turno único, depois "Championship Playoff" e "Relegation Playoff" são grupos (com tabela e rodadas)
_POR["2024/25"].fases = [(r"^Relegation Playoff$", "Grupo do rebaixamento"), (r"^Championship Playoff$", "Fase final"),
                         (r"^Regular Stage$", "")]
_POR["2025/26"].fases = list(_POR["2024/25"].fases)

# 2011/12: o ogol chama o Telephonat Beni Suef de "Bani Ebeid" (a tabela da RSSSF e a da Wikipédia trazem o Telephonat, e
# não o Beni Ebeid)
_POR["2011/12"].nomes = {"Bani Ebeid": "Telephonat Beni Suef"}

# 2008/09: Al-Ahly e Ismaily empataram em pontos; "Championship Playoff" é um jogo só
_POR["2008/09"].fases = [(r"^Championship Playoff", "Desempate do título")]

# a Copa do Egito vem logo depois da liga, sem título ("Preliminary Round")
_POR["2004/05"].trechos = [("egy05", 0, 510)]

for _t, (_inc, _fs) in _PARCIAIS.items():
    _POR[_t].trechos, _POR[_t].tabelas = _POR[_t].tabelas, []
    _POR[_t].incompleta, _POR[_t].fases = _inc, _fs
