"""Importa jogos do Brasileiro 1981 (Taca de Ouro, 44 clubes).

Primeira fase: quatro grupos de 10 (A a D), turno unico. Segunda fase: oito
grupos de 4 (E a L), com quatro clubes vindos da Taca de Prata (Nautico,
Bahia, Palmeiras e Uberaba). Oitavas, quartas, semifinais e final em ida e
volta (Gremio campeao contra o Sao Paulo).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1981
SOURCE = "https://www.rsssf.org/tablesb/braz81.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 180),
    Fase("Segunda fase", "Second Phase", "1/8 Finals", "grupo", 96),
    Fase("Oitavas de final", "1/8 Finals", "Quarterfinals", "mata_mata", 16, ida_volta=True),
    Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=306)
