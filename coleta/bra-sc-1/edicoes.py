"""Edições do Campeonato Catarinense (1ª divisão, `bra-sc-1`): temporadas, anos e nomes oficiais.

1924 a 2026, 102 edições (escopo aprovado pelo Guilherme em 27/11/2026). Fica fora 1946, que não foi disputado (a
federação estava suspensa pela CBD). 1924, 1925, 1926, 1934, 1935 e 1936 eram os campeonatos da capital, homologados como
estaduais pela FCF (RSSSF, página de 1935). 1933 não terminou: entra com os jogos e sem campeão. Em 1935 só entra o
campeonato da FCD (o da ACD, de Joinville, a FCF não reconhece). Fontes da lista: RSSSF Brasil (tablessz/sccamp.htm) e
Wikipédia ("Campeonato Catarinense de Futebol Masculino").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-sc-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

NAO_DISPUTADOS = {1946}
TEMPORADAS = [str(a) for a in range(1924, 2027) if a not in NAO_DISPUTADOS]
NAO_OFICIAIS: dict[str, str] = {}

# edições sem jogos: entram só com campeão e vice (decisão do Guilherme, 25/11/2026). A página só traz participantes,
# campeão e um ou outro jogo solto (que daria uma tabela errada); 1933 (não terminou) fica sem campeão e sem jogos
SEM_JOGOS = {"1925", "1926", "1928", "1933", "1934", "1943", "1945"}


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Catarinense"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablessz/) de cada temporada."""
    return f"sc{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Catarinense"
