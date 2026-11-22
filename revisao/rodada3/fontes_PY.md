# Fontes avaliadas — par-1 (revisor PY, 22/11/2026)

### Wikipédia es — artigo da liga (tabela "Títulos de Liga por año")
- endereço: https://es.wikipedia.org/w/api.php?action=parse&page=Primera_Divisi%C3%B3n_de_Paraguay&prop=wikitext&format=json
- cobre: campeão, vice, 3º, artilheiro (nome e gols) e técnico campeão, 1906-2026 Apertura (inclusive Apertura/Clausura)
- como baixar: em lote (uma página); wikitexto (tabela com `|-`; leitor em revisao/PY/wiki_es_campeoes.py e artilheiros_es.py)
- amostra: campeão bateu 133 de 133 com edicoes.csv; vice bate com a RSSSF (parachamp) em todos os anos em que a RSSSF dá um vice só; artilheiro bateu 82 de 95 (diferenças em PY-019)
- serve a: coleta-sulamerica; buscar: vice e 3º de cada edição (PY-002), artilheiros de 2014-2025 (PY-018)

### Wikipédia es — páginas de temporada ("Torneo Apertura/Clausura AAAA (Paraguay)", "Campeonato Paraguayo de Fútbol AAAA") e anexos de resultados
- endereço: https://es.wikipedia.org/wiki/Torneo_Clausura_2019_(Paraguay) ; https://es.wikipedia.org/wiki/Anexo:Resultados_del_Campeonato_Paraguayo_de_F%C3%BAtbol_2007
- cobre: jogos com placar (de 2017 em diante também data, hora e estádio), tabela final (módulo Football table), artilheiros, promedio e descenso; 1997-2007 com fases; nada antes de 1994 (1962 e 1981 não existem)
- como baixar: jogo a jogo por página de temporada (uma página por torneio); três formatos: "Fecha N" (revisao/PY/wiki_jogos.py), tabela de confrontos com siglas (wiki_cruzada.py) e {{Partidos}}
- amostra: placares iguais 2020 Clausura 66/66, 2022 Apertura 132/132, 2024 Clausura 132/132, 2010 Apertura 119/120, 2010 Clausura 121/121, 2011 Apertura 121/121, 2014 Clausura 121/121, 2017 Apertura 131/132, 2019 Clausura 130/132, 2007 264/264, 2004 178/180, 1998 24/24, 1999 23/24, 1997 16/17; tabelas finais 2017A, 2019C, 2020C, 2022A, 2024C iguais (2019C com 1 gol de diferença em Sol x Gral. Díaz); as diferenças que sobram são erros da própria Wikipédia (a tabela dela bate com o pacote)
- serve a: coleta-sulamerica; buscar: estrutura das fases 1996-2007 (Pre-Sudamericana, finais), rebaixados por ano, artilheiros; terceira opinião de placar 1997-2025

### RSSSF — páginas do ano (para60 … para2025) e parahist/parachamp (fonte da coleta, usada aqui só para conferir a LEITURA)
- endereço: https://www.rsssf.org/tablesp/para62.html ; https://www.rsssf.org/tablesp/parahist.html ; https://www.rsssf.org/tablesp/parachamp.html
- cobre: tudo o que o pacote tem; também os títulos das fases que o leitor não reconhece (Torneo Preparación, Copa Asunción, Pre-Sudamericana, Overall Final), as datas "First Leg [Dec 15]" e as linhas "Relegated on points average"
- como baixar: já está em data/coleta/par-1/rsssf/
- amostra: a leitura de parahist perde clubes em 36 edições (PY-003); 1960-1967 x tabela final da página: só 1960 (1 jogo) e 1967 batem (PY-005)
- serve a: coleta-sulamerica; buscar: linha de início do campeonato (1962-1966), rebaixados (PY-012), datas dos playoffs (PY-009)

### ESPN (par.1) — fonte da coleta, usada como segunda opinião de placar e data
- endereço: data/coleta/par-1/espn/par1_AAAA.json (placar diário da ESPN)
- cobre: 2005-2025 (5.189 jogos)
- como baixar: em lote (já baixado)
- amostra: placar igual em 5.149 de 5.166 jogos casados (11 diferenças são 0-0 de jogo sem dados na ESPN; 6 reais, PY-030); data igual em 5.120, ±1 dia em 31, 2+ dias em 15 (jogos de playoff e 9 jogos do Clausura 2005)
- serve a: coleta-sulamerica; buscar: data dos playoffs de 2005 em diante (PY-009)

### transfermarkt
- endereço: https://www.transfermarkt.com/primera-division-apertura/gesamtspielplan/wettbewerb/PR1A/saison_id/2024
- cobre: Apertura/Clausura só de 2015 em diante (o seletor de temporada começa em 2014/15); ficha de jogo com árbitro, público, autores e cartões
- como baixar: jogo a jogo (ficha) ou por temporada (calendário); HTML
- amostra: não conferida jogo a jogo (só a cobertura); uma página baixada (data/cache/revisao/PY/tm-PR1A-2010.html, que devolveu 2026)
- serve a: coleta-sulamerica; buscar: árbitro e público de 2015 em diante (buraco da seção 4)

### apf.org.py
- endereço: https://www.apf.org.py/
- cobre: site da federação; a página inicial não traz histórico de campeões nem tabelas antigas
- como baixar: —
- amostra: 0 (nada útil achado na página inicial)
- serve a: —; buscar: palmarés oficial (não achado)

### ogol
- endereço: https://www.ogol.com.br/edicao/liga-paraguaia-1998/
- cobre: segundo a coleta, só 2005 em diante (calendário vazio antes); respondeu 200 em 22/11
- como baixar: por edição (calendário); HTML
- amostra: não conferido (a coleta já testou e descartou)
- serve a: coleta-sulamerica; buscar: nada novo antes de 2005

### Fontes independentes para 1906-1995 (jogos)
- nenhuma achada: a Wikipédia es não tem páginas de 1960-1967 e 1981 (ou tem só a tabela), o transfermarkt começa em 2015, o ogol em 2005, footballdatabase.eu sem cota em 22/11. Os placares de 1960-1967 e 1981 só puderam ser conferidos contra as tabelas da própria RSSSF.
