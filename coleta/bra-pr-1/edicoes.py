"""Edições do Campeonato Paranaense (1ª divisão, `bra-pr-1`): temporadas, anos e nomes oficiais.

1915 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). Todos os anos foram disputados. 1980 teve título dividido
(Colorado e Cascavel). Em 2002 houve dois torneios: o campeonato oficial da FPF, sem os clubes da Copa Sul-Minas
(temporada "2002", campeão o Iraty), e o Supercampeonato, com eles ("2002 Supercampeonato", campeão o Atlético), que entra
como edição não oficial (o Athletico conta o título). Fontes da lista: RSSSF Brasil (tablesfq/prcamp.htm) e ogol
(competições "campeonato-paranaense" e "supercampeonato-paranaense").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-pr-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

SUPER = "2002 Supercampeonato"
TEMPORADAS = [t for a in range(1915, 2027) for t in ((str(a), SUPER) if a == 2002 else (str(a),))]
NAO_OFICIAIS = {SUPER: "Supercampeonato Paranaense de 2002, com os clubes da Copa Sul-Minas (que não jogaram o campeonato da FPF); "
                       "o Athletico conta o título, mas a lista oficial da FPF não foi achada (escopo aprovado em 25/11/2026)"}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Supercampeonato Paranaense" if temporada == SUPER else "Campeonato Paranaense"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesfq/) de cada temporada; o Supercampeonato de 2002 tem a sua."""
    return "pr2002sc.htm" if temporada == SUPER else f"pr{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão: o Supercampeonato é outra competição no ogol
EDICAO_OGOL: dict[str, int] = {SUPER: 119188}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Paranaense"
