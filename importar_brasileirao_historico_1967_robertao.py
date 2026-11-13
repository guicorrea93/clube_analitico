"""Importa jogos do Robertao 1967 (Torneio Roberto Gomes Pedrosa, 15 clubes).

Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1967
houve tambem a Taca Brasil (edicao 1967_taca_brasil).
Primeira fase: turno unico entre os 15 clubes, com a classificacao em dois
grupos (A e B); os 2 primeiros de cada grupo vao ao quadrangular final, em
turno e returno (Palmeiras campeao).

Fonte: RSSSF Brasil, em portugues e em varios blocos <pre>: le os blocos 0
(primeira fase) e 2 (quadrangular). O bloco 3 ("Title match") repete o jogo
decisivo Palmeiras 2 x 1 Gremio e fica de fora.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1967
EDICAO = "1967_robertao"
SOURCE = "https://rsssfbrasil.com/tablesr/rgp1967.htm"
ARQUIVO = "rsssfbrasil_rgp1967.htm"
BLOCOS_PRE = [0, 2]

CANONICAL.update({
    "atletico mineiro": "Atletico-MG",
    "ferroviario": "Ferroviário-PR",
    "portuguesa de desportos": "Portuguesa",
})

FASES = [
    Fase("Primeira fase", "1ª FASE", "CLASSIFICAÇÃO", "liga", 105),
    Fase("Quadrangular final", "QUADRANGULAR FINAL", "", "grupo", 12),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=117, arquivo=ARQUIVO, edicao=EDICAO, blocos_pre=BLOCOS_PRE)
