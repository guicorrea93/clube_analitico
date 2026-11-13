"""Importa jogos do Brasileiro 1971 (1o Campeonato Nacional, 20 clubes).

Primeira fase: turno unico entre os 20 clubes, com a classificacao em dois
grupos (A e B). Segunda fase: tres grupos de 4 (turno e returno). Triangular
final em turno unico (Atletico-MG campeao, sobre Sao Paulo e Botafogo).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1971
SOURCE = "https://www.rsssf.org/tablesb/braz71.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "liga", 190),
    Fase("Segunda fase", "Second Phase", "Final Playoff", "grupo", 36),
    Fase("Triangular final", "Final Playoff", "", "grupo", 3),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=229)
