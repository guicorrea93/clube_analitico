"""Importa jogos do Brasileiro 1983 (Taca de Ouro, 44 clubes).

Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
colocados disputam o playoff (jogo unico, fora da tabela final da RSSSF);
os quintos e os eliminados no playoff vao para a Taca de Prata. Quatro clubes
da Taca de Prata (Americano, Botafogo-SP, Guarani e Uberaba) entram na
segunda fase: oito grupos de 4 (I a P). Terceira fase: quatro grupos de 4.
Quartas, semifinais e final em ida e volta (Flamengo campeao contra o Santos).
A Taca de Prata, no fim da pagina, fica de fora.
"""
from importar_brasileirao_historico_base import Fase, corrigir_placar, rodar

YEAR = 1983
SOURCE = "https://www.rsssf.org/tablesb/braz83.html"

FASES = [
    Fase("Primeira fase", "First Phase", "\nPlayoff\n", "grupo", 160),
    Fase("Playoff", "\nPlayoff\n", "Second Phase", "mata_mata", 4),
    Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 96),
    Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 48),
    Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
    Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]


def AJUSTAR(games):
    # "Atletico-PR 2-1 0-1 Sao Paulo": a volta veio do ponto de vista do
    # mandante. O Athletico venceu por 1-0 no Morumbi (gol de Assis) e foi a
    # semifinal; a tabela final da propria RSSSF (11 V, 32-28) confirma.
    return corrigir_placar(games, "Quartas de final", "Sao Paulo", "Atletico-PR", 0, 1,
                           "Volta corrigida: a RSSSF escreve 0-1 do ponto de vista do mandante.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=322, ajustar=AJUSTAR)
