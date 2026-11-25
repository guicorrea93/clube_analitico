"""Edições do Campeonato Mineiro (1ª divisão, `bra-mg-1`): temporadas, anos e nomes oficiais.

1915 a 2026. Em 1932 houve duas ligas, e a federação reconhece os dois títulos: cada torneio vira uma edição com temporada
própria, "1932 LMDT" (Liga Mineira de Desportos Terrestres, campeão Atlético) e "1932 AMEG" (Associação Mineira de Esportes
Gerais, campeão Villa Nova). 1956 teve título dividido (Atlético e Cruzeiro). Em 2002 os clubes da Copa Sul-Minas (Atlético,
Cruzeiro e América) não jogaram o Mineiro; o campeão foi a Caldense. Fontes da lista: RSSSF Brasil (tablesfq/mgcamp.htm) e
ogol (competição "campeonato-mineiro").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-mg-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

LIGAS = {1932: ("LMDT", "AMEG")}
TEMPORADAS = [f"{a} {l}".strip() for a in range(1915, 2027) for l in LIGAS.get(a, ("",))]


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    liga = liga_de(temporada)
    return f"Campeonato Mineiro ({liga})" if liga else "Campeonato Mineiro"


# página da RSSSF (tablesfq/) de cada temporada: 1926 e 1932 têm a letra da liga no nome do arquivo
PAGINA_RSSSF = {"1926": "mg1926l.htm", "1932 LMDT": "mg1932l.htm", "1932 AMEG": "mg1932a.htm"}


def pagina_rsssf(temporada: str) -> str:
    return PAGINA_RSSSF.get(temporada, f"mg{ano_de(temporada)}.htm")


# edição do ogol nos anos de duas ligas (os dois aparecem como "1932" na lista; conferido pelo campeão de cada uma)
EDICAO_OGOL = {"1932 LMDT": 23251, "1932 AMEG": 150256}

# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Mineiro"
