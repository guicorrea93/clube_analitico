"""Importa jogos da Taca Brasil 1961 (18 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra
o Bahia).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1961
EDICAO = "1961"
SOURCE = "https://www.rsssf.org/tablesb/brazcup61.html"
ARQUIVO = "rsssf_brazcup61.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL["america"] = "America-RJ"  # a fonte escreve so "America" (Rio de Janeiro-GB)
CANONICAL["santa cruz"] = "Santa Cruz-SE"  # o de Aracaju; o de Recife nao jogou em 1961

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 15, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 16, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=38, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
