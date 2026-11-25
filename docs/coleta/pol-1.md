# Campeonato Polonês (1ª divisão) — coleta de dados

Gerado por `python coleta/pol-1/importar.py`. Pacote em `data/coleta/pol-1/pacote/`.

**Edições:** 98, de 1921 a 2025/26: os 98 títulos que a federação reconhece (torneios entre os campeões regionais em 1921-1926, 1946 e 1947; liga de 1927 a 1938 e desde 1948; 1962 só com a primavera).

**Total:** 19667 jogos, 53027 gols, 103 clubes. Sem autores dos gols, cartões e público.

**Fontes:**
- RSSSF (polhist.html): matriz dos torneios (base dos jogos de 1921-1926, 1946 e 1947), tabela e matriz de cada temporada até 2000/01 (conferência), final de 1922 e play-offs de 1962; lista de campeões e de artilheiros;
- Wikipédia (en): tabela de cada fase (ordem oficial, punições, bônus), matriz de resultados (base dos jogos de 1927 a 1962, conferência depois), fichas das finais de 1923, do desempate de 1925 e do mata-mata de 1946;
- ogol (zerozero): base dos jogos desde 1962/63, com data, hora e rodada; calendários em `data/cache/ogol-pol-1/`;
- football-data: conferência dos placares desde 2012/13.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; nos torneios, o grupo final ou a final e depois a posição no grupo; em 1962, os play-offs de classificação). Pontos 2-1-0 até 1994/95 e 3-1-0 depois; bônus de 1986/87 a 1989/90 e pontos da fase regular divididos por dois de 2013/14 a 2019/20, em `ajuste_pontos`. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (em 1938, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 47 fases, saldo em 37, confronto direto em 46).

| Temporada | Clubes | Jogos | Gols | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|
| 1921 | 5 | 20 | 84 | 2 / 0 | Cracovia | — |
| 1922 | 8 | 26 | 154 | 0 / 4 | Pogoń Lwów | — |
| 1923 | 8 | 27 | 137 | 0 / 4 | Pogoń Lwów | — |
| 1925 | 9 | 25 | 90 | 8 / 0 | Pogoń Lwów | — |
| 1926 | 9 | 18 | 113 | 4 / 2 | Pogoń Lwów | — |
| 1927 | 14 | 182 | 827 | 0 / 2 | Wisła Cracóvia | — |
| 1928 | 15 | 210 | 852 | 1 / 1 | Wisła Cracóvia | — |
| 1929 | 13 | 156 | 608 | 1 / 1 | Warta Poznań | — |
| 1930 | 12 | 132 | 508 | 1 / 1 | Cracovia | — |
| 1931 | 12 | 132 | 511 | 1 / 1 | Garbarnia Cracóvia | — |
| 1932 | 12 | 132 | 452 | 2 / 0 | Cracovia | — |
| 1933 | 12 | 120 | 415 | 6 / 2 | Ruch Chorzów | — |
| 1934 | 12 | 132 | 508 | 0 / 2 | Ruch Chorzów | — |
| 1935 | 11 | 110 | 407 | 0 / 2 | Ruch Chorzów | — |
| 1936 | 10 | 90 | 332 | 1 / 1 | Ruch Chorzów | — |
| 1937 | 9 | 72 | 271 | 0 / 2 | Cracovia | — |
| 1938 | 10 | 90 | 386 | 0 / 2 | Ruch Chorzów | — |
| 1946 | 18 | 26 | 153 | 2 / 0 | Polonia Varsóvia | — |
| 1947 | 28 | 240 | 1302 | 5 / 3 | Warta Poznań | — |
| 1948 | 14 | 183 | 735 | 2 / 0 | Cracovia | — |
| 1949 | 12 | 132 | 498 | 0 / 2 | Wisła Cracóvia | — |
| 1950 | 12 | 132 | 453 | 2 / 0 | Wisła Cracóvia | — |
| 1951 | 12 | 132 | 387 | 2 / 0 | Ruch Chorzów | — |
| 1952 | 12 | 62 | 184 | 4 / 0 | Ruch Chorzów | — |
| 1953 | 12 | 132 | 370 | 0 / 2 | Ruch Chorzów | — |
| 1954 | 11 | 110 | 264 | 2 / 0 | Polonia Bytom | — |
| 1955 | 12 | 132 | 332 | 2 / 0 | Legia Varsóvia | — |
| 1956 | 12 | 132 | 394 | 0 / 2 | Legia Varsóvia | — |
| 1957 | 12 | 132 | 454 | 0 / 2 | Górnik Zabrze | — |
| 1958 | 12 | 132 | 472 | 0 / 2 | ŁKS Łódź | — |
| 1959 | 12 | 132 | 400 | 2 / 0 | Górnik Zabrze | — |
| 1960 | 12 | 132 | 420 | 0 / 2 | Ruch Chorzów | — |
| 1961 | 14 | 182 | 568 | 1 / 1 | Górnik Zabrze | — |
| 1962 | 14 | 98 | 274 | 4 / 0 | Polonia Bytom | — |
| 1962/63 | 14 | 182 | 516 | 2 / 0 | Górnik Zabrze | — |
| 1963/64 | 14 | 182 | 546 | 0 / 2 | Górnik Zabrze | — |
| 1964/65 | 14 | 182 | 560 | 2 / 0 | Górnik Zabrze | — |
| 1965/66 | 14 | 182 | 489 | 2 / 0 | Górnik Zabrze | — |
| 1966/67 | 14 | 182 | 444 | 2 / 0 | Górnik Zabrze | — |
| 1967/68 | 14 | 182 | 430 | 2 / 0 | Ruch Chorzów | — |
| 1968/69 | 14 | 182 | 410 | 0 / 2 | Legia Varsóvia | — |
| 1969/70 | 14 | 182 | 382 | 2 / 0 | Legia Varsóvia | — |
| 1970/71 | 14 | 182 | 395 | 2 / 0 | Górnik Zabrze | — |
| 1971/72 | 14 | 182 | 402 | 2 / 0 | Górnik Zabrze | — |
| 1972/73 | 14 | 182 | 373 | 1 / 1 | Stal Mielec | — |
| 1973/74 | 16 | 240 | 476 | 2 / 0 | Ruch Chorzów | — |
| 1974/75 | 16 | 240 | 569 | 1 / 1 | Ruch Chorzów | — |
| 1975/76 | 16 | 240 | 560 | 2 / 0 | Stal Mielec | — |
| 1976/77 | 16 | 240 | 578 | 2 / 0 | Śląsk Wrocław | — |
| 1977/78 | 16 | 240 | 510 | 2 / 0 | Wisła Cracóvia | — |
| 1978/79 | 16 | 240 | 524 | 1 / 1 | Ruch Chorzów | — |
| 1979/80 | 16 | 240 | 587 | 2 / 0 | Szombierki Bytom | — |
| 1980/81 | 16 | 240 | 549 | 2 / 0 | Widzew Łódź | — |
| 1981/82 | 16 | 240 | 533 | 2 / 0 | Widzew Łódź | — |
| 1982/83 | 16 | 240 | 550 | 2 / 0 | Lech Poznań | — |
| 1983/84 | 16 | 240 | 548 | 2 / 0 | Lech Poznań | — |
| 1984/85 | 16 | 240 | 485 | 1 / 1 | Górnik Zabrze | — |
| 1985/86 | 16 | 240 | 597 | 0 / 2 | Górnik Zabrze | — |
| 1986/87 | 16 | 240 | 539 | 0 / 1 | Górnik Zabrze | — |
| 1987/88 | 16 | 240 | 515 | 0 / 1 | Górnik Zabrze | — |
| 1988/89 | 16 | 240 | 566 | 0 / 1 | Ruch Chorzów | — |
| 1989/90 | 16 | 240 | 484 | 0 / 1 | Lech Poznań | — |
| 1990/91 | 16 | 240 | 578 | 0 / 2 | Zagłębie Lubin | — |
| 1991/92 | 18 | 306 | 678 | 0 / 2 | Lech Poznań | — |
| 1992/93 | 18 | 304 | 792 | 0 / 2 | Lech Poznań | — |
| 1993/94 | 18 | 306 | 716 | 0 / 2 | Legia Varsóvia | Legia Varsóvia -3 pontos; ŁKS Łódź -3 pontos; Wisła Cracóvia -3 pontos |
| 1994/95 | 18 | 306 | 735 | 0 / 2 | Legia Varsóvia | — |
| 1995/96 | 18 | 306 | 775 | 1 / 1 | Widzew Łódź | — |
| 1996/97 | 18 | 306 | 764 | 2 / 0 | Widzew Łódź | — |
| 1997/98 | 18 | 306 | 730 | 2 / 0 | ŁKS Łódź | — |
| 1998/99 | 16 | 240 | 608 | 2 / 0 | Wisła Cracóvia | — |
| 1999/00 | 16 | 240 | 675 | 0 / 2 | Polonia Varsóvia | — |
| 2000/01 | 16 | 240 | 615 | 0 / 1 | Wisła Cracóvia | — |
| 2001/02 | 16 | 224 | 562 | 4 / 0 | Legia Varsóvia | — |
| 2002/03 | 16 | 240 | 647 | 0 / 1 | Wisła Cracóvia | — |
| 2003/04 | 14 | 182 | 500 | 0 / 1 | Wisła Cracóvia | — |
| 2004/05 | 14 | 182 | 498 | 1 / 0 | Wisła Cracóvia | — |
| 2005/06 | 16 | 240 | 557 | 1 / 0 | Legia Varsóvia | — |
| 2006/07 | 16 | 240 | 624 | 1 / 0 | Zagłębie Lubin | — |
| 2007/08 | 16 | 240 | 577 | 1 / 0 | Wisła Cracóvia | — |
| 2008/09 | 16 | 240 | 524 | 1 / 0 | Wisła Cracóvia | — |
| 2009/10 | 16 | 240 | 532 | 1 / 0 | Lech Poznań | Jagiellonia Białystok -10 pontos |
| 2010/11 | 16 | 240 | 578 | 0 / 1 | Wisła Cracóvia | — |
| 2011/12 | 16 | 240 | 527 | 1 / 0 | Śląsk Wrocław | — |
| 2012/13 | 16 | 240 | 598 | 1 / 0 | Legia Varsóvia | Zagłębie Lubin -3 pontos |
| 2013/14 | 16 | 296 | 786 | 3 / 0 | Legia Varsóvia | — |
| 2014/15 | 16 | 296 | 790 | 3 / 0 | Lech Poznań | — |
| 2015/16 | 16 | 296 | 778 | 3 / 0 | Legia Varsóvia | — |
| 2016/17 | 16 | 296 | 812 | 3 / 0 | Legia Varsóvia | — |
| 2017/18 | 16 | 296 | 781 | 3 / 0 | Legia Varsóvia | — |
| 2018/19 | 16 | 296 | 823 | 3 / 0 | Piast Gliwice | — |
| 2019/20 | 16 | 296 | 767 | 3 / 0 | Legia Varsóvia | — |
| 2020/21 | 16 | 240 | 589 | 1 / 0 | Legia Varsóvia | Cracovia -5 pontos |
| 2021/22 | 18 | 306 | 818 | 1 / 0 | Lech Poznań | — |
| 2022/23 | 18 | 306 | 758 | 1 / 0 | Raków Częstochowa | — |
| 2023/24 | 18 | 306 | 823 | 1 / 0 | Jagiellonia Białystok | — |
| 2024/25 | 18 | 306 | 843 | 1 / 0 | Lech Poznań | — |
| 2025/26 | 18 | 306 | 837 | 1 / 0 | Lech Poznań | Lechia Gdańsk -5 pontos |

## Conferência e ocorrências, temporada a temporada

### 1921

- sem ocorrências

### 1922

- a Wikipédia polonesa dá Warta 23:6, Pogoń 37:6 e Ruch 6:38 (gols), como os jogos; a Wikipédia em inglês e a RSSSF dão 33:6, 37:8 e 8:38 (https://pl.wikipedia.org/wiki/Mistrzostwa_Polski_w_piłce_nożnej_(1922))
- Grupo Sul: a matriz da RSSSF está trocada com a do outro grupo (a nota dela sobre Ruch x Cracovia, 2-8 e 0-7, está na matriz do outro grupo); os jogos vêm da matriz certa, linha a linha pela posição; com isso, os números fecham com as tabelas da Wikipédia polonesa
- Grupo Norte: a matriz da RSSSF está trocada com a do outro grupo (a nota dela sobre Ruch x Cracovia, 2-8 e 0-7, está na matriz do outro grupo); os jogos vêm da matriz certa, linha a linha pela posição; com isso, os números fecham com as tabelas da Wikipédia polonesa
- tabela (Grupo Sul) da Wikipédia x jogos — Pogoń Lwów tabela [6, 5, 0, 1, 37, 8, 10] jogos [6, 5, 0, 1, 37, 6, 10]
- tabela (Grupo Sul) da Wikipédia x jogos — Ruch Chorzów tabela [6, 1, 0, 5, 8, 38, 2] jogos [6, 1, 0, 5, 6, 38, 2]
- tabela (Grupo Sul) da RSSSF x jogos — Pogoń Lwów tabela [6, 5, 0, 1, 37, 8, 10] jogos [6, 5, 0, 1, 37, 6, 10]
- tabela (Grupo Sul) da RSSSF x jogos — Ruch Chorzów tabela [6, 1, 0, 5, 8, 38, 2] jogos [6, 1, 0, 5, 6, 38, 2]
- tabela (Grupo Norte) da Wikipédia x jogos — Warta Poznań tabela [6, 6, 0, 0, 33, 6, 12] jogos [6, 6, 0, 0, 23, 6, 12]
- tabela (Grupo Norte) da RSSSF x jogos — Warta Poznań tabela [6, 6, 0, 0, 33, 6, 12] jogos [6, 6, 0, 0, 23, 6, 12]

### 1923

- tabela (Grupo Oeste) da Wikipédia x jogos — ŁKS Łódź tabela [6, 3, 1, 2, 21, 11, 7] jogos [6, 3, 1, 2, 17, 10, 7]
- tabela (Grupo Oeste) da Wikipédia x jogos — Iskra Siemianowice tabela [6, 0, 0, 6, 1, 36, 0] jogos [6, 0, 0, 6, 0, 32, 0]
- tabela (Grupo Oeste) da RSSSF x jogos — Warta Poznań tabela [6, 3, 2, 1, 20, 9, 6] jogos [6, 3, 2, 1, 20, 9, 8] (a tabela da Wikipédia fecha com os jogos)
- tabela (Grupo Oeste) da RSSSF x jogos — ŁKS Łódź tabela [6, 3, 1, 2, 21, 11, 0] jogos [6, 3, 1, 2, 17, 10, 7]
- tabela (Grupo Oeste) da RSSSF x jogos — Iskra Siemianowice tabela [6, 0, 0, 6, 1, 36, 0] jogos [6, 0, 0, 6, 0, 32, 0]
- tabela (Grupo Leste) da Wikipédia x jogos — Lublinianka tabela [6, 0, 1, 5, 1, 39, 1] jogos [6, 0, 1, 5, 1, 30, 1]
- tabela (Grupo Leste) da RSSSF x jogos — Lublinianka tabela [6, 0, 1, 5, 1, 39, 1] jogos [6, 0, 1, 5, 1, 30, 1]

### 1925

- sem ocorrências

### 1926

- tabela (Grupo Oeste) da Wikipédia x jogos — Turyści Łódź tabela [4, 1, 0, 3, 5, 10, 2] jogos [4, 1, 1, 2, 6, 10, 3]
- tabela (Grupo Oeste) da Wikipédia x jogos — Ruch Chorzów tabela [4, 1, 0, 3, 4, 13, 2] jogos [4, 0, 1, 3, 4, 14, 1]
- tabela (Grupo Oeste) da RSSSF x jogos — Turyści Łódź tabela [4, 1, 0, 3, 5, 10, 2] jogos [4, 1, 1, 2, 6, 10, 3]
- tabela (Grupo Oeste) da RSSSF x jogos — Ruch Chorzów tabela [4, 1, 0, 3, 4, 13, 2] jogos [4, 0, 1, 3, 4, 14, 1]
- Grupo final: sem os jogos em nenhuma fonte (RSSSF, Wikipédia em inglês e em polonês); fica a tabela publicada

### 1927

- Legia Varsóvia x Polonia Varsóvia: a matriz da RSSSF dá 1-2; fica 2-2 (Wikipédia), que fecha melhor ou igual com as tabelas
- Polonia Varsóvia x Legia Varsóvia: a matriz da RSSSF dá 2-2; fica 2-1 (Wikipédia), que fecha melhor ou igual com as tabelas
- tabela da Wikipédia x jogos — TKS Toruń tabela [26, 10, 4, 12, 56, 86, 24] jogos [26, 11, 2, 13, 56, 86, 24]
- tabela da RSSSF x jogos — Pogoń Lwów tabela [26, 13, 3, 10, 85, 42, 29] jogos [26, 13, 3, 10, 65, 42, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Legia Varsóvia tabela [26, 12, 3, 11, 60, 75, 27] jogos [26, 12, 3, 11, 70, 65, 27] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [26, 9, 7, 10, 54, 51, 25] jogos [26, 11, 3, 12, 54, 51, 25] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Polonia Varsóvia tabela [26, 11, 3, 12, 61, 66, 25] jogos [26, 9, 7, 10, 61, 68, 25] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Czarni Lwów tabela [26, 11, 2, 13, 45, 50, 24] jogos [26, 10, 4, 12, 45, 50, 24] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — TKS Toruń tabela [26, 10, 4, 12, 56, 86, 24] jogos [26, 11, 2, 13, 56, 86, 24]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1928

- tabela da RSSSF x jogos — Warta Poznań tabela [28, 16, 8, 4, 83, 39, 40] jogos [28, 16, 8, 4, 63, 39, 40] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [28, 10, 5, 13, 55, 57, 25] jogos [28, 10, 5, 13, 58, 57, 25] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Ruch Chorzów tabela [28, 10, 5, 13, 43, 84, 25] jogos [28, 10, 5, 13, 43, 54, 25] (a tabela da Wikipédia fecha com os jogos)

### 1929

- tabela da RSSSF x jogos — Garbarnia Cracóvia tabela [24, 13, 6, 5, 62, 43, 33] jogos [24, 13, 6, 5, 62, 43, 32] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Cracovia tabela [24, 10, 8, 6, 50, 35, 28] jogos [24, 10, 8, 6, 60, 35, 28] (a tabela da Wikipédia fecha com os jogos)

### 1930

- tabela da RSSSF x jogos — Wisła Cracóvia tabela [22, 14, 4, 4, 52, 34, 32] jogos [22, 14, 4, 4, 53, 34, 32] (a tabela da Wikipédia fecha com os jogos)

### 1931

- Ruch Chorzów x Garbarnia Cracóvia: fica 1-1 (RSSSF); a matriz da Wikipédia dá 1-0, que fecha pior com as tabelas
- tabela da RSSSF x jogos — Wisła Cracóvia tabela [22, 14, 1, 7, 53, 30, 29] jogos [22, 13, 3, 6, 53, 30, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Legia Varsóvia tabela [22, 13, 3, 6, 57, 34, 29] jogos [22, 14, 1, 7, 57, 34, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Pogoń Lwów tabela [22, 11, 6, 5, 47, 33, 29] jogos [22, 11, 6, 5, 47, 33, 28] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [22, 10, 4, 8, 48, 35, 24] jogos [22, 10, 4, 8, 48, 38, 24] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Cracovia tabela [22, 6, 6, 10, 32, 52, 18] jogos [22, 6, 6, 10, 33, 52, 18] (a tabela da Wikipédia fecha com os jogos)

### 1932

- sem ocorrências

### 1933

- tabela da Wikipédia sem matriz (play-off contra clubes da 2ª divisão), fora do pacote: ['Garbarnia Cracóvia', 'Śmigły Wilno', 'Czarni Lwów']
- tabela (Grupo Leste) da RSSSF x jogos — Pogoń Lwów tabela [10, 6, 3, 1, 19, 4, 15] jogos [10, 6, 3, 1, 19, 14, 15] (a tabela da Wikipédia fecha com os jogos)
- tabela (Grupo Leste) da RSSSF x jogos — Strzelec Siedlce tabela [10, 1, 1, 8, 15, 20, 3] jogos [10, 1, 1, 8, 15, 29, 3] (a tabela da Wikipédia fecha com os jogos)
- tabela (Grupo Oeste) da RSSSF x jogos — Warta Poznań tabela [10, 3, 0, 7, 15, 18, 6] jogos [10, 3, 0, 7, 15, 16, 6] (a tabela da Wikipédia fecha com os jogos)

### 1934

- Garbarnia Cracóvia x ŁKS Łódź: derrota para os dois (jogo não disputado; W.O. contra os dois (RSSSF))
- tabela da Wikipédia x jogos — Garbarnia Cracóvia tabela [21, 11, 3, 7, 49, 36, 25] jogos [22, 11, 3, 8, 49, 33, 25]
- tabela da Wikipédia x jogos — ŁKS Łódź tabela [21, 10, 1, 10, 31, 45, 21] jogos [22, 10, 1, 11, 31, 40, 21]
- tabela da Wikipédia x jogos — Warszawianka tabela [22, 8, 1, 13, 26, 33, 17] jogos [22, 8, 1, 13, 26, 53, 17]
- tabela da RSSSF x jogos — Garbarnia Cracóvia tabela [22, 11, 3, 7, 49, 36, 25] jogos [22, 11, 3, 8, 49, 33, 25]
- tabela da RSSSF x jogos — ŁKS Łódź tabela [22, 10, 1, 10, 31, 45, 21] jogos [22, 10, 1, 11, 31, 40, 21]
- tabela da RSSSF x jogos — Warszawianka tabela [22, 8, 1, 13, 26, 33, 17] jogos [22, 8, 1, 13, 26, 53, 17]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1935

- tabela da Wikipédia x jogos — Pogoń Lwów tabela [20, 11, 3, 6, 55, 31, 25] jogos [20, 10, 3, 7, 52, 34, 23]
- tabela da Wikipédia x jogos — Wisła Cracóvia tabela [20, 10, 3, 7, 51, 33, 23] jogos [20, 10, 3, 7, 51, 38, 23]
- tabela da Wikipédia x jogos — Legia Varsóvia tabela [20, 8, 2, 10, 32, 46, 18] jogos [20, 9, 2, 9, 35, 43, 20]
- tabela da Wikipédia x jogos — Polonia Varsóvia tabela [20, 3, 2, 15, 15, 57, 8] jogos [20, 3, 2, 15, 18, 57, 8]
- tabela da RSSSF x jogos — Pogoń Lwów tabela [20, 11, 3, 6, 55, 31, 25] jogos [20, 10, 3, 7, 52, 34, 23]
- tabela da RSSSF x jogos — Wisła Cracóvia tabela [20, 10, 3, 7, 51, 33, 23] jogos [20, 10, 3, 7, 51, 38, 23]
- tabela da RSSSF x jogos — Legia Varsóvia tabela [20, 8, 2, 10, 32, 46, 18] jogos [20, 9, 2, 9, 35, 43, 20]
- tabela da RSSSF x jogos — Polonia Varsóvia tabela [20, 3, 2, 15, 15, 57, 8] jogos [20, 3, 2, 15, 18, 57, 8]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 4 clubes: a classificação final fica com os números publicados (observação na linha)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (media) difere em 5 posições (ex.: ['Pogoń Lwów', 'Warta Poznań'])

### 1936

- tabela da RSSSF x jogos — Śląsk Świętochłowice tabela [18, 4, 3, 11, 31, 40, 11] jogos [18, 4, 3, 11, 21, 40, 11] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Legia Varsóvia tabela [18, 3, 2, 13, 34, 46, 8] jogos [18, 3, 2, 13, 24, 46, 8] (a tabela da Wikipédia fecha com os jogos)

### 1937

- tabela da Wikipédia x jogos — Warta Poznań tabela [16, 6, 4, 6, 34, 38, 16] jogos [16, 6, 4, 6, 34, 36, 16]
- tabela da RSSSF x jogos — Cracovia tabela [18, 8, 6, 2, 37, 16, 22] jogos [16, 8, 6, 2, 37, 16, 22] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — AKS Chorzów tabela [18, 8, 4, 4, 31, 22, 20] jogos [16, 8, 4, 4, 31, 22, 20] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Ruch Chorzów tabela [18, 7, 5, 4, 40, 29, 19] jogos [16, 7, 5, 4, 40, 29, 19] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Warta Poznań tabela [18, 6, 4, 6, 34, 38, 16] jogos [16, 6, 4, 6, 34, 36, 16]
- tabela da RSSSF x jogos — Wisła Cracóvia tabela [18, 6, 3, 7, 30, 23, 15] jogos [16, 6, 3, 7, 30, 23, 15] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Pogoń Lwów tabela [18, 6, 3, 7, 19, 23, 15] jogos [16, 6, 3, 7, 19, 23, 15] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Warszawianka tabela [18, 6, 2, 8, 28, 44, 14] jogos [16, 6, 2, 8, 28, 44, 14] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [18, 5, 2, 9, 30, 39, 12] jogos [16, 5, 2, 9, 30, 39, 12] (a tabela da Wikipédia fecha com os jogos)

### 1938

- tabela da Wikipédia x jogos — Polonia Varsóvia tabela [18, 9, 1, 8, 40, 35, 19] jogos [18, 9, 1, 8, 40, 38, 19]
- tabela da RSSSF x jogos — Polonia Varsóvia tabela [18, 9, 1, 8, 40, 35, 19] jogos [18, 9, 1, 8, 40, 38, 19]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1946

- sem ocorrências

### 1947

- tabela (Grupo 1) da RSSSF x jogos — Polonia Varsóvia tabela [16, 10, 4, 2, 70, 20, 24] jogos [16, 10, 4, 2, 70, 26, 24] (a tabela da Wikipédia fecha com os jogos)
- tabela (Grupo 2) da RSSSF x jogos — Glinik Gorlice tabela [18, 5, 2, 11, 55, 52, 12] jogos [18, 5, 2, 11, 35, 52, 12] (a tabela da Wikipédia fecha com os jogos)
- tabela (Grupo 3) da RSSSF x jogos — Tęcza Kielce tabela [16, 8, 1, 7, 34, 38, 17] jogos [16, 8, 1, 7, 34, 36, 17] (a tabela da Wikipédia fecha com os jogos)

### 1948

- sem ocorrências

### 1949

- tabela da Wikipédia x jogos — ŁKS Łódź tabela [22, 8, 6, 8, 43, 48, 22] jogos [22, 8, 6, 8, 49, 48, 22]
- tabela da RSSSF x jogos — ŁKS Łódź tabela [22, 8, 6, 8, 43, 48, 22] jogos [22, 8, 6, 8, 49, 48, 22]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1950

- Lech Poznań x Ruch Chorzów: fica 1-3 (RSSSF); a matriz da Wikipédia dá 1-2, que fecha pior com as tabelas

### 1951

- sem ocorrências

### 1952

- sem ocorrências

### 1953

- tabela da Wikipédia x jogos — Polonia Bytom tabela [22, 10, 3, 9, 33, 29, 23] jogos [22, 10, 3, 9, 33, 28, 23]
- tabela da Wikipédia x jogos — Lechia Gdańsk tabela [22, 2, 8, 12, 21, 35, 12] jogos [22, 2, 8, 12, 20, 35, 12]
- tabela da RSSSF x jogos — Polonia Bytom tabela [22, 10, 3, 9, 33, 29, 23] jogos [22, 10, 3, 9, 33, 28, 23]
- tabela da RSSSF x jogos — Lechia Gdańsk tabela [22, 2, 8, 12, 21, 35, 12] jogos [22, 2, 8, 12, 20, 35, 12]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 2 clubes: a classificação final fica com os números publicados (observação na linha)

### 1954

- sem ocorrências

### 1955

- sem ocorrências

### 1956

- tabela da Wikipédia x jogos — Zagłębie Sosnowiec tabela [22, 6, 5, 11, 35, 43, 17] jogos [22, 6, 5, 11, 32, 43, 17]
- tabela da RSSSF x jogos — Zagłębie Sosnowiec tabela [22, 6, 5, 11, 35, 43, 17] jogos [22, 6, 5, 11, 32, 43, 17]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1957

- tabela da Wikipédia x jogos — Zagłębie Sosnowiec tabela [22, 5, 10, 7, 38, 45, 20] jogos [22, 5, 10, 7, 28, 45, 20]
- tabela da RSSSF x jogos — Zagłębie Sosnowiec tabela [22, 5, 10, 7, 38, 45, 20] jogos [22, 5, 10, 7, 28, 45, 20]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1958

- tabela da Wikipédia x jogos — Wisła Cracóvia tabela [23, 8, 4, 11, 39, 50, 20] jogos [22, 8, 4, 10, 39, 50, 20]
- tabela da RSSSF x jogos — Wisła Cracóvia tabela [22, 8, 4, 11, 39, 50, 20] jogos [22, 8, 4, 10, 39, 50, 20]

### 1959

- sem ocorrências

### 1960

- tabela da Wikipédia x jogos — Lechia Gdańsk tabela [22, 7, 4, 11, 25, 35, 18] jogos [22, 7, 4, 11, 29, 35, 18]
- tabela da RSSSF x jogos — Lechia Gdańsk tabela [22, 7, 4, 11, 25, 35, 18] jogos [22, 7, 4, 11, 29, 35, 18]
- os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em 1 clubes: a classificação final fica com os números publicados (observação na linha)

### 1961

- tabela da RSSSF x jogos — Polonia Bydgoszcz tabela [26, 8, 3, 15, 36, 71, 19] jogos [26, 8, 3, 15, 36, 69, 19] (a tabela da Wikipédia fecha com os jogos)

### 1962

- sem ocorrências

### 1962/63

- sem ocorrências

### 1963/64

- tabela da Wikipédia x jogos — Górnik Zabrze tabela [26, 17, 6, 3, 57, 23, 40] jogos [26, 17, 6, 3, 59, 24, 40]
- tabela da Wikipédia x jogos — Polonia Bytom tabela [26, 11, 5, 10, 39, 33, 27] jogos [26, 11, 5, 10, 40, 35, 27]
- tabela da RSSSF x jogos — Górnik Zabrze tabela [26, 17, 6, 3, 57, 23, 38] jogos [26, 17, 6, 3, 59, 24, 40]
- tabela da RSSSF x jogos — Polonia Bytom tabela [26, 11, 5, 10, 39, 33, 27] jogos [26, 11, 5, 10, 40, 35, 27]

### 1964/65

- Gwardia Varsóvia x Ruch Chorzów: o ogol não tem o jogo; entra 1-1 pela matriz da Wikipédia, sem data
- ŁKS Łódź x Zawisza Bydgoszcz: o ogol não tem o jogo; entra 2-0 pela matriz da Wikipédia, sem data
- Odra Opole x Śląsk Wrocław: o ogol não tem o jogo; entra 0-0 pela matriz da Wikipédia, sem data
- Stal Rzeszów x Unia Racibórz: o ogol não tem o jogo; entra 5-0 pela matriz da Wikipédia, sem data
- Pogoń Szczecin x Legia Varsóvia: o ogol não tem o jogo; entra 1-3 pela matriz da Wikipédia, sem data

### 1965/66

- sem ocorrências

### 1966/67

- sem ocorrências

### 1967/68

- sem ocorrências

### 1968/69

- tabela da Wikipédia x jogos — Polonia Bytom tabela [29, 8, 12, 9, 30, 23, 28] jogos [26, 8, 12, 6, 30, 23, 28]
- tabela da RSSSF x jogos — Polonia Bytom tabela [26, 8, 12, 9, 30, 23, 28] jogos [26, 8, 12, 6, 30, 23, 28]

### 1969/70

- placar diferente na matriz da Wikipédia — Szombierki Bytom x Legia Varsóvia: ogol 2-2; Wikipédia 3-2

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- tabela da RSSSF x jogos — Legia Varsóvia tabela [26, 6, 11, 9, 29, 28, 26] jogos [26, 6, 11, 9, 29, 28, 23] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Zagłębie Sosnowiec tabela [26, 8, 6, 12, 30, 31, 23] jogos [26, 8, 6, 12, 30, 31, 22] (a tabela da Wikipédia fecha com os jogos)

### 1973/74

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['ŁKS Łódź', 'ROW Rybnik'])

### 1974/75

- tabela da RSSSF x jogos — Górnik Zabrze tabela [30, 7, 15, 8, 48, 46, 28] jogos [30, 7, 15, 8, 48, 46, 29] (a tabela da Wikipédia fecha com os jogos)

### 1975/76

- sem ocorrências

### 1976/77

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Wisła Cracóvia', 'Szombierki Bytom'])

### 1977/78

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 8 posições (ex.: ['ŁKS Łódź', 'Legia Varsóvia'])

### 1978/79

- tabela da RSSSF x jogos — Odra Opole tabela [30, 13, 6, 11, 42, 28, 34] jogos [30, 14, 6, 10, 42, 28, 34] (a tabela da Wikipédia fecha com os jogos)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['ŁKS Łódź', 'Wisła Cracóvia'])

### 1979/80

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Górnik Zabrze', 'ŁKS Łódź'])

### 1980/81

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 6 posições (ex.: ['Szombierki Bytom', 'Śląsk Wrocław'])

### 1981/82

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['Widzew Łódź', 'Śląsk Wrocław'])

### 1982/83

- sem ocorrências

### 1983/84

- sem ocorrências

### 1984/85

- tabela da RSSSF x jogos — Widzew Łódź tabela [30, 13, 12, 5, 34, 16, 39] jogos [30, 13, 12, 5, 34, 16, 38] (a tabela da Wikipédia fecha com os jogos)

### 1985/86

- tabela da Wikipédia x jogos — Śląsk Wrocław tabela [30, 9, 11, 10, 39, 35, 29] jogos [30, 9, 11, 10, 39, 36, 29]
- tabela da RSSSF x jogos — Śląsk Wrocław tabela [30, 9, 11, 10, 39, 35, 29] jogos [30, 9, 11, 10, 39, 36, 29]

### 1986/87

- tabela da Wikipédia x jogos — Lech Poznań tabela [29, 9, 11, 9, 36, 35, 29] jogos [30, 9, 12, 9, 37, 36, 30]
- tabela da Wikipédia x jogos — Zagłębie Lubin tabela [29, 8, 12, 9, 27, 25, 28] jogos [30, 8, 12, 10, 27, 27, 28]
- tabela da Wikipédia x jogos — Olimpia Poznań tabela [29, 6, 14, 9, 21, 35, 22] jogos [30, 6, 14, 10, 22, 38, 22]
- tabela da Wikipédia x jogos — Polonia Bytom tabela [29, 5, 14, 10, 24, 37, 21] jogos [30, 5, 15, 10, 25, 38, 22]
- tabela da Wikipédia x jogos — Ruch Chorzów tabela [29, 3, 14, 12, 16, 33, 18] jogos [30, 4, 14, 12, 18, 33, 20]
- tabela da Wikipédia x jogos — Stal Mielec tabela [29, 5, 10, 14, 24, 44, 17] jogos [30, 6, 10, 14, 27, 45, 19]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Olimpia Poznań', 'Polonia Bytom'])

### 1987/88

- tabela da Wikipédia x jogos — Śląsk Wrocław tabela [30, 9, 11, 10, 32, 30, 29] jogos [30, 9, 11, 10, 31, 32, 29]
- tabela da Wikipédia x jogos — Zagłębie Lubin tabela [30, 8, 10, 12, 23, 25, 26] jogos [30, 8, 11, 11, 23, 25, 26]

### 1988/89

- tabela da Wikipédia x jogos — Śląsk Wrocław tabela [30, 7, 15, 8, 34, 35, 29] jogos [30, 7, 14, 9, 34, 35, 28]
- tabela da Wikipédia x jogos — Pogoń Szczecin tabela [30, 6, 10, 14, 34, 50, 19] jogos [30, 7, 9, 14, 34, 50, 20]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 3 posições (ex.: ['Śląsk Wrocław', 'Widzew Łódź'])

### 1989/90

- tabela da Wikipédia x jogos — Olimpia Poznań tabela [30, 12, 10, 8, 35, 22, 36] jogos [30, 12, 10, 8, 35, 23, 36]
- tabela da Wikipédia x jogos — Wisła Cracóvia tabela [30, 8, 12, 10, 32, 34, 31] jogos [30, 8, 12, 10, 32, 33, 31]
- tabela da Wikipédia x jogos — Stal Mielec tabela [30, 8, 10, 12, 27, 37, 26] jogos [30, 8, 10, 12, 27, 38, 26]
- tabela da Wikipédia x jogos — Jagiellonia Białystok tabela [29, 3, 13, 13, 19, 45, 13] jogos [30, 3, 13, 14, 19, 45, 13]

### 1990/91

- tabela da Wikipédia x jogos — Lech Poznań tabela [30, 10, 13, 7, 48, 28, 33] jogos [30, 10, 13, 7, 49, 28, 33]
- tabela da Wikipédia x jogos — Igloopol Dębica tabela [30, 7, 12, 11, 29, 44, 26] jogos [30, 7, 12, 11, 29, 45, 26]
- tabela da Wikipédia x jogos — Ruch Chorzów tabela [30, 7, 11, 12, 25, 34, 25] jogos [30, 7, 11, 12, 25, 35, 25]
- tabela da RSSSF x jogos — Lech Poznań tabela [30, 11, 12, 7, 48, 28, 33] jogos [30, 10, 13, 7, 49, 28, 33]
- tabela da RSSSF x jogos — Igloopol Dębica tabela [30, 7, 12, 11, 29, 44, 26] jogos [30, 7, 12, 11, 29, 45, 26]
- tabela da RSSSF x jogos — Ruch Chorzów tabela [30, 7, 11, 12, 25, 34, 25] jogos [30, 7, 11, 12, 25, 35, 25]
- tabela da RSSSF x jogos — Zawisza Bydgoszcz tabela [30, 8, 8, 14, 27, 41, 23] jogos [30, 8, 7, 15, 27, 41, 23] (a tabela da Wikipédia fecha com os jogos)

### 1991/92

- tabela da Wikipédia x jogos — Igloopol Dębica tabela [34, 2, 7, 25, 15, 76, 11] jogos [34, 2, 7, 25, 14, 76, 11]
- tabela da RSSSF x jogos — Igloopol Dębica tabela [34, 2, 7, 25, 15, 76, 11] jogos [34, 2, 7, 25, 14, 76, 11]

### 1992/93

- ŁKS Łódź x Olimpia Poznań (1993-06-20, 7-1 no ogol): fora do pacote — 7-1 no campo, anulado pela federação por suspeita de manipulação
- Wisła Cracóvia x Legia Varsóvia (1993-06-20, 6-0 no ogol): fora do pacote — 0-6 no campo, anulado pela federação por suspeita de manipulação
- tabela da Wikipédia x jogos — ŁKS Łódź tabela [33, 18, 11, 4, 50, 26, 47] jogos [33, 18, 11, 4, 53, 32, 47]
- tabela da Wikipédia x jogos — Siarka Tarnobrzeg tabela [34, 11, 9, 14, 39, 38, 31] jogos [34, 11, 9, 14, 39, 42, 31]
- tabela da Wikipédia x jogos — Śląsk Wrocław tabela [34, 9, 5, 20, 33, 72, 23] jogos [34, 9, 5, 20, 33, 74, 23]
- tabela da RSSSF x jogos — Legia Varsóvia tabela [34, 21, 7, 6, 50, 26, 47] jogos [33, 20, 7, 6, 50, 26, 47] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [34, 19, 11, 4, 53, 32, 47] jogos [33, 18, 11, 4, 53, 32, 47]
- tabela da RSSSF x jogos — Wisła Cracóvia tabela [34, 12, 10, 12, 48, 42, 34] jogos [33, 12, 10, 11, 49, 37, 34] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Siarka Tarnobrzeg tabela [34, 11, 9, 14, 39, 38, 31] jogos [34, 11, 9, 14, 39, 42, 31]
- tabela da RSSSF x jogos — Hutnik Cracóvia tabela [34, 9, 12, 13, 40, 46, 29] jogos [34, 8, 13, 13, 40, 46, 29] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Śląsk Wrocław tabela [34, 9, 5, 20, 33, 72, 23] jogos [34, 9, 5, 20, 33, 74, 23]
- tabela da RSSSF x jogos — Olimpia Poznań tabela [34, 7, 7, 20, 28, 56, 21] jogos [33, 7, 7, 19, 27, 49, 21] (a tabela da Wikipédia fecha com os jogos)
- 304 jogos para 18 clubes (esperados 306)

### 1993/94

- tabela da Wikipédia x jogos — Widzew Łódź tabela [34, 12, 15, 7, 43, 34, 39] jogos [34, 12, 15, 7, 45, 33, 39]
- tabela da Wikipédia x jogos — Hutnik Cracóvia tabela [34, 12, 13, 9, 34, 28, 37] jogos [34, 12, 13, 9, 33, 30, 37]
- tabela da Wikipédia x jogos — Stal Stalowa Wola tabela [34, 8, 14, 12, 40, 47, 30] jogos [34, 8, 14, 12, 25, 37, 30]
- tabela da Wikipédia x jogos — Zagłębie Lubin tabela [34, 9, 12, 13, 25, 37, 30] jogos [34, 9, 12, 13, 40, 47, 30]
- tabela da Wikipédia x jogos — Siarka Tarnobrzeg tabela [34, 5, 9, 20, 28, 61, 19] jogos [34, 5, 9, 20, 25, 57, 19]
- tabela da Wikipédia x jogos — Polonia Varsóvia tabela [34, 4, 11, 19, 25, 57, 19] jogos [34, 4, 11, 19, 28, 61, 19]
- tabela da RSSSF x jogos — Legia Varsóvia tabela [34, 18, 13, 3, 52, 20, 49] jogos [34, 19, 13, 2, 72, 24, 48] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — GKS Katowice tabela [34, 18, 11, 5, 65, 22, 47] jogos [34, 17, 13, 4, 52, 28, 47] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Górnik Zabrze tabela [34, 14, 14, 6, 35, 19, 42] jogos [34, 17, 12, 5, 56, 32, 46] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — ŁKS Łódź tabela [34, 16, 9, 9, 47, 32, 41] jogos [34, 17, 11, 6, 49, 24, 42] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Pogoń Szczecin tabela [34, 14, 12, 8, 41, 32, 40] jogos [34, 11, 19, 4, 39, 24, 41] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Widzew Łódź tabela [34, 13, 12, 9, 29, 25, 38] jogos [34, 12, 15, 7, 45, 33, 39]
- tabela da RSSSF x jogos — Ruch Chorzów tabela [34, 10, 14, 10, 30, 27, 34] jogos [34, 14, 9, 11, 48, 41, 37] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Hutnik Cracóvia tabela [34, 12, 10, 12, 38, 43, 34] jogos [34, 12, 13, 9, 33, 30, 37]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Siarka Tarnobrzeg', 'Polonia Varsóvia'])

### 1994/95

- tabela da Wikipédia x jogos — Widzew Łódź tabela [34, 17, 11, 6, 47, 25, 45] jogos [34, 17, 11, 6, 48, 25, 45]
- tabela da Wikipédia x jogos — Wisła Płock tabela [34, 8, 14, 12, 35, 42, 30] jogos [34, 8, 14, 12, 35, 43, 30]
- tabela da RSSSF x jogos — Widzew Łódź tabela [34, 17, 11, 6, 47, 25, 45] jogos [34, 17, 11, 6, 48, 25, 45]
- tabela da RSSSF x jogos — Wisła Płock tabela [34, 8, 14, 12, 35, 42, 30] jogos [34, 8, 14, 12, 35, 43, 30]
- Sokół Pniewy não está na temporada seguinte, mas não caiu: mudou-se para Tychy (Sokół Tychy, hoje GKS Tychy, que ficou com a vaga em 1995/96)
- Olimpia Poznań não está na temporada seguinte, mas não caiu: fundiu-se com o Lechia Gdańsk (Olimpia/Lechia Gdańsk, que ficou com a vaga em 1995/96)

### 1995/96

- tabela da RSSSF x jogos — Zagłębie Lubin tabela [34, 11, 11, 12, 34, 35, 32] jogos [34, 11, 11, 12, 34, 35, 44] (a tabela da Wikipédia fecha com os jogos)

### 1996/97

- GKS Tychy x Odra Wodzisław (1997-04-05): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Śląsk Wrocław x GKS Tychy (1997-05-04): DA no ogol; fica 3-0 pela matriz da Wikipédia
- GKS Tychy x Widzew Łódź (1997-05-07): DA no ogol; fica 0-3 pela matriz da Wikipédia
- GKS Katowice x GKS Tychy (1997-05-11): DA no ogol; fica 3-0 pela matriz da Wikipédia
- GKS Tychy x Amica Wronki (1997-05-18): DA no ogol; fica 0-3 pela matriz da Wikipédia
- GKS Tychy x Raków Częstochowa (1997-05-24): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Legia Varsóvia x GKS Tychy (1997-06-05): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Raków Częstochowa x Śląsk Wrocław (1997-06-18): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Zagłębie Lubin x GKS Tychy (1997-06-18): DA no ogol; fica 3-0 pela matriz da Wikipédia
- GKS Tychy x ŁKS Łódź (1997-06-25): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Śląsk Wrocław x Zagłębie Lubin (1997-06-25): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 1997/98

- sem ocorrências

### 1998/99

- sem ocorrências

### 1999/00

- Polonia Varsóvia x Wisła Płock (1999-11-06): DA no ogol; fica 3-0 pela matriz da Wikipédia
- tabela da Wikipédia x jogos — Polonia Varsóvia tabela [30, 20, 5, 5, 56, 26, 65] jogos [30, 20, 5, 5, 57, 25, 65]
- tabela da Wikipédia x jogos — Wisła Płock tabela [30, 9, 7, 14, 35, 48, 34] jogos [30, 9, 7, 14, 35, 49, 34]
- tabela da Wikipédia x jogos — Pogoń Szczecin tabela [30, 8, 10, 12, 41, 53, 34] jogos [30, 8, 10, 12, 42, 53, 34]
- tabela da Wikipédia x jogos — ŁKS Łódź tabela [30, 7, 7, 16, 29, 42, 28] jogos [30, 7, 7, 16, 28, 42, 28]
- tabela da RSSSF x jogos — Polonia Varsóvia tabela [30, 20, 5, 5, 56, 26, 65] jogos [30, 20, 5, 5, 57, 25, 65]
- tabela da RSSSF x jogos — Wisła Płock tabela [30, 9, 7, 14, 35, 48, 34] jogos [30, 9, 7, 14, 35, 49, 34]
- tabela da RSSSF x jogos — Pogoń Szczecin tabela [30, 8, 10, 12, 41, 53, 34] jogos [30, 8, 10, 12, 42, 53, 34]
- tabela da RSSSF x jogos — ŁKS Łódź tabela [30, 7, 7, 16, 29, 42, 28] jogos [30, 7, 7, 16, 28, 42, 28]

### 2000/01

- tabela da Wikipédia x jogos — Ruch Chorzów tabela [30, 13, 5, 12, 50, 48, 44] jogos [30, 13, 5, 12, 50, 46, 44]
- tabela da Wikipédia x jogos — Ruch Radzionków tabela [30, 9, 4, 17, 29, 51, 31] jogos [30, 9, 4, 17, 27, 51, 31]

### 2001/02

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (saldo) difere em 3 posições (ex.: ['Odra Wodzisław', 'GKS Katowice'])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 2 posições (ex.: ['Śląsk Wrocław', 'Stomil Olsztyn'])

### 2002/03

- Ruch Chorzów x Pogoń Szczecin (2002-06-03): DA no ogol; fica 3-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Ruch Chorzów x Zagłębie Lubin: ogol 0-3; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Widzew Łódź x Wisła Cracóvia: ogol 2-4; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — Wisła Cracóvia x Polonia Varsóvia: ogol 3-0; Wikipédia 2-0
- tabela da Wikipédia x jogos — Legia Varsóvia tabela [30, 17, 9, 4, 61, 29, 60] jogos [30, 17, 9, 4, 59, 29, 60]
- tabela da Wikipédia x jogos — Wisła Płock tabela [30, 10, 7, 13, 29, 38, 37] jogos [30, 10, 7, 13, 29, 36, 37]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Widzew Łódź', 'Wisła Płock'])

### 2003/04

- Widzew Łódź x Dyskobolia (2004-06-11): DA no ogol; fica 0-1 pela matriz da Wikipédia
- Widzew Łódź x Polonia Varsóvia: o ogol tem o par duas vezes com o mesmo mandante; a matriz da Wikipédia dá Polonia Varsóvia 2-1 Widzew Łódź no returno; fica o ogol (a troca não fecha melhor)
- placar diferente na matriz da Wikipédia — Lech Poznań x Legia Varsóvia: ogol 0-1; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Lech Poznań x Widzew Łódź: ogol 1-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Widzew Łódź x Polonia Varsóvia: ogol 1-1, 2-1; Wikipédia 1-1
- tabela da Wikipédia x jogos — Dyskobolia tabela [26, 13, 7, 6, 59, 31, 46] jogos [26, 13, 7, 6, 57, 31, 46]
- tabela da Wikipédia x jogos — Widzew Łódź tabela [26, 4, 7, 15, 25, 52, 19] jogos [26, 4, 7, 15, 25, 50, 19]

### 2004/05

- GKS Katowice x Odra Wodzisław (2005-05-25): fica 0-3 pela matriz da Wikipédia; o ogol dá 1-1, que fecha pior com as tabelas

### 2005/06

- placar diferente na matriz da Wikipédia — Amica Wronki x GKS Bełchatów: ogol 3-1; Wikipédia 2-1
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 13 posições (ex.: ['Zagłębie Lubin', 'Amica Wronki'])
- Amica Wronki não está na temporada seguinte, mas não caiu: fundiu-se com o Lech Poznań depois da temporada (nota da tabela da Wikipédia)
- rebaixados pela temporada seguinte ['Polonia Varsóvia']; marcados na tabela da Wikipédia ['Lech Poznań', 'Polonia Varsóvia']

### 2006/07

- Arka Gdynia x Widzew Łódź (2007-05-16): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Korona Kielce x Górnik Zabrze (2006-11-17): fica 4-2 pela matriz da Wikipédia; o ogol dá Górnik Zabrze 0-0 Korona Kielce (o par duas vezes com o mesmo mandante)
- placar diferente na matriz da Wikipédia — Górnik Zabrze x Arka Gdynia: ogol 0-2; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Górnik Zabrze x Cracovia: ogol 5-1; Wikipédia 1-5
- placar diferente na matriz da Wikipédia — Górnik Zabrze x GKS Bełchatów: ogol 1-0; Wikipédia 0-4
- placar diferente na matriz da Wikipédia — Górnik Zabrze x Górnik Łęczna: ogol 2-3; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Górnik Zabrze x Widzew Łódź: ogol 0-0; Wikipédia 0-3
- placar diferente na matriz da Wikipédia — Widzew Łódź x Górnik Łęczna: ogol 3-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Widzew Łódź x Górnik Zabrze: ogol 2-1; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Wisła Płock x Górnik Zabrze: ogol 1-3; Wikipédia 0-1

### 2007/08

- Polonia Bytom x Odra Wodzisław (2007-11-03): fica 1-0 pela matriz da Wikipédia; o ogol dá 0-1, que fecha pior com as tabelas
- placar diferente na matriz da Wikipédia — Dyskobolia x Polonia Bytom: ogol 5-0; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — GKS Bełchatów x Cracovia: ogol 1-1; Wikipédia 0-4
- placar diferente na matriz da Wikipédia — GKS Bełchatów x Dyskobolia: ogol 0-4; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — ŁKS Łódź x Dyskobolia: ogol 1-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Polonia Bytom x Górnik Zabrze: ogol 0-1; Wikipédia 0-4
- placar diferente na matriz da Wikipédia — Odra Wodzisław x Dyskobolia: ogol 2-3; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Widzew Łódź x Lech Poznań: ogol 1-1; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Zagłębie Sosnowiec x Jagiellonia Białystok: ogol 3-1; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Zagłębie Sosnowiec x Widzew Łódź: ogol 0-0; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Zagłębie Sosnowiec x Wisła Cracóvia: ogol 1-3; Wikipédia 0-0
- Dyskobolia não está na temporada seguinte, mas não caiu: fundiu-se com a Polonia Varsóvia, que ficou com a vaga em 2008/09

### 2008/09

- Górnik Zabrze x Piast Gliwice: o ogol tem o par duas vezes com o mesmo mandante; a matriz da Wikipédia dá Piast Gliwice 1-0 Górnik Zabrze no returno; fica o ogol (a troca não fecha melhor)
- placar diferente na matriz da Wikipédia — Górnik Zabrze x Piast Gliwice: ogol 0-1, 1-0; Wikipédia 1-0
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 9 posições (ex.: ['Jagiellonia Białystok', 'Ruch Chorzów'])

### 2009/10

- sem ocorrências

### 2010/11

- placar diferente na matriz da Wikipédia — Zagłębie Lubin x Wisła Cracóvia: ogol 0-3; Wikipédia 0-2
- tabela da Wikipédia x jogos — Zagłębie Lubin tabela [30, 10, 9, 11, 31, 41, 39] jogos [30, 10, 9, 11, 31, 38, 39]
- tabela da Wikipédia x jogos — Korona Kielce tabela [30, 10, 7, 13, 34, 49, 37] jogos [30, 10, 7, 13, 34, 48, 37]

### 2011/12

- Polonia Varsóvia x Lechia Gdańsk: o ogol tem o par duas vezes com o mesmo mandante; a matriz da Wikipédia dá Lechia Gdańsk 1-3 Polonia Varsóvia no returno; fica o ogol (a troca não fecha melhor)
- placar diferente na matriz da Wikipédia — Polonia Varsóvia x Lechia Gdańsk: ogol 1-0, 3-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Polonia Varsóvia x Podbeskidzie: ogol 2-1; Wikipédia 2-2

### 2012/13

- rebaixados pela temporada seguinte ['GKS Bełchatów', 'Polonia Varsóvia']; marcados na tabela da Wikipédia ['GKS Bełchatów']

### 2013/14

- Legia Varsóvia x Jagiellonia Białystok (2014-03-02): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Zagłębie Lubin x Widzew Łódź (2014-05-31): DA no ogol; fica 0-3 pela matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (saldo) difere em 0 posições (ex.: [])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 0 posições (ex.: [])

### 2014/15

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (confronto) difere em 0 posições (ex.: [])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 0 posições (ex.: [])

### 2015/16

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (confronto) difere em 0 posições (ex.: [])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 0 posições (ex.: [])

### 2016/17

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (saldo) difere em 2 posições (ex.: ['Jagiellonia Białystok', 'Lech Poznań'])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 2 posições (ex.: ['Arka Gdynia', 'Cracovia'])

### 2017/18

- Piast Gliwice x Górnik Zabrze (2018-03-03): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Lech Poznań x Legia Varsóvia (2018-05-20): DA no ogol; fica 0-3 pela matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (saldo) difere em 0 posições (ex.: [])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 1 posições (ex.: ['Sandecja Nowy Sącz'])

### 2018/19

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (confronto) difere em 2 posições (ex.: ['Cracovia', 'Jagiellonia Białystok'])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 1 posições (ex.: ['Zagłębie Sosnowiec'])

### 2019/20

- nenhum critério calculado reproduz a ordem oficial (Grupo do título); o mais próximo (confronto) difere em 0 posições (ex.: [])
- nenhum critério calculado reproduz a ordem oficial (Grupo de rebaixamento); o mais próximo (confronto) difere em 5 posições (ex.: ['Górnik Zabrze', 'Raków Częstochowa'])

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- Piast Gliwice x Lechia Gdańsk (2023-05-27): fica 3-0 pela matriz da Wikipédia (igual ao football-data); o ogol dá 0-1, que fecha pior com as tabelas

### 2023/24

- sem ocorrências

### 2024/25

- sem ocorrências

### 2025/26

- Jagiellonia Białystok x Wisła Płock (2025-09-19): fica 1-2 pela matriz da Wikipédia (igual ao football-data); o ogol dá 1-0
- Wisła Płock x Jagiellonia Białystok (2026-03-21): fica 0-1 pela matriz da Wikipédia (igual ao football-data); o ogol dá 2-1

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_pol.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os redirecionamentos). Mesmo clube: Wisła Cracóvia = Gwardia Kraków; Lech = KKS Poznań e Kolejarz; Ruch = Unia Chorzów; Legia = CWKS; Wisła Płock = Petrochemia e Orlen; GKS Tychy = Sokół; ROW Rybnik = Energetyk; Stomil = OKS Olsztyn; Termalica = LKS Nieciecza; Rymer Niedobczyce = Rymer Rybnik. Pelo link, a Wikipédia dá o PKS Szczecin de 1946-47 como o Pogoń Szczecin, o Motor Białystok de 1947 como o Jagiellonia, o Grochów de 1947 como o Gwardia Varsóvia e o RKU Sosnowiec como o Zagłębie Sosnowiec.
- Clubes de Lwów e Wilno com o país de hoje: Ucrânia (Lviv) e Lituânia (Vilnius). O Strzelec Wilno de 1922 (a RSSSF o chama de Śmigły, clube fundado em 1933 da fusão do Strzelec com outros).
- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Datas e rodadas de 1921 a 1962** (só a matriz de resultados, exceto as fichas da Wikipédia e a final de 1952).
- **Os jogos do grupo final de 1926:** nenhuma fonte traz (a Wikipédia polonesa só cita a vitória decisiva do Pogoń sobre a Polonia, 2-0, sem o mando); fica a tabela publicada.
- **Autores dos gols, cartões, público, estádio e árbitro:** nenhuma fonte em lote cobre a Polônia (sem ESPN; o football-data não traz cartões da Polônia); só a ficha de cada jogo no ogol.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.
