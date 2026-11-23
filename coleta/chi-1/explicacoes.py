"""Correções e explicações da coleta da 1ª divisão chilena, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
_TROCA = "clube trocado na rodada (um clube aparece duas vezes, o outro nenhuma); com a troca a tabela publicada fecha (CH-002)"
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("chile44", 167): ("Everton                 0-2 Santiago Morning", "Everton                 0-2 Universidad Católica", _TROCA),
    ("chile43", 186): ("Audax Italiano          3-4 Santiago Morning", "Audax Italiano          3-4 Badminton", _TROCA),
    ("chile53", 198): ("Magallanes              1-1 Rangers", "Unión Española          1-1 Rangers", _TROCA),
    ("chile72", 214): ("Universidad Católica    2-0 Unión San Felipe", "Unión Española          2-0 Unión San Felipe", _TROCA),
    ("chiletops", 16): ("Costa Rica Audax", "Costa Rica  Audax", "um espaço só entre o país e o clube: a linha não era lida (CH-018)"),
    ("chiletops", 17): ("Costa Rica Audax", "Costa Rica  Audax", "um espaço só entre o país e o clube (CH-018)"),
}
_TM = "o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)"
CORRIGE: dict[tuple[str, str], dict] = {
    ("1990", "ogol:5257815"): {"gm": 2, "gv": 1, "motivo": "Universidad Católica 2-1 Everton: " + _TM},
    ("1990", "ogol:5257902"): {"gm": 1, "gv": 1, "motivo": "Unión Española 1-1 La Serena: " + _TM},
    ("1990", "ogol:5257949"): {"gm": 0, "gv": 0, "motivo": "Huachipato 0-0 Palestino: " + _TM},
    ("1991", "ogol:5249721"): {"gm": 4, "gv": 2, "motivo": "O'Higgins 4-2 Deportes Concepción: " + _TM},
    ("1993", "ogol:5247516"): {"gm": 2, "gv": 1, "motivo": "Everton 2-1 Unión Española: " + _TM},
    ("1994", "ogol:5241920"): {"gm": 1, "gv": 0, "motivo": "Universidad Católica 1-0 Universidad de Chile: " + _TM},
    ("1995", "ogol:5237549"): {"gm": 2, "gv": 0, "motivo": "Palestino 2-0 La Serena: " + _TM},
    ("1988", "ogol:5293713"): {"m": "Naval de Talcahuano", "v": "O'Higgins", "gm": 1, "gv": 1,
                               "motivo": "o ogol repete O'Higgins 0-2 Naval; o jogo que falta é Naval 1-1 O'Higgins (CH-014)"},
    ("2011 Apertura", "chile2011:67"): {"esp": "", "gm": 2, "gv": 0,
                                       "motivo": "Ñublense 2-0 Wanderers: a decisão do tribunal foi revogada (\"award revoked\") (CH-015)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1984": ["duas zonas (Norte e Sul) de 13 clubes e um quadrangular final. As tabelas das zonas (chilehist.html) dão 26 jogos "
             "por clube: os 24 da zona e 2 interzonais. O calendário do ogol, a base deste ano, não tem os 26 jogos "
             "interzonais; nenhuma outra fonte que baixamos os traz. A classificação é calculada com os jogos que há"],
    "1999": ["o octogonal final (\"Championship Playoff\") somou aos clubes um quarto dos pontos e todos os gols da 1ª fase: "
             "a tabela publicada mostra esses gols acumulados. Vitórias, empates e derrotas fecham com os jogos"],
}
