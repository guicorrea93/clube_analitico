"""Importa jogos do Brasileiro 1978 (Copa Brasil, 74 clubes).

Primeira fase: seis grupos (A a F). Os 6 primeiros de cada grupo vao a
segunda fase (grupos G a J); os demais disputam a repescagem (grupos K a P),
em paralelo, que devolve um clube. Terceira fase: quatro grupos (Q a T).
Quartas, semifinais e final em ida e volta (Guarani campeao contra o
Palmeiras). Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, corrigir_placar, renomear_clube, rodar, trocar_clube

YEAR = 1978
SOURCE = "https://www.rsssf.org/tablesb/braz78.html"

CANONICAL["xv de novembro"] = "XV de Piracicaba"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 420),
    Fase("Segunda fase", "Second Phase", "Respescagem", "grupo", 144),
    Fase("Repescagem", "Respescagem", "Third Phase", "grupo", 102),
    Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 112),
    Fase("Quartas de final", "Quarterfinals", "Semifinal", "mata_mata", 8, ida_volta=True),
    Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]


def AJUSTAR(games):
    # Operario de Campo Grande aparece como "-MT" (o Mato Grosso do Sul so
    # passou a valer em 1979); no banco e o Operario-MS.
    games = renomear_clube(games, "Operario-MT", "Operário-MS")
    # Quartas: "Internacional 1-0 1-2 Santa Cruz" - a volta veio do ponto de
    # vista do mandante. O Inter venceu por 2-1 em Recife e foi a semifinal;
    # a tabela final da RSSSF confirma.
    games = corrigir_placar(games, "Quartas de final", "Santa Cruz", "Internacional", 1, 2,
                            "Volta corrigida: a RSSSF escreve 1-2 do ponto de vista do mandante.")
    # Segunda fase: "Juventude 1-1 America-SP" esta no grupo do America-RJ.
    return trocar_clube(games, "Segunda fase", "Juventude", "1-1", "America-SP", "America-SP", "America-RJ",
                        "Na RSSSF aparece 'America-SP'; o adversario do grupo era o America-RJ.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=792, ajustar=AJUSTAR)
