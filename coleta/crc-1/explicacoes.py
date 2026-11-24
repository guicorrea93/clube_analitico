"""Correções e explicações da coleta da 1ª divisão da Costa Rica, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1999/00", "cos00:123"): {"esp": "", "motivo": "San Carlos x Limonense interrompido em 17/10 (1-0, mau tempo) e jogado de "
                                                    "novo: 1-1, o placar que vale (a tabela conta o jogo); o San Carlos x Limonense "
                                                    "da linha 442 é o do 2º turno, não a repetição"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "2002/03": ["San Carlos x Herediano (21ª rodada do Clausura) foi dado como derrota sem gols para os dois clubes; o banco não "
                "tem como registrar isso no jogo (fica sem placar), e a tabela publicada conta uma derrota a mais para cada um"],
    "2003/04": ["falta um Pérez Zeledón x Carmelita no Apertura (a página só tem o jogo de ida, 3-0); pela tabela, a volta foi "
                "empate 1-1"],
}
