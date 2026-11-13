"""Importa jogos do Robertao 1970 (Torneio Roberto Gomes Pedrosa, 17 clubes).

Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010).
Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
grupos (A e B); os 2 primeiros de cada grupo vao a fase final. Fase final:
quadrangular em turno unico (Fluminense campeao).

Fonte: RSSSF Brasil. A lista de jogos da RSSSF (braz70.html) tem placares que
nao fecham com a tabela dela mesma (ex.: Sao Paulo 1-0 Palmeiras, que no RSSSF
Brasil e 0-2, com os autores dos gols); a do RSSSF Brasil fecha.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1970
EDICAO = "1970"
SOURCE = "https://rsssfbrasil.com/tablesr/rgp1970.htm"
ARQUIVO = "rsssfbrasil_rgp1970.htm"

CANONICAL["america"] = "America-RJ"  # a fonte escreve so "America"

FASES = [
    Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
    Fase("Fase final", "Final Phase", "", "grupo", 6),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=142, arquivo=ARQUIVO, edicao=EDICAO)
