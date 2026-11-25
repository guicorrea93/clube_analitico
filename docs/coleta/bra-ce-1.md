# Campeonato Cearense (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-ce-1/importar.py`. Pacote em `data/coleta/bra-ce-1/pacote/`. Mesmo código do Paranaense
(`docs/coleta/bra-pr-1.md`), com as fontes do Ceará.

**Temporadas:** 1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 25/11/2026; a conta da FCF). Ficam fora 1913
(campeão desconhecido) e 1914 (a FCF não reconhece). 1915-1919 são os torneios da Liga Metropolitana, reconhecidos pela
FCF em 2008 (Ato nº 11/2008). 17 edições sem jogos em nenhuma fonte (1916-1919, 1924-1927, 1929-1932, 1934-1938) entram
só com campeão e vice. 1992 teve título dividido entre Fortaleza, Ceará, Tiradentes e Icasa; em 2004 não houve final
(o STJD deu o título ao Fortaleza).

**Fontes:** RSSSF Brasil (`tablesae/ce{ano}.htm`: jogos, fases, datas, autores e tabelas; quando o site não respondeu,
a cópia do Internet Archive, listada em `data/coleta/bra-ce-1/rsssfbrasil/origem.json`); ogol (calendário de cada edição
e o código de cada clube); Wikipédia em português (artigo "Campeonato Cearense de Futebol Masculino": campeão e vice
de cada ano, segunda fonte). Artilheiros pela lista da RSSSF (`cetops.htm`).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1915 | RSSSF | 2 | 1 (0) | 3 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1917 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1918 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1919 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1920 | RSSSF + ogol | 4 | 13 (12) | 30 | 0 | 0 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF | 5 | 6 (0) | 17 | 0 | 1 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF | 5 | 17 (0) | 82 | 0 | 1 / 0 | Ceará | RSSSF (classificação geral publicada) |
| 1923 | RSSSF | 8 | 28 (0) | 118 | 1 | 0 / 2 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1925 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1926 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1927 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1928 | RSSSF | 5 | 19 (0) | 87 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1929 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1930 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1931 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1932 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1933 | RSSSF | 5 | 22 (0) | 113 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1935 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1936 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1937 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1938 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1939 | RSSSF | 7 | 36 (0) | 208 | 0 | 0 / 1 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF | 7 | 47 (0) | 245 | 0 | 2 / 0 | Tramways | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF | 7 | 21 (0) | 111 | 0 | 1 / 0 | Ceará | RSSSF (classificação geral publicada) |
| 1942 | RSSSF | 6 | 40 (0) | 204 | 0 | 0 / 1 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF | 5 | 22 (0) | 100 | 0 | 3 / 0 | Maguari | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 | RSSSF | 6 | 22 (0) | 136 | 0 | 2 / 0 | Maguari | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF | 5 | 18 (0) | 84 | 0 | 0 / 2 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF | 5 | 20 (0) | 100 | 0 | 1 / 0 | Fortaleza | RSSSF (classificação geral publicada) |
| 1947 | RSSSF | 6 | 32 (0) | 164 | 0 | 0 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 8 | 55 (0) | 281 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF + ogol | 6 | 33 (33) | 135 | 0 | 1 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF | 8 | 43 (0) | 160 | 0 | 0 / 1 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 6 | 35 (0) | 165 | 0 | 2 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 5 | 22 (0) | 86 | 0 | 2 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF | 8 | 59 (0) | 188 | 0 | 2 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 8 | 69 (0) | 236 | 0 | 2 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 8 | 46 (0) | 157 | 0 | 2 / 0 | Calouros do Ar | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 8 | 43 (0) | 154 | 0 | 1 / 1 | Gentilândia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 7 | 48 (0) | 154 | 0 | 2 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF | 8 | 90 (0) | 285 | 0 | 2 / 2 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF | 8 | 88 (0) | 279 | 0 | 2 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 8 | 85 (0) | 240 | 0 | 3 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF + ogol | 8 | 91 (87) | 267 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF | 8 | 88 (0) | 371 | 0 | 4 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF | 8 | 71 (0) | 237 | 0 | 4 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF | 8 | 85 (0) | 275 | 0 | 4 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF | 7 | 72 (0) | 222 | 0 | 2 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF | 6 | 60 (0) | 151 | 0 | 2 / 0 | América-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF | 6 | 63 (0) | 149 | 0 | 2 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF | 8 | 56 (0) | 140 | 0 | 2 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF | 8 | 84 (0) | 253 | 0 | 4 / 0 | Fortaleza | RSSSF (classificação geral publicada) |
| 1970 | RSSSF | 8 | 87 (0) | 264 | 0 | 4 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF | 8 | 89 (0) | 279 | 0 | 2 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 9 | 109 (0) | 289 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 11 | 124 (0) | 299 | 0 | 2 / 3 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF | 11 | 94 (0) | 272 | 0 | 3 / 2 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 11 | 78 (0) | 189 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF | 10 | 133 (0) | 358 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 10 | 177 (0) | 433 | 0 | 3 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 10 | 144 (0) | 332 | 0 | 2 / 2 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 10 | 209 (0) | 556 | 0 | 1 / 4 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF | 10 | 184 (0) | 493 | 0 | 1 / 5 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF | 9 | 160 (0) | 438 | 0 | 1 / 5 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF | 10 | 168 (0) | 439 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF | 10 | 162 (0) | 387 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 10 | 122 (0) | 293 | 0 | 1 / 3 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 10 | 172 (0) | 336 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 10 | 120 (0) | 359 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF | 10 | 136 (0) | 332 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 10 | 149 (0) | 308 | 0 | 2 / 4 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 10 | 130 (0) | 295 | 0 | 1 / 3 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF | 10 | 98 (0) | 230 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF | 10 | 211 (0) | 406 | 0 | 7 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF | 10 | 112 (0) | 279 | 0 | 11 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF | 10 | 132 (0) | 365 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 11 | 169 (168) | 410 | 0 | 2 / 6 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 12 | 133 (0) | 337 | 0 | 0 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 16 | 187 (0) | 550 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 16 | 266 (0) | 785 | 0 | 0 / 4 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF | 11 | 75 (0) | 248 | 0 | 3 / 4 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF | 10 | 167 (0) | 489 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF | 10 | 132 (0) | 340 | 0 | 3 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 10 | 102 (102) | 317 | 0 | 2 / 3 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 10 | 152 (151) | 492 | 476 | 0 / 6 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 10 | 96 (95) | 300 | 7 | 2 / 1 | Fortaleza | RSSSF (classificação geral publicada) |
| 2004 | RSSSF + ogol | 10 | 102 (102) | 312 | 285 | 2 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 10 | 102 (102) | 303 | 268 | 2 / 1 | Fortaleza | RSSSF (classificação geral publicada) |
| 2006 | RSSSF + ogol | 10 | 96 (96) | 313 | 0 | 1 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 10 | 96 (96) | 323 | 0 | 2 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 10 | 104 (104) | 334 | 0 | 2 / 3 | Fortaleza | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 10 | 105 (105) | 315 | 5 | 2 / 2 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 12 | 142 (142) | 432 | 0 | 1 / 4 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 12 | 140 (140) | 455 | 0 | 2 / 3 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 12 | 138 (140) | 407 | 0 | 0 / 2 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 11 | 134 (134) | 358 | 151 | 1 / 2 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 11 | 108 (108) | 319 | 319 | 2 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 10 | 76 (76) | 222 | 222 | 7 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 10 | 76 (76) | 186 | 185 | 10 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 10 | 61 (62) | 163 | 158 | 8 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 10 | 66 (66) | 192 | 0 | 1 / 1 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 10 | 62 (62) | 146 | 144 | 5 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 10 | 61 (60) | 140 | 112 | 1 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 10 | 59 (59) | 181 | 181 | 5 / 0 | Fortaleza | RSSSF (classificação geral publicada) |
| 2022 | RSSSF + ogol | 10 | 65 (66) | 152 | 140 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 11 | 47 (47) | 132 | 62 | 1 / 1 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 10 | 47 (47) | 116 | 105 | 6 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | ogol | 10 | 42 (42) | 117 | 0 | 0 / 0 | Ceará | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 10 | 43 (43) | 94 | 0 | 0 / 0 | Fortaleza | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1915

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Stela
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Stela — clube que o ogol não tem; entra só pela RSSSF

### 1916

- sem ocorrências

### 1917

- sem ocorrências

### 1918

- sem ocorrências

### 1919

- sem ocorrências

### 1920

- tabela publicada x jogos — Segunda fase / -: Guarany de Fortaleza tabela [6, 4, 0, 2, 6, 5] jogos [5, 3, 0, 2, 6, 5] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / -: Bangu-CE tabela [6, 0, 2, 4, 5, 8] jogos [5, 0, 2, 3, 5, 8] — a tabela conta 6 jogos e as fontes trazem 5
- mando invertido no ogol — RSSSF Guarany de Fortaleza 1-0 Ceará, ogol Ceará 0-1 Guarany de Fortaleza (1920-09-19); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu-CE 2-3 Fortaleza, ogol Fortaleza 3-2 Bangu-CE (1920-09-26); fica a RSSSF
- mando invertido no ogol — RSSSF Fortaleza 0-3 Guarany de Fortaleza, ogol Guarany de Fortaleza 3-0 Fortaleza (1920-10-10); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu-CE 0-1 Guarany de Fortaleza, ogol Guarany de Fortaleza 1-0 Bangu-CE (1920-10-17); fica a RSSSF
- mando invertido no ogol — RSSSF Ceará 1-3 Fortaleza, ogol Fortaleza 3-1 Ceará (1920-10-24); fica a RSSSF
- mando invertido no ogol — RSSSF Bangu-CE 1-1 Ceará, ogol Ceará 1-1 Bangu-CE (1920-11-21); fica a RSSSF
- jogo só no ogol, incluído em Second Stage: Ceará 0-0 Fortaleza (1920-10-28)
- jogo só no ogol, incluído em Second Stage: Bangu-CE 0-1 Guarany de Fortaleza (1920-11-07)
- só na RSSSF (não achado no ogol): Fortaleza 2-0 Guarany de Fortaleza (1920-12-12)
- vice pela Wikipédia (sem final de dois clubes): Guarany de Fortaleza

### 1921

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bangu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Bangu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bangu-CE)
- Botafogo — clube que o ogol não tem; entra só pela RSSSF
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Guarany de Fortaleza

### 1922

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Botafogo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo-CE)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1923

- tabela publicada x jogos — Segunda fase / -: Ceará tabela [9, 4, 3, 2, 16, 11] jogos [9, 4, 3, 2, 19, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Flamengo-CE tabela [6, 1, 1, 4, 5, 18] jogos [6, 0, 1, 5, 5, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Humaytá tabela [6, 1, 0, 5, 4, 20] jogos [6, 0, 1, 5, 4, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Botafogo-CE tabela [6, 0, 0, 6, 7, 14] jogos [5, 1, 1, 3, 7, 17] — a tabela conta 6 jogos e as fontes trazem 5
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cutuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Humaytá
- Botafogo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo-CE)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Cutuba — clube que o ogol não tem; entra só pela RSSSF
- Flamengo — clube que o ogol não tem; entra só pela RSSSF
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Humaytá — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): América-CE

### 1924

- sem ocorrências

### 1925

- sem ocorrências

### 1926

- sem ocorrências

### 1927

- sem ocorrências

### 1928

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fluminense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fluminense — clube que o ogol não tem; entra só pela RSSSF
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Maguari — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Maguari

### 1929

- sem ocorrências

### 1930

- sem ocorrências

### 1931

- sem ocorrências

### 1932

- sem ocorrências

### 1933

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sam Christovam
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Sam Christovam — clube que o ogol não tem; entra só pela RSSSF

### 1934

- sem ocorrências

### 1935

- sem ocorrências

### 1936

- sem ocorrências

### 1937

- sem ocorrências

### 1938

- sem ocorrências

### 1939

- tabela publicada x jogos — 2º Turno / -: Ceará tabela [11, 9, 2, 0, 38, 16] jogos [10, 8, 2, 0, 32, 15] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Maguari tabela [11, 4, 2, 5, 31, 32] jogos [10, 3, 2, 5, 26, 30] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — 2º Turno / -: Fortaleza tabela [10, 3, 2, 5, 23, 32] jogos [10, 3, 2, 5, 22, 32] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Tramways tabela [11, 2, 2, 7, 24, 47] jogos [9, 2, 2, 5, 21, 36] — a tabela conta 11 jogos e as fontes trazem 9
- jogo anulado ou cancelado fica de fora: Ceará 2-1 Tramways (1939-09-24) [jogo anulado]
- jogo anulado ou cancelado fica de fora: Tramways 2-1 Maguari (1939-10-08) [jogo anulado]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela do Mar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Estrela do Mar — clube que o ogol não tem; entra só pela RSSSF
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Tramways — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Estrela do Mar-CE

### 1940

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1941

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tramways
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Tramways — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tramways)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1942

- tabela publicada x jogos — Fase única / -: Maguari tabela [14, 7, 0, 7, 39, 31] jogos [13, 6, 0, 7, 39, 31] — a tabela conta 14 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: América-CE tabela [12, 5, 0, 7, 21, 40] jogos [12, 4, 0, 8, 21, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Penarol-CE tabela [13, 3, 3, 7, 22, 49] jogos [12, 3, 3, 6, 22, 49] — a tabela conta 13 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Fortaleza tabela [14, 1, 3, 10, 21, 40] jogos [14, 2, 3, 9, 21, 40] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1943

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1945

- tabela publicada x jogos — 1º Turno / -: Flamengo-CE tabela [4, 1, 1, 2, 5, 9] jogos [3, 0, 1, 2, 5, 9] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 1º Turno / -: Luso tabela [3, 0, 1, 2, 1, 3] jogos [2, 0, 1, 1, 1, 3] — a tabela conta 3 jogos e as fontes trazem 2
- tabela publicada x jogos — 2º Turno / -: Ferroviário-CE tabela [4, 3, 0, 1, 7, 5] jogos [3, 2, 0, 1, 7, 5] — a tabela conta 4 jogos e as fontes trazem 3
- tabela publicada x jogos — 2º Turno / -: Fortaleza tabela [4, 2, 0, 2, 10, 6] jogos [3, 2, 0, 1, 10, 6] — a tabela conta 4 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)

### 1946

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Luso
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Flamengo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Flamengo-CE)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Luso — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1947

- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [10, 5, 5, 0, 39, 16] jogos [10, 6, 4, 0, 39, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [10, 6, 1, 3, 25, 15] jogos [10, 5, 2, 3, 25, 15] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1948

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)

### 1949

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Ferroviário-CE x Fortaleza na Tie-Break Matches: sempre na mesma ordem) — ogol Fortaleza 1-1 Ferroviário-CE (1950-03-12)
- placar diferente no ogol — Ceará x Penarol-CE (1949-03-20): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- adversário diferente no ogol — RSSSF Ferroviário-CE 1-0 Ceará, ogol Ferroviário-CE 1-0 América-CE (1949-07-24); fica a RSSSF
- campeão pela lista oficial, Fortaleza; o 1º pela soma dos jogos da última fase é Ferroviário-CE (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1950

- tabela publicada x jogos — Fase única / -: Ferroviário-CE tabela [10, 8, 0, 2, 20, 5] jogos [12, 10, 0, 2, 24, 6] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Fortaleza tabela [10, 6, 1, 3, 21, 16] jogos [12, 7, 2, 3, 23, 16] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Ceará tabela [10, 5, 2, 3, 21, 16] jogos [12, 6, 2, 4, 28, 19] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Gentilândia tabela [10, 3, 2, 5, 18, 23] jogos [12, 4, 3, 5, 22, 26] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: América-CE tabela [10, 2, 4, 4, 20, 25] jogos [12, 3, 5, 4, 25, 29] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: Nacional-CE tabela [10, 1, 1, 8, 15, 30] jogos [12, 3, 1, 8, 21, 32] — a tabela conta 10 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Porangaba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Volante
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Porangaba — clube que o ogol não tem; entra só pela RSSSF
- Volante — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1951

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)

### 1953

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)

### 1954

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)

### 1956

- tabela publicada x jogos — Primeira fase / -: América-CE tabela [7, 3, 2, 2, 24, 12] jogos [7, 4, 2, 1, 24, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Gentilândia tabela [7, 3, 1, 3, 11, 18] jogos [7, 2, 1, 4, 11, 18] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- vice pela Wikipédia (sem final de dois clubes): Usina Ceará

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1958

- tabela publicada x jogos — 2º Turno / -: Ferroviário-CE tabela [7, 5, 2, 0, 19, 9] jogos [7, 4, 2, 1, 19, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Fortaleza tabela [7, 3, 1, 3, 15, 13] jogos [7, 4, 1, 2, 15, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Fortaleza tabela [7, 5, 2, 0, 16, 9] jogos [7, 4, 3, 0, 16, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Gentilândia tabela [7, 3, 0, 4, 13, 12] jogos [7, 3, 1, 3, 13, 12] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1959

- tabela publicada x jogos — 3º Turno / -: Fortaleza tabela [7, 5, 1, 1, 12, 6] jogos [7, 4, 2, 1, 12, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Nacional-CE tabela [7, 2, 0, 5, 6, 16] jogos [7, 2, 1, 4, 6, 16] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)

### 1960

- tabela publicada x jogos — 1º Turno / -: Fortaleza tabela [7, 5, 2, 0, 13, 5] jogos [7, 4, 3, 0, 13, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Nacional-CE tabela [7, 0, 0, 7, 7, 20] jogos [7, 0, 1, 6, 7, 20] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)

### 1961

- placar diferente no ogol — Ceará x Fortaleza (1961-10-22): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Fortaleza x Nacional-CE (1961-07-02): RSSSF 4-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Fortaleza x América-CE (1961-10-07): RSSSF 4-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Usina Ceará x Gentilândia (1961-11-18): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Ceará x Ferroviário-CE (1961-11-19): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Ceará x Fortaleza, ogol 1961-10-22); fica a do ogol
- jogo só no ogol, incluído em 1. Turno: Calouros do Ar 1-0 Usina Ceará (1961-04-16)
- jogo só no ogol, incluído em 1. Turno: Usina Ceará 1-0 Calouros do Ar (1961-04-17)
- jogo só no ogol, incluído em Final: Ceará 1-0 Usina Ceará (1961-06-11)
- só na RSSSF (não achado no ogol): Calouros do Ar 1-0 Usina Ceará (1961-10-11)
- só na RSSSF (não achado no ogol): Ceará 0-0 Fortaleza (1961-10-22)
- só na RSSSF (não achado no ogol): Usina Ceará 1-0 Calouros do Ar (1961-12-17)
- só na RSSSF (não achado no ogol): Ceará 1-0 Usina Ceará (1962-01-14)

### 1962

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- vice pela Wikipédia (sem final de dois clubes): Usina Ceará

### 1963

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1964

- tabela publicada x jogos — Fase final / -: Ceará tabela [14, 10, 1, 3, 45, 18] jogos [16, 10, 2, 4, 48, 24] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase final / -: América-CE tabela [14, 7, 3, 4, 38, 14] jogos [16, 8, 4, 4, 44, 17] — a tabela conta 14 jogos e as fontes trazem 16
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Usina Ceará
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- Usina Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Usina Ceará)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1965

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gentilândia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Gentilândia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Gentilândia)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1966

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional-CE
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Nacional-CE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-CE)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1967

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)

### 1968

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Messejana
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Messejana — clube que o ogol não tem; entra só pela RSSSF
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1969

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1970

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1971

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)

### 1972

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1973

- tabela publicada x jogos — 1º Turno / -: Fortaleza tabela [10, 6, 3, 1, 23, 4] jogos [11, 6, 4, 1, 23, 4] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Calouros do Ar tabela [10, 1, 4, 5, 5, 11] jogos [11, 1, 5, 5, 5, 11] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno - Fase final / -: Fortaleza tabela [3, 2, 1, 0, 4, 2] jogos [4, 2, 2, 0, 4, 2] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno - Fase final / -: Ceará tabela [3, 2, 1, 0, 3, 1] jogos [4, 2, 2, 0, 3, 1] — a tabela conta 3 jogos e as fontes trazem 4
- tabela publicada x jogos — partida extra - desempate do 2º turno / -: Fortaleza tabela [27, 18, 8, 1, 58, 9] jogos [28, 18, 9, 1, 57, 9] — a tabela conta 27 jogos e as fontes trazem 28
- tabela publicada x jogos — partida extra - desempate do 2º turno / -: Ceará tabela [27, 18, 5, 4, 53, 15] jogos [27, 18, 5, 4, 53, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — partida extra - desempate do 2º turno / -: Calouros do Ar tabela [20, 4, 7, 9, 21, 35] jogos [21, 4, 8, 9, 21, 35] — a tabela conta 20 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1974

- tabela publicada x jogos — 2. turno - classificatória / -: Ceará tabela [10, 9, 1, 0, 39, 7] jogos [23, 16, 3, 4, 52, 22] — a tabela conta 10 jogos e as fontes trazem 23
- tabela publicada x jogos — 2. turno - classificatória / -: Fortaleza tabela [10, 8, 1, 1, 36, 6] jogos [24, 17, 4, 3, 61, 20] — a tabela conta 10 jogos e as fontes trazem 24
- tabela publicada x jogos — 2. turno - classificatória / -: Ferroviário-CE tabela [10, 7, 0, 3, 29, 12] jogos [21, 12, 4, 5, 45, 20] — a tabela conta 10 jogos e as fontes trazem 21
- tabela publicada x jogos — 2. turno - classificatória / -: Tiradentes-CE tabela [10, 5, 3, 2, 15, 10] jogos [21, 7, 4, 10, 21, 27] — a tabela conta 10 jogos e as fontes trazem 21
- tabela publicada x jogos — 2. turno - classificatória / -: Icasa tabela [10, 3, 3, 4, 11, 11] jogos [18, 7, 5, 6, 22, 24] — a tabela conta 10 jogos e as fontes trazem 18
- tabela publicada x jogos — 2. turno - classificatória / -: Guarani de Juazeiro tabela [10, 3, 3, 4, 11, 16] jogos [15, 5, 4, 6, 17, 23] — a tabela conta 10 jogos e as fontes trazem 15
- tabela publicada x jogos — 2. turno - classificatória / -: Maguari tabela [10, 4, 0, 6, 13, 21] jogos [12, 3, 3, 6, 13, 15] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — 2. turno - classificatória / -: Calouros do Ar tabela [10, 3, 1, 6, 10, 25] jogos [13, 2, 3, 8, 9, 22] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — 2. turno - classificatória / -: América-CE tabela [10, 2, 1, 7, 10, 26] jogos [14, 1, 3, 10, 13, 44] — a tabela conta 10 jogos e as fontes trazem 14
- tabela publicada x jogos — 2. turno - classificatória / -: Guarany tabela [10, 1, 3, 6, 9, 30] jogos [14, 3, 2, 9, 15, 34] — a tabela conta 10 jogos e as fontes trazem 14
- tabela publicada x jogos — 2. turno - classificatória / -: Quixadá tabela [10, 1, 2, 7, 8, 27] jogos [13, 2, 3, 8, 4, 21] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — Final / -: Fortaleza tabela [30, 23, 4, 3, 87, 22] jogos [24, 17, 4, 3, 61, 20] — a tabela conta 30 jogos e as fontes trazem 24
- tabela publicada x jogos — Final / -: Ceará tabela [30, 22, 4, 4, 82, 26] jogos [23, 16, 3, 4, 52, 22] — a tabela conta 30 jogos e as fontes trazem 23
- tabela publicada x jogos — Final / -: Ferroviário-CE tabela [28, 16, 4, 8, 60, 30] jogos [21, 12, 4, 5, 45, 20] — a tabela conta 28 jogos e as fontes trazem 21
- tabela publicada x jogos — Final / -: Tiradentes-CE tabela [28, 11, 6, 11, 34, 35] jogos [21, 7, 4, 10, 21, 27] — a tabela conta 28 jogos e as fontes trazem 21
- tabela publicada x jogos — Final / -: Icasa tabela [24, 8, 7, 9, 27, 31] jogos [18, 7, 5, 6, 22, 24] — a tabela conta 24 jogos e as fontes trazem 18
- tabela publicada x jogos — Final / -: Guarani de Juazeiro tabela [24, 8, 7, 9, 27, 36] jogos [15, 5, 4, 6, 17, 23] — a tabela conta 24 jogos e as fontes trazem 15
- tabela publicada x jogos — Final / -: Maguari tabela [20, 6, 3, 11, 21, 29] jogos [12, 3, 3, 6, 13, 15] — a tabela conta 20 jogos e as fontes trazem 12
- tabela publicada x jogos — Final / -: Guarany tabela [20, 4, 5, 11, 22, 49] jogos [14, 3, 2, 9, 15, 34] — a tabela conta 20 jogos e as fontes trazem 14
- tabela publicada x jogos — Final / -: Calouros do Ar tabela [20, 4, 4, 12, 16, 42] jogos [13, 2, 3, 8, 9, 22] — a tabela conta 20 jogos e as fontes trazem 13
- tabela publicada x jogos — Final / -: Quixadá tabela [20, 2, 4, 14, 11, 45] jogos [13, 2, 3, 8, 4, 21] — a tabela conta 20 jogos e as fontes trazem 13
- tabela publicada x jogos — Final / -: América-CE tabela [20, 2, 4, 14, 17, 59] jogos [14, 1, 3, 10, 13, 44] — a tabela conta 20 jogos e as fontes trazem 14
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)

### 1975

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ICASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Maguari
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- ICASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Maguari — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Maguari)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1976

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ICASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- ICASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1977

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1978

- tabela publicada x jogos — Segunda fase / -: Ceará tabela [9, 6, 2, 1, 20, 4] jogos [10, 6, 2, 2, 21, 7] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [9, 6, 2, 1, 22, 8] jogos [10, 6, 3, 1, 22, 8] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [9, 5, 4, 0, 17, 4] jogos [11, 6, 5, 0, 20, 5] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Terceira fase / -: Fortaleza tabela [9, 5, 4, 0, 17, 4] jogos [10, 5, 4, 1, 17, 6] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Terceira fase / -: Tiradentes-CE tabela [9, 1, 4, 4, 8, 14] jogos [8, 1, 4, 3, 8, 12] — a tabela conta 9 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)

### 1979

- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 8, 1, 0, 27, 7] jogos [51, 34, 11, 6, 116, 40] — a tabela conta 9 jogos e as fontes trazem 51
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 6, 3, 0, 26, 10] jogos [52, 36, 11, 5, 113, 43] — a tabela conta 9 jogos e as fontes trazem 52
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 6, 1, 2, 14, 9] jogos [48, 21, 11, 16, 60, 54] — a tabela conta 9 jogos e as fontes trazem 48
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 5, 1, 3, 12, 10] jogos [45, 23, 9, 13, 64, 44] — a tabela conta 9 jogos e as fontes trazem 45
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [9, 4, 2, 3, 9, 8] jogos [36, 9, 11, 16, 29, 49] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 3, 2, 4, 7, 12] jogos [36, 12, 12, 12, 44, 51] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 2, 2, 5, 10, 14] jogos [36, 10, 9, 17, 32, 51] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 2, 0, 7, 14, 20] jogos [42, 9, 8, 25, 49, 69] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [9, 1, 1, 7, 4, 21] jogos [36, 4, 6, 26, 25, 79] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 0, 3, 6, 3, 15] jogos [36, 2, 10, 24, 24, 76] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [15, 10, 5, 0, 41, 16] jogos [52, 36, 11, 5, 113, 43] — a tabela conta 15 jogos e as fontes trazem 52
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [15, 10, 4, 1, 37, 13] jogos [51, 34, 11, 6, 116, 40] — a tabela conta 15 jogos e as fontes trazem 51
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [15, 6, 4, 5, 18, 20] jogos [45, 23, 9, 13, 64, 44] — a tabela conta 15 jogos e as fontes trazem 45
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [15, 6, 3, 6, 19, 23] jogos [48, 21, 11, 16, 60, 54] — a tabela conta 15 jogos e as fontes trazem 48
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 7, 2, 0, 30, 4] jogos [51, 34, 11, 6, 116, 40] — a tabela conta 9 jogos e as fontes trazem 51
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 7, 1, 1, 16, 4] jogos [52, 36, 11, 5, 113, 43] — a tabela conta 9 jogos e as fontes trazem 52
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 4, 3, 2, 15, 11] jogos [42, 9, 8, 25, 49, 69] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 3, 5, 1, 8, 5] jogos [48, 21, 11, 16, 60, 54] — a tabela conta 9 jogos e as fontes trazem 48
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 3, 4, 2, 11, 12] jogos [36, 12, 12, 12, 44, 51] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 4, 1, 4, 15, 7] jogos [45, 23, 9, 13, 64, 44] — a tabela conta 9 jogos e as fontes trazem 45
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 5, 3, 7, 16] jogos [36, 2, 10, 24, 24, 76] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [9, 1, 3, 5, 7, 19] jogos [36, 9, 11, 16, 29, 49] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [9, 0, 4, 5, 7, 23] jogos [36, 4, 6, 26, 25, 79] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 0, 2, 7, 3, 18] jogos [36, 10, 9, 17, 32, 51] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [15, 11, 2, 2, 42, 10] jogos [51, 34, 11, 6, 116, 40] — a tabela conta 15 jogos e as fontes trazem 51
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [15, 11, 2, 2, 27, 11] jogos [52, 36, 11, 5, 113, 43] — a tabela conta 15 jogos e as fontes trazem 52
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [15, 5, 7, 3, 13, 12] jogos [48, 21, 11, 16, 60, 54] — a tabela conta 15 jogos e as fontes trazem 48
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [15, 4, 4, 7, 16, 20] jogos [42, 9, 8, 25, 49, 69] — a tabela conta 15 jogos e as fontes trazem 42
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ICASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- ICASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1980

- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 2, 3, 0, 10, 3] jogos [42, 23, 11, 8, 81, 36] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 1, 1, 5, 2] jogos [46, 27, 11, 8, 84, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 2, 2, 1, 6, 5] jogos [46, 28, 11, 7, 89, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 1, 4, 0, 4, 2] jogos [42, 16, 19, 7, 50, 39] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Tiradentes-CE tabela [5, 0, 2, 3, 4, 8] jogos [37, 14, 8, 15, 57, 54] — a tabela conta 5 jogos e as fontes trazem 37
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 0, 2, 3, 2, 11] jogos [37, 11, 9, 17, 47, 53] — a tabela conta 5 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 7, 2, 0, 23, 6] jogos [46, 27, 11, 8, 84, 30] — a tabela conta 9 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 6, 3, 0, 23, 7] jogos [46, 28, 11, 7, 89, 30] — a tabela conta 9 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 5, 2, 2, 16, 8] jogos [42, 23, 11, 8, 81, 36] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 5, 1, 3, 20, 13] jogos [37, 14, 8, 15, 57, 54] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 4, 3, 2, 11, 8] jogos [42, 16, 19, 7, 50, 39] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 2, 5, 2, 8, 10] jogos [37, 9, 12, 16, 34, 64] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 3, 2, 4, 16, 11] jogos [37, 11, 9, 17, 47, 53] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 3, 5, 4, 14] jogos [27, 3, 9, 15, 16, 45] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [9, 1, 0, 8, 5, 30] jogos [27, 2, 2, 23, 13, 82] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [9, 0, 1, 8, 6, 25] jogos [27, 2, 6, 19, 22, 60] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 2, 0, 10, 2] jogos [46, 27, 11, 8, 84, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 2, 2, 1, 8, 6] jogos [46, 28, 11, 7, 89, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 2, 2, 1, 3, 5] jogos [42, 16, 19, 7, 50, 39] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Tiradentes-CE tabela [5, 2, 1, 2, 4, 7] jogos [37, 14, 8, 15, 57, 54] — a tabela conta 5 jogos e as fontes trazem 37
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 2, 0, 3, 8, 7] jogos [42, 23, 11, 8, 81, 36] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [5, 0, 1, 4, 2, 8] jogos [37, 9, 12, 16, 34, 64] — a tabela conta 5 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 7, 2, 0, 17, 3] jogos [42, 23, 11, 8, 81, 36] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 6, 2, 1, 18, 4] jogos [46, 28, 11, 7, 89, 30] — a tabela conta 9 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 5, 1, 3, 12, 7] jogos [37, 11, 9, 17, 47, 53] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 3, 4, 2, 11, 10] jogos [42, 16, 19, 7, 50, 39] — a tabela conta 9 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 4, 1, 4, 9, 15] jogos [37, 9, 12, 16, 34, 64] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 3, 3, 3, 17, 10] jogos [46, 27, 11, 8, 84, 30] — a tabela conta 9 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 3, 2, 4, 14, 12] jogos [37, 14, 8, 15, 57, 54] — a tabela conta 9 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 5, 3, 4, 8] jogos [27, 3, 9, 15, 16, 45] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [9, 1, 1, 7, 5, 26] jogos [27, 2, 2, 23, 13, 82] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [9, 0, 3, 6, 5, 17] jogos [27, 2, 6, 19, 22, 60] — a tabela conta 9 jogos e as fontes trazem 27
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 4, 0, 1, 13, 1] jogos [46, 28, 11, 7, 89, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 3, 1, 1, 11, 5] jogos [42, 23, 11, 8, 81, 36] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 1, 1, 9, 4] jogos [46, 27, 11, 8, 84, 30] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 1, 3, 1, 10, 12] jogos [42, 16, 19, 7, 50, 39] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [5, 0, 2, 3, 6, 18] jogos [37, 9, 12, 16, 34, 64] — a tabela conta 5 jogos e as fontes trazem 37
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 0, 1, 4, 4, 13] jogos [37, 11, 9, 17, 47, 53] — a tabela conta 5 jogos e as fontes trazem 37
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ICASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- ICASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)

### 1981

- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 1, 1, 11, 4] jogos [46, 30, 12, 4, 92, 32] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 2, 3, 0, 6, 4] jogos [44, 24, 9, 11, 84, 46] — a tabela conta 5 jogos e as fontes trazem 44
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 2, 2, 1, 9, 5] jogos [39, 9, 18, 12, 42, 40] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 2, 1, 2, 6, 6] jogos [39, 12, 8, 19, 43, 60] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 1, 2, 2, 6, 11] jogos [41, 19, 13, 9, 77, 45] — a tabela conta 5 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Tiradentes-CE tabela [5, 0, 1, 4, 3, 11] jogos [39, 15, 10, 14, 49, 52] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [8, 7, 1, 0, 22, 4] jogos [41, 19, 13, 9, 77, 45] — a tabela conta 8 jogos e as fontes trazem 41
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [8, 5, 3, 0, 13, 3] jogos [46, 30, 12, 4, 92, 32] — a tabela conta 8 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [8, 4, 1, 3, 10, 8] jogos [39, 15, 10, 14, 49, 52] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [8, 3, 2, 3, 6, 8] jogos [39, 9, 18, 12, 42, 40] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [8, 3, 1, 4, 15, 14] jogos [44, 24, 9, 11, 84, 46] — a tabela conta 8 jogos e as fontes trazem 44
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [8, 2, 3, 3, 13, 12] jogos [39, 12, 8, 19, 43, 60] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [8, 2, 3, 3, 11, 10] jogos [24, 4, 5, 15, 22, 50] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [8, 0, 4, 4, 5, 17] jogos [24, 4, 6, 14, 18, 39] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [8, 0, 2, 6, 2, 21] jogos [24, 1, 3, 20, 11, 74] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 4, 1, 0, 9, 5] jogos [46, 30, 12, 4, 92, 32] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 4, 0, 1, 9, 3] jogos [44, 24, 9, 11, 84, 46] — a tabela conta 5 jogos e as fontes trazem 44
- tabela publicada x jogos — Segunda fase / -: Tiradentes-CE tabela [5, 1, 2, 2, 6, 7] jogos [39, 15, 10, 14, 49, 52] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 1, 1, 3, 10, 10] jogos [41, 19, 13, 9, 77, 45] — a tabela conta 5 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 1, 1, 3, 3, 7] jogos [39, 12, 8, 19, 43, 60] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 0, 3, 2, 5, 10] jogos [39, 9, 18, 12, 42, 40] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [8, 6, 1, 1, 19, 5] jogos [44, 24, 9, 11, 84, 46] — a tabela conta 8 jogos e as fontes trazem 44
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [8, 5, 3, 0, 21, 5] jogos [46, 30, 12, 4, 92, 32] — a tabela conta 8 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [8, 5, 2, 1, 17, 4] jogos [41, 19, 13, 9, 77, 45] — a tabela conta 8 jogos e as fontes trazem 41
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [8, 4, 3, 1, 15, 9] jogos [39, 15, 10, 14, 49, 52] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [8, 2, 2, 4, 6, 10] jogos [39, 12, 8, 19, 43, 60] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [8, 1, 4, 3, 6, 6] jogos [39, 9, 18, 12, 42, 40] — a tabela conta 8 jogos e as fontes trazem 39
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [8, 2, 1, 5, 6, 14] jogos [24, 4, 6, 14, 18, 39] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [8, 2, 1, 5, 6, 17] jogos [24, 4, 5, 15, 22, 50] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [8, 0, 1, 7, 3, 29] jogos [24, 1, 3, 20, 11, 74] — a tabela conta 8 jogos e as fontes trazem 24
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [5, 3, 1, 1, 15, 6] jogos [44, 24, 9, 11, 84, 46] — a tabela conta 5 jogos e as fontes trazem 44
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 1, 1, 13, 8] jogos [46, 30, 12, 4, 92, 32] — a tabela conta 5 jogos e as fontes trazem 46
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 2, 2, 1, 6, 6] jogos [41, 19, 13, 9, 77, 45] — a tabela conta 5 jogos e as fontes trazem 41
- tabela publicada x jogos — Segunda fase / -: Tiradentes-CE tabela [5, 2, 1, 2, 7, 10] jogos [39, 15, 10, 14, 49, 52] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 1, 3, 1, 6, 5] jogos [39, 9, 18, 12, 42, 40] — a tabela conta 5 jogos e as fontes trazem 39
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 0, 0, 5, 3, 15] jogos [39, 12, 8, 19, 43, 60] — a tabela conta 5 jogos e as fontes trazem 39
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ICASA
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- ICASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1982

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1983

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- campeão pela lista oficial, Fortaleza; o 1º pela soma dos jogos da última fase é Ferroviário-CE (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1984

- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 4, 1, 0, 11, 3] jogos [30, 23, 5, 2, 66, 16] — a tabela conta 5 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 2, 2, 1, 9, 5] jogos [28, 12, 8, 8, 45, 28] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [5, 2, 2, 1, 7, 3] jogos [28, 10, 9, 9, 29, 29] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 1, 2, 2, 2, 4] jogos [28, 16, 6, 6, 50, 27] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 0, 3, 2, 1, 3] jogos [30, 14, 8, 8, 33, 16] — a tabela conta 5 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: América-CE tabela [5, 1, 0, 4, 1, 13] jogos [23, 6, 2, 15, 13, 45] — a tabela conta 5 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [9, 9, 0, 0, 22, 4] jogos [21, 16, 3, 2, 44, 13] — a tabela conta 9 jogos e as fontes trazem 21
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [9, 7, 0, 2, 27, 15] jogos [19, 12, 2, 5, 40, 23] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [9, 6, 1, 2, 15, 5] jogos [21, 10, 5, 6, 26, 13] — a tabela conta 9 jogos e as fontes trazem 21
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [9, 5, 1, 3, 15, 9] jogos [19, 8, 5, 6, 29, 21] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [9, 4, 1, 4, 12, 15] jogos [19, 6, 6, 7, 21, 26] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Quixadá tabela [9, 3, 3, 3, 12, 12] jogos [14, 3, 5, 6, 13, 22] — a tabela conta 9 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: América-CE tabela [9, 1, 1, 7, 5, 19] jogos [14, 2, 1, 11, 6, 32] — a tabela conta 9 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 4, 1, 0, 10, 1] jogos [30, 14, 8, 8, 33, 16] — a tabela conta 5 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [5, 4, 0, 1, 11, 4] jogos [28, 16, 6, 6, 50, 27] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 1, 2, 2, 7, 6] jogos [30, 23, 5, 2, 66, 16] — a tabela conta 5 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: Icasa tabela [5, 1, 2, 2, 5, 7] jogos [28, 12, 8, 8, 45, 28] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [5, 0, 3, 2, 2, 8] jogos [28, 10, 9, 9, 29, 29] — a tabela conta 5 jogos e as fontes trazem 28
- tabela publicada x jogos — Segunda fase / -: Quixadá tabela [5, 0, 2, 3, 1, 10] jogos [23, 4, 10, 9, 16, 28] — a tabela conta 5 jogos e as fontes trazem 23
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1985

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vencedor da final pelos jogos (Ceará) diferente do campeão oficial (Fortaleza); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1986

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)

### 1987

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vencedor da final pelos jogos (Ceará) diferente do campeão oficial (Fortaleza); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1988

- tabela publicada x jogos — Primeira fase / Grupo A: Ferroviário-CE tabela [9, 6, 3, 0, 12, 3] jogos [12, 10, 1, 1, 23, 6] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Ceará tabela [9, 5, 2, 2, 14, 8] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo A: Quixadá tabela [9, 4, 3, 2, 9, 9] jogos [12, 5, 4, 3, 16, 11] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Icasa tabela [9, 2, 1, 6, 6, 10] jogos [12, 3, 0, 9, 11, 24] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: América-CE tabela [9, 1, 2, 6, 3, 17] jogos [12, 0, 3, 9, 2, 22] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Tiradentes-CE tabela [9, 5, 3, 1, 12, 8] jogos [12, 7, 4, 1, 13, 7] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Guarany tabela [9, 5, 1, 3, 10, 5] jogos [12, 7, 2, 3, 11, 4] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Guarani de Juazeiro tabela [9, 3, 3, 3, 9, 6] jogos [12, 2, 4, 6, 6, 10] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Fortaleza tabela [9, 3, 1, 5, 12, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Primeira fase / Grupo B: Calouros do Ar tabela [9, 0, 3, 6, 0, 9] jogos [12, 0, 3, 9, 1, 13] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Ferroviário-CE tabela [9, 6, 1, 2, 8, 3] jogos [12, 10, 1, 1, 23, 6] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Fortaleza tabela [9, 5, 2, 2, 13, 5] jogos [12, 7, 2, 3, 22, 11] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Quixadá tabela [9, 4, 1, 4, 13, 13] jogos [12, 5, 4, 3, 16, 11] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Icasa tabela [9, 1, 3, 5, 7, 17] jogos [12, 3, 0, 9, 11, 24] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: América-CE tabela [9, 1, 2, 6, 5, 10] jogos [12, 0, 3, 9, 2, 22] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Ceará tabela [9, 5, 4, 0, 11, 3] jogos [12, 5, 5, 2, 10, 7] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Tiradentes-CE tabela [9, 5, 3, 1, 11, 5] jogos [12, 7, 4, 1, 13, 7] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Guarany tabela [9, 4, 0, 5, 7, 8] jogos [12, 7, 2, 3, 11, 4] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Guarani de Juazeiro tabela [9, 2, 2, 5, 4, 10] jogos [12, 2, 4, 6, 6, 10] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Calouros do Ar tabela [9, 1, 4, 4, 4, 9] jogos [12, 0, 3, 9, 1, 13] — a tabela conta 9 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Fortaleza

### 1989

- tabela publicada x jogos — Fase única / -: Ceará tabela [9, 6, 3, 0, 25, 2] jogos [34, 20, 9, 5, 64, 18] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase única / -: Fortaleza tabela [9, 6, 2, 1, 16, 4] jogos [29, 11, 13, 5, 34, 19] — a tabela conta 9 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase única / -: Ferroviário-CE tabela [9, 5, 3, 1, 17, 11] jogos [30, 15, 11, 4, 50, 28] — a tabela conta 9 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase única / -: Tiradentes-CE tabela [9, 6, 0, 3, 18, 9] jogos [30, 14, 5, 11, 45, 30] — a tabela conta 9 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase única / -: Guarany tabela [9, 3, 4, 2, 9, 4] jogos [26, 11, 9, 6, 23, 12] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Quixadá tabela [9, 3, 1, 5, 10, 14] jogos [25, 5, 6, 14, 19, 41] — a tabela conta 9 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Calouros do Ar tabela [9, 2, 2, 5, 6, 13] jogos [25, 7, 5, 13, 15, 32] — a tabela conta 9 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Icasa tabela [9, 2, 2, 5, 9, 18] jogos [18, 2, 6, 10, 15, 33] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase única / -: Guarani de Juazeiro tabela [9, 1, 2, 6, 7, 24] jogos [25, 4, 7, 14, 18, 47] — a tabela conta 9 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: América-CE tabela [9, 1, 1, 7, 6, 24] jogos [18, 4, 3, 11, 12, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase única / -: Guarany tabela [7, 4, 3, 0, 6, 1] jogos [26, 11, 9, 6, 23, 12] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Ferroviário-CE tabela [7, 3, 4, 0, 11, 5] jogos [30, 15, 11, 4, 50, 28] — a tabela conta 7 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase única / -: Ceará tabela [7, 3, 2, 2, 13, 8] jogos [34, 20, 9, 5, 64, 18] — a tabela conta 7 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase única / -: Tiradentes-CE tabela [7, 3, 1, 3, 7, 6] jogos [30, 14, 5, 11, 45, 30] — a tabela conta 7 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase única / -: Fortaleza tabela [7, 1, 5, 1, 7, 6] jogos [29, 11, 13, 5, 34, 19] — a tabela conta 7 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase única / -: Calouros do Ar tabela [7, 2, 1, 4, 4, 11] jogos [25, 7, 5, 13, 15, 32] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Quixadá tabela [7, 1, 3, 3, 6, 13] jogos [25, 5, 6, 14, 19, 41] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Guarani de Juazeiro tabela [7, 1, 1, 5, 3, 7] jogos [25, 4, 7, 14, 18, 47] — a tabela conta 7 jogos e as fontes trazem 25
- tabela publicada x jogos — Fase única / -: Ceará tabela [34, 20, 9, 5, 65, 19] jogos [34, 20, 9, 5, 64, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Ferroviário-CE tabela [30, 15, 11, 4, 51, 29] jogos [30, 15, 11, 4, 50, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Quixadá tabela [25, 5, 7, 13, 19, 41] jogos [25, 5, 6, 14, 19, 41] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 1990

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vencedor da final pelos jogos (Fortaleza) diferente do campeão oficial (Ceará); fica o oficial

### 1991

- tabela publicada x jogos — 1º Turno / -: Guarany tabela [9, 3, 1, 5, 8, 12] jogos [9, 4, 1, 4, 9, 11] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Quixadá tabela [9, 1, 5, 3, 2, 2] jogos [9, 1, 5, 3, 2, 3] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vencedor da final pelos jogos (Ceará) diferente do campeão oficial (Fortaleza); fica o oficial

### 1992

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Fortaleza

### 1993

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- vice pela Wikipédia (sem final de dois clubes): Icasa

### 1994

- tabela publicada x jogos — Primeira fase / -: Icasa tabela [10, 4, 5, 1, 10, 5] jogos [10, 4, 5, 1, 11, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [10, 4, 5, 1, 9, 4] jogos [10, 4, 5, 1, 10, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [10, 7, 3, 0, 31, 3] jogos [38, 22, 13, 3, 86, 24] — a tabela conta 10 jogos e as fontes trazem 38
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [10, 6, 4, 0, 20, 6] jogos [36, 15, 14, 7, 50, 26] — a tabela conta 10 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [10, 4, 4, 2, 10, 13] jogos [34, 13, 12, 9, 46, 39] — a tabela conta 10 jogos e as fontes trazem 34
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [10, 4, 1, 5, 13, 14] jogos [29, 8, 9, 12, 29, 31] — a tabela conta 10 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [10, 2, 0, 8, 6, 14] jogos [20, 5, 9, 6, 16, 19] — a tabela conta 10 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [10, 1, 2, 7, 2, 13] jogos [29, 1, 6, 22, 14, 70] — a tabela conta 10 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [10, 4, 4, 2, 14, 12] jogos [12, 4, 5, 3, 15, 14] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [10, 3, 3, 4, 15, 14] jogos [10, 3, 3, 4, 15, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [10, 3, 3, 4, 6, 14] jogos [10, 2, 4, 4, 6, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [10, 2, 1, 7, 3, 28] jogos [10, 1, 2, 7, 2, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 5, 3, 1, 19, 7] jogos [38, 22, 13, 3, 86, 24] — a tabela conta 9 jogos e as fontes trazem 38
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 5, 2, 2, 19, 7] jogos [34, 14, 13, 7, 47, 28] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 5, 2, 2, 13, 6] jogos [36, 15, 14, 7, 50, 26] — a tabela conta 9 jogos e as fontes trazem 36
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 4, 4, 1, 20, 4] jogos [34, 13, 12, 9, 46, 39] — a tabela conta 9 jogos e as fontes trazem 34
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 4, 3, 2, 19, 11] jogos [30, 14, 10, 6, 57, 33] — a tabela conta 9 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 5, 0, 4, 12, 7] jogos [29, 8, 9, 12, 29, 31] — a tabela conta 9 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 4, 1, 4, 9, 11] jogos [29, 10, 9, 10, 32, 35] — a tabela conta 9 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 2, 2, 5, 4, 10] jogos [30, 8, 11, 11, 22, 31] — a tabela conta 9 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [9, 1, 1, 7, 2, 27] jogos [29, 3, 6, 20, 11, 74] — a tabela conta 9 jogos e as fontes trazem 29
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [9, 1, 0, 8, 4, 31] jogos [29, 1, 6, 22, 14, 70] — a tabela conta 9 jogos e as fontes trazem 29
- tabela publicada x jogos — Fase final / -: Ferroviário-CE tabela [37, 21, 13, 3, 81, 24] jogos [38, 22, 13, 3, 86, 24] — a tabela conta 37 jogos e as fontes trazem 38
- tabela publicada x jogos — Fase final / -: Ceará tabela [36, 16, 13, 7, 51, 26] jogos [36, 15, 14, 7, 50, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Guarany tabela [34, 15, 12, 7, 48, 28] jogos [34, 14, 13, 7, 47, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Itapipoca tabela [33, 12, 13, 8, 45, 34] jogos [34, 13, 12, 9, 46, 39] — a tabela conta 33 jogos e as fontes trazem 34
- tabela publicada x jogos — Fase final / -: Quixadá tabela [29, 9, 8, 12, 30, 31] jogos [29, 8, 9, 12, 29, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Guarani de Juazeiro tabela [20, 5, 4, 11, 16, 24] jogos [20, 5, 9, 6, 16, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Calouros do Ar tabela [29, 4, 5, 20, 12, 74] jogos [29, 3, 6, 20, 11, 74] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: América-CE tabela [29, 2, 5, 22, 15, 70] jogos [29, 1, 6, 22, 14, 70] — há jogo do clube sem conferência no ogol
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Ferroviário-CE x Ceará na Finals sempre na mesma ordem) — ogol Ceará 0-2 Ferroviário-CE (1994-11-27)
- placar corrigido pelo ogol — Ferroviário-CE x América-CE (1994-06-30): RSSSF 3-0, ogol 2-0; fica o do ogol, que fecha com a tabela publicada
- placar diferente no ogol — Ferroviário-CE x Itapipoca (1994-09-01): RSSSF 5-0, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Ferroviário-CE x Itapipoca, ogol 1994-09-01); fica a do ogol
- jogo só no ogol, incluído em Finals: Calouros do Ar 0-0 Guarani de Juazeiro (1994-06-25)
- jogo só no ogol, incluído em Finals: Calouros do Ar 0-4 Ceará (1994-06-30)
- jogo só no ogol, incluído em Finals: Guarani de Juazeiro 0-0 Quixadá (1994-07-02)
- jogo só no ogol, incluído em Finals: Guarany 0-0 Guarani de Juazeiro (1994-07-06)
- jogo só no ogol, incluído em Finals: Guarani de Juazeiro 0-0 Ceará (1994-07-12)
- jogo só no ogol, incluído em Finals: Guarani de Juazeiro 0-0 Icasa (1994-07-20)
- jogo só no ogol, incluído em Finals: Ferroviário-CE 5-0 Fortaleza (1994-07-24)
- jogo só no ogol, incluído em Finals: América-CE 0-0 Calouros do Ar (1994-07-24)
- jogo só no ogol, incluído em Finals: Itapipoca 1-0 Calouros do Ar (1994-07-27)
- jogo só no ogol, incluído em First Phase (top 4 qualify for semifinals): Quixadá 1-0 Ceará (1994-10-02)
- jogo só no ogol, incluído em First Phase (top 4 qualify for semifinals): Fortaleza 1-1 Itapipoca (1994-10-02)
- só na RSSSF (não achado no ogol): Ferroviário-CE 1-1 Itapipoca (1994-09-01)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 1995

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapipoca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruburetama
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Itapipoca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itapipoca)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Uruburetama — clube que o ogol não tem; entra só pela RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ferroviário-CE

### 1996

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América-R
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapipoca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruburetama
- América-R — clube que o ogol não tem; entra só pela RSSSF
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Itapipoca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itapipoca)
- Portuguesa — clube que o ogol não tem; entra só pela RSSSF
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Uruburetama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Uruburetama)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 1997

- tabela publicada x jogos — Primeira fase / -: Ceará tabela [15, 13, 2, 0, 41, 4] jogos [15, 13, 2, 0, 40, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Russas tabela [15, 6, 4, 5, 25, 27] jogos [15, 7, 3, 5, 25, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Iguatu 1996 tabela [15, 4, 6, 5, 14, 22] jogos [15, 4, 5, 6, 13, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [15, 4, 3, 8, 11, 18] jogos [15, 4, 3, 8, 11, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [6, 3, 3, 0, 10, 5] jogos [12, 5, 4, 3, 17, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [6, 1, 3, 2, 8, 8] jogos [12, 6, 4, 2, 23, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [6, 1, 3, 2, 6, 10] jogos [12, 2, 3, 7, 9, 20] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [15, 11, 4, 0, 32, 4] jogos [30, 24, 6, 0, 72, 8] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [15, 10, 1, 4, 33, 17] jogos [30, 20, 5, 5, 68, 35] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [15, 8, 6, 1, 23, 12] jogos [30, 12, 9, 9, 34, 29] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [15, 9, 2, 4, 27, 16] jogos [30, 21, 3, 6, 76, 29] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [15, 7, 6, 2, 25, 7] jogos [30, 15, 9, 6, 48, 23] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [15, 7, 5, 3, 26, 17] jogos [30, 14, 6, 10, 41, 31] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Esporte Limoeiro tabela [15, 7, 2, 6, 35, 32] jogos [30, 12, 3, 15, 56, 65] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [15, 6, 4, 5, 18, 19] jogos [30, 10, 11, 9, 39, 38] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Portuguesa-CE tabela [15, 6, 4, 5, 16, 18] jogos [30, 9, 5, 16, 31, 54] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Russas tabela [15, 5, 1, 9, 22, 22] jogos [30, 12, 4, 14, 47, 48] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Uruburetama tabela [15, 4, 4, 7, 21, 25] jogos [30, 9, 6, 15, 40, 57] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Iguatu 1996 tabela [15, 4, 4, 7, 11, 24] jogos [30, 8, 9, 13, 24, 46] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [15, 3, 3, 9, 13, 23] jogos [30, 8, 5, 17, 27, 42] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [15, 2, 3, 10, 18, 36] jogos [30, 6, 4, 20, 41, 72] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: América-CE tabela [15, 2, 3, 10, 16, 42] jogos [30, 4, 6, 20, 37, 83] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [15, 2, 2, 11, 17, 39] jogos [30, 8, 5, 17, 35, 56] — a tabela conta 15 jogos e as fontes trazem 30
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [6, 5, 1, 0, 15, 4] jogos [12, 6, 4, 2, 23, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Fortaleza tabela [6, 2, 1, 3, 7, 8] jogos [12, 5, 4, 3, 17, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [6, 1, 0, 5, 3, 10] jogos [12, 2, 3, 7, 9, 20] — a tabela conta 6 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapipoca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Russas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruburetama
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Itapipoca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itapipoca)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa-CE)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Russas — clube que o ogol não tem; entra só pela RSSSF
- Uruburetama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Uruburetama)

### 1998

- tabela publicada x jogos — Turnos - Fase final / -: Ferroviário-CE tabela [2, 1, 1, 0, 6, 4] jogos [4, 2, 1, 1, 9, 8] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Turnos - Fase final / -: Icasa tabela [2, 0, 0, 2, 3, 6] jogos [4, 1, 0, 3, 8, 8] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [5, 4, 1, 0, 15, 7] jogos [25, 16, 5, 4, 55, 32] — a tabela conta 5 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [5, 4, 1, 0, 8, 3] jogos [21, 9, 4, 8, 32, 27] — a tabela conta 5 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [5, 3, 0, 2, 14, 13] jogos [12, 3, 2, 7, 17, 26] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [5, 2, 1, 2, 14, 9] jogos [18, 10, 3, 5, 43, 20] — a tabela conta 5 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Uruburetama tabela [5, 2, 1, 2, 7, 9] jogos [9, 3, 2, 4, 13, 18] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [5, 3, 1, 1, 14, 10] jogos [14, 7, 2, 5, 25, 26] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [5, 2, 1, 2, 11, 9] jogos [15, 4, 5, 6, 22, 26] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Esporte Limoeiro tabela [5, 1, 2, 2, 3, 6] jogos [15, 6, 3, 6, 19, 21] — a tabela conta 5 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Calouros do Ar tabela [5, 0, 0, 5, 4, 16] jogos [12, 2, 1, 9, 11, 31] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [5, 0, 0, 5, 9, 17] jogos [8, 1, 1, 6, 9, 18] — a tabela conta 5 jogos e as fontes trazem 8
- tabela publicada x jogos — Turnos - Fase final / -: Icasa tabela [2, 1, 0, 1, 5, 2] jogos [4, 1, 0, 3, 8, 8] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Turnos - Fase final / -: Ferroviário-CE tabela [2, 1, 0, 1, 3, 4] jogos [4, 2, 1, 1, 9, 8] — a tabela conta 2 jogos e as fontes trazem 4
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Calouros do Ar
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Icasa
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruburetama
- Calouros do Ar — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Calouros do Ar)
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Icasa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Icasa)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Uruburetama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Uruburetama)

### 1999

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapipoca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uniclinic
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruburetama
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Itapipoca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itapipoca)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Uniclinic — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Cearense)
- Uruburetama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Uruburetama)
- vice pela Wikipédia (sem final de dois clubes): Juazeiro-CE

### 2000

- tabela publicada x jogos — Fase final / -: Fortaleza tabela [23, 17, 3, 3, 43, 20] jogos [23, 17, 3, 3, 44, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Itapipoca tabela [21, 8, 5, 8, 27, 26] jogos [21, 8, 5, 8, 26, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Juazeiro-CE tabela [21, 6, 5, 10, 21, 27] jogos [21, 6, 5, 10, 20, 27] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceará
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Crato
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fortaleza
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itapipoca
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quixadá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uniclinic
- Ceará — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceará)
- Crato — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Crato)
- Fortaleza — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fortaleza)
- Itapipoca — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itapipoca)
- Quixadá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quixadá)
- Uniclinic — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Cearense)
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 2001

- tabela publicada x jogos — Segunda fase / -: Guarany tabela [9, 3, 3, 3, 14, 10] jogos [9, 3, 4, 2, 14, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Juazeiro-CE tabela [9, 3, 1, 5, 11, 19] jogos [9, 2, 2, 5, 11, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [9, 3, 3, 3, 14, 10] jogos [9, 3, 4, 2, 14, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Juazeiro-CE tabela [9, 3, 1, 5, 11, 19] jogos [9, 2, 2, 5, 11, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Fortaleza tabela [18, 14, 2, 2, 39, 19] jogos [26, 19, 4, 3, 62, 28] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Final / -: Ceará tabela [18, 9, 4, 5, 38, 25] jogos [26, 11, 7, 8, 55, 40] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Final / -: Guarany tabela [18, 6, 6, 6, 30, 26] jogos [20, 6, 8, 6, 32, 29] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Itapajé tabela [18, 6, 6, 6, 21, 21] jogos [20, 7, 6, 7, 23, 30] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Atlético Cearense tabela [18, 6, 6, 6, 33, 35] jogos [20, 7, 6, 7, 37, 43] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Ferroviário-CE tabela [18, 6, 5, 7, 26, 30] jogos [20, 6, 5, 9, 27, 35] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Final / -: Juazeiro-CE tabela [18, 5, 5, 8, 18, 29] jogos [18, 4, 6, 8, 18, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Atlético Cearense x Ceará (2001-06-30): RSSSF 1-6, ogol 1-4; fica o da RSSSF
- placar diferente no ogol — Fortaleza x Itapajé (2001-07-01): RSSSF 8-0, ogol 5-0; fica o da RSSSF

### 2002

- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [14, 6, 2, 6, 21, 31] jogos [14, 6, 2, 6, 22, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Boa Viagem tabela [6, 2, 1, 3, 6, 6] jogos [7, 3, 1, 3, 9, 7] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / -: Maranguape tabela [6, 1, 1, 4, 8, 13] jogos [7, 1, 1, 5, 8, 15] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [9, 5, 2, 2, 15, 12] jogos [23, 11, 4, 8, 37, 42] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 3, 4, 2, 20, 16] jogos [23, 9, 6, 8, 38, 31] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 4, 0, 5, 20, 22] jogos [23, 8, 2, 13, 47, 51] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 2, 4, 3, 11, 14] jogos [23, 8, 8, 7, 30, 29] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [9, 2, 4, 3, 15, 22] jogos [23, 10, 7, 6, 40, 38] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Itapajé tabela [9, 1, 5, 3, 11, 14] jogos [23, 6, 9, 8, 27, 30] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 1, 5, 3, 9, 17] jogos [23, 6, 12, 5, 25, 30] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 1, 3, 5, 17, 24] jogos [23, 3, 7, 13, 35, 51] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Terceira fase / -: Ceará tabela [10, 7, 1, 2, 21, 11] jogos [12, 8, 2, 2, 26, 14] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Terceira fase / -: Maranguape tabela [10, 6, 1, 3, 27, 21] jogos [12, 6, 2, 4, 30, 26] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Final / -: Fortaleza tabela [29, 16, 9, 4, 64, 34] jogos [29, 15, 9, 5, 63, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Ceará tabela [31, 14, 13, 4, 55, 32] jogos [31, 16, 11, 4, 58, 33] — placar diverge entre RSSSF e ogol em Limoeiro x Ceará (1-2 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Final / -: Maranguape tabela [41, 18, 9, 14, 78, 76] jogos [42, 17, 10, 15, 78, 79] — a tabela conta 41 jogos e as fontes trazem 42
- tabela publicada x jogos — Final / -: Limoeiro tabela [35, 12, 7, 16, 46, 73] jogos [35, 12, 6, 17, 48, 72] — placar diverge entre RSSSF e ogol em Limoeiro x Ceará (1-2 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Final / -: Itapajé tabela [23, 6, 9, 8, 26, 29] jogos [23, 6, 9, 8, 27, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Boa Viagem x Maranguape (2002-06-02): RSSSF 2-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Limoeiro x Ceará (2002-06-23): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Boa Viagem x Maranguape, ogol 2002-06-02); fica a do ogol
- jogo só no ogol, incluído em Second Phase: Boa Viagem 2-0 Maranguape (2002-04-12)
- jogo só no ogol, incluído em Third Stage: Ceará 4-2 Boa Viagem (2002-07-16)
- só na RSSSF (não achado no ogol): Boa Viagem 0-0 Maranguape (2002-06-02)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 2003

- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 8, 1, 0, 24, 4] jogos [22, 16, 5, 1, 53, 17] — a tabela conta 9 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 5, 1, 3, 13, 8] jogos [20, 9, 4, 7, 33, 26] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 4, 3, 2, 14, 11] jogos [19, 6, 5, 8, 24, 29] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [9, 4, 1, 4, 19, 16] jogos [20, 9, 3, 8, 39, 35] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 3, 3, 3, 13, 12] jogos [20, 8, 6, 6, 31, 27] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 3, 2, 4, 21, 20] jogos [18, 4, 7, 7, 36, 36] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [9, 3, 2, 4, 13, 15] jogos [19, 9, 4, 6, 27, 24] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 2, 2, 5, 9, 16] jogos [18, 3, 6, 9, 17, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapajé tabela [9, 2, 2, 5, 9, 20] jogos [18, 3, 5, 10, 20, 43] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 1, 3, 5, 8, 19] jogos [18, 3, 7, 8, 20, 32] — a tabela conta 9 jogos e as fontes trazem 18
- placar diferente no ogol — Ferroviário-CE x Ceará (2003-01-29): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- só na RSSSF (não achado no ogol): Boa Viagem 2-6 Quixadá (2003-03-19)
- vice pela Wikipédia (sem final de dois clubes): Ferroviário-CE

### 2004

- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [9, 6, 3, 0, 19, 9] jogos [20, 7, 6, 7, 31, 36] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 5, 3, 1, 18, 12] jogos [26, 14, 8, 4, 47, 27] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 4, 3, 2, 17, 14] jogos [20, 6, 8, 6, 31, 35] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 3, 4, 2, 9, 8] jogos [26, 11, 10, 5, 39, 27] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 3, 2, 4, 19, 18] jogos [18, 5, 6, 7, 36, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 2, 4, 3, 13, 13] jogos [18, 4, 7, 7, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 2, 4, 3, 11, 12] jogos [20, 6, 8, 6, 26, 23] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 3, 0, 6, 11, 19] jogos [20, 8, 2, 10, 28, 32] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [9, 2, 0, 7, 10, 20] jogos [18, 3, 4, 11, 25, 38] — a tabela conta 9 jogos e as fontes trazem 18
- placar diferente no ogol — Atlético Cearense x Maranguape (2004-03-17): RSSSF 1-0, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Atlético Cearense x Quixadá (2004-03-04): RSSSF 4-1, ogol 1-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Atlético Cearense x Maranguape, ogol 2004-03-17); fica a do ogol

### 2005

- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 6, 2, 1, 17, 8] jogos [26, 15, 7, 4, 49, 29] — a tabela conta 9 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 6, 1, 2, 16, 9] jogos [21, 9, 4, 8, 32, 30] — a tabela conta 9 jogos e as fontes trazem 21
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 6, 0, 3, 14, 10] jogos [25, 16, 3, 6, 37, 23] — a tabela conta 9 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 5, 0, 4, 15, 15] jogos [20, 9, 2, 9, 31, 37] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 4, 1, 4, 15, 13] jogos [18, 6, 3, 9, 28, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [9, 4, 1, 4, 13, 15] jogos [18, 6, 4, 8, 19, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 3, 2, 4, 15, 14] jogos [20, 9, 4, 7, 37, 30] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 3, 2, 4, 13, 15] jogos [18, 6, 4, 8, 27, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 2, 2, 5, 10, 14] jogos [20, 6, 4, 10, 25, 29] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [9, 0, 1, 8, 9, 24] jogos [18, 1, 3, 14, 18, 40] — a tabela conta 9 jogos e as fontes trazem 18
- placar diferente no ogol — Icasa x Quixadá (2005-02-13): RSSSF 2-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Atlético Cearense x Icasa (2005-03-31): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- vencedor da final pelos jogos (Icasa) diferente do campeão oficial (Fortaleza); fica o oficial

### 2006

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Fortaleza x Atlético Cearense na FIRST STAGE sempre na mesma ordem) — ogol Atlético Cearense 2-2 Fortaleza (2006-02-08)
- placar diferente no ogol — Itapipoca x Atlético Cearense (2006-01-08): RSSSF 1-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Fortaleza x Maranguape (2006-01-12): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Atlético Cearense x Limoeiro (2006-01-28): RSSSF 3-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Maranguape x Quixadá (2006-01-28): RSSSF 3-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Quixadá x Ferroviário-CE (2006-02-22): RSSSF 2-1, ogol 3-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Maranguape x Ferroviário-CE, ogol 2006-01-19); fica a do ogol
- jogo só no ogol, incluído em SEMIFINALS:: Ceará 4-0 Icasa (2006-03-30)

### 2007

- tabela publicada x jogos — Fase final / -: Fortaleza tabela [22, 13, 5, 4, 40, 22] jogos [22, 13, 5, 4, 43, 24] — placar diverge entre RSSSF e ogol em Fortaleza x Itapipoca (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Icasa tabela [22, 12, 6, 4, 44, 25] jogos [22, 12, 6, 4, 50, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ceará tabela [20, 11, 4, 5, 35, 24] jogos [20, 11, 4, 5, 38, 28] — placar diverge entre RSSSF e ogol em Ceará x Guarani de Juazeiro (5-1 x 5-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Itapipoca tabela [20, 10, 4, 6, 37, 29] jogos [20, 10, 5, 5, 37, 29] — placar diverge entre RSSSF e ogol em Fortaleza x Itapipoca (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Itapipoca 2-0 Guarani de Juazeiro, ogol Guarani de Juazeiro 0-2 Itapipoca (2007-03-31); fica a RSSSF
- mando invertido no ogol — RSSSF Fortaleza 2-2 Icasa, ogol Icasa 2-2 Fortaleza (2007-04-29); fica a RSSSF
- mando invertido no ogol — RSSSF Icasa 0-1 Fortaleza, ogol Fortaleza 1-0 Icasa (2007-05-06); fica a RSSSF
- placar diferente no ogol — Ceará x Guarani de Juazeiro (2007-01-18): RSSSF 5-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Fortaleza x Itapipoca (2007-04-22): RSSSF 0-0, ogol 1-0; fica o da RSSSF

### 2008

- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [9, 5, 2, 2, 14, 8] jogos [18, 11, 3, 4, 37, 19] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 5, 2, 2, 14, 12] jogos [18, 8, 5, 5, 26, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 5, 1, 3, 15, 13] jogos [18, 11, 1, 6, 36, 27] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 4, 4, 1, 21, 13] jogos [18, 9, 7, 2, 43, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 4, 2, 3, 17, 16] jogos [18, 5, 5, 8, 26, 37] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 4, 1, 4, 17, 17] jogos [18, 10, 3, 5, 33, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 3, 2, 4, 11, 15] jogos [18, 4, 6, 8, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 2, 5, 2, 11, 11] jogos [18, 2, 11, 5, 16, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 2, 3, 4, 17, 18] jogos [18, 5, 6, 7, 33, 33] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 0, 0, 9, 10, 24] jogos [18, 1, 1, 16, 20, 46] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 6, 2, 1, 16, 8] jogos [18, 10, 3, 5, 33, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [9, 6, 1, 2, 23, 11] jogos [18, 11, 3, 4, 37, 19] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 6, 0, 3, 21, 14] jogos [18, 11, 1, 6, 36, 27] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 5, 3, 1, 22, 11] jogos [18, 9, 7, 2, 43, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 3, 3, 3, 16, 15] jogos [18, 5, 6, 7, 33, 33] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 3, 3, 3, 12, 14] jogos [18, 8, 5, 5, 26, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 3, 5, 9, 21] jogos [18, 5, 5, 8, 26, 37] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 1, 4, 4, 12, 16] jogos [18, 4, 6, 8, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 0, 6, 3, 5, 14] jogos [18, 2, 11, 5, 16, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 1, 1, 7, 10, 22] jogos [18, 1, 1, 16, 20, 46] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 6, 2, 1, 16, 8] jogos [18, 10, 3, 5, 33, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [9, 6, 1, 2, 23, 11] jogos [18, 11, 3, 4, 37, 19] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 6, 0, 3, 21, 14] jogos [18, 11, 1, 6, 36, 27] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 5, 3, 1, 22, 11] jogos [18, 9, 7, 2, 43, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 3, 3, 3, 16, 15] jogos [18, 5, 6, 7, 33, 33] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 3, 3, 3, 12, 14] jogos [18, 8, 5, 5, 26, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 3, 5, 9, 21] jogos [18, 5, 5, 8, 26, 37] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 1, 4, 4, 12, 16] jogos [18, 4, 6, 8, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 0, 6, 3, 5, 14] jogos [18, 2, 11, 5, 16, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 1, 1, 7, 10, 22] jogos [18, 1, 1, 16, 20, 46] — a tabela conta 9 jogos e as fontes trazem 18
- mando invertido no ogol — RSSSF Horizonte 1-3 Fortaleza, ogol Fortaleza 3-1 Horizonte (2008-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Fortaleza 0-1 Horizonte, ogol Horizonte 1-0 Fortaleza (2008-04-27); fica a RSSSF
- placar corrigido pelo ogol — Icasa x Ceará (2008-02-10): RSSSF 0-2, ogol 1-2; fica o do ogol, que fecha com a tabela publicada
- jogo só no ogol, incluído em Stage Semifinals: Horizonte 1-3 Fortaleza (2008-02-11)

### 2009

- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 5, 3, 1, 17, 11] jogos [18, 9, 4, 5, 32, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 5, 3, 1, 17, 14] jogos [18, 9, 6, 3, 33, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [9, 4, 4, 1, 21, 16] jogos [18, 6, 10, 2, 37, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 4, 3, 2, 18, 11] jogos [18, 10, 4, 4, 38, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [9, 4, 3, 2, 17, 12] jogos [18, 4, 7, 7, 26, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 2, 5, 2, 8, 8] jogos [18, 7, 6, 5, 25, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 2, 4, 3, 11, 17] jogos [18, 4, 6, 8, 20, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 2, 2, 5, 10, 14] jogos [18, 6, 4, 8, 26, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 1, 2, 6, 12, 15] jogos [18, 4, 3, 11, 27, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 1, 1, 7, 10, 23] jogos [18, 5, 2, 11, 19, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [9, 6, 1, 2, 20, 11] jogos [18, 10, 4, 4, 38, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [9, 5, 1, 3, 17, 14] jogos [18, 7, 6, 5, 25, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [9, 4, 3, 2, 16, 11] jogos [18, 9, 6, 3, 33, 25] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [9, 4, 2, 3, 16, 16] jogos [18, 6, 4, 8, 26, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [9, 4, 1, 4, 15, 17] jogos [18, 9, 4, 5, 32, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [9, 4, 1, 4, 9, 12] jogos [18, 5, 2, 11, 19, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [9, 2, 6, 1, 16, 10] jogos [18, 6, 10, 2, 37, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [9, 3, 1, 5, 15, 17] jogos [18, 4, 3, 11, 27, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [9, 2, 2, 5, 9, 18] jogos [18, 4, 6, 8, 20, 35] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [9, 0, 4, 5, 9, 16] jogos [18, 4, 7, 7, 26, 28] — a tabela conta 9 jogos e as fontes trazem 18
- jogo só no ogol, incluído em Stage finals:: Ceará 1-0 Ferroviário-CE (2009-02-21)
- vencedor da final pelos jogos (Ceará) diferente do campeão oficial (Fortaleza); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 2010

- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 6, 3, 2, 15, 8] jogos [22, 11, 6, 5, 31, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 5, 6, 0, 16, 11] jogos [22, 11, 9, 2, 39, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 6, 2, 3, 25, 16] jogos [22, 12, 5, 5, 44, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 6, 2, 3, 22, 15] jogos [22, 11, 4, 7, 39, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 6, 1, 4, 17, 17] jogos [22, 7, 7, 8, 29, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 5, 0, 6, 16, 12] jogos [22, 11, 0, 11, 29, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 4, 1, 6, 18, 14] jogos [22, 11, 5, 6, 41, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 4, 1, 6, 19, 29] jogos [22, 7, 3, 12, 27, 52] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 3, 4, 4, 16, 21] jogos [22, 6, 7, 9, 29, 39] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [11, 3, 1, 7, 13, 18] jogos [22, 6, 4, 12, 24, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 2, 4, 5, 17, 26] jogos [22, 6, 4, 12, 34, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [11, 2, 3, 6, 13, 20] jogos [22, 4, 4, 14, 25, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 7, 4, 0, 23, 4] jogos [22, 11, 5, 6, 41, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 6, 3, 2, 23, 12] jogos [22, 11, 9, 2, 39, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 6, 3, 2, 19, 12] jogos [22, 12, 5, 5, 44, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 6, 0, 5, 13, 16] jogos [22, 11, 0, 11, 29, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 5, 3, 3, 16, 15] jogos [22, 11, 6, 5, 31, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 5, 2, 4, 17, 13] jogos [22, 11, 4, 7, 39, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 4, 0, 7, 17, 17] jogos [22, 6, 4, 12, 34, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [11, 3, 3, 5, 11, 15] jogos [22, 6, 4, 12, 24, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 3, 3, 5, 13, 18] jogos [22, 6, 7, 9, 29, 39] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 3, 2, 6, 8, 23] jogos [22, 7, 3, 12, 27, 52] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 1, 6, 4, 12, 16] jogos [22, 7, 7, 8, 29, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [11, 2, 1, 8, 12, 23] jogos [22, 4, 4, 14, 25, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 7, 4, 0, 23, 4] jogos [22, 11, 5, 6, 41, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 6, 3, 2, 23, 12] jogos [22, 11, 9, 2, 39, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 6, 3, 2, 19, 12] jogos [22, 12, 5, 5, 44, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 6, 0, 5, 13, 16] jogos [22, 11, 0, 11, 29, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 5, 3, 3, 16, 15] jogos [22, 11, 6, 5, 31, 23] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 5, 2, 4, 17, 13] jogos [22, 11, 4, 7, 39, 28] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 4, 0, 7, 17, 17] jogos [22, 6, 4, 12, 34, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Maranguape tabela [11, 3, 3, 5, 11, 15] jogos [22, 6, 4, 12, 24, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 3, 3, 5, 13, 18] jogos [22, 6, 7, 9, 29, 39] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 3, 2, 6, 8, 23] jogos [22, 7, 3, 12, 27, 52] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 1, 6, 4, 12, 16] jogos [22, 7, 7, 8, 29, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Boa Viagem tabela [11, 2, 1, 8, 12, 23] jogos [22, 4, 4, 14, 25, 43] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Guarany tabela [26, 12, 11, 3, 47, 31] jogos [28, 12, 11, 5, 49, 43] — a tabela conta 26 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase final / -: Horizonte tabela [24, 12, 6, 6, 47, 32] jogos [26, 14, 6, 6, 59, 34] — a tabela conta 24 jogos e as fontes trazem 26
- placar diferente no ogol — Limoeiro x Crato (2010-01-27): RSSSF 0-3, ogol 0-1; fica o da RSSSF
- vencedor da final pelos jogos (Horizonte) diferente do campeão oficial (Fortaleza); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Ceará

### 2011

- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 9, 2, 0, 22, 7] jogos [22, 17, 2, 3, 49, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 7, 3, 1, 25, 12] jogos [22, 12, 3, 7, 44, 29] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 6, 3, 2, 23, 15] jogos [22, 12, 6, 4, 44, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 5, 2, 4, 20, 17] jogos [22, 11, 4, 7, 48, 37] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 4, 5, 2, 19, 13] jogos [22, 10, 7, 5, 38, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [11, 5, 0, 6, 21, 15] jogos [22, 10, 2, 10, 45, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [11, 4, 1, 6, 9, 12] jogos [22, 8, 4, 10, 30, 35] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 4, 1, 6, 13, 23] jogos [22, 10, 2, 10, 29, 36] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 3, 2, 6, 14, 18] jogos [22, 3, 5, 14, 22, 42] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 2, 3, 6, 13, 20] jogos [22, 6, 3, 13, 33, 46] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 2, 3, 6, 12, 25] jogos [22, 5, 4, 13, 27, 49] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 2, 1, 8, 12, 26] jogos [22, 6, 2, 14, 21, 45] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 8, 0, 3, 27, 11] jogos [22, 17, 2, 3, 49, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 6, 3, 2, 21, 15] jogos [22, 12, 6, 4, 44, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 6, 2, 3, 28, 20] jogos [22, 11, 4, 7, 48, 37] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 6, 2, 3, 19, 17] jogos [22, 10, 7, 5, 38, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 6, 1, 4, 16, 13] jogos [22, 10, 2, 10, 29, 36] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [11, 5, 2, 4, 24, 18] jogos [22, 10, 2, 10, 45, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 5, 0, 6, 19, 17] jogos [22, 12, 3, 7, 44, 29] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [11, 4, 3, 4, 21, 23] jogos [22, 8, 4, 10, 30, 35] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 4, 1, 6, 9, 19] jogos [22, 6, 2, 14, 21, 45] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 4, 0, 7, 20, 26] jogos [22, 6, 3, 13, 33, 46] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 3, 1, 7, 15, 24] jogos [22, 5, 4, 13, 27, 49] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 0, 3, 8, 8, 24] jogos [22, 3, 5, 14, 22, 42] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ceará tabela [11, 8, 0, 3, 27, 11] jogos [22, 17, 2, 3, 49, 18] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [11, 6, 3, 2, 21, 15] jogos [22, 12, 6, 4, 44, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Horizonte tabela [11, 6, 2, 3, 28, 20] jogos [22, 11, 4, 7, 48, 37] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Guarany tabela [11, 6, 2, 3, 19, 17] jogos [22, 10, 7, 5, 38, 30] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Itapipoca tabela [11, 6, 1, 4, 16, 13] jogos [22, 10, 2, 10, 29, 36] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Tiradentes-CE tabela [11, 5, 2, 4, 24, 18] jogos [22, 10, 2, 10, 45, 33] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Fortaleza tabela [11, 5, 0, 6, 19, 17] jogos [22, 12, 3, 7, 44, 29] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Icasa tabela [11, 4, 3, 4, 21, 23] jogos [22, 8, 4, 10, 30, 35] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Ferroviário-CE tabela [11, 4, 1, 6, 9, 19] jogos [22, 6, 2, 14, 21, 45] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Crato tabela [11, 4, 0, 7, 20, 26] jogos [22, 6, 3, 13, 33, 46] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Quixadá tabela [11, 3, 1, 7, 15, 24] jogos [22, 5, 4, 13, 27, 49] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Limoeiro tabela [11, 0, 3, 8, 8, 24] jogos [22, 3, 5, 14, 22, 42] — a tabela conta 11 jogos e as fontes trazem 22
- placar diferente no ogol — Guarany x Crato (2011-03-20): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 10 jogos (ex.: Guarany x Horizonte, ogol 2011-03-31); fica a do ogol
- jogo só no ogol, incluído em Final: Horizonte 2-2 Guarani de Juazeiro (2011-05-11)
- jogo só no ogol, incluído em Final: Guarani de Juazeiro 4-0 Horizonte (2011-05-14)
- vice pela Wikipédia (sem final de dois clubes): Guarani de Juazeiro

### 2012

- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [22, 9, 2, 11, 36, 37] jogos [22, 9, 2, 11, 36, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [22, 9, 2, 11, 36, 37] jogos [22, 9, 2, 11, 36, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: Tiradentes-CE x Icasa, ogol 2012-03-10); fica a do ogol
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Crato 2-4 Horizonte (2012-05-01)
- jogo do torneio à parte no ogol (torneio à parte), fica de fora: Horizonte 5-1 Crato (2012-05-05)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 2013

- tabela publicada x jogos — Segunda fase / -: Guarany tabela [14, 7, 1, 6, 22, 19] jogos [14, 7, 1, 6, 19, 19] — placar diverge entre RSSSF e ogol em Ferroviário-CE x Guarany (1-3 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Segunda fase / -: Horizonte tabela [21, 14, 2, 5, 4, 5] jogos [14, 5, 4, 5, 18, 17] — a tabela conta 21 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Guarani de Juazeiro tabela [14, 3, 0, 11, 13, 31] jogos [14, 3, 0, 11, 13, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Guarany tabela [34, 14, 7, 13, 49, 47] jogos [34, 14, 7, 13, 46, 47] — placar diverge entre RSSSF e ogol em Ferroviário-CE x Guarany (1-3 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: Guarani de Juazeiro tabela [30, 10, 4, 16, 27, 42] jogos [30, 10, 4, 16, 27, 39] — há jogo do clube sem conferência no ogol
- placar diferente no ogol — Ferroviário-CE x Guarany (2013-04-16): RSSSF 1-3, ogol 1-2; fica o da RSSSF
- W.O. do ogol incluído: Guarani de Juazeiro x Guarany (2013-04-07), vitória do Guarany pela tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 2014

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 2015

- tabela publicada x jogos — Primeira fase / Grupo A2: Guarany tabela [6, 4, 2, 0, 13, 8] jogos [14, 7, 3, 4, 18, 19] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / Grupo A2: Itapipoca tabela [6, 2, 2, 2, 14, 15] jogos [14, 4, 3, 7, 18, 26] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / Grupo A2: Horizonte tabela [6, 2, 1, 3, 13, 11] jogos [8, 4, 1, 3, 16, 12] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo A2: São Benedito tabela [6, 0, 3, 3, 9, 15] jogos [8, 0, 3, 5, 10, 18] — a tabela conta 6 jogos e as fontes trazem 8

### 2016

- placar diferente no ogol — Quixadá x Guarany (2016-02-17): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- jogo só no ogol, incluído em Final: Fortaleza 1-0 Atlético Cearense (2016-05-08)

### 2017

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Tiradentes-CE x Horizonte, ogol 2017-02-08); fica a do ogol

### 2018

- tabela publicada x jogos — Primeira fase / -: Atlético Cearense tabela [9, 4, 3, 2, 13, 13] jogos [9, 4, 3, 2, 12, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [9, 2, 0, 7, 12, 21] jogos [9, 2, 0, 7, 12, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em Semifinal: Floresta-CE 1-3 Fortaleza (2018-04-01)
- jogo só no ogol, incluído em Semifinal: Ceará 0-1 Atlético Cearense (2018-04-01)
- jogo só no ogol, incluído em Final: Ceará 2-1 Fortaleza (2018-04-05)
- jogo só no ogol, incluído em Final: Fortaleza 1-2 Ceará (2018-04-08)

### 2019

- sem ocorrências

### 2020

- tabela publicada x jogos — Segunda fase / -: Ferroviário-CE tabela [6, 4, 1, 1, 7, 5] jogos [13, 7, 4, 2, 13, 9] — a tabela conta 6 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Ceará tabela [5, 3, 2, 0, 4, 1] jogos [6, 4, 2, 0, 5, 1] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — Segunda fase / -: Guarany tabela [5, 3, 1, 1, 5, 2] jogos [12, 7, 4, 1, 14, 5] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Atlético Cearense tabela [5, 2, 0, 3, 8, 10] jogos [13, 4, 2, 7, 16, 20] — a tabela conta 5 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Caucaia tabela [5, 1, 0, 4, 4, 7] jogos [12, 2, 5, 5, 13, 15] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Barbalha tabela [5, 1, 0, 4, 6, 12] jogos [12, 5, 2, 5, 17, 15] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Pacajus tabela [6, 1, 0, 5, 5, 12] jogos [13, 2, 4, 7, 9, 18] — a tabela conta 6 jogos e as fontes trazem 13
- jogo só no ogol, incluído em Second Phase: Barbalha 0-5 Ceará (2020-07-13)
- jogo só no ogol, incluído em Second Phase: Caucaia 0-3 Atlético Cearense (2020-07-13)
- jogo só no ogol, incluído em Second Phase: Guarany 0-5 Fortaleza (2020-07-13)
- jogo só no ogol, incluído em Second Phase: Ferroviário-CE 0-0 Caucaia (2020-07-15)
- jogo só no ogol, incluído em Second Phase: Ceará 1-2 Fortaleza (2020-07-16)
- jogo só no ogol, incluído em Second Phase: Barbalha 0-2 Guarany (2020-07-16)
- jogo só no ogol, incluído em Second Phase: Atlético Cearense 2-2 Pacajus (2020-07-16)
- jogo só no ogol, incluído em Semifinal: Fortaleza 1-0 Guarany (2020-07-18)
- jogo só no ogol, incluído em Semifinal: Ceará 1-0 Ferroviário-CE (2020-07-19)
- jogo só no ogol, incluído em Final: Ceará 1-2 Fortaleza (2020-10-01)
- jogo só no ogol, incluído em Final: Fortaleza 1-0 Ceará (2020-10-22)
- só na RSSSF (não achado no ogol): Atlético Cearense 0-1 Ceará (2020-03-08)

### 2021

- placar diferente no ogol — Icasa x Caucaia (2021-05-15): RSSSF 2-3, ogol 3-2; fica o da RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Fortaleza

### 2022

- placar diferente no ogol — Pacajus x Fortaleza (2022-03-02): RSSSF 5-0, ogol 0-5; fica o da RSSSF
- jogo só no ogol, incluído em Semifinais: Iguatu 1-1 Caucaia (2022-03-12)
- jogo só no ogol, incluído em Semifinais: Fortaleza 2-1 Ferroviário-CE (2022-03-12)
- jogo só no ogol, incluído em Final: Caucaia 0-0 Fortaleza (2022-04-23)
- jogo só no ogol, incluído em Final: Fortaleza 4-0 Caucaia (2022-04-24)
- W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: Crato x Ferroviário (2022-02-19)

### 2023

- tabela publicada x jogos — Primeira fase / -: Guarani de Juazeiro tabela [4, 0, 0, 4, 1, 16] jogos [3, 0, 0, 3, 1, 11] — a tabela conta 4 jogos e as fontes trazem 3
- adversário diferente no ogol — RSSSF Guarany 0-5 Ceará, ogol Guarani de Juazeiro 0-5 Ceará (2023-01-15); fica a RSSSF
- jogo só no ogol, incluído em FIRST STAGE:: Guarani de Juazeiro 2-3 Barbalha (2023-02-07)
- jogo só no ogol, incluído em FIRST STAGE:: Caucaia 2-0 Pacajus (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Ceará 2-1 Fortaleza (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético Cearense 1-1 Maracanã (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Iguatu 2-1 Ferroviário-CE (2023-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Barbalha 1-2 Caucaia (2023-02-11)
- jogo só no ogol, incluído em Quartas de final: Ferroviário-CE 2-0 Maracanã (2023-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani de Juazeiro 0-1 Pacajus (2023-02-12)
- jogo só no ogol, incluído em Quartas de final: Atlético Cearense 1-2 Iguatu (2023-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: Caucaia 1-0 Guarani de Juazeiro (2023-02-16)
- jogo só no ogol, incluído em FIRST STAGE:: Pacajus 1-2 Barbalha (2023-02-17)
- jogo só no ogol, incluído em FIRST STAGE:: Pacajus 1-1 Caucaia (2023-02-25)
- jogo só no ogol, incluído em Quartas de final: Maracanã 1-3 Ferroviário-CE (2023-02-25)
- jogo só no ogol, incluído em Quartas de final: Iguatu 1-0 Atlético Cearense (2023-02-25)
- jogo só no ogol, incluído em FIRST STAGE:: Barbalha 0-1 Guarani de Juazeiro (2023-02-26)
- jogo só no ogol, incluído em FIRST STAGE:: Caucaia 0-0 Pacajus (2023-02-28)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani de Juazeiro 1-4 Barbalha (2023-03-02)
- jogo só no ogol, incluído em FIRST STAGE:: Barbalha 1-0 Pacajus (2023-03-05)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani de Juazeiro 1-1 Caucaia (2023-03-06)
- jogo só no ogol, incluído em FIRST STAGE:: Pacajus 7-0 Guarani de Juazeiro (2023-03-10)
- jogo só no ogol, incluído em FIRST STAGE:: Caucaia 2-0 Barbalha (2023-03-10)
- jogo só no ogol, incluído em Semifinal: Iguatu 1-1 Ceará (2023-03-12)
- jogo só no ogol, incluído em Semifinal: Ferroviário-CE 1-1 Fortaleza (2023-03-12)
- jogo só no ogol, incluído em Semifinal: Ceará 2-0 Iguatu (2023-03-18)
- jogo só no ogol, incluído em Semifinal: Fortaleza 4-0 Ferroviário-CE (2023-03-19)
- jogo só no ogol, incluído em Final: Fortaleza 2-1 Ceará (2023-04-01)
- jogo só no ogol, incluído em Final: Ceará 2-2 Fortaleza (2023-04-08)

### 2024

- jogo só no ogol, incluído em FIRST STAGE:: Ceará 6-0 Atlético Cearense (2024-02-01)
- jogo só no ogol, incluído em RELEGATION TOURNAMENT:: Barbalha 2-0 Atlético Cearense (2024-03-08)
- jogo só no ogol, incluído em RELEGATION TOURNAMENT:: Caucaia 0-1 Atlético Cearense (2024-03-15)
- jogo só no ogol, incluído em Final: Fortaleza 0-0 Ceará (2024-03-30)
- jogo só no ogol, incluído em Final: Ceará 1-1 Fortaleza (2024-04-06)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ceará

### 2025

- jogo só no ogol, incluído em Primeira fase / Grupo A: Ceará 2-1 Tirol (2025-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Iguatu 0-1 Maracanã (2025-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Floresta-CE 3-1 Barbalha (2025-01-19)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ferroviário-CE 1-2 Horizonte (2025-01-19)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Barbalha 3-1 Cariri FC (2025-01-23)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Iguatu 1-1 Floresta-CE (2025-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Horizonte 1-3 Fortaleza (2025-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Maracanã 1-1 Tirol (2025-01-26)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ferroviário-CE 1-2 Ceará (2025-01-26)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 7-0 Cariri FC (2025-01-27)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Barbalha 1-1 Horizonte (2025-01-28)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Floresta-CE 3-3 Ferroviário-CE (2025-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ceará 1-0 Iguatu (2025-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Tirol 4-0 Cariri FC (2025-01-30)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 1-0 Maracanã (2025-01-30)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Floresta-CE 0-1 Fortaleza (2025-02-01)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ferroviário-CE 1-0 Maracanã (2025-02-02)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ceará 5-0 Barbalha (2025-02-02)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Cariri FC 1-5 Iguatu (2025-02-03)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Horizonte 0-0 Tirol (2025-02-04)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Maracanã 4-1 Barbalha (2025-02-08)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Iguatu 1-1 Horizonte (2025-02-08)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Cariri FC 0-2 Ferroviário-CE (2025-02-08)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Tirol 2-0 Floresta-CE (2025-02-08)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 1-2 Ceará (2025-02-08)
- jogo só no ogol, incluído em Primeira fase: Barbalha 1-1 Floresta-CE (2025-02-15)
- jogo só no ogol, incluído em Primeira fase: Iguatu 3-0 Cariri FC (2025-02-15)
- jogo só no ogol, incluído em Quartas de final: Ferroviário-CE 2-1 Tirol (2025-02-15)
- jogo só no ogol, incluído em Quartas de final: Horizonte 2-3 Maracanã (2025-02-16)
- jogo só no ogol, incluído em Primeira fase: Floresta-CE 1-0 Iguatu (2025-02-21)
- jogo só no ogol, incluído em Primeira fase: Cariri FC 1-1 Barbalha (2025-02-22)
- jogo só no ogol, incluído em Quartas de final: Tirol 0-3 Ferroviário-CE (2025-02-22)
- jogo só no ogol, incluído em Quartas de final: Maracanã 1-0 Horizonte (2025-02-23)
- jogo só no ogol, incluído em Primeira fase: Floresta-CE 2-1 Cariri FC (2025-02-27)
- jogo só no ogol, incluído em Primeira fase: Iguatu 3-3 Barbalha (2025-02-27)
- jogo só no ogol, incluído em Semifinal: Ferroviário-CE 0-0 Fortaleza (2025-03-01)
- jogo só no ogol, incluído em Semifinal: Maracanã 0-3 Ceará (2025-03-02)
- jogo só no ogol, incluído em Semifinal: Fortaleza 1-0 Ferroviário-CE (2025-03-08)
- jogo só no ogol, incluído em Semifinal: Ceará 4-0 Maracanã (2025-03-09)
- jogo só no ogol, incluído em Final: Fortaleza 0-1 Ceará (2025-03-15)
- jogo só no ogol, incluído em Primeira fase / Grupo 3/4: Maracanã 2-1 Ferroviário-CE (2025-03-15)
- jogo só no ogol, incluído em Final: Ceará 1-1 Fortaleza (2025-03-22)

### 2026

- jogo só no ogol, incluído em Primeira fase / Grupo A: Maracanã 0-1 Ferroviário-CE (2026-01-06)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Tirol 0-2 Floresta-CE (2026-01-07)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Horizonte 0-0 Quixadá (2026-01-07)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Iguatu 2-0 Maranguape (2026-01-08)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Floresta-CE 0-1 Ceará (2026-01-10)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Quixadá 1-0 Maracanã (2026-01-10)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Maranguape 1-0 Tirol (2026-01-11)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ferroviário-CE 0-0 Fortaleza (2026-01-11)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Maracanã 1-2 Horizonte (2026-01-13)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Iguatu 0-0 Tirol (2026-01-14)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Ceará 1-0 Maranguape (2026-01-15)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 4-0 Quixadá (2026-01-15)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Ferroviário-CE 2-2 Horizonte (2026-01-16)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Ceará 1-1 Iguatu (2026-01-17)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Maranguape 0-3 Floresta-CE (2026-01-17)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 1-0 Maracanã (2026-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Tirol 1-4 Ceará (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Floresta-CE 1-1 Iguatu (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Quixadá 1-2 Ferroviário-CE (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Horizonte 0-1 Fortaleza (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Ferroviário-CE 1-5 Ceará (2026-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Fortaleza 1-0 Floresta-CE (2026-01-26)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Iguatu 1-1 Horizonte (2026-01-27)
- jogo só no ogol, incluído em Primeira fase: Maranguape 1-1 Maracanã (2026-01-28)
- jogo só no ogol, incluído em Primeira fase: Quixadá 0-1 Tirol (2026-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Fortaleza 1-1 Iguatu (2026-01-31)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Ceará 4-0 Horizonte (2026-02-01)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Floresta-CE 0-0 Ferroviário-CE (2026-02-02)
- jogo só no ogol, incluído em Primeira fase: Maranguape 3-2 Tirol (2026-02-03)
- jogo só no ogol, incluído em Primeira fase: Maracanã 2-3 Quixadá (2026-02-04)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Ferroviário-CE 2-0 Iguatu (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Horizonte 0-1 Floresta-CE (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo D: Ceará 0-0 Fortaleza (2026-02-08)
- jogo só no ogol, incluído em Primeira fase: Quixadá 1-3 Maranguape (2026-02-09)
- jogo só no ogol, incluído em Primeira fase: Tirol 0-2 Maracanã (2026-02-09)
- jogo só no ogol, incluído em Primeira fase / Grupo 5/6: Iguatu 3-1 Horizonte (2026-02-11)
- jogo só no ogol, incluído em Semifinal: Ferroviário-CE 0-2 Fortaleza (2026-02-14)
- jogo só no ogol, incluído em Semifinal: Floresta-CE 0-3 Ceará (2026-02-15)
- jogo só no ogol, incluído em Semifinal: Fortaleza 2-0 Ferroviário-CE (2026-02-21)
- jogo só no ogol, incluído em Semifinal: Ceará 4-0 Floresta-CE (2026-02-22)
- jogo só no ogol, incluído em Primeira fase / Grupo 3/4: Ferroviário-CE 1-0 Floresta-CE (2026-02-26)
- jogo só no ogol, incluído em Final: Fortaleza 1-1 Ceará (2026-03-01)
- jogo só no ogol, incluído em Final: Ceará 1-1 Fortaleza (2026-03-08)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Fortaleza

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-ce1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
