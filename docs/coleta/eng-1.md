# Campeonato Inglês (1ª divisão) — coleta de dados

Gerado por `python coleta/eng-1/importar.py`. Pacote em `data/coleta/eng-1/pacote/`.

**Edições:** 127, de 1888/89 a 2025/26: Football League (1888/89-1891/92), First Division (1892/93-1991/92), FA Premier League (1992/93-2006/07) e Premier League (2007/08 em diante). Sem liga em 1915/16-1918/19 e 1939/40-1945/46 (guerras; a temporada 1939/40 parou na 3ª rodada e foi anulada).

**Total:** 51330 jogos, 152539 gols, 25878 gols com autor (ESPN), 33166 cartões, 65 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1888/89-2024/25, menos 2022/23;
- football-data.co.uk: base de 2022/23 e 2025/26; de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time (chutes, faltas, escanteios, cartões; 2000/01+);
- ogol: rodada de cada jogo (só nas temporadas com rodadas fixas: 1992/93, 1993/94 e de 1995/96 em diante) e conferência de placar; calendários guardados em `data/cache/ogol-eng-1/` para os escudos;
- ESPN (liga `eng.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (engpaul/FLA, Paul Felton e Barry Spencer): tabela final publicada até 2006/07 e matriz de resultados (1888/89-1938/39, menos 1925/26) — conferência jogo a jogo;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e lista de artilheiros;
- BDFutbol (1960/61+): árbitro com o nome completo e estádio onde a ESPN não tem; autores dos 12 jogos em que os gols da ESPN não fecham com o placar (ficha de cada jogo).

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local de Londres. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1888/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 587 | 0 | 1 / 1 | Preston | — |
| 1889/90 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 611 | 0 | 2 / 0 | Preston | — |
| 1890/91 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 554 | 0 | 2 / 0 | Everton | Sunderland -2 pontos |
| 1891/92 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 777 | 0 | 2 / 0 | Sunderland | — |
| 1892/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 936 | 0 | 2 / 0 | Sunderland | — |
| 1893/94 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 939 | 0 | 2 / 0 | Aston Villa | — |
| 1894/95 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 917 | 0 | 2 / 0 | Sunderland | — |
| 1895/96 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 807 | 0 | 2 / 0 | Aston Villa | — |
| 1896/97 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 751 | 0 | 2 / 0 | Aston Villa | — |
| 1897/98 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 724 | 0 | 2 / 0 | Sheffield United | — |
| 1898/99 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 868 | 0 | 2 / 0 | Aston Villa | — |
| 1899/00 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 856 | 0 | 2 / 0 | Aston Villa | — |
| 1900/01 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 855 | 0 | 2 / 0 | Liverpool | — |
| 1901/02 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 840 | 0 | 2 / 0 | Sunderland | — |
| 1902/03 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 885 | 0 | 2 / 0 | Sheffield Wednesday | — |
| 1903/04 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 939 | 0 | 2 / 0 | Sheffield Wednesday | — |
| 1904/05 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 904 | 0 | 2 / 0 | Newcastle | — |
| 1905/06 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1242 | 0 | 2 / 0 | Liverpool | — |
| 1906/07 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1148 | 0 | 2 / 0 | Newcastle | — |
| 1907/08 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1176 | 0 | 2 / 0 | Manchester United | — |
| 1908/09 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1185 | 0 | 2 / 0 | Newcastle | — |
| 1909/10 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1194 | 0 | 2 / 0 | Aston Villa | — |
| 1910/11 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1028 | 0 | 2 / 0 | Manchester United | — |
| 1911/12 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1057 | 0 | 2 / 0 | Blackburn | — |
| 1912/13 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1153 | 0 | 2 / 0 | Sunderland | — |
| 1913/14 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1103 | 0 | 2 / 0 | Blackburn | — |
| 1914/15 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1201 | 0 | 2 / 0 | Everton | — |
| 1919/20 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1332 | 0 | 2 / 0 | West Bromwich | — |
| 1920/21 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1276 | 0 | 2 / 0 | Burnley | — |
| 1921/22 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1244 | 0 | 2 / 0 | Liverpool | — |
| 1922/23 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1215 | 0 | 2 / 0 | Liverpool | — |
| 1923/24 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1143 | 0 | 2 / 0 | Huddersfield | — |
| 1924/25 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1192 | 0 | 2 / 0 | Huddersfield | — |
| 1925/26 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1703 | 0 | 2 / 0 | Huddersfield | — |
| 1926/27 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1668 | 0 | 2 / 0 | Newcastle | — |
| 1927/28 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1765 | 0 | 2 / 0 | Everton | — |
| 1928/29 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1688 | 0 | 2 / 0 | Sheffield Wednesday | — |
| 1929/30 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1758 | 0 | 2 / 0 | Sheffield Wednesday | — |
| 1930/31 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1823 | 0 | 2 / 0 | Arsenal | — |
| 1931/32 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1727 | 0 | 2 / 0 | Everton | — |
| 1932/33 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1645 | 0 | 2 / 0 | Arsenal | — |
| 1933/34 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1524 | 0 | 2 / 0 | Arsenal | — |
| 1934/35 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1677 | 0 | 2 / 0 | Arsenal | — |
| 1935/36 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1556 | 0 | 2 / 0 | Sunderland | — |
| 1936/37 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1555 | 0 | 2 / 0 | Manchester City | — |
| 1937/38 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1430 | 0 | 2 / 0 | Arsenal | — |
| 1938/39 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1418 | 0 | 2 / 0 | Everton | — |
| 1946/47 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1513 | 0 | 2 / 0 | Liverpool | — |
| 1947/48 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1343 | 0 | 2 / 0 | Arsenal | — |
| 1948/49 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1303 | 0 | 2 / 0 | Portsmouth | — |
| 1949/50 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1247 | 0 | 2 / 0 | Portsmouth | — |
| 1950/51 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1413 | 0 | 2 / 0 | Tottenham | — |
| 1951/52 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1490 | 0 | 2 / 0 | Manchester United | — |
| 1952/53 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1508 | 0 | 2 / 0 | Arsenal | — |
| 1953/54 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1626 | 0 | 2 / 0 | Wolverhampton | — |
| 1954/55 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1572 | 0 | 2 / 0 | Chelsea | — |
| 1955/56 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1529 | 0 | 2 / 0 | Manchester United | — |
| 1956/57 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1612 | 0 | 2 / 0 | Manchester United | — |
| 1957/58 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1721 | 0 | 2 / 0 | Wolverhampton | — |
| 1958/59 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1692 | 0 | 2 / 0 | Wolverhampton | — |
| 1959/60 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1618 | 0 | 2 / 0 | Burnley | — |
| 1960/61 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1724 | 0 | 1 / 0 | Tottenham | — |
| 1961/62 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1582 | 0 | 2 / 0 | Ipswich | — |
| 1962/63 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1536 | 0 | 2 / 0 | Everton | — |
| 1963/64 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1571 | 0 | 2 / 0 | Liverpool | — |
| 1964/65 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1543 | 0 | 2 / 0 | Manchester United | — |
| 1965/66 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1457 | 0 | 2 / 0 | Liverpool | — |
| 1966/67 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1387 | 0 | 1 / 0 | Manchester United | — |
| 1967/68 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1398 | 0 | 2 / 0 | Manchester City | — |
| 1968/69 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1213 | 0 | 1 / 0 | Leeds | — |
| 1969/70 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1212 | 0 | 2 / 0 | Everton | — |
| 1970/71 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1089 | 0 | 2 / 0 | Arsenal | — |
| 1971/72 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1160 | 0 | 2 / 0 | Derby County | — |
| 1972/73 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1160 | 0 | 2 / 0 | Liverpool | — |
| 1973/74 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1107 | 0 | 2 / 0 | Leeds | — |
| 1974/75 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1213 | 0 | 2 / 0 | Derby County | — |
| 1975/76 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1230 | 0 | 1 / 0 | Liverpool | — |
| 1976/77 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1183 | 0 | 1 / 0 | Liverpool | — |
| 1977/78 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1231 | 0 | 2 / 0 | Nottingham Forest | — |
| 1978/79 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1217 | 0 | 2 / 0 | Liverpool | — |
| 1979/80 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1159 | 0 | 2 / 0 | Liverpool | — |
| 1980/81 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1228 | 0 | 2 / 0 | Aston Villa | — |
| 1981/82 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1173 | 0 | 2 / 0 | Liverpool | — |
| 1982/83 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1264 | 0 | 2 / 0 | Liverpool | — |
| 1983/84 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1250 | 0 | 2 / 0 | Liverpool | — |
| 1984/85 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1288 | 0 | 2 / 0 | Everton | — |
| 1985/86 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1288 | 0 | 2 / 0 | Liverpool | — |
| 1986/87 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1215 | 0 | 2 / 0 | Everton | — |
| 1987/88 | engsoccerdata + ogol + RSSSF + Wikipédia | 21 | 420 (420) | 1049 | 0 | 2 / 0 | Liverpool | — |
| 1988/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 962 | 0 | 2 / 0 | Arsenal | — |
| 1989/90 | engsoccerdata + ogol + RSSSF | 20 | 380 (380) | 986 | 0 | 1 / 0 | Liverpool | — |
| 1990/91 | engsoccerdata + ogol + RSSSF | 20 | 380 (380) | 1049 | 0 | 1 / 0 | Arsenal | Arsenal -2 pontos; Manchester United -1 pontos |
| 1991/92 | engsoccerdata + ogol + RSSSF | 22 | 462 (462) | 1174 | 0 | 1 / 0 | Leeds | — |
| 1992/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 22 | 462 (462) | 1222 | 0 | 2 / 0 | Manchester United | — |
| 1993/94 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 22 | 462 (462) | 1195 | 0 | 2 / 0 | Manchester United | — |
| 1994/95 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 22 | 462 (462) | 1195 | 0 | 2 / 0 | Blackburn | — |
| 1995/96 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 988 | 0 | 2 / 0 | Manchester United | — |
| 1996/97 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 970 | 0 | 2 / 0 | Manchester United | Middlesbrough -3 pontos |
| 1997/98 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 1019 | 0 | 2 / 0 | Arsenal | — |
| 1998/99 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 959 | 0 | 2 / 0 | Manchester United | — |
| 1999/00 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 1060 | 0 | 2 / 0 | Manchester United | — |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 992 | 0 | 2 / 0 | Manchester United | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1001 | 1001 | 2 / 0 | Arsenal | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1000 | 1000 | 2 / 0 | Manchester United | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1012 | 1012 | 2 / 0 | Arsenal | — |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 975 | 975 | 2 / 0 | Chelsea | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 944 | 944 | 2 / 0 | Chelsea | — |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 931 | 931 | 2 / 0 | Manchester United | — |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1002 | 1002 | 1 / 0 | Manchester United | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 942 | 942 | 1 / 0 | Manchester United | — |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1053 | 1053 | 1 / 0 | Chelsea | Portsmouth -9 pontos |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1063 | 1063 | 1 / 0 | Manchester United | — |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1066 | 1066 | 1 / 0 | Manchester City | — |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1063 | 1063 | 1 / 0 | Manchester United | — |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1052 | 1052 | 1 / 0 | Manchester City | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 975 | 975 | 1 / 0 | Chelsea | — |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1026 | 1026 | 1 / 0 | Leicester | — |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1064 | 1064 | 1 / 0 | Chelsea | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1018 | 1018 | 1 / 0 | Manchester City | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1072 | 1072 | 1 / 0 | Manchester City | — |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1034 | 1034 | 1 / 0 | Liverpool | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1024 | 1024 | 1 / 0 | Manchester City | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1071 | 1071 | 1 / 0 | Manchester City | — |
| 2022/23 | football-data + ogol + ESPN + Wikipédia | 20 | 380 (380) | 1084 | 1084 | 1 / 0 | Manchester City | — |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1246 | 1246 | 1 / 0 | Manchester City | Everton -8 pontos; Nottingham Forest -4 pontos |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1115 | 1115 | 1 / 0 | Liverpool | — |
| 2025/26 | football-data + ogol + ESPN + Wikipédia | 20 | 380 (380) | 1045 | 1045 | 1 / 0 | Arsenal | — |

## Conferência e ocorrências, temporada a temporada

### 1888/89

- Wolverhampton x Everton (26/01/1889) fica 5-0 (ver a correção abaixo); a matriz e a tabela da RSSSF, feitas com 4-0, ficam com 1 gol a menos para o Wolverhampton e para o Everton
- placar corrigido: Wolverhampton Wanderers x Everton de 4-0 para 5-0 — três jornais da época trazem 5-0 (Cricket and Football Field, Liverpool Courier e Athletic News, transcritos em bluecorrespondent.co.uk/1888-89/january1889.html); também o ogol, o 11v11, a página da temporada do Wolverhampton na Wikipédia e a tabela final da Wikipédia (Wolverhampton 51 gols pró, Everton 47 contra). O 4-0 vem da RSSSF e de quem a copia (um gol de Knight foi anulado por impedimento)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- placar diferente na matriz da RSSSF — Wolverhampton Wanderers x Everton: base 5-0, RSSSF 4-0
- tabela publicada x jogos (RSSSF) — Wolverhampton Wanderers tabela [22, 12, 4, 6, 50, 37, 28] jogos [22, 12, 4, 6, 51, 37, 28]
- tabela publicada x jogos (RSSSF) — Everton tabela [22, 9, 2, 11, 35, 46, 20] jogos [22, 9, 2, 11, 35, 47, 20]

### 1889/90

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- Stoke City não está na temporada seguinte, mas não foi rebaixado: não foi reeleito para a Football League (foi para a Football Alliance); não havia rebaixamento

### 1890/91

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1891/92

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- Darwen não está na temporada seguinte, mas não foi rebaixado: não foi reeleito para a 1ª divisão e foi posto na nova 2ª divisão; não havia rebaixamento

### 1892/93

- 4 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Small Heath 1-1 Manchester United): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1893/94

- 3 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Liverpool 2-0 Manchester United): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1894/95

- 3 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Stoke City 3-0 Manchester United): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1895/96

- 1 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Burnley x Sheffield United (1896-02-03 -> 1896-02-04)
- 8 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Liverpool 4-0 Small Heath): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Burnley x Blackburn Rovers: base 1896-04-18, ogol 1896-04-13); fica a da base

### 1896/97

- 8 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Notts County 1-0 Sunderland): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1897/98

- 8 test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da 2ª divisão; ex.: Blackburn Rovers 1-3 Burnley): ficam de fora
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1898/99

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1899/00

- 9 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Aston Villa x Sunderland (1899-12-29 -> 1899-12-30); Burnley x Glossop North End (1899-12-29 -> 1899-12-30); Liverpool x Stoke City (1899-12-29 -> 1899-12-30); Manchester City x Blackburn Rovers (1899-12-29 -> 1899-12-30) ...
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1900/01

- a matriz da RSSSF traz Newcastle 4-0 Sheffield United; a tabela da RSSSF e a da Wikipédia fecham com o 3-0 da base: erro de digitação da matriz
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- placar diferente na matriz da RSSSF — Newcastle United x Sheffield United: base 3-0, RSSSF 4-0

### 1901/02

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1902/03

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1903/04

- a matriz da RSSSF troca os placares de Stoke x West Bromwich (5-0) e Stoke x Wolverhampton (5-1); as tabelas da RSSSF e da Wikipédia fecham com a base: erro da matriz
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- placar diferente na matriz da RSSSF — Stoke City x West Bromwich Albion: base 5-0, RSSSF 5-1
- placar diferente na matriz da RSSSF — Stoke City x Wolverhampton Wanderers: base 5-1, RSSSF 5-0

### 1904/05

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1905/06

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1906/07

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1907/08

- a RSSSF põe Arsenal e Blackburn empatados em 14º ('14='), com os mesmos pontos e a mesma média de gols; a Wikipédia ordena Arsenal 14º e Blackburn 15º. Fica a ordem da Wikipédia
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- ordem da tabela diferente entre RSSSF e Wikipédia; fica a da Wikipédia
- a ordem oficial não é a do critério calculado em 2 posições (ex.: ['Blackburn Rovers', 'Arsenal'])

### 1908/09

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1909/10

- a matriz da RSSSF traz Bolton 0-1 Sheffield Wednesday; as tabelas da RSSSF e da Wikipédia fecham com o 0-2 da base: erro da matriz
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- placar diferente na matriz da RSSSF — Bolton Wanderers x Sheffield Wednesday: base 0-2, RSSSF 0-1

### 1910/11

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1911/12

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1912/13

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1913/14

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Bolton Wanderers x Chelsea: base 1914-02-11, ogol 1914-02-10); fica a da base

### 1914/15

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1919/20

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1920/21

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1921/22

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1922/23

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1923/24

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Chelsea x Everton: base 1924-02-23, ogol 1924-02-22); fica a da base

### 1924/25

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1925/26

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1926/27

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1927/28

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1928/29

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1929/30

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1930/31

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1931/32

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1932/33

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1933/34

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Tottenham Hotspur x Chelsea: base 1934-02-10, ogol 1934-02-12); fica a da base

### 1934/35

- 1 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Blackburn Rovers x Chelsea (1934-11-12 -> 1934-11-17)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Tottenham Hotspur x Chelsea: base 1935-01-30, ogol 1935-01-29); fica a da base

### 1935/36

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1936/37

- 2 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Derby County x Brentford (1936-10-23 -> 1936-10-03); West Bromwich Albion x Bolton Wanderers (1936-11-03 -> 1936-11-14)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1937/38

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1938/39

- 2 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Leicester City x Portsmouth (1938-11-21 -> 1938-11-12); Charlton Athletic x Arsenal (1938-12-26 -> 1938-12-27)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1946/47

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1947/48

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1948/49

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Liverpool x Manchester United: base 1948-12-27, ogol 1948-12-26); fica a da base

### 1949/50

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Chelsea x Derby County: base 1949-08-27, ogol 1949-08-28); fica a da base

### 1950/51

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Chelsea x Sunderland: base 1950-10-28, ogol 1950-10-30); fica a da base

### 1951/52

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1952/53

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1953/54

- 1 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Sheffield Wednesday x Aston Villa (1953-09-07 -> 1953-11-07)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Sheffield Wednesday x Aston Villa: base 1953-11-07, ogol 1953-09-07); fica a da base

### 1954/55

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1955/56

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1956/57

- Birmingham e Chelsea terminaram com 39 pontos e média de gols igual (69/69 e 73/73 = 1,000); a ordem oficial (RSSSF e Wikipédia) põe o Birmingham em 12º; o critério calculado aqui (gols pró) poria o Chelsea
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- a ordem oficial não é a do critério calculado em 2 posições (ex.: ['Birmingham City', 'Chelsea'])

### 1957/58

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1958/59

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Arsenal x Bolton Wanderers: base 1958-09-09, ogol 1959-01-09); fica a da base

### 1959/60

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1960/61

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Manchester United x Tottenham Hotspur: base 1961-01-16, ogol 1961-01-14); fica a da base

### 1961/62

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1962/63

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Tottenham Hotspur x Manchester United: base 1962-10-24, ogol 1962-10-20); fica a da base

### 1963/64

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1964/65

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1965/66

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1966/67

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1967/68

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: West Bromwich Albion x Manchester United: base 1968-04-29, ogol 1968-04-27); fica a da base

### 1968/69

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1969/70

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1970/71

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1971/72

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Coventry City x Arsenal: base 1972-05-01, ogol 1972-05-02); fica a da base

### 1972/73

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1973/74

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1974/75

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1975/76

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1976/77

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Bristol City x Arsenal: base 1977-01-22, ogol 1977-01-27); fica a da base

### 1977/78

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1978/79

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Ipswich Town x Leeds United: base 1978-12-02, ogol 1978-12-03); fica a da base

### 1979/80

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1980/81

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1981/82

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1982/83

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1983/84

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1984/85

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 1 jogos (ex.: Chelsea x Coventry City: base 1984-11-03, ogol 1984-11-04); fica a da base

### 1985/86

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1986/87

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1987/88

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Charlton Athletic x Southampton: base 1987-10-31, ogol 1987-10-30); fica a da base

### 1988/89

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1989/90

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1990/91

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 3 jogos (ex.: Wimbledon x Arsenal: base 1990-08-25, ogol 1990-08-24); fica a da base

### 1991/92

- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada
- data diferente no ogol em 2 jogos (ex.: Sheffield United x Southampton: base 1991-08-24, ogol 1991-08-23); fica a da base

### 1992/93

- data diferente no ogol em 1 jogos (ex.: Wimbledon x Manchester United: base 1993-05-09, ogol 1993-05-08); fica a da base

### 1993/94

- 3 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Ipswich Town x Sheffield United (1994-02-26 -> 1994-02-22); Newcastle United x Ipswich Town (1994-03-22 -> 1994-03-23); Wimbledon x Leeds United (1994-03-27 -> 1994-03-26)

### 1994/95

- 2 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Everton x Leeds United (1994-12-04 -> 1994-12-05); Blackburn Rovers x Crystal Palace (1995-04-19 -> 1995-04-20)
- sem rodadas fixas nesta temporada (no ogol há clubes com mais de um jogo na mesma "rodada"): a rodada fica vazia e não há tabela rodada a rodada

### 1995/96

- 11 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): West Ham United x Manchester United (1996-01-23 -> 1996-01-22); Arsenal x Bolton Wanderers (1996-05-04 -> 1996-05-05); Chelsea x Blackburn Rovers (1996-05-04 -> 1996-05-05); Coventry City x Leeds United (1996-05-04 -> 1996-05-05) ...
- data diferente no ogol em 1 jogos (ex.: Leeds United x Southampton: base 1996-04-03, ogol 1996-04-30); fica a da base

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- 1 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Manchester United x Derby County (1999-02-02 -> 1999-02-03)
- data diferente no ogol em 1 jogos (ex.: Chelsea x Leeds United: base 1999-05-05, ogol 1999-05-04); fica a da base

### 1999/00

- sem ocorrências

### 2000/01

- sem ocorrências

### 2001/02

- sem ocorrências

### 2002/03

- placar diferente na ESPN — Fulham x Aston Villa (2003-02-08): base 2-1, ESPN 1-1
- placar diferente na ESPN — Birmingham City x Sunderland (2003-04-12): base 2-0, ESPN 1-0
- os gols da ESPN não fecham com o placar em West Bromwich Albion 1-0 Southampton: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=610818)
- os gols da ESPN não fecham com o placar em Sunderland 1-3 Charlton Athletic: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=611018)
- os gols da ESPN não fecham com o placar em Fulham 2-1 Aston Villa: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=611026)

### 2003/04

- os gols da ESPN não fecham com o placar em Leeds United 2-1 Manchester City: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=611432)

### 2004/05

- os gols da ESPN não fecham com o placar em Tottenham Hotspur 2-3 Charlton Athletic: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=611643)

### 2005/06

- sem ocorrências

### 2006/07

- os gols da ESPN não fecham com o placar em West Ham United 0-2 Wigan Athletic: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=612435)

### 2007/08

- sem ocorrências

### 2008/09

- sem ocorrências

### 2009/10

- 357 eventos repetidos da ESPN descartados (mesmo jogo com outro id e placar e lances de outra liga; fica o evento com o placar da base)

### 2010/11

- os gols da ESPN não fecham com o placar em Everton 1-4 West Bromwich Albion: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=613952)

### 2011/12

- os gols da ESPN não fecham com o placar em Everton 2-0 West Bromwich Albion: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=614493)

### 2012/13

- sem ocorrências

### 2013/14

- os gols da ESPN não fecham com o placar em Manchester City 4-1 Manchester United: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=614998)

### 2014/15

- os gols da ESPN não fecham com o placar em Manchester City 1-0 Manchester United: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=618794)

### 2015/16

- 1 datas corrigidas (o 11v11 e o ogol concordam contra a base; conferência da revisão, EN-005): Manchester United x AFC Bournemouth (2016-05-16 -> 2016-05-17)

### 2016/17

- os gols da ESPN não fecham com o placar em Liverpool 2-2 West Ham United: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=619637)
- os gols da ESPN não fecham com o placar em Stoke City 1-1 Everton: os autores vêm da ficha do BDFutbol (https://www.bdfutbol.com/es/p/p.php?id=619717)

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- sem ocorrências

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- sem ocorrências

### 2023/24

- sem ocorrências

### 2024/25

- sem ocorrências

### 2025/26

- sem ocorrências

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_eng.py` (serve para todas as divisões inglesas): nome de exibição como o clube é conhecido no Brasil ("Tottenham", "West Ham", "Wolverhampton", "QPR"), cidade e país. Cardiff e Swansea são do País de Gales (`WAL`, em `paises.csv`).
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 65 códigos do ogol e 44 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv` (ex.: `ogol:Newton Heath`).
- "Accrington" é o Accrington FC original (1878-1896), não o Accrington Stanley; "Wimbledon" é o Wimbledon FC (1889-2004).

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. O ogol tem a ficha de muitos jogos, mas seriam uns 40 mil pedidos; fica como próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** idem.
- **Test matches (1892/93-1897/98) e play-offs (1986/87-1987/88):** jogos entre clubes da 1ª e da 2ª divisão, que decidiam o rebaixamento; ficam de fora (entram quando a 2ª divisão for coletada).
- **Rodadas antes de 1992/93 (e em 1994/95):** a liga inglesa não tinha rodadas fixas, e o número de rodada do ogol junta jogos de datas diferentes (clubes com 2 ou 3 jogos na mesma rodada). Nessas 94 temporadas a rodada fica vazia e não há tabela rodada a rodada; a ordem dos jogos é a das datas.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
