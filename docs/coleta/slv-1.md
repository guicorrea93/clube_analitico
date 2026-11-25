# Campeonato Salvadorenho (Primera División) — coleta de dados

Gerado por `python coleta/slv-1/importar.py`. Pacote em `data/coleta/slv-1/pacote/`.

**Edições:** 111, uma por título, como a lista de campeões da RSSSF (`elsalchamp.html`, 110 títulos desde 1926), que é a contagem da imprensa salvadorenha (FAS 20, Alianza 18, Águila 17). Escopo decidido em 24/11/2026: de 1926 a 1946 os nove campeonatos nacionais oficiais (final, ou quadrangular, entre os campeões das zonas); ficam fora 1924 e 1925 (torneios da Semana Deportiva que a RSSSF chama de não oficiais), os títulos só da Zona Central (1931-36, 1939-41 e 1944-45, que a tradição às vezes conta como nacionais), 1947 (parou depois de duas rodadas, sem tabela) e a Copa Pilsener 1998/99 (não é título oficial). Um campeão por temporada de 1948/49 a 1998/99 (em 1998/99, o Clausura); Apertura e Clausura de 1999/00 em diante, uma edição cada; o Clausura 2023 (cancelado nas quartas de final depois da tragédia no estádio Cuscatlán) entra sem campeão.

**Edições sem jogos (52):** 1942, 1943 e 1946 (quadrangulares só com a tabela), de 1948/49 a 1995/96 (a RSSSF só tem as tabelas e as finais) e do Apertura 2010 ao Clausura 2012 (a página só tem as tabelas e a fase final). O vice é o da lista de campeões.

**Fontes:** RSSSF (`data/coleta/slv-1/rsssf/`: a lista de campeões, a página de tabelas finais e as páginas das temporadas, casadas pelo título) e ESPN (liga `slv.1`).

**Clubes:** nomes e identidades no começo de `coleta/slv-1/clubes_slv.py`. Homônimos de clubes de outros países levam o país ou a cidade: Hércules de El Salvador, Libertad de El Salvador, España de El Salvador, Atlante de El Salvador, Internacional de El Salvador, Excélsior de Santa Ana, Platense de Zacatecoluca, Independiente de San Vicente, Alianza, Leones, Once Deportivo, San Luis, Santa Clara e Tiburones "de El Salvador".

**Pontos:** 2 ou 3 por vitória conforme a tabela publicada de cada temporada.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1926 | 2 | 1 (1) | 3 | 0 | 0 / 0 | Chinameca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1927 | 2 | 1 (1) | 3 | 0 | 0 / 0 | Hércules de El Salvador | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1928 | 2 | 2 (2) | 4 | 0 | 0 / 0 | Hércules de El Salvador | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1929/30 | 2 | 3 (3) | 6 | 0 | 0 / 0 | Hércules de El Salvador | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1937 | 4 | 4 (4) | 21 | 0 | 0 / 0 | CD 33 | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1938 | 4 | 4 (4) | 27 | 0 | 0 / 0 | CD 33 | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1942 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Quequeisque | RSSSF (elsalhist) |
| 1943 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Quequeisque | RSSSF (elsalhist) |
| 1946 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Libertad de El Salvador | RSSSF (elsalhist) |
| 1948/49 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Once Municipal | RSSSF (elsalhist) |
| 1950/51 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Dragón | RSSSF (elsalhist) |
| 1951/52 | 8 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1952/53 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Dragón | RSSSF (elsalhist) |
| 1953/54 | 8 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1955 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1955/56 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1956/57 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1957/58 | 11 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1959 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1960/61 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1961/62 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1962 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1963/64 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1964 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1965/66 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsalhist) |
| 1966/67 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsalhist) |
| 1967/68 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1968/69 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1970 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1971 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Juventud Olímpica | RSSSF (elsalhist) |
| 1972 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1973 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Juventud Olímpica | RSSSF (elsalhist) |
| 1974/75 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Platense de Zacatecoluca | RSSSF (elsalhist) |
| 1975/76 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1976/77 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1977/78 | 12 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1978/79 | 13 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1979/80 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Santiagueño | RSSSF (elsalhist) |
| 1980/81 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1981 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1982 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1983 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1984 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsalhist) |
| 1985 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Marte | RSSSF (elsalhist) |
| 1986/87 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsal87) |
| 1987/88 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsalhist) |
| 1988/89 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Luis Ángel Firpo | RSSSF (elsal89) |
| 1989/90 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsalhist) |
| 1990/91 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Luis Ángel Firpo | RSSSF (elsal91) |
| 1991/92 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Luis Ángel Firpo | RSSSF (elsal92) |
| 1992/93 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Luis Ángel Firpo | RSSSF (elsal93) |
| 1993/94 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsal94) |
| 1994/95 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsal95) |
| 1995/96 | 10 | 0 (0) | 0 | 0 | 0 / 0 | FAS | RSSSF (elsal96) |
| 1996/97 | 10 | 193 (193) | 602 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal97) |
| 1997/98 | 10 | 132 (132) | 360 | 0 | 3 / 0 | Luis Ángel Firpo | RSSSF (elsal98) |
| 1998/99 | 10 | 95 (95) | 245 | 3 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal99) |
| 1999 Apertura | 10 | 95 (95) | 216 | 1 | 1 / 0 | Águila | RSSSF (elsal00) |
| 2000 Clausura | 10 | 95 (95) | 249 | 12 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal00) |
| 2000 Apertura | 10 | 96 (95) | 306 | 5 | 1 / 0 | Águila | RSSSF (elsal01) |
| 2001 Clausura | 10 | 94 (94) | 257 | 0 | 1 / 0 | Águila | RSSSF (elsal01) |
| 2001 Apertura | 10 | 95 (95) | 302 | 3 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal02) |
| 2002 Clausura | 10 | 96 (96) | 285 | 4 | 0 / 1 | FAS | RSSSF (elsal02) |
| 2002 Apertura | 10 | 96 (96) | 252 | 4 | 1 / 0 | FAS | RSSSF (elsal03) |
| 2003 Clausura | 10 | 95 (95) | 258 | 3 | 1 / 0 | San Salvador FC | RSSSF (elsal03) |
| 2003 Apertura | 10 | 96 (96) | 257 | 11 | 1 / 0 | FAS | RSSSF (elsal04) |
| 2004 Clausura | 10 | 95 (95) | 257 | 2 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal04) |
| 2004 Apertura | 10 | 96 (96) | 239 | 14 | 1 / 0 | FAS | RSSSF (elsal05) |
| 2005 Clausura | 10 | 95 (95) | 259 | 3 | 1 / 0 | FAS | RSSSF (elsal05) |
| 2005 Apertura | 10 | 95 (95) | 241 | 33 | 1 / 0 | Vista Hermosa | RSSSF (elsal06) |
| 2006 Clausura | 10 | 95 (95) | 257 | 151 | 1 / 0 | Águila | RSSSF (elsal06) |
| 2006 Apertura | 10 | 96 (96) | 254 | 189 | 1 / 0 | Once Municipal | RSSSF (elsal07) |
| 2007 Clausura | 10 | 95 (95) | 245 | 1 | 1 / 0 | Isidro Metapán | RSSSF (elsal07) |
| 2007 Apertura | 10 | 96 (96) | 252 | 185 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal08) |
| 2008 Clausura | 10 | 95 (95) | 243 | 89 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal08) |
| 2008 Apertura | 10 | 95 (95) | 261 | 192 | 1 / 0 | Isidro Metapán | RSSSF (elsal09) |
| 2009 Clausura | 10 | 95 (95) | 220 | 168 | 0 / 0 | Isidro Metapán | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 10 | 97 (96) | 232 | 210 | 1 / 0 | FAS | RSSSF (elsal2010) |
| 2010 Clausura | 10 | 95 (95) | 226 | 165 | 1 / 0 | Isidro Metapán | RSSSF (elsal2010) |
| 2010 Apertura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Isidro Metapán | RSSSF (elsal2011) |
| 2011 Clausura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Alianza de El Salvador | RSSSF (elsal2011) |
| 2011 Apertura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Isidro Metapán | RSSSF (elsal2012) |
| 2012 Clausura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Águila | RSSSF (elsal2012) |
| 2012 Apertura | 10 | 95 (95) | 282 | 2 | 1 / 0 | Isidro Metapán | RSSSF (elsal2013) |
| 2013 Clausura | 10 | 96 (96) | 233 | 5 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal2013) |
| 2013 Apertura | 10 | 96 (96) | 245 | 10 | 1 / 0 | Isidro Metapán | RSSSF (elsal2014) |
| 2014 Clausura | 10 | 96 (96) | 251 | 120 | 1 / 0 | Isidro Metapán | RSSSF (elsal2014) |
| 2014 Apertura | 10 | 96 (95) | 191 | 0 | 1 / 0 | Isidro Metapán | RSSSF (elsal2015) |
| 2015 Clausura | 10 | 96 (96) | 234 | 17 | 1 / 0 | Santa Tecla FC | RSSSF (elsal2015) |
| 2015 Apertura | 12 | 145 (145) | 361 | 245 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2016) |
| 2016 Clausura | 12 | 145 (145) | 352 | 203 | 1 / 0 | Dragón | RSSSF (elsal2016) |
| 2016 Apertura | 12 | 145 (145) | 385 | 220 | 1 / 0 | Santa Tecla FC | RSSSF (elsal2017) |
| 2017 Clausura | 12 | 145 (145) | 362 | 172 | 1 / 0 | Santa Tecla FC | RSSSF (elsal2017) |
| 2017 Apertura | 12 | 145 (145) | 390 | 240 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2018) |
| 2018 Clausura | 12 | 145 (145) | 357 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2018) |
| 2018 Apertura | 12 | 145 (145) | 359 | 0 | 1 / 0 | Santa Tecla FC | RSSSF (elsal2019) |
| 2019 Clausura | 12 | 145 (145) | 326 | 0 | 1 / 0 | Águila | RSSSF (elsal2019) |
| 2019 Apertura | 12 | 141 (141) | 372 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2020) |
| 2020 Clausura | 12 | 66 (66) | 132 | 0 | 1 / 0 | Once Deportivo de El Salvador | RSSSF (elsal2020) |
| 2020 Apertura | 12 | 110 (110) | 272 | 0 | 5 / 0 | Alianza de El Salvador | RSSSF (elsal2021) |
| 2021 Clausura | 12 | 109 (109) | 271 | 0 | 5 / 0 | FAS | RSSSF (elsal2021) |
| 2021 Apertura | 12 | 145 (145) | 380 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2022) |
| 2022 Clausura | 12 | 145 (145) | 334 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2022) |
| 2022 Apertura | 12 | 73 (73) | 180 | 0 | 2 / 0 | FAS | RSSSF (elsal2023) |
| 2023 Clausura | 12 | 140 (140) | 324 | 0 | 1 / 0 | None | RSSSF (elsal2023) |
| 2023 Apertura | 12 | 146 (145) | 388 | 0 | 1 / 0 | Águila | RSSSF (elsal2024) |
| 2024 Clausura | 12 | 145 (145) | 364 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2024) |
| 2024 Apertura | 11 | 123 (123) | 286 | 0 | 1 / 0 | Once Deportivo de El Salvador | RSSSF (elsal2025) |
| 2025 Clausura | 11 | 123 (123) | 265 | 0 | 1 / 0 | Alianza de El Salvador | RSSSF (elsal2025) |
| 2025 Apertura | 12 | 146 (145) | 396 | 0 | 1 / 0 | Luis Ángel Firpo | RSSSF (elsal2026) |
| 2026 Clausura | 12 | 146 (146) | 374 | 0 | 1 / 0 | FAS | RSSSF (elsal2026) |

## Conferência e correções, edição a edição

### 1926

- final entre os campeões das zonas (Semana Deportiva até 1929/30)

### 1927

- final entre os campeões das zonas (Semana Deportiva até 1929/30)

### 1928

- final entre os campeões das zonas (Semana Deportiva até 1929/30)

### 1929/30

- final entre os campeões das zonas (Semana Deportiva até 1929/30)
- não jogado — Hércules de El Salvador Excélsior de Santa Ana (s/d)

### 1937

- final entre os campeões das zonas (Semana Deportiva até 1929/30)

### 1938

- final entre os campeões das zonas (Semana Deportiva até 1929/30)

### 1942

- quadrangular entre os campeões das zonas: a RSSSF só tem a tabela

### 1943

- quadrangular entre os campeões das zonas: a RSSSF só tem a tabela

### 1946

- quadrangular entre os campeões das zonas: a RSSSF só tem a tabela

### 1948/49

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1950/51

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1951/52

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1952/53

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1953/54

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1955

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1955/56

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1956/57

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1957/58

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1959

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1960/61

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1961/62

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1962

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1963/64

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1964

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1965/66

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1966/67

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1967/68

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1968/69

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1970

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1971

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1972

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1973

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1974/75

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1975/76

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1976/77

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1977/78

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1978/79

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1979/80

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1980/81

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1981

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1982

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1983

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1984

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1985

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1986/87

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1987/88

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1988/89

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1989/90

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1990/91

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1991/92

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1992/93

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1993/94

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1994/95

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1995/96

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1996/97

- o repechaje Municipal Limeño x Real Independiente (vaga na 1ª divisão, contra clube da 2ª) fica fora

### 1997/98

- sem ocorrências

### 1998/99

- só o Clausura ("Copa Clima"), que deu o título; a Copa Pilsener (Apertura) não é título oficial

### 1999 Apertura

- sem ocorrências

### 2000 Clausura

- sem ocorrências

### 2000 Apertura

- abandonado/suspenso, sem valer — Águila Atlético Marte (2000-09-07): abandoned at 1-1 in 70' replay, date not known (end Nov, early Dec)

### 2001 Clausura

- sem ocorrências

### 2001 Apertura

- sem ocorrências

### 2002 Clausura

- Atlético Balboa: os jogos da página somam 25 gols sofridos, a tabela publicada diz 24 (um placar da página ou a tabela tem um gol a mais; fica como a página)
- tabela publicada x jogos — elsal02:189: Atlético Balboa tabela [18, 5, 7, 6, 19, 24] jogos [18, 5, 7, 6, 19, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2002 Apertura

- sem ocorrências

### 2003 Clausura

- sem ocorrências

### 2003 Apertura

- sem ocorrências

### 2004 Clausura

- sem ocorrências

### 2004 Apertura

- sem ocorrências

### 2005 Clausura

- sem ocorrências

### 2005 Apertura

- sem ocorrências

### 2006 Clausura

- decidido fora de campo — Águila Alianza de El Salvador (2006-03-04): awarded 0-2; abandoned at 0-0 in 83'

### 2006 Apertura

- ESPN: 77 jogos casados

### 2007 Clausura

- ESPN: 73 jogos casados

### 2007 Apertura

- ESPN: 71 jogos casados

### 2008 Clausura

- ESPN: 77 jogos casados

### 2008 Apertura

- ESPN: 73 jogos casados
- decidido fora de campo — Nejapa FC Luis Ángel Firpo (2008-11-30): awarded 0-2; match abandoned at 0-0

### 2009 Clausura

- ESPN: 71 jogos casados

### 2009 Apertura

- ESPN: 89 jogos casados
- abandonado/suspenso, sem valer — Águila Alianza de El Salvador (2009-10-17): abandoned at 1-0 at half-time

### 2010 Clausura

- ESPN: 79 jogos casados

### 2010 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Apertura

- ESPN: 77 jogos casados

### 2013 Clausura

- ESPN: 70 jogos casados

### 2013 Apertura

- ESPN: 94 jogos casados

### 2014 Clausura

- ESPN: 94 jogos casados
- decidido fora de campo — Alianza de El Salvador Águila (2014-04-02): awarded 2-0, originally 1-2, Águila

### 2014 Apertura

- ESPN: 93 jogos casados
- abandonado/suspenso, sem valer — FAS Alianza de El Salvador (2014-08-16): abandoned at 0-0 at half-time due to rain

### 2015 Clausura

- ESPN: 88 jogos casados

### 2015 Apertura

- ESPN: 145 jogos casados

### 2016 Clausura

- ESPN: 143 jogos casados

### 2016 Apertura

- ESPN: 144 jogos casados
- decidido fora de campo — Isidro Metapán Chalatenango (2016-10-01): awarded 0-2; originally 2-1, Isidro-Metapán

### 2017 Clausura

- ESPN: 140 jogos casados

### 2017 Apertura

- ESPN: 143 jogos casados
- decidido fora de campo — Luis Ángel Firpo Chalatenango (2017-10-21): awarded 0-2; match not played as Firpo

### 2018 Clausura

- ESPN: 143 jogos casados

### 2018 Apertura

- ESPN: 145 jogos casados

### 2019 Clausura

- ESPN: 145 jogos casados
- decidido fora de campo — Audaz Isidro Metapán (2019-01-13): awarded 0-2

### 2019 Apertura

- ESPN: 141 jogos casados
- decidido fora de campo — Isidro Metapán Municipal Limeño (2019-11-23): awarded 0-2

### 2020 Clausura

- ESPN: 65 jogos casados

### 2020 Apertura

- ESPN: 84 jogos casados
- abandonado/suspenso, sem valer — Luis Ángel Firpo Águila (2020-10-25): abandoned at 1-0 at start of second half

### 2021 Clausura

- ESPN: 109 jogos casados

### 2021 Apertura

- ESPN: 144 jogos casados
- decidido fora de campo — Luis Ángel Firpo Santa Tecla FC (2021-09-19): awarded 0-2; originally 0-0, LA Firpo used

### 2022 Clausura

- ESPN: 145 jogos casados

### 2022 Apertura

- as duas rodadas de julho foram anuladas (campeonato parado pela investigação contra a federação e recomeçado em setembro): ficam fora, com a tabela do momento da parada
- ESPN: 73 jogos casados

### 2023 Clausura

- ESPN: 138 jogos casados
- abandonado/suspenso, sem valer — Alianza de El Salvador FAS (2023-05-20): abandoned at 0-0 in 20' due to a stampede in
- não jogado — Águila Jocoro (2023-05-20)
- não jogado — Once Deportivo de El Salvador Isidro Metapán (2023-05-20)

### 2023 Apertura

- ESPN: 145 jogos casados
- abandonado/suspenso, sem valer — Municipal Limeño FAS (2023-09-20): abandoned at 1-2 at half-time due to heavy rain

### 2024 Clausura

- ESPN: 145 jogos casados
- decidido fora de campo — Jocoro Santa Tecla FC (2024-03-16): awarded 0-2; match not played due

### 2024 Apertura

- ESPN: 123 jogos casados

### 2025 Clausura

- ESPN: 122 jogos casados

### 2025 Apertura

- ESPN: 136 jogos casados
- abandonado/suspenso, sem valer — Cacahuatique Inter FA (2025-09-28): abandoned at 0-0 at half-time due to heavy rain

### 2026 Clausura

- ESPN: 144 jogos casados
- abandonado/suspenso, sem valer — Isidro Metapán Luis Ángel Firpo (2026-05-06): abandoned at 0-1 at half-time due to power cut

