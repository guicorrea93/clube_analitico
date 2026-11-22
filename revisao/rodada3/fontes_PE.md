# Fontes avaliadas — per-1 (revisor PE, 22/11/2026)

### Wikipédia es — páginas de temporada (Campeonato Peruano de Fútbol de <ano>, Campeonato Descentralizado <ano>, Liga 1 <ano> (Perú))
- endereço: https://es.wikipedia.org/w/api.php?action=parse&page=Campeonato_Descentralizado_2000&prop=wikitext&format=json&redirects=1 (títulos tirados dos links do Palmarés de "Primera División del Perú")
- cobre: 1912-2025, todas as edições; resultados (matriz match_X_Y e {{Partidos}} com data, estádio, árbitro e autores) de 1930-2008 quase completos; tabelas por fase e tabela acumulada (com ajustar_puntos/adjust_points e a nota da resolução da FPF); seção "Ascensos y descensos" (rebaixados do ano anterior); tabelas de 1912-1921
- como baixar: em lote (110 páginas, 1 pedido por página pela API); wikitexto (módulo sports table, em inglês até ~2008 e em espanhol — ganados_/empates_/ajustar_puntos_ — de 2022 em diante)
- amostra: 8.747 resultados casados com o pacote (1930-2008, anos em que a coleta NÃO usou a es) -> 7.736 iguais; o resto são liguillas pré-Libertadores/promoção que o pacote deixa de fora e anos incompletos (1984, 1986, 1991); ~12 divergências reais (PE-017). Rebaixados: confirmou os erros PE-003/PE-004/PE-006. Tabela acumulada: confirmou PE-008.
- serve a: coleta-sulamerica; buscar: rebaixados por ano (Ascensos y descensos), tabela acumulada de 1998, 2000, 2001, 2004, 2005, 2009, 2012, descontos de pontos com a resolução, final nacional de 1990 (data), datas de finais ({{Partidos|fecha=}}).

### Wikipédia es — "Primera División del Perú" (Palmarés e Goleadores por año)
- endereço: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_del_Per%C3%BA
- cobre: campeão e vice de 1912-2025 (109 edições, conta a Liga Peruana 1912-1921 como a FPF/ADFP: Universitario 29, Alianza 25, Cristal 20); artilheiro de 1928-2025
- como baixar: 1 página (API)
- amostra: campeões 109/109; vices 107/109 (1918 e 1921 = PE-001); artilheiros 87/97 iguais (PE-015, PE-016)
- serve a: coleta-sulamerica; buscar: vice 1918/1921, artilheiro 1996.

### Wikipédia en — páginas de temporada ("<ano> Peruvian Primera División")
- endereço: https://en.wikipedia.org/w/api.php?action=parse&page=1955_Peruvian_Primera_Divisi%C3%B3n&prop=wikitext&format=json&redirects=1
- cobre: 1926-1965 com matriz de resultados (anos em que a coleta usou a es)
- como baixar: em lote (1 página por ano)
- amostra: 2.291 resultados casados -> 2.172 iguais; as diferenças são de outros torneios na mesma página (1943, 1948 3º turno, 1950). Provavelmente copia a es: serve como segunda opinião fraca.
- serve a: coleta-sulamerica; buscar: pouco (confirmação dos anos 1943-1965).

### RSSSF — peru1912.html ... peru1921.html (Liga Peruana)
- endereço: https://www.rsssf.org/tablesp/peru1913.html
- cobre: classificação completa de 1912-1917 (1912 com pontos), campeão, vice e participantes de 1918-1921, subidas e descidas
- como baixar: já está em data/coleta/per-1/rsssf/ (a coleta baixou e não usou)
- amostra: confirma o vice de 1918/1921 = Jorge Chávez No. 2 (PE-001); diverge da es/en no vice de 1914 (PE-026)
- serve a: coleta-sulamerica; buscar: classificação de 1912-1921 (PE-019).

### transfermarkt — Liga 1 Apertura / Clausura (TDeA / TDeC)
- endereço: https://www.transfermarkt.com/liga-1-apertura/gesamtspielplan/wettbewerb/TDeA/saison_id/2013 (Clausura: TDeC); temporadas 2006, 2014, 2015, 2017-2026 (o filtro da página só lista essas)
- cobre: calendário com data, hora e placar; a ficha de cada jogo tem árbitro, público, autores e cartões
- como baixar: em lote por torneio (1 página por Apertura/Clausura) e jogo a jogo para a ficha
- amostra: 4 de 4 placares em que ESPN e pacote divergiam -> transfermarkt = pacote (PE-028)
- serve a: coleta-sulamerica; buscar: árbitro e público (2014 em diante, campos vazios no pacote), terceira fonte de placar.

### ESPN (per.1) — já usada pela coleta, aqui como conferência de datas
- endereço: data/coleta/per-1/espn/per1_<ano>.json (placar diário da ESPN)
- cobre: 2005-2025, data e hora UTC
- como baixar: já baixado
- amostra: 6.418 jogos casados; 87 com data diferente, 30 por mais de 1 dia, quase todos finais/semifinais com a data herdada (PE-009); 54 placares diferentes, a maioria 0-0 de enchimento da ESPN
- serve a: coleta-sulamerica; buscar: data local (UTC-5) dos jogos de mata-mata.

### liga1.pe
- endereço: https://liga1.pe/ , https://liga1.pe/disciplinario/
- cobre: só a temporada atual (2026): tabela, fixture e resoluções disciplinares (PDF)
- como baixar: página a página
- amostra: sem histórico; não serve para 1912-2025
- serve a: coleta-sulamerica; buscar: só a temporada 2026 quando for coletada.

### dechalaca.com e ogol.com.br
- endereço: https://dechalaca.com/ ; https://www.ogol.com.br/edicao/liga-1-2023/178478
- cobre: respondem (200) em 22/11; não testei conteúdo por amostra (a coleta diz que o ogol não tem jogos peruanos)
- como baixar: —
- amostra: não feita
- serve a: coleta-sulamerica; buscar: terceira fonte para PE-016/PE-017 (dechalaca tem crônicas históricas).

### footballdatabase.eu
- não testado (limite diário de 50 páginas já esgotado em 22/11, aviso do briefing).
