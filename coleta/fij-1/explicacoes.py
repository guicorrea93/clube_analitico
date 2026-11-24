"""Correções e decisões da coleta de Fiji (fij-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}

CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    # 2000: a página não sabe o adversário ("Tavua/Lautoka" = Tavua ou Lautoka): os três jogos ficam de fora
    ("fiji00", 56): None, ("fiji00", 57): None, ("fiji00", 167): None, ("fiji00", 168): None,
    ("fiji09", 134): ({"gm_of": None, "gv_of": None, "especial": ""}, "a página traz Tavua 1-1 Labasa \"possibly awarded 2-0\"; a "
                      "tabela conta o empate"),
    ("fiji2010", 228): ({"gm_of": None, "gv_of": None, "especial": ""}, "Lautoka 1-1 Rewa: dado 2-0 ao Lautoka em 11/03/2011 e "
                        "revogado em 10/07/2011 (o título voltou ao Ba); vale o 1-1, que é o que a tabela conta"),
}

TABELAS_FORA: dict[tuple[str, int], str] = {
    ("fiji2025", 128): "tabela do meio da temporada (\"Hakfway Table\", com erro de digitação)",
}

EXPLICACOES: dict[str, str] = {
    "2005": "grupo do rebaixamento (Pepsi 4): três jogos só com \"drw\" (empate sem placar) na página ficam de fora; a tabela "
            "conta os empates",
}
