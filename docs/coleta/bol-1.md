# Campeonato Boliviano (1ª divisão) — coleta de dados

Gerado por `python coleta/bol-1/importar.py`. Pacote em `data/coleta/bol-1/pacote/`.

**Edições:** 94, uma por título de 1950 a 2025, como na lista de campeões da Wikipédia em inglês (página "FBF División Profesional") e na contagem de 93 campeonatos da RSSSF (`bolchamp.html`), mais o Clausura 2022, abandonado (edição sem campeão). Liga de La Paz semiprofissional (1950-1953), Torneo Integrado (1954-1957), Certamen Nacional Mixto (1957/58, edição "1957 Mixto"), campeonato nacional (1958-1976; Copa Simón Bolívar de 1960 a 1976; sem campeonato em 1962) e liga profissional (1977 em diante). Até 2002, Apertura e Clausura são fases do ano; de 2003 a 2019 e em 2022, cada torneio que dá título é uma edição (2005 Apertura é o Apertura 2005/06, abortado; 2011/12 e 2016/17 no calendário europeu).

**Fora do pacote:** a liga amadora de La Paz (1914-1949), os campeonatos regionais que serviam de classificatória do nacional (1960-1976), a Copa Simón Bolívar de 2ª divisão (1977 em diante), a Nacional B, as copas (Copa Bolivia, Copa de la División Profesional, Copa Paceña), os playoffs da Libertadores e da Sudamericana e os jogos de promoção.

**Edições sem jogos (22):** 1952, 1954-1959 (com o 1957 Mixto), 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981 e 1984. Pesquisamos RSSSF (só tabelas finais, em `bolhist.html`), Wikipédia em espanhol e inglês e ogol (sem jogos bolivianos antigos): nenhuma fonte pública traz os jogos. Entram com o campeão, o vice e a tabela final da RSSSF quando há (não há tabela do nacional de 1960 a 1964).

**Edições com jogos incompletos:** 1951, 1960, 1966, 1968, 1971, 1976, 1978, 1979, 1982, 1983 e 1985-1989 (só as fases finais, da Wikipédia em espanhol ou da RSSSF), 1990 e 1991 (jogos da Wikipédia sem a divisão em fases das tabelas da RSSSF) e 1992-1994 (a RSSSF tem só as tabelas da maior parte das fases). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.

**Fontes:** RSSSF (uma página por temporada de 1971, 1977 e 1990 em diante, e a lista de tabelas finais `bolhist.html` de 1950 a 1990, em `data/coleta/bol-1/rsssf/`: base de jogos de 1977 e 1992 em diante, com fases, grupos, rodadas, datas e autores dos gols); Wikipédia em espanhol (jogos de 1950, 1953, 1990 e 1991 e das fases finais de outros anos; em `data/coleta/bol-1/wikipedia/`); ESPN (liga `bol.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões: segunda fonte do campeão, fonte do vice de 1977 em diante e dos artilheiros fora da lista da RSSSF, que vai de 1977 a 2005).

**Clubes:** nome pelo qual o clube é conhecido (Bolívar, The Strongest, Jorge Wilstermann, Oriente Petrolero). Homônimos levam a cidade: os Universitarios (de La Paz, Sucre, Potosí, Beni, Pando e Vinto), Ferroviario de La Paz, Municipal de La Paz, Internacional de Oruro (1957) e de La Paz (1958-1960), Litoral de La Paz e de Cochabamba, Petrolero de Cochabamba e de Yacuiba, Primero de Mayo de La Paz e de Potosí. O mesmo clube com outro nome fica com o atual: Deportivo Chaco = Chaco Petrolero; Universidad Iberoamericana = Iberoamericana; CDT Real Oruro = Real Oruro; Atlético Palmaflor = Palmaflor.

**Regras:** o placar é o da fonte de base (RSSSF ou Wikipédia). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação; "awarded to X (originally 0-0)" vira vitória de X com os gols do campo, como a tabela conta. Ida e volta numa linha só ("A 1-0 0-4 B") vira dois jogos, com os gols de A primeiro e o mando da volta presumido. Pontos: 2 por vitória até 1994 e 3 a partir de 1995. Nas edições sem jogos, campeão e vice da lista ficam em 1º e 2º mesmo quando não estão na tabela usada (sem a campanha).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1950 | 9 | 73 (73) | 327 | 0 | 0 / 1 | Bolívar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1951 | 8 | 3 (3) | 15 | 0 | 0 / 0 | Always Ready | RSSSF (bolhist) |
| 1952 | 8 | 0 (0) | 0 | 0 | 0 / 0 | The Strongest | RSSSF (bolhist) |
| 1953 | 8 | 56 (56) | 219 | 0 | 0 / 1 | Bolívar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1954 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Litoral de La Paz | RSSSF (bolhist) |
| 1955 | 11 | 0 (0) | 0 | 0 | 0 / 0 | San José | RSSSF (bolhist) |
| 1956 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1957 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Always Ready | RSSSF (bolhist) |
| 1957 Mixto | 7 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1958 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1959 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1960 | 8 | 24 (24) | 91 | 0 | 0 / 0 | Jorge Wilstermann | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1961 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Municipal de La Paz | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1963 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Aurora | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1964 | 0 | 0 (0) | 0 | 0 | 0 / 0 | The Strongest | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1965 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Municipal de La Paz | RSSSF (bolhist) |
| 1966 | 4 | 12 (12) | 30 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1967 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1968 | 6 | 30 (30) | 87 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1969 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Universitario de La Paz | RSSSF (bolhist) |
| 1970 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Chaco Petrolero | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1971 | 13 | 12 (12) | 33 | 3 | 0 / 0 | Oriente Petrolero | RSSSF (bol71) |
| 1972 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1973 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | lista de campeões (RSSSF e Wikipédia) |
| 1974 | 0 | 0 (0) | 0 | 0 | 0 / 0 | The Strongest | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1975 | 19 | 0 (0) | 0 | 0 | 0 / 0 | Guabirá | RSSSF (bolhist) |
| 1976 | 15 | 42 (42) | 149 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1977 | 16 | 167 (167) | 605 | 0 | 2 / 4 | The Strongest | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1978 | 16 | 13 (13) | 53 | 0 | 0 / 0 | Bolívar | lista de campeões (RSSSF e Wikipédia) |
| 1979 | 17 | 3 (3) | 7 | 0 | 0 / 0 | Oriente Petrolero | RSSSF (bolhist) |
| 1980 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1981 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Wilstermann | RSSSF (bolhist) |
| 1982 | 14 | 4 (4) | 11 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1983 | 14 | 9 (9) | 31 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1984 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Blooming | RSSSF (bolhist) |
| 1985 | 15 | 3 (3) | 11 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1986 | 15 | 3 (3) | 10 | 0 | 0 / 0 | The Strongest | RSSSF (bolhist) |
| 1987 | 14 | 3 (3) | 16 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1988 | 13 | 1 (1) | 3 | 0 | 0 / 0 | Bolívar | RSSSF (bolhist) |
| 1989 | 12 | 4 (4) | 4 | 0 | 0 / 0 | The Strongest | RSSSF (bolhist) |
| 1990 | 13 | 168 (168) | 451 | 0 | 0 / 0 | Oriente Petrolero | RSSSF (bol90) |
| 1991 | 14 | 91 (91) | 232 | 0 | 0 / 0 | Bolívar | RSSSF (bol91) |
| 1992 | 16 | 8 (8) | 27 | 0 | 0 / 0 | Bolívar | RSSSF (bol92) |
| 1993 | 15 | 112 (112) | 362 | 0 | 0 / 0 | The Strongest | RSSSF (bol93) |
| 1994 | 13 | 9 (9) | 30 | 0 | 0 / 0 | Bolívar | RSSSF (bol94) |
| 1995 | 12 | 174 (174) | 461 | 0 | 3 / 1 | San José | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996 | 12 | 194 (194) | 604 | 0 | 2 / 3 | Bolívar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 | 12 | 168 (168) | 521 | 65 | 4 / 1 | Bolívar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 | 12 | 236 (236) | 694 | 1 | 1 / 4 | Blooming | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 | 12 | 236 (236) | 750 | 366 | 3 / 2 | Blooming | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 | 12 | 267 (267) | 848 | 574 | 3 / 0 | Jorge Wilstermann | RSSSF (bol00) |
| 2001 | 12 | 244 (244) | 805 | 516 | 5 / 2 | Oriente Petrolero | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 | 12 | 268 (268) | 913 | 415 | 1 / 2 | Bolívar | RSSSF (bol02) |
| 2003 Apertura | 12 | 132 (132) | 433 | 220 | 1 / 0 | The Strongest | RSSSF (bol03) |
| 2003 Clausura | 12 | 108 (108) | 318 | 164 | 5 / 0 | The Strongest | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Apertura | 12 | 132 (132) | 424 | 157 | 1 / 0 | Bolívar | RSSSF (bol04) |
| 2004 Clausura | 12 | 119 (119) | 370 | 159 | 3 / 0 | The Strongest | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Adecuación | 12 | 132 (132) | 411 | 164 | 1 / 0 | Bolívar | RSSSF (bol05) |
| 2005 Apertura | 12 | 102 (102) | 336 | 330 | 3 / 0 | Blooming | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Apertura | 12 | 132 (132) | 406 | 402 | 1 / 0 | Bolívar | RSSSF (bol06) |
| 2006 Clausura | 12 | 102 (102) | 275 | 275 | 3 / 0 | Jorge Wilstermann | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Apertura | 12 | 132 (132) | 404 | 390 | 1 / 0 | Real Potosí | RSSSF (bol07) |
| 2007 Clausura | 12 | 104 (104) | 290 | 270 | 3 / 0 | San José | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Apertura | 12 | 132 (132) | 456 | 414 | 1 / 0 | Universitario de Sucre | RSSSF (bol08) |
| 2008 Clausura | 12 | 67 (67) | 183 | 180 | 2 / 0 | Aurora | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 12 | 132 (132) | 412 | 394 | 1 / 0 | Bolívar | RSSSF (bol09) |
| 2009 Clausura | 12 | 84 (84) | 221 | 221 | 2 / 0 | Blooming | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Apertura | 12 | 132 (132) | 404 | 248 | 4 / 0 | Jorge Wilstermann | RSSSF (bol2010) |
| 2010 Clausura | 12 | 132 (132) | 377 | 362 | 1 / 0 | Oriente Petrolero | RSSSF (bol2010) |
| 2011/12 Adecuación | 12 | 132 (132) | 370 | 278 | 1 / 0 | Bolívar | RSSSF (bol2012) |
| 2011/12 Apertura | 12 | 88 (88) | 268 | 263 | 2 / 0 | The Strongest | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011/12 Clausura | 12 | 132 (132) | 397 | 394 | 1 / 0 | The Strongest | RSSSF (bol2012) |
| 2012/13 Apertura | 12 | 132 (132) | 408 | 230 | 1 / 0 | The Strongest | RSSSF (bol2013) |
| 2012/13 Clausura | 12 | 132 (132) | 403 | 370 | 1 / 0 | Bolívar | RSSSF (bol2013) |
| 2013/14 Apertura | 12 | 132 (132) | 399 | 382 | 1 / 0 | The Strongest | RSSSF (bol2014) |
| 2013/14 Clausura | 12 | 132 (132) | 401 | 209 | 1 / 0 | Universitario de Sucre | RSSSF (bol2014) |
| 2014/15 Apertura | 12 | 132 (132) | 361 | 227 | 1 / 0 | Bolívar | RSSSF (bol2015) |
| 2014/15 Clausura | 12 | 132 (132) | 360 | 210 | 1 / 0 | Bolívar | RSSSF (bol2015) |
| 2015/16 Apertura | 12 | 132 (132) | 426 | 224 | 1 / 0 | Sport Boys Warnes | RSSSF (bol2016) |
| 2015/16 Clausura | 12 | 132 (132) | 379 | 212 | 1 / 0 | Jorge Wilstermann | RSSSF (bol2016) |
| 2016/17 Apertura | 12 | 133 (133) | 374 | 248 | 1 / 0 | The Strongest | RSSSF (bol2017) |
| 2016/17 Adecuación | 12 | 132 (132) | 453 | 190 | 1 / 0 | Bolívar | RSSSF (bol2017) |
| 2016/17 Clausura | 12 | 132 (132) | 347 | 224 | 1 / 0 | Bolívar | RSSSF (bol2017) |
| 2018 Apertura | 14 | 115 (115) | 368 | 173 | 2 / 0 | Jorge Wilstermann | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2018 Clausura | 14 | 182 (182) | 589 | 268 | 1 / 0 | San José | RSSSF (bol2018) |
| 2019 Apertura | 14 | 182 (182) | 608 | 283 | 1 / 0 | Bolívar | RSSSF (bol2019) |
| 2019 Clausura | 14 | 182 (181) | 600 | 284 | 1 / 0 | Jorge Wilstermann | RSSSF (bol2019) |
| 2020 | 14 | 182 (182) | 567 | 291 | 1 / 0 | Always Ready | RSSSF (bol2020) |
| 2021 | 16 | 240 (240) | 735 | 462 | 1 / 0 | Independiente Petrolero | RSSSF (bol2021) |
| 2022 Apertura | 16 | 141 (141) | 395 | 220 | 2 / 0 | Bolívar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 Clausura | 16 | 192 (192) | 537 | 342 | 1 / 0 | None | RSSSF (bol2022) |
| 2023 | 17 | 272 (272) | 750 | 434 | 1 / 0 | The Strongest | RSSSF (bol2023) |
| 2024 | 16 | 319 (319) | 950 | 581 | 5 / 0 | Bolívar | RSSSF (bol2024) |
| 2025 | 16 | 240 (240) | 869 | 377 | 1 / 0 | Always Ready | RSSSF (bol2025) |

## Conferência e correções, edição a edição

### 1950

- os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols de quatro clubes diferem em um ou dois
- tabela publicada x jogos — bolhist:17: Bolívar tabela [16, 8, 5, 3, 40, 32] jogos [16, 8, 5, 3, 40, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Litoral de La Paz tabela [16, 8, 5, 3, 48, 31] jogos [16, 8, 5, 3, 50, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Unión Maestranza tabela [16, 8, 3, 5, 41, 26] jogos [16, 7, 4, 5, 42, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Ferroviario de La Paz tabela [16, 6, 3, 7, 32, 30] jogos [16, 6, 3, 7, 33, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: The Strongest tabela [16, 5, 5, 6, 29, 40] jogos [16, 6, 5, 5, 36, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Always Ready tabela [16, 4, 5, 7, 29, 36] jogos [16, 4, 4, 8, 29, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Ingavi tabela [16, 5, 2, 9, 33, 46] jogos [16, 5, 2, 9, 38, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:17: Northern tabela [16, 3, 5, 8, 24, 38] jogos [16, 3, 5, 8, 29, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1951

- sem ocorrências

### 1952

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1953

- os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols do Ferroviario diferem (a Wikipédia tem um placar diferente num jogo dele)
- tabela publicada x jogos — bolhist:70: Ferroviario de La Paz tabela [14, 5, 3, 6, 32, 28] jogos [14, 4, 5, 5, 22, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:70: Litoral de La Paz tabela [14, 5, 2, 7, 21, 22] jogos [14, 5, 2, 7, 20, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bolhist:70: The Strongest tabela [14, 3, 4, 7, 26, 38] jogos [14, 3, 4, 7, 26, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1954

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1955

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1956

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1957

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1957 Mixto

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1958

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1959

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1960

- sem ocorrências

### 1961

- a lista de campeões da RSSSF dá o vice Aurora e a da Wikipédia em inglês, o The Strongest; fica o da RSSSF (fonte de base)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1963

- a lista de campeões da RSSSF dá o vice Deportivo Municipal e a da Wikipédia em inglês, o Jorge Wilstermann; fica o da RSSSF (fonte de base)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1964

- a lista de campeões da RSSSF dá o vice Aurora e a da Wikipédia em inglês, o Deportivo Municipal; fica o da RSSSF (fonte de base)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1965

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1966

- sem ocorrências

### 1967

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1968

- a lista de campeões da RSSSF dá o vice Guabirá e a da Wikipédia em inglês, o Litoral de Cochabamba; fica o da RSSSF (fonte de base; a tabela final da RSSSF também põe o Guabirá em 2º)

### 1969

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1970

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1971

- sem ocorrências

### 1972

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1973

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1974

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1975

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1976

- sem ocorrências

### 1977

- tabela publicada x jogos — bol77:215: Guabirá tabela [14, 5, 5, 4, 29, 25] jogos [14, 5, 4, 5, 28, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bol77:215: Stormers tabela [14, 0, 4, 10, 13, 41] jogos [14, 1, 3, 10, 13, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — bol77:226: Jorge Wilstermann tabela [14, 6, 4, 4, 29, 25] jogos [14, 6, 4, 4, 30, 27] — a outra tabela publicada (bol77) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol77:305: Bolívar tabela [8, 5, 1, 2, 17, 13] jogos [7, 5, 0, 2, 16, 12] — a outra tabela publicada (bol77) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol77:305: San José tabela [8, 4, 1, 3, 15, 16] jogos [7, 4, 0, 3, 14, 15] — a outra tabela publicada (bol77) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol77:313: Jorge Wilstermann tabela [8, 4, 2, 2, 14, 10] jogos [8, 4, 2, 2, 14, 11] — a outra tabela publicada (bol77) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol77:313: Petrolero de Cochabamba tabela [8, 1, 4, 3, 8, 10] jogos [8, 1, 4, 3, 9, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1981

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1982

- sem ocorrências

### 1983

- sem ocorrências

### 1984

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)

### 1985

- sem ocorrências

### 1986

- sem ocorrências

### 1987

- sem ocorrências

### 1988

- sem ocorrências

### 1989

- sem ocorrências

### 1990

- sem ocorrências

### 1991

- sem ocorrências

### 1992

- sem ocorrências

### 1993

- sem ocorrências

### 1994

- sem ocorrências

### 1995

- tabela publicada x jogos — bol95:303: The Strongest tabela [14, 4, 5, 5, 19, 17] jogos [13, 4, 5, 4, 18, 15] — a outra tabela publicada (bol95) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol95:303: Independiente Petrolero tabela [14, 3, 6, 5, 17, 26] jogos [13, 2, 6, 5, 15, 25] — a outra tabela publicada (bol95) fecha com os jogos: o erro é desta tabela

### 1996

- tabela publicada x jogos — bol96:18: Jorge Wilstermann tabela [14, 4, 6, 4, 21, 20] jogos [15, 3, 7, 5, 21, 23] — a outra tabela publicada (bol96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol96:18: Independiente Petrolero tabela [14, 2, 4, 8, 15, 29] jogos [13, 2, 5, 6, 15, 26] — a outra tabela publicada (bol96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol96:27: San José tabela [14, 6, 5, 3, 24, 18] jogos [14, 7, 4, 3, 24, 18] — a outra tabela publicada (bol96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol96:27: Stormers tabela [14, 3, 5, 6, 21, 30] jogos [14, 3, 4, 7, 21, 30] — a outra tabela publicada (bol96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol96:306: San José tabela [12, 5, 4, 3, 24, 12] jogos [12, 5, 4, 3, 25, 13] — a outra tabela publicada (bol96) fecha com os jogos: o erro é desta tabela

### 1997

- tabela publicada x jogos — bol97:259: The Strongest tabela [12, 5, 5, 2, 23, 13] jogos [12, 6, 5, 1, 23, 13] — a outra tabela publicada (bol97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol97:259: Jorge Wilstermann tabela [12, 4, 5, 3, 16, 16] jogos [12, 4, 5, 3, 16, 15] — a outra tabela publicada (bol97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol97:259: Guabirá tabela [12, 3, 5, 4, 15, 19] jogos [12, 2, 5, 5, 15, 19] — a outra tabela publicada (bol97) fecha com os jogos: o erro é desta tabela

### 1998

- tabela publicada x jogos — bol98:16: San José tabela [22, 9, 7, 6, 27, 26] jogos [22, 9, 7, 6, 29, 26] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:392: San José tabela [12, 5, 2, 5, 23, 20] jogos [12, 5, 2, 5, 23, 19] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:392: Oriente Petrolero tabela [12, 4, 4, 4, 19, 18] jogos [13, 4, 5, 4, 20, 19] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — bol98:403: Blooming tabela [12, 7, 5, 0, 24, 10] jogos [11, 7, 4, 0, 23, 9] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:403: Jorge Wilstermann tabela [12, 6, 2, 4, 16, 15] jogos [12, 6, 2, 4, 15, 15] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:620: Jorge Wilstermann tabela [34, 19, 8, 7, 44, 26] jogos [34, 19, 8, 7, 43, 26] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:620: Blooming tabela [34, 18, 9, 7, 60, 42] jogos [33, 18, 8, 7, 59, 41] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:620: San José tabela [34, 14, 9, 11, 52, 46] jogos [34, 14, 9, 11, 52, 45] — a outra tabela publicada (bol98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol98:620: Oriente Petrolero tabela [34, 14, 8, 12, 51, 51] jogos [35, 14, 9, 12, 52, 52] — sobram 1 jogo(s) do clube na página

### 1999

- tabela publicada x jogos — bol99:19: Real Santa Cruz tabela [22, 9, 4, 9, 35, 49] jogos [21, 8, 4, 9, 32, 44] — a outra tabela publicada (bol99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol99:19: Destroyers tabela [22, 5, 4, 13, 33, 56] jogos [21, 5, 4, 12, 28, 53] — a outra tabela publicada (bol99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol99:832: Real Santa Cruz tabela [34, 14, 5, 15, 47, 62] jogos [33, 13, 5, 15, 44, 57] — a outra tabela publicada (bol99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol99:832: Destroyers tabela [34, 6, 6, 22, 46, 93] jogos [33, 6, 6, 21, 41, 90] — a outra tabela publicada (bol99) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Real Santa Cruz Destroyers (1999-04-14): finished 3-5; points awarded to Santa Cruz
- W.O./pontos para o mandante — Real Santa Cruz 0-0 Bolívar (1999-08-08): awarded to Santa Cruz (originally 0-0)
- W.O./pontos para o mandante — Guabirá 1-1 The Strongest (1999-08-15): awarded to Gaubira (originally 1-1)

### 2000

- sem ocorrências

### 2001

- tabela publicada x jogos — bol01:17: Oriente Petrolero tabela [22, 13, 3, 6, 48, 31] jogos [21, 12, 3, 6, 45, 30] — a outra tabela publicada (bol01) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol01:17: Iberoamericana tabela [22, 5, 5, 12, 37, 47] jogos [21, 5, 5, 11, 36, 44] — a outra tabela publicada (bol01) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol01:641: Oriente Petrolero tabela [34, 17, 7, 10, 70, 47] jogos [33, 16, 7, 10, 67, 46] — a outra tabela publicada (bol01) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol01:641: Iberoamericana tabela [34, 9, 8, 17, 59, 70] jogos [33, 9, 8, 16, 58, 67] — a outra tabela publicada (bol01) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Oriente Petrolero 3-1 Iberoamericana (2001-06-13): Iberoamericana have appealed as Oriente fielded Ronald Arana who is suspended

### 2002

- tabela publicada x jogos — bol02:396: Blooming tabela [22, 10, 2, 10, 40, 53] jogos [21, 10, 2, 9, 40, 53] — a outra tabela publicada (bol02) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol02:396: Mariscal Braun tabela [22, 5, 3, 14, 21, 44] jogos [21, 4, 3, 14, 21, 44] — a outra tabela publicada (bol02) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol02:771: Blooming tabela [44, 22, 3, 19, 83, 98] jogos [43, 22, 3, 18, 83, 98] — a outra tabela publicada (bol02) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — bol02:771: Mariscal Braun tabela [44, 8, 6, 30, 38, 92] jogos [43, 7, 6, 30, 38, 92] — a outra tabela publicada (bol02) fecha com os jogos: o erro é desta tabela
- não jogado — Bolívar Jorge Wilstermann (2002-10-02): not played due to strike Wilstermann players
- decidido fora de campo — Mariscal Braun Blooming (2002-11-24)

### 2003 Apertura

- corrigido — Independiente Petrolero x Bolívar (2003-05-18): jogo interrompido por temporal no intervalo (1-2) e completado depois (linha 233, "[remaining 45']", 2-3): fica a segunda

### 2003 Clausura

- decidido fora de campo — Guabirá Independiente Petrolero (2003-10-26): awarded 2-0; abandoned in 55' at 1-0 when Independiente walked off;

### 2004 Apertura

- sem ocorrências

### 2004 Clausura

- sem ocorrências

### 2005 Adecuación

- sem ocorrências

### 2005 Apertura

- ESPN: 100 jogos casados

### 2006 Apertura

- ESPN: 132 jogos casados

### 2006 Clausura

- ESPN: 102 jogos casados

### 2007 Apertura

- ESPN: 132 jogos casados

### 2007 Clausura

- ESPN: 100 jogos casados

### 2008 Apertura

- ESPN: 121 jogos casados

### 2008 Clausura

- ESPN: 66 jogos casados

### 2009 Apertura

- ESPN: 132 jogos casados

### 2009 Clausura

- ESPN: 84 jogos casados

### 2010 Apertura

- ESPN: 72 jogos casados

### 2010 Clausura

- ESPN: 130 jogos casados

### 2011/12 Adecuación

- ESPN: 17 jogos casados

### 2011/12 Apertura

- ESPN: 85 jogos casados

### 2011/12 Clausura

- ESPN: 131 jogos casados
- decidido fora de campo — Universitario de Sucre Bolívar (2012-05-10): awarded 3-0; abandoned at 1-0 in 7' as Bolívar had shown

### 2012/13 Apertura

- sem ocorrências

### 2012/13 Clausura

- ESPN: 110 jogos casados

### 2013/14 Apertura

- ESPN: 132 jogos casados

### 2013/14 Clausura

- ESPN: 130 jogos casados

### 2014/15 Apertura

- ESPN: 131 jogos casados

### 2014/15 Clausura

- ESPN: 132 jogos casados
- decidido fora de campo — Bolívar Universitario de Sucre (2015-04-11): awarded 3-0; abandoned at 2-0 when Universitario

### 2015/16 Apertura

- ESPN: 132 jogos casados

### 2015/16 Clausura

- ESPN: 132 jogos casados

### 2016/17 Apertura

- ESPN: 132 jogos casados

### 2016/17 Adecuación

- ESPN: 132 jogos casados

### 2016/17 Clausura

- ESPN: 16 jogos casados

### 2018 Apertura

- ESPN: 114 jogos casados

### 2018 Clausura

- ESPN: 182 jogos casados

### 2019 Apertura

- ESPN: 182 jogos casados

### 2019 Clausura

- ESPN: 181 jogos casados
- decidido fora de campo — Bolívar Aurora (2019-12-15): awarded 5-0; abandoned at 5-0 at start second
- não jogado — Real Potosí Sport Boys Warnes (2019-12-28): Sport Boys dns

### 2020

- ESPN: 182 jogos casados

### 2021

- ESPN: 239 jogos casados
- decidido fora de campo — The Strongest Royal Pari (2021-05-08): awarded 3-0; abandoned at 3-0 after 11'
- decidido fora de campo — San José Jorge Wilstermann (2021-12-11): awarded 0-3, San José suspended

### 2022 Apertura

- ESPN: 140 jogos casados

### 2022 Clausura

- abandonado (protestos no departamento de Santa Cruz): sem campeão
- ESPN: 192 jogos casados

### 2023

- ESPN: 272 jogos casados

### 2024

- ESPN: 319 jogos casados

### 2025

- ESPN: 240 jogos casados

