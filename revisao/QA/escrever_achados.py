"""Grava SCRATCH/achados_QA.csv (3ª rodada, 22/11/2026)."""
import csv, os
SCR = r"C:\Users\GUILHE~1\AppData\Local\Temp\claude\c--Users-guilhermecorrea-Downloads-Gui-GitHub\a75361b9-f474-4b01-be59-ef64c90aa262\scratchpad"
TM = "https://www.transfermarkt.com.br"
BNA = "https://www.bolanaarea.com/"
A = []


def ach(*x):
    A.append(x)


ach("QA-001", "bra-serie-a", "C jogos (placar)", "2001", "Bahia; Ponte Preta; Fluminense",
    "Rodada 18 (14/10/2001): Bahia 3x1 Ponte Preta; quartas (05/12/2001): Fluminense 2x1 Ponte Preta (placar posto pelo SA-012)",
    "Transfermarkt e Bola na Área: Bahia 3x2 Ponte Preta e Fluminense 3x2 Ponte Preta. Com os dois, a classificação fecha com a Wikipédia en "
    "(Fluminense 49-34; Ponte Preta 55-51): é a diferença de 1-2 gols que a reconferência deixou no SA-012 | SUGESTÃO: Bahia 3x2 Ponte Preta "
    "(14/10/2001, rodada 18) e Fluminense 3x2 Ponte Preta (05/12/2001, quartas, com prorrogação); fonte: " + TM + "/spielbericht/index/spielbericht/3687306 e "
    + TM + "/spielbericht/index/spielbericht/4414464; " + BNA + "brasileirao_2001_tabela_fase1.htm e brasileirao_2001_tabela_fasefinal.htm; mexer em: "
    "futebol/migrar_brasileirao.py, corrigir_serie_a (trocar o 2-1 do bloco SA-012 por 3-2 e acrescentar o UPDATE do Bahia x Ponte Preta da rodada 18)",
    TM + "/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/2000; " + BNA + "brasileirao_2001_tabela_fase1.htm",
    "media", "banco-painel", "aberto")

ach("QA-002", "bra-serie-a", "C jogos (placar, mando e data)", "1959 (Taça Brasil)",
    "Atlético-MG; Rio Branco-ES; Bahia; Santos; Ceará; ABC; Ferroviário-MA; Tuna Luso; Sport; Hercílio Luz; Athletico-PR",
    "Atlético-MG 2x0 Rio Branco-ES (20/09/1959; 102 gols na edição); 3º jogo da final Bahia 3x1 Santos em 03/03/1960; Ceará 2x1 ABC (desempate) sem data; "
    "mando e datas trocados: Tuna 3x1 Ferroviário-MA (23/08) e Ferroviário-MA 3x1 Tuna (30/08); Athletico-PR 2x1 Hercílio Luz (23/08) e Hercílio Luz 0x1 "
    "Athletico-PR (30/08); Tuna 2x2 Sport (13/09) e Sport 3x1 Tuna (20/09)",
    "Wikipédia pt (footballbox de cada jogo; infobox: 36 jogos e 103 gols) e Bola na Área (com autores dos gols) concordam: Atlético-MG 2x1 Rio Branco-ES "
    "(Maurício 2; Alcenir); final em 29/03/1960 (também en); Ceará 2x1 ABC em 01/09/1959; Ferroviário-MA 1x3 Tuna (23/08) e Tuna 1x3 Ferroviário-MA (30/08); "
    "Hercílio Luz 1x2 Atlético-PR (23/08) e Atlético-PR 1x0 Hercílio Luz (30/08); Sport 2x2 Tuna (24/09) e Tuna 1x3 Sport (27/09) | SUGESTÃO: Atlético-MG 2x1 "
    "Rio Branco-ES; data 1960-03-29 no 3º jogo Bahia x Santos; data 1959-09-01 no desempate Ceará x ABC; inverter mandante/visitante e trocar as datas dos 6 jogos "
    "de Ferroviário-MA x Tuna, Hercílio Luz x Athletico-PR e Sport x Tuna como acima; fonte: https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1959 e "
    + BNA + "taca_brasil_1959_tab.htm; mexer em: futebol/migrar_brasileirao.py, corrigir_serie_a (bloco 1959, junto do SA-013; a data do desempate entra no INSERT do SA-013)",
    "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1959; " + BNA + "taca_brasil_1959_tab.htm; https://en.wikipedia.org/wiki/1959_Campeonato_Brasileiro_S%C3%A9rie_A",
    "media", "banco-painel", "aberto")

ach("QA-003", "bra-serie-a", "C jogos (datas)", "1974; 1988; 1991; 1993; 1994; 1995; 1999", "vários",
    "1995: 89 jogos sem data (ex.: 1ª rodada, Cruzeiro 0x0 Juventude); 1974: 12 sem data. Datas diferentes das duas fontes novas, que concordam entre si: "
    "1991 18 (rodada 12 em 05/04/1991; rodada 5 em 23/03), 1999 14 (rodada 11 em 18-19/08/1999, antes da rodada 6), 1995 12, 1988 3, 1993 2, 1994 2 "
    "(1996-1998 estão no SA-025)",
    "Transfermarkt (página de jogos da temporada) e Bola na Área dão a mesma data: 1995, 81 dos 89 sem data (ex.: 20/08/1995 Cruzeiro 0x0 Juventude); 1991 rodada 12 "
    "em 05/05/1991 e rodada 5 em 03/03/1991; 1999 rodada 11 em 18-19/09/1999. Com as datas novas, o conflito de 1991 zera e os de 1999 caem de 7 para 4 | "
    "SUGESTÃO: aplicar as linhas com situacao 'banco sem data; BNA = fonte2' ou 'banco diferente; BNA = fonte2' (coluna sugestao) de "
    "revisao/QA/saida/datas_bra-serie-a_<ano>.csv (1988, 1991, 1993, 1994, 1995, 1999); 1974: as 12 sem data só têm a Bola na Área (linhas 'banco sem data; só BNA'), "
    "conferir antes; fonte: " + TM + "/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/<ano-1> e " + BNA + "brasileirao_<ano>.htm; "
    "mexer em: futebol/migrar_brasileirao.py, datas_serie_a (além do ogol, ler um CSV de datas revisadas, ex. data/serie_a/datas_revisadas.csv com ano, mandante, "
    "visitante, placar e data; trocar quando a data do banco está vazia ou diferente; recusar troca que deixe clube com 2 jogos no dia)",
    TM + "/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/1994; " + BNA + "brasileirao_1995_fase1.htm; revisao/QA/saida/datas_bra-serie-a_1995.csv",
    "media", "banco-painel", "aberto")

ach("QA-004", "bra-serie-a", "C jogos (pênaltis)", "1988", "vários",
    "Os 96 empates da 1ª fase decididos nos pênaltis (ponto extra) guardam a disputa só na observação ('Penaltis: 6-5.'); penaltis_mandante e penaltis_visitante "
    "vazios nos 290 jogos",
    "RSSSF braz88 (fonte da coleta) traz os pênaltis de cada empate; o Transfermarkt soma os pênaltis ao placar (Vitória 5x3 América = 0x0 e 5-3 nos pênaltis) | "
    "SUGESTÃO: preencher penaltis_mandante/penaltis_visitante a partir da observação 'Penaltis: x-y.' nos 96 jogos de 1988 (e em qualquer jogo com esse texto); "
    "fonte: https://www.rsssf.org/tablesb/braz88.html; mexer em: futebol/migrar_brasileirao.py (na cópia das partidas da Série A, ler 'Penaltis: (\\d+)-(\\d+)' "
    "da observação) ou historico/base.py (onde a observação é montada)",
    "https://www.rsssf.org/tablesb/braz88.html; " + TM + "/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/1987",
    "baixa", "banco-painel", "aberto")

ach("QA-005", "bra-serie-b", "C jogos (1ª fase, Grupo A)", "1971", "ABC; Campinense; Ferroviário do Recife; Ferroviário-CE",
    "Grupo A com 12 jogos (todos com 6 J): ABC 0x0 Ferroviário do Recife (19/09), Campinense 3x3 ABC (10/10), Ferroviário do Recife 1x2 Campinense (13/10), "
    "Ferroviário do Recife 1x1 ABC (20/10); a edição tem 76 jogos e 179 gols",
    "Wikipédia pt e Bola na Área: 10 jogos, 2 não disputados (Ferroviário-PE x Campinense e ABC x Ferroviário-PE, 'não interferiam mais'), com Campinense 1x0 ABC "
    "(12/09) e Ferroviário-PE 3x3 ABC (10/10); a pt dá 74 jogos e 178 gols à edição. A RSSSF Brasil (base da coleta, com autores) traz a versão do banco; o ogol "
    "tem 10 jogos, 2 sem placar. O 1º do grupo (Ferroviário-CE) não muda | SUGESTÃO: decisão: ver decisoes (QA-D1). Se valer pt/BNA: tirar ABC 0x0 Ferroviário do "
    "Recife (19/09) e Ferroviário do Recife 1x2 Campinense (13/10), trocar Campinense 3x3 ABC (10/10) por Campinense 1x0 ABC (12/09) e Ferroviário do Recife 1x1 ABC "
    "(20/10) por Ferroviário do Recife 3x3 ABC (10/10); mexer em: serie_b/importar.py (CORRECOES e um conjunto de jogos a retirar por (ano, mandante, visitante, data))",
    "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1971_-_S%C3%A9rie_B (Grupo A); " + BNA + "serie_b_1971_tabela.htm; data/serie_b/rsssfbrasil/br1971l2.htm",
    "media", "banco-painel", "aberto")

ach("QA-006", "bra-serie-b", "C jogos (placar)", "1972", "Atlético-BA; Central",
    "16/09/1972 Atlético-BA 0x0 Central (1ª fase)",
    "Bola na Área, Wikipédia pt ('16/09/72 Atlético de Alagoinhas 3x1 Central') e ogol: 3x1. A coleta anotou a diferença com o ogol e ficou com a RSSSF | "
    "SUGESTÃO: Atlético-BA 3x1 Central; fonte: https://www.ogol.com.br/jogo/1972-09-16-atletico-ba-central/1217126, " + BNA + "serie_b_1972_tabela.htm; "
    "mexer em: serie_b/importar.py, CORRECOES[(1972, 'Atlético-BA', 'Central')] = (3, 1, '', 'Placar 3-1 (ogol, Wikipédia pt e Bola na Área). Achado QA-006.')",
    "https://www.ogol.com.br/jogo/1972-09-16-atletico-ba-central/1217126; https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1972_-_S%C3%A9rie_B; "
    + BNA + "serie_b_1972_tabela.htm",
    "media", "banco-painel", "aberto")

ach("QA-007", "bra-serie-b", "C jogos (jogo sem placar)", "1981", "Flamengo-PI; Remo",
    "Flamengo-PI x Remo (6ª rodada, 27/01/1981) sem placar, 'n/p'",
    "Bola na Área ('Complemento da 6ª Rodada, 03/02/1981, Flamengo 2x2 Remo'), Wikipédia pt ('03/02/1981 - Flamengo 2x2 Remo') e ogol (jogo de 03/02/1981, 2x2): "
    "o jogo foi adiado e disputado | SUGESTÃO: Flamengo-PI 2x2 Remo em 1981-02-03, sem 'n/p'; fonte: https://www.ogol.com.br/jogo/1981-02-03-flamengo-pi-remo/8320291, "
    + BNA + "serie_b_1981_fase1.htm; mexer em: serie_b/importar.py, CORRECOES[(1981, 'Flamengo-PI', 'Remo')] = (2, 2, '', 'Adiado; jogado em 03/02/1981 (ogol, "
    "Wikipédia pt, Bola na Área). Achado QA-007.') e a data (CORRECOES não troca a data: acrescentar a data na tupla ou um dicionário DATAS)",
    "https://www.ogol.com.br/jogo/1981-02-03-flamengo-pi-remo/8320291; https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1981_-_S%C3%A9rie_B; "
    + BNA + "serie_b_1981_fase1.htm",
    "media", "banco-painel", "aberto")

ach("QA-008", "bra-serie-b", "C jogos (placar; fontes empatadas)", "1971; 1981; 1991",
    "Ferroviário-CE; Itabaiana; Flamengo-PI; Rio Negro-AM; Ceará; Independência; Paysandu",
    "1971 2ª fase: Ferroviário-CE 1x1 Itabaiana (07/11) e Itabaiana 1x0 Ferroviário-CE (24/11); 1981: Flamengo-PI 3x1 Rio Negro-AM (22/01) e Ceará 1x0 "
    "Rio Negro-AM (25/01); 1991: Independência 0x3 Paysandu (1ª fase)",
    "Duas fontes contra duas: o banco segue a RSSSF Brasil e o ogol (1971, 1981) ou a RSSSF e a Bola na Área (1991). A outra dupla: 1971 Ferroviário-CE 0x2 "
    "Itabaiana e Itabaiana 1x1 Ferroviário-CE (Bola na Área, com autores, e pt); 1981 Flamengo-PI 2x1 Rio Negro e Ceará 2x0 Rio Negro (Bola na Área e pt); "
    "1991 Independência 3x0 Paysandu em 24/02 (pt e ogol) | SUGESTÃO: decisão: ver decisoes (QA-D2); desempatar jogo a jogo na Hemeroteca Digital (Jornal dos "
    "Sports) antes de mexer; depois, CORRECOES em serie_b/importar.py",
    BNA + "serie_b_1971_tabela.htm; " + BNA + "serie_b_1981_fase1.htm; https://www.ogol.com.br/jogo/1991-02-17-independencia-ac-paysandu/2178404",
    "media", "banco-painel", "aberto")

ach("QA-009", "bra-serie-b", "C jogos (mando)", "1992", "Ceará; Fortaleza",
    "1ª fase: 23/02/1992 Fortaleza 1x2 Ceará e 15/03/1992 Ceará 0x0 Fortaleza",
    "Bola na Área e ogol: 23/02/1992 Ceará 2x1 Fortaleza e 15/03/1992 Fortaleza 0x0 Ceará (mando trocado nos dois jogos; gols de cada clube iguais) | SUGESTÃO: "
    "inverter mandante e visitante nos dois jogos da 1ª fase; fonte: https://www.ogol.com.br/jogo/1992-02-23-ceara-fortaleza/2178921 e "
    "https://www.ogol.com.br/jogo/1992-03-15-fortaleza-ceara/2178932, " + BNA + "serie_b_1992_fase1.htm; mexer em: serie_b/importar.py (dicionário novo "
    "MANDO_INVERTIDO por (ano, mandante, visitante, data), aplicado em corrigir)",
    "https://www.ogol.com.br/jogo/1992-02-23-ceara-fortaleza/2178921; " + BNA + "serie_b_1992_fase1.htm",
    "baixa", "banco-painel", "aberto")

ach("QA-010", "bra-serie-b", "C jogos (placar)", "1994", "Democrata-GV; Sergipe",
    "24/08/1994 Democrata-GV 1x1 Sergipe (1ª fase)",
    "Bola na Área e ogol: 0x0. A coleta anotou a diferença com o ogol e ficou com a RSSSF | SUGESTÃO: Democrata-GV 0x0 Sergipe; fonte: "
    "https://www.ogol.com.br/jogo/1994-08-24-democrata-gv-sergipe/2182025, " + BNA + "serie_b_1994_fase1.htm; mexer em: serie_b/importar.py, "
    "CORRECOES[(1994, 'Democrata-GV', 'Sergipe')] = (0, 0, '', 'Placar 0-0 (ogol e Bola na Área). Achado QA-010.')",
    "https://www.ogol.com.br/jogo/1994-08-24-democrata-gv-sergipe/2182025; " + BNA + "serie_b_1994_fase1.htm",
    "media", "banco-painel", "aberto")

ach("QA-011", "bra-serie-b", "C jogos (tribunal sem placar)", "1982", "América-MG; Uberaba; Criciúma; Athletico-PR",
    "América-MG x Uberaba (23/01/1982) e Criciúma x Athletico-PR (31/01/1982): 'awd' sem placar (a observação diz 'victory awarded to Uberaba' e "
    "'victory awarded to Atlético')",
    "Bola na Área e ogol: 0x1 nos dois (vitória dada ao visitante; em campo, Criciúma 4x0) | SUGESTÃO: placar 0x1 com resultado_especial 'awd', como o "
    "Figueirense x Caxias de 2001; fonte: " + BNA + "serie_b_1982_fase1.htm e o calendário do ogol de 1982 (data/serie_b/ogol/serie_b_1982.json); mexer em: "
    "serie_b/importar.py, CORRECOES[(1982, 'América-MG', 'Uberaba')] = (0, 1, 'awd', ...) e CORRECOES[(1982, 'Criciúma', 'Athletico-PR')] = (0, 1, 'awd', "
    "'Em campo 4-0; vitória dada ao Atlético-PR (jogador irregular).')",
    BNA + "serie_b_1982_fase1.htm",
    "baixa", "banco-painel", "aberto")

ach("QA-012", "bra-serie-b", "C jogos (datas)", "2009; 1981; 1982; 1989", "vários",
    "2009: 54 jogos com data diferente (ex.: Juventude 2x0 Figueirense, rodada 11, em 11/07/2009, mesmo dia da rodada 10); 1981: 13; 1982: 3. 1989: os 18 jogos "
    "do grupo J (Esportivo-MG, Bragantino, São José-SP, Santo André, Volta Redonda, GE Novorizontino) ficaram em 28/10/1989 (Esportivo-MG com 6 jogos no dia; "
    "São José-SP x Bragantino ida e volta no mesmo dia)",
    "2009: Transfermarkt e Bola na Área dão a mesma data (ex.: 14/07/2009 Juventude 2x0 Figueirense); 1981 e 1982: Bola na Área e Wikipédia pt concordam. "
    "1989: o ogol tem os jogos do grupo J com data (09/09 a 28/10/1989), mas como 'Esportivo Passense', nome que a coleta não casou | SUGESTÃO: 2009, 1981 e 1982: "
    "aplicar as linhas 'BNA = fonte2' de revisao/QA/saida/datas_bra-serie-b_<ano>.csv; 1989: pôr 'Esportivo Passense' (ogol) como nome do Esportivo-MG para o "
    "aplicar_ogol usar as datas do ogol; fonte: " + TM + "/campeonato-brasileiro-serie-b/gesamtspielplan/wettbewerb/BRA2/saison_id/2008, " + BNA
    + "serie_b_2009_turno1.htm, https://www.ogol.com.br/jogo/1989-09-09-santo-andre-esportivo-passense/2463251; mexer em: serie_b/importar.py (aplicar_ogol e um "
    "DATAS_REVISADAS lido de CSV) e serie_b/clubes.py (nome do ogol 'Esportivo Passense' -> Esportivo-MG em 1989)",
    TM + "/campeonato-brasileiro-serie-b/gesamtspielplan/wettbewerb/BRA2/saison_id/2008; " + BNA + "serie_b_2009_turno1.htm; data/serie_b/ogol/serie_b_1989.json",
    "media", "banco-painel", "aberto")

cab = "id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao".split(",")
with open(os.path.join(SCR, "achados_QA.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cab)
    w.writerows(A)
print(len(A), "achados")
