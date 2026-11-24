"""Correções e decisões da coleta da Nova Caledônia (ncl-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}

CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    ("newcal03", 194): ({"gv": 9}, "a página traz Olympique 1-0 AS Magenta, mas a tabela da mesma página dá vitória do Magenta e 9 "
                        "gols a mais para ele (e sofridos pelo Olympique): só este jogo explica (o outro entre os dois foi 3-0 para "
                        "o Magenta); placar provável 1-9"),
    ("newcal08", 49): ({"especial": "wo_v", "gm": 1, "gv": 1, "gols_contam": True},
                       "vitória dada ao Kirikitr (o Mont-Dore escalou jogador suspenso); em campo, 1-1, e a tabela conta esses gols"),
    ("newcal2011", 139): ({"especial": "wo_m", "gm": 0, "gv": 4}, "vitória dada ao Hienghène sem gols (\"awarded 0-0 win\"); "
                          "em campo, 0-4"),
}

TABELAS_FORA: dict[tuple[str, int], str] = {
    ("newcal09", 68): "tabela do playoff com os resultados de campo (antes da decisão da comissão que deu o jogo ao Lössi)",
}

EXPLICACOES: dict[str, str] = {
    "2004/05": "Grande Terre: dois jogos só com o vencedor na página (ACB Poya \"bt\" ASLN Kouaoua, AS Poum \"bt\" CA "
               "Saint-Louis), que ficam de fora; falta também um jogo USC Nouméa x ASLN Kouaoua (3-2 pela tabela) e o JS Baco tem "
               "um gol a mais a favor e contra; a classificação é a tabela da página",
    "2013": "AS Lössi x AS Mont-Dore só com \"drw\" (empate sem placar) na página: fica de fora; a tabela conta o empate",
    "2015": "jogos sem placar na página (Gaïtcha \"drw\" Lössi; Auteuil \"lt\" Baco, \"by 1 goal\") ficam de fora; a tabela é a "
            "de antes das punições do fim da temporada e conta o 2-2 de campo de Lössi x Gaïtcha (dado 3-0 ao Lössi); a "
            "classificação é essa tabela",
    "2018": "um gol de diferença: o Trio Kedeigne tem um gol a mais a favor e o SC Ne Drehu um a mais contra na tabela do que "
            "nos jogos entre os dois (1-3 e 5-1); não dá para saber em qual; fica o placar da página",
}
