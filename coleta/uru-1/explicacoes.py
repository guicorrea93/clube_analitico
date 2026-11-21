"""Correções e explicações da coleta da 1ª divisão uruguaia, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {
    "1994": [
        {"mandante": "Peñarol", "visitante": "Defensor Sporting", "gm": 1, "gv": 1, "fase": "Final", "fonte_id": "rsssf:uru94:314",
         "obs": "1º jogo da final (a página traz os dois empates na mesma linha, \"1-1 1-1\"; mando não informado)"},
        {"mandante": "Peñarol", "visitante": "Defensor Sporting", "gm": 1, "gv": 1, "fase": "Final", "fonte_id": "rsssf:uru94:314",
         "obs": "2º jogo da final (a página traz os dois empates na mesma linha, \"1-1 1-1\"; mando não informado)"},
    ],
}

CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("uru34", 156): ("4-1 Defensor", "4-1 Sud América", "linha \"Defensor 4-1 Defensor\"; falta o 3º Defensor x Sud América e, "
                     "com o Sud América, as linhas dos dois clubes fecham com a tabela publicada"),
    ("uru41", 169): ("1-0 Sud América", "1-0 Liverpool", "linha \"Sud América 1-0 Sud América\"; falta o 2º Sud América x "
                     "Liverpool e, com o Liverpool, as linhas dos dois clubes fecham com a tabela publicada"),
    ("uru43", 117): ("2-1 Racing", "2-1 Rampla Juniors", "o Nacional aparece três vezes contra o Racing e uma contra o Rampla; "
                     "com o Rampla, as linhas dos dois clubes fecham com a tabela publicada"),
    ("uru56", 127): ("5-1 Liverpool", "3-1 Liverpool", "o 2º Peñarol x Liverpool aparece como 5-1, igual ao 1º; a Wikipédia "
                     "em espanhol (Campeonato Uruguayo 1956) traz 3-1, que fecha com a tabela publicada para os dois clubes"),
    ("uru40", 119): ("3-9 Peñarol", "3-0 Peñarol", "\"3-9\" não fecha com a tabela; com 3-0 (vitória do Wanderers) as linhas "
                     "dos dois clubes fecham com ela"),
}

CORRIGE: dict[tuple[str, str], dict] = {
    ("1939", "uru39:127"): {"esp": "wo_v", "gm": 6, "gv": 1, "motivo": "Nacional 6-1 Racing em campo; pontos dados ao Racing "
                                                                      "(jogador irregular do Nacional); a tabela conta os gols de campo"},
    ("1947", "uru47:171"): {"fase": "Desempate do 2º lugar", "motivo": "jogo do triangular pelo 2º lugar (a página abre rodadas "
                                                                      "dentro do desempate)"},
    ("1947", "uru47:175"): {"fase": "Desempate do 2º lugar", "motivo": "jogo do triangular pelo 2º lugar"},
    ("1947", "uru47:179"): {"fase": "Desempate do 2º lugar", "motivo": "jogo do triangular pelo 2º lugar (não jogado)"},
    ("1994", "uru94:314"): {"descartar": True, "motivo": "linha com os dois primeiros jogos da final (\"1-1 1-1\"): vira dois jogos "
                                                       "escritos à mão (EXTRAS)"},
}

TABELAS_FORA: dict[tuple[str, str], str] = {
    ("2005/06", "uru06:494"): "\"Annual Table 2005\": soma o Torneo Especial 2005 e o Apertura 2005/06 (ano civil, para "
                              "rebaixamento e vagas), não é tabela desta edição",
}

EXPLICACOES: dict[str, list[str]] = {}
