# Fontes avaliadas — Campeonato Português (`por-1`), revisão de 22/11/2026

A coleta usou: ogol (base), RSSSF (tabelas, matrizes até 2004/05, campeões, artilheiros), engsoccerdata, football-data,
ESPN e Wikipédia en (só as tabelas). As fontes abaixo são as que a revisão usou ou testou.

### Wikipédia pt (páginas de temporada)
- endereço: https://pt.wikipedia.org/wiki/Primeira_Divis%C3%A3o_de_1950%E2%80%9351 (1938/39-1998/99), https://pt.wikipedia.org/wiki/Primeira_Liga_de_2005%E2%80%9306 (1934/35-1937/38 e 1999/00+)
- cobre: classificação final (85 de 92 temporadas legíveis), matriz de resultados (74 temporadas), campeão e vice (infobox), artilheiro (infobox), seção "Despromovidos" (33 temporadas; de 2018/19 em diante ela lista os rebaixados da temporada anterior), textos sobre rebaixamentos administrativos (Leça 1997/98, Gil Vicente 2005/06) e a devolução dos pontos do Porto (2007/08)
- como baixar: em lote; HTML pela API parse (`action=parse&prop=text`), 92 páginas; leitor em revisao/PT/ptw.py
- amostra: placares 16.072 de 16.143 iguais ao pacote (as diferenças são quase todas erro da pt: 1943/44 troca Porto e Olhanense na matriz; 2009/10 Belenenses x Sporting invertido); tabelas: 61 de 85 idênticas, ~45 linhas com erro de digitação da pt (ponto ou gol trocado); campeões 92/92; vice 92/92 contra o pacote, menos 1944/45 (a pt está certa)
- serve a: coleta-europa; buscar: ordem de desempate (2005/06, 1944/45), rebaixamentos fora de campo, 1986/87 Braga x Benfica

### Transfermarkt (calendário completo por temporada)
- endereço: https://www.transfermarkt.com/primeira-liga/gesamtspielplan/wettbewerb/PO1?saison_id=1950 (ano de início)
- cobre: todos os jogos de 1934/35 a 2025/26 com rodada, data e placar; na página do jogo (`/x/index/spielbericht/<id>`): árbitro, público e marcadores, de ~1990 em diante (amostra 1990/91 e 2010/11 com árbitro; 1975/76 sem gols)
- como baixar: em lote (1 página por temporada, 92 páginas) para placar e data; jogo a jogo para árbitro, público e marcadores (~11 mil páginas de 1990/91 em diante); leitor em revisao/PT/tm.py
- amostra: 20.918 de 20.936 placares iguais (99,9%; as 18 diferenças estão no relatório); datas 19.413 de 20.936 iguais
- armadilhas: 1935/36 e 1936/37 chama o Vitória de Setúbal de "Vitória Guimarães SC"; 1941/42 junta Académica e Académico do Porto ("Académico FC"); junta SL Elvas e O Elvas; datas de 1935/36-1937/38 com um ano a menos; antes de 1994/95 põe todos os jogos na data da rodada (os sábados viram domingo); 1936/37 permuta 3 placares de 07/03/1937; a tabela do site é calculada por saldo (não serve para desempate)
- serve a: coleta-europa; buscar: árbitro e público (0% no pacote), marcadores de 1990/91 a 2005/06, terceira opinião de placar

### Wikipédia en — matrizes das temporadas (já baixadas pela coleta, não usadas para jogos)
- endereço: https://en.wikipedia.org/wiki/1980%E2%80%9381_Primeira_Divis%C3%A3o (arquivos em data/coleta/por-1/wikipedia/*.wiki, parâmetros `match_XXX_YYY`)
- cobre: matriz de resultados da maioria das temporadas
- como baixar: já está no disco (em lote)
- amostra: nos 8 jogos discutidos (1963/64, 1965/66, 1974/75, 1980/81) bateu com o Transfermarkt e a pt
- serve a: coleta-europa; buscar: segunda opinião de placar sem baixar nada

### Wikipédia en — artigos de temporada de clube (ex.: Benfica)
- endereço: https://en.wikipedia.org/wiki/1994%E2%80%9395_S.L._Benfica_season
- cobre: todos os jogos do clube na temporada, com data, placar, marcadores com minuto, público, árbitro e link do relatório do foradejogo.net; notas de decisões fora de campo com fonte de jornal (1986/87)
- como baixar: jogo a jogo por clube e temporada (`{{Football box collapsible}}`); leitor em revisao/PT/boxes.py
- amostra: decidiu 1994/95 Benfica 1-2 Sporting (PT-002) e 1986/87 Braga x Benfica (PT-004); 1980/81 parcial
- serve a: coleta-europa; buscar: jogos disputados dos grandes (Benfica; ver se há artigos de Porto e Sporting)

### Wikipédia en — "Bola de Prata (Portugal)"
- endereço: https://en.wikipedia.org/wiki/Bola_de_Prata_(Portugal)
- cobre: artilheiro de cada temporada, com gols e jogos
- como baixar: em lote (1 página)
- amostra: 87 de 92 batem com o pacote; das 5 diferenças, 4 são erro da en (1945/46, 1946/47, 1948/49 digitação; 1973/74 leitura) e 1 é erro do pacote (2018/19 Seferović 23, não 33)
- serve a: coleta-europa; buscar: conferência de artilheiros

### RSSSF — páginas de temporada com marcadores (port00 a port06)
- endereço: https://www.rsssf.org/tablesp/port01.html (port06.html já está em data/coleta/por-1/rsssf/)
- cobre: resultados rodada a rodada com marcadores de 1999/00 a 2005/06 (port99 parcial; port98 e anteriores não têm)
- como baixar: em lote (7 páginas)
- amostra: 2000/01, 297 jogos lidos por um leitor simples, soma dos gols fecha com o placar em 284
- serve a: coleta-europa; buscar: gols com autor de 1999/00 a 2005/06 (hoje 0%)

### ogol — ficha do jogo
- endereço: https://www.ogol.com.br/jogo.php?id=10409
- cobre: marcadores com minuto, placar do intervalo, motivo de resultado administrativo
- como baixar: jogo a jogo (~14 mil jogos antes de 2006/07)
- amostra: 5 fichas de 1963/64 e 1965/66 trazem marcadores que fecham com o placar do pacote (PT-008); a ficha de Espinho x Benfica 1980/81 lista 2 gols num 3-0 (PT-007). Atenção: o `fonte_id` do pacote (ogol:NNNN) nem sempre é o id da ficha (`jogo.php?id=`): 4 de 9 ids abriram outro jogo
- serve a: coleta-europa; buscar: marcadores e cartões antes de 2006/07; motivo dos jogos fora de campo

### football-data.co.uk (data)
- endereço: data/coleta/por-1/football-data/P1_9798.csv (já baixado pela coleta)
- cobre: data de 1994/95 em diante
- como baixar: em lote
- amostra: com o Transfermarkt, desmente a data do ogol em 26 jogos (±1-2 dias) e em Leça x Boavista 1997/98 (10/05/1998)
- serve a: coleta-europa; buscar: data quando o ogol diverge

### Jornal de Negócios / arquivo da UEFA (Apito Final)
- endereço: https://www.jornaldenegocios.pt/empresas/desporto/detalhe/justica-desportiva-iliba-pinto-da-costa-no-caso-apito-final ; https://web.archive.org/web/20080512145908/http://www.uefa.com/footballeurope/news/kind%3D2/newsid%3D693942.html
- cobre: punição do Porto em 2008 (-6) e devolução dos 6 pontos pelo Conselho de Justiça da FPF em 2017
- como baixar: página única
- amostra: as duas abriram e confirmam
- serve a: coleta-europa (decisão D1)

### ligaportugal.pt
- endereço: https://www.ligaportugal.pt/
- cobre: site atual (aplicativo Nuxt); não achei página pública de classificação ou jogos de temporadas antigas
- como baixar: não avaliado (não testei a API interna do site)
- amostra: nenhuma
- serve a: ninguém por enquanto

### foradejogo.net
- endereço: https://www.foradejogo.net/match.php?match=199515400013005
- cobre: (é a fonte dos artigos de clube da Wikipédia en: fichas de jogo da liga portuguesa)
- como baixar: não abriu (curl sem resposta, código 000, 22/11/2026)
- amostra: nenhuma
- serve a: ninguém por enquanto; tentar de novo mais tarde

### footballdatabase.eu
- endereço: https://www.footballdatabase.eu/en/competition/overall/<id>-<nome>/<temporada>
- cobre: responde, mas cada temporada tem um id próprio; não achei o da liga portuguesa antiga
- como baixar: não avaliado
- amostra: nenhuma
- serve a: ninguém por enquanto
