"""Nomes de jogadores da ESPN em formato de documento (sobrenomes na frente) -> nome de jogo. Aplicado ao gravar o pacote
(pacote.py), em todas as ligas europeias (revisão RC-004; antes só no Espanhol, ES-006).

Os casos mais frequentes estão aqui, mais os da varredura de 24/11/2026 (o mesmo jogador com o nome de documento e o
nome de jogo no mesmo clube e temporada). Os outros nomes de 3 palavras ou mais (cerca de 2 mil, quase todos nomes de
verdade, como "Kevin De Bruyne") não têm referência para conferir um a um: a ESPN não dá o código do jogador.
"""
from __future__ import annotations


# nome de jogador da ESPN em formato de documento (sobrenomes na frente) -> nome de jogo. Aplicado ao gravar o pacote
# (pacote.py), em todas as ligas (revisão RC-004; antes só no Espanhol, ES-006)
NOMES_JOGADORES = {
    # varredura de 24/11/2026: o mesmo jogador com o nome de documento e o nome de jogo no mesmo clube e temporada (ESPN)
    "Ricardo Emido Ramalho da Silva": "Ricardo Silva", "Barbosa Rodrigo Tabata": "Rodrigo Tabata",
    "Cesario Marcus Vinicius": "Marcus Vinícius", "Jose Miguel Organista de Simoes Aguiar": "José Aguiar",
    "Vinicius Tulio De Melo": "Túlio de Melo", "Vinicius De Melo": "Túlio de Melo",
    "De Souza Santos Luiz Henrique": "Luiz Henrique", "Souza Santos Luiz Henrique": "Luiz Henrique",
    "Enrique Gabriel Gomez": "Gabriel Gómez", "José Alberto Schaffer": "José Schaffer", "Augustin Gilles Binya": "Gilles Binya",
    "Alexander Fabio Coentrao": "Fábio Coentrão", "Luiz Santos Viana Andre Bahia": "André Bahia",
    "Ricardo Ribeiro Jesus Paulo Machado": "Paulo Machado", "Miguel Costa Nuno Silva": "Nuno Silva",
    "Pedro Jorge Marques Pereira": "Pedro Pereira", "Filipe Tavares Bruno Pinheiro": "Bruno Pinheiro",
    "Alexandre Mauro Almeida": "Mauro Almeida", "Cristian Chagos Tarouco Titi": "Titi",
    "Mohammed Abdel Kader Toure": "Kader Touré", "Jorge Ciro Perdomo Fucile": "Jorge Fucile",
    "Volkan Kursat Bekiroglu": "Volkan Bekiroğlu", "Dos Santos Anderson": "Anderson", "Fabio Da Silva Bilica": "Fábio Bilica",
    "Rodriguez Javi Venta": "Javi Venta", "Gomez Javi Gonzalez": "Javi González", "Jean Pierre Barrientos": "Jean Barrientos",
    "Ernest Webnje Nfor": "Ernest Nfor", "Rosa Ferreira Mombra Bruno Mezenga": "Bruno Mezenga",
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
