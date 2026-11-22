"""Gera SCRATCH/achados_CO.csv (achados da revisão do col-1, 3ª rodada, 22/11/2026). Uso: python -I revisao/CO/achados_csv.py <saida.csv>"""
import csv, sys

C = "col-1"
RS = "https://www.rsssf.org/tablesc/"
WK = "https://es.wikipedia.org/wiki/Categor%C3%ADa_Primera_A (Títulos por temporada)"
A = []


def a(item, edicao, clube, painel, fonte_diz, fonte, grav, quem):
    A.append([item, edicao, clube, painel, fonte_diz, fonte, grav, quem, "aberto"])


a("A vice", "55 edições: 1955, 1957, 1958, 1959, 1961, 1969, 1970, 1976, 1978, 1979, 1981, 1982, 1984, 1989, 1992, 1993, 1994, 1995/96, "
  "1996/97, 2000, 2001, 2002 Ap e Fi, 2004 Ap e Fi, 2006 Ap, 2007 Ap, 2008 Ap e Fi, 2009 Ap e Fi, 2010 Ap, 2011 Ap e Fi, 2012 Ap, 2013 Fi, "
  "2014 Ap, 2015 Ap, 2016 Ap e Fi, 2017 Ap e Fi, 2018 Fi, 2019 Ap e Fi, 2021 Ap e Fi, 2022 Ap e Fi, 2023 Ap e Fi, 2024 Ap e Fi, 2025 Ap e Fi",
  "vários (lista em revisao/CO/lista_vices.txt)",
  "vice = 2º da classificação do pacote (ex.: 2002 Ap Deportivo Cali; 2024 Fi Independiente Santa Fe; 1989 Atlético Nacional sem haver campeão); "
  "o Pódio e o 3º lugar da História e do Resumo também saem errados (Nacional aparece com 15 vices)",
  "RSSSF colchamp (coluna Runners Up, que a coleta não leu) e Wikipédia es concordam nas 101 edições: ex. 2002 Ap Atlético Nacional (perdeu a final "
  "para o América), 2024 Fi Deportes Tolima, 1957 Deportes Tolima, 1976 Deportivo Cali, 1989 sem vice | SUGESTÃO: vice = coluna Runners Up da "
  "colchamp.html em todas as edições (1989 vazio); fonte: " + RS + "colchamp.html; mexer em: coleta/col-1/ler_rsssf.py campeoes() (ler o grupo 4, "
  "'Runners Up') e coleta/col-1/importar.py gravar() (vice = lista, não final[1]) + classificacao() (pôr o vice em 2º como já faz com o campeão)",
  RS + "colchamp.html ; " + WK, "alta", "coleta-sulamerica")
a("B classificação", "2002 Apertura a 2025 Finalización (todas com fase final) e 1967, 1976, 1996/97, 1999, 2000, 2001", "vários",
  "classificação final = tabela da 1ª fase da RSSSF com só o campeão puxado para o 1º; finalistas e semifinalistas ficam onde estavam na 1ª fase "
  "(2002 Ap: Atlético Nacional, vice, em 4º; varredura: semifinalista fora do top 4 em 2011 Ap e Fi, 2015 Ap, 2016 Ap e Fi, 2017 Ap e Fi, 2018 Fi, 2020 Ap, 2021 Ap)",
  "o campeão sai da final; vice = perdedor da final; 3º/4º = semifinalistas ou 2º dos quadrangulares (RSSSF colNN, seções Cuadrangulares/Final) | "
  "SUGESTÃO: ordenar por fase alcançada (Final > quadrangular/semifinal > quartas > 1ª fase) e, dentro de cada nível, pela ordem da tabela "
  "publicada da 1ª fase; vice da colchamp em 2º; fonte: " + RS + "col02.html (Cuadrangulares/Final); mexer em: coleta/col-1/importar.py classificacao() "
  "(hoje usa 'pub' sem olhar o nível; aplicar a ordenação por nivel também quando há tabela publicada)",
  RS + "col02.html ; " + RS + "col2014.html", "alta", "coleta-sulamerica")
a("B classificação", "1987, 1991, 1992, 1993, 1994, 1995 (sem jogos)", "todos",
  "classificação com todos os números 0 (J, V, E, D, gols e pontos), em ordem alfabética depois do campeão e do 2º; 1995 com 19 clubes, "
  "incluindo 3 da Primeira B (Atlético Bucaramanga, Real Cartagena, Unicosta) e marcando Unicosta como estreante; no ar (print c_1995_classificacao)",
  "RSSSF traz a tabela final de cada ano (col95: 'Final Table Primera A', 16 clubes, Junior 30 18 8 4 66-37 62; Tuluá -2 pts; Cúcuta relegated) | "
  "SUGESTÃO: usar a tabela final da RSSSF como classificação (como a ficha diz que faz) e só os clubes da Primera A; fonte: " + RS + "col95.html, "
  "col87.html, col91.html a col94.html; mexer em: coleta/col-1/edicoes.py (trecho 'tabelas' desses anos) e o leitor de tabela "
  "(tabelas_publicadas.csv não tem nenhuma linha de 1987 e 1991-1995: a tabela não é lida), importar.classificacao() (ramo e.sem_jogos)",
  RS + "col95.html", "alta", "coleta-sulamerica")
a("C jogos", "1955, 1958, 1959, 1960, 1961, 1963, 1966", "todos",
  "metade (ou 2/3) dos jogos: 1955 90 de 135; 1958 90 de 180; 1959 130 de 264; 1960 132 de 264; 1961 132 de 264; 1963 156 de 312; 1966 350 de 364. "
  "A classificação é calculada desses jogos (1960: 22 jogos por clube em vez de 44) e dá vice errado em 1955, 1958, 1959, 1961",
  "RSSSF 'Final Table' de cada ano (1960: 12 clubes x 44 jogos; Wikipédia es 1960 tem 'Tercera vuelta' e 'Cuarta vuelta'; 1963: 52 fechas, "
  "312 jogos) | SUGESTÃO: ler as 4 voltas e as listas 'Fecha N' da Wikipédia es (1963: o leitor pegou só a matriz e só o 1º placar de cada "
  "célula, que traz 2 jogos '6:2 / 1:1'); conferir com a tabela da RSSSF (hoje esses anos saem como 'sem tabela para conferir': a tabela não é lida); "
  "fonte: " + RS + "col60.html, col63.html; https://es.wikipedia.org/wiki/Campeonato_colombiano_1960; mexer em: coleta/col-1/wikipedia_jogos.py jogos() "
  "(matriz com 2 placares por célula; seções 'Tercera/Cuarta vuelta'); conferência em coleta/col-1/conferir.py. Lista por clube: revisao/CO/saida_tabela_anual.txt",
  RS + "col60.html ; " + RS + "col63.html", "alta", "coleta-sulamerica")
a("C jogos", "1964", "todos",
  "467 jogos (72 por clube) e classificação com J=72 (no ar, print c_1964_classificacao)",
  "RSSSF col64: 13 clubes x 48 jogos = 312; Wikipédia es tem a matriz (156 jogos, só o 1º placar) E a lista 'Fecha 1..52' (311 jogos): o leitor "
  "pegou as duas | SUGESTÃO: só a lista 'Fecha N' (com data); descartar a matriz quando a seção tem lista; falta 1 jogo (Deportivo Cali x Deportes "
  "Quindío, 71 jogos cada); fonte: " + RS + "col64.html; mexer em: coleta/col-1/wikipedia_jogos.py jogos() (regra 'numa mesma seção com lista e "
  "matriz, fica a lista' não pega quando estão em seções diferentes: 'Resultados' x 'Resultados por fecha')",
  RS + "col64.html", "alta", "coleta-sulamerica")
a("C jogos", "1986, 1988, 1989, 1976", "todos",
  "1986: só 21 jogos do octogonal e 8 dos 14 clubes na classificação; 1988: Finalización com 12 jogos por clube (de 28), 222 jogos no total; "
  "1989: 32 jogos e 8 clubes (sem Apertura e Finalización); 1976: Hexagonal final com 20 de 30 jogos (faltam todos com Atlético Nacional ou "
  "Deportes Quindío em casa) — por isso o vice de 1976 sai Millonarios",
  "RSSSF col86 (tabelas do Apertura e Clausura, 14 clubes), col88 (Finalización 28 jogos por clube), col89 ('318 matches'), col76 (Final Hexagonal, "
  "Round 1 a 10 com 3 jogos cada); Wikipédia es 1989 tem 'Fecha 1 (Marzo 5)'... de Apertura e Finalización | SUGESTÃO: 1976 e 1988: completar "
  "pela RSSSF (jogos da fase final em texto) e pela Wikipédia; 1989: ler as listas 'Fecha N (data)' da Wikipédia es; 1986: classificação pelas "
  "tabelas da RSSSF (Apertura + Clausura) com os 14 clubes; fonte: " + RS + "col76.html, col86.html, col88.html, col89.html; mexer em: "
  "coleta/col-1/wikipedia_jogos.py e coleta/col-1/edicoes.py (trechos da RSSSF para as fases finais 1976/1988)",
  RS + "col76.html ; " + RS + "col89.html", "alta", "coleta-sulamerica")
a("B rebaixados", "1992 a 2025 (45 rebaixamentos)", "lista em revisao/CO/saida_rebaixados.txt",
  "só 1 rebaixado marcado (Boyacá Chicó, 2021 Apertura); os outros 45 sem 'rebaixado' (ex.: 2011 Fi América de Cali e Deportivo Pereira; "
  "2024 Fi Patriotas e Jaguares; 2025 Fi Unión Magdalena e Envigado)",
  "Wikipédia es Anexo Ascensos y descensos (46 rebaixamentos 1992-2025) e as seções 'Relegation' das páginas da RSSSF (ex.: col2024: "
  "'decided over points average') | SUGESTÃO: dicionário REBAIXADOS {temporada: [clubes]} na última edição de cada ano e situacao='rebaixado'; "
  "fonte: https://es.wikipedia.org/wiki/Anexo:Ascensos_y_descensos_de_la_Categor%C3%ADa_Primera_A ; mexer em: coleta/col-1/importar.py situacao() "
  "(hoje só marca quando a linha da tabela tem 'relegated') e um dicionário novo em coleta/col-1/explicacoes.py",
  "https://es.wikipedia.org/wiki/Anexo:Ascensos_y_descensos_de_la_Categor%C3%ADa_Primera_A", "alta", "coleta-sulamerica")
a("C datas", "48 edições de 1995/96 a 2024 Finalización (finais, semifinais, quartas)", "vários",
  "jogos de mata-mata com a data e a rodada do último jogo com data (ex.: 2024 Fi final Tolima x Nacional e Nacional x Tolima os dois em "
  "2024-12-08; 2014 Ap quartas, semis e final todos em 2014-05-04, rodada 18); varredura: 'clube 2 jogos no mesmo dia' em 143 casos",
  "RSSSF escreve 'First Leg [Dec 18]' / 'Second Leg [Dec 22]' (col2024 linhas 938-942); ESPN e Wikipédia es confirmam (2024 Fi: 18/12 e 22/12; "
  "2016 Ap: 15/06 e 19/06) | SUGESTÃO: ler a data de 'First/Second Leg(s) [Mon DD]' e '[Mon DD]' soltos; quando a ESPN casou o jogo e a data "
  "difere >1 dia, usar a da ESPN; rodada vazia nos mata-matas; fonte: " + RS + "col2024.html; mexer em: coleta/col-1/ler_rsssf.py (FECHA/_torneios) "
  "ou rsssf_sul (armadilha já descrita no COMECE-AQUI, seção 6) e coleta/col-1/importar.py (data = data or ESPN). Lista: revisao/CO/saida_datas_repetidas.txt "
  "e revisao/CO/saida_datas_espn.txt",
  RS + "col2024.html ; ESPN placar diário col.1", "media", "coleta-sulamerica")
a("C jogo ligado errado", "2025 Finalización", "Junior de Barranquilla; Deportes Tolima",
  "final: ida em 2025-05-31 17:30 (público 16.483) e volta em 2025-04-15 20:30 (público 18.000), com cartões de outros jogos; varredura: "
  "'Final' fora de ordem",
  "Wikipédia es Torneo Finalización 2025 (== Final ==): {{fecha|12|12|2025}} Junior 3:0 Tolima e {{fecha|16|12|2025}} Tolima 0:1 Junior; a ESPN "
  "casada (736069, 730445) é do Apertura (1-1 e 0-0); os certos são 762528 (público 46.692) e 762529 | SUGESTÃO: datas 2025-12-12 e 2025-12-16, "
  "ESPN 762528/762529; fonte: https://es.wikipedia.org/wiki/Torneo_Finalizaci%C3%B3n_2025_(Colombia) ; mexer em: coleta/col-1/wikipedia_jogos.py "
  "(ler {{fecha|DD|MM|AAAA}} do {{Partido}}) e coleta/col-1/outras_fontes.py espn() (sem data, exigir placar igual para casar)",
  "https://es.wikipedia.org/wiki/Torneo_Finalizaci%C3%B3n_2025_(Colombia)", "media", "coleta-sulamerica")
a("C datas", "1957; 1971", "Independiente Medellín, Cúcuta Deportivo; Independiente Santa Fe, Atlético Nacional",
  "1957 final em 1957-03-19 e 1957-03-23 (antes do início do torneio, 31/03); 1971 desempate do título em 1971-01-30, 1971-02-03 e 1971-02-10",
  "Wikipédia es 1957: desempate 'diciembre 08/1957-febrero 02/1958', final 19 e 23 de março (de 1958); Wikipédia es 1971 'Desempate final': "
  "'El 10 de febrero de 1972' | SUGESTÃO: 1958-03-19, 1958-03-23; 1972-01-30, 1972-02-03, 1972-02-10; fonte: "
  "https://es.wikipedia.org/wiki/Campeonato_colombiano_1971 ; mexer em: coleta/col-1/wikipedia_jogos.py _data() (data sem ano depois da virada "
  "do ano = ano + 1)", "https://es.wikipedia.org/wiki/Campeonato_colombiano_1971", "media", "coleta-sulamerica")
a("C fases", "1969 a 1999 (Finalización) e todas com quadrangulares/hexagonais/octogonais", "—",
  "fase 'Finalización' gravada como mata_mata / ida_volta (fases.csv) e os quadrangulares, hexagonais e octogonais também; no Resumo: "
  "'Quadrangulares semifinais: mata-mata · ida e volta · 8 clubes' (print c_2002_Apertura_resumo)",
  "RSSSF: Finalización é liga (às vezes em 2 grupos) e os quadrangulares/hexagonais são grupos de pontos corridos (col02 'Cuadrangulares: Tables "
  "Group A/B') | SUGESTÃO: Finalización tipo liga/grupos; quadrangulares, hexagonais e octogonais tipo grupos (pontos corridos, 2 grupos quando "
  "houver); fonte: " + RS + "col75.html, col02.html; mexer em: coleta/col-1/conferir.py eh_mata() ('Finalización'.startswith('Final'), armadilha "
  "do COMECE-AQUI) e coleta/col-1/importar.py gravar() (tipo da fase)", RS + "col02.html", "media", "coleta-sulamerica")
a("C grupos", "2001 a 2024 (menos 2012-2014) e 1989, 1995/96, 1999; 1ª fase de 2002 Ap a 2025 Fi (33 edições)", "—",
  "quadrangulares com os 24 jogos no grupo 'B' (os do grupo A também); 1989/1995-96/1999 sem grupo; 425 jogos da 1ª fase com grupo A ou B "
  "(os jogos entre clubes que depois caíram no mesmo quadrangular), e o painel diz 'Primeira fase: grupos · 2 grupos' (print c_2002_Apertura_resumo)",
  "RSSSF col02: 1ª fase é uma tabela única de 18 clubes (22 rodadas); 'Group A: Nacional, Magdalena, Cali, Pasto / Group B: América, Santa Fe, "
  "Envigado, Bucaramanga' | SUGESTÃO: grupo do quadrangular pelo clube (tabelas Group A/B que vêm antes das rodadas); 1ª fase sem grupo; fonte: "
  + RS + "col02.html linhas 492-506; mexer em: coleta/col-1/ler_rsssf.py ler() (linhas 176-190, grupo herdado de _torneios) e _torneios()",
  RS + "col02.html", "media", "coleta-sulamerica")
a("C fases", "1957", "vários",
  "'Octogonal final' com 8 jogos (3 rodadas) do octogonal que foi cancelado, como fase válida (mata_mata, jogo_unico); os dois hexagonais "
  "(grupos A e B) num grupo só; o desempate do grupo A (Medellín, Pereira, Tolima) como 'Desempate do título'; Cúcuta x Tolima (3 jogos) dentro do "
  "'Hexagonal final'",
  "Wikipédia es 1957: '== Octogonal (Cancelado) ==', '== Grupos hexagonales == Grupo A / Grupo B', 'Desempate Grupo A', Final Medellín x Cúcuta | "
  "SUGESTÃO: octogonal como jogos anulados (resultado_especial n/p) ou fora; hexagonais com grupo A/B; desempates com o nome certo; fonte: "
  "https://es.wikipedia.org/wiki/Campeonato_colombiano_1957 ; mexer em: coleta/col-1/wikipedia_jogos.py FASES (títulos de seção) e "
  "coleta/col-1/explicacoes.py CORRIGE", "https://es.wikipedia.org/wiki/Campeonato_colombiano_1957", "media", "coleta-sulamerica")
a("C fases", "1974, 1976, 1979, 1980, 1982; 1999", "vários",
  "'Desempate do título' para as finais do Apertura (julho: 1974 Nacional x Cali, 1976 Junior x Millonarios, 1979 América x Cali, 1980 Junior x Cali, "
  "1982 Cali x América) — varredura: fase fora de ordem em 1979; 1999: 'Final' com 4 jogos e 3 clubes (inclui a Final Clausura Medellín x Nacional)",
  "Wikipédia es: 'En el Apertura [1980] disputaron la final, la cual ganaría Junior'; RSSSF col99 'Final Clausura' (linha 669) x 'Championship "
  "Final' (linha 699) | SUGESTÃO: fase 'Final do Apertura' / 'Final do Finalización' (nível 0, não decide o título); fonte: " + RS + "col99.html; "
  "mexer em: coleta/col-1/ler_rsssf.py FASES e coleta/col-1/wikipedia_jogos.py FASES; NIVEL_FASE em coleta/col-1/importar.py",
  RS + "col99.html", "media", "coleta-sulamerica")
a("C placares", "1948, 1949, 1974, 1977, 1979, 2001 e jogos 2005-2018 com a ESPN", "vários",
  "1948: Junior 3-2 Universidad e Universidad 0-4 Junior (mando trocado); 1949: Santa Fe x Medellín 2 vezes com o Santa Fe em casa (falta Medellín "
  "3-2 Santa Fe), América 3-1 Boca (fonte 3-4), América 0-1 Cali (1-4), Cali 1-0 Universidad (3-0), Dep. Barranquilla 0-1 Once Caldas (1-0); 1974 Cali "
  "2-2 América (0-0); 1977 Nacional 1-0 Cali (2-0); 1979 Cali 2-0 Magdalena (0-0); 2001 América 2-2 Once Caldas (Wikipédia es 0-0); ESPN difere em "
  "2005 Fi América 3-2 Once Caldas (2-1), 2006 Ap Envigado 2-0 Pereira (1-0), 2006 Ap Millonarios 1-1 Cúcuta (1-0), 2007 Fi Nacional 2-0 América "
  "(1-0), 2010 Ap Pereira 1-2 Cali (1-3), 2018 Fi semifinal Medellín 2-1 Tolima (2-2)",
  "RSSSF Cross-Table col48/col49 (fonte independente da Wikipédia, base da coleta nesses anos), jogos das fases finais col74-col79, Wikipédia es 2001, "
  "ESPN | SUGESTÃO: corrigir 1948-1949 pela tabela de confrontos da RSSSF (que fecha com a tabela publicada); os de 2001-2018 conferir numa 3ª fonte "
  "(transfermarkt, ficha do jogo) antes de mudar; mexer em: coleta/col-1/explicacoes.py CORRIGE (hoje vazio). Lista: revisao/CO/saida_amostra.txt",
  RS + "col48.html ; " + RS + "col49.html", "media", "coleta-sulamerica")
a("B ajustes de pontos", "1983 a 1999 (fases finais) e 1995", "vários",
  "bônus das fases finais não aplicados (ajuste só em 1996/97); 1995 sem os -2 pontos do Tuluá (edição sem tabela)",
  "RSSSF 'Bonus Table' em col83-col88, col93, col94; '[BP: 1.5]' em col98; 'Top-4 of Apertura and Finalizacion obtain bonus points' em col90-col92; "
  "col95 '11.Deportivo Tulua ... [2 pts deducted]' | SUGESTÃO: bônus em ajuste_pontos da fase final (e na classificação final), com a "
  "observação; fonte: " + RS + "col84.html, col98.html, col95.html; mexer em: coleta/col-1/importar.py classificacao() e explicacoes.py",
  RS + "col84.html ; " + RS + "col98.html", "media", "coleta-sulamerica")
a("D artilheiros", "1971, 1977, 1978; 2008-2025", "vários",
  "1977 e 1978 sem artilheiro; 1971 só Lóndero (falta Apolinar Paniagua, 30); 2008+ (contagem dos gols com autor): sem artilheiro em 2009 Ap, "
  "2013 Ap, 2013 Fi, 2014 Fi, 2015 Ap, 2015 Fi, 2016 Ap, 2017 Fi, 2018 Ap, 2018 Fi; nome/gols diferentes em 2008 Ap, 2010 Ap, 2011 Ap, 2011 Fi, "
  "2017 Ap, 2019 Ap, 2024 Ap, 2024 Fi",
  "RSSSF coltops: '1977 Oswaldo Marcial PALAVECINO (Arg.) Atlético Nacional 33', 1978 idem 36, 1971 Paniagua 30 (Pereira); a coltops acaba em 2007; "
  "Wikipédia es (Máximo goleador): 2013 Ap Wilder Medina 12, 2016 Ap Miguel Borja 19, 2018 Fi Germán Cano 20, 2024 Ap Carlos Bacca e Hugo Rodallega 12 | "
  "SUGESTÃO: regex aceitar 1 espaço entre '(Arg.)' e o clube e as linhas de empate; de 2008 em diante usar a lista da Wikipédia es; fonte: "
  + RS + "coltops.html; " + WK + "; mexer em: coleta/col-1/importar.py artilheiros_rsssf() e o ramo 'contagem dos gols com autor'. Lista: "
  "revisao/CO/saida_artilheiros.txt", RS + "coltops.html ; " + WK, "media", "coleta-sulamerica")
a("D gols com autor", "2007 Apertura; 2008 Finalización; 2010 Apertura", "vários",
  "mais gols com autor que o placar: 2007 Ap Santa Fe 1-1 Cali (autores 1+3); 2008 Fi Pasto 1-0 Huila (1+1); 2010 Ap Pereira 1-2 Cali (1+3)",
  "placar da RSSSF x lances da ESPN do mesmo jogo (ESPN 2010: Pereira 1-3 Cali) | SUGESTÃO: só gravar os gols quando a soma por lado bate com o "
  "placar; conferir o placar numa 3ª fonte; mexer em: coleta/col-1/importar.py gravar() (gols da RSSSF + da ESPN no mesmo jogo)",
  "pacote gols.csv x partidas.csv", "media", "coleta-sulamerica")
a("A clubes por edição", "1986, 1989, 1995", "—",
  "num_clubes 8 (1986), 8 (1989), 19 (1995)",
  "RSSSF/Wikipédia es: 14 (1986), 15 (1989), 16 (1995) | SUGESTÃO: sai junto com a correção dos jogos e das tabelas (achados de 1986/1989 e 1995); "
  "fonte: " + RS + "col86.html, col95.html; mexer em: coleta/col-1/importar.py (num_clubes = clubes da classificação)",
  RS + "col86.html ; " + WK, "baixa", "coleta-sulamerica")
a("C cobertura de datas", "1952-1963, 1968-1988", "—",
  "datas vazias (ex.: 1952-1961 0%, 1968 1%, 1975 0%), embora a Wikipédia es traga a data no título da rodada",
  "Wikipédia es: 'Fecha 1 — 1 de marzo de 1964', 'Fecha 1 septiembre 14' (1957), 'Fecha 1 (Marzo 5)' (1989); contagem por ano em "
  "revisao/CO/saida_cobertura_datas.txt | SUGESTÃO: ler a data do título da rodada nos formatos 'Fecha N (mes D)', '!Fecha N mes D', "
  "'Fecha NN (mes DD)'; fonte: https://es.wikipedia.org/wiki/Campeonato_colombiano_1975 ; mexer em: coleta/col-1/wikipedia_jogos.py _data() e "
  "contexto()", "https://es.wikipedia.org/wiki/Campeonato_colombiano_1975", "baixa", "coleta-sulamerica")
a("C jogos suspensos", "2008 Apertura; 2013 Finalización", "Independiente Medellín x Boyacá Chicó; Once Caldas x Millonarios",
  "jogo suspenso guardado como linha 'abd' além do jogo completado (varredura: jogo repetido)",
  "RSSSF col08 linha 328 'abandoned at 1-0 ... due to rain' + linha 330 'remaining time' | SUGESTÃO: descartar a 1ª linha em CORRIGE (regra do "
  "COMECE-AQUI, seção 6) e datar o complemento; mexer em: coleta/col-1/explicacoes.py CORRIGE", RS + "col08.html", "baixa", "coleta-sulamerica")
a("Seção 3 documentação", "38 edições com tabela divergente", "—",
  "explicacoes.py está vazio (nenhuma correção, nenhuma explicação); as divergências ficam só com a frase automática 'placar diferente em algum "
  "jogo (a página não diz qual)' ou 'o erro é desta tabela' (falso em 1988: a tabela col88:78 é a do Finalización, com 28 jogos, e faltam jogos); "
  "'menos jogos que o esperado' falso em 1969-1985 (o esperado soma a tabela anual); logs dizem 'RSSSF' em anos que vêm da Wikipédia",
  "achados de jogos e placares acima | SUGESTÃO: cada divergência com explicação ou correção em explicacoes.py; esperados() só com tabelas da mesma "
  "fase; mexer em: coleta/col-1/importar.py esperados() e diagnostico(), coleta/col-1/explicacoes.py", "docs/coleta/col-1.md", "baixa", "coleta-sulamerica")
a("E escudo", "—", "Huracán de Medellín",
  "escudo do Huracán argentino (globo com 'H'), homônimo",
  "o clube é o Huracán de Medellín (1949-1952), sem relação com o Club Atlético Huracán | SUGESTÃO: tirar o escudo (deixar sem) até achar um do "
  "próprio clube; mexer em: baixar_escudos.py (PAGINAS / espn_auto.json) e data/escudos/", "painel/index.html ESCUDOS; folha SCRATCH/CO/escudos.png",
  "baixa", "banco-painel")
a("E escudo", "—", "Atlético Manizales, Centauros Villavicencio, Deportivo Barranquilla, Deportivo Samarios, Leones FC, Libertad de Barranquilla, Oro Negro, Unicosta",
  "8 clubes sem escudo", "SUGESTÃO: Wikipédia es de cada clube (Leones: 'Itagüí Leones'; Centauros: 'Centauros Villavicencio'); mexer em: baixar_escudos.py PAGINAS",
  "painel/index.html ESCUDOS", "baixa", "banco-painel")
a("F celular", "—", "—", "no celular (420 px) a página fica mais larga que a tela (cartões cortados à direita) — pendência já conhecida do agente 1",
  "print SCRATCH/CO/telas/cel_campeonato_classificacao_2002_20Apertura.png | SUGESTÃO: a do agente 1; mexer em: painel/index.html (CSS)",
  "print do site", "baixa", "banco-painel")
# verificados e certos
A.append(["A campeões", "101 edições", "—", "campeão de cada edição", "RSSSF colchamp e Wikipédia es: 101 de 101 batem (1989 sem campeão); títulos "
          "por clube batem (Nacional 18, Millonarios 16, América 15, Junior 11 até 2025...)", RS + "colchamp.html ; " + WK, "baixa", "coleta-sulamerica", "nao-e-erro"])
A.append(["F curiosidades", "1951, 1952, 1957", "—", "maior goleada Samarios 12-1 Universidad (1951); fora Samarios 1-11 Quindío (1952); mais gols "
          "Medellín 9-5 Santa Fe (1957)", "Wikipédia es Categoría Primera A, 'Otros datos > Goles': os três recordes batem", WK, "baixa", "banco-painel", "nao-e-erro"])
A.append(["E clubes", "—", "42 clubes", "nomes únicos no banco; identidades (Deportes Caldas = Once Caldas, Municipal = Nacional, Cristal Caldas = Once "
          "Caldas, Itagüí = Águilas Doradas, La Equidad = Internacional de Bogotá, Alianza Petrolera = Alianza FC)", "RSSSF colchamp (1950 Once Caldas) e "
          "Wikipédia es ('[[Once Caldas|Deportes Caldas]]') confirmam; nenhum homônimo sem cidade", RS + "colchamp.html ; " + WK, "baixa", "coleta-sulamerica", "nao-e-erro"])

with open(sys.argv[1], "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "competicao", "item", "edicao", "clube", "o_que_esta_no_painel", "o_que_a_fonte_diz", "fonte", "gravidade", "quem_corrige", "situacao"])
    for k, r in enumerate(A, 1):
        w.writerow([f"CO-{k:03d}", C] + r)
print(len(A), "linhas")
