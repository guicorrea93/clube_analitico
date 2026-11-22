"""Correções e explicações da coleta da 1ª divisão boliviana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}

_20_AGOSTO = ("o 20 de Agosto (Beni) é o único dos 16 clubes que falta na rodada; \"2 de Agosto\" e \"10 de Agosto\" não "
              "existem no campeonato de 1977")
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("bol77", 72): ("2 de Agosto ", "20 de Agosto", _20_AGOSTO),
    ("bol77", 84): ("10 de Agosto", "20 de Agosto", _20_AGOSTO),
    ("bol2024", 325): ("Final", "Apertura Final", "a final do Apertura 2024 (o título do ano veio do Clausura): o título "
                                                  "\"Final\" sozinho é lido como a final do ano"),
}

CORRIGE: dict[tuple[str, str], dict] = {
    ("2003 Apertura", "bol03:230"): {"descartar": True, "motivo": "jogo interrompido por temporal no intervalo (1-2) e completado "
                                                                  "depois (linha 233, \"[remaining 45']\", 2-3): fica a segunda"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_VICE = "a lista de campeões da RSSSF dá o vice {r} e a da Wikipédia em inglês, o {w}; fica o da RSSSF (fonte de base{x})"
EXPLICACOES: dict[str, list[str]] = {
    "1961": [_VICE.format(r="Aurora", w="The Strongest", x="")],
    "1963": [_VICE.format(r="Deportivo Municipal", w="Jorge Wilstermann", x="")],
    "1964": [_VICE.format(r="Aurora", w="Deportivo Municipal", x="")],
    "1968": [_VICE.format(r="Guabirá", w="Litoral de Cochabamba", x="; a tabela final da RSSSF também põe o Guabirá em 2º")],
    "1950": ["os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols de quatro clubes diferem em um ou dois"],
    "1953": ["os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols do Ferroviario diferem (a Wikipédia tem "
             "um placar diferente num jogo dele)"],
}
