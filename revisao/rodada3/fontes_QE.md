# Fontes avaliadas — Inglês (eng-1) e Espanhol (esp-1), revisor QE, 22/11/2026

Testadas por amostra e, quando a página da temporada traz todos os jogos, por comparação completa. Scripts em
`revisao/QE/`, páginas em `data/cache/revisao/QE/` (fora do git). Nenhuma delas foi usada pela coleta (engsoccerdata,
football-data, ogol, ESPN, RSSSF, Wikipédia en) nem pelas revisões anteriores (11v11, Wikipédia en/es, football-data para
datas).

## Resumo: placares e datas por década contra a fonte nova

| Década | esp-1 (BDFutbol) jogos · placar igual · data igual | eng-1 jogos · placar igual · data igual (fonte) |
|---|---|---|
| 1880s | — | 176 · 176 · 167 (transfermarkt; as 9 diferenças são da temporada 1889/90, incompleta e com datas impossíveis lá) |
| 1890s | — | 116 · 116 · 116 (transfermarkt; parcial) |
| 1900s | — | 544 · 544 · 544 (transfermarkt; parcial) |
| 1910s | — | 420 · 420 · 420 (transfermarkt; parcial) |
| 1920s | 180 · 180 · 179 | 3.955 · 3.955 · 3.955 (transfermarkt) |
| 1930s | 756 · 755 · 752 | 4.158 · 4.158 · 4.157 (transfermarkt) |
| 1940s | 1.770 · 1.770 · 1.766 | 1.848 · 1.848 · 1.848 (transfermarkt) |
| 1950s | 2.400 · 2.400 · 2.399 | 4.620 · 4.607 · 4.619 (transfermarkt; os 13 placares são erro dele: 1ª rodada de 1957/58 com placares de enfeite) |
| 1960s | 2.400 · 2.400 · 2.400 | 4.620 · 4.620 · 4.616 (BDFutbol) |
| 1970s | 2.994 · 2.993 · 2.993 | 4.620 · 4.620 · 4.617 (BDFutbol) |
| 1980s | 3.372 · 3.372 · 3.365 | 4.414 · 4.414 · 4.404 (BDFutbol) |
| 1990s | 3.964 · 3.964 · 3.964 | 4.128 · 4.128 · 4.127 (BDFutbol) |
| 2000s | 3.800 · 3.800 · 3.797 | 3.800 · 3.800 · 3.796 (BDFutbol) |
| 2010s | 3.800 · 3.800 · 3.799 | 3.800 · 3.800 · 3.800 (BDFutbol) |
| 2020s | 2.280 · 2.280 · 2.279 | 2.280 · 2.280 · 2.280 (BDFutbol) |

- esp-1: os 27.716 jogos (todas as 95 temporadas, inclusive 2025/26). Diferenças de placar: 1932/33 Athletic 9-5 Racing
  (BDFutbol 9-4; o transfermarkt dá 9-5, como o pacote; ES-015 já tratado) e 1979/80 CD Málaga x Salamanca (BDFutbol 0-0, o
  jogo anulado; o pacote fica com o 0-3 confirmado em 1982). Datas: 23 diferenças; a terceira opinião (ogol, transfermarkt) confirma o pacote em 19; 1 erro do pacote (QE-003), 2 jogos
  suspensos e completados noutro dia (QE-004) e 1 dividido (1932/33 Alavés x Betis: BDFutbol e transfermarkt 15/01/1933, pacote e ogol 17/01).
- eng-1: 44.499 dos 51.330 jogos (1888/89, 1922/23-2025/26 inteiras; 1889/90-1921/22 em parte). Datas: o pacote está certo em
  todas as diferenças com o BDFutbol (11v11, ogol ou transfermarkt confirmam); 1 erro do pacote (QE-005).
- Classificação final do BDFutbol x pacote: esp-1 1.614 de 1.624 linhas iguais (fora 1986/87, em grupos; diferenças: 1960/61,
  QE-002; 1932/33 o 9-4; 1979/80 o jogo anulado; punições, que o BDFutbol mostra sem pontos); eng-1 1.362 de 1.383 (igual de
  1976/77 em diante, menos 2023/24, em que o BDFutbol ignora a punição do Everton; antes de 1976 ele ordena pelo saldo, não
  pela média de gols: erro dele).

### BDFutbol — Espanha (página da temporada)
- endereço: https://www.bdfutbol.com/es/t/t1928-29.html (uma por temporada; 1999/00 = t1999-00.html)
- cobre: 1ª divisão espanhola 1928/29-2026/27, todos os jogos: rodada, data, mandante, placar, visitante, **estádio** e
  **árbitro** (árbitro em 100% dos jogos de todas as décadas); classificação final com cartões da temporada (TA/TR)
- como baixar: em lote; 1 página HTML por temporada (~1 MB), 95 páginas (já em cache); leitor em `revisao/QE/bdfutbol.py`
  (`jogos_temporada`, `tabela_final`)
- amostra: 27.716 de 27.716 jogos casados; placar igual em 27.714, data igual em 27.693 (as 23 diferenças estão em
  `revisao/QE/cmp_bdfutbol_esp.txt`; terceira opinião em `revisao/QE/terceira_datas.py`)
- serve a: coleta-europa; buscar: **árbitro** (hoje 0% no esp-1) e **estádio antes de 2001/02** (hoje 0%), em lote; data e
  placar como 3ª opinião

### BDFutbol — Espanha e Inglaterra (ficha do jogo)
- endereço: https://www.bdfutbol.com/es/p/p.php?id=1 (o id vem da página da temporada)
- cobre: autores dos gols com minuto (gol contra "(pp)" e pênalti "(p)"), árbitro, hora (às vezes), escalações, técnicos,
  cartões (com minuto, nas fichas recentes; nas amostras de antes de 2000 não veio cartão); **sem público**. Espanha desde
  1928/29; Inglaterra desde 1960/61
- como baixar: jogo a jogo; ~890 KB por página. Autores antes de 2001/02: Espanha 19.668 jogos (~11 h a 1 pedido/2 s,
  ~17 GB), Inglaterra 1960/61-2000/01 ~18.160 jogos (~10 h, ~16 GB). O site oferece "Servicio de Datos / API Datos" (pago):
  vale perguntar antes de baixar tanto
- amostra: 72 fichas (2 a 6 por década, sorteio fixo; `revisao/QE/amostra_fichas_saida.txt`): 72 de 72 com a soma dos
  autores igual ao placar; nas décadas em que o pacote tem autores (2001+), 95 de 99 autores iguais (os outros 4: grafia —
  "Loren" x "Lorenzo Morón", "Nzonzi" x "N'Zonzi" — e um gol contra de Ximo Navarro que a ESPN dá a Franco Cervi, Celta 4-0
  Alavés, 07/05/2022). Os 12 jogos do EN-016: todos com autores, fechando com o placar
- serve a: coleta-europa; buscar: **EN-016** (feito: 12 fichas), autores antes de 2001/02 (Espanha toda; Inglaterra desde
  1960/61), escalações e técnicos

### BDFutbol — Inglaterra (página da temporada)
- endereço: https://www.bdfutbol.com/es/t/teng1960-61.html (não existe antes de 1960/61: teng1959-60 dá 404)
- cobre: 1960/61-2026/27, todos os jogos com data, placar, estádio e árbitro (árbitro em 74% dos jogos dos anos 1960, 86%
  nos 1970, 85% nos 1980, 100% de 1990 em diante)
- como baixar: em lote; 66 páginas (~1,6 MB; já em cache)
- amostra: 28.662 de 28.662 jogos casados; placar igual em todos; data igual em 28.640 (22 diferenças, todas erro do BDFutbol
  pela terceira opinião); árbitro: sobrenome igual ao do football-data em 9.607 de 9.880 jogos de 2000/01+ (o resto é grafia
  do football-data e 40 jogos com outro nome, QE-006)
- serve a: coleta-europa; buscar: **árbitro de 1960/61 a 1999/00** (hoje 0%) e nome completo do árbitro de 2000/01+ (QE-006);
  estádio de 1960/61 a 2000/01 (hoje 0%)

### transfermarkt — Inglaterra, "First Division (- 91/92)" (EFD1), calendário da temporada
- endereço: https://www.transfermarkt.com/first-division-bis-91-92-/gesamtspielplan/wettbewerb/EFD1/saison_id/1925
  (achado pela busca do site; GB1 só tem a Premier League, de 1992/93)
- cobre: 1888/89 e 1922/23-1991/92 completos; 1889/90-1921/22 só uma parte dos jogos (0 a 196 por temporada); data e placar,
  com o id da ficha
- como baixar: em lote; 1 página por temporada (~120 KB); 1888-1959 já em cache (62 páginas)
- amostra: 15.837 jogos de 1888/89-1959/60 casados; placar igual em 15.824 (13 erros dele em 1950/51, 1951/52 e 1957/58);
  data igual em 15.826 (diferenças: 1889/90, erro dele; 1935/36 Stoke x Birmingham, erro dele pelo 11v11; 1953/54 Sheffield
  Wednesday x Aston Villa, erro do pacote, QE-005). `revisao/QE/cmp_tm_eng.py`, saída `cmp_tm_eng.txt`
- serve a: coleta-europa; buscar: data e placar como 3ª opinião antes de 1960; o id da ficha (abaixo)

### transfermarkt — ficha do jogo (Inglaterra e Espanha)
- endereço: https://www.transfermarkt.com/spielbericht/index/spielbericht/4252483
- cobre: autores com nome completo e na ordem (e assistências nos jogos recentes), **público**, árbitro, estádio, placar do
  intervalo, cartões, substituições. Inglaterra: desde 1888/89 onde o calendário existe; Espanha: autores e árbitro desde 1928/29
  (amostra 1960 e 1988), público só em parte dos jogos de 2000 em diante (1960 e 1988 sem público)
- como baixar: jogo a jogo, ~117 KB por página. Inglaterra 1888/89 + 1922/23-1959/60: ~14.450 páginas (~8-9 h, ~1,7 GB);
  1960/61-1991/92 mais ~14.500; Premier League 1992/93-2000/01 (GB1) ~3.670
- amostra: 24 fichas de 1888/89 a 1959/60 (3 por década; `revisao/QE/amostra_tm_saida.txt`): 23 com a soma dos autores igual
  ao placar (a que falha é de 1889/90, temporada incompleta no site), 24 com público (ex.: Arsenal 0-1 Tottenham, 29/08/1925,
  53.183, árbitro Dave Asson); 1995 (GB1): público, árbitro e cartões; Espanha 2000/01 e 2004/05: público em 3 de 4
- serve a: coleta-europa; buscar: **autores e público do Inglês antes de 2001/02** (a única fonte testada com os dois antes de
  1960), cartões e público da Premier League 1992/93-2000/01; na Espanha, cartões antes de 2001/02 (o BDFutbol não tem)

### transfermarkt — Espanha, LaLiga (ES1), calendário da temporada
- endereço: https://www.transfermarkt.com/laliga/gesamtspielplan/wettbewerb/ES1/saison_id/1960
- cobre: data, hora (recente), placar e id da ficha (amostra 1929, 1932, 1946, 1955, 1960, 1977, 1988, 2000, 2003, 2004, 2011,
  2023)
- como baixar: em lote, 1 página por temporada
- amostra: usado como 3ª opinião nas 23 datas em que BDFutbol e pacote diferem: confirmou o pacote em 16, o BDFutbol em 3
  (Alavés x Betis 1932/33; Barcelona x Sevilla 2003/04, QE-003; Granada x Athletic 2023/24, data de início, QE-004), as duas
  datas em 1 (Real Madrid x Real Sociedad 2004/05) e não achou o jogo em 3
- serve a: coleta-europa; buscar: 3ª opinião de data; id da ficha

### 11v11 — ficha do jogo (já usado pela 2ª rodada para tabelas e datas, não para fichas)
- endereço: https://www.11v11.com/matches/huddersfield-town-v-west-bromwich-albion-29-august-1925-63155/
- cobre: placar, estádio e **público** de jogos antigos (1925: 21.975); os autores não aparecem na página
- como baixar: jogo a jogo
- amostra: 1 ficha (1925); páginas de jogos por clube (2 de 2 confirmaram as datas de 1935/36 e 1953/54)
- serve a: coleta-europa; buscar: público e estádio do Inglês antes de 1960 (alternativa ao transfermarkt)

### Wikipédia en — biografias de jogadores
- endereço: https://en.wikipedia.org/wiki/Albert_Shepherd_(footballer)
- cobre: gols por temporada de alguns jogadores
- como baixar: 1 página por jogador (a API deu 429 várias vezes em 22/11: há muitos revisores)
- amostra: EN-004: a biografia dá Shepherd **25** gols e artilheiro em 1905/06 (cita The History of the English Football
  League); a de Walter White só dá 88 gols pelo Bolton em 1902-08
- serve a: coleta-europa; buscar: desempate de artilheiros quando as listas divergem

### Testadas e descartadas
- **statto.com**: só a Premier League de 1992/93 a 2016/17 (site parado); `.../premier-league/1960-1961/results` dá 404.
- **myfootballfacts.com**: textos e listas da Premier League; sem jogos antigos.
- **englandfootballonline.com**: não respondeu (seleção inglesa, de todo jeito).
- **transfermarkt GB1 antes de 1992**: devolve a temporada atual (usar EFD1).
- **bdfutbol, público**: não há campo de público nas fichas (nem antigas nem recentes).
- **footballdatabase.eu**: não testado (limite diário do IP já esgotado em 22/11).
