"""Edições do Campeonato Gaúcho (1ª divisão, `bra-rs-1`): temporadas, anos e nomes oficiais.

1919 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). Ficam fora 1918, 1923 e 1924, que não foram disputados (a
Revolução de 1923; o ogol marca 1923 e 1924 como "Não Disputada"). Até 1960 o campeonato era por regiões: os campeões das
cidades disputavam os regionais, e os campeões regionais, a fase estadual; entram a fase estadual e as decisões de zona e
região que a página da RSSSF traz, não os campeonatos das cidades. 1930 foi organizado pela FAGET, no lugar da FRGD.
Fontes da lista: RSSSF Brasil (tablesr/rscamp.htm) e ogol (competição "campeonato-gaucho").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-rs-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

NAO_DISPUTADOS = {1918, 1923, 1924}
TEMPORADAS = [str(a) for a in range(1919, 2027) if a not in NAO_DISPUTADOS]


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    return "Campeonato Gaúcho"


def pagina_rsssf(temporada: str) -> str:
    """Página da RSSSF (tablesr/) de cada temporada."""
    return f"rs{ano_de(temporada)}.htm"


# edição do ogol escolhida à mão (nenhuma por ora: uma edição por ano)
EDICAO_OGOL: dict[str, int] = {}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Gaúcho"
