# Campeonato Belga (`bel-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/bel-1/pacote/` e do importador `coleta/bel-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bel-1.md`.

## 1. O que temos

- **Edições:** 123, de 1895/96 a 2025/26.
- **Jogos:** 28712; **gols:** 90510; **gols com autor:** 12031 (13%); **cartões:** 18167; **jogos com estatísticas** (chutes, faltas, escanteios): 2559.
- **Clubes:** 81; **artilheiros:** 79 temporadas com artilheiro (86 linhas, com empates).
- **Classificação final:** 123 temporadas; **rodada a rodada:** 66 temporadas.
- **Tabelas publicadas guardadas para conferência:** 3685 linhas, de 223 tabelas.
- **Observação da competição:** 1ª divisão belga desde a criação (1895/96): Coupe de Championnat, Division d'Honneur, First Division, First Division A e Pro League. Sem 1914/15-1918/19, 1939/40-1940/41 e 1944/45 (guerras). De 1898/99 a 1903/04, dois grupos e um torneio final. Desde 2009/10, fase regular e play-offs (o título é decidido no play-off, que começa com a metade dos pontos da fase regular).

## 2. Fontes e regras

**Fontes:**

- Wikipédia (en): matriz de resultados (base dos jogos até 1959/60, sem data), tabelas da fase regular e dos play-offs (com o ponto de partida dos play-offs) e conferência jogo a jogo depois;
- ogol (zerozero): base dos jogos de 1960/61 em diante, com data e rodada; o clube pelo código do ogol (os nomes do calendário não são confiáveis); calendários em `data/cache/ogol-bel-1/` para os escudos;
- RSSSF: tabelas finais de 1895/96 a 2007/08 (belghist.html; de 1898/99 a 1903/04, grupos e torneio final), lista de campeões e de artilheiros (desde 1945/46);
- engsoccerdata e football-data: conferência de placar de 1995/96 em diante; hora e estatísticas do football-data;
- ESPN (liga `bel.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). Nos play-offs (2009/10+), a classificação final é a do play-off do título, depois os outros clubes pela fase regular e o play-off de rebaixamento; os pontos são os oficiais (a metade da fase regular, arredondada para cima, mais os do play-off) e a diferença para a soma de todos os jogos fica em `ajuste_pontos`. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (vitórias em 90, saldo em 17, confronto direto em 5, média de gols em 6).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 185 tabelas fecham com os jogos e 83 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1895/96, 1897/98, 1898/99, 1899/00, 1900/01, 1901/02, 1902/03, 1903/04, 1904/05, 1905/06, 1906/07, 1907/08, 1908/09, 1909/10, 1910/11, 1911/12, 1912/13, 1913/14, 1919/20, 1921/22, 1922/23, 1923/24, 1924/25, 1926/27, 1927/28, 1928/29, 1933/34, 1938/39, 1942/43, 1946/47, 1947/48, 1948/49, 1949/50, 1950/51, 1952/53, 1954/55, 1955/56, 1957/58, 1981/82, 1995/96, 2019/20.
- Temporadas com alguma tabela divergente: 1895/96, 1896/97, 1897/98, 1900/01, 1904/05, 1905/06, 1906/07, 1907/08, 1908/09, 1909/10, 1910/11, 1911/12, 1912/13, 1913/14, 1919/20, 1921/22, 1922/23, 1923/24, 1924/25, 1926/27, 1927/28, 1928/29, 1933/34, 1938/39, 1942/43, 1943/44, 1946/47, 1947/48, 1948/49, 1949/50, 1950/51, 1951/52, 1952/53, 1954/55, 1955/56, 1957/58, 1970/71, 1973/74, 1981/82, 1984/85, 1985/86, 1986/87, 1995/96, 1999/00, 2005/06, 2012/13, 2019/20.
- Temporadas com número de jogos diferente do turno e returno completo: 1897/98 (19 de 20), 1904/05 (109 de 110), 1907/08 (89 de 90), 1943/44 (239 de 240), 1954/55 (232 de 240), 2008/09 (308 de 306), 2009/10 (268 de 210), 2010/11 (300 de 240), 2011/12 (302 de 240), 2012/13 (302 de 240), 2013/14 (299 de 240), 2014/15 (302 de 240), 2015/16 (298 de 240), 2016/17 (332 de 240), 2017/18 (331 de 240), 2018/19 (332 de 240), 2019/20 (232 de 240), 2020/21 (330 de 306), 2021/22 (330 de 306), 2022/23 (330 de 306), 2023/24 (313 de 240), 2024/25 (313 de 240), 2025/26 (313 de 240).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1890s | 96 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1900s | 716 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 660 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 1770 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 1638 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 2065 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 2392 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2906 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 2990 | 100% | 37% | 98% | 37% | 0% | 0% | 0% | 33% | 1.4 |
| 2010s | 3030 | 100% | 77% | 79% | 72% | 31% | 0% | 23% | 45% | 2.1 |
| 2020s | 1929 | 100% | 96% | 89% | 96% | 80% | 0% | 96% | 95% | 3.9 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1895/96: 7 clubes
- 1896/97: 6 clubes
- 1897/98: 5 clubes
- 1898/99: 9 clubes
- 1899/00: 10 clubes
- 1900/01: 9 clubes
- 1901/02: 11 clubes
- 1902/03: 10 clubes
- 1903/04: 12 clubes
- 1904/05: 11 clubes
- 1905/06 a 1907/08: 10 clubes
- 1908/09 a 1920/21: 12 clubes
- 1921/22 a 1941/42: 14 clubes
- 1942/43 a 1943/44: 16 clubes
- 1945/46 a 1946/47: 19 clubes
- 1947/48 a 1973/74: 16 clubes
- 1974/75: 20 clubes
- 1975/76: 19 clubes
- 1976/77 a 2001/02: 18 clubes
- 2002/03: 17 clubes
- 2003/04 a 2008/09: 18 clubes
- 2009/10: 15 clubes
- 2010/11 a 2019/20: 16 clubes
- 2020/21 a 2022/23: 18 clubes
- 2023/24 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1895/96 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1895/96 a 2015/16: Belgian First Division
- 2016/17 a 2021/22: Belgian First Division A
- 2022/23 a 2025/26: Belgian Pro League

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1898/99: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1899/00: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta); Desempate (mata_mata, jogo_unico)
- 1901/02: Grupos (grupos, pontos_corridos); Torneio final (grupos, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1902/03: Grupos (grupos, pontos_corridos); Torneio final (grupos, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1903/04: Grupos (grupos, pontos_corridos); Torneio final (grupos, pontos_corridos)
- 2008/09: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 2009/10: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2010/11: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2011/12: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2012/13: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2013/14: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2014/15: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2015/16: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2016/17: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2017/18: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2018/19: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2020/21: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2021/22: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2022/23: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2023/24: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2024/25: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)
- 2025/26: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-off de rebaixamento (grupos, pontos_corridos)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, vitórias, saldo de gols, gols pró: 90 temporadas
- pontos: 26 temporadas
- pontos, com a metade dos pontos da fase regular de partida: 24 temporadas
- pontos, saldo de gols, gols pró: 17 temporadas
- pontos, média de gols (goal average): 6 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 5 temporadas
- jogo-desempate: 3 temporadas
- jogos-desempate, fora da tabela: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1898/99: sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF
- 1899/00: sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF
- 1901/02: sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF
- 1902/03: sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF
- 1903/04: sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF
- 2002/03: KFC Lommel SK desistiu com 8 rodadas por jogar (falência; só 13 jogadores); os jogos dele foram anulados
- 2008/09: Standard e Anderlecht terminaram empatados em pontos e vitórias; o título foi decidido em dois jogos (Anderlecht 1-1 Standard e Standard 1-0 Anderlecht)
- 2009/10: Excelsior Mouscron saiu em dezembro de 2009 (falência); os jogos dele foram anulados
- 2016/17: punições: Standard Liège -3 pontos
- 2019/20: temporada interrompida em março de 2020 pela pandemia de covid-19, antes da última rodada da fase regular; o Club Brugge foi declarado campeão e não houve play-offs

## 6. Campeões, rebaixados e punições

**Títulos:**

- Anderlecht: 34
- Club Brugge: 20
- Union Saint-Gilloise: 12
- Standard Liège: 10
- Beerschot VAC: 7
- Racing Club de Bruxelles: 6
- RFC Liège: 5
- Daring Club de Bruxelles: 5
- Antwerp: 5
- Lierse: 4
- KV Mechelen: 4
- Genk: 4
- Cercle Brugge: 3
- KSK Beveren: 2
- RWD Molenbeek: 1
- Gent: 1

**Rebaixamentos:** 219 no total; quem mais caiu: KV Mechelen (12), Berchem Sport (7), Beringen (7), Club Brugge (6), Racing Mechelen (6).

**Punições em pontos:**

- 1926/27: Racing Gent 1
- 2008/09: Standard Liège -4
- 2008/09: Anderlecht -1
- 2009/10: Anderlecht -34
- 2009/10: Gent -24
- 2009/10: Club Brugge -28
- 2009/10: Sint-Truiden -21
- 2009/10: Kortrijk -22
- 2009/10: Zulte Waregem -20
- 2009/10: KV Mechelen -10
- 2009/10: Standard Liège -8
- 2009/10: Cercle Brugge -7
- 2009/10: Germinal Beerschot -5
- 2009/10: Genk -26
- 2009/10: Westerlo -11
- 2009/10: Charleroi -4
- 2009/10: Lokeren -6
- 2010/11: Genk -32
- 2010/11: Standard Liège -49
- 2010/11: Anderlecht -32
- 2010/11: Club Brugge -26
- 2010/11: Gent -28
- 2010/11: Lokeren -25
- 2010/11: KV Mechelen -8
- 2010/11: Westerlo -16
- 2010/11: Cercle Brugge -10
- 2010/11: Kortrijk -3
- 2010/11: Zulte Waregem -10
- 2010/11: Sint-Truiden -6
- 2010/11: Germinal Beerschot -6
- 2010/11: Lierse -8
- 2010/11: Eupen -20
- 2010/11: Charleroi -19
- 2011/12: Anderlecht -33
- 2011/12: Club Brugge -30
- 2011/12: Genk -23
- 2011/12: Gent -34
- 2011/12: Standard Liège -25
- 2011/12: Kortrijk -23
- 2011/12: Cercle Brugge -17
- 2011/12: Lokeren -6
- 2011/12: KV Mechelen -4
- 2011/12: Mons -11
- 2011/12: Germinal Beerschot -7
- 2011/12: Lierse -7
- 2011/12: Zulte Waregem -8
- 2011/12: OH Leuven -10
- 2011/12: Westerlo -17
- 2011/12: Sint-Truiden -19
- 2012/13: Anderlecht -33
- 2012/13: Zulte Waregem -31
- 2012/13: Club Brugge -27
- 2012/13: Standard Liège -28
- 2012/13: Genk -27
- 2012/13: Lokeren -25
- 2012/13: Mons -10
- 2012/13: KV Mechelen -10
- 2012/13: Kortrijk -5
- 2012/13: OH Leuven -10
- 2012/13: Charleroi -7
- 2012/13: Gent -23
- 2012/13: Waasland-Beveren -5
- 2012/13: Lierse -4
- 2012/13: Cercle Brugge -14
- 2012/13: Germinal Beerschot -20
- 2013/14: Anderlecht -28
- 2013/14: Standard Liège -33
- 2013/14: Club Brugge -31
- 2013/14: Zulte Waregem -26
- 2013/14: Lokeren -25
- 2013/14: Genk -22
- 2013/14: Gent -10
- 2013/14: Kortrijk -15
- 2013/14: Oostende -16
- 2013/14: Charleroi -13
- 2013/14: Lierse -6
- 2013/14: KV Mechelen -9
- 2013/14: Waasland-Beveren -4
- 2013/14: OH Leuven -24
- 2013/14: Mons -22
- 2014/15: Gent -28
- 2014/15: Club Brugge -30
- 2014/15: Anderlecht -28
- 2014/15: Standard Liège -26
- 2014/15: Charleroi -27
- 2014/15: Kortrijk -25
- 2014/15: Genk -15
- 2014/15: Lokeren -14
- 2014/15: KV Mechelen -22
- 2014/15: Oostende -6
- 2014/15: Westerlo -5
- 2014/15: Zulte Waregem -4
- 2014/15: Royal Excel Mouscron -10
- 2014/15: Waasland-Beveren -1
- 2014/15: Lierse -22
- 2014/15: Cercle Brugge -21
- 2015/16: Club Brugge -32
- 2015/16: Anderlecht -27
- 2015/16: Gent -30
- 2015/16: Genk -27
- 2015/16: Oostende -24
- 2015/16: Zulte Waregem -21
- 2015/16: Standard Liège -10
- 2015/16: Charleroi -20
- 2015/16: Kortrijk -14
- 2015/16: KV Mechelen -7
- 2015/16: Lokeren -11
- 2015/16: Waasland-Beveren -4
- 2015/16: Sint-Truiden -3
- 2015/16: Royal Excel Mouscron -5
- 2016/17: Anderlecht -30
- 2016/17: Club Brugge -29
- 2016/17: Gent -25
- 2016/17: Oostende -28
- 2016/17: Charleroi -24
- 2016/17: Zulte Waregem -27
- 2016/17: KV Mechelen -16
- 2016/17: Genk -29
- 2016/17: Standard Liège -17
- 2016/17: Kortrijk -12
- 2016/17: Lokeren -15
- 2016/17: Sint-Truiden -22
- 2016/17: Eupen -13
- 2016/17: Waasland-Beveren -15
- 2016/17: Royal Excel Mouscron -8
- 2017/18: Club Brugge -33
- 2017/18: Standard Liège -22
- 2017/18: Anderlecht -27
- 2017/18: Gent -25
- 2017/18: Genk -22
- 2017/18: Charleroi -25
- 2017/18: Kortrijk -19
- 2017/18: Antwerp -14
- 2017/18: Zulte Waregem -29
- 2017/18: Sint-Truiden -17
- 2017/18: Oostende -14
- 2017/18: Waasland-Beveren -8
- 2017/18: Lokeren -22
- 2017/18: Royal Excel Mouscron -14
- 2017/18: Eupen -8
- 2018/19: Genk -31
- 2018/19: Club Brugge -28
- 2018/19: Standard Liège -26
- 2018/19: Antwerp -27
- 2018/19: Gent -25
- 2018/19: Anderlecht -25
- 2018/19: Sint-Truiden -17
- 2018/19: Kortrijk -24
- 2018/19: Charleroi -25
- 2018/19: Royal Excel Mouscron -8
- 2018/19: Zulte Waregem -13
- 2018/19: Eupen -11
- 2018/19: Cercle Brugge -7
- 2018/19: Oostende -12
- 2018/19: Waasland-Beveren -13
- 2020/21: Club Brugge -38
- 2020/21: Genk -28
- 2020/21: Antwerp -30
- 2020/21: Anderlecht -29
- 2020/21: Oostende -7
- 2020/21: Standard Liège -3
- 2020/21: Gent -13
- 2020/21: KV Mechelen -11
- 2021/22: Club Brugge -36
- 2021/22: Union Saint-Gilloise -38
- 2021/22: Anderlecht -32
- 2021/22: Antwerp -31
- 2021/22: Gent -12
- 2021/22: Charleroi -7
- 2021/22: KV Mechelen -4
- 2021/22: Genk -11
- 2022/23: Antwerp -36
- 2022/23: Genk -37
- 2022/23: Union Saint-Gilloise -37
- 2022/23: Club Brugge -29
- 2022/23: Gent -16
- 2022/23: Standard Liège -2
- 2022/23: Westerlo -4
- 2022/23: Cercle Brugge -11
- 2023/24: Club Brugge -25
- 2023/24: Union Saint-Gilloise -35
- 2023/24: Anderlecht -31
- 2023/24: Cercle Brugge -23
- 2023/24: Genk -23
- 2023/24: Antwerp -26
- 2023/24: Gent -27
- 2023/24: KV Mechelen -16
- 2023/24: Sint-Truiden -13
- 2023/24: Standard Liège -5
- 2023/24: Westerlo -9
- 2023/24: OH Leuven -15
- 2024/25: Union Saint-Gilloise -27
- 2024/25: Club Brugge -29
- 2024/25: Genk -34
- 2024/25: Anderlecht -25
- 2024/25: Antwerp -23
- 2024/25: Gent -22
- 2024/25: Standard Liège -7
- 2024/25: KV Mechelen -12
- 2024/25: Westerlo -14
- 2024/25: Charleroi -24
- 2024/25: OH Leuven -8
- 2024/25: Dender -13
- 2025/26: Club Brugge -31
- 2025/26: Union Saint-Gilloise -33
- 2025/26: Sint-Truiden -28
- 2025/26: Anderlecht -22
- 2025/26: Gent -23
- 2025/26: KV Mechelen -22
- 2025/26: Genk -18
- 2025/26: Standard Liège -17
- 2025/26: Westerlo -13
- 2025/26: Antwerp -13
- 2025/26: Charleroi -17
- 2025/26: OH Leuven -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/bel-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1994/95 · Eendracht Aalst · KV Mechelen:** [1, 1] o ogol dá 0-0; a matriz da Wikipédia e as tabelas da RSSSF e da Wikipédia (gols de Aalst e Mechelen) dão 1-1
- **2008/09 · Lokeren · Roeselare:** [2, 1] o ogol dá 1-1; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia dão 2-1
- **2024/25 · Antwerp · Beerschot:** [5, 0] o ogol dá 4-0; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia dão 5-0
- **1995/96 · RFC Seraing (1904) · RWD Molenbeek:** [0, 1] "DA" no ogol, sem placar; football-data, engsoccerdata e as tabelas da RSSSF e da Wikipédia dão 0-1 (a matriz da Wikipédia, 0-5)

### Temporadas interrompidas (`INTERROMPIDAS`)

- **2019/20:** interrompida em março de 2020 pela pandemia de covid-19, antes da última rodada da fase regular; o Club Brugge foi declarado campeão e não houve play-offs

### Ajustes da Wikipédia que não são punição (`IGNORAR_AJUSTE`)

- (1970, 'Sint-Truiden')

### Nomes de artilheiros acertados (`NOMES_ARTILHEIRO`)

- **Ren Thirifays:** René Thirifays

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1948/49:** na matriz de resultados da Wikipédia os nomes de KVM e RCM estão cruzados (KVM leva ao Racing Mechelen); pelos códigos (KVM = KV, RCM = Racing, como na tabela do artigo) os jogos fecham com as duas tabelas (MATRIZ_CODIGOS)
- **1970/71:** a Wikipédia dá ao Sint-Truiden 12 vitórias e 2 pontos a menos (com "?"); a RSSSF e os jogos dão 11 vitórias e 29 pontos, sem punição: fica a RSSSF (IGNORAR_AJUSTE)
- **1973/74:** a tabela da Wikipédia traz 10-11-9 para o RFC Liège; a RSSSF e os jogos, 11-9-10 (mesmos pontos)
- **1981/82:** os números de Club Brugge e Cercle Brugge estão trocados na tabela da RSSSF (e na da Wikipédia, que a copia); o ogol e a matriz da Wikipédia, montados jogo a jogo, concordam entre si, e a ordem da tabela (Club 14º, Cercle 15º, empatados em pontos e vitórias) só fecha pelo saldo com os números dos jogos
- **1984/85:** a tabela da Wikipédia dá 32 jogos ao Beerschot VAC; a RSSSF e os jogos, 34
- **1985/86:** a tabela da RSSSF dá 35 jogos ao Kortrijk (erro de digitação: 8+9+17 = 34)
- **1986/87:** a tabela da RSSSF dá 33 jogos ao KSK Beveren (erro de digitação: 15+14+5 = 34)
- **1995/96:** o Eendracht Aalst perdeu por 0-5, só para ele, os jogos com o RFC Seraing (2-4 em campo) e o Sint-Truiden (0-0): os adversários ficaram com o resultado de campo (a RSSSF e a Wikipédia mostram assim); a classificação do Aalst fica com os números da tabela publicada (TABELA_OFICIAL) / Gent (gols pró) e Cercle Brugge (gols contra): 1 gol a menos na RSSSF que na Wikipédia e nos jogos
- **1999/00:** a tabela da RSSSF de 1999/00 tem as linhas do 7º ao 14º deslocadas (os números de cada clube estão na linha de outro); a da Wikipédia fecha com os jogos e dá a ordem
- **2005/06:** a tabela da Wikipédia traz 10-8-16 e 38-56 para o Cercle Brugge; a RSSSF e os jogos, 10-7-17 e 38-61
- **2008/09:** Cercle Brugge x Genk (26/04/2009): o football-data e o engsoccerdata dão 1-3; o ogol, a matriz e as tabelas, 1-2: fica 1-2
- **2012/13:** play-off do título: a tabela da Wikipédia dá 22-20 gols ao Standard e 11-13 ao Genk; o ogol e a matriz da Wikipédia (jogo a jogo) dão 18-17 e 11-12 / play-off de rebaixamento: a tabela da Wikipédia dá 3-2 gols ao Cercle Brugge; o ogol e a matriz, 5-3 (1-0, 0-1, 2-1 e 2-1)
- **2019/20:** a tabela da Wikipédia dá 36-53 gols ao Sint-Truiden; os jogos (com o 3-3 do jogo suspenso contra o Genk, que vale) dão 33-50, e a mesma tabela fecha para o Genk

### Clubes excluídos no meio da temporada (jogos anulados) (`EXCLUIDOS`)

- **2002/03:** {'KFC Lommel SK': 'desistiu com 8 rodadas por jogar (falência; só 13 jogadores); os jogos dele foram anulados'}
- **2009/10:** {'Excelsior Mouscron': 'saiu em dezembro de 2009 (falência); os jogos dele foram anulados'}

### Desempates pelo título fora da tabela (`DESEMPATES`)

- **2008/09:** Standard e Anderlecht terminaram empatados em pontos e vitórias; o título foi decidido em dois jogos (Anderlecht 1-1 Standard e Standard 1-0 Anderlecht)

### Classificação pelos números da tabela publicada (punição só para um lado) (`TABELA_OFICIAL`)

- **1995/96 · Eendracht Aalst:** perdeu por 0-5, só para ele, os jogos com RFC Seraing (2-4 em campo) e Sint-Truiden (0-0 em campo); números da tabela publicada

## 8. O que não deu para coletar

- **Datas e rodadas antes de 1960/61:** a matriz da Wikipédia não traz; o ogol não tem esses jogos.
- **Jogos dos grupos de 1898/99 a 1903/04:** só as tabelas e os jogos finais.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências e próximos passos

- Antes de 1960/61: jogos só pela matriz da Wikipédia, sem data nem rodada (o ogol não tem); quando a soma não fecha com a tabela da RSSSF, a classificação final fica com os números publicados (observação na linha). Conferir a matriz com outra fonte jogo a jogo (jornais da época, nl/fr.wikipedia) seria o próximo passo.
- 1898/99, 1899/00, 1901/02, 1902/03 e 1903/04 (grupos): só as tabelas da RSSSF e os jogos finais e de desempate; sem os jogos dos grupos e sem classificação oficial além do campeão e do torneio final.
- Autores dos gols e cartões: só com a ESPN (2006/07+), que não tem lances de 2011/12 a 2014/15 nem dos play-offs; antes e nesses anos, jogo a jogo (ficha do ogol).
- Jogos de play-off de acesso e rebaixamento contra clubes da 2ª divisão (até 2008/09) ficam de fora; desde 2016/17 os clubes da 2ª divisão no play-off europeu entram nos jogos, mas não na classificação final.
- Artilheiros só desde 1945/46 (lista da RSSSF).

## 10. Arquivos

- Código: `coleta/bel-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_bel.py`.
- Fontes baixadas: `data/coleta/bel-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-bel-1/`.
- Pacote: `data/coleta/bel-1/pacote/`; relatório: `docs/coleta/bel-1.md`.
- Refazer do zero: `python coleta/bel-1/baixar.py ...` (ver o docstring), `python coleta/bel-1/importar.py`, `python coleta/comum-europa/testar_carga.py bel-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

