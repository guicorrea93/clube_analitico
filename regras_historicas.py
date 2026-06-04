"""Regras estruturais curadas do Campeonato Brasileiro 1989-2002.

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
