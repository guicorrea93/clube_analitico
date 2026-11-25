"""Correções e explicações da coleta da 1ª divisão angolana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados): (clube, motivo) ou lista.
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1999", "ango99:235"): {"descartar": True, "motivo": "a linha repete o Sporting de Cabinda 2-1 Sagrada Esperança da "
                             "linha 232 (colada na continuação da nota do jogo de cima)"},
}
ANULA_CLUBE: dict[str, tuple[str, str] | list[tuple[str, str]]] = {
    "1998": ("Kabuscorp", "o Kabuscorp foi desclassificado; os jogos dele foram anulados (\"anulled\" na página)"),
    "2018": ("JGM", "o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados"),
    "2019/20": ("1º de Maio", "o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados"),
    "2022/23": ("Cuando Cubango", "o Cuando Cubango desistiu; todos os seus resultados foram anulados"),
}
_ANULADA = "linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)"
_DO_ANO = "tabela do meio da temporada (a final vem depois)"
TABELAS_FORA: dict[tuple[str, str], str] = {
    **{("1998", f"ango98:{n}"): _DO_ANO for n in (122, 196, 266, 388, 392, 395, 399, 403)},
    **{("2018", f"ango2018:{n}"): _ANULADA for n in (64, 318, 547)},
    **{("2019/20", f"ango2020:{n}"): _ANULADA for n in (69, 319, 476)},
    **{("2022/23", f"ango2023:{n}"): _ANULADA for n in (68, 318, 530)},
}
EXPLICACOES: dict[str, list[str]] = {}
