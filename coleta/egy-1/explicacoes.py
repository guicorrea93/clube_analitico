"""Correções e explicações da coleta da 1ª divisão egípcia, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

_CRUZADA = "egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)"
EXTRAS: dict[str, list[dict]] = {
    # 1962/63: os desempates vêm em tabela cruzada, que o leitor não lê; com estes jogos, as tabelas dos dois desempates fecham
    "1962/63": [{"mandante": m, "visitante": v, "gm": a, "gv": b, "fase": f, "fonte_id": _CRUZADA}
                for m, v, a, b, f in [
                    ("Ismaily", "Tersana", 0, 1, "Desempate do grupo B"), ("Ismaily", "Zamalek", 0, 1, "Desempate do grupo B"),
                    ("Tersana", "Zamalek", 0, 1, "Desempate do grupo B"),
                    ("Al-Ahly", "Qanah", 1, 1, "Fase final"), ("Al-Ahly", "Tersana", 0, 2, "Fase final"),
                    ("Al-Ahly", "Zamalek", 1, 1, "Fase final"), ("Qanah", "Tersana", 1, 2, "Fase final"),
                    ("Qanah", "Zamalek", 1, 2, "Fase final"), ("Tersana", "Zamalek", 3, 3, "Fase final")]],
    # jogos do turno que faltam no calendário do ogol (a base destes anos); o placar sai da diferença entre a tabela da
    # RSSSF e a soma dos jogos, que fecha com os dois clubes; sem data
    "1990/91": [{"mandante": "Al-Ahly", "visitante": "Ismaily", "gm": 1, "gv": 0, "fase": "",
                 "fonte_id": "egy91: tabela final e a lista de resultados do Ismaily (\"2 losses: Ahly, Tersana\")",
                 "obs": "jogo do turno que falta no ogol (o Ismaily x Al-Ahly da 24ª rodada foi 1-1); o placar 1-0 sai da tabela"}],
    "2011/12": [{"mandante": "Al-Masry", "visitante": "Al-Ahly", "gm": 3, "gv": 1, "fase": "", "data": "2012-02-01", "rodada": 17,
                 "fonte_id": "egy2012: tabela no abandono (a Wikipédia traz a mesma)",
                 "obs": "o jogo da tragédia do estádio de Port Said (74 mortos, depois do apito final); o ogol o marca como "
                        "anulado, mas a tabela no abandono conta o 3-1"}],
    "1993/94": [{"mandante": "Al-Ahly", "visitante": "Ismaily", "gm": 1, "gv": 1, "fase": "",
                 "fonte_id": "egy94: tabela final",
                 "obs": "jogo do returno que falta no ogol (o da 6ª rodada também foi 1-1); o placar sai da tabela"}],
}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1948/49", "egy49:43"): {"data": None, "motivo": "desempate do 2º lugar sem data na página (a data lida era a da "
                                                      "rodada de cima)"},
    ("2023/24", "egy2024:479"): {"descartar": True, "motivo": "Pyramids x Smouha (28/6/2025) foi interrompido aos 50' com 1-1 "
                                                              "(incêndio no estádio) e completado em 2/7: fica só a linha da "
                                                              "continuação, com o placar final"},
    ("2023/24", "egy2024:485"): {"nota": "interrompido aos 50' com 1-1 em 28/6/2025 (incêndio no estádio); os 40 minutos que "
                                         "faltavam foram jogados em 2/7/2025",
                                 "motivo": "a página escreve o jogo em duas linhas (interrupção e continuação)"},
    # 2011/12 (abandonada em 1/2/2012): o ogol põe 0-0 em jogos que não aconteceram; a tabela no abandono (RSSSF e
    # Wikipédia, iguais) não os conta, e sem eles as linhas dos clubes fecham
    ("2011/12", "ogol:6940584"): {"descartar": True, "motivo": "Ismaily 0-0 Ghazl El-Mahalla (6/3/2012): jogo adiado da "
                                                               "10ª rodada, marcado depois do abandono; nunca foi jogado"},
    ("2011/12", "ogol:6940585"): {"descartar": True, "motivo": "Al-Ahly 0-0 Wadi Degla (6/3/2012): jogo adiado da 10ª "
                                                               "rodada, marcado depois do abandono; nunca foi jogado"},
    ("2011/12", "ogol:6940640"): {"esp": "abd", "motivo": "Zamalek x Ismaily (1/2/2012): interrompido (o ogol traz 0-0); "
                                                          "a tabela no abandono não o conta"},
    ("2011/12", "ogol:6940586"): {"descartar": True, "motivo": "Al-Masry 0-0 Petrojet (30/12/2011): a tabela no abandono não "
                                                               "conta este jogo (adiado); sem ele, os dois clubes fecham"},
    ("2011/12", "ogol:6940587"): {"descartar": True, "motivo": "Zamalek 0-0 Haras El-Hodoud (30/12/2011): a tabela no abandono "
                                                               "não conta este jogo (adiado); sem ele, os dois clubes fecham"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1992/93": ["a tabela da RSSSF dá 26 jogos a El-Merreikh e El-Minya, com uma derrota a mais para cada um (e 5 gols "
                "sofridos a mais para o Merreikh); o ogol e a tabela da Wikipédia dão 25 jogos aos dois. O jogo entre eles "
                "não aparece em nenhuma fonte de jogos (provavelmente decidido fora de campo, com derrota para os dois). A "
                "classificação usa os números dos jogos; faltam 1 dos 182 jogos esperados pela tabela da RSSSF"],
    "1974/75": ["a tabela da RSSSF troca os números de Plastic e Suez (12º e 13º, os dois com 28 pontos); o ogol e a tabela "
                "da Wikipédia dão a cada um os seus. A classificação usa os números dos jogos"],
}
