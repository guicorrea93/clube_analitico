"""Edições do Campeonato Pernambucano (1ª divisão, `bra-pe-1`): temporadas, anos e nomes oficiais.

1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 27/11/2026; a conta da FPF, da RSSSF e da Wikipédia). Nenhum
título dividido. A edição 2026/27 (Turno Forró em 2026, Turno Frevo em 2027) fica de fora até terminar. Edições sem página
da RSSSF e sem jogos no ogol entram só com campeão e vice (SEM_JOGOS). Fontes da lista: RSSSF Brasil (tablesfq/pecamp.htm)
e Wikipédia ("Campeonato Pernambucano de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-pe-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1915, 2027)]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem página da RSSSF e sem jogos no ogol: entram só com campeão e vice (decisão do Guilherme, 25/11/2026).
# 1992-1993: a RSSSF Brasil nunca teve a página (404 no site e no Internet Archive) e o ogol não tem os jogos. 1991 também
# não tem página, mas o ogol tem a final (Sport x Náutico, 2 jogos): entra com ela
SEM_JOGOS = {"1992", "1993"}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Pernambucano"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesfq/) de cada temporada."""
    return f"pe{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão: em 2026 o ogol tem duas com o rótulo "2026"; a 225812 é a 2026/27 (Turno Forró)
EDICAO_OGOL: dict[str, int] = {"2026": 210257}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Pernambucano"
