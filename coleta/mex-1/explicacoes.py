"""Correções e explicações da coleta da 1ª divisão mexicana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("mex77", 109): ("2.3", "2-3", "ponto no lugar do hífen no placar (U. de Curtidores 2-3 U. de G.); a tabela final fecha com 2-3"),
    ("mex02", 145): ("U.N.A.M:", "U.N.A.M ", "dois-pontos depois do nome do mandante (U.N.A.M. 5-0 Celaya)"),
    ("mex81", 1152): ("U.A.G   .", "U.A.G.   ", "ponto solto depois do nome do mandante (U.A.G. 0-0 Cruz Azul, grupo semifinal)"),
}
CORRIGE: dict[tuple[str, str], dict] = {
    ("2006 Apertura", "mex07:336"): {"descartar": True, "motivo": "Necaxa x Morelia suspenso aos 40' (1-1) e completado depois "
                                                                  "(os 50' restantes): fica só a linha da continuação, com o placar final"},
    ("2017 Apertura", "mex2018:289"): {"descartar": True, "motivo": "Monterrey x Santos suspenso aos 12' (0-0, tempestade) e "
                                                                    "completado em 9/11 (os 79' restantes): fica só a linha da "
                                                                    "continuação, com o placar final (1-1)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {
    ("1940/41", "mex41:283"): "tabela de campo, de antes da decisão de 5/2/1941 que deu ao Selección Jalisco, ao Atlante e ao "
                              "América os jogos contra o Asturias (jogador irregular); vale a tabela oficial logo abaixo",
}
EXPLICACOES: dict[str, list[str]] = {}
