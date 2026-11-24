"""Correções e explicações da coleta da 1ª divisão venezuelana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1940", "venez40:64"): {"descartar": True, "motivo": "quarto Deportivo Español x Loyola num turno triplo (as rodadas 11-15 "
                                                         "listam 16 jogos para 15); sem ele a tabela final fecha com os jogos"},
    ("2010/11", "espn:311428"): {"gm": 3, "gv": 0, "motivo": "a ESPN dá 15-0; a tabela final da RSSSF só fecha com 3-0 (gols "
                                                             "pró do El Vigía e contra do Caroní)"},
    ("2010/11", "espn:311418"): {"gm_of": 0, "gv_of": 3, "motivo": "a ESPN dá 0-0 e a RSSSF lista o jogo sem placar; a tabela final "
                                                                   "da RSSSF conta vitória do Mineros por 3-0 (provável W.O.)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_VICE = "a lista de campeões da RSSSF dá o vice {r} e a da Wikipédia em inglês, o {w}; fica o da RSSSF (fonte de base)"
_ZULIA = ("o Atlético Zulia (Maracaibo) é o Unicol (Lagunillas) renomeado, como dizem as páginas da RSSSF de 1995/96 e "
          "1996/97, a Wikipédia em espanhol e a ForoVinotinto (decisão C1 do Guilherme, 24/11/2026); a nota da lista de campeões "
          "da RSSSF (\"ULA relocated and renamed Atlético Zulia\") não se sustenta: a ULA jogou o Torneo de Promoción de 1997")
EXPLICACOES: dict[str, list[str]] = {
    "1966": [_VICE.format(r="Deportivo Galicia", w="Deportivo Portugués")],
    "1975": [_VICE.format(r="Deportivo Galicia", w="Estudiantes de Mérida")],
    "1984": ["Petroleros del Zulia x Universidad de Los Andes (15/08) está como \"awd\" sem placar: a tabela conta derrota "
             "por 0-1 para os dois clubes"],
    "1992/93": ["falta um Unión Deportiva Lara x Atlético Zamora (a página só lista o de 13/12, 0-0); pela tabela final, o "
                "Zamora venceu o que falta por 1-0"],
    "1994/95": ["5 jogos do Apertura (Copa Venezuela) estão na página como \"drw\" (empate sem placar, decidido nos pênaltis) "
                "e ficam de fora; \"bt\" / \"lt\" (venceu / perdeu sem placar) entram como W.O."],
    "1996/97": [_ZULIA],
    "1997/98": [_ZULIA + "; o título do Apertura e o do ano ficam com o Atlético Zulia"],
    "1998/99": ["o Internacional de Lara entra como Trujillanos (\"Trujillanos were relocated and renamed Internacional de "
                "Lara\", RSSSF); no ano seguinte o Internacional foi para El Vigía e virou El Vigía FC, e o Trujillanos voltou"],
    "2000/01": ["a 1ª fase foi a Copa Venezuela 2000 (Apertura, com final Caracas x Táchira) e a 2ª, o Torneo Nacional 2001, "
                "que deu o título; o \"Monagas\" da 1ª fase é o Atlético Monagas e o do Torneo Nacional, o Monagas SC (que "
                "comprou a vaga do El Vigía; \"different from Atlético Monagas\", RSSSF)"],
    "2010/11": ["o Clausura 2011 tem 82 jogos sem placar na RSSSF: 81 vêm da ESPN; o Caroní x Zulia não está em nenhuma das "
                "duas (pela tabela final, o Zulia venceu por 3-0)"],
    "2011/12": ["a página da RSSSF só tem as tabelas: os jogos vêm da ESPN, que não tem dois do Apertura (Mineros x Zamora, "
                "2-1 para o Mineros pela tabela, e Carabobo x Aragua, 1-1 pela tabela)"],
    "2015": ["o Torneo de Adecuación 2015 conta como título na RSSSF (Zamora); a Wikipédia em inglês não o conta como "
             "temporada"],
}
