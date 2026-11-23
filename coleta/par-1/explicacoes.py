"""Correções e explicações da coleta da 1ª divisão paraguaia, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
_NOTA05 = "nota quebrada em três linhas (o fim dela ia para o jogo seguinte e o placar de campo para os autores) (PY-029)"
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("para05", 572): ("[awarded to Libertad; originally", "[awarded to Libertad; originally 2-1, Gral. Caballero used suspended player]",
                      _NOTA05),
    ("para05", 573): ("]      2-1, Gral. Caballero", "]", _NOTA05),
    ("para05", 574): ("used suspended player]", "", _NOTA05),
}
CORRIGE: dict[tuple[str, str], dict] = {
    ("2005", "para05:572"): {"esp": "wo_v", "gm": 2, "gv": 1, "motivo": "General Caballero 2-1 em campo; pontos para o Libertad "
                                                                  "(jogador suspenso); a tabela conta os gols de campo (PY-029)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {}
