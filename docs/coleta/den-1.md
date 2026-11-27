# Campeonato Dinamarquês (1ª divisão) — coleta de dados

Gerado por `python coleta/den-1/importar.py`. Pacote em `data/coleta/den-1/pacote/`.

**Edições:** 112, de 1912/13 a 2025/26: os 112 títulos que a federação reconhece.

**Total:** 14016 jogos, 42946 gols, 11661 gols com autor, 12026 cartões, 72 clubes.

**Fontes:**
- Wikipédia (en): tabelas, matriz de resultados (base dos jogos de 1945/46 a 1990), mata-mata da Landsfodboldturneringen e do torneio da guerra;
- ogol (zerozero): base dos jogos desde 1991, com data, hora e rodada; calendários em `data/cache/ogol-den-1/`;
- RSSSF: tabelas de 1927 a 1998 (denhist.html; a única fonte de 1928/29), página de cada temporada desde 1995/96, lista de campeões e de artilheiros;
- football-data: placar e hora desde 2012/13;
- ESPN (liga `den.1`): estádio, público, gols e cartões desde 2006/07 (25 clubes casados por votação).

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; antes de 1945, a final e o mata-mata, depois a tabela; com grupos finais, o grupo do título, depois os outros). Pontos 2-1-0 até 1994/95 e 3-1-0 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 15 tabelas, saldo em 92, confronto direto em 2).

| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|
| 1912/13 | 11 | 5 | 27 | 0 | 0 / 0 | KB | — |
| 1913/14 | 11 | 6 | 27 | 0 | 0 / 0 | KB | — |
| 1915/16 | 10 | 5 | 34 | 0 | 0 / 0 | B.93 | — |
| 1916/17 | 10 | 5 | 23 | 0 | 0 / 0 | KB | — |
| 1917/18 | 10 | 4 | 16 | 0 | 0 / 0 | KB | — |
| 1918/19 | 11 | 4 | 17 | 0 | 0 / 0 | AB | — |
| 1919/20 | 11 | 4 | 13 | 0 | 0 / 0 | B 1903 | — |
| 1920/21 | 10 | 5 | 18 | 0 | 0 / 0 | AB | — |
| 1921/22 | 10 | 5 | 26 | 0 | 0 / 0 | KB | — |
| 1922/23 | 10 | 5 | 17 | 0 | 0 / 0 | Frem | — |
| 1923/24 | 11 | 7 | 30 | 0 | 0 / 0 | B 1903 | — |
| 1924/25 | 11 | 5 | 35 | 0 | 0 / 0 | KB | — |
| 1925/26 | 11 | 7 | 45 | 0 | 0 / 0 | B 1903 | — |
| 1926/27 | 6 | 5 | 28 | 0 | 0 / 0 | B.93 | — |
| 1928/29 | 25 | 0 | 0 | 0 | 0 / 0 | B.93 | — |
| 1929/30 | 10 | 0 | 0 | 0 | 0 / 0 | B.93 | — |
| 1930/31 | 10 | 0 | 0 | 0 | 0 / 0 | Frem | — |
| 1931/32 | 10 | 0 | 0 | 0 | 0 / 0 | KB | — |
| 1932/33 | 10 | 0 | 0 | 0 | 0 / 0 | Frem | — |
| 1933/34 | 10 | 0 | 0 | 0 | 0 / 0 | B.93 | — |
| 1934/35 | 10 | 0 | 0 | 0 | 0 / 0 | B.93 | — |
| 1935/36 | 10 | 0 | 0 | 0 | 0 / 0 | Frem | — |
| 1936/37 | 10 | 0 | 0 | 0 | 0 / 0 | AB | — |
| 1937/38 | 10 | 0 | 0 | 0 | 0 / 0 | B 1903 | — |
| 1938/39 | 10 | 0 | 0 | 0 | 0 / 0 | B.93 | — |
| 1939/40 | 10 | 0 | 0 | 0 | 0 / 0 | KB | — |
| 1940/41 | 22 | 7 | 36 | 0 | 0 / 0 | Frem | — |
| 1941/42 | 28 | 7 | 26 | 0 | 0 / 0 | B.93 | — |
| 1942/43 | 29 | 7 | 24 | 0 | 0 / 0 | AB | — |
| 1943/44 | 28 | 7 | 37 | 0 | 0 / 0 | Frem | — |
| 1944/45 | 29 | 15 | 62 | 0 | 0 / 0 | AB | — |
| 1945/46 | 10 | 90 | 357 | 0 | 2 / 0 | B.93 | — |
| 1946/47 | 10 | 90 | 403 | 0 | 2 / 0 | AB | — |
| 1947/48 | 10 | 90 | 405 | 0 | 2 / 0 | KB | — |
| 1948/49 | 10 | 90 | 341 | 0 | 2 / 0 | KB | — |
| 1949/50 | 10 | 90 | 300 | 0 | 2 / 0 | KB | — |
| 1950/51 | 10 | 90 | 268 | 0 | 2 / 0 | AB | — |
| 1951/52 | 10 | 90 | 301 | 0 | 0 / 2 | AB | — |
| 1952/53 | 10 | 90 | 350 | 0 | 2 / 0 | KB | — |
| 1953/54 | 10 | 90 | 303 | 0 | 2 / 0 | Køge | — |
| 1954/55 | 10 | 90 | 320 | 0 | 2 / 0 | AGF | — |
| 1955/56 | 10 | 90 | 332 | 0 | 2 / 0 | AGF | — |
| 1956/57 | 10 | 135 | 485 | 0 | 0 / 2 | AGF | — |
| 1958 | 12 | 132 | 537 | 0 | 2 / 0 | Vejle | — |
| 1959 | 12 | 132 | 487 | 0 | 2 / 0 | B 1909 | — |
| 1960 | 12 | 132 | 461 | 0 | 2 / 0 | AGF | — |
| 1961 | 12 | 132 | 484 | 0 | 2 / 0 | Esbjerg | — |
| 1962 | 12 | 132 | 483 | 0 | 2 / 0 | Esbjerg | — |
| 1963 | 12 | 132 | 526 | 0 | 2 / 0 | Esbjerg | — |
| 1964 | 12 | 132 | 484 | 0 | 2 / 0 | B 1909 | — |
| 1965 | 12 | 132 | 434 | 0 | 0 / 2 | Esbjerg | — |
| 1966 | 12 | 132 | 434 | 0 | 2 / 0 | Hvidovre | — |
| 1967 | 12 | 132 | 425 | 0 | 2 / 0 | AB | — |
| 1968 | 12 | 132 | 397 | 0 | 2 / 0 | KB | — |
| 1969 | 12 | 132 | 477 | 0 | 2 / 0 | B 1903 | — |
| 1970 | 12 | 132 | 400 | 0 | 2 / 0 | B 1903 | — |
| 1971 | 12 | 132 | 512 | 0 | 2 / 0 | Vejle | — |
| 1972 | 12 | 132 | 468 | 0 | 2 / 0 | Vejle | — |
| 1973 | 12 | 132 | 434 | 0 | 2 / 0 | Hvidovre | — |
| 1974 | 12 | 132 | 435 | 0 | 2 / 0 | KB | — |
| 1975 | 16 | 240 | 772 | 0 | 2 / 0 | Køge | — |
| 1976 | 16 | 240 | 710 | 0 | 2 / 0 | B 1903 | — |
| 1977 | 16 | 240 | 785 | 0 | 2 / 0 | OB | — |
| 1978 | 16 | 240 | 730 | 0 | 2 / 0 | Vejle | — |
| 1979 | 16 | 240 | 720 | 0 | 2 / 0 | Esbjerg | — |
| 1980 | 16 | 240 | 721 | 0 | 2 / 0 | KB | — |
| 1981 | 16 | 240 | 704 | 0 | 2 / 0 | Hvidovre | — |
| 1982 | 16 | 240 | 678 | 0 | 2 / 0 | OB | — |
| 1983 | 16 | 240 | 632 | 0 | 0 / 2 | Lyngby | — |
| 1984 | 16 | 240 | 671 | 0 | 2 / 0 | Vejle | — |
| 1985 | 16 | 240 | 694 | 0 | 2 / 0 | Brøndby | — |
| 1986 | 14 | 182 | 519 | 0 | 2 / 0 | AGF | — |
| 1987 | 14 | 182 | 535 | 0 | 2 / 0 | Brøndby | — |
| 1988 | 14 | 182 | 533 | 0 | 2 / 0 | Brøndby | — |
| 1989 | 14 | 182 | 488 | 0 | 2 / 0 | OB | — |
| 1990 | 14 | 182 | 455 | 0 | 2 / 0 | Brøndby | — |
| 1991 | 10 | 90 | 236 | 0 | 1 / 0 | Brøndby | — |
| 1991/92 | 10 | 146 | 417 | 0 | 0 / 2 | Lyngby | — |
| 1992/93 | 10 | 146 | 424 | 0 | 2 / 0 | Copenhague | — |
| 1993/94 | 10 | 146 | 436 | 0 | 2 / 0 | Silkeborg | — |
| 1994/95 | 10 | 146 | 465 | 0 | 2 / 0 | AaB | — |
| 1995/96 | 12 | 198 | 579 | 0 | 1 / 0 | Brøndby | — |
| 1996/97 | 12 | 198 | 609 | 0 | 1 / 0 | Brøndby | — |
| 1997/98 | 12 | 198 | 662 | 0 | 2 / 0 | Brøndby | — |
| 1998/99 | 12 | 198 | 626 | 0 | 1 / 0 | AaB | — |
| 1999/00 | 12 | 198 | 573 | 0 | 2 / 0 | Herfølge | — |
| 2000/01 | 12 | 198 | 589 | 275 | 1 / 0 | Copenhague | — |
| 2001/02 | 12 | 198 | 573 | 531 | 2 / 0 | Brøndby | — |
| 2002/03 | 12 | 198 | 620 | 548 | 2 / 0 | Copenhague | — |
| 2003/04 | 12 | 198 | 600 | 409 | 2 / 0 | Copenhague | AB -9 pontos |
| 2004/05 | 12 | 198 | 579 | 536 | 2 / 0 | Brøndby | — |
| 2005/06 | 12 | 198 | 554 | 546 | 1 / 1 | Copenhague | — |
| 2006/07 | 12 | 198 | 555 | 385 | 1 / 1 | Copenhague | — |
| 2007/08 | 12 | 198 | 543 | 476 | 1 / 1 | AaB | — |
| 2008/09 | 12 | 198 | 544 | 537 | 2 / 0 | Copenhague | — |
| 2009/10 | 12 | 198 | 515 | 501 | 2 / 0 | Copenhague | — |
| 2010/11 | 12 | 198 | 533 | 531 | 2 / 0 | Copenhague | — |
| 2011/12 | 12 | 198 | 540 | 0 | 1 / 0 | Nordsjælland | — |
| 2012/13 | 12 | 198 | 561 | 1 | 1 / 0 | Copenhague | — |
| 2013/14 | 12 | 198 | 543 | 1 | 2 / 0 | AaB | — |
| 2014/15 | 12 | 198 | 478 | 131 | 2 / 0 | Midtjylland | — |
| 2015/16 | 12 | 198 | 549 | 519 | 2 / 0 | Copenhague | — |
| 2016/17 | 14 | 251 | 665 | 467 | 5 / 0 | Copenhague | — |
| 2017/18 | 14 | 251 | 733 | 584 | 5 / 0 | Midtjylland | — |
| 2018/19 | 14 | 247 | 687 | 685 | 5 / 0 | Copenhague | — |
| 2019/20 | 14 | 243 | 678 | 671 | 5 / 0 | Midtjylland | — |
| 2020/21 | 12 | 193 | 559 | 555 | 4 / 0 | Brøndby | — |
| 2021/22 | 12 | 193 | 512 | 510 | 4 / 0 | Copenhague | — |
| 2022/23 | 12 | 193 | 529 | 529 | 4 / 0 | Copenhague | — |
| 2023/24 | 12 | 193 | 544 | 535 | 4 / 0 | Midtjylland | — |
| 2024/25 | 12 | 193 | 606 | 606 | 4 / 0 | Copenhague | — |
| 2025/26 | 12 | 193 | 599 | 592 | 4 / 0 | AGF | — |

## Conferência e ocorrências, temporada a temporada

### 1912/13

- sem ocorrências

### 1913/14

- sem ocorrências

### 1915/16

- sem ocorrências

### 1916/17

- sem ocorrências

### 1917/18

- sem ocorrências

### 1918/19

- sem ocorrências

### 1919/20

- sem ocorrências

### 1920/21

- sem ocorrências

### 1921/22

- sem ocorrências

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

- sem ocorrências

### 1941/42

- sem ocorrências

### 1942/43

- sem ocorrências

### 1943/44

- sem ocorrências

### 1944/45

- sem ocorrências

### 1945/46

- sem ocorrências

### 1946/47

- artilheiro sem um clube só na lista da RSSSF: Helge Bronee (Osterbros Boldklub)

### 1947/48

- sem ocorrências

### 1948/49

- sem ocorrências

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- tabela da Wikipédia x jogos — AB tabela [18, 11, 4, 3, 40, 21, 26] jogos [18, 11, 4, 3, 41, 21, 26]
- tabela da Wikipédia x jogos — Skovshoved tabela [18, 7, 4, 7, 36, 34, 18] jogos [18, 7, 4, 7, 36, 36, 18]
- tabela da Wikipédia x jogos — B 1903 tabela [18, 6, 4, 8, 26, 34, 16] jogos [18, 6, 4, 8, 27, 34, 16]
- tabela da RSSSF x jogos — AB tabela [18, 11, 4, 3, 40, 21, 26] jogos [18, 11, 4, 3, 41, 21, 26]
- tabela da RSSSF x jogos — Skovshoved tabela [18, 7, 4, 7, 36, 34, 18] jogos [18, 7, 4, 7, 36, 36, 18]
- tabela da RSSSF x jogos — B 1903 tabela [18, 6, 4, 8, 26, 34, 16] jogos [18, 6, 4, 8, 27, 34, 16]

### 1952/53

- sem ocorrências

### 1953/54

- sem ocorrências

### 1954/55

- sem ocorrências

### 1955/56

- sem ocorrências

### 1956/57

- tabela da Wikipédia x jogos — Frem tabela [27, 13, 6, 8, 61, 44, 32] jogos [28, 14, 6, 8, 64, 45, 34]
- tabela da Wikipédia x jogos — KB tabela [27, 9, 9, 9, 40, 48, 27] jogos [26, 8, 9, 9, 37, 47, 25]
- tabela da RSSSF x jogos — Frem tabela [27, 13, 6, 8, 61, 44, 32] jogos [28, 14, 6, 8, 64, 45, 34]
- tabela da RSSSF x jogos — KB tabela [27, 9, 9, 9, 40, 48, 27] jogos [26, 8, 9, 9, 37, 47, 25]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['KB', 'Esbjerg'])

### 1958

- sem ocorrências

### 1959

- sem ocorrências

### 1960

- sem ocorrências

### 1961

- sem ocorrências

### 1962

- sem ocorrências

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- tabela da Wikipédia x jogos — B 1909 tabela [22, 9, 2, 11, 36, 46, 20] jogos [22, 9, 2, 11, 37, 48, 20]
- tabela da Wikipédia x jogos — B 1913 tabela [22, 7, 5, 10, 31, 38, 19] jogos [22, 7, 5, 10, 33, 39, 19]
- tabela da RSSSF x jogos — B 1909 tabela [22, 9, 2, 11, 36, 46, 20] jogos [22, 9, 2, 11, 37, 48, 20]
- tabela da RSSSF x jogos — B 1913 tabela [22, 7, 5, 10, 31, 38, 19] jogos [22, 7, 5, 10, 33, 39, 19]

### 1966

- sem ocorrências

### 1967

- sem ocorrências

### 1968

- sem ocorrências

### 1969

- sem ocorrências

### 1970

- sem ocorrências

### 1971

- artilheiro sem um clube só na lista da RSSSF: John Nielsen (B 1901 Nykobing)

### 1972

- artilheiro sem um clube só na lista da RSSSF: John Nielsen (B 1901 Nykobing)

### 1973

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Nykøbing FC', 'Næstved'])

### 1974

- sem ocorrências

### 1975

- sem ocorrências

### 1976

- sem ocorrências

### 1977

- sem ocorrências

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- sem ocorrências

### 1981

- sem ocorrências

### 1982

- sem ocorrências

### 1983

- tabela da Wikipédia x jogos — Næstved tabela [30, 12, 7, 11, 48, 45, 31] jogos [30, 12, 7, 11, 48, 44, 31]
- tabela da Wikipédia x jogos — Vejle tabela [30, 11, 8, 11, 49, 40, 30] jogos [30, 11, 8, 11, 48, 40, 30]
- tabela da RSSSF x jogos — Næstved tabela [30, 12, 7, 11, 48, 45, 31] jogos [30, 12, 7, 11, 48, 44, 31]
- tabela da RSSSF x jogos — Vejle tabela [30, 11, 8, 11, 49, 40, 30] jogos [30, 11, 8, 11, 48, 40, 30]

### 1984

- sem ocorrências

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

### 1991/92

- tabela da Wikipédia x jogos — AaB tabela [18, 6, 7, 5, 30, 18, 19] jogos [18, 6, 7, 5, 29, 25, 19]
- tabela da Wikipédia x jogos — B 1903 tabela [14, 8, 2, 4, 32, 26, 29] jogos [14, 8, 2, 4, 23, 11, 29]
- tabela da Wikipédia x jogos — Næstved tabela [14, 2, 3, 9, 33, 34, 15] jogos [14, 2, 3, 9, 13, 33, 15]
- B 1903 não está na temporada seguinte, mas não caiu: fundiu-se com o KB e formou o FC København em 1992

### 1992/93

- placar diferente na matriz da Wikipédia — OB x Brøndby: ogol 0-0, 2-0; Wikipédia 2-1, 0-0

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

- RSSSF — Esbjerg x OB: ogol 2-0, 0-2, RSSSF 1-0
- RSSSF — AGF x Vejle: ogol 1-2, 2-0, RSSSF 3-2
- RSSSF — Copenhague x Silkeborg: ogol 4-1, RSSSF 2-0
- RSSSF — AB x Herfølge: ogol 2-2, 3-0, RSSSF 1-0
- RSSSF — AGF x Brøndby: ogol 0-2, RSSSF 0-1
- RSSSF — Copenhague x AB: ogol 1-2, RSSSF 1-1
- RSSSF — Esbjerg x AaB: ogol 0-0, 0-0, RSSSF 1-2
- RSSSF — Lyngby x Viborg: ogol 1-3, RSSSF 2-3
- RSSSF — Viborg x Brøndby: ogol 2-0, 2-2, RSSSF 1-0
- RSSSF — AaB x AB: ogol 2-2, 0-2, RSSSF 2-1
- ... e mais 3 diferenças com o RSSSF

### 2000/01

- tabela da RSSSF com outros clubes: ['AB', 'AGF', 'AaB', 'Brøndby', 'Copenhague', 'Herfølge', 'Lyngby', 'Midtjylland', 'None', 'OB', 'Silkeborg', 'Viborg']

### 2001/02

- RSSSF — Vejle x OB: ogol 1-1, RSSSF 1-2
- RSSSF — Brøndby x OB: ogol 2-0, 4-1, RSSSF 2-4
- RSSSF — Midtjylland x AaB: ogol 0-1, RSSSF 1-1
- RSSSF — AGF x Esbjerg: ogol 1-6, RSSSF 1-2
- RSSSF — OB x AaB: ogol 0-2, 1-2, RSSSF 1-1
- RSSSF — Esbjerg x AB: ogol 1-2, RSSSF 1-0
- RSSSF — Copenhague x Esbjerg: ogol 6-0, RSSSF 1-0
- RSSSF — Esbjerg x Copenhague: ogol 2-1, 1-3, RSSSF 0-0
- RSSSF — Copenhague x OB: ogol 1-1, 4-0, RSSSF 1-2

### 2002/03

- sem ocorrências

### 2003/04

- RSSSF — Midtjylland x Frem: ogol 4-1, 3-3, RSSSF 0-1
- RSSSF — AB x Viborg: ogol 1-4, 0-3, RSSSF 0-1
- RSSSF — Esbjerg x AaB: ogol 3-2, 4-2, RSSSF 1-2
- RSSSF — Brøndby x AaB: ogol 1-1, 4-0, RSSSF 0-0
- RSSSF — Copenhague x OB: ogol 2-4, 2-2, RSSSF 3-1
- RSSSF — AaB x Brøndby: ogol 1-1, RSSSF 2-1
- RSSSF — OB x Copenhague: ogol 0-4, RSSSF 2-4

### 2004/05

- sem ocorrências

### 2005/06

- tabela da Wikipédia x jogos — Brøndby tabela [33, 21, 4, 8, 60, 32, 67] jogos [33, 21, 4, 8, 60, 34, 67] (a tabela da RSSSF fecha com os jogos)
- tabela da Wikipédia x jogos — Silkeborg tabela [33, 11, 6, 16, 33, 51, 39] jogos [33, 11, 6, 16, 33, 50, 39] (a tabela da RSSSF fecha com os jogos)

### 2006/07

- Esbjerg x Silkeborg (2007-04-22): fica 0-3 (1-2 no campo; dado como 0-3 porque o Esbjerg escalou um jogador irregular (nota da Wikipédia; a ESPN e as tabelas dão 0-3))
- tabela da Wikipédia x jogos — OB tabela [33, 17, 7, 9, 45, 36, 58] jogos [33, 17, 7, 9, 46, 36, 58] (a tabela da RSSSF fecha com os jogos)
- tabela da Wikipédia x jogos — Nordsjælland tabela [33, 16, 9, 8, 68, 40, 57] jogos [33, 16, 9, 8, 67, 39, 57] (a tabela da RSSSF fecha com os jogos)

### 2007/08

- tabela da RSSSF x jogos — Copenhague tabela [33, 17, 9, 7, 51, 29, 57] jogos [33, 17, 9, 7, 51, 29, 60] (a tabela da Wikipédia fecha com os jogos)

### 2008/09

- placar diferente na matriz da Wikipédia — Nordsjælland x SønderjyskE: ogol 0-0, 0-1; Wikipédia 0-2, 0-0
- placar diferente na matriz da Wikipédia — SønderjyskE x Midtjylland: ogol 1-1, 1-1; Wikipédia 1-1, 0-0
- placar diferente na matriz da Wikipédia — AGF x Copenhague: ogol 1-0; Wikipédia 0-1

### 2009/10

- sem ocorrências

### 2010/11

- sem ocorrências

### 2011/12

- tabela da RSSSF com outros clubes: ['AC Horsens', 'AaB', 'Brøndby', 'Copenhague', 'HB Køge', 'Lyngby', 'Midtjylland', 'Nordsjælland', 'OB', 'Silkeborg', 'SønderjyskE']

### 2012/13

- tabela da RSSSF com outros clubes: ['AC Horsens', 'AaB', 'Brøndby', 'Copenhague', 'Esbjerg', 'Midtjylland', 'Nordsjælland', 'OB', 'Randers', 'Silkeborg', 'SønderjyskE']
- placar diferente na matriz da Wikipédia — AaB x Randers: ogol 2-2, 4-0; Wikipédia 4-0, 1-1

### 2013/14

- Esbjerg x Randers (2014-04-17): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Viborg x AGF (2014-04-27): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2014/15

- placar diferente na matriz da Wikipédia — Brøndby x Hobro: ogol 0-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Nordsjælland x AaB: ogol 0-1; Wikipédia 1-0
- placar diferente na ESPN — SønderjyskE x OB (2014-11-09): 2-1, ESPN 1-0
- artilheiro sem um clube só na lista da RSSSF: Martin Pusic (Esbjerg/Midtjylland)

### 2015/16

- placar diferente na ESPN — Hobro x AGF (2015-09-11): 0-3, ESPN 2-1
- placar diferente na ESPN — Hobro x AGF (2015-10-23): 3-1, ESPN 3-0
- placar diferente na ESPN — Nordsjælland x AGF (2016-05-21): 3-3, ESPN 2-0

### 2016/17

- Viborg x AC Horsens (2017-05-12): o ogol não tem o jogo; entra 3-0 pelo football-data
- Esbjerg x AGF (2017-05-14): o ogol não tem o jogo; entra 0-0 pelo football-data
- AC Horsens x Viborg (2017-05-16): o ogol não tem o jogo; entra 1-0 pelo football-data
- AGF x Esbjerg (2017-05-17): o ogol não tem o jogo; entra 3-1 pelo football-data
- Esbjerg x AC Horsens (2017-05-20): o ogol não tem o jogo; entra 1-1 pelo football-data
- Viborg x AGF (2017-05-22): o ogol não tem o jogo; entra 2-2 pelo football-data
- AC Horsens x Esbjerg (2017-05-28): o ogol não tem o jogo; entra 3-2 pelo football-data
- AGF x Viborg (2017-05-28): o ogol não tem o jogo; entra 1-0 pelo football-data
- AC Horsens x Vendsyssel (2017-05-31): o ogol não tem o jogo; entra 0-0 pelo football-data
- Helsingør x Viborg (2017-05-31): o ogol não tem o jogo; entra 1-1 pelo football-data
- Vendsyssel x AC Horsens (2017-06-04): o ogol não tem o jogo; entra 1-3 pelo football-data
- Viborg x Helsingør (2017-06-04): o ogol não tem o jogo; entra 1-1 pelo football-data
- jogo com clube de fora da liga (acesso e rebaixamento), fora do pacote: AC Horsens x Vendsyssel (2017-05-31, )
- jogo com clube de fora da liga (acesso e rebaixamento), fora do pacote: Helsingør x Viborg (2017-05-31, )
- jogo com clube de fora da liga (acesso e rebaixamento), fora do pacote: Vendsyssel x AC Horsens (2017-06-04, )
- jogo com clube de fora da liga (acesso e rebaixamento), fora do pacote: Viborg x Helsingør (2017-06-04, )

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- placar diferente na matriz da Wikipédia — Hobro x Lyngby: ogol 1-2, 2-2; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — AC Horsens x Brøndby: ogol 3-2; Wikipédia 2-2
- artilheiro sem um clube só na lista da RSSSF: Ronnie Schwartz (Silkeborg/Midtjylland)

### 2020/21

- football-data — AGF x AaB (2021-05-28): ogol 3-0, 2-2, football-data 1-1

### 2021/22

- placar diferente na matriz da Wikipédia — Viborg x SønderjyskE: ogol 1-1, 2-1; Wikipédia 1-1, 1-0

### 2022/23

- sem ocorrências

### 2023/24

- sem ocorrências

### 2024/25

- placar diferente na matriz da Wikipédia — Silkeborg x Viborg: ogol 1-2, 3-2; Wikipédia 3-3, 1-2
- placar diferente na matriz da Wikipédia — SønderjyskE x Viborg: ogol 2-2, 2-2; Wikipédia 3-3, 2-2

### 2025/26

- jogos da página da RSSSF fora da conferência: só 2 de 15 batem com o ogol (a página mistura outras competições ou a leitura falhou)
- placar diferente na matriz da Wikipédia — Brøndby x Copenhague: ogol 1-3, 2-1; Wikipédia 1-0

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_den.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os redirecionamentos). Pelos links, são o mesmo clube: Horsens fS e AC Horsens; Farum BK e FC Nordsjælland; Haderslev FK e SønderjyskE; B 1901 e Nykøbing FC; Helsingør IF e FC Helsingør. KB, B 1903 e FC København (a fusão de 1992) ficam separados, como na lista de campeões da RSSSF.
- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Jogos das ligas de Copenhague (até 1927), da liga de 1928/29 a 1939/40 e das séries da guerra:** nenhuma fonte em lote traz (só as tabelas); o banco Haslund não é baixável em lote.
- **Datas e rodadas até 1990** (só as matrizes e as listas do mata-mata).
- **Autores dos gols e cartões** antes da ESPN (2006/07), fora as páginas da RSSSF.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.
