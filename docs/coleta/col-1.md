# Campeonato Colombiano (1ª divisão) — coleta de dados

Gerado por `python coleta/col-1/importar.py`. Pacote em `data/coleta/col-1/pacote/`.

**Edições:** 101, uma por título de campeão colombiano da 1ª divisão, de 1948 a 2025, como na lista de campeões da RSSSF (`colchamp.html`) e na Wikipédia em inglês. Até 2001 um campeão por ano: de 1968 em diante, Apertura e Finalización (e os quadrangulares, hexagonais e octogonais finais) são fases da edição anual. 1989 entra sem campeão (a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega); 1995 foi o torneio de transição e 1995/96 e 1996/97 seguiram o calendário europeu. De 2002 em diante, Apertura e Finalización dão título cada um: uma edição por torneio (em 2020 só houve o Apertura).

**Edições sem jogos (6):** 1987 e 1991-1995. Nenhuma fonte pública que achamos tem os jogos desses anos (a RSSSF e a Wikipédia trazem só as tabelas; o ogol tem as edições vazias). Elas entram com a tabela final da RSSSF como classificação e o campeão. Em 1986 a Wikipédia traz só parte do octogonal final.

**Fora do pacote:** a Copa Colombia, a Superliga, as liguillas, o Torneo Adecuación 1997 e os jogos de promoção.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/col-1/rsssf/`: base de jogos de 1995/96 em diante, menos 2011, 2012 e 2025, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas de todos os anos são a conferência); Wikipédia em espanhol (páginas "Campeonato colombiano <ano>" e "Torneo Apertura <ano> (Colombia)": jogos de 1948-1986, 1988-1990, 2011, 2012 e 2025, por rodada ou em tabela de confrontos, sem autores dos gols, e as finais com data e estádio); ESPN (liga `col.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol não tem os jogos da liga colombiana.

**Clubes:** Deportes Caldas (campeão em 1950) entra como Once Caldas, como a RSSSF e o próprio clube contam; Atlético Municipal é o Atlético Nacional; Cristal Caldas, o Once Caldas; Itagüí, o Águilas Doradas; La Equidad, o Internacional de Bogotá (2025); Alianza Petrolera, o Alianza FC (2024). Homônimos de outros países levam a cidade: Libertad de Barranquilla, Universidad Nacional de Bogotá, Boca Juniors de Cali, Huracán de Medellín.

**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela). Jogo decidido no tribunal leva o placar dado (`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (as tabelas de vários anos têm pontos de bônus, que vão em `ajuste_pontos`).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1948 | 10 | 90 (90) | 409 | 0 | 0 / 1 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1949 | 14 | 184 (184) | 820 | 0 | 1 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1950 | 16 | 240 (240) | 991 | 0 | 0 / 1 | Once Caldas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1951 | 18 | 306 (306) | 1250 | 0 | 0 / 2 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1952 | 15 | 209 (210) | 767 | 0 | 0 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1953 | 12 | 131 (132) | 534 | 0 | 0 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1954 | 10 | 86 (86) | 349 | 0 | 0 / 1 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1955 | 10 | 135 (135) | 507 | 0 | 1 / 0 | Independiente Medellín | RSSSF (col55) |
| 1956 | 13 | 156 (156) | 625 | 0 | 0 / 1 | Deportes Quindío | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1957 | 12 | 211 (211) | 695 | 0 | 0 / 1 | Independiente Medellín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1958 | 10 | 180 (180) | 644 | 0 | 0 / 1 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1959 | 12 | 261 (261) | 916 | 0 | 1 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1960 | 12 | 264 (264) | 815 | 0 | 0 / 1 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961 | 12 | 264 (264) | 846 | 0 | 1 / 0 | Millonarios | RSSSF (col61) |
| 1962 | 12 | 264 (264) | 893 | 0 | 0 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1963 | 13 | 312 (624) | 1062 | 0 | 0 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964 | 13 | 311 (312) | 996 | 0 | 0 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1965 | 13 | 312 (312) | 992 | 0 | 0 / 1 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 14 | 350 (350) | 1147 | 0 | 0 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1967 | 14 | 364 (364) | 1105 | 0 | 1 / 0 | Deportivo Cali | RSSSF (col67) |
| 1968 | 14 | 368 (368) | 1121 | 0 | 0 / 2 | Unión Magdalena | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1969 | 14 | 373 (555) | 1060 | 0 | 1 / 2 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1970 | 14 | 376 (558) | 995 | 0 | 1 / 2 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1971 | 14 | 379 (561) | 1025 | 0 | 1 / 2 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1972 | 14 | 376 (558) | 845 | 0 | 1 / 2 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1973 | 14 | 344 (344) | 840 | 0 | 0 / 3 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 | 14 | 361 (543) | 832 | 0 | 1 / 3 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1975 | 14 | 358 (358) | 873 | 0 | 1 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1976 | 14 | 361 (543) | 933 | 0 | 4 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1977 | 14 | 359 (541) | 897 | 0 | 0 / 4 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1978 | 14 | 365 (547) | 974 | 0 | 4 / 3 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979 | 14 | 367 (514) | 914 | 0 | 2 / 4 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1980 | 14 | 333 (333) | 833 | 0 | 0 / 7 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 | 14 | 329 (511) | 836 | 0 | 2 / 4 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982 | 14 | 387 (569) | 1078 | 0 | 0 / 4 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1983 | 14 | 336 (518) | 833 | 0 | 0 / 5 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1984 | 14 | 336 (518) | 783 | 0 | 2 / 4 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 | 14 | 336 (518) | 873 | 0 | 0 / 5 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986 | 8 | 21 (21) | 56 | 0 | 0 / 1 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Millonarios | RSSSF (col87) |
| 1988 | 15 | 146 (146) | 336 | 0 | 5 / 4 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1989 | 15 | 242 (242) | 544 | 0 | 0 / 0 | None | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1990 | 15 | 335 (425) | 752 | 0 | 1 / 5 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Nacional | RSSSF (col91) |
| 1992 | 16 | 0 (0) | 0 | 0 | 0 / 0 | América de Cali | RSSSF (col92) |
| 1993 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Junior de Barranquilla | RSSSF (col93) |
| 1994 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Atlético Nacional | RSSSF (col94) |
| 1995 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Junior de Barranquilla | RSSSF (col95) |
| 1995/96 | 16 | 208 (208) | 541 | 0 | 5 / 4 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996/97 | 16 | 380 (636) | 948 | 0 | 4 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 | 16 | 426 (426) | 1159 | 80 | 0 / 0 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 | 16 | 380 (380) | 997 | 1 | 5 / 2 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 | 16 | 364 (364) | 972 | 951 | 4 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001 | 16 | 378 (378) | 927 | 894 | 5 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Apertura | 18 | 224 (224) | 504 | 502 | 3 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Finalización | 18 | 224 (224) | 525 | 459 | 3 / 0 | Independiente Medellín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Apertura | 18 | 188 (188) | 449 | 295 | 2 / 1 | Once Caldas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Finalización | 18 | 188 (188) | 447 | 304 | 3 / 0 | Deportes Tolima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Apertura | 18 | 188 (188) | 465 | 301 | 3 / 0 | Independiente Medellín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Finalización | 18 | 188 (188) | 447 | 318 | 3 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Apertura | 18 | 188 (188) | 456 | 299 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Finalización | 18 | 187 (188) | 464 | 454 | 2 / 1 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Apertura | 18 | 188 (188) | 475 | 471 | 3 / 0 | Deportivo Pasto | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Finalización | 18 | 188 (179) | 479 | 479 | 3 / 1 | Cúcuta Deportivo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Apertura | 18 | 188 (188) | 482 | 472 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Finalización | 18 | 189 (188) | 446 | 404 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Apertura | 18 | 188 (188) | 469 | 452 | 3 / 0 | Boyacá Chicó | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Finalización | 18 | 188 (188) | 427 | 427 | 3 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 18 | 189 (188) | 439 | 411 | 3 / 0 | Once Caldas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Finalización | 18 | 189 (188) | 530 | 524 | 3 / 0 | Independiente Medellín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Apertura | 18 | 168 (168) | 457 | 443 | 1 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Finalización | 18 | 189 (188) | 498 | 496 | 3 / 0 | Once Caldas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Apertura | 18 | 176 (176) | 475 | 456 | 1 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Finalización | 18 | 176 (176) | 429 | 417 | 1 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2012 Apertura | 18 | 188 (188) | 453 | 453 | 3 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2012 Finalización | 18 | 188 (188) | 423 | 419 | 2 / 1 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2013 Apertura | 18 | 188 (188) | 469 | 0 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2013 Finalización | 18 | 188 (188) | 463 | 85 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2014 Apertura | 18 | 176 (176) | 444 | 440 | 1 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2014 Finalización | 18 | 188 (188) | 453 | 421 | 3 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2015 Apertura | 20 | 214 (214) | 523 | 482 | 1 / 0 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2015 Finalización | 20 | 214 (214) | 459 | 426 | 1 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2016 Apertura | 20 | 214 (214) | 534 | 487 | 1 / 0 | Independiente Medellín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2016 Finalización | 20 | 214 (214) | 498 | 483 | 1 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2017 Apertura | 20 | 214 (214) | 468 | 453 | 1 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2017 Finalización | 20 | 214 (214) | 455 | 421 | 1 / 0 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2018 Apertura | 20 | 204 (204) | 427 | 359 | 1 / 0 | Deportes Tolima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2018 Finalización | 20 | 204 (204) | 468 | 415 | 1 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2019 Apertura | 20 | 226 (226) | 502 | 489 | 3 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2019 Finalización | 20 | 226 (226) | 508 | 500 | 3 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2020 Apertura | 20 | 214 (214) | 517 | 501 | 1 / 0 | América de Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2021 Apertura | 19 | 185 (185) | 408 | 405 | 1 / 0 | Deportes Tolima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2021 Finalización | 20 | 226 (226) | 521 | 521 | 3 / 0 | Deportivo Cali | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 Apertura | 20 | 226 (226) | 491 | 480 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 Finalización | 20 | 226 (226) | 529 | 529 | 3 / 0 | Deportivo Pereira | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2023 Apertura | 20 | 226 (226) | 506 | 501 | 3 / 0 | Millonarios | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2023 Finalización | 20 | 226 (226) | 518 | 515 | 3 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2024 Apertura | 20 | 216 (216) | 467 | 459 | 3 / 0 | Atlético Bucaramanga | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2024 Finalización | 20 | 216 (216) | 473 | 467 | 3 / 0 | Atlético Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Apertura | 20 | 226 (226) | 489 | 486 | 3 / 0 | Independiente Santa Fe | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Finalización | 20 | 226 (226) | 547 | 544 | 3 / 0 | Junior de Barranquilla | calculada (fase alcançada, pontos, saldo, gols pró) |

## Conferência e correções, edição a edição

### 1948

- ogol: 42 jogos casados (edição 24306 do ogol, 90 jogos)
- tabela publicada x jogos — col48:17: Once Deportivo tabela [18, 5, 5, 8, 32, 50] jogos [18, 5, 4, 9, 32, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Once Caldas x Independiente Santa Fe (None): RSSSF 1-1, ogol 2-2; fica o da RSSSF

### 1949

- ogol: 134 jogos casados (edição 24846 do ogol, 184 jogos)
- tabela publicada x jogos — col49:18: Deportivo Barranquilla tabela [26, 5, 5, 16, 34, 49] jogos [26, 6, 5, 15, 35, 48] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Boca Juniors de Cali x Once Caldas (None): RSSSF 3-1, ogol 3-4; fica o da RSSSF
- placar diferente no ogol — Millonarios x Boca Juniors de Cali (None): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Deportivo Barranquilla x Once Caldas (None): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Deportivo Barranquilla x Once Deportivo (None): RSSSF 0-1, ogol 3-3; fica o da RSSSF
- data diferente no ogol — Millonarios x Deportivo Cali: RSSSF 1949-12-04, ogol 1949-11-27; fica a da RSSSF

### 1950

- ogol: 210 jogos casados (edição 24845 do ogol, 240 jogos)
- tabela publicada x jogos — col50:14: Independiente Medellín tabela [30, 15, 4, 11, 60, 45] jogos [30, 15, 5, 10, 61, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Cúcuta Deportivo tabela [30, 15, 3, 12, 61, 56] jogos [30, 14, 4, 12, 59, 58] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Boca Juniors de Cali tabela [30, 12, 8, 10, 79, 60] jogos [30, 11, 10, 9, 73, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Independiente Santa Fe tabela [30, 12, 8, 10, 67, 59] jogos [30, 13, 8, 9, 67, 55] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Junior de Barranquilla tabela [30, 12, 7, 11, 52, 57] jogos [30, 13, 8, 9, 53, 51] — a diferença vem de Junior de Barranquilla x Universidad Nacional de Bogotá (s/d), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — col50:14: América de Cali tabela [30, 11, 8, 11, 62, 64] jogos [30, 11, 8, 11, 62, 62] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Sporting de Barranquilla tabela [30, 11, 7, 12, 70, 79] jogos [30, 11, 8, 11, 71, 78] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Universidad Nacional de Bogotá tabela [30, 9, 5, 16, 55, 75] jogos [30, 9, 4, 17, 55, 72] — a diferença vem de Junior de Barranquilla x Universidad Nacional de Bogotá (s/d), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — col50:14: Deportivo Pereira tabela [30, 7, 9, 14, 62, 79] jogos [30, 5, 9, 16, 55, 80] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Huracán de Medellín tabela [30, 7, 6, 17, 57, 96] jogos [30, 7, 7, 16, 56, 93] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col50:14: Atlético Nacional tabela [30, 6, 4, 20, 55, 79] jogos [30, 4, 6, 20, 52, 79] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — América de Cali x Atlético Nacional (None): RSSSF 4-1, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Atlético Bucaramanga x Deportivo Cali (None): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Cúcuta Deportivo x Sporting de Barranquilla (None): RSSSF 2-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Deportivo Cali x Cúcuta Deportivo (None): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — América de Cali x Deportivo Pereira (None): RSSSF 4-1, ogol 4-3; fica o da RSSSF
- placar diferente no ogol — Boca Juniors de Cali x Junior de Barranquilla (None): RSSSF 0-0, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Deportivo Pereira x Junior de Barranquilla (None): RSSSF 1-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Junior de Barranquilla x Sporting de Barranquilla (None): RSSSF 2-3, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Huracán de Medellín x Atlético Nacional (None): RSSSF 1-1, ogol 2-4; fica o da RSSSF
- placar diferente no ogol — Independiente Medellín x Atlético Nacional (None): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Independiente Santa Fe x Deportivo Pereira (None): RSSSF 3-0, ogol 3-4; fica o da RSSSF
- decidido fora de campo — Junior de Barranquilla 2-2 Universidad Nacional de Bogotá (s/d): placar em campo 2-2; o tribunal deu 0-1

### 1951

- ogol: 240 jogos casados (edição 24982 do ogol, 306 jogos)
- tabela publicada x jogos — col51:14: Millonarios tabela [34, 28, 4, 2, 98, 29] jogos [4, 3, 1, 0, 10, 3] — faltam 30 jogo(s) do clube na página
- tabela publicada x jogos — col51:14: Boca Juniors de Cali tabela [34, 22, 5, 7, 110, 55] jogos [4, 0, 0, 4, 5, 12] — faltam 30 jogo(s) do clube na página
- tabela publicada x jogos — col51:14: Cúcuta Deportivo tabela [34, 21, 6, 7, 93, 56] jogos [4, 2, 1, 1, 7, 7] — faltam 30 jogo(s) do clube na página
- tabela publicada x jogos — col51:18: Deportes Quindío tabela [34, 15, 9, 10, 70, 62] jogos [34, 14, 11, 9, 67, 58] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Independiente Santa Fe tabela [34, 14, 9, 11, 90, 75] jogos [34, 14, 9, 11, 92, 75] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Sporting de Barranquilla tabela [34, 14, 9, 11, 78, 73] jogos [34, 15, 9, 10, 77, 69] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Junior de Barranquilla tabela [34, 14, 8, 12, 66, 58] jogos [34, 14, 8, 12, 62, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Once Deportivo tabela [34, 14, 7, 13, 72, 66] jogos [34, 12, 8, 14, 68, 69] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Once Caldas tabela [34, 14, 6, 14, 77, 74] jogos [34, 14, 6, 14, 75, 74] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Deportivo Pereira tabela [34, 12, 10, 12, 66, 67] jogos [34, 12, 10, 12, 66, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Atlético Bucaramanga tabela [34, 14, 6, 14, 55, 60] jogos [34, 15, 6, 13, 59, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: América de Cali tabela [34, 11, 7, 16, 66, 76] jogos [34, 10, 8, 16, 66, 77] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Deportivo Samarios tabela [34, 10, 7, 17, 64, 69] jogos [34, 9, 6, 19, 57, 67] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Atlético Nacional tabela [34, 7, 9, 18, 54, 96] jogos [34, 7, 9, 18, 52, 95] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col51:18: Universidad Nacional de Bogotá tabela [34, 5, 4, 25, 48, 126] jogos [34, 7, 3, 24, 50, 123] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Cúcuta Deportivo x Sporting de Barranquilla (None): RSSSF 1-3, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Deportes Quindío x Deportivo Cali (None): RSSSF 0-0, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Once Deportivo x Atlético Bucaramanga (None): RSSSF 1-3, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Deportes Quindío x Junior de Barranquilla (None): RSSSF 0-0, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Deportivo Pereira x Deportes Quindío (None): RSSSF 4-2, ogol 34-2; fica o da RSSSF
- placar diferente no ogol — Once Deportivo x Sporting de Barranquilla (None): RSSSF 0-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Atlético Bucaramanga x Deportivo Cali (None): RSSSF 1-1, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Huracán de Medellín x Once Caldas (None): RSSSF 1-2, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Independiente Santa Fe x Deportes Quindío (None): RSSSF 3-2, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Deportes Quindío x Huracán de Medellín (None): RSSSF 0-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Boca Juniors de Cali x Deportivo Cali (None): RSSSF 2-1, ogol 5-1; fica o da RSSSF
- placar diferente no ogol — Once Caldas x Deportivo Pereira (None): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Independiente Santa Fe x Once Deportivo (None): RSSSF 3-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Sporting de Barranquilla x Junior de Barranquilla (None): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Cúcuta Deportivo x Millonarios (None): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Deportivo Cali x Deportivo Pereira (None): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Huracán de Medellín x Once Deportivo (None): RSSSF 0-1, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — América de Cali x Huracán de Medellín (None): RSSSF 1-1, ogol 1-0; fica o da RSSSF

### 1952

- tabela publicada x jogos — col52:14: Millonarios tabela [28, 20, 6, 2, 70, 14] jogos [28, 20, 6, 2, 70, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col52:14: América de Cali tabela [28, 12, 7, 9, 50, 38] jogos [28, 13, 7, 8, 49, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col52:14: Universidad Nacional de Bogotá tabela [28, 9, 6, 13, 53, 54] jogos [28, 9, 6, 13, 52, 54] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col52:14: Deportivo Samarios tabela [28, 7, 5, 16, 38, 78] jogos [27, 6, 5, 16, 37, 78] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col52:14: Atlético Bucaramanga tabela [28, 3, 6, 19, 35, 86] jogos [27, 2, 6, 19, 32, 84] — faltam 1 jogo(s) do clube na página

### 1953

- tabela publicada x jogos — col53:14: Deportes Quindío tabela [22, 14, 5, 3, 66, 40] jogos [21, 13, 5, 3, 65, 40] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col53:14: Independiente Santa Fe tabela [22, 12, 5, 5, 57, 30] jogos [21, 12, 5, 4, 57, 29] — faltam 1 jogo(s) do clube na página

### 1954

- tabela publicada x jogos — col54:14: Deportes Quindío tabela [18, 11, 3, 4, 57, 27] jogos [18, 11, 3, 4, 56, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col54:14: Boca Juniors de Cali tabela [16, 6, 3, 7, 32, 33] jogos [16, 6, 3, 7, 32, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1955

- sem ocorrências

### 1956

- tabela publicada x jogos — col56:14: Libertad de Barranquilla tabela [24, 9, 3, 12, 44, 59] jogos [24, 9, 3, 12, 43, 59] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col56:14: Atlético Nacional tabela [24, 8, 4, 12, 53, 57] jogos [24, 8, 4, 12, 53, 56] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1957

- tabela publicada x jogos — col57:16: Boca Juniors de Cali tabela [22, 12, 5, 5, 43, 16] jogos [22, 12, 5, 5, 43, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col57:16: Deportes Quindío tabela [22, 10, 4, 8, 34, 32] jogos [22, 10, 4, 8, 34, 30] — a diferença vem de Deportivo Pereira x Deportes Quindío (1957-09-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — col57:16: Deportivo Pereira tabela [22, 9, 6, 7, 41, 51] jogos [22, 9, 6, 7, 42, 51] — a diferença vem de Deportivo Pereira x Deportes Quindío (1957-09-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — col57:16: América de Cali tabela [22, 8, 3, 11, 39, 45] jogos [22, 8, 3, 11, 39, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col57:16: Millonarios tabela [22, 4, 8, 10, 25, 40] jogos [22, 4, 7, 11, 25, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Independiente Medellín x Cúcuta Deportivo (1957-09-14): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Deportivo Pereira x Deportes Quindío (1957-09-14): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Independiente Santa Fe x Independiente Medellín (1957-09-21): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Unión Magdalena x Boca Juniors de Cali (1957-09-21): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Deportes Quindío x Deportes Tolima (1957-09-21): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Cúcuta Deportivo x Deportivo Pereira (1957-09-21): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Independiente Santa Fe x Unión Magdalena (1957-09-28): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Independiente Medellín x Deportivo Pereira (1957-09-28): octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- corrigido — Unión Magdalena x Independiente Medellín (1957-10-06): hexagonal do grupo A (CO-013)
- corrigido — Atlético Nacional x Deportes Quindío (1957-10-06): hexagonal do grupo A (CO-013)
- corrigido — Deportivo Pereira x Deportes Tolima (1957-10-06): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Atlético Nacional (1957-10-13): hexagonal do grupo A (CO-013)
- corrigido — Deportes Tolima x Unión Magdalena (1957-10-13): hexagonal do grupo A (CO-013)
- corrigido — Deportes Quindío x Deportivo Pereira (1957-10-13): hexagonal do grupo A (CO-013)
- corrigido — Unión Magdalena x Deportes Quindío (1957-10-20): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Deportes Tolima (1957-10-20): hexagonal do grupo A (CO-013)
- corrigido — Deportivo Pereira x Atlético Nacional (1957-10-20): hexagonal do grupo A (CO-013)
- corrigido — Atlético Nacional x Unión Magdalena (1957-10-27): hexagonal do grupo A (CO-013)
- corrigido — Deportivo Pereira x Independiente Medellín (1957-10-27): hexagonal do grupo A (CO-013)
- corrigido — Deportes Tolima x Deportes Quindío (1957-10-27): hexagonal do grupo A (CO-013)
- corrigido — Deportes Quindío x Independiente Medellín (1957-11-01): hexagonal do grupo A (CO-013)
- corrigido — Unión Magdalena x Deportivo Pereira (1957-11-01): hexagonal do grupo A (CO-013)
- corrigido — Atlético Nacional x Deportes Tolima (1957-11-01): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Unión Magdalena (1957-11-03): hexagonal do grupo A (CO-013)
- corrigido — Deportes Quindío x Atlético Nacional (1957-11-03): hexagonal do grupo A (CO-013)
- corrigido — Deportes Tolima x Deportivo Pereira (1957-11-03): hexagonal do grupo A (CO-013)
- corrigido — Atlético Nacional x Independiente Medellín (1957-11-10): hexagonal do grupo A (CO-013)
- corrigido — Unión Magdalena x Deportes Tolima (1957-11-10): hexagonal do grupo A (CO-013)
- corrigido — Deportivo Pereira x Deportes Quindío (1957-11-10): hexagonal do grupo A (CO-013)
- corrigido — Deportes Quindío x Unión Magdalena (1957-11-17): hexagonal do grupo A (CO-013)
- corrigido — Deportes Tolima x Independiente Medellín (1957-11-17): hexagonal do grupo A (CO-013)
- corrigido — Atlético Nacional x Deportivo Pereira (1957-11-17): hexagonal do grupo A (CO-013)
- corrigido — Unión Magdalena x Atlético Nacional (1957-11-24): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Deportivo Pereira (1957-11-24): hexagonal do grupo A (CO-013)
- corrigido — Deportes Quindío x Deportes Tolima (1957-11-24): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Deportes Quindío (1957-11-30): hexagonal do grupo A (CO-013)
- corrigido — Deportivo Pereira x Unión Magdalena (1957-11-30): hexagonal do grupo A (CO-013)
- corrigido — Deportes Tolima x Atlético Nacional (1957-11-30): hexagonal do grupo A (CO-013)
- corrigido — Independiente Medellín x Deportivo Pereira (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Independiente Medellín x Deportes Tolima (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Deportivo Pereira x Independiente Medellín (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Deportivo Pereira x Deportes Tolima (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Deportes Tolima x Independiente Medellín (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Deportes Tolima x Deportivo Pereira (None): desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- corrigido — Cúcuta Deportivo x América de Cali (1957-10-06): hexagonal do grupo B (CO-013)
- corrigido — Millonarios x Atlético Bucaramanga (1957-10-06): hexagonal do grupo B (CO-013)
- corrigido — Boca Juniors de Cali x Independiente Santa Fe (1957-10-06): hexagonal do grupo B (CO-013)
- corrigido — América de Cali x Millonarios (1957-10-13): hexagonal do grupo B (CO-013)
- corrigido — Independiente Santa Fe x Cúcuta Deportivo (1957-10-13): hexagonal do grupo B (CO-013)
- corrigido — Atlético Bucaramanga x Boca Juniors de Cali (1957-10-13): hexagonal do grupo B (CO-013)
- corrigido — Cúcuta Deportivo x Atlético Bucaramanga (1957-10-20): hexagonal do grupo B (CO-013)
- corrigido — América de Cali x Independiente Santa Fe (1957-10-20): hexagonal do grupo B (CO-013)
- corrigido — Millonarios x Boca Juniors de Cali (1957-10-20): hexagonal do grupo B (CO-013)
- corrigido — Atlético Bucaramanga x América de Cali (1957-10-27): hexagonal do grupo B (CO-013)
- corrigido — Boca Juniors de Cali x Cúcuta Deportivo (1957-10-27): hexagonal do grupo B (CO-013)
- corrigido — Millonarios x Independiente Santa Fe (1957-10-27): hexagonal do grupo B (CO-013)
- corrigido — América de Cali x Boca Juniors de Cali (1957-11-01): hexagonal do grupo B (CO-013)
- corrigido — Cúcuta Deportivo x Millonarios (1957-11-01): hexagonal do grupo B (CO-013)
- corrigido — Independiente Santa Fe x Atlético Bucaramanga (1957-11-01): hexagonal do grupo B (CO-013)
- corrigido — América de Cali x Cúcuta Deportivo (1957-11-03): hexagonal do grupo B (CO-013)
- corrigido — Atlético Bucaramanga x Millonarios (1957-11-03): hexagonal do grupo B (CO-013)
- corrigido — Independiente Santa Fe x Boca Juniors de Cali (1957-11-03): hexagonal do grupo B (CO-013)
- corrigido — Millonarios x América de Cali (1957-11-10): hexagonal do grupo B (CO-013)
- corrigido — Cúcuta Deportivo x Independiente Santa Fe (1957-11-10): hexagonal do grupo B (CO-013)
- corrigido — Boca Juniors de Cali x Atlético Bucaramanga (1957-11-10): hexagonal do grupo B (CO-013)
- corrigido — Atlético Bucaramanga x Cúcuta Deportivo (1957-11-17): hexagonal do grupo B (CO-013)
- corrigido — Independiente Santa Fe x América de Cali (1957-11-17): hexagonal do grupo B (CO-013)
- corrigido — Boca Juniors de Cali x Millonarios (1957-11-17): hexagonal do grupo B (CO-013)
- corrigido — América de Cali x Atlético Bucaramanga (1957-11-24): hexagonal do grupo B (CO-013)
- corrigido — Cúcuta Deportivo x Boca Juniors de Cali (1957-11-24): hexagonal do grupo B (CO-013)
- corrigido — Independiente Santa Fe x Millonarios (1957-11-24): hexagonal do grupo B (CO-013)
- corrigido — Boca Juniors de Cali x América de Cali (1957-11-30): hexagonal do grupo B (CO-013)
- corrigido — Millonarios x Cúcuta Deportivo (1957-11-30): hexagonal do grupo B (CO-013)
- corrigido — Atlético Bucaramanga x Independiente Santa Fe (1957-11-30): hexagonal do grupo B (CO-013)
- corrigido — Cúcuta Deportivo x Deportes Tolima (1957-02-16): final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- corrigido — Deportes Tolima x Cúcuta Deportivo (1957-02-23): final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- corrigido — Cúcuta Deportivo x Deportes Tolima (1957-03-15): final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- anulado — Independiente Medellín 7-1 Cúcuta Deportivo (1957-09-14)
- anulado — Deportivo Pereira 1-2 Deportes Quindío (1957-09-14)
- anulado — Independiente Santa Fe 2-3 Independiente Medellín (1957-09-21)
- anulado — Unión Magdalena 2-0 Boca Juniors de Cali (1957-09-21)
- anulado — Deportes Quindío 1-0 Deportes Tolima (1957-09-21)
- anulado — Cúcuta Deportivo 1-4 Deportivo Pereira (1957-09-21)
- anulado — Independiente Santa Fe 2-2 Unión Magdalena (1957-09-28)
- anulado — Independiente Medellín 3-1 Deportivo Pereira (1957-09-28)

### 1958

- tabela publicada x jogos — col58:14: Cúcuta Deportivo tabela [36, 11, 11, 14, 63, 66] jogos [36, 11, 11, 14, 62, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col58:14: América de Cali tabela [36, 4, 4, 28, 44, 99] jogos [36, 4, 4, 28, 44, 98] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1959

- tabela publicada x jogos — col59:20: Deportes Quindío tabela [44, 13, 14, 17, 60, 70] jogos [43, 12, 14, 17, 59, 70] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col59:20: Atlético Bucaramanga tabela [44, 14, 11, 19, 67, 78] jogos [44, 15, 11, 18, 69, 76] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col59:20: Deportes Tolima tabela [44, 12, 14, 18, 78, 95] jogos [43, 12, 14, 17, 78, 94] — faltam 1 jogo(s) do clube na página

### 1960

- tabela publicada x jogos — col60:14: Deportes Quindío tabela [44, 14, 15, 15, 64, 71] jogos [44, 15, 15, 14, 65, 70] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col60:14: Unión Magdalena tabela [44, 10, 12, 22, 57, 83] jogos [44, 9, 12, 23, 56, 84] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1961

- sem ocorrências

### 1962

- tabela publicada x jogos — col62:14: Millonarios tabela [44, 25, 11, 8, 96, 44] jogos [44, 25, 12, 7, 96, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col62:14: Deportes Quindío tabela [44, 6, 12, 26, 51, 102] jogos [44, 6, 13, 25, 51, 102] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1963

- tabela publicada x jogos — col63:14: Millonarios tabela [48, 27, 9, 12, 102, 60] jogos [48, 27, 9, 12, 102, 61] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Independiente Santa Fe tabela [48, 24, 13, 11, 112, 61] jogos [48, 24, 13, 11, 112, 81] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Cúcuta Deportivo tabela [48, 21, 14, 13, 96, 67] jogos [48, 21, 13, 14, 95, 68] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Deportivo Pereira tabela [48, 18, 12, 18, 96, 77] jogos [48, 19, 12, 17, 96, 77] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: América de Cali tabela [48, 13, 21, 14, 73, 67] jogos [48, 14, 20, 14, 73, 68] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Atlético Nacional tabela [48, 16, 9, 23, 79, 101] jogos [48, 15, 10, 23, 79, 101] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Atlético Bucaramanga tabela [48, 14, 13, 21, 66, 80] jogos [48, 14, 13, 21, 68, 80] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col63:14: Deportes Tolima tabela [48, 8, 12, 28, 59, 109] jogos [48, 8, 12, 28, 61, 109] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1964

- tabela publicada x jogos — col64:14: Cúcuta Deportivo tabela [48, 19, 18, 11, 79, 56] jogos [48, 19, 18, 11, 79, 57] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col64:14: Deportes Quindío tabela [48, 18, 16, 14, 81, 68] jogos [47, 18, 15, 14, 78, 65] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col64:14: Deportivo Cali tabela [48, 15, 21, 12, 83, 71] jogos [47, 15, 20, 12, 80, 68] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col64:14: América de Cali tabela [48, 15, 18, 15, 71, 71] jogos [48, 15, 18, 15, 71, 70] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1965

- tabela publicada x jogos — col65:14: Deportivo Cali tabela [48, 27, 8, 13, 93, 65] jogos [48, 27, 8, 13, 93, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col65:14: Millonarios tabela [48, 18, 21, 9, 91, 66] jogos [48, 18, 21, 9, 91, 65] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1966

- sem ocorrências

### 1967

- sem ocorrências

### 1968

- tabela publicada x jogos — col68:14: Unión Magdalena tabela [26, 15, 8, 3, 43, 28] jogos [26, 15, 8, 3, 52, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col68:14: Junior de Barranquilla tabela [26, 14, 7, 5, 52, 31] jogos [26, 14, 7, 5, 54, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col68:14: Cúcuta Deportivo tabela [26, 2, 10, 14, 26, 52] jogos [26, 2, 10, 14, 26, 54] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col68:31: Junior de Barranquilla tabela [26, 16, 3, 7, 56, 37] jogos [26, 16, 3, 7, 55, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col68:31: Independiente Medellín tabela [26, 9, 7, 10, 32, 37] jogos [26, 9, 7, 10, 32, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col68:31: Deportes Quindío tabela [26, 5, 2, 19, 26, 61] jogos [26, 5, 2, 19, 25, 61] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1969

- tabela publicada x jogos — col69:14: Deportivo Cali tabela [26, 14, 8, 4, 55, 32] jogos [26, 14, 8, 4, 55, 31] — a outra tabela publicada (col69) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col69:14: América de Cali tabela [26, 10, 13, 3, 36, 25] jogos [26, 10, 13, 3, 36, 26] — a outra tabela publicada (col69) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col69:14: Cúcuta Deportivo tabela [26, 11, 4, 11, 46, 42] jogos [26, 11, 4, 11, 46, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:14: Once Caldas tabela [26, 8, 9, 9, 37, 48] jogos [26, 7, 9, 10, 37, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:14: Deportes Tolima tabela [26, 7, 6, 13, 38, 49] jogos [26, 7, 6, 13, 37, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:14: Atlético Nacional tabela [26, 4, 9, 13, 30, 45] jogos [26, 5, 9, 12, 32, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:34: América de Cali tabela [26, 12, 6, 8, 43, 26] jogos [26, 12, 6, 8, 43, 25] — a outra tabela publicada (col69) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col69:34: Junior de Barranquilla tabela [26, 10, 9, 7, 47, 42] jogos [26, 10, 9, 7, 45, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:34: Once Caldas tabela [26, 10, 7, 9, 36, 35] jogos [26, 10, 6, 10, 34, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col69:34: Cúcuta Deportivo tabela [26, 5, 4, 17, 27, 52] jogos [26, 5, 4, 17, 28, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1970

- tabela publicada x jogos — col70:17: Unión Magdalena tabela [26, 7, 11, 8, 30, 36] jogos [26, 7, 11, 8, 31, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col70:17: América de Cali tabela [26, 8, 8, 10, 30, 34] jogos [26, 8, 8, 10, 30, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col70:40: Unión Magdalena tabela [26, 12, 6, 8, 38, 32] jogos [26, 12, 6, 8, 37, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col70:40: Independiente Santa Fe tabela [26, 9, 11, 6, 46, 31] jogos [26, 9, 12, 5, 46, 31] — a outra tabela publicada (col70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col70:40: América de Cali tabela [26, 9, 11, 6, 36, 29] jogos [26, 9, 11, 6, 36, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col70:40: Deportivo Pereira tabela [26, 8, 4, 14, 32, 48] jogos [26, 8, 4, 14, 32, 52] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1971

- tabela publicada x jogos — col71:23: Independiente Santa Fe tabela [26, 12, 10, 4, 42, 27] jogos [27, 13, 10, 4, 44, 26] — a outra tabela publicada (col71) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col71:23: América de Cali tabela [26, 9, 8, 9, 34, 33] jogos [25, 9, 8, 8, 34, 32] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col71:23: Deportes Quindío tabela [26, 7, 11, 8, 31, 41] jogos [26, 6, 11, 9, 29, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col71:23: Deportes Tolima tabela [26, 6, 10, 10, 33, 38] jogos [26, 6, 9, 11, 32, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col71:23: Real Cartagena tabela [26, 4, 12, 10, 18, 32] jogos [26, 5, 11, 10, 18, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col71:46: Independiente Santa Fe tabela [26, 16, 6, 4, 50, 21] jogos [26, 15, 6, 5, 48, 23] — a outra tabela publicada (col71) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col71:46: Deportes Quindío tabela [26, 10, 8, 8, 39, 35] jogos [26, 11, 8, 7, 41, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1972

- tabela publicada x jogos — col72:15: Unión Magdalena tabela [26, 12, 10, 4, 28, 22] jogos [26, 4, 10, 12, 18, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:15: Deportivo Pereira tabela [26, 7, 13, 6, 35, 27] jogos [26, 7, 13, 6, 31, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:15: Independiente Medellín tabela [26, 7, 11, 8, 25, 25] jogos [26, 6, 11, 9, 24, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:15: Atlético Bucaramanga tabela [26, 7, 7, 12, 29, 31] jogos [26, 7, 7, 12, 27, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:15: América de Cali tabela [26, 4, 8, 14, 16, 40] jogos [26, 5, 8, 13, 17, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:35: Deportivo Cali tabela [26, 16, 4, 6, 49, 27] jogos [30, 19, 4, 7, 56, 31] — a outra tabela publicada (col72) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col72:35: Millonarios tabela [26, 17, 2, 7, 39, 20] jogos [30, 19, 3, 8, 45, 24] — a outra tabela publicada (col72) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col72:35: Atlético Nacional tabela [26, 14, 8, 4, 34, 20] jogos [30, 14, 9, 7, 35, 26] — sobram 4 jogo(s) do clube na página
- tabela publicada x jogos — col72:35: América de Cali tabela [26, 9, 9, 8, 21, 22] jogos [26, 8, 9, 9, 20, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:35: Deportivo Pereira tabela [26, 5, 12, 9, 28, 39] jogos [26, 5, 12, 9, 32, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:35: Independiente Medellín tabela [26, 6, 7, 13, 17, 25] jogos [26, 7, 7, 12, 18, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:35: Atlético Bucaramanga tabela [26, 3, 12, 11, 18, 36] jogos [26, 3, 12, 11, 20, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col72:35: Unión Magdalena tabela [26, 3, 10, 13, 10, 49] jogos [26, 4, 8, 14, 20, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1973

- tabela publicada x jogos — col73:15: Deportivo Cali tabela [26, 13, 10, 3, 41, 22] jogos [26, 12, 11, 3, 40, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:15: Atlético Nacional tabela [26, 11, 9, 6, 35, 30] jogos [26, 11, 9, 6, 34, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:15: Deportivo Pereira tabela [26, 7, 9, 10, 37, 38] jogos [26, 7, 10, 9, 37, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:15: Independiente Santa Fe tabela [26, 7, 8, 11, 26, 35] jogos [26, 7, 8, 11, 26, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:35: Independiente Medellín tabela [24, 12, 7, 5, 28, 19] jogos [24, 11, 8, 5, 27, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:35: Deportivo Pereira tabela [24, 7, 7, 10, 27, 38] jogos [24, 7, 7, 10, 27, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:35: Atlético Bucaramanga tabela [24, 7, 4, 13, 26, 38] jogos [24, 7, 5, 12, 26, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col73:62: Deportivo Cali tabela [4, 1, 1, 2, 2, 2] jogos [4, 1, 1, 2, 2, 3] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1974

- tabela publicada x jogos — col74:15: Millonarios tabela [26, 15, 3, 8, 38, 21] jogos [26, 15, 3, 8, 37, 20] — a outra tabela publicada (col74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col74:15: Independiente Medellín tabela [26, 11, 8, 7, 32, 22] jogos [26, 12, 7, 7, 32, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col74:15: América de Cali tabela [26, 9, 11, 6, 27, 24] jogos [26, 9, 11, 6, 27, 23] — a outra tabela publicada (col74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col74:15: Cúcuta Deportivo tabela [26, 6, 10, 10, 18, 26] jogos [26, 6, 10, 10, 19, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col74:15: Once Caldas tabela [26, 8, 5, 13, 31, 41] jogos [26, 7, 6, 13, 29, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col74:51: Millonarios tabela [21, 9, 8, 4, 26, 14] jogos [21, 10, 6, 5, 26, 14] — a outra tabela publicada (col74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col74:61: Deportivo Pereira tabela [21, 10, 5, 6, 21, 16] jogos [21, 10, 5, 6, 21, 17] — a outra tabela publicada (col74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col74:61: Deportes Quindío tabela [21, 9, 3, 9, 30, 27] jogos [21, 9, 3, 9, 34, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col74:61: Unión Magdalena tabela [21, 2, 5, 14, 16, 40] jogos [21, 2, 5, 14, 16, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Atlético Nacional x Deportivo Cali (1974-07-11): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- corrigido — Deportivo Cali x Atlético Nacional (1974-07-14): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)

### 1975

- linha lida como jogo e descartada (clube não reconhecido): wiki-es_1975:598 «Cúcuta x Deportivo»

### 1976

- corrigido — Junior de Barranquilla x Millonarios (1976-07-18): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- corrigido — Millonarios x Junior de Barranquilla (1976-07-20): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)

### 1977

- tabela publicada x jogos — col77:15: Once Caldas tabela [26, 11, 6, 9, 36, 36] jogos [26, 11, 6, 9, 32, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:15: Atlético Bucaramanga tabela [26, 4, 14, 8, 26, 34] jogos [26, 4, 14, 8, 26, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:37: Independiente Santa Fe tabela [21, 9, 4, 8, 33, 26] jogos [21, 9, 4, 8, 31, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:37: Once Caldas tabela [21, 6, 8, 7, 35, 38] jogos [21, 6, 8, 7, 35, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:47: Atlético Bucaramanga tabela [21, 6, 10, 5, 23, 21] jogos [21, 5, 11, 5, 23, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:47: Cúcuta Deportivo tabela [21, 6, 8, 7, 21, 25] jogos [21, 6, 9, 6, 22, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:47: Unión Magdalena tabela [21, 6, 8, 7, 21, 25] jogos [21, 7, 7, 7, 24, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:47: Deportivo Pereira tabela [21, 5, 8, 8, 23, 27] jogos [21, 5, 7, 9, 23, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:47: Deportes Tolima tabela [21, 5, 6, 10, 16, 26] jogos [21, 4, 8, 9, 17, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:110: Deportivo Cali tabela [10, 5, 2, 3, 20, 13] jogos [10, 5, 2, 3, 21, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:110: Atlético Nacional tabela [10, 3, 4, 3, 12, 10] jogos [10, 3, 4, 3, 13, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col77:110: Atlético Bucaramanga tabela [10, 2, 0, 8, 12, 24] jogos [10, 2, 0, 8, 12, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1978

- tabela publicada x jogos — col78:15: Deportes Quindío tabela [26, 8, 8, 10, 24, 31] jogos [26, 8, 8, 10, 25, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col78:15: Deportes Tolima tabela [26, 7, 7, 12, 30, 38] jogos [26, 7, 8, 11, 30, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col78:15: Independiente Medellín tabela [26, 8, 2, 16, 29, 42] jogos [26, 7, 3, 16, 28, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col78:15: Deportivo Pereira tabela [26, 2, 7, 17, 13, 42] jogos [26, 2, 7, 17, 12, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col78:36: América de Cali tabela [21, 10, 7, 4, 30, 23] jogos [21, 9, 7, 5, 30, 25] — a outra tabela publicada (col78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col78:36: Atlético Nacional tabela [21, 10, 3, 8, 25, 18] jogos [21, 10, 3, 8, 25, 19] — a outra tabela publicada (col78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col78:36: Deportivo Cali tabela [21, 5, 6, 10, 27, 33] jogos [21, 6, 6, 9, 29, 33] — a outra tabela publicada (col78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col78:36: Atlético Bucaramanga tabela [21, 4, 8, 9, 29, 30] jogos [21, 4, 8, 9, 26, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col78:49: Independiente Medellín tabela [21, 2, 9, 10, 18, 34] jogos [21, 2, 9, 10, 19, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1979

- tabela publicada x jogos — col79:15: América de Cali tabela [26, 13, 8, 5, 29, 19] jogos [10, 3, 6, 1, 9, 6] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:15: Deportivo Cali tabela [26, 13, 8, 5, 37, 27] jogos [10, 5, 2, 3, 13, 11] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — col79:15: Once Caldas tabela [26, 13, 7, 6, 42, 24] jogos [12, 5, 4, 3, 20, 10] — faltam 14 jogo(s) do clube na página
- tabela publicada x jogos — col79:15: Junior de Barranquilla tabela [26, 13, 6, 7, 36, 27] jogos [10, 2, 4, 4, 8, 11] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:15: Unión Magdalena tabela [26, 9, 10, 7, 27, 25] jogos [12, 4, 3, 5, 8, 14] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:15: Independiente Medellín tabela [26, 9, 9, 8, 34, 30] jogos [10, 1, 5, 4, 6, 12] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — col79:22: Millonarios tabela [26, 11, 4, 11, 42, 37] jogos [14, 11, 1, 2, 34, 12] — faltam 12 jogo(s) do clube na página
- tabela publicada x jogos — col79:22: Atlético Nacional tabela [26, 8, 8, 10, 32, 38] jogos [12, 4, 3, 5, 16, 17] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:22: Deportes Quindío tabela [26, 7, 10, 9, 27, 24] jogos [12, 4, 5, 3, 12, 10] — faltam 14 jogo(s) do clube na página
- tabela publicada x jogos — col79:22: Atlético Bucaramanga tabela [26, 8, 7, 11, 34, 38] jogos [12, 5, 2, 5, 18, 19] — faltam 14 jogo(s) do clube na página
- tabela publicada x jogos — col79:22: Deportivo Pereira tabela [26, 8, 7, 11, 34, 41] jogos [12, 5, 2, 5, 17, 15] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:22: Cúcuta Deportivo tabela [26, 6, 10, 10, 27, 40] jogos [14, 4, 4, 6, 14, 23] — faltam 12 jogo(s) do clube na página
- tabela publicada x jogos — col79:22: Deportes Tolima tabela [26, 2, 6, 18, 22, 58] jogos [12, 1, 3, 8, 8, 23] — faltam 14 jogo(s) do clube na página
- tabela publicada x jogos — col79:39: América de Cali tabela [21, 13, 5, 3, 33, 14] jogos [21, 13, 5, 3, 34, 14] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Deportivo Cali tabela [21, 11, 5, 5, 30, 21] jogos [21, 11, 5, 5, 31, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:39: Deportivo Pereira tabela [21, 11, 4, 6, 41, 28] jogos [21, 11, 5, 5, 42, 33] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Unión Magdalena tabela [21, 10, 4, 7, 24, 20] jogos [21, 10, 5, 6, 24, 20] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Atlético Nacional tabela [21, 5, 13, 3, 26, 22] jogos [21, 5, 13, 3, 26, 23] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Deportes Quindío tabela [21, 7, 8, 6, 26, 21] jogos [21, 8, 7, 6, 27, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:39: Junior de Barranquilla tabela [21, 7, 8, 6, 25, 24] jogos [21, 6, 8, 7, 25, 27] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Millonarios tabela [21, 7, 7, 7, 36, 29] jogos [21, 8, 7, 6, 38, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:39: Independiente Santa Fe tabela [21, 7, 7, 7, 35, 33] jogos [21, 7, 8, 6, 32, 28] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:39: Atlético Bucaramanga tabela [21, 7, 5, 9, 26, 36] jogos [21, 7, 5, 9, 27, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:39: Once Caldas tabela [21, 7, 4, 10, 34, 28] jogos [21, 7, 4, 10, 34, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:39: Deportes Tolima tabela [21, 3, 7, 11, 16, 37] jogos [21, 3, 6, 12, 17, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col79:103: Unión Magdalena tabela [6, 2, 3, 1, 5, 2] jogos [6, 2, 3, 1, 6, 3] — a outra tabela publicada (col79) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col79:103: Deportivo Cali tabela [6, 1, 4, 1, 5, 4] jogos [6, 1, 4, 1, 6, 5] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — América de Cali x Deportivo Cali (1979-06-28): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- corrigido — Deportivo Cali x América de Cali (1979-07-01): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)

### 1980

- tabela publicada x jogos — col80:16: Deportes Quindío tabela [26, 9, 9, 8, 25, 29] jogos [26, 9, 9, 8, 24, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:16: Unión Magdalena tabela [26, 8, 8, 10, 27, 36] jogos [26, 8, 8, 10, 25, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:28: Cúcuta Deportivo tabela [26, 3, 9, 14, 21, 39] jogos [26, 3, 10, 13, 21, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:38: Deportivo Pereira tabela [21, 6, 9, 6, 38, 39] jogos [21, 7, 8, 6, 38, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:38: Once Caldas tabela [21, 4, 10, 7, 18, 22] jogos [21, 4, 10, 7, 18, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:38: Deportes Quindío tabela [21, 2, 10, 9, 15, 24] jogos [21, 2, 10, 9, 16, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:50: Cúcuta Deportivo tabela [21, 10, 8, 3, 33, 22] jogos [21, 10, 8, 3, 34, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:50: Deportes Tolima tabela [21, 9, 8, 4, 29, 21] jogos [21, 9, 8, 4, 30, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:50: Unión Magdalena tabela [21, 6, 7, 8, 19, 24] jogos [21, 4, 8, 9, 20, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:73: América de Cali tabela [6, 4, 1, 1, 9, 4] jogos [6, 2, 1, 3, 9, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:73: Deportivo Cali tabela [6, 3, 2, 1, 11, 6] jogos [6, 6, 0, 0, 16, 7] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:73: Millonarios tabela [6, 2, 1, 3, 8, 13] jogos [6, 2, 1, 3, 9, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:73: Cúcuta Deportivo tabela [6, 0, 2, 4, 6, 11] jogos [6, 0, 2, 4, 4, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:80: Junior de Barranquilla tabela [6, 3, 2, 1, 8, 10] jogos [6, 1, 4, 1, 4, 3] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:80: Atlético Nacional tabela [6, 3, 1, 2, 11, 9] jogos [6, 1, 2, 3, 6, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:80: Once Caldas tabela [6, 2, 1, 3, 17, 13] jogos [6, 2, 3, 1, 6, 4] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:80: Deportivo Pereira tabela [6, 1, 2, 3, 8, 12] jogos [6, 2, 3, 1, 4, 4] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:90: Junior de Barranquilla tabela [6, 3, 3, 0, 9, 6] jogos [6, 2, 4, 0, 7, 4] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:90: Deportivo Cali tabela [6, 2, 3, 1, 11, 10] jogos [6, 2, 3, 1, 10, 7] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:90: América de Cali tabela [6, 1, 2, 3, 5, 7] jogos [6, 1, 2, 3, 8, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col80:90: Atlético Nacional tabela [6, 0, 4, 2, 9, 11] jogos [6, 1, 3, 2, 9, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Junior de Barranquilla x Deportivo Cali (1980-07-16): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- corrigido — Deportivo Cali x Junior de Barranquilla (1980-07-20): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)

### 1981

- tabela publicada x jogos — col81:15: Atlético Nacional tabela [26, 13, 7, 6, 41, 32] jogos [26, 14, 7, 5, 45, 33] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:15: Unión Magdalena tabela [26, 9, 9, 8, 23, 28] jogos [26, 8, 9, 9, 23, 28] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:15: Independiente Medellín tabela [26, 7, 8, 11, 26, 36] jogos [26, 6, 8, 12, 25, 37] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:15: Once Caldas tabela [26, 7, 6, 13, 32, 41] jogos [26, 7, 6, 13, 31, 41] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:63: América de Cali tabela [6, 4, 1, 1, 12, 1] jogos [6, 4, 1, 1, 8, 3] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:63: Junior de Barranquilla tabela [6, 4, 1, 1, 11, 9] jogos [6, 0, 3, 3, 2, 7] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:63: Millonarios tabela [6, 1, 1, 4, 5, 12] jogos [6, 4, 1, 1, 11, 6] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:63: Unión Magdalena tabela [6, 1, 1, 4, 3, 9] jogos [6, 1, 1, 4, 4, 9] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:70: Deportes Tolima tabela [6, 2, 4, 0, 6, 4] jogos [6, 1, 1, 4, 3, 7] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:70: Atlético Nacional tabela [6, 2, 3, 1, 8, 4] jogos [6, 3, 1, 2, 7, 6] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:70: Deportivo Cali tabela [6, 2, 2, 2, 10, 9] jogos [6, 4, 0, 2, 10, 4] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:70: Deportes Quindío tabela [6, 0, 3, 3, 3, 10] jogos [6, 2, 2, 2, 3, 6] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col81:80: Atlético Nacional tabela [6, 3, 2, 1, 7, 6] jogos [6, 4, 1, 1, 9, 5] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:80: Deportes Tolima tabela [6, 2, 2, 2, 10, 9] jogos [6, 2, 1, 3, 4, 5] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:80: América de Cali tabela [6, 1, 3, 2, 6, 8] jogos [6, 3, 2, 1, 5, 2] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col81:80: Junior de Barranquilla tabela [6, 1, 3, 2, 10, 10] jogos [6, 0, 2, 4, 3, 9] — a outra tabela publicada (col81) fecha com os jogos: o erro é desta tabela

### 1982

- tabela publicada x jogos — col82:15: Deportivo Cali tabela [26, 13, 7, 6, 45, 30] jogos [26, 14, 6, 6, 45, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:15: Cúcuta Deportivo tabela [26, 10, 6, 10, 36, 38] jogos [26, 10, 5, 11, 35, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:39: Deportivo Pereira tabela [21, 7, 10, 4, 27, 22] jogos [21, 7, 10, 4, 28, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:39: Independiente Santa Fe tabela [21, 6, 8, 7, 41, 36] jogos [21, 5, 8, 8, 41, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:49: Millonarios tabela [21, 12, 5, 4, 33, 12] jogos [21, 12, 5, 4, 35, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:49: Atlético Bucaramanga tabela [21, 7, 1, 13, 26, 42] jogos [21, 7, 1, 13, 26, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:62: Millonarios tabela [14, 6, 3, 5, 17, 15] jogos [14, 5, 3, 6, 15, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col82:62: Independiente Medellín tabela [14, 4, 3, 7, 13, 18] jogos [14, 5, 3, 6, 16, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Deportivo Cali x América de Cali (1982-07-18): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- corrigido — América de Cali x Deportivo Cali (1982-07-20): final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)

### 1983

- tabela publicada x jogos — col83:16: Deportivo Cali tabela [14, 6, 4, 4, 18, 14] jogos [14, 6, 5, 3, 17, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:16: Independiente Santa Fe tabela [14, 6, 1, 7, 15, 18] jogos [14, 6, 1, 7, 15, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:16: Deportes Tolima tabela [14, 4, 5, 5, 14, 19] jogos [14, 4, 4, 6, 14, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:16: Unión Magdalena tabela [14, 4, 4, 6, 20, 21] jogos [14, 3, 6, 5, 18, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:26: Millonarios tabela [14, 7, 4, 3, 21, 17] jogos [14, 7, 4, 3, 19, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:36: Once Caldas tabela [2, 1, 1, 0, 4, 2] jogos [2, 1, 1, 0, 2, 1] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:36: Junior de Barranquilla tabela [2, 0, 1, 1, 2, 4] jogos [2, 1, 0, 1, 2, 2] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:36: Independiente Medellín tabela [2, 1, 0, 1, 2, 2] jogos [2, 0, 1, 1, 1, 2] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Junior de Barranquilla tabela [26, 13, 8, 5, 48, 25] jogos [26, 13, 8, 5, 48, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Independiente Santa Fe tabela [26, 14, 4, 8, 54, 36] jogos [26, 14, 5, 7, 53, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Independiente Medellín tabela [26, 7, 14, 5, 29, 28] jogos [26, 6, 15, 5, 27, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Deportivo Pereira tabela [26, 11, 4, 11, 35, 39] jogos [26, 10, 4, 12, 34, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Deportivo Cali tabela [26, 10, 5, 11, 29, 30] jogos [26, 10, 5, 11, 29, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Unión Magdalena tabela [26, 8, 8, 10, 24, 29] jogos [26, 8, 7, 11, 23, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Once Caldas tabela [26, 5, 14, 7, 28, 31] jogos [26, 7, 13, 6, 28, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:46: Deportes Quindío tabela [26, 4, 5, 17, 16, 42] jogos [26, 4, 5, 17, 15, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:78: América de Cali tabela [14, 7, 5, 2, 23, 15] jogos [14, 6, 6, 2, 21, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col83:78: Independiente Medellín tabela [14, 1, 5, 8, 8, 16] jogos [14, 1, 6, 7, 7, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1984

- tabela publicada x jogos — col84:16: Atlético Nacional tabela [14, 9, 2, 3, 19, 8] jogos [14, 10, 1, 3, 19, 7] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:16: Deportivo Pereira tabela [14, 4, 2, 8, 15, 19] jogos [14, 4, 1, 9, 14, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col84:28: Millonarios tabela [14, 5, 6, 3, 23, 25] jogos [14, 5, 6, 3, 23, 15] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:36: América de Cali tabela [2, 2, 0, 0, 3, 0] jogos [2, 1, 0, 1, 4, 3] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:36: Junior de Barranquilla tabela [2, 0, 0, 2, 0, 3] jogos [2, 1, 0, 1, 4, 1] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:36: Atlético Nacional tabela [2, 1, 1, 0, 4, 3] jogos [2, 1, 0, 1, 1, 4] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:36: Deportes Tolima tabela [2, 0, 1, 1, 3, 4] jogos [2, 1, 0, 1, 3, 4] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:46: Independiente Medellín tabela [26, 10, 11, 5, 32, 18] jogos [26, 10, 11, 5, 34, 18] — a outra tabela publicada (col84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col84:46: Independiente Santa Fe tabela [26, 9, 8, 9, 36, 31] jogos [26, 9, 8, 9, 36, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1985

- tabela publicada x jogos — col85:16: Millonarios tabela [14, 5, 6, 3, 15, 12] jogos [14, 3, 7, 4, 12, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:16: Atlético Bucaramanga tabela [14, 5, 5, 4, 26, 21] jogos [14, 5, 5, 4, 27, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:16: Unión Magdalena tabela [14, 4, 5, 5, 13, 14] jogos [14, 4, 5, 5, 13, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:16: Deportivo Pereira tabela [14, 2, 8, 4, 18, 19] jogos [14, 3, 8, 3, 20, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:16: Deportes Tolima tabela [14, 1, 8, 5, 11, 21] jogos [14, 0, 8, 6, 9, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:26: Once Caldas tabela [14, 5, 5, 4, 15, 18] jogos [14, 5, 4, 5, 14, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:26: Independiente Santa Fe tabela [14, 2, 6, 6, 22, 26] jogos [14, 3, 6, 5, 22, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:26: Deportes Quindío tabela [14, 3, 3, 8, 13, 22] jogos [14, 4, 3, 7, 13, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:36: Junior de Barranquilla tabela [2, 1, 1, 0, 2, 0] jogos [2, 2, 0, 0, 6, 2] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:36: Independiente Medellín tabela [2, 0, 1, 1, 0, 2] jogos [2, 1, 1, 0, 2, 1] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:36: América de Cali tabela [2, 1, 1, 0, 4, 3] jogos [4, 1, 1, 2, 3, 6] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — col85:36: Deportivo Cali tabela [2, 0, 1, 1, 3, 4] jogos [4, 0, 2, 2, 1, 3] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — col85:46: América de Cali tabela [26, 16, 6, 4, 38, 18] jogos [26, 17, 5, 4, 39, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Deportivo Cali tabela [26, 12, 12, 2, 36, 17] jogos [26, 11, 13, 2, 33, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Atlético Nacional tabela [26, 12, 6, 8, 43, 30] jogos [26, 12, 7, 7, 42, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Deportes Quindío tabela [26, 11, 7, 8, 30, 33] jogos [26, 10, 7, 9, 27, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Millonarios tabela [26, 10, 9, 7, 41, 39] jogos [26, 10, 9, 7, 43, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Independiente Medellín tabela [26, 10, 6, 10, 39, 32] jogos [26, 10, 5, 11, 39, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Deportivo Pereira tabela [26, 9, 8, 9, 40, 38] jogos [26, 10, 8, 8, 43, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Atlético Bucaramanga tabela [26, 9, 7, 10, 39, 39] jogos [26, 9, 6, 11, 38, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Junior de Barranquilla tabela [26, 9, 4, 13, 37, 33] jogos [26, 9, 4, 13, 37, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Once Caldas tabela [26, 7, 6, 13, 23, 37] jogos [26, 7, 6, 13, 23, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:46: Independiente Santa Fe tabela [26, 6, 4, 16, 28, 52] jogos [26, 7, 3, 16, 32, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:78: Deportivo Cali tabela [14, 8, 3, 3, 22, 8] jogos [14, 8, 3, 3, 20, 7] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:78: Junior de Barranquilla tabela [14, 5, 6, 3, 20, 17] jogos [14, 6, 5, 3, 19, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:78: Independiente Medellín tabela [14, 4, 5, 5, 22, 20] jogos [14, 4, 4, 6, 20, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:78: Unión Magdalena tabela [14, 2, 3, 9, 16, 27] jogos [14, 2, 3, 9, 15, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col85:78: Atlético Bucaramanga tabela [14, 2, 3, 9, 20, 34] jogos [14, 2, 3, 9, 20, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1986

- tabela publicada x jogos — col86:36: Junior de Barranquilla tabela [2, 0, 2, 0, 1, 1] jogos [0, 0, 0, 0, 0, 0] — faltam 2 jogo(s) do clube na página
- tabela publicada x jogos — col86:36: Independiente Medellín tabela [2, 0, 2, 0, 1, 1] jogos [3, 0, 1, 2, 2, 6] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — col86:36: Millonarios tabela [2, 1, 0, 1, 3, 2] jogos [4, 1, 2, 1, 4, 2] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — col86:36: América de Cali tabela [2, 1, 0, 1, 2, 3] jogos [3, 2, 1, 0, 3, 1] — sobram 1 jogo(s) do clube na página
- linha lida como jogo e descartada (clube não reconhecido): wiki-es_1986:733 «América x »

### 1987

- sem ocorrências

### 1988

- tabela publicada x jogos — col88:18: Deportes Tolima tabela [8, 1, 3, 4, 11, 22] jogos [8, 1, 3, 4, 11, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col88:26: Deportes Quindío tabela [8, 1, 5, 2, 6, 9] jogos [8, 1, 5, 2, 7, 10] — a outra tabela publicada (col88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col88:26: Once Caldas tabela [8, 1, 3, 4, 5, 7] jogos [8, 1, 3, 4, 6, 8] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col88:45: Atlético Nacional tabela [4, 2, 2, 0, 5, 2] jogos [4, 1, 3, 0, 3, 2] — a outra tabela publicada (col88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col88:45: Deportivo Pereira tabela [4, 0, 2, 2, 1, 4] jogos [4, 0, 3, 1, 1, 2] — a outra tabela publicada (col88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col88:69: Once Caldas tabela [4, 0, 2, 2, 5, 9] jogos [4, 0, 1, 3, 5, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1989

- título não concedido: a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega (RSSSF)

### 1990

- tabela publicada x jogos — col90:17: Independiente Santa Fe tabela [12, 5, 6, 1, 19, 8] jogos [12, 4, 7, 1, 17, 7] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:17: Atlético Bucaramanga tabela [12, 5, 3, 4, 9, 9] jogos [12, 5, 3, 4, 9, 8] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:17: Deportivo Cali tabela [12, 3, 6, 3, 17, 13] jogos [12, 3, 6, 3, 14, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:17: Deportes Tolima tabela [12, 2, 6, 4, 10, 14] jogos [12, 2, 7, 3, 9, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:17: Once Caldas tabela [12, 4, 1, 7, 13, 24] jogos [12, 4, 1, 7, 13, 21] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:17: Deportivo Pereira tabela [12, 3, 3, 6, 8, 15] jogos [11, 2, 3, 6, 7, 15] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col90:17: Cúcuta Deportivo tabela [12, 0, 6, 6, 6, 14] jogos [11, 0, 6, 5, 6, 13] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col90:36: Independiente Medellín tabela [28, 14, 10, 4, 36, 22] jogos [28, 15, 9, 4, 38, 23] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:36: Deportivo Cali tabela [28, 11, 12, 5, 29, 29] jogos [28, 11, 12, 5, 30, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:36: Atlético Nacional tabela [28, 11, 10, 7, 36, 26] jogos [28, 11, 9, 8, 36, 27] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:36: Independiente Santa Fe tabela [28, 10, 9, 9, 33, 38] jogos [28, 10, 9, 9, 34, 39] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:36: Deportes Tolima tabela [28, 8, 7, 13, 21, 34] jogos [28, 8, 7, 13, 22, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:55: Independiente Medellín tabela [40, 18, 14, 8, 50, 37] jogos [40, 19, 13, 8, 52, 38] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:55: Atlético Bucaramanga tabela [40, 20, 9, 11, 49, 36] jogos [40, 20, 9, 11, 49, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:55: Atlético Nacional tabela [40, 16, 15, 9, 55, 41] jogos [40, 16, 14, 10, 55, 42] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:55: Deportivo Cali tabela [40, 14, 18, 8, 46, 42] jogos [40, 14, 18, 8, 44, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:55: Independiente Santa Fe tabela [40, 15, 15, 10, 52, 46] jogos [40, 14, 16, 10, 51, 46] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:55: Once Caldas tabela [40, 15, 13, 12, 44, 51] jogos [40, 15, 13, 12, 44, 48] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:55: Deportivo Pereira tabela [40, 13, 13, 14, 38, 45] jogos [39, 12, 13, 14, 37, 45] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col90:55: Deportes Tolima tabela [40, 10, 13, 17, 31, 48] jogos [40, 10, 14, 16, 31, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:55: Cúcuta Deportivo tabela [40, 6, 12, 22, 22, 59] jogos [39, 6, 12, 21, 22, 58] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — col90:83: América de Cali tabela [6, 3, 1, 2, 9, 4] jogos [6, 3, 1, 2, 8, 4] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:83: Deportivo Cali tabela [6, 3, 0, 3, 9, 12] jogos [6, 3, 0, 3, 9, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:97: Atlético Nacional tabela [6, 3, 1, 2, 7, 3] jogos [6, 3, 1, 2, 7, 4] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col90:97: Atlético Bucaramanga tabela [6, 1, 3, 2, 5, 10] jogos [6, 1, 3, 2, 5, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — col90:97: Independiente Santa Fe tabela [6, 0, 3, 3, 5, 13] jogos [6, 0, 3, 3, 5, 11] — a outra tabela publicada (col90) fecha com os jogos: o erro é desta tabela

### 1991

- sem ocorrências

### 1992

- sem ocorrências

### 1993

- sem ocorrências

### 1994

- sem ocorrências

### 1995

- torneio de transição para o calendário europeu (Torneo Nivelación)

### 1995/96

- tabela publicada x jogos — col96:324: Deportivo Cali tabela [18, 11, 4, 3, 37, 20] jogos [14, 9, 3, 2, 32, 16] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — col96:324: Deportes Tolima tabela [18, 8, 5, 5, 22, 24] jogos [14, 6, 4, 4, 14, 18] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:324: Unión Magdalena tabela [18, 8, 3, 7, 21, 20] jogos [14, 6, 2, 6, 17, 18] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — col96:324: Millonarios tabela [18, 7, 6, 5, 26, 18] jogos [14, 5, 5, 4, 18, 14] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — col96:324: Once Caldas tabela [18, 5, 8, 5, 23, 20] jogos [14, 5, 6, 3, 20, 13] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:324: Atlético Bucaramanga tabela [18, 6, 5, 7, 18, 20] jogos [14, 4, 3, 7, 14, 20] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:324: Deportes Quindío tabela [18, 6, 3, 9, 26, 32] jogos [14, 5, 2, 7, 21, 24] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:324: Independiente Medellín tabela [18, 2, 5, 11, 17, 32] jogos [14, 2, 3, 9, 14, 27] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Atlético Nacional tabela [18, 9, 5, 4, 29, 23] jogos [14, 7, 4, 3, 23, 18] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: América de Cali tabela [18, 8, 6, 4, 39, 24] jogos [14, 6, 5, 3, 33, 19] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Junior de Barranquilla tabela [18, 7, 4, 7, 23, 26] jogos [14, 6, 3, 5, 21, 22] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — col96:337: Atlético Huila tabela [18, 6, 6, 6, 29, 35] jogos [14, 5, 6, 3, 26, 26] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Independiente Santa Fe tabela [18, 6, 5, 7, 28, 27] jogos [14, 4, 4, 6, 19, 21] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Envigado tabela [18, 5, 7, 6, 19, 19] jogos [14, 4, 5, 5, 16, 15] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Deportivo Pereira tabela [18, 3, 9, 6, 19, 24] jogos [14, 2, 7, 5, 15, 21] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:337: Cortuluá tabela [18, 2, 9, 7, 17, 29] jogos [14, 2, 6, 6, 14, 25] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:931: Millonarios tabela [6, 4, 0, 2, 11, 6] jogos [0, 0, 0, 0, 0, 0] — faltam 6 jogo(s) do clube na página
- tabela publicada x jogos — col96:931: Atlético Nacional tabela [6, 1, 2, 3, 6, 10] jogos [2, 1, 0, 1, 2, 4] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:931: América de Cali tabela [6, 1, 2, 3, 4, 9] jogos [2, 1, 0, 1, 4, 2] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:967: Independiente Santa Fe tabela [6, 4, 2, 0, 11, 4] jogos [4, 2, 2, 0, 6, 3] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:967: Envigado tabela [6, 3, 2, 1, 6, 3] jogos [4, 1, 2, 1, 3, 3] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:967: Cortuluá tabela [6, 1, 3, 2, 6, 8] jogos [6, 0, 4, 2, 5, 8] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col96:967: Independiente Medellín tabela [6, 0, 1, 5, 5, 13] jogos [2, 0, 2, 0, 2, 2] — a outra tabela publicada (col96) fecha com os jogos: o erro é desta tabela

### 1996/97

- sem ocorrências

### 1998

- sem ocorrências

### 1999

- tabela publicada x jogos — col99:746: Atlético Nacional tabela [50, 23, 16, 11, 70, 53] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (col99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col99:750: América de Cali tabela [44, 18, 15, 11, 70, 53] jogos [46, 18, 17, 11, 71, 54] — a outra tabela publicada (col99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col99:750: Deportivo Pasto tabela [50, 14, 16, 20, 72, 76] jogos [50, 14, 16, 20, 72, 77] — a outra tabela publicada (col99) fecha com os jogos: o erro é desta tabela
- corrigido — Independiente Medellín x Atlético Nacional (1999-12-08): final do Clausura (Medellín x Nacional), não a do ano (CO-014)
- corrigido — Atlético Nacional x Independiente Medellín (1999-12-12): final do Clausura (Medellín x Nacional), não a do ano (CO-014)
- linha lida como jogo e descartada (clube não reconhecido): col99:736 «América: Oviedo x (failed), Pérez 2-0 (failed), Moreno 3-1»
- linha lida como jogo e descartada (clube não reconhecido): col99:739 «Nacional won x on penalties»

### 2000

- ogol: 12 jogos casados (edição 28964 do ogol, 12 jogos)
- placar diferente no ogol — Junior de Barranquilla x América de Cali (2000-12-13): RSSSF 0-0, ogol 1-0; fica o da RSSSF

### 2001

- sem ocorrências

### 2002 Apertura

- sem ocorrências

### 2002 Finalización

- decidido fora de campo — Junior de Barranquilla Atlético Nacional (2002-07-07): awarded 0-2, originally 1-0

### 2003 Apertura

- tabela publicada x jogos — col03:17: Junior de Barranquilla tabela [18, 8, 4, 6, 19, 17] jogos [18, 8, 3, 7, 19, 18] — a outra tabela publicada (col03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col03:17: Deportivo Pereira tabela [18, 7, 4, 7, 22, 26] jogos [18, 7, 5, 6, 22, 25] — a outra tabela publicada (col03) fecha com os jogos: o erro é desta tabela

### 2003 Finalización

- sem ocorrências

### 2004 Apertura

- sem ocorrências

### 2004 Finalización

- decidido fora de campo — Millonarios Independiente Medellín (2004-08-07): awarded 0-3; originally 1-1

### 2005 Apertura

- sem ocorrências

### 2005 Finalización

- ESPN: 186 jogos casados
- tabela publicada x jogos — col05:583: Once Caldas tabela [18, 8, 5, 5, 25, 21] jogos [17, 8, 4, 5, 25, 21] — a outra tabela publicada (col05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col05:583: Atlético Bucaramanga tabela [18, 7, 6, 5, 24, 16] jogos [17, 7, 5, 5, 24, 16] — faltam 1 jogo(s) do clube na página

### 2006 Apertura

- ESPN: 188 jogos casados

### 2006 Finalización

- ESPN: 188 jogos casados
- tabela publicada x jogos — col06:484: Boyacá Chicó tabela [17, 10, 2, 5, 22, 13] jogos [18, 10, 2, 6, 22, 15] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Deportes Tolima tabela [17, 9, 4, 4, 28, 18] jogos [18, 10, 4, 4, 31, 19] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Deportivo Pasto tabela [17, 9, 3, 5, 23, 13] jogos [18, 9, 3, 6, 23, 15] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Independiente Medellín tabela [17, 9, 2, 6, 26, 21] jogos [18, 10, 2, 6, 29, 22] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Atlético Huila tabela [17, 8, 4, 5, 23, 16] jogos [18, 9, 4, 5, 25, 17] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Cúcuta Deportivo tabela [17, 8, 4, 5, 21, 18] jogos [18, 9, 4, 5, 22, 18] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Atlético Nacional tabela [17, 8, 4, 5, 18, 15] jogos [18, 9, 4, 5, 20, 15] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Millonarios tabela [17, 8, 3, 6, 21, 16] jogos [18, 8, 3, 7, 23, 19] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Deportivo Cali tabela [17, 6, 7, 4, 22, 18] jogos [18, 6, 7, 5, 23, 21] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Independiente Santa Fe tabela [17, 6, 6, 5, 33, 28] jogos [18, 6, 6, 6, 34, 30] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Deportes Quindío tabela [17, 7, 3, 7, 23, 25] jogos [18, 8, 3, 7, 24, 25] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Real Cartagena tabela [17, 6, 4, 7, 15, 17] jogos [18, 7, 4, 7, 17, 17] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Deportivo Pereira tabela [17, 5, 4, 8, 20, 22] jogos [18, 6, 4, 8, 23, 24] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Once Caldas tabela [17, 5, 4, 8, 22, 28] jogos [18, 5, 4, 9, 23, 31] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Junior de Barranquilla tabela [17, 4, 5, 8, 17, 29] jogos [18, 5, 5, 8, 19, 29] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Atlético Bucaramanga tabela [17, 4, 4, 9, 22, 31] jogos [18, 4, 4, 10, 22, 32] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: América de Cali tabela [17, 3, 4, 10, 20, 31] jogos [18, 3, 4, 11, 20, 33] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col06:484: Envigado tabela [17, 3, 3, 11, 14, 31] jogos [18, 3, 3, 12, 14, 32] — a outra tabela publicada (col06) fecha com os jogos: o erro é desta tabela

### 2007 Apertura

- ESPN: 188 jogos casados

### 2007 Finalización

- ESPN: 186 jogos casados
- abandonado/suspenso, sem valer — Real Cartagena Junior de Barranquilla (2007-09-15): abandoned at 0-0 in 25' due to rain

### 2008 Apertura

- ESPN: 188 jogos casados
- corrigido — Independiente Medellín x Boyacá Chicó (2008-06-07): jogo suspenso e completado depois: fica a linha do jogo completo (CO-021)

### 2008 Finalización

- ESPN: 188 jogos casados

### 2009 Apertura

- ESPN: 179 jogos casados
- decidido fora de campo — Deportivo Cali Internacional de Bogotá (2009-02-22): awarded 3-0, originally 2-3
- abandonado/suspenso, sem valer — Envigado Junior de Barranquilla (2009-04-11): abandoned at 0-0 in 8'

### 2009 Finalización

- ESPN: 188 jogos casados
- decidido fora de campo — Independiente Santa Fe Independiente Medellín (2009-08-08): awarded 0-3, originally 2-1
- decidido fora de campo — Deportivo Pasto Real Cartagena (2009-10-25): awarded 0-3, originally 1-0
- abandonado/suspenso, sem valer — Atlético Huila Junior de Barranquilla (2009-10-31): abandoned at 1-1 in 68'

### 2010 Apertura

- ESPN: 167 jogos casados

### 2010 Finalización

- ESPN: 188 jogos casados
- abandonado/suspenso, sem valer — Deportes Quindío Deportivo Cali (2010-08-15): abandoned at 0-0 in 60'

### 2011 Apertura

- jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- ESPN: 176 jogos casados

### 2011 Finalización

- jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- ESPN: 176 jogos casados

### 2012 Apertura

- jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- ESPN: 188 jogos casados

### 2012 Finalización

- jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- ESPN: 188 jogos casados
- tabela publicada x jogos — col2012:86: Junior de Barranquilla tabela [18, 8, 8, 2, 27, 14] jogos [18, 8, 8, 2, 27, 15] — a outra tabela publicada (col2012) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col2012:86: Deportes Tolima tabela [18, 8, 5, 5, 27, 19] jogos [18, 8, 5, 5, 26, 20] — a outra tabela publicada (col2012) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — col2012:86: Real Cartagena tabela [18, 3, 3, 12, 13, 34] jogos [18, 3, 3, 12, 15, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2013 Apertura

- ESPN: 188 jogos casados

### 2013 Finalización

- ESPN: 119 jogos casados
- corrigido — Once Caldas x Millonarios (2013-11-27): jogo suspenso pela chuva e completado depois (CO-021)

### 2014 Apertura

- ESPN: 176 jogos casados

### 2014 Finalización

- ESPN: 188 jogos casados

### 2015 Apertura

- ESPN: 214 jogos casados

### 2015 Finalización

- ESPN: 213 jogos casados
- decidido fora de campo — Deportivo Cali Jaguares de Córdoba (2015-07-12): awarded 0-3, originally 0-1; Cali fielded Oct 11]                                   suspended player

### 2016 Apertura

- ESPN: 214 jogos casados

### 2016 Finalización

- ESPN: 214 jogos casados
- decidido fora de campo — Millonarios Atlético Bucaramanga (2016-08-10): awarded 0-3; abandoned at 0-1 in 88' due to crowd trouble

### 2017 Apertura

- ESPN: 214 jogos casados

### 2017 Finalización

- ESPN: 214 jogos casados

### 2018 Apertura

- ESPN: 185 jogos casados

### 2018 Finalización

- ESPN: 185 jogos casados

### 2019 Apertura

- ESPN: 226 jogos casados

### 2019 Finalización

- ESPN: 223 jogos casados
- decidido fora de campo — Águilas Doradas Deportes Tolima (2019-07-26): awarded 3-0; originally 0-2, Tolima

### 2020 Apertura

- ESPN: 214 jogos casados
- decidido fora de campo — Once Caldas Deportivo Pereira (2020-10-06): awarded 0-3, originally 2-2; Caldas
- decidido fora de campo — Cúcuta Deportivo América de Cali (2020-11-12): awarded 0-3, Cúcuta entered liquidation
- decidido fora de campo — Atlético Nacional Cúcuta Deportivo (2020-11-15): awarded 3-0, Cúcuta entered liquidation

### 2021 Apertura

- ESPN: 185 jogos casados

### 2021 Finalización

- ESPN: 226 jogos casados

### 2022 Apertura

- ESPN: 226 jogos casados
- decidido fora de campo — Unión Magdalena Atlético Bucaramanga (2022-02-15): awarded 0-3, originally 0-1
- decidido fora de campo — Unión Magdalena Junior de Barranquilla (2022-04-23): awarded 0-3; originally 1-1
- decidido fora de campo — Jaguares de Córdoba Independiente Medellín (2022-05-07): awarded 3-0

### 2022 Finalización

- ESPN: 226 jogos casados

### 2023 Apertura

- ESPN: 226 jogos casados
- decidido fora de campo — Once Caldas Alianza FC (2023-04-18): awarded 0-3; originally 1-2; Caldas

### 2023 Finalización

- ESPN: 226 jogos casados

### 2024 Apertura

- ESPN: 216 jogos casados
- decidido fora de campo — Patriotas Boyacá Deportivo Pereira (2024-03-10): awarded 0-3; abandoned at 0-2 in 64' due

### 2024 Finalización

- ESPN: 216 jogos casados
- decidido fora de campo — Deportivo Cali Deportivo Pasto (2024-09-02): awarded 0-3, originally 0-2
- decidido fora de campo — Atlético Nacional Junior de Barranquilla (2024-09-26): awarded 0-3; abandoned at 2-0 in 56' due

### 2025 Apertura

- jogos da Wikipédia em espanhol: a página da RSSSF só traz as tabelas
- ESPN: 225 jogos casados

### 2025 Finalización

- jogos da Wikipédia em espanhol: a página da RSSSF só traz as tabelas
- ESPN: 226 jogos casados

