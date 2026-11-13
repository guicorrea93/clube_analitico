"""Importa jogos do Brasileiro 1975 (Copa Brasil, 42 clubes).

Primeira fase: grupos A e B (10 clubes cada, jogando contra o outro grupo)
e grupos C e D (11 clubes cada, tambem jogando contra o outro grupo). Segunda fase: grupos 1 e
2 (20 clubes, jogando contra o outro grupo) e repescagem nos grupos 3 a 6.
Terceira fase: dois grupos de 8. Semifinais e final em jogo unico
(Internacional campeao contra o Cruzeiro). Vitoria por 2 gols ou mais valia
3 pontos; as demais, 2. A pagina da RSSSF nao tem "Final Table": a tabela
final vem logo depois da frase do campeao.
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1975
SOURCE = "https://www.rsssf.org/tablesb/braz75.html"
CORTE_FINAL = "are the 1975 Brazilian champions"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 221),
    Fase("Segunda fase", "Groups 1 and 2", "Group 3", "grupo", 100),
    Fase("Repescagem", "Group 3", "Third Phase", "grupo", 50),
    Fase("Terceira fase", "Third Phase", "Semifinals", "grupo", 56),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 2),
    Fase("Final", "\nFinal", "", "mata_mata", 1),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=430, corte_final=CORTE_FINAL)
