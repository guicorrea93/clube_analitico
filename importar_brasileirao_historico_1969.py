"""Importa jogos do Robertao 1969 (Torneio Roberto Gomes Pedrosa, 17 clubes).

Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010).
Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
grupos (A e B); os 2 primeiros de cada grupo vao a fase final. Fase final:
quadrangular em turno unico (Palmeiras campeao).

Fonte: RSSSF Brasil (a pagina da RSSSF de 1969 so traz as tabelas). Formato
"TIME 1 x 0 TIME" e datas 06.09.1969; a leitura para no "Title Match", que
repete o ultimo jogo.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1969
EDICAO = "1969"
SOURCE = "https://rsssfbrasil.com/tablesr/rgp1969.htm"
ARQUIVO = "rsssfbrasil_rgp1969.htm"
CORTE_FINAL = "Title Match"

CANONICAL.update({
    "america": "America-RJ",
    "atletico mineiro": "Atletico-MG",
    "portuguesa de desportos": "Portuguesa",
})

FASES = [
    Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
    Fase("Fase final", "Final Phase", "", "grupo", 6),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=142, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
