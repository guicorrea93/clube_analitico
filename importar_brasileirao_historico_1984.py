"""Importa jogos do Brasileiro 1984 (Copa Brasil, 41 clubes).

Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
colocados disputam a repescagem (jogo unico, fora da tabela final da RSSSF).
Segunda fase: sete grupos de 4 (I a O). Terceira fase: quatro grupos de 4,
com o Uberlandia vindo da Taca CBF. Quartas, semifinais e final em ida e
volta (Fluminense campeao contra o Vasco).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1984
SOURCE = "https://www.rsssf.org/tablesb/braz84.html"

FASES = [
    Fase("Primeira fase", "First Phase", "\nRepescagem\n", "grupo", 160),
    Fase("Repescagem", "\nRepescagem\n", "Second Phase", "mata_mata", 4),
    Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 84),
    Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 48),
    Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=310)
