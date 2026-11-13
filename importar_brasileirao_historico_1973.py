"""Importa jogos do Brasileiro 1973 (3o Campeonato Nacional, 40 clubes).

Primeira fase em dois estagios (28 jogos por clube). Segunda fase: dois
grupos de 10 (turno unico), em janeiro e fevereiro de 1974. Quadrangular
final em turno unico (Palmeiras campeao). A pagina da RSSSF nao tem
"Final Table".
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1973
SOURCE = "https://www.rsssf.org/tablesb/braz73.html"
VIRADA = 7  # jogos de janeiro a junho sao de 1974

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "liga", 560),
    Fase("Segunda fase", "Second Phase", "Final Playoff", "grupo", 90),
    Fase("Quadrangular final", "Final Playoff", "", "grupo", 6),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=656, virada=VIRADA)
