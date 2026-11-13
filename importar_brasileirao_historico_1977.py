"""Importa jogos do Brasileiro 1977 (Copa Brasil, 62 clubes).

Primeira fase: seis grupos (A a F). Os 5 primeiros de cada grupo vao aos
grupos de vencedores da segunda fase (G a L); os demais, aos grupos de
perdedores (M a R), que tambem dao vagas a fase final. Fase final: quatro
grupos (S a V). Semifinais em ida e volta e final em jogo unico (Sao Paulo
campeao nos penaltis contra o Atletico-MG, em marco de 1978). Vitoria por
3 gols ou mais valia 3 pontos; as demais, 2.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, corrigir_placar, rodar

YEAR = 1977
SOURCE = "https://www.rsssf.org/tablesb/braz77.html"

CANONICAL["xv de novembro"] = "XV de Piracicaba"
CANONICAL["operario"] = "Operário-MS"  # Operario de Campo Grande
VIRADA = 7  # jogos de janeiro a junho sao de 1978

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 290),
    Fase("Segunda fase", "Winners Groups", "Losers Groups", "grupo", 60),
    Fase("Repescagem", "Losers Groups", "Final Phase", "grupo", 70),
    Fase("Fase final", "Final Phase", "Semifinals", "grupo", 60),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 1),
]


def AJUSTAR(games):
    # Desportiva x Fluminense-BA (grupo de perdedores): o Fluminense-BA
    # abandonou o jogo, subornado pela federacao baiana, para a Desportiva nao
    # tirar a vaga do Vitoria-BA. A RSSSF conta o jogo como 0-0. A CBD mandou
    # fazer um jogo extra Desportiva x Vitoria-BA; o Vitoria nao foi e a vaga
    # ficou com a Desportiva (jogo nao disputado, fora da base).
    return corrigir_placar(games, "Repescagem", "Desportiva-ES", "Fluminense-BA", 0, 0,
                           "Jogo abandonado pelo Fluminense-BA (suborno da federacao baiana); contado como 0-0, como na RSSSF.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=485, ajustar=AJUSTAR, virada=VIRADA)
