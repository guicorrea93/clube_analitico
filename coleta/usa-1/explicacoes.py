"""Correções e explicações da coleta da 1ª divisão dos EUA, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {
    ("2020", "usa2020:107"): "tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)",
    ("2020", "usa2020:124"): "tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)",
}
EXPLICACOES_2020 = ("a temporada parou em março (pandemia) e voltou com o torneio MLS is Back (Flórida, julho e agosto), cuja "
                    "fase de grupos contou para a fase regular; o mata-mata do torneio não é da liga e fica fora; a "
                    "classificação foi por pontos por jogo, e 7 jogos do Oeste não foram disputados")
EXPLICACOES: dict[str, list[str]] = {"2020": [EXPLICACOES_2020]}
