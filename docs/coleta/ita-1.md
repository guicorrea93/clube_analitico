# Campeonato Italiano (1ª divisão) — coleta de dados

Gerado por `python coleta/ita-1/importar.py`. Pacote em `data/coleta/ita-1/pacote/`.

**Edições:** 124: as 29 de antes da Serie A (1898 a 1928/29, com grupos regionais e finais; em 1921/22 dois campeonatos, FIGC e CCI) e a Serie A de 1929/30 a 2025/26 (1945/46 foi a Divisione Nazionale). Sem 1915/16 a 1918/19 (Primeira Guerra) e 1943/44 e 1944/45 (Segunda Guerra).

**Total:** 34732 jogos, 94266 gols, 24598 gols com autor (ESPN; na era antiga, as fichas da Wikipédia it), 43962 cartões, 191 clubes.

**Era antiga (1898 a 1928/29):** Wikipédia em italiano, artigo de cada edição — classificação de cada grupo, Calendario (jogos com data e rodada) ou Tabellone (sem data) e fichas das finais (estádio, público, árbitro, gols). Campeão pelo albo d'oro oficial (1915 dado ao Genoa depois da guerra; 1927 revogado do Torino). Ver `coleta/ita-1/antigo.py`.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1929/30-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ita-1/` para os escudos;
- ESPN (liga `ita.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (Maurizio Mariani e outros): tabela final, nas temporadas em que a página traz uma tabela legível;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e Capocannoniere.

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Roma). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94, 3 a partir de 1994/95. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 57, saldo de gols em 27, média de gols em 11); é ele que ordena a classificação rodada a rodada. Até 2004/05, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio), que não está no pacote.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1898 | Wikipédia it | 4 | 3 (0) | 8 | 0 | 0 / 0 | Genoa | — |
| 1899 | Wikipédia it | 4 | 3 (0) | 8 | 2 | 0 / 0 | Genoa | — |
| 1900 | Wikipédia it | 6 | 9 (0) | 28 | 3 | 1 / 0 | Genoa | — |
| 1901 | Wikipédia it | 4 | 3 (0) | 13 | 5 | 0 / 0 | Milan | — |
| 1902 | Wikipédia it | 8 | 5 (0) | 20 | 4 | 0 / 0 | Genoa | — |
| 1903 | Wikipédia it | 6 | 5 (0) | 21 | 0 | 0 / 0 | Genoa | — |
| 1904 | Wikipédia it | 5 | 5 (0) | 12 | 2 | 0 / 0 | Genoa | — |
| 1905 | Wikipédia it | 6 | 12 (0) | 45 | 0 | 0 / 0 | Juventus | — |
| 1906 | Wikipédia it | 5 | 12 (0) | 31 | 0 | 0 / 0 | Milan | — |
| 1907 | Wikipédia it | 6 | 12 (0) | 36 | 6 | 0 / 0 | Milan | — |
| 1908 | Wikipédia it | 4 | 8 (0) | 19 | 0 | 0 / 0 | Pro Vercelli | — |
| 1909 | Wikipédia it | 9 | 20 (0) | 77 | 0 | 0 / 1 | Pro Vercelli | — |
| 1909/10 | Wikipédia it | 9 | 73 (0) | 306 | 0 | 0 / 1 | Inter de Milão | — |
| 1910/11 | Wikipédia it | 13 | 86 (0) | 304 | 0 | 2 / 0 | Pro Vercelli | — |
| 1911/12 | Wikipédia it | 15 | 106 (0) | 369 | 0 | 1 / 1 | Pro Vercelli | — |
| 1912/13 | Wikipédia it | 35 | 177 (0) | 710 | 0 | 5 / 1 | Pro Vercelli | — |
| 1913/14 | Wikipédia it | 45 | 376 (0) | 1580 | 1 | 6 / 0 | Casale | — |
| 1914/15 | Wikipédia it | 50 | 321 (0) | 1363 | 0 | 12 / 2 | Genoa | — |
| 1919/20 | Wikipédia it | 75 | 448 (0) | 1639 | 3 | 12 / 4 | Inter de Milão | — |
| 1920/21 | Wikipédia it | 88 | 522 (0) | 1869 | 1 | 16 / 10 | Pro Vercelli | — |
| 1921/22 (FIGC) | Wikipédia it | 46 | 214 (0) | 623 | 0 | 12 / 2 | Novese | — |
| 1921/22 (CCI) | Wikipédia it | 58 | 438 (0) | 1458 | 0 | 5 / 4 | Pro Vercelli | — |
| 1922/23 | Wikipédia it | 56 | 503 (0) | 1495 | 0 | 4 / 6 | Genoa | — |
| 1923/24 | Wikipédia it | 47 | 383 (0) | 1124 | 0 | 6 / 2 | Genoa | — |
| 1924/25 | Wikipédia it | 43 | 372 (0) | 1129 | 0 | 6 / 1 | Bologna | — |
| 1925/26 | Wikipédia it | 44 | 373 (0) | 1459 | 0 | 5 / 2 | Juventus | — |
| 1926/27 | Wikipédia it | 20 | 210 (0) | 695 | 0 | 3 / 0 | — (revogado) | — |
| 1927/28 | Wikipédia it | 22 | 276 (0) | 963 | 0 | 3 / 0 | Torino | — |
| 1928/29 | Wikipédia it | 32 | 483 (0) | 1787 | 0 | 2 / 0 | Bologna | — |
| 1929/30 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 969 | 0 | 1 / 1 | Inter de Milão | — |
| 1930/31 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 952 | 0 | 1 / 1 | Juventus | — |
| 1931/32 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 949 | 0 | 2 / 0 | Juventus | — |
| 1932/33 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 941 | 0 | 2 / 0 | Juventus | — |
| 1933/34 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 844 | 0 | 2 / 0 | Juventus | — |
| 1934/35 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 629 | 0 | 2 / 0 | Juventus | — |
| 1935/36 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 610 | 0 | 2 / 0 | Bologna | — |
| 1936/37 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 639 | 0 | 2 / 0 | Bologna | — |
| 1937/38 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 617 | 0 | 2 / 0 | Inter de Milão | — |
| 1938/39 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 593 | 0 | 2 / 0 | Bologna | — |
| 1939/40 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 625 | 0 | 2 / 0 | Inter de Milão | — |
| 1940/41 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 733 | 0 | 2 / 0 | Bologna | — |
| 1941/42 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 687 | 0 | 2 / 0 | Roma | — |
| 1942/43 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 742 | 0 | 2 / 0 | Torino | — |
| 1945/46 | engsoccerdata + ogol + Wikipédia | 25 | 348 (348) | 883 | 0 | 1 / 0 | Torino | — |
| 1946/47 | engsoccerdata + ogol + Wikipédia | 20 | 380 (380) | 1064 | 0 | 1 / 0 | Torino | — |
| 1947/48 | engsoccerdata + ogol + Wikipédia | 21 | 420 (420) | 1200 | 0 | 2 / 0 | Torino | — |
| 1948/49 | engsoccerdata + ogol + Wikipédia | 20 | 380 (380) | 1110 | 0 | 1 / 1 | Torino | — |
| 1949/50 | engsoccerdata + ogol + Wikipédia | 20 | 380 (380) | 1265 | 0 | 2 / 0 | Juventus | — |
| 1950/51 | engsoccerdata + ogol + Wikipédia | 20 | 380 (380) | 1192 | 0 | 2 / 0 | Milan | — |
| 1951/52 | engsoccerdata + ogol + Wikipédia | 20 | 380 (380) | 1101 | 0 | 1 / 0 | Juventus | — |
| 1952/53 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 830 | 0 | 2 / 0 | Inter de Milão | — |
| 1953/54 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 825 | 0 | 2 / 0 | Inter de Milão | — |
| 1954/55 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 832 | 0 | 2 / 0 | Milan | — |
| 1955/56 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 838 | 0 | 2 / 0 | Fiorentina | — |
| 1956/57 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 845 | 0 | 2 / 0 | Milan | — |
| 1957/58 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 880 | 0 | 1 / 0 | Juventus | — |
| 1958/59 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 897 | 0 | 2 / 0 | Milan | — |
| 1959/60 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 792 | 0 | 1 / 1 | Juventus | Genoa -18 pontos |
| 1960/61 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 814 | 0 | 2 / 0 | Juventus | — |
| 1961/62 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 770 | 0 | 1 / 0 | Milan | — |
| 1962/63 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 741 | 0 | 2 / 0 | Inter de Milão | — |
| 1963/64 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 647 | 0 | 2 / 0 | Bologna | — |
| 1964/65 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 640 | 0 | 2 / 0 | Inter de Milão | — |
| 1965/66 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 668 | 0 | 2 / 0 | Inter de Milão | — |
| 1966/67 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 613 | 0 | 1 / 0 | Juventus | — |
| 1967/68 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 504 | 0 | 2 / 0 | Milan | — |
| 1968/69 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 497 | 0 | 2 / 0 | Fiorentina | — |
| 1969/70 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 464 | 0 | 2 / 0 | Cagliari | — |
| 1970/71 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 505 | 0 | 2 / 0 | Inter de Milão | — |
| 1971/72 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 483 | 0 | 2 / 0 | Juventus | — |
| 1972/73 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 449 | 0 | 2 / 0 | Juventus | — |
| 1973/74 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 497 | 0 | 1 / 0 | Lazio | Sampdoria -3 pontos; Foggia -6 pontos |
| 1974/75 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 467 | 0 | 2 / 0 | Juventus | — |
| 1975/76 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 542 | 0 | 2 / 0 | Torino | — |
| 1976/77 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 532 | 0 | 1 / 0 | Juventus | Napoli -1 pontos |
| 1977/78 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 512 | 0 | 2 / 0 | Juventus | — |
| 1978/79 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 455 | 0 | 2 / 0 | Milan | — |
| 1979/80 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 452 | 0 | 2 / 0 | Inter de Milão | — |
| 1980/81 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 459 | 0 | 1 / 0 | Juventus | Bologna -5 pontos; Avellino -5 pontos; Perugia -5 pontos |
| 1981/82 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 474 | 0 | 2 / 0 | Juventus | — |
| 1982/83 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 505 | 0 | 2 / 0 | Roma | — |
| 1983/84 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 573 | 0 | 2 / 0 | Juventus | — |
| 1984/85 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 504 | 0 | 2 / 0 | Verona | — |
| 1985/86 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 495 | 0 | 2 / 0 | Juventus | — |
| 1986/87 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 462 | 0 | 2 / 0 | Napoli | Udinese -9 pontos |
| 1987/88 | engsoccerdata + ogol + Wikipédia | 16 | 240 (240) | 504 | 0 | 2 / 0 | Milan | Empoli -5 pontos |
| 1988/89 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 645 | 0 | 2 / 0 | Inter de Milão | — |
| 1989/90 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 684 | 0 | 2 / 0 | Napoli | — |
| 1990/91 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 702 | 0 | 2 / 0 | Sampdoria | — |
| 1991/92 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 695 | 0 | 2 / 0 | Milan | — |
| 1992/93 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 858 | 0 | 2 / 0 | Milan | — |
| 1993/94 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 741 | 0 | 1 / 1 | Milan | — |
| 1994/95 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 773 | 0 | 2 / 0 | Juventus | — |
| 1995/96 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 805 | 0 | 1 / 0 | Milan | — |
| 1996/97 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 808 | 0 | 2 / 0 | Juventus | — |
| 1997/98 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 847 | 0 | 2 / 0 | Juventus | — |
| 1998/99 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 845 | 0 | 1 / 0 | Milan | Empoli -2 pontos |
| 1999/00 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 764 | 0 | 1 / 0 | Lazio | — |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 845 | 0 | 2 / 0 | Roma | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 806 | 787 | 2 / 0 | Juventus | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 789 | 787 | 2 / 0 | Juventus | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 18 | 306 (306) | 816 | 814 | 1 / 0 | Milan | — |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 960 | 960 | 1 / 0 | — | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 991 | 988 | 1 / 0 | Inter de Milão | Milan -30 pontos; Fiorentina -30 pontos; Lazio -30 pontos |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 969 | 948 | 1 / 0 | Inter de Milão | Lazio -3 pontos; Milan -8 pontos; Fiorentina -15 pontos; Reggina -11 pontos; Siena -1 pontos |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 970 | 959 | 2 / 0 | Inter de Milão | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 988 | 975 | 2 / 0 | Inter de Milão | — |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 992 | 989 | 2 / 0 | Inter de Milão | — |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 955 | 952 | 2 / 0 | Milan | Bologna -3 pontos |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 972 | 960 | 2 / 0 | Juventus | Atalanta -6 pontos |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1003 | 1000 | 1 / 0 | Juventus | Sampdoria -1 pontos; Atalanta -2 pontos; Torino -1 pontos; Siena -6 pontos |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1035 | 1025 | 2 / 0 | Juventus | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1024 | 1021 | 2 / 0 | Juventus | Parma -7 pontos |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 979 | 979 | 2 / 0 | Juventus | — |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + Wikipédia | 20 | 380 (380) | 1123 | 1120 | 1 / 0 | Juventus | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1017 | 1017 | 2 / 0 | Juventus | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1019 | 1019 | 2 / 0 | Juventus | Chievo -3 pontos |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1154 | 1154 | 2 / 0 | Juventus | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1163 | 1160 | 2 / 0 | Inter de Milão | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1089 | 1089 | 2 / 0 | Milan | — |
| 2022/23 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 974 | 974 | 2 / 0 | Napoli | Juventus -10 pontos |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 992 | 992 | 2 / 0 | Inter de Milão | — |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 973 | 973 | 2 / 0 | Napoli | — |
| 2025/26 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 922 | 922 | 2 / 0 | Inter de Milão | — |

## Conferência e ocorrências, temporada a temporada

### 1898

- sem ocorrências

### 1899

- sem ocorrências

### 1900

- sem ocorrências

### 1901

- sem ocorrências

### 1902

- sem ocorrências

### 1903

- sem ocorrências

### 1904

- sem ocorrências

### 1905

- sem ocorrências

### 1906

- sem ocorrências

### 1907

- sem ocorrências

### 1908

- o Campionato Italiano (só com jogadores italianos), o que vale o título; o Campionato Federale do mesmo ano, aberto a estrangeiros, não é contado

### 1909

- o Campionato Federale, que passou a valer o título; o Campionato Italiano do mesmo ano não é contado
- classificação do Eliminatórias lombarda x jogos — US Milanese tabela [2, 2, 0, 0, 5, 1, 4] jogos [4, 4, 0, 0, 10, 2, 8]
- classificação do Eliminatórias lombarda x jogos — Milan tabela [2, 1, 0, 1, 4, 5, 2] jogos [4, 2, 0, 2, 8, 10, 4]
- classificação do Eliminatórias lombarda x jogos — Inter de Milão tabela [2, 0, 0, 2, 2, 5, 0] jogos [4, 0, 0, 4, 4, 10, 0]

### 1909/10

- classificação do Fase única x jogos — Juventus tabela [16, 8, 2, 6, 29, 20, 18] jogos [16, 8, 2, 6, 28, 19, 18]
- classificação do Fase única x jogos — Torino tabela [16, 8, 1, 7, 45, 30, 17] jogos [16, 8, 1, 7, 43, 30, 17]
- classificação do Fase única x jogos — Genoa tabela [16, 7, 3, 6, 31, 23, 17] jogos [16, 7, 3, 6, 29, 23, 17]
- classificação do Fase única x jogos — Milan tabela [16, 6, 1, 9, 24, 36, 13] jogos [16, 6, 1, 9, 23, 36, 13]
- classificação do Fase única x jogos — Andrea Doria tabela [16, 5, 1, 10, 18, 40, 11] jogos [16, 5, 1, 10, 18, 39, 11]

### 1910/11

- sem ocorrências

### 1911/12

- classificação do Campeonato do Noroeste x jogos — Casale tabela [18, 6, 3, 9, 20, 27, 15] jogos [18, 6, 3, 9, 19, 26, 15]

### 1912/13

- classificação do Torneio do Centro-Sul · Seção toscana x jogos — Virtus Juventusque tabela [6, 4, 1, 2, 11, 8, 9] jogos [6, 4, 1, 1, 11, 8, 9]

### 1913/14

- sem ocorrências

### 1914/15

- interrompido em 23/05/1915 pela entrada da Itália na Primeira Guerra Mundial, antes do fim do grupo final do Norte e da final nacional; a federação deu o título ao Genoa (líder do grupo final do Norte) depois da guerra
- classificação do Torneio do Centro-Sul · Seção toscana x jogos — Lucchese tabela [12, 7, 2, 3, 23, 11, 16] jogos [12, 6, 3, 3, 21, 11, 15]
- classificação do Torneio do Centro-Sul · Seção toscana x jogos — SPES Livorno tabela [12, 3, 3, 6, 13, 18, 9] jogos [11, 3, 3, 5, 13, 18, 9]
- classificação do Torneio do Centro-Sul · Seção toscana x jogos — Virtus Juventusque tabela [12, 2, 3, 7, 15, 27, 7] jogos [11, 2, 3, 6, 15, 25, 7]
- classificação do Torneio do Centro-Sul · Seção do Lácio x jogos — Roman tabela [10, 9, 0, 1, 42, 13, 18] jogos [10, 9, 0, 1, 42, 14, 18]
- classificação do Torneio do Centro-Sul · Seção do Lácio x jogos — Fortitudo tabela [10, 3, 0, 7, 12, 35, 6] jogos [10, 3, 0, 7, 13, 35, 6]
- classificação do Torneio do Centro-Sul · Seção do Lácio x jogos — Juventus Roma tabela [10, 2, 1, 7, 14, 31, 5] jogos [10, 2, 1, 7, 14, 32, 5]
- classificação do Torneio do Centro-Sul · Seção do Lácio x jogos — Pro Roma tabela [10, 2, 1, 7, 17, 38, 5] jogos [10, 2, 1, 7, 18, 38, 5]

### 1919/20

- classificação do Torneio principal · Grupos regionais de qualificação · Seção lombarda · Grupo A x jogos — AC Libertas tabela [10, 2, 1, 7, 14, 26, 5] jogos [10, 2, 1, 7, 11, 31, 5]
- classificação do Torneio principal · Grupos regionais de qualificação · Seção lombarda · Grupo A x jogos — Cremonese tabela [10, 2, 1, 7, 11, 31, 5] jogos [10, 2, 1, 7, 14, 26, 5]
- classificação do Torneio principal · Semifinais nacionais · Grupo C x jogos — Novara tabela [10, 5, 1, 3, 21, 16, 11] jogos [10, 5, 1, 4, 21, 16, 11]
- classificação do Torneio do Centro-Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Audace Roma tabela [12, 6, 4, 2, 19, 12, 16] jogos [12, 6, 4, 2, 19, 11, 16]
- classificação do Torneio do Centro-Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Lazio tabela [12, 6, 2, 4, 22, 11, 14] jogos [12, 6, 2, 4, 21, 11, 14]
- classificação do Torneio do Centro-Sul · Semifinais inter-regionais · Grupo B x jogos — Audace Roma tabela [4, 1, 0, 3, 7, 5, 4] jogos [4, 2, 0, 2, 7, 5, 4]

### 1920/21

- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lígure x jogos — Andrea Doria tabela [14, 9, 4, 1, 33, 9, 22] jogos [14, 9, 4, 1, 32, 9, 22]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lígure x jogos — Spezia tabela [14, 6, 5, 3, 17, 9, 17] jogos [14, 6, 5, 3, 18, 9, 17]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lígure x jogos — Spes Genova tabela [14, 5, 2, 7, 16, 27, 12] jogos [14, 5, 2, 7, 16, 26, 12]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lígure x jogos — Sestrese tabela [14, 2, 5, 7, 11, 23, 9] jogos [14, 2, 5, 7, 11, 24, 9]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo A x jogos — Casteggio tabela [6, 3, 1, 2, 18, 12, 7] jogos [6, 3, 1, 2, 18, 13, 7]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo A x jogos — Giovani Calciatori Legnanesi tabela [6, 2, 1, 3, 16, 20, 5] jogos [6, 2, 1, 3, 17, 20, 5]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo C x jogos — Varese tabela [6, 1, 0, 5, 5, 15, 2] jogos [6, 0, 0, 6, 3, 15, 0]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo C x jogos — Pro Sesto tabela [6, 1, 0, 5, 7, 22, 2] jogos [6, 2, 0, 4, 7, 20, 4]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo D x jogos — Como tabela [6, 3, 2, 1, 12, 10, 8] jogos [6, 3, 2, 1, 12, 8, 8]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo D x jogos — Chiasso tabela [6, 1, 1, 4, 6, 14, 3] jogos [6, 1, 1, 4, 5, 14, 3]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo D x jogos — Stelvio Milano tabela [6, 0, 3, 3, 4, 12, 3] jogos [6, 0, 3, 3, 4, 13, 3]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo final regional x jogos — US Milanese tabela [10, 5, 1, 4, 15, 14, 11] jogos [10, 5, 1, 4, 15, 13, 11]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo final regional x jogos — Trevigliese tabela [10, 1, 0, 9, 9, 28, 2] jogos [10, 1, 0, 9, 8, 28, 2]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo A x jogos — Pastore tabela [10, 1, 1, 8, 10, 32, 3] jogos [10, 1, 1, 8, 10, 33, 3]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo A x jogos — Carignano tabela [10, 0, 1, 9, 5, 43, 1] jogos [10, 0, 1, 9, 5, 42, 1]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo B x jogos — Pro Vercelli tabela [10, 6, 1, 3, 23, 10, 13] jogos [10, 6, 1, 3, 24, 10, 13]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo B x jogos — Biellese tabela [10, 5, 1, 4, 16, 17, 11] jogos [10, 5, 1, 4, 16, 18, 11]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo B x jogos — Valenzana tabela [10, 2, 1, 7, 12, 25, 5] jogos [10, 2, 1, 7, 10, 23, 5]
- classificação do Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa · Grupo B x jogos — Amatori Torino tabela [10, 0, 0, 10, 3, 44, 0] jogos [10, 0, 0, 10, 1, 42, 0]
- classificação do Torneio do Norte · Semifinais nacionais · Grupo A x jogos — Genoa tabela [6, 2, 3, 1, 9, 8, 7] jogos [6, 2, 3, 1, 10, 9, 7]
- classificação do Torneio do Norte · Semifinais nacionais · Grupo A x jogos — Novara tabela [6, 2, 2, 2, 6, 6, 6] jogos [6, 2, 2, 2, 7, 7, 6]
- classificação do Torneio peninsular · Grupos regionais de qualificação · Seção da Campânia · Grupo final regional x jogos — Naples tabela [6, 3, 1, 2, 9, 7, 7] jogos [6, 3, 1, 2, 8, 7, 7]
- classificação do Torneio peninsular · Grupos regionais de qualificação · Seção da Campânia · Grupo final regional x jogos — Puteolana tabela [6, 5, 0, 1, 11, 7, 10] jogos [6, 5, 0, 1, 11, 6, 10]
- classificação do Torneio peninsular · Grupos regionais de qualificação · Seção do Lácio x jogos — Audace Roma tabela [14, 5, 1, 8, 30, 34, 11] jogos [14, 5, 1, 8, 29, 34, 11]
- classificação do Torneio peninsular · Grupos regionais de qualificação · Seção do Lácio x jogos — US Romana tabela [14, 5, 0, 9, 23, 35, 10] jogos [14, 5, 0, 9, 22, 37, 10]
- classificação do Torneio peninsular · Grupos regionais de qualificação · Seção do Lácio x jogos — Vittoria Roma tabela [14, 2, 3, 9, 12, 44, 7] jogos [14, 2, 3, 9, 15, 43, 7]

### 1921/22 (FIGC)

- temporada com dois campeonatos, depois da cisão dos grandes clubes: o da FIGC (Prima Categoria, Novese) e o da CCI (Prima Divisione, Pro Vercelli); os dois títulos são oficiais
- classificação do Grupos regionais de qualificação · Seção lígure x jogos — Sampierdarenese tabela [10, 8, 2, 0, 25, 7, 18] jogos [9, 8, 1, 0, 23, 5, 17]
- classificação do Grupos regionais de qualificação · Seção lígure x jogos — Rivarolese tabela [10, 4, 2, 4, 13, 13, 10] jogos [9, 4, 1, 4, 11, 11, 9]
- classificação do Grupos regionais de qualificação · Seção toscana x jogos — Pro Livorno tabela [10, 7, 1, 2, 20, 8, 15] jogos [10, 7, 1, 2, 22, 8, 15]
- classificação do Grupos regionais de qualificação · Seção toscana x jogos — Libertas Firenze tabela [10, 5, 2, 3, 11, 15, 12] jogos [10, 5, 2, 3, 11, 16, 12]
- classificação do Grupos regionais de qualificação · Seção toscana x jogos — Prato tabela [10, 1, 3, 6, 11, 18, 5] jogos [10, 1, 3, 6, 10, 18, 5]

### 1921/22 (CCI)

- 9 jogos do calendário sem placar (não disputados): Libertas-Vigor; Messinese-Vigor; Libertas-Palermo; Messinese-Libertas; Messina-Vigor; Umberto I-Vigor; Libertas-Messina; Vigor-Palermo
- temporada com dois campeonatos, depois da cisão dos grandes clubes: o da CCI (Prima Divisione, Pro Vercelli) e o da FIGC (Prima Categoria, Novese); os dois títulos são oficiais
- classificação do Liga Norte · Grupo B x jogos — Savona tabela [22, 9, 2, 11, 28, 33, 20] jogos [22, 8, 2, 12, 28, 36, 18]
- classificação do Liga Norte · Grupo B x jogos — Brescia tabela [22, 6, 3, 13, 19, 33, 15] jogos [22, 7, 3, 12, 22, 33, 17]
- classificação do Liga Sul · Seção do Lácio x jogos — Fortitudo tabela [16, 13, 2, 1, 35, 10, 28] jogos [18, 15, 2, 1, 44, 11, 32]
- classificação do Liga Sul · Seção do Lácio x jogos — Alba Roma tabela [16, 11, 2, 3, 38, 13, 24] jogos [18, 12, 2, 4, 59, 13, 26]
- classificação do Liga Sul · Seção do Lácio x jogos — Juventus Audax tabela [16, 8, 4, 4, 45, 26, 20] jogos [17, 9, 4, 4, 43, 26, 22]
- classificação do Liga Sul · Seção do Lácio x jogos — Lazio tabela [16, 8, 4, 4, 37, 22, 20] jogos [16, 8, 4, 4, 35, 22, 20]
- classificação do Liga Sul · Seção do Lácio x jogos — US Romana tabela [16, 5, 4, 7, 24, 29, 14] jogos [17, 7, 4, 6, 33, 28, 18]
- classificação do Liga Sul · Seção das Marcas · Grupo final x jogos — Ancona tabela [6, 6, 0, 0, 19, 3, 12] jogos [4, 4, 0, 0, 13, 3, 8]
- classificação do Liga Sul · Seção das Marcas · Grupo final x jogos — Vigor Senigallia tabela [6, 3, 1, 2, 13, 12, 7] jogos [4, 3, 1, 0, 13, 6, 7]
- classificação do Liga Sul · Seção das Marcas · Grupo final x jogos — Helvia Recina tabela [6, 2, 0, 4, 8, 13, 4] jogos [4, 0, 0, 4, 3, 10, 0]
- classificação do Liga Sul · Seção das Marcas · Grupo final x jogos — Macerata tabela [6, 0, 1, 5, 9, 21, 1] jogos [4, 0, 1, 3, 6, 16, 1]
- classificação do Liga Sul · Seção da Apúlia x jogos — Pro Italia Taranto tabela [6, 3, 2, 1, 11, 6, 8] jogos [6, 3, 2, 1, 18, 6, 8]
- classificação do Liga Sul · Seção da Apúlia x jogos — Liberty Bari tabela [6, 2, 2, 2, 13, 8, 6] jogos [5, 1, 2, 2, 5, 8, 4]
- classificação do Liga Sul · Seção da Apúlia x jogos — Veloce Taranto tabela [6, 0, 1, 5, 1, 20, 1] jogos [5, 0, 1, 4, 1, 19, 1]

### 1922/23

- classificação do Liga Norte · Grupo A x jogos — Pro Vercelli tabela [22, 17, 2, 3, 44, 15, 36] jogos [22, 17, 2, 3, 49, 14, 36]
- classificação do Liga Norte · Grupo A x jogos — Casale tabela [22, 7, 9, 6, 23, 18, 23] jogos [22, 7, 9, 6, 23, 17, 23]
- classificação do Liga Norte · Grupo A x jogos — Inter de Milão tabela [22, 8, 5, 9, 32, 37, 21] jogos [22, 8, 5, 9, 33, 37, 21]
- classificação do Liga Norte · Grupo A x jogos — Virtus Bologna tabela [22, 8, 5, 9, 16, 23, 21] jogos [22, 8, 5, 9, 15, 22, 21]
- classificação do Liga Norte · Grupo A x jogos — US Torinese tabela [22, 6, 4, 12, 23, 36, 16] jogos [22, 6, 4, 12, 23, 41, 16]
- classificação do Liga Norte · Grupo B x jogos — Juventus tabela [22, 10, 5, 7, 31, 23, 25] jogos [22, 10, 5, 7, 31, 21, 25]
- classificação do Liga Norte · Grupo B x jogos — Modena tabela [22, 10, 4, 8, 27, 23, 24] jogos [22, 10, 4, 8, 24, 23, 24]
- classificação do Liga Norte · Grupo B x jogos — Esperia tabela [22, 1, 4, 17, 11, 50, 5] jogos [22, 1, 4, 17, 11, 49, 6]
- classificação do Liga Norte · Grupo C x jogos — Livorno tabela [22, 13, 4, 5, 43, 19, 30] jogos [22, 13, 3, 6, 42, 19, 29]
- classificação do Liga Norte · Grupo C x jogos — Novara tabela [22, 12, 2, 8, 42, 24, 26] jogos [22, 12, 2, 8, 41, 24, 26]
- classificação do Liga Norte · Grupo C x jogos — Andrea Doria tabela [22, 9, 6, 7, 40, 29, 24] jogos [22, 10, 5, 7, 40, 28, 25]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção siciliana x jogos — Messina FC tabela [4, 1, 2, 1, 4, 3, 4] jogos [2, 0, 2, 0, 1, 1, 2]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção siciliana x jogos — Palermo FC tabela [4, 1, 2, 1, 5, 5, 4] jogos [2, 0, 2, 0, 1, 1, 2]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção siciliana x jogos — Libertas Palermo tabela [4, 1, 2, 1, 5, 6, 4] jogos [2, 0, 2, 0, 2, 2, 2]
- classificação do Liga Sul · Semifinais inter-regionais · Grupo A x jogos — Ancona tabela [6, 3, 1, 2, 8, 5, 7] jogos [6, 3, 1, 2, 10, 9, 7]
- classificação do Liga Sul · Semifinais inter-regionais · Grupo A x jogos — Alba Roma tabela [6, 3, 1, 2, 10, 9, 7] jogos [6, 3, 1, 2, 8, 5, 7]
- classificação do Liga Sul · Semifinais inter-regionais · Grupo B x jogos — Libertas Palermo tabela [6, 2, 0, 4, 10, 20, 3] jogos [6, 2, 0, 4, 10, 20, 4]

### 1923/24

- classificação do Liga Norte · Grupo B x jogos — Torino tabela [22, 12, 6, 4, 43, 22, 30] jogos [21, 12, 6, 3, 43, 21, 30]
- classificação do Liga Norte · Grupo B x jogos — Pisa tabela [22, 7, 8, 7, 26, 35, 22] jogos [22, 7, 8, 7, 28, 37, 22]
- classificação do Liga Norte · Grupo B x jogos — Andrea Doria tabela [22, 7, 7, 8, 28, 26, 21] jogos [22, 7, 7, 8, 30, 28, 21]
- classificação do Liga Norte · Grupo B x jogos — Spezia tabela [22, 7, 3, 12, 16, 35, 17] jogos [21, 6, 3, 12, 15, 35, 15]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção da Apúlia x jogos — Audace Taranto tabela [10, 7, 2, 1, 16, 4, 16] jogos [8, 6, 1, 1, 15, 4, 13]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção da Apúlia x jogos — Ideale Bari tabela [10, 7, 1, 2, 20, 6, 15] jogos [8, 5, 1, 2, 15, 6, 11]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção da Apúlia x jogos — Enotria Taranto tabela [10, 4, 2, 4, 10, 11, 10] jogos [8, 3, 1, 4, 8, 10, 7]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção da Apúlia x jogos — Liberty Bari tabela [10, 4, 2, 4, 12, 13, 10] jogos [8, 4, 1, 3, 12, 12, 9]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção da Apúlia x jogos — Pro Italia Taranto tabela [10, 4, 0, 6, 8, 13, 8] jogos [8, 4, 0, 4, 8, 8, 8]

### 1924/25

- classificação do Liga Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Lazio tabela [8, 5, 1, 2, 20, 10, 11] jogos [6, 3, 1, 2, 14, 10, 7]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Pro Roma tabela [8, 0, 2, 6, 4, 21, 2] jogos [6, 0, 2, 4, 4, 15, 2]

### 1925/26

- classificação do Liga Norte · Grupo B x jogos — Milan tabela [22, 10, 2, 10, 43, 39, 22] jogos [22, 10, 2, 10, 42, 39, 22]
- classificação do Liga Norte · Grupo B x jogos — Mantova tabela [22, 2, 4, 16, 24, 81, 8] jogos [22, 2, 4, 16, 24, 80, 8]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Alba Roma tabela [10, 8, 1, 1, 41, 13, 17] jogos [9, 7, 1, 1, 39, 12, 15]
- classificação do Liga Sul · Grupos regionais de qualificação · Seção do Lácio x jogos — Pro Roma tabela [10, 0, 0, 10, 5, 44, 0] jogos [9, 0, 0, 9, 4, 42, 0]

### 1926/27

- título revogado: o Torino ganhou o grupo final, mas a federação tirou o título em 03/11/1927 (caso Allemandi, suborno de um jogador da Juventus); o título não foi dado a ninguém

### 1927/28

- sem ocorrências

### 1928/29

- sem ocorrências

### 1929/30

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- resultado do tribunal: US Cremonese x AC Milan fica 0-2 (base 0-3) — 0-2 a tavolino (RSSSF "0-2 *"; matriz da Wikipédia it)
- tabela publicada x jogos (Wikipédia) — Genoa CFC tabela [34, 20, 8, 6, 63, 36, 48] jogos [34, 20, 8, 6, 63, 39, 48]
- tabela publicada x jogos (Wikipédia) — Unione Triestina tabela [34, 11, 6, 17, 42, 78, 28] jogos [34, 11, 6, 17, 42, 59, 28]

### 1930/31

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos, menos o Brescia: a RSSSF dá 32 pontos, mas a base, o ogol e a Wikipédia dão 13 vitórias e 8 empates (34 pontos)
- resultado do tribunal: Legnano x Lazio Roma fica 0-2 (base 0-1) — 0-2 a tavolino (matriz da Wikipédia it)
- 27 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 26 jogos (ex.: Genoa CFC x Pro Vercelli: base 1930-12-21, ogol 1930-10-21); fica a da base
- pontos da última classificação da RSSSF x jogos — Brescia Calcio RSSSF 32 jogos 34

### 1931/32

- 1 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Bari 2-1 Brescia (1932-06-16)

### 1932/33

- sem ocorrências

### 1933/34

- placar corrigido: AC Milan x Casale de 6-1 para 6-2 — o ogol e a tabela da Wikipédia fecham com este placar
- placar corrigido: AS Livorno x US Palermo de 3-1 para 3-2 — o ogol e a tabela da Wikipédia fecham com este placar
- placar corrigido: Torino FC x AS Roma de 3-1 para 3-6 — o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 40, Torino 29)
- placar corrigido: Juventus x Bologna FC de 4-2 para 4-1 — o ogol e a tabela da Wikipédia fecham com este placar
- 75 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 75 jogos (ex.: Calcio Padova x AS Roma: base 1934-01-11, ogol 1933-12-17); fica a da base

### 1934/35

- placar corrigido: US Alessandria 1912 x AS Roma de 1-1 para 1-6 — o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 35, Alessandria 29)
- 33 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 33 jogos (ex.: Brescia Calcio x Sampierdarenese: base 1934-12-06, ogol 1934-12-02); fica a da base

### 1935/36

- sem ocorrências

### 1936/37

- sem ocorrências

### 1937/38

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Genoa CFC', 'AC Milan']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1938/39

- sem ocorrências

### 1939/40

- sem ocorrências

### 1940/41

- sem ocorrências

### 1941/42

- sem ocorrências

### 1942/43

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: Sampierdarenese x AS Roma: base 1943-02-18, ogol 1942-11-08); fica a da base
- Bari: rebaixado em campo (triangular com Triestina e Venezia) e readmitido
- Sampierdarenese: rebaixado em campo (como Liguria) e readmitido
- 4 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Bari 1-1 Venezia (1943-05-02); Triestina 2-0 Venezia (1943-05-09); Triestina 3-2 Bari (1943-05-16); Venezia 3-0 Bari (1943-06-06)

### 1945/46

- Andrea Doria x Sampierdarenese (21/10/1945): o ogol traz 0-1 e a base 0-0. Os grupos de 1945/46 não têm tabela publicada legível para desempatar: fica a base
- 14 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — Andrea Doria x Sampierdarenese (1945-10-21): base 0-0, ogol 0-1
- data diferente no ogol em 14 jogos (ex.: Ancona Calcio x US Palermo: base 1946-01-13, ogol 1945-11-04); fica a da base
- Andrea Doria não está na temporada seguinte, mas não caiu: fundiu-se com a Sampierdarenese em 1946 e formou a Sampdoria
- Sampierdarenese não está na temporada seguinte, mas não caiu: fundiu-se com a Andrea Doria em 1946 e formou a Sampdoria
- Ancona não está na temporada seguinte, mas não caiu: clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- Palermo FC não está na temporada seguinte, mas não caiu: clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- Pescara não está na temporada seguinte, mas não caiu: clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- Salernitana não está na temporada seguinte, mas não caiu: clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- Siena não está na temporada seguinte, mas não caiu: clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B

### 1946/47

- a base não fecha nesta temporada (370 jogos): montada pelo calendário do ogol (380 jogos), com 380 jogos da base
- 2 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 2 jogos (ex.: AC Milan x Unione Triestina: base 1947-01-01, ogol 1946-09-29); fica a da base

### 1947/48

- a base traz só 380 dos 420 jogos (21 clubes): os que faltam entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- a base não fecha nesta temporada (380 jogos): montada pelo calendário do ogol (420 jogos), com 379 jogos da base
- 41 jogos só no ogol, que entram com o placar do ogol: SSC Napoli 1-2 US Alessandria 1912 (1947-10-26); US Alessandria 1912 2-2 Lazio Roma (1948-06-27); Atalanta 1-0 ACF Fiorentina (1948-06-27); Bologna FC 0-0 AS Bari (1948-06-27); Genoa CFC 1-2 Torino FC (1948-06-27); Juventus 2-0 Salernitana Calcio 1919 (1948-06-27) ...
- 1 jogos da base fora do calendário do ogol, descartados: US Alessandria 1912 2-1 SSC Napoli (1947-10-26)
- 193 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 193 jogos (ex.: Atalanta x Lucchese: base 1947-12-14, ogol 1947-12-07); fica a da base
- Napoli declassado ao último lugar por tentativa de corrupção (terminou em 18º em campo); Wikipédia it, Serie A 1947-1948, classifica finale; na classificação final fica em último

### 1948/49

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos (Bologna: a Wikipédia dá 11 vitórias e 18 empates; os jogos e a RSSSF, 12 e 17)
- 13 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 13 jogos (ex.: Atalanta x Sampdoria: base 1948-12-23, ogol 1948-12-08); fica a da base
- tabela publicada x jogos (Wikipédia) — Bologna FC tabela [38, 11, 18, 9, 53, 46, 40] jogos [38, 12, 17, 9, 53, 46, 41]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Lucchese', 'Unione Triestina']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1949/50

- 13 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 13 jogos (ex.: Pro Patria x Sampdoria: base 1950-01-05, ogol 1949-12-26); fica a da base

### 1950/51

- 14 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 14 jogos (ex.: Pro Patria x Sampdoria: base 1951-01-04, ogol 1950-12-24); fica a da base

### 1951/52

- 30 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 30 jogos (ex.: Novara Calcio x Legnano: base 1952-01-09, ogol 1951-12-23); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['ACF Fiorentina', 'Lazio Roma']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 3 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Lucchese 3-3 Triestina (1952-06-29); Triestina 1-0 Lucchese (1952-07-06); Triestina 1-0 Brescia (1952-07-13)

### 1952/53

- a base traz Novara 3-2 Pro Patria duas vezes; o ogol mostra que o jogo de 03/05/1953 foi Pro Patria 2-3 Novara (o returno)
- a base não fecha nesta temporada (306 jogos): montada pelo calendário do ogol (306 jogos), com 305 jogos da base
- 1 jogos só no ogol, que entram com o placar do ogol: Pro Patria 2-3 Novara Calcio (1953-05-03)
- 1 jogos da base fora do calendário do ogol, descartados: Novara Calcio 3-2 Pro Patria (1953-05-03)
- placar corrigido: Torino FC x US Palermo de 3-0 para 3-1 — gol de Cecconi (Palermo) aos 4 minutos na ficha da Wikipédia it (AC Torino 1952-1953); a matriz e a tabela da Wikipédia it e en e o transfermarkt dão 3-1
- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — Torino FC x US Palermo (1952-11-30): base 3-1, ogol 3-0
- data diferente no ogol em 1 jogos (ex.: Torino FC x AC Milan: base 1953-01-06, ogol 1953-01-04); fica a da base

### 1953/54

- o triangular de rebaixamento (Udinese, SPAL e Palermo; caiu o Palermo) entra na fase "Desempate" com os placares, datas e autores dos gols da RSSSF (tablesi/ital54.html); a Wikipédia it só traz a tabela
- 3 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 3 jogos (ex.: SSC Napoli x Legnano: base 1954-01-06, ogol 1953-12-20); fica a da base
- 3 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Udinese 2-0 SPAL (1954-06-06); Udinese 1-1 Palermo (1954-06-13); SPAL 2-1 Palermo (1954-06-20)

### 1954/55

- 3 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 3 jogos (ex.: Calcio Catania x Atalanta: base 1954-12-22, ogol 1954-12-12); fica a da base
- SPAL: rebaixado em campo e readmitido (ficou no lugar de Udinese e Catania, punidos)
- Pro Patria: rebaixado em campo e readmitido (ficou no lugar de Udinese e Catania, punidos)

### 1955/56

- 18 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 18 jogos (ex.: SSC Napoli x Juventus: base 1955-12-04, ogol 1955-11-20); fica a da base

### 1956/57

- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: Atalanta x Udinese Calcio: base 1957-01-02, ogol 1956-12-23); fica a da base

### 1957/58

- 13 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 13 jogos (ex.: Hellas Verona x Atalanta: base 1957-11-10, ogol 1957-12-01); fica a da base
- 2 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Verona 0-1 Bari (1958-07-20); Bari 2-0 Verona (1958-07-24)

### 1958/59

- placar corrigido: Calcio Padova x Lazio Roma de 3-0 para 3-1 — o ogol e a tabela da Wikipédia fecham com este placar
- data diferente no ogol em 1 jogos (ex.: Vicenza Calcio x Calcio Padova: base 1958-12-28, ogol 1959-01-14); fica a da base

### 1959/60

- Genoa: 18 pontos a menos (suborno), e mandado para a Serie B; a Wikipédia desconta, a classificação da RSSSF não
- pontos da última classificação da RSSSF x jogos — Genoa CFC RSSSF 18 jogos 0

### 1960/61

- 2 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 2 jogos (ex.: AC Milan x Lazio Roma: base 1961-01-25, ogol 1961-01-08); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 3 posições (ex.: ['Calcio Lecco 1912', 'Udinese Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 3 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Bari 2-4 Lecco (1961-06-11); Udinese 0-0 Bari (1961-06-14); Lecco 3-3 Udinese (1961-06-18)

### 1961/62

- data diferente no ogol em 9 jogos (ex.: Calcio Padova x ACF Fiorentina: base 1961-11-26, ogol 1961-11-19); fica a da base

### 1962/63

- placar corrigido: SSC Napoli x US Palermo de 3-0 para 3-1 — a matriz e a tabela da Wikipédia it e en, a página do US Palermo 1962-1963 e o transfermarkt dão 3-1 (autor do gol do Palermo não encontrado)
- 12 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — SSC Napoli x US Palermo (1962-12-16): base 3-1, ogol 3-0
- data diferente no ogol em 12 jogos (ex.: Juventus x SSC Napoli: base 1962-11-04, ogol 1962-11-08); fica a da base

### 1963/64

- os dois jogos de 07/06/1964 que só o ogol traz são desempates (spareggi): Bologna 2-0 Inter, pelo título, e Sampdoria 2-0 Modena, pelo rebaixamento. Entram na fase "Desempate", fora da tabela
- resultado do tribunal: AS Bari x Genoa CFC fica 0-2 (base 1-2) — 0-2 a tavolino (matriz da Wikipédia it; página do AS Bari 1963-1964)
- 11 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — AS Bari x Genoa CFC (1964-05-03): base 0-2, ogol 1-2
- jogo do ogol sem par na base: Bologna 2-0 Internazionale (1964-06-07, F)
- jogo do ogol sem par na base: Sampdoria 2-0 Modena (1964-06-07, )
- data diferente no ogol em 119 jogos (ex.: Inter x Torino FC: base 1963-11-13, ogol 1963-09-25); fica a da base
- 2 jogo(s)-desempate (spareggi) de rebaixamento e título entram na fase "Desempate", fora da tabela: Bologna 2-0 Inter (1964-06-07); Modena 0-2 Sampdoria (1964-06-07)

### 1964/65

- data diferente no ogol em 1 jogos (ex.: AC Mantova x ACF Fiorentina: base 1965-01-20, ogol 1965-01-10); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['ACF Fiorentina', 'Juventus']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1965/66

- mando corrigido: Juventus 2-0 Torino FC (1965-11-21); a base e o ogol trazem o mando trocado — a RSSSF traz Juventus 2-0 Torino na 10ª rodada; no returno, Torino 0-0 Juventus
- mando corrigido: Cagliari Calcio 1-3 Bologna FC (1966-01-23); a base e o ogol trazem o mando trocado — a RSSSF traz Cagliari 1-3 Bologna na 18ª rodada, jogado em Bolonha; no turno, Bologna 1-0 Cagliari

### 1966/67

- 3 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 3 jogos (ex.: ACF Fiorentina x Vicenza Calcio: base 1967-01-04, ogol 1966-11-06); fica a da base

### 1967/68

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: SSC Napoli x Sampdoria: base 1968-03-03, ogol 1968-04-03); fica a da base

### 1968/69

- sem ocorrências

### 1969/70

- 2 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 2 jogos (ex.: AC Milan x AS Roma: base 1969-10-16, ogol 1969-10-19); fica a da base

### 1970/71

- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — Torino FC x Juventus (1970-11-22): base 2-1, ogol 2-0
- data diferente no ogol em 1 jogos (ex.: Hellas Verona x Torino FC: base 1971-01-06, ogol 1970-12-20); fica a da base

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 4 posições (ex.: ['Sampdoria', 'US Foggia']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1974/75

- 112 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 111 jogos (ex.: SSC Napoli x Ascoli Calcio: base 1974-10-06, ogol 1974-09-30); fica a da base

### 1975/76

- sem ocorrências

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- data diferente no ogol em 16 jogos (ex.: Inter x Vicenza Calcio: base 1978-12-17, ogol 1978-10-17); fica a da base

### 1979/80

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: Cagliari Calcio x US Avellino: base 1979-11-11, ogol 1979-10-11); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 14 posições (ex.: ['Torino FC', 'Ascoli Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1980/81

- sem ocorrências

### 1981/82

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: Genoa CFC x AC Milan: base 1982-04-18, ogol 1982-04-11); fica a da base

### 1982/83

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 16 jogos (ex.: ACF Fiorentina x Udinese Calcio: base 1982-09-26, ogol 1982-09-25); fica a da base
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 11º Genoa, 12º Pisa; a Wikipédia en trazia outra ordem

### 1983/84

- 8 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: Inter x US Avellino: base 1984-04-15, ogol 1984-04-08); fica a da base

### 1984/85

- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: Juventus x Lazio Roma: base 1985-01-30, ogol 1985-01-13); fica a da base

### 1985/86

- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: Juventus x Sampdoria: base 1985-12-31, ogol 1985-12-08); fica a da base

### 1986/87

- data diferente no ogol em 8 jogos (ex.: AS Roma x ACF Fiorentina: base 1987-04-05, ogol 1987-04-25); fica a da base
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 9º Torino, 10º Como, 11º Fiorentina; a Wikipédia en trazia outra ordem
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['AC Milan', 'Sampdoria']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1987/88

- placar diferente no ogol — Juventus x AC Cesena (1987-11-22): base 0-2, ogol 2-1
- placar diferente no ogol — AC Milan x AS Roma (1987-12-13): base 0-2, ogol 1-0
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 10º Como, 11º Verona; a Wikipédia en trazia outra ordem

### 1988/89

- 9 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- placar diferente no ogol — US Lecce x Juventus (1989-04-09): base 2-0, ogol 0-2
- jogo do ogol sem par na base: Fiorentina 1-0 Roma (1989-06-30, )
- data diferente no ogol em 8 jogos (ex.: Como Calcio x Pescara Calcio: base 1989-01-22, ogol 1988-11-22); fica a da base
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 10º Cesena, 11º Lazio, 13º Bologna, 14º Verona, 15º Pescara, 16º Torino; a Wikipédia en trazia outra ordem
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 4 posições (ex.: ['ACF Fiorentina', 'AS Roma']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1989/90

- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 12º Cesena, 13º Fiorentina; a Wikipédia en trazia outra ordem

### 1990/91

- data diferente no ogol em 1 jogos (ex.: AC Milan x Pisa SC: base 1990-12-09, ogol 1990-01-23); fica a da base

### 1991/92

- 9 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 9 jogos (ex.: AS Roma x Genoa CFC: base 1991-09-22, ogol 1991-09-15); fica a da base
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 10º Atalanta, 11º Lazio; a Wikipédia en trazia outra ordem

### 1992/93

- data diferente no ogol em 2 jogos (ex.: SSC Napoli x Atalanta: base 1993-03-28, ogol 1993-03-24); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Udinese Calcio', 'Brescia Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 1 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Udinese 3-1 Brescia (1993-06-12)

### 1993/94

- a tabela da Wikipédia dá à Cremonese 8 vitórias e 16 empates; os jogos e a RSSSF dão 9 e 14 (os mesmos 32 pontos)
- 9 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 9 jogos (ex.: Udinese Calcio x AC Milan: base 1993-12-12, ogol 1994-01-06); fica a da base
- tabela publicada x jogos (Wikipédia) — US Cremonese tabela [34, 8, 16, 10, 41, 41, 32] jogos [34, 9, 14, 11, 41, 41, 32]
- ordem entre empatados pela Wikipédia it (classifica avulsa, confronto direto, a regra da época): 10º Genoa, 11º Cremonese; a Wikipédia en trazia outra ordem

### 1994/95

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Calcio Padova', 'Genoa CFC']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 1 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Padova 1-1 Genoa (1995-06-10)

### 1995/96

- data diferente no ogol em 1 jogos (ex.: Sampdoria x Lazio Roma: base 1996-04-20, ogol 1996-04-21); fica a da base
- a última classificação da página da RSSSF não é a final (11 clubes com outros pontos): não serve para conferir

### 1996/97

- data diferente no ogol em 1 jogos (ex.: AC Perugia x Udinese Calcio: base 1996-10-27, ogol 1996-10-26); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Piacenza Calcio', 'Cagliari Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 1 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Piacenza 3-1 Cagliari (1997-06-15)

### 1997/98

- sem ocorrências

### 1998/99

- jogo do ogol sem par na base: Internazionale 1-2 Bologna (1999-05-27, )
- jogo do ogol sem par na base: Udinese 0-0 Juventus (1999-05-28, )
- jogo do ogol sem par na base: Bologna 2-1 Internazionale (1999-05-30, )
- jogo do ogol sem par na base: Juventus 1-1 Udinese (1999-05-31, )
- data diferente no ogol em 1 jogos (ex.: AC Venezia x Empoli FC: base 1999-01-06, ogol 1999-01-20); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Udinese Calcio', 'Juventus']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1999/00

- jogo do ogol sem par na base: Parma 1-3 Internazionale (2000-05-23, POff)

### 2000/01

- placar diferente no ogol — Hellas Verona x Parma FC (2001-01-28): base 0-2, ogol 2-0
- placar diferente no ogol — ACF Fiorentina x Brescia Calcio (2001-02-25): base 2-2, ogol 4-0
- placar diferente no ogol — ACF Fiorentina x Atalanta (2001-05-27): base 1-1, ogol 2-0
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Reggina Calcio, Wikipédia Hellas Verona); fica a da Wikipédia
- 2 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Verona 1-0 Reggina (2001-06-21); Reggina 2-1 Verona (2001-06-24)

### 2001/02

- 1 datas corrigidas pelo Calendario da Wikipédia it (igual à RSSSF); a base e o ogol traziam outra (lista em data/coleta/ita-1/correcoes/datas.csv)
- data diferente no ogol em 4 jogos (ex.: Piacenza Calcio x AS Roma: base 2001-09-16, ogol 2001-09-14); fica a da base
- placar diferente na ESPN — Hellas Verona x AC Perugia (2001-09-16): base 1-1, ESPN 2-1
- ESPN com 304 de 306 jogos (ex. sem ESPN: Brescia Calcio x Chievo Verona, 2001-10-14)
- gols da ESPN não batem com o placar — Hellas Verona 1-1 AC Perugia: ESPN 2-1 (descartados)
- gols da ESPN não batem com o placar — Hellas Verona 1-0 Piacenza Calcio: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Parma FC 2-1 Bologna FC: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — Hellas Verona 1-2 ACF Fiorentina: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — Udinese Calcio 3-2 Brescia Calcio: ESPN 4-2 (descartados)

### 2002/03

- ESPN com 305 de 306 jogos (ex. sem ESPN: Como Calcio x Udinese Calcio, 2002-12-18)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Atalanta, Wikipédia Reggina Calcio); fica a da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Reggina Calcio', 'Atalanta']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- 2 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Reggina 0-0 Atalanta (2003-05-29); Atalanta 1-2 Reggina (2003-06-02)

### 2003/04

- ESPN com 305 de 306 jogos (ex. sem ESPN: Sampdoria x Reggina Calcio, 2004-01-24)
- 2 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Perugia 0-1 Fiorentina (2004-06-16); Fiorentina 1-1 Perugia (2004-06-20)

### 2004/05

- os dois jogos de junho de 2005 que só o ogol traz (Parma x Bologna) são o desempate (spareggio) de rebaixamento: entram na fase "Desempate", fora da tabela
- jogo do ogol sem par na base: Parma 0-1 Bologna (2005-06-14, POff)
- jogo do ogol sem par na base: Bologna 0-2 Parma (2005-06-18, POff)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Parma FC', 'Bologna FC']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- título não atribuído (lista de campeões da Wikipédia); Juventus terminou em 1º
- 2 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Parma 0-1 Bologna (2005-06-14); Bologna 0-2 Parma (2005-06-18)

### 2005/06

- Calciopoli: a ordem oficial (Wikipédia) põe a Juventus em último e desconta pontos de Fiorentina, Lazio e Milan; a Inter recebeu o título
- resultado do tribunal: A.C.R. Messina x Empoli FC fica 0-3 (base 1-2) — abandonado aos 89 minutos com 1-2; vitória de 3-0 dada ao Empoli (RSSSF; ogol e Wikipédia contam 0-3). O engsoccerdata, o football-data e a ESPN trazem o 1-2 de campo
- placar diferente no football-data — A.C.R. Messina x Empoli FC: base 0-3, football-data 1-2
- placar diferente na ESPN — A.C.R. Messina x Empoli FC (2006-05-07): base 0-3, ESPN 1-2
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 19 posições (ex.: ['Inter', 'AS Roma']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- Messina: rebaixado em campo e readmitido (Calciopoli)
- gols da ESPN não batem com o placar — A.C.R. Messina 0-3 Empoli FC: ESPN 1-2 (descartados)

### 2006/07

- data diferente no ogol em 1 jogos (ex.: Reggina Calcio x US Palermo: base 2007-01-20, ogol 2007-01-21); fica a da base

### 2007/08

- placar diferente na ESPN — AC Siena x Sampdoria (2007-08-26): base 1-2, ESPN 0-0
- gols da ESPN não batem com o placar — AC Siena 1-2 Sampdoria: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Parma FC 2-2 AC Siena: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — Atalanta 1-3 US Palermo: ESPN 1-4 (descartados)

### 2008/09

- gols da ESPN não batem com o placar — Inter 2-1 Calcio Catania: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — AC Milan 1-0 SSC Napoli: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Bologna FC 5-2 Torino FC: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — AC Milan 1-1 Juventus: ESPN 1-2 (descartados)

### 2009/10

- data diferente no ogol em 1 jogos (ex.: AS Roma x Chievo Verona: base 2010-01-09, ogol 2010-01-10); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Cagliari Calcio, Wikipédia Chievo Verona); fica a da Wikipédia
- gols da ESPN não batem com o placar — AS Livorno 2-1 Parma FC: ESPN 2-2 (descartados)

### 2010/11

- gols da ESPN não batem com o placar — Juventus 2-1 Lazio Roma: ESPN 3-1 (descartados)

### 2011/12

- gols da ESPN não batem com o placar — AC Milan 4-0 Calcio Catania: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — US Lecce 2-2 Chievo Verona: ESPN 3-2 (descartados)

### 2012/13

- sem ocorrências

### 2013/14

- gols da ESPN não batem com o placar — Cagliari Calcio 2-2 Sampdoria: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — SSC Napoli 3-3 Udinese Calcio: ESPN 3-4 (descartados)

### 2014/15

- gols da ESPN não batem com o placar — Cagliari Calcio 2-1 Sassuolo Calcio: ESPN 2-2 (descartados)

### 2015/16

- sem ocorrências

### 2016/17

- placar diferente na ESPN — Sassuolo Calcio x Pescara Calcio (2016-08-28): base 0-3, ESPN 2-1
- gols da ESPN não batem com o placar — Sassuolo Calcio 0-3 Pescara Calcio: ESPN 2-1 (descartados)

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- data diferente no ogol em 1 jogos (ex.: US Lecce x Cagliari Calcio: base 2019-11-25, ogol 2019-11-24); fica a da base

### 2020/21

- resultado do tribunal: Hellas Verona x AS Roma fica 3-0 (base 0-0) — 0-0 em campo; a Roma escalou um jogador irregular e perdeu por 3-0 (ogol: "DA"; as tabelas da RSSSF e da Wikipédia contam 3-0). O engsoccerdata traz 0-0
- placar diferente no football-data — Hellas Verona x AS Roma: base 3-0, football-data 0-0
- placar diferente na ESPN — Hellas Verona x AS Roma (2020-09-19): base 3-0, ESPN 0-0

### 2021/22

- sem ocorrências

### 2022/23

- jogo do ogol sem par na base: Spezia 1-3 Hellas Verona (2023-06-11, )
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Spezia Calcio, Wikipédia Hellas Verona); fica a da Wikipédia
- 1 jogo(s)-desempate (spareggi) de rebaixamento entram na fase "Desempate", fora da tabela: Spezia 1-3 Verona (2023-06-11)

### 2023/24

- sem ocorrências

### 2024/25

- sem ocorrências

### 2025/26

- sem ocorrências

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_ita.py` (serve para todas as divisões italianas): nome de exibição como o clube é conhecido no Brasil, cidade e país. As grafias de época do engsoccerdata viram um clube só (Genova 1893 e Genoa; AC Liguria e Sampierdarenese; Lanerossi Vicenza e Vicenza; US e AS Livorno; Parma AC e Parma FC; US Anconitana e Ancona).
- A Sampdoria (fusão de 1946) fica separada da Sampierdarenese e da Andrea Doria. "Inter" fica "Inter de Milão".
- "Palermo" já é um clube argentino no banco: o italiano fica "Palermo FC".
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 69 códigos do ogol e 50 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** não entraram. A RSSSF traz os autores rodada a rodada em muitas temporadas antigas (formato italiano, "MARCATORI"); dá para ler num próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Spareggi de vaga europeia** (1986/87, 1987/88, 1988/89, 1998/99, 1999/2000): ficam de fora; os de título e de rebaixamento entram na fase "Desempate", fora da tabela (o triangular de 1953/54 pela RSSSF).
- **Campeonatos de 1897/98 a 1928/29** (grupos regionais e finais): ficam para depois; o ogol tem os calendários.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
