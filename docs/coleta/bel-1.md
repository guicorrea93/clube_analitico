# Campeonato Belga (1ª divisão) — coleta de dados

Gerado por `python coleta/bel-1/importar.py`. Pacote em `data/coleta/bel-1/pacote/`.

**Edições:** 123, de 1895/96 a 2025/26. Sem 1914/15-1918/19, 1939/40-1940/41 e 1944/45 (guerras).

**Total:** 28712 jogos, 90510 gols, 12031 gols com autor (ESPN), 18167 cartões, 81 clubes.

**Fontes:**
- Wikipédia (en): matriz de resultados (base dos jogos até 1959/60, sem data), tabelas da fase regular e dos play-offs (com o ponto de partida dos play-offs) e conferência jogo a jogo depois;
- ogol (zerozero): base dos jogos de 1960/61 em diante, com data e rodada; o clube pelo código do ogol (os nomes do calendário não são confiáveis); calendários em `data/cache/ogol-bel-1/` para os escudos;
- RSSSF: tabelas finais de 1895/96 a 2007/08 (belghist.html; de 1898/99 a 1903/04, grupos e torneio final), lista de campeões e de artilheiros (desde 1945/46);
- engsoccerdata e football-data: conferência de placar de 1995/96 em diante; hora e estatísticas do football-data;
- ESPN (liga `bel.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). Nos play-offs (2009/10+), a classificação final é a do play-off do título, depois os outros clubes pela fase regular e o play-off de rebaixamento; os pontos são os oficiais (a metade da fase regular, arredondada para cima, mais os do play-off) e a diferença para a soma de todos os jogos fica em `ajuste_pontos`. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (vitórias em 90, saldo em 17, confronto direto em 5, média de gols em 6).

| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1895/96 | Wikipédia + RSSSF | 7 | 42 | 211 | 0 | 0 / 2 | RFC Liège | — |
| 1896/97 | Wikipédia + RSSSF | 6 | 30 | 154 | 0 | 1 / 1 | Racing Club de Bruxelles | — |
| 1897/98 | Wikipédia + RSSSF | 5 | 19 | 92 | 0 | 0 / 2 | RFC Liège | — |
| 1898/99 | RSSSF | 9 | 2 | 9 | 0 | 0 / 0 | RFC Liège | — |
| 1899/00 | RSSSF | 10 | 3 | 13 | 0 | 0 / 0 | Racing Club de Bruxelles | — |
| 1900/01 | Wikipédia + RSSSF | 9 | 72 | 310 | 0 | 0 / 2 | Racing Club de Bruxelles | — |
| 1901/02 | RSSSF | 11 | 1 | 7 | 0 | 0 / 0 | Racing Club de Bruxelles | — |
| 1902/03 | RSSSF | 10 | 1 | 5 | 0 | 0 / 0 | Racing Club de Bruxelles | — |
| 1903/04 | RSSSF | 12 | 0 | 0 | 0 | 0 / 0 | Union Saint-Gilloise | — |
| 1904/05 | Wikipédia + RSSSF | 11 | 109 | 511 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1905/06 | Wikipédia + RSSSF | 10 | 90 | 412 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1906/07 | Wikipédia + RSSSF | 10 | 90 | 391 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1907/08 | Wikipédia + RSSSF | 10 | 89 | 429 | 0 | 0 / 2 | Racing Club de Bruxelles | — |
| 1908/09 | Wikipédia + RSSSF | 12 | 132 | 592 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1909/10 | Wikipédia + RSSSF | 12 | 132 | 540 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1910/11 | Wikipédia + RSSSF | 12 | 132 | 567 | 0 | 0 / 2 | Cercle Brugge | — |
| 1911/12 | Wikipédia + RSSSF | 12 | 132 | 516 | 0 | 0 / 2 | Daring Club de Bruxelles | — |
| 1912/13 | Wikipédia + RSSSF | 12 | 132 | 537 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1913/14 | Wikipédia + RSSSF | 12 | 132 | 492 | 0 | 0 / 2 | Daring Club de Bruxelles | — |
| 1919/20 | Wikipédia + RSSSF | 12 | 132 | 518 | 0 | 0 / 2 | Club Brugge | — |
| 1920/21 | Wikipédia + RSSSF | 12 | 132 | 428 | 0 | 2 / 0 | Daring Club de Bruxelles | — |
| 1921/22 | Wikipédia + RSSSF | 14 | 182 | 542 | 0 | 0 / 2 | Beerschot VAC | — |
| 1922/23 | Wikipédia + RSSSF | 14 | 182 | 623 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1923/24 | Wikipédia + RSSSF | 14 | 182 | 523 | 0 | 0 / 2 | Beerschot VAC | — |
| 1924/25 | Wikipédia + RSSSF | 14 | 182 | 479 | 0 | 0 / 2 | Beerschot VAC | — |
| 1925/26 | Wikipédia + RSSSF | 14 | 182 | 776 | 0 | 2 / 0 | Beerschot VAC | — |
| 1926/27 | Wikipédia + RSSSF | 14 | 182 | 754 | 0 | 0 / 2 | Cercle Brugge | — |
| 1927/28 | Wikipédia + RSSSF | 14 | 182 | 791 | 0 | 0 / 2 | Beerschot VAC | — |
| 1928/29 | Wikipédia + RSSSF | 14 | 182 | 696 | 0 | 0 / 2 | Antwerp | — |
| 1929/30 | Wikipédia + RSSSF | 14 | 182 | 716 | 0 | 2 / 0 | Cercle Brugge | — |
| 1930/31 | Wikipédia + RSSSF | 14 | 182 | 745 | 0 | 2 / 0 | Antwerp | — |
| 1931/32 | Wikipédia + RSSSF | 14 | 182 | 800 | 0 | 2 / 0 | Lierse | — |
| 1932/33 | Wikipédia + RSSSF | 14 | 182 | 720 | 0 | 2 / 0 | Union Saint-Gilloise | — |
| 1933/34 | Wikipédia + RSSSF | 14 | 182 | 856 | 0 | 0 / 2 | Union Saint-Gilloise | — |
| 1934/35 | Wikipédia + RSSSF | 14 | 182 | 840 | 0 | 2 / 0 | Union Saint-Gilloise | — |
| 1935/36 | Wikipédia + RSSSF | 14 | 182 | 772 | 0 | 2 / 0 | Daring Club de Bruxelles | — |
| 1936/37 | Wikipédia + RSSSF | 14 | 182 | 742 | 0 | 2 / 0 | Daring Club de Bruxelles | — |
| 1937/38 | Wikipédia + RSSSF | 14 | 182 | 745 | 0 | 2 / 0 | Beerschot VAC | — |
| 1938/39 | Wikipédia + RSSSF | 14 | 182 | 703 | 0 | 0 / 2 | Beerschot VAC | — |
| 1941/42 | Wikipédia + RSSSF | 14 | 182 | 789 | 0 | 2 / 0 | Lierse | — |
| 1942/43 | Wikipédia + RSSSF | 16 | 240 | 972 | 0 | 0 / 2 | KV Mechelen | — |
| 1943/44 | Wikipédia + RSSSF | 16 | 239 | 978 | 0 | 1 / 1 | Antwerp | — |
| 1945/46 | Wikipédia + RSSSF | 19 | 342 | 1341 | 0 | 2 / 0 | KV Mechelen | — |
| 1946/47 | Wikipédia + RSSSF | 19 | 342 | 1394 | 0 | 0 / 2 | Anderlecht | — |
| 1947/48 | Wikipédia + RSSSF | 16 | 240 | 927 | 0 | 0 / 2 | KV Mechelen | — |
| 1948/49 | Wikipédia + RSSSF | 16 | 240 | 842 | 0 | 0 / 2 | Anderlecht | — |
| 1949/50 | Wikipédia + RSSSF | 16 | 240 | 916 | 0 | 0 / 2 | Anderlecht | — |
| 1950/51 | Wikipédia + RSSSF | 16 | 240 | 821 | 0 | 0 / 2 | Anderlecht | — |
| 1951/52 | Wikipédia + RSSSF | 16 | 240 | 873 | 0 | 1 / 1 | RFC Liège | — |
| 1952/53 | Wikipédia + RSSSF | 16 | 240 | 824 | 0 | 0 / 2 | RFC Liège | — |
| 1953/54 | Wikipédia + RSSSF | 16 | 240 | 822 | 0 | 2 / 0 | Anderlecht | — |
| 1954/55 | Wikipédia + RSSSF | 16 | 232 | 862 | 0 | 0 / 2 | Anderlecht | — |
| 1955/56 | Wikipédia + RSSSF | 16 | 240 | 842 | 0 | 0 / 2 | Anderlecht | — |
| 1956/57 | Wikipédia + RSSSF | 16 | 240 | 842 | 0 | 2 / 0 | Antwerp | — |
| 1957/58 | Wikipédia + RSSSF | 16 | 240 | 779 | 0 | 0 / 2 | Standard Liège | — |
| 1958/59 | Wikipédia + RSSSF | 16 | 240 | 838 | 0 | 2 / 0 | Anderlecht | — |
| 1959/60 | Wikipédia + RSSSF | 16 | 240 | 753 | 0 | 2 / 0 | Lierse | — |
| 1960/61 | ogol + RSSSF + Wikipédia | 16 | 240 | 696 | 0 | 2 / 0 | Standard Liège | — |
| 1961/62 | ogol + RSSSF + Wikipédia | 16 | 240 | 712 | 0 | 2 / 0 | Anderlecht | — |
| 1962/63 | ogol + RSSSF + Wikipédia | 16 | 240 | 640 | 0 | 2 / 0 | Standard Liège | — |
| 1963/64 | ogol + RSSSF + Wikipédia | 16 | 240 | 645 | 0 | 2 / 0 | Anderlecht | — |
| 1964/65 | ogol + RSSSF + Wikipédia | 16 | 240 | 727 | 0 | 2 / 0 | Anderlecht | — |
| 1965/66 | ogol + RSSSF + Wikipédia | 16 | 240 | 649 | 0 | 2 / 0 | Anderlecht | — |
| 1966/67 | ogol + RSSSF + Wikipédia | 16 | 240 | 648 | 0 | 2 / 0 | Anderlecht | — |
| 1967/68 | ogol + RSSSF + Wikipédia | 16 | 240 | 660 | 0 | 2 / 0 | Anderlecht | — |
| 1968/69 | ogol + RSSSF + Wikipédia | 16 | 240 | 663 | 0 | 2 / 0 | Standard Liège | — |
| 1969/70 | ogol + RSSSF + Wikipédia | 16 | 240 | 667 | 0 | 2 / 0 | Standard Liège | — |
| 1970/71 | ogol + RSSSF + Wikipédia | 16 | 240 | 613 | 0 | 1 / 1 | Standard Liège | — |
| 1971/72 | ogol + RSSSF + Wikipédia | 16 | 240 | 573 | 0 | 2 / 0 | Anderlecht | — |
| 1972/73 | ogol + RSSSF + Wikipédia | 16 | 240 | 574 | 0 | 2 / 0 | Club Brugge | — |
| 1973/74 | ogol + RSSSF + Wikipédia | 16 | 240 | 665 | 0 | 1 / 1 | Anderlecht | — |
| 1974/75 | ogol + RSSSF + Wikipédia | 20 | 380 | 1001 | 0 | 2 / 0 | RWD Molenbeek | — |
| 1975/76 | ogol + RSSSF + Wikipédia | 19 | 342 | 929 | 0 | 2 / 0 | Club Brugge | — |
| 1976/77 | ogol + RSSSF + Wikipédia | 18 | 306 | 871 | 0 | 2 / 0 | Club Brugge | — |
| 1977/78 | ogol + RSSSF + Wikipédia | 18 | 306 | 864 | 0 | 2 / 0 | Club Brugge | — |
| 1978/79 | ogol + RSSSF + Wikipédia | 18 | 306 | 833 | 0 | 2 / 0 | KSK Beveren | — |
| 1979/80 | ogol + RSSSF + Wikipédia | 18 | 306 | 863 | 0 | 2 / 0 | Club Brugge | — |
| 1980/81 | ogol + RSSSF + Wikipédia | 18 | 306 | 934 | 0 | 2 / 0 | Anderlecht | — |
| 1981/82 | ogol + RSSSF + Wikipédia | 18 | 306 | 766 | 0 | 0 / 2 | Standard Liège | — |
| 1982/83 | ogol + RSSSF + Wikipédia | 18 | 306 | 861 | 0 | 2 / 0 | Standard Liège | — |
| 1983/84 | ogol + RSSSF + Wikipédia | 18 | 306 | 862 | 0 | 2 / 0 | KSK Beveren | — |
| 1984/85 | ogol + RSSSF + Wikipédia | 18 | 306 | 904 | 0 | 1 / 1 | Anderlecht | — |
| 1985/86 | ogol + RSSSF + Wikipédia | 18 | 306 | 826 | 0 | 1 / 1 | Anderlecht | — |
| 1986/87 | ogol + RSSSF + Wikipédia | 18 | 306 | 788 | 0 | 1 / 1 | Anderlecht | — |
| 1987/88 | ogol + RSSSF + Wikipédia | 18 | 306 | 805 | 0 | 2 / 0 | Club Brugge | — |
| 1988/89 | ogol + RSSSF + Wikipédia | 18 | 306 | 845 | 0 | 2 / 0 | KV Mechelen | — |
| 1989/90 | ogol + RSSSF + Wikipédia | 18 | 306 | 809 | 0 | 2 / 0 | Club Brugge | — |
| 1990/91 | ogol + RSSSF + Wikipédia | 18 | 306 | 814 | 0 | 2 / 0 | Anderlecht | — |
| 1991/92 | ogol + RSSSF + Wikipédia | 18 | 306 | 815 | 0 | 2 / 0 | Club Brugge | — |
| 1992/93 | ogol + RSSSF + Wikipédia | 18 | 306 | 947 | 0 | 2 / 0 | Anderlecht | — |
| 1993/94 | ogol + RSSSF + Wikipédia | 18 | 306 | 816 | 0 | 2 / 0 | Anderlecht | — |
| 1994/95 | ogol + RSSSF + Wikipédia | 18 | 306 | 844 | 0 | 2 / 0 | Anderlecht | — |
| 1995/96 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 870 | 0 | 0 / 2 | Club Brugge | — |
| 1996/97 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 889 | 0 | 2 / 0 | Lierse | — |
| 1997/98 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 904 | 0 | 2 / 0 | Club Brugge | — |
| 1998/99 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 972 | 0 | 2 / 0 | Genk | — |
| 1999/00 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 1037 | 0 | 1 / 1 | Anderlecht | — |
| 2000/01 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 940 | 0 | 2 / 0 | Anderlecht | — |
| 2001/02 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 978 | 0 | 2 / 0 | Genk | — |
| 2002/03 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 17 | 272 | 888 | 0 | 2 / 0 | Club Brugge | — |
| 2003/04 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 824 | 0 | 2 / 0 | Anderlecht | — |
| 2004/05 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 850 | 0 | 2 / 0 | Club Brugge | — |
| 2005/06 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 778 | 0 | 1 / 1 | Anderlecht | — |
| 2006/07 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 853 | 706 | 2 / 0 | Anderlecht | — |
| 2007/08 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 795 | 757 | 2 / 0 | Standard Liège | — |
| 2008/09 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 308 | 858 | 836 | 1 / 0 | Standard Liège | — |
| 2009/10 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 15 | 268 | 736 | 541 | 4 / 0 | Anderlecht | — |
| 2010/11 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 300 | 798 | 616 | 5 / 0 | Genk | — |
| 2011/12 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 302 | 893 | 0 | 5 / 0 | Anderlecht | — |
| 2012/13 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 302 | 880 | 0 | 3 / 2 | Anderlecht | — |
| 2013/14 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 299 | 814 | 3 | 5 / 0 | Anderlecht | — |
| 2014/15 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 302 | 862 | 16 | 5 / 0 | Gent | — |
| 2015/16 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 298 | 866 | 672 | 4 / 0 | Club Brugge | — |
| 2016/17 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 332 | 945 | 616 | 4 / 0 | Anderlecht | Standard Liège -3 pontos |
| 2017/18 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 331 | 974 | 649 | 4 / 0 | Club Brugge | — |
| 2018/19 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 332 | 994 | 696 | 4 / 0 | Genk | — |
| 2019/20 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 232 | 655 | 646 | 0 / 1 | Club Brugge | — |
| 2020/21 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 330 | 1002 | 907 | 3 / 0 | Club Brugge | — |
| 2021/22 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 330 | 959 | 890 | 3 / 0 | Club Brugge | — |
| 2022/23 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 330 | 1011 | 919 | 3 / 0 | Antwerp | — |
| 2023/24 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 313 | 884 | 877 | 4 / 0 | Club Brugge | — |
| 2024/25 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 313 | 863 | 849 | 4 / 0 | Union Saint-Gilloise | — |
| 2025/26 | ogol + football-data + ESPN + Wikipédia | 16 | 313 | 837 | 835 | 4 / 0 | Club Brugge | — |

## Conferência e ocorrências, temporada a temporada

### 1895/96

- tabela publicada x jogos (RSSSF) — RFC Liège tabela [12, 9, 2, 1, 32, 11, 20] jogos [12, 9, 2, 1, 47, 11, 20]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [12, 7, 0, 5, 33, 13, 14] jogos [12, 7, 0, 5, 38, 18, 14]
- tabela publicada x jogos (RSSSF) — Sporting Club de Bruxelles tabela [12, 6, 1, 5, 31, 29, 13] jogos [12, 6, 1, 5, 31, 35, 13]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [12, 6, 0, 6, 31, 29, 12] jogos [12, 6, 0, 6, 31, 34, 12]
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [12, 6, 0, 6, 32, 31, 12] jogos [12, 5, 1, 6, 32, 31, 11]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [12, 5, 1, 6, 22, 21, 11] jogos [12, 5, 2, 5, 27, 21, 12]
- tabela publicada x jogos (RSSSF) — Union d'Ixelles tabela [12, 1, 0, 11, 5, 51, 2] jogos [12, 1, 0, 11, 5, 61, 2]
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [12, 9, 2, 1, 32, 11, 20] jogos [12, 9, 2, 1, 47, 11, 20]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [12, 7, 0, 5, 33, 13, 14] jogos [12, 7, 0, 5, 38, 18, 14]
- tabela publicada x jogos (Wikipédia) — Sporting Club de Bruxelles tabela [12, 6, 1, 5, 31, 29, 13] jogos [12, 6, 1, 5, 31, 35, 13]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [12, 6, 0, 6, 31, 29, 12] jogos [12, 6, 0, 6, 31, 34, 12]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [12, 6, 0, 6, 32, 31, 12] jogos [12, 5, 1, 6, 32, 31, 11]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [12, 5, 1, 6, 22, 21, 11] jogos [12, 5, 2, 5, 27, 21, 12]
- tabela publicada x jogos (Wikipédia) — Union d'Ixelles tabela [12, 1, 0, 11, 5, 51, 2] jogos [12, 1, 0, 11, 5, 61, 2]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Racing Club de Bruxelles', 'Club Brugge'])

### 1896/97

- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [10, 8, 2, 0, 40, 10, 18] jogos [10, 8, 2, 0, 45, 10, 18]
- tabela publicada x jogos (RSSSF) — RFC Liège tabela [10, 6, 2, 2, 16, 13, 14] jogos [10, 6, 2, 2, 31, 13, 14]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [10, 6, 1, 3, 22, 10, 13] jogos [10, 6, 1, 3, 27, 10, 13]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [10, 4, 0, 6, 9, 28, 8] jogos [10, 4, 0, 6, 24, 33, 8]
- tabela publicada x jogos (RSSSF) — Athletic & Running Club de Bruxelles tabela [10, 3, 1, 6, 25, 14, 7] jogos [10, 3, 1, 6, 25, 24, 7]
- tabela publicada x jogos (RSSSF) — Sporting Club de Bruxelles tabela [10, 0, 0, 10, 2, 39, 0] jogos [10, 0, 0, 10, 2, 64, 0]

### 1897/98

- fase regular com 19 jogos de 20
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [8, 4, 2, 2, 18, 7, 10] jogos [8, 4, 2, 2, 29, 9, 10]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [8, 2, 4, 2, 17, 23, 8] jogos [7, 2, 3, 2, 15, 13, 7]
- tabela publicada x jogos (RSSSF) — Athletic & Running Club de Bruxelles tabela [8, 2, 2, 4, 11, 17, 6] jogos [8, 2, 1, 5, 11, 36, 5]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [8, 1, 0, 7, 7, 31, 2] jogos [7, 1, 0, 6, 7, 29, 2]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [8, 4, 2, 2, 18, 7, 10] jogos [8, 4, 2, 2, 29, 9, 10]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [8, 2, 4, 2, 17, 23, 8] jogos [7, 2, 3, 2, 15, 13, 7]
- tabela publicada x jogos (Wikipédia) — Athletic & Running Club de Bruxelles tabela [8, 2, 2, 4, 11, 17, 6] jogos [8, 2, 1, 5, 11, 36, 5]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [8, 1, 0, 7, 7, 31, 2] jogos [7, 1, 0, 6, 7, 29, 2]

### 1898/99

- temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio final) e os jogos finais e de desempate listados nas notas
- nota da RSSSF: (no official final table known at this moment)
- nota da RSSSF: (and uncertainty about participating teams)
- nota da RSSSF: Skill FC Bruxelles was admitted to the league

### 1899/00

- temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio final) e os jogos finais e de desempate listados nas notas
- nota da RSSSF: (no official final table known at this moment)
- nota da RSSSF: For the new season there will be only one division
- nota da RSSSF: Antwerp FC withdrew from the league, 3 new clubs were admitted

### 1900/01

- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [16, 10, 6, 0, 44, 11, 26] jogos [16, 10, 6, 0, 54, 11, 26]
- tabela publicada x jogos (RSSSF) — Beerschot VAC tabela [16, 11, 3, 2, 47, 21, 25] jogos [16, 11, 3, 2, 52, 21, 25]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [16, 10, 3, 3, 37, 20, 23] jogos [16, 10, 3, 3, 42, 20, 23]
- tabela publicada x jogos (RSSSF) — Athletic & Running Club de Bruxelles tabela [16, 7, 4, 5, 39, 26, 18] jogos [16, 7, 4, 5, 44, 26, 18]
- tabela publicada x jogos (RSSSF) — Skill FC de Bruxelles tabela [16, 5, 3, 8, 36, 30, 13] jogos [16, 5, 3, 8, 41, 40, 13]
- tabela publicada x jogos (RSSSF) — RFC Liège tabela [16, 5, 3, 8, 21, 29, 13] jogos [16, 5, 3, 8, 22, 45, 13]
- tabela publicada x jogos (RSSSF) — CS Verviétois tabela [16, 6, 0, 10, 19, 43, 12] jogos [16, 6, 0, 10, 24, 49, 12]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [16, 2, 4, 10, 10, 45, 8] jogos [16, 2, 4, 10, 15, 45, 8]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [16, 10, 6, 0, 44, 11, 26] jogos [16, 10, 6, 0, 54, 11, 26]
- tabela publicada x jogos (Wikipédia) — Beerschot VAC tabela [16, 11, 3, 2, 47, 21, 25] jogos [16, 11, 3, 2, 52, 21, 25]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [16, 10, 3, 3, 37, 20, 23] jogos [16, 10, 3, 3, 42, 20, 23]
- tabela publicada x jogos (Wikipédia) — Athletic & Running Club de Bruxelles tabela [16, 7, 4, 5, 39, 26, 18] jogos [16, 7, 4, 5, 44, 26, 18]
- tabela publicada x jogos (Wikipédia) — Skill FC de Bruxelles tabela [16, 5, 3, 8, 36, 30, 13] jogos [16, 5, 3, 8, 41, 40, 13]
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [16, 5, 3, 8, 21, 29, 13] jogos [16, 5, 3, 8, 22, 45, 13]
- tabela publicada x jogos (Wikipédia) — CS Verviétois tabela [16, 6, 0, 10, 19, 43, 12] jogos [16, 6, 0, 10, 24, 49, 12]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [16, 2, 4, 10, 10, 45, 8] jogos [16, 2, 4, 10, 15, 45, 8]

### 1901/02

- temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio final) e os jogos finais e de desempate listados nas notas
- nota da RSSSF: Skill FC  Bruxelles withdrew

### 1902/03

- temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio final) e os jogos finais e de desempate listados nas notas
- nota da RSSSF: Olympia Club de Bruxelles and Daring Club de Bruxelles were admitted
- nota da RSSSF: to the league
- nota da RSSSF: Verviers FC changed their name in CS Verviétois

### 1903/04

- temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio final) e os jogos finais e de desempate listados nas notas
- nota da RSSSF: Olympia Club de Bruxelles withdrew, only one first division next season

### 1904/05

- fase regular com 109 jogos de 110
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [20, 13, 4, 3, 76, 25, 30] jogos [20, 13, 4, 3, 79, 27, 30]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [20, 13, 2, 5, 63, 26, 28] jogos [20, 13, 2, 5, 62, 24, 28]
- tabela publicada x jogos (RSSSF) — RFC Liège tabela [20, 13, 1, 6, 48, 29, 27] jogos [20, 13, 1, 6, 48, 27, 27]
- tabela publicada x jogos (RSSSF) — Daring Club de Bruxelles tabela [19, 10, 2, 7, 42, 33, 22] jogos [20, 11, 2, 7, 42, 33, 24]
- tabela publicada x jogos (RSSSF) — CS Verviétois tabela [19, 8, 0, 11, 43, 63, 16] jogos [20, 8, 0, 12, 43, 68, 16]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [19, 6, 3, 10, 33, 40, 15] jogos [19, 6, 3, 10, 33, 44, 15]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [19, 5, 2, 12, 35, 60, 12] jogos [20, 6, 2, 12, 40, 60, 14]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [18, 4, 1, 13, 28, 56, 9] jogos [19, 4, 1, 14, 28, 57, 9]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [20, 13, 4, 3, 76, 25, 30] jogos [20, 13, 4, 3, 79, 27, 30]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [20, 13, 2, 5, 63, 26, 28] jogos [20, 13, 2, 5, 62, 24, 28]
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [20, 13, 1, 6, 48, 29, 27] jogos [20, 13, 1, 6, 48, 27, 27]
- tabela publicada x jogos (Wikipédia) — Daring Club de Bruxelles tabela [19, 10, 2, 7, 42, 33, 22] jogos [20, 11, 2, 7, 42, 33, 24]
- tabela publicada x jogos (Wikipédia) — CS Verviétois tabela [19, 8, 0, 11, 43, 63, 16] jogos [20, 8, 0, 12, 43, 68, 16]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [19, 6, 3, 10, 33, 40, 15] jogos [19, 6, 3, 10, 33, 44, 15]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [19, 5, 2, 12, 35, 60, 12] jogos [20, 6, 2, 12, 40, 60, 14]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [18, 4, 1, 13, 28, 56, 9] jogos [19, 4, 1, 14, 28, 57, 9]

### 1905/06

- tabela publicada x jogos (RSSSF) — Léopold Club tabela [18, 7, 2, 9, 38, 52, 16] jogos [18, 7, 2, 9, 40, 52, 16]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [18, 4, 4, 10, 30, 45, 12] jogos [18, 4, 4, 10, 30, 47, 12]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [18, 7, 2, 9, 38, 52, 16] jogos [18, 7, 2, 9, 40, 52, 16]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [18, 4, 4, 10, 30, 45, 12] jogos [18, 4, 4, 10, 30, 47, 12]

### 1906/07

- tabela publicada x jogos (RSSSF) — Daring Club de Bruxelles tabela [18, 10, 3, 5, 47, 18, 23] jogos [18, 10, 3, 5, 47, 20, 23]
- tabela publicada x jogos (RSSSF) — Kortrijk tabela [18, 4, 2, 12, 29, 61, 10] jogos [18, 4, 2, 12, 29, 65, 10]
- tabela publicada x jogos (RSSSF) — RFC Liège tabela [18, 5, 0, 13, 25, 65, 10] jogos [18, 5, 0, 13, 25, 63, 10]
- tabela publicada x jogos (RSSSF) — CS Verviétois tabela [18, 3, 0, 15, 32, 77, 6] jogos [18, 3, 0, 15, 21, 77, 6]
- tabela publicada x jogos (Wikipédia) — Daring Club de Bruxelles tabela [18, 10, 3, 5, 47, 18, 23] jogos [18, 10, 3, 5, 47, 20, 23]
- tabela publicada x jogos (Wikipédia) — Kortrijk tabela [18, 4, 2, 12, 29, 61, 10] jogos [18, 4, 2, 12, 29, 65, 10]
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [18, 5, 0, 13, 25, 65, 10] jogos [18, 5, 0, 13, 25, 63, 10]
- tabela publicada x jogos (Wikipédia) — CS Verviétois tabela [18, 3, 0, 15, 32, 77, 6] jogos [18, 3, 0, 15, 21, 77, 6]

### 1907/08

- fase regular com 89 jogos de 90
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [18, 12, 2, 4, 58, 26, 26] jogos [17, 12, 2, 3, 58, 26, 26]
- tabela publicada x jogos (RSSSF) — Daring Club de Bruxelles tabela [18, 9, 0, 9, 58, 35, 18] jogos [18, 9, 0, 9, 58, 34, 18]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [18, 8, 2, 8, 30, 42, 18] jogos [17, 8, 2, 7, 30, 42, 18]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [18, 2, 2, 14, 23, 57, 6] jogos [18, 2, 2, 14, 22, 57, 6]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [18, 12, 2, 4, 58, 26, 26] jogos [17, 12, 2, 3, 58, 26, 26]
- tabela publicada x jogos (Wikipédia) — Daring Club de Bruxelles tabela [18, 9, 0, 9, 58, 35, 18] jogos [18, 9, 0, 9, 58, 34, 18]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [18, 8, 2, 8, 30, 42, 18] jogos [17, 8, 2, 7, 30, 42, 18]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [18, 2, 2, 14, 23, 57, 6] jogos [18, 2, 2, 14, 22, 57, 6]

### 1908/09

- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [22, 11, 0, 11, 57, 45, 22] jogos [22, 10, 0, 12, 57, 45, 20]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [22, 7, 1, 14, 48, 57, 15] jogos [22, 9, 1, 12, 48, 57, 19]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [22, 3, 5, 14, 30, 70, 11] jogos [22, 2, 6, 14, 30, 70, 10]
- tabela publicada x jogos (RSSSF) — Racing Gent tabela [22, 2, 3, 17, 19, 78, 7] jogos [22, 2, 4, 16, 19, 78, 8]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [22, 11, 0, 11, 57, 45, 22] jogos [22, 10, 0, 12, 57, 45, 20]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [22, 7, 1, 14, 48, 57, 15] jogos [22, 9, 1, 12, 48, 57, 19]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [22, 3, 5, 14, 30, 70, 11] jogos [22, 2, 6, 14, 30, 70, 10]
- tabela publicada x jogos (Wikipédia) — Racing Gent tabela [22, 2, 3, 17, 19, 78, 7] jogos [22, 2, 4, 16, 19, 78, 8]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 4 posições (ex.: ['Cercle Brugge', 'Excelsior SC de Bruxelles'])

### 1909/10

- tabela publicada x jogos (RSSSF) — Excelsior SC de Bruxelles tabela [22, 8, 3, 11, 48, 44, 19] jogos [22, 8, 3, 11, 48, 43, 19]
- tabela publicada x jogos (RSSSF) — Kortrijk tabela [22, 3, 5, 14, 18, 62, 11] jogos [22, 3, 5, 14, 17, 62, 11]
- tabela publicada x jogos (Wikipédia) — Excelsior SC de Bruxelles tabela [22, 8, 3, 11, 48, 44, 19] jogos [22, 8, 3, 11, 48, 43, 19]
- tabela publicada x jogos (Wikipédia) — Kortrijk tabela [22, 3, 5, 14, 18, 62, 11] jogos [22, 3, 5, 14, 17, 62, 11]

### 1910/11

- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [21, 16, 2, 3, 76, 24, 34] jogos [22, 16, 3, 3, 76, 24, 35]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [21, 16, 1, 4, 70, 27, 33] jogos [22, 16, 2, 4, 70, 27, 34]
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [22, 11, 2, 9, 52, 42, 24] jogos [22, 11, 2, 9, 52, 43, 24]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [22, 9, 3, 10, 43, 46, 21] jogos [22, 9, 3, 10, 44, 46, 21]
- tabela publicada x jogos (RSSSF) — Racing Mechelen tabela [22, 8, 2, 12, 39, 59, 18] jogos [22, 8, 2, 12, 39, 56, 18]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [21, 16, 2, 3, 76, 24, 34] jogos [22, 16, 3, 3, 76, 24, 35]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [21, 16, 1, 4, 70, 27, 33] jogos [22, 16, 2, 4, 70, 27, 34]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [22, 11, 2, 9, 52, 42, 24] jogos [22, 11, 2, 9, 52, 43, 24]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [22, 9, 3, 10, 43, 46, 21] jogos [22, 9, 3, 10, 44, 46, 21]
- tabela publicada x jogos (Wikipédia) — Racing Mechelen tabela [22, 8, 2, 12, 39, 59, 18] jogos [22, 8, 2, 12, 39, 56, 18]

### 1911/12

- tabela publicada x jogos (RSSSF) — Club Brugge tabela [22, 11, 7, 4, 47, 25, 29] jogos [22, 11, 5, 6, 56, 29, 27]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [22, 11, 5, 6, 56, 29, 27] jogos [22, 11, 7, 4, 47, 25, 29]
- tabela publicada x jogos (RSSSF) — Standard Liège tabela [22, 6, 3, 13, 29, 85, 15] jogos [22, 6, 3, 13, 30, 84, 15]
- tabela publicada x jogos (RSSSF) — Racing Mechelen tabela [22, 3, 7, 12, 22, 42, 13] jogos [22, 3, 7, 12, 24, 42, 13]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [22, 3, 4, 15, 24, 46, 10] jogos [22, 3, 4, 15, 23, 47, 10]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [22, 11, 7, 4, 47, 25, 29] jogos [22, 11, 5, 6, 56, 29, 27]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [22, 11, 5, 6, 56, 29, 27] jogos [22, 11, 7, 4, 47, 25, 29]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [22, 6, 3, 13, 29, 85, 15] jogos [22, 6, 3, 13, 30, 84, 15]
- tabela publicada x jogos (Wikipédia) — Racing Mechelen tabela [22, 3, 7, 12, 22, 42, 13] jogos [22, 3, 7, 12, 24, 42, 13]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [22, 3, 4, 15, 24, 46, 10] jogos [22, 3, 4, 15, 23, 47, 10]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Club Brugge', 'Cercle Brugge'])

### 1912/13

- tabela publicada x jogos (RSSSF) — Standard Liège tabela [22, 6, 5, 11, 24, 66, 17] jogos [22, 6, 5, 11, 26, 64, 17]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [22, 6, 5, 11, 24, 66, 17] jogos [22, 6, 5, 11, 26, 64, 17]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Union Saint-Gilloise', 'Daring Club de Bruxelles'])

### 1913/14

- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [22, 11, 3, 8, 46, 32, 25] jogos [22, 12, 3, 7, 53, 33, 27]
- tabela publicada x jogos (RSSSF) — Gent tabela [23, 6, 3, 14, 29, 53, 15] jogos [22, 5, 3, 14, 27, 53, 13]
- tabela publicada x jogos (RSSSF) — Standard Liège tabela [23, 6, 1, 16, 29, 53, 13] jogos [22, 6, 1, 15, 21, 55, 13]
- tabela publicada x jogos (RSSSF) — Léopold Club tabela [22, 4, 1, 17, 31, 63, 9] jogos [22, 4, 1, 17, 32, 70, 9]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [22, 11, 3, 8, 46, 32, 25] jogos [22, 12, 3, 7, 53, 33, 27]
- tabela publicada x jogos (Wikipédia) — Gent tabela [23, 6, 3, 14, 29, 53, 15] jogos [22, 5, 3, 14, 27, 53, 13]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [23, 6, 1, 16, 29, 53, 13] jogos [22, 6, 1, 15, 21, 55, 13]
- tabela publicada x jogos (Wikipédia) — Léopold Club tabela [22, 4, 1, 17, 31, 63, 9] jogos [22, 4, 1, 17, 32, 70, 9]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Gent', 'Standard Liège'])

### 1919/20

- tabela publicada x jogos (RSSSF) — Beerschot VAC tabela [22, 11, 3, 8, 44, 34, 25] jogos [22, 11, 3, 8, 44, 35, 25]
- tabela publicada x jogos (RSSSF) — Gent tabela [22, 3, 4, 15, 28, 68, 10] jogos [22, 3, 4, 15, 28, 67, 10]
- tabela publicada x jogos (Wikipédia) — Beerschot VAC tabela [22, 11, 3, 8, 44, 34, 25] jogos [22, 11, 3, 8, 44, 35, 25]
- tabela publicada x jogos (Wikipédia) — Gent tabela [22, 3, 4, 15, 28, 68, 10] jogos [22, 3, 4, 15, 28, 67, 10]

### 1920/21

- sem ocorrências

### 1921/22

- tabela publicada x jogos (RSSSF) — Daring Club de Bruxelles tabela [26, 10, 6, 10, 28, 32, 26] jogos [26, 10, 5, 11, 28, 31, 25]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [26, 8, 8, 10, 38, 42, 24] jogos [26, 9, 7, 10, 39, 42, 25]
- tabela publicada x jogos (Wikipédia) — Daring Club de Bruxelles tabela [26, 10, 6, 10, 28, 32, 26] jogos [26, 10, 5, 11, 28, 31, 25]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [26, 8, 8, 10, 38, 42, 24] jogos [26, 9, 7, 10, 39, 42, 25]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['CS Verviétois', 'Gent'])

### 1922/23

- tabela publicada x jogos (RSSSF) — Club Brugge tabela [26, 9, 6, 11, 47, 54, 24] jogos [26, 9, 5, 12, 47, 54, 23]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [26, 9, 6, 11, 47, 54, 24] jogos [26, 9, 5, 12, 47, 54, 23]

### 1923/24

- tabela publicada x jogos (RSSSF) — CS Verviétois tabela [26, 5, 5, 16, 23, 59, 15] jogos [26, 5, 5, 16, 28, 59, 15]
- tabela publicada x jogos (Wikipédia) — CS Verviétois tabela [26, 5, 5, 16, 23, 59, 15] jogos [26, 5, 5, 16, 28, 59, 15]

### 1924/25

- tabela publicada x jogos (RSSSF) — Gent tabela [26, 7, 9, 10, 24, 33, 23] jogos [26, 7, 9, 10, 24, 38, 23]
- tabela publicada x jogos (Wikipédia) — Gent tabela [26, 7, 9, 10, 24, 33, 23] jogos [26, 7, 9, 10, 24, 38, 23]

### 1925/26

- sem ocorrências

### 1926/27

- tabela publicada x jogos (RSSSF) — Racing Gent tabela [26, 9, 8, 9, 61, 59, 27] jogos [26, 9, 7, 10, 58, 57, 25]
- tabela publicada x jogos (RSSSF) — Gent tabela [26, 11, 4, 11, 56, 63, 26] jogos [26, 11, 5, 10, 59, 65, 27]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [26, 15, 2, 9, 85, 58, 32] jogos [26, 14, 4, 8, 85, 58, 32]
- tabela publicada x jogos (Wikipédia) — Racing Gent tabela [26, 9, 8, 9, 61, 59, 26] jogos [26, 9, 7, 10, 58, 57, 25]
- tabela publicada x jogos (Wikipédia) — Gent tabela [26, 11, 4, 11, 56, 63, 26] jogos [26, 11, 5, 10, 59, 65, 27]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Racing Gent', 'Gent'])

### 1927/28

- tabela publicada x jogos (RSSSF) — Club Brugge tabela [26, 9, 4, 13, 53, 58, 22] jogos [26, 9, 4, 13, 43, 59, 22]
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [26, 8, 6, 12, 43, 59, 22] jogos [26, 8, 6, 12, 53, 58, 22]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [26, 9, 4, 13, 53, 58, 22] jogos [26, 9, 4, 13, 43, 59, 22]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [26, 8, 6, 12, 43, 59, 22] jogos [26, 8, 6, 12, 53, 58, 22]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 3 posições (ex.: ['Daring Club de Bruxelles', 'Club Brugge'])

### 1928/29

- tabela publicada x jogos (RSSSF) — Berchem Sport tabela [26, 10, 6, 10, 48, 44, 26] jogos [26, 9, 8, 9, 48, 41, 26]
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [26, 9, 8, 9, 48, 41, 26] jogos [26, 10, 6, 10, 48, 44, 26]
- tabela publicada x jogos (Wikipédia) — Berchem Sport tabela [26, 10, 6, 10, 48, 44, 26] jogos [26, 9, 8, 9, 48, 41, 26]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [26, 9, 8, 9, 48, 41, 26] jogos [26, 10, 6, 10, 48, 44, 26]

### 1929/30

- sem ocorrências

### 1930/31

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Standard Liège', 'Racing Mechelen'])

### 1931/32

- sem ocorrências

### 1932/33

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Racing Club de Bruxelles', 'Racing Mechelen'])

### 1933/34

- tabela publicada x jogos (RSSSF) — Lierse tabela [26, 14, 1, 11, 56, 57, 29] jogos [26, 13, 1, 12, 54, 59, 27]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [26, 9, 7, 10, 53, 50, 25] jogos [26, 10, 7, 9, 55, 48, 27]
- tabela publicada x jogos (Wikipédia) — Lierse tabela [26, 14, 1, 11, 56, 57, 29] jogos [26, 13, 1, 12, 54, 59, 27]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [26, 9, 7, 10, 53, 50, 25] jogos [26, 10, 7, 9, 55, 48, 27]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 6 posições (ex.: ['Lierse', 'Beerschot VAC'])

### 1934/35

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Racing Mechelen', 'Berchem Sport'])

### 1935/36

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Union Saint-Gilloise', 'Antwerp'])

### 1936/37

- sem ocorrências

### 1937/38

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Club Brugge', 'Gent'])

### 1938/39

- tabela publicada x jogos (RSSSF) — RWD Molenbeek tabela [26, 8, 6, 12, 45, 64, 22] jogos [26, 7, 7, 12, 44, 64, 21]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [26, 6, 5, 15, 40, 64, 17] jogos [26, 6, 6, 14, 40, 63, 18]
- tabela publicada x jogos (Wikipédia) — RWD Molenbeek tabela [26, 8, 6, 12, 45, 64, 22] jogos [26, 7, 7, 12, 44, 64, 21]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [26, 6, 5, 15, 40, 64, 17] jogos [26, 6, 6, 14, 40, 63, 18]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 3 posições (ex.: ['RWD Molenbeek', 'Cercle Brugge'])

### 1941/42

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Anderlecht', 'Gent'])

### 1942/43

- tabela publicada x jogos (RSSSF) — Tilleur tabela [30, 10, 9, 11, 52, 55, 29] jogos [30, 10, 9, 11, 53, 56, 29]
- tabela publicada x jogos (RSSSF) — La Forestoise tabela [30, 9, 5, 16, 40, 92, 23] jogos [30, 9, 5, 16, 40, 93, 23]
- tabela publicada x jogos (Wikipédia) — Tilleur tabela [30, 10, 9, 11, 52, 55, 29] jogos [30, 10, 9, 11, 53, 56, 29]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Union Saint-Gilloise', 'Standard Liège'])

### 1943/44

- fase regular com 239 jogos de 240
- tabela publicada x jogos (Wikipédia) — Berchem Sport tabela [30, 11, 9, 10, 63, 84, 31] jogos [30, 11, 9, 10, 63, 64, 31]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [30, 12, 5, 13, 51, 47, 29] jogos [30, 12, 5, 13, 52, 47, 29]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [29, 9, 4, 16, 57, 87, 22] jogos [29, 9, 4, 16, 57, 88, 22]
- tabela publicada x jogos (Wikipédia) — Tilleur tabela [30, 5, 8, 17, 36, 71, 18] jogos [30, 5, 8, 17, 35, 72, 18]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1945/46

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['RFC Liège', 'Berchem Sport'])

### 1946/47

- tabela publicada x jogos (RSSSF) — KV Mechelen tabela [36, 17, 11, 8, 89, 49, 45] jogos [36, 17, 12, 7, 88, 45, 46]
- tabela publicada x jogos (RSSSF) — Racing Club de Bruxelles tabela [36, 16, 11, 9, 82, 69, 43] jogos [36, 15, 12, 9, 78, 68, 42]
- tabela publicada x jogos (RSSSF) — Gent tabela [35, 14, 6, 15, 64, 76, 34] jogos [36, 14, 6, 16, 64, 76, 34]
- tabela publicada x jogos (Wikipédia) — KV Mechelen tabela [36, 17, 11, 8, 89, 49, 45] jogos [36, 17, 12, 7, 88, 45, 46]
- tabela publicada x jogos (Wikipédia) — Racing Club de Bruxelles tabela [36, 16, 11, 9, 82, 69, 43] jogos [36, 15, 12, 9, 78, 68, 42]
- tabela publicada x jogos (Wikipédia) — Gent tabela [35, 14, 6, 15, 64, 76, 34] jogos [36, 14, 6, 16, 64, 76, 34]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Lyra', 'Standard Liège'])

### 1947/48

- tabela publicada x jogos (RSSSF) — Olympic Charleroi tabela [30, 13, 4, 13, 55, 39, 30] jogos [30, 13, 4, 13, 56, 40, 30]
- tabela publicada x jogos (RSSSF) — Lyra tabela [30, 11, 5, 14, 54, 48, 27] jogos [30, 11, 5, 14, 55, 49, 27]
- tabela publicada x jogos (Wikipédia) — Olympic Charleroi tabela [30, 13, 4, 13, 55, 39, 30] jogos [30, 13, 4, 13, 56, 40, 30]
- tabela publicada x jogos (Wikipédia) — Lyra tabela [30, 11, 5, 14, 54, 48, 27] jogos [30, 11, 5, 14, 55, 49, 27]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 3 posições (ex.: ['Racing Club de Bruxelles', 'Standard Liège'])

### 1948/49

- na matriz de resultados da Wikipédia os nomes de KVM e RCM estão cruzados (KVM leva ao Racing Mechelen); pelos códigos (KVM = KV, RCM = Racing, como na tabela do artigo) os jogos fecham com as duas tabelas (MATRIZ_CODIGOS)
- tabela publicada x jogos (RSSSF) — Berchem Sport tabela [30, 16, 6, 8, 56, 38, 38] jogos [30, 15, 7, 8, 53, 38, 37]
- tabela publicada x jogos (RSSSF) — Standard Liège tabela [30, 17, 4, 9, 57, 48, 38] jogos [30, 17, 4, 9, 57, 46, 38]
- tabela publicada x jogos (RSSSF) — Beerschot VAC tabela [30, 15, 3, 12, 54, 46, 33] jogos [30, 15, 3, 12, 53, 46, 33]
- tabela publicada x jogos (RSSSF) — Gent tabela [30, 8, 9, 13, 50, 57, 25] jogos [30, 8, 9, 13, 50, 56, 25]
- tabela publicada x jogos (RSSSF) — Union Saint-Gilloise tabela [30, 8, 4, 18, 49, 70, 20] jogos [30, 8, 5, 17, 49, 67, 21]
- tabela publicada x jogos (Wikipédia) — Berchem Sport tabela [30, 16, 6, 8, 56, 38, 38] jogos [30, 15, 7, 8, 53, 38, 37]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [30, 17, 4, 9, 57, 48, 38] jogos [30, 17, 4, 9, 57, 46, 38]
- tabela publicada x jogos (Wikipédia) — Beerschot VAC tabela [30, 15, 3, 12, 54, 46, 33] jogos [30, 15, 3, 12, 53, 46, 33]
- tabela publicada x jogos (Wikipédia) — Gent tabela [30, 8, 9, 13, 50, 57, 25] jogos [30, 8, 9, 13, 50, 56, 25]
- tabela publicada x jogos (Wikipédia) — Union Saint-Gilloise tabela [30, 8, 4, 18, 49, 70, 20] jogos [30, 8, 5, 17, 49, 67, 21]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Berchem Sport', 'Standard Liège'])

### 1949/50

- tabela publicada x jogos (RSSSF) — KV Mechelen tabela [30, 14, 8, 8, 67, 46, 36] jogos [30, 14, 8, 8, 68, 45, 36]
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [30, 9, 4, 17, 43, 60, 22] jogos [30, 9, 4, 17, 43, 59, 22]
- tabela publicada x jogos (RSSSF) — Lyra tabela [30, 7, 5, 18, 51, 81, 19] jogos [30, 7, 5, 18, 50, 81, 19]
- tabela publicada x jogos (RSSSF) — Stade Leuven tabela [30, 4, 7, 19, 46, 85, 15] jogos [30, 4, 7, 19, 45, 86, 15]
- tabela publicada x jogos (Wikipédia) — KV Mechelen tabela [30, 14, 8, 8, 67, 46, 36] jogos [30, 14, 8, 8, 68, 45, 36]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [30, 9, 4, 17, 43, 60, 22] jogos [30, 9, 4, 17, 43, 59, 22]
- tabela publicada x jogos (Wikipédia) — Lyra tabela [30, 7, 5, 18, 51, 81, 19] jogos [30, 7, 5, 18, 50, 81, 19]
- tabela publicada x jogos (Wikipédia) — Stade Leuven tabela [30, 4, 7, 19, 46, 85, 15] jogos [30, 4, 7, 19, 45, 86, 15]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Racing Club de Bruxelles', 'Beerschot VAC'])

### 1950/51

- tabela publicada x jogos (RSSSF) — RFC Liège tabela [30, 13, 9, 8, 65, 41, 35] jogos [30, 13, 9, 8, 64, 41, 35]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [30, 13, 8, 9, 54, 52, 34] jogos [30, 13, 8, 9, 54, 49, 34]
- tabela publicada x jogos (RSSSF) — Charleroi tabela [30, 9, 9, 12, 42, 47, 27] jogos [30, 9, 9, 12, 39, 47, 27]
- tabela publicada x jogos (RSSSF) — Beringen tabela [30, 9, 4, 17, 43, 78, 22] jogos [30, 9, 4, 17, 43, 77, 22]
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [30, 13, 9, 8, 65, 41, 35] jogos [30, 13, 9, 8, 64, 41, 35]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [30, 13, 8, 9, 54, 52, 34] jogos [30, 13, 8, 9, 54, 49, 34]
- tabela publicada x jogos (Wikipédia) — Charleroi tabela [30, 9, 9, 12, 42, 47, 27] jogos [30, 9, 9, 12, 39, 47, 27]
- tabela publicada x jogos (Wikipédia) — Beringen tabela [30, 9, 4, 17, 43, 78, 22] jogos [30, 9, 4, 17, 43, 77, 22]

### 1951/52

- tabela publicada x jogos (RSSSF) — Olympic Charleroi tabela [30, 10, 11, 9, 47, 38, 31] jogos [30, 10, 11, 9, 47, 48, 31]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Daring Club de Bruxelles', 'Beerschot VAC'])

### 1952/53

- tabela publicada x jogos (RSSSF) — Antwerp tabela [30, 10, 7, 13, 47, 57, 27] jogos [30, 10, 7, 13, 46, 57, 27]
- tabela publicada x jogos (RSSSF) — Charleroi tabela [30, 10, 4, 16, 48, 78, 24] jogos [30, 10, 4, 16, 48, 77, 24]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [30, 10, 7, 13, 47, 57, 27] jogos [30, 10, 7, 13, 46, 57, 27]
- tabela publicada x jogos (Wikipédia) — Charleroi tabela [30, 10, 4, 16, 48, 78, 24] jogos [30, 10, 4, 16, 48, 77, 24]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Olympic Charleroi', 'Union Saint-Gilloise'])

### 1953/54

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 5 posições (ex.: ['KV Mechelen', 'Gent'])

### 1954/55

- fase regular com 232 jogos de 240
- tabela publicada x jogos (RSSSF) — Gent tabela [30, 16, 6, 8, 55, 33, 38] jogos [29, 15, 6, 8, 51, 34, 36]
- tabela publicada x jogos (RSSSF) — Standard Liège tabela [30, 16, 5, 9, 75, 46, 37] jogos [30, 16, 5, 9, 76, 47, 37]
- tabela publicada x jogos (RSSSF) — Berchem Sport tabela [30, 10, 11, 9, 49, 40, 31] jogos [29, 9, 11, 9, 44, 40, 29]
- tabela publicada x jogos (RSSSF) — Charleroi tabela [30, 12, 6, 12, 53, 57, 30] jogos [29, 11, 6, 12, 48, 57, 28]
- tabela publicada x jogos (RSSSF) — KV Mechelen tabela [30, 13, 4, 13, 57, 52, 30] jogos [29, 12, 4, 13, 52, 52, 28]
- tabela publicada x jogos (RSSSF) — Antwerp tabela [30, 13, 4, 13, 50, 47, 30] jogos [29, 11, 5, 13, 45, 48, 27]
- tabela publicada x jogos (RSSSF) — Beerschot VAC tabela [30, 12, 4, 14, 75, 64, 28] jogos [29, 11, 5, 13, 71, 64, 27]
- tabela publicada x jogos (RSSSF) — Racing Mechelen tabela [30, 12, 4, 14, 56, 60, 28] jogos [29, 11, 4, 14, 51, 60, 26]
- tabela publicada x jogos (Wikipédia) — Gent tabela [30, 16, 6, 8, 55, 33, 38] jogos [29, 15, 6, 8, 51, 34, 36]
- tabela publicada x jogos (Wikipédia) — Standard Liège tabela [30, 16, 5, 9, 75, 46, 37] jogos [30, 16, 5, 9, 76, 47, 37]
- tabela publicada x jogos (Wikipédia) — Berchem Sport tabela [30, 10, 11, 9, 49, 40, 31] jogos [29, 9, 11, 9, 44, 40, 29]
- tabela publicada x jogos (Wikipédia) — Charleroi tabela [30, 12, 6, 12, 53, 57, 30] jogos [29, 11, 6, 12, 48, 57, 28]
- tabela publicada x jogos (Wikipédia) — KV Mechelen tabela [30, 13, 4, 13, 57, 52, 30] jogos [29, 12, 4, 13, 52, 52, 28]
- tabela publicada x jogos (Wikipédia) — Antwerp tabela [30, 13, 4, 13, 50, 47, 30] jogos [29, 11, 5, 13, 45, 48, 27]
- tabela publicada x jogos (Wikipédia) — Beerschot VAC tabela [30, 12, 4, 14, 75, 64, 28] jogos [29, 11, 5, 13, 71, 64, 27]
- tabela publicada x jogos (Wikipédia) — Racing Mechelen tabela [30, 12, 4, 14, 56, 60, 28] jogos [29, 11, 4, 14, 51, 60, 26]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 10 posições (ex.: ['Gent', 'Standard Liège'])

### 1955/56

- tabela publicada x jogos (RSSSF) — Racing Mechelen tabela [30, 13, 7, 10, 55, 56, 33] jogos [30, 13, 7, 10, 55, 57, 33]
- tabela publicada x jogos (RSSSF) — Lierse tabela [30, 12, 4, 14, 41, 53, 28] jogos [30, 12, 4, 14, 42, 53, 28]
- tabela publicada x jogos (Wikipédia) — Racing Mechelen tabela [30, 13, 7, 10, 55, 56, 33] jogos [30, 13, 7, 10, 55, 57, 33]
- tabela publicada x jogos (Wikipédia) — Lierse tabela [30, 12, 4, 14, 41, 53, 28] jogos [30, 12, 4, 14, 42, 53, 28]

### 1956/57

- sem ocorrências

### 1957/58

- tabela publicada x jogos (RSSSF) — Union Saint-Gilloise tabela [30, 14, 8, 8, 61, 44, 36] jogos [30, 14, 8, 8, 61, 47, 36]
- tabela publicada x jogos (RSSSF) — Berchem Sport tabela [30, 8, 8, 14, 38, 52, 24] jogos [30, 8, 8, 14, 41, 52, 24]
- tabela publicada x jogos (Wikipédia) — Union Saint-Gilloise tabela [30, 14, 8, 8, 61, 44, 36] jogos [30, 14, 8, 8, 61, 47, 36]
- tabela publicada x jogos (Wikipédia) — Berchem Sport tabela [30, 8, 8, 14, 38, 52, 24] jogos [30, 8, 8, 14, 41, 52, 24]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Sint-Truiden', 'Berchem Sport'])

### 1958/59

- sem ocorrências

### 1959/60

- sem ocorrências

### 1960/61

- placar diferente na matriz da Wikipédia — Eendracht Aalst x CS Verviétois: ogol 1-0; Wikipédia 0-4
- placar diferente na matriz da Wikipédia — Anderlecht x Gent: ogol 1-2; Wikipédia 0-5
- placar diferente na matriz da Wikipédia — Antwerp x Eendracht Aalst: ogol 5-1; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Antwerp x Waterschei: ogol 1-0; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Daring Club de Bruxelles x Beerschot VAC: ogol 0-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Union Saint-Gilloise x Standard Liège: ogol —; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Waterschei x Antwerp: ogol 3-1; Wikipédia 3-0
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 5 posições (ex.: ['Club Brugge', 'Antwerp'])

### 1961/62

- placar diferente na matriz da Wikipédia — Beerschot VAC x Daring Club de Bruxelles: ogol 2-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Waterschei x Eendracht Aalst: ogol 2-2; Wikipédia 3-2

### 1962/63

- sem ocorrências

### 1963/64

- placar diferente na matriz da Wikipédia — Club Brugge x Turnhout: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Lierse x Standard Liège: ogol 3-2; Wikipédia 5-1
- placar diferente na matriz da Wikipédia — Lierse x Sint-Truiden: ogol 5-1; Wikipédia 3-2

### 1964/65

- placar diferente na matriz da Wikipédia — Anderlecht x Standard Liège: ogol 2-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Beringen x Diest: ogol 3-0; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — Union Saint-Gilloise x Standard Liège: ogol 0-1; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Union Saint-Gilloise x Sint-Truiden: ogol 1-3; Wikipédia 0-1

### 1965/66

- sem ocorrências

### 1966/67

- placar diferente na matriz da Wikipédia — Antwerp x Charleroi: ogol 2-0; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Beringen x Standard Liège: ogol 0-1; Wikipédia 2-1

### 1967/68

- placar diferente na matriz da Wikipédia — Daring Club de Bruxelles x Charleroi: ogol 2-0; Wikipédia 5-0
- placar diferente na matriz da Wikipédia — KSV Waregem x Olympic Charleroi: ogol 4-1; Wikipédia 1-1

### 1968/69

- placar diferente na matriz da Wikipédia — Anderlecht x Gent: ogol 2-3; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — RWD Molenbeek x Sint-Truiden: ogol 0-5; Wikipédia 0-1

### 1969/70

- sem ocorrências

### 1970/71

- a Wikipédia dá ao Sint-Truiden 12 vitórias e 2 pontos a menos (com "?"); a RSSSF e os jogos dão 11 vitórias e 29 pontos, sem punição: fica a RSSSF (IGNORAR_AJUSTE)
- tabela publicada x jogos (Wikipédia) — Sint-Truiden tabela [30, 12, 7, 11, 36, 39, 29] jogos [30, 11, 7, 12, 36, 39, 29]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1971/72

- placar diferente na matriz da Wikipédia — RFC Liège x Sint-Truiden: ogol 2-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Sint-Truiden x Standard Liège: ogol 1-2; Wikipédia 2-3

### 1972/73

- placar diferente na matriz da Wikipédia — RFC Liège x Crossing Schaerbeek: ogol 0-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — RWD Molenbeek x Crossing Schaerbeek: ogol 3-0; Wikipédia 4-0

### 1973/74

- a tabela da Wikipédia traz 10-11-9 para o RFC Liège; a RSSSF e os jogos, 11-9-10 (mesmos pontos)
- placar diferente na matriz da Wikipédia — RWD Molenbeek x Antwerp: ogol 2-0; Wikipédia 5-0
- tabela publicada x jogos (Wikipédia) — RFC Liège tabela [30, 10, 11, 9, 42, 42, 31] jogos [30, 11, 9, 10, 42, 42, 31]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1974/75

- placar diferente na matriz da Wikipédia — Standard Liège x Diest: ogol 4-0; Wikipédia 4-1

### 1975/76

- placar diferente na matriz da Wikipédia — Anderlecht x KV Mechelen: ogol 2-2; Wikipédia 3-3
- placar diferente na matriz da Wikipédia — Anderlecht x Racing Mechelen: ogol 4-0; Wikipédia 5-0
- placar diferente na matriz da Wikipédia — Berchem Sport x KSV Waregem: ogol 0-1; Wikipédia 0-4
- placar diferente na matriz da Wikipédia — Lokeren x Charleroi: ogol 4-0; Wikipédia 0-2

### 1976/77

- placar diferente na matriz da Wikipédia — RFC Liège x Kortrijk: ogol 3-1; Wikipédia 2-1

### 1977/78

- placar diferente na matriz da Wikipédia — KSV Waregem x RAA Louviéroise: ogol 3-0; Wikipédia 4-0

### 1978/79

- sem ocorrências

### 1979/80

- placar diferente na matriz da Wikipédia — Lierse x Waterschei: ogol 3-1; Wikipédia 6-1

### 1980/81

- placar diferente na matriz da Wikipédia — Antwerp x KSK Beveren: ogol 2-1; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Antwerp x Cercle Brugge: ogol 1-2; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Antwerp x Club Brugge: ogol 3-2; Wikipédia 1-2

### 1981/82

- os números de Club Brugge e Cercle Brugge estão trocados na tabela da RSSSF (e na da Wikipédia, que a copia); o ogol e a matriz da Wikipédia, montados jogo a jogo, concordam entre si, e a ordem da tabela (Club 14º, Cercle 15º, empatados em pontos e vitórias) só fecha pelo saldo com os números dos jogos
- tabela publicada x jogos (RSSSF) — Club Brugge tabela [34, 10, 8, 16, 57, 61, 28] jogos [34, 10, 8, 16, 46, 46, 28]
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [34, 10, 8, 16, 46, 46, 28] jogos [34, 10, 8, 16, 57, 61, 28]
- tabela publicada x jogos (Wikipédia) — Club Brugge tabela [34, 10, 8, 16, 57, 61, 28] jogos [34, 10, 8, 16, 46, 46, 28]
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [34, 10, 8, 16, 46, 46, 28] jogos [34, 10, 8, 16, 57, 61, 28]

### 1982/83

- sem ocorrências

### 1983/84

- placar diferente na matriz da Wikipédia — Anderlecht x Beringen: ogol 6-1; Wikipédia 3-1
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Kortrijk', 'RFC Liège'])

### 1984/85

- a tabela da Wikipédia dá 32 jogos ao Beerschot VAC; a RSSSF e os jogos, 34
- tabela publicada x jogos (Wikipédia) — Beerschot VAC tabela [32, 7, 10, 15, 38, 60, 24] jogos [34, 7, 10, 17, 38, 60, 24]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1985/86

- a tabela da RSSSF dá 35 jogos ao Kortrijk (erro de digitação: 8+9+17 = 34)
- placar diferente na matriz da Wikipédia — Kortrijk x Lierse: ogol 2-2; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — Kortrijk x Lokeren: ogol 4-0; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Waterschei x Standard Liège: ogol 0-3; Wikipédia 1-3
- tabela publicada x jogos (RSSSF) — Kortrijk tabela [35, 8, 9, 18, 40, 52, 25] jogos [34, 8, 9, 17, 40, 52, 25]

### 1986/87

- a tabela da RSSSF dá 33 jogos ao KSK Beveren (erro de digitação: 15+14+5 = 34)
- placar diferente na matriz da Wikipédia — RFC Seraing (1904) x RWD Molenbeek: ogol 0-0; Wikipédia 1-0
- tabela publicada x jogos (RSSSF) — KSK Beveren tabela [33, 15, 14, 4, 44, 24, 44] jogos [34, 15, 14, 5, 44, 24, 44]

### 1987/88

- sem ocorrências

### 1988/89

- placar diferente na matriz da Wikipédia — Sint-Truiden x Kortrijk: ogol 3-0; Wikipédia 3-1

### 1989/90

- placar diferente na matriz da Wikipédia — Gent x KSK Beveren: ogol 2-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — KSV Waregem x Gent: ogol 0-3; Wikipédia 0-2

### 1990/91

- sem ocorrências

### 1991/92

- placar diferente na matriz da Wikipédia — Anderlecht x Genk: ogol 0-2; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Gent x Germinal Beerschot: ogol 2-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Genk x Anderlecht: ogol 0-0; Wikipédia 2-0

### 1992/93

- placar diferente na matriz da Wikipédia — Charleroi x KV Mechelen: ogol 2-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Germinal Beerschot x KSK Beveren: ogol 5-2; Wikipédia 4-1

### 1993/94

- placar diferente na matriz da Wikipédia — KFC Lommel SK x Germinal Beerschot: ogol 3-1; Wikipédia 2-1

### 1994/95

- Eendracht Aalst x KV Mechelen (1995-03-19): placar corrigido para 1-1 (o ogol dá 0-0; a matriz da Wikipédia e as tabelas da RSSSF e da Wikipédia (gols de Aalst e Mechelen) dão 1-1)

### 1995/96

- o Eendracht Aalst perdeu por 0-5, só para ele, os jogos com o RFC Seraing (2-4 em campo) e o Sint-Truiden (0-0): os adversários ficaram com o resultado de campo (a RSSSF e a Wikipédia mostram assim); a classificação do Aalst fica com os números da tabela publicada (TABELA_OFICIAL)
- Gent (gols pró) e Cercle Brugge (gols contra): 1 gol a menos na RSSSF que na Wikipédia e nos jogos
- RFC Seraing (1904) x RWD Molenbeek (1996-04-13): DA no ogol; fica 0-5 pela matriz da Wikipédia
- RFC Seraing (1904) x RWD Molenbeek (1996-04-13): placar corrigido para 0-1 ("DA" no ogol, sem placar; football-data, engsoccerdata e as tabelas da RSSSF e da Wikipédia dão 0-1 (a matriz da Wikipédia, 0-5))
- placar diferente na matriz da Wikipédia — Eendracht Aalst x Sint-Truiden: ogol 0-0; Wikipédia 0-5; engsoccerdata 0-0; football-data 0-0
- placar diferente na matriz da Wikipédia — Antwerp x Club Brugge: ogol 0-3; Wikipédia 0-2; engsoccerdata 0-3; football-data 0-3
- placar diferente na matriz da Wikipédia — RFC Seraing (1904) x Eendracht Aalst: ogol 2-4; Wikipédia 5-0; engsoccerdata 2-4; football-data 2-4
- placar diferente na matriz da Wikipédia — RFC Seraing (1904) x Club Brugge: ogol 1-1; Wikipédia 2-3; engsoccerdata 1-1; football-data 1-1
- placar diferente na matriz da Wikipédia — RFC Seraing (1904) x Charleroi: ogol 2-3; Wikipédia 1-0; engsoccerdata 2-3; football-data 2-3
- placar diferente na matriz da Wikipédia — RFC Seraing (1904) x RWD Molenbeek: ogol 0-1; Wikipédia 0-5; engsoccerdata 0-1; football-data 0-1
- tabela publicada x jogos (RSSSF) — Cercle Brugge tabela [34, 13, 10, 11, 51, 46, 49] jogos [34, 13, 10, 11, 51, 47, 49]
- tabela publicada x jogos (RSSSF) — Eendracht Aalst tabela [34, 11, 9, 14, 51, 58, 42] jogos [34, 12, 10, 12, 55, 50, 46]
- tabela publicada x jogos (RSSSF) — Gent tabela [34, 10, 11, 13, 38, 49, 41] jogos [34, 10, 11, 13, 39, 49, 41]
- tabela publicada x jogos (Wikipédia) — RWD Molenbeek tabela [34, 13, 14, 7, 43, 29, 53] jogos [34, 13, 14, 7, 39, 29, 53]
- tabela publicada x jogos (Wikipédia) — Eendracht Aalst tabela [34, 11, 9, 14, 51, 58, 42] jogos [34, 12, 10, 12, 55, 50, 46]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 3 posições (ex.: ['KV Mechelen', 'Harelbeke'])

### 1996/97

- sem ocorrências

### 1997/98

- Lokeren x Antwerp (1998-05-03): DA no ogol; fica 5-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Antwerp x RWD Molenbeek: ogol 3-4; Wikipédia 1-0; engsoccerdata 3-4; football-data 3-4
- placar diferente na matriz da Wikipédia — KSK Beveren x Lierse: ogol 2-3; Wikipédia 1-2; engsoccerdata 2-3; football-data 2-3
- placar diferente na matriz da Wikipédia — Club Brugge x RWD Molenbeek: ogol 4-0; Wikipédia 4-1; engsoccerdata 4-0; football-data 4-0
- placar diferente no engsoccerdata — Antwerp x KFC Lommel SK (1998-01-31): ogol 2-1, engsoccerdata 2-5
- placar diferente no engsoccerdata — Antwerp x Harelbeke (1998-02-28): ogol 0-2, engsoccerdata 1-3
- placar diferente no engsoccerdata — KFC Lommel SK x Antwerp (1997-08-22): ogol 5-2, engsoccerdata 1-2
- placar diferente no engsoccerdata — Harelbeke x Antwerp (1997-09-28): ogol 3-1, engsoccerdata 2-0
- placar diferente no football-data — Antwerp x KFC Lommel SK (1998-01-31): ogol 2-1, football-data 2-5
- placar diferente no football-data — Antwerp x Harelbeke (1998-02-28): ogol 0-2, football-data 1-3
- placar diferente no football-data — KFC Lommel SK x Antwerp (1997-08-22): ogol 5-2, football-data 1-2
- placar diferente no football-data — Harelbeke x Antwerp (1997-09-28): ogol 3-1, football-data 2-0

### 1998/99

- Charleroi x Lierse (1998-09-23): DA no ogol; fica 5-0 pela matriz da Wikipédia

### 1999/00

- a tabela da RSSSF de 1999/00 tem as linhas do 7º ao 14º deslocadas (os números de cada clube estão na linha de outro); a da Wikipédia fecha com os jogos e dá a ordem
- Harelbeke x KSK Beveren (2000-01-23): DA no ogol; fica 0-5 pela matriz da Wikipédia
- tabela publicada x jogos (RSSSF) — Eendracht Aalst tabela [34, 16, 7, 11, 56, 45, 55] jogos [34, 11, 4, 19, 53, 72, 37]
- tabela publicada x jogos (RSSSF) — Germinal Beerschot tabela [34, 16, 6, 12, 63, 59, 54] jogos [34, 16, 7, 11, 56, 45, 55]
- tabela publicada x jogos (RSSSF) — Genk tabela [34, 15, 7, 12, 65, 47, 52] jogos [34, 16, 6, 12, 63, 59, 54]
- tabela publicada x jogos (RSSSF) — Lierse tabela [34, 12, 11, 11, 56, 58, 47] jogos [34, 15, 7, 12, 65, 47, 52]
- tabela publicada x jogos (RSSSF) — Lokeren tabela [34, 12, 5, 17, 47, 77, 41] jogos [34, 12, 11, 11, 56, 58, 47]
- tabela publicada x jogos (RSSSF) — Harelbeke tabela [34, 11, 5, 18, 62, 70, 38] jogos [34, 10, 5, 19, 56, 72, 35]
- tabela publicada x jogos (RSSSF) — KV Mechelen tabela [34, 11, 4, 19, 53, 72, 37] jogos [34, 12, 5, 17, 47, 77, 41]
- tabela publicada x jogos (RSSSF) — KSK Beveren tabela [34, 8, 8, 18, 49, 75, 32] jogos [34, 9, 8, 17, 51, 69, 35]

### 2000/01

- Gent x KSK Beveren (2000-09-16): DA no ogol; fica 5-0 pela matriz da Wikipédia
- Standard Liège x Lokeren (2001-05-20): DA no ogol; fica 0-5 pela matriz da Wikipédia
- placar diferente no engsoccerdata — Charleroi x KV Mechelen (2001-04-28): ogol 4-2, engsoccerdata 4-1
- placar diferente no football-data — Charleroi x KV Mechelen (2001-04-28): ogol 4-2, football-data 4-1

### 2001/02

- Eendracht Aalst x Excelsior Mouscron (2001-08-12): DA no ogol; fica 0-5 pela matriz da Wikipédia

### 2002/03

- Lierse x KSK Beveren (2002-08-24): DA no ogol; fica 5-0 pela matriz da Wikipédia
- Excelsior Mouscron x Mons (2002-09-28): DA no ogol; fica 0-5 pela matriz da Wikipédia
- Club Brugge x Excelsior Mouscron (2002-10-06): DA no ogol; fica 5-0 pela matriz da Wikipédia
- KSK Beveren x Anderlecht (2003-05-25): DA no ogol; fica 5-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Sint-Truiden x Charleroi: ogol 2-1; Wikipédia 2-2; engsoccerdata 2-1; football-data 2-1
- KFC Lommel SK desistiu com 8 rodadas por jogar (falência; só 13 jogadores); os jogos dele foram anulados (27 jogos na matriz da Wikipédia, fora do pacote); fica no fim, zerado

### 2003/04

- placar diferente na matriz da Wikipédia — Lokeren x Lierse: ogol 3-0; Wikipédia 2-0; engsoccerdata 3-0; football-data 3-0
- placar diferente na matriz da Wikipédia — Lokeren x RAA Louviéroise: ogol 2-0; Wikipédia 3-0; engsoccerdata 2-0; football-data 2-0

### 2004/05

- Gent x Germinal Beerschot (2004-08-07): DA no ogol; fica 5-0 pela matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Genk', 'Standard Liège'])

### 2005/06

- a tabela da Wikipédia traz 10-8-16 e 38-56 para o Cercle Brugge; a RSSSF e os jogos, 10-7-17 e 38-61
- Genk x RAA Louviéroise (2006-02-25): DA no ogol; fica 5-0 pela matriz da Wikipédia
- Germinal Beerschot x Cercle Brugge (2006-02-25): DA no ogol; fica 5-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Cercle Brugge x Excelsior Mouscron: ogol 1-0; Wikipédia 1-1; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Lokeren x KSK Beveren: ogol 1-2; Wikipédia 1-1; engsoccerdata 1-2; football-data 1-2
- tabela publicada x jogos (Wikipédia) — Cercle Brugge tabela [34, 10, 8, 16, 38, 56, 38] jogos [34, 10, 7, 17, 38, 61, 37]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 2006/07

- placar diferente no engsoccerdata — Roeselare x Charleroi (2007-02-17): ogol 1-3, engsoccerdata 1-2
- placar diferente no football-data — Roeselare x Charleroi (2007-02-17): ogol 1-3, football-data 1-2

### 2007/08

- FC Brussels x Genk (2007-12-08): DA no ogol; fica 0-5 pela matriz da Wikipédia

### 2008/09

- Cercle Brugge x Genk (26/04/2009): o football-data e o engsoccerdata dão 1-3; o ogol, a matriz e as tabelas, 1-2: fica 1-2
- Lokeren x Roeselare (2009-02-14): placar corrigido para 2-1 (o ogol dá 1-1; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia dão 2-1)
- placar diferente no engsoccerdata — Cercle Brugge x Genk (2009-04-26): ogol 1-2, engsoccerdata 1-3
- placar diferente no football-data — Cercle Brugge x Genk (2009-04-26): ogol 1-2, football-data 1-3
- placar diferente na ESPN — Gent x Anderlecht (2009-01-23): ogol 1-2, ESPN 0-1
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 2 posições (ex.: ['Standard Liège', 'Anderlecht'])
- desempate pelo título fora da tabela: Standard e Anderlecht terminaram empatados em pontos e vitórias; o título foi decidido em dois jogos (Anderlecht 1-1 Standard e Standard 1-0 Anderlecht)

### 2009/10

- placar diferente na ESPN — Genk x Zulte Waregem (2009-12-19): ogol 2-2, ESPN 1-2
- placar diferente na ESPN — Zulte Waregem x Roeselare (2010-02-20): ogol 1-1, ESPN 0-0
- placar diferente na ESPN — Zulte Waregem x Cercle Brugge (2009-12-13): ogol 1-0, ESPN 0-1
- placar diferente na ESPN — Zulte Waregem x Westerlo (2009-12-27): ogol 1-0, ESPN 0-1
- placar diferente na ESPN — Zulte Waregem x Anderlecht (2010-04-30): ogol 0-0, ESPN 1-2
- placar diferente na ESPN — Germinal Beerschot x Zulte Waregem (2010-03-07): ogol 1-1, ESPN 3-2
- placar diferente na ESPN — KV Mechelen x Zulte Waregem (2010-03-21): ogol 2-1, ESPN 0-1
- placar diferente na ESPN — Zulte Waregem x Kortrijk (2010-05-08): ogol 1-2, ESPN 0-5
- Excelsior Mouscron saiu em dezembro de 2009 (falência); os jogos dele foram anulados (20 jogos na matriz da Wikipédia, fora do pacote); fica no fim, zerado

### 2010/11

- placar diferente na ESPN — Charleroi x Cercle Brugge (2010-12-04): ogol 0-3, ESPN 0-5

### 2011/12

- sem ocorrências

### 2012/13

- play-off do título: a tabela da Wikipédia dá 22-20 gols ao Standard e 11-13 ao Genk; o ogol e a matriz da Wikipédia (jogo a jogo) dão 18-17 e 11-12
- play-off de rebaixamento: a tabela da Wikipédia dá 3-2 gols ao Cercle Brugge; o ogol e a matriz, 5-3 (1-0, 0-1, 2-1 e 2-1)
- placar diferente na ESPN — Charleroi x Standard Liège (2012-08-19): ogol 2-6, ESPN 1-3
- tabela do Play-off do título (Wikipédia) x jogos — Standard Liège tabela [10, 5, 2, 3, 22, 20, 42] jogos [10, 5, 2, 3, 18, 17, 42]
- tabela do Play-off do título (Wikipédia) x jogos — Genk tabela [10, 3, 3, 4, 11, 13, 40] jogos [10, 3, 3, 4, 11, 12, 40]
- tabela do Play-off de rebaixamento (Wikipédia) x jogos — Cercle Brugge tabela [4, 3, 0, 1, 3, 2, 9] jogos [4, 3, 0, 1, 5, 3, 9]
- tabela do Play-off de rebaixamento (Wikipédia) x jogos — Germinal Beerschot tabela [4, 1, 0, 3, 2, 3, 6] jogos [4, 1, 0, 3, 3, 5, 6]

### 2013/14

- placar diferente na ESPN — Genk x Charleroi (2013-12-26): ogol 0-3, ESPN 0-2

### 2014/15

- placar diferente na ESPN — Lierse x Anderlecht (2014-09-13): ogol 2-2, ESPN 3-2

### 2015/16

- placar diferente na ESPN — Lokeren x Royal Excel Mouscron (2015-09-19): ogol 1-2, ESPN 0-1
- placar diferente na ESPN — Genk x Royal Excel Mouscron (2015-10-23): ogol 0-4, ESPN 0-2
- placar diferente na ESPN — Kortrijk x Anderlecht (2015-10-29): ogol 1-1, ESPN 0-1

### 2016/17

- placar diferente na matriz da Wikipédia — Charleroi x Standard Liège: ogol 1-3; Wikipédia 1-3, 3-1, 3-1; engsoccerdata 1-3; football-data 1-3

### 2017/18

- Lierse x Waasland-Beveren (2018-05-11): DA no ogol; fica 0-5 pela matriz da Wikipédia
- Zulte Waregem x Lierse (2018-05-18): DA no ogol; fica 5-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — KV Mechelen x Genk: ogol 3-2; Wikipédia 3-1; engsoccerdata 3-2; football-data 3-2

### 2018/19

- Standard Liège x Anderlecht (2019-04-12): SUSP no ogol; fica 5-0 pela matriz da Wikipédia

### 2019/20

- a tabela da Wikipédia dá 36-53 gols ao Sint-Truiden; os jogos (com o 3-3 do jogo suspenso contra o Genk, que vale) dão 33-50, e a mesma tabela fecha para o Genk
- Sint-Truiden x Genk (2019-09-28): SUSP no ogol; fica 3-3 pela matriz da Wikipédia
- Charleroi x KV Mechelen (2020-02-11): SUSP no ogol; fica 2-1 pela matriz da Wikipédia
- tabela publicada x jogos (Wikipédia) — Sint-Truiden tabela [29, 9, 6, 14, 36, 53, 33] jogos [29, 9, 6, 14, 33, 50, 33]

### 2020/21

- placar diferente na matriz da Wikipédia — Oostende x Sint-Truiden: ogol 3-1; Wikipédia 1-3; engsoccerdata 3-1; football-data 3-1

### 2021/22

- OH Leuven x KV Mechelen (2022-01-15): DA no ogol; fica 5-0 pela matriz da Wikipédia
- Union Saint-Gilloise x Beerschot (2022-04-10): DA no ogol; fica 5-0 pela matriz da Wikipédia

### 2022/23

- Standard Liège x Anderlecht (2022-10-23): DA no ogol; fica 5-0 pela matriz da Wikipédia
- Charleroi x KV Mechelen (2022-11-12): AJ no ogol; fica 0-5 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Genk x Seraing: ogol 4-0; Wikipédia 2-0; engsoccerdata 4-0; football-data 4-0

### 2023/24

- Standard Liège x Westerlo (2024-05-10): DA no ogol; fica 0-5 pela matriz da Wikipédia

### 2024/25

- Antwerp x Beerschot (2024-09-29): placar corrigido para 5-0 (o ogol dá 4-0; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia dão 5-0)

### 2025/26

- sem ocorrências

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_bel.py`: o mesmo clube com nomes de época vira uma chave só (pela matrícula da federação, como na Wikipédia); clubes diferentes com nome parecido ficam separados (os três Beerschot, os dois Seraing, Mouscron, Lommel e RWDM; KSK Beveren e Waasland-Beveren; AS Oostende e KV Oostende).
- A ESPN é casada por votação jogo a jogo (mesma data e placar): 33 códigos.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Datas e rodadas antes de 1960/61:** a matriz da Wikipédia não traz; o ogol não tem esses jogos.
- **Jogos dos grupos de 1898/99 a 1903/04:** só as tabelas e os jogos finais.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.
