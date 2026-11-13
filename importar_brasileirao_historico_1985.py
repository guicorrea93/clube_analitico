"""Importa jogos do Brasileiro 1985 (Copa Brasil, 44 clubes).

Primeira fase: grupos A e B (10 clubes cada, jogando contra o outro grupo nos
dois estagios) e grupos C e D (12 clubes cada, turno e returno no proprio
grupo). Segunda fase: quatro quadrangulares (E a H). Semifinais em ida e
volta e final em jogo unico (Coritiba campeao nos penaltis contra o Bangu).
A Taca CBF (2a divisao), no fim da pagina, fica de fora.
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1985
SOURCE = "https://www.rsssf.org/tablesb/braz85.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 464),
    Fase("Segunda fase", "Second Phase", "Semifinals", "grupo", 48),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 1),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=517)
