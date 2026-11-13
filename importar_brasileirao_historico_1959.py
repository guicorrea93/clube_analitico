"""Importa jogos da Taca Brasil 1959 (16 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate quando cada clube vencia uma
vez: grupos regionais nas zonas Norte e Sul, decisao de cada zona,
semifinais (Santos e Vasco entraram direto) e final. Bahia campeao no
terceiro jogo contra o Santos, em marco de 1960.
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1959
EDICAO = "1959"
SOURCE = "https://www.rsssf.org/tablesb/brazcup59.html"
ARQUIVO = "rsssf_brazcup59.html"
CORTE_FINAL = "Taça Brasil champions"
VIRADA = 7

CANONICAL.update({
    "auto esporte": "Auto Esporte",      # Joao Pessoa-PB
    "ferroviario": "Ferroviário-MA",     # Sao Luis-MA
})

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 17, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 10, misto=True),
    Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=35, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO, virada=VIRADA)
