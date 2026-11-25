"""Correções e explicações da coleta da 1ª divisão ganesa, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {
    # 2009/10: a página da RSSSF não traz o returno Asante Kotoko x New Edubiase; o ogol traz, e com ele a tabela fecha
    "2009/10": [{"mandante": "Asante Kotoko", "visitante": "New Edubiase United", "gm": 2, "gv": 0, "data": "2010-03-03",
                 "base": "ogol", "fonte_id": "ogol:1353495",
                 "obs": "jogo que falta na página da RSSSF (vem do ogol; a tabela da RSSSF só fecha com ele)"}],
}
# linhas da tabela em que vitórias + empates + derrotas não dão o número de jogos (a linha não era lida e a tabela se
# partia); os pontos (2 por vitória até 1986/87, 3 depois) dizem qual número está errado
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("ghahist", 279): ("27  11  7 10", "27  11  7  9", "Venomous Vipers: 11+7+10 não dá 27 jogos; 29 pontos = 11 vitórias e 7 empates, logo 9 derrotas"),
    ("ghahist", 493): ("38  17  5 15", "38  17  5 16", "Bofoakwa: 17+5+15 não dá 38 jogos; 39 pontos = 17 vitórias e 5 empates, logo 16 derrotas"),
    ("ghahist", 516): ("21   8  5  9", "21   8  5  8", "Great Olympics: 8+5+9 não dá 21 jogos; 21 pontos = 8 vitórias e 5 empates, logo 8 derrotas"),
    ("ghahist", 588): ("34   5  9 17", "34   8  9 17", "Susu Biribi: 5+9+17 não dá 34 jogos; 25 pontos e 9 empates dão 8 vitórias"),
    ("ghahist", 634): ("15   2  5  7", "15   2  5  8", "Brong Ahafo United: 2+5+7 não dá 15 jogos; 9 pontos = 2 vitórias e 5 empates, logo 8 derrotas"),
    ("ghahist", 717): ("22  15  2  2", "22  15  5  2", "Asante Kotoko: 15+2+2 não dá 22 jogos; 35 pontos e 15 vitórias dão 5 empates"),
    ("gha09", 54): ("30 10 10 13", "30 10  7 13", "AshantiGold: 10+10+13 não dá 30 jogos; 37 pontos e 10 vitórias dão 7 empates"),
    ("gha09", 418): ("30 10 10 13", "30 10  7 13", "AshantiGold (a tabela repetida no fim da página): o mesmo erro"),
}
# 2003: a tabela conta oito jogos como resultado dado ("the table above has the following eight matches counted as
# awarded"); a nota que os lista (linhas 41 a 48, repetida em 436 a 443) era lida como jogos
_N2003 = "linha da nota sobre os resultados dados (não é jogo)"
_A2003 = "resultado dado que a tabela conta (nota da página: \"counted as awarded\")"
CORRIGE: dict[tuple[str, str], dict] = {
    **{("2003", f"gha03:{n}"): {"descartar": True, "motivo": _N2003} for n in (41, 42, 43, 44, 45, 436, 437, 438, 439, 440)},
    **{("2003", f"gha03:{n}"): {"oficial": placar, "nota": f"{placar[0]}-{placar[1]} dado ({campo} em campo)", "motivo": _A2003}
       for n, placar, campo in ((69, (0, 3), "1-0"), (91, (0, 3), "1-0; revogado?"), (103, (0, 3), "1-0"),
                                (123, (3, 0), "1-1"), (144, (0, 3), "4-0"), (199, (0, 3), "3-1"), (282, (3, 0), "1-1"),
                                (308, (0, 3), "1-1"))},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_LISTA = ("a lista de jogos da página não fecha com a tabela em dois clubes (sem terceira fonte); nenhum placar foi mudado "
          "e o relatório aponta o jogo provável")
EXPLICACOES: dict[str, list[str]] = {
    "1999": [_LISTA], "2000": [_LISTA],
    "2003": ["a tabela conta oito resultados dados (nota da página) e um desconto de 3 pontos de quem perdeu cada decisão; os "
             "jogos ficam com o placar dado e o de campo na observação"],
    "2004/05": ["dois grupos, jogo do título (Hearts of Oak 1-0 Asante Kotoko, abril de 2005), 3º lugar e desempate do "
                "rebaixamento"],
    "2009/10": ["o returno Asante Kotoko x New Edubiase vem do ogol (falta na página da RSSSF)"],
    "2010/11": ["os jogos vêm do ogol e não fecham com a tabela da RSSSF em sete clubes; nenhum placar foi mudado e a "
                "classificação é a tabela publicada"],
    "2015": ["Asante Kotoko com 3 gols a mais nos jogos que na tabela (provável punição de gols, como as da Nigéria); "
             "nenhum placar mudado"],
}
