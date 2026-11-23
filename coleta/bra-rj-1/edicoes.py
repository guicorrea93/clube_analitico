"""Edições do Campeonato Carioca (1ª divisão, `bra-rj-1`): temporadas, anos e nomes oficiais.

1906 a 2026. Até 1959 é o campeonato do Distrito Federal (a cidade do Rio de Janeiro); de 1960 a 1974, o do estado da
Guanabara; de 1975 em diante, o do novo estado do Rio de Janeiro (a fusão). O campeonato do antigo estado do Rio
(interior, "Campeonato Fluminense", rjflucamp.htm) é outra competição e fica de fora.

Nos anos de ligas rivais a federação reconhece os dois títulos, e cada torneio vira uma edição com temporada própria:
1912 (AFRJ e LMSA), 1924 (LMDT e AMEA), 1933 e 1934 (AMEA e LCF), 1935 e 1936 (FMD e LCF). Em 1937 a LFRJ (a liga
unificada) fica com a temporada "1937", e o torneio da FMD, que parou no meio com a pacificação, é a "1937 FMD": a FMD
proclamou o São Cristóvão campeão em 1937, e a FERJ homologou o título em dezembro de 2023. 1979 teve dois campeonatos: o normal e o "especial" (rj1979s.htm),
os dois reconhecidos. Fontes da lista: RSSSF Brasil (rjcamp.htm) e ogol (competição "campeonato-carioca/893").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bra-rj-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

LIGAS = {1912: ("AFRJ", "LMSA"), 1924: ("LMDT", "AMEA"), 1933: ("AMEA", "LCF"), 1934: ("AMEA", "LCF"),
         1935: ("FMD", "LCF"), 1936: ("FMD", "LCF"), 1937: ("", "FMD"),
         1979: ("", "Especial")}
TEMPORADAS = [f"{a} {l}".strip() for a in range(1906, 2027) for l in LIGAS.get(a, ("",))]


def ano_de(temporada: str) -> int:
    return int(temporada[:4])


def liga_de(temporada: str) -> str:
    return temporada[5:] if len(temporada) > 4 else ""


def nome_oficial(temporada: str) -> str:
    a, liga = ano_de(temporada), liga_de(temporada)
    if liga == "Especial":
        return "Campeonato Carioca Especial"
    if liga:
        return f"Campeonato Carioca ({liga})"
    return "Campeonato Carioca"


# página da RSSSF (tablesr/) e edição do ogol de cada temporada
def pagina_rsssf(temporada: str) -> str:
    return "rj1979s.htm" if temporada == "1979 Especial" else f"rj{ano_de(temporada)}.htm"


def slug_ogol(temporada: str) -> str:
    a, liga = ano_de(temporada), liga_de(temporada)
    if not liga or (a == 1912 and liga == "AFRJ"):
        return f"campeonato-carioca-{a}"
    return f"campeonato-carioca-{a}-{liga.lower()}"


# nomes que o importador comum espera
ANOS = TEMPORADAS
NOME_OFICIAL = {t: nome_oficial(t) for t in TEMPORADAS}
NOME_PADRAO = "Campeonato Carioca"
