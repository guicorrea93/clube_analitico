"""Importa jogos da Copa dos Campeoes Estaduais 1937 (Torneio dos Campeoes).

Reconhecida pela CBF como Campeonato Brasileiro em agosto de 2023 (Atletico-MG
campeao). Fase preliminar com Alianca, Liga de Sports da Marinha e Rio Branco
(ES); quadrangular em turno e returno com Atletico-MG, Fluminense, Rio Branco
e Portuguesa.

Fonte: Wikipedia PT, "Campeonato Brasileiro de Futebol de 1937" (a mesma da
classificacao final ja no banco), que cita O Globo, Jornal do Brasil e
Correio da Manha de janeiro e fevereiro de 1937. A RSSSF e o RSSSF Brasil nao
tem pagina de jogos desta edicao. Os jogos da Wikipedia PT fecham exatamente
com a tabela do quadrangular dela; a versao em ingles diverge em datas e
traz Rio Branco 3-1 Portuguesa (aqui 3-2), que nao fecha com a tabela.
Mandante = clube da casa (o estadio de cada jogo esta na fonte).
"""
from importar_brasileirao_historico_base import Game, import_year, write_audit

YEAR = 1937
EDICAO = "1937"
SOURCE = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1937"

# (fase, ordem, tipo, data, mandante, gols, gols, visitante, observacao)
JOGOS = [
    ("Fase preliminar", 1, "mata_mata", "1937-01-06", "Aliança", 0, 2, "Liga da Marinha", "Campo da Usina, Campos dos Goytacazes."),
    ("Fase preliminar", 1, "mata_mata", "1937-01-11", "Rio Branco-ES", 2, 0, "Liga da Marinha", "Estadio Governador Bley, Vitoria. Apos prorrogacao."),
    ("Quadrangular final", 2, "grupo", "1937-01-10", "Portuguesa", 4, 1, "Fluminense", "Campo do Cambuci, Sao Paulo."),
    ("Quadrangular final", 2, "grupo", "1937-01-13", "Fluminense", 6, 0, "Atletico-MG", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-13", "Rio Branco-ES", 3, 2, "Portuguesa", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-17", "Rio Branco-ES", 1, 1, "Atletico-MG", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-20", "Fluminense", 6, 2, "Portuguesa", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-24", "Rio Branco-ES", 4, 3, "Fluminense", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-24", "Atletico-MG", 5, 0, "Portuguesa", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-01-28", "Fluminense", 5, 2, "Rio Branco-ES", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-31", "Atletico-MG", 4, 1, "Fluminense", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-01-31", "Portuguesa", 4, 0, "Rio Branco-ES", "Campo do Cambuci, Sao Paulo."),
    ("Quadrangular final", 2, "grupo", "1937-02-03", "Atletico-MG", 5, 1, "Rio Branco-ES", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-02-14", "Portuguesa", 2, 3, "Atletico-MG", "Campo do Cambuci, Sao Paulo."),
]


def jogos() -> list[Game]:
    out = []
    for i, (fase, ordem, tipo, data, mand, gm, gv, vis, obs) in enumerate(JOGOS, start=1):
        out.append(Game(YEAR, fase, ordem, tipo, None, i, data, mand, vis, gm, gv, SOURCE, obs))
    return out


if __name__ == "__main__":
    games = jogos()
    participantes = import_year(YEAR, SOURCE, games, EDICAO)
    audit = write_audit(YEAR, games, EDICAO)
    print(f"{YEAR}: {len(participantes)} participantes, {len({g.fase for g in games})} fases, {len(games)} jogos")
    print(f"auditoria: {audit}")
