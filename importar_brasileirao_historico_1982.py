"""Importa jogos do Brasileiro 1982 (Taca de Ouro, 44 clubes).

Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
colocados disputam a repescagem (jogo unico, fora da tabela final da RSSSF).
Segunda fase: oito grupos de 4 (J a Q), com quatro clubes vindos da Taca de
Prata (America-RJ, Athletico-PR, Corinthians e Sao Paulo-RS). Terceira e
quarta fases, semifinais em ida e volta e final em melhor de 3 (Flamengo
campeao no terceiro jogo, contra o Gremio).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1982
SOURCE = "https://www.rsssf.org/tablesb/braz82.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Playoff (Repescagem)", "grupo", 160),
    Fase("Repescagem", "Playoff (Repescagem)", "Second Phase", "mata_mata", 4),
    Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 96),
    Fase("Terceira fase", "Third Phase", "Fourth Phase", "mata_mata", 16, ida_volta=True),
    Fase("Quarta fase", "Fourth Phase", "Semifinals", "mata_mata", 8, ida_volta=True),
    Fase("Semifinal", "Semifinals", "\nFinals", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinals", "", "mata_mata", 3),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=291)
