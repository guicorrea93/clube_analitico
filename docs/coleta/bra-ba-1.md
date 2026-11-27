# Campeonato Baiano (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-ba-1/importar.py`. Pacote em `data/coleta/bra-ba-1/pacote/`. Mesmo código do Catarinense
(`docs/coleta/bra-sc-1.md`), com as fontes da Bahia.

**Temporadas:** 1905 a 2026, 122 edições (escopo aprovado pelo Guilherme em 27/11/2026). Em 1915 e 1916 só entra o
campeonato oficial (o da liga rival, a LSB, ninguém reconhece). Títulos divididos: 1938 (o cisma; Bahia e Botafogo) e
1999 (Bahia e Vitória). Edições sem página da RSSSF e sem jogos no ogol entram só com campeão e vice.

**Fontes:** RSSSF Brasil (`tablesae/ba{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada
edição e o código de cada clube; jogos a partir de 1999); Wikipédia em português (artigo "Campeonato Baiano de Futebol
Masculino": campeão e vice de cada ano, segunda fonte).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1905 | RSSSF + ogol | 4 | 12 (12) | 36 | 1 | 2 / 0 | Internacional de Cricket | RSSSF (classificação geral publicada) |
| 1906 | RSSSF + ogol | 5 | 15 (12) | 36 | 0 | 0 / 2 | São Salvador-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1907 | RSSSF + ogol | 4 | 12 (12) | 43 | 0 | 2 / 0 | São Salvador-BA | RSSSF (classificação geral publicada) |
| 1908 | RSSSF | 3 | 6 (0) | 16 | 6 | 0 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1909 | RSSSF | 3 | 6 (0) | 10 | 0 | 2 / 0 | Vitória | RSSSF (classificação geral publicada) |
| 1910 | RSSSF | 4 | 12 (0) | 24 | 0 | 2 / 0 | Santos Dumont | RSSSF (classificação geral publicada) |
| 1911 | RSSSF | 5 | 20 (0) | 71 | 0 | 0 / 2 | Sport Club Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1912 | RSSSF | 5 | 13 (0) | 34 | 0 | 0 / 2 | Santos Dumont | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1913 | RSSSF | 4 | 12 (0) | 32 | 0 | 2 / 0 | Fluminense de Salvador | RSSSF (classificação geral publicada) |
| 1914 | RSSSF | 5 | 18 (0) | 27 | 0 | 0 / 1 | Internacional de Cricket | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1915 | RSSSF | 5 | 17 (0) | 38 | 0 | 0 / 1 | Fluminense de Salvador | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 | RSSSF | 5 | 20 (0) | 62 | 0 | 1 / 0 | República-BA | RSSSF (classificação geral publicada) |
| 1917 | RSSSF | 6 | 26 (0) | 59 | 0 | 0 / 1 | Ypiranga-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1918 | RSSSF | 5 | 18 (0) | 66 | 0 | 0 / 1 | Ypiranga-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1919 | RSSSF | 6 | 31 (0) | 90 | 0 | 0 / 1 | Botafogo-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF | 12 | 65 (0) | 231 | 0 | 1 / 1 | Ypiranga-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF | 12 | 64 (0) | 231 | 0 | 0 / 1 | Ypiranga-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1923 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1924 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1925 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1926 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1927 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1928 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1929 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1930 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1931 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1932 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1933 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1934 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1935 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1936 | RSSSF | 7 | 39 (0) | 205 | 0 | 0 / 1 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF | 5 | 29 (0) | 126 | 0 | 0 / 1 | Galícia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1939 | RSSSF | 5 | 30 (0) | 168 | 164 | 1 / 0 | Ypiranga-BA | RSSSF (classificação geral publicada) |
| 1940 | RSSSF | 5 | 21 (0) | 116 | 0 | 1 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1941 | RSSSF | 5 | 20 (0) | 84 | 0 | 1 / 0 | Galícia | RSSSF (classificação geral publicada) |
| 1942 | RSSSF | 6 | 29 (0) | 141 | 0 | 0 / 1 | Galícia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF | 6 | 39 (0) | 185 | 0 | 1 / 3 | Galícia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 | RSSSF | 6 | 30 (0) | 135 | 0 | 1 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1945 | RSSSF | 6 | 48 (0) | 240 | 0 | 2 / 3 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF | 7 | 48 (0) | 195 | 0 | 3 / 0 | Guarany-BA | RSSSF (classificação geral publicada) |
| 1947 | RSSSF | 7 | 64 (0) | 295 | 0 | 4 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1948 | RSSSF | 7 | 71 (0) | 281 | 0 | 1 / 4 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 7 | 46 (0) | 167 | 0 | 1 / 3 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF | 7 | 44 (0) | 167 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 7 | 64 (0) | 219 | 0 | 0 / 3 | Ypiranga-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 7 | 68 (0) | 211 | 0 | 5 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1953 | RSSSF | 7 | 63 (0) | 215 | 0 | 2 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 3 | 7 (0) | 16 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 7 | 45 (0) | 143 | 0 | 4 / 0 | Vitória | RSSSF (classificação geral publicada) |
| 1956 | RSSSF | 7 | 46 (0) | 150 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 7 | 65 (0) | 223 | 0 | 5 / 0 | Vitória | RSSSF (classificação geral publicada) |
| 1958 | RSSSF | 7 | 65 (0) | 195 | 0 | 4 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1959 | RSSSF | 8 | 87 (0) | 261 | 3 | 3 / 2 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 9 | 73 (0) | 259 | 0 | 1 / 3 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1962 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1963 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1964 | RSSSF | 9 | 66 (0) | 196 | 0 | 0 / 1 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF | 9 | 67 (0) | 177 | 0 | 3 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF | 11 | 76 (0) | 231 | 0 | 3 / 0 | Leônico-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF | 14 | 186 (0) | 445 | 0 | 0 / 4 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF | 14 | 137 (0) | 315 | 0 | 4 / 2 | Galícia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1970 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1971 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1972 | RSSSF | 13 | 161 (0) | 340 | 0 | 5 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 13 | 146 (0) | 299 | 0 | 5 / 2 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1975 | RSSSF | 10 | 103 (0) | 215 | 0 | 4 / 1 | Bahia | RSSSF (classificação geral publicada) |
| 1976 | RSSSF | 12 | 156 (0) | 396 | 0 | 4 / 9 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 12 | 172 (0) | 405 | 0 | 4 / 8 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 9 | 85 (0) | 203 | 0 | 3 / 1 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 11 | 153 (0) | 345 | 0 | 2 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF | 13 | 193 (0) | 416 | 0 | 0 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF | 12 | 182 (0) | 442 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1983 | RSSSF | 12 | 191 (0) | 362 | 0 | 6 / 3 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 10 | 148 (0) | 307 | 0 | 4 / 4 | Bahia | RSSSF (classificação geral publicada) |
| 1985 | RSSSF | 12 | 154 (0) | 327 | 0 | 2 / 5 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 12 | 148 (0) | 325 | 0 | 5 / 1 | Bahia | RSSSF (classificação geral publicada) |
| 1987 | RSSSF | 12 | 139 (0) | 321 | 0 | 5 / 3 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 10 | 127 (0) | 283 | 0 | 7 / 7 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 10 | 127 (0) | 262 | 0 | 13 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF | 10 | 59 (0) | 95 | 0 | 3 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF | 2 | 1 (0) | 2 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF | 2 | 1 (0) | 6 | 0 | 0 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF | 10 | 114 (0) | 237 | 0 | 13 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 1994 | RSSSF | 3 | 6 (0) | 17 | 2 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 13 | 186 (0) | 438 | 0 | 9 / 2 | Vitória | RSSSF (classificação geral publicada) |
| 1996 | RSSSF | 14 | 99 (0) | 240 | 0 | 0 / 6 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 15 | 114 (110) | 300 | 0 | 4 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 12 | 78 (78) | 216 | 0 | 5 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 10 | 59 (59) | 166 | 0 | 4 / 1 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 10 | 96 (96) | 272 | 0 | 0 / 3 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 10 | 95 (95) | 319 | 2 | 3 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 12 | 105 (74) | 299 | 193 | 0 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 13 | 58 (58) | 163 | 61 | 3 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 13 | 58 (58) | 153 | 52 | 2 / 1 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 13 | 68 (68) | 186 | 0 | 4 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 12 | 162 (162) | 515 | 0 | 1 / 5 | Colo Colo-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 12 | 144 (144) | 460 | 0 | 1 / 2 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 12 | 144 (144) | 428 | 0 | 5 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 12 | 138 (138) | 392 | 284 | 1 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 12 | 114 (114) | 319 | 282 | 6 / 1 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 12 | 116 (114) | 322 | 7 | 5 / 1 | Bahia de Feira | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 12 | 140 (140) | 405 | 313 | 1 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 12 | 76 (76) | 188 | 119 | 4 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 12 | 76 (76) | 231 | 231 | 3 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 12 | 56 (56) | 126 | 126 | 6 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 12 | 56 (56) | 136 | 95 | 1 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 11 | 61 (61) | 156 | 156 | 4 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 10 | 50 (51) | 135 | 135 | 3 / 1 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 10 | 51 (51) | 142 | 142 | 4 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 10 | 51 (51) | 141 | 141 | 4 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 10 | 51 (51) | 111 | 111 | 3 / 0 | Atlético-BA | RSSSF (classificação geral publicada) |
| 2022 | ogol | 10 | 51 (51) | 110 | 0 | 0 / 0 | Atlético-BA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 10 | 51 (51) | 113 | 113 | 3 / 0 | Bahia | RSSSF (classificação geral publicada) |
| 2024 | RSSSF + ogol | 10 | 51 (51) | 134 | 121 | 4 / 0 | Vitória | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 10 | 50 (51) | 116 | 37 | 1 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 10 | 48 (48) | 123 | 0 | 0 / 0 | Bahia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1905

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Bahiano x Internacional de Cricket, ogol 1905-07-23); fica a do ogol
- vice pela Wikipédia (sem final de dois clubes): São Salvador-BA

### 1906

- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [6, 5, 1, 0, 11, 0] jogos [7, 6, 1, 0, 12, 0] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Vitória tabela [6, 3, 1, 2, 16, 3] jogos [7, 4, 1, 2, 18, 4] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Bahiano tabela [6, 0, 2, 4, 0, 17] jogos [7, 0, 2, 5, 0, 21] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [6, 5, 1, 0, 11, 0] jogos [7, 6, 1, 0, 12, 0] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Vitória tabela [6, 3, 1, 2, 16, 3] jogos [7, 4, 1, 2, 18, 4] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Bahiano tabela [6, 0, 2, 4, 0, 17] jogos [7, 0, 2, 5, 0, 21] — a tabela conta 6 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- só na RSSSF (não achado no ogol): Internacional de Cricket 4-0 Bahiano (1906-05-13)
- só na RSSSF (não achado no ogol): São Salvador-BA 1-0 Internacional de Cricket (1906-05-27)
- só na RSSSF (não achado no ogol): Vitória 2-1 Internacional de Cricket (1906-06-10)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1907

- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: São Salvador-BA x Santos Dumont, ogol 1907-06-16); fica a do ogol
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1908

- tabela publicada x jogos — Fase única / -: Vitória tabela [4, 4, 0, 0, 6, 1] jogos [4, 4, 0, 0, 8, 1] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Santos Dumont tabela [4, 2, 0, 2, 6, 4] jogos [4, 2, 0, 2, 8, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [4, 0, 0, 4, 0, 7] jogos [4, 0, 0, 4, 0, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vitória tabela [4, 4, 0, 0, 6, 1] jogos [4, 4, 0, 0, 8, 1] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Santos Dumont tabela [4, 2, 0, 2, 6, 4] jogos [4, 2, 0, 2, 8, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [4, 0, 0, 4, 0, 7] jogos [4, 0, 0, 4, 0, 11] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santos Dumont
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Salvador
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Santos Dumont — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santos Dumont)
- São Salvador — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Salvador-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Santos Dumont

### 1909

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santos Dumont
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Salvador
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Santos Dumont — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santos Dumont)
- São Salvador — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Salvador-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Santos Dumont

### 1910

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Vermelho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santos Dumont
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Rio Vermelho — clube que o ogol não tem; entra só pela RSSSF
- Santos Dumont — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santos Dumont)
- São Paulo — clube que o ogol não tem; entra só pela RSSSF
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1911

- tabela publicada x jogos — Fase única / -: Vitória tabela [8, 5, 1, 2, 15, 18] jogos [8, 5, 1, 2, 15, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vitória tabela [8, 5, 1, 2, 15, 18] jogos [8, 5, 1, 2, 15, 8] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Vermelho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santos Dumont
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Salvador
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Rio Vermelho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Vermelho)
- Santos Dumont — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santos Dumont)
- São Salvador — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Salvador-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1912

- tabela publicada x jogos — Fase única / -: Santos Dumont tabela [4, 3, 1, 0, 4, 1] jogos [6, 5, 1, 0, 7, 2] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Vitória tabela [4, 2, 1, 1, 8, 4] jogos [6, 3, 1, 2, 14, 9] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [4, 0, 0, 4, 2, 9] jogos [6, 0, 0, 6, 2, 11] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Santos Dumont tabela [4, 3, 1, 0, 4, 1] jogos [6, 5, 1, 0, 7, 2] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Vitória tabela [4, 2, 1, 1, 8, 4] jogos [6, 3, 1, 2, 14, 9] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: São Salvador-BA tabela [4, 0, 0, 4, 2, 9] jogos [6, 0, 0, 6, 2, 11] — a tabela conta 4 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio Vermelho
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Salvador
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Rio Vermelho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Vermelho)
- São Salvador — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Salvador-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1913

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ideal
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Ideal — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Sul América — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Internacional de Cricket

### 1914

- tabela publicada x jogos — Segunda fase / -: Ypiranga-BA tabela [8, 3, 3, 2, 3, 3] jogos [7, 1, 3, 3, 2, 4] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Sul América-BA tabela [8, 2, 1, 5, 6, 9] jogos [7, 3, 0, 4, 6, 7] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Brasileiro tabela [8, 0, 0, 8, 3, 11] jogos [8, 0, 1, 7, 4, 12] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasileiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Brasileiro — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- vice pela Wikipédia (sem final de dois clubes): Fluminense de Salvador

### 1915

- tabela publicada x jogos — Segunda fase / -: Fluminense de Salvador tabela [8, 6, 1, 1, 11, 5] jogos [7, 5, 1, 1, 11, 5] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Internacional de Cricket tabela [8, 4, 0, 4, 8, 13] jogos [7, 3, 0, 4, 8, 13] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Sul América-BA tabela [8, 3, 1, 4, 8, 11] jogos [7, 2, 1, 4, 8, 11] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Guarany-BA tabela [8, 0, 0, 8, 0, 5] jogos [5, 0, 0, 5, 0, 5] — a tabela conta 8 jogos e as fontes trazem 5
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Guarany — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- campeão pela lista oficial, Fluminense de Salvador; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ypiranga-BA

### 1916

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): República
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- República — clube que o ogol não tem; entra só pela RSSSF
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- campeão pela lista oficial, República-BA; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Fluminense de Salvador

### 1917

- tabela publicada x jogos — Segunda fase / -: Ypiranga-BA tabela [10, 8, 2, 0, 9, 1] jogos [8, 6, 2, 0, 9, 1] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / -: Fluminense de Salvador tabela [10, 4, 3, 3, 9, 8] jogos [9, 3, 3, 3, 9, 8] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Botafogo-BA tabela [10, 3, 4, 3, 14, 11] jogos [9, 3, 4, 2, 14, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: República-BA tabela [10, 3, 3, 4, 12, 9] jogos [9, 3, 3, 3, 12, 9] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Internacional de Cricket tabela [10, 2, 5, 3, 9, 11] jogos [9, 1, 5, 3, 9, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Sul América-BA tabela [10, 1, 1, 8, 6, 19] jogos [8, 1, 1, 6, 6, 19] — a tabela conta 10 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): República
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- República — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (República-BA)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- vice pela Wikipédia (sem final de dois clubes): Fluminense de Salvador

### 1918

- tabela publicada x jogos — Segunda fase / -: Ypiranga-BA tabela [8, 8, 0, 0, 21, 7] jogos [7, 7, 0, 0, 21, 7] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Botafogo-BA tabela [8, 4, 1, 3, 20, 10] jogos [7, 4, 1, 2, 20, 10] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Fluminense de Salvador tabela [8, 4, 1, 3, 9, 7] jogos [7, 3, 1, 3, 9, 7] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Sul América-BA tabela [8, 3, 0, 5, 10, 15] jogos [7, 3, 0, 4, 10, 15] — a tabela conta 8 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- vice pela Wikipédia (sem final de dois clubes): Botafogo-BA

### 1919

- tabela publicada x jogos — Segunda fase / -: Fluminense de Salvador tabela [10, 8, 1, 1, 20, 6] jogos [9, 7, 1, 1, 20, 6] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Ypiranga-BA tabela [10, 5, 1, 4, 17, 8] jogos [9, 5, 1, 3, 17, 8] — a tabela conta 10 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)

### 1920

- tabela publicada x jogos — Primeira fase / -: Fluminense de Salvador tabela [11, 9, 1, 1, 44, 5] jogos [10, 9, 1, 0, 44, 5] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Santa Cruz-BA tabela [11, 7, 2, 2, 21, 15] jogos [10, 6, 2, 2, 21, 15] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Botafogo-BA tabela [11, 5, 3, 3, 13, 15] jogos [10, 4, 3, 3, 13, 15] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Vitória tabela [11, 3, 2, 6, 19, 18] jogos [10, 3, 2, 5, 19, 18] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Yankee tabela [11, 3, 2, 6, 14, 27] jogos [11, 2, 2, 7, 11, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Sul América-BA tabela [11, 2, 4, 5, 3, 16] jogos [10, 1, 4, 5, 3, 16] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Internacional de Cricket tabela [11, 0, 3, 8, 4, 21] jogos [10, 1, 3, 6, 7, 18] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Itapagipe tabela [11, 1, 0, 10, 4, 39] jogos [9, 0, 0, 9, 4, 39] — a tabela conta 11 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahiano de Tênis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapagipe
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Yankee
- Bahiano de Tênis — clube que o ogol não tem; entra só pela RSSSF
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Itapagipe — clube que o ogol não tem; entra só pela RSSSF
- Nacional — clube que o ogol não tem; entra só pela RSSSF
- Santa Cruz — clube que o ogol não tem; entra só pela RSSSF
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Yankee — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Fluminense de Salvador

### 1921

- tabela publicada x jogos — Fase única / -: AA da Bahia tabela [11, 10, 0, 1, 41, 6] jogos [10, 9, 0, 1, 41, 6] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Botafogo-BA tabela [11, 7, 1, 3, 20, 11] jogos [10, 7, 1, 2, 20, 11] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: São Bento-BA tabela [11, 4, 2, 5, 13, 25] jogos [10, 3, 2, 5, 13, 25] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Sul América-BA tabela [11, 1, 1, 9, 10, 31] jogos [10, 0, 1, 9, 5, 36] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Internacional de Cricket tabela [11, 1, 1, 9, 16, 39] jogos [11, 2, 1, 8, 21, 34] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahiano de Tênis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sul América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Bento
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória'
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Yankee
- Bahiano de Tênis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahiano de Tênis)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Cricket)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-BA)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz-BA)
- Sul América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sul América-BA)
- São Bento — clube que o ogol não tem; entra só pela RSSSF
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Vitória' — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Yankee — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Yankee)

### 1922

- sem ocorrências

### 1923

- sem ocorrências

### 1924

- sem ocorrências

### 1925

- sem ocorrências

### 1926

- sem ocorrências

### 1927

- sem ocorrências

### 1928

- sem ocorrências

### 1929

- sem ocorrências

### 1930

- sem ocorrências

### 1931

- sem ocorrências

### 1932

- sem ocorrências

### 1933

- sem ocorrências

### 1934

- sem ocorrências

### 1935

- sem ocorrências

### 1936

- tabela publicada x jogos — Fase única / -: Galícia tabela [12, 7, 3, 2, 22, 15] jogos [11, 6, 3, 2, 22, 15] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Botafogo-BA tabela [12, 6, 2, 4, 35, 22] jogos [11, 5, 2, 4, 35, 22] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Vitória tabela [12, 4, 1, 7, 34, 22] jogos [9, 4, 1, 4, 34, 22] — a tabela conta 12 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Fluminense de Salvador tabela [12, 1, 2, 9, 12, 53] jogos [11, 0, 2, 9, 12, 53] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brasil
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Brasil — clube que o ogol não tem; entra só pela RSSSF
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1937

- tabela publicada x jogos — Fase única / -: Galícia tabela [12, 11, 0, 1, 34, 10] jogos [11, 10, 0, 1, 34, 10] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Botafogo-BA tabela [11, 4, 0, 7, 20, 23] jogos [10, 4, 0, 6, 20, 23] — a tabela conta 11 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- vice pela Wikipédia (sem final de dois clubes): Ypiranga-BA

### 1938

- sem ocorrências

### 1939

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1940

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1941

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 1942

- tabela publicada x jogos — Fase única / -: Vitória tabela [10, 7, 0, 3, 31, 15] jogos [9, 7, 0, 2, 29, 12] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Ypiranga-BA tabela [10, 3, 2, 5, 20, 24] jogos [9, 2, 2, 5, 17, 22] — a tabela conta 10 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1943

- tabela publicada x jogos — 2º Turno / -: Galícia tabela [5, 4, 1, 0, 26, 9] jogos [12, 8, 2, 2, 46, 28] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [5, 3, 0, 2, 9, 11] jogos [12, 5, 2, 5, 22, 28] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [5, 2, 2, 1, 14, 10] jogos [5, 1, 3, 1, 14, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [5, 2, 2, 1, 16, 13] jogos [9, 3, 2, 4, 28, 22] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [5, 1, 1, 3, 6, 6] jogos [5, 1, 3, 1, 6, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [4, 2, 1, 1, 8, 7] jogos [17, 8, 4, 5, 34, 32] — a tabela conta 4 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Galícia tabela [4, 2, 1, 1, 10, 14] jogos [17, 9, 3, 5, 57, 39] — a tabela conta 4 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [4, 1, 0, 3, 12, 9] jogos [14, 6, 3, 5, 41, 33] — a tabela conta 4 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Galícia tabela [17, 10, 3, 4, 54, 36] jogos [17, 9, 3, 5, 57, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [17, 9, 3, 5, 34, 32] jogos [17, 8, 4, 5, 34, 32] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [14, 7, 2, 5, 41, 32] jogos [14, 6, 3, 5, 41, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [10, 4, 2, 4, 21, 18] jogos [10, 4, 4, 2, 24, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [10, 3, 2, 5, 17, 13] jogos [10, 3, 4, 3, 17, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Guarany-BA tabela [10, 0, 0, 10, 11, 47] jogos [10, 0, 0, 10, 12, 51] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Botafogo-BA

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Bahia; o 1º pela soma dos jogos da última fase é Galícia (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1945

- tabela publicada x jogos — 3º Turno / -: Vitória tabela [5, 4, 0, 1, 25, 8] jogos [15, 8, 3, 4, 50, 29] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Botafogo-BA tabela [5, 4, 0, 1, 18, 9] jogos [15, 7, 1, 7, 42, 42] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Bahia tabela [5, 4, 0, 1, 16, 8] jogos [20, 13, 2, 5, 57, 27] — a tabela conta 5 jogos e as fontes trazem 20
- tabela publicada x jogos — 3º Turno / -: Galícia tabela [5, 2, 0, 3, 9, 13] jogos [17, 10, 2, 5, 43, 31] — a tabela conta 5 jogos e as fontes trazem 17
- tabela publicada x jogos — 3º Turno / -: Ypiranga-BA tabela [5, 1, 0, 4, 9, 14] jogos [15, 5, 2, 8, 31, 35] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Guarany-BA tabela [5, 0, 0, 5, 6, 31] jogos [14, 0, 0, 14, 17, 76] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — 3º Turno / -: Bahia tabela [5, 5, 0, 0, 14, 1] jogos [20, 13, 2, 5, 57, 27] — a tabela conta 5 jogos e as fontes trazem 20
- tabela publicada x jogos — 3º Turno / -: Vitória tabela [5, 2, 1, 2, 5, 3] jogos [15, 8, 3, 4, 50, 29] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Galícia tabela [5, 2, 1, 2, 10, 7] jogos [17, 10, 2, 5, 43, 31] — a tabela conta 5 jogos e as fontes trazem 17
- tabela publicada x jogos — 3º Turno / -: Ypiranga-BA tabela [5, 2, 1, 2, 10, 9] jogos [15, 5, 2, 8, 31, 35] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Botafogo-BA tabela [5, 2, 1, 2, 10, 12] jogos [15, 7, 1, 7, 42, 42] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Guarany-BA tabela [5, 0, 0, 5, 3, 20] jogos [14, 0, 0, 14, 17, 76] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — 3º Turno / -: Vitória tabela [17, 9, 3, 5, 50, 29] jogos [15, 8, 3, 4, 50, 29] — a tabela conta 17 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Botafogo-BA tabela [16, 8, 1, 7, 42, 42] jogos [15, 7, 1, 7, 42, 42] — a tabela conta 16 jogos e as fontes trazem 15
- tabela publicada x jogos — 3º Turno / -: Guarany-BA tabela [15, 0, 0, 15, 17, 76] jogos [14, 0, 0, 14, 17, 76] — a tabela conta 15 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1946

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — clube que o ogol não tem; entra só pela RSSSF
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Ypiranga-BA

### 1947

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1948

- tabela publicada x jogos — 1º Turno / -: Ypiranga-BA tabela [6, 3, 1, 2, 17, 8] jogos [6, 3, 1, 2, 15, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: São Cristóvão-BA tabela [5, 1, 0, 4, 9, 14] jogos [5, 1, 0, 4, 9, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Vitória tabela [6, 4, 2, 0, 13, 6] jogos [6, 3, 3, 0, 13, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Bahia tabela [6, 4, 0, 2, 16, 7] jogos [6, 3, 0, 3, 15, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Galícia tabela [6, 2, 1, 3, 13, 8] jogos [6, 3, 1, 2, 14, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Botafogo-BA tabela [6, 1, 1, 4, 8, 17] jogos [6, 1, 2, 3, 9, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Bahia tabela [3, 2, 1, 0, 10, 2] jogos [4, 3, 1, 0, 13, 2] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Galícia tabela [3, 2, 1, 0, 5, 3] jogos [4, 2, 1, 1, 5, 6] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase final / -: Bahia tabela [21, 12, 4, 5, 47, 28] jogos [22, 12, 4, 6, 49, 29] — a tabela conta 21 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Galícia tabela [21, 10, 5, 6, 52, 37] jogos [24, 11, 5, 8, 54, 47] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase final / -: Vitória tabela [21, 10, 5, 6, 50, 35] jogos [21, 9, 6, 6, 50, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ypiranga-BA tabela [21, 9, 6, 6, 39, 30] jogos [23, 11, 6, 6, 45, 31] — a tabela conta 21 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase final / -: São Cristóvão-BA tabela [17, 4, 4, 9, 28, 45] jogos [17, 4, 4, 9, 28, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Botafogo-BA tabela [17, 4, 3, 10, 25, 47] jogos [17, 4, 4, 9, 26, 47] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1949

- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [6, 5, 1, 0, 17, 8] jogos [10, 6, 2, 2, 22, 15] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [6, 2, 3, 1, 11, 9] jogos [10, 4, 4, 2, 18, 14] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [16, 9, 4, 3, 36, 24] jogos [16, 9, 5, 2, 38, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [12, 4, 3, 5, 23, 21] jogos [12, 4, 6, 2, 19, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Galícia tabela [12, 3, 5, 4, 16, 18] jogos [12, 2, 4, 6, 16, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: São Cristóvão-BA tabela [12, 3, 4, 5, 17, 25] jogos [12, 2, 2, 8, 15, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [12, 0, 1, 11, 13, 36] jogos [12, 2, 2, 8, 18, 36] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Bahia; o 1º pela soma dos jogos da última fase é Ypiranga-BA (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ypiranga-BA

### 1950

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1951

- tabela publicada x jogos — 1º Turno / -: Bahia tabela [6, 3, 1, 2, 12, 10] jogos [6, 3, 1, 2, 11, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [12, 5, 3, 4, 24, 21] jogos [12, 5, 3, 4, 23, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Bahia tabela [18, 9, 4, 5, 42, 28] jogos [18, 9, 4, 5, 41, 28] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ypiranga-BA

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Ypiranga-BA

### 1953

- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [6, 2, 3, 1, 7, 8] jogos [5, 1, 3, 1, 7, 8] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / -: Guarany-BA tabela [6, 0, 2, 4, 6, 13] jogos [5, 0, 2, 3, 6, 13] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Final / -: Ypiranga-BA tabela [18, 9, 4, 5, 30, 24] jogos [17, 8, 4, 5, 30, 24] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Final / -: Guarany-BA tabela [18, 0, 5, 13, 15, 44] jogos [17, 0, 5, 12, 15, 44] — a tabela conta 18 jogos e as fontes trazem 17
- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1954

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1956

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1958

- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1959

- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [7, 2, 1, 4, 5, 8] jogos [6, 1, 1, 4, 5, 8] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Final / -: Bahia tabela [24, 16, 5, 3, 45, 12] jogos [25, 16, 6, 3, 46, 13] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Final / -: Vitória tabela [24, 16, 5, 3, 39, 14] jogos [25, 16, 6, 3, 40, 15] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Final / -: Botafogo-BA tabela [21, 7, 3, 11, 23, 37] jogos [20, 6, 3, 11, 23, 37] — a tabela conta 21 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1960

- tabela publicada x jogos — 1º Turno / -: Bahia tabela [8, 6, 1, 1, 28, 10] jogos [7, 5, 1, 1, 27, 10] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Botafogo-BA tabela [8, 3, 2, 3, 11, 12] jogos [7, 2, 2, 3, 10, 12] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Final / -: Bahia tabela [19, 16, 1, 2, 58, 17] jogos [18, 15, 1, 2, 57, 17] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Botafogo-BA tabela [16, 5, 4, 7, 22, 29] jogos [15, 4, 4, 7, 21, 29] — a tabela conta 16 jogos e as fontes trazem 15
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Leônico — clube que o ogol não tem; entra só pela RSSSF
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1961

- sem ocorrências

### 1962

- sem ocorrências

### 1963

- sem ocorrências

### 1964

- tabela publicada x jogos — 1º Turno / -: Leônico-BA tabela [8, 5, 1, 2, 16, 14] jogos [8, 5, 1, 2, 16, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Guarany-BA tabela [8, 1, 0, 7, 8, 35] jogos [8, 1, 0, 7, 6, 35] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1965

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1966

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela de Março
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SMTC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Estrela de Março — clube que o ogol não tem; entra só pela RSSSF
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Guarany — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarany-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- SMTC — clube que o ogol não tem; entra só pela RSSSF
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1967

- tabela publicada x jogos — 1º Turno / -: Fluminense-BA tabela [13, 7, 5, 1, 17, 9] jogos [13, 7, 5, 1, 22, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Leônico-BA tabela [13, 6, 5, 2, 24, 15] jogos [13, 6, 5, 2, 24, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Conquista 1967 tabela [13, 5, 3, 5, 20, 16] jogos [13, 5, 3, 5, 20, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Bahia de Feira tabela [13, 3, 5, 5, 17, 15] jogos [13, 3, 5, 5, 13, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Ypiranga-BA tabela [13, 2, 2, 9, 13, 27] jogos [13, 2, 2, 9, 11, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — *mando de campo invertido por decisão dos clubes / -: São Cristóvão-BA tabela [13, 3, 6, 4, 11, 18] jogos [12, 2, 6, 4, 11, 18] — a tabela conta 13 jogos e as fontes trazem 12
- tabela publicada x jogos — *mando de campo invertido por decisão dos clubes / -: Vitória de Ilhéus tabela [13, 1, 5, 7, 10, 21] jogos [12, 1, 5, 6, 10, 21] — a tabela conta 13 jogos e as fontes trazem 12
- tabela publicada x jogos — Final / -: Fluminense-BA tabela [26, 15, 8, 3, 39, 14] jogos [26, 15, 8, 3, 44, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Conquista 1967 tabela [25, 8, 5, 12, 30, 30] jogos [25, 8, 5, 12, 30, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Vitória tabela [26, 6, 8, 12, 24, 34] jogos [26, 9, 9, 8, 25, 26] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia de Feira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristovão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória de Ilhéus
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Bahia de Feira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia de Feira)
- Flamengo — clube que o ogol não tem; entra só pela RSSSF
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- São Cristovão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Vitória de Ilhéus — clube que o ogol não tem; entra só pela RSSSF

### 1968

- tabela publicada x jogos — Segunda fase / CHAVE B 2º Turno: Flamengo-BA tabela [12, 3, 6, 3, 10, 14] jogos [6, 0, 5, 1, 4, 7] — a tabela conta 12 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: Flamengo-BA tabela [12, 3, 6, 3, 10, 14] jogos [11, 2, 6, 3, 11, 15] — a tabela conta 12 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia de Feira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Cristóvão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória de Ilhéus
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Bahia de Feira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia de Feira)
- Flamengo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo-BA)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- São Cristóvão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Cristóvão-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Vitória de Ilhéus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória de Ilhéus)
- vice pela Wikipédia (sem final de dois clubes): Fluminense-BA

### 1969

- sem ocorrências

### 1970

- sem ocorrências

### 1971

- sem ocorrências

### 1972

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ilhéus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Ilhéus — clube que o ogol não tem; entra só pela RSSSF
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Palestra — clube que o ogol não tem; entra só pela RSSSF
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1973

- tabela publicada x jogos — Fase final / -: Atlético-BA tabela [3, 2, 1, 0, 5, 1] jogos [7, 2, 1, 4, 5, 6] — a tabela conta 3 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase final / -: Bahia tabela [3, 1, 2, 0, 7, 3] jogos [8, 6, 2, 0, 14, 3] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Vitória tabela [3, 1, 1, 1, 4, 4] jogos [6, 3, 1, 2, 6, 5] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: Bahia tabela [3, 3, 0, 0, 3, 0] jogos [30, 21, 8, 1, 60, 14] — a tabela conta 3 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Vitória tabela [3, 2, 0, 1, 2, 1] jogos [27, 19, 5, 3, 45, 13] — a tabela conta 3 jogos e as fontes trazem 27
- tabela publicada x jogos — Fase final / -: Botafogo-BA tabela [3, 0, 2, 1, 2, 1] jogos [25, 8, 9, 8, 19, 20] — a tabela conta 3 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase final / -: Atlético-BA tabela [3, 0, 0, 3, 0, 3] jogos [28, 11, 10, 7, 32, 17] — a tabela conta 3 jogos e as fontes trazem 28
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ilhéus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Ilhéus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ilhéus)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Palestra — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palestra-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Atlético-BA

### 1974

- sem ocorrências

### 1975

- tabela publicada x jogos — 1º Turno - Final / -: Vitória tabela [3, 1, 1, 1, 3, 3] jogos [3, 0, 2, 1, 2, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Final / -: Botafogo-BA tabela [3, 0, 2, 1, 2, 3] jogos [3, 1, 1, 1, 3, 3] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Bahia

### 1976

- tabela publicada x jogos — 1º Turno - Fase final / -: Vitória tabela [3, 3, 0, 0, 6, 2] jogos [36, 23, 8, 5, 77, 22] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 1º Turno - Fase final / -: Bahia tabela [3, 2, 0, 1, 5, 1] jogos [36, 27, 6, 3, 92, 14] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 1º Turno - Fase final / -: Atlético-BA tabela [3, 1, 0, 2, 5, 6] jogos [34, 16, 9, 9, 49, 39] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — 1º Turno - Fase final / -: Jequié tabela [3, 0, 0, 3, 2, 9] jogos [24, 7, 7, 10, 21, 32] — a tabela conta 3 jogos e as fontes trazem 24
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Bahia tabela [6, 4, 2, 0, 14, 3] jogos [9, 5, 3, 1, 17, 4] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo A: Leônico-BA tabela [6, 2, 2, 2, 7, 5] jogos [9, 2, 3, 4, 9, 10] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo B: Atlético-BA tabela [6, 4, 1, 1, 15, 8] jogos [9, 5, 1, 3, 21, 18] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno - Segunda fase / Grupo B: Vitória tabela [6, 4, 1, 1, 17, 3] jogos [9, 7, 1, 1, 24, 5] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 1º Turno - Fase final / -: Vitória tabela [3, 3, 0, 0, 7, 2] jogos [36, 23, 8, 5, 77, 22] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 1º Turno - Fase final / -: Bahia tabela [3, 1, 1, 1, 3, 1] jogos [36, 27, 6, 3, 92, 14] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 1º Turno - Fase final / -: Atlético-BA tabela [3, 1, 0, 2, 6, 10] jogos [34, 16, 9, 9, 49, 39] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — 1º Turno - Fase final / -: Leônico-BA tabela [3, 0, 1, 2, 2, 5] jogos [25, 5, 6, 14, 23, 44] — a tabela conta 3 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno - Final / -: Bahia tabela [3, 3, 0, 0, 5, 1] jogos [36, 27, 6, 3, 92, 14] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno - Final / -: Vitória tabela [3, 2, 0, 1, 7, 6] jogos [36, 23, 8, 5, 77, 22] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno - Final / -: Fluminense-BA tabela [3, 1, 0, 2, 2, 4] jogos [24, 6, 9, 9, 22, 31] — a tabela conta 3 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno - Final / -: Atlético-BA tabela [3, 0, 0, 3, 3, 6] jogos [34, 16, 9, 9, 49, 39] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Bahia tabela [6, 4, 1, 1, 16, 3] jogos [9, 7, 1, 1, 22, 4] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Ypiranga-BA tabela [6, 4, 1, 1, 9, 4] jogos [9, 4, 1, 4, 11, 12] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Fluminense-BA tabela [6, 0, 3, 3, 4, 11] jogos [5, 0, 3, 2, 4, 9] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Atlético-BA tabela [6, 4, 2, 0, 6, 0] jogos [9, 5, 2, 2, 9, 6] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Vitória tabela [6, 4, 1, 1, 11, 3] jogos [9, 6, 1, 2, 17, 5] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Galícia tabela [6, 2, 1, 3, 5, 9] jogos [5, 1, 1, 3, 3, 9] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / -: Bahia tabela [3, 3, 0, 0, 6, 1] jogos [36, 27, 6, 3, 92, 14] — a tabela conta 3 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno - Fase final / -: Atlético-BA tabela [3, 1, 0, 2, 3, 6] jogos [34, 16, 9, 9, 49, 39] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno - Fase final / -: Ypiranga-BA tabela [3, 0, 0, 3, 2, 8] jogos [25, 10, 4, 11, 30, 34] — a tabela conta 3 jogos e as fontes trazem 25
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Humaitá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitoria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Humaitá — clube que o ogol não tem; entra só pela RSSSF
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — clube que o ogol não tem; entra só pela RSSSF
- Vitoria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1977

- tabela publicada x jogos — 1º Turno / Grupo A: Botafogo-BA tabela [5, 1, 3, 1, 0, 10] jogos [5, 4, 1, 0, 10, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / Grupo B: Vitória tabela [5, 3, 2, 0, 0, 17] jogos [5, 5, 0, 0, 17, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [6, 2, 3, 1, 0, 16] jogos [38, 26, 10, 2, 71, 11] — a tabela conta 6 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Itabuna-BA tabela [6, 3, 1, 2, 0, 15] jogos [30, 12, 10, 8, 44, 26] — a tabela conta 6 jogos e as fontes trazem 30
- tabela publicada x jogos — 3º Turno / Grupo A: Bahia tabela [5, 1, 2, 2, 0, 9] jogos [5, 3, 2, 0, 9, 0] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / Grupo A: Botafogo-BA tabela [5, 1, 0, 4, 0, 7] jogos [5, 1, 4, 0, 7, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / Grupo B: Atlético-BA tabela [5, 1, 2, 2, 0, 9] jogos [5, 3, 2, 0, 9, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 4º Turno / -: Bahia tabela [6, 3, 1, 2, 0, 14] jogos [38, 26, 10, 2, 71, 11] — a tabela conta 6 jogos e as fontes trazem 38
- tabela publicada x jogos — 4º Turno / -: Botafogo-BA tabela [6, 3, 1, 2, 0, 14] jogos [34, 16, 10, 8, 54, 27] — a tabela conta 6 jogos e as fontes trazem 34
- tabela publicada x jogos — 4º Turno / -: Vitória tabela [6, 0, 3, 3, 0, 5] jogos [34, 16, 11, 7, 51, 21] — a tabela conta 6 jogos e as fontes trazem 34
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Humaitá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Humaitá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Humaitá-BA)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Botafogo-BA

### 1978

- tabela publicada x jogos — 1º Turno / -: Itabuna-BA tabela [8, 4, 4, 0, 8, 5] jogos [7, 3, 4, 0, 8, 5] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / -: Vitória tabela [8, 3, 1, 4, 6, 5] jogos [7, 3, 1, 3, 6, 5] — a tabela conta 8 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BAHIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITABUNA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JEQUIÉ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): LEÔNICO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): REDENÇÃO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VITÓRIA
- ABB — clube que o ogol não tem; entra só pela RSSSF
- BAHIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- ITABUNA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- JEQUIÉ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- LEÔNICO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- REDENÇÃO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- VITÓRIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1979

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- ABB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ABB-BA)
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1980

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galicia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Humaitá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- ABB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ABB-BA)
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Galicia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Humaitá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Humaitá-BA)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1981

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galicia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galicia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1982

- sem ocorrências

### 1983

- tabela publicada x jogos — 2º Turno / -: Catuense tabela [6, 2, 3, 1, 4, 2] jogos [6, 2, 4, 0, 4, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [6, 2, 2, 2, 10, 6] jogos [6, 2, 3, 1, 10, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Galícia tabela [6, 2, 0, 4, 7, 7] jogos [6, 2, 2, 2, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [6, 0, 2, 4, 1, 14] jogos [6, 3, 2, 1, 11, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 4º Turno / -: Bahia tabela [6, 0, 2, 4, 3, 9] jogos [6, 3, 3, 0, 5, 1] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Fluminense-BA tabela [34, 15, 11, 8, 37, 29] jogos [34, 15, 12, 7, 37, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Serrano-BA tabela [36, 15, 10, 11, 35, 27] jogos [36, 14, 11, 11, 33, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Vitória tabela [32, 10, 14, 8, 38, 30] jogos [32, 10, 15, 7, 38, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Galícia tabela [30, 11, 8, 11, 34, 35] jogos [30, 11, 8, 11, 33, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Botafogo-BA tabela [28, 5, 9, 14, 19, 38] jogos [28, 4, 10, 14, 18, 38] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia de Feira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leõnico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitoria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Bahia de Feira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia de Feira)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Leõnico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitoria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Bahia

### 1984

- tabela publicada x jogos — Coloca��o - Segundo Turno (Primeira Fase) / -: Fluminense-BA tabela [9, 3, 2, 4, 11, 8] jogos [9, 4, 2, 3, 11, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Coloca��o - Terceiro Turno (Primeira Fase) / -: Fluminense-BA tabela [7, 2, 1, 4, 5, 12] jogos [7, 1, 1, 5, 5, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno - Fase final / -: Catuense tabela [3, 2, 0, 1, 6, 3] jogos [9, 3, 3, 3, 13, 12] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — 3º Turno - Fase final / -: Bahia tabela [3, 2, 0, 1, 3, 2] jogos [9, 5, 3, 1, 17, 9] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Coloca��o - Fase Final do Campeonato / -: Bahia tabela [6, 3, 3, 0, 14, 7] jogos [9, 5, 3, 1, 17, 9] — a tabela conta 6 jogos e as fontes trazem 9
- tabela publicada x jogos — Coloca��o - Fase Final do Campeonato / -: Catuense tabela [6, 1, 3, 2, 7, 9] jogos [9, 3, 3, 3, 13, 12] — a tabela conta 6 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Leônico-BA

### 1985

- tabela publicada x jogos — 1º Turno - Segunda fase / -: Botafogo-BA tabela [6, 4, 2, 0, 4, 4] jogos [22, 5, 2, 15, 10, 30] — a tabela conta 6 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Ypiranga-BA tabela [5, 3, 1, 1, 3, 3] jogos [24, 8, 5, 11, 18, 23] — a tabela conta 5 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Atlético-BA tabela [5, 3, 1, 1, 3, 4] jogos [5, 1, 1, 3, 4, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: Redenção tabela [5, 3, 1, 1, 3, 5] jogos [5, 1, 1, 3, 5, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: ABB-BA tabela [5, 3, 1, 1, 3, 4] jogos [5, 1, 1, 3, 4, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo B: Ypiranga-BA tabela [5, 3, 1, 1, 3, 5] jogos [5, 1, 1, 3, 5, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno - Fase final / -: Serrano-BA tabela [6, 4, 2, 0, 4, 6] jogos [28, 14, 5, 9, 25, 27] — a tabela conta 6 jogos e as fontes trazem 28
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Redenção
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- ABB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ABB-BA)
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Redenção — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Redenção)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 1986

- tabela publicada x jogos — 2º Turno / Grupo B: Leônico-BA tabela [10, 4, 4, 2, 14, 7] jogos [10, 4, 3, 3, 14, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo B: Serrano-BA tabela [10, 3, 6, 1, 14, 11] jogos [10, 4, 4, 2, 14, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / Grupo B: Fluminense-BA tabela [10, 4, 3, 3, 14, 9] jogos [10, 3, 6, 1, 14, 11] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- ABB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ABB-BA)
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Bahia; o 1º pela soma dos jogos da última fase é Vitória (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Catuense

### 1987

- tabela publicada x jogos — 2º Turno / Grupo A: Bahia tabela [11, 8, 3, 0, 26, 7] jogos [2, 2, 0, 0, 5, 2] — a tabela conta 11 jogos e as fontes trazem 2
- tabela publicada x jogos — 2º Turno / Grupo A: Itabuna-BA tabela [11, 4, 4, 3, 9, 8] jogos [2, 2, 0, 0, 5, 1] — a tabela conta 11 jogos e as fontes trazem 2
- tabela publicada x jogos — 2º Turno / Grupo A: Fluminense-BA tabela [11, 4, 4, 3, 10, 9] jogos [3, 1, 0, 2, 3, 4] — a tabela conta 11 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / Grupo A: Bahia de Feira tabela [11, 1, 1, 9, 11, 31] jogos [3, 0, 0, 3, 4, 10] — a tabela conta 11 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / Grupo B: Atlético-BA tabela [11, 5, 2, 4, 12, 12] jogos [9, 4, 2, 3, 10, 7] — a tabela conta 11 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Botafogo-BA tabela [11, 2, 6, 3, 11, 13] jogos [5, 1, 2, 2, 5, 7] — a tabela conta 11 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: Leônico-BA tabela [11, 3, 2, 6, 15, 18] jogos [10, 3, 2, 5, 14, 16] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / Grupo C: Vitória tabela [11, 8, 2, 1, 16, 6] jogos [1, 0, 1, 0, 1, 1] — a tabela conta 11 jogos e as fontes trazem 1
- tabela publicada x jogos — 2º Turno / Grupo C: Serrano-BA tabela [11, 5, 4, 2, 9, 8] jogos [1, 0, 1, 0, 1, 1] — a tabela conta 11 jogos e as fontes trazem 1
- tabela publicada x jogos — 2º Turno / Grupo C: Ypiranga-BA tabela [11, 1, 5, 5, 7, 18] jogos [1, 0, 1, 0, 1, 1] — a tabela conta 11 jogos e as fontes trazem 1
- tabela publicada x jogos — 2º Turno / Grupo C: Galícia tabela [11, 1, 3, 7, 8, 17] jogos [1, 0, 1, 0, 1, 1] — a tabela conta 11 jogos e as fontes trazem 1
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia de Feira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Bahia de Feira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia de Feira)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1988

- tabela publicada x jogos — 1º Turno - Fase final / -: Bahia tabela [3, 1, 2, 0, 2, 0] jogos [6, 2, 3, 1, 3, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Fase final / -: Vitória tabela [3, 1, 2, 0, 1, 0] jogos [6, 3, 3, 0, 4, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Fase final / -: Catuense tabela [3, 1, 1, 1, 1, 2] jogos [6, 1, 2, 3, 2, 5] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Fase final / -: Vitória tabela [3, 2, 1, 0, 3, 1] jogos [6, 3, 3, 0, 4, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Fase final / -: Bahia tabela [3, 1, 1, 1, 1, 1] jogos [6, 2, 3, 1, 3, 1] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Fase final / -: Catuense tabela [3, 0, 1, 2, 1, 3] jogos [6, 1, 2, 3, 2, 5] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Leônico-BA tabela [5, 0, 0, 5, 4, 10] jogos [5, 0, 0, 5, 3, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno - Fase final / -: Bahia tabela [3, 2, 1, 0, 8, 0] jogos [37, 21, 10, 6, 74, 21] — a tabela conta 3 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno - Fase final / -: Fluminense-BA tabela [3, 2, 0, 1, 9, 6] jogos [30, 12, 9, 9, 34, 29] — a tabela conta 3 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno - Fase final / -: Catuense tabela [3, 1, 1, 1, 2, 2] jogos [33, 10, 13, 10, 33, 26] — a tabela conta 3 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno - Fase final / -: Atlanta-BA tabela [3, 0, 0, 3, 2, 13] jogos [21, 4, 1, 16, 15, 51] — a tabela conta 3 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno - Fase final / Grupo A: Vitória tabela [4, 3, 0, 1, 7, 2] jogos [5, 3, 0, 2, 7, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / Grupo A: Serrano-BA tabela [4, 2, 2, 0, 6, 3] jogos [5, 3, 2, 0, 7, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / Grupo A: Fluminense-BA tabela [4, 2, 1, 1, 7, 5] jogos [5, 3, 1, 1, 14, 7] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / Grupo A: Atlanta-BA tabela [4, 0, 0, 4, 3, 11] jogos [5, 0, 0, 5, 5, 18] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / Grupo B: Botafogo-BA tabela [4, 3, 0, 1, 7, 5] jogos [5, 3, 1, 1, 7, 5] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / Grupo B: Bahia tabela [4, 2, 1, 1, 7, 4] jogos [6, 2, 3, 1, 7, 4] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno - Fase final / Grupo B: Catuense tabela [4, 2, 1, 1, 5, 3] jogos [5, 2, 2, 1, 5, 3] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno - Fase final / -: Bahia tabela [3, 2, 1, 0, 8, 3] jogos [37, 21, 10, 6, 74, 21] — a tabela conta 3 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno - Fase final / -: Serrano-BA tabela [3, 1, 1, 1, 5, 5] jogos [24, 6, 9, 9, 23, 24] — a tabela conta 3 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno - Fase final / -: Vitória tabela [3, 1, 0, 2, 5, 8] jogos [34, 18, 9, 7, 42, 30] — a tabela conta 3 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno - Fase final / -: Botafogo-BA tabela [3, 0, 2, 1, 4, 6] jogos [21, 6, 4, 11, 21, 39] — a tabela conta 3 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlanta
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Atlanta — clube que o ogol não tem; entra só pela RSSSF
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1989

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 1990

- tabela publicada x jogos — 2º Turno / -: Galícia tabela [5, 2, 2, 1, 8, 3] jogos [1, 0, 1, 0, 0, 0] — a tabela conta 5 jogos e as fontes trazem 1
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [5, 2, 1, 2, 8, 8] jogos [1, 0, 0, 1, 0, 3] — a tabela conta 5 jogos e as fontes trazem 1
- tabela publicada x jogos — 2º Turno / -: Jacuipense tabela [5, 2, 0, 3, 8, 6] jogos [4, 2, 0, 2, 8, 4] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Catuense tabela [5, 0, 2, 3, 2, 5] jogos [4, 0, 2, 2, 1, 3] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Fluminense-BA tabela [5, 4, 1, 0, 7, 1] jogos [16, 8, 6, 2, 14, 6] — a tabela conta 5 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [5, 3, 1, 1, 7, 4] jogos [19, 9, 6, 4, 20, 10] — a tabela conta 5 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Itabuna-BA tabela [5, 3, 0, 2, 8, 6] jogos [10, 6, 1, 3, 12, 9] — a tabela conta 5 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Atlético-BA tabela [5, 1, 2, 2, 3, 7] jogos [7, 2, 1, 4, 4, 7] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Leônico-BA tabela [5, 0, 3, 2, 3, 12] jogos [7, 0, 2, 5, 4, 16] — a tabela conta 5 jogos e as fontes trazem 7
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacuipense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Leônico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jacuipense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacuipense)
- Leônico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Leônico-BA)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vencedor da final pelos jogos (Fluminense-BA) diferente do campeão oficial (Vitória); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Fluminense-BA

### 1991

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)

### 1992

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Vitória; o 1º pela soma dos jogos da última fase é Bahia (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 1993

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Camaçari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itabuna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacuipense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Camaçari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Camaçari)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Itabuna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itabuna-BA)
- Jacuipense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacuipense)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1994

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Camaçari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Camaçari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Camaçari)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Bahia; o 1º pela soma dos jogos da última fase é Vitória (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Vitória

### 1995

- tabela publicada x jogos — 2º Turno - Final / -: Vitória tabela [2, 2, 0, 0, 2, 0] jogos [4, 4, 0, 0, 6, 0] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno - Final / -: Vitória tabela [2, 2, 0, 0, 4, 0] jogos [4, 4, 0, 0, 6, 0] — a tabela conta 2 jogos e as fontes trazem 4
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Camaçari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Eunápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Poções
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Camaçari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Camaçari)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Eunápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Eunápolis)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Poções — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Poções)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- vice pela Wikipédia (sem final de dois clubes): Galícia

### 1996

- tabela publicada x jogos — 1º Turno / -: Eunápolis tabela [7, 5, 1, 1, 8, 5] jogos [5, 3, 1, 1, 3, 2] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / -: Poções tabela [7, 3, 3, 1, 4, 7] jogos [6, 3, 3, 0, 4, 1] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Galícia tabela [7, 2, 2, 3, 5, 7] jogos [4, 1, 2, 1, 4, 5] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: São Francisco 1996 tabela [7, 2, 2, 3, 5, 10] jogos [4, 1, 1, 2, 3, 5] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Camaçari tabela [7, 1, 2, 4, 6, 12] jogos [5, 1, 1, 3, 2, 4] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno / -: Bahia tabela [7, 5, 0, 2, 16, 5] jogos [4, 3, 0, 1, 5, 2] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: River Ilheense tabela [7, 3, 1, 3, 9, 5] jogos [6, 2, 1, 3, 5, 5] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Catuense tabela [7, 3, 0, 4, 8, 8] jogos [7, 2, 1, 4, 8, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Jacuipense tabela [7, 1, 4, 2, 7, 9] jogos [4, 0, 3, 1, 4, 6] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno / -: Ypiranga-BA tabela [7, 1, 1, 5, 6, 12] jogos [6, 1, 1, 4, 4, 9] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Conquista-BA tabela [7, 0, 4, 3, 3, 11] jogos [4, 0, 2, 2, 0, 7] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Fluminense-BA tabela [7, 3, 2, 2, 6, 5] jogos [5, 2, 1, 2, 4, 5] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Poções tabela [7, 3, 2, 2, 11, 8] jogos [6, 3, 1, 2, 10, 7] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Vitória tabela [7, 2, 3, 2, 14, 12] jogos [4, 1, 3, 0, 8, 5] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Galícia tabela [7, 1, 3, 3, 7, 10] jogos [6, 0, 3, 3, 5, 9] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Camaçari tabela [7, 1, 1, 5, 9, 13] jogos [4, 0, 1, 3, 5, 8] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Eunápolis tabela [7, 0, 4, 3, 6, 11] jogos [4, 0, 2, 2, 3, 7] — a tabela conta 7 jogos e as fontes trazem 4
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Conquista-BA tabela [7, 5, 2, 0, 9, 4] jogos [5, 4, 1, 0, 6, 2] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Catuense tabela [7, 5, 1, 1, 14, 10] jogos [5, 3, 1, 1, 8, 6] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Bahia tabela [7, 3, 2, 2, 11, 8] jogos [5, 3, 1, 1, 9, 5] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Ypiranga-BA tabela [7, 2, 4, 1, 9, 9] jogos [5, 2, 3, 0, 7, 5] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — 1º Turno - Segunda fase / -: Jacuipense tabela [7, 2, 2, 3, 6, 7] jogos [2, 0, 1, 1, 1, 2] — a tabela conta 7 jogos e as fontes trazem 2
- tabela publicada x jogos — 2º Turno / -: Vitória tabela [8, 5, 2, 1, 22, 11] jogos [18, 12, 4, 2, 41, 14] — a tabela conta 8 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Poções tabela [8, 4, 1, 3, 11, 8] jogos [20, 10, 6, 4, 25, 15] — a tabela conta 8 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Catuense tabela [8, 3, 1, 4, 17, 11] jogos [18, 7, 3, 8, 24, 23] — a tabela conta 8 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Conquista-BA tabela [8, 1, 2, 5, 10, 16] jogos [13, 4, 4, 5, 12, 20] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Bahia tabela [8, 5, 2, 1, 15, 8] jogos [6, 4, 1, 1, 14, 8] — a tabela conta 8 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Fluminense-BA tabela [8, 4, 0, 4, 10, 18] jogos [6, 3, 0, 3, 8, 10] — a tabela conta 8 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / -: Eunápolis tabela [8, 2, 3, 3, 13, 17] jogos [3, 0, 2, 1, 3, 6] — a tabela conta 8 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Camaçari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Catuense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Eunápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Galícia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jacuipense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jequié
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Poções
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Camaçari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Camaçari)
- Catuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catuense)
- Eunápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Eunápolis)
- Galícia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Galícia)
- Jacuipense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jacuipense)
- Jequié — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jequié)
- Poções — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Poções)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- campeão pela lista oficial, Vitória; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 1997

- data diferente entre RSSSF e ogol (mais de 3 dias) em 12 jogos (ex.: Bahia x Conquista-BA, ogol 1997-02-02); fica a do ogol
- adversário diferente no ogol — RSSSF Bahia 2-0 São Francisco 1996, ogol Bahia 2-0 São Francisco-BA (1997-01-26); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 2-1 Eunápolis, ogol São Francisco-BA 2-1 Eunápolis (1997-02-16); fica a RSSSF
- adversário diferente no ogol — RSSSF River Ilheense 0-1 São Francisco 1996, ogol River Ilheense 0-1 São Francisco-BA (1997-03-02); fica a RSSSF
- adversário diferente no ogol — RSSSF Jequié 0-1 São Francisco 1996, ogol Jequié 0-1 São Francisco-BA (1997-03-09); fica a RSSSF
- adversário diferente no ogol — RSSSF Catuense 0-0 São Francisco 1996, ogol Catuense 0-0 São Francisco-BA (1997-03-16); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 1-0 Catuense, ogol São Francisco-BA 1-0 Catuense (1997-04-16); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 1-0 Jequié, ogol São Francisco-BA 1-0 Jequié (1997-04-20); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 1-1 Bahia, ogol São Francisco-BA 1-1 Bahia (1997-04-27); fica a RSSSF
- adversário diferente no ogol — RSSSF Eunápolis 1-3 São Francisco 1996, ogol Eunápolis 1-3 São Francisco-BA (1997-04-30); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 0-0 River Ilheense, ogol São Francisco-BA 0-0 River Ilheense (1997-05-04); fica a RSSSF
- adversário diferente no ogol — RSSSF Ypiranga-BA 2-0 São Francisco 1996, ogol Ypiranga-BA 2-0 São Francisco-BA (1997-05-10); fica a RSSSF
- adversário diferente no ogol — RSSSF Poções 4-2 São Francisco 1996, ogol Poções 4-2 São Francisco-BA (1997-05-24); fica a RSSSF
- jogo só no ogol, incluído em First Phase: São Francisco-BA 0-0 Poções (1997-02-02)
- jogo só no ogol, incluído em First Phase: São Francisco-BA 2-1 Ypiranga-BA (1997-02-23)
- jogo só no ogol, incluído em Semi-Finals:: São Francisco-BA 0-1 Bahia (1997-03-23)
- jogo só no ogol, incluído em Semi-Finals:: Bahia 5-1 São Francisco-BA (1997-03-30)
- só na RSSSF (não achado no ogol): São Francisco 1996 0-0 Poções (1997-01-26)
- só na RSSSF (não achado no ogol): São Francisco 1996 2-1 Ypiranga-BA (1997-02-16)
- só na RSSSF (não achado no ogol): São Francisco 1996 0-1 Bahia (None)
- só na RSSSF (não achado no ogol): Bahia 5-1 São Francisco 1996 (None)

### 1998

- adversário diferente no ogol — RSSSF Vitória 5-0 São Francisco 1996, ogol Vitória 5-0 São Francisco-BA (1998-01-25); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 0-1 Camaçari, ogol São Francisco-BA 0-1 Camaçari (1998-02-01); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 5-1 Ypiranga-BA, ogol São Francisco-BA 5-1 Ypiranga-BA (1998-02-07); fica a RSSSF
- adversário diferente no ogol — RSSSF Fluminense-BA 1-2 São Francisco 1996, ogol Fluminense-BA 1-2 São Francisco-BA (1998-02-15); fica a RSSSF
- adversário diferente no ogol — RSSSF Poções 0-1 São Francisco 1996, ogol Poções 0-1 São Francisco-BA (1998-03-01); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 1-0 Eunápolis, ogol São Francisco-BA 1-0 Eunápolis (1998-03-08); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 0-2 Bahia, ogol São Francisco-BA 0-2 Bahia (1998-04-07); fica a RSSSF
- adversário diferente no ogol — RSSSF Galícia 1-1 São Francisco 1996, ogol Galícia 1-1 São Francisco-BA (1998-04-12); fica a RSSSF
- adversário diferente no ogol — RSSSF Juazeiro 1-2 São Francisco 1996, ogol Juazeiro 1-2 São Francisco-BA (1998-04-19); fica a RSSSF
- adversário diferente no ogol — RSSSF São Francisco 1996 1-1 Catuense, ogol São Francisco-BA 1-1 Catuense (1998-04-21); fica a RSSSF
- adversário diferente no ogol — RSSSF Conquista-BA 1-1 São Francisco 1996, ogol Conquista-BA 1-1 São Francisco-BA (1998-05-01); fica a RSSSF

### 1999

- tabela publicada x jogos — Final / -: Vitória tabela [9, 6, 3, 0, 20, 4] jogos [18, 11, 5, 2, 38, 13] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Bahia tabela [9, 6, 1, 2, 20, 7] jogos [18, 10, 5, 3, 34, 15] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Conquista-BA tabela [9, 4, 4, 1, 13, 11] jogos [11, 4, 4, 3, 15, 22] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Poções tabela [9, 4, 3, 2, 9, 7] jogos [11, 4, 3, 4, 10, 10] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Juazeiro tabela [9, 4, 2, 3, 16, 11] jogos [11, 4, 3, 4, 17, 15] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Camaçari tabela [9, 3, 2, 4, 16, 17] jogos [11, 3, 3, 5, 19, 21] — a tabela conta 9 jogos e as fontes trazem 11
- 1 jogos de repescagem contra clube de fora da divisão ficam fora (D-04): Fluminense 1-1 Galícia
- placar diferente no ogol — Poções x Vitória (1999-05-09): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Bahia x Camaçari, ogol 1999-05-15); fica a do ogol

### 2000

- tabela publicada x jogos — Primeira fase / -: Juazeiro tabela [9, 5, 3, 1, 10, 6] jogos [9, 5, 3, 1, 11, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Poções tabela [9, 4, 2, 3, 15, 16] jogos [9, 4, 2, 3, 15, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Fluminense-BA tabela [9, 3, 1, 5, 13, 16] jogos [9, 3, 1, 5, 13, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Bahia tabela [9, 8, 0, 1, 28, 6] jogos [11, 9, 0, 2, 32, 8] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Vitória tabela [9, 6, 1, 2, 18, 9] jogos [11, 7, 1, 3, 22, 13] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Juazeiro tabela [9, 4, 1, 4, 15, 15] jogos [9, 4, 1, 4, 16, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Bahia tabela [18, 13, 2, 3, 44, 13] jogos [22, 14, 3, 5, 50, 19] — a tabela conta 18 jogos e as fontes trazem 22
- tabela publicada x jogos — Final / -: Vitória tabela [18, 12, 3, 3, 33, 14] jogos [24, 15, 4, 5, 43, 22] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Juazeiro tabela [18, 9, 4, 5, 25, 21] jogos [20, 10, 4, 6, 29, 25] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Poções tabela [18, 8, 3, 7, 36, 36] jogos [18, 8, 3, 7, 36, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Fluminense-BA tabela [18, 5, 4, 9, 20, 29] jogos [18, 5, 4, 9, 20, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 15 jogos (ex.: Camaçari x Vitória, ogol 2000-04-01); fica a do ogol

### 2001

- sem ocorrências

### 2002

- tabela publicada x jogos — Primeira fase / -: Colo Colo-BA tabela [16, 6, 5, 5, 22, 28] jogos [16, 6, 4, 6, 19, 25] — placar diverge entre RSSSF e ogol em Poções x Colo Colo-BA (None-None x 1-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Poções tabela [16, 3, 7, 6, 21, 28] jogos [16, 3, 7, 6, 18, 25] — placar diverge entre RSSSF e ogol em Poções x Colo Colo-BA (None-None x 1-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Cruzeiro-BA tabela [10, 4, 0, 6, 10, 18] jogos [27, 12, 6, 9, 42, 37] — a tabela conta 10 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Catuense tabela [10, 2, 5, 3, 14, 13] jogos [25, 8, 11, 6, 33, 28] — a tabela conta 10 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Palmeiras Nordeste tabela [10, 3, 1, 6, 8, 16] jogos [28, 12, 8, 8, 44, 37] — a tabela conta 10 jogos e as fontes trazem 28
- jogo anulado ou cancelado fica de fora: Catuense 3-0 Cruzeiro (2002-05-28) [Catuense played 10 minutes of the match with 12 players,  [Fumaça, Braína, Elzon]         they scored a goal that was annulled due to that irregular]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bahia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vitória
- Bahia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bahia)
- Vitória — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vitória)
- só na RSSSF (não achado no ogol): Bahia 1-1 Catuense (2002-05-15)
- só na RSSSF (não achado no ogol): Palmeiras Nordeste 3-1 Vitória (2002-05-15)
- só na RSSSF (não achado no ogol): Cruzeiro-BA 0-2 Fluminense-BA (2002-05-15)
- só na RSSSF (não achado no ogol): Fluminense-BA 0-0 Bahia (2002-05-19)
- só na RSSSF (não achado no ogol): Catuense 1-1 Palmeiras Nordeste (2002-05-19)
- só na RSSSF (não achado no ogol): Vitória 4-0 Cruzeiro-BA (2002-05-19)
- só na RSSSF (não achado no ogol): Bahia 5-2 Cruzeiro-BA (2002-05-22)
- só na RSSSF (não achado no ogol): Palmeiras Nordeste 1-0 Fluminense-BA (2002-05-22)
- só na RSSSF (não achado no ogol): Catuense 1-2 Vitória (2002-05-22)
- só na RSSSF (não achado no ogol): Vitória 4-3 Bahia (2002-05-26)
- só na RSSSF (não achado no ogol): Cruzeiro-BA 3-0 Palmeiras Nordeste (2002-05-26)
- só na RSSSF (não achado no ogol): Fluminense-BA 3-3 Catuense (2002-05-26)
- só na RSSSF (não achado no ogol): Bahia 5-0 Palmeiras Nordeste (2002-05-28)
- só na RSSSF (não achado no ogol): Fluminense-BA 0-0 Vitória (2002-05-28)
- só na RSSSF (não achado no ogol): Bahia 2-3 Fluminense-BA (2002-05-30)
- só na RSSSF (não achado no ogol): Palmeiras Nordeste 1-2 Catuense (2002-05-30)
- só na RSSSF (não achado no ogol): Cruzeiro-BA 2-1 Vitória (2002-05-30)
- só na RSSSF (não achado no ogol): Catuense 0-0 Bahia (2002-06-02)
- só na RSSSF (não achado no ogol): Vitória 2-0 Palmeiras Nordeste (2002-06-02)
- só na RSSSF (não achado no ogol): Fluminense-BA 1-0 Cruzeiro-BA (2002-06-02)
- só na RSSSF (não achado no ogol): Cruzeiro-BA 1-0 Bahia (2002-06-05)
- só na RSSSF (não achado no ogol): Fluminense-BA 1-1 Palmeiras Nordeste (2002-06-05)
- só na RSSSF (não achado no ogol): Vitória 2-1 Catuense (2002-06-05)
- só na RSSSF (não achado no ogol): Bahia 3-3 Vitória (2002-06-09)
- só na RSSSF (não achado no ogol): Palmeiras Nordeste 1-0 Cruzeiro-BA (2002-06-09)
- só na RSSSF (não achado no ogol): Catuense 1-1 Fluminense-BA (2002-06-09)
- só na RSSSF (não achado no ogol): Palmeiras Nordeste 0-1 Bahia (2002-06-12)
- só na RSSSF (não achado no ogol): Vitória 3-1 Fluminense-BA (2002-06-12)
- só na RSSSF (não achado no ogol): Cruzeiro-BA 2-1 Catuense (2002-06-12)
- só na RSSSF (não achado no ogol): Fluminense-BA 0-0 Vitória (2002-06-16)
- só na RSSSF (não achado no ogol): Vitória 5-0 Fluminense-BA (2002-06-20)

### 2003

- sem ocorrências

### 2004

- tabela publicada x jogos — Primeira fase / Grupo 2: Palmeiras Nordeste tabela [6, 2, 1, 3, 8, 9] jogos [6, 2, 1, 3, 8, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Vitória x Camaçari, ogol 2004-01-18); fica a do ogol

### 2005

- tabela publicada x jogos — Primeira fase / Grupo A: Atlético-BA tabela [8, 4, 0, 4, 9, 11] jogos [8, 4, 0, 4, 9, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Atlético-BA tabela [8, 4, 0, 4, 9, 11] jogos [8, 4, 0, 4, 9, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Juazeiro x Bahia, ogol 2005-01-26); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vitória

### 2006

- tabela publicada x jogos — Primeira fase / Grupo 1: Camaçari tabela [12, 4, 2, 6, 18, 13] jogos [12, 4, 2, 6, 17, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 1: Poções tabela [12, 4, 1, 7, 14, 23] jogos [12, 4, 1, 7, 14, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 2: Ipitanga tabela [12, 5, 5, 2, 22, 15] jogos [12, 5, 5, 2, 21, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 2: Vitória tabela [10, 7, 3, 0, 27, 7] jogos [8, 6, 2, 0, 23, 4] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 2: Itabuna-BA tabela [10, 5, 1, 4, 17, 20] jogos [8, 3, 1, 4, 13, 19] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 2: Ipitanga tabela [10, 4, 2, 4, 18, 16] jogos [8, 3, 3, 2, 15, 12] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 2: Juazeiro tabela [10, 3, 2, 5, 18, 22] jogos [8, 2, 2, 4, 13, 14] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 2: Atlético-BA tabela [10, 3, 1, 6, 12, 23] jogos [8, 1, 2, 5, 5, 20] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Final / -: Vitória tabela [22, 16, 6, 0, 59, 17] jogos [24, 16, 7, 1, 60, 19] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Colo Colo-BA tabela [22, 12, 6, 4, 45, 30] jogos [24, 13, 7, 4, 47, 31] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Ipitanga tabela [22, 9, 7, 6, 40, 31] jogos [22, 9, 8, 5, 39, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Camaçari tabela [22, 7, 9, 6, 35, 25] jogos [22, 7, 9, 6, 34, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Atlético-BA tabela [22, 6, 1, 15, 20, 45] jogos [22, 5, 2, 15, 18, 44] — placar diverge entre RSSSF e ogol em Atlético-BA x Catuense (0-1 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Atlético-BA x Catuense (2006-01-15): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Fluminense-BA x Camaçariense (2006-02-05): RSSSF 2-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo-BA x Bahia (2006-04-07): RSSSF 3-1, ogol 2-0; fica o da RSSSF
- jogo só no ogol, incluído em Primeira Fase: Colo Colo-BA 1-1 Vitória (2006-03-26)
- jogo só no ogol, incluído em Primeira Fase: Vitória 0-1 Colo Colo-BA (2006-04-01)
- jogo só no ogol, incluído em Torneio de rebaixamento: Camaçariense 3-2 Catuense (2006-05-14)
- jogo só no ogol, incluído em Torneio de rebaixamento: Catuense 1-0 Camaçariense (2006-05-21)
- jogo só no ogol, incluído em Final: Colo Colo-BA 4-3 Vitória (2006-05-25)
- jogo só no ogol, incluído em Final: Vitória 2-4 Colo Colo-BA (2006-05-28)

### 2007

- tabela publicada x jogos — Primeira fase / -: Bahia tabela [22, 15, 5, 2, 50, 27] jogos [22, 15, 5, 2, 51, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Atlético-BA tabela [22, 11, 3, 8, 42, 35] jogos [22, 11, 3, 8, 42, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Juazeiro tabela [22, 11, 1, 10, 33, 35] jogos [22, 11, 1, 10, 32, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Catuense tabela [22, 3, 4, 15, 19, 49] jogos [22, 3, 4, 15, 19, 50] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Bahia tabela [22, 15, 5, 2, 50, 27] jogos [22, 15, 5, 2, 51, 27] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Atlético-BA tabela [22, 11, 3, 8, 42, 35] jogos [22, 11, 3, 8, 42, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Juazeiro tabela [22, 11, 1, 10, 33, 35] jogos [22, 11, 1, 10, 32, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Catuense tabela [22, 3, 4, 15, 19, 49] jogos [22, 3, 4, 15, 19, 50] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 75 jogos (ex.: Juazeiro x Ipitanga, ogol 2007-02-14); fica a do ogol
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 1-1 Colo Colo-BA (2007-01-17)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 2-1 Itabuna-BA (2007-01-21)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 7-0 Ipitanga (2007-01-31)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 1-3 Bahia (2007-02-04)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 2-3 Vitória da Conquista (2007-02-14)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético-BA 1-2 Juazeiro (2007-02-21)
- jogo só no ogol, incluído em Final Stage: Poções 0-2 Bahia (2007-05-03)
- jogo só no ogol, incluído em Final Stage: Poções 1-2 Vitória (2007-05-06)
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 2008

- placar diferente no ogol — Itabuna-BA x Vitória (2008-02-17): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Ipitanga x Vitória da Conquista (2008-03-16): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Bahia

### 2009

- placar diferente no ogol — Fluminense-BA x Feirense (2009-03-22): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar corrigido pelo ogol — Atlético-BA x Itabuna-BA (2009-04-05): RSSSF 1-2, ogol 1-4; fica o do ogol, que fecha com a tabela publicada
- jogo só no ogol, incluído em Primeira Fase: Madre de Deus 2-2 Poções (2009-03-28)
- jogo só no ogol, incluído em Semi-Final: Bahia 1-2 Vitória (2009-04-26)
- jogo só no ogol, incluído em Final: Vitória 2-2 Bahia (2009-05-03)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vitória

### 2010

- tabela publicada x jogos — Segunda fase / Grupo A: Atlético-BA tabela [6, 0, 3, 3, 4, 12] jogos [6, 0, 3, 3, 4, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Feirense x Camaçari, ogol 2010-04-01); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vitória

### 2011

- tabela publicada x jogos — Quartas de final / -: Bahia de Feira tabela [6, 4, 0, 2, 10, 8] jogos [23, 13, 7, 3, 37, 24] — a tabela conta 6 jogos e as fontes trazem 23
- tabela publicada x jogos — Quartas de final / -: Bahia tabela [6, 3, 1, 2, 10, 4] jogos [21, 11, 3, 7, 35, 20] — a tabela conta 6 jogos e as fontes trazem 21
- tabela publicada x jogos — Quartas de final / -: Vitória da Conquista tabela [6, 2, 1, 3, 11, 15] jogos [19, 8, 3, 8, 28, 32] — a tabela conta 6 jogos e as fontes trazem 19
- tabela publicada x jogos — Quartas de final / -: Atlético-BA tabela [6, 2, 0, 4, 7, 11] jogos [19, 7, 3, 9, 30, 31] — a tabela conta 6 jogos e as fontes trazem 19
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Colo Colo-BA x Ipitanga, ogol 2011-01-30); fica a do ogol
- ano errado na data da RSSSF — Ipitanga 1-0 Colo Colo-BA: RSSSF 2010-03-19, ogol 2011-03-19; fica a do ogol
- ano errado na data da RSSSF — Juazeiro 1-1 Fluminense-BA: RSSSF 2010-03-19, ogol 2011-03-19; fica a do ogol
- ano errado na data da RSSSF — Serrano-BA 1-0 Feirense: RSSSF 2010-03-19, ogol 2011-03-19; fica a do ogol
- ano errado na data da RSSSF — Atlético-BA 2-0 Bahia de Feira: RSSSF 2010-03-20, ogol 2011-03-20; fica a do ogol
- ano errado na data da RSSSF — Vitória da Conquista 2-2 Bahia: RSSSF 2010-03-20, ogol 2011-03-20; fica a do ogol
- ano errado na data da RSSSF — Camaçari 0-2 Vitória: RSSSF 2010-03-20, ogol 2011-03-20; fica a do ogol
- ano errado na data da RSSSF — Fluminense-BA 3-1 Ipitanga: RSSSF 2010-03-22, ogol 2011-03-22; fica a do ogol
- ano errado na data da RSSSF — Vitória 2-1 Serrano-BA: RSSSF 2010-03-23, ogol 2011-03-23; fica a do ogol
- ano errado na data da RSSSF — Colo Colo-BA 2-0 Juazeiro: RSSSF 2010-03-23, ogol 2011-03-23; fica a do ogol
- ano errado na data da RSSSF — Feirense 2-0 Camaçari: RSSSF 2010-03-24, ogol 2011-03-24; fica a do ogol
- ano errado na data da RSSSF — Fluminense-BA 1-0 Colo Colo-BA: RSSSF 2010-03-26, ogol 2011-03-26; fica a do ogol
- ano errado na data da RSSSF — Serrano-BA 1-0 Camaçari: RSSSF 2010-03-26, ogol 2011-03-26; fica a do ogol
- ano errado na data da RSSSF — Bahia 3-0 Bahia de Feira: RSSSF 2010-03-27, ogol 2011-03-27; fica a do ogol
- ano errado na data da RSSSF — Vitória da Conquista 3-0 Atlético-BA: RSSSF 2010-03-27, ogol 2011-03-27; fica a do ogol
- ano errado na data da RSSSF — Feirense 1-3 Vitória: RSSSF 2010-03-27, ogol 2011-03-27; fica a do ogol
- ano errado na data da RSSSF — Juazeiro 7-4 Ipitanga: RSSSF 2010-03-27, ogol 2011-03-27; fica a do ogol
- ano errado na data da RSSSF — Atlético-BA 3-4 Vitória da Conquista: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Bahia de Feira 1-0 Bahia: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Camaçari 1-0 Serrano-BA: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Vitória 4-1 Feirense: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Colo Colo-BA 0-2 Fluminense-BA: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Ipitanga 3-2 Juazeiro: RSSSF 2010-04-03, ogol 2011-04-03; fica a do ogol
- ano errado na data da RSSSF — Ipitanga 2-0 Fluminense-BA: RSSSF 2010-04-06, ogol 2011-04-06; fica a do ogol
- ano errado na data da RSSSF — Juazeiro 2-1 Colo Colo-BA: RSSSF 2010-04-06, ogol 2011-04-06; fica a do ogol
- ano errado na data da RSSSF — Serrano-BA 2-3 Vitória: RSSSF 2010-04-09, ogol 2011-04-09; fica a do ogol
- ano errado na data da RSSSF — Atlético-BA 1-0 Bahia: RSSSF 2010-04-10, ogol 2011-04-10; fica a do ogol
- ano errado na data da RSSSF — Vitória da Conquista 1-2 Bahia de Feira: RSSSF 2010-04-10, ogol 2011-04-10; fica a do ogol
- ano errado na data da RSSSF — Camaçari 1-1 Feirense: RSSSF 2010-04-10, ogol 2011-04-10; fica a do ogol
- ano errado na data da RSSSF — Fluminense-BA 1-1 Juazeiro: RSSSF 2010-04-10, ogol 2011-04-10; fica a do ogol
- ano errado na data da RSSSF — Feirense 0-0 Serrano-BA: RSSSF 2010-04-16, ogol 2011-04-16; fica a do ogol
- ano errado na data da RSSSF — Vitória 0-0 Camaçari: RSSSF 2010-04-16, ogol 2011-04-16; fica a do ogol
- ano errado na data da RSSSF — Bahia 4-0 Vitória da Conquista: RSSSF 2010-04-17, ogol 2011-04-17; fica a do ogol
- ano errado na data da RSSSF — Bahia de Feira 3-1 Atlético-BA: RSSSF 2010-04-17, ogol 2011-04-17; fica a do ogol
- ano errado na data da RSSSF — Bahia 0-1 Vitória: RSSSF 2010-04-24, ogol 2011-04-24; fica a do ogol
- ano errado na data da RSSSF — Serrano-BA 1-2 Bahia de Feira: RSSSF 2010-04-24, ogol 2011-04-24; fica a do ogol
- ano errado na data da RSSSF — Bahia de Feira 1-1 Serrano-BA: RSSSF 2010-05-01, ogol 2011-05-01; fica a do ogol
- ano errado na data da RSSSF — Vitória 2-3 Bahia: RSSSF 2010-05-01, ogol 2011-05-01; fica a do ogol
- ano errado na data da RSSSF — Bahia de Feira 2-2 Vitória: RSSSF 2010-05-08, ogol 2011-05-08; fica a do ogol
- ano errado na data da RSSSF — Vitória 1-2 Bahia de Feira: RSSSF 2010-05-15, ogol 2011-05-15; fica a do ogol
- jogo só no ogol, incluído em Quartas-de-Final: Bahia de Feira 4-1 Vitória da Conquista (2011-03-24)
- jogo só no ogol, incluído em Quartas-de-Final: Bahia 1-0 Atlético-BA (2011-03-25)
- só na RSSSF (não achado no ogol): Bahia de Feira 4-1 Vitória da Conquista (2010-03-23)
- só na RSSSF (não achado no ogol): Bahia 1-0 Atlético-BA (2010-03-24)

### 2012

- placar corrigido pelo ogol — Vitória da Conquista x Bahia de Feira (2012-04-01): RSSSF 4-1, ogol 4-2; fica o do ogol, que fecha com a tabela publicada
- jogo só no ogol, incluído em Final: Vitória 0-0 Bahia (2012-05-06)
- jogo só no ogol, incluído em Semi-Final: Vitória da Conquista 1-4 Feirense (2012-05-06)
- jogo só no ogol, incluído em Final: Bahia 3-3 Vitória (2012-05-13)
- jogo só no ogol, incluído em Semi-Final: Feirense 2-3 Vitória da Conquista (2012-05-13)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Bahia

### 2013

- sem ocorrências

### 2014

- sem ocorrências

### 2015

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Serrano-BA x Jacobina, ogol 2015-03-22); fica a do ogol

### 2016

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flameno
- Flameno — clube que o ogol não tem; entra só pela RSSSF
- jogo só no ogol, incluído em Quartas de final: Fluminense-BA 3-0 Galícia (2016-03-19)
- jogo só no ogol, incluído em Quartas de final: Flamengo de Guanambi 1-0 Vitória (2016-03-19)
- jogo só no ogol, incluído em Quartas de final: Bahia de Feira 0-2 Bahia (2016-03-20)
- jogo só no ogol, incluído em Quartas de final: Juazeirense 2-0 Jacobina (2016-03-20)
- jogo só no ogol, incluído em FIRST STAGE:: Colo Colo-BA 0-0 Vitória da Conquista (2016-03-20)
- jogo só no ogol, incluído em FIRST STAGE:: Jacuipense 2-1 Feirense (2016-03-20)
- jogo só no ogol, incluído em Quartas de final: Galícia 1-0 Fluminense-BA (2016-03-26)
- jogo só no ogol, incluído em Quartas de final: Vitória 3-0 Flamengo de Guanambi (2016-03-26)
- jogo só no ogol, incluído em FIRST STAGE:: Feirense 0-1 Jacuipense (2016-03-27)
- jogo só no ogol, incluído em FIRST STAGE:: Vitória da Conquista 2-1 Colo Colo-BA (2016-03-27)
- jogo só no ogol, incluído em Quartas de final: Bahia 2-1 Bahia de Feira (2016-03-27)
- jogo só no ogol, incluído em Quartas de final: Jacobina 1-0 Juazeirense (2016-03-27)
- jogo só no ogol, incluído em Semifinal: Fluminense-BA 0-2 Bahia (2016-04-09)
- jogo só no ogol, incluído em Semifinal: Juazeirense 2-3 Vitória (2016-04-10)
- jogo só no ogol, incluído em Semifinal: Bahia 2-1 Fluminense-BA (2016-04-21)
- jogo só no ogol, incluído em Semifinal: Vitória 3-0 Juazeirense (2016-04-21)
- jogo só no ogol, incluído em Final: Vitória 2-0 Bahia (2016-05-01)
- jogo só no ogol, incluído em FIRST STAGE:: Fluminense-BA 0-0 Juazeirense (2016-05-01)
- jogo só no ogol, incluído em Final: Bahia 1-0 Vitória (2016-05-08)
- jogo só no ogol, incluído em FIRST STAGE:: Juazeirense 1-1 Fluminense-BA (2016-05-08)

### 2017

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vitória

### 2018

- tabela publicada x jogos — Primeira fase / -: Vitória tabela [9, 7, 1, 1, 19, 9] jogos [8, 7, 1, 0, 19, 6] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Bahia tabela [9, 6, 2, 1, 21, 6] jogos [8, 5, 2, 1, 18, 6] — a tabela conta 9 jogos e as fontes trazem 8
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Vitória x Bahia (2018-02-18)

### 2019

- sem ocorrências

### 2020

- sem ocorrências

### 2021

- sem ocorrências

### 2022

- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 2-2 Bahia (2022-01-15)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 1-0 Doce Mel (2022-01-15)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 4-1 Vitória da Conquista (2022-01-15)
- jogo só no ogol, incluído em Primeira fase: Vitória 1-1 Juazeirense (2022-01-16)
- jogo só no ogol, incluído em Primeira fase: UNIRB 0-0 Barcelona de Ilhéus (2022-01-16)
- jogo só no ogol, incluído em Primeira fase: Bahia 1-1 UNIRB (2022-01-19)
- jogo só no ogol, incluído em Primeira fase: Doce Mel 1-3 Atlético-BA (2022-01-20)
- jogo só no ogol, incluído em Primeira fase: Vitória da Conquista 0-2 Bahia de Feira (2022-01-22)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 0-1 Vitória (2022-01-23)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 2-5 Jacuipense (2022-01-23)
- jogo só no ogol, incluído em Primeira fase: Bahia 1-0 Doce Mel (2022-01-26)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 0-1 Barcelona de Ilhéus (2022-01-27)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 1-0 Vitória (2022-01-29)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 1-0 Atlético-BA (2022-01-30)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 0-0 Vitória da Conquista (2022-01-30)
- jogo só no ogol, incluído em Primeira fase: Vitória 1-1 Bahia (2022-02-02)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 2-0 UNIRB (2022-02-03)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 1-0 Juazeirense (2022-02-05)
- jogo só no ogol, incluído em Primeira fase: UNIRB 0-1 Jacuipense (2022-02-06)
- jogo só no ogol, incluído em Primeira fase: Doce Mel 2-0 Vitória da Conquista (2022-02-06)
- jogo só no ogol, incluído em Primeira fase: Bahia 0-1 Barcelona de Ilhéus (2022-02-09)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 3-3 UNIRB (2022-02-10)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 0-0 Doce Mel (2022-02-12)
- jogo só no ogol, incluído em Primeira fase: Vitória da Conquista 0-1 Vitória (2022-02-13)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 2-0 Bahia de Feira (2022-02-16)
- jogo só no ogol, incluído em Primeira fase: UNIRB 3-2 Doce Mel (2022-02-17)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 3-1 Vitória da Conquista (2022-02-19)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 1-1 Bahia de Feira (2022-02-20)
- jogo só no ogol, incluído em Primeira fase: Vitória 0-0 Atlético-BA (2022-02-26)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 1-0 Bahia (2022-02-27)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 2-1 Bahia (2022-03-02)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 0-3 Jacuipense (2022-03-05)
- jogo só no ogol, incluído em Primeira fase: Vitória da Conquista 2-0 UNIRB (2022-03-06)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 2-1 Juazeirense (2022-03-06)
- jogo só no ogol, incluído em Primeira fase: Doce Mel 1-0 Vitória (2022-03-09)
- jogo só no ogol, incluído em Primeira fase: Vitória da Conquista 1-0 Barcelona de Ilhéus (2022-03-10)
- jogo só no ogol, incluído em Primeira fase: Bahia 4-1 Jacuipense (2022-03-12)
- jogo só no ogol, incluído em Primeira fase: UNIRB 1-1 Vitória (2022-03-12)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 2-0 Juazeirense (2022-03-13)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 2-1 Doce Mel (2022-03-13)
- jogo só no ogol, incluído em Primeira fase: Doce Mel 1-2 Barcelona de Ilhéus (2022-03-16)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 2-3 Atlético-BA (2022-03-16)
- jogo só no ogol, incluído em Primeira fase: Bahia 3-0 Vitória da Conquista (2022-03-16)
- jogo só no ogol, incluído em Primeira fase: Vitória 2-1 Bahia de Feira (2022-03-16)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 2-0 UNIRB (2022-03-16)
- jogo só no ogol, incluído em Semifinal: Bahia de Feira 0-1 Atlético-BA (2022-03-26)
- jogo só no ogol, incluído em Semifinal: Barcelona de Ilhéus 0-0 Jacuipense (2022-03-27)
- jogo só no ogol, incluído em Semifinal: Atlético-BA 1-0 Bahia de Feira (2022-03-30)
- jogo só no ogol, incluído em Semifinal: Jacuipense 1-0 Barcelona de Ilhéus (2022-03-31)
- jogo só no ogol, incluído em Final: Atlético-BA 1-1 Jacuipense (2022-04-03)
- jogo só no ogol, incluído em Final: Jacuipense 0-2 Atlético-BA (2022-04-10)

### 2023

- sem ocorrências

### 2024

- sem ocorrências

### 2025

- sem ocorrências

### 2026

- jogo só no ogol, incluído em Primeira fase: Vitória 0-0 Atlético-BA (2026-01-10)
- jogo só no ogol, incluído em Primeira fase: Porto-BA 3-2 Jacuipense (2026-01-10)
- jogo só no ogol, incluído em Primeira fase: Bahia 4-2 Jequié (2026-01-11)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 0-0 Bahia de Feira (2026-01-11)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 2-0 Galícia (2026-01-12)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 0-0 Vitória (2026-01-13)
- jogo só no ogol, incluído em Primeira fase: Galícia 2-0 Juazeirense (2026-01-14)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 0-3 Bahia (2026-01-14)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 0-1 Barcelona de Ilhéus (2026-01-15)
- jogo só no ogol, incluído em Primeira fase: Jequié 1-1 Porto-BA (2026-01-15)
- jogo só no ogol, incluído em Primeira fase: Bahia 3-0 Galícia (2026-01-17)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 0-0 Jacuipense (2026-01-17)
- jogo só no ogol, incluído em Primeira fase: Porto-BA 1-1 Vitória (2026-01-18)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 0-0 Bahia de Feira (2026-01-18)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 1-0 Jequié (2026-01-19)
- jogo só no ogol, incluído em Primeira fase: Bahia 5-1 Barcelona de Ilhéus (2026-01-20)
- jogo só no ogol, incluído em Primeira fase: Vitória 4-0 Juazeirense (2026-01-21)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 1-1 Porto-BA (2026-01-22)
- jogo só no ogol, incluído em Primeira fase: Jequié 4-1 Atlético-BA (2026-01-23)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 2-1 Galícia (2026-01-24)
- jogo só no ogol, incluído em Primeira fase: Vitória 0-1 Bahia (2026-01-25)
- jogo só no ogol, incluído em Primeira fase: Galícia 1-0 Atlético-BA (2026-01-27)
- jogo só no ogol, incluído em Primeira fase: Porto-BA 1-1 Barcelona de Ilhéus (2026-01-28)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 0-0 Jacuipense (2026-01-29)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 1-2 Jequié (2026-01-29)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 0-2 Vitória (2026-02-01)
- jogo só no ogol, incluído em Primeira fase: Bahia 3-1 Porto-BA (2026-02-01)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 1-2 Juazeirense (2026-02-03)
- jogo só no ogol, incluído em Primeira fase: Galícia 1-2 Bahia de Feira (2026-02-04)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 0-2 Jequié (2026-02-04)
- jogo só no ogol, incluído em Primeira fase: Jequié 2-2 Vitória (2026-02-07)
- jogo só no ogol, incluído em Primeira fase: Porto-BA 1-0 Galícia (2026-02-07)
- jogo só no ogol, incluído em Primeira fase: Juazeirense 1-1 Bahia (2026-02-08)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 2-1 Atlético-BA (2026-02-10)
- jogo só no ogol, incluído em Primeira fase: Bahia de Feira 6-1 Barcelona de Ilhéus (2026-02-11)
- jogo só no ogol, incluído em Primeira fase: Galícia 2-1 Jequié (2026-02-12)
- jogo só no ogol, incluído em Primeira fase: Bahia 2-2 Jacuipense (2026-02-14)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 0-0 Porto-BA (2026-02-15)
- jogo só no ogol, incluído em Primeira fase: Vitória 1-0 Bahia de Feira (2026-02-18)
- jogo só no ogol, incluído em Primeira fase: Barcelona de Ilhéus 0-0 Juazeirense (2026-02-19)
- jogo só no ogol, incluído em Primeira fase: Atlético-BA 2-4 Bahia (2026-02-21)
- jogo só no ogol, incluído em Primeira fase: Jacuipense 3-1 Bahia de Feira (2026-02-22)
- jogo só no ogol, incluído em Primeira fase: Vitória 3-0 Galícia (2026-02-22)
- jogo só no ogol, incluído em Primeira fase: Porto-BA 1-3 Juazeirense (2026-02-22)
- jogo só no ogol, incluído em Primeira fase: Jequié 1-1 Barcelona de Ilhéus (2026-02-22)
- jogo só no ogol, incluído em Semifinal: Bahia 4-2 Juazeirense (2026-02-28)
- jogo só no ogol, incluído em Semifinal: Vitória 1-1 Jacuipense (2026-03-01)
- jogo só no ogol, incluído em Final: Bahia 2-1 Vitória (2026-03-07)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-ba1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
