"""Importa jogos da Taca Brasil 1964 (22 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra o Flamengo).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1964
EDICAO = "1964"
SOURCE = "https://www.rsssf.org/tablesb/brazcup64.html"
ARQUIVO = "rsssf_brazcup64.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL["atletico"] = "Atletico-MG"
CANONICAL["gremio maringa"] = "GE Maringá"

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 23, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 20, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=49, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
