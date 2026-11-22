# Fontes avaliadas — ita-1 (revisão, 22/11/2026)

### Wikipédia it — página de cada temporada (Serie A AAAA-AAAA)
- endereço: https://it.wikipedia.org/w/index.php?title=Serie_A_1952-1953&action=raw (1945/46: Divisione_Nazionale_1945-1946)
- cobre: 1929/30 a 2025/26. Classificação final (com punição em `<small>(-x)</small>`, cor de rebaixado e notas de readmissão, declassamento e spareggi), matriz (Tabellone, com "a tavolino"), Calendario com data de cada jogo (adiados com a data própria), artilharia ("Classifica marcatori") e seção Spareggi
- como baixar: em lote, 95 páginas (action=raw, wikitexto); leitor em revisao/IT/itwiki.py
- amostra: classificação 1.703 linhas (números iguais em 1.692; as 11 diferenças: 5 são erros do pacote, IT-003 a IT-007); placares 28.896 de 28.896 jogos de pontos corridos (33 diferenças: 7 erros do pacote, o resto erro da matriz da Wiki it); datas 28.248 jogos (26.830 iguais, 452 com 1 dia, 988 com mais; 622 erros do pacote confirmados pela RSSSF); artilheiro 93 de 95
- serve a: coleta-europa; buscar: datas (Calendario), jogos "a tavolino", declassamentos, readmissões, spareggi, ordem pela classifica avulsa. Atenção: a matriz tem erros de célula e de coluna (1967/68 SPAL/Sampdoria trocadas); a data de julho de 2020 (covid) precisa do ano certo

### Wikipédia it — páginas de temporada dos clubes (ex.: Associazione Calcio Torino 1952-1953)
- endereço: https://it.wikipedia.org/w/index.php?title=Associazione_Calcio_Torino_1952-1953&action=raw
- cobre: fichas de jogo ({{Incontro di club}}) com data, estádio, público, árbitro e autores dos gols, para muitos clubes e temporadas antigas
- como baixar: jogo a jogo dentro da página do clube (uma página por clube e temporada; o título varia com o nome do clube na época)
- amostra: 3 de 3 casos decididos (Torino x Palermo 1952/53, Napoli x Palermo 1962/63, Bari x Genoa 1963/64)
- serve a: coleta-europa; buscar: desempate de placar duvidoso; autores dos gols, público e árbitro antes de 2001/02 (buraco da seção 4 da ficha), clube a clube

### RSSSF — páginas por temporada (já baixadas pela coleta: data/coleta/ita-1/rsssf/)
- endereço: https://www.rsssf.org/tablesi/ital53.html
- cobre: 1929/30 a 2009/10 com rodada a rodada: data de cada giornata, notas "* played dd mmm aaaa", placar, autores dos gols com minuto, "a tavolino" com o motivo, classificação após cada rodada e artilharia
- como baixar: em lote (já em cache); leitor de datas em revisao/IT/rsssf_datas.py
- amostra: datas — terceira opinião em 862 jogos divergentes (622 a favor da Wiki it, 163 a favor do pacote); tavolino 20 de 20 com o motivo; placares: erra em 2 (omite um gol do Palermo em 1952/53 e 1962/63)
- serve a: coleta-europa; buscar: datas (o importador só usa a tabela da RSSSF hoje), motivo dos jogos de tribunal, e autores dos gols antes de 2001/02 (ficha, seção 8: "MARCATORI" rodada a rodada), em lote

### transfermarkt (com)
- endereço: https://www.transfermarkt.com/serie-a/gesamtspielplan/wettbewerb/IT1/saison_id/1952
- cobre: calendário com placar e data de todas as temporadas da Serie A (testado 1952/53 e 1962/63)
- como baixar: em lote, uma página por temporada (~700 KB, HTML)
- amostra: 2 de 2 placares disputados batem com a Wiki it (3-1); as datas antigas são da rodada
- serve a: coleta-europa; buscar: terceira opinião de placar. Cuidado: o histórico antigo pode ter sido copiado da Wikipédia

### Wikipédia it — Albo d'oro del campionato italiano di calcio
- endereço: https://it.wikipedia.org/w/index.php?title=Albo_d%27oro_del_campionato_italiano_di_calcio&action=raw
- cobre: campeões de 1898 a 2025/26, com títulos revogados (1927, 2005) e não atribuídos; contagem oficial (Juventus 36, Inter 21, Milan 19)
- como baixar: em lote (uma página)
- amostra: 95 de 95 campeões desde 1929/30 batem com o pacote
- serve a: coleta-europa; buscar: campeões de 1898-1929, se o Guilherme quiser incluir (D-IT-01)

### 11v11, footballdatabase.eu, soccerway, legaseriea.it
- endereço: https://www.11v11.com/competitions/serie-a/1953/ ; https://www.footballdatabase.eu/ ; https://www.soccerway.com/national/italy/serie-a/ ; https://www.legaseriea.it/it/serie-a/albo-d-oro
- cobre: 11v11 responde com página curta (6 KB) para a Serie A, sem jogos; footballdatabase e soccerway respondem (200), não testados a fundo; legaseriea redireciona (307)
- como baixar: não avaliado
- amostra: nenhuma
- serve a: — ; buscar: nada por ora (as fontes acima bastam)
