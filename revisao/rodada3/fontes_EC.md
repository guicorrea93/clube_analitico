# Fontes avaliadas — Campeonato Equatoriano (ecu-1), revisão de 22/11/2026

A coleta usou: RSSSF (base de todos os anos), ESPN `ecu.1` (2005 em diante) e Wikipédia em inglês (campeão e vice).

### Wikipédia es — página da liga ("Serie A de Ecuador")
- endereço: https://es.wikipedia.org/wiki/Serie_A_de_Ecuador (wikitexto: https://es.wikipedia.org/w/index.php?title=Serie_A_de_Ecuador&action=raw)
- cobre: campeão, vice, 3º e 4º de 1957 a 2025 (Historial); rebaixados e promovidos ano a ano (Ascensos y descensos); artilheiro por temporada; estreia e nº de temporadas dos clubes atuais
- como baixar: em lote; wikitexto (uma página)
- amostra: campeão e vice 68/68 iguais ao pacote; 3º/4º 221 de 272 posições iguais (as 51 diferentes são erros do pacote, EC-001 a EC-003); artilheiros 65/68; rebaixados: faltam 90 no pacote, em 34 edições (EC-004), e 2025 tem 3 a mais (EC-005)
- serve a: coleta-sulamerica; buscar: lista de rebaixados (REBAIXADOS), 3º/4º oficiais, artilheiros de 1988, 1996 e 1999

### Wikipédia es — páginas de temporada ("Campeonato Ecuatoriano de Fútbol <ano>", "Serie A de Ecuador <ano>")
- endereço: https://es.wikipedia.org/wiki/Campeonato_Ecuatoriano_de_F%C3%BAtbol_1982 (modelo)
- cobre: tabelas por fase com bônus e punições (todas); resultados com data e estádio só em 1957, 1960, 1982 e 2008-2025 (1961-1981 e 1983-2007 têm a grade de resultados vazia); finais com data, público e árbitro (2009+); notas de punição e rebaixamento administrativo
- como baixar: em lote (uma página por ano, 72 páginas); wikitexto
- amostra: placar igual em 3.030 jogos de 1957-2025 (1950s 7, 1960s 30, 1970s 9, 1980s 231, 1990s 11, 2000s 449, 2010s 1.072, 2020s 1.221); 28 diferentes, quase todos contrariados pelas tabelas da RSSSF (o pacote fecha com elas); datas iguais na maioria (diferenças de 1-3 dias e lixo do leitor)
- serve a: coleta-sulamerica; buscar: datas de 1960 (27 jogos que o pacote tem sem data), punições de 2015-2025 com motivo, 2025 (El Nacional -9, W.O. contra o Delfín, só Vinotinto cai no Grupo Descenso)

### Wikipédia es — páginas de clube
- endereço: https://es.wikipedia.org/wiki/Liga_Deportiva_Universitaria_de_Quito (modelo)
- cobre: recordes do clube com data (ex.: 11-0 no América de Ambato em 26/10/1969)
- como baixar: jogo a jogo (uma página por clube); wikitexto
- amostra: 1 de 1 (a goleada recorde do painel confere)
- serve a: coleta-sulamerica; buscar: datas de jogos-recorde que o pacote tem sem data

### RSSSF (páginas por ano e listas)
- endereço: https://www.rsssf.org/tablese/ecua2014.html (modelo)
- cobre: base da coleta (jogos de todos os anos); as próprias páginas trazem o que o pacote deixou passar: datas no título dos blocos de mata-mata ("First Leg [Dec 17]"), notas de rebaixamento, jogos perdidos por jogador irregular (1965), autores que contradizem o placar (2005 Apertura)
- como baixar: em lote; já está em data/coleta/ecu-1/rsssf/
- amostra: 42 datas de mata-mata lidas do título do bloco, 41 diferentes do pacote (EC-009)
- serve a: coleta-sulamerica; buscar: o que já está baixado (não precisa baixar de novo)

### ESPN (placar diário `ecu.1`)
- endereço: https://site.api.espn.com/apis/site/v2/sports/soccer/ecu.1/scoreboard?dates=AAAAMMDD (usada pela coleta)
- cobre: 2005 em diante: data e hora, estádio, público, gols com minuto e cartões (quase sem lances de 2014 a 2020)
- como baixar: em lote (já baixado em data/coleta/ecu-1/espn/)
- amostra: 5.145 jogos casados; data diferente em 78 (36 por causa das finais com data herdada, EC-009); placar diferente em 15 (a RSSSF fica, e a Wikipédia es confirma em 2008)
- serve a: coleta-sulamerica; buscar: recasar as finais depois de corrigir as datas (hora, estádio, lances dos 2ºs jogos)

### ogol.com.br
- endereço: https://www.ogol.com.br/competicao/liga-equatoriana/274 (lista das edições 1957-2026); https://www.ogol.com.br/edicao/liga-equador-1975/36418/calendario
- cobre: lista de edições; calendário VAZIO nos anos testados (1969, 1975, 1985, 2003: 0 jogos); a página de uma edição às vezes devolve outra competição (1999 -> "Liga Uruguaia 1920/21")
- como baixar: jogo a jogo / por edição; HTML
- amostra: 0 jogos em 4 edições antigas
- serve a: banco-painel; buscar: só escudos de clube (página /equipe/<nome>/<id>, ex.: https://www.ogol.com.br/equipe/aucas/2368)

### Transfermarkt (LigaPro Serie A, EC1N)
- endereço: https://www.transfermarkt.com/liga-pro-serie-a/gesamtspielplan/wettbewerb/EC1N/saison_id/2018
- cobre: o seletor só oferece as temporadas 2019, 2025 e 2026; pedir outro ano devolve a atual
- como baixar: jogo a jogo (ficha do jogo); HTML
- amostra: 0 (não serve para anos antigos)
- serve a: coleta-sulamerica; buscar: no máximo árbitro/público de 2019 e 2025, jogo a jogo (custo alto)

### Soccerway
- endereço: https://es.soccerway.com/matches/2014/12/18/ecuador/primera-a/... (links citados pela Wikipédia es)
- cobre: o endereço antigo devolve a página inicial (site novo); não deu para ler ficha de jogo
- como baixar: —
- amostra: 0 de 1
- serve a: nenhum (descartada)

### ligapro.ec
- endereço: https://ligapro.ec/
- cobre: só notícias e jogos da temporada atual (2026); sem histórico
- como baixar: —
- amostra: página inicial lida; sem tabelas antigas
- serve a: nenhum para o histórico (só confirmar a temporada corrente)

### footballdatabase.eu
- endereço: https://www.footballdatabase.eu/
- cobre: não testada (limite diário do IP esgotado em 22/11, aviso do briefing)
- como baixar: —
- amostra: —
- serve a: testar outro dia como 3ª opinião de placares e datas de 1960-1999 (único buraco sem fonte independente)
