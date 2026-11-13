"""Importa jogos do Robertao 1968 (Torneio Roberto Gomes Pedrosa, 17 clubes).

Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1968
houve tambem a Taca Brasil (edicao 1968_taca_brasil).
Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
grupos (A e B); os 2 primeiros de cada grupo vao ao quadrangular final, em
turno unico (Santos campeao).

Fonte: RSSSF Brasil ("TIME 1 x 0 TIME", datas 06.09.1968). A pagina repete
as tabelas e a fase final depois do quadro do campeao; a leitura para no
primeiro "Table" da fase final.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1968
EDICAO = "1968_robertao"
SOURCE = "https://rsssfbrasil.com/tablesr/rgp1968.htm"
ARQUIVO = "rsssfbrasil_rgp1968.htm"

CANONICAL.update({
    "atletico mineiro": "Atletico-MG",
    "portuguesa de desportos": "Portuguesa",
})

FASES = [
    Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
    Fase("Fase final", "Final Phase", "Table", "grupo", 6),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=142, arquivo=ARQUIVO, edicao=EDICAO)
