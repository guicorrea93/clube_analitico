"""Correções e decisões da coleta do Taiti (tah-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}

CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    ("tahiti71", 159): ({"especial": "anulado"}, "resultado não homologado por erro do árbitro; o jogo foi repetido (0-6)"),
    ("tahiti2022", 99): ({"especial": "derrota_ambos"}, "a federação deu derrota aos dois clubes (\"awarded 0-0 loss to both\"); "
                         "em campo, 3-0"),
}

TABELAS_FORA: dict[tuple[str, int], str] = {
    ("tahiti01", 36): "tabela depois de 6 rodadas (2000/01)",
    ("tahiti01", 75): "tabela depois de 14 rodadas (2000/01); a final não está na página",
}

EXPLICACOES: dict[str, str] = {}
