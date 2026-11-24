"""Correções e explicações da coleta da 1ª divisão sul-africana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
# linhas da tabela em que vitórias + empates + derrotas não dão o número de jogos (a linha não era lida e a tabela se
# partia); os pontos (2 por vitória) dizem qual número está errado
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("zaf82", 22): ("34  15  9  0", "34  15  9 10", "Arcadia: 15+9+0 não dá 34 jogos; 39 pontos = 15 vitórias e 9 "
                    "empates, logo 10 derrotas"),
    ("zaf82", 23): ("34  16  7  1", "34  16  7 11", "Dynamos: 16+7+1 não dá 34 jogos; 39 pontos = 16 vitórias e 7 "
                    "empates, logo 11 derrotas"),
    ("zaf86", 28): ("34   5  14  14", "34   5  14  15", "Durban City: 5+14+14 não dá 34 jogos; 24 pontos = 5 vitórias e "
                    "14 empates, logo 15 derrotas"),
    ("zaf93", 29): ("38  13 10 13", "38  13 10 15", "Witbank Aces: 13+10+13 não dá 38 jogos; 36 pontos = 13 vitórias e "
                    "10 empates, logo 15 derrotas"),
    ("zaf93", 356): ("38  13  10  13", "38  13  10  15", "Witbank Aces (a tabela repetida no fim da temporada): o mesmo erro"),
}
CORRIGE: dict[tuple[str, str], dict] = {
    # a nota do resultado dado continua na linha de baixo ("... attacked the referee, awarded 1-0]") e o leitor não a pega
    ("2001/02", "zaf02:49"): {"oficial": (1, 0), "nota": "abandonado aos 85' com 1-0 (jogadores do Orlando Pirates "
                                                        "agrediram o árbitro); 1-0 dado ao Ajax Cape Town",
                              "motivo": "1-0 dado ao Ajax Cape Town (nota da página, na linha de baixo)"},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {
    "2024/25": ("Royal AM", "Royal AM excluído do campeonato; todos os seus resultados anulados (\"excluded; all results "
                            "annulled\")"),
}
TABELAS_FORA: dict[tuple[str, str], str] = {
    ("2024/25", "zaf2025:42"): "campanha do Royal AM até a exclusão (resultados anulados), não é tabela da edição",
    ("2024/25", "zaf2025:473"): "campanha do Royal AM até a exclusão (repetida no fim da página)",
}
EXPLICACOES: dict[str, list[str]] = {
    **{t: ["a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada"]
       for t in ("1987", "1992", "1993", "1996/97")},
    "1993": ["a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada",
             "quatro clubes mudaram de nome no meio da temporada (notas da página): Score Stars = Qwa Qwa Stars, Ratanang "
             "= Chatsworth Rangers, Albany City = Pretoria City, Highlands Park = Welkom Eagles"],
    "1999/00": ["a lista de jogos da página não fecha com a tabela em seis clubes (a Wikipédia confirma a tabela da RSSSF); "
                "nenhum placar foi mudado e o relatório aponta o jogo provável"],
    "2001/02": ["Ajax Cape Town x Orlando Pirates: abandonado aos 85' com 1-0 e dado ao Ajax Cape Town por 1-0 (nota da "
                "página)"],
    "2007/08": ["o Benoni Premier United mudou de nome para Thanda Royal Zulu no meio da temporada: é um clube só"],
    "2024/25": ["o Royal AM foi excluído e todos os seus resultados anulados; o Cape Town City perdeu o desempate de "
                "acesso"],
}
