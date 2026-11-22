# Campeonato Paraguaio (1ª divisão) — coleta de dados

Gerado por `python coleta/par-1/importar.py`. Pacote em `data/coleta/par-1/pacote/`.

**Edições:** 133, uma por título de campeão paraguaio da 1ª divisão, de 1906 a 2025, como na lista de campeões da RSSSF (`parachamp.html`) e na Wikipédia em inglês. Até 2007 um campeão por ano (sem campeonato em 1908, 1922 e 1932-1934); de 1996 a 2007 o Apertura e o Clausura são fases da edição anual, com a final entre os vencedores. De 2008 em diante, Apertura e Clausura dão título cada um: uma edição por torneio.

**Edições sem jogos (76):** 1906-1959, 1968-1980 e 1982-1995. Pesquisamos RSSSF, ogol, Wikipédias em espanhol, inglês e guarani, Transfermarkt, worldfootball, sites e livros paraguaios: nenhuma fonte pública traz os jogos completos desses anos (a RSSSF tem só alguns resultados soltos, "Known Results"). Decisão do Guilherme (21/11/2026): essas edições entram só com o campeão, o vice e a tabela da RSSSF quando há: completa em 1943, 1945, 1955 e 1990-1995; parcial (posição e pontos, às vezes parte da campanha) nos outros anos; sem tabela, a classificação tem só o campeão e o vice. Os jogos soltos ficam de fora.

**Fora do pacote:** a Copa Paraguay, a Copa República, a Intermedia (2ª divisão), as liguillas e os jogos de promoção.

**Fontes:** RSSSF (uma página por temporada de 1960 em diante e a história da liga 1906-1959, `parahist.html`, em `data/coleta/par-1/rsssf/`: base de jogos de 1960-1967, 1981 e 1996 em diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas são a conferência); ESPN (liga `par.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol só tem jogos de 2005 em diante e não entrou.

**Clubes:** homônimos de outros países levam a cidade: Nacional de Asunción (o Nacional é o uruguaio), River Plate de Asunción, Sportivo San Lorenzo, Independiente de Campo Grande, Universal de Encarnación; o Guaraní é "Guaraní de Asunción" para não se confundir com o Guarani de Campinas. General Caballero (Zeballos Cué) e General Caballero JLM, e Cerro Porteño e Cerro Porteño PF, são clubes diferentes.

**Regras:** o placar é o da RSSSF. Jogo decidido no tribunal leva o placar dado (`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1906 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1907 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | lista de campeões e vices da RSSSF (parachamp.html) |
| 1909 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist) |
| 1910 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | lista de campeões e vices da RSSSF (parachamp.html) |
| 1911 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1912 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1913 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1914 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1915 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1916 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1917 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (parahist, tabela parcial) |
| 1918 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1919 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1920 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (parahist, tabela parcial) |
| 1921 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1923 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1924 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1925 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1926 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist, tabela parcial) |
| 1927 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1928 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1929 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1930 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (parahist, tabela parcial) |
| 1931 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1935 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1936 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1937 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1938 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1939 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1940 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1941 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1942 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist) |
| 1943 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para43) |
| 1944 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1945 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para45) |
| 1946 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Nacional de Asunción | RSSSF (parahist) |
| 1947 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1948 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1949 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | RSSSF (parahist, tabela parcial) |
| 1950 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1951 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Sportivo Luqueño | RSSSF (parahist, tabela parcial) |
| 1952 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Presidente Hayes | RSSSF (parahist, tabela parcial) |
| 1953 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Sportivo Luqueño | RSSSF (parahist, tabela parcial) |
| 1954 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (parahist, tabela parcial) |
| 1955 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Libertad | RSSSF (para55) |
| 1956 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1957 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1958 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1959 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (parahist, tabela parcial) |
| 1960 | 10 | 136 (136) | 443 | 0 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961 | 11 | 118 (116) | 384 | 0 | 1 / 1 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1962 | 11 | 138 (136) | 544 | 0 | 1 / 2 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1963 | 11 | 132 (238) | 449 | 0 | 1 / 2 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964 | 10 | 116 (116) | 301 | 0 | 0 / 0 | Guaraní de Asunción | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1965 | 9 | 134 (40) | 389 | 0 | 0 / 3 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 10 | 94 (94) | 271 | 0 | 2 / 1 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
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
| 1981 | 10 | 141 (134) | 280 | 0 | 2 / 2 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (para82, tabela parcial) |
| 1983 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1984 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Guaraní de Asunción | lista de campeões e vices da RSSSF (parachamp.html) |
| 1985 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | lista de campeões e vices da RSSSF (parachamp.html) |
| 1986 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Sol de América | RSSSF (para86) |
| 1987 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (para87) |
| 1988 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (para88) |
| 1989 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (para89) |
| 1990 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (para90) |
| 1991 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Sol de América | RSSSF (para91, tabela parcial) |
| 1992 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (para92) |
| 1993 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (para93) |
| 1994 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Cerro Porteño | RSSSF (para94) |
| 1995 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Olimpia | RSSSF (para95) |
| 1996 | 13 | 182 (182) | 519 | 0 | 0 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 | 13 | 190 (190) | 528 | 7 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 | 12 | 170 (170) | 472 | 0 | 5 / 10 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 | 11 | 145 (145) | 398 | 7 | 4 / 11 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 | 10 | 172 (172) | 485 | 123 | 6 / 2 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001 | 10 | 104 (104) | 295 | 183 | 3 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 | 10 | 151 (151) | 418 | 288 | 4 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 | 10 | 153 (153) | 398 | 239 | 4 / 3 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 | 10 | 186 (186) | 489 | 284 | 4 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 | 12 | 184 (184) | 478 | 318 | 3 / 5 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 | 11 | 210 (210) | 603 | 573 | 6 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 | 12 | 255 (255) | 645 | 273 | 5 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Apertura | 12 | 126 (126) | 376 | 350 | 4 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Clausura | 12 | 127 (127) | 325 | 257 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 12 | 129 (129) | 311 | 311 | 0 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Clausura | 12 | 126 (126) | 299 | 222 | 3 / 0 | Nacional de Asunción | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Apertura | 12 | 132 (132) | 342 | 325 | 2 / 0 | Guaraní de Asunción | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Clausura | 12 | 132 (132) | 325 | 318 | 2 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Apertura | 12 | 132 (132) | 319 | 319 | 2 / 0 | Nacional de Asunción | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Clausura | 12 | 132 (132) | 369 | 369 | 2 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2012 Apertura | 12 | 132 (132) | 355 | 355 | 1 / 0 | Cerro Porteño | RSSSF (para2012) |
| 2012 Clausura | 12 | 132 (132) | 339 | 339 | 1 / 0 | Libertad | RSSSF (para2012) |
| 2013 Apertura | 12 | 132 (132) | 351 | 351 | 1 / 0 | Nacional de Asunción | RSSSF (para2013) |
| 2013 Clausura | 12 | 132 (132) | 362 | 362 | 1 / 0 | Cerro Porteño | RSSSF (para2013) |
| 2014 Apertura | 12 | 130 (130) | 378 | 217 | 1 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2014 Clausura | 12 | 130 (130) | 337 | 201 | 2 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2015 Apertura | 12 | 132 (132) | 372 | 206 | 1 / 0 | Cerro Porteño | RSSSF (para2015) |
| 2015 Clausura | 12 | 133 (133) | 386 | 230 | 1 / 0 | Olimpia | RSSSF (para2015) |
| 2016 Apertura | 12 | 132 (132) | 433 | 206 | 1 / 0 | Libertad | RSSSF (para2016) |
| 2016 Clausura | 12 | 132 (132) | 354 | 226 | 1 / 0 | Guaraní de Asunción | RSSSF (para2016) |
| 2017 Apertura | 12 | 133 (133) | 340 | 329 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2017 Clausura | 12 | 132 (132) | 329 | 222 | 1 / 0 | Cerro Porteño | RSSSF (para2017) |
| 2018 Apertura | 12 | 132 (132) | 381 | 378 | 1 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2018 Clausura | 12 | 132 (132) | 355 | 224 | 2 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2019 Apertura | 12 | 132 (132) | 381 | 378 | 1 / 0 | Olimpia | RSSSF (para2019) |
| 2019 Clausura | 12 | 132 (132) | 339 | 213 | 1 / 0 | Olimpia | RSSSF (para2019) |
| 2020 Apertura | 12 | 132 (132) | 347 | 344 | 2 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2020 Clausura | 12 | 73 (73) | 198 | 111 | 1 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2021 Apertura | 10 | 90 (90) | 234 | 234 | 2 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2021 Clausura | 10 | 90 (90) | 222 | 143 | 2 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 Apertura | 12 | 132 (132) | 336 | 336 | 1 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 Clausura | 12 | 133 (133) | 323 | 323 | 0 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2023 Apertura | 12 | 132 (132) | 317 | 317 | 1 / 0 | Libertad | RSSSF (para2023) |
| 2023 Clausura | 12 | 133 (133) | 348 | 348 | 0 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2024 Apertura | 12 | 132 (132) | 339 | 336 | 2 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2024 Clausura | 12 | 132 (132) | 277 | 238 | 2 / 0 | Olimpia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Apertura | 12 | 132 (132) | 288 | 220 | 2 / 0 | Libertad | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Clausura | 12 | 132 (132) | 341 | 192 | 2 / 0 | Cerro Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |

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

- abandonado/suspenso, sem valer — Libertad Olimpia (1960-10-30): abandoned at 0-2 in 43'

### 1961

- tabela publicada x jogos — para61:18: Presidente Hayes tabela [20, 2, 7, 11, 25, 47] jogos [22, 3, 8, 11, 31, 49] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — para61:18: Atlético Tembetary tabela [20, 4, 3, 13, 25, 50] jogos [22, 4, 4, 14, 27, 56] — sobram 2 jogo(s) do clube na página

### 1962

- tabela publicada x jogos — para62:79: Guaraní de Asunción tabela [4, 1, 3, 0, 7, 6] jogos [5, 1, 3, 1, 8, 9] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — para62:79: Atlético Tembetary tabela [4, 2, 1, 1, 6, 6] jogos [5, 3, 1, 1, 9, 7] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — para62:103: River Plate de Asunción tabela [20, 12, 4, 4, 45, 31] jogos [22, 13, 5, 4, 53, 38] — a outra tabela publicada (para62) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para62:103: Atlético Tembetary tabela [20, 4, 8, 8, 30, 43] jogos [22, 4, 9, 9, 37, 51] — sobram 2 jogo(s) do clube na página

### 1963

- tabela publicada x jogos — para63:44: Cerro Porteño tabela [5, 3, 1, 1, 16, 10] jogos [15, 10, 3, 2, 40, 22] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:44: Olimpia tabela [5, 3, 1, 1, 11, 8] jogos [15, 6, 4, 5, 22, 16] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:44: Sportivo San Lorenzo tabela [5, 3, 1, 1, 14, 11] jogos [15, 4, 4, 7, 23, 36] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:44: Nacional de Asunción tabela [5, 1, 1, 3, 13, 14] jogos [15, 2, 5, 8, 22, 32] — sobram 10 jogo(s) do clube na página
- tabela publicada x jogos — para63:44: Guaraní de Asunción tabela [5, 1, 1, 3, 9, 14] jogos [15, 6, 4, 5, 26, 26] — sobram 10 jogo(s) do clube na página
- tabela publicada x jogos — para63:44: River Plate de Asunción tabela [5, 1, 1, 3, 7, 13] jogos [15, 4, 6, 5, 22, 23] — sobram 10 jogo(s) do clube na página
- tabela publicada x jogos — para63:88: Cerro Porteño tabela [20, 15, 2, 3, 47, 20] jogos [25, 18, 3, 4, 63, 30] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:88: Olimpia tabela [20, 10, 6, 4, 35, 18] jogos [25, 13, 7, 5, 46, 26] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:88: River Plate de Asunción tabela [20, 7, 8, 5, 32, 25] jogos [25, 8, 9, 8, 39, 38] — sobram 5 jogo(s) do clube na página
- tabela publicada x jogos — para63:88: Guaraní de Asunción tabela [20, 6, 9, 5, 29, 23] jogos [25, 7, 10, 8, 38, 37] — sobram 5 jogo(s) do clube na página
- tabela publicada x jogos — para63:88: Nacional de Asunción tabela [20, 6, 6, 8, 29, 34] jogos [25, 7, 7, 11, 42, 48] — sobram 5 jogo(s) do clube na página
- tabela publicada x jogos — para63:88: Sportivo San Lorenzo tabela [20, 5, 6, 9, 22, 36] jogos [25, 8, 7, 10, 36, 47] — a outra tabela publicada (para63) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para63:88: Sportivo Luqueño tabela [20, 5, 4, 11, 32, 42] jogos [22, 5, 6, 11, 38, 48] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — para63:88: Atlético Tembetary tabela [20, 4, 6, 10, 24, 38] jogos [22, 4, 8, 10, 30, 44] — sobram 2 jogo(s) do clube na página
- abandonado/suspenso, sem valer — River Plate de Asunción Sol de América (1963-07-14): abandoned at 0-0 in 56'

### 1964

- abandonado/suspenso, sem valer — Presidente Hayes Nacional de Asunción (1964-03-13): abandoned at 1-0 in 48' due to rain

### 1965

- tabela publicada x jogos — para65:94: Cerro Porteño tabela [5, 3, 1, 1, 14, 5] jogos [20, 11, 5, 4, 44, 18] — sobram 15 jogo(s) do clube na página
- tabela publicada x jogos — para65:94: Sportivo San Lorenzo tabela [5, 2, 2, 1, 4, 2] jogos [20, 8, 5, 7, 25, 30] — sobram 15 jogo(s) do clube na página
- tabela publicada x jogos — para65:94: Guaraní de Asunción tabela [5, 3, 0, 2, 8, 7] jogos [20, 10, 2, 8, 26, 27] — sobram 15 jogo(s) do clube na página
- tabela publicada x jogos — para65:94: Olimpia tabela [5, 2, 0, 3, 7, 7] jogos [20, 10, 6, 4, 41, 26] — sobram 15 jogo(s) do clube na página
- tabela publicada x jogos — para65:94: Nacional de Asunción tabela [5, 1, 2, 2, 3, 7] jogos [20, 3, 6, 11, 16, 31] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:94: Rubio Ñu tabela [5, 1, 1, 3, 7, 15] jogos [20, 4, 4, 12, 27, 47] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:124: Cerro Porteño tabela [8, 6, 1, 1, 25, 8] jogos [29, 14, 8, 7, 57, 29] — sobram 21 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Olimpia tabela [8, 6, 1, 1, 18, 7] jogos [32, 19, 8, 5, 69, 32] — sobram 24 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Guaraní de Asunción tabela [8, 5, 0, 3, 13, 10] jogos [29, 18, 3, 8, 47, 29] — sobram 21 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Sportivo San Lorenzo tabela [8, 3, 2, 3, 11, 14] jogos [29, 9, 8, 12, 34, 49] — sobram 21 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Rubio Ñu tabela [8, 4, 0, 4, 10, 17] jogos [29, 8, 7, 14, 40, 55] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:124: Presidente Hayes tabela [8, 3, 1, 4, 8, 8] jogos [27, 6, 10, 11, 27, 47] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: River Plate de Asunción tabela [8, 2, 2, 4, 10, 14] jogos [27, 9, 7, 11, 36, 46] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Libertad tabela [8, 2, 0, 6, 6, 17] jogos [27, 5, 10, 12, 33, 48] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — para65:124: Nacional de Asunción tabela [8, 1, 1, 6, 8, 14] jogos [29, 6, 9, 14, 32, 40] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:228: Guaraní de Asunción tabela [16, 10, 3, 3, 26, 12] jogos [3, 1, 0, 2, 4, 7] — faltam 13 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: Olimpia tabela [16, 8, 7, 1, 28, 16] jogos [4, 3, 0, 1, 9, 5] — faltam 12 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: Cerro Porteño tabela [16, 5, 6, 5, 18, 16] jogos [1, 0, 0, 1, 1, 2] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: River Plate de Asunción tabela [16, 6, 4, 6, 18, 27] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: Rubio Ñu tabela [16, 4, 6, 6, 23, 23] jogos [0, 0, 0, 0, 0, 0] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:228: Libertad tabela [16, 3, 8, 5, 23, 24] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: Presidente Hayes tabela [16, 3, 8, 5, 17, 23] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — para65:228: Nacional de Asunción tabela [16, 3, 6, 7, 21, 19] jogos [0, 0, 0, 0, 0, 0] — a diferença vem de Rubio Ñu x Nacional de Asunción (1965-11-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — para65:228: Sportivo San Lorenzo tabela [16, 4, 4, 8, 19, 33] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- abandonado/suspenso, sem valer — Rubio Ñu Nacional de Asunción (1965-11-26): abandoned at 1-2 in 73']     [at Cerro Porteño

### 1966

- tabela publicada x jogos — para66:114: Cerro Porteño tabela [16, 10, 4, 2, 33, 16] jogos [18, 11, 5, 2, 36, 18] — a outra tabela publicada (para66) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para66:114: Olimpia tabela [16, 9, 4, 3, 20, 13] jogos [18, 9, 5, 4, 22, 16] — a outra tabela publicada (para66) fecha com os jogos: o erro é desta tabela

### 1967

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

- tabela publicada x jogos — para81:274: Libertad tabela [18, 8, 8, 2, 25, 14] jogos [20, 9, 8, 3, 28, 16] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para81:274: Sol de América tabela [18, 11, 2, 5, 24, 14] jogos [22, 14, 2, 6, 29, 17] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para81:274: Olimpia tabela [18, 8, 8, 2, 22, 13] jogos [22, 9, 8, 5, 24, 18] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para81:302: Sol de América tabela [2, 2, 0, 0, 3, 1] jogos [8, 6, 0, 2, 12, 7] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para81:302: Libertad tabela [2, 1, 0, 1, 3, 2] jogos [6, 1, 2, 3, 3, 6] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para81:302: Olimpia tabela [2, 0, 0, 2, 0, 3] jogos [8, 2, 2, 4, 6, 8] — a outra tabela publicada (para81) fecha com os jogos: o erro é desta tabela
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

- tabela publicada x jogos — para98:139: Olimpia tabela [2, 1, 0, 1, 5, 2] jogos [4, 3, 0, 1, 9, 3] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Guaraní de Asunción tabela [2, 1, 1, 0, 5, 4] jogos [4, 1, 1, 2, 6, 8] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Sportivo Luqueño tabela [2, 0, 1, 1, 2, 6] jogos [3, 0, 1, 2, 3, 8] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:139: Sol de América tabela [2, 1, 0, 1, 4, 4] jogos [3, 2, 0, 1, 6, 5] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:146: Cerro Porteño tabela [2, 2, 0, 0, 6, 2] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:148: Presidente Hayes tabela [2, 0, 0, 2, 2, 6] jogos [1, 0, 0, 1, 0, 1] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:148: Cerro Corá tabela [2, 0, 1, 1, 2, 4] jogos [1, 1, 0, 0, 1, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:173: Olimpia tabela [3, 2, 0, 1, 7, 2] jogos [4, 3, 0, 1, 9, 3] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:173: Guaraní de Asunción tabela [3, 1, 1, 1, 5, 6] jogos [4, 1, 1, 2, 6, 8] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:180: Cerro Porteño tabela [3, 3, 0, 0, 10, 2] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:182: Cerro Corá tabela [3, 1, 1, 1, 3, 4] jogos [6, 2, 3, 1, 9, 9] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:216: Nacional de Asunción tabela [11, 3, 6, 2, 17, 22] jogos [11, 2, 7, 2, 17, 23] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:342: Olimpia tabela [3, 2, 1, 0, 7, 4] jogos [3, 2, 1, 0, 6, 3] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:342: Cerro Corá tabela [3, 1, 2, 0, 6, 5] jogos [2, 0, 2, 0, 4, 4] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:342: Guaraní de Asunción tabela [3, 1, 1, 1, 4, 4] jogos [3, 0, 1, 2, 3, 6] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Cerro Porteño tabela [22, 16, 3, 3, 52, 19] jogos [2, 0, 1, 1, 3, 5] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Guaraní de Asunción tabela [22, 10, 6, 6, 31, 28] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Olimpia tabela [22, 9, 5, 8, 28, 19] jogos [2, 1, 1, 0, 5, 3] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Sportivo Luqueño tabela [22, 8, 8, 6, 25, 29] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:419: Cerro Corá tabela [22, 8, 6, 8, 33, 34] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:425: Atlético Colegiales tabela [22, 8, 4, 10, 24, 29] jogos [25, 9, 5, 11, 28, 32] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:425: Sol de América tabela [22, 5, 11, 6, 24, 25] jogos [28, 7, 12, 9, 34, 38] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:425: Presidente Hayes tabela [22, 5, 9, 8, 23, 28] jogos [25, 5, 9, 11, 25, 35] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para98:425: Sportivo San Lorenzo tabela [22, 5, 8, 9, 25, 33] jogos [25, 6, 8, 11, 31, 40] — a outra tabela publicada (para98) fecha com os jogos: o erro é desta tabela
- linha lida como jogo e descartada (clube não reconhecido): para98:432 «Promoted: Resistencia (won final versus Sportivo Iteño x on penalties)»

### 1999

- tabela publicada x jogos — para99:158: Olimpia tabela [3, 2, 1, 0, 9, 5] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:160: Sportivo San Lorenzo tabela [3, 0, 1, 2, 3, 6] jogos [6, 1, 1, 4, 7, 13] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:165: Atlético Colegiales tabela [3, 3, 0, 0, 9, 1] jogos [4, 4, 0, 0, 11, 2] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:165: Cerro Porteño tabela [3, 2, 0, 1, 4, 5] jogos [4, 3, 0, 1, 5, 5] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:165: Guaraní de Asunción tabela [3, 1, 0, 2, 3, 5] jogos [4, 1, 0, 3, 3, 6] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:165: Sportivo Luqueño tabela [3, 0, 0, 3, 0, 5] jogos [4, 0, 0, 4, 1, 7] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:189: Cerro Porteño tabela [10, 7, 1, 2, 25, 8] jogos [12, 9, 1, 2, 30, 9] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:194: Atlético Colegiales tabela [10, 2, 3, 5, 9, 12] jogos [11, 3, 3, 5, 11, 13] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:194: Cerro Corá tabela [10, 2, 3, 5, 10, 16] jogos [13, 2, 3, 8, 12, 23] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Cerro Porteño tabela [2, 1, 1, 0, 5, 2] jogos [4, 3, 1, 0, 8, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Sportivo San Lorenzo tabela [2, 1, 0, 1, 3, 5] jogos [3, 1, 0, 2, 4, 7] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Cerro Corá tabela [2, 1, 1, 0, 4, 2] jogos [3, 2, 1, 0, 6, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:321: Guaraní de Asunción tabela [2, 0, 0, 2, 2, 5] jogos [4, 0, 0, 4, 3, 8] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: Sportivo Luqueño tabela [2, 1, 1, 0, 4, 2] jogos [1, 1, 0, 0, 3, 1] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:328: Olimpia tabela [2, 1, 0, 1, 4, 3] jogos [1, 0, 0, 1, 1, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:331: Atlético Colegiales tabela [2, 0, 0, 2, 0, 4] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:359: Cerro Porteño tabela [3, 2, 1, 0, 6, 2] jogos [4, 3, 1, 0, 8, 3] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:359: Guaraní de Asunción tabela [3, 0, 0, 3, 2, 6] jogos [4, 0, 0, 4, 3, 8] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Olimpia tabela [20, 12, 7, 1, 39, 17] jogos [2, 2, 0, 0, 4, 2] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Cerro Porteño tabela [20, 12, 5, 3, 46, 20] jogos [2, 0, 0, 2, 2, 4] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Sportivo Luqueño tabela [20, 11, 6, 3, 44, 27] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Sportivo San Lorenzo tabela [20, 6, 11, 3, 26, 22] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:408: Guaraní de Asunción tabela [20, 6, 10, 4, 29, 27] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:414: Atlético Colegiales tabela [20, 6, 4, 10, 25, 31] jogos [27, 11, 4, 12, 38, 38] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:414: Sol de América tabela [20, 5, 6, 9, 18, 22] jogos [23, 6, 6, 11, 22, 29] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para99:414: Cerro Corá tabela [20, 4, 6, 10, 27, 39] jogos [26, 6, 7, 13, 35, 49] — a outra tabela publicada (para99) fecha com os jogos: o erro é desta tabela

### 2000

- tabela publicada x jogos — para00:282: Cerro Porteño tabela [9, 3, 5, 1, 16, 10] jogos [9, 3, 5, 1, 15, 9] — a outra tabela publicada (para00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para00:526: Cerro Porteño tabela [3, 2, 0, 1, 8, 6] jogos [4, 3, 0, 1, 12, 8] — a outra tabela publicada (para00) fecha com os jogos: o erro é desta tabela

### 2001

- sem ocorrências

### 2002

- sem ocorrências

### 2003

- tabela publicada x jogos — para03:193: Sol de América tabela [2, 1, 0, 1, 4, 3] jogos [3, 1, 0, 2, 6, 6] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para03:193: Cerro Porteño tabela [2, 0, 0, 2, 3, 6] jogos [3, 1, 0, 2, 6, 8] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para03:245: Libertad tabela [18, 9, 6, 3, 32, 20] jogos [19, 9, 7, 3, 32, 20] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para03:245: Olimpia tabela [18, 9, 6, 3, 30, 18] jogos [19, 9, 7, 3, 30, 18] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para03:571: Cerro Porteño tabela [3, 1, 0, 2, 4, 7] jogos [4, 1, 0, 3, 6, 11] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para03:571: Sol de América tabela [3, 0, 1, 2, 5, 9] jogos [4, 1, 1, 2, 9, 11] — a outra tabela publicada (para03) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Sportivo San Lorenzo Cerro Porteño (2003-03-01): abandoned at 0-3 in 70' due to light

### 2004

- sem ocorrências

### 2005

- tabela publicada x jogos — para05:334: Libertad tabela [18, 9, 5, 4, 30, 23] jogos [19, 9, 5, 5, 34, 24] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para05:338: Guaraní de Asunción tabela [18, 6, 2, 10, 18, 25] jogos [20, 7, 2, 11, 21, 30] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para05:343: General Caballero tabela [18, 3, 1, 14, 15, 29] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para05:649: Libertad tabela [36, 13, 12, 11, 51, 46] jogos [37, 13, 12, 12, 55, 47] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para05:649: Guaraní de Asunción tabela [36, 15, 6, 15, 39, 43] jogos [38, 16, 6, 16, 42, 48] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — para05:655: General Caballero tabela [36, 5, 8, 23, 31, 57] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (para05) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — General Caballero Olimpia (2006-05-21): abandoned at 1-0 in 32'
- decidido fora de campo — General Caballero Libertad (2006-11-26): awarded to Libertad; originally

### 2006

- ESPN: 186 jogos casados

### 2007

- ESPN: 1 jogos casados
- abandonado/suspenso, sem valer — 2 de Mayo Sol de América (2008-05-18): abandoned at 1-1 in 68'

### 2008 Apertura

- ESPN: 121 jogos casados

### 2008 Clausura

- ESPN: 86 jogos casados
- abandonado/suspenso, sem valer — Guaraní de Asunción Libertad (2008-10-25): abandoned at 1-1 at half-time

### 2009 Apertura

- ESPN: 123 jogos casados
- abandonado/suspenso, sem valer — Tacuary Cerro Porteño (2009-04-04): abandoned at 0-1 at
- abandonado/suspenso, sem valer — 2 de Mayo 3 de Febrero (2009-05-29): abandoned at 0-1 in 32'

### 2009 Clausura

- ESPN: 70 jogos casados

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

- ESPN: 127 jogos casados

### 2014 Clausura

- ESPN: 80 jogos casados

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

