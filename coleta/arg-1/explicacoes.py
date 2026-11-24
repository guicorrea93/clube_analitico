"""Correções e explicações da coleta da 1ª divisão argentina, edição a edição (entram no relatório).

- EXTRAS: jogos que a página da RSSSF traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {
    # AR-018: jogos de 2016/17 que a página da RSSSF não tem (os 4 clubes ficavam com 28 jogos); da ESPN, hora local (UTC-3)
    "2016/17": [
        {"mandante": "Lanús", "visitante": "Atlético Tucumán", "gm": 1, "gv": 0, "data": "2016-11-19", "estadio": "Ciudad de Lanús",
         "cidade": "Lanús", "fonte_id": "espn:462770", "obs": "jogo que só a ESPN tem"},
        {"mandante": "Lanús", "visitante": "Gimnasia La Plata", "gm": 1, "gv": 0, "data": "2016-12-05", "estadio": "Ciudad de Lanús",
         "cidade": "Lanús", "fonte_id": "espn:462744", "obs": "jogo que só a ESPN tem"},
        {"mandante": "Tigre", "visitante": "Atlético Tucumán", "gm": 0, "gv": 0, "data": "2016-12-19",
         "estadio": "Monumental de Victoria (José Dellagiovanna)", "cidade": "Victoria", "fonte_id": "espn:462710",
         "obs": "jogo que só a ESPN tem"},
        {"mandante": "Tigre", "visitante": "Gimnasia La Plata", "gm": 0, "gv": 1, "data": "2017-03-18",
         "estadio": "Monumental de Victoria (José Dellagiovanna)", "cidade": "Victoria", "fonte_id": "espn:462684",
         "obs": "jogo que só a ESPN tem"},
    ],
    "1936 Copa de Oro": [
        {"mandante": "River Plate", "visitante": "San Lorenzo", "gm": 4, "gv": 2, "data": "1936-12-20", "fase": "Final",
         "estadio": "Estádio do Independiente", "cidade": "Avellaneda", "fonte_id": "rsssf:arg-oro36:9",
         "gols": [("River Plate", "Renato Cesarini", 39, "normal"), ("San Lorenzo", "Miguel Pantó", 55, "normal"),
                  ("River Plate", "Bernabé Ferreyra", 73, "normal"), ("River Plate", "Adolfo Pedernera", 76, "normal"),
                  ("San Lorenzo", "Rubén Cavadini", 81, "normal"), ("River Plate", "Renato Cesarini", 86, "normal")],
         "obs": "jogo único; o 2-1 de Bernabé Ferreyra desviou em Chividini; o 3-2 é de Cavadini (outras fontes: Canteli)"},
    ],
}

# erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo)
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("arg66", 396): ("0 6 Racing", "0:6 Racing", "placar sem os dois-pontos ('0 6'); 0-6 fecha com a tabela publicada"),
    ("arg49", 246): ("Estudiantes de La Plata Gimnasia", "Estudiantes de La Plata  Gimnasia",
                     "um espaço só entre o visitante e o local do jogo: era lido como 'Gimnasia 1-0 Gimnasia' (AR-016)"),
    ("arg98", 61): ("River Plate   1-3 Rosario", "River Plate   1-3 Rosario Central",
                    "'Rosario' sozinho não era reconhecido e o jogo caía (AR-014)"),
}

# (temporada, "página:linha") -> {campo: valor, "motivo": texto}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1923 Asociación", "arg23:820"): {"fase": "Desempate do título", "motivo": "desempate Boca x Huracán de 1924, sem título "
                                                                    "na página (AR-025)"},
    ("1923 Asociación", "arg23:824"): {"fase": "Desempate do título", "motivo": "desempate Boca x Huracán de 1924, sem título "
                                                                    "na página (AR-025)"},
    ("1923 Asociación", "arg23:828"): {"fase": "Desempate do título", "motivo": "desempate Boca x Huracán de 1924, sem título "
                                                                    "na página (AR-025)"},
    ("1923 Asociación", "arg23:832"): {"fase": "Desempate do título", "motivo": "desempate Boca x Huracán de 1924, sem título "
                                                                    "na página (AR-025)"},
    ("1987/88", "arg88:483"): {"esp": "awd", "gm": 0, "gv": 1, "motivo": "abandonado antes de começar; \"later awarded "
                                                                       "0-1\" (nota da página); vale na tabela (AR-003)"},
    ("1913 Federación", "arg13:447"): {"esp": "", "motivo": "Kimberley 3-1 Porteño é o jogo repetido em 15/08 (a nota fala do "
                                                            "primeiro, abandonado com 0-0 aos 75' e anulado); vale na tabela"},
    ("1936 Copa de Oro", "arg-oro36:17"): {"descartar": True, "motivo": "a linha do texto corrido vira o jogo escrito à mão "
                                                                       "(EXTRAS), com data, local e autores dos gols"},
    ("1965", "arg65:198"): {"esp": "abd", "motivo": "Independiente 2-2 Racing Club suspenso aos 68' e não continuado; a tabela "
                                                    "publicada não conta o jogo (33 jogos para os dois)"},
}

EXPLICACOES: dict[str, list[str]] = {
    "1908": ["Nacional de Buenos Aires: eliminado depois de 2 jogos, anulados (nota da página); fica no fim da classificação, "
             "fora da tabela publicada (AR-020)"],
    "1929": ["classificação com os números das tabelas dos grupos (com os pontos dados por W.O.: Tigre x Lanús, Defensores x "
             "Barracas Central, Quilmes x Sportivo Barracas) mais os desempates, o 3º lugar e a final (AR-020)"],
    "1965": ["Estudiantes e Racing empatam com 36 pontos: a tabela da RSSSF põe o Estudiantes em 5º, a Wikipédia em espanhol, o "
             "Racing (saldo de gols); fica a ordem publicada (AR-020)"],
    "1934 Liga": ["fusões temporárias de 1934 à parte dos clubes (D-25 h): os jogos de \"Atlanta/Argentinos Jrs\" ficam com o "
                  "Atlanta-Argentinos Juniors e os de \"Talleres/Lanús\" com a Unión Talleres-Lanús; a tabela da RSSSF põe a "
                  "campanha inteira (39 jogos) na linha do Argentinos Juniors, que fica com só os 14 jogos de antes da fusão"],
    "1893": ["Quilmes Club (1893) e Quilmes Rovers (1895) são clubes à parte do Quilmes atual: a ligação não tem prova (D-25 g)"],
    "2026 Apertura": ["edição de 2026 que já terminou, entra agora (D-01); o Clausura 2026 e a tabela anual entram quando acabarem"],
    "1975 Metropolitano": ["a tabela da Wikipédia em espanhol tem 1 gol a mais para River (contra), Huracán (contra), Estudiantes "
                           "(pró) e Banfield (pró): ela conta os gols de campo de Estudiantes 1-2 Huracán (abandonado aos 78', dado "
                           "0-2) e Banfield 1-2 River Plate (dado 0-2); a RSSSF e o pacote contam o placar dado (AR-019)"],
    "1926 Amateurs": ["a página arg26 põe cada linha num <PRE> próprio, sem quebra: o texto puro juntava os jogos e só 43 dos 325 "
                      "eram lidos; com a quebra por <PRE> (ler_rsssf.PRE_POR_LINHA) entram todos (AR-006, AR-034)"],
    "1919 Asociación": ["o campeonato começado em março foi anulado (clubes desfiliados ou expulsos) e recomeçado em setembro "
                        "com 6 clubes; só os jogos do recomeçado entram (12 não foram jogados) (AR-008)"],
    "1912 Asociación": ["a classificação é a tabela publicada, sem os clubes que saíram para a FAF no meio do campeonato "
                        "(os jogos deles ficam) (AR-010)"],
    "1891": ["a liga da época deu o título dividido entre Saint Andrew's e Caledonians (empatados); Saint Andrew's venceu o "
             "desempate pelas medalhas. A AFA cita só o Saint Andrew's, que fica como campeão no pacote"],
    "1936 Copa de Oro": ["jogo único entre os campeões da Copa de Honor (San Lorenzo) e da Copa Campeonato (River Plate), "
                         "lido à mão da página arg-oro36 da RSSSF (texto corrido)"],
}
