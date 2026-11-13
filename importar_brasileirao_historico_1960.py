"""Importa jogos da Taca Brasil 1960 (17 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Palmeiras campeao
contra o Fortaleza).
"""
from importar_brasileirao_historico_base import Fase, rodar

YEAR = 1960
EDICAO = "1960"
SOURCE = "https://www.rsssf.org/tablesb/brazcup60.html"
ARQUIVO = "rsssf_brazcup60.html"
CORTE_FINAL = "Taça Brasil Champions"

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 16, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 15, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=37, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
