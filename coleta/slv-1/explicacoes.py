"""Correções e explicações da coleta da 1ª divisão de El Salvador, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("elsal05", 379): ("once Municipal 0-3", "Once Municipal 0-3", "inicial minúscula no nome do mandante: o leitor não lia a "
                                                                    "linha como jogo (e a tabela fecha com ele)"),
}
CORRIGE: dict[tuple[str, str], dict] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "2002 Clausura": ["Atlético Balboa: os jogos da página somam 25 gols sofridos, a tabela publicada diz 24 (um placar da "
                      "página ou a tabela tem um gol a mais; fica como a página)"],
}
