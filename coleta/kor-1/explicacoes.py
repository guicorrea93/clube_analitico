"""Correções e casos especiais da K League, com a prova de cada um (chave: "<ano>_<meetSeq>_<gameId>" do portal).

- WO: jogos que a K League deu por W.O. (기권패). O portal registra 0-0 sem lances; entram com `resultado_especial` = "wo"
  e o vencedor na observação: em 1987 sem placar (a tabela oficial conta a vitória sem gols), em 2012 com o 2-0 dado
  (a tabela oficial conta os gols).
- GOL_FALTANDO: gols que o boletim do portal não tem, com a fonte que os dá (o placar segue a fonte e as tabelas).
"""
from __future__ import annotations

_WO_1987 = ("o Hyundai Horang-i não jogou (\"현대 호랑이 기권패\"; a K League "
            "dá 2-0, sem contar os gols na tabela; Wikipédia em coreano, 1987년 K리그의 경기 결과); no portal, 0-0 sem lances")
_WO_2012 = ("o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não "
            "cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do "
            "Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro")
WO = {
    "1987_1_79": {"esp": "wo", "vencedor": "m", "motivo": _WO_1987},
    "1987_1_80": {"esp": "wo", "vencedor": "m", "motivo": _WO_1987},
}
for _g, _lado in ((247, "m"), (256, "v"), (262, "v"), (270, "m"), (278, "v"), (286, "m"), (294, "v"), (302, "m"), (312, "v"),
                  (320, "m"), (326, "v"), (333, "m"), (344, "m"), (351, "v")):
    WO[f"2012_1_{_g}"] = {"esp": "wo", "vencedor": _lado, "gm_of": 2 if _lado == "m" else 0, "gv_of": 0 if _lado == "m" else 2,
                          "motivo": _WO_2012}

# (lado, jogador em hangul, tempo, minuto contado do começo do tempo, acréscimo, tipo)
GOL_FALTANDO = {
    "1990_1_76": ([("v", "변병주", 2, 45, 1, "normal")],
                  "o 3º gol do Ulsan Hyundai (Byeon Byeong-ju, 90+1) não está no boletim do portal (que dá 2-2); 2-3 na RSSSF e "
                  "na Wikipédia em coreano (1990년 K리그의 경기 결과), e as duas tabelas do ano fecham com 2-3"),
}

# linhas da tabela da RSSSF que não fecham com os jogos, e o que a Wikipédia em coreano (tabela do ano) diz
TABELA_RSSSF = {
    1987: "A Wikipédia em coreano (1987년 K리그) dá os mesmos números daqui para o FC Seoul (Lucky-Goldstar): 7-7-18, 26-55, "
          "21 pontos; a RSSSF tem 56 gols sofridos e um placar diferente (Pohang 2-1 Lucky-Goldstar em 31/10; o portal e a Wikipédia em coreano dão 2-3).",
    1989: "A Wikipédia em coreano (1989년 K리그) dá 47 pontos ao FC Seoul (Lucky-Goldstar), como aqui (15 vitórias e 17 "
          "empates); os 42 da RSSSF são erro de conta.",
    1991: "A Wikipédia em coreano (1991년 K리그) dá ao Jeju United (Yukong) 10-17-13, 38-40, 37 pontos, como aqui.",
    1997: "Sem explicação: a RSSSF dá ao Jeju United (Puchon SK) 18-35 e aqui são 19-36 (mesmos pontos); a RSSSF não tem os "
          "jogos de 1997 e a Wikipédia em coreano não tem a tabela; os outros 9 clubes fecham.",
    2007: "Erro de digitação da skorhist.html: 27-53 para o Jeju United; a página de 2007 da RSSSF dá 27-35, como aqui e como a "
          "tabela oficial da K League.",
    2016: "O Jeonbuk Hyundai perdeu 9 pontos (suborno de árbitros por um olheiro do clube, em 2013): 69 nos jogos, 60 na "
          "RSSSF e na tabela oficial (ajuste_pontos -9).",
}

# empate nos pênaltis decidido no sorteio: (vencedor "m"/"v", motivo); os pênaltis ficam como foram
SORTEIO = {
    "1998_1_29": ("m", "1-1 na prorrogação e 5-5 nos pênaltis; o estádio de Cheonan não tinha refletores para seguir com as "
                       "cobranças e o jogo foi decidido no sorteio, que o Chunan Ilhwa Chunma (Seongnam FC) ganhou (Wikipédia em "
                       "coreano, 1998년 K리그 e 1998년 K리그의 경기 결과; RSSSF: \"5TK5\", e a tabela dá a vitória ao Chunan)"),
}

# observação na classificação final: saídas da liga que não foram rebaixamento comum (antes de 2012 não havia queda)
OBS_CLASSIFICACAO = {
    (1984, "Kookmin Bank"): "saiu da liga depois de 1984 (time amador de banco)",
    (1985, "Hallelujah FC"): "saiu da liga depois de 1985 (virou amador)",
    (1985, "Sangmu"): "saiu da liga depois de 1985 (time do Exército)",
    (1986, "Hanil Bank"): "saiu da liga depois de 1986 (time amador de banco)",
    (1994, "Chonbuk Buffalo"): "fechou no fim de 1994",
    (2010, "Gwangju Sangmu"): "o time do Exército mudou para Sangju em 2011 (Sangju Sangmu, outro código na K League)",
    (2012, "Sangju Sangmu"): "rebaixado por decisão da liga (o time do Exército não cumpria as regras de clube); abandonou "
                             "o resto da temporada (14 derrotas por W.O.)",
    (2020, "Sangju Sangmu"): "rebaixado por decisão da liga: o time do Exército mudou para Gimcheon e recomeçou na K League 2 "
                             "(Gimcheon Sangmu, outro código na K League)",
}

# jogos decididos fora de campo: placar oficial (gm_of, gv_of); os autores de campo vão para o gols_texto
AWD = {
    "1996_1_111": {"esp": "awd", "gm_of": 3, "gv_of": 0, "campo": "1-1, parado aos 68'",
                   "motivo": "o Suwon Samsung escalou um estrangeiro a mais que o permitido; o jogo parou aos 68' com 1-1 e a K "
                             "League deu 3-0 ao Pohang (\"수원 삼성 몰수패\"; RSSSF e Wikipédia em coreano, 1996년 K리그의 "
                             "경기 결과); o portal registra 1-0, só com o gol do Hwang Seon-hong"},
    "2021_1_176": {"esp": "awd", "gm_of": 0, "gv_of": 3, "campo": "1-1",
                   "motivo": "o Gwangju FC fez mais substituições que o permitido; a K League deu 3-0 ao Jeju United (\"교체 "
                             "횟수 초과\", News1, 24/09/2021; Wikipédia em inglês e em coreano; o site oficial dá 0-3)"},
}
