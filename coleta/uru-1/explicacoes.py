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
    ("uru06", 838): ("[Apr 17]", "[May 17]", "mês trocado: entre a rodada 12 (13/05) e a 15 (21/05); a ESPN dá maio (QU-006)"),
    ("uru06", 855): ("[Apr 18]", "[May 18]", "mês trocado (QU-006)"),
    ("uru06", 860): ("[Apr 20]", "[May 20]", "mês trocado (QU-006)"),
    ("uru96", 420): ("Nacional 1-1 Peñarol (59' Juan Martín Parodi; 55' Antonio Pacheco)",
                     "Nacional 1-1 Peñarol [59' Juan Martín Parodi; 55' Antonio Pacheco]",
                     "autores entre parênteses na linha do jogo viravam parte do nome do Peñarol (UY-023)"),
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
    ("2018", "uru2018:1010"): {"descartar": True, "motivo": "Supercopa 2019 (03/02/2019) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2019", "uru2019:1040"): {"descartar": True, "motivo": "Supercopa 2020 (01/02/2020) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2020", "uru2020:1152"): {"descartar": True, "motivo": "Supercopa 2021 (02/05/2021) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2021", "uru2021:860"): {"descartar": True, "motivo": "Supercopa 2022 (30/01/2022) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2022", "uru2022:1071"): {"descartar": True, "motivo": "Supercopa 2023 (29/01/2023) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2023", "uru2023:1102"): {"descartar": True, "motivo": "Supercopa 2024 (31/01/2024) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2024", "uru2024:1039"): {"descartar": True, "motivo": "Supercopa 2025 (26/01/2025) entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("2025", "uru2025:1041"): {"descartar": True, "motivo": "Supercopa 2026 entre o campeão e o vencedor da tabela anual: outra competição, não a "
                                                   "final do campeonato (UY-013)"},
    ("1908", "wiki:es_1908:842"): {"esp": "wo_v", "motivo": "o Intrépido não compareceu: W.O. para o Bristol (UY-010)"},
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

EXPLICACOES: dict[str, list[str]] = {
    "1951": ["a tabela publicada (RSSSF e es concordam) não fecha com nenhum jogo da página (Nacional e Danubio com 1 vitória "
             "trocada); a classificação é a tabela publicada (UY-011)"],
    "1954": ["vice Nacional (RSSSF e Wikipédia em inglês); a es dá o Danubio. Fica o da RSSSF até uma 3ª fonte (D-22 b, UY-007)"],
    "1913": ["tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF, base da coleta (UY-012)"],
    "1917": ["tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)"],
    "1919": ["tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)"],
    "1920": ["tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)"],
    "1955": ["a es dá Sud América 15 e Liverpool 13 pontos; a RSSSF, 16 e 12 (ajustes de +1/-1); fica a RSSSF (UY-012)"],
    "1991": ["tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)"],
    "2017": ["artilheiro pela AUF: Maureen Franco 25; a es dá Cristian Palacios 29 (QU-008)"],
    "2023": ["artilheiro pela AUF: Juan Ignacio Ramírez 18; a es dá 19 (QU-008)"],
}
