# Campeonato Pernambucano (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-pe-1/importar.py`. Pacote em `data/coleta/bra-pe-1/pacote/`. Mesmo código do Baiano
(`docs/coleta/bra-ba-1.md`), com as fontes de Pernambuco.

**Temporadas:** 1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 27/11/2026). Nenhum título dividido. A
edição 2026/27 (Turno Forró em 2026, Turno Frevo em 2027) fica de fora até terminar. Edições sem página da RSSSF e sem
jogos no ogol (1991-1993) entram só com campeão e vice.

**Fontes:** RSSSF Brasil (`tablesfq/pe{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada
edição e o código de cada clube); Wikipédia em português (artigo "Campeonato Pernambucano de Futebol Masculino":
campeão e vice de cada ano, segunda fonte).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15); vitória sem placar conhecido também (como no Mineiro), com o vencedor na observação. Autores dos
gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo
nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1915 | RSSSF + ogol | 6 | 18 (18) | 35 | 0 | 2 / 0 | Flamengo Recife | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 | RSSSF + ogol | 9 | 34 (34) | 152 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1917 | RSSSF + ogol | 9 | 30 (30) | 150 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1918 | RSSSF + ogol | 6 | 30 (30) | 141 | 0 | 1 / 0 | América-PE | RSSSF (classificação geral publicada) |
| 1919 | RSSSF + ogol | 8 | 28 (28) | 131 | 0 | 1 / 0 | América-PE | RSSSF (classificação geral publicada) |
| 1920 | RSSSF | 8 | 51 (0) | 160 | 0 | 1 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF | 8 | 50 (0) | 155 | 0 | 1 / 1 | América-PE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF | 8 | 28 (0) | 72 | 0 | 1 / 0 | América-PE | RSSSF (classificação geral publicada) |
| 1923 | RSSSF | 8 | 56 (0) | 218 | 0 | 0 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 | RSSSF | 8 | 41 (0) | 173 | 0 | 0 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 | RSSSF | 6 | 30 (0) | 120 | 0 | 0 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 | RSSSF | 8 | 36 (0) | 117 | 0 | 0 / 1 | Torre | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 | RSSSF | 7 | 42 (0) | 131 | 0 | 1 / 0 | América-PE | RSSSF (classificação geral publicada) |
| 1928 | RSSSF | 7 | 42 (0) | 162 | 0 | 1 / 0 | Sport | RSSSF (classificação geral publicada) |
| 1929 | RSSSF | 8 | 48 (0) | 154 | 0 | 0 / 1 | Torre | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF | 8 | 36 (0) | 139 | 0 | 1 / 0 | Torre | RSSSF (classificação geral publicada) |
| 1931 | RSSSF | 11 | 55 (0) | 314 | 0 | 1 / 0 | Santa Cruz | RSSSF (classificação geral publicada) |
| 1932 | RSSSF | 11 | 52 (0) | 296 | 0 | 2 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 | RSSSF | 14 | 87 (0) | 433 | 0 | 2 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 | RSSSF | 8 | 57 (0) | 257 | 0 | 1 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 | RSSSF | 8 | 55 (0) | 359 | 0 | 0 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 | RSSSF | 9 | 55 (0) | 349 | 0 | 0 / 1 | Tramways-PE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF | 9 | 67 (0) | 375 | 0 | 0 / 1 | Tramways-PE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF | 8 | 56 (0) | 336 | 0 | 2 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF | 5 | 40 (0) | 204 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF | 8 | 76 (0) | 331 | 0 | 2 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF | 7 | 35 (0) | 194 | 0 | 1 / 2 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF | 5 | 47 (0) | 186 | 0 | 6 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF | 6 | 22 (0) | 110 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 | RSSSF | 7 | 64 (0) | 311 | 2 | 1 / 2 | América-PE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF | 7 | 52 (0) | 266 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF | 6 | 27 (0) | 125 | 0 | 1 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF | 7 | 66 (0) | 316 | 0 | 2 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 5 | 33 (0) | 132 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 8 | 40 (0) | 183 | 0 | 1 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF | 5 | 43 (0) | 152 | 0 | 1 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 5 | 43 (0) | 144 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 7 | 72 (0) | 210 | 0 | 1 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF | 7 | 48 (0) | 193 | 0 | 1 / 2 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 7 | 54 (0) | 170 | 0 | 2 / 2 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 8 | 67 (0) | 237 | 0 | 1 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 8 | 67 (0) | 220 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 8 | 74 (0) | 288 | 0 | 5 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF | 9 | 102 (0) | 393 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF | 6 | 63 (0) | 228 | 0 | 2 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 6 | 61 (0) | 279 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF | 7 | 65 (0) | 204 | 0 | 1 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF | 6 | 62 (0) | 193 | 0 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF | 8 | 89 (0) | 260 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF | 8 | 86 (0) | 311 | 0 | 1 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF | 7 | 75 (0) | 257 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF | 8 | 89 (0) | 301 | 0 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF | 8 | 53 (0) | 140 | 0 | 3 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF | 8 | 63 (0) | 191 | 0 | 2 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF | 8 | 90 (0) | 281 | 0 | 2 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF | 8 | 89 (0) | 228 | 0 | 2 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF | 6 | 48 (0) | 127 | 0 | 1 / 3 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 8 | 86 (0) | 228 | 0 | 1 / 2 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 8 | 120 (0) | 339 | 0 | 4 / 0 | Santa Cruz | RSSSF (classificação geral publicada) |
| 1974 | RSSSF | 9 | 104 (0) | 301 | 0 | 0 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 8 | 107 (0) | 307 | 0 | 1 / 3 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF + ogol | 8 | 109 (109) | 303 | 0 | 0 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 6 | 96 (0) | 220 | 0 | 2 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 8 | 89 (0) | 283 | 0 | 5 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 9 | 126 (0) | 374 | 0 | 5 / 5 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF | 10 | 146 (0) | 374 | 0 | 1 / 9 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF | 10 | 160 (0) | 430 | 0 | 6 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF | 12 | 177 (0) | 499 | 0 | 0 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF | 11 | 165 (0) | 471 | 0 | 4 / 14 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 11 | 66 (0) | 180 | 0 | 0 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 11 | 157 (0) | 414 | 0 | 8 / 4 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 11 | 116 (0) | 332 | 0 | 15 / 5 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF | 11 | 83 (0) | 186 | 0 | 4 / 2 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 10 | 101 (0) | 268 | 0 | 4 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 12 | 142 (0) | 370 | 2 | 4 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF | 12 | 37 (0) | 93 | 0 | 2 / 2 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | ogol | 2 | 2 (2) | 9 | 0 | 0 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1993 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1994 | RSSSF | 16 | 177 (0) | 512 | 0 | 3 / 6 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 10 | 184 (0) | 571 | 0 | 4 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 9 | 124 (0) | 322 | 0 | 0 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 11 | 96 (0) | 259 | 0 | 6 / 3 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF | 11 | 114 (0) | 337 | 0 | 1 / 7 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 10 | 133 (133) | 343 | 0 | 3 / 2 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 10 | 122 (121) | 366 | 0 | 3 / 2 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 10 | 136 (124) | 378 | 0 | 2 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 10 | 92 (92) | 254 | 0 | 3 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 10 | 115 (111) | 375 | 10 | 2 / 2 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 10 | 92 (92) | 268 | 255 | 3 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 10 | 90 (90) | 277 | 0 | 3 / 0 | Santa Cruz | RSSSF (classificação geral publicada) |
| 2006 | RSSSF + ogol | 10 | 92 (92) | 255 | 0 | 3 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 10 | 97 (90) | 285 | 0 | 0 / 3 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 12 | 132 (102) | 384 | 0 | 2 / 4 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 12 | 132 (132) | 373 | 0 | 5 / 0 | Sport | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 12 | 144 (144) | 409 | 284 | 3 / 0 | Sport | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 12 | 144 (144) | 378 | 0 | 3 / 0 | Santa Cruz | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 12 | 138 (138) | 357 | 0 | 2 / 1 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 12 | 138 (138) | 380 | 242 | 2 / 6 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 12 | 147 (110) | 326 | 309 | 2 / 1 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 12 | 128 (124) | 303 | 292 | 3 / 2 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 12 | 92 (92) | 187 | 0 | 4 / 4 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 12 | 95 (95) | 220 | 210 | 9 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 11 | 64 (64) | 145 | 140 | 2 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 10 | 54 (54) | 153 | 146 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 10 | 57 (57) | 134 | 125 | 3 / 0 | Salgueiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 10 | 57 (57) | 142 | 0 | 1 / 4 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 10 | 57 (57) | 167 | 0 | 1 / 1 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 13 | 84 (84) | 198 | 40 | 2 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 10 | 53 (53) | 136 | 0 | 1 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 10 | 53 (53) | 125 | 117 | 1 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | RSSSF + ogol | 8 | 38 (38) | 111 | 99 | 6 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1915

- jogo só no ogol, incluído em Fase única: América-PE 0-0 Peres (1915-10-17)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1916

- placar diferente no ogol — Náutico x Casa Forte (1916-07-09): RSSSF 6-1, ogol 6-0; fica o da RSSSF

### 1917

- sem ocorrências

### 1918

- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1919

- vice pela Wikipédia (sem final de dois clubes): Sport

### 1920

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Peres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Varzeano FC
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Peres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Peres)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Varzeano FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Varzeano)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1921

- tabela publicada x jogos — Primeira fase / -: América-PE tabela [13, 8, 3, 2, 27, 16] jogos [14, 8, 4, 2, 31, 17] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Santa Cruz tabela [13, 8, 3, 2, 25, 14] jogos [14, 7, 3, 4, 26, 18] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Sport tabela [13, 7, 3, 3, 33, 15] jogos [13, 8, 3, 2, 33, 15] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Peres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Varzeano FC
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Peres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Peres)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Varzeano FC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Varzeano)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1922

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Peres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Peres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Peres)
- Equador-PE — clube que o ogol não tem; entra só pela RSSSF
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Sport

### 1923

- tabela publicada x jogos — Fase única / -: Náutico tabela [14, 4, 4, 6, 26, 40] jogos [14, 3, 4, 7, 26, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Peres tabela [14, 0, 0, 14, 6, 51] jogos [14, 1, 0, 13, 6, 51] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Peres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Peres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Peres)
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1924

- tabela publicada x jogos — Fase única / -: América-PE tabela [13, 9, 0, 4, 35, 20] jogos [11, 7, 0, 4, 35, 20] — a tabela conta 13 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Torre tabela [13, 8, 2, 3, 21, 13] jogos [11, 6, 2, 3, 21, 13] — a tabela conta 13 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Santa Cruz tabela [12, 7, 1, 4, 25, 17] jogos [11, 6, 1, 4, 25, 17] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Flamengo Recife tabela [12, 6, 2, 4, 28, 18] jogos [10, 4, 2, 4, 28, 18] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Náutico tabela [13, 2, 0, 11, 17, 42] jogos [13, 3, 0, 10, 17, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Equador-PE tabela [7, 1, 0, 6, 3, 9] jogos [3, 1, 0, 2, 3, 9] — a tabela conta 7 jogos e as fontes trazem 3
- tabela publicada x jogos — Fase única / -: Peres tabela [13, 0, 0, 13, 3, 40] jogos [10, 0, 0, 10, 3, 40] — a tabela conta 13 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Peres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Peres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Peres)
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1925

- tabela publicada x jogos — Fase única / -: Santa Cruz tabela [10, 4, 2, 4, 16, 19] jogos [10, 3, 2, 5, 16, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-PE tabela [10, 1, 4, 5, 15, 23] jogos [10, 2, 4, 4, 15, 23] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Torre

### 1926

- tabela publicada x jogos — Fase única / -: Torre tabela [11, 8, 2, 1, 17, 7] jogos [11, 7, 2, 2, 17, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Santa Cruz tabela [11, 5, 3, 3, 13, 14] jogos [11, 4, 4, 3, 13, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Sport tabela [7, 4, 0, 3, 17, 4] jogos [6, 3, 0, 3, 17, 4] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: CS Pernambucano tabela [11, 3, 1, 7, 10, 23] jogos [10, 2, 1, 7, 10, 23] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Flamengo Recife tabela [11, 2, 0, 9, 13, 16] jogos [9, 3, 1, 5, 13, 16] — a tabela conta 11 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CS Pernambucano
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- CS Pernambucano — clube que o ogol não tem; entra só pela RSSSF
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1927

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Torre

### 1928

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Torre

### 1929

- tabela publicada x jogos — Fase única / -: Torre tabela [13, 9, 4, 0, 26, 10] jogos [12, 7, 5, 0, 25, 10] — a tabela conta 13 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Náutico tabela [13, 7, 2, 4, 27, 18] jogos [12, 7, 2, 3, 27, 17] — a tabela conta 13 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: América-PE tabela [13, 6, 2, 5, 27, 17] jogos [13, 6, 3, 4, 27, 17] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Equador-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — clube que o ogol não tem; entra só pela RSSSF
- Equador-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Equador-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1930

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Íris-PE — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1931

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA Arruda
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Israelita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- AA Arruda — clube que o ogol não tem; entra só pela RSSSF
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Fluminense (RE) — clube que o ogol não tem; entra só pela RSSSF
- Israelita — clube que o ogol não tem; entra só pela RSSSF
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1932

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Israelita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Fluminense (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fluminense-PE)
- Great Western — clube que o ogol não tem; entra só pela RSSSF
- Israelita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Israelita)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)

### 1933

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atheniense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Israelita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tuyuty
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Varzeano SC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Atheniense — clube que o ogol não tem; entra só pela RSSSF
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Fluminense (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fluminense-PE)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Israelita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Israelita)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Tuyuty — clube que o ogol não tem; entra só pela RSSSF
- Varzeano SC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Varzeano)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)

### 1934

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1935

- tabela publicada x jogos — Primeira fase / -: Sport tabela [14, 8, 2, 4, 46, 35] jogos [13, 7, 2, 4, 46, 35] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / -: Flamengo Recife tabela [12, 2, 3, 7, 29, 43] jogos [11, 2, 3, 6, 29, 43] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Encruzilhada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Encruzilhada — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Encruzilhada)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Tramways-PE — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Tramways-PE

### 1936

- tabela publicada x jogos — Fase única / -: Náutico tabela [12, 8, 1, 3, 47, 24] jogos [11, 7, 1, 3, 47, 24] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Flamengo Recife tabela [12, 4, 1, 7, 19, 44] jogos [11, 4, 1, 6, 19, 44] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1937

- tabela publicada x jogos — Fase única / -: Tramways-PE tabela [30, 15, 14, 1, 0, 64] jogos [15, 14, 1, 0, 64, 16] — a tabela conta 30 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Náutico tabela [16, 8, 1, 7, 49, 37] jogos [15, 8, 1, 6, 49, 37] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Flamengo Recife tabela [14, 4, 0, 10, 27, 56] jogos [13, 3, 0, 10, 27, 56] — a tabela conta 14 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1938

- tabela publicada x jogos — Fase preliminar / -: Santa Cruz tabela [7, 5, 1, 1, 25, 13] jogos [6, 4, 1, 1, 25, 13] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase preliminar / -: Náutico tabela [7, 4, 2, 1, 23, 15] jogos [6, 3, 2, 1, 23, 15] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase preliminar / -: Great Western tabela [7, 2, 0, 5, 18, 36] jogos [6, 1, 0, 5, 18, 36] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase preliminar / -: Flamengo Recife tabela [7, 0, 0, 7, 3, 38] jogos [4, 0, 0, 4, 3, 38] — a tabela conta 7 jogos e as fontes trazem 4
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íris-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- Íris-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íris-PE)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1939

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1940

- tabela publicada x jogos — Fase preliminar / -: Sport tabela [7, 6, 0, 1, 21, 9] jogos [7, 5, 1, 1, 21, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase preliminar / -: Torre tabela [7, 1, 0, 6, 9, 24] jogos [7, 1, 1, 5, 9, 24] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Torre
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Torre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Torre)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- vencedor da final pelos jogos (Sport) diferente do campeão oficial (Santa Cruz); fica o oficial

### 1941

- tabela publicada x jogos — 2º Turno / -: Sport tabela [6, 5, 1, 0, 24, 6] jogos [11, 10, 1, 0, 49, 10] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Santa Cruz tabela [6, 4, 2, 0, 11, 7] jogos [10, 4, 2, 4, 29, 25] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: América-PE tabela [6, 4, 1, 1, 16, 9] jogos [11, 5, 4, 2, 28, 20] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [6, 2, 0, 4, 14, 15] jogos [11, 5, 1, 5, 36, 24] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Tramways-PE tabela [6, 1, 0, 5, 5, 7] jogos [8, 2, 1, 5, 22, 31] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Flamengo Recife tabela [6, 0, 0, 6, 1, 20] jogos [9, 0, 2, 7, 9, 50] — a tabela conta 6 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways-PE
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Tramways-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways-PE)
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1942

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1943

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- campeão pela lista oficial, Sport; o 1º pela soma dos jogos da última fase é América-PE (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1944

- tabela publicada x jogos — 1º Turno / -: Sport tabela [6, 4, 1, 1, 17, 8] jogos [6, 3, 2, 1, 17, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Portela-PE tabela [6, 1, 1, 4, 12, 15] jogos [6, 1, 2, 3, 12, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Náutico tabela [6, 4, 2, 0, 15, 7] jogos [5, 3, 2, 0, 15, 7] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 3º Turno / -: Sport tabela [6, 4, 1, 1, 12, 7] jogos [5, 3, 1, 1, 12, 7] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 3º Turno / -: Santa Cruz tabela [6, 4, 1, 1, 14, 13] jogos [5, 3, 1, 1, 14, 13] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 3º Turno / -: Flamengo Recife tabela [6, 0, 1, 5, 7, 21] jogos [3, 0, 1, 2, 7, 21] — a tabela conta 6 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portela-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Portela-PE — clube que o ogol não tem; entra só pela RSSSF
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)

### 1945

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portela-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Portela-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portela-PE)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1946

- tabela publicada x jogos — Fase preliminar / -: Santa Cruz tabela [5, 3, 1, 1, 13, 5] jogos [4, 2, 1, 1, 13, 5] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase preliminar / -: Sport tabela [5, 3, 1, 1, 9, 7] jogos [4, 2, 1, 1, 9, 7] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase preliminar / -: Náutico tabela [5, 2, 2, 1, 8, 7] jogos [4, 1, 2, 1, 8, 7] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase preliminar / -: Great Western tabela [5, 1, 1, 3, 5, 14] jogos [4, 0, 1, 3, 5, 14] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase preliminar / -: Flamengo Recife tabela [5, 0, 0, 5, 0, 9] jogos [1, 0, 0, 1, 0, 9] — a tabela conta 5 jogos e as fontes trazem 1
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1947

- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [8, 7, 0, 1, 19, 8] jogos [7, 6, 0, 1, 19, 8] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / -: Flamengo Recife tabela [8, 5, 0, 3, 3, 17] jogos [7, 5, 0, 2, 3, 17] — a tabela conta 8 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Moinho Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Moinho Recife — clube que o ogol não tem; entra só pela RSSSF
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1948

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1949

- tabela publicada x jogos — 1º Turno / -: Great Western tabela [7, 4, 1, 2, 11, 5] jogos [6, 3, 1, 2, 11, 5] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Flamengo Recife tabela [7, 0, 0, 7, 2, 46] jogos [6, 0, 0, 6, 2, 46] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo (RE)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Moinho Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Flamengo (RE) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo Recife)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Moinho Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Moinho Recife)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1950

- tabela publicada x jogos — 2º Turno / -: América-PE tabela [8, 5, 2, 1, 16, 10] jogos [8, 4, 2, 2, 16, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Íbis tabela [8, 0, 0, 8, 7, 24] jogos [8, 1, 0, 7, 7, 24] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1951

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — clube que o ogol não tem; entra só pela RSSSF
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)

### 1952

- tabela publicada x jogos — 2º Turno / -: América-PE tabela [9, 3, 5, 1, 12, 11] jogos [10, 4, 5, 1, 12, 11] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Íbis tabela [9, 2, 2, 5, 12, 21] jogos [10, 2, 2, 6, 12, 21] — a tabela conta 9 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): América-PE

### 1953

- tabela publicada x jogos — 2º Turno / -: Santa Cruz tabela [10, 8, 0, 2, 23, 6] jogos [9, 8, 0, 1, 23, 6] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [10, 6, 0, 4, 19, 11] jogos [8, 6, 0, 2, 19, 11] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Auto Esporte-PE tabela [10, 4, 0, 6, 10, 23] jogos [8, 2, 0, 6, 10, 23] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: Great Western tabela [10, 3, 0, 7, 4, 31] jogos [13, 3, 0, 10, 13, 52] — a tabela conta 10 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1954

- tabela publicada x jogos — 1º Turno / -: Sport tabela [4, 3, 1, 0, 4, 1] jogos [21, 10, 7, 4, 34, 19] — a tabela conta 4 jogos e as fontes trazem 21
- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [4, 2, 2, 0, 9, 3] jogos [18, 10, 5, 3, 33, 14] — a tabela conta 4 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [4, 2, 1, 1, 9, 6] jogos [21, 12, 5, 4, 46, 25] — a tabela conta 4 jogos e as fontes trazem 21
- tabela publicada x jogos — 1º Turno / -: América-PE tabela [4, 1, 0, 3, 6, 10] jogos [17, 7, 3, 7, 35, 26] — a tabela conta 4 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: Auto Esporte-PE tabela [4, 0, 0, 4, 1, 9] jogos [18, 2, 1, 15, 11, 46] — a tabela conta 4 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: América-PE tabela [8, 1, 3, 4, 11, 10] jogos [7, 1, 3, 3, 11, 10] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Auto Esporte-PE tabela [8, 1, 0, 7, 2, 19] jogos [7, 0, 0, 7, 2, 19] — a tabela conta 8 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Great Western
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Great Western — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Great Western)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1955

- tabela publicada x jogos — 1º Turno / -: Sport tabela [14, 11, 2, 1, 45, 10] jogos [13, 10, 2, 1, 45, 10] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [14, 11, 0, 3, 39, 11] jogos [13, 10, 0, 3, 39, 11] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — 1º Turno / -: América-PE tabela [14, 7, 0, 7, 21, 17] jogos [11, 7, 0, 4, 21, 17] — a tabela conta 14 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Íbis tabela [14, 3, 2, 9, 10, 29] jogos [13, 2, 2, 9, 10, 29] — a tabela conta 14 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1956

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Sport

### 1958

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Asas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Auto Esporte-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Asas — clube que o ogol não tem; entra só pela RSSSF
- Auto Esporte-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Auto Esporte-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1959

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Asas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Asas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Asas-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1960

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Asas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Asas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Asas-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1961

- tabela publicada x jogos — 1º Turno / -: Náutico tabela [12, 7, 4, 1, 37, 10] jogos [12, 6, 4, 2, 37, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Íbis tabela [12, 2, 2, 8, 11, 24] jogos [12, 3, 2, 7, 11, 24] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Asas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Asas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Asas-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1962

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1963

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Centro Limoeirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Centro Limoeirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Centro Limoeirense)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1964

- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [14, 6, 3, 5, 29, 24] jogos [14, 5, 3, 6, 29, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Ferroviário Recife tabela [14, 1, 3, 10, 20, 33] jogos [14, 2, 3, 9, 20, 33] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Centro Limoeirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Centro Limoeirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Centro Limoeirense)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Sport

### 1965

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1966

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1967

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Sport

### 1968

- tabela publicada x jogos — 3º Turno / -: Náutico tabela [8, 5, 1, 2, 15, 6] jogos [5, 3, 1, 1, 11, 3] — a tabela conta 8 jogos e as fontes trazem 5
- tabela publicada x jogos — 3º Turno / -: Sport tabela [8, 5, 1, 2, 17, 10] jogos [5, 4, 1, 0, 14, 6] — a tabela conta 8 jogos e as fontes trazem 5
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1969

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1970

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-PE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Recife
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- América-PE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-PE)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport Recife — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1971

- tabela publicada x jogos — 2º Turno / -: Santa Cruz tabela [5, 5, 0, 0, 10, 1] jogos [6, 5, 1, 0, 10, 1] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: América-PE tabela [5, 1, 1, 3, 6, 9] jogos [6, 1, 2, 3, 6, 9] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [5, 0, 2, 3, 4, 7] jogos [6, 0, 3, 3, 4, 7] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Ferroviário Recife tabela [5, 1, 0, 4, 5, 12] jogos [6, 1, 1, 4, 5, 12] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 3º Turno / -: Santa Cruz tabela [5, 2, 2, 1, 12, 5] jogos [5, 2, 2, 1, 12, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Central tabela [5, 2, 2, 1, 7, 8] jogos [5, 2, 2, 1, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Santa Cruz tabela [16, 12, 2, 2, 30, 9] jogos [17, 12, 3, 2, 30, 10] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Náutico tabela [15, 6, 4, 5, 19, 16] jogos [16, 6, 5, 5, 19, 16] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: Central tabela [15, 6, 3, 6, 18, 23] jogos [15, 6, 3, 6, 18, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: América-PE tabela [15, 3, 2, 10, 14, 27] jogos [16, 3, 3, 10, 14, 27] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Final / -: Ferroviário Recife tabela [15, 2, 0, 13, 14, 38] jogos [16, 2, 1, 13, 14, 38] — a tabela conta 15 jogos e as fontes trazem 16
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)

### 1972

- tabela publicada x jogos — 1º Turno / -: América-PE tabela [14, 5, 4, 5, 22, 21] jogos [14, 5, 4, 5, 22, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Íbis tabela [14, 0, 1, 13, 4, 43] jogos [14, 0, 1, 13, 5, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: América-PE tabela [24, 6, 6, 12, 29, 37] jogos [24, 6, 6, 12, 29, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Íbis tabela [14, 0, 1, 13, 4, 43] jogos [14, 0, 1, 13, 5, 43] — há jogo do clube sem conferência no ogol
- jogo anulado ou cancelado fica de fora: América 1-1 Central (1972-03-02) [annulled]
- jogo anulado ou cancelado fica de fora: Sport 1-0 Santo Amaro (1972-03-02) [annulled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Sport

### 1973

- jogo anulado ou cancelado fica de fora: Náutico 2-0 Ferroviário (1973-04-21) [match annulled]
- jogo anulado ou cancelado fica de fora: Sport 0-0 Santa Cruz (1973-06-17) [match annulled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1974

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Desportiva PITU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Desportiva PITU — clube que o ogol não tem; entra só pela RSSSF
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1975

- tabela publicada x jogos — Segunda fase / -: Central tabela [14, 4, 4, 6, 14, 20] jogos [14, 4, 4, 6, 14, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Ferroviário Recife tabela [14, 4, 3, 7, 15, 24] jogos [14, 4, 3, 7, 16, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Quarta fase / -: Sport tabela [10, 7, 3, 0, 72, 14] jogos [33, 25, 7, 1, 91, 18] — a tabela conta 10 jogos e as fontes trazem 33
- tabela publicada x jogos — Quarta fase / -: Náutico tabela [10, 6, 3, 1, 45, 10] jogos [33, 21, 7, 5, 55, 19] — a tabela conta 10 jogos e as fontes trazem 33
- tabela publicada x jogos — Quarta fase / -: Santa Cruz tabela [10, 6, 1, 3, 55, 8] jogos [32, 22, 5, 5, 74, 14] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — Quarta fase / -: Central tabela [10, 1, 4, 5, 19, 35] jogos [32, 6, 9, 17, 25, 55] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — Quarta fase / -: América-PE tabela [10, 0, 5, 5, 33, 36] jogos [32, 4, 9, 19, 24, 58] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — Quarta fase / -: Ferroviário Recife tabela [10, 0, 4, 6, 20, 41] jogos [24, 4, 7, 13, 21, 41] — a tabela conta 10 jogos e as fontes trazem 24
- tabela publicada x jogos — Sexta fase / -: Sport tabela [8, 6, 2, 0, 90, 18] jogos [33, 25, 7, 1, 91, 18] — a tabela conta 8 jogos e as fontes trazem 33
- tabela publicada x jogos — Sexta fase / -: Santa Cruz tabela [8, 6, 1, 1, 74, 13] jogos [32, 22, 5, 5, 74, 14] — a tabela conta 8 jogos e as fontes trazem 32
- tabela publicada x jogos — Sexta fase / -: Náutico tabela [8, 4, 1, 3, 55, 18] jogos [33, 21, 7, 5, 55, 19] — a tabela conta 8 jogos e as fontes trazem 33
- tabela publicada x jogos — Sexta fase / -: Central tabela [8, 1, 1, 6, 28, 54] jogos [32, 6, 9, 17, 25, 55] — a tabela conta 8 jogos e as fontes trazem 32
- tabela publicada x jogos — Sexta fase / -: América-PE tabela [8, 0, 1, 7, 39, 52] jogos [32, 4, 9, 19, 24, 58] — a tabela conta 8 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1976

- placar diferente no ogol — Central x Náutico (1976-03-28): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- jogo só no ogol, incluído em 3. FASE &: Central 1-1 Ferroviário Recife (1976-06-13)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1977

- tabela publicada x jogos — Terceira fase / -: Náutico tabela [10, 6, 3, 1, 14, 4] jogos [11, 7, 3, 1, 15, 4] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Terceira fase / -: Sport tabela [10, 6, 3, 1, 14, 4] jogos [11, 6, 3, 2, 14, 5] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Caruaru — clube que o ogol não tem; entra só pela RSSSF
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)

### 1978

- tabela publicada x jogos — 1º Turno / -: América-PE tabela [7, 3, 1, 3, 8, 18] jogos [7, 3, 1, 3, 8, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Central tabela [7, 2, 1, 4, 8, 18] jogos [7, 2, 1, 4, 8, 8] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1979

- tabela publicada x jogos — 1º Turno / -: Central tabela [8, 4, 0, 4, 10, 18] jogos [7, 4, 0, 3, 9, 16] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / -: Atlético Caruaru tabela [8, 2, 1, 5, 5, 16] jogos [7, 1, 1, 5, 3, 15] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Atlético Caruaru tabela [4, 1, 0, 3, 4, 6] jogos [3, 0, 0, 3, 1, 6] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Íbis tabela [4, 0, 0, 4, 0, 18] jogos [3, 0, 0, 3, 0, 15] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [12, 11, 1, 0, 59, 5] jogos [14, 12, 1, 1, 63, 9] — a tabela conta 12 jogos e as fontes trazem 14
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [11, 9, 1, 1, 32, 6] jogos [13, 10, 1, 2, 36, 10] — a tabela conta 11 jogos e as fontes trazem 13
- tabela publicada x jogos — 1º Turno / -: Central tabela [11, 6, 0, 5, 14, 21] jogos [10, 6, 0, 4, 13, 19] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 1º Turno / -: Atlético Caruaru tabela [12, 3, 1, 8, 9, 22] jogos [10, 1, 1, 8, 4, 21] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — 1º Turno / -: Íbis tabela [12, 0, 0, 12, 1, 51] jogos [11, 0, 0, 11, 1, 48] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [7, 4, 2, 1, 15, 3] jogos [7, 5, 2, 0, 15, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Central tabela [7, 3, 1, 3, 3, 9] jogos [7, 2, 1, 4, 3, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: América-PE tabela [7, 2, 1, 4, 5, 14] jogos [6, 2, 1, 3, 4, 11] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Atlético Caruaru tabela [7, 1, 3, 3, 4, 11] jogos [6, 0, 3, 3, 1, 10] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [10, 8, 2, 0, 33, 5] jogos [39, 31, 4, 4, 134, 23] — a tabela conta 10 jogos e as fontes trazem 39
- tabela publicada x jogos — 1º Turno / -: Sport tabela [10, 8, 2, 0, 23, 5] jogos [35, 22, 6, 7, 68, 30] — a tabela conta 10 jogos e as fontes trazem 35
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [10, 5, 3, 2, 19, 5] jogos [35, 24, 6, 5, 70, 22] — a tabela conta 10 jogos e as fontes trazem 35
- tabela publicada x jogos — 1º Turno / -: América-PE tabela [10, 3, 2, 5, 7, 17] jogos [30, 5, 5, 20, 19, 56] — a tabela conta 10 jogos e as fontes trazem 30
- tabela publicada x jogos — 1º Turno / -: Central tabela [10, 3, 2, 5, 3, 13] jogos [30, 12, 4, 14, 25, 45] — a tabela conta 10 jogos e as fontes trazem 30
- tabela publicada x jogos — 1º Turno / -: Atlético Caruaru tabela [10, 1, 4, 5, 4, 15] jogos [29, 3, 6, 20, 13, 54] — a tabela conta 10 jogos e as fontes trazem 29
- tabela publicada x jogos — 1º Turno / -: Santo Amaro-PE tabela [10, 2, 2, 6, 9, 21] jogos [22, 6, 4, 12, 21, 43] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 1º Turno / -: Ferroviário Recife tabela [10, 1, 1, 8, 7, 24] jogos [21, 5, 1, 15, 23, 53] — a tabela conta 10 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — clube que o ogol não tem; entra só pela RSSSF
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1980

- tabela publicada x jogos — 1º Turno / -: Sport tabela [9, 7, 2, 0, 28, 2] jogos [9, 7, 2, 0, 28, 0] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [9, 7, 0, 2, 26, 6] jogos [9, 6, 1, 2, 26, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Comercial-PE tabela [9, 2, 2, 5, 4, 16] jogos [9, 2, 3, 4, 5, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Santo Amaro-PE tabela [9, 1, 3, 5, 6, 18] jogos [9, 1, 2, 6, 6, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Sport tabela [4, 3, 1, 0, 14, 2] jogos [5, 3, 1, 1, 14, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Santa Cruz tabela [4, 4, 0, 0, 10, 1] jogos [5, 5, 0, 0, 11, 1] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Santo Amaro-PE tabela [4, 2, 1, 1, 9, 2] jogos [4, 2, 1, 1, 8, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Sport tabela [7, 5, 1, 1, 9, 7] jogos [7, 5, 1, 1, 9, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Ferroviário Recife tabela [7, 0, 0, 7, 2, 18] jogos [7, 0, 0, 7, 3, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Segunda fase / -: Sport tabela [3, 3, 0, 0, 3, 0] jogos [4, 4, 0, 0, 6, 1] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno - Segunda fase / -: Náutico tabela [3, 3, 0, 0, 10, 0] jogos [4, 3, 0, 1, 11, 3] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — 3º Turno / -: Náutico tabela [5, 2, 1, 2, 7, 5] jogos [5, 2, 1, 2, 7, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno - Segunda fase / -: Santa Cruz tabela [3, 2, 1, 0, 11, 1] jogos [4, 2, 2, 0, 11, 1] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — 3º Turno - Segunda fase / -: Náutico tabela [3, 3, 0, 0, 14, 0] jogos [4, 3, 1, 0, 14, 0] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — 3º Turno - Segunda fase / -: Caruaru tabela [3, 1, 1, 1, 1, 8] jogos [3, 1, 1, 1, 1, 7] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Comercial — clube que o ogol não tem; entra só pela RSSSF
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1981

- tabela publicada x jogos — 3º Turno - Final / -: Sport tabela [2, 1, 1, 0, 2, 0] jogos [3, 1, 2, 0, 2, 0] — a tabela conta 2 jogos e as fontes trazem 3
- tabela publicada x jogos — 3º Turno - Final / -: Náutico tabela [2, 1, 0, 1, 1, 2] jogos [3, 1, 1, 1, 1, 2] — a tabela conta 2 jogos e as fontes trazem 3
- jogo anulado ou cancelado fica de fora: Central 0-0 Náutico (1981-10-18) [match annulled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1982

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-PE)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1983

- tabela publicada x jogos — 1º Turno - Fase final / -: Náutico tabela [3, 2, 1, 0, 6, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Santa Cruz tabela [3, 2, 0, 1, 5, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Sport tabela [3, 1, 1, 1, 3, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Central tabela [3, 0, 0, 3, 3, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Náutico tabela [5, 4, 1, 0, 18, 2] jogos [6, 5, 1, 0, 20, 3] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Santa Cruz tabela [5, 4, 1, 0, 15, 1] jogos [6, 4, 1, 1, 16, 3] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: América-PE tabela [5, 1, 2, 2, 5, 10] jogos [5, 1, 2, 2, 6, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo B: Sport tabela [4, 4, 0, 0, 15, 3] jogos [5, 5, 0, 0, 16, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo B: Central tabela [4, 3, 0, 1, 8, 5] jogos [5, 3, 0, 2, 8, 6] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Fase final / -: Sport tabela [3, 1, 2, 0, 2, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Náutico tabela [3, 1, 1, 1, 3, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Central tabela [3, 1, 1, 1, 1, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 1º Turno - Fase final / -: Santa Cruz tabela [3, 0, 2, 1, 1, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno / Grupo A: Santa Cruz tabela [5, 4, 1, 0, 17, 2] jogos [6, 5, 1, 0, 18, 2] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / Grupo A: Náutico tabela [5, 3, 2, 0, 15, 1] jogos [6, 3, 2, 1, 15, 2] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / Grupo B: Sport tabela [4, 4, 0, 0, 9, 0] jogos [5, 5, 0, 0, 11, 1] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: Central tabela [4, 3, 0, 1, 5, 1] jogos [5, 3, 0, 2, 6, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / -: Santa Cruz tabela [3, 3, 0, 0, 4, 0] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Sport tabela [3, 2, 0, 1, 4, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Náutico tabela [3, 1, 0, 2, 5, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Central tabela [3, 0, 0, 3, 2, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Sport tabela [4, 4, 0, 0, 19, 1] jogos [5, 4, 1, 0, 20, 2] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Central tabela [4, 3, 0, 1, 15, 4] jogos [5, 3, 1, 1, 16, 5] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Santa Cruz tabela [5, 4, 0, 1, 18, 1] jogos [6, 4, 1, 1, 18, 1] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Náutico tabela [5, 4, 0, 1, 7, 1] jogos [6, 4, 1, 1, 7, 1] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno - Fase final / -: Náutico tabela [3, 2, 1, 0, 3, 0] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Santa Cruz tabela [3, 0, 3, 0, 1, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Central tabela [3, 0, 2, 1, 1, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno - Fase final / -: Sport tabela [3, 0, 2, 1, 2, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [17, 11, 3, 3, 31, 6] jogos [46, 29, 10, 7, 102, 22] — a tabela conta 17 jogos e as fontes trazem 46
- tabela publicada x jogos — 2º Turno / -: Santa Cruz tabela [17, 11, 4, 2, 40, 5] jogos [47, 29, 13, 5, 100, 22] — a tabela conta 17 jogos e as fontes trazem 47
- tabela publicada x jogos — 2º Turno / -: Sport tabela [14, 10, 2, 2, 34, 8] jogos [43, 27, 10, 6, 82, 23] — a tabela conta 14 jogos e as fontes trazem 43
- tabela publicada x jogos — 2º Turno / -: Central tabela [14, 6, 2, 6, 23, 15] jogos [38, 16, 6, 16, 62, 41] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: América-PE tabela [9, 4, 2, 3, 7, 9] jogos [26, 8, 8, 10, 29, 44] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — 2º Turno / -: Sete de Setembro-PE tabela [10, 2, 4, 4, 13, 18] jogos [25, 4, 8, 13, 23, 47] — a tabela conta 10 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Santo Amaro-PE tabela [9, 3, 0, 6, 10, 21] jogos [26, 3, 4, 19, 20, 69] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — 2º Turno / -: 66985 tabela [9, 2, 2, 5, 8, 22] jogos [26, 8, 5, 13, 26, 50] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — 2º Turno / -: Ferroviário Recife tabela [8, 0, 3, 5, 4, 19] jogos [16, 2, 4, 10, 8, 40] — a tabela conta 8 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Íbis tabela [9, 0, 3, 6, 6, 38] jogos [18, 0, 5, 13, 11, 73] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Atlético Caruaru tabela [8, 0, 1, 7, 5, 20] jogos [17, 0, 3, 14, 8, 40] — a tabela conta 8 jogos e as fontes trazem 17
- tabela publicada x jogos — 3º Turno / -: Náutico tabela [7, 6, 0, 1, 19, 3] jogos [8, 6, 0, 2, 19, 4] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — 3º Turno / -: Sport tabela [7, 6, 0, 1, 12, 5] jogos [8, 7, 0, 1, 13, 5] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Náutico tabela [2, 0, 2, 0, 1, 1] jogos [3, 0, 3, 0, 2, 2] — a tabela conta 2 jogos e as fontes trazem 3
- tabela publicada x jogos — Fase final / -: Náutico tabela [47, 29, 11, 7, 103, 23] jogos [46, 29, 10, 7, 102, 22] — a tabela conta 47 jogos e as fontes trazem 46
- tabela publicada x jogos — Fase final / -: Sport tabela [44, 27, 11, 6, 83, 24] jogos [43, 27, 10, 6, 82, 23] — a tabela conta 44 jogos e as fontes trazem 43
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1984

- tabela publicada x jogos — Primeira fase / -: Sport tabela [10, 9, 0, 1, 30, 6] jogos [10, 8, 1, 1, 30, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Atlético Caruaru tabela [10, 2, 3, 5, 8, 16] jogos [10, 2, 4, 4, 9, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-PE tabela [10, 2, 1, 7, 5, 19] jogos [10, 2, 1, 7, 7, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Santo Amaro-PE tabela [10, 0, 1, 9, 2, 28] jogos [10, 0, 1, 9, 2, 30] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- campeão pela lista oficial, Náutico; o 1º pela soma dos jogos da última fase é Sport (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 1985

- tabela publicada x jogos — 1º Turno - Desempate / Grupo B: Íbis tabela [4, 2, 1, 1, 2, 4] jogos [3, 1, 1, 1, 1, 4] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 1º Turno - Desempate / Grupo B: Ferroviário Recife tabela [4, 0, 2, 2, 3, 5] jogos [3, 0, 2, 1, 3, 4] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 3º Turno / Grupo A: Central tabela [5, 3, 0, 2, 13, 8] jogos [5, 3, 0, 2, 13, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / Grupo B: Íbis tabela [4, 1, 1, 2, 5, 7] jogos [4, 1, 1, 2, 5, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno - Segunda fase / Grupo A: Atlético Caruaru tabela [5, 0, 0, 5, 2, 9] jogos [5, 0, 0, 5, 2, 8] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1986

- tabela publicada x jogos — 1º Turno / Grupo B: América-PE tabela [4, 3, 1, 0, 10, 0] jogos [6, 5, 1, 0, 15, 2] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / Grupo B: Íbis tabela [4, 2, 0, 2, 7, 15] jogos [5, 2, 0, 3, 7, 17] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / Grupo B: Santo Amaro-PE tabela [4, 0, 2, 2, 4, 8] jogos [5, 0, 2, 3, 6, 11] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / Grupo B: América-PE tabela [4, 3, 1, 0, 10, 0] jogos [6, 5, 1, 0, 15, 2] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / Grupo B: Íbis tabela [4, 2, 0, 2, 7, 15] jogos [5, 2, 0, 3, 7, 17] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / Grupo B: Santo Amaro-PE tabela [4, 0, 2, 2, 4, 8] jogos [5, 0, 2, 3, 6, 11] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 3º Turno / -: Santa Cruz tabela [6, 3, 2, 1, 11, 4] jogos [7, 3, 3, 1, 13, 6] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 3º Turno / -: Central tabela [6, 3, 2, 1, 7, 5] jogos [7, 3, 3, 1, 9, 7] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 3º Turno / -: Santa Cruz tabela [6, 3, 2, 1, 11, 4] jogos [7, 3, 3, 1, 13, 6] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 3º Turno / -: Central tabela [6, 3, 2, 1, 7, 5] jogos [7, 3, 3, 1, 9, 7] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase final / -: Santa Cruz tabela [29, 14, 9, 6, 45, 23] jogos [29, 14, 9, 6, 46, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Central tabela [27, 14, 8, 5, 38, 22] jogos [27, 14, 8, 5, 39, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: América-PE tabela [17, 7, 4, 6, 24, 28] jogos [19, 9, 4, 6, 29, 30] — a tabela conta 17 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Íbis tabela [15, 4, 1, 10, 19, 49] jogos [16, 4, 1, 11, 19, 51] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: Santo Amaro-PE tabela [16, 2, 3, 11, 15, 36] jogos [17, 2, 3, 12, 17, 39] — a tabela conta 16 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Caruaru
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Atlético Caruaru — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Caruaru)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Santa Cruz

### 1987

- tabela publicada x jogos — 1º Turno - Segunda fase / -: Central tabela [6, 4, 1, 1, 4, 4] jogos [6, 2, 1, 3, 4, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Atlético Caruaru tabela [6, 2, 2, 2, 4, 7] jogos [6, 1, 2, 3, 4, 7] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Santa Cruz

### 1988

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1989

- tabela publicada x jogos — 1º Turno / -: Central tabela [7, 4, 1, 2, 7, 2] jogos [6, 3, 1, 2, 7, 2] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Sete de Setembro-PE tabela [7, 2, 2, 3, 3, 5] jogos [6, 2, 2, 2, 3, 5] — a tabela conta 7 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estudantes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Estudantes — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estudantes)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1990

- tabela publicada x jogos — Segunda fase / Grupo A: Santa Cruz tabela [7, 7, 0, 0, 16, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Náutico tabela [7, 5, 1, 1, 12, 2] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Sport tabela [7, 4, 2, 1, 21, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: 66985 tabela [7, 2, 2, 3, 6, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Estudantes tabela [7, 1, 2, 4, 2, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Santo Amaro-PE tabela [7, 1, 2, 4, 1, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Sete de Setembro-PE tabela [7, 1, 2, 4, 7, 18] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo A: Central tabela [7, 0, 3, 4, 3, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: América-PE tabela [3, 3, 0, 0, 9, 1] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Atlético Caruaru tabela [3, 1, 1, 1, 2, 5] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Íbis tabela [3, 0, 2, 1, 1, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / Grupo B: Ferroviário Recife tabela [3, 0, 1, 2, 1, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estudantes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Estudantes — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estudantes)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)
- vencedor da final pelos jogos (Sport) diferente do campeão oficial (Santa Cruz); fica o oficial

### 1991

- jogo só no ogol, incluído em Final: Náutico 3-3 Sport (1991-12-08)
- jogo só no ogol, incluído em Final: Sport 3-0 Náutico (1991-12-15)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 1992

- sem ocorrências

### 1993

- sem ocorrências

### 1994

- tabela publicada x jogos — 1º Turno - Segunda fase / -: 16927 tabela [10, 2, 4, 4, 10, 18] jogos [10, 2, 4, 4, 11, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Casa Caiada tabela [8, 3, 2, 3, 20, 9] jogos [8, 3, 2, 3, 21, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [6, 4, 2, 0, 11, 7] jogos [6, 3, 2, 1, 10, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Sete de Setembro-PE tabela [6, 2, 1, 3, 8, 8] jogos [6, 3, 1, 2, 9, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [9, 6, 2, 1, 21, 6] jogos [10, 7, 2, 1, 25, 6] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Santa Cruz tabela [9, 5, 3, 1, 20, 8] jogos [10, 5, 3, 2, 20, 12] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno - Segunda fase / -: Sport tabela [10, 5, 4, 1, 13, 5] jogos [10, 4, 5, 1, 13, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Segunda fase / -: 16927 tabela [10, 2, 1, 7, 10, 17] jogos [10, 2, 2, 6, 11, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Sport tabela [40, 26, 9, 5, 72, 19] jogos [40, 25, 10, 5, 72, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: 16927 tabela [37, 11, 10, 16, 45, 60] jogos [37, 11, 11, 15, 45, 60] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Casa Caiada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Centro Limoeirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Destilaria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estudantes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Íbis
- Casa Caiada — clube que o ogol não tem; entra só pela RSSSF
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Centro Limoeirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Centro Limoeirense)
- Destilaria — clube que o ogol não tem; entra só pela RSSSF
- Estudantes — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estudantes)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- Íbis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Íbis)

### 1995

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Destilaria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estudantes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Destilaria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Destilaria)
- Estudantes — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Estudantes)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)

### 1996

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Cabense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabense)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Sport

### 1997

- tabela publicada x jogos — 1º Turno / -: Santa Cruz tabela [6, 3, 2, 1, 8, 7] jogos [21, 7, 9, 5, 28, 28] — a tabela conta 6 jogos e as fontes trazem 21
- tabela publicada x jogos — 1º Turno / -: Náutico tabela [6, 2, 2, 2, 8, 8] jogos [14, 5, 4, 5, 20, 21] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — 1º Turno / -: Flamengo-PE tabela [6, 2, 2, 2, 6, 6] jogos [15, 4, 5, 6, 11, 17] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — 1º Turno / -: Ypiranga-PE tabela [6, 1, 2, 3, 6, 11] jogos [9, 1, 4, 4, 10, 19] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno / -: Centro Limoeirense tabela [6, 1, 1, 4, 6, 12] jogos [9, 1, 1, 7, 9, 21] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno / -: Central tabela [6, 0, 2, 4, 4, 15] jogos [18, 2, 7, 9, 13, 31] — a tabela conta 6 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno - Final / -: Porto-PE tabela [5, 3, 2, 0, 11, 3] jogos [21, 9, 7, 5, 30, 25] — a tabela conta 5 jogos e as fontes trazem 21
- tabela publicada x jogos — 1º Turno - Final / -: 16927 tabela [5, 2, 1, 2, 5, 3] jogos [14, 3, 5, 6, 12, 18] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — 1º Turno - Final / -: Central tabela [5, 1, 4, 0, 2, 1] jogos [18, 2, 7, 9, 13, 31] — a tabela conta 5 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno - Final / -: Ypiranga-PE tabela [5, 1, 2, 2, 8, 12] jogos [9, 1, 4, 4, 10, 19] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno - Final / -: Centro Limoeirense tabela [5, 1, 0, 4, 4, 11] jogos [9, 1, 1, 7, 9, 21] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / -: Porto-PE tabela [5, 1, 4, 0, 4, 3] jogos [21, 9, 7, 5, 30, 25] — a tabela conta 5 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Central tabela [5, 2, 2, 1, 4, 5] jogos [18, 2, 7, 9, 13, 31] — a tabela conta 5 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Santo Amaro-PE tabela [5, 2, 1, 2, 8, 10] jogos [23, 8, 8, 7, 37, 32] — a tabela conta 5 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Náutico tabela [5, 2, 0, 3, 5, 6] jogos [14, 5, 4, 5, 20, 21] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: 16927 tabela [5, 1, 1, 3, 5, 8] jogos [14, 3, 5, 6, 12, 18] — a tabela conta 5 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Cabense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabense)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- campeão pela lista oficial, Sport; o 1º pela soma dos jogos da última fase é Porto-PE (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Porto-PE

### 1998

- tabela publicada x jogos — Primeira fase / -: Sport tabela [11, 10, 1, 0, 35, 3] jogos [10, 10, 0, 0, 35, 3] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Náutico tabela [11, 8, 2, 1, 23, 9] jogos [10, 7, 2, 1, 18, 8] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Porto-PE tabela [11, 4, 5, 2, 20, 13] jogos [10, 4, 4, 2, 19, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Santa Cruz tabela [11, 4, 5, 2, 17, 10] jogos [10, 3, 5, 2, 15, 9] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Central tabela [11, 4, 4, 3, 14, 15] jogos [10, 4, 3, 3, 11, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Ferroviário Recife tabela [11, 4, 4, 3, 13, 18] jogos [10, 4, 3, 3, 12, 17] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: 16927 tabela [11, 4, 3, 4, 11, 14] jogos [10, 3, 3, 4, 10, 14] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Santo Amaro-PE tabela [11, 3, 4, 4, 15, 14] jogos [21, 9, 5, 7, 36, 28] — a tabela conta 11 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / -: Flamengo-PE tabela [11, 2, 4, 5, 8, 14] jogos [20, 7, 4, 9, 26, 31] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Petrolândia tabela [11, 1, 1, 9, 12, 26] jogos [20, 3, 5, 12, 23, 46] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Cabense tabela [11, 0, 1, 10, 7, 36] jogos [20, 1, 3, 16, 12, 55] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Sport tabela [7, 6, 1, 0, 18, 5] jogos [6, 5, 1, 0, 14, 4] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Porto-PE tabela [7, 4, 1, 2, 15, 9] jogos [6, 3, 1, 2, 11, 9] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [7, 3, 2, 2, 10, 7] jogos [6, 2, 2, 2, 9, 7] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [7, 3, 1, 3, 15, 10] jogos [6, 2, 1, 3, 9, 10] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Ferroviário Recife tabela [7, 3, 1, 3, 11, 13] jogos [6, 2, 1, 3, 8, 13] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: 16927 tabela [7, 1, 3, 3, 5, 10] jogos [6, 0, 3, 3, 3, 9] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Central tabela [7, 2, 1, 4, 5, 8] jogos [6, 2, 1, 3, 5, 7] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Repescagem / -: Petrolândia tabela [6, 0, 3, 3, 6, 13] jogos [6, 0, 3, 3, 6, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Sport tabela [23, 20, 3, 0, 62, 9] jogos [5, 4, 1, 0, 9, 1] — a tabela conta 23 jogos e as fontes trazem 5
- tabela publicada x jogos — Terceira fase / -: Porto-PE tabela [23, 11, 7, 5, 43, 28] jogos [5, 3, 1, 1, 8, 6] — a tabela conta 23 jogos e as fontes trazem 5
- tabela publicada x jogos — Terceira fase / -: Náutico tabela [23, 13, 4, 6, 46, 26] jogos [5, 2, 1, 2, 8, 7] — a tabela conta 23 jogos e as fontes trazem 5
- tabela publicada x jogos — Terceira fase / -: Santa Cruz tabela [23, 8, 8, 7, 32, 26] jogos [5, 1, 1, 3, 5, 9] — a tabela conta 23 jogos e as fontes trazem 5
- tabela publicada x jogos — Terceira fase / -: Ferroviário Recife tabela [23, 8, 5, 10, 29, 41] jogos [5, 1, 0, 4, 5, 10] — a tabela conta 23 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase final / -: 16927 tabela [5, 5, 0, 0, 19, 2] jogos [4, 4, 0, 0, 17, 1] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Flamengo-PE tabela [5, 3, 0, 2, 12, 11] jogos [4, 2, 0, 2, 9, 10] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Central tabela [5, 2, 1, 2, 12, 8] jogos [4, 1, 1, 2, 7, 7] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Petrolândia tabela [5, 2, 1, 2, 6, 12] jogos [4, 2, 1, 1, 6, 10] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Cabense tabela [5, 1, 0, 4, 5, 14] jogos [20, 1, 3, 16, 12, 55] — a tabela conta 5 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cabense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Central
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Náutico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Petrolândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport
- Cabense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cabense)
- Central — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Central)
- Náutico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Náutico)
- Petrolândia — clube que o ogol não tem; entra só pela RSSSF
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz)
- Sport — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sport)
- vencedor da final pelos jogos (16927) diferente do campeão oficial (Sport); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Porto-PE

### 1999

- tabela publicada x jogos — Primeira fase / -: Ferroviário Serra Talhada tabela [6, 3, 1, 2, 6, 7] jogos [12, 4, 5, 3, 12, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Surubim tabela [6, 2, 1, 3, 3, 3] jogos [12, 3, 4, 5, 8, 9] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Flamengo-PE tabela [6, 1, 2, 3, 4, 7] jogos [12, 2, 5, 5, 10, 17] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Ferroviário Serra Talhada tabela [6, 1, 4, 1, 7, 7] jogos [12, 4, 5, 3, 12, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Flamengo-PE tabela [6, 1, 3, 2, 6, 10] jogos [12, 2, 5, 5, 10, 17] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Surubim tabela [6, 1, 3, 2, 5, 6] jogos [12, 3, 4, 5, 8, 9] — a tabela conta 6 jogos e as fontes trazem 12

### 2000

- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [9, 7, 1, 1, 23, 11] jogos [10, 8, 1, 1, 26, 11] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Ferroviário Serra Talhada tabela [9, 0, 3, 6, 5, 18] jogos [10, 0, 3, 7, 5, 21] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [18, 10, 7, 1, 35, 19] jogos [19, 11, 7, 1, 38, 19] — a tabela conta 18 jogos e as fontes trazem 19
- mando invertido no ogol — RSSSF Santo Amaro-PE 2-2 Sport, ogol Sport 2-2 Santo Amaro-PE (2000-04-22); fica a RSSSF
- placar diferente no ogol — Ferroviário Serra Talhada x Santa Cruz (2000-04-30): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- placar corrigido pelo ogol — Íbis x Central (2000-04-29): RSSSF 1-2, ogol 1-3; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 10 jogos (ex.: Sport x Unibol Pernambuco, ogol 2000-03-03); fica a do ogol
- jogo só no ogol, incluído em Second Stage: Ferroviário Serra Talhada 0-3 Vitória das Tabocas (2000-04-23)
- só na RSSSF (não achado no ogol): Ferroviário Serra Talhada 0-2 Santa Cruz (2000-04-29)

### 2001

- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [10, 8, 1, 1, 18, 4] jogos [11, 9, 1, 1, 19, 4] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [10, 4, 4, 2, 14, 10] jogos [11, 4, 4, 3, 14, 11] — a tabela conta 10 jogos e as fontes trazem 11
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: Náutico x AGA, ogol 2001-03-05); fica a do ogol
- jogo só no ogol, incluído em Second Stage: Náutico 0-1 Santa Cruz (2001-07-05)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 0-0 Ferroviário Serra Talhada (2001-05-27)
- só na RSSSF (não achado no ogol): Centro Limoeirense 1-4 Santo Amaro-PE (2001-05-27)
- só na RSSSF (não achado no ogol): Ferroviário Serra Talhada 1-0 Centro Limoeirense (2001-06-03)
- só na RSSSF (não achado no ogol): Santo Amaro-PE 1-0 Vitória das Tabocas (2001-06-03)
- só na RSSSF (não achado no ogol): Ferroviário Serra Talhada 2-2 Santo Amaro-PE (2001-06-09)
- só na RSSSF (não achado no ogol): Centro Limoeirense 3-1 Vitória das Tabocas (2001-06-09)
- só na RSSSF (não achado no ogol): Santo Amaro-PE 3-3 Ferroviário Serra Talhada (2001-06-14)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 1-0 Centro Limoeirense (2001-06-14)
- só na RSSSF (não achado no ogol): Centro Limoeirense 1-3 Ferroviário Serra Talhada (2001-06-17)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 1-1 Santo Amaro-PE (2001-06-17)
- só na RSSSF (não achado no ogol): Ferroviário Serra Talhada 4-1 Vitória das Tabocas (2001-06-20)
- só na RSSSF (não achado no ogol): Santo Amaro-PE 6-0 Centro Limoeirense (2001-06-20)

### 2002

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Santa Cruz x Santo Amaro-PE, ogol 2002-06-09); fica a do ogol

### 2003

- tabela publicada x jogos — Segunda fase / -: Sport tabela [18, 14, 3, 1, 52, 19] jogos [28, 19, 6, 3, 76, 34] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [18, 11, 2, 5, 40, 19] jogos [29, 14, 7, 8, 51, 28] — a tabela conta 18 jogos e as fontes trazem 29
- tabela publicada x jogos — Segunda fase / -: AGA tabela [18, 8, 6, 4, 29, 20] jogos [27, 8, 13, 6, 36, 32] — a tabela conta 18 jogos e as fontes trazem 27
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [18, 8, 4, 6, 38, 29] jogos [26, 12, 6, 8, 51, 38] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Petrolina tabela [18, 6, 3, 9, 24, 31] jogos [20, 6, 3, 11, 25, 38] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Central tabela [18, 6, 3, 9, 23, 35] jogos [21, 6, 6, 9, 25, 37] — a tabela conta 18 jogos e as fontes trazem 21
- tabela publicada x jogos — Segunda fase / -: Santo Amaro-PE tabela [18, 5, 6, 7, 29, 35] jogos [22, 5, 8, 9, 31, 41] — a tabela conta 18 jogos e as fontes trazem 22
- tabela publicada x jogos — Segunda fase / -: Itacuruba tabela [18, 5, 4, 9, 30, 34] jogos [21, 7, 4, 10, 38, 42] — a tabela conta 18 jogos e as fontes trazem 21
- tabela publicada x jogos — Terceira fase / -: Sport tabela [6, 4, 2, 0, 14, 5] jogos [28, 19, 6, 3, 76, 34] — a tabela conta 6 jogos e as fontes trazem 28
- tabela publicada x jogos — Terceira fase / -: Náutico tabela [6, 2, 2, 2, 6, 8] jogos [26, 12, 6, 8, 51, 38] — a tabela conta 6 jogos e as fontes trazem 26
- tabela publicada x jogos — Terceira fase / -: Santa Cruz tabela [6, 1, 2, 3, 3, 5] jogos [29, 14, 7, 8, 51, 28] — a tabela conta 6 jogos e as fontes trazem 29
- tabela publicada x jogos — Terceira fase / -: AGA tabela [6, 0, 4, 2, 5, 10] jogos [27, 8, 13, 6, 36, 32] — a tabela conta 6 jogos e as fontes trazem 27
- mando invertido no ogol — RSSSF AGA 1-1 Náutico, ogol Náutico 1-1 AGA (2003-07-02); fica a RSSSF
- mando invertido no ogol — RSSSF Náutico 2-2 AGA, ogol AGA 2-2 Náutico (2003-07-09); fica a RSSSF
- placar diferente no ogol — Itacuruba x Santo Amaro-PE (2003-01-29): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Petrolina x Intercontinental (2003-02-02): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Náutico x Intercontinental (2003-04-13): RSSSF 5-2, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Sport x Itacuruba (2003-04-16): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Sport x AGA (2003-06-24): RSSSF 5-1, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Náutico x Santa Cruz (2003-07-16): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Santa Cruz x Náutico (2003-06-25): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Itacuruba x Náutico, ogol 2003-03-30); fica a do ogol
- jogo só no ogol, incluído em First Stage: 1° de Maio 1-1 Central (2003-01-26)
- jogo só no ogol, incluído em First Stage: Náutico 6-1 1° de Maio (2003-01-29)
- jogo só no ogol, incluído em First Stage: Sport 8-0 1° de Maio (2003-02-01)
- jogo só no ogol, incluído em First Stage: 1° de Maio 1-1 Intercontinental (2003-02-06)
- jogo só no ogol, incluído em First Stage: Itacuruba 1-0 1° de Maio (2003-02-16)
- jogo só no ogol, incluído em First Stage: 1° de Maio 1-2 AGA (2003-02-20)
- jogo só no ogol, incluído em First Stage: 1° de Maio 2-1 Santa Cruz (2003-02-22)
- jogo só no ogol, incluído em First Stage: Santo Amaro-PE 2-0 1° de Maio (2003-02-26)
- jogo só no ogol, incluído em First Stage: 1° de Maio 1-1 Petrolina (2003-03-09)
- jogo só no ogol, incluído em Second Stage: Central 3-1 1° de Maio (2003-03-12)
- jogo só no ogol, incluído em Second Stage: 1° de Maio 0-1 Náutico (2003-03-16)
- jogo só no ogol, incluído em Second Stage: 1° de Maio 1-1 Sport (2003-03-29)
- jogo só no ogol, incluído em Second Stage: Intercontinental 3-0 1° de Maio (2003-04-03)
- jogo só no ogol, incluído em Second Stage: 1° de Maio 2-2 Itacuruba (2003-04-10)
- jogo só no ogol, incluído em Second Stage: AGA 4-0 1° de Maio (2003-04-13)
- jogo só no ogol, incluído em Second Stage: Santa Cruz 0-0 1° de Maio (2003-04-18)
- jogo só no ogol, incluído em Second Stage: 1° de Maio 1-3 Santo Amaro-PE (2003-04-24)
- jogo só no ogol, incluído em Second Stage: Petrolina 1-1 1° de Maio (2003-05-04)
- jogo só no ogol, incluído em Third Stage Qualifiers: Santo Amaro-PE 1-1 Santa Cruz (2033-06-05)
- jogo só no ogol, incluído em Third Stage Qualifiers: Itacuruba 4-2 Sport (2033-06-05)
- jogo só no ogol, incluído em Third Stage Qualifiers: Central 1-1 AGA (2033-06-05)
- jogo só no ogol, incluído em Third Stage Qualifiers: Santa Cruz 2-0 Santo Amaro-PE (2033-06-11)
- só na RSSSF (não achado no ogol): Itacuruba 4-2 Sport (2003-06-04)
- só na RSSSF (não achado no ogol): Santo Amaro-PE 1-1 Santa Cruz (2003-06-04)
- só na RSSSF (não achado no ogol): Central 1-1 AGA (2003-06-04)
- só na RSSSF (não achado no ogol): Santa Cruz 2-0 Santo Amaro-PE (2003-06-10)
- vice pela Wikipédia (sem final de dois clubes): Santa Cruz

### 2004

- tabela publicada x jogos — Segunda fase / -: Náutico tabela [18, 12, 3, 3, 36, 18] jogos [18, 12, 3, 3, 37, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Central tabela [18, 3, 3, 12, 19, 32] jogos [18, 4, 3, 11, 20, 31] — placar diverge entre RSSSF e ogol em Serrano-PE x Central (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Sport x Itacuruba (2004-03-03): RSSSF 3-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Serrano-PE x Central (2004-03-28): RSSSF 0-0, ogol 0-2; fica o da RSSSF

### 2005

- mando invertido no ogol — RSSSF Serrano-PE 0-0 Santo Amaro-PE, ogol Santo Amaro-PE 0-0 Serrano-PE (2005-02-03); fica a RSSSF
- mando invertido no ogol — RSSSF Sport 4-1 Santo Amaro-PE, ogol Santo Amaro-PE 1-4 Sport (2005-02-20); fica a RSSSF
- mando invertido no ogol — RSSSF Santo Amaro-PE 2-4 Santa Cruz, ogol Santa Cruz 4-2 Santo Amaro-PE (2005-03-13); fica a RSSSF
- mando invertido no ogol — RSSSF Santo Amaro-PE 0-0 Serrano-PE, ogol Serrano-PE 0-0 Santo Amaro-PE (2005-03-23); fica a RSSSF
- mando invertido no ogol — RSSSF Santo Amaro-PE 0-0 Itacuruba, ogol Itacuruba 0-0 Santo Amaro-PE (2005-03-31); fica a RSSSF
- mando invertido no ogol — RSSSF Santo Amaro-PE 0-0 Sport, ogol Sport 0-0 Santo Amaro-PE (2005-04-03); fica a RSSSF
- placar diferente no ogol — Petrolina x Itacuruba (2005-03-13): RSSSF 2-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Porto-PE x Serrano-PE (2005-03-20): RSSSF 0-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Santo Amaro-PE x Petrolina (2005-03-28): RSSSF 5-3, ogol 3-3; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 2006

- placar diferente no ogol — Serrano-PE x Estudantes (2006-02-01): RSSSF 3-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Estudantes x Central (2006-03-26): RSSSF 3-0, ogol 4-0; fica o da RSSSF

### 2007

- tabela publicada x jogos — Primeira fase / -: Sport tabela [9, 8, 1, 0, 18, 3] jogos [19, 17, 1, 1, 44, 8] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Porto-PE tabela [9, 5, 1, 3, 15, 13] jogos [19, 9, 3, 7, 34, 33] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Náutico tabela [9, 5, 0, 4, 14, 12] jogos [20, 12, 1, 7, 43, 23] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Central tabela [9, 5, 0, 4, 10, 9] jogos [20, 11, 3, 6, 26, 24] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Ypiranga-PE tabela [9, 4, 2, 3, 10, 12] jogos [19, 7, 4, 8, 24, 36] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Vera Cruz-PE tabela [9, 4, 1, 4, 11, 11] jogos [19, 7, 4, 8, 25, 25] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Santa Cruz tabela [9, 3, 2, 4, 14, 15] jogos [20, 6, 6, 8, 33, 37] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Serrano-PE tabela [9, 3, 2, 4, 10, 12] jogos [19, 5, 5, 9, 22, 31] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Cabense tabela [9, 2, 2, 5, 7, 11] jogos [19, 4, 3, 12, 17, 31] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Belo Jardim tabela [9, 0, 1, 8, 7, 18] jogos [20, 3, 2, 15, 17, 37] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Central tabela [9, 5, 2, 2, 12, 12] jogos [10, 5, 3, 2, 13, 13] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [9, 5, 1, 3, 25, 10] jogos [10, 6, 1, 3, 26, 10] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [9, 3, 3, 3, 16, 18] jogos [10, 3, 4, 3, 17, 19] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Belo Jardim tabela [9, 3, 1, 5, 9, 15] jogos [10, 3, 1, 6, 9, 16] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Sport tabela [18, 16, 1, 1, 39, 7] jogos [19, 17, 1, 1, 44, 8] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Central tabela [18, 10, 2, 6, 22, 21] jogos [20, 11, 3, 6, 26, 24] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [18, 10, 1, 7, 39, 22] jogos [20, 12, 1, 7, 43, 23] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Porto-PE tabela [18, 9, 2, 7, 34, 33] jogos [19, 9, 3, 7, 34, 33] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Vera Cruz-PE tabela [18, 7, 4, 7, 24, 20] jogos [19, 7, 4, 8, 25, 25] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [18, 6, 5, 7, 30, 33] jogos [20, 6, 6, 8, 33, 37] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [18, 6, 4, 8, 23, 36] jogos [19, 7, 4, 8, 24, 36] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Serrano-PE tabela [18, 5, 5, 8, 22, 30] jogos [19, 5, 5, 9, 22, 31] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Cabense tabela [18, 4, 2, 12, 17, 31] jogos [19, 4, 3, 12, 17, 31] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Belo Jardim tabela [18, 3, 2, 13, 16, 33] jogos [20, 3, 2, 15, 17, 37] — a tabela conta 18 jogos e as fontes trazem 20
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Santa Cruz x Central, ogol 2007-03-29); fica a do ogol
- jogo só no ogol, incluído em SECOND STAGE - Taça Confederação Do Equador:: Vera Cruz-PE 0-0 Ypiranga-PE (2007-03-25)
- jogo só no ogol, incluído em SECOND STAGE - Taça Confederação Do Equador:: Náutico 2-1 Santa Cruz (2007-03-25)
- jogo só no ogol, incluído em SECOND STAGE - Taça Confederação Do Equador:: Serrano-PE 2-1 Cabense (2007-04-01)
- jogo só no ogol, incluído em SECOND STAGE - Taça Confederação Do Equador:: Central 1-0 Porto-PE (2007-04-01)
- jogo só no ogol, incluído em SECOND STAGE - Taça Confederação Do Equador:: Santa Cruz 2-1 Vera Cruz-PE (2007-04-01)
- só na RSSSF (não achado no ogol): Ypiranga-PE 1-0 Serrano-PE (2007-01-31)
- só na RSSSF (não achado no ogol): Cabense 0-0 Porto-PE (2007-01-31)
- só na RSSSF (não achado no ogol): Central 3-2 Santa Cruz (2007-01-31)
- só na RSSSF (não achado no ogol): Náutico 3-1 Belo Jardim (2007-01-31)
- só na RSSSF (não achado no ogol): Sport 5-1 Vera Cruz-PE (2007-02-01)
- só na RSSSF (não achado no ogol): Santa Cruz 1-1 Central (2007-03-28)
- só na RSSSF (não achado no ogol): Belo Jardim 0-1 Náutico (2007-03-28)
- vice pela Wikipédia (sem final de dois clubes): Central

### 2008

- tabela publicada x jogos — Segunda fase / -: Sport tabela [10, 6, 3, 1, 16, 4] jogos [16, 11, 3, 2, 37, 10] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Central tabela [10, 5, 2, 3, 19, 13] jogos [16, 7, 6, 3, 28, 19] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [10, 4, 3, 3, 19, 9] jogos [16, 10, 3, 3, 37, 11] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Salgueiro tabela [10, 4, 1, 5, 9, 15] jogos [16, 7, 1, 8, 18, 27] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [10, 3, 2, 5, 18, 26] jogos [16, 6, 5, 5, 27, 32] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Serrano-PE tabela [10, 2, 1, 7, 6, 20] jogos [16, 4, 2, 10, 13, 35] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Sport tabela [10, 6, 3, 1, 16, 4] jogos [16, 11, 3, 2, 37, 10] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Central tabela [10, 5, 2, 3, 19, 13] jogos [16, 7, 6, 3, 28, 19] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [10, 4, 3, 3, 19, 9] jogos [16, 10, 3, 3, 37, 11] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Salgueiro tabela [10, 4, 1, 5, 9, 13] jogos [16, 7, 1, 8, 18, 27] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [10, 3, 2, 5, 18, 26] jogos [16, 6, 5, 5, 27, 32] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Serrano-PE tabela [10, 2, 1, 7, 6, 20] jogos [16, 4, 2, 10, 13, 35] — a tabela conta 10 jogos e as fontes trazem 16
- tabela publicada x jogos — Torneio de rebaixamento / -: Sete de Setembro-PE tabela [22, 4, 8, 10, 21, 32] jogos [22, 4, 8, 10, 21, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Torneio de rebaixamento / -: Sete de Setembro-PE tabela [22, 4, 8, 10, 21, 32] jogos [22, 4, 8, 10, 21, 31] — há jogo do clube sem conferência no ogol
- só na RSSSF (não achado no ogol): Sete de Setembro-PE 1-1 Santa Cruz (2008-03-09)
- só na RSSSF (não achado no ogol): Vera Cruz-PE 2-0 Petrolina (2008-03-09)
- só na RSSSF (não achado no ogol): Porto-PE 4-0 Centro Limoeirense (2008-03-09)
- só na RSSSF (não achado no ogol): Santa Cruz 0-2 Porto-PE (2008-03-12)
- só na RSSSF (não achado no ogol): Sete de Setembro-PE 0-0 Vera Cruz-PE (2008-03-12)
- só na RSSSF (não achado no ogol): Petrolina 2-1 Centro Limoeirense (2008-03-12)
- só na RSSSF (não achado no ogol): Porto-PE 2-0 Petrolina (2008-03-15)
- só na RSSSF (não achado no ogol): Centro Limoeirense 2-4 Sete de Setembro-PE (2008-03-16)
- só na RSSSF (não achado no ogol): Vera Cruz-PE 1-1 Santa Cruz (2008-03-16)
- só na RSSSF (não achado no ogol): Porto-PE 2-0 Vera Cruz-PE (2008-03-23)
- só na RSSSF (não achado no ogol): Petrolina 2-2 Sete de Setembro-PE (2008-03-23)
- só na RSSSF (não achado no ogol): Centro Limoeirense 2-3 Santa Cruz (2008-03-23)
- só na RSSSF (não achado no ogol): Santa Cruz 2-2 Petrolina (2008-03-26)
- só na RSSSF (não achado no ogol): Vera Cruz-PE 3-0 Centro Limoeirense (2008-03-26)
- só na RSSSF (não achado no ogol): Sete de Setembro-PE 0-0 Porto-PE (2008-03-26)
- só na RSSSF (não achado no ogol): Petrolina 1-1 Vera Cruz-PE (2008-03-30)
- só na RSSSF (não achado no ogol): Santa Cruz 1-0 Sete de Setembro-PE (2008-03-30)
- só na RSSSF (não achado no ogol): Centro Limoeirense 1-1 Porto-PE (2008-03-30)
- só na RSSSF (não achado no ogol): Porto-PE 1-2 Santa Cruz (2008-04-06)
- só na RSSSF (não achado no ogol): Vera Cruz-PE 0-1 Sete de Setembro-PE (2008-04-06)
- só na RSSSF (não achado no ogol): Centro Limoeirense 0-2 Petrolina (2008-04-06)
- só na RSSSF (não achado no ogol): Petrolina 5-1 Porto-PE (2008-04-13)
- só na RSSSF (não achado no ogol): Sete de Setembro-PE 1-1 Centro Limoeirense (2008-04-13)
- só na RSSSF (não achado no ogol): Santa Cruz 4-2 Vera Cruz-PE (2008-04-13)
- só na RSSSF (não achado no ogol): Petrolina 2-1 Santa Cruz (2008-04-16)
- só na RSSSF (não achado no ogol): Centro Limoeirense 1-0 Vera Cruz-PE (2008-04-16)
- só na RSSSF (não achado no ogol): Porto-PE 2-0 Sete de Setembro-PE (2008-04-16)
- só na RSSSF (não achado no ogol): Vera Cruz-PE 2-2 Porto-PE (2008-04-19)
- só na RSSSF (não achado no ogol): Sete de Setembro-PE 1-0 Petrolina (2008-04-19)
- só na RSSSF (não achado no ogol): Santa Cruz 3-0 Centro Limoeirense (2008-04-19)
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 2009

- placar diferente no ogol — Salgueiro x Porto-PE (2009-01-28): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Vitória das Tabocas x Petrolina (2009-01-28): RSSSF 0-2, ogol 0-3; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 2010

- vencedor da final pelos jogos (Salgueiro) diferente do campeão oficial (Sport); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Náutico

### 2011

- placar corrigido pelo ogol — Araripina x Vitória das Tabocas (2011-04-03): RSSSF 2-3, ogol 2-0; fica o do ogol, que fecha com a tabela publicada
- vencedor da final pelos jogos (Araripina) diferente do campeão oficial (Santa Cruz); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Sport

### 2012

- tabela publicada x jogos — Fase final / -: Santa Cruz tabela [26, 16, 3, 7, 51, 27] jogos [26, 16, 3, 7, 50, 26] — placar diverge entre RSSSF e ogol em Sport x Santa Cruz (1-2 x 2-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Sport tabela [26, 16, 7, 3, 48, 26] jogos [26, 16, 7, 3, 47, 25] — placar diverge entre RSSSF e ogol em Sport x Santa Cruz (1-2 x 2-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Sport x Santa Cruz (2012-05-13): RSSSF 1-2, ogol 2-3; fica o da RSSSF

### 2013

- tabela publicada x jogos — Segunda fase / -: Náutico tabela [11, 7, 0, 4, 32, 12] jogos [19, 13, 1, 5, 49, 20] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [11, 5, 4, 2, 20, 16] jogos [19, 7, 6, 6, 25, 24] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Pesqueira tabela [11, 4, 3, 4, 19, 18] jogos [19, 7, 6, 6, 28, 25] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Porto-PE tabela [11, 3, 4, 4, 17, 20] jogos [19, 4, 7, 8, 18, 29] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Belo Jardim tabela [11, 3, 4, 4, 15, 20] jogos [19, 7, 6, 6, 23, 26] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Petrolina tabela [11, 3, 3, 5, 11, 19] jogos [19, 3, 4, 12, 14, 29] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Chã Grande tabela [11, 3, 3, 5, 12, 23] jogos [19, 5, 5, 9, 18, 31] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Serra Talhada tabela [11, 3, 2, 6, 15, 19] jogos [19, 7, 3, 9, 25, 30] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Central tabela [11, 3, 2, 6, 11, 16] jogos [19, 9, 3, 7, 25, 22] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Sport tabela [2, 2, 0, 0, 9, 3] jogos [15, 8, 4, 3, 33, 17] — a tabela conta 2 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [2, 1, 0, 1, 2, 2] jogos [15, 9, 3, 3, 20, 10] — a tabela conta 2 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [2, 0, 0, 2, 3, 9] jogos [23, 7, 7, 9, 29, 37] — a tabela conta 2 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / -: Santa Cruz tabela [2, 2, 0, 0, 3, 0] jogos [15, 9, 3, 3, 20, 10] — a tabela conta 2 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Sport tabela [2, 0, 0, 2, 0, 3] jogos [15, 8, 4, 3, 33, 17] — a tabela conta 2 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Náutico tabela [2, 1, 1, 0, 4, 1] jogos [23, 15, 2, 6, 55, 23] — a tabela conta 2 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / -: Ypiranga-PE tabela [2, 0, 1, 1, 1, 4] jogos [23, 7, 7, 9, 29, 37] — a tabela conta 2 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / -: Central tabela [7, 5, 0, 2, 14, 12] jogos [26, 14, 3, 9, 39, 34] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Salgueiro tabela [7, 4, 2, 1, 10, 5] jogos [18, 7, 4, 7, 18, 22] — a tabela conta 7 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Pesqueira tabela [7, 4, 1, 2, 20, 7] jogos [26, 11, 7, 8, 48, 32] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Serra Talhada tabela [7, 3, 1, 3, 9, 8] jogos [26, 10, 4, 12, 34, 38] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Porto-PE tabela [7, 3, 1, 3, 8, 11] jogos [26, 7, 8, 11, 26, 40] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Chã Grande tabela [7, 3, 0, 4, 10, 10] jogos [26, 8, 5, 13, 28, 41] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Petrolina tabela [7, 2, 2, 3, 7, 14] jogos [26, 5, 6, 15, 21, 43] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Belo Jardim tabela [7, 0, 1, 6, 6, 17] jogos [26, 7, 7, 12, 29, 43] — a tabela conta 7 jogos e as fontes trazem 26
- vice pela Wikipédia (sem final de dois clubes): Sport

### 2014

- tabela publicada x jogos — Segunda fase / -: Salgueiro tabela [10, 4, 2, 4, 9, 18] jogos [26, 15, 5, 6, 32, 25] — a tabela conta 10 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Central tabela [10, 3, 4, 3, 14, 12] jogos [26, 13, 8, 5, 43, 26] — a tabela conta 10 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Porto-PE tabela [10, 1, 0, 9, 4, 24] jogos [26, 8, 3, 15, 20, 36] — a tabela conta 10 jogos e as fontes trazem 26
- placar diferente no ogol — Ypiranga-PE x América-PE (2013-12-18): RSSSF 0-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Vitória das Tabocas x Chã Grande (2014-01-09): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Serra Talhada x Chã Grande (2013-12-29): RSSSF 0-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Ypiranga-PE x Pesqueira (2013-12-26): RSSSF 0-0, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 10 jogos (ex.: Chã Grande x Central, ogol 2014-01-12); fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-0 Serra Talhada: RSSSF 2013-01-02, ogol 2014-01-02; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 3-1 Pesqueira: RSSSF 2013-01-02, ogol 2014-01-02; fica a do ogol
- ano errado na data da RSSSF — Vitória das Tabocas 1-2 Central: RSSSF 2013-01-02, ogol 2014-01-02; fica a do ogol
- ano errado na data da RSSSF — Chã Grande 2-0 América-PE: RSSSF 2013-01-03, ogol 2014-01-03; fica a do ogol
- ano errado na data da RSSSF — Central 2-0 Ypiranga-PE: RSSSF 2013-01-05, ogol 2014-01-05; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 1-0 Porto-PE: RSSSF 2013-01-05, ogol 2014-01-05; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 1-1 Chã Grande: RSSSF 2013-01-06, ogol 2014-01-06; fica a do ogol
- ano errado na data da RSSSF — América-PE 0-0 Salgueiro: RSSSF 2013-01-06, ogol 2014-01-06; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 1-2 América-PE: RSSSF 2013-01-09, ogol 2014-01-09; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-1 Salgueiro: RSSSF 2013-01-09, ogol 2014-01-09; fica a do ogol
- ano errado na data da RSSSF — Central 1-0 Porto-PE: RSSSF 2013-01-09, ogol 2014-01-09; fica a do ogol
- ano errado na data da RSSSF — América-PE 3-3 Pesqueira: RSSSF 2013-01-15, ogol 2014-01-15; fica a do ogol
- ano errado na data da RSSSF — Central 1-0 Salgueiro: RSSSF 2013-01-15, ogol 2014-01-15; fica a do ogol
- ano errado na data da RSSSF — Vitória das Tabocas 1-0 Porto-PE: RSSSF 2013-01-15, ogol 2014-01-15; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-1 Chã Grande: RSSSF 2013-01-15, ogol 2014-01-15; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-0 Chã Grande: RSSSF 2013-01-19, ogol 2014-01-19; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 1-1 Central: RSSSF 2013-01-19, ogol 2014-01-19; fica a do ogol
- ano errado na data da RSSSF — América-PE 0-1 Ypiranga-PE: RSSSF 2013-01-19, ogol 2014-01-19; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 2-1 Vitória das Tabocas: RSSSF 2013-01-19, ogol 2014-01-19; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 0-2 Porto-PE: RSSSF 2013-01-22, ogol 2014-01-22; fica a do ogol
- ano errado na data da RSSSF — Central 0-0 Pesqueira: RSSSF 2013-01-22, ogol 2014-01-22; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-1 Serra Talhada: RSSSF 2013-01-22, ogol 2014-01-22; fica a do ogol
- ano errado na data da RSSSF — Vitória das Tabocas 2-0 América-PE: RSSSF 2013-01-22, ogol 2014-01-22; fica a do ogol
- ano errado na data da RSSSF — Chã Grande 1-2 Salgueiro: RSSSF 2013-01-26, ogol 2014-01-26; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 2-0 Vitória das Tabocas: RSSSF 2013-01-26, ogol 2014-01-26; fica a do ogol
- ano errado na data da RSSSF — América-PE 0-1 Central: RSSSF 2013-01-26, ogol 2014-01-26; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 0-1 Ypiranga-PE: RSSSF 2013-01-26, ogol 2014-01-26; fica a do ogol
- ano errado na data da RSSSF — Vitória das Tabocas 2-1 Ypiranga-PE: RSSSF 2013-01-29, ogol 2014-01-29; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 1-0 Pesqueira: RSSSF 2013-01-29, ogol 2014-01-29; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 0-1 América-PE: RSSSF 2013-01-29, ogol 2014-01-29; fica a do ogol
- ano errado na data da RSSSF — Chã Grande 1-2 Serra Talhada: RSSSF 2013-01-30, ogol 2014-01-30; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 0-0 Salgueiro: RSSSF 2013-02-02, ogol 2014-02-02; fica a do ogol
- ano errado na data da RSSSF — América-PE 0-1 Chã Grande: RSSSF 2013-02-02, ogol 2014-02-02; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 0-1 Porto-PE: RSSSF 2013-02-02, ogol 2014-02-02; fica a do ogol
- ano errado na data da RSSSF — Chã Grande 0-0 Pesqueira: RSSSF 2013-02-05, ogol 2014-02-05; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 3-0 América-PE: RSSSF 2013-02-05, ogol 2014-02-05; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-1 Serra Talhada: RSSSF 2013-02-05, ogol 2014-02-05; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-5 Central: RSSSF 2013-02-05, ogol 2014-02-05; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 4-2 Central: RSSSF 2013-02-09, ogol 2014-02-09; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-1 Porto-PE: RSSSF 2013-02-09, ogol 2014-02-09; fica a do ogol
- ano errado na data da RSSSF — Central 1-1 Náutico: RSSSF 2013-02-13, ogol 2014-02-13; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 0-0 Central: RSSSF 2013-02-16, ogol 2014-02-16; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 0-0 Náutico: RSSSF 2013-02-19, ogol 2014-02-19; fica a do ogol
- ano errado na data da RSSSF — Sport 1-1 Central: RSSSF 2013-02-22, ogol 2014-02-22; fica a do ogol
- ano errado na data da RSSSF — Náutico 3-0 Porto-PE: RSSSF 2013-02-23, ogol 2014-02-23; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 1-1 Santa Cruz: RSSSF 2013-02-23, ogol 2014-02-23; fica a do ogol
- ano errado na data da RSSSF — Náutico 2-1 Sport: RSSSF 2013-02-27, ogol 2014-02-27; fica a do ogol
- ano errado na data da RSSSF — Central 2-1 Porto-PE: RSSSF 2013-03-05, ogol 2014-03-05; fica a do ogol
- ano errado na data da RSSSF — Sport 3-0 Santa Cruz: RSSSF 2013-03-06, ogol 2014-03-06; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-4 Náutico: RSSSF 2013-03-08, ogol 2014-03-08; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 7-0 Salgueiro: RSSSF 2013-03-09, ogol 2014-03-09; fica a do ogol
- ano errado na data da RSSSF — Central 0-2 Sport: RSSSF 2013-03-09, ogol 2014-03-09; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 4-0 Porto-PE: RSSSF 2013-03-15, ogol 2014-03-15; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-1 Sport: RSSSF 2013-03-16, ogol 2014-03-16; fica a do ogol
- ano errado na data da RSSSF — Náutico 2-1 Central: RSSSF 2013-03-16, ogol 2014-03-16; fica a do ogol
- ano errado na data da RSSSF — Sport 1-0 Porto-PE: RSSSF 2013-03-22, ogol 2014-03-22; fica a do ogol
- ano errado na data da RSSSF — Central 1-0 Salgueiro: RSSSF 2013-03-23, ogol 2014-03-23; fica a do ogol
- ano errado na data da RSSSF — Náutico 3-5 Santa Cruz: RSSSF 2013-03-23, ogol 2014-03-23; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 1-3 Náutico: RSSSF 2013-03-26, ogol 2014-03-26; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 0-5 Central: RSSSF 2013-03-26, ogol 2014-03-26; fica a do ogol
- ano errado na data da RSSSF — Central 1-1 Santa Cruz: RSSSF 2013-03-30, ogol 2014-03-30; fica a do ogol
- ano errado na data da RSSSF — Sport 0-1 Náutico: RSSSF 2013-03-30, ogol 2014-03-30; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 0-1 Salgueiro: RSSSF 2013-03-30, ogol 2014-03-30; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-0 Náutico: RSSSF 2013-04-06, ogol 2014-04-06; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 3-0 Sport: RSSSF 2013-04-06, ogol 2014-04-06; fica a do ogol
- ano errado na data da RSSSF — Náutico 1-0 Salgueiro: RSSSF 2013-04-12, ogol 2014-04-12; fica a do ogol
- ano errado na data da RSSSF — Sport 1-0 Santa Cruz: RSSSF 2013-04-13, ogol 2014-04-13; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 1-1 Santa Cruz: RSSSF 2013-04-16, ogol 2014-04-16; fica a do ogol
- jogo só no ogol, incluído em First Phase: Central 2-1 Vitória das Tabocas (2014-02-02)
- jogo só no ogol, incluído em Second Phase - Hexagonal - Título: Porto-PE 0-2 Sport (2014-02-20)
- jogo só no ogol, incluído em Second Phase - Hexagonal - Título: Náutico 0-2 Salgueiro (2014-03-06)
- jogo só no ogol, incluído em Second Phase - Hexagonal - Título: Santa Cruz 1-1 Sport (2014-03-27)
- jogo só no ogol, incluído em Fourth Phase - Decisão do Third Lugar: Sport 2-0 Náutico (2014-04-17)
- jogo só no ogol, incluído em Disputa do 3º lugar: Santa Cruz 1-2 Salgueiro (2014-04-23)
- jogo só no ogol, incluído em Third Phase - Final: Náutico 0-1 Sport (2014-04-24)
- só na RSSSF (não achado no ogol): Ypiranga-PE 2-1 América-PE (2013-12-18)
- só na RSSSF (não achado no ogol): Ypiranga-PE 0-2 Pesqueira (2013-12-26)
- só na RSSSF (não achado no ogol): Serra Talhada 1-0 Chã Grande (2013-12-29)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 1-1 Chã Grande (2013-01-09)
- só na RSSSF (não achado no ogol): Central 2-1 Vitória das Tabocas (2013-02-01)
- só na RSSSF (não achado no ogol): Serra Talhada 1-0 Pesqueira (2013-02-13)
- só na RSSSF (não achado no ogol): América-PE 1-0 Vitória das Tabocas (2013-02-16)
- só na RSSSF (não achado no ogol): Chã Grande 4-0 Serra Talhada (2013-02-16)
- só na RSSSF (não achado no ogol): Pesqueira 2-1 Ypiranga-PE (2013-02-16)
- só na RSSSF (não achado no ogol): Ypiranga-PE 0-0 Chã Grande (2013-02-19)
- só na RSSSF (não achado no ogol): Serra Talhada 2-1 Vitória das Tabocas (2013-02-19)
- só na RSSSF (não achado no ogol): América-PE 1-2 Pesqueira (2013-02-19)
- só na RSSSF (não achado no ogol): Chã Grande 1-1 Pesqueira (2013-02-22)
- só na RSSSF (não achado no ogol): Serra Talhada 0-0 América-PE (2013-02-23)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 0-2 Ypiranga-PE (2013-02-23)
- só na RSSSF (não achado no ogol): América-PE 1-0 Chã Grande (2013-02-26)
- só na RSSSF (não achado no ogol): Pesqueira 1-0 Vitória das Tabocas (2013-02-26)
- só na RSSSF (não achado no ogol): Ypiranga-PE 1-1 Serra Talhada (2013-02-26)
- só na RSSSF (não achado no ogol): Pesqueira 0-1 Serra Talhada (2013-03-09)
- só na RSSSF (não achado no ogol): América-PE 0-2 Ypiranga-PE (2013-03-09)
- só na RSSSF (não achado no ogol): Chã Grande 0-4 Vitória das Tabocas (2013-03-09)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 0-1 América-PE (2013-03-12)
- só na RSSSF (não achado no ogol): Chã Grande 2-2 Ypiranga-PE (2013-03-15)
- só na RSSSF (não achado no ogol): Pesqueira 2-0 América-PE (2013-03-16)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 1-3 Serra Talhada (2013-03-16)
- só na RSSSF (não achado no ogol): Pesqueira 1-0 Chã Grande (2013-03-19)
- só na RSSSF (não achado no ogol): Ypiranga-PE 2-0 Vitória das Tabocas (2013-03-19)
- só na RSSSF (não achado no ogol): América-PE 3-2 Serra Talhada (2013-03-19)
- só na RSSSF (não achado no ogol): Vitória das Tabocas 1-3 Pesqueira (2013-03-22)
- só na RSSSF (não achado no ogol): Serra Talhada 1-0 Ypiranga-PE (2013-03-23)
- só na RSSSF (não achado no ogol): Chã Grande 1-0 América-PE (2013-03-23)
- só na RSSSF (não achado no ogol): Porto-PE 0-2 Sport (2013-02-19)
- só na RSSSF (não achado no ogol): Náutico 0-2 Salgueiro (2013-03-05)
- só na RSSSF (não achado no ogol): Santa Cruz 1-1 Sport (2013-03-26)
- só na RSSSF (não achado no ogol): Santa Cruz 1-2 Salgueiro (2013-04-22)
- só na RSSSF (não achado no ogol): Sport 2-0 Náutico (2013-04-16)
- só na RSSSF (não achado no ogol): Náutico 0-1 Sport (2013-04-23)

### 2015

- tabela publicada x jogos — Segunda fase / -: Central tabela [10, 4, 2, 4, 10, 10] jogos [24, 11, 6, 7, 30, 22] — a tabela conta 10 jogos e as fontes trazem 24
- tabela publicada x jogos — Segunda fase / -: Serra Talhada tabela [10, 3, 1, 6, 10, 18] jogos [24, 9, 6, 9, 31, 30] — a tabela conta 10 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Santa Cruz tabela [2, 1, 1, 0, 1, 0] jogos [17, 9, 4, 4, 20, 13] — a tabela conta 2 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Salgueiro tabela [2, 0, 1, 1, 0, 1] jogos [15, 4, 5, 6, 13, 15] — a tabela conta 2 jogos e as fontes trazem 15
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: América-PE x Porto-PE, ogol 2015-01-11); fica a do ogol
- ano errado na data da RSSSF — América-PE 1-1 Vera Cruz-PE: RSSSF 2014-01-04, ogol 2015-01-04; fica a do ogol
- ano errado na data da RSSSF — Central 0-1 Pesqueira: RSSSF 2014-01-04, ogol 2015-01-04; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 1-2 Porto-PE: RSSSF 2014-01-04, ogol 2015-01-04; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 2-2 Atlético Pernambucano: RSSSF 2014-01-04, ogol 2015-01-04; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 3-1 Serra Talhada: RSSSF 2014-01-07, ogol 2015-01-07; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 4-1 Ypiranga-PE: RSSSF 2014-01-07, ogol 2015-01-07; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 0-2 Central: RSSSF 2014-01-07, ogol 2015-01-07; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 2-0 América-PE: RSSSF 2014-01-07, ogol 2015-01-07; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-3 Central: RSSSF 2014-01-14, ogol 2015-01-14; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 1-0 Pesqueira: RSSSF 2014-01-14, ogol 2015-01-14; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-0 Serra Talhada: RSSSF 2014-01-14, ogol 2015-01-14; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 1-1 América-PE: RSSSF 2014-01-14, ogol 2015-01-14; fica a do ogol
- ano errado na data da RSSSF — América-PE 1-0 Ypiranga-PE: RSSSF 2014-01-18, ogol 2015-01-18; fica a do ogol
- ano errado na data da RSSSF — Central 3-2 Serra Talhada: RSSSF 2014-01-18, ogol 2015-01-18; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 1-1 Atlético Pernambucano: RSSSF 2014-01-18, ogol 2015-01-18; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 1-2 Porto-PE: RSSSF 2014-01-18, ogol 2015-01-18; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 4-5 Pesqueira: RSSSF 2014-01-21, ogol 2015-01-21; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 2-0 Central: RSSSF 2014-01-21, ogol 2015-01-21; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-1 Vera Cruz-PE: RSSSF 2014-01-21, ogol 2015-01-21; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 2-0 América-PE: RSSSF 2014-01-21, ogol 2015-01-21; fica a do ogol
- ano errado na data da RSSSF — América-PE 0-2 Pesqueira: RSSSF 2014-01-24, ogol 2015-01-24; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-1 Atlético Pernambucano: RSSSF 2014-01-25, ogol 2015-01-25; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 0-6 Serra Talhada: RSSSF 2014-01-25, ogol 2015-01-25; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 1-1 Central: RSSSF 2014-01-25, ogol 2015-01-25; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 1-2 Vera Cruz-PE: RSSSF 2014-01-28, ogol 2015-01-28; fica a do ogol
- ano errado na data da RSSSF — Central 0-0 América-PE: RSSSF 2014-01-28, ogol 2015-01-28; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 0-0 Ypiranga-PE: RSSSF 2014-01-28, ogol 2015-01-28; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 1-0 Porto-PE: RSSSF 2014-01-28, ogol 2015-01-28; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 0-3 Sport: RSSSF 2014-01-31, ogol 2015-01-31; fica a do ogol
- ano errado na data da RSSSF — Náutico 0-0 Salgueiro: RSSSF 2014-02-01, ogol 2015-02-01; fica a do ogol
- ano errado na data da RSSSF — Central 1-0 Serra Talhada: RSSSF 2014-02-01, ogol 2015-02-01; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-0 Pesqueira: RSSSF 2014-02-03, ogol 2015-02-03; fica a do ogol
- ano errado na data da RSSSF — América-PE 2-0 Vera Cruz-PE: RSSSF 2014-02-03, ogol 2015-02-03; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 1-1 Atlético Pernambucano: RSSSF 2014-02-03, ogol 2015-02-03; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 2-0 Porto-PE: RSSSF 2014-02-07, ogol 2015-02-07; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 4-0 Ypiranga-PE: RSSSF 2014-02-07, ogol 2015-02-07; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 1-0 América-PE: RSSSF 2014-02-07, ogol 2015-02-07; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 3-0 Santa Cruz: RSSSF 2014-02-08, ogol 2015-02-08; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 0-1 Central: RSSSF 2014-02-08, ogol 2015-02-08; fica a do ogol
- ano errado na data da RSSSF — Sport 1-0 Náutico: RSSSF 2014-02-08, ogol 2015-02-08; fica a do ogol
- ano errado na data da RSSSF — América-PE 2-2 Ypiranga-PE: RSSSF 2014-02-10, ogol 2015-02-10; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 1-1 Porto-PE: RSSSF 2014-02-10, ogol 2015-02-10; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 2-1 Atlético Pernambucano: RSSSF 2014-02-10, ogol 2015-02-10; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 0-3 Sport: RSSSF 2014-02-13, ogol 2015-02-13; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 2-1 América-PE: RSSSF 2014-02-21, ogol 2015-02-21; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 0-2 Pesqueira: RSSSF 2014-02-21, ogol 2015-02-21; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 2-0 Vera Cruz-PE: RSSSF 2014-02-21, ogol 2015-02-21; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 0-1 Salgueiro: RSSSF 2014-02-21, ogol 2015-02-21; fica a do ogol
- ano errado na data da RSSSF — Sport 4-2 Serra Talhada: RSSSF 2014-02-22, ogol 2015-02-22; fica a do ogol
- ano errado na data da RSSSF — Central 1-1 Náutico: RSSSF 2014-02-22, ogol 2015-02-22; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 1-0 Ypiranga-PE: RSSSF 2014-02-24, ogol 2015-02-24; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 3-1 Pesqueira: RSSSF 2014-02-24, ogol 2015-02-24; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 2-2 América-PE: RSSSF 2014-02-24, ogol 2015-02-24; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 1-0 Salgueiro: RSSSF 2014-02-25, ogol 2015-02-25; fica a do ogol
- ano errado na data da RSSSF — Sport 1-0 Central: RSSSF 2014-02-26, ogol 2015-02-26; fica a do ogol
- ano errado na data da RSSSF — América-PE 1-0 Atlético Pernambucano: RSSSF 2014-02-28, ogol 2015-02-28; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 2-4 Porto-PE: RSSSF 2014-02-28, ogol 2015-02-28; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 1-1 Vera Cruz-PE: RSSSF 2014-02-28, ogol 2015-02-28; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 0-0 Náutico: RSSSF 2014-03-01, ogol 2015-03-01; fica a do ogol
- ano errado na data da RSSSF — Central 1-0 Sport: RSSSF 2014-03-01, ogol 2015-03-01; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-2 Serra Talhada: RSSSF 2014-03-01, ogol 2015-03-01; fica a do ogol
- ano errado na data da RSSSF — América-PE 3-3 Porto-PE: RSSSF 2014-03-03, ogol 2015-03-03; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 2-1 Ypiranga-PE: RSSSF 2014-03-03, ogol 2015-03-03; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 2-2 Atlético Pernambucano: RSSSF 2014-03-03, ogol 2015-03-03; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 2-0 Vera Cruz-PE: RSSSF 2014-03-07, ogol 2015-03-07; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 1-1 América-PE: RSSSF 2014-03-07, ogol 2015-03-07; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 1-1 Pesqueira: RSSSF 2014-03-07, ogol 2015-03-07; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 1-0 Santa Cruz: RSSSF 2014-03-08, ogol 2015-03-08; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 0-1 Sport: RSSSF 2014-03-08, ogol 2015-03-08; fica a do ogol
- ano errado na data da RSSSF — Náutico 2-2 Central: RSSSF 2014-03-08, ogol 2015-03-08; fica a do ogol
- ano errado na data da RSSSF — Porto-PE 4-2 Atlético Pernambucano: RSSSF 2014-03-10, ogol 2015-03-10; fica a do ogol
- ano errado na data da RSSSF — América-PE 1-0 Pesqueira: RSSSF 2014-03-10, ogol 2015-03-10; fica a do ogol
- ano errado na data da RSSSF — Ypiranga-PE 2-0 Vera Cruz-PE: RSSSF 2014-03-10, ogol 2015-03-10; fica a do ogol
- ano errado na data da RSSSF — Vera Cruz-PE 1-0 América-PE: RSSSF 2014-03-14, ogol 2015-03-14; fica a do ogol
- ano errado na data da RSSSF — Atlético Pernambucano 2-1 Ypiranga-PE: RSSSF 2014-03-14, ogol 2015-03-14; fica a do ogol
- ano errado na data da RSSSF — Pesqueira 2-0 Porto-PE: RSSSF 2014-03-14, ogol 2015-03-14; fica a do ogol
- ano errado na data da RSSSF — Sport 3-1 Salgueiro: RSSSF 2014-03-14, ogol 2015-03-14; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 1-0 Central: RSSSF 2014-03-15, ogol 2015-03-15; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 0-2 Náutico: RSSSF 2014-03-15, ogol 2015-03-15; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 3-0 Serra Talhada: RSSSF 2014-03-21, ogol 2015-03-21; fica a do ogol
- ano errado na data da RSSSF — Náutico 0-2 Sport: RSSSF 2014-03-22, ogol 2015-03-22; fica a do ogol
- ano errado na data da RSSSF — Central 2-1 Salgueiro: RSSSF 2014-03-22, ogol 2015-03-22; fica a do ogol
- ano errado na data da RSSSF — Sport 1-1 Santa Cruz: RSSSF 2014-04-05, ogol 2015-04-05; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 4-1 Náutico: RSSSF 2014-04-05, ogol 2015-04-05; fica a do ogol
- ano errado na data da RSSSF — Serra Talhada 2-1 Central: RSSSF 2014-04-05, ogol 2015-04-05; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 4-0 Central: RSSSF 2014-04-18, ogol 2015-04-18; fica a do ogol
- ano errado na data da RSSSF — Salgueiro 2-0 Sport: RSSSF 2014-04-19, ogol 2015-04-19; fica a do ogol
- ano errado na data da RSSSF — Sport 1-1 Salgueiro: RSSSF 2014-04-26, ogol 2015-04-26; fica a do ogol
- ano errado na data da RSSSF — Central 0-2 Santa Cruz: RSSSF 2014-04-26, ogol 2015-04-26; fica a do ogol
- ano errado na data da RSSSF — Sport 0-0 Central: RSSSF 2014-05-02, ogol 2015-05-02; fica a do ogol
- ano errado na data da RSSSF — Santa Cruz 1-0 Salgueiro: RSSSF 2014-05-03, ogol 2015-05-03; fica a do ogol
- jogo só no ogol, incluído em Second Phase - Hexagonal - Título: Central 1-2 Santa Cruz (2015-02-19)
- jogo só no ogol, incluído em Second Phase - Hexagonal - Título: Náutico 1-2 Santa Cruz (2015-02-26)
- jogo só no ogol, incluído em Disputa do 3º lugar: Central 0-5 Sport (2015-04-30)
- jogo só no ogol, incluído em Fourth Phase - Final: Salgueiro 0-0 Santa Cruz (2015-04-30)
- só na RSSSF (não achado no ogol): Central 1-2 Santa Cruz (2014-02-18)
- só na RSSSF (não achado no ogol): Náutico 1-2 Santa Cruz (2014-02-25)
- só na RSSSF (não achado no ogol): Central 0-5 Sport (2014-04-29)
- só na RSSSF (não achado no ogol): Salgueiro 0-0 Santa Cruz (2014-04-29)

### 2016

- tabela publicada x jogos — Primeira fase / Grupo A: Atlético Pernambucano tabela [6, 2, 3, 1, 4, 3] jogos [10, 5, 4, 1, 9, 4] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo A: Porto-PE tabela [6, 2, 2, 2, 5, 6] jogos [10, 2, 4, 4, 6, 10] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo A: Belo Jardim tabela [6, 0, 2, 4, 3, 8] jogos [10, 1, 3, 6, 4, 10] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo B: Serra Talhada tabela [6, 2, 3, 1, 6, 5] jogos [10, 4, 5, 1, 11, 7] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo B: Vitória das Tabocas tabela [6, 1, 2, 3, 6, 7] jogos [10, 1, 6, 3, 9, 10] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo B: Pesqueira tabela [6, 1, 2, 3, 4, 7] jogos [10, 1, 4, 5, 7, 13] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo B: Atlético Pernambucano tabela [10, 6, 2, 2, 15, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Serra Talhada tabela [10, 4, 3, 3, 13, 11] jogos [10, 4, 5, 1, 11, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: Belo Jardim tabela [10, 3, 3, 4, 10, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Vitória das Tabocas tabela [10, 2, 6, 2, 11, 13] jogos [10, 1, 6, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: Porto-PE tabela [10, 2, 5, 3, 6, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Pesqueira tabela [10, 1, 5, 4, 7, 11] jogos [10, 1, 4, 5, 7, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: Atlético Pernambucano tabela [10, 6, 2, 2, 15, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Serra Talhada tabela [10, 4, 3, 3, 13, 11] jogos [10, 4, 5, 1, 11, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: Belo Jardim tabela [10, 3, 3, 4, 10, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Vitória das Tabocas tabela [10, 2, 6, 2, 11, 13] jogos [10, 1, 6, 3, 9, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: Porto-PE tabela [10, 2, 5, 3, 6, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Pesqueira tabela [10, 1, 5, 4, 7, 11] jogos [10, 1, 4, 5, 7, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em SEMIFINALS:: Salgueiro 0-1 Náutico (2016-05-04)
- jogo só no ogol, incluído em Final: Santa Cruz 1-0 Sport (2016-05-05)
- jogo só no ogol, incluído em SEMIFINALS:: Náutico 3-0 Salgueiro (2016-05-07)
- jogo só no ogol, incluído em Final: Sport 0-0 Santa Cruz (2016-05-08)

### 2017

- sem ocorrências

### 2018

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2019

- 7 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2020

- 4 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- mando invertido no ogol — RSSSF Petrolina 1-1 Vitória das Tabocas, ogol Vitória das Tabocas 1-1 Petrolina (2020-08-01); fica a RSSSF

### 2021

- tabela publicada x jogos — Primeira fase / -: Retrô FC tabela [9, 3, 1, 5, 15, 15] jogos [12, 5, 1, 6, 22, 17] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Central tabela [9, 2, 3, 4, 8, 16] jogos [12, 2, 4, 6, 9, 20] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-PE tabela [9, 1, 3, 5, 7, 12] jogos [12, 2, 5, 5, 8, 12] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Vitória das Tabocas tabela [9, 1, 2, 6, 7, 21] jogos [12, 2, 3, 7, 9, 26] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Retrô FC tabela [3, 2, 0, 1, 7, 2] jogos [12, 5, 1, 6, 22, 17] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-PE tabela [3, 1, 2, 0, 1, 0] jogos [12, 2, 5, 5, 8, 12] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Vitória das Tabocas tabela [3, 1, 1, 1, 2, 5] jogos [12, 2, 3, 7, 9, 26] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Central tabela [3, 0, 1, 2, 1, 4] jogos [12, 2, 4, 6, 9, 20] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Retrô FC tabela [3, 2, 0, 1, 7, 2] jogos [12, 5, 1, 6, 22, 17] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Sete de Setembro-PE tabela [3, 1, 2, 0, 1, 0] jogos [12, 2, 5, 5, 8, 12] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Vitória das Tabocas tabela [3, 1, 1, 1, 2, 5] jogos [12, 2, 3, 7, 9, 26] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Central tabela [3, 0, 1, 2, 1, 4] jogos [12, 2, 4, 6, 9, 20] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Santa Cruz tabela [11, 4, 4, 3, 13, 11] jogos [11, 3, 5, 3, 13, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Afogados da Ingazeira tabela [10, 2, 6, 2, 9, 7] jogos [10, 2, 7, 1, 9, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Retrô FC x Sete de Setembro-PE, ogol 2021-05-17); fica a do ogol

### 2022

- tabela publicada x jogos — Primeira fase / Grupo: Afogados da Ingazeira tabela [3, 1, 2, 0, 5, 2] jogos [12, 3, 6, 3, 18, 20] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo: Íbis tabela [3, 1, 2, 0, 4, 2] jogos [12, 2, 4, 6, 8, 18] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo: Sete de Setembro-PE tabela [3, 0, 3, 0, 3, 3] jogos [12, 1, 3, 8, 7, 32] — a tabela conta 3 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo: Vera Cruz-PE tabela [3, 0, 1, 2, 3, 8] jogos [12, 1, 4, 7, 17, 26] — a tabela conta 3 jogos e as fontes trazem 12
- jogo só no ogol, incluído em Semifinal: Náutico 0-0 Santa Cruz (2022-04-02)
- jogo só no ogol, incluído em Quartas de final: Sport 2-2 Salgueiro (2022-04-07)
- jogo só no ogol, incluído em Final: Retrô FC 0-1 Náutico (2022-04-30)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Náutico

### 2023

- jogo só no ogol, incluído em FIRST STAGE:: Petrolina 1-1 Íbis (2023-01-18)
- jogo só no ogol, incluído em FIRST STAGE:: Náutico 2-0 Belo Jardim (2023-01-18)
- jogo só no ogol, incluído em FIRST STAGE:: Porto-PE 0-0 Santa Cruz (2023-01-19)
- jogo só no ogol, incluído em FIRST STAGE:: Caruaru City 0-4 Retrô FC (2023-01-19)
- jogo só no ogol, incluído em FIRST STAGE:: Central 1-1 Afogados da Ingazeira (2023-01-19)
- jogo só no ogol, incluído em FIRST STAGE:: Íbis 0-0 Salgueiro (2023-01-24)
- jogo só no ogol, incluído em FIRST STAGE:: Sport 6-1 Belo Jardim (2023-01-24)
- jogo só no ogol, incluído em FIRST STAGE:: Porto-PE 1-1 Afogados da Ingazeira (2023-01-25)
- jogo só no ogol, incluído em FIRST STAGE:: Retrô FC 1-1 Náutico (2023-01-25)
- jogo só no ogol, incluído em FIRST STAGE:: Maguary-PE 2-1 Petrolina (2023-01-26)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Cruz 1-0 Caruaru City (2023-01-26)
- jogo só no ogol, incluído em FIRST STAGE:: Sport 1-0 Retrô FC (2023-01-28)
- jogo só no ogol, incluído em FIRST STAGE:: Salgueiro 1-1 Central (2023-01-28)
- jogo só no ogol, incluído em FIRST STAGE:: Íbis 3-1 Caruaru City (2023-01-29)
- jogo só no ogol, incluído em FIRST STAGE:: Belo Jardim 1-2 Petrolina (2023-01-29)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Cruz 1-1 Maguary-PE (2023-01-29)
- jogo só no ogol, incluído em FIRST STAGE:: Náutico 0-0 Porto-PE (2023-01-30)
- jogo só no ogol, incluído em FIRST STAGE:: Sport 4-1 Afogados da Ingazeira (2023-02-01)
- jogo só no ogol, incluído em FIRST STAGE:: Caruaru City 0-2 Salgueiro (2023-02-01)
- jogo só no ogol, incluído em FIRST STAGE:: Central 2-1 Íbis (2023-02-01)
- jogo só no ogol, incluído em FIRST STAGE:: Petrolina 0-0 Santa Cruz (2023-02-01)
- jogo só no ogol, incluído em FIRST STAGE:: Maguary-PE 0-0 Belo Jardim (2023-02-02)
- jogo só no ogol, incluído em FIRST STAGE:: Retrô FC 1-0 Porto-PE (2023-02-04)
- jogo só no ogol, incluído em FIRST STAGE:: Salgueiro 0-1 Santa Cruz (2023-02-04)
- jogo só no ogol, incluído em FIRST STAGE:: Central 1-2 Petrolina (2023-02-05)
- jogo só no ogol, incluído em FIRST STAGE:: Íbis 2-0 Belo Jardim (2023-02-07)
- jogo só no ogol, incluído em FIRST STAGE:: Afogados da Ingazeira 0-1 Náutico (2023-02-07)
- jogo só no ogol, incluído em FIRST STAGE:: Caruaru City 2-3 Maguary-PE (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Porto-PE 0-0 Sport (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Belo Jardim 0-1 Salgueiro (2023-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Afogados da Ingazeira 0-2 Retrô FC (2023-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Náutico 2-2 Sport (2023-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Petrolina 2-0 Caruaru City (2023-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: Maguary-PE 1-1 Central (2023-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: Retrô FC 1-1 Santa Cruz (2023-02-25)
- jogo só no ogol, incluído em FIRST STAGE:: Belo Jardim 1-2 Central (2023-02-26)
- jogo só no ogol, incluído em FIRST STAGE:: Caruaru City 0-3 Sport (2023-02-26)
- jogo só no ogol, incluído em FIRST STAGE:: Afogados da Ingazeira 1-1 Maguary-PE (2023-02-26)
- jogo só no ogol, incluído em FIRST STAGE:: Salgueiro 0-0 Porto-PE (2023-02-28)
- jogo só no ogol, incluído em FIRST STAGE:: Sport 5-0 Íbis (2023-03-01)
- jogo só no ogol, incluído em FIRST STAGE:: Retrô FC 0-0 Petrolina (2023-03-04)
- jogo só no ogol, incluído em FIRST STAGE:: Central 1-1 Caruaru City (2023-03-05)
- jogo só no ogol, incluído em FIRST STAGE:: Porto-PE 2-1 Íbis (2023-03-11)
- jogo só no ogol, incluído em FIRST STAGE:: Sport 2-0 Santa Cruz (2023-03-11)
- jogo só no ogol, incluído em FIRST STAGE:: Petrolina 4-2 Afogados da Ingazeira (2023-03-12)
- jogo só no ogol, incluído em FIRST STAGE:: Náutico 2-0 Salgueiro (2023-03-12)
- jogo só no ogol, incluído em FIRST STAGE:: Caruaru City 0-4 Belo Jardim (2023-03-15)
- jogo só no ogol, incluído em FIRST STAGE:: Íbis 0-4 Náutico (2023-03-15)
- jogo só no ogol, incluído em FIRST STAGE:: Petrolina 1-0 Porto-PE (2023-03-18)
- jogo só no ogol, incluído em FIRST STAGE:: Maguary-PE 0-1 Náutico (2023-03-18)
- jogo só no ogol, incluído em FIRST STAGE:: Retrô FC 1-0 Salgueiro (2023-03-19)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Cruz 3-1 Central (2023-03-25)
- jogo só no ogol, incluído em FIRST STAGE:: Afogados da Ingazeira 1-0 Íbis (2023-03-25)
- jogo só no ogol, incluído em FIRST STAGE:: Maguary-PE 1-3 Retrô FC (2023-03-26)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Cruz 1-3 Íbis (2023-03-29)
- jogo só no ogol, incluído em FIRST STAGE:: Porto-PE 1-1 Maguary-PE (2023-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Náutico 1-0 Petrolina (2023-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Salgueiro 3-2 Afogados da Ingazeira (2023-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Íbis 1-4 Retrô FC (2023-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Central 0-1 Sport (2023-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Belo Jardim 1-3 Santa Cruz (2023-04-01)
- jogo só no ogol, incluído em Quartas de final: Petrolina 1-1 Santa Cruz (2023-04-04)
- jogo só no ogol, incluído em Quartas de final: Náutico 1-1 Salgueiro (2023-04-06)
- jogo só no ogol, incluído em Semifinal: Sport 2-0 Petrolina (2023-04-07)
- jogo só no ogol, incluído em Semifinal: Retrô FC 3-1 Salgueiro (2023-04-08)
- jogo só no ogol, incluído em Final: Retrô FC 1-2 Sport (2023-04-15)
- jogo só no ogol, incluído em Final: Sport 2-0 Retrô FC (2023-04-22)

### 2024

- placar diferente no ogol — Sport x Santa Cruz (2024-03-16): RSSSF 1-1, ogol 0-0; fica o da RSSSF

### 2025

- 4 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- jogo só no ogol, incluído em Final: Retrô FC 2-3 Sport (2025-03-22)
- jogo só no ogol, incluído em Final: Sport 1-2 Retrô FC (2025-04-03)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Sport

### 2026

- sem ocorrências

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-pe1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
