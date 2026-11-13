"""Importa jogos da Taca Brasil 1963 (20 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra o Bahia).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1963
EDICAO = "1963"
SOURCE = "https://www.rsssf.org/tablesb/brazcup63.html"
ARQUIVO = "rsssf_brazcup63.html"
CORTE_FINAL = "Taça Brasil champions"
VIRADA = 7  # a final foi em janeiro de 1964

CANONICAL["atletico"] = "Atletico-MG"

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 23, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 16, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=45, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO, virada=VIRADA)
