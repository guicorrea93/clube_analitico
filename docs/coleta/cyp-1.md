# Campeonato Cipriota (1ª divisão) — coleta de dados

Gerado por `python coleta/cyp-1/importar.py`. Pacote em `data/coleta/cyp-1/pacote/`.

**Edições:** 86, de 1934/35 a 2025/26: os 86 títulos que a federação reconhece.

**Total:** 13465 jogos, 40239 gols, 46 clubes. Sem autores dos gols e cartões (sem ESPN e sem football-data para Chipre).

**Fontes:**
- Wikipédia (en): tabelas e matriz de resultados (base dos jogos até 1995/96, conferência depois);
- ogol (zerozero): base dos jogos desde 1996/97, com data, hora e rodada; calendários em `data/cache/ogol-cyp-1/`;
- RSSSF: página de cada temporada (tabela; jogos por rodada desde 2009/10), lista de campeões e de artilheiros.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; com grupos, o grupo do título, depois os outros). Pontos 2-1-0 até 1990/91 e 3-1-0 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (antes de uma temporada sem campeão, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 22 tabelas, saldo em 90, confronto direto em 16).

| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|
| 1934/35 | 8 | 53 | 223 | 0 | 2 / 0 | Enosis Neon Trust | — |
| 1935/36 | 8 | 48 | 223 | 0 | 0 / 2 | APOEL | — |
| 1936/37 | 7 | 42 | 195 | 0 | 0 / 2 | APOEL | — |
| 1937/38 | 5 | 12 | 62 | 0 | 0 / 1 | APOEL | — |
| 1938/39 | 7 | 33 | 167 | 0 | 0 / 2 | APOEL | — |
| 1939/40 | 6 | 29 | 134 | 0 | 2 / 0 | APOEL | — |
| 1940/41 | 5 | 16 | 118 | 0 | 0 / 2 | AEL Limassol | — |
| 1944/45 | 6 | 30 | 178 | 0 | 0 / 2 | EPA Larnaca | — |
| 1945/46 | 6 | 30 | 136 | 0 | 2 / 0 | EPA Larnaca | — |
| 1946/47 | 7 | 42 | 184 | 0 | 2 / 0 | APOEL | — |
| 1947/48 | 5 | 20 | 102 | 0 | 0 / 2 | APOEL | — |
| 1948/49 | 8 | 35 | 177 | 0 | 0 / 2 | APOEL | — |
| 1949/50 | 8 | 56 | 285 | 0 | 2 / 0 | Anorthosis | — |
| 1950/51 | 8 | 56 | 246 | 0 | 2 / 0 | Çetinkaya | — |
| 1951/52 | 8 | 56 | 240 | 0 | 2 / 0 | APOEL | — |
| 1952/53 | 8 | 56 | 224 | 0 | 0 / 2 | AEL Limassol | — |
| 1953/54 | 9 | 72 | 260 | 0 | 1 / 0 | Pezoporikos Larnaca | — |
| 1954/55 | 10 | 90 | 339 | 0 | 0 / 1 | AEL Limassol | — |
| 1955/56 | 9 | 72 | 258 | 0 | 0 / 1 | AEL Limassol | — |
| 1956/57 | 9 | 72 | 269 | 0 | 0 / 1 | Anorthosis | — |
| 1957/58 | 10 | 85 | 305 | 0 | 0 / 2 | Anorthosis | — |
| 1959/60 | 11 | 110 | 386 | 0 | 0 / 2 | Anorthosis | — |
| 1960/61 | 13 | 156 | 621 | 0 | 2 / 0 | Omonia | — |
| 1961/62 | 13 | 156 | 579 | 0 | 1 / 0 | Anorthosis | Olympiakos Nicosia -1 pontos |
| 1962/63 | 12 | 132 | 512 | 0 | 2 / 0 | Anorthosis | Orfeas Nicosia -1 pontos |
| 1964/65 | 11 | 110 | 431 | 0 | 2 / 0 | APOEL | — |
| 1965/66 | 11 | 110 | 392 | 0 | 0 / 2 | Omonia | AEL Limassol -1 pontos |
| 1966/67 | 12 | 132 | 553 | 0 | 0 / 2 | Olympiakos Nicosia | — |
| 1967/68 | 12 | 132 | 536 | 0 | 2 / 0 | AEL Limassol | — |
| 1968/69 | 12 | 132 | 387 | 0 | 2 / 0 | Olympiakos Nicosia | — |
| 1969/70 | 12 | 132 | 309 | 0 | 2 / 0 | EPA Larnaca | Anorthosis -1 pontos; Apollon Limassol -1 pontos |
| 1970/71 | 12 | 132 | 295 | 0 | 1 / 0 | Olympiakos Nicosia | — |
| 1971/72 | 12 | 132 | 255 | 0 | 2 / 0 | Omonia | — |
| 1972/73 | 14 | 182 | 358 | 0 | 1 / 0 | APOEL | — |
| 1973/74 | 14 | 182 | 400 | 0 | 2 / 0 | Omonia | — |
| 1974/75 | 14 | 182 | 510 | 0 | 2 / 0 | Omonia | — |
| 1975/76 | 15 | 210 | 621 | 0 | 2 / 0 | Omonia | — |
| 1976/77 | 16 | 240 | 679 | 0 | 2 / 0 | Omonia | — |
| 1977/78 | 16 | 240 | 632 | 0 | 0 / 2 | Omonia | — |
| 1978/79 | 16 | 240 | 548 | 0 | 0 / 2 | Omonia | — |
| 1979/80 | 15 | 210 | 537 | 0 | 0 / 1 | APOEL | — |
| 1980/81 | 14 | 182 | 450 | 0 | 0 / 1 | Omonia | — |
| 1981/82 | 14 | 182 | 414 | 0 | 1 / 0 | Omonia | — |
| 1982/83 | 14 | 182 | 442 | 0 | 0 / 1 | Omonia | — |
| 1983/84 | 14 | 182 | 455 | 0 | 0 / 1 | Omonia | — |
| 1984/85 | 14 | 182 | 464 | 0 | 1 / 0 | Omonia | — |
| 1985/86 | 14 | 182 | 483 | 0 | 0 / 1 | APOEL | — |
| 1986/87 | 16 | 240 | 678 | 0 | 0 / 1 | Omonia | — |
| 1987/88 | 16 | 240 | 648 | 0 | 1 / 0 | Pezoporikos Larnaca | — |
| 1988/89 | 15 | 210 | 598 | 0 | 1 / 0 | Omonia | — |
| 1989/90 | 14 | 182 | 467 | 0 | 1 / 0 | APOEL | — |
| 1990/91 | 14 | 182 | 501 | 0 | 1 / 0 | Apollon Limassol | APEP -4 pontos |
| 1991/92 | 14 | 182 | 540 | 0 | 1 / 0 | APOEL | — |
| 1992/93 | 14 | 182 | 612 | 0 | 1 / 0 | Omonia | — |
| 1993/94 | 14 | 182 | 592 | 0 | 1 / 0 | Apollon Limassol | APEP -4 pontos |
| 1994/95 | 12 | 198 | 617 | 0 | 1 / 0 | Anorthosis | — |
| 1995/96 | 14 | 182 | 553 | 0 | 1 / 0 | APOEL | — |
| 1996/97 | 14 | 182 | 564 | 0 | 1 / 0 | Anorthosis | — |
| 1997/98 | 14 | 182 | 657 | 0 | 1 / 0 | Anorthosis | — |
| 1998/99 | 14 | 182 | 731 | 0 | 1 / 0 | Anorthosis | — |
| 1999/00 | 14 | 182 | 670 | 0 | 1 / 0 | Anorthosis | — |
| 2000/01 | 14 | 182 | 646 | 0 | 1 / 0 | Omonia | — |
| 2001/02 | 14 | 182 | 669 | 0 | 1 / 0 | APOEL | Alki Larnaca -3 pontos |
| 2002/03 | 14 | 182 | 628 | 0 | 1 / 0 | Omonia | — |
| 2003/04 | 14 | 182 | 592 | 0 | 1 / 0 | APOEL | — |
| 2004/05 | 14 | 181 | 548 | 0 | 1 / 0 | Anorthosis | — |
| 2005/06 | 14 | 182 | 603 | 0 | 1 / 0 | Apollon Limassol | — |
| 2006/07 | 14 | 182 | 496 | 0 | 1 / 0 | APOEL | — |
| 2007/08 | 14 | 218 | 591 | 0 | 4 / 0 | Anorthosis | — |
| 2008/09 | 14 | 218 | 612 | 0 | 4 / 0 | APOEL | APOP Kinyras -6 pontos |
| 2009/10 | 14 | 218 | 577 | 0 | 4 / 0 | Omonia | APEP -6 pontos |
| 2010/11 | 14 | 218 | 569 | 0 | 4 / 0 | APOEL | — |
| 2011/12 | 14 | 218 | 478 | 0 | 4 / 0 | AEL Limassol | — |
| 2012/13 | 14 | 218 | 592 | 0 | 4 / 0 | APOEL | Olympiakos Nicosia -3 pontos; AEP Paphos -12 pontos |
| 2013/14 | 14 | 242 | 703 | 0 | 3 / 0 | APOEL | Nea Salamina -3 pontos; Enosis Paralimni -3 pontos; Alki Larnaca -41 pontos |
| 2014/15 | 12 | 192 | 503 | 0 | 3 / 0 | APOEL | — |
| 2015/16 | 14 | 242 | 669 | 0 | 3 / 0 | APOEL | AEL Limassol -2 pontos |
| 2016/17 | 14 | 242 | 696 | 0 | 3 / 0 | APOEL | AEZ Zakakiou -6 pontos; Ermis Aradippou -6 pontos |
| 2017/18 | 14 | 242 | 727 | 0 | 3 / 0 | APOEL | — |
| 2018/19 | 12 | 192 | 534 | 0 | 3 / 0 | APOEL | Anorthosis -6 pontos; Pafos FC -6 pontos |
| 2020/21 | 14 | 268 | 666 | 0 | 3 / 0 | Omonia | — |
| 2021/22 | 12 | 192 | 456 | 0 | 3 / 0 | Apollon Limassol | — |
| 2022/23 | 14 | 267 | 636 | 0 | 4 / 0 | Aris Limassol | — |
| 2023/24 | 14 | 268 | 778 | 0 | 4 / 0 | APOEL | — |
| 2024/25 | 14 | 240 | 635 | 0 | 4 / 0 | Pafos FC | — |
| 2025/26 | 14 | 240 | 633 | 0 | 4 / 0 | Omonia | — |

## Conferência e ocorrências, temporada a temporada

### 1934/35

- 53 jogos para 8 clubes (esperados 56)

### 1935/36

- tabela da Wikipédia x jogos — APOEL tabela [14, 12, 0, 2, 52, 15, 24] jogos [12, 9, 0, 3, 48, 17, 18]
- tabela da Wikipédia x jogos — Enosis Neon Trust tabela [14, 9, 2, 3, 39, 21, 20] jogos [12, 7, 2, 3, 35, 19, 16]
- tabela da Wikipédia x jogos — Çetinkaya tabela [14, 9, 1, 4, 28, 21, 19] jogos [13, 8, 1, 4, 27, 21, 17]
- tabela da Wikipédia x jogos — AEL Limassol tabela [14, 8, 1, 5, 35, 17, 17] jogos [13, 7, 1, 5, 34, 18, 15]
- tabela da Wikipédia x jogos — Aris Limassol tabela [14, 8, 0, 6, 37, 33, 16] jogos [13, 8, 0, 5, 36, 29, 16]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [14, 4, 1, 9, 23, 56, 9] jogos [14, 4, 1, 9, 21, 56, 9]
- tabela da Wikipédia x jogos — Anorthosis tabela [14, 2, 1, 11, 14, 38, 5] jogos [11, 1, 1, 9, 14, 34, 3]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [14, 0, 2, 12, 8, 35, 2] jogos [8, 0, 2, 6, 8, 29, 2]
- tabela da RSSSF x jogos — APOEL tabela [14, 12, 0, 2, 52, 15, 24] jogos [12, 9, 0, 3, 48, 17, 18]
- tabela da RSSSF x jogos — Enosis Neon Trust tabela [14, 9, 2, 3, 39, 21, 20] jogos [12, 7, 2, 3, 35, 19, 16]
- tabela da RSSSF x jogos — Çetinkaya tabela [14, 9, 1, 4, 28, 21, 19] jogos [13, 8, 1, 4, 27, 21, 17]
- tabela da RSSSF x jogos — AEL Limassol tabela [14, 8, 1, 5, 35, 17, 17] jogos [13, 7, 1, 5, 34, 18, 15]
- tabela da RSSSF x jogos — Aris Limassol tabela [14, 8, 0, 6, 37, 33, 16] jogos [13, 8, 0, 5, 36, 29, 16]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [14, 4, 1, 9, 23, 56, 9] jogos [14, 4, 1, 9, 21, 56, 9]
- tabela da RSSSF x jogos — Anorthosis tabela [14, 2, 1, 11, 14, 38, 5] jogos [11, 1, 1, 9, 14, 34, 3]
- tabela da RSSSF x jogos — EPA Larnaca tabela [14, 0, 2, 12, 8, 35, 2] jogos [8, 0, 2, 6, 8, 29, 2]
- os jogos da matriz não fecham com as tabelas publicadas em 8 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 4 posições (ex.: ['Enosis Neon Trust', 'Çetinkaya'])
- 48 jogos para 8 clubes (esperados 56)

### 1936/37

- tabela da Wikipédia x jogos — AEL Limassol tabela [12, 6, 2, 4, 39, 24, 14] jogos [12, 5, 2, 5, 36, 27, 12]
- tabela da Wikipédia x jogos — Anorthosis tabela [12, 2, 1, 9, 10, 51, 5] jogos [12, 3, 1, 8, 13, 48, 7]
- tabela da RSSSF x jogos — AEL Limassol tabela [12, 6, 2, 4, 39, 24, 14] jogos [12, 5, 2, 5, 36, 27, 12]
- tabela da RSSSF x jogos — Anorthosis tabela [12, 2, 1, 9, 10, 51, 5] jogos [12, 3, 1, 8, 13, 48, 7]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Olympiakos Nicosia', 'Anorthosis'])

### 1937/38

- tabela da RSSSF sem casar pelos números com a da Wikipédia (1 linhas iguais)
- tabela da Wikipédia x jogos — APOEL tabela [6, 5, 1, 0, 29, 11, 11] jogos [6, 5, 1, 0, 27, 11, 11]
- tabela da Wikipédia x jogos — Enosis Neon Trust tabela [4, 1, 3, 0, 7, 5, 5] jogos [3, 1, 2, 0, 6, 4, 4]
- tabela da Wikipédia x jogos — Çetinkaya tabela [4, 2, 1, 1, 8, 10, 5] jogos [5, 2, 2, 1, 9, 9, 6]
- os jogos da matriz não fecham com as tabelas publicadas em 3 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Enosis Neon Trust', 'Çetinkaya'])
- 12 jogos para 5 clubes (esperados 20)

### 1938/39

- tabela da Wikipédia x jogos — APOEL tabela [11, 9, 2, 0, 36, 11, 20] jogos [11, 9, 2, 0, 36, 12, 20]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [9, 2, 0, 7, 13, 42, 4] jogos [9, 2, 0, 7, 14, 42, 4]
- tabela da RSSSF x jogos — APOEL tabela [11, 9, 2, 0, 36, 11, 20] jogos [11, 9, 2, 0, 36, 12, 20]
- tabela da RSSSF x jogos — Çetinkaya tabela [8, 2, 1, 5, 12, 16, 5] jogos [9, 2, 1, 6, 12, 18, 5] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Pezoporikos Larnaca tabela [9, 2, 1, 6, 12, 18, 5] jogos [8, 2, 1, 5, 12, 16, 5] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [9, 2, 0, 7, 13, 42, 4] jogos [9, 2, 0, 7, 14, 42, 4]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Çetinkaya', 'Pezoporikos Larnaca'])
- 33 jogos para 7 clubes (esperados 42)

### 1939/40

- 29 jogos para 6 clubes (esperados 30)

### 1940/41

- tabela da Wikipédia x jogos — AEL Limassol tabela [7, 6, 0, 1, 43, 11, 12] jogos [7, 6, 0, 1, 41, 11, 12]
- tabela da Wikipédia x jogos — APOEL tabela [7, 6, 0, 1, 41, 8, 12] jogos [7, 6, 0, 1, 41, 5, 12]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [7, 2, 0, 5, 16, 50, 4] jogos [7, 2, 0, 5, 15, 50, 4]
- tabela da RSSSF x jogos — AEL Limassol tabela [7, 6, 0, 1, 43, 11, 12] jogos [7, 6, 0, 1, 41, 11, 12]
- tabela da RSSSF x jogos — APOEL tabela [7, 6, 0, 1, 41, 8, 12] jogos [7, 6, 0, 1, 41, 5, 12]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [7, 2, 0, 5, 16, 50, 4] jogos [7, 2, 0, 5, 15, 50, 4]
- os jogos da matriz não fecham com as tabelas publicadas em 3 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['AEL Limassol', 'APOEL'])
- 16 jogos para 5 clubes (esperados 20)

### 1944/45

- tabela da Wikipédia x jogos — APOEL tabela [10, 8, 1, 1, 40, 13, 17] jogos [10, 8, 1, 1, 41, 16, 17]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [10, 2, 2, 6, 19, 37, 6] jogos [10, 2, 2, 6, 22, 38, 6]
- tabela da RSSSF x jogos — APOEL tabela [10, 8, 1, 1, 40, 13, 17] jogos [10, 8, 1, 1, 41, 16, 17]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [10, 2, 2, 6, 19, 37, 6] jogos [10, 2, 2, 6, 22, 38, 6]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1945/46

- sem ocorrências

### 1946/47

- sem ocorrências

### 1947/48

- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [8, 4, 0, 4, 25, 23, 8] jogos [8, 4, 0, 4, 26, 22, 8]
- tabela da Wikipédia x jogos — AYMA Nicosia tabela [8, 2, 1, 5, 12, 26, 5] jogos [8, 2, 1, 5, 13, 27, 5]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [8, 4, 0, 4, 25, 23, 8] jogos [8, 4, 0, 4, 26, 22, 8]
- tabela da RSSSF x jogos — AYMA Nicosia tabela [8, 2, 1, 5, 14, 26, 5] jogos [8, 2, 1, 5, 13, 27, 5]
- os jogos da matriz não fecham com as tabelas publicadas em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1948/49

- tabela da Wikipédia x jogos — Anorthosis tabela [14, 10, 1, 3, 58, 26, 21] jogos [8, 5, 1, 2, 23, 16, 11]
- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [14, 9, 1, 4, 42, 40, 19] jogos [8, 4, 2, 2, 24, 22, 10]
- tabela da Wikipédia x jogos — AEL Limassol tabela [14, 5, 5, 4, 31, 25, 15] jogos [8, 1, 3, 4, 15, 16, 5]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [14, 4, 1, 9, 25, 36, 9] jogos [8, 3, 0, 5, 17, 27, 6]
- tabela da Wikipédia x jogos — AYMA Nicosia tabela [14, 2, 5, 7, 32, 36, 9] jogos [8, 1, 2, 5, 18, 22, 4]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [14, 2, 2, 10, 22, 41, 6] jogos [8, 1, 1, 6, 12, 23, 3]
- tabela da Wikipédia x jogos — Çetinkaya tabela [14, 2, 1, 11, 21, 58, 5] jogos [8, 1, 1, 6, 17, 31, 3]
- tabela da RSSSF x jogos — Anorthosis tabela [14, 10, 1, 3, 58, 26, 21] jogos [8, 5, 1, 2, 23, 16, 11]
- tabela da RSSSF x jogos — Pezoporikos Larnaca tabela [14, 8, 3, 3, 42, 40, 19] jogos [8, 4, 2, 2, 24, 22, 10]
- tabela da RSSSF x jogos — AEL Limassol tabela [14, 5, 5, 4, 31, 25, 15] jogos [8, 1, 3, 4, 15, 16, 5]
- tabela da RSSSF x jogos — EPA Larnaca tabela [14, 4, 1, 9, 25, 36, 9] jogos [8, 3, 0, 5, 17, 27, 6]
- tabela da RSSSF x jogos — AYMA Nicosia tabela [14, 2, 5, 7, 32, 36, 9] jogos [8, 1, 2, 5, 18, 22, 4]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [14, 2, 2, 10, 22, 41, 6] jogos [8, 1, 1, 6, 12, 23, 3]
- tabela da RSSSF x jogos — Çetinkaya tabela [14, 2, 1, 11, 21, 58, 5] jogos [8, 1, 1, 6, 17, 31, 3]
- os jogos da matriz não fecham com as tabelas publicadas em 6 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['AEL Limassol', 'EPA Larnaca'])
- 35 jogos para 8 clubes (esperados 56)

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- sem ocorrências

### 1952/53

- tabela da Wikipédia x jogos — AEL Limassol tabela [14, 11, 1, 2, 43, 23, 23] jogos [14, 11, 1, 2, 42, 21, 23]
- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [14, 9, 3, 2, 33, 16, 21] jogos [14, 10, 3, 1, 33, 14, 23]
- tabela da Wikipédia x jogos — APOEL tabela [14, 6, 5, 3, 33, 25, 17] jogos [14, 5, 5, 4, 31, 26, 15]
- tabela da RSSSF x jogos — AEL Limassol tabela [14, 11, 1, 2, 41, 23, 23] jogos [14, 11, 1, 2, 42, 21, 23]
- tabela da RSSSF x jogos — Pezoporikos Larnaca tabela [14, 9, 3, 2, 33, 14, 21] jogos [14, 10, 3, 1, 33, 14, 23]
- tabela da RSSSF x jogos — APOEL tabela [14, 6, 5, 3, 33, 25, 17] jogos [14, 5, 5, 4, 31, 26, 15]
- os jogos da matriz não fecham com as tabelas publicadas em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1953/54

- sem ocorrências

### 1954/55

- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [18, 10, 4, 4, 45, 19, 24] jogos [18, 11, 3, 4, 51, 19, 25]
- tabela da Wikipédia x jogos — APOEL tabela [18, 8, 7, 3, 37, 25, 23] jogos [18, 8, 6, 4, 37, 31, 22]
- tabela da Wikipédia x jogos — Omonia tabela [18, 7, 3, 8, 29, 27, 17] jogos [18, 7, 3, 8, 30, 27, 17]
- tabela da Wikipédia x jogos — Anorthosis tabela [18, 6, 4, 8, 35, 31, 16] jogos [18, 7, 3, 8, 41, 29, 17]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [18, 5, 1, 12, 24, 55, 11] jogos [18, 5, 0, 13, 22, 61, 10]
- tabela da Wikipédia x jogos — Aris Limassol tabela [18, 1, 4, 13, 15, 51, 6] jogos [18, 1, 4, 13, 15, 52, 6]
- os jogos da matriz não fecham com as tabelas publicadas em 6 clubes: a classificação final fica com os números publicados (observação na linha)

### 1955/56

- tabela da Wikipédia x jogos — AEL Limassol tabela [16, 9, 5, 2, 38, 17, 23] jogos [16, 9, 6, 1, 35, 15, 24]
- tabela da Wikipédia x jogos — APOEL tabela [16, 9, 3, 4, 30, 16, 21] jogos [16, 8, 3, 5, 28, 18, 19]
- tabela da Wikipédia x jogos — Omonia tabela [16, 7, 2, 7, 23, 26, 16] jogos [16, 7, 3, 6, 23, 21, 17]
- os jogos da matriz não fecham com as tabelas publicadas em 3 clubes: a classificação final fica com os números publicados (observação na linha)

### 1956/57

- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [16, 8, 5, 3, 40, 24, 21] jogos [16, 8, 5, 3, 40, 25, 21]
- tabela da Wikipédia x jogos — AEL Limassol tabela [16, 4, 4, 8, 18, 32, 12] jogos [16, 4, 4, 8, 19, 32, 12]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1957/58

- tabela da Wikipédia x jogos — Anorthosis tabela [17, 12, 3, 2, 55, 22, 27] jogos [17, 11, 4, 2, 55, 25, 26]
- tabela da Wikipédia x jogos — APOEL tabela [16, 5, 5, 6, 20, 23, 15] jogos [16, 7, 3, 6, 26, 27, 17]
- tabela da Wikipédia x jogos — Aris Limassol tabela [17, 5, 5, 7, 22, 32, 15] jogos [17, 5, 4, 8, 24, 35, 14]
- tabela da Wikipédia x jogos — Olympiakos Nicosia tabela [17, 1, 7, 9, 21, 35, 9] jogos [17, 1, 7, 9, 26, 38, 9]
- tabela da RSSSF x jogos — Anorthosis tabela [17, 12, 3, 2, 55, 22, 27] jogos [17, 11, 4, 2, 55, 25, 26]
- tabela da RSSSF x jogos — APOEL tabela [16, 5, 5, 6, 20, 23, 15] jogos [16, 7, 3, 6, 26, 27, 17]
- tabela da RSSSF x jogos — Aris Limassol tabela [17, 5, 5, 7, 22, 32, 15] jogos [17, 5, 4, 8, 24, 35, 14]
- tabela da RSSSF x jogos — Olympiakos Nicosia tabela [17, 1, 7, 9, 21, 35, 9] jogos [17, 1, 7, 9, 26, 38, 9]
- os jogos da matriz não fecham com as tabelas publicadas em 4 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 2 posições (ex.: ['Omonia', 'APOEL'])
- 85 jogos para 10 clubes (esperados 90)

### 1959/60

- tabela da Wikipédia x jogos — Omonia tabela [20, 13, 3, 4, 40, 20, 29] jogos [20, 14, 3, 3, 41, 19, 31]
- tabela da Wikipédia x jogos — AEL Limassol tabela [20, 6, 10, 4, 36, 36, 22] jogos [20, 7, 9, 4, 39, 37, 23]
- tabela da Wikipédia x jogos — Apollon Limassol tabela [20, 5, 8, 7, 39, 42, 18] jogos [20, 5, 7, 8, 45, 42, 17]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [20, 5, 4, 11, 31, 50, 14] jogos [20, 6, 1, 13, 34, 60, 13]
- tabela da Wikipédia x jogos — Aris Limassol tabela [20, 4, 4, 12, 27, 51, 12] jogos [20, 4, 3, 13, 27, 54, 11]
- tabela da RSSSF x jogos — Omonia tabela [20, 13, 3, 4, 40, 20, 29] jogos [20, 14, 3, 3, 41, 19, 31]
- tabela da RSSSF x jogos — Pezoporikos Larnaca tabela [20, 7, 9, 4, 39, 37, 23] jogos [20, 9, 4, 7, 40, 35, 22] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — AEL Limassol tabela [20, 9, 4, 7, 40, 35, 22] jogos [20, 7, 9, 4, 39, 37, 23]
- tabela da RSSSF x jogos — Apollon Limassol tabela [20, 5, 8, 7, 39, 42, 18] jogos [20, 5, 7, 8, 45, 42, 17]
- tabela da RSSSF x jogos — EPA Larnaca tabela [20, 5, 4, 11, 17, 32, 14] jogos [20, 6, 1, 13, 34, 60, 13]
- tabela da RSSSF x jogos — Orfeas Nicosia tabela [20, 5, 3, 12, 32, 53, 13] jogos [20, 5, 4, 11, 17, 32, 14] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Aris Limassol tabela [20, 4, 4, 12, 27, 51, 12] jogos [20, 4, 3, 13, 27, 54, 11]
- os jogos da matriz não fecham com as tabelas publicadas em 3 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 6 posições (ex.: ['Anorthosis', 'Omonia'])

### 1960/61

- sem ocorrências

### 1961/62

- sem ocorrências

### 1962/63

- sem ocorrências

### 1964/65

- sem ocorrências

### 1965/66

- tabela da Wikipédia x jogos — Anorthosis tabela [20, 8, 7, 5, 41, 31, 43] jogos [20, 8, 7, 5, 44, 32, 43]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [20, 6, 3, 11, 20, 33, 35] jogos [20, 6, 3, 11, 20, 32, 35]
- tabela da Wikipédia x jogos — Aris Limassol tabela [20, 2, 1, 17, 17, 73, 25] jogos [20, 2, 1, 17, 16, 75, 25]
- tabela da RSSSF x jogos — Anorthosis tabela [20, 8, 7, 5, 40, 30, 43] jogos [20, 8, 7, 5, 44, 32, 43]
- tabela da RSSSF x jogos — EPA Larnaca tabela [20, 6, 3, 11, 20, 33, 35] jogos [20, 6, 3, 11, 20, 32, 35]
- tabela da RSSSF x jogos — Aris Limassol tabela [20, 2, 1, 17, 17, 73, 25] jogos [20, 2, 1, 17, 16, 75, 25]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1966/67

- tabela da Wikipédia x jogos — Apollon Limassol tabela [22, 11, 6, 5, 50, 25, 50] jogos [22, 11, 6, 5, 50, 26, 50]
- tabela da Wikipédia x jogos — AEL Limassol tabela [22, 7, 5, 10, 41, 42, 41] jogos [22, 7, 5, 10, 40, 43, 41]
- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [22, 6, 4, 12, 40, 54, 38] jogos [22, 6, 4, 12, 41, 53, 38]
- tabela da Wikipédia x jogos — APOP Paphos tabela [22, 1, 2, 19, 21, 107, 26] jogos [22, 1, 2, 19, 22, 107, 26]
- tabela da RSSSF x jogos — Apollon Limassol tabela [22, 11, 6, 5, 50, 25, 50] jogos [22, 11, 6, 5, 50, 26, 50]
- tabela da RSSSF x jogos — AEL Limassol tabela [22, 7, 5, 10, 41, 42, 41] jogos [22, 7, 5, 10, 40, 43, 41]
- tabela da RSSSF x jogos — Pezoporikos Larnaca tabela [22, 6, 4, 12, 40, 54, 38] jogos [22, 6, 4, 12, 41, 53, 38]
- tabela da RSSSF x jogos — EPA Larnaca tabela [22, 6, 3, 13, 36, 53, 36] jogos [22, 6, 3, 13, 36, 53, 37] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — APOP Paphos tabela [22, 1, 2, 19, 21, 107, 26] jogos [22, 1, 2, 19, 22, 107, 26]
- os jogos da matriz não fecham com as tabelas publicadas em 4 clubes: a classificação final fica com os números publicados (observação na linha)

### 1967/68

- sem ocorrências

### 1968/69

- sem ocorrências

### 1969/70

- sem ocorrências

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- sem ocorrências

### 1974/75

- sem ocorrências

### 1975/76

- sem ocorrências

### 1976/77

- sem ocorrências

### 1977/78

- tabela da Wikipédia x jogos — Apollon Limassol tabela [30, 10, 10, 10, 40, 36, 30] jogos [30, 10, 9, 11, 39, 36, 29]
- tabela da Wikipédia x jogos — APOP Paphos tabela [30, 6, 10, 14, 22, 45, 22] jogos [30, 6, 11, 13, 23, 45, 23]
- tabela da RSSSF x jogos — Apollon Limassol tabela [30, 10, 10, 10, 40, 36, 30] jogos [30, 10, 9, 11, 39, 36, 29]
- tabela da RSSSF x jogos — APOP Paphos tabela [30, 6, 10, 14, 22, 45, 22] jogos [30, 6, 11, 13, 23, 45, 23]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1978/79

- tabela da Wikipédia x jogos — APOEL tabela [30, 20, 4, 6, 54, 18, 44] jogos None
- tabela da Wikipédia x jogos — Apollon Limassol tabela [30, 10, 10, 10, 25, 28, 30] jogos [60, 30, 14, 16, 79, 46, 74]
- tabela da RSSSF x jogos — APOEL tabela [30, 20, 4, 6, 54, 18, 44] jogos None
- tabela da RSSSF x jogos — Apollon Limassol tabela [30, 10, 10, 10, 25, 28, 30] jogos [60, 30, 14, 16, 79, 46, 74]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 11 posições (ex.: ['Omonia', 'APOEL'])

### 1979/80

- tabela da Wikipédia x jogos — Enosis Paralimni tabela [28, 8, 8, 12, 23, 26, 24] jogos [28, 8, 8, 12, 22, 27, 24]
- tabela da Wikipédia x jogos — APOP Paphos tabela [28, 5, 9, 14, 23, 53, 19] jogos [28, 5, 9, 14, 24, 52, 19]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1980/81

- tabela da Wikipédia x jogos — Apollon Limassol tabela [26, 10, 6, 10, 32, 32, 26] jogos [26, 10, 6, 10, 31, 32, 26]
- tabela da Wikipédia x jogos — Alki Larnaca tabela [26, 7, 7, 12, 25, 40, 21] jogos [26, 7, 7, 12, 26, 40, 21]
- os jogos da matriz não fecham com as tabelas publicadas em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1981/82

- sem ocorrências

### 1982/83

- tabela da Wikipédia x jogos — Anorthosis tabela [26, 12, 11, 3, 46, 21, 35] jogos [26, 13, 9, 4, 46, 21, 35]
- tabela da Wikipédia x jogos — Alki Larnaca tabela [26, 8, 11, 7, 32, 35, 27] jogos [26, 7, 12, 7, 31, 35, 26]
- tabela da Wikipédia x jogos — Enosis Paralimni tabela [26, 5, 13, 8, 35, 40, 23] jogos [26, 5, 14, 7, 35, 39, 24]
- os jogos da matriz não fecham com as tabelas publicadas em 3 clubes: a classificação final fica com os números publicados (observação na linha)

### 1983/84

- tabela da Wikipédia x jogos — AEL Limassol tabela [26, 9, 8, 9, 30, 26, 26] jogos [26, 9, 8, 9, 29, 25, 26]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [26, 6, 13, 7, 28, 31, 25] jogos [26, 6, 13, 7, 27, 30, 25]
- tabela da Wikipédia x jogos — Alki Larnaca tabela [26, 6, 10, 10, 26, 28, 22] jogos [26, 6, 10, 10, 26, 27, 22]
- tabela da Wikipédia x jogos — Omonia Aradippou tabela [26, 4, 8, 14, 23, 41, 16] jogos [26, 4, 8, 14, 22, 41, 16]
- os jogos da matriz não fecham com as tabelas publicadas em 4 clubes: a classificação final fica com os números publicados (observação na linha)

### 1984/85

- sem ocorrências

### 1985/86

- tabela da Wikipédia x jogos — Anorthosis tabela [26, 13, 6, 7, 36, 27, 32] jogos [26, 13, 6, 7, 36, 26, 32]
- tabela da Wikipédia x jogos — AEL Limassol tabela [26, 9, 6, 11, 27, 26, 24] jogos [26, 9, 6, 11, 28, 27, 24]
- tabela da Wikipédia x jogos — Enosis Paralimni tabela [26, 8, 7, 11, 33, 35, 23] jogos [26, 7, 8, 11, 33, 36, 22]
- tabela da Wikipédia x jogos — EPA Larnaca tabela [26, 6, 10, 10, 27, 35, 22] jogos [26, 6, 11, 9, 27, 35, 23]
- tabela da Wikipédia x jogos — APOP Paphos tabela [26, 6, 9, 11, 26, 44, 21] jogos [26, 5, 10, 11, 24, 44, 20]
- tabela da Wikipédia x jogos — Aris Limassol tabela [26, 5, 9, 12, 32, 42, 19] jogos [26, 5, 10, 11, 32, 40, 20]
- os jogos da matriz não fecham com as tabelas publicadas em 6 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Enosis Paralimni', 'EPA Larnaca'])

### 1986/87

- tabela da Wikipédia x jogos — Enosis Paralimni tabela [30, 9, 8, 13, 34, 53, 26] jogos [30, 10, 7, 13, 36, 54, 27]
- tabela da Wikipédia x jogos — Pezoporikos Larnaca tabela [30, 4, 16, 10, 25, 28, 24] jogos [30, 3, 17, 10, 23, 27, 23]
- tabela da Wikipédia x jogos — Nea Salamina tabela [30, 7, 10, 13, 45, 54, 24] jogos [30, 7, 9, 14, 46, 56, 23]
- tabela da Wikipédia x jogos — Omonia Aradippou tabela [30, 2, 9, 19, 21, 64, 13] jogos [30, 2, 10, 18, 20, 62, 14]
- os jogos da matriz não fecham com as tabelas publicadas em 4 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Pezoporikos Larnaca', 'Alki Larnaca'])

### 1987/88

- sem ocorrências

### 1988/89

- sem ocorrências

### 1989/90

- sem ocorrências

### 1990/91

- sem ocorrências

### 1991/92

- sem ocorrências

### 1992/93

- sem ocorrências

### 1993/94

- sem ocorrências

### 1994/95

- sem ocorrências

### 1995/96

- sem ocorrências

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- sem ocorrências

### 1999/00

- sem ocorrências

### 2000/01

- sem ocorrências

### 2001/02

- sem ocorrências

### 2002/03

- sem ocorrências

### 2003/04

- Anagennisi Deryneia x Onisilos Sotira (2004-01-10): fica 0-2 pela matriz da Wikipédia; o ogol dá 2-2, que fecha pior com as tabelas

### 2004/05

- 181 jogos para 14 clubes (esperados 182)

### 2005/06

- APEP x Omonia (2006-05-06): fica 0-5 pela matriz da Wikipédia; o ogol dá 0-3, que fecha pior com as tabelas

### 2006/07

- sem ocorrências

### 2007/08

- Apollon Limassol x APOEL (2008-02-02): fica 0-2 pela matriz da Wikipédia; o ogol dá 2-2, que fecha pior com as tabelas
- Apollon Limassol x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 2-2 pela matriz da Wikipédia, sem data
- Apollon Limassol x Enosis Paralimni (grupo intermediário): o ogol não tem o jogo; entra 4-1 pela matriz da Wikipédia, sem data
- Apollon Limassol x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 0-2 pela matriz da Wikipédia, sem data
- APOP Kinyras x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 1-2 pela matriz da Wikipédia, sem data
- APOP Kinyras x Enosis Paralimni (grupo intermediário): o ogol não tem o jogo; entra 3-4 pela matriz da Wikipédia, sem data
- APOP Kinyras x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 1-0 pela matriz da Wikipédia, sem data
- Enosis Paralimni x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 1-0 pela matriz da Wikipédia, sem data
- Enosis Paralimni x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 4-3 pela matriz da Wikipédia, sem data
- Enosis Paralimni x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- Ethnikos Achna x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- Ethnikos Achna x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 2-2 pela matriz da Wikipédia, sem data
- Ethnikos Achna x Enosis Paralimni (grupo intermediário): o ogol não tem o jogo; entra 4-3 pela matriz da Wikipédia, sem data
- Doxa Katokopias x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 0-0 pela matriz da Wikipédia, sem data
- Doxa Katokopias x AEL Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 1-2 pela matriz da Wikipédia, sem data
- Doxa Katokopias x Aris Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 2-0 pela matriz da Wikipédia, sem data
- Alki Larnaca x Doxa Katokopias (grupo de rebaixamento): o ogol não tem o jogo; entra 1-0 pela matriz da Wikipédia, sem data
- Alki Larnaca x AEL Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 2-1 pela matriz da Wikipédia, sem data
- Alki Larnaca x Aris Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 4-1 pela matriz da Wikipédia, sem data
- AEL Limassol x Doxa Katokopias (grupo de rebaixamento): o ogol não tem o jogo; entra 2-2 pela matriz da Wikipédia, sem data
- AEL Limassol x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 1-0 pela matriz da Wikipédia, sem data
- AEL Limassol x Aris Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 3-2 pela matriz da Wikipédia, sem data
- Aris Limassol x Doxa Katokopias (grupo de rebaixamento): o ogol não tem o jogo; entra 3-0 pela matriz da Wikipédia, sem data
- Aris Limassol x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 1-2 pela matriz da Wikipédia, sem data
- Aris Limassol x AEL Limassol (grupo de rebaixamento): o ogol não tem o jogo; entra 0-2 pela matriz da Wikipédia, sem data
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['AEL Limassol', 'Alki Larnaca'])

### 2008/09

- APOEL x Omonia: derrota para os dois (jogo da última rodada suspenso no intervalo pela violência das duas torcidas; a tabela da Wikipédia dá uma derrota a cada um, sem gols)
- Apollon Limassol x Doxa Katokopias (2008-12-07): fica 0-2, decidido fora de campo (nota da matriz da Wikipédia); o ogol dá 1-2
- Apollon Limassol x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 3-2 pela matriz da Wikipédia, sem data
- Apollon Limassol x Doxa Katokopias (grupo intermediário): o ogol não tem o jogo; entra 3-1 pela matriz da Wikipédia, sem data
- Apollon Limassol x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 2-0 pela matriz da Wikipédia, sem data
- APOP Kinyras x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 2-2 pela matriz da Wikipédia, sem data
- APOP Kinyras x Doxa Katokopias (grupo intermediário): o ogol não tem o jogo; entra 1-0 pela matriz da Wikipédia, sem data
- APOP Kinyras x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 1-4 pela matriz da Wikipédia, sem data
- Doxa Katokopias x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- Doxa Katokopias x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 3-2 pela matriz da Wikipédia, sem data
- Doxa Katokopias x Ethnikos Achna (grupo intermediário): o ogol não tem o jogo; entra 2-5 pela matriz da Wikipédia, sem data
- Ethnikos Achna x Apollon Limassol (grupo intermediário): o ogol não tem o jogo; entra 2-4 pela matriz da Wikipédia, sem data
- Ethnikos Achna x APOP Kinyras (grupo intermediário): o ogol não tem o jogo; entra 2-2 pela matriz da Wikipédia, sem data
- Ethnikos Achna x Doxa Katokopias (grupo intermediário): o ogol não tem o jogo; entra 0-2 pela matriz da Wikipédia, sem data
- AEP Paphos x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 3-4 pela matriz da Wikipédia, sem data
- AEP Paphos x APEP (grupo de rebaixamento): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- AEP Paphos x Enosis Paralimni (grupo de rebaixamento): o ogol não tem o jogo; entra 3-0 pela matriz da Wikipédia, sem data
- Alki Larnaca x AEP Paphos (grupo de rebaixamento): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- Alki Larnaca x APEP (grupo de rebaixamento): o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- Alki Larnaca x Enosis Paralimni (grupo de rebaixamento): o ogol não tem o jogo; entra 1-2 pela matriz da Wikipédia, sem data
- APEP x AEP Paphos (grupo de rebaixamento): o ogol não tem o jogo; entra 0-1 pela matriz da Wikipédia, sem data
- APEP x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 0-4 pela matriz da Wikipédia, sem data
- APEP x Enosis Paralimni (grupo de rebaixamento): o ogol não tem o jogo; entra 2-0 pela matriz da Wikipédia, sem data
- Enosis Paralimni x AEP Paphos (grupo de rebaixamento): o ogol não tem o jogo; entra 0-0 pela matriz da Wikipédia, sem data
- Enosis Paralimni x Alki Larnaca (grupo de rebaixamento): o ogol não tem o jogo; entra 2-1 pela matriz da Wikipédia, sem data
- Enosis Paralimni x APEP (grupo de rebaixamento): o ogol não tem o jogo; entra 0-1 pela matriz da Wikipédia, sem data

### 2009/10

- Nea Salamina x APOEL (2009-11-15): fica 0-3, decidido fora de campo (nota da matriz da Wikipédia); o ogol dá 0-1
- Anorthosis x Enosis Paralimni (2009-12-12): fica 2-0 pela matriz da Wikipédia; o ogol dá 1-0, que fecha pior com as tabelas
- placar diferente na matriz da Wikipédia — AEP Paphos x APOEL: ogol 0-0; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Anorthosis x APOEL: ogol 0-2, 1-1; Wikipédia 0-0, 1-1
- placar diferente na matriz da Wikipédia — APEP x APOEL: ogol 1-3; Wikipédia 1-4
- placar diferente na matriz da Wikipédia — APOEL x AEP Paphos: ogol 1-0; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — APOEL x Anorthosis: ogol 0-0, 1-0; Wikipédia 2-0, 1-0
- placar diferente na matriz da Wikipédia — APOEL x APEP: ogol 4-1; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — APOEL x Apollon Limassol: ogol 0-2, 3-2; Wikipédia 1-1, 3-2
- placar diferente na matriz da Wikipédia — Apollon Limassol x APOEL: ogol 1-1, 1-2; Wikipédia 2-0, 1-2

### 2010/11

- sem ocorrências

### 2011/12

- AEL Limassol x Apollon Limassol (2012-03-18): DA no ogol; fica 3-0 pela matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Enosis Paralimni', 'Ethnikos Achna'])

### 2012/13

- sem ocorrências

### 2013/14

- AEL Limassol x APOEL (2014-05-31): fica 0-3, decidido fora de campo (nota da matriz da Wikipédia); o ogol dá 0-1
- Ermis Aradippou x AEL Limassol (2014-05-03): fica 0-3, decidido fora de campo (nota da matriz da Wikipédia); o ogol dá 0-2

### 2014/15

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Ayia Napa', 'Othellos Athienou'])

### 2015/16

- Apollon Limassol x Anorthosis (2015-10-18): DA no ogol; fica 3-0 pela matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Doxa Katokopias', 'Aris Limassol'])

### 2016/17

- sem ocorrências

### 2017/18

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Ermis Aradippou', 'Doxa Katokopias'])

### 2018/19

- AEK Larnaca x Pafos FC (2019-01-02): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Anorthosis x Apollon Limassol (2019-02-02): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2020/21

- sem ocorrências

### 2021/22

- Ethnikos Achna x Omonia (2022-04-20): SUSP no ogol; fica 0-0 pela matriz da Wikipédia

### 2022/23

- 181 jogos para 14 clubes (esperados 182)

### 2023/24

- sem ocorrências

### 2024/25

- Apollon Limassol x AEL Limassol (2024-09-15): DA no ogol; fica 3-0 pela matriz da Wikipédia
- 28 jogos para 8 clubes (esperados 56)

### 2025/26

- placar diferente na matriz da Wikipédia — Aris Limassol x AEL Limassol: ogol 4-0; Wikipédia 4-1
- 28 jogos para 8 clubes (esperados 56)

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_cyp.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os redirecionamentos). O AEK Larnaca fica separado do EPA e do Pezoporikos; o AEP Paphos, do Evagoras e do APOP Paphos; o Lefkoşa Türk é o Çetinkaya; o "Trast" de 1934/35 é o Enosis Neon Trust. APOEL, AEL Limassol, EPA Larnaca e Olympiakos Nicosia têm o mesmo nome do gre-1 (os campeões cipriotas no Campeonato Grego).
- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Datas e rodadas até 1995/96** (só as matrizes).
- **Autores dos gols e cartões:** nenhuma fonte em lote cobre Chipre.
- **Jogos que faltam nas matrizes antigas** (temporadas dos anos 1930 e 1940).
