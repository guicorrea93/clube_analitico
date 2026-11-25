# Campeonato Costarriquenho (1ª divisão) — coleta de dados

Gerado por `python coleta/crc-1/importar.py`. Pacote em `data/coleta/crc-1/pacote/`.

**Edições:** 123, uma por título, como a contagem oficial da UNAFUT, que a lista de campeões da RSSSF (`coschamp.html`) reproduz. Escopo decidido em 24/11/2026: 1921 a 1985, um campeão por ano (1954 e 1956 não foram disputados; 1961 teve duas entidades rivais, Asofútbol e Federación, e entra com duas edições); 1986/87 a 2006/07, uma por temporada (de 1997/98 em diante, Apertura e Clausura são fases do ano); de 2007/08 em diante, Apertura e Clausura, uma edição cada, até o Clausura 2026 (o Apertura 2026 ainda está em disputa).

**Edições sem jogos (74):** de 1921 a 1995/96 a RSSSF traz quase só as tabelas (a edição entra com elas, com campeão e vice; os poucos jogos de final ficam de fora); 1991/92 e 1993/94 não têm página (só campeão e vice da lista).

**Edições com jogos incompletos (4):** Apertura 2010, Clausura 2011, Apertura 2011 e Clausura 2012: a RSSSF só tem a tabela da fase regular e a fase final; a ESPN desses anos tem jogos adiados repetidos e jogos faltando, e não foi usada.

**Fontes:** RSSSF (`data/coleta/crc-1/rsssf/`) e ESPN (liga `crc.1`: hora, estádio, público, gols com minuto e cartões, casados com os jogos da RSSSF).

**Clubes:** nomes e identidades no começo de `coleta/crc-1/clubes_crc.py` (Carmen FC = Carmelita; Liberia Mía = Municipal Liberia; Municipal Puntarenas e Puntarenas FC separados, como na lista de campeões). Homônimos de clubes de outros países levam a cidade: Santos de Guápiles, Sporting de San José, Uruguay de Coronado.

**Pontos:** 2 por vitória até 1994/95 e 3 a partir de 1995/96.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1921 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos21) |
| 1922 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos22) |
| 1923 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Cartaginés | RSSSF (cos23) |
| 1924 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos24) |
| 1925 | 5 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos25) |
| 1926 | 7 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos26) |
| 1927 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos27) |
| 1928 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos28) |
| 1929 | 4 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos29) |
| 1930 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos30) |
| 1931 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos31) |
| 1932 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos32) |
| 1933 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos33) |
| 1934 | 8 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos34) |
| 1935 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos35) |
| 1936 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Cartaginés | RSSSF (cos36) |
| 1937 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos37) |
| 1938 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Orión | RSSSF (cos38) |
| 1939 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos39) |
| 1940 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Cartaginés | RSSSF (cos40) |
| 1941 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos41) |
| 1942 | 7 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos42) |
| 1943 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Universidad de Costa Rica | RSSSF (cos43) |
| 1944 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Orión | RSSSF (cos44) |
| 1945 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos45) |
| 1946 | 7 | 0 (0) | 0 | 0 | 0 / 0 | La Libertad | RSSSF (cos46) |
| 1947 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos47) |
| 1948 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos48) |
| 1949 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos49) |
| 1950 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos50) |
| 1951 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos51) |
| 1952 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos52) |
| 1953 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos53) |
| 1955 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos55) |
| 1957 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos57) |
| 1958 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos58) |
| 1959 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos59) |
| 1960 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos60) |
| 1961 Asofútbol | 5 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos61) |
| 1961 Federación | 3 | 0 (0) | 0 | 0 | 0 / 0 | Carmelita | RSSSF (cos61) |
| 1962 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos62) |
| 1963 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Uruguay de Coronado | RSSSF (cos63) |
| 1964 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos64) |
| 1965 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos65) |
| 1966 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos66) |
| 1967 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos67) |
| 1968 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos68) |
| 1969 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos69) |
| 1970 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos70) |
| 1971 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1972 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1973 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1974 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1975 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1976 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1977 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1978 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1979 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1980 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos80) |
| 1981 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos81) |
| 1982 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos82) |
| 1983 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos83) |
| 1984 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos84) |
| 1985 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos85) |
| 1986/87 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Municipal Puntarenas | RSSSF (cos86) |
| 1987/88 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | RSSSF (cos87) |
| 1988/89 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos88) |
| 1989/90 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos89) |
| 1990/91 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos91) |
| 1991/92 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1992/93 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Herediano | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1993/94 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1994/95 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Saprissa | RSSSF (cos95) |
| 1995/96 | 28 | 0 (0) | 0 | 0 | 0 / 0 | Alajuelense | RSSSF (cos96) |
| 1996/97 | 12 | 224 (224) | 562 | 8 | 0 / 0 | Alajuelense | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997/98 | 12 | 222 (318) | 592 | 4 | 3 / 0 | Saprissa | RSSSF (cos98) |
| 1998/99 | 14 | 266 (266) | 779 | 0 | 0 / 1 | Saprissa | RSSSF (cos99) |
| 1999/00 | 12 | 264 (264) | 791 | 0 | 2 / 0 | Alajuelense | RSSSF (cos00) |
| 2000/01 | 12 | 230 (230) | 640 | 4 | 5 / 1 | Alajuelense | RSSSF (cos01) |
| 2001/02 | 12 | 267 (266) | 792 | 8 | 2 / 0 | Alajuelense | RSSSF (cos02) |
| 2002/03 | 12 | 264 (264) | 759 | 0 | 1 / 1 | Alajuelense | RSSSF (cos03) |
| 2003/04 | 12 | 265 (266) | 702 | 7 | 1 / 1 | Saprissa | RSSSF (cos04) |
| 2004/05 | 12 | 204 (204) | 561 | 20 | 4 / 0 | Alajuelense | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005/06 | 12 | 204 (204) | 492 | 490 | 4 / 0 | Saprissa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006/07 | 12 | 220 (220) | 540 | 160 | 4 / 0 | Saprissa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Apertura | 12 | 106 (106) | 278 | 163 | 2 / 0 | Saprissa | RSSSF (cos08) |
| 2008 Clausura | 12 | 106 (106) | 258 | 117 | 2 / 0 | Saprissa | RSSSF (cos08) |
| 2008 Apertura | 12 | 106 (106) | 308 | 193 | 2 / 0 | Saprissa | RSSSF (cos09) |
| 2009 Clausura | 12 | 107 (107) | 240 | 144 | 2 / 0 | Municipal Liberia | RSSSF (cos09) |
| 2009 Apertura | 12 | 106 (106) | 249 | 148 | 2 / 0 | Brujas de Escazú | RSSSF (cos2010) |
| 2010 Clausura | 12 | 106 (106) | 231 | 146 | 2 / 0 | Saprissa | RSSSF (cos2010) |
| 2010 Apertura | 12 | 14 (14) | 38 | 17 | 0 / 0 | Alajuelense | RSSSF (cos2011) |
| 2011 Clausura | 12 | 14 (14) | 38 | 28 | 0 / 0 | Alajuelense | RSSSF (cos2011) |
| 2011 Apertura | 11 | 6 (6) | 13 | 2 | 0 / 0 | Alajuelense | RSSSF (cos2012) |
| 2012 Clausura | 11 | 6 (6) | 15 | 0 | 0 / 0 | Herediano | RSSSF (cos2012) |
| 2012 Apertura | 12 | 138 (138) | 367 | 4 | 1 / 0 | Alajuelense | RSSSF (cos2013) |
| 2013 Clausura | 12 | 138 (138) | 380 | 1 | 1 / 0 | Herediano | RSSSF (cos2013) |
| 2013 Apertura | 12 | 138 (138) | 364 | 37 | 1 / 0 | Alajuelense | RSSSF (cos2014) |
| 2014 Clausura | 12 | 138 (138) | 374 | 6 | 1 / 0 | Saprissa | RSSSF (cos2014) |
| 2014 Apertura | 12 | 138 (138) | 367 | 7 | 1 / 0 | Saprissa | RSSSF (cos2015) |
| 2015 Clausura | 12 | 138 (138) | 374 | 0 | 1 / 0 | Herediano | RSSSF (cos2015) |
| 2015 Apertura | 12 | 138 (138) | 376 | 309 | 1 / 0 | Saprissa | RSSSF (cos2016) |
| 2016 Clausura | 12 | 138 (138) | 333 | 190 | 1 / 0 | Herediano | RSSSF (cos2016) |
| 2016 Apertura | 12 | 144 (144) | 398 | 249 | 2 / 0 | Saprissa | RSSSF (cos2017) |
| 2017 Clausura | 12 | 146 (146) | 389 | 208 | 2 / 0 | Herediano | RSSSF (cos2017) |
| 2017 Apertura | 12 | 146 (146) | 426 | 281 | 2 / 0 | Pérez Zeledón | RSSSF (cos2018) |
| 2018 Clausura | 12 | 146 (146) | 390 | 0 | 2 / 0 | Saprissa | RSSSF (cos2018) |
| 2018 Apertura | 12 | 140 (140) | 413 | 0 | 1 / 0 | Herediano | RSSSF (cos2019) |
| 2019 Clausura | 12 | 138 (138) | 385 | 0 | 1 / 0 | San Carlos | RSSSF (cos2019) |
| 2019 Apertura | 12 | 140 (140) | 405 | 0 | 1 / 0 | Herediano | RSSSF (cos2020) |
| 2020 Clausura | 12 | 138 (137) | 408 | 0 | 1 / 0 | Saprissa | RSSSF (cos2020) |
| 2020 Apertura | 12 | 104 (104) | 275 | 0 | 2 / 0 | Alajuelense | RSSSF (cos2021) |
| 2021 Clausura | 12 | 140 (140) | 361 | 0 | 1 / 0 | Saprissa | RSSSF (cos2021) |
| 2021 Apertura | 12 | 140 (140) | 377 | 0 | 1 / 0 | Herediano | RSSSF (cos2022) |
| 2022 Clausura | 12 | 140 (140) | 376 | 0 | 1 / 0 | Cartaginés | RSSSF (cos2022) |
| 2022 Apertura | 12 | 104 (104) | 292 | 0 | 2 / 0 | Saprissa | RSSSF (cos2023) |
| 2023 Clausura | 12 | 140 (140) | 400 | 0 | 1 / 0 | Saprissa | RSSSF (cos2023) |
| 2023 Apertura | 12 | 138 (138) | 383 | 0 | 1 / 0 | Saprissa | RSSSF (cos2024) |
| 2024 Clausura | 12 | 138 (138) | 353 | 0 | 1 / 0 | Saprissa | RSSSF (cos2024) |
| 2024 Apertura | 12 | 140 (140) | 378 | 0 | 1 / 0 | Herediano | RSSSF (cos2025) |
| 2025 Clausura | 12 | 140 (140) | 312 | 0 | 1 / 0 | Herediano | RSSSF (cos2025) |
| 2025 Apertura | 10 | 96 (96) | 235 | 0 | 2 / 0 | Alajuelense | RSSSF (cos2026) |
| 2026 Clausura | 10 | 96 (96) | 239 | 0 | 1 / 0 | Herediano | RSSSF (cos2026) |

## Conferência e correções, edição a edição

### 1921

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1922

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1923

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1924

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1925

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1926

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1927

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1928

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1929

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1930

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1931

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1932

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1933

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1934

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1935

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1936

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1937

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1938

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1939

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1940

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1941

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1942

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1943

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1944

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1945

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1946

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1947

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1948

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1949

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1950

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1951

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1952

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1953

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1955

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1957

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1958

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1959

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1960

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1961 Asofútbol

- campeonato da Asociación de Fútbol (os clubes rebeldes), paralelo ao da Federación; só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1961 Federación

- campeonato da Federación (3 clubes); o título do Carmelita foi reconhecido pela UNAFUT em 2003; só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1962

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1963

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1964

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1965

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1966

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1967

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1968

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1969

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1970

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1971

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1972

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1973

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1974

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1975

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1976

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1977

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1978

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1979

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1980

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1981

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1982

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1983

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1984

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1985

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1986/87

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1987/88

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1988/89

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1989/90

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1990/91

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1991/92

- sem página da RSSSF: só o campeão e o vice da lista

### 1992/93

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1993/94

- sem página da RSSSF: só o campeão e o vice da lista

### 1994/95

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1995/96

- só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- tabela publicada x jogos — cos99:464: Saprissa tabela [44, 29, 12, 3, 108, 37] jogos [44, 28, 13, 3, 108, 37] — a diferença vem de San Carlos x Saprissa (1998-12-02), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — cos99:464: San Carlos tabela [44, 8, 15, 21, 52, 87] jogos [44, 8, 16, 20, 52, 87] — a diferença vem de San Carlos x Saprissa (1998-12-02), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — San Carlos Saprissa (1998-12-02): awarded 0-0 to Saprissa

### 1999/00

- corrigido — San Carlos x Limonense (1999-11-17): San Carlos x Limonense interrompido em 17/10 (1-0, mau tempo) e jogado de novo: 1-1, o placar que vale (a tabela conta o jogo); o San Carlos x Limonense da linha 442 é o do 2º turno, não a repetição

### 2000/01

- tabela publicada x jogos — cos01:19: Osa tabela [22, 4, 9, 9, 24, 36] jogos [22, 3, 9, 10, 19, 37] — a outra tabela publicada (cos01) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — cos01:19: Limonense tabela [22, 5, 3, 14, 30, 35] jogos [22, 6, 3, 13, 31, 30] — a outra tabela publicada (cos01) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Osa 5-1 Limonense (2000-09-10): temporarily awarded 0-2 due to Osa fielding Evance

### 2001/02

- abandonado/suspenso, sem valer — Santos de Guápiles Saprissa (2001-11-25): abandoned at 1-0

### 2002/03

- San Carlos x Herediano (21ª rodada do Clausura) foi dado como derrota sem gols para os dois clubes; o banco não tem como registrar isso no jogo (fica sem placar), e a tabela publicada conta uma derrota a mais para cada um
- tabela publicada x jogos — cos03:267: Herediano tabela [22, 12, 3, 7, 49, 22] jogos [21, 12, 3, 6, 49, 22] — a outra tabela publicada (cos03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — cos03:267: San Carlos tabela [22, 4, 8, 10, 18, 24] jogos [21, 4, 8, 9, 18, 24] — a outra tabela publicada (cos03) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Herediano Osa (s/d): awarded 5-0, originally 5-3
- decidido fora de campo — Guanacasteca Saprissa (s/d): awarded 2-0, originally 2-2
- decidido fora de campo — Carmelita Santos de Guápiles (s/d): awarded 1-0, originally 1-1
- decidido fora de campo — San Carlos Herediano (s/d): awarded goalless loss to both teams;
- decidido fora de campo — Pérez Zeledón Municipal Liberia (s/d): awarded 2-0, originally 2-1

### 2003/04

- falta um Pérez Zeledón x Carmelita no Apertura (a página só tem o jogo de ida, 3-0); pela tabela, a volta foi empate 1-1
- tabela publicada x jogos — cos04:19: Pérez Zeledón tabela [22, 8, 5, 9, 28, 26] jogos [21, 8, 4, 9, 27, 25] — a outra tabela publicada (cos04) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — cos04:19: Carmelita tabela [22, 6, 5, 11, 25, 30] jogos [21, 6, 4, 11, 24, 29] — a outra tabela publicada (cos04) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Alajuelense Cartaginés (2003-09-17): awarded 3-0; abandoned at 1-1 in 34'

### 2004/05

- decidido fora de campo — Brujas de Escazú Belén (2005-02-12): awarded 3-0, originally 2-2

### 2005/06

- sem ocorrências

### 2006/07

- ESPN: 144 jogos casados

### 2007 Apertura

- ESPN: 70 jogos casados
- decidido fora de campo — Cartaginés Brujas de Escazú (2007-07-29): awarded 3-0, originally 1-1

### 2008 Clausura

- ESPN: 51 jogos casados

### 2008 Apertura

- ESPN: 72 jogos casados

### 2009 Clausura

- ESPN: 66 jogos casados
- abandonado/suspenso, sem valer — Ramonense Herediano (2009-05-06): abandoned at 0-0 at half-time due

### 2009 Apertura

- ESPN: 66 jogos casados

### 2010 Clausura

- ESPN: 71 jogos casados

### 2010 Apertura

- ESPN: 10 jogos casados
- decidido fora de campo — Santos de Guápiles Barrio México (s/d): awarded 3-0
- decidido fora de campo — Barrio México Santos de Guápiles (2010-11-20): awarded 0-3

### 2011 Clausura

- ESPN: 11 jogos casados

### 2011 Apertura

- ESPN: 6 jogos casados

### 2012 Clausura

- ESPN: 5 jogos casados

### 2012 Apertura

- ESPN: 135 jogos casados

### 2013 Clausura

- ESPN: 137 jogos casados

### 2013 Apertura

- ESPN: 135 jogos casados

### 2014 Clausura

- ESPN: 136 jogos casados

### 2014 Apertura

- ESPN: 137 jogos casados

### 2015 Clausura

- ESPN: 135 jogos casados
- decidido fora de campo — Limón FC Carmelita (2015-01-18): awarded 0-3

### 2015 Apertura

- ESPN: 138 jogos casados

### 2016 Clausura

- ESPN: 135 jogos casados
- decidido fora de campo — Pérez Zeledón Santos de Guápiles (2016-01-16): awarded 3-0; Santos suspended for debts
- decidido fora de campo — Santos de Guápiles Saprissa (2016-01-24): awarded 0-3; Santos suspended for debts
- decidido fora de campo — Cartaginés Santos de Guápiles (2016-01-27): awarded 3-0; Santos suspended for debts

### 2016 Apertura

- ESPN: 143 jogos casados

### 2017 Clausura

- ESPN: 146 jogos casados

### 2017 Apertura

- ESPN: 145 jogos casados

### 2018 Clausura

- ESPN: 145 jogos casados

### 2018 Apertura

- ESPN: 136 jogos casados

### 2019 Clausura

- ESPN: 138 jogos casados

### 2019 Apertura

- ESPN: 136 jogos casados

### 2020 Clausura

- ESPN: 135 jogos casados
- decidido fora de campo — Guadalupe Grecia (2020-02-08): awarded 3-0; Grecia suspended because of licensing problems
- decidido fora de campo — Grecia Limón FC (2020-02-12): awarded 0-3; Grecia suspended because of licensing problems
- decidido fora de campo — Grecia Saprissa (2020-02-15): awarded 0-3; Grecia suspended because of licensing problems
- não jogado — Santos de Guápiles Limón FC (2020-06-10): not played due to health concerns in Pococí region

### 2020 Apertura

- ESPN: 104 jogos casados

### 2021 Clausura

- ESPN: 140 jogos casados
- decidido fora de campo — Guadalupe Limón FC (2021-01-12): awarded 3-0

### 2021 Apertura

- ESPN: 137 jogos casados

### 2022 Clausura

- ESPN: 134 jogos casados
- decidido fora de campo — San Carlos Alajuelense (2022-03-06): awarded 0-3, originally 1-1

### 2022 Apertura

- ESPN: 100 jogos casados

### 2023 Clausura

- ESPN: 136 jogos casados

### 2023 Apertura

- ESPN: 138 jogos casados

### 2024 Clausura

- ESPN: 138 jogos casados

### 2024 Apertura

- ESPN: 138 jogos casados
- decidido fora de campo — Guanacasteca San Carlos (2024-07-19): awarded 0-3; not played as Guanacasteca

### 2025 Clausura

- ESPN: 134 jogos casados
- decidido fora de campo — Cartaginés Guanacasteca (2025-04-20): awarded 3-0
- decidido fora de campo — Guanacasteca Sporting de San José (2025-04-26): awarded 0-3
- decidido fora de campo — Saprissa Guanacasteca (2025-05-04): awarded 3-0
- decidido fora de campo — San Carlos Santos de Guápiles (2025-05-07): awarded 3-0
- decidido fora de campo — Guanacasteca Herediano (2025-05-07): awarded 0-3

### 2025 Apertura

- ESPN: 96 jogos casados

### 2026 Clausura

- ESPN: 96 jogos casados

