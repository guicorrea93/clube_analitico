# Campeonato Mineiro (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-mg-1/importar.py`. Pacote em `data/coleta/bra-mg-1/pacote/`. Mesmo código do Carioca
(`docs/coleta/bra-rj-1.md`), com as fontes de Minas Gerais.

**Temporadas:** 1915 a 2026. Até os anos 1940 é o campeonato dos clubes de Belo Horizonte e arredores; o interior entra
aos poucos (1958-1959 com os torneios de classificação; de 1970 em diante, o campeonato estadual). Em 1932 houve duas
ligas e a FMF reconhece os dois títulos: cada torneio é uma edição ("1932 LMDT" e "1932 AMEG"). 1956 teve título
dividido (Atlético e Cruzeiro). 1925 é a edição que a liga considerou inexistente na época e a FMF homologou em 2012
(campeão o América). Em 2002 Atlético, Cruzeiro e América (Copa Sul-Minas) não jogaram; o campeão foi a Caldense.

**Fontes:** RSSSF Brasil (`tablesfq/mg{ano}.htm`: jogos, fases, datas, autores e tabelas; `mg1926l.htm`,
`mg1932l.htm` e `mg1932a.htm` com a letra da liga); ogol (calendário de cada edição e o código de cada clube; confere
placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do Campeonato
Mineiro: tabela de resultados ano a ano, segunda fonte do campeão e do vice). Artilheiros pela lista da RSSSF
(`mgtops.htm`).

**Fases:** os torneios de classificação (1921, 1958-1959, 1970-1973) entram como "Fase classificatória"; os
desempates como "<fase> - Desempate"; os turnos com semifinal e final próprias (1975-1987) como "1º Turno",
"1º Turno - Final" etc. Jogos anulados ou cancelados ("[annulled]", "[cancelled]") ficam fora. A repescagem contra o
campeão da 2ª divisão fica só na observação da edição (decisão D-04). Os Torneios Paralelos de 1976 (consolação) ficam fora.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. W.O. conta como vitória sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o
placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo nome (cadastro comum
`data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1915 | RSSSF + ogol | 5 | 16 (16) | 43 | 31 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 | RSSSF + ogol | 6 | 20 (20) | 55 | 40 | 2 / 0 | América-MG | RSSSF (classificação geral publicada) |
| 1917 | RSSSF + ogol | 5 | 20 (20) | 36 | 17 | 2 / 0 | América-MG | RSSSF (classificação geral publicada) |
| 1918 | RSSSF + ogol | 5 | 17 (17) | 50 | 39 | 0 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1919 | RSSSF + ogol | 4 | 12 (11) | 39 | 8 | 0 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF + ogol | 6 | 32 (32) | 141 | 78 | 2 / 0 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF + ogol | 12 | 48 (42) | 180 | 97 | 2 / 0 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF + ogol | 7 | 43 (43) | 129 | 62 | 0 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1923 | RSSSF + ogol | 7 | 19 (21) | 70 | 24 | 0 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 | RSSSF + ogol | 5 | 7 (4) | 22 | 0 | 2 / 0 | América-MG | RSSSF (classificação geral publicada) |
| 1925 | RSSSF | 6 | 4 (0) | 13 | 6 | 0 / 0 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 | RSSSF + ogol | 6 | 31 (36) | 155 | 0 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 | RSSSF + ogol | 11 | 58 (59) | 296 | 178 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 | RSSSF + ogol | 9 | 72 (72) | 423 | 349 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1929 | RSSSF + ogol | 10 | 63 (57) | 364 | 315 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF + ogol | 7 | 42 (52) | 243 | 219 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF + ogol | 5 | 24 (55) | 124 | 110 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 LMDT | RSSSF + ogol | 8 | 56 (56) | 249 | 220 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 AMEG | RSSSF + ogol | 6 | 30 (30) | 126 | 0 | 0 / 2 | Villa Nova-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 | RSSSF + ogol | 9 | 72 (68) | 291 | 253 | 0 / 0 | Villa Nova-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 | RSSSF + ogol | 8 | 43 (43) | 174 | 147 | 2 / 0 | Villa Nova-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 | RSSSF + ogol | 6 | 30 (30) | 141 | 129 | 2 / 0 | Villa Nova-MG | RSSSF (classificação geral publicada) |
| 1936 | RSSSF + ogol | 3 | 9 (36) | 57 | 57 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF + ogol | 6 | 34 (33) | 99 | 92 | 0 / 2 | Siderúrgica | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF + ogol | 6 | 45 (45) | 142 | 132 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF + ogol | 6 | 44 (45) | 129 | 114 | 0 / 4 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF + ogol | 5 | 23 (30) | 86 | 77 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF + ogol | 7 | 52 (52) | 217 | 214 | 1 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF + ogol | 6 | 30 (36) | 105 | 89 | 2 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 1943 | RSSSF + ogol | 6 | 30 (30) | 105 | 97 | 2 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 1944 | RSSSF + ogol | 6 | 45 (45) | 156 | 150 | 1 / 1 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF + ogol | 7 | 63 (63) | 238 | 230 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF + ogol | 7 | 63 (63) | 216 | 214 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF + ogol | 7 | 42 (42) | 174 | 158 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF + ogol | 7 | 63 (63) | 221 | 207 | 0 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF + ogol | 7 | 63 (63) | 228 | 209 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF + ogol | 7 | 42 (42) | 182 | 179 | 2 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 1951 | RSSSF + ogol | 8 | 59 (59) | 203 | 203 | 5 / 0 | Villa Nova-MG | RSSSF (classificação geral publicada) |
| 1952 | RSSSF + ogol | 9 | 74 (73) | 268 | 268 | 4 / 1 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF + ogol | 10 | 93 (93) | 328 | 314 | 4 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF + ogol | 9 | 98 (97) | 310 | 293 | 6 / 1 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF + ogol | 9 | 92 (92) | 308 | 286 | 6 / 4 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF + ogol | 10 | 96 (96) | 322 | 320 | 3 / 2 | Atlético-MG | RSSSF (classificação geral publicada) |
| 1957 | RSSSF + ogol | 10 | 96 (96) | 312 | 253 | 2 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF + ogol | 16 | 182 (182) | 629 | 603 | 4 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF + ogol | 17 | 194 (194) | 636 | 625 | 8 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF + ogol | 16 | 240 (240) | 771 | 757 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF + ogol | 14 | 185 (185) | 552 | 550 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF + ogol | 12 | 135 (135) | 373 | 365 | 2 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF + ogol | 12 | 132 (132) | 315 | 299 | 0 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF + ogol | 12 | 132 (132) | 352 | 343 | 2 / 0 | Siderúrgica | RSSSF (classificação geral publicada) |
| 1965 | RSSSF + ogol | 12 | 132 (132) | 441 | 419 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF + ogol | 12 | 132 (132) | 383 | 380 | 0 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF + ogol | 12 | 134 (134) | 385 | 385 | 2 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF + ogol | 12 | 132 (132) | 347 | 328 | 2 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 1969 | RSSSF + ogol | 16 | 240 (240) | 636 | 610 | 2 / 3 | Cruzeiro | RSSSF (classificação geral publicada) |
| 1970 | RSSSF + ogol | 28 | 300 (300) | 771 | 694 | 2 / 4 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF + ogol | 21 | 177 (177) | 388 | 347 | 8 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF + ogol | 20 | 157 (157) | 348 | 306 | 10 / 7 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF + ogol | 16 | 125 (125) | 270 | 205 | 12 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF + ogol | 14 | 126 (126) | 299 | 286 | 6 / 3 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF + ogol | 16 | 106 (106) | 249 | 228 | 2 / 8 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF + ogol | 23 | 189 (251) | 468 | 445 | 10 / 8 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF + ogol | 12 | 135 (135) | 275 | 266 | 2 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF + ogol | 12 | 144 (144) | 301 | 299 | 2 / 4 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF + ogol | 16 | 273 (273) | 651 | 644 | 0 / 7 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF + ogol | 21 | 119 (119) | 289 | 273 | 8 / 1 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF + ogol | 12 | 162 (162) | 343 | 312 | 4 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF + ogol | 12 | 200 (201) | 393 | 366 | 4 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF + ogol | 12 | 192 (191) | 420 | 412 | 1 / 9 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF + ogol | 14 | 194 (194) | 375 | 373 | 4 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF + ogol | 14 | 211 (207) | 371 | 236 | 2 / 7 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF + ogol | 16 | 240 (240) | 500 | 264 | 0 / 5 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF + ogol | 16 | 248 (248) | 429 | 421 | 0 / 5 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 16 | 240 (240) | 522 | 2 | 1 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF + ogol | 17 | 192 (188) | 409 | 0 | 5 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 18 | 307 (307) | 686 | 1 | 4 / 1 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF + ogol | 24 | 288 (288) | 553 | 0 | 15 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 1992 | RSSSF + ogol | 24 | 209 (209) | 456 | 194 | 12 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF + ogol | 23 | 185 (185) | 406 | 153 | 12 / 1 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 12 | 132 (132) | 334 | 0 | 2 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 1995 | RSSSF + ogol | 12 | 132 (132) | 302 | 4 | 5 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 1996 | RSSSF + ogol | 13 | 186 (186) | 445 | 1 | 4 / 3 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 12 | 146 (146) | 375 | 0 | 2 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 12 | 110 (110) | 282 | 5 | 2 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 12 | 127 (127) | 312 | 312 | 4 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 12 | 114 (114) | 327 | 327 | 2 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 12 | 92 (92) | 243 | 232 | 4 / 2 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 8 | 56 (56) | 155 | 149 | 2 / 0 | Caldense | RSSSF (classificação geral publicada) |
| 2003 | RSSSF + ogol | 13 | 78 (78) | 252 | 250 | 0 / 2 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2004 | RSSSF + ogol | 14 | 97 (97) | 293 | 275 | 2 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 12 | 72 (72) | 208 | 208 | 2 / 0 | Ipatinga | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 12 | 72 (72) | 218 | 214 | 2 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 12 | 72 (72) | 201 | 201 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2008 | RSSSF + ogol | 12 | 72 (72) | 208 | 208 | 3 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 12 | 80 (80) | 220 | 220 | 2 / 1 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 12 | 80 (80) | 248 | 248 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 12 | 72 (72) | 246 | 211 | 2 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 12 | 72 (72) | 195 | 190 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 12 | 72 (72) | 209 | 197 | 2 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 12 | 72 (72) | 168 | 165 | 3 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2015 | RSSSF + ogol | 12 | 72 (72) | 156 | 156 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2016 | RSSSF + ogol | 12 | 72 (72) | 173 | 168 | 1 / 3 | América-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 12 | 72 (72) | 160 | 155 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2018 | RSSSF + ogol | 12 | 76 (76) | 164 | 157 | 0 / 3 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2019 | RSSSF + ogol | 12 | 76 (76) | 194 | 192 | 3 / 0 | Cruzeiro | RSSSF (classificação geral publicada) |
| 2020 | RSSSF + ogol | 12 | 72 (75) | 163 | 163 | 0 / 3 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 12 | 72 (75) | 152 | 152 | 3 / 0 | Atlético-MG | RSSSF (classificação geral publicada) |
| 2022 | RSSSF + ogol | 12 | 73 (78) | 159 | 152 | 0 / 3 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 12 | 59 (66) | 145 | 145 | 1 / 6 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 12 | 60 (66) | 168 | 157 | 5 / 2 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 12 | 54 (60) | 118 | 115 | 6 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | RSSSF + ogol | 12 | 53 (59) | 126 | 126 | 6 / 2 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1915

- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [8, 6, 1, 1, 21, 5] jogos [8, 6, 1, 1, 20, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Hygienicos tabela [6, 0, 1, 5, 3, 12] jogos [6, 0, 1, 5, 3, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [8, 6, 1, 1, 21, 5] jogos [8, 6, 1, 1, 20, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Hygienicos tabela [6, 0, 1, 5, 3, 12] jogos [6, 0, 1, 5, 3, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1916

- sem ocorrências

### 1917

- placar diferente no ogol — Atlético-MG x Sete de Setembro-MG (1917-06-28): RSSSF 4-0, ogol 6-0; fica o da RSSSF
- placar diferente no ogol — Sete de Setembro-MG x Christovam Colombo (1917-07-29): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Atlético-MG x Sete de Setembro-MG, ogol 1917-06-28); fica a do ogol

### 1918

- tabela publicada x jogos — Fase única / -: América-MG tabela [8, 7, 1, 0, 22, 4] jogos [8, 6, 2, 0, 22, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [6, 0, 1, 5, 4, 14] jogos [6, 0, 2, 4, 4, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: América-MG tabela [8, 7, 1, 0, 22, 4] jogos [8, 6, 2, 0, 22, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [6, 0, 1, 5, 4, 14] jogos [6, 0, 2, 4, 4, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado ou cancelado fica de fora: Villa Nova 10-1 Yale (1918-04-21) [annulled]
- jogo anulado ou cancelado fica de fora: Luzitano 0-7 Villa Nova (1918-05-12) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 0-2 América (1918-06-02) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro - Villa Nova (1918-06-23) [W.O.: victory awarded to Sete de Setembro; annulled]
- jogo anulado ou cancelado fica de fora: Atlético - Villa Nova (1918-06-30) [W.O.: victory awarded to Atlético; annulled]
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Yale-MG, ogol 1918-09-08); fica a do ogol

### 1919

- tabela publicada x jogos — Fase única / -: América-MG tabela [6, 5, 1, 0, 19, 7] jogos [6, 5, 1, 0, 21, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [6, 4, 0, 2, 9, 9] jogos [6, 4, 0, 2, 11, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-MG tabela [6, 5, 1, 0, 19, 7] jogos [6, 5, 1, 0, 21, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [6, 4, 0, 2, 9, 9] jogos [6, 4, 0, 2, 11, 7] — há jogo do clube sem conferência no ogol
- jogo anulado ou cancelado fica de fora: Yale 3-0 Sete de Setembro (1919-05-04) [cancelled]
- jogo anulado ou cancelado fica de fora: Yale 0-0 Atlético (1919-05-25) [cancelled]
- jogo anulado ou cancelado fica de fora: América 2-1 Yale (1919-06-08) [cancelled]
- jogo anulado ou cancelado fica de fora: Luzitano 1-3 Yale (1919-07-06) [cancelled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Corinthians
- Corinthians — clube que o ogol não tem; entra só pela RSSSF
- só na RSSSF (não achado no ogol): Atlético-MG None-None Sete de Setembro-MG (1919-07-13)

### 1920

- jogo anulado ou cancelado fica de fora: S. de Setembro 2-1 Alves Nogueira (1920-05-16) [annulled]
- jogo anulado ou cancelado fica de fora: América - Alves Nogueira (1920-06-13) [W.O.: victory awarded to América; annulled]
- jogo anulado ou cancelado fica de fora: Guarany 2-0 Alves Nogueira (1920-06-27) [annulled]
- jogo anulado ou cancelado fica de fora: Yale 6-0 Alves Nogueira (1920-07-25) [annulled]
- jogo anulado ou cancelado fica de fora: Luzitano 3-2 Alves Nogueira (1920-09-19) [annulled]
- 1 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Guarany 3-2 Ipanema (13/03/1921)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Sete de Setembro-MG, ogol 1921-01-09); fica a do ogol
- campeão pela lista oficial, América-MG; o 1º pela soma dos jogos da última fase é Sete de Setembro-MG (desempate, jogo extra ou pontos tirados fora de campo)

### 1921

- jogo anulado ou cancelado fica de fora: Sete de Setembro 2-3 Progresso (1921-04-21) [annulled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hellênico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipanema
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- Hellênico — clube que o ogol não tem; entra só pela RSSSF
- Ipanema — clube que o ogol não tem; entra só pela RSSSF
- Palmeiras — clube que o ogol não tem; entra só pela RSSSF
- placar diferente no ogol — Atlético-MG x Luzitano-MG (1921-06-19): RSSSF 1-3, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Cruzeiro x Guarany B. Horizonte, ogol 1921-07-07); fica a do ogol
- só na RSSSF (não achado no ogol): Cruzeiro 3-2 Ipanema (None)
- só na RSSSF (não achado no ogol): Guarany B. Horizonte 2-1 Hellênico-MG (1921-04-21)
- só na RSSSF (não achado no ogol): Cruzeiro 4-1 Palmeiras-MG (1921-04-21)
- só na RSSSF (não achado no ogol): Luzitano-MG 6-0 Christovam Colombo (1921-04-21)
- só na RSSSF (não achado no ogol): Sete de Setembro-MG 1-0 Progresso-BH (1921-05-01)
- só na RSSSF (não achado no ogol): Guarany B. Horizonte 0-2 Progresso-BH (1921-12-25)
- campeão pela lista oficial, América-MG; o 1º pela soma dos jogos da última fase é Progresso-BH (desempate, jogo extra ou pontos tirados fora de campo)

### 1922

- tabela publicada x jogos — Primeira fase / -: América-MG tabela [12, 8, 2, 2, 35, 13] jogos [12, 8, 2, 2, 34, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [12, 7, 4, 1, 20, 12] jogos [12, 7, 4, 1, 20, 11] — placar diverge entre RSSSF e ogol em Cruzeiro x Luzitano-MG (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [12, 8, 2, 2, 35, 13] jogos [12, 8, 2, 2, 34, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [12, 7, 4, 1, 20, 12] jogos [12, 7, 4, 1, 20, 11] — placar diverge entre RSSSF e ogol em Cruzeiro x Luzitano-MG (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- jogo só no ogol, incluído em Fase única: Yale-MG 0-0 Luzitano-MG (1922-06-25)

### 1923

- tabela publicada x jogos — Fase única / -: América-MG tabela [6, 5, 1, 0, 25, 5] jogos [6, 5, 1, 0, 26, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [6, 3, 3, 0, 10, 5] jogos [6, 3, 3, 0, 11, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [5, 1, 2, 2, 5, 8] jogos [5, 1, 2, 2, 5, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Yale-MG tabela [4, 0, 2, 2, 5, 7] jogos [4, 0, 2, 2, 5, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: América-MG tabela [6, 5, 1, 0, 25, 5] jogos [6, 5, 1, 0, 26, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [6, 3, 3, 0, 10, 5] jogos [6, 3, 3, 0, 11, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [5, 1, 2, 2, 5, 8] jogos [5, 1, 2, 2, 5, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Yale-MG tabela [4, 0, 2, 2, 5, 7] jogos [4, 0, 2, 2, 5, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado fica de fora (1): América 10-0 Yale — 2º turno: uma assembleia geral anulou todos os jogos do 2º turno e deu o título ao América, vencedor do 1º (a página marca os outros jogos "[annulled]", este não)
- jogo anulado ou cancelado fica de fora: Atlético 2-1 Yale (1923-04-22) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 1-0 Luzitano (1923-04-22) [annulled]
- jogo anulado ou cancelado fica de fora: Yale 0-3 Atlético (1923-08-26) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 3-3 Luzitano (1923-08-26) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 1-0 Luzitano (1923-10-07) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Itália - Yale (1923-10-07) [W.O.: victory awarded to Yale; *]           [annulled]
- jogo anulado ou cancelado fica de fora: América 1-0 Palestra Itália (1923-10-14) [annulled]
- 1 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Progresso 0-3 Palmeiras (20/05/1923)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: América-MG x Luzitano-MG, ogol 1923-06-08); fica a do ogol

### 1924

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-MG)
- data com dia e mês trocados na RSSSF em 1 jogos (ex.: América-MG x Sete de Setembro-MG); fica a data do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-MG x Yale-MG, ogol 1924-06-11); fica a do ogol
- só na RSSSF (não achado no ogol): Palmeiras-MG 0-1 Sete de Setembro-MG (1924-10-05)
- só na RSSSF (não achado no ogol): América-MG 3-0 Palmeiras-MG (1924-10-12)
- só na RSSSF (não achado no ogol): América-MG None-None Cruzeiro (1924-12-21)

### 1925

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Luzitano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra Itália
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sete de Setembro
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-MG)
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-MG)
- Luzitano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Luzitano-MG)
- Palestra Itália — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro)
- Sete de Setembro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sete de Setembro-MG)
- campeão pela lista oficial, América-MG; o 1º pela soma dos jogos da última fase é Sete de Setembro-MG (desempate, jogo extra ou pontos tirados fora de campo)

### 1926

- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [10, 8, 1, 1, 37, 17] jogos [11, 9, 1, 1, 44, 18] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [10, 8, 0, 2, 34, 17] jogos [10, 8, 0, 2, 34, 23] — placar diverge entre RSSSF e ogol em Guarany B. Horizonte x Palmeiras-MG (None-None x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: América-MG tabela [10, 4, 0, 6, 30, 23] jogos [10, 5, 1, 4, 30, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Calafate tabela [10, 3, 1, 6, 15, 19] jogos [10, 3, 2, 5, 15, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [10, 3, 0, 7, 17, 36] jogos [11, 2, 0, 9, 18, 43] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [10, 8, 0, 2, 34, 17] jogos [10, 8, 0, 2, 34, 23] — placar diverge entre RSSSF e ogol em Guarany B. Horizonte x Palmeiras-MG (None-None x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: América-MG tabela [10, 4, 0, 6, 30, 23] jogos [9, 5, 0, 4, 30, 23] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Calafate tabela [10, 3, 1, 6, 15, 19] jogos [9, 3, 1, 5, 15, 19] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [10, 3, 0, 7, 17, 36] jogos [10, 2, 0, 8, 17, 36] — há jogo do clube sem conferência no ogol
- jogo anulado ou cancelado fica de fora: América 1-2 Syrio (1926-05-09) [annulled]
- jogo anulado ou cancelado fica de fora: Calafate 1-3 Syrio (1926-05-30) [annulled]
- jogo anulado ou cancelado fica de fora: Syrio 4-0 Guarany (1926-06-27) [annulled]
- jogo anulado ou cancelado fica de fora: Syrio 3-1 Palmeiras (1926-06-29) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 5-2 Syrio (1926-07-18) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 2-2 Syrio (1926-07-25) [annulled]
- jogo anulado ou cancelado fica de fora: América 1-1 Syrio (1926-08-29) [annulled]
- mando invertido no ogol — RSSSF Atlético-MG 6-3 América-MG, ogol América-MG 3-6 Atlético-MG (1926-05-23); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Guarany B. Horizonte x Calafate na Fase única sempre na mesma ordem) — ogol Calafate 2-0 Guarany B. Horizonte (1926-09-19)
- mando invertido no ogol — RSSSF América-MG 1-2 Calafate, ogol Calafate 2-1 América-MG (1926-10-10); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Palmeiras-MG na Fase única sempre na mesma ordem) — ogol Palmeiras-MG 4-1 Atlético-MG (1926-10-17)
- mando invertido e placar diferente no ogol — RSSSF América-MG None-None Sete de Setembro-MG, ogol Sete de Setembro-MG 0-1 América-MG (1926-12-09); fica a RSSSF
- jogo só no ogol, incluído em Fase única: América-MG 0-0 Calafate (1926-07-11)
- jogo só no ogol, incluído em Fase única: Sete de Setembro-MG 1-7 Atlético-MG (1926-10-24)
- só na RSSSF (não achado no ogol): Atlético-MG 7-1 Sete de Setembro-MG (1926-09-15)
- só na RSSSF (não achado no ogol): Atlético-MG None-None Calafate (1926-10-03)

### 1927

- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [12, 7, 1, 4, 44, 29] jogos [12, 7, 1, 4, 44, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Syrio Horizontino tabela [10, 2, 1, 7, 16, 35] jogos [10, 2, 1, 7, 14, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [12, 10, 1, 1, 56, 145] jogos [12, 10, 1, 1, 56, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Cruzeiro tabela [12, 7, 1, 4, 44, 29] jogos [12, 7, 1, 4, 44, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Syrio Horizontino tabela [10, 2, 1, 7, 16, 35] jogos [10, 2, 1, 7, 14, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado ou cancelado fica de fora: Villa Nova 4-5 Atlético (1927-09-04) [annulled]
- mando invertido no ogol — RSSSF Atlético-MG 3-1 América-MG, ogol América-MG 1-3 Atlético-MG (1927-06-12); fica a RSSSF
- campeão pela lista oficial, Atlético-MG; o 1º pela soma dos jogos da última fase é América-MG (desempate, jogo extra ou pontos tirados fora de campo)

### 1928

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [16, 13, 2, 1, 93, 18] jogos [16, 13, 2, 1, 91, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [16, 12, 3, 1, 60, 24] jogos [16, 12, 3, 1, 59, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [16, 1, 2, 13, 15, 92] jogos [16, 1, 2, 13, 15, 90] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [16, 13, 2, 1, 93, 18] jogos [16, 13, 2, 1, 91, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [16, 12, 3, 1, 60, 24] jogos [16, 12, 3, 1, 59, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [16, 1, 2, 13, 15, 92] jogos [16, 1, 2, 13, 15, 90] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado ou cancelado fica de fora: Palestra Itália 8-2 Syrio Horizontino (1928-04-08) [Cancelled]
- jogo anulado ou cancelado fica de fora: Sete Setembro 5-2 Syrio Horizontino (1928-04-22) [Cancelled]
- jogo anulado ou cancelado fica de fora: Alves Nogueira 2-1 Syrio Horizontino (1928-04-29) [Cancelled]
- jogo anulado ou cancelado fica de fora: Palmeiras 2-3 Syrio Horizontino (1928-05-13) [Cancelled]
- jogo anulado ou cancelado fica de fora: Atlético 10-0 Syrio Horizontino (1928-05-27) [Cancelled]
- jogo anulado ou cancelado fica de fora: Villa Nova 3-2 Syrio Horizontino (1928-06-10) [Cancelled]
- jogo anulado ou cancelado fica de fora: Calafate 2-2 Syrio Horizontino (1928-07-01) [Cancelled]
- jogo anulado ou cancelado fica de fora: América 3-1 Syrio Horizontino (1928-07-15) [Cancelled]
- jogo anulado ou cancelado fica de fora: Guarany 1-1 Syrio Horizontino (1928-07-22) [Cancelled]
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Guarany B. Horizonte na Fase única sempre na mesma ordem) — ogol Guarany B. Horizonte 2-3 Atlético-MG (1928-11-11)
- mando invertido no ogol — RSSSF Atlético-MG 3-6 América-MG, ogol América-MG 6-3 Atlético-MG (1928-11-25); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Calafate na Fase única sempre na mesma ordem) — ogol Calafate 1-6 Atlético-MG (1928-12-09)
- placar diferente no ogol — Alves Nogueira x Guarany B. Horizonte (1928-04-15): RSSSF 3-3, ogol 3-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 9 jogos (ex.: Atlético-MG x Palmeiras-MG, ogol 1928-08-05); fica a do ogol

### 1929

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [14, 14, 0, 0, 82, 12] jogos [15, 15, 0, 0, 83, 12] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [14, 11, 0, 3, 80, 17] jogos [14, 11, 0, 3, 80, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-MG tabela [14, 11, 0, 3, 68, 18] jogos [14, 11, 0, 3, 67, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [14, 7, 1, 6, 35, 40] jogos [15, 7, 1, 7, 36, 40] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Santa Cruz B. Horizonte tabela [8, 3, 0, 5, 15, 41] jogos [13, 6, 1, 6, 21, 46] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Guarany B. Horizonte tabela [14, 2, 2, 10, 18, 73] jogos [15, 2, 3, 10, 19, 74] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [8, 2, 0, 6, 16, 44] jogos [10, 3, 0, 7, 20, 47] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [14, 14, 0, 0, 82, 12] jogos [15, 15, 0, 0, 83, 12] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [14, 11, 0, 3, 80, 17] jogos [14, 11, 0, 3, 80, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-MG tabela [14, 11, 0, 3, 68, 18] jogos [14, 11, 0, 3, 67, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [14, 7, 1, 6, 35, 40] jogos [15, 7, 1, 7, 36, 40] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Santa Cruz B. Horizonte tabela [8, 3, 0, 5, 15, 41] jogos [13, 6, 1, 6, 21, 46] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Guarany B. Horizonte tabela [14, 2, 2, 10, 18, 73] jogos [15, 2, 3, 10, 19, 74] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Palmeiras-MG tabela [8, 2, 0, 6, 16, 44] jogos [10, 3, 0, 7, 20, 47] — a tabela conta 8 jogos e as fontes trazem 10
- jogo anulado ou cancelado fica de fora: América 4-5 Palestra Itália (1929-06-02) [match annulled and rescheduled to July 7]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Villa Nova
- Villa Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Villa Nova-MG)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na League sempre na mesma ordem) — ogol Sete de Setembro-MG 1-3 Atlético-MG (1929-04-28)
- mando invertido no ogol — RSSSF Atlético-MG 7-1 Calafate, ogol Calafate 1-7 Atlético-MG (1929-05-05); fica a RSSSF
- mando invertido no ogol — RSSSF Calafate 0-13 Atlético-MG, ogol Atlético-MG 13-0 Calafate (1929-08-11); fica a RSSSF
- só na RSSSF (não achado no ogol): Palmeiras-MG 1-3 Santa Cruz B. Horizonte (1929-04-14)
- só na RSSSF (não achado no ogol): Palmeiras-MG 3-0 Santa Cruz B. Horizonte (1929-05-19)
- só na RSSSF (não achado no ogol): Sete de Setembro-MG 0-2 Santa Cruz B. Horizonte (1929-04-21)
- só na RSSSF (não achado no ogol): Cruzeiro None-None Villa Nova-MG (1929-04-21)
- só na RSSSF (não achado no ogol): Santa Cruz B. Horizonte None-None Villa Nova-MG (1929-04-28)
- só na RSSSF (não achado no ogol): Santa Cruz B. Horizonte 1-1 Guarany B. Horizonte (1929-05-05)

### 1930

- tabela publicada x jogos — Fase única / -: América-MG tabela [12, 9, 0, 3, 51, 27] jogos [12, 9, 0, 3, 50, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [12, 7, 0, 5, 49, 21] jogos [12, 7, 0, 5, 49, 19] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Calafate (None-None x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [12, 5, 1, 6, 30, 38] jogos [12, 5, 1, 6, 29, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Calafate tabela [12, 3, 2, 7, 16, 35] jogos [12, 3, 2, 7, 15, 35] — placar diverge entre RSSSF e ogol em Calafate x Palmeiras-MG (3-2 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: América-MG tabela [12, 9, 0, 3, 51, 27] jogos [12, 9, 0, 3, 50, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [12, 7, 0, 5, 49, 21] jogos [12, 7, 0, 5, 49, 19] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Calafate (None-None x 0-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [12, 5, 1, 6, 30, 38] jogos [12, 5, 1, 6, 29, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Calafate tabela [12, 3, 2, 7, 16, 35] jogos [12, 3, 2, 7, 15, 35] — placar diverge entre RSSSF e ogol em Calafate x Palmeiras-MG (3-2 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- jogo anulado ou cancelado fica de fora: Atlético 3-3 Calafate (1930-04-20) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 9-0 Guarany (1930-04-27) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 3-0 Sete de Setembro (1930-05-04) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 1-2 Palestra Itália (1930-06-01) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 4-6 América (1930-06-08) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 8-0 Palmeiras (1930-06-15) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 0-2 Atlético (1930-06-29) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 11-0 Calafate (1930-07-08) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 6-1 Guarany (1930-07-13) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 9-1 Sete de Setembro (1930-07-20) [annulled]
- 3 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Fluminense 6-1 Palmeiras (07/12/1930); Palmeiras 4-4 Fluminense (14/12/1930); Palmeiras 0-1 Fluminense (21/12/1930)
- placar diferente no ogol — Calafate x Palmeiras-MG (1930-08-24): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Calafate x Palmeiras-MG, ogol 1930-08-24); fica a do ogol

### 1931

- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [8, 7, 0, 1, 45, 11] jogos [8, 7, 0, 1, 45, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarany B. Horizonte tabela [8, 2, 0, 6, 19, 38] jogos [8, 2, 0, 6, 18, 38] — placar diverge entre RSSSF e ogol em Guarany B. Horizonte x Calafate (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [8, 7, 0, 1, 45, 11] jogos [8, 7, 0, 1, 45, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarany B. Horizonte tabela [8, 2, 0, 6, 19, 38] jogos [8, 2, 0, 6, 18, 38] — placar diverge entre RSSSF e ogol em Guarany B. Horizonte x Calafate (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- jogo anulado ou cancelado fica de fora: Villa Nova 4-3 Fluminense (1931-04-19) [annulled]
- jogo anulado ou cancelado fica de fora: América 4-2 Sete de Setembro (1931-04-19) [annulled]
- jogo anulado ou cancelado fica de fora: Guarany 4-5 Villa Nova (1931-04-26) [annulled]
- jogo anulado ou cancelado fica de fora: América 6-0 Calafate (1931-04-26) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 1-2 América (1931-05-17) [annulled]
- jogo anulado ou cancelado fica de fora: Fluminense 6-2 Sete de Setembro (1931-05-17) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 2-2 Villa Nova (1931-05-24) [annulled]
- jogo anulado ou cancelado fica de fora: América 4-2 Fluminense (1931-05-24) [annulled]
- jogo anulado ou cancelado fica de fora: Guarany 6-5 Sete de Setembro (1931-05-24) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 1-2 América (1931-05-31) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 11-0 Calafate (1931-05-31) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Itália 4-1 Sete de Setembro (1931-05-31) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 7-1 Sete de Setembro (1931-06-07) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Itália 1-3 Villa Nova (1931-06-07) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 2-1 Sete de Setembro (1931-06-14) [annulled]
- jogo anulado ou cancelado fica de fora: América 4-3 Palestra Itália (1931-06-14) [annulled]
- jogo anulado ou cancelado fica de fora: Calafate 5-7 Sete de Setembro (1931-06-21) [annulled]
- jogo anulado ou cancelado fica de fora: América 2-1 Guarany (1931-06-21) [Match cancelled by LMDT and rescheduled to August 9]
- jogo anulado ou cancelado fica de fora: América 11-1 Guarany (1931-08-09) [annulled]
- jogo anulado ou cancelado fica de fora: Fluminense 0-0 Villa Nova (1931-08-23) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 10-0 Sete de Setembro (1931-08-30) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 4-1 Guarany (1931-08-30) [annulled]
- jogo anulado ou cancelado fica de fora: Calafate 1-7 América (1931-08-30) [annulled]
- jogo anulado ou cancelado fica de fora: América 1-2 Villa Nova (1931-09-06) [annulled]
- jogo anulado ou cancelado fica de fora: Guarany 0-0 Sete de Setembro (1931-09-06) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 2-1 Palestra Itália (1931-09-13) [annulled]
- jogo anulado ou cancelado fica de fora: América 7-1 Sete de Setembro (1931-09-13) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 0-3 Villa Nova (1931-09-20) [annulled]
- jogo anulado ou cancelado fica de fora: Fluminense 2-4 América (1931-09-20) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 3-3 Atlético (1931-09-27) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Itália 8-1 América (1931-09-27) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro - Palestra Itália (1931-10-04) [W.O.: victory awarded to Palestra Itália; annulled]
- jogo anulado ou cancelado fica de fora: América - Guarany (1931-10-04) [W.O.: victory awarded to Guarany; annulled]
- jogo anulado ou cancelado fica de fora: Calafate - Villa Nova (1931-10-04) [W.O.: victory awarded to Calafate; annulled]
- jogo anulado ou cancelado fica de fora: Calafate - Sete de Setembro (1931-11-01) [cancelled]
- jogo do ogol tirado junto com o da RSSSF: Fluminense-BH 4-1 Guarany B. Horizonte (1931-05-31)
- mando invertido no ogol — RSSSF Guarany B. Horizonte 2-3 Atlético-MG, ogol Atlético-MG 3-2 Guarany B. Horizonte (1931-09-20); fica a RSSSF
- placar diferente no ogol — Guarany B. Horizonte x Calafate (1931-10-11): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- só na RSSSF (não achado no ogol): Fluminense-BH 4-1 Guarany B. Horizonte (1931-05-31)
- só na RSSSF (não achado no ogol): América-MG None-None Atlético-MG (1931-10-11)
- só na RSSSF (não achado no ogol): Fluminense-BH None-None Sete de Setembro-MG (1931-10-11)

### 1932 LMDT

- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [14, 12, 2, 0, 48, 12] jogos [14, 12, 2, 0, 47, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Calafate tabela [14, 1, 2, 11, 18, 47] jogos [14, 1, 2, 11, 20, 51] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [14, 12, 2, 0, 48, 12] jogos [14, 12, 2, 0, 47, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Calafate tabela [14, 1, 2, 11, 18, 47] jogos [14, 1, 2, 11, 20, 51] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fuminense
- Fuminense — clube que o ogol não tem; entra só pela RSSSF
- mando invertido no ogol — RSSSF Santa Cruz B. Horizonte 1-1 Atlético-MG, ogol Atlético-MG 1-1 Santa Cruz B. Horizonte (1932-06-12); fica a RSSSF
- mando invertido no ogol — RSSSF Carlos Prates 1-3 Atlético-MG, ogol Atlético-MG 3-1 Carlos Prates (1932-06-26); fica a RSSSF
- mando invertido no ogol — RSSSF Calafate 0-4 Atlético-MG, ogol Atlético-MG 4-0 Calafate (1932-09-11); fica a RSSSF

### 1932 AMEG

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [10, 7, 1, 2, 34, 17] jogos [10, 7, 1, 2, 35, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: América-MG tabela [10, 4, 0, 6, 21, 17] jogos [10, 4, 0, 6, 21, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Vespasiano-MG tabela [10, 2, 1, 7, 15, 28] jogos [10, 2, 1, 7, 14, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [10, 7, 1, 2, 34, 17] jogos [10, 7, 1, 2, 35, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: América-MG tabela [10, 4, 0, 6, 21, 17] jogos [10, 4, 0, 6, 21, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Vespasiano-MG tabela [10, 2, 1, 7, 15, 28] jogos [10, 2, 1, 7, 14, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1933

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Retiro na Fase única sempre na mesma ordem) — ogol Retiro 1-3 Atlético-MG (1933-06-25)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Cruzeiro x Atlético-MG na Fase única sempre na mesma ordem) — ogol Atlético-MG 2-3 Cruzeiro (1933-10-22)
- placar diferente no ogol — Retiro x América-MG (1933-07-02): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-MG x Retiro, ogol 1934-01-21); fica a do ogol
- só na RSSSF (não achado no ogol): Tupynambás None-None Atlético-MG (1933-10-29)
- só na RSSSF (não achado no ogol): Tupi None-None Retiro (1933-11-12)
- só na RSSSF (não achado no ogol): Sport-MG None-None América-MG (1933-11-19)
- só na RSSSF (não achado no ogol): Sport-MG None-None Siderúrgica (1933-12-10)

### 1934

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 1-2 Atlético-MG (1934-06-10)
- mando invertido no ogol — RSSSF Sete de Setembro-MG 2-6 Atlético-MG, ogol Atlético-MG 6-2 Sete de Setembro-MG (1934-07-08); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Sete de Setembro-MG x Villa Nova-MG, ogol 1934-08-05); fica a do ogol

### 1935

- sem ocorrências

### 1936

- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [6, 3, 1, 2, 20, 14] jogos [6, 3, 1, 2, 19, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Retiro tabela [6, 0, 0, 6, 5, 38] jogos [6, 0, 0, 6, 5, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [6, 3, 1, 2, 20, 14] jogos [6, 3, 1, 2, 19, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Retiro tabela [6, 0, 0, 6, 5, 38] jogos [6, 0, 0, 6, 5, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- 10 jogos do Palestra Itália ficam de fora: abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)
- 8 jogos do América ficam de fora: abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)
- 9 jogos do Villa Nova ficam de fora: abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)

### 1937

- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [10, 6, 2, 2, 21, 10] jogos [10, 5, 3, 2, 21, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [10, 4, 2, 4, 15, 12] jogos [11, 5, 2, 4, 17, 13] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Retiro tabela [10, 0, 2, 8, 6, 24] jogos [11, 0, 3, 8, 7, 26] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [10, 6, 2, 2, 21, 10] jogos [10, 5, 3, 2, 21, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Retiro tabela [10, 0, 2, 8, 6, 24] jogos [10, 0, 3, 7, 6, 24] — placar diverge entre RSSSF e ogol em Atlético-MG x Retiro (1-1 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Atlético-MG x Retiro (1938-01-26): RSSSF 1-1, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Retiro, ogol 1938-01-26); fica a do ogol
- jogo só no ogol, incluído em Fase única: Retiro 1-2 Atlético-MG (1938-01-02)
- só na RSSSF (não achado no ogol): Atlético-MG 3-0 Retiro (1938-01-26)

### 1938

- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [15, 6, 3, 6, 22, 17] jogos [15, 5, 4, 6, 22, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [15, 6, 3, 6, 22, 17] jogos [15, 5, 4, 6, 22, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 0-3 Atlético-MG (1938-06-19)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 0-3 Atlético-MG (1938-09-04)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 1-3 Atlético-MG (1938-11-20)

### 1939

- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [15, 7, 2, 6, 18, 19] jogos [15, 7, 2, 6, 17, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [15, 1, 0, 14, 16, 45] jogos [14, 1, 0, 13, 14, 40] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [15, 7, 2, 6, 18, 19] jogos [15, 7, 2, 6, 17, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [15, 1, 0, 14, 16, 45] jogos [14, 1, 0, 13, 14, 40] — a tabela conta 15 jogos e as fontes trazem 14
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 2-4 Atlético-MG (1939-09-10)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de América-MG x Atlético-MG na Fase única sempre na mesma ordem) — ogol Atlético-MG 0-0 América-MG (1939-09-17)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 0-4 Atlético-MG (1940-01-11)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Villa Nova-MG, ogol 1939-08-28); fica a do ogol
- jogo só no ogol, incluído em Fase única: Cruzeiro 2-2 América-MG (1939-12-31)
- jogo só no ogol, incluído em Fase única: Cruzeiro 2-0 Atlético-MG (1940-02-18)

### 1940

- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [7, 4, 3, 0, 21, 7] jogos [8, 4, 3, 1, 22, 10] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [7, 5, 1, 1, 18, 9] jogos [8, 5, 1, 2, 21, 10] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [8, 2, 1, 5, 13, 20] jogos [8, 3, 1, 4, 13, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [7, 4, 3, 0, 21, 7] jogos [8, 4, 3, 1, 22, 10] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [7, 5, 1, 1, 18, 9] jogos [8, 5, 1, 2, 21, 10] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [8, 2, 1, 5, 13, 20] jogos [8, 3, 1, 4, 13, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado ou cancelado fica de fora: Sete de Setembro 1-4 Atlético (1940-05-19) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Itália 4-1 Sete de Setembro (1940-06-09) [annulled]
- jogo anulado ou cancelado fica de fora: América 2-3 Sete de Setembro (1940-06-16) [annulled]
- jogo anulado ou cancelado fica de fora: Siderúrgica 7-1 Sete de Setembro (1940-06-30) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 1-3 Villa Nova (1940-07-07) [annulled]
- jogo anulado ou cancelado fica de fora: Sete de Setembro 1-4 América (1940-10-20) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 5-1 Sete de Setembro (1940-11-03) [annulled]
- jogo anulado ou cancelado fica de fora: Atlético 2-0 Sete de Setembro (1940-12-15) [annulled]
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Siderúrgica x Villa Nova-MG, ogol 1940-06-21); fica a do ogol
- só na RSSSF (não achado no ogol): Atlético-MG 1-3 Cruzeiro (1940-12-29)

### 1941

- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [12, 9, 1, 2, 39, 15] jogos [12, 9, 1, 2, 39, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [12, 9, 1, 2, 39, 15] jogos [12, 9, 1, 2, 39, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 5-3 América-MG, ogol América-MG 3-5 Atlético-MG (1941-08-18); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Aeroporto na Fase única sempre na mesma ordem) — ogol Aeroporto 1-6 Atlético-MG (1941-09-14)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Siderúrgica x América-MG, ogol 1941-11-01); fica a do ogol

### 1942

- jogo anulado ou cancelado fica de fora: Atlético 3-1 Aeroporto (1942-05-15) [annulled]
- jogo anulado ou cancelado fica de fora: América 4-1 Aeroporto (1942-05-31) [annulled]
- jogo anulado ou cancelado fica de fora: Villa Nova 2-2 Aeroporto (1942-06-14) [annulled]
- jogo anulado ou cancelado fica de fora: Siderúrgica 1-1 Aeroporto (1942-06-28) [annulled]
- jogo anulado ou cancelado fica de fora: Palestra Mineiro 6-2 Aeroporto (1942-07-12) [annulled]
- jogo anulado ou cancelado fica de fora: Aeroporto 2-1 Sete de Setembro (1942-07-26) [annulled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra Mineiro
- Palestra Mineiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro)
- mando invertido no ogol — RSSSF Sete de Setembro-MG 0-2 Atlético-MG, ogol Atlético-MG 2-0 Sete de Setembro-MG (1942-07-19); fica a RSSSF
- mando invertido no ogol — RSSSF Atlético-MG 2-0 Sete de Setembro-MG, ogol Sete de Setembro-MG 0-2 Atlético-MG (1942-09-27); fica a RSSSF
- mando invertido no ogol — RSSSF Cruzeiro 1-2 Atlético-MG, ogol Atlético-MG 2-1 Cruzeiro (1942-10-04); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Villa Nova-MG, ogol 1942-06-24); fica a do ogol

### 1943

- sem ocorrências

### 1944

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [15, 9, 6, 0, 30, 17] jogos [15, 9, 6, 0, 31, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [15, 9, 2, 4, 33, 17] jogos [15, 9, 2, 4, 33, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1945

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [18, 14, 2, 2, 50, 22] jogos [18, 13, 3, 2, 50, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [18, 10, 3, 5, 40, 28] jogos [18, 10, 4, 4, 40, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [18, 6, 1, 11, 18, 45] jogos [18, 5, 2, 11, 18, 45] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Uberaba tabela [18, 4, 3, 11, 28, 44] jogos [18, 4, 4, 10, 28, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [18, 14, 2, 2, 50, 22] jogos [18, 13, 3, 2, 50, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [18, 10, 3, 5, 40, 28] jogos [18, 10, 4, 4, 40, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [18, 6, 1, 11, 18, 45] jogos [18, 5, 2, 11, 18, 45] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Uberaba tabela [18, 4, 3, 11, 28, 44] jogos [18, 4, 4, 10, 28, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Cruzeiro x Atlético-MG na Fase única sempre na mesma ordem) — ogol Atlético-MG 2-3 Cruzeiro (1945-09-16)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Uberaba, ogol 1945-07-01); fica a do ogol

### 1946

- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [18, 14, 3, 1, 50, 20] jogos [18, 14, 3, 1, 49, 19] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Atlético-MG (1-1 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [18, 5, 1, 12, 25, 37] jogos [18, 5, 1, 12, 24, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [18, 14, 3, 1, 50, 20] jogos [18, 14, 3, 1, 49, 19] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Atlético-MG (1-1 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [18, 5, 1, 12, 25, 37] jogos [18, 5, 1, 12, 24, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 2-1 América-MG, ogol América-MG 1-2 Atlético-MG (1946-04-14); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 3-5 Atlético-MG (1946-10-02)

### 1947

- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [12, 6, 4, 2, 26, 15] jogos [12, 6, 3, 3, 26, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [12, 0, 1, 11, 14, 47] jogos [12, 1, 0, 11, 17, 47] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [12, 6, 4, 2, 26, 15] jogos [12, 6, 3, 3, 26, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [12, 0, 1, 11, 14, 47] jogos [12, 1, 0, 11, 17, 47] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 2-1 América-MG, ogol América-MG 1-2 Atlético-MG (1947-05-25); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 0-2 Atlético-MG, ogol Atlético-MG 2-0 América-MG (1947-10-05); fica a RSSSF

### 1948

- tabela publicada x jogos — Fase única / -: América-MG tabela [18, 13, 3, 2, 42, 17] jogos [18, 13, 3, 2, 42, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [18, 6, 2, 10, 29, 42] jogos [18, 6, 2, 10, 28, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-MG tabela [18, 13, 3, 2, 42, 17] jogos [18, 13, 3, 2, 42, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [18, 6, 2, 10, 29, 42] jogos [18, 6, 2, 10, 28, 42] — há jogo do clube sem conferência no ogol
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Siderúrgica na Fase única sempre na mesma ordem) — ogol Siderúrgica 1-4 Atlético-MG (1948-10-16)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x América-MG, ogol 1948-08-28); fica a do ogol
- jogo só no ogol, incluído em Fase única: Siderúrgica 3-1 Sete de Setembro-MG (1948-05-09)

### 1949

- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [18, 14, 2, 2, 50, 23] jogos [18, 13, 2, 3, 50, 23] — placar diverge entre RSSSF e ogol em Atlético-MG x Villa Nova-MG (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [18, 9, 4, 5, 25, 22] jogos [18, 9, 4, 5, 26, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Metalusina tabela [18, 6, 2, 10, 29, 36] jogos [18, 5, 3, 10, 30, 37] — placar diverge entre RSSSF e ogol em Metalusina x Villa Nova-MG (1-1 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [18, 3, 5, 10, 30, 37] jogos [18, 4, 6, 8, 32, 38] — placar diverge entre RSSSF e ogol em Atlético-MG x Villa Nova-MG (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [18, 4, 1, 13, 21, 39] jogos [18, 4, 1, 13, 21, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [18, 14, 2, 2, 50, 23] jogos [18, 13, 2, 3, 50, 23] — placar diverge entre RSSSF e ogol em Atlético-MG x Villa Nova-MG (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [18, 9, 4, 5, 25, 22] jogos [18, 9, 4, 5, 26, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Metalusina tabela [18, 6, 2, 10, 29, 36] jogos [18, 5, 3, 10, 30, 37] — placar diverge entre RSSSF e ogol em Metalusina x Villa Nova-MG (1-1 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [18, 3, 5, 10, 30, 37] jogos [18, 4, 6, 8, 32, 38] — placar diverge entre RSSSF e ogol em Atlético-MG x Villa Nova-MG (2-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Sete de Setembro-MG tabela [18, 4, 1, 13, 21, 39] jogos [18, 4, 1, 13, 21, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Siderúrgica na Fase única sempre na mesma ordem) — ogol Siderúrgica 1-6 Atlético-MG (1949-06-25)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Siderúrgica na Fase única sempre na mesma ordem) — ogol Siderúrgica 1-2 Atlético-MG (1949-09-18)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Villa Nova-MG na Fase única sempre na mesma ordem) — ogol Villa Nova-MG 3-5 Atlético-MG (1949-10-08)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 2-2 Atlético-MG (1949-10-23)
- campeão pela lista oficial, Atlético-MG; o 1º pela soma dos jogos da última fase é América-MG (desempate, jogo extra ou pontos tirados fora de campo)

### 1950

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 2-6 Atlético-MG (1950-12-31)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Atlético-MG x Villa Nova-MG, ogol 1950-06-23); fica a do ogol

### 1951

- mando invertido no ogol — RSSSF Villa Nova-MG 1-1 Atlético-MG, ogol Atlético-MG 1-1 Villa Nova-MG (1952-01-13); fica a RSSSF

### 1952

- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [16, 15, 0, 1, 40, 8] jogos [18, 17, 0, 1, 45, 10] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [16, 11, 1, 4, 44, 17] jogos [18, 11, 1, 6, 37, 20] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metalusina tabela [16, 5, 0, 11, 28, 40] jogos [16, 5, 0, 11, 27, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 6-0 Asas, ogol Asas 0-6 Atlético-MG (1952-11-27); fica a RSSSF
- só na RSSSF (não achado no ogol): Sete de Setembro-MG 1-3 Villa Nova-MG (1953-01-03)

### 1953

- mando invertido no ogol — RSSSF Atlético-MG 1-0 Sete de Setembro-MG, ogol Sete de Setembro-MG 0-1 Atlético-MG (1953-10-18); fica a RSSSF

### 1954

- tabela publicada x jogos — OVERALL TABLE - FIRST AND SECOND STAGES / -: Cruzeiro tabela [16, 12, 2, 2, 44, 17] jogos [22, 13, 4, 5, 49, 23] — a tabela conta 16 jogos e as fontes trazem 22
- tabela publicada x jogos — OVERALL TABLE - FIRST AND SECOND STAGES / -: Atlético-MG tabela [16, 12, 2, 2, 28, 14] jogos [22, 15, 4, 3, 34, 19] — a tabela conta 16 jogos e as fontes trazem 22
- mando invertido no ogol — RSSSF Atlético-MG 2-0 Cruzeiro, ogol Cruzeiro 0-2 Atlético-MG (1955-05-01); fica a RSSSF
- só na RSSSF (não achado no ogol): Sete de Setembro-MG 1-3 Asas (1955-01-16)

### 1955

- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [8, 6, 1, 1, 16, 7] jogos [8, 6, 1, 1, 15, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [8, 3, 4, 1, 15, 14] jogos [8, 2, 4, 2, 14, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [8, 3, 2, 3, 10, 12] jogos [8, 3, 2, 3, 10, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [8, 6, 1, 1, 16, 7] jogos [8, 6, 1, 1, 15, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [8, 3, 4, 1, 15, 14] jogos [8, 2, 4, 2, 14, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [8, 3, 2, 3, 10, 12] jogos [8, 3, 2, 3, 10, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Democrata-SL tabela [16, 12, 3, 1, 37, 15] jogos [16, 12, 3, 1, 38, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [16, 10, 4, 2, 30, 15] jogos [20, 11, 5, 4, 34, 24] — a tabela conta 16 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Siderúrgica tabela [16, 7, 6, 3, 30, 26] jogos [16, 6, 6, 4, 29, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: América-MG tabela [16, 7, 4, 5, 22, 19] jogos [16, 7, 4, 5, 22, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Villa Nova-MG tabela [16, 6, 4, 6, 31, 30] jogos [20, 9, 5, 6, 41, 34] — a tabela conta 16 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Asas tabela [16, 4, 4, 8, 28, 29] jogos [16, 4, 4, 8, 28, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [27, 16, 7, 4, 55, 32] jogos [28, 17, 7, 4, 55, 31] — a tabela conta 27 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase final / -: Villa Nova-MG tabela [27, 9, 7, 11, 49, 52] jogos [28, 9, 7, 12, 49, 53] — a tabela conta 27 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase final / -: América-MG tabela [20, 8, 7, 5, 27, 22] jogos [20, 8, 7, 5, 27, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Siderúrgica tabela [20, 7, 7, 6, 35, 35] jogos [20, 7, 7, 6, 34, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Villa Nova-MG 6-2 Atlético-MG, ogol Atlético-MG 2-6 Villa Nova-MG (1956-04-15); fica a RSSSF
- mando invertido no ogol — RSSSF Democrata-SL 0-1 Atlético-MG, ogol Atlético-MG 1-0 Democrata-SL (1956-05-13); fica a RSSSF

### 1956

- título dividido entre Atlético e Cruzeiro: o pacote tem o Atlético em campeao, o Cruzeiro em co_campeao e o vice vazio (D-07, como o Carioca 1907 e o Paulista 1973)
- tabela publicada x jogos — Segunda fase / -: Siderúrgica tabela [9, 5, 1, 3, 19, 9] jogos [9, 5, 1, 3, 19, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Siderúrgica tabela [9, 5, 1, 3, 19, 9] jogos [9, 5, 1, 3, 19, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 1-0 América-MG, ogol América-MG 0-1 Atlético-MG (1956-08-22); fica a RSSSF
- mando invertido no ogol — RSSSF Metalusina 1-6 Atlético-MG, ogol Atlético-MG 6-1 Metalusina (1956-11-11); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Cruzeiro na Finals sempre na mesma ordem) — ogol Cruzeiro 0-1 Atlético-MG (1957-06-02)
- placar diferente no ogol — Asas x Meridional (1956-09-30): RSSSF 4-2, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Sete de Setembro-MG x Siderúrgica, ogol 1956-08-18); fica a do ogol

### 1957

- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [9, 7, 1, 1, 24, 6] jogos [9, 6, 3, 0, 24, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [9, 3, 1, 5, 15, 15] jogos [9, 3, 1, 5, 14, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [9, 7, 1, 1, 24, 6] jogos [9, 6, 3, 0, 24, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Siderúrgica tabela [9, 3, 1, 5, 15, 15] jogos [9, 3, 1, 5, 14, 14] — há jogo do clube sem conferência no ogol
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de América-MG x Siderúrgica na Segunda fase - Desempate sempre na mesma ordem) — ogol Siderúrgica 1-1 América-MG (1957-12-05)
- placar diferente no ogol — América-MG x Villa Nova-MG (1957-10-06): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Sete de Setembro-MG x Democrata-SL, ogol 1957-10-12); fica a do ogol
- jogo só no ogol, incluído em FIRST STAGE:: Meridional 0-4 Democrata-SL (1957-07-07)
- jogo só no ogol, incluído em FIRST STAGE:: Asas 3-4 Atlético-MG (1957-07-14)
- jogo só no ogol, incluído em FIRST STAGE:: Meridional 3-1 Sete de Setembro-MG (1957-07-21)
- jogo só no ogol, incluído em FIRST STAGE:: Meridional 2-1 Siderúrgica (1957-08-11)
- jogo só no ogol, incluído em SECOND STAGE:: Democrata-SL 4-1 Metalusina (1957-10-06)

### 1958

- tabela publicada x jogos — Fase classificatória / -: Democrata-SL tabela [15, 9, 2, 4, 35, 23] jogos [15, 9, 2, 4, 35, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / -: Curvelo tabela [15, 3, 1, 11, 25, 43] jogos [15, 3, 1, 11, 24, 43] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / -: Democrata-SL tabela [15, 9, 2, 4, 35, 23] jogos [15, 9, 2, 4, 35, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / -: Curvelo tabela [15, 3, 1, 11, 25, 43] jogos [15, 3, 1, 11, 24, 43] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- ano errado na data da RSSSF — Cruzeiro 1-1 América-MG: RSSSF 1959-04-05, ogol 1958-04-05; fica a do ogol
- ano errado na data da RSSSF — América-MG 1-1 Cruzeiro: RSSSF 1959-04-09, ogol 1958-04-09; fica a do ogol
- ano errado na data da RSSSF — América-MG 3-1 Cruzeiro: RSSSF 1959-04-12, ogol 1958-04-12; fica a do ogol

### 1959

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Sete de Setembro-MG x Atlético-MG na QUALIFY TOURNAMENTS sempre na mesma ordem) — ogol Atlético-MG 0-0 Sete de Setembro-MG (1959-07-04)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Renascença na LEAGUE sempre na mesma ordem) — ogol Renascença 0-2 Atlético-MG (1960-03-27)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 24 jogos (ex.: Bela Vista-MG x Curvelo, ogol 1959-07-05); fica a do ogol

### 1960

- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [30, 21, 6, 3, 55, 24] jogos [30, 21, 6, 3, 56, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [30, 16, 5, 9, 55, 35] jogos [30, 16, 5, 9, 55, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Pedro Leopoldo FC tabela [30, 11, 6, 13, 45, 56] jogos [30, 11, 6, 13, 45, 57] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Guarani-MG tabela [30, 8, 8, 14, 44, 51] jogos [30, 8, 8, 14, 45, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Curvelo tabela [30, 7, 5, 18, 41, 62] jogos [30, 7, 5, 18, 40, 62] — placar diverge entre RSSSF e ogol em Curvelo x Metalusina (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Metalusina tabela [30, 5, 4, 21, 26, 79] jogos [30, 5, 4, 21, 26, 78] — placar diverge entre RSSSF e ogol em Curvelo x Metalusina (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Cruzeiro tabela [30, 21, 6, 3, 55, 24] jogos [30, 21, 6, 3, 56, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético-MG tabela [30, 16, 5, 9, 55, 35] jogos [30, 16, 5, 9, 55, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Pedro Leopoldo FC tabela [30, 11, 6, 13, 45, 56] jogos [30, 11, 6, 13, 45, 57] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Guarani-MG tabela [30, 8, 8, 14, 44, 51] jogos [30, 8, 8, 14, 45, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Curvelo tabela [30, 7, 5, 18, 41, 62] jogos [30, 7, 5, 18, 40, 62] — placar diverge entre RSSSF e ogol em Curvelo x Metalusina (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Metalusina tabela [30, 5, 4, 21, 26, 79] jogos [30, 5, 4, 21, 26, 78] — placar diverge entre RSSSF e ogol em Curvelo x Metalusina (None-None x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Siderúrgica x Atlético-MG na Fase única sempre na mesma ordem) — ogol Atlético-MG 2-2 Siderúrgica (1960-09-03)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Valeriodoce na Fase única sempre na mesma ordem) — ogol Valeriodoce 0-1 Atlético-MG (1960-10-30)
- mando invertido no ogol — RSSSF América-MG 1-0 Atlético-MG, ogol Atlético-MG 0-1 América-MG (1960-11-13); fica a RSSSF

### 1961

- tabela publicada x jogos — Primeira fase / -: Renascença tabela [26, 5, 10, 11, 34, 38] jogos [26, 6, 10, 10, 34, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-MG tabela [26, 3, 9, 14, 33, 48] jogos [26, 2, 9, 15, 33, 48] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Renascença tabela [26, 5, 10, 11, 34, 38] jogos [26, 6, 10, 10, 34, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-MG tabela [26, 3, 9, 14, 33, 48] jogos [26, 2, 9, 15, 33, 48] — há jogo do clube sem conferência no ogol
- 3 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Itaú 1-0 Bela Vista (03/06/1962); Bela Vista 2-0 Itaú (10/06/1962); Bela Vista 2-2 Itaú (13/06/1962)
- jogo do ogol tirado junto com o da RSSSF: Itaú 1-0 Bela Vista-MG (1962-06-03)
- jogo do ogol tirado junto com o da RSSSF: Itaú 0-2 Bela Vista-MG (1962-06-10)
- jogo do ogol tirado junto com o da RSSSF: Bela Vista-MG 2-2 Itaú (1962-06-13)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Pedro Leopoldo FC na Fase única sempre na mesma ordem) — ogol Pedro Leopoldo FC 0-3 Atlético-MG (1961-09-03)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Sete de Setembro-MG na Fase única sempre na mesma ordem) — ogol Sete de Setembro-MG 0-1 Atlético-MG (1961-09-23)
- mando invertido no ogol — RSSSF Renascença 0-1 Atlético-MG, ogol Atlético-MG 1-0 Renascença (1962-02-04); fica a RSSSF
- mando invertido no ogol — RSSSF Valeriodoce 1-4 Sete de Setembro-MG, ogol Sete de Setembro-MG 4-1 Valeriodoce (1962-02-18); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Bela Vista-MG na Fase única sempre na mesma ordem) — ogol Bela Vista-MG 3-1 Atlético-MG (1962-02-18)
- placar diferente no ogol — Atlético-MG x Uberaba (1961-10-07): RSSSF 3-1, ogol 3-2; fica o da RSSSF
- campeão pela lista oficial, Cruzeiro; o 1º pela soma dos jogos da última fase é Renascença (desempate, jogo extra ou pontos tirados fora de campo)

### 1962

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Atlético-MG x Pedro Leopoldo FC, ogol 1962-09-12); fica a do ogol

### 1963

- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [22, 10, 5, 7, 28, 21] jogos [22, 11, 4, 7, 28, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Renascença tabela [22, 5, 6, 11, 19, 31] jogos [22, 5, 5, 12, 18, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Siderúrgica tabela [22, 10, 5, 7, 28, 21] jogos [22, 11, 4, 7, 28, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Renascença tabela [22, 5, 6, 11, 19, 31] jogos [22, 5, 5, 12, 18, 31] — há jogo do clube sem conferência no ogol
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Pedro Leopoldo FC na Fase única sempre na mesma ordem) — ogol Pedro Leopoldo FC 0-1 Atlético-MG (1963-07-21)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 1-2 Atlético-MG (1963-08-10)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Renascença na Fase única sempre na mesma ordem) — ogol Renascença 0-2 Atlético-MG (1963-08-25)
- mando invertido no ogol — RSSSF Atlético-MG 2-0 América-MG, ogol América-MG 0-2 Atlético-MG (1963-11-17); fica a RSSSF
- mando invertido no ogol — RSSSF Valeriodoce 2-3 Atlético-MG, ogol Atlético-MG 3-2 Valeriodoce (1963-12-08); fica a RSSSF

### 1964

- sem ocorrências

### 1965

- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [22, 6, 7, 9, 29, 42] jogos [22, 5, 7, 10, 29, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Uberaba tabela [22, 4, 7, 11, 26, 36] jogos [22, 5, 8, 9, 26, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Renascença tabela [22, 4, 6, 12, 29, 47] jogos [22, 3, 7, 12, 29, 47] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [22, 6, 7, 9, 29, 42] jogos [22, 5, 7, 10, 29, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Uberaba tabela [22, 4, 7, 11, 26, 36] jogos [22, 5, 8, 9, 26, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Renascença tabela [22, 4, 6, 12, 29, 47] jogos [22, 3, 7, 12, 29, 47] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Villa Nova-MG 1-5 Atlético-MG, ogol Atlético-MG 5-1 Villa Nova-MG (1965-07-15); fica a RSSSF

### 1966

- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [22, 9, 4, 9, 31, 32] jogos [22, 9, 4, 9, 30, 32] — placar diverge entre RSSSF e ogol em Uberlândia x Villa Nova-MG (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Uberlândia tabela [22, 7, 8, 7, 29, 33] jogos [22, 7, 8, 7, 29, 32] — placar diverge entre RSSSF e ogol em Uberlândia x Villa Nova-MG (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Villa Nova-MG tabela [22, 9, 4, 9, 31, 32] jogos [22, 9, 4, 9, 30, 32] — placar diverge entre RSSSF e ogol em Uberlândia x Villa Nova-MG (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Uberlândia tabela [22, 7, 8, 7, 29, 33] jogos [22, 7, 8, 7, 29, 32] — placar diverge entre RSSSF e ogol em Uberlândia x Villa Nova-MG (3-2 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Uberlândia x Villa Nova-MG (1966-11-20): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América-MG x Siderúrgica, ogol 1966-08-11); fica a do ogol

### 1967

- 2 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Nacional-U 1-3 Independente-U (31/03/1968); Independente-U 1-0 Nacional-U (02/04/1968)
- jogo do ogol tirado junto com o da RSSSF: Nacional Uberaba 1-3 Independente-MG (1968-03-31)
- jogo do ogol tirado junto com o da RSSSF: Independente-MG 1-0 Nacional Uberaba (1968-04-02)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 0-1 Atlético-MG (1967-08-13)
- mando invertido no ogol — RSSSF Uberlândia 0-2 Atlético-MG, ogol Atlético-MG 2-0 Uberlândia (1967-09-02); fica a RSSSF

### 1968

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na Fase única sempre na mesma ordem) — ogol América-MG 0-1 Atlético-MG (1968-07-27)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 25 jogos (ex.: Cruzeiro x Araxá, ogol 1968-08-04); fica a do ogol

### 1969

- tabela publicada x jogos — Segunda fase / -: Tupi tabela [14, 5, 4, 5, 21, 14] jogos [15, 6, 4, 5, 23, 15] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Democrata-GV tabela [14, 4, 4, 6, 13, 18] jogos [15, 4, 4, 7, 14, 20] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Tupi tabela [14, 5, 4, 5, 21, 14] jogos [15, 6, 4, 5, 23, 15] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Democrata-GV tabela [14, 4, 4, 6, 13, 18] jogos [15, 4, 4, 7, 14, 20] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Democrata-GV tabela [30, 8, 5, 17, 33, 42] jogos [30, 9, 6, 15, 33, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Independente-MG x América-MG, ogol 1969-04-02); fica a do ogol

### 1970

- tabela publicada x jogos — Fase classificatória / Grupo B: Sport-MG tabela [14, 6, 3, 5, 20, 22] jogos [14, 5, 4, 5, 18, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo B: Tupynambás tabela [14, 2, 1, 11, 7, 23] jogos [14, 2, 2, 10, 7, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Valeriodoce tabela [22, 9, 4, 9, 28, 24] jogos [22, 9, 4, 9, 29, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Uberaba tabela [22, 6, 5, 11, 20, 33] jogos [22, 6, 5, 11, 20, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Valeriodoce tabela [36, 19, 6, 11, 60, 35] jogos [36, 19, 6, 11, 61, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Sport-MG tabela [36, 14, 8, 14, 37, 49] jogos [36, 13, 9, 14, 35, 49] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Uberaba tabela [36, 11, 10, 15, 44, 51] jogos [36, 11, 10, 15, 44, 52] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Tupynambás tabela [14, 2, 1, 11, 7, 23] jogos [14, 2, 2, 10, 7, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Villa Nova-MG 0-3 Atlético-MG, ogol Atlético-MG 3-0 Villa Nova-MG (1970-07-11); fica a RSSSF
- mando invertido no ogol — RSSSF Sport-MG 1-0 Atlético-MG, ogol Atlético-MG 0-1 Sport-MG (1970-07-15); fica a RSSSF
- mando invertido no ogol — RSSSF Atl. Três Corações 0-2 Atlético-MG, ogol Atlético-MG 2-0 Atl. Três Corações (1970-07-22); fica a RSSSF
- mando invertido no ogol — RSSSF Valeriodoce 0-2 Atlético-MG, ogol Atlético-MG 2-0 Valeriodoce (1970-08-05); fica a RSSSF
- mando invertido no ogol — RSSSF Uberlândia 0-1 Atlético-MG, ogol Atlético-MG 1-0 Uberlândia (1970-08-09); fica a RSSSF
- mando invertido no ogol — RSSSF Flamengo FC-MG 1-3 Atlético-MG, ogol Atlético-MG 3-1 Flamengo FC-MG (1970-08-16); fica a RSSSF
- mando invertido no ogol — RSSSF Tupi 1-3 Atlético-MG, ogol Atlético-MG 3-1 Tupi (1970-09-16); fica a RSSSF

### 1971

- tabela publicada x jogos — Primeira fase / -: América-MG tabela [22, 16, 6, 0, 39, 16] jogos [22, 16, 6, 0, 38, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [22, 16, 4, 2, 44, 10] jogos [22, 16, 4, 2, 45, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [22, 6, 9, 7, 29, 31] jogos [22, 6, 9, 7, 30, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [22, 7, 6, 9, 15, 23] jogos [22, 7, 6, 9, 16, 23] — placar diverge entre RSSSF e ogol em Uberaba x Atl. Três Corações (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Atl. Três Corações tabela [22, 4, 10, 8, 20, 28] jogos [22, 4, 10, 8, 20, 29] — placar diverge entre RSSSF e ogol em Uberaba x Atl. Três Corações (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [22, 16, 6, 0, 39, 16] jogos [22, 16, 6, 0, 38, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [22, 16, 4, 2, 44, 10] jogos [22, 16, 4, 2, 45, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [22, 6, 9, 7, 29, 31] jogos [22, 6, 9, 7, 30, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [22, 7, 6, 9, 15, 23] jogos [22, 7, 6, 9, 16, 23] — placar diverge entre RSSSF e ogol em Uberaba x Atl. Três Corações (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Atl. Três Corações tabela [22, 4, 10, 8, 20, 28] jogos [22, 4, 10, 8, 20, 29] — placar diverge entre RSSSF e ogol em Uberaba x Atl. Três Corações (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de América-MG x Cruzeiro na LEAGUE sempre na mesma ordem) — ogol Cruzeiro 1-1 América-MG (1971-04-18)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de América-MG x Atlético-MG na LEAGUE sempre na mesma ordem) — ogol Atlético-MG 0-1 América-MG (1971-05-23)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Cruzeiro na LEAGUE sempre na mesma ordem) — ogol Cruzeiro 0-1 Atlético-MG (1971-06-27)
- placar diferente no ogol — Uberaba x Atl. Três Corações (1971-03-17): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- adversário diferente no ogol — RSSSF Atlético-MG 2-1 Nacional Atl. Muriaé, ogol Atl. Três Corações 2-1 Nacional Atl. Muriaé (1971-03-10); fica a RSSSF

### 1972

- tabela publicada x jogos — Fase classificatória / Grupo B: Atl. Três Corações tabela [6, 3, 2, 1, 5, 3] jogos [6, 2, 3, 1, 5, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo B: Flamengo FC-MG tabela [6, 2, 0, 4, 5, 5] jogos [6, 2, 1, 3, 5, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo B: Atl. Três Corações tabela [6, 3, 2, 1, 5, 3] jogos [6, 2, 3, 1, 5, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo B: Flamengo FC-MG tabela [6, 2, 0, 4, 5, 5] jogos [6, 2, 1, 3, 5, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Democrata-SL tabela [6, 5, 0, 1, 8, 2] jogos [6, 5, 0, 1, 9, 2] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Cassimiro de Abreu tabela [6, 2, 1, 3, 8, 5] jogos [6, 2, 1, 3, 11, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Formiga tabela [6, 0, 0, 6, 1, 16] jogos [6, 0, 0, 6, 1, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Democrata-SL tabela [6, 5, 0, 1, 8, 2] jogos [6, 5, 0, 1, 9, 2] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Cassimiro de Abreu tabela [6, 2, 1, 3, 8, 5] jogos [6, 2, 1, 3, 11, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase classificatória / Grupo C: Formiga tabela [6, 0, 0, 6, 1, 16] jogos [6, 0, 0, 6, 1, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo B: Atlético-MG tabela [8, 4, 2, 2, 7, 7] jogos [8, 5, 1, 2, 17, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo B: Atlético-MG tabela [8, 4, 2, 2, 7, 7] jogos [8, 5, 1, 2, 17, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Cruzeiro tabela [25, 13, 11, 1, 36, 9] jogos [25, 14, 10, 1, 36, 8] — placar diverge entre RSSSF e ogol em Atl. Três Corações x Cruzeiro (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Atlético-MG tabela [24, 6, 9, 9, 19, 26] jogos [25, 13, 9, 3, 44, 18] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: América-MG tabela [24, 10, 8, 6, 28, 22] jogos [24, 10, 8, 6, 28, 21] — placar diverge entre RSSSF e ogol em América-MG x Nacional Uberaba (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Caldense tabela [18, 7, 5, 6, 23, 18] jogos [29, 12, 9, 8, 37, 27] — a tabela conta 18 jogos e as fontes trazem 29
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Nacional Uberaba tabela [18, 4, 4, 10, 19, 36] jogos [29, 9, 7, 13, 33, 47] — a tabela conta 18 jogos e as fontes trazem 29
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Fluminense-MG tabela [10, 3, 2, 5, 8, 18] jogos [18, 7, 5, 6, 19, 26] — a tabela conta 10 jogos e as fontes trazem 18
- tabela publicada x jogos — Campeonato Mineiro 1972 - Final Match - September 7, 1972 / -: Democrata-SL tabela [10, 0, 1, 9, 4, 22] jogos [16, 5, 1, 10, 13, 24] — a tabela conta 10 jogos e as fontes trazem 16
- mando invertido no ogol — RSSSF Villa Nova-MG 0-1 Cruzeiro, ogol Cruzeiro 1-0 Villa Nova-MG (1972-05-06); fica a RSSSF
- mando invertido no ogol — RSSSF Cruzeiro 1-1 Atlético-MG, ogol Atlético-MG 1-1 Cruzeiro (1972-05-21); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 0-2 Cruzeiro, ogol Cruzeiro 2-0 América-MG (1972-07-23); fica a RSSSF
- mando invertido no ogol — RSSSF Atlético-MG 0-1 Cruzeiro, ogol Cruzeiro 1-0 Atlético-MG (1972-08-06); fica a RSSSF
- mando invertido no ogol — RSSSF Atl. Três Corações 0-1 Atlético-MG, ogol Atlético-MG 1-0 Atl. Três Corações (1972-08-30); fica a RSSSF
- placar diferente no ogol — Atl. Três Corações x Cruzeiro (1972-03-30): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — América-MG x Nacional Uberaba (1972-05-21): RSSSF 4-0, ogol 4-1; fica o da RSSSF
- mando invertido no ogol — RSSSF Uberaba 1-1 Nacional Uberaba, ogol Nacional Uberaba 1-1 Uberaba (1972-03-05); fica a RSSSF

### 1973

- tabela publicada x jogos — Segunda fase / Grupo A: Atlético-MG tabela [8, 4, 3, 1, 8, 6] jogos [8, 2, 4, 2, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo A: Atlético-MG tabela [8, 4, 3, 1, 8, 6] jogos [8, 2, 4, 2, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Uberaba 1-3 Atlético-MG, ogol Atlético-MG 3-1 Uberaba (1973-07-22); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 30 jogos (ex.: Araguari x União Tijucana, ogol 1972-10-29); fica a do ogol

### 1974

- tabela publicada x jogos — Primeira fase / Grupo A: Caldense tabela [6, 4, 1, 1, 9, 3] jogos [6, 4, 1, 1, 10, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Nacional Uberaba tabela [6, 0, 2, 4, 1, 8] jogos [6, 0, 2, 4, 1, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Caldense tabela [6, 4, 1, 1, 9, 3] jogos [6, 4, 1, 1, 10, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Nacional Uberaba tabela [6, 0, 2, 4, 1, 8] jogos [6, 0, 2, 4, 1, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 0, 3, 3, 2, 11] jogos [27, 20, 3, 4, 58, 15] — a tabela conta 6 jogos e as fontes trazem 27
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): S.Setembro
- S.Setembro — clube que o ogol não tem; entra só pela RSSSF
- mando invertido no ogol — RSSSF Atlético-MG 1-0 Sete de Setembro-MG, ogol Sete de Setembro-MG 0-1 Atlético-MG (1974-08-31); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 30 jogos (ex.: Uberaba x Cruzeiro, ogol 1974-08-21); fica a do ogol

### 1975

- tabela publicada x jogos — 1º Turno / Grupo A: Cruzeiro tabela [8, 5, 3, 0, 13, 6] jogos [8, 4, 4, 0, 14, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Nacional Atl. Muriaé tabela [8, 2, 2, 4, 6, 10] jogos [8, 3, 2, 3, 7, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Sete de Setembro-MG tabela [8, 1, 3, 4, 6, 11] jogos [8, 1, 4, 3, 6, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Democrata-GV tabela [8, 1, 1, 6, 2, 16] jogos [8, 1, 1, 6, 4, 19] — placar diverge entre RSSSF e ogol em Caldense x Democrata-GV (4-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / Grupo B: América-MG tabela [8, 6, 0, 2, 19, 10] jogos [8, 5, 0, 3, 18, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Atlético-MG tabela [8, 4, 2, 2, 15, 5] jogos [8, 4, 3, 1, 17, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Caldense tabela [8, 4, 2, 2, 9, 5] jogos [8, 5, 2, 1, 13, 4] — placar diverge entre RSSSF e ogol em Caldense x Democrata-GV (4-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / Grupo B: Valeriodoce tabela [8, 3, 2, 3, 8, 4] jogos [8, 3, 2, 3, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Uberlândia tabela [8, 3, 2, 3, 2, 13] jogos [8, 2, 3, 3, 9, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Esportiva Guaxupé tabela [8, 1, 5, 2, 8, 8] jogos [8, 1, 5, 2, 6, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Nacional Uberaba tabela [8, 1, 0, 7, 3, 8] jogos [8, 1, 0, 7, 5, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Cruzeiro tabela [8, 5, 3, 0, 13, 6] jogos [8, 4, 4, 0, 14, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Nacional Atl. Muriaé tabela [8, 2, 2, 4, 6, 10] jogos [8, 3, 2, 3, 7, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Sete de Setembro-MG tabela [8, 1, 3, 4, 6, 11] jogos [8, 1, 4, 3, 6, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo A: Democrata-GV tabela [8, 1, 1, 6, 2, 16] jogos [8, 1, 1, 6, 4, 19] — placar diverge entre RSSSF e ogol em Caldense x Democrata-GV (4-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / Grupo B: América-MG tabela [8, 6, 0, 2, 19, 10] jogos [8, 5, 0, 3, 18, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Atlético-MG tabela [8, 4, 2, 2, 15, 5] jogos [8, 4, 3, 1, 17, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Caldense tabela [8, 4, 2, 2, 9, 5] jogos [8, 5, 2, 1, 13, 4] — placar diverge entre RSSSF e ogol em Caldense x Democrata-GV (4-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / Grupo B: Valeriodoce tabela [8, 3, 2, 3, 8, 4] jogos [8, 3, 2, 3, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Uberlândia tabela [8, 3, 2, 3, 2, 13] jogos [8, 2, 3, 3, 9, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Esportiva Guaxupé tabela [8, 1, 5, 2, 8, 8] jogos [8, 1, 5, 2, 6, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / Grupo B: Nacional Uberaba tabela [8, 1, 0, 7, 3, 8] jogos [8, 1, 0, 7, 5, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo B: Cruzeiro tabela [7, 4, 1, 2, 9, 5] jogos [7, 4, 1, 2, 7, 2] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo B: Cruzeiro tabela [7, 4, 1, 2, 9, 5] jogos [7, 4, 1, 2, 7, 2] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Caldense tabela [6, 1, 0, 5, 3, 9] jogos [6, 1, 0, 5, 4, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Caldense tabela [6, 1, 0, 5, 3, 9] jogos [6, 1, 0, 5, 4, 11] — há jogo do clube sem conferência no ogol
- mando invertido no ogol — RSSSF Caldense 0-1 Atlético-MG, ogol Atlético-MG 1-0 Caldense (1976-02-04); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 23 jogos (ex.: Fluminense-MG x Caldense, ogol 1975-04-20); fica a do ogol

### 1976

- Torneios Paralelos I, II e III: consolação para os 11 clubes que não foram à Taça Governador do Estado; ficam fora (rsssf_mg1.ANOS_A_PARTE), como os torneios à parte do Carioca
- tabela publicada x jogos — 1º Turno / -: Atlético-MG tabela [10, 10, 0, 0, 42, 2] jogos [10, 10, 0, 0, 42, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Sete de Setembro-MG tabela [10, 1, 2, 7, 4, 22] jogos [10, 1, 3, 6, 5, 22] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Sport-MG tabela [10, 1, 2, 7, 2, 20] jogos [10, 0, 3, 7, 2, 21] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Atlético-MG tabela [10, 10, 0, 0, 42, 2] jogos [10, 10, 0, 0, 42, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Sete de Setembro-MG tabela [10, 1, 2, 7, 4, 22] jogos [10, 1, 3, 6, 5, 22] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Sport-MG tabela [10, 1, 2, 7, 2, 20] jogos [10, 0, 3, 7, 2, 21] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno - Final / -: Atlético-MG tabela [10, 10, 0, 0, 42, 2] jogos [10, 10, 0, 0, 42, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Final / -: Sete de Setembro-MG tabela [10, 1, 2, 7, 4, 22] jogos [10, 1, 3, 6, 5, 22] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno - Final / -: Sport-MG tabela [10, 1, 2, 7, 2, 20] jogos [10, 0, 3, 7, 2, 21] — placar diverge entre RSSSF e ogol em Sport-MG x Sete de Setembro-MG (1-1 x 0-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / Grupo A: Caldense tabela [7, 2, 3, 2, 5, 8] jogos [7, 1, 4, 2, 4, 8] — placar diverge entre RSSSF e ogol em Caldense x ESAB (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / Grupo A: Villa Nova-MG tabela [7, 1, 3, 3, 8, 10] jogos [7, 2, 2, 3, 10, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo A: Uberaba tabela [7, 1, 2, 4, 8, 11] jogos [7, 2, 2, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo B: ESAB tabela [7, 1, 3, 3, 3, 7] jogos [7, 1, 4, 2, 3, 6] — placar diverge entre RSSSF e ogol em Caldense x ESAB (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / Grupo B: Esportiva Guaxupé tabela [7, 0, 2, 5, 2, 12] jogos [7, 0, 1, 6, 2, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo A: Caldense tabela [7, 2, 3, 2, 5, 8] jogos [7, 1, 4, 2, 4, 8] — placar diverge entre RSSSF e ogol em Caldense x ESAB (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / Grupo A: Uberaba tabela [7, 1, 2, 4, 8, 11] jogos [7, 2, 2, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo B: ESAB tabela [7, 1, 3, 3, 3, 7] jogos [7, 1, 4, 2, 3, 6] — placar diverge entre RSSSF e ogol em Caldense x ESAB (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Villa Nova-MG 0-2 Atlético-MG, ogol Atlético-MG 2-0 Villa Nova-MG (1976-03-25); fica a RSSSF
- placar diferente no ogol — Sport-MG x Sete de Setembro-MG (1976-03-07): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Caldense x ESAB (1976-06-30): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 75 jogos (ex.: América-MG x Democrata-GV, ogol 1976-03-07); fica a do ogol
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 1-0 Sport-MG (1976-05-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 1-0 Democrata-GV (1976-05-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: União Tijucana 4-1 Araguari (1976-05-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Arsenal-MG 2-1 URT (1976-05-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Fluminense-MG 1-0 13 De Maio (1976-05-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 4-0 Democrata-GV (1976-05-12)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sport-MG 2-0 Sete de Setembro-MG (1976-05-12)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: 13 De Maio 1-0 União Tijucana (1976-05-12)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Fluminense-MG 1-1 Arsenal-MG (1976-05-12)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 3-2 Araguari (1976-05-12)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sete de Setembro-MG 0-1 Guarani-MG (1976-05-15)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: 13 De Maio 1-0 URT (1976-05-15)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 1-0 Sport-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: União Tijucana 1-1 Fluminense-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Araguari 3-0 Arsenal-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 2-0 Sete de Setembro-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sport-MG 2-1 Democrata-GV (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Arsenal-MG 0-0 União Tijucana (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Araguari 1-0 13 De Maio (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 1-0 Fluminense-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 1-0 Tupi (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sete de Setembro-MG 2-1 Democrata-GV (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: União Tijucana 1-0 URT (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Araguari 1-1 Fluminense-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Arsenal-MG 1-0 13 De Maio (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 4-1 Sport-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 2-0 Democrata-GV (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 3-0 Arsenal-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Araguari 2-1 União Tijucana (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: 13 De Maio 1-0 Fluminense-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 0-2 Guarani-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sete de Setembro-MG 1-0 Sport-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: União Tijucana 0-0 13 De Maio (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Arsenal-MG 1-0 Fluminense-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Araguari 0-0 URT (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 1-0 Sport-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 3-0 Sete de Setembro-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Fluminense-MG 3-0 União Tijucana (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Arsenal-MG 1-1 Araguari (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 1-0 13 De Maio (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sete de Setembro-MG 3-2 Tupi (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Sport-MG 1-1 Democrata-GV (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: União Tijucana 2-0 Arsenal-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: 13 De Maio 2-1 Araguari (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Fluminense-MG 1-0 URT (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 1-0 União Tijucana (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Fluminense-MG 1-0 Araguari (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: 13 De Maio 0-0 Arsenal-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 3-0 Sete de Setembro-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tupi 0-2 Guarani-MG (1976-05-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 3-0 Nacional Uberaba (1976-06-06)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Atl. Muriaé 0-1 Valeriodoce (1976-06-06)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Valeriodoce 1-1 Uberlândia (1976-06-10)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Uberaba 1-1 Nacional Atl. Muriaé (1976-06-10)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 2-0 Nacional Atl. Muriaé (1976-06-13)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Valeriodoce 1-1 Nacional Uberaba (1976-06-13)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Valeriodoce 2-0 Nacional Atl. Muriaé (1976-06-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Uberaba 2-3 Uberlândia (1976-06-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 4-0 Valeriodoce (1976-06-20)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Atl. Muriaé 2-1 Nacional Uberaba (1976-06-20)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Atl. Muriaé 4-2 Uberlândia (1976-06-27)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Nacional Uberaba 2-0 Valeriodoce (1976-06-27)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 0-0 Uberlândia (1976-06-30)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Guarani-MG 5-1 URT (1976-07-02)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 4-2 URT (1976-07-04)
- só na RSSSF (não achado no ogol): Cruzeiro None-None Guarani-MG (1976-07-25)
- só na RSSSF (não achado no ogol): Atlético-MG None-None Caldense (1976-07-25)
- só na RSSSF (não achado no ogol): América-MG None-None Uberlândia (1976-07-25)

### 1977

- tabela publicada x jogos — Segunda fase / -: Cruzeiro tabela [11, 8, 2, 1, 18, 7] jogos [11, 8, 2, 1, 18, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: América-MG tabela [11, 7, 2, 2, 17, 5] jogos [11, 7, 2, 2, 13, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Uberlândia tabela [11, 2, 5, 4, 7, 9] jogos [11, 2, 5, 4, 6, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Cruzeiro tabela [11, 8, 2, 1, 18, 7] jogos [11, 8, 2, 1, 18, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: América-MG tabela [11, 7, 2, 2, 17, 5] jogos [11, 7, 2, 2, 13, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Uberlândia tabela [11, 2, 5, 4, 7, 9] jogos [11, 2, 5, 4, 6, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo anulado ou cancelado fica de fora: Villa Nova 1-5 Atlético (1977-06-04) [Match annuled by TJD and rescheduled for July 31]
- mando invertido no ogol — RSSSF Atlético-MG 4-1 América-MG, ogol América-MG 1-4 Atlético-MG (1977-05-15); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 0-2 Atlético-MG, ogol Atlético-MG 2-0 América-MG (1977-07-17); fica a RSSSF
- mando invertido no ogol — RSSSF Cruzeiro 0-0 Atlético-MG, ogol Atlético-MG 0-0 Cruzeiro (1977-08-07); fica a RSSSF

### 1978

- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [11, 7, 2, 2, 26, 6] jogos [11, 7, 2, 2, 22, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [11, 7, 2, 2, 26, 6] jogos [11, 7, 2, 2, 22, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [11, 8, 2, 1, 11, 3] jogos [11, 8, 2, 1, 15, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [11, 8, 2, 1, 11, 3] jogos [11, 8, 2, 1, 15, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1979

- tabela publicada x jogos — Primeira fase / -: Nacional Atl. Muriaé tabela [15, 5, 5, 5, 15, 12] jogos [15, 5, 5, 5, 14, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Nacional Atl. Muriaé tabela [15, 5, 5, 5, 15, 12] jogos [15, 5, 5, 5, 14, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Cruzeiro tabela [16, 11, 2, 3, 32, 7] jogos [15, 10, 2, 3, 31, 11] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [16, 11, 0, 5, 34, 6] jogos [15, 11, 0, 4, 34, 8] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Valeriodoce tabela [15, 9, 2, 4, 19, 14] jogos [15, 9, 2, 4, 19, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: América-MG tabela [15, 8, 3, 4, 32, 9] jogos [15, 8, 3, 4, 32, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Uberlândia tabela [15, 7, 5, 3, 23, 26] jogos [15, 7, 5, 3, 23, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Uberaba tabela [15, 7, 5, 3, 18, 13] jogos [15, 7, 5, 3, 18, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Guarani-MG tabela [15, 7, 5, 3, 19, 19] jogos [15, 7, 5, 3, 18, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Nacional Atl. Muriaé tabela [15, 7, 4, 4, 16, 12] jogos [15, 7, 4, 4, 16, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Villa Nova-MG tabela [15, 6, 5, 4, 13, 19] jogos [15, 6, 5, 4, 13, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Caldense tabela [15, 4, 6, 5, 17, 18] jogos [15, 4, 6, 5, 17, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Araxá tabela [15, 4, 3, 8, 15, 14] jogos [15, 4, 3, 8, 15, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Nacional Uberaba tabela [15, 3, 4, 8, 19, 22] jogos [15, 3, 4, 8, 19, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Esportiva Guaxupé tabela [15, 3, 3, 9, 11, 17] jogos [15, 3, 3, 9, 11, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Ateneu tabela [15, 2, 5, 8, 6, 37] jogos [15, 2, 5, 8, 6, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Democrata-GV tabela [15, 1, 7, 7, 9, 30] jogos [15, 1, 7, 7, 9, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Araguari tabela [15, 0, 3, 12, 6, 33] jogos [15, 0, 3, 12, 6, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase - Desempate / -: Cruzeiro tabela [16, 11, 2, 3, 32, 7] jogos [3, 1, 1, 1, 2, 2] — a tabela conta 16 jogos e as fontes trazem 3
- tabela publicada x jogos — Segunda fase - Desempate / -: Atlético-MG tabela [16, 11, 0, 5, 34, 6] jogos [3, 1, 1, 1, 2, 2] — a tabela conta 16 jogos e as fontes trazem 3
- tabela publicada x jogos — Segunda fase - Desempate / -: Valeriodoce tabela [15, 9, 2, 4, 19, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: América-MG tabela [15, 8, 3, 4, 32, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Uberlândia tabela [15, 7, 5, 3, 23, 26] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Uberaba tabela [15, 7, 5, 3, 18, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Guarani-MG tabela [15, 7, 5, 3, 19, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Nacional Atl. Muriaé tabela [15, 7, 4, 4, 16, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Villa Nova-MG tabela [15, 6, 5, 4, 13, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Caldense tabela [15, 4, 6, 5, 17, 18] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Araxá tabela [15, 4, 3, 8, 15, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Nacional Uberaba tabela [15, 3, 4, 8, 19, 22] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Esportiva Guaxupé tabela [15, 3, 3, 9, 11, 17] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Ateneu tabela [15, 2, 5, 8, 6, 37] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Democrata-GV tabela [15, 1, 7, 7, 9, 30] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase - Desempate / -: Araguari tabela [15, 0, 3, 12, 6, 33] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Overall Staing of 1st Phase / -: Atlético-MG tabela [33, 22, 6, 5, 63, 18] jogos [33, 22, 6, 5, 63, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Overall Staing of 1st Phase / -: Guarani-MG tabela [30, 13, 7, 10, 36, 32] jogos [30, 13, 7, 10, 35, 33] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall Staing of 1st Phase / -: Nacional Atl. Muriaé tabela [30, 12, 9, 9, 32, 25] jogos [30, 12, 9, 9, 30, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall Staing of 1st Phase / -: Nacional Uberaba tabela [30, 7, 9, 14, 34, 50] jogos [30, 7, 9, 14, 34, 49] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall Staing of 1st Phase / -: Ateneu tabela [30, 4, 9, 17, 20, 51] jogos [30, 4, 9, 17, 19, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: América-MG tabela [10, 4, 3, 3, 9, 10] jogos [10, 2, 4, 4, 4, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Uberlândia tabela [10, 2, 4, 4, 4, 8] jogos [10, 4, 3, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: América-MG tabela [10, 4, 3, 3, 9, 10] jogos [10, 2, 4, 4, 4, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Uberlândia tabela [10, 2, 4, 4, 4, 8] jogos [10, 4, 3, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Cruzeiro 1-0 Atlético-MG, ogol Atlético-MG 0-1 Cruzeiro (1979-07-22); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Cruzeiro x Atlético-MG na Segunda fase - Desempate sempre na mesma ordem) — ogol Atlético-MG 1-1 Cruzeiro (1979-08-01)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x Cruzeiro na Segunda fase - Desempate sempre na mesma ordem) — ogol Cruzeiro 0-1 Atlético-MG (1979-08-05)

### 1980

- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 2, 2, 2, 6, 9] jogos [20, 18, 1, 1, 55, 8] — a tabela conta 6 jogos e as fontes trazem 20

### 1981

- mando invertido no ogol — RSSSF Villa Nova-MG 1-2 Atlético-MG, ogol Atlético-MG 2-1 Villa Nova-MG (1981-09-19); fica a RSSSF
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Atlético-MG x América-MG na FINAL PHASE sempre na mesma ordem) — ogol América-MG 0-1 Atlético-MG (1981-11-22)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 24 jogos (ex.: Villa Nova-MG x Guarani-MG, ogol 1981-06-21); fica a do ogol

### 1982

- tabela publicada x jogos — Primeira fase / -: Uberlândia tabela [22, 12, 7, 3, 26, 12] jogos [22, 12, 7, 3, 27, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [22, 6, 5, 11, 18, 27] jogos [22, 6, 4, 12, 17, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Uberlândia tabela [22, 12, 7, 3, 26, 12] jogos [22, 12, 7, 3, 27, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [22, 6, 5, 11, 18, 27] jogos [22, 6, 4, 12, 17, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- 3 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Fluminense 2-1 Caldense (20/02/1983); Caldense None-None Fluminense (25/02/1983); Caldense 0-0 Fluminense (27/02/1983)
- jogo do ogol tirado junto com o da RSSSF: Fluminense-MG 2-1 Caldense (1983-02-20)
- jogo do ogol tirado junto com o da RSSSF: Caldense 0-0 Fluminense-MG (1983-02-27)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 20 jogos (ex.: Villa Nova-MG x Cruzeiro, ogol 1982-10-21); fica a do ogol

### 1983

- tabela publicada x jogos — 1º Turno / -: Uberaba tabela [11, 5, 3, 3, 15, 14] jogos [12, 6, 3, 3, 17, 14] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 1º Turno / -: Nacional Uberaba tabela [11, 4, 2, 5, 15, 12] jogos [12, 4, 2, 6, 15, 14] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Uberlândia tabela [11, 4, 5, 2, 10, 7] jogos [11, 4, 4, 3, 10, 8] — placar diverge entre RSSSF e ogol em Guarani-MG x Uberlândia (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Valeriodoce tabela [11, 5, 2, 4, 14, 13] jogos [11, 5, 2, 4, 14, 14] — placar diverge entre RSSSF e ogol em Valeriodoce x Democrata-GV (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Democrata-GV tabela [11, 3, 2, 6, 10, 20] jogos [11, 3, 2, 6, 11, 20] — placar diverge entre RSSSF e ogol em Valeriodoce x Democrata-GV (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Guarani-MG tabela [11, 0, 6, 5, 4, 12] jogos [11, 1, 5, 5, 5, 12] — placar diverge entre RSSSF e ogol em Guarani-MG x Uberlândia (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Uberlândia tabela [11, 4, 5, 2, 10, 7] jogos [11, 4, 4, 3, 10, 8] — placar diverge entre RSSSF e ogol em Guarani-MG x Uberlândia (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Valeriodoce tabela [11, 5, 2, 4, 14, 13] jogos [11, 5, 2, 4, 14, 14] — placar diverge entre RSSSF e ogol em Valeriodoce x Democrata-GV (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Democrata-GV tabela [11, 3, 2, 6, 10, 20] jogos [11, 3, 2, 6, 11, 20] — placar diverge entre RSSSF e ogol em Valeriodoce x Democrata-GV (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Guarani-MG tabela [11, 0, 6, 5, 4, 12] jogos [11, 1, 5, 5, 5, 12] — placar diverge entre RSSSF e ogol em Guarani-MG x Uberlândia (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase - Final / -: Cruzeiro tabela [22, 11, 10, 1, 31, 8] jogos [2, 0, 0, 2, 0, 6] — a tabela conta 22 jogos e as fontes trazem 2
- tabela publicada x jogos — Primeira fase - Final / -: América-MG tabela [22, 11, 6, 5, 28, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase - Final / -: Uberlândia tabela [22, 9, 8, 5, 24, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase - Final / -: Valeriodoce tabela [22, 8, 7, 7, 25, 25] jogos [22, 8, 7, 7, 25, 26] — placar diverge entre RSSSF e ogol em Valeriodoce x Uberlândia (0-2 x 0-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase - Final / -: Guarani-MG tabela [22, 2, 10, 10, 12, 32] jogos [22, 3, 9, 10, 13, 32] — placar diverge entre RSSSF e ogol em Guarani-MG x Uberlândia (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase - Final / -: Democrata-GV tabela [22, 4, 6, 12, 15, 34] jogos [22, 4, 6, 12, 16, 34] — placar diverge entre RSSSF e ogol em Valeriodoce x Democrata-GV (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Nacional Uberaba tabela [14, 4, 1, 9, 16, 32] jogos [14, 4, 1, 9, 15, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Valeriodoce tabela [14, 4, 1, 9, 15, 28] jogos [14, 4, 1, 9, 16, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Nacional Uberaba tabela [14, 4, 1, 9, 16, 32] jogos [14, 4, 1, 9, 15, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Valeriodoce tabela [14, 4, 1, 9, 15, 28] jogos [14, 4, 1, 9, 16, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- 3 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Alfenese 1-2 Democrata-GV (04/12/1983); Democrata-GV 1-1 Alfenense (08/12/1983); Democrata-GV 4-2 Alfenense (11/12/1983)
- placar diferente no ogol — Uberaba x Nacional Uberaba (1983-11-27): RSSSF 2-0, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Valeriodoce x Uberlândia (1983-07-03): RSSSF 0-2, ogol 0-3; fica o da RSSSF
- placar diferente no ogol — Nacional Uberaba x Valeriodoce (1983-07-30): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Guarani-MG x Uberlândia (1983-08-18): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — América-MG x Villa Nova-MG (1983-09-10): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Valeriodoce x Democrata-GV (1983-09-21): RSSSF 4-0, ogol 4-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: América-MG x Democrata-SL, ogol 1983-06-02); fica a do ogol
- jogo só no ogol, incluído em 1º Turno: Uberaba 2-0 Nacional Uberaba (1983-06-02)
- só na RSSSF (não achado no ogol): Uberaba 1-2 Nacional Uberaba (1983-11-27)

### 1984

- tabela publicada x jogos — 2º Turno / -: Nacional Uberaba tabela [13, 2, 7, 4, 4, 7] jogos [13, 2, 7, 4, 7, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Nacional Uberaba tabela [13, 2, 7, 4, 4, 7] jogos [13, 2, 7, 4, 7, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Cruzeiro 2-1 América-MG, ogol América-MG 1-2 Cruzeiro (1984-09-19); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 1-2 Cruzeiro, ogol Cruzeiro 2-1 América-MG (1984-09-23); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 0-1 Atlético-MG, ogol Atlético-MG 1-0 América-MG (1984-10-21); fica a RSSSF
- mando invertido no ogol — RSSSF Cruzeiro 4-0 Atlético-MG, ogol Atlético-MG 0-4 Cruzeiro (1984-12-05); fica a RSSSF
- mando invertido no ogol — RSSSF Atlético-MG 1-0 Cruzeiro, ogol Cruzeiro 0-1 Atlético-MG (1984-12-09); fica a RSSSF
- placar diferente no ogol — Uberlândia x Uberaba (1984-06-03): RSSSF 2-0, ogol 2-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Democrata-GV x Uberaba, ogol 1984-08-01); fica a do ogol

### 1985

- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [13, 10, 2, 1, 26, 7] jogos [26, 16, 8, 2, 46, 13] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [13, 7, 3, 3, 15, 6] jogos [28, 10, 13, 5, 25, 18] — a tabela conta 13 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [13, 6, 5, 2, 19, 10] jogos [27, 13, 12, 2, 38, 17] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [13, 6, 3, 4, 14, 9] jogos [27, 9, 11, 7, 22, 20] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [13, 5, 5, 3, 17, 14] jogos [26, 9, 11, 6, 31, 27] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [13, 5, 5, 3, 9, 10] jogos [26, 7, 12, 7, 15, 18] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Nacional Uberaba tabela [13, 5, 3, 5, 11, 13] jogos [26, 6, 7, 13, 15, 31] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Uberlândia tabela [13, 4, 4, 5, 13, 15] jogos [26, 8, 11, 7, 25, 24] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: XV Uber tabela [13, 4, 3, 6, 11, 16] jogos [26, 6, 7, 13, 23, 34] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [13, 3, 5, 5, 6, 12] jogos [26, 6, 11, 9, 16, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Fabril tabela [13, 4, 2, 7, 7, 13] jogos [26, 6, 9, 11, 19, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Valeriodoce tabela [13, 2, 6, 5, 8, 15] jogos [26, 7, 12, 7, 22, 22] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Guarani-MG tabela [13, 3, 1, 9, 5, 14] jogos [26, 5, 9, 12, 12, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Villa Nova-MG tabela [13, 1, 5, 7, 3, 10] jogos [26, 4, 11, 11, 14, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase final / -: Cruzeiro tabela [6, 2, 4, 0, 5, 3] jogos [12, 3, 8, 1, 12, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 2, 3, 1, 7, 4] jogos [12, 5, 6, 1, 14, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Cruzeiro tabela [6, 2, 4, 0, 5, 3] jogos [12, 3, 8, 1, 12, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 2, 3, 1, 7, 4] jogos [12, 5, 6, 1, 14, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [13, 7, 6, 0, 19, 7] jogos [27, 13, 12, 2, 38, 17] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [13, 6, 6, 1, 20, 6] jogos [26, 16, 8, 2, 46, 13] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Valeriodoce tabela [13, 5, 6, 2, 14, 7] jogos [26, 7, 12, 7, 22, 22] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Uberlândia tabela [13, 4, 7, 2, 12, 9] jogos [26, 8, 11, 7, 25, 24] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [13, 4, 6, 3, 14, 13] jogos [26, 9, 11, 6, 31, 27] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [13, 3, 8, 2, 10, 12] jogos [28, 10, 13, 5, 25, 18] — a tabela conta 13 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [13, 3, 7, 3, 8, 11] jogos [27, 9, 11, 7, 22, 20] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [13, 3, 6, 4, 10, 11] jogos [26, 6, 11, 9, 16, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Villa Nova-MG tabela [13, 3, 6, 4, 11, 13] jogos [26, 4, 11, 11, 14, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Guarani-MG tabela [13, 2, 8, 3, 7, 9] jogos [26, 5, 9, 12, 12, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [13, 2, 7, 4, 6, 8] jogos [26, 7, 12, 7, 15, 18] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Fabril tabela [13, 2, 7, 4, 12, 17] jogos [26, 6, 9, 11, 19, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: XV Uber tabela [13, 2, 4, 7, 12, 18] jogos [26, 6, 7, 13, 23, 34] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Nacional Uberaba tabela [13, 1, 4, 8, 4, 18] jogos [26, 6, 7, 13, 15, 31] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [13, 7, 6, 0, 19, 7] jogos [27, 13, 12, 2, 38, 17] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Atlético-MG tabela [13, 6, 6, 1, 20, 6] jogos [26, 16, 8, 2, 46, 13] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Valeriodoce tabela [13, 5, 6, 2, 14, 7] jogos [26, 7, 12, 7, 22, 22] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Uberlândia tabela [13, 4, 7, 2, 12, 9] jogos [26, 8, 11, 7, 25, 24] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [13, 4, 6, 3, 14, 13] jogos [26, 9, 11, 6, 31, 27] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [13, 3, 8, 2, 10, 12] jogos [28, 10, 13, 5, 25, 18] — a tabela conta 13 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [13, 3, 7, 3, 8, 11] jogos [27, 9, 11, 7, 22, 20] — a tabela conta 13 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [13, 3, 6, 4, 10, 11] jogos [26, 6, 11, 9, 16, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Villa Nova-MG tabela [13, 3, 6, 4, 11, 13] jogos [26, 4, 11, 11, 14, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Guarani-MG tabela [13, 2, 8, 3, 7, 9] jogos [26, 5, 9, 12, 12, 23] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [13, 2, 7, 4, 6, 8] jogos [26, 7, 12, 7, 15, 18] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Fabril tabela [13, 2, 7, 4, 12, 17] jogos [26, 6, 9, 11, 19, 30] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: XV Uber tabela [13, 2, 4, 7, 12, 18] jogos [26, 6, 7, 13, 23, 34] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Nacional Uberaba tabela [13, 1, 4, 8, 4, 18] jogos [26, 6, 7, 13, 15, 31] — a tabela conta 13 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 3, 3, 0, 7, 3] jogos [12, 5, 6, 1, 14, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Cruzeiro tabela [6, 1, 4, 1, 7, 6] jogos [12, 3, 8, 1, 12, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [6, 3, 3, 0, 7, 3] jogos [12, 5, 6, 1, 14, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Cruzeiro tabela [6, 1, 4, 1, 7, 6] jogos [12, 3, 8, 1, 12, 9] — a tabela conta 6 jogos e as fontes trazem 12
- placar diferente no ogol — Tupi x América-MG (1985-08-15): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Cruzeiro x América-MG (1985-10-06): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Cruzeiro x Atlético-MG (1985-12-08): RSSSF 1-3, ogol 0-0; fica o da RSSSF
- data com dia e mês trocados na RSSSF em 1 jogos (ex.: América-MG x Cruzeiro); fica a data do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 18 jogos (ex.: Guarani-MG x Valeriodoce, ogol 1985-08-01); fica a do ogol
- jogo só no ogol, incluído em First Phase:: Tupi 0-0 América-MG (1985-08-01)
- jogo só no ogol, incluído em First Phase:: Cruzeiro 0-0 América-MG (1985-08-18)
- só na RSSSF (não achado no ogol): Tupi 1-0 América-MG (1985-09-15)
- só na RSSSF (não achado no ogol): Cruzeiro 1-1 América-MG (1985-10-06)
- só na RSSSF (não achado no ogol): Uberlândia 0-2 Valeriodoce (1985-12-01)
- só na RSSSF (não achado no ogol): Cruzeiro 0-0 Atlético-MG (1985-12-08)

### 1986

- tabela publicada x jogos — Primeira fase / -: América-MG tabela [15, 6, 7, 2, 15, 9] jogos [15, 6, 7, 2, 17, 8] — placar diverge entre RSSSF e ogol em Caldense x América-MG (2-1 x 2-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Caldense tabela [15, 7, 3, 5, 16, 15] jogos [15, 7, 3, 5, 16, 16] — placar diverge entre RSSSF e ogol em Caldense x América-MG (2-1 x 2-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [15, 4, 7, 4, 18, 15] jogos [15, 4, 7, 4, 17, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: América-MG tabela [15, 6, 7, 2, 15, 10] jogos [15, 6, 7, 2, 17, 8] — placar diverge entre RSSSF e ogol em Caldense x América-MG (2-1 x 2-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [15, 4, 7, 4, 18, 15] jogos [15, 4, 7, 4, 17, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [15, 10, 3, 2, 32, 9] jogos [15, 10, 3, 2, 32, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético-MG tabela [15, 10, 3, 2, 32, 9] jogos [15, 10, 3, 2, 32, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [30, 21, 7, 2, 69, 15] jogos [30, 21, 7, 2, 69, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: América-MG tabela [30, 12, 14, 4, 35, 20] jogos [30, 12, 14, 4, 36, 19] — placar diverge entre RSSSF e ogol em Caldense x América-MG (2-1 x 2-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Tupi tabela [30, 7, 14, 9, 28, 33] jogos [30, 7, 14, 9, 27, 33] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Villa Nova-MG 1-2 Uberlândia, ogol Uberlândia 2-1 Villa Nova-MG (1986-01-29); fica a RSSSF
- mando invertido no ogol — RSSSF Villa Nova-MG 0-2 Cruzeiro, ogol Cruzeiro 2-0 Villa Nova-MG (1986-02-06); fica a RSSSF
- placar diferente no ogol — Caldense x América-MG (1986-03-02): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: Villa Nova-MG x Tupi, ogol 1986-03-09); fica a do ogol

### 1987

- tabela publicada x jogos — 1º Turno / -: Fabril tabela [15, 4, 5, 6, 9, 11] jogos [15, 4, 5, 6, 10, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Uberaba tabela [15, 7, 6, 2, 15, 12] jogos [15, 7, 6, 2, 14, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Fabril tabela [15, 4, 5, 6, 9, 11] jogos [15, 4, 5, 6, 10, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Democrata-GV tabela [15, 3, 2, 10, 13, 26] jogos [15, 3, 2, 10, 12, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Cruzeiro tabela [15, 9, 4, 2, 19, 8] jogos [15, 9, 4, 2, 18, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: América-MG tabela [15, 4, 7, 4, 14, 13] jogos [15, 4, 7, 4, 13, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Cruzeiro tabela [15, 9, 4, 2, 19, 8] jogos [15, 9, 4, 2, 18, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: América-MG tabela [15, 4, 7, 4, 14, 13] jogos [15, 4, 7, 4, 13, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Cruzeiro tabela [32, 21, 6, 5, 43, 13] jogos [36, 22, 8, 6, 47, 16] — a tabela conta 32 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [30, 6, 10, 14, 24, 37] jogos [34, 14, 14, 6, 51, 30] — a tabela conta 30 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase final / -: Tupi tabela [30, 10, 14, 6, 27, 25] jogos [32, 11, 15, 6, 29, 25] — a tabela conta 30 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase final / -: Uberaba tabela [30, 9, 13, 8, 24, 26] jogos [31, 9, 14, 8, 25, 27] — a tabela conta 30 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Caldense tabela [30, 10, 10, 10, 25, 30] jogos [31, 10, 10, 11, 25, 32] — a tabela conta 30 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Valeriodoce tabela [30, 8, 13, 9, 30, 26] jogos [31, 8, 13, 10, 30, 28] — a tabela conta 30 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Villa Nova-MG tabela [30, 8, 12, 10, 22, 30] jogos [31, 8, 13, 10, 22, 30] — a tabela conta 30 jogos e as fontes trazem 31
- mando invertido no ogol — RSSSF Cruzeiro 2-3 Atlético-MG, ogol Atlético-MG 3-2 Cruzeiro (1987-05-10); fica a RSSSF

### 1988

- tabela publicada x jogos — Primeira fase / -: Uberaba tabela [15, 7, 3, 5, 16, 13] jogos [15, 6, 5, 4, 16, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Rio Branco-MG tabela [15, 3, 3, 9, 10, 22] jogos [15, 3, 4, 8, 10, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Fabril tabela [30, 14, 8, 8, 42, 28] jogos [30, 14, 8, 8, 42, 27] — placar diverge entre RSSSF e ogol em Tupi x Fabril (0-2 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Democrata-SL tabela [30, 10, 11, 9, 37, 31] jogos [30, 10, 11, 9, 37, 30] — placar diverge entre RSSSF e ogol em Democrata-SL x Tupi (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Tupi tabela [30, 8, 9, 13, 30, 40] jogos [30, 8, 9, 13, 28, 40] — placar diverge entre RSSSF e ogol em Democrata-SL x Tupi (4-0 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Uberlândia 0-2 América-MG, ogol América-MG 2-0 Uberlândia (1988-05-18); fica a RSSSF
- mando invertido no ogol — RSSSF Villa Nova-MG 1-3 Atlético-MG, ogol Atlético-MG 3-1 Villa Nova-MG (1988-05-22); fica a RSSSF
- placar diferente no ogol — Democrata-SL x Tupi (1988-04-20): RSSSF 4-0, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Tupi x Fabril (1988-05-18): RSSSF 0-2, ogol 1-2; fica o da RSSSF

### 1989

- tabela publicada x jogos — Primeira fase / Grupo A: Pouso Alegre tabela [16, 5, 3, 8, 13, 25] jogos [16, 5, 3, 8, 14, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Pouso Alegre tabela [16, 5, 3, 8, 13, 25] jogos [16, 5, 3, 8, 14, 25] — há jogo do clube sem conferência no ogol
- só na RSSSF (não achado no ogol): Pouso Alegre 0-1 Flamengo-MG (1989-05-30)
- só na RSSSF (não achado no ogol): Pouso Alegre 2-0 Villa Nova-MG (1989-06-15)
- só na RSSSF (não achado no ogol): Pouso Alegre 1-0 Nacional Uberaba (1989-07-02)
- só na RSSSF (não achado no ogol): Uberlândia 4-0 Pouso Alegre (1989-07-16)

### 1990

- tabela publicada x jogos — Final / -: Rio Branco-MG tabela [34, 13, 16, 5, 29, 22] jogos [34, 13, 16, 5, 41, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Juventus de Divinópolis tabela [34, 7, 13, 14, 27, 41] jogos [34, 7, 13, 14, 27, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Atlético-MG 0-0 Uberaba, ogol Uberaba 0-0 Atlético-MG (1990-03-08); fica a RSSSF

### 1991

- mando invertido no ogol — RSSSF Fabril 1-2 Uberlândia, ogol Uberlândia 2-1 Fabril (1991-08-18); fica a RSSSF
- mando invertido no ogol — RSSSF CA Patrocinense 0-0 Cruzeiro, ogol Cruzeiro 0-0 CA Patrocinense (1991-08-18); fica a RSSSF

### 1992

- placar diferente no ogol — Villa Nova-MG x Valeriodoce (1992-10-01): RSSSF 0-2, ogol 0-3; fica o da RSSSF

### 1993

- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [10, 4, 4, 2, 11, 7] jogos [17, 10, 3, 4, 31, 16] — a tabela conta 10 jogos e as fontes trazem 17
- placar diferente no ogol — Nacional Uberaba x Mamoré (1993-03-10): RSSSF 1-0, ogol 0-1; fica o da RSSSF

### 1994

- sem ocorrências

### 1995

- sem ocorrências

### 1996

- tabela publicada x jogos — Segunda fase / -: Villa Nova-MG tabela [12, 7, 3, 2, 18, 9] jogos [12, 7, 3, 2, 16, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Rio Branco-MG tabela [12, 4, 0, 8, 9, 23] jogos [12, 4, 0, 8, 9, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Villa Nova-MG tabela [12, 7, 3, 2, 18, 9] jogos [12, 7, 3, 2, 16, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Rio Branco-MG tabela [12, 4, 0, 8, 9, 23] jogos [12, 4, 0, 8, 9, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall 1st Phase / -: Villa Nova-MG tabela [24, 11, 8, 5, 27, 17] jogos [24, 11, 8, 5, 25, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall 1st Phase / -: Rio Branco-MG tabela [24, 8, 3, 13, 21, 39] jogos [24, 8, 3, 13, 21, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall 1st Phase / -: Guarani-MG tabela [24, 7, 5, 12, 9, 18] jogos [24, 7, 5, 12, 26, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Overall 1st Phase / -: URT tabela [24, 1, 9, 14, 5, 18] jogos [24, 1, 9, 14, 12, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 7 jogos (ex.: Rio Branco-MG x Democrata-GV, ogol 1996-02-11); fica a do ogol

### 1997

- placar diferente no ogol — Uberlândia x Guarani-MG (1997-04-13): RSSSF 0-0, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Cruzeiro x Montes Claros, ogol 1997-05-25); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Cruzeiro

### 1998

- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: Guarani-MG x América-MG, ogol 1998-04-08); fica a do ogol

### 1999

- tabela publicada x jogos — Primeira fase / -: Caldense tabela [14, 5, 6, 3, 17, 15] jogos [14, 5, 6, 3, 16, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Social tabela [14, 3, 5, 6, 9, 14] jogos [14, 3, 5, 6, 8, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Caldense tabela [14, 5, 6, 3, 17, 15] jogos [14, 5, 6, 3, 16, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Social tabela [14, 3, 5, 6, 9, 14] jogos [14, 3, 5, 6, 8, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Atlético-MG

### 2000

- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [14, 7, 2, 5, 24, 16] jogos [14, 7, 2, 5, 24, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Valeriodoce tabela [14, 1, 4, 9, 11, 25] jogos [14, 1, 4, 9, 10, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [14, 7, 2, 5, 24, 16] jogos [14, 7, 2, 5, 24, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Valeriodoce tabela [14, 1, 4, 9, 11, 25] jogos [14, 1, 4, 9, 10, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Ipiranga 0-1 Democrata-GV, ogol Democrata-GV 1-0 Ipiranga (2000-02-16); fica a RSSSF
- mando invertido no ogol — RSSSF Rio Branco-MG 2-1 Ipiranga, ogol Ipiranga 1-2 Rio Branco-MG (2000-03-02); fica a RSSSF
- mando invertido no ogol — RSSSF América-MG 1-2 Atlético-MG, ogol Atlético-MG 2-1 América-MG (2000-04-15); fica a RSSSF

### 2001

- tabela publicada x jogos — Primeira fase / -: Rio Branco-MG tabela [11, 4, 4, 3, 11, 14] jogos [11, 4, 4, 3, 12, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Rio Branco-MG tabela [11, 4, 4, 3, 11, 14] jogos [11, 4, 4, 3, 12, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Ipatinga x Caldense, ogol 2001-05-13); fica a do ogol

### 2002

- placar diferente no ogol — Rio Branco-MG x Uberlândia (2002-03-17): RSSSF 2-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Villa Nova-MG x Uberlândia (2002-05-05): RSSSF 3-0, ogol 3-2; fica o da RSSSF

### 2003

- tabela publicada x jogos — Fase única / -: Tupi tabela [12, 5, 6, 1, 21, 17] jogos [12, 5, 5, 2, 21, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Tupi tabela [12, 5, 6, 1, 21, 17] jogos [12, 5, 5, 2, 21, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Villa Nova-MG x Rio Branco-MG, ogol 2003-02-27); fica a do ogol

### 2004

- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [13, 8, 2, 3, 37, 14] jogos [13, 8, 2, 3, 35, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Cruzeiro tabela [13, 8, 2, 3, 37, 14] jogos [13, 8, 2, 3, 35, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em First Phase: Social 1-2 Caldense (2004-01-25)

### 2005

- sem ocorrências

### 2006

- placar corrigido pelo ogol — América-MG x Uberlândia (2006-02-25): RSSSF 1-1, ogol 1-0; fica o do ogol, que fecha com a tabela publicada

### 2007

- sem ocorrências

### 2008

- sem ocorrências

### 2009

- tabela publicada x jogos — Fase final / -: Atlético-MG tabela [17, 12, 3, 2, 36, 14] jogos [17, 12, 3, 2, 35, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Rio Branco-MG tabela [15, 6, 3, 6, 17, 16] jogos [15, 6, 3, 6, 17, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2010

- mando invertido no ogol — RSSSF Atlético-MG 2-1 Democrata-GV, ogol Democrata-GV 1-2 Atlético-MG (2010-04-10); fica a RSSSF
- mando invertido no ogol — RSSSF Democrata-GV 0-0 Atlético-MG, ogol Atlético-MG 0-0 Democrata-GV (2010-04-17); fica a RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: América T.O. x Atlético-MG, ogol 2010-03-24); fica a do ogol

### 2011

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-TO
- América-TO — casado pelo nome com o clube do calendário do ogol deste ano (América T.O.)

### 2012

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Nacional-MG x América-MG, ogol 2012-02-22); fica a do ogol

### 2013

- sem ocorrências

### 2014

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Guarani-MG x URT, ogol 2014-02-23); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Cruzeiro

### 2015

- sem ocorrências

### 2016

- tabela publicada x jogos — Primeira fase / -: Tricordiano tabela [11, 4, 1, 6, 12, 14] jogos [11, 4, 1, 6, 13, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Tricordiano tabela [11, 4, 1, 6, 12, 14] jogos [11, 4, 1, 6, 13, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Tricordiano tabela [11, 4, 1, 6, 12, 14] jogos [11, 4, 1, 6, 13, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2017

- sem ocorrências

### 2018

- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [11, 3, 1, 7, 12, 26] jogos [11, 3, 1, 7, 12, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Democrata-GV tabela [11, 3, 1, 7, 12, 26] jogos [11, 3, 1, 7, 12, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Democrata-GV tabela [11, 3, 1, 7, 12, 26] jogos [11, 3, 1, 7, 12, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Cruzeiro

### 2019

- sem ocorrências

### 2020

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- tabela publicada x jogos — Primeira fase / -: Coimbra-MG tabela [11, 2, 4, 5, 6, 13] jogos [11, 2, 4, 5, 6, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Tupynambás tabela [11, 0, 3, 8, 5, 26] jogos [11, 0, 3, 8, 6, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Coimbra-MG tabela [11, 2, 4, 5, 6, 13] jogos [11, 2, 4, 5, 6, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Tupynambás tabela [11, 0, 3, 8, 5, 26] jogos [11, 0, 3, 8, 6, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Coimbra-MG tabela [11, 2, 4, 5, 6, 13] jogos [11, 2, 4, 5, 6, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Tupynambás tabela [11, 0, 3, 8, 5, 26] jogos [11, 0, 3, 8, 6, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Cruzeiro 3-0 CA Patrocinense (2020-08-01)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 2-2 Boa Esporte (2020-08-02)

### 2021

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 1-1 Athletic Club (2021-05-01)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Pouso Alegre 0-0 Caldense (2021-05-01)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 0-0 Pouso Alegre (2021-05-05)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Atlético-MG

### 2022

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- tabela publicada x jogos — Primeira fase / -: CA Patrocinense tabela [11, 3, 1, 7, 7, 15] jogos [11, 3, 1, 7, 7, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: CA Patrocinense tabela [11, 3, 1, 7, 7, 15] jogos [11, 3, 1, 7, 7, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: CA Patrocinense tabela [11, 3, 1, 7, 7, 15] jogos [11, 3, 1, 7, 7, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Cruzeiro x Uberlândia (2022-02-17): RSSSF 1-0, ogol 2-1; fica o do ogol, que fecha com a tabela publicada
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tombense 3-1 América-MG (2022-03-24)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 1-2 Villa Nova-MG (2022-03-24)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: América-MG 1-1 Tombense (2022-03-26)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Villa Nova-MG 1-3 Democrata-GV (2022-03-27)
- jogo só no ogol, incluído em Disputa do 3º lugar: Caldense 1-1 Athletic Club (2022-03-31)
- jogo só no ogol, incluído em Disputa do 3º lugar: Athletic Club 0-0 Caldense (2022-04-03)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 1-0 Tombense (2022-04-03)

### 2023

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- tabela publicada x jogos — Primeira fase / Grupo A: Villa Nova-MG tabela [8, 3, 1, 4, 8, 14] jogos [8, 4, 1, 3, 11, 11] — placar diverge entre RSSSF e ogol em Tombense x Villa Nova-MG (0-3 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo B: CA Patrocinense tabela [8, 1, 1, 6, 7, 12] jogos [8, 1, 1, 6, 8, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo C: Tombense tabela [8, 3, 2, 3, 13, 11] jogos [8, 2, 2, 4, 11, 15] — placar diverge entre RSSSF e ogol em Tombense x Villa Nova-MG (0-3 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo A: Villa Nova-MG tabela [8, 3, 1, 4, 8, 14] jogos [8, 4, 1, 3, 11, 11] — placar diverge entre RSSSF e ogol em Tombense x Villa Nova-MG (0-3 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo B: CA Patrocinense tabela [8, 1, 1, 6, 7, 12] jogos [8, 1, 1, 6, 8, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo C: Tombense tabela [8, 3, 2, 3, 13, 11] jogos [8, 2, 2, 4, 11, 15] — placar diverge entre RSSSF e ogol em Tombense x Villa Nova-MG (0-3 x 3-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Tombense x Villa Nova-MG (2023-02-27): RSSSF 0-3, ogol 3-0; fica o da RSSSF
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Pouso Alegre 2-2 Tombense (2023-03-11)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 0-2 Villa Nova-MG (2023-03-13)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tombense 0-0 Pouso Alegre (2023-03-18)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Villa Nova-MG 2-0 Democrata-GV (2023-03-19)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Villa Nova-MG 1-2 Tombense (2023-03-26)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tombense 3-2 Villa Nova-MG (2023-04-01)

### 2024

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- tabela publicada x jogos — Primeira fase / Grupo A: Tombense tabela [8, 4, 3, 1, 15, 8] jogos [8, 4, 3, 1, 15, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Ipatinga tabela [8, 1, 2, 5, 9, 17] jogos [8, 2, 1, 5, 9, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Tombense tabela [8, 4, 3, 1, 15, 8] jogos [8, 4, 3, 1, 15, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Ipatinga tabela [8, 1, 2, 5, 9, 17] jogos [8, 2, 1, 5, 9, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 2-2 Athletic Club (2024-03-09)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Itabirito FC 4-1 Pouso Alegre (2024-03-10)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Pouso Alegre 5-2 Itabirito FC (2024-03-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Athletic Club 0-0 Uberlândia (2024-03-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Pouso Alegre 1-3 Athletic Club (2024-03-23)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Athletic Club 3-0 Pouso Alegre (2024-03-28)

### 2025

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Democrata-GV 0-0 Athletic Club (2025-02-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 0-0 Betim Futebol (2025-02-16)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Athletic Club 1-0 Democrata-GV (2025-02-21)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Betim Futebol 1-1 Uberlândia (2025-02-22)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 0-2 Athletic Club (2025-03-08)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Athletic Club 3-2 Uberlândia (2025-03-15)

### 2026

- Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- tabela publicada x jogos — Primeira fase / Grupo C: Atlético-MG tabela [8, 1, 4, 3, 7, 13] jogos [1, 1, 0, 0, 7, 2] — a tabela conta 8 jogos e as fontes trazem 1
- tabela publicada x jogos — Primeira fase / Grupo C: Atlético-MG tabela [8, 1, 4, 3, 7, 13] jogos [1, 1, 0, 0, 7, 2] — a tabela conta 8 jogos e as fontes trazem 1
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Tombense 0-1 URT (2026-02-20)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Uberlândia 1-1 North Esporte Clube (2026-02-21)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 3-1 Tombense (2026-02-28)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: North Esporte Clube 0-0 Uberlândia (2026-03-01)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: URT 1-2 North Esporte Clube (2026-03-04)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: North Esporte Clube 1-0 URT (2026-03-07)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Clube que o ogol não tem entra pela RSSSF, com código "rs-<nome>". Nunca com o nome exato de outro clube (regra 6b).
- Mesmo clube com outro nome fica com o nome de hoje (Palestra Itália, depois Palestra Mineiro, é o Cruzeiro).

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
