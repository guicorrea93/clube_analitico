# Campeonato Turco (1ª divisão) — coleta de dados

Gerado por `python coleta/tur-1/importar.py`. Pacote em `data/coleta/tur-1/pacote/`.

**Edições:** 97, de 1959 a 2025/26 (a liga nacional; os campeonatos anteriores a 1959 não são contados pela federação e ficam de fora).

**Total:** 20971 jogos, 54296 gols, 13891 gols com autor (ESPN), 23395 cartões, 168 clubes.

**Fontes:**
- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol (os nomes do calendário não são confiáveis nas temporadas antigas); calendários em `data/cache/ogol-tur-1/` para os escudos;
- RSSSF: tabelas finais de 1959 a 1996/97 (turkhist.html, com os grupos de 1959 e 1962/63), lista de campeões e de artilheiros;
- Wikipédia (en): tabelas e matriz de resultados de cada temporada (conferência jogo a jogo);
- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do football-data;
- ESPN (liga `tur.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). 2 pontos por vitória até 1986/87, 3 a partir de 1987/88. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 34, saldo em 28, vitórias em 1, média de gols em 3).

| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1924 (Şampiyonası) | Wikipédia (en) | 14 | 16 | 52 | 0 | 0 / 0 | — (Harp Okulu, não reconhecido) | — |
| 1927 (Şampiyonası) | Wikipédia (en) | 17 | 19 | 136 | 0 | 0 / 0 | — (Muhafızgücü, não reconhecido) | — |
| 1932 (Şampiyonası) | Wikipédia (en) | 20 | 21 | 114 | 3 | 0 / 0 | — (İstanbulspor, não reconhecido) | — |
| 1933 (Şampiyonası) | Wikipédia (en) | 18 | 16 | 98 | 23 | 0 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1934 (Şampiyonası) | Wikipédia (en) | 20 | 19 | 105 | 4 | 0 / 0 | — (Beşiktaş, não reconhecido) | — |
| 1935 (Şampiyonası) | Wikipédia (en) | 22 | 21 | 112 | 4 | 0 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1937 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 237 | 0 | 2 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1938 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 217 | 0 | 0 / 2 | — (Güneş, não reconhecido) | — |
| 1939 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 230 | 0 | 0 / 2 | — (Galatasaray, não reconhecido) | — |
| 1940 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 264 | 0 | 1 / 1 | — (Fenerbahçe, não reconhecido) | — |
| 1940 (Şampiyonası) | Wikipédia (en) | 2 | 2 | 4 | 4 | 0 / 0 | — (Eskişehir Demirspor, não reconhecido) | — |
| 1941 (Millî Küme) | Wikipédia (en) + RSSSF | 10 | 90 | 361 | 0 | 2 / 0 | — (Beşiktaş, não reconhecido) | — |
| 1941 (Şampiyonası) | Wikipédia (en) | 7 | 6 | 28 | 5 | 0 / 0 | — (Gençlerbirliği, não reconhecido) | — |
| 1942 (Şampiyonası) | Wikipédia (en) + RSSSF | 4 | 6 | 34 | 0 | 2 / 0 | — (Harp Okulu, não reconhecido) | — |
| 1943 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 212 | 0 | 2 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1944 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 191 | 0 | 2 / 0 | — (Beşiktaş, não reconhecido) | — |
| 1944 (Şampiyonası) | Wikipédia (en) + RSSSF | 4 | 6 | 35 | 6 | 2 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1945 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 205 | 0 | 1 / 1 | — (Fenerbahçe, não reconhecido) | — |
| 1945 (Şampiyonası) | Wikipédia (en) + RSSSF | 7 | 9 | 43 | 0 | 2 / 0 | — (Harp Okulu, não reconhecido) | — |
| 1946 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 30 | 139 | 0 | 1 / 2 | — (Fenerbahçe, não reconhecido) | — |
| 1946 (Şampiyonası) | Wikipédia (en) + RSSSF | 4 | 6 | 36 | 15 | 0 / 2 | — (Gençlerbirliği, não reconhecido) | — |
| 1947 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 223 | 0 | 1 / 1 | — (Beşiktaş, não reconhecido) | — |
| 1947 (Şampiyonası) | Wikipédia (en) + RSSSF | 3 | 3 | 15 | 9 | 2 / 0 | — (Ankara Demirspor, não reconhecido) | — |
| 1949 (Şampiyonası) | Wikipédia (en) + RSSSF | 6 | 9 | 28 | 7 | 2 / 0 | — (Ankaragücü, não reconhecido) | — |
| 1950 (Millî Küme) | Wikipédia (en) + RSSSF | 8 | 56 | 187 | 0 | 2 / 0 | — (Fenerbahçe, não reconhecido) | — |
| 1950 (Şampiyonası) | Wikipédia (en) + RSSSF | 4 | 12 | 36 | 0 | 2 / 0 | — (Göztepe, não reconhecido) | — |
| 1951 (Şampiyonası) | Wikipédia (en) + RSSSF | 9 | 11 | 48 | 0 | 2 / 0 | — (Beşiktaş, não reconhecido) | — |
| 1956/57 (Federasyon Kupası) | Wikipédia (en) + RSSSF | 27 | 51 | 180 | 0 | 0 / 2 | Beşiktaş | — |
| 1957/58 (Federasyon Kupası) | Wikipédia (en) | 38 | 46 | 155 | 0 | 2 / 0 | Beşiktaş | — |
| 1959 | ogol + RSSSF + Wikipédia | 16 | 114 | 264 | 0 | 3 / 1 | Fenerbahçe | — |
| 1959/60 | ogol + RSSSF + Wikipédia | 20 | 380 | 929 | 0 | 0 / 2 | Beşiktaş | — |
| 1960/61 | ogol + RSSSF + Wikipédia | 20 | 380 | 850 | 0 | 0 / 2 | Fenerbahçe | — |
| 1961/62 | ogol + RSSSF + Wikipédia | 20 | 380 | 857 | 0 | 2 / 0 | Galatasaray | — |
| 1962/63 | ogol + RSSSF + Wikipédia | 22 | 352 | 937 | 0 | 2 / 4 | Galatasaray | — |
| 1963/64 | ogol + RSSSF + Wikipédia | 18 | 306 | 631 | 0 | 2 / 0 | Fenerbahçe | — |
| 1964/65 | ogol + RSSSF + Wikipédia | 16 | 240 | 516 | 0 | 2 / 0 | Fenerbahçe | — |
| 1965/66 | ogol + RSSSF + Wikipédia | 16 | 240 | 545 | 0 | 0 / 2 | Beşiktaş | — |
| 1966/67 | ogol + RSSSF + Wikipédia | 17 | 272 | 549 | 0 | 2 / 0 | Beşiktaş | — |
| 1967/68 | ogol + RSSSF + Wikipédia | 17 | 272 | 602 | 0 | 2 / 0 | Fenerbahçe | — |
| 1968/69 | ogol + RSSSF + Wikipédia | 16 | 240 | 471 | 0 | 2 / 0 | Galatasaray | — |
| 1969/70 | ogol + RSSSF + Wikipédia | 16 | 240 | 419 | 0 | 2 / 0 | Fenerbahçe | — |
| 1970/71 | ogol + RSSSF + Wikipédia | 16 | 240 | 445 | 0 | 2 / 0 | Galatasaray | — |
| 1971/72 | ogol + RSSSF + Wikipédia | 16 | 240 | 464 | 0 | 2 / 0 | Galatasaray | — |
| 1972/73 | ogol + RSSSF + Wikipédia | 16 | 240 | 449 | 0 | 2 / 0 | Galatasaray | — |
| 1973/74 | ogol + RSSSF + Wikipédia | 16 | 240 | 405 | 0 | 2 / 0 | Fenerbahçe | — |
| 1974/75 | ogol + RSSSF + Wikipédia | 16 | 240 | 442 | 0 | 2 / 0 | Fenerbahçe | — |
| 1975/76 | ogol + RSSSF + Wikipédia | 16 | 240 | 479 | 0 | 2 / 0 | Trabzonspor | — |
| 1976/77 | ogol + RSSSF + Wikipédia | 16 | 240 | 442 | 0 | 2 / 0 | Trabzonspor | — |
| 1977/78 | ogol + RSSSF + Wikipédia | 16 | 240 | 474 | 0 | 0 / 2 | Fenerbahçe | — |
| 1978/79 | ogol + RSSSF + Wikipédia | 16 | 240 | 486 | 0 | 2 / 0 | Trabzonspor | — |
| 1979/80 | ogol + RSSSF + Wikipédia | 16 | 240 | 422 | 0 | 2 / 0 | Trabzonspor | — |
| 1980/81 | ogol + RSSSF + Wikipédia | 16 | 240 | 466 | 0 | 2 / 0 | Trabzonspor | — |
| 1981/82 | ogol + RSSSF + Wikipédia | 17 | 272 | 490 | 0 | 2 / 0 | Beşiktaş | — |
| 1982/83 | ogol + RSSSF + Wikipédia | 18 | 306 | 636 | 0 | 2 / 0 | Fenerbahçe | — |
| 1983/84 | ogol + RSSSF + Wikipédia | 18 | 306 | 633 | 0 | 2 / 0 | Trabzonspor | — |
| 1984/85 | ogol + RSSSF + Wikipédia | 18 | 306 | 686 | 0 | 2 / 0 | Fenerbahçe | — |
| 1985/86 | ogol + RSSSF + Wikipédia | 19 | 342 | 808 | 0 | 2 / 0 | Beşiktaş | — |
| 1986/87 | ogol + RSSSF + Wikipédia | 19 | 342 | 776 | 0 | 2 / 0 | Galatasaray | — |
| 1987/88 | ogol + RSSSF + Wikipédia | 20 | 380 | 1032 | 0 | 2 / 0 | Galatasaray | — |
| 1988/89 | ogol + RSSSF + Wikipédia | 19 | 342 | 985 | 0 | 1 / 1 | Fenerbahçe | — |
| 1989/90 | ogol + RSSSF + Wikipédia | 18 | 306 | 819 | 0 | 2 / 0 | Beşiktaş | — |
| 1990/91 | ogol + RSSSF + Wikipédia | 16 | 240 | 672 | 0 | 2 / 0 | Beşiktaş | — |
| 1991/92 | ogol + RSSSF + Wikipédia | 16 | 240 | 677 | 0 | 2 / 0 | Beşiktaş | — |
| 1992/93 | ogol + RSSSF + Wikipédia | 16 | 240 | 716 | 0 | 2 / 0 | Galatasaray | — |
| 1993/94 | ogol + RSSSF + Wikipédia | 16 | 240 | 700 | 0 | 2 / 0 | Galatasaray | — |
| 1994/95 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 945 | 0 | 2 / 0 | Beşiktaş | — |
| 1995/96 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 873 | 0 | 2 / 0 | Fenerbahçe | — |
| 1996/97 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 878 | 0 | 2 / 0 | Galatasaray | — |
| 1997/98 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 861 | 0 | 1 / 0 | Galatasaray | — |
| 1998/99 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 875 | 0 | 1 / 0 | Galatasaray | — |
| 1999/00 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 878 | 0 | 1 / 0 | Galatasaray | — |
| 2000/01 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 1017 | 0 | 1 / 0 | Fenerbahçe | — |
| 2001/02 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 910 | 0 | 1 / 0 | Galatasaray | — |
| 2002/03 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 853 | 0 | 0 / 1 | Beşiktaş | — |
| 2003/04 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 908 | 0 | 1 / 0 | Fenerbahçe | — |
| 2004/05 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 901 | 0 | 1 / 0 | Fenerbahçe | — |
| 2005/06 | ogol + engsoccerdata + football-data + Wikipédia | 18 | 306 | 849 | 0 | 1 / 0 | Galatasaray | — |
| 2006/07 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 736 | 496 | 1 / 0 | Fenerbahçe | — |
| 2007/08 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 786 | 764 | 1 / 0 | Galatasaray | — |
| 2008/09 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 787 | 772 | 1 / 0 | Beşiktaş | — |
| 2009/10 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 764 | 651 | 1 / 0 | Bursaspor | — |
| 2010/11 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 838 | 825 | 1 / 0 | Fenerbahçe | — |
| 2011/12 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 330 | 860 | 56 | 2 / 1 | Galatasaray | — |
| 2012/13 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 817 | 15 | 1 / 0 | Galatasaray | — |
| 2013/14 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 809 | 1 | 1 / 0 | Fenerbahçe | — |
| 2014/15 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 873 | 187 | 1 / 0 | Galatasaray | — |
| 2015/16 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 827 | 751 | 1 / 0 | Beşiktaş | — |
| 2016/17 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 828 | 816 | 0 / 1 | Beşiktaş | — |
| 2017/18 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 906 | 903 | 1 / 0 | Galatasaray | — |
| 2018/19 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 821 | 690 | 1 / 0 | Galatasaray | — |
| 2019/20 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 18 | 306 | 875 | 875 | 1 / 0 | İstanbul Başakşehir | — |
| 2020/21 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 21 | 420 | 1136 | 1119 | 1 / 0 | Beşiktaş | — |
| 2021/22 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 20 | 380 | 1067 | 1067 | 1 / 0 | Trabzonspor | — |
| 2022/23 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 19 | 342 | 1041 | 954 | 1 / 0 | Galatasaray | Kayserispor -3 pontos |
| 2023/24 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 20 | 380 | 1062 | 1056 | 1 / 0 | Galatasaray | Kayserispor -3 pontos; İstanbulspor -3 pontos |
| 2024/25 | ogol + engsoccerdata + football-data + ESPN + Wikipédia | 19 | 342 | 1004 | 1001 | 1 / 0 | Galatasaray | Adana Demirspor -12 pontos |
| 2025/26 | ogol + football-data + ESPN + Wikipédia | 18 | 306 | 812 | 812 | 1 / 0 | Galatasaray | — |

## Conferência e ocorrências, temporada a temporada

### 1924 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Harp Okulu, vice Bahriye — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1927 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Muhafızgücü, vice Altınordu — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1932 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor İstanbulspor, vice Altınordu — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1933 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Fenerbahçe, vice İzmirspor — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1934 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Beşiktaş, vice Altay — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1935 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Fenerbahçe, vice Altınordu — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1937 (Millî Küme)

- Millî Küme: vencedor Fenerbahçe, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1938 (Millî Küme)

- o Fenerbahçe abandonou a liga depois da 4ª rodada; os jogos que faltavam valeram 3-0 e os pontos para os adversários (sem ponto para o Fenerbahçe), e as tabelas contam os gols de outro jeito
- Millî Küme: vencedor Güneş, vice Beşiktaş — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Altay tabela [14, 4, 0, 10, 19, 37] jogos [14, 4, 0, 10, 19, 40]
- tabela (Wikipédia) x jogos — Fenerbahçe tabela [14, 1, 2, 11, 12, 7] jogos [14, 1, 2, 11, 12, 37]
- tabela (RSSSF) x jogos — Altay tabela [14, 4, 0, 10, 19, 37] jogos [14, 4, 0, 10, 19, 40]
- tabela (RSSSF) x jogos — Fenerbahçe tabela [14, 1, 2, 11, 12, 7] jogos [14, 1, 2, 11, 12, 37]

### 1939 (Millî Küme)

- Galatasaray com 35 pontos na RSSSF (36 pela conta 3-2-1): derrota por W.O. não dava ponto
- Millî Küme: vencedor Galatasaray, vice Ankara Demirspor — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Galatasaray tabela [14, 11, 0, 3, 43, 19] jogos [14, 11, 0, 3, 43, 22]
- tabela (RSSSF) x jogos — Galatasaray tabela [14, 11, 0, 3, 43, 19] jogos [14, 11, 0, 3, 43, 22]

### 1940 (Millî Küme)

- Millî Küme: vencedor Fenerbahçe, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (RSSSF) x jogos — Galatasaray tabela [14, 9, 2, 3, 35, 16] jogos [14, 9, 2, 3, 45, 19]

### 1940 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Eskişehir Demirspor, vice Fenerbahçe — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1941 (Millî Küme)

- Millî Küme: vencedor Beşiktaş, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1941 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Gençlerbirliği, vice Beşiktaş — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1942 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Harp Okulu, vice Göztepe — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1943 (Millî Küme)

- Millî Küme: vencedor Fenerbahçe, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1944 (Millî Küme)

- Millî Küme: vencedor Beşiktaş, vice Fenerbahçe — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1944 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Fenerbahçe, vice Harp Okulu — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1945 (Millî Küme)

- Millî Küme: vencedor Fenerbahçe, vice Beşiktaş — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Fenerbahçe tabela [14, 10, 3, 1, 42, 17] jogos [14, 10, 3, 1, 43, 17]
- tabela (Wikipédia) x jogos — Beşiktaş tabela [14, 8, 4, 2, 39, 19] jogos [14, 8, 4, 2, 39, 20]
- tabela (Wikipédia) x jogos — Uçaksavar tabela [14, 5, 5, 4, 24, 30] jogos [14, 5, 2, 7, 24, 30]
- tabela (Wikipédia) x jogos — Altınordu tabela [14, 3, 1, 10, 16, 28] jogos [14, 3, 1, 10, 14, 33]
- tabela (Wikipédia) x jogos — Karşıyaka tabela [14, 1, 4, 9, 14, 33] jogos [14, 1, 4, 9, 13, 41]

### 1945 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Harp Okulu, vice İzmit Harp Filosu — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1946 (Millî Küme)

- duas fases (liga e grupo final de 4); a tabela do grupo final na Wikipédia não traz os gols
- Millî Küme: vencedor Fenerbahçe, vice Beşiktaş — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Beşiktaş tabela [6, 4, 1, 1, None, None] jogos [2, 1, 0, 1, 3, 4]
- tabela (Wikipédia) x jogos — Fenerbahçe tabela [6, 3, 2, 1, None, None] jogos [2, 1, 0, 1, 4, 3]
- tabela (Wikipédia) x jogos — Beşiktaş tabela [10, 7, 2, 1, 32, 15] jogos [10, 7, 1, 2, 32, 15]
- tabela (Wikipédia) x jogos — Kayagücü tabela [10, 3, 2, 5, 19, 28] jogos [10, 4, 1, 5, 19, 28]
- tabela (Wikipédia) x jogos — Muhafızgücü tabela [10, 3, 0, 7, 24, 31] jogos [10, 3, 0, 7, 25, 31]
- tabela (Wikipédia) x jogos — Göztepe tabela [10, 2, 2, 6, 18, 27] jogos [10, 2, 2, 6, 18, 28]

### 1946 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Gençlerbirliği, vice Beşiktaş — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Beşiktaş tabela [3, 2, 0, 1, 6, 5] jogos [3, 1, 0, 2, 6, 15]
- tabela (Wikipédia) x jogos — Altay tabela [3, 0, 0, 3, 2, 10] jogos [3, 1, 0, 2, 12, 10]
- tabela (RSSSF) x jogos — Beşiktaş tabela [3, 2, 0, 1, 6, 5] jogos [3, 1, 0, 2, 6, 15]
- tabela (RSSSF) x jogos — Altay tabela [3, 0, 0, 3, 2, 10] jogos [3, 1, 0, 2, 12, 10]

### 1947 (Millî Küme)

- Millî Küme: vencedor Beşiktaş, vice Fenerbahçe — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- tabela (Wikipédia) x jogos — Vefa tabela [14, 6, 4, 4, 29, 23] jogos [14, 6, 4, 4, 29, 22]
- tabela (Wikipédia) x jogos — Altınordu tabela [14, 2, 2, 10, 18, 38] jogos [14, 2, 2, 10, 17, 38]

### 1947 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Ankara Demirspor, vice Fenerbahçe — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1949 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Ankaragücü, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1950 (Millî Küme)

- Millî Küme: vencedor Fenerbahçe, vice Galatasaray — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1950 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Göztepe, vice Gençlerbirliği — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1951 (Şampiyonası)

- Türkiye Futbol Şampiyonası: vencedor Beşiktaş, vice Altay — título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)

### 1956/57 (Federasyon Kupası)

- Federasyon Kupası: vencedor Beşiktaş, vice Galatasaray
- tabela (Wikipédia) x jogos — Altay tabela [10, 5, 2, 3, 18, 14] jogos [10, 5, 2, 3, 19, 17]
- tabela (Wikipédia) x jogos — Gençlerbirliği tabela [10, 4, 1, 5, 15, 12] jogos [10, 3, 2, 5, 15, 13]
- tabela (Wikipédia) x jogos — Kültürspor tabela [10, 3, 1, 6, 10, 25] jogos [10, 3, 1, 6, 13, 26]
- tabela (Wikipédia) x jogos — Adana Millî Mensucat tabela [10, 0, 1, 9, 5, 28] jogos [10, 0, 2, 8, 6, 28]
- tabela (RSSSF) x jogos — Altay tabela [10, 5, 2, 3, 18, 14] jogos [10, 5, 2, 3, 19, 17]
- tabela (RSSSF) x jogos — Gençlerbirliği tabela [10, 4, 1, 5, 15, 12] jogos [10, 3, 2, 5, 15, 13]
- tabela (RSSSF) x jogos — Kültürspor tabela [10, 3, 1, 6, 10, 25] jogos [10, 3, 1, 6, 13, 26]
- tabela (RSSSF) x jogos — Adana Millî Mensucat tabela [10, 0, 1, 9, 5, 28] jogos [10, 0, 2, 8, 6, 28]

### 1957/58 (Federasyon Kupası)

- Federasyon Kupası: vencedor Beşiktaş, vice Galatasaray

### 1959

- a matriz de resultados da Wikipédia de 1959 difere do ogol em 16 pares (parece ter mandos trocados); o ogol fecha com as tabelas dos grupos, menos 1 gol do Beşiktaş e 1 do Hacettepe na RSSSF
- placar diferente na matriz da Wikipédia — Adalet x Karagümrük: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Ankara Demirspor x Adalet: ogol 2-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Galatasaray x Göztepe: ogol 0-0; Wikipédia 5-0
- placar diferente na matriz da Wikipédia — Galatasaray x Vefa: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Karagümrük: ogol 0-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Göztepe x Galatasaray: ogol 0-5; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Karagümrük x Gençlerbirliği: ogol 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Karşıyaka x Göztepe: ogol 0-3; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Vefa x Galatasaray: ogol 0-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Altay x Beşiktaş: ogol 1-2; Wikipédia 3-1
- placar diferente na matriz da Wikipédia — Ankaragücü x İstanbulspor: ogol 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Beykoz x Beşiktaş: ogol 1-0; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — Beykoz x Hacettepe: ogol 0-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Beykoz x İstanbulspor: ogol 0-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Beykoz x İzmirspor: ogol 2-1; Wikipédia 0-2
- ... e mais 5 pares com placar diferente na matriz da Wikipédia
- tabela do Grupos Grupo Branco (RSSSF) x jogos — Beşiktaş tabela [14, 8, 2, 4, 22, 17, 18] jogos [14, 8, 2, 4, 22, 16, 18]
- tabela do Grupos Grupo Branco (RSSSF) x jogos — Hacettepe tabela [14, 5, 1, 8, 15, 20, 11] jogos [14, 5, 1, 8, 14, 20, 11]

### 1959/60

- o ogol e a matriz da Wikipédia concordam jogo a jogo; as tabelas da RSSSF e da Wikipédia (que a copia) têm 1 ou 2 gols a mais ou a menos em 6 clubes, sem mudar pontos nem posições
- tabela publicada (RSSSF) x jogos — İzmirspor tabela [38, 17, 13, 8, 62, 44, 47] jogos [38, 17, 13, 8, 62, 43, 47]
- tabela publicada (RSSSF) x jogos — İstanbulspor tabela [38, 13, 16, 9, 38, 35, 42] jogos [38, 13, 16, 9, 39, 34, 42]
- tabela publicada (RSSSF) x jogos — Şekerspor tabela [38, 12, 10, 16, 37, 43, 34] jogos [38, 12, 10, 16, 35, 43, 34]
- tabela publicada (RSSSF) x jogos — Göztepe tabela [38, 9, 14, 15, 34, 41, 32] jogos [38, 9, 14, 15, 35, 41, 32]
- tabela publicada (RSSSF) x jogos — Altay tabela [38, 10, 8, 20, 45, 64, 28] jogos [38, 10, 8, 20, 44, 66, 28]
- tabela publicada (RSSSF) x jogos — Altınordu tabela [38, 6, 8, 24, 38, 69, 20] jogos [38, 6, 8, 24, 38, 68, 20]
- tabela publicada (Wikipédia) x jogos — İzmirspor tabela [38, 17, 13, 8, 62, 44, 47] jogos [38, 17, 13, 8, 62, 43, 47]
- tabela publicada (Wikipédia) x jogos — İstanbulspor tabela [38, 13, 16, 9, 38, 35, 42] jogos [38, 13, 16, 9, 39, 34, 42]
- tabela publicada (Wikipédia) x jogos — Şekerspor tabela [38, 12, 10, 16, 37, 43, 34] jogos [38, 12, 10, 16, 35, 43, 34]
- tabela publicada (Wikipédia) x jogos — Göztepe tabela [38, 9, 14, 15, 34, 41, 32] jogos [38, 9, 14, 15, 35, 41, 32]
- tabela publicada (Wikipédia) x jogos — Altay tabela [38, 10, 8, 20, 45, 64, 28] jogos [38, 10, 8, 20, 44, 66, 28]
- tabela publicada (Wikipédia) x jogos — Altınordu tabela [38, 6, 8, 24, 38, 69, 20] jogos [38, 6, 8, 24, 38, 68, 20]

### 1960/61

- a tabela da RSSSF de 1960/61 tem erros em 8 clubes (números de um clube em outro); a da Wikipédia fecha com os jogos, menos os gols contra do Feriköy e os gols do Altınordu (17-31 em vez de 31-53, erro de digitação), e dá a ordem
- placar diferente na matriz da Wikipédia — Altay x Göztepe: ogol 2-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Ankaragücü x Vefa: ogol 0-1; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Galatasaray x Kasımpaşa: ogol 0-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Göztepe x Altay: ogol 1-0; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Göztepe x İzmirspor: ogol 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Göztepe x Karşıyaka: ogol 2-6; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — İzmirspor x Göztepe: ogol 0-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Karagümrük x Kasımpaşa: ogol 1-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Karşıyaka x Göztepe: ogol 0-0; Wikipédia 6-2
- placar diferente na matriz da Wikipédia — Kasımpaşa x Galatasaray: ogol 0-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Kasımpaşa x Göztepe: ogol 0-0; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Kasımpaşa x Karagümrük: ogol 2-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Kasımpaşa x Vefa: ogol 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Vefa x Ankaragücü: ogol 1-2; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Vefa x Kasımpaşa: ogol 1-1; Wikipédia 0-1
- tabela publicada (RSSSF) x jogos — Beşiktaş tabela [38, 22, 11, 5, 60, 26, 55] jogos [38, 22, 11, 5, 61, 26, 55]
- tabela publicada (RSSSF) x jogos — Beykoz tabela [38, 17, 16, 5, 51, 32, 50] jogos [38, 17, 15, 6, 51, 34, 49]
- tabela publicada (RSSSF) x jogos — Gençlerbirliği tabela [38, 15, 13, 10, 52, 41, 43] jogos [38, 16, 13, 9, 54, 39, 45]
- tabela publicada (RSSSF) x jogos — Göztepe tabela [38, 13, 11, 14, 42, 49, 37] jogos [38, 12, 10, 16, 40, 53, 34]
- tabela publicada (RSSSF) x jogos — Vefa tabela [38, 11, 15, 12, 31, 42, 37] jogos [38, 13, 15, 10, 32, 39, 41]
- tabela publicada (RSSSF) x jogos — İstanbulspor tabela [38, 12, 12, 14, 44, 51, 36] jogos [38, 11, 11, 16, 42, 54, 33]
- tabela publicada (RSSSF) x jogos — Kasımpaşa tabela [38, 11, 14, 13, 28, 34, 36] jogos [38, 10, 14, 14, 27, 35, 34]
- tabela publicada (RSSSF) x jogos — Feriköy tabela [38, 10, 14, 14, 30, 39, 34] jogos [38, 11, 13, 14, 32, 38, 35]
- tabela publicada (Wikipédia) x jogos — Feriköy tabela [38, 11, 13, 14, 32, 36, 35] jogos [38, 11, 13, 14, 32, 38, 35]
- tabela publicada (Wikipédia) x jogos — Altınordu tabela [38, 5, 16, 17, 17, 31, 26] jogos [38, 5, 16, 17, 31, 53, 26]

### 1961/62

- placar diferente na matriz da Wikipédia — Altay x İzmir Demirspor: ogol —; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Altınordu x İzmir Demirspor: ogol —; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Ankara Demirspor x İzmir Demirspor: ogol —; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Ankaragücü x Fenerbahçe: ogol 0-3; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Ankaragücü x İzmir Demirspor: ogol —; Wikipédia 4-1
- placar diferente na matriz da Wikipédia — Beşiktaş x İzmir Demirspor: ogol —; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — Beykoz x İzmir Demirspor: ogol —; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Fenerbahçe x Ankaragücü: ogol 1-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Fenerbahçe x İzmir Demirspor: ogol —; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Fenerbahçe x Karagümrük: ogol 1-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Feriköy x İzmir Demirspor: ogol —; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Galatasaray x İzmir Demirspor: ogol —; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Gençlerbirliği x İzmir Demirspor: ogol —; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Göztepe x İzmir Demirspor: ogol —; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Göztepe x Kasımpaşa: ogol 0-0; Wikipédia 1-3
- ... e mais 28 pares com placar diferente na matriz da Wikipédia

### 1962/63

- o ogol tem alguns jogos dos grupos com o mando trocado em relação à matriz da Wikipédia (os totais dos grupos fecham com as tabelas, menos 1 gol do Ankara Demirspor e 1 do Beykoz); no grupo final, as tabelas da RSSSF e da Wikipédia diferem dos jogos em 6 clubes, sem outra fonte para decidir: ficam os jogos do ogol
- o grupo de classificação (7º a 9º de cada grupo) não tem os jogos no ogol nem na Wikipédia: entra a tabela
- placar diferente na matriz da Wikipédia — Altay x Göztepe: ogol —; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Beykoz x Galatasaray: ogol 1-3; Wikipédia 1-3, 1-6
- placar diferente na matriz da Wikipédia — Feriköy x Beykoz: ogol —; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Feriköy x Galatasaray: ogol —; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Ankara Demirspor: ogol 3-1; Wikipédia 0-1, 3-1
- placar diferente na matriz da Wikipédia — Göztepe x Karşıyaka: ogol —; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Karagümrük x Beyoğluspor: ogol —; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Karagümrük x Feriköy: ogol —; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Karagümrük x Galatasaray: ogol —; Wikipédia 1-5
- placar diferente na matriz da Wikipédia — Karşıyaka x Altay: ogol 2-2; Wikipédia 0-1, 2-2
- placar diferente na matriz da Wikipédia — Şekerspor x Ankara Demirspor: ogol —; Wikipédia 2-5
- placar diferente na matriz da Wikipédia — Şekerspor x Gençlerbirliği: ogol —; Wikipédia 1-4
- placar diferente na matriz da Wikipédia — Ankaragücü x Türk Telekomspor: ogol —; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — İstanbulspor x Beşiktaş: ogol 0-2; Wikipédia 0-2, 1-1
- placar diferente na matriz da Wikipédia — İstanbulspor x Fenerbahçe: ogol 0-0; Wikipédia 0-0, 0-2
- ... e mais 13 pares com placar diferente na matriz da Wikipédia
- tabela do Grupos Grupo Vermelho (RSSSF) x jogos — Ankara Demirspor tabela [20, 9, 5, 6, 38, 26, 23] jogos [20, 9, 5, 6, 37, 26, 23]
- tabela do Grupos Grupo Vermelho (RSSSF) x jogos — Beykoz tabela [20, 8, 5, 7, 18, 23, 21] jogos [20, 8, 5, 7, 18, 22, 21]
- tabela do Grupo final (RSSSF) x jogos — Fenerbahçe tabela [22, 11, 6, 5, 33, 19, 28] jogos [22, 10, 6, 6, 31, 19, 26]
- tabela do Grupo final (RSSSF) x jogos — Gençlerbirliği tabela [22, 5, 11, 6, 32, 30, 21] jogos [22, 5, 11, 6, 31, 29, 21]
- tabela do Grupo final (RSSSF) x jogos — Hacettepe tabela [22, 8, 4, 10, 34, 41, 20] jogos [22, 8, 4, 10, 32, 41, 20]
- tabela do Grupo final (RSSSF) x jogos — İzmirspor tabela [22, 7, 6, 9, 27, 38, 20] jogos [22, 7, 6, 9, 28, 39, 20]
- tabela do Grupo final (RSSSF) x jogos — Beykoz tabela [22, 5, 8, 9, 25, 28, 18] jogos [22, 5, 8, 9, 26, 29, 18]
- tabela do Grupo final (RSSSF) x jogos — Karşıyaka tabela [22, 3, 7, 12, 26, 57, 13] jogos [22, 4, 7, 11, 27, 54, 15]
- tabela do Grupos Grupo Vermelho (Wikipédia) x jogos — Ankara Demirspor tabela [20, 9, 5, 6, 38, 26, 23] jogos [20, 9, 5, 6, 37, 26, 23]
- tabela do Grupos Grupo Vermelho (Wikipédia) x jogos — Beykoz tabela [20, 8, 5, 7, 18, 23, 21] jogos [20, 8, 5, 7, 18, 22, 21]
- tabela do Grupo final (Wikipédia) x jogos — Fenerbahçe tabela [22, 11, 6, 5, 33, 19, 28] jogos [22, 10, 6, 6, 31, 19, 26]
- tabela do Grupo final (Wikipédia) x jogos — Gençlerbirliği tabela [22, 5, 11, 6, 32, 30, 21] jogos [22, 5, 11, 6, 31, 29, 21]
- tabela do Grupo final (Wikipédia) x jogos — Hacettepe tabela [22, 8, 4, 10, 34, 41, 20] jogos [22, 8, 4, 10, 32, 41, 20]
- tabela do Grupo final (Wikipédia) x jogos — İzmirspor tabela [22, 7, 6, 9, 27, 38, 20] jogos [22, 7, 6, 9, 28, 39, 20]
- tabela do Grupo final (Wikipédia) x jogos — Beykoz tabela [22, 5, 8, 9, 25, 28, 18] jogos [22, 5, 8, 9, 26, 29, 18]
- tabela do Grupo final (Wikipédia) x jogos — Karşıyaka tabela [22, 3, 7, 12, 26, 57, 13] jogos [22, 4, 7, 11, 27, 54, 15]

### 1963/64

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Beykoz', 'Karşıyaka'])

### 1964/65

- placar diferente na matriz da Wikipédia — Altay x Beykoz: ogol 2-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Altay x İzmirspor: ogol 1-2; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Altınordu x Beykoz: ogol 1-2; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Altınordu x İzmirspor: ogol 1-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Ankara Demirspor x Beykoz: ogol 2-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Ankara Demirspor x İzmirspor: ogol 1-1; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Beşiktaş x Beykoz: ogol 2-1; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Beşiktaş x İzmirspor: ogol 3-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Beykoz x Altay: ogol 2-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Beykoz x Altınordu: ogol 0-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Beykoz x Ankara Demirspor: ogol 4-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Beykoz x Ankaragücü: ogol 3-1; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Beykoz x Beşiktaş: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Beykoz x Fenerbahçe: ogol 0-0; Wikipédia 1-5
- placar diferente na matriz da Wikipédia — Beykoz x Galatasaray: ogol 0-5; Wikipédia 1-2
- ... e mais 39 pares com placar diferente na matriz da Wikipédia

### 1965/66

- Altay (gols pró) e Şekerspor (gols contra): 2 gols a mais nas tabelas que nos jogos do ogol e da matriz
- tabela publicada (RSSSF) x jogos — Altay tabela [30, 10, 8, 12, 28, 28, 28] jogos [30, 10, 8, 12, 26, 28, 28]
- tabela publicada (RSSSF) x jogos — Şekerspor tabela [30, 7, 10, 13, 40, 47, 24] jogos [30, 7, 10, 13, 40, 45, 24]
- tabela publicada (Wikipédia) x jogos — Altay tabela [30, 10, 8, 12, 28, 28, 28] jogos [30, 10, 8, 12, 26, 28, 28]
- tabela publicada (Wikipédia) x jogos — Şekerspor tabela [30, 7, 10, 13, 40, 47, 24] jogos [30, 7, 10, 13, 40, 45, 24]

### 1966/67

- placar diferente na matriz da Wikipédia — Altınordu x Ankaragücü: ogol 1-1; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Ankaragücü x Altınordu: ogol 2-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Ankaragücü x Gençlerbirliği: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Ankaragücü x Göztepe: ogol 0-3; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Feriköy x İstanbulspor: ogol 1-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Ankaragücü: ogol 0-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Göztepe x Ankaragücü: ogol 0-0; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — İstanbulspor x Feriköy: ogol 1-0; Wikipédia 2-1

### 1967/68

- sem ocorrências

### 1968/69

- placar diferente na matriz da Wikipédia — Altınordu x İzmirspor: ogol 2-2; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Ankara Demirspor x Şekerspor: ogol 1-0; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Beşiktaş x Galatasaray: ogol 0-1; Wikipédia 0-2
- placar diferente na matriz da Wikipédia — Fenerbahçe x Vefa: ogol 0-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Galatasaray x Beşiktaş: ogol 2-0; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Şekerspor: ogol 0-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Göztepe x İzmirspor: ogol 1-1; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — İstanbulspor x Vefa: ogol 2-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — İzmirspor x Altınordu: ogol 1-1; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — İzmirspor x Göztepe: ogol 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Türk Telekomspor x Şekerspor: ogol 2-2; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Şekerspor x Ankara Demirspor: ogol 0-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Şekerspor x Gençlerbirliği: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Şekerspor x Türk Telekomspor: ogol 1-1; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Vefa x Fenerbahçe: ogol 0-1; Wikipédia 0-0
- ... e mais 1 pares com placar diferente na matriz da Wikipédia

### 1969/70

- sem ocorrências

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- placar diferente na matriz da Wikipédia — Fenerbahçe x Galatasaray: ogol 1-1; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Galatasaray x Fenerbahçe: ogol 1-0; Wikipédia 1-1

### 1973/74

- sem ocorrências

### 1974/75

- placar diferente na matriz da Wikipédia — Kayseri Erciyesspor x Altay: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Kayseri Erciyesspor x Ankaragücü: ogol 0-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Kayseri Erciyesspor x Boluspor: ogol 1-0; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Kayseri Erciyesspor x Bursaspor: ogol 0-0; Wikipédia 1-0

### 1975/76

- sem ocorrências

### 1976/77

- sem ocorrências

### 1977/78

- Samsunspor e Mersin İdmanyurdu: 1 gol de diferença nas tabelas (o ogol e a matriz concordam)
- tabela publicada (RSSSF) x jogos — Samsunspor tabela [30, 8, 8, 14, 26, 36, 24] jogos [30, 8, 8, 14, 25, 36, 24]
- tabela publicada (RSSSF) x jogos — Mersin İdmanyurdu tabela [30, 3, 15, 12, 18, 34, 21] jogos [30, 3, 15, 12, 19, 34, 21]
- tabela publicada (Wikipédia) x jogos — Samsunspor tabela [30, 8, 8, 14, 26, 36, 24] jogos [30, 8, 8, 14, 25, 36, 24]
- tabela publicada (Wikipédia) x jogos — Mersin İdmanyurdu tabela [30, 3, 15, 12, 18, 34, 21] jogos [30, 3, 15, 12, 19, 34, 21]

### 1978/79

- placar diferente na matriz da Wikipédia — Beşiktaş x Galatasaray: ogol 0-1; Wikipédia 1-3
- placar diferente na matriz da Wikipédia — Diyarbakırspor x Zonguldakspor: ogol 2-0; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Galatasaray x Beşiktaş: ogol 3-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Zonguldakspor x Diyarbakırspor: ogol 0-0; Wikipédia 0-2

### 1979/80

- placar diferente na matriz da Wikipédia — Fenerbahçe x Galatasaray: ogol 1-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Galatasaray x Fenerbahçe: ogol 0-0; Wikipédia 1-1

### 1980/81

- sem ocorrências

### 1981/82

- sem ocorrências

### 1982/83

- placar diferente na matriz da Wikipédia — Sarıyer x Mersin İdmanyurdu: ogol 3-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Sarıyer x Sakaryaspor: ogol 1-1; Wikipédia 3-0
- placar diferente na matriz da Wikipédia — Trabzonspor x Gaziantepspor: ogol 3-0; Wikipédia 3-2

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- placar diferente na matriz da Wikipédia — Diyarbakırspor x Sarıyer: ogol 0-4; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Fenerbahçe x Altay: ogol 2-2; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Fenerbahçe x Ankaragücü: ogol 1-1; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Sarıyer x Samsunspor: ogol 2-3; Wikipédia 3-2

### 1987/88

- placar diferente na matriz da Wikipédia — Galatasaray x Sakaryaspor: ogol 3-1; Wikipédia 3-2

### 1988/89

- a RSSSF separa o Samsunspor em duas linhas: os 18 jogos disputados e os 18 dados por 0-3 depois do acidente; os jogos e a Wikipédia somam os 36
- Samsunspor: 18 jogos marcados `awd` — o ônibus do Samsunspor sofreu um acidente grave em 20/01/1989 e o clube não pôde jogar o resto da temporada: os 18 jogos que faltavam foram dados por 3-0 aos adversários, e o Samsunspor não caiu
- tabela publicada (RSSSF) x jogos — Samsunspor tabela [18, 4, 7, 7, 12, 16, 19] jogos [36, 4, 7, 25, 12, 70, 19]

### 1989/90

- placar diferente na matriz da Wikipédia — Trabzonspor x Adanaspor: ogol 4-1; Wikipédia 4-0

### 1990/91

- placar diferente na matriz da Wikipédia — Galatasaray x Zeytinburnuspor: ogol 2-2; Wikipédia 2-0

### 1991/92

- placar diferente na matriz da Wikipédia — Fenerbahçe x Trabzonspor: ogol 4-1; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Konyaspor x Bakırköyspor: ogol 0-0; Wikipédia 1-4

### 1992/93

- placar diferente na matriz da Wikipédia — Karşıyaka x Beşiktaş: ogol 2-2; Wikipédia 2-1

### 1993/94

- placar diferente na matriz da Wikipédia — Beşiktaş x Galatasaray: ogol 0-1; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Galatasaray x Beşiktaş: ogol 1-1; Wikipédia 1-0

### 1994/95

- placar diferente no engsoccerdata — Gaziantepspor x Gençlerbirliği (1995-03-19): ogol 3-1, engsoccerdata 3-0
- placar diferente no football-data — Gaziantepspor x Gençlerbirliği (1995-03-19): ogol 3-1, football-data 3-0

### 1995/96

- placar diferente no engsoccerdata — Denizlispor x Fenerbahçe (1996-03-17): ogol 0-2, engsoccerdata 0-0
- placar diferente no engsoccerdata — Denizlispor x Gaziantepspor (1996-04-14): ogol 0-1, engsoccerdata 2-3
- placar diferente no engsoccerdata — Galatasaray x Kayseri Erciyesspor (1996-02-11): ogol 5-0, engsoccerdata 4-0
- placar diferente no engsoccerdata — Fenerbahçe x Denizlispor (1995-10-14): ogol 0-0, engsoccerdata 2-0
- placar diferente no engsoccerdata — Gaziantepspor x Denizlispor (1995-11-19): ogol 3-2, engsoccerdata 1-0
- placar diferente no football-data — Denizlispor x Fenerbahçe (1996-03-17): ogol 0-2, football-data 0-0
- placar diferente no football-data — Denizlispor x Gaziantepspor (1996-04-14): ogol 0-1, football-data 2-3
- placar diferente no football-data — Galatasaray x Kayseri Erciyesspor (1996-02-11): ogol 5-0, football-data 4-0
- placar diferente no football-data — Fenerbahçe x Denizlispor (1995-10-14): ogol 0-0, football-data 2-0
- placar diferente no football-data — Gaziantepspor x Denizlispor (1995-11-19): ogol 3-2, football-data 1-0

### 1996/97

- placar diferente na matriz da Wikipédia — Zeytinburnuspor x Ankaragücü: ogol 1-1; Wikipédia 3-2; engsoccerdata 1-1; football-data 1-1
- placar diferente no engsoccerdata — Kocaelispor x Gençlerbirliği (1997-05-11): ogol 3-2, engsoccerdata 3-1
- placar diferente no engsoccerdata — Trabzonspor x Denizlispor (1997-05-11): ogol 3-1, engsoccerdata 2-1
- placar diferente no engsoccerdata — Zeytinburnuspor x İstanbulspor (1997-05-18): ogol 1-2, engsoccerdata 0-2
- placar diferente no football-data — Kocaelispor x Gençlerbirliği (1997-05-11): ogol 3-2, football-data 3-1
- placar diferente no football-data — Trabzonspor x Denizlispor (1997-05-11): ogol 3-1, football-data 2-1
- placar diferente no football-data — Zeytinburnuspor x İstanbulspor (1997-05-18): ogol 1-2, football-data 0-2

### 1997/98

- placar diferente no engsoccerdata — Fenerbahçe x Gaziantepspor (1997-08-02): ogol 3-0, engsoccerdata 1-0
- placar diferente no engsoccerdata — Beşiktaş x Gençlerbirliği (1998-01-24): ogol 3-0, engsoccerdata 3-1
- placar diferente no football-data — Fenerbahçe x Gaziantepspor (1997-08-02): ogol 3-0, football-data 1-0
- placar diferente no football-data — Beşiktaş x Gençlerbirliği (1998-01-24): ogol 3-0, football-data 3-1

### 1998/99

- sem ocorrências

### 1999/00

- Antalyaspor x İstanbulspor (1999-08-08): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2000/01

- Samsunspor x Kocaelispor (2000-10-15): DA no ogol; fica 3-0 pela matriz da Wikipédia

### 2001/02

- Samsunspor x Gençlerbirliği (2001-08-18): placar corrigido para 2-2 (o ogol dá 0-2; football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham)
- Kocaelispor x Samsunspor (2001-11-03): placar corrigido para 0-1 (o ogol dá Samsunspor 0-0 Kocaelispor; football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham)
- Gençlerbirliği x Samsunspor (2002-01-23): placar corrigido para 2-0 (o ogol dá Samsunspor 0-2 Gençlerbirliği (mando invertido); football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham)
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Samsunspor: ogol 2-0; Wikipédia 2-2; engsoccerdata 2-0; football-data 2-0
- placar diferente na matriz da Wikipédia — Samsunspor x Gençlerbirliği: ogol 2-2; Wikipédia 0-2; engsoccerdata 2-2; football-data 2-2

### 2002/03

- İstanbulspor: 1 gol contra a mais na tabela da Wikipédia (o ogol e a matriz concordam)
- tabela publicada (Wikipédia) x jogos — İstanbulspor tabela [34, 12, 7, 15, 42, 48, 43] jogos [34, 12, 7, 15, 42, 47, 43]

### 2003/04

- Çaykur Rizespor x Trabzonspor (2003-09-13): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente no engsoccerdata — Beşiktaş x Samsunspor (2004-01-25): ogol 0-4, engsoccerdata 1-4
- placar diferente no football-data — Beşiktaş x Samsunspor (2004-01-25): ogol 0-4, football-data 1-4

### 2004/05

- placar diferente na matriz da Wikipédia — Beşiktaş x Gençlerbirliği: ogol 0-0; Wikipédia 1-1; engsoccerdata 0-0; football-data 0-0
- placar diferente na matriz da Wikipédia — Beşiktaş x İstanbulspor: ogol 2-1; Wikipédia 0-0; engsoccerdata 2-1; football-data 2-1

### 2005/06

- Diyarbakırspor x Konyaspor (2006-02-26): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Trabzonspor x Diyarbakırspor (2006-04-16): placar corrigido para 3-0 (o ogol dá 2-1; matriz da Wikipédia, football-data e engsoccerdata dão 3-0, e a tabela da Wikipédia fecha)
- Gaziantepspor x Malatyaspor (2006-05-14): placar corrigido para 1-0 (o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão 1-0, e a tabela da Wikipédia fecha)
- Samsunspor x Diyarbakırspor (2006-05-14): placar corrigido para 1-0 (o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão 1-0, e a tabela da Wikipédia fecha)

### 2006/07

- Manisaspor x Sakaryaspor (2007-03-17): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2007/08

- sem ocorrências

### 2008/09

- sem ocorrências

### 2009/10

- Diyarbakırspor x Bursaspor (2010-03-06): WO no ogol; fica 0-3 pela matriz da Wikipédia
- Ankaraspor: 34 jogos marcados `awd` — a federação rebaixou o Ankaraspor em 07/10/2009, com efeito imediato, pela ligação dos dirigentes com os do Ankaragücü; todos os 34 jogos dele valeram 3-0 para os adversários

### 2010/11

- placar diferente na ESPN — İstanbul Başakşehir x Antalyaspor (2011-05-07): ogol 1-1, ESPN 0-1
- placar diferente na ESPN — Kayserispor x Gaziantepspor (2011-05-15): ogol 1-2, ESPN 0-0

### 2011/12

- Trabzonspor x Gaziantepspor (10/02/2012): a matriz e a tabela da Wikipédia dão 4-0; o ogol, o football-data e o engsoccerdata, 4-1: fica 4-1
- placar diferente na matriz da Wikipédia — Ankaragücü x Karabükspor: ogol 2-1; Wikipédia 1-5, 2-1; engsoccerdata 2-1; football-data 2-1
- placar diferente na matriz da Wikipédia — Ankaragücü x Orduspor: ogol 0-2; Wikipédia 0-2, 0-3; engsoccerdata 0-2; football-data 0-2
- placar diferente na matriz da Wikipédia — Ankaragücü x Samsunspor: ogol 0-3; Wikipédia 0-3, 1-0; engsoccerdata 0-3; football-data 0-3
- placar diferente na matriz da Wikipédia — Antalyaspor x Gaziantepspor: ogol 1-0; Wikipédia 1-0, 4-2; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Antalyaspor x Gençlerbirliği: ogol 2-2; Wikipédia 1-3, 2-2; engsoccerdata 2-2; football-data 2-2
- placar diferente na matriz da Wikipédia — Antalyaspor x Kayserispor: ogol 1-0; Wikipédia 1-0, 3-1; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Gaziantepspor x Antalyaspor: ogol 1-0; Wikipédia 1-0, 3-1; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Gaziantepspor x Gençlerbirliği: ogol 3-0; Wikipédia 3-0, 4-0; engsoccerdata 3-0; football-data 3-0
- placar diferente na matriz da Wikipédia — Gaziantepspor x Kayserispor: ogol 1-2; Wikipédia 1-2, 3-2; engsoccerdata 1-2; football-data 1-2
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Antalyaspor: ogol 3-0; Wikipédia 3-0, 3-2; engsoccerdata 3-0; football-data 3-0
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Gaziantepspor: ogol 1-0; Wikipédia 0-2, 1-0; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Gençlerbirliği x Kayserispor: ogol 1-0; Wikipédia 0-1, 1-0; engsoccerdata 1-0; football-data 1-0
- placar diferente na matriz da Wikipédia — Karabükspor x Ankaragücü: ogol 3-2; Wikipédia 3-1, 3-2; engsoccerdata 3-2; football-data 3-2
- placar diferente na matriz da Wikipédia — Karabükspor x Orduspor: ogol 1-2; Wikipédia 1-2, 2-4; engsoccerdata 1-2; football-data 1-2
- placar diferente na matriz da Wikipédia — Karabükspor x Samsunspor: ogol 2-1; Wikipédia 1-1, 2-1; engsoccerdata 2-1; football-data 2-1
- ... e mais 11 pares com placar diferente na matriz da Wikipédia
- placar diferente na ESPN — Eskişehirspor x Beşiktaş (2011-09-10): ogol 2-1, ESPN 1-1
- placar diferente na ESPN — Samsunspor x Gençlerbirliği (2011-09-10): ogol 3-2, ESPN 3-0
- placar diferente na ESPN — Ankaragücü x Mersin İdmanyurdu (2011-09-10): ogol 1-2, ESPN 0-0
- placar diferente na ESPN — Manisaspor x Trabzonspor (2011-09-10): ogol 1-1, ESPN 0-1
- placar diferente na ESPN — Antalyaspor x Gaziantepspor (2011-09-11): ogol 1-0, ESPN 0-0
- placar diferente na ESPN — İstanbul Başakşehir x Galatasaray (2011-09-11): ogol 2-0, ESPN 1-0
- placar diferente na ESPN — Gaziantepspor x Fenerbahçe (2011-09-16): ogol 1-3, ESPN 1-1
- placar diferente na ESPN — Kayserispor x Antalyaspor (2011-09-16): ogol 0-1, ESPN 0-0
- placar diferente na ESPN — Gençlerbirliği x Karabükspor (2011-09-17): ogol 2-1, ESPN 2-0
- placar diferente na ESPN — Trabzonspor x İstanbul Başakşehir (2011-09-17): ogol 0-1, ESPN 0-0
- placar diferente na ESPN — Mersin İdmanyurdu x Bursaspor (2011-09-18): ogol 1-3, ESPN 1-1
- placar diferente na ESPN — Sivasspor x Eskişehirspor (2011-09-18): ogol 0-4, ESPN 0-2
- placar diferente na ESPN — Galatasaray x Samsunspor (2011-09-18): ogol 3-1, ESPN 1-0
- placar diferente na ESPN — Beşiktaş x Ankaragücü (2011-09-19): ogol 3-1, ESPN 1-0
- placar diferente na ESPN — Fenerbahçe x Manisaspor (2011-09-20): ogol 1-1, ESPN 1-0
- placar diferente na ESPN — İstanbul Başakşehir x Orduspor (2011-09-20): ogol 1-1, ESPN 0-1
- placar diferente na ESPN — İstanbul Başakşehir x Karabükspor (2012-02-09): ogol 2-2, ESPN 1-2
- tabela publicada (Wikipédia) x jogos — Trabzonspor tabela [34, 15, 11, 8, 60, 39, 56] jogos [34, 15, 11, 8, 60, 40, 56]
- tabela publicada (Wikipédia) x jogos — Gaziantepspor tabela [34, 13, 9, 12, 39, 33, 48] jogos [34, 13, 9, 12, 40, 33, 48]

### 2012/13

- placar diferente na ESPN — Kasımpaşa x Karabükspor (2012-08-24): ogol 2-1, ESPN 1-1

### 2013/14

- Trabzonspor x Fenerbahçe (2014-03-10): DA no ogol; fica 0-3 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Akhisarspor x Antalyaspor: ogol 0-0; Wikipédia 1-0; engsoccerdata 0-0; football-data 0-0
- placar diferente na matriz da Wikipédia — Akhisarspor x Beşiktaş: ogol 3-3; Wikipédia 2-3; engsoccerdata 3-3; football-data 3-3
- placar diferente na ESPN — Kasımpaşa x Beşiktaş (2014-02-11): ogol 0-3, ESPN 2-1

### 2014/15

- placar diferente na ESPN — Kasımpaşa x Balıkesirspor (2015-05-12): ogol 2-3, ESPN 2-0

### 2015/16

- placar diferente na ESPN — Eskişehirspor x Kayserispor (2015-10-23): ogol 1-3, ESPN 1-2

### 2016/17

- Adanaspor x Kasımpaşa (30/01/2017): a matriz e a tabela da Wikipédia dão 3-0; o ogol, o football-data e o engsoccerdata, 2-0: fica 2-0
- placar diferente na matriz da Wikipédia — Adanaspor x Kasımpaşa: ogol 2-0; Wikipédia 3-0; engsoccerdata 2-0; football-data 2-0
- tabela publicada (Wikipédia) x jogos — Kasımpaşa tabela [34, 12, 7, 15, 46, 50, 43] jogos [34, 12, 7, 15, 46, 49, 43]
- tabela publicada (Wikipédia) x jogos — Adanaspor tabela [34, 6, 7, 21, 33, 62, 25] jogos [34, 6, 7, 21, 32, 62, 25]

### 2017/18

- sem ocorrências

### 2018/19

- placar diferente na matriz da Wikipédia — Akhisarspor x Ankaragücü: ogol 0-0; Wikipédia 1-1; engsoccerdata 0-0; football-data 0-0
- placar diferente no engsoccerdata — Akhisarspor x Beşiktaş (2019-01-18): ogol 0-3, engsoccerdata 1-3
- placar diferente no football-data — Akhisarspor x Beşiktaş (2019-01-18): ogol 0-3, football-data 1-3

### 2019/20

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Kayserispor', 'Ankaragücü'])

### 2020/21

- Alanyaspor x Sivasspor (2021-01-30): SUSP no ogol; fica 3-1 pela matriz da Wikipédia

### 2021/22

- placar diferente na matriz da Wikipédia — Sivasspor x Yeni Malatyaspor: ogol 2-1; Wikipédia 1-2; engsoccerdata 2-1; football-data 2-1

### 2022/23

- Adana Demirspor x Hatayspor (2023-03-05): WO no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Galatasaray (2023-03-05): WO no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Konyaspor (2023-03-12): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Ümraniyespor x Gaziantep FK (2023-03-12): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Trabzonspor (2023-03-19): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Kayserispor x Hatayspor (2023-03-19): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Kasımpaşa (2023-04-02): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Sivasspor (2023-04-02): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Adana Demirspor x Gaziantep FK (2023-04-09): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Alanyaspor x Hatayspor (2023-04-09): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Konyaspor (2023-04-16): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Karagümrük (2023-04-16): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Beşiktaş x Hatayspor (2023-04-19): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Alanyaspor (2023-04-23): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Ankaragücü (2023-04-23): DA no ogol; fica 0-3 pela matriz da Wikipédia
- İstanbul Başakşehir x Hatayspor (2023-04-30): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Kayserispor x Gaziantep FK (2023-04-30): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Karagümrük (2023-05-07): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x İstanbulspor (2023-05-07): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Beşiktaş x Gaziantep FK (2023-05-17): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Giresunspor x Hatayspor (2023-05-17): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x Giresunspor (2023-05-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Fenerbahçe (2023-05-21): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Hatayspor x Ümraniyespor (2023-05-30): DA no ogol; fica 0-3 pela matriz da Wikipédia
- İstanbul Başakşehir x Gaziantep FK (2023-05-30): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Antalyaspor x Hatayspor (2023-06-03): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Gaziantep FK x İstanbulspor (2023-06-03): DA no ogol; fica 0-3 pela matriz da Wikipédia
- Fenerbahçe x Gaziantep FK (2023-06-07): DA no ogol; fica 3-0 pela matriz da Wikipédia
- Hatayspor x Galatasaray (2023-06-07): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2023/24

- İstanbulspor x Trabzonspor (2023-12-19): DA no ogol; fica 0-3 pela matriz da Wikipédia

### 2024/25

- Galatasaray x Adana Demirspor (2025-02-09): DA no ogol; fica 3-0 pela matriz da Wikipédia
- placar diferente na matriz da Wikipédia — Göztepe x Adana Demirspor: ogol 3-1; Wikipédia 3-0; engsoccerdata 3-1; football-data 3-1

### 2025/26

- sem ocorrências

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_tur.py`, pela linhagem legal do clube (como na Wikipédia). Kayseri: o Kayserispor de 1966 (1ª divisão de 1973/74 a 1997/98) trocou de nome, escudo e cores com o Erciyesspor em 2004 e virou o Kayseri Erciyesspor; o Kayserispor de 2004/05 em diante é o antigo Erciyesspor.
- A ESPN é casada por votação jogo a jogo (mesma data e placar): 54 códigos.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Jogos do grupo de classificação de 1962/63:** nem o ogol nem a Wikipédia têm; entra a tabela.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (ficha do ogol, jogo a jogo).
- **Campeonatos anteriores a 1959** (Türkiye Futbol Şampiyonası e Millî Küme): fora do escopo; a federação não os conta.
