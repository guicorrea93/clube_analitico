"""Regras estruturais curadas do Campeonato Brasileiro 1971-2002.

Este modulo concentra os METADADOS de fase que o parser RSSSF nao captura:
numero de grupos paralelos, formato da serie (mata-mata), criterio de
classificacao/titulo e pontos por vitoria da epoca. Tudo foi conferido contra a
fonte RSSSF local e corroboracao independente (auditoria 2026-06).

A atribuicao concreta de GRUPO por partida nao mora aqui: e derivada de forma
deterministica por componentes conexos em `enriquecer_historico.py` (os grupos
de cada fase sao disjuntos no calendario). Aqui ficam apenas os numeros
esperados de grupos e a narrativa.
"""
from __future__ import annotations

# Pontos por vitoria por epoca (2 pts ate 1994; 3 pts a partir de 1995).
PONTOS_VITORIA: dict[int, int] = {
    # 1977-1978: vitoria por 3 gols ou mais valia 3 pontos e as demais 2; o
    # dashboard usa 2 (a regra de saldo fica no criterio das fases).
    # 1975: o bonus era para vitoria por 2 gols ou mais; 1976: por 3 ou mais.
    1971: 2, 1972: 2, 1973: 2,
    1974: 2, 1975: 2, 1976: 2,
    1977: 2, 1978: 2, 1979: 2,
    1980: 2, 1981: 2, 1982: 2,
    1983: 2, 1984: 2, 1985: 2,
    1986: 2,
    1987: 2,
    1988: 3,
    1989: 2,
    1990: 2, 1991: 2,
    1992: 2, 1993: 2, 1994: 2,
    1995: 3, 1996: 3, 1997: 3, 1998: 3, 1999: 3,
    2000: 3, 2001: 3, 2002: 3,
}


def pontos_vitoria(ano: int) -> int:
    """Regra geral: 2 pts ate 1994, 3 pts depois (cobre anos fora do dict)."""
    return PONTOS_VITORIA.get(ano, 2 if ano <= 1994 else 3)


# Formatos de serie (valor de fase.formato_serie).
PONTOS_CORRIDOS = "pontos_corridos"   # liga: todos contra todos, turno unico
GRUPOS = "grupos"                     # grupos paralelos (quadrangulares/etc)
JOGO_UNICO = "jogo_unico"             # mata-mata em jogo unico
IDA_VOLTA = "ida_volta"               # mata-mata ida e volta (agregado)
MELHOR_DE_3 = "melhor_de_3"           # mata-mata melhor de 3 jogos

# Metadados por (ano, fase_nome). num_grupos > 1 dispara a derivacao de grupos.
# criterio explica como a fase classifica/decide (vai para fase.criterio).
FASE_META: dict[tuple[int, str], dict] = {
    # ---------------- 1971 (1o Campeonato Nacional, 20 clubes, 2 pts) ----------------
    (1971, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico entre os 20 clubes; a classificacao era dividida em dois grupos (A e B) e os melhores de cada grupo avancavam."},
    (1971, "Segunda fase"): {"num_grupos": 3, "formato_serie": GRUPOS,
        "criterio": "Tres grupos de 4 (turno e returno); o 1o de cada grupo vai ao triangular final."},
    (1971, "Triangular final"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Triangular em turno unico; Atletico-MG campeao (1-0 no Sao Paulo e 1-0 no Botafogo, no Maracana)."},

    # ---------------- 1972 (2o Campeonato Nacional, 26 clubes, 2 pts) ----------------
    (1972, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico entre os 26 clubes, com a classificacao em quatro grupos (A a D). ABC 2-1 Botafogo teve os pontos dados ao Botafogo no tribunal (gravado 0-1)."},
    (1972, "Segunda fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (turno unico); o 1o de cada grupo vai as semifinais."},
    (1972, "Semifinal"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico; empate classificava o de melhor campanha (Palmeiras 1-1 Internacional)."},
    (1972, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico no Morumbi; 0-0 com o Botafogo e Palmeiras campeao pela melhor campanha."},

    # ---------------- 1973 (3o Campeonato Nacional, 40 clubes, 2 pts) ----------------
    (1973, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Dois estagios, 28 jogos por clube, com tabela unica de 40 clubes; os 20 melhores avancam."},
    (1973, "Segunda fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 10 (turno unico), em janeiro e fevereiro de 1974; os 2 primeiros vao ao quadrangular final."},
    (1973, "Quadrangular final"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Quadrangular em turno unico; Palmeiras campeao invicto."},

    # ---------------- 1974 (Campeonato Nacional, 40 clubes, 2 pts) ----------------
    (1974, "Primeira fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 20 (turno unico); os melhores de cada grupo vao a fase semifinal."},
    (1974, "Fase semifinal"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 6 (turno unico); o 1o de cada grupo vai a fase final."},
    (1974, "Fase final"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Quadrangular em turno unico; Cruzeiro e Vasco empataram em pontos e foram ao jogo extra."},
    (1974, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo extra no Maracana (a CBD tirou o jogo do Mineirao); Vasco campeao, 2-1 no Cruzeiro."},

    # ---------------- 1975 (Copa Brasil, 42 clubes) ----------------
    (1975, "Primeira fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Grupos A e B (10 clubes cada) jogaram contra o outro grupo, assim como os grupos C e D (11 clubes cada); por isso cada par aparece junto. Vitoria por 2 gols ou mais valia 3 pontos; as demais, 2 (o dashboard conta 2)."},
    (1975, "Segunda fase"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Grupos 1 e 2 (10 clubes cada) jogaram contra o outro grupo, por isso aparecem juntos; os 6 primeiros de cada grupo avancam."},
    (1975, "Repescagem"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Grupos 3 a 6, com os eliminados da primeira fase; os vencedores voltam a disputa."},
    (1975, "Terceira fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 8 (turno unico); os 2 primeiros vao as semifinais."},
    (1975, "Semifinal"): {"num_grupos": 1, "formato_serie": JOGO_UNICO, "criterio": "Jogo unico."},
    (1975, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico no Beira-Rio; Internacional campeao (1-0 no Cruzeiro, gol de Figueroa)."},

    # ---------------- 1976 (Copa Brasil, 54 clubes) ----------------
    (1976, "Primeira fase"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Seis grupos (turno unico). Os 4 primeiros vao a segunda fase; os demais, a repescagem. Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2 (o dashboard conta 2)."},
    (1976, "Segunda fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 6 (G a J), turno unico."},
    (1976, "Repescagem"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Seis grupos (K a P) com os eliminados da primeira fase; o 1o de cada grupo segue na disputa."},
    (1976, "Terceira fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos (Q e R), turno unico; os 2 primeiros vao as semifinais."},
    (1976, "Semifinal"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico; o Corinthians eliminou o Fluminense nos penaltis (1-1, 4-1) no Maracana."},
    (1976, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico no Beira-Rio; Internacional campeao (2-0 no Corinthians)."},

    # ---------------- 1977 (Copa Brasil, 62 clubes) ----------------
    (1977, "Primeira fase"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Seis grupos. Os 5 primeiros vao aos grupos de vencedores; os demais, aos de perdedores. Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2 (o dashboard conta 2)."},
    (1977, "Segunda fase"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Grupos de vencedores (G a L), turno unico; os melhores vao a fase final."},
    (1977, "Repescagem"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Grupos de perdedores (M a R), turno unico, com vagas para a fase final. No grupo Q, o Fluminense-BA abandonou o jogo contra a Desportiva (suborno da federacao baiana; contado 0-0); o Vitoria-BA nao foi ao jogo extra e a vaga ficou com a Desportiva."},
    (1977, "Fase final"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 6 (turno unico); o 1o de cada grupo vai a semifinal."},
    (1977, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1977, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico no Mineirao em 05/03/1978; 0-0 e Sao Paulo campeao nos penaltis (3-2) contra o Atletico-MG, que terminou invicto."},

    # ---------------- 1978 (Copa Brasil, 74 clubes) ----------------
    (1978, "Primeira fase"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Seis grupos (turno unico). Os 6 primeiros vao a segunda fase; os demais, a repescagem. Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2 (o dashboard conta 2)."},
    (1978, "Segunda fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos (G a J), turno unico."},
    (1978, "Repescagem"): {"num_grupos": 6, "formato_serie": GRUPOS,
        "criterio": "Seis grupos (K a P) com os eliminados da primeira fase, em paralelo a segunda fase; o Gremio Maringa ganhou a vaga."},
    (1978, "Terceira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 8 (Q a T), turno unico; os 2 primeiros vao as quartas."},
    (1978, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Vasco avancou contra o Gremio pela melhor campanha (1-1 e 1-1)."},
    (1978, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1978, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Guarani campeao (1-0 e 1-0 contra o Palmeiras)."},

    # ---------------- 1979 (Copa Brasil, 94 clubes, 2 pts) ----------------
    (1979, "Primeira fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos (A a H), turno unico; 14 clubes entraram direto na segunda fase. Sao Paulo-RS x Operario-PR teve os pontos dados ao Sao Paulo-RS no tribunal (gravado 1-0)."},
    (1979, "Segunda fase"): {"num_grupos": 7, "formato_serie": GRUPOS,
        "criterio": "Sete grupos (I a O), turno unico; Palmeiras e Guarani de folga."},
    (1979, "Terceira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (P a S), turno unico; o 1o vai a semifinal. O Atletico-MG abandonou a fase: W.O. para Goias e Internacional (gravados 1-0)."},
    (1979, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1979, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Internacional campeao invicto (2-0 e 2-1 contra o Vasco)."},

    # ---------------- 1980 (Taca de Ouro, 44 clubes, 2 pts) ----------------
    (1980, "Primeira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 10 (turno unico); os 7 primeiros de cada grupo avancam."},
    (1980, "Segunda fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 4 (turno e returno), com America-SP, Americano, Bangu e Sport vindos da Taca de Prata; os 2 primeiros avancam."},
    (1980, "Desempate"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo extra pelo 2o lugar do grupo I da segunda fase; Guarani venceu o America-RJ por 3-2. A RSSSF nao soma este jogo na tabela final."},
    (1980, "Terceira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (turno unico); so o 1o colocado vai a semifinal."},
    (1980, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1980, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Agregado 3-3 com o Atletico-MG (0-1 e 3-2); Flamengo campeao pela melhor campanha na semifinal."},

    # ---------------- 1981 (Taca de Ouro, 44 clubes, 2 pts) ----------------
    (1981, "Primeira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 10 (turno unico); os 7 primeiros de cada grupo avancam."},
    (1981, "Segunda fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 4 (turno e returno), com Nautico, Bahia, Palmeiras e Uberaba vindos da Taca de Prata; os 2 primeiros vao as oitavas."},
    (1981, "Oitavas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1981, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Ponte Preta avancou contra o Vasco pela melhor campanha nas oitavas (0-0 e 0-0)."},
    (1981, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Gremio e Sao Paulo avancaram pela melhor campanha nas quartas (agregados empatados)."},
    (1981, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Gremio campeao (2-1 no Olimpico e 1-0 no Morumbi contra o Sao Paulo)."},

    # ---------------- 1982 (Taca de Ouro, 44 clubes, 2 pts) ----------------
    (1982, "Primeira fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 5 (turno e returno). Os 3 primeiros avancam; os quartos disputam a repescagem."},
    (1982, "Repescagem"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico entre quartos colocados; Londrina avancou pela melhor campanha no 0-0 com o Goias. A RSSSF nao soma estes jogos na tabela final."},
    (1982, "Segunda fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 4 (turno e returno), com America-RJ, Athletico-PR, Corinthians e Sao Paulo-RS vindos da Taca de Prata; os 2 primeiros avancam."},
    (1982, "Terceira fase"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Mata-mata em ida e volta."},
    (1982, "Quarta fase"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Corinthians avancou contra o Bangu pela melhor campanha na terceira fase (agregado 2-2)."},
    (1982, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1982, "Final"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3,
        "criterio": "Melhor de 3 contra o Gremio: 1-1, 0-0 e 1-0 (gol de Nunes no Olimpico); Flamengo campeao."},

    # ---------------- 1983 (Taca de Ouro, 44 clubes, 2 pts) ----------------
    (1983, "Primeira fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 5 (turno e returno). Os 3 primeiros avancam; os quartos vao ao playoff e os quintos a Taca de Prata."},
    (1983, "Playoff"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico entre quartos colocados; os pontos nao contam na tabela final. Os eliminados foram a Taca de Prata, de onde vieram Americano, Botafogo-SP, Guarani e Uberaba para a segunda fase."},
    (1983, "Segunda fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 4 (turno e returno); os 2 primeiros avancam."},
    (1983, "Terceira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (turno e returno); os 2 primeiros vao as quartas."},
    (1983, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Santos avancou contra o Goias por melhor campanha na terceira fase (0-0 e 2-2)."},
    (1983, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; Santos avancou contra o Atletico-MG no agregado (2-1 e 0-0)."},
    (1983, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Flamengo campeao (perdeu por 2-1 e venceu o Santos por 3-0 no Maracana)."},

    # ---------------- 1984 (Copa Brasil, 41 clubes, 2 pts) ----------------
    (1984, "Primeira fase"): {"num_grupos": 8, "formato_serie": GRUPOS,
        "criterio": "Oito grupos de 5 (turno e returno). Os 3 primeiros avancam; os quartos disputam a repescagem."},
    (1984, "Repescagem"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico entre quartos colocados; os vencedores entram na segunda fase. A RSSSF nao soma estes jogos na tabela final."},
    (1984, "Segunda fase"): {"num_grupos": 7, "formato_serie": GRUPOS,
        "criterio": "Sete grupos de 4 (turno e returno)."},
    (1984, "Terceira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (turno e returno), com o Uberlandia vindo da Taca CBF; os 2 primeiros vao as quartas."},
    (1984, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1984, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1984, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Fluminense campeao (1-0 e 0-0 contra o Vasco)."},

    # ---------------- 1985 (Copa Brasil, 44 clubes, 2 pts) ----------------
    (1985, "Primeira fase"): {"num_grupos": 3, "formato_serie": GRUPOS,
        "criterio": "Grupos A e B (10 clubes cada) jogaram contra o outro grupo nos dois estagios, por isso aparecem juntos; grupos C e D (12 clubes) jogaram turno e returno no proprio grupo. Vencedores de cada estagio e melhores campanhas avancam."},
    (1985, "Segunda fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 4 (turno e returno); so o 1o colocado vai a semifinal."},
    (1985, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": "Ida e volta."},
    (1985, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Jogo unico no Maracana; Coritiba campeao nos penaltis (1-1, 6-5) contra o Bangu."},

    # ---------------- 1986 (48 clubes no recorte oficial local) ----------------
    (1986, "Primeira fase"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Recorte local de 48 clubes: grupos A-D completos e vencedores dos grupos E-H que entram depois. A RSSSF lista outros grupos inferiores, que nao sao misturados nesta edicao."},
    (1986, "Segunda fase"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos em turno e returno; classificados avancam ao mata-mata."},
    (1986, "Terceira fase"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Mata-mata em ida e volta; alguns empates foram decididos por melhor campanha da fase anterior."},
    (1986, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Mata-mata em ida e volta; Atletico-MG avancou por melhor campanha no agregado empatado contra o Cruzeiro."},
    (1986, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Mata-mata em ida e volta."},
    (1986, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Sao Paulo e Guarani empataram no agregado; Sao Paulo campeao nos penaltis."},

    # ---------------- 1987 (Copa Uniao/Modulo Verde + final CBF) ----------------
    (1987, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Modulo Verde/Copa Uniao: dois grupos de 8 em dois estagios. Vencedores dos grupos/estagios avancaram as semifinais. Mantido como liga unica no dashboard para preservar a corrida agregada do modulo."},
    (1987, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Semifinais do Modulo Verde em ida e volta; Internacional decidiu na prorrogacao contra o Cruzeiro."},
    (1987, "Final Copa Uniao"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Final do Modulo Verde/Copa Uniao; Flamengo venceu o Internacional."},
    (1987, "Final CBF"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Cruzamento CBF nao disputado por Flamengo e Internacional. Sport e Guarani jogaram a decisao oficial; Sport campeao pela CBF."},

    # ---------------- 1988 (24 clubes, regra 3/2/1 em empates) ----------------
    (1988, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Fase inicial em dois estagios com grupos e cruzamentos. Vitoria valia 3 pontos; empate ia aos penaltis, com 2 pontos ao vencedor e 1 ao perdedor. Oito clubes avancaram ao mata-mata."},
    (1988, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Mata-mata em ida e volta; a regra de penaltis da fase inicial nao se aplicava."},
    (1988, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Mata-mata em ida e volta; a regra de penaltis da fase inicial nao se aplicava."},
    (1988, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Bahia campeao (2-1 e 0-0 contra o Internacional)."},

    # ---------------- 1989 (22 clubes, 2 pts) ----------------
    (1989, "Primeira fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 11; 8 melhores de cada grupo avancam. Coritiba foi eliminado por W.O. e perdeu 5 pontos."},
    (1989, "Segunda fase"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Segunda fase com 16 clubes em dois grupos cruzados; vencedores de grupo vao a final. Mantida como grupo unico no dashboard porque os jogos cruzam clubes dos dois grupos."},
    (1989, "Torneio de rebaixamento"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Torneio entre os remanescentes da primeira fase; Athletico-PR, Guarani e Sport foram rebaixados, alem do Coritiba eliminado."},
    (1989, "Final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO,
        "criterio": "Vasco entrou com ponto bonus pela melhor campanha e foi campeao ao vencer o Sao Paulo por 1-0; nao houve segundo jogo."},

    # ---------------- 1990 (20 clubes, 2 pts) ----------------
    (1990, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico em 2 estagios (1o contra o outro grupo de 10, 2o contra o proprio grupo). Vencedores de grupo de cada estagio + 4 melhores campanhas avancam; 2 rebaixados."},
    (1990, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
                                  "criterio": "Mata-mata em ida e volta; empate no agregado decidido pela melhor campanha."},
    (1990, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
                           "criterio": "Mata-mata em ida e volta; empate no agregado decidido pela melhor campanha."},
    (1990, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Corinthians campeao (agregado 2-0 sobre o Sao Paulo)."},

    # ---------------- 1991 (20 clubes, 2 pts) ----------------
    (1991, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico de 20 clubes; 4 melhores as semifinais; 2 rebaixados (Gremio e Vitoria)."},
    (1991, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Ida e volta; vantagem do empate ao de melhor campanha. Sao Paulo avancou no agregado empatado (1-1)."},
    (1991, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Sao Paulo campeao (agregado 1-0 sobre o Bragantino)."},

    # ---------------- 1992 (20 clubes, 2 pts) ----------------
    (1992, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico de 20 clubes; 8 melhores avancam. Sem rebaixamento nesta edicao."},
    (1992, "Segunda fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois quadrangulares (duplo turno); o vencedor de cada grupo vai a final."},
    (1992, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Botafogo tinha a vantagem do empate (melhor campanha), mas o Flamengo venceu por 5-2 no agregado e foi campeao."},

    # ---------------- 1993 (32 clubes, 2 pts) ----------------
    (1993, "Primeira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 8 (duplo turno). Grupos A/B classificam 3; C/D classificam 2 e disputam repescagem."},
    (1993, "Playoff"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Repescagem (ida e volta) entre clubes dos grupos C e D pela vaga restante."},
    (1993, "Segunda fase"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 4; o vencedor de cada grupo vai a final."},
    (1993, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Palmeiras campeao."},

    # ---------------- 1994 (24 clubes, 2 pts) ----------------
    (1994, "Primeira fase"): {"num_grupos": 4, "formato_serie": GRUPOS,
        "criterio": "Quatro grupos de 6 (duplo turno)."},
    (1994, "Segunda fase"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Fase de grupos da segunda etapa (estrutura E/F com subfases na fonte; times se cruzam entre subfases)."},
    (1994, "Repescagem"): {"num_grupos": 1, "formato_serie": GRUPOS,
        "criterio": "Repescagem concorrente a segunda fase, por vagas no mata-mata."},
    (1994, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (1994, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (1994, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Palmeiras campeao."},

    # ---------------- 1995 (24 clubes, 3 pts) ----------------
    # Os dois turnos somam um turno unico completo (11 intra-grupo + 12 cross-grupo = 23 jogos/clube).
    (1995, "Primeiro turno"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Primeira metade do turno unico (confrontos dentro de cada grupo de 12)."},
    (1995, "Segundo turno"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Segunda metade do turno unico (confrontos cruzados entre os grupos); junto com o 1o turno equivale a todos contra todos."},
    (1995, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (1995, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Botafogo campeao (vantagem de melhor campanha no agregado empatado)."},

    # ---------------- 1996 (24 clubes, 3 pts) ----------------
    (1996, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico; 8 melhores ao mata-mata; 2 rebaixados."},
    (1996, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (1996, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (1996, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Gremio campeao por melhor campanha (agregado 2-2 com a Portuguesa)."},

    # ---------------- 1997 (26 clubes, 3 pts) ----------------
    (1997, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico de 26 clubes; 8 melhores avancam."},
    (1997, "Grupo semifinal"): {"num_grupos": 2, "formato_serie": GRUPOS,
        "criterio": "Dois grupos de 4 (duplo turno); apenas o 1o colocado de cada grupo vai a final."},
    (1997, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Vasco campeao por melhor campanha (0-0 e 0-0 na final)."},

    # ---------------- 1998 (24 clubes, 3 pts) ----------------
    (1998, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico; 8 melhores ao mata-mata."},
    (1998, "Quartas de final"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3, "criterio": "Serie melhor de 3 jogos."},
    (1998, "Semifinal"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3, "criterio": "Serie melhor de 3 jogos."},
    (1998, "Final"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3,
        "criterio": "Final em melhor de 3; Corinthians campeao no 3o jogo."},

    # ---------------- 1999 (22 clubes, 3 pts) ----------------
    (1999, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico; 8 melhores ao mata-mata."},
    (1999, "Quartas de final"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3,
        "criterio": "Serie melhor de 3; vantagem ao melhor classificado."},
    (1999, "Semifinal"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3,
        "criterio": "Serie melhor de 3; vantagem ao melhor classificado."},
    (1999, "Final"): {"num_grupos": 1, "formato_serie": MELHOR_DE_3,
        "criterio": "Final em melhor de 3; Corinthians campeao."},

    # ---------------- 2000 (Copa Joao Havelange, 3 pts) ----------------
    (2000, "Modulo Azul"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Modulo Azul (1o nivel, 25 clubes) - 1 dos 4 modulos da Copa Joao Havelange. Turno unico."},
    (2000, "Oitavas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (2000, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (2000, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (2000, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Vasco campeao (agregado 4-2). A volta foi um replay em 18/01/2001, apos a queda do alambrado em Sao Januario."},

    # ---------------- 2001 (28 clubes, 3 pts) ----------------
    (2001, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico de 28 clubes (tabela unica); 8 melhores ao mata-mata. Athletico-PR comecou com -5 pts (punicao)."},
    (2001, "Quartas de final"): {"num_grupos": 1, "formato_serie": JOGO_UNICO, "criterio": "Jogo unico."},
    (2001, "Semifinal"): {"num_grupos": 1, "formato_serie": JOGO_UNICO, "criterio": "Jogo unico."},
    (2001, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Athletico-PR campeao (agregado 5-2 sobre o Sao Caetano)."},

    # ---------------- 2002 (26 clubes, 3 pts) ----------------
    (2002, "Primeira fase"): {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS,
        "criterio": "Turno unico de 26 clubes (tabela unica); 8 melhores ao mata-mata."},
    (2002, "Quartas de final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (2002, "Semifinal"): {"num_grupos": 1, "formato_serie": IDA_VOLTA, "criterio": ""},
    (2002, "Final"): {"num_grupos": 1, "formato_serie": IDA_VOLTA,
        "criterio": "Santos campeao (agregado 5-2 sobre o Corinthians)."},
}


def fase_meta(ano: int, fase_nome: str, fase_tipo: str, num_times: int, num_jogos: int) -> dict:
    """Retorna metadados curados; cai para inferencia razoavel quando ausente."""
    m = FASE_META.get((ano, fase_nome))
    if m:
        return {"num_grupos": m["num_grupos"], "formato_serie": m["formato_serie"], "criterio": m.get("criterio", "")}
    # Inferencia de fallback (anos/fases nao curados).
    if fase_tipo == "liga":
        return {"num_grupos": 1, "formato_serie": PONTOS_CORRIDOS, "criterio": ""}
    if fase_tipo == "mata_mata":
        legs = JOGO_UNICO if num_jogos <= num_times // 2 else IDA_VOLTA
        return {"num_grupos": 1, "formato_serie": legs, "criterio": ""}
    return {"num_grupos": 1, "formato_serie": GRUPOS, "criterio": ""}
