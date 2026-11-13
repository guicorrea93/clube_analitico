"""Importa jogos do Brasileiro 1979 (Copa Brasil, 94 clubes).

Primeira fase: oito grupos (A a H); 14 clubes entram direto na segunda fase.
Segunda fase: sete grupos (I a O), com Palmeiras e Guarani de folga. Terceira
fase: quatro grupos de 4 (P a S), turno unico. Semifinais e final em ida e
volta (Internacional campeao invicto contra o Vasco).
"""
from importar_brasileirao_historico_base import Fase, corrigir_placar, rodar, trocar_clube

YEAR = 1979
SOURCE = "https://www.rsssf.org/tablesb/braz79.html"

FASES = [
    Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 359),
    Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 194),
    Fase("Terceira fase", "Third Phase", "Semifinal", "grupo", 24),
    Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 4, ida_volta=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
]


def AJUSTAR(games):
    # Jogos sem placar na fonte ficam 1-0 para quem recebeu os pontos (mesma
    # regra do importador de 1986). A RSSSF conta esses jogos sem gols, entao
    # os gols destes clubes ficam 1 acima da tabela dela.
    # Sao Paulo-RS x Operario-PR (grupo B): em campo 0-1, mas o Operario ficou
    # com 6 jogadores aos 85' e os pontos foram dados ao Sao Paulo-RS.
    games = corrigir_placar(games, "Primeira fase", "Sao Paulo-RS", "Operario-PR", 1, 0,
                            "Pontos dados ao Sao Paulo-RS no tribunal (Operario com 6 jogadores aos 85'); em campo, 0-1. Placar tratado como 1-0.")
    # Atletico-MG abandonou a terceira fase: W.O. para Goias e Internacional.
    games = corrigir_placar(games, "Terceira fase", "Goias", "Atletico-MG", 1, 0,
                            "Nao disputado: o Atletico-MG abandonou a terceira fase; pontos ao Goias. Placar tratado como 1-0.")
    games = corrigir_placar(games, "Terceira fase", "Atletico-MG", "Internacional-RS", 0, 1,
                            "Nao disputado: o Atletico-MG abandonou a terceira fase; pontos ao Internacional. Placar tratado como 0-1.")
    # Segunda fase: "Sao Paulo-RS 1-0 Goias" e do grupo do Goytacaz (o Goias
    # estava em outro grupo); erro de digitacao da fonte.
    return trocar_clube(games, "Segunda fase", "Sao Paulo-RS", "1-0", "Goias", "Goias", "Goytacaz",
                        "Na RSSSF aparece 'Goias'; o adversario do grupo era o Goytacaz.")


if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=583, ajustar=AJUSTAR)
