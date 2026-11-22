# Fontes novas: Séries A e B (revisor QA, 22/11/2026)

Testadas por amostra contra o banco (`db/futebol.db`, só leitura) com os scripts de `revisao/QA/` (`cmp_tm.py`, `cmp_bna.py`, `cdf.py`, `datas_3fontes.py`, `amostra_fichas.py`). Páginas em `data/cache/revisao/QA/`. Nenhuma delas foi usada pela coleta das Séries A e B (a coleta usou RSSSF, RSSSF Brasil, ESPN, ogol só como calendário e Wikipédia en; o Transfermarkt só para eventos da Série A 2003-2006).

### Transfermarkt: página de jogos da temporada (gesamtspielplan)
- endereço: https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/1994 (Série B: .../campeonato-brasileiro-serie-b/.../BRA2/saison_id/2008). O `saison_id` é o ano anterior ao da edição (1994 = Série A 1995).
- cobre: placar, data, rodada e id da ficha de cada jogo. Série A de 1985 em diante (1985 só com 184 jogos; 1986 sem os grupos E a H); Série B de 2005 em diante (2003-2004 vêm com datas e clubes errados: não usar).
- como baixar: em lote, 1 página por temporada (HTML); ~40 páginas para A e B inteiras.
- amostra (placar / data, jogos casados): A 1980s 1.114 jogos (1985, 1986, 1988, 1989): placar 1.017 (os 96 de 1988 trazem os pênaltis somados ao placar; 1 erro de pênalti na final de 1986) e data 1.040; A 1990s 2.498 (1990-1999): placar 2.493, data 2.138 (as diferenças são em grande parte erros do banco, confirmados pela Bola na Área); A 2000s 1.558 (2000, 2001, 2005, 2008): placar 1.556 (os 2 restantes são erro do banco: QA-001), data 1.554; A 2010s 380 (2015): 380 e 380; A 2020s 380 (2022): 380 e 363. B 2000s 611 (2005, 2009): 611 e 447; B 2010s 342 (2015): 342 e 342; B 2020s 380 (2022): 376 e 324.
- riscos achados: datas de jogos à noite às vezes 1 dia antes (Série A 2022 17 jogos, Série B 2005 e 2022); mando trocado em alguns mata-matas (quartas de 1988 e 1994) e na final CBF de 1987; 4 placares errados na Série B 2022; "Botafogo FC" é o de Ribeirão Preto e "America FC" muda de clube conforme o ano. Usar sempre com uma segunda fonte.
- serve a: banco-painel; buscar: datas da Série A 1985-1999 (jogos sem data de 1995-1996 e datas impossíveis de 1991, 1997, 1999) e da Série B 2005-2025; terceira opinião em placar.

### Transfermarkt: ficha de jogo (spielbericht)
- endereço: https://www.transfermarkt.com.br/spielbericht/index/spielbericht/4831609
- cobre: autores dos gols com minuto, cartões, estádio, público e árbitro, escalação e técnico. Amostra de 30 fichas: autores completos em todos os anos testados da Série A (1985, 1991, 1997, 2001, 2005, 2015, 2022: 37 de 38 gols com autor); público e árbitro só em parte das fichas antigas (1991 sim; 1985, 1997, 2001 e 2005 não) e em todas de 2015 e 2022; Série B 2009, 2015 e 2022: autores, árbitro e público em 8 de 9.
- como baixar: jogo a jogo (1 página por jogo; o id vem da página da temporada). Custo: autores da Série A 1985-2002, cerca de 5.600 páginas (~3 h a 1 pedido a cada 2 s); árbitro da Série A 2010-2025, ~6.000 páginas; árbitro da Série B 2009-2025, ~6.500 páginas.
- amostra: 30 fichas (revisao/QA/saida/fichas.csv); gols com autor batem com o placar em 29 de 30.
- serve a: banco-painel; buscar: autores dos gols da Série A 1985-2002 (o banco não tem nenhum antes de 2003), árbitro das Séries A e B (o banco não tem nenhum), público da Série A recente (o banco não tem nenhum).

### Bola na Área (bolanaarea.com)
- endereço: https://www.bolanaarea.com/brasileirao_1975.htm (Série A, 1971-2024), https://www.bolanaarea.com/serie_b_1985.htm (Série B, 1971-2024, inclusive 1986, 1987 e 2000), https://www.bolanaarea.com/taca_brasil_1959_tab.htm (Taça Brasil 1959-1960); cada edição tem subpáginas de jogos (fase1, fase2, fasefinal, turno1, turno2, tabela).
- cobre: data, placar e rodada de todos os jogos; em parte dos jogos, local, público e autores com minuto (Série B 1985: 43 de 48 com público e 38 com autores; Série A 2008: 250 de 376 com público; Série B 2015: 366 de 380 com público; Série A 1959: 34 de 35 com autores); tabela final e "principais artilheiros" de cada edição.
- como baixar: em lote, 2 a 4 páginas por edição (HTML; o texto precisa de leitor próprio, ver `revisao/QA/bna.py`). Cerca de 250 páginas para as duas séries inteiras.
- amostra (placar / data, jogos casados): A 1950s 35 (1959): 28 / 27, as diferenças confirmadas pela Wikipédia pt (QA-002); A 1960s 16 (1960): 16 / 16; A 1970s 1.620 (1971, 1974, 1975, 1979): 1.603 / 1.570; A 1980s 1.396 (1980, 1984, 1985, 1987, 1989): 1.370 / 1.350; A 1990s 1.538 (1990, 1991, 1993, 1994, 1997, 1999): 1.524 / 1.294 (1997 puxa a data para baixo); A 2000s 1.224 (2001, 2005, 2008): 1.202 / 1.192 (2005 tem os 11 jogos anulados da Máfia do Apito); A 2010s 379 (2015): 379 / 379; A 2020s 379 (2022): 379 / 369. B 1970s 205 (1971, 1972): 200 / 200; B 1980s 1.383 (1980-1985, 1988, 1989): 1.364 / 1.320; B 1990s 1.861 (1990-1992, 1994-1999): 1.820 / 1.252 (o banco não tem data em 301 jogos de 1991 e erra muitas em 1990, 1991 e 1998); B 2000s 647 (2005, 2009): 646 / 593; B 2010s 380 (2015): 380 / 372; B 2020s 378 (2022): 376 / 366. As diferenças de placar foram conferidas uma a uma: quase todas são ida e volta casadas trocadas ou erro da própria BNA (ela erra sozinha em ~10 placares da Série B, por isso só vale com outra fonte); onde BNA e outra fonte concordam contra o banco, viraram achado (QA-001, QA-002, QA-006, QA-007, QA-009, QA-010).
- riscos: datas da Série A 1996 e 1997 muitas vezes são as da rodada (diverge do Transfermarkt e do banco em ~130 jogos cada ano); 1989 da Série B não tem datas por jogo; a tabela final às vezes não acompanha a lista de jogos (1984).
- serve a: banco-painel; buscar: datas da Série B 1971-1999 (com a Wikipédia pt) e da Série A 1971-1999 (com o Transfermarkt); público e autores onde houver (Série B 1985, Série A 2008); artilheiros que faltam na Série B (1971, 1988-1990).

### ogol: ficha de jogo
- endereço: https://www.ogol.com.br/jogo/1977-11-20-uberaba-atletico-mineiro/632153 (os endereços já estão nos JSON da coleta: data/serie_a/ogol/ e data/serie_b/ogol/)
- cobre: escalações quase sempre; autores com minuto, árbitro e estádio só em parte (Série A 1977: 3 de 3 com árbitro e estádio, autores em 13 de 18 gols; Série A 1980 e 1993: sem árbitro, autores em ~1/3; Série B 1981, 1992 e 2002: quase nada além da escalação). Público: não achado em nenhuma das 18 fichas.
- como baixar: jogo a jogo (HTML). A coleta usou só o calendário do ogol, não as fichas.
- amostra: 18 fichas (revisao/QA/saida/fichas.csv); placar sempre igual ao banco.
- serve a: banco-painel; buscar: autores e árbitro da Série A anos 1970 (complemento ao Transfermarkt, que só começa em 1985). Baixa prioridade para a Série B.

### Campeões do Futebol (campeoesdofutebol.com.br)
- endereço: https://www.campeoesdofutebol.com.br/torneio_robertao_1967.html, https://www.campeoesdofutebol.com.br/tab_torneio_nacional_1937.html, https://www.campeoesdofutebol.com.br/art_brasilb.html (artilheiros da Série B), https://www.campeoesdofutebol.com.br/art_brasil.html (Série A)
- cobre: jogos com data e placar de 1937 e do Robertão 1967-1968; artilheiros por edição das Séries A e B; total de público por clube (1971-2012) e maiores públicos (não jogo a jogo).
- como baixar: em lote, 1 página por edição/lista (HTML, linhas "dd/mm- A NxM B").
- amostra: 1930s, 1937: 14 jogos, placar 13 e data 11 (a Wikipédia pt confirma o banco nos 4 casos: o erro é da fonte); 1960s, Robertão 1967: 117 jogos, placar 117 e data 117. Artilheiros da Série B 1971, 2004 e 2016 conferidos (SB-013).
- serve a: banco-painel; buscar: terceira opinião para 1937 e o Robertão, artilheiros (Série B 1971). Não serve para datas sozinha.

### CBF (cbf.com.br)
- endereço: https://www.cbf.com.br/futebol-brasileiro/tabelas/campeonato-brasileiro/serie-a/2015
- cobre: tabela de classificação e artilharia; os jogos, súmulas, público e árbitro vêm por chamada de API do navegador (Next.js), não pelo HTML. O endereço antigo de súmula (conteudo.cbf.com.br/sumulas/AAAA/142NNNse.pdf) dá 404.
- como baixar: só descobrindo a API (custo médio; não tentei contornar nada).
- amostra: 0 jogos (a página não traz jogos no HTML).
- serve a: banco-painel; buscar: árbitro e público oficiais de 2013 em diante, se alguém achar a API. Hoje não recomendo.

### Futebol Interior (futebolinterior.com.br)
- endereço: https://www.futebolinterior.com.br/campeonato/brasileirao-serie-b-2009/
- cobre: tabela por rodada de 2006 a 2026 (Séries A e B), carregada por API (wp-json/api/miniscore_get_gamelist).
- como baixar: por API (não testada); o HTML não traz os jogos.
- amostra: 0 jogos.
- serve a: banco-painel; buscar: quarta opinião para datas de 2006-2025. Baixa prioridade (Transfermarkt e Bola na Área já cobrem).

### Hemeroteca Digital (memoria.bn.gov.br)
- endereço: https://memoria.bn.gov.br/DocReader/DocReader.aspx?bib=112518_04&pesq=Itabaiana (Jornal dos Sports 1970-1979; há décadas seguintes e jornais regionais)
- cobre: jornal do dia seguinte de cada jogo, com placar, autores, público, renda e árbitro, desde os anos 1930.
- como baixar: só jogo a jogo, à mão (página ASP.NET com captcha na busca; imagem com OCR). Não dá para baixar em lote.
- amostra: a página responde (200); não li jogos.
- serve a: banco-painel; buscar: desempate dos casos em que as fontes empatam (QA-005, QA-008, River-PI 1979 do SA-017, Portuguesa x Botafogo 1984). Recomendo como último recurso, uma consulta por jogo.

### RSSSF Brasil (rsssfbrasil.com)
- endereço: https://www.rsssfbrasil.com/tablesae/br1975.htm
- cobre: é a base da coleta da Série B (cópias em data/serie_b/rsssfbrasil/); para a Série A seria fonte nova.
- como baixar: em 22/11 o servidor não respondeu daqui (porta 443 sem conexão em 3 tentativas, 21 s cada).
- amostra: 0.
- serve a: banco-painel; buscar: tentar de novo outro dia para a Série A (autores dos gols antigos, se a página trouxer).
