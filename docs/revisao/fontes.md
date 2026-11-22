# Catálogo de fontes

Revisão profunda de 22/11/2026. Uma entrada por fonte, juntando o que os 15 revisores testaram
(`revisao/rodada3/fontes_<P>.md`). Amostra = jogos casados com o pacote ou o banco: "placar igual / data igual".

Regras de uso (valem para todas):
- 1 pedido a cada 2 s, cache em `data/cache/`, tratar o 429 (esperar 30-60 s). Os revisores e coletores dividem o IP.
- Não tente contornar bloqueio.
- Fonte que copia outra não conta como segunda opinião (ex.: a Wikipédia pt cita o Bola n@ Área; muitas páginas da
  Wikipédia copiam a RSSSF).

Agentes: CB = coleta Brasil, CE = coleta Europa, CS = coleta América do Sul, BP = banco e painel (agente 1).

## Geral

### Transfermarkt (calendário e ficha do jogo)
- **Endereço:** calendário `https://www.transfermarkt.com.br/<liga>/gesamtspielplan/wettbewerb/<código>/saison_id/<ano>`
  (ex.: BRA1, BRA2, BRA3, BRA4, BRC, BCP1, IT1, L1, FR1, PO1, ES1, EFD1, AR1N, URU1, CLPD, COLP, TDeA/TDeC, PR1A);
  ficha `https://www.transfermarkt.com/spielbericht/index/spielbericht/<id>`. O `saison_id` é, em geral, o ano anterior.
- **Cobre (calendário: data, hora, rodada, placar, id da ficha):** Série A 1985+ (1985 parcial; 1986 sem grupos E-H);
  Série B 2005+; Série C 2009+; Série D 2010+; Copa do Brasil 1998+; Paulista 2006+; Itália todas; Alemanha 1963/64+;
  França 1948/49+ (antes errado); Portugal 1934/35+; Inglaterra 1888/89 e 1922/23-1991/92 (EFD1; 1889-1922 parcial) e
  Premier League (GB1); Espanha todas; Argentina 2010s; Uruguai 2005/06+; Chile 1990-1996, 1998-2001, 2018-2025;
  Colômbia 2000s+; Peru 2006 e 2014+; Paraguai 2015+; Equador só 2019, 2025 e 2026.
- **Cobre (ficha):** autores com minuto, árbitro, público, cartões, escalações. Até em jogos antigos (Inglaterra 1888+,
  França 1977, Alemanha 1972); no Brasil, público e árbitro só em parte das fichas antes de 2009.
- **Como baixar e custo:** calendário em lote (1 página por temporada, 120-700 KB). Ficha jogo a jogo (~117 KB):
  autores da Série A 1985-2002 ~5.600 páginas (~3 h); França ~27 mil; Portugal 1990+ ~11 mil (~6 h); Inglaterra
  1888-1960 ~14.450 (~8-9 h).
- **Amostras:** Série A 1990s 2.498 jogos: 2.493 / 2.138 (as datas diferentes são, em boa parte, erro do banco); Série A
  2010s 380 / 380 / 380. Série C 2010s placar 468/468; Série D 2010s 840/840. Alemanha 19.220 / 19.220 placares; 102
  das 116 datas diferentes ele acerta. França 27.900 jogos, 17 placares diferentes (3 erros do pacote). Portugal
  20.918 de 20.936 placares; 19.413 datas. Inglaterra 1888-1960: 15.837 jogos, 15.824 / 15.826. Chile 4.713 jogos, 24
  placares diferentes. Argentina 2018/19: 298 de 300 placares. Fichas: Brasil 29 de 30 com a soma dos autores igual ao
  placar; Inglaterra antiga 23 de 24, todas com público.
- **Serve a:** BP (datas da Série A 1985-1999 e da B 2005+; autores da A 1985-2002; árbitro e público); CB (3ª opinião
  de datas da C, D e Copa); CE (datas do Alemão e do Francês; autores e público do Inglês antigo; árbitro e público de
  Portugal); CS (3ª opinião de placar do Chile 1990-1995; árbitro e público).
- **Cuidados:** data em fuso europeu ou UTC (jogo noturno com ±1 dia; Copa 2000s com +1 em 45 de 207); pênaltis somados
  ao placar nos mata-matas (Brasil 1988 e Copa); nomes trocados ("Botafogo FC" é o de Ribeirão Preto; Portugal 1935-1937
  troca Vitória de Setúbal e Guimarães); Portugal antes de 1994/95 com a data da rodada; Série B 2003-2004 errada;
  GB1 antes de 1992 devolve a temporada atual (usar EFD1). Sempre com uma segunda fonte.

### ESPN (placar diário)
- **Endereço:** `https://site.api.espn.com/apis/site/v2/sports/soccer/<liga>/scoreboard?dates=AAAAMMDD` (ex.: ecu.1).
  Já baixada pelas coletas em `data/coleta/<slug>/espn/`.
- **Cobre:** data e hora (UTC), placar, estádio, público, gols com minuto e cartões. Argentina e Chile 2001+; Uruguai,
  Colômbia, Peru, Paraguai e Equador 2005+.
- **Como baixar e custo:** já está no disco.
- **Amostras:** Colômbia 7.968 jogos, data igual em 97%; Peru 6.418 jogos, 87 datas diferentes (quase todas finais);
  Paraguai 5.166 jogos, 5.149 placares iguais; Equador 5.145 jogos, 78 datas diferentes; Argentina e Uruguai: 73 jogos
  adiados que a ESPN tem com outra data (QU-003).
- **Serve a:** CS. Buscar: data dos mata-matas e dos jogos adiados (casar pelo par de clubes dentro da edição).
- **Cuidados:** UTC (converter para a hora local); 0-0 de preenchimento em jogos sem dados (Colômbia 2013 Fi); gol
  repetido ou sem lado; nomes fora de ordem ("Goncalves da Silva Ailton"); jogador "2" ou "22".

### RSSSF (partes que as coletas não leram)
- **Endereço:** `https://www.rsssf.org/tables<letra>/<página>.html`.
- **Cobre e onde buscar:**
  - Colômbia: `colchamp.html` coluna "Runners Up" (vice 1948-2026); "Final Table" de 1987 e 1991-1995; tabelas de
    confrontos de 1948, 1949 e 1960; seções "Relegation";
  - Chile: `chilehist.html` (RELEGATED, PROMOTED e bônus da Polla Gol, 1933-1996);
  - Peru: `peru1912.html` a `peru1921.html` (classificação de 1912-1917; participantes de 1918-1921);
  - Datas no título da fase ("First Leg [Dec 17]", "Final [Dec 18, Quito]") em todas as ligas sul-americanas;
  - Itália: `italNN.html` com a data de cada rodada e o motivo dos jogos "a tavolino";
  - Alemanha: `duitNN.html` com autores dos gols 1963/64-1998/99; `duitchamp.html` (fase final 1902/03-1962/63);
    `ddrNN.html` (DDR-Oberliga);
  - Portugal: `port00.html` a `port06.html` com os marcadores de 1999/00 a 2005/06;
  - artilheiros: `engtops`, `chiletops`, `coltops` (até 2007), `urutops`, `argtops`, `paratops`.
- **Como baixar e custo:** em lote; quase tudo já está em `data/coleta/<slug>/rsssf/`.
- **Amostras:** colchamp: vice igual à Wikipédia es em 101 de 101; chilehist: rebaixados batem com a temporada seguinte
  em todos os anos de 1958-1996; Itália: 3ª opinião em 862 datas (622 contra o pacote); tavolino 20 de 20; Alemanha:
  autores fecham com o placar em 7.678 de 9.660 jogos; datas iguais ao transfermarkt em 101 de 102; Portugal 2000/01:
  284 de 297 jogos fecham; Colômbia 1948 88 de 90, 1949 177 de 182.
- **Serve a:** CS (vices, rebaixados, datas de mata-mata, Peru antigo); CE (datas italianas, autores alemães e
  portugueses, eras antigas).
- **Cuidados:** erra às vezes (gol do Palermo em 1952/53 e 1962/63; data da rodada 7 da A2 2021); França por temporada
  não existe (404). A RSSSF Brasil é outro site (ver Brasil).

### Wikipédia em inglês
- **Endereço:** páginas de temporada e de clube (ex.: `https://en.wikipedia.org/wiki/1994%E2%80%9395_S.L._Benfica_season`),
  listas (`List_of_Argentine_football_champions`, `Bola_de_Prata_(Portugal)`), biografias
  (`Albert_Shepherd_(footballer)`), regras de desempate (`class_rules`).
- **Cobre:** jogos de um clube na temporada (data, placar, marcadores, público, árbitro); artilheiros por temporada;
  listas de campeões; regra de desempate de cada temporada.
- **Como baixar e custo:** 1 página por tema (API; muitos 429 em 22/11).
- **Amostras:** Bola de Prata 87 de 92 artilheiros (4 erros dela, 1 do pacote: Seferović 2018/19); artigos do Benfica
  decidiram PT-002 e PT-004; Peru 1926-1965: 2.172 de 2.291 (copia a es).
- **Serve a:** CE (Portugal, Inglês 1905/06, desempate do Espanhol); CS (listas de campeões).
- **Cuidados:** muitas tabelas copiam a RSSSF; erra digitação (Bola de Prata 1945-1949).

### footballdatabase.eu
- **Endereço:** `https://www.footballdatabase.eu/en/competition/overall/<id>-<nome>/<temporada>/<id>-journee_<n>`
  (cada temporada tem id próprio).
- **Cobre:** data, placar, autores com minuto, tabela, promovidos e rebaixados. Alemanha 1963/64+ (e Oberligas 1945-1963);
  França 88 temporadas.
- **Como baixar e custo:** 1 página por rodada (~10 jogos). Grátis, mas **50 páginas por dia por IP** sem conta.
- **Amostras:** Alemanha 236 de 238 em data e placar (as 2 são erro dela); França 1977/78: tabela e rebaixados batem.
- **Serve a:** CE (datas e rodadas da França nos anos 1930: 356 jogos sem data; autores antigos); CS (testar para
  Uruguai e Equador antigos, onde não há outra fonte).
- **Cuidados:** limite diário esgotou em 22/11; depois de ~40 páginas devolve "Adblocker detected" (HTTP 200, sem jogos):
  10 s entre pedidos e conferir se a página tem `/en/match/overview`. Na Alemanha repete as datas erradas da base: não é
  independente para datas.

### ogol (ficha de jogo e calendário)
- **Endereço:** ficha `https://www.ogol.com.br/jogo/1995-04-27-vasco-nacional-am/666997`; calendário
  `https://www.ogol.com.br/edicao/liga-chilena-1977/37074/calendario?page=4`.
- **Cobre:** ficha com escalações e, em parte, autores com minuto, árbitro, estádio e público (Copa 1995: público 678);
  motivo de resultado fora de campo (Portugal).
- **Como baixar e custo:** jogo a jogo (~8 mil Série C, ~6 mil D, ~4 mil Copa; ~14 mil Portugal antes de 2006/07).
  Calendário: 50 jogos por página.
- **Amostras:** Série A: 18 fichas, placar sempre igual (autores em ~1/3 em 1980 e 1993); Portugal: 5 fichas de
  1963-1966 fecham com o pacote.
- **Serve a:** CB (autores da Copa 1990-1999 e da Série C 1994-2001); CE (marcadores de Portugal antes de 2006/07); CS
  (datas do Chile 1964, 1971, 1977, 1982); BP (autores e árbitro da Série A anos 1970).
- **Cuidados:** jogo noturno gravado no dia seguinte; o `fonte_id` do pacote nem sempre é o id da ficha (Portugal: 4 de
  9 abriram outro jogo); calendário vazio no Equador antigo e no Paraguai antes de 2005; na Itália repete as datas da base
  (não serve para conferir data).

### football-data.co.uk
- **Endereço:** `https://www.football-data.co.uk/mmz4281/9394/D1.csv` (1 CSV por liga e temporada).
- **Cobre:** placar e data de 1993/94 em diante; hora, árbitro e estatísticas nas recentes (Inglaterra).
- **Como baixar e custo:** em lote; as coletas já têm.
- **Amostras:** Alemanha 10.098 jogos, 0 placares diferentes, 152 datas diferentes (117 em 1993/94); Portugal: com o
  transfermarkt, desmente o ogol em 26 datas.
- **Serve a:** CE. Buscar: data quando o ogol diverge (Portugal 1995-2016).
- **Cuidados:** de 1993/94 a 1996/97 a data é a da rodada (Alemanha e França): não usar para datas antes de 1997/98.
  Não traz árbitro de França nem de Portugal; o árbitro inglês vem em 3 formatos.

### 11v11
- **Endereço:** `https://www.11v11.com/matches/huddersfield-town-v-west-bromwich-albion-29-august-1925-63155/`
- **Cobre:** só a liga inglesa: placar, estádio e público de jogos antigos (1925: 21.975); sem autores.
- **Como baixar e custo:** jogo a jogo.
- **Amostras:** 2 de 2 datas confirmadas (1935/36, 1953/54).
- **Serve a:** CE (público e estádio do Inglês antes de 1960; alternativa ao transfermarkt).
- **Cuidados:** não tem Alemanha, França, Itália nem Colômbia (404).

## Brasil

### Bola n@ Área (bolanaarea.com)
- **Endereço:** `https://www.bolanaarea.com/brasileirao_1975.htm`, `serie_b_1985.htm`, `serie_c_1981_tab.htm`,
  `serie_d_2013_fasefinal.htm`, `copa_do_brasil_1989_tabela.htm`, `taca_brasil_1959_tab.htm` (índices `gal_*.htm`).
- **Cobre:** Série A 1971-2024 e Taça Brasil; Série B 1971-2024 (inclusive 1986, 1987 e 2000); Série C 1981-2024
  (inclusive 1987 e 2000); Série D 2009-2024; Copa 1989-2024. Por jogo: data, placar, pênaltis; em muitos anos público,
  árbitro e autores. Por edição: classificação final, artilheiros, participantes com cidade, "números do torneio".
- **Como baixar e custo:** em lote, 2 a 6 páginas por edição (~250 páginas A e B; 295 C, D e Copa). HTML
  windows-1252; leitores `revisao/QA/bna.py` e `revisao/QC/bola.py`.
- **Amostras:** Série A 1970s 1.620 jogos: 1.603 / 1.570; Série B 1990s 1.861: 1.820 / 1.252 (o banco não tem data em
  301 jogos de 1991); Série C 2000s 2.390/2.407 e 1.904/2.335; Série D 2010s 1.883/1.890 e 1.835/1.890; Copa 2010s
  1.108/1.110 e 1.063/1.110. Achou os 17 pênaltis que faltam na Série D.
- **Serve a:** BP (datas das Séries A e B 1971-1999; artilheiros da B; cidades); CB (pênaltis; datas; público e
  árbitro; autores que faltam na C, D e Copa; totais por edição).
- **Cuidados:** erra sozinha em ~10 placares da Série B e em datas (usa a da rodada: Série A 1996-1997, Série C anos
  1990-2000). Só vale com outra fonte. A Wikipédia pt copia o Bola: não são duas fontes.

### Futebol Nacional (futebolnacional.com.br)
- **Endereço:** resumo de cada competição com o código das edições, ex. Paulista
  `https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=A27437D2CE0894275C03A3BAEDA49F41A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR`;
  edição `controller.jsp?module=championship&code=<código>&lang=pt-br` (os códigos da `app/championship.jsp` não servem).
- **Cobre:** Paulista 1902-2026 inteiro (jogos com data, placar, fase e nota: cancelado, W.O., "ganhou os pontos");
  Série C 1998-1999 e 2007-2026; Série D 2009-2026; Copa em boa parte dos anos (1999 com a preliminar); campeão, vice e
  artilheiro de todas as edições. Árbitro e público só na parte paga.
- **Como baixar e custo:** em lote, 1 página por edição (137 do Paulista ~6 min; 91 da C, D e Copa). Às vezes volta
  vazia: esperar 30-60 s. Leitores `revisao/QS/fn_jogos.py` e `revisao/QC/fn.py`.
- **Amostras:** Paulista por década, todas acima de 99% em placar (ex.: 1980s 3.717/3.738 e 3.733/3.738); 1990s data
  2.698/2.896 (1997 com +1 dia). Série C 2010s 1.736/1.736 e 1.665/1.736; Série D 2020s 3.538/3.541.
- **Serve a:** CB. Buscar: jogos cancelados, W.O. e pontos fora de campo (Paulista); jogos que faltam; 3ª opinião de
  placar e data; preliminar da Copa 1999.
- **Cuidados:** erra datas em lote (Paulista 1978, 1990, 1997); mistura o Troféu do Interior nas edições 2007-2023; não
  diz de onde tirou cada jogo. Usar como 3ª opinião, nunca como base única.

### FPF (API do site e lista oficial de campeões)
- **Endereço:** jogos `https://futebolpaulista.com.br/Handlers/Competicoes/ListarTabela.ashx?IdCampeonato=73&Ano=2019&Rodada=1&IdClube=0&IdCategoria=39`
  (A2: IdCampeonato=74); artilharia `ListarArtilharia.ashx?idCampeonato=73&IdClube=&exercicio=<ano>&idCategoria=39&pagina=0&tipoGol=`;
  campeões da A2 `Handlers/Clube/ListarCampeoes.ashx?IdCategoria=2`; campeões da A1 (Tableau)
  `https://public.tableau.com/static/images/Ca/CampeesSrieA1/Dashboard1/1.png`; súmula `http://conteudo.fpf.org.br/sumulas/2019/3973/1.pdf`.
- **Cobre:** A1 2007-2026 e A2 2008-2026: data, hora, rodada, fase e grupo, estádio, placar; artilharia oficial
  completa; súmulas (árbitro, gols, cartões) ~2016+; campeões oficiais (A2 1916-2026).
- **Como baixar e custo:** em lote, JSON: 1 pedido por rodada (~400 para 2007-2026) + 1 por ano de artilharia;
  súmulas 1 PDF por jogo (~2.200).
- **Amostras:** A1 2007-2025: 2.806 jogos, 2.805 placares iguais e 2.738 datas iguais (68 diferentes: QS-008); A2:
  180 de 180 placares, 164 datas (as 16 são erro do pacote); campeões da A2 63 de 63.
- **Serve a:** CB. Buscar: datas oficiais 2007+, fase e grupo de 2024-2025, artilheiros 2007-2026, edição de 2026,
  campeões das edições da A2 que faltam.
- **Cuidados:** "NomePopular" é o nome de hoje ("Osasco Sporting" = Oeste): casar por id do clube ou por par + data.
  Os jogos "só FPF" são o Troféu do Interior.

### CBF (súmulas em PDF)
- **Endereço:** `https://conteudo.cbf.com.br/sumulas/<ano>/<código><nº>se.pdf` (Série A 142, C 342, D 542, Copa 424);
  borderô `<código><nº>b.pdf`.
- **Cobre:** data, hora, estádio, árbitro, gols com minuto e tipo, cartões, escalações. Série C 2013-2025, D 2013 e
  2015-2025, Copa 2014-2025.
- **Como baixar e custo:** jogo a jogo (~57 KB por PDF; texto com PyMuPDF).
- **Amostras:** 9 súmulas, datas e placares iguais; resolveu o SD-011.
- **Serve a:** CB (cartões, hoje 0%; autores e árbitro 2013+; data oficial em caso de dúvida).
- **Cuidados:** 2009-2012 dão 404; o borderô (público) é imagem. O site novo da CBF pede token (ver descartadas).

### RSSSF Brasil (rsssfbrasil.com)
- **Endereço:** `https://rsssfbrasil.com/tablessz/sptops.htm`; páginas da A2 não linkadas `sp1968l2.htm`, `sp1969l2`,
  `sp1971l2`, `sp1976l2`, `sp1980l2`, `sp1984l2`.
- **Cobre:** artilheiros do Paulista 1902-2021 (com a liga); jogos da A2 de 1968-1984 (parciais).
- **Como baixar e custo:** em lote; a `sptops.htm` já está em `data/coleta/bra-sp-1/rsssfbrasil/`.
- **Amostras:** artilheiros: bate com o Futebol Nacional nas 17 edições em que a Wikipédia pt diverge.
- **Serve a:** CB (artilheiros do Paulista; A2 1967-1984); BP (Série A, se a página trouxer autores).
- **Cuidados:** em 22/11 o servidor não respondeu para o revisor das Séries A e B (tentar outro dia).

### Wikipédia em português
- **Endereço:** páginas de edição (ex.: `https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_1985_-_Segunda_Divisão`);
  `Predefinição:Campeões_do_Campeonato_Paulista_de_Futebol_-_Série_A2`; Portugal `Primeira_Divisão_de_1950–51`.
- **Cobre:** A2 1947-2026 (menos 1972, 2008, 2009): infobox (rebaixados, promovidos, artilheiro), tabelas e finais;
  predefinição com vice, 3º e 4º; Série B (datas jogo a jogo de 1990 e 1991); Portugal 1934-2026 (matriz, tabela,
  "Despromovidos", devolução dos pontos do Porto).
- **Como baixar e custo:** em lote, 1 pedido por página (`action=raw` ou API).
- **Amostras:** A2: tabelas 326 linhas iguais e 65 diferentes (nomes antigos); artilheiros 36 de 36; predefinição:
  campeões 63/63, vices 58/63 (os 5 são erro do pacote). Portugal: placares 16.072 de 16.143; campeões 92/92.
- **Serve a:** CB (rebaixados e artilheiros da A2; edições 1967-1984); BP (datas da Série B 1990-1991); CE (desempates e
  rebaixamentos fora de campo de Portugal).
- **Cuidados:** cita o Bola n@ Área (Copa 1990, 1991, 1995, 1999, 2001; Série C 1981, 1990, 1992, 1994) e a RSSSF;
  erra artilheiros do Paulista em 17 edições; tabelas de Portugal com ~45 erros de digitação.

### Campeões do Futebol (campeoesdofutebol.com.br)
- **Endereço:** `https://www.campeoesdofutebol.com.br/torneio_robertao_1967.html`, `art_brasilb.html`, `art_brasil.html`.
- **Cobre:** jogos de 1937 e do Robertão 1967-1968; artilheiros das Séries A e B; públicos por clube.
- **Como baixar e custo:** em lote, 1 página por lista.
- **Amostras:** Robertão 1967 117 de 117 em placar e data; 1937 14 jogos, 13 / 11 (o erro é dela).
- **Serve a:** BP (artilheiros da Série B; 3ª opinião de 1937 e do Robertão).
- **Cuidados:** não serve sozinha para datas.

### Jornais da época (Hemeroteca Digital, Estadão, Folha)
- **Endereço:** `https://memoria.bn.gov.br/hdb/periodico.aspx` (Jornal dos Sports, Jornal do Brasil, Diario de
  Pernambuco, Correio Paulistano...); `https://acervo.estadao.com.br/`; `https://acervo.folha.com.br/`.
- **Cobre:** o jogo do dia seguinte: placar, autores, público, renda, árbitro, desde os anos 1900-1930.
- **Como baixar e custo:** só jogo a jogo, à mão (busca com captcha e JavaScript; Estadão e Folha pedem assinatura).
- **Amostras:** nenhuma jogo a jogo; a Hemeroteca abriu para um revisor e falhou (DNS) para outro.
- **Serve a:** CB e BP, só para desempatar casos pontuais (D-13, D-14 em `decisoes-guilherme.md`).
- **Cuidados:** você decidiu (A2, 21/11) que o que só existe em jornal fica de fora. Uso só para tirar dúvida.

### Sites de clubes paulistas (SPFCpédia, Meu Timão, Palmeiras)
- **Endereço:** `https://www.saopaulofc.net/enciclopedia-clube-lista-de-jogos/`, `https://www.meutimao.com.br/estatisticas-do-corinthians-em-1930`,
  `https://www.palmeiras.com.br/derby/todos-os-jogos`.
- **Cobre:** jogos de um clube (data, estádio, em parte autores).
- **Como baixar e custo:** jogo a jogo; formato muda por site. Custo alto, cobertura parcial.
- **Amostras:** só verificado que respondem.
- **Serve a:** CB, prioridade baixa (autores da era amadora, se você quiser esse nível).

## Europa

### Wikipédia em italiano
- **Endereço:** `https://it.wikipedia.org/w/index.php?title=Serie_A_1952-1953&action=raw`; páginas de temporada de
  clube (`Associazione_Calcio_Torino_1952-1953`); `Albo_d%27oro_del_campionato_italiano_di_calcio`; Argentina
  `Primera_División_1896_(Argentina)`.
- **Cobre:** Itália 1929/30-2025/26: classificação com punições, matriz, calendário com a data de cada jogo, "a tavolino",
  spareggi, artilharia; fichas de jogo nas páginas de clube (público, árbitro, autores); campeões de 1898 em diante.
  Argentina: tabela e artilheiro de cada temporada desde 1891.
- **Como baixar e custo:** em lote (95 páginas da Itália; leitor `revisao/IT/itwiki.py`).
- **Amostras:** classificação 1.692 de 1.703 linhas; placares 28.896 jogos (33 diferenças, 7 erros do pacote); datas
  26.830 de 28.248 iguais (622 erros do pacote confirmados pela RSSSF); artilheiro 93 de 95; Albo d'oro 95 de 95;
  páginas de clube 3 de 3 casos decididos; Argentina 1896 igual à es.
- **Serve a:** CE (datas, tribunal, declassamentos, readmissões, spareggi, ordem da classifica avulsa; campeões
  1898-1929); CS (3ª opinião do amadorismo argentino).
- **Cuidados:** a matriz tem erros de célula e de coluna (1967/68); datas de julho de 2020 precisam do ano certo; na
  Argentina cita a RSSSF e a IFFHS (não independente); API com 429.

### Wikipédia em alemão
- **Endereço:** `https://de.wikipedia.org/wiki/Fußball-Bundesliga_1971/72`; `Liste_der_Torschützenkönige_der_Fußball-Bundesliga`;
  `Deutsche_Fußballmeisterschaft_1955/56`; `Liste_der_deutschen_Fußballmeister`.
- **Cobre:** Bundesliga 1963/64-2025/26: tabela (Abzug = pontos tirados; Rang2 = posição dividida), quem caiu e por quê,
  matriz, Relegation, notas de tribunal e jogos repetidos, artilheiros; fase final de 1903 a 1963.
- **Como baixar e custo:** em lote, 1 página por temporada (wikitexto; scripts `revisao/DE/dewiki.py`).
- **Amostras:** placares 17.962 de 17.962; tabelas 1.129 de 1.131 linhas (as 2 são achados); campeões 63/63;
  artilheiros 63/63; rebaixados certos nas 63.
- **Serve a:** CE (punições, tribunal, Relegation, nome curto do artilheiro; era antiga 1902-1963).

### Wikipédia em francês
- **Endereço:** `https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_1974-1975`;
  `Meilleurs_buteurs_du_championnat_de_France_de_football`.
- **Cobre:** 88 temporadas: tabela com bônus e cor de rebaixado, grade de resultados com notas de tribunal ("tapis
  vert"), "relégué fin", barrages, regras (bônus, média de gols); artilheiros pela contagem da LFP.
- **Como baixar e custo:** em lote pela API (1 página por temporada; leitor `revisao/FR/frwiki.py`).
- **Amostras:** tabelas 1.638 de 1.666 linhas; grade 29.026 de 29.087 placares; artilheiros 76 de 88.
- **Serve a:** CE (tribunal, bônus, rebaixamentos administrativos, fusões; artilheiros e nomes usuais).
- **Cuidados:** a API dá 429 com frequência (esperar 45 s); nos anos 2010 a grade tem linhas desalinhadas (usar o
  transfermarkt ali).

### BDFutbol (bdfutbol.com)
- **Endereço:** temporada `https://www.bdfutbol.com/es/t/t1928-29.html` (Espanha), `teng1960-61.html` (Inglaterra);
  ficha `https://www.bdfutbol.com/es/p/p.php?id=<id>`; escudos `/i/eg/<id>.png`.
- **Cobre:** Espanha 1928/29+ e Inglaterra 1960/61+: todos os jogos com data, placar, estádio e árbitro (Espanha 100%;
  Inglaterra 74-100%); ficha com autores e minuto, árbitro, escalações, cartões recentes. Sem público.
- **Como baixar e custo:** temporadas em lote (95 + 66 páginas, já em `data/cache/revisao/QE/`; leitor
  `revisao/QE/bdfutbol.py`). Fichas jogo a jogo (~890 KB): Espanha antes de 2001/02 19.668 jogos (~11 h, ~17 GB). O
  site tem serviço de dados pago: perguntar antes de baixar tanto.
- **Amostras:** Espanha 27.716 jogos: 27.714 / 27.693; Inglaterra 28.662: todos os placares, 28.640 datas (22 erros
  dele); fichas 72 de 72 com a soma dos autores igual ao placar.
- **Serve a:** CE (árbitro e estádio do Espanhol em lote; árbitro do Inglês 1960-2000; autores antigos; EN-016); BP
  (escudos de época: CD Málaga, AD Almería).
- **Cuidados:** a tabela antes de 1976 ordena por saldo (erro dele); ignora a punição do Everton 2023/24.

## América do Sul

### Wikipédia em espanhol
- **Endereço:** páginas da liga (`Serie_A_de_Ecuador`, `Primera_División_de_Chile`, `Categoría_Primera_A`,
  `Primera_División_del_Perú`, `Primera_División_de_Paraguay`, `Primera_División_de_Uruguay`) e de cada temporada;
  anexos (`Anexo:Ascensos_y_descensos_de_la_Categoría_Primera_A`, resultados do Paraguai).
- **Cobre:** campeão, vice, 3º e 4º; rebaixados por ano; artilheiros; tabelas por fase e acumuladas, com punições;
  jogos com data (Chile ~1992+, Colômbia 2005+, Equador 2008+, Peru 1930-2008, Paraguai 2007+).
- **Como baixar e custo:** em lote, 1 página por liga ou temporada (API).
- **Amostras:** Chile campeões 109/109, vices 102/109 (os 7 são erro do pacote); Colômbia campeão e vice 101/101,
  artilheiros 73/100; Equador campeão e vice 68/68, 3º/4º 221 de 272 (51 erros do pacote), 3.030 placares iguais;
  Peru 7.736 de 8.747 placares, vices 107/109; Paraguai campeão 133/133, artilheiro 82/95.
- **Serve a:** CS. Buscar: vices e pódio; rebaixados (Ascensos y descensos); artilheiros recentes; tabela acumulada do
  Peru; datas das finais; nota da AUF sobre títulos.
- **Cuidados:** páginas antigas do Chile (1933-1961) copiam a RSSSF; API com muitos 429 em 22/11 (110 páginas do Chile
  levaram mais de 1 hora).

### historiadeboca.com.ar
- **Endereço:** campanha `https://historiadeboca.com.ar/campeonato-1928/1928/1012.html`; ficha
  `https://historiadeboca.com.ar/partido/newell_s-0-boca-2-temporada-1989-90/2321/1990/36/29.html`.
- **Cobre:** todos os jogos do Boca Juniors 1905-2026 (data, rodada, placar, estádio; na ficha, árbitro, escalações e
  autores). Separa torneios anulados e desempates.
- **Como baixar e custo:** 1 página por campanha (+2 pedidos para achar o endereço); fichas jogo a jogo (~4.000).
  Scripts `revisao/QU/baixar_hdb.py` e `cmp_hdb.py`.
- **Amostras:** 1.278 jogos do Boca (1913-2025): 1.270 placares iguais; 964 datas iguais e 272 só com o ano errado (o
  erro é do banco, AR-022).
- **Serve a:** CS. Buscar: data de cada rodada nas temporadas antigas (o Boca joga todas); jogos do Boca que faltam.
- **Cuidados:** site de torcedor, de um clube só; não cobre antes de 1913.

### AUF (auf.org.uy)
- **Endereço:** `https://www.auf.org.uy/historico-temporadas/3/12/` (2025; ids 2 = 2013/14 ... 13 = 2026); tabela anual
  `https://www.auf.org.uy/url.php?id=ajaxapp&tabla_anual=1&id1=3&id2=12`.
- **Cobre:** Uruguai 2013/14-2026: todos os jogos (data, hora, estádio), Supercopa em seção própria, tabela de cada
  torneio, tabela anual oficial com punições, artilharia oficial; escudos dos clubes atuais.
- **Como baixar e custo:** em lote, 1 página por temporada (~2 MB, cp1252) + 1 pedido da tabela anual. Leitor
  `revisao/QU/auf.py`.
- **Amostras:** 3.357 jogos: 2010s 1.578/1.615 e 1.564/1.615; 2020s 1.724/1.738 e 1.523/1.738. Todas as diferenças de
  placar são W.O., tribunal ou Supercopa.
- **Serve a:** CS (tabela anual, decisões, Supercopa, datas de 2020, artilharia); BP (escudos).
- **Cuidados:** só de 2013/14 em diante; erra a contagem de pênaltis em 5 decisões (a RSSSF fecha).

### BDFA (bdfa.com.ar)
- **Endereço:** `https://www.bdfa.com.ar/argentina-campeones-primera-division.html`; resumo
  `https://www.bdfa.com.ar/resumen-campeonato-5615.html`; escudo `https://www.bdfa.com.ar/imagenes/<clube>_p.gif`.
- **Cobre:** campeões; resumo (tabela, descensos, punições, artilheiros) de 2012/13 a 2021; escudo de todos os clubes
  argentinos. Não tem a lista de jogos.
- **Como baixar e custo:** 1 página por torneio (latin-1).
- **Amostras:** 2018/19: tabela igual à RSSSF; artilheiro igual ao banco.
- **Serve a:** CS (rebaixados 2012/13-2021); BP (114 escudos que faltam).
- **Cuidados:** cobertura curta; resumo de 1931 e 2025 com erro do servidor.

## A testar outro dia

- footballdatabase.eu para Uruguai e Equador antigos (quando o limite diário voltar).
- dechalaca.com (Peru): respondeu, sem amostra; pode desempatar placares antigos (PE-017).
- Gallica (jornais franceses L'Auto e L'Équipe): sugerida para as dúvidas FR-017 e FR-005; não testada.
- foradejogo.net (Portugal, fonte dos artigos de clube da Wikipédia en): não respondeu em 22/11.
- API do Futebol Interior (`wp-json/api/miniscore_get_gamelist`, Séries A e B 2006-2026): não testada; baixa prioridade.

## Testadas e descartadas

- Soccerway: endereços antigos levam à página inicial (site novo em JavaScript).
- Futebol Interior (HTML): não traz os jogos (só por API).
- Futpédia (Globo): não respondeu.
- Site novo da CBF (`cbf.com.br/futebol-brasileiro/tabelas/...`): monta as tabelas por API que pede token.
- ligue1.com: só a temporada atual (ignora o parâmetro `season`).
- ligaportugal.pt, anfp.cl, liga1.pe, ligapro.ec, apf.org.py: só a temporada atual ou nada histórico.
- afa.com.ar: só notícias. dfb.de: montado no navegador. legaseriea.it: redireciona.
- statto.com: só a Premier League de 1992/93 a 2016/17. myfootballfacts.com: sem jogos antigos.
- englandfootballonline.com, solofutbol.cl, historiayfutbol.com, historiadelfutbolargentino.com,
  estadisticasfutbol.com.ar, museodelfutbol.uy, enciclopediadelcalcio.it, footballfacts.ru: não abriram.
- iffhs.com: página vazia. golgolgol.net (arquivo da web): veio vazio.
- padreydecano.com, nacional.uy, decano.com: sem base de jogos.
- RSSSF França por temporada (`fran34.html`): não existe (404).
- Transfermarkt Equador (EC1N): só 2019, 2025 e 2026. ogol Equador antigo e Paraguai antes de 2005: calendário vazio.

## Bloqueadas (403)

worldfootball.net, weltfussball.de, livefutbol.com, fbref.com, kicker.de, fussballdaten.de, zerozero.pt.
