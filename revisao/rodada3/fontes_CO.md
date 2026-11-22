# Fontes avaliadas — Campeonato Colombiano (col-1), revisão CO, 22/11/2026

### RSSSF — lista de campeões e vices (colchamp)
- endereço: https://www.rsssf.org/tablesc/colchamp.html
- cobre: campeão E vice de 1948 a 2026 Ap (a coleta só leu o campeão)
- como baixar: em lote; uma página de texto (já está em data/coleta/col-1/rsssf/colchamp.html)
- amostra: vice bate com a Wikipédia es em 101 de 101 edições
- serve a: coleta-sulamerica; buscar: coluna "Runners Up" (CO-001)

### RSSSF — páginas por temporada, partes que a coleta não usou
- endereço: https://www.rsssf.org/tablesc/col48.html, col49.html, col60.html (Cross-Table); col74.html a col79.html (jogos das fases finais); col95.html ("Final Table Primera A"); col2024.html ("Relegation", "First Leg [Dec 18]")
- cobre: tabela de confrontos 1948, 1949 e 1960 (todos os jogos, sem data); jogos das fases finais 1974-1979; tabelas finais dos anos sem jogos (1987, 1991-1995); seções de rebaixamento por promédio (2000s em diante); datas das finais
- como baixar: em lote; texto (já baixadas em data/coleta/col-1/rsssf/)
- amostra: 1948 88 de 90 jogos batem com o pacote; 1949 177 de 182; 1960 109 de 220 (o resto falta no pacote); fases finais 1974-79: 172 de 185
- serve a: coleta-sulamerica; buscar: jogos de 1960 (2ª metade), fases finais de 1976/1988, tabelas de 1987/1991-1995, datas "First/Second Leg [..]", rebaixados

### Wikipédia es — Categoría Primera A (Títulos por temporada; Otros datos)
- endereço: https://es.wikipedia.org/wiki/Categor%C3%ADa_Primera_A
- cobre: campeão, subcampeão, resultado da final, técnico, máximo goleador e gols, nº de clubes (1948-2026); recordes (maiores goleadas)
- como baixar: em lote; wikitexto pela API (1 página)
- amostra: campeão 101/101 e vice 101/101 iguais à RSSSF colchamp; artilheiro (nome e gols) bate com o pacote em 73 de 100 edições (diferenças em CO-017); 3 recordes do painel batem
- serve a: coleta-sulamerica; buscar: artilheiros de 2008 em diante (a coltops da RSSSF acaba em 2007), nº de clubes

### Wikipédia es — Anexo:Ascensos y descensos de la Categoría Primera A
- endereço: https://es.wikipedia.org/wiki/Anexo:Ascensos_y_descensos_de_la_Categor%C3%ADa_Primera_A
- cobre: rebaixados e promovidos de 1991 a 2026; séries de promoção 2006-2014
- como baixar: em lote; wikitexto (1 página)
- amostra: 46 rebaixamentos 1992-2025; o do 2021 Ap (Boyacá Chicó) bate com o único marcado no pacote; 1995 (Cúcuta) e 2024 (Patriotas, Jaguares) batem com a RSSSF
- serve a: coleta-sulamerica; buscar: dicionário de rebaixados por temporada (CO-007)

### Wikipédia es — páginas de temporada/torneio (1995 em diante)
- endereço: https://es.wikipedia.org/wiki/Torneo_Apertura_2005_(Colombia) (modelo "Torneo Apertura|Finalización AAAA (Colombia)"; "Campeonato colombiano AAAA" até 2001)
- cobre: todos os jogos com data e placar (2005 em diante); finais com data, estádio e reporte; até 2001 a página quase só traz as finais
- como baixar: em lote; wikitexto por torneio (o leitor da coleta, wikipedia_jogos.py, lê direto)
- amostra: 2005 Ap 171/188, 2009 Fi 128/188 (diferenças de 1-2 dias em que a ESPN dá razão ao pacote), 2016 Ap 210/213, 2022 Fi 224/226 — as diferenças restantes são as datas das finais (pacote errado, CO-008)
- serve a: coleta-sulamerica; buscar: datas das finais e semifinais; 3ª opinião de placares

### ESPN (placar diário col.1) — uso novo: conferência de data e placar
- endereço: data/coleta/col-1/espn/col1_AAAA.json (já baixado pela coleta)
- cobre: 2005-2025, data e hora, público, lances; 2013 Fi tem muitos placares 0-0 de preenchimento
- como baixar: em lote (já em disco)
- amostra: 7.968 jogos casados; data igual em 97%; 104 jogos com data diferente > 1 dia (quase todos finais/semis com data herdada no pacote)
- serve a: coleta-sulamerica; buscar: data dos mata-matas; ligação errada da final de 2025 Fi (CO-009)

### transfermarkt
- endereço: https://www.transfermarkt.com/liga-dimayor-apertura/gesamtspielplan/wettbewerb/COLP/saison_id/2009 (saison_id = ano − 1: 2009 → Apertura 2010)
- cobre: calendário com data, hora e placar; link para a ficha de cada jogo (árbitro, público, autores, cartões); temporadas antigas (1985) redirecionam para a atual
- como baixar: em lote o calendário (1 página por torneio); ficha jogo a jogo
- amostra: 2010 Ap rodada 1 (9 jogos) igual ao pacote em placar
- serve a: coleta-sulamerica; buscar: árbitro e público 2000s em diante; 3ª opinião para os placares de CO-015

### golgolgol.net (citado pela Wikipédia es para recordes)
- endereço: https://web.archive.org/web/20130531141619/http://colombia.golgolgol.net/liga-postobon/calendario-y-resultados/partidos/sam-uni_106-29213.html
- cobre: em tese, ficha de jogos desde 1948
- como baixar: só pelo arquivo da web; a página arquivada veio vazia (8 KB, sem a ficha)
- amostra: 0 de 1
- serve a: nenhuma (não recomendado)

### 11v11
- endereço: https://www.11v11.com/competitions/colombian-primera-a/1985/
- cobre: nada (404 para a liga colombiana)
- como baixar: —
- amostra: 0 de 1
- serve a: nenhuma
