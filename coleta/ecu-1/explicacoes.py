"""Correções e explicações da coleta da 1ª divisão equatoriana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("ecua99", 501): ("No Descenso:", "Liguilla No Descenso", "título curto: os 30 jogos da liguilla do rebaixamento iam para a "
                                                             "\"Final\" (EC-006)"),
    ("ecua63", 64): ("Final", "Final Round", "grupo final de pontos corridos, não mata-mata (EC-007)"),
    ("ecua66", 90): ("Final", "Final Round", "grupo final de pontos corridos, não mata-mata (EC-007)"),
    ("ecua97", 393): ("Championship Playoff", "Hexagonal Final", "hexagonal final de pontos corridos, não mata-mata (EC-007)"),
    ("ecua97", 467): ("Playoff Descenso", "Relegation Group", "quadrangular do rebaixamento de pontos corridos (EC-010)"),
    ("ecua05", 53): ("Emelec                0-2 LDU de Quito", "Emelec                2-2 LDU de Quito",
                     "placar errado na página: com 2-2 a tabela do Apertura 2005 fecha (EC-011)"),
    ("ecua64", 46): ("Deportivo Quito 1 0 LDU Quito", "Deportivo Quito 1-0 LDU Quito", "placar sem o hífen (\"1 0\")"),
    ("ecua64", 37): ("4.Amèrica", "4.América de Manta", "\"Amèrica\" [Manta] na tabela: o América de Manta (\"AmM\" na tabela "
                                                       "de confrontos)"),
    ("ecua64", 41): ("8.América", "8.América de Ambato", "\"América\" [Ambato] na tabela: o América de Ambato (\"AmA\")"),
    ("ecua66", 32): ("4.América", "4.América de Ambato", "\"América\" [Ambato] na tabela do grupo A: o América de Ambato "
                                                        "(\"AmA\" na tabela de confrontos)"),
    **{("ecua66", n): (f"{nome}5  ", f"{nome}6  ", "grupo A da Costa com 5 jogos por clube na tabela; são 6 (turno e returno "
                                                   "entre 4 clubes, como a tabela de confrontos e V+E+D)")
       for n, nome in ((65, "Patria                "), (66, "Emelec                "), (67, "9 de Octubre          "),
                       (68, "América               "))},
    ("ecua66", 68): ("4.América               5  ", "4.América de Manta       6  ",
                     "\"América\" [Manta] na tabela do grupo A da Costa: o América de Manta (\"AmM\"); são 6 jogos, não 5"),
    ("ecua73", 114): ("LDU de Quito", "Barcelona", "a LDU de Quito não jogou a Serie A de 1973; o terceiro jogo da semifinal "
                                                   "foi El Nacional 2-0 Barcelona, em Cuenca (Wikipédia em espanhol)"),
    ("ecua05", 563): ("Deportivo Quevedo", "Olmedo", "o Deportivo Quevedo caiu no Apertura; os três gols do visitante são de "
                                                    "Celso Cuero, do Olmedo, e a tabela do Clausura conta esse jogo para o Olmedo"),
    **{("ecua85", n): ("30 18  8  8", "30 18  8  4", "Filanbanco com 18 vitórias, 8 empates e 8 derrotas em 30 jogos (dá 34); "
                                                    "são 4 derrotas, como os 44 pontos (2 x 18 + 8) e os jogos da página")
       for n in (19, 403)},
    **{("ecua85", n): ("9 de octubre", "9 de Octubre", "nome em minúscula (o leitor de tabela espera \"9 de Octubre\")")
       for n in (438, 558)},
    ("ecua99", 407): ("Championship Final:", "Liguilla Final:", "o título \"Championship Final\" abre a liguilla final de pontos "
                                                              "corridos (a final de ida e volta vem depois, na linha 489)"),
    ("ecua05", 333): ("", "Quarterfinals", "as quartas de final do Apertura não têm título (só a nota \"top-8 qualify for "
                                           "knock-out stage (quarterfinals)\"): a linha em branco antes dos jogos vira o título"),
    ("ecua06", 227): ("Olmedo                1-0 Emelec", "Olmedo                1-0 Deportivo Cuenca",
                      "o Emelec aparece duas vezes na 13ª rodada do Apertura e o Deportivo Cuenca nenhuma; a tabela do "
                      "Apertura conta a derrota por 0-1 para o Cuenca"),
    ("ecua06", 556): ("Aucas                  -  Deportivo Azogues", "Aucas                 2-0 Deportivo Azogues",
                      "jogo sem placar; os dois gols listados são do Aucas (Palacios, Rodríguez) e a tabela do Clausura conta "
                      "o 2-0"),
    ("ecua07", 222): ("Deportivo Quito        -  Macará", "Deportivo Quito       1-0 Macará",
                      "jogo sem placar; um gol listado (Vinces, do Deportivo Quito) e a tabela da 1ª etapa conta o 1-0"),
    ("ecua98", 418): ("Emelec dns for 2nd half;", "Emelec dns for 2nd half; apparently awarded 2-0]",
                      "a nota do jogo dado continua na linha de baixo, junto do jogo seguinte"),
    ("ecua98", 419): ("Espoli       apparently awarded 2-0]", "Espoli", "fim da nota do jogo de cima (linha 418), não deste"),
    ("ecua98", 624): ("Championship", "Championship Final", "título da final entre os campeões do Apertura e do Clausura "
                                                            "(\"Playoffs: / Championship\")"),
}

_DUP = "a mesma partida aparece duas vezes na página (no grupo e de novo na fase seguinte): fica a primeira (EC-008)"
CORRIGE: dict[tuple[str, str], dict] = {
    **{("1984", f"ecua84:{n}"): {"descartar": True, "motivo": _DUP} for n in (483, 492, 501, 511, 521, 531)},
    **{("1986", f"ecua86:{n}"): {"descartar": True, "motivo": _DUP} for n in (541, 542, 552, 553, 565, 566, 579, 580, 592, 593, 603, 604)},
    **{("1994", f"ecua94:{n}"): {"descartar": True, "motivo": _DUP} for n in (484, 494)},
    ("1965", "ecua65:39"): {"esp": "wo_m", "motivo": "Aucas perdeu os pontos (jogador irregular); placar de campo 0-1 (EC-012)"},
    ("1965", "ecua65:46"): {"esp": "wo_m", "motivo": "Aucas perdeu os pontos (jogadores irregulares); placar de campo 0-0 (EC-012)"},
    ("1965", "ecua65:53"): {"esp": "wo_v", "motivo": "Aucas perdeu os pontos (jogadores irregulares); placar de campo 0-0 (EC-012)"},
    ("1965", "ecua65:72"): {"esp": "wo_v", "motivo": "Aucas perdeu os pontos (jogadores irregulares); placar de campo 2-2 (EC-012)"},
    ("2025", "espn:759348"): {"esp": "wo_v", "motivo": "El Nacional x Delfín: W.O. 0-3 para o Delfín (ESPN e es), como decidido "
                                                    "pelo Guilherme (D-20 c, EC-015)"},
    ("1998", "ecua98:129"): {"esp": "", "motivo": "jogo interrompido por invasão de campo aos 81 minutos, com 1-2, e terminado em "
                                                  "16 de maio (nota da página): vale o 1-2, como a tabela conta"},
    **{(t, f"{pg}:{n}"): {"descartar": True, "motivo": "jogo interrompido e completado depois: a página traz as duas linhas "
                                                       "(\"abd\" e a do restante do jogo, com o placar final); fica a segunda"}
       for t, pg, n in (("2003", "ecua03", 46), ("2006", "ecua06", 260), ("2024", "ecua2024", 106))},
    ("2025", "espn:759348"): {"esp": "n/p", "motivo": "último jogo do Hexagonal 2 (El Nacional x Delfín, 19/12): a RSSSF diz que "
                                                     "não foi disputado e as tabelas contam 39 jogos para os dois; a ESPN "
                                                     "registra 0-3 (provável W.O. do El Nacional, rebaixado por dívidas)"},
    ("1998", "ecua98:418"): {"esp": "awd", "gm_of": 2, "gv_of": 0,
                             "motivo": "jogo abandonado no intervalo com 2-0 (o Emelec não voltou para o 2º tempo) e dado ao "
                                       "Deportivo Quito por 2-0 (nota da página), como a tabela do Hexagonal 1 conta"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1988": ["artilheiro Janio Pinto (LDU de Quito) com 19 gols, como a página do ano na RSSSF (Topscorers) e a Wikipédia em "
             "espanhol; a lista da RSSSF (ecuatops) dá 18 (EC-014)"],
    "1996": ["artilheiro Ariel Graziani (Emelec) com 29 gols, como a RSSSF, a Wikipédia em inglês (temporada 1996) e o El "
             "Universo (26/12/2002); a Wikipédia em espanhol dá 30 (EC-014)"],
    "1999": ["artilheiro Christian Bottero (Macará) com 25 gols, como a RSSSF e o El Universo (26/12/2002); a Wikipédia em "
             "espanhol dá 24 (EC-014)"],
}
