"""Grava SCRATCH/achados_PY.csv (revisão par-1, 3ª rodada, 22/11/2026). Uso: python -I revisao/PY/gravar_achados.py <arquivo csv>"""
import csv
import sys

RS = "https://www.rsssf.org/tablesp/"
WES = "https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Paraguay#T%C3%ADtulos_de_Liga_por_a%C3%B1o"
C = "par-1"
A = []


def a(item, edicao, clube, painel, fonte_diz, fonte, grav, quem, sit="aberto"):
    A.append([f"PY-{len(A) + 1:03d}", C, item, edicao, clube, painel, fonte_diz, fonte, grav, quem, sit])


# 001
a("A campeão (classificação)", "1917; 1928; 1936; 1991", "Olimpia; Sol de América; Guaraní de Asunción; Nacional de Asunción",
  "O campeão não está na classificação final e outro clube aparece em 1º: 1917 Olimpia, 1928 Sol de América (era o 9º da "
  "tabela), 1936 Guaraní (era o 11º), 1991 Nacional (era o 5º da 2ª rodada). O painel tira o campeão da 1ª linha: no ar, "
  "títulos Olimpia 46 (certo 47), Libertad 25 (26), Guaraní 12 (11), Nacional 10 (9), Sol de América com 1928 no lugar de 1991. "
  "edicoes.csv e o banco (edicao.campeao_id) estão certos.",
  "Campeões 1917 Libertad (Gran Partido Final Olimpia 0-1 Libertad, parahist l.525), 1928 Olimpia, 1936 Olimpia (líder no "
  "abandono), 1991 Sol de América (final x Cerro Porteño, para91 l.90-97) | SUGESTÃO: importar.classificacao(): quando o "
  "campeão da lista não está nas linhas, inserir uma linha dele no topo (colunas vazias, fonte parachamp) em vez de deixar o "
  "1º da tabela; e o painel usar edicao.campeao_id em vez da posição 1; fonte: " + RS + "parachamp.html; mexer em: "
  "coleta/par-1/importar.py classificacao() e gerar_dashboard_v2.py (campeão do ED)",
  RS + "parachamp.html ; " + RS + "parahist.html (1917, 1928, 1936) ; " + RS + "para91.html ; " + WES, "alta",
  "coleta-sulamerica; banco-painel")
# 002
a("A vice", "1909; 1914; 1915; 1917; 1918; 1928; 1936; 1942; 1962; 1966; 1986; 1987; 1989; 1990; 1991; 1992; 1999; 2000; 2001; "
  "2002; 2003; 2005; 2020 Clausura", "",
  "Vice errado ou vazio em 23 edições. Pacote: 1909/1914/1915/1918/1928/1936/1942/1989 vazio; 1917 River Plate; 1962 River Plate; "
  "1966 Olimpia; 1986 Colegiales; 1987 Nacional; 1990 Nacional; 1991 Guaraní; 1992 Olimpia; 1999 Sp. Luqueño; 2000 Sol de "
  "América; 2001 Libertad; 2002 Sp. Luqueño; 2003 Cerro Porteño; 2005 Nacional; 2020 Clausura 12 de Octubre. No site (versão "
  "antiga) 18 destes estão errados (1909-1992 + 2004 Guaraní e 2005); 1999-2003 e 2020C estão certos no site e ERRADOS no "
  "pacote novo (regressão do 0b793ba).",
  "RSSSF parachamp e Wikipédia es concordam: 1909 Libertad, 1914 Cerro Porteño, 1915 Olimpia, 1917 Olimpia, 1918 Nacional, "
  "1928 Libertad, 1936 Atlántida, 1942 Cerro Porteño, 1962 Nacional, 1966 Guaraní, 1986 Olimpia, 1987 Olimpia, 1989 Guaraní, "
  "1990 Libertad, 1991 Cerro Porteño, 1992 Libertad, 1999 Cerro Porteño, 2000 Guaraní (final 1-0/3-1), 2001 Sp. Luqueño "
  "(final 3-0/3-1), 2002 12 de Octubre (final), 2003 Guaraní, 2005 Libertad (Playoff for Second Place), 2020C Guaraní (final 2-2, "
  "pên. 5-4) | SUGESTÃO: em importar.classificacao(), depois de pôr o campeão em 1º, pôr o vice da lista (VICES, parachamp) em "
  "2º (inserindo a linha se faltar); hoje o vice é a 2ª linha da tabela agregada; fonte: " + RS + "parachamp.html; mexer em: "
  "coleta/par-1/importar.py classificacao() e o cálculo de 'vice' em gravar()",
  RS + "parachamp.html ; " + WES, "alta", "coleta-sulamerica")
# 003
a("B classificação (tabela parcial)", "1909; 1911; 1912; 1914; 1915; 1916; 1918; 1919; 1920; 1921; 1923; 1924; 1925; 1926; 1927; 1928; 1929; 1935; 1936; 1937; 1938; 1940; 1941; 1942; 1944; 1946; 1948; 1949; 1950; 1951; 1952; 1953; 1954; 1957; 1958; 1959", "",
  "A tabela parcial de parahist é cortada na 1ª linha sem número (clube empatado): entram 1 a 6 clubes de tabelas com 6 a 11 "
  "(ex.: 1909 1 de 6, 1914 1 de 6, 1918 1 de 9, 1925 2 de 8, 1927 2 de 10, 1928 1 de 10, 1936 1 de 11, 1942 1 de 10, 1944 2 de 9, "
  "1946 2 de 10, 1952 e 1953 2 de 11). É a causa de PY-001 (1928, 1936) e de vices vazios. Lista completa: revisao/PY/tabelas_parciais.py.",
  "parahist traz as tabelas inteiras (linhas sem número = mesma posição da de cima), ex.: 1928 l.966-976 (10 clubes), 1936 "
  "l.1193-1204 (11 clubes) | SUGESTÃO: em ler_rsssf.tabela_parcial(), aceitar linha sem número dentro do bloco (herda a posição) "
  "e não reiniciar a tabela nela; fonte: " + RS + "parahist.html; mexer em: coleta/par-1/ler_rsssf.py tabela_parcial() e _PARCIAL",
  RS + "parahist.html", "alta", "coleta-sulamerica")
# 004
a("B classificação (1982-1995)", "1986; 1987; 1988; 1989; 1990; 1991; 1992; 1993; 1995", "",
  "Nos anos 1982-1995 a classificação é a 1ª tabela completa da página, que é de UMA fase: 1986 1ª fase (27 j), 1987 3ª fase "
  "(9 j), 1988 fase final (7 j), 1990 grupo A da 3ª fase (6 clubes, vice Nacional), 1991 2ª rodada a partir do 5º (Nacional 1º), "
  "1992/1993 1ª fase (11 j; 1992 Cerro campeão com 8 pts em 1º), 1995 1ª fase (12 j). 1989: colunas trocadas (Olimpia J 33, V 50, "
  "E 74, D 35, Pts 2, ajuste -172) e só 1 clube de 12. A ficha diz 'completa em 1990-1995'.",
  "As páginas têm várias fases e, em 1990, 1991 e 1994, os jogos da final; 1989 é 'J-Pts (GP-GC) V E D' com 12 clubes "
  "(para89 l.15-28) | SUGESTÃO: escolher em edicoes.py a tabela certa por ano (tabelas=[(página, linha, linha)] da tabela "
  "acumulada/final; sem acumulada, só campeão e vice) e ler 1989 com o formato próprio; fonte: " + RS + "para89.html, para90.html, "
  "para91.html; mexer em: coleta/par-1/edicoes.py (_PAGINAS/tabelas) e importar.classificacao() (pub sem_conferencia)",
  RS + "para86.html … para95.html", "alta", "coleta-sulamerica")
# 005
a("C jogos de outros torneios (1962-1966)", "1962; 1963; 1964; 1965; 1966", "",
  "152 jogos de torneios de pré-temporada entram na edição: 1962 Torneo Preparación (28), 1963 Copa Asunción (18), 1964 "
  "Clasificatorio e Copa Asunción (26), 1965 Clasificatorio, Copa Asunción e Torneo Preparación (58), 1966 Torneo de Honor e "
  "Copa República (22, com 'Ovetense', que é a seleção da Liga Ovetense). A liga verdadeira de 1962 e 1966 ficou com a fase "
  "'Final' (112 e 75 jogos). A classificação calculada difere da tabela da RSSSF (ex.: 1964 San Lorenzo 3º com 30 pts; RSSSF "
  "Nacional 3º, San Lorenzo 20 pts; 1965 Olimpia 52 pts, RSSSF 23).",
  "O campeonato começa em para62 l.98, para63 l.83, para64 l.127, para65 l.217, para66 l.109 ('Campeonato de Primera División "
  "A/de Honor'); antes vêm as copas | SUGESTÃO: começar os trechos nessas linhas (trechos=[('para62', 98, None)] etc.) e deixar a "
  "classificação ser a 'Final Table' do campeonato; fonte: " + RS + "para62.html … para66.html; mexer em: coleta/par-1/edicoes.py "
  "(_COM_JOGOS: linha inicial por ano)",
  RS + "para62.html ; para63.html ; para64.html ; para65.html ; para66.html", "alta", "coleta-sulamerica")
# 006
a("C playoffs de rebaixamento como liga/título", "1961; 1963", "Presidente Hayes; Atlético Tembetary; Sportivo Luqueño",
  "1961: 'Playoff against 11th Place' (Hayes x Tembetary, 2 jogos) entrou na fase de liga (+2 jogos na campanha deles); 1963: o "
  "playoff de 11º lugar (Luqueño x Tembetary, 3 jogos, Dec 19/23 e Jan 12) e o desempate da Copa Asunción viraram 'Desempate do "
  "título'/liga com data 1963-12-06.",
  "para61 l.283-291 e para63 l.351-362 | SUGESTÃO: incluir em ler_rsssf.FASES os títulos 'Playoff against 11th Place' -> "
  "'Desempate do rebaixamento' (ou cortar com FIM_PADRAO); fonte: " + RS + "para61.html; mexer em: coleta/par-1/ler_rsssf.py FASES "
  "e edicoes.FIM_PADRAO",
  RS + "para61.html ; " + RS + "para63.html", "media", "coleta-sulamerica")
# 007
a("C jogos que não valem o título (1996-2007)", "2000; 2004; 2005", "Fernando de la Mora; 2 de Mayo",
  "2000: 'Second Place Playoff' e 'Cuadrangular for Third Copa Libertadores Place' (9 jogos) como 'Desempate do 2º lugar' e "
  "'Fase final'; 2004: Pre-Sudamericana (semis e final, 6 jogos) como 'Semifinal'/'Final'; 2005: Pre-Sudamericana (3 jogos) e a "
  "final da Intermedia (2ª divisão) 2 de Mayo x Fernando de la Mora (2 jogos, que põem o Fernando de la Mora no par-1 de 2005) "
  "como 'Final'; 2005: 'Playoff for Second Place' Guaraní x Libertad lido como jogos do Clausura.",
  "para00 l.496-531, para04 (Pre-Sudamericana; Wikipédia es 2004 confirma), para05 l.315-327, l.628-639 e l.953-962 ('Championship "
  "Final' da Intermedia; edicoes.py a soma de propósito achando que é a final do campeonato) | SUGESTÃO: tirar ('para05', 953, "
  "971) de edicoes._ANUAL e cortar 'Pre-Sudamericana', 'Cuadrangular for ... Libertadores', 'Second Place Playoff' por FIM/fase; "
  "fonte: " + RS + "para05.html; mexer em: coleta/par-1/edicoes.py e ler_rsssf.FASES",
  RS + "para00.html ; para04.html ; para05.html ; https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_2004",
  "media", "coleta-sulamerica")
# 008
a("C nomes de fase", "1981; 1996; 1997; 1998; 1999; 2003", "",
  "As semifinais e finais do Apertura e do Clausura e a final do ano levam o mesmo nome ('Semifinal'/'Final'): 1998 'Final' tem 4 "
  "jogos de 3 clubes e a final de verdade é 'Desempate do título'; 1997 e 1999 idem. 1981: 'Triangular de Desempate' e 'Overall "
  "Final' viraram 'Segunda fase' e 'Desempate do título'; a 'Final' de 1981 é a do 1º turno.",
  "Títulos nas páginas: 'Apertura Final', 'Clausura Final', 'Final' (do ano), 'Triangular de Desempate', 'Overall Final' | "
  "SUGESTÃO: preencher ler_rsssf.TORNEIOS/FECHA (hoje vazios, copiados da Colômbia) para os torneios do ano e mapear 'Overall "
  "Final'/'Finalísima' -> 'Final' e as finais dos torneios -> 'Final do Apertura/Clausura' (já existe _fase()); fonte: " + RS +
  "para98.html; mexer em: coleta/par-1/ler_rsssf.py TORNEIOS, FECHA, FASES",
  RS + "para81.html ; para97.html ; para98.html ; para99.html", "media", "coleta-sulamerica")
# 009
a("C datas e rodadas de mata-mata", "1961-1967; 1981; 1996-2007; 2015 Clausura; 2020 Clausura", "",
  "Jogos de playoff herdam a data e a rodada da última rodada lida: 84 casos de 'clube com 2+ jogos no mesmo dia'. Ex.: 1967 "
  "desempate do 2º lugar 1967-12-03 (página: Dec 15 e Dec 22); 1981 final 1981-12-01 (Dec 6, Dec 13, Dec 18) e semis/final do 1º "
  "turno 06-21 (Jun 28, Jul 3); 2000 final 11-19 (Nov 28, Dec 3); 2007 final 12-02 (ESPN 12-09); 2020 Clausura semis 12-23 (ESPN "
  "12-27) e final com rodada 11.",
  "Datas no formato 'First Leg [Dec 15]' (armadilha conhecida no COMECE-AQUI) | SUGESTÃO: ler a data do título da fase ('First Leg "
  "[..]', 'Semifinals [Jun 28]', 'Final [Jul 3]') no rsssf_sul ou corrigir em CORRIGE; de 2005 em diante, usar a data da ESPN "
  "quando a da RSSSF vier de rodada anterior; fonte: " + RS + "para67.html; mexer em: coleta/comum-sulamerica/rsssf_sul.py (data de "
  "título de fase) ou coleta/par-1/explicacoes.py CORRIGE; lista: revisao/PY/varredura.py",
  RS + "para67.html ; para81.html ; para00.html ; para2020.html", "media", "coleta-sulamerica")
# 010
a("B jogo decidido no tribunal", "1960", "Libertad; Atlético Tembetary",
  "Tembetary 2-2 Libertad (1960-04-17) sem 'awd': Libertad 25 pts (RSSSF 26), Tembetary 24 (RSSSF 23).",
  "para60 l.69 'awarded as a win to Libertad' | SUGESTÃO: aceitar 'awarded as a win to' em _vitoria_dada (ou CORRIGE com "
  "esp='wo_v'); fonte: " + RS + "para60.html; mexer em: coleta/par-1/ler_rsssf.py _vitoria_dada()",
  RS + "para60.html", "media", "coleta-sulamerica")
# 011
a("B rebaixado", "1967", "Sportivo San Lorenzo",
  "San Lorenzo marcado 'rebaixado' (a nota 'Relegation Playoff' casa com 'relegat').",
  "para67 l.316-324: San Lorenzo 3-2 e 0-0 Presidente Hayes, 'both remain at former level' | SUGESTÃO: em importar.situacao() não "
  "tratar 'Relegation Playoff' como queda; fonte: " + RS + "para67.html; mexer em: coleta/par-1/importar.py situacao()",
  RS + "para67.html", "alta", "coleta-sulamerica")
# 012
a("B rebaixados não marcados", "1965-2025", "",
  "Só 1967 e 1994 têm 'rebaixado'; nos outros anos a aba Participantes mostra '—' (ex.: 2024 Clausura Sol de América e Tacuary). "
  "Em 1994 faltam 8 de Diciembre, Boquerón, 12 de Octubre e Cerro Porteño (Cd. Este) (caíram na reestruturação de 1995) e "
  "Pettirossi está marcado por ter jogado o 'Relegation Playoff' (ganhou).",
  "RSSSF traz a queda por promedio no fim de cada ano: 2010 Sport Colombia e Trinidense; 2015 Santaní e San Lorenzo; 2019 Capiatá "
  "e Santaní; 2024 Sol de América e Tacuary; 2025 Gral. Caballero JLM e Tembetary; para94 l.93-102 | SUGESTÃO: lista REBAIXADOS "
  "por ano (linhas 'Relegated'/'relegated on points average') aplicada na última edição do ano; fonte: " + RS + "para2024.html "
  "l.856; mexer em: coleta/par-1/importar.py situacao() + nova lista em explicacoes.py",
  RS + "para2010.html ; para2015.html ; para2019.html ; para2024.html ; para2025.html ; para94.html", "media", "coleta-sulamerica")
# 013
a("E clubes juntados", "1994", "Silvio Pettirossi",
  "O 'Pettirossi (Encarnación)' de 1994 foi juntado ao Silvio Pettirossi de Asunción (1926), que jogou a 1ª em 1970 e 2008.",
  "Wikipédia es 1994 lista 'Club Pettirossi' de Encarnación (fundado 1916, estádio Carlos Memmel); para94 l.34 'Pettirossi "
  "(Encarnación)' | SUGESTÃO (decisão do Guilherme): clube novo 'Pettirossi de Encarnación' e regra só para 1994; fonte: "
  "https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994; mexer em: coleta/par-1/clubes_par.py CLUBES e REGRAS",
  "https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994 ; https://es.wikipedia.org/wiki/Club_Silvio_Pettirossi ; "
  + RS + "para94.html", "media", "coleta-sulamerica")
# 014
a("E clube duplicado", "1994; 2012-2013", "Cerro Porteño de Ciudad del Este; Cerro Porteño PF",
  "'Cerro Porteño de Ciudad del Este' (1994) e 'Cerro Porteño PF' (2012-2013) são dois cadastros.",
  "Wikipédia es do Cerro Porteño (Presidente Franco): 'En 1994 el equipo fue incluido junto con otros 5 clubes del interior en el "
  "nuevo Torneo Nacional'; a página de 1994 lista 'Club Cerro Porteño (Presidente Franco)' | SUGESTÃO (decisão do Guilherme): "
  "juntar em 'Cerro Porteño PF'; fonte: https://es.wikipedia.org/wiki/Club_Cerro_Porte%C3%B1o_(Presidente_Franco); mexer em: "
  "coleta/par-1/clubes_par.py REGRAS (regra 'cerro porteno cd este' -> Cerro Porteño PF)",
  "https://es.wikipedia.org/wiki/Club_Cerro_Porte%C3%B1o_(Presidente_Franco)", "media", "coleta-sulamerica")
# 015
a("E cidade do clube", "1994", "8 de Diciembre", "Cidade Caacupé (Cordillera).",
  "Wikipédia es 1994: Club 8 de Diciembre, Caaguazú, estádio Federico Llamosas, fundado em 1961 | SUGESTÃO: ('Caaguazú', "
  "'Caaguazú'); fonte: https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994; mexer em: coleta/par-1/clubes_par.py CLUBES",
  "https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994", "baixa", "coleta-sulamerica")
# 016
a("E escudos", "", "Presidente Hayes; Sport Colombia; Atlético Colegiales; Cerro Corá; Atlántida; Universal de Encarnación; Silvio "
  "Pettirossi; Deportivo Humaitá; Deportivo Boquerón; 8 de Diciembre; Fernando de la Mora; Guaraní de Coronel Oviedo; Cerro Porteño "
  "PF; Cerro Porteño de Ciudad del Este; Ovetense; Capitán Figari",
  "16 dos 43 clubes sem escudo; o do 12 de Octubre é uma imagem genérica (círculo azul). Os 26 outros conferem (folha de contato).",
  "Escudos na Wikipédia es dos clubes / transfermarkt | SUGESTÃO: incluir em PAGINAS (Wikipédia es) os clubes tradicionais "
  "(Presidente Hayes, Sport Colombia, Colegiales, Cerro Corá, Atlántida); fonte: https://es.wikipedia.org/wiki/Club_Presidente_Hayes; "
  "mexer em: baixar_escudos.py PAGINAS",
  "SCRATCH/PY/escudos.png", "baixa", "banco-painel")
# 017
a("E nome único", "", "Olimpia",
  "'Olimpia' (PAR) e 'Olímpia' (BRA) só diferem no acento; sem acento colidem (o relatório da coleta diz que conferiu sem acento).",
  "banco: clube 'Olímpia' (BRA) | SUGESTÃO (decisão do Guilherme): manter 'Olimpia' (o mais conhecido) e chamar o brasileiro de "
  "'Olímpia-SP', ou aceitar; fonte: tabela clube do db/futebol.db; mexer em: futebol/ (cadastro do clube brasileiro)",
  "db/futebol.db (clube)", "baixa", "banco-painel")
# 018
a("D artilheiros faltando", "2014 Apertura; 2014 Clausura; 2015 Apertura; 2015 Clausura; 2016 Apertura; 2016 Clausura; 2017 "
  "Clausura; 2018 Clausura; 2019 Clausura; 2020 Clausura; 2021 Clausura; 2024 Clausura; 2025 Apertura; 2025 Clausura", "",
  "14 edições sem artilheiro (paratops vai até 2011 e a contagem só entra com 95% dos gols com autor).",
  "Wikipédia es (coluna Goleador): ex. 2015 Clausura Santiago Salcedo 19, 2019 Clausura Roque Santa Cruz 15, 2024 Clausura Redes, "
  "Ruiz Díaz e Ferreira 7; as páginas anuais da RSSSF têm 'Topscorers' | SUGESTÃO: ler 'Topscorers' de para20xx ou a coluna da "
  "Wikipédia es; fonte: " + WES + "; mexer em: coleta/par-1/importar.py artilheiros_rsssf()/TOPS",
  WES, "media", "coleta-sulamerica")
# 019
a("D artilheiro (gols)", "1935; 1962; 1963; 1967; 1970; 2003", "",
  "Pacote (paratops): 1935 Osorio 18, 1962 Cecilio Martínez 19, 1963 Juan Cabañas 17, 1967 Fleitas 18, 1970 Saturnino Arrúa 19, "
  "2003 Erwin Ávalos 17.",
  "Wikipédia es: 17, 17, 19, 18, 11, 16; a própria página do ano na RSSSF dá 1962 18 (para62 l.356) e 1967 16 (para67 l.306) | "
  "SUGESTÃO: conferir com a página do ano e, sem acordo, registrar a divergência na observação; fonte: " + WES + "; mexer em: "
  "coleta/par-1/explicacoes.py (nova lista de correções de artilheiros) e importar.py",
  WES + " ; " + RS + "paratops.html", "media", "coleta-sulamerica")
# 020
a("D gols com autor x placar", "2007", "Nacional de Asunción",
  "Sportivo Trinidense 2-2 Nacional (2007-04-08): 3 gols do Nacional (um gol da ESPN sem lado, aos 81', foi para o visitante).",
  "ESPN 213940: lance de 81' sem 'lado' | SUGESTÃO: descartar lance sem lado ou exigir soma total igual ao placar antes de usar "
  "os gols da ESPN; fonte: data/coleta/par-1/espn/par1_2007.json; mexer em: coleta/par-1/importar.py (bloco 'ge = es[\"ligado\"]') "
  "e outras_fontes.lances_espn()",
  "data/coleta/par-1/espn/par1_2007.json", "baixa", "coleta-sulamerica")
# 021
a("D jogador sem nome", "2006; 2007", "Sportivo Luqueño; Cerro Porteño; Sol de América",
  "19 gols do Sportivo Luqueño em 2006 com jogador '2' e 3 cartões com jogador '2'/'22' (ESPN).",
  "ESPN sem nome do jogador | SUGESTÃO: descartar nome só com dígitos (gol fica sem autor, sem minuto inventado); fonte: "
  "data/coleta/par-1/espn/par1_2006.json; mexer em: coleta/par-1/outras_fontes.lances_espn()",
  "data/coleta/par-1/pacote/gols.csv", "baixa", "coleta-sulamerica")
# 022
a("F site desatualizado", "", "",
  "O painel publicado é o do pacote antigo (7.794 jogos; 1994 com 13 clubes); o painel/dados/par-1.js local (22/11 09:53) já tem "
  "o pacote novo (7.849 jogos), mas traz a regressão dos vices de PY-002 (1999-2003 e 2020 Clausura).",
  "https://clubeanalitico.pages.dev/dados/par-1.js x painel/dados/par-1.js | SUGESTÃO: só publicar o par-1 novo depois de "
  "corrigir PY-001 a PY-005; mexer em: publicação (wrangler) do painel",
  "https://clubeanalitico.pages.dev/dados/par-1.js", "media", "banco-painel")
# 023
a("F tabela parcial com jogos", "1909; 1911; 1912; 1913; 1915; 1916; 1917; 1918; 1929; 1930; 1935; 1941; 1947; 1948; 1949; 1951; 1953; 1954; 1957; 1958; 1959; 1991", "",
  "87 linhas com J preenchido e V/E/D vazios aparecem com 0 pontos e '0 V · 0 E · 0 D' (ex.: 1917 Olimpia 0 pts, fonte 23; "
  "1991 'melhor ataque 0 gols em 11 jogos').",
  "classificacao_final.csv traz os pontos publicados | SUGESTÃO: marcar a linha como parcial quando V, E ou D for vazio (não só J) "
  "e esconder 'Destaques' quando a tabela é parcial; mexer em: gerar_dashboard_v2.py (bloco 'if da_fonte', ~l.651: "
  "publicada.get(...)[0] is None)",
  "https://clubeanalitico.pages.dev/?c=par-1#campeonato/classificacao/1917", "media", "banco-painel")
# 024
a("F participações", "", "Olimpia",
  "Olimpia aparece com '111ª participação' em 2025 Apertura e 110ª em 2024 Clausura; jogou todas as edições (as tabelas parciais e "
  "as edições só com campeão e vice deixam clubes de fora).",
  "Wikipédia es: 'el único equipo que ha participado en todas las ediciones es el Club Olimpia' | SUGESTÃO: avisar no painel que "
  "participações antes de 1996 são parciais ou contar só edições com tabela completa; mexer em: gerar_dashboard_v2.py (PART)",
  WES, "baixa", "banco-painel")
# 025
a("F estádios", "2007-2025", "",
  "Nomes de estádio com patrocinador atual aplicados a jogos antigos: 'Estadio ueno Defensores del Chaco' (620 jogos desde 2007), "
  "'Estadio UENO Osvaldo Domínguez Dibb', 'Estadio ueno La Nueva Olla', 'Estadio Tigo La Huerta'; e grafias duplas ('Luis Alfonso "
  "Giagni' x 'Estadio Luis Alfonso Giagni', 'Rogelio Livieres' x 'Rogelio Lorenzo Livieres').",
  "ESPN devolve o nome de hoje | SUGESTÃO: tabela de nomes de estádio (tirar 'ueno'/'Tigo', padronizar 'Estadio ...'); mexer em: "
  "coleta/par-1/importar.py (estadio = ge.get('estadio')) ou coleta/comum-sulamerica/espn.py",
  "data/coleta/par-1/pacote/partidas.csv (coluna estadio)", "baixa", "coleta-sulamerica")
# 026
a("F celular", "", "", "No celular (420 px) a página fica mais larga que a tela (já conhecido).",
  "Print SCRATCH/PY/telas/cel_campeonato_classificacao_1917.png | SUGESTÃO: pendência já registrada do agente 1; mexer em: painel/index.html (CSS)",
  "SCRATCH/PY/telas/cel_campeonato_classificacao_1917.png", "baixa", "banco-painel")
# 027
a("A edição faltando", "2026 Apertura", "Olimpia",
  "O pacote vai até 2025 Clausura; o Apertura 2026 já terminou (para2026.html está baixada).",
  "RSSSF parachamp: '2026 Olimpia (Apertura) Nacional' | SUGESTÃO: incluir '2026 Apertura' em edicoes._AC quando o Guilherme quiser "
  "o ano corrente; fonte: " + RS + "para2026.html; mexer em: coleta/par-1/edicoes.py _AC",
  RS + "parachamp.html", "baixa", "coleta-sulamerica")
# 028
a("A vice com empate na lista", "1926; 1927; 1952; 1953; 1964", "",
  "Pacote: 1926 Olimpia, 1927 Nacional, 1952 Sol de América, 1953 Cerro Porteño, 1964 Cerro Porteño.",
  "RSSSF parachamp lista dois vices: 1926 River Plate e Sol de América, 1927 Libertad e Nacional, 1952 Sol de América e Libertad, "
  "1953 Cerro Porteño e Libertad, 1964 Cerro Porteño e Nacional; a Wikipédia es escolhe River Plate, Libertad, Libertad, Libertad "
  "e Nacional; em 1926 a tabela de parahist tem Olimpia 2º (24 pts) | SUGESTÃO (decisão do Guilherme): ver decisoes_PY.md; mexer "
  "em: coleta/par-1/importar.py (VICES) ou explicacoes.py (vice escolhido)",
  RS + "parachamp.html ; " + WES, "media", "coleta-sulamerica")
# 029
a("C texto dos jogos", "2005", "General Caballero; Libertad; Olimpia",
  "2005-11-26 General Caballero awd Libertad: gols_texto com lixo ('Fernando Oliveira 41; Rodrigo López 75] 2-1'); a nota "
  "quebrada vai para Olimpia x 12 de Octubre ('used suspended player]').",
  "para05 l.572-575 (nota em duas linhas) | SUGESTÃO: CONSERTA_TEXTO juntando a nota; mexer em: coleta/par-1/explicacoes.py CONSERTA_TEXTO",
  RS + "para05.html", "baixa", "coleta-sulamerica")
# 030
a("C placares RSSSF x ESPN", "2007; 2010", "", "Placar da RSSSF mantido onde a ESPN diverge.",
  "Terceira fonte confirma a RSSSF: Libertad 3-1 Sol (2007-08-15) e 12 de Octubre 2-3 Cerro (2007-08-25) no Anexo de 2007 da "
  "Wikipédia es; Luqueño 3-1 Tacuary (2010-11-21) na tabela de confrontos do Clausura 2010. Sem 3ª fonte: 2 de Mayo 0-3 Nacional "
  "(2008-05-14; ESPN 0-4), Rubio Ñu 0-3 Cerro (2010-05-29; ESPN 0-2), Libertad 3-0 3 de Febrero (2011-05-21; ESPN 1-0); os autores "
  "da RSSSF somam o placar dela",
  "https://es.wikipedia.org/wiki/Anexo:Resultados_del_Campeonato_Paraguayo_de_F%C3%BAtbol_2007", "baixa", "coleta-sulamerica",
  "nao-e-erro")
# 031
a("Ficha (documentação)", "", "",
  "A ficha diz 'completa em 1943, 1945, 1955 e 1990-1995' (1990-1995 são tabelas de uma fase), lista 'Edições com menos jogos que o "
  "esperado' com edições que têm MAIS jogos (1965: 134 de 40) e a seção 7 está vazia (explicacoes.py não tem nenhuma correção; "
  "as 12 edições divergentes têm só o diagnóstico automático, que não acha a causa real: torneios misturados).",
  "Ver PY-004 e PY-005 | SUGESTÃO: corrigir o texto e o rótulo (mais/menos) no gerador; mexer em: coleta/comum-sulamerica/documentar.py "
  "e o texto do relatório em coleta/par-1/importar.py relatorio()",
  "coleta/comum-sulamerica/documentacao/par-1.md", "baixa", "coleta-sulamerica")

with open(sys.argv[1], "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "competicao", "item", "edicao", "clube", "o_que_esta_no_painel", "o_que_a_fonte_diz", "fonte", "gravidade",
                "quem_corrige", "situacao"])
    w.writerows(A)
print(len(A), "achados")
