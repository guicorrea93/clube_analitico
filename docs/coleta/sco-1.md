# Campeonato Escocês (1ª divisão) — coleta de dados

Gerado por `python coleta/sco-1/importar.py`. Pacote em `data/coleta/sco-1/pacote/`.

**Edições:** 129, de 1890/91 a 2025/26: Scottish Football League e Division One (até 1974/75), Premier Division (1975/76-1997/98), Scottish Premier League (1998/99-2012/13) e Scottish Premiership. Sem 1939/40-1945/46 (guerra: o campeonato de 1939/40 parou na 5ª rodada e os seguintes foram ligas regionais não oficiais).

**Total:** 33076 jogos, 105133 gols, 14565 gols com autor (ESPN), 19812 cartões, 46 clubes.

**Fontes:**
- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; calendários guardados em `data/cache/ogol-sco-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);
- RSSSF: tabela final de 1890/91 a 1998/99 (scothist.html) e da página de cada temporada depois; lista de campeões e de artilheiros (com o clube);
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;
- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ESPN (liga `sco.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista oficial de rebaixados.

**Regras:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). O mesmo par se enfrenta 2, 3 ou 4 vezes por temporada: as outras fontes são casadas pelo par e pela data mais próxima. Desde 2000/01 a liga se divide em dois grupos de 6 depois da 33ª rodada; na classificação rodada a rodada, o grupo de cima fica nas 6 primeiras posições a partir da 34ª. Gols da ESPN só entram quando a soma bate com o placar. Hora local (Reino Unido). Rebaixado = clube que não está na 1ª divisão na temporada seguinte; até 1920/21 não havia rebaixamento (os últimos pediam reeleição à liga). 2 pontos por vitória até 1993/94, 3 a partir de 1994/95.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 58, saldo de gols em 54, média de gols em 11); é ele que ordena a classificação rodada a rodada.

| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1890/91 | ogol + RSSSF + Wikipédia | 10 | 90 | 409 | 0 | 1 / 1 | Dumbarton | Celtic -4 pontos; Third Lanark -4 pontos; Cowlairs -4 pontos |
| 1891/92 | ogol + RSSSF + Wikipédia | 12 | 132 | 593 | 0 | 1 / 1 | Dumbarton | — |
| 1892/93 | ogol + RSSSF + Wikipédia | 10 | 90 | 388 | 0 | 2 / 0 | Celtic | — |
| 1893/94 | ogol + RSSSF + Wikipédia | 10 | 90 | 421 | 0 | 2 / 0 | Celtic | — |
| 1894/95 | ogol + RSSSF + Wikipédia | 10 | 90 | 388 | 0 | 2 / 0 | Hearts | — |
| 1895/96 | ogol + RSSSF + Wikipédia | 10 | 90 | 469 | 0 | 2 / 0 | Celtic | — |
| 1896/97 | ogol + RSSSF + Wikipédia | 10 | 90 | 388 | 0 | 2 / 0 | Hearts | — |
| 1897/98 | ogol + RSSSF + Wikipédia | 10 | 90 | 414 | 0 | 2 / 0 | Celtic | — |
| 1898/99 | ogol + RSSSF + Wikipédia | 10 | 90 | 402 | 0 | 2 / 0 | Rangers | — |
| 1899/00 | ogol + RSSSF + Wikipédia | 10 | 90 | 379 | 0 | 1 / 1 | Rangers | — |
| 1900/01 | ogol + RSSSF + Wikipédia | 11 | 110 | 385 | 0 | 2 / 0 | Rangers | — |
| 1901/02 | ogol + RSSSF + Wikipédia | 10 | 90 | 286 | 0 | 1 / 1 | Rangers | — |
| 1902/03 | ogol + RSSSF + Wikipédia | 12 | 132 | 429 | 0 | 1 / 1 | Hibernian | — |
| 1903/04 | ogol + RSSSF + Wikipédia | 14 | 182 | 624 | 0 | 0 / 2 | Third Lanark | — |
| 1904/05 | ogol + RSSSF + Wikipédia | 14 | 182 | 580 | 0 | 0 / 2 | Celtic | — |
| 1905/06 | ogol + RSSSF + Wikipédia | 16 | 240 | 773 | 0 | 1 / 1 | Celtic | — |
| 1906/07 | ogol + RSSSF + Wikipédia | 18 | 306 | 909 | 0 | 1 / 1 | Celtic | — |
| 1907/08 | ogol + RSSSF + Wikipédia | 18 | 306 | 1006 | 0 | 0 / 2 | Celtic | — |
| 1908/09 | ogol + RSSSF + Wikipédia | 18 | 306 | 976 | 0 | 1 / 1 | Celtic | — |
| 1909/10 | ogol + RSSSF + Wikipédia | 18 | 306 | 919 | 0 | 1 / 1 | Celtic | — |
| 1910/11 | ogol + RSSSF + Wikipédia | 18 | 306 | 868 | 0 | 1 / 1 | Rangers | — |
| 1911/12 | ogol + RSSSF + Wikipédia | 18 | 306 | 815 | 0 | 1 / 1 | Rangers | — |
| 1912/13 | ogol + RSSSF + Wikipédia | 18 | 306 | 883 | 0 | 1 / 1 | Rangers | — |
| 1913/14 | ogol + RSSSF + Wikipédia | 20 | 380 | 1120 | 0 | 1 / 1 | Celtic | — |
| 1914/15 | ogol + RSSSF + Wikipédia | 20 | 380 | 1122 | 0 | 1 / 1 | Celtic | — |
| 1915/16 | ogol + RSSSF + Wikipédia | 20 | 379 | 1177 | 0 | 2 / 0 | Celtic | — |
| 1916/17 | ogol + RSSSF + Wikipédia | 20 | 380 | 1111 | 0 | 1 / 1 | Celtic | — |
| 1917/18 | ogol + RSSSF + Wikipédia | 18 | 306 | 928 | 0 | 2 / 0 | Rangers | — |
| 1918/19 | ogol + RSSSF + Wikipédia | 18 | 306 | 990 | 0 | 2 / 0 | Celtic | — |
| 1919/20 | ogol + RSSSF + Wikipédia | 22 | 462 | 1411 | 0 | 0 / 2 | Rangers | — |
| 1920/21 | ogol + RSSSF + Wikipédia | 22 | 462 | 1327 | 0 | 0 / 2 | Rangers | Celtic -6 pontos |
| 1921/22 | ogol + RSSSF + Wikipédia | 22 | 462 | 1238 | 0 | 2 / 0 | Celtic | — |
| 1922/23 | ogol + RSSSF + Wikipédia | 20 | 380 | 937 | 0 | 1 / 1 | Rangers | — |
| 1923/24 | ogol + RSSSF + Wikipédia | 20 | 380 | 1070 | 0 | 2 / 0 | Rangers | — |
| 1924/25 | ogol + RSSSF + Wikipédia | 20 | 380 | 1178 | 0 | 1 / 1 | Rangers | — |
| 1925/26 | ogol + RSSSF + Wikipédia | 20 | 380 | 1337 | 0 | 0 / 2 | Celtic | — |
| 1926/27 | ogol + RSSSF + Wikipédia | 20 | 380 | 1421 | 0 | 0 / 2 | Rangers | — |
| 1927/28 | ogol + RSSSF + Wikipédia | 20 | 380 | 1420 | 0 | 2 / 0 | Rangers | — |
| 1928/29 | ogol + RSSSF + Wikipédia | 20 | 380 | 1421 | 0 | 0 / 2 | Rangers | — |
| 1929/30 | ogol + RSSSF + Wikipédia | 20 | 380 | 1392 | 0 | 2 / 0 | Rangers | — |
| 1930/31 | ogol + RSSSF + Wikipédia | 20 | 380 | 1357 | 0 | 1 / 1 | Rangers | — |
| 1931/32 | ogol + RSSSF + Wikipédia | 20 | 380 | 1452 | 0 | 2 / 0 | Motherwell | — |
| 1932/33 | ogol + RSSSF + Wikipédia | 20 | 380 | 1484 | 0 | 2 / 0 | Rangers | — |
| 1933/34 | ogol + RSSSF + Wikipédia | 20 | 380 | 1454 | 0 | 0 / 2 | Rangers | — |
| 1934/35 | ogol + RSSSF + Wikipédia | 20 | 380 | 1372 | 0 | 1 / 1 | Rangers | — |
| 1935/36 | ogol + RSSSF + Wikipédia | 20 | 380 | 1430 | 0 | 1 / 1 | Celtic | — |
| 1936/37 | ogol + RSSSF + Wikipédia | 20 | 380 | 1450 | 0 | 2 / 0 | Rangers | — |
| 1937/38 | ogol + RSSSF + Wikipédia | 20 | 380 | 1431 | 0 | 1 / 1 | Celtic | — |
| 1938/39 | ogol + RSSSF + Wikipédia | 20 | 380 | 1524 | 0 | 1 / 1 | Rangers | — |
| 1946/47 | ogol + RSSSF + Wikipédia | 16 | 240 | 891 | 0 | 2 / 0 | Rangers | — |
| 1947/48 | ogol + RSSSF + Wikipédia | 16 | 240 | 844 | 0 | 0 / 2 | Hibernian | — |
| 1948/49 | ogol + RSSSF + Wikipédia | 16 | 240 | 861 | 0 | 2 / 0 | Rangers | — |
| 1949/50 | ogol + RSSSF + Wikipédia | 16 | 240 | 848 | 0 | 1 / 1 | Rangers | — |
| 1950/51 | ogol + RSSSF + Wikipédia | 16 | 240 | 831 | 0 | 2 / 0 | Hibernian | — |
| 1951/52 | ogol + RSSSF + Wikipédia | 16 | 240 | 888 | 0 | 2 / 0 | Hibernian | — |
| 1952/53 | ogol + RSSSF + Wikipédia | 16 | 240 | 953 | 0 | 1 / 1 | Rangers | — |
| 1953/54 | ogol + RSSSF + Wikipédia | 16 | 240 | 905 | 0 | 2 / 0 | Celtic | — |
| 1954/55 | ogol + RSSSF + Wikipédia | 16 | 240 | 862 | 0 | 1 / 1 | Aberdeen | — |
| 1955/56 | ogol + RSSSF + Wikipédia | 18 | 306 | 1138 | 0 | 1 / 1 | Rangers | — |
| 1956/57 | ogol + RSSSF + Wikipédia | 18 | 306 | 1160 | 0 | 2 / 0 | Rangers | — |
| 1957/58 | ogol + RSSSF + Wikipédia | 18 | 306 | 1238 | 0 | 1 / 1 | Hearts | — |
| 1958/59 | ogol + RSSSF + Wikipédia | 18 | 306 | 1195 | 0 | 2 / 0 | Rangers | — |
| 1959/60 | ogol + RSSSF + Wikipédia | 18 | 306 | 1249 | 0 | 2 / 0 | Hearts | — |
| 1960/61 | ogol + RSSSF + Wikipédia | 18 | 306 | 1146 | 0 | 2 / 0 | Rangers | — |
| 1961/62 | ogol + RSSSF + Wikipédia | 18 | 306 | 1096 | 0 | 0 / 2 | Dundee | — |
| 1962/63 | ogol + RSSSF + Wikipédia | 18 | 306 | 1101 | 0 | 2 / 0 | Rangers | — |
| 1963/64 | ogol + RSSSF + Wikipédia | 18 | 306 | 1094 | 0 | 1 / 1 | Rangers | — |
| 1964/65 | ogol + RSSSF + Wikipédia | 18 | 306 | 1096 | 0 | 2 / 0 | Kilmarnock | — |
| 1965/66 | ogol + RSSSF + Wikipédia | 18 | 306 | 1130 | 0 | 1 / 1 | Celtic | — |
| 1966/67 | ogol + RSSSF + Wikipédia | 18 | 306 | 1034 | 0 | 2 / 0 | Celtic | — |
| 1967/68 | ogol + RSSSF + Wikipédia | 18 | 306 | 1037 | 0 | 1 / 1 | Celtic | — |
| 1968/69 | ogol + RSSSF + Wikipédia | 18 | 306 | 956 | 0 | 1 / 1 | Celtic | — |
| 1969/70 | ogol + RSSSF + Wikipédia | 18 | 306 | 944 | 0 | 1 / 1 | Celtic | — |
| 1970/71 | ogol + RSSSF + Wikipédia | 18 | 306 | 889 | 0 | 0 / 2 | Celtic | — |
| 1971/72 | ogol + RSSSF + Wikipédia | 18 | 306 | 951 | 0 | 2 / 0 | Celtic | — |
| 1972/73 | ogol + RSSSF + Wikipédia | 18 | 306 | 932 | 0 | 2 / 0 | Celtic | — |
| 1973/74 | ogol + RSSSF + Wikipédia | 18 | 306 | 872 | 0 | 2 / 0 | Celtic | — |
| 1974/75 | ogol + RSSSF + Wikipédia | 18 | 306 | 950 | 0 | 2 / 0 | Rangers | — |
| 1975/76 | ogol + RSSSF + Wikipédia | 10 | 180 | 501 | 0 | 2 / 0 | Rangers | — |
| 1976/77 | ogol + RSSSF + Wikipédia | 10 | 180 | 507 | 0 | 2 / 0 | Celtic | — |
| 1977/78 | ogol + RSSSF + Wikipédia | 10 | 180 | 508 | 0 | 1 / 1 | Rangers | — |
| 1978/79 | ogol + RSSSF + Wikipédia | 10 | 180 | 483 | 0 | 2 / 0 | Celtic | — |
| 1979/80 | ogol + RSSSF + Wikipédia | 10 | 180 | 484 | 0 | 2 / 0 | Aberdeen | — |
| 1980/81 | ogol + RSSSF + Wikipédia | 10 | 180 | 481 | 0 | 2 / 0 | Celtic | — |
| 1981/82 | ogol + RSSSF + Wikipédia | 10 | 180 | 498 | 0 | 2 / 0 | Celtic | — |
| 1982/83 | ogol + RSSSF + Wikipédia | 10 | 180 | 529 | 0 | 1 / 1 | Dundee United | — |
| 1983/84 | ogol + RSSSF + Wikipédia | 10 | 180 | 533 | 0 | 2 / 0 | Aberdeen | — |
| 1984/85 | ogol + RSSSF + Wikipédia | 10 | 180 | 522 | 0 | 2 / 0 | Aberdeen | — |
| 1985/86 | ogol + RSSSF + Wikipédia | 10 | 180 | 498 | 0 | 2 / 0 | Celtic | — |
| 1986/87 | ogol + RSSSF + Wikipédia | 12 | 264 | 670 | 0 | 2 / 0 | Rangers | — |
| 1987/88 | ogol + RSSSF + Wikipédia | 12 | 264 | 646 | 0 | 2 / 0 | Celtic | — |
| 1988/89 | ogol + RSSSF + Wikipédia | 10 | 180 | 422 | 0 | 2 / 0 | Rangers | — |
| 1989/90 | ogol + RSSSF + Wikipédia | 10 | 180 | 414 | 0 | 2 / 0 | Rangers | — |
| 1990/91 | ogol + RSSSF + Wikipédia | 10 | 180 | 447 | 0 | 2 / 0 | Rangers | — |
| 1991/92 | ogol + RSSSF + Wikipédia | 12 | 264 | 677 | 0 | 2 / 0 | Rangers | — |
| 1992/93 | ogol + RSSSF + Wikipédia | 12 | 264 | 699 | 0 | 2 / 0 | Rangers | — |
| 1993/94 | ogol + RSSSF + Wikipédia | 12 | 264 | 583 | 0 | 2 / 0 | Rangers | — |
| 1994/95 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 453 | 0 | 2 / 0 | Rangers | — |
| 1995/96 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 477 | 0 | 2 / 0 | Rangers | — |
| 1996/97 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 504 | 0 | 2 / 0 | Rangers | — |
| 1997/98 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 497 | 0 | 1 / 1 | Celtic | Dunfermline -1 pontos |
| 1998/99 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 471 | 0 | 2 / 0 | Rangers | — |
| 1999/00 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 10 | 180 | 528 | 0 | 2 / 0 | Rangers | — |
| 2000/01 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 12 | 228 | 605 | 0 | 2 / 0 | Celtic | — |
| 2001/02 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 617 | 617 | 2 / 0 | Celtic | — |
| 2002/03 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 669 | 666 | 2 / 0 | Rangers | — |
| 2003/04 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 637 | 634 | 2 / 0 | Celtic | — |
| 2004/05 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 596 | 596 | 2 / 0 | Rangers | — |
| 2005/06 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 641 | 641 | 2 / 0 | Celtic | — |
| 2006/07 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 560 | 552 | 2 / 0 | Celtic | — |
| 2007/08 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 610 | 604 | 2 / 0 | Celtic | Gretna -10 pontos |
| 2008/09 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 548 | 548 | 2 / 0 | Rangers | — |
| 2009/10 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 585 | 585 | 2 / 0 | Rangers | — |
| 2010/11 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 584 | 570 | 2 / 0 | Rangers | — |
| 2011/12 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 601 | 596 | 2 / 0 | Celtic | Rangers -10 pontos |
| 2012/13 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 623 | 623 | 2 / 0 | Celtic | — |
| 2013/14 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 626 | 616 | 2 / 0 | Celtic | Hearts -15 pontos |
| 2014/15 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 587 | 587 | 2 / 0 | Celtic | — |
| 2015/16 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 650 | 650 | 1 / 1 | Celtic | Dundee United -3 pontos |
| 2016/17 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 628 | 607 | 2 / 0 | Celtic | — |
| 2017/18 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 594 | 585 | 2 / 0 | Celtic | — |
| 2018/19 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 578 | 578 | 2 / 0 | Celtic | — |
| 2019/20 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 12 | 179 | 490 | 464 | 1 / 0 | Celtic | — |
| 2020/21 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 552 | 552 | 2 / 0 | Rangers | — |
| 2021/22 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 563 | 563 | 2 / 0 | Celtic | — |
| 2022/23 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 670 | 670 | 2 / 0 | Celtic | — |
| 2023/24 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 629 | 155 | 2 / 0 | Celtic | — |
| 2024/25 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 675 | 675 | 2 / 0 | Celtic | — |
| 2025/26 | ogol + football-data + ESPN + RSSSF + Wikipédia | 12 | 228 | 634 | 631 | 2 / 0 | Celtic | — |

## Conferência e ocorrências, temporada a temporada

### 1890/91

- tabela publicada x jogos (Wikipédia) — clubes diferentes: ['Renton']
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- Cowlairs não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- título dividido entre Dumbarton e Rangers: empataram em pontos e no jogo de desempate (2-2); os dois ficam como campeões, na 1ª posição
- 90 jogos sem rodada no ogol (ex.: Abercorn x Cowlairs)

### 1891/92

- placar diferente na matriz da Wikipédia — Clyde x Abercorn: ogol 7-2; Wikipédia 7-3
- placar diferente na matriz da Wikipédia — Renton x Dumbarton: ogol 1-2; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — St Mirren x Abercorn: ogol 0-3; Wikipédia 2-1
- placar corrigido pela matriz da Wikipédia: Renton x Dumbarton (1891-11-15) de 1-2 para 2-3 — com ele, as tabelas publicadas fecham melhor (6 -> 2 linhas que não fecham)
- tabela publicada x jogos (Wikipédia) — Clyde tabela [22, 8, 4, 10, 63, 62, 20] jogos [22, 8, 4, 10, 63, 61, 20]
- tabela publicada x jogos (Wikipédia) — Abercorn tabela [22, 6, 5, 11, 45, 59, 17] jogos [22, 6, 5, 11, 44, 59, 17]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- Cambuslang não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- Vale of Leven não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 132 jogos sem rodada no ogol (ex.: Clyde x Third Lanark)

### 1892/93

- placar diferente na matriz da Wikipédia — Clyde x Third Lanark: ogol 1-4; Wikipédia 2-4
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Leith Athletic, Wikipédia Dumbarton); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- Abercorn não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- Clyde não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Leith Athletic x Celtic)

### 1893/94

- Renton não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Celtic x Third Lanark)

### 1894/95

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Leith Athletic, Wikipédia Dumbarton); fica a da Wikipédia
- Leith Athletic não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Celtic x St Bernard's)

### 1895/96

- placar diferente na matriz da Wikipédia — Dundee x Hibernian: ogol 2-2; Wikipédia 2-0
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Third Lanark, Wikipédia St Bernard's); fica a da Wikipédia
- Dumbarton não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Dundee x Celtic)

### 1896/97

- Abercorn não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Clyde x St Bernard's)

### 1897/98

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Third Lanark, Wikipédia St Mirren); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 90 jogos sem rodada no ogol (ex.: Partick Thistle x Third Lanark)

### 1898/99

- placar diferente na matriz da Wikipédia — Rangers x Hibernian: ogol 10-0; Wikipédia 10-1
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF St Bernard's, Wikipédia Clyde); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- Partick Thistle não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Rangers x Celtic)

### 1899/00

- tabela publicada x jogos (RSSSF) — Rangers tabela [18, 15, 3, 1, 69, 27, 32] jogos [18, 15, 2, 1, 69, 27, 32]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- Clyde não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- St Bernard's não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 90 jogos sem rodada no ogol (ex.: Celtic x Rangers)

### 1900/01

- Partick Thistle não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- 110 jogos sem rodada no ogol (ex.: Kilmarnock x Third Lanark)

### 1901/02

- tabela publicada x jogos (Wikipédia) — Hibernian tabela [18, 6, 4, 8, 36, 24, 16] jogos [18, 6, 4, 8, 36, 23, 16]
- tabela publicada x jogos (Wikipédia) — Kilmarnock tabela [18, 5, 6, 7, 21, 25, 16] jogos [18, 5, 6, 7, 22, 27, 16]
- tabela publicada x jogos (Wikipédia) — Dundee tabela [18, 4, 5, 9, 16, 31, 13] jogos [18, 4, 5, 9, 15, 31, 13]
- tabela publicada x jogos (Wikipédia) — Greenock Morton tabela [18, 1, 5, 12, 18, 40, 7] jogos [18, 1, 5, 12, 20, 41, 7]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- 90 jogos sem rodada no ogol (ex.: Celtic x Rangers)

### 1902/03

- tabela publicada x jogos (Wikipédia) — Rangers tabela [22, 12, 5, 5, 56, 24, 29] jogos [22, 12, 5, 5, 56, 30, 29]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- 132 jogos sem rodada no ogol (ex.: Rangers x Celtic)

### 1903/04

- mando corrigido: o ogol traz Queen's Park 1-1 Hibernian (1903-12-19); a matriz da Wikipédia traz o jogo com o outro mandante
- mando corrigido: o ogol traz Kilmarnock 0-2 Motherwell (1903-10-24); a matriz da Wikipédia traz o jogo com o outro mandante
- mando corrigido: o ogol traz Greenock Morton 1-3 Rangers (1903-10-24); a matriz da Wikipédia traz o jogo com o outro mandante
- placar diferente na matriz da Wikipédia — Kilmarnock x Dundee: ogol 0-1; Wikipédia 1-2
- placar corrigido pela matriz da Wikipédia: Kilmarnock x Dundee (1903-11-07) de 0-1 para 1-2 — com ele, as tabelas publicadas fecham melhor (9 -> 8 linhas que não fecham)
- tabela publicada x jogos (RSSSF) — St Mirren tabela [26, 11, 5, 8, 45, 38, 27] jogos [26, 11, 5, 10, 45, 38, 27]
- tabela publicada x jogos (Wikipédia) — Celtic tabela [26, 18, 2, 6, 68, 27, 38] jogos [26, 18, 2, 6, 69, 28, 38]
- tabela publicada x jogos (Wikipédia) — Dundee tabela [26, 13, 2, 11, 54, 45, 28] jogos [26, 13, 2, 11, 55, 46, 28]
- tabela publicada x jogos (Wikipédia) — Partick Thistle tabela [26, 10, 7, 9, 46, 41, 27] jogos [26, 10, 7, 9, 43, 40, 27]
- tabela publicada x jogos (Wikipédia) — Port Glasgow Athletic tabela [26, 8, 4, 14, 32, 49, 20] jogos [26, 8, 4, 14, 33, 49, 20]
- tabela publicada x jogos (Wikipédia) — Hibernian tabela [26, 7, 5, 14, 29, 40, 19] jogos [26, 7, 5, 14, 31, 42, 19]
- tabela publicada x jogos (Wikipédia) — Greenock Morton tabela [26, 7, 4, 15, 32, 53, 18] jogos [26, 7, 4, 15, 31, 51, 18]
- tabela publicada x jogos (Wikipédia) — Kilmarnock tabela [26, 4, 5, 17, 24, 63, 13] jogos [26, 4, 5, 17, 27, 66, 13]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: St Mirren; Wikipédia: Celtic, Dundee, Greenock Morton, Hibernian, Kilmarnock, Partick Thistle, Port Glasgow Athletic): em cada clube, a outra tabela fecha com os jogos
- 182 jogos sem rodada no ogol (ex.: Port Glasgow Athletic x Third Lanark)

### 1904/05

- placar diferente na matriz da Wikipédia — Motherwell x Hearts: ogol 2-4; Wikipédia 0-4
- tabela publicada x jogos (RSSSF) — Greenock Morton tabela [26, 7, 4, 15, 27, 48, 18] jogos [26, 7, 4, 15, 27, 50, 18]
- tabela publicada x jogos (Wikipédia) — Hearts tabela [26, 11, 3, 12, 46, 44, 25] jogos [26, 11, 3, 12, 43, 44, 25]
- tabela publicada x jogos (Wikipédia) — Port Glasgow Athletic tabela [26, 8, 5, 13, 30, 51, 21] jogos [26, 8, 5, 13, 30, 48, 21]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Greenock Morton; Wikipédia: Hearts, Port Glasgow Athletic): em cada clube, a outra tabela fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Dundee, Wikipédia Hearts); fica a da Wikipédia
- a ordem da Wikipédia não sai de nenhum critério de desempate e a da RSSSF sai: fica a da RSSSF
- 182 jogos sem rodada no ogol (ex.: Rangers x Celtic)

### 1905/06

- placar diferente na matriz da Wikipédia — Falkirk x Aberdeen: ogol 2-2; Wikipédia 1-1
- tabela publicada x jogos (RSSSF) — Aberdeen tabela [30, 8, 8, 14, 36, 48, 24] jogos [30, 8, 8, 14, 37, 49, 24]
- tabela publicada x jogos (RSSSF) — Falkirk tabela [30, 9, 5, 16, 52, 68, 23] jogos [30, 9, 5, 16, 53, 69, 23]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 240 jogos sem rodada no ogol (ex.: Celtic x Rangers)

### 1906/07

- tabela publicada x jogos (RSSSF) — Aberdeen tabela [34, 10, 10, 14, 48, 54, 30] jogos [34, 10, 10, 14, 48, 55, 30]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Aberdeen, Wikipédia Hibernian); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada

### 1907/08

- tabela publicada x jogos (RSSSF) — Hibernian tabela [34, 17, 8, 9, 55, 45, 42] jogos [34, 17, 8, 9, 55, 42, 42]
- tabela publicada x jogos (RSSSF) — Aberdeen tabela [34, 12, 9, 13, 45, 44, 35] jogos [34, 13, 9, 12, 45, 44, 35]
- tabela publicada x jogos (Wikipédia) — Clyde tabela [34, 5, 8, 21, 38, 75, 18] jogos [34, 5, 8, 21, 36, 75, 18]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Aberdeen, Hibernian; Wikipédia: Clyde): em cada clube, a outra tabela fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Hamilton Academical, Wikipédia Hearts); fica a da Wikipédia
- a ordem da Wikipédia não sai de nenhum critério de desempate e a da RSSSF sai: fica a da RSSSF

### 1908/09

- placar diferente na matriz da Wikipédia — Partick Thistle x Motherwell: ogol 0-2; Wikipédia 2-0
- tabela publicada x jogos (RSSSF) — Celtic tabela [34, 23, 5, 6, 71, 21, 51] jogos [34, 23, 5, 6, 71, 24, 51]
- tabela publicada x jogos (RSSSF) — Rangers tabela [34, 19, 7, 7, 91, 38, 45] jogos [34, 19, 7, 8, 91, 38, 45]
- tabela publicada x jogos (RSSSF) — Hearts tabela [34, 12, 7, 14, 54, 49, 32] jogos [34, 12, 8, 14, 54, 49, 32]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF Falkirk, Wikipédia Kilmarnock); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada

### 1909/10

- tabela publicada x jogos (RSSSF) — Falkirk tabela [34, 22, 11, 4, 71, 28, 52] jogos [34, 22, 8, 4, 71, 28, 52]
- tabela publicada x jogos (RSSSF) — Airdrieonians tabela [34, 12, 9, 13, 47, 57, 33] jogos [34, 12, 9, 13, 46, 57, 33]
- tabela publicada x jogos (RSSSF) — Hearts tabela [34, 12, 7, 15, 53, 40, 31] jogos [34, 12, 7, 15, 59, 50, 31]
- tabela publicada x jogos (RSSSF) — Queen's Park tabela [34, 12, 6, 16, 50, 74, 30] jogos [34, 12, 6, 16, 54, 74, 30]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- Port Glasgow Athletic não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)

### 1910/11

- tabela publicada x jogos (RSSSF) — Motherwell tabela [34, 8, 4, 22, 34, 56, 20] jogos [34, 8, 4, 22, 37, 66, 20]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Clyde, Wikipédia Third Lanark); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 306 jogos sem rodada no ogol (ex.: Dundee x Motherwell)

### 1911/12

- placar diferente na matriz da Wikipédia — Aberdeen x Greenock Morton: ogol 1-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Rangers x Airdrieonians: ogol 4-1; Wikipédia 2-1
- tabela publicada x jogos (Wikipédia) — Falkirk tabela [34, 15, 6, 13, 46, 33, 36] jogos [34, 15, 6, 13, 46, 43, 36]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- 306 jogos sem rodada no ogol (ex.: Motherwell x Aberdeen)

### 1912/13

- placar diferente na matriz da Wikipédia — Celtic x Queen's Park: ogol 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Clyde x Hamilton Academical: ogol 0-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Queen's Park x Hibernian: ogol 3-5; Wikipédia 2-5
- placar corrigido pela matriz da Wikipédia: Clyde x Hamilton Academical (1912-08-17) de 0-0 para 2-1 — com ele, as tabelas publicadas fecham melhor (5 -> 1 linhas que não fecham)
- tabela publicada x jogos (RSSSF) — Queen's Park tabela [34, 5, 3, 26, 34, 87, 13] jogos [34, 5, 3, 26, 34, 88, 13]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 5 posições (ex.: RSSSF Motherwell, Wikipédia Hibernian); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 306 jogos sem rodada no ogol (ex.: Aberdeen x Raith Rovers)

### 1913/14

- tabela publicada x jogos (RSSSF) — Kilmarnock tabela [38, 11, 9, 18, 40, 68, 31] jogos [38, 11, 9, 18, 48, 68, 31]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Hamilton Academical, Wikipédia Motherwell); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 380 jogos sem rodada no ogol (ex.: Airdrieonians x Clyde)

### 1914/15

- placar diferente na matriz da Wikipédia — Greenock Morton x Queen's Park: ogol 6-2; Wikipédia 4-2
- tabela publicada x jogos (RSSSF) — Falkirk tabela [38, 16, 7, 16, 48, 58, 39] jogos [38, 16, 7, 15, 48, 48, 39]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 8 posições (ex.: RSSSF Hamilton Academical, Wikipédia Partick Thistle); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- 380 jogos sem rodada no ogol (ex.: Greenock Morton x Hearts)

### 1915/16

- um jogo da temporada não foi disputado (379 de 380); as tabelas da RSSSF e da Wikipédia fecham com os 379
- temporada com 379 jogos de 380 (jogos por par: {1: 379})
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Partick Thistle, Wikipédia Hearts); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada

### 1916/17

- tabela publicada x jogos (RSSSF) — Hamilton Academical tabela [38, 13, 9, 16, 53, 73, 35] jogos [38, 13, 9, 16, 54, 73, 35]
- tabela publicada x jogos (RSSSF) — Clyde tabela [38, 10, 14, 14, 41, 52, 34] jogos [38, 10, 14, 14, 41, 53, 34]
- tabela publicada x jogos (RSSSF) — Hibernian tabela [38, 10, 10, 18, 57, 62, 30] jogos [38, 10, 10, 18, 57, 72, 30]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Partick Thistle, Wikipédia Dumbarton); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada
- Aberdeen não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- Dundee não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)
- Raith Rovers não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)

### 1917/18

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Queen's Park, Wikipédia Dumbarton); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada

### 1918/19

- placar diferente na matriz da Wikipédia — Clydebank (1914) x Greenock Morton: ogol 0-3; Wikipédia 2-3
- placar corrigido pela matriz da Wikipédia: Clydebank (1914) x Greenock Morton (1919-01-04) de 0-3 para 2-3 — com ele, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF Queen's Park, Wikipédia Kilmarnock); fica a da Wikipédia
- até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o título ia para jogo extra); a ordem entre eles é a da tabela publicada

### 1919/20

- tabela publicada x jogos (RSSSF) — Rangers tabela [42, 31, 9, 2, 105, 25, 71] jogos [42, 31, 9, 2, 106, 25, 71]
- tabela publicada x jogos (RSSSF) — Queen's Park tabela [42, 14, 14, 18, 67, 81, 38] jogos [42, 14, 10, 18, 67, 73, 38]
- tabela publicada x jogos (RSSSF) — Raith Rovers tabela [42, 11, 6, 21, 61, 83, 32] jogos [42, 11, 10, 21, 61, 83, 32]
- tabela publicada x jogos (Wikipédia) — Clydebank (1914) tabela [42, 20, 8, 14, 79, 65, 48] jogos [42, 20, 8, 14, 78, 54, 48]
- tabela publicada x jogos (Wikipédia) — Kilmarnock tabela [42, 20, 3, 19, 59, 73, 43] jogos [42, 20, 3, 19, 59, 74, 43]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Queen's Park, Raith Rovers, Rangers; Wikipédia: Clydebank (1914), Kilmarnock): em cada clube, a outra tabela fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Queen's Park, Wikipédia St Mirren); fica a da Wikipédia
- a ordem da Wikipédia não sai de nenhum critério de desempate e a da RSSSF sai: fica a da RSSSF

### 1920/21

- punição tirada da tabela da RSSSF: Celtic -6 pontos
- tabela publicada x jogos (RSSSF) — Hearts tabela [42, 20, 10, 4, 74, 49, 50] jogos [42, 20, 10, 12, 74, 49, 50]
- tabela publicada x jogos (RSSSF) — Motherwell tabela [42, 19, 10, 13, 75, 48, 48] jogos [42, 19, 10, 13, 75, 51, 48]
- tabela publicada x jogos (Wikipédia) — Celtic tabela [42, 30, 6, 6, 89, 31, 66] jogos [42, 30, 6, 6, 86, 35, 60]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Hearts, Motherwell; Wikipédia: Celtic): em cada clube, a outra tabela fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF Aberdeen, Wikipédia Kilmarnock); fica a da Wikipédia
- a ordem da Wikipédia não sai de nenhum critério de desempate e a da RSSSF sai: fica a da RSSSF
- 462 jogos sem rodada no ogol (ex.: Albion Rovers x Raith Rovers)

### 1921/22

- placar diferente na matriz da Wikipédia — St Mirren x Raith Rovers: ogol 1-1; Wikipédia 1-2
- 462 jogos sem rodada no ogol (ex.: Partick Thistle x Aberdeen)

### 1922/23

- tabela publicada x jogos (RSSSF) — Ayr United tabela [38, 13, 12, 13, 43, 74, 38] jogos [38, 13, 12, 13, 43, 44, 38]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1923/24

- sem ocorrências

### 1924/25

- placar diferente na matriz da Wikipédia — Hearts x Dundee: ogol 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Queen's Park x St Mirren: ogol 2-2; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — St Mirren x St Johnstone: ogol 0-1; Wikipédia 1-0
- tabela publicada x jogos (RSSSF) — St Mirren tabela [38, 18, 4, 16, 65, 63, 40] jogos [38, 18, 5, 15, 66, 63, 41]
- tabela publicada x jogos (RSSSF) — Queen's Park tabela [38, 12, 8, 18, 50, 71, 32] jogos [38, 11, 9, 18, 50, 72, 31]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1925/26

- placar diferente na matriz da Wikipédia — Clydebank (1914) x Cowdenbeath: ogol 4-3; Wikipédia 3-4
- placar diferente na matriz da Wikipédia — Clydebank (1914) x Hamilton Academical: ogol 1-3; Wikipédia 1-4
- placar diferente na matriz da Wikipédia — Clydebank (1914) x Rangers: ogol 2-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Hibernian x Cowdenbeath: ogol 1-2; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Motherwell x St Mirren: ogol 0-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — St Johnstone x St Mirren: ogol 1-0; Wikipédia 0-1
- tabela publicada x jogos (RSSSF) — Airdrieonians tabela [38, 23, 4, 10, 95, 54, 50] jogos [38, 23, 4, 11, 95, 54, 50]
- tabela publicada x jogos (Wikipédia) — St Mirren tabela [38, 20, 7, 11, 63, 52, 47] jogos [38, 20, 7, 11, 62, 52, 47]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Airdrieonians; Wikipédia: St Mirren): em cada clube, a outra tabela fecha com os jogos

### 1926/27

- tabela publicada x jogos (RSSSF) — Hamilton Academical tabela [38, 13, 9, 16, 60, 82, 35] jogos [38, 13, 9, 16, 60, 85, 35]
- tabela publicada x jogos (Wikipédia) — Falkirk tabela [38, 15, 12, 11, 77, 60, 42] jogos [38, 16, 10, 12, 77, 60, 42]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Hamilton Academical; Wikipédia: Falkirk): em cada clube, a outra tabela fecha com os jogos

### 1927/28

- sem ocorrências

### 1928/29

- tabela publicada x jogos (RSSSF) — Partick Thistle tabela [38, 17, 7, 14, 91, 72, 41] jogos [38, 17, 7, 14, 91, 70, 41]
- tabela publicada x jogos (RSSSF) — Airdrieonians tabela [38, 12, 7, 19, 53, 65, 31] jogos [38, 12, 7, 19, 56, 65, 31]
- tabela publicada x jogos (RSSSF) — Ayr United tabela [38, 9, 7, 19, 65, 84, 31] jogos [38, 12, 7, 19, 65, 84, 31]
- tabela publicada x jogos (Wikipédia) — Dundee tabela [38, 9, 11, 18, 59, 59, 29] jogos [38, 9, 11, 18, 59, 69, 29]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Airdrieonians, Ayr United, Partick Thistle; Wikipédia: Dundee): em cada clube, a outra tabela fecha com os jogos

### 1929/30

- placar diferente na matriz da Wikipédia — Ayr United x St Mirren: ogol 1-0; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Queen's Park x St Mirren: ogol 1-6; Wikipédia 1-0

### 1930/31

- tabela publicada x jogos (RSSSF) — East Fife tabela [38, 8, 4, 23, 45, 113, 20] jogos [38, 8, 4, 26, 45, 113, 20]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- 380 jogos sem rodada no ogol (ex.: Airdrieonians x Queen's Park)

### 1931/32

- 380 jogos sem rodada no ogol (ex.: Aberdeen x Cowdenbeath)

### 1932/33

- sem ocorrências

### 1933/34

- tabela publicada x jogos (RSSSF) — Partick Thistle tabela [38, 14, 5, 19, 72, 78, 33] jogos [38, 14, 5, 19, 73, 78, 33]
- tabela publicada x jogos (Wikipédia) — Queen of the South tabela [38, 21, 3, 14, 75, 48, 45] jogos [38, 21, 3, 14, 75, 78, 45]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Partick Thistle; Wikipédia: Queen of the South): em cada clube, a outra tabela fecha com os jogos

### 1934/35

- tabela publicada x jogos (RSSSF) — Ayr United tabela [38, 12, 5, 22, 61, 112, 29] jogos [38, 12, 5, 21, 61, 112, 29]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1935/36

- tabela publicada x jogos (RSSSF) — Ayr United tabela [38, 8, 3, 24, 53, 98, 25] jogos [38, 11, 3, 24, 53, 98, 25]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1936/37

- placar diferente na matriz da Wikipédia — Falkirk x Aberdeen: ogol 1-2; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Hearts x Rangers: ogol 5-2; Wikipédia 4-2
- placar diferente na matriz da Wikipédia — Partick Thistle x Queen of the South: ogol 4-1; Wikipédia 3-1

### 1937/38

- placar diferente na matriz da Wikipédia — Aberdeen x Clyde: ogol 5-2; Wikipédia 3-2
- tabela publicada x jogos (RSSSF) — Hearts tabela [38, 26, 6, 6, 90, 70, 58] jogos [38, 26, 6, 6, 90, 50, 58]
- tabela publicada x jogos (RSSSF) — Queen of the South tabela [38, 11, 9, 16, 58, 71, 33] jogos [38, 11, 11, 16, 58, 71, 33]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1938/39

- placar diferente na matriz da Wikipédia — St Johnstone x Queen of the South: ogol 3-1; Wikipédia 3-0
- tabela publicada x jogos (RSSSF) — Queen of the South tabela [38, 17, 9, 12, 69, 64, 43] jogos [38, 17, 9, 12, 70, 64, 43]
- tabela publicada x jogos (RSSSF) — St Johnstone tabela [38, 17, 6, 15, 85, 82, 40] jogos [38, 17, 6, 15, 85, 83, 40]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1946/47

- placar diferente na matriz da Wikipédia — Queen's Park x Hamilton Academical: ogol 3-1; Wikipédia 2-1
- placar corrigido pela matriz da Wikipédia: Queen's Park x Hamilton Academical (1946-11-23) de 3-1 para 2-1 — com ele, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- 240 jogos sem rodada no ogol (ex.: Aberdeen x Kilmarnock)

### 1947/48

- placar diferente na matriz da Wikipédia — Falkirk x Partick Thistle: ogol 1-2; Wikipédia 1-3
- tabela publicada x jogos (RSSSF) — Aberdeen tabela [30, 10, 8, 12, 45, 45, 27] jogos [30, 10, 7, 13, 45, 45, 27]
- tabela publicada x jogos (Wikipédia) — Hibernian tabela [30, 22, 4, 4, 85, 26, 48] jogos [30, 22, 4, 4, 86, 27, 48]
- tabela publicada x jogos (Wikipédia) — Rangers tabela [30, 21, 4, 5, 92, 20, 46] jogos [30, 21, 4, 5, 64, 28, 46]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Aberdeen; Wikipédia: Hibernian, Rangers): em cada clube, a outra tabela fecha com os jogos

### 1948/49

- placar diferente na matriz da Wikipédia — Rangers x Greenock Morton: ogol 4-1; Wikipédia 4-0
- 240 jogos sem rodada no ogol (ex.: Celtic x Greenock Morton)

### 1949/50

- tabela publicada x jogos (RSSSF) — Partick Thistle tabela [30, 11, 3, 14, 55, 45, 29] jogos [30, 13, 3, 14, 55, 45, 29]
- tabela publicada x jogos (RSSSF) — Motherwell tabela [30, 17, 5, 15, 53, 58, 25] jogos [30, 10, 5, 15, 53, 58, 25]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1950/51

- placar corrigido: Airdrieonians x Falkirk de 1-1 para 11-1 — o ogol e a matriz da Wikipédia trazem 1-1; as tabelas da RSSSF e da Wikipédia só fecham com 11-1, e o Falkirk registra o 1-11 como a maior derrota da sua história na liga (fitbastats.com/falkirk, recordes do clube)
- placar diferente na matriz da Wikipédia — Airdrieonians x Falkirk: ogol 11-1; Wikipédia 1-1
- 240 jogos sem rodada no ogol (ex.: Airdrieonians x Aberdeen)

### 1951/52

- sem ocorrências

### 1952/53

- tabela publicada x jogos (RSSSF) — Dundee tabela [30, 9, 11, 11, 44, 37, 29] jogos [30, 9, 11, 10, 44, 37, 29]
- tabela publicada x jogos (RSSSF) — Celtic tabela [30, 9, 7, 12, 51, 54, 29] jogos [30, 11, 7, 12, 51, 54, 29]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1953/54

- sem ocorrências

### 1954/55

- placar diferente na matriz da Wikipédia — Queen of the South x Raith Rovers: ogol 2-0; Wikipédia 2-3
- tabela publicada x jogos (RSSSF) — Clyde tabela [30, 11, 10, 9, 59, 50, 31] jogos [30, 11, 9, 10, 59, 50, 31]
- tabela publicada x jogos (RSSSF) — Kilmarnock tabela [30, 10, 6, 14, 44, 58, 26] jogos [30, 10, 6, 14, 46, 58, 26]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1955/56

- placar diferente na matriz da Wikipédia — Queen of the South x Stirling Albion: ogol 4-0; Wikipédia 4-2
- placar diferente na matriz da Wikipédia — Raith Rovers x Hibernian: ogol 0-4; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Rangers x Queen of the South: ogol 8-0; Wikipédia 6-0
- tabela publicada x jogos (RSSSF) — Rangers tabela [34, 22, 8, 4, 39, 27, 52] jogos [34, 22, 8, 4, 85, 27, 52]
- tabela publicada x jogos (RSSSF) — East Fife tabela [34, 13, 5, 16, 60, 69, 31] jogos [34, 13, 5, 16, 61, 69, 31]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1956/57

- placar diferente na matriz da Wikipédia — Partick Thistle x Ayr United: ogol 5-1; Wikipédia 3-1

### 1957/58

- placar diferente na matriz da Wikipédia — Clyde x Aberdeen: ogol 5-1; Wikipédia 3-1
- tabela publicada x jogos (RSSSF) — Celtic tabela [34, 19, 8, 7, 86, 47, 46] jogos [34, 19, 8, 7, 84, 47, 46]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1958/59

- placar diferente na matriz da Wikipédia — Clyde x Stirling Albion: ogol 2-2; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — Hearts x Dundee: ogol 1-0; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Raith Rovers x Falkirk: ogol 1-2; Wikipédia 1-0

### 1959/60

- placar diferente na matriz da Wikipédia — Celtic x Airdrieonians: ogol 0-0; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Hearts x Dunfermline: ogol 3-1; Wikipédia 5-1

### 1960/61

- placar diferente na matriz da Wikipédia — Dundee x Third Lanark: ogol 0-2; Wikipédia 2-2
- 306 jogos sem rodada no ogol (ex.: Aberdeen x Dunfermline)

### 1961/62

- placar diferente na matriz da Wikipédia — Rangers x Third Lanark: ogol 3-1; Wikipédia 3-0
- tabela publicada x jogos (RSSSF) — Motherwell tabela [34, 13, 6, 15, 66, 62, 32] jogos [34, 13, 6, 15, 65, 62, 32]
- tabela publicada x jogos (Wikipédia) — Hearts tabela [34, 16, 6, 12, 55, 49, 38] jogos [34, 16, 6, 12, 54, 49, 38]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Motherwell; Wikipédia: Hearts): em cada clube, a outra tabela fecha com os jogos

### 1962/63

- sem ocorrências

### 1963/64

- tabela publicada x jogos (RSSSF) — St Johnstone tabela [34, 11, 5, 17, 54, 70, 28] jogos [34, 11, 6, 17, 54, 70, 28]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1964/65

- sem ocorrências

### 1965/66

- tabela publicada x jogos (RSSSF) — Dunfermline tabela [34, 19, 8, 9, 94, 55, 44] jogos [34, 19, 6, 9, 94, 55, 44]
- tabela publicada x jogos (RSSSF) — Falkirk tabela [34, 15, 2, 17, 48, 72, 31] jogos [34, 15, 1, 18, 48, 72, 31]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1966/67

- sem ocorrências

### 1967/68

- tabela publicada x jogos (RSSSF) — Aberdeen tabela [34, 16, 5, 13, 65, 48, 37] jogos [34, 16, 5, 13, 63, 48, 37]
- tabela publicada x jogos (RSSSF) — Falkirk tabela [34, 7, 12, 15, 36, 45, 26] jogos [34, 7, 12, 15, 36, 50, 26]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1968/69

- placar diferente na matriz da Wikipédia — Arbroath x Falkirk: ogol 3-0; Wikipédia 3-1
- tabela publicada x jogos (RSSSF) — Arbroath tabela [34, 5, 6, 23, 41, 102, 16] jogos [34, 5, 6, 23, 41, 82, 16]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos

### 1969/70

- tabela publicada x jogos (RSSSF) — Dunfermline tabela [34, 13, 9, 12, 52, 52, 35] jogos [34, 15, 5, 14, 45, 45, 35]
- tabela publicada x jogos (RSSSF) — Greenock Morton tabela [34, 15, 5, 14, 45, 45, 35] jogos [34, 13, 9, 12, 52, 52, 35]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Dunfermline, Wikipédia Greenock Morton); fica a da Wikipédia

### 1970/71

- tabela publicada x jogos (RSSSF) — Celtic tabela [34, 26, 6, 3, 89, 23, 56] jogos [34, 25, 6, 3, 89, 23, 56]
- tabela publicada x jogos (Wikipédia) — Cowdenbeath tabela [34, 7, 3, 24, 33, 69, 17] jogos [34, 7, 3, 24, 33, 77, 17]
- as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: Celtic; Wikipédia: Cowdenbeath): em cada clube, a outra tabela fecha com os jogos
- 306 jogos sem rodada no ogol (ex.: Aberdeen x Airdrieonians)

### 1971/72

- sem ocorrências

### 1972/73

- 306 jogos sem rodada no ogol (ex.: Aberdeen x Hibernian)

### 1973/74

- 306 jogos sem rodada no ogol (ex.: Clyde x East Fife)

### 1974/75

- sem ocorrências

### 1975/76

- sem ocorrências

### 1976/77

- 180 jogos sem rodada no ogol (ex.: Aberdeen x Hearts)

### 1977/78

- tabela publicada x jogos (Wikipédia) — Partick Thistle tabela [36, 14, 5, 17, 52, 62, 33] jogos [36, 14, 5, 17, 52, 64, 33]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- 180 jogos sem rodada no ogol (ex.: Rangers x Hibernian)

### 1978/79

- placar diferente na matriz da Wikipédia — Dundee United x Celtic: ogol 1-0, 1-0; Wikipédia 1-0, 2-1
- placar diferente na matriz da Wikipédia — Motherwell x Aberdeen: ogol 1-1, 3-1; Wikipédia 1-1, 1-1
- placar corrigido pela matriz da Wikipédia: Dundee United x Celtic (1978-10-14) de 1-0 para 2-1 — com ele, as tabelas publicadas fecham melhor (8 -> 4 linhas que não fecham)
- placar corrigido pela matriz da Wikipédia: Motherwell x Aberdeen (1978-11-11) de 3-1 para 1-1 — com ele, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- 38 jogos sem rodada no ogol (ex.: Dundee United x Hibernian)

### 1979/80

- sem ocorrências

### 1980/81

- sem ocorrências

### 1981/82

- sem ocorrências

### 1982/83

- tabela publicada x jogos (Wikipédia) — Aberdeen tabela [36, 25, 5, 6, 76, 25, 55] jogos [36, 25, 5, 6, 76, 24, 55]
- tabela publicada x jogos (Wikipédia) — Rangers tabela [36, 13, 12, 11, 53, 41, 38] jogos [36, 13, 12, 11, 52, 41, 38]
- tabela publicada x jogos (Wikipédia) — Greenock Morton tabela [36, 6, 8, 22, 36, 81, 20] jogos [36, 6, 8, 22, 30, 74, 20]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985/86

- placar diferente na matriz da Wikipédia — Celtic x Dundee: ogol 2-0, 2-1; Wikipédia 2-1, 2-1

### 1986/87

- placar diferente na matriz da Wikipédia — Aberdeen x Clydebank: ogol 1-1, 5-0; Wikipédia 1-1, 4-0

### 1987/88

- placar diferente na matriz da Wikipédia — Falkirk x Hearts: ogol 1-5, 2-0; Wikipédia 1-5, 2-1

### 1988/89

- a caixa de resumo da Wikipédia não lista rebaixados; o Hamilton Academical, último, não está em 1989/90
- placar diferente na matriz da Wikipédia — Dundee United x Hamilton Academical: ogol 0-1, 1-0; Wikipédia 0-0, 1-0
- rebaixados: pela temporada seguinte ['Hamilton Academical']; caixa da Wikipédia []

### 1989/90

- a caixa de resumo da Wikipédia não lista rebaixados; o Dundee, último, não está em 1990/91
- placar diferente na matriz da Wikipédia — Dundee x Motherwell: ogol 1-2, 2-2; Wikipédia 1-2, 2-1
- placar diferente na matriz da Wikipédia — Dundee x St Mirren: ogol 1-2, 3-1; Wikipédia 1-2, 3-3
- placar diferente na matriz da Wikipédia — St Mirren x Motherwell: ogol 0-0, 2-1; Wikipédia 0-0, 2-2
- placar corrigido pela matriz da Wikipédia: Dundee x Motherwell (1989-12-02) de 2-2 para 2-1 — junto com outros 2, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- placar corrigido pela matriz da Wikipédia: Dundee x St Mirren (1989-12-09) de 3-1 para 3-3 — junto com outros 2, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- placar corrigido pela matriz da Wikipédia: St Mirren x Motherwell (1989-11-04) de 2-1 para 2-2 — junto com outros 2, as tabelas publicadas fecham melhor (4 -> 0 linhas que não fecham)
- rebaixados: pela temporada seguinte ['Dundee']; caixa da Wikipédia []

### 1990/91

- placar diferente na matriz da Wikipédia — Hibernian x Dundee United: ogol 0-0, 1-0; Wikipédia 0-0, 3-0
- placar diferente na matriz da Wikipédia — Hibernian x Dunfermline: ogol 1-1, 3-0; Wikipédia 1-0, 1-1

### 1991/92

- placar diferente na matriz da Wikipédia — Hearts x Falkirk: ogol 1-1, 2-0; Wikipédia 1-0, 2-0

### 1992/93

- placar diferente na matriz da Wikipédia — Dundee United x Aberdeen: ogol 1-4, 2-2; Wikipédia 2-2, 3-0
- placar diferente na matriz da Wikipédia — Dundee United x Airdrieonians: ogol 0-0, 3-0; Wikipédia 0-0, 1-4
- placar diferente na matriz da Wikipédia — St Johnstone x Dundee: ogol 1-1, 4-4; Wikipédia 1-1, 4-0

### 1993/94

- sem ocorrências

### 1994/95

- placar diferente na matriz da Wikipédia — Celtic x Hearts: ogol 0-1, 1-1; Wikipédia 1-1, 3-0
- placar diferente na matriz da Wikipédia — Celtic x Hibernian: ogol 2-0, 2-2; Wikipédia 1-1, 3-0
- placar diferente na matriz da Wikipédia — Hearts x Celtic: ogol 1-0, 1-1; Wikipédia 0-1, 1-0
- placar diferente na matriz da Wikipédia — Hibernian x Celtic: ogol 1-1, 1-1; Wikipédia 0-2, 0-2

### 1995/96

- o Partick Thistle perdeu o play-off de rebaixamento e caiu; a caixa da Wikipédia lista só o Falkirk
- rebaixados: pela temporada seguinte ['Falkirk', 'Partick Thistle']; caixa da Wikipédia ['Falkirk']

### 1996/97

- resultado decidido fora de campo: Aberdeen x Dunfermline fica 3-0 (ogol DA) — derrota administrativa do Dunfermline, 3-0 (ficha do ogol); o football-data traz o mesmo 3-0
- placar diferente na matriz da Wikipédia — Dundee United x Motherwell: ogol 1-1, 2-0; Wikipédia 1-1, 2-2
- placar diferente na matriz da Wikipédia — Dunfermline x Celtic: ogol 0-2, 2-2; Wikipédia 0-2, 1-1
- placar diferente na matriz da Wikipédia — Dunfermline x Dundee United: ogol 1-1, 1-3; Wikipédia 1-1, 2-3

### 1997/98

- placar diferente na matriz da Wikipédia — Dundee United x Celtic: ogol 1-2, 1-2; Wikipédia 0-1, 1-2
- placar diferente na matriz da Wikipédia — Rangers x Hibernian: ogol 1-0, 3-0; Wikipédia 1-0, 1-0
- punição tirada da tabela da RSSSF: Dunfermline -1 pontos
- tabela publicada x jogos (Wikipédia) — Dunfermline tabela [36, 8, 13, 15, 43, 68, 37] jogos [36, 8, 13, 15, 43, 68, 36]
- a tabela da Wikipédia tem erro de digitação em alguma linha (gols ou V-E-D); a da RSSSF fecha com os jogos
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1998/99

- sem ocorrências

### 1999/00

- sem ocorrências

### 2000/01

- sem ocorrências

### 2001/02

- placar diferente na matriz da Wikipédia — Aberdeen x Dunfermline: ogol 1-0, 3-2; Wikipédia 3-2, 4-1
- placar diferente na matriz da Wikipédia — Aberdeen x Kilmarnock: ogol 1-1, 2-0; Wikipédia 1-0, 2-0

### 2002/03

- gols da ESPN não batem com o placar — Aberdeen 3-0 Dundee United: ESPN 4-0 (descartados)

### 2003/04

- placar diferente na matriz da Wikipédia — Dunfermline x Hearts: ogol 0-0, 0-1; Wikipédia 0-0, 2-1
- placar diferente na matriz da Wikipédia — Hearts x Dunfermline: ogol 1-2, 2-1; Wikipédia 1-0, 2-1
- mando corrigido: o ogol traz Dunfermline 0-1 Hearts (2003-08-31); o engsoccerdata traz Hearts x Dunfermline na mesma data
- placar diferente no engsoccerdata — Dunfermline x Hearts (2004-02-28): ogol 0-0, engsoccerdata 2-1
- jogo do engsoccerdata sem par no ogol: Dunfermline x Hearts (2004-02-28)
- placar diferente no engsoccerdata — Hearts x Rangers (2004-03-13): ogol 1-1, engsoccerdata 0-0
- placar diferente no football-data — Dunfermline x Hearts (2004-02-28): ogol 0-0, football-data 2-1
- jogo do football-data sem par no ogol: Dunfermline x Hearts (2004-02-28)
- placar diferente no football-data — Hearts x Rangers (2004-03-13): ogol 1-1, football-data 0-0
- jogo da ESPN sem par no ogol: Dunfermline Athletic 2-1 Heart of Midlothian (2003-12-06)
- ESPN com 227 de 228 jogos (ex. sem ESPN: Hearts x Dunfermline, 2003-12-06)

### 2004/05

- sem ocorrências

### 2005/06

- sem ocorrências

### 2006/07

- placar diferente na matriz da Wikipédia — Celtic x Hibernian: ogol 1-0, 2-1; Wikipédia 2-1, 2-1
- placar diferente na matriz da Wikipédia — Celtic x Kilmarnock: ogol 2-0, 4-1; Wikipédia 4-0, 4-1
- placar diferente na matriz da Wikipédia — Celtic x Motherwell: ogol 1-0, 2-1; Wikipédia 2-0, 2-1
- placar diferente na matriz da Wikipédia — Celtic x St Mirren: ogol 2-0, 5-1; Wikipédia 2-0, 3-1
- placar diferente na matriz da Wikipédia — Dundee United x Celtic: ogol 1-1, 1-4; Wikipédia 0-3, 1-4
- placar diferente na matriz da Wikipédia — Falkirk x St Mirren: ogol 0-2, 1-1, 2-0; Wikipédia 0-2, 1-1, 2-1
- placar diferente na matriz da Wikipédia — Hearts x Celtic: ogol 1-2, 2-1; Wikipédia 1-4, 2-1
- placar diferente na matriz da Wikipédia — Hearts x Hibernian: ogol 2-0, 3-2; Wikipédia 2-0, 3-1
- placar diferente na matriz da Wikipédia — Kilmarnock x Celtic: ogol 1-2, 1-2; Wikipédia 1-2, 1-3
- gols da ESPN não batem com o placar — Motherwell 0-2 Hearts: ESPN 0-3 (descartados)
- gols da ESPN não batem com o placar — Aberdeen 2-4 Dundee United: ESPN 2-5 (descartados)

### 2007/08

- gols da ESPN não batem com o placar — Hibernian 1-0 Inverness CT: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Inverness CT 3-2 Celtic: ESPN 3-3 (descartados)

### 2008/09

- sem ocorrências

### 2009/10

- placar diferente na matriz da Wikipédia — Celtic x Aberdeen: ogol 3-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Hearts x Hamilton Academical: ogol 2-0, 2-1; Wikipédia 0-2, 2-0

### 2010/11

- gols da ESPN não batem com o placar — Aberdeen 4-2 Hibernian: ESPN 5-2 (descartados)
- gols da ESPN não batem com o placar — Motherwell 1-2 Hearts: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — Rangers 0-2 Celtic: ESPN 0-3 (descartados)
- gols da ESPN não batem com o placar — Motherwell 2-0 Celtic: ESPN 3-0 (descartados)

### 2011/12

- gols da ESPN não batem com o placar — Rangers 5-0 Dundee United: ESPN 4-0 (descartados)

### 2012/13

- sem ocorrências

### 2013/14

- placar diferente na ESPN — Motherwell x Kilmarnock (2014-03-29): ogol 1-2, ESPN 1-1
- placar diferente na ESPN — Celtic x Aberdeen (2013-11-23): ogol 3-1, ESPN 2-1
- placar diferente na ESPN — Kilmarnock x Partick Thistle (2013-12-21): ogol 2-1, ESPN 1-0
- placar diferente na ESPN — St Johnstone x Partick Thistle (2014-03-29): ogol 1-1, ESPN 1-0
- placar diferente na ESPN — Inverness CT x Dundee United (2014-01-12): ogol 1-1, ESPN 1-0
- placar diferente na ESPN — Inverness CT x Motherwell (2013-08-17): ogol 2-0, ESPN 0-1
- placar diferente na ESPN — Motherwell x Inverness CT (2014-03-19): ogol 2-0, ESPN 2-1
- jogo da ESPN sem par no ogol: Inverness Caledonian Thistle 2-0 Motherwell (2013-08-17)
- jogo da ESPN sem par no ogol: Motherwell 2-0 Inverness Caledonian Thistle (2014-03-19)
- gols da ESPN não batem com o placar — Celtic 2-1 Ross County: ESPN 1-1 (descartados)
- gols da ESPN não batem com o placar — Inverness CT 2-0 Motherwell: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — Motherwell 2-0 Inverness CT: ESPN 2-1 (descartados)

### 2014/15

- jogo da ESPN sem par no ogol: Queen of the South 1-2 Rangers (2015-05-09)

### 2015/16

- jogo acrescentado: St Johnstone 0-0 Hamilton Academical (2016-01-16) — falta no calendário do ogol; o football-data, o engsoccerdata e a ESPN trazem 0-0 em 16/01/2016
- 3 jogos da ESPN com clube da 2ª divisão (play-off de rebaixamento): ficam de fora
- tabela publicada x jogos (RSSSF) — Dundee United tabela [38, 8, 7, 23, 45, 70, 31] jogos [38, 8, 7, 23, 45, 70, 28]
- a tabela da RSSSF tem erro de digitação em alguma linha (gols ou V-E-D); a da Wikipédia fecha com os jogos
- 1 jogos sem rodada no ogol (ex.: St Johnstone x Hamilton Academical)

### 2016/17

- placar diferente na matriz da Wikipédia — St Johnstone x Celtic: ogol 2-4, 2-5; Wikipédia 2-4
- matriz da Wikipédia com 227 placares (ogol 228 jogos)
- jogo da ESPN sem par no ogol: Dundee United 2-2 Falkirk (2017-05-16)
- jogo da ESPN sem par no ogol: Falkirk 1-2 Dundee United (2017-05-19)
- 1 jogos da ESPN com clube da 2ª divisão (play-off de rebaixamento): ficam de fora
- gols da ESPN não batem com o placar — Motherwell 1-3 Hearts: ESPN 1-4 (descartados)
- gols da ESPN não batem com o placar — Rangers 1-0 Inverness CT: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — St Johnstone 2-5 Celtic: ESPN 3-5 (descartados)
- gols da ESPN não batem com o placar — Ross County 1-2 St Johnstone: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — Aberdeen 1-0 Inverness CT: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Ross County 3-2 Hamilton Academical: ESPN 4-2 (descartados)

### 2017/18

- jogo da ESPN sem par no ogol: Partick Thistle 2-2 Rangers (2017-09-15)
- jogo da ESPN sem par no ogol: Heart of Midlothian 1-0 St Johnstone (2018-02-03)
- 2 jogos da ESPN com clube da 2ª divisão (play-off de rebaixamento): ficam de fora
- ESPN com 226 de 228 jogos (ex. sem ESPN: Partick Thistle x Rangers, 2017-09-19)
- gols da ESPN não batem com o placar — St Johnstone 1-0 Hamilton Academical: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Hamilton Academical 1-2 Kilmarnock: ESPN 2-2 (descartados)

### 2018/19

- 2 jogos da ESPN com clube da 2ª divisão (play-off de rebaixamento): ficam de fora

### 2019/20

- a ordem oficial é pela média de pontos por jogo (temporada interrompida)
- gols da ESPN não batem com o placar — St Johnstone 2-1 Motherwell: ESPN 3-2 (descartados)
- gols da ESPN não batem com o placar — Ross County 1-1 St Johnstone: ESPN 1-2 (descartados)
- gols da ESPN não batem com o placar — Aberdeen 1-2 Ross County: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — Hibernian 1-1 Livingston: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Celtic 3-1 Kilmarnock: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — St Johnstone 2-2 Rangers: ESPN 3-4 (descartados)
- gols da ESPN não batem com o placar — Hibernian 1-3 Hearts: ESPN 1-4 (descartados)
- gols da ESPN não batem com o placar — Rangers 0-1 Hamilton Academical: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Hearts 1-1 Motherwell: ESPN 1-2 (descartados)
- gols da ESPN não batem com o placar — St Mirren 1-0 Hearts: ESPN 2-0 (descartados)

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- sem ocorrências

### 2023/24

- ESPN com 52 de 228 jogos (ex. sem ESPN: Celtic x Ross County, 2023-08-05)

### 2024/25

- placar diferente na matriz da Wikipédia — Aberdeen x Celtic: ogol 0-1, 1-5; Wikipédia 1-5
- placar diferente na matriz da Wikipédia — Aberdeen x Hibernian: ogol 1-0, 1-3; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Celtic x Hibernian: ogol 3-0, 3-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Celtic x St Mirren: ogol 1-1, 3-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Dundee x Motherwell: ogol 1-2, 4-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Dundee x Ross County: ogol 0-3, 1-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Dundee United x Aberdeen: ogol 1-0, 2-1; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Dundee United x Celtic: ogol 0-0, 0-5; Wikipédia 0-5
- placar diferente na matriz da Wikipédia — Dundee United x St Mirren: ogol 0-2, 2-0; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Hearts x Dundee: ogol 0-1, 2-0; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Hearts x Motherwell: ogol 1-0, 3-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Hearts x St Johnstone: ogol 2-1, 2-1; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Hibernian x Dundee United: ogol 1-1, 3-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Hibernian x Rangers: ogol 2-2, 3-3; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Kilmarnock x Dundee: ogol 1-1, 3-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Kilmarnock x Hearts: ogol 0-1, 1-0; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Kilmarnock x Ross County: ogol 0-1, 2-0; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Motherwell x Kilmarnock: ogol 1-1, 3-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Motherwell x St Johnstone: ogol 2-1, 3-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Rangers x Aberdeen: ogol 3-0, 4-0; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — Rangers x Celtic: ogol 1-1, 3-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Rangers x Dundee United: ogol 1-1, 3-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Ross County x Hearts: ogol 1-3, 2-2; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Ross County x Motherwell: ogol 1-1, 2-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — St Johnstone x Dundee: ogol 0-2, 1-3; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — St Johnstone x Kilmarnock: ogol 0-2, 1-0; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — St Johnstone x Ross County: ogol 1-0, 2-1, 3-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — St Mirren x Aberdeen: ogol 1-0, 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — St Mirren x Hibernian: ogol 0-0, 2-2, 3-0; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — St Mirren x Rangers: ogol 2-1, 2-2; Wikipédia 2-2
- matriz da Wikipédia com 30 placares (ogol 228 jogos)

### 2025/26

- placar diferente na matriz da Wikipédia — Aberdeen x Dundee United: ogol 1-1, 2-0; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Aberdeen x Kilmarnock: ogol 1-0, 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Aberdeen x St Mirren: ogol 0-2, 3-3; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Celtic x Falkirk: ogol 2-0, 3-1, 4-0; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Celtic x Rangers: ogol 1-3, 3-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Dundee x Aberdeen: ogol 1-3, 3-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Dundee x Livingston: ogol 2-2, 3-0, 3-2; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Dundee x St Mirren: ogol 1-0, 3-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Dundee United x Dundee: ogol 0-1, 3-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Dundee United x Livingston: ogol 0-0, 1-1, 3-2; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Falkirk x Hibernian: ogol 1-3, 2-2, 4-1; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Falkirk x Motherwell: ogol 0-0, 1-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Hearts x Falkirk: ogol 1-0, 3-0, 3-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Hearts x Rangers: ogol 2-1, 2-1; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Hibernian x Celtic: ogol 1-2, 1-2; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Hibernian x Hearts: ogol 1-2, 3-2; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Kilmarnock x Dundee: ogol 0-0, 2-2, 3-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Kilmarnock x Dundee United: ogol 1-1, 3-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Livingston x Aberdeen: ogol 0-1, 2-2; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Livingston x Kilmarnock: ogol 1-1, 1-4; Wikipédia 1-4
- placar diferente na matriz da Wikipédia — Motherwell x Celtic: ogol 2-0, 2-3; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — Motherwell x Hearts: ogol 0-0, 1-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Rangers x Hibernian: ogol 1-0, 1-2; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Rangers x Motherwell: ogol 1-0, 2-3; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — St Mirren x Dundee United: ogol 1-1, 2-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — St Mirren x Kilmarnock: ogol 0-0, 0-3; Wikipédia 0-3
- placar diferente na matriz da Wikipédia — St Mirren x Livingston: ogol 0-2, 1-0; Wikipédia 0-2
- matriz da Wikipédia com 27 placares (ogol 228 jogos)
- gols da ESPN não batem com o placar — Aberdeen 1-2 Celtic: ESPN 0-1 (descartados)

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_sco.py` (serve para todas as divisões escocesas): nome de exibição como o clube é conhecido no Brasil, cidade e país (Escócia, `SCO`, em `paises.csv`). O Rangers é um clube só, também depois da liquidação da empresa em 2012, como na liga e na lista oficial de campeões.
- O ogol entra pelo código do clube (tabela `OGOL` do cadastro); a ESPN é casada por votação jogo a jogo (mesma data e placar): 20 códigos.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.
- **Público e estádio antes da ESPN:** nenhuma fonte em lote.
- **Play-offs de rebaixamento (contra clubes da 2ª divisão) e jogos de desempate pelo título (1890/91, 1904/05):** ficam de fora.
- **Ligas de guerra (1939/40-1945/46):** não oficiais; ficam de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
