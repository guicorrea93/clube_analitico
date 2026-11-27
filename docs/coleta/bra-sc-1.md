# Campeonato Catarinense (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-sc-1/importar.py`. Pacote em `data/coleta/bra-sc-1/pacote/`. Mesmo código do Goiano
(`docs/coleta/bra-go-1.md`), com as fontes de Santa Catarina.

**Temporadas:** 1924 a 2026, 102 edições (escopo aprovado pelo Guilherme em 27/11/2026). Fica fora 1946, que não foi
disputado. 1924-1926 e 1934-1936 eram os campeonatos da capital, homologados como estaduais pela FCF. 1933 não terminou
e fica sem campeão. Em 1935 só entra o campeonato da FCD (o da ACD, de Joinville, a FCF não reconhece).

**Fontes:** RSSSF Brasil (`tablessz/sc{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada
edição e o código de cada clube; jogos a partir dos anos 2000); Wikipédia em português (artigo "Campeonato Catarinense
de Futebol Masculino": campeão e vice de cada ano, segunda fonte).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1924 | RSSSF | 10 | 10 (0) | 45 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1926 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1927 | RSSSF | 6 | 5 (0) | 17 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1929 | RSSSF | 2 | 1 (0) | 10 | 0 | 0 / 0 | Caxias-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF | 4 | 3 (0) | 13 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF | 4 | 2 (0) | 8 | 0 | 0 / 0 | Lauro Müller | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 | RSSSF | 4 | 4 (0) | 30 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1934 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1935 | RSSSF | 9 | 9 (0) | 43 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 | RSSSF | 9 | 8 (0) | 44 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF | 6 | 13 (0) | 82 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF | 2 | 1 (0) | 2 | 0 | 0 / 0 | CIP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF | 7 | 6 (0) | 36 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF | 6 | 5 (0) | 12 | 0 | 0 / 0 | Ypiranga-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF | 7 | 7 (0) | 32 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF | 4 | 3 (0) | 14 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1944 | RSSSF | 5 | 8 (0) | 51 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1947 | RSSSF | 4 | 6 (0) | 39 | 0 | 0 / 0 | América-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 4 | 13 (0) | 61 | 0 | 0 / 0 | América-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 6 | 10 (0) | 57 | 0 | 0 / 0 | Olímpico-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF | 4 | 5 (0) | 19 | 0 | 0 / 0 | Carlos Renaux | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF | 8 | 12 (0) | 48 | 0 | 0 / 0 | América-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF | 2 | 2 (0) | 10 | 0 | 0 / 0 | América-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF | 5 | 8 (0) | 49 | 0 | 0 / 0 | Carlos Renaux | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 10 | 14 (0) | 84 | 0 | 0 / 0 | Caxias-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 2 | 3 (0) | 10 | 0 | 0 / 0 | Caxias-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 5 | 4 (0) | 12 | 0 | 0 / 0 | Operário-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 8 | 17 (0) | 68 | 0 | 0 / 0 | Hercílio Luz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF | 6 | 11 (0) | 49 | 0 | 0 / 0 | Hercílio Luz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF | 14 | 30 (0) | 113 | 0 | 0 / 0 | Paula Ramos-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF | 9 | 20 (0) | 66 | 0 | 0 / 0 | Metropol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF | 6 | 13 (0) | 52 | 0 | 0 / 0 | Metropol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF | 13 | 23 (0) | 90 | 0 | 0 / 0 | Metropol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF | 10 | 88 (0) | 328 | 0 | 0 / 0 | Marcílio Dias | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF | 12 | 24 (0) | 74 | 0 | 0 / 0 | Olímpico-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF | 40 | 161 (0) | 571 | 3 | 0 / 0 | Internacional-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF | 25 | 54 (0) | 164 | 0 | 0 / 0 | Perdigão | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF | 9 | 9 (0) | 21 | 0 | 0 / 0 | Metropol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF | 12 | 18 (0) | 44 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF | 13 | 23 (0) | 59 | 0 | 0 / 0 | Metropol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF | 15 | 120 (0) | 322 | 0 | 0 / 0 | Ferroviário-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF | 13 | 147 (0) | 306 | 0 | 0 / 0 | América-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 10 | 102 (0) | 220 | 0 | 1 / 1 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 10 | 134 (0) | 276 | 0 | 2 / 2 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF | 7 | 17 (0) | 35 | 0 | 0 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 13 | 213 (0) | 498 | 0 | 0 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF | 15 | 135 (0) | 282 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 20 | 373 (0) | 839 | 0 | 9 / 5 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 17 | 347 (0) | 671 | 653 | 6 / 12 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 14 | 47 (0) | 100 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF | 11 | 51 (0) | 110 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF | 13 | 125 (0) | 326 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF | 12 | 307 (0) | 676 | 9 | 0 / 1 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1983 | RSSSF | 12 | 188 (0) | 210 | 0 | 0 / 3 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 12 | 217 (0) | 437 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 13 | 354 (0) | 673 | 0 | 0 / 0 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 10 | 166 (0) | 327 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF | 10 | 195 (0) | 404 | 0 | 0 / 1 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 12 | 173 (0) | 372 | 12 | 0 / 2 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 12 | 207 (0) | 374 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF | 12 | 117 (0) | 127 | 0 | 0 / 5 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF | 14 | 332 (0) | 688 | 0 | 7 / 2 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF | 14 | 196 (0) | 389 | 0 | 0 / 0 | Brusque | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF | 14 | 185 (0) | 410 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF | 14 | 263 (0) | 701 | 0 | 4 / 2 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 20 | 290 (0) | 804 | 0 | 6 / 2 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 10 | 105 (0) | 267 | 0 | 2 / 4 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 10 | 108 (0) | 312 | 0 | 1 / 2 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF | 11 | 115 (0) | 282 | 2 | 1 / 3 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF | 12 | 163 (0) | 526 | 0 | 3 / 3 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF | 12 | 138 (0) | 400 | 0 | 2 / 3 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 13 | 162 (104) | 489 | 0 | 1 / 4 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 16 | 126 (90) | 398 | 0 | 1 / 6 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 12 | 66 (66) | 218 | 181 | 1 / 1 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 12 | 72 (72) | 235 | 0 | 2 / 1 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 12 | 90 (90) | 271 | 268 | 4 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 12 | 90 (90) | 289 | 0 | 3 / 1 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 12 | 134 (134) | 433 | 422 | 2 / 1 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 12 | 134 (134) | 477 | 0 | 2 / 3 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 10 | 104 (104) | 325 | 0 | 8 / 0 | Avaí | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 10 | 98 (98) | 309 | 309 | 3 / 3 | Avaí | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 10 | 98 (98) | 315 | 2 | 3 / 3 | Chapecoense | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 10 | 96 (96) | 323 | 0 | 6 / 0 | Avaí | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 10 | 96 (96) | 287 | 7 | 3 / 2 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 10 | 89 (89) | 230 | 0 | 3 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 10 | 89 (89) | 210 | 210 | 3 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 10 | 92 (92) | 246 | 186 | 2 / 2 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 10 | 92 (92) | 251 | 251 | 3 / 0 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 10 | 91 (91) | 212 | 212 | 1 / 0 | Figueirense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 10 | 93 (93) | 200 | 200 | 1 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 10 | 61 (61) | 129 | 129 | 9 / 0 | Chapecoense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 12 | 81 (80) | 179 | 172 | 2 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 12 | 80 (80) | 167 | 48 | 0 / 2 | Brusque | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 12 | 80 (80) | 145 | 0 | 1 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | ogol | 12 | 80 (80) | 203 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 12 | 74 (74) | 158 | 0 | 2 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | RSSSF + ogol | 12 | 70 (70) | 168 | 158 | 4 / 8 | Barra-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1924

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Continental
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Deodoro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Externato
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Florianópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Internato
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sport Catharinense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Trabalhista
- Continental — clube que o ogol não tem; entra só pela RSSSF
- Deodoro — clube que o ogol não tem; entra só pela RSSSF
- Externato — clube que o ogol não tem; entra só pela RSSSF
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Florianópolis — clube que o ogol não tem; entra só pela RSSSF
- Internato — clube que o ogol não tem; entra só pela RSSSF
- Palestra — clube que o ogol não tem; entra só pela RSSSF
- Sport Catharinense — clube que o ogol não tem; entra só pela RSSSF
- Trabalhista — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Trabalhista

### 1925

- sem ocorrências

### 1926

- sem ocorrências

### 1927

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Adolpho Konder
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Externato
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Trabalhista
- Adolpho Konder — clube que o ogol não tem; entra só pela RSSSF
- Externato — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Externato)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Trabalhista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Trabalhista)
- vice pela Wikipédia (sem final de dois clubes): Blumenau

### 1928

- sem ocorrências

### 1929

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Adolpho Konder
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- Adolpho Konder — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Adolpho Konder)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- campeão pela lista oficial, Caxias-SC; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Adolpho Konder

### 1930

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusquense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- Brusquense — clube que o ogol não tem; entra só pela RSSSF
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)

### 1931

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lauro Müller
- Atlético — clube que o ogol não tem; entra só pela RSSSF
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Lauro Müller — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Caxias-SC

### 1932

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bom Retiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- Bom Retiro — clube que o ogol não tem; entra só pela RSSSF
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)

### 1933

- sem ocorrências

### 1934

- sem ocorrências

### 1935

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Combinado de Laguna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iris
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamandaré
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Combinado de Laguna — clube que o ogol não tem; entra só pela RSSSF
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Iris — clube que o ogol não tem; entra só pela RSSSF
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tamandaré — clube que o ogol não tem; entra só pela RSSSF
- vencedor da final pelos jogos (Atlético Catarinense de Florianópolis) diferente do campeão oficial (Figueirense); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Iris

### 1936

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América/MAF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iris
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luiz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamandaré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- América/MAF — clube que o ogol não tem; entra só pela RSSSF
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Iris — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iris)
- São Luiz — clube que o ogol não tem; entra só pela RSSSF
- Tamandaré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tamandaré)
- Ypiranga — clube que o ogol não tem; entra só pela RSSSF
- vencedor da final pelos jogos (Pery Ferroviário) diferente do campeão oficial (Figueirense); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Iris

### 1937

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Iris
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamandaré
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Iris — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Iris)
- Tamandaré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tamandaré)
- vice pela Wikipédia (sem final de dois clubes): Caxias-SC

### 1938

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CIP
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- CIP — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Atlético-SC

### 1939

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pery Ferroviário
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Pery Ferroviário — clube que o ogol não tem; entra só pela RSSSF
- vencedor da final pelos jogos (Hercílio Luz) diferente do campeão oficial (Figueirense); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Pery Ferroviário

### 1940

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pery Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Paysandu — clube que o ogol não tem; entra só pela RSSSF
- Pery Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pery Ferroviário)
- Ypiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ypiranga-SC)

### 1941

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusquense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pery Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- Brusquense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusquense)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Pery Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pery Ferroviário)
- Ypiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ypiranga-SC)
- vice pela Wikipédia (sem final de dois clubes): Caxias-SC

### 1942

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusquense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- América — clube que o ogol não tem; entra só pela RSSSF
- Brusquense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusquense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)

### 1943

- sem ocorrências

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concórdia/RSU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Concórdia/RSU — clube que o ogol não tem; entra só pela RSSSF
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)

### 1945

- sem ocorrências

### 1947

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paula Ramos
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Operário — clube que o ogol não tem; entra só pela RSSSF
- Paula Ramos — clube que o ogol não tem; entra só pela RSSSF

### 1948

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paula Ramos
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Ipiranga — clube que o ogol não tem; entra só pela RSSSF
- Paula Ramos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paula Ramos-SC)
- vice pela Wikipédia (sem final de dois clubes): Paula Ramos-SC

### 1949

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético (SF)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus (PU)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- Atlético (SF) — clube que o ogol não tem; entra só pela RSSSF
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-SC)
- Juventus (PU) — clube que o ogol não tem; entra só pela RSSSF
- Olímpico — clube que o ogol não tem; entra só pela RSSSF

### 1950

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Duque de Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Duque de Caxias — clube que o ogol não tem; entra só pela RSSSF
- Ferroviário — clube que o ogol não tem; entra só pela RSSSF
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- campeão pela lista oficial, Carlos Renaux; o 1º pela soma dos jogos da última fase é Figueirense (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Figueirense

### 1951

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aliados
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Duque de Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estivadores
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- Aliados — clube que o ogol não tem; entra só pela RSSSF
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Cruzeiro — clube que o ogol não tem; entra só pela RSSSF
- Duque de Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Duque de Caxias-SC)
- Estivadores — clube que o ogol não tem; entra só pela RSSSF
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- vice pela Wikipédia (sem final de dois clubes): Carlos Renaux

### 1953

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Grêmio — clube que o ogol não tem; entra só pela RSSSF
- União — clube que o ogol não tem; entra só pela RSSSF

### 1954

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Henrique Lage
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- Baependi — clube que o ogol não tem; entra só pela RSSSF
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Henrique Lage — clube que o ogol não tem; entra só pela RSSSF
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- vice pela Wikipédia (sem final de dois clubes): Blumenau

### 1956

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- vice pela Wikipédia (sem final de dois clubes): Paysandu-SC

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Acaraí
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sadia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- Acaraí — clube que o ogol não tem; entra só pela RSSSF
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Baependi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Baependi)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — clube que o ogol não tem; entra só pela RSSSF
- Sadia — clube que o ogol não tem; entra só pela RSSSF
- Ypiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ypiranga-SC)

### 1958

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Baependi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Baependi)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- vencedor da final pelos jogos (Marcílio Dias) diferente do campeão oficial (Hercílio Luz); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Carlos Renaux

### 1959

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paula Ramos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Seleto
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasto Verde
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Atlético Operário — clube que o ogol não tem; entra só pela RSSSF
- Baependi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Baependi)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Comercial — clube que o ogol não tem; entra só pela RSSSF
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Independente — clube que o ogol não tem; entra só pela RSSSF
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Paula Ramos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paula Ramos-SC)
- Seleto — clube que o ogol não tem; entra só pela RSSSF
- Vasto Verde — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Paula Ramos-SC; o 1º pela soma dos jogos da última fase é América-SC (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Caxias-SC

### 1960

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paula Ramos
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — clube que o ogol não tem; entra só pela RSSSF
- Paula Ramos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paula Ramos-SC)
- vencedor da final pelos jogos (Avaí) diferente do campeão oficial (Metropol); fica o oficial

### 1961

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Metropol

### 1962

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Estrela
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ypiranga
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Atlético Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Operário)
- Baependi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Baependi)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Estrela — clube que o ogol não tem; entra só pela RSSSF
- Flamengo — clube que o ogol não tem; entra só pela RSSSF
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Ypiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ypiranga-SC)
- campeão pela lista oficial, Metropol; o 1º pela soma dos jogos da última fase é Caxias-SC (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Marcílio Dias

### 1963

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- vice pela Wikipédia (sem final de dois clubes): Almirante Barroso

### 1964

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tupy
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- Santa Cruz — clube que o ogol não tem; entra só pela RSSSF
- Tupy — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Internacional-SC

### 1965

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Baependi
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Cruzeiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guatá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guaycurus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hervalense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Imbituba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itaúna
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nevada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paula Ramos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Perdigão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Postal Telegráfico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tamandaré
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tupy
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Urussanga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Atlético Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Operário)
- Baependi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Baependi)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-SC)
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Guarany — clube que o ogol não tem; entra só pela RSSSF
- Guatá — clube que o ogol não tem; entra só pela RSSSF
- Guaycurus — clube que o ogol não tem; entra só pela RSSSF
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Hervalense — clube que o ogol não tem; entra só pela RSSSF
- Imbituba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Imbituba)
- Itaúna — clube que o ogol não tem; entra só pela RSSSF
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Nacional — clube que o ogol não tem; entra só pela RSSSF
- Nevada — clube que o ogol não tem; entra só pela RSSSF
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- Paula Ramos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paula Ramos-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Perdigão — clube que o ogol não tem; entra só pela RSSSF
- Postal Telegráfico — clube que o ogol não tem; entra só pela RSSSF
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz-SC)
- São Paulo — clube que o ogol não tem; entra só pela RSSSF
- Tamandaré — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tamandaré)
- Tupy — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tupy-SC)
- Urussanga — clube que o ogol não tem; entra só pela RSSSF
- Vasco — clube que o ogol não tem; entra só pela RSSSF
- vencedor da final pelos jogos (Metropol) diferente do campeão oficial (Internacional-SC); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Metropol

### 1966

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani/BLU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani/LAG
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guaycurus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Imbituba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Perdigão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sadia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco da Gama
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Atlético Chapecoense — clube que o ogol não tem; entra só pela RSSSF
- Atlético Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Operário)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani/BLU — clube que o ogol não tem; entra só pela RSSSF
- Guarani/LAG — clube que o ogol não tem; entra só pela RSSSF
- Guaycurus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guaycurus)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Imbituba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Imbituba)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- Perdigão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Perdigão)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- Sadia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sadia)
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União-SC)
- Vasco da Gama — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Perdigão; o 1º pela soma dos jogos da última fase é Metropol (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Comercial-SC

### 1967

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Perdigão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-SC)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Perdigão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Perdigão)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vencedor da final pelos jogos (Guarani-SC) diferente do campeão oficial (Metropol); fica o oficial

### 1968

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Perdigão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- Atlético Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Operário)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Perdigão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Perdigão)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Criciúma

### 1969

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Metropol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Metropol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Metropol)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)

### 1970

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Olímpico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Olímpico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpico-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- campeão pela lista oficial, Ferroviário-SC; o 1º pela soma dos jogos da última fase é América-SC (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Olímpico-SC

### 1971

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Almirante Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Almirante Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Almirante Barroso)
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- campeão pela lista oficial, América-SC; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Próspera

### 1972

- tabela publicada x jogos — 2º Turno / -: Figueirense tabela [6, 3, 0, 3, 0, 3] jogos [24, 12, 6, 6, 23, 13] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [6, 2, 2, 2, 6, 4] jogos [24, 10, 7, 7, 31, 22] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: América-SC tabela [6, 2, 1, 3, 4, 6] jogos [24, 11, 6, 7, 33, 19] — a tabela conta 6 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [6, 1, 2, 3, 1, 4] jogos [24, 8, 8, 8, 18, 22] — a tabela conta 6 jogos e as fontes trazem 24
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Avaí

### 1973

- tabela publicada x jogos — 3º Turno / -: Caxias-SC tabela [8, 3, 4, 1, 12, 6] jogos [8, 3, 4, 1, 13, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: Próspera tabela [8, 3, 4, 1, 4, 3] jogos [8, 3, 4, 1, 6, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3º Turno / -: América-SC tabela [8, 3, 2, 3, 8, 10] jogos [7, 2, 2, 3, 8, 10] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 3º Turno / -: Internacional-SC tabela [8, 3, 1, 4, 4, 8] jogos [7, 2, 1, 4, 5, 10] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — 3º Turno / -: Figueirense tabela [8, 2, 2, 4, 6, 14] jogos [8, 2, 2, 4, 7, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Próspera tabela [26, 9, 11, 6, 19, 16] jogos [26, 9, 11, 6, 21, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: América-SC tabela [26, 9, 6, 11, 26, 32] jogos [25, 8, 6, 11, 26, 32] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Internacional-SC tabela [26, 8, 6, 12, 22, 34] jogos [25, 7, 6, 12, 23, 36] — a tabela conta 26 jogos e as fontes trazem 25
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)

### 1974

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Internacional-SC

### 1975

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-SC)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)

### 1976

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmitos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Palmitos — clube que o ogol não tem; entra só pela RSSSF
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)

### 1977

- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo D: Chapecoense tabela [6, 5, 1, 0, 8, 0] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo D: Carlos Renaux tabela [6, 2, 2, 2, 4, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo D: Avaí tabela [6, 1, 3, 2, 4, 3] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo D: Figueirense tabela [6, 0, 2, 4, 1, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo E: Joinville tabela [6, 6, 0, 0, 7, 0] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo E: Internacional-SC tabela [6, 3, 0, 3, 7, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo E: Marcílio Dias tabela [6, 2, 0, 4, 5, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — All teams in Group D and E qualified to Third Phase / Grupo E: Blumenau tabela [6, 1, 0, 5, 4, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Grupo I: Juventus Jaraguá tabela [16, 6, 4, 6, 17, 14] jogos [16, 7, 4, 5, 18, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — General Table (Final Classification) / -: Marcílio Dias tabela [34, 13, 7, 14, 32, 35] jogos [34, 13, 7, 14, 32, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — General Table (Final Classification) / -: Juventus Jaraguá tabela [34, 10, 9, 15, 31, 37] jogos [34, 11, 9, 14, 32, 37] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Kindermann
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lages
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palmitos
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Xanxerense
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Kindermann — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avaí/Kindermann)
- Lages — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lages)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Palmitos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmitos)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Xanxerense — clube que o ogol não tem; entra só pela RSSSF

### 1978

- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [22, 12, 7, 3, 34, 12] jogos [58, 24, 18, 16, 73, 48] — a tabela conta 22 jogos e as fontes trazem 58
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [22, 9, 7, 6, 19, 15] jogos [49, 16, 16, 17, 43, 47] — a tabela conta 22 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Paysandu-SC tabela [22, 6, 7, 9, 12, 20] jogos [42, 8, 11, 23, 24, 49] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Carlos Renaux tabela [22, 2, 11, 9, 11, 23] jogos [42, 11, 18, 13, 34, 36] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [22, 1, 12, 9, 15, 28] jogos [49, 13, 22, 14, 47, 49] — a tabela conta 22 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Blumenau tabela [22, 11, 7, 4, 25, 13] jogos [48, 20, 16, 12, 52, 38] — a tabela conta 22 jogos e as fontes trazem 48
- tabela publicada x jogos — Primeira fase / -: Internacional-SC tabela [22, 8, 8, 6, 19, 14] jogos [57, 16, 23, 18, 41, 46] — a tabela conta 22 jogos e as fontes trazem 57
- tabela publicada x jogos — Primeira fase / -: Operário-SC tabela [22, 9, 5, 8, 21, 20] jogos [52, 19, 10, 23, 57, 63] — a tabela conta 22 jogos e as fontes trazem 52
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [22, 8, 7, 7, 23, 21] jogos [41, 15, 14, 12, 41, 37] — a tabela conta 22 jogos e as fontes trazem 41
- tabela publicada x jogos — Primeira fase / -: Juventus de Rio do Sul tabela [22, 7, 6, 9, 22, 25] jogos [42, 15, 10, 17, 49, 52] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / Grupo C: Joaçaba EC tabela [22, 7, 10, 5, 20, 17] jogos [5, 4, 0, 1, 14, 3] — a tabela conta 22 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo C: Caçadorense tabela [22, 6, 5, 11, 19, 32] jogos [3, 0, 1, 2, 0, 6] — a tabela conta 22 jogos e as fontes trazem 3
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [22, 12, 7, 3, 34, 12] jogos [58, 24, 18, 16, 73, 48] — a tabela conta 22 jogos e as fontes trazem 58
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [22, 9, 7, 6, 19, 15] jogos [49, 16, 16, 17, 43, 47] — a tabela conta 22 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Paysandu-SC tabela [22, 6, 7, 9, 12, 20] jogos [42, 8, 11, 23, 24, 49] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Carlos Renaux tabela [22, 2, 11, 9, 11, 23] jogos [42, 11, 18, 13, 34, 36] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [22, 1, 12, 9, 15, 28] jogos [49, 13, 22, 14, 47, 49] — a tabela conta 22 jogos e as fontes trazem 49
- tabela publicada x jogos — Primeira fase / -: Blumenau tabela [22, 11, 7, 4, 25, 13] jogos [48, 20, 16, 12, 52, 38] — a tabela conta 22 jogos e as fontes trazem 48
- tabela publicada x jogos — Primeira fase / -: Internacional-SC tabela [22, 8, 8, 6, 19, 14] jogos [57, 16, 23, 18, 41, 46] — a tabela conta 22 jogos e as fontes trazem 57
- tabela publicada x jogos — Primeira fase / -: Operário-SC tabela [22, 9, 5, 8, 21, 20] jogos [52, 19, 10, 23, 57, 63] — a tabela conta 22 jogos e as fontes trazem 52
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [22, 8, 7, 7, 23, 21] jogos [41, 15, 14, 12, 41, 37] — a tabela conta 22 jogos e as fontes trazem 41
- tabela publicada x jogos — Primeira fase / -: Juventus de Rio do Sul tabela [22, 7, 6, 9, 22, 25] jogos [42, 15, 10, 17, 49, 52] — a tabela conta 22 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / Grupo C: Joaçaba EC tabela [22, 7, 10, 5, 20, 17] jogos [5, 4, 0, 1, 14, 3] — a tabela conta 22 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo C: Caçadorense tabela [22, 6, 5, 11, 19, 32] jogos [3, 0, 1, 2, 0, 6] — a tabela conta 22 jogos e as fontes trazem 3
- tabela publicada x jogos — Terceira fase / Winners' Group: Joinville tabela [18, 11, 5, 2, 22, 5] jogos [18, 11, 6, 1, 22, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / Winners' Group: Figueirense tabela [18, 8, 6, 4, 21, 12] jogos [18, 7, 7, 4, 21, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / Winners' Group: Joinville tabela [18, 11, 5, 2, 22, 5] jogos [18, 11, 6, 1, 22, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / Winners' Group: Figueirense tabela [18, 8, 6, 4, 21, 12] jogos [18, 7, 7, 4, 21, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / Requalifying Group: Juventus Jaraguá tabela [8, 3, 2, 3, 8, 7] jogos [7, 2, 2, 3, 6, 7] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Terceira fase / Requalifying Group: Juventus de Rio do Sul tabela [8, 3, 1, 4, 8, 10] jogos [9, 4, 1, 4, 10, 10] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Requalifying Group: Juventus Jaraguá tabela [8, 3, 2, 3, 8, 7] jogos [7, 2, 2, 3, 6, 7] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Terceira fase / Requalifying Group: Juventus de Rio do Sul tabela [8, 3, 1, 4, 8, 10] jogos [9, 4, 1, 4, 10, 10] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Joinville tabela [8, 3, 3, 2, 12, 8] jogos [10, 4, 3, 3, 14, 10] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Criciúma tabela [8, 3, 3, 2, 12, 9] jogos [9, 3, 3, 3, 13, 11] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Chapecoense tabela [8, 3, 3, 2, 9, 9] jogos [9, 4, 3, 2, 13, 10] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Internacional-SC tabela [8, 2, 4, 2, 5, 6] jogos [10, 3, 5, 2, 7, 7] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Joaçaba EC tabela [8, 1, 3, 4, 7, 13] jogos [9, 1, 3, 5, 8, 17] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Joinville tabela [8, 3, 3, 2, 12, 8] jogos [10, 4, 3, 3, 14, 10] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Criciúma tabela [8, 3, 3, 2, 12, 9] jogos [9, 3, 3, 3, 13, 11] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Chapecoense tabela [8, 3, 3, 2, 9, 9] jogos [9, 4, 3, 2, 13, 10] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Internacional-SC tabela [8, 2, 4, 2, 5, 6] jogos [10, 3, 5, 2, 7, 7] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Joaçaba EC tabela [8, 1, 3, 4, 7, 13] jogos [9, 1, 3, 5, 8, 17] — a tabela conta 8 jogos e as fontes trazem 9
- jogo anulado ou cancelado fica de fora: Avaí - Chapecoense (1978-12-13) [Avaí quit the league; all their games in this stage are cancelled]
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concordiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Concordiense — clube que o ogol não tem; entra só pela RSSSF
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-SC)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Operário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Operário-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- vice pela Wikipédia (sem final de dois clubes): Chapecoense

### 1979

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CARLOS RENAUX
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PAYSANDU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio do Sul
- CARLOS RENAUX — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- JUVENTUS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- PAYSANDU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Rio do Sul — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Figueirense

### 1980

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIUMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JUVENTUS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCILIO DIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PAYSANDU
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIUMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- JUVENTUS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- MARCILIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- PAYSANDU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- vice pela Wikipédia (sem final de dois clubes): Criciúma

### 1981

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CARLOS RENAUX
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIUMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciuma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCILIO DIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcilio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PAYSANDU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO DO SUL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio do Sul
- CARLOS RENAUX — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIUMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciuma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- MARCILIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Marcilio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- PAYSANDU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- RIO DO SUL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio do Sul)
- Rio do Sul — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio do Sul)
- vice pela Wikipédia (sem final de dois clubes): Criciúma

### 1982

- tabela publicada x jogos — 1º Turno - Fase final / -: Joinville tabela [6, 3, 3, 0, 11, 6] jogos [49, 23, 13, 13, 55, 35] — a tabela conta 6 jogos e as fontes trazem 49
- tabela publicada x jogos — 1º Turno - Fase final / -: Marcílio Dias tabela [6, 2, 4, 0, 8, 6] jogos [65, 25, 23, 17, 75, 63] — a tabela conta 6 jogos e as fontes trazem 65
- tabela publicada x jogos — 1º Turno - Fase final / -: Criciúma tabela [6, 2, 1, 3, 8, 9] jogos [54, 23, 16, 15, 67, 55] — a tabela conta 6 jogos e as fontes trazem 54
- tabela publicada x jogos — 1º Turno - Fase final / -: Avaí tabela [6, 0, 2, 4, 4, 9] jogos [59, 24, 16, 19, 74, 56] — a tabela conta 6 jogos e as fontes trazem 59
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciuma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio do Sul
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciuma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Rio do Sul — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio do Sul)

### 1983

- tabela publicada x jogos — 1º Turno / -: Joinville tabela [10, 6, 1, 3, 12, 7] jogos [38, 18, 11, 9, 31, 12] — a tabela conta 10 jogos e as fontes trazem 38
- tabela publicada x jogos — 1º Turno / -: Avaí tabela [10, 4, 3, 3, 13, 9] jogos [34, 12, 14, 8, 24, 15] — a tabela conta 10 jogos e as fontes trazem 34
- tabela publicada x jogos — 1º Turno / -: Figueirense tabela [10, 4, 2, 4, 12, 11] jogos [38, 17, 14, 7, 23, 12] — a tabela conta 10 jogos e as fontes trazem 38
- tabela publicada x jogos — 1º Turno / -: Blumenau tabela [10, 4, 2, 4, 12, 16] jogos [28, 13, 4, 11, 17, 15] — a tabela conta 10 jogos e as fontes trazem 28
- tabela publicada x jogos — 1º Turno / -: Rio do Sul tabela [10, 2, 2, 6, 9, 15] jogos [24, 8, 1, 15, 10, 26] — a tabela conta 10 jogos e as fontes trazem 24
- tabela publicada x jogos — 1º Turno / GRUPO DOS PERDEDORES: Internacional-SC tabela [10, 7, 1, 2, 17, 8] jogos [7, 6, 0, 1, 8, 1] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / GRUPO DOS PERDEDORES: Paysandu-SC tabela [10, 5, 4, 1, 9, 6] jogos [8, 5, 1, 2, 5, 3] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / GRUPO DOS PERDEDORES: Carlos Renaux tabela [10, 3, 3, 4, 10, 9] jogos [8, 2, 2, 4, 3, 5] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / GRUPO DOS PERDEDORES: Criciúma tabela [9, 2, 1, 6, 8, 11] jogos [8, 2, 2, 4, 4, 5] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / GRUPO DOS PERDEDORES: Joaçaba EC tabela [9, 1, 3, 5, 4, 13] jogos [5, 0, 1, 4, 0, 6] — a tabela conta 9 jogos e as fontes trazem 5
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CARLOS RENAUX
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCILIO DIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCÍLIO DIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PAYSANDU
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PAYSANDÚ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): RIO DO SUL
- CARLOS RENAUX — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- MARCILIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- MARCÍLIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- PAYSANDU — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- PAYSANDÚ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- RIO DO SUL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio do Sul)
- vencedor da final pelos jogos (Figueirense) diferente do campeão oficial (Joinville); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Figueirense

### 1984

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Carlos Renaux
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rio do Sul
- Carlos Renaux — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Carlos Renaux)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Rio do Sul — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio do Sul)
- vice pela Wikipédia (sem final de dois clubes): Figueirense

### 1985

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Avaí

### 1986

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Marcílio Dias

### 1987

- tabela publicada x jogos — Fase final / -: Joinville tabela [6, 4, 2, 0, 8, 2] jogos [10, 4, 4, 2, 8, 6] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase final / -: Criciúma tabela [6, 2, 2, 2, 4, 5] jogos [8, 4, 2, 2, 8, 5] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Chapecoense tabela [6, 1, 2, 3, 2, 4] jogos [8, 1, 4, 3, 2, 4] — a tabela conta 6 jogos e as fontes trazem 8
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciuma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviario
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paysandú
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Prospera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciuma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Ferroviario — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Paysandu — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Paysandú — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paysandu-SC)
- Prospera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Criciúma

### 1988

- tabela publicada x jogos — 1º Turno - Fase final / -: Figueirense tabela [12, 2, 5, 5, 12, 20] jogos [12, 2, 4, 6, 11, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno - Fase final / -: Próspera tabela [12, 1, 5, 6, 10, 16] jogos [12, 2, 4, 6, 10, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Criciúma tabela [10, 6, 3, 1, 11, 5] jogos [37, 19, 10, 8, 49, 28] — a tabela conta 10 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno / -: Marcílio Dias tabela [10, 4, 5, 1, 15, 8] jogos [38, 13, 12, 13, 58, 51] — a tabela conta 10 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Joinville tabela [10, 5, 2, 3, 16, 10] jogos [40, 15, 13, 12, 52, 41] — a tabela conta 10 jogos e as fontes trazem 40
- tabela publicada x jogos — 2º Turno / -: Blumenau tabela [10, 4, 4, 2, 12, 7] jogos [34, 13, 12, 9, 35, 31] — a tabela conta 10 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Figueirense tabela [10, 4, 4, 2, 12, 8] jogos [22, 6, 8, 8, 23, 28] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [10, 4, 4, 2, 9, 7] jogos [34, 18, 9, 7, 43, 31] — a tabela conta 10 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Chapecoense tabela [10, 4, 2, 4, 10, 11] jogos [22, 7, 6, 9, 18, 25] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Próspera tabela [10, 2, 5, 3, 8, 11] jogos [22, 4, 9, 9, 18, 26] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Brusque tabela [10, 1, 5, 4, 8, 12] jogos [32, 8, 13, 11, 31, 31] — a tabela conta 10 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno / -: Internacional-SC tabela [10, 2, 3, 5, 11, 17] jogos [22, 3, 9, 10, 17, 30] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [10, 0, 6, 4, 7, 13] jogos [22, 3, 10, 9, 16, 28] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Ferroviário-SC tabela [10, 0, 5, 5, 3, 13] jogos [21, 3, 11, 7, 12, 22] — a tabela conta 10 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRUSQUE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FERROVIÁRIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): HERCÍLIO LUZ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCÍLIO DIAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PRÓSPERA
- BRUSQUE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FERROVIÁRIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- HERCÍLIO LUZ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- MARCÍLIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- PRÓSPERA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vice pela Wikipédia (sem final de dois clubes): Blumenau

### 1989

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviario
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercilio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcilio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Prospera
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Próspera
- Araranguá — clube que o ogol não tem; entra só pela RSSSF
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Ferroviario — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercilio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcilio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Prospera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- Próspera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Próspera)
- vencedor da final pelos jogos (Joinville) diferente do campeão oficial (Criciúma); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Joinville

### 1990

- tabela publicada x jogos — 1º Turno / -: Criciúma tabela [11, 8, 1, 2, 22, 14] jogos [20, 9, 10, 1, 14, 1] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 1º Turno / -: Blumenau tabela [11, 6, 3, 2, 14, 8] jogos [17, 6, 4, 7, 8, 11] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: Chapecoense tabela [11, 6, 2, 3, 13, 9] jogos [22, 9, 8, 5, 14, 6] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — 1º Turno / -: Figueirense tabela [11, 5, 4, 2, 11, 6] jogos [20, 7, 6, 7, 9, 10] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 1º Turno / -: Joinville tabela [11, 5, 3, 3, 11, 7] jogos [25, 14, 5, 6, 23, 6] — a tabela conta 11 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Hercílio Luz tabela [11, 3, 4, 4, 13, 10] jogos [14, 3, 4, 7, 8, 11] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — 1º Turno / -: Araranguá tabela [11, 3, 3, 5, 10, 13] jogos [18, 7, 5, 6, 14, 11] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Avaí tabela [11, 2, 5, 4, 5, 9] jogos [19, 4, 5, 10, 4, 14] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — 1º Turno / -: Ferroviário-SC tabela [11, 2, 5, 4, 9, 15] jogos [20, 5, 9, 6, 6, 13] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 1º Turno / -: Brusque tabela [11, 2, 4, 5, 5, 8] jogos [22, 8, 6, 8, 12, 12] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — 1º Turno / -: Caçadorense tabela [11, 2, 3, 6, 9, 17] jogos [18, 4, 4, 10, 7, 17] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Marcílio Dias tabela [11, 1, 5, 5, 6, 13] jogos [19, 6, 4, 9, 8, 15] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Joinville tabela [11, 9, 0, 2, 22, 4] jogos [25, 14, 5, 6, 23, 6] — a tabela conta 11 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Criciúma tabela [11, 5, 5, 1, 14, 6] jogos [20, 9, 10, 1, 14, 1] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Araranguá tabela [11, 5, 4, 2, 13, 6] jogos [18, 7, 5, 6, 14, 11] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Figueirense tabela [11, 4, 4, 3, 12, 9] jogos [20, 7, 6, 7, 9, 10] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Brusque tabela [11, 4, 4, 3, 10, 11] jogos [22, 8, 6, 8, 12, 12] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Chapecoense tabela [11, 5, 1, 5, 11, 12] jogos [22, 9, 8, 5, 14, 6] — a tabela conta 11 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Ferroviário-SC tabela [11, 2, 7, 2, 7, 8] jogos [20, 5, 9, 6, 6, 13] — a tabela conta 11 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Blumenau tabela [11, 3, 3, 5, 12, 15] jogos [17, 6, 4, 7, 8, 11] — a tabela conta 11 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Marcílio Dias tabela [11, 3, 3, 5, 8, 15] jogos [19, 6, 4, 9, 8, 15] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Caçadorense tabela [11, 2, 4, 5, 9, 19] jogos [18, 4, 4, 10, 7, 17] — a tabela conta 11 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [11, 1, 5, 5, 8, 14] jogos [14, 3, 4, 7, 8, 11] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [11, 1, 4, 6, 6, 13] jogos [19, 4, 5, 10, 4, 14] — a tabela conta 11 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Criciúma tabela [22, 13, 6, 3, 36, 20] jogos [20, 9, 10, 1, 14, 1] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Joinville tabela [22, 14, 3, 5, 33, 11] jogos [25, 14, 5, 6, 23, 6] — a tabela conta 22 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Figueirense tabela [22, 9, 8, 5, 23, 15] jogos [20, 7, 6, 7, 9, 10] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Chapecoense tabela [22, 11, 3, 8, 24, 21] jogos [22, 9, 8, 5, 14, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Blumenau tabela [22, 9, 6, 7, 26, 23] jogos [17, 6, 4, 7, 8, 11] — a tabela conta 22 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Araranguá tabela [22, 8, 7, 7, 22, 20] jogos [18, 7, 5, 6, 14, 11] — a tabela conta 22 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Brusque tabela [22, 6, 8, 8, 15, 19] jogos [22, 8, 6, 8, 12, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Ferroviário-SC tabela [22, 4, 12, 6, 16, 23] jogos [20, 5, 9, 6, 6, 13] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [22, 4, 9, 9, 21, 24] jogos [14, 3, 4, 7, 8, 11] — a tabela conta 22 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Marcílio Dias tabela [22, 4, 8, 10, 15, 27] jogos [19, 6, 4, 9, 8, 15] — a tabela conta 22 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Caçadorense tabela [22, 4, 7, 11, 17, 36] jogos [18, 4, 4, 10, 7, 17] — a tabela conta 22 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [22, 3, 9, 10, 11, 22] jogos [19, 4, 5, 10, 4, 14] — a tabela conta 22 jogos e as fontes trazem 19
- tabela publicada x jogos — 1º Turno - Final / -: Criciúma tabela [10, 4, 6, 0, 11, 3] jogos [20, 9, 10, 1, 14, 1] — a tabela conta 10 jogos e as fontes trazem 20
- tabela publicada x jogos — 1º Turno - Final / -: Chapecoense tabela [10, 3, 6, 1, 10, 6] jogos [22, 9, 8, 5, 14, 6] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 1º Turno - Final / -: Joinville tabela [10, 4, 3, 3, 12, 10] jogos [25, 14, 5, 6, 23, 6] — a tabela conta 10 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno - Final / -: Figueirense tabela [10, 2, 5, 3, 6, 8] jogos [20, 7, 6, 7, 9, 10] — a tabela conta 10 jogos e as fontes trazem 20
- tabela publicada x jogos — 1º Turno - Final / -: Araranguá tabela [10, 3, 2, 5, 11, 15] jogos [18, 7, 5, 6, 14, 11] — a tabela conta 10 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno - Final / -: Blumenau tabela [10, 1, 4, 5, 7, 15] jogos [17, 6, 4, 7, 8, 11] — a tabela conta 10 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Ferroviário-SC tabela [10, 5, 3, 2, 11, 7] jogos [20, 5, 9, 6, 6, 13] — a tabela conta 10 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Marcílio Dias tabela [10, 4, 3, 3, 10, 10] jogos [19, 6, 4, 9, 8, 15] — a tabela conta 10 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [10, 5, 1, 4, 13, 9] jogos [19, 4, 5, 10, 4, 14] — a tabela conta 10 jogos e as fontes trazem 19
- tabela publicada x jogos — 2º Turno / -: Brusque tabela [10, 4, 2, 4, 9, 9] jogos [22, 8, 6, 8, 12, 12] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [10, 3, 2, 5, 13, 16] jogos [14, 3, 4, 7, 8, 11] — a tabela conta 10 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Caçadorense tabela [10, 3, 1, 6, 8, 13] jogos [18, 4, 4, 10, 7, 17] — a tabela conta 10 jogos e as fontes trazem 18
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ARARANGUÁ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): BRUSQUE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CHAPECOENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FERROVIÁRIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): HERCÍLIO LUZ
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MARCÍLIO DIAS
- ARARANGUÁ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- BRUSQUE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- CHAPECOENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FERROVIÁRIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- HERCÍLIO LUZ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- MARCÍLIO DIAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- vencedor da final pelos jogos (Chapecoense) diferente do campeão oficial (Criciúma); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Joinville

### 1991

- tabela publicada x jogos — Primeira fase / Grupo 5: Caçadorense tabela [6, 2, 2, 2, 8, 10] jogos [10, 3, 3, 4, 12, 17] — a tabela conta 6 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo 5: Juventus-SC tabela [6, 1, 3, 2, 8, 8] jogos [8, 2, 4, 2, 12, 10] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 5: Marcílio Dias tabela [6, 2, 1, 3, 7, 10] jogos [8, 3, 1, 4, 10, 12] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [26, 11, 10, 5, 36, 28] jogos [25, 10, 10, 5, 34, 27] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Segunda fase / -: Araranguá tabela [26, 11, 6, 9, 30, 22] jogos [25, 11, 6, 8, 29, 20] — a tabela conta 26 jogos e as fontes trazem 25
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- Araranguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-SC)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)

### 1992

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concórdia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Araranguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Concórdia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Concórdia)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- vencedor da final pelos jogos (Criciúma) diferente do campeão oficial (Brusque); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Avaí

### 1993

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concórdia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Araranguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Concórdia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Concórdia)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)

### 1994

- tabela publicada x jogos — Primeira fase / -: Caçadorense tabela [26, 7, 9, 10, 23, 37] jogos [25, 5, 9, 11, 21, 36] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / -: Concórdia tabela [26, 8, 6, 12, 43, 46] jogos [25, 8, 6, 11, 42, 44] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Quadrangular de Repescagem / -: Internacional-SC tabela [6, 5, 0, 1, 13, 5] jogos [6, 6, 0, 0, 14, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Quadrangular de Repescagem / -: Caçadorense tabela [6, 3, 2, 1, 10, 7] jogos [6, 2, 2, 2, 9, 8] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concordia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concórdia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hermann Aichinger
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Araranguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Concordia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Concórdia)
- Concórdia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Concórdia)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hermann Aichinger — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hermann Aichinger)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)

### 1995

- tabela publicada x jogos — 2º Turno / -: Chapecoense tabela [14, 9, 5, 0, 24, 11] jogos [46, 29, 11, 6, 78, 33] — a tabela conta 14 jogos e as fontes trazem 46
- tabela publicada x jogos — 2º Turno / -: Criciúma tabela [14, 7, 4, 3, 25, 13] jogos [46, 27, 12, 7, 79, 34] — a tabela conta 14 jogos e as fontes trazem 46
- tabela publicada x jogos — 2º Turno / -: Marcílio Dias tabela [14, 6, 2, 6, 25, 20] jogos [34, 14, 6, 14, 54, 52] — a tabela conta 14 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Concórdia tabela [14, 5, 4, 5, 25, 24] jogos [34, 10, 10, 14, 51, 57] — a tabela conta 14 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Tubarão FC tabela [14, 4, 6, 4, 18, 21] jogos [34, 11, 10, 13, 40, 49] — a tabela conta 14 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Avaí tabela [14, 4, 3, 7, 28, 28] jogos [28, 10, 6, 12, 45, 44] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Joinville tabela [14, 3, 6, 5, 17, 22] jogos [30, 10, 8, 12, 36, 43] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Atlético-SC tabela [14, 1, 4, 9, 9, 32] jogos [30, 7, 9, 14, 35, 63] — a tabela conta 14 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Figueirense tabela [14, 8, 5, 1, 21, 10] jogos [38, 15, 14, 9, 47, 38] — a tabela conta 14 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Blumenau tabela [14, 7, 2, 5, 22, 17] jogos [36, 9, 12, 15, 42, 52] — a tabela conta 14 jogos e as fontes trazem 36
- tabela publicada x jogos — 2º Turno / -: Araranguá tabela [14, 5, 7, 2, 16, 12] jogos [28, 9, 12, 7, 31, 27] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Juventus-SC tabela [14, 4, 5, 5, 14, 16] jogos [28, 5, 9, 14, 29, 44] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Brusque tabela [14, 4, 4, 6, 18, 16] jogos [20, 9, 5, 6, 44, 23] — a tabela conta 14 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Hercílio Luz tabela [14, 3, 6, 5, 16, 21] jogos [28, 7, 14, 7, 40, 40] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Internacional-SC tabela [14, 4, 2, 8, 16, 22] jogos [28, 8, 5, 15, 35, 46] — a tabela conta 14 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno / -: Caçadorense tabela [14, 2, 7, 5, 9, 18] jogos [28, 4, 14, 10, 24, 39] — a tabela conta 14 jogos e as fontes trazem 28
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Araranguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Concórdia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Hercílio Luz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Imbituba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Juventus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sombrio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tupy
- Araranguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araranguá)
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Concórdia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Concórdia)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Hercílio Luz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Hercílio Luz)
- Imbituba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Imbituba)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Juventus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Juventus-SC)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Sombrio — clube que o ogol não tem; entra só pela RSSSF
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- Tupy — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tupy-SC)
- vencedor da final pelos jogos (Joaçaba EC) diferente do campeão oficial (Criciúma); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Chapecoense

### 1996

- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [9, 5, 4, 0, 19, 9] jogos [12, 7, 4, 1, 24, 12] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [9, 5, 3, 1, 15, 9] jogos [12, 7, 3, 2, 19, 13] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [9, 3, 2, 4, 16, 13] jogos [12, 3, 3, 6, 18, 18] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Tubarão FC tabela [9, 3, 1, 5, 14, 14] jogos [12, 4, 2, 6, 18, 17] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [3, 2, 1, 0, 3, 1] jogos [26, 14, 8, 4, 40, 25] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [3, 1, 1, 1, 3, 3] jogos [26, 15, 6, 5, 45, 25] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [3, 0, 1, 2, 3, 5] jogos [24, 7, 6, 11, 35, 33] — a tabela conta 3 jogos e as fontes trazem 24
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [3, 2, 0, 1, 5, 3] jogos [26, 15, 6, 5, 45, 25] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [3, 2, 0, 1, 4, 4] jogos [26, 14, 8, 4, 40, 25] — a tabela conta 3 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Tubarão FC tabela [3, 1, 1, 1, 4, 3] jogos [24, 11, 5, 8, 36, 28] — a tabela conta 3 jogos e as fontes trazem 24
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [3, 0, 1, 2, 2, 5] jogos [24, 7, 6, 11, 35, 33] — a tabela conta 3 jogos e as fontes trazem 24
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jaraguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Jaraguá — clube que o ogol não tem; entra só pela RSSSF
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Chapecoense

### 1997

- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 5, 2, 2, 20, 12] jogos [11, 6, 2, 3, 25, 17] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Tubarão FC tabela [9, 5, 2, 2, 15, 9] jogos [11, 6, 3, 2, 18, 11] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 5, 1, 3, 21, 13] jogos [11, 5, 2, 4, 23, 16] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 4, 4, 1, 13, 4] jogos [11, 5, 4, 2, 18, 9] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Total Table both Phases / -: Chapecoense tabela [18, 9, 5, 4, 33, 22] jogos [22, 11, 6, 5, 42, 29] — a tabela conta 18 jogos e as fontes trazem 22
- tabela publicada x jogos — Total Table both Phases / -: Avaí tabela [18, 9, 2, 7, 30, 27] jogos [22, 10, 5, 7, 34, 30] — a tabela conta 18 jogos e as fontes trazem 22
- tabela publicada x jogos — Total Table both Phases / -: Blumenau tabela [18, 6, 4, 8, 18, 25] jogos [20, 6, 6, 8, 18, 25] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Total Table both Phases / -: Atlético-SC tabela [18, 4, 6, 8, 18, 30] jogos [20, 4, 6, 10, 21, 36] — a tabela conta 18 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jaraguá
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Jaraguá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jaraguá-SC)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- vice pela Wikipédia (sem final de dois clubes): Tubarão FC

### 1998

- tabela publicada x jogos — Segunda fase / -: Atlético-SC tabela [9, 1, 5, 3, 10, 12] jogos [5, 0, 3, 2, 6, 9] — a tabela conta 9 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase final / -: Criciúma tabela [18, 10, 5, 3, 30, 15] jogos [32, 17, 10, 5, 53, 30] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase final / -: Tubarão FC tabela [18, 9, 7, 2, 30, 18] jogos [32, 13, 13, 6, 47, 34] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase final / -: Avaí tabela [18, 8, 6, 4, 25, 16] jogos [31, 12, 9, 10, 37, 32] — a tabela conta 18 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Brusque tabela [18, 8, 5, 5, 23, 15] jogos [26, 10, 7, 9, 32, 28] — a tabela conta 18 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase final / -: Chapecoense tabela [18, 8, 3, 7, 19, 26] jogos [19, 8, 3, 8, 20, 28] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Atlético-SC tabela [18, 5, 6, 7, 21, 25] jogos [14, 4, 4, 6, 17, 22] — a tabela conta 18 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Criciúma tabela [6, 4, 2, 0, 15, 9] jogos [11, 5, 5, 1, 17, 12] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Tubarão FC tabela [6, 2, 4, 0, 9, 6] jogos [11, 3, 6, 2, 14, 10] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Avaí tabela [6, 0, 2, 4, 3, 9] jogos [10, 2, 3, 5, 7, 13] — a tabela conta 6 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atletico
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atletico Alto Vale
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciuma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcilio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarao
- Atletico — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Atletico Alto Vale — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Alto Vale)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciuma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Marcilio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarao — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- vice pela Wikipédia (sem final de dois clubes): Tubarão FC

### 1999

- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [11, 6, 4, 1, 20, 8] jogos [10, 5, 4, 1, 19, 8] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [11, 6, 2, 3, 18, 13] jogos [10, 6, 2, 2, 18, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Quartas de final / -: Figueirense tabela [11, 6, 4, 1, 20, 8] jogos [10, 5, 4, 1, 19, 8] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Quartas de final / -: Joinville tabela [11, 6, 2, 3, 18, 13] jogos [10, 6, 2, 2, 18, 12] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Criciúma win second phase, / -: Figueirense tabela [22, 14, 6, 2, 55, 21] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Avaí tabela [22, 13, 5, 4, 46, 21] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Joinville tabela [22, 13, 4, 5, 47, 28] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Criciúma tabela [22, 12, 5, 5, 47, 22] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Fraiburgo tabela [22, 11, 3, 8, 31, 25] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Chapecoense tabela [22, 10, 4, 8, 32, 32] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Tubarão FC tabela [22, 8, 5, 9, 30, 27] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Avaí/Kindermann tabela [22, 7, 6, 9, 32, 40] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Criciúma win second phase, / -: Atlético-SC tabela [22, 5, 6, 11, 26, 35] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRICIÚMA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): FIGUEIRENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fraiburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JOINVILLE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Kindermann
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lages
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Atlético — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético-SC)
- Botafogo — clube que o ogol não tem; entra só pela RSSSF
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- CRICIÚMA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- FIGUEIRENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Fraiburgo — clube que o ogol não tem; entra só pela RSSSF
- JOINVILLE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Kindermann — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avaí/Kindermann)
- Lages — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lages)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)
- vice pela Wikipédia (sem final de dois clubes): Avaí

### 2000

- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [11, 6, 2, 3, 23, 16] jogos [11, 5, 2, 4, 23, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Fraiburgo tabela [11, 3, 2, 6, 11, 16] jogos [11, 4, 2, 5, 13, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [11, 6, 2, 3, 23, 16] jogos [11, 5, 2, 4, 23, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Fraiburgo tabela [11, 3, 2, 6, 11, 16] jogos [11, 4, 2, 5, 13, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Marcílio Dias tabela [22, 12, 5, 5, 45, 29] jogos [22, 11, 5, 6, 45, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Fraiburgo tabela [22, 9, 5, 8, 27, 31] jogos [22, 10, 5, 7, 29, 31] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Chapecoense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Criciúma
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Figueirense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fraiburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Joinville
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Kindermann
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lages
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Marcílio Dias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tubarão
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Chapecoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Chapecoense)
- Criciúma — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Criciúma)
- Figueirense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Figueirense)
- Fraiburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fraiburgo)
- Joinville — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Joinville)
- Kindermann — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Avaí/Kindermann)
- Lages — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lages)
- Marcílio Dias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marcílio Dias)
- Tubarão — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tubarão FC)

### 2001

- tabela publicada x jogos — Primeira fase / -: Tubarão FC tabela [9, 6, 2, 1, 17, 10] jogos [16, 10, 5, 1, 27, 15] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Primeira fase / -: Internacional-SC tabela [9, 4, 1, 4, 14, 14] jogos [16, 6, 1, 9, 20, 26] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Primeira fase / -: Avaí/Kindermann tabela [9, 3, 2, 4, 16, 16] jogos [16, 5, 5, 6, 25, 26] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Primeira fase / -: Atlético Alto Vale tabela [9, 2, 2, 5, 11, 16] jogos [16, 4, 5, 7, 21, 25] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 0, 1, 8, 8, 24] jogos [16, 2, 5, 9, 19, 32] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [9, 6, 2, 1, 25, 14] jogos [15, 8, 5, 2, 37, 25] — a tabela conta 9 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [9, 5, 3, 1, 26, 17] jogos [15, 8, 6, 1, 41, 23] — a tabela conta 9 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Tubarão FC tabela [9, 4, 2, 3, 15, 12] jogos [22, 9, 4, 9, 31, 36] — a tabela conta 9 jogos e as fontes trazem 22
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [9, 4, 2, 3, 17, 15] jogos [15, 5, 4, 6, 23, 23] — a tabela conta 9 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Atlético Alto Vale tabela [9, 3, 2, 4, 15, 22] jogos [16, 8, 3, 5, 32, 27] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Internacional-SC tabela [9, 2, 4, 3, 8, 10] jogos [16, 2, 5, 9, 11, 28] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [9, 2, 3, 4, 17, 19] jogos [16, 6, 6, 4, 31, 26] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / -: Avaí/Kindermann tabela [9, 2, 3, 4, 12, 17] jogos [16, 7, 4, 5, 21, 23] — a tabela conta 9 jogos e as fontes trazem 16
- tabela publicada x jogos — Combined Table (both stages) / -: Tubarão FC tabela [18, 10, 4, 4, 32, 22] jogos [34, 19, 8, 7, 53, 37] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — Combined Table (both stages) / -: Internacional-SC tabela [18, 6, 5, 7, 22, 24] jogos [32, 8, 6, 18, 31, 54] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — Combined Table (both stages) / -: Avaí/Kindermann tabela [18, 5, 5, 8, 28, 33] jogos [32, 12, 9, 11, 46, 49] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — Combined Table (both stages) / -: Atlético Alto Vale tabela [18, 5, 4, 9, 26, 38] jogos [34, 12, 9, 13, 54, 54] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — Combined Table (both stages) / -: Chapecoense tabela [18, 2, 4, 12, 25, 43] jogos [32, 8, 11, 13, 50, 58] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [6, 3, 3, 0, 15, 6] jogos [26, 14, 8, 4, 61, 36] — a tabela conta 6 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [6, 2, 3, 1, 12, 11] jogos [26, 12, 8, 6, 57, 43] — a tabela conta 6 jogos e as fontes trazem 26
- tabela publicada x jogos — Segunda fase / -: Tubarão FC tabela [6, 1, 2, 3, 7, 15] jogos [40, 20, 10, 10, 60, 52] — a tabela conta 6 jogos e as fontes trazem 40
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [6, 1, 2, 3, 6, 8] jogos [24, 10, 6, 8, 39, 36] — a tabela conta 6 jogos e as fontes trazem 24
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Brusque
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fraiburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Lages
- Lages — casado pelo nome com o clube do calendário do ogol deste ano (Internacional-SC)
- Brusque — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Brusque)
- Fraiburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fraiburgo)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Internacional-SC x Tubarão FC, ogol 2001-02-11); fica a do ogol
- ano errado na data da RSSSF — Joinville 1-0 Internacional-SC: RSSSF 2000-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 0-0 Avaí: RSSSF 2000-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Figueirense 1-3 Criciúma: RSSSF 2000-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 2-1 Chapecoense: RSSSF 2000-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 3-0 Marcílio Dias: RSSSF 2000-01-21, ogol 2001-01-21; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 2-0 Figueirense: RSSSF 2000-01-27, ogol 2001-01-27; fica a do ogol
- ano errado na data da RSSSF — Criciúma 2-2 Tubarão FC: RSSSF 2000-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 1-0 Atlético Alto Vale: RSSSF 2000-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 0-2 Avaí/Kindermann: RSSSF 2000-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-2 Joinville: RSSSF 2000-01-28, ogol 2001-01-28; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 2-4 Figueirense: RSSSF 2000-02-03, ogol 2001-02-03; fica a do ogol
- ano errado na data da RSSSF — Joinville 2-0 Chapecoense: RSSSF 2000-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 1-0 Marcílio Dias: RSSSF 2000-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 2-1 Criciúma: RSSSF 2000-02-04, ogol 2001-02-04; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 2-1 Joinville: RSSSF 2000-02-10, ogol 2001-02-10; fica a do ogol
- ano errado na data da RSSSF — Joinville 3-3 Criciúma: RSSSF 2000-02-17, ogol 2001-02-17; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 2-4 Internacional-SC: RSSSF 2000-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-1 Marcílio Dias: RSSSF 2000-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 2-2 Figueirense: RSSSF 2000-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 1-2 Tubarão FC: RSSSF 2000-02-18, ogol 2001-02-18; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-0 Internacional-SC: RSSSF 2000-02-21, ogol 2001-02-21; fica a do ogol
- ano errado na data da RSSSF — Criciúma 0-1 Avaí: RSSSF 2000-03-03, ogol 2001-03-03; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 3-2 Atlético Alto Vale: RSSSF 2000-03-04, ogol 2001-03-04; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 2-1 Avaí/Kindermann: RSSSF 2000-03-04, ogol 2001-03-04; fica a do ogol
- ano errado na data da RSSSF — Figueirense 1-0 Joinville: RSSSF 2000-03-04, ogol 2001-03-04; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 4-0 Chapecoense: RSSSF 2000-03-04, ogol 2001-03-04; fica a do ogol
- ano errado na data da RSSSF — Joinville 1-3 Tubarão FC: RSSSF 2000-03-10, ogol 2001-03-10; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-3 Figueirense: RSSSF 2000-03-10, ogol 2001-03-10; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 0-0 Internacional-SC: RSSSF 2000-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 2-4 Criciúma: RSSSF 2000-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 5-2 Atlético Alto Vale: RSSSF 2000-03-11, ogol 2001-03-11; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 1-1 Joinville: RSSSF 2000-03-17, ogol 2001-03-17; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 1-0 Avaí: RSSSF 2000-03-17, ogol 2001-03-17; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 4-3 Avaí/Kindermann: RSSSF 2000-03-18, ogol 2001-03-18; fica a do ogol
- ano errado na data da RSSSF — Figueirense 3-2 Chapecoense: RSSSF 2000-03-18, ogol 2001-03-18; fica a do ogol
- ano errado na data da RSSSF — Criciúma 4-1 Internacional-SC: RSSSF 2000-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 1-2 Figueirense: RSSSF 2000-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 1-1 Tubarão FC: RSSSF 2000-03-24, ogol 2001-03-24; fica a do ogol
- ano errado na data da RSSSF — Avaí 2-1 Atlético Alto Vale: RSSSF 2000-03-25, ogol 2001-03-25; fica a do ogol
- ano errado na data da RSSSF — Joinville 4-2 Avaí/Kindermann: RSSSF 2000-03-25, ogol 2001-03-25; fica a do ogol
- ano errado na data da RSSSF — Criciúma 1-1 Marcílio Dias: RSSSF 2000-03-27, ogol 2001-03-27; fica a do ogol
- ano errado na data da RSSSF — Criciúma 2-1 Figueirense: RSSSF 2000-03-31, ogol 2001-03-31; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 0-1 Joinville: RSSSF 2000-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-3 Avaí/Kindermann: RSSSF 2000-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 3-3 Atlético Alto Vale: RSSSF 2000-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 1-1 Tubarão FC: RSSSF 2000-04-01, ogol 2001-04-01; fica a do ogol
- ano errado na data da RSSSF — Figueirense 3-1 Internacional-SC: RSSSF 2000-04-04, ogol 2001-04-04; fica a do ogol
- ano errado na data da RSSSF — Joinville 2-1 Avaí: RSSSF 2000-04-04, ogol 2001-04-04; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 1-3 Criciúma: RSSSF 2000-04-04, ogol 2001-04-04; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 2-1 Marcílio Dias: RSSSF 2000-04-04, ogol 2001-04-04; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 2-4 Chapecoense: RSSSF 2000-04-04, ogol 2001-04-04; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 1-1 Avaí: RSSSF 2000-04-07, ogol 2001-04-07; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 3-3 Joinville: RSSSF 2000-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 0-0 Avaí/Kindermann: RSSSF 2000-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Criciúma 5-2 Atlético Alto Vale: RSSSF 2000-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Figueirense 3-1 Tubarão FC: RSSSF 2000-04-08, ogol 2001-04-08; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 0-0 Internacional-SC: RSSSF 2000-04-12, ogol 2001-04-12; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 3-2 Figueirense: RSSSF 2000-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Joinville 3-0 Marcílio Dias: RSSSF 2000-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 1-1 Criciúma: RSSSF 2000-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Avaí 3-1 Chapecoense: RSSSF 2000-04-14, ogol 2001-04-14; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 1-1 Chapecoense: RSSSF 2000-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Criciúma 3-2 Joinville: RSSSF 2000-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 2-0 Atlético Alto Vale: RSSSF 2000-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 4-0 Avaí: RSSSF 2000-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Figueirense 2-0 Avaí/Kindermann: RSSSF 2000-04-18, ogol 2001-04-18; fica a do ogol
- ano errado na data da RSSSF — Joinville 4-4 Figueirense: RSSSF 2000-04-21, ogol 2001-04-21; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 0-1 Marcílio Dias: RSSSF 2000-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Avaí 1-4 Criciúma: RSSSF 2000-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 1-4 Tubarão FC: RSSSF 2000-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 2-1 Internacional-SC: RSSSF 2000-04-22, ogol 2001-04-22; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 2-3 Joinville: RSSSF 2000-04-28, ogol 2001-04-28; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 1-1 Marcílio Dias: RSSSF 2000-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Criciúma 3-1 Chapecoense: RSSSF 2000-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Figueirense 1-0 Avaí: RSSSF 2000-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 1-2 Avaí/Kindermann: RSSSF 2000-04-29, ogol 2001-04-29; fica a do ogol
- ano errado na data da RSSSF — Joinville 5-1 Atlético Alto Vale: RSSSF 2000-05-02, ogol 2001-05-02; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 0-1 Internacional-SC: RSSSF 2000-05-02, ogol 2001-05-02; fica a do ogol
- ano errado na data da RSSSF — Avaí 0-1 Tubarão FC: RSSSF 2000-05-02, ogol 2001-05-02; fica a do ogol
- ano errado na data da RSSSF — Chapecoense 3-0 Figueirense: RSSSF 2000-05-02, ogol 2001-05-02; fica a do ogol
- ano errado na data da RSSSF — Marcílio Dias 3-3 Criciúma: RSSSF 2000-05-02, ogol 2001-05-02; fica a do ogol
- ano errado na data da RSSSF — Internacional-SC 2-1 Criciúma: RSSSF 2000-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Figueirense 1-1 Marcílio Dias: RSSSF 2000-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 3-1 Chapecoense: RSSSF 2000-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Atlético Alto Vale 1-1 Avaí: RSSSF 2000-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Avaí/Kindermann 3-3 Joinville: RSSSF 2000-05-05, ogol 2001-05-05; fica a do ogol
- ano errado na data da RSSSF — Joinville 2-2 Criciúma: RSSSF 2000-05-09, ogol 2001-05-09; fica a do ogol
- ano errado na data da RSSSF — Figueirense 4-0 Tubarão FC: RSSSF 2000-05-09, ogol 2001-05-09; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 0-1 Joinville: RSSSF 2000-05-12, ogol 2001-05-12; fica a do ogol
- ano errado na data da RSSSF — Criciúma 1-0 Figueirense: RSSSF 2000-05-13, ogol 2001-05-13; fica a do ogol
- ano errado na data da RSSSF — Joinville 5-1 Figueirense: RSSSF 2000-05-16, ogol 2001-05-16; fica a do ogol
- ano errado na data da RSSSF — Criciúma 3-3 Tubarão FC: RSSSF 2000-05-16, ogol 2001-05-16; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 3-2 Criciúma: RSSSF 2000-05-20, ogol 2001-05-20; fica a do ogol
- ano errado na data da RSSSF — Figueirense 0-0 Joinville: RSSSF 2000-05-20, ogol 2001-05-20; fica a do ogol
- ano errado na data da RSSSF — Figueirense 0-1 Criciúma: RSSSF 2000-05-23, ogol 2001-05-23; fica a do ogol
- ano errado na data da RSSSF — Joinville 4-0 Tubarão FC: RSSSF 2000-05-23, ogol 2001-05-23; fica a do ogol
- ano errado na data da RSSSF — Tubarão FC 1-1 Figueirense: RSSSF 2000-05-26, ogol 2001-05-26; fica a do ogol
- ano errado na data da RSSSF — Criciúma 3-3 Joinville: RSSSF 2000-05-26, ogol 2001-05-26; fica a do ogol
- ano errado na data da RSSSF — Joinville 3-0 Criciúma: RSSSF 2000-05-30, ogol 2001-05-30; fica a do ogol
- ano errado na data da RSSSF — Criciúma 0-2 Joinville: RSSSF 2000-06-03, ogol 2001-06-03; fica a do ogol
- só na RSSSF (não achado no ogol): Joaçaba EC 3-1 Internacional-SC (2000-10-15)
- só na RSSSF (não achado no ogol): Fraiburgo 0-0 Tubarão FC (2000-10-15)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 0-1 Brusque (2000-10-15)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 0-0 Chapecoense (2000-10-15)
- só na RSSSF (não achado no ogol): Tubarão FC 3-1 Joaçaba EC (2000-10-18)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 0-2 Fraiburgo (2000-10-18)
- só na RSSSF (não achado no ogol): Internacional-SC 0-1 Avaí/Kindermann (2000-10-18)
- só na RSSSF (não achado no ogol): Brusque 0-0 Chapecoense (2000-10-18)
- só na RSSSF (não achado no ogol): Chapecoense 3-1 Internacional-SC (2000-10-22)
- só na RSSSF (não achado no ogol): Brusque 1-1 Fraiburgo (2000-10-22)
- só na RSSSF (não achado no ogol): Joaçaba EC 2-2 Atlético Alto Vale (2000-10-22)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 1-1 Tubarão FC (2000-10-22)
- só na RSSSF (não achado no ogol): Tubarão FC 1-0 Chapecoense (2000-10-25)
- só na RSSSF (não achado no ogol): Joaçaba EC 1-0 Fraiburgo (2000-10-25)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 3-2 Avaí/Kindermann (2000-10-25)
- só na RSSSF (não achado no ogol): Internacional-SC 1-0 Brusque (2000-10-25)
- só na RSSSF (não achado no ogol): Chapecoense 2-2 Atlético Alto Vale (2000-10-29)
- só na RSSSF (não achado no ogol): Internacional-SC 1-2 Tubarão FC (2000-10-29)
- só na RSSSF (não achado no ogol): Brusque 1-2 Joaçaba EC (2000-10-29)
- só na RSSSF (não achado no ogol): Fraiburgo 3-1 Avaí/Kindermann (2000-10-29)
- só na RSSSF (não achado no ogol): Tubarão FC 3-2 Brusque (2000-11-01)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 2-1 Joaçaba EC (2000-11-01)
- só na RSSSF (não achado no ogol): Chapecoense 3-1 Fraiburgo (2000-11-01)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 3-0 Internacional-SC (2000-11-01)
- só na RSSSF (não achado no ogol): Joaçaba EC 3-3 Chapecoense (2000-11-05)
- só na RSSSF (não achado no ogol): Tubarão FC 0-0 Atlético Alto Vale (2000-11-05)
- só na RSSSF (não achado no ogol): Fraiburgo 0-2 Internacional-SC (2000-11-05)
- só na RSSSF (não achado no ogol): Brusque 2-2 Avaí/Kindermann (2000-11-05)
- só na RSSSF (não achado no ogol): Internacional-SC 1-1 Joaçaba EC (2000-11-12)
- só na RSSSF (não achado no ogol): Tubarão FC 1-0 Fraiburgo (2000-11-12)
- só na RSSSF (não achado no ogol): Brusque 0-2 Atlético Alto Vale (2000-11-12)
- só na RSSSF (não achado no ogol): Chapecoense 2-2 Avaí/Kindermann (2000-11-12)
- só na RSSSF (não achado no ogol): Joaçaba EC 2-1 Tubarão FC (2000-11-15)
- só na RSSSF (não achado no ogol): Fraiburgo 0-1 Atlético Alto Vale (2000-11-15)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 1-0 Internacional-SC (2000-11-15)
- só na RSSSF (não achado no ogol): Chapecoense 5-2 Brusque (2000-11-15)
- só na RSSSF (não achado no ogol): Internacional-SC 1-2 Chapecoense (2000-11-19)
- só na RSSSF (não achado no ogol): Fraiburgo 2-1 Brusque (2000-11-19)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 3-1 Joaçaba EC (2000-11-19)
- só na RSSSF (não achado no ogol): Tubarão FC 2-0 Avaí/Kindermann (2000-11-19)
- só na RSSSF (não achado no ogol): Chapecoense 2-0 Tubarão FC (2000-11-22)
- só na RSSSF (não achado no ogol): Fraiburgo 2-1 Joaçaba EC (2000-11-22)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 1-0 Atlético Alto Vale (2000-11-22)
- só na RSSSF (não achado no ogol): Brusque 6-0 Internacional-SC (2000-11-22)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 1-1 Chapecoense (2000-11-26)
- só na RSSSF (não achado no ogol): Tubarão FC 2-0 Internacional-SC (2000-11-26)
- só na RSSSF (não achado no ogol): Joaçaba EC 3-0 Brusque (2000-11-26)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 1-0 Fraiburgo (2000-11-26)
- só na RSSSF (não achado no ogol): Brusque 0-2 Tubarão FC (2000-11-29)
- só na RSSSF (não achado no ogol): Joaçaba EC 1-2 Avaí/Kindermann (2000-11-29)
- só na RSSSF (não achado no ogol): Fraiburgo 1-1 Chapecoense (2000-11-29)
- só na RSSSF (não achado no ogol): Internacional-SC 1-5 Atlético Alto Vale (2000-11-29)
- só na RSSSF (não achado no ogol): Chapecoense 1-0 Joaçaba EC (2000-12-03)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 5-1 Tubarão FC (2000-12-03)
- só na RSSSF (não achado no ogol): Avaí/Kindermann 2-1 Brusque (2000-12-03)
- só na RSSSF (não achado no ogol): Internacional-SC 0-1 Fraiburgo (2000-12-03)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 1-1 Tubarão FC (2000-12-07)
- só na RSSSF (não achado no ogol): Tubarão FC 1-0 Atlético Alto Vale (2000-12-10)

### 2002

- tabela publicada x jogos — Primeira fase / -: Atlético Chapecó tabela [5, 3, 0, 2, 8, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / -: Marcílio Dias tabela [5, 3, 2, 0, 9, 1] jogos [12, 5, 3, 4, 17, 17] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [5, 3, 1, 1, 10, 3] jogos [14, 7, 3, 4, 20, 13] — a tabela conta 5 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Atlético Chapecó tabela [5, 1, 2, 2, 2, 6] jogos [5, 3, 2, 0, 11, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Atlético Chapecó tabela [10, 4, 2, 4, 10, 12] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [5, 3, 1, 1, 9, 6] jogos [12, 4, 1, 7, 22, 25] — a tabela conta 5 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [7, 2, 3, 2, 9, 8] jogos [17, 8, 5, 4, 26, 14] — a tabela conta 7 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [7, 2, 2, 3, 8, 14] jogos [22, 10, 7, 5, 37, 32] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [7, 1, 1, 5, 12, 17] jogos [17, 6, 6, 5, 27, 21] — a tabela conta 7 jogos e as fontes trazem 17
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [7, 5, 2, 0, 25, 8] jogos [9, 6, 3, 0, 28, 9] — a tabela conta 7 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [7, 4, 1, 2, 9, 7] jogos [14, 7, 3, 4, 20, 13] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Marcílio Dias tabela [7, 2, 1, 4, 8, 16] jogos [12, 5, 3, 4, 17, 17] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [7, 1, 0, 6, 13, 19] jogos [12, 4, 1, 7, 22, 25] — a tabela conta 7 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Chapecó
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caxias
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Fraiburgo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tiradentes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Águia do Vale
- Atlético Chapecó — clube que o ogol não tem; entra só pela RSSSF
- Caxias — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caxias-SC)
- Fraiburgo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fraiburgo)
- Tiradentes — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tiradentes-SC)
- Águia do Vale — clube que o ogol não tem; entra só pela RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Criciúma x Figueirense, ogol 2002-05-22); fica a do ogol
- só na RSSSF (não achado no ogol): Chapecoense 2-2 Atlético Chapecó (2002-03-03)
- só na RSSSF (não achado no ogol): Tiradentes-SC 5-3 Fraiburgo (2002-03-03)
- só na RSSSF (não achado no ogol): Caxias-SC 2-4 Águia do Vale (2002-03-03)
- só na RSSSF (não achado no ogol): Atlético Chapecó 2-2 Caxias-SC (2002-03-06)
- só na RSSSF (não achado no ogol): Águia do Vale 3-3 Tiradentes-SC (2002-03-06)
- só na RSSSF (não achado no ogol): Fraiburgo 1-0 Chapecoense (2002-03-06)
- só na RSSSF (não achado no ogol): Fraiburgo 3-2 Atlético Chapecó (2002-03-10)
- só na RSSSF (não achado no ogol): Chapecoense 4-1 Águia do Vale (2002-03-10)
- só na RSSSF (não achado no ogol): Tiradentes-SC 0-0 Caxias-SC (2002-03-10)
- só na RSSSF (não achado no ogol): Atlético Chapecó 0-2 Tiradentes-SC (2002-03-13)
- só na RSSSF (não achado no ogol): Caxias-SC 1-2 Chapecoense (2002-03-13)
- só na RSSSF (não achado no ogol): Águia do Vale 3-2 Fraiburgo (2002-03-13)
- só na RSSSF (não achado no ogol): Águia do Vale 2-1 Atlético Chapecó (2002-03-17)
- só na RSSSF (não achado no ogol): Fraiburgo 3-0 Caxias-SC (2002-03-17)
- só na RSSSF (não achado no ogol): Chapecoense 2-0 Tiradentes-SC (2002-03-17)
- só na RSSSF (não achado no ogol): Atlético Chapecó 2-1 Chapecoense (2002-03-24)
- só na RSSSF (não achado no ogol): Fraiburgo 3-2 Tiradentes-SC (2002-03-24)
- só na RSSSF (não achado no ogol): Águia do Vale 1-3 Caxias-SC (2002-03-24)
- só na RSSSF (não achado no ogol): Caxias-SC 3-3 Atlético Chapecó (2002-03-27)
- só na RSSSF (não achado no ogol): Tiradentes-SC 3-1 Águia do Vale (2002-03-27)
- só na RSSSF (não achado no ogol): Chapecoense 2-2 Fraiburgo (2002-03-27)
- só na RSSSF (não achado no ogol): Atlético Chapecó 3-3 Fraiburgo (2002-03-31)
- só na RSSSF (não achado no ogol): Águia do Vale 1-2 Chapecoense (2002-03-31)
- só na RSSSF (não achado no ogol): Caxias-SC 2-2 Tiradentes-SC (2002-03-31)
- só na RSSSF (não achado no ogol): Tiradentes-SC 0-1 Atlético Chapecó (2002-04-03)
- só na RSSSF (não achado no ogol): Chapecoense 2-0 Caxias-SC (2002-04-03)
- só na RSSSF (não achado no ogol): Fraiburgo 3-0 Águia do Vale (2002-04-03)
- só na RSSSF (não achado no ogol): Atlético Chapecó 2-0 Águia do Vale (2002-04-07)
- só na RSSSF (não achado no ogol): Caxias-SC 4-2 Fraiburgo (2002-04-07)
- só na RSSSF (não achado no ogol): Tiradentes-SC 1-2 Chapecoense (2002-04-07)
- só na RSSSF (não achado no ogol): Atlético Chapecó 2-3 Chapecoense (2002-04-11)
- só na RSSSF (não achado no ogol): Chapecoense 1-1 Atlético Chapecó (2002-04-14)
- só na RSSSF (não achado no ogol): Internacional-SC 2-1 Atlético Alto Vale (2002-04-21)
- só na RSSSF (não achado no ogol): Chapecoense 2-2 Avaí/Kindermann (2002-04-21)
- só na RSSSF (não achado no ogol): Chapecoense 2-0 Atlético Alto Vale (2002-04-28)
- só na RSSSF (não achado no ogol): Atlético Alto Vale 2-2 Chapecoense (2002-05-01)
- vencedor da final pelos jogos (Chapecoense) diferente do campeão oficial (Figueirense); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Criciúma

### 2003

- tabela publicada x jogos — Primeira fase / Grupo B: Chapecoense tabela [10, 6, 1, 3, 15, 13] jogos [10, 5, 1, 4, 15, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- ano errado na data da RSSSF — Tiradentes-SC 0-4 Lages: RSSSF 2003-01-23, ogol 2002-01-23; fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Figueirense

### 2004

- tabela publicada x jogos — Segunda fase / -: Guarani-SC tabela [6, 2, 1, 3, 9, 13] jogos [6, 2, 1, 3, 9, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2005

- sem ocorrências

### 2006

- tabela publicada x jogos — Primeira fase / Grupo A: Chapecoense tabela [10, 1, 3, 6, 11, 22] jogos [10, 1, 3, 6, 11, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2007

- tabela publicada x jogos — Segunda fase / -: Metropolitano tabela [22, 6, 5, 11, 29, 39] jogos [22, 6, 5, 11, 29, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Marcílio Dias tabela [22, 4, 7, 11, 23, 38] jogos [22, 4, 7, 11, 24, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Metropolitano x Chapecoense, ogol 2007-02-22); fica a do ogol

### 2008

- tabela publicada x jogos — Segunda fase / -: Avaí tabela [11, 7, 3, 1, 31, 9] jogos [11, 7, 3, 1, 30, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Hermann Aichinger tabela [11, 3, 3, 5, 16, 21] jogos [11, 3, 3, 5, 16, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [11, 7, 3, 1, 31, 9] jogos [11, 7, 3, 1, 30, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Hermann Aichinger tabela [11, 3, 3, 5, 16, 21] jogos [11, 3, 3, 5, 16, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Avaí tabela [22, 14, 4, 4, 60, 20] jogos [22, 14, 4, 4, 59, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Hermann Aichinger tabela [22, 6, 7, 9, 30, 38] jogos [22, 6, 7, 9, 30, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Marcílio Dias 1-5 Criciúma, ogol Criciúma 5-1 Marcílio Dias (2008-02-27); fica a RSSSF
- placar diferente no ogol — Criciúma x Figueirense (2008-05-04): RSSSF 3-1, ogol 3-2; fica o da RSSSF
- vencedor da final pelos jogos (Criciúma) diferente do campeão oficial (Figueirense); fica o oficial

### 2009

- placar diferente no ogol — Avaí x Chapecoense (2009-05-03): RSSSF 3-1, ogol 6-1; fica o da RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Avaí

### 2010

- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 6, 1, 2, 18, 12] jogos [18, 10, 4, 4, 34, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 5, 3, 1, 20, 11] jogos [18, 11, 4, 3, 39, 19] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Hermann Aichinger tabela [9, 5, 2, 2, 15, 10] jogos [18, 7, 6, 5, 24, 23] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 5, 0, 4, 10, 8] jogos [18, 8, 1, 9, 24, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 5, 0, 4, 16, 15] jogos [18, 8, 3, 7, 29, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 4, 2, 3, 18, 14] jogos [18, 9, 5, 4, 42, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 3, 2, 4, 13, 16] jogos [18, 6, 5, 7, 22, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 3, 0, 6, 12, 17] jogos [18, 7, 2, 9, 29, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 2, 2, 5, 14, 16] jogos [18, 3, 6, 9, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [9, 0, 2, 7, 6, 23] jogos [18, 2, 2, 14, 20, 47] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 6, 1, 2, 19, 8] jogos [24, 15, 6, 3, 52, 25] — a tabela conta 9 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 5, 3, 1, 24, 8] jogos [20, 9, 7, 4, 43, 23] — a tabela conta 9 jogos e as fontes trazem 20
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 4, 3, 2, 16, 16] jogos [23, 10, 7, 6, 38, 36] — a tabela conta 9 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 4, 2, 3, 17, 13] jogos [19, 7, 2, 10, 32, 34] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 3, 3, 3, 13, 15] jogos [18, 8, 3, 7, 29, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 3, 3, 3, 9, 14] jogos [18, 6, 5, 7, 22, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 3, 1, 5, 14, 18] jogos [19, 8, 2, 9, 26, 28] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Hermann Aichinger tabela [9, 2, 4, 3, 9, 13] jogos [19, 7, 6, 6, 24, 25] — a tabela conta 9 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 1, 4, 4, 9, 15] jogos [18, 3, 6, 9, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [9, 2, 0, 7, 14, 24] jogos [18, 2, 2, 14, 20, 47] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 6, 1, 2, 19, 8] jogos [18, 11, 4, 3, 39, 19] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 5, 3, 1, 24, 8] jogos [18, 9, 5, 4, 42, 22] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 4, 3, 2, 16, 16] jogos [18, 10, 4, 4, 34, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 4, 2, 3, 17, 13] jogos [18, 7, 2, 9, 29, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 3, 3, 3, 13, 15] jogos [18, 8, 3, 7, 29, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 3, 3, 3, 9, 14] jogos [18, 6, 5, 7, 22, 30] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 3, 1, 5, 14, 18] jogos [18, 8, 1, 9, 24, 26] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Hermann Aichinger tabela [9, 2, 4, 3, 9, 13] jogos [18, 7, 6, 5, 24, 23] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 1, 4, 4, 9, 15] jogos [18, 3, 6, 9, 23, 31] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [9, 2, 0, 7, 14, 24] jogos [18, 2, 2, 14, 20, 47] — a tabela conta 9 jogos e as fontes trazem 18
- vice pela Wikipédia (sem final de dois clubes): Joinville

### 2011

- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 4, 4, 1, 23, 12] jogos [18, 10, 6, 2, 45, 20] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 4, 3, 2, 18, 9] jogos [18, 7, 7, 4, 36, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 4, 3, 2, 18, 16] jogos [18, 11, 4, 3, 35, 23] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 4, 1, 4, 16, 20] jogos [18, 7, 6, 5, 34, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [9, 3, 4, 2, 15, 12] jogos [18, 4, 5, 9, 22, 27] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 3, 3, 3, 18, 17] jogos [18, 6, 5, 7, 27, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 3, 2, 4, 12, 12] jogos [18, 5, 5, 8, 24, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 3, 2, 4, 11, 15] jogos [18, 8, 3, 7, 30, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 2, 3, 4, 12, 18] jogos [18, 3, 6, 9, 20, 40] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Concórdia tabela [9, 1, 3, 5, 15, 27] jogos [18, 3, 5, 10, 24, 45] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 7, 1, 1, 17, 7] jogos [18, 11, 4, 3, 35, 23] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 6, 2, 1, 22, 8] jogos [18, 10, 6, 2, 45, 20] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 5, 1, 3, 19, 13] jogos [18, 8, 3, 7, 30, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 3, 5, 1, 18, 9] jogos [18, 7, 6, 5, 34, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 3, 4, 2, 18, 15] jogos [18, 7, 7, 4, 36, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 3, 2, 4, 9, 12] jogos [18, 6, 5, 7, 27, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 2, 3, 4, 12, 20] jogos [18, 5, 5, 8, 24, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Concórdia tabela [9, 2, 2, 5, 9, 18] jogos [18, 3, 5, 10, 24, 45] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 1, 3, 5, 8, 22] jogos [18, 3, 6, 9, 20, 40] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [9, 1, 1, 7, 7, 15] jogos [18, 4, 5, 9, 22, 27] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Chapecoense tabela [9, 7, 1, 1, 17, 7] jogos [18, 11, 4, 3, 35, 23] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Figueirense tabela [9, 6, 2, 1, 22, 8] jogos [18, 10, 6, 2, 45, 20] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Avaí tabela [9, 5, 1, 3, 19, 13] jogos [18, 8, 3, 7, 30, 28] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Joinville tabela [9, 3, 5, 1, 18, 9] jogos [18, 7, 6, 5, 34, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Criciúma tabela [9, 3, 4, 2, 18, 15] jogos [18, 7, 7, 4, 36, 24] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Brusque tabela [9, 3, 2, 4, 9, 12] jogos [18, 6, 5, 7, 27, 29] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Metropolitano tabela [9, 2, 3, 4, 12, 20] jogos [18, 5, 5, 8, 24, 32] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Concórdia tabela [9, 2, 2, 5, 9, 18] jogos [18, 3, 5, 10, 24, 45] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Imbituba tabela [9, 1, 3, 5, 8, 22] jogos [18, 3, 6, 9, 20, 40] — a tabela conta 9 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Marcílio Dias tabela [9, 1, 1, 7, 7, 15] jogos [18, 4, 5, 9, 22, 27] — a tabela conta 9 jogos e as fontes trazem 18
- placar corrigido pelo ogol — Metropolitano x Avaí (2011-01-30): RSSSF 2-2, ogol 0-0; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Marcílio Dias x Brusque (2011-01-30): RSSSF 0-0, ogol 2-2; fica o do ogol, que fecha com a tabela publicada
- vencedor da final pelos jogos (Criciúma) diferente do campeão oficial (Chapecoense); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Criciúma

### 2012

- sem ocorrências

### 2013

- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [9, 5, 3, 1, 25, 11] jogos [11, 6, 3, 2, 28, 14] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [9, 5, 2, 2, 18, 14] jogos [11, 6, 2, 3, 21, 17] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [9, 4, 3, 2, 16, 10] jogos [11, 4, 4, 3, 18, 13] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [9, 3, 4, 2, 6, 7] jogos [11, 4, 5, 2, 9, 9] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [9, 5, 3, 1, 25, 11] jogos [11, 6, 3, 2, 28, 14] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [9, 5, 2, 2, 18, 14] jogos [11, 6, 2, 3, 21, 17] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [9, 4, 3, 2, 16, 10] jogos [11, 4, 4, 3, 18, 13] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [9, 3, 4, 2, 6, 7] jogos [11, 4, 5, 2, 9, 9] — a tabela conta 9 jogos e as fontes trazem 11

### 2014

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Figueirense

### 2015

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Figueirense

### 2016

- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [5, 4, 1, 0, 15, 5] jogos [9, 4, 2, 3, 20, 14] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [5, 4, 1, 0, 8, 4] jogos [9, 7, 2, 0, 16, 6] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [5, 3, 0, 2, 8, 3] jogos [9, 5, 0, 4, 18, 9] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [5, 3, 0, 2, 8, 4] jogos [9, 5, 2, 2, 13, 6] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Metropolitano tabela [5, 2, 2, 1, 10, 7] jogos [9, 4, 2, 3, 15, 14] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Brusque tabela [5, 2, 1, 2, 8, 8] jogos [9, 3, 3, 3, 13, 14] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Camboriú tabela [5, 2, 1, 2, 7, 10] jogos [9, 2, 2, 5, 10, 20] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Guarani-SC tabela [5, 1, 1, 3, 7, 10] jogos [9, 4, 1, 4, 16, 16] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Internacional-SC tabela [5, 0, 1, 4, 4, 13] jogos [9, 2, 2, 5, 10, 18] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [5, 0, 0, 5, 1, 12] jogos [9, 1, 0, 8, 2, 16] — a tabela conta 5 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / -: Chapecoense tabela [13, 11, 2, 0, 25, 5] jogos [20, 12, 5, 3, 35, 18] — a tabela conta 13 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [13, 8, 2, 3, 21, 9] jogos [18, 10, 2, 6, 31, 17] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Brusque tabela [13, 5, 3, 5, 15, 17] jogos [18, 6, 6, 6, 23, 26] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Joinville tabela [13, 4, 6, 3, 15, 15] jogos [20, 8, 8, 4, 25, 19] — a tabela conta 13 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [13, 5, 2, 6, 16, 19] jogos [18, 6, 2, 10, 17, 24] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Figueirense tabela [13, 4, 3, 6, 13, 14] jogos [18, 7, 5, 6, 20, 16] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Internacional-SC tabela [13, 4, 3, 6, 17, 21] jogos [18, 6, 5, 7, 25, 28] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Metropolitano tabela [13, 4, 3, 6, 15, 22] jogos [18, 6, 4, 8, 22, 31] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Camboriú tabela [13, 3, 4, 6, 19, 22] jogos [18, 3, 6, 9, 24, 34] — a tabela conta 13 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Guarani-SC tabela [13, 1, 4, 8, 13, 25] jogos [18, 4, 5, 9, 24, 33] — a tabela conta 13 jogos e as fontes trazem 18
- jogo só no ogol, incluído em SECOND STAGE:: Guarani-SC 2-1 Criciúma (2016-04-02)
- jogo só no ogol, incluído em SECOND STAGE:: Figueirense 1-1 Chapecoense (2016-04-02)
- jogo só no ogol, incluído em SECOND STAGE:: Internacional-SC 3-1 Metropolitano (2016-04-03)
- jogo só no ogol, incluído em SECOND STAGE:: Joinville 1-0 Camboriú (2016-04-03)
- jogo só no ogol, incluído em SECOND STAGE:: Brusque 1-0 Avaí (2016-04-03)
- jogo só no ogol, incluído em SECOND STAGE:: Guarani-SC 4-2 Brusque (2016-04-09)
- jogo só no ogol, incluído em SECOND STAGE:: Criciúma 5-0 Camboriú (2016-04-09)
- jogo só no ogol, incluído em SECOND STAGE:: Figueirense 1-0 Avaí (2016-04-10)
- jogo só no ogol, incluído em SECOND STAGE:: Metropolitano 2-1 Chapecoense (2016-04-10)
- jogo só no ogol, incluído em SECOND STAGE:: Joinville 3-0 Internacional-SC (2016-04-10)
- jogo só no ogol, incluído em SECOND STAGE:: Chapecoense 1-3 Joinville (2016-04-17)
- jogo só no ogol, incluído em SECOND STAGE:: Brusque 1-1 Internacional-SC (2016-04-17)
- jogo só no ogol, incluído em SECOND STAGE:: Avaí 1-0 Guarani-SC (2016-04-19)
- jogo só no ogol, incluído em SECOND STAGE:: Camboriú 1-1 Figueirense (2016-04-19)
- jogo só no ogol, incluído em SECOND STAGE:: Metropolitano 2-1 Criciúma (2016-04-21)
- jogo só no ogol, incluído em SECOND STAGE:: Figueirense 2-0 Metropolitano (2016-04-23)
- jogo só no ogol, incluído em SECOND STAGE:: Guarani-SC 3-2 Camboriú (2016-04-23)
- jogo só no ogol, incluído em SECOND STAGE:: Joinville 1-1 Brusque (2016-04-24)
- jogo só no ogol, incluído em SECOND STAGE:: Criciúma 3-2 Chapecoense (2016-04-24)
- jogo só no ogol, incluído em SECOND STAGE:: Internacional-SC 2-0 Avaí (2016-04-24)
- jogo só no ogol, incluído em Final: Joinville 0-1 Chapecoense (2016-05-01)
- jogo só no ogol, incluído em Final: Chapecoense 1-1 Joinville (2016-05-08)

### 2017

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Chapecoense

### 2018

- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2019

- 3 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2020

- sem ocorrências

### 2021

- jogo anulado ou cancelado fica de fora: Hercílio Luz 0-0 Chapecoense (2021-04-25) [cancelled (3)]
- jogo anulado ou cancelado fica de fora: Chapecoense 1-0 Hercílio Luz (2021-04-28) [cancelled (3)]
- jogo do ogol tirado junto com o da RSSSF: Juventus Jaraguá 0-1 Marcílio Dias (2021-04-28)
- jogo do ogol tirado junto com o da RSSSF: Brusque 1-0 Joinville (2021-04-28)
- jogo só no ogol, incluído em QUARTERFINALS:: Chapecoense 1-0 Hercílio Luz (2021-04-29)
- só na RSSSF (não achado no ogol): Brusque 1-0 Joinville (2021-04-28)
- só na RSSSF (não achado no ogol): Juventus Jaraguá 0-1 Marcílio Dias (2021-04-28)

### 2022

- tabela publicada x jogos — Primeira fase / -: Barra-SC tabela [11, 3, 1, 7, 12, 14] jogos [12, 3, 1, 8, 12, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / -: Juventus Jaraguá tabela [11, 1, 4, 6, 7, 18] jogos [10, 1, 4, 5, 7, 16] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Final / -: Barra-SC tabela [11, 3, 1, 7, 12, 14] jogos [12, 3, 1, 8, 12, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — Final / -: Juventus Jaraguá tabela [11, 1, 4, 6, 7, 18] jogos [10, 1, 4, 5, 7, 16] — a tabela conta 11 jogos e as fontes trazem 10
- data diferente entre RSSSF e ogol (mais de 3 dias) em 37 jogos (ex.: Juventus Jaraguá x Avaí, ogol 2022-02-03); fica a do ogol
- adversário diferente no ogol — RSSSF Chapecoense 2-0 Barra-SC, ogol Chapecoense 2-0 Juventus Jaraguá (2022-01-30); fica a RSSSF
- jogo só no ogol, incluído em First Phase: Juventus Jaraguá 1-2 Brusque (2022-02-13)
- jogo só no ogol, incluído em First Phase: Brusque 3-1 Barra-SC (2022-02-20)
- jogo só no ogol, incluído em QUARTER-FINALS: Figueirense 1-1 Camboriú (2022-03-23)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Brusque

### 2023

- jogo só no ogol, incluído em Fase única: Criciúma 1-0 Figueirense (2023-02-25)
- jogo só no ogol, incluído em Fase única: Avaí 1-0 Concórdia (2023-02-25)
- jogo só no ogol, incluído em Fase única: Barra-SC 3-1 Marcílio Dias (2023-02-25)
- jogo só no ogol, incluído em Fase única: Chapecoense 3-1 Atlético Catarinense (2023-02-26)
- jogo só no ogol, incluído em Fase única: Hercílio Luz 1-0 Joinville (2023-02-26)
- jogo só no ogol, incluído em Fase única: Brusque 1-1 Camboriú (2023-02-26)
- jogo só no ogol, incluído em Fase única: Chapecoense 0-0 Brusque (2023-03-04)
- jogo só no ogol, incluído em Fase única: Marcílio Dias 1-2 Concórdia (2023-03-04)
- jogo só no ogol, incluído em Fase única: Joinville 3-0 Avaí (2023-03-05)
- jogo só no ogol, incluído em Fase única: Figueirense 1-1 Hercílio Luz (2023-03-05)
- jogo só no ogol, incluído em Fase única: Camboriú 2-2 Barra-SC (2023-03-05)
- jogo só no ogol, incluído em Fase única: Criciúma 2-0 Atlético Catarinense (2023-03-07)
- jogo só no ogol, incluído em Fase única: Avaí 2-2 Criciúma (2023-03-11)
- jogo só no ogol, incluído em Fase única: Brusque 3-2 Figueirense (2023-03-11)
- jogo só no ogol, incluído em Fase única: Concórdia 1-0 Joinville (2023-03-11)
- jogo só no ogol, incluído em Fase única: Barra-SC 0-0 Chapecoense (2023-03-11)
- jogo só no ogol, incluído em Fase única: Atlético Catarinense 1-2 Marcílio Dias (2023-03-11)
- jogo só no ogol, incluído em Fase única: Hercílio Luz 0-0 Camboriú (2023-03-11)
- jogo só no ogol, incluído em Quartas de final: Avaí 0-0 Criciúma (2023-03-18)
- jogo só no ogol, incluído em Quartas de final: Barra-SC 2-0 Chapecoense (2023-03-18)
- jogo só no ogol, incluído em Quartas de final: Concórdia 0-0 Brusque (2023-03-19)
- jogo só no ogol, incluído em Quartas de final: Figueirense 0-1 Hercílio Luz (2023-03-19)
- jogo só no ogol, incluído em Quartas de final: Criciúma 0-0 Avaí (2023-03-22)
- jogo só no ogol, incluído em Quartas de final: Hercílio Luz 0-0 Figueirense (2023-03-22)
- jogo só no ogol, incluído em Quartas de final: Brusque 2-0 Concórdia (2023-03-23)
- jogo só no ogol, incluído em Quartas de final: Chapecoense 1-2 Barra-SC (2023-03-24)
- jogo só no ogol, incluído em Semifinal: Criciúma 2-0 Hercílio Luz (2023-03-25)
- jogo só no ogol, incluído em Semifinal: Barra-SC 1-2 Brusque (2023-03-26)
- jogo só no ogol, incluído em Semifinal: Brusque 3-1 Barra-SC (2023-03-29)
- jogo só no ogol, incluído em Semifinal: Hercílio Luz 2-1 Criciúma (2023-03-30)
- jogo só no ogol, incluído em Final: Criciúma 1-0 Brusque (2023-04-01)
- jogo só no ogol, incluído em Final: Brusque 0-1 Criciúma (2023-04-08)

### 2024

- jogo só no ogol, incluído em Primeira fase: Criciúma 4-1 Figueirense (2024-01-20)
- jogo só no ogol, incluído em Primeira fase: Joinville 2-3 Marcílio Dias (2024-01-20)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 1-0 Hercílio Luz (2024-01-20)
- jogo só no ogol, incluído em Primeira fase: Internacional-SC 0-0 Concórdia (2024-01-21)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 1-3 Brusque (2024-01-21)
- jogo só no ogol, incluído em Primeira fase: Avaí 3-2 Nação (2024-01-21)
- jogo só no ogol, incluído em Primeira fase: Concórdia 1-2 Criciúma (2024-01-24)
- jogo só no ogol, incluído em Primeira fase: Figueirense 1-1 Joinville (2024-01-24)
- jogo só no ogol, incluído em Primeira fase: Brusque 0-0 Chapecoense (2024-01-24)
- jogo só no ogol, incluído em Primeira fase: Marcílio Dias 2-1 Internacional-SC (2024-01-25)
- jogo só no ogol, incluído em Primeira fase: Nação 0-4 Barra-SC (2024-01-25)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 2-1 Avaí (2024-01-26)
- jogo só no ogol, incluído em Primeira fase: Brusque 0-0 Figueirense (2024-01-27)
- jogo só no ogol, incluído em Primeira fase: Concórdia 3-2 Nação (2024-01-28)
- jogo só no ogol, incluído em Primeira fase: Joinville 2-1 Internacional-SC (2024-01-28)
- jogo só no ogol, incluído em Primeira fase: Avaí 3-2 Chapecoense (2024-01-28)
- jogo só no ogol, incluído em Primeira fase: Criciúma 2-0 Hercílio Luz (2024-01-28)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 1-0 Marcílio Dias (2024-01-28)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 2-2 Barra-SC (2024-01-31)
- jogo só no ogol, incluído em Primeira fase: Marcílio Dias 1-0 Criciúma (2024-01-31)
- jogo só no ogol, incluído em Primeira fase: Nação 1-0 Brusque (2024-01-31)
- jogo só no ogol, incluído em Primeira fase: Internacional-SC 2-3 Avaí (2024-02-01)
- jogo só no ogol, incluído em Primeira fase: Figueirense 2-0 Concórdia (2024-02-01)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 1-1 Joinville (2024-02-02)
- jogo só no ogol, incluído em Primeira fase: Avaí 2-2 Marcílio Dias (2024-02-03)
- jogo só no ogol, incluído em Primeira fase: Criciúma 1-0 Nação (2024-02-03)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 0-1 Figueirense (2024-02-04)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 3-3 Internacional-SC (2024-02-04)
- jogo só no ogol, incluído em Primeira fase: Brusque 1-1 Joinville (2024-02-04)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 0-1 Concórdia (2024-02-04)
- jogo só no ogol, incluído em Primeira fase: Concórdia 1-1 Brusque (2024-02-07)
- jogo só no ogol, incluído em Primeira fase: Marcílio Dias 2-1 Chapecoense (2024-02-07)
- jogo só no ogol, incluído em Primeira fase: Criciúma 1-0 Barra-SC (2024-02-07)
- jogo só no ogol, incluído em Primeira fase: Joinville 2-2 Avaí (2024-02-08)
- jogo só no ogol, incluído em Primeira fase: Internacional-SC 2-0 Nação (2024-02-08)
- jogo só no ogol, incluído em Primeira fase: Figueirense 0-0 Hercílio Luz (2024-02-08)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 2-3 Joinville (2024-02-10)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 3-0 Concórdia (2024-02-10)
- jogo só no ogol, incluído em Primeira fase: Nação 0-1 Figueirense (2024-02-11)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 2-0 Marcílio Dias (2024-02-11)
- jogo só no ogol, incluído em Primeira fase: Brusque 0-1 Internacional-SC (2024-02-11)
- jogo só no ogol, incluído em Primeira fase: Avaí 2-3 Criciúma (2024-02-12)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 2-1 Internacional-SC (2024-02-14)
- jogo só no ogol, incluído em Primeira fase: Criciúma 1-2 Brusque (2024-02-15)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 2-2 Nação (2024-02-15)
- jogo só no ogol, incluído em Primeira fase: Figueirense 1-2 Avaí (2024-02-17)
- jogo só no ogol, incluído em Primeira fase: Concórdia 0-1 Marcílio Dias (2024-02-17)
- jogo só no ogol, incluído em Primeira fase: Internacional-SC 0-1 Criciúma (2024-02-18)
- jogo só no ogol, incluído em Primeira fase: Brusque 1-1 Hercílio Luz (2024-02-18)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 1-1 Joinville (2024-02-18)
- jogo só no ogol, incluído em Primeira fase: Nação 1-3 Chapecoense (2024-02-19)
- jogo só no ogol, incluído em Primeira fase: Joinville 1-2 Concórdia (2024-02-21)
- jogo só no ogol, incluído em Primeira fase: Marcílio Dias 2-0 Figueirense (2024-02-22)
- jogo só no ogol, incluído em Primeira fase: Avaí 0-1 Brusque (2024-02-24)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 0-1 Figueirense (2024-02-24)
- jogo só no ogol, incluído em Primeira fase: Joinville 0-0 Criciúma (2024-02-24)
- jogo só no ogol, incluído em Primeira fase: Marcílio Dias 1-1 Nação (2024-02-24)
- jogo só no ogol, incluído em Primeira fase: Hercílio Luz 3-0 Concórdia (2024-02-25)
- jogo só no ogol, incluído em Primeira fase: Internacional-SC 0-2 Barra-SC (2024-02-25)
- jogo só no ogol, incluído em Primeira fase: Avaí 1-0 Barra-SC (2024-02-28)
- jogo só no ogol, incluído em Primeira fase: Figueirense 3-1 Internacional-SC (2024-03-02)
- jogo só no ogol, incluído em Primeira fase: Criciúma 2-0 Chapecoense (2024-03-02)
- jogo só no ogol, incluído em Primeira fase: Nação 1-3 Joinville (2024-03-02)
- jogo só no ogol, incluído em Primeira fase: Brusque 4-1 Marcílio Dias (2024-03-02)
- jogo só no ogol, incluído em Primeira fase: Concórdia 0-1 Avaí (2024-03-02)
- jogo só no ogol, incluído em Primeira fase: Barra-SC 1-0 Hercílio Luz (2024-03-02)
- jogo só no ogol, incluído em Quartas de final: Brusque 1-1 Marcílio Dias (2024-03-08)
- jogo só no ogol, incluído em Quartas de final: Joinville 1-1 Avaí (2024-03-09)
- jogo só no ogol, incluído em Quartas de final: Hercílio Luz 1-1 Criciúma (2024-03-09)
- jogo só no ogol, incluído em Quartas de final: Barra-SC 1-3 Figueirense (2024-03-10)
- jogo só no ogol, incluído em Quartas de final: Figueirense 1-3 Barra-SC (2024-03-15)
- jogo só no ogol, incluído em Quartas de final: Avaí 4-0 Joinville (2024-03-16)
- jogo só no ogol, incluído em Quartas de final: Marcílio Dias 0-0 Brusque (2024-03-17)
- jogo só no ogol, incluído em Quartas de final: Criciúma 2-1 Hercílio Luz (2024-03-17)
- jogo só no ogol, incluído em Semifinal: Brusque 2-0 Avaí (2024-03-20)
- jogo só no ogol, incluído em Semifinal: Barra-SC 2-1 Criciúma (2024-03-21)
- jogo só no ogol, incluído em Semifinal: Avaí 2-2 Brusque (2024-03-23)
- jogo só no ogol, incluído em Semifinal: Criciúma 2-1 Barra-SC (2024-03-24)
- jogo só no ogol, incluído em Final: Brusque 1-2 Criciúma (2024-03-30)
- jogo só no ogol, incluído em Final: Criciúma 1-1 Brusque (2024-04-06)

### 2025

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Avaí

### 2026

- tabela publicada x jogos — Segunda fase / -: Concórdia tabela [2, 0, 2, 0, 1, 1] jogos [4, 0, 3, 1, 3, 7] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Segunda fase / -: Santa Catarina tabela [2, 0, 1, 1, 1, 2] jogos [4, 0, 1, 3, 2, 7] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [2, 1, 0, 1, 2, 2] jogos [4, 3, 0, 1, 7, 3] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [2, 0, 1, 1, 1, 2] jogos [4, 1, 2, 1, 7, 4] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — Segunda fase / -: Criciúma tabela [2, 1, 1, 0, 6, 2] jogos [13, 6, 4, 3, 21, 15] — a tabela conta 2 jogos e as fontes trazem 13
- tabela publicada x jogos — Segunda fase / -: Concórdia tabela [2, 0, 1, 1, 2, 6] jogos [10, 2, 4, 4, 8, 17] — a tabela conta 2 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Avaí tabela [2, 2, 0, 0, 5, 1] jogos [11, 6, 1, 4, 15, 11] — a tabela conta 2 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Santa Catarina tabela [2, 0, 0, 2, 1, 5] jogos [10, 3, 4, 3, 12, 12] — a tabela conta 2 jogos e as fontes trazem 10
- tabela publicada x jogos — Terceira fase / -: Brusque tabela [2, 1, 0, 1, 1, 3] jogos [3, 1, 0, 2, 1, 4] — a tabela conta 2 jogos e as fontes trazem 3
- tabela publicada x jogos — Terceira fase / -: Camboriú tabela [2, 0, 1, 1, 1, 4] jogos [3, 1, 1, 1, 2, 4] — a tabela conta 2 jogos e as fontes trazem 3
- 2 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- vice pela Wikipédia (sem final de dois clubes): Chapecoense

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-sc1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
