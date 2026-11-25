# Campeonato Gaúcho (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-rs-1/importar.py`. Pacote em `data/coleta/bra-rs-1/pacote/`. Mesmo código do Mineiro
(`docs/coleta/bra-mg-1.md`), com as fontes do Rio Grande do Sul.

**Temporadas:** 1919 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). 1918, 1923 e 1924 não foram disputados.
Até 1960 o campeonato era por regiões: os campeões das cidades disputavam os regionais e os campeões regionais, a fase
estadual. Entram a fase estadual e as decisões de zona e região que a página da RSSSF traz ("Fase regional"), não os
campeonatos das cidades. A Divisão Especial, com clubes de todo o estado, começou em 1961. 1930 foi organizado pela
FAGET, no lugar da FRGD.

**Fontes:** RSSSF Brasil (`tablesr/rs{ano}.htm`, 1919-2024: jogos, fases, datas, autores e tabelas); ogol (calendário
de cada edição e o código de cada clube; não tem jogos de 1925 a 1976, salvo 1965; 2025 e 2026 só nele); Wikipédia em
português (artigo do Campeonato Gaúcho: campeão e vice de cada ano, segunda fonte). Artilheiros pela lista da RSSSF
(`rstops.htm`), menos 1940-1960, em que ela traz os do campeonato de Porto Alegre.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1919 | RSSSF + ogol | 2 | 1 (1) | 6 | 0 | 0 / 0 | Brasil de Pelotas | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF + ogol | 3 | 3 (3) | 5 | 0 | 0 / 0 | Guarany de Bagé | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF + ogol | 5 | 7 (6) | 18 | 8 | 1 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF + ogol | 4 | 8 (8) | 25 | 3 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 | RSSSF | 11 | 9 (0) | 32 | 0 | 0 / 0 | Bagé | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 | RSSSF | 19 | 18 (0) | 107 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 | RSSSF | 20 | 15 (0) | 66 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 | RSSSF | 14 | 15 (0) | 69 | 3 | 0 / 0 | Americano-RS | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1929 | RSSSF | 5 | 4 (0) | 11 | 0 | 0 / 0 | Cruzeiro-RS | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF | 6 | 4 (0) | 20 | 0 | 0 / 0 | Pelotas | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF | 11 | 12 (0) | 51 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 | RSSSF | 6 | 5 (0) | 31 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 | RSSSF | 11 | 9 (0) | 54 | 0 | 0 / 0 | SÃO PAULO-RS | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 | RSSSF | 14 | 12 (0) | 38 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 | RSSSF | 20 | 19 (0) | 111 | 0 | 0 / 0 | Farroupilha | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 | RSSSF | 9 | 8 (0) | 50 | 0 | 0 / 0 | Rio Grande | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF | 11 | 14 (0) | 63 | 0 | 0 / 0 | Grêmio Santanense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF | 11 | 13 (0) | 51 | 0 | 0 / 0 | Guarany de Bagé | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF | 10 | 16 (0) | 61 | 8 | 0 / 0 | FC Riograndense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF | 12 | 10 (0) | 49 | 3 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF | 8 | 10 (0) | 63 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF | 7 | 7 (0) | 49 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF | 5 | 6 (0) | 39 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 | RSSSF | 5 | 6 (0) | 31 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF | 4 | 6 (0) | 32 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF | 5 | 5 (0) | 24 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF | 8 | 11 (0) | 51 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 8 | 8 (0) | 40 | 40 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 5 | 8 (0) | 34 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF | 8 | 18 (0) | 70 | 0 | 0 / 1 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 3 | 6 (0) | 22 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 4 | 12 (0) | 41 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF | 4 | 9 (0) | 41 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 3 | 6 (0) | 15 | 0 | 0 / 0 | Renner | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 5 | 12 (0) | 37 | 3 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 5 | 8 (0) | 30 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 5 | 10 (0) | 39 | 11 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF | 5 | 11 (0) | 28 | 6 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF | 4 | 12 (0) | 39 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 6 | 15 (0) | 65 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF | 12 | 132 (0) | 461 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF | 13 | 119 (0) | 320 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF | 12 | 130 (0) | 331 | 0 | 0 / 1 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF | 12 | 129 (0) | 341 | 0 | 1 / 2 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF + ogol | 12 | 132 (132) | 346 | 0 | 1 / 0 | Grêmio | RSSSF (classificação geral publicada) |
| 1966 | RSSSF | 12 | 131 (0) | 307 | 0 | 0 / 1 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF | 12 | 132 (0) | 309 | 0 | 0 / 1 | Grêmio | RSSSF (classificação geral publicada) |
| 1968 | RSSSF | 19 | 175 (0) | 449 | 0 | 0 / 3 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF | 18 | 199 (0) | 489 | 0 | 1 / 3 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF | 17 | 190 (0) | 394 | 0 | 0 / 5 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF | 26 | 352 (0) | 818 | 0 | 1 / 3 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 25 | 200 (0) | 382 | 0 | 3 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 22 | 322 (0) | 609 | 0 | 1 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF | 16 | 177 (0) | 355 | 0 | 0 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 33 | 327 (0) | 672 | 4 | 8 / 3 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF | 32 | 324 (0) | 699 | 0 | 6 / 3 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF + ogol | 24 | 311 (311) | 611 | 25 | 5 / 3 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF + ogol | 20 | 248 (243) | 501 | 4 | 4 / 5 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF + ogol | 21 | 474 (437) | 950 | 0 | 7 / 3 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF + ogol | 16 | 270 (270) | 513 | 0 | 1 / 2 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF + ogol | 12 | 187 (187) | 371 | 0 | 5 / 5 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF + ogol | 12 | 163 (162) | 328 | 7 | 0 / 3 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF + ogol | 12 | 193 (193) | 322 | 0 | 0 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF + ogol | 14 | 344 (344) | 601 | 0 | 2 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF + ogol | 14 | 182 (182) | 364 | 0 | 2 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF + ogol | 43 | 487 (194) | 983 | 0 | 11 / 6 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF + ogol | 52 | 696 (237) | 1381 | 0 | 17 / 16 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 14 | 184 (127) | 349 | 5 | 3 / 5 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF + ogol | 14 | 190 (133) | 394 | 0 | 0 / 18 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 14 | 198 (195) | 406 | 0 | 0 / 8 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF + ogol | 20 | 218 (217) | 453 | 0 | 4 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF + ogol | 22 | 257 (257) | 541 | 0 | 2 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF + ogol | 24 | 336 (335) | 718 | 0 | 7 / 6 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 24 | 507 (506) | 1062 | 0 | 0 / 1 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF + ogol | 24 | 321 (30) | 771 | 0 | 1 / 6 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 27 | 217 (117) | 542 | 0 | 4 / 10 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 28 | 275 (245) | 820 | 0 | 6 / 4 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 27 | 189 (189) | 487 | 0 | 6 / 1 | Juventude | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 30 | 226 (225) | 582 | 0 | 11 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 17 | 142 (142) | 410 | 0 | 4 / 3 | Caxias | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 17 | 136 (136) | 389 | 0 | 0 / 4 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 17 | 174 (170) | 507 | 0 | 8 / 2 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 18 | 200 (200) | 568 | 0 | 3 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 18 | 222 (222) | 624 | 624 | 4 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 18 | 116 (116) | 318 | 318 | 5 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 18 | 116 (116) | 337 | 0 | 6 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 18 | 152 (152) | 428 | 0 | 5 / 2 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 16 | 126 (126) | 376 | 0 | 6 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 16 | 134 (134) | 407 | 404 | 4 / 3 | Internacional | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 16 | 136 (136) | 450 | 0 | 8 / 2 | Grêmio | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 16 | 135 (136) | 408 | 389 | 4 / 1 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 16 | 136 (136) | 364 | 153 | 6 / 1 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 16 | 134 (134) | 285 | 112 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 16 | 128 (128) | 311 | 308 | 2 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 16 | 130 (130) | 268 | 0 | 3 / 0 | Internacional | RSSSF (classificação geral publicada) |
| 2016 | RSSSF + ogol | 14 | 101 (101) | 255 | 251 | 3 / 0 | Internacional | RSSSF (classificação geral publicada) |
| 2017 | RSSSF + ogol | 12 | 80 (80) | 168 | 168 | 8 / 0 | Novo Hamburgo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 12 | 80 (80) | 174 | 169 | 8 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 12 | 80 (80) | 179 | 174 | 8 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 12 | 74 (74) | 162 | 157 | 5 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 12 | 73 (72) | 182 | 173 | 2 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 12 | 72 (72) | 149 | 0 | 2 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 12 | 72 (72) | 158 | 158 | 3 / 0 | Grêmio | RSSSF (classificação geral publicada) |
| 2024 | RSSSF + ogol | 12 | 76 (76) | 165 | 155 | 2 / 1 | Grêmio | RSSSF (classificação geral publicada) |
| 2025 | ogol | 12 | 72 (72) | 165 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 12 | 64 (64) | 146 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1919

- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1920

- mando invertido no ogol — RSSSF Guarany de Bagé 1-0 Uruguaiana, ogol Uruguaiana 0-1 Guarany de Bagé (1920-11-21); fica a RSSSF
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1921

- mando invertido no ogol — RSSSF Uruguaiana 0-1 Brasil de Pelotas, ogol Brasil de Pelotas 1-0 Uruguaiana (1921-11-15); fica a RSSSF
- adversário diferente no ogol — RSSSF Grêmio 1-0 FC Riograndense, ogol Grêmio 1-0 Riograndense (1921-11-13); fica a RSSSF
- adversário diferente no ogol — RSSSF FC Riograndense 2-1 Brasil de Pelotas, ogol Riograndense 2-1 Brasil de Pelotas (1921-11-22); fica a RSSSF
- jogo só no ogol, incluído em Quadrangular em turno único. Todas: Uruguaiana 1-4 Riograndense (1921-11-19)
- só na RSSSF (não achado no ogol): FC Riograndense 4-1 Uruguaiana (1921-11-19)

### 1922

- placar diferente no ogol — Grêmio x Bagé (1922-11-19): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Guarani de Alegrete

### 1925

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BAGÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bataclan
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gen. Osório - Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Taquarense
- BAGÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Bataclan — clube que o ogol não tem; entra só pela RSSSF
- Gen. Osório - Rio Grande — clube que o ogol não tem; entra só pela RSSSF
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Taquarense — clube que o ogol não tem; entra só pela RSSSF

### 1926

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Club Athlético Gabrielense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dom Pedrito
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tabajara - Erechim
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Club Athlético Gabrielense — clube que o ogol não tem; entra só pela RSSSF
- Dom Pedrito — clube que o ogol não tem; entra só pela RSSSF
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Independente — clube que o ogol não tem; entra só pela RSSSF
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- Tabajara - Erechim — clube que o ogol não tem; entra só pela RSSSF

### 1927

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 15 de Novembro - D. Pedrito
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Ijuhyense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Italo-Brasileiro -
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Livramento
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- 15 de Novembro - D. Pedrito — clube que o ogol não tem; entra só pela RSSSF
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio Ijuhyense — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Italo-Brasileiro - — clube que o ogol não tem; entra só pela RSSSF
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Livramento — clube que o ogol não tem; entra só pela RSSSF
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)

### 1928

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Americano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil - Júlio de Castilhos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Ijuhyense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Santoangelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- Americano — clube que o ogol não tem; entra só pela RSSSF
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil - Júlio de Castilhos — clube que o ogol não tem; entra só pela RSSSF
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio Ijuhyense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio Ijuhyense)
- Grêmio Santoangelense — clube que o ogol não tem; entra só pela RSSSF
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)

### 1929

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)

### 1930

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Pelotas

### 1931

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Taquarense
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- Taquarense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquarense)

### 1932

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)

### 1933

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Universal
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitoriense
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- Universal — clube que o ogol não tem; entra só pela RSSSF
- Vitoriense — clube que o ogol não tem; entra só pela RSSSF

### 1934

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro do Sul - Jaguarão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio E. 7º RI - SM
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Cruzeiro do Sul - Jaguarão — clube que o ogol não tem; entra só pela RSSSF
- Grêmio E. 7º RI - SM — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)

### 1935

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil das Minas S. Jerônimo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HAMBURGO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário de Uruguaiana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Osório(???) - D. Pedrito
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SC Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SC Sao Paulo
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Brasil das Minas S. Jerônimo — clube que o ogol não tem; entra só pela RSSSF
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- NOVO HAMBURGO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Operário de Uruguaiana — clube que o ogol não tem; entra só pela RSSSF
- Osório(???) - D. Pedrito — clube que o ogol não tem; entra só pela RSSSF
- SC Rio Branco — clube que o ogol não tem; entra só pela RSSSF
- SC Sao Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- vencedor da final pelos jogos (Grêmio Santanense) diferente do campeão oficial (Farroupilha); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1936

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro PF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- Botafogo — clube que o ogol não tem; entra só pela RSSSF
- Cruzeiro PF — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)

### 1937

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Americano-Universitário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro PF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- Americano-Universitário — clube que o ogol não tem; entra só pela RSSSF
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Cruzeiro PF — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro PF)
- Ferroviário — clube que o ogol não tem; entra só pela RSSSF
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)

### 1938

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Renner
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Renner — clube que o ogol não tem; entra só pela RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Guarany de Bagé

### 1939

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco - STV
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Rio Branco - STV — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Grêmio Santanense

### 1940

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bancário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Escola de Comércio de Carazinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente Alegrete
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- Bancário — clube que o ogol não tem; entra só pela RSSSF
- Escola de Comércio de Carazinho — clube que o ogol não tem; entra só pela RSSSF
- Independente Alegrete — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)

### 1941

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho Erechim
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- 14 de Julho Erechim — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)

### 1942

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Armour
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- Armour — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Armour (Particulares))
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)

### 1943

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)

### 1945

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- Esperança — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)

### 1946

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)

### 1947

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bancário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Bancário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bancário)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Fluminense — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)

### 1948

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- vice pela Wikipédia (sem final de dois clubes): Grêmio Santanense

### 1949

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)

### 1950

- tabela publicada x jogos — Fase única / -: Internacional tabela [3, 2, 1, 0, 6, 2] jogos [7, 4, 1, 2, 13, 9] — a tabela conta 3 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Novo Hamburgo tabela [3, 2, 0, 1, 5, 4] jogos [4, 3, 0, 1, 13, 5] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase única / -: Brasil de Pelotas tabela [3, 1, 0, 2, 3, 3] jogos [6, 3, 1, 2, 12, 7] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Uruguaiana tabela [3, 0, 1, 2, 1, 6] jogos [7, 3, 1, 3, 9, 12] — a tabela conta 3 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Fluminense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fluminense-RS)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- vice pela Wikipédia (sem final de dois clubes): Novo Hamburgo

### 1951

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- vice pela Wikipédia (sem final de dois clubes): Pelotas

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- vice pela Wikipédia (sem final de dois clubes): Novo Hamburgo

### 1953

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é Brasil de Pelotas (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Brasil de Pelotas

### 1954

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Renner
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Renner — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Renner)
- vice pela Wikipédia (sem final de dois clubes): Brasil de Pelotas

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)

### 1956

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Veronese
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Veronese — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é Pelotas (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Pelotas

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é Bagé (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Bagé

### 1958

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Veronese
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Veronese — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Veronese)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é Guarany de Bagé (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Guarany de Bagé

### 1959

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- vice pela Wikipédia (sem final de dois clubes): Farroupilha

### 1960

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho/L
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- 14 de Julho/L — clube que o ogol não tem; entra só pela RSSSF
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- vice pela Wikipédia (sem final de dois clubes): Pelotas

### 1961

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1962

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani de Alegrete)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)

### 1963

- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [22, 18, 3, 1, 42, 12] jogos [21, 17, 3, 1, 41, 12] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Aimoré tabela [22, 10, 4, 8, 27, 21] jogos [21, 9, 4, 8, 26, 21] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [22, 7, 7, 8, 21, 28] jogos [22, 8, 6, 8, 21, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Flamengo-RS tabela [22, 6, 7, 9, 29, 36] jogos [21, 6, 7, 8, 29, 35] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Guarany de Bagé tabela [22, 4, 6, 12, 18, 32] jogos [21, 4, 6, 11, 18, 31] — a tabela conta 22 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Internacional

### 1964

- tabela publicada x jogos — 2º Turno / -: Brasil de Pelotas tabela [22, 11, 4, 7, 34, 29] jogos [21, 10, 4, 7, 31, 28] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Aimoré tabela [22, 6, 6, 10, 30, 41] jogos [21, 6, 6, 9, 29, 39] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-RS tabela [22, 6, 4, 12, 22, 38] jogos [20, 5, 4, 11, 20, 36] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Flamengo-RS tabela [22, 5, 5, 12, 28, 35] jogos [21, 4, 5, 12, 27, 35] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Rio Grande tabela [22, 4, 6, 12, 21, 35] jogos [21, 4, 6, 11, 20, 32] — a tabela conta 22 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Internacional

### 1965

- placar diferente no ogol — Rio Grande x Guarany de Bagé (1965-10-24): RSSSF 3-0, ogol 0-0; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Juventude

### 1966

- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [22, 7, 7, 8, 35, 32] jogos [21, 6, 7, 8, 31, 32] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Flamengo-RS tabela [22, 5, 5, 12, 20, 31] jogos [21, 5, 5, 11, 20, 27] — a tabela conta 22 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Internacional

### 1967

- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [22, 5, 3, 14, 25, 35] jogos [22, 5, 3, 14, 25, 36] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GAÚCHO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GAÚCHO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- campeão pela lista oficial, Grêmio; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Internacional

### 1968

- tabela publicada x jogos — Fase preliminar / GRUPO A: Brasil de Pelotas tabela [14, 9, 2, 3, 28, 14] jogos [13, 8, 2, 3, 26, 14] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase preliminar / GRUPO A: Gaúcho tabela [14, 6, 3, 5, 16, 30] jogos [13, 6, 3, 4, 16, 28] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase preliminar / GRUPO A: Rio Grande tabela [14, 4, 5, 5, 27, 28] jogos [13, 3, 5, 5, 24, 26] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase preliminar / GRUPO A: São José-RS tabela [14, 4, 4, 6, 18, 19] jogos [14, 4, 4, 6, 18, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase preliminar / GRUPO A: Flamengo-RS tabela [8, 2, 1, 5, 11, 17] jogos [7, 2, 1, 4, 9, 14] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase preliminar / GRUPO B: Juventude tabela [14, 9, 2, 3, 27, 16] jogos [14, 8, 3, 3, 27, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [14, 9, 4, 1, 25, 6] jogos [28, 18, 7, 3, 66, 18] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Internacional tabela [14, 7, 4, 3, 18, 14] jogos [28, 15, 8, 5, 37, 22] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-RS tabela [14, 7, 1, 6, 19, 18] jogos [28, 12, 5, 11, 32, 32] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Brasil de Pelotas tabela [14, 4, 4, 6, 13, 15] jogos [27, 12, 6, 9, 39, 29] — a tabela conta 14 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Juventude tabela [14, 3, 6, 5, 7, 12] jogos [28, 11, 9, 8, 34, 28] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Santa Cruz-RS tabela [14, 3, 6, 5, 11, 22] jogos [28, 10, 7, 11, 37, 41] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Pelotas tabela [14, 3, 5, 6, 19, 18] jogos [28, 10, 8, 10, 35, 31] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Gaúcho tabela [14, 2, 6, 6, 12, 19] jogos [27, 8, 9, 10, 28, 47] — a tabela conta 14 jogos e as fontes trazem 27
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GAÚCHO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HAMBURGO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SÃO PAULO
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GAÚCHO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- NOVO HAMBURGO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- SÃO PAULO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- vice pela Wikipédia (sem final de dois clubes): Internacional

### 1969

- tabela publicada x jogos — Fase preliminar / GRUPO B: Flamengo-RS tabela [16, 9, 2, 5, 19, 17] jogos [16, 9, 2, 5, 22, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase preliminar / GRUPO B: Rio Grande tabela [16, 2, 3, 11, 16, 31] jogos [16, 2, 3, 11, 16, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Internacional tabela [14, 9, 4, 1, 19, 4] jogos [29, 21, 5, 3, 52, 12] — a tabela conta 14 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [14, 7, 7, 0, 14, 2] jogos [30, 17, 11, 2, 38, 9] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-RS tabela [14, 4, 5, 5, 12, 9] jogos [30, 12, 9, 9, 39, 27] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Gaúcho tabela [14, 2, 4, 8, 8, 23] jogos [30, 8, 10, 12, 38, 44] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Brasil de Pelotas tabela [14, 4, 4, 6, 16, 19] jogos [30, 12, 7, 11, 41, 39] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: 14 de Julho tabela [14, 2, 8, 4, 10, 18] jogos [30, 9, 11, 10, 33, 42] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Santa Cruz-RS tabela [14, 3, 4, 7, 17, 24] jogos [30, 10, 7, 13, 41, 49] — a tabela conta 14 jogos e as fontes trazem 30
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GAÚCHO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HAMBURGO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SÃO PAULO
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GAÚCHO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- NOVO HAMBURGO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- SÃO PAULO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1970

- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Grêmio tabela [16, 10, 2, 4, 28, 12] jogos [14, 9, 1, 4, 26, 11] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Flamengo-RS tabela [16, 7, 5, 4, 16, 14] jogos [14, 6, 5, 3, 14, 12] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Inter de Santa Maria tabela [16, 7, 4, 5, 18, 16] jogos [13, 5, 3, 5, 15, 15] — a tabela conta 16 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Esportivo-RS tabela [16, 5, 7, 4, 16, 14] jogos [14, 5, 7, 2, 15, 10] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Ypiranga-RS tabela [16, 3, 10, 3, 16, 21] jogos [14, 3, 8, 3, 15, 20] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Juventude tabela [16, 4, 5, 7, 15, 17] jogos [14, 4, 4, 6, 13, 14] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: Gaúcho tabela [16, 5, 2, 9, 15, 24] jogos [14, 4, 1, 9, 12, 22] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE CENTRO: São José-RS tabela [16, 2, 6, 8, 9, 17] jogos [13, 2, 5, 6, 7, 13] — a tabela conta 16 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase preliminar / CHAVE SUL: Internacional tabela [16, 12, 2, 2, 30, 9] jogos [14, 10, 2, 2, 27, 9] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE SUL: Santa Cruz-RS tabela [16, 5, 6, 5, 16, 16] jogos [14, 5, 6, 3, 16, 13] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase preliminar / CHAVE SUL: Aimoré tabela [16, 4, 6, 6, 10, 17] jogos [16, 4, 6, 6, 10, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase preliminar / CHAVE SUL: Guarany de Bagé tabela [16, 3, 6, 7, 12, 24] jogos [16, 2, 7, 7, 12, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Internacional tabela [18, 14, 4, 0, 22, 1] jogos [23, 17, 4, 2, 38, 10] — a tabela conta 18 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [18, 12, 4, 2, 26, 9] jogos [30, 19, 5, 6, 49, 19] — a tabela conta 18 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Flamengo-RS tabela [18, 9, 5, 4, 27, 16] jogos [28, 13, 10, 5, 36, 23] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Esportivo-RS tabela [18, 9, 5, 4, 23, 15] jogos [28, 13, 11, 4, 34, 20] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-RS tabela [18, 6, 9, 3, 14, 6] jogos [30, 11, 12, 7, 26, 15] — a tabela conta 18 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [18, 6, 5, 7, 15, 18] jogos [32, 13, 11, 8, 39, 31] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Santa Cruz-RS tabela [18, 4, 4, 10, 17, 28] jogos [29, 7, 10, 12, 29, 39] — a tabela conta 18 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Inter de Santa Maria tabela [18, 1, 6, 11, 9, 24] jogos [29, 6, 8, 15, 22, 36] — a tabela conta 18 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Pelotas tabela [18, 1, 6, 11, 7, 26] jogos [32, 5, 12, 15, 26, 38] — a tabela conta 18 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASIL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ESPORTIVO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FARROUPILHA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GAÚCHO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GUARANY
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HAMBURGO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PELOTAS
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BRASIL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- ESPORTIVO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- FARROUPILHA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- GAÚCHO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- GUARANY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- JUVENTUDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- NOVO HAMBURGO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- PELOTAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1971

- tabela publicada x jogos — Primeira fase / GRUPO B: Flamengo-RS tabela [24, 13, 6, 5, 39, 20] jogos [23, 12, 6, 5, 38, 20] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / GRUPO B: Inter de Santa Maria tabela [24, 7, 8, 9, 27, 32] jogos [23, 7, 8, 8, 26, 30] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / GRUPO B: Guarany de Bagé tabela [24, 6, 9, 9, 17, 21] jogos [23, 6, 8, 9, 16, 20] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / GRUPO B: Ypiranga-RS tabela [24, 7, 6, 11, 24, 25] jogos [25, 7, 6, 12, 24, 27] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / GRUPO B: Avenida tabela [24, 6, 7, 11, 25, 37] jogos [23, 6, 7, 10, 25, 36] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Internacional tabela [14, 10, 3, 1, 22, 6] jogos [38, 25, 11, 2, 67, 16] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [14, 9, 2, 3, 17, 8] jogos [38, 25, 8, 5, 66, 24] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Esportivo-RS tabela [14, 6, 2, 6, 13, 13] jogos [37, 22, 4, 11, 66, 37] — a tabela conta 14 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno / -: São José-RS tabela [14, 6, 1, 7, 18, 16] jogos [38, 19, 6, 13, 54, 44] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [14, 4, 5, 5, 9, 13] jogos [38, 16, 13, 9, 47, 29] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-RS tabela [14, 4, 4, 6, 9, 13] jogos [38, 15, 13, 10, 49, 30] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Gaúcho tabela [14, 2, 5, 7, 8, 18] jogos [38, 13, 13, 12, 32, 29] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Flamengo-RS tabela [14, 2, 4, 8, 9, 18] jogos [37, 14, 10, 13, 47, 38] — a tabela conta 14 jogos e as fontes trazem 37
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlântico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Avenida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamoio
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Atlântico — clube que o ogol não tem; entra só pela RSSSF
- Avenida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avenida)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani de Alegrete)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- Tamoio — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1972

- tabela publicada x jogos — Fase final / Grupo C: Cruzeiro-RS tabela [10, 5, 3, 2, 10, 5] jogos [10, 4, 4, 2, 10, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / Grupo C: Riograndense tabela [10, 2, 1, 7, 4, 8] jogos [10, 2, 2, 6, 4, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [18, 9, 3, 6, 15, 13] jogos [28, 13, 8, 7, 23, 16] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Caxias tabela [18, 8, 4, 6, 17, 16] jogos [28, 14, 6, 8, 35, 23] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [18, 6, 5, 7, 15, 18] jogos [26, 10, 9, 7, 26, 24] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Gaúcho tabela [18, 5, 6, 7, 12, 18] jogos [26, 10, 9, 7, 30, 27] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Cruzeiro-RS tabela [18, 5, 6, 7, 12, 20] jogos [28, 9, 10, 9, 22, 25] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Brasil de Pelotas tabela [18, 3, 4, 11, 9, 24] jogos [28, 10, 7, 11, 25, 29] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Aimoré tabela [18, 2, 5, 11, 7, 18] jogos [28, 6, 9, 13, 14, 23] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Santa Cruz-RS tabela [18, 1, 6, 11, 9, 29] jogos [28, 6, 8, 14, 21, 36] — a tabela conta 18 jogos e as fontes trazem 28
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sá Viana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamoio
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional (São Leopoldo))
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Sá Viana — clube que o ogol não tem; entra só pela RSSSF
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- Tamoio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tamoio)
- vencedor da final pelos jogos (Brasil de Pelotas) diferente do campeão oficial (Internacional); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1973

- tabela publicada x jogos — Primeira fase / -: Cruzeiro-RS tabela [19, 5, 7, 7, 11, 14] jogos [18, 4, 7, 7, 10, 14] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Atlético-RS tabela [19, 4, 6, 9, 16, 24] jogos [20, 5, 6, 9, 17, 24] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Guarany de Bagé tabela [19, 4, 6, 9, 19, 28] jogos [19, 4, 6, 9, 19, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Riograndense tabela [19, 1, 6, 12, 13, 32] jogos [19, 1, 6, 12, 13, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Gaúcho tabela [11, 4, 4, 3, 13, 11] jogos [30, 13, 10, 7, 47, 34] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [11, 4, 4, 3, 15, 14] jogos [30, 14, 10, 6, 44, 22] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: AE Santo Ângelo tabela [11, 3, 6, 2, 6, 10] jogos [30, 11, 15, 4, 28, 17] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Brasil de Pelotas tabela [11, 4, 3, 4, 7, 8] jogos [30, 17, 6, 7, 35, 16] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [11, 3, 5, 3, 8, 10] jogos [30, 12, 12, 6, 32, 21] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Pelotas tabela [11, 2, 6, 3, 8, 12] jogos [30, 8, 16, 6, 27, 25] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Bagé tabela [11, 2, 4, 5, 10, 9] jogos [30, 8, 13, 9, 28, 25] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Inter de Santa Maria tabela [11, 1, 6, 4, 6, 12] jogos [30, 8, 12, 10, 25, 28] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: São José-RS tabela [11, 2, 2, 7, 5, 12] jogos [30, 10, 7, 13, 16, 23] — a tabela conta 11 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Aimoré tabela [11, 0, 6, 5, 4, 13] jogos [30, 9, 14, 7, 29, 26] — a tabela conta 11 jogos e as fontes trazem 30
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Avenida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Avenida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avenida)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brasil de Pelotas)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Fluminense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fluminense-RS)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany de Bagé)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1974

- tabela publicada x jogos — Primeira fase / -: Internacional tabela [9, 9, 0, 0, 21, 1] jogos [6, 6, 0, 0, 18, 1] — a tabela conta 9 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [9, 4, 2, 3, 10, 8] jogos [8, 4, 2, 2, 10, 7] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Gaúcho tabela [9, 3, 2, 4, 7, 10] jogos [8, 3, 2, 3, 7, 9] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Atlético-RS tabela [9, 2, 3, 4, 6, 7] jogos [8, 2, 3, 3, 6, 6] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Disputa do 3º lugar / -: Internacional tabela [9, 9, 0, 0, 22, 1] jogos [7, 7, 0, 0, 20, 1] — a tabela conta 9 jogos e as fontes trazem 7
- tabela publicada x jogos — Disputa do 3º lugar / -: Santa Cruz-RS tabela [9, 2, 3, 4, 4, 5] jogos [8, 2, 3, 3, 4, 4] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Disputa do 3º lugar / -: Esportivo-RS tabela [9, 1, 3, 5, 5, 10] jogos [8, 1, 3, 4, 5, 9] — a tabela conta 9 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ARMOUR
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CAXIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ESPORTIVO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GAÚCHO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GRÊMIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INTERNACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HAMBURGO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SÃO LUIZ
- ARMOUR — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Armour (Particulares))
- CAXIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- ESPORTIVO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- GAÚCHO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- GRÊMIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- INTERNACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- NOVO HAMBURGO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- SÃO LUIZ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luiz)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1975

- tabela publicada x jogos — Primeira fase - Final / Grupo C: AE Santo Ângelo tabela [8, 1, 4, 3, 8, 9] jogos [8, 1, 4, 3, 6, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase - Final / Grupo F: Internacional (São Borja) tabela [8, 2, 2, 4, 5, 5] jogos [8, 2, 2, 4, 5, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [19, 10, 6, 3, 27, 10] jogos [19, 10, 6, 3, 22, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Bagé tabela [19, 7, 6, 6, 15, 12] jogos [19, 6, 7, 6, 15, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: AE Santo Ângelo tabela [19, 7, 5, 7, 21, 21] jogos [19, 7, 6, 6, 22, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Guarany de Bagé tabela [19, 5, 7, 7, 17, 17] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Alegrete
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlântico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cachoeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Elite
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeado
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Hamburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio-Grandense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luiz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Alegrete — clube que o ogol não tem; entra só pela RSSSF
- Atlântico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlântico)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Cachoeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cachoeira)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- Elite — clube que o ogol não tem; entra só pela RSSSF
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani de Alegrete)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Lajeado — clube que o ogol não tem; entra só pela RSSSF
- Novo Hamburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Hamburgo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- Rio-Grandense — clube que o ogol não tem; entra só pela RSSSF
- São Luiz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luiz)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SÃO PAULO-RS)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1976

- tabela publicada x jogos — Fase preliminar / Grupo 6: Gaúcho tabela [8, 3, 5, 0, 18, 4] jogos [8, 3, 5, 0, 17, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — CLASSIFICAÇÃO PRIMEIRA TURNO / -: Estrela-RS tabela [19, 7, 5, 7, 16, 17] jogos [27, 11, 5, 11, 27, 26] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — CLASSIFICAÇÃO PRIMEIRA TURNO / -: Inter de Santa Maria tabela [19, 5, 9, 5, 18, 19] jogos [27, 8, 13, 6, 30, 24] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase final / -: Estrela-RS tabela [19, 7, 5, 7, 16, 17] jogos [27, 11, 5, 11, 27, 26] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [19, 5, 9, 5, 18, 19] jogos [27, 8, 13, 6, 30, 24] — a tabela conta 19 jogos e as fontes trazem 27
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Alegrete
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Armour
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlântico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esportivo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventude-gup
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pradense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Rosa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sá Viana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luiz
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Alegrete — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Alegrete)
- Armour — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Armour (Particulares))
- Atlântico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlântico)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- Esportivo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportivo-RS)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Grêmio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional)
- Juventude — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventude)
- Juventude-gup — clube que o ogol não tem; entra só pela RSSSF
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- Pradense — clube que o ogol não tem; entra só pela RSSSF
- Santa Rosa — clube que o ogol não tem; entra só pela RSSSF
- Sá Viana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sá Viana)
- São Luiz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luiz)

### 1977

- tabela publicada x jogos — 7-14 de Julho       13  5  3  5  12-14  13  Repescagem / -: Cachoeira tabela [13, 3, 3, 7, 12, 35] jogos [13, 3, 3, 7, 14, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [9, 6, 3, 0, 21, 1] jogos [34, 26, 5, 3, 70, 9] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Internacional tabela [9, 6, 2, 1, 13, 3] jogos [34, 22, 6, 6, 61, 21] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [9, 5, 2, 2, 13, 5] jogos [33, 19, 5, 9, 43, 19] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Santa Cruz-RS tabela [9, 3, 3, 3, 8, 10] jogos [33, 10, 12, 11, 33, 35] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Cruzeiro-RS tabela [9, 3, 2, 4, 7, 13] jogos [41, 9, 18, 14, 30, 49] — a tabela conta 9 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Caxias tabela [9, 2, 3, 4, 7, 9] jogos [33, 16, 9, 8, 33, 19] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [9, 2, 3, 4, 6, 8] jogos [33, 15, 9, 9, 39, 28] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Brasil de Pelotas tabela [9, 2, 3, 4, 4, 10] jogos [33, 7, 14, 12, 19, 33] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Pelotas tabela [9, 1, 4, 4, 4, 16] jogos [33, 8, 14, 11, 28, 39] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [9, 1, 3, 5, 3, 11] jogos [41, 14, 12, 15, 21, 33] — a tabela conta 9 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [9, 7, 1, 1, 19, 3] jogos [34, 26, 5, 3, 70, 9] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Caxias tabela [9, 6, 2, 1, 11, 3] jogos [33, 16, 9, 8, 33, 19] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Internacional tabela [9, 6, 1, 2, 14, 4] jogos [34, 22, 6, 6, 61, 21] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [9, 5, 2, 2, 9, 4] jogos [33, 19, 5, 9, 43, 19] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [9, 5, 1, 3, 11, 9] jogos [33, 15, 9, 9, 39, 28] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [9, 2, 3, 4, 2, 10] jogos [41, 14, 12, 15, 21, 33] — a tabela conta 9 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Santa Cruz-RS tabela [9, 0, 5, 4, 4, 9] jogos [33, 10, 12, 11, 33, 35] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Pelotas tabela [9, 0, 5, 4, 2, 10] jogos [33, 8, 14, 11, 28, 39] — a tabela conta 9 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Cruzeiro-RS tabela [9, 0, 5, 4, 3, 12] jogos [41, 9, 18, 14, 30, 49] — a tabela conta 9 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Brasil de Pelotas tabela [9, 0, 3, 6, 1, 12] jogos [33, 7, 14, 12, 19, 33] — a tabela conta 9 jogos e as fontes trazem 33
- data diferente entre RSSSF e ogol (mais de 3 dias) em 157 jogos (ex.: Estrela-RS x Bagé, ogol 1977-04-27); fica a do ogol

### 1978

- tabela publicada x jogos — Primeira fase / -: Novo Hamburgo tabela [10, 2, 3, 5, 6, 11] jogos [11, 2, 3, 6, 6, 12] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [10, 6, 3, 1, 25, 5] jogos [17, 7, 5, 5, 37, 17] — a tabela conta 10 jogos e as fontes trazem 17
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [10, 5, 3, 2, 13, 9] jogos [15, 7, 4, 4, 20, 18] — a tabela conta 10 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / Grupo II: Internacional tabela [10, 8, 1, 1, 22, 5] jogos [11, 9, 1, 1, 23, 5] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Grupo II: Esportivo-RS tabela [10, 1, 2, 7, 5, 21] jogos [11, 1, 2, 8, 5, 22] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Grêmio tabela [10, 6, 4, 0, 19, 5] jogos [11, 6, 4, 1, 20, 7] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Internacional tabela [10, 4, 6, 0, 15, 5] jogos [13, 7, 6, 0, 20, 6] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Esportivo-RS tabela [10, 2, 4, 4, 7, 16] jogos [13, 3, 4, 6, 10, 20] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Novo Hamburgo tabela [10, 0, 5, 5, 3, 12] jogos [11, 0, 5, 6, 4, 15] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASSOCIAÇÃO SANTA CRUZ
- ASSOCIAÇÃO SANTA CRUZ — casado pelo nome com o clube do calendário do ogol deste ano (Santa Cruz-RS)
- placar diferente no ogol — Esportivo-RS x Novo Hamburgo (1978-11-26): RSSSF 3-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Novo Hamburgo x Internacional (1978-11-16): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Juventude x Esportivo-RS (1978-09-15): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Esportivo-RS x Juventude (1978-09-10): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Esportivo-RS x Internacional (1978-11-19): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Guarany de Bagé x Juventude (1978-10-18): RSSSF 1-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Inter de Santa Maria x Cruzeiro-RS (1978-10-22): RSSSF 2-3, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Juventude x Guarany de Bagé (1978-10-01): RSSSF 0-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Cruzeiro-RS x Inter de Santa Maria (1978-10-04): RSSSF 0-1, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Grêmio x Juventude (1978-11-19): RSSSF 3-4, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Grêmio x Caxias (1978-11-01): RSSSF 5-0, ogol 3-0; fica o da RSSSF
- mando invertido no ogol — RSSSF Inter de Santa Maria 0-1 Bagé, ogol Bagé 1-0 Inter de Santa Maria (1978-08-02); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 0-2 São Paulo-RS, ogol São Paulo-RS 2-0 Santa Cruz-RS (1978-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF Farroupilha 0-4 Grêmio, ogol Grêmio 4-0 Farroupilha (1978-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-2 Cruzeiro-RS, ogol Cruzeiro-RS 2-0 AE Santo Ângelo (1978-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 1-2 Inter de Santa Maria, ogol Inter de Santa Maria 2-1 Santa Cruz-RS (1978-08-12); fica a RSSSF
- mando invertido no ogol — RSSSF 14 de Julho 1-3 Juventude, ogol Juventude 3-1 14 de Julho (1978-08-13); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 1-4 Gaúcho, ogol Gaúcho 4-1 AE Santo Ângelo (1978-08-13); fica a RSSSF
- mando invertido no ogol — RSSSF São Paulo-RS 3-6 Internacional, ogol Internacional 6-3 São Paulo-RS (1978-08-15); fica a RSSSF
- mando invertido no ogol — RSSSF Cruzeiro-RS 0-1 Esportivo-RS, ogol Esportivo-RS 1-0 Cruzeiro-RS (1978-08-16); fica a RSSSF
- mando invertido no ogol — RSSSF Novo Hamburgo 0-1 Santa Cruz-RS, ogol Santa Cruz-RS 1-0 Novo Hamburgo (1978-08-20); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 0-1 Grêmio, ogol Grêmio 1-0 Santa Cruz-RS (1978-08-23); fica a RSSSF
- mando invertido no ogol — RSSSF Farroupilha 0-1 Novo Hamburgo, ogol Novo Hamburgo 1-0 Farroupilha (1978-08-23); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-2 Brasil de Pelotas, ogol Brasil de Pelotas 2-0 AE Santo Ângelo (1978-08-23); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 0-2 Guarany de Bagé, ogol Guarany de Bagé 2-0 Santa Cruz-RS (1978-08-27); fica a RSSSF
- mando invertido no ogol — RSSSF Inter de Santa Maria 0-1 Internacional, ogol Internacional 1-0 Inter de Santa Maria (1978-08-27); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-2 Juventude, ogol Juventude 2-0 AE Santo Ângelo (1978-08-27); fica a RSSSF
- mando invertido no ogol — RSSSF Estrela-RS 0-3 Grêmio, ogol Grêmio 3-0 Estrela-RS (1978-09-03); fica a RSSSF
- mando invertido no ogol — RSSSF Esportivo-RS 0-1 Internacional, ogol Internacional 1-0 Esportivo-RS (1978-09-20); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 0-1 Caxias, ogol Caxias 1-0 Santa Cruz-RS (1978-09-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bagé 0-1 Pelotas, ogol Pelotas 1-0 Bagé (1978-09-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bagé 1-2 Caxias, ogol Caxias 2-1 Bagé (1978-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-1 Internacional, ogol Internacional 1-0 AE Santo Ângelo (1978-10-01); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-3 Farroupilha, ogol Farroupilha 3-0 AE Santo Ângelo (1978-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Brasil de Pelotas 0-1 Inter de Santa Maria, ogol Inter de Santa Maria 1-0 Brasil de Pelotas (1978-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF 14 de Julho 1-2 Internacional, ogol Internacional 2-1 14 de Julho (1978-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF AE Santo Ângelo 0-3 Estrela-RS, ogol Estrela-RS 3-0 AE Santo Ângelo (1978-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF Esportivo-RS 1-2 Farroupilha, ogol Farroupilha 2-1 Esportivo-RS (1978-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF Esportivo-RS 0-2 Estrela-RS, ogol Estrela-RS 2-0 Esportivo-RS (1978-10-15); fica a RSSSF
- mando invertido no ogol — RSSSF Gaúcho 0-1 Grêmio, ogol Grêmio 1-0 Gaúcho (1978-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Estrela-RS 0-2 Caxias, ogol Caxias 2-0 Estrela-RS (1978-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Santa Cruz-RS 0-1 Pelotas, ogol Pelotas 1-0 Santa Cruz-RS (1978-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF São Paulo-RS 0-1 Gaúcho, ogol Gaúcho 1-0 São Paulo-RS (1978-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Novo Hamburgo 0-1 Cruzeiro-RS, ogol Cruzeiro-RS 1-0 Novo Hamburgo (1978-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Esportivo-RS 0-3 Grêmio, ogol Grêmio 3-0 Esportivo-RS (1978-11-12); fica a RSSSF
- mando invertido no ogol — RSSSF Novo Hamburgo 0-1 Grêmio, ogol Grêmio 1-0 Novo Hamburgo (1978-11-22); fica a RSSSF
- mando invertido no ogol — RSSSF Juventude 0-2 Internacional, ogol Internacional 2-0 Juventude (1978-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Grêmio 1-2 Internacional, ogol Internacional 2-1 Grêmio (1978-12-17); fica a RSSSF
- jogo só no ogol, incluído em First Round - First Phase: Internacional 1-0 Novo Hamburgo (1978-09-03)
- jogo só no ogol, incluído em Second Round - First Phase / Group II: Internacional 1-0 Esportivo-RS (1978-10-04)
- jogo só no ogol, incluído em Second Round - First Phase / Group I: Juventude 4-3 Grêmio (1978-10-25)
- só na RSSSF (não achado no ogol): Novo Hamburgo 0-0 Internacional (None)
- só na RSSSF (não achado no ogol): Grêmio 2-0 Juventude (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Internacional (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-1 Cruzeiro-RS (None)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1979

- tabela publicada x jogos — 1º Turno / -: Esportivo-RS tabela [19, 9, 8, 2, 32, 18] jogos [18, 9, 7, 2, 31, 17] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: 14 de Julho tabela [19, 8, 4, 7, 21, 12] jogos [18, 8, 3, 7, 20, 11] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [19, 16, 3, 0, 37, 6] jogos [54, 43, 10, 1, 108, 15] — a tabela conta 19 jogos e as fontes trazem 54
- tabela publicada x jogos — 2º Turno / -: Internacional tabela [19, 13, 5, 1, 40, 5] jogos [54, 35, 13, 6, 109, 20] — a tabela conta 19 jogos e as fontes trazem 54
- tabela publicada x jogos — 2º Turno / -: São Paulo-RS tabela [19, 10, 7, 2, 24, 9] jogos [54, 22, 15, 17, 52, 39] — a tabela conta 19 jogos e as fontes trazem 54
- tabela publicada x jogos — 2º Turno / -: Inter de Santa Maria tabela [19, 9, 6, 4, 19, 7] jogos [20, 7, 7, 6, 13, 7] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Esportivo-RS tabela [19, 8, 7, 4, 15, 11] jogos [21, 9, 7, 5, 16, 12] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Caxias tabela [19, 8, 6, 5, 20, 13] jogos [20, 8, 7, 5, 20, 13] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Juventude tabela [19, 7, 7, 5, 21, 15] jogos [21, 8, 8, 5, 23, 16] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Brasil de Pelotas tabela [19, 6, 8, 5, 18, 17] jogos [20, 6, 8, 6, 19, 19] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Pelotas tabela [19, 6, 8, 5, 17, 16] jogos [20, 6, 9, 5, 19, 18] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Farroupilha tabela [19, 6, 8, 5, 18, 21] jogos [20, 7, 8, 5, 20, 22] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [19, 5, 8, 6, 15, 20] jogos [20, 5, 8, 7, 15, 22] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: 241325 tabela [19, 4, 5, 10, 13, 27] jogos [20, 4, 6, 10, 14, 28] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Bagé tabela [19, 3, 7, 9, 4, 12] jogos [20, 3, 9, 8, 4, 11] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Riograndense tabela [19, 5, 2, 12, 16, 38] jogos [20, 5, 2, 13, 16, 40] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Estrela-RS tabela [19, 3, 6, 10, 10, 19] jogos [20, 4, 6, 10, 12, 19] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Guarany de Bagé tabela [19, 4, 2, 13, 12, 19] jogos [20, 4, 2, 14, 12, 20] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Avenida tabela [19, 4, 2, 13, 18, 41] jogos [20, 5, 2, 13, 19, 42] — a tabela conta 19 jogos e as fontes trazem 20
- jogo só no ogol, incluído em 1. TURNO: Estrela-RS 0-0 14 de Julho-PF (1979-03-07)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 2-0 São Paulo-RS (1979-03-10)
- jogo só no ogol, incluído em 1. TURNO: Avenida 1-2 14 de Julho-PF (1979-03-14)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 0-1 Inter de Santa Maria (1979-03-18)
- jogo só no ogol, incluído em 1. TURNO: Guarany de Bagé 2-1 14 de Julho-PF (1979-03-21)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 0-0 Internacional (1979-03-25)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 1-1 Esportivo-RS (1979-03-28)
- jogo só no ogol, incluído em 1. TURNO: Juventude 1-0 14 de Julho-PF (1979-04-01)
- jogo só no ogol, incluído em 1. TURNO: Novo Hamburgo 1-0 14 de Julho-PF (1979-04-05)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 0-1 Pelotas (1979-04-08)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 5-0 Bagé (1979-04-12)
- jogo só no ogol, incluído em 1. TURNO: Riograndense 0-2 14 de Julho-PF (1979-04-15)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 2-0 Farroupilha (1979-04-18)
- jogo só no ogol, incluído em 1. TURNO: Gaúcho 1-1 14 de Julho-PF (1979-04-22)
- jogo só no ogol, incluído em 1. TURNO: Grêmio 1-0 14 de Julho-PF (1979-04-25)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 1-0 Brasil de Pelotas (1979-04-28)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 2-0 Caxias (1979-05-02)
- jogo só no ogol, incluído em 1. TURNO: Cachoeira 1-0 14 de Julho-PF (1979-05-06)
- jogo só no ogol, incluído em 1. TURNO: 14 de Julho-PF 2-1 241325 (1979-05-12)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 1-0 Guarany de Bagé (1979-05-16)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 0-2 Estrela-RS (1979-05-19)
- jogo só no ogol, incluído em 2. TURNO: São Paulo-RS 3-1 14 de Julho-PF (1979-05-23)
- jogo só no ogol, incluído em 2. TURNO: Bagé 0-0 Inter de Santa Maria (1979-05-23)
- jogo só no ogol, incluído em 2. TURNO: Internacional 0-0 Pelotas (1979-05-27)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 3-1 Avenida (1979-05-27)
- jogo só no ogol, incluído em 2. TURNO: Inter de Santa Maria 1-0 14 de Julho-PF (1979-05-30)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 2-0 Novo Hamburgo (1979-06-03)
- jogo só no ogol, incluído em 2. TURNO: Guarany de Bagé 0-1 Internacional (1979-06-06)
- jogo só no ogol, incluído em 2. TURNO: 241325 1-1 14 de Julho-PF (1979-06-06)
- jogo só no ogol, incluído em 2. TURNO: Guarany de Bagé 2-1 Riograndense (1979-06-09)
- jogo só no ogol, incluído em 2. TURNO: Esportivo-RS 1-0 14 de Julho-PF (1979-06-10)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 1-1 Juventude (1979-06-13)
- jogo só no ogol, incluído em 2. TURNO: Gaúcho 1-1 Novo Hamburgo (1979-06-17)
- jogo só no ogol, incluído em 2. TURNO: Inter de Santa Maria 0-1 Cachoeira (1979-06-17)
- jogo só no ogol, incluído em 2. TURNO: Caxias 0-0 14 de Julho-PF (1979-06-17)
- jogo só no ogol, incluído em 2. TURNO: Brasil de Pelotas 1-2 14 de Julho-PF (1979-06-20)
- jogo só no ogol, incluído em 2. TURNO: Gaúcho 2-0 14 de Julho-PF (1979-06-24)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 3-1 Cachoeira (1979-06-28)
- jogo só no ogol, incluído em 2. TURNO: Farroupilha 2-1 14 de Julho-PF (1979-07-01)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 2-0 Riograndense (1979-07-04)
- jogo só no ogol, incluído em 2. TURNO: Inter de Santa Maria 0-1 Avenida (1979-07-11)
- jogo só no ogol, incluído em 2. TURNO: Pelotas 2-2 14 de Julho-PF (1979-07-11)
- jogo só no ogol, incluído em 2. TURNO: Internacional 3-0 14 de Julho-PF (1979-07-15)
- jogo só no ogol, incluído em 2. TURNO: 14 de Julho-PF 0-0 Grêmio (1979-07-18)
- jogo só no ogol, incluído em 2. TURNO: Bagé 0-0 14 de Julho-PF (1979-07-22)
- jogo só no ogol, incluído em FASE FINAL: Internacional 1-2 Grêmio (1979-08-26)
- jogo só no ogol, incluído em FASE FINAL: Novo Hamburgo 1-0 Internacional (1979-08-29)
- jogo só no ogol, incluído em FASE FINAL: Brasil de Pelotas 0-1 Internacional (1979-09-02)
- jogo só no ogol, incluído em FASE FINAL: Internacional 0-0 Juventude (1979-09-16)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Avenida 1-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Guarany de Bagé 2-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-0 Internacional (None)
- só na RSSSF (não achado no ogol): Juventude 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 Pelotas (None)
- só na RSSSF (não achado no ogol): 14 de Julho 5-0 Bagé (None)
- só na RSSSF (não achado no ogol): Riograndense 0-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Farroupilha (None)
- só na RSSSF (não achado no ogol): Gaúcho 1-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): Grêmio 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Caxias (None)
- só na RSSSF (não achado no ogol): Cachoeira 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 241325 (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Guarany de Bagé (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-2 Estrela-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 3-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 3-1 Avenida (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): 241325 1-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Juventude (None)
- só na RSSSF (não achado no ogol): Caxias 0-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): Gaúcho 2-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 3-1 Cachoeira (None)
- só na RSSSF (não achado no ogol): Farroupilha 2-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Riograndense (None)
- só na RSSSF (não achado no ogol): Pelotas 2-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): Internacional 3-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-0 Grêmio (None)
- só na RSSSF (não achado no ogol): Bagé 0-0 14 de Julho (None)
- vice pela Wikipédia (sem final de dois clubes): Esportivo-RS

### 1980

- tabela publicada x jogos — CLASSIFICAÇÂO SEGUNDO TURNO / -: Juventude tabela [15, 6, 7, 2, 10, 12] jogos [15, 6, 7, 2, 16, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Critério de desempate: Numero de Vitorias / -: Juventude tabela [40, 11, 16, 13, 29, 38] jogos [40, 10, 18, 12, 29, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Internacional 0-0 Grêmio, ogol Grêmio 0-0 Internacional (1980-11-05); fica a RSSSF
- placar diferente no ogol — Pelotas x São Paulo-RS (1980-07-27): RSSSF 0-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Esportivo-RS x Farroupilha (1980-10-01): RSSSF 2-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Guarany de Bagé x Farroupilha (1980-10-16): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 97 jogos (ex.: Grêmio x Caxias, ogol 1980-07-20); fica a do ogol
- mando invertido no ogol — RSSSF Grêmio 0-0 Internacional, ogol Internacional 0-0 Grêmio (1980-11-23); fica a RSSSF

### 1981

- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [11, 8, 3, 0, 20, 3] jogos [11, 8, 3, 0, 22, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: São Paulo-RS tabela [11, 4, 3, 4, 8, 9] jogos [11, 4, 3, 4, 8, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Internacional tabela [22, 15, 5, 2, 34, 8] jogos [36, 23, 9, 4, 62, 17] — a tabela conta 22 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [22, 6, 11, 5, 22, 18] jogos [20, 5, 10, 5, 18, 17] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [14, 6, 7, 1, 18, 9] jogos [13, 6, 6, 1, 18, 9] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Caxias tabela [14, 4, 3, 7, 15, 12] jogos [13, 4, 2, 7, 13, 12] — a tabela conta 14 jogos e as fontes trazem 13
- jogo só no ogol, incluído em 1. TURNO: Guarany de Bagé 1-1 Internacional (1981-06-21)
- jogo só no ogol, incluído em 1. TURNO: Juventude 0-0 Internacional (1981-07-05)
- jogo só no ogol, incluído em 1. TURNO: 241325 0-1 Internacional (1981-07-09)
- jogo só no ogol, incluído em 1. TURNO: Internacional 0-1 São Paulo-RS (1981-07-19)
- jogo só no ogol, incluído em 1. TURNO: Grêmio 0-0 Internacional (1981-07-26)
- jogo só no ogol, incluído em 1. TURNO: Inter de Santa Maria 0-0 Caxias (1981-08-02)
- jogo só no ogol, incluído em 1. TURNO: 241325 4-1 Juventude (1981-08-08)
- jogo só no ogol, incluído em 2 TURNO: Internacional 2-0 241325 (1981-09-06)
- jogo só no ogol, incluído em 2 TURNO: Inter de Santa Maria 4-1 São Gabriel (1981-09-06)
- jogo só no ogol, incluído em 2 TURNO: Brasil de Pelotas 1-0 Caxias (1981-09-06)
- jogo só no ogol, incluído em 2 TURNO: Guarany de Bagé 1-1 Armour (Particulares) (1981-09-06)
- jogo só no ogol, incluído em 2 TURNO: São Paulo-RS 0-1 Internacional (1981-09-20)
- jogo só no ogol, incluído em 2 TURNO: Armour (Particulares) 1-2 Internacional (1981-09-30)
- jogo só no ogol, incluído em 2 TURNO: Internacional 0-0 Grêmio (1981-10-07)
- jogo só no ogol, incluído em FASE FINAL: 241325 0-2 Internacional (1981-10-14)
- jogo só no ogol, incluído em FASE FINAL: Internacional 3-0 São Paulo-RS (1981-10-21)
- jogo só no ogol, incluído em FASE FINAL: Internacional 2-1 Grêmio (1981-11-04)
- jogo só no ogol, incluído em FASE FINAL: Novo Hamburgo 1-1 Internacional (1981-11-25)
- jogo só no ogol, incluído em FASE FINAL: Grêmio 1-1 Internacional (1981-11-29)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1982

- tabela publicada x jogos — 1º Turno / -: Internacional tabela [11, 9, 1, 1, 24, 5] jogos [11, 9, 1, 1, 26, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Grêmio tabela [11, 9, 1, 1, 20, 4] jogos [11, 9, 1, 1, 20, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Inter de Santa Maria tabela [11, 6, 2, 3, 15, 7] jogos [11, 5, 3, 3, 14, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: 241325 tabela [11, 4, 4, 3, 13, 12] jogos [11, 3, 4, 4, 12, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Esportivo-RS tabela [11, 4, 1, 6, 12, 13] jogos [11, 4, 1, 6, 11, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Juventude tabela [11, 2, 4, 5, 6, 17] jogos [11, 3, 5, 3, 7, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [11, 7, 3, 1, 16, 6] jogos [11, 7, 3, 1, 19, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Esportivo-RS tabela [11, 7, 2, 2, 14, 7] jogos [10, 6, 2, 2, 12, 6] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [11, 3, 5, 3, 12, 13] jogos [11, 3, 5, 3, 11, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Inter de Santa Maria tabela [11, 3, 3, 5, 12, 14] jogos [10, 3, 3, 4, 11, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: 241325 tabela [11, 3, 3, 5, 7, 13] jogos [11, 3, 3, 5, 7, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Internacional tabela [10, 8, 2, 0, 18, 4] jogos [11, 9, 2, 0, 20, 4] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Grêmio tabela [10, 7, 1, 2, 18, 6] jogos [11, 7, 1, 3, 18, 8] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Esportivo-RS tabela [10, 3, 5, 2, 10, 9] jogos [11, 4, 5, 2, 12, 10] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [10, 0, 3, 7, 6, 18] jogos [11, 0, 3, 8, 7, 20] — a tabela conta 10 jogos e as fontes trazem 11
- jogo só no ogol, incluído em PRIMEIRO TURNO: São Paulo-RS 0-1 Internacional (1982-07-26)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Inter de Santa Maria 2-0 Novo Hamburgo (1982-08-01)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Brasil de Pelotas 0-0 Guarany de Bagé (1982-08-01)
- jogo só no ogol, incluído em PRIMEIRO TURNO: 241325 4-1 Esportivo-RS (1982-08-01)
- jogo só no ogol, incluído em 2. TURNO: Juventude 2-1 Internacional (1982-09-19)
- jogo só no ogol, incluído em 2. TURNO: Internacional 1-1 São Paulo-RS (1982-10-06)
- jogo só no ogol, incluído em 2. TURNO: 241325 2-0 Novo Hamburgo (1982-10-06)
- jogo só no ogol, incluído em FASE FINAL: São Paulo-RS 0-1 Internacional (1982-10-20)
- jogo só no ogol, incluído em FASE FINAL: Esportivo-RS 2-1 Inter de Santa Maria (1982-11-07)
- jogo só no ogol, incluído em FASE FINAL: Internacional 3-1 Grêmio (1982-11-07)
- jogo só no ogol, incluído em FASE FINAL: Novo Hamburgo 0-0 Internacional (1982-11-14)
- só na RSSSF (não achado no ogol): Grêmio 0-2 Internacional (None)
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1983

- tabela publicada x jogos — 2º Turno / -: Internacional tabela [22, 8, 11, 3, 20, 11] jogos [37, 16, 18, 3, 41, 18] — a tabela conta 22 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno / -: Grêmio tabela [22, 8, 10, 4, 23, 14] jogos [40, 14, 16, 10, 41, 29] — a tabela conta 22 jogos e as fontes trazem 40
- tabela publicada x jogos — 2º Turno / -: São Paulo-RS tabela [22, 8, 10, 4, 24, 15] jogos [38, 11, 16, 11, 39, 39] — a tabela conta 22 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Esportivo-RS tabela [22, 8, 10, 4, 21, 17] jogos [37, 10, 18, 9, 32, 31] — a tabela conta 22 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno / -: 241325 tabela [22, 8, 8, 6, 21, 17] jogos [36, 10, 14, 12, 28, 32] — a tabela conta 22 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno / -: Novo Hamburgo tabela [22, 7, 10, 5, 17, 13] jogos [36, 11, 15, 10, 27, 26] — a tabela conta 22 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno / -: Brasil de Pelotas tabela [22, 7, 9, 6, 15, 18] jogos [38, 13, 16, 9, 33, 29] — a tabela conta 22 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Juventude tabela [22, 6, 10, 6, 18, 14] jogos [36, 12, 13, 11, 32, 31] — a tabela conta 22 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: Grêmio tabela [14, 6, 4, 4, 18, 11] jogos [15, 6, 4, 5, 19, 13] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Novo Hamburgo tabela [14, 4, 5, 5, 10, 13] jogos [15, 5, 5, 5, 12, 14] — a tabela conta 14 jogos e as fontes trazem 15
- jogo só no ogol, incluído em 1" TURNO: Internacional 2-1 São Paulo-RS (1983-07-06)
- jogo só no ogol, incluído em 1" TURNO: Internacional 0-0 Caxias (1983-07-26)
- jogo só no ogol, incluído em 1" TURNO: Brasil de Pelotas 0-0 Grêmio (1983-08-07)
- jogo só no ogol, incluído em 2" TURNO: Internacional 0-0 241325 (1983-09-07)
- jogo só no ogol, incluído em 2" TURNO: Inter de Santa Maria 0-1 Grêmio (1983-09-07)
- jogo só no ogol, incluído em 2" TURNO: Grêmio 0-0 Brasil de Pelotas (1983-09-11)
- jogo só no ogol, incluído em 2" TURNO: Caxias 0-1 Internacional (1983-09-29)
- jogo só no ogol, incluído em 2" TURNO: Brasil de Pelotas 0-0 Internacional (1983-10-04)
- jogo só no ogol, incluído em 2" TURNO: Internacional 2-0 Esportivo-RS (1983-10-09)
- jogo só no ogol, incluído em FASE FINAL: 241325 0-0 Internacional (1983-10-12)
- jogo só no ogol, incluído em FASE FINAL: 241325 1-0 Grêmio (1983-10-23)
- jogo só no ogol, incluído em FASE FINAL: Internacional 2-0 Brasil de Pelotas (1983-10-26)
- jogo só no ogol, incluído em FASE FINAL: Novo Hamburgo 2-1 Grêmio (1983-11-23)
- vice pela Wikipédia (sem final de dois clubes): Brasil de Pelotas

### 1984

- tabela publicada x jogos — Segunda fase / -: Brasil de Pelotas tabela [13, 6, 5, 2, 14, 8] jogos [35, 15, 16, 4, 37, 20] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [13, 5, 5, 3, 9, 7] jogos [35, 12, 11, 12, 33, 35] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Aimoré tabela [13, 4, 7, 2, 11, 8] jogos [35, 12, 13, 10, 31, 31] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [13, 4, 7, 2, 12, 10] jogos [35, 10, 13, 12, 38, 44] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Inter de Santa Maria tabela [13, 4, 6, 3, 7, 4] jogos [35, 13, 14, 8, 31, 20] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Caxias tabela [13, 3, 6, 4, 9, 8] jogos [35, 11, 13, 11, 26, 24] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Pelotas tabela [13, 2, 8, 3, 7, 7] jogos [35, 9, 18, 8, 25, 21] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Santa Cruz-RS tabela [13, 3, 5, 5, 8, 11] jogos [35, 8, 12, 15, 25, 35] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Bagé tabela [13, 2, 6, 5, 5, 10] jogos [35, 6, 13, 16, 26, 40] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [13, 2, 5, 6, 6, 12] jogos [35, 15, 9, 11, 31, 23] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: São Paulo-RS tabela [13, 2, 5, 6, 7, 16] jogos [35, 6, 15, 14, 27, 43] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: 241325 tabela [13, 1, 6, 6, 5, 15] jogos [35, 7, 16, 12, 23, 33] — a tabela conta 13 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Internacional tabela [13, 9, 3, 1, 23, 4] jogos [36, 22, 10, 4, 55, 16] — a tabela conta 13 jogos e as fontes trazem 36
- tabela publicada x jogos — Segunda fase / -: Pelotas tabela [13, 7, 3, 3, 14, 8] jogos [58, 17, 25, 16, 45, 44] — a tabela conta 13 jogos e as fontes trazem 58
- tabela publicada x jogos — Segunda fase / -: 241325 tabela [13, 6, 5, 2, 11, 8] jogos [48, 13, 21, 14, 34, 41] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [13, 5, 6, 2, 14, 7] jogos [36, 15, 13, 8, 41, 26] — a tabela conta 13 jogos e as fontes trazem 36
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [13, 4, 6, 3, 9, 7] jogos [58, 19, 19, 20, 48, 51] — a tabela conta 13 jogos e as fontes trazem 58
- tabela publicada x jogos — Segunda fase / -: Inter de Santa Maria tabela [13, 4, 6, 3, 11, 10] jogos [48, 17, 20, 11, 42, 30] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [13, 3, 8, 2, 13, 8] jogos [58, 21, 21, 16, 54, 42] — a tabela conta 13 jogos e as fontes trazem 58
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [13, 6, 1, 6, 11, 12] jogos [48, 16, 14, 18, 49, 56] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Aimoré tabela [13, 4, 5, 4, 14, 14] jogos [48, 16, 18, 14, 45, 45] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Brasil de Pelotas tabela [13, 4, 4, 5, 10, 11] jogos [58, 22, 25, 11, 52, 35] — a tabela conta 13 jogos e as fontes trazem 58
- tabela publicada x jogos — Segunda fase / -: Santa Cruz-RS tabela [13, 4, 3, 6, 11, 17] jogos [48, 12, 15, 21, 36, 52] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Caxias tabela [13, 2, 5, 6, 11, 20] jogos [48, 13, 18, 17, 37, 44] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: São Paulo-RS tabela [13, 2, 4, 7, 5, 14] jogos [48, 8, 19, 21, 32, 57] — a tabela conta 13 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Bagé tabela [13, 0, 3, 10, 5, 22] jogos [48, 6, 16, 26, 31, 62] — a tabela conta 13 jogos e as fontes trazem 48
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 1985

- jogo só no ogol, incluído em 1. TURNO: Esportivo-RS 0-0 Internacional (1985-09-15)
- jogo só no ogol, incluído em 1. TURNO: Internacional 0-1 Novo Hamburgo (1985-09-29)
- jogo só no ogol, incluído em 1. TURNO: Internacional 2-0 Grêmio (1985-10-20)
- jogo só no ogol, incluído em 2. TURNO: Caxias 1-1 Internacional (1985-10-23)
- jogo só no ogol, incluído em 2. TURNO: Pelotas 0-0 Caxias (1985-11-03)
- jogo só no ogol, incluído em 2. TURNO: Aimoré 0-0 Santa Cruz-RS (1985-11-03)

### 1986

- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [13, 4, 6, 3, 13, 10] jogos [13, 4, 6, 3, 13, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [13, 3, 8, 2, 12, 16] jogos [13, 3, 8, 2, 12, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: 241325 tabela [13, 4, 3, 6, 10, 18] jogos [13, 4, 3, 6, 16, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Esportivo-RS tabela [13, 3, 3, 7, 12, 26] jogos [13, 3, 3, 7, 12, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Southern Group: Rio Grande tabela [8, 2, 5, 1, 7, 8] jogos [8, 2, 5, 1, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Southern Group: FC Riograndense tabela [8, 0, 4, 4, 4, 8] jogos [8, 0, 4, 4, 3, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Eastern Group: Pradense tabela [8, 0, 2, 6, 3, 22] jogos [8, 0, 2, 6, 4, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Eastern/Central Zone: São José-RS tabela [10, 5, 5, 0, 12, 3] jogos [11, 6, 5, 0, 13, 3] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Eastern/Central Zone: Lajeadense tabela [10, 5, 4, 1, 14, 4] jogos [9, 4, 4, 1, 13, 4] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Lajeadense tabela [14, 7, 6, 1, 13, 5] jogos [14, 7, 6, 1, 14, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ypiranga-RS tabela [14, 5, 5, 4, 11, 12] jogos [14, 5, 5, 4, 11, 13] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Avenida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dínamo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Elite
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Glória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Igrejinha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Oriental
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Passo Fundo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pradense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio-Grandense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Riograndense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rosário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Bárbara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santoangelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Gabriel
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luiz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Veranense
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Avenida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avenida)
- Botafogo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo-RS)
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-RS)
- Dínamo — clube que o ogol não tem; entra só pela RSSSF
- Elite — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Elite)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Glória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Glória)
- Igrejinha — clube que o ogol não tem; entra só pela RSSSF
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Oriental — clube que o ogol não tem; entra só pela RSSSF
- Passo Fundo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Passo Fundo)
- Pradense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pradense)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- Rio-Grandense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio-Grandense)
- Riograndense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (FC Riograndense)
- Rosário — clube que o ogol não tem; entra só pela RSSSF
- Santa Bárbara — clube que o ogol não tem; entra só pela RSSSF
- Santoangelense — clube que o ogol não tem; entra só pela RSSSF
- São Gabriel — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Gabriel)
- São Luiz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luiz)
- Veranense — clube que o ogol não tem; entra só pela RSSSF
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Cruzeiro-RS (1986-04-06)
- só na RSSSF (não achado no ogol): São Gabriel 2-1 Rosário-RS (1986-04-06)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-2 São Gabriel (1986-04-13)
- só na RSSSF (não achado no ogol): Rosário-RS 0-1 14 de Julho (1986-04-13)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 2-0 Rosário-RS (1986-04-20)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Grêmio Santanense (1986-04-20)
- só na RSSSF (não achado no ogol): São Gabriel 1-2 14 de Julho (1986-04-27)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Cruzeiro-RS (1986-04-27)
- só na RSSSF (não achado no ogol): Rosário-RS 2-1 Grêmio Santanense (1986-05-01)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-1 São Gabriel (1986-05-01)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-1 14 de Julho (1986-05-04)
- só na RSSSF (não achado no ogol): Rosário-RS 2-2 São Gabriel (1986-05-04)
- só na RSSSF (não achado no ogol): São Gabriel 1-1 Grêmio Santanense (1986-05-11)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 Rosário-RS (1986-05-11)
- só na RSSSF (não achado no ogol): Rosário-RS 1-0 Cruzeiro-RS (1986-05-18)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-2 14 de Julho (1986-05-18)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 São Gabriel (1986-05-25)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 2-0 Grêmio Santanense (1986-05-25)
- só na RSSSF (não achado no ogol): Grêmio Santanense 3-1 Rosário-RS (1986-06-01)
- só na RSSSF (não achado no ogol): São Gabriel 0-1 Cruzeiro-RS (1986-06-01)
- só na RSSSF (não achado no ogol): Guarany de Bagé 3-1 FC Riograndense (1986-04-05)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Farroupilha (1986-04-06)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Guarany de Bagé (1986-04-12)
- só na RSSSF (não achado no ogol): FC Riograndense 0-0 Rio-Grandense (1986-04-13)
- só na RSSSF (não achado no ogol): Rio-Grandense 3-1 Rio Grande (1986-04-19)
- só na RSSSF (não achado no ogol): Farroupilha 1-0 FC Riograndense (1986-04-21)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Farroupilha (1986-04-26)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-1 Rio-Grandense (1986-04-27)
- só na RSSSF (não achado no ogol): Farroupilha 0-0 Guarany de Bagé (1986-05-01)
- só na RSSSF (não achado no ogol): FC Riograndense None-None Rio Grande (1986-05-01)
- só na RSSSF (não achado no ogol): Farroupilha 0-2 Rio-Grandense (1986-05-03)
- só na RSSSF (não achado no ogol): FC Riograndense 1-1 Guarany de Bagé (1986-05-04)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-0 Rio Grande (1986-05-10)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 FC Riograndense (1986-05-11)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Rio-Grandense (1986-05-17)
- só na RSSSF (não achado no ogol): FC Riograndense 1-1 Farroupilha (1986-05-18)
- só na RSSSF (não achado no ogol): Farroupilha 1-1 Rio Grande (1986-05-24)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-1 Guarany de Bagé (1986-05-24)
- só na RSSSF (não achado no ogol): Rio Grande 2-0 FC Riograndense (1986-05-29)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-1 Farroupilha (1986-05-29)
- só na RSSSF (não achado no ogol): Estrela-RS 1-0 Avenida (1986-04-06)
- só na RSSSF (não achado no ogol): Igrejinha 1-1 Brasil de Pelotas (1986-04-06)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Igrejinha (1986-04-13)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-0 Estrela-RS (1986-04-23)
- só na RSSSF (não achado no ogol): Avenida 5-2 Brasil de Pelotas (1986-04-20)
- só na RSSSF (não achado no ogol): Estrela-RS 1-1 Lajeadense (1986-04-20)
- só na RSSSF (não achado no ogol): Igrejinha 1-2 Estrela-RS (1986-04-27)
- só na RSSSF (não achado no ogol): Lajeadense 2-0 Avenida (1986-04-27)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-0 Lajeadense (1986-05-01)
- só na RSSSF (não achado no ogol): Avenida 3-1 Igrejinha (1986-05-01)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-4 Igrejinha (1986-05-04)
- só na RSSSF (não achado no ogol): Avenida 2-0 Estrela-RS (1986-05-05)
- só na RSSSF (não achado no ogol): Igrejinha 0-2 Lajeadense (1986-05-11)
- só na RSSSF (não achado no ogol): Estrela-RS 0-1 Brasil de Pelotas (1986-05-11)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-0 Avenida (1986-05-18)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Estrela-RS (1986-05-18)
- só na RSSSF (não achado no ogol): Estrela-RS 3-0 Igrejinha (1986-05-25)
- só na RSSSF (não achado no ogol): Avenida 1-0 Lajeadense (1986-05-25)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Brasil de Pelotas (1986-05-29)
- só na RSSSF (não achado no ogol): Igrejinha 1-3 Avenida (1986-05-31)
- só na RSSSF (não achado no ogol): Glória 2-1 Veranense (1986-04-06)
- só na RSSSF (não achado no ogol): Pratense 0-0 Pradense (1986-04-06)
- só na RSSSF (não achado no ogol): São José-RS 5-0 Pratense (1986-04-12)
- só na RSSSF (não achado no ogol): Pradense 0-4 Glória (1986-04-13)
- só na RSSSF (não achado no ogol): Veranense 1-0 Pradense (1986-04-20)
- só na RSSSF (não achado no ogol): Glória 1-1 São José-RS (1986-04-20)
- só na RSSSF (não achado no ogol): São José-RS 2-0 Veranense (1986-04-26)
- só na RSSSF (não achado no ogol): Pratense 0-1 Glória (1986-04-27)
- só na RSSSF (não achado no ogol): Pradense 3-8 São José-RS (1986-05-01)
- só na RSSSF (não achado no ogol): Veranense 1-2 Pratense (1986-06-02)
- só na RSSSF (não achado no ogol): Veranense 0-1 Glória (1986-05-04)
- só na RSSSF (não achado no ogol): Pradense 0-2 Pratense (1986-05-04)
- só na RSSSF (não achado no ogol): Pratense 0-2 São José-RS (1986-05-10)
- só na RSSSF (não achado no ogol): Glória 6-0 Pradense (1986-05-11)
- só na RSSSF (não achado no ogol): São José-RS 6-0 Glória (1986-05-17)
- só na RSSSF (não achado no ogol): Pradense 1-1 Veranense (1986-05-18)
- só na RSSSF (não achado no ogol): Glória 1-1 Pratense (1986-05-25)
- só na RSSSF (não achado no ogol): Veranense 1-0 São José-RS (1986-05-25)
- só na RSSSF (não achado no ogol): São José-RS 1-0 Pradense (1986-05-29)
- só na RSSSF (não achado no ogol): Pratense 1-0 Veranense (1986-05-31)
- só na RSSSF (não achado no ogol): Botafogo-RS 0-1 Dínamo (1986-04-06)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Passo Fundo (1986-04-06)
- só na RSSSF (não achado no ogol): Oriental-RS 3-4 Ypiranga-RS (1986-04-13)
- só na RSSSF (não achado no ogol): Passo Fundo 3-1 Botafogo-RS (1986-04-13)
- só na RSSSF (não achado no ogol): Dínamo 0-0 Passo Fundo (1986-04-20)
- só na RSSSF (não achado no ogol): Botafogo-RS 0-0 Oriental-RS (1986-04-20)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 Botafogo-RS (1986-04-27)
- só na RSSSF (não achado no ogol): Oriental-RS 1-3 Dínamo (1986-04-27)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 Oriental-RS (1986-05-01)
- só na RSSSF (não achado no ogol): Dínamo 0-0 Ypiranga-RS (1986-05-01)
- só na RSSSF (não achado no ogol): Dínamo 2-3 Botafogo-RS (1986-05-04)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 Ypiranga-RS (1986-05-04)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Oriental-RS (1986-05-11)
- só na RSSSF (não achado no ogol): Botafogo-RS 0-2 Passo Fundo (1986-05-11)
- só na RSSSF (não achado no ogol): Passo Fundo 2-0 Dínamo (1986-05-18)
- só na RSSSF (não achado no ogol): Oriental-RS 3-3 Botafogo-RS (1986-05-18)
- só na RSSSF (não achado no ogol): Botafogo-RS 1-1 Ypiranga-RS (1986-05-25)
- só na RSSSF (não achado no ogol): Dínamo 2-0 Oriental-RS (1986-05-25)
- só na RSSSF (não achado no ogol): Ypiranga-RS 3-0 Dínamo (1986-06-30)
- só na RSSSF (não achado no ogol): Oriental-RS 0-2 Passo Fundo (1986-05-31)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 Santa Bárbara-RS (1986-04-06)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Guarany-RS (1986-04-09)
- só na RSSSF (não achado no ogol): Elite 2-3 São Luiz (1986-04-13)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 Santoangelense (1986-04-13)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-0 Guarany-RS (1986-04-20)
- só na RSSSF (não achado no ogol): Santoangelense 1-0 Elite (1986-04-20)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Santoangelense (1986-04-27)
- só na RSSSF (não achado no ogol): Elite 2-1 Santa Bárbara-RS (1986-04-27)
- só na RSSSF (não achado no ogol): Guarany-RS 3-0 Elite (1986-05-01)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-1 São Luiz (1986-05-01)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-1 Santoangelense (1986-05-04)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 São Luiz (1986-05-04)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Elite (1986-05-11)
- só na RSSSF (não achado no ogol): Santoangelense 2-2 Guarany-RS (1986-05-11)
- só na RSSSF (não achado no ogol): Guarany-RS 2-0 Santa Bárbara-RS (1986-05-18)
- só na RSSSF (não achado no ogol): Elite 1-1 Santoangelense (1986-05-18)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 São Luiz (1986-05-25)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-0 Elite (1986-05-25)
- só na RSSSF (não achado no ogol): Elite 0-1 Guarany-RS (1986-06-01)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Santa Bárbara-RS (1986-06-01)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Guarany-RS (1986-06-24)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 São Luiz (1986-06-30)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-2 Rio Grande (1986-07-06)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-0 Farroupilha (1986-07-06)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 São Gabriel (1986-07-06)
- só na RSSSF (não achado no ogol): Farroupilha 1-0 Cruzeiro-RS (1986-07-12)
- só na RSSSF (não achado no ogol): São Gabriel 0-0 Rio-Grandense (1986-07-12)
- só na RSSSF (não achado no ogol): Rio Grande 0-0 14 de Julho (1986-07-13)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-1 14 de Julho (1986-07-19)
- só na RSSSF (não achado no ogol): São Gabriel 1-1 Farroupilha (1986-07-20)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-2 Rio Grande (1986-07-20)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-0 São Gabriel (1986-07-27)
- só na RSSSF (não achado no ogol): 14 de Julho 0-0 Rio-Grandense (1986-07-27)
- só na RSSSF (não achado no ogol): Rio Grande 3-0 Farroupilha (1986-07-27)
- só na RSSSF (não achado no ogol): Rio-Grandense 2-0 Cruzeiro-RS (1986-08-03)
- só na RSSSF (não achado no ogol): São Gabriel 0-0 Rio Grande (1986-08-03)
- só na RSSSF (não achado no ogol): Farroupilha 2-0 14 de Julho (1986-08-03)
- só na RSSSF (não achado no ogol): Rio Grande 0-1 Cruzeiro-RS (1986-08-10)
- só na RSSSF (não achado no ogol): Farroupilha 3-0 Rio-Grandense (1986-08-10)
- só na RSSSF (não achado no ogol): São Gabriel 0-3 14 de Julho (1986-08-10)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 0-0 Farroupilha (1986-08-17)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Rio Grande (1986-08-17)
- só na RSSSF (não achado no ogol): Rio-Grandense 3-1 São Gabriel (1986-08-17)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Cruzeiro-RS (1986-08-24)
- só na RSSSF (não achado no ogol): Farroupilha 1-0 São Gabriel (1986-08-24)
- só na RSSSF (não achado no ogol): Rio Grande 1-0 Rio-Grandense (1986-08-24)
- só na RSSSF (não achado no ogol): São Gabriel 2-4 Cruzeiro-RS (1986-08-30)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-1 14 de Julho (1986-08-31)
- só na RSSSF (não achado no ogol): Farroupilha 1-1 Rio Grande (1986-08-31)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 0-0 Rio-Grandense (1986-09-07)
- só na RSSSF (não achado no ogol): Rio Grande 3-1 São Gabriel (1986-09-07)
- só na RSSSF (não achado no ogol): 14 de Julho 0-0 Farroupilha (1986-09-07)
- só na RSSSF (não achado no ogol): São José-RS 1-1 Lajeadense (1986-07-05)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 Glória (1986-07-06)
- só na RSSSF (não achado no ogol): Pratense 0-0 Avenida (1986-07-06)
- só na RSSSF (não achado no ogol): Glória 0-1 São José-RS (1986-07-12)
- só na RSSSF (não achado no ogol): Lajeadense 2-0 Pratense (1986-07-12)
- só na RSSSF (não achado no ogol): Avenida 2-3 Estrela-RS (1986-07-12)
- só na RSSSF (não achado no ogol): São José-RS 5-1 Pratense (1986-07-19)
- só na RSSSF (não achado no ogol): Avenida 1-2 Glória (1986-07-19)
- só na RSSSF (não achado no ogol): Estrela-RS 2-1 Lajeadense (1986-07-19)
- só na RSSSF (não achado no ogol): São José-RS 0-0 Avenida (1986-07-27)
- só na RSSSF (não achado no ogol): Pratense 0-1 Estrela-RS (1986-07-27)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Glória (1986-07-27)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 São José-RS (1986-08-03)
- só na RSSSF (não achado no ogol): Avenida 0-1 São José-RS (1986-08-03)
- só na RSSSF (não achado no ogol): Glória 4-0 Pratense (1986-08-03)
- só na RSSSF (não achado no ogol): Lajeadense 1-1 São José-RS (1986-08-10)
- só na RSSSF (não achado no ogol): Glória 1-0 Estrela-RS (1986-08-10)
- só na RSSSF (não achado no ogol): Avenida 3-2 Pratense (1986-08-10)
- só na RSSSF (não achado no ogol): São José-RS 1-0 Glória (1986-08-17)
- só na RSSSF (não achado no ogol): Pratense 0-4 Lajeadense (1986-08-17)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 Avenida (1986-08-17)
- só na RSSSF (não achado no ogol): Pratense 0-2 São José-RS (1986-08-24)
- só na RSSSF (não achado no ogol): Glória 2-1 Avenida (1986-08-24)
- só na RSSSF (não achado no ogol): Lajeadense 3-0 Estrela-RS (1986-08-24)
- só na RSSSF (não achado no ogol): Avenida 0-0 São José-RS (1986-08-31)
- só na RSSSF (não achado no ogol): Estrela-RS 3-1 Pratense (1986-08-31)
- só na RSSSF (não achado no ogol): Glória 0-0 Lajeadense (1986-08-31)
- só na RSSSF (não achado no ogol): São José-RS 1-0 Estrela-RS (1986-09-06)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 Avenida (1986-09-07)
- só na RSSSF (não achado no ogol): Pratense 1-2 Glória (1986-09-07)
- só na RSSSF (não achado no ogol): Santoangelense 1-0 Ypiranga-RS (1986-07-04)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Dínamo (1986-07-06)
- só na RSSSF (não achado no ogol): São Luiz 0-1 Passo Fundo (1986-07-06)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 Guarany-RS (1986-07-12)
- só na RSSSF (não achado no ogol): Dínamo 0-1 Santoangelense (1986-07-12)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 São Luiz (1986-07-12)
- só na RSSSF (não achado no ogol): Guarany-RS 3-2 Santoangelense (1986-07-19)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Passo Fundo (1986-07-19)
- só na RSSSF (não achado no ogol): São Luiz 2-1 Dínamo (1986-07-19)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 Ypiranga-RS (1986-07-27)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 São Luiz (1986-07-27)
- só na RSSSF (não achado no ogol): Dínamo 2-0 Passo Fundo (1986-07-27)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Guarany-RS (1986-08-02)
- só na RSSSF (não achado no ogol): Ypiranga-RS 3-0 Dínamo (1986-08-03)
- só na RSSSF (não achado no ogol): Passo Fundo 3-0 Santoangelense (1986-08-03)
- só na RSSSF (não achado no ogol): Dínamo 0-1 Guarany-RS (1986-08-10)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 São Luiz (1986-08-10)
- só na RSSSF (não achado no ogol): Ypiranga-RS 5-2 Santoangelense (1986-08-10)
- só na RSSSF (não achado no ogol): Guarany-RS 1-2 Passo Fundo (1986-08-17)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 Dínamo (1986-08-17)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Ypiranga-RS (1986-08-17)
- só na RSSSF (não achado no ogol): Santoangelense 2-1 Guarany-RS (1986-08-24)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 Ypiranga-RS (1986-08-24)
- só na RSSSF (não achado no ogol): Dínamo 0-0 São Luiz (1986-08-24)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-0 Guarany-RS (1986-08-31)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Santoangelense (1986-08-31)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 Dínamo (1986-08-31)
- só na RSSSF (não achado no ogol): Guarany-RS 4-0 São Luiz (1986-09-07)
- só na RSSSF (não achado no ogol): Dínamo 0-2 Ypiranga-RS (1986-09-07)
- só na RSSSF (não achado no ogol): Santoangelense 0-1 Passo Fundo (1986-09-07)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Ypiranga-RS (1986-09-10)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 Guarany-RS (1986-09-14)
- só na RSSSF (não achado no ogol): Rosário-RS 1-1 Grêmio Santanense (1986-07-06)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Rosário-RS (1986-07-13)
- só na RSSSF (não achado no ogol): Igrejinha 3-3 Brasil de Pelotas (1986-07-06)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-2 Igrejinha (1986-07-12)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-0 Igrejinha (1986-07-06)
- só na RSSSF (não achado no ogol): Pradense 3-1 Veranense (1986-07-06)
- só na RSSSF (não achado no ogol): Veranense 1-2 Pradense (1986-07-12)
- só na RSSSF (não achado no ogol): Oriental-RS 0-1 Botafogo-RS (1986-07-06)
- só na RSSSF (não achado no ogol): Botafogo-RS 1-0 Oriental-RS (1986-07-12)
- só na RSSSF (não achado no ogol): Elite 1-2 Santa Bárbara-RS (1986-07-06)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 3-2 Elite (1986-07-12)
- só na RSSSF (não achado no ogol): Guarany de Bagé 2-1 Grêmio Santanense (1986-07-19)
- só na RSSSF (não achado no ogol): Grêmio Santanense 3-1 Guarany de Bagé (1986-07-26)
- só na RSSSF (não achado no ogol): Pradense 0-1 Brasil de Pelotas (1986-07-19)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-0 Pradense (None)
- só na RSSSF (não achado no ogol): Botafogo-RS 2-2 Santa Bárbara-RS (1986-07-19)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-0 Botafogo-RS (1986-07-27)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Santa Bárbara-RS (1986-08-03)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-1 Guarany de Bagé (1986-08-10)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-1 Brasil de Pelotas (1986-08-17)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-1 Brasil de Pelotas (1986-08-24)
- só na RSSSF (não achado no ogol): Guarany de Bagé None-None Santa Bárbara-RS (1986-08-31)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 3-1 Guarany de Bagé (1986-09-07)
- só na RSSSF (não achado no ogol): Lajeadense 0-1 Passo Fundo (1986-09-21)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-2 São José-RS (1986-09-21)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Guarany de Bagé (1986-09-21)
- só na RSSSF (não achado no ogol): Rio Grande 2-1 14 de Julho (1986-09-21)
- só na RSSSF (não achado no ogol): São José-RS 2-1 Rio Grande (1986-09-27)
- só na RSSSF (não achado no ogol): Passo Fundo 3-1 Brasil de Pelotas (1986-09-28)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-1 Lajeadense (1986-09-28)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Ypiranga-RS (1986-09-28)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-1 Passo Fundo (1986-10-05)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Brasil de Pelotas (1986-10-05)
- só na RSSSF (não achado no ogol): Lajeadense 2-1 14 de Julho (1986-10-05)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 São José-RS (1986-10-05)
- só na RSSSF (não achado no ogol): São José-RS 1-3 Lajeadense (1986-10-11)
- só na RSSSF (não achado no ogol): Passo Fundo 2-0 Rio Grande (1986-10-12)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Guarany de Bagé (1986-10-12)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Ypiranga-RS (1986-10-12)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 14 de Julho (1986-10-15)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Rio Grande (1986-10-15)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-2 São José-RS (1986-10-15)
- só na RSSSF (não achado no ogol): Lajeadense 1-1 Brasil de Pelotas (1986-10-15)
- só na RSSSF (não achado no ogol): São José-RS 2-1 14 de Julho (1986-10-18)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-2 Passo Fundo (1986-10-19)
- só na RSSSF (não achado no ogol): Rio Grande 0-2 Lajeadense (1986-10-19)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Guarany de Bagé (1986-10-19)
- só na RSSSF (não achado no ogol): Passo Fundo 0-1 São José-RS (1986-10-26)
- só na RSSSF (não achado no ogol): 14 de Julho 2-0 Brasil de Pelotas (1986-10-26)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-0 Rio Grande (1986-10-26)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Ypiranga-RS (1986-10-26)
- só na RSSSF (não achado no ogol): São José-RS 1-1 Brasil de Pelotas (1986-11-01)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 Lajeadense (1986-11-02)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-0 Ypiranga-RS (1986-11-02)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Rio Grande (1986-11-02)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Passo Fundo (1986-11-09)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 Guarany de Bagé (1986-11-09)
- só na RSSSF (não achado no ogol): Rio Grande 1-2 São José-RS (1986-11-09)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 14 de Julho (1986-11-09)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-2 Rio Grande (1986-11-12)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Guarany de Bagé (1986-11-12)
- só na RSSSF (não achado no ogol): 14 de Julho 0-0 Lajeadense (1986-11-12)
- só na RSSSF (não achado no ogol): São José-RS 0-0 Ypiranga-RS (1986-11-12)
- só na RSSSF (não achado no ogol): Rio Grande 0-1 Passo Fundo (1986-11-16)
- só na RSSSF (não achado no ogol): Guarany de Bagé 2-0 14 de Julho (1986-11-16)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Brasil de Pelotas (1986-11-16)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 São José-RS (1986-11-16)
- só na RSSSF (não achado no ogol): Rio Grande 3-0 Ypiranga-RS (1986-11-19)
- só na RSSSF (não achado no ogol): 14 de Julho 0-2 Passo Fundo (1986-11-19)
- só na RSSSF (não achado no ogol): São José-RS 2-0 Guarany de Bagé (1986-11-19)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Lajeadense (1986-11-20)
- só na RSSSF (não achado no ogol): Passo Fundo 3-1 Ypiranga-RS (1986-11-23)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 São José-RS (1986-11-23)
- só na RSSSF (não achado no ogol): Lajeadense 2-1 Rio Grande (1986-11-23)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-1 Brasil de Pelotas (1986-11-23)
- só na RSSSF (não achado no ogol): São José-RS 0-0 Passo Fundo (1986-11-30)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-2 14 de Julho (1986-11-30)
- só na RSSSF (não achado no ogol): Rio Grande 0-0 Guarany de Bagé (1986-11-30)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-0 Lajeadense (1986-11-30)
- vencedor da final pelos jogos (Passo Fundo) diferente do campeão oficial (Grêmio); fica o oficial

### 1987

- tabela publicada x jogos — Primeira fase / -: Caxias tabela [6, 3, 1, 2, 6, 5] jogos [42, 14, 19, 9, 44, 37] — a tabela conta 6 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Grêmio tabela [6, 3, 1, 2, 6, 5] jogos [49, 23, 18, 8, 65, 33] — a tabela conta 6 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Internacional tabela [6, 2, 1, 3, 6, 6] jogos [49, 25, 16, 8, 74, 29] — a tabela conta 6 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Juventude tabela [6, 1, 3, 2, 4, 6] jogos [48, 16, 21, 11, 45, 39] — a tabela conta 6 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Internacional tabela [13, 6, 6, 1, 19, 5] jogos [19, 10, 7, 2, 29, 9] — a tabela conta 13 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [13, 5, 8, 0, 15, 8] jogos [19, 6, 10, 3, 19, 16] — a tabela conta 13 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Inter de Santa Maria tabela [13, 4, 8, 1, 11, 3] jogos [19, 5, 8, 6, 12, 11] — a tabela conta 13 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [13, 6, 3, 4, 15, 6] jogos [19, 9, 6, 4, 23, 9] — a tabela conta 13 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Internacional tabela [6, 4, 1, 1, 10, 4] jogos [49, 25, 16, 8, 74, 29] — a tabela conta 6 jogos e as fontes trazem 49
- tabela publicada x jogos — Segunda fase / -: Grêmio tabela [6, 3, 3, 0, 8, 3] jogos [49, 23, 18, 8, 65, 33] — a tabela conta 6 jogos e as fontes trazem 49
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [6, 1, 2, 3, 4, 8] jogos [48, 16, 21, 11, 45, 39] — a tabela conta 6 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Inter de Santa Maria tabela [6, 1, 0, 5, 1, 8] jogos [32, 7, 13, 12, 19, 26] — a tabela conta 6 jogos e as fontes trazem 32
- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [26, 10, 8, 8, 27, 25] jogos [25, 10, 7, 8, 26, 25] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Brasil de Pelotas tabela [26, 6, 15, 5, 22, 18] jogos [25, 6, 14, 5, 21, 17] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Novo Hamburgo tabela [26, 5, 8, 13, 25, 37] jogos [26, 5, 8, 13, 26, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — CHAMPIONSHIP TOURNAMENT STANDINGS / -: Grêmio tabela [10, 6, 4, 0, 17, 7] jogos [11, 6, 5, 0, 17, 7] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — CHAMPIONSHIP TOURNAMENT STANDINGS / -: Internacional tabela [10, 5, 3, 2, 11, 6] jogos [11, 5, 4, 2, 11, 6] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Grêmio tabela [48, 24, 15, 9, 65, 33] jogos [49, 23, 18, 8, 65, 33] — a tabela conta 48 jogos e as fontes trazem 49
- tabela publicada x jogos — Fase final / -: Internacional tabela [42, 21, 14, 7, 64, 25] jogos [49, 25, 16, 8, 74, 29] — a tabela conta 42 jogos e as fontes trazem 49
- tabela publicada x jogos — Fase final / -: Esportivo-RS tabela [36, 13, 13, 10, 33, 33] jogos [36, 13, 13, 10, 33, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Caxias tabela [42, 15, 17, 10, 44, 37] jogos [42, 14, 19, 9, 44, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Brasil de Pelotas tabela [36, 6, 17, 13, 28, 36] jogos [48, 7, 22, 19, 41, 61] — a tabela conta 36 jogos e as fontes trazem 48
- tabela publicada x jogos — Fase final / -: Novo Hamburgo tabela [26, 5, 8, 13, 25, 37] jogos [26, 5, 8, 13, 26, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Frontier Group: São Gabriel tabela [12, 4, 5, 3, 12, 11] jogos [12, 4, 5, 3, 11, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Frontier Group: Brasil de Pelotas tabela [12, 1, 5, 6, 13, 26] jogos [12, 1, 5, 6, 13, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Eastern Group: Pradense tabela [12, 5, 4, 3, 13, 9] jogos [12, 5, 4, 3, 14, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Eastern Group: Veranense tabela [12, 2, 5, 5, 8, 15] jogos [12, 2, 6, 4, 9, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Eastern Group: Pratense tabela [12, 2, 4, 6, 8, 15] jogos [12, 1, 5, 6, 8, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Northern Group: Gaúcho tabela [10, 4, 2, 4, 15, 12] jogos [10, 3, 2, 5, 9, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Northern Group: Tabajara Guaíba tabela [10, 0, 2, 8, 8, 28] jogos [10, 1, 2, 7, 8, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / "Missões" Group: Botafogo/TM tabela [14, 1, 6, 7, 13, 24] jogos [14, 1, 6, 7, 14, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — with the top 2 of Losers group of the 3rd phase / -: Veranense tabela [8, 4, 2, 2, 9, 10] jogos [8, 4, 2, 2, 8, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — with the top 2 of Losers group of the 3rd phase / -: Dalban tabela [8, 2, 4, 2, 9, 8] jogos [8, 2, 4, 2, 8, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Veranense tabela [4, 1, 3, 0, 7, 6] jogos [10, 3, 4, 3, 13, 15] — a tabela conta 4 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Tabajara Guaíba tabela [4, 1, 2, 1, 6, 7] jogos [10, 1, 6, 3, 12, 14] — a tabela conta 4 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Rio-Grandense tabela [2, 1, 1, 0, 1, 0] jogos [22, 5, 8, 9, 13, 25] — a tabela conta 2 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Elite tabela [2, 0, 2, 0, 1, 1] jogos [22, 6, 13, 3, 25, 17] — a tabela conta 2 jogos e as fontes trazem 22
- tabela publicada x jogos — 2nd and 3rd Phase Losers Group winners playoff / -: Elite tabela [6, 2, 4, 0, 9, 5] jogos [46, 18, 20, 8, 69, 34] — a tabela conta 6 jogos e as fontes trazem 46
- tabela publicada x jogos — 2nd and 3rd Phase Losers Group winners playoff / -: Rio-Grandense tabela [6, 2, 3, 1, 7, 7] jogos [38, 8, 14, 16, 25, 51] — a tabela conta 6 jogos e as fontes trazem 38
- tabela publicada x jogos — 2nd and 3rd Phase Losers Group winners playoff / -: Veranense tabela [6, 2, 1, 3, 6, 9] jogos [30, 9, 12, 9, 30, 39] — a tabela conta 6 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Guarany-RS tabela [14, 6, 7, 1, 12, 8] jogos [16, 8, 7, 1, 16, 10] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Aimoré tabela [14, 5, 9, 0, 9, 3] jogos [16, 5, 9, 2, 11, 7] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Elite tabela [14, 4, 7, 3, 15, 11] jogos [22, 6, 13, 3, 25, 17] — a tabela conta 14 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Rio-Grandense tabela [14, 2, 4, 8, 5, 18] jogos [22, 5, 8, 9, 13, 25] — a tabela conta 14 jogos e as fontes trazem 22
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 14 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aurora
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Avenida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bagé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo/FV
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo/TM
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dalban
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dínamo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Farroupilha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gaúcho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Igrejinha
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Oriental
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pradense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio-Grandense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rosário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Bárbara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santoangelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Gabriel
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luiz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tabajara Guaíba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Três Passos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Veranense
- 14 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (14 de Julho)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Aurora — clube que o ogol não tem; entra só pela RSSSF
- Avenida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avenida)
- Bagé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Botafogo/FV — clube que o ogol não tem; entra só pela RSSSF
- Botafogo/TM — clube que o ogol não tem; entra só pela RSSSF
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-RS)
- Dalban — clube que o ogol não tem; entra só pela RSSSF
- Dínamo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Dínamo)
- Farroupilha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Farroupilha)
- Gaúcho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gaúcho)
- Igrejinha — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Igrejinha)
- Oriental — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Oriental-RS)
- Pradense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pradense)
- Rio Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- Rio-Grandense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio-Grandense)
- Rosário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rosário-RS)
- Santa Bárbara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Bárbara-RS)
- Santoangelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santoangelense)
- São Gabriel — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Gabriel)
- São Luiz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luiz)
- Tabajara Guaíba — clube que o ogol não tem; entra só pela RSSSF
- Três Passos — clube que o ogol não tem; entra só pela RSSSF
- Veranense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Veranense)
- placar corrigido pelo ogol — Santa Cruz-RS x Lajeadense (1987-02-23): RSSSF 2-1, ogol 2-2; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Inter de Santa Maria x Pelotas (1987-05-26): RSSSF 0-0, ogol 1-1; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Grêmio x Lajeadense, ogol 1987-02-21); fica a do ogol
- jogo só no ogol, incluído em First Phase: Internacional 2-0 Juventude (1987-03-22)
- jogo só no ogol, incluído em First Phase: Caxias 0-0 Grêmio (1987-03-22)
- jogo só no ogol, incluído em First Phase: Grêmio 1-1 Juventude (1987-03-25)
- jogo só no ogol, incluído em First Phase: Caxias 2-1 Internacional (1987-03-25)
- jogo só no ogol, incluído em First Phase: Grêmio 2-1 Internacional (1987-03-29)
- jogo só no ogol, incluído em First Phase: Juventude 1-1 Caxias (1987-03-29)
- jogo só no ogol, incluído em First Phase: Internacional 1-0 Caxias (1987-04-01)
- jogo só no ogol, incluído em First Phase: Juventude 1-0 Grêmio (1987-04-01)
- jogo só no ogol, incluído em First Phase: Internacional 0-1 Grêmio (1987-04-05)
- jogo só no ogol, incluído em First Phase: Caxias 1-0 Juventude (1987-04-05)
- jogo só no ogol, incluído em First Phase: Grêmio 2-2 Caxias (1987-04-08)
- jogo só no ogol, incluído em First Phase: Juventude 1-1 Internacional (1987-04-08)
- jogo só no ogol, incluído em SECOND STAGE(SECOND TURN): Esportivo-RS 1-1 Brasil de Pelotas (1987-05-17)
- jogo só no ogol, incluído em SECOND STAGE(SECOND TURN): Grêmio 2-2 Juventude (1987-05-28)
- jogo só no ogol, incluído em SECOND STAGE(SECOND TURN): Inter de Santa Maria 0-1 Internacional (1987-05-28)
- jogo só no ogol, incluído em Second Phase: Internacional 1-1 Grêmio (1987-05-31)
- jogo só no ogol, incluído em Second Phase: Juventude 0-1 Inter de Santa Maria (1987-05-31)
- jogo só no ogol, incluído em Second Phase: Grêmio 1-0 Inter de Santa Maria (1987-06-03)
- jogo só no ogol, incluído em Second Phase: Juventude 0-1 Internacional (1987-06-03)
- jogo só no ogol, incluído em Second Phase: Juventude 0-0 Grêmio (1987-06-07)
- jogo só no ogol, incluído em Second Phase: Internacional 3-0 Inter de Santa Maria (1987-06-07)
- jogo só no ogol, incluído em Second Phase: Internacional 4-0 Juventude (1987-06-10)
- jogo só no ogol, incluído em Second Phase: Inter de Santa Maria 0-1 Grêmio (1987-06-10)
- jogo só no ogol, incluído em Second Phase: Inter de Santa Maria 0-2 Juventude (1987-06-13)
- jogo só no ogol, incluído em Second Phase: Grêmio 3-0 Internacional (1987-06-14)
- jogo só no ogol, incluído em CHAMPIONSHIP TOURNAMENT: Grêmio 0-0 Internacional (1987-06-16)
- só na RSSSF (não achado no ogol): Rosário-RS 0-1 14 de Julho (1987-03-15)
- só na RSSSF (não achado no ogol): Uruguaiana 0-0 São Gabriel (1987-04-08)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Cruzeiro-RS (1987-04-08)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 3-0 Rosário-RS (1987-03-22)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Grêmio Santanense (1987-03-22)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 2-0 Grêmio Santanense (1987-03-25)
- só na RSSSF (não achado no ogol): Grêmio Santanense 2-0 Rosário-RS (1987-03-29)
- só na RSSSF (não achado no ogol): São Gabriel 0-0 14 de Julho (1987-03-29)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-1 Uruguaiana (1987-03-29)
- só na RSSSF (não achado no ogol): São Gabriel 2-0 Brasil de Pelotas (1987-04-05)
- só na RSSSF (não achado no ogol): Uruguaiana 2-1 Grêmio Santanense (1987-04-05)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Cruzeiro-RS (1987-04-05)
- só na RSSSF (não achado no ogol): Grêmio Santanense 6-2 Brasil de Pelotas (1987-04-12)
- só na RSSSF (não achado no ogol): Rosário-RS 3-2 São Gabriel (1987-04-12)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-0 Uruguaiana (1987-04-12)
- só na RSSSF (não achado no ogol): São Gabriel 0-0 Cruzeiro-RS (1987-04-15)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Rosário-RS (1987-04-15)
- só na RSSSF (não achado no ogol): Uruguaiana 3-1 14 de Julho (1987-04-16)
- só na RSSSF (não achado no ogol): 14 de Julho 2-2 Brasil de Pelotas (1987-04-19)
- só na RSSSF (não achado no ogol): São Gabriel 0-0 Grêmio Santanense (1987-04-19)
- só na RSSSF (não achado no ogol): Rosário-RS 0-0 Uruguaiana (1987-04-19)
- só na RSSSF (não achado no ogol): Rosário-RS 0-1 Grêmio Santanense (1987-04-26)
- só na RSSSF (não achado no ogol): 14 de Julho 4-0 São Gabriel (1987-04-26)
- só na RSSSF (não achado no ogol): Uruguaiana 2-1 Brasil de Pelotas (1987-04-26)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 São Gabriel (1987-05-03)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-0 14 de Julho (1987-05-03)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Uruguaiana (1987-05-03)
- só na RSSSF (não achado no ogol): Grêmio Santanense 2-0 Cruzeiro-RS (1987-05-06)
- só na RSSSF (não achado no ogol): São Gabriel 2-1 Uruguaiana (1987-05-10)
- só na RSSSF (não achado no ogol): 14 de Julho 4-2 Rosário-RS (1987-05-13)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 3-1 Brasil de Pelotas (1987-05-13)
- só na RSSSF (não achado no ogol): Rosário-RS 0-2 Cruzeiro-RS (1987-05-10)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-0 14 de Julho (1987-05-10)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Grêmio Santanense (1987-05-17)
- só na RSSSF (não achado no ogol): São Gabriel 2-0 Rosário-RS (1987-05-17)
- só na RSSSF (não achado no ogol): Uruguaiana 0-2 Cruzeiro-RS (1987-05-17)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 0-1 São Gabriel (1987-05-20)
- só na RSSSF (não achado no ogol): Rosário-RS 4-1 Brasil de Pelotas (1987-05-20)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 Uruguaiana (1987-05-20)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-2 14 de Julho (1987-05-24)
- só na RSSSF (não achado no ogol): Grêmio Santanense 2-2 São Gabriel (1987-05-24)
- só na RSSSF (não achado no ogol): Uruguaiana 3-1 Rosário-RS (1987-05-24)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-2 Guarany de Bagé (1987-03-15)
- só na RSSSF (não achado no ogol): Bagé 2-0 Rio Grande (1987-03-15)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-0 Bagé (1987-03-22)
- só na RSSSF (não achado no ogol): Rio Grande 0-1 Farroupilha (1987-03-22)
- só na RSSSF (não achado no ogol): Bagé 4-1 Rio-Grandense (1987-03-29)
- só na RSSSF (não achado no ogol): Farroupilha 2-1 Guarany de Bagé (1987-03-29)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-0 Farroupilha (1987-04-05)
- só na RSSSF (não achado no ogol): Guarany de Bagé 3-1 Rio Grande (1987-04-05)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Rio-Grandense (1987-04-11)
- só na RSSSF (não achado no ogol): Farroupilha 1-1 Bagé (1987-04-11)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 Bagé (1987-04-18)
- só na RSSSF (não achado no ogol): Guarany de Bagé 2-0 Rio-Grandense (1987-04-18)
- só na RSSSF (não achado no ogol): Farroupilha 2-0 Rio Grande (1987-04-25)
- só na RSSSF (não achado no ogol): Bagé 0-0 Guarany de Bagé (1987-04-26)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Bagé (1987-05-03)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-0 Farroupilha (1987-05-03)
- só na RSSSF (não achado no ogol): Farroupilha 0-2 Rio-Grandense (1987-05-09)
- só na RSSSF (não achado no ogol): Rio Grande 2-2 Guarany de Bagé (1987-05-10)
- só na RSSSF (não achado no ogol): Bagé 0-0 Farroupilha (1987-05-17)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-1 Rio Grande (1987-05-17)
- só na RSSSF (não achado no ogol): Avenida 3-1 Igrejinha (1987-03-15)
- só na RSSSF (não achado no ogol): Estrela-RS 1-0 Botafogo/FV (1987-03-28)
- só na RSSSF (não achado no ogol): Encantado 2-1 São José-RS (1987-03-29)
- só na RSSSF (não achado no ogol): São José-RS 1-0 Estrela-RS (1987-04-04)
- só na RSSSF (não achado no ogol): Igrejinha 3-2 Encantado (1987-04-05)
- só na RSSSF (não achado no ogol): Botafogo/FV 3-4 Avenida (1987-04-05)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 Encantado (1987-04-08)
- só na RSSSF (não achado no ogol): Igrejinha 1-0 Botafogo/FV (1987-04-08)
- só na RSSSF (não achado no ogol): Avenida 1-0 São José-RS (1987-04-08)
- só na RSSSF (não achado no ogol): São José-RS 0-2 Igrejinha (1987-04-11)
- só na RSSSF (não achado no ogol): Estrela-RS 1-0 Avenida (1987-04-11)
- só na RSSSF (não achado no ogol): Encantado 0-1 Botafogo/FV (1987-04-12)
- só na RSSSF (não achado no ogol): Avenida 2-1 Encantado (1987-04-18)
- só na RSSSF (não achado no ogol): Botafogo/FV 1-1 São José-RS (1987-04-19)
- só na RSSSF (não achado no ogol): Igrejinha 0-0 Estrela-RS (1987-04-19)
- só na RSSSF (não achado no ogol): São José-RS 2-0 Encantado (1987-04-25)
- só na RSSSF (não achado no ogol): Igrejinha 2-2 Avenida (1987-04-26)
- só na RSSSF (não achado no ogol): Botafogo/FV 1-2 Estrela-RS (1987-04-26)
- só na RSSSF (não achado no ogol): Estrela-RS 0-1 São José-RS (1987-05-02)
- só na RSSSF (não achado no ogol): Encantado 0-2 Igrejinha (1987-05-03)
- só na RSSSF (não achado no ogol): Avenida 3-0 Botafogo/FV (1987-05-03)
- só na RSSSF (não achado no ogol): São José-RS 2-1 Avenida (1987-05-09)
- só na RSSSF (não achado no ogol): Encantado 2-1 Estrela-RS (1987-05-10)
- só na RSSSF (não achado no ogol): Botafogo/FV 1-0 Igrejinha (1987-05-10)
- só na RSSSF (não achado no ogol): Avenida 0-0 Estrela-RS (1987-05-16)
- só na RSSSF (não achado no ogol): Botafogo/FV 3-2 Encantado (1987-05-17)
- só na RSSSF (não achado no ogol): Igrejinha 1-1 São José-RS (1987-05-17)
- só na RSSSF (não achado no ogol): São José-RS 3-0 Botafogo/FV (1987-05-23)
- só na RSSSF (não achado no ogol): Estrela-RS 2-0 Igrejinha (1987-05-23)
- só na RSSSF (não achado no ogol): Encantado 0-2 Avenida (1987-05-23)
- só na RSSSF (não achado no ogol): Pradense 1-2 Glória (1987-03-15)
- só na RSSSF (não achado no ogol): Veranense 1-1 Pratense (1987-03-15)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-2 Aimoré (1987-03-15)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Veranense (1987-03-21)
- só na RSSSF (não achado no ogol): Glória 0-0 Brasil de Farroupilha (1987-03-22)
- só na RSSSF (não achado no ogol): Dalban 0-3 Pradense (1987-04-08)
- só na RSSSF (não achado no ogol): Pratense 0-1 Aimoré (1987-03-25)
- só na RSSSF (não achado no ogol): Veranense 1-1 Glória (1987-03-25)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-0 Dalban (1987-04-01)
- só na RSSSF (não achado no ogol): Pradense 2-1 Brasil de Farroupilha (1987-03-29)
- só na RSSSF (não achado no ogol): Glória 5-2 Pratense (1987-03-29)
- só na RSSSF (não achado no ogol): Dalban 2-2 Veranense (1987-03-29)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Glória (1987-04-04)
- só na RSSSF (não achado no ogol): Veranense 0-0 Pradense (1987-04-05)
- só na RSSSF (não achado no ogol): Pratense 1-1 Dalban (1987-04-05)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-1 Veranense (1987-04-12)
- só na RSSSF (não achado no ogol): Dalban 0-0 Aimoré (1987-04-12)
- só na RSSSF (não achado no ogol): Pradense 0-0 Pratense (1987-04-12)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Pradense (1987-04-18)
- só na RSSSF (não achado no ogol): Pratense 2-2 Brasil de Farroupilha (1987-04-19)
- só na RSSSF (não achado no ogol): Glória 4-0 Dalban (1987-04-19)
- só na RSSSF (não achado no ogol): Aimoré 2-0 Brasil de Farroupilha (1987-04-25)
- só na RSSSF (não achado no ogol): Pratense 1-1 Veranense (1987-04-26)
- só na RSSSF (não achado no ogol): Glória 0-0 Pradense (1987-04-26)
- só na RSSSF (não achado no ogol): Pradense 3-1 Dalban (1987-05-03)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-0 Glória (1987-05-03)
- só na RSSSF (não achado no ogol): Veranense 1-0 Aimoré (1987-05-03)
- só na RSSSF (não achado no ogol): Aimoré 2-0 Pratense (1987-05-06)
- só na RSSSF (não achado no ogol): Dalban 2-3 Brasil de Farroupilha (1987-05-06)
- só na RSSSF (não achado no ogol): Glória 3-0 Veranense (1987-05-06)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 3-0 Pradense (1987-05-10)
- só na RSSSF (não achado no ogol): Pratense 0-1 Glória (1987-05-10)
- só na RSSSF (não achado no ogol): Veranense 1-0 Dalban (1987-05-10)
- só na RSSSF (não achado no ogol): Glória 1-1 Aimoré (1987-05-17)
- só na RSSSF (não achado no ogol): Pradense 3-1 Veranense (1987-05-17)
- só na RSSSF (não achado no ogol): Dalban 2-0 Pratense (1987-05-17)
- só na RSSSF (não achado no ogol): Aimoré 3-0 Dalban (1987-05-20)
- só na RSSSF (não achado no ogol): Veranense 0-2 Brasil de Farroupilha (1987-05-20)
- só na RSSSF (não achado no ogol): Pratense 1-0 Pradense (1987-05-20)
- só na RSSSF (não achado no ogol): Dalban 1-0 Glória (1987-05-24)
- só na RSSSF (não achado no ogol): Pradense 1-0 Aimoré (1987-05-24)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha None-None Pratense (1987-05-25)
- só na RSSSF (não achado no ogol): Guarany-RS 3-0 Ypiranga-RS (1987-03-14)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Tabajara Guaíba (1987-04-18)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-1 Gaúcho (1987-04-19)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 1-2 Santa Bárbara-RS (1987-03-22)
- só na RSSSF (não achado no ogol): Gaúcho 0-1 Guarany-RS (1987-03-22)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-0 São Luiz (1987-03-22)
- só na RSSSF (não achado no ogol): São Luiz 1-1 Gaúcho (1987-03-28)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 0-0 Guarany-RS (1987-03-29)
- só na RSSSF (não achado no ogol): Ypiranga-RS 4-1 Tabajara Guaíba (1987-03-29)
- só na RSSSF (não achado no ogol): Gaúcho 0-1 Tabajara Guaíba (1987-04-05)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 São Luiz (1987-04-05)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-1 Ypiranga-RS (1987-04-05)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Santa Bárbara-RS (1987-04-11)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-1 Gaúcho (1987-04-12)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 2-2 Guarany-RS (1987-04-12)
- só na RSSSF (não achado no ogol): Gaúcho 2-0 Santa Bárbara-RS (1987-04-26)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 0-1 São Luiz (1987-04-26)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-1 Guarany-RS (1987-04-26)
- só na RSSSF (não achado no ogol): Guarany-RS 3-0 Gaúcho (1987-05-01)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Ypiranga-RS (1987-05-02)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 2-0 Tabajara Guaíba (1987-05-03)
- só na RSSSF (não achado no ogol): Gaúcho 0-1 São Luiz (1987-05-09)
- só na RSSSF (não achado no ogol): Guarany-RS 3-0 Santa Bárbara-RS (1987-05-10)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 2-2 Ypiranga-RS (1987-05-10)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-0 Santa Bárbara-RS (1987-05-15)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Guarany-RS (1987-05-16)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 1-4 Gaúcho (1987-05-17)
- só na RSSSF (não achado no ogol): Gaúcho 0-3 Ypiranga-RS (1987-05-24)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 3-1 São Luiz (1987-05-24)
- só na RSSSF (não achado no ogol): Guarany-RS 4-0 Tabajara Guaíba (1987-05-24)
- só na RSSSF (não achado no ogol): Santoangelense 0-1 Dínamo (1987-03-15)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-1 Três Passos (1987-03-29)
- só na RSSSF (não achado no ogol): Tupy 0-0 Oriental-RS (1987-03-29)
- só na RSSSF (não achado no ogol): Aurora-RS 1-1 Elite (1987-03-29)
- só na RSSSF (não achado no ogol): Elite 4-0 Botafogo/TM (1987-03-22)
- só na RSSSF (não achado no ogol): Oriental-RS 2-0 Santoangelense (1987-03-22)
- só na RSSSF (não achado no ogol): Três Passos 1-2 Tupy (1987-04-15)
- só na RSSSF (não achado no ogol): Aurora-RS 1-0 Dínamo (1987-04-15)
- só na RSSSF (não achado no ogol): Dínamo 1-0 Oriental-RS (1987-04-01)
- só na RSSSF (não achado no ogol): Três Passos 3-0 Santoangelense (1987-04-01)
- só na RSSSF (não achado no ogol): Elite 3-0 Tupy (1987-04-01)
- só na RSSSF (não achado no ogol): Botafogo/TM 2-0 Aurora-RS (1987-04-22)
- só na RSSSF (não achado no ogol): Três Passos 2-1 Elite (1987-04-05)
- só na RSSSF (não achado no ogol): Tupy 1-1 Dínamo (1987-04-05)
- só na RSSSF (não achado no ogol): Oriental-RS 1-1 Botafogo/TM (1987-04-05)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 Aurora-RS (1987-04-05)
- só na RSSSF (não achado no ogol): Oriental-RS 0-0 Três Passos (1987-04-08)
- só na RSSSF (não achado no ogol): Dínamo 1-1 Elite (1987-04-08)
- só na RSSSF (não achado no ogol): Aurora-RS 1-3 Tupy (1987-04-08)
- só na RSSSF (não achado no ogol): Santoangelense 1-0 Botafogo/TM (1987-04-08)
- só na RSSSF (não achado no ogol): Tupy 1-1 Santoangelense (1987-04-12)
- só na RSSSF (não achado no ogol): Elite 5-1 Oriental-RS (1987-04-12)
- só na RSSSF (não achado no ogol): Botafogo/TM 0-1 Dínamo (1987-04-12)
- só na RSSSF (não achado no ogol): Três Passos 2-1 Aurora-RS (1987-04-12)
- só na RSSSF (não achado no ogol): Tupy 1-1 Botafogo/TM (1987-04-19)
- só na RSSSF (não achado no ogol): Oriental-RS 1-0 Aurora-RS (1987-04-19)
- só na RSSSF (não achado no ogol): Dínamo 0-0 Três Passos (1987-04-19)
- só na RSSSF (não achado no ogol): Santoangelense 2-0 Elite (1987-04-19)
- só na RSSSF (não achado no ogol): Três Passos 1-0 Oriental-RS (1987-04-26)
- só na RSSSF (não achado no ogol): Elite 5-0 Dínamo (1987-04-26)
- só na RSSSF (não achado no ogol): Botafogo/TM 0-0 Santoangelense (1987-04-26)
- só na RSSSF (não achado no ogol): Tupy 4-0 Aurora-RS (1987-04-26)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 Tupy (1987-05-03)
- só na RSSSF (não achado no ogol): Oriental-RS 0-0 Elite (1987-05-03)
- só na RSSSF (não achado no ogol): Dínamo 4-1 Botafogo/TM (1987-05-03)
- só na RSSSF (não achado no ogol): Aurora-RS 3-2 Três Passos (1987-05-03)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-3 Tupy (1987-05-10)
- só na RSSSF (não achado no ogol): Aurora-RS 0-0 Oriental-RS (1987-05-10)
- só na RSSSF (não achado no ogol): Três Passos 3-1 Dínamo (1987-05-10)
- só na RSSSF (não achado no ogol): Elite 0-0 Santoangelense (1987-05-10)
- só na RSSSF (não achado no ogol): Botafogo/TM 3-3 Elite (1987-05-13)
- só na RSSSF (não achado no ogol): Santoangelense 0-0 Oriental-RS (1987-05-13)
- só na RSSSF (não achado no ogol): Tupy 2-2 Três Passos (1987-05-13)
- só na RSSSF (não achado no ogol): Dínamo 4-0 Aurora-RS (1987-05-13)
- só na RSSSF (não achado no ogol): Dínamo 1-1 Santoangelense (1987-05-17)
- só na RSSSF (não achado no ogol): Três Passos 2-1 Botafogo/TM (1987-05-17)
- só na RSSSF (não achado no ogol): Oriental-RS 1-2 Tupy (1987-05-17)
- só na RSSSF (não achado no ogol): Elite 4-0 Aurora-RS (1987-05-17)
- só na RSSSF (não achado no ogol): Oriental-RS 0-0 Dínamo (1987-05-20)
- só na RSSSF (não achado no ogol): Tupy 0-1 Elite (1987-05-20)
- só na RSSSF (não achado no ogol): Aurora-RS 2-2 Botafogo/TM (1987-05-20)
- só na RSSSF (não achado no ogol): Santoangelense 1-2 Três Passos (1987-05-20)
- só na RSSSF (não achado no ogol): Elite 1-0 Três Passos (1987-05-24)
- só na RSSSF (não achado no ogol): Dínamo 4-0 Tupy (1987-05-24)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-2 Oriental-RS (1987-05-24)
- só na RSSSF (não achado no ogol): Aurora-RS 0-2 Santoangelense (1987-05-24)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 4-1 Grêmio Santanense (1987-05-31)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 São Gabriel (1987-05-31)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-0 14 de Julho (1987-06-07)
- só na RSSSF (não achado no ogol): São Gabriel 0-1 Cruzeiro-RS (1987-06-07)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 São Gabriel (1987-06-14)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 0-1 14 de Julho (1987-06-14)
- só na RSSSF (não achado no ogol): São Gabriel 2-2 Grêmio Santanense (1987-06-21)
- só na RSSSF (não achado no ogol): 14 de Julho 1-2 Cruzeiro-RS (1987-06-21)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-0 São Gabriel (1987-06-27)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Grêmio Santanense (1987-06-28)
- só na RSSSF (não achado no ogol): São Gabriel 1-1 14 de Julho (1987-07-05)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Cruzeiro-RS (1987-07-05)
- só na RSSSF (não achado no ogol): Rio-Grandense 2-2 Guarany de Bagé (1987-05-31)
- só na RSSSF (não achado no ogol): Bagé 1-1 Farroupilha (1987-05-31)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-0 Bagé (1987-06-07)
- só na RSSSF (não achado no ogol): Farroupilha 1-1 Rio-Grandense (1987-06-07)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-0 Farroupilha (1987-06-14)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-2 Bagé (1987-06-14)
- só na RSSSF (não achado no ogol): Farroupilha 0-2 Guarany de Bagé (1987-06-20)
- só na RSSSF (não achado no ogol): Bagé 4-0 Rio-Grandense (1987-06-21)
- só na RSSSF (não achado no ogol): Bagé 1-0 Guarany de Bagé (1987-06-28)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-2 Farroupilha (1987-06-28)
- só na RSSSF (não achado no ogol): Farroupilha 1-3 Bagé (1987-07-05)
- só na RSSSF (não achado no ogol): Guarany de Bagé 4-0 Rio-Grandense (1987-07-05)
- só na RSSSF (não achado no ogol): São José-RS 0-0 Estrela-RS (1987-05-30)
- só na RSSSF (não achado no ogol): Avenida 2-4 Igrejinha (1987-05-31)
- só na RSSSF (não achado no ogol): Estrela-RS 1-0 Avenida (1987-06-07)
- só na RSSSF (não achado no ogol): Igrejinha 1-0 São José-RS (1987-06-07)
- só na RSSSF (não achado no ogol): São José-RS 0-0 Avenida (1987-06-13)
- só na RSSSF (não achado no ogol): Igrejinha 1-0 Estrela-RS (1987-06-14)
- só na RSSSF (não achado no ogol): Avenida 2-1 São José-RS (1987-06-20)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 Igrejinha (1987-06-21)
- só na RSSSF (não achado no ogol): São José-RS 2-1 Igrejinha (1987-06-27)
- só na RSSSF (não achado no ogol): Avenida 0-0 Estrela-RS (1987-06-28)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 São José-RS (1987-07-05)
- só na RSSSF (não achado no ogol): Igrejinha 1-0 Avenida (1987-07-05)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-0 Aimoré (1987-05-31)
- só na RSSSF (não achado no ogol): Glória 0-1 Pradense (1987-05-31)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Glória (1987-06-06)
- só na RSSSF (não achado no ogol): Pradense 1-3 Brasil de Farroupilha (1987-06-07)
- só na RSSSF (não achado no ogol): Aimoré 3-0 Pradense (1987-06-13)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-0 Glória (1987-06-14)
- só na RSSSF (não achado no ogol): Pradense 1-0 Aimoré (1987-06-21)
- só na RSSSF (não achado no ogol): Glória 2-0 Brasil de Farroupilha (1987-06-21)
- só na RSSSF (não achado no ogol): Glória 0-1 Aimoré (1987-06-28)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-0 Pradense (1987-06-28)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Brasil de Farroupilha (1987-07-05)
- só na RSSSF (não achado no ogol): Pradense 0-0 Glória (1987-07-05)
- só na RSSSF (não achado no ogol): São Luiz 1-2 Guarany-RS (1987-05-30)
- só na RSSSF (não achado no ogol): Gaúcho 1-0 Ypiranga-RS (1987-05-31)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 São Luiz (1987-06-07)
- só na RSSSF (não achado no ogol): Guarany-RS 2-1 Gaúcho (1987-06-07)
- só na RSSSF (não achado no ogol): São Luiz 2-0 Gaúcho (1987-06-13)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-1 Guarany-RS (1987-06-14)
- só na RSSSF (não achado no ogol): Gaúcho 0-0 São Luiz (1987-06-21)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Ypiranga-RS (1987-06-21)
- só na RSSSF (não achado no ogol): São Luiz 2-0 Ypiranga-RS (1987-06-27)
- só na RSSSF (não achado no ogol): Gaúcho 0-1 Guarany-RS (1987-06-27)
- só na RSSSF (não achado no ogol): Guarany-RS 0-1 São Luiz (1987-07-05)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Gaúcho (1987-07-05)
- só na RSSSF (não achado no ogol): Elite 1-0 Dínamo (1987-05-31)
- só na RSSSF (não achado no ogol): Tupy 1-0 Três Passos (1987-05-31)
- só na RSSSF (não achado no ogol): Três Passos 1-1 Elite (1987-06-06)
- só na RSSSF (não achado no ogol): Dínamo 2-1 Tupy (1987-06-07)
- só na RSSSF (não achado no ogol): Dínamo 2-1 Três Passos (1987-06-14)
- só na RSSSF (não achado no ogol): Elite 0-1 Tupy (1987-06-14)
- só na RSSSF (não achado no ogol): Três Passos 0-1 Dínamo (1987-06-21)
- só na RSSSF (não achado no ogol): Tupy 2-1 Elite (1987-06-21)
- só na RSSSF (não achado no ogol): Elite 5-0 Três Passos (1987-06-27)
- só na RSSSF (não achado no ogol): Tupy 1-0 Dínamo (1987-06-28)
- só na RSSSF (não achado no ogol): Três Passos 0-0 Tupy (1987-07-05)
- só na RSSSF (não achado no ogol): Dínamo 1-0 Elite (1987-07-05)
- só na RSSSF (não achado no ogol): Rosário-RS 2-1 Uruguaiana (1987-05-31)
- só na RSSSF (não achado no ogol): Uruguaiana 1-1 Rio Grande (1987-06-07)
- só na RSSSF (não achado no ogol): Rio Grande None-None Rosário-RS (1987-06-13)
- só na RSSSF (não achado no ogol): Uruguaiana 3-0 Rosário-RS (1987-06-13)
- só na RSSSF (não achado no ogol): Rio Grande 0-1 Uruguaiana (1987-06-27)
- só na RSSSF (não achado no ogol): Rosário-RS 0-1 Rio Grande (1987-08-30)
- só na RSSSF (não achado no ogol): Pratense 1-0 Encantado (1987-05-31)
- só na RSSSF (não achado no ogol): Dalban 2-2 Botafogo/FV (1987-05-31)
- só na RSSSF (não achado no ogol): Encantado 1-1 Dalban (1987-06-07)
- só na RSSSF (não achado no ogol): Veranense 2-1 Pratense (1987-06-07)
- só na RSSSF (não achado no ogol): Botafogo/FV 0-0 Encantado (1987-06-14)
- só na RSSSF (não achado no ogol): Dalban 0-0 Veranense (1987-06-14)
- só na RSSSF (não achado no ogol): Veranense 1-1 Botafogo/FV (1987-06-17)
- só na RSSSF (não achado no ogol): Pratense 1-2 Dalban (1987-06-18)
- só na RSSSF (não achado no ogol): Encantado 2-1 Veranense (1987-06-21)
- só na RSSSF (não achado no ogol): Botafogo/FV 1-3 Pratense (1987-06-21)
- só na RSSSF (não achado no ogol): Encantado 3-0 Pratense (1987-06-27)
- só na RSSSF (não achado no ogol): Botafogo/FV 2-0 Dalban (1987-06-28)
- só na RSSSF (não achado no ogol): Dalban 3-1 Encantado (1987-07-01)
- só na RSSSF (não achado no ogol): Pratense 3-0 Veranense (1987-07-01)
- só na RSSSF (não achado no ogol): Encantado 6-0 Botafogo/FV (1987-07-05)
- só na RSSSF (não achado no ogol): Veranense None-None Dalban (1987-07-05)
- só na RSSSF (não achado no ogol): Dalban 0-0 Pratense (1987-07-12)
- só na RSSSF (não achado no ogol): Botafogo/FV 2-3 Veranense (1987-07-12)
- só na RSSSF (não achado no ogol): Veranense 1-0 Encantado (1987-07-15)
- só na RSSSF (não achado no ogol): Pratense 2-0 Botafogo/FV (1987-07-15)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 1-0 Santa Bárbara-RS (1987-05-31)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-1 Oriental-RS (1987-05-31)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-2 Botafogo/TM (1987-06-07)
- só na RSSSF (não achado no ogol): Oriental-RS 1-0 Tabajara Guaíba (1987-06-07)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-1 Oriental-RS (1987-06-14)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-1 Tabajara Guaíba (1987-06-14)
- só na RSSSF (não achado no ogol): Oriental-RS 1-0 Santa Bárbara-RS (1987-06-21)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 0-0 Botafogo/TM (1987-06-21)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 4-3 Oriental-RS (1987-06-27)
- só na RSSSF (não achado no ogol): Botafogo/TM 1-0 Santa Bárbara-RS (1987-06-28)
- só na RSSSF (não achado no ogol): Santa Bárbara-RS 1-4 Tabajara Guaíba (1987-07-05)
- só na RSSSF (não achado no ogol): Oriental-RS 0-0 Botafogo/TM (1987-07-05)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 2-2 Veranense (1987-07-26)
- só na RSSSF (não achado no ogol): Uruguaiana 2-0 Tabajara Guaíba (1987-09-02)
- só na RSSSF (não achado no ogol): Veranense 1-0 Uruguaiana (1987-09-05)
- só na RSSSF (não achado no ogol): Uruguaiana 2-2 Veranense (1987-09-07)
- só na RSSSF (não achado no ogol): Veranense 2-2 Tabajara Guaíba (1987-09-10)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 2-1 Uruguaiana (1987-09-13)
- só na RSSSF (não achado no ogol): Guarany de Bagé 5-0 14 de Julho (1987-07-19)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 2-1 Bagé (1987-07-19)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 Cruzeiro-RS (1987-07-26)
- só na RSSSF (não achado no ogol): Bagé 0-0 Guarany de Bagé (1987-07-26)
- só na RSSSF (não achado no ogol): Bagé 1-0 14 de Julho (1987-08-02)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-1 Guarany de Bagé (1987-08-02)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Bagé (1987-08-16)
- só na RSSSF (não achado no ogol): Guarany de Bagé 4-0 Cruzeiro-RS (1987-08-16)
- só na RSSSF (não achado no ogol): Cruzeiro-RS 1-0 14 de Julho (1987-08-23)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-0 Bagé (1987-08-23)
- só na RSSSF (não achado no ogol): 14 de Julho 3-1 Guarany de Bagé (1987-08-30)
- só na RSSSF (não achado no ogol): Bagé 3-0 Cruzeiro-RS (1987-08-30)
- só na RSSSF (não achado no ogol): Igrejinha 2-1 Aimoré (1987-07-19)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-2 Estrela-RS (1987-07-19)
- só na RSSSF (não achado no ogol): Estrela-RS 0-0 Igrejinha (1987-07-26)
- só na RSSSF (não achado no ogol): Aimoré 3-0 Brasil de Farroupilha (1987-07-26)
- só na RSSSF (não achado no ogol): Aimoré 0-1 Estrela-RS (1987-08-02)
- só na RSSSF (não achado no ogol): Igrejinha 0-1 Brasil de Farroupilha (1987-08-02)
- só na RSSSF (não achado no ogol): Estrela-RS 1-2 Aimoré (1987-08-16)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-1 Igrejinha (1987-08-16)
- só na RSSSF (não achado no ogol): Igrejinha 1-0 Estrela-RS (1987-08-23)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-0 Aimoré (1987-08-23)
- só na RSSSF (não achado no ogol): Aimoré 3-0 Igrejinha (1987-08-30)
- só na RSSSF (não achado no ogol): Estrela-RS 1-1 Brasil de Farroupilha (1987-08-30)
- só na RSSSF (não achado no ogol): São Luiz 3-1 Tupy (1987-07-18)
- só na RSSSF (não achado no ogol): Dínamo 1-0 Guarany-RS (1987-07-19)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 São Luiz (1987-07-26)
- só na RSSSF (não achado no ogol): Tupy 0-1 Dínamo (1987-07-26)
- só na RSSSF (não achado no ogol): Guarany-RS 2-0 Tupy (1987-08-02)
- só na RSSSF (não achado no ogol): Dínamo 2-0 São Luiz (1987-08-02)
- só na RSSSF (não achado no ogol): São Luiz 1-1 Dínamo (1987-08-15)
- só na RSSSF (não achado no ogol): Tupy 2-2 Guarany-RS (1987-08-16)
- só na RSSSF (não achado no ogol): São Luiz 1-1 Guarany-RS (1987-08-22)
- só na RSSSF (não achado no ogol): Dínamo 3-0 Tupy (1987-08-23)
- só na RSSSF (não achado no ogol): Tupy 0-2 São Luiz (1987-08-30)
- só na RSSSF (não achado no ogol): Guarany-RS 4-1 Dínamo (1987-08-30)
- só na RSSSF (não achado no ogol): Grêmio Santanense 2-1 São Gabriel (1987-07-12)
- só na RSSSF (não achado no ogol): São Gabriel 4-1 Grêmio Santanense (1987-07-19)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-0 São Gabriel (1987-07-26)
- só na RSSSF (não achado no ogol): São Gabriel 1-1 Rio-Grandense (1987-08-02)
- só na RSSSF (não achado no ogol): São José-RS 3-3 Avenida (1987-07-11)
- só na RSSSF (não achado no ogol): Avenida 1-1 São José-RS (1987-07-18)
- só na RSSSF (não achado no ogol): Glória 1-0 Pradense (1987-07-12)
- só na RSSSF (não achado no ogol): Pradense 1-1 Glória (1987-07-19)
- só na RSSSF (não achado no ogol): Avenida 1-0 Glória (1987-07-26)
- só na RSSSF (não achado no ogol): Glória 2-1 Avenida (None)
- só na RSSSF (não achado no ogol): Três Passos 1-3 Elite (1987-07-12)
- só na RSSSF (não achado no ogol): Elite 2-0 Três Passos (1987-07-18)
- só na RSSSF (não achado no ogol): Elite 1-0 Ypiranga-RS (1987-07-26)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-1 Elite (1987-08-02)
- só na RSSSF (não achado no ogol): Elite 1-1 Glória (1987-08-09)
- só na RSSSF (não achado no ogol): Glória 0-1 Rio-Grandense (1987-08-16)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Elite (1987-08-23)
- só na RSSSF (não achado no ogol): Elite 2-1 Veranense (1987-09-16)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 0-0 Rio-Grandense (1987-09-17)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Elite (1987-09-20)
- só na RSSSF (não achado no ogol): Veranense 2-1 Tabajara Guaíba (1987-09-20)
- só na RSSSF (não achado no ogol): Tabajara Guaíba 1-1 Elite (1987-09-23)
- só na RSSSF (não achado no ogol): Veranense 0-2 Rio-Grandense (1987-09-23)
- só na RSSSF (não achado no ogol): Elite 1-1 Tabajara Guaíba (1987-09-27)
- só na RSSSF (não achado no ogol): Rio-Grandense 2-1 Veranense (1987-09-27)
- só na RSSSF (não achado no ogol): Veranense 2-2 Elite (1987-09-30)
- só na RSSSF (não achado no ogol): Rio-Grandense 3-3 Tabajara Guaíba (1987-10-01)
- só na RSSSF (não achado no ogol): Elite 3-0 Rio-Grandense (1987-10-04)
- só na RSSSF (não achado no ogol): Tabajara Guaíba None-None Veranense (1987-10-04)
- só na RSSSF (não achado no ogol): Dínamo 0-0 Aimoré (1987-09-13)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-2 Guarany-RS (1987-09-13)
- só na RSSSF (não achado no ogol): Igrejinha 0-0 14 de Julho (1987-09-16)
- só na RSSSF (não achado no ogol): Elite 2-0 Rio-Grandense (1987-10-21)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Guarany de Bagé (1987-09-19)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 Dínamo (1987-09-20)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-2 Igrejinha (1987-10-28)
- só na RSSSF (não achado no ogol): Guarany-RS 1-1 Elite (1987-10-28)
- só na RSSSF (não achado no ogol): Guarany de Bagé 2-0 14 de Julho (1987-09-26)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Igrejinha (1987-09-27)
- só na RSSSF (não achado no ogol): Elite 1-1 Aimoré (1987-11-17)
- só na RSSSF (não achado no ogol): Dínamo 2-0 Rio-Grandense (1987-11-18)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Guarany-RS (1987-10-04)
- só na RSSSF (não achado no ogol): Igrejinha 0-0 Dínamo (1987-10-04)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-0 Elite (1987-11-11)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-0 14 de Julho (1987-11-11)
- só na RSSSF (não achado no ogol): Igrejinha 1-1 Elite (1987-10-10)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-2 Guarany-RS (1987-10-10)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 Aimoré (1987-10-11)
- só na RSSSF (não achado no ogol): Dínamo 1-0 Guarany de Bagé (1987-10-11)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 Dínamo (1987-10-14)
- só na RSSSF (não achado no ogol): Guarany de Bagé 3-1 Rio-Grandense (1987-10-14)
- só na RSSSF (não achado no ogol): Elite 0-0 14 de Julho (1987-10-14)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Igrejinha (1987-10-15)
- só na RSSSF (não achado no ogol): 14 de Julho 0-1 Guarany-RS (1987-10-18)
- só na RSSSF (não achado no ogol): Igrejinha 1-1 Guarany de Bagé (1987-10-18)
- só na RSSSF (não achado no ogol): Dínamo 1-1 Elite (1987-10-18)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Aimoré (1987-10-18)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Dínamo (1987-10-25)
- só na RSSSF (não achado no ogol): Guarany-RS 1-1 Guarany de Bagé (1987-10-25)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-1 Elite (1987-10-25)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Igrejinha (1987-10-25)
- só na RSSSF (não achado no ogol): Guarany de Bagé 1-1 Aimoré (1987-11-01)
- só na RSSSF (não achado no ogol): Dínamo 1-3 14 de Julho (1987-11-01)
- só na RSSSF (não achado no ogol): Igrejinha 0-1 Rio-Grandense (1987-11-01)
- só na RSSSF (não achado no ogol): Elite 3-0 Guarany-RS (1987-11-01)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Elite (1987-11-06)
- só na RSSSF (não achado no ogol): Igrejinha 1-1 Guarany-RS (1987-11-07)
- só na RSSSF (não achado no ogol): 14 de Julho 1-0 Guarany de Bagé (1987-11-08)
- só na RSSSF (não achado no ogol): Rio-Grandense 1-1 Dínamo (1987-11-08)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Aimoré (1987-11-15)
- só na RSSSF (não achado no ogol): Dínamo 1-0 Igrejinha (1987-11-15)
- só na RSSSF (não achado no ogol): Elite 1-2 Guarany de Bagé (1987-11-15)
- só na RSSSF (não achado no ogol): 14 de Julho 3-0 Rio-Grandense (1987-11-15)
- só na RSSSF (não achado no ogol): Aimoré 1-0 14 de Julho (1987-11-22)
- só na RSSSF (não achado no ogol): Guarany de Bagé 0-1 Dínamo (1987-11-22)
- só na RSSSF (não achado no ogol): Elite 3-0 Igrejinha (1987-11-22)
- só na RSSSF (não achado no ogol): Guarany-RS 2-0 Rio-Grandense (1987-11-22)
- só na RSSSF (não achado no ogol): Igrejinha 0-2 Aimoré (1987-11-25)
- só na RSSSF (não achado no ogol): Dínamo 0-0 Guarany-RS (1987-11-25)
- só na RSSSF (não achado no ogol): Rio-Grandense 0-0 Guarany de Bagé (1987-11-25)
- só na RSSSF (não achado no ogol): 14 de Julho 3-0 Elite (1987-11-25)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 14 de Julho (1987-11-29)
- só na RSSSF (não achado no ogol): Guarany de Bagé None-None Igrejinha (1987-11-29)
- só na RSSSF (não achado no ogol): Elite 0-1 Dínamo (1987-11-29)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Rio-Grandense (1987-11-29)
- só na RSSSF (não achado no ogol): Aimoré 1-2 Guarany-RS (1987-12-04)
- só na RSSSF (não achado no ogol): Guarany-RS 2-1 Aimoré (1987-12-07)
- vencedor da final pelos jogos (Elite) diferente do campeão oficial (Grêmio); fica o oficial

### 1988

- tabela publicada x jogos — 1º Turno / -: Aimoré tabela [7, 3, 2, 2, 8, 6] jogos [7, 3, 2, 2, 8, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Guarany-RS tabela [7, 2, 2, 3, 10, 13] jogos [7, 2, 2, 3, 10, 15] — placar diverge entre RSSSF e ogol em Santa Cruz-RS x Guarany-RS (5-1 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Santa Cruz-RS tabela [7, 3, 3, 1, 9, 6] jogos [7, 3, 3, 1, 11, 6] — placar diverge entre RSSSF e ogol em Santa Cruz-RS x Guarany-RS (5-1 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / GRUPO A: Juventude tabela [6, 2, 2, 2, 5, 7] jogos [6, 2, 2, 2, 5, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Grêmio tabela [13, 9, 2, 2, 28, 10] jogos [17, 13, 2, 2, 36, 12] — a tabela conta 13 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [13, 7, 4, 2, 17, 14] jogos [15, 7, 5, 3, 19, 17] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [13, 5, 6, 2, 13, 9] jogos [14, 5, 6, 3, 15, 12] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Inter de Santa Maria tabela [13, 5, 5, 3, 10, 4] jogos [14, 4, 4, 6, 9, 10] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Juventude tabela [13, 4, 7, 2, 14, 14] jogos [14, 4, 8, 2, 15, 16] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Pelotas tabela [13, 4, 6, 3, 10, 8] jogos [14, 4, 6, 4, 10, 10] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Aimoré tabela [13, 4, 6, 3, 12, 10] jogos [13, 4, 6, 3, 12, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarany-RS tabela [13, 3, 6, 4, 15, 18] jogos [13, 3, 6, 4, 15, 20] — placar diverge entre RSSSF e ogol em Santa Cruz-RS x Guarany-RS (5-1 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Grêmio tabela [10, 4, 5, 1, 12, 7] jogos [13, 6, 6, 1, 17, 9] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Caxias tabela [10, 0, 6, 4, 3, 9] jogos [12, 0, 7, 5, 4, 11] — a tabela conta 10 jogos e as fontes trazem 12
- placar diferente no ogol — Santa Cruz-RS x Guarany-RS (1988-03-06): RSSSF 5-1, ogol 3-1; fica o da RSSSF
- mando invertido no ogol — RSSSF Pelotas 2-0 Brasil de Pelotas, ogol Brasil de Pelotas 0-2 Pelotas (1988-03-06); fica a RSSSF
- só na RSSSF (não achado no ogol): Aimoré 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 2-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 0-4 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-2 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-1 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 0-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 3-2 Lajeadense (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 0-0 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-1 Lajeadense (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Aimoré 3-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Guarany-RS 2-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Lajeadense 4-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 4-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-1 Lajeadense (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 1-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 3-2 Aimoré (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 3-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Aimoré 2-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Guarany-RS 3-2 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Aimoré 2-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 0-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Caxias 0-0 Grêmio (None)

### 1989

- tabela publicada x jogos — Primeira fase / -: Internacional tabela [7, 3, 1, 3, 0, 9] jogos [27, 14, 8, 5, 41, 19] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [7, 4, 3, 0, 0, 9] jogos [29, 12, 8, 9, 35, 31] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [7, 1, 3, 3, 1, 4] jogos [27, 8, 11, 8, 23, 33] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Inter de Santa Maria tabela [7, 1, 4, 2, 0, 6] jogos [27, 6, 8, 13, 22, 33] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: São Paulo-RS tabela [7, 1, 5, 1, 0, 5] jogos [27, 4, 8, 15, 13, 38] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Lajeadense tabela [7, 5, 0, 2, 5, 15] jogos [27, 5, 9, 13, 24, 39] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Grêmio tabela [13, 7, 4, 2, 0, 1] jogos [26, 14, 9, 3, 45, 20] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [12, 7, 3, 2, 0, 2] jogos [28, 10, 11, 7, 27, 18] — a tabela conta 12 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Novo Hamburgo tabela [7, 3, 3, 1, 0, 10] jogos [27, 7, 10, 10, 26, 26] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Quadrangular First Stage Standings / -: Internacional tabela [3, 2, 0, 1, 0, 5] jogos [27, 14, 8, 5, 41, 19] — a tabela conta 3 jogos e as fontes trazem 27
- tabela publicada x jogos — Quadrangular First Stage Standings / -: Passo Fundo tabela [3, 1, 2, 0, 0, 3] jogos [26, 7, 10, 9, 29, 33] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Quadrangular First Stage Standings / -: Glória tabela [3, 1, 1, 1, 1, 2] jogos [26, 7, 13, 6, 27, 26] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Aimoré tabela [6, 3, 1, 2, 0, 6] jogos [30, 7, 14, 9, 15, 23] — a tabela conta 6 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / Grupo A: Internacional tabela [6, 3, 3, 0, 0, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Lajeadense tabela [6, 1, 4, 1, 0, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: São Paulo-RS tabela [6, 5, 0, 1, 1, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / -: Juventude tabela [9, 6, 1, 2, 3, 0] jogos [27, 12, 9, 6, 42, 27] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Segunda fase / -: Novo Hamburgo tabela [6, 4, 1, 1, 4, 9] jogos [27, 7, 10, 10, 26, 26] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — QUADRANGULAR SECOND STAGE STANDINGS / -: Grêmio tabela [3, 1, 0, 2, 0, 2] jogos [26, 14, 9, 3, 45, 20] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — QUADRANGULAR SECOND STAGE STANDINGS / -: Pelotas tabela [5, 3, 1, 1, 1, 0] jogos [26, 9, 8, 9, 25, 28] — a tabela conta 5 jogos e as fontes trazem 26
- tabela publicada x jogos — QUADRANGULAR SECOND STAGE STANDINGS / -: Aimoré tabela [3, 2, 0, 1, 0, 3] jogos [30, 7, 14, 9, 15, 23] — a tabela conta 3 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Caxias tabela [13, 8, 5, 0, 0, 17] jogos [29, 12, 8, 9, 35, 31] — a tabela conta 13 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [13, 6, 4, 3, 0, 19] jogos [27, 6, 8, 13, 22, 33] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase final / -: Esportivo-RS tabela [20, 13, 4, 3, 2, 4] jogos [28, 10, 11, 7, 27, 18] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — Torneio de rebaixamento / -: Novo Hamburgo tabela [22, 14, 4, 4, 4, 1] jogos [27, 7, 10, 10, 26, 26] — a tabela conta 22 jogos e as fontes trazem 27
- tabela publicada x jogos — Torneio de rebaixamento / -: Santa Cruz-RS tabela [21, 14, 4, 3, 4, 2] jogos [27, 8, 11, 8, 23, 33] — a tabela conta 21 jogos e as fontes trazem 27
- tabela publicada x jogos — Torneio de rebaixamento / -: Aimoré tabela [20, 14, 3, 3, 5, 3] jogos [30, 7, 14, 9, 15, 23] — a tabela conta 20 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Passo Fundo tabela [10, 5, 2, 3, 7, 17] jogos [26, 7, 10, 9, 29, 33] — a tabela conta 10 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase final / -: Santa Cruz-RS tabela [42, 27, 8, 7, 7, 4] jogos [27, 8, 11, 8, 23, 33] — a tabela conta 42 jogos e as fontes trazem 27
- placar diferente no ogol — Novo Hamburgo x Lajeadense (1989-03-01): RSSSF 4-0, ogol 4-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Esportivo-RS x Internacional, ogol 1989-03-07); fica a do ogol
- jogo só no ogol, incluído em FIRST STAGE: Passo Fundo 1-1 Aimoré (1989-03-01)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Internacional (1989-03-07)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-2 Juventude (1989-05-17)
- só na RSSSF (não achado no ogol): Juventude 2-0 Aimoré (1989-05-21)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 Novo Hamburgo (1989-05-14)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-1 Santa Cruz-RS (1989-05-21)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Esportivo-RS (1989-05-14)
- só na RSSSF (não achado no ogol): Novo Hamburgo 4-1 Inter de Santa Maria (1989-05-21)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 São Paulo-RS (1989-05-14)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Lajeadense (1989-05-21)
- só na RSSSF (não achado no ogol): Juventude 2-0 Novo Hamburgo (1989-05-28)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-4 Juventude (1989-06-04)
- só na RSSSF (não achado no ogol): Aimoré 1-0 São Paulo-RS (1989-05-27)
- só na RSSSF (não achado no ogol): Novo Hamburgo 1-0 Esportivo-RS (1989-06-03)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-2 Lajeadense (1989-05-28)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 3-1 Aimoré (1989-06-04)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-3 Esportivo-RS (1989-05-28)
- só na RSSSF (não achado no ogol): Lajeadense 3-0 Santa Cruz-RS (1989-06-04)
- só na RSSSF (não achado no ogol): Lajeadense 2-3 Juventude (1989-06-11)
- só na RSSSF (não achado no ogol): Juventude 2-1 Santa Cruz-RS (1989-06-17)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Novo Hamburgo (1989-06-10)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-1 Esportivo-RS (1989-06-17)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-0 Inter de Santa Maria (1989-06-11)
- só na RSSSF (não achado no ogol): Novo Hamburgo 3-0 São Paulo-RS (1989-06-18)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-0 São Paulo-RS (1989-06-11)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Lajeadense (1989-06-17)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Juventude (1989-06-25)
- só na RSSSF (não achado no ogol): Juventude 5-0 Inter de Santa Maria (1989-07-02)
- só na RSSSF (não achado no ogol): São Paulo-RS 0-0 Inter de Santa Maria (1989-06-25)
- só na RSSSF (não achado no ogol): Novo Hamburgo 1-1 Santa Cruz-RS (1989-07-02)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Novo Hamburgo (1989-06-25)
- só na RSSSF (não achado no ogol): Esportivo-RS 0-0 Aimoré (1989-07-02)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-0 Aimoré (1989-06-25)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-0 Lajeadense (1989-07-02)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Juventude (1989-07-09)
- só na RSSSF (não achado no ogol): Novo Hamburgo 0-2 Juventude (1989-07-16)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 São Paulo-RS (1989-07-09)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Santa Cruz-RS (1989-07-15)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-1 Novo Hamburgo (1989-07-09)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-0 Aimoré (1989-07-16)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Esportivo-RS (1989-07-09)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 Inter de Santa Maria (1989-07-16)
- só na RSSSF (não achado no ogol): Juventude 0-0 São Paulo-RS (1989-07-22)
- só na RSSSF (não achado no ogol): Juventude 0-0 Lajeadense (1989-07-30)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Inter de Santa Maria (1989-07-22)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-0 Esportivo-RS (1989-07-29)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 4-2 Lajeadense (1989-07-23)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 3-0 Santa Cruz-RS (1989-07-29)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Novo Hamburgo (1989-07-23)
- só na RSSSF (não achado no ogol): Novo Hamburgo 0-0 Aimoré (1989-07-30)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-0 Juventude (1989-08-06)
- só na RSSSF (não achado no ogol): Juventude 1-0 Esportivo-RS (1989-08-12)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Inter de Santa Maria (1989-08-05)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-1 São Paulo-RS (1989-08-13)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-2 Novo Hamburgo (1989-08-06)
- só na RSSSF (não achado no ogol): Novo Hamburgo 0-0 Lajeadense (1989-08-13)
- só na RSSSF (não achado no ogol): Lajeadense 3-0 Aimoré (1989-08-06)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Santa Cruz-RS (1989-08-13)
- vencedor da final pelos jogos (Juventude) diferente do campeão oficial (Grêmio); fica o oficial

### 1990

- tabela publicada x jogos — Fase final / -: Grêmio tabela [13, 9, 3, 1, 28, 6] jogos [32, 18, 9, 5, 62, 23] — a tabela conta 13 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase classificatória / -: Ypiranga-RS tabela [13, 5, 3, 5, 19, 17] jogos [14, 5, 4, 5, 20, 18] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase classificatória / -: Santa Cruz-RS tabela [13, 2, 7, 4, 12, 15] jogos [13, 3, 6, 4, 12, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / -: Aimoré tabela [13, 0, 8, 5, 7, 13] jogos [14, 0, 9, 5, 8, 14] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Caxias tabela [13, 7, 4, 2, 22, 13] jogos [33, 15, 14, 4, 43, 29] — a tabela conta 13 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase classificatória / -: Grêmio tabela [13, 6, 4, 3, 22, 10] jogos [32, 18, 9, 5, 62, 23] — a tabela conta 13 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase classificatória / -: Pelotas tabela [13, 5, 5, 3, 16, 11] jogos [27, 9, 11, 7, 29, 23] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase classificatória / -: Guarany-RS tabela [13, 5, 5, 3, 13, 10] jogos [27, 9, 10, 8, 23, 24] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase classificatória / -: Ypiranga-RS tabela [13, 4, 7, 2, 15, 11] jogos [28, 9, 11, 8, 35, 30] — a tabela conta 13 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase classificatória / -: Santa Cruz-RS tabela [13, 4, 7, 2, 10, 10] jogos [26, 7, 13, 6, 22, 24] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Glória tabela [13, 4, 6, 3, 10, 13] jogos [26, 7, 10, 9, 22, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Juventude tabela [13, 5, 3, 5, 10, 11] jogos [34, 11, 12, 11, 33, 34] — a tabela conta 13 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase classificatória / -: Internacional tabela [13, 4, 5, 4, 12, 8] jogos [32, 12, 12, 8, 32, 20] — a tabela conta 13 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase classificatória / -: Esportivo-RS tabela [13, 4, 3, 6, 12, 14] jogos [26, 8, 7, 11, 28, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Lajeadense tabela [13, 3, 5, 5, 6, 13] jogos [26, 6, 10, 10, 16, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Passo Fundo tabela [13, 2, 7, 4, 9, 14] jogos [26, 6, 9, 11, 22, 34] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Novo Hamburgo tabela [13, 3, 2, 8, 14, 19] jogos [26, 6, 6, 14, 22, 38] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase classificatória / -: Aimoré tabela [13, 1, 5, 7, 9, 23] jogos [27, 1, 14, 12, 17, 37] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase classificatória / -: Ypiranga-RS tabela [26, 9, 10, 7, 34, 28] jogos [27, 9, 11, 7, 35, 29] — a tabela conta 26 jogos e as fontes trazem 27
- tabela publicada x jogos — Desempate da vaga / -: Santa Cruz-RS tabela [26, 6, 14, 6, 22, 27] jogos [26, 7, 13, 6, 22, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Desempate da vaga / -: Aimoré tabela [26, 1, 13, 12, 16, 36] jogos [27, 1, 14, 12, 17, 37] — a tabela conta 26 jogos e as fontes trazem 27
- tabela publicada x jogos — Melhor do interior nessa fase sera o Campeao do Interior / -: Juventude tabela [6, 0, 4, 2, 6, 10] jogos [7, 1, 4, 2, 7, 10] — a tabela conta 6 jogos e as fontes trazem 7
- placar diferente no ogol — Caxias x Aimoré (1990-05-09): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Pelotas x Guarany-RS (1990-06-22): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Aimoré x Caxias (1990-02-19): RSSSF 0-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Caxias x Juventude (1990-07-29): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Internacional x Grêmio (1990-07-15): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar corrigido pelo ogol — Caxias x Novo Hamburgo (1990-06-18): RSSSF 0-1, ogol 2-1; fica o do ogol, que fecha com a tabela publicada
- placar diferente no ogol — Grêmio x Internacional (1990-03-22): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- mando invertido no ogol — RSSSF Caxias 3-0 Lajeadense, ogol Lajeadense 0-3 Caxias (1990-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF Pelotas 5-1 Lajeadense, ogol Lajeadense 1-5 Pelotas (1990-05-09); fica a RSSSF
- jogo só no ogol, incluído em Top 2 qualified to finals: Guarany-RS 0-0 Pelotas (1990-04-14)
- jogo só no ogol, incluído em Top 2 qualified to finals: Juventude 0-1 Caxias (1990-05-20)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Ypiranga-RS (None)
- só na RSSSF (não achado no ogol): Pelotas 2-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Caxias 1-1 Juventude (None)
- vice pela Wikipédia (sem final de dois clubes): Caxias

### 1991

- placar diferente no ogol — Novo Hamburgo x Santa Cruz-RS (1991-08-28): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Grêmio x Lajeadense (1991-11-13): RSSSF 3-1, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Internacional x Grêmio (1991-12-08): RSSSF 1-0, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Grêmio x Internacional (1991-12-01): RSSSF 2-0, ogol 0-1; fica o da RSSSF
- jogo só no ogol, incluído em First Phase: Lajeadense 1-3 Grêmio (1991-09-05)
- só na RSSSF (não achado no ogol): Grêmio 4-2 Lajeadense (None)
- vencedor da final pelos jogos (Grêmio) diferente do campeão oficial (Internacional); fica o oficial

### 1992

- tabela publicada x jogos — Primeira fase / GRUPO 1: Grêmio tabela [21, 10, 9, 2, 33, 13] jogos [22, 11, 9, 2, 34, 13] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / GRUPO 1: Inter de Santa Maria tabela [21, 9, 7, 5, 27, 20] jogos [22, 9, 7, 6, 27, 21] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / GRUPO 1: Aimoré tabela [21, 5, 6, 10, 21, 27] jogos [21, 4, 7, 10, 19, 27] — placar diverge entre RSSSF e ogol em Lajeadense x Aimoré (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / GRUPO 1: Lajeadense tabela [21, 3, 8, 10, 12, 26] jogos [21, 3, 9, 9, 12, 24] — placar diverge entre RSSSF e ogol em Lajeadense x Aimoré (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / GRUPO 1: Grêmio tabela [6, 3, 2, 1, 7, 3] jogos [5, 2, 2, 1, 6, 3] — a tabela conta 6 jogos e as fontes trazem 5
- placar diferente no ogol — São Luiz x Pelotas (1992-07-29): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Passo Fundo x Pelotas (1992-08-02): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Lajeadense x Aimoré (1992-11-05): RSSSF 0-0, ogol 0-2; fica o da RSSSF
- mando invertido no ogol — RSSSF Grêmio 1-0 Guarany-RS, ogol Guarany-RS 0-1 Grêmio (1992-09-04); fica a RSSSF
- jogo só no ogol, incluído em PRIMEIRA FASE: Guarani V. Aires 4-1 Ypiranga-RS (1992-08-09)
- jogo só no ogol, incluído em PRIMEIRA FASE: Internacional 1-1 Grêmio (1992-09-13)
- jogo só no ogol, incluído em FINAL: Grêmio 1-3 Internacional (1992-12-20)

### 1993

- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: Lajeadense tabela [21, 10, 6, 5, 30, 23] jogos [41, 16, 12, 13, 47, 39] — a tabela conta 21 jogos e as fontes trazem 41
- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: GA Guarany tabela [21, 10, 4, 7, 26, 23] jogos [26, 10, 7, 9, 30, 29] — a tabela conta 21 jogos e as fontes trazem 26
- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: Santa Cruz-RS tabela [21, 9, 5, 7, 24, 20] jogos [28, 9, 7, 12, 27, 31] — a tabela conta 21 jogos e as fontes trazem 28
- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: Guarany-RS tabela [21, 8, 5, 8, 25, 26] jogos [22, 8, 6, 8, 26, 27] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: Grêmio Santanense tabela [21, 8, 5, 8, 23, 22] jogos [21, 8, 5, 8, 23, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — CLASSIFICAÇÂO PRIMEIRA FASE / -: Passo Fundo tabela [21, 7, 7, 7, 26, 30] jogos [22, 8, 7, 7, 29, 32] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Segunda fase / -: Ypiranga-RS tabela [6, 3, 1, 2, 6, 6] jogos [6, 3, 2, 1, 5, 4] — placar diverge entre RSSSF e ogol em Lajeadense x Ypiranga-RS (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / -: Lajeadense tabela [6, 3, 1, 2, 5, 3] jogos [41, 16, 12, 13, 47, 39] — a tabela conta 6 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Passo Fundo tabela [6, 0, 3, 3, 5, 8] jogos [28, 8, 10, 10, 33, 39] — a tabela conta 6 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase final / -: Inter de Santa Maria tabela [14, 1, 9, 4, 3, 8] jogos [14, 1, 8, 5, 3, 10] — placar diverge entre RSSSF e ogol em Inter de Santa Maria x Guarany-RS (0-2 x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Guarany-RS tabela [14, 1, 7, 6, 6, 14] jogos [14, 2, 7, 5, 7, 12] — placar diverge entre RSSSF e ogol em Grêmio Santanense x Guarany-RS (0-0 x 2-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Grêmio Santanense tabela [14, 3, 2, 9, 13, 21] jogos [14, 2, 3, 9, 11, 20] — placar diverge entre RSSSF e ogol em Grêmio Santanense x Guarany-RS (0-0 x 2-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Santa Cruz-RS x São Luiz (1993-03-24): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Glória x São Luiz (1993-04-07): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Juventude x Ypiranga-RS (1993-05-09): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Lajeadense x Ypiranga-RS (1993-06-02): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Ypiranga-RS x Passo Fundo (1993-06-10): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Grêmio Santanense x Guarany-RS (1993-06-24): RSSSF 0-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Inter de Santa Maria x Guarany-RS (1993-07-11): RSSSF 0-2, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Grêmio x Grêmio Santanense, ogol 1993-06-11); fica a do ogol
- adversário diferente no ogol — RSSSF Guarany-RS 1-1 Lajeadense, ogol GA Guarany 1-1 Lajeadense (1993-03-03); fica a RSSSF
- adversário diferente no ogol — RSSSF Santa Cruz-RS 2-2 Brasil de Pelotas, ogol São Luiz 2-2 Brasil de Pelotas (1993-03-28); fica a RSSSF
- só na RSSSF (não achado no ogol): Passo Fundo 3-2 Ypiranga-RS (1993-04-04)

### 1994

- tabela publicada x jogos — 2º Turno / -: Brasil de Farroupilha tabela [44, 15, 18, 11, 44, 35] jogos [44, 14, 19, 11, 43, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Pelotas tabela [44, 17, 11, 16, 55, 53] jogos [45, 17, 12, 16, 55, 53] — a tabela conta 44 jogos e as fontes trazem 45
- tabela publicada x jogos — 2º Turno / -: Guarani V. Aires tabela [44, 12, 19, 13, 41, 41] jogos [44, 12, 20, 12, 41, 40] — placar diverge entre RSSSF e ogol em Santa Cruz-RS x Guarani V. Aires (1-1 x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRASfL/FAR
- BRASfL/FAR — clube que o ogol não tem; entra só pela RSSSF
- placar diferente no ogol — Esportivo-RS x Guarany-RS (1994-03-27): RSSSF 3-0, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Santa Cruz-RS x Guarani V. Aires (1994-06-22): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Caxias x São Paulo-RS (1994-06-18): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Grêmio x Guarani V. Aires (1994-09-04): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Guarani V. Aires x Glória (1994-10-16): RSSSF 1-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Guarani V. Aires x Veranópolis (1994-11-20): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Pelotas x Grêmio (1994-12-13): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- jogo só no ogol, incluído em PRIMEIRO TURNO: Brasil de Farroupilha 0-0 Internacional (1994-03-19)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Ypiranga-RS 4-1 Grêmio Santanense (1994-03-20)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Brasil de Pelotas 1-0 Lajeadense (1994-03-31)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Internacional 1-0 São Paulo-RS (1994-04-10)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Internacional 1-0 Guarany-RS (1994-04-13)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Santa Cruz-RS 3-0 GA Guarany (1994-04-17)
- jogo só no ogol, incluído em PRIMEIRO TURNO: GA Guarany 2-0 São Paulo-RS (1994-04-20)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Santa Cruz-RS 0-0 Internacional (1994-05-01)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Inter de Santa Maria 2-1 Brasil de Pelotas (1994-05-29)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Veranópolis 1-2 Internacional (1994-06-02)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Ypiranga-RS 0-0 Internacional (1994-06-15)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Internacional 0-0 Brasil de Pelotas (1994-06-29)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Caxias 1-0 Internacional (1994-07-12)
- jogo só no ogol, incluído em PRIMEIRO TURNO: Internacional 2-0 Lajeadense (1994-07-21)
- jogo só no ogol, incluído em SEGUNDO TURNO: Esportivo-RS 2-0 Aimoré (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Caxias 1-0 Pelotas (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Guarani V. Aires 0-0 São Luiz (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Lajeadense 0-0 Grêmio Santanense (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Ypiranga-RS 2-0 GA Guarany (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Pelotas 0-0 Glória (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Passo Fundo 0-1 Internacional (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Farroupilha 2-0 Veranópolis (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Santa Cruz-RS 1-6 Juventude (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: Bagé 1-1 Inter de Santa Maria (1994-07-24)
- jogo só no ogol, incluído em SEGUNDO TURNO: São Luiz 2-0 Aimoré (1994-07-27)
- jogo só no ogol, incluído em SEGUNDO TURNO: Glória 1-0 Esportivo-RS (1994-07-27)
- jogo só no ogol, incluído em SEGUNDO TURNO: São Luiz 1-0 Caxias (1994-07-30)
- jogo só no ogol, incluído em SEGUNDO TURNO: Grêmio Santanense 0-3 Guarani V. Aires (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Glória 0-1 Ypiranga-RS (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Veranópolis 1-0 Passo Fundo (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Juventude 2-0 Brasil de Farroupilha (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Inter de Santa Maria 1-0 Santa Cruz-RS (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Guarany-RS 1-1 Bagé (1994-07-31)
- jogo só no ogol, incluído em SEGUNDO TURNO: Pelotas 3-0 Esportivo-RS (1994-08-03)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Farroupilha 0-0 Guarani V. Aires (1994-08-28)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Farroupilha 0-1 São Luiz (1994-09-04)
- jogo só no ogol, incluído em SEGUNDO TURNO: Caxias 1-0 Lajeadense (1994-09-04)
- jogo só no ogol, incluído em SEGUNDO TURNO: GA Guarany 1-1 Inter de Santa Maria (1994-09-07)
- jogo só no ogol, incluído em SEGUNDO TURNO: Glória 1-1 Brasil de Farroupilha (1994-09-07)
- jogo só no ogol, incluído em SEGUNDO TURNO: Internacional 2-0 Pelotas (1994-09-14)
- jogo só no ogol, incluído em SEGUNDO TURNO: São Paulo-RS 0-2 Guarani V. Aires (1994-09-18)
- jogo só no ogol, incluído em SEGUNDO TURNO: Internacional 1-0 Esportivo-RS (1994-10-19)
- jogo só no ogol, incluído em SEGUNDO TURNO: GA Guarany 4-0 Lajeadense (1994-10-27)
- jogo só no ogol, incluído em SEGUNDO TURNO: Internacional 1-0 Aimoré (1994-11-14)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Farroupilha 0-0 Pelotas (1994-11-19)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Pelotas 1-0 Guarany-RS (1994-11-19)
- jogo só no ogol, incluído em SEGUNDO TURNO: Brasil de Pelotas 0-0 Internacional (1994-12-01)
- jogo só no ogol, incluído em SEGUNDO TURNO: Guarany-RS 1-1 Grêmio (1994-12-04)
- jogo só no ogol, incluído em SEGUNDO TURNO: Guarani V. Aires 1-1 Internacional (1994-12-05)
- jogo só no ogol, incluído em SEGUNDO TURNO: São Luiz 0-2 Internacional (1994-12-07)
- jogo só no ogol, incluído em SEGUNDO TURNO: Internacional 0-1 Juventude (1994-12-16)
- só na RSSSF (não achado no ogol): BRASfL/FAR 0-0 Pelotas (None)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é Juventude (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Juventude

### 1995

- tabela publicada x jogos — Primeira fase / -: Juventude tabela [26, 10, 15, 1, 46, 24] jogos [34, 14, 15, 5, 55, 33] — a tabela conta 26 jogos e as fontes trazem 34
- tabela publicada x jogos — Primeira fase / -: Grêmio tabela [26, 11, 9, 6, 52, 27] jogos [36, 19, 11, 6, 78, 36] — a tabela conta 26 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Internacional tabela [26, 12, 6, 8, 36, 28] jogos [36, 17, 8, 11, 55, 35] — a tabela conta 26 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Ypiranga-RS tabela [26, 10, 10, 6, 43, 30] jogos [31, 13, 10, 8, 49, 36] — a tabela conta 26 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / -: Brasil de Farroupilha tabela [26, 9, 10, 7, 38, 39] jogos [33, 10, 13, 10, 40, 42] — a tabela conta 26 jogos e as fontes trazem 33
- tabela publicada x jogos — Primeira fase / -: São Luiz tabela [26, 8, 11, 7, 27, 25] jogos [35, 10, 13, 12, 35, 42] — a tabela conta 26 jogos e as fontes trazem 35
- tabela publicada x jogos — Primeira fase / -: Glória tabela [26, 8, 10, 8, 33, 30] jogos [25, 8, 10, 7, 34, 30] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [26, 8, 9, 9, 35, 27] jogos [25, 8, 8, 9, 34, 26] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Guarany-RS tabela [26, 8, 8, 10, 35, 37] jogos [23, 6, 8, 9, 19, 21] — a tabela conta 26 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Veranópolis tabela [26, 6, 12, 8, 25, 27] jogos [26, 5, 14, 7, 21, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Grêmio Santanense tabela [26, 6, 12, 8, 23, 38] jogos [25, 6, 11, 8, 20, 41] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Pelotas tabela [26, 5, 12, 9, 28, 43] jogos [25, 4, 13, 8, 28, 42] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Brasil de Pelotas tabela [26, 4, 12, 10, 27, 38] jogos [22, 4, 8, 10, 22, 33] — a tabela conta 26 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [26, 5, 6, 15, 26, 58] jogos [27, 5, 7, 15, 26, 58] — a tabela conta 26 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: GA Guarany tabela [18, 8, 5, 5, 23, 13] jogos [18, 7, 6, 5, 22, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Passo Fundo tabela [18, 8, 5, 5, 31, 23] jogos [17, 8, 4, 5, 30, 22] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Aimoré tabela [18, 5, 8, 5, 23, 26] jogos [17, 5, 7, 5, 22, 25] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Guarany-RS tabela [18, 4, 5, 9, 14, 19] jogos [17, 4, 4, 9, 13, 18] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / Grupo A: Esportivo-RS tabela [4, 3, 0, 1, 9, 3] jogos [8, 6, 0, 2, 16, 6] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo A: 15 de Novembro tabela [4, 1, 2, 1, 2, 5] jogos [8, 2, 2, 4, 5, 11] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo A: Inter de Santa Maria tabela [4, 0, 2, 2, 1, 4] jogos [8, 2, 2, 4, 3, 7] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / GRUPO B: Atlético-RS tabela [4, 2, 1, 1, 9, 4] jogos [8, 4, 2, 2, 15, 8] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / GRUPO B: GA Guarany tabela [4, 1, 2, 1, 5, 6] jogos [8, 3, 2, 3, 11, 11] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / GRUPO B: Passo Fundo tabela [4, 0, 3, 1, 3, 7] jogos [8, 1, 4, 3, 8, 15] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Grêmio tabela [36, 17, 12, 7, 73, 36] jogos [36, 19, 11, 6, 78, 36] — placar diverge entre RSSSF e ogol em Brasil de Farroupilha x Grêmio (2-2 x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Internacional tabela [36, 17, 8, 11, 56, 36] jogos [36, 17, 8, 11, 55, 35] — placar diverge entre RSSSF e ogol em São Luiz x Internacional (0-2 x 1-5) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Juventude tabela [34, 14, 16, 4, 57, 34] jogos [34, 14, 15, 5, 55, 33] — placar diverge entre RSSSF e ogol em Ypiranga-RS x Juventude (1-1 x 2-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: São Luiz tabela [34, 10, 13, 11, 35, 41] jogos [35, 10, 13, 12, 35, 42] — a tabela conta 34 jogos e as fontes trazem 35
- tabela publicada x jogos — Fase final / -: Ypiranga-RS tabela [32, 13, 11, 8, 50, 37] jogos [31, 13, 10, 8, 49, 36] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Glória tabela [26, 8, 10, 8, 33, 30] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Caxias tabela [26, 8, 9, 9, 35, 27] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Guarani V. Aires tabela [26, 8, 8, 10, 35, 37] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Veranópolis tabela [26, 6, 12, 8, 25, 27] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Grêmio Santanense tabela [26, 6, 12, 8, 23, 38] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Pelotas tabela [26, 5, 12, 9, 28, 43] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Brasil de Pelotas tabela [26, 4, 12, 10, 27, 38] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Fase final / -: Santa Cruz-RS tabela [26, 5, 6, 15, 26, 58] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aimoré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BAGÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Glória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): LAJEADENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lajeadense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PASSO FUNDO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pelotas
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- Aimoré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- BAGÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bagé)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias)
- Glória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Glória)
- LAJEADENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- Lajeadense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lajeadense)
- PASSO FUNDO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Passo Fundo)
- Pelotas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pelotas)
- placar diferente no ogol — São Luiz x Internacional (1995-07-22): RSSSF 0-2, ogol 1-5; fica o da RSSSF
- placar diferente no ogol — Ypiranga-RS x Juventude (1995-07-01): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Internacional x Ypiranga-RS (1995-07-05): RSSSF 1-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Grêmio x São Luiz (1995-07-19): RSSSF 0-0, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Juventude x Internacional (1995-07-12): RSSSF 5-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Brasil de Farroupilha x Grêmio (1995-07-08): RSSSF 2-2, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 7 jogos (ex.: São Luiz x Internacional, ogol 1995-07-22); fica a do ogol
- só na RSSSF (não achado no ogol): Grêmio 5-2 Brasil de Farroupilha (1995-02-17)
- só na RSSSF (não achado no ogol): Internacional 2-2 Caxias (1995-02-20)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-2 Internacional (1995-02-12)
- só na RSSSF (não achado no ogol): Juventude 0-3 Grêmio (1995-04-30)
- só na RSSSF (não achado no ogol): Glória 1-1 Pelotas (1995-04-12)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 Glória (1995-02-19)
- só na RSSSF (não achado no ogol): Veranópolis 1-0 São Luiz (1995-04-12)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Brasil de Pelotas (1995-02-19)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-1 Juventude (1995-02-11)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-0 Veranópolis (1995-02-19)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 Ypiranga-RS (1995-02-11)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-1 Guarani V. Aires (1995-02-19)
- só na RSSSF (não achado no ogol): Caxias 4-1 Santa Cruz-RS (1995-02-23)
- só na RSSSF (não achado no ogol): Pelotas 0-0 Grêmio Santanense (1995-02-18)
- só na RSSSF (não achado no ogol): Grêmio 3-1 Brasil de Pelotas (1995-03-04)
- só na RSSSF (não achado no ogol): Internacional 1-0 Veranópolis (1995-03-12)
- só na RSSSF (não achado no ogol): Guarani V. Aires 2-1 Internacional (1995-05-17)
- só na RSSSF (não achado no ogol): São Luiz 2-1 Grêmio (1995-05-17)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-1 Ypiranga-RS (1995-03-05)
- só na RSSSF (não achado no ogol): Glória 2-2 Guarani V. Aires (1995-03-12)
- só na RSSSF (não achado no ogol): Caxias 3-1 Pelotas (1995-03-05)
- só na RSSSF (não achado no ogol): Juventude 4-4 Brasil de Farroupilha (1995-03-12)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-1 São Luiz (1995-03-05)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-0 Santa Cruz-RS (1995-03-12)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-0 Juventude (1995-03-05)
- só na RSSSF (não achado no ogol): Ypiranga-RS 4-1 Pelotas (1995-03-12)
- só na RSSSF (não achado no ogol): Veranópolis 0-1 Glória (1995-03-05)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Caxias (1995-03-12)
- só na RSSSF (não achado no ogol): Grêmio 4-3 Ypiranga-RS (1995-03-12)
- só na RSSSF (não achado no ogol): Internacional 1-0 Santa Cruz-RS (1995-03-19)
- só na RSSSF (não achado no ogol): Pelotas 0-2 Internacional (1995-03-15)
- só na RSSSF (não achado no ogol): Veranópolis 1-1 Grêmio (1995-04-21)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-0 Veranópolis (1995-03-15)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-2 Glória (1995-03-15)
- só na RSSSF (não achado no ogol): Caxias 4-1 Brasil de Pelotas (1995-03-15)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 Guarani V. Aires (1995-03-15)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-1 Juventude (1995-03-07)
- só na RSSSF (não achado no ogol): Juventude 3-2 Brasil de Pelotas (1995-03-15)
- só na RSSSF (não achado no ogol): São Luiz 2-0 Grêmio Santanense (1995-03-15)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 3-1 Caxias (1995-03-15)
- só na RSSSF (não achado no ogol): Glória 0-1 Brasil de Farroupilha (1995-03-15)
- só na RSSSF (não achado no ogol): Pelotas 2-2 São Luiz (1995-03-15)
- só na RSSSF (não achado no ogol): Internacional 0-0 Grêmio Santanense (1995-03-26)
- só na RSSSF (não achado no ogol): Grêmio 4-3 Santa Cruz-RS (1995-04-29)
- só na RSSSF (não achado no ogol): Glória 2-2 Grêmio (1995-03-25)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 3-1 Internacional (1995-03-29)
- só na RSSSF (não achado no ogol): Ypiranga-RS 3-1 Guarani V. Aires (1995-03-26)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Glória (1995-03-29)
- só na RSSSF (não achado no ogol): Caxias 0-1 Juventude (1995-03-26)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Caxias (1995-03-29)
- só na RSSSF (não achado no ogol): Veranópolis 2-2 Brasil de Farroupilha (1995-03-26)
- só na RSSSF (não achado no ogol): Juventude 2-2 Ypiranga-RS (1995-03-29)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-2 Pelotas (1995-03-26)
- só na RSSSF (não achado no ogol): Guarani V. Aires 4-2 Pelotas (1995-03-29)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-1 São Luiz (1995-03-26)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Veranópolis (1995-03-29)
- só na RSSSF (não achado no ogol): Internacional 2-1 Grêmio (1995-04-02)
- só na RSSSF (não achado no ogol): Internacional 2-0 Glória (1995-04-05)
- só na RSSSF (não achado no ogol): São Luiz 1-0 Guarani V. Aires (1995-04-02)
- só na RSSSF (não achado no ogol): Grêmio 7-0 Grêmio Santanense (1995-04-05)
- só na RSSSF (não achado no ogol): Caxias 2-0 Ypiranga-RS (1995-04-02)
- só na RSSSF (não achado no ogol): Ypiranga-RS 3-0 São Luiz (1995-04-05)
- só na RSSSF (não achado no ogol): Veranópolis 1-1 Juventude (1995-04-02)
- só na RSSSF (não achado no ogol): Pelotas 0-0 Juventude (1995-04-05)
- só na RSSSF (não achado no ogol): Pelotas 4-3 Brasil de Farroupilha (1995-04-02)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-1 Brasil de Pelotas (1995-04-05)
- só na RSSSF (não achado no ogol): Glória 3-0 Brasil de Pelotas (1995-04-02)
- só na RSSSF (não achado no ogol): Caxias 2-0 Veranópolis (1995-04-05)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 3-2 Grêmio Santanense (1995-04-02)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-1 Brasil de Farroupilha (1995-04-05)
- só na RSSSF (não achado no ogol): Grêmio 0-0 Pelotas (1995-06-05)
- só na RSSSF (não achado no ogol): Veranópolis 1-0 São Luiz (1995-04-12)
- só na RSSSF (não achado no ogol): Grêmio 3-0 Guarani V. Aires (1995-04-12)
- só na RSSSF (não achado no ogol): Juventude 4-0 Glória (1995-05-09)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-2 Pelotas (1995-04-12)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Brasil de Farroupilha (1995-04-12)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-2 Grêmio Santanense (1995-05-09)
- só na RSSSF (não achado no ogol): Veranópolis 2-2 Santa Cruz-RS (1995-05-09)
- só na RSSSF (não achado no ogol): Glória 2-1 Caxias (1995-04-16)
- só na RSSSF (não achado no ogol): Guarani V. Aires 0-0 Caxias (1995-05-09)
- só na RSSSF (não achado no ogol): Juventude 1-1 São Luiz (1995-04-16)
- só na RSSSF (não achado no ogol): Internacional 1-1 Juventude (1995-04-19)
- só na RSSSF (não achado no ogol): Caxias 2-0 Grêmio (1995-05-14)
- só na RSSSF (não achado no ogol): São Luiz 2-1 Glória (1995-04-19)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-0 Ypiranga-RS (1995-04-19)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Brasil de Pelotas (1995-04-19)
- só na RSSSF (não achado no ogol): Pelotas 0-1 Veranópolis (1995-04-19)
- só na RSSSF (não achado no ogol): Guarani V. Aires 3-0 Santa Cruz-RS (1995-04-19)
- só na RSSSF (não achado no ogol): Internacional 0-0 Brasil de Pelotas (1995-04-23)
- só na RSSSF (não achado no ogol): Caxias 0-1 Internacional (1995-04-27)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-0 Caxias (1995-04-23)
- só na RSSSF (não achado no ogol): Juventude 0-3 Grêmio (1995-04-27)
- só na RSSSF (não achado no ogol): Juventude 2-0 Guarani V. Aires (1995-04-23)
- só na RSSSF (não achado no ogol): Glória 4-0 Santa Cruz-RS (1995-04-30)
- só na RSSSF (não achado no ogol): Glória 1-1 Pelotas (1995-04-23)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 2-1 São Luiz (1995-04-30)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Veranópolis (1995-04-23)
- só na RSSSF (não achado no ogol): Veranópolis 3-0 Ypiranga-RS (1995-04-30)
- só na RSSSF (não achado no ogol): Ypiranga-RS 3-0 Grêmio Santanense (1995-04-23)
- só na RSSSF (não achado no ogol): Guarani V. Aires 5-1 Brasil de Farroupilha (1995-04-30)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 Pelotas (1995-04-30)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Grêmio (1995-05-27)
- só na RSSSF (não achado no ogol): Veranópolis 2-1 Internacional (1995-06-15)
- só na RSSSF (não achado no ogol): Internacional 5-0 Guarani V. Aires (1995-05-03)
- só na RSSSF (não achado no ogol): Ypiranga-RS 5-1 Santa Cruz-RS (1995-05-03)
- só na RSSSF (não achado no ogol): Guarani V. Aires 2-2 Glória (1995-06-15)
- só na RSSSF (não achado no ogol): Pelotas 1-4 Caxias (1995-05-03)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-1 Juventude (1995-06-24)
- só na RSSSF (não achado no ogol): São Luiz 1-1 Brasil de Farroupilha (1995-05-03)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 3-1 Brasil de Pelotas (1995-05-17)
- só na RSSSF (não achado no ogol): Juventude 5-0 Grêmio Santanense (1995-05-04)
- só na RSSSF (não achado no ogol): Pelotas 0-0 Ypiranga-RS (1995-05-17)
- só na RSSSF (não achado no ogol): Glória 3-0 Veranópolis (1995-05-03)
- só na RSSSF (não achado no ogol): Caxias 1-2 Grêmio Santanense (1995-05-17)
- só na RSSSF (não achado no ogol): Ypiranga-RS 0-0 Grêmio (1995-06-25)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-4 Internacional (1995-05-13)
- só na RSSSF (não achado no ogol): Internacional 1-1 Pelotas (1995-05-10)
- só na RSSSF (não achado no ogol): Grêmio 1-1 Veranópolis (1995-06-08)
- só na RSSSF (não achado no ogol): Veranópolis 0-0 Guarani V. Aires (1995-05-10)
- só na RSSSF (não achado no ogol): Glória 2-1 Ypiranga-RS (1995-05-14)
- só na RSSSF (não achado no ogol): Juventude 2-0 Santa Cruz-RS (1995-05-10)
- só na RSSSF (não achado no ogol): Guarani V. Aires 2-0 Grêmio Santanense (1995-05-14)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Caxias (1995-05-10)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-2 Juventude (1995-05-14)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 São Luiz (1995-05-10)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-2 Veranópolis (1995-05-14)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-0 Glória (1995-05-10)
- só na RSSSF (não achado no ogol): São Luiz 2-2 Pelotas (1995-05-14)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-1 Internacional (1995-05-21)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-2 Grêmio (1995-06-23)
- só na RSSSF (não achado no ogol): Grêmio 3-0 Glória (1995-05-20)
- só na RSSSF (não achado no ogol): Internacional 0-1 Brasil de Farroupilha (1995-05-24)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-1 Ypiranga-RS (1995-05-21)
- só na RSSSF (não achado no ogol): Glória 4-1 Grêmio Santanense (1995-05-24)
- só na RSSSF (não achado no ogol): Juventude 1-1 Caxias (1995-05-21)
- só na RSSSF (não achado no ogol): Caxias 0-0 São Luiz (1995-05-25)
- só na RSSSF (não achado no ogol): Pelotas 1-1 Brasil de Pelotas (1995-05-21)
- só na RSSSF (não achado no ogol): São Luiz 4-1 Santa Cruz-RS (1995-05-21)
- só na RSSSF (não achado no ogol): Pelotas 2-0 Guarani V. Aires (1995-05-24)
- só na RSSSF (não achado no ogol): Veranópolis 1-1 Brasil de Farroupilha (1995-06-18)
- só na RSSSF (não achado no ogol): Grêmio 2-0 Internacional (1995-06-28)
- só na RSSSF (não achado no ogol): Glória 1-2 Internacional (1995-06-01)
- só na RSSSF (não achado no ogol): Guarani V. Aires 0-2 São Luiz (1995-05-29)
- só na RSSSF (não achado no ogol): Grêmio 7-0 Grêmio Santanense (1995-05-31)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 Caxias (1995-05-29)
- só na RSSSF (não achado no ogol): São Luiz 2-1 Ypiranga-RS (1995-05-31)
- só na RSSSF (não achado no ogol): Juventude 1-1 Veranópolis (1995-05-29)
- só na RSSSF (não achado no ogol): Juventude 4-0 Pelotas (1995-05-31)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 2-0 Pelotas (1995-05-29)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Guarani V. Aires (1995-05-31)
- só na RSSSF (não achado no ogol): Veranópolis 1-1 Caxias (1995-05-31)
- só na RSSSF (não achado no ogol): Grêmio Santanense 4-0 Santa Cruz-RS (1995-05-29)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-1 Santa Cruz-RS (1995-06-01)
- só na RSSSF (não achado no ogol): Pelotas 2-1 Grêmio (1995-06-03)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-0 Grêmio (1995-06-10)
- só na RSSSF (não achado no ogol): Internacional 1-0 São Luiz (1995-06-04)
- só na RSSSF (não achado no ogol): Glória 1-1 Juventude (1995-06-04)
- só na RSSSF (não achado no ogol): São Luiz 0-0 Juventude (1995-06-11)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-2 Brasil de Pelotas (1995-06-04)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 1-0 Brasil de Pelotas (1995-06-11)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-0 Brasil de Farroupilha (1995-06-04)
- só na RSSSF (não achado no ogol): Grêmio Santanense 1-0 Veranópolis (1995-06-11)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 Veranópolis (1995-06-04)
- só na RSSSF (não achado no ogol): Pelotas 2-1 Santa Cruz-RS (1995-06-11)
- só na RSSSF (não achado no ogol): Caxias 3-1 Guarani V. Aires (1995-06-04)
- só na RSSSF (não achado no ogol): Caxias 0-0 Glória (1995-06-11)
- só na RSSSF (não achado no ogol): Glória 2-1 São Luiz (1995-06-18)
- só na RSSSF (não achado no ogol): Grêmio 3-1 Caxias (1995-06-24)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-0 Brasil de Farroupilha (1995-06-18)
- só na RSSSF (não achado no ogol): Grêmio Santanense 0-0 Brasil de Farroupilha (1995-06-18)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 Veranópolis (1995-06-18)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-6 Guarani V. Aires (1995-06-25)
- só na RSSSF (não achado no ogol): Bagé 0-1 Lajeadense (None)
- só na RSSSF (não achado no ogol): Guarany-RS 2-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 0-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 3-6 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Atlético-RS 3-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): GA Guarany 0-0 Bagé (None)
- só na RSSSF (não achado no ogol): Aimoré 0-1 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 3-0 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Bagé 0-1 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 3-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-0 Bagé (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Atlético-RS 0-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 3-1 15 de Novembro (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 2-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Aimoré (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-2 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-0 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 1-3 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 0-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-1 Bagé (None)
- só na RSSSF (não achado no ogol): Aimoré 2-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 3-0 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Bagé (None)
- só na RSSSF (não achado no ogol): Aimoré 2-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-0 Atlético-RS (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Bagé 2-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Aimoré 2-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 2-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): GA Guarany 4-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 4-2 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Bagé (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-2 Lajeadense (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 0-4 GA Guarany (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 1-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 15 de Novembro (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 1-0 Bagé (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 3-2 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Aimoré 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 1-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Lajeadense 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Atlético-RS 0-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 Bagé (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): GA Guarany 4-1 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Atlético-RS 1-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 6-1 Bagé (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 0-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 3-0 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 3-1 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 1-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Lajeadense 1-0 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): GA Guarany 2-1 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Bagé 1-2 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Atlético-RS 2-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Guarany-RS 1-2 15 de Novembro (None)
- só na RSSSF (não achado no ogol): Lajeadense 1-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): GA Guarany 0-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 2-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-0 15 de Novembro (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 2-1 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): Esportivo-RS 4-0 15 de Novembro (None)
- só na RSSSF (não achado no ogol): 15 de Novembro 0-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-2 Esportivo-RS (None)
- só na RSSSF (não achado no ogol): GA Guarany 0-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-4 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 2-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): GA Guarany 3-2 Atlético-RS (None)
- só na RSSSF (não achado no ogol): Atlético-RS 1-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-2 GA Guarany (None)
- só na RSSSF (não achado no ogol): Bagé 1-1 Lajeadense (None)
- só na RSSSF (não achado no ogol): Guarany-RS 0-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Lajeadense 2-2 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 1-1 Bagé (None)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Bagé 0-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Guarany-RS 2-1 Bagé (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Guarany-RS 2-0 Lajeadense (None)
- só na RSSSF (não achado no ogol): Bagé 0-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Lajeadense 0-1 Bagé (None)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Guarany-RS (None)
- só na RSSSF (não achado no ogol): Internacional 3-1 Ypiranga-RS (1995-07-05)
- só na RSSSF (não achado no ogol): Ypiranga-RS 2-1 Juventude (1995-07-01)
- só na RSSSF (não achado no ogol): Juventude 0-0 Internacional (1995-07-12)
- só na RSSSF (não achado no ogol): Brasil de Farroupilha 0-0 Grêmio (1995-07-08)
- só na RSSSF (não achado no ogol): Ypiranga-RS 1-0 Internacional (1995-07-19)
- só na RSSSF (não achado no ogol): Grêmio 3-3 São Luiz (1995-07-19)
- só na RSSSF (não achado no ogol): São Luiz 1-5 Internacional (1995-07-22)

### 1996

- tabela publicada x jogos — Segunda fase / Grupo 1: Internacional tabela [6, 1, 3, 2, 5, 6] jogos [12, 3, 5, 4, 16, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo 2: Grêmio tabela [6, 1, 3, 2, 5, 5] jogos [12, 4, 5, 3, 14, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 1: Brasil de Pelotas tabela [12, 6, 4, 2, 18, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 1: Santa Cruz-RS tabela [12, 5, 4, 3, 19, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 1: Taquariense tabela [12, 4, 5, 3, 14, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 1: Aimoré tabela [12, 4, 4, 4, 17, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 1: 14 de Julho tabela [12, 5, 1, 6, 14, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / -: São Paulo-RS tabela [12, 3, 3, 6, 11, 16] jogos [13, 4, 3, 6, 12, 15] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 3: Brasil de Pelotas tabela [6, 4, 1, 1, 8, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 3: Aimoré tabela [6, 3, 0, 3, 6, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 3: Inter de Santa Maria tabela [6, 2, 1, 3, 13, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 3: Palmeirense tabela [6, 1, 2, 3, 5, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 4: Santo Ângelo tabela [6, 4, 1, 1, 9, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 4: Santa Cruz-RS tabela [6, 3, 0, 3, 10, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 4: Passo Fundo tabela [6, 2, 2, 2, 6, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Combined Table (First and Second Stages) / SÉRIE 4: Taquariense tabela [6, 1, 1, 4, 6, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Torneio de rebaixamento / -: São Paulo-RS tabela [6, 4, 0, 2, 5, 5] jogos [13, 4, 3, 6, 12, 15] — a tabela conta 6 jogos e as fontes trazem 13
- tabela publicada x jogos — Torneio de rebaixamento / -: Pratense tabela [6, 3, 1, 2, 9, 7] jogos [15, 3, 4, 8, 11, 19] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Torneio de rebaixamento / -: Rio Grande tabela [6, 0, 2, 4, 3, 9] jogos [14, 3, 1, 10, 12, 24] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / Grupo 1: Internacional tabela [6, 2, 2, 2, 11, 6] jogos [12, 3, 5, 4, 16, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo 2: Grêmio tabela [6, 3, 2, 1, 9, 4] jogos [12, 4, 5, 3, 14, 9] — a tabela conta 6 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AIMORÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PALMEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PASSO FUNDO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO GRANDE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SÃO PAULO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): TAQUARIENSE
- AIMORÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aimoré)
- PALMEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeirense)
- PASSO FUNDO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Passo Fundo)
- RIO GRANDE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Grande)
- SÃO PAULO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Paulo-RS)
- TAQUARIENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquariense)
- só na RSSSF (não achado no ogol): Taquariense 1-1 Aimoré (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-2 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 2-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 Taquariense (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 2-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 3-3 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Taquariense 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-2 Taquariense (None)
- só na RSSSF (não achado no ogol): Aimoré 0-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): 14 de Julho 0-5 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-1 Taquariense (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 3-0 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): Taquariense 0-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 3-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 0-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Taquariense 0-1 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 0-0 Taquariense (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Taquariense 2-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): Aimoré 5-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 3-1 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 2-0 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-2 Aimoré (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-1 14 de Julho (None)
- só na RSSSF (não achado no ogol): Aimoré 1-3 Taquariense (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 1-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 Rio Grande (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-0 Pratense (None)
- só na RSSSF (não achado no ogol): Rio Grande 0-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-2 Palmeirense (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Pratense 1-0 Rio Grande (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 2-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-0 Pratense (None)
- só na RSSSF (não achado no ogol): Rio Grande 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Palmeirense (None)
- só na RSSSF (não achado no ogol): Pratense 1-3 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 Pratense (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 4-1 Rio Grande (None)
- só na RSSSF (não achado no ogol): Pratense 0-2 Passo Fundo (None)
- só na RSSSF (não achado no ogol): GA Guarany 2-0 Palmeirense (None)
- só na RSSSF (não achado no ogol): Rio Grande 0-2 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-1 Pratense (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 3-1 Rio Grande (None)
- só na RSSSF (não achado no ogol): GA Guarany 0-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Pratense 1-1 Palmeirense (None)
- só na RSSSF (não achado no ogol): GA Guarany 2-1 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Rio Grande 1-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 1-1 Pratense (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 3-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): Passo Fundo 0-0 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Pratense 1-1 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): GA Guarany 3-0 Rio Grande (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 1-0 Palmeirense (None)
- só na RSSSF (não achado no ogol): Rio Grande 2-0 Pratense (None)
- só na RSSSF (não achado no ogol): Passo Fundo 3-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Pratense 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-1 Rio Grande (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-0 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Rio Grande 3-1 Palmeirense (None)
- só na RSSSF (não achado no ogol): Aimoré 3-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-2 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 5-0 Palmeirense (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 1-0 Aimoré (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 2-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Aimoré 1-0 Palmeirense (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 3-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Palmeirense 2-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Palmeirense 2-2 Inter de Santa Maria (None)
- só na RSSSF (não achado no ogol): Aimoré 0-1 Brasil de Pelotas (None)
- só na RSSSF (não achado no ogol): Inter de Santa Maria 0-1 Aimoré (None)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-0 Palmeirense (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 2-1 Taquariense (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 2-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Taquariense 1-0 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 1-1 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Taquariense 1-1 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 3-2 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-0 Taquariense (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 1-0 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Santa Cruz-RS 4-2 Taquariense (None)
- só na RSSSF (não achado no ogol): Santo Ângelo 1-0 Passo Fundo (None)
- só na RSSSF (não achado no ogol): Taquariense 1-2 Santo Ângelo (None)
- só na RSSSF (não achado no ogol): Passo Fundo 2-1 Santa Cruz-RS (None)
- só na RSSSF (não achado no ogol): Pratense 1-0 São Paulo-RS (None)
- só na RSSSF (não achado no ogol): São Paulo-RS 2-1 Pratense (None)
- só na RSSSF (não achado no ogol): Pratense 2-0 Rio Grande (None)
- só na RSSSF (não achado no ogol): Rio Grande 2-1 São Paulo-RS (None)

### 1997

- tabela publicada x jogos — Primeira fase / Grupo A: Grêmio tabela [13, 2, 4, 7, 8, 26] jogos [13, 9, 3, 1, 31, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Grêmio tabela [13, 2, 4, 7, 8, 26] jogos [13, 9, 3, 1, 31, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 1: Novo Hamburgo tabela [12, 2, 3, 7, 10, 18] jogos [12, 2, 3, 7, 10, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 1: 14 de Julho tabela [12, 1, 3, 8, 8, 29] jogos [12, 1, 3, 8, 8, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Torneio de rebaixamento / -: GA Guarany tabela [10, 3, 3, 4, 16, 16] jogos [9, 2, 3, 4, 13, 15] — a tabela conta 10 jogos e as fontes trazem 9
- placar corrigido pelo ogol — Farroupilha x Novo Hamburgo (1997-02-08): RSSSF 0-0, ogol 2-0; fica o do ogol, que fecha com a tabela publicada
- placar diferente no ogol — Santa Cruz-RS x Grêmio (1997-06-11): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- data com dia e mês trocados na RSSSF em 1 jogos (ex.: Brasil de Pelotas x Brasil de Farroupilha); fica a data do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 14 jogos (ex.: Caxias x Glória, ogol 1997-02-19); fica a do ogol
- só na RSSSF (não achado no ogol): 241325 3-2 São José-RS (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): São José-RS 2-3 Palmeirense (None)
- só na RSSSF (não achado no ogol): GA Guarany 4-1 241325 (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 1-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): São José-RS 4-1 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): 241325 2-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Palmeirense (None)
- só na RSSSF (não achado no ogol): 241325 2-1 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): GA Guarany 1-2 São José-RS (None)
- só na RSSSF (não achado no ogol): São José-RS 0-0 14 de Julho (None)
- só na RSSSF (não achado no ogol): Palmeirense 5-2 241325 (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 1-0 GA Guarany (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 São José-RS (None)
- só na RSSSF (não achado no ogol): Guarani V. Aires 3-1 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): 241325 3-3 Palmeirense (None)
- só na RSSSF (não achado no ogol): São José-RS 1-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 3-2 241325 (None)
- só na RSSSF (não achado no ogol): Palmeirense 4-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): 14 de Julho 2-1 241325 (None)
- só na RSSSF (não achado no ogol): GA Guarany 3-2 Palmeirense (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 2-0 São José-RS (None)
- só na RSSSF (não achado no ogol): Palmeirense 1-1 São José-RS (None)
- só na RSSSF (não achado no ogol): 241325 4-1 GA Guarany (None)
- só na RSSSF (não achado no ogol): 14 de Julho 1-1 Novo Hamburgo (None)
- só na RSSSF (não achado no ogol): São José-RS 3-2 241325 (None)
- só na RSSSF (não achado no ogol): GA Guarany 2-2 14 de Julho (None)
- só na RSSSF (não achado no ogol): Novo Hamburgo 5-2 Palmeirense (None)

### 1998

- tabela publicada x jogos — Primeira fase / Grupo B: São Paulo-RS tabela [12, 4, 6, 2, 13, 8] jogos [12, 3, 6, 3, 12, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Novo Hamburgo tabela [12, 5, 1, 6, 17, 23] jogos [12, 6, 1, 5, 18, 22] — há jogo do clube sem conferência no ogol
- mando invertido e placar diferente no ogol — RSSSF São Paulo-RS 0-1 Novo Hamburgo, ogol Novo Hamburgo 0-1 São Paulo-RS (1998-03-29); fica a RSSSF

### 1999

- placar diferente no ogol — Grêmio x Pelotas (1999-05-09): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- só na RSSSF (não achado no ogol): Grêmio 2-1 Veranópolis (1999-06-09)

### 2000

- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [12, 6, 3, 3, 21, 16] jogos [12, 6, 3, 3, 22, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Avenida tabela [12, 1, 2, 9, 14, 24] jogos [12, 1, 2, 9, 14, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [7, 5, 1, 1, 13, 6] jogos [19, 10, 4, 5, 32, 21] — a tabela conta 7 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [7, 2, 1, 4, 9, 11] jogos [26, 8, 6, 12, 38, 42] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [7, 1, 2, 4, 6, 9] jogos [26, 9, 9, 8, 32, 31] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Passo Fundo tabela [7, 0, 2, 5, 5, 20] jogos [26, 8, 7, 11, 34, 53] — a tabela conta 7 jogos e as fontes trazem 26

### 2001

- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [12, 7, 3, 2, 18, 12] jogos [12, 7, 3, 2, 18, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: São José-RS tabela [12, 7, 1, 4, 19, 11] jogos [12, 7, 1, 4, 24, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Veranópolis tabela [12, 4, 1, 7, 17, 21] jogos [12, 4, 1, 7, 17, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Pelotas tabela [7, 4, 0, 3, 9, 9] jogos [19, 11, 3, 5, 32, 20] — a tabela conta 7 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: São José-RS tabela [7, 3, 2, 2, 8, 6] jogos [19, 10, 3, 6, 32, 17] — a tabela conta 7 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-RS tabela [7, 2, 2, 3, 7, 9] jogos [19, 9, 5, 5, 25, 22] — a tabela conta 7 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Esportivo-RS tabela [7, 0, 1, 6, 5, 16] jogos [19, 5, 6, 8, 32, 33] — a tabela conta 7 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Pelotas tabela [7, 2, 3, 2, 6, 10] jogos [7, 2, 3, 2, 8, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Grêmio 2-0 São José-RS, ogol São José-RS 0-2 Grêmio (2001-05-18); fica a RSSSF

### 2002

- tabela publicada x jogos — Primeira fase / -: Santo Ângelo tabela [12, 5, 1, 6, 17, 17] jogos [11, 4, 1, 6, 14, 16] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Passo Fundo tabela [24, 9, 4, 11, 34, 40] jogos [24, 9, 4, 11, 35, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — São Gabriel x Esportivo-RS (2002-05-19): RSSSF 6-0, ogol 2-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: São Gabriel x Esportivo-RS, ogol 2002-05-19); fica a do ogol
- jogo só no ogol, incluído em First Stage: Santo Ângelo 3-1 15 de Novembro (2002-02-28)
- só na RSSSF (não achado no ogol): Guarani V. Aires 1-1 15 de Novembro (2002-05-05)
- só na RSSSF (não achado no ogol): Guarani V. Aires 0-0 São Gabriel (2002-05-08)
- só na RSSSF (não achado no ogol): São Gabriel 0-1 Guarani V. Aires (2002-05-12)
- só na RSSSF (não achado no ogol): São Gabriel 2-1 Esportivo-RS (2002-05-19)

### 2003

- sem ocorrências

### 2004

- placar diferente no ogol — Internacional x Juventude (2004-03-14): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- vencedor da final pelos jogos (Canoas) diferente do campeão oficial (Internacional); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Canoas

### 2005

- placar diferente no ogol — São José-RS x 15 de Novembro (2005-02-24): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Esportivo-RS x Canoas (2005-02-24): RSSSF 0-2, ogol 1-2; fica o da RSSSF

### 2006

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Grêmio

### 2007

- tabela publicada x jogos — Primeira fase / -: Glória tabela [16, 2, 4, 10, 18, 26] jogos [16, 2, 4, 10, 19, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Glória tabela [16, 2, 4, 10, 18, 26] jogos [16, 2, 4, 10, 19, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Brasil de Pelotas x Caxias (2007-02-25): RSSSF 1-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — São Luiz x 15 de Novembro (2007-02-26): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Veranópolis x Santa Cruz-RS (2007-03-25): RSSSF 3-1, ogol 2-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Novo Hamburgo x Glória, ogol 2007-03-04); fica a do ogol

### 2008

- sem ocorrências

### 2009

- tabela publicada x jogos — 1º Turno / Grupo 2: São Luiz tabela [8, 3, 2, 3, 8, 7] jogos [8, 3, 2, 3, 6, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo 2: Caxias tabela [7, 3, 2, 2, 15, 10] jogos [7, 3, 2, 2, 16, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo 2: São Luiz tabela [7, 1, 1, 5, 10, 17] jogos [7, 1, 1, 5, 5, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo 2: Caxias tabela [7, 3, 2, 2, 15, 10] jogos [7, 3, 2, 2, 16, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo 2: São Luiz tabela [7, 1, 1, 5, 10, 17] jogos [7, 1, 1, 5, 5, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Internacional x Avenida (2009-04-02): RSSSF 4-0, ogol 3-0; fica o do ogol, que fecha com a tabela publicada
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 2010

- tabela publicada x jogos — 2º Turno / Grupo 2: Grêmio tabela [15, 12, 2, 1, 33, 14] jogos [18, 15, 2, 1, 42, 17] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / Grupo 2: Internacional tabela [15, 10, 3, 2, 31, 15] jogos [17, 11, 3, 3, 34, 17] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / Grupo 2: São José-RS tabela [15, 9, 4, 2, 34, 20] jogos [16, 9, 4, 3, 34, 22] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / Grupo 2: Veranópolis tabela [15, 7, 4, 4, 34, 24] jogos [16, 7, 4, 5, 36, 28] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / Grupo 2: São Luiz tabela [15, 6, 5, 4, 29, 20] jogos [16, 6, 5, 5, 29, 22] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / Grupo 2: Novo Hamburgo tabela [15, 6, 3, 6, 23, 22] jogos [18, 8, 3, 7, 27, 24] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / Grupo 2: Inter de Santa Maria tabela [15, 5, 3, 7, 21, 32] jogos [17, 6, 3, 8, 24, 36] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / Grupo 2: Juventude tabela [15, 2, 6, 7, 19, 29] jogos [16, 2, 6, 8, 19, 31] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: São José-RS tabela [18, 9, 5, 4, 34, 22] jogos [18, 9, 6, 3, 35, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Esportivo-RS x Veranópolis (2010-02-03): RSSSF 1-3, ogol 0-3; fica o do ogol, que fecha com a tabela publicada

### 2011

- tabela publicada x jogos — Final / -: Grêmio tabela [15, 9, 3, 3, 28, 16] jogos [23, 13, 6, 4, 49, 29] — a tabela conta 15 jogos e as fontes trazem 23
- tabela publicada x jogos — Final / -: Internacional tabela [15, 8, 4, 3, 29, 15] jogos [21, 11, 6, 4, 39, 23] — a tabela conta 15 jogos e as fontes trazem 21
- tabela publicada x jogos — Final / -: Juventude tabela [15, 8, 4, 3, 27, 16] jogos [18, 9, 4, 5, 31, 20] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Cruzeiro-RS tabela [15, 8, 2, 5, 29, 18] jogos [19, 9, 3, 7, 36, 26] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Final / -: Ypiranga-RS tabela [15, 7, 3, 5, 26, 25] jogos [17, 7, 4, 6, 27, 31] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: São José-RS tabela [15, 6, 4, 5, 28, 19] jogos [17, 7, 5, 5, 31, 20] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Caxias tabela [15, 6, 4, 5, 24, 23] jogos [18, 7, 6, 5, 28, 26] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Lajeadense tabela [15, 5, 7, 3, 26, 19] jogos [16, 5, 7, 4, 26, 22] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: Veranópolis tabela [15, 5, 3, 7, 23, 30] jogos [16, 5, 3, 8, 23, 31] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: Santa Cruz-RS tabela [15, 4, 6, 5, 16, 21] jogos [16, 4, 6, 6, 16, 22] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: São Luiz tabela [15, 4, 5, 6, 23, 21] jogos [16, 4, 5, 7, 23, 23] — a tabela conta 15 jogos e as fontes trazem 16
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Internacional

### 2012

- tabela publicada x jogos — Final / -: Canoas tabela [15, 3, 4, 8, 17, 27] jogos [8, 0, 1, 7, 8, 21] — a tabela conta 15 jogos e as fontes trazem 8
- tabela publicada x jogos — Final / -: Avenida tabela [15, 3, 4, 8, 15, 27] jogos [8, 2, 2, 4, 10, 16] — a tabela conta 15 jogos e as fontes trazem 8
- tabela publicada x jogos — Final / -: Ypiranga-RS tabela [15, 2, 6, 7, 11, 18] jogos [8, 0, 3, 5, 6, 12] — a tabela conta 15 jogos e as fontes trazem 8
- mando invertido no ogol — RSSSF Caxias 1-1 Grêmio, ogol Grêmio 1-1 Caxias (2012-02-26); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Caxias x São José-RS, ogol 2012-02-22); fica a do ogol

### 2013

- jogo só no ogol, incluído em 1º Turno - Quartas de final: Lajeadense 1-1 Esportivo-RS (2013-02-24)
- jogo só no ogol, incluído em 2º Turno - Quartas de final: Passo Fundo 0-0 Veranópolis (2013-04-21)
- jogo só no ogol, incluído em 2º Turno: Grêmio 0-0 São Luiz (2013-04-23)
- jogo só no ogol, incluído em 2º Turno - Semifinal: Juventude 1-1 Grêmio (2013-04-27)
- jogo só no ogol, incluído em 2º Turno - Quartas de final: Internacional 0-0 Juventude (2013-05-05)
- campeão pela lista oficial, Internacional; o 1º pela soma dos jogos da última fase é Juventude (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Juventude

### 2014

- sem ocorrências

### 2015

- sem ocorrências

### 2016

- jogo só no ogol, incluído em FIRST STAGE:: São José-RS 0-0 Internacional (2016-02-03)

### 2017

- sem ocorrências

### 2018

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Avenida x Caxias, ogol 2018-03-17); fica a do ogol

### 2019

- sem ocorrências

### 2020

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2021

- só na RSSSF (não achado no ogol): Grêmio 1-1 Internacional (None)

### 2022

- sem ocorrências

### 2023

- sem ocorrências

### 2024

- tabela publicada x jogos — Primeira fase / -: Internacional tabela [11, 9, 1, 1, 21, 7] jogos [12, 10, 1, 1, 24, 7] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Grêmio tabela [11, 7, 2, 2, 23, 10] jogos [12, 8, 2, 2, 25, 10] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Caxias tabela [11, 4, 4, 3, 15, 14] jogos [12, 5, 4, 3, 16, 14] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Guarany de Bagé tabela [11, 4, 4, 3, 12, 15] jogos [12, 4, 4, 4, 12, 19] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Juventude tabela [11, 4, 3, 4, 15, 9] jogos [12, 5, 3, 4, 19, 9] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: São José-RS tabela [11, 3, 6, 2, 11, 10] jogos [12, 3, 6, 3, 11, 11] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Brasil de Pelotas tabela [11, 3, 6, 2, 9, 8] jogos [12, 3, 6, 3, 9, 10] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: São Luiz tabela [11, 2, 7, 2, 9, 9] jogos [12, 2, 7, 3, 9, 12] — a tabela conta 11 jogos e as fontes trazem 12
- jogo só no ogol, incluído em FIRST STAGE:: Caxias 1-0 São José-RS (2024-03-08)
- jogo só no ogol, incluído em FIRST STAGE:: Internacional 3-0 São Luiz (2024-03-09)
- jogo só no ogol, incluído em FIRST STAGE:: Guarany de Bagé 0-4 Juventude (2024-03-09)
- jogo só no ogol, incluído em FIRST STAGE:: Grêmio 2-0 Brasil de Pelotas (2024-03-10)

### 2025

- sem página da RSSSF (a lista de campeões ainda não tem o link): os jogos vêm do ogol
- vencedor da final pelos jogos (Ypiranga-RS) diferente do campeão oficial (Internacional); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Grêmio

### 2026

- sem página da RSSSF: os jogos vêm do ogol

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- De 1925 a 1976 o ogol não tem os jogos: o clube é casado pelo nome com o das outras temporadas.
- Clube que o ogol não tem entra pela RSSSF, com código "rs-<nome>". Nunca com o nome exato de outro clube (regra 6b).

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
