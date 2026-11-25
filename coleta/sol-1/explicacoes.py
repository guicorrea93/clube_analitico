"""Correções e decisões da coleta das Ilhas Salomão (sol-1), sempre com o motivo.

- CONSERTA_TEXTO: (página, linha) -> (trecho, troca, motivo): erro de digitação da página corrigido antes da leitura;
- CORRIGE: (página, linha[, mandante, visitante]) -> ({campo: valor}, motivo), ou None para descartar o jogo;
- TERCEIROS: temporada -> (3º colocado, motivo), quando a disputa do 3º lugar não tem placar na página;
- TABELAS_FORA: (página, linha) das tabelas que não são da edição (ou que não servem de conferência);
- EXPLICACOES: temporada -> texto das divergências que ficam (erro da própria página).
"""
from __future__ import annotations

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("solom07", 85): ("Koloale  FC", "Koloale FC", "espaço duplo no meio do nome (o leitor lia só \"FC\")"),
    **{("solom2013", n): ("-.Marist", "9.Marist", "o desclassificado vem sem posição (\"-.\") e o leitor pulava a linha")
       for n in (32, 133, 208)},
    **{("solom2013", n): ("disqualified; playing record;      4   1  2  1   2- 2   5",
                          "[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]",
                          "a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela")
       for n in (33, 134, 209)},
    # 2009/10: a nota do jogo da linha 86 continua à direita dos três jogos de baixo
    ("solom2010", 86): ("[awarded to Rendova Devon as",
                        "[awarded to Rendova Devon as Northern United used Koloale players who had not been released]",
                        "a nota continua nas três linhas de baixo, ao lado de outros jogos"),
    ("solom2010", 87): ("Northern United used Koloale", "", "pedaço da nota do jogo de cima"),
    ("solom2010", 88): ("players who had not been", "", "pedaço da nota do jogo de cima"),
    ("solom2010", 89): ("released]", "", "fim da nota do jogo de cima"),
    # 2010/11: a nota do jogo da linha 69 continua ao lado da data e do jogo de baixo
    ("solom2011", 69): ("[awarded 0-3; originally 3-1;", "[awarded 0-3; originally 3-1; KOSSA used an unregistered player]",
                        "a nota continua nas duas linhas de baixo"),
    ("solom2011", 70): ("KOSSA used an unregistered", "", "pedaço da nota do jogo de cima, ao lado da data"),
    ("solom2011", 71): ("player]", "", "fim da nota do jogo de cima"),
    # 2025: a nota do jogo da linha 215 continua em duas linhas e esconde o "Round 17"
    ("solom2025", 215): ("[match postponed on Sep 28 due to weather",
                         "[match postponed on Sep 28 due to weather conditions and not refixtured but awarded as 0-0 in the "
                         "standings]", "a nota continua nas duas linhas de baixo"),
    ("solom2025", 216): ("conditions and not refixtured but awarded", "", "pedaço da nota do jogo de cima"),
    ("solom2025", 217): ("as 0-0 in the standings]", "", "fim da nota do jogo de cima, ao lado do \"Round 17\""),
}

CORRIGE: dict[tuple, tuple[dict, str] | None] = {
    ("solom04", 28): ({"especial": "wo_m"}, "final por W.O.: o Makuru, de dono adventista, não joga aos sábados"),
    ("solom2010", 86): ({"especial": "wo_v"}, "5-1 em campo, mas os pontos foram dados ao Rendova Devon (o Northern United usou "
                                              "jogadores do Koloale que não tinham sido liberados); a tabela conta vitória sem gols"),
    ("solom06", 82): ({}, "semifinal abandonada (chuva forte) e jogada de novo em 01/03 (Koloale 2-1)"),
    ("solom09", 80): ({"gm": 3, "gv": 2}, "abandonado aos 72' com 3-2 (briga na torcida); não entra na tabela"),
    ("solom2025", 108): ({}, "abandonado aos 24' (chuva forte) e jogado de novo no dia seguinte (Malaita Kingz 1-0)"),
}

TERCEIROS: dict[str, tuple[str, str]] = {
    "2015/16": ("KOSSA", "a disputa do 3º lugar está na página como \"KOSSA bt Solomon Warriors\" (vitória, placar desconhecido)"),
}

TABELAS_FORA: dict[tuple[str, int], str] = {}

EXPLICACOES: dict[str, str] = {
    "2005/06": "seis jogos da fase de grupos estão na página sem placar (\"drw\" e \"bt\": Tematangi x Mafi, Tematangi x "
               "Kuara, Camp United x Ngaube, Marist x Kuara, Koloale x Camp United, Aimela x Ngaube); as tabelas os contam e eles "
               "ficam de fora dos jogos (a página avisa: \"missing goals of various matches\")",
    "2006/07": "a tabela do grupo A é de antes da última rodada (Koloale 2-1 Marist vem depois dela), e os jogos com \"-\" "
               "(sem placar) não estão em nenhuma das duas",
    "2009/10": "um jogo do grupo B está na página só como vitória sem placar (\"Rendova Devon bt Ka'arua\"); a tabela o conta "
               "(\"w/o goals\") e ele fica de fora dos jogos",
    "2010/11": "os 4 jogos da 12ª rodada estão na página só com o resultado, sem placar (\"drw\", \"lt\"); a tabela os conta "
               "(\"w/o goals round 12\") e eles ficam de fora dos jogos",
}
