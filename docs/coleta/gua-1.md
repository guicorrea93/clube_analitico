# Campeonato Guatemalteco (Liga Nacional) — coleta de dados

Gerado por `python coleta/gua-1/importar.py`. Pacote em `data/coleta/gua-1/pacote/`.

**Edições:** 101, uma por título, como a lista de campeões da RSSSF (`guatchamp.html`, 100 títulos desde 1942) e a contagem oficial (Municipal 33, Comunicaciones 32). Escopo decidido em 24/11/2026: só o Campeonato de Liga (Liga Nacional), de 1942/43 em diante; a Liga Capitalina / Liga Mayor (1919-1941, liga da capital) fica fora. Um campeão por temporada até 1998/99 (os anos sem campeonato não têm edição); Apertura e Clausura de 1999/00 em diante, uma edição cada (em 2001 o primeiro torneio foi o Reordenamiento); o Clausura 2020 (pandemia) entra sem campeão.

**Edições sem jogos (48):** de 1942/43 a 1995/96 (a RSSSF quase só tem as tabelas) e do Apertura 2010 ao Clausura 2012 (a página só tem as tabelas e a fase final). A lista de campeões não traz o vice: o vice é o 2º da classificação.

**Fontes:** RSSSF (`data/coleta/gua-1/rsssf/`; os arquivos têm nomes irregulares e o casamento com a temporada é pelo título da página) e ESPN (liga `gua.1`).

**Clubes:** nomes e identidades no começo de `coleta/gua-1/clubes_gua.py`. Homônimos de clubes de outros países levam o país: Aurora de Guatemala, Hércules de Guatemala, Racing de Guatemala, España de Guatemala, América de Guatemala, Eureka de Guatemala.

**Pontos:** 2 ou 3 por vitória conforme a tabela publicada de cada temporada.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1942/43 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat42) |
| 1943 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Tipografía Nacional | RSSSF (guat43) |
| 1944/45 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Tipografía Nacional | RSSSF (guat45) |
| 1947 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat47) |
| 1950/51 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat51) |
| 1952/53 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Tipografía Nacional | RSSSF (guat53) |
| 1954/55 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat55) |
| 1956 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat56) |
| 1957/58 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat58) |
| 1959/60 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat60) |
| 1961/62 | 24 | 0 (0) | 0 | 0 | 0 / 0 | Xelajú MC | RSSSF (guat62) |
| 1963/64 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat63) |
| 1964 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat64) |
| 1965/66 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat65) |
| 1966 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat66) |
| 1967/68 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat68) |
| 1968/69 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat69) |
| 1969/70 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat70) |
| 1970/71 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat71a) |
| 1971 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat71) |
| 1972 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat72) |
| 1973 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat73) |
| 1974 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat74) |
| 1975 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat75) |
| 1976 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat76) |
| 1977 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat77) |
| 1978 | 19 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat78) |
| 1979/80 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat79) |
| 1980 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Xelajú MC | RSSSF (guat80) |
| 1981 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat81) |
| 1982 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat82) |
| 1983 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Suchitepéquez | RSSSF (guat83) |
| 1984 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat84) |
| 1985/86 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat85) |
| 1986 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat86) |
| 1987 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat87) |
| 1988/89 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat89) |
| 1989/90 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat90) |
| 1990/91 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat91) |
| 1991/92 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat92) |
| 1992/93 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Aurora de Guatemala | RSSSF (guat93) |
| 1993/94 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat94) |
| 1994/95 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat95) |
| 1995/96 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Xelajú MC | RSSSF (guat96) |
| 1996/97 | 13 | 164 (164) | 419 | 2 | 1 / 1 | Comunicaciones | RSSSF (guat97) |
| 1997/98 | 12 | 162 (162) | 417 | 0 | 2 / 0 | Comunicaciones | RSSSF (guat98) |
| 1998/99 | 15 | 220 (220) | 598 | 0 | 2 / 0 | Comunicaciones | RSSSF (guat99) |
| 1999 Apertura | 12 | 145 (146) | 402 | 0 | 0 / 1 | Comunicaciones | RSSSF (guat00) |
| 2000 Clausura | 12 | 146 (146) | 417 | 0 | 1 / 0 | Municipal | RSSSF (guat00) |
| 2000 Apertura | 12 | 146 (146) | 414 | 0 | 0 / 1 | Municipal | RSSSF (guat01) |
| 2001 Clausura | 12 | 147 (146) | 431 | 9 | 1 / 0 | Comunicaciones | RSSSF (guat01) |
| 2001 Reordenamiento | 12 | 146 (146) | 420 | 0 | 1 / 0 | Municipal | RSSSF (guat02) |
| 2002 Clausura | 10 | 100 (100) | 327 | 5 | 1 / 0 | Municipal | RSSSF (guat02) |
| 2002 Apertura | 10 | 100 (100) | 269 | 5 | 1 / 0 | Comunicaciones | RSSSF (guat03) |
| 2003 Clausura | 10 | 100 (100) | 269 | 5 | 1 / 0 | Comunicaciones | RSSSF (guat03) |
| 2003 Apertura | 10 | 100 (100) | 291 | 0 | 1 / 0 | Municipal | RSSSF (guat04) |
| 2004 Clausura | 10 | 100 (100) | 335 | 9 | 1 / 0 | Cobán Imperial | RSSSF (guat04) |
| 2004 Apertura | 10 | 100 (100) | 319 | 11 | 1 / 0 | Municipal | RSSSF (guat05) |
| 2005 Clausura | 10 | 100 (100) | 264 | 7 | 1 / 0 | Municipal | RSSSF (guat05) |
| 2005 Apertura | 10 | 100 (100) | 274 | 0 | 1 / 0 | Municipal | RSSSF (guat06) |
| 2006 Clausura | 10 | 100 (100) | 255 | 0 | 1 / 0 | Municipal | RSSSF (guat06) |
| 2006 Apertura | 10 | 100 (100) | 275 | 234 | 1 / 0 | Municipal | RSSSF (guat07) |
| 2007 Clausura | 10 | 100 (100) | 287 | 0 | 1 / 0 | Xelajú MC | RSSSF (guat07) |
| 2007 Apertura | 10 | 100 (100) | 263 | 204 | 1 / 0 | Jalapa | RSSSF (guat08) |
| 2008 Clausura | 10 | 100 (100) | 243 | 172 | 1 / 0 | Municipal | RSSSF (guat08) |
| 2008 Apertura | 10 | 100 (100) | 261 | 247 | 1 / 0 | Comunicaciones | RSSSF (guat09) |
| 2009 Clausura | 10 | 100 (100) | 239 | 228 | 0 / 0 | Jalapa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 12 | 142 (142) | 358 | 329 | 1 / 0 | Municipal | RSSSF (guat2010) |
| 2010 Clausura | 12 | 142 (142) | 350 | 241 | 1 / 0 | Municipal | RSSSF (guat2010) |
| 2010 Apertura | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat2011) |
| 2011 Clausura | 12 | 0 (0) | 0 | 0 | 0 / 0 | Comunicaciones | RSSSF (guat2011) |
| 2011 Apertura | 12 | 0 (0) | 0 | 0 | 0 / 0 | Municipal | RSSSF (guat2012) |
| 2012 Clausura | 12 | 0 (0) | 0 | 0 | 0 / 0 | Xelajú MC | RSSSF (guat2012) |
| 2012 Apertura | 12 | 146 (146) | 420 | 0 | 1 / 0 | Comunicaciones | RSSSF (guat2013) |
| 2013 Clausura | 12 | 146 (146) | 370 | 1 | 1 / 0 | Comunicaciones | RSSSF (guat2013) |
| 2013 Apertura | 12 | 146 (146) | 370 | 45 | 1 / 0 | Comunicaciones | RSSSF (guat2014) |
| 2014 Clausura | 12 | 146 (146) | 384 | 1 | 1 / 0 | Comunicaciones | RSSSF (guat2014) |
| 2014 Apertura | 12 | 142 (142) | 345 | 0 | 1 / 0 | Comunicaciones | RSSSF (guat2015) |
| 2015 Clausura | 12 | 143 (142) | 340 | 6 | 1 / 0 | Comunicaciones | RSSSF (guat2015) |
| 2015 Apertura | 12 | 142 (142) | 351 | 298 | 1 / 0 | Antigua GFC | RSSSF (guat2016) |
| 2016 Clausura | 12 | 142 (142) | 364 | 268 | 1 / 0 | Suchitepéquez | RSSSF (guat2016) |
| 2016 Apertura | 12 | 142 (142) | 332 | 224 | 1 / 0 | Antigua GFC | RSSSF (guat2017) |
| 2017 Clausura | 12 | 142 (142) | 271 | 160 | 1 / 0 | Municipal | RSSSF (guat2017) |
| 2017 Apertura | 12 | 142 (142) | 340 | 268 | 1 / 0 | Antigua GFC | RSSSF (guat2018) |
| 2018 Clausura | 12 | 142 (142) | 353 | 0 | 1 / 0 | Guastatoya | RSSSF (guat2018) |
| 2018 Apertura | 12 | 142 (142) | 339 | 0 | 1 / 0 | Guastatoya | RSSSF (guat2019) |
| 2019 Clausura | 12 | 142 (142) | 336 | 0 | 1 / 0 | Antigua GFC | RSSSF (guat2019) |
| 2019 Apertura | 12 | 142 (142) | 345 | 0 | 1 / 0 | Municipal | RSSSF (guat2020) |
| 2020 Clausura | 12 | 78 (78) | 176 | 0 | 0 / 0 | None | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2020 Apertura | 12 | 110 (110) | 276 | 0 | 2 / 0 | Guastatoya | RSSSF (guat2021) |
| 2021 Clausura | 12 | 111 (111) | 260 | 11 | 2 / 0 | Santa Lucía Cotzumalguapa | RSSSF (guat2021) |
| 2021 Apertura | 12 | 146 (146) | 318 | 0 | 1 / 0 | Malacateco | RSSSF (guat2022) |
| 2022 Clausura | 12 | 146 (146) | 357 | 0 | 1 / 0 | Comunicaciones | RSSSF (guat2022) |
| 2022 Apertura | 12 | 146 (146) | 359 | 0 | 1 / 0 | Cobán Imperial | RSSSF (guat2023) |
| 2023 Clausura | 12 | 146 (146) | 360 | 0 | 1 / 0 | Xelajú MC | RSSSF (guat2023) |
| 2023 Apertura | 12 | 110 (110) | 280 | 0 | 1 / 0 | Comunicaciones | RSSSF (guat2024) |
| 2024 Clausura | 12 | 110 (110) | 262 | 1 | 1 / 0 | Municipal | RSSSF (guat2024) |
| 2024 Apertura | 12 | 110 (110) | 254 | 0 | 1 / 0 | Xelajú MC | RSSSF (guat2025) |
| 2025 Clausura | 11 | 124 (124) | 297 | 0 | 1 / 0 | Antigua GFC | RSSSF (guat2025) |
| 2025 Apertura | 12 | 146 (146) | 351 | 0 | 1 / 0 | Antigua GFC | RSSSF (guat2026) |
| 2026 Clausura | 12 | 146 (146) | 355 | 0 | 1 / 0 | Municipal | RSSSF (guat2026) |

## Conferência e correções, edição a edição

### 1942/43

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1943

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1944/45

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1947

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1950/51

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1952/53

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1954/55

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1956

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1957/58

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1959/60

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1961/62

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1963/64

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1964

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1965/66

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1966

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1967/68

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1968/69

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1969/70

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1970/71

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1971

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1972

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1973

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1974

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1975

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1976

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1977

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1978

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1979/80

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1980

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1981

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1982

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1983

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1984

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1985/86

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1986

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1987

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

- tabela publicada x jogos — guat97:16: Azucareros tabela [22, 7, 9, 6, 25, 19] jogos [21, 7, 8, 6, 24, 18] — a outra tabela publicada (guat97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — guat97:16: Sacachispas tabela [22, 4, 7, 11, 13, 30] jogos [22, 4, 7, 11, 14, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1997/98

- sem ocorrências

### 1998/99

- tabela guat99:319 fora da conferência: tabela acumulada (fase regular + grupo do rebaixamento); a página dá parte dos jogos do grupo do rebaixamento só com o resultado ("home win", "draw"), sem placar
- tabela guat99:380 fora da conferência: a mesma tabela acumulada, repetida no fim (fase regular + grupo do rebaixamento); a página dá parte dos jogos do grupo do rebaixamento só com o resultado ("home win", "draw"), sem placar
- decidido fora de campo — Cobán Imperial Zacapa (s/d): awarded 0-3, originally 4-1

### 1999 Apertura

- tabela publicada x jogos — guat00:17: Cobán Imperial tabela [22, 7, 8, 7, 27, 27] jogos [21, 7, 8, 6, 27, 27] — a diferença vem de Cobán Imperial x Sacachispas (1999-08-01), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — guat00:17: Sacachispas tabela [22, 7, 6, 9, 21, 35] jogos [21, 6, 6, 9, 21, 35] — a diferença vem de Cobán Imperial x Sacachispas (1999-08-01), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Cobán Imperial Sacachispas (1999-08-01): awarded 3-0

### 2000 Clausura

- decidido fora de campo — Santa Lucía Cotzumalguapa Sacachispas (2000-01-23): awarded 0-3; orginally 4-3;

### 2000 Apertura

- tabela publicada x jogos — guat01:17: Zacapa tabela [22, 8, 8, 6, 36, 30] jogos [22, 8, 8, 6, 35, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2001 Clausura

- abandonado/suspenso, sem valer — USAC Aurora de Guatemala (2001-04-07): abandoned at 0-0 in 33' when Universidad fans

### 2001 Reordenamiento

- sem ocorrências

### 2002 Clausura

- decidido fora de campo — Cobán Imperial Zacapa (2002-02-17): awarded 0-1; originally 5-1 but Coban

### 2002 Apertura

- decidido fora de campo — Xelajú MC Cobán Imperial (2002-08-04): awarded 0-3; originally 2-1 but

### 2003 Clausura

- decidido fora de campo — Zacapa Aurora de Guatemala (2003-01-26): awarded 0-3; originally 0-1
- decidido fora de campo — Municipal Antigua GFC (2003-04-30): awarded 0-3; originally 2-0;
- decidido fora de campo — Comunicaciones Municipal (2003-04-27): awarded 3-0; abandoned after 5'

### 2003 Apertura

- decidido fora de campo — Jalapa Zacapa (2003-09-07): awarded 3-0; abandoned at 1-1 in
- decidido fora de campo — Zacapa Antigua GFC (2003-09-21): awarded 0-3; originally 3-2

### 2004 Clausura

- sem ocorrências

### 2004 Apertura

- sem ocorrências

### 2005 Clausura

- sem ocorrências

### 2005 Apertura

- sem ocorrências

### 2006 Clausura

- sem ocorrências

### 2006 Apertura

- ESPN: 96 jogos casados
- decidido fora de campo — Suchitepéquez Comunicaciones (2006-10-01): awarded 0-3; abandoned at 1-1 in

### 2007 Clausura

- ESPN: 99 jogos casados

### 2007 Apertura

- ESPN: 83 jogos casados

### 2008 Clausura

- ESPN: 75 jogos casados

### 2008 Apertura

- ESPN: 98 jogos casados

### 2009 Clausura

- ESPN: 98 jogos casados
- decidido fora de campo — Zacapa Comunicaciones (2009-05-17): awarded 0-3; abandoned at 1-2

### 2009 Apertura

- ESPN: 131 jogos casados

### 2010 Clausura

- ESPN: 106 jogos casados

### 2010 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Apertura

- ESPN: 84 jogos casados

### 2013 Clausura

- ESPN: 135 jogos casados

### 2013 Apertura

- ESPN: 137 jogos casados

### 2014 Clausura

- ESPN: 138 jogos casados

### 2014 Apertura

- ESPN: 128 jogos casados

### 2015 Clausura

- ESPN: 131 jogos casados
- abandonado/suspenso, sem valer — Marquense Antigua GFC (2015-04-18): abandoned at 0-0 in 3' due to fog

### 2015 Apertura

- ESPN: 139 jogos casados

### 2016 Clausura

- ESPN: 135 jogos casados

### 2016 Apertura

- ESPN: 142 jogos casados

### 2017 Clausura

- ESPN: 142 jogos casados

### 2017 Apertura

- ESPN: 141 jogos casados

### 2018 Clausura

- ESPN: 142 jogos casados

### 2018 Apertura

- ESPN: 142 jogos casados
- decidido fora de campo — Cobán Imperial Guastatoya (2018-12-05): awarded 0-3; abandoned at 0-0 in 85'

### 2019 Clausura

- ESPN: 142 jogos casados
- decidido fora de campo — Sanarate Siquinalá (2019-02-03): awarded 0-3; originally 1-0, Sanarate

### 2019 Apertura

- ESPN: 142 jogos casados

### 2020 Clausura

- ESPN: 78 jogos casados
- decidido fora de campo — Sanarate Mixco (2020-03-08): awarded 0-3; originally 2-1; Sanarate
- decidido fora de campo — Antigua GFC Sanarate (2020-03-15): awarded 3-0; originally 2-1; Sanarate

### 2020 Apertura

- ESPN: 100 jogos casados

### 2021 Clausura

- ESPN: 110 jogos casados
- abandonado/suspenso, sem valer — Santa Lucía Cotzumalguapa Guastatoya (2021-05-13): abandoned at 1-0 at half-time due to

### 2021 Apertura

- ESPN: 145 jogos casados

### 2022 Clausura

- ESPN: 146 jogos casados
- decidido fora de campo — Achuapa Antigua GFC (2022-03-13): awarded 3-0, originally 1-1

### 2022 Apertura

- ESPN: 146 jogos casados

### 2023 Clausura

- ESPN: 146 jogos casados
- decidido fora de campo — Malacateco Xelajú MC (2023-04-16): awarded 0-3; originally 1-1

### 2023 Apertura

- ESPN: 109 jogos casados

### 2024 Clausura

- ESPN: 109 jogos casados
- decidido fora de campo — Municipal Mixco (2024-02-03): awarded 0-3; originally 0-0,

### 2024 Apertura

- ESPN: 109 jogos casados
- decidido fora de campo — Xinabajul Cobán Imperial (2024-08-04): awarded 0-3, Xinabajul forfeited

### 2025 Clausura

- ESPN: 124 jogos casados
- decidido fora de campo — Marquense Xinabajul (2025-01-18): awarded 0-3; originally 2-0

### 2025 Apertura

- ESPN: 146 jogos casados
- decidido fora de campo — Xelajú MC Municipal (2025-11-02): awarded 0-3, originally 1-1

### 2026 Clausura

- ESPN: 143 jogos casados

