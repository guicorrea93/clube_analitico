"""Importa jogos do Brasileiro 1980 (Taca de Ouro, 44 clubes).

Primeira fase: quatro grupos de 10 (A a D), turno unico. Segunda fase: oito
grupos de 4 (E a L), com quatro clubes vindos da Taca de Prata (America-SP,
Americano, Bangu e Sport). Terceira fase: quatro grupos de 4 (M a P), turno
unico. Semifinais e final em ida e volta (Flamengo campeao contra o
Atletico-MG, pela melhor campanha na semifinal).
"""
from importar_brasileirao_historico_base import Fase, rodar, separar_jogo

YEAR = 1980
SOURCE = "https://www.rsssf.org/tablesb/braz80.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 180),
    Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 97),
    Fase("Terceira fase", "Third Phase", "Semifinals", "grupo", 24),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]


def AJUSTAR(games):
    # O desempate Guarani 3-2 America-RJ (2o lugar do grupo I) esta no meio
    # da segunda fase; separado para nao entrar na tabela do grupo. A RSSSF
    # tambem nao o soma na tabela final.
    return separar_jogo(games, "Segunda fase", "Guarani", "3-2", "America-RJ", "Desempate",
                        "Desempate pelo 2o lugar do grupo I da segunda fase.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=307, ajustar=AJUSTAR)
