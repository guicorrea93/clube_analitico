"""Importa jogos do Brasileiro 1972 (2o Campeonato Nacional, 26 clubes).

Primeira fase: turno unico entre os 26 clubes, com a classificacao em quatro
grupos (A a D). Segunda fase: quatro grupos de 4 (turno unico). Semifinais e
final em jogo unico (0-0 com o Botafogo; Palmeiras campeao pela campanha).
A pagina da RSSSF nao tem "Final Table".
"""
from importar_brasileirao_historico_base import Fase, corrigir_placar, rodar

YEAR = 1972
SOURCE = "https://www.rsssf.org/tablesb/braz72.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "liga", 325),
    Fase("Segunda fase", "Second Phase", "Semifinals", "grupo", 24),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 2),
    Fase("Final", "\nFinal", "", "mata_mata", 1),
]


def AJUSTAR(games):
    # ABC 2-1 Botafogo: o ABC escalou tres jogadores irregulares e os pontos
    # foram dados ao Botafogo (a fonte nao marca "awd"). Gravado 0-1, como os
    # outros jogos decididos no tribunal sem placar atribuido.
    return corrigir_placar(games, "Primeira fase", "ABC", "Botafogo", 0, 1,
                           "Pontos dados ao Botafogo no tribunal (ABC com tres jogadores irregulares); em campo, 2-1 para o ABC. Placar tratado como 0-1.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=352, ajustar=AJUSTAR)
