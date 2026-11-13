"""Importa jogos da Taca Brasil 1965 (22 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
Norte e Sul, decisao de cada zona, quartas de final, semifinais e final
(Santos campeao contra o Vasco). Nesta pagina as fases nacionais vem como
"QUARTERFINALS", "Semifinal" e "Final".
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1965
EDICAO = "1965"
SOURCE = "https://www.rsssf.org/tablesb/brazcup65.html"
ARQUIVO = "rsssf_brazcup65.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL.update({
    "eletrovapo": "Eletrovapo-RJ",
    "gremio maringa": "GE Maringá",
    "guanabara": "Guanabara-DF",
    "olimpico": "Olímpico-AM",
})

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 16, misto=True),
    Fase("Quartas de final", "QUARTERFINALS", "\nSemifinal", "mata_mata", 5, misto=True),
    Fase("Semifinal", "\nSemifinal", "\nFinal", "mata_mata", 4, misto=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=48, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
