"""Edições da 1ª divisão peruana (per-1): uma por título de campeão peruano, como na lista da RSSSF (peruchamp.html).

1912-1921: Liga Peruana de Football (antes da Federação, de 1922). A RSSSF lista os campeões à parte e não os soma aos
títulos nacionais; a Wikipédia os conta. Entram como edições só com o campeão (nenhuma fonte tem tabela ou jogos completos).
1926-2025: um campeão por ano (sem campeonato oficial em 1936). Apertura, Clausura, Torneo de Verano, liguillas e finais são
fases da edição anual. Ficam de fora a Copa Perú e a Segunda División, as ligas de reservas (que davam pontos de bônus de
1931 a 1934), o Intermedio, o Torneo del Inca, a Copa Bicentenario, as liguillas pré-Libertadores e os jogos de promoção
contra clubes de baixo.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). 1930-1942, 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984 e 1986 em diante.
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1926-1929, 1943-1967, 1982 e 1985.
- sem jogos: 1912-1921, 1970-1974, 1976, 1977 e 1979 (nenhuma fonte pública traz os jogos; pesquisa no relatório). Entram
  com a tabela final da RSSSF (peruhist.html), quando há.
- tabelas: trechos lidos só pelas tabelas (a conferência): a seção do ano em peruhist.html nos anos sem página da RSSSF.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "per-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Reserve League|Promotion Liguilla|Promotion Playoff|Promotion/Relegation|Playoff for Promotion|"
              r"Playoff against (Eleventh|11th)|Divisi[oó]n Intermedia|Intermedia(ry|te)? (Division|Tournament)|"
              r"Intermedio Tournament|Second Division|Segunda Divisi|Second Level|Copa Per[uú]|Liguilla Pre|Liguilla Playoffs|"
              r"Playoff for Liguilla|Preliguilla|Cuadrangular/Triangular|Copa Sudamericana|Third Copa Libertadores|"
              r"Copa Libertadores \d{4} Playoff|Playoff for Copa|Copa Conmebol|Tournament Unofficial|Zonal Tournament|Supercopa|"
              r"Copa Bicentenario|Torneo Intermedio|Copa Federaci|Liga de Arequipa|Liga Distrital|Torneo Promoci|Arequipa \d{4}|"
              r"Relegation Final Table|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1950", "2003"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: str | None = None                                       # ano da página da Wikipédia em espanhol com os jogos
    hist: str = ""                                                # (não usado)
    ogol: int | None = None                                       # (não usado: o ogol não tem o Peru)
    espn: tuple[str, str] | None = None                           # (não usado)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""                                           # o que falta nos jogos (entra na observação)

    @property
    def pontos_vitoria(self) -> int:
        """3-2-1 de 1931 a 1942 (vitória, empate, derrota); 2 por vitória até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None


@lru_cache(maxsize=None)
def secao_hist(ano: int) -> tuple[str, int, int] | None:
    """(página, início, fim) da seção do ano em peruhist.html (título = o ano sozinho na linha)."""
    sys.path.insert(0, str(RAIZ / "coleta" / "comum-sulamerica"))
    import rsssf_sul
    ls = rsssf_sul.texto(PASTA_DADOS / "rsssf" / "peruhist.html")
    ini = next((i for i, l in enumerate(ls) if l.strip() == str(ano)), None)
    if ini is None:
        return None
    fim = next((i for i in range(ini + 1, len(ls)) if re.fullmatch(r"\d{4}(-\d{4} missing)?|About this document", ls[i].strip())),
               len(ls))
    return "peruhist", ini, fim


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


_SEM_JOGOS = "sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)"
_WIKI = {*range(1926, 1930), *range(1943, 1968), 1982, 1985}
_RSSSF = {*range(1930, 1943), 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984, *range(1986, 2026)} - {1936}
# trechos explícitos: a página tem outra competição no meio ou antes do campeonato
_TRECHOS: dict[int, list[tuple[str, int, int | None]]] = {
    2003: [("peru03", 12, 404), ("peru03", 418, 748)],   # playoff da Sudamericana entre o Apertura e o Clausura
    2014: [("peru2014", 442, None)],                      # o Torneo del Inca (copa) abre a página
    2015: [("peru2015", 364, None)],
    2019: [("peru2019", 23, 495), ("peru2019", 802, None)],   # a Copa Bicentenario entre o Apertura e o Clausura
    1969: [("peru69", 52, 359)],                          # o resumo do topo repete as tabelas das liguillas
    2021: [("peru2021", 0, 816), ("peru2021", 830, 845)],  # PE-005: a final, depois do playoff de promoção/rebaixamento
}
# fases marcadas no título da rodada ("Round 1 (Liguilla Final)")
_FASES_ANO: dict[int, list[tuple[str, str]]] = {
    1969: [(r"^Round \d+ \(Liguilla Final\)", "Fase final"), (r"^Round \d+ \(Liguilla No Descenso\)", "Grupo do rebaixamento")],
    1987: [(r"^Regional Final", "Final do Regional")],   # PE-011: a liguilla final do Regional, à parte da Zona Sul
    1988: [(r"^Regional Final", "Final do Regional")],
}
# jogos que faltam nas fontes (entra na observação da edição)
_INCOMPLETA = {
    1926: "a Wikipédia traz parte dos jogos (o torneio foi suspenso em novembro e a tabela publicada é a da suspensão)",
    1982: "a Wikipédia não traz todos os jogos da fase final",
    1984: "a RSSSF traz os jogos do Descentralizado; do Torneo Regional, só as tabelas",
    1986: "a RSSSF traz parte dos jogos (Regional só com tabelas)",
    1989: "a RSSSF traz parte dos jogos (página em construção)",
    1990: "a RSSSF traz só as tabelas da maior parte das fases e os jogos finais",
    1991: "a RSSSF traz só as tabelas da maior parte das fases e os jogos finais",
    1988: "os jogos do Descentralizado \"B\" (cujo vencedor entrava no grupo final) estão em tabela de confrontos sem datas e "
          "não foram lidos",
    2003: "a RSSSF não traz as rodadas 16 e 17 do Clausura",
}

EDICOES: list[Edicao] = []
for _a in range(1912, 1922):
    EDICOES.append(_e(str(_a), _a, _a, [], f"Liga Peruana de Football {_a}",
                      obs="sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma "
                          "fonte pública traz os jogos nem a tabela, só o campeão"))
for _a in range(1926, 2026):
    if _a == 1936:   # sem campeonato oficial (a seleção foi aos Jogos Olímpicos de Berlim)
        continue
    if _a <= 1950:
        _nome = f"Campeonato de Primera División del Perú {_a}"
    elif _a <= 1965:
        _nome = f"Campeonato Profesional del Perú {_a}"
    elif _a <= 2018:
        _nome = f"Campeonato Descentralizado {_a}"
    else:
        _nome = f"Liga 1 {_a}"
    _pg = f"peru{_a % 100:02d}" if _a < 2010 else f"peru{_a}"
    _hist = [secao_hist(_a)] if secao_hist(_a) else []
    if _a in _WIKI:
        EDICOES.append(_e(str(_a), _a, _a, [], _nome, wiki=str(_a), tabelas=_hist, incompleta=_INCOMPLETA.get(_a, "")))
    elif _a in _RSSSF:
        EDICOES.append(_e(str(_a), _a, _a, _TRECHOS.get(_a, [(_pg, 0, None)]), _nome, incompleta=_INCOMPLETA.get(_a, ""),
                          fases=list(_FASES_ANO.get(_a, []))))
    else:
        EDICOES.append(_e(str(_a), _a, _a, [], _nome, tabelas=_hist, obs=_SEM_JOGOS))
