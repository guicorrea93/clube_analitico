# Campeonato Grego (1ª divisão) — coleta de dados

Gerado por `python coleta/gre-1/importar.py`. Pacote em `data/coleta/gre-1/pacote/`.

**Edições:** 90, de 1927/28 a 2025/26. Sem 1928/29, 1934/35, 1940/41-1944/45, 1949/50 e 1951/52.

**Total:** 18689 jogos, 46867 gols, 8900 gols com autor, 20025 cartões, 69 clubes.

**Fontes:**
- RSSSF: fase nacional de 1927/28 a 1958/59 (grkprehist.html); matriz de resultados de 1959/60 a 1992/93 (base dos jogos, sem data; grkhist.html e a página de cada temporada desde 1968/69); tabelas finais; lista de campeões e de artilheiros;
- Wikipédia (en): matriz de resultados (conferência), tabelas da fase regular e dos play-offs, fichas dos jogos-desempate (data, local, autores dos gols);
- ogol (zerozero): base dos jogos de 1993/94 em diante, com data e rodada; o clube pelo código do ogol; calendários em `data/cache/ogol-gre-1/` para os escudos;
- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do football-data;
- ESPN (liga `gre.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). Pontos: 3 por vitória, 2 por empate e 1 por derrota até 1972/73; 2-1-0 de 1973/74 a 1991/92; 3-1-0 desde 1992/93 (`pontos_vitoria` traz o da vitória; o sistema 3-2-1 vai na observação da edição). Jogos-desempate (título, 3º lugar) entram na fase "Desempate", fora da tabela. Play-off europeu de 2007/08 a 2016/17: fora da classificação. Desde 2019/20, a classificação final é a ordem dos grupos do play-off, com os números de todos os jogos e o ajuste (metade dos pontos no play-off europeu, punições) em `ajuste_pontos`. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (os cipriotas voltaram à liga deles).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 49, saldo em 9, vitórias em 1, média de gols em 8).

| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1927/28 | RSSSF + Wikipédia | 3 | 6 | 24 | 0 | 1 / 0 | Aris Salônica | — |
| 1929/30 | RSSSF + Wikipédia | 3 | 6 | 30 | 0 | 2 / 0 | Panathinaikos | — |
| 1930/31 | RSSSF + Wikipédia | 8 | 56 | 202 | 0 | 2 / 0 | Olympiacos | — |
| 1931/32 | RSSSF + Wikipédia | 8 | 56 | 180 | 0 | 2 / 0 | Aris Salônica | — |
| 1932/33 | RSSSF + Wikipédia | 3 | 5 | 19 | 0 | 0 / 1 | Olympiacos | — |
| 1933/34 | RSSSF + Wikipédia | 2 | 2 | 8 | 0 | 0 / 0 | Olympiacos | — |
| 1935/36 | RSSSF + Wikipédia | 8 | 56 | 196 | 0 | 1 / 1 | Olympiacos | — |
| 1936/37 | RSSSF + Wikipédia | 3 | 6 | 15 | 0 | 2 / 0 | Olympiacos | — |
| 1937/38 | RSSSF + Wikipédia | 3 | 6 | 27 | 0 | 2 / 0 | Olympiacos | — |
| 1938/39 | RSSSF + Wikipédia | 2 | 2 | 10 | 0 | 0 / 0 | AEK Atenas | — |
| 1939/40 | RSSSF + Wikipédia | 2 | 2 | 8 | 0 | 0 / 0 | AEK Atenas | — |
| 1945/46 | RSSSF + Wikipédia | 3 | 6 | 13 | 13 | 2 / 0 | Aris Salônica | — |
| 1946/47 | RSSSF + Wikipédia | 6 | 30 | 109 | 0 | 0 / 2 | Olympiacos | Iraklis -1 pontos; Makedonikos -2 pontos |
| 1947/48 | RSSSF + Wikipédia | 3 | 6 | 14 | 0 | 2 / 0 | Olympiacos | — |
| 1948/49 | RSSSF + Wikipédia | 3 | 6 | 24 | 0 | 2 / 0 | Panathinaikos | Panathinaikos -1 pontos; Aris Salônica -1 pontos |
| 1950/51 | RSSSF + Wikipédia | 3 | 6 | 19 | 0 | 2 / 0 | Olympiacos | Iraklis -1 pontos |
| 1952/53 | RSSSF + Wikipédia | 3 | 6 | 8 | 0 | 1 / 1 | Panathinaikos | — |
| 1953/54 | RSSSF + Wikipédia | 6 | 30 | 89 | 0 | 1 / 1 | Olympiacos | — |
| 1954/55 | RSSSF + Wikipédia | 6 | 30 | 113 | 0 | 0 / 2 | Olympiacos | — |
| 1955/56 | RSSSF + Wikipédia | 6 | 32 | 83 | 0 | 0 / 2 | Olympiacos | — |
| 1956/57 | RSSSF + Wikipédia | 10 | 92 | 290 | 1 | 2 / 0 | Olympiacos | Ethnikos Piraeus -4 pontos; Panargiakos -2 pontos |
| 1957/58 | RSSSF + Wikipédia | 12 | 132 | 373 | 0 | 1 / 1 | Olympiacos | Ethnikos Piraeus -2 pontos |
| 1958/59 | RSSSF + Wikipédia | 10 | 90 | 249 | 0 | 2 / 0 | Olympiacos | Apollon Kalamarias -1 pontos |
| 1959/60 | RSSSF + Wikipédia | 16 | 244 | 627 | 3 | 2 / 0 | Panathinaikos | — |
| 1960/61 | RSSSF + Wikipédia | 16 | 242 | 680 | 0 | 2 / 0 | Panathinaikos | AEK Atenas -1 pontos; Atromitos Piraeus -1 pontos |
| 1961/62 | RSSSF + Wikipédia | 16 | 245 | 709 | 0 | 2 / 0 | Panathinaikos | Panionios -1 pontos; Apollon Kalamarias -1 pontos |
| 1962/63 | RSSSF + Wikipédia | 16 | 248 | 625 | 6 | 2 / 0 | AEK Atenas | Egaleo -1 pontos |
| 1963/64 | RSSSF + Wikipédia | 16 | 241 | 569 | 0 | 2 / 0 | Panathinaikos | PAOK -1 pontos; Egaleo -1 pontos |
| 1964/65 | RSSSF + Wikipédia | 16 | 243 | 682 | 0 | 2 / 0 | Panathinaikos | — |
| 1965/66 | RSSSF + Wikipédia | 16 | 243 | 672 | 0 | 2 / 0 | Olympiacos | AEK Atenas -2 pontos; Panionios -1 pontos |
| 1966/67 | RSSSF + Wikipédia | 16 | 241 | 589 | 0 | 1 / 1 | Olympiacos | Pierikos -1 pontos |
| 1967/68 | RSSSF + Wikipédia | 18 | 306 | 788 | 0 | 2 / 0 | AEK Atenas | — |
| 1968/69 | RSSSF + Wikipédia | 18 | 306 | 808 | 0 | 2 / 0 | Panathinaikos | AEK Atenas -1 pontos |
| 1969/70 | RSSSF + Wikipédia | 18 | 306 | 697 | 0 | 1 / 0 | Panathinaikos | Panachaiki -13 pontos |
| 1970/71 | RSSSF + Wikipédia | 18 | 306 | 690 | 0 | 2 / 0 | AEK Atenas | EPA Larnaca -1 pontos |
| 1971/72 | RSSSF + Wikipédia | 18 | 306 | 720 | 0 | 2 / 0 | Panathinaikos | Olympiakos Nicosia -1 pontos |
| 1972/73 | RSSSF + Wikipédia | 18 | 306 | 705 | 0 | 2 / 0 | Olympiacos | Panathinaikos -3 pontos; Omonia Nicosia -1 pontos |
| 1973/74 | RSSSF + Wikipédia | 18 | 309 | 770 | 0 | 1 / 1 | Olympiacos | — |
| 1974/75 | RSSSF + Wikipédia | 18 | 306 | 766 | 0 | 2 / 0 | Olympiacos | — |
| 1975/76 | RSSSF + Wikipédia | 16 | 240 | 553 | 0 | 2 / 0 | PAOK | Atromitos -3 pontos |
| 1976/77 | RSSSF + Wikipédia | 18 | 306 | 806 | 0 | 1 / 1 | Panathinaikos | Atromitos -3 pontos |
| 1977/78 | RSSSF + Wikipédia | 18 | 306 | 733 | 0 | 1 / 1 | AEK Atenas | Veria -10 pontos |
| 1978/79 | RSSSF + Wikipédia | 18 | 306 | 788 | 0 | 1 / 1 | AEK Atenas | — |
| 1979/80 | RSSSF + Wikipédia | 18 | 308 | 711 | 3 | 2 / 0 | Olympiacos | Kastoria -1 pontos |
| 1980/81 | RSSSF + Wikipédia | 18 | 306 | 720 | 0 | 1 / 1 | Olympiacos | — |
| 1981/82 | RSSSF + Wikipédia | 18 | 307 | 712 | 3 | 1 / 1 | Olympiacos | — |
| 1982/83 | RSSSF + Wikipédia | 18 | 307 | 734 | 0 | 1 / 1 | Olympiacos | — |
| 1983/84 | RSSSF + Wikipédia | 16 | 241 | 531 | 0 | 1 / 1 | Panathinaikos | — |
| 1984/85 | RSSSF + Wikipédia | 16 | 240 | 663 | 0 | 2 / 0 | PAOK | — |
| 1985/86 | RSSSF + Wikipédia | 16 | 241 | 558 | 0 | 1 / 1 | Panathinaikos | Panachaiki -1 pontos |
| 1986/87 | RSSSF + Wikipédia | 16 | 240 | 510 | 0 | 2 / 0 | Olympiacos | PAOK -6 pontos; Iraklis -6 pontos; AEK Atenas -9 pontos; Larissa -6 pontos; Veria -6 pontos; Ethnikos Piraeus -6 pontos; Aris Salônica -6 pontos; Apollon Kalamarias -6 pontos; Diagoras -6 pontos; Doxa Drama -6 pontos; Apollon Smyrnis -6 pontos; PAS Giannina -6 pontos |
| 1987/88 | RSSSF + Wikipédia | 16 | 240 | 602 | 0 | 2 / 0 | Larissa | Panachaiki -1 pontos |
| 1988/89 | RSSSF + Wikipédia | 16 | 241 | 570 | 0 | 2 / 0 | AEK Atenas | — |
| 1989/90 | RSSSF + Wikipédia | 18 | 306 | 735 | 0 | 0 / 2 | Panathinaikos | Levadiakos -4 pontos |
| 1990/91 | RSSSF + Wikipédia | 18 | 306 | 772 | 0 | 2 / 0 | Panathinaikos | Olympiacos -2 pontos; PAOK -3 pontos |
| 1991/92 | RSSSF + Wikipédia | 18 | 306 | 755 | 0 | 2 / 0 | AEK Atenas | — |
| 1992/93 | RSSSF + Wikipédia | 18 | 306 | 821 | 0 | 2 / 0 | AEK Atenas | — |
| 1993/94 | ogol + RSSSF + Wikipédia | 18 | 306 | 874 | 0 | 2 / 0 | AEK Atenas | — |
| 1994/95 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 823 | 0 | 1 / 1 | Panathinaikos | — |
| 1995/96 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 870 | 0 | 2 / 0 | Panathinaikos | PAOK -3 pontos |
| 1996/97 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 787 | 0 | 2 / 0 | Olympiacos | Aris Salônica -3 pontos |
| 1997/98 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 843 | 0 | 2 / 0 | Olympiacos | — |
| 1998/99 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 833 | 0 | 1 / 1 | Olympiacos | — |
| 1999/00 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 885 | 0 | 1 / 1 | Olympiacos | — |
| 2000/01 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 16 | 240 | 717 | 0 | 1 / 1 | Olympiacos | — |
| 2001/02 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 14 | 182 | 524 | 0 | 2 / 0 | Olympiacos | — |
| 2002/03 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 16 | 240 | 617 | 0 | 2 / 0 | Olympiacos | PAS Giannina -90 pontos |
| 2003/04 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 16 | 240 | 627 | 0 | 2 / 0 | Panathinaikos | — |
| 2004/05 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 16 | 240 | 557 | 0 | 2 / 0 | Olympiacos | Aris Salônica -3 pontos |
| 2005/06 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 16 | 240 | 559 | 0 | 2 / 0 | Olympiacos | — |
| 2006/07 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 558 | 491 | 2 / 0 | Olympiacos | Ionikos -5 pontos |
| 2007/08 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 601 | 543 | 2 / 1 | Olympiacos | Apollon Kalamarias -1 pontos |
| 2008/09 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 547 | 503 | 3 / 0 | Olympiacos | — |
| 2009/10 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 587 | 545 | 3 / 0 | Panathinaikos | — |
| 2010/11 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 559 | 519 | 3 / 0 | Olympiacos | — |
| 2011/12 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 556 | 5 | 3 / 0 | Olympiacos | Panathinaikos -3 pontos; Aris Salônica -3 pontos |
| 2012/13 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 16 | 253 | 542 | 11 | 2 / 0 | Olympiacos | Panathinaikos -2 pontos; AEK Atenas -3 pontos |
| 2013/14 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 318 | 802 | 1 | 3 / 0 | Olympiacos | — |
| 2014/15 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 318 | 775 | 64 | 3 / 0 | Olympiacos | Panathinaikos -3 pontos; OFI Creta -29 pontos; Niki Volos -13 pontos |
| 2015/16 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 567 | 483 | 1 / 2 | Olympiacos | Panathinaikos -3 pontos; AEK Atenas -3 pontos; PAOK -3 pontos; Atromitos -3 pontos |
| 2016/17 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 252 | 577 | 544 | 3 / 0 | Olympiacos | PAOK -3 pontos |
| 2017/18 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 530 | 511 | 1 / 1 | AEK Atenas | PAOK -3 pontos; Olympiacos -3 pontos; Panathinaikos -8 pontos |
| 2018/19 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 549 | 546 | 2 / 0 | PAOK | PAOK -2 pontos; AEK Atenas -3 pontos; Panathinaikos -11 pontos |
| 2019/20 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 14 | 240 | 567 | 565 | 3 / 1 | Olympiacos | Xanthi -12 pontos; Panionios -6 pontos |
| 2020/21 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 14 | 240 | 529 | 529 | 3 / 0 | Olympiacos | — |
| 2021/22 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 14 | 240 | 570 | 570 | 4 / 0 | Olympiacos | — |
| 2022/23 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 14 | 240 | 564 | 564 | 4 / 0 | AEK Atenas | — |
| 2023/24 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 14 | 240 | 713 | 707 | 4 / 0 | PAOK | — |
| 2024/25 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 14 | 236 | 578 | 569 | 5 / 0 | Olympiacos | — |
| 2025/26 | ogol + football-data + ESPN + RSSSF + Wikipédia | 14 | 236 | 606 | 601 | 5 / 0 | AEK Atenas | — |

## Conferência e ocorrências, temporada a temporada

### 1927/28

- sem ocorrências

### 1929/30

- sem ocorrências

### 1930/31

- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: RSSSF 2-2; Wikipédia 4-2
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: RSSSF 2-4; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x PAOK: RSSSF 1-2; Wikipédia 1-3

### 1931/32

- Iraklis x PAOK: fica 2-5 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-3
- AEK Atenas x Olympiacos: fica 0-4 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 4-0
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: RSSSF 3-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x AEK Atenas: RSSSF 2-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: RSSSF 2-1; Wikipédia 0-3
- placar diferente na matriz da Wikipédia — AEK Atenas x Apollon Smyrnis: RSSSF 1-2; Wikipédia 0-2

### 1932/33

- a tabela da Wikipédia conta AEK 1-2 Aris (o placar na hora da suspensão); a RSSSF diz que o jogo não foi repetido nem contado, porque não mudava o campeão. Fica a RSSSF
- AEK x Aris foi suspenso por tumulto e não foi repetido, porque não mudava o campeão (RSSSF)
- Olympiacos x AEK Atenas: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-2
- tabela da Wikipédia x jogos — Aris Salônica tabela [3, 1, 0, 2, 4, 9] jogos [3, 0, 0, 3, 3, 10]
- tabela da Wikipédia x jogos — AEK Atenas tabela [3, 0, 0, 3, 2, 7] jogos [3, 1, 0, 2, 3, 6]
- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: RSSSF —; Wikipédia 1-2

### 1933/34

- sem ocorrências

### 1935/36

- a tabela da RSSSF não fecha nem com a matriz da própria RSSSF; com os placares da matriz da Wikipédia onde as duas discordam, os jogos fecham com a tabela da Wikipédia
- Panathinaikos x Aris Salônica: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-1
- Aris Salônica x Iraklis: fica 3-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- AEK Atenas x Apollon Smyrnis: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- PAOK x Aris Salônica: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- tabela da RSSSF x jogos — Panathinaikos tabela [14, 8, 2, 4, 35, 19] jogos [14, 9, 1, 4, 37, 19]
- tabela da RSSSF x jogos — Aris Salônica tabela [14, 4, 5, 5, 18, 22] jogos [14, 4, 5, 5, 21, 24]
- tabela da RSSSF x jogos — PAOK tabela [14, 4, 3, 7, 24, 32] jogos [14, 4, 3, 7, 23, 32]
- tabela da RSSSF x jogos — Iraklis tabela [14, 2, 2, 10, 15, 33] jogos [14, 1, 3, 10, 16, 36]
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: RSSSF 6-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Panathinaikos x Iraklis: RSSSF 4-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Ethnikos Piraeus: RSSSF 3-0; Wikipédia 4-1
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x PAOK: RSSSF 3-3; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: RSSSF 4-2; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Ethnikos Piraeus: RSSSF 1-0; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: RSSSF 2-2; Wikipédia 2-4
- placar diferente na matriz da Wikipédia — AEK Atenas x Iraklis: RSSSF 3-1; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Apollon Smyrnis: RSSSF 1-4; Wikipédia 0-3
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Aris Salônica: RSSSF 3-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Iraklis: RSSSF 6-0; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: RSSSF 0-1; Wikipédia 1-6
- placar diferente na matriz da Wikipédia — PAOK x Apollon Smyrnis: RSSSF 1-2; Wikipédia 3-3
- placar diferente na matriz da Wikipédia — Iraklis x Panathinaikos: RSSSF 2-1; Wikipédia 1-4
- placar diferente na matriz da Wikipédia — Iraklis x AEK Atenas: RSSSF 2-3; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Iraklis x Ethnikos Piraeus: RSSSF 0-0; Wikipédia 0-6

### 1936/37

- sem ocorrências

### 1937/38

- sem ocorrências

### 1938/39

- sem ocorrências

### 1939/40

- sem ocorrências

### 1945/46

- sem ocorrências

### 1946/47

- a tabela da RSSSF dá ao Makedonikos 0-0-8 em 10 jogos (erro de digitação: são 10 derrotas) e 8 pontos (10 menos os 2 de punição); a da Wikipédia dá AEK 0-1 Iraklis, e a RSSSF (matriz e tabela) 2-0. Fica a RSSSF
- punição tirada da tabela da RSSSF: Iraklis -1 pontos
- tabela da RSSSF x jogos — Makedonikos tabela [10, 0, 0, 8, 13, 36, 8] jogos [10, 0, 0, 10, 13, 36, 10]
- tabela da Wikipédia x jogos — AEK Atenas tabela [10, 3, 1, 6, 13, 16] jogos [10, 4, 1, 5, 15, 14]
- placar diferente na matriz da Wikipédia — AEK Atenas x Iraklis: RSSSF 2-0; Wikipédia 0-1
- punição pela nota da RSSSF: Makedonikos -2 pontos

### 1947/48

- sem ocorrências

### 1948/49

- punição tirada da tabela da RSSSF: Panathinaikos -1 pontos
- punição tirada da tabela da RSSSF: Aris Salônica -1 pontos

### 1950/51

- punição tirada da tabela da RSSSF: Iraklis -1 pontos

### 1952/53

- a tabela da RSSSF dá ao Aris 0-2-3 em 4 jogos (erro de digitação: são 0-1-3); a da Wikipédia fecha
- tabela da RSSSF x jogos — Aris Salônica tabela [4, 0, 2, 3, 1, 5, 5] jogos [4, 0, 1, 3, 1, 5, 5]

### 1953/54

- a tabela da RSSSF dá 1 gol a menos ao Panathinaikos e ao Panachaiki; a da Wikipédia fecha com os jogos (3-0 no Panathinaikos x Panachaiki, da matriz da Wikipédia; a da RSSSF dá 2-0)
- Panathinaikos x PAOK: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Panathinaikos x Panachaiki: fica 3-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- PAOK x Panathinaikos: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- PAOK x Niki Volos: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-1
- Niki Volos x PAOK: fica 2-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 4-2
- tabela da RSSSF x jogos — Panathinaikos tabela [10, 5, 5, 0, 12, 5] jogos [10, 5, 5, 0, 13, 5]
- tabela da RSSSF x jogos — Panachaiki tabela [10, 1, 1, 8, 5, 30] jogos [10, 1, 1, 8, 5, 31]

### 1954/55

- as tabelas da RSSSF e da Wikipédia concordam entre si e dão ao Apollon 2 gols pró a menos e ao Olympiacos Volos e ao Panetolikos 1 gol contra a menos; nenhuma das duas matrizes fecha com elas. Limite de fonte (seria preciso o jornal da época)
- Olympiacos Volos x Apollon Smyrnis: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-2
- tabela da RSSSF x jogos — Olympiacos tabela [10, 9, 0, 1, 28, 9] jogos [10, 9, 1, 0, 28, 9]
- tabela da RSSSF x jogos — Apollon Smyrnis tabela [10, 6, 0, 4, 18, 15] jogos [10, 6, 0, 4, 20, 15]
- tabela da RSSSF x jogos — Olympiacos Volos tabela [10, 1, 0, 9, 9, 29] jogos [10, 1, 0, 9, 9, 30]
- tabela da RSSSF x jogos — Panetolikos tabela [10, 1, 0, 9, 6, 35] jogos [10, 1, 0, 9, 6, 36]
- tabela da Wikipédia x jogos — Apollon Smyrnis tabela [10, 6, 0, 4, 18, 15] jogos [10, 6, 0, 4, 20, 15]
- tabela da Wikipédia x jogos — Olympiacos Volos tabela [10, 1, 0, 9, 9, 29] jogos [10, 1, 0, 9, 9, 30]
- tabela da Wikipédia x jogos — Panetolikos tabela [10, 1, 0, 9, 6, 35] jogos [10, 1, 0, 9, 6, 36]
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x PAOK: RSSSF 2-1; Wikipédia 0-3
- placar diferente na matriz da Wikipédia — PAOK x Apollon Smyrnis: RSSSF 3-0; Wikipédia 1-2

### 1955/56

- fase final: as tabelas da RSSSF e da Wikipédia concordam entre si (Olympiacos 13-9, Ethnikos 12-8, Panathinaikos 15-11) e não fecham com a matriz da RSSSF, a única da fase final (a Wikipédia não tem matriz dela). Limite de fonte
- tabela da RSSSF x jogos — Olympiacos tabela [10, 4, 5, 1, 13, 9, 23] jogos [10, 4, 5, 1, 14, 10, 23]
- tabela da RSSSF x jogos — Ethnikos Piraeus tabela [10, 4, 4, 2, 12, 8, 22] jogos [10, 4, 4, 2, 16, 12, 22]
- tabela da RSSSF x jogos — Panathinaikos tabela [10, 5, 2, 3, 15, 11, 22] jogos [10, 5, 2, 3, 12, 8, 22]
- tabela da Wikipédia x jogos — Olympiacos tabela [10, 4, 5, 1, 13, 9] jogos [10, 4, 5, 1, 14, 10]
- tabela da Wikipédia x jogos — Ethnikos Piraeus tabela [10, 4, 4, 2, 12, 8] jogos [10, 4, 4, 2, 16, 12]
- tabela da Wikipédia x jogos — Panathinaikos tabela [10, 5, 2, 3, 15, 11] jogos [10, 5, 2, 3, 12, 8]

### 1956/57

- PAOK x Panathinaikos: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-2
- Panionios x Proodeftiki: fica 2-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- punição tirada da tabela da RSSSF: Ethnikos Piraeus -4 pontos
- punição tirada da tabela da RSSSF: Panargiakos -2 pontos

### 1957/58

- a tabela da RSSSF dá ao Proodeftiki 10-3-9 (os jogos e a tabela da Wikipédia, 9-3-10) e 1 ponto a mais ao Olympiacos e ao Panionios; a da Wikipédia fecha com os jogos e dá as punições
- AEK Atenas x Apollon Kalamarias: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- AEK Atenas x Doxa Drama: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- AEK Atenas x OFI Creta: fica 4-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-1
- Panathinaikos x Doxa Drama: fica 3-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Panathinaikos x PAOK: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-2
- Apollon Kalamarias x AEK Atenas: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-2
- Apollon Kalamarias x Panionios: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-2
- Apollon Kalamarias x Proodeftiki: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Apollon Kalamarias x Doxa Drama: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Apollon Kalamarias x PAOK: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Apollon Kalamarias x Apollon Smyrnis: fica 1-5 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-2
- Panionios x Apollon Kalamarias: fica 2-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Panionios x Proodeftiki: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- Panionios x Iraklis: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Panionios x Apollon Smyrnis: fica 5-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Proodeftiki x Apollon Kalamarias: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- Proodeftiki x Panionios: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- Proodeftiki x Ethnikos Piraeus: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Doxa Drama x AEK Atenas: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- Doxa Drama x Panathinaikos: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-3
- Doxa Drama x Apollon Kalamarias: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Doxa Drama x Iraklis: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- PAOK x Panathinaikos: fica 2-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- PAOK x Apollon Kalamarias: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-2
- PAOK x Apollon Smyrnis: fica 2-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- Iraklis x Apollon Kalamarias: fica 0-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-0
- Iraklis x Doxa Drama: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Iraklis x Ethnikos Piraeus: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Iraklis x OFI Creta: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Ethnikos Piraeus x Iraklis: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Apollon Smyrnis x Olympiacos: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-2
- Apollon Smyrnis x AEK Atenas: fica 1-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-4
- Apollon Smyrnis x Panathinaikos: fica 2-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Apollon Smyrnis x Apollon Kalamarias: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Apollon Smyrnis x Panionios: fica 1-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-1
- Apollon Smyrnis x Doxa Drama: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-1
- Apollon Smyrnis x PAOK: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-2
- Apollon Smyrnis x Iraklis: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-5
- Apollon Smyrnis x Ethnikos Piraeus: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-5
- Apollon Smyrnis x OFI Creta: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-2
- OFI Creta x AEK Atenas: fica 1-3 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-4
- OFI Creta x Apollon Smyrnis: fica 3-4 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-2
- tabela da RSSSF x jogos — Proodeftiki tabela [22, 10, 3, 9, 32, 33] jogos [22, 9, 3, 10, 32, 33]
- punição pela tabela da Wikipédia (que fecha com os jogos): Ethnikos Piraeus -2 pontos

### 1958/59

- PAOK x Ethnikos Piraeus: fica 2-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-2
- punição tirada da tabela da RSSSF: Apollon Kalamarias -1 pontos
- placar diferente na matriz da Wikipédia — Olympiacos x Doxa Drama: RSSSF 3-1; Wikipédia 4-1

### 1959/60

- sem ocorrências

### 1960/61

- sem ocorrências

### 1961/62

- sem ocorrências

### 1962/63

- nota da RSSSF com placar diferente da matriz: Panionios - Egaleo originally 1-1 , 2-0 forfait Egaleo -1 point (matriz 1-1)

### 1963/64

- sem ocorrências

### 1964/65

- sem ocorrências

### 1965/66

- Aris Salônica x Niki Volos: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-1
- PAOK x Panionios: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1

### 1966/67

- a tabela da RSSSF dá 47 pontos ao Trikala; os jogos dão 48, como a tabela da Wikipédia: erro da RSSSF
- tabela publicada x jogos (RSSSF) — Veria tabela [30, 8, 7, 15, 23, 37, 53] jogos [30, 7, 9, 14, 23, 37, 53] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Trikala tabela [30, 6, 6, 18, 29, 54, 47] jogos [30, 6, 6, 18, 29, 54, 48] (a tabela da Wikipédia fecha com os jogos)

### 1967/68

- AEK Atenas x Egaleo: fica 3-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-0
- AEK Atenas x Panelefsiniakos: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Olympiakos Nicosia não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1968/69

- AEL Limassol não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1969/70

- Panachaiki x Aris Salônica: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-2
- Olympiakos Nicosia não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1970/71

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Egaleo', 'Iraklis'])
- EPA Larnaca não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1971/72

- Panathinaikos x Apollon Smyrnis: fica 3-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Panathinaikos x Fostiras: fica 7-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 6-0
- Panathinaikos x Olympiacos Volos: fica 5-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 7-2
- Panathinaikos x Pierikos: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-1
- Panathinaikos x Veria: fica 6-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Olympiakos Nicosia não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1972/73

- Panathinaikos x Aris Salônica: fica 7-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 7-0
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Panionios', 'Iraklis'])
- Omonia Nicosia não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1973/74

- Aris Salônica x Olympiacos: fica 2-4 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-4
- a tabela da RSSSF dá 55 pontos ao Panathinaikos; os jogos dão 54, como a tabela da Wikipédia: erro da RSSSF
- tabela publicada x jogos (RSSSF) — Panathinaikos tabela [34, 24, 6, 4, 76, 27, 55] jogos [34, 24, 6, 4, 76, 27, 54] (a tabela da Wikipédia fecha com os jogos)
- APOEL não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga cipriota

### 1974/75

- sem ocorrências

### 1975/76

- Panionios x Atromitos: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0

### 1976/77

- Olympiacos x Atromitos: fica 5-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 5-0
- tabela publicada x jogos (RSSSF) — Atromitos tabela [34, 6, 4, 24, 28, 68, 14] jogos [34, 6, 4, 24, 28, 68, 13] (a tabela da Wikipédia fecha com os jogos)

### 1977/78

- Apollon Smyrnis x Iraklis: fica 2-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- Panathinaikos x Veria: fica 6-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-1
- Panserraikos x AEK Atenas: fica 0-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-1
- tabela publicada x jogos (RSSSF) — Panathinaikos tabela [34, 19, 7, 8, 64, 25, 45] jogos [34, 19, 7, 8, 63, 25, 45] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Olympiacos tabela [34, 17, 10, 7, 47, 19, 44] jogos [34, 17, 10, 7, 46, 20, 44] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Aris Salônica tabela [34, 12, 12, 10, 39, 36, 36] jogos [34, 12, 12, 10, 39, 35, 36] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — OFI Creta tabela [34, 9, 14, 11, 32, 46, 32] jogos [34, 9, 14, 11, 32, 47, 32] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panserraikos tabela [34, 11, 6, 17, 29, 40, 28] jogos [34, 11, 6, 17, 31, 38, 28] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Pierikos tabela [34, 10, 6, 18, 46, 55, 26] jogos [34, 10, 6, 18, 46, 56, 26] (a tabela da Wikipédia fecha com os jogos)

### 1978/79

- Olympiacos x Apollon Smyrnis: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- placar diferente na matriz da Wikipédia — Olympiacos x Larissa: RSSSF 4-1; Wikipédia 4-3
- placar diferente na matriz da Wikipédia — Olympiacos x PAS Giannina: RSSSF 4-3; Wikipédia 2-1
- tabela publicada x jogos (RSSSF) — Rodos tabela [34, 13, 3, 18, 50, 64, 29] jogos [34, 13, 3, 18, 50, 62, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Larissa tabela [34, 12, 5, 17, 34, 53, 29] jogos [34, 12, 5, 17, 32, 53, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Egaleo tabela [34, 10, 6, 18, 34, 59, 26] jogos [34, 10, 6, 18, 33, 57, 26] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panserraikos tabela [34, 4, 5, 25, 17, 63, 13] jogos [34, 4, 5, 25, 16, 63, 13] (a tabela da Wikipédia fecha com os jogos)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Panionios', 'PAS Giannina'])

### 1979/80

- PAOK x Kavala: fica 6-2 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 6-1

### 1980/81

- tabela publicada x jogos (RSSSF) — PAOK tabela [34, 15, 11, 8, 53, 31, 42] jogos [34, 15, 12, 7, 52, 31, 42] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panachaiki tabela [34, 9, 8, 17, 21, 26, 26] jogos [34, 9, 8, 17, 21, 36, 26] (a tabela da Wikipédia fecha com os jogos)

### 1981/82

- tabela publicada x jogos (RSSSF) — OFI Creta tabela [34, 11, 11, 12, 37, 35, 33] jogos [34, 11, 11, 12, 38, 36, 33] (a tabela da Wikipédia fecha com os jogos)

### 1982/83

- Ethnikos Piraeus x PAS Giannina: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- PAS Giannina x AEK Atenas: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- tabela publicada x jogos (RSSSF) — Panathinaikos tabela [34, 14, 9, 11, 49, 42, 37] jogos [34, 14, 9, 11, 50, 42, 37] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Iraklis tabela [34, 12, 10, 12, 54, 43, 34] jogos [34, 12, 10, 12, 52, 39, 34] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Ethnikos Piraeus tabela [34, 10, 11, 13, 39, 38, 31] jogos [34, 10, 11, 13, 34, 38, 31] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Makedonikos tabela [34, 11, 7, 16, 30, 52, 29] jogos [34, 11, 7, 16, 30, 50, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panachaiki tabela [34, 11, 4, 19, 34, 49, 26] jogos [34, 11, 4, 19, 35, 50, 26] (a tabela da Wikipédia fecha com os jogos)

### 1983/84

- tabela publicada x jogos (RSSSF) — Ethnikos Piraeus tabela [30, 11, 4, 15, 38, 43, 26] jogos [30, 9, 8, 13, 38, 43, 26] (a tabela da Wikipédia fecha com os jogos)

### 1984/85

- sem ocorrências

### 1985/86

- tabela publicada x jogos (RSSSF) — Apollon Kalamarias tabela [30, 9, 10, 11, 24, 29, 28] jogos [30, 9, 10, 11, 25, 30, 28] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — PAOK tabela [30, 10, 7, 13, 34, 39, 27] jogos [30, 10, 7, 13, 33, 38, 27] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — PAS Giannina tabela [30, 8, 8, 14, 29, 41, 24] jogos [30, 8, 8, 14, 30, 42, 24] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Apollon Smyrnis tabela [30, 5, 14, 11, 20, 35, 24] jogos [30, 5, 14, 11, 19, 34, 24] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panachaiki tabela [30, 9, 3, 18, 29, 43, 20] jogos [30, 8, 5, 17, 29, 43, 20] (a tabela da Wikipédia fecha com os jogos)

### 1986/87

- sem ocorrências

### 1987/88

- Apollon Kalamarias x Ethnikos Piraeus: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- Apollon Kalamarias x Iraklis: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1
- Apollon Kalamarias x OFI Creta: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Apollon Kalamarias x Panionios: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-0
- Apollon Kalamarias x Panserraikos: fica 5-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- Apollon Kalamarias x Veria: fica 2-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 5-0
- Olympiacos x Ethnikos Piraeus: fica 4-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- Olympiacos x Levadiakos: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0
- Apollon Kalamarias x Aris Salônica: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1 (trocado com outro jogo)
- Apollon Kalamarias x Diagoras: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0 (trocado com outro jogo)
- Apollon Kalamarias x Panathinaikos: fica 1-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-0 (trocado com outro jogo)
- Olympiacos x Apollon Kalamarias: fica 1-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0 (trocado com outro jogo)
- Olympiacos x Aris Salônica: fica 2-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1 (trocado com outro jogo)
- Olympiacos x Diagoras: fica 0-0 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 1-1 (trocado com outro jogo)

### 1988/89

- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Diagoras: RSSSF 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Doxa Drama: RSSSF 1-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Levadiakos x Apollon Kalamarias: RSSSF 2-0; Wikipédia 2-1

### 1989/90

- Ethnikos Piraeus x Iraklis: fica 0-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 0-0
- Panserraikos x Apollon Kalamarias: fica 3-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 3-0
- tabela publicada x jogos (RSSSF) — Iraklis tabela [34, 14, 11, 9, 43, 35, 39] jogos [34, 14, 11, 9, 44, 36, 39] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Aris Salônica tabela [34, 11, 13, 10, 37, 40, 35] jogos [34, 11, 13, 10, 36, 39, 35]
- tabela publicada x jogos (Wikipédia) — Aris Salônica tabela [34, 11, 13, 10, 37, 40, 35] jogos [34, 11, 13, 10, 36, 39, 35]

### 1990/91

- Panachaiki x Xanthi: fica 5-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 5-2

### 1991/92

- sem ocorrências

### 1992/93

- AEK Atenas x Panathinaikos: fica 3-1 (matriz da Wikipédia), que fecha com as tabelas; a matriz da RSSSF dá 2-1
- placar diferente na matriz da Wikipédia — Larissa x Pierikos: RSSSF 4-3; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Larissa x PAOK: RSSSF 2-1; Wikipédia 4-3

### 1993/94

- sem ocorrências

### 1994/95

- placar diferente na matriz da Wikipédia — AEK Atenas x Larissa: ogol 2-0; Wikipédia 4-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x OFI Creta: ogol 4-0; Wikipédia 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Ethnikos Piraeus x Levadiakos: ogol 1-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Iraklis x Ionikos: ogol 6-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Iraklis x Panionios: ogol 4-1; Wikipédia 2-0 (football-data e engsoccerdata = ogol)
- tabela publicada x jogos (Wikipédia) — Iraklis tabela [34, 18, 8, 8, 55, 36, 62] jogos [34, 18, 8, 8, 62, 38, 62] (a tabela da RSSSF fecha com os jogos)
- tabela publicada x jogos (Wikipédia) — Panionios tabela [34, 10, 6, 18, 35, 56, 36] jogos [34, 10, 6, 18, 36, 58, 36] (a tabela da RSSSF fecha com os jogos)
- tabela publicada x jogos (Wikipédia) — Ionikos tabela [34, 9, 7, 18, 26, 48, 34] jogos [34, 9, 7, 18, 27, 53, 34] (a tabela da RSSSF fecha com os jogos)
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1995/96

- placar diferente na matriz da Wikipédia — Larissa x AEK Atenas: ogol 1-0; Wikipédia 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Apollon Smyrnis: ogol 1-1; Wikipédia 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Aris Salônica: ogol 1-0; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Athinaikos: ogol 1-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Edessaikos: ogol 0-2; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Ionikos: ogol 1-0; Wikipédia 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Iraklis: ogol 0-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Kalamata: ogol 1-1; Wikipédia 5-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x OFI Creta: ogol 2-6; Wikipédia 2-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Olympiacos: ogol 3-2; Wikipédia 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Panachaiki: ogol 4-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Paniliakos: ogol 1-0; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Panionios: ogol 0-0; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x PAOK: ogol 2-1; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Xanthi: ogol 1-2; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- ... e mais 2 pares com placar diferente na matriz da Wikipédia

### 1996/97

- sem ocorrências

### 1997/98

- Ionikos x Olympiacos (1997-11-23): placar corrigido para 0-1 (o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as tabelas da RSSSF e da Wikipédia dão 0-1)
- placar diferente na matriz da Wikipédia — Paniliakos x Panachaiki: ogol 2-0; Wikipédia 2-1 (football-data e engsoccerdata = ogol)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Apollon Smyrnis', 'Panionios'])

### 1998/99

- Aris Salônica x Ionikos (1998-09-13): placar corrigido para 1-1 (o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as tabelas da RSSSF e da Wikipédia dão 1-1)
- placar diferente na matriz da Wikipédia — Kavala x Apollon Smyrnis: ogol 0-1; Wikipédia 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Kavala x Aris Salônica: ogol 3-1; Wikipédia 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Veria: ogol 2-0; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente no engsoccerdata — PAOK x Olympiacos (1998-10-31): ogol 1-2, engsoccerdata 0-2
- placar diferente no football-data — PAOK x Olympiacos (1998-10-31): ogol 1-2, football-data 0-2
- tabela publicada x jogos (RSSSF) — Olympiacos tabela [34, 27, 4, 3, 82, 21, 85] jogos [34, 27, 4, 3, 82, 22, 85] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — PAOK tabela [34, 19, 5, 10, 51, 31, 62] jogos [34, 19, 5, 10, 52, 31, 62] (a tabela da Wikipédia fecha com os jogos)

### 1999/00

- placar diferente na matriz da Wikipédia — Aris Salônica x Panionios: ogol 5-1; Wikipédia 3-2, 5-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Iraklis x Aris Salônica: ogol 2-0; Wikipédia 2-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Iraklis x Panionios: ogol 1-2; Wikipédia 1-2, 2-2 (football-data e engsoccerdata = ogol)
- tabela publicada x jogos (RSSSF) — AEK Atenas tabela [34, 20, 6, 6, 69, 39, 66] jogos [34, 20, 6, 8, 69, 39, 66] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Xanthi tabela [34, 11, 8, 16, 36, 43, 41] jogos [34, 11, 8, 15, 36, 43, 41] (a tabela da Wikipédia fecha com os jogos)

### 2000/01

- tabela publicada x jogos (RSSSF) — Olympiacos tabela [30, 25, 2, 2, 84, 22, 78] jogos [30, 25, 3, 2, 84, 22, 78] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Panathinaikos tabela [30, 20, 6, 2, 61, 20, 66] jogos [30, 20, 6, 4, 61, 20, 66] (a tabela da Wikipédia fecha com os jogos)

### 2001/02

- Panachaiki x Ethnikos Asteras (2001-10-14): mando e placar corrigidos (o ogol traz Ethnikos Asteras 1-1 Panachaiki nesta data e de novo em 17/02/2002; o engsoccerdata, a matriz da Wikipédia e as tabelas da RSSSF e da Wikipédia dão Panachaiki 0-0 Ethnikos Asteras na 3ª rodada)

### 2002/03

- sem ocorrências

### 2003/04

- placar diferente na matriz da Wikipédia — Egaleo x Panionios: ogol 0-0; Wikipédia 4-1 (football-data e engsoccerdata = ogol)

### 2004/05

- o clube da liga era o Chalkidona (Wikipédia, engsoccerdata); ele se fundiu com o Atromitos em 2005 e o ogol põe a temporada no código do Atromitos
- placar diferente no engsoccerdata — Aris Salônica x Iraklis (2005-05-15): ogol 0-2, engsoccerdata 1-2

### 2005/06

- placar diferente na matriz da Wikipédia — Levadiakos x PAOK: ogol 2-2; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Xanthi x PAOK: ogol 1-0; Wikipédia 1-1 (football-data e engsoccerdata = ogol)

### 2006/07

- Ionikos x Iraklis (2006-12-09): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — AEK Atenas x AO Kerkyra: ogol 4-1; Wikipédia 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Ergotelis: ogol 2-1; Wikipédia 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x OFI Creta: ogol 2-2; Wikipédia 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Egaleo x Aris Salônica: ogol 1-1; Wikipédia 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Ionikos x Egaleo: ogol 0-1; Wikipédia 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Ionikos x Ergotelis: ogol 1-3; Wikipédia 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Ergotelis: ogol 1-0; Wikipédia 3-1 (football-data e engsoccerdata = ogol)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 4 posições (ex.: ['Larissa', 'Xanthi'])

### 2007/08

- Apollon Kalamarias x Olympiacos (2008-02-03): IJ no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 1-1; Wikipédia 1-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panionios: ogol 2-3; Wikipédia 2-3, 5-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 0-1; Wikipédia 0-1, 4-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x Panathinaikos: ogol 0-1; Wikipédia 0-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x Panionios: ogol 0-0; Wikipédia 0-0, 3-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 2-1; Wikipédia 2-1, 4-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Aris Salônica: ogol 1-0; Wikipédia 1-0, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Panionios: ogol 2-1; Wikipédia 2-1, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x AEK Atenas: ogol 0-3; Wikipédia 0-3, 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Aris Salônica: ogol 0-3; Wikipédia 0-3, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Panathinaikos: ogol 1-0; Wikipédia 1-0, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Xanthi: ogol 3-2; Wikipédia 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Veria: ogol 2-2; Wikipédia 3-2 (football-data e engsoccerdata = ogol)
- tabela publicada x jogos (Wikipédia) — Aris Salônica tabela [30, 14, 8, 8, 32, 20, 50] jogos [30, 14, 8, 8, 33, 20, 50] (a tabela da RSSSF fecha com os jogos)
- tabela publicada x jogos (Wikipédia) — Iraklis tabela [30, 8, 11, 11, 28, 33, 35] jogos [30, 8, 11, 11, 28, 34, 35] (a tabela da RSSSF fecha com os jogos)
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 2008/09

- placar diferente na matriz da Wikipédia — AEK Atenas x Larissa: ogol 1-1; Wikipédia 1-1, 3-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 2-1; Wikipédia 0-2, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-0; Wikipédia 1-0, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x AEK Atenas: ogol 1-1; Wikipédia 0-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Panathinaikos: ogol 1-1; Wikipédia 0-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x PAOK: ogol 0-0; Wikipédia 0-0, 0-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 0-0; Wikipédia 0-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Larissa: ogol 3-0; Wikipédia 3-0, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 3-0; Wikipédia 3-0, 4-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 1-1; Wikipédia 0-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Larissa: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 0-0; Wikipédia 0-0, 0-1 (football-data e engsoccerdata = ogol)

### 2009/10

- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 1-0; Wikipédia 1-0, 4-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 1-2; Wikipédia 1-2, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-0; Wikipédia 0-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 1-0; Wikipédia 1-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x PAOK: ogol 2-0; Wikipédia 2-0, 3-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos x AEK Atenas: ogol 1-2; Wikipédia 1-2, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos x Aris Salônica: ogol 2-1; Wikipédia 0-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos x PAOK: ogol 0-1; Wikipédia 0-1, 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 0-1; Wikipédia 0-1, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Aris Salônica: ogol 4-1; Wikipédia 2-0, 4-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Olympiacos: ogol 1-2; Wikipédia 1-0, 1-2 (football-data e engsoccerdata = ogol)

### 2010/11

- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos Volos: ogol 0-4; Wikipédia 0-4, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-0; Wikipédia 0-2, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 4-0; Wikipédia 3-0, 4-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos Volos x AEK Atenas: ogol 3-1; Wikipédia 1-0, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos Volos x Panathinaikos: ogol 3-2; Wikipédia 2-1, 3-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Olympiacos Volos x PAOK: ogol 0-3; Wikipédia 0-3, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 3-1; Wikipédia 1-1, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Olympiacos Volos: ogol 0-1; Wikipédia 0-1, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 2-1; Wikipédia 2-1, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Olympiacos Volos: ogol 1-1; Wikipédia 1-1, 5-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 0-1; Wikipédia 0-1, 2-1 (football-data e engsoccerdata = ogol)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 6 posições (ex.: ['Atromitos', 'AO Kerkyra'])

### 2011/12

- Panathinaikos x Olympiacos (2012-03-18): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Aris Salônica x Asteras Tripolis (2012-04-08): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — AEK Atenas x Atromitos: ogol 0-0; Wikipédia 0-0, 3-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 2-0; Wikipédia 2-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 0-2; Wikipédia 0-2, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x AEK Atenas: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Panathinaikos: ogol 1-1; Wikipédia 0-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x PAOK: ogol 0-0; Wikipédia 0-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 3-2; Wikipédia 1-0, 3-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Atromitos: ogol 1-0; Wikipédia 1-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 0-2; Wikipédia 0-2, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 3-0; Wikipédia 1-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Atromitos: ogol 3-1; Wikipédia 0-1, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 1-3; Wikipédia 1-0, 1-3 (football-data e engsoccerdata = ogol)
- placar diferente na ESPN — AO Kerkyra x Panetolikos (2011-09-17): ogol 2-3, ESPN 1-2
- placar diferente na ESPN — Levadiakos x AO Kerkyra (2012-03-04): ogol 4-3, ESPN 2-1

### 2012/13

- AEK Atenas x Panthrakikos (2013-04-14): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 3-0; Wikipédia 2-1, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x PAOK: ogol 1-0; Wikipédia 1-0, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x PAS Giannina: ogol 2-0; Wikipédia 2-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Asteras Tripolis: ogol 0-2; Wikipédia 0-0, 0-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x PAOK: ogol 1-0; Wikipédia 1-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x PAS Giannina: ogol 0-0; Wikipédia 0-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Asteras Tripolis: ogol 2-1; Wikipédia 1-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Atromitos: ogol 0-0; Wikipédia 0-0, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x PAS Giannina: ogol 2-0; Wikipédia 0-1, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAS Giannina x Asteras Tripolis: ogol 1-2; Wikipédia 1-2, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAS Giannina x Atromitos: ogol 0-0; Wikipédia 0-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAS Giannina x PAOK: ogol 1-3; Wikipédia 1-2, 1-3 (football-data e engsoccerdata = ogol)
- placar diferente na ESPN — Olympiacos x Platanias (2012-12-01): ogol 2-1, ESPN 2-0
- tabela da RSSSF com outros clubes: ['AEK Atenas', 'AO Kerkyra', 'Aris Salônica', 'Levadiakos', 'OFI Creta', 'Panionios', 'Panthrakikos', 'Platanias', 'Veria', 'Xanthi']

### 2013/14

- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 2-2; Wikipédia 1-0, 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Panathinaikos: ogol 1-0; Wikipédia 1-0, 1-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x PAOK: ogol 2-1; Wikipédia 1-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Asteras Tripolis: ogol 3-1; Wikipédia 3-1, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Panathinaikos: ogol 0-0; Wikipédia 0-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x PAOK: ogol 1-1; Wikipédia 1-1, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Asteras Tripolis: ogol 2-1; Wikipédia 1-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Atromitos: ogol 1-2; Wikipédia 1-1, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 2-1; Wikipédia 1-1, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Asteras Tripolis: ogol 2-0; Wikipédia 1-1, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Atromitos: ogol 2-0; Wikipédia 2-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 2-1; Wikipédia 1-0, 2-1 (football-data e engsoccerdata = ogol)

### 2014/15

- Niki Volos x Panetolikos (2014-12-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- OFI Creta x Niki Volos (2015-01-03): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Levadiakos (2015-01-11): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Niki Volos x Olympiacos (2015-01-15): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Atromitos x Niki Volos (2015-01-18): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x PAOK (2015-01-25): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Atromitos x OFI Creta (2015-02-01): ANU no ogol; fica 3-0 pela matriz da Wikipédia
- Ergotelis x Niki Volos (2015-02-01): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Panathinaikos (2015-02-05): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Asteras Tripolis x Niki Volos (2015-02-08): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Panthrakikos x Niki Volos (2015-02-14): ANU no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Xanthi (2015-02-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- PAE Kerkyra x Niki Volos (2015-03-01): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x PAS Giannina (2015-03-08): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Levadiakos x Niki Volos (2015-03-15): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Panionios (2015-03-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- OFI Creta x PAS Giannina (2015-03-23): DA no ogol; fica 0-3 pela matriz da Wikipédia
- AEL Kalloni x Niki Volos (2015-04-04): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Levadiakos x OFI Creta (2015-04-05): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Platanias (2015-04-10): DA no ogol; fica 0-3 pela matriz da Wikipédia
- OFI Creta x Panionios (2015-04-19): DA no ogol; fica 0-3 pela matriz da Wikipédia
- AEL Kalloni x OFI Creta (2015-04-25): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Niki Volos x Veria (2015-04-26): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Panetolikos x Niki Volos (2015-05-03): DA no ogol; fica 3-0 pela matriz da Wikipédia
- OFI Creta x Platanias (2015-05-03): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Niki Volos x OFI Creta (2015-05-10): ANU no ogol; derrota para os dois
- Asteras Tripolis x Ergotelis (2015-03-22): placar corrigido para 2-1 (o ogol dá 3-0; o football-data, o engsoccerdata, a ESPN e as tabelas da RSSSF e da Wikipédia dão 2-1)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Panathinaikos: ogol 1-1; Wikipédia 0-4, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x PAOK: ogol 3-0; Wikipédia 1-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Asteras Tripolis: ogol 4-3; Wikipédia 0-0, 4-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x Panathinaikos: ogol 2-0; Wikipédia 2-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Atromitos x PAOK: ogol 4-0; Wikipédia 1-1, 4-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Asteras Tripolis: ogol 2-2; Wikipédia 0-0, 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Atromitos: ogol 2-0; Wikipédia 2-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 4-3; Wikipédia 2-0, 4-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Asteras Tripolis: ogol 0-0; Wikipédia 0-0, 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Atromitos: ogol 2-1; Wikipédia 0-1, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 1-2; Wikipédia 0-1, 1-2 (football-data e engsoccerdata = ogol)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (vitorias) difere em 8 posições (ex.: ['AEL Kalloni', 'Panthrakikos'])

### 2015/16

- Panathinaikos x Olympiacos (2015-11-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-0; Wikipédia 1-0, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panionios: ogol 2-0; Wikipédia 1-0, 2-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-0; Wikipédia 0-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 0-0; Wikipédia 0-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Panionios: ogol 0-0; Wikipédia 0-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 2-2; Wikipédia 1-1, 2-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x AEK Atenas: ogol 1-1; Wikipédia 1-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Panathinaikos: ogol 1-0; Wikipédia 1-0, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x PAOK: ogol 3-1; Wikipédia 0-2, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 2-1; Wikipédia 2-1, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 3-1; Wikipédia 1-1, 3-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panionios: ogol 2-1; Wikipédia 2-0, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na ESPN — AEL Kalloni x Panathinaikos (2016-01-11): ogol 0-2, ESPN 5-0
- placar diferente na ESPN — Panthrakikos x PAS Giannina (2016-02-28): ogol 2-4, ESPN 1-1
- tabela publicada x jogos (RSSSF) — AEK Atenas tabela [30, 17, 6, 7, 43, 21, 57] jogos [30, 17, 6, 7, 43, 21, 54] (a tabela da Wikipédia fecha com os jogos)
- tabela publicada x jogos (RSSSF) — Atromitos tabela [30, 12, 6, 12, 26, 31, 42] jogos [30, 12, 6, 12, 26, 31, 39] (a tabela da Wikipédia fecha com os jogos)
- tabela do Play-off europeu (Wikipédia) x jogos — AEK Atenas tabela [6, 2, 1, 3, 5, 7, 9] jogos [6, 2, 1, 3, 6, 7, 9]
- tabela do Play-off europeu (Wikipédia) x jogos — Panionios tabela [6, 1, 1, 4, 2, 7, 4] jogos [6, 1, 1, 4, 2, 8, 4]

### 2016/17

- Panathinaikos x PAOK (2017-05-17): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 2-3; Wikipédia 1-0, 2-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panionios: ogol 0-0; Wikipédia 0-0, 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 3-0; Wikipédia 1-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x AEK Atenas: ogol 0-0; Wikipédia 0-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x Panionios: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panathinaikos x PAOK: ogol 1-0; Wikipédia 0-3, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x AEK Atenas: ogol 1-1; Wikipédia 1-1, 1-2 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x Panathinaikos: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Panionios x PAOK: ogol 1-0; Wikipédia 0-1, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x AEK Atenas: ogol 1-0; Wikipédia 0-1, 1-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panathinaikos: ogol 3-0; Wikipédia 2-3, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — PAOK x Panionios: ogol 1-0; Wikipédia 1-0, 1-0 (football-data e engsoccerdata = ogol)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 4 posições (ex.: ['Asteras Tripolis', 'Larissa'])

### 2017/18

- PAOK x Olympiacos (2018-02-25): DA no ogol; fica 0-3 pela matriz da Wikipédia
- PAOK x AEK Atenas (2018-03-11): DA no ogol; fica 0-3 pela matriz da Wikipédia
- tabela publicada x jogos (RSSSF) — Panathinaikos tabela [30, 10, 10, 10, 30, 30, 29] jogos [30, 10, 10, 10, 30, 30, 32] (a tabela da Wikipédia fecha com os jogos)

### 2018/19

- Panathinaikos x Olympiacos (2019-03-17): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2019/20

- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 1-1; Wikipédia 1-1, 2-2
- placar diferente na matriz da Wikipédia — AEK Atenas x OFI Creta: ogol 3-0; Wikipédia 2-0, 3-0
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 0-0; Wikipédia 0-0, 1-2
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-0; Wikipédia 1-0, 1-1
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 2-2; Wikipédia 0-0, 2-2
- placar diferente na matriz da Wikipédia — Larissa x Asteras Tripolis: ogol 3-0; Wikipédia 1-2, 3-0
- placar diferente na matriz da Wikipédia — Larissa x Panionios: ogol 2-0; Wikipédia 0-0, 2-0
- placar diferente na matriz da Wikipédia — Larissa x Volos NFC: ogol 2-1; Wikipédia 2-1, 3-1
- placar diferente na matriz da Wikipédia — Larissa x Xanthi: ogol 3-0; Wikipédia 0-0, 3-0
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 0-1; Wikipédia 0-1, 1-4
- placar diferente na matriz da Wikipédia — Aris Salônica x OFI Creta: ogol 1-1; Wikipédia 1-1, 3-1
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 1-2; Wikipédia 1-2, 2-4
- placar diferente na matriz da Wikipédia — Aris Salônica x Panathinaikos: ogol 4-0; Wikipédia 0-1, 4-0
- placar diferente na matriz da Wikipédia — Aris Salônica x PAOK: ogol 4-2; Wikipédia 0-2, 4-2
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 2-1; Wikipédia 1-1, 2-1
- ... e mais 43 pares com placar diferente na matriz da Wikipédia
- tabela publicada x jogos (RSSSF) — Xanthi tabela [26, 8, 6, 12, 21, 32, 30] jogos [26, 8, 6, 12, 21, 32, 18] (a tabela da Wikipédia fecha com os jogos)

### 2020/21

- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 0-2; Wikipédia 0-0, 0-2
- placar diferente na matriz da Wikipédia — AEK Atenas x Asteras Tripolis: ogol 2-2; Wikipédia 2-2, 3-1
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 1-1; Wikipédia 1-1, 1-5
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-2; Wikipédia 1-1, 1-2
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-1; Wikipédia 1-1, 1-2
- placar diferente na matriz da Wikipédia — Larissa x OFI Creta: ogol 0-1; Wikipédia 0-1, 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Panetolikos: ogol 1-0; Wikipédia 1-0, 1-1
- placar diferente na matriz da Wikipédia — Larissa x PAS Giannina: ogol 0-0; Wikipédia 0-0, 2-0
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Larissa: ogol 1-0; Wikipédia 0-2, 1-0
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Lamia: ogol 0-1; Wikipédia 0-1, 0-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x OFI Creta: ogol 2-1; Wikipédia 0-0, 2-1
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Volos NFC: ogol 3-3; Wikipédia 0-0, 3-3
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 0-1; Wikipédia 0-1, 1-3
- placar diferente na matriz da Wikipédia — Aris Salônica x Asteras Tripolis: ogol 1-0; Wikipédia 1-0, 2-0
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 1-2; Wikipédia 1-1, 1-2
- ... e mais 43 pares com placar diferente na matriz da Wikipédia

### 2021/22

- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 2-1; Wikipédia 1-2, 2-1
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 2-3; Wikipédia 2-3, 2-3 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-0; Wikipédia 0-0, 1-0
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-1; Wikipédia 0-1, 1-1
- placar diferente na matriz da Wikipédia — AEK Atenas x PAS Giannina: ogol 2-0; Wikipédia 2-0, 3-0
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Lamia: ogol 0-0; Wikipédia 0-0, 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Panetolikos: ogol 0-0; Wikipédia 0-0, 1-0
- placar diferente na matriz da Wikipédia — Apollon Smyrnis x Volos NFC: ogol 1-3; Wikipédia 1-1, 1-3
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 2-1; Wikipédia 2-1, 3-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 2-1; Wikipédia 0-1, 2-1
- placar diferente na matriz da Wikipédia — Aris Salônica x Panathinaikos: ogol 1-0; Wikipédia 0-0, 1-0
- placar diferente na matriz da Wikipédia — Aris Salônica x PAOK: ogol 0-0; Wikipédia 0-0, 1-0
- placar diferente na matriz da Wikipédia — Aris Salônica x PAS Giannina: ogol 0-5; Wikipédia 0-0, 0-5
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Apollon Smyrnis: ogol 1-0; Wikipédia 1-0, 2-2
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 6-2; Wikipédia 0-0, 6-2
- ... e mais 43 pares com placar diferente na matriz da Wikipédia

### 2022/23

- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 3-0; Wikipédia 3-0, 3-1
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 1-3; Wikipédia 0-0, 1-3
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 1-0; Wikipédia 0-0, 1-0
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 2-0; Wikipédia 2-0, 4-0
- placar diferente na matriz da Wikipédia — AEK Atenas x Volos NFC: ogol 0-1; Wikipédia 0-1, 4-0
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 0-2; Wikipédia 0-2, 1-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 2-1; Wikipédia 2-1, 2-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Aris Salônica x Panathinaikos: ogol 1-2; Wikipédia 0-1, 1-2
- placar diferente na matriz da Wikipédia — Aris Salônica x PAOK: ogol 0-0; Wikipédia 0-0, 1-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Volos NFC: ogol 3-0; Wikipédia 3-0, 4-2
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Lamia: ogol 3-0; Wikipédia 0-0, 3-0
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Levadiakos: ogol 0-0; Wikipédia 0-0, 0-1
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Panetolikos: ogol 0-0; Wikipédia 0-0, 2-1
- placar diferente na matriz da Wikipédia — Atromitos x Ionikos: ogol 2-0; Wikipédia 2-0, 2-0 (football-data e engsoccerdata = ogol)
- ... e mais 43 pares com placar diferente na matriz da Wikipédia

### 2023/24

- Olympiacos x Panathinaikos (2023-10-22): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Kifisia x Volos NFC (2024-02-11): placar corrigido para 3-0 (0-0 em campo; em 04/03/2024 a vitória foi dada ao Kifisia por 3-0, depois da agressão racista do presidente do Volos a Andrews Tetteh (nota da matriz da Wikipédia); as tabelas da RSSSF e da Wikipédia contam o 3-0)
- placar diferente na matriz da Wikipédia — AEK Atenas x Aris Salônica: ogol 1-0; Wikipédia 1-0, 2-0
- placar diferente na matriz da Wikipédia — AEK Atenas x Lamia: ogol 3-0; Wikipédia 3-0, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 1-1; Wikipédia 1-0, 1-1
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 2-2; Wikipédia 2-2, 3-0
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 2-0; Wikipédia 2-0, 2-2
- placar diferente na matriz da Wikipédia — Kifisia x OFI Creta: ogol 0-0; Wikipédia 0-0, 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Kifisia x Panetolikos: ogol 2-2; Wikipédia 0-1, 2-2
- placar diferente na matriz da Wikipédia — Kifisia x PAS Giannina: ogol 4-2; Wikipédia 2-3, 4-2
- placar diferente na matriz da Wikipédia — Aris Salônica x AEK Atenas: ogol 3-3; Wikipédia 1-2, 3-3
- placar diferente na matriz da Wikipédia — Aris Salônica x Lamia: ogol 2-2; Wikipédia 2-2, 3-1
- placar diferente na matriz da Wikipédia — Aris Salônica x Olympiacos: ogol 1-2; Wikipédia 1-1, 1-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Panathinaikos: ogol 2-0; Wikipédia 0-2, 2-0
- placar diferente na matriz da Wikipédia — Aris Salônica x PAOK: ogol 2-1; Wikipédia 1-2, 2-1
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Kifisia: ogol 3-3; Wikipédia 1-2, 3-3
- placar diferente na matriz da Wikipédia — Asteras Tripolis x OFI Creta: ogol 3-0; Wikipédia 1-1, 3-0
- ... e mais 43 pares com placar diferente na matriz da Wikipédia

### 2024/25

- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 0-1; Wikipédia 0-1, 0-2
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 2-0; Wikipédia 1-2, 2-0
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 1-1; Wikipédia 1-1, 2-3
- placar diferente na matriz da Wikipédia — Aris Salônica x Asteras Tripolis: ogol 1-1; Wikipédia 1-1, 4-2
- placar diferente na matriz da Wikipédia — Aris Salônica x Atromitos: ogol 2-1; Wikipédia 1-0, 2-1
- placar diferente na matriz da Wikipédia — Aris Salônica x OFI Creta: ogol 0-2; Wikipédia 0-2, 2-0
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Aris Salônica: ogol 2-1; Wikipédia 0-2, 2-1
- placar diferente na matriz da Wikipédia — Asteras Tripolis x Atromitos: ogol 1-2; Wikipédia 1-2, 1-4
- placar diferente na matriz da Wikipédia — Asteras Tripolis x OFI Creta: ogol 3-0; Wikipédia 2-1, 3-0
- placar diferente na matriz da Wikipédia — Kallithea x Lamia: ogol 2-1; Wikipédia 2-1, 3-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Kallithea x Levadiakos: ogol 2-4; Wikipédia 0-3, 2-4
- placar diferente na matriz da Wikipédia — Kallithea x Panetolikos: ogol 1-1; Wikipédia 0-0, 1-1
- placar diferente na matriz da Wikipédia — Kallithea x Panserraikos: ogol 1-2; Wikipédia 1-1, 1-2
- placar diferente na matriz da Wikipédia — Kallithea x Volos NFC: ogol 2-0; Wikipédia 1-1, 2-0
- placar diferente na matriz da Wikipédia — Atromitos x Aris Salônica: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- ... e mais 39 pares com placar diferente na matriz da Wikipédia

### 2025/26

- placar diferente na matriz da Wikipédia — AEK Atenas x Olympiacos: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — AEK Atenas x Panathinaikos: ogol 4-0; Wikipédia 2-1, 4-0
- placar diferente na matriz da Wikipédia — AEK Atenas x PAOK: ogol 0-2; Wikipédia 0-2, 3-0
- placar diferente na matriz da Wikipédia — Kifisia x Larissa: ogol 1-1; Wikipédia 1-1, 3-2
- placar diferente na matriz da Wikipédia — Kifisia x Asteras Tripolis: ogol 0-0; Wikipédia 0-0, 0-0 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Kifisia x Atromitos: ogol 0-1; Wikipédia 0-1, 0-3
- placar diferente na matriz da Wikipédia — Kifisia x Panetolikos: ogol 1-1; Wikipédia 0-0, 1-1
- placar diferente na matriz da Wikipédia — Kifisia x Panserraikos: ogol 3-0; Wikipédia 1-2, 3-0
- placar diferente na matriz da Wikipédia — Larissa x Kifisia: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Asteras Tripolis: ogol 1-1; Wikipédia 1-1, 1-1 (football-data e engsoccerdata = ogol)
- placar diferente na matriz da Wikipédia — Larissa x Atromitos: ogol 0-0; Wikipédia 0-0, 2-1
- placar diferente na matriz da Wikipédia — Larissa x Panetolikos: ogol 1-4; Wikipédia 1-2, 1-4
- placar diferente na matriz da Wikipédia — Larissa x Panserraikos: ogol 1-0; Wikipédia 0-1, 1-0
- placar diferente na matriz da Wikipédia — Aris Salônica x Levadiakos: ogol 2-2; Wikipédia 2-2, 3-0
- placar diferente na matriz da Wikipédia — Aris Salônica x OFI Creta: ogol 0-2; Wikipédia 0-2, 3-1
- ... e mais 39 pares com placar diferente na matriz da Wikipédia

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_gre.py`: pela linhagem do clube, como na Wikipédia (o alvo do link na tabela de cada temporada). Mesmo clube: Apollon Athens e Apollon Smyrnis; Apollon Salonika/Thessaloniki/Kalamarias; Xanthi e Skoda Xanthi; Pankorinthiakos e Korinthos; Megas Alexandros e Pierikos. Clubes diferentes: Atromitos Piraeus e Atromitos; Rodos e AE Rodos; AO Kerkyra e PAE Kerkyra; Chalkidona (2004/05, que o ogol põe no Atromitos).
- A ESPN é casada por votação jogo a jogo (mesma data e placar): 40 códigos.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Datas e rodadas de 1959/60 a 1992/93:** a matriz da RSSSF e a da Wikipédia não trazem; o ogol não tem esses jogos. Rodadas de 1994/95 a 1996/97: o ogol não traz.
- **Era antiga (até 1958/59):** só a fase nacional; as ligas regionais ficam de fora.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (só as fichas dos jogos-desempate).
- **Jogos de acesso contra clubes da 2ª divisão:** ficam de fora.
