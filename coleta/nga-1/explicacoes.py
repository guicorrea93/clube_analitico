"""Correções e explicações da coleta da 1ª divisão nigeriana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
# linhas da tabela em que vitórias + empates + derrotas não dão o número de jogos (a linha não era lida); os pontos (3 por
# vitória, 2 por empate com gols e 1 por empate sem gols) dizem qual número está errado
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("nig92", 29): ("30 7 11 14", "30 7 11 12", "Bendel United: 7+11+14 não dá 30 jogos; 33 pontos fecham com 7 vitórias e "
                    "11 empates, logo 12 derrotas"),
    ("nig94", 22): ("32  13  12   6", "32  13  12   7", "Berger: 13+12+6 não dá 32 jogos; 58 pontos fecham com 13 vitórias "
                    "e 12 empates, logo 7 derrotas"),
    ("nig96", 24): ("34  15   5  15", "34  15   5  14", "Nationale: 15+5+15 não dá 34 jogos; 50 pontos fecham com 15 vitórias "
                    "e 5 empates, logo 14 derrotas"),
    ("nig02", 25): ("34 14  4 15", "34 14  4 16", "Lobi Stars: 14+4+15 não dá 34 jogos; 46 pontos fecham com 14 vitórias "
                    "e 4 empates, logo 16 derrotas"),
    ("nig02", 453): ("34 14  4 15", "34 14  4 16", "Lobi Stars (a tabela repetida no fim da temporada): o mesmo erro"),
    # notas com números que o leitor tomava por placar
    ("nig02", 128): ("Rounds 6-9 missing", "Rounds 6 to 9 missing", "nota (\"rodadas 6 a 9 faltam\"), não é jogo"),
    ("nig09", 646): ("following a 13-0 win", "following a 13 to 0 win", "nota sobre a temporada anterior, não é jogo"),
}
_R2005 = "a rodada 20 de julho foi anulada e jogada de novo em novembro (\"Replay Round 20\"); vale o jogo de novembro"
CORRIGE: dict[tuple[str, str], dict] = {
    **{("2005", f"nig05:{n}"): {"esp": "anulado", "motivo": _R2005} for n in (323, 324, 325, 326, 327, 329, 330)},
    ("2005", "nig05:448"): {"esp": "abd", "nota": "abandonado com 1-1 (os oficiais foram ameaçados com uma arma); o 0-2 dado "
                                                  "ao Sharks foi revogado e o jogo, repetido em 16/11 (0-4)",
                            "motivo": "o 0-2 dado foi revogado (\"later revoked\") e o jogo repetido em 16/11"},
    ("2006", "nig06:353"): {"oficial": (0, 3), "nota": "0-3 dado ao Kano Pillars: o Ranchers Bees não compareceu",
                            "motivo": "\"n/p\" na página, mas com \"awarded 0-3; Ranchers Bees dns\": o resultado dado vale"},
    ("2023/24", "nig2024:435"): {"esp": "", "nota": "",
                                 "motivo": "a nota (\"... committee annulled a change of decision ...\") é do Enyimba x Doma "
                                           "United, na linha de cima; o jogo vale (as tabelas da RSSSF e da Wikipédia o contam)"},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {
    "2016": ("Giwa", "Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados"),
}
TABELAS_FORA: dict[tuple[str, str], str] = {
    ("2016", "nig2016:43"): "campanha do clube expulso até a expulsão (\"record at expulsion\"), não é tabela da edição",
    ("2016", "nig2016:636"): "campanha do clube expulso até a expulsão (repetida no fim da página)",
}
_OGOL = ("os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve "
         "trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é "
         "a tabela publicada")
_PUNICAO = ("punição de 3 pontos e 3 gols (\"3 points and 3 goals deducted\"): a tabela desconta os gols, os jogos não; a "
            "classificação é a tabela publicada")
EXPLICACOES: dict[str, list[str]] = {
    **{t: [_OGOL] for t in ("2009/10", "2010/11", "2011/12")},
    "2005": ["a rodada 20 de julho foi anulada e jogada de novo em novembro; Gateway x Sharks de setembro (0-2 dado e depois "
             "revogado) foi repetido em novembro"],
    "2019": ["o Delta Force tem só 11 dos 22 jogos na página; a classificação é a tabela publicada"],
    "2019/20": ["temporada abandonada (Covid-19); a página só traz parte dos jogos; no meio da temporada o Delta Force vendeu "
                "a vaga ao Akwa Starlets"],
    "2023": ["Bayelsa United com 3 gols a mais nos jogos que na tabela (a Wikipédia confirma a tabela); nenhum placar mudado"],
    "2023/24": ["Gombe United: " + _PUNICAO + " (duas vezes)"],
    "2024/25": ["Plateau United com 3 gols a mais nos jogos que na tabela (provável punição como as de 2023/24 e 2025/26)"],
    "2025/26": ["Kano Pillars e Kwara United: " + _PUNICAO],
}
