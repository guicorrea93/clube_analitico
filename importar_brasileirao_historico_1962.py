"""Importa jogos da Taca Brasil 1962 (18 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao no terceiro jogo contra o Botafogo (4-3, 1-3 e 5-0), em abril de 1963).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1962
EDICAO = "1962"
SOURCE = "https://www.rsssf.org/tablesb/brazcup62.html"
ARQUIVO = "rsssf_brazcup62.html"
CORTE_FINAL = "Taça Brasil champions"
VIRADA = 7  # a final foi em 1963

CANONICAL["comercial"] = "Comercial-PR"

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 10, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=39, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO, virada=VIRADA)
