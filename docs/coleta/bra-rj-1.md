# Campeonato Carioca (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-rj-1/importar.py`. Pacote em `data/coleta/bra-rj-1/pacote/`. Mesmo código do Paulista
(`docs/coleta/bra-sp-1.md`), com as fontes do Rio.

**Temporadas:** 1906 a 2026. Até 1959 é o campeonato do Distrito Federal (a cidade do Rio de Janeiro); de 1960 a 1974,
o do estado da Guanabara; de 1975 em diante, o do estado do Rio de Janeiro. Nos anos de ligas rivais cada torneio
reconhecido é uma edição: 1912 (AFRJ e LMSA), 1924 (LMDT e AMEA), 1933 e 1934 (AMEA e LCF), 1935 e 1936 (FMD e LCF),
1937 (LFRJ, a liga da pacificação, na temporada "1937"; e o torneio inacabado da FMD, "1937 FMD", título homologado
pela FERJ em 2023).
1979 teve dois campeonatos reconhecidos: o Especial (fevereiro a abril) e o normal (maio a setembro). O campeonato do
antigo estado do Rio (interior, até 1978) é outra competição e fica de fora.

**Fontes:** RSSSF Brasil (`tablesr/rj{ano}.htm`: jogos, fases, datas, autores e tabelas; `rj1979s.htm`: o Especial de
1979; não há página de 2025 nem de 2026); ogol (calendário de cada edição, de 1906 a 2026, e o código de cada clube;
confere placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do
Campeonato Carioca: campeões e vices de cada ano, segunda fonte do campeão). Artilheiros pela lista da RSSSF
(`rjtops.htm`).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos
outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1906 | RSSSF + ogol | 6 | 30 (30) | 137 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1907 | RSSSF + ogol | 4 | 12 (12) | 42 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1908 | RSSSF + ogol | 6 | 30 (30) | 103 | 0 | 1 / 0 | Fluminense | RSSSF (classificação geral publicada) |
| 1909 | RSSSF + ogol | 7 | 31 (30) | 172 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1910 | RSSSF + ogol | 6 | 28 (30) | 157 | 0 | 0 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1911 | RSSSF + ogol | 4 | 12 (12) | 48 | 0 | 0 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1912 AFRJ | RSSSF + ogol | 7 | 27 (30) | 134 | 0 | 1 / 2 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1912 LMSA | RSSSF + ogol | 8 | 55 (56) | 272 | 0 | 0 / 0 | Paysandu-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1913 | RSSSF + ogol | 10 | 67 (66) | 261 | 0 | 0 / 1 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1914 | RSSSF + ogol | 7 | 42 (42) | 166 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1915 | RSSSF + ogol | 8 | 44 (42) | 211 | 0 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 | RSSSF + ogol | 8 | 45 (42) | 173 | 0 | 0 / 1 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1917 | RSSSF + ogol | 11 | 91 (90) | 398 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1918 | RSSSF + ogol | 11 | 92 (90) | 428 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1919 | RSSSF + ogol | 11 | 92 (90) | 403 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF + ogol | 10 | 90 (90) | 400 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1921 | RSSSF + ogol | 14 | 87 (44) | 338 | 0 | 2 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF + ogol | 14 | 86 (43) | 311 | 0 | 0 / 2 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1923 | RSSSF + ogol | 16 | 112 (57) | 451 | 0 | 1 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 LMDT | RSSSF + ogol | 23 | 153 (156) | 542 | 2 | 1 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 AMEA | RSSSF + ogol | 8 | 57 (56) | 266 | 0 | 1 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 | RSSSF + ogol | 12 | 91 (90) | 399 | 2 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 | RSSSF + ogol | 10 | 91 (90) | 478 | 0 | 0 / 1 | São Cristóvão | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 | RSSSF + ogol | 10 | 90 (90) | 468 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1928 | RSSSF + ogol | 11 | 110 (110) | 440 | 0 | 0 / 1 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1929 | RSSSF + ogol | 11 | 114 (113) | 465 | 0 | 0 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF + ogol | 11 | 111 (110) | 454 | 0 | 0 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF + ogol | 11 | 112 (113) | 455 | 0 | 0 / 1 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 | RSSSF + ogol | 12 | 133 (132) | 568 | 0 | 0 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 AMEA | RSSSF + ogol | 13 | 95 (90) | 441 | 0 | 0 / 0 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 LCF | RSSSF + ogol | 6 | 30 (30) | 113 | 0 | 0 / 1 | Bangu | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 AMEA | RSSSF + ogol | 10 | 39 (41) | 182 | 0 | 0 / 2 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 LCF | ogol | 7 | 42 (42) | 169 | 0 | 0 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 FMD | RSSSF + ogol | 9 | 90 (84) | 405 | 0 | 0 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 LCF | RSSSF + ogol | 6 | 45 (45) | 226 | 0 | 0 / 1 | América-RJ | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 FMD | RSSSF + ogol | 7 | 46 (46) | 188 | 0 | 3 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 LCF | RSSSF + ogol | 6 | 48 (48) | 210 | 0 | 1 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF + ogol | 12 | 132 (132) | 654 | 0 | 1 / 0 | Fluminense | RSSSF (classificação geral publicada) |
| 1937 FMD | RSSSF | 8 | 26 (0) | 100 | 0 | 1 / 0 | São Cristóvão | RSSSF (classificação geral publicada) |
| 1938 | RSSSF + ogol | 9 | 72 (72) | 339 | 0 | 0 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF + ogol | 9 | 108 (108) | 432 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1940 | RSSSF + ogol | 9 | 108 (108) | 456 | 0 | 0 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF + ogol | 10 | 120 (120) | 592 | 0 | 1 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF + ogol | 10 | 135 (135) | 635 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1943 | RSSSF + ogol | 10 | 90 (90) | 459 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1944 | RSSSF + ogol | 10 | 90 (90) | 379 | 0 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF + ogol | 10 | 90 (90) | 370 | 0 | 1 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 1946 | RSSSF + ogol | 10 | 102 (102) | 498 | 0 | 0 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF + ogol | 11 | 110 (110) | 534 | 0 | 1 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 1948 | RSSSF + ogol | 11 | 110 (110) | 499 | 0 | 1 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF + ogol | 11 | 110 (110) | 494 | 0 | 1 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 1950 | RSSSF + ogol | 11 | 110 (110) | 474 | 0 | 1 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 1951 | RSSSF + ogol | 11 | 112 (112) | 399 | 0 | 1 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF + ogol | 11 | 120 (110) | 504 | 154 | 1 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF + ogol | 12 | 160 (147) | 562 | 208 | 1 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF + ogol | 12 | 147 (147) | 558 | 0 | 2 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF + ogol | 12 | 150 (150) | 560 | 0 | 1 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF + ogol | 12 | 132 (132) | 455 | 0 | 1 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 1957 | RSSSF + ogol | 12 | 132 (132) | 456 | 0 | 1 / 0 | Botafogo | RSSSF (classificação geral publicada) |
| 1958 | RSSSF + ogol | 12 | 138 (138) | 487 | 0 | 1 / 2 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF + ogol | 12 | 134 (134) | 421 | 0 | 0 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF + ogol | 12 | 132 (132) | 391 | 0 | 1 / 0 | América-RJ | RSSSF (classificação geral publicada) |
| 1961 | RSSSF + ogol | 12 | 122 (122) | 282 | 0 | 1 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF + ogol | 13 | 156 (156) | 437 | 0 | 1 / 0 | Botafogo | RSSSF (classificação geral publicada) |
| 1963 | RSSSF + ogol | 13 | 158 (156) | 429 | 0 | 0 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF + ogol | 13 | 158 (158) | 423 | 0 | 1 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF + ogol | 8 | 56 (56) | 149 | 0 | 1 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 1966 | RSSSF + ogol | 12 | 94 (94) | 263 | 0 | 2 / 0 | Bangu | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF + ogol | 12 | 94 (94) | 252 | 0 | 2 / 0 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF + ogol | 12 | 94 (94) | 224 | 0 | 3 / 0 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF + ogol | 12 | 94 (94) | 237 | 0 | 2 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF + ogol | 12 | 94 (94) | 240 | 0 | 1 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF + ogol | 12 | 92 (92) | 194 | 0 | 0 / 3 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF + ogol | 12 | 125 (125) | 253 | 0 | 4 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF + ogol | 12 | 114 (114) | 258 | 0 | 1 / 3 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF + ogol | 12 | 126 (125) | 272 | 0 | 3 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF + ogol | 12 | 166 (165) | 441 | 0 | 2 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF + ogol | 15 | 212 (209) | 503 | 0 | 5 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF + ogol | 15 | 212 (211) | 505 | 0 | 1 / 2 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF + ogol | 12 | 132 (132) | 339 | 0 | 2 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF + ogol | 18 | 255 (255) | 598 | 0 | 2 / 2 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 Especial | RSSSF + ogol | 10 | 90 (90) | 265 | 0 | 1 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF + ogol | 14 | 138 (138) | 316 | 0 | 1 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF + ogol | 12 | 201 (200) | 490 | 0 | 2 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF + ogol | 12 | 136 (136) | 360 | 0 | 3 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF + ogol | 12 | 137 (136) | 294 | 0 | 2 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF + ogol | 12 | 143 (135) | 294 | 0 | 2 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF + ogol | 12 | 136 (136) | 275 | 0 | 2 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF + ogol | 12 | 135 (135) | 274 | 0 | 1 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF + ogol | 14 | 191 (191) | 368 | 0 | 3 / 2 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 12 | 140 (140) | 297 | 0 | 2 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF + ogol | 12 | 134 (134) | 291 | 0 | 2 / 0 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 12 | 134 (134) | 269 | 0 | 1 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF + ogol | 24 | 265 (135) | 532 | 0 | 1 / 3 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF + ogol | 26 | 315 (157) | 659 | 0 | 2 / 2 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF + ogol | 24 | 267 (135) | 557 | 0 | 3 / 1 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 12 | 79 (79) | 179 | 0 | 3 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF + ogol | 17 | 170 (169) | 447 | 5 | 6 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 12 | 160 (132) | 431 | 0 | 3 / 3 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 12 | 113 (112) | 295 | 1 | 4 / 3 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 12 | 85 (56) | 221 | 0 | 0 / 3 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 13 | 112 (92) | 306 | 3 | 6 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 14 | 153 (113) | 454 | 3 | 8 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 16 | 133 (101) | 400 | 0 | 3 / 3 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 12 | 148 (146) | 468 | 0 | 4 / 1 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 12 | 72 (72) | 193 | 147 | 0 / 2 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 12 | 74 (74) | 206 | 41 | 5 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 12 | 75 (74) | 220 | 19 | 3 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 12 | 75 (74) | 252 | 0 | 3 / 2 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 12 | 78 (76) | 272 | 0 | 3 / 3 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 16 | 128 (128) | 421 | 0 | 9 / 0 | Flamengo | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 16 | 128 (128) | 393 | 0 | 8 / 1 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 16 | 132 (132) | 403 | 399 | 2 / 8 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 16 | 126 (132) | 367 | 358 | 4 / 5 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 16 | 128 (134) | 369 | 361 | 6 / 5 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 16 | 126 (126) | 323 | 0 | 8 / 1 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 16 | 126 (126) | 340 | 340 | 2 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 16 | 128 (128) | 324 | 318 | 4 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 16 | 127 (127) | 314 | 0 | 9 / 0 | Vasco | RSSSF (classificação geral publicada) |
| 2017 | RSSSF + ogol | 16 | 109 (109) | 287 | 287 | 2 / 4 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 16 | 103 (103) | 270 | 126 | 0 / 0 | Botafogo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 16 | 109 (103) | 248 | 214 | 4 / 2 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 16 | 109 (107) | 257 | 198 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 17 | 108 (108) | 283 | 0 | 6 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 12 | 78 (78) | 189 | 0 | 2 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 12 | 78 (78) | 198 | 197 | 7 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 12 | 78 (78) | 200 | 0 | 2 / 1 | Flamengo | RSSSF (classificação geral publicada) |
| 2025 | ogol | 12 | 78 (78) | 170 | 0 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 12 | 62 (62) | 159 | 0 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1906

- tabela publicada x jogos — Fase única / -: Paysandu-RJ tabela [10, 7, 0, 3, 26, 12] jogos [10, 7, 0, 3, 27, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Rio Cricket tabela [10, 6, 0, 4, 23, 9] jogos [10, 6, 0, 4, 24, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Bangu tabela [10, 3, 0, 7, 13, 18] jogos [10, 3, 0, 7, 13, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Football and Athletic tabela [10, 1, 0, 9, 2, 55] jogos [10, 1, 0, 9, 3, 55] — há jogo do clube sem conferência no ogol
- jogo anulado fica de fora (1): F. ATHLETIC C 5-2 RIACHUELO F. C — jogo anotado depois da fonte, no fim da página (4/11/1906): o Riachuelo não jogou o campeonato de 1906 (não está na tabela nem no ogol)
- jogo só no ogol, incluído em Fase única: Rio Cricket 1-0 Paysandu-RJ (1906-06-16)
- jogo só no ogol, incluído em Fase única: Paysandu-RJ 1-0 Bangu (1906-09-16)
- jogo só no ogol, incluído em Fase única: Football and Athletic 1-0 Rio Cricket (1906-10-27)

### 1907

- título dividido entre Fluminense e Botafogo: terminaram empatados (Botafogo 10 pontos e Fluminense 8 na tabela da RSSSF, os dois com 2 pontos perdidos), não houve acordo sobre o desempate e a LMSA acabou sem declarar campeão; em 1996 a FERJ declarou os dois campeões (RSSSF; Lance; Wikipédia). O pacote tem o Fluminense no campo campeao, o vice vazio e o Botafogo na observação até o banco aceitar dois campeões numa edição (D-07, como o Paulista 1973)
- tabela publicada x jogos — Fase única / -: Botafogo tabela [6, 5, 0, 1, 14, 9] jogos [6, 5, 0, 1, 15, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Fluminense tabela [6, 5, 0, 1, 15, 5] jogos [6, 4, 0, 2, 15, 8] — placar diverge entre RSSSF e ogol em Fluminense x Football and Athletic (0-3 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Football and Athletic tabela [6, 1, 0, 5, 2, 9] jogos [6, 2, 0, 4, 5, 10] — placar diverge entre RSSSF e ogol em Fluminense x Football and Athletic (0-3 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Paysandu-RJ x Fluminense, ogol 1907-06-16); fica a do ogol
- jogo só no ogol, incluído em Fase única: Botafogo 1-0 Football and Athletic (1907-09-29)
- campeão pela lista oficial, Fluminense; o 1º pela soma dos jogos da última fase é Botafogo (desempate, jogo extra ou pontos tirados fora de campo)

### 1908

- mando invertido no ogol — RSSSF Paysandu-RJ 1-10 Fluminense, ogol Fluminense 10-1 Paysandu-RJ (1908-05-03); fica a RSSSF
- W.O. do ogol incluído: Rio Cricket x Riachuelo-RJ (1908-07-19), vitória do Rio Cricket pela tabela publicada
- W.O. do ogol incluído: Paysandu-RJ x Riachuelo-RJ (1908-07-26), vitória do Paysandu-RJ pela tabela publicada
- W.O. do ogol incluído: América-RJ x Riachuelo-RJ (1908-08-09), vitória do América-RJ pela tabela publicada
- W.O. do ogol incluído: Paysandu-RJ x Botafogo (1908-08-09), vitória do Botafogo pela tabela publicada
- W.O. do ogol incluído: Fluminense x Riachuelo-RJ (1908-08-16), vitória do Fluminense pela tabela publicada
- W.O. do ogol incluído: Paysandu-RJ x Riachuelo-RJ (1908-09-13), vitória do Paysandu-RJ pela tabela publicada
- W.O. do ogol incluído: Botafogo x Rio Cricket (1908-09-13), vitória do Botafogo pela tabela publicada
- W.O. do ogol incluído: Botafogo x Riachuelo-RJ (1908-09-27), vitória do Botafogo pela tabela publicada
- W.O. do ogol incluído: Rio Cricket x América-RJ (1908-09-27), vitória do América-RJ pela tabela publicada
- W.O. do ogol incluído: Rio Cricket x Riachuelo-RJ (1908-10-18), vitória do Rio Cricket pela tabela publicada
- W.O. do ogol incluído: Paysandu-RJ x América-RJ (1908-10-18), vitória do América-RJ pela tabela publicada

### 1909

- tabela publicada x jogos — Fase única / -: Fluminense tabela [10, 8, 2, 0, 45, 8] jogos [10, 8, 2, 0, 54, 8] — placar diverge entre RSSSF e ogol em Riachuelo-RJ x Fluminense (2-8 x 2-7) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Botafogo tabela [10, 7, 2, 1, 53, 6] jogos [10, 7, 2, 1, 54, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-RJ tabela [10, 6, 2, 2, 28, 11] jogos [10, 6, 2, 2, 29, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Riachuelo-RJ tabela [10, 3, 1, 6, 12, 32] jogos [11, 3, 1, 7, 14, 36] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Haddock Lobo tabela [10, 1, 2, 7, 13, 53] jogos [10, 1, 2, 7, 13, 54] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Mangueira tabela [10, 0, 1, 9, 4, 45] jogos [8, 0, 1, 7, 4, 45] — a tabela conta 10 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bangu
- Bangu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bangu)
- placar diferente no ogol — Riachuelo-RJ x Fluminense (1909-09-26): RSSSF 2-8, ogol 2-7; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: Haddock Lobo 0-1 Botafogo (1909-10-10)
- só na RSSSF (não achado no ogol): Bangu 0-1 América-RJ (1909-05-09)
- só na RSSSF (não achado no ogol): Bangu 0-9 Fluminense (1909-05-23)
- só na RSSSF (não achado no ogol): Bangu 4-2 Riachuelo-RJ (1909-06-06)
- W.O. do ogol incluído: Riachuelo-RJ x Mangueira (1909-08-22), vitória do Riachuelo-RJ pela tabela publicada
- W.O. do ogol incluído: Botafogo x Mangueira (1909-09-12), vitória do Botafogo pela tabela publicada
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: America-RJ x Mangueira (1909-10-03)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Fluminense x Mangueira (1909-10-10)

### 1910

- tabela publicada x jogos — Fase única / -: América-RJ tabela [10, 7, 0, 3, 31, 18] jogos [10, 7, 0, 3, 32, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Riachuelo-RJ tabela [10, 3, 0, 7, 16, 37] jogos [8, 2, 0, 6, 16, 38] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Rio Cricket tabela [10, 2, 1, 7, 4, 26] jogos [8, 1, 1, 6, 4, 26] — a tabela conta 10 jogos e as fontes trazem 8
- jogo só no ogol, incluído em Fase única: Rio Cricket 2-1 Haddock Lobo (1910-09-04)
- jogo só no ogol, incluído em Fase única: América-RJ 1-0 Riachuelo-RJ (1910-09-18)
- W.O. do ogol incluído: Riachuelo-RJ x Fluminense (1910-10-09), vitória do Fluminense pela tabela publicada
- W.O. do ogol incluído: Fluminense x Haddock Lobo (1910-10-20), vitória do Fluminense pela tabela publicada
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Riachuelo-RJ x Rio Cricket (1910-07-24)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Rio Cricket x Riachuelo-RJ (1910-10-30)

### 1911

- placar diferente no ogol — Fluminense x América-RJ (1911-07-09): RSSSF 2-0, ogol 4-0; fica o da RSSSF
- jogo só no ogol, incluído em Primeira fase / Grupo C: Paysandu-RJ 0-2 Fluminense (1911-05-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 3-3 América-RJ (1911-05-28)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 0-5 Fluminense (1911-06-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Paysandu-RJ 2-4 América-RJ (1911-07-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 4-1 Paysandu-RJ (1911-07-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-1 Rio Cricket (1911-08-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-1 Paysandu-RJ (1911-09-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 5-0 Rio Cricket (1911-09-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-1 Paysandu-RJ (1911-09-24)
- jogo só no ogol, incluído em 2º Turno: América-RJ 0-2 Fluminense (1911-10-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Paysandu-RJ 2-1 Rio Cricket (1911-10-22)

### 1912 AFRJ

- tabela publicada x jogos — 1° TURNO / -: Paulistano-RJ tabela [5, 2, 1, 2, 9, 12] jogos [9, 3, 3, 3, 13, 23] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — 1° TURNO / -: Germânia-RJ tabela [5, 1, 1, 3, 8, 16] jogos [9, 2, 1, 6, 11, 37] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — 2° TURNO / -: SC Americano-RJ tabela [10, 8, 1, 1, 46, 12] jogos [9, 6, 2, 1, 37, 10] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2° TURNO / -: Paulistano-RJ tabela [10, 4, 2, 4, 17, 26] jogos [9, 3, 3, 3, 13, 23] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2° TURNO / -: Germânia-RJ tabela [10, 3, 1, 6, 12, 33] jogos [9, 2, 1, 6, 11, 37] — a tabela conta 10 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Petropolitano F.C
- Petropolitano F.C — clube que o ogol não tem; entra só pela RSSSF
- placar diferente no ogol — Paulistano-RJ x SC Americano-RJ (1912-08-11): RSSSF 0-0, ogol 1-3; fica o da RSSSF
- jogo só no ogol, incluído em Primeira fase / Grupo C: Cattete FC 1-2 Paulistano-RJ (1912-05-12)
- jogo só no ogol, incluído em 2° TURNO: SC Americano-RJ 3-1 Botafogo (1912-05-13)
- jogo só no ogol, incluído em 1° TURNO: Internacional-RJ 1-3 Germânia-RJ (1912-05-19)
- jogo só no ogol, incluído em 1° TURNO: Botafogo 6-2 Cattete FC (1912-06-02)
- jogo só no ogol, incluído em 1° TURNO: Paulistano-RJ 3-1 Internacional-RJ (1912-06-23)
- jogo só no ogol, incluído em 2° TURNO: Germânia-RJ 0-1 Botafogo (1912-07-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: SC Americano-RJ 5-3 Cattete FC (1912-07-07)
- jogo só no ogol, incluído em 2° TURNO: Germânia-RJ 3-3 Paulistano-RJ (1912-07-14)
- jogo só no ogol, incluído em 2° TURNO: Paulistano-RJ 0-4 Botafogo (1912-07-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Internacional-RJ 1-8 SC Americano-RJ (1912-07-21)
- jogo só no ogol, incluído em 2° TURNO: Germânia-RJ 1-9 SC Americano-RJ (1912-07-28)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 9-0 Internacional-RJ (1912-08-04)
- jogo só no ogol, incluído em 2° TURNO: Cattete FC 2-1 Germânia-RJ (1912-08-11)
- jogo só no ogol, incluído em 2° TURNO: Botafogo 2-0 SC Americano-RJ (1912-08-18)
- jogo só no ogol, incluído em 2° TURNO: Paulistano-RJ 0-5 Cattete FC (1912-09-01)
- jogo só no ogol, incluído em 2° TURNO: Germânia-RJ 2-1 Internacional-RJ (1912-09-01)
- jogo só no ogol, incluído em 2° TURNO: Cattete FC 0-0 Internacional-RJ (1912-09-07)
- jogo só no ogol, incluído em 2° TURNO: Botafogo 8-1 Paulistano-RJ (1912-09-08)
- jogo só no ogol, incluído em 2° TURNO: Cattete FC 1-2 SC Americano-RJ (1912-09-15)
- jogo só no ogol, incluído em 2° TURNO: SC Americano-RJ 10-1 Internacional-RJ (1912-09-22)
- jogo só no ogol, incluído em 2° TURNO: Paulistano-RJ 4-1 Germânia-RJ (1912-10-13)
- jogo só no ogol, incluído em 2° TURNO: SC Americano-RJ 0-0 Paulistano-RJ (1912-10-27)
- só na RSSSF (não achado no ogol): Petropolitano F.C 2-2 Internacional-RJ (1912-05-26)
- só na RSSSF (não achado no ogol): Petropolitano F.C 6-0 Germânia-RJ (1912-06-16)
- só na RSSSF (não achado no ogol): Petropolitano F.C 1-2 Cattete FC (1912-06-30)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Internacional-RJ x Cattete FC (1912-08-18)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Internacional-RJ x Paulistano-RJ (1912-09-29)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: SC Americano-RJ x Germânia-RJ (1912-10-06)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Botafogo x Cattete FC (1912-10-13)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Botafogo x Internacional-RJ (1912-10-20)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Germânia-RJ x Cattete FC (1912-10-27)

### 1912 LMSA

- placar diferente no ogol — Bangu x Rio Cricket (1912-10-13): RSSSF 3-5, ogol 2-5; fica o da RSSSF
- jogo só no ogol, incluído em 1º Turno: São Cristóvão 1-1 América-RJ (1912-05-05)
- jogo só no ogol, incluído em 1º Turno: São Cristóvão 0-1 Fluminense (1912-06-02)
- jogo só no ogol, incluído em 1º Turno: São Cristóvão 3-0 Mangueira (1912-06-30)
- jogo só no ogol, incluído em 2º Turno: São Cristóvão 0-3 Flamengo (1912-11-01)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: São Cristóvão x Rio Cricket (1912-09-29)

### 1913

- tabela publicada x jogos — 2º Turno / -: América-RJ tabela [9, 0, 0, 9, 3, 31] jogos [16, 12, 0, 4, 41, 13] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Flamengo tabela [15, 10, 2, 3, 43, 13] jogos [15, 10, 2, 3, 44, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Paysandu-RJ tabela [15, 7, 3, 5, 29, 25] jogos [15, 7, 3, 5, 30, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: São Cristóvão tabela [15, 4, 4, 7, 22, 32] jogos [16, 5, 4, 7, 24, 32] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Rio Cricket tabela [15, 4, 3, 8, 18, 27] jogos [15, 4, 3, 8, 19, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Mangueira tabela [9, 3, 0, 6, 12, 42] jogos [9, 3, 0, 6, 13, 42] — há jogo do clube sem conferência no ogol
- placar diferente no ogol — SC Americano-RJ x Bangu (1913-06-15): RSSSF 0-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — São Cristóvão x América-RJ (1913-11-30): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: São Cristóvão x América-RJ, ogol 1913-11-30); fica a do ogol
- jogo só no ogol, incluído em 1º Turno: Rio Cricket 1-0 SC Americano-RJ (1913-06-29)
- jogo só no ogol, incluído em 1º Turno: Rio Cricket 2-3 São Cristóvão (1913-08-17)
- jogo só no ogol, incluído em 1º Turno: Flamengo 1-0 SC Americano-RJ (1913-08-17)
- jogo só no ogol, incluído em 1º Turno: Paysandu-RJ 1-0 SC Americano-RJ (1913-09-07)
- jogo só no ogol, incluído em 1º Turno: Mangueira 1-0 SC Americano-RJ (1913-09-13)
- jogo só no ogol, incluído em 2º Turno: América-RJ 1-0 Paysandu-RJ (1913-11-01)
- jogo só no ogol, incluído em 2º Turno: São Cristóvão 1-0 Rio Cricket (1913-12-07)
- só na RSSSF (não achado no ogol): São Cristóvão 0-1 América-RJ (1913-11-30)
- campeão pela lista oficial, América-RJ; o 1º pela soma dos jogos da última fase é Flamengo (desempate, jogo extra ou pontos tirados fora de campo)

### 1914

- jogo só no ogol, incluído em Fase única: Rio Cricket 1-2 São Cristóvão (1914-09-27)
- W.O. do ogol incluído: América-RJ x Botafogo (1914-05-31), vitória do América-RJ pela tabela publicada

### 1915

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANDARAHY
- ANDARAHY — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Andarahy)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-3 Fluminense (1915-05-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 0-5 Flamengo (1915-05-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 0-3 Botafogo (1915-05-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-0 América-RJ (1915-05-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-1 Rio Cricket (1915-05-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 0-5 América-RJ (1915-05-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 0-5 Flamengo (1915-05-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 3-5 Fluminense (1915-05-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-1 Botafogo (1915-05-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 0-8 América-RJ (1915-05-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-1 São Cristóvão (1915-06-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 3-1 Bangu (1915-06-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-2 Botafogo (1915-07-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 8-2 São Cristóvão (1915-07-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 0-1 Rio Cricket (1915-07-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 2-4 Flamengo (1915-07-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 4-1 Bangu (1915-07-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-1 São Cristóvão (1915-07-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 0-4 Flamengo (1915-07-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 2-5 Flamengo (1915-08-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 9-1 São Cristóvão (1915-08-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 6-3 Rio Cricket (1915-08-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 6-1 Bangu (1915-08-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 1-1 Fluminense (1915-08-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 3-0 Bangu (1915-08-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 0-5 Fluminense (1915-08-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-0 Botafogo (1915-08-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 0-0 São Cristóvão (1915-09-05)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 5-0 Bangu (1915-09-05)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 0-0 Flamengo (1915-09-19)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 7-0 Rio Cricket (1915-09-19)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-3 América-RJ (1915-09-26)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 4-1 Rio Cricket (1915-09-26)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-2 América-RJ (1915-10-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Rio Cricket 1-4 São Cristóvão (1915-10-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-4 Fluminense (1915-10-12)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-1 América-RJ (1915-10-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 4-2 Botafogo (1915-10-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 4-1 Botafogo (1915-10-31)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 5-1 Bangu (1915-10-31)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 5-3 Fluminense (1915-11-01)
- só na RSSSF (não achado no ogol): Andarahy 2-2 Rio Cricket (None)
- só na RSSSF (não achado no ogol): Rio Cricket 2-2 Andarahy (None)
- só na RSSSF (não achado no ogol): Andarahy 4-2 Rio Cricket (None)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Flamengo x Rio Cricket (1915-05-02)
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é Fluminense (desempate, jogo extra ou pontos tirados fora de campo)

### 1916

- tabela publicada x jogos — Fase única / -: Flamengo tabela [12, 4, 3, 5, 23, 22] jogos [12, 4, 3, 5, 22, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Fluminense tabela [12, 4, 3, 5, 24, 25] jogos [12, 3, 3, 6, 24, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Andarahy tabela [12, 4, 2, 6, 16, 19] jogos [11, 4, 2, 5, 16, 15] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: São Cristóvão tabela [12, 3, 2, 7, 23, 30] jogos [11, 3, 2, 6, 22, 28] — a tabela conta 12 jogos e as fontes trazem 11
- jogo só no ogol, incluído em Fase única: Andarahy 0-4 Flamengo (1916-05-07)
- jogo só no ogol, incluído em Fase única: São Cristóvão 1-2 Fluminense (1916-09-10)
- só na RSSSF (não achado no ogol): Fluminense 2-3 Flamengo (1916-10-22)
- só na RSSSF (não achado no ogol): Botafogo 2-1 Bangu (1916-12-17)
- só na RSSSF (não achado no ogol): São Cristóvão 5-3 Carioca FC (1916-12-17)

### 1917

- tabela publicada x jogos — Fase única / -: Flamengo tabela [18, 12, 2, 4, 44, 25] jogos [17, 11, 2, 4, 44, 25] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Andarahy tabela [18, 8, 3, 7, 36, 32] jogos [17, 7, 3, 7, 36, 32] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Bangu tabela [18, 5, 1, 12, 27, 54] jogos [16, 5, 1, 10, 27, 54] — a tabela conta 18 jogos e as fontes trazem 16
- jogo só no ogol, incluído em Fase única: Andarahy 1-0 Bangu (1917-11-18)
- jogo só no ogol, incluído em Fase única: Bangu 0-1 Flamengo (1917-12-16)
- só na RSSSF (não achado no ogol): Villa Isabel 5-0 Cattete FC (1918-02-24)

### 1918

- tabela publicada x jogos — Fase única / -: Fluminense tabela [18, 13, 3, 2, 52, 17] jogos [17, 13, 3, 1, 52, 17] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Botafogo tabela [18, 12, 2, 4, 55, 22] jogos [17, 11, 2, 4, 55, 22] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Carioca FC tabela [18, 8, 0, 10, 31, 50] jogos [17, 7, 0, 10, 31, 50] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Mangueira tabela [18, 0, 1, 17, 13, 58] jogos [17, 0, 1, 16, 13, 58] — a tabela conta 18 jogos e as fontes trazem 17
- jogo só no ogol, incluído em Fase única: Mangueira 0-1 Botafogo (1918-06-30)
- jogo só no ogol, incluído em Fase única: Fluminense 0-1 Carioca FC (1918-12-22)
- só na RSSSF (não achado no ogol): Botafogo 3-2 São Cristóvão (1919-04-06)
- só na RSSSF (não achado no ogol): Mangueira 2-1 Americano FC Rio (1919-04-06)

### 1919

- tabela publicada x jogos — Fase única / -: Bangu tabela [18, 8, 0, 10, 24, 38] jogos [18, 8, 0, 10, 25, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Andarahy tabela [18, 5, 2, 11, 27, 40] jogos [18, 5, 2, 11, 27, 41] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Carioca FC tabela [18, 1, 3, 14, 24, 63] jogos [20, 2, 3, 15, 30, 68] — a tabela conta 18 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PALMEIRAS
- PALMEIRAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-RJ)
- jogo só no ogol, incluído em Fase única: Andarahy 4-0 Villa Isabel (1919-07-20)
- jogo só no ogol, incluído em Fase única: Bangu 1-0 Andarahy (1919-12-25)
- só na RSSSF (não achado no ogol): Carioca FC 4-1 Palmeiras-RJ (1920-01-06)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 4-2 Carioca FC (1920-01-06)
- W.O. do ogol incluído: Bangu x Flamengo (1919-12-28), vitória do Bangu pela tabela publicada

### 1920

- W.O. do ogol incluído: Bangu x São Cristóvão (1920-12-12), vitória do Bangu pela tabela publicada

### 1921

- o desempate Flamengo x América foi 1-1 no tempo normal e 1-0 na prorrogação: fica 2-1 para o Flamengo
- tabela publicada x jogos — Final / -: Americano FC Rio tabela [12, 2, 4, 6, 17, 25] jogos [12, 3, 4, 5, 17, 25] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carioca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mackenzie
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mangueira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco
- Carioca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carioca FC)
- Mackenzie — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mackenzie-RJ)
- Mangueira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mangueira)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-RJ)
- Vasco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vasco)
- só na RSSSF (não achado no ogol): Vasco 2-0 Palmeiras-RJ (1921-04-03)
- só na RSSSF (não achado no ogol): Carioca FC 2-2 Americano FC Rio (1921-04-10)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-4 Villa Isabel (1921-04-10)
- só na RSSSF (não achado no ogol): Villa Isabel 4-1 Vasco (1921-04-17)
- só na RSSSF (não achado no ogol): Mangueira 3-1 Palmeiras-RJ (1921-04-17)
- só na RSSSF (não achado no ogol): Villa Isabel 4-6 Mackenzie-RJ (1921-04-24)
- só na RSSSF (não achado no ogol): Mangueira 1-2 Americano FC Rio (1921-04-24)
- só na RSSSF (não achado no ogol): Carioca FC 3-2 Mackenzie-RJ (1921-05-01)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-3 Palmeiras-RJ (1921-05-01)
- só na RSSSF (não achado no ogol): Mangueira 1-2 Villa Isabel (1921-05-08)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 2-0 Palmeiras-RJ (1921-05-08)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 2-2 Carioca FC (1921-05-15)
- só na RSSSF (não achado no ogol): Carioca FC 1-0 Villa Isabel (1921-05-22)
- só na RSSSF (não achado no ogol): Vasco 4-2 Mackenzie-RJ (1921-05-22)
- só na RSSSF (não achado no ogol): Mangueira 2-1 Carioca FC (1921-05-29)
- só na RSSSF (não achado no ogol): Villa Isabel 2-0 Americano FC Rio (1921-05-29)
- só na RSSSF (não achado no ogol): Vasco 0-0 Carioca FC (1921-06-05)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-1 Mackenzie-RJ (1921-06-05)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 3-0 Mangueira (1921-06-12)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-2 Vasco (1921-06-12)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-2 Carioca FC (1921-06-19)
- só na RSSSF (não achado no ogol): Vasco 1-2 Mangueira (1921-06-26)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-3 Carioca FC (1921-06-26)
- só na RSSSF (não achado no ogol): Villa Isabel 7-1 Palmeiras-RJ (1921-06-26)
- só na RSSSF (não achado no ogol): Vasco 3-2 Villa Isabel (1921-07-03)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-1 Mangueira (1921-07-03)
- só na RSSSF (não achado no ogol): Carioca FC 3-2 Vasco (1921-07-17)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 2-1 Mackenzie-RJ (1921-07-17)
- só na RSSSF (não achado no ogol): Mangueira 0-4 Vasco (1921-07-24)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-6 Villa Isabel (1921-07-24)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-5 Vasco (1921-08-07)
- só na RSSSF (não achado no ogol): Carioca FC 4-2 Palmeiras-RJ (1921-08-07)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-0 Mangueira (1921-08-07)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-5 Villa Isabel (1921-08-14)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 2-1 Americano FC Rio (1921-08-14)
- só na RSSSF (não achado no ogol): Carioca FC 4-2 Mangueira (1921-08-14)
- só na RSSSF (não achado no ogol): Villa Isabel 5-2 Mangueira (1921-08-21)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-1 Vasco (1921-08-21)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 2-2 Americano FC Rio (1921-08-21)
- só na RSSSF (não achado no ogol): Mangueira 1-3 Mackenzie-RJ (1921-08-28)
- só na RSSSF (não achado no ogol): Vasco 2-0 Americano FC Rio (1921-08-28)
- só na RSSSF (não achado no ogol): Villa Isabel 1-0 Carioca FC (1921-08-28)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-0 Palmeiras-RJ (1921-09-25)
- vencedor da final pelos jogos (Americano FC Rio) diferente do campeão oficial (Flamengo); fica o oficial

### 1922

- tabela publicada x jogos — Primeira fase / Série A: América-RJ tabela [12, 9, 0, 3, 19, 7] jogos [12, 9, 1, 2, 19, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Série A: Fluminense tabela [12, 7, 2, 3, 24, 12] jogos [12, 6, 3, 3, 24, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Série B: Carioca FC tabela [12, 5, 2, 5, 26, 34] jogos [12, 4, 2, 6, 26, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Série B: Mackenzie-RJ tabela [12, 0, 4, 8, 17, 27] jogos [12, 1, 4, 7, 17, 27] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carioca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mackenzie
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mangueira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Villa Isabel
- Carioca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carioca FC)
- Mackenzie — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mackenzie-RJ)
- Mangueira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mangueira)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-RJ)
- Villa Isabel — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Villa Isabel)
- só na RSSSF (não achado no ogol): Fluminense 0-0 América-RJ (1922-06-04)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 3-2 Mangueira (1922-04-02)
- só na RSSSF (não achado no ogol): Villa Isabel 2-0 Americano FC Rio (1922-04-02)
- só na RSSSF (não achado no ogol): Villa Isabel 3-0 Mangueira (1922-04-09)
- só na RSSSF (não achado no ogol): Carioca FC 1-1 Mackenzie-RJ (1922-04-16)
- só na RSSSF (não achado no ogol): Vasco 4-0 Palmeiras-RJ (1922-04-16)
- só na RSSSF (não achado no ogol): Americano FC Rio 3-2 Mangueira (1922-04-21)
- só na RSSSF (não achado no ogol): Carioca FC 2-0 Americano FC Rio (1922-04-23)
- só na RSSSF (não achado no ogol): Villa Isabel 1-0 Vasco (1922-04-23)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-0 Mackenzie-RJ (1922-04-23)
- só na RSSSF (não achado no ogol): Villa Isabel 2-1 Carioca FC (1922-04-30)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 0-3 Vasco (1922-04-30)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-1 Palmeiras-RJ (1922-05-03)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-2 Villa Isabel (1922-05-07)
- só na RSSSF (não achado no ogol): Carioca FC 2-1 Mangueira (1922-05-07)
- só na RSSSF (não achado no ogol): Villa Isabel 4-1 Palmeiras-RJ (1922-05-13)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 3-4 Mangueira (1922-05-13)
- só na RSSSF (não achado no ogol): Carioca FC 1-2 Vasco (1922-05-14)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-1 Vasco (1922-05-21)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-1 Carioca FC (1922-05-21)
- só na RSSSF (não achado no ogol): Vasco 2-1 Mangueira (1922-05-28)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-1 Mackenzie-RJ (1922-05-28)
- só na RSSSF (não achado no ogol): Vasco 2-1 Villa Isabel (1922-06-04)
- só na RSSSF (não achado no ogol): Carioca FC 6-4 Palmeiras-RJ (1922-06-04)
- só na RSSSF (não achado no ogol): Mangueira 1-2 Villa Isabel (1922-06-11)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 5-1 Carioca FC (1922-06-11)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 4-6 Americano FC Rio (1922-06-11)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-2 Villa Isabel (1922-06-18)
- só na RSSSF (não achado no ogol): Mangueira 2-5 Americano FC Rio (1922-06-18)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-1 Villa Isabel (1922-06-25)
- só na RSSSF (não achado no ogol): Vasco 3-0 Mackenzie-RJ (1922-06-25)
- só na RSSSF (não achado no ogol): Mangueira 2-4 Vasco (1922-07-02)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-4 Carioca FC (1922-07-02)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 2-2 Palmeiras-RJ (1922-07-02)
- só na RSSSF (não achado no ogol): Mangueira 2-2 Mackenzie-RJ (1922-07-09)
- só na RSSSF (não achado no ogol): Vasco 2-0 Americano FC Rio (1922-07-09)
- só na RSSSF (não achado no ogol): Carioca FC 2-3 Villa Isabel (1922-07-09)
- só na RSSSF (não achado no ogol): Mangueira 2-2 Palmeiras-RJ (1922-07-16)
- só na RSSSF (não achado no ogol): Villa Isabel 3-1 Mackenzie-RJ (1922-07-16)
- só na RSSSF (não achado no ogol): Vasco 8-3 Carioca FC (1922-07-16)
- só na RSSSF (não achado no ogol): Mangueira 5-2 Carioca FC (1922-07-23)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-4 Americano FC Rio (1922-07-23)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-5 Vasco (1922-07-23)
- W.O. do ogol incluído: Fluminense x América-RJ (1922-09-01), vitória do Fluminense pela tabela publicada
- campeão pela lista oficial, América-RJ; o 1º pela soma dos jogos da última fase é Vasco (desempate, jogo extra ou pontos tirados fora de campo)

### 1923

- tabela publicada x jogos — Primeira fase / Série A: Vasco tabela [14, 12, 1, 1, 32, 19] jogos [14, 12, 1, 1, 31, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Série A: Fluminense tabela [14, 5, 4, 5, 33, 26] jogos [13, 5, 3, 5, 31, 24] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / Série A: América-RJ tabela [14, 5, 3, 6, 20, 25] jogos [13, 5, 2, 6, 20, 25] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / Série A: Andarahy tabela [14, 3, 4, 7, 20, 29] jogos [12, 3, 2, 7, 17, 26] — a tabela conta 14 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carioca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mackenzie
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mangueira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): River
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SC Brasil
- Carioca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carioca FC)
- Mackenzie — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mackenzie-RJ)
- Mangueira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mangueira)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-RJ)
- River — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (River-RJ)
- SC Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SC Brasil-RJ)
- só na RSSSF (não achado no ogol): River-RJ 2-2 Villa Isabel (1923-04-15)
- só na RSSSF (não achado no ogol): Americano FC Rio 0-1 Mackenzie-RJ (1923-04-15)
- só na RSSSF (não achado no ogol): Carioca FC 7-2 Americano FC Rio (1923-04-22)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 4-1 Palmeiras-RJ (1923-04-22)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-1 River-RJ (1923-04-22)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-4 Mangueira (1923-04-29)
- só na RSSSF (não achado no ogol): River-RJ 2-0 SC Brasil-RJ (1923-04-29)
- só na RSSSF (não achado no ogol): Villa Isabel 1-0 Carioca FC (1923-04-29)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 3-2 Villa Isabel (1923-05-06)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 6-0 Americano FC Rio (1923-05-06)
- só na RSSSF (não achado no ogol): Villa Isabel 3-1 Palmeiras-RJ (1923-05-13)
- só na RSSSF (não achado no ogol): River-RJ 1-1 Mangueira (1923-05-13)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 1-2 Carioca FC (1923-05-13)
- só na RSSSF (não achado no ogol): Carioca FC 5-0 Palmeiras-RJ (1923-05-20)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-6 Mangueira (1923-05-20)
- só na RSSSF (não achado no ogol): Villa Isabel 3-1 SC Brasil-RJ (1923-05-20)
- só na RSSSF (não achado no ogol): Mangueira 1-0 Carioca FC (1923-05-27)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 3-4 SC Brasil-RJ (1923-05-27)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-3 River-RJ (1923-05-27)
- só na RSSSF (não achado no ogol): River-RJ 3-2 Americano FC Rio (1923-06-03)
- só na RSSSF (não achado no ogol): Mangueira 1-0 Mackenzie-RJ (1923-06-03)
- só na RSSSF (não achado no ogol): Carioca FC 7-2 SC Brasil-RJ (1923-06-10)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 1-2 Americano FC Rio (1923-06-10)
- só na RSSSF (não achado no ogol): Mangueira 0-0 Villa Isabel (1923-06-10)
- só na RSSSF (não achado no ogol): Americano FC Rio 1-4 Villa Isabel (1923-06-17)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-2 Mackenzie-RJ (1923-06-17)
- só na RSSSF (não achado no ogol): Carioca FC 3-1 River-RJ (1923-06-17)
- só na RSSSF (não achado no ogol): Mangueira 2-1 SC Brasil-RJ (1923-06-17)
- só na RSSSF (não achado no ogol): Villa Isabel 4-0 River-RJ (1923-06-25)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 7-1 Americano FC Rio (1923-06-25)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 2-1 SC Brasil-RJ (1923-07-01)
- só na RSSSF (não achado no ogol): River-RJ 3-5 Mackenzie-RJ (1923-07-01)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-3 Carioca FC (1923-07-01)
- só na RSSSF (não achado no ogol): Carioca FC 1-2 Villa Isabel (1923-07-08)
- só na RSSSF (não achado no ogol): Mangueira 1-2 Palmeiras-RJ (1923-07-08)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 2-0 River-RJ (1923-07-08)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-1 SC Brasil-RJ (1923-07-14)
- só na RSSSF (não achado no ogol): Villa Isabel 4-3 Mackenzie-RJ (1923-07-14)
- só na RSSSF (não achado no ogol): Mangueira 3-1 River-RJ (1923-07-22)
- só na RSSSF (não achado no ogol): Carioca FC 3-1 Mackenzie-RJ (1923-07-22)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-3 Villa Isabel (1923-07-22)
- só na RSSSF (não achado no ogol): Mangueira 2-0 Americano FC Rio (1923-07-29)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 3-2 Villa Isabel (1923-07-29)
- só na RSSSF (não achado no ogol): Palmeiras-RJ 0-0 Carioca FC (1923-07-29)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 2-3 Mackenzie-RJ (1923-08-05)
- só na RSSSF (não achado no ogol): River-RJ 1-1 Palmeiras-RJ (1923-08-05)
- só na RSSSF (não achado no ogol): Carioca FC 1-3 Mangueira (1923-08-05)
- só na RSSSF (não achado no ogol): River-RJ 3-0 Americano FC Rio (1923-08-12)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 1-5 Carioca FC (1923-08-12)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 2-0 Mangueira (1923-08-12)
- só na RSSSF (não achado no ogol): Americano FC Rio 2-3 Palmeiras-RJ (1923-08-19)
- só na RSSSF (não achado no ogol): River-RJ 2-0 Carioca FC (1923-08-19)
- só na RSSSF (não achado no ogol): Villa Isabel 2-2 Mangueira (1923-08-19)
- só na RSSSF (não achado no ogol): SC Brasil-RJ 0-1 Mangueira (1923-08-26)
- só na RSSSF (não achado no ogol): Mackenzie-RJ 4-0 Palmeiras-RJ (1923-08-26)
- só na RSSSF (não achado no ogol): Villa Isabel 10-0 Americano FC Rio (1923-08-26)
- só na RSSSF (não achado no ogol): Villa Isabel 3-2 Mangueira (1923-09-20)
- W.O. do ogol incluído: Vasco x Andarahy (1923-04-15), vitória do Vasco pela tabela publicada
- W.O. do ogol incluído: Andarahy x São Cristóvão (1923-04-22), vitória do São Cristóvão pela tabela publicada
- W.O. do ogol incluído: Andarahy x Botafogo (1923-08-26), vitória do Andarahy pela tabela publicada
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Andarahy x America-RJ (1923-04-29)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Andarahy x Fluminense (1923-07-22)

### 1924 LMDT

- tabela publicada x jogos — Primeira fase / Série A: Americano FC Rio tabela [14, 4, 2, 8, 20, 24] jogos [13, 3, 2, 8, 20, 24] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / Série A: Progresso-RJ tabela [14, 0, 2, 12, 11, 32] jogos [13, 0, 2, 11, 11, 32] — a tabela conta 14 jogos e as fontes trazem 13
- W.O. do ogol incluído: Engenho de Dentro x Independência-RJ (1924-07-27), vitória do Engenho de Dentro pela tabela publicada
- W.O. do ogol incluído: Modesto x Olaria (1924-10-12), vitória do Modesto pela tabela publicada
- W.O. do ogol incluído: SC Everest-RJ x Olaria (1924-10-19), vitória do SC Everest-RJ pela tabela publicada
- W.O. do ogol incluído: Campo Grande-RJ x Independência-RJ (1924-10-26), vitória do Campo Grande-RJ pela tabela publicada
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Confiança-RJ x Americano FC Rio (1924-10-26)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Carioca FC x Villa Isabel (1924-11-02)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Progresso x São Paulo-Rio (1924-11-02)

### 1924 AMEA

- só na RSSSF (não achado no ogol): Fluminense 7-0 SC Brasil-RJ (1924-10-19)

### 1925

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ENGENHO DE DENTRO AC
- ENGENHO DE DENTRO AC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Engenho de Dentro)
- placar diferente no ogol — SC Brasil-RJ x Fluminense (1925-05-24): RSSSF 2-6, ogol 1-6; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: Fluminense 2-0 América-RJ (1925-11-01)
- jogo só no ogol, incluído em Fase única: Botafogo 2-0 Bangu (1925-12-20)
- só na RSSSF (não achado no ogol): Engenho de Dentro 5-0 Americano FC Rio (1925-12-20)

### 1926

- tabela publicada x jogos — Fase única / -: São Cristóvão tabela [18, 14, 2, 2, 70, 37] jogos [19, 14, 2, 3, 71, 40] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase única / -: Flamengo tabela [18, 7, 5, 6, 53, 40] jogos [19, 8, 5, 6, 56, 41] — a tabela conta 18 jogos e as fontes trazem 19
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Vasco x Flamengo, ogol 1926-06-12); fica a do ogol
- só na RSSSF (não achado no ogol): Flamengo 3-1 São Cristóvão (1926-08-01)

### 1927

- sem ocorrências

### 1928

- tabela publicada x jogos — 2º Turno / -: América-RJ tabela [19, 14, 4, 1, 53, 24] jogos [18, 14, 3, 1, 51, 22] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Vasco tabela [19, 12, 4, 3, 43, 17] jogos [18, 11, 4, 3, 39, 17] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Botafogo tabela [19, 10, 4, 5, 55, 32] jogos [18, 9, 4, 5, 53, 30] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [19, 11, 1, 7, 41, 32] jogos [17, 9, 1, 7, 33, 31] — a tabela conta 19 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [19, 7, 1, 11, 37, 36] jogos [19, 7, 2, 10, 37, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: SC Brasil-RJ tabela [19, 2, 3, 14, 20, 49] jogos [18, 2, 3, 13, 20, 49] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Villa Isabel tabela [19, 2, 1, 16, 23, 80] jogos [17, 2, 1, 14, 22, 68] — a tabela conta 19 jogos e as fontes trazem 17
- jogo anulado fica de fora (1): SC AMÉRICA 1-0 CAMPO GRANDE AC — decisão da série de subúrbio (SC América, não o America FC); outra divisão
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Fluminense x Syrio e Libanez, ogol 1928-09-23); fica a do ogol
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 São Cristóvão (1928-04-15)
- jogo só no ogol, incluído em 1º Turno: Fluminense 8-1 Villa Isabel (1928-04-15)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 SC Brasil-RJ (1928-04-22)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Bangu (1928-04-29)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Fluminense (1928-05-06)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 América-RJ (1928-05-13)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Flamengo (1928-05-20)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Vasco (1928-05-27)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Villa Isabel (1928-06-03)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Botafogo (1928-06-10)
- jogo só no ogol, incluído em 1º Turno: Syrio e Libanez 0-1 Andarahy (1928-06-17)
- jogo só no ogol, incluído em 2º Turno: Fluminense 1-0 SC Brasil-RJ (1928-08-12)
- jogo só no ogol, incluído em 2º Turno: América-RJ 2-2 Botafogo (1928-09-30)
- jogo só no ogol, incluído em 2º Turno: Vasco 4-0 Villa Isabel (1928-10-07)
- campeão pela lista oficial, América-RJ; o 1º pela soma dos jogos da última fase é Vasco (desempate, jogo extra ou pontos tirados fora de campo)

### 1929

- tabela publicada x jogos — Fase única / -: América-RJ tabela [20, 15, 3, 2, 66, 21] jogos [21, 16, 3, 2, 67, 21] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase única / -: Botafogo tabela [20, 8, 4, 8, 55, 54] jogos [21, 8, 4, 9, 55, 55] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase única / -: Bonsucesso tabela [20, 5, 5, 10, 34, 55] jogos [20, 5, 5, 10, 39, 56] — placar diverge entre RSSSF e ogol em Fluminense x Bonsucesso (3-1 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: SC Brasil-RJ tabela [20, 1, 2, 17, 20, 66] jogos [20, 1, 2, 17, 21, 71] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado fica de fora (1): SC AMÉRICA 3-2 MAVILIS FC — final da série de subúrbio (SC América, não o America FC); outra divisão
- placar diferente no ogol — Fluminense x Bonsucesso (1929-05-12): RSSSF 3-1, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — América-RJ x Botafogo (1929-11-03): RSSSF 1-0, ogol 11-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-RJ x Botafogo, ogol 1929-11-03); fica a do ogol
- só na RSSSF (não achado no ogol): América-RJ 11-2 Botafogo (1929-11-03)
- campeão pela lista oficial, Vasco; o 1º pela soma dos jogos da última fase é América-RJ (desempate, jogo extra ou pontos tirados fora de campo)

### 1930

- tabela publicada x jogos — Fase única / -: América-RJ tabela [20, 11, 5, 4, 47, 33] jogos [21, 11, 6, 4, 50, 36] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase única / -: Fluminense tabela [20, 10, 3, 7, 39, 36] jogos [21, 10, 4, 7, 42, 39] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase única / -: Andarahy tabela [20, 3, 3, 14, 27, 53] jogos [20, 3, 3, 14, 27, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado fica de fora (1): GS SANTA CRUZ 2-0 SC AMÉRICA — final da série de subúrbio (GS Santa Cruz x SC América); outra divisão
- placar diferente no ogol — América-RJ x Fluminense (1930-12-28): RSSSF 3-3, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-RJ x Fluminense, ogol 1930-12-28); fica a do ogol
- só na RSSSF (não achado no ogol): América-RJ 1-1 Fluminense (1930-12-28)

### 1931

- tabela publicada x jogos — Fase única / -: Flamengo tabela [20, 10, 1, 9, 30, 46] jogos [20, 10, 1, 9, 33, 48] — placar diverge entre RSSSF e ogol em SC Brasil-RJ x Flamengo (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: SC Brasil-RJ tabela [20, 4, 6, 10, 30, 46] jogos [20, 4, 6, 10, 32, 49] — placar diverge entre RSSSF e ogol em SC Brasil-RJ x Flamengo (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Andarahy tabela [20, 4, 2, 14, 33, 51] jogos [22, 4, 3, 15, 34, 55] — a tabela conta 20 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase única / -: Carioca FC tabela [20, 4, 2, 14, 31, 63] jogos [22, 5, 3, 14, 35, 64] — a tabela conta 20 jogos e as fontes trazem 22
- jogo só no ogol, incluído em Fase única: Carioca FC 1-0 Andarahy (1930-12-27)
- jogo só no ogol, incluído em Fase única: São Cristóvão 3-4 Flamengo (1931-12-06)
- jogo só no ogol, incluído em Fase única: Carioca FC 3-1 Andarahy (1932-01-03)
- W.O. do ogol incluído: São Cristóvão x América-RJ (1931-11-29), vitória do América-RJ pela tabela publicada

### 1932

- tabela publicada x jogos — Fase única / -: Vasco tabela [22, 9, 5, 8, 52, 43] jogos [23, 10, 5, 8, 54, 44] — a tabela conta 22 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase única / -: SC Brasil-RJ tabela [22, 2, 5, 15, 34, 66] jogos [23, 2, 5, 16, 35, 68] — a tabela conta 22 jogos e as fontes trazem 23
- placar diferente no ogol — SC Brasil-RJ x Vasco (1932-06-02): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: SC Brasil-RJ x Vasco, ogol 1932-06-02); fica a do ogol
- só na RSSSF (não achado no ogol): SC Brasil-RJ 1-1 Vasco (1932-06-02)

### 1933 AMEA

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carioca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- Carioca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carioca FC)
- Flamengo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão)
- jogo só no ogol, incluído em Fase única: Engenho de Dentro 1-2 Andarahy (1933-04-30)
- só na RSSSF (não achado no ogol): Flamengo 2-2 Olaria (1933-04-30)
- só na RSSSF (não achado no ogol): River-RJ 4-5 Carioca FC (1933-04-30)
- só na RSSSF (não achado no ogol): São Cristóvão 6-3 SC Brasil-RJ (1933-05-07)
- só na RSSSF (não achado no ogol): Carioca FC 2-3 Flamengo (1933-05-07)
- só na RSSSF (não achado no ogol): Flamengo 16-2 River-RJ (1933-05-14)
- só na RSSSF (não achado no ogol): Engenho de Dentro 2-1 Carioca FC (1933-05-14)
- só na RSSSF (não achado no ogol): Andarahy 3-2 São Cristóvão (1933-05-14)
- só na RSSSF (não achado no ogol): River-RJ 1-5 São Cristóvão (1933-05-21)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: River-RJ x Cocotá (1933-11-12)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: SC Brasil x River-RJ (1933-11-19)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Cocotá x Mavilis (1933-12-03)

### 1933 LCF

- tabela publicada x jogos — Fase única / -: Bonsucesso tabela [10, 4, 2, 4, 16, 23] jogos [10, 4, 2, 4, 14, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Flamengo tabela [10, 2, 1, 7, 13, 20] jogos [10, 2, 1, 7, 11, 18] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF Bangu 4-3 Bonsucesso, ogol Bonsucesso 3-4 Bangu (1933-06-11); fica a RSSSF
- jogo só no ogol, incluído em and Torneio Rio-São Paulo: América-RJ 1-3 Vasco (1933-11-12)
- jogo só no ogol, incluído em and Torneio Rio-São Paulo: Bangu 4-0 Fluminense (1933-11-12)
- W.O. do ogol incluído: Flamengo x Bonsucesso (1933-11-05), vitória do Bonsucesso pela tabela publicada

### 1934 AMEA

- tabela publicada x jogos — Fase única / -: Botafogo tabela [8, 6, 1, 1, 21, 10] jogos [11, 7, 2, 2, 31, 17] — a tabela conta 8 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Mavilis tabela [8, 4, 1, 3, 24, 21] jogos [10, 5, 1, 4, 29, 26] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Andarahy tabela [8, 3, 3, 2, 17, 14] jogos [12, 6, 3, 3, 32, 21] — a tabela conta 8 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Olaria tabela [8, 3, 1, 4, 10, 13] jogos [11, 6, 1, 4, 23, 18] — a tabela conta 8 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Portuguesa-RJ tabela [8, 1, 0, 7, 8, 22] jogos [12, 2, 1, 9, 18, 35] — a tabela conta 8 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Andarahy tabela [12, 7, 3, 2, 32, 18] jogos [12, 6, 3, 3, 32, 21] — placar diverge entre RSSSF e ogol em Andarahy x Portuguesa-RJ (0-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Mavilis tabela [11, 6, 1, 4, 29, 26] jogos [10, 5, 1, 4, 29, 26] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Portuguesa-RJ tabela [12, 1, 1, 10, 15, 35] jogos [12, 2, 1, 9, 18, 35] — placar diverge entre RSSSF e ogol em Andarahy x Portuguesa-RJ (0-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: SC Brasil x Cocotá (1934-04-15)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Mavilis x River-RJ (1934-06-10)

### 1934 LCF

- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 0-1 São Cristóvão (1934-04-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 2-1 América-RJ (1934-04-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 6-2 Bangu (1934-04-05)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-3 Flamengo (1934-04-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 2-0 Bangu (1934-04-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 2-0 Bonsucesso (1934-04-12)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 1-2 América-RJ (1934-04-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-3 Fluminense (1934-04-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 1-2 Bonsucesso (1934-04-19)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 8-2 Bonsucesso (1934-04-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 0-1 São Cristóvão (1934-04-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-2 América-RJ (1934-04-26)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 4-1 Bonsucesso (1934-04-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-3 Bangu (1934-04-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 5-2 Flamengo (1934-05-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-2 Vasco (1934-05-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 1-2 Bangu (1934-05-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 3-4 São Cristóvão (1934-05-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-1 Bonsucesso (1934-05-12)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 4-3 Flamengo (1934-05-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 1-1 São Cristóvão (1934-05-20)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 2-2 Vasco (1934-05-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-0 Bonsucesso (1934-05-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-3 Bangu (1934-06-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 3-4 Vasco (1934-06-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-2 Fluminense (1934-06-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-0 São Cristóvão (1934-06-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 1-1 Flamengo (1934-06-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 5-2 Bangu (1934-06-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 2-4 Bangu (1934-07-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-1 Vasco (1934-07-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-3 Fluminense (1934-07-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 2-7 Flamengo (1934-07-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 4-1 América-RJ (1934-07-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-1 Bangu (1934-07-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 3-2 Vasco (1934-07-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 0-5 América-RJ (1934-07-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 2-1 Flamengo (1934-07-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 1-0 Fluminense (1934-07-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 2-2 Fluminense (1934-08-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 1-2 Bangu (1934-08-05)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 1-1 América-RJ (1934-08-12)

### 1935 FMD

- tabela publicada x jogos — Fase única / -: Botafogo tabela [21, 15, 4, 2, 70, 42] jogos [24, 17, 5, 2, 76, 44] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Vasco tabela [21, 14, 4, 3, 59, 22] jogos [22, 14, 5, 3, 70, 23] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase única / -: Andarahy tabela [21, 7, 7, 7, 52, 52] jogos [22, 8, 7, 7, 57, 53] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase única / -: Bangu tabela [21, 6, 7, 8, 55, 62] jogos [23, 7, 7, 9, 62, 66] — a tabela conta 21 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase única / -: Carioca FC tabela [21, 5, 4, 12, 30, 47] jogos [21, 6, 4, 11, 32, 47] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SC Brasil
- SC Brasil — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SC Brasil-RJ)
- placar diferente no ogol — Botafogo x Bangu (1935-11-24): RSSSF 2-1, ogol 6-4; fica o da RSSSF
- placar diferente no ogol — Vasco x Botafogo (1935-10-06): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Botafogo x Bangu, ogol 1935-11-24); fica a do ogol
- jogo só no ogol, incluído em Fase única: Botafogo 3-0 São Cristóvão (1935-06-09)
- jogo só no ogol, incluído em Fase única: São Cristóvão 0-0 Bangu (1935-12-26)
- jogo só no ogol, incluído em Fase única: São Cristóvão 4-6 Botafogo (1935-12-29)
- jogo só no ogol, incluído em Fase única: Vasco 8-1 Olaria (1935-12-29)
- só na RSSSF (não achado no ogol): Carioca FC 2-0 SC Brasil-RJ (1935-05-12)
- só na RSSSF (não achado no ogol): Andarahy 5-1 SC Brasil-RJ (1935-05-19)
- só na RSSSF (não achado no ogol): Botafogo 3-0 SC Brasil-RJ (1935-05-26)
- só na RSSSF (não achado no ogol): Bangu 6-2 SC Brasil-RJ (1935-06-09)
- só na RSSSF (não achado no ogol): Vasco 10-0 SC Brasil-RJ (1935-06-16)
- só na RSSSF (não achado no ogol): Vasco 0-1 Botafogo (1935-10-06)
- só na RSSSF (não achado no ogol): Botafogo 6-4 Bangu (1935-11-24)
- W.O. do ogol incluído: Madureira x Carioca FC (1935-12-29), vitória do Madureira pela tabela publicada
- W.O. do ogol incluído: Olaria x Carioca FC (1936-01-12), vitória do Olaria pela tabela publicada
- W.O. do ogol incluído: São Cristóvão x Carioca FC (1936-01-26), vitória do São Cristóvão pela tabela publicada
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Vasco x Carioca FC (1936-01-23)

### 1935 LCF

- tabela publicada x jogos — Fase única / -: Modesto tabela [15, 2, 1, 12, 19, 56] jogos [15, 3, 1, 11, 19, 56] — placar diverge entre RSSSF e ogol em Portuguesa-RJ x Modesto (3-4 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Portuguesa-RJ tabela [15, 2, 0, 13, 25, 64] jogos [15, 1, 0, 14, 25, 64] — placar diverge entre RSSSF e ogol em Portuguesa-RJ x Modesto (3-4 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- jogo só no ogol, incluído em Fase única: Fluminense 2-2 Flamengo (1935-07-21)
- jogo só no ogol, incluído em Fase única: América-RJ 2-1 Bonsucesso (1935-07-21)
- jogo só no ogol, incluído em Fase única: Flamengo 6-1 Portuguesa-RJ (1935-07-28)

### 1936 FMD

- jogo só no ogol, incluído em 1º Turno: Vasco 2-0 São Cristóvão (1936-09-13)

### 1936 LCF

- sem ocorrências

### 1937

- torneio da LFRJ (a liga da pacificação: FMD e LCF juntas), campeão o Fluminense. O torneio da FMD, disputado antes, é a edição "1937 FMD"

### 1937 FMD

- torneio da FMD, que parou na 8ª rodada (26 jogos, de 02/05 a 11/07) com a pacificação entre a FMD e a LCF; os jogos não foram anulados. A FMD proclamou o São Cristóvão campeão em 03/09/1937 (invicto, 7 vitórias em 7 jogos); o título ficou esquecido e a FERJ o homologou em dezembro de 2023, depois do dossiê do jornalista André Luiz Pereira Nunes (cerimônia em 13/01/2024; Super Rádio Tupi, 09/01/2024). A lista de campeões da RSSSF é de antes e ainda diz "unfinished": o campeão vem de importar.CAMPEOES_MANUAIS. O ogol não tem essa edição; os jogos vêm só da RSSSF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Andarahy
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bangu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carioca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Madureira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olaria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco
- Andarahy — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Andarahy)
- Bangu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bangu)
- Botafogo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo)
- Carioca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carioca FC)
- Madureira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Madureira)
- Olaria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olaria)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão)
- Vasco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vasco)

### 1938

- tabela publicada x jogos — Fase única / -: Botafogo tabela [16, 8, 3, 5, 44, 27] jogos [16, 9, 3, 4, 44, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Bonsucesso tabela [16, 3, 4, 9, 29, 68] jogos [16, 2, 4, 10, 29, 68] — há jogo do clube sem conferência no ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Fluminense x América-RJ, ogol 1938-12-30); fica a do ogol
- jogo só no ogol, incluído em Fase única: São Cristóvão 3-3 Bonsucesso (1939-01-01)

### 1939

- sem ocorrências

### 1940

- sem ocorrências

### 1941

- tabela publicada x jogos — 4º Turno / -: Fluminense tabela [10, 8, 1, 1, 41, 14] jogos [28, 22, 1, 5, 106, 48] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 4º Turno / -: Vasco tabela [10, 6, 2, 2, 23, 11] jogos [28, 15, 7, 6, 69, 39] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 4º Turno / -: Botafogo tabela [10, 6, 1, 3, 25, 23] jogos [28, 18, 3, 7, 91, 65] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 4º Turno / -: Flamengo tabela [10, 5, 2, 3, 24, 17] jogos [28, 20, 4, 4, 85, 32] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 4º Turno / -: Madureira tabela [10, 1, 0, 9, 16, 39] jogos [28, 8, 1, 19, 59, 84] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 4º Turno / -: Bangu tabela [10, 1, 0, 9, 22, 47] jogos [28, 7, 2, 19, 57, 99] — a tabela conta 10 jogos e as fontes trazem 28
- mando invertido no ogol — RSSSF Fluminense 3-0 São Cristóvão, ogol São Cristóvão 0-3 Fluminense (1941-05-17); fica a RSSSF
- mando invertido no ogol — RSSSF São Cristóvão 0-9 Fluminense, ogol Fluminense 9-0 São Cristóvão (1941-07-20); fica a RSSSF
- campeão pela lista oficial, Fluminense; o 1º pela soma dos jogos da última fase é Vasco (desempate, jogo extra ou pontos tirados fora de campo)

### 1942

- sem ocorrências

### 1943

- jogo só no ogol, incluído em Fase única: Flamengo 2-1 Madureira (1943-06-13)
- jogo só no ogol, incluído em Fase única: Fluminense 6-2 Bangu (1943-06-17)

### 1944

- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-3 Fluminense (1944-07-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 2-1 Flamengo (1944-07-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-0 Bonsucesso (1944-07-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 5-1 Bangu (1944-07-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 2-1 São Cristóvão (1944-07-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 7-1 Madureira (1944-07-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 2-2 Canto do Rio (1944-07-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 2-0 Bonsucesso (1944-07-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 4-1 Botafogo (1944-07-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 6-1 Bangu (1944-07-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-0 América-RJ (1944-07-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-2 São Cristóvão (1944-07-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-1 Madureira (1944-07-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-2 Bangu (1944-07-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 3-1 Bonsucesso (1944-07-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-0 Botafogo (1944-07-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-0 Canto do Rio (1944-07-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 8-1 Bonsucesso (1944-07-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 5-1 América-RJ (1944-07-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 3-3 Bangu (1944-07-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-2 América-RJ (1944-07-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 4-2 Bangu (1944-07-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 5-2 São Cristóvão (1944-07-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 6-1 Bonsucesso (1944-07-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 2-1 Madureira (1944-07-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-0 Bangu (1944-08-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 1-0 Madureira (1944-08-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 4-1 Bonsucesso (1944-08-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 5-1 Botafogo (1944-08-06)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-1 São Cristóvão (1944-08-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-2 São Cristóvão (1944-08-12)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 4-1 Bangu (1944-08-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 2-2 Madureira (1944-08-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 2-1 Vasco (1944-08-13)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-1 Bonsucesso (1944-08-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 0-0 Fluminense (1944-08-19)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 4-1 Bonsucesso (1944-08-20)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 4-2 América-RJ (1944-08-20)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-0 São Cristóvão (1944-08-20)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 7-2 Bangu (1944-08-20)
- jogo só no ogol, incluído em 2º Turno: Vasco 2-1 Flamengo (1944-08-26)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-2 Canto do Rio (1944-08-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 1-1 Botafogo (1944-08-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 2-0 Madureira (1944-08-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 3-1 Bonsucesso (1944-08-27)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-1 Vasco (1944-09-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-0 Bonsucesso (1944-09-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 4-1 América-RJ (1944-09-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 3-0 Canto do Rio (1944-09-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 3-1 Bangu (1944-09-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 1-0 São Cristóvão (1944-09-09)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 5-2 Flamengo (1944-09-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 3-1 Madureira (1944-09-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-1 Canto do Rio (1944-09-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-3 Bangu (1944-09-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 2-1 Fluminense (1944-09-16)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 3-1 Madureira (1944-09-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-1 Bangu (1944-09-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 1-1 Bonsucesso (1944-09-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 3-0 São Cristóvão (1944-09-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 6-1 Bonsucesso (1944-09-23)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 4-3 São Cristóvão (1944-09-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 1-1 Botafogo (1944-09-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-1 Canto do Rio (1944-09-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-1 Madureira (1944-09-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: São Cristóvão 2-0 Fluminense (1944-09-30)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-2 Vasco (1944-10-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-0 Bonsucesso (1944-10-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 5-1 Madureira (1944-10-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 3-2 Canto do Rio (1944-10-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 1-0 São Cristóvão (1944-10-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 3-0 Canto do Rio (1944-10-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 3-2 Fluminense (1944-10-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 5-1 Bonsucesso (1944-10-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 2-0 Madureira (1944-10-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 1-0 Botafogo (1944-10-14)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 6-1 Bonsucesso (1944-10-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 3-0 São Cristóvão (1944-10-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Canto do Rio 3-2 Madureira (1944-10-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 7-1 Bangu (1944-10-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 4-3 Bangu (1944-10-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 6-1 Fluminense (1944-10-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-0 São Cristóvão (1944-10-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: América-RJ 1-1 Canto do Rio (1944-10-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bonsucesso 3-3 Madureira (1944-10-22)
- jogo só no ogol, incluído em 2º Turno: Fluminense 4-1 Canto do Rio (1944-10-28)
- jogo só no ogol, incluído em 2º Turno: Madureira 4-1 São Cristóvão (1944-10-29)
- jogo só no ogol, incluído em 2º Turno: Botafogo 3-0 América-RJ (1944-10-29)
- jogo só no ogol, incluído em 2º Turno: Bonsucesso 5-4 Bangu (1944-10-29)
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é Fluminense (desempate, jogo extra ou pontos tirados fora de campo)

### 1945

- jogo só no ogol, incluído em Fase única: Madureira 0-4 Flamengo (1945-07-22)
- jogo só no ogol, incluído em Fase única: Botafogo 1-1 Fluminense (1945-07-22)
- jogo só no ogol, incluído em Fase única: Canto do Rio 1-2 América-RJ (1945-07-22)
- jogo só no ogol, incluído em Fase única: São Cristóvão 1-1 Bangu (1945-07-22)
- jogo só no ogol, incluído em Fase única: Bonsucesso 0-2 Canto do Rio (1945-07-29)

### 1946

- tabela publicada x jogos — Fase única / -: Fluminense tabela [18, 13, 0, 5, 74, 36] jogos [24, 18, 1, 5, 97, 45] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Botafogo tabela [18, 11, 4, 3, 58, 25] jogos [24, 15, 4, 5, 65, 30] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Flamengo tabela [18, 12, 2, 4, 72, 33] jogos [24, 14, 3, 7, 81, 45] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: América-RJ tabela [18, 13, 0, 5, 51, 32] jogos [24, 13, 0, 11, 61, 55] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: São Cristóvão tabela [18, 9, 2, 7, 38, 32] jogos [18, 8, 3, 7, 38, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Madureira tabela [18, 3, 2, 13, 31, 64] jogos [18, 3, 3, 12, 31, 64] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Fluminense tabela [6, 5, 1, 0, 23, 9] jogos [24, 18, 1, 5, 97, 45] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Botafogo tabela [6, 4, 0, 2, 7, 5] jogos [24, 15, 4, 5, 65, 30] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Flamengo tabela [6, 2, 1, 3, 9, 12] jogos [24, 14, 3, 7, 81, 45] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: América-RJ tabela [6, 0, 0, 6, 10, 23] jogos [24, 13, 0, 11, 61, 55] — a tabela conta 6 jogos e as fontes trazem 24
- jogo só no ogol, incluído em Fase única: Canto do Rio 3-2 América-RJ (1946-07-07)
- jogo só no ogol, incluído em Fase única: Botafogo 0-3 Vasco (1946-07-07)
- jogo só no ogol, incluído em Fase única: Vasco 2-6 Bangu (1946-07-13)
- jogo só no ogol, incluído em Fase única: Fluminense 5-0 Canto do Rio (1946-07-14)

### 1947

- sem ocorrências

### 1948

- tabela publicada x jogos — Fase única / -: América-RJ tabela [20, 8, 2, 10, 31, 39] jogos [20, 7, 2, 11, 31, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em Fase única: Bonsucesso 1-3 Flamengo (1948-09-18)

### 1949

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: São Cristóvão x Botafogo, ogol 1949-09-11); fica a do ogol

### 1950

- sem ocorrências

### 1951

- sem ocorrências

### 1952

- placar diferente no ogol — Fluminense x Bonsucesso (1952-11-16): RSSSF 6-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Botafogo x Olaria (1953-01-04): RSSSF 3-2, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Olaria x Flamengo (1952-11-16): RSSSF 2-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Bonsucesso x América-RJ (1952-11-30): RSSSF 4-2, ogol 0-4; fica o da RSSSF
- placar diferente no ogol — Fluminense x Madureira (1952-11-23): RSSSF 3-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Vasco x Olaria (1953-01-20): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Bangu x Bonsucesso (1952-11-09): RSSSF 4-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Flamengo x São Cristóvão (1952-11-29): RSSSF 9-0, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Fluminense x Olaria (1953-01-17): RSSSF 3-1, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Botafogo x Bonsucesso (1952-11-22): RSSSF 3-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Madureira x Bonsucesso (1952-12-21): RSSSF 6-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Vasco x São Cristóvão (1952-11-09): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Madureira x Fluminense (1952-09-07): RSSSF 2-1, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — América-RJ x Bonsucesso (1952-09-06): RSSSF 4-0, ogol 2-4; fica o da RSSSF
- mando invertido no ogol — RSSSF América-RJ 5-2 Olaria, ogol Olaria 2-5 América-RJ (1952-11-09); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-0 Madureira, ogol Madureira 0-2 Flamengo (1952-11-09); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 7-1 Canto do Rio, ogol Canto do Rio 1-7 Bangu (1952-11-16); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Canto do Rio, ogol Canto do Rio 0-1 Vasco (1952-11-23); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-0 Canto do Rio, ogol Canto do Rio 0-3 Fluminense (1952-11-30); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 2-1 Madureira, ogol Madureira 1-2 Olaria (1952-11-30); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-0 Madureira, ogol Madureira 0-3 Vasco (1952-12-07); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-0 Bangu, ogol Bangu 0-3 Flamengo (1952-12-07); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-1 Botafogo, ogol Botafogo 1-3 Fluminense (1952-12-13); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 4-2 São Cristóvão, ogol São Cristóvão 2-4 Bangu (1952-12-13); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 4-3 Canto do Rio, ogol Canto do Rio 3-4 Madureira (1952-12-13); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Flamengo, ogol Flamengo 0-1 Vasco (1952-12-14); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 5-2 São Cristóvão, ogol São Cristóvão 2-5 Fluminense (1952-12-21); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-0 Canto do Rio, ogol Canto do Rio 0-2 Flamengo (1952-12-21); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 América-RJ, ogol América-RJ 0-2 Vasco (1952-12-28); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 4-1 Bonsucesso, ogol Bonsucesso 1-4 Vasco (1953-01-03); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 6-3 Botafogo, ogol Botafogo 3-6 Flamengo (1953-01-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-2 Madureira, ogol Madureira 2-3 Bangu (1953-01-10); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 4-1 Canto do Rio, ogol Canto do Rio 1-4 América-RJ (1953-01-11); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 5-2 Bonsucesso, ogol Bonsucesso 2-5 Flamengo (1953-01-12); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-0 América-RJ, ogol América-RJ 0-3 Botafogo (1953-01-17); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-1 Bangu, ogol Bangu 1-2 Vasco (1953-01-18); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 5-3 Madureira, ogol Madureira 3-5 Botafogo (1953-01-20); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-1 Fluminense, ogol Fluminense 1-3 Flamengo (1953-01-20); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-1 América-RJ, ogol América-RJ 1-2 Bangu (1953-01-22); fica a RSSSF
- jogo só no ogol, incluído em 1º TURNO: Olaria 2-3 Botafogo (1952-08-24)
- jogo só no ogol, incluído em 1º TURNO: Bonsucesso 1-6 Fluminense (1952-08-24)
- jogo só no ogol, incluído em 1º TURNO: Flamengo 1-2 Olaria (1952-08-31)
- jogo só no ogol, incluído em 1º TURNO: Olaria 1-2 Vasco (1952-10-05)
- jogo só no ogol, incluído em 1º TURNO: Bonsucesso 0-4 Bangu (1952-10-05)
- jogo só no ogol, incluído em 1º TURNO: São Cristóvão 0-9 Flamengo (1952-10-12)
- jogo só no ogol, incluído em 1º TURNO: Bonsucesso 0-3 Botafogo (1952-10-19)
- jogo só no ogol, incluído em 1º TURNO: Olaria 1-3 Fluminense (1952-10-19)
- jogo só no ogol, incluído em 1º TURNO: Bonsucesso 1-6 Madureira (1952-10-26)
- jogo só no ogol, incluído em 1º TURNO: São Cristóvão 1-2 Vasco (1952-10-26)
- só na RSSSF (não achado no ogol): Bangu 3-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Vasco 3-1 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Fluminense 3-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Olaria 0-0 Flamengo (None)
- só na RSSSF (não achado no ogol): Botafogo 1-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Flamengo 4-2 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Madureira 2-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Botafogo 4-1 Olaria (None)
- só na RSSSF (não achado no ogol): Fluminense 3-0 Olaria (None)
- só na RSSSF (não achado no ogol): Vasco 1-0 Olaria (None)

### 1953

- tabela publicada x jogos — 2º Turno / -: Botafogo tabela [22, 16, 3, 3, 57, 23] jogos [21, 15, 3, 3, 51, 23] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [22, 9, 5, 8, 41, 39] jogos [21, 9, 5, 7, 41, 33] — a tabela conta 22 jogos e as fontes trazem 21
- placar diferente no ogol — Vasco x Canto do Rio (1953-10-18): RSSSF 6-0, ogol 6-1; fica o da RSSSF
- placar diferente no ogol — América-RJ x Canto do Rio (1953-10-31): RSSSF 2-0, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Vasco x São Cristóvão (1953-09-26): RSSSF 3-0, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Bonsucesso x Canto do Rio (1953-12-05): RSSSF 3-2, ogol 5-1; fica o da RSSSF
- placar diferente no ogol — América-RJ x Portuguesa-RJ (1953-11-22): RSSSF 4-2, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Olaria x Canto do Rio (1953-11-07): RSSSF 4-0, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Botafogo x Olaria (1953-12-05): RSSSF 2-1, ogol 4-3; fica o da RSSSF
- placar diferente no ogol — Madureira x Portuguesa-RJ (1953-09-27): RSSSF 1-0, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Bonsucesso x Olaria (1953-11-22): RSSSF 3-2, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Flamengo x Canto do Rio (1953-10-10): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — São Cristóvão x Portuguesa-RJ (1953-12-05): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Portuguesa-RJ x Madureira (1953-08-30): RSSSF 2-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Flamengo x Bangu (1954-01-03): RSSSF 7-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Fluminense x Bangu (1954-01-06): RSSSF 2-1, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Fluminense x América-RJ (1953-12-13): RSSSF 6-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Canto do Rio x Olaria (1953-08-16): RSSSF 3-1, ogol 0-4; fica o da RSSSF
- placar diferente no ogol — Flamengo x América-RJ (1953-12-28): RSSSF 3-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Vasco x Botafogo (1953-12-27): RSSSF 2-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Bangu x Fluminense (1953-10-11): RSSSF 3-1, ogol 1-2; fica o da RSSSF
- mando invertido no ogol — RSSSF Bangu 2-0 São Cristóvão, ogol São Cristóvão 0-2 Bangu (1953-07-19); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Canto do Rio, ogol Canto do Rio 1-2 Fluminense (1953-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-0 Bonsucesso, ogol Bonsucesso 0-2 Botafogo (1953-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-1 Olaria, ogol Olaria 1-2 América-RJ (1953-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 4-0 Canto do Rio, ogol Canto do Rio 0-4 Botafogo (1953-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-0 Bonsucesso, ogol Bonsucesso 0-1 Madureira (1953-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-0 São Cristóvão, ogol São Cristóvão 0-3 Fluminense (1953-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 5-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-5 Vasco (1953-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-1 Olaria, ogol Olaria 1-3 Flamengo (1953-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-3 Botafogo (1953-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 3-0 Bonsucesso, ogol Bonsucesso 0-3 América-RJ (1953-10-11); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-1 Bonsucesso, ogol Bonsucesso 1-3 Flamengo (1953-10-18); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Olaria, ogol Olaria 0-1 Bangu (1953-10-18); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 2-0 Canto do Rio, ogol Canto do Rio 0-2 Madureira (1953-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 2-1 Portuguesa-RJ, ogol Portuguesa-RJ 1-2 Olaria (1953-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Bonsucesso, ogol Bonsucesso 0-2 Vasco (1953-11-01); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Bonsucesso, ogol Bonsucesso 1-2 Fluminense (1953-11-08); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Madureira, ogol Madureira 0-2 Vasco (1953-11-08); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 5-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-5 Flamengo (1953-11-11); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-2 Canto do Rio, ogol Canto do Rio 2-3 Bangu (1953-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 São Cristóvão, ogol São Cristóvão 0-1 Botafogo (1953-11-17); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 5-0 Madureira, ogol Madureira 0-5 Flamengo (1953-11-22); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 4-0 São Cristóvão, ogol São Cristóvão 0-4 Flamengo (1953-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-1 Olaria, ogol Olaria 1-3 Fluminense (1953-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-0 Bonsucesso, ogol Bonsucesso 0-2 Bangu (1953-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-1 Fluminense, ogol Fluminense 1-2 Flamengo (1953-12-22); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-0 Botafogo, ogol Botafogo 0-1 América-RJ (1954-01-09); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 4-1 Vasco, ogol Vasco 1-4 Flamengo (1954-01-10); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-2 Vasco, ogol Vasco 2-3 Fluminense (1954-01-14); fica a RSSSF
- jogo só no ogol, incluído em 1º Turno: Canto do Rio 0-6 Vasco (1953-07-19)
- jogo só no ogol, incluído em 1º Turno: Canto do Rio 0-2 América-RJ (1953-08-02)
- jogo só no ogol, incluído em 1º Turno: São Cristóvão 0-3 Vasco (1953-08-02)
- jogo só no ogol, incluído em 1º Turno: Canto do Rio 2-3 Bonsucesso (1953-08-09)
- jogo só no ogol, incluído em 1º Turno: Portuguesa-RJ 2-4 América-RJ (1953-08-16)
- jogo só no ogol, incluído em 1º Turno: Olaria 1-2 Botafogo (1953-08-30)
- jogo só no ogol, incluído em 1º Turno: Olaria 2-3 Bonsucesso (1953-09-06)
- jogo só no ogol, incluído em 1º Turno: Portuguesa-RJ 1-2 São Cristóvão (1953-09-13)
- jogo só no ogol, incluído em 1º Turno: Canto do Rio 0-1 Flamengo (1953-09-13)
- jogo só no ogol, incluído em 1º Turno: Bangu 2-7 Flamengo (1953-09-27)
- jogo só no ogol, incluído em 2º Turno: Bangu 0-6 Botafogo (1953-10-24)
- jogo só no ogol, incluído em 2º Turno: América-RJ 1-6 Fluminense (1953-10-25)
- jogo só no ogol, incluído em 2º Turno: América-RJ 2-3 Flamengo (1953-11-14)
- jogo só no ogol, incluído em 2º Turno: Botafogo 1-2 Vasco (1953-11-29)
- só na RSSSF (não achado no ogol): Vasco 3-3 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Flamengo 2-1 Canto do Rio (None)
- só na RSSSF (não achado no ogol): Vasco 6-1 Canto do Rio (None)
- só na RSSSF (não achado no ogol): América-RJ 4-1 Canto do Rio (None)
- só na RSSSF (não achado no ogol): Bonsucesso 0-0 Olaria (None)
- só na RSSSF (não achado no ogol): América-RJ 3-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Botafogo 4-3 Olaria (None)
- só na RSSSF (não achado no ogol): Bonsucesso 5-1 Canto do Rio (None)
- só na RSSSF (não achado no ogol): Fluminense 2-0 América-RJ (None)
- só na RSSSF (não achado no ogol): Vasco 1-1 Botafogo (None)
- só na RSSSF (não achado no ogol): Flamengo 2-0 América-RJ (None)
- só na RSSSF (não achado no ogol): Flamengo 2-0 Bangu (None)

### 1954

- sem ocorrências

### 1955

- tabela publicada x jogos — 3º Turno / -: América-RJ tabela [5, 4, 1, 0, 16, 6] jogos [8, 5, 1, 2, 22, 12] — a tabela conta 5 jogos e as fontes trazem 8
- tabela publicada x jogos — 3º Turno / -: Flamengo tabela [5, 2, 0, 3, 10, 11] jogos [8, 4, 0, 4, 16, 17] — a tabela conta 5 jogos e as fontes trazem 8
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é América-RJ (desempate, jogo extra ou pontos tirados fora de campo)

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- tabela publicada x jogos — Fase única / -: Vasco tabela [2, 1, 0, 1, 2, 1] jogos [26, 16, 5, 5, 56, 31] — a tabela conta 2 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Botafogo tabela [2, 1, 0, 1, 2, 2] jogos [26, 15, 5, 6, 61, 32] — a tabela conta 2 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Flamengo tabela [2, 1, 0, 1, 2, 3] jogos [26, 15, 6, 5, 66, 29] — a tabela conta 2 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Vasco tabela [2, 1, 1, 0, 3, 2] jogos [26, 16, 5, 5, 56, 31] — a tabela conta 2 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Flamengo tabela [2, 0, 2, 0, 3, 3] jogos [26, 15, 6, 5, 66, 29] — a tabela conta 2 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Botafogo tabela [2, 0, 1, 1, 3, 4] jogos [26, 15, 5, 6, 61, 32] — a tabela conta 2 jogos e as fontes trazem 26
- placar diferente no ogol — Olaria x Fluminense (1958-07-26): RSSSF 1-3, ogol 1-2; fica o da RSSSF

### 1959

- tabela publicada x jogos — Fase única / -: Botafogo tabela [22, 15, 2, 5, 61, 28] jogos [24, 17, 2, 5, 65, 28] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Bangu tabela [22, 13, 6, 3, 39, 20] jogos [24, 13, 6, 5, 39, 24] — a tabela conta 22 jogos e as fontes trazem 24
- placar diferente no ogol — Botafogo x Bangu (1959-12-20): RSSSF 2-0, ogol 4-1; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: Canto do Rio 0-1 Flamengo (1959-12-20)
- jogo só no ogol, incluído em Fase única: Botafogo 2-0 Bangu (1959-12-30)

### 1960

- sem ocorrências

### 1961

- tabela publicada x jogos — 3º Turno / -: Botafogo tabela [14, 11, 2, 1, 30, 10] jogos [25, 18, 6, 1, 54, 18] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: Flamengo tabela [14, 6, 4, 4, 21, 16] jogos [25, 12, 6, 7, 43, 29] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: Fluminense tabela [14, 5, 6, 3, 14, 14] jogos [25, 10, 8, 7, 27, 28] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: Vasco tabela [14, 7, 2, 5, 18, 19] jogos [25, 12, 6, 7, 34, 26] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: Bangu tabela [14, 6, 3, 5, 18, 13] jogos [25, 10, 8, 7, 26, 20] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: América-RJ tabela [14, 4, 2, 8, 14, 17] jogos [25, 8, 6, 11, 27, 25] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: Olaria tabela [14, 3, 3, 8, 14, 24] jogos [25, 8, 5, 12, 24, 34] — a tabela conta 14 jogos e as fontes trazem 25
- tabela publicada x jogos — 3º Turno / -: São Cristóvão tabela [14, 1, 4, 9, 6, 22] jogos [25, 5, 7, 13, 14, 35] — a tabela conta 14 jogos e as fontes trazem 25

### 1962

- sem ocorrências

### 1963

- tabela publicada x jogos — Fase única / -: Fluminense tabela [24, 16, 6, 2, 48, 10] jogos [25, 17, 6, 2, 51, 10] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Vasco tabela [24, 11, 7, 6, 39, 23] jogos [25, 11, 8, 6, 40, 24] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Bonsucesso tabela [24, 4, 5, 15, 14, 32] jogos [25, 4, 5, 16, 14, 35] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Madureira tabela [24, 2, 2, 20, 15, 64] jogos [25, 2, 3, 20, 16, 65] — a tabela conta 24 jogos e as fontes trazem 25
- placar diferente no ogol — Bonsucesso x Fluminense (1963-08-07): RSSSF 0-3, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Madureira x Vasco (1963-09-25): RSSSF 1-1, ogol 1-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Bonsucesso x Fluminense, ogol 1963-08-07); fica a do ogol
- só na RSSSF (não achado no ogol): Bonsucesso 0-1 Fluminense (1963-08-07)
- só na RSSSF (não achado no ogol): Madureira 1-2 Vasco (1963-09-25)
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é Fluminense (desempate, jogo extra ou pontos tirados fora de campo)

### 1964

- sem ocorrências

### 1965

- jogo só no ogol, incluído em Fase única: Flamengo 2-1 Vasco (1965-10-09)

### 1966

- sem ocorrências

### 1967

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Campo Grande-RJ x Bangu, ogol 1967-10-25); fica a do ogol
- jogo só no ogol, incluído em 1º Turno: Vasco 1-2 Fluminense (1967-10-21)
- jogo só no ogol, incluído em 1º Turno: Flamengo 1-2 Botafogo (1967-10-22)
- jogo só no ogol, incluído em 1º Turno: São Cristóvão 1-2 Bonsucesso (1967-10-22)
- jogo só no ogol, incluído em 1º Turno: Madureira 1-1 Campo Grande-RJ (1967-10-28)

### 1968

- sem ocorrências

### 1969

- mando invertido no ogol — RSSSF Bonsucesso 0-0 Bangu, ogol Bangu 0-0 Bonsucesso (1969-04-30); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-1 América-RJ, ogol América-RJ 1-2 Bangu (1969-05-03); fica a RSSSF

### 1970

- tabela publicada x jogos — 2º Turno / -: Madureira tabela [7, 1, 1, 5, 4, 13] jogos [7, 1, 1, 5, 4, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Campo Grande-RJ tabela [7, 1, 0, 6, 4, 21] jogos [7, 1, 0, 6, 6, 17] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF Bangu 2-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-2 Bangu (1970-06-27); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Bonsucesso (1970-07-04); fica a RSSSF
- mando invertido e placar diferente no ogol — RSSSF Madureira 0-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-1 Madureira (1970-09-17); fica a RSSSF

### 1971

- tabela publicada x jogos — Primeira fase / Grupo A: Bonsucesso tabela [6, 2, 1, 3, 3, 5] jogos [6, 1, 2, 3, 3, 5] — placar diverge entre RSSSF e ogol em São Cristóvão x Bonsucesso (0-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo B: São Cristóvão tabela [6, 0, 1, 5, 0, 11] jogos [6, 0, 2, 4, 0, 11] — placar diverge entre RSSSF e ogol em São Cristóvão x Bonsucesso (0-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Fluminense tabela [14, 8, 5, 1, 23, 10] jogos [14, 7, 6, 1, 23, 10] — placar diverge entre RSSSF e ogol em América-RJ x Fluminense (0-0 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: América-RJ tabela [13, 2, 6, 5, 8, 12] jogos [14, 2, 8, 4, 8, 12] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Bangu tabela [13, 4, 2, 7, 12, 15] jogos [14, 4, 3, 7, 12, 15] — a tabela conta 13 jogos e as fontes trazem 14
- placar diferente no ogol — América-RJ x Fluminense (1971-05-01): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Vasco x Botafogo, ogol 1971-04-06); fica a do ogol
- jogo só no ogol, incluído em First Phase: Vasco 1-0 Bangu (1971-03-07)
- jogo só no ogol, incluído em Final Phase: Bangu 0-0 América-RJ (1971-06-27)

### 1972

- mando invertido no ogol — RSSSF América-RJ 4-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-4 América-RJ (1972-04-23); fica a RSSSF
- placar diferente no ogol — Olaria x Bonsucesso (1972-04-19): RSSSF 2-0, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Bonsucesso x Olaria (1972-08-13): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Olaria x São Cristóvão, ogol 1972-08-26); fica a do ogol

### 1973

- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [7, 4, 3, 0, 14, 4] jogos [25, 13, 7, 5, 36, 16] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Vasco tabela [7, 4, 3, 0, 10, 4] jogos [24, 16, 6, 2, 35, 10] — a tabela conta 7 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Flamengo tabela [7, 4, 1, 2, 13, 5] jogos [24, 14, 5, 5, 34, 16] — a tabela conta 7 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: América-RJ tabela [7, 2, 4, 1, 8, 6] jogos [22, 10, 8, 4, 35, 27] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Botafogo tabela [7, 2, 3, 2, 8, 7] jogos [23, 11, 7, 5, 39, 25] — a tabela conta 7 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Bonsucesso tabela [7, 1, 3, 3, 4, 7] jogos [22, 4, 10, 8, 13, 17] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Olaria tabela [7, 1, 1, 5, 4, 9] jogos [22, 7, 4, 11, 18, 24] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [7, 0, 2, 5, 0, 19] jogos [22, 4, 6, 12, 17, 35] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / Grupo A: Vasco tabela [4, 4, 0, 0, 6, 0] jogos [3, 2, 1, 0, 6, 2] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / Grupo A: Flamengo tabela [4, 1, 1, 2, 2, 3] jogos [3, 2, 0, 1, 11, 3] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / Grupo A: América-RJ tabela [3, 1, 1, 1, 3, 6] jogos [3, 0, 2, 1, 2, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo A: Bangu tabela [4, 0, 2, 2, 1, 3] jogos [3, 0, 1, 2, 0, 11] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / Grupo B: Fluminense tabela [4, 2, 1, 1, 3, 2] jogos [4, 4, 0, 0, 8, 2] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Botafogo tabela [4, 2, 1, 1, 7, 3] jogos [4, 1, 1, 2, 3, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Olaria tabela [3, 0, 2, 1, 3, 2] jogos [3, 0, 1, 2, 3, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Bonsucesso tabela [4, 0, 2, 2, 1, 4] jogos [3, 0, 2, 1, 2, 4] — a tabela conta 4 jogos e as fontes trazem 3
- mando invertido no ogol — RSSSF Bangu 0-0 América-RJ, ogol América-RJ 0-0 Bangu (1973-07-22); fica a RSSSF
- jogo só no ogol, incluído em 2º Turno (Taça Francisco Laport): Fluminense 1-0 Vasco (1973-07-27)
- jogo só no ogol, incluído em 2º Turno (Taça Francisco Laport): Olaria 0-0 América-RJ (1973-08-15)

### 1974

- tabela publicada x jogos — Primeira fase / -: Vasco tabela [7, 4, 3, 0, 9, 3] jogos [27, 15, 8, 4, 43, 28] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [7, 3, 4, 0, 12, 4] jogos [27, 15, 9, 3, 42, 21] — a tabela conta 7 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Botafogo tabela [7, 4, 2, 1, 10, 4] jogos [25, 10, 10, 5, 37, 24] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: América-RJ tabela [7, 4, 1, 2, 13, 10] jogos [28, 19, 3, 6, 48, 26] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Fluminense tabela [7, 2, 2, 3, 5, 4] jogos [25, 11, 7, 7, 30, 17] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [7, 2, 0, 5, 7, 15] jogos [25, 5, 7, 13, 23, 38] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Bonsucesso tabela [7, 1, 2, 4, 4, 12] jogos [25, 6, 8, 11, 19, 27] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Campo Grande-RJ tabela [7, 0, 2, 5, 2, 10] jogos [25, 3, 11, 11, 13, 28] — a tabela conta 7 jogos e as fontes trazem 25
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-3 Madureira, ogol Madureira 3-0 Campo Grande-RJ (1974-10-19); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Botafogo x Bangu, ogol 1974-09-02); fica a do ogol
- jogo só no ogol, incluído em Fase única: Olaria 0-1 América-RJ (1974-09-19)
- só na RSSSF (não achado no ogol): América-RJ 1-0 Olaria (1974-09-14)

### 1975

- tabela publicada x jogos — 1º Turno / -: Vasco tabela [11, 7, 3, 1, 24, 11] jogos [12, 8, 3, 1, 27, 12] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 1º Turno / -: Bangu tabela [11, 4, 3, 4, 9, 12] jogos [12, 4, 3, 5, 10, 15] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 3º Turno (Taça Danilo Leal Carneiro) / -: Vasco tabela [7, 6, 0, 1, 19, 7] jogos [8, 7, 0, 1, 20, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — 3º Turno (Taça Danilo Leal Carneiro) / -: Flamengo tabela [7, 6, 0, 1, 22, 6] jogos [8, 6, 0, 2, 22, 7] — a tabela conta 7 jogos e as fontes trazem 8
- mando invertido no ogol — RSSSF América-RJ 2-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-2 América-RJ (1975-03-16); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-2 Flamengo, ogol Flamengo 2-1 Vasco (1975-06-08); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-3 Flamengo (1975-07-10); fica a RSSSF
- só na RSSSF (não achado no ogol): Vasco 3-1 Bangu (1975-02-20)

### 1976

- tabela publicada x jogos — Fase final / -: Fluminense tabela [3, 1, 2, 0, 4, 2] jogos [4, 2, 2, 0, 5, 2] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Vasco tabela [3, 1, 2, 0, 4, 3] jogos [4, 1, 2, 1, 4, 4] — a tabela conta 3 jogos e as fontes trazem 4
- mando invertido no ogol — RSSSF Madureira 2-1 São Cristóvão, ogol São Cristóvão 1-2 Madureira (1976-07-17); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-3 Flamengo, ogol Flamengo 3-0 Olaria (1976-07-24); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-0 São Cristóvão, ogol São Cristóvão 0-2 América-RJ (1976-07-30); fica a RSSSF
- placar diferente no ogol — São Cristóvão x Campo Grande-RJ (1976-07-28): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Vasco x São Cristóvão, ogol 1976-04-14); fica a do ogol
- mando invertido e placar diferente no ogol — RSSSF Vasco 4-0 Volta Redonda, ogol Volta Redonda 0-2 Vasco (1976-08-04); fica a RSSSF
- jogo só no ogol, incluído em Final Phase: Olaria 1-1 Goytacaz (1976-09-04)
- só na RSSSF (não achado no ogol): Olaria 1-1 Goytacaz (1976-07-04)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-1 América-RJ (1976-08-11)
- só na RSSSF (não achado no ogol): Madureira 0-1 Bonsucesso (1976-08-11)

### 1977

- tabela publicada x jogos — 2º Turno / -: Vasco tabela [14, 12, 2, 0, 29, 0] jogos [16, 12, 4, 0, 29, 0] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Flamengo tabela [14, 12, 2, 0, 37, 2] jogos [15, 12, 3, 0, 37, 2] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [14, 8, 0, 6, 17, 14] jogos [15, 8, 1, 6, 17, 14] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Combined Table - Both stages / -: Vasco tabela [28, 25, 2, 1, 69, 5] jogos [30, 25, 4, 1, 69, 5] — a tabela conta 28 jogos e as fontes trazem 30
- tabela publicada x jogos — Combined Table - Both stages / -: Flamengo tabela [28, 23, 3, 2, 75, 12] jogos [29, 23, 4, 2, 75, 12] — a tabela conta 28 jogos e as fontes trazem 29
- tabela publicada x jogos — Combined Table - Both stages / -: Bangu tabela [28, 9, 10, 9, 28, 33] jogos [29, 9, 11, 9, 28, 33] — a tabela conta 28 jogos e as fontes trazem 29
- mando invertido no ogol — RSSSF Olaria 0-3 Fluminense, ogol Fluminense 3-0 Olaria (1977-05-29); fica a RSSSF
- placar diferente no ogol — Bangu x Vasco (1977-09-21): RSSSF 0-0, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Bonsucesso x Vasco, ogol 1977-08-24); fica a do ogol
- só na RSSSF (não achado no ogol): Bangu 0-2 Vasco (1977-09-21)

### 1978

- placar diferente no ogol — Fluminense x Campo Grande-RJ (1978-09-10): RSSSF 2-0, ogol 2-1; fica o da RSSSF
- mando invertido no ogol — RSSSF Madureira 1-2 Bangu, ogol Bangu 2-1 Madureira (1978-10-28); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 2-5 Flamengo, ogol Flamengo 5-2 Campo Grande-RJ (1978-10-29); fica a RSSSF

### 1979

- artilheiro: a RSSSF dá Zico 26 no campeonato normal e 34 no Especial; a Wikipédia, o contrário. Fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Serrano tabela [17, 6, 6, 5, 11, 14] jogos [18, 7, 6, 5, 13, 15] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: São Cristóvão tabela [17, 3, 3, 11, 8, 32] jogos [17, 2, 4, 11, 8, 32] — placar diverge entre RSSSF e ogol em São Cristóvão x Olaria (1-1 x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Olaria tabela [17, 2, 4, 11, 12, 28] jogos [18, 2, 5, 11, 13, 30] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Flamengo tabela [13, 7, 5, 1, 1, 15] jogos [7, 5, 1, 1, 15, 6] — a tabela conta 13 jogos e as fontes trazem 7
- placar diferente no ogol — São Cristóvão x Olaria (1979-06-02): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- vencedor da final pelos jogos (Vasco) diferente do campeão oficial (Flamengo); fica o oficial
- special: placar diferente no ogol — Americano-RJ x Fluminense (1979-02-11): RSSSF 2-2, ogol 2-3; fica o da RSSSF
- special: placar diferente no ogol — Fluminense Nova Friburgo x América-RJ (1979-04-29): RSSSF 1-4, ogol 4-1; fica o da RSSSF

### 1979 Especial

- tabela publicada x jogos — 2º Turno / -: Americano-RJ tabela [9, 4, 2, 3, 14, 12] jogos [9, 3, 3, 3, 14, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Volta Redonda tabela [9, 3, 1, 5, 9, 10] jogos [9, 4, 1, 4, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: São Cristóvão tabela [9, 2, 2, 5, 5, 22] jogos [9, 1, 2, 6, 5, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Fluminense Nova Friburgo tabela [9, 0, 1, 8, 1, 23] jogos [9, 0, 2, 7, 1, 23] — placar diverge entre RSSSF e ogol em Fluminense Nova Friburgo x América-RJ (1-4 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF

### 1980

- tabela publicada x jogos — 2º Turno / -: Vasco tabela [9, 7, 1, 1, 19, 9] jogos [10, 7, 2, 1, 20, 10] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Campo Grande-RJ tabela [9, 5, 1, 3, 8, 7] jogos [9, 4, 2, 3, 8, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [9, 2, 4, 3, 15, 15] jogos [10, 2, 5, 3, 16, 16] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: América-RJ tabela [9, 2, 2, 5, 6, 12] jogos [9, 2, 3, 4, 7, 12] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF Bonsucesso 0-2 Fluminense, ogol Fluminense 2-0 Bonsucesso (1980-08-17); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-1 Fluminense, ogol Fluminense 1-1 Goytacaz (1980-09-05); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Fluminense, ogol Fluminense 1-1 Flamengo (1980-09-14); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-1 Fluminense, ogol Fluminense 1-1 Volta Redonda (1980-09-18); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-1 AD Niterói, ogol AD Niterói 1-3 Fluminense (1980-09-28); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 Volta Redonda, ogol Volta Redonda 0-0 Vasco (1980-10-01); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-2 Fluminense, ogol Fluminense 2-1 Vasco (1980-10-05); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Flamengo, ogol Flamengo 1-1 Botafogo (1980-10-12); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 4-0 Olaria, ogol Olaria 0-4 Fluminense (1980-10-15); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-3 Campo Grande-RJ, ogol Campo Grande-RJ 3-2 Volta Redonda (1980-11-02); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 2-0 América-RJ, ogol América-RJ 0-2 Serrano (1980-11-02); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-3 Fluminense, ogol Fluminense 3-2 Volta Redonda (1980-11-09); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-RJ x Volta Redonda, ogol 1980-11-13); fica a do ogol
- mando invertido no ogol — RSSSF América-RJ 0-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-0 América-RJ (1980-09-11); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 2-0 Volta Redonda, ogol Volta Redonda 0-2 Americano-RJ (1980-09-11); fica a RSSSF
- jogo só no ogol, incluído em 2º Turno (Taça Gustavo de Carvalho): Fluminense 1-1 Vasco (1980-10-26)

### 1981

- tabela publicada x jogos — 3º Turno (Taça Sylvio Corrêa Pacheco) / -: Madureira tabela [11, 4, 3, 4, 9, 16] jogos [11, 3, 3, 5, 9, 16] — placar diverge entre RSSSF e ogol em Olaria x Madureira (3-0 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 3º Turno (Taça Sylvio Corrêa Pacheco) / -: Olaria tabela [11, 1, 0, 10, 5, 18] jogos [11, 2, 0, 9, 5, 18] — placar diverge entre RSSSF e ogol em Olaria x Madureira (3-0 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-0 Bangu, ogol Bangu 0-0 Madureira (1981-05-24); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-1 Americano-RJ, ogol Americano-RJ 1-2 Volta Redonda (1981-05-24); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 2-4 Flamengo, ogol Flamengo 4-2 Madureira (1981-05-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-2 Americano-RJ, ogol Americano-RJ 2-2 Fluminense (1981-05-31); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-0 América-RJ, ogol América-RJ 0-0 Campo Grande-RJ (1981-05-31); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-3 Botafogo, ogol Botafogo 3-1 Madureira (1981-05-31); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 0-1 Olaria, ogol Olaria 1-0 Serrano (1981-05-31); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-3 Bangu, ogol Bangu 3-3 Fluminense (1981-06-07); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-1 Flamengo, ogol Flamengo 1-0 Vasco (1981-06-07); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 4-1 Madureira, ogol Madureira 1-4 Vasco (1981-06-10); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 1-2 Fluminense, ogol Fluminense 2-1 Serrano (1981-06-11); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 0-1 Botafogo, ogol Botafogo 1-0 Volta Redonda (1981-06-11); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 3-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-3 Volta Redonda (1981-06-14); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 5-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-5 Flamengo (1981-06-21); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-2 Flamengo, ogol Flamengo 2-1 Volta Redonda (1981-06-24); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Olaria, ogol Olaria 0-2 Vasco (1981-06-24); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 0-2 América-RJ, ogol América-RJ 2-0 Volta Redonda (1981-06-27); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Flamengo, ogol Flamengo 1-2 Fluminense (1981-06-28); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 1-1 Bangu, ogol Bangu 1-1 Serrano (1981-07-05); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-2 Americano-RJ, ogol Americano-RJ 2-0 Campo Grande-RJ (1981-07-05); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-4 Madureira, ogol Madureira 4-2 Volta Redonda (1981-07-11); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-1 Bangu, ogol Bangu 1-3 Vasco (1981-07-12); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-0 Americano-RJ, ogol Americano-RJ 0-0 Olaria (1981-07-12); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Serrano, ogol Serrano 0-1 Bangu (1981-07-26); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Olaria, ogol Olaria 0-0 América-RJ (1981-08-02); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Volta Redonda, ogol Volta Redonda 1-1 Flamengo (1981-08-02); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-1 Serrano, ogol Serrano 1-0 Olaria (1981-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-2 Volta Redonda, ogol Volta Redonda 2-1 Americano-RJ (1981-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-1 América-RJ (1981-08-16); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-1 Fluminense, ogol Fluminense 1-0 Americano-RJ (1981-08-19); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-1 Volta Redonda, ogol Volta Redonda 1-1 Campo Grande-RJ (1981-08-30); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-5 Vasco, ogol Vasco 5-1 Madureira (1981-09-02); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-3 Flamengo, ogol Flamengo 3-0 Campo Grande-RJ (1981-09-02); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-0 Olaria, ogol Olaria 0-2 Fluminense (1981-09-02); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-1 Volta Redonda, ogol Volta Redonda 1-3 Botafogo (1981-09-06); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Fluminense, ogol Fluminense 1-1 Flamengo (1981-09-07); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-0 Madureira, ogol Madureira 0-1 Flamengo (1981-09-10); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-0 Olaria, ogol Olaria 0-1 Campo Grande-RJ (1981-09-12); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Serrano, ogol Serrano 1-2 Fluminense (1981-09-13); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-0 Volta Redonda, ogol Volta Redonda 0-0 Madureira (1981-09-13); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-3 Vasco, ogol Vasco 3-2 Bangu (1981-09-16); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Vasco, ogol Vasco 1-1 Flamengo (1981-09-20); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-3 Campo Grande-RJ, ogol Campo Grande-RJ 3-0 Americano-RJ (1981-09-20); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-5 Vasco, ogol Vasco 5-0 Americano-RJ (1981-09-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-0 Madureira, ogol Madureira 0-2 Bangu (1981-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-1 Botafogo, ogol Botafogo 1-1 Madureira (1981-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-2 Bangu, ogol Bangu 2-0 Olaria (1981-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-4 Flamengo, ogol Flamengo 4-0 Olaria (1981-10-07); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-0 Americano-RJ, ogol Americano-RJ 0-3 Fluminense (1981-10-18); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Olaria, ogol Olaria 0-1 Vasco (1981-10-18); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-1 América-RJ, ogol América-RJ 1-0 Olaria (1981-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 1-3 Fluminense, ogol Fluminense 3-1 Serrano (1981-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-3 Bangu, ogol Bangu 3-0 Fluminense (1981-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-2 Flamengo (1981-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-2 Americano-RJ, ogol Americano-RJ 2-1 Botafogo (1981-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 0-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-0 Serrano (1981-10-31); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-2 Americano-RJ, ogol Americano-RJ 2-0 Olaria (1981-11-01); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-2 Fluminense, ogol Fluminense 2-0 Madureira (1981-11-04); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-0 América-RJ, ogol América-RJ 0-0 Americano-RJ (1981-11-04); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-2 Americano-RJ, ogol Americano-RJ 2-1 Bangu (1981-11-08); fica a RSSSF
- mando invertido no ogol — RSSSF Serrano 1-1 Madureira, ogol Madureira 1-1 Serrano (1981-11-08); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Bangu, ogol Bangu 0-1 Vasco (1981-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 2-1 Americano-RJ, ogol Americano-RJ 1-2 Madureira (1981-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-3 Flamengo, ogol Flamengo 3-1 Fluminense (1981-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-1 Botafogo, ogol Botafogo 1-0 Olaria (1981-11-18); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-1 Bangu, ogol Bangu 1-0 Madureira (1981-11-18); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-0 Olaria, ogol Olaria 0-1 Volta Redonda (1981-11-22); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Vasco x Flamengo na Final Phase sempre na mesma ordem) — ogol Flamengo 0-2 Vasco (1981-11-29)
- placar diferente no ogol — Olaria x Madureira (1981-10-25): RSSSF 3-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Volta Redonda x América-RJ, ogol 1981-09-23); fica a do ogol
- mando invertido e placar diferente no ogol — RSSSF Olaria 1-2 América-RJ, ogol América-RJ 1-2 Olaria (1981-07-01); fica a RSSSF
- jogo só no ogol, incluído em 1º Turno (Taça Guanabara): Bangu 1-1 Americano-RJ (1981-07-08)
- só na RSSSF (não achado no ogol): Americano-RJ 1-1 Bangu (1981-09-06)
- vencedor da final pelos jogos (Vasco) diferente do campeão oficial (Flamengo); fica o oficial

### 1982

- mando invertido no ogol — RSSSF Portuguesa-RJ 1-2 Bangu, ogol Bangu 2-1 Portuguesa-RJ (1982-07-18); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-0 América-RJ, ogol América-RJ 0-0 Americano-RJ (1982-07-18); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-4 Flamengo, ogol Flamengo 4-0 Portuguesa-RJ (1982-07-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-1 América-RJ, ogol América-RJ 1-1 Bonsucesso (1982-07-24); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 Madureira, ogol Madureira 0-0 Vasco (1982-07-25); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-0 Americano-RJ, ogol Americano-RJ 0-0 Campo Grande-RJ (1982-07-25); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-2 Botafogo, ogol Botafogo 2-2 Volta Redonda (1982-07-25); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-1 Americano-RJ, ogol Americano-RJ 1-0 Flamengo (1982-08-01); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-8 Flamengo, ogol Flamengo 8-0 Madureira (1982-08-04); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-1 Volta Redonda (1982-08-08); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-3 Flamengo, ogol Flamengo 3-0 Botafogo (1982-08-14); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-3 Fluminense (1982-08-15); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-2 Americano-RJ, ogol Americano-RJ 2-1 Portuguesa-RJ (1982-08-15); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-1 Bangu, ogol Bangu 1-1 Madureira (1982-08-18); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-3 Flamengo, ogol Flamengo 3-1 Volta Redonda (1982-08-18); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-3 América-RJ, ogol América-RJ 3-0 Portuguesa-RJ (1982-08-18); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 2-2 Botafogo, ogol Botafogo 2-2 Campo Grande-RJ (1982-08-19); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-0 Madureira, ogol Madureira 0-1 Volta Redonda (1982-08-21); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-2 Bonsucesso, ogol Bonsucesso 2-3 Flamengo (1982-08-21); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-2 Vasco, ogol Vasco 2-1 América-RJ (1982-08-21); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-3 Campo Grande-RJ, ogol Campo Grande-RJ 3-1 Volta Redonda (1982-08-28); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-3 Botafogo, ogol Botafogo 3-1 Portuguesa-RJ (1982-08-29); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-3 Americano-RJ, ogol Americano-RJ 3-0 Madureira (1982-09-05); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-0 Madureira, ogol Madureira 0-0 Portuguesa-RJ (1982-09-11); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-1 Americano-RJ, ogol Americano-RJ 1-1 Volta Redonda (1982-09-18); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Vasco x Flamengo na 1º Turno (Taça Guanabara) sempre na mesma ordem) — ogol Flamengo 0-0 Vasco (1982-09-19)
- mando invertido no ogol — RSSSF Madureira 0-1 Vasco, ogol Vasco 1-0 Madureira (1982-09-26); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Volta Redonda, ogol Volta Redonda 1-1 Flamengo (1982-09-26); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-1 Americano-RJ (1982-09-29); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-3 Flamengo, ogol Flamengo 3-1 Bonsucesso (1982-10-02); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 2-1 Volta Redonda, ogol Volta Redonda 1-2 Campo Grande-RJ (1982-10-10); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-0 Americano-RJ, ogol Americano-RJ 0-1 América-RJ (1982-10-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-2 Vasco, ogol Vasco 2-1 Bangu (1982-10-12); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-1 Americano-RJ (1982-10-16); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Bonsucesso, ogol Bonsucesso 0-0 América-RJ (1982-10-16); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-3 Vasco, ogol Vasco 3-2 Fluminense (1982-10-17); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-2 Botafogo, ogol Botafogo 2-0 Americano-RJ (1982-10-20); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-0 Vasco, ogol Vasco 0-2 América-RJ (1982-10-24); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-1 Volta Redonda, ogol Volta Redonda 1-1 Madureira (1982-10-24); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-2 Botafogo (1982-10-24); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-3 Portuguesa-RJ, ogol Portuguesa-RJ 3-2 Flamengo (1982-10-25); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 2-1 Portuguesa-RJ, ogol Portuguesa-RJ 1-2 Madureira (1982-10-31); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 Volta Redonda, ogol Volta Redonda 0-1 Botafogo (1982-10-31); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 2-0 Madureira, ogol Madureira 0-2 Bonsucesso (1982-11-06); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 4-1 Vasco, ogol Vasco 1-4 Botafogo (1982-11-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-2 Bangu (1982-11-07); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-6 Volta Redonda, ogol Volta Redonda 6-1 Portuguesa-RJ (1982-11-07); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 3-0 Fluminense, ogol Fluminense 0-3 Campo Grande-RJ (1982-11-10); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-3 Flamengo, ogol Flamengo 3-0 Americano-RJ (1982-11-10); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 3-1 Portuguesa-RJ, ogol Portuguesa-RJ 1-3 América-RJ (1982-11-10); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-2 Vasco, ogol Vasco 2-1 Portuguesa-RJ (1982-11-14); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 3-1 Volta Redonda, ogol Volta Redonda 1-3 Americano-RJ (1982-11-14); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-3 Vasco, ogol Vasco 3-1 Flamengo (1982-11-20); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-2 Botafogo, ogol Botafogo 2-0 Bangu (1982-11-21); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Vasco x Portuguesa-RJ, ogol 1982-08-31); fica a do ogol

### 1983

- tabela publicada x jogos — Taça Rio de Janeiro winner qualified to the final playoff / -: Flamengo tabela [11, 9, 0, 2, 23, 6] jogos [12, 10, 0, 2, 24, 6] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Taça Rio de Janeiro winner qualified to the final playoff / -: Bangu tabela [11, 8, 2, 1, 22, 6] jogos [12, 8, 2, 2, 22, 7] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [22, 14, 5, 3, 41, 16] jogos [23, 14, 5, 4, 41, 17] — a tabela conta 22 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [22, 13, 2, 7, 38, 24] jogos [23, 14, 2, 7, 39, 24] — a tabela conta 22 jogos e as fontes trazem 23
- mando invertido no ogol — RSSSF São Cristóvão 0-3 Fluminense, ogol Fluminense 3-0 São Cristóvão (1983-07-02); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 6-2 Flamengo, ogol Flamengo 2-6 Bangu (1983-09-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Vasco, ogol Vasco 1-1 Bangu (1983-07-10); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-1 Botafogo, ogol Botafogo 1-1 Volta Redonda (1983-09-07); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-0 Fluminense, ogol Fluminense 0-0 Flamengo (1983-07-16); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-0 São Cristóvão, ogol São Cristóvão 0-2 Botafogo (1983-07-17); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-0 Bonsucesso, ogol Bonsucesso 0-0 Campo Grande-RJ (1983-07-17); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-1 Vasco, ogol Vasco 1-2 América-RJ (1983-07-31); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-3 Fluminense, ogol Fluminense 3-0 Bangu (1983-08-07); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 2-2 Botafogo, ogol Botafogo 2-2 Campo Grande-RJ (1983-08-21); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-3 Bangu, ogol Bangu 3-1 América-RJ (1983-08-25); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-2 Botafogo, ogol Botafogo 2-1 Bonsucesso (1983-08-28); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 3-1 Flamengo, ogol Flamengo 1-3 América-RJ (1983-08-28); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Botafogo, ogol Botafogo 0-1 Bangu (1983-09-10); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Flamengo x Bangu na Taça Rio de Janeiro winner qualified to the final playoff sempre na mesma ordem) — ogol Bangu 1-3 Flamengo (1983-11-23)
- mando invertido no ogol — RSSSF São Cristóvão 0-0 Americano-RJ, ogol Americano-RJ 0-0 São Cristóvão (1983-09-25); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Volta Redonda, ogol Volta Redonda 1-1 Botafogo (1983-09-25); fica a RSSSF
- mando invertido no ogol — RSSSF São Cristóvão 0-0 Botafogo, ogol Botafogo 0-0 São Cristóvão (1983-10-01); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-1 Bonsucesso (1983-10-02); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 0-0 Vasco, ogol Vasco 0-0 Goytacaz (1983-10-02); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-2 Flamengo, ogol Flamengo 2-1 Fluminense (1983-10-02); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 0-3 Bangu, ogol Bangu 3-0 Bonsucesso (1983-10-15); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 América-RJ, ogol América-RJ 0-0 Vasco (1983-10-16); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 4-0 Goytacaz, ogol Goytacaz 0-4 América-RJ (1983-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-1 América-RJ, ogol América-RJ 1-3 Bangu (1983-11-06); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 2-4 Flamengo, ogol Flamengo 4-2 Bonsucesso (1983-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Bonsucesso, ogol Bonsucesso 0-0 Botafogo (1983-11-12); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-0 América-RJ, ogol América-RJ 0-2 Flamengo (1983-11-13); fica a RSSSF
- mando invertido no ogol — RSSSF São Cristóvão 0-1 Bonsucesso, ogol Bonsucesso 1-0 São Cristóvão (1983-11-27); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-1 Bangu, ogol Bangu 1-0 Botafogo (1983-11-27); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-2 Flamengo, ogol Flamengo 2-0 Bangu (1983-12-14); fica a RSSSF
- placar diferente no ogol — São Cristóvão x Volta Redonda (1983-11-06): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- jogo só no ogol, incluído em First Stage - First Phase: Bangu 2-2 Vasco (1983-08-25)
- só na RSSSF (não achado no ogol): Vasco 2-2 Bangu (1983-09-25)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Fluminense

### 1984

- placar diferente no ogol — Campo Grande-RJ x Vasco (1984-09-30): RSSSF 2-1, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Fluminense x Olaria (1984-10-17): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Bangu x Vasco (1984-10-07): RSSSF 4-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Bangu x Olaria (1984-10-14): RSSSF 4-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — América-RJ x Campo Grande-RJ (1984-10-06): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Botafogo x Campo Grande-RJ (1984-11-04): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Vasco x Olaria (1984-11-10): RSSSF 2-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Flamengo x Campo Grande-RJ (1984-11-23): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Volta Redonda x Americano-RJ (1984-12-02): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Vasco x Campo Grande-RJ (1984-07-01): RSSSF 2-0, ogol 1-2; fica o da RSSSF
- mando invertido no ogol — RSSSF Friburguense 1-3 Botafogo, ogol Botafogo 3-1 Friburguense (1984-07-22); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-0 Fluminense, ogol Fluminense 0-1 Flamengo (1984-09-20); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-0 Vasco, ogol Vasco 0-1 América-RJ (1984-09-23); fica a RSSSF
- mando invertido no ogol — RSSSF Friburguense 0-1 Bangu, ogol Bangu 1-0 Friburguense (1984-09-30); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Olaria, ogol Olaria 1-1 Botafogo (1984-09-30); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-2 Botafogo, ogol Botafogo 2-3 Flamengo (1984-10-14); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-2 Bangu (1984-10-28); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Olaria, ogol Olaria 1-1 Flamengo (1984-10-28); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-0 América-RJ, ogol América-RJ 0-2 Botafogo (1984-10-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-1 Fluminense (1984-11-11); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Bangu, ogol Bangu 1-1 Flamengo (1984-11-11); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-1 Fluminense, ogol Fluminense 1-2 Vasco (1984-11-15); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-0 América-RJ, ogol América-RJ 0-1 Flamengo (1984-11-17); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 4-2 Fluminense, ogol Fluminense 2-4 Botafogo (1984-11-18); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-1 Botafogo, ogol Botafogo 1-2 Vasco (1984-11-24); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Bangu, ogol Bangu 0-0 América-RJ (1984-11-24); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-2 Bangu, ogol Bangu 2-2 Botafogo (1984-12-02); fica a RSSSF
- jogo só no ogol, incluído em First Stage - First Phase: Olaria 0-2 Fluminense (1984-07-07)
- jogo só no ogol, incluído em First Stage - First Phase: Vasco 0-4 Bangu (1984-07-08)
- jogo só no ogol, incluído em First Stage - First Phase: Olaria 2-4 Bangu (1984-07-15)
- jogo só no ogol, incluído em First Stage - First Phase: Campo Grande-RJ 0-1 América-RJ (1984-08-12)
- jogo só no ogol, incluído em First Stage - First Phase: Campo Grande-RJ 0-1 Botafogo (1984-08-19)
- jogo só no ogol, incluído em First Stage - First Phase: Olaria 1-2 Vasco (1984-09-05)
- jogo só no ogol, incluído em First Stage - First Phase: Campo Grande-RJ 0-1 Flamengo (1984-09-16)
- jogo só no ogol, incluído em First Stage - First Phase: Americano-RJ 1-0 Volta Redonda (1984-09-23)
- só na RSSSF (não achado no ogol): América-RJ 0-0 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): Bangu 2-1 Vasco (None)
- só na RSSSF (não achado no ogol): Bangu 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Fluminense 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Botafogo 2-1 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): Vasco 0-0 Olaria (None)
- só na RSSSF (não achado no ogol): Flamengo 1-1 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): Volta Redonda 0-0 Americano-RJ (None)

### 1985

- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [11, 8, 3, 0, 18, 5] jogos [12, 9, 3, 0, 19, 5] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [11, 8, 3, 0, 18, 6] jogos [12, 8, 3, 1, 18, 7] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [22, 14, 7, 1, 38, 14] jogos [23, 14, 7, 2, 38, 15] — a tabela conta 22 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [22, 13, 7, 2, 30, 11] jogos [23, 14, 7, 2, 31, 11] — a tabela conta 22 jogos e as fontes trazem 23
- mando invertido no ogol — RSSSF América-RJ 1-2 Bangu, ogol Bangu 2-1 América-RJ (1985-09-01); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 Fluminense, ogol Fluminense 0-0 Vasco (1985-09-01); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-2 Fluminense, ogol Fluminense 2-2 Bangu (1985-09-07); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-2 Fluminense, ogol Fluminense 2-1 Volta Redonda (1985-09-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Vasco, ogol Vasco 0-0 Botafogo (1985-09-15); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-1 Fluminense, ogol Fluminense 1-0 América-RJ (1985-10-09); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-2 América-RJ, ogol América-RJ 2-1 Botafogo (1985-10-13); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 0-2 Flamengo, ogol Flamengo 2-0 Bonsucesso (1985-11-20); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-0 Fluminense, ogol Fluminense 0-0 Americano-RJ (1985-10-20); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 2-1 Olaria, ogol Olaria 1-2 Bonsucesso (1985-10-20); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-0 Vasco, ogol Vasco 0-2 Fluminense (1985-10-27); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-1 América-RJ, ogol América-RJ 1-1 Goytacaz (1985-10-30); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Americano-RJ, ogol Americano-RJ 0-1 Bangu (1985-11-06); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Botafogo, ogol Botafogo 0-1 Vasco (1985-11-10); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-0 América-RJ, ogol América-RJ 0-0 Olaria (1985-11-13); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-0 Goytacaz, ogol Goytacaz 0-1 Bonsucesso (1985-11-17); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-2 Flamengo, ogol Flamengo 2-0 Vasco (1985-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 América-RJ, ogol América-RJ 1-0 Fluminense (1985-11-30); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Bangu, ogol Bangu 1-1 Botafogo (1985-12-01); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Fluminense, ogol Fluminense 1-1 Flamengo (1985-12-11); fica a RSSSF

### 1986

- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [11, 7, 2, 2, 15, 3] jogos [10, 7, 2, 1, 15, 3] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [11, 4, 5, 2, 15, 7] jogos [12, 5, 5, 2, 19, 7] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Americano-RJ tabela [11, 3, 4, 4, 8, 13] jogos [11, 2, 4, 5, 8, 17] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF Mesquita 0-0 Americano-RJ, ogol Americano-RJ 0-0 Mesquita (1986-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-1 Bangu, ogol Bangu 1-0 Portuguesa-RJ (1986-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 2-1 América-RJ, ogol América-RJ 1-2 Campo Grande-RJ (1986-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-4 Flamengo, ogol Flamengo 4-1 Fluminense (1986-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 0-1 Bangu, ogol Bangu 1-0 Goytacaz (1986-02-23); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-0 América-RJ, ogol América-RJ 0-2 Fluminense (1986-03-01); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-2 Goytacaz, ogol Goytacaz 2-0 Olaria (1986-03-02); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-2 Bangu, ogol Bangu 2-0 Mesquita (1986-03-02); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-2 Bangu, ogol Bangu 2-2 Vasco (1986-03-09); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-2 América-RJ, ogol América-RJ 2-1 Goytacaz (1986-03-09); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-1 Olaria, ogol Olaria 1-1 Portuguesa-RJ (1986-03-09); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 1-3 Flamengo, ogol Flamengo 3-1 Mesquita (1986-03-09); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 1-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-1 Olaria (1986-03-16); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-2 Fluminense, ogol Fluminense 2-0 Mesquita (1986-03-16); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-2 Flamengo, ogol Flamengo 2-0 Olaria (1986-03-20); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-0 Americano-RJ, ogol Americano-RJ 0-2 Bangu (1986-03-20); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-3 Vasco (1986-03-20); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Olaria, ogol Olaria 0-2 Vasco (1986-03-23); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 1-2 Botafogo, ogol Botafogo 2-1 Mesquita (1986-03-23); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-2 Fluminense, ogol Fluminense 2-1 Portuguesa-RJ (1986-03-23); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 1-1 América-RJ, ogol América-RJ 1-1 Olaria (1986-03-30); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-1 Americano-RJ, ogol Americano-RJ 1-2 Vasco (1986-03-30); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-2 Mesquita, ogol Mesquita 2-1 Portuguesa-RJ (1986-03-30); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-2 Botafogo, ogol Botafogo 2-0 Vasco (1986-04-06); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 1-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-1 Mesquita (1986-04-13); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-4 Botafogo, ogol Botafogo 4-1 Fluminense (1986-04-19); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Flamengo, ogol Flamengo 0-2 Vasco (1986-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-1 Mesquita, ogol Mesquita 1-0 Botafogo (1986-05-01); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-2 Vasco, ogol Vasco 2-0 Campo Grande-RJ (1986-05-04); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-2 Flamengo, ogol Flamengo 2-0 América-RJ (1986-05-04); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 3-2 Vasco, ogol Vasco 2-3 Americano-RJ (1986-05-08); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-1 América-RJ (1986-05-10); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-1 Flamengo, ogol Flamengo 1-2 Botafogo (1986-05-11); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-1 Mesquita, ogol Mesquita 1-1 Fluminense (1986-05-11); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-1 Vasco, ogol Vasco 1-2 América-RJ (1986-05-18); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-1 Olaria, ogol Olaria 1-0 Botafogo (1986-05-18); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-0 Mesquita, ogol Mesquita 0-3 Bangu (1986-05-18); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-4 Vasco, ogol Vasco 4-0 Olaria (1986-05-21); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-2 Fluminense (1986-05-25); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-1 Botafogo, ogol Botafogo 1-0 Bangu (1986-05-25); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-0 Olaria, ogol Olaria 0-2 América-RJ (1986-05-25); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Bangu (1986-05-29); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-1 Mesquita, ogol Mesquita 1-3 Flamengo (1986-05-29); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-2 Olaria, ogol Olaria 2-1 Goytacaz (1986-05-29); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Goytacaz, ogol Goytacaz 1-1 Bangu (1986-07-02); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-1 Olaria, ogol Olaria 1-2 Flamengo (1986-07-06); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-2 Fluminense, ogol Fluminense 2-0 Botafogo (1986-07-06); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-1 Mesquita, ogol Mesquita 1-1 Americano-RJ (1986-07-06); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-0 Vasco, ogol Vasco 0-2 Bangu (1986-07-12); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Flamengo, ogol Flamengo 1-1 Bangu (1986-07-19); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-0 Mesquita, ogol Mesquita 0-0 Campo Grande-RJ (1986-07-20); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Mesquita (1986-07-26); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Goytacaz, ogol Goytacaz 1-1 América-RJ (1986-07-26); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Flamengo x Vasco na Final Phase sempre na mesma ordem) — ogol Vasco 0-0 Flamengo (1986-08-03)
- placar diferente no ogol — Portuguesa-RJ x Olaria (1986-07-19): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- jogo só no ogol, incluído em 2º Turno (Taça Rio de Janeiro): Bangu 4-0 Americano-RJ (1986-06-01)
- só na RSSSF (não achado no ogol): Americano-RJ 0-4 Bangu (1986-06-08)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Americano x Fluminense (1986-05-18)

### 1987

- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [13, 7, 5, 1, 14, 7] jogos [13, 7, 5, 1, 15, 7] — placar diverge entre RSSSF e ogol em Cabofriense x Fluminense (0-1 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Cabofriense tabela [13, 4, 4, 5, 13, 20] jogos [13, 4, 4, 5, 12, 20] — placar diverge entre RSSSF e ogol em Cabofriense x Fluminense (0-1 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-2 Americano-RJ, ogol Americano-RJ 2-0 Portuguesa-RJ (1987-02-14); fica a RSSSF
- mando invertido no ogol — RSSSF Porto Alegre-RJ 1-3 Campo Grande-RJ, ogol Campo Grande-RJ 3-1 Porto Alegre-RJ (1987-02-25); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-2 Bangu, ogol Bangu 2-0 Portuguesa-RJ (1987-02-26); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-0 Cabofriense, ogol Cabofriense 0-0 Mesquita (1987-03-08); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 Americano-RJ, ogol Americano-RJ 0-0 Vasco (1987-03-08); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-1 Bangu, ogol Bangu 1-0 Mesquita (1987-03-12); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 2-0 América-RJ, ogol América-RJ 0-2 Goytacaz (1987-03-14); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-0 Fluminense, ogol Fluminense 0-0 Olaria (1987-03-14); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-2 Flamengo, ogol Flamengo 2-0 Portuguesa-RJ (1987-03-15); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Americano-RJ, ogol Americano-RJ 1-1 Bangu (1987-03-15); fica a RSSSF
- mando invertido no ogol — RSSSF Porto Alegre-RJ 2-1 América-RJ, ogol América-RJ 1-2 Porto Alegre-RJ (1987-03-18); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-3 Cabofriense, ogol Cabofriense 3-1 Goytacaz (1987-03-22); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-0 Porto Alegre-RJ, ogol Porto Alegre-RJ 0-0 Portuguesa-RJ (1987-03-22); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 1-2 Botafogo, ogol Botafogo 2-1 Olaria (1987-03-25); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-3 Bangu, ogol Bangu 3-1 Goytacaz (1987-03-25); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Flamengo, ogol Flamengo 0-0 Botafogo (1987-03-28); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 0-1 Americano-RJ, ogol Americano-RJ 1-0 Cabofriense (1987-03-28); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 1-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-1 Olaria (1987-03-29); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 0-0 América-RJ, ogol América-RJ 0-0 Portuguesa-RJ (1987-03-29); fica a RSSSF
- mando invertido no ogol — RSSSF Porto Alegre-RJ 0-0 Mesquita, ogol Mesquita 0-0 Porto Alegre-RJ (1987-03-29); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 2-5 Bangu, ogol Bangu 5-2 Cabofriense (1987-04-02); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-1 Goytacaz, ogol Goytacaz 1-0 Olaria (1987-04-04); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-1 Mesquita, ogol Mesquita 1-1 Portuguesa-RJ (1987-04-05); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-2 Vasco (1987-04-05); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-3 Vasco (1987-04-08); fica a RSSSF
- mando invertido no ogol — RSSSF Porto Alegre-RJ 0-1 Botafogo, ogol Botafogo 1-0 Porto Alegre-RJ (1987-04-12); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 Cabofriense, ogol Cabofriense 0-2 Vasco (1987-04-15); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-0 Americano-RJ, ogol Americano-RJ 0-0 Mesquita (1987-04-18); fica a RSSSF
- mando invertido no ogol — RSSSF Porto Alegre-RJ 0-1 Goytacaz, ogol Goytacaz 1-0 Porto Alegre-RJ (1987-04-19); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-0 Goytacaz, ogol Goytacaz 0-0 Bangu (1987-04-22); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-1 Bangu, ogol Bangu 1-0 Americano-RJ (1987-04-26); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-2 Goytacaz, ogol Goytacaz 2-1 América-RJ (1987-04-26); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-0 Olaria, ogol Olaria 0-1 Fluminense (1987-04-26); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-2 Vasco, ogol Vasco 2-1 Botafogo (1987-04-26); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-1 Portuguesa-RJ, ogol Portuguesa-RJ 1-2 Flamengo (1987-04-26); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 0-6 Vasco, ogol Vasco 6-0 Cabofriense (1987-04-29); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Olaria, ogol Olaria 0-0 Botafogo (1987-04-29); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 3-1 Campo Grande-RJ, ogol Campo Grande-RJ 1-3 América-RJ (1987-04-29); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Mesquita, ogol Mesquita 0-1 Bangu (1987-04-29); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Porto Alegre-RJ, ogol Porto Alegre-RJ 0-0 Botafogo (1987-05-03); fica a RSSSF
- mando invertido no ogol — RSSSF Mesquita 0-6 Vasco, ogol Vasco 6-0 Mesquita (1987-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 3-1 Portuguesa-RJ, ogol Portuguesa-RJ 1-3 Americano-RJ (1987-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Porto Alegre-RJ, ogol Porto Alegre-RJ 0-0 América-RJ (1987-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 2-0 Cabofriense, ogol Cabofriense 0-2 Americano-RJ (1987-05-10); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-1 Olaria, ogol Olaria 1-0 Campo Grande-RJ (1987-05-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Fluminense, ogol Fluminense 1-1 Bangu (1987-05-13); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 1-4 Goytacaz, ogol Goytacaz 4-1 Cabofriense (1987-05-14); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-2 Mesquita, ogol Mesquita 2-1 Americano-RJ (1987-05-17); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 0-0 Mesquita, ogol Mesquita 0-0 Cabofriense (1987-05-20); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-1 Vasco, ogol Vasco 1-0 Americano-RJ (1987-05-20); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-0 Porto Alegre-RJ, ogol Porto Alegre-RJ 0-0 Olaria (1987-05-20); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Botafogo, ogol Botafogo 1-1 América-RJ (1987-05-20); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Flamengo, ogol Flamengo 0-1 Bangu (1987-05-21); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 0-4 Porto Alegre-RJ, ogol Porto Alegre-RJ 4-0 Campo Grande-RJ (1987-05-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-1 Bangu (1987-05-24); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Botafogo (1987-05-27); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 0-1 Olaria, ogol Olaria 1-0 Goytacaz (1987-05-30); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa-RJ 1-5 Vasco, ogol Vasco 5-1 Portuguesa-RJ (1987-06-03); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 Mesquita, ogol Mesquita 0-1 Botafogo (1987-06-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 2-1 Cabofriense, ogol Cabofriense 1-2 Bangu (1987-06-07); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 1-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-1 Cabofriense (1987-06-14); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-1 Botafogo, ogol Botafogo 1-3 Bangu (1987-06-14); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-1 Flamengo, ogol Flamengo 1-1 Fluminense (1987-06-21); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-2 Fluminense, ogol Fluminense 2-0 América-RJ (1987-06-27); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-0 Vasco, ogol Vasco 0-0 Flamengo (1987-07-18); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 Flamengo, ogol Flamengo 1-0 Fluminense (1987-07-27); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-1 Flamengo, ogol Flamengo 1-0 Bangu (1987-08-05); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-1 Vasco, ogol Vasco 1-0 Flamengo (1987-08-09); fica a RSSSF
- placar diferente no ogol — Portuguesa-RJ x Porto Alegre-RJ (1987-05-13): RSSSF 2-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Portuguesa-RJ x Mesquita (1987-05-30): RSSSF 2-3, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — América-RJ x Americano-RJ (1987-05-31): RSSSF 2-0, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Cabofriense x Fluminense (1987-06-18): RSSSF 0-1, ogol 1-0; fica o da RSSSF

### 1988

- tabela publicada x jogos — 1º Turno / -: Botafogo tabela [11, 3, 5, 3, 14, 12] jogos [11, 2, 6, 3, 14, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Goytacaz tabela [11, 3, 3, 5, 6, 7] jogos [11, 3, 4, 4, 7, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF América-RJ 1-4 Vasco, ogol Vasco 4-1 América-RJ (1988-03-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-1 Flamengo, ogol Flamengo 1-1 Bangu (1988-03-09); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-2 América-RJ, ogol América-RJ 2-1 Botafogo (1988-03-12); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 Vasco, ogol Vasco 1-0 Fluminense (1988-03-13); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-1 Goytacaz, ogol Goytacaz 1-1 Americano-RJ (1988-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Flamengo, ogol Flamengo 0-0 América-RJ (1988-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-2 Fluminense, ogol Fluminense 2-0 Botafogo (1988-04-17); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-1 Fluminense, ogol Fluminense 1-0 Bangu (1988-04-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-2 Vasco, ogol Vasco 2-0 Bangu (1988-05-01); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-0 América-RJ, ogol América-RJ 0-2 Vasco (1988-05-14); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 2-0 Porto Alegre-RJ, ogol Porto Alegre-RJ 0-2 Americano-RJ (1988-05-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-3 Vasco, ogol Vasco 3-0 Botafogo (1988-05-23); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 2-1 Fluminense, ogol Fluminense 1-2 Vasco (1988-05-29); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Americano-RJ, ogol Americano-RJ 0-1 Vasco (1988-06-05); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-1 Fluminense, ogol Fluminense 1-1 Vasco (1988-06-08); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-2 Vasco, ogol Vasco 2-1 Flamengo (1988-06-19); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Flamengo, ogol Flamengo 0-1 Vasco (1988-06-22); fica a RSSSF
- placar diferente no ogol — América-RJ x Volta Redonda (1988-04-30): RSSSF 1-3, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Friburguense x Cabofriense (1988-05-01): RSSSF 1-3, ogol 3-1; fica o da RSSSF

### 1989

- placar diferente no ogol — Nova Cidade x Americano-RJ (1989-05-03): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Flamengo x Porto Alegre-RJ, ogol 1989-02-12); fica a do ogol

### 1990

- tabela publicada x jogos — 2º Turno / -: Botafogo tabela [11, 5, 5, 1, 15, 5] jogos [12, 6, 5, 1, 16, 5] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Vasco tabela [11, 3, 5, 3, 18, 11] jogos [12, 3, 5, 4, 18, 12] — a tabela conta 11 jogos e as fontes trazem 12
- mando invertido no ogol — RSSSF América-RJ 0-0 Botafogo, ogol Botafogo 0-0 América-RJ (1990-01-27); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 Vasco, ogol Vasco 1-0 Fluminense (1990-01-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-2 Botafogo, ogol Botafogo 2-0 Fluminense (1990-02-11); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-2 Vasco, ogol Vasco 2-0 América-RJ (1990-02-21); fica a RSSSF
- mando invertido no ogol — RSSSF Nova Cidade 0-1 Botafogo, ogol Botafogo 1-0 Nova Cidade (1990-03-04); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-1 Itaperuna, ogol Itaperuna 1-1 Campo Grande-RJ (1990-03-11); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-0 Botafogo, ogol Botafogo 0-0 Americano-RJ (1990-03-21); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-1 Fluminense, ogol Fluminense 1-0 Vasco (1990-03-25); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-4 Flamengo, ogol Flamengo 4-0 América-RJ (1990-03-28); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-0 Botafogo, ogol Botafogo 0-0 Bangu (1990-04-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Itaperuna, ogol Itaperuna 0-1 Bangu (1990-04-11); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-2 Botafogo, ogol Botafogo 2-0 Flamengo (1990-04-28); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-0 Fluminense, ogol Fluminense 0-2 América-RJ (1990-04-29); fica a RSSSF

### 1991

- tabela publicada x jogos — 1º Turno / Grupo B: Mesquita tabela [11, 7, 3, 1, 12, 5] jogos [11, 7, 3, 1, 11, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / Grupo B: Bangu tabela [11, 2, 4, 5, 8, 8] jogos [22, 6, 8, 8, 13, 13] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / Grupo A: Flamengo tabela [11, 8, 3, 0, 18, 5] jogos [12, 9, 3, 0, 19, 5] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / Grupo A: Botafogo tabela [11, 8, 3, 0, 31, 15] jogos [12, 8, 3, 1, 31, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / Grupo B: Madureira tabela [10, 6, 3, 1, 12, 5] jogos [11, 7, 3, 1, 13, 5] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / Grupo B: Friburguense tabela [10, 3, 7, 0, 9, 6] jogos [10, 3, 7, 0, 10, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo B: Bonsucesso tabela [10, 4, 2, 4, 7, 15] jogos [11, 4, 3, 4, 8, 16] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / Grupo B: Cabofriense tabela [10, 1, 6, 3, 5, 7] jogos [10, 1, 6, 3, 6, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo B: Olaria tabela [10, 2, 2, 6, 4, 8] jogos [11, 3, 2, 6, 8, 9] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bonsucesso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabofriense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Friburguense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Madureira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mesquita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Miguel Couto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Cidade
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olaria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paduano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Nacional
- Bonsucesso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bonsucesso)
- Cabofriense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabofriense)
- Friburguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Friburguense)
- Madureira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Madureira)
- Mesquita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mesquita)
- Miguel Couto — clube que o ogol não tem; entra só pela RSSSF
- Nova Cidade — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nova Cidade)
- Olaria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olaria)
- Paduano — clube que o ogol não tem; entra só pela RSSSF
- União Nacional — clube que o ogol não tem; entra só pela RSSSF
- placar diferente no ogol — Fluminense x Campo Grande-RJ (1991-11-04): RSSSF 3-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Flamengo x Bangu (1991-10-06): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — América-RJ x Campo Grande-RJ (1991-11-10): RSSSF 1-1, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Botafogo x Fluminense (1991-11-17): RSSSF 2-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Fluminense x Bangu (1991-11-25): RSSSF 0-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Flamengo x Campo Grande-RJ (1991-12-02): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Bangu x São Cristóvão (1991-11-03): RSSSF 0-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Fluminense x Botafogo (1991-09-08): RSSSF 2-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Campo Grande-RJ x América de Três Rios (1991-11-17): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- mando invertido no ogol — RSSSF Vasco 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Vasco (1991-08-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-0 Bangu (1991-08-24); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Flamengo, ogol Flamengo 1-2 Fluminense (1991-09-01); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-0 Itaperuna, ogol Itaperuna 0-3 Fluminense (1991-09-18); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 Portuguesa-RJ, ogol Portuguesa-RJ 0-1 Botafogo (1991-09-18); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-1 São Cristóvão, ogol São Cristóvão 1-3 Fluminense (1991-10-19); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-0 Itaperuna, ogol Itaperuna 0-0 Bangu (1991-10-19); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-1 São Cristóvão, ogol São Cristóvão 1-2 América-RJ (1991-10-30); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-3 Vasco, ogol Vasco 3-3 Botafogo (1991-11-03); fica a RSSSF
- mando invertido no ogol — RSSSF Goytacaz 1-1 Itaperuna, ogol Itaperuna 1-1 Goytacaz (1991-11-10); fica a RSSSF
- mando invertido no ogol — RSSSF Itaperuna 0-3 Vasco, ogol Vasco 3-0 Itaperuna (1991-11-17); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 4-0 Fluminense, ogol Fluminense 0-4 Vasco (1991-12-01); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-0 Itaperuna, ogol Itaperuna 0-1 Campo Grande-RJ (1991-12-07); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-1 América-RJ, ogol América-RJ 1-1 Fluminense (1991-12-07); fica a RSSSF
- jogo só no ogol, incluído em First Stage - First Phase / Group A: Campo Grande-RJ 1-3 Fluminense (1991-08-24)
- jogo só no ogol, incluído em First Stage - First Phase / Group A: Bangu 0-1 Flamengo (1991-08-29)
- jogo só no ogol, incluído em First Stage - First Phase / Group A: Campo Grande-RJ 1-1 América-RJ (1991-09-01)
- jogo só no ogol, incluído em First Stage - First Phase / Group A: Bangu 0-0 Fluminense (1991-09-14)
- jogo só no ogol, incluído em First Stage - First Phase / Group A: Campo Grande-RJ 1-1 Flamengo (1991-09-22)
- só na RSSSF (não achado no ogol): Miguel Couto 0-1 Bangu (None)
- só na RSSSF (não achado no ogol): Madureira 1-0 Goytacaz (None)
- só na RSSSF (não achado no ogol): Paduano 1-1 Mesquita (None)
- só na RSSSF (não achado no ogol): Olaria 2-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Cabofriense 0-2 União Nacional (None)
- só na RSSSF (não achado no ogol): São Cristóvão 4-1 Paduano (None)
- só na RSSSF (não achado no ogol): Bangu 0-0 Madureira (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Miguel Couto (None)
- só na RSSSF (não achado no ogol): União Nacional 0-0 Bangu (None)
- só na RSSSF (não achado no ogol): Goytacaz 2-1 Olaria (None)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Cabofriense (None)
- só na RSSSF (não achado no ogol): Miguel Couto 1-1 Madureira (None)
- só na RSSSF (não achado no ogol): Paduano 1-1 União Nacional (None)
- só na RSSSF (não achado no ogol): Olaria 0-0 Bangu (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Bangu 0-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Cabofriense 1-2 Goytacaz (None)
- só na RSSSF (não achado no ogol): São Cristóvão 3-1 Miguel Couto (None)
- só na RSSSF (não achado no ogol): União Nacional 0-1 Mesquita (None)
- só na RSSSF (não achado no ogol): Madureira 0-0 Olaria (None)
- só na RSSSF (não achado no ogol): Friburguense 2-0 Paduano (None)
- só na RSSSF (não achado no ogol): Bangu 1-0 Cabofriense (None)
- só na RSSSF (não achado no ogol): Bangu 2-0 Bangu (None)
- só na RSSSF (não achado no ogol): São Cristóvão 2-0 União Nacional (None)
- só na RSSSF (não achado no ogol): Miguel Couto 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Paduano 1-2 Goytacaz (None)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 Madureira (None)
- só na RSSSF (não achado no ogol): Mesquita 2-0 Friburguense (None)
- só na RSSSF (não achado no ogol): Goytacaz 1-0 Mesquita (None)
- só na RSSSF (não achado no ogol): União Nacional 0-0 Miguel Couto (None)
- só na RSSSF (não achado no ogol): Bangu 1-0 Paduano (None)
- só na RSSSF (não achado no ogol): Madureira 1-1 Bangu (None)
- só na RSSSF (não achado no ogol): Olaria 3-2 Cabofriense (None)
- só na RSSSF (não achado no ogol): Friburguense 0-1 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Bangu 4-1 Olaria (None)
- só na RSSSF (não achado no ogol): Miguel Couto 0-1 Cabofriense (None)
- só na RSSSF (não achado no ogol): Paduano 0-1 Madureira (None)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Bangu (None)
- só na RSSSF (não achado no ogol): União Nacional 0-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 União Nacional (None)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Miguel Couto (None)
- só na RSSSF (não achado no ogol): Olaria 2-0 Paduano (None)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 Bangu (None)
- só na RSSSF (não achado no ogol): Madureira 2-2 Mesquita (None)
- só na RSSSF (não achado no ogol): Bangu 1-1 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Miguel Couto 0-0 Bangu (None)
- só na RSSSF (não achado no ogol): Paduano 1-1 Cabofriense (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): São Cristóvão 2-1 Madureira (None)
- só na RSSSF (não achado no ogol): União Nacional 1-0 Bangu (None)
- só na RSSSF (não achado no ogol): Friburguense 0-0 Goytacaz (None)
- só na RSSSF (não achado no ogol): Goytacaz 3-1 Miguel Couto (None)
- só na RSSSF (não achado no ogol): Bangu 1-1 Paduano (None)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 Mesquita (None)
- só na RSSSF (não achado no ogol): Olaria 0-0 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Madureira 2-1 União Nacional (None)
- só na RSSSF (não achado no ogol): Bangu 1-0 Friburguense (None)
- só na RSSSF (não achado no ogol): Miguel Couto 0-1 Paduano (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Bangu (None)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Cabofriense (None)
- só na RSSSF (não achado no ogol): União Nacional 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Madureira (None)
- só na RSSSF (não achado no ogol): Goytacaz 1-0 Bangu (None)
- só na RSSSF (não achado no ogol): Goytacaz 0-0 Mesquita (None)
- só na RSSSF (não achado no ogol): Flamengo 2-1 Bangu (None)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Goytacaz (None)
- só na RSSSF (não achado no ogol): Bangu 2-1 São Cristóvão (None)
- só na RSSSF (não achado no ogol): Fluminense 1-1 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): América-RJ 4-2 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): Fluminense 3-1 Bangu (None)
- só na RSSSF (não achado no ogol): Goytacaz 1-0 Bangu (None)
- só na RSSSF (não achado no ogol): Flamengo 1-0 Campo Grande-RJ (None)
- só na RSSSF (não achado no ogol): Bonsucesso 1-1 Miguel Couto (None)
- só na RSSSF (não achado no ogol): Madureira 1-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Paduano (None)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Nova Cidade (None)
- só na RSSSF (não achado no ogol): União Nacional 3-2 Cabofriense (None)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Nova Cidade 1-2 União Nacional (None)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Olaria 3-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Madureira 3-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Paduano 3-2 Volta Redonda (None)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-0 Cabofriense (None)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Madureira 1-0 Miguel Couto (None)
- só na RSSSF (não achado no ogol): União Nacional 1-1 Paduano (None)
- só na RSSSF (não achado no ogol): Friburguense 1-1 Nova Cidade (None)
- só na RSSSF (não achado no ogol): Volta Redonda 3-2 Mesquita (None)
- só na RSSSF (não achado no ogol): Nova Cidade 0-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Paduano 0-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Madureira 2-0 Olaria (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 União Nacional (None)
- só na RSSSF (não achado no ogol): Olaria 4-1 Miguel Couto (None)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 2-1 Paduano (None)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Nova Cidade (None)
- só na RSSSF (não achado no ogol): Madureira 1-0 Cabofriense (None)
- só na RSSSF (não achado no ogol): Friburguense 1-1 Mesquita (None)
- só na RSSSF (não achado no ogol): União Nacional 0-2 Volta Redonda (None)
- só na RSSSF (não achado no ogol): Nova Cidade 0-0 Madureira (None)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Paduano 2-0 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 Olaria (None)
- só na RSSSF (não achado no ogol): Volta Redonda 0-0 Friburguense (None)
- só na RSSSF (não achado no ogol): Madureira 2-1 Paduano (None)
- só na RSSSF (não achado no ogol): Olaria 0-0 Nova Cidade (None)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Mesquita (None)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Volta Redonda (None)
- só na RSSSF (não achado no ogol): Friburguense 1-1 União Nacional (None)
- só na RSSSF (não achado no ogol): União Nacional 1-0 Portuguesa-RJ (None)
- só na RSSSF (não achado no ogol): Paduano 1-0 Olaria (None)
- só na RSSSF (não achado no ogol): Nova Cidade 0-1 Cabofriense (None)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Madureira (None)
- só na RSSSF (não achado no ogol): Volta Redonda 5-0 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Cabofriense 0-0 Paduano (None)
- só na RSSSF (não achado no ogol): Olaria 0-1 Mesquita (None)
- só na RSSSF (não achado no ogol): Madureira 0-1 Volta Redonda (None)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 União Nacional (None)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Friburguense (None)
- só na RSSSF (não achado no ogol): Paduano 3-1 Nova Cidade (None)
- só na RSSSF (não achado no ogol): Mesquita 1-1 Cabofriense (None)
- só na RSSSF (não achado no ogol): Volta Redonda 2-0 Olaria (None)
- só na RSSSF (não achado no ogol): União Nacional 0-1 Madureira (None)
- só na RSSSF (não achado no ogol): Friburguense 1-1 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Nova Cidade 0-1 Mesquita (None)
- só na RSSSF (não achado no ogol): Olaria 0-0 União Nacional (None)
- só na RSSSF (não achado no ogol): Madureira 2-2 Friburguense (None)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 3-0 Bonsucesso (None)
- só na RSSSF (não achado no ogol): Cabofriense 0-0 Volta Redonda (None)

### 1992

- tabela publicada x jogos — 1º Turno / Grupo B: Paduano tabela [13, 3, 3, 7, 10, 16] jogos [13, 3, 3, 7, 11, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / Grupo B: Olympico FC tabela [13, 1, 2, 10, 14, 33] jogos [13, 1, 2, 10, 14, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo A: Campo Grande-RJ tabela [13, 3, 3, 7, 9, 13] jogos [14, 3, 4, 7, 10, 14] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / Grupo A: Madureira tabela [13, 1, 5, 7, 5, 18] jogos [14, 1, 6, 7, 6, 19] — a tabela conta 13 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA Cabofriense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barra Mansa FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bonsucesso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Entrerriense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Friburguense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mesquita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olympico FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paduano EC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Saquarema FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Nacional FC
- AA Cabofriense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabofriense)
- Barra Mansa FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barra Mansa)
- Bonsucesso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bonsucesso)
- Entrerriense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Entrerriense)
- Friburguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Friburguense)
- Mesquita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mesquita)
- Olympico FC — clube que o ogol não tem; entra só pela RSSSF
- Paduano EC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paduano)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa-RJ)
- Saquarema FC — clube que o ogol não tem; entra só pela RSSSF
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão)
- União Nacional FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Nacional)
- mando invertido no ogol — RSSSF América-RJ 0-1 Fluminense, ogol Fluminense 1-0 América-RJ (1992-09-12); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-4 Vasco, ogol Vasco 4-0 América-RJ (1992-09-20); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-2 Botafogo, ogol Botafogo 2-1 Campo Grande-RJ (1992-09-21); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Vasco, ogol Vasco 1-1 Flamengo (1992-10-04); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-2 Campo Grande-RJ, ogol Campo Grande-RJ 2-3 Vasco (1992-10-12); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-2 América de Três Rios, ogol América de Três Rios 2-0 Americano-RJ (1992-10-17); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-0 Olaria, ogol Olaria 0-0 Fluminense (1992-10-18); fica a RSSSF
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-2 Botafogo, ogol Botafogo 2-1 Campo Grande-RJ (1992-10-19); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-0 Itaperuna, ogol Itaperuna 0-3 Vasco (1992-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 1-0 América-RJ, ogol América-RJ 0-1 Olaria (1992-10-22); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-2 Botafogo, ogol Botafogo 2-2 Fluminense (1992-10-24); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-4 Flamengo, ogol Flamengo 4-0 América-RJ (1992-11-02); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-2 Botafogo, ogol Botafogo 2-1 Flamengo (1992-11-08); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-0 Bangu, ogol Bangu 0-0 Fluminense (1992-11-09); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-3 Vasco, ogol Vasco 3-1 Botafogo (1992-11-14); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Madureira, ogol Madureira 0-0 Botafogo (1992-11-18); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 2-1 Fluminense, ogol Fluminense 1-2 Americano-RJ (1992-11-19); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Botafogo, ogol Botafogo 1-1 América-RJ (1992-11-21); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-0 Flamengo, ogol Flamengo 0-1 Fluminense (1992-11-22); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-1 Vasco, ogol Vasco 1-0 Bangu (1992-11-24); fica a RSSSF
- mando invertido no ogol — RSSSF América de Três Rios 0-4 Flamengo, ogol Flamengo 4-0 América de Três Rios (1992-11-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 Vasco, ogol Vasco 1-0 Fluminense (1992-11-29); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-1 Vasco, ogol Vasco 1-1 Flamengo (1992-12-06); fica a RSSSF
- mando invertido no ogol — RSSSF Itaperuna 0-3 Botafogo, ogol Botafogo 3-0 Itaperuna (1992-12-06); fica a RSSSF
- mando invertido no ogol — RSSSF Olaria 0-0 Madureira, ogol Madureira 0-0 Olaria (1992-12-06); fica a RSSSF
- placar diferente no ogol — América-RJ x Madureira (1992-09-22): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Bangu x América de Três Rios (1992-09-28): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Botafogo x Olaria (1992-11-04): RSSSF 0-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — América-RJ x Campo Grande-RJ (1992-11-16): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Olaria x Campo Grande-RJ (1992-11-22): RSSSF 2-0, ogol 2-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Volta Redonda x Americano-RJ, ogol 1992-09-30); fica a do ogol
- mando invertido no ogol — RSSSF Fluminense 1-1 Vasco, ogol Vasco 1-1 Fluminense (1992-09-29); fica a RSSSF
- jogo só no ogol, incluído em 2º Turno (Taça Rio de Janeiro) / Group A: Campo Grande-RJ 1-1 Madureira (1992-11-30)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Goytacaz (1992-08-01)
- só na RSSSF (não achado no ogol): Olaria 3-0 Paduano (1992-08-01)
- só na RSSSF (não achado no ogol): Barra Mansa 2-0 Mesquita (1992-08-02)
- só na RSSSF (não achado no ogol): São Cristóvão 5-0 Olympico FC (1992-08-02)
- só na RSSSF (não achado no ogol): Friburguense 2-2 Portuguesa-RJ (1992-08-02)
- só na RSSSF (não achado no ogol): Saquarema FC 0-0 União Nacional (1992-08-02)
- só na RSSSF (não achado no ogol): Entrerriense 1-0 Cabofriense (1992-08-02)
- só na RSSSF (não achado no ogol): Olaria 0-0 Friburguense (1992-08-08)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 União Nacional (1992-08-08)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-0 Saquarema FC (1992-08-08)
- só na RSSSF (não achado no ogol): Mesquita 1-1 Entrerriense (1992-08-09)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 Goytacaz (1992-08-09)
- só na RSSSF (não achado no ogol): Paduano 1-0 Barra Mansa (1992-08-09)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 Bonsucesso (1992-08-09)
- só na RSSSF (não achado no ogol): Olympico FC 0-4 Olaria (1992-08-15)
- só na RSSSF (não achado no ogol): Bonsucesso 0-0 Paduano (1992-08-15)
- só na RSSSF (não achado no ogol): Mesquita 0-1 Cabofriense (1992-08-16)
- só na RSSSF (não achado no ogol): Goytacaz 3-0 Barra Mansa (1992-08-16)
- só na RSSSF (não achado no ogol): Friburguense 2-0 São Cristóvão (1992-08-16)
- só na RSSSF (não achado no ogol): União Nacional 1-0 Portuguesa-RJ (1992-08-16)
- só na RSSSF (não achado no ogol): Entrerriense 2-1 Saquarema FC (1992-08-16)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-1 São Cristóvão (1992-08-22)
- só na RSSSF (não achado no ogol): Saquarema FC 2-2 Mesquita (1992-08-23)
- só na RSSSF (não achado no ogol): Goytacaz 0-0 Entrerriense (1992-08-23)
- só na RSSSF (não achado no ogol): Paduano 1-1 Cabofriense (1992-08-23)
- só na RSSSF (não achado no ogol): Barra Mansa 3-1 Olympico FC (1992-08-23)
- só na RSSSF (não achado no ogol): Friburguense 5-1 Bonsucesso (1992-08-23)
- só na RSSSF (não achado no ogol): União Nacional 1-1 Olaria (1992-08-23)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Barra Mansa (1992-08-26)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Bonsucesso (1992-08-26)
- só na RSSSF (não achado no ogol): Goytacaz 1-0 Olaria (1992-08-26)
- só na RSSSF (não achado no ogol): Paduano 0-0 São Cristóvão (1992-08-26)
- só na RSSSF (não achado no ogol): Olympico FC 2-3 Portuguesa-RJ (1992-08-26)
- só na RSSSF (não achado no ogol): União Nacional 1-1 Friburguense (1992-08-26)
- só na RSSSF (não achado no ogol): Cabofriense 2-0 Saquarema FC (1992-08-27)
- só na RSSSF (não achado no ogol): Olaria 2-1 Mesquita (1992-08-29)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Entrerriense (1992-08-29)
- só na RSSSF (não achado no ogol): São Cristóvão 1-1 Goytacaz (1992-08-29)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Paduano (1992-08-29)
- só na RSSSF (não achado no ogol): União Nacional 2-1 Olympico FC (1992-08-30)
- só na RSSSF (não achado no ogol): Saquarema FC 2-1 Friburguense (1992-08-30)
- só na RSSSF (não achado no ogol): Barra Mansa 1-0 Cabofriense (1992-08-30)
- só na RSSSF (não achado no ogol): Mesquita 0-0 São Cristóvão (1992-09-06)
- só na RSSSF (não achado no ogol): Goytacaz 4-0 Portuguesa-RJ (1992-09-06)
- só na RSSSF (não achado no ogol): Paduano 0-1 União Nacional (1992-09-06)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 Friburguense (1992-09-06)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Bonsucesso (1992-09-06)
- só na RSSSF (não achado no ogol): Olaria 3-0 Entrerriense (1992-09-06)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-0 Mesquita (1992-09-09)
- só na RSSSF (não achado no ogol): União Nacional 1-1 Goytacaz (1992-09-09)
- só na RSSSF (não achado no ogol): Friburguense 4-2 Paduano (1992-09-09)
- só na RSSSF (não achado no ogol): Olaria 0-0 Cabofriense (1992-09-09)
- só na RSSSF (não achado no ogol): São Cristóvão 0-2 Entrerriense (1992-09-09)
- só na RSSSF (não achado no ogol): Bonsucesso 2-0 Barra Mansa (1992-09-09)
- só na RSSSF (não achado no ogol): Saquarema FC 3-1 Olympico FC (1992-09-10)
- só na RSSSF (não achado no ogol): Mesquita 1-0 União Nacional (1992-09-13)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 Friburguense (1992-09-13)
- só na RSSSF (não achado no ogol): Paduano 6-2 Olympico FC (1992-09-13)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Portuguesa-RJ (1992-09-13)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 São Cristóvão (1992-09-13)
- só na RSSSF (não achado no ogol): Saquarema FC 2-0 Bonsucesso (1992-09-13)
- só na RSSSF (não achado no ogol): Barra Mansa 0-1 Olaria (1992-09-13)
- só na RSSSF (não achado no ogol): Barra Mansa 1-1 Saquarema FC (1992-09-16)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-0 Barra Mansa (1992-09-19)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Bonsucesso (1992-09-19)
- só na RSSSF (não achado no ogol): Mesquita 2-1 Olympico FC (1992-09-20)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 Paduano (1992-09-20)
- só na RSSSF (não achado no ogol): Entrerriense 4-2 Friburguense (1992-09-20)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 União Nacional (1992-09-20)
- só na RSSSF (não achado no ogol): Saquarema FC 2-1 Olaria (1992-09-20)
- só na RSSSF (não achado no ogol): Mesquita 0-1 Goytacaz (1992-09-23)
- só na RSSSF (não achado no ogol): Entrerriense 1-0 Paduano (1992-09-23)
- só na RSSSF (não achado no ogol): Cabofriense 0-2 Olympico FC (1992-09-23)
- só na RSSSF (não achado no ogol): Friburguense 2-1 Barra Mansa (1992-09-23)
- só na RSSSF (não achado no ogol): Bonsucesso 3-0 União Nacional (1992-09-23)
- só na RSSSF (não achado no ogol): Olaria 1-2 Portuguesa-RJ (1992-09-23)
- só na RSSSF (não achado no ogol): São Cristóvão 1-1 Saquarema FC (1992-09-23)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-1 Bonsucesso (1992-09-26)
- só na RSSSF (não achado no ogol): Olaria 3-2 São Cristóvão (1992-09-26)
- só na RSSSF (não achado no ogol): Paduano 0-1 Mesquita (1992-09-27)
- só na RSSSF (não achado no ogol): Saquarema FC 0-0 Goytacaz (1992-09-27)
- só na RSSSF (não achado no ogol): Olympico FC 1-1 Entrerriense (1992-09-27)
- só na RSSSF (não achado no ogol): Friburguense 2-0 Cabofriense (1992-09-27)
- só na RSSSF (não achado no ogol): Barra Mansa 0-0 União Nacional (1992-09-27)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 3-1 Cabofriense (1992-10-03)
- só na RSSSF (não achado no ogol): Bonsucesso 0-1 Olaria (1992-10-03)
- só na RSSSF (não achado no ogol): Barra Mansa 1-1 São Cristóvão (1992-10-04)
- só na RSSSF (não achado no ogol): Friburguense 2-0 Mesquita (1992-10-04)
- só na RSSSF (não achado no ogol): Olympico FC 1-1 Goytacaz (1992-10-04)
- só na RSSSF (não achado no ogol): Paduano 0-1 Saquarema FC (1992-10-04)
- só na RSSSF (não achado no ogol): União Nacional 0-1 Entrerriense (1992-10-04)
- só na RSSSF (não achado no ogol): Madureira 1-3 Campo Grande-RJ (1992-10-31)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Cabofriense (1992-10-17)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-2 Olympico FC (1992-10-17)
- só na RSSSF (não achado no ogol): Paduano 1-1 Friburguense (1992-10-18)
- só na RSSSF (não achado no ogol): Mesquita 4-0 Barra Mansa (1992-10-18)
- só na RSSSF (não achado no ogol): União Nacional 0-1 Saquarema FC (1992-10-18)
- só na RSSSF (não achado no ogol): São Cristóvão 3-1 Mesquita (1992-10-24)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-1 Entrerriense (1992-10-24)
- só na RSSSF (não achado no ogol): Bonsucesso 1-1 Olympico FC (1992-10-24)
- só na RSSSF (não achado no ogol): Cabofriense 0-0 Friburguense (1992-10-25)
- só na RSSSF (não achado no ogol): União Nacional 2-1 Barra Mansa (1992-10-25)
- só na RSSSF (não achado no ogol): Saquarema FC 2-0 Paduano (1992-10-25)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 União Nacional (1992-10-28)
- só na RSSSF (não achado no ogol): Friburguense 3-1 Olympico FC (1992-10-28)
- só na RSSSF (não achado no ogol): Mesquita 0-1 Portuguesa-RJ (1992-10-28)
- só na RSSSF (não achado no ogol): Cabofriense 0-0 Paduano (1992-10-28)
- só na RSSSF (não achado no ogol): Saquarema FC 0-0 Barra Mansa (1992-10-28)
- só na RSSSF (não achado no ogol): Entrerriense 3-1 Bonsucesso (1992-10-28)
- só na RSSSF (não achado no ogol): Bonsucesso 0-0 Friburguense (1992-10-31)
- só na RSSSF (não achado no ogol): Mesquita 1-1 Saquarema FC (1992-11-01)
- só na RSSSF (não achado no ogol): Olympico FC 1-0 São Cristóvão (1992-11-01)
- só na RSSSF (não achado no ogol): Barra Mansa 0-0 Entrerriense (1992-11-01)
- só na RSSSF (não achado no ogol): União Nacional 0-0 Paduano (1992-11-01)
- só na RSSSF (não achado no ogol): Cabofriense 0-0 Portuguesa-RJ (1992-11-04)
- só na RSSSF (não achado no ogol): Cabofriense 1-2 Mesquita (1992-11-07)
- só na RSSSF (não achado no ogol): Friburguense 1-0 União Nacional (1992-11-08)
- só na RSSSF (não achado no ogol): Barra Mansa 0-0 Portuguesa-RJ (1992-11-08)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Olympico FC (1992-11-08)
- só na RSSSF (não achado no ogol): Bonsucesso 2-0 Saquarema FC (1992-11-11)
- só na RSSSF (não achado no ogol): Entrerriense 2-1 São Cristóvão (1992-11-11)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Portuguesa-RJ (1992-11-14)
- só na RSSSF (não achado no ogol): Friburguense 5-3 Saquarema FC (1992-11-15)
- só na RSSSF (não achado no ogol): Olympico FC 0-0 Mesquita (1992-11-15)
- só na RSSSF (não achado no ogol): União Nacional 2-0 Cabofriense (1992-11-15)
- só na RSSSF (não achado no ogol): Barra Mansa 0-1 Bonsucesso (1992-11-15)
- só na RSSSF (não achado no ogol): Paduano 0-1 Entrerriense (1992-11-15)
- só na RSSSF (não achado no ogol): Bonsucesso 2-2 São Cristóvão (1992-11-18)
- só na RSSSF (não achado no ogol): Barra Mansa 0-0 Friburguense (1992-11-18)
- só na RSSSF (não achado no ogol): Saquarema FC 3-0 Cabofriense (1992-11-18)
- só na RSSSF (não achado no ogol): Olympico FC 0-0 União Nacional (1992-11-18)
- só na RSSSF (não achado no ogol): Paduano 1-2 Portuguesa-RJ (1992-11-18)
- só na RSSSF (não achado no ogol): Entrerriense 0-0 Mesquita (1992-11-19)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-0 Friburguense (1992-11-21)
- só na RSSSF (não achado no ogol): União Nacional 1-0 Mesquita (1992-11-22)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 Barra Mansa (1992-11-22)
- só na RSSSF (não achado no ogol): Entrerriense 1-0 Saquarema FC (1992-11-22)
- só na RSSSF (não achado no ogol): Paduano 2-0 Bonsucesso (1992-11-22)
- só na RSSSF (não achado no ogol): São Cristóvão 2-0 Paduano (1992-11-25)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Barra Mansa (1992-11-28)
- só na RSSSF (não achado no ogol): Mesquita 1-1 Friburguense (1992-11-29)
- só na RSSSF (não achado no ogol): Cabofriense 0-2 Entrerriense (1992-11-29)
- só na RSSSF (não achado no ogol): União Nacional 1-1 Bonsucesso (1992-11-29)
- só na RSSSF (não achado no ogol): Saquarema FC 1-1 Portuguesa-RJ (1992-11-29)
- só na RSSSF (não achado no ogol): Paduano 0-2 Olympico FC (1992-11-29)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Cabofriense (1992-12-02)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-0 Bonsucesso (1992-12-06)
- só na RSSSF (não achado no ogol): Friburguense 0-0 São Cristóvão (1992-12-06)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 Barra Mansa (1992-12-06)
- só na RSSSF (não achado no ogol): Entrerriense 4-1 União Nacional (1992-12-06)
- só na RSSSF (não achado no ogol): Olympico FC 3-1 Saquarema FC (1992-12-06)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Paduano (1992-12-06)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 3-0 União Nacional (1992-12-12)
- só na RSSSF (não achado no ogol): Bonsucesso 0-0 Mesquita (1992-12-13)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Entrerriense (1992-12-13)
- só na RSSSF (não achado no ogol): Saquarema FC 2-2 São Cristóvão (1992-12-13)
- só na RSSSF (não achado no ogol): Barra Mansa 4-0 Paduano (1992-12-13)
- só na RSSSF (não achado no ogol): Olympico FC 9-1 Cabofriense (1992-12-20)

### 1993

- tabela publicada x jogos — 2º Turno / Grupo B: Barreira tabela [11, 4, 2, 5, 13, 13] jogos [10, 4, 2, 4, 13, 13] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / Grupo B: Mesquita tabela [11, 3, 4, 4, 3, 9] jogos [10, 2, 4, 4, 3, 9] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / Grupo B: Entrerriense tabela [11, 3, 4, 4, 10, 8] jogos [11, 2, 4, 5, 10, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo B: Goytacaz tabela [11, 2, 4, 5, 10, 15] jogos [11, 3, 4, 4, 11, 15] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barreira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Grande
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Friburguense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goytacaz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Madureira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mesquita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olympico FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Saquarema FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Serrano
- Barreira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barreira)
- Campo Grande — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Grande-RJ)
- Friburguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Friburguense)
- Goytacaz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goytacaz)
- Madureira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Madureira)
- Mesquita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mesquita)
- Olympico FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olympico FC)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa-RJ)
- Saquarema FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saquarema FC)
- Serrano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Serrano)
- mando invertido no ogol — RSSSF América de Três Rios 1-2 Volta Redonda, ogol Volta Redonda 2-1 América de Três Rios (1993-02-14); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 6-1 Americano-RJ, ogol Americano-RJ 1-6 Botafogo (1993-03-01); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Flamengo, ogol Flamengo 1-2 Fluminense (1993-03-14); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-3 Vasco, ogol Vasco 3-0 América-RJ (1993-03-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Flamengo, ogol Flamengo 1-1 Botafogo (1993-03-28); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Fluminense, ogol Fluminense 1-1 América-RJ (1993-03-29); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-2 Botafogo, ogol Botafogo 2-2 América-RJ (1993-04-01); fica a RSSSF
- mando invertido no ogol — RSSSF São Cristóvão 1-1 América-RJ, ogol América-RJ 1-1 São Cristóvão (1993-04-04); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-3 Fluminense, ogol Fluminense 3-0 Botafogo (1993-04-04); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-0 Volta Redonda, ogol Volta Redonda 0-1 Fluminense (1993-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 1-2 Vasco, ogol Vasco 2-1 Flamengo (1993-04-11); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-4 Flamengo, ogol Flamengo 4-2 América-RJ (1993-04-17); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 0-1 Vasco, ogol Vasco 1-0 Volta Redonda (1993-04-19); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-2 Americano-RJ, ogol Americano-RJ 2-2 Flamengo (1993-04-19); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-2 Vasco, ogol Vasco 2-1 Botafogo (1993-05-09); fica a RSSSF
- mando invertido no ogol — RSSSF Bonsucesso 1-3 Flamengo, ogol Flamengo 3-1 Bonsucesso (1993-05-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Vasco, ogol Vasco 0-1 Bangu (1993-05-11); fica a RSSSF
- placar diferente no ogol — Fluminense x Botafogo (1993-05-16): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Vasco x América-RJ, ogol 1993-05-26); fica a do ogol
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-0 Saquarema FC (1993-02-06)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Olympico FC (1993-02-06)
- só na RSSSF (não achado no ogol): Serrano 1-1 Goytacaz (1993-02-07)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 2-1 Mesquita (1993-02-07)
- só na RSSSF (não achado no ogol): Barreira 0-3 Madureira (1993-02-07)
- só na RSSSF (não achado no ogol): Friburguense 1-2 Itaperuna (1993-02-07)
- só na RSSSF (não achado no ogol): Madureira 1-1 Campo Grande-RJ (1993-02-13)
- só na RSSSF (não achado no ogol): Saquarema FC 2-1 Serrano (1993-02-14)
- só na RSSSF (não achado no ogol): Olympico FC 0-0 Portuguesa-RJ (1993-02-14)
- só na RSSSF (não achado no ogol): Mesquita 0-1 Bonsucesso (1993-02-14)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Barreira (1993-02-14)
- só na RSSSF (não achado no ogol): Goytacaz 2-1 Friburguense (1993-02-14)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 2-1 Mesquita (1993-02-27)
- só na RSSSF (não achado no ogol): Bonsucesso 2-0 Madureira (1993-02-27)
- só na RSSSF (não achado no ogol): Saquarema FC 4-1 Olympico FC (1993-02-27)
- só na RSSSF (não achado no ogol): Serrano 0-1 Friburguense (1993-02-28)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 0-1 Itaperuna (1993-02-28)
- só na RSSSF (não achado no ogol): Barreira 1-0 Goytacaz (1993-02-28)
- só na RSSSF (não achado no ogol): Madureira 1-2 Portuguesa-RJ (1993-03-03)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 Serrano (1993-03-03)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Bonsucesso (1993-03-03)
- só na RSSSF (não achado no ogol): Goytacaz 0-0 Campo Grande-RJ (1993-03-03)
- só na RSSSF (não achado no ogol): Friburguense 0-2 Barreira (1993-03-03)
- só na RSSSF (não achado no ogol): Mesquita 1-1 Saquarema FC (1993-03-03)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Itaperuna (1993-03-06)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Goytacaz (1993-03-06)
- só na RSSSF (não achado no ogol): Serrano 1-1 Barreira (1993-03-07)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 1-2 Friburguense (1993-03-07)
- só na RSSSF (não achado no ogol): Saquarema FC 2-1 Madureira (1993-03-07)
- só na RSSSF (não achado no ogol): Olympico FC 0-1 Mesquita (1993-03-07)
- só na RSSSF (não achado no ogol): Madureira 3-1 Olympico FC (1993-03-13)
- só na RSSSF (não achado no ogol): Mesquita 2-0 Serrano (1993-03-14)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 Portuguesa-RJ (1993-03-14)
- só na RSSSF (não achado no ogol): Friburguense 0-1 Bonsucesso (1993-03-14)
- só na RSSSF (não achado no ogol): Barreira 3-0 Campo Grande-RJ (1993-03-14)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Saquarema FC (1993-03-14)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-4 Friburguense (1993-03-20)
- só na RSSSF (não achado no ogol): Bonsucesso 1-0 Barreira (1993-03-20)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Madureira (1993-03-20)
- só na RSSSF (não achado no ogol): Serrano 0-0 Campo Grande-RJ (1993-03-21)
- só na RSSSF (não achado no ogol): Saquarema FC 0-2 Goytacaz (1993-03-21)
- só na RSSSF (não achado no ogol): Olympico FC 0-1 Itaperuna (1993-03-21)
- só na RSSSF (não achado no ogol): Madureira 0-0 Serrano (1993-03-27)
- só na RSSSF (não achado no ogol): Barreira 1-0 Portuguesa-RJ (1993-03-28)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 2-3 Bonsucesso (1993-03-28)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Saquarema FC (1993-03-28)
- só na RSSSF (não achado no ogol): Goytacaz 2-1 Olympico FC (1993-03-28)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Mesquita (1993-03-28)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-0 Campo Grande-RJ (1993-04-03)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Goytacaz (1993-04-03)
- só na RSSSF (não achado no ogol): Madureira 0-1 Itaperuna (1993-04-03)
- só na RSSSF (não achado no ogol): Serrano 1-1 Bonsucesso (1993-04-04)
- só na RSSSF (não achado no ogol): Saquarema FC 1-0 Barreira (1993-04-04)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 Friburguense (1993-04-04)
- só na RSSSF (não achado no ogol): Bonsucesso 3-1 Portuguesa-RJ (1993-04-07)
- só na RSSSF (não achado no ogol): Itaperuna 2-0 Serrano (1993-04-07)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 3-0 Saquarema FC (1993-04-07)
- só na RSSSF (não achado no ogol): Barreira 2-0 Olympico FC (1993-04-07)
- só na RSSSF (não achado no ogol): Friburguense 3-1 Mesquita (1993-04-07)
- só na RSSSF (não achado no ogol): Goytacaz 1-1 Madureira (1993-04-07)
- só na RSSSF (não achado no ogol): Madureira 0-2 Friburguense (1993-04-10)
- só na RSSSF (não achado no ogol): Serrano 5-2 Portuguesa-RJ (1993-04-11)
- só na RSSSF (não achado no ogol): Saquarema FC 0-2 Bonsucesso (1993-04-11)
- só na RSSSF (não achado no ogol): Olympico FC 2-1 Campo Grande-RJ (1993-04-11)
- só na RSSSF (não achado no ogol): Mesquita 0-2 Barreira (1993-04-11)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Goytacaz (1993-04-11)
- só na RSSSF (não achado no ogol): Madureira 3-1 Barreira (1993-04-24)
- só na RSSSF (não achado no ogol): Saquarema FC 1-0 Portuguesa-RJ (1993-04-25)
- só na RSSSF (não achado no ogol): Olympico FC 1-2 América de Três Rios (1993-04-25)
- só na RSSSF (não achado no ogol): Goytacaz 4-4 Serrano (1993-04-25)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Campo Grande-RJ (1993-04-25)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Friburguense (1993-04-25)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 0-0 Madureira (1993-05-01)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-1 Olympico FC (1993-05-01)
- só na RSSSF (não achado no ogol): América de Três Rios 1-1 Mesquita (1993-05-01)
- só na RSSSF (não achado no ogol): Barreira 1-0 Entrerriense (1993-05-02)
- só na RSSSF (não achado no ogol): Serrano 0-0 Saquarema FC (1993-05-02)
- só na RSSSF (não achado no ogol): Friburguense 2-0 Goytacaz (1993-05-02)
- só na RSSSF (não achado no ogol): Madureira 0-0 América de Três Rios (1993-05-08)
- só na RSSSF (não achado no ogol): Entrerriense 0-0 Campo Grande-RJ (1993-05-08)
- só na RSSSF (não achado no ogol): Mesquita 0-0 Portuguesa-RJ (1993-05-08)
- só na RSSSF (não achado no ogol): Friburguense 0-0 Serrano (1993-05-09)
- só na RSSSF (não achado no ogol): Goytacaz 0-0 Barreira (1993-05-09)
- só na RSSSF (não achado no ogol): Olympico FC 0-0 Saquarema FC (1993-05-09)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Madureira (1993-05-15)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 3-1 Goytacaz (1993-05-15)
- só na RSSSF (não achado no ogol): Saquarema FC 3-0 Mesquita (1993-05-15)
- só na RSSSF (não achado no ogol): Serrano 1-0 Olympico FC (1993-05-16)
- só na RSSSF (não achado no ogol): Barreira 2-1 Friburguense (1993-05-16)
- só na RSSSF (não achado no ogol): América de Três Rios 0-4 Entrerriense (1993-05-16)
- só na RSSSF (não achado no ogol): Madureira 0-0 Saquarema FC (1993-05-22)
- só na RSSSF (não achado no ogol): Entrerriense 0-1 Portuguesa-RJ (1993-05-23)
- só na RSSSF (não achado no ogol): Goytacaz 1-1 América de Três Rios (1993-05-23)
- só na RSSSF (não achado no ogol): Barreira 3-1 Serrano (1993-05-23)
- só na RSSSF (não achado no ogol): Friburguense 1-3 Campo Grande-RJ (1993-05-23)
- só na RSSSF (não achado no ogol): Mesquita 0-1 Olympico FC (1993-05-23)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 4-0 Goytacaz (1993-05-29)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 2-2 Barreira (1993-05-29)
- só na RSSSF (não achado no ogol): América de Três Rios 0-1 Friburguense (1993-05-30)
- só na RSSSF (não achado no ogol): Olympico FC 1-3 Madureira (1993-05-30)
- só na RSSSF (não achado no ogol): Serrano 0-0 Mesquita (1993-05-30)
- só na RSSSF (não achado no ogol): Saquarema FC 2-1 Entrerriense (1993-05-30)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 2-0 Serrano (1993-06-05)
- só na RSSSF (não achado no ogol): Madureira 2-0 Mesquita (1993-06-05)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Portuguesa-RJ (1993-06-06)
- só na RSSSF (não achado no ogol): Barreira 2-1 América de Três Rios (1993-06-06)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 Saquarema FC (1993-06-06)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Olympico FC (1993-06-06)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 2-1 Barreira (1993-06-12)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Entrerriense (1993-06-12)
- só na RSSSF (não achado no ogol): América de Três Rios 1-2 Campo Grande-RJ (1993-06-13)
- só na RSSSF (não achado no ogol): Serrano 0-0 Madureira (1993-06-13)
- só na RSSSF (não achado no ogol): Saquarema FC 0-1 Friburguense (1993-06-13)
- só na RSSSF (não achado no ogol): Olympico FC 1-0 Goytacaz (1993-06-13)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 1-0 Portuguesa-RJ (1993-06-19)
- só na RSSSF (não achado no ogol): América de Três Rios 1-2 Serrano (1993-06-19)
- só na RSSSF (não achado no ogol): Entrerriense 1-1 Madureira (1993-06-20)
- só na RSSSF (não achado no ogol): Barreira 0-1 Saquarema FC (1993-06-20)
- só na RSSSF (não achado no ogol): Friburguense 1-0 Olympico FC (1993-06-20)
- só na RSSSF (não achado no ogol): Goytacaz 2-0 Mesquita (1993-06-20)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 2-1 América de Três Rios (1993-06-23)
- só na RSSSF (não achado no ogol): Madureira 0-0 Goytacaz (1993-06-23)
- só na RSSSF (não achado no ogol): Mesquita 1-0 Friburguense (1993-06-23)
- só na RSSSF (não achado no ogol): Olympico FC 2-1 Barreira (1993-06-23)
- só na RSSSF (não achado no ogol): Saquarema FC 0-0 Campo Grande-RJ (1993-06-23)
- só na RSSSF (não achado no ogol): Serrano 0-2 Entrerriense (1993-06-23)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-0 Serrano (1993-06-27)
- só na RSSSF (não achado no ogol): Campo Grande-RJ 0-0 Olympico FC (1993-06-27)
- só na RSSSF (não achado no ogol): América de Três Rios 1-1 Saquarema FC (1993-06-27)
- só na RSSSF (não achado no ogol): Friburguense 0-1 Madureira (1993-06-27)
- só na RSSSF (não achado no ogol): Goytacaz 1-0 Entrerriense (1993-06-27)
- só na RSSSF (não achado no ogol): Vasco 0-0 Fluminense (1993-06-16)

### 1994

- mando invertido no ogol — RSSSF Fluminense 1-2 Botafogo, ogol Botafogo 2-1 Fluminense (1994-02-20); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-0 Campo Grande-RJ, ogol Campo Grande-RJ 0-1 América-RJ (1994-02-20); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 Madureira, ogol Madureira 0-1 Botafogo (1994-03-02); fica a RSSSF
- mando invertido no ogol — RSSSF Itaperuna 1-2 Olaria, ogol Olaria 2-1 Itaperuna (1994-03-03); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Bangu, ogol Bangu 0-0 América-RJ (1994-03-13); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Madureira, ogol Madureira 0-0 América-RJ (1994-03-26); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-0 Vasco, ogol Vasco 0-0 Fluminense (1994-03-27); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-4 Vasco, ogol Vasco 4-1 Fluminense (1994-04-03); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-1 Vasco, ogol Vasco 1-0 Botafogo (1994-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-1 Vasco, ogol Vasco 1-1 Fluminense (1994-04-17); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-1 Fluminense, ogol Fluminense 1-1 Botafogo (1994-04-22); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Americano-RJ x Olaria, ogol 1994-03-20); fica a do ogol
- vencedor da final pelos jogos (Flamengo) diferente do campeão oficial (Vasco); fica o oficial

### 1995

- tabela publicada x jogos — 2º Turno / -: Flamengo tabela [7, 4, 2, 1, 16, 9] jogos [29, 19, 6, 4, 75, 32] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Volta Redonda tabela [7, 4, 2, 1, 11, 6] jogos [28, 10, 5, 13, 29, 46] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Fluminense tabela [7, 3, 3, 1, 11, 5] jogos [28, 18, 7, 3, 49, 19] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [7, 2, 5, 0, 8, 5] jogos [28, 7, 13, 8, 31, 34] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Campo Grande-RJ tabela [7, 1, 3, 3, 2, 7] jogos [14, 1, 4, 9, 7, 25] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Friburguense tabela [7, 1, 3, 3, 4, 10] jogos [14, 2, 4, 8, 9, 24] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Madureira tabela [7, 1, 2, 4, 3, 9] jogos [14, 5, 5, 4, 13, 14] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Americano-RJ tabela [7, 0, 4, 3, 1, 5] jogos [14, 1, 6, 7, 5, 16] — a tabela conta 7 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barra
- Barra — clube que o ogol não tem; entra só pela RSSSF
- mando invertido no ogol — RSSSF Madureira 1-0 Fluminense, ogol Fluminense 0-1 Madureira (1995-01-28); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 0-1 Fluminense, ogol Fluminense 1-0 Bangu (1995-02-05); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-1 Botafogo, ogol Botafogo 1-0 Fluminense (1995-04-02); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-4 Fluminense, ogol Fluminense 4-3 Flamengo (1995-04-30); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 2-2 Volta Redonda, ogol Volta Redonda 2-2 América-RJ (1995-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-1 Fluminense, ogol Fluminense 1-0 América-RJ (1995-05-14); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 0-0 Fluminense, ogol Fluminense 0-0 Botafogo (1995-05-21); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Itaperuna x Entrerriense, ogol 1995-03-02); fica a do ogol
- mando invertido no ogol — RSSSF Campo Grande-RJ 1-5 Fluminense, ogol Fluminense 5-1 Campo Grande-RJ (1995-02-23); fica a RSSSF
- só na RSSSF (não achado no ogol): Entrerriense 3-2 Barra-RJ (1995-03-23)

### 1996

- tabela publicada x jogos — Primeira fase / -: Botafogo tabela [7, 6, 1, 0, 21, 6] jogos [29, 17, 10, 2, 68, 30] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [7, 4, 2, 1, 7, 6] jogos [29, 9, 7, 13, 24, 41] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [7, 3, 4, 0, 10, 6] jogos [29, 21, 8, 0, 67, 21] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Vasco tabela [7, 3, 2, 2, 16, 11] jogos [29, 19, 5, 5, 58, 26] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Fluminense tabela [7, 2, 2, 3, 12, 12] jogos [29, 13, 6, 10, 49, 38] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [7, 2, 1, 4, 7, 14] jogos [29, 6, 11, 12, 29, 42] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: América-RJ tabela [7, 0, 2, 5, 6, 14] jogos [29, 5, 9, 15, 27, 48] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Olaria tabela [7, 0, 2, 5, 8, 18] jogos [29, 6, 6, 17, 38, 67] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [11, 10, 1, 0, 30, 8] jogos [18, 13, 5, 0, 40, 14] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Vasco tabela [11, 9, 0, 2, 25, 13] jogos [18, 12, 2, 4, 41, 24] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fluminense tabela [11, 6, 2, 3, 20, 15] jogos [18, 8, 4, 6, 32, 27] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Botafogo tabela [11, 5, 4, 2, 22, 16] jogos [18, 11, 5, 2, 43, 22] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: América-RJ tabela [11, 3, 4, 4, 12, 13] jogos [18, 3, 6, 9, 18, 27] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [11, 3, 3, 5, 16, 15] jogos [18, 5, 4, 9, 23, 29] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [11, 2, 1, 8, 8, 19] jogos [18, 6, 3, 9, 15, 25] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Olaria tabela [11, 1, 3, 7, 13, 28] jogos [18, 1, 5, 12, 21, 46] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Flamengo tabela [11, 10, 1, 0, 30, 8] jogos [18, 13, 5, 0, 40, 14] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Vasco tabela [11, 9, 0, 2, 25, 13] jogos [18, 12, 2, 4, 41, 24] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fluminense tabela [11, 6, 2, 3, 20, 15] jogos [18, 8, 4, 6, 32, 27] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Botafogo tabela [11, 5, 4, 2, 22, 16] jogos [18, 11, 5, 2, 43, 22] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: América-RJ tabela [11, 3, 4, 4, 12, 13] jogos [18, 3, 6, 9, 18, 27] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [11, 3, 3, 5, 16, 15] jogos [18, 5, 4, 9, 23, 29] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [11, 2, 1, 8, 8, 19] jogos [18, 6, 3, 9, 15, 25] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Olaria tabela [11, 1, 3, 7, 13, 28] jogos [18, 1, 5, 12, 21, 46] — a tabela conta 11 jogos e as fontes trazem 18
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barreirense
- Barreirense — clube que o ogol não tem; entra só pela RSSSF
- mando invertido no ogol — RSSSF Bangu 4-1 Barreira, ogol Barreira 1-4 Bangu (1996-03-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-2 Flamengo, ogol Flamengo 2-1 Bangu (1996-03-20); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 3-0 Barreira, ogol Barreira 0-3 Flamengo (1996-03-24); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-2 Vasco, ogol Vasco 2-3 Botafogo (1996-03-24); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-0 Madureira, ogol Madureira 0-0 América-RJ (1996-03-31); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-1 Barreira, ogol Barreira 1-1 Volta Redonda (1996-04-07); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-0 Fluminense, ogol Fluminense 0-3 Bangu (1996-04-07); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 0-3 Flamengo, ogol Flamengo 3-0 Madureira (1996-04-13); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 1-1 América-RJ, ogol América-RJ 1-1 Americano-RJ (1996-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 3-2 Bangu, ogol Bangu 2-3 Vasco (1996-04-21); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 3-3 Olaria, ogol Olaria 3-3 Botafogo (1996-04-21); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 4-1 América-RJ, ogol América-RJ 1-4 Flamengo (1996-04-28); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-0 Americano-RJ, ogol Americano-RJ 0-1 Volta Redonda (1996-04-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-0 Botafogo, ogol Botafogo 0-0 Fluminense (1996-04-28); fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 1-0 Barreira, ogol Barreira 0-1 Vasco (1996-04-28); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-0 Volta Redonda, ogol Volta Redonda 0-1 Fluminense (1996-04-17); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-7 Botafogo, ogol Botafogo 7-0 América-RJ (1996-05-11); fica a RSSSF
- mando invertido no ogol — RSSSF Barreira 1-2 Madureira, ogol Madureira 2-1 Barreira (1996-05-19); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 2-0 América-RJ, ogol América-RJ 0-2 Volta Redonda (1996-05-26); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 0-2 Olaria, ogol Olaria 2-0 América-RJ (1996-06-02); fica a RSSSF
- mando invertido no ogol — RSSSF América-RJ 1-1 Itaperuna, ogol Itaperuna 1-1 América-RJ (1996-06-07); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-2 Vasco, ogol Vasco 2-0 Fluminense (1996-06-09); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-2 Madureira, ogol Madureira 2-1 Volta Redonda (1996-06-16); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 1-3 Botafogo, ogol Botafogo 3-1 Fluminense (1996-06-22); fica a RSSSF
- placar diferente no ogol — Olaria x América-RJ (1996-04-06): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Botafogo x Olaria (1996-06-15): RSSSF 2-0, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Vasco x Olaria (1996-03-10): RSSSF 6-2, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Fluminense x Olaria (1996-03-27): RSSSF 2-0, ogol 6-1; fica o da RSSSF
- placar diferente no ogol — Olaria x Flamengo (1996-03-31): RSSSF 1-1, ogol 2-6; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Olaria x América-RJ, ogol 1996-04-06); fica a do ogol
- mando invertido e placar diferente no ogol — RSSSF Volta Redonda 2-0 Americano-RJ, ogol Americano-RJ 1-2 Volta Redonda (1996-06-23); fica a RSSSF
- só na RSSSF (não achado no ogol): Madureira 2-1 Olaria (1996-01-27)
- só na RSSSF (não achado no ogol): Botafogo 3-1 América-RJ (1996-01-28)
- só na RSSSF (não achado no ogol): Fluminense 4-1 Bangu (1996-01-28)
- só na RSSSF (não achado no ogol): Vasco 0-0 Flamengo (1996-01-28)
- só na RSSSF (não achado no ogol): Madureira 1-1 Flamengo (1996-02-03)
- só na RSSSF (não achado no ogol): Bangu 1-1 Vasco (1996-02-04)
- só na RSSSF (não achado no ogol): Botafogo 2-0 Fluminense (1996-02-04)
- só na RSSSF (não achado no ogol): Bangu 0-2 Flamengo (1996-02-07)
- só na RSSSF (não achado no ogol): Vasco 2-0 América-RJ (1996-02-07)
- só na RSSSF (não achado no ogol): Bangu 2-0 América-RJ (1996-02-11)
- só na RSSSF (não achado no ogol): Flamengo 2-1 Fluminense (1996-02-11)
- só na RSSSF (não achado no ogol): Botafogo 3-0 Madureira (1996-02-29)
- só na RSSSF (não achado no ogol): Flamengo 2-1 América-RJ (1996-02-17)
- só na RSSSF (não achado no ogol): Botafogo 5-3 Vasco (1996-02-17)
- só na RSSSF (não achado no ogol): Fluminense 2-4 Vasco (1996-02-24)
- só na RSSSF (não achado no ogol): Madureira 1-0 América-RJ (1996-02-25)
- só na RSSSF (não achado no ogol): Botafogo 4-0 Bangu (1996-02-25)
- só na RSSSF (não achado no ogol): Bangu 3-2 Olaria (1996-03-02)
- só na RSSSF (não achado no ogol): Fluminense 2-2 América-RJ (1996-03-02)
- só na RSSSF (não achado no ogol): Vasco 0-1 Madureira (1996-03-08)
- só na RSSSF (não achado no ogol): Vasco 4-1 Olaria (1996-03-10)
- só na RSSSF (não achado no ogol): Fluminense 6-1 Olaria (1996-03-27)
- só na RSSSF (não achado no ogol): Olaria 2-6 Flamengo (1996-03-31)
- só na RSSSF (não achado no ogol): Olaria 1-1 América-RJ (1996-04-06)
- só na RSSSF (não achado no ogol): Madureira 1-0 Bangu (1996-04-27)
- só na RSSSF (não achado no ogol): Fluminense 1-1 Madureira (1996-05-26)
- só na RSSSF (não achado no ogol): Botafogo 2-2 Flamengo (1996-06-02)
- só na RSSSF (não achado no ogol): Botafogo 2-2 Olaria (1996-06-15)

### 1997

- tabela publicada x jogos — 1º Turno / -: Botafogo tabela [11, 11, 0, 0, 29, 8] jogos [12, 12, 0, 0, 33, 9] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 1º Turno / -: Fluminense tabela [11, 4, 3, 4, 13, 13] jogos [12, 4, 3, 5, 14, 17] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Terceira fase / -: Vasco tabela [5, 3, 2, 0, 10, 3] jogos [5, 2, 2, 1, 9, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Flamengo tabela [5, 1, 1, 3, 2, 5] jogos [5, 2, 1, 2, 3, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Vasco tabela [5, 3, 2, 0, 10, 3] jogos [5, 2, 2, 1, 9, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Flamengo tabela [5, 1, 1, 3, 2, 5] jogos [5, 2, 1, 2, 3, 4] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF América-RJ 1-1 Olaria, ogol Olaria 1-1 América-RJ (1997-01-11); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-2 Vasco, ogol Vasco 2-1 Madureira (1997-01-15); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 1-0 Fluminense, ogol Fluminense 0-1 Bangu (1997-03-23); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-2 Flamengo, ogol Flamengo 2-2 Botafogo (1997-04-06); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu 3-0 Volta Redonda, ogol Volta Redonda 0-3 Bangu (1997-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 2-3 Fluminense, ogol Fluminense 3-2 Flamengo (1997-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 0-0 Botafogo, ogol Botafogo 0-0 Fluminense (1997-05-04); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo 0-2 Fluminense, ogol Fluminense 2-0 Flamengo (1997-05-17); fica a RSSSF
- mando invertido no ogol — RSSSF Americano-RJ 0-1 Botafogo, ogol Botafogo 1-0 Americano-RJ (1997-05-18); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 2-1 Botafogo, ogol Botafogo 1-2 Fluminense (1997-07-02); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 26 jogos (ex.: Fluminense x Itaperuna, ogol 1997-02-07); fica a do ogol
- jogo só no ogol, incluído em First Stage - First Phase: Botafogo 4-1 Fluminense (1997-02-23)
- só na RSSSF (não achado no ogol): Fluminense 1-4 Botafogo (1997-02-02)
- só na RSSSF (não achado no ogol): Americano-RJ 1-0 Flamengo (1997-05-14)
- só na RSSSF (não achado no ogol): Flamengo 1-0 Vasco (1997-07-02)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Vasco x Flamengo (1997-05-18)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Flamengo x Americano (1997-06-01)

### 1998

- tabela publicada x jogos — Primeira fase / -: América-RJ tabela [10, 2, 3, 5, 8, 14] jogos [10, 3, 2, 5, 8, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Itaperuna tabela [10, 1, 2, 7, 8, 22] jogos [10, 1, 1, 8, 7, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [7, 3, 1, 3, 10, 14] jogos [17, 8, 4, 5, 26, 22] — a tabela conta 7 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Friburguense tabela [7, 1, 2, 4, 6, 12] jogos [17, 7, 5, 5, 24, 21] — a tabela conta 7 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Vasco tabela [7, 6, 0, 1, 11, 3] jogos [6, 5, 0, 1, 9, 3] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / -: Fluminense tabela [7, 3, 2, 2, 10, 6] jogos [7, 4, 2, 1, 12, 4] — placar diverge entre RSSSF e ogol em Flamengo x Fluminense (0-2 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Botafogo tabela [7, 1, 3, 3, 10, 13] jogos [6, 1, 3, 2, 10, 11] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itaperuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olaria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Volta Redonda
- Itaperuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itaperuna)
- Olaria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olaria)
- Volta Redonda — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Volta Redonda)
- placar diferente no ogol — Madureira x Friburguense (1998-04-08): RSSSF 2-1, ogol 1-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 12 jogos (ex.: Friburguense x Vasco, ogol 1998-04-07); fica a do ogol
- só na RSSSF (não achado no ogol): Madureira 0-0 Friburguense (1998-01-25)
- só na RSSSF (não achado no ogol): América-RJ 1-0 Itaperuna (1998-01-25)
- só na RSSSF (não achado no ogol): Olaria 0-0 Volta Redonda (1998-01-25)
- só na RSSSF (não achado no ogol): Volta Redonda 0-1 América-RJ (1998-01-28)
- só na RSSSF (não achado no ogol): Friburguense 0-0 Olaria (1998-01-28)
- só na RSSSF (não achado no ogol): Itaperuna 0-1 Madureira (1998-01-28)
- só na RSSSF (não achado no ogol): Madureira 3-1 América-RJ (1998-02-01)
- só na RSSSF (não achado no ogol): Olaria 3-1 Itaperuna (1998-02-01)
- só na RSSSF (não achado no ogol): Friburguense 2-1 Volta Redonda (1998-02-01)
- só na RSSSF (não achado no ogol): Madureira 0-1 Volta Redonda (1998-02-04)
- só na RSSSF (não achado no ogol): Itaperuna 1-3 Friburguense (1998-02-04)
- só na RSSSF (não achado no ogol): América-RJ 0-2 Olaria (1998-02-04)
- só na RSSSF (não achado no ogol): Olaria 0-0 Madureira (1998-02-08)
- só na RSSSF (não achado no ogol): Volta Redonda 0-1 Itaperuna (1998-02-08)
- só na RSSSF (não achado no ogol): América-RJ 0-1 Friburguense (1998-02-08)
- só na RSSSF (não achado no ogol): Friburguense 4-2 Madureira (1998-02-12)
- só na RSSSF (não achado no ogol): Volta Redonda 2-1 Olaria (1998-02-12)
- só na RSSSF (não achado no ogol): Itaperuna 1-1 América-RJ (1998-02-12)
- só na RSSSF (não achado no ogol): Madureira 4-0 Itaperuna (1998-02-14)
- só na RSSSF (não achado no ogol): América-RJ 2-0 Volta Redonda (1998-02-14)
- só na RSSSF (não achado no ogol): Olaria 3-3 Friburguense (1998-02-14)
- só na RSSSF (não achado no ogol): América-RJ 1-1 Madureira (1998-02-18)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Friburguense (1998-02-18)
- só na RSSSF (não achado no ogol): Itaperuna 0-2 Olaria (1998-02-18)
- só na RSSSF (não achado no ogol): Friburguense 3-0 Itaperuna (1998-02-26)
- só na RSSSF (não achado no ogol): Olaria 3-0 América-RJ (1998-02-26)
- só na RSSSF (não achado no ogol): Volta Redonda 0-2 Madureira (1998-02-26)
- só na RSSSF (não achado no ogol): Madureira 3-1 Olaria (1998-03-01)
- só na RSSSF (não achado no ogol): Itaperuna 3-4 Volta Redonda (1998-03-01)
- só na RSSSF (não achado no ogol): Friburguense 2-1 América-RJ (1998-03-01)
- só na RSSSF (não achado no ogol): Vasco 2-0 Flamengo (1998-05-17)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Vasco x Botafogo (1998-05-10)

### 1999

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabofriense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Volta Redonda
- Cabofriense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabofriense)
- Volta Redonda — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Volta Redonda)
- mando invertido no ogol — RSSSF Flamengo 0-2 Fluminense, ogol Fluminense 2-0 Flamengo (1999-05-23); fica a RSSSF
- jogo só no ogol, incluído em First Stage - First Phase: Bangu 2-2 Americano-RJ (1999-03-31)
- só na RSSSF (não achado no ogol): Olaria 2-3 Itaperuna (1999-01-31)
- só na RSSSF (não achado no ogol): Volta Redonda 2-0 América-RJ (1999-01-31)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Volta Redonda (1999-02-03)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Olaria (1999-02-03)
- só na RSSSF (não achado no ogol): Olaria 1-1 Volta Redonda (1999-02-07)
- só na RSSSF (não achado no ogol): Cabofriense 2-0 América-RJ (1999-02-07)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Cabofriense (1999-02-10)
- só na RSSSF (não achado no ogol): América-RJ 0-2 Itaperuna (1999-02-10)
- só na RSSSF (não achado no ogol): Itaperuna 2-1 Cabofriense (1999-02-13)
- só na RSSSF (não achado no ogol): América-RJ 0-2 Olaria (1999-02-13)
- só na RSSSF (não achado no ogol): Itaperuna 0-0 Olaria (1999-02-18)
- só na RSSSF (não achado no ogol): América-RJ 0-2 Volta Redonda (1999-02-18)
- só na RSSSF (não achado no ogol): Olaria 3-0 Cabofriense (1999-02-21)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Itaperuna (1999-02-21)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Olaria (1999-02-24)
- só na RSSSF (não achado no ogol): Cabofriense 2-0 América-RJ (1999-02-24)
- só na RSSSF (não achado no ogol): Cabofriense 3-2 Volta Redonda (1999-02-28)
- só na RSSSF (não achado no ogol): Itaperuna 2-0 América-RJ (1999-02-28)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Itaperuna (1999-03-03)
- só na RSSSF (não achado no ogol): Olaria 2-0 América-RJ (1999-03-03)

### 2000

- tabela publicada x jogos — 2º Turno / -: Americano-RJ tabela [20, 7, 5, 8, 29, 36] jogos [28, 12, 6, 10, 41, 43] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Olaria tabela [20, 7, 2, 11, 27, 41] jogos [28, 10, 3, 15, 39, 56] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Bangu tabela [20, 5, 6, 9, 24, 35] jogos [28, 6, 9, 13, 33, 47] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: América-RJ tabela [20, 4, 8, 8, 23, 35] jogos [28, 7, 12, 9, 38, 44] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Friburguense tabela [20, 4, 8, 8, 19, 31] jogos [28, 8, 10, 10, 32, 38] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Madureira tabela [20, 4, 6, 10, 19, 34] jogos [28, 9, 8, 11, 35, 44] — a tabela conta 20 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Volta Redonda tabela [11, 1, 3, 7, 9, 19] jogos [19, 4, 4, 11, 16, 28] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Cabofriense tabela [11, 0, 5, 6, 4, 21] jogos [19, 2, 7, 10, 11, 32] — a tabela conta 11 jogos e as fontes trazem 19
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabo Frio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itaperuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Serrano
- Cabo Frio — clube que o ogol não tem; entra só pela RSSSF
- Itaperuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itaperuna)
- Serrano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Serrano)
- mando invertido no ogol — RSSSF Vasco 5-1 Flamengo, ogol Flamengo 1-5 Vasco (2000-04-23); fica a RSSSF
- placar diferente no ogol — Madureira x Olaria (2000-04-16): RSSSF 3-0, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Friburguense x Volta Redonda (2000-03-12): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Volta Redonda x Americano-RJ (2000-03-19): RSSSF 0-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Bangu x América-RJ (2000-03-29): RSSSF 0-2, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Madureira x América-RJ, ogol 2000-04-12); fica a do ogol
- só na RSSSF (não achado no ogol): Olaria 2-2 Itaperuna (2000-01-29)
- só na RSSSF (não achado no ogol): Friburguense 2-0 Cabofriense (2000-01-30)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 Serrano (2000-01-30)
- só na RSSSF (não achado no ogol): Serrano 2-2 Friburguense (2000-02-02)
- só na RSSSF (não achado no ogol): América-RJ 2-2 Bangu (2000-02-02)
- só na RSSSF (não achado no ogol): Cabofriense 1-1 Americano-RJ (2000-02-02)
- só na RSSSF (não achado no ogol): Itaperuna 3-1 Madureira (2000-02-02)
- só na RSSSF (não achado no ogol): Bangu 1-1 Itaperuna (2000-02-05)
- só na RSSSF (não achado no ogol): Americano-RJ 1-0 Serrano (2000-02-05)
- só na RSSSF (não achado no ogol): Serrano 1-0 Cabofriense (2000-02-09)
- só na RSSSF (não achado no ogol): Itaperuna 1-1 América-RJ (2000-02-09)
- só na RSSSF (não achado no ogol): Olaria 1-0 Bangu (2000-02-09)
- só na RSSSF (não achado no ogol): Bangu 1-2 Madureira (2000-02-12)
- só na RSSSF (não achado no ogol): América-RJ 2-0 Olaria (2000-02-12)
- só na RSSSF (não achado no ogol): Cabofriense 0-1 Volta Redonda (2000-02-12)
- só na RSSSF (não achado no ogol): Americano-RJ 1-0 Friburguense (2000-02-13)
- só na RSSSF (não achado no ogol): Serrano 2-2 Volta Redonda (2000-02-16)
- só na RSSSF (não achado no ogol): América-RJ 2-2 Madureira (2000-02-16)
- só na RSSSF (não achado no ogol): Itaperuna 1-4 Olaria (2000-02-16)
- só na RSSSF (não achado no ogol): Cabofriense 2-2 Friburguense (2000-02-16)
- só na RSSSF (não achado no ogol): Madureira 1-0 Itaperuna (2000-02-19)
- só na RSSSF (não achado no ogol): Americano-RJ 3-0 Cabofriense (2000-02-19)
- só na RSSSF (não achado no ogol): Friburguense 3-0 Serrano (2000-02-20)
- só na RSSSF (não achado no ogol): Serrano 3-2 Americano-RJ (2000-02-23)
- só na RSSSF (não achado no ogol): Itaperuna 1-1 Bangu (2000-02-23)
- só na RSSSF (não achado no ogol): Olaria 2-4 Madureira (2000-02-23)
- só na RSSSF (não achado no ogol): Volta Redonda 2-0 Friburguense (2000-02-23)
- só na RSSSF (não achado no ogol): Americano-RJ 3-0 Volta Redonda (2000-02-26)
- só na RSSSF (não achado no ogol): Bangu 3-1 Olaria (2000-02-26)
- só na RSSSF (não achado no ogol): Cabofriense 2-0 Serrano (2000-02-26)
- só na RSSSF (não achado no ogol): América-RJ 5-1 Itaperuna (2000-02-27)
- só na RSSSF (não achado no ogol): Olaria 2-0 América-RJ (2000-03-01)
- só na RSSSF (não achado no ogol): Volta Redonda 1-2 Cabofriense (2000-03-01)
- só na RSSSF (não achado no ogol): Friburguense 3-0 Americano-RJ (2000-03-01)
- só na RSSSF (não achado no ogol): Friburguense 0-0 Volta Redonda (2000-03-12)
- só na RSSSF (não achado no ogol): Volta Redonda 2-2 Americano-RJ (2000-03-19)
- só na RSSSF (não achado no ogol): Bangu 3-0 América-RJ (2000-03-29)
- só na RSSSF (não achado no ogol): Madureira 1-1 América-RJ (2000-04-12)
- só na RSSSF (não achado no ogol): Madureira 4-1 Olaria (2000-04-16)
- só na RSSSF (não achado no ogol): Madureira 2-1 Bangu (2000-04-22)

### 2001

- tabela publicada x jogos — 1º Turno / Grupo B: Cabofriense tabela [5, 1, 0, 4, 6, 14] jogos [15, 7, 3, 5, 21, 20] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: Americano-RJ tabela [11, 7, 2, 2, 17, 9] jogos [12, 8, 2, 2, 18, 9] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Volta Redonda tabela [11, 2, 2, 7, 12, 19] jogos [12, 2, 2, 8, 12, 20] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Vasco tabela [17, 12, 3, 2, 38, 13] jogos [17, 12, 3, 2, 39, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Olaria tabela [16, 7, 2, 7, 25, 24] jogos [16, 7, 2, 7, 26, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Friburguense tabela [16, 4, 4, 8, 26, 28] jogos [16, 4, 4, 8, 28, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Volta Redonda tabela [16, 3, 3, 10, 15, 27] jogos [26, 8, 6, 12, 27, 35] — a tabela conta 16 jogos e as fontes trazem 26
- tabela publicada x jogos — 2º Turno / -: Cabofriense tabela [16, 3, 3, 10, 19, 40] jogos [26, 9, 6, 11, 34, 46] — a tabela conta 16 jogos e as fontes trazem 26
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itaperuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Serrano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- Itaperuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itaperuna)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa-RJ)
- Serrano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Serrano)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão)
- ano errado na data da RSSSF — Flamengo 3-0 Olaria: RSSSF 2002-01-20, ogol 2001-01-20; fica a do ogol
- ano errado na data da RSSSF — Botafogo 0-0 Bangu: RSSSF 2002-01-20, ogol 2001-01-20; fica a do ogol
- ano errado na data da RSSSF — Fluminense 3-1 América-RJ: RSSSF 2002-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 3-2 Friburguense: RSSSF 2002-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-0 Volta Redonda: RSSSF 2002-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-2 Madureira: RSSSF 2002-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-1 Cabofriense: RSSSF 2002-01-26, ogol 2001-01-26; fica a do ogol
- ano errado na data da RSSSF — Friburguense 1-2 Vasco: RSSSF 2002-01-27, ogol 2001-01-27; fica a do ogol
- ano errado na data da RSSSF — Flamengo 4-0 Americano-RJ: RSSSF 2002-01-27, ogol 2001-01-27; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-3 Fluminense: RSSSF 2002-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-1 Olaria: RSSSF 2002-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-0 Volta Redonda: RSSSF 2002-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — América-RJ 0-1 Vasco: RSSSF 2002-02-03, ogol 2001-02-03; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 0-4 Fluminense: RSSSF 2002-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Olaria 3-2 Botafogo: RSSSF 2002-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-3 Flamengo: RSSSF 2002-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-0 Bangu: RSSSF 2002-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Friburguense 0-0 Madureira: RSSSF 2002-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Bangu 2-3 Flamengo: RSSSF 2002-02-10, ogol 2001-02-10; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 2-1 Olaria: RSSSF 2002-02-10, ogol 2001-02-10; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-0 Botafogo: RSSSF 2002-02-11, ogol 2001-02-11; fica a do ogol
- ano errado na data da RSSSF — Friburguense 4-1 América-RJ: RSSSF 2002-02-11, ogol 2001-02-11; fica a do ogol
- ano errado na data da RSSSF — Madureira 3-1 Cabofriense: RSSSF 2002-02-11, ogol 2001-02-11; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-1 Cabofriense: RSSSF 2002-02-17, ogol 2001-02-17; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-1 América-RJ: RSSSF 2002-02-17, ogol 2001-02-17; fica a do ogol
- ano errado na data da RSSSF — Fluminense 6-1 Friburguense: RSSSF 2002-02-17, ogol 2001-02-17; fica a do ogol
- ano errado na data da RSSSF — Olaria 0-0 Americano-RJ: RSSSF 2002-02-17, ogol 2001-02-17; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-1 Botafogo: RSSSF 2002-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-1 Volta Redonda: RSSSF 2002-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-0 Vasco: RSSSF 2002-02-22, ogol 2001-02-22; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-0 Americano-RJ: RSSSF 2002-02-24, ogol 2001-02-24; fica a do ogol
- ano errado na data da RSSSF — Olaria 3-2 Fluminense: RSSSF 2002-03-10, ogol 2001-03-10; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-1 Bangu: RSSSF 2002-03-10, ogol 2001-03-10; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 3-1 Madureira: RSSSF 2002-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-1 Cabofriense: RSSSF 2002-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-2 América-RJ: RSSSF 2002-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 1-1 Friburguense: RSSSF 2002-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-1 América-RJ: RSSSF 2002-03-17, ogol 2001-03-17; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-2 Friburguense: RSSSF 2002-03-17, ogol 2001-03-17; fica a do ogol
- ano errado na data da RSSSF — Olaria 0-1 Vasco: RSSSF 2002-03-17, ogol 2001-03-17; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-0 Volta Redonda: RSSSF 2002-03-18, ogol 2001-03-18; fica a do ogol
- ano errado na data da RSSSF — Fluminense 5-1 Madureira: RSSSF 2002-03-18, ogol 2001-03-18; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-0 Cabofriense: RSSSF 2002-03-18, ogol 2001-03-18; fica a do ogol
- ano errado na data da RSSSF — Fluminense 3-1 América-RJ: RSSSF 2002-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Madureira 3-3 Volta Redonda: RSSSF 2002-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-1 Olaria: RSSSF 2002-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-1 Bangu: RSSSF 2002-03-25, ogol 2001-03-25; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-1 Flamengo: RSSSF 2002-03-25, ogol 2001-03-25; fica a do ogol
- ano errado na data da RSSSF — Friburguense 0-1 Americano-RJ: RSSSF 2002-03-28, ogol 2001-03-28; fica a do ogol
- ano errado na data da RSSSF — Olaria 1-0 Volta Redonda: RSSSF 2002-03-28, ogol 2001-03-28; fica a do ogol
- ano errado na data da RSSSF — Fluminense 5-0 Cabofriense: RSSSF 2002-03-28, ogol 2001-03-28; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-1 Flamengo: RSSSF 2002-03-29, ogol 2001-03-29; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-4 Botafogo: RSSSF 2002-03-29, ogol 2001-03-29; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-1 Madureira: RSSSF 2002-03-30, ogol 2001-03-30; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-0 Americano-RJ: RSSSF 2002-03-31, ogol 2001-03-31; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-1 Flamengo: RSSSF 2002-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-1 Friburguense: RSSSF 2002-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Olaria 0-2 Bangu: RSSSF 2002-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Vasco 2-1 Volta Redonda: RSSSF 2002-04-02, ogol 2001-04-02; fica a do ogol
- ano errado na data da RSSSF — Madureira 4-1 Cabofriense: RSSSF 2002-04-02, ogol 2001-04-02; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-0 Friburguense: RSSSF 2002-04-07, ogol 2001-04-07; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-1 América-RJ: RSSSF 2002-04-07, ogol 2001-04-07; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 3-2 Botafogo: RSSSF 2002-04-07, ogol 2001-04-07; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-2 Olaria: RSSSF 2002-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-1 Fluminense: RSSSF 2002-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-1 Vasco: RSSSF 2002-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-3 Americano-RJ: RSSSF 2002-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Flamengo 4-2 Olaria: RSSSF 2002-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-3 Friburguense: RSSSF 2002-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-1 Volta Redonda: RSSSF 2002-04-15, ogol 2001-04-15; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-3 Botafogo: RSSSF 2002-04-15, ogol 2001-04-15; fica a do ogol
- ano errado na data da RSSSF — Fluminense 3-3 Vasco: RSSSF 2002-04-15, ogol 2001-04-15; fica a do ogol
- ano errado na data da RSSSF — Friburguense 0-2 Vasco: RSSSF 2002-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Olaria 2-1 Friburguense: RSSSF 2002-04-21, ogol 2001-04-21; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-3 Flamengo: RSSSF 2002-04-21, ogol 2001-04-21; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-3 Cabofriense: RSSSF 2002-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-1 Botafogo: RSSSF 2002-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-2 Bangu: RSSSF 2002-04-26, ogol 2001-04-26; fica a do ogol
- ano errado na data da RSSSF — Olaria 5-0 América-RJ: RSSSF 2002-04-28, ogol 2001-04-28; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-3 Flamengo: RSSSF 2002-04-28, ogol 2001-04-28; fica a do ogol
- ano errado na data da RSSSF — Friburguense 6-1 Madureira: RSSSF 2002-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 2-1 Fluminense: RSSSF 2002-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-1 Americano-RJ: RSSSF 2002-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Vasco 7-0 Botafogo: RSSSF 2002-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — América-RJ 0-5 Vasco: RSSSF 2002-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-5 Olaria: RSSSF 2002-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-0 Americano-RJ: RSSSF 2002-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-2 Bangu: RSSSF 2002-05-06, ogol 2001-05-06; fica a do ogol
- ano errado na data da RSSSF — Friburguense 1-1 Cabofriense: RSSSF 2002-05-06, ogol 2001-05-06; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-0 Fluminense: RSSSF 2002-05-06, ogol 2001-05-06; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-2 Botafogo: RSSSF 2002-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Friburguense 5-2 Fluminense: RSSSF 2002-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-0 Olaria: RSSSF 2002-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Bangu 3-1 Madureira: RSSSF 2002-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-2 América-RJ: RSSSF 2002-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-0 Vasco: RSSSF 2002-05-13, ogol 2001-05-13; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-2 Vasco: RSSSF 2002-05-20, ogol 2001-05-20; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-3 Flamengo: RSSSF 2002-05-27, ogol 2001-05-27; fica a do ogol
- jogo só no ogol, incluído em First Stage - First Phase / Group B: Fluminense 0-2 Vasco (2001-02-11)
- jogo só no ogol, incluído em Second Stage - First Phase: Americano-RJ 1-0 Volta Redonda (2001-04-22)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 3-1 São Cristóvão (2001-11-15)
- só na RSSSF (não achado no ogol): Serrano 1-0 Itaperuna (2001-11-15)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 Volta Redonda (2001-11-15)
- só na RSSSF (não achado no ogol): Itaperuna 1-0 Cabofriense (2001-11-18)
- só na RSSSF (não achado no ogol): São Cristóvão 1-0 Volta Redonda (2001-11-18)
- só na RSSSF (não achado no ogol): Serrano 1-0 Portuguesa-RJ (2001-11-19)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 São Cristóvão (2001-11-22)
- só na RSSSF (não achado no ogol): Itaperuna 1-2 Portuguesa-RJ (2001-11-22)
- só na RSSSF (não achado no ogol): Volta Redonda 2-0 Serrano (2001-11-22)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-3 Cabofriense (2001-11-25)
- só na RSSSF (não achado no ogol): Volta Redonda 1-1 Itaperuna (2001-11-25)
- só na RSSSF (não achado no ogol): Serrano 3-1 São Cristóvão (2001-11-26)
- só na RSSSF (não achado no ogol): Cabofriense 4-1 Serrano (2001-11-29)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 2-2 Volta Redonda (2001-11-29)
- só na RSSSF (não achado no ogol): São Cristóvão 1-1 Itaperuna (2001-11-29)
- só na RSSSF (não achado no ogol): São Cristóvão 2-0 Portuguesa-RJ (2001-12-02)
- só na RSSSF (não achado no ogol): Itaperuna 4-2 Serrano (2001-12-02)
- só na RSSSF (não achado no ogol): Volta Redonda 1-1 Cabofriense (2001-12-02)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 0-1 Serrano (2001-12-06)
- só na RSSSF (não achado no ogol): Volta Redonda 1-0 São Cristóvão (2001-12-06)
- só na RSSSF (não achado no ogol): Cabofriense 1-0 Itaperuna (2001-12-06)
- só na RSSSF (não achado no ogol): São Cristóvão 0-0 Cabofriense (2001-12-09)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 3-0 Itaperuna (2001-12-09)
- só na RSSSF (não achado no ogol): Serrano 0-1 Volta Redonda (2001-12-10)
- só na RSSSF (não achado no ogol): Cabofriense 3-3 Portuguesa-RJ (2001-12-13)
- só na RSSSF (não achado no ogol): Itaperuna 1-2 Volta Redonda (2001-12-13)
- só na RSSSF (não achado no ogol): São Cristóvão 0-1 Serrano (2001-12-13)
- só na RSSSF (não achado no ogol): Serrano 0-1 Cabofriense (2001-12-16)
- só na RSSSF (não achado no ogol): Volta Redonda 2-1 Portuguesa-RJ (2001-12-16)
- só na RSSSF (não achado no ogol): Itaperuna 6-2 São Cristóvão (2001-12-16)
- só na RSSSF (não achado no ogol): Vasco 2-0 Fluminense (2002-02-11)
- só na RSSSF (não achado no ogol): Americano-RJ 2-1 Volta Redonda (2002-04-22)

### 2002

- tabela publicada x jogos — Overall Table (both stages) / -: Americano-RJ tabela [22, 17, 3, 2, 44, 16] jogos [22, 17, 3, 2, 45, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall Table (both stages) / -: Madureira tabela [22, 9, 2, 11, 23, 38] jogos [22, 9, 2, 11, 33, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Botafogo 2-2 Fluminense, ogol Fluminense 2-2 Botafogo (2002-02-01); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 4-1 Flamengo, ogol Flamengo 1-4 Fluminense (2002-06-09); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Fluminense x Americano-RJ na Second Stage - Finals sempre na mesma ordem) — ogol Americano-RJ 0-2 Fluminense (2002-06-23)
- placar diferente no ogol — Friburguense x Fluminense (2002-03-18): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Americano-RJ x Friburguense, ogol 2002-05-21); fica a do ogol
- só na RSSSF (não achado no ogol): Fluminense 0-0 Bangu (2002-06-16)
- só na RSSSF (não achado no ogol): Americano-RJ 1-0 Friburguense (2002-06-16)

### 2003

- tabela publicada x jogos — 1º Turno / -: Bangu tabela [11, 4, 3, 4, 10, 12] jogos [10, 3, 3, 4, 10, 13] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 1º Turno / -: Olaria tabela [11, 3, 2, 6, 11, 14] jogos [10, 3, 2, 5, 11, 14] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 1º Turno / -: Bangu tabela [11, 4, 3, 4, 10, 12] jogos [10, 3, 3, 4, 10, 13] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 1º Turno / -: Olaria tabela [11, 3, 2, 6, 11, 14] jogos [10, 3, 2, 5, 11, 14] — a tabela conta 11 jogos e as fontes trazem 10
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Americano-RJ x Friburguense, ogol 2003-03-05); fica a do ogol

### 2004

- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Flamengo tabela [11, 4, 3, 4, 19, 15] jogos [15, 8, 3, 4, 29, 19] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Vasco tabela [11, 8, 2, 1, 24, 8] jogos [16, 9, 3, 4, 29, 17] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Fluminense tabela [11, 7, 2, 2, 23, 13] jogos [15, 9, 2, 4, 31, 20] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Americano-RJ tabela [11, 6, 5, 0, 14, 8] jogos [13, 6, 5, 2, 16, 13] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Friburguense tabela [11, 5, 3, 3, 10, 10] jogos [12, 5, 4, 3, 11, 11] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Vasco da Gama won the 2nd stage / -: Portuguesa-RJ tabela [11, 2, 4, 5, 11, 17] jogos [11, 2, 4, 5, 11, 15] — placar diverge entre RSSSF e ogol em Cabofriense x Portuguesa-RJ (2-2 x 2-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Vasco 0-2 Flamengo, ogol Flamengo 2-0 Vasco (2004-02-14); fica a RSSSF
- placar diferente no ogol — Cabofriense x Portuguesa-RJ (2004-03-14): RSSSF 2-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Olaria x Cabofriense (2004-03-21): RSSSF 0-0, ogol 3-0; fica o da RSSSF

### 2005

- tabela publicada x jogos — 1º Turno / Grupo A: Botafogo tabela [5, 3, 1, 1, 7, 5] jogos [6, 3, 1, 2, 7, 6] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / Grupo A: Friburguense tabela [5, 2, 1, 2, 5, 6] jogos [6, 3, 1, 2, 6, 6] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Fluminense tabela [11, 6, 2, 3, 29, 16] jogos [15, 8, 3, 4, 40, 23] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Volta Redonda tabela [11, 7, 2, 2, 20, 12] jogos [16, 9, 3, 4, 27, 19] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Botafogo tabela [11, 6, 3, 2, 18, 15] jogos [13, 6, 3, 4, 19, 18] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Americano-RJ tabela [11, 6, 1, 4, 14, 11] jogos [13, 7, 2, 4, 16, 12] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Vasco tabela [11, 5, 4, 2, 21, 15] jogos [12, 5, 5, 2, 22, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Cabofriense tabela [11, 5, 1, 5, 22, 25] jogos [12, 5, 1, 6, 22, 27] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Flamengo tabela [11, 3, 4, 4, 15, 16] jogos [13, 4, 4, 5, 17, 20] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Fluminense won the 2nd stage / -: Friburguense tabela [11, 3, 3, 5, 13, 18] jogos [12, 4, 3, 5, 14, 18] — a tabela conta 11 jogos e as fontes trazem 12
- mando invertido no ogol — RSSSF Volta Redonda 0-0 Americano-RJ, ogol Americano-RJ 0-0 Volta Redonda (2005-02-20); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 4-1 Flamengo, ogol Flamengo 1-4 Fluminense (2005-04-03); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 4-3 Fluminense, ogol Fluminense 3-4 Volta Redonda (2005-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF Fluminense 3-1 Volta Redonda, ogol Volta Redonda 1-3 Fluminense (2005-04-17); fica a RSSSF
- placar diferente no ogol — Americano-RJ x Friburguense (2005-03-23): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Friburguense x Botafogo, ogol 2005-02-05); fica a do ogol
- só na RSSSF (não achado no ogol): Friburguense 1-0 Botafogo (2005-02-05)

### 2006

- tabela publicada x jogos — 1º Turno / Grupo A: Cabofriense tabela [5, 3, 0, 2, 7, 7] jogos [5, 3, 0, 2, 8, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Nova Iguaçu tabela [5, 3, 0, 2, 5, 11] jogos [5, 3, 0, 2, 8, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Botafogo tabela [11, 4, 4, 3, 22, 18] jogos [16, 9, 4, 3, 35, 22] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: Madureira tabela [11, 4, 2, 5, 13, 17] jogos [15, 5, 3, 7, 16, 23] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Final / -: América-RJ tabela [11, 6, 2, 3, 20, 12] jogos [15, 6, 3, 6, 24, 22] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Final / -: Cabofriense tabela [11, 5, 3, 3, 17, 14] jogos [13, 5, 5, 3, 20, 16] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Final / -: Americano-RJ tabela [11, 5, 3, 3, 21, 19] jogos [14, 6, 3, 5, 25, 23] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Final / -: Nova Iguaçu tabela [11, 4, 1, 6, 15, 24] jogos [11, 4, 1, 6, 18, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF América-RJ 1-3 Botafogo, ogol Botafogo 3-1 América-RJ (2006-02-12); fica a RSSSF
- mando invertido no ogol — RSSSF Madureira 1-0 Americano-RJ, ogol Americano-RJ 0-1 Madureira (2006-03-30); fica a RSSSF
- só na RSSSF (não achado no ogol): Botafogo 3-1 América-RJ (2006-02-12)

### 2007

- tabela publicada x jogos — 2º Turno / Grupo A: Madureira tabela [6, 4, 0, 2, 11, 7] jogos [7, 4, 0, 3, 12, 11] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo A: Flamengo tabela [6, 3, 0, 3, 10, 10] jogos [7, 4, 0, 3, 14, 11] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase final / -: Flamengo tabela [11, 6, 1, 4, 19, 18] jogos [16, 7, 4, 5, 28, 25] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Botafogo tabela [11, 7, 2, 2, 30, 13] jogos [16, 8, 6, 2, 43, 24] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Vasco tabela [11, 6, 2, 3, 31, 15] jogos [15, 7, 4, 4, 40, 22] — a tabela conta 11 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Volta Redonda tabela [11, 6, 1, 4, 19, 19] jogos [12, 6, 2, 4, 20, 20] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: América-RJ tabela [11, 5, 1, 5, 16, 20] jogos [12, 5, 1, 6, 17, 22] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Cabofriense tabela [11, 4, 1, 6, 17, 17] jogos [14, 4, 3, 7, 21, 23] — a tabela conta 11 jogos e as fontes trazem 14
- mando invertido no ogol — RSSSF Botafogo 4-4 Vasco, ogol Vasco 4-4 Botafogo (2007-04-12); fica a RSSSF
- mando invertido no ogol — RSSSF Volta Redonda 1-1 Cabofriense, ogol Cabofriense 1-1 Volta Redonda (2007-04-13); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 2-2 Cabofriense, ogol Cabofriense 2-2 Botafogo (2007-04-15); fica a RSSSF
- mando invertido no ogol — RSSSF Cabofriense 1-3 Botafogo, ogol Botafogo 3-1 Cabofriense (2007-04-22); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Vasco x Madureira, ogol 2007-03-11); fica a do ogol
- jogo só no ogol, incluído em First Stage - Finals: Flamengo 0-1 Madureira (2007-03-04)
- jogo só no ogol, incluído em Second Stage - First phase: Madureira 1-4 Flamengo (2007-03-08)
- só na RSSSF (não achado no ogol): Madureira 1-0 Vasco (2007-03-04)
- só na RSSSF (não achado no ogol): Vasco 4-1 Madureira (2007-03-11)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

### 2008

- mando invertido no ogol — RSSSF Botafogo 2-0 Fluminense, ogol Fluminense 0-2 Botafogo (2008-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo 1-0 Fluminense, ogol Fluminense 0-1 Botafogo (2008-04-20); fica a RSSSF
- placar diferente no ogol — Resende x Cardoso Moreira (2008-04-05): RSSSF 1-0, ogol 3-0; fica o da RSSSF

### 2009

- tabela publicada x jogos — Fase final / -: Flamengo tabela [17, 10, 6, 1, 35, 19] jogos [20, 12, 6, 2, 38, 22] — a tabela conta 17 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Botafogo tabela [17, 10, 4, 3, 42, 22] jogos [21, 13, 4, 4, 50, 23] — a tabela conta 17 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Vasco tabela [15, 12, 2, 1, 35, 9] jogos [16, 12, 2, 2, 35, 13] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Fluminense tabela [15, 9, 4, 2, 29, 15] jogos [17, 9, 4, 4, 29, 17] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Resende tabela [15, 5, 2, 8, 17, 27] jogos [17, 6, 2, 9, 20, 31] — a tabela conta 15 jogos e as fontes trazem 17
- placar diferente no ogol — Resende x Boavista-RJ (2009-03-25): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é Botafogo (desempate, jogo extra ou pontos tirados fora de campo)

### 2010

- tabela publicada x jogos — 1º Turno / Grupo A: Olaria tabela [7, 3, 3, 1, 12, 8] jogos [7, 3, 3, 1, 14, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Olaria tabela [7, 3, 3, 1, 12, 8] jogos [7, 3, 3, 1, 14, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: América-RJ tabela [7, 3, 1, 3, 13, 12] jogos [7, 3, 1, 3, 13, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: América-RJ tabela [7, 3, 1, 3, 13, 12] jogos [7, 3, 1, 3, 13, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: Fluminense tabela [8, 6, 1, 1, 19, 8] jogos [8, 6, 1, 1, 19, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: Fluminense tabela [8, 6, 1, 1, 19, 8] jogos [8, 6, 1, 1, 19, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Torneio de rebaixamento / -: Resende tabela [4, 0, 3, 1, 4, 5] jogos [4, 0, 3, 1, 3, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Botafogo tabela [15, 11, 2, 2, 35, 22] jogos [19, 15, 2, 2, 44, 26] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Flamengo tabela [15, 13, 2, 0, 42, 18] jogos [18, 14, 2, 2, 46, 23] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Fluminense tabela [15, 11, 2, 2, 36, 13] jogos [17, 11, 3, 3, 38, 17] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Vasco tabela [15, 11, 1, 3, 33, 12] jogos [18, 11, 2, 5, 34, 16] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Duque de Caxias tabela [15, 3, 3, 9, 16, 27] jogos [19, 5, 5, 9, 23, 31] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Friburguense tabela [15, 3, 3, 9, 13, 26] jogos [19, 3, 6, 10, 14, 29] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Resende tabela [15, 3, 3, 9, 17, 34] jogos [19, 3, 6, 10, 20, 38] — a tabela conta 15 jogos e as fontes trazem 19
- campeão pela lista oficial, Botafogo; o 1º pela soma dos jogos da última fase é Duque de Caxias (desempate, jogo extra ou pontos tirados fora de campo)

### 2011

- tabela publicada x jogos — 2º Turno / Grupo A: Resende tabela [8, 2, 2, 4, 12, 12] jogos [8, 2, 2, 4, 11, 12] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo A: América-RJ tabela [8, 1, 1, 6, 7, 15] jogos [8, 1, 1, 6, 6, 14] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo B: Madureira tabela [8, 4, 1, 3, 16, 15] jogos [8, 3, 2, 3, 16, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Duque de Caxias tabela [8, 3, 2, 3, 10, 14] jogos [8, 3, 2, 3, 9, 13] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo B: Macaé tabela [8, 2, 2, 4, 11, 14] jogos [8, 2, 2, 4, 11, 13] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo A: Resende tabela [8, 2, 2, 4, 12, 12] jogos [8, 2, 2, 4, 11, 12] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo A: América-RJ tabela [8, 1, 1, 6, 7, 15] jogos [8, 1, 1, 6, 6, 14] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo B: Madureira tabela [8, 4, 1, 3, 16, 15] jogos [8, 3, 2, 3, 16, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Duque de Caxias tabela [8, 3, 2, 3, 10, 14] jogos [8, 3, 2, 3, 9, 13] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo B: Macaé tabela [8, 2, 2, 4, 11, 14] jogos [8, 2, 2, 4, 11, 13] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Flamengo tabela [15, 11, 4, 0, 27, 11] jogos [19, 12, 7, 0, 30, 13] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Fluminense tabela [15, 11, 2, 2, 33, 15] jogos [17, 11, 4, 2, 36, 18] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Botafogo tabela [15, 9, 4, 2, 32, 15] jogos [16, 9, 5, 2, 33, 16] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Boavista-RJ tabela [15, 8, 2, 5, 28, 19] jogos [17, 8, 3, 6, 30, 22] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Olaria tabela [15, 7, 4, 4, 21, 20] jogos [16, 7, 4, 5, 21, 21] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Vasco tabela [15, 7, 3, 5, 35, 19] jogos [17, 8, 4, 5, 36, 19] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Resende tabela [15, 6, 3, 6, 21, 17] jogos [15, 6, 3, 6, 20, 17] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Duque de Caxias tabela [15, 5, 3, 7, 23, 28] jogos [15, 5, 3, 7, 22, 27] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Nova Iguaçu tabela [15, 5, 3, 7, 23, 28] jogos [15, 5, 3, 7, 19, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Macaé tabela [15, 3, 6, 6, 22, 27] jogos [15, 3, 6, 6, 22, 26] — placar diverge entre RSSSF e ogol em Resende x Macaé (4-2 x 5-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: América-RJ tabela [15, 2, 2, 11, 13, 37] jogos [15, 2, 2, 11, 12, 36] — placar diverge entre RSSSF e ogol em América-RJ x Duque de Caxias (0-1 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Boavista-RJ 0-1 Flamengo, ogol Flamengo 1-0 Boavista-RJ (2011-02-27); fica a RSSSF
- placar diferente no ogol — América-RJ x Duque de Caxias (2011-03-27): RSSSF 0-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Resende x Macaé (2011-03-27): RSSSF 4-2, ogol 5-2; fica o da RSSSF
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Resende 1-1 Bangu (2011-02-19)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Nova Iguaçu 1-3 Olaria (2011-02-20)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Resende 1-1 Olaria (2011-02-27)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Americano-RJ 1-2 Madureira (2011-04-23)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo 2-5 Boavista-RJ (2011-04-23)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Boavista-RJ 1-3 Madureira (2011-05-01)
- campeão pela lista oficial, Flamengo; o 1º pela soma dos jogos da última fase é Vasco (desempate, jogo extra ou pontos tirados fora de campo)

### 2012

- tabela publicada x jogos — 2º Turno / Grupo A: Madureira tabela [8, 3, 1, 4, 11, 12] jogos [8, 3, 1, 4, 11, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Vasco tabela [8, 4, 2, 2, 16, 10] jogos [8, 4, 2, 2, 17, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: Madureira tabela [8, 3, 1, 4, 11, 12] jogos [8, 3, 1, 4, 11, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Vasco tabela [8, 4, 2, 2, 16, 10] jogos [8, 4, 2, 2, 17, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Fluminense tabela [15, 8, 2, 5, 30, 17] jogos [19, 11, 3, 5, 39, 20] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Final / -: Botafogo tabela [15, 9, 6, 0, 35, 12] jogos [20, 11, 7, 2, 44, 21] — a tabela conta 15 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Flamengo tabela [15, 11, 3, 1, 27, 9] jogos [17, 11, 3, 3, 30, 14] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Vasco tabela [15, 11, 2, 2, 32, 13] jogos [19, 13, 2, 4, 40, 22] — a tabela conta 15 jogos e as fontes trazem 19
- tabela publicada x jogos — Final / -: Resende tabela [15, 7, 4, 4, 20, 20] jogos [15, 7, 4, 4, 20, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Macaé tabela [15, 6, 2, 7, 20, 23] jogos [15, 6, 2, 7, 19, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Bangu tabela [15, 4, 3, 8, 17, 23] jogos [16, 4, 3, 9, 19, 27] — a tabela conta 15 jogos e as fontes trazem 16
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Resende 0-1 Friburguense (2012-02-23)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Boavista-RJ 1-3 Nova Iguaçu (2012-02-23)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Friburguense 2-2 Nova Iguaçu (2012-02-26)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Resende 0-2 Volta Redonda (2012-04-20)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Fluminense 2-1 Macaé (2012-04-21)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Fluminense 2-0 Volta Redonda (2012-04-28)

### 2013

- tabela publicada x jogos — Fase final / -: Flamengo tabela [15, 10, 3, 2, 28, 12] jogos [16, 10, 3, 3, 28, 14] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Fluminense tabela [15, 9, 5, 1, 28, 12] jogos [18, 10, 5, 3, 34, 17] — a tabela conta 15 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Vasco tabela [15, 7, 2, 6, 23, 20] jogos [17, 8, 2, 7, 26, 23] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Resende tabela [15, 6, 5, 4, 26, 25] jogos [16, 6, 5, 5, 26, 30] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Volta Redonda tabela [15, 5, 4, 6, 12, 15] jogos [16, 5, 4, 7, 13, 19] — a tabela conta 15 jogos e as fontes trazem 16

### 2014

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

### 2015

- sem ocorrências

### 2016

- mando invertido no ogol — RSSSF Boavista-RJ 1-4 Resende, ogol Resende 4-1 Boavista-RJ (2016-04-23); fica a RSSSF

### 2017

- tabela publicada x jogos — Segunda fase / Grupo B: Nova Iguaçu tabela [5, 1, 3, 1, 5, 7] jogos [10, 3, 5, 2, 16, 14] — a tabela conta 5 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Portuguesa-RJ tabela [5, 0, 2, 3, 5, 11] jogos [10, 3, 3, 4, 10, 16] — a tabela conta 5 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Botafogo tabela [6, 4, 1, 1, 12, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Flamengo tabela [6, 3, 3, 0, 13, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Nova Iguaçu tabela [6, 3, 1, 2, 7, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Boavista-RJ tabela [6, 2, 2, 2, 3, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Madureira tabela [6, 1, 2, 3, 8, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Macaé tabela [6, 0, 2, 4, 6, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Vasco tabela [6, 3, 3, 0, 8, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Fluminense tabela [6, 3, 2, 1, 12, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Volta Redonda tabela [6, 2, 2, 2, 8, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Portuguesa-RJ tabela [6, 2, 2, 2, 7, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Resende tabela [6, 1, 1, 4, 5, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo C: Bangu tabela [6, 1, 1, 4, 4, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Final / -: Flamengo tabela [2, 2, 0, 0, 3, 1] jogos [17, 12, 5, 0, 39, 12] — a tabela conta 2 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Fluminense tabela [2, 0, 0, 2, 1, 3] jogos [17, 9, 4, 4, 34, 17] — a tabela conta 2 jogos e as fontes trazem 17
- 14 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- mando invertido no ogol — RSSSF Fluminense 3-3 Flamengo, ogol Flamengo 3-3 Fluminense (2017-03-05); fica a RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

### 2018

- a página da RSSSF parou em fevereiro de 2018 (44 jogos sem placar, na Taça Rio): as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Bonsucesso x Cabofriense, ogol 2018-01-10); fica a do ogol
- ano errado na data da RSSSF — América-RJ 1-2 Goytacaz: RSSSF 2017-01-06, ogol 2018-01-06; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-0 Macaé: RSSSF 2017-01-06, ogol 2018-01-06; fica a do ogol
- ano errado na data da RSSSF — Resende 2-4 Bonsucesso: RSSSF 2017-01-06, ogol 2018-01-06; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-1 Cabofriense: RSSSF 2017-01-13, ogol 2018-01-13; fica a do ogol
- ano errado na data da RSSSF — Resende 0-1 Macaé: RSSSF 2017-01-13, ogol 2018-01-13; fica a do ogol
- ano errado na data da RSSSF — Bonsucesso 1-3 Goytacaz: RSSSF 2017-01-13, ogol 2018-01-13; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-2 Portuguesa-RJ: RSSSF 2017-01-16, ogol 2018-01-16; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-1 Cabofriense: RSSSF 2017-01-17, ogol 2018-01-17; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 3-1 Fluminense: RSSSF 2017-01-17, ogol 2018-01-17; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-2 Macaé: RSSSF 2017-01-17, ogol 2018-01-17; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-2 Flamengo: RSSSF 2017-01-17, ogol 2018-01-17; fica a do ogol
- ano errado na data da RSSSF — Vasco 0-2 Bangu: RSSSF 2017-01-18, ogol 2018-01-18; fica a do ogol
- ano errado na data da RSSSF — Resende 2-1 América-RJ: RSSSF 2017-01-20, ogol 2018-01-20; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 0-0 Madureira: RSSSF 2017-01-20, ogol 2018-01-20; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 0-1 Macaé: RSSSF 2017-01-20, ogol 2018-01-20; fica a do ogol
- ano errado na data da RSSSF — Fluminense 0-0 Botafogo: RSSSF 2017-01-20, ogol 2018-01-20; fica a do ogol
- ano errado na data da RSSSF — Bangu 2-2 Volta Redonda: RSSSF 2017-01-21, ogol 2018-01-21; fica a do ogol
- ano errado na data da RSSSF — Vasco 4-2 Nova Iguaçu: RSSSF 2017-01-21, ogol 2018-01-21; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-0 Cabofriense: RSSSF 2017-01-21, ogol 2018-01-21; fica a do ogol
- ano errado na data da RSSSF — Goytacaz 2-2 Bonsucesso: RSSSF 2017-01-22, ogol 2018-01-22; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-1 Boavista-RJ: RSSSF 2017-01-23, ogol 2018-01-23; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-1 Vasco: RSSSF 2017-01-24, ogol 2018-01-24; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-0 Bangu: RSSSF 2017-01-24, ogol 2018-01-24; fica a do ogol
- ano errado na data da RSSSF — Fluminense 0-0 Portuguesa-RJ: RSSSF 2017-01-24, ogol 2018-01-24; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 2-0 Volta Redonda: RSSSF 2017-01-25, ogol 2018-01-25; fica a do ogol
- ano errado na data da RSSSF — Macaé 1-2 Botafogo: RSSSF 2017-01-25, ogol 2018-01-25; fica a do ogol
- ano errado na data da RSSSF — Bonsucesso 1-1 Resende: RSSSF 2017-01-27, ogol 2018-01-27; fica a do ogol
- ano errado na data da RSSSF — América-RJ 4-1 Goytacaz: RSSSF 2017-01-27, ogol 2018-01-27; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-0 Vasco: RSSSF 2017-01-27, ogol 2018-01-27; fica a do ogol
- ano errado na data da RSSSF — Bangu 0-0 Nova Iguaçu: RSSSF 2017-01-28, ogol 2018-01-28; fica a do ogol
- ano errado na data da RSSSF — Macaé 1-2 Portuguesa-RJ: RSSSF 2017-01-28, ogol 2018-01-28; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-0 Boavista-RJ: RSSSF 2017-01-28, ogol 2018-01-28; fica a do ogol
- ano errado na data da RSSSF — Madureira 1-2 Fluminense: RSSSF 2017-01-28, ogol 2018-01-28; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 3-2 Cabofriense: RSSSF 2017-01-29, ogol 2018-01-29; fica a do ogol
- ano errado na data da RSSSF — Resende 1-1 Goytacaz: RSSSF 2017-02-03, ogol 2018-02-03; fica a do ogol
- ano errado na data da RSSSF — América-RJ 3-1 Bonsucesso: RSSSF 2017-02-03, ogol 2018-02-03; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-0 Macaé: RSSSF 2017-02-03, ogol 2018-02-03; fica a do ogol
- ano errado na data da RSSSF — Botafogo 0-0 Madureira: RSSSF 2017-02-03, ogol 2018-02-03; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 0-1 Boavista-RJ: RSSSF 2017-02-03, ogol 2018-02-03; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-1 Volta Redonda: RSSSF 2017-02-04, ogol 2018-02-04; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 0-1 Flamengo: RSSSF 2017-02-04, ogol 2018-02-04; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 0-2 Bangu: RSSSF 2017-02-04, ogol 2018-02-04; fica a do ogol
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: Bonsucesso 1-1 Goytacaz (2018-02-07)
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: América-RJ 1-2 Resende (2018-02-07)
- jogo só no ogol, incluído em Semifinal: Boavista-RJ 2-2 Bangu (2018-02-08)
- jogo só no ogol, incluído em Semifinal: Flamengo 3-1 Botafogo (2018-02-10)
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: Resende 1-2 Bonsucesso (2018-02-17)
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: Goytacaz 3-1 América-RJ (2018-02-17)
- jogo só no ogol, incluído em Final: Boavista-RJ 0-2 Flamengo (2018-02-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Volta Redonda 0-2 Portuguesa-RJ (2018-02-19)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 0-4 Fluminense (2018-02-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 4-0 Madureira (2018-02-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Cabofriense 2-3 Boavista-RJ (2018-02-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Nova Iguaçu 1-2 Botafogo (2018-02-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Macaé 2-2 Bangu (2018-02-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 4-0 Flamengo (2018-02-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Boavista-RJ 2-1 Nova Iguaçu (2018-02-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Portuguesa-RJ 1-0 Vasco (2018-02-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-0 Cabofriense (2018-02-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 0-0 Volta Redonda (2018-02-26)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 2-1 Macaé (2018-03-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 1-1 Portuguesa-RJ (2018-03-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 1-0 Botafogo (2018-03-03)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Nova Iguaçu 1-1 Madureira (2018-03-04)
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: Goytacaz 1-0 Resende (2018-03-04)
- jogo só no ogol, incluído em PRELIMINARY STAGE: / RELEGATION GROUP - Grupo X: Bonsucesso 1-1 América-RJ (2018-03-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-1 Volta Redonda (2018-03-04)
- jogo só no ogol, incluído em PRELIMINARY STAGE:: Cabofriense 1-0 Macaé (2018-03-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 4-3 Boavista-RJ (2018-03-04)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 1-0 Bangu (2018-03-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 0-2 Cabofriense (2018-03-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Portuguesa-RJ 2-1 Nova Iguaçu (2018-03-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Macaé 1-1 Volta Redonda (2018-03-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vasco 0-0 Fluminense (2018-03-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Boavista-RJ 0-3 Flamengo (2018-03-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Madureira 1-3 Vasco (2018-03-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Boavista-RJ 0-2 Bangu (2018-03-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Macaé 1-0 Flamengo (2018-03-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Portuguesa-RJ 1-2 Cabofriense (2018-03-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Volta Redonda 1-1 Botafogo (2018-03-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Fluminense 2-1 Nova Iguaçu (2018-03-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Cabofriense 1-1 Fluminense (2018-03-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Botafogo 2-3 Vasco (2018-03-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Flamengo 4-0 Portuguesa-RJ (2018-03-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Nova Iguaçu 0-2 Macaé (2018-03-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Volta Redonda 2-3 Boavista-RJ (2018-03-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Bangu 0-3 Madureira (2018-03-18)
- jogo só no ogol, incluído em Semifinal: Vasco 2-3 Botafogo (2018-03-22)
- jogo só no ogol, incluído em Semifinal: Fluminense 1-1 Flamengo (2018-03-22)
- jogo só no ogol, incluído em First Stage - First phase / Group C: Fluminense 3-0 Botafogo (2018-03-25)
- jogo só no ogol, incluído em Semifinal: Flamengo 0-1 Botafogo (2018-03-29)
- jogo só no ogol, incluído em Semifinal: Fluminense 2-3 Vasco (2018-03-30)
- jogo só no ogol, incluído em Final: Botafogo 2-3 Vasco (2018-04-01)
- jogo só no ogol, incluído em Final: Vasco 0-1 Botafogo (2018-04-08)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Botafogo

### 2019

- tabela publicada x jogos — 2º Turno / Grupo B: Fluminense tabela [6, 3, 2, 1, 11, 6] jogos [8, 4, 2, 2, 14, 8] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo B: Vasco tabela [6, 2, 2, 2, 7, 6] jogos [8, 4, 2, 2, 10, 6] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo B: Portuguesa-RJ tabela [6, 1, 1, 4, 5, 14] jogos [8, 1, 1, 6, 7, 21] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo C: Bangu tabela [6, 5, 0, 1, 9, 3] jogos [8, 5, 0, 3, 9, 6] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo C: Flamengo tabela [6, 4, 2, 0, 13, 5] jogos [8, 6, 2, 0, 18, 7] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo C: Botafogo tabela [6, 2, 3, 1, 10, 7] jogos [7, 3, 3, 1, 14, 8] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo C: Resende tabela [6, 0, 2, 4, 3, 9] jogos [7, 0, 2, 5, 3, 11] — a tabela conta 6 jogos e as fontes trazem 7
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Goytacaz x América-RJ, ogol 2019-01-10); fica a do ogol
- ano errado na data da RSSSF — Resende 1-0 Goytacaz: RSSSF 2018-01-06, ogol 2019-01-06; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-1 Nova Iguaçu: RSSSF 2018-01-06, ogol 2019-01-06; fica a do ogol
- ano errado na data da RSSSF — América-RJ 1-0 Macaé: RSSSF 2018-01-06, ogol 2019-01-06; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-2 Resende: RSSSF 2018-01-09, ogol 2019-01-09; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-2 Americano-RJ: RSSSF 2018-01-09, ogol 2019-01-09; fica a do ogol
- ano errado na data da RSSSF — Resende 1-0 Americano-RJ: RSSSF 2018-01-13, ogol 2019-01-13; fica a do ogol
- ano errado na data da RSSSF — América-RJ 1-1 Nova Iguaçu: RSSSF 2018-01-13, ogol 2019-01-13; fica a do ogol
- ano errado na data da RSSSF — Macaé 2-1 Goytacaz: RSSSF 2018-01-13, ogol 2019-01-13; fica a do ogol
- ano errado na data da RSSSF — América-RJ 0-0 Macaé: RSSSF 2018-01-19, ogol 2019-01-19; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-1 Vasco: RSSSF 2018-01-19, ogol 2019-01-19; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-1 Volta Redonda: RSSSF 2018-01-19, ogol 2019-01-19; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 0-1 Americano-RJ: RSSSF 2018-01-20, ogol 2019-01-20; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-1 Bangu: RSSSF 2018-01-20, ogol 2019-01-20; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 3-1 Botafogo: RSSSF 2018-01-20, ogol 2019-01-20; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 2-1 Resende: RSSSF 2018-01-20, ogol 2019-01-20; fica a do ogol
- ano errado na data da RSSSF — Goytacaz 1-0 Nova Iguaçu: RSSSF 2018-01-21, ogol 2019-01-21; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 0-0 Madureira: RSSSF 2018-01-23, ogol 2019-01-23; fica a do ogol
- ano errado na data da RSSSF — Botafogo 0-0 Bangu: RSSSF 2018-01-23, ogol 2019-01-23; fica a do ogol
- ano errado na data da RSSSF — Resende 1-1 Flamengo: RSSSF 2018-01-23, ogol 2019-01-23; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 1-0 Cabofriense: RSSSF 2018-01-23, ogol 2019-01-23; fica a do ogol
- ano errado na data da RSSSF — Vasco 5-2 Volta Redonda: RSSSF 2018-01-23, ogol 2019-01-23; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 0-4 Fluminense: RSSSF 2018-01-24, ogol 2019-01-24; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 2-1 Madureira: RSSSF 2018-01-26, ogol 2019-01-26; fica a do ogol
- ano errado na data da RSSSF — Bangu 2-0 Boavista-RJ: RSSSF 2018-01-26, ogol 2019-01-26; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-0 Goytacaz: RSSSF 2018-01-26, ogol 2019-01-26; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-2 Flamengo: RSSSF 2018-01-26, ogol 2019-01-26; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-0 América-RJ: RSSSF 2018-01-27, ogol 2019-01-27; fica a do ogol
- ano errado na data da RSSSF — Fluminense 3-1 Portuguesa-RJ: RSSSF 2018-01-27, ogol 2019-01-27; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-0 Americano-RJ: RSSSF 2018-01-27, ogol 2019-01-27; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-1 Resende: RSSSF 2018-01-27, ogol 2019-01-27; fica a do ogol
- ano errado na data da RSSSF — Flamengo 3-1 Boavista-RJ: RSSSF 2018-01-29, ogol 2019-01-29; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 0-1 Vasco: RSSSF 2018-01-30, ogol 2019-01-30; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-2 Volta Redonda: RSSSF 2018-01-30, ogol 2019-01-30; fica a do ogol
- ano errado na data da RSSSF — Fluminense 4-0 Madureira: RSSSF 2018-01-30, ogol 2019-01-30; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-0 Cabofriense: RSSSF 2018-01-31, ogol 2019-01-31; fica a do ogol
- ano errado na data da RSSSF — Botafogo 0-1 Resende: RSSSF 2018-01-31, ogol 2019-01-31; fica a do ogol
- ano errado na data da RSSSF — Madureira 1-1 Americano-RJ: RSSSF 2018-02-02, ogol 2019-02-02; fica a do ogol
- ano errado na data da RSSSF — Goytacaz 1-2 América-RJ: RSSSF 2018-02-02, ogol 2019-02-02; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 0-2 Macaé: RSSSF 2018-02-02, ogol 2019-02-02; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-0 Fluminense: RSSSF 2018-02-02, ogol 2019-02-02; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 1-0 Portuguesa-RJ: RSSSF 2018-02-02, ogol 2019-02-02; fica a do ogol
- ano errado na data da RSSSF — Flamengo 4-0 Cabofriense: RSSSF 2018-02-03, ogol 2019-02-03; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 0-3 Botafogo: RSSSF 2018-02-03, ogol 2019-02-03; fica a do ogol
- ano errado na data da RSSSF — Resende 3-0 Bangu: RSSSF 2018-02-03, ogol 2019-02-03; fica a do ogol
- ano errado na data da RSSSF — Macaé 1-1 América-RJ: RSSSF 2018-02-13, ogol 2019-02-13; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-0 Goytacaz: RSSSF 2018-02-13, ogol 2019-02-13; fica a do ogol
- ano errado na data da RSSSF — Vasco 3-0 Resende: RSSSF 2018-02-13, ogol 2019-02-13; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-1 Fluminense: RSSSF 2018-02-14, ogol 2019-02-14; fica a do ogol
- ano errado na data da RSSSF — América-RJ 0-1 Nova Iguaçu: RSSSF 2018-02-17, ogol 2019-02-17; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-0 Fluminense: RSSSF 2018-02-17, ogol 2019-02-17; fica a do ogol
- ano errado na data da RSSSF — Goytacaz 1-2 Macaé: RSSSF 2018-02-18, ogol 2019-02-18; fica a do ogol
- ano errado na data da RSSSF — Resende 0-1 Volta Redonda: RSSSF 2018-02-22, ogol 2019-02-22; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-4 Nova Iguaçu: RSSSF 2018-02-22, ogol 2019-02-22; fica a do ogol
- ano errado na data da RSSSF — América-RJ 3-2 Goytacaz: RSSSF 2018-02-23, ogol 2019-02-23; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 1-1 Madureira: RSSSF 2018-02-23, ogol 2019-02-23; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-1 Vasco: RSSSF 2018-02-23, ogol 2019-02-23; fica a do ogol
- ano errado na data da RSSSF — Flamengo 4-1 Americano-RJ: RSSSF 2018-02-24, ogol 2019-02-24; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-0 Portuguesa-RJ: RSSSF 2018-02-24, ogol 2019-02-24; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-1 Resende: RSSSF 2018-03-01, ogol 2019-03-01; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-1 Bangu: RSSSF 2018-03-01, ogol 2019-03-01; fica a do ogol
- ano errado na data da RSSSF — Vasco 2-0 Boavista-RJ: RSSSF 2018-03-02, ogol 2019-03-02; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-4 Cabofriense: RSSSF 2018-03-02, ogol 2019-03-02; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 1-0 Botafogo: RSSSF 2018-03-02, ogol 2019-03-02; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-1 Bangu: RSSSF 2018-03-08, ogol 2019-03-08; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 1-1 Boavista-RJ: RSSSF 2018-03-09, ogol 2019-03-09; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-1 Flamengo: RSSSF 2018-03-09, ogol 2019-03-09; fica a do ogol
- ano errado na data da RSSSF — Fluminense 2-1 Cabofriense: RSSSF 2018-03-10, ogol 2019-03-10; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-1 Resende: RSSSF 2018-03-10, ogol 2019-03-10; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-1 Madureira: RSSSF 2018-03-11, ogol 2019-03-11; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 0-3 Fluminense: RSSSF 2018-03-14, ogol 2019-03-14; fica a do ogol
- ano errado na data da RSSSF — Bangu 3-0 Portuguesa-RJ: RSSSF 2018-03-15, ogol 2019-03-15; fica a do ogol
- ano errado na data da RSSSF — Resende 0-2 Madureira: RSSSF 2018-03-16, ogol 2019-03-16; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-0 Volta Redonda: RSSSF 2018-03-16, ogol 2019-03-16; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-0 Vasco: RSSSF 2018-03-17, ogol 2019-03-17; fica a do ogol
- ano errado na data da RSSSF — Fluminense 1-1 Botafogo: RSSSF 2018-03-17, ogol 2019-03-17; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 1-0 Americano-RJ: RSSSF 2018-03-17, ogol 2019-03-17; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-2 Flamengo: RSSSF 2018-03-19, ogol 2019-03-19; fica a do ogol
- ano errado na data da RSSSF — Bangu 2-0 Americano-RJ: RSSSF 2018-03-20, ogol 2019-03-20; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-1 Volta Redonda: RSSSF 2018-03-21, ogol 2019-03-21; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-2 Bangu: RSSSF 2018-03-23, ogol 2019-03-23; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-2 Botafogo: RSSSF 2018-03-24, ogol 2019-03-24; fica a do ogol
- ano errado na data da RSSSF — Flamengo 3-2 Fluminense: RSSSF 2018-03-24, ogol 2019-03-24; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 2-1 Resende: RSSSF 2018-03-24, ogol 2019-03-24; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-0 Cabofriense: RSSSF 2018-03-24, ogol 2019-03-24; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 2-4 Boavista-RJ: RSSSF 2018-03-24, ogol 2019-03-24; fica a do ogol
- ano errado na data da RSSSF — Vasco 1-1 Flamengo: RSSSF 2018-03-31, ogol 2019-03-31; fica a do ogol
- ano errado na data da RSSSF — Flamengo 1-1 Fluminense: RSSSF 2018-04-06, ogol 2019-04-06; fica a do ogol
- ano errado na data da RSSSF — Vasco 2-1 Bangu: RSSSF 2018-04-07, ogol 2019-04-07; fica a do ogol
- ano errado na data da RSSSF — Vasco 0-2 Flamengo: RSSSF 2018-04-14, ogol 2019-04-14; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-0 Vasco: RSSSF 2018-04-21, ogol 2019-04-21; fica a do ogol
- jogo só no ogol, incluído em Second Stage - First phase: Bangu 0-2 Fluminense (2019-02-23)
- jogo só no ogol, incluído em Second Stage - First phase: Portuguesa-RJ 1-3 Flamengo (2019-03-01)
- jogo só no ogol, incluído em Second Stage - First phase: Resende 0-2 Vasco (2019-03-21)
- jogo só no ogol, incluído em Second Stage - First phase: Botafogo 4-1 Portuguesa-RJ (2019-03-22)
- jogo só no ogol, incluído em Second Stage - First phase: Fluminense 1-2 Flamengo (2019-03-28)
- jogo só no ogol, incluído em Second Stage - First phase: Bangu 0-1 Vasco (2019-03-29)
- só na RSSSF (não achado no ogol): Bangu 0-2 Fluminense (2018-02-22)
- só na RSSSF (não achado no ogol): Portuguesa-RJ 1-3 Flamengo (2018-02-28)
- só na RSSSF (não achado no ogol): Resende 0-2 Vasco (2018-03-20)
- só na RSSSF (não achado no ogol): Botafogo 4-1 Portuguesa-RJ (2018-03-21)
- só na RSSSF (não achado no ogol): Fluminense 1-2 Flamengo (2018-03-27)
- só na RSSSF (não achado no ogol): Bangu 0-1 Vasco (2018-03-28)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

### 2020

- a página da RSSSF parou em março de 2020 (21 jogos sem placar): as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Friburguense x Americano-RJ, ogol 2020-01-11); fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-2 Americano-RJ: RSSSF 2019-01-04, ogol 2020-01-04; fica a do ogol
- ano errado na data da RSSSF — América-RJ 1-1 Portuguesa-RJ: RSSSF 2019-01-04, ogol 2020-01-04; fica a do ogol
- ano errado na data da RSSSF — Macaé 1-0 Friburguense: RSSSF 2019-01-04, ogol 2020-01-04; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 3-2 Nova Iguaçu: RSSSF 2019-01-08, ogol 2020-01-08; fica a do ogol
- ano errado na data da RSSSF — Friburguense 0-0 América-RJ: RSSSF 2019-01-08, ogol 2020-01-08; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-0 Macaé: RSSSF 2019-01-08, ogol 2020-01-08; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 0-0 Nova Iguaçu: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Friburguense 2-2 América-RJ: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Madureira 1-0 Portuguesa-RJ: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-0 Flamengo: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Resende 0-0 Boavista-RJ: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 1-0 Botafogo: RSSSF 2019-01-18, ogol 2020-01-18; fica a do ogol
- ano errado na data da RSSSF — Vasco 0-0 Bangu: RSSSF 2019-01-19, ogol 2020-01-19; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 0-1 Fluminense: RSSSF 2019-01-19, ogol 2020-01-19; fica a do ogol
- ano errado na data da RSSSF — Madureira 2-0 Botafogo: RSSSF 2019-01-21, ogol 2020-01-21; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 4-0 Cabofriense: RSSSF 2019-01-22, ogol 2020-01-22; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-3 Boavista-RJ: RSSSF 2019-01-22, ogol 2020-01-22; fica a do ogol
- ano errado na data da RSSSF — Resende 1-1 Bangu: RSSSF 2019-01-23, ogol 2020-01-23; fica a do ogol
- ano errado na data da RSSSF — Fluminense 2-0 Portuguesa-RJ: RSSSF 2019-01-23, ogol 2020-01-23; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 1-2 Friburguense: RSSSF 2019-01-25, ogol 2020-01-25; fica a do ogol
- ano errado na data da RSSSF — América-RJ 4-0 Americano-RJ: RSSSF 2019-01-25, ogol 2020-01-25; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 0-1 Madureira: RSSSF 2019-01-25, ogol 2020-01-25; fica a do ogol
- ano errado na data da RSSSF — Flamengo 3-2 Volta Redonda: RSSSF 2019-01-25, ogol 2020-01-25; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 0-1 Vasco: RSSSF 2019-01-25, ogol 2020-01-25; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 1-0 Resende: RSSSF 2019-01-26, ogol 2020-01-26; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-5 Fluminense: RSSSF 2019-01-26, ogol 2020-01-26; fica a do ogol
- ano errado na data da RSSSF — Botafogo 3-1 Macaé: RSSSF 2019-01-26, ogol 2020-01-26; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 3-1 Madureira: RSSSF 2019-01-28, ogol 2020-01-28; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 4-1 Macaé: RSSSF 2019-01-29, ogol 2020-01-29; fica a do ogol
- ano errado na data da RSSSF — Bangu 0-1 Volta Redonda: RSSSF 2019-01-29, ogol 2020-01-29; fica a do ogol
- ano errado na data da RSSSF — Flamengo 0-1 Fluminense: RSSSF 2019-01-29, ogol 2020-01-29; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-1 Resende: RSSSF 2019-01-30, ogol 2020-01-30; fica a do ogol
- ano errado na data da RSSSF — Vasco 0-1 Cabofriense: RSSSF 2019-01-31, ogol 2020-01-31; fica a do ogol
- ano errado na data da RSSSF — Madureira 0-0 Bangu: RSSSF 2019-02-01, ogol 2020-02-01; fica a do ogol
- ano errado na data da RSSSF — Fluminense 0-1 Boavista-RJ: RSSSF 2019-02-01, ogol 2020-02-01; fica a do ogol
- ano errado na data da RSSSF — Botafogo 1-0 Vasco: RSSSF 2019-02-02, ogol 2020-02-02; fica a do ogol
- ano errado na data da RSSSF — Macaé 1-0 Cabofriense: RSSSF 2019-02-03, ogol 2020-02-03; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 2-0 Portuguesa-RJ: RSSSF 2019-02-03, ogol 2020-02-03; fica a do ogol
- ano errado na data da RSSSF — Resende 1-3 Flamengo: RSSSF 2019-02-03, ogol 2020-02-03; fica a do ogol
- ano errado na data da RSSSF — Friburguense 1-2 Americano-RJ: RSSSF 2019-02-05, ogol 2020-02-05; fica a do ogol
- ano errado na data da RSSSF — América-RJ 1-2 Nova Iguaçu: RSSSF 2019-02-05, ogol 2020-02-05; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 0-4 Americano-RJ: RSSSF 2019-02-08, ogol 2020-02-08; fica a do ogol
- ano errado na data da RSSSF — América-RJ 2-2 Friburguense: RSSSF 2019-02-08, ogol 2020-02-08; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-0 Macaé: RSSSF 2019-02-08, ogol 2020-02-08; fica a do ogol
- ano errado na data da RSSSF — Flamengo 2-0 Madureira: RSSSF 2019-02-08, ogol 2020-02-08; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 2-1 Volta Redonda: RSSSF 2019-02-08, ogol 2020-02-08; fica a do ogol
- ano errado na data da RSSSF — Fluminense 3-0 Botafogo: RSSSF 2019-02-09, ogol 2020-02-09; fica a do ogol
- ano errado na data da RSSSF — Portuguesa-RJ 2-3 Vasco: RSSSF 2019-02-09, ogol 2020-02-09; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 2-3 Resende: RSSSF 2019-02-09, ogol 2020-02-09; fica a do ogol
- ano errado na data da RSSSF — Friburguense 1-0 Nova Iguaçu: RSSSF 2019-02-15, ogol 2020-02-15; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 1-1 Volta Redonda: RSSSF 2019-02-16, ogol 2020-02-16; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 2-0 América-RJ: RSSSF 2019-02-16, ogol 2020-02-16; fica a do ogol
- ano errado na data da RSSSF — Americano-RJ 1-2 Friburguense: RSSSF 2019-02-19, ogol 2020-02-19; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 2-2 América-RJ: RSSSF 2019-02-19, ogol 2020-02-19; fica a do ogol
- ano errado na data da RSSSF — Bangu 1-0 Portuguesa-RJ: RSSSF 2019-02-28, ogol 2020-02-28; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 1-0 Macaé: RSSSF 2019-02-28, ogol 2020-02-28; fica a do ogol
- ano errado na data da RSSSF — Fluminense 5-1 Madureira: RSSSF 2019-03-01, ogol 2020-03-01; fica a do ogol
- ano errado na data da RSSSF — Botafogo 2-1 Boavista-RJ: RSSSF 2019-03-01, ogol 2020-03-01; fica a do ogol
- ano errado na data da RSSSF — América-RJ 0-1 Americano-RJ: RSSSF 2019-03-04, ogol 2020-03-04; fica a do ogol
- ano errado na data da RSSSF — Boavista-RJ 2-1 Bangu: RSSSF 2019-03-06, ogol 2020-03-06; fica a do ogol
- ano errado na data da RSSSF — Nova Iguaçu 0-2 América-RJ: RSSSF 2019-03-07, ogol 2020-03-07; fica a do ogol
- ano errado na data da RSSSF — Cabofriense 1-4 Portuguesa-RJ: RSSSF 2019-03-07, ogol 2020-03-07; fica a do ogol
- ano errado na data da RSSSF — Macaé 0-3 Madureira: RSSSF 2019-03-07, ogol 2020-03-07; fica a do ogol
- ano errado na data da RSSSF — Flamengo 3-0 Botafogo: RSSSF 2019-03-07, ogol 2020-03-07; fica a do ogol
- ano errado na data da RSSSF — Volta Redonda 0-0 Vasco: RSSSF 2019-03-08, ogol 2020-03-08; fica a do ogol
- ano errado na data da RSSSF — Fluminense 4-0 Resende: RSSSF 2019-03-08, ogol 2020-03-08; fica a do ogol
- jogo só no ogol, incluído em First Stage - First Phase: Vasco 0-1 Flamengo (2020-01-23)
- jogo só no ogol, incluído em Preliminary Phase: Boavista-RJ 1-2 Flamengo (2020-02-22)
- jogo só no ogol, incluído em Preliminary Phase / Group Z: Nova Iguaçu 1-2 Americano-RJ (2020-03-14)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Resende 0-1 Macaé (2020-03-14)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Flamengo 2-1 Portuguesa-RJ (2020-03-14)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Boavista-RJ 2-0 Cabofriense (2020-03-14)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Botafogo 1-1 Bangu (2020-03-15)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Vasco 0-2 Fluminense (2020-03-15)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Madureira 2-1 Volta Redonda (2020-03-16)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Bangu 0-3 Flamengo (2020-06-19)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Portuguesa-RJ 0-0 Boavista-RJ (2020-06-19)
- jogo só no ogol, incluído em Preliminary Phase / Group Z: Americano-RJ 0-2 América-RJ (2020-06-27)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Botafogo 6-2 Cabofriense (2020-06-28)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Madureira 0-2 Resende (2020-06-28)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Vasco 3-1 Macaé (2020-06-28)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Fluminense 0-3 Volta Redonda (2020-06-28)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Bangu 1-0 Cabofriense (2020-07-01)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Flamengo 2-0 Boavista-RJ (2020-07-02)
- jogo só no ogol, incluído em Second Stage - First Phase / Group A: Portuguesa-RJ 0-0 Botafogo (2020-07-02)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Macaé 0-0 Fluminense (2020-07-02)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Vasco 1-0 Madureira (2020-07-03)
- jogo só no ogol, incluído em Second Stage - First Phase / Group B: Volta Redonda 2-1 Resende (2020-07-03)
- jogo só no ogol, incluído em Preliminary Phase / Group Z: América-RJ 1-1 Nova Iguaçu (2020-07-04)
- jogo só no ogol, incluído em Semifinals - Taça Guanabara: Flamengo 2-0 Volta Redonda (2020-07-05)
- jogo só no ogol, incluído em First Stage - First Phase: Fluminense 0-0 Botafogo (2020-07-05)
- jogo só no ogol, incluído em Semifinals - Taça Guanabara: Fluminense 1-1 Flamengo (2020-07-09)
- jogo só no ogol, incluído em Semifinals - Taça Guanabara: Fluminense 1-2 Flamengo (2020-07-12)
- jogo só no ogol, incluído em Semifinals - Taça Guanabara: Flamengo 1-0 Fluminense (2020-07-16)
- só na RSSSF (não achado no ogol): Vasco 0-1 Flamengo (2019-01-22)
- só na RSSSF (não achado no ogol): Boavista-RJ 1-2 Flamengo (2019-02-17)

### 2021

- sem ocorrências

### 2022

- tabela publicada x jogos — Primeira fase / -: Nova Iguaçu tabela [7, 4, 2, 1, 9, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / -: Resende tabela [7, 3, 2, 2, 8, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / -: Madureira tabela [7, 3, 2, 2, 5, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / -: Audax Rio tabela [7, 3, 1, 3, 6, 8] jogos [13, 3, 2, 8, 11, 18] — a tabela conta 7 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / -: Portuguesa-RJ tabela [7, 2, 3, 2, 5, 5] jogos [13, 3, 4, 6, 13, 15] — a tabela conta 7 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / -: Bangu tabela [7, 1, 3, 3, 4, 7] jogos [11, 2, 3, 6, 5, 17] — a tabela conta 7 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Volta Redonda tabela [7, 1, 2, 4, 9, 9] jogos [11, 1, 3, 7, 11, 21] — a tabela conta 7 jogos e as fontes trazem 11

### 2023

- campeão pela lista oficial, Fluminense; o 1º pela soma dos jogos da última fase é Botafogo (desempate, jogo extra ou pontos tirados fora de campo)

### 2024

- tabela publicada x jogos — Primeira fase / -: Vasco tabela [13, 6, 5, 2, 21, 13] jogos [13, 6, 5, 2, 21, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Flamengo x Nova Iguaçu, ogol 2024-04-07); fica a do ogol

### 2025

- sem página da RSSSF (a lista de campeões tem o link, mas a página não existe): os jogos vêm do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

### 2026

- sem página da RSSSF: os jogos vêm do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Flamengo

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Clube que o ogol não tem entra pela RSSSF, com código "rs-<nome>". Nunca com o nome exato de outro clube (regra 6b).
- Mesmo clube com outro nome fica com o nome de hoje (Botafogo Football Club e Botafogo de Futebol e Regatas, depois da
  fusão de 1942).

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** 3.383 gols com autor, quase todos de 2010 em diante (74% dos gols dos anos 2010). Nas outras
  décadas a RSSSF não traz os autores ou traz num formato que o leitor ainda não junta ao jogo ("Gols: ..." na linha de
  baixo, nos anos 1900); só entram quando a soma bate com o placar (pendência).
- **W.O. sem vencedor:** o ogol traz cerca de 66 W.O. (1908-1935) sem dizer quem venceu; o vencedor sai da tabela
  publicada, e o W.O. conta como vitória sem gols. Sem como decidir pela tabela, fica fora (ver as temporadas).
- **Torneios à parte:** os de consolação entre os turnos (2009-2012) e as séries de subúrbio (1928-1930) ficam fora.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.
