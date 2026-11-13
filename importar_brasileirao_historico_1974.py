"""Importa jogos do Brasileiro 1974 (Campeonato Nacional, 40 clubes).

Primeira fase: dois grupos de 20 (A e B), turno unico. Fase semifinal:
quatro grupos (1 a 4). Fase final: quadrangular em turno unico com Cruzeiro,
Vasco, Santos e Internacional; Cruzeiro e Vasco empataram em pontos e
fizeram um jogo extra no Maracana (Vasco campeao, 2-1).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1974
SOURCE = "https://www.rsssf.org/tablesb/braz74.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Semifinal Phase", "grupo", 380),
    Fase("Fase semifinal", "Semifinal Phase", "Final Phase", "grupo", 60),
    Fase("Fase final", "Final Phase", "Final Match", "grupo", 6),
    Fase("Final", "Final Match", "", "mata_mata", 1),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=447)
