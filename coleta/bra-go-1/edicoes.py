"""Edições do Campeonato Goiano (1ª divisão, `bra-go-1`): temporadas, anos e nomes oficiais.

1944 a 2026, 83 edições (escopo aprovado pelo Guilherme em 25/11/2026; a conta da FGF e da RSSSF). 1944-1962 é a era amadora
(o campeonato de Goiânia, que a FGF conta como Goiano); profissional desde 1963. Ficam fora os campeonatos de Goiânia de 1940
e 1943 e o "Campeonato Estadual de Goiás" amador (capital x interior), que a FGF não reconhece. Edições sem página da RSSSF e
sem jogos no ogol entram só com campeão e vice (SEM_JOGOS). Fontes da lista: RSSSF Brasil (tablesfq/gocamp.htm) e Wikipédia
("Campeonato Goiano de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-go-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

TEMPORADAS = [str(a) for a in range(1944, 2027)]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem página da RSSSF e sem jogos no ogol: entram só com campeão e vice (decisão do Guilherme, 25/11/2026); 1945 tem
# página, mas só com a tabela final, sem os jogos
SEM_JOGOS = {"1945", "1946", "1950", "1951", "1960", "1963", "1965", "1966"}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Goiano"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesfq/) de cada temporada."""
    return f"go{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Goiano"
