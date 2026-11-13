"""Importa jogos da Taca Brasil 1966 (22 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Cruzeiro campeao
contra o Santos, 6-2 e 3-2).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1966
EDICAO = "1966"
SOURCE = "https://www.rsssf.org/tablesb/brazcup66.html"
ARQUIVO = "rsssf_brazcup66.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL.update({
    "ferroviario": "Ferroviário-PR",  # o de Curitiba
    "rabello": "Rabello-DF",
})

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 19, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=47, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
