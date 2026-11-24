# Campeonato Hondurenho (Liga Nacional) — coleta de dados

Gerado por `python coleta/hon-1/importar.py`. Pacote em `data/coleta/hon-1/pacote/`.

**Edições:** 89, uma por título, como a lista de campeões da RSSSF (`hondchamp.html`, 87 títulos da Liga Nacional). Escopo decidido em 24/11/2026, depois de pesquisa a pedido do Guilherme: só a Liga Nacional, de 1965/66 em diante, como a liga conta. Um campeão por temporada até 1996/97 (1972/73 foi abandonada e entra sem campeão); Apertura e Clausura de 1997/98 em diante, uma edição cada, com o torneio único de 1999; o Clausura 2020 (pandemia) entra sem campeão. A Liga Amateur de Honduras (1947-1964) fica fora: era um mata-mata entre campeões regionais, a RSSSF a lista à parte e a liga e a FENAFUTH não reconhecem esses títulos.

**Edições sem jogos (35):** de 1965/66 a 1995/96 (a RSSSF só tem as tabelas finais, `hondhist.html`) e as edições de 2010/11 e 2011/12 em que a página só tem as tabelas e a fase final.

**Fontes:** RSSSF (`data/coleta/hon-1/rsssf/`) e ESPN (liga `hon.1`: hora, estádio, público, gols com minuto e cartões, casados com os jogos da RSSSF).

**Clubes:** nomes e identidades no começo de `coleta/hon-1/clubes_hon.py` (La Salle = San Pedro; Honduras = Honduras Progreso; Atlético Olanchano e Olancho FC separados). Homônimos de clubes de outros países levam a cidade ou o país: Olimpia de Tegucigalpa, Necaxa de Tegucigalpa, Real Sociedad de Tocoa, Palestino de Honduras, Independiente de Honduras, Progreso de Honduras, Atlético Español de Honduras, Platense de Puerto Cortés, San Pedro de Honduras, Atlántida de La Ceiba.

**Pontos:** 2 por vitória até 1993/94 e 3 a partir de 1994/95.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1965/66 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Platense de Puerto Cortés | RSSSF (hondhist) |
| 1966/67 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1967/68 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1968/69 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hondhist) |
| 1969/70 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1970/71 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hondhist) |
| 1971/72 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1972/73 | 10 | 0 (0) | 0 | 0 | 0 / 0 | None | RSSSF (hondhist) |
| 1973 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hondhist) |
| 1974 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1975 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1976 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1977 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1978/79 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hondhist) |
| 1979 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Marathón | RSSSF (hondhist) |
| 1980 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1981 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Vida | RSSSF (hondhist) |
| 1982 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1983 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Vida | RSSSF (hondhist) |
| 1984 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1985 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Marathón | RSSSF (hondhist) |
| 1986 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1987 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1988 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1989/90 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1990/91 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1991/92 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hondhist) |
| 1992/93 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hondhist) |
| 1993/94 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hondhist) |
| 1994/95 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Victoria | RSSSF (hondhist) |
| 1995/96 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hond96) |
| 1996/97 | 10 | 150 (150) | 315 | 9 | 2 / 0 | Olimpia de Tegucigalpa | RSSSF (hond97) |
| 1997 Apertura | 11 | 122 (122) | 340 | 8 | 0 / 1 | Motagua | RSSSF (hond98) |
| 1998 Clausura | 11 | 123 (123) | 336 | 1 | 0 / 0 | Motagua | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 | 10 | 102 (102) | 237 | 3 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond99) |
| 1999 Apertura | 10 | 102 (102) | 243 | 0 | 1 / 0 | Motagua | RSSSF (hond00) |
| 2000 Clausura | 10 | 98 (98) | 253 | 0 | 1 / 0 | Motagua | RSSSF (hond00) |
| 2000 Apertura | 10 | 102 (102) | 254 | 3 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond01) |
| 2001 Clausura | 10 | 102 (102) | 258 | 3 | 1 / 0 | Platense de Puerto Cortés | RSSSF (hond01) |
| 2001 Apertura | 10 | 96 (96) | 239 | 6 | 1 / 0 | Motagua | RSSSF (hond02) |
| 2002 Clausura | 10 | 96 (96) | 219 | 1 | 0 / 1 | Marathón | RSSSF (hond02) |
| 2002 Apertura | 10 | 97 (96) | 233 | 5 | 0 / 1 | Olimpia de Tegucigalpa | RSSSF (hond03) |
| 2003 Clausura | 10 | 96 (96) | 218 | 1 | 1 / 0 | Marathón | RSSSF (hond03) |
| 2003 Apertura | 10 | 96 (96) | 252 | 3 | 1 / 0 | Real España | RSSSF (hond04) |
| 2004 Clausura | 9 | 78 (78) | 207 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond04) |
| 2004 Apertura | 10 | 96 (96) | 257 | 0 | 1 / 0 | Marathón | RSSSF (hond05) |
| 2005 Clausura | 10 | 96 (96) | 202 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond05) |
| 2005 Apertura | 10 | 96 (96) | 256 | 0 | 0 / 1 | Olimpia de Tegucigalpa | RSSSF (hond06) |
| 2006 Clausura | 10 | 96 (96) | 223 | 92 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond06) |
| 2006 Apertura | 10 | 96 (96) | 256 | 234 | 1 / 0 | Motagua | RSSSF (hond07) |
| 2007 Clausura | 10 | 97 (94) | 226 | 2 | 0 / 1 | Real España | RSSSF (hond07) |
| 2007 Apertura | 10 | 96 (96) | 211 | 193 | 1 / 0 | Marathón | RSSSF (hond08) |
| 2008 Clausura | 10 | 96 (96) | 243 | 133 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond08) |
| 2008 Apertura | 10 | 96 (96) | 237 | 216 | 1 / 0 | Marathón | RSSSF (hond09) |
| 2009 Clausura | 10 | 96 (95) | 229 | 188 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond09) |
| 2009 Apertura | 10 | 96 (96) | 246 | 210 | 1 / 0 | Marathón | RSSSF (hond2010) |
| 2010 Clausura | 10 | 96 (96) | 241 | 232 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2010) |
| 2010 Apertura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Real España | RSSSF (hond2011) |
| 2011 Clausura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Motagua | RSSSF (hond2011) |
| 2011 Apertura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2012) |
| 2012 Clausura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2012) |
| 2012 Apertura | 10 | 100 (100) | 241 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2013) |
| 2013 Clausura | 10 | 100 (100) | 250 | 15 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2013) |
| 2013 Apertura | 10 | 100 (100) | 292 | 51 | 1 / 0 | Real España | RSSSF (hond2014) |
| 2014 Clausura | 10 | 100 (100) | 238 | 6 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2014) |
| 2014 Apertura | 10 | 100 (100) | 301 | 13 | 1 / 0 | Motagua | RSSSF (hond2015) |
| 2015 Clausura | 10 | 100 (100) | 280 | 22 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2015) |
| 2015 Apertura | 10 | 100 (100) | 275 | 192 | 1 / 0 | Honduras Progreso | RSSSF (hond2016) |
| 2016 Clausura | 10 | 100 (100) | 269 | 186 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2016) |
| 2016 Apertura | 10 | 100 (100) | 274 | 181 | 1 / 0 | Motagua | RSSSF (hond2017) |
| 2017 Clausura | 10 | 100 (100) | 294 | 126 | 1 / 0 | Motagua | RSSSF (hond2017) |
| 2017 Apertura | 10 | 100 (100) | 296 | 194 | 1 / 0 | Real España | RSSSF (hond2018) |
| 2018 Clausura | 10 | 100 (100) | 249 | 0 | 1 / 0 | Marathón | RSSSF (hond2018) |
| 2018 Apertura | 10 | 100 (100) | 262 | 0 | 1 / 0 | Motagua | RSSSF (hond2019) |
| 2019 Clausura | 10 | 100 (100) | 254 | 0 | 1 / 0 | Motagua | RSSSF (hond2019) |
| 2019 Apertura | 10 | 100 (100) | 290 | 0 | 2 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2020) |
| 2020 Clausura | 10 | 64 (64) | 172 | 0 | 0 / 0 | None | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2020 Apertura | 10 | 84 (84) | 247 | 0 | 2 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2021) |
| 2021 Clausura | 10 | 82 (82) | 239 | 0 | 2 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2021) |
| 2021 Apertura | 10 | 100 (100) | 278 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2022) |
| 2022 Clausura | 10 | 100 (100) | 268 | 0 | 1 / 0 | Motagua | RSSSF (hond2022) |
| 2022 Apertura | 10 | 100 (100) | 280 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2023) |
| 2023 Clausura | 10 | 100 (100) | 260 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2023) |
| 2023 Apertura | 10 | 100 (100) | 278 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2024) |
| 2024 Clausura | 10 | 100 (100) | 246 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2024) |
| 2024 Apertura | 10 | 100 (100) | 266 | 0 | 1 / 0 | Motagua | RSSSF (hond2025) |
| 2025 Clausura | 10 | 100 (100) | 239 | 0 | 1 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2025) |
| 2025 Apertura | 11 | 124 (124) | 387 | 0 | 3 / 0 | Olimpia de Tegucigalpa | RSSSF (hond2026) |
| 2026 Clausura | 11 | 124 (124) | 327 | 0 | 3 / 0 | Motagua | RSSSF (hond2026) |

## Conferência e correções, edição a edição

### 1965/66

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1966/67

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1967/68

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1968/69

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1969/70

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1970/71

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1971/72

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1972/73

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1973

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1974

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1975

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1976

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1977

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1978/79

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1979

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1980

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1981

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1982

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1983

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1984

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1985

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1986

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1987

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1988

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1989/90

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1990/91

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1991/92

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1992/93

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1993/94

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1994/95

- só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época

### 1995/96

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1996/97

- sem ocorrências

### 1997 Apertura

- tabela publicada x jogos — hond98:15: Motagua tabela [20, 10, 7, 3, 23, 17] jogos [20, 9, 8, 3, 22, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — hond98:15: Independiente de Honduras tabela [20, 1, 8, 11, 19, 42] jogos [20, 1, 9, 10, 19, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1998 Clausura

- decidido fora de campo — Marathón 4-1 Palestino de Honduras (1998-08-30): awarded 5-0?

### 1999

- sem ocorrências

### 1999 Apertura

- sem ocorrências

### 2000 Clausura

- sem ocorrências

### 2000 Apertura

- sem ocorrências

### 2001 Clausura

- sem ocorrências

### 2001 Apertura

- sem ocorrências

### 2002 Clausura

- tabela publicada x jogos — hond02:261: Victoria tabela [18, 6, 7, 5, 19, 21] jogos [18, 6, 8, 4, 19, 18] — a diferença vem de Victoria x Deportes Savio (2002-01-19), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — hond02:261: Deportes Savio tabela [18, 6, 3, 9, 19, 25] jogos [18, 5, 4, 9, 16, 25] — a diferença vem de Victoria x Deportes Savio (2002-01-19), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Victoria 0-3 Deportes Savio (2002-01-19): awarded? originally reported 0-0

### 2002 Apertura

- tabela publicada x jogos — hond03:17: Universidad tabela [18, 3, 10, 5, 20, 26] jogos [18, 3, 11, 4, 20, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — hond03:17: Real Maya tabela [18, 2, 8, 8, 11, 31] jogos [18, 0, 10, 8, 11, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — hond03:17: Victoria tabela [18, 2, 5, 11, 15, 26] jogos [18, 2, 6, 10, 15, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- não jogado — Marathón Real España (2002-09-28): apparently annulled; originally 0-2

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

- tabela publicada x jogos — hond06:17: Hispano tabela [18, 5, 7, 6, 24, 24] jogos [18, 5, 7, 6, 21, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2006 Clausura

- sem ocorrências

### 2006 Apertura

- ESPN: 95 jogos casados

### 2007 Clausura

- ESPN: 78 jogos casados
- tabela publicada x jogos — hond07:241: Olimpia de Tegucigalpa tabela [18, 11, 3, 4, 26, 12] jogos [17, 10, 3, 4, 24, 12] — a diferença vem de Atlético Olanchano x Olimpia de Tegucigalpa (2007-02-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — hond07:241: Atlético Olanchano tabela [17, 5, 3, 9, 16, 23] jogos [16, 5, 3, 8, 16, 21] — a diferença vem de Atlético Olanchano x Olimpia de Tegucigalpa (2007-02-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- não jogado — Atlético Olanchano Olimpia de Tegucigalpa (2007-02-11): annulled; originally 2-0 but
- decidido fora de campo — Atlético Olanchano Olimpia de Tegucigalpa (2007-02-11): replay, behind closed doors; awarded
- não jogado — Platense de Puerto Cortés Universidad (2007-04-29)
- não jogado — Victoria Atlético Olanchano (2007-04-29)

### 2007 Apertura

- ESPN: 89 jogos casados

### 2008 Clausura

- ESPN: 64 jogos casados

### 2008 Apertura

- ESPN: 95 jogos casados

### 2009 Clausura

- ESPN: 90 jogos casados
- não jogado — Platense de Puerto Cortés Hispano (2009-05-02): not played due to irrelevance

### 2009 Apertura

- ESPN: 85 jogos casados
- decidido fora de campo — Hispano Real España (2009-09-20): awarded 0-3, Hispano dns

### 2010 Clausura

- ESPN: 95 jogos casados

### 2010 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Apertura

- ESPN: 30 jogos casados
- decidido fora de campo — Vida Real España (2012-08-05): awarded 0-3, originally 1-0
- decidido fora de campo — Victoria Vida (2012-08-12): awarded 3-0, originally 1-2

### 2013 Clausura

- ESPN: 95 jogos casados

### 2013 Apertura

- ESPN: 96 jogos casados

### 2014 Clausura

- ESPN: 98 jogos casados

### 2014 Apertura

- ESPN: 92 jogos casados
- decidido fora de campo — Real Sociedad de Tocoa Marathón (2014-10-12): awarded 3-0, originally 1-1

### 2015 Clausura

- ESPN: 100 jogos casados

### 2015 Apertura

- ESPN: 97 jogos casados

### 2016 Clausura

- ESPN: 94 jogos casados

### 2016 Apertura

- ESPN: 98 jogos casados

### 2017 Clausura

- ESPN: 97 jogos casados

### 2017 Apertura

- ESPN: 100 jogos casados

### 2018 Clausura

- ESPN: 99 jogos casados

### 2018 Apertura

- ESPN: 99 jogos casados
- decidido fora de campo — Juticalpa Marathón (2018-08-15): awarded 0-3; originally 1-1, Juticalpa

### 2019 Clausura

- ESPN: 99 jogos casados

### 2019 Apertura

- ESPN: 100 jogos casados

### 2020 Clausura

- ESPN: 64 jogos casados

### 2020 Apertura

- ESPN: 78 jogos casados

### 2021 Clausura

- ESPN: 80 jogos casados

### 2021 Apertura

- ESPN: 96 jogos casados

### 2022 Clausura

- ESPN: 99 jogos casados
- decidido fora de campo — Lobos UPNFM Vida (2022-01-19): awarded 3-0, originally 1-1
- decidido fora de campo — Victoria Lobos UPNFM (2022-02-12): awarded 3-0, UPNFM dns

### 2022 Apertura

- ESPN: 99 jogos casados

### 2023 Clausura

- ESPN: 98 jogos casados

### 2023 Apertura

- ESPN: 99 jogos casados

### 2024 Clausura

- ESPN: 98 jogos casados

### 2024 Apertura

- ESPN: 100 jogos casados

### 2025 Clausura

- ESPN: 94 jogos casados

### 2025 Apertura

- ESPN: 122 jogos casados
- decidido fora de campo — Olimpia de Tegucigalpa Victoria (2025-12-06): awarded 3-0, Victoria dns

### 2026 Clausura

- ESPN: 124 jogos casados

