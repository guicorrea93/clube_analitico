"""Grava SCRATCH/achados_ES.csv (achados da revisão do esp-1). Uso: python -I revisao/ES/gravar_achados.py CAMINHO_CSV"""
import csv, sys

W = "https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_"
C = "esp-1"
A = [
    ("A rebaixados", "1935/36", "Real Oviedo; Atlético de Madrid",
     "Banco/pacote (classificacao_final.situacao): Real Oviedo, 3º colocado, marcado como rebaixado (regra 'não está na temporada seguinte'). "
     "Atlético de Madrid (11º) não marcado. No painel não aparece (a Corrida pinta 11º-12º)",
     "Oviedo não caiu: teve dispensa por ter o estádio destruído na guerra; ficou fora de 1939/40 com a vaga reservada para 1940/41. "
     "Caíram Athletic de Madrid (11º) e Osasuna (12º); o Atlético voltou na repescagem pela vaga do Oviedo (Athletic de Madrid 3-1 Osasuna, Valência, 26/11/1939)",
     W + "1935-36 (ficha 'Descendidos' e nota_OVI da tabela); " + W + "1939-40 (nota_ATM)", "media", "coleta-europa", "aberto"),
    ("B classificação", "1986/87", "Racing Santander; Cádiz; Osasuna",
     "Faltam os 3 jogos do triangular de rebaixamento. Classificação: 16º Osasuna, 17º Racing (rebaixado), 18º Cádiz (não rebaixado): o rebaixado aparece acima de quem ficou",
     "Triangular entre os 3 últimos do grupo de rebaixamento: Racing 1-1 Cádiz, Cádiz 1-1 Osasuna, Osasuna 2-0 Racing; Osasuna 1º, Cádiz 2º, Racing 3º e rebaixado (único rebaixado; a liga passou a 20)",
     W + "1986-87 (Play-off Descenso); https://en.wikipedia.org/wiki/1986%E2%80%9387_La_Liga (Relegation playoffs)", "alta", "coleta-europa", "aberto"),
    ("B classificação", "1979/80", "AD Almería; CD Málaga",
     "Sub-aba Classificação conta os gols do W.O. CD Málaga 0-1 AD Almería (30/03/1980): Almería GP 42, Málaga GC 59. O banco (classificacao_final) tem 41 e 58",
     "Tabela oficial: o W.O. vale a vitória mas não os gols: Almería 41 GP, Málaga 58 GC (RSSSF, en e es.wikipedia; o próprio relatório da coleta diz isso)",
     W + "1979-80 (Clasificación); docs/coleta/esp-1.md (1979/80)", "media", "banco-painel", "aberto"),
    ("F Corrida faixas", "1965/66; 1989/90; 1993/94; 1997/98; 2014/15", "",
     "A faixa vermelha 'rebaixamento' da Corrida pinta as últimas N posições (N = nº de rebaixados): 1965/66 pinta 14º-16º, 1989/90 18º-20º, 1993/94 18º-20º, 1997/98 18º-20º, 2014/15 18º-20º (Eibar 18º, que ficou)",
     "Quem caiu: 1965/66 13º CD Málaga (promoción), 15º e 16º; 1989/90 17º CD Málaga (promoción), 19º e 20º; 1993/94 17º Rayo (promoción), 19º e 20º; "
     "1997/98 17º Compostela (promoción), 19º e 20º; 2014/15 13º Elche (descenso administrativo), 19º e 20º",
     W + "AAAA-AA (estado_X=D e resultadoN de cada tabela); revisao/ES/zonas_wiki.py", "baixa", "coleta-europa", "aberto"),
    ("D artilheiro", "1929/30; 1934/35; 1935/36; 1954/55; 2003/04", "Gorostiza; Lángara; Arza; Ronaldo",
     "Gols do artilheiro: 1929/30 Gorostiza 19; 1934/35 Lángara 26; 1935/36 Lángara 28; 1954/55 Arza 28; 2003/04 Ronaldo 25",
     "Lista do Trofeo Pichichi na es.wikipedia: 20, 27, 27 (nota: Marca 27, LFP 28; o relatório de coleta diz que fica 'a contagem do Marca'), 29 e 24. "
     "Em 2003/04 os gols por jogador do próprio banco (ESPN) também dão 24 ao Ronaldo",
     "https://es.wikipedia.org/wiki/Trofeo_Pichichi (Trofeo Pichichi de 1ª División); revisao/ES/compara_pichichi.py", "baixa", "coleta-europa", "aberto"),
    ("D nomes de jogadores", "2001/02 a 2008/09", "vários",
     "Nomes da ESPN fora de ordem ou trocados, que aparecem em Por clube > Artilharia: 'Kahveci Nihat' (76 gols), 'Fernando Sanchez Morientes', 'Ismael Aranda Urzaiz', "
     "'Mendez Ruben Navarro', 'Mocelin Magno', 'Alsocer Raul Molina', 'Bortolini Pimentel Savio', 'Fernandez Manuel Gutierrez Victor', 'Víctor -'. "
     "O mesmo jogador partido em dois: 'Ballesta Salva' (2001-05, 27 gols) + 'Salvador Ballesta Vialcho' (2005-09, 16)",
     "Nihat Kahveci, Fernando Morientes, Ismael Urzaiz, Rubén Navarro, Magno Mocelin, Raúl Molina, Sávio, Víctor Fernández; Salva Ballesta (43 gols somados)",
     "banco (tabela gol, fonte ESPN); print SCRATCH/ES/telas/1400_clube_artilharia_alaves.png", "baixa", "coleta-europa", "aberto"),
    ("F aba Por campeonato/Artilharia", "2001/02 a 2024/25", "",
     "Nas 24 temporadas com gols por jogador (24.048 gols com autor), a sub-aba Artilharia mostra só o artilheiro oficial (1 linha); "
     "o ranking de gols por jogador não aparece (ex.: 2003/04 só 'Ronaldo 25')",
     "Mostrar a lista oficial e também o ranking de gols por jogador que o banco tem",
     "https://clubeanalitico.pages.dev/?c=esp-1#campeonato/artilharia/2003/04 (print SCRATCH/ES/telas/1400_campeonato_artilharia_2003_04.png); painel/index.html função artilharia()",
     "baixa", "banco-painel", "aberto"),
    ("F aba História/Curiosidades", "1983/84", "Athletic Bilbao; Real Madrid",
     "Campeões > 'Título mais apertado: Athletic Bilbao · 1983 · -2 pontos à frente · vice Real Madrid' (conta 3 pontos por vitória numa temporada de 2)",
     "1983/84 com 2 pontos por vitória: Athletic e Real Madrid com 49 pontos (empate; Athletic campeão no desempate). "
     "Há 6 títulos empatados em pontos: 1930/31, 1946/47, 1959/60, 1970/71, 1980/81 e 1983/84",
     "https://clubeanalitico.pages.dev/?c=esp-1#historia/curiosidades (Campeões; print SCRATCH/ES/telas/cur_campeoes.png); " + W
     + "1983-84; gerar_dashboard_v2.py (vant = pts - (3*V+E) do vice)", "media", "banco-painel", "aberto"),
    ("F aba História/Curiosidades", "1962/63", "Real Madrid",
     "Campeões > 'Maior vantagem sobre o vice: Real Madrid 21 pontos à frente · 1962 · vice Atlético de Madrid' (pontos refeitos com 3 por vitória)",
     "1962/63 com 2 pontos por vitória: Real Madrid 49 x Atlético 37 = 12. Em pontos reais, a maior vantagem é Barcelona 2012/13 (100 x 85 = 15)",
     W + "1962-63; conta no banco (pontos_vitoria de cada edição)", "media", "banco-painel", "aberto"),
    ("F aba História/Curiosidades", "", "",
     "Campeões > cartão 'Títulos por estado' mostra uma linha '?' com os 94 títulos (cartão pensado para os estados do Brasil)",
     "Esconder o cartão nas ligas estrangeiras (ou trocar por região)",
     "print SCRATCH/ES/telas/cur_campeoes.png", "baixa", "banco-painel", "aberto"),
    ("F aba Por campeonato/Classificação", "1979/80; 2003/04; 2014/15; 1994/95; 1986/87", "CD Málaga; Racing Santander; Almería; Elche",
     "Punições e casos de tribunal não são explicados (o desconto entra na coluna Pts, sem nota): 1979/80 CD Málaga -3 (W.O.); 2003/04 Racing -1; "
     "2014/15 Almería -3 e Elche (13º) rebaixado por dívidas, Eibar (18º) fica. ED.nota vazio em todas as edições, embora edicao.observacao tenha as punições",
     "Nota curta na edição (o banco já tem o texto em edicao.observacao). Ajudaria também em 1994/95 (Valladolid 19º e Albacete 17º salvos pela ampliação para 22) "
     "e 1986/87 (formato com fase final)",
     W + "1979-80, 2003-04 e 2014-15 (notas das tabelas)", "baixa", "banco-painel", "aberto"),
    ("E escudos", "", "CD Málaga; AD Almería",
     "CD Málaga (1949-1992) usa o escudo do Málaga CF atual (escrito 'MÁLAGA C.F.'); AD Almería (1979-81) usa o escudo da UD Almería ('U D ALMERÍA'). "
     "Já previsto no pedido 4 da coleta (o ogol junta os dois Málaga)",
     "Escudos próprios do CD Málaga e da AD Almería (es.wikipedia: Club Deportivo Málaga, Agrupación Deportiva Almería)",
     "folha de contato SCRATCH/ES/folha.png (63 escudos)", "baixa", "banco-painel", "aberto"),
    ("E nomes de época", "1928/29 a 1971/72", "Atlético de Madrid; Athletic Bilbao; Real Madrid; Espanyol",
     "O painel mostra sempre o nome atual: o campeão de 1939/40 e 1940/41 aparece como 'Atlético de Madrid' (era Atlético Aviación); 'Athletic Bilbao' nos anos do nome "
     "castelhanizado (Atlético de Bilbao, 1941-1972); 'Real Madrid' em 1931-1941 (Madrid FC); 'Espanyol' (Español). Os nomes estão no banco (clube_nome), mas não aparecem",
     "Nomes de época nas fontes (es.wikipedia de cada temporada, ogol)",
     W + "1939-40; clubes.csv do pacote (nomes_fonte)", "baixa", "banco-painel", "aberto"),
    ("F datas no texto", "todas", "",
     "Cartões, eixos e chips usam o ano de início: 'de 1928 a 2024' (a última é 2024/25), Pódio com '1931' para 1931/32, 'último título em 2020' (2020/21), "
     "'Valencia campeão em 1970 e de novo só em 2001'. Já conhecido (resposta do agente 1 ao pedido 5: nas contas e nos eixos continua o ano de início)",
     "Temporada '1931/32' (ou o ano de fim) onde o texto fala de uma edição",
     "prints SCRATCH/ES/telas/1400_historia_podio.png e cur_campeoes.png", "baixa", "banco-painel", "aberto"),
    ("C jogos", "1932/33", "Athletic Bilbao; Racing Santander",
     "Athletic 9-5 Racing (05/02/1933): recorde de gols num jogo (14) no painel",
     "A página da temporada na es.wikipedia traz 9-4 (tabela e matriz), mas o anexo de estatísticas da es.wikipedia e a en.wikipedia (AS.com) confirmam 9-5; RSSSF e ogol também",
     "https://es.wikipedia.org/wiki/Anexo:Estad%C3%ADsticas_de_la_Primera_Divisi%C3%B3n_de_Espa%C3%B1a; https://en.wikipedia.org/wiki/La_Liga_records_and_statistics",
     "media", "coleta-europa", "nao-e-erro"),
    ("C jogos", "1928/29; 1934/35; 2006/07", "Atlético de Madrid; Real Oviedo; Valencia; Levante; Gimnàstic; Real Sociedad",
     "11 jogos do Atlético em 1928/29, Oviedo 4-4 Valencia (1934/35), Atlético 1-0 Levante e Gimnàstic 1-3 Real Sociedad (2006/07)",
     "A matriz da es.wikipedia diverge, mas não fecha com a própria tabela (ex.: Atlético 1928/29 daria 69-37; a tabela diz 43-41); o banco fecha com a tabela e com RSSSF, ogol e football-data",
     W + "1928-29, 1934-35 e 2006-07 (Resultados); revisao/ES/compara_jogos.py", "media", "coleta-europa", "nao-e-erro"),
    ("B classificação", "2018/19", "Valladolid; Celta",
     "Valladolid 16º e Celta 17º (41 pontos)",
     "A es.wikipedia inverte, mas o confronto direto (Celta 3-3 Valladolid, Valladolid 2-1 Celta) põe o Valladolid à frente; RSSSF e en.wikipedia como o painel",
     W + "2018-19", "alta", "coleta-europa", "nao-e-erro"),
    ("B punições", "1979/80", "Salamanca",
     "Salamanca 9º, sem desconto de pontos",
     "A tabela da es.wikipedia desconta 2 pontos (Málaga 0-3 Salamanca anulado em 20/06/1980), mas a nota da própria página diz que o CSD revogou a sanção em 08/05/1981; RSSSF: resultado confirmado",
     W + "1979-80 (nota_SAL)", "media", "coleta-europa", "nao-e-erro"),
    ("E clubes", "", "CD Málaga x Málaga; AD Almería x Almería; Burgos x Real Burgos",
     "Clubes separados no painel",
     "A es.wikipedia também os trata como clubes diferentes (artigos e códigos separados nas tabelas); separação coerente",
     W + "1979-80, 1999-2000 e 1990-91 (nombre_X das tabelas)", "baixa", "coleta-europa", "nao-e-erro"),
    ("F celular", "todas", "",
     "Nos prints a 420 px a página parece mais larga que a tela",
     "Medido: o Chrome sem janela não desce de 504 px de largura; nessa largura scrollWidth = 489 (não transborda). O corte nos prints vem do Chrome headless, não do painel",
     "SCRATCH/ES/medida.html (innerWidth/scrollWidth = 504/489 em #campeonato/classificacao/2024/25)", "baixa", "banco-painel", "nao-e-erro"),
]

with open(sys.argv[1], "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow("id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao".split(","))
    for i, (item, ed, cl, painel, fonte_diz, fonte, g, q, s) in enumerate(A, 1):
        w.writerow([f"ES-{i:03d}", C, item, ed, cl, painel, fonte_diz, fonte, g, q, s])
print(len(A), "achados")
