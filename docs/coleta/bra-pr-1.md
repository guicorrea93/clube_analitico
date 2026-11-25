# Campeonato Paranaense (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-pr-1/importar.py`. Pacote em `data/coleta/bra-pr-1/pacote/`. Mesmo código do Mineiro
(`docs/coleta/bra-mg-1.md`), com as fontes do Rio Grande do Sul.

**Temporadas:** 1919 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). 1918, 1923 e 1924 não foram disputados.
Até 1960 o campeonato era por regiões: os campeões das cidades disputavam os regionais e os campeões regionais, a fase
estadual. Entram a fase estadual e as decisões de zona e região que a página da RSSSF traz ("Fase regional"), não os
campeonatos das cidades. A Divisão Especial, com clubes de todo o estado, começou em 1961. 1930 foi organizado pela
FAGET, no lugar da FRGD.

**Fontes:** RSSSF Brasil (`tablesfq/pr{ano}.htm`, 1919-2024: jogos, fases, datas, autores e tabelas); ogol (calendário
de cada edição e o código de cada clube; não tem jogos de 1925 a 1976, salvo 1965; 2025 e 2026 só nele); Wikipédia em
português (artigo do Campeonato Paranaense: campeão e vice de cada ano, segunda fonte). Artilheiros pela lista da RSSSF
(`prtops.htm`), menos 1940-1960, em que ela traz os do campeonato de Porto Alegre.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1915 | RSSSF | 6 | 26 (0) | 91 | 0 | 0 / 1 | Internacional-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 | RSSSF | 13 | 75 (0) | 296 | 0 | 0 / 5 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1917 | RSSSF | 7 | 29 (0) | 114 | 0 | 0 / 0 | América-Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1918 | RSSSF | 6 | 28 (0) | 127 | 0 | 0 / 1 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1919 | RSSSF | 5 | 18 (0) | 49 | 0 | 0 / 1 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF | 7 | 42 (0) | 199 | 0 | 0 / 1 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF | 8 | 47 (0) | 205 | 0 | 0 / 1 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF | 8 | 37 (0) | 176 | 0 | 0 / 1 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1923 | RSSSF | 8 | 32 (0) | 158 | 0 | 0 / 3 | Britânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 | RSSSF | 8 | 24 (0) | 105 | 0 | 0 / 2 | Palestra Itália | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 | RSSSF | 8 | 36 (0) | 165 | 0 | 1 / 2 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 | RSSSF | 7 | 25 (0) | 139 | 0 | 0 / 1 | Palestra Itália | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 | RSSSF | 6 | 23 (0) | 96 | 0 | 0 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 | RSSSF | 4 | 12 (0) | 49 | 0 | 1 / 0 | Britânia | RSSSF (classificação geral publicada) |
| 1929 | RSSSF | 10 | 43 (0) | 227 | 0 | 0 / 1 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF | 7 | 21 (0) | 110 | 0 | 0 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF | 10 | 47 (0) | 267 | 0 | 0 / 2 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 | RSSSF | 9 | 21 (0) | 134 | 0 | 1 / 1 | Palestra Itália | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 | RSSSF | 6 | 21 (0) | 81 | 0 | 1 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 | RSSSF | 7 | 33 (0) | 98 | 0 | 0 / 1 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 | RSSSF | 14 | 34 (0) | 146 | 0 | 0 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 | RSSSF | 11 | 47 (0) | 168 | 0 | 1 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF | 11 | 49 (0) | 194 | 0 | 2 / 0 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF | 11 | 42 (0) | 186 | 0 | 0 / 1 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF | 8 | 46 (0) | 210 | 0 | 2 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF | 7 | 41 (0) | 172 | 0 | 1 / 2 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF | 9 | 43 (0) | 179 | 0 | 2 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF | 7 | 65 (0) | 298 | 0 | 0 / 3 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF | 7 | 43 (0) | 174 | 0 | 5 / 0 | Athletico-PR | RSSSF (classificação geral publicada) |
| 1944 | RSSSF | 6 | 29 (0) | 144 | 0 | 1 / 0 | Ferroviário-PR | RSSSF (classificação geral publicada) |
| 1945 | RSSSF | 7 | 44 (0) | 165 | 0 | 1 / 2 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF | 7 | 60 (0) | 282 | 0 | 0 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF | 7 | 40 (0) | 151 | 0 | 3 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 14 | 55 (0) | 263 | 0 | 0 / 1 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 7 | 42 (0) | 210 | 0 | 1 / 0 | Athletico-PR | RSSSF (classificação geral publicada) |
| 1950 | RSSSF | 8 | 54 (0) | 198 | 0 | 0 / 1 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 9 | 67 (0) | 272 | 0 | 0 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 10 | 86 (0) | 392 | 0 | 1 / 0 | Coritiba | RSSSF (classificação geral publicada) |
| 1953 | RSSSF | 10 | 85 (0) | 354 | 0 | 1 / 5 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 10 | 107 (0) | 399 | 0 | 2 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 10 | 82 (0) | 325 | 0 | 0 / 0 | Monte Alegre | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 13 | 156 (0) | 605 | 0 | 3 / 0 | Coritiba | RSSSF (classificação geral publicada) |
| 1957 | RSSSF | 11 | 108 (0) | 449 | 0 | 3 / 0 | Coritiba | RSSSF (classificação geral publicada) |
| 1958 | RSSSF | 11 | 110 (0) | 401 | 0 | 1 / 0 | Athletico-PR | RSSSF (classificação geral publicada) |
| 1959 | RSSSF | 19 | 177 (0) | 681 | 0 | 1 / 5 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 25 | 313 (0) | 1073 | 0 | 1 / 4 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF | 35 | 434 (0) | 1452 | 0 | 1 / 10 | Comercial-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF | 37 | 441 (0) | 1585 | 0 | 3 / 8 | Londrina | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF | 34 | 462 (0) | 1602 | 0 | 3 / 5 | Grêmio Maringá | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF | 35 | 355 (0) | 1155 | 0 | 1 / 8 | Grêmio Maringá | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF + ogol | 30 | 431 (2) | 1411 | 0 | 0 / 7 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF | 12 | 132 (0) | 359 | 0 | 0 / 1 | Ferroviário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF + ogol | 12 | 136 (3) | 331 | 0 | 2 / 0 | Água Verde | RSSSF (classificação geral publicada) |
| 1968 | RSSSF | 14 | 185 (0) | 492 | 0 | 2 / 0 | Coritiba | RSSSF (classificação geral publicada) |
| 1969 | RSSSF | 14 | 167 (0) | 476 | 0 | 0 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF | 14 | 211 (0) | 556 | 4 | 0 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF | 20 | 236 (0) | 625 | 0 | 0 / 3 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 15 | 268 (0) | 689 | 0 | 0 / 5 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 12 | 156 (0) | 354 | 0 | 0 / 2 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF | 11 | 131 (0) | 285 | 0 | 0 / 2 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 12 | 166 (0) | 384 | 0 | 2 / 4 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF | 14 | 222 (0) | 593 | 0 | 13 / 4 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 16 | 205 (0) | 443 | 19 | 4 / 11 | Grêmio Maringá | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 14 | 123 (0) | 253 | 0 | 6 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 18 | 348 (0) | 709 | 0 | 3 / 14 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF | 20 | 258 (0) | 545 | 0 | 2 / 3 | Colorado-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF | 13 | 165 (0) | 313 | 1 | 1 / 4 | Londrina | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF | 13 | 204 (0) | 408 | 5 | 2 / 5 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF | 12 | 224 (0) | 378 | 0 | 2 / 9 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 12 | 208 (0) | 403 | 0 | 2 / 2 | Pinheiros-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 12 | 167 (0) | 286 | 0 | 3 / 3 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 12 | 158 (0) | 332 | 0 | 1 / 4 | Coritiba | RSSSF (classificação geral publicada) |
| 1987 | RSSSF | 12 | 162 (0) | 318 | 0 | 2 / 2 | Pinheiros-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 12 | 138 (0) | 232 | 0 | 1 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 18 | 233 (0) | 486 | 0 | 1 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF | 22 | 273 (0) | 583 | 0 | 3 / 5 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF | 24 | 369 (0) | 751 | 0 | 3 / 7 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF | 20 | 232 (0) | 530 | 16 | 4 / 1 | Londrina | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF | 20 | 281 (0) | 620 | 0 | 7 / 1 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF | 20 | 213 (0) | 505 | 0 | 0 / 0 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 21 | 297 (0) | 734 | 0 | 1 / 2 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 20 | 110 (0) | 283 | 0 | 1 / 15 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 21 | 236 (0) | 706 | 0 | 4 / 1 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF | 12 | 147 (0) | 407 | 0 | 1 / 4 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF | 12 | 86 (0) | 241 | 0 | 2 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF | 12 | 95 (0) | 299 | 0 | 2 / 2 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 10 | 97 (97) | 350 | 0 | 2 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 8 | 56 (56) | 155 | 0 | 1 / 0 | Iraty | RSSSF (classificação geral publicada) |
| 2002 Supercampeonato | RSSSF + ogol | 8 | 16 (16) | 46 | 0 | 2 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 16 | 77 (76) | 244 | 0 | 1 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 16 | 104 (104) | 329 | 0 | 3 / 2 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 16 | 122 (122) | 364 | 2 | 2 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 16 | 126 (126) | 395 | 0 | 2 / 0 | Paraná | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 16 | 149 (149) | 468 | 0 | 4 / 3 | Paranavaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 16 | 150 (150) | 436 | 0 | 4 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 15 | 133 (133) | 351 | 0 | 2 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 14 | 119 (119) | 326 | 312 | 5 / 0 | Coritiba | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 12 | 134 (132) | 392 | 0 | 4 / 1 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 12 | 136 (136) | 377 | 373 | 3 / 2 | Coritiba | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 12 | 136 (134) | 351 | 351 | 3 / 2 | Coritiba | RSSSF (classificação geral publicada) |
| 2014 | RSSSF + ogol | 12 | 94 (94) | 245 | 241 | 2 / 0 | Londrina | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 12 | 92 (92) | 208 | 208 | 8 / 1 | Operário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 12 | 80 (80) | 220 | 218 | 4 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 12 | 82 (80) | 187 | 187 | 9 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 12 | 74 (74) | 171 | 167 | 5 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 12 | 74 (74) | 153 | 151 | 5 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 12 | 80 (80) | 200 | 155 | 1 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 12 | 80 (80) | 178 | 0 | 1 / 0 | Londrina | RSSSF (classificação geral publicada) |
| 2022 | RSSSF + ogol | 12 | 80 (80) | 187 | 0 | 9 / 0 | Coritiba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 12 | 80 (80) | 197 | 0 | 2 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 12 | 80 (80) | 184 | 0 | 0 / 2 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 12 | 80 (80) | 190 | 0 | 2 / 0 | Operário-PR | RSSSF (classificação geral publicada) |
| 2026 | RSSSF + ogol | 12 | 54 (54) | 132 | 0 | 2 / 1 | Operário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1915

- tabela publicada x jogos — 2º Turno / -: Internacional-PR tabela [10, 9, 0, 1, 26, 7] jogos [8, 7, 0, 1, 26, 7] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Paraná SC tabela [10, 7, 1, 2, 18, 5] jogos [8, 5, 1, 2, 18, 5] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: América-PR tabela [10, 5, 1, 4, 15, 14] jogos [8, 3, 1, 4, 15, 14] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 3, 3, 4, 14, 12] jogos [8, 3, 2, 3, 13, 11] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Rio Branco-PR tabela [10, 1, 2, 7, 8, 16] jogos [5, 1, 1, 3, 7, 15] — a tabela conta 10 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / -: Paranaguá tabela [10, 1, 1, 8, 12, 39] jogos [9, 1, 1, 7, 12, 39] — a tabela conta 10 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranaguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- América — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — clube que o ogol não tem; entra só pela RSSSF
- Paranaguá — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- campeão pela lista oficial, Internacional-PR; o 1º pela soma dos jogos da última fase é Paraná SC (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Paraná SC

### 1916

- tabela publicada x jogos — 2º Turno / APSA: Coritiba tabela [12, 10, 0, 2, 38, 14] jogos [11, 9, 0, 2, 38, 14] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / APSA: Água Verde tabela [12, 9, 2, 1, 36, 14] jogos [12, 10, 1, 1, 39, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / APSA: Palmeiras-PR tabela [12, 3, 5, 4, 19, 21] jogos [12, 3, 4, 5, 22, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / APSA: Espartano tabela [12, 2, 3, 7, 14, 35] jogos [11, 1, 3, 7, 14, 35] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / APSA: Paraná SC tabela [12, 1, 3, 8, 13, 35] jogos [11, 1, 2, 8, 13, 35] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / APSA: Rio Branco-PR tabela [12, 1, 2, 9, 11, 21] jogos [9, 1, 1, 7, 10, 20] — a tabela conta 12 jogos e as fontes trazem 9
- tabela publicada x jogos — JOGO DESEMPATE / -: Coritiba tabela [13, 11, 0, 2, 39, 14] jogos [13, 11, 0, 2, 41, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — JOGO DESEMPATE / -: Água Verde tabela [13, 9, 2, 2, 36, 15] jogos [13, 10, 1, 2, 39, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — JOGO DESEMPATE / -: Palmeiras-PR tabela [12, 3, 5, 4, 19, 21] jogos [12, 3, 4, 5, 22, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — JOGO DESEMPATE / -: Espartano tabela [12, 2, 3, 7, 14, 35] jogos [11, 1, 3, 7, 14, 35] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — JOGO DESEMPATE / -: Paraná SC tabela [12, 1, 3, 8, 13, 35] jogos [11, 1, 2, 8, 13, 35] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — JOGO DESEMPATE / -: Rio Branco-PR tabela [12, 1, 2, 9, 11, 21] jogos [9, 1, 1, 7, 10, 20] — a tabela conta 12 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / LSP: Britânia tabela [10, 8, 0, 2, 29, 10] jogos [11, 8, 0, 3, 29, 11] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / LSP: América de Paranaguá tabela [10, 8, 0, 2, 17, 12] jogos [11, 9, 0, 2, 19, 12] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / LSP: Internacional-PR tabela [10, 6, 1, 3, 36, 14] jogos [9, 6, 1, 2, 37, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / LSP: Bela Vista-PR tabela [10, 3, 2, 5, 15, 23] jogos [12, 4, 2, 6, 17, 26] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / LSP: Pinheiro SC tabela [10, 0, 0, 10, 4, 33] jogos [11, 0, 0, 11, 4, 37] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase - Final / LSP: Britânia tabela [11, 9, 0, 2, 33, 10] jogos [12, 9, 0, 3, 33, 11] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase - Final / LSP: América de Paranaguá tabela [11, 8, 0, 3, 17, 16] jogos [12, 9, 0, 3, 19, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase - Final / LSP: Internacional-PR tabela [10, 6, 1, 3, 36, 14] jogos [9, 6, 1, 2, 37, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase - Final / LSP: Bela Vista-PR tabela [10, 3, 2, 5, 15, 23] jogos [12, 4, 2, 6, 17, 26] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase - Final / LSP: Pinheiro SC tabela [10, 0, 0, 10, 4, 33] jogos [11, 0, 0, 11, 4, 37] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Coritiba tabela [13, 11, 0, 2, 39, 14] jogos [13, 11, 0, 2, 41, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Britânia tabela [11, 9, 0, 2, 33, 10] jogos [13, 9, 0, 4, 34, 13] — a tabela conta 11 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Americano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bela Vista
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Espartano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Americano — clube que o ogol não tem; entra só pela RSSSF
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PR)
- Bela Vista — clube que o ogol não tem; entra só pela RSSSF
- Britânia — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Espartano — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- Palmeiras — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1917

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmeiras
- América-Paraná — clube que o ogol não tem; entra só pela RSSSF
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras-PR)
- campeão pela lista oficial, América-Paraná; o 1º pela soma dos jogos da última fase é Britânia (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Internacional-PR

### 1918

- tabela publicada x jogos — Fase única / -: Britânia tabela [10, 7, 1, 2, 34, 14] jogos [9, 6, 1, 2, 34, 14] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Coritiba tabela [10, 6, 1, 3, 28, 14] jogos [9, 6, 1, 2, 28, 14] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Internacional-PR tabela [10, 6, 1, 3, 21, 19] jogos [9, 5, 1, 3, 21, 19] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Água Verde FBC tabela [10, 5, 1, 4, 18, 24] jogos [8, 3, 1, 4, 18, 24] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Acadêmica-PR tabela [10, 0, 0, 10, 6, 38] jogos [7, 0, 0, 7, 6, 38] — a tabela conta 10 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Acadêmica
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Acadêmica — clube que o ogol não tem; entra só pela RSSSF
- América-Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-Paraná)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- vice pela Wikipédia (sem final de dois clubes): Internacional-PR

### 1919

- tabela publicada x jogos — Fase única / -: Britânia tabela [7, 5, 2, 0, 14, 4] jogos [7, 5, 2, 0, 17, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Água Verde FBC tabela [7, 2, 2, 3, 7, 15] jogos [7, 1, 2, 4, 8, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Internacional-PR tabela [4, 0, 1, 3, 1, 2] jogos [2, 0, 1, 1, 1, 2] — a tabela conta 4 jogos e as fontes trazem 2
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Acadêmica
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Acadêmica — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Acadêmica-PR)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1920

- tabela publicada x jogos — Segunda fase / -: Britânia tabela [11, 8, 1, 2, 41, 18] jogos [14, 10, 2, 2, 55, 26] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [10, 7, 2, 1, 30, 17] jogos [12, 8, 3, 1, 37, 23] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Água Verde tabela [10, 6, 1, 3, 26, 15] jogos [13, 9, 1, 3, 40, 17] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Paraná SC tabela [10, 4, 2, 4, 19, 20] jogos [12, 4, 3, 5, 22, 24] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Internacional-PR tabela [6, 2, 0, 4, 11, 20] jogos [9, 3, 0, 6, 18, 32] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Esperança-PR tabela [10, 2, 0, 8, 10, 34] jogos [13, 2, 0, 11, 11, 47] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: América-PR tabela [9, 0, 2, 7, 13, 26] jogos [11, 0, 3, 8, 16, 30] — a tabela conta 9 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Esperança — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1921

- tabela publicada x jogos — Segunda fase / -: Palestra Itália tabela [12, 7, 3, 2, 27, 15] jogos [13, 7, 3, 3, 27, 17] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Água Verde tabela [12, 7, 0, 5, 28, 23] jogos [14, 9, 0, 5, 37, 23] — a tabela conta 12 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Paraná SC tabela [12, 2, 1, 9, 19, 36] jogos [13, 3, 1, 9, 22, 37] — a tabela conta 12 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Esperança — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esperança-PR)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)

### 1922

- tabela publicada x jogos — 2º Turno / -: Britânia tabela [11, 10, 1, 0, 47, 11] jogos [10, 9, 1, 0, 47, 11] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Internacional-PR tabela [11, 4, 3, 4, 17, 17] jogos [10, 4, 3, 3, 17, 17] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Paraná SC tabela [9, 4, 1, 4, 20, 21] jogos [9, 4, 1, 4, 23, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [6, 1, 0, 5, 14, 18] jogos [6, 1, 0, 5, 14, 21] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)

### 1923

- tabela publicada x jogos — 1º Turno / -: Coritiba tabela [13, 7, 5, 1, 1, 16] jogos [4, 3, 1, 0, 12, 4] — a tabela conta 13 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Água Verde tabela [7, 4, 2, 1, 14, 8] jogos [5, 3, 2, 0, 14, 6] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / -: Campo Alegre tabela [7, 2, 0, 5, 8, 29] jogos [6, 1, 0, 5, 8, 29] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Internacional-PR tabela [7, 1, 0, 6, 5, 13] jogos [4, 1, 0, 3, 5, 13] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Universal-PR tabela [7, 1, 0, 6, 9, 40] jogos [6, 0, 0, 6, 6, 38] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [10, 5, 3, 2, 24, 17] jogos [8, 4, 3, 1, 24, 15] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 5, 1, 4, 18, 16] jogos [7, 3, 1, 3, 14, 13] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [10, 5, 3, 2, 24, 17] jogos [8, 4, 3, 1, 24, 15] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 5, 1, 4, 18, 16] jogos [7, 3, 1, 3, 14, 13] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Campo Alegre tabela [7, 2, 0, 5, 8, 29] jogos [6, 1, 0, 5, 8, 29] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Internacional-PR tabela [7, 1, 0, 6, 5, 13] jogos [4, 1, 0, 3, 5, 13] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Universal-PR tabela [7, 1, 0, 6, 9, 40] jogos [6, 0, 0, 6, 6, 38] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Universal
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Alegre)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional-PR)
- Universal — clube que o ogol não tem; entra só pela RSSSF

### 1924

- tabela publicada x jogos — 1º Turno / -: Palestra Itália tabela [7, 5, 2, 0, 23, 11] jogos [7, 5, 2, 0, 23, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Coritiba tabela [7, 5, 1, 1, 31, 10] jogos [9, 5, 2, 2, 30, 13] — a tabela conta 7 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno / -: Britânia tabela [7, 4, 2, 1, 18, 11] jogos [7, 2, 1, 4, 10, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Água Verde tabela [7, 4, 1, 2, 16, 8] jogos [7, 5, 1, 1, 11, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Athletico-PR tabela [7, 4, 0, 3, 20, 15] jogos [4, 2, 0, 2, 13, 10] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Campo Alegre tabela [7, 1, 1, 5, 10, 23] jogos [7, 1, 1, 5, 9, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Universal-PR tabela [7, 1, 0, 6, 7, 35] jogos [4, 0, 0, 4, 5, 22] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Paraná SC tabela [7, 0, 1, 6, 4, 16] jogos [3, 0, 1, 2, 4, 12] — a tabela conta 7 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / -: Palestra Itália tabela [10, 7, 3, 0, 30, 14] jogos [7, 5, 2, 0, 23, 9] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 6, 2, 2, 37, 14] jogos [9, 5, 2, 2, 30, 13] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [10, 6, 1, 3, 19, 10] jogos [7, 5, 1, 1, 11, 5] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Britânia tabela [10, 4, 2, 4, 21, 21] jogos [7, 2, 1, 4, 10, 15] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [7, 4, 0, 3, 20, 15] jogos [4, 2, 0, 2, 13, 10] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Campo Alegre tabela [7, 1, 1, 5, 10, 23] jogos [7, 1, 1, 5, 9, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Universal-PR tabela [7, 1, 0, 6, 7, 35] jogos [4, 0, 0, 4, 5, 22] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Paraná SC tabela [7, 0, 1, 6, 4, 16] jogos [3, 0, 1, 2, 4, 12] — a tabela conta 7 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Universal
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Alegre)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Universal — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Universal-PR)

### 1925

- tabela publicada x jogos — 1º Turno / -: Paraná SC tabela [7, 2, 0, 5, 13, 29] jogos [6, 1, 0, 5, 13, 29] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Campo Alegre tabela [7, 1, 0, 6, 8, 23] jogos [6, 1, 0, 5, 8, 23] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Paraná SC tabela [7, 2, 0, 5, 13, 29] jogos [6, 1, 0, 5, 13, 29] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Campo Alegre tabela [7, 1, 0, 6, 8, 23] jogos [6, 1, 0, 5, 8, 23] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Universal
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Alegre)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Universal — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Universal-PR)
- campeão pela lista oficial, Athletico-PR; o 1º pela soma dos jogos da última fase é Água Verde (desempate, jogo extra ou pontos tirados fora de campo)

### 1926

- tabela publicada x jogos — Segunda fase / -: Palestra Itália tabela [10, 8, 0, 2, 19, 10] jogos [6, 4, 0, 2, 17, 9] — a tabela conta 10 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [10, 6, 1, 3, 22, 16] jogos [7, 4, 1, 2, 21, 14] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [10, 5, 1, 4, 29, 20] jogos [10, 5, 1, 4, 42, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Água Verde tabela [10, 5, 0, 5, 22, 19] jogos [8, 5, 0, 3, 22, 19] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / -: Paraná SC tabela [6, 1, 0, 5, 5, 23] jogos [6, 1, 0, 5, 6, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Campo Alegre tabela [6, 0, 0, 6, 1, 15] jogos [3, 0, 0, 3, 1, 15] — a tabela conta 6 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Alegre)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- campeão pela lista oficial, Palestra Itália; o 1º pela soma dos jogos da última fase é Coritiba (desempate, jogo extra ou pontos tirados fora de campo)

### 1927

- tabela publicada x jogos — Operário não participou do returno e o / -: Athletico-PR tabela [9, 6, 2, 1, 19, 9] jogos [8, 5, 2, 1, 19, 9] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Operário não participou do returno e o / -: Britânia tabela [9, 3, 3, 3, 17, 18] jogos [8, 2, 3, 3, 17, 18] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Operário não participou do returno e o / -: Campo Alegre tabela [9, 1, 1, 7, 8, 20] jogos [7, 1, 1, 5, 8, 20] — a tabela conta 9 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Alegre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Campo Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Alegre)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1928

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1929

- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [12, 10, 2, 0, 48, 11] jogos [13, 11, 2, 0, 58, 12] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Palestra Itália tabela [12, 10, 0, 2, 57, 13] jogos [11, 9, 0, 2, 57, 13] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [12, 6, 1, 5, 56, 32] jogos [10, 4, 1, 5, 36, 31] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Bangu-PR tabela [12, 2, 1, 9, 11, 42] jogos [10, 2, 1, 7, 11, 42] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Aquidaban-PR tabela [7, 0, 2, 5, 4, 43] jogos [6, 0, 2, 4, 3, 33] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Paranaense tabela [7, 0, 1, 6, 3, 36] jogos [6, 0, 1, 5, 3, 26] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aquidaban
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bangu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranaense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranaguá
- Aquidaban — clube que o ogol não tem; entra só pela RSSSF
- Bangu — clube que o ogol não tem; entra só pela RSSSF
- Brasil — clube que o ogol não tem; entra só pela RSSSF
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Paranaense — clube que o ogol não tem; entra só pela RSSSF
- Paranaguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranaguá)
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1930

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aquidaban
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranaense
- Aquidaban — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aquidaban-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Paranaense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranaense)

### 1931

- tabela publicada x jogos — Primeira fase / -: Ferroviário-PR tabela [8, 4, 0, 4, 15, 16] jogos [8, 4, 0, 4, 17, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Paranaense tabela [8, 0, 0, 8, 5, 47] jogos [8, 0, 0, 8, 5, 49] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Ferroviário-PR tabela [12, 5, 1, 6, 21, 31] jogos [12, 5, 1, 6, 23, 31] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aquidaban
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olinda
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranaense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Poty
- Aquidaban — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aquidaban-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — clube que o ogol não tem; entra só pela RSSSF
- Olinda — clube que o ogol não tem; entra só pela RSSSF
- Paranaense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranaense)
- Poty — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Guarani-PR

### 1932

- tabela publicada x jogos — Primeira fase / -: Palestra Itália tabela [8, 6, 1, 1, 26, 11] jogos [5, 3, 1, 1, 19, 8] — a tabela conta 8 jogos e as fontes trazem 5
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Elite
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra/UV
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Elite — clube que o ogol não tem; entra só pela RSSSF
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Palestra/UV — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1933

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Rússia
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Nova Rússia — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Nova Rússia

### 1934

- tabela publicada x jogos — 2º Turno / -: Britânia tabela [10, 5, 2, 3, 18, 13] jogos [11, 5, 2, 4, 18, 14] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 3, 2, 5, 14, 18] jogos [11, 4, 2, 5, 15, 18] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1935

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Americano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Junak
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Matarazzo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Oceania
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olinda
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- Americano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Americano-PR)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Junak — clube que o ogol não tem; entra só pela RSSSF
- Matarazzo — clube que o ogol não tem; entra só pela RSSSF
- Oceania — clube que o ogol não tem; entra só pela RSSSF
- Olinda — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olinda)
- União — clube que o ogol não tem; entra só pela RSSSF

### 1936

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Junak
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Matarazzo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Junak — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Junak)
- Matarazzo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Matarazzo)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vencedor da final pelos jogos (Operário-PR) diferente do campeão oficial (Athletico-PR); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1937

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Junak
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Matarazzo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Junak — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Junak)
- Matarazzo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Matarazzo)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1938

- tabela publicada x jogos — 2º Turno / -: Ferroviário-PR tabela [10, 7, 2, 1, 35, 23] jogos [13, 10, 2, 1, 49, 27] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 4, 3, 3, 26, 18] jogos [11, 4, 3, 4, 27, 20] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Ypiranga — clube que o ogol não tem; entra só pela RSSSF

### 1939

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pinheiral
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- Pinheiral — clube que o ogol não tem; entra só pela RSSSF

### 1940

- tabela publicada x jogos — Segunda fase / -: Britânia tabela [6, 3, 1, 2, 8, 11] jogos [5, 2, 1, 2, 8, 11] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / -: Ferroviário-PR tabela [6, 3, 0, 3, 12, 13] jogos [5, 3, 0, 2, 12, 13] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / -: Ferroviário-PR tabela [12, 8, 0, 4, 28, 22] jogos [11, 8, 0, 3, 28, 22] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)

### 1941

- tabela publicada x jogos — Primeira fase / -: Ferroviário-PR tabela [6, 1, 1, 4, 8, 18] jogos [6, 1, 1, 4, 8, 16] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Antoninense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Antoninense — clube que o ogol não tem; entra só pela RSSSF
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jacarezinho — clube que o ogol não tem; entra só pela RSSSF
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)

### 1942

- tabela publicada x jogos — Segunda fase / -: Ferroviário-PR tabela [12, 9, 1, 2, 40, 19] jogos [12, 8, 1, 3, 34, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [12, 7, 2, 3, 40, 21] jogos [12, 8, 2, 2, 41, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Coritiba tabela [6, 4, 1, 1, 21, 8] jogos [6, 4, 1, 1, 22, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Palestra Itália tabela [6, 1, 1, 4, 14, 23] jogos [6, 1, 1, 4, 14, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [20, 12, 4, 4, 69, 33] jogos [20, 13, 4, 3, 71, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Ferroviário-PR tabela [20, 11, 4, 5, 58, 44] jogos [20, 10, 4, 6, 52, 45] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Palestra Itália tabela [18, 5, 2, 11, 32, 53] jogos [18, 5, 2, 11, 32, 54] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)

### 1943

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1945

- tabela publicada x jogos — Segunda fase / -: Ferroviário-PR tabela [6, 3, 1, 2, 11, 11] jogos [5, 2, 1, 2, 10, 11] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / -: Juventus-PR tabela [6, 0, 0, 6, 4, 15] jogos [5, 0, 0, 5, 4, 14] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Final / -: Athletico-PR tabela [15, 11, 2, 2, 42, 25] jogos [15, 11, 2, 2, 42, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Coritiba tabela [15, 8, 0, 7, 32, 26] jogos [15, 8, 0, 7, 29, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Ferroviário-PR tabela [12, 6, 2, 4, 22, 18] jogos [11, 5, 2, 4, 21, 18] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Juventus-PR tabela [12, 1, 0, 11, 10, 32] jogos [11, 1, 0, 10, 10, 31] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)

### 1946

- tabela publicada x jogos — Terceira fase / -: Coritiba tabela [17, 13, 1, 3, 70, 26] jogos [18, 14, 2, 2, 72, 27] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Terceira fase / -: Ferroviário-PR tabela [17, 10, 3, 4, 56, 31] jogos [18, 11, 3, 4, 57, 31] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Terceira fase / -: Athletico-PR tabela [16, 10, 2, 4, 44, 25] jogos [17, 9, 3, 5, 45, 27] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Terceira fase / -: Água Verde tabela [16, 1, 2, 13, 16, 52] jogos [17, 1, 2, 14, 16, 53] — a tabela conta 16 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1947

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1948

- tabela publicada x jogos — Segunda fase / -: Britânia tabela [12, 3, 1, 8, 24, 36] jogos [12, 3, 1, 8, 21, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Juventus-PR tabela [12, 3, 1, 8, 21, 29] jogos [12, 3, 1, 8, 24, 36] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fanático
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fuganti
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Matarazzo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Fanático — clube que o ogol não tem; entra só pela RSSSF
- Fuganti — clube que o ogol não tem; entra só pela RSSSF
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- Matarazzo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Matarazzo)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vencedor da final pelos jogos (Jacarezinho) diferente do campeão oficial (Ferroviário-PR); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1949

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1950

- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [13, 5, 0, 8, 23, 29] jogos [13, 5, 0, 8, 23, 28] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-PR)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1951

- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [16, 10, 4, 2, 41, 17] jogos [14, 9, 4, 1, 39, 16] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Jacarezinho tabela [16, 11, 1, 4, 49, 17] jogos [14, 10, 1, 3, 44, 14] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Monte Alegre tabela [16, 7, 0, 9, 31, 31] jogos [13, 5, 0, 8, 29, 31] — a tabela conta 16 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [16, 6, 1, 9, 39, 41] jogos [14, 6, 1, 7, 37, 34] — a tabela conta 16 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Monte Alegre
- Bloco Morgenau — clube que o ogol não tem; entra só pela RSSSF
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Monte Alegre — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Coritiba; o 1º pela soma dos jogos da última fase é Palestra Itália (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Jacarezinho

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CAMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambaraense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- CAMA — clube que o ogol não tem; entra só pela RSSSF
- Cambaraense — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- vice pela Wikipédia (sem final de dois clubes): Palestra Itália

### 1953

- tabela publicada x jogos — Segunda fase / -: Cambaraense tabela [18, 14, 0, 4, 57, 25] jogos [18, 15, 0, 3, 60, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Água Verde tabela [17, 10, 2, 5, 39, 27] jogos [16, 8, 2, 6, 29, 27] — a tabela conta 17 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Monte Alegre tabela [18, 8, 2, 8, 49, 44] jogos [19, 8, 3, 8, 50, 45] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Jacarezinho tabela [16, 6, 5, 5, 25, 18] jogos [15, 6, 4, 5, 24, 17] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Palestra Itália tabela [18, 5, 5, 8, 24, 40] jogos [17, 4, 5, 8, 21, 38] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Segunda fase / -: Bloco Morgenau tabela [16, 1, 1, 14, 15, 61] jogos [16, 1, 1, 14, 14, 57] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambaraense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Monte Alegre
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambaraense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambaraense)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Monte Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Monte Alegre)
- vice pela Wikipédia (sem final de dois clubes): Cambaraense

### 1954

- tabela publicada x jogos — Final / -: Athletico-PR tabela [23, 9, 10, 4, 41, 34] jogos [22, 9, 9, 4, 41, 34] — a tabela conta 23 jogos e as fontes trazem 22
- tabela publicada x jogos — Final / -: CAMA tabela [23, 11, 3, 9, 65, 40] jogos [22, 11, 2, 9, 65, 40] — a tabela conta 23 jogos e as fontes trazem 22
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CAMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): guarani
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- CAMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CAMA)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Monte Alegre
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Caramuru — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Monte Alegre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Monte Alegre)
- campeão pela lista oficial, Monte Alegre; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1956

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CAMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru EC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- CAMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CAMA)
- Caramuru EC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1958

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1959

- tabela publicada x jogos — Primeira fase / Southern Group: Coritiba tabela [20, 14, 5, 1, 59, 31] jogos [19, 13, 5, 1, 55, 29] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Caramuru tabela [20, 13, 2, 5, 42, 25] jogos [19, 12, 2, 5, 38, 22] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Guarani-PR tabela [20, 11, 4, 5, 46, 34] jogos [19, 10, 4, 5, 44, 33] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Ferroviário-PR tabela [20, 10, 5, 5, 48, 36] jogos [19, 10, 5, 4, 47, 34] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Athletico-PR tabela [20, 8, 5, 7, 43, 35] jogos [19, 8, 5, 6, 41, 31] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Operário-PR tabela [20, 9, 2, 9, 58, 42] jogos [19, 9, 2, 8, 54, 38] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Southern Group: Rio Branco-PR tabela [20, 8, 2, 10, 33, 41] jogos [20, 8, 2, 10, 33, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ferroviário-PR tabela [6, 4, 2, 0, 18, 5] jogos [8, 4, 2, 2, 20, 9] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Coritiba tabela [6, 4, 1, 1, 22, 7] jogos [10, 8, 1, 1, 31, 10] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Londrina tabela [7, 5, 1, 1, 22, 5] jogos [10, 8, 2, 0, 31, 7] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Arapongas FC tabela [7, 5, 1, 1, 13, 7] jogos [12, 7, 2, 3, 21, 13] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Northern Group: Mandaguari tabela [7, 4, 1, 2, 16, 10] jogos [10, 4, 1, 5, 18, 21] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Nacional-PR tabela [7, 1, 6, 0, 9, 8] jogos [10, 4, 5, 1, 21, 10] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Portuguesa Londrinense tabela [7, 2, 1, 4, 12, 15] jogos [11, 2, 4, 5, 19, 26] — a tabela conta 7 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / Northern Group: Comercial-PR tabela [7, 2, 1, 4, 7, 11] jogos [9, 1, 2, 6, 11, 24] — a tabela conta 7 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / Northern Group: Astorga tabela [7, 1, 1, 5, 6, 14] jogos [12, 1, 3, 8, 13, 32] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Northern Group: Londrina tabela [7, 6, 1, 0, 22, 5] jogos [10, 8, 2, 0, 31, 7] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Mandaguari tabela [7, 4, 1, 2, 12, 11] jogos [10, 4, 1, 5, 18, 21] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Arapongas FC tabela [7, 3, 2, 2, 7, 6] jogos [12, 7, 2, 3, 21, 13] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Northern Group: Nacional-PR tabela [7, 3, 2, 2, 17, 8] jogos [10, 4, 5, 1, 21, 10] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Portuguesa Londrinense tabela [7, 1, 3, 3, 10, 15] jogos [11, 2, 4, 5, 19, 26] — a tabela conta 7 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / Northern Group: Comercial-PR tabela [7, 1, 3, 3, 9, 15] jogos [9, 1, 2, 6, 11, 24] — a tabela conta 7 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / Northern Group: Astorga tabela [7, 0, 2, 5, 5, 18] jogos [12, 1, 3, 8, 13, 32] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Northern Group: Londrina tabela [14, 11, 2, 1, 44, 10] jogos [10, 8, 2, 0, 31, 7] — a tabela conta 14 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Arapongas FC tabela [14, 8, 3, 3, 20, 13] jogos [12, 7, 2, 3, 21, 13] — a tabela conta 14 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Northern Group: Mandaguari tabela [14, 8, 2, 4, 28, 21] jogos [10, 4, 1, 5, 18, 21] — a tabela conta 14 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Nacional-PR tabela [14, 4, 8, 2, 26, 16] jogos [10, 4, 5, 1, 21, 10] — a tabela conta 14 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / Northern Group: Portuguesa Londrinense tabela [14, 3, 4, 7, 22, 30] jogos [11, 2, 4, 5, 19, 26] — a tabela conta 14 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / Northern Group: Comercial-PR tabela [14, 3, 4, 7, 16, 26] jogos [9, 1, 2, 6, 11, 24] — a tabela conta 14 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / Northern Group: Astorga tabela [14, 1, 3, 10, 11, 32] jogos [12, 1, 3, 8, 13, 32] — a tabela conta 14 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Astorga — clube que o ogol não tem; entra só pela RSSSF
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Gera — clube que o ogol não tem; entra só pela RSSSF
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vencedor da final pelos jogos (Londrina) diferente do campeão oficial (Coritiba); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Londrina

### 1960

- tabela publicada x jogos — 3º Turno / -: Coritiba tabela [7, 4, 2, 1, 18, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Ferroviário-PR tabela [7, 4, 1, 2, 15, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Operário-PR tabela [7, 3, 2, 2, 15, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Água Verde tabela [7, 3, 2, 2, 9, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Rio Branco-PR tabela [7, 3, 1, 3, 16, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Iraty tabela [7, 3, 1, 3, 11, 23] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Athletico-PR tabela [7, 2, 1, 4, 12, 16] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Guarani-PR tabela [7, 0, 2, 5, 9, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — CLASSIFICAÇÃO DOS DOIS TURNOS / -: Gera tabela [22, 7, 6, 9, 28, 37] jogos [20, 6, 6, 8, 26, 35] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — CLASSIFICAÇÃO DOS DOIS TURNOS / -: Paranavaí tabela [22, 7, 5, 10, 45, 42] jogos [21, 7, 5, 9, 45, 41] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 3º Turno / -: Mandaguari tabela [5, 2, 3, 0, 7, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Nacional-PR tabela [5, 2, 3, 0, 9, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Paranavaí tabela [5, 2, 3, 0, 11, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Arapongas FC tabela [5, 2, 1, 2, 9, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Comercial-PR tabela [5, 1, 2, 2, 8, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / -: Londrina tabela [5, 0, 0, 5, 2, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Final / -: Mandaguari tabela [34, 16, 14, 4, 78, 32] jogos [32, 15, 13, 4, 72, 29] — a tabela conta 34 jogos e as fontes trazem 32
- tabela publicada x jogos — Final / -: Comercial-PR tabela [32, 17, 8, 7, 63, 37] jogos [30, 16, 8, 6, 60, 34] — a tabela conta 32 jogos e as fontes trazem 30
- tabela publicada x jogos — Final / -: Nacional-PR tabela [31, 13, 13, 5, 69, 43] jogos [28, 13, 10, 5, 64, 38] — a tabela conta 31 jogos e as fontes trazem 28
- tabela publicada x jogos — Final / -: Londrina tabela [29, 16, 4, 9, 55, 35] jogos [26, 15, 3, 8, 50, 30] — a tabela conta 29 jogos e as fontes trazem 26
- tabela publicada x jogos — Final / -: Paranavaí tabela [33, 10, 11, 12, 66, 64] jogos [28, 9, 9, 10, 58, 54] — a tabela conta 33 jogos e as fontes trazem 28
- tabela publicada x jogos — Final / -: Gera tabela [24, 7, 7, 10, 32, 43] jogos [20, 6, 6, 8, 26, 35] — a tabela conta 24 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela do Norte
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GERA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — clube que o ogol não tem; entra só pela RSSSF
- Astorga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Astorga)
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambé — clube que o ogol não tem; entra só pela RSSSF
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Estrela do Norte — clube que o ogol não tem; entra só pela RSSSF
- GERA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gera)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Independente — clube que o ogol não tem; entra só pela RSSSF
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vice pela Wikipédia (sem final de dois clubes): Mandaguari

### 1961

- tabela publicada x jogos — Primeira fase / ZONA SUL - 1º: Iraty tabela [14, 6, 3, 5, 17, 18] jogos [14, 5, 3, 6, 17, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / ZONA SUL - 1º: Palestra Itália tabela [14, 2, 2, 10, 16, 31] jogos [14, 3, 2, 9, 16, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / ZONA SUL - 2º: Seleto tabela [14, 5, 1, 8, 22, 26] jogos [14, 5, 1, 8, 21, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / -: Coritiba tabela [28, 18, 7, 3, 72, 23] jogos [31, 19, 8, 4, 76, 26] — a tabela conta 28 jogos e as fontes trazem 31
- tabela publicada x jogos — duas primeiras partidas da decisão / -: Operário-PR tabela [28, 18, 7, 3, 64, 24] jogos [31, 19, 8, 4, 67, 28] — a tabela conta 28 jogos e as fontes trazem 31
- tabela publicada x jogos — duas primeiras partidas da decisão / -: Iraty tabela [28, 16, 4, 8, 47, 34] jogos [28, 15, 4, 9, 47, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / -: Seleto tabela [28, 7, 6, 15, 37, 55] jogos [28, 7, 6, 15, 36, 54] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / -: Palestra Itália tabela [27, 3, 2, 22, 25, 71] jogos [27, 4, 2, 21, 25, 71] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 1º: Mandaguari tabela [13, 7, 6, 0, 20, 7] jogos [10, 4, 6, 0, 14, 6] — a tabela conta 13 jogos e as fontes trazem 10
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 1º: Paranavaí tabela [13, 7, 2, 4, 19, 12] jogos [11, 7, 2, 2, 18, 9] — a tabela conta 13 jogos e as fontes trazem 11
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 1º: Nacional-PR tabela [11, 5, 2, 4, 15, 13] jogos [10, 5, 2, 3, 15, 10] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Comercial-PR tabela [10, 8, 2, 0, 18, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Mandaguari tabela [10, 5, 4, 1, 14, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Arapongas FC tabela [10, 5, 2, 3, 20, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Nacional-PR tabela [10, 5, 2, 3, 15, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Londrina tabela [10, 4, 2, 4, 22, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Cambé tabela [10, 3, 4, 3, 19, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Paranavaí tabela [10, 3, 4, 3, 12, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Independente-PR tabela [10, 3, 3, 4, 14, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Astorga tabela [10, 1, 4, 5, 7, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Apucarana tabela [10, 2, 1, 7, 9, 20] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - 2º: Nova Esperança tabela [10, 1, 2, 7, 5, 17] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Comercial-PR tabela [21, 14, 5, 2, 43, 20] jogos [24, 16, 6, 2, 47, 22] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Mandaguari tabela [21, 10, 10, 1, 31, 16] jogos [25, 11, 11, 3, 33, 21] — a tabela conta 21 jogos e as fontes trazem 25
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Paranavaí tabela [21, 10, 6, 5, 30, 23] jogos [24, 11, 6, 7, 42, 26] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Nacional-PR tabela [21, 10, 4, 7, 30, 26] jogos [20, 9, 4, 7, 30, 23] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Arapongas FC tabela [21, 9, 6, 6, 33, 28] jogos [21, 10, 6, 5, 33, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE - FINAL: Portuguesa Londrinense tabela [11, 1, 1, 9, 7, 26] jogos [12, 1, 1, 10, 7, 37] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 1º: Guarani-PR tabela [9, 5, 1, 3, 16, 11] jogos [37, 17, 7, 13, 64, 49] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 1º: Operário-PR tabela [9, 2, 2, 5, 17, 20] jogos [40, 21, 10, 9, 84, 48] — a tabela conta 9 jogos e as fontes trazem 40
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Jacarezinho tabela [9, 8, 0, 1, 24, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Santa Mariana tabela [9, 5, 1, 3, 29, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Tavorense tabela [9, 5, 1, 3, 27, 18] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Pindorama-PR tabela [9, 4, 3, 2, 26, 27] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Guarani-PR tabela [9, 4, 2, 3, 16, 13] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Araucaria/SAP tabela [9, 4, 1, 4, 15, 16] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Operário-PR tabela [9, 4, 1, 4, 18, 22] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Ribeirão Claro tabela [9, 4, 0, 5, 17, 23] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: VII de Setembro tabela [9, 1, 3, 5, 17, 22] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Cambaraense tabela [9, 0, 0, 9, 17, 43] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Guarani-PR tabela [18, 9, 3, 6, 32, 24] jogos [46, 21, 9, 16, 80, 62] — a tabela conta 18 jogos e as fontes trazem 46
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Pindorama-PR tabela [18, 7, 5, 6, 40, 44] jogos [18, 6, 6, 6, 40, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Operário-PR tabela [18, 6, 3, 9, 35, 42] jogos [49, 25, 11, 13, 102, 70] — a tabela conta 18 jogos e as fontes trazem 49
- tabela publicada x jogos — duas primeiras partidas da decisão / ZONA NORTE VELHO - 2º: Cambaraense tabela [18, 1, 3, 14, 26, 61] jogos [18, 1, 4, 13, 26, 61] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Operário-PR tabela [18, 6, 3, 9, 35, 42] jogos [53, 27, 12, 14, 116, 75] — a tabela conta 18 jogos e as fontes trazem 53
- tabela publicada x jogos — Fase final / -: Coritiba tabela [32, 19, 9, 4, 77, 27] jogos [31, 19, 8, 4, 76, 26] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Mandaguari tabela [26, 12, 11, 3, 36, 21] jogos [25, 11, 11, 3, 33, 21] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase final / -: Iraty tabela [28, 16, 4, 8, 47, 34] jogos [28, 15, 4, 9, 47, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Guarani-PR tabela [28, 12, 6, 10, 48, 38] jogos [46, 21, 9, 16, 80, 62] — a tabela conta 28 jogos e as fontes trazem 46
- tabela publicada x jogos — Fase final / -: Nacional-PR tabela [21, 10, 4, 7, 30, 26] jogos [20, 9, 4, 7, 30, 23] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Arapongas FC tabela [21, 9, 6, 6, 33, 28] jogos [21, 10, 6, 5, 33, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Paranavaí tabela [23, 10, 6, 7, 31, 26] jogos [24, 11, 6, 7, 42, 26] — a tabela conta 23 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Pindorama-PR tabela [18, 7, 5, 6, 40, 44] jogos [18, 6, 6, 6, 40, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Seleto tabela [28, 7, 6, 15, 37, 55] jogos [28, 7, 6, 15, 36, 54] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Palestra Itália tabela [27, 3, 2, 22, 25, 71] jogos [27, 4, 2, 21, 25, 71] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Cambaraense tabela [18, 1, 3, 14, 26, 61] jogos [18, 1, 4, 13, 26, 61] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Portuguesa Londrinense tabela [11, 1, 1, 9, 7, 26] jogos [12, 1, 1, 10, 7, 37] — a tabela conta 11 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araucaria/SAP
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambaraense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeirão Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Mariana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tavorense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Olímpico
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Araucaria/SAP — clube que o ogol não tem; entra só pela RSSSF
- Astorga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Astorga)
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambaraense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambaraense)
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente-PR)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Nova Esperança — clube que o ogol não tem; entra só pela RSSSF
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Primavera — clube que o ogol não tem; entra só pela RSSSF
- Ribeirão Claro — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Santa Mariana — clube que o ogol não tem; entra só pela RSSSF
- Seleto — clube que o ogol não tem; entra só pela RSSSF
- Tavorense — clube que o ogol não tem; entra só pela RSSSF
- União Olímpico — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Operário-PR

### 1962

- tabela publicada x jogos — Primeira fase / ZONA SUL - FINAL: Coritiba tabela [28, 19, 6, 3, 72, 34] jogos [31, 21, 6, 4, 76, 39] — a tabela conta 28 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / ZONA SUL - FINAL: Ferroviário-PR tabela [28, 16, 7, 5, 57, 28] jogos [31, 17, 7, 7, 62, 32] — a tabela conta 28 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 1º Turno: Paranavaí tabela [11, 6, 3, 2, 23, 10] jogos [10, 6, 3, 1, 22, 10] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 1º Turno: Nova Esperança tabela [11, 4, 0, 7, 17, 27] jogos [10, 3, 0, 7, 17, 26] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Mandaguari tabela [11, 6, 2, 3, 20, 11] jogos [10, 5, 2, 3, 19, 11] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Grêmio Maringá tabela [11, 6, 1, 4, 21, 17] jogos [10, 5, 1, 4, 20, 17] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Comercial-PR tabela [11, 3, 4, 4, 9, 11] jogos [10, 2, 4, 4, 8, 11] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Paranavaí tabela [11, 5, 0, 6, 20, 20] jogos [10, 4, 0, 6, 19, 20] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Cambé tabela [11, 3, 1, 7, 14, 26] jogos [10, 2, 1, 7, 13, 26] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / ZONA NORTE - 2º Turno: Astorga tabela [11, 0, 0, 11, 4, 23] jogos [6, 0, 0, 6, 4, 18] — a tabela conta 11 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Londrina tabela [26, 17, 6, 3, 52, 27] jogos [25, 16, 6, 3, 50, 26] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Apucarana tabela [26, 13, 8, 5, 54, 40] jogos [25, 13, 8, 4, 53, 38] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Mandaguari tabela [22, 10, 7, 5, 38, 23] jogos [21, 9, 7, 5, 37, 23] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Paranavaí tabela [22, 11, 3, 8, 43, 30] jogos [20, 10, 3, 7, 41, 30] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Comercial-PR tabela [22, 9, 7, 6, 27, 20] jogos [21, 8, 7, 6, 26, 20] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Grêmio Maringá tabela [22, 9, 5, 8, 43, 39] jogos [21, 8, 5, 8, 42, 39] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Cambé tabela [22, 7, 5, 10, 31, 43] jogos [21, 6, 5, 10, 30, 43] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Nova Esperança tabela [22, 5, 3, 14, 30, 48] jogos [21, 4, 3, 14, 30, 47] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Astorga tabela [22, 1, 3, 18, 15, 51] jogos [17, 1, 3, 13, 15, 46] — a tabela conta 22 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / ZONA NORTE VELHO - 1º Turno: Santa Mariana tabela [10, 6, 1, 3, 16, 12] jogos [9, 5, 1, 3, 16, 12] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / ZONA NORTE VELHO - 1º Turno: Araucária tabela [10, 1, 2, 7, 8, 18] jogos [8, 0, 2, 6, 8, 18] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / ZONA NORTE VELHO - 1º Turno: Pindorama-PR tabela [10, 2, 0, 8, 8, 24] jogos [9, 2, 0, 7, 8, 24] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / ZONA NORTE VELHO - 2º Turno: Ribeirão Claro tabela [9, 5, 2, 2, 19, 10] jogos [8, 4, 2, 2, 18, 10] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / ZONA NORTE VELHO - 2º Turno: Tavorense tabela [9, 4, 1, 4, 12, 12] jogos [8, 4, 1, 3, 12, 11] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Santa Mariana tabela [21, 13, 2, 6, 38, 27] jogos [20, 12, 2, 6, 38, 27] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Operário-PR tabela [18, 10, 4, 4, 46, 18] jogos [46, 25, 11, 10, 114, 74] — a tabela conta 18 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Ribeirão Claro tabela [19, 7, 4, 8, 32, 37] jogos [18, 6, 4, 8, 31, 37] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Tavorense tabela [19, 7, 3, 9, 31, 34] jogos [18, 7, 3, 8, 31, 33] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Araucária tabela [19, 3, 2, 14, 16, 45] jogos [17, 2, 2, 13, 16, 45] — a tabela conta 19 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / ZONA NORTE - FINAL: Pindorama-PR tabela [18, 3, 1, 14, 11, 43] jogos [17, 3, 1, 13, 11, 43] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Londrina tabela [30, 20, 7, 3, 67, 35] jogos [29, 19, 7, 3, 65, 34] — a tabela conta 30 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Santa Mariana tabela [21, 13, 2, 6, 38, 27] jogos [20, 12, 2, 6, 38, 27] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Operário-PR tabela [28, 15, 7, 6, 68, 56] jogos [46, 25, 11, 10, 114, 74] — a tabela conta 28 jogos e as fontes trazem 46
- tabela publicada x jogos — Fase final / -: Apucarana tabela [26, 13, 8, 5, 54, 40] jogos [25, 13, 8, 4, 53, 38] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase final / -: Mandaguari tabela [22, 10, 7, 5, 38, 23] jogos [21, 9, 7, 5, 37, 23] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Paranavaí tabela [22, 11, 3, 8, 43, 30] jogos [20, 10, 3, 7, 41, 30] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Comercial-PR tabela [22, 9, 7, 6, 27, 20] jogos [21, 8, 7, 6, 26, 20] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [22, 9, 5, 8, 43, 39] jogos [21, 8, 5, 8, 42, 39] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Ribeirão Claro tabela [19, 7, 4, 8, 32, 37] jogos [18, 6, 4, 8, 31, 37] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Tavorense tabela [19, 7, 3, 9, 31, 34] jogos [18, 7, 3, 8, 31, 33] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Cambé tabela [22, 7, 5, 10, 31, 43] jogos [21, 6, 5, 10, 30, 43] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Nova Esperança tabela [22, 5, 3, 14, 30, 48] jogos [21, 4, 3, 14, 30, 47] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Araucária tabela [19, 3, 2, 14, 16, 45] jogos [17, 2, 2, 13, 16, 45] — a tabela conta 19 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Pindorama-PR tabela [18, 3, 1, 14, 11, 43] jogos [17, 3, 1, 13, 11, 43] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Astorga tabela [22, 1, 3, 18, 15, 51] jogos [17, 1, 3, 13, 15, 46] — a tabela conta 22 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araucária
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambaraense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeirão Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Mariana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sertaneja
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tavorense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VII de Setembro
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Araucária — clube que o ogol não tem; entra só pela RSSSF
- Astorga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Astorga)
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambaraense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambaraense)
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Carlópolis — clube que o ogol não tem; entra só pela RSSSF
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente-PR)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Nova Esperança — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nova Esperança)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Ribeirão Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ribeirão Claro)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Santa Mariana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Mariana)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- Sertaneja — clube que o ogol não tem; entra só pela RSSSF
- Tavorense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tavorense)
- União Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Olímpico)
- VII de Setembro — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1963

- tabela publicada x jogos — 2º Turno / Norte Velho: Cambará tabela [10, 9, 0, 1, 20, 7] jogos [8, 7, 0, 1, 20, 7] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Norte Velho: Santa Mariana tabela [9, 4, 1, 4, 14, 9] jogos [7, 4, 1, 2, 14, 9] — a tabela conta 9 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / Norte Novo: Paranavaí tabela [9, 2, 4, 3, 12, 15] jogos [10, 2, 4, 4, 12, 19] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / Norte Novo: Arapongas FC tabela [10, 5, 3, 2, 19, 9] jogos [9, 5, 2, 2, 19, 9] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Norte Novo: Independente-PR tabela [10, 2, 4, 4, 12, 19] jogos [9, 2, 3, 4, 12, 19] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Norte Novo: Mandaguari tabela [10, 2, 3, 5, 9, 15] jogos [9, 2, 2, 5, 9, 15] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Norte Novo: Comercial-PR tabela [10, 0, 5, 5, 5, 12] jogos [7, 0, 2, 5, 5, 12] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Norte Novo: Arapongas FC tabela [20, 8, 5, 7, 29, 23] jogos [19, 8, 4, 7, 29, 23] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / Norte Novo: Paranavaí tabela [19, 6, 7, 6, 27, 24] jogos [20, 6, 7, 7, 27, 28] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Norte Novo: Mandaguari tabela [20, 7, 5, 8, 24, 26] jogos [19, 7, 4, 8, 24, 26] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / Norte Novo: Comercial-PR tabela [20, 4, 9, 7, 17, 24] jogos [17, 4, 6, 7, 17, 24] — a tabela conta 20 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / Norte Novo: Independente-PR tabela [20, 3, 7, 10, 27, 42] jogos [19, 3, 6, 10, 27, 42] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / Zona Sul: Água Verde tabela [14, 9, 2, 3, 40, 21] jogos [14, 8, 2, 4, 37, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Zona Sul: Rio Branco-PR tabela [14, 8, 3, 3, 34, 21] jogos [14, 8, 3, 3, 32, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Zona Sul: Coritiba tabela [13, 7, 1, 5, 26, 21] jogos [13, 7, 1, 5, 26, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Zona Sul: Iraty tabela [12, 5, 0, 7, 18, 21] jogos [12, 6, 0, 6, 21, 18] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Andiraense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Esperança
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeirão Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Mariana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sertaneja
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uraí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): apucarana
- Andiraense — clube que o ogol não tem; entra só pela RSSSF
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambará — clube que o ogol não tem; entra só pela RSSSF
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente-PR)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Nova Esperança — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nova Esperança)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Platinense — clube que o ogol não tem; entra só pela RSSSF
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Ribeirão Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ribeirão Claro)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Santa Mariana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Mariana)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- Sertaneja — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sertaneja)
- União Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Olímpico)
- Uraí — clube que o ogol não tem; entra só pela RSSSF
- apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1964

- tabela publicada x jogos — Primeira fase / -: Água Verde tabela [9, 4, 3, 2, 18, 12] jogos [8, 4, 3, 1, 17, 10] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Primavera-PR tabela [9, 3, 3, 3, 16, 18] jogos [8, 3, 2, 3, 14, 16] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Seleto tabela [9, 3, 5, 1, 12, 7] jogos [8, 2, 5, 1, 10, 6] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Palestra Itália tabela [9, 2, 2, 5, 11, 19] jogos [8, 2, 1, 5, 9, 17] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Iraty tabela [8, 5, 0, 3, 12, 13] jogos [7, 4, 0, 3, 10, 12] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / -: Caramuru tabela [8, 2, 0, 6, 7, 16] jogos [7, 2, 0, 5, 6, 14] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / -: Guarani-PR tabela [7, 1, 1, 5, 6, 18] jogos [13, 3, 1, 9, 20, 41] — a tabela conta 7 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Seleto tabela [8, 6, 1, 1, 16, 7] jogos [13, 8, 3, 2, 19, 9] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [8, 4, 1, 3, 13, 12] jogos [13, 5, 3, 5, 15, 15] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Guarani-PR tabela [8, 1, 0, 7, 4, 20] jogos [13, 2, 0, 11, 9, 43] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Mandaguari tabela [12, 5, 3, 4, 12, 10] jogos [11, 5, 3, 3, 12, 9] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Jandaia tabela [12, 2, 2, 8, 17, 26] jogos [11, 2, 2, 7, 16, 26] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Guarani-PR tabela [6, 2, 0, 4, 14, 23] jogos [13, 3, 1, 9, 20, 41] — a tabela conta 6 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Pindorama-PR tabela [6, 2, 0, 4, 5, 15] jogos [5, 1, 0, 4, 5, 15] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / -: Guarani-PR tabela [6, 1, 0, 5, 5, 23] jogos [13, 2, 0, 11, 9, 43] — a tabela conta 6 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [33, 22, 6, 5, 47, 19] jogos [29, 19, 5, 5, 64, 22] — a tabela conta 33 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Seleto tabela [33, 12, 12, 9, 22, 15] jogos [29, 14, 11, 4, 44, 24] — a tabela conta 33 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Cambará tabela [18, 12, 2, 4, 19, 15] jogos [15, 12, 2, 1, 59, 13] — a tabela conta 18 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Água Verde tabela [30, 15, 9, 6, 19, 18] jogos [29, 14, 9, 6, 53, 35] — a tabela conta 30 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Ribeirão Claro tabela [15, 8, 2, 5, 10, 18] jogos [15, 9, 2, 4, 44, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: São Paulo-PR tabela [27, 12, 6, 9, 27, 23] jogos [27, 15, 6, 6, 45, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Jacarezinho tabela [12, 8, 2, 2, 2, 4] jogos [12, 8, 2, 2, 46, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Arapongas FC tabela [27, 15, 7, 5, 34, 20] jogos [27, 15, 7, 5, 59, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Londrina tabela [25, 13, 8, 4, 31, 14] jogos [25, 13, 8, 4, 53, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Cambé tabela [25, 13, 7, 5, 22, 24] jogos [25, 11, 7, 7, 50, 32] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Paranavaí tabela [25, 12, 8, 5, 24, 28] jogos [25, 11, 8, 6, 42, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [25, 13, 5, 7, 19, 15] jogos [25, 14, 5, 6, 50, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Primavera-PR tabela [25, 12, 6, 7, 17, 21] jogos [24, 11, 5, 8, 48, 42] — a tabela conta 25 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Rio Branco-PR tabela [25, 12, 6, 7, 23, 22] jogos [25, 10, 6, 9, 49, 41] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Mandaguari tabela [26, 10, 7, 9, 19, 16] jogos [24, 12, 6, 6, 31, 22] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Britânia tabela [25, 11, 5, 9, 14, 12] jogos [25, 10, 5, 10, 34, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Nacional-PR tabela [25, 11, 5, 9, 14, 12] jogos [25, 11, 5, 9, 33, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Caramuru tabela [8, 3, 0, 5, 2, 2] jogos [7, 2, 0, 5, 6, 14] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase final / -: União Olímpico tabela [8, 3, 0, 5, 1, 0] jogos [8, 3, 0, 5, 16, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: XV de Novembro tabela [12, 3, 3, 6, 4, 3] jogos [12, 3, 3, 6, 16, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Guarani-PR tabela [35, 12, 2, 21, 7, 7] jogos [34, 10, 2, 22, 43, 95] — a tabela conta 35 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase final / -: Operário-PR tabela [24, 7, 3, 14, 6, 4] jogos [24, 7, 3, 14, 32, 48] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Iraty tabela [23, 8, 2, 13, 5, 3] jogos [22, 10, 2, 10, 29, 38] — a tabela conta 23 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Comercial-PR tabela [13, 3, 3, 7, 5, 2] jogos [13, 2, 3, 8, 11, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: VII de Setembro tabela [12, 3, 1, 8, 4, 5] jogos [12, 2, 1, 9, 11, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Palestra Itália tabela [9, 2, 2, 5, 11, 19] jogos [8, 2, 1, 5, 9, 17] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Pindorama-PR tabela [12, 3, 0, 9, 5, 2] jogos [11, 2, 0, 9, 13, 38] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Astorga tabela [25, 4, 4, 17, 14, 38] jogos [25, 2, 4, 19, 19, 61] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Jandaia tabela [25, 4, 4, 17, 17, 27] jogos [24, 3, 4, 17, 25, 65] — a tabela conta 25 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Bela Vista-PR tabela [25, 3, 2, 20, 14, 30] jogos [25, 3, 2, 20, 21, 66] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Estrela do Norte-PR tabela [25, 2, 4, 19, 18, 31] jogos [25, 3, 4, 18, 23, 55] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bela Vista
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bloco Morgenau
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela do Norte
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GERA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani FC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani SC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pindorama
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeiráo Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeirão Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VII de Setembro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): XV de Novembro
- Astorga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Astorga)
- Bela Vista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bela Vista-PR)
- Bloco Morgenau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bloco Morgenau)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambará)
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Estrela do Norte — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estrela do Norte-PR)
- GERA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gera)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Guarani FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Guarani SC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Jandaia — clube que o ogol não tem; entra só pela RSSSF
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pindorama — clube que o ogol não tem; entra só pela RSSSF
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Ribeiráo Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ribeirão Claro)
- Ribeirão Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ribeirão Claro)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- São Paulo — clube que o ogol não tem; entra só pela RSSSF
- União Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Olímpico)
- VII de Setembro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (VII de Setembro)
- XV de Novembro — clube que o ogol não tem; entra só pela RSSSF
- vencedor da final pelos jogos (Cambará) diferente do campeão oficial (Grêmio Maringá); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Seleto

### 1965

- tabela publicada x jogos — Primeira fase / -: Grêmio Maringá tabela [16, 11, 2, 3, 43, 12] jogos [14, 10, 1, 3, 43, 12] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Ribeirão Claro tabela [16, 3, 2, 11, 14, 33] jogos [15, 3, 2, 10, 14, 33] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Estrela do Norte-PR tabela [16, 1, 5, 10, 12, 25] jogos [17, 1, 6, 10, 12, 25] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Segunda fase / -: União Bandeirante tabela [16, 10, 3, 3, 34, 15] jogos [15, 9, 3, 3, 34, 15] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Arapongas FC tabela [16, 5, 3, 8, 22, 31] jogos [15, 4, 3, 8, 22, 31] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Comercial-PR tabela [16, 3, 2, 11, 24, 37] jogos [14, 3, 2, 9, 24, 37] — a tabela conta 16 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Grêmio Maringá tabela [32, 25, 3, 4, 89, 26] jogos [32, 24, 2, 6, 89, 29] — placar diverge entre RSSSF e ogol em Ferroviário-PR x Grêmio Maringá (2-0 x 3-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / -: União Bandeirante tabela [32, 21, 3, 8, 70, 37] jogos [31, 20, 3, 8, 70, 37] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Segunda fase / -: Arapongas FC tabela [32, 15, 6, 11, 52, 45] jogos [31, 14, 6, 11, 52, 45] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Segunda fase / -: Estrela do Norte-PR tabela [32, 6, 7, 19, 41, 55] jogos [33, 6, 8, 19, 41, 55] — a tabela conta 32 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Comercial-PR tabela [32, 6, 2, 24, 43, 84] jogos [30, 6, 2, 22, 43, 84] — a tabela conta 32 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: Ribeirão Claro tabela [32, 5, 5, 22, 31, 75] jogos [31, 5, 5, 21, 31, 75] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Segunda fase / ZONA SUL: Ferroviário-PR tabela [24, 14, 7, 3, 57, 29] jogos [23, 13, 7, 3, 55, 29] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / ZONA SUL: União Olímpico tabela [24, 2, 7, 15, 21, 53] jogos [23, 2, 7, 14, 21, 51] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Desempate do rebaixamento / -: Ferroviário-PR tabela [26, 15, 8, 3, 57, 29] jogos [27, 16, 8, 3, 60, 30] — a tabela conta 26 jogos e as fontes trazem 27
- tabela publicada x jogos — Desempate do rebaixamento / -: Coritiba tabela [26, 15, 6, 5, 50, 23] jogos [26, 15, 6, 5, 51, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Desempate do rebaixamento / -: União Olímpico tabela [24, 2, 7, 15, 21, 53] jogos [23, 2, 7, 14, 21, 51] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Final / -: Ferroviário-PR tabela [28, 17, 8, 3, 60, 29] jogos [27, 16, 8, 3, 60, 30] — a tabela conta 28 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: União Bandeirante tabela [32, 21, 3, 8, 70, 37] jogos [31, 20, 3, 8, 70, 37] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Final / -: Coritiba tabela [26, 15, 6, 5, 50, 23] jogos [26, 15, 6, 5, 51, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Arapongas FC tabela [32, 15, 6, 11, 52, 45] jogos [31, 14, 6, 11, 52, 45] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Final / -: Estrela do Norte-PR tabela [32, 6, 7, 19, 41, 55] jogos [33, 6, 8, 19, 41, 55] — a tabela conta 32 jogos e as fontes trazem 33
- tabela publicada x jogos — Final / -: Ribeirão Claro tabela [32, 5, 5, 22, 31, 75] jogos [31, 5, 5, 21, 31, 75] — a tabela conta 32 jogos e as fontes trazem 31
- tabela publicada x jogos — Final / -: União Olímpico tabela [24, 2, 7, 15, 21, 53] jogos [23, 2, 7, 14, 21, 51] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Final / -: Comercial-PR tabela [32, 6, 2, 24, 43, 84] jogos [30, 6, 2, 22, 43, 84] — a tabela conta 32 jogos e as fontes trazem 30
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela do Norte
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacarezinho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mandaguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ribeirão Claro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Olímpico
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Cambará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambará)
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Estrela do Norte — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estrela do Norte-PR)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-PR)
- Jacarezinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacarezinho)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mandaguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mandaguari)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Ribeirão Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ribeirão Claro)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Paulo-PR)
- União Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Olímpico)
- placar diferente no ogol — Ferroviário-PR x Grêmio Maringá (1966-03-20): RSSSF 2-0, ogol 3-1; fica o da RSSSF
- só na RSSSF (não achado no ogol): Grêmio Maringá 4-0 CAFE (1965-05-01)
- só na RSSSF (não achado no ogol): Arapongas FC 0-0 Cambará (1965-05-02)
- só na RSSSF (não achado no ogol): Cambé 2-2 Estrela do Norte-PR (1965-05-02)
- só na RSSSF (não achado no ogol): Jacarezinho 4-0 Apucarana (1965-05-02)
- só na RSSSF (não achado no ogol): Mandaguari 1-0 Jandaia (1965-05-02)
- só na RSSSF (não achado no ogol): Paranavaí 4-0 Comercial-PR (1965-05-02)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-1 Londrina (1965-05-02)
- só na RSSSF (não achado no ogol): São Paulo-PR 3-0 Nacional-PR (1965-05-02)
- só na RSSSF (não achado no ogol): Apucarana 6-0 CAFE (1965-05-09)
- só na RSSSF (não achado no ogol): Cambará 3-1 Mandaguari (1965-05-09)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 1-2 Arapongas FC (1965-05-09)
- só na RSSSF (não achado no ogol): Jandaia 1-0 São Paulo-PR (1965-05-09)
- só na RSSSF (não achado no ogol): Londrina 3-1 Jacarezinho (1965-05-09)
- só na RSSSF (não achado no ogol): Nacional-PR 4-0 Comercial-PR (1965-05-09)
- só na RSSSF (não achado no ogol): Paranavaí 0-2 Grêmio Maringá (1965-05-09)
- só na RSSSF (não achado no ogol): União Bandeirante 4-0 Ribeirão Claro (1965-05-09)
- só na RSSSF (não achado no ogol): Arapongas FC 0-0 Cambé (1965-05-16)
- só na RSSSF (não achado no ogol): CAFE 2-3 Londrina (1965-05-16)
- só na RSSSF (não achado no ogol): Comercial-PR 3-1 Jandaia (1965-05-16)
- só na RSSSF (não achado no ogol): Jacarezinho 2-3 União Bandeirante (1965-05-16)
- só na RSSSF (não achado no ogol): Mandaguari 2-0 Estrela do Norte-PR (1965-05-16)
- só na RSSSF (não achado no ogol): Paranavaí 2-1 Apucarana (1965-05-16)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-0 Cambará (1965-05-16)
- só na RSSSF (não achado no ogol): Ribeirão Claro 0-3 Jacarezinho (1965-05-23)
- só na RSSSF (não achado no ogol): Apucarana 2-0 Nacional-PR (1965-05-23)
- só na RSSSF (não achado no ogol): Cambará 3-0 Comercial-PR (1965-05-23)
- só na RSSSF (não achado no ogol): Cambé 4-1 Mandaguari (1965-05-23)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 1-1 São Paulo-PR (1965-05-23)
- só na RSSSF (não achado no ogol): Jandaia 1-0 Grêmio Maringá (1965-05-23)
- só na RSSSF (não achado no ogol): Londrina 2-1 Paranavaí (1965-05-23)
- só na RSSSF (não achado no ogol): União Bandeirante 2-0 CAFE (1965-05-23)
- só na RSSSF (não achado no ogol): CAFE 4-0 Ribeirão Claro (1965-05-30)
- só na RSSSF (não achado no ogol): Comercial-PR 2-1 Estrela do Norte-PR (1965-05-30)
- só na RSSSF (não achado no ogol): Grêmio Maringá 7-0 Cambará (1965-05-30)
- só na RSSSF (não achado no ogol): Jandaia 0-1 Apucarana (1965-05-30)
- só na RSSSF (não achado no ogol): Mandaguari 1-2 Arapongas FC (1965-05-30)
- só na RSSSF (não achado no ogol): Nacional-PR 2-2 Londrina (1965-05-30)
- só na RSSSF (não achado no ogol): Paranavaí 2-1 União Bandeirante (1965-05-30)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-0 Cambé (1965-05-30)
- só na RSSSF (não achado no ogol): Arapongas FC 1-0 São Paulo-PR (1965-06-06)
- só na RSSSF (não achado no ogol): Cambará 4-1 Apucarana (1965-06-06)
- só na RSSSF (não achado no ogol): Cambé 3-1 Comercial-PR (1965-06-06)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 1-2 Grêmio Maringá (1965-06-06)
- só na RSSSF (não achado no ogol): Jacarezinho 1-0 CAFE (1965-06-06)
- só na RSSSF (não achado no ogol): Londrina 4-0 Jandaia (1965-06-06)
- só na RSSSF (não achado no ogol): Ribeirão Claro 3-1 Paranavaí (1965-06-06)
- só na RSSSF (não achado no ogol): União Bandeirante 3-1 Nacional-PR (1965-06-06)
- só na RSSSF (não achado no ogol): Apucarana 4-2 Estrela do Norte-PR (1965-06-13)
- só na RSSSF (não achado no ogol): Cambará 1-1 Londrina (1965-06-13)
- só na RSSSF (não achado no ogol): Comercial-PR 2-3 Arapongas FC (1965-06-13)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 Cambé (1965-06-13)
- só na RSSSF (não achado no ogol): Jandaia 2-1 União Bandeirante (1965-06-13)
- só na RSSSF (não achado no ogol): Nacional-PR 3-0 Ribeirão Claro (1965-06-13)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 Jacarezinho (1965-06-13)
- só na RSSSF (não achado no ogol): São Paulo-PR 7-0 Mandaguari (1965-06-13)
- só na RSSSF (não achado no ogol): Arapongas FC 1-0 Grêmio Maringá (1965-06-20)
- só na RSSSF (não achado no ogol): Cambé 0-1 Apucarana (1965-06-20)
- só na RSSSF (não achado no ogol): CAFE 1-5 Paranavaí (1965-06-20)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 0-1 Londrina (1965-06-20)
- só na RSSSF (não achado no ogol): Jacarezinho 5-3 Nacional-PR (1965-06-20)
- só na RSSSF (não achado no ogol): Mandaguari 1-0 Comercial-PR (1965-06-20)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-2 Jandaia (1965-06-20)
- só na RSSSF (não achado no ogol): União Bandeirante 1-2 Cambará (1965-06-20)
- só na RSSSF (não achado no ogol): Comercial-PR 1-5 São Paulo-PR (1965-06-27)
- só na RSSSF (não achado no ogol): Apucarana 2-0 Arapongas FC (1965-06-27)
- só na RSSSF (não achado no ogol): Cambará 2-1 Ribeirão Claro (1965-06-27)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 0-4 União Bandeirante (1965-06-27)
- só na RSSSF (não achado no ogol): Grêmio Maringá 8-1 Mandaguari (1965-06-27)
- só na RSSSF (não achado no ogol): Jandaia 1-1 Jacarezinho (1965-06-27)
- só na RSSSF (não achado no ogol): Londrina 2-0 Cambé (1965-06-27)
- só na RSSSF (não achado no ogol): Nacional-PR 0-0 CAFE (1965-06-27)
- só na RSSSF (não achado no ogol): Arapongas FC 0-0 Londrina (1965-07-04)
- só na RSSSF (não achado no ogol): Cambé 2-5 União Bandeirante (1965-07-04)
- só na RSSSF (não achado no ogol): CAFE 2-1 Jandaia (1965-07-04)
- só na RSSSF (não achado no ogol): Jacarezinho 4-1 Cambará (1965-07-04)
- só na RSSSF (não achado no ogol): Mandaguari 2-1 Apucarana (1965-07-04)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 Nacional-PR (1965-07-04)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-1 Estrela do Norte-PR (1965-07-04)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-3 Grêmio Maringá (1965-07-04)
- só na RSSSF (não achado no ogol): Apucarana 7-1 São Paulo-PR (1965-07-11)
- só na RSSSF (não achado no ogol): Cambará 3-2 CAFE (1965-07-11)
- só na RSSSF (não achado no ogol): Cambé 2-0 Ribeirão Claro (1965-07-11)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 2-0 Jacarezinho (1965-07-11)
- só na RSSSF (não achado no ogol): Grêmio Maringá 6-1 Comercial-PR (1965-07-11)
- só na RSSSF (não achado no ogol): Jandaia 2-1 Paranavaí (1965-07-11)
- só na RSSSF (não achado no ogol): Londrina 1-0 Mandaguari (1965-07-11)
- só na RSSSF (não achado no ogol): União Bandeirante 0-4 Arapongas FC (1965-07-11)
- só na RSSSF (não achado no ogol): Arapongas FC 4-0 Ribeirão Claro (1965-07-18)
- só na RSSSF (não achado no ogol): CAFE 1-0 Estrela do Norte-PR (1965-07-18)
- só na RSSSF (não achado no ogol): Comercial-PR 0-2 Apucarana (1965-07-18)
- só na RSSSF (não achado no ogol): Jacarezinho 4-2 Cambé (1965-07-18)
- só na RSSSF (não achado no ogol): Mandaguari 1-2 União Bandeirante (1965-07-18)
- só na RSSSF (não achado no ogol): Nacional-PR 0-1 Jandaia (1965-07-18)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 Cambará (1965-07-18)
- só na RSSSF (não achado no ogol): São Paulo-PR 0-0 Londrina (1965-07-18)
- só na RSSSF (não achado no ogol): Apucarana 2-4 Grêmio Maringá (1965-07-25)
- só na RSSSF (não achado no ogol): Arapongas FC 1-0 Jacarezinho (1965-07-25)
- só na RSSSF (não achado no ogol): Cambará 3-0 Nacional-PR (1965-07-25)
- só na RSSSF (não achado no ogol): Cambé 0-1 CAFE (1965-07-25)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 0-1 Paranavaí (1965-07-25)
- só na RSSSF (não achado no ogol): Londrina 5-3 Comercial-PR (1965-07-25)
- só na RSSSF (não achado no ogol): Ribeirão Claro 0-1 Mandaguari (1965-07-25)
- só na RSSSF (não achado no ogol): União Bandeirante 2-1 São Paulo-PR (1965-07-25)
- só na RSSSF (não achado no ogol): CAFE 2-1 Arapongas FC (1965-08-01)
- só na RSSSF (não achado no ogol): Comercial-PR 2-3 União Bandeirante (1965-08-01)
- só na RSSSF (não achado no ogol): Grêmio Maringá 1-1 Londrina (1965-08-01)
- só na RSSSF (não achado no ogol): Jacarezinho 2-0 Mandaguari (1965-08-01)
- só na RSSSF (não achado no ogol): Jandaia 1-0 Cambará (1965-08-01)
- só na RSSSF (não achado no ogol): Nacional-PR 0-0 Estrela do Norte-PR (1965-08-01)
- só na RSSSF (não achado no ogol): Paranavaí 2-2 Cambé (1965-08-01)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-1 Ribeirão Claro (1965-08-01)
- só na RSSSF (não achado no ogol): Arapongas FC 6-1 Paranavaí (1965-08-08)
- só na RSSSF (não achado no ogol): Cambé 3-2 Nacional-PR (1965-08-08)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 1-1 Jandaia (1965-08-08)
- só na RSSSF (não achado no ogol): Jacarezinho 1-0 São Paulo-PR (1965-08-08)
- só na RSSSF (não achado no ogol): Londrina 1-1 Apucarana (1965-08-08)
- só na RSSSF (não achado no ogol): Mandaguari 2-2 CAFE (1965-08-08)
- só na RSSSF (não achado no ogol): Ribeirão Claro 3-2 Comercial-PR (1965-08-08)
- só na RSSSF (não achado no ogol): União Bandeirante 2-1 Grêmio Maringá (1965-08-08)
- só na RSSSF (não achado no ogol): Apucarana 2-1 União Bandeirante (1965-08-15)
- só na RSSSF (não achado no ogol): Cambará 1-0 Estrela do Norte-PR (1965-08-15)
- só na RSSSF (não achado no ogol): Comercial-PR 1-0 Jacarezinho (1965-08-15)
- só na RSSSF (não achado no ogol): Jandaia 2-0 Cambé (1965-08-15)
- só na RSSSF (não achado no ogol): Nacional-PR 0-3 Arapongas FC (1965-08-15)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 Mandaguari (1965-08-15)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-1 CAFE (1965-08-15)
- só na RSSSF (não achado no ogol): Ribeirão Claro 3-1 Apucarana (1965-08-22)
- só na RSSSF (não achado no ogol): Cambé 3-1 Cambará (1965-08-22)
- só na RSSSF (não achado no ogol): CAFE 3-1 Comercial-PR (1965-08-22)
- só na RSSSF (não achado no ogol): Jacarezinho 0-0 Estrela do Norte-PR (1965-08-22)
- só na RSSSF (não achado no ogol): Arapongas FC 2-5 Jandaia (1965-08-22)
- só na RSSSF (não achado no ogol): União Bandeirante 2-0 Londrina (1965-08-22)
- só na RSSSF (não achado no ogol): Mandaguari 2-2 Nacional-PR (1965-08-22)
- só na RSSSF (não achado no ogol): São Paulo-PR 3-2 Paranavaí (1965-08-22)
- só na RSSSF (não achado no ogol): Nacional-PR 0-3 Grêmio Maringá (1965-08-22)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 2-3 Cambé (1965-08-29)
- só na RSSSF (não achado no ogol): Londrina 5-0 Ribeirão Claro (1965-08-29)
- só na RSSSF (não achado no ogol): Cambará 5-5 Arapongas FC (1965-08-29)
- só na RSSSF (não achado no ogol): Apucarana 3-0 Jacarezinho (1965-08-29)
- só na RSSSF (não achado no ogol): Jandaia 1-0 Mandaguari (1965-08-29)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 CAFE (1965-08-29)
- só na RSSSF (não achado no ogol): Nacional-PR 4-1 São Paulo-PR (1965-08-29)
- só na RSSSF (não achado no ogol): Comercial-PR 1-2 Paranavaí (1965-08-29)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-3 União Bandeirante (1965-09-05)
- só na RSSSF (não achado no ogol): Arapongas FC 3-1 Estrela do Norte-PR (1965-09-05)
- só na RSSSF (não achado no ogol): Jacarezinho 1-1 Londrina (1965-09-05)
- só na RSSSF (não achado no ogol): Mandaguari 2-4 Cambará (1965-09-05)
- só na RSSSF (não achado no ogol): CAFE 3-1 Apucarana (1965-09-05)
- só na RSSSF (não achado no ogol): São Paulo-PR 4-1 Jandaia (1965-09-05)
- só na RSSSF (não achado no ogol): Paranavaí 1-3 Grêmio Maringá (1965-09-05)
- só na RSSSF (não achado no ogol): Comercial-PR 3-3 Nacional-PR (1965-09-05)
- só na RSSSF (não achado no ogol): Cambé 0-2 Arapongas FC (1965-09-12)
- só na RSSSF (não achado no ogol): União Bandeirante 7-0 Jacarezinho (1965-09-12)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 5-0 Mandaguari (1965-09-12)
- só na RSSSF (não achado no ogol): Londrina 2-1 CAFE (1965-09-12)
- só na RSSSF (não achado no ogol): Cambará 2-1 São Paulo-PR (1965-09-12)
- só na RSSSF (não achado no ogol): Apucarana 2-0 Paranavaí (1965-09-12)
- só na RSSSF (não achado no ogol): Jandaia 2-0 Comercial-PR (1965-09-12)
- só na RSSSF (não achado no ogol): Grêmio Maringá 5-1 Nacional-PR (1965-09-12)
- só na RSSSF (não achado no ogol): Jacarezinho 4-0 Ribeirão Claro (1965-09-19)
- só na RSSSF (não achado no ogol): Mandaguari 0-0 Cambé (1965-09-19)
- só na RSSSF (não achado no ogol): CAFE 2-0 União Bandeirante (1965-09-19)
- só na RSSSF (não achado no ogol): São Paulo-PR 3-0 Estrela do Norte-PR (1965-09-19)
- só na RSSSF (não achado no ogol): Paranavaí 0-0 Londrina (1965-09-19)
- só na RSSSF (não achado no ogol): Comercial-PR 1-5 Cambará (1965-09-19)
- só na RSSSF (não achado no ogol): Nacional-PR 3-1 Apucarana (1965-09-19)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 Jandaia (1965-09-19)
- só na RSSSF (não achado no ogol): Arapongas FC 3-1 Mandaguari (1965-09-26)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-1 CAFE (1965-09-26)
- só na RSSSF (não achado no ogol): Cambé 1-2 São Paulo-PR (1965-09-26)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 2-0 Comercial-PR (1965-09-26)
- só na RSSSF (não achado no ogol): Londrina 5-0 Nacional-PR (1965-09-26)
- só na RSSSF (não achado no ogol): Cambará 1-3 Grêmio Maringá (1965-09-26)
- só na RSSSF (não achado no ogol): Apucarana 2-1 Jandaia (1965-09-26)
- só na RSSSF (não achado no ogol): CAFE 4-0 Jacarezinho (1965-10-02)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-0 Arapongas FC (1965-10-02)
- só na RSSSF (não achado no ogol): Paranavaí 5-2 Ribeirão Claro (1965-10-02)
- só na RSSSF (não achado no ogol): Nacional-PR 1-3 União Bandeirante (1965-10-02)
- só na RSSSF (não achado no ogol): Comercial-PR 2-2 Cambé (1965-10-02)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 Estrela do Norte-PR (1965-10-02)
- só na RSSSF (não achado no ogol): Jandaia 2-0 Londrina (1965-10-02)
- só na RSSSF (não achado no ogol): Apucarana 3-0 Cambará (1965-10-02)
- só na RSSSF (não achado no ogol): Mandaguari 0-2 São Paulo-PR (1965-10-10)
- só na RSSSF (não achado no ogol): Jacarezinho 2-2 Paranavaí (1965-10-10)
- só na RSSSF (não achado no ogol): Ribeirão Claro 0-0 Nacional-PR (1965-10-10)
- só na RSSSF (não achado no ogol): Cambé 2-2 Grêmio Maringá (1965-10-10)
- só na RSSSF (não achado no ogol): União Bandeirante 3-1 Jandaia (1965-10-10)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 2-2 Apucarana (1965-10-10)
- só na RSSSF (não achado no ogol): Londrina 5-1 Cambará (1965-10-10)
- só na RSSSF (não achado no ogol): Paranavaí 2-1 CAFE (1965-10-17)
- só na RSSSF (não achado no ogol): Comercial-PR 6-1 Mandaguari (1965-10-17)
- só na RSSSF (não achado no ogol): Nacional-PR 1-3 Jacarezinho (1965-10-17)
- só na RSSSF (não achado no ogol): Grêmio Maringá 5-0 Arapongas FC (1965-10-17)
- só na RSSSF (não achado no ogol): Jandaia 4-4 Ribeirão Claro (1965-10-17)
- só na RSSSF (não achado no ogol): Apucarana 1-0 Cambé (1965-10-17)
- só na RSSSF (não achado no ogol): Cambará 0-2 União Bandeirante (1965-10-17)
- só na RSSSF (não achado no ogol): Londrina 2-2 Estrela do Norte-PR (1965-10-17)
- só na RSSSF (não achado no ogol): São Paulo-PR 5-0 Comercial-PR (1965-10-24)
- só na RSSSF (não achado no ogol): CAFE 0-0 Nacional-PR (1965-10-24)
- só na RSSSF (não achado no ogol): Mandaguari 0-2 Grêmio Maringá (1965-10-24)
- só na RSSSF (não achado no ogol): Jacarezinho 1-0 Jandaia (1965-10-24)
- só na RSSSF (não achado no ogol): Arapongas FC 0-1 Apucarana (1965-10-24)
- só na RSSSF (não achado no ogol): Ribeirão Claro 0-2 Cambará (1965-10-24)
- só na RSSSF (não achado no ogol): Cambé 1-2 Londrina (1965-10-24)
- só na RSSSF (não achado no ogol): União Bandeirante 2-1 Estrela do Norte-PR (1965-10-24)
- só na RSSSF (não achado no ogol): Nacional-PR 0-1 Paranavaí (1965-10-31)
- só na RSSSF (não achado no ogol): Grêmio Maringá 4-0 São Paulo-PR (1965-10-31)
- só na RSSSF (não achado no ogol): Jandaia 2-0 CAFE (1965-10-31)
- só na RSSSF (não achado no ogol): Apucarana 4-1 Mandaguari (1965-10-31)
- só na RSSSF (não achado no ogol): Cambará 1-2 Jacarezinho (1965-10-31)
- só na RSSSF (não achado no ogol): Londrina 4-1 Arapongas FC (1965-10-31)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 3-1 Ribeirão Claro (1965-10-31)
- só na RSSSF (não achado no ogol): União Bandeirante 1-1 Cambé (1965-10-31)
- só na RSSSF (não achado no ogol): Comercial-PR 0-2 Grêmio Maringá (1965-11-07)
- só na RSSSF (não achado no ogol): São Paulo-PR 4-0 Apucarana (1965-11-07)
- só na RSSSF (não achado no ogol): CAFE 2-0 Cambará (1965-11-07)
- só na RSSSF (não achado no ogol): Mandaguari 2-2 Londrina (1965-11-07)
- só na RSSSF (não achado no ogol): Jacarezinho 3-0 Estrela do Norte-PR (1965-11-07)
- só na RSSSF (não achado no ogol): Arapongas FC 2-2 União Bandeirante (1965-11-07)
- só na RSSSF (não achado no ogol): Ribeirão Claro 3-0 Cambé (1965-11-07)
- só na RSSSF (não achado no ogol): Jandaia 0-0 Nacional-PR (1965-11-14)
- só na RSSSF (não achado no ogol): Apucarana 5-3 Comercial-PR (1965-11-14)
- só na RSSSF (não achado no ogol): Cambará 3-2 Paranavaí (1965-11-14)
- só na RSSSF (não achado no ogol): Londrina 1-0 São Paulo-PR (1965-11-14)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 4-2 CAFE (1965-11-14)
- só na RSSSF (não achado no ogol): União Bandeirante 3-0 Mandaguari (1965-11-14)
- só na RSSSF (não achado no ogol): Cambé 0-0 Jacarezinho (1965-11-14)
- só na RSSSF (não achado no ogol): Ribeirão Claro 1-0 Arapongas FC (1965-11-14)
- só na RSSSF (não achado no ogol): Grêmio Maringá 4-0 Apucarana (1965-11-21)
- só na RSSSF (não achado no ogol): Nacional-PR 0-0 Cambará (1965-11-21)
- só na RSSSF (não achado no ogol): Comercial-PR 0-2 Londrina (1965-11-21)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 Estrela do Norte-PR (1965-11-21)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-0 União Bandeirante (1965-11-21)
- só na RSSSF (não achado no ogol): CAFE 1-1 Cambé (1965-11-21)
- só na RSSSF (não achado no ogol): Mandaguari 4-1 Ribeirão Claro (1965-11-21)
- só na RSSSF (não achado no ogol): Jacarezinho 3-0 Arapongas FC (1965-11-21)
- só na RSSSF (não achado no ogol): Cambará 4-2 Jandaia (1965-11-28)
- só na RSSSF (não achado no ogol): Londrina 1-0 Grêmio Maringá (1965-11-28)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 3-0 Nacional-PR (1965-11-28)
- só na RSSSF (não achado no ogol): Cambé 1-0 Paranavaí (1965-11-28)
- só na RSSSF (não achado no ogol): Ribeirão Claro 0-1 São Paulo-PR (1965-11-28)
- só na RSSSF (não achado no ogol): Arapongas FC 1-2 CAFE (1965-11-28)
- só na RSSSF (não achado no ogol): Jacarezinho 5-0 Mandaguari (1965-11-28)
- só na RSSSF (não achado no ogol): Apucarana 3-0 Londrina (1965-12-05)
- só na RSSSF (não achado no ogol): Jandaia 3-2 Estrela do Norte-PR (1965-12-05)
- só na RSSSF (não achado no ogol): Grêmio Maringá 3-2 União Bandeirante (1965-12-05)
- só na RSSSF (não achado no ogol): Nacional-PR 1-4 Cambé (1965-12-05)
- só na RSSSF (não achado no ogol): Comercial-PR 4-1 Ribeirão Claro (1965-12-05)
- só na RSSSF (não achado no ogol): Paranavaí 3-1 Arapongas FC (1965-12-05)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-0 Jacarezinho (1965-12-05)
- só na RSSSF (não achado no ogol): CAFE 9-0 Mandaguari (1965-12-05)
- só na RSSSF (não achado no ogol): Paranavaí 1-4 União Bandeirante (1965-12-08)
- só na RSSSF (não achado no ogol): Estrela do Norte-PR 1-2 Cambará (1965-12-12)
- só na RSSSF (não achado no ogol): União Bandeirante 1-1 Apucarana (1965-12-12)
- só na RSSSF (não achado no ogol): Cambé 3-1 Jandaia (1965-12-12)
- só na RSSSF (não achado no ogol): Ribeirão Claro 2-5 Grêmio Maringá (1965-12-12)
- só na RSSSF (não achado no ogol): Arapongas FC 3-0 Nacional-PR (1965-12-12)
- só na RSSSF (não achado no ogol): Jacarezinho 4-1 Comercial-PR (1965-12-12)
- só na RSSSF (não achado no ogol): Mandaguari 2-2 Paranavaí (1965-12-12)
- só na RSSSF (não achado no ogol): CAFE 0-2 São Paulo-PR (1965-12-12)
- só na RSSSF (não achado no ogol): Londrina 0-1 União Bandeirante (1965-12-19)
- só na RSSSF (não achado no ogol): Cambará 5-2 Cambé (1965-12-19)
- só na RSSSF (não achado no ogol): Apucarana 1-0 Ribeirão Claro (1965-12-19)
- só na RSSSF (não achado no ogol): Jandaia 1-1 Arapongas FC (1965-12-19)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 Jacarezinho (1965-12-19)
- só na RSSSF (não achado no ogol): Nacional-PR 1-1 Mandaguari (1965-12-19)
- só na RSSSF (não achado no ogol): Comercial-PR 3-1 CAFE (1965-12-19)
- só na RSSSF (não achado no ogol): Paranavaí 2-0 São Paulo-PR (1965-12-19)
- só na RSSSF (não achado no ogol): Paranavaí 2-1 Jandaia (1966-01-01)
- só na RSSSF (não achado no ogol): Palestra Itália 0-3 Athletico-PR (1966-05-08)
- só na RSSSF (não achado no ogol): Coritiba 2-2 Operário-PR (1966-05-09)
- só na RSSSF (não achado no ogol): Guarani-PR 3-2 Seleto (1966-05-09)
- só na RSSSF (não achado no ogol): Rio Branco-PR 2-1 Primavera-PR (1966-05-09)
- só na RSSSF (não achado no ogol): Água Verde 3-0 União Olímpico (1966-05-09)
- só na RSSSF (não achado no ogol): Caramuru 1-2 Ferroviário-PR (1966-05-09)
- só na RSSSF (não achado no ogol): Athletico-PR 6-1 Caramuru (1966-05-15)
- só na RSSSF (não achado no ogol): Primavera-PR 3-0 Guarani-PR (1966-05-16)
- só na RSSSF (não achado no ogol): Operário-PR 1-2 Britânia (1966-05-16)
- só na RSSSF (não achado no ogol): Seleto 5-1 Palestra Itália (1966-05-16)
- só na RSSSF (não achado no ogol): União Olímpico 0-2 Coritiba (1966-05-16)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-1 Rio Branco-PR (1966-05-16)
- só na RSSSF (não achado no ogol): Britânia 0-1 Seleto (1966-05-22)
- só na RSSSF (não achado no ogol): Palestra Itália 2-2 União Olímpico (1966-05-23)
- só na RSSSF (não achado no ogol): Coritiba 2-3 Primavera-PR (1966-05-23)
- só na RSSSF (não achado no ogol): Guarani-PR 4-5 Ferroviário-PR (1966-05-23)
- só na RSSSF (não achado no ogol): Rio Branco-PR 3-0 Operário-PR (1966-05-23)
- só na RSSSF (não achado no ogol): Caramuru 0-5 Água Verde (1966-05-23)
- só na RSSSF (não achado no ogol): Primavera-PR 1-2 Palestra Itália (1966-05-27)
- só na RSSSF (não achado no ogol): Água Verde 1-0 Rio Branco-PR (1966-05-29)
- só na RSSSF (não achado no ogol): União Olímpico 1-2 Caramuru (1966-05-30)
- só na RSSSF (não achado no ogol): Operário-PR 2-4 Athletico-PR (1966-05-30)
- só na RSSSF (não achado no ogol): Ferroviário-PR 0-0 Britânia (1966-05-30)
- só na RSSSF (não achado no ogol): Seleto 2-1 Coritiba (1966-05-30)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-2 Palestra Itália (1966-06-05)
- só na RSSSF (não achado no ogol): Athletico-PR 2-2 Seleto (1966-06-06)
- só na RSSSF (não achado no ogol): Rio Branco-PR 4-0 União Olímpico (1966-06-06)
- só na RSSSF (não achado no ogol): Caramuru 1-3 Guarani-PR (1966-06-06)
- só na RSSSF (não achado no ogol): Operário-PR 1-1 Primavera-PR (1966-06-06)
- só na RSSSF (não achado no ogol): Britânia 3-2 Água Verde (1966-06-06)
- só na RSSSF (não achado no ogol): Coritiba 5-0 Palestra Itália (1966-06-19)
- só na RSSSF (não achado no ogol): Britânia 3-0 Caramuru (1966-06-19)
- só na RSSSF (não achado no ogol): Primavera-PR 2-0 União Olímpico (1966-06-20)
- só na RSSSF (não achado no ogol): Seleto 0-0 Rio Branco-PR (1966-06-20)
- só na RSSSF (não achado no ogol): Athletico-PR 3-1 Guarani-PR (1966-06-20)
- só na RSSSF (não achado no ogol): Operário-PR 1-2 Água Verde (1966-06-20)
- só na RSSSF (não achado no ogol): Palestra Itália 1-1 Água Verde (1966-06-26)
- só na RSSSF (não achado no ogol): Guarani-PR 1-1 Britânia (1966-06-27)
- só na RSSSF (não achado no ogol): Seleto 6-1 Caramuru (1966-06-27)
- só na RSSSF (não achado no ogol): União Olímpico 2-0 Athletico-PR (1966-06-27)
- só na RSSSF (não achado no ogol): Coritiba 3-0 Rio Branco-PR (1966-06-27)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-0 Operário-PR (1966-06-29)
- só na RSSSF (não achado no ogol): Athletico-PR 1-2 Britânia (1966-07-03)
- só na RSSSF (não achado no ogol): Água Verde 7-2 Guarani-PR (1966-07-04)
- só na RSSSF (não achado no ogol): Operário-PR 2-1 Palestra Itália (1966-07-04)
- só na RSSSF (não achado no ogol): Rio Branco-PR 6-0 Caramuru (1966-07-04)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-3 Coritiba (1966-07-04)
- só na RSSSF (não achado no ogol): Primavera-PR 0-0 Seleto (1966-07-07)
- só na RSSSF (não achado no ogol): Coritiba 3-1 Athletico-PR (1966-07-10)
- só na RSSSF (não achado no ogol): Seleto 1-2 Ferroviário-PR (1966-07-11)
- só na RSSSF (não achado no ogol): Caramuru 1-1 Palestra Itália (1966-07-11)
- só na RSSSF (não achado no ogol): Água Verde 2-2 Primavera-PR (1966-07-11)
- só na RSSSF (não achado no ogol): Operário-PR 1-3 Guarani-PR (1966-07-11)
- só na RSSSF (não achado no ogol): Britânia 4-1 União Olímpico (1966-07-11)
- só na RSSSF (não achado no ogol): Athletico-PR 1-1 Ferroviário-PR (1966-07-17)
- só na RSSSF (não achado no ogol): Britânia 1-1 Primavera-PR (1966-07-17)
- só na RSSSF (não achado no ogol): Palestra Itália 0-0 Rio Branco-PR (1966-07-18)
- só na RSSSF (não achado no ogol): Coritiba 1-1 Água Verde (1966-07-18)
- só na RSSSF (não achado no ogol): Seleto 2-1 Operário-PR (1966-07-18)
- só na RSSSF (não achado no ogol): Guarani-PR 3-1 União Olímpico (1966-07-18)
- só na RSSSF (não achado no ogol): Palestra Itália 0-0 Guarani-PR (1966-07-24)
- só na RSSSF (não achado no ogol): Britânia 0-0 Coritiba (1966-07-24)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-2 Água Verde (1966-07-25)
- só na RSSSF (não achado no ogol): Primavera-PR 5-1 Caramuru (1966-07-25)
- só na RSSSF (não achado no ogol): Rio Branco-PR 2-2 Athletico-PR (1966-07-25)
- só na RSSSF (não achado no ogol): União Olímpico 2-2 Seleto (1966-07-25)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-0 União Olímpico (1966-07-29)
- só na RSSSF (não achado no ogol): Athletico-PR 0-4 Primavera-PR (1966-07-31)
- só na RSSSF (não achado no ogol): Água Verde 5-1 Seleto (1966-08-01)
- só na RSSSF (não achado no ogol): Rio Branco-PR 3-1 Britânia (1966-08-01)
- só na RSSSF (não achado no ogol): Guarani-PR 1-1 Coritiba (1966-08-01)
- só na RSSSF (não achado no ogol): Caramuru 1-1 Operário-PR (1966-08-01)
- só na RSSSF (não achado no ogol): Água Verde 3-0 Athletico-PR (1966-08-14)
- só na RSSSF (não achado no ogol): Caramuru 1-2 Coritiba (1966-08-15)
- só na RSSSF (não achado no ogol): União Olímpico 1-1 Operário-PR (1966-08-15)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-2 Primavera-PR (1966-08-15)
- só na RSSSF (não achado no ogol): Britânia 1-2 Palestra Itália (1966-08-15)
- só na RSSSF (não achado no ogol): Guarani-PR 3-3 Rio Branco-PR (1966-08-15)
- só na RSSSF (não achado no ogol): Athletico-PR 4-3 Palestra Itália (1966-08-20)
- só na RSSSF (não achado no ogol): Operário-PR 1-2 Coritiba (1966-08-21)
- só na RSSSF (não achado no ogol): Seleto 3-1 Guarani-PR (1966-08-21)
- só na RSSSF (não achado no ogol): Primavera-PR 0-0 Rio Branco-PR (1966-08-21)
- só na RSSSF (não achado no ogol): União Olímpico 2-2 Água Verde (1966-08-21)
- só na RSSSF (não achado no ogol): Ferroviário-PR 5-0 Caramuru (1966-08-21)
- só na RSSSF (não achado no ogol): Coritiba 1-0 União Olímpico (1966-08-28)
- só na RSSSF (não achado no ogol): Britânia 5-1 Operário-PR (1966-08-29)
- só na RSSSF (não achado no ogol): Palestra Itália 2-2 Seleto (1966-08-29)
- só na RSSSF (não achado no ogol): Rio Branco-PR 2-4 Ferroviário-PR (1966-08-29)
- só na RSSSF (não achado no ogol): Guarani-PR 1-1 Primavera-PR (1966-08-29)
- só na RSSSF (não achado no ogol): Caramuru 2-1 Athletico-PR (1966-08-29)
- só na RSSSF (não achado no ogol): Ferroviário-PR 4-0 Guarani-PR (1966-09-04)
- só na RSSSF (não achado no ogol): União Olímpico 2-1 Palestra Itália (1966-09-05)
- só na RSSSF (não achado no ogol): Operário-PR 1-2 Rio Branco-PR (1966-09-05)
- só na RSSSF (não achado no ogol): Água Verde 6-1 Caramuru (1966-09-05)
- só na RSSSF (não achado no ogol): Primavera-PR 1-2 Coritiba (1966-09-05)
- só na RSSSF (não achado no ogol): Seleto 2-0 Britânia (1966-09-05)
- só na RSSSF (não achado no ogol): Britânia 1-1 Ferroviário-PR (1966-09-11)
- só na RSSSF (não achado no ogol): Palestra Itália 1-5 Primavera-PR (1966-09-11)
- só na RSSSF (não achado no ogol): Caramuru 6-2 União Olímpico (1966-09-12)
- só na RSSSF (não achado no ogol): Athletico-PR 3-0 Operário-PR (1966-09-12)
- só na RSSSF (não achado no ogol): Rio Branco-PR 1-1 Água Verde (1966-09-12)
- só na RSSSF (não achado no ogol): Coritiba 2-0 Seleto (1966-09-12)
- só na RSSSF (não achado no ogol): Ferroviário-PR 4-0 Palestra Itália (1966-09-18)
- só na RSSSF (não achado no ogol): Água Verde 1-1 Britânia (1966-09-19)
- só na RSSSF (não achado no ogol): Seleto 0-1 Athletico-PR (1966-09-19)
- só na RSSSF (não achado no ogol): Guarani-PR 1-0 Caramuru (1966-09-19)
- só na RSSSF (não achado no ogol): União Olímpico 3-3 Rio Branco-PR (1966-09-19)
- só na RSSSF (não achado no ogol): Primavera-PR 1-0 Operário-PR (1966-09-19)
- só na RSSSF (não achado no ogol): Água Verde 3-0 Operário-PR (1966-09-25)
- só na RSSSF (não achado no ogol): Rio Branco-PR 0-1 Seleto (1966-09-26)
- só na RSSSF (não achado no ogol): Palestra Itália 2-0 Coritiba (1966-09-26)
- só na RSSSF (não achado no ogol): Caramuru 1-2 Britânia (1966-09-26)
- só na RSSSF (não achado no ogol): Guarani-PR 2-2 Athletico-PR (1966-09-26)
- só na RSSSF (não achado no ogol): União Olímpico 0-0 Primavera-PR (1966-09-26)
- só na RSSSF (não achado no ogol): Água Verde 3-1 Palestra Itália (1966-10-02)
- só na RSSSF (não achado no ogol): Athletico-PR 3-0 União Olímpico (1966-10-09)
- só na RSSSF (não achado no ogol): Britânia 4-1 Guarani-PR (1966-10-10)
- só na RSSSF (não achado no ogol): Caramuru 0-2 Seleto (1966-10-10)
- só na RSSSF (não achado no ogol): Operário-PR 1-3 Ferroviário-PR (1966-10-10)
- só na RSSSF (não achado no ogol): Rio Branco-PR 2-4 Coritiba (1966-10-10)
- só na RSSSF (não achado no ogol): Britânia 3-0 Athletico-PR (1966-10-16)
- só na RSSSF (não achado no ogol): Palestra Itália 3-1 Operário-PR (1966-10-16)
- só na RSSSF (não achado no ogol): Guarani-PR 2-1 Água Verde (1966-10-17)
- só na RSSSF (não achado no ogol): Seleto 0-0 Primavera-PR (1966-10-17)
- só na RSSSF (não achado no ogol): Caramuru 2-5 Rio Branco-PR (1966-10-17)
- só na RSSSF (não achado no ogol): Coritiba 2-2 Ferroviário-PR (1966-10-17)
- só na RSSSF (não achado no ogol): Athletico-PR 3-0 Coritiba (1966-10-23)
- só na RSSSF (não achado no ogol): Palestra Itália 2-1 Caramuru (1966-10-24)
- só na RSSSF (não achado no ogol): Guarani-PR 2-0 Operário-PR (1966-10-24)
- só na RSSSF (não achado no ogol): Ferroviário-PR 4-2 Seleto (1966-10-24)
- só na RSSSF (não achado no ogol): União Olímpico 0-1 Britânia (1966-10-24)
- só na RSSSF (não achado no ogol): Primavera-PR 1-1 Água Verde (1966-10-24)
- só na RSSSF (não achado no ogol): Ferroviário-PR 0-0 Athletico-PR (1966-10-30)
- só na RSSSF (não achado no ogol): Água Verde 0-1 Coritiba (1966-10-31)
- só na RSSSF (não achado no ogol): Operário-PR 0-1 Seleto (1966-10-31)
- só na RSSSF (não achado no ogol): União Olímpico 1-1 Guarani-PR (1966-10-31)
- só na RSSSF (não achado no ogol): Primavera-PR 2-1 Britânia (1966-11-01)
- só na RSSSF (não achado no ogol): Rio Branco-PR 4-1 Palestra Itália (1966-11-03)
- só na RSSSF (não achado no ogol): Coritiba 3-0 Britânia (1966-11-06)
- só na RSSSF (não achado no ogol): Água Verde 4-2 Ferroviário-PR (1966-11-07)
- só na RSSSF (não achado no ogol): Guarani-PR 1-0 Palestra Itália (1966-11-07)
- só na RSSSF (não achado no ogol): Athletico-PR 3-1 Rio Branco-PR (1966-11-07)
- só na RSSSF (não achado no ogol): Seleto 4-1 União Olímpico (1966-11-07)
- só na RSSSF (não achado no ogol): Primavera-PR 1-3 Athletico-PR (1966-11-13)
- só na RSSSF (não achado no ogol): Coritiba 3-0 Guarani-PR (1966-11-14)
- só na RSSSF (não achado no ogol): Seleto 1-3 Água Verde (1966-11-14)
- só na RSSSF (não achado no ogol): Britânia 2-3 Rio Branco-PR (1966-11-14)
- só na RSSSF (não achado no ogol): Operário-PR 3-0 Caramuru (1966-11-14)
- só na RSSSF (não achado no ogol): Primavera-PR 0-5 Ferroviário-PR (1966-11-20)
- só na RSSSF (não achado no ogol): Palestra Itália 0-5 Britânia (1966-11-20)
- só na RSSSF (não achado no ogol): Rio Branco-PR 2-0 Guarani-PR (1966-11-21)
- só na RSSSF (não achado no ogol): Coritiba 5-0 Caramuru (1966-11-21)
- só na RSSSF (não achado no ogol): Operário-PR 2-0 União Olímpico (1966-11-21)
- só na RSSSF (não achado no ogol): Athletico-PR 1-0 Água Verde (1966-11-21)
- só na RSSSF (não achado no ogol): Caramuru 1-3 Primavera-PR (1966-11-25)
- só na RSSSF (não achado no ogol): Coritiba 1-1 Ferroviário-PR (1966-11-28)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-0 Coritiba (1966-12-05)
- só na RSSSF (não achado no ogol): Primavera-PR 1-0 Britânia (None)
- só na RSSSF (não achado no ogol): Seleto 2-0 Primavera-PR (None)
- só na RSSSF (não achado no ogol): Seleto 2-1 Britânia (None)

### 1966

- tabela publicada x jogos — Segunda fase / -: Ferroviário-PR tabela [22, 9, 10, 3, 32, 21] jogos [11, 7, 2, 2, 26, 13] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: União Bandeirante tabela [22, 11, 5, 6, 31, 19] jogos [11, 7, 1, 3, 18, 12] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: São Paulo-PR tabela [22, 10, 6, 6, 38, 33] jogos [11, 4, 4, 3, 15, 16] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Grêmio Maringá tabela [22, 9, 8, 5, 36, 27] jogos [11, 4, 2, 5, 14, 14] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [22, 9, 8, 5, 33, 25] jogos [11, 5, 4, 2, 20, 12] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [22, 9, 7, 6, 33, 24] jogos [11, 1, 5, 5, 10, 16] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [22, 8, 5, 9, 27, 26] jogos [11, 3, 3, 5, 12, 14] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Apucarana tabela [22, 7, 5, 10, 27, 45] jogos [11, 2, 3, 6, 10, 18] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Primavera-PR tabela [22, 6, 6, 10, 28, 32] jogos [11, 4, 5, 2, 14, 11] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Água Verde tabela [22, 6, 6, 10, 27, 31] jogos [11, 5, 4, 2, 19, 12] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Seleto tabela [22, 3, 10, 9, 20, 33] jogos [11, 3, 4, 4, 10, 16] — a tabela conta 22 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Arapongas FC tabela [22, 5, 4, 13, 28, 44] jogos [11, 1, 3, 7, 10, 24] — a tabela conta 22 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Paulo-PR)
- vice pela Wikipédia (sem final de dois clubes): União Bandeirante

### 1967

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Paulo-PR)
- só na RSSSF (não achado no ogol): Água Verde 0-1 São Paulo-PR (1967-03-20)
- só na RSSSF (não achado no ogol): Seleto 2-0 Primavera-PR (1967-05-21)
- só na RSSSF (não achado no ogol): Jandaia 2-2 Ferroviário-PR (1967-05-21)
- só na RSSSF (não achado no ogol): Coritiba 1-0 Apucarana (1967-05-21)
- só na RSSSF (não achado no ogol): Londrina 1-0 Grêmio Maringá (1967-05-21)
- só na RSSSF (não achado no ogol): União Bandeirante 2-1 Athletico-PR (1967-05-21)
- só na RSSSF (não achado no ogol): Primavera-PR 0-2 Água Verde (1967-05-27)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-1 União Bandeirante (1967-05-28)
- só na RSSSF (não achado no ogol): Athletico-PR 0-2 Londrina (1967-05-28)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-0 Coritiba (1967-05-28)
- só na RSSSF (não achado no ogol): Apucarana 1-2 Jandaia (1967-05-28)
- só na RSSSF (não achado no ogol): Ferroviário-PR 5-1 Seleto (1967-06-03)
- só na RSSSF (não achado no ogol): Jandaia 3-1 Grêmio Maringá (1967-06-04)
- só na RSSSF (não achado no ogol): Coritiba 2-2 Athletico-PR (1967-06-04)
- só na RSSSF (não achado no ogol): São Paulo-PR 0-1 Primavera-PR (1967-06-04)
- só na RSSSF (não achado no ogol): União Bandeirante 1-0 Londrina (1967-06-04)
- só na RSSSF (não achado no ogol): Água Verde 1-0 Ferroviário-PR (1967-06-10)
- só na RSSSF (não achado no ogol): Seleto 4-1 Apucarana (1967-06-11)
- só na RSSSF (não achado no ogol): Athletico-PR 0-1 Jandaia (1967-06-11)
- só na RSSSF (não achado no ogol): Londrina 2-2 Coritiba (1967-06-11)
- só na RSSSF (não achado no ogol): Grêmio Maringá 6-1 São Paulo-PR (1967-06-11)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-1 São Paulo-PR (1967-06-17)
- só na RSSSF (não achado no ogol): Grêmio Maringá 0-0 Seleto (1967-06-18)
- só na RSSSF (não achado no ogol): Apucarana 0-0 Água Verde (1967-06-18)
- só na RSSSF (não achado no ogol): Primavera-PR 3-0 União Bandeirante (1967-06-18)
- só na RSSSF (não achado no ogol): Jandaia 1-1 Londrina (1967-06-18)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-0 Primavera-PR (1967-06-24)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-1 Apucarana (1967-06-25)
- só na RSSSF (não achado no ogol): Água Verde 2-0 Grêmio Maringá (1967-06-25)
- só na RSSSF (não achado no ogol): Seleto 1-1 Athletico-PR (1967-06-25)
- só na RSSSF (não achado no ogol): Jandaia 0-1 Coritiba (1967-06-25)
- só na RSSSF (não achado no ogol): Athletico-PR 1-1 Água Verde (1967-07-01)
- só na RSSSF (não achado no ogol): Coritiba 1-0 União Bandeirante (1967-07-02)
- só na RSSSF (não achado no ogol): Londrina 1-1 Seleto (1967-07-02)
- só na RSSSF (não achado no ogol): Apucarana 0-1 Primavera-PR (1967-07-02)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-0 Ferroviário-PR (1967-07-02)
- só na RSSSF (não achado no ogol): Primavera-PR 2-1 Grêmio Maringá (1967-07-08)
- só na RSSSF (não achado no ogol): São Paulo-PR 3-2 Athletico-PR (1967-07-09)
- só na RSSSF (não achado no ogol): Água Verde 1-1 Londrina (1967-07-09)
- só na RSSSF (não achado no ogol): Seleto 0-1 Coritiba (1967-07-09)
- só na RSSSF (não achado no ogol): União Bandeirante 2-0 Jandaia (1967-07-09)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-1 Apucarana (1967-07-15)
- só na RSSSF (não achado no ogol): União Bandeirante 2-1 Grêmio Maringá (1967-07-16)
- só na RSSSF (não achado no ogol): Londrina 0-0 São Paulo-PR (1967-07-16)
- só na RSSSF (não achado no ogol): Athletico-PR 0-1 Primavera-PR (1967-07-16)
- só na RSSSF (não achado no ogol): Jandaia 0-1 Seleto (1967-07-16)
- só na RSSSF (não achado no ogol): Primavera-PR 1-1 Londrina (1967-07-22)
- só na RSSSF (não achado no ogol): Coritiba 1-1 Água Verde (1967-07-23)
- só na RSSSF (não achado no ogol): Apucarana 1-0 União Bandeirante (1967-07-23)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-1 Jandaia (1967-07-23)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-1 Athletico-PR (1967-07-29)
- só na RSSSF (não achado no ogol): Apucarana 2-3 Grêmio Maringá (1967-07-30)
- só na RSSSF (não achado no ogol): Coritiba 3-1 São Paulo-PR (1967-07-30)
- só na RSSSF (não achado no ogol): União Bandeirante 1-0 Seleto (1967-07-30)
- só na RSSSF (não achado no ogol): Jandaia 3-1 Água Verde (1967-07-30)
- só na RSSSF (não achado no ogol): Athletico-PR 0-0 Apucarana (1967-08-05)
- só na RSSSF (não achado no ogol): Londrina 2-0 Ferroviário-PR (1967-08-06)
- só na RSSSF (não achado no ogol): Seleto 3-1 São Paulo-PR (1967-08-06)
- só na RSSSF (não achado no ogol): Ferroviário-PR 0-0 União Bandeirante (1967-08-12)
- só na RSSSF (não achado no ogol): Água Verde 1-3 Seleto (1967-08-13)
- só na RSSSF (não achado no ogol): Apucarana 1-0 Londrina (1967-08-13)
- só na RSSSF (não achado no ogol): Primavera-PR 3-3 Coritiba (1967-08-15)
- só na RSSSF (não achado no ogol): Primavera-PR 0-0 Jandaia (1967-08-19)
- só na RSSSF (não achado no ogol): Coritiba 1-1 Ferroviário-PR (1967-08-20)
- só na RSSSF (não achado no ogol): União Bandeirante 1-3 Água Verde (1967-08-20)
- só na RSSSF (não achado no ogol): Grêmio Maringá 1-0 Athletico-PR (1967-08-29)
- só na RSSSF (não achado no ogol): Ferroviário-PR 5-2 Jandaia (1967-08-26)
- só na RSSSF (não achado no ogol): Apucarana 2-0 Coritiba (1967-08-27)
- só na RSSSF (não achado no ogol): Grêmio Maringá 0-2 Água Verde (1967-08-27)
- só na RSSSF (não achado no ogol): União Bandeirante 3-1 São Paulo-PR (1967-08-27)
- só na RSSSF (não achado no ogol): Primavera-PR 2-2 Seleto (1967-08-27)
- só na RSSSF (não achado no ogol): Athletico-PR 1-0 União Bandeirante (1967-09-02)
- só na RSSSF (não achado no ogol): Coritiba 1-2 Grêmio Maringá (1967-09-03)
- só na RSSSF (não achado no ogol): Seleto 0-0 Ferroviário-PR (1967-09-03)
- só na RSSSF (não achado no ogol): Londrina 0-1 Primavera-PR (1967-09-03)
- só na RSSSF (não achado no ogol): Jandaia 1-2 Apucarana (1967-09-03)
- só na RSSSF (não achado no ogol): Água Verde 2-1 Primavera-PR (1967-09-07)
- só na RSSSF (não achado no ogol): Água Verde 2-2 União Bandeirante (1967-09-10)
- só na RSSSF (não achado no ogol): Apucarana 1-1 Athletico-PR (1967-09-10)
- só na RSSSF (não achado no ogol): Grêmio Maringá 3-1 Jandaia (1967-09-10)
- só na RSSSF (não achado no ogol): Londrina 3-1 São Paulo-PR (1967-09-10)
- só na RSSSF (não achado no ogol): Primavera-PR 3-2 São Paulo-PR (1967-09-16)
- só na RSSSF (não achado no ogol): Seleto 1-1 Grêmio Maringá (1967-09-17)
- só na RSSSF (não achado no ogol): União Bandeirante 1-1 Ferroviário-PR (1967-09-17)
- só na RSSSF (não achado no ogol): Londrina 2-0 Apucarana (1967-09-17)
- só na RSSSF (não achado no ogol): Athletico-PR 0-5 Coritiba (1967-09-17)
- só na RSSSF (não achado no ogol): Athletico-PR 5-2 São Paulo-PR (1967-09-23)
- só na RSSSF (não achado no ogol): Ferroviário-PR 0-0 Água Verde (1967-09-24)
- só na RSSSF (não achado no ogol): Grêmio Maringá 3-0 Londrina (1967-09-24)
- só na RSSSF (não achado no ogol): União Bandeirante 0-0 Primavera-PR (1967-09-24)
- só na RSSSF (não achado no ogol): Apucarana 4-2 Seleto (1967-09-24)
- só na RSSSF (não achado no ogol): Primavera-PR 0-0 Athletico-PR (1967-09-30)
- só na RSSSF (não achado no ogol): Coritiba 1-2 Londrina (1967-10-01)
- só na RSSSF (não achado no ogol): Apucarana 0-0 Ferroviário-PR (1967-10-01)
- só na RSSSF (não achado no ogol): São Paulo-PR 3-1 Seleto (1967-10-01)
- só na RSSSF (não achado no ogol): Jandaia 1-1 União Bandeirante (1967-10-01)
- só na RSSSF (não achado no ogol): Água Verde 1-1 Coritiba (1967-10-08)
- só na RSSSF (não achado no ogol): Seleto 1-1 União Bandeirante (1967-10-08)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-1 Apucarana (1967-10-08)
- só na RSSSF (não achado no ogol): Londrina 1-0 Jandaia (1967-10-08)
- só na RSSSF (não achado no ogol): Athletico-PR 0-1 Ferroviário-PR (1967-10-08)
- só na RSSSF (não achado no ogol): Primavera-PR 2-1 Apucarana (1967-10-14)
- só na RSSSF (não achado no ogol): Ferroviário-PR 2-0 Londrina (1967-10-15)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-2 Grêmio Maringá (1967-10-15)
- só na RSSSF (não achado no ogol): Seleto 0-1 Água Verde (1967-10-15)
- só na RSSSF (não achado no ogol): Jandaia 3-0 Athletico-PR (1967-10-15)
- só na RSSSF (não achado no ogol): Apucarana 2-1 Seleto (1967-10-22)
- só na RSSSF (não achado no ogol): Água Verde 1-1 Jandaia (1967-10-22)
- só na RSSSF (não achado no ogol): Ferroviário-PR 3-4 Coritiba (1967-10-22)
- só na RSSSF (não achado no ogol): Grêmio Maringá 3-1 Primavera-PR (1967-10-22)
- só na RSSSF (não achado no ogol): Londrina 2-0 Athletico-PR (1967-10-22)
- só na RSSSF (não achado no ogol): Coritiba 1-0 Primavera-PR (1967-10-28)
- só na RSSSF (não achado no ogol): São Paulo-PR 2-2 Ferroviário-PR (1967-10-29)
- só na RSSSF (não achado no ogol): Seleto 1-1 Londrina (1967-10-29)
- só na RSSSF (não achado no ogol): União Bandeirante 0-0 Apucarana (1967-10-29)
- só na RSSSF (não achado no ogol): Athletico-PR 2-4 Grêmio Maringá (1967-10-29)
- só na RSSSF (não achado no ogol): Ferroviário-PR 1-1 Grêmio Maringá (1967-11-05)
- só na RSSSF (não achado no ogol): União Bandeirante 0-0 Coritiba (1967-11-05)
- só na RSSSF (não achado no ogol): Londrina 0-1 Água Verde (1967-11-05)
- só na RSSSF (não achado no ogol): Jandaia 1-0 São Paulo-PR (1967-11-05)
- só na RSSSF (não achado no ogol): Athletico-PR 2-1 Seleto (1967-11-11)
- só na RSSSF (não achado no ogol): Coritiba 1-0 Jandaia (1967-11-12)
- só na RSSSF (não achado no ogol): São Paulo-PR 0-0 Água Verde (1967-11-12)
- só na RSSSF (não achado no ogol): Água Verde 1-1 Athletico-PR (1967-11-18)
- só na RSSSF (não achado no ogol): Coritiba 2-1 Seleto (1967-11-19)
- só na RSSSF (não achado no ogol): Londrina 2-2 União Bandeirante (1967-11-19)
- só na RSSSF (não achado no ogol): Jandaia 5-0 Primavera-PR (1967-11-19)
- só na RSSSF (não achado no ogol): Apucarana 1-1 São Paulo-PR (1967-11-19)
- só na RSSSF (não achado no ogol): Água Verde 2-0 Apucarana (1967-11-25)
- só na RSSSF (não achado no ogol): São Paulo-PR 1-0 Coritiba (1967-11-26)
- só na RSSSF (não achado no ogol): Seleto 2-1 Jandaia (1967-11-26)
- só na RSSSF (não achado no ogol): Grêmio Maringá 2-0 União Bandeirante (1967-11-26)
- só na RSSSF (não achado no ogol): Primavera-PR 0-6 Ferroviário-PR (1967-11-26)

### 1968

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Britânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): primavera
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Britânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Britânia)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)

### 1969

- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [26, 17, 7, 2, 44, 10] jogos [24, 15, 7, 2, 35, 9] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Ferroviário-PR tabela [26, 16, 4, 6, 44, 22] jogos [24, 15, 4, 5, 40, 17] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: União Bandeirante tabela [26, 14, 8, 4, 59, 33] jogos [24, 12, 7, 5, 54, 33] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [26, 12, 4, 10, 43, 40] jogos [24, 10, 4, 10, 39, 40] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [25, 10, 7, 8, 37, 29] jogos [23, 10, 6, 7, 36, 27] — a tabela conta 25 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [24, 12, 2, 10, 45, 42] jogos [22, 11, 2, 9, 40, 38] — a tabela conta 24 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Paranavaí tabela [26, 8, 8, 10, 27, 28] jogos [24, 7, 7, 10, 25, 27] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: CAFE tabela [26, 9, 4, 13, 29, 44] jogos [24, 9, 4, 11, 29, 36] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [24, 9, 3, 12, 38, 36] jogos [22, 9, 2, 11, 36, 33] — a tabela conta 24 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Seleto tabela [26, 6, 9, 11, 31, 38] jogos [24, 6, 7, 11, 29, 36] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Grêmio Oeste tabela [26, 8, 3, 15, 27, 50] jogos [24, 8, 3, 13, 26, 45] — a tabela conta 26 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Primavera-PR tabela [25, 5, 5, 15, 31, 50] jogos [23, 5, 5, 13, 30, 45] — a tabela conta 25 jogos e as fontes trazem 23
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Oeste
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Primavera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Grêmio Oeste — clube que o ogol não tem; entra só pela RSSSF
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- campeão pela lista oficial, Coritiba; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-PR

### 1970

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Oeste
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Grêmio Oeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio Oeste)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- campeão pela lista oficial, Athletico-PR; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1971

- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [16, 8, 6, 2, 23, 9] jogos [16, 8, 6, 2, 25, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [16, 7, 5, 4, 34, 19] jogos [17, 8, 6, 3, 38, 18] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Cascavel FC tabela [16, 5, 3, 8, 19, 28] jogos [17, 4, 5, 8, 17, 28] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Caramuru tabela [16, 0, 5, 11, 11, 30] jogos [17, 0, 5, 12, 11, 32] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Paranavaí tabela [16, 8, 4, 4, 24, 20] jogos [15, 8, 4, 3, 22, 17] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [16, 9, 1, 6, 38, 19] jogos [17, 10, 1, 6, 41, 20] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Jandaia tabela [16, 6, 6, 4, 32, 26] jogos [15, 5, 6, 4, 29, 24] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: Nacional-PR tabela [16, 6, 4, 6, 20, 27] jogos [17, 7, 4, 6, 24, 27] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Cambé tabela [16, 2, 5, 9, 14, 39] jogos [17, 3, 5, 9, 15, 39] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [18, 12, 5, 1, 31, 14] jogos [34, 20, 11, 3, 56, 24] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: União Bandeirante tabela [18, 10, 6, 2, 28, 13] jogos [34, 22, 10, 2, 83, 26] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [18, 10, 4, 4, 27, 10] jogos [34, 16, 9, 9, 53, 27] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [18, 8, 8, 2, 22, 13] jogos [34, 19, 11, 4, 47, 21] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [17, 5, 6, 6, 21, 19] jogos [33, 16, 11, 6, 50, 34] — a tabela conta 17 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [17, 4, 6, 7, 13, 17] jogos [34, 14, 7, 13, 54, 37] — a tabela conta 17 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Pontagrossense tabela [17, 4, 6, 7, 12, 21] jogos [33, 9, 14, 10, 36, 38] — a tabela conta 17 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno / -: Paranavaí tabela [18, 4, 2, 12, 20, 31] jogos [33, 12, 6, 15, 42, 48] — a tabela conta 18 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno / -: Jandaia tabela [17, 2, 5, 10, 5, 28] jogos [32, 7, 11, 14, 34, 52] — a tabela conta 17 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Água Verde tabela [16, 3, 2, 11, 18, 31] jogos [33, 11, 8, 14, 56, 49] — a tabela conta 16 jogos e as fontes trazem 33
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Astorga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cambé
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caramuru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Oeste
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mourãoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pontagrossense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Astorga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Astorga)
- Cambé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cambé)
- Caramuru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Grêmio Oeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio Oeste)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mourãoense — clube que o ogol não tem; entra só pela RSSSF
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pontagrossense — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Seleto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Seleto)
- campeão pela lista oficial, Coritiba; o 1º pela soma dos jogos da última fase é União Bandeirante (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): União Bandeirante

### 1972

- tabela publicada x jogos — Primeira fase / -: Pinheiros-PR tabela [28, 12, 9, 7, 42, 39] jogos [28, 12, 9, 7, 44, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: CAFE tabela [28, 7, 7, 14, 25, 37] jogos [28, 7, 7, 14, 25, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Pinheiros-PR tabela [28, 12, 9, 7, 42, 39] jogos [28, 12, 9, 7, 44, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: CAFE tabela [28, 7, 7, 14, 25, 37] jogos [28, 7, 7, 14, 25, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [14, 9, 4, 1, 23, 9] jogos [14, 9, 4, 1, 24, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Pontagrossense tabela [14, 2, 3, 9, 12, 21] jogos [14, 2, 3, 9, 12, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [14, 9, 4, 1, 23, 9] jogos [14, 9, 4, 1, 24, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Pontagrossense tabela [14, 2, 3, 9, 12, 21] jogos [14, 2, 3, 9, 12, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [44, 27, 14, 3, 91, 28] jogos [44, 27, 14, 3, 92, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Pinheiros-PR tabela [40, 14, 13, 13, 53, 57] jogos [40, 14, 13, 13, 55, 57] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Pontagrossense tabela [42, 15, 10, 17, 46, 48] jogos [42, 15, 10, 17, 46, 49] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: CAFE tabela [28, 7, 7, 14, 25, 37] jogos [28, 7, 7, 14, 25, 39] — há jogo do clube sem conferência no ogol
- jogo anulado ou cancelado fica de fora: Rio Branco 2-1 Cascavel (1973-02-11) [cancelled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CAFE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mourãoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pontagrossense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- CAFE — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mourãoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mourãoense)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pontagrossense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pontagrossense)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1973

- tabela publicada x jogos — 2º Turno / -: Pontagrossense tabela [22, 10, 6, 6, 26, 22] jogos [21, 9, 6, 6, 26, 22] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [20, 8, 6, 6, 21, 6] jogos [17, 8, 6, 3, 21, 6] — a tabela conta 20 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Iguaçu tabela [21, 6, 5, 10, 16, 25] jogos [20, 5, 5, 10, 16, 25] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Pinheiros-PR tabela [22, 5, 5, 12, 20, 40] jogos [21, 4, 5, 12, 20, 40] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Rio Branco-PR tabela [22, 5, 3, 14, 13, 38] jogos [20, 4, 3, 13, 13, 38] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — 4º Turno / -: Coritiba tabela [10, 8, 2, 0, 13, 2] jogos [32, 27, 4, 1, 64, 10] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 4º Turno / -: Athletico-PR tabela [10, 3, 6, 1, 10, 8] jogos [32, 19, 10, 3, 55, 23] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 4º Turno / -: Pontagrossense tabela [10, 4, 2, 4, 12, 11] jogos [31, 13, 8, 10, 38, 33] — a tabela conta 10 jogos e as fontes trazem 31
- tabela publicada x jogos — 4º Turno / -: Colorado-PR tabela [10, 4, 2, 4, 8, 8] jogos [27, 12, 8, 7, 29, 14] — a tabela conta 10 jogos e as fontes trazem 27
- tabela publicada x jogos — 4º Turno / -: Londrina tabela [10, 2, 2, 6, 8, 12] jogos [32, 10, 8, 14, 36, 35] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 4º Turno / -: União Bandeirante tabela [10, 1, 2, 7, 4, 14] jogos [32, 10, 6, 16, 29, 37] — a tabela conta 10 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mourãoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pontagrossense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mourãoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mourãoense)
- Pontagrossense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pontagrossense)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1974

- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [20, 5, 4, 11, 10, 21] jogos [20, 5, 4, 11, 16, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: União Bandeirante tabela [6, 1, 3, 2, 8, 5] jogos [6, 1, 3, 2, 5, 8] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AC Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- AC Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Colorado-PR

### 1975

- tabela publicada x jogos — Primeira fase / -: Umuarama tabela [11, 3, 2, 6, 9, 12] jogos [11, 3, 3, 5, 9, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Pinheiros-PR tabela [11, 2, 4, 5, 8, 12] jogos [11, 1, 5, 5, 7, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined table - both stages / -: Pinheiros-PR tabela [22, 7, 6, 9, 23, 30] jogos [22, 6, 7, 9, 22, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined table - both stages / -: Umuarama tabela [22, 6, 6, 10, 26, 29] jogos [22, 6, 7, 9, 26, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: União Bandeirante tabela [7, 3, 2, 2, 6, 7] jogos [7, 3, 2, 2, 6, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Iguaçu tabela [7, 2, 0, 5, 5, 7] jogos [7, 2, 0, 5, 4, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined table - all stages / -: União Bandeirante tabela [29, 14, 6, 9, 32, 30] jogos [29, 14, 6, 9, 32, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined table - all stages / -: Pinheiros-PR tabela [29, 9, 10, 10, 33, 34] jogos [29, 8, 11, 10, 32, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined table - all stages / -: Iguaçu tabela [29, 8, 7, 14, 33, 37] jogos [29, 8, 7, 14, 32, 37] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AC Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- AC Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Colorado-PR

### 1976

- tabela publicada x jogos — Terceira fase / -: Colorado-PR tabela [7, 6, 0, 1, 12, 6] jogos [7, 6, 1, 0, 12, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Grêmio Maringá tabela [7, 4, 3, 0, 10, 4] jogos [7, 3, 4, 0, 9, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Colorado-PR tabela [7, 6, 0, 1, 12, 5] jogos [7, 6, 1, 0, 12, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Grêmio Maringá tabela [7, 4, 3, 0, 9, 4] jogos [7, 3, 4, 0, 9, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Colorado-PR tabela [33, 17, 10, 6, 52, 20] jogos [33, 17, 11, 5, 52, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Grêmio Maringá tabela [33, 15, 9, 9, 53, 39] jogos [33, 14, 10, 9, 53, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [39, 19, 13, 7, 55, 25] jogos [39, 19, 14, 6, 55, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [33, 15, 9, 9, 54, 39] jogos [33, 14, 10, 9, 53, 39] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 9 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mourãoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- 9 de Julho — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mourãoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mourãoense)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Colorado-PR

### 1977

- tabela publicada x jogos — Segunda fase - Desempate / -: Athletico-PR tabela [7, 3, 4, 0, 6, 1] jogos [35, 15, 17, 3, 41, 15] — a tabela conta 7 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase - Desempate / -: Coritiba tabela [7, 3, 4, 0, 6, 4] jogos [37, 16, 17, 4, 51, 22] — a tabela conta 7 jogos e as fontes trazem 37
- tabela publicada x jogos — Segunda fase - Desempate / -: Matsubara tabela [7, 4, 1, 2, 9, 8] jogos [28, 12, 6, 10, 33, 31] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase - Desempate / -: União Bandeirante tabela [7, 3, 1, 3, 8, 8] jogos [28, 9, 11, 8, 27, 27] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase - Desempate / -: Londrina tabela [7, 2, 2, 3, 10, 5] jogos [28, 12, 9, 7, 38, 23] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase - Desempate / -: Colorado-PR tabela [7, 2, 2, 3, 6, 6] jogos [34, 13, 13, 8, 48, 28] — a tabela conta 7 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase - Desempate / -: Iguaçu tabela [7, 2, 1, 4, 6, 8] jogos [28, 7, 10, 11, 23, 29] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase - Desempate / -: Centenário tabela [7, 1, 1, 5, 8, 19] jogos [28, 11, 8, 9, 35, 37] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Colorado-PR tabela [7, 4, 3, 0, 9, 2] jogos [34, 13, 13, 8, 48, 28] — a tabela conta 7 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [7, 3, 3, 1, 10, 6] jogos [37, 16, 17, 4, 51, 22] — a tabela conta 7 jogos e as fontes trazem 37
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [7, 3, 3, 1, 6, 3] jogos [35, 15, 17, 3, 41, 15] — a tabela conta 7 jogos e as fontes trazem 35
- tabela publicada x jogos — Segunda fase / -: Centenário tabela [7, 4, 0, 3, 7, 8] jogos [28, 11, 8, 9, 35, 37] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [7, 2, 3, 2, 6, 6] jogos [28, 12, 9, 7, 38, 23] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Matsubara tabela [7, 2, 1, 4, 7, 9] jogos [28, 12, 6, 10, 33, 31] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: União Bandeirante tabela [7, 1, 3, 3, 5, 10] jogos [28, 9, 11, 8, 27, 27] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Iguaçu tabela [7, 0, 2, 5, 5, 11] jogos [28, 7, 10, 11, 23, 29] — a tabela conta 7 jogos e as fontes trazem 28
- tabela publicada x jogos — Combined Table - First and Second stage / -: Athletico-PR tabela [14, 6, 7, 1, 12, 4] jogos [35, 15, 17, 3, 41, 15] — a tabela conta 14 jogos e as fontes trazem 35
- tabela publicada x jogos — Combined Table - First and Second stage / -: Coritiba tabela [14, 6, 7, 1, 16, 10] jogos [37, 16, 17, 4, 51, 22] — a tabela conta 14 jogos e as fontes trazem 37
- tabela publicada x jogos — Repescagem / Zona Sul: Pinheiros-PR tabela [2, 1, 1, 0, 2, 1] jogos [6, 2, 2, 2, 5, 4] — a tabela conta 2 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Sul: Rio Branco-PR tabela [2, 1, 0, 1, 3, 2] jogos [6, 3, 2, 1, 6, 3] — a tabela conta 2 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Sul: Operário-PR tabela [2, 0, 1, 1, 2, 4] jogos [4, 0, 2, 2, 2, 6] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Repescagem / Zona Sul: Rio Branco-PR tabela [2, 1, 1, 0, 1, 0] jogos [6, 3, 2, 1, 6, 3] — a tabela conta 2 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Sul: Pinheiros-PR tabela [2, 1, 0, 1, 2, 1] jogos [6, 2, 2, 2, 5, 4] — a tabela conta 2 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Sul: Operário-PR tabela [2, 0, 1, 1, 0, 2] jogos [4, 0, 2, 2, 2, 6] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Repescagem / Zona Norte: Grêmio Maringá tabela [3, 2, 1, 0, 9, 1] jogos [6, 5, 1, 0, 17, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Norte: Paranavaí tabela [3, 1, 1, 1, 3, 4] jogos [6, 1, 2, 3, 3, 10] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Norte: Umuarama tabela [3, 0, 1, 2, 1, 7] jogos [6, 1, 1, 4, 3, 10] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Norte: Grêmio Maringá tabela [3, 3, 0, 0, 8, 0] jogos [6, 5, 1, 0, 17, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Norte: Umuarama tabela [3, 1, 0, 2, 2, 3] jogos [6, 1, 1, 4, 3, 10] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / Zona Norte: Paranavaí tabela [3, 0, 1, 2, 0, 6] jogos [6, 1, 2, 3, 3, 10] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [3, 2, 1, 0, 4, 2] jogos [30, 14, 10, 6, 48, 23] — a tabela conta 3 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Coritiba tabela [3, 1, 1, 1, 4, 3] jogos [37, 16, 17, 4, 51, 22] — a tabela conta 3 jogos e as fontes trazem 37
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [3, 0, 2, 1, 1, 2] jogos [35, 15, 17, 3, 41, 15] — a tabela conta 3 jogos e as fontes trazem 35
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [3, 0, 2, 1, 1, 3] jogos [34, 13, 13, 8, 48, 28] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase final / -: Coritiba tabela [3, 2, 1, 0, 4, 2] jogos [37, 16, 17, 4, 51, 22] — a tabela conta 3 jogos e as fontes trazem 37
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [3, 1, 1, 1, 4, 4] jogos [30, 14, 10, 6, 48, 23] — a tabela conta 3 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [3, 1, 1, 1, 2, 2] jogos [35, 15, 17, 3, 41, 15] — a tabela conta 3 jogos e as fontes trazem 35
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [3, 0, 1, 2, 4, 6] jogos [34, 13, 13, 8, 48, 28] — a tabela conta 3 jogos e as fontes trazem 34
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 9 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AC Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Centenário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mourãoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- 9 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (9 de Julho)
- AC Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Centenário — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mourãoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mourãoense)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)

### 1978

- tabela publicada x jogos — Segunda fase / Grupo D: Athletico-PR tabela [6, 3, 3, 0, 13, 7] jogos [6, 3, 3, 0, 15, 7] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Coritiba

### 1979

- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [17, 8, 6, 3, 30, 13] jogos [17, 7, 7, 3, 30, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Umuarama tabela [17, 6, 2, 9, 16, 20] jogos [17, 6, 3, 8, 16, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [17, 8, 6, 3, 30, 13] jogos [17, 7, 7, 3, 30, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Umuarama tabela [17, 6, 2, 9, 16, 20] jogos [17, 6, 3, 8, 16, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [17, 5, 9, 3, 16, 10] jogos [17, 5, 9, 3, 16, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [17, 4, 10, 3, 19, 17] jogos [18, 4, 11, 3, 21, 19] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [17, 6, 4, 7, 16, 21] jogos [17, 6, 4, 7, 15, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Rio Branco-PR tabela [17, 1, 8, 8, 7, 15] jogos [18, 1, 9, 8, 10, 18] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [17, 5, 9, 3, 16, 10] jogos [17, 5, 9, 3, 16, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [17, 4, 10, 3, 19, 17] jogos [18, 4, 11, 3, 21, 19] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [17, 6, 4, 7, 16, 21] jogos [17, 6, 4, 7, 15, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Rio Branco-PR tabela [17, 1, 8, 8, 7, 15] jogos [18, 1, 9, 8, 10, 18] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [34, 16, 11, 7, 52, 26] jogos [34, 15, 12, 7, 52, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [34, 12, 14, 8, 40, 28] jogos [34, 12, 14, 8, 40, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [34, 12, 9, 13, 34, 36] jogos [33, 12, 8, 13, 31, 33] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / -: Umuarama tabela [34, 8, 10, 16, 26, 44] jogos [34, 8, 11, 15, 26, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Rio Branco-PR tabela [34, 3, 13, 18, 14, 41] jogos [35, 3, 14, 18, 17, 44] — a tabela conta 34 jogos e as fontes trazem 35
- tabela publicada x jogos — Terceira fase / -: Athletico-PR tabela [7, 2, 4, 1, 11, 7] jogos [8, 3, 4, 1, 13, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Terceira fase / -: Matsubara tabela [7, 0, 5, 2, 3, 5] jogos [8, 0, 5, 3, 3, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Terceira fase / -: Athletico-PR tabela [7, 2, 4, 1, 11, 7] jogos [8, 3, 4, 1, 13, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Terceira fase / -: Matsubara tabela [7, 0, 5, 2, 3, 5] jogos [8, 0, 5, 3, 3, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Terceira fase / -: Athletico-PR tabela [41, 18, 15, 8, 63, 33] jogos [41, 17, 16, 8, 63, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Londrina tabela [41, 15, 17, 9, 52, 33] jogos [41, 15, 17, 9, 52, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Toledo FC tabela [42, 13, 13, 16, 43, 52] jogos [41, 12, 13, 16, 38, 49] — a tabela conta 42 jogos e as fontes trazem 41
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [47, 19, 19, 9, 66, 35] jogos [47, 18, 20, 9, 66, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Londrina tabela [41, 15, 17, 9, 52, 33] jogos [41, 15, 17, 9, 52, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Toledo FC tabela [42, 13, 13, 16, 43, 52] jogos [41, 12, 13, 16, 38, 49] — a tabela conta 42 jogos e as fontes trazem 41
- tabela publicada x jogos — Fase final / -: Operário-PR tabela [35, 10, 13, 12, 37, 38] jogos [35, 10, 14, 11, 37, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Umuarama tabela [34, 8, 10, 16, 26, 44] jogos [34, 8, 11, 15, 26, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Rio Branco-PR tabela [34, 3, 13, 18, 14, 41] jogos [35, 3, 14, 18, 17, 44] — a tabela conta 34 jogos e as fontes trazem 35
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 9 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Agroceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Centenário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarapuava
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- 9 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (9 de Julho)
- Agroceres — clube que o ogol não tem; entra só pela RSSSF
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Centenário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Centenário)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarapuava — clube que o ogol não tem; entra só pela RSSSF
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Colorado-PR

### 1980

- tabela publicada x jogos — Primeira fase / -: Grêmio Maringá tabela [19, 11, 6, 2, 29, 15] jogos [18, 11, 6, 1, 29, 13] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [19, 6, 5, 8, 25, 30] jogos [19, 6, 5, 8, 25, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Umuarama tabela [19, 3, 7, 9, 12, 26] jogos [19, 3, 7, 9, 11, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Iguaçu tabela [19, 4, 2, 13, 10, 29] jogos [19, 4, 2, 13, 10, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Rio Branco-PR tabela [19, 3, 4, 12, 12, 35] jogos [20, 3, 4, 13, 12, 37] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Apucarana tabela [19, 2, 3, 14, 15, 36] jogos [19, 2, 3, 14, 16, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Londrina tabela [7, 3, 0, 4, 1, 10] jogos [7, 3, 0, 4, 11, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Pinheiros-PR tabela [14, 6, 6, 2, 15, 10] jogos [39, 14, 17, 8, 41, 29] — a tabela conta 14 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [14, 7, 2, 5, 12, 8] jogos [39, 20, 9, 10, 44, 25] — a tabela conta 14 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Cascavel tabela [14, 5, 5, 4, 14, 16] jogos [39, 17, 11, 11, 51, 36] — a tabela conta 14 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Londrina tabela [14, 6, 3, 5, 9, 15] jogos [39, 18, 10, 11, 54, 38] — a tabela conta 14 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Coritiba tabela [14, 5, 5, 4, 12, 10] jogos [33, 16, 8, 9, 44, 25] — a tabela conta 14 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [14, 4, 5, 5, 12, 16] jogos [32, 15, 11, 6, 41, 29] — a tabela conta 14 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase final / -: União Bandeirante tabela [14, 4, 3, 7, 15, 18] jogos [33, 14, 9, 10, 40, 34] — a tabela conta 14 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase final / -: Toledo FC tabela [14, 2, 5, 7, 10, 16] jogos [33, 11, 11, 11, 31, 29] — a tabela conta 14 jogos e as fontes trazem 33
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Agroceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarapuava
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- Agroceres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Agroceres)
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Guarapuava — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarapuava)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pato Branco — clube que o ogol não tem; entra só pela RSSSF
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vencedor da final pelos jogos (Cascavel) diferente do campeão oficial (Colorado-PR); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Londrina

### 1981

- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [6, 2, 4, 0, 8, 3] jogos [12, 4, 4, 4, 12, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Londrina tabela [6, 2, 3, 1, 7, 5] jogos [12, 6, 4, 2, 16, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Cascavel tabela [11, 3, 4, 4, 1, 15] jogos [11, 3, 4, 4, 14, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Colorado-PR tabela [11, 3, 4, 4, 7, 8] jogos [12, 4, 4, 4, 8, 8] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [11, 3, 4, 4, 7, 12] jogos [12, 3, 4, 5, 7, 13] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Londrina tabela [6, 4, 1, 1, 9, 5] jogos [12, 6, 4, 2, 16, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [6, 2, 0, 4, 4, 7] jogos [12, 4, 4, 4, 12, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Final / -: Londrina tabela [38, 20, 9, 9, 30, 49] jogos [38, 20, 9, 9, 53, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Matsubara tabela [28, 9, 7, 12, 24, 28] jogos [28, 9, 8, 11, 24, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Colorado-PR tabela [23, 7, 9, 7, 18, 17] jogos [24, 8, 9, 7, 19, 17] — a tabela conta 23 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Toledo FC tabela [22, 6, 7, 9, 14, 23] jogos [23, 6, 7, 10, 14, 24] — a tabela conta 22 jogos e as fontes trazem 23
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): A. C. Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- A. C. Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)

### 1982

- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [11, 5, 6, 0, 16, 8] jogos [10, 4, 6, 0, 14, 7] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Grêmio Maringá tabela [11, 5, 4, 2, 14, 10] jogos [11, 5, 4, 2, 15, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Matsubara tabela [11, 4, 1, 6, 13, 16] jogos [10, 4, 1, 5, 12, 14] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Toledo FC tabela [11, 2, 5, 4, 8, 13] jogos [10, 1, 5, 4, 7, 13] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: União Bandeirante tabela [11, 1, 6, 4, 9, 13] jogos [10, 1, 6, 3, 9, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [11, 6, 5, 0, 16, 7] jogos [12, 7, 5, 0, 20, 7] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Colorado-PR tabela [11, 6, 3, 2, 12, 6] jogos [13, 7, 4, 2, 15, 8] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Matsubara tabela [11, 5, 4, 2, 13, 12] jogos [12, 5, 4, 3, 14, 13] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [11, 5, 3, 3, 14, 14] jogos [12, 5, 3, 4, 14, 18] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [11, 2, 3, 6, 8, 14] jogos [10, 2, 3, 5, 7, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: União Bandeirante tabela [11, 2, 3, 6, 5, 11] jogos [9, 2, 2, 5, 5, 9] — a tabela conta 11 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / -: União Bandeirante tabela [11, 4, 5, 2, 10, 5] jogos [12, 4, 6, 2, 10, 5] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [39, 22, 15, 2, 70, 25] jogos [37, 21, 14, 2, 67, 23] — a tabela conta 39 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Matsubara tabela [34, 14, 6, 14, 35, 42] jogos [33, 14, 6, 13, 34, 40] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Primeira fase / -: União Bandeirante tabela [34, 7, 15, 12, 24, 29] jogos [31, 7, 14, 10, 24, 26] — a tabela conta 34 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / -: Toledo FC tabela [33, 6, 15, 12, 22, 37] jogos [30, 4, 14, 12, 18, 35] — a tabela conta 33 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [33, 8, 10, 15, 29, 37] jogos [32, 8, 10, 14, 28, 35] — a tabela conta 33 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- vice pela Wikipédia (sem final de dois clubes): Colorado-PR

### 1983

- tabela publicada x jogos — Fase final / -: Coritiba tabela [6, 4, 1, 1, 5, 1] jogos [20, 8, 7, 5, 17, 13] — a tabela conta 6 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [6, 3, 1, 2, 4, 3] jogos [12, 3, 5, 4, 7, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Grêmio Maringá tabela [6, 3, 0, 3, 5, 5] jogos [12, 5, 3, 4, 10, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [6, 1, 0, 5, 4, 9] jogos [20, 7, 5, 8, 18, 19] — a tabela conta 6 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / Grupo A: Toledo FC tabela [6, 3, 2, 1, 9, 6] jogos [8, 3, 3, 2, 9, 8] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / Grupo A: Pinheiros-PR tabela [6, 2, 2, 2, 5, 4] jogos [12, 5, 5, 2, 13, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Grupo A: Londrina tabela [6, 1, 4, 1, 4, 5] jogos [8, 2, 5, 1, 6, 5] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / Grupo A: Operário-PR tabela [6, 1, 2, 3, 6, 9] jogos [12, 1, 4, 7, 10, 19] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Grupo B: União Bandeirante tabela [6, 3, 3, 0, 13, 3] jogos [11, 6, 5, 0, 18, 5] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / Grupo B: Matsubara tabela [6, 1, 5, 0, 6, 4] jogos [9, 0, 7, 2, 6, 8] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / Grupo B: Pato Branco tabela [6, 1, 3, 2, 3, 8] jogos [1, 0, 0, 1, 2, 6] — a tabela conta 6 jogos e as fontes trazem 1
- tabela publicada x jogos — Fase final / Grupo B: Cascavel tabela [6, 0, 3, 3, 3, 10] jogos [9, 1, 3, 5, 7, 15] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: Colorado-PR tabela [11, 6, 3, 2, 12, 7] jogos [22, 12, 6, 4, 24, 14] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Londrina tabela [11, 5, 4, 2, 12, 6] jogos [22, 8, 9, 5, 18, 11] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [11, 6, 1, 4, 12, 8] jogos [22, 14, 3, 5, 30, 16] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Toledo FC tabela [11, 5, 3, 3, 8, 5] jogos [22, 6, 8, 8, 17, 20] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Pinheiros-PR tabela [11, 5, 3, 3, 8, 7] jogos [22, 7, 10, 5, 15, 13] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Cascavel tabela [11, 3, 6, 2, 11, 10] jogos [22, 4, 10, 8, 18, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [11, 4, 3, 4, 14, 11] jogos [22, 10, 5, 7, 33, 19] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Matsubara tabela [11, 4, 2, 5, 6, 11] jogos [22, 5, 7, 10, 11, 21] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Pato Branco tabela [11, 2, 5, 4, 6, 9] jogos [22, 4, 11, 7, 13, 19] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Grêmio Maringá tabela [11, 1, 6, 4, 7, 10] jogos [22, 7, 9, 6, 20, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [11, 1, 5, 5, 6, 10] jogos [22, 3, 8, 11, 13, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: União Bandeirante tabela [11, 1, 5, 5, 3, 11] jogos [22, 4, 10, 8, 11, 19] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Londrina tabela [6, 3, 2, 1, 5, 2] jogos [18, 5, 8, 5, 11, 12] — a tabela conta 6 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [6, 2, 2, 2, 8, 7] jogos [20, 7, 5, 8, 18, 19] — a tabela conta 6 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Toledo FC tabela [6, 2, 2, 2, 4, 5] jogos [14, 6, 4, 4, 15, 14] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Colorado-PR tabela [6, 0, 4, 2, 3, 6] jogos [12, 3, 5, 4, 7, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Grupo A: Pinheiros-PR tabela [6, 3, 3, 0, 8, 3] jogos [12, 5, 5, 2, 13, 7] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Grupo A: Pato Branco tabela [6, 1, 5, 0, 3, 7] jogos [6, 1, 5, 0, 4, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / Grupo A: Operário-PR tabela [6, 0, 2, 4, 4, 10] jogos [12, 1, 4, 7, 10, 19] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / Grupo B: União Bandeirante tabela [6, 3, 3, 0, 5, 2] jogos [11, 6, 5, 0, 18, 5] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / Grupo B: Cascavel tabela [5, 1, 1, 3, 4, 6] jogos [9, 1, 3, 5, 7, 15] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / Grupo B: Matsubara tabela [5, 0, 3, 2, 2, 4] jogos [9, 0, 7, 2, 6, 8] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [6, 3, 2, 1, 4, 2] jogos [20, 7, 5, 8, 18, 19] — a tabela conta 6 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Coritiba tabela [6, 2, 3, 1, 4, 3] jogos [20, 8, 7, 5, 17, 13] — a tabela conta 6 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Londrina tabela [6, 2, 1, 3, 2, 5] jogos [18, 5, 8, 5, 11, 12] — a tabela conta 6 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: União Bandeirante tabela [6, 1, 2, 3, 4, 4] jogos [24, 9, 10, 5, 28, 15] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Londrina tabela [40, 14, 16, 10, 29, 23] jogos [40, 13, 17, 10, 29, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: União Bandeirante tabela [46, 13, 19, 14, 41, 32] jogos [46, 13, 20, 13, 39, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Pinheiros-PR tabela [38, 14, 16, 8, 31, 25] jogos [38, 14, 16, 8, 32, 23] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- vencedor da final pelos jogos (União Bandeirante) diferente do campeão oficial (Athletico-PR); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1984

- tabela publicada x jogos — Segunda fase / -: Colorado-PR tabela [11, 6, 4, 1, 13, 5] jogos [10, 5, 4, 1, 11, 4] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Paranavaí tabela [11, 2, 5, 4, 10, 12] jogos [10, 2, 5, 3, 9, 10] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Terceira fase / -: Coritiba tabela [11, 4, 4, 3, 16, 4] jogos [11, 4, 4, 3, 16, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Grêmio Maringá tabela [11, 3, 6, 2, 13, 11] jogos [11, 3, 6, 2, 12, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Londrina tabela [11, 4, 3, 4, 14, 16] jogos [10, 3, 3, 4, 12, 15] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Terceira fase / -: Matsubara tabela [11, 1, 5, 5, 7, 11] jogos [10, 1, 5, 4, 6, 9] — a tabela conta 11 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1985

- tabela publicada x jogos — 1º Turno / -: Athletico-PR tabela [11, 7, 2, 2, 14, 9] jogos [28, 15, 6, 7, 32, 21] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Pinheiros-PR tabela [11, 5, 5, 1, 10, 4] jogos [28, 12, 13, 3, 30, 15] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Coritiba tabela [11, 6, 2, 3, 16, 8] jogos [27, 10, 9, 8, 30, 20] — a tabela conta 11 jogos e as fontes trazem 27
- tabela publicada x jogos — 1º Turno / -: Londrina tabela [11, 5, 3, 3, 16, 9] jogos [28, 7, 11, 10, 26, 26] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: União Bandeirante tabela [11, 5, 3, 3, 8, 9] jogos [28, 10, 11, 7, 26, 20] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Grêmio Maringá tabela [11, 4, 3, 4, 14, 8] jogos [28, 10, 9, 9, 27, 25] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Toledo FC tabela [11, 3, 6, 2, 7, 8] jogos [28, 5, 14, 9, 16, 24] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Cascavel tabela [11, 2, 8, 1, 9, 6] jogos [28, 9, 13, 6, 25, 22] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Apucarana tabela [11, 1, 6, 4, 6, 10] jogos [28, 7, 14, 7, 20, 23] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Matsubara tabela [11, 2, 4, 5, 4, 9] jogos [28, 7, 12, 9, 17, 23] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Pato Branco tabela [11, 1, 3, 7, 6, 16] jogos [27, 4, 8, 15, 17, 33] — a tabela conta 11 jogos e as fontes trazem 27
- tabela publicada x jogos — 1º Turno / -: Colorado-PR tabela [11, 1, 3, 7, 5, 19] jogos [28, 6, 10, 12, 20, 34] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [11, 6, 2, 3, 14, 7] jogos [28, 15, 6, 7, 32, 21] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Pinheiros-PR tabela [11, 4, 6, 1, 12, 6] jogos [28, 12, 13, 3, 30, 15] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [11, 4, 5, 2, 11, 8] jogos [28, 6, 10, 12, 20, 34] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [11, 4, 5, 2, 11, 10] jogos [28, 9, 13, 6, 25, 22] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Apucarana tabela [11, 4, 4, 3, 6, 7] jogos [28, 7, 14, 7, 20, 23] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: União Bandeirante tabela [11, 3, 6, 2, 10, 5] jogos [28, 10, 11, 7, 26, 20] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Matsubara tabela [11, 3, 6, 2, 8, 9] jogos [28, 7, 12, 9, 17, 23] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [11, 3, 5, 3, 8, 6] jogos [27, 10, 9, 8, 30, 20] — a tabela conta 11 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [11, 3, 5, 3, 6, 9] jogos [28, 10, 9, 9, 27, 25] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Pato Branco tabela [11, 2, 3, 6, 10, 15] jogos [27, 4, 8, 15, 17, 33] — a tabela conta 11 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [11, 1, 5, 5, 4, 10] jogos [28, 7, 11, 10, 26, 26] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Toledo FC tabela [11, 1, 4, 6, 4, 12] jogos [28, 5, 14, 9, 16, 24] — a tabela conta 11 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [22, 13, 4, 5, 28, 16] jogos [28, 15, 6, 7, 32, 21] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Pinheiros-PR tabela [22, 9, 11, 2, 22, 10] jogos [28, 12, 13, 3, 30, 15] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [22, 9, 7, 6, 24, 14] jogos [27, 10, 9, 8, 30, 20] — a tabela conta 22 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: União Bandeirante tabela [22, 8, 9, 5, 18, 14] jogos [28, 10, 11, 7, 26, 20] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [22, 6, 13, 3, 20, 16] jogos [28, 9, 13, 6, 25, 22] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [22, 7, 8, 7, 20, 17] jogos [28, 10, 9, 9, 27, 25] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Apucarana tabela [22, 5, 10, 7, 12, 17] jogos [28, 7, 14, 7, 20, 23] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [22, 6, 8, 8, 20, 19] jogos [28, 7, 11, 10, 26, 26] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Matsubara tabela [22, 5, 10, 7, 12, 18] jogos [28, 7, 12, 9, 17, 23] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [22, 5, 8, 9, 16, 27] jogos [28, 6, 10, 12, 20, 34] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Toledo FC tabela [22, 4, 10, 8, 11, 20] jogos [28, 5, 14, 9, 16, 24] — a tabela conta 22 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Pato Branco tabela [22, 3, 6, 13, 16, 31] jogos [27, 4, 8, 15, 17, 33] — a tabela conta 22 jogos e as fontes trazem 27
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- campeão pela lista oficial, Athletico-PR; o 1º pela soma dos jogos da última fase é Cascavel (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Pinheiros-PR

### 1986

- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [11, 2, 7, 2, 4, 4] jogos [11, 2, 7, 2, 5, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Pinheiros-PR tabela [6, 1, 5, 0, 5, 4] jogos [12, 4, 8, 0, 12, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Cascavel tabela [6, 2, 3, 1, 5, 4] jogos [12, 2, 6, 4, 10, 15] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [6, 2, 2, 2, 8, 6] jogos [12, 3, 3, 6, 13, 14] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [11, 5, 5, 1, 16, 8] jogos [22, 11, 5, 6, 30, 22] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Londrina tabela [11, 5, 4, 2, 16, 9] jogos [22, 10, 7, 5, 28, 17] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Pinheiros-PR tabela [11, 5, 4, 2, 12, 7] jogos [22, 12, 6, 4, 33, 16] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Cascavel tabela [11, 4, 6, 1, 16, 8] jogos [22, 10, 8, 4, 33, 21] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Colorado-PR tabela [11, 4, 5, 2, 13, 9] jogos [22, 7, 8, 7, 22, 21] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [11, 4, 4, 3, 16, 13] jogos [22, 6, 11, 5, 21, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: União Bandeirante tabela [11, 2, 6, 3, 10, 13] jogos [22, 5, 8, 9, 15, 22] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Grêmio Maringá tabela [11, 1, 8, 2, 14, 17] jogos [22, 6, 10, 6, 27, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Apucarana tabela [11, 3, 3, 5, 8, 14] jogos [22, 4, 9, 9, 17, 29] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Platinense tabela [11, 2, 5, 4, 7, 10] jogos [22, 8, 7, 7, 19, 17] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Matsubara tabela [11, 1, 6, 4, 5, 11] jogos [22, 4, 9, 9, 16, 24] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Toledo FC tabela [11, 2, 0, 9, 9, 23] jogos [22, 3, 4, 15, 18, 42] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Segunda fase / -: Pinheiros-PR tabela [6, 3, 3, 0, 7, 4] jogos [12, 4, 8, 0, 12, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [6, 1, 1, 4, 5, 8] jogos [12, 3, 3, 6, 13, 14] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Cascavel tabela [6, 0, 3, 3, 5, 11] jogos [12, 2, 6, 4, 10, 15] — a tabela conta 6 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)

### 1987

- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [11, 5, 4, 2, 15, 10] jogos [16, 7, 6, 3, 22, 13] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [11, 5, 3, 3, 11, 8] jogos [16, 7, 5, 4, 14, 11] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [11, 5, 3, 3, 13, 10] jogos [16, 5, 7, 4, 15, 13] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [11, 4, 5, 2, 10, 7] jogos [16, 5, 7, 4, 14, 14] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [11, 3, 6, 2, 12, 9] jogos [16, 4, 8, 4, 17, 15] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Pinheiros-PR tabela [11, 2, 2, 7, 5, 12] jogos [16, 4, 4, 8, 9, 15] — a tabela conta 11 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Pinheiros-PR tabela [10, 6, 3, 1, 12, 7] jogos [32, 14, 10, 8, 38, 31] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [10, 5, 4, 1, 14, 4] jogos [32, 14, 12, 6, 44, 25] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Colorado-PR tabela [10, 3, 3, 4, 12, 13] jogos [32, 10, 13, 9, 34, 32] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [10, 2, 4, 4, 9, 13] jogos [32, 10, 11, 11, 34, 33] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [10, 2, 3, 5, 10, 14] jogos [32, 8, 15, 9, 31, 32] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [10, 2, 3, 5, 6, 12] jogos [32, 11, 11, 10, 29, 26] — a tabela conta 10 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- campeão pela lista oficial, Pinheiros-PR; o 1º pela soma dos jogos da última fase é Athletico-PR (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1988

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)

### 1989

- tabela publicada x jogos — 3º Turno / Grupo B: Foz do Iguaçu EC tabela [24, 7, 9, 8, 14, 15] jogos [24, 8, 8, 8, 14, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / Grupo B: Umuarama tabela [24, 5, 10, 9, 16, 30] jogos [24, 5, 9, 10, 16, 30] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)

### 1990

- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [11, 9, 1, 1, 21, 1] jogos [17, 11, 4, 2, 27, 6] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Paraná tabela [11, 6, 4, 1, 26, 8] jogos [17, 8, 8, 1, 32, 10] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [11, 5, 6, 0, 17, 8] jogos [17, 7, 8, 2, 21, 12] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Matsubara tabela [11, 5, 5, 1, 20, 10] jogos [17, 7, 8, 2, 29, 18] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Toledo FC tabela [11, 5, 5, 1, 12, 5] jogos [11, 5, 5, 1, 12, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Batel tabela [11, 5, 3, 3, 13, 9] jogos [17, 7, 3, 7, 17, 16] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [11, 4, 4, 3, 15, 9] jogos [17, 6, 5, 6, 18, 13] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Operário-PR tabela [11, 4, 6, 1, 9, 6] jogos [17, 6, 9, 2, 19, 11] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Campo Mourão tabela [11, 5, 3, 3, 18, 14] jogos [17, 7, 4, 6, 21, 21] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Apucarana tabela [11, 4, 4, 3, 14, 10] jogos [17, 6, 6, 5, 18, 13] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Platinense tabela [11, 4, 4, 3, 15, 18] jogos [17, 4, 4, 9, 18, 32] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Umuarama tabela [11, 2, 4, 5, 7, 11] jogos [11, 2, 4, 5, 7, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [11, 1, 6, 4, 8, 13] jogos [17, 6, 7, 4, 23, 19] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Arapongas tabela [11, 1, 0, 10, 4, 18] jogos [11, 1, 0, 10, 4, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Athletico-PR tabela [12, 6, 5, 1, 0, 15] jogos [31, 15, 11, 5, 45, 30] — a tabela conta 12 jogos e as fontes trazem 31
- tabela publicada x jogos — 2º Turno / -: Paraná tabela [6, 2, 4, 0, 6, 3] jogos [29, 12, 13, 4, 43, 19] — a tabela conta 6 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Grêmio Maringá tabela [6, 1, 4, 1, 4, 5] jogos [27, 9, 12, 6, 24, 18] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [6, 2, 2, 2, 4, 4] jogos [27, 9, 13, 5, 27, 20] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [6, 2, 1, 3, 3, 4] jogos [27, 9, 10, 8, 29, 22] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Platinense tabela [6, 0, 0, 6, 3, 14] jogos [27, 8, 6, 13, 34, 46] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Coritiba tabela [6, 2, 3, 1, 6, 5] jogos [31, 19, 9, 3, 55, 18] — a tabela conta 6 jogos e as fontes trazem 31
- tabela publicada x jogos — 2º Turno / -: Operário-PR tabela [6, 2, 3, 1, 10, 5] jogos [29, 12, 11, 6, 34, 20] — a tabela conta 6 jogos e as fontes trazem 29
- tabela publicada x jogos — 2º Turno / -: Matsubara tabela [6, 2, 3, 1, 9, 8] jogos [27, 13, 11, 3, 48, 27] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Apucarana tabela [6, 2, 2, 2, 4, 3] jogos [27, 10, 8, 9, 27, 21] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Campo Mourão tabela [6, 2, 1, 3, 3, 7] jogos [27, 11, 7, 9, 29, 29] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Batel tabela [6, 2, 0, 4, 4, 7] jogos [27, 10, 7, 10, 29, 31] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Operário-PR tabela [35, 14, 14, 7, 44, 25] jogos [29, 12, 11, 6, 34, 20] — a tabela conta 35 jogos e as fontes trazem 29
- tabela publicada x jogos — Final / -: Paraná tabela [35, 14, 17, 4, 49, 23] jogos [29, 12, 13, 4, 43, 19] — a tabela conta 35 jogos e as fontes trazem 29
- tabela publicada x jogos — Final / -: Londrina tabela [33, 11, 15, 7, 31, 24] jogos [27, 9, 13, 5, 27, 20] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Apucarana tabela [33, 12, 10, 11, 31, 24] jogos [27, 10, 8, 9, 27, 21] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Matsubara tabela [33, 15, 14, 4, 57, 35] jogos [27, 13, 11, 3, 48, 27] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Platinense tabela [33, 8, 6, 19, 37, 60] jogos [27, 8, 6, 13, 34, 46] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Batel tabela [33, 12, 7, 14, 33, 38] jogos [27, 10, 7, 10, 29, 31] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Campo Mourão tabela [33, 13, 8, 12, 32, 36] jogos [27, 11, 7, 9, 29, 29] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Cascavel tabela [33, 11, 11, 11, 32, 26] jogos [27, 9, 10, 8, 29, 22] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Grêmio Maringá tabela [33, 10, 16, 7, 28, 23] jogos [27, 9, 12, 6, 24, 18] — a tabela conta 33 jogos e as fontes trazem 27
- tabela publicada x jogos — Final / -: Toledo FC tabela [21, 8, 6, 7, 20, 21] jogos [21, 8, 6, 7, 20, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Arapongas tabela [21, 3, 4, 14, 9, 27] jogos [21, 3, 4, 14, 9, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Umuarama tabela [21, 4, 9, 8, 12, 22] jogos [21, 4, 9, 8, 12, 23] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 9 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Arapongas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Mourão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- 9 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (9 de Julho)
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Arapongas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Arapongas)
- Campo Mourão — clube que o ogol não tem; entra só pela RSSSF
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- MAC — clube que o ogol não tem; entra só pela RSSSF
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Athletico-PR

### 1991

- tabela publicada x jogos — Primeira fase / -: Apucarana tabela [8, 5, 3, 0, 11, 3] jogos [9, 5, 4, 0, 12, 4] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: Campo Mourão tabela [8, 4, 3, 1, 15, 4] jogos [9, 5, 3, 1, 16, 4] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: Paranavaí tabela [8, 1, 1, 6, 5, 21] jogos [9, 1, 1, 7, 5, 23] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / -: Apucarana tabela [8, 3, 3, 2, 6, 4] jogos [17, 8, 7, 2, 18, 8] — a tabela conta 8 jogos e as fontes trazem 17
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / -: Toledo FC tabela [8, 2, 3, 3, 2, 7] jogos [18, 5, 10, 3, 9, 11] — a tabela conta 8 jogos e as fontes trazem 18
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / -: Arapongas tabela [8, 2, 2, 4, 8, 8] jogos [18, 7, 6, 5, 22, 17] — a tabela conta 8 jogos e as fontes trazem 18
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / -: Matsubara tabela [12, 9, 1, 2, 23, 9] jogos [48, 23, 12, 13, 65, 40] — a tabela conta 12 jogos e as fontes trazem 48
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo E: Campo Mourão tabela [12, 6, 3, 3, 18, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo E: Goioerê tabela [12, 3, 5, 4, 9, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo E: Paranavaí tabela [12, 2, 6, 4, 13, 17] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo E: Platinense tabela [12, 1, 5, 6, 10, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo E: Batel tabela [12, 1, 4, 7, 11, 19] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Foz do Iguaçu EC tabela [12, 5, 5, 2, 9, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Cascavel tabela [12, 5, 4, 3, 13, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Iguaçu tabela [12, 4, 4, 4, 11, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Umuarama tabela [12, 3, 6, 3, 17, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: União Bandeirante tabela [12, 2, 7, 3, 14, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Pato Branco tabela [12, 3, 5, 4, 7, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — leva um ponto extra para a Fase Final. Todas as equipes / Grupo F: Mixto Bordô tabela [12, 3, 3, 6, 7, 17] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [26, 12, 10, 4, 31, 21] jogos [34, 15, 15, 4, 39, 25] — a tabela conta 26 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Grêmio Maringá tabela [26, 10, 8, 8, 29, 32] jogos [34, 12, 11, 11, 32, 36] — a tabela conta 26 jogos e as fontes trazem 34
- tabela publicada x jogos — Segunda fase / -: Matsubara tabela [26, 9, 8, 9, 29, 24] jogos [48, 23, 12, 13, 65, 40] — a tabela conta 26 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Apucarana tabela [26, 7, 10, 9, 24, 25] jogos [43, 15, 17, 11, 42, 33] — a tabela conta 26 jogos e as fontes trazem 43
- tabela publicada x jogos — Segunda fase / -: Foz do Iguaçu EC tabela [26, 8, 8, 10, 24, 33] jogos [48, 16, 15, 17, 40, 50] — a tabela conta 26 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Cascavel tabela [26, 7, 9, 10, 18, 29] jogos [48, 17, 15, 16, 43, 48] — a tabela conta 26 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Campo Mourão tabela [26, 8, 6, 12, 28, 32] jogos [47, 19, 12, 16, 62, 47] — a tabela conta 26 jogos e as fontes trazem 47
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [26, 2, 15, 9, 16, 28] jogos [44, 7, 25, 12, 25, 39] — a tabela conta 26 jogos e as fontes trazem 44
- tabela publicada x jogos — Segunda fase / -: Arapongas tabela [26, 3, 5, 18, 16, 50] jogos [44, 10, 11, 23, 38, 67] — a tabela conta 26 jogos e as fontes trazem 44
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 9 de Julho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Arapongas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campo Mourão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maringá Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mixto Bordô
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Umuarama
- 9 de Julho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (9 de Julho)
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Arapongas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Arapongas)
- Campo Mourão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campo Mourão)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Maringá Atlético — clube que o ogol não tem; entra só pela RSSSF
- Mixto Bordô — clube que o ogol não tem; entra só pela RSSSF
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- Umuarama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1992

- tabela publicada x jogos — 2º Turno / -: Paraná tabela [6, 5, 0, 1, 15, 8] jogos [27, 19, 3, 5, 48, 22] — a tabela conta 6 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Londrina tabela [6, 3, 1, 2, 7, 5] jogos [30, 11, 15, 4, 38, 24] — a tabela conta 6 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Operário-PR tabela [6, 2, 1, 3, 5, 7] jogos [25, 14, 4, 7, 35, 20] — a tabela conta 6 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Cascavel tabela [6, 1, 0, 5, 4, 11] jogos [25, 9, 6, 10, 25, 30] — a tabela conta 6 jogos e as fontes trazem 25
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): APUCARANA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): COMERCIAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CORITIBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): IGUAÇU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): LONDRINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PARANÁ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PATO BRANCO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PLATINENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pato Branco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SPORT CAMPO MOURÃO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): UMUARAMA
- APUCARANA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- COMERCIAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- CORITIBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- IGUAÇU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- LONDRINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- PARANÁ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- PATO BRANCO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- PLATINENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- Pato Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pato Branco)
- SPORT CAMPO MOURÃO — clube que o ogol não tem; entra só pela RSSSF
- UMUARAMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)

### 1993

- tabela publicada x jogos — Torneio de rebaixamento / -: Iguaçu tabela [10, 3, 2, 5, 5, 8] jogos [10, 3, 1, 6, 5, 10] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): APUCARANA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CARAMURU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CORITIBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FRANCISCO BELTRÃO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): IGUAÇU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): LONDRINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PARANAVAÍ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PARANÁ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PLATINENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): UMUARAMA
- APUCARANA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- CARAMURU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caramuru)
- CORITIBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- FRANCISCO BELTRÃO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- IGUAÇU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- LONDRINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- PARANAVAÍ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- PARANÁ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- PLATINENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- UMUARAMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Umuarama)
- vice pela Wikipédia (sem final de dois clubes): Londrina

### 1994

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coronel Vivida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Coronel Vivida — clube que o ogol não tem; entra só pela RSSSF
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vice pela Wikipédia (sem final de dois clubes): Londrina

### 1995

- tabela publicada x jogos — Segunda fase / -: Matsubara tabela [7, 5, 1, 1, 12, 7] jogos [14, 7, 2, 5, 18, 20] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [7, 4, 2, 1, 11, 4] jogos [14, 7, 4, 3, 17, 10] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Paraná tabela [13, 7, 3, 3, 1, 9] jogos [14, 6, 5, 3, 17, 11] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [7, 3, 3, 1, 12, 2] jogos [14, 8, 3, 3, 23, 11] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [7, 2, 1, 4, 10, 11] jogos [14, 6, 3, 5, 23, 14] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Batel tabela [7, 1, 4, 2, 8, 10] jogos [14, 4, 8, 2, 18, 14] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Rio Branco-PR tabela [7, 1, 1, 5, 6, 19] jogos [14, 3, 1, 10, 11, 30] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [7, 0, 3, 4, 4, 12] jogos [14, 0, 4, 10, 6, 23] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [7, 5, 0, 2, 11, 9] jogos [14, 8, 3, 3, 23, 11] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [7, 4, 2, 1, 13, 3] jogos [14, 6, 3, 5, 23, 14] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Batel tabela [7, 3, 4, 0, 10, 4] jogos [14, 4, 8, 2, 18, 14] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Paraná tabela [7, 3, 2, 2, 8, 4] jogos [14, 6, 5, 3, 17, 11] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [7, 3, 2, 2, 6, 6] jogos [14, 7, 4, 3, 17, 10] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Matsubara tabela [7, 2, 1, 4, 6, 13] jogos [14, 7, 2, 5, 18, 20] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Rio Branco-PR tabela [7, 2, 0, 5, 5, 11] jogos [14, 3, 1, 10, 11, 30] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Toledo FC tabela [7, 0, 1, 6, 2, 11] jogos [14, 0, 4, 10, 6, 23] — a tabela conta 7 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coronel Vivida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ponta Grossa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PR)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Coronel Vivida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coronel Vivida)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Ponta Grossa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponta Grossa)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1996

- tabela publicada x jogos — Primeira fase / Chave A: Londrina tabela [4, 2, 2, 0, 5, 3] jogos [1, 0, 1, 0, 1, 1] — a tabela conta 4 jogos e as fontes trazem 1
- tabela publicada x jogos — Primeira fase / Chave A: Francisco Beltrão tabela [4, 2, 0, 2, 3, 4] jogos [2, 1, 0, 1, 1, 2] — a tabela conta 4 jogos e as fontes trazem 2
- tabela publicada x jogos — Primeira fase / Chave A: Rio Branco-PR tabela [4, 1, 1, 2, 3, 4] jogos [2, 0, 1, 1, 0, 1] — a tabela conta 4 jogos e as fontes trazem 2
- tabela publicada x jogos — Primeira fase / Chave A: Matsubara tabela [4, 0, 1, 3, 3, 6] jogos [1, 0, 0, 1, 0, 1] — a tabela conta 4 jogos e as fontes trazem 1
- tabela publicada x jogos — Primeira fase / Chave B: Coritiba tabela [4, 2, 1, 1, 3, 2] jogos [3, 1, 1, 1, 1, 2] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — Primeira fase / Chave B: Batel tabela [4, 1, 0, 3, 2, 5] jogos [3, 1, 0, 2, 2, 3] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — Primeira fase / Chave C: Paranavaí tabela [4, 4, 0, 0, 10, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Maringá FC 1995 tabela [4, 2, 1, 1, 5, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Ponta Grossa tabela [4, 1, 2, 1, 4, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Grêmio Maringá tabela [4, 1, 0, 3, 6, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Foz do Iguaçu tabela [4, 0, 1, 3, 2, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave A: Londrina tabela [5, 3, 1, 1, 7, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave A: Francisco Beltrão tabela [5, 2, 1, 2, 5, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave A: Matsubara tabela [5, 2, 1, 2, 12, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave A: Paraná tabela [5, 1, 2, 2, 8, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave A: Rio Branco-PR tabela [5, 1, 0, 4, 3, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave B: Coritiba tabela [5, 5, 0, 0, 20, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave B: Athletico-PR tabela [5, 3, 2, 0, 7, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave B: União Bandeirante tabela [5, 2, 2, 1, 7, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave B: Batel tabela [5, 1, 1, 3, 6, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave B: Toledo FC tabela [5, 0, 0, 5, 4, 15] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Maringá FC 1995 tabela [5, 3, 2, 0, 9, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Grêmio Maringá tabela [5, 3, 2, 0, 8, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Ponta Grossa tabela [5, 3, 0, 2, 11, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Paranavaí tabela [5, 1, 2, 2, 6, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave C: Foz do Iguaçu tabela [5, 1, 1, 3, 6, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave D: Apucarana tabela [5, 2, 2, 1, 9, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave D: Cascavel tabela [5, 2, 2, 1, 6, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave D: Jandaia tabela [5, 1, 3, 1, 4, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave D: Arapongas tabela [5, 1, 0, 4, 5, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Chave D: Coronel Vivida tabela [5, 1, 0, 4, 5, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave E: Athletico-PR tabela [7, 5, 1, 1, 18, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave E: Ponta Grossa tabela [7, 3, 1, 3, 8, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave E: Apucarana tabela [7, 1, 2, 4, 8, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave E: Jandaia tabela [7, 1, 2, 4, 5, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave F: Coritiba tabela [7, 7, 0, 0, 24, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave F: Rio Branco-PR tabela [7, 2, 2, 3, 9, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave F: Londrina tabela [7, 2, 1, 4, 7, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave F: Grêmio Maringá tabela [7, 1, 2, 4, 5, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave G: União Bandeirante tabela [7, 6, 0, 1, 10, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave G: Maringá FC 1995 tabela [7, 2, 4, 1, 12, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave G: Francisco Beltrão tabela [7, 2, 1, 4, 8, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave G: Batel tabela [7, 0, 3, 4, 5, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Chave H: Paranavaí tabela [7, 2, 4, 1, 7, 6] jogos [5, 1, 3, 1, 3, 3] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / Chave H: Paraná tabela [7, 3, 2, 2, 7, 5] jogos [2, 1, 0, 1, 3, 2] — a tabela conta 7 jogos e as fontes trazem 2
- tabela publicada x jogos — Segunda fase / Chave H: Matsubara tabela [7, 1, 3, 3, 11, 14] jogos [5, 1, 3, 1, 10, 11] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — Terceira fase / Série I: Paraná tabela [7, 6, 1, 0, 17, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Série I: Coritiba tabela [7, 3, 4, 0, 11, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Série I: Ponta Grossa tabela [7, 1, 3, 3, 6, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Série I: Maringá FC 1995 tabela [7, 1, 1, 5, 3, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Série J: Athletico-PR tabela [7, 4, 2, 1, 14, 9] jogos [3, 2, 1, 0, 7, 5] — a tabela conta 7 jogos e as fontes trazem 3
- tabela publicada x jogos — Terceira fase / Série J: União Bandeirante tabela [7, 2, 2, 3, 10, 12] jogos [6, 2, 2, 2, 9, 10] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Terceira fase / Série J: Rio Branco-PR tabela [7, 0, 5, 2, 8, 13] jogos [6, 0, 5, 1, 7, 9] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: Coritiba tabela [3, 2, 1, 0, 7, 1] jogos [13, 9, 3, 1, 29, 11] — a tabela conta 3 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [3, 1, 2, 0, 3, 2] jogos [11, 6, 4, 1, 22, 10] — a tabela conta 3 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Paraná tabela [3, 1, 1, 1, 5, 6] jogos [11, 6, 4, 1, 16, 6] — a tabela conta 3 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: União Bandeirante tabela [3, 0, 0, 3, 3, 9] jogos [17, 7, 4, 6, 21, 22] — a tabela conta 3 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: Paraná tabela [3, 2, 1, 0, 6, 0] jogos [11, 6, 4, 1, 16, 6] — a tabela conta 3 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Coritiba tabela [3, 2, 0, 1, 6, 5] jogos [13, 9, 3, 1, 29, 11] — a tabela conta 3 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase final / -: Athletico-PR tabela [3, 1, 1, 1, 3, 2] jogos [11, 6, 4, 1, 22, 10] — a tabela conta 3 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: União Bandeirante tabela [3, 0, 0, 3, 1, 9] jogos [17, 7, 4, 6, 21, 22] — a tabela conta 3 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Arapongas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coronel Vivida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jandaia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ponta Grossa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Arapongas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Arapongas)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Coronel Vivida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coronel Vivida)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Jandaia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jandaia)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Ponta Grossa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponta Grossa)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vencedor da final pelos jogos (Coritiba) diferente do campeão oficial (Paraná); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Coritiba

### 1997

- tabela publicada x jogos — Primeira fase / Grupo B: Apucarana tabela [8, 6, 1, 1, 21, 9] jogos [8, 6, 1, 1, 21, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Iraty tabela [8, 5, 3, 0, 20, 8] jogos [8, 5, 3, 0, 19, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Cascavel tabela [6, 2, 2, 2, 13, 12] jogos [7, 2, 3, 2, 13, 12] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / Grupo B: Mixto Bordô tabela [7, 1, 1, 5, 10, 26] jogos [8, 1, 2, 5, 10, 26] — a tabela conta 7 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Foz do Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iguaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mixto Bordô
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paranavaí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Platinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ponta Grossa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Foz do Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Foz do Iguaçu)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Iguaçu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iguaçu)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Mixto Bordô — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mixto Bordô)
- Paranavaí — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paranavaí)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Platinense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Platinense)
- Ponta Grossa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponta Grossa)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 1998

- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [11, 8, 2, 1, 28, 5] jogos [14, 10, 3, 1, 32, 6] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [11, 6, 4, 1, 21, 11] jogos [14, 8, 5, 1, 25, 12] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Iraty tabela [11, 6, 2, 3, 17, 18] jogos [14, 6, 2, 6, 18, 23] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Paraná tabela [11, 4, 4, 3, 11, 7] jogos [14, 5, 4, 5, 13, 11] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Maringá FC 1995 tabela [11, 0, 1, 10, 10, 28] jogos [11, 0, 1, 10, 9, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Combined Table first and second stage / -: Maringá FC 1995 tabela [22, 2, 2, 18, 23, 54] jogos [22, 2, 2, 18, 22, 53] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Coritiba tabela [3, 3, 0, 0, 8, 1] jogos [31, 18, 8, 5, 57, 31] — a tabela conta 3 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [3, 2, 0, 1, 6, 3] jogos [31, 23, 6, 2, 71, 22] — a tabela conta 3 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / -: Paraná tabela [3, 0, 1, 2, 2, 5] jogos [28, 11, 8, 9, 36, 28] — a tabela conta 3 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: Iraty tabela [3, 0, 1, 2, 3, 10] jogos [28, 10, 5, 13, 37, 49] — a tabela conta 3 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Athletico-PR tabela [3, 2, 1, 0, 4, 1] jogos [31, 23, 6, 2, 71, 22] — a tabela conta 3 jogos e as fontes trazem 31
- tabela publicada x jogos — Segunda fase / -: Coritiba tabela [3, 2, 1, 0, 4, 1] jogos [31, 18, 8, 5, 57, 31] — a tabela conta 3 jogos e as fontes trazem 31
- tabela publicada x jogos — Segunda fase / -: Paraná tabela [3, 1, 0, 2, 2, 4] jogos [28, 11, 8, 9, 36, 28] — a tabela conta 3 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Iraty tabela [3, 0, 0, 3, 1, 5] jogos [28, 10, 5, 13, 37, 49] — a tabela conta 3 jogos e as fontes trazem 28
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ponta Grossa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Ponta Grossa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponta Grossa)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 1999

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Apucarana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iraty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Malutrom
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Apucarana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Apucarana)
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Iraty — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iraty)
- Malutrom — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (J.Malucelli)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)

### 2000

- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [11, 2, 5, 4, 12, 17] jogos [10, 2, 4, 4, 11, 16] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Batel tabela [11, 2, 1, 8, 11, 20] jogos [10, 2, 0, 8, 10, 19] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [11, 2, 5, 4, 12, 17] jogos [10, 2, 4, 4, 11, 16] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Batel tabela [11, 2, 1, 8, 11, 20] jogos [10, 2, 0, 8, 10, 19] — a tabela conta 11 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Coritiba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francisco Beltrão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Londrina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Malutrom
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paraná
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Branco
- Coritiba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Coritiba)
- Francisco Beltrão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francisco Beltrão)
- Londrina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Londrina)
- Malutrom — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (J.Malucelli)
- Paraná — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraná)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-PR)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Athletico-PR

### 2001

- placar diferente no ogol — Athletico-PR x Paraná (2001-05-27): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Athletico-PR x Paraná (2001-06-03): RSSSF 1-1, ogol 2-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Athletico-PR x Paraná, ogol 2001-05-27); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Athletico-PR

### 2002

- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Grêmio Maringá x Iraty, ogol 2002-04-10); fica a do ogol
- vice pela Wikipédia (sem final de dois clubes): Grêmio Maringá

### 2002 Supercampeonato

- sem ocorrências

### 2003

- tabela publicada x jogos — Final / -: Londrina tabela [13, 5, 7, 1, 23, 16] jogos [14, 6, 7, 1, 25, 16] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Final / -: Prudentópolis EC tabela [13, 4, 5, 4, 19, 25] jogos [14, 4, 5, 5, 19, 27] — a tabela conta 13 jogos e as fontes trazem 14
- placar diferente no ogol — Paranavaí x Prudentópolis EC (2003-03-09): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- ano errado na data da RSSSF — Prudentópolis EC 1-1 Londrina: RSSSF 2003-03-16, ogol 3003-03-16; fica a do ogol
- jogo só no ogol, incluído em Semi-finals: Paranavaí 2-2 Coritiba (2003-03-15)
- jogo só no ogol, incluído em Disputa do 3º lugar: Londrina 2-0 Prudentópolis EC (3003-03-20)
- só na RSSSF (não achado no ogol): Londrina 3-0 Prudentópolis EC (2003-03-20)

### 2004

- tabela publicada x jogos — Segunda fase / Grupo D: Rio Branco-PR tabela [4, 0, 0, 4, 4, 9] jogos [5, 0, 1, 4, 4, 9] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / Grupo D: Francisco Beltrão tabela [4, 0, 0, 4, 3, 9] jogos [5, 0, 1, 4, 3, 9] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — Torneio de rebaixamento / -: Nacional-PR tabela [6, 3, 1, 2, 10, 6] jogos [6, 3, 1, 2, 9, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2005

- jogo só no ogol, incluído em First Phase / Group B: Nacional-PR 2-0 Londrina (0000-00-00)
- jogo só no ogol, incluído em First Phase / Group B: J.Malucelli 2-0 Iraty (0000-00-00)
- jogo só no ogol, incluído em First Phase / Group A: Coritiba 2-1 Engenheiro Beltrão (2005-01-19)
- jogo só no ogol, incluído em First Phase / Group A: Rio Branco-PR 0-2 Paraná (2005-02-05)

### 2006

- sem ocorrências

### 2007

- tabela publicada x jogos — Primeira fase / -: Galo Maringá tabela [15, 8, 6, 1, 32, 18] jogos [14, 8, 5, 1, 31, 17] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: J.Malucelli tabela [15, 5, 5, 5, 24, 22] jogos [14, 5, 4, 5, 23, 21] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Iguaçu tabela [15, 4, 4, 7, 14, 29] jogos [15, 3, 5, 7, 13, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Portuguesa Londrinense tabela [15, 2, 6, 7, 14, 19] jogos [15, 2, 7, 6, 14, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Nacional-PR tabela [15, 1, 2, 12, 17, 40] jogos [15, 1, 3, 11, 17, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Galo Maringá tabela [15, 8, 6, 1, 32, 18] jogos [14, 8, 5, 1, 31, 17] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: J.Malucelli tabela [15, 5, 5, 5, 24, 22] jogos [14, 5, 4, 5, 23, 21] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Iguaçu tabela [15, 4, 4, 7, 14, 29] jogos [15, 3, 5, 7, 13, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Portuguesa Londrinense tabela [15, 2, 6, 7, 14, 19] jogos [15, 2, 7, 6, 14, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Nacional-PR tabela [15, 1, 2, 12, 17, 40] jogos [15, 1, 3, 11, 17, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Galo Maringá tabela [21, 10, 7, 4, 37, 28] jogos [20, 10, 6, 4, 36, 27] — a tabela conta 21 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: J.Malucelli tabela [15, 5, 5, 5, 24, 22] jogos [14, 5, 4, 5, 23, 21] — a tabela conta 15 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Iguaçu tabela [15, 4, 4, 7, 14, 29] jogos [15, 3, 5, 7, 13, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Portuguesa Londrinense tabela [15, 2, 6, 7, 14, 19] jogos [15, 2, 7, 6, 14, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Nacional-PR tabela [15, 1, 2, 12, 17, 40] jogos [15, 1, 3, 11, 17, 39] — há jogo do clube sem conferência no ogol
- jogo anulado ou cancelado fica de fora: J.Malucelli 1-1 Adap/Galo (2007-01-31) [This match was cancelled and a replay, starting at 1-0, was ordered by the FA, for the referee allowed kick-off while a player was still celebrating J. Malucelli's goal on Galo's side of the pitch; the replay was later cancelled, and the result stood]
- jogo do ogol tirado junto com o da RSSSF: JMalucelli 1-1 Galo Maringá (2007-01-31)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Cascavel CR x Engenheiro Beltrão, ogol 2007-01-21); fica a do ogol
- jogo só no ogol, incluído em First Phase: Iguaçu 0-0 Nacional-PR (2007-02-25)

### 2008

- sem ocorrências

### 2009

- campeão pela lista oficial, Athletico-PR; o 1º pela soma dos jogos da última fase é J.Malucelli (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): J.Malucelli

### 2010

- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 2011

- tabela publicada x jogos — Fase final / -: Operário-PR tabela [22, 12, 4, 6, 35, 25] jogos [24, 13, 4, 7, 36, 28] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Cianorte tabela [22, 10, 4, 8, 33, 25] jogos [24, 11, 4, 9, 36, 26] — a tabela conta 22 jogos e as fontes trazem 24
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Rio Branco-PR x Athletico-PR, ogol 2011-05-30); fica a do ogol
- só na RSSSF (não achado no ogol): Cianorte 3-0 Operário-PR (2011-05-08)
- só na RSSSF (não achado no ogol): Operário-PR 1-0 Cianorte (2011-05-15)
- vencedor da final pelos jogos (Cianorte) diferente do campeão oficial (Coritiba); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 2012

- tabela publicada x jogos — Primeira fase / -: Roma Apucarana tabela [11, 2, 5, 4, 11, 20] jogos [11, 2, 5, 4, 10, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [11, 2, 3, 6, 14, 21] jogos [11, 2, 3, 6, 15, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Roma Apucarana tabela [11, 2, 5, 4, 11, 20] jogos [11, 2, 5, 4, 10, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Operário-PR tabela [11, 2, 3, 6, 14, 21] jogos [11, 2, 3, 6, 15, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Paranavaí x Coritiba (2012-02-01): RSSSF 1-2, ogol 1-3; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: Londrina x Athletico-PR, ogol 2012-03-01); fica a do ogol
- vencedor da final pelos jogos (Cianorte) diferente do campeão oficial (Coritiba); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Athletico-PR

### 2013

- tabela publicada x jogos — Segunda fase / -: Londrina tabela [11, 8, 1, 2, 19, 7] jogos [13, 9, 1, 3, 22, 10] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [11, 6, 3, 2, 21, 10] jogos [13, 7, 3, 3, 24, 13] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Londrina tabela [11, 8, 1, 2, 19, 7] jogos [13, 9, 1, 3, 22, 10] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Operário-PR tabela [11, 6, 3, 2, 21, 10] jogos [13, 7, 3, 3, 24, 13] — a tabela conta 11 jogos e as fontes trazem 13
- só na RSSSF (não achado no ogol): Operário-PR 2-1 Londrina (2013-05-05)
- só na RSSSF (não achado no ogol): Londrina 2-1 Operário-PR (2013-05-12)

### 2014

- jogo só no ogol, incluído em Final: Rio Branco-PR 1-2 Prudentópolis (2014-04-10)
- jogo só no ogol, incluído em Final: Prudentópolis 1-0 Rio Branco-PR (2014-04-12)
- vencedor da final pelos jogos (Prudentópolis) diferente do campeão oficial (Londrina); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Maringá

### 2015

- tabela publicada x jogos — Primeira fase / -: Athletico-PR tabela [6, 4, 1, 1, 14, 5] jogos [17, 7, 3, 7, 26, 15] — a tabela conta 6 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Rio Branco-PR tabela [6, 2, 2, 2, 7, 6] jogos [17, 5, 3, 9, 15, 20] — a tabela conta 6 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Nacional-PR tabela [6, 2, 2, 2, 4, 8] jogos [17, 3, 3, 11, 16, 37] — a tabela conta 6 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Prudentópolis tabela [6, 0, 3, 3, 5, 11] jogos [17, 0, 6, 11, 10, 34] — a tabela conta 6 jogos e as fontes trazem 17

### 2016

- sem ocorrências

### 2017

- jogo anulado ou cancelado fica de fora: Londrina 1-3 J Malucelli (2017-04-02) [Cancelled]  (O J Malucelli perdeu 16 pontos na 1ª Fase, sendo eliminado da competição. Este jogo foi cancelado posteriormente)]
- só na RSSSF (não achado no ogol): Londrina 4-1 Cianorte (2017-04-30)
- só na RSSSF (não achado no ogol): Cianorte 1-1 Londrina (2017-05-07)

### 2018

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- jogo só no ogol, incluído em 1º Turno - Final: Coritiba 3-0 Rio Branco-PR (2018-02-25)
- jogo só no ogol, incluído em 2º Turno - Final: Athletico-PR 1-0 Londrina (2018-03-29)

### 2019

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2020

- jogo só no ogol, incluído em Quartas de final: Rio Branco-PR 0-3 FC Cascavel (2020-07-18)
- jogo só no ogol, incluído em Quartas de final: Cianorte 0-1 Operário-PR (2020-07-18)
- jogo só no ogol, incluído em Quartas de final: Paraná 0-1 Coritiba (2020-07-19)
- jogo só no ogol, incluído em Quartas de final: Londrina 1-1 Athletico-PR (2020-07-19)
- jogo só no ogol, incluído em Quartas de final: FC Cascavel 5-0 Rio Branco-PR (2020-07-22)
- jogo só no ogol, incluído em Quartas de final: Operário-PR 0-2 Cianorte (2020-07-23)
- jogo só no ogol, incluído em Quartas de final: Athletico-PR 5-0 Londrina (2020-07-23)
- jogo só no ogol, incluído em Quartas de final: Coritiba 2-1 Paraná (2020-07-24)
- jogo só no ogol, incluído em Semifinal: Cianorte 2-3 Coritiba (2020-07-26)
- jogo só no ogol, incluído em Semifinal: Athletico-PR 5-1 FC Cascavel (2020-07-26)
- jogo só no ogol, incluído em Semifinal: FC Cascavel 0-0 Athletico-PR (2020-07-29)
- jogo só no ogol, incluído em Semifinal: Coritiba 2-0 Cianorte (2020-07-30)
- jogo só no ogol, incluído em Final: Athletico-PR 1-0 Coritiba (2020-08-02)
- jogo só no ogol, incluído em Final: Coritiba 1-2 Athletico-PR (2020-08-06)

### 2021

- placar corrigido pelo ogol — Londrina x Cianorte (2021-03-21): RSSSF 0-3, ogol 3-3; fica o do ogol, que fecha com a tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Londrina

### 2022

- sem ocorrências

### 2023

- sem ocorrências

### 2024

- tabela publicada x jogos — Primeira fase / -: Azuriz Futebol tabela [11, 5, 2, 4, 13, 12] jogos [11, 5, 2, 4, 12, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Galo Maringá 2020 tabela [11, 1, 4, 6, 13, 23] jogos [11, 1, 4, 6, 13, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Coritiba tabela [13, 8, 3, 2, 26, 9] jogos [15, 8, 4, 3, 28, 13] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Final / -: Maringá tabela [12, 6, 4, 2, 18, 10] jogos [17, 7, 6, 4, 23, 17] — a tabela conta 12 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Operário-PR tabela [12, 5, 3, 4, 11, 9] jogos [15, 6, 4, 5, 13, 11] — a tabela conta 12 jogos e as fontes trazem 15
- tabela publicada x jogos — Final / -: Azuriz Futebol tabela [12, 5, 3, 4, 12, 12] jogos [13, 5, 3, 5, 12, 13] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Final / -: FC Cascavel tabela [12, 5, 3, 4, 11, 11] jogos [13, 5, 4, 4, 12, 12] — a tabela conta 12 jogos e as fontes trazem 13
- jogo só no ogol, incluído em 1ª FASE: FC Cascavel 1-0 Cianorte (2024-02-15)
- jogo só no ogol, incluído em 1ª FASE: Azuriz Futebol 1-0 PSTC (2024-02-25)

### 2025

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Operário-PR

### 2026

- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Londrina tabela [8, 5, 2, 1, 14, 3] jogos [12, 5, 7, 0, 19, 7] — a tabela conta 8 jogos e as fontes trazem 12
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Athletico-PR tabela [7, 4, 1, 2, 10, 6] jogos [10, 5, 2, 3, 20, 10] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Coritiba tabela [8, 2, 3, 3, 11, 12] jogos [10, 4, 4, 2, 14, 11] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Operário-PR tabela [7, 1, 4, 2, 5, 7] jogos [12, 3, 6, 3, 12, 12] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: São Joseense tabela [7, 4, 0, 3, 5, 4] jogos [8, 3, 3, 2, 6, 5] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Azuriz Futebol tabela [7, 3, 3, 1, 6, 5] jogos [8, 3, 2, 3, 5, 8] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Cianorte tabela [8, 1, 4, 3, 11, 12] jogos [8, 1, 4, 3, 8, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: FC Cascavel tabela [7, 0, 5, 2, 5, 7] jogos [8, 3, 3, 2, 8, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Foz do Iguaçu tabela [7, 2, 2, 3, 11, 10] jogos [8, 3, 2, 3, 12, 18] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Galo Maringá 2020 tabela [7, 2, 0, 5, 6, 13] jogos [8, 1, 0, 7, 5, 20] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Maringá tabela [7, 2, 2, 3, 7, 10] jogos [8, 4, 2, 2, 16, 7] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — CLASSIFICAÇÃO 1ª FASE / -: Andraus tabela [7, 1, 1, 5, 7, 16] jogos [8, 1, 1, 6, 7, 16] — a tabela conta 7 jogos e as fontes trazem 8
- jogo só no ogol, incluído em Torneio de rebaixamento: Foz do Iguaçu 1-3 Athletico-PR (2026-02-07)
- jogo só no ogol, incluído em Torneio de rebaixamento: Londrina 1-1 São Joseense (2026-02-07)
- jogo só no ogol, incluído em Torneio de rebaixamento: Coritiba 2-0 Cianorte (2026-02-08)
- jogo só no ogol, incluído em Torneio de rebaixamento: Azuriz Futebol 0-2 Operário-PR (2026-02-08)
- jogo só no ogol, incluído em Final: Londrina 0-0 Operário-PR (2026-03-07)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Operário-PR

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- De 1925 a 1976 o ogol não tem os jogos: o clube é casado pelo nome com o das outras temporadas.
- Clube que o ogol não tem entra pela RSSSF, com código "rs-<nome>". Nunca com o nome exato de outro clube (regra 6b).

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
