"""Correções e explicações da coleta da 1ª divisão chilena, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1984": ["duas zonas (Norte e Sul) de 13 clubes e um quadrangular final. As tabelas das zonas (chilehist.html) dão 26 jogos "
             "por clube: os 24 da zona e 2 interzonais. O calendário do ogol, a base deste ano, não tem os 26 jogos "
             "interzonais; nenhuma outra fonte que baixamos os traz. A classificação é calculada com os jogos que há"],
    "1999": ["o octogonal final (\"Championship Playoff\") somou aos clubes um quarto dos pontos e todos os gols da 1ª fase: "
             "a tabela publicada mostra esses gols acumulados. Vitórias, empates e derrotas fecham com os jogos"],
}
