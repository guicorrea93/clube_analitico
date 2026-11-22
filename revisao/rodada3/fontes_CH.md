# Fontes avaliadas — Campeonato Chileno (chi-1), revisão de 22/11/2026

### transfermarkt (com)
- endereço: https://www.transfermarkt.com/primera-division-de-chile/gesamtspielplan/wettbewerb/CLPD/saison_id/1992 (saison_id = ano - 1; rótulo "1993")
- cobre: todos os jogos (data, rodada, placar, link da ficha) de 1990-1996, 1998-2001 e 2018-2025 na competição CLPD; Apertura/Clausura 2002-2017 não aparecem nesse seletor. A ficha de cada jogo tem árbitro, público, autores e cartões.
- como baixar: em lote (uma página por temporada, ~600 KB HTML); fichas jogo a jogo
- amostra: 4.724 jogos de 19 temporadas, 4.713 casados com o pacote; 24 placares diferentes. Nos anos-base do ogol (1990-1995) confirmou erros do ogol que a tabela da RSSSF já apontava (9 jogos); nos anos-base da RSSSF/ESPN errou ele (ex.: 2021 La Serena 2-2 Huachipato, ESPN confirma 2-2). Também inverte mandante em alguns jogos de 1995.
- serve a: coleta-sulamerica; buscar: 3ª fonte para os placares de 1990-1995 (base ogol), datas de 2020, árbitro/público/autores de 1990-2001 (fichas)

### Wikipédia em espanhol — páginas de temporada
- endereço: https://es.wikipedia.org/w/api.php?action=parse&page=Primera_División_de_Chile_1993&prop=wikitext&format=json ; torneios: "Torneo Apertura 2005 (Chile)", "Torneo Clausura 2014 (Chile)", "Torneo Transición 2013 (Chile)", "Liga de Primera 2025"
- cobre: tabela final de todas as temporadas (1933-1961 muitas citam a própria RSSSF: não é independente), goleadores (1963 em diante), liguillas de promoção/descenso e, de ~1992 em diante, todos os jogos por rodada com data e estádio
- como baixar: em lote (uma página por temporada, API); hoje a API deu muitos 429 (IP dividido): ~110 páginas levaram mais de 1 hora
- amostra: campeões 109/109 iguais; vices 102/109 (os 7 diferentes conferem com a RSSSF: erros do pacote); jogos 2.708 casados (1992-1995, 2005-2009) com 4 placares diferentes (2 erros do pacote, 2 da Wikipédia) e as datas dos mata-matas certas
- serve a: coleta-sulamerica; buscar: vice/3º, rebaixados de cada ano (tabelas "Descendidos"), datas dos mata-matas 2002-2012, artilheiros 2011-2025

### Wikipédia em espanhol — "Primera División de Chile" (Historial)
- endereço: https://es.wikipedia.org/wiki/Primera_División_de_Chile (seção Historial)
- cobre: campeão e vice de todos os 110 torneios (1933-2026)
- como baixar: em lote (uma página)
- amostra: campeões 109 de 109 iguais; vices 102 de 109
- serve a: coleta-sulamerica; buscar: segunda fonte de campeão/vice (hoje a coleta usa a en.wiki)

### RSSSF chilehist.html (tabelas finais 1933-1996)
- endereço: https://www.rsssf.org/tablesc/chilehist.html
- cobre: tabela final de cada ano com pontos de bônus anotados "(1)/(2)", campeão, classificados, RELEGATED e PROMOTED de 1933 a 1996
- como baixar: em lote (já baixada em data/coleta/chi-1/rsssf/)
- amostra: rebaixados x participação no ano seguinte: bateu em todos os anos testados (1958-1996)
- serve a: coleta-sulamerica; buscar: rebaixados oficiais (linhas RELEGATED), bônus da Polla Gol (1979-1990), ordem oficial das tabelas

### ESPN (liga chi.1) como 3ª fonte de datas
- endereço: data/coleta/chi-1/espn/chi1_<ano>.json (já baixada)
- cobre: 2001-2025, data/hora UTC, placar, estádio, lances
- como baixar: em lote (já no disco)
- amostra: datas dos mata-matas 2005-2008: ESPN = es.wiki em todos os ~15 jogos que as duas têm; o pacote erra
- serve a: coleta-sulamerica; buscar: datas de ida e volta dos mata-matas; repetir o casamento de 2020 depois de corrigir as datas

### ogol (calendário completo)
- endereço: https://www.ogol.com.br/edicao/liga-chilena-1977/37074/calendario?page=4
- cobre: datas de jogos dos anos 1930-1983 que a RSSSF não data; a coleta baixou só até a 3ª página em 1964, 1971, 1977 e 1982, e nada em 1951-1957
- como baixar: em lote (50 jogos por página)
- amostra: 1977 p1-p3 = 150 jogos com data; faltam as páginas 4-7
- serve a: coleta-sulamerica; buscar: datas de 1964, 1971, 1977, 1982 (e conferir se 1951-1957 existem com outro id de edição)

### solofutbol.cl (citada pela es.wiki)
- endereço: http://www.solofutbol.cl/futbol%20chileno/Campeonatos%20Nacionales/...
- cobre: (segundo a es.wiki) tabelas e jogos chilenos
- como baixar: não respondeu em 22/11 (conexão recusada)
- amostra: nenhuma
- serve a: —; buscar: —

### anfp.cl
- endereço: https://www.anfp.cl/
- cobre: só a temporada atual (responde 200, sem histórico em lote)
- como baixar: —
- amostra: não usada
- serve a: —
