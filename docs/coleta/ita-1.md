# Campeonato Italiano (1ª divisão) — coleta de dados

Gerado por `python coleta/ita-1/importar.py`. Pacote em `data/coleta/ita-1/pacote/`.

**Edições:** 95, de 1929/30 a 2025/26 (Serie A; 1945/46 foi a Divisione Nazionale). Sem 1943/44 e 1944/45 (Segunda Guerra).

**Total:** 29244 jogos, 74998 gols, 24564 gols com autor (ESPN), 43962 cartões, 69 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1929/30-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ita-1/` para os escudos;
- ESPN (liga `ita.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (Maurizio Mariani e outros): tabela final, nas temporadas em que a página traz uma tabela legível;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e Capocannoniere.

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Roma). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94, 3 a partir de 1994/95. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 51, saldo de gols em 33, média de gols em 11); é ele que ordena a classificação rodada a rodada. Até 2004/05, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio), que não está no pacote.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1929/30 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 970 | 0 | 1 / 1 | Inter de Milão | — |
| 1930/31 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 951 | 0 | 0 / 2 | Juventus | — |
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
| 1952/53 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 829 | 0 | 1 / 1 | Inter de Milão | — |
| 1953/54 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 825 | 0 | 2 / 0 | Inter de Milão | — |
| 1954/55 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 832 | 0 | 2 / 0 | Milan | — |
| 1955/56 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 838 | 0 | 2 / 0 | Fiorentina | — |
| 1956/57 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 845 | 0 | 2 / 0 | Milan | — |
| 1957/58 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 880 | 0 | 1 / 0 | Juventus | — |
| 1958/59 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 897 | 0 | 2 / 0 | Milan | — |
| 1959/60 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 792 | 0 | 1 / 1 | Juventus | Genoa -18 pontos |
| 1960/61 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 814 | 0 | 2 / 0 | Juventus | — |
| 1961/62 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 770 | 0 | 1 / 0 | Milan | — |
| 1962/63 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 740 | 0 | 1 / 1 | Inter de Milão | — |
| 1963/64 | engsoccerdata + ogol + Wikipédia | 18 | 306 (306) | 648 | 0 | 1 / 1 | Bologna | — |
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

### 1929/30

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- tabela publicada x jogos (Wikipédia) — Genoa CFC tabela [34, 20, 8, 6, 63, 36, 48] jogos [34, 20, 8, 6, 63, 39, 48]
- tabela publicada x jogos (Wikipédia) — AC Milan tabela [34, 11, 10, 13, 52, 48, 32] jogos [34, 11, 10, 13, 53, 48, 32]
- tabela publicada x jogos (Wikipédia) — Unione Triestina tabela [34, 11, 6, 17, 42, 78, 28] jogos [34, 11, 6, 17, 42, 59, 28]
- tabela publicada x jogos (Wikipédia) — US Cremonese tabela [34, 4, 8, 22, 31, 83, 16] jogos [34, 4, 8, 22, 31, 84, 16]

### 1930/31

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos, menos o Brescia: a RSSSF dá 32 pontos, mas a base, o ogol e a Wikipédia dão 13 vitórias e 8 empates (34 pontos)
- data diferente no ogol em 1 jogos (ex.: Lazio Roma x Juventus: base 1930-10-21, ogol 1930-12-21); fica a da base
- pontos da última classificação da RSSSF x jogos — Brescia Calcio RSSSF 32 jogos 34
- tabela publicada x jogos (Wikipédia) — Lazio Roma tabela [34, 15, 5, 14, 45, 44, 35] jogos [34, 15, 5, 14, 44, 44, 35]
- tabela publicada x jogos (Wikipédia) — Legnano tabela [34, 6, 7, 21, 30, 71, 19] jogos [34, 6, 7, 21, 30, 70, 19]

### 1931/32

- sem ocorrências

### 1932/33

- sem ocorrências

### 1933/34

- placar corrigido: AC Milan x Casale de 6-1 para 6-2 — o ogol e a tabela da Wikipédia fecham com este placar
- placar corrigido: AS Livorno x US Palermo de 3-1 para 3-2 — o ogol e a tabela da Wikipédia fecham com este placar
- placar corrigido: Torino FC x AS Roma de 3-1 para 3-6 — o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 40, Torino 29)
- placar corrigido: Juventus x Bologna FC de 4-2 para 4-1 — o ogol e a tabela da Wikipédia fecham com este placar

### 1934/35

- placar corrigido: US Alessandria 1912 x AS Roma de 1-1 para 1-6 — o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 35, Alessandria 29)

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

- sem ocorrências

### 1945/46

- Andrea Doria x Sampierdarenese (21/10/1945): o ogol traz 0-1 e a base 0-0. Os grupos de 1945/46 não têm tabela publicada legível para desempatar: fica a base
- placar diferente no ogol — Andrea Doria x Sampierdarenese (1945-10-21): base 0-0, ogol 0-1

### 1946/47

- a base não fecha nesta temporada (370 jogos): montada pelo calendário do ogol (380 jogos), com 380 jogos da base

### 1947/48

- a base traz só 380 dos 420 jogos (21 clubes): os que faltam entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- a base não fecha nesta temporada (380 jogos): montada pelo calendário do ogol (420 jogos), com 379 jogos da base
- 41 jogos só no ogol, que entram com o placar do ogol: SSC Napoli 1-2 US Alessandria 1912 (1947-10-26); US Alessandria 1912 2-2 Lazio Roma (1948-06-27); Atalanta 1-0 ACF Fiorentina (1948-06-27); Bologna FC 0-0 AS Bari (1948-06-27); Genoa CFC 1-2 Torino FC (1948-06-27); Juventus 2-0 Salernitana Calcio 1919 (1948-06-27) ...
- 1 jogos da base fora do calendário do ogol, descartados: US Alessandria 1912 2-1 SSC Napoli (1947-10-26)

### 1948/49

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos (Bologna: a Wikipédia dá 11 vitórias e 18 empates; os jogos e a RSSSF, 12 e 17)
- tabela publicada x jogos (Wikipédia) — Bologna FC tabela [38, 11, 18, 9, 53, 46, 40] jogos [38, 12, 17, 9, 53, 46, 41]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Lucchese', 'Unione Triestina']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['ACF Fiorentina', 'Lazio Roma']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1952/53

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- a base traz Novara 3-2 Pro Patria duas vezes; o ogol mostra que o jogo de 03/05/1953 foi Pro Patria 2-3 Novara (o returno)
- a base não fecha nesta temporada (306 jogos): montada pelo calendário do ogol (306 jogos), com 305 jogos da base
- 1 jogos só no ogol, que entram com o placar do ogol: Pro Patria 2-3 Novara Calcio (1953-05-03)
- 1 jogos da base fora do calendário do ogol, descartados: Novara Calcio 3-2 Pro Patria (1953-05-03)
- tabela publicada x jogos (Wikipédia) — Torino FC tabela [34, 11, 9, 14, 47, 50, 31] jogos [34, 11, 9, 14, 47, 49, 31]
- tabela publicada x jogos (Wikipédia) — US Palermo tabela [34, 10, 10, 14, 43, 56, 30] jogos [34, 10, 10, 14, 42, 56, 30]

### 1953/54

- sem ocorrências

### 1954/55

- sem ocorrências

### 1955/56

- sem ocorrências

### 1956/57

- sem ocorrências

### 1957/58

- data diferente no ogol em 6 jogos (ex.: Genoa CFC x Sampdoria: base 1957-10-20, ogol 1957-11-01); fica a da base

### 1958/59

- placar corrigido: Calcio Padova x Lazio Roma de 3-0 para 3-1 — o ogol e a tabela da Wikipédia fecham com este placar
- data diferente no ogol em 1 jogos (ex.: Vicenza Calcio x Calcio Padova: base 1958-12-28, ogol 1959-01-14); fica a da base

### 1959/60

- Genoa: 18 pontos a menos (suborno), e mandado para a Serie B; a Wikipédia desconta, a classificação da RSSSF não
- pontos da última classificação da RSSSF x jogos — Genoa CFC RSSSF 18 jogos 0

### 1960/61

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 3 posições (ex.: ['Calcio Lecco 1912', 'Udinese Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1961/62

- data diferente no ogol em 9 jogos (ex.: Calcio Padova x ACF Fiorentina: base 1961-11-26, ogol 1961-11-19); fica a da base

### 1962/63

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- tabela publicada x jogos (Wikipédia) — SSC Napoli tabela [34, 9, 9, 16, 35, 59, 27] jogos [34, 9, 9, 16, 35, 58, 27]
- tabela publicada x jogos (Wikipédia) — US Palermo tabela [34, 5, 10, 19, 18, 54, 20] jogos [34, 5, 10, 19, 17, 54, 20]

### 1963/64

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- os dois jogos de 07/06/1964 que só o ogol traz são desempates (spareggi): Bologna 2-0 Inter, pelo título, e Sampdoria 2-0 Modena, pelo rebaixamento. Ficam de fora
- jogo do ogol sem par na base: Bologna 2-0 Internazionale (1964-06-07, F)
- jogo do ogol sem par na base: Sampdoria 2-0 Modena (1964-06-07, )
- data diferente no ogol em 117 jogos (ex.: AC Milan x Calcio Catania: base 1963-10-23, ogol 1963-10-27); fica a da base
- tabela publicada x jogos (Wikipédia) — Genoa CFC tabela [34, 10, 10, 14, 33, 34, 30] jogos [34, 10, 10, 14, 33, 35, 30]
- tabela publicada x jogos (Wikipédia) — AS Bari tabela [34, 6, 10, 18, 20, 43, 22] jogos [34, 6, 10, 18, 21, 43, 22]

### 1964/65

- data diferente no ogol em 1 jogos (ex.: AC Mantova x ACF Fiorentina: base 1965-01-20, ogol 1965-01-10); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['ACF Fiorentina', 'Juventus']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1965/66

- mando corrigido: Juventus 2-0 Torino FC (1965-11-21); a base e o ogol trazem o mando trocado — a RSSSF traz Juventus 2-0 Torino na 10ª rodada; no returno, Torino 0-0 Juventus
- mando corrigido: Cagliari Calcio 1-3 Bologna FC (1966-01-23); a base e o ogol trazem o mando trocado — a RSSSF traz Cagliari 1-3 Bologna na 18ª rodada, jogado em Bolonha; no turno, Bologna 1-0 Cagliari

### 1966/67

- sem ocorrências

### 1967/68

- sem ocorrências

### 1968/69

- sem ocorrências

### 1969/70

- sem ocorrências

### 1970/71

- placar diferente no ogol — Torino FC x Juventus (1970-11-22): base 2-1, ogol 2-0

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 4 posições (ex.: ['Sampdoria', 'US Foggia']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1974/75

- data diferente no ogol em 1 jogos (ex.: Lazio Roma x Cagliari Calcio: base 1974-11-10, ogol 1974-11-24); fica a da base

### 1975/76

- sem ocorrências

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- data diferente no ogol em 16 jogos (ex.: Inter x Vicenza Calcio: base 1978-12-17, ogol 1978-10-17); fica a da base

### 1979/80

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 14 posições (ex.: ['Torino FC', 'Ascoli Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1980/81

- sem ocorrências

### 1981/82

- sem ocorrências

### 1982/83

- data diferente no ogol em 8 jogos (ex.: ACF Fiorentina x Udinese Calcio: base 1982-09-26, ogol 1982-09-25); fica a da base

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- data diferente no ogol em 8 jogos (ex.: AS Roma x ACF Fiorentina: base 1987-04-05, ogol 1987-04-25); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['AC Milan', 'Sampdoria']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1987/88

- placar diferente no ogol — Juventus x AC Cesena (1987-11-22): base 0-2, ogol 2-1
- placar diferente no ogol — AC Milan x AS Roma (1987-12-13): base 0-2, ogol 1-0

### 1988/89

- placar diferente no ogol — US Lecce x Juventus (1989-04-09): base 2-0, ogol 0-2
- jogo do ogol sem par na base: Fiorentina 1-0 Roma (1989-06-30, )
- data diferente no ogol em 1 jogos (ex.: AS Roma x AC Milan: base 1988-11-22, ogol 1989-01-22); fica a da base

### 1989/90

- sem ocorrências

### 1990/91

- data diferente no ogol em 1 jogos (ex.: AC Milan x Pisa SC: base 1990-12-09, ogol 1990-01-23); fica a da base

### 1991/92

- sem ocorrências

### 1992/93

- data diferente no ogol em 2 jogos (ex.: SSC Napoli x Atalanta: base 1993-03-28, ogol 1993-03-24); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Udinese Calcio', 'Brescia Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1993/94

- a tabela da Wikipédia dá à Cremonese 8 vitórias e 16 empates; os jogos e a RSSSF dão 9 e 14 (os mesmos 32 pontos)
- data diferente no ogol em 2 jogos (ex.: Udinese Calcio x AC Milan: base 1993-12-12, ogol 1994-01-06); fica a da base
- tabela publicada x jogos (Wikipédia) — US Cremonese tabela [34, 8, 16, 10, 41, 41, 32] jogos [34, 9, 14, 11, 41, 41, 32]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['US Cremonese', 'Genoa CFC']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1994/95

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Calcio Padova', 'Genoa CFC']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

### 1995/96

- data diferente no ogol em 1 jogos (ex.: Sampdoria x Lazio Roma: base 1996-04-20, ogol 1996-04-21); fica a da base
- a última classificação da página da RSSSF não é a final (11 clubes com outros pontos): não serve para conferir

### 1996/97

- data diferente no ogol em 1 jogos (ex.: AC Perugia x Udinese Calcio: base 1996-10-27, ogol 1996-10-26); fica a da base
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Piacenza Calcio', 'Cagliari Calcio']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida

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

### 2001/02

- data diferente no ogol em 3 jogos (ex.: Piacenza Calcio x AS Roma: base 2001-09-16, ogol 2001-09-14); fica a da base
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

### 2003/04

- ESPN com 305 de 306 jogos (ex. sem ESPN: Sampdoria x Reggina Calcio, 2004-01-24)

### 2004/05

- os dois jogos de junho de 2005 que só o ogol traz (Parma x Bologna) são o desempate (spareggio) de rebaixamento: ficam de fora
- jogo do ogol sem par na base: Parma 0-1 Bologna (2005-06-14, POff)
- jogo do ogol sem par na base: Bologna 0-2 Parma (2005-06-18, POff)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Parma FC', 'Bologna FC']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
- título não atribuído (lista de campeões da Wikipédia); Juventus terminou em 1º

### 2005/06

- Calciopoli: a ordem oficial (Wikipédia) põe a Juventus em último e desconta pontos de Fiorentina, Lazio e Milan; a Inter recebeu o título
- resultado do tribunal: A.C.R. Messina x Empoli FC fica 0-3 (base 1-2) — abandonado aos 89 minutos com 1-2; vitória de 3-0 dada ao Empoli (RSSSF; ogol e Wikipédia contam 0-3). O engsoccerdata, o football-data e a ESPN trazem o 1-2 de campo
- placar diferente no football-data — A.C.R. Messina x Empoli FC: base 0-3, football-data 1-2
- placar diferente na ESPN — A.C.R. Messina x Empoli FC (2006-05-07): base 0-3, ESPN 1-2
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 19 posições (ex.: ['Inter', 'AS Roma']). Na Itália, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio) ou deixado como posição dividida
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
- **Spareggi (jogos-desempate de título e rebaixamento):** ficam de fora.
- **Campeonatos de 1897/98 a 1928/29** (grupos regionais e finais): ficam para depois; o ogol tem os calendários.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
