"""Nomes de jogadores da ESPN em formato de documento (sobrenomes na frente) -> nome de jogo. Aplicado ao gravar o pacote
(pacote.py), em todas as ligas europeias (revisão RC-004; antes só no Espanhol, ES-006).

Os casos mais frequentes estão aqui; a varredura completa dos nomes com 3 palavras ou mais fica como pendência
(documentacao/README e PENDENCIAS de documentar.py).
"""
from __future__ import annotations


# nome de jogador da ESPN em formato de documento (sobrenomes na frente) -> nome de jogo. Aplicado ao gravar o pacote
# (pacote.py), em todas as ligas (revisão RC-004; antes só no Espanhol, ES-006)
NOMES_JOGADORES = {
    "Kahveci Nihat": "Nihat Kahveci", "Fernando Sanchez Morientes": "Fernando Morientes", "Ismael Aranda Urzaiz": "Ismael Urzaiz",
    "Mendez Ruben Navarro": "Rubén Navarro", "Mocelin Magno": "Magno Mocelin", "Alsocer Raul Molina": "Raúl Molina",
    "Bortolini Pimentel Savio": "Sávio", "Fernandez Manuel Gutierrez Victor": "Víctor Fernández", "Víctor -": "Víctor Fernández",
    "Ballesta Salva": "Salva Ballesta", "Salvador Ballesta Vialcho": "Salva Ballesta",
    "Goncalves da Silva Ailton": "Ailton", "Silva do Nascimento Andre Luiz": "André Luiz", "Jeronimo Baretto Cacau": "Cacau",
    "Eugen Anghel Ewerthon": "Ewerthon", "Duran Fernando Sanz": "Fernando Sanz", "Sanchez Alex Fernandez": "Álex Fernández",
    "Rodrigues Dos Santos Cristiano": "Cristiano", "Francisco Munoz Xisco": "Xisco",
}


def nome_jogador(nome: str | None) -> str | None:
    return NOMES_JOGADORES.get(nome, nome) if nome else nome
