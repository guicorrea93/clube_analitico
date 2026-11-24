# Campeonato Paraguaio (1ª divisão) — coleta de dados

Gerado por `python coleta/par-1/importar.py`. Pacote em `data/coleta/par-1/pacote/`.

**Edições:** 134, uma por título de campeão paraguaio da 1ª divisão, de 1906 a 2025, como na lista de campeões da RSSSF (`parachamp.html`) e na Wikipédia em inglês. Até 2007 um campeão por ano (sem campeonato em 1908, 1922 e 1932-1934); de 1996 a 2007 o Apertura e o Clausura são fases da edição anual, com a final entre os vencedores. De 2008 em diante, Apertura e Clausura dão título cada um: uma edição por torneio.

**Edições sem jogos (76):** 1906-1959, 1968-1980 e 1982-1995. Pesquisamos RSSSF, ogol, Wikipédias em espanhol, inglês e guarani, Transfermarkt, worldfootball, sites e livros paraguaios: nenhuma fonte pública traz os jogos completos desses anos (a RSSSF tem só alguns resultados soltos, "Known Results"). Decisão do Guilherme (21/11/2026): essas edições entram só com o campeão, o vice e a tabela da RSSSF quando há: completa em 1909, 1943, 1945, 1946, 1955, 1986 e 1994 (PY-031); parcial (posição e pontos, às vezes parte da campanha) nos outros anos; sem tabela, a classificação tem só o campeão e o vice. Os jogos soltos ficam de fora.

**Fora do pacote:** a Copa Paraguay, a Copa República, a Intermedia (2ª divisão), as liguillas e os jogos de promoção.

**Fontes:** RSSSF (uma página por temporada de 1960 em diante e a história da liga 1906-1959, `parahist.html`, em `data/coleta/par-1/rsssf/`: base de jogos de 1960-1967, 1981 e 1996 em diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas são a conferência); ESPN (liga `par.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol só tem jogos de 2005 em diante e não entrou.

**Clubes:** homônimos de outros países levam a cidade: Nacional de Asunción (o Nacional é o uruguaio), River Plate de Asunción, Sportivo San Lorenzo, Independiente de Campo Grande, Universal de Encarnación; o Guaraní é "Guaraní de Asunción" para não se confundir com o Guarani de Campinas. General Caballero (Zeballos Cué) e General Caballero JLM, e Cerro Porteño e Cerro Porteño PF, são clubes diferentes.

**Regras:** o placar é o da RSSSF. Jogo decidido no tribunal leva o placar dado (`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1906 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1907 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | lista de campeões e vices da RSSSF (parachamp.html) |
| 1909 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist) |
| 1910 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | lista de campeões e vices da RSSSF (parachamp.html) |
| 1911 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1912 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1913 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1914 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1915 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1916 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1917 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | lista de campeões e vices da RSSSF (parachamp.html) |
| 1918 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1919 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1920 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (parahist, tabela parcial) |
| 1921 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1923 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1924 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1925 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1926 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1927 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1928 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1929 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1930 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (parahist, tabela parcial) |
| 1931 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1935 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1936 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1937 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1938 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1939 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1940 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1941 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1942 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1943 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para43) |
| 1944 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1945 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para45) |
| 1946 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist) |
| 1947 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1948 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1949 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1950 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1951 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Sportivo Luqueño | RSSSF (parahist, tabela parcial) |
| 1952 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Presidente Hayes | RSSSF (parahist, tabela parcial) |
| 1953 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Sportivo Luqueño | RSSSF (parahist, tabela parcial) |
| 1954 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1955 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para55) |
| 1956 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1957 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1958 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1959 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1960 | 10 | 136 (136) | 439 | 0 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961 | 11 | 118 (118) | 384 | 0 | 2 / 0 | Cerro Porteño | RSSSF (para61) |
| 1962 | 11 | 110 (110) | 412 | 0 | 1 / 0 | Olimpia | RSSSF (para62) |
| 1963 | 11 | 114 (113) | 365 | 0 | 1 / 0 | Cerro Porteño | RSSSF (para63) |
| 1964 | 10 | 90 (90) | 223 | 0 | 1 / 0 | Guaraní de Asunción | RSSSF (para64) |
| 1965 | 9 | 76 (75) | 204 | 0 | 0 / 1 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 9 | 72 (72) | 187 | 0 | 1 / 0 | Cerro Porteño | RSSSF (para66) |
| 1967 | 9 | 110 (110) | 282 | 0 | 1 / 2 | Guaraní de Asunción | RSSSF (para67) |
| 1968 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1969 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (para69, tabela parcial) |
| 1970 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1971 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1972 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1973 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1974 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1975 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1976 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | lista de campeões e vices da RSSSF (parachamp.html) |
| 1977 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1978 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1979 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1980 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1981 | 10 | 141 (140) | 280 | 0 | 4 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1983 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1984 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | lista de campeões e vices da RSSSF (parachamp.html) |
| 1985 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1986 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Sol de América | RSSSF (para86) |
| 1987 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1988 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1989 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1990 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1991 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Sol de América | lista de campeões e vices da RSSSF (parachamp.html) |
| 1992 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | lista de campeões e vices da RSSSF (parachamp.html) |
| 1993 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1994 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (para94) |
| 1995 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1996 | 13 | 182 (182) | 519 | 0 | 0 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 | 13 | 190 (190) | 528 | 7 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 | 12 | 170 (170) | 472 | 0 | 6 / 4 | Olimpia | RSSSF (para98) |
| 1999 | 11 | 145 (145) | 398 | 12 | 6 / 3 | Olimpia | RSSSF (para99) |
| 2000 | 10 | 163 (163) | 437 | 120 | 3 / 1 | Olimpia | RSSSF (para00) |
| 2001 | 10 | 104 (104) | 295 | 278 | 2 / 0 | Cerro Porteño | RSSSF (para01) |
| 2002 | 10 | 151 (151) | 418 | 413 | 3 / 0 | Libertad | RSSSF (para02) |
| 2003 | 10 | 153 (152) | 398 | 394 | 5 / 0 | Libertad | RSSSF (para03) |
| 2004 | 10 | 180 (180) | 465 | 465 | 2 / 0 | Cerro Porteño | RSSSF (para04) |
| 2005 | 10 | 181 (180) | 462 | 462 | 3 / 0 | Cerro Porteño | RSSSF (para05) |
| 2006 | 11 | 222 (222) | 634 | 634 | 2 / 0 | Libertad | RSSSF (para06) |
| 2007 | 12 | 267 (266) | 676 | 671 | 2 / 0 | Libertad | RSSSF (para07) |
| 2008 Apertura | 12 | 132 (132) | 391 | 375 | 1 / 0 | Libertad | RSSSF (para08) |
| 2008 Clausura | 12 | 133 (133) | 341 | 341 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 12 | 134 (134) | 326 | 326 | 0 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Clausura | 12 | 132 (132) | 314 | 314 | 1 / 0 | Nacional de Asunción | RSSSF (para09) |
| 2010 Apertura | 12 | 132 (132) | 342 | 339 | 1 / 0 | Guaraní de Asunción | RSSSF (para2010) |
| 2010 Clausura | 12 | 132 (132) | 325 | 325 | 1 / 0 | Libertad | RSSSF (para2010) |
| 2011 Apertura | 12 | 132 (132) | 319 | 319 | 1 / 0 | Nacional de Asunción | RSSSF (para2011) |
| 2011 Clausura | 12 | 132 (132) | 369 | 369 | 1 / 0 | Olimpia | RSSSF (para2011) |
| 2012 Apertura | 12 | 132 (132) | 355 | 355 | 1 / 0 | Cerro Porteño | RSSSF (para2012) |
| 2012 Clausura | 12 | 132 (132) | 339 | 339 | 1 / 0 | Libertad | RSSSF (para2012) |
| 2013 Apertura | 12 | 132 (132) | 351 | 351 | 1 / 0 | Nacional de Asunción | RSSSF (para2013) |
| 2013 Clausura | 12 | 132 (132) | 362 | 362 | 1 / 0 | Cerro Porteño | RSSSF (para2013) |
| 2014 Apertura | 12 | 132 (132) | 385 | 371 | 1 / 0 | Libertad | RSSSF (para2014) |
| 2014 Clausura | 12 | 132 (132) | 341 | 334 | 1 / 0 | Libertad | RSSSF (para2014) |
| 2015 Apertura | 12 | 132 (132) | 372 | 372 | 1 / 0 | Cerro Porteño | RSSSF (para2015) |
| 2015 Clausura | 12 | 133 (133) | 386 | 386 | 1 / 0 | Olimpia | RSSSF (para2015) |
| 2016 Apertura | 12 | 132 (132) | 433 | 423 | 1 / 0 | Libertad | RSSSF (para2016) |
| 2016 Clausura | 12 | 132 (132) | 354 | 354 | 1 / 0 | Guaraní de Asunción | RSSSF (para2016) |
| 2017 Apertura | 12 | 133 (133) | 340 | 340 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2017 Clausura | 12 | 132 (132) | 329 | 326 | 1 / 0 | Cerro Porteño | RSSSF (para2017) |
| 2018 Apertura | 12 | 132 (132) | 381 | 378 | 1 / 0 | Olimpia | RSSSF (para2018) |
| 2018 Clausura | 12 | 132 (132) | 355 | 349 | 1 / 0 | Olimpia | RSSSF (para2018) |
| 2019 Apertura | 12 | 132 (132) | 381 | 378 | 1 / 0 | Olimpia | RSSSF (para2019) |
| 2019 Clausura | 12 | 132 (132) | 339 | 337 | 1 / 0 | Olimpia | RSSSF (para2019) |
| 2020 Apertura | 12 | 132 (132) | 347 | 344 | 1 / 0 | Cerro Porteño | RSSSF (para2020) |
| 2020 Clausura | 12 | 73 (73) | 198 | 175 | 1 / 0 | Olimpia | RSSSF (para2020) |
| 2021 Apertura | 10 | 90 (90) | 234 | 234 | 1 / 0 | Libertad | RSSSF (para2021) |
| 2021 Clausura | 10 | 90 (90) | 222 | 218 | 1 / 0 | Cerro Porteño | RSSSF (para2021) |
| 2022 Apertura | 12 | 132 (132) | 336 | 336 | 1 / 0 | Libertad | RSSSF (para2022) |
| 2022 Clausura | 12 | 133 (133) | 323 | 323 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2023 Apertura | 12 | 132 (132) | 317 | 317 | 1 / 0 | Libertad | RSSSF (para2023) |
| 2023 Clausura | 12 | 133 (133) | 348 | 348 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2024 Apertura | 12 | 132 (132) | 339 | 336 | 1 / 0 | Libertad | RSSSF (para2024) |
| 2024 Clausura | 12 | 132 (132) | 277 | 277 | 1 / 0 | Olimpia | RSSSF (para2024) |
| 2025 Apertura | 12 | 132 (132) | 288 | 281 | 1 / 0 | Libertad | RSSSF (para2025) |
| 2025 Clausura | 12 | 132 (132) | 341 | 334 | 1 / 0 | Cerro Porteño | RSSSF (para2025) |
| 2026 Apertura | 12 | 132 (132) | 322 | 313 | 1 / 0 | Olimpia | RSSSF (para2026) |

## Conferência e correções, edição a edição

### 1906

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1907

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1909

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1910

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1911

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1912

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1913

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1914

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1915

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1916

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1917

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1918

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1919

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1920

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1921

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1923

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1924

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1925

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1926

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1927

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1928

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1929

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1930

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1931

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1935

- artilheiro pela lista da RSSSF (paratops); Pedro Osorio (Cerro Porteño) com 18 gols; a Wikipédia em espanhol dá 17. Sem 3ª fonte: fica a RSSSF (PY-019)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1936

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1937

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1938

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1939

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1940

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1941

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1942

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1943

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1944

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1945

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1946

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1947

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1948

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1949

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1950

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1951

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1952

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1953

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1954

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1955

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1956

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1957

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1958

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1959

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1960

- W.O./pontos para o visitante — Atlético Tembetary 2-2 Libertad (1960-04-17): awarded as a win to Libertad as Tembetary
- abandonado/suspenso, sem valer — Libertad Olimpia (1960-10-30): abandoned at 0-2 in 43'

### 1961

- sem ocorrências

### 1962

- artilheiro pela lista da RSSSF (paratops); Cecilio Martínez (Nacional) com 19 gols; a página do ano na RSSSF dá 18 e a Wikipédia em espanhol, 17 pelo Libertad (ela troca clube e gols com 1963). Três números diferentes: fica a lista da RSSSF (PY-019)

### 1963

- artilheiro pela lista da RSSSF (paratops); Juan Cabañas (Libertad) com 17 gols; a Wikipédia em espanhol dá 19 pelo Nacional (troca clube e gols com 1962). Fica a RSSSF (PY-019)
- abandonado/suspenso, sem valer — River Plate de Asunción Sol de América (1963-07-14): abandoned at 0-0 in 56'

### 1964

- sem ocorrências

### 1965

- tabela publicada x jogos — para65:228: Rubio Ñu tabela [16, 4, 6, 6, 23, 23] jogos [16, 3, 6, 7, 23, 23] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:228: Nacional de Asunción tabela [16, 3, 6, 7, 21, 19] jogos [16, 4, 6, 6, 21, 19] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — Rubio Ñu Nacional de Asunción (1965-11-26): abandoned at 1-2 in 73']     [at Cerro Porteño

### 1966

- sem ocorrências

### 1967

- artilheiro pela lista da RSSSF (paratops); Sebastián Fleitas (Libertad) com 18 gols, como a Wikipédia em espanhol; a página do ano na RSSSF dá 16 (PY-019)
- tabela publicada x jogos — para67:103: Guaraní de Asunción tabela [8, 6, 2, 0, 15, 2] jogos [24, 15, 8, 1, 34, 4] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Olimpia tabela [8, 5, 2, 1, 15, 8] jogos [24, 12, 9, 3, 35, 20] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Libertad tabela [8, 5, 1, 2, 19, 14] jogos [24, 15, 3, 6, 50, 31] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Cerro Porteño tabela [8, 4, 1, 3, 17, 13] jogos [24, 9, 5, 10, 33, 28] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Sol de América tabela [8, 3, 2, 3, 12, 9] jogos [24, 8, 8, 8, 34, 26] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Rubio Ñu tabela [8, 2, 3, 3, 11, 13] jogos [24, 5, 9, 10, 21, 32] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: River Plate de Asunción tabela [8, 1, 3, 4, 7, 12] jogos [24, 5, 7, 12, 33, 45] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Nacional de Asunción tabela [8, 1, 2, 5, 4, 14] jogos [24, 6, 5, 13, 25, 40] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:103: Sportivo San Lorenzo tabela [8, 0, 2, 6, 6, 21] jogos [24, 2, 8, 14, 14, 53] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Guaraní de Asunción tabela [16, 12, 4, 0, 29, 2] jogos [24, 15, 8, 1, 34, 4] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Libertad tabela [16, 10, 2, 4, 34, 25] jogos [24, 15, 3, 6, 50, 31] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Olimpia tabela [16, 8, 5, 3, 24, 14] jogos [24, 12, 9, 3, 35, 20] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Cerro Porteño tabela [16, 9, 2, 5, 28, 16] jogos [24, 9, 5, 10, 33, 28] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Sol de América tabela [16, 6, 5, 5, 28, 18] jogos [24, 8, 8, 8, 34, 26] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Rubio Ñu tabela [16, 3, 5, 8, 14, 24] jogos [24, 5, 9, 10, 21, 32] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: River Plate de Asunción tabela [16, 3, 4, 9, 20, 32] jogos [24, 5, 7, 12, 33, 45] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Sportivo San Lorenzo tabela [16, 2, 4, 10, 9, 35] jogos [24, 2, 8, 14, 14, 53] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para67:189: Nacional de Asunción tabela [16, 2, 3, 11, 11, 31] jogos [24, 6, 5, 13, 25, 40] — a outra tabela publicada (para67) fecha com os jogos: o erro é desta tabela

### 1968

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1969

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1970

- artilheiro pela lista da RSSSF (paratops); Saturnino Arrúa (Cerro Porteño) com 19 gols; a Wikipédia em espanhol dá 11. Fica a RSSSF (PY-019)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1971

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1972

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1973

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1974

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1975

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1976

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1977

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1978

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1979

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1980

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1981

- corrigido — Cerro Porteño x Guaraní de Asunción (1981-06-28): decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- corrigido — Olimpia x Resistencia (1981-06-28): decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- corrigido — Olimpia x Cerro Porteño (1981-07-03): decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- abandonado/suspenso, sem valer — Resistencia Nacional de Asunción (1981-09-13): abandoned at 1-1 in 66' due to incidents
- abandonado/suspenso, sem valer — Sol de América Olimpia (1981-11-29): abandoned at half-time due to heavy rain

### 1982

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1983

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1984

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1985

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1986

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1987

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1988

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1989

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1990

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1991

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1992

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1993

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1994

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1995

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

### 1996

- sem ocorrências

### 1997

- sem ocorrências

### 1998

- tabela publicada x jogos — para98:139: Olimpia tabela [2, 1, 0, 1, 5, 2] jogos [3, 2, 0, 1, 7, 2] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Guaraní de Asunción tabela [2, 1, 1, 0, 5, 4] jogos [3, 1, 1, 1, 5, 6] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Sportivo Luqueño tabela [2, 0, 1, 1, 2, 6] jogos [3, 0, 1, 2, 3, 8] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Sol de América tabela [2, 1, 0, 1, 4, 4] jogos [3, 2, 0, 1, 6, 5] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:146: Cerro Porteño tabela [2, 2, 0, 0, 6, 2] jogos [3, 3, 0, 0, 10, 2] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:146: 12 de Octubre tabela [2, 1, 1, 0, 4, 2] jogos [3, 1, 1, 1, 4, 6] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:146: Presidente Hayes tabela [2, 0, 0, 2, 2, 6] jogos [3, 0, 0, 3, 2, 7] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:146: Cerro Corá tabela [2, 0, 1, 1, 2, 4] jogos [3, 1, 1, 1, 3, 4] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:211: Nacional de Asunción tabela [11, 3, 6, 2, 17, 22] jogos [11, 2, 7, 2, 17, 23] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Cerro Porteño tabela [22, 16, 3, 3, 52, 19] jogos [28, 22, 3, 3, 70, 25] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Guaraní de Asunción tabela [22, 10, 6, 6, 31, 28] jogos [28, 12, 8, 8, 40, 38] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Olimpia tabela [22, 9, 5, 8, 28, 19] jogos [28, 13, 6, 9, 42, 25] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Sportivo Luqueño tabela [22, 8, 8, 6, 25, 29] jogos [25, 8, 9, 8, 28, 37] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Cerro Corá tabela [22, 8, 6, 8, 33, 34] jogos [28, 10, 9, 9, 42, 43] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: 12 de Octubre tabela [22, 8, 5, 9, 32, 35] jogos [28, 9, 6, 13, 38, 47] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Atlético Colegiales tabela [22, 8, 4, 10, 24, 29] jogos [25, 9, 5, 11, 28, 32] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Sol de América tabela [22, 5, 11, 6, 24, 25] jogos [28, 7, 12, 9, 34, 38] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Presidente Hayes tabela [22, 5, 9, 8, 23, 28] jogos [25, 5, 9, 11, 25, 35] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Sportivo San Lorenzo tabela [22, 5, 8, 9, 25, 33] jogos [25, 6, 8, 11, 31, 40] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- linha lida como jogo e descartada (clube não reconhecido): para98:432 «Promoted: Resistencia (won final versus Sportivo Iteño x on penalties)»

### 1999

- tabela publicada x jogos — para99:321: Cerro Porteño tabela [2, 1, 1, 0, 5, 2] jogos [3, 2, 1, 0, 6, 2] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Sportivo San Lorenzo tabela [2, 1, 0, 1, 3, 5] jogos [3, 1, 0, 2, 4, 7] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Cerro Corá tabela [2, 1, 1, 0, 4, 2] jogos [3, 2, 1, 0, 6, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Guaraní de Asunción tabela [2, 0, 0, 2, 2, 5] jogos [3, 0, 0, 3, 2, 6] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: Sportivo Luqueño tabela [2, 1, 1, 0, 4, 2] jogos [3, 1, 1, 1, 5, 4] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: Olimpia tabela [2, 1, 0, 1, 4, 3] jogos [3, 2, 0, 1, 5, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: 12 de Octubre tabela [2, 1, 1, 0, 2, 1] jogos [3, 1, 1, 1, 2, 2] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: Atlético Colegiales tabela [2, 0, 0, 2, 0, 4] jogos [3, 1, 0, 2, 2, 5] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Olimpia tabela [20, 12, 7, 1, 39, 17] jogos [26, 16, 8, 2, 53, 25] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Cerro Porteño tabela [20, 12, 5, 3, 46, 20] jogos [26, 16, 6, 4, 56, 27] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Sportivo Luqueño tabela [20, 11, 6, 3, 44, 27] jogos [26, 12, 7, 7, 49, 36] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Sportivo San Lorenzo tabela [20, 6, 11, 3, 26, 22] jogos [26, 7, 12, 7, 33, 35] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Guaraní de Asunción tabela [20, 6, 10, 4, 29, 27] jogos [26, 7, 10, 9, 34, 38] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: 12 de Octubre tabela [20, 5, 12, 3, 27, 22] jogos [26, 8, 13, 5, 34, 27] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Atlético Colegiales tabela [20, 6, 4, 10, 25, 31] jogos [26, 10, 4, 12, 36, 37] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Sol de América tabela [20, 5, 6, 9, 18, 22] jogos [23, 6, 6, 11, 22, 29] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Cerro Corá tabela [20, 4, 6, 10, 27, 39] jogos [23, 6, 7, 10, 33, 42] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela

### 2000

- tabela publicada x jogos — para00:280: Cerro Porteño tabela [9, 3, 5, 1, 16, 10] jogos [9, 3, 5, 1, 15, 9] — a outra tabela publicada (para00) fecha com os jogos: o erro é desta tabela

### 2001

- sem ocorrências

### 2002

- sem ocorrências

### 2003

- artilheiro pela lista da RSSSF (paratops); Erwin Ávalos (Cerro Porteño) com 17 gols; a Wikipédia em espanhol dá 16. Sem 3ª fonte: fica a RSSSF (PY-019)
- abandonado/suspenso, sem valer — Sportivo San Lorenzo Cerro Porteño (2003-03-01): abandoned at 0-3 in 70' due to light

### 2004

- sem ocorrências

### 2005

- ESPN: 84 jogos casados
- corrigido — General Caballero x Libertad (2005-11-26): General Caballero 2-1 em campo; pontos para o Libertad (jogador suspenso); a tabela conta os gols de campo (PY-029)
- abandonado/suspenso, sem valer — General Caballero Olimpia (2005-05-21): abandoned at 1-0 in 32'
- W.O./pontos para o visitante — General Caballero Libertad (2005-11-26): awarded to Libertad; originally 2-1, Gral. Caballero used suspended player

### 2006

- ESPN: 216 jogos casados

### 2007

- ESPN: 265 jogos casados
- abandonado/suspenso, sem valer — 2 de Mayo Sol de América (2007-05-18): abandoned at 1-1 in 68'

### 2008 Apertura

- ESPN: 131 jogos casados

### 2008 Clausura

- ESPN: 130 jogos casados
- abandonado/suspenso, sem valer — Guaraní de Asunción Libertad (2008-10-25): abandoned at 1-1 at half-time

### 2009 Apertura

- ESPN: 132 jogos casados
- abandonado/suspenso, sem valer — Tacuary Cerro Porteño (2009-04-04): abandoned at 0-1 at
- abandonado/suspenso, sem valer — 2 de Mayo 3 de Febrero (2009-05-29): abandoned at 0-1 in 32'

### 2009 Clausura

- ESPN: 132 jogos casados

### 2010 Apertura

- ESPN: 131 jogos casados

### 2010 Clausura

- ESPN: 132 jogos casados

### 2011 Apertura

- ESPN: 132 jogos casados

### 2011 Clausura

- ESPN: 132 jogos casados

### 2012 Apertura

- ESPN: 132 jogos casados

### 2012 Clausura

- ESPN: 131 jogos casados

### 2013 Apertura

- ESPN: 132 jogos casados

### 2013 Clausura

- ESPN: 132 jogos casados

### 2014 Apertura

- ESPN: 132 jogos casados

### 2014 Clausura

- ESPN: 132 jogos casados

### 2015 Apertura

- ESPN: 132 jogos casados

### 2015 Clausura

- ESPN: 132 jogos casados

### 2016 Apertura

- ESPN: 132 jogos casados

### 2016 Clausura

- ESPN: 132 jogos casados

### 2017 Apertura

- ESPN: 132 jogos casados
- abandonado/suspenso, sem valer — Olimpia Guaraní de Asunción (2017-05-08): abandoned at 0-0 in 10' due to bad weather

### 2017 Clausura

- ESPN: 132 jogos casados

### 2018 Apertura

- ESPN: 132 jogos casados
- decidido fora de campo — Independiente de Campo Grande Nacional de Asunción (2018-02-09): awarded 0-3, originally 4-0; Independiente

### 2018 Clausura

- ESPN: 132 jogos casados

### 2019 Apertura

- ESPN: 132 jogos casados
- decidido fora de campo — Sportivo San Lorenzo Libertad (2019-05-05): awarded 3-0; originally 3-4, Libertad fielded five

### 2019 Clausura

- ESPN: 132 jogos casados

### 2020 Apertura

- ESPN: 132 jogos casados
- decidido fora de campo — Guaraní de Asunción Olimpia (2020-02-08): awarded 0-3, originally 4-2; Guaraní fielded

### 2020 Clausura

- ESPN: 72 jogos casados

### 2021 Apertura

- ESPN: 90 jogos casados

### 2021 Clausura

- ESPN: 90 jogos casados

### 2022 Apertura

- ESPN: 132 jogos casados

### 2022 Clausura

- ESPN: 132 jogos casados
- abandonado/suspenso, sem valer — 12 de Octubre Sportivo Ameliano (2022-10-26): abandoned at 1-0 in 34' due to heavy rain

### 2023 Apertura

- ESPN: 132 jogos casados

### 2023 Clausura

- ESPN: 132 jogos casados
- abandonado/suspenso, sem valer — Guaireña General Caballero JLM (2023-09-01): abandoned at 1-1 at half-time

### 2024 Apertura

- ESPN: 132 jogos casados
- decidido fora de campo — Cerro Porteño 2 de Mayo (2024-01-29): awarded 0-3; abandoned at 0-0

### 2024 Clausura

- ESPN: 132 jogos casados

### 2025 Apertura

- ESPN: 132 jogos casados

### 2025 Clausura

- ESPN: 131 jogos casados

### 2026 Apertura

- decidido fora de campo — Olimpia Cerro Porteño (2026-04-19): awarded 3-0; abandoned at 0-0 in 30' due

