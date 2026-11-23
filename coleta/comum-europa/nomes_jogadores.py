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
    # Alemão (revisão DE-009: revisao/DE/nomes_espn.txt)
    'Marcelo Marcelinho': 'Marcelinho',
    'Francoaldo Franca': 'França',
    'Cassio Lincoln': 'Lincoln',
    'Cassio Souza Soares Lincoln': 'Lincoln',
    'Bergantin Vinicius': 'Vinícius',
    'Vinicius': 'Vinícius',
    'Hennig Christian Maicon Chris': 'Chris',
    'Christian Maicon Hening Chris': 'Chris',
    'Mazzoli Athirson': 'Athirson',
    'Jiri Stajner': 'Jiří Štajner',
    'Jirí Stajner': 'Jiří Štajner',
    'Antonio Salvo': 'Antonio Di Salvo',
    'Marcelo Jose Bordon': 'Marcelo Bordon',
    'Marcio Santo Borges': 'Márcio Borges',
    'Marcio Borges': 'Márcio Borges',
    'Javier Horacio Pinola': 'Javier Pinola',
    'Ahmed Reda Madouni': 'Ahmed Madouni',
    'Tskitishvili': 'Levan Tskitishvili',
    'Alexander Hleb': 'Aleksandr Hleb',
    'Radoslaw Kaluzny': 'Radosław Kałużny',
    'Radoslav Kaluzny': 'Radosław Kałużny',
    'Vragel Da Silva': 'Vragel da Silva',
    'Niko Kovac': 'Niko Kovač',
    'Nico Kovac': 'Niko Kovač',
    'Dick Van Burik': 'Dick van Burik',
    'Christian Worns': 'Christian Wörns',
    'Rudiger Kauf': 'Rüdiger Kauf',
    'Tomas Zdebel': 'Tomasz Zdebel',
    'David Jarolim': 'David Jarolím',
    'Robert Vittek': 'Róbert Vittek',
    'Christoph Babatz': 'Christof Babatz',
    'Mathieu Delpierre': 'Matthieu Delpierre',
    'Yildiray Basturk': 'Yıldıray Baştürk',
    'Yildiray Bastürk': 'Yıldıray Baştürk',
    'Matthias Abel': 'Mathias Abel',
    'Marc-Andre Kruska': 'Marc-André Kruska',
    'Benjamin Kohler': 'Benjamin Köhler',
    'Marcus Weissenberger': 'Markus Weissenberger',
    'Stefan Kiessling': 'Stefan Kießling',
    'Stefan Kießling (artilheiro 2012': 'Stefan Kießling',
    '13)': 'Stefan Kießling',
}


def nome_jogador(nome: str | None) -> str | None:
    return NOMES_JOGADORES.get(nome, nome) if nome else nome
