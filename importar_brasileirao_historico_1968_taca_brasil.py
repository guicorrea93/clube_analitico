"""Importa jogos da Taca Brasil 1968 (21 clubes).

Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1968
houve tambem o Robertao, outro campeonato reconhecido (edicao 1968_robertao).
Zonas Norte, Central e Sul (com triangulares regionais em turno e returno,
que no painel aparecem como confrontos), quartas de final, semifinais e final
(Botafogo campeao). A edicao terminou em 1969; as datas trazem "/69".
"""
from importar_brasileirao_historico_base import CANONICAL, Fase, rodar

YEAR = 1968
EDICAO = "1968_taca_brasil"
SOURCE = "https://www.rsssf.org/tablesb/brazcup68.html"
ARQUIVO = "rsssf_brazcup68.html"
CORTE_FINAL = "Taça Brasil champions"

CANONICAL["operario"] = "Operário-MT"  # a classificacao do banco usa o de Mato Grosso

FASES = [
    Fase("Zona Norte", "NORTHERN ZONE", "CENTRAL ZONE", "mata_mata", 25, misto=True),
    Fase("Zona Central", "CENTRAL ZONE", "SOUTHERN ZONE", "mata_mata", 13, misto=True),
    Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 6, misto=True),
    Fase("Quartas de final", "QUARTERFINALS", "SEMIFINAL", "mata_mata", 2, misto=True),
    Fase("Semifinal", "SEMIFINAL", "\nFinal", "mata_mata", 5, misto=True),
    Fase("Final", "\nFinal", "", "mata_mata", 2, misto=True),
]

if __name__ == "__main__":
    rodar(YEAR, SOURCE, FASES, total=53, corte_final=CORTE_FINAL, arquivo=ARQUIVO, edicao=EDICAO)
