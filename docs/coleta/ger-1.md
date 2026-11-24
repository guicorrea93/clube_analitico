# Campeonato Alemão (Bundesliga) — coleta de dados

Gerado por `python coleta/ger-1/importar.py`. Pacote em `data/coleta/ger-1/pacote/`.

**Edições:** 124, de 1902/03 a 2025/26. Até 1962/63, o campeonato tinha ligas regionais e uma fase final entre os campeões regionais (e, de 1947/48 em diante, também os vices): entram a fase final (jogos da RSSSF, com data e cidade; estádio, público, árbitro e gols das partidas com ficha na Wikipédia, quase sempre a final), as tabelas dos grupos e o campeão oficial (lista da RSSSF). A classificação final é o campeão em 1º e depois a fase alcançada. Sem campeonato em 1914/15-1918/19 e 1944/45-1946/47; sem campeão em 1903/04 e 1921/22. Desde 1963/64, a Bundesliga completa.

**Total:** 20303 jogos, 63752 gols, 56842 gols com autor (ESPN), 30251 cartões, 194 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1963/64-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ger-1/` para os escudos;
- ESPN (liga `ger.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: tabela final de cada temporada e lista de artilheiros de cada temporada (com o clube); até 1962/63, os jogos da fase final (tablesd/duit1903.html ... duit1944.html e duithist4763.html) e a lista de campeões (duitchamp.html);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista de campeões (com os gols do artilheiro); até 1962/63, a ficha das partidas com "football box" (estádio, público, árbitro, gols com minuto).

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Berlim). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 0, saldo de gols em 57, média de gols em 6); é ele que ordena a classificação rodada a rodada.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1902/03 | RSSSF + Wikipédia | 6 | 4 (0) | 31 | 4 | 0 / 0 | VfB Leipzig | — |
| 1903/04 | RSSSF + Wikipédia | 8 | 6 (0) | 36 | 13 | 0 / 0 | — | — |
| 1904/05 | RSSSF + Wikipédia | 7 | 5 (0) | 23 | 9 | 0 / 0 | Union 92 Berlin | — |
| 1905/06 | RSSSF + Wikipédia | 8 | 7 (0) | 40 | 0 | 0 / 0 | VfB Leipzig | — |
| 1906/07 | RSSSF | 6 | 5 (0) | 26 | 0 | 0 / 0 | Freiburger FC | — |
| 1907/08 | RSSSF | 8 | 8 (0) | 34 | 0 | 0 / 0 | Viktoria Berlin | — |
| 1908/09 | RSSSF | 8 | 7 (0) | 54 | 0 | 0 / 0 | Phönix Karlsruhe | — |
| 1909/10 | RSSSF | 9 | 8 (0) | 28 | 0 | 0 / 0 | Karlsruher FV | — |
| 1910/11 | RSSSF | 8 | 6 (0) | 23 | 0 | 0 / 0 | Viktoria Berlin | — |
| 1911/12 | RSSSF | 8 | 7 (0) | 32 | 0 | 0 / 0 | Holstein Kiel | — |
| 1912/13 | RSSSF | 7 | 6 (0) | 26 | 0 | 0 / 0 | VfB Leipzig | — |
| 1913/14 | RSSSF + Wikipédia | 8 | 7 (0) | 30 | 0 | 0 / 0 | Greuther Fürth | — |
| 1914/15 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1915/16 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1916/17 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1917/18 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1918/19 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1919/20 | RSSSF + Wikipédia | 8 | 7 (0) | 26 | 2 | 0 / 0 | Nuremberg | — |
| 1920/21 | RSSSF + Wikipédia | 7 | 6 (0) | 23 | 5 | 0 / 0 | Nuremberg | — |
| 1921/22 | RSSSF + Wikipédia | 8 | 8 (0) | 25 | 6 | 0 / 0 | — | — |
| 1922/23 | RSSSF + Wikipédia | 6 | 7 (0) | 20 | 3 | 0 / 0 | Hamburgo | — |
| 1923/24 | RSSSF + Wikipédia | 7 | 6 (0) | 24 | 2 | 0 / 0 | Nuremberg | — |
| 1924/25 | RSSSF + Wikipédia | 16 | 15 (0) | 51 | 1 | 0 / 0 | Nuremberg | — |
| 1925/26 | RSSSF + Wikipédia | 16 | 15 (0) | 73 | 5 | 0 / 0 | Greuther Fürth | — |
| 1926/27 | RSSSF | 16 | 15 (0) | 75 | 0 | 0 / 0 | Nuremberg | — |
| 1927/28 | RSSSF | 16 | 15 (0) | 75 | 0 | 0 / 0 | Hamburgo | — |
| 1928/29 | RSSSF + Wikipédia | 16 | 16 (0) | 79 | 5 | 0 / 0 | Greuther Fürth | — |
| 1929/30 | RSSSF | 16 | 16 (0) | 102 | 0 | 0 / 0 | Hertha Berlin | — |
| 1930/31 | RSSSF | 16 | 15 (0) | 69 | 0 | 0 / 0 | Hertha Berlin | — |
| 1931/32 | RSSSF | 16 | 15 (0) | 72 | 0 | 0 / 0 | Bayern de Munique | — |
| 1932/33 | RSSSF | 16 | 15 (0) | 76 | 0 | 0 / 0 | Fortuna Düsseldorf | — |
| 1933/34 | RSSSF | 16 | 51 (0) | 219 | 0 | 4 / 0 | Schalke 04 | — |
| 1934/35 | RSSSF | 16 | 51 (0) | 237 | 0 | 4 / 0 | Schalke 04 | — |
| 1935/36 | RSSSF | 16 | 52 (0) | 211 | 0 | 4 / 0 | Nuremberg | — |
| 1936/37 | RSSSF | 16 | 52 (0) | 213 | 0 | 4 / 0 | Schalke 04 | — |
| 1937/38 | RSSSF | 16 | 54 (0) | 226 | 0 | 4 / 0 | Hannover 96 | — |
| 1938/39 | RSSSF | 18 | 55 (0) | 224 | 0 | 5 / 0 | Schalke 04 | — |
| 1939/40 | RSSSF + Wikipédia | 18 | 55 (0) | 253 | 1 | 5 / 0 | Schalke 04 | — |
| 1940/41 | RSSSF + Wikipédia | 20 | 56 (0) | 248 | 7 | 6 / 0 | Rapid Viena | — |
| 1941/42 | RSSSF + Wikipédia | 8 | 8 (0) | 38 | 6 | 0 / 0 | Schalke 04 | — |
| 1942/43 | RSSSF + Wikipédia | 29 | 31 (0) | 144 | 28 | 0 / 0 | Dresdner SC | — |
| 1943/44 | RSSSF + Wikipédia | 31 | 32 (0) | 185 | 13 | 0 / 0 | Dresdner SC | — |
| 1944/45 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1945/46 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1946/47 | RSSSF | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | — |
| 1947/48 | RSSSF | 14 | 14 (0) | 60 | 0 | 0 / 0 | Nuremberg | — |
| 1948/49 | RSSSF + Wikipédia | 10 | 14 (0) | 48 | 39 | 0 / 0 | VfR Mannheim | — |
| 1949/50 | RSSSF + Wikipédia | 16 | 17 (0) | 66 | 3 | 0 / 0 | Stuttgart | — |
| 1950/51 | RSSSF + Wikipédia | 8 | 25 (0) | 99 | 3 | 2 / 0 | Kaiserslautern | — |
| 1951/52 | RSSSF + Wikipédia | 8 | 25 (0) | 113 | 5 | 2 / 0 | Stuttgart | — |
| 1952/53 | RSSSF + Wikipédia | 8 | 25 (0) | 93 | 5 | 2 / 0 | Kaiserslautern | — |
| 1953/54 | RSSSF + Wikipédia | 6 | 7 (0) | 29 | 6 | 2 / 0 | Hannover 96 | — |
| 1954/55 | RSSSF + Wikipédia | 9 | 29 (0) | 107 | 7 | 2 / 0 | Rot-Weiss Essen | — |
| 1955/56 | RSSSF + Wikipédia | 9 | 29 (0) | 124 | 6 | 2 / 0 | Borussia Dortmund | — |
| 1956/57 | RSSSF | 9 | 14 (0) | 65 | 0 | 1 / 1 | Borussia Dortmund | — |
| 1957/58 | RSSSF | 9 | 15 (0) | 68 | 0 | 2 / 0 | Schalke 04 | — |
| 1958/59 | RSSSF | 9 | 26 (0) | 122 | 0 | 2 / 0 | Eintracht Frankfurt | — |
| 1959/60 | RSSSF | 9 | 26 (0) | 118 | 0 | 2 / 0 | Hamburgo | — |
| 1960/61 | RSSSF | 9 | 26 (0) | 111 | 0 | 2 / 0 | Nuremberg | — |
| 1961/62 | RSSSF | 9 | 14 (0) | 65 | 0 | 2 / 0 | Colônia | — |
| 1962/63 | RSSSF + Wikipédia | 9 | 26 (0) | 110 | 4 | 1 / 1 | Borussia Dortmund | — |
| 1963/64 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 857 | 827 | 2 / 0 | Colônia | — |
| 1964/65 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 796 | 775 | 2 / 0 | Werder Bremen | — |
| 1965/66 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 987 | 947 | 2 / 0 | 1860 Munique | — |
| 1966/67 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 895 | 877 | 2 / 0 | Eintracht Braunschweig | — |
| 1967/68 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 993 | 964 | 2 / 0 | Nuremberg | — |
| 1968/69 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 873 | 865 | 2 / 0 | Bayern de Munique | — |
| 1969/70 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 951 | 927 | 1 / 1 | Borussia Mönchengladbach | — |
| 1970/71 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 926 | 919 | 2 / 0 | Borussia Mönchengladbach | — |
| 1971/72 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1006 | 932 | 0 / 2 | Bayern de Munique | Arminia Bielefeld -19 pontos |
| 1972/73 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1045 | 985 | 2 / 0 | Bayern de Munique | — |
| 1973/74 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1085 | 1033 | 2 / 0 | Bayern de Munique | — |
| 1974/75 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1056 | 1024 | 2 / 0 | Borussia Mönchengladbach | — |
| 1975/76 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1009 | 936 | 2 / 0 | Borussia Mönchengladbach | — |
| 1976/77 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1084 | 1019 | 2 / 0 | Borussia Mönchengladbach | — |
| 1977/78 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1014 | 943 | 2 / 0 | Colônia | — |
| 1978/79 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 963 | 908 | 2 / 0 | Hamburgo | — |
| 1979/80 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1023 | 960 | 1 / 1 | Bayern de Munique | — |
| 1980/81 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1039 | 989 | 2 / 0 | Bayern de Munique | — |
| 1981/82 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1081 | 1026 | 2 / 0 | Hamburgo | — |
| 1982/83 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1036 | 979 | 2 / 0 | Hamburgo | — |
| 1983/84 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1097 | 1039 | 2 / 0 | Stuttgart | — |
| 1984/85 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1074 | 1028 | 2 / 0 | Bayern de Munique | — |
| 1985/86 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 992 | 931 | 2 / 0 | Bayern de Munique | — |
| 1986/87 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 990 | 950 | 2 / 0 | Bayern de Munique | — |
| 1987/88 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 962 | 955 | 2 / 0 | Werder Bremen | — |
| 1988/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 852 | 794 | 2 / 0 | Bayern de Munique | — |
| 1989/90 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 790 | 770 | 2 / 0 | Bayern de Munique | — |
| 1990/91 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 886 | 860 | 2 / 0 | Kaiserslautern | — |
| 1991/92 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 994 | 983 | 2 / 0 | Stuttgart | — |
| 1992/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 893 | 880 | 2 / 0 | Werder Bremen | — |
| 1993/94 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 895 | 862 | 1 / 1 | Bayern de Munique | Dynamo Dresden -4 pontos |
| 1994/95 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 918 | 873 | 2 / 0 | Borussia Dortmund | — |
| 1995/96 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 831 | 801 | 2 / 0 | Borussia Dortmund | — |
| 1996/97 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 911 | 893 | 2 / 0 | Bayern de Munique | — |
| 1997/98 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 883 | 860 | 2 / 0 | Kaiserslautern | — |
| 1998/99 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 866 | 837 | 2 / 0 | Bayern de Munique | — |
| 1999/00 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 885 | 494 | 2 / 0 | Bayern de Munique | Eintracht Frankfurt -2 pontos |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 897 | 440 | 2 / 0 | Bayern de Munique | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 893 | 884 | 2 / 0 | Borussia Dortmund | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 821 | 821 | 2 / 0 | Bayern de Munique | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 909 | 909 | 2 / 0 | Werder Bremen | Kaiserslautern -3 pontos |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 890 | 890 | 2 / 0 | Bayern de Munique | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 861 | 854 | 2 / 0 | Bayern de Munique | — |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 837 | 837 | 2 / 0 | Stuttgart | — |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 860 | 859 | 2 / 0 | Bayern de Munique | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 894 | 894 | 2 / 0 | Wolfsburg | — |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 866 | 866 | 2 / 0 | Bayern de Munique | — |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 894 | 882 | 2 / 0 | Borussia Dortmund | — |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 875 | 845 | 2 / 0 | Borussia Dortmund | — |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 898 | 889 | 2 / 0 | Bayern de Munique | — |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 967 | 967 | 2 / 0 | Bayern de Munique | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 843 | 843 | 2 / 0 | Bayern de Munique | — |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 866 | 866 | 2 / 0 | Bayern de Munique | — |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 877 | 877 | 2 / 0 | Bayern de Munique | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 855 | 855 | 2 / 0 | Bayern de Munique | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 973 | 973 | 2 / 0 | Bayern de Munique | — |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 982 | 973 | 2 / 0 | Bayern de Munique | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 928 | 928 | 2 / 0 | Bayern de Munique | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 954 | 954 | 2 / 0 | Bayern de Munique | — |
| 2022/23 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 971 | 971 | 2 / 0 | Bayern de Munique | — |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 985 | 985 | 2 / 0 | Bayer Leverkusen | — |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 959 | 957 | 2 / 0 | Bayern de Munique | — |
| 2025/26 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 990 | 990 | 2 / 0 | Bayern de Munique | — |

## Conferência e ocorrências, temporada a temporada

### 1902/03

- sem ocorrências

### 1903/04

- partida da Wikipédia sem par na RSSSF: Germania Hamburg 11-0 Hannover 96 (None)
- partida da Wikipédia sem par na RSSSF: Germania Hamburg 1-3 Britannia Berlin (None)
- final não jogada: a federação anulou a fase final depois do protesto do Karlsruher FV; sem campeão

### 1904/05

- partida da Wikipédia sem par na RSSSF: Schlesien Breslau 5-1 Alemannia Cottbus (None)
- partida da Wikipédia sem par na RSSSF: Eintracht Braunschweig 3-2 Hannover 96 (None)
- partida da Wikipédia sem par na RSSSF: Eintracht Braunschweig 2-1 SV Victoria 96 Magdeburg (None)

### 1905/06

- Schlesien Breslau x Hertha (quartas de final): 1-7 na RSSSF, 0-7 na Wikipédia; fica a RSSSF
- placar diferente na Wikipédia — Schlesien Breslau x Hertha Berlin: RSSSF 1-7, Wikipédia Schlesien Breslau 0-7 Berliner FC Hertha 92
- partida da Wikipédia sem par na RSSSF: 1. FC Pforzheim 4-2 SC Koln 99 (None)

### 1906/07

- sem ocorrências

### 1907/08

- sem ocorrências

### 1908/09

- sem ocorrências

### 1909/10

- sem ocorrências

### 1910/11

- sem ocorrências

### 1911/12

- sem ocorrências

### 1912/13

- sem ocorrências

### 1913/14

- gols da Wikipédia não batem com o placar — Greuther Fürth 3-2 VfB Leipzig: 2 e 2

### 1914/15

- sem campeonato (Primeira Guerra Mundial)

### 1915/16

- sem campeonato (Primeira Guerra Mundial)

### 1916/17

- sem campeonato (Primeira Guerra Mundial)

### 1917/18

- sem campeonato (Primeira Guerra Mundial)

### 1918/19

- sem campeonato (Primeira Guerra Mundial)

### 1919/20

- sem ocorrências

### 1920/21

- sem ocorrências

### 1921/22

- título não atribuído: a final entre Hamburger SV e Nürnberg teve dois jogos sem vencedor (2-2 e o segundo interrompido em 1-1); a federação deu o título ao Hamburgo, que renunciou a ele

### 1922/23

- sem ocorrências

### 1923/24

- sem ocorrências

### 1924/25

- sem ocorrências

### 1925/26

- sem ocorrências

### 1926/27

- sem ocorrências

### 1927/28

- sem ocorrências

### 1928/29

- sem ocorrências

### 1929/30

- sem ocorrências

### 1930/31

- sem ocorrências

### 1931/32

- sem ocorrências

### 1932/33

- sem ocorrências

### 1933/34

- sem ocorrências

### 1934/35

- sem ocorrências

### 1935/36

- sem ocorrências

### 1936/37

- sem ocorrências

### 1937/38

- sem ocorrências

### 1938/39

- sem ocorrências

### 1939/40

- sem ocorrências

### 1940/41

- data diferente — Rapid Viena x Schalke 04: RSSSF 1941-07-22, Wikipédia 1941-06-22; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)

### 1941/42

- data diferente — Schalke 04 x First Vienna: RSSSF 1942-07-04, Wikipédia 1942-07-05; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)

### 1942/43

- sem ocorrências

### 1943/44

- sem ocorrências

### 1944/45

- sem campeonato (Segunda Guerra Mundial)

### 1945/46

- sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)

### 1946/47

- sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)

### 1947/48

- a Wikipédia (en) traz Kaiserslautern 1-0 1860 Munique e Union Oberschöneweide 0-4 St. Pauli nas quartas e Kaiserslautern 2-0 Neuendorf na semifinal; a RSSSF traz 5-1, 0-7 e 5-1. Fica a RSSSF, fonte principal, confirmada pela Wikipédia em alemão (artigo da fase final de 1948: 5:1, 0:7 e 5:1)
- placar diferente na Wikipédia — Kaiserslautern x 1860 Munique: RSSSF 5-1, Wikipédia 1. FC Kaiserslautern 1-0 TSV 1860 Munich
- placar diferente na Wikipédia — Union Berlin x St. Pauli: RSSSF 0-7, Wikipédia SG Oberschöneweide 0-4 FC St. Pauli
- placar diferente na Wikipédia — Kaiserslautern x TuS Koblenz: RSSSF 5-1, Wikipédia 1. FC Kaiserslautern 2-0 TuS Neuendorf

### 1948/49

- data diferente — Berliner SV 92 x Borussia Dortmund: RSSSF 1949-06-06, Wikipédia 1949-06-12; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — Kaiserslautern x St. Pauli: RSSSF 1949-06-06, Wikipédia 1949-06-12; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — Kickers Offenbach x Wormatia Worms: RSSSF 1949-06-06, Wikipédia 1949-06-12; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — VfR Mannheim x Hamburgo: RSSSF 1949-06-06, Wikipédia 1949-06-12; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — Kaiserslautern x St. Pauli: RSSSF 1949-06-16, Wikipédia 1949-06-19; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — Kickers Offenbach x Wormatia Worms: RSSSF 1949-06-16, Wikipédia 1949-06-19; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)
- data diferente — Kaiserslautern x Kickers Offenbach: RSSSF 1949-07-03, Wikipédia 1949-07-09; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)

### 1949/50

- sem ocorrências

### 1950/51

- data diferente — Kaiserslautern x Preußen Münster: RSSSF 1951-07-01, Wikipédia 1951-06-30; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)

### 1951/52

- sem ocorrências

### 1952/53

- sem ocorrências

### 1953/54

- sem ocorrências

### 1954/55

- sem ocorrências

### 1955/56

- sem ocorrências

### 1956/57

- tabela do Grupo 2 na RSSSF: Kickers Offenbach com 2 vitórias, 1 empate e 0 derrota e 4 pontos (a conta não fecha); os jogos dão 2 vitórias e 1 derrota (3-1 Hertha, 4-1 Kaiserslautern, 1-2 Dortmund) e os mesmos 4 pontos: erro de digitação da RSSSF
- tabela do Grupo 2 (RSSSF) x jogos — Kickers Offenbach tabela [3, 2, 1, 0, 8, 4, 4] jogos [3, 2, 0, 1, 8, 4, 4]

### 1957/58

- sem ocorrências

### 1958/59

- sem ocorrências

### 1959/60

- sem ocorrências

### 1960/61

- sem ocorrências

### 1961/62

- sem ocorrências

### 1962/63

- tabela do Grupo 2 na RSSSF: Borussia Neunkirchen com 6 gols pró; os jogos dão 8 (3-0 e 1-1 com o Hamburgo, 0-0 e 2-5 com o Dortmund, 0-4 e 2-1 com o 1860), e só com 8 os gols pró do grupo fecham com os contra (40): erro de digitação da RSSSF
- tabela do Grupo 2 (RSSSF) x jogos — Borussia Neunkirchen tabela [6, 2, 2, 2, 6, 11, 6] jogos [6, 2, 2, 2, 8, 11, 6]

### 1963/64

- 2 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 2 jogos (ex.: VfB Stuttgart x Werder Bremen: base 1964-03-30, ogol 1964-01-25); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Eintracht Braunschweig, Wikipédia Werder Bremen); fica a da Wikipédia

### 1964/65

- Dortmund x Duisburg em 19/11/1964 (base e ogol); só o transfermarkt dá 14/11 (revisão DE-004). Fica a base: duas fontes contra uma
- 4 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 4 jogos (ex.: Borussia Dortmund x VfB Stuttgart: base 1964-09-05, ogol 1964-09-11); fica a da base

### 1965/66

- Lothar Emmerich (Dortmund) foi o artilheiro com 31 gols (RSSSF); a lista de campeões da Wikipédia traz 26, que são os gols do 2º colocado
- 8 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: Eintracht Frankfurt x 1. FC Nurnberg: base 1965-08-28, ogol 1965-09-03); fica a da base
- artilheiro: a RSSSF dá Lothar Emmerich com 31 gols; a lista de campeões da Wikipédia dá 26 gols. Fica a RSSSF

### 1966/67

- 3 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- placar diferente no ogol — Hannover 96 x Bor. Monchengladbach (1966-10-01): base 1-1, ogol 2-0
- placar diferente no ogol — FC Schalke 04 x VfB Stuttgart (1967-03-11): base 2-0, ogol 1-1
- placar diferente no ogol — Hannover 96 x FC Schalke 04 (1967-05-27): base 1-2, ogol 2-1
- 16 jogos sem rodada no ogol ficam com a rodada dos outros jogos do mesmo dia
- data diferente no ogol em 3 jogos (ex.: Borussia Dortmund x VfB Stuttgart: base 1966-10-29, ogol 1966-11-29); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Rot-Weiss Essen, Wikipédia Fortuna Dusseldorf); fica a da Wikipédia

### 1967/68

- sem ocorrências

### 1968/69

- 8 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 8 jogos (ex.: MSV Duisburg x Eintracht Frankfurt: base 1968-08-30, ogol 1968-08-31); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 7 posições (ex.: RSSSF Eintracht Braunschweig, Wikipédia Bor. Monchengladbach); fica a da Wikipédia

### 1969/70

- Colônia x Werder em 18/03/1970 (base e ogol); só o transfermarkt dá 17/03 (revisão DE-004). Fica a base
- a tabela da RSSSF dá ao Bayern uma vitória a mais e ao Rot-Weiß Oberhausen um empate a menos (com 2 gols a menos para o Oberhausen e 2 gols sofridos a menos para o Bayern); a base, o ogol e a tabela da Wikipédia concordam com os jogos: erro da RSSSF
- 10 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 10 jogos (ex.: Rot-Weiss Oberhausen x Hertha BSC: base 1969-10-18, ogol 1969-10-15); fica a da base
- tabela publicada x jogos (RSSSF) — Bayern Munchen tabela [34, 22, 4, 8, 88, 35, 48] jogos [34, 21, 5, 8, 88, 37, 47]
- tabela publicada x jogos (RSSSF) — Rot-Weiss Oberhausen tabela [34, 11, 6, 17, 48, 62, 28] jogos [34, 11, 7, 16, 50, 62, 29]
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF VfB Stuttgart, Wikipédia Hamburger SV); fica a da Wikipédia

### 1970/71

- resultado do tribunal: Bor. Monchengladbach x Werder Bremen fica 0-2 (em campo, 1-1) — interrompido aos 88 minutos com a trave quebrada; a DFB deu o 2-0 ao Werder
- 10 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 10 jogos (ex.: Rot-Weiss Essen x 1. FC Kaiserslautern: base 1970-08-29, ogol 1970-08-28); fica a da base

### 1971/72

- 17 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 17 jogos (ex.: Borussia Dortmund x Hamburger SV: base 1971-08-20, ogol 1971-08-21); fica a da base
- punição: Arminia Bielefeld -19 pontos — perdeu todos os pontos (escândalo da Bundesliga de 1971) e foi rebaixado de ofício (Wikipédia de: Abzug 19; RSSSF: stripped of all points)
- tabela publicada x jogos (RSSSF) — Arminia Bielefeld tabela [34, 6, 7, 21, 41, 75, 19] jogos [34, 6, 7, 21, 41, 75, 0]
- tabela publicada x jogos (Wikipédia) — Arminia Bielefeld tabela [34, 6, 7, 21, 41, 75, 19] jogos [34, 6, 7, 21, 41, 75, 0]
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Eintracht Braunschweig, Wikipédia Werder Bremen); fica a da Wikipédia

### 1972/73

- 1 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 3 jogos (ex.: Werder Bremen x Bor. Monchengladbach: base 1972-12-06, ogol 1972-12-13); fica a da base

### 1973/74

- 9 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 9 jogos (ex.: Kickers Offenbach x Wuppertaler SV: base 1973-08-22, ogol 1973-08-21); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Fortuna Koln, Wikipédia Wuppertaler SV); fica a da Wikipédia

### 1974/75

- 11 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 11 jogos (ex.: VfB Stuttgart x Bayern Munchen: base 1974-09-12, ogol 1974-09-11); fica a da base

### 1975/76

- sem ocorrências

### 1976/77

- resultado do tribunal: 1. FC Kaiserslautern x Fortuna Dusseldorf fica 0-2 (em campo, 0-1) — interrompido aos 76 minutos (garrafa atirada da torcida); a DFB deu o 2-0 ao Düsseldorf

### 1977/78

- 5 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 6 jogos (ex.: Eintracht Frankfurt x 1. FC Kaiserslautern: base 1977-10-01, ogol 1977-09-01); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF Fortuna Dusseldorf, Wikipédia VfB Stuttgart); fica a da Wikipédia

### 1978/79

- Colônia x Braunschweig em 09/02/1979 (base e ogol); só o transfermarkt dá 10/02 (revisão DE-004). Fica a base
- 2 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 2 jogos (ex.: Eintracht Braunschweig x Hertha BSC: base 1978-12-12, ogol 1978-12-09); fica a da base

### 1979/80

- a tabela da Wikipédia troca as linhas de Stuttgart e Kaiserslautern (os dois com 41 pontos e 75-53 de gols); a da RSSSF fecha com os jogos e dá a ordem
- tabela publicada x jogos (Wikipédia) — VfB Stuttgart tabela [34, 18, 5, 11, 75, 53, 41] jogos [34, 17, 7, 10, 75, 53, 41]
- tabela publicada x jogos (Wikipédia) — 1. FC Kaiserslautern tabela [34, 17, 7, 10, 75, 53, 41] jogos [34, 18, 5, 11, 75, 53, 41]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- o critério do regulamento (saldo) não reproduz a ordem oficial em 2 posições (ex.: ['VfB Stuttgart', '1. FC Kaiserslautern']): desempate final pelo confronto direto

### 1980/81

- 3 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 3 jogos (ex.: Arminia Bielefeld x Eintracht Frankfurt: base 1981-02-03, ogol 1981-01-24); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF 1. FC Nurnberg, Wikipédia Fortuna Dusseldorf); fica a da Wikipédia

### 1981/82

- sem ocorrências

### 1982/83

- 4 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: FC Schalke 04 x Bayern Munchen: base 1982-12-05, ogol 1982-12-04); fica a da base

### 1983/84

- data diferente no ogol em 1 jogos (ex.: Eintracht Frankfurt x Bayer Leverkusen: base 1983-08-24, ogol 1984-08-24); fica a da base

### 1984/85

- 4 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF VfL Bochum, Wikipédia FC Schalke 04); fica a da Wikipédia

### 1985/86

- sem ocorrências

### 1986/87

- 1 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: FC 08 Homburg x Hamburger SV: base 1987-04-15, ogol 1987-04-14); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Werder Bremen, Wikipédia Borussia Dortmund); fica a da Wikipédia

### 1987/88

- ordem diferente entre RSSSF e Wikipédia em 8 posições (ex.: RSSSF 1. FC Koln, Wikipédia Bayern Munchen); fica a da Wikipédia

### 1988/89

- sem ocorrências

### 1989/90

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF FC St. Pauli, Wikipédia 1. FC Kaiserslautern); fica a da Wikipédia

### 1990/91

- 1 datas corrigidas: o transfermarkt e a RSSSF concordam contra a base (lista em data/coleta/ger-1/correcoes/datas.csv)
- data diferente no ogol em 1 jogos (ex.: Hertha BSC x Hamburger SV: base 1991-04-26, ogol 1991-04-20); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Hamburger SV, Wikipédia Eintracht Frankfurt); fica a da Wikipédia

### 1991/92

- a base para em 25/04/1992 (faltam as 4 últimas rodadas da temporada de 20 clubes, depois da reunificação): os 40 jogos entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- a base não fecha nesta temporada (340 jogos): montada pelo calendário do ogol (380 jogos), com 340 jogos da base
- 40 jogos só no ogol, que entram com o placar do ogol: Werder Bremen 1-1 Hamburger SV (1992-04-28); 1. FC Kaiserslautern 2-2 Werder Bremen (1992-05-01); 1. FC Nurnberg 1-0 Bayer Leverkusen (1992-05-01); Bayern Munchen 5-2 SG Wattenscheid 09 (1992-05-01); 1. FC Koln 3-1 Hansa Rostock (1992-05-02); Borussia Dortmund 2-2 Bor. Monchengladbach (1992-05-02) ...

### 1992/93

- resultado do tribunal: Bayer 05 Uerdingen x Eintracht Frankfurt fica 2-0 (em campo, 2-5) — o Frankfurt escalou 4 estrangeiros; a DFB deu o 2-0 ao Uerdingen
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF SG Wattenscheid 09, Wikipédia 1. FC Nurnberg); fica a da Wikipédia

### 1993/94

- Dynamo Dresden: 4 pontos a menos (licença); a Wikipédia desconta, a tabela da RSSSF não
- tabela publicada x jogos (RSSSF) — Dynamo Dresden tabela [34, 10, 14, 10, 33, 44, 34] jogos [34, 10, 14, 10, 33, 44, 30]
- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF Borussia Dortmund, Wikipédia Bayer Leverkusen); fica a da Wikipédia

### 1994/95

- resultado do tribunal: Eintracht Frankfurt x Bayern Munchen fica 2-0 (em campo, 2-5) — o Bayern escalou 4 amadores; a DFB deu o 2-0 ao Frankfurt

### 1995/96

- placar diferente no ogol — Bayer 05 Uerdingen x Eintracht Frankfurt (1995-08-19): base 1-1, ogol 0-2
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF FC St. Pauli, Wikipédia Bayer Leverkusen); fica a da Wikipédia

### 1996/97

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Hansa Rostock, Wikipédia Arminia Bielefeld); fica a da Wikipédia

### 1997/98

- sem ocorrências

### 1998/99

- ordem diferente entre RSSSF e Wikipédia em 6 posições (ex.: RSSSF FC Schalke 04, Wikipédia TSV 1860 Munchen); fica a da Wikipédia

### 1999/00

- sem ocorrências

### 2000/01

- sem ocorrências

### 2001/02

- ESPN com 305 de 306 jogos (ex. sem ESPN: Bayern Munchen x 1. FC Kaiserslautern, 2001-10-20)
- gols da ESPN não batem com o placar — VfB Stuttgart 2-0 FC St. Pauli: ESPN 3-0 (descartados)

### 2002/03

- sem ocorrências

### 2003/04

- sem ocorrências

### 2004/05

- sem ocorrências

### 2005/06

- gols da ESPN não batem com o placar — Bayer Leverkusen 1-1 VfB Stuttgart: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — 1. FC Kaiserslautern 2-2 Bayer Leverkusen: ESPN 4-4 (descartados)
- gols da ESPN não batem com o placar — Hertha BSC 1-0 Arminia Bielefeld: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Bayern Munchen 2-2 1. FC Koln: ESPN 4-4 (descartados)
- gols da ESPN não batem com o placar — Bayer Leverkusen 2-2 1. FC Nurnberg: ESPN 4-4 (descartados)

### 2006/07

- sem ocorrências

### 2007/08

- gols da ESPN não batem com o placar — Eintracht Frankfurt 1-0 Hertha BSC: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — VfB Stuttgart 4-1 Hansa Rostock: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — 1. FC Nurnberg 1-0 VfL Wolfsburg: ESPN 2-0 (descartados)

### 2008/09

- gols da ESPN não batem com o placar — FC Schalke 04 4-0 Energie Cottbus: ESPN 8-0 (descartados)

### 2009/10

- gols da ESPN não batem com o placar — Hamburger SV 4-1 Borussia Dortmund: ESPN 4-2 (descartados)

### 2010/11

- resultado do tribunal: FC St. Pauli x FC Schalke 04 fica 0-2 (em campo, 0-2) — interrompido aos 88 minutos (copo atirado no assistente); a DFB manteve o 0-2
- gols da ESPN não batem com o placar — 1899 Hoffenheim 2-2 Bayer Leverkusen: ESPN 3-2 (descartados)
- gols da ESPN não batem com o placar — Hamburger SV 2-4 Bayer Leverkusen: ESPN 2-5 (descartados)
- gols da ESPN não batem com o placar — Bayern Munchen 5-1 Bayer Leverkusen: ESPN 6-1 (descartados)

### 2011/12

- gols da ESPN não batem com o placar — FC Augsburg 1-4 Bayer Leverkusen: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — VfL Wolfsburg 2-2 1. FSV Mainz 05: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — 1. FC Nurnberg 2-0 Hertha BSC: ESPN 3-0 (descartados)
- gols da ESPN não batem com o placar — Bayer Leverkusen 3-2 1. FSV Mainz 05: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — 1. FC Koln 1-4 FC Schalke 04: ESPN 2-8 (descartados)
- gols da ESPN não batem com o placar — Bayer Leverkusen 4-1 FC Augsburg: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — Bayer Leverkusen 2-0 Bayern Munchen: ESPN 1-0 (descartados)
- gols da ESPN não batem com o placar — VfL Wolfsburg 3-2 Bayer Leverkusen: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — Bayer Leverkusen 3-3 Hertha BSC: ESPN 2-3 (descartados)

### 2012/13

- gols da ESPN não batem com o placar — Hannover 96 3-2 Bayer Leverkusen: ESPN 6-4 (descartados)
- gols da ESPN não batem com o placar — FC Augsburg 1-2 1. FC Nurnberg: ESPN 0-2 (descartados)

### 2013/14

- sem ocorrências

### 2014/15

- sem ocorrências

### 2015/16

- sem ocorrências

### 2016/17

- sem ocorrências

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- gols da ESPN não batem com o placar — FC Augsburg 1-3 1899 Hoffenheim: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — 1899 Hoffenheim 4-0 1. FC Union Berlin: ESPN 8-0 (descartados)
- gols da ESPN não batem com o placar — FC Schalke 04 1-4 VfL Wolfsburg: ESPN 2-8 (descartados)

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- sem ocorrências

### 2023/24

- sem ocorrências

### 2024/25

- gols da ESPN não batem com o placar — 1. FC Union Berlin 0-2 VfL Bochum: ESPN 1-1 (descartados)

### 2025/26

- VfL Wolfsburg rebaixado: 16º, perdeu o play-off para o SC Paderborn (0-0 em Wolfsburg, 1-2 em Paderborn; Wikipédia)

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_ger.py` (serve para todas as divisões alemãs): nome de exibição como o clube é conhecido no Brasil ("Bayern de Munique", "Colônia", "Hamburgo", "1860 Munique"), cidade e país. As grafias de época do engsoccerdata viram um clube só (Meidericher SV e Duisburg; Frankfurter SG Eintracht e Eintracht Frankfurt; SV Bayer 04 e Bayer Leverkusen).
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 58 códigos do ogol e 38 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Play-offs de rebaixamento (Relegation) contra clubes da 2. Bundesliga:** ficam de fora (entram com a 2ª divisão).
- **Ligas regionais de 1902/03 a 1962/63** (só a fase final entra) e a **DDR-Oberliga**: ficam para depois.
- **Era antiga, além da fase final:** artilheiros, e gols com autor fora das partidas com ficha na Wikipédia.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
