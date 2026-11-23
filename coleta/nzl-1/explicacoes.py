"""Correções e decisões da coleta da Nova Zelândia (nzl-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- MATRIZ_NOME: nome da linha da matriz de resultados -> nome da tabela, quando a semelhança não basta;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("nz89", 35): ("4-0*2-1", "3-0 2-1", "Christchurch United x Manurewa: a matriz traz 4-0 com a nota \"other sources give "
                   "Christchurch vs Manurewa as 3-0\"; a tabela da página (e a da Wikipédia) conta 3-0 (o asterisco colado também "
                   "impedia a leitura da matriz)"),
}

MATRIZ_NOME: dict[str, str] = {
    "Mirmar Rangers": "Miramar",   # nz81: erro de digitação na matriz
}

CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    ("nz01", 322): None,   # "Final [8 Sep, 2:45 pm]": título lido como jogo (a hora parece placar)
    ("nz00", 137): ({"visitante": "Miramar"}, "a página põe \"Metro 0-4 Manawatu\", mas os quatro autores (Patrick, George, "
                    "Longley, Bernard) são do Miramar Rangers, e assim Manawatu e Miramar ficam com os 18 jogos da tabela"),
    ("nz97", 224): ({"gv": 0}, "Napier City Rovers 3-2 Waitakere City na página, sem autor dos gols do Waitakere; a tabela da "
                    "mesma página conta 3-0 (gols do Waitakere e sofridos do Napier 2 a menos)"),
    ("nz78", 34, "Hamilton", "Woolston"): ({"gm": 2}, "a matriz traz Hamilton 3-3 Woolston, mas a tabela da página (igual à da "
                                            "Wikipédia) dá derrota do Hamilton e vitória do Woolston, com um gol a menos do "
                                            "Hamilton: 2-3 (o outro jogo entre os dois, 0-3, não explica a diferença)"),
    ("nz82", 38, "Napier City Rovers", "Manurewa"): ({"gm_of": 0, "gv_of": 1, "especial": "awd"},
                                                     "1-1 em campo; o resultado virou 0-1 para o Manurewa porque o Napier escalou "
                                                     "jogador sem registro (Wikipédia, citando Hilton 1991); a tabela da página já "
                                                     "conta assim"),
    ("nz87", 172, "Mt Maunganui", "Christchurch Utd"): ({"gv": 2}, "a matriz traz 0-1; a lista da 5ª rodada, na mesma página, traz "
                                                         "0-2, e é o que a tabela conta (60 gols do Christchurch United)"),
    ("wikipedia", "2024", "Birkenhead United", "Auckland City"): (
        {"gm": 1, "gv": 3}, "a matriz da Wikipédia traz Birkenhead 3-1 Auckland City; a tabela da RSSSF e a da própria Wikipédia "
                            "contam vitória do Auckland City por 3-1 (placar invertido na matriz)"),
    ("nz07", 72): ({"especial": "wo_m", "gm": 0, "gv": 1}, "vitória dada ao Waitakere United sem gols (\"awarded 0-0 win\"); "
                   "em campo, 0-1 (o Auckland City escalou jogador irregular)"),
}

# ligas regionais cuja matriz de resultados da Wikipédia não serve (os jogos ficam de fora; a tabela da RSSSF fica)
WIKI_FORA: dict[tuple[str, str], str] = {
    ("2025", "Sul"): "a matriz da Southern League 2025 na Wikipédia tem só 9 dos 10 clubes da tabela (falta o University of "
                     "Canterbury); entram os jogos do ogol",
    ("2025", "Centro"): "a matriz da Central League 2025 na Wikipédia foi preenchida no começo da temporada (\"update=12 April "
                        "2025\") e não fecha nem com a tabela da própria página: 8 dos 10 clubes divergem",
}

TABELAS_FORA: dict[tuple[str, int], str] = {
    ("nz2021", 95): "tabela do meio da temporada (Halfway Table)",
}

_UM_GOL = ("um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): {x}; "
           "não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela")
EXPLICACOES: dict[str, str] = {
    "1973": _UM_GOL.format(x="o Wellington United tem um gol a mais contra o Eastern Suburbs (3-1 e 1-4)"),
    "1982": _UM_GOL.format(x="o Miramar Rangers tem um gol a mais contra o Christchurch United (0-2 e 1-3)"),
    "1988": _UM_GOL.format(x="um gol do Miramar Rangers aparece como do Manawatu United nos jogos entre os dois (1-2 e 2-3)"),
    "1990": _UM_GOL.format(x="o Waikato United tem um gol a mais contra o Waitakere City, e o Wellington United dois a mais a "
                             "favor e dois a mais contra"),
    "1991": _UM_GOL.format(x="o Manurewa tem um gol a mais contra o New Plymouth Rangers (2-0 e 1-1)"),
    "1992": "a tabela da RSSSF não fecha consigo mesma (581 gols pró x 580 contra) e erra os gols de 5 clubes; a da Wikipédia "
            "fecha com os jogos da matriz e é a usada na classificação",
    "1993": "fase nacional: a página traz Wellington Olympic 3-0 Christchurch Rangers e a tabela conta um gol do Rangers (3-1?); "
            "fica o placar da página",
    "2023": "Central League (jogos da matriz da Wikipédia): Wellington Olympic, Petone, Western Suburbs e Stop Out não fecham com "
            "a tabela da RSSSF, e a tabela da própria Wikipédia também difere da RSSSF (Wellington Olympic e Western Suburbs). As "
            "fontes discordam entre si; ficam os jogos da Wikipédia e a classificação é a tabela da RSSSF",
    "2024": "Central League: Wellington Phoenix Reserves x Waterside Karori (2-2 e 2-1 na matriz da Wikipédia) com 2 gols a menos "
            "para cada lado do que nas tabelas da RSSSF e da Wikipédia; Southern League: Ferrymead Bays com um gol a mais. Ficam "
            "os jogos da Wikipédia e a classificação é a tabela da RSSSF",
    "2025": "Central e Southern League pelo ogol (a matriz da Wikipédia não serve): falta 1 jogo da Central (Petone x Wellington "
            "Phoenix Reserves) e, na Southern, Coastal Spirit e Dunedin City Royals têm um jogo a mais e Nelson Suburbs e Wanaka "
            "um a menos; a classificação é a tabela da RSSSF",
}
