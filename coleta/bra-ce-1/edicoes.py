"""Edições do Campeonato Cearense (1ª divisão, `bra-ce-1`): temporadas, anos e nomes oficiais.

1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 25/11/2026; a conta da FCF e da Wikipédia). Ficam fora 1913
(campeão desconhecido) e 1914 (Rio Branco: a FCF não reconhece e a RSSSF duvida que tenha existido). 1915-1919 são os
torneios da Liga Metropolitana, reconhecidos pela FCF em 2008 (Ato nº 11/2008). Edições sem jogos em nenhuma fonte entram
só com campeão e vice (SEM_JOGOS). 1992: título dividido entre quatro clubes. Fontes da lista: RSSSF Brasil
(tablesae/cecamp.htm) e Wikipédia ("Campeonato Cearense de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-ce-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1915, 2027)]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem jogos em nenhuma fonte (a página da RSSSF só traz participantes e campeão, ou não existe; o ogol e a
# Wikipédia não têm os jogos): entram só com campeão e vice (decisão do Guilherme, 25/11/2026)
SEM_JOGOS = {"1916", "1917", "1918", "1919", "1924", "1925", "1926", "1927", "1929", "1930", "1931", "1932", "1934", "1935",
             "1936", "1937", "1938"}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Torneio da Liga Metropolitana Cearense" if ano_de(temporada) <= 1919 else "Campeonato Cearense"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesae/) de cada temporada."""
    return f"ce{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Cearense"
