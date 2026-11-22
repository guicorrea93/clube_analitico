"""Edições da 1ª divisão equatoriana (ecu-1): uma por título de campeão equatoriano, como na lista da RSSSF (ecuachamp.html).

1957 e 1960-2025: um campeão por ano (sem campeonato nacional em 1958 e 1959); 2005 deu dois títulos (Apertura e Clausura),
uma edição cada. Até 1967 o campeonato nacional era um torneio curto entre os melhores dos campeonatos regionais
(Interandino, de Quito e Ambato, e o de Guayaquil); os regionais são outras competições e ficam de fora. Apertura,
Clausura, liguillas, hexagonais e finais são fases da edição anual. Ficam de fora a Serie B e as divisões de baixo, a Copa
Ecuador e os playoffs da Copa Sudamericana e da Copa Conmebol.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). Todos os anos; de 1960 a 1974 parte das fases vem em tabela de confrontos
  (ler_rsssf.confrontos).
- espn: (início, fim) das datas dos jogos que a página não traz (2011, 2012 e 2025: a RSSSF só tem as tabelas e as finais).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "ecu-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^((Ecuador )?Serie B|Second Level|Third Level|Segunda Categor|Segunda Divisi|Copa Ecuador|Copa Sudamericana|Copa Credif|"
              r"Copa Conmebol|Supercopa|Hexagonal de Ascenso|Campeonato Profesional (Interandino|de Guayaquil)|Campeonato del Guayas|"
              r"About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1957", "2005 Apertura"
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
    # fases dos jogos da ESPN: [(a partir da data, fase)]; fase "*": a da tabela da página que tem os dois clubes
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""                                           # o que falta nos jogos (entra na observação)

    @property
    def pontos_vitoria(self) -> int:
        """2 por vitória até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _nome(a: int) -> str:
    if a <= 1970:
        return f"Campeonato Ecuatoriano de Fútbol {a}"
    if a <= 2017:
        return f"Campeonato Ecuatoriano de Fútbol Serie A {a}"
    return f"LigaPro Serie A {a}"


# trechos explícitos: a página tem duas edições
_TRECHOS: dict[str, list[tuple[str, int, int | None]]] = {
    "2005 Apertura": [("ecua05", 20, 409)],
    "2005 Clausura": [("ecua05", 410, 862)],
    "2025": [("ecua2025", 0, 90)],          # a página só tem as tabelas; a Copa Ecuador vem depois
}
# fases que a página só marca no título de cada bloco
_FASES_ANO: dict[int, list[tuple[str, str]]] = {
    1993: [(r"^Playoff for second place to Conmebol", "Triangular do 2º lugar")],   # triangular com rodadas
    1998: [(r"^Hexagonal [12]$", "")],   # os hexagonais são os dois grupos do Clausura
}
# jogos que a página não traz: vêm da ESPN, das datas (início, fim)
# (até antes dos jogos finais que a página traz: 2011 e 2012 têm as finais e os jogos pelo 2º e pelo 4º lugar)
_ESPN = {2011: ("2011-01-01", "2011-12-05"), 2012: ("2012-01-01", "2012-12-05"), 2025: ("2025-01-01", "2025-12-31")}
# 1ª etapa até o intervalo do meio do ano; 2ª etapa (ou a fase de playoffs de 2025) depois dele
_ESPN_FASES = {2011: [("2011-07-01", "Segunda fase")], 2012: [("2012-07-10", "Segunda fase")], 2025: [("2025-10-01", "*")]}
# jogos que faltam nas fontes (entra na observação da edição)
_INCOMPLETA: dict[int, str] = {}

EDICOES: list[Edicao] = []
for _a in [1957, *range(1960, 2026)]:
    _pg = f"ecua{_a % 100:02d}" if _a < 2010 else f"ecua{_a}"
    _kw = dict(incompleta=_INCOMPLETA.get(_a, ""), fases=list(_FASES_ANO.get(_a, [])), espn=_ESPN.get(_a),
               espn_fases=list(_ESPN_FASES.get(_a, [])))
    if _a == 2005:
        for _t in ("Apertura", "Clausura"):
            EDICOES.append(_e(f"2005 {_t}", 2005, 2005, _TRECHOS[f"2005 {_t}"], f"{_nome(2005)} – {_t}", **_kw))
        continue
    EDICOES.append(_e(str(_a), _a, _a, _TRECHOS.get(str(_a), [(_pg, 0, None)]), _nome(_a), **_kw))
