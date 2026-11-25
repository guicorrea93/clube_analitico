"""Correções e explicações da coleta da 1ª divisão do Panamá, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("panama97", 242): ("San Francisco, Euro 5-4 on pen", "San Francisco  [Eurokickers 5-4 pen]",
                        "os pênaltis vinham colados ao nome do visitante; viram nota (o leitor lia \"San Francisco, Euro 5-4 on pen\" "
                        "como clube)"),
}
CORRIGE: dict[tuple[str, str], dict] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1997/98": ["dois jogos da primeira fase estão na página só com o resultado, sem placar (\"Pan A ppd Nacional [away win]\" "
                "e \"Ejecutivo - Chiriqui [draw]\"): ficam fora; a tabela publicada os conta (Atlético Nacional, Chiriquí, Pan de "
                "Azúcar e Ejecutivo com um jogo a menos nos jogos lidos)"],
    "2004 Apertura": ["Tauro: os jogos da página somam 26-12, a tabela publicada diz 25-11 (um placar com um gol a mais de cada "
                      "lado; fica como a página)"],
    "2008 Apertura": ["San Francisco e Plaza Amador: os jogos da página dão ao San Francisco um empate a menos e uma derrota a "
                      "mais, e ao Plaza Amador o contrário, do que a tabela publicada (com os mesmos gols); fica como a página"],
}
