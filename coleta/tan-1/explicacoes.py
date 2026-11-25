"""Correções e explicações da coleta da 1ª divisão tanzaniana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
_PRISONS = "Prisons: 10+12+7 não dá 30 jogos; 42 pontos = 10 vitórias e 12 empates, logo 8 derrotas"
_BANDARI = "Bandari: 6+12+13 não dá 30 jogos; 30 pontos = 6 vitórias e 12 empates, logo 12 derrotas"
_MJI = "Mji: 10+2+10 não dá 20 jogos; 32 pontos = 10 vitórias e 2 empates, logo 8 derrotas"
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("tanz01", 45): ("20 10  2 10", "20 10  2  8", _MJI),
    ("tanz01", 510): ("20 10  2 10", "20 10  2  8", _MJI + " (a segunda cópia da tabela)"),
    ("tanz06", 21): ("30 10 12  7", "30 10 12  8", _PRISONS),
    ("tanz06", 31): ("30  6 12 13", "30  6 12 12", _BANDARI),
    ("tanz06", 397): ("30 10 12  7", "30 10 12  8", _PRISONS + " (a segunda cópia da tabela)"),
    ("tanz06", 407): ("30  6 12 13", "30  6 12 12", _BANDARI + " (a segunda cópia da tabela)"),
}
CORRIGE: dict[tuple[str, str], dict] = {
    **{("2004", f"tanz04:{n}"): {"descartar": True, "motivo": "nota sobre os gols do Moro United, do Mji e do Kahama "
                                  "(\"Moro 16-9 goals; Mji 6-11 goals; Kahama 8-7 goals\"), lida como jogo"} for n in (61, 491)},
    ("1999", "tanz99:168"): {"oficial": None, "nota": "",
                             "motivo": "a nota diz que o jogo ainda podia ser dado ao Young Africans (\"may yet be "
                             "awarded 2-0\"), mas a tabela conta o 1-1 de campo"},
    ("1999", "tanz99:414"): {"oficial": (2, 0), "nota": "abandonado aos 78' com 2-0",
                             "motivo": "\"abandoned in 78' at 2-0; awarded 2-0\": não é abandono sem valer; a tabela "
                             "conta o jogo"},
    ("2000", "tanz00:71:4"): {"oficial": (0, 2), "nota": "o Mji não compareceu",
                              "motivo": "\"Mji vs Mtibwa awarded 0-2, Mji dns\""},
    ("2000", "tanz00:39:1"): {"oficial": (2, 0), "nota": "abandonado aos 89' com 2-1",
                              "motivo": "\"Tukuyu-Majimaji abandoned at 2-1 in 89', awarded 2-0\""},
}
# clube que desistiu ou foi excluído: (clube, motivo), ou uma lista deles
ANULA_CLUBE: dict[str, tuple[str, str] | list[tuple[str, str]]] = {
    "2001": ("Kagera Stars", "o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados"),
    "2004": [("Reli Kigoma", "o Reli foi desclassificado em 5/7; a campanha foi anulada"),
             ("Kariakoo", "o Kariakoo foi desclassificado em 5/7; a campanha foi anulada"),
             ("Pallsons", "o Pallsons desistiu em 3/6; a campanha foi anulada")],
}
_ANULADA = "linha da campanha anulada de um clube excluído (não conta na classificação)"
_PARCIAL_DO_ANO = "tabela do meio da temporada (a final vem depois)"
TABELAS_FORA: dict[tuple[str, str], str] = {
    **{("2001", f"tanz01:{n}"): _ANULADA for n in (35, 500)},
    **{("2004", f"tanz04:{n}"): _ANULADA for n in (31, 51, 53, 461, 481, 483)},
    **{("2005", f"tanz05:{n}"): _PARCIAL_DO_ANO for n in (347, 352, 355, 454, 461)},
}
EXPLICACOES: dict[str, list[str]] = {}
