# Fontes avaliadas — Campeonato Alemão (`ger-1`), revisão de 22/11/2026

### Wikipédia de (página de cada temporada)
- endereço: https://de.wikipedia.org/wiki/Fußball-Bundesliga_1971/72 (1999/2000 tem o ano inteiro no título);
  wikitexto por `index.php?title=...&action=raw`.
- cobre, nas 63 temporadas:
  - Abschlusstabelle (V-E-D, gols, `Abzug` = pontos tirados, `Rang2` = posição dividida);
  - Farblegende (quem caiu e por quê);
  - Kreuztabelle (placar de todos os jogos);
  - seção Relegation;
  - notas (FNZ) com jogos abandonados, decididos no tribunal e repetidos;
  - Torschützenliste.
- como baixar: em lote, uma página por temporada (63 páginas); wikitexto.
- amostra:
  - placares: 17.962 de 17.962 iguais. A Kreuztabelle foi lida em 59 temporadas; 4 têm o modelo diferente;
  - tabelas: 1.129 de 1.131 linhas iguais. As 2 diferenças são achados (DE-001 Arminia 1971/72; DE-013 3º dividido
    em 1979/80);
  - campeões: 63 de 63;
  - rebaixados: certos nas 63 temporadas. Nas antigas, conferidos pela legenda "Abstieg"; nas recentes, pelas seções
    Relegation e Farbe, à mão.
- serve a: coleta-europa.
- buscar: punições (`Abzug`), notas de tribunal ("gewertet"), Relegation e jogos repetidos.
- Scripts: `revisao/DE/dewiki.py` e `revisao/DE/cmp_dewiki.py`.

### Wikipédia de — Liste der Torschützenkönige der Fußball-Bundesliga
- endereço: https://de.wikipedia.org/wiki/Liste_der_Torschützenkönige_der_Fußball-Bundesliga
- cobre: artilheiro(s) de 1963/64 a 2025/26, com clube e gols.
- como baixar: em lote, 1 página.
- amostra: 63 de 63 temporadas batem em gols e clube. Os nomes do pacote vêm no formato da RSSSF em 8 delas (DE-008).
- serve a: coleta-europa.
- buscar: o nome curto do artilheiro.

### transfermarkt — gesamtspielplan (calendário da temporada)
- endereço: https://www.transfermarkt.com/bundesliga/gesamtspielplan/wettbewerb/L1/saison_id/1972
- cobre: data (e hora nas recentes) e placar oficial de todos os jogos, de 1963/64 a 2025/26.
- como baixar: em lote, 1 página por temporada (63 páginas, ~700 KB cada); HTML (linhas `<tr>`, data em
  `datum/AAAA-MM-DD`, placar em `ergebnis-link`).
- amostra:
  - 19.220 de 19.220 jogos casados e 19.220 placares iguais;
  - 116 datas diferentes, todas de 1963/64 a 1996/97;
  - 102 dessas datas o transfermarkt acerta (com a RSSSF ou o ogol);
  - 11 ele erra (a RSSSF fica com o pacote) e 3 ficam em dúvida.
- serve a: coleta-europa.
- buscar: data de cada jogo (DE-003); dá para trocar a base de datas de 1963/64 a 1992/93.
- Script: `revisao/DE/cmp_tm.py`. Respondeu a 63 pedidos seguidos a cada 2 s, sem bloqueio.

### transfermarkt — spielbericht (ficha do jogo)
- endereço: https://www.transfermarkt.com/1-fc-union-berlin_vfl-bochum/index/spielbericht/4373534
- cobre:
  - autor e minuto de cada gol, com assistência;
  - escalações, cartões e árbitro (não conferido a fundo).
  - Tem até os jogos de 1972/73 (ex.: `/rot-weiss-oberhausen_fc-bayern-munich/index/spielbericht/9814`).
- como baixar: jogo a jogo. O id está no link `ergebnis-link` do gesamtspielplan.
- amostra: 2 fichas abertas (2024/25 e 1972/73), com os gols certos.
- serve a: coleta-europa.
- buscar:
  - os 36 jogos sem autor (DE-010);
  - autores de 1999/00 e 2000/01 (DE-011).

### RSSSF — página de cada temporada (tablesd/duitNN.html)
- endereço: https://www.rsssf.org/tablesd/duit75.html. A coleta já tem todas em `data/coleta/ger-1/rsssf/`, mas leu só a
  tabela final.
- cobre:
  - de 1963/64 a 1998/99: jogo a jogo, rodada com data ("Round 19 [Feb 1]") e subdatas ("[Oct 1]"), autores dos gols
    com minuto, pênalti ("p"), gol contra ("o") e pênaltis perdidos ("m/pen");
  - de 1999/00 em diante: páginas de várias divisões e sem autores.
- como baixar: em lote (já baixado); texto pré-formatado.
- amostra:
  - 10.341 jogos casados (1963/64–1998/99);
  - placares: 0 diferenças reais. As 4 que apareceram são casamento errado do meu leitor ou o placar de campo de um
    jogo decidido no tribunal (1992/93 Uerdingen x Frankfurt 2-5; DE-005);
  - datas: concorda com o transfermarkt em 101 das 102 correções;
  - autores: o leitor simples fecha a soma com o placar em 7.678 de 9.660 jogos com gol.
- serve a: coleta-europa.
- buscar: autores dos gols de 1963/64 a 1998/99 (DE-011) e conferência de datas.
- Script: `revisao/DE/cmp_rsssf_datas.py`.

### RSSSF — campeões e período de antes da Bundesliga
- endereço: https://www.rsssf.org/tablesd/duitchamp.html
- cobre:
  - finais de 1902/03 a 1962/63 e lista dos campeões da Bundesliga;
  - índice para "Germany - Championships 1902-1945 / 1947-1963", Oberligas 1945–1963 (Berlin, Nord, Süd, Südwest,
    West) e Regionalligas 1963–1974 (2º nível).
- como baixar: em lote, uma página por período.
- amostra: os campeões da Bundesliga de 1963/64 a 1990/91 conferidos visualmente batem com o pacote.
- serve a: coleta-europa.
- buscar: fase final de 1902/03 a 1962/63 (DE-D1, opção B); Oberligas (opção C); Regionalligas para um futuro `ger-2`.

### RSSSF — DDR-Oberliga (tablesd/ddrNN.html)
- endereço: https://www.rsssf.org/tablesd/ddr72.html (= 1971/72)
- cobre: DDR-Oberliga jogo a jogo, com a data de cada rodada.
- como baixar: em lote, uma página por temporada (1949/50–1990/91).
- amostra: 1 página aberta (1971/72), com rodadas, datas e placares.
- serve a: coleta-europa.
- buscar: competição à parte `gdr-1` (DE-D1, opção D).

### Wikipédia de — Deutsche Fußballmeisterschaft (por ano) e Liste der deutschen Fußballmeister
- endereço:
  - https://de.wikipedia.org/wiki/Deutsche_Fußballmeisterschaft_1955/56
  - https://de.wikipedia.org/wiki/Liste_der_deutschen_Fußballmeister
- cobre: fase final de cada ano (participantes, eliminatórias, grupos, final, artilheiro) e campeão, vice, 3º e 4º desde
  1903.
- como baixar: em lote, uma página por ano.
- amostra: 1955/56 aberta: 8 clubes (12 com as eliminatórias), 25 jogos, 102 gols.
- serve a: coleta-europa.
- buscar: DE-D1, opção B.

### footballdatabase.eu
- endereço:
  - página de rodada: https://www.footballdatabase.eu/en/competition/overall/226-bundesliga/1972-1973/7456-journee_34;
  - a temporada tem um id próprio, listado no seletor da página
    https://www.footballdatabase.eu/en/competition/overall/23394-bundesliga/2026-2027.
- cobre: data, placar, autores dos gols e minuto, de 1963/64 em diante. O seletor lista também a Oberliga de 1945/46 a
  1962/63.
- como baixar: por rodada (34 páginas por temporada); HTML.
- amostra:
  - 236 de 238 jogos iguais em data e placar (10 temporadas de 1963/64 a 1996/97);
  - as 2 diferenças são erros dela: 1972/73 Werder x M'gladbach e 1977/78 1860 x Stuttgart. A data do pacote é a do
    transfermarkt e da RSSSF;
  - pior: ela repete as datas erradas da base. Em 1977/78 (rodada 10) e 1982/83 (rodada 8) ela "bate" com o pacote em
    jogos que o transfermarkt e a RSSSF põem um mês depois. Então não é independente para datas.
- serve a: coleta-europa, só para autores dos gols e como terceira opinião de placar, não de data.
- buscar: autores dos gols antigos, se a RSSSF falhar.
- **Bloqueia** depois de ~40 páginas seguidas, com a página "Adblocker detected" (HTTP 200, sem os jogos). Use ≥10 s
  entre pedidos e confira se a página tem `/en/match/overview`.

### football-data.co.uk
- endereço: https://www.football-data.co.uk/mmz4281/9394/D1.csv
- cobre: placar desde 1993/94; data; hora, árbitro e estatísticas nas recentes.
- como baixar: em lote, 1 CSV por temporada (a coleta já tem).
- amostra: 10.098 jogos. Placar: 0 diferenças. Datas: 152 diferenças, 117 delas em 1993/94. De 1993/94 a 1996/97 a data
  é a da rodada (o sábado), não a do jogo; o transfermarkt confirma o pacote.
- serve a: coleta-europa.
- buscar: nada novo; **não usar para datas antes de 1997/98** (DE-017).

### 11v11
- endereço: https://www.11v11.com/teams/bayern-munich/tab/matches/season/1972/
- cobre: não tem a Bundesliga (404 nas páginas de clube alemão; a lista de competições não traz a Alemanha).
- como baixar: —
- amostra: 0.
- serve a: ninguém, para a Alemanha.

### dfb.de
- endereço: https://www.dfb.de/bundesliga/spieltagtabelle/
- cobre: responde (200), mas a página é montada no navegador e o HTML baixado não traz os jogos de temporadas antigas.
- como baixar: não deu por curl.
- amostra: 0.
- serve a: banco-painel (só referência oficial manual).

### kicker, fussballdaten, weltfussball
- Bloqueiam (403), segundo o briefing. Não testei, para não insistir.
