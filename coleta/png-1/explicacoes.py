"""Correções e decisões da coleta de Papua-Nova Guiné (png-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TERCEIROS: temporada -> (3º colocado, motivo), quando a disputa do 3º lugar não tem placar na página;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("png2014", 89): ("[abandoned at 1-0 in 89' due to", "[abandoned at 1-0 in 89' due to crowd trouble]",
                      "a nota continua na linha de baixo, ao lado do jogo seguinte"),
    ("png2014", 90): ("crowd trouble]", "", "o fim da nota de cima (não é nota deste jogo)"),
}
_AMBOS = ("jogo não disputado: a federação deu derrota por 0-3 aos dois clubes (\"awarded 0-3 against both clubs\"; a tabela "
          "da página conta os 3 gols contra para cada um)")
CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    ("png2018", 95): ({"especial": "derrota_ambos", "gc_ambos": 3}, _AMBOS),
    ("png2018", 146): ({"especial": "derrota_ambos", "gc_ambos": 3}, _AMBOS),
    ("png06", 171): ({"gm": 0, "gv": 0},
                     "semifinal abandonada com 0-0 por falta de luz e jogada de novo no dia seguinte (5-6 na prorrogação)"),
    ("png06", 174): ({"nota": "aet; jogo repetido (o de 18/11 foi abandonado com 0-0 por falta de luz)"},
                     "nota da página (\"[aet] [replay]\") reescrita"),
    ("png2014", 89): ({"gm": 1, "gv": 0}, "abandonado aos 89' com 1-0 (briga na torcida); não foi jogado de novo nem entrou na tabela"),
    ("png2019", 471): ({"gm": 0, "gv": 0}, "quartas de final abandonadas aos 48' com 0-0 (campo alagado) e jogadas de novo em 16/05"),
    ("png2022", 88): ({"gm": 2, "gv": 0}, "abandonado aos 57' com 2-0 (falta de luz) e jogado de novo em 23/11 (4-2)"),
    ("png2025", 291): ({"especial": "wo_m"}, "o Hekari United não se apresentou (\"dns\"): W.O. para o Lae City, 3º lugar"),
    ("png2014", 152): ({"gm": 0, "gv": 3, "especial": ""},
                       "a final foi abandonada aos 70' com 0-3 (violência da torcida); o resultado ficou e o Hekari United "
                       "foi o campeão (lista de campeões da RSSSF)"),
}

# 3º lugar de jogo que a página dá sem placar ("bt" = venceu): o jogo fica de fora, o 3º entra na classificação
TERCEIROS: dict[str, tuple[str, str]] = {
    "2014": ("Morobe United", "a disputa do 3º lugar está na página como \"Gigira Laitepo Morobe bt Oro [aet]\" (vitória na "
                              "prorrogação, placar desconhecido)"),
}

TABELAS_FORA: dict[tuple[str, int], str] = {
    ("png2023", 133): "tabela depois da 11ª rodada (a final vem no fim da fase)",
}

EXPLICACOES: dict[str, str] = {
    "2023": "dois jogos da 12ª rodada (United Highlands x Lae City e Lae City Dwellers x Morobe Wawens, este abandonado no 2º "
            "tempo) estão na página como empate sem placar (\"drw\"); a tabela os conta como empates e eles ficam de fora dos jogos",
    "2025": "um jogo remarcado da 15ª rodada (Morobe Wawens x Hekari United, 1-0 no intervalo) está na página como empate sem placar; a tabela o "
            "conta como empate e ele fica de fora dos jogos",
    "2026": "dois jogos do Lae City (Lae City Dwellers x Lae City, 17ª rodada, \"possivelmente 1-3\"; Finschhafen Bavarians x Lae "
            "City, 18ª) estão na página só como derrota do mandante, sem placar (\"lt\"); a tabela os conta e eles ficam de fora dos jogos",
}
