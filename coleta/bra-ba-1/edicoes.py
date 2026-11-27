"""Edições do Campeonato Baiano (1ª divisão, `bra-ba-1`): temporadas, anos e nomes oficiais.

1905 a 2026, 122 edições (escopo aprovado pelo Guilherme em 27/11/2026; a conta da FBF, da RSSSF e da Wikipédia). Em 1915 e
1916 só entra o campeonato oficial (o da liga rival, a LSB, ninguém reconhece). Títulos divididos: 1938 (o cisma; Bahia e
Botafogo) e 1999 (Bahia e Vitória). Edições sem página da RSSSF e sem jogos no ogol entram só com campeão e vice
(SEM_JOGOS). Fontes da lista: RSSSF Brasil (tablesae/bacamp.htm) e Wikipédia ("Campeonato Baiano de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-ba-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1905, 2027)]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem página da RSSSF e sem jogos no ogol: entram só com campeão e vice (decisão do Guilherme, 25/11/2026)
SEM_JOGOS = {"1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934",
             "1935", "1938", "1961", "1962", "1963", "1969", "1970", "1971", "1974", "1982"}
# 1922-1935, 1970 e 1982: a lista da RSSSF Brasil tem o link, mas a página nunca foi criada (404 no site e nas cópias do
# Internet Archive, 27/11/2026); 1938: "ba1938c1"/"ba1938c2", também sem jogos ("o arquivo ainda não foi criado")


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Baiano"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesae/) de cada temporada."""
    return f"ba{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Baiano"
