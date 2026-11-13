"""Importa jogos da Taca Brasil 1967 (21 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1967
houve tambem o Robertao, outro campeonato reconhecido (edicao 1967_robertao).
Mata-mata em ida e volta, com jogo de desempate: zonas Norte, Central e Sul,
quartas de final, semifinais e final (Palmeiras campeao).
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1967
EDICAO = "1967_taca_brasil"
SOURCE = "https://www.rsssf.org/tablesb/brazcup67.html"
ARQUIVO = "rsssf_brazcup67.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL.update({
    "atletico": "Atletico-MG",
    "ferroviario": "Ferroviário-PR",  # o de Curitiba
})

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "CENTRAL ZONE", "mata_mata", 26, misto=True),
    Fase("Zona Central", "CENTRAL ZONE", "SOUTHERN ZONE", "mata_mata", 17, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 6, misto=True),
    Fase("Quartas de final", "QUARTERFINALS", "SEMIFINALS", "mata_mata", 3, misto=True),
    Fase("Semifinal", "SEMIFINALS", "\nFINAL", "mata_mata", 6, misto=True),
    Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=61, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
