"""Grava SCRATCH/achados_SP.csv com os achados da revisão do Paulista (bra-sp-1)."""
import csv, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
OUT = r"C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/achados_SP.csv"
PT = "https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol"
EN = "https://en.wikipedia.org/wiki/Campeonato_Paulista"


def ed(a):
    return f"https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_{a}"


S = "bra-sp-1"
A = []


def add(item, edicao, clube, painel, fonte_diz, fonte, grav, quem, sit="aberto"):
    A.append([f"SP-{len(A)+1:03d}", S, item, edicao, clube, painel, fonte_diz, fonte, grav, quem, sit])


# SP-001
add("A título dividido", "1973", "Santos; Portuguesa",
    "Campeã só a Portuguesa; Santos aparece como vice (pódio; Corrida dos títulos com Santos 21). Sem nota na edição.",
    "A FPF declarou os dois campeões (cobranças de pênaltis encerradas por engano por Armando Marques); o Palmeiras herdou o vice. Santos tem 22 títulos. Como mostrar 2 campeões: decisão do Guilherme.",
    f"{PT} (seção Campeões, nota de 1973); {EN} (Champions: 1973 Portuguesa e Santos, vice Palmeiras)", "alta", "coleta-brasil")
# SP-002
add("A vice", "1906, 1913 LPF, 1916 APEA, 1927 APEA, 1927 LAF, 1928 APEA, 1930, 1942, 1951, 1957, 1976, 1978, 1997, 2003", "",
    "Vices: 1906 AA das Palmeiras; 1913 LPF SC Internacional-SP; 1916 APEA Ypiranga-SP; 1927 APEA Corinthians; 1927 LAF Germânia; 1928 APEA Palmeiras; 1930 Palmeiras; 1942 São Paulo; 1951 Jabaquara; 1957 Corinthians; 1976 Guarani; 1978 Corinthians; 1997 Santos; 2003 Botafogo-SP",
    "Vices: 1906 SC Internacional (a AA das Palmeiras foi eliminada); 1913 LPF Ypiranga; 1916 APEA AA São Bento; 1927 APEA Santos; 1927 LAF Hespanha (Jabaquara); 1928 APEA Santos; 1930 São Paulo; 1942 Corinthians; 1951 Palmeiras; 1957 Santos; 1976 XV de Piracicaba; 1978 São Paulo; 1997 São Paulo; 2003 São Paulo. 119 de 134 vices batem. Causas em SP-007 a SP-013.",
    f"{EN} (Champions, coluna Runners-up); {PT} (Campeões, coluna Vice-campeão). Lista: revisao/SP/saida_podio.txt", "alta", "coleta-brasil")
# SP-003
add("A 3º lugar", "1906, 1908, 1913 LPF, 1914 LPF, 1916 APEA, 1917, 1927 APEA, 1927 LAF, 1928 APEA, 1928 LAF, 1930, 1942, 1951, 1954, 1957, 1959, 1971, 1976, 1978, 1984, 1988, 1989, 1990, 1997, 1998, 1999, 2003, 2008, 2025", "",
    "3º do banco/painel diferente da fonte em 29 edições (ex.: 1998 Inter de Limeira, 1999 Araçatuba, 2003 Atlético Sorocaba, 2025 São Bernardo)",
    "3º da fonte: 1998 Portuguesa, 1999 São Paulo, 2003 Portuguesa Santista, 2025 São Paulo (semifinalista) etc. 98 de 128 batem (2010 Barueri = Grêmio Prudente, mesmo clube: não é erro).",
    f"{PT} (Campeões, coluna Terceiro colocado). Lista: revisao/SP/saida_podio.txt", "media", "coleta-brasil")
# SP-004
add("A edições", "2026", "Palmeiras; Novorizontino",
    "O painel vai de 1902 a 2025 (selo '1902 a hoje'); falta a edição de 2026, já encerrada",
    "2026: Palmeiras campeão, Novorizontino vice (3º São Paulo, 4º Corinthians)",
    f"{EN} (Champions, 2026); {PT} (Campeões, 2026)", "media", "coleta-brasil")
# SP-005
add("A edições", "1933, 1934", "Albion; Fiorentino (Juventus)",
    "Só os campeonatos da APEA (Palestra Itália) em 1933 e 1934",
    "As listas da Wikipédia pt e en trazem também os campeonatos da FPF (amadora): 1933 Albion (vice União Guarany) e 1934 Fiorentino (vice Hespanha). Reconhecer ou não: decisão do Guilherme.",
    f"{PT} (Campeões, linhas 1933 e 1934 FPF); {EN} (Champions, 1933 e 1934 FPF)", "media", "coleta-brasil")
# SP-006
add("A edições", "1970, 1972, 1973, 1974", "",
    "Banco com 10/12/12/14 clubes: só a fase principal",
    "A Wikipédia conta 16/18/18/21 participantes: houve fase preliminar ('Paulistinha') com os clubes do interior, classificatória para o Paulistão. Se entra: decisão do Guilherme.",
    f"{ed(1970)} (Regulamento); {ed(1972)} (Regulamento); {ed(1974)} (Regulamento)", "baixa", "coleta-brasil")
# SP-007
add("B classificação (fase decisiva)", "1951, 1998, 1999, 2003", "",
    "Repescagem/Torneio de rebaixamento conta como a fase mais avançada: 1951 Jabaquara 2º e XV de Jaú 3º; 1998 Inter de Limeira, Portuguesa Santista, Araçatuba e Juventus em 3º-6º; 1999 Araçatuba, União São João, Ituano e São José em 3º-6º; 2003 Botafogo-SP 2º (e rebaixado) e Atlético Sorocaba 3º. A varredura acusa 'fase fora de ordem' (essas fases com ordem 1)",
    "Vices: 1951 Palmeiras, 2003 São Paulo; 3º: 1998 Portuguesa, 1999 São Paulo, 2003 Portuguesa Santista. Repescagem e quadrangular da morte não decidem o pódio.",
    f"{EN}; {PT}; {ed(1999)} (Regulamento: Quadrangular da Morte); revisao/SP/varredura_saida.txt", "alta", "coleta-brasil")
# SP-008
add("B classificação (fase final)", "1957, 1976, 1978, 1997, 2024, 2025", "",
    "A fase final não decide a ordem: 1957 (fase final 'Série Azul') Corinthians 2º; 1976 Guarani 2º; 1978 a 'Final' gravada é a decisão do 1º turno (Corinthians 1x0 Santos, 26/11/1978) e a final de junho/1979 (Santos x São Paulo) está em 'Primeira fase'; 1997 quadrangular final ignorado (Santos 2º); 2025 quartas, semis e final dentro de 'Fase única' (formato 'pontos corridos'; 3º São Bernardo); 2024 a final está dentro da fase 'Semifinal'",
    "Vices: 1957 Santos, 1976 XV de Piracicaba, 1978 São Paulo, 1997 São Paulo; 2025: 3º São Paulo e 4º Santos (semifinalistas)",
    f"{EN}; {PT}; {ed(1997)} (Classificação geral); {ed(2025)}", "alta", "coleta-brasil")
# SP-009
add("B/C clube trocado", "1927 APEA", "Corinthians; Corinthians de Santo André",
    "13 jogos do Corinthians de Santo André gravados como Corinthians (29 jogos; 'Corinthians 4x1 Corinthians' em 31/07/1927); jogo repetido Palmeiras x Corinthians em 21/08/1927 (11x2 e 3x1). Corinthians 2º",
    "Tabela final: Palestra Itália 16 jogos (14-1-1); Santos 2º (16 jogos, 14-0-2); Corinthians 3º com 16 jogos (12-0-4)",
    f"{ed('1927_(APEA)')} (Classificação final); revisao/SP/varredura_saida.txt (clube contra ele mesmo, jogo repetido)", "alta", "coleta-brasil")
# SP-010
add("B/C jogos a mais", "1927 LAF", "",
    "15 clubes e até 13 jogos por clube; entram Corinthians (5 jogos), Independência-SP, EC Sírio, Sílex e Taubaté; Germânia 2º",
    "Tabela final com 10 clubes e 9 jogos cada; vice Hespanha (Jabaquara), 3º Paulista",
    f"{ed('1927_(LAF)')} (Classificação final); {EN}", "alta", "coleta-brasil")
# SP-011
add("C jogo falso", "1928 LAF", "Paulista; LAF",
    "Jogo 'Paulista 127 x 0 LAF' (data 0000-00-00, só no ogol) contra um clube 'LAF' (sem cidade nem escudo): entra na classificação (13 clubes) e vira recorde no painel: maior goleada e jogo com mais gols (História > Estatísticas), 'Paulista: 156 gols em 23 jogos' (mais gols numa edição), 691 gols e 5,16 por jogo em 1928 LAF",
    "Não existe; a maior goleada do Paulista é Paulistano 12x0 AA das Palmeiras (16/05/1920). 1928 LAF teve 12 clubes.",
    f"{PT} (Maiores goleadas > Em toda a história); {ed('1928_(LAF)')} (infobox: 12 participantes); docs/coleta/bra-sp-1.md (1928 LAF)", "alta", "coleta-brasil")
# SP-012
add("B/C jogo faltando", "1942", "Palmeiras; Corinthians",
    "109 jogos; Palmeiras e Corinthians com 19 jogos (falta Corinthians x Palmeiras); São Paulo 2º com 32 pts, Corinthians 3º com 31",
    "110 jogos; Corinthians 2º (20 jogos, 15-3-2, 33 pts), São Paulo 3º (32); Palmeiras 17-2-1",
    f"{ed(1942)} (Classificação final); {EN}", "alta", "coleta-brasil")
# SP-013
add("B punição", "1930", "Palmeiras; São Paulo",
    "Palmeiras 2º com 42 pts (18-6-2), São Paulo 3º com 41",
    "Palestra Itália 3º com 40 pts com a mesma campanha 18-6-2 (2 pontos a menos); São Paulo vice com 41",
    f"{ed(1930)} (Classificação final); {EN} (1930 vice São Paulo)", "alta", "coleta-brasil")
# SP-014
add("B/C clube trocado", "1988", "Juventus-SP; Ponte Preta; Bandeirante-SP",
    "2º turno com Juventus-SP no lugar de outro clube: 21 jogos do Juventus, 'Juventus x Juventus' em 29/05/1988, jogos repetidos em 25/05 e 05/06 e Juventus com 2-3 jogos no mesmo dia; Ponte Preta (2 jogos) e Bandeirante-SP (12) a mais; 22 clubes e 239 jogos",
    "20 clubes, 217 jogos e 497 gols (banco: 533)",
    f"{ed(1988)} (infobox); revisao/SP/varredura_saida.txt", "media", "coleta-brasil")
# SP-015
add("B rebaixamento", "1994, 1998, 1999, 2002, 2014, 2015, 2017, 2018, 2019, 2020, 2022, 2023, 2024", "",
    "Sem marca de rebaixado: 2014 (Atlético Sorocaba, Comercial-RP, Oeste, Paulista), 2015 (Bragantino, Marília, Penapolense, Portuguesa), 2017 (Osasco Audax, São Bernardo), 2018 (Linense, Santo André), 2019 (São Bento, São Caetano), 2020 (EC Água Santa, Oeste), 2022 (Novorizontino, Ponte Preta), 2023 (Ferroviária-SP, São Bento), 2024 (Ituano, Santo André). Marcados e que jogaram o ano seguinte: 1994 Mogi Mirim; 1998 Inter de Limeira, Portuguesa Santista, Araçatuba; 1999 Araçatuba, União São João; 2002 Portuguesa Santista",
    "Rebaixados conforme a participação no ano seguinte e as páginas das edições; em 1998 e 1999 só os 2 últimos do quadrangular da morte caem",
    f"Banco: classificacao_final.situacao x participação no ano seguinte; {ed(1999)} (Regulamento)", "alta", "coleta-brasil")
# SP-016
add("B W.O. fora da classificação", "1905, 1908, 1909, 1910", "",
    "Vitórias dadas sem placar (awd) não contam na classificação: 1908 Americano-SP 7 jogos e CA Internacional-SP 6; 1909 Germânia 8 jogos e 5º lugar; o painel conta 21.839 de 21.855 jogos",
    "A tabela conta o W.O. como vitória/derrota (1909: Germânia 10 jogos, 2-1-7, 4º; 'Atlética ganha 2 pontos')",
    f"{ed(1909)} (Tabela e Classificação Final); {ed(1908)}", "media", "coleta-brasil")
# SP-017
add("B critério de desempate", "1971, 1984, 2008", "",
    "1971: Portuguesa 3º (mais vitórias), Corinthians 4º e Santos 5º (todos com 28 pts); 1984: Palmeiras 3º com 52 pts, São Paulo 4º com 51; 2008: Guaratinguetá 3º, São Paulo 4º",
    "1971: Corinthians 3º, Santos 4º (desempate por saldo, como no regulamento de 1974); 1984: São Paulo 3º com 53 pts, Palmeiras 50 (pontos diferentes com a mesma campanha); 2008: São Paulo 3º (41 pts), Guaratinguetá 4º (40)",
    f"{ed(1971)}; {ed(1984)} (Classificação final); {ed(2008)} (Classificação geral); {ed(1974)} (Regulamento)", "baixa", "coleta-brasil")
# SP-018
add("B classificação", "1929 LAF", "",
    "Portuguesa Santista 5º (20 pts), Independência-SP 6º, Paulista 10º (14 pts), AA das Palmeiras 12º (16 jogos)",
    "Portuguesa Santista 8º (18 pts), Independência 4º (21), Paulista 12º (11), AA das Palmeiras 11º (17 jogos); há jogos 'só no ogol' incluídos",
    f"{ed('1929_(LAF)')} (Classificação final)", "media", "coleta-brasil")
# SP-019
add("C total de jogos e gols", "1916 LPF, 1920, 1921, 1928 APEA, 1935 APEA, 1957, 1958, 1960, 1977, 1999, 2002, 2016", "",
    "Banco: 1916 LPF 47 jogos; 1920 80; 1921 132; 1928 APEA 47 (212 gols); 1935 APEA 58; 1957 370; 1958 1.329 gols; 1960 306 (1.052 gols); 1977 379; 1999 174 (590 gols); 2002 134 jogos e 13 clubes; 2016 158 (411 gols)",
    "Infobox: 1916 LPF 51; 1920 82; 1921 131; 1928 APEA 44 (199); 1935 APEA 54; 1957 371; 1958 1.387 gols; 1960 312 (1.069); 1977 360; 1999 162 (555); 2002 140 jogos e 16 clubes; 2016 150 (387). As diferenças de 2008-2013 e 2017-2023 são o Troféu do Interior/Taça Independência, que a coleta tirou de propósito (não é erro).",
    "Infobox das páginas https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_<ano>; lista: revisao/SP/saida_infobox.txt", "media", "coleta-brasil")
# SP-020
add("C placar", "1904, 1905, 1916 LPF, 1946, 2021", "",
    "1904-08-21 SC Internacional-SP 5x0 AA das Palmeiras; 1905-09-23 Mackenzie-SP 5x2 AA das Palmeiras; 1916 LPF sem Corinthians x Americano (03/12/1916); 1946-04-14 São Paulo 4x0 Jabaquara; 2021-03-23 Mirassol 0x1 Corinthians",
    "1904: 5x1; 1905: AA das Palmeiras 5x2 Mackenzie; 1916: Corinthians 3x0 Americano; 1946: São Paulo 5x0 Jabaquara; 2021: Mirassol 1x1 Corinthians (fonte única: em dúvida)",
    f"{ed(1904)} (Tabela); {ed(1905)}; {ed('1916_(LPF)')}; {ed(1946)}; https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_2021_-_Série_A1 (Confrontos)", "media", "coleta-brasil")
# SP-021
add("C datas", "1907 a 2022 (28 edições)", "",
    "72 casos de clube com 2 jogos no mesmo dia; os maiores: 1978 (14, em maio/1979), 1988 (11), 1927 APEA (5), 1949 (4); ex.: 13/03/2022 Palmeiras x Santos e Ferroviária x Santos",
    "Um clube não joga duas vezes no mesmo dia: uma das datas está errada (ou o jogo é de outra fase)",
    "revisao/SP/varredura_saida.txt; revisao/SP/datas_repetidas_saida.txt", "baixa", "coleta-brasil")
# SP-022
add("C observações", "1905 a 1968", "",
    "Observações dos jogos em inglês no pacote/banco (ex.: 'victory awarded to Americano', 'match postponed from 1º Turno', 'São Paulo AC withdrew from the championship...'), '*' em 6 jogos de 1940 e 3 jogos sem data (um com 0000-00-00)",
    "Em português, como pedido na revisão da Copa (CB-015)",
    "data/coleta/bra-sp-1/pacote/partidas.csv (coluna observacao)", "baixa", "coleta-brasil")
# SP-023
add("D artilheiro", "2001, 2009, 2010, 2012, 2013, 2017, 2019, 2023", "",
    "Artilheiro do banco (fonte 'contagem dos gols com autor'): 2001 Washington 14; 2009 Keirrison 13; 2010 Rodriguinho 15; 2012 Neymar 15; 2013 Neymar 12; 2017 só Gilberto 9; 2019 5 empatados com 6; 2023 só Róger Guedes 8",
    "Oficial: 2001 Washington 16; 2009 Pedrão (Grêmio Barueri) 15/16; 2010 Ricardo Bueno (Oeste) 16; 2012 Neymar 20; 2013 William (Ponte Preta) 13; 2017 Gilberto e William Pottker 9; 2019 Jean Mota 7; 2023 Galoppo e Róger Guedes 8. Batem: 2011, 2015, 2016, 2020, 2021",
    f"{PT} (Estatísticas > Artilheiros); {EN} (Top scorers)", "media", "coleta-brasil")
# SP-024
add("D artilheiro ausente", "1902-2000, 2002-2008, 2014, 2018, 2022, 2024, 2025", "",
    "Só 13 edições têm artilheiro no banco",
    "A lista da Wikipédia pt tem o artilheiro de 125 edições (1902 a 2026)",
    f"{PT} (Estatísticas > Artilheiros); revisao/SP/artilheiros_wiki.json", "media", "coleta-brasil")
# SP-025
add("F aba Artilharia", "1951, 1999, 2000, 2003, 2004, 2014, 2018, 2022, 2024, 2025", "",
    "A aba Artilharia mostra como 1º a contagem parcial dos gols com autor: 1951 Guanxuma 1 gol; 1999 Dinei 1; 2000 Marcelinho 3; 2003 Ricardo Oliveira 7; 2004 Vágner Love 11; 2018 Borja 5; 2022 Raphael Veiga 4; 2024 Flaco López 4; 2025 Gabriel (Mirassol) 2. O card 'Maior artilheiro' dos clubes usa a mesma conta (ex.: Paulista, Marcelo Macedo 9)",
    "Artilheiros: 1951 Carbone 30; 1999 Alex 12; 2000 França 18; 2003 Luís Fabiano 8; 2004 Vágner Love 12; 2018 Borja 7; 2022 Ronaldo 9; 2024 Flaco López 10; 2025 Guilherme 10. Com cobertura de 1% a 36% dos gols, o painel deveria avisar ou esconder",
    f"{PT} (Artilheiros); https://clubeanalitico.pages.dev/?c=bra-sp-1#campeonato/artilharia/2025", "media", "banco-painel")
# SP-026
add("E clube duplicado", "1914 a 1933", "AA São Bento; São Bento de São Paulo",
    "Dois cadastros: 'AA São Bento' (1914-1932, campeão 1914 APEA e 1925) e 'São Bento de São Paulo' (só 1933, com 'AA São Bento' em clube_nome), com escudos diferentes",
    "É a Associação Atlética São Bento da capital nos dois casos; juntar ou não: decisão do Guilherme",
    "Banco: clube_id 766 e 816; docs/coleta/bra-sp-1.md (1914 APEA, 1925, 1933)", "media", "coleta-brasil")
# SP-027
add("E clube e cidade", "1934 a 1936", "CA Paulista; ECPaulista",
    "'ECPaulista' (só 1935 LPF, cidade São Carlos, nome sem espaço) separado de 'CA Paulista' (1934 e 1936, São Paulo, com 'EC Paulista' em clube_nome)",
    "Provável mesmo clube da capital (decisão do Guilherme); o nome de exibição está sem espaço",
    "Banco: clube_id 784 e 778", "baixa", "coleta-brasil")
# SP-028
add("E nomes e cadastro", "", "Red Bull Bragantino II; Humberto Primeiro; Juventus-SP; União Barbarense; Inter de Limeira",
    "Red Bull Brasil (2015-2019) aparece como 'Red Bull Bragantino II'; Humberto Primeiro com cidade 'Vila Mariana' (bairro); São Caetano EC com cidade 'São Caetano'; nomes estranhos em clube_nome: Juventus-SP com 'Ponte Preta', União Barbarense com 'União Bandeirante', Inter de Limeira com 'Internacional-SP'/'Internacional' (colide com o SC Internacional-SP de 1902-1932)",
    "Nome de época Red Bull Brasil (Wikipédia 2016, 2018, 2019); cidades São Paulo e São Caetano do Sul; nome de outro clube não deve casar",
    "Banco: tabelas clube e clube_nome", "baixa", "banco-painel")
# SP-029
add("E escudos", "", "Oeste; LAF",
    "Sem escudo: Oeste (já conhecido, Wikimedia 429) e 'LAF' (não é clube, ver SP-011). Folha dos 115 clubes olhada: nenhum escudo trocado visível",
    "—", "SCRATCH/SP/escudos.png (folha de contato)", "baixa", "banco-painel")
# SP-030
add("F celular", "", "",
    "No celular (420 px) a página fica mais larga que a tela (cartões e abas cortados à direita) — já conhecido",
    "—", "SCRATCH/SP/telas/420_*.png", "baixa", "banco-painel")
# SP-031
add("C jogos (amostra)", "1904-1925, 1929 LAF, 1945, 1946, 1956, 2018-2025", "",
    "1.477 jogos achados na Wikipédia: 1.464 com o mesmo placar",
    "As diferenças estão em SP-020; 2022 bate 96/96 e 2023-2025 batem 100%",
    "revisao/SP/saida_jogos.txt", "baixa", "coleta-brasil", "nao-e-erro")
# SP-032
add("D gols com autor", "todas", "",
    "2.239 jogos com autor: a soma dos gols nunca passa do placar e sempre fecha (6.405 gols)",
    "—", "Banco (consulta da revisão)", "baixa", "coleta-brasil", "nao-e-erro")

with open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow("id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao".split(","))
    w.writerows(A)
print(len(A), Counter((a[8], a[10]) for a in A))
