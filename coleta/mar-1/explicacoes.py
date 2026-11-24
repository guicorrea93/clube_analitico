"""Correções e explicações da coleta da 1ª divisão marroquina, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("maro95", 20): ("Credit Agricole Rabat30", "Credit Agricole Rabat 30", "nome grudado no número: a linha não era lida e a "
                     "tabela se partia em duas"),
}
CORRIGE: dict[tuple[str, str], dict] = {}
# clube que desistiu no meio do campeonato: os jogos dele ficam anulados (a tabela publicada não os conta)
ANULA_CLUBE: dict[str, tuple[str, str]] = {
    "1959/60": ("Hassania Agadir", "o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os "
                                   "resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)"),
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {}

EXPLICACOES.update({
    "1933/34": ["dois jogos da página não têm placar (\"drw\", empate sem placar conhecido: Racing Casablanca x SA Marrakech na "
                "6ª rodada e ASPTT Casablanca x Roches Noires na 12ª) e ficam de fora, como no ven-1; por isso esses quatro "
                "clubes têm um jogo e um empate a menos que a tabela"],
    "1954/55": ["a tabela é a publicada na época, que a própria RSSSF diz estar \"cheia de absurdos\" (as linhas não fecham "
                "com o sistema 3-2-1); entra como está, só como classificação"],
    "1959/60": ["Kénitra, FAR e Raja terminaram empatados em pontos; o triangular do título virou um jogo só (KAC Kénitra 3-1 "
                "FAR), porque o Raja se recusou a jogar, dizendo que o título era dele pelo goal average"],
})
_MATRIZ_DIF = ("a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e "
               "derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das "
               "duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da "
               "tabela de confrontos; a classificação é a tabela publicada")
for _t in ("1956/57", "1957/58", "1958/59", "1959/60", "1960/61", "1961/62", "1962/63", "1963/64", "1965/66", "1966/67", "1967/68",
           "1980/81", "1989/90"):
    EXPLICACOES.setdefault(_t, []).append(_MATRIZ_DIF)
