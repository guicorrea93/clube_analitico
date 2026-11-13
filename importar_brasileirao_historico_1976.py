"""Importa jogos do Brasileiro 1976 (Copa Brasil, 54 clubes).

Primeira fase: seis grupos (A a F). Os 4 primeiros de cada grupo vao a
segunda fase (grupos G a J); os demais, a repescagem (grupos K a P), que
tambem da vagas a terceira fase. Terceira fase: dois grupos (Q e R).
Semifinais e final em jogo unico (Internacional campeao contra o
Corinthians). Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1976
SOURCE = "https://www.rsssf.org/tablesb/braz76.html"

CANONICAL["operario"] = "Operário-MS"  # Operario de Campo Grande

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 216),
    Fase("Segunda fase", "Second Phase", "Group K", "grupo", 60),
    Fase("Repescagem", "Group K", "Third Phase", "grupo", 60),
    Fase("Terceira fase", "Third Phase", "Semifinal", "grupo", 72),
    Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 2),
    Fase("Final", "\nFinal", "", "mata_mata", 1),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=411)
