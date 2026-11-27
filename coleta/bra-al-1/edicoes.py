"""Edições do Campeonato Alagoano (1ª divisão, `bra-al-1`): temporadas, anos e nomes oficiais.

1918 a 2026, 105 edições (escopo aprovado pelo Guilherme em 27/11/2026; a conta da FAF e da Wikipédia): os campeonatos da
Liga (1918-1926) foram reconhecidos pela CBF em 2026 (Resolução da Diretoria nº 01/2026; títulos do CRB). Ficam de fora
1931, 1932 e 1934 (suspensos), 1943 (não terminou; a FAF não conta) e o Torneio Centenário de 1922 (Santa Cruz de
Penedo, que a FAF não reconhece). Título dividido: 1953 (ASA e Ferroviário, lista da FAF). Edições sem página da RSSSF e
sem jogos no ogol entram só com campeão e vice (SEM_JOGOS). Fontes da lista: FAF, RSSSF Brasil (tablesae/alcamp.htm, que
começa em 1927) e Wikipédia ("Campeonato Alagoano de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-al-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1918, 2027) if a not in (1931, 1932, 1934, 1943)]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem página da RSSSF e sem jogos no ogol (que só tem jogos a partir de 1995): entram só com campeão e vice
# (decisão do Guilherme, 25/11/2026). 1918-1926: os jogos estão só no documento da FAF ("Campeonatos de Futebol das
# Ligas - 1918 a 1926", PDF escaneado)
SEM_JOGOS = {str(a) for a in [*range(1918, 1927), 1928, 1929, 1930, 1935, 1936, 1937, 1939, 1941, 1944, 1945, 1948, 1949,
                               1950, 1951, 1952, 1955, 1956, 1957, 1958, 1959, 1963, 1971, 1974, 1975, 1976, 1978, 1979,
                               1981, 1982, 1989,
                               # a página da RSSSF só traz a tabela final (sem os jogos)
                               1933, 1946, 1960, 1961, 1962, *range(1964, 1971),
                               # 1953: só a final por W.O., que não combina com o título dividido da FAF; 1990-1994: só
                               # umas rodadas soltas (o ogol só tem jogos a partir de 1995)
                               1953, *range(1990, 1995)]}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Alagoano"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesae/) de cada temporada."""
    return f"al{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Alagoano"
