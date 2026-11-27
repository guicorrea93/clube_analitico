# Campeonato Alagoano (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-al-1/importar.py`. Pacote em `data/coleta/bra-al-1/pacote/`. Mesmo código do
Pernambucano (`docs/coleta/bra-pe-1.md`), com as fontes de Alagoas.

**Temporadas:** 1918 a 2026, 105 edições (escopo aprovado pelo Guilherme em 27/11/2026; a conta da FAF): 1918-1926 são
os campeonatos da Liga, reconhecidos pela CBF em 2026. Ficam de fora 1931, 1932 e 1934 (suspensos), 1943 (não terminou)
e o Torneio Centenário de 1922. Título dividido: 1953 (ASA e Ferroviário). Edições sem página da RSSSF e sem jogos no
ogol entram só com campeão e vice.

**Fontes:** RSSSF Brasil (`tablesae/al{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada
edição, jogos a partir de 1995, e o código de cada clube); Wikipédia em português (artigo "Campeonato Alagoano de
Futebol Masculino": campeão e vice de cada ano, segunda fonte); lista de campeões da FAF.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1918 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1919 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1920 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1921 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1922 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1923 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1924 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1925 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1926 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1927 | RSSSF | 7 | 19 (0) | 85 | 2 | 0 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1929 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1930 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1933 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1935 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1936 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1937 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1938 | RSSSF | 6 | 31 (0) | 128 | 7 | 0 / 3 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1940 | RSSSF | 6 | 25 (0) | 135 | 0 | 0 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1942 | RSSSF | 4 | 18 (0) | 100 | 0 | 0 / 1 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1945 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1946 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1947 | RSSSF | 6 | 31 (0) | 172 | 2 | 3 / 0 | Alexandria | RSSSF (classificação geral publicada) |
| 1948 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1949 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1950 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1951 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1952 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1953 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1954 | RSSSF | 2 | 2 (0) | 9 | 0 | 0 / 0 | Ferroviário-AL | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1956 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1957 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1958 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1959 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1960 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1961 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1962 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1963 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1964 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1965 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1966 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1967 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1968 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1969 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1970 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1971 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1972 | RSSSF | 8 | 76 (0) | 248 | 0 | 4 / 0 | CRB | RSSSF (classificação geral publicada) |
| 1973 | RSSSF | 9 | 85 (0) | 212 | 0 | 2 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1975 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1976 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1977 | RSSSF | 8 | 103 (0) | 232 | 0 | 8 / 1 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1979 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1980 | RSSSF | 8 | 114 (0) | 282 | 1 | 7 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1982 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1983 | RSSSF | 9 | 126 (0) | 327 | 0 | 3 / 4 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 9 | 117 (0) | 308 | 0 | 3 / 4 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 8 | 15 (0) | 27 | 0 | 0 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 8 | 74 (0) | 153 | 0 | 6 / 4 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF | 10 | 146 (0) | 318 | 0 | 3 / 3 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 10 | 204 (0) | 433 | 0 | 0 / 4 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1990 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1991 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1992 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1993 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1994 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1995 | RSSSF + ogol | 10 | 202 (202) | 543 | 0 | 5 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 12 | 146 (146) | 376 | 0 | 5 / 5 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 10 | 119 (117) | 341 | 0 | 2 / 8 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 12 | 146 (146) | 467 | 0 | 3 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 12 | 140 (139) | 344 | 0 | 1 / 1 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 9 | 87 (87) | 221 | 0 | 2 / 0 | ASA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 8 | 72 (71) | 173 | 0 | 3 / 1 | ASA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 8 | 99 (95) | 267 | 0 | 1 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 8 | 62 (62) | 177 | 177 | 1 / 1 | ASA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 8 | 74 (72) | 221 | 24 | 1 / 2 | Corinthians-AL | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 9 | 128 (128) | 388 | 272 | 0 / 0 | ASA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 10 | 162 (162) | 444 | 403 | 0 / 1 | Coruripe | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 10 | 120 (120) | 342 | 336 | 2 / 1 | Coruripe | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 10 | 95 (93) | 294 | 272 | 2 / 4 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 10 | 116 (102) | 332 | 213 | 3 / 2 | ASA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 10 | 98 (98) | 303 | 0 | 3 / 0 | Murici | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 10 | 98 (98) | 300 | 26 | 2 / 0 | ASA | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 10 | 104 (104) | 313 | 3 | 4 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 10 | 104 (92) | 290 | 287 | 4 / 3 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 10 | 90 (90) | 230 | 73 | 1 / 0 | Coruripe | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 9 | 73 (73) | 172 | 152 | 1 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 10 | 83 (83) | 206 | 201 | 4 / 2 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 10 | 85 (85) | 199 | 199 | 8 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 9 | 42 (42) | 101 | 46 | 1 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 8 | 36 (36) | 99 | 89 | 5 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 8 | 34 (34) | 69 | 0 | 2 / 1 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 9 | 47 (46) | 107 | 0 | 0 / 2 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 8 | 39 (38) | 99 | 0 | 2 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 8 | 36 (36) | 89 | 0 | 0 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 8 | 36 (36) | 74 | 69 | 2 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 7 | 36 (36) | 62 | 0 | 0 / 1 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | RSSSF + ogol | 8 | 34 (34) | 70 | 70 | 4 / 0 | CRB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1918

- sem ocorrências

### 1919

- sem ocorrências

### 1920

- sem ocorrências

### 1921

- sem ocorrências

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

- tabela publicada x jogos — Fase única / -: CRB tabela [6, 6, 0, 0, 20, 1] jogos [5, 4, 1, 0, 20, 1] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase única / -: Tiradentes-AL tabela [6, 2, 1, 3, 4, 23] jogos [5, 1, 1, 3, 4, 23] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase única / -: Uruguai tabela [6, 0, 2, 4, 5, 14] jogos [6, 0, 3, 3, 5, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Flamengo-AL tabela [6, 0, 1, 5, 5, 17] jogos [4, 0, 1, 3, 5, 17] — a tabela conta 6 jogos e as fontes trazem 4
- tabela publicada x jogos — Fase única / -: CRB tabela [6, 6, 0, 0, 20, 1] jogos [5, 4, 1, 0, 20, 1] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase única / -: Tiradentes-AL tabela [6, 2, 1, 3, 4, 23] jogos [5, 1, 1, 3, 4, 23] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase única / -: Uruguai tabela [6, 0, 2, 4, 5, 14] jogos [6, 0, 3, 3, 5, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Flamengo-AL tabela [6, 0, 1, 5, 5, 17] jogos [4, 0, 1, 3, 5, 17] — a tabela conta 6 jogos e as fontes trazem 4
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Flamengo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Tiradentes
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uruguai
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vera Cruz
- Barroso — clube que o ogol não tem; entra só pela RSSSF
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- Flamengo — clube que o ogol não tem; entra só pela RSSSF
- Tiradentes — clube que o ogol não tem; entra só pela RSSSF
- Uruguai — clube que o ogol não tem; entra só pela RSSSF
- Vera Cruz — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, CRB; o 1º pela soma dos jogos da última fase é CSA (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1928

- sem ocorrências

### 1929

- sem ocorrências

### 1930

- sem ocorrências

### 1933

- sem ocorrências

### 1935

- sem ocorrências

### 1936

- sem ocorrências

### 1937

- sem ocorrências

### 1938

- tabela publicada x jogos — Primeira fase / -: CRB tabela [5, 4, 0, 1, 19, 3] jogos [5, 5, 0, 0, 19, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Desempate / -: CRB tabela [7, 5, 1, 1, 18, 7] jogos [5, 4, 0, 1, 14, 4] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — Desempate / -: CSA tabela [7, 4, 1, 2, 18, 14] jogos [5, 4, 0, 1, 15, 10] — a tabela conta 7 jogos e as fontes trazem 5
- tabela publicada x jogos — Fase final / -: CRB tabela [12, 9, 1, 2, 37, 10] jogos [12, 10, 1, 1, 37, 10] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nordeste
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco da Gama
- Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barroso)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- Nordeste — clube que o ogol não tem; entra só pela RSSSF
- Santa Cruz — clube que o ogol não tem; entra só pela RSSSF
- Vasco da Gama — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, CRB; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1939

- sem ocorrências

### 1940

- tabela publicada x jogos — 1º Turno / -: Barroso tabela [5, 2, 0, 3, 7, 12] jogos [5, 1, 0, 4, 5, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Santa Cruz-AL tabela [5, 0, 2, 3, 8, 20] jogos [5, 1, 2, 2, 11, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Nordeste tabela [5, 1, 3, 1, 13, 15] jogos [4, 0, 3, 1, 11, 15] — a tabela conta 5 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: Barroso tabela [3, 0, 0, 3, 0, 7] jogos [2, 0, 0, 2, 0, 5] — a tabela conta 3 jogos e as fontes trazem 2
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nordeste
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vasco da Gama
- Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barroso)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- Nordeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nordeste)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz-AL)
- Vasco da Gama — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vasco da Gama-AL)
- campeão pela lista oficial, CRB; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1941

- sem ocorrências

### 1942

- tabela publicada x jogos — Terceira fase / -: CRB tabela [9, 6, 0, 3, 28, 15] jogos [9, 6, 0, 3, 31, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Santa Cruz-AL tabela [9, 4, 1, 4, 24, 22] jogos [9, 4, 1, 4, 27, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / -: Barroso tabela [9, 0, 0, 9, 10, 41] jogos [9, 0, 0, 9, 10, 47] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Cruz
- Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barroso)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- Santa Cruz — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Cruz-AL)
- campeão pela lista oficial, CSA; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CRB

### 1944

- sem ocorrências

### 1945

- sem ocorrências

### 1946

- sem ocorrências

### 1947

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Alexandria
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Barroso
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comércio
- Alexandria — clube que o ogol não tem; entra só pela RSSSF
- Barroso — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barroso)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- Comércio — clube que o ogol não tem; entra só pela RSSSF

### 1948

- sem ocorrências

### 1949

- sem ocorrências

### 1950

- sem ocorrências

### 1951

- sem ocorrências

### 1952

- sem ocorrências

### 1953

- sem ocorrências

### 1954

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): 29 de Setembro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- 29 de Setembro — clube que o ogol não tem; entra só pela RSSSF
- Ferroviário — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, Ferroviário-AL; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): 29 de Setembro

### 1955

- sem ocorrências

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- sem ocorrências

### 1959

- sem ocorrências

### 1960

- sem ocorrências

### 1961

- sem ocorrências

### 1962

- sem ocorrências

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- sem ocorrências

### 1966

- sem ocorrências

### 1967

- sem ocorrências

### 1968

- sem ocorrências

### 1969

- sem ocorrências

### 1970

- sem ocorrências

### 1971

- sem ocorrências

### 1972

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dínamo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Dínamo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Dínamo EC-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Guarani — clube que o ogol não tem; entra só pela RSSSF
- campeão pela lista oficial, CRB; o 1º pela soma dos jogos da última fase é ? (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1973

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Dínamo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarani
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Dínamo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Dínamo EC-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Guarani — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guarani-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)

### 1974

- sem ocorrências

### 1975

- sem ocorrências

### 1976

- sem ocorrências

### 1977

- tabela publicada x jogos — 3º Turno - Segunda fase / -: São Domingos tabela [3, 1, 1, 1, 3, 3] jogos [3, 0, 3, 0, 3, 3] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Canavieiro
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Guarany
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Canavieiro — clube que o ogol não tem; entra só pela RSSSF
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Guarany — clube que o ogol não tem; entra só pela RSSSF
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- vencedor da final pelos jogos (CRB) diferente do campeão oficial (CSA); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): CRB

### 1981

- sem ocorrências

### 1982

- sem ocorrências

### 1983

- tabela publicada x jogos — Fase final / -: CRB tabela [3, 3, 0, 0, 4, 0] jogos [9, 7, 2, 0, 17, 4] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 1, 1, 1, 3, 2] jogos [9, 1, 4, 4, 7, 12] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 0, 2, 1, 1, 3] jogos [8, 1, 4, 3, 7, 14] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 0, 1, 2, 0, 3] jogos [8, 1, 4, 3, 5, 6] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 2, 1, 0, 7, 2] jogos [9, 7, 2, 0, 17, 4] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 1, 1, 1, 2] jogos [8, 1, 4, 3, 5, 6] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 1, 1, 1, 3, 3] jogos [8, 1, 4, 3, 7, 14] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 0, 1, 2, 0, 4] jogos [9, 1, 4, 4, 7, 12] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 2, 1, 0, 6, 2] jogos [9, 7, 2, 0, 17, 4] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 2, 0, 5, 1] jogos [8, 1, 4, 3, 5, 6] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 0, 2, 1, 4, 6] jogos [9, 1, 4, 4, 7, 12] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 0, 1, 2, 3, 9] jogos [8, 1, 4, 3, 7, 14] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSA tabela [34, 15, 12, 7, 67, 22] jogos [33, 14, 12, 7, 66, 22] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase final / -: ASA tabela [33, 15, 11, 7, 58, 38] jogos [32, 15, 11, 6, 58, 37] — a tabela conta 33 jogos e as fontes trazem 32
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Sebastião
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- São Sebastião — clube que o ogol não tem; entra só pela RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, CRB

### 1984

- tabela publicada x jogos — Fase final / -: CRB tabela [3, 3, 0, 0, 4, 0] jogos [9, 5, 2, 2, 17, 7] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 1, 1, 1, 3, 2] jogos [9, 0, 3, 6, 4, 17] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 0, 2, 1, 1, 3] jogos [8, 3, 2, 3, 10, 13] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 0, 1, 2, 0, 3] jogos [8, 4, 3, 1, 10, 4] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 2, 1, 0, 7, 2] jogos [9, 5, 2, 2, 17, 7] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 1, 1, 1, 2] jogos [8, 4, 3, 1, 10, 4] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 1, 1, 1, 3, 3] jogos [8, 3, 2, 3, 10, 13] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 0, 1, 2, 0, 4] jogos [9, 0, 3, 6, 4, 17] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 2, 1, 0, 6, 2] jogos [9, 5, 2, 2, 17, 7] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 2, 0, 5, 1] jogos [8, 4, 3, 1, 10, 4] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 0, 2, 1, 4, 6] jogos [9, 0, 3, 6, 4, 17] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 0, 1, 2, 3, 9] jogos [8, 3, 2, 3, 10, 13] — a tabela conta 3 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: CRB tabela [34, 24, 8, 2, 71, 14] jogos [33, 21, 9, 3, 69, 15] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase final / -: CSA tabela [34, 15, 12, 7, 67, 22] jogos [32, 18, 10, 4, 67, 13] — a tabela conta 34 jogos e as fontes trazem 32
- tabela publicada x jogos — Fase final / -: ASA tabela [33, 15, 11, 7, 58, 38] jogos [30, 15, 9, 6, 57, 33] — a tabela conta 33 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: CSE tabela [32, 13, 13, 6, 46, 29] jogos [30, 12, 8, 10, 38, 32] — a tabela conta 32 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: São Sebastião tabela [23, 8, 3, 12, 25, 47] jogos [15, 6, 1, 8, 17, 32] — a tabela conta 23 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Ferroviário-AL tabela [23, 5, 6, 12, 18, 33] jogos [22, 7, 3, 12, 20, 36] — a tabela conta 23 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Penedense tabela [23, 5, 5, 13, 19, 31] jogos [22, 4, 3, 15, 13, 34] — a tabela conta 23 jogos e as fontes trazem 22
- tabela publicada x jogos — Fase final / -: Capelense-AL tabela [22, 4, 5, 13, 15, 46] jogos [21, 3, 4, 14, 15, 54] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: São Domingos tabela [24, 1, 5, 18, 9, 68] jogos [23, 3, 3, 17, 12, 59] — a tabela conta 24 jogos e as fontes trazem 23
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Sebastião
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- São Sebastião — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Sebastião)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, CSA

### 1985

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- campeão pela lista oficial, CSA; o 1º pela soma dos jogos da última fase é CRB (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CRB

### 1986

- tabela publicada x jogos — Fase final / -: CSA tabela [3, 2, 1, 0, 6, 0] jogos [9, 4, 3, 2, 15, 8] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 1, 2, 0, 3, 0] jogos [9, 6, 3, 0, 14, 3] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 1, 0, 2, 2, 4] jogos [9, 2, 3, 4, 10, 13] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 3, 0, 0, 6, 1] jogos [9, 6, 3, 0, 14, 3] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 1, 1, 5, 4] jogos [9, 4, 3, 2, 15, 8] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 1, 0, 2, 3, 6] jogos [6, 1, 0, 5, 4, 12] — a tabela conta 3 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 0, 1, 2, 2, 5] jogos [9, 2, 3, 4, 10, 13] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [14, 10, 4, 0, 18, 2] jogos [23, 14, 7, 2, 33, 10] — a tabela conta 14 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase final / -: CRB tabela [14, 9, 5, 0, 22, 2] jogos [23, 15, 8, 0, 36, 5] — a tabela conta 14 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase final / -: CSE tabela [14, 8, 2, 4, 17, 15] jogos [23, 10, 5, 8, 27, 28] — a tabela conta 14 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase final / -: ASA tabela [14, 4, 5, 5, 19, 19] jogos [20, 5, 5, 10, 23, 31] — a tabela conta 14 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: CRB tabela [3, 2, 1, 0, 5, 2] jogos [9, 6, 3, 0, 14, 3] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSE tabela [3, 1, 2, 0, 6, 4] jogos [9, 2, 3, 4, 10, 13] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: CSA tabela [3, 1, 1, 1, 4, 4] jogos [9, 4, 3, 2, 15, 8] — a tabela conta 3 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: ASA tabela [3, 0, 0, 3, 1, 6] jogos [6, 1, 0, 5, 4, 12] — a tabela conta 3 jogos e as fontes trazem 6
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1987

- tabela publicada x jogos — 1º Turno / -: CSE tabela [9, 4, 2, 3, 9, 10] jogos [8, 3, 2, 3, 9, 10] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / -: Comercial-AL tabela [9, 2, 1, 6, 12, 13] jogos [8, 2, 1, 5, 12, 13] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno - Final / -: CRB tabela [18, 6, 9, 3, 20, 14] jogos [38, 20, 11, 7, 52, 28] — a tabela conta 18 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno - Final / -: CSA tabela [18, 6, 9, 3, 17, 14] jogos [34, 10, 15, 9, 27, 24] — a tabela conta 18 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno - Final / -: Penedense tabela [18, 6, 7, 5, 18, 18] jogos [33, 8, 8, 17, 29, 49] — a tabela conta 18 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno - Final / -: CSE tabela [18, 6, 7, 5, 16, 17] jogos [37, 14, 13, 10, 36, 32] — a tabela conta 18 jogos e as fontes trazem 37
- tabela publicada x jogos — 2º Turno - Final / -: Comercial-AL tabela [18, 7, 4, 7, 23, 21] jogos [32, 10, 8, 14, 38, 43] — a tabela conta 18 jogos e as fontes trazem 32
- tabela publicada x jogos — 2º Turno - Final / -: Capelense-AL tabela [18, 5, 8, 5, 20, 18] jogos [24, 5, 11, 8, 22, 27] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — 1º Turno / -: CRB tabela [10, 8, 0, 2, 15, 5] jogos [38, 20, 11, 7, 52, 28] — a tabela conta 10 jogos e as fontes trazem 38
- tabela publicada x jogos — 1º Turno / -: ASA tabela [10, 4, 3, 3, 16, 13] jogos [40, 22, 12, 6, 65, 33] — a tabela conta 10 jogos e as fontes trazem 40
- tabela publicada x jogos — 1º Turno / -: CSE tabela [10, 4, 3, 3, 9, 7] jogos [37, 14, 13, 10, 36, 32] — a tabela conta 10 jogos e as fontes trazem 37
- tabela publicada x jogos — 1º Turno / -: CSA tabela [10, 3, 3, 4, 6, 7] jogos [34, 10, 15, 9, 27, 24] — a tabela conta 10 jogos e as fontes trazem 34
- tabela publicada x jogos — 1º Turno / -: Comercial-AL tabela [9, 2, 3, 4, 7, 10] jogos [32, 10, 8, 14, 38, 43] — a tabela conta 9 jogos e as fontes trazem 32
- tabela publicada x jogos — 1º Turno / -: Penedense tabela [9, 2, 0, 7, 7, 18] jogos [33, 8, 8, 17, 29, 49] — a tabela conta 9 jogos e as fontes trazem 33
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- campeão pela lista oficial, CRB; o 1º pela soma dos jogos da última fase é CSE (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CSE

### 1988

- tabela publicada x jogos — 2º Turno / -: Comercial-AL tabela [18, 11, 4, 3, 20, 14] jogos [17, 11, 3, 3, 20, 14] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: CSE tabela [18, 9, 7, 2, 24, 8] jogos [16, 9, 5, 2, 24, 8] — a tabela conta 18 jogos e as fontes trazem 16
- tabela publicada x jogos — 2º Turno / -: São Domingos tabela [18, 7, 6, 5, 14, 11] jogos [17, 7, 5, 5, 14, 11] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Penedense tabela [18, 5, 6, 7, 15, 16] jogos [17, 5, 5, 7, 15, 16] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: CSA tabela [18, 5, 3, 10, 14, 19] jogos [17, 5, 2, 10, 14, 19] — a tabela conta 18 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase final / -: ASA tabela [6, 2, 3, 1, 4, 3] jogos [12, 2, 8, 2, 13, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: São Domingos tabela [6, 1, 5, 0, 6, 5] jogos [15, 4, 6, 5, 18, 16] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: CSE tabela [6, 1, 5, 0, 5, 4] jogos [15, 3, 7, 5, 18, 23] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: CSA tabela [18, 9, 6, 3, 19, 14] jogos [45, 21, 10, 14, 51, 43] — a tabela conta 18 jogos e as fontes trazem 45
- tabela publicada x jogos — 2º Turno / -: São Domingos tabela [18, 9, 5, 4, 24, 15] jogos [50, 20, 16, 14, 56, 42] — a tabela conta 18 jogos e as fontes trazem 50
- tabela publicada x jogos — 2º Turno / -: CRB tabela [18, 8, 6, 4, 23, 10] jogos [39, 17, 9, 13, 43, 31] — a tabela conta 18 jogos e as fontes trazem 39
- tabela publicada x jogos — 2º Turno / -: CSE tabela [18, 8, 6, 4, 21, 20] jogos [48, 20, 17, 11, 63, 51] — a tabela conta 18 jogos e as fontes trazem 48
- tabela publicada x jogos — 2º Turno / -: ASA tabela [18, 7, 8, 3, 20, 11] jogos [47, 21, 19, 7, 60, 33] — a tabela conta 18 jogos e as fontes trazem 47
- tabela publicada x jogos — 2º Turno / -: Capelense-AL tabela [18, 7, 6, 5, 16, 13] jogos [35, 14, 9, 12, 38, 27] — a tabela conta 18 jogos e as fontes trazem 35
- tabela publicada x jogos — 2º Turno / -: Penedense tabela [17, 6, 3, 8, 20, 19] jogos [33, 11, 7, 15, 35, 35] — a tabela conta 17 jogos e as fontes trazem 33
- tabela publicada x jogos — 2º Turno / -: Comercial-AL tabela [18, 4, 7, 7, 16, 18] jogos [41, 15, 13, 13, 39, 38] — a tabela conta 18 jogos e as fontes trazem 41
- tabela publicada x jogos — 2º Turno / -: Ferroviário-AL tabela [17, 4, 6, 7, 20, 22] jogos [34, 7, 12, 15, 37, 52] — a tabela conta 17 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-AL tabela [18, 0, 1, 17, 8, 45] jogos [36, 0, 4, 32, 11, 81] — a tabela conta 18 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: CSA tabela [12, 6, 4, 2, 0, 13] jogos [45, 21, 10, 14, 51, 43] — a tabela conta 12 jogos e as fontes trazem 45
- tabela publicada x jogos — Fase final / -: São Domingos tabela [6, 3, 1, 2, 7, 6] jogos [50, 20, 16, 14, 56, 42] — a tabela conta 6 jogos e as fontes trazem 50
- tabela publicada x jogos — Fase final / -: ASA tabela [6, 0, 5, 1, 9, 10] jogos [47, 21, 19, 7, 60, 33] — a tabela conta 6 jogos e as fontes trazem 47
- tabela publicada x jogos — Fase final / -: CSE tabela [6, 0, 2, 4, 8, 14] jogos [48, 20, 17, 11, 63, 51] — a tabela conta 6 jogos e as fontes trazem 48
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ASA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Capelense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Penedense
- ASA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ASA)
- CRB — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRB)
- CSA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSA)
- CSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CSE)
- Capelense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capelense-AL)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-AL)
- Penedense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penedense)
- vice pela Wikipédia (sem final de dois clubes): São Domingos

### 1989

- sem ocorrências

### 1990

- sem ocorrências

### 1991

- sem ocorrências

### 1992

- sem ocorrências

### 1993

- sem ocorrências

### 1994

- sem ocorrências

### 1995

- placar diferente no ogol — CSA x CRB (1995-08-15): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): CSA

### 1996

- tabela publicada x jogos — 2º Turno / -: CRB tabela [6, 5, 1, 0, 13, 4] jogos [8, 5, 2, 1, 15, 7] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / -: ASA tabela [6, 5, 1, 0, 14, 2] jogos [8, 6, 2, 0, 17, 4] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno - Segunda fase / Grupo A: CSE tabela [5, 1, 2, 2, 4, 9] jogos [5, 1, 2, 2, 5, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: CRB tabela [22, 16, 5, 1, 48, 13] jogos [34, 22, 7, 5, 59, 22] — a tabela conta 22 jogos e as fontes trazem 34
- tabela publicada x jogos — 2º Turno / -: CSA tabela [22, 14, 5, 3, 55, 25] jogos [30, 19, 5, 6, 69, 30] — a tabela conta 22 jogos e as fontes trazem 30
- tabela publicada x jogos — 2º Turno / -: Miguelense tabela [22, 13, 2, 7, 33, 19] jogos [22, 13, 2, 7, 33, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Comercial-AL tabela [22, 8, 8, 6, 32, 37] jogos [22, 8, 8, 6, 32, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: ASA tabela [22, 7, 8, 7, 33, 30] jogos [26, 8, 10, 8, 36, 33] — a tabela conta 22 jogos e as fontes trazem 26
- tabela publicada x jogos — 2º Turno / -: Batalhense tabela [22, 6, 8, 8, 26, 29] jogos [22, 6, 8, 8, 22, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Cruzeiro-AL tabela [22, 5, 10, 7, 25, 32] jogos [24, 5, 10, 9, 26, 43] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: Sporting FC tabela [22, 6, 5, 11, 20, 38] jogos [24, 6, 5, 13, 20, 42] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno / -: CSE tabela [22, 2, 6, 14, 16, 45] jogos [22, 2, 6, 14, 17, 46] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: CSA tabela [30, 19, 5, 6, 69, 25] jogos [30, 19, 5, 6, 69, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: CRB tabela [34, 22, 7, 5, 60, 22] jogos [34, 22, 7, 5, 59, 22] — placar diverge entre RSSSF e ogol em CRB x Sporting FC (3-0 x 0-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Miguelense tabela [22, 13, 2, 7, 31, 18] jogos [22, 13, 2, 7, 33, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: ASA tabela [26, 9, 9, 8, 34, 30] jogos [26, 8, 10, 8, 36, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Comercial-AL tabela [22, 8, 7, 7, 31, 27] jogos [22, 8, 8, 6, 32, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Zumbi tabela [22, 6, 9, 7, 25, 23] jogos [22, 5, 9, 8, 24, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Capela tabela [22, 6, 9, 7, 18, 23] jogos [22, 7, 8, 7, 19, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Batalhense tabela [22, 6, 8, 8, 23, 27] jogos [22, 6, 8, 8, 22, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Sporting FC tabela [24, 5, 6, 13, 20, 43] jogos [24, 6, 5, 13, 20, 42] — placar diverge entre RSSSF e ogol em CRB x Sporting FC (3-0 x 0-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Bom Jesus-AL tabela [22, 2, 8, 12, 19, 41] jogos [22, 2, 8, 12, 19, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de CRB x ASA na 2. Turno - First Phase sempre na mesma ordem) — ogol ASA 2-1 CRB (1996-06-16)
- mando invertido no ogol — RSSSF CRB 1-0 CSA, ogol CSA 0-1 CRB (1996-07-17); fica a RSSSF
- mando invertido no ogol — RSSSF CRB 1-0 ASA, ogol ASA 0-1 CRB (1996-07-24); fica a RSSSF
- mando invertido no ogol — RSSSF CRB 0-2 CSA, ogol CSA 2-0 CRB (1996-07-28); fica a RSSSF
- placar diferente no ogol — CRB x Sporting FC (1996-04-07): RSSSF 3-0, ogol 0-3; fica o da RSSSF

### 1997

- tabela publicada x jogos — 2º Turno / Grupo A: CSA tabela [4, 2, 2, 0, 14, 5] jogos [7, 4, 2, 1, 21, 10] — a tabela conta 4 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo A: Comercial-AL tabela [4, 2, 1, 1, 8, 2] jogos [7, 4, 2, 1, 14, 4] — a tabela conta 4 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo A: Zumbi tabela [4, 1, 1, 2, 10, 14] jogos [7, 1, 3, 3, 17, 22] — a tabela conta 4 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo A: Dínamo EC-AL tabela [4, 1, 1, 2, 2, 12] jogos [7, 1, 1, 5, 3, 21] — a tabela conta 4 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / Grupo A: Miguelense tabela [4, 0, 3, 1, 5, 6] jogos [8, 2, 4, 2, 15, 13] — a tabela conta 4 jogos e as fontes trazem 8
- tabela publicada x jogos — 2º Turno / Grupo B: ASA tabela [4, 3, 1, 0, 8, 4] jogos [5, 4, 1, 0, 13, 6] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: CRB tabela [4, 2, 0, 2, 9, 7] jogos [5, 3, 0, 2, 10, 7] — a tabela conta 4 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: Capela tabela [4, 2, 0, 2, 5, 5] jogos [6, 1, 0, 5, 4, 9] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / Grupo B: São Domingos tabela [4, 1, 1, 2, 3, 10] jogos [6, 2, 1, 3, 6, 11] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 1º Turno / -: Comercial-AL tabela [5, 4, 0, 1, 9, 7] jogos [21, 10, 6, 5, 34, 23] — a tabela conta 5 jogos e as fontes trazem 21
- tabela publicada x jogos — 1º Turno / -: CSA tabela [5, 3, 1, 1, 13, 6] jogos [38, 22, 7, 9, 78, 48] — a tabela conta 5 jogos e as fontes trazem 38
- tabela publicada x jogos — 1º Turno / -: Miguelense tabela [5, 2, 2, 1, 6, 5] jogos [22, 8, 7, 7, 36, 31] — a tabela conta 5 jogos e as fontes trazem 22
- tabela publicada x jogos — 1º Turno / -: Zumbi tabela [5, 1, 3, 1, 6, 7] jogos [17, 3, 9, 5, 26, 33] — a tabela conta 5 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: Dínamo EC-AL tabela [5, 1, 0, 4, 5, 14] jogos [17, 4, 2, 11, 11, 40] — a tabela conta 5 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: CRB tabela [5, 3, 1, 1, 8, 6] jogos [42, 21, 10, 11, 63, 44] — a tabela conta 5 jogos e as fontes trazem 42
- tabela publicada x jogos — 1º Turno / -: ASA tabela [5, 2, 3, 0, 12, 4] jogos [27, 9, 12, 6, 40, 26] — a tabela conta 5 jogos e as fontes trazem 27
- tabela publicada x jogos — 1º Turno / -: Capela tabela [5, 1, 2, 2, 6, 8] jogos [17, 3, 4, 10, 15, 25] — a tabela conta 5 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: São Domingos tabela [5, 0, 0, 5, 4, 13] jogos [18, 3, 1, 14, 12, 43] — a tabela conta 5 jogos e as fontes trazem 18
- tabela publicada x jogos — 2º Turno / -: Comercial-AL tabela [3, 2, 1, 0, 6, 2] jogos [21, 10, 6, 5, 34, 23] — a tabela conta 3 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Miguelense tabela [4, 2, 1, 1, 10, 7] jogos [22, 8, 7, 7, 36, 31] — a tabela conta 4 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: CSA tabela [3, 2, 0, 1, 7, 5] jogos [38, 22, 7, 9, 78, 48] — a tabela conta 3 jogos e as fontes trazem 38
- tabela publicada x jogos — 2º Turno / -: Zumbi tabela [3, 0, 2, 1, 7, 8] jogos [17, 3, 9, 5, 26, 33] — a tabela conta 3 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / -: Dínamo EC-AL tabela [3, 0, 0, 3, 1, 9] jogos [17, 4, 2, 11, 11, 40] — a tabela conta 3 jogos e as fontes trazem 17
- tabela publicada x jogos — 2º Turno / Grupo B: ASA tabela [3, 2, 1, 0, 8, 4] jogos [5, 4, 1, 0, 13, 6] — a tabela conta 3 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: CRB tabela [3, 2, 1, 0, 4, 2] jogos [5, 3, 0, 2, 10, 7] — a tabela conta 3 jogos e as fontes trazem 5
- tabela publicada x jogos — 2º Turno / Grupo B: São Domingos tabela [4, 1, 0, 3, 3, 9] jogos [6, 2, 1, 3, 6, 11] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — 2º Turno / Grupo B: Capela tabela [3, 0, 0, 3, 1, 4] jogos [6, 1, 0, 5, 4, 9] — a tabela conta 3 jogos e as fontes trazem 6
- placar diferente no ogol — CSA x CRB (1997-06-18): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — CSA x Miguelense (1997-04-13): RSSSF 2-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — ASA x CRB (1997-04-13): RSSSF 1-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — CRB x CSA (1997-06-14): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Comercial-AL x ASA, ogol 1997-03-26); fica a do ogol
- jogo só no ogol, incluído em 2. Turno - Semifinals: CRB 1-0 ASA (1997-05-28)
- jogo só no ogol, incluído em 2. Turno - Semifinals: ASA 1-2 CRB (1997-05-28)
- só na RSSSF (não achado no ogol): CRB 0-1 CSA (None)
- só na RSSSF (não achado no ogol): CSA 1-1 CRB (None)

### 1998

- placar diferente no ogol — São Domingos x ASA (1998-04-22): RSSSF 0-2, ogol 0-1; fica o da RSSSF
- mando invertido no ogol — RSSSF CSA 2-2 CRB, ogol CRB 2-2 CSA (1998-06-21); fica a RSSSF

### 1999

- tabela publicada x jogos — Semifinal / -: Miguelense tabela [19, 11, 8, 0, 32, 14] jogos [28, 13, 11, 4, 42, 28] — a tabela conta 19 jogos e as fontes trazem 28
- tabela publicada x jogos — Semifinal / -: CSA tabela [19, 8, 8, 3, 29, 18] jogos [27, 12, 12, 3, 40, 21] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — Semifinal / -: CRB tabela [20, 8, 7, 5, 36, 25] jogos [25, 10, 9, 6, 40, 28] — a tabela conta 20 jogos e as fontes trazem 25
- tabela publicada x jogos — Semifinal / -: Murici tabela [20, 7, 10, 3, 14, 11] jogos [21, 7, 10, 4, 14, 12] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Semifinal / -: Corinthians-AL tabela [19, 8, 6, 5, 26, 19] jogos [24, 9, 7, 8, 33, 28] — a tabela conta 19 jogos e as fontes trazem 24
- tabela publicada x jogos — Semifinal / -: Jaciobá tabela [20, 8, 2, 10, 24, 28] jogos [22, 8, 4, 10, 25, 29] — a tabela conta 20 jogos e as fontes trazem 22
- tabela publicada x jogos — Semifinal / -: ASA tabela [19, 7, 5, 7, 26, 24] jogos [21, 8, 6, 7, 31, 24] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — Semifinal / -: Comercial-AL tabela [20, 6, 6, 8, 24, 29] jogos [22, 7, 7, 8, 28, 30] — a tabela conta 20 jogos e as fontes trazem 22
- tabela publicada x jogos — Semifinal / -: Capela tabela [19, 6, 5, 8, 22, 22] jogos [22, 7, 6, 9, 28, 29] — a tabela conta 19 jogos e as fontes trazem 22
- tabela publicada x jogos — Semifinal / -: Zumbi tabela [19, 5, 5, 9, 27, 37] jogos [22, 6, 7, 9, 31, 40] — a tabela conta 19 jogos e as fontes trazem 22
- tabela publicada x jogos — Semifinal / -: Sporting FC tabela [20, 6, 1, 13, 17, 36] jogos [22, 6, 2, 14, 18, 42] — a tabela conta 20 jogos e as fontes trazem 22
- tabela publicada x jogos — Semifinal / -: CSE tabela [20, 3, 5, 12, 14, 28] jogos [22, 3, 5, 14, 14, 33] — a tabela conta 20 jogos e as fontes trazem 22
- placar diferente no ogol — CSE x Corinthians-AL (1999-02-28): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 11 jogos (ex.: ASA x CSE, ogol 1999-05-25); fica a do ogol
- só na RSSSF (não achado no ogol): ASA None-None Murici (1999-07-10)

### 2000

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, ASA

### 2001

- tabela publicada x jogos — Primeira fase / -: Penedense tabela [14, 7, 4, 3, 14, 11] jogos [15, 7, 5, 3, 15, 12] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Corinthians-AL tabela [14, 5, 7, 2, 19, 16] jogos [15, 5, 8, 2, 20, 17] — a tabela conta 14 jogos e as fontes trazem 15
- placar diferente no ogol — Corinthians-AL x Penedense (2001-04-29): RSSSF 1-1, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Penedense x Corinthians-AL (2001-06-17): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Corinthians-AL x ASA (2001-06-24): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Corinthians-AL x ASA (2001-05-27): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Penedense x Corinthians-AL (2001-05-27): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 22 jogos (ex.: Murici x Corinthians-AL, ogol 2001-04-18); fica a do ogol
- jogo só no ogol, incluído em First Phase: Corinthians-AL 1-1 Penedense (2001-04-18)
- só na RSSSF (não achado no ogol): Corinthians-AL 3-0 Penedense (2001-07-12)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 2002

- tabela publicada x jogos — Segunda fase / -: Bom Jesus-AL tabela [13, 5, 3, 5, 14, 21] jogos [14, 5, 3, 6, 15, 23] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Segunda fase / -: Capela tabela [13, 5, 2, 6, 17, 19] jogos [14, 6, 2, 6, 19, 20] — a tabela conta 13 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: CRB tabela [6, 5, 1, 0, 10, 4] jogos [6, 5, 1, 0, 11, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Capela x Bom Jesus-AL, ogol 2002-06-05); fica a do ogol
- só na RSSSF (não achado no ogol): Capela 2-1 Bom Jesus-AL (2002-05-11)
- só na RSSSF (não achado no ogol): Murici None-None Penedense (2002-06-09)
- só na RSSSF (não achado no ogol): Bom Jesus-AL None-None Capela (2002-06-09)
- só na RSSSF (não achado no ogol): Corinthians-AL None-None Murici (2002-06-29)
- vice pela Wikipédia (sem final de dois clubes): CSA

### 2003

- tabela publicada x jogos — Fase final / -: ASA tabela [18, 9, 3, 6, 36, 23] jogos [18, 9, 3, 6, 37, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 20 jogos (ex.: CSE x Murici, ogol 2003-02-14); fica a do ogol

### 2004

- tabela publicada x jogos — Primeira fase / -: CRB tabela [7, 6, 0, 1, 15, 7] jogos [24, 12, 2, 10, 50, 36] — a tabela conta 7 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: Coruripe tabela [7, 4, 2, 1, 16, 10] jogos [26, 16, 6, 4, 45, 35] — a tabela conta 7 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / -: Corinthians-AL tabela [7, 4, 1, 2, 14, 6] jogos [22, 12, 3, 7, 35, 23] — a tabela conta 7 jogos e as fontes trazem 22
- tabela publicada x jogos — Primeira fase / -: ASA tabela [7, 4, 1, 2, 12, 8] jogos [18, 6, 4, 8, 25, 27] — a tabela conta 7 jogos e as fontes trazem 18
- tabela publicada x jogos — Primeira fase / -: Murici tabela [7, 3, 1, 3, 7, 13] jogos [14, 5, 4, 5, 18, 22] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Bom Jesus-AL tabela [7, 2, 1, 4, 11, 14] jogos [16, 5, 5, 6, 21, 26] — a tabela conta 7 jogos e as fontes trazem 16
- tabela publicada x jogos — Primeira fase / -: CSE tabela [7, 1, 1, 5, 8, 17] jogos [14, 2, 3, 9, 17, 30] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Primeira fase / -: Capela tabela [7, 0, 1, 6, 7, 15] jogos [14, 0, 5, 9, 10, 22] — a tabela conta 7 jogos e as fontes trazem 14
- tabela publicada x jogos — Coruripe win Second Stage / -: CRB tabela [14, 10, 0, 4, 29, 16] jogos [14, 10, 0, 4, 29, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Coruripe win Second Stage / -: Bom Jesus-AL tabela [14, 5, 4, 5, 18, 20] jogos [14, 5, 4, 5, 18, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Corinthians-AL x Coruripe (2004-03-03): RSSSF 1-2, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Corinthians-AL x Coruripe, ogol 2004-05-15); fica a do ogol
- só na RSSSF (não achado no ogol): ASA 1-2 Coruripe (2004-04-21)
- só na RSSSF (não achado no ogol): Coruripe 2-1 ASA (2004-04-25)

### 2005

- jogo só no ogol, incluído em First Phase: CSE 2-2 Murici (2005-02-13)
- jogo só no ogol, incluído em First Phase: ASA 2-5 CRB (2005-02-13)
- jogo só no ogol, incluído em First Phase: CSE 2-2 CRB (2005-02-19)
- jogo só no ogol, incluído em First Phase: ASA 2-0 Dimensão Saúde (2005-02-19)
- jogo só no ogol, incluído em First Phase: CRB 2-0 Penedense (2005-02-22)
- jogo só no ogol, incluído em First Phase: ASA 2-0 CSE (2005-02-24)
- jogo só no ogol, incluído em First Phase: CRB 1-2 Dimensão Saúde (2005-02-24)
- jogo só no ogol, incluído em First Phase: CSE 2-3 Coruripe (2005-02-27)
- jogo só no ogol, incluído em First Phase: CRB 1-1 Bom Jesus-AL (2005-03-05)
- jogo só no ogol, incluído em First Phase: CSE 1-0 Corinthians-AL (2005-03-05)
- jogo só no ogol, incluído em First Phase: ASA 3-0 Corinthians-AL (2005-03-10)
- jogo só no ogol, incluído em First Phase: ASA 4-3 Penedense (2005-03-13)
- jogo só no ogol, incluído em First Phase: CSE 2-1 Dimensão Saúde (2005-03-13)
- jogo só no ogol, incluído em First Phase: CRB 1-1 Coruripe (2005-03-13)
- jogo só no ogol, incluído em First Phase: CRB 1-0 ASA (2005-03-16)
- jogo só no ogol, incluído em First Phase: CRB 2-0 CSE (2005-03-20)
- jogo só no ogol, incluído em First Phase: ASA 2-0 Coruripe (2005-03-23)
- jogo só no ogol, incluído em First Phase: CSE 1-2 ASA (2005-03-26)
- jogo só no ogol, incluído em First Phase: ASA 3-0 Bom Jesus-AL (2005-03-30)
- jogo só no ogol, incluído em Second Phase: CRB 5-1 Bom Jesus-AL (2005-03-31)
- jogo só no ogol, incluído em Second Phase: ASA 2-0 Penedense (2005-04-02)
- jogo só no ogol, incluído em Second Phase: CRB 1-1 ASA (2005-04-06)
- jogo só no ogol, incluído em Second Phase: ASA 1-1 CRB (2005-04-10)
- jogo só no ogol, incluído em First Phase: CSE 1-1 ASA (2005-04-29)
- jogo só no ogol, incluído em First Phase: CSE 1-1 Coruripe (2005-05-01)
- jogo só no ogol, incluído em First Phase: ASA 2-2 Penedense (2005-05-05)
- jogo só no ogol, incluído em First Phase: ASA 3-2 Murici (2005-05-08)
- jogo só no ogol, incluído em First Phase: CSE 1-2 Penedense (2005-05-09)
- jogo só no ogol, incluído em First Phase: ASA 3-1 Bom Jesus-AL (2005-05-12)
- jogo só no ogol, incluído em First Phase: CSE 1-0 Bom Jesus-AL (2005-05-19)
- jogo só no ogol, incluído em First Phase: ASA 0-0 CSE (2005-05-22)
- jogo só no ogol, incluído em First Phase: ASA 2-1 Corinthians-AL (2005-05-27)
- jogo só no ogol, incluído em First Phase: CSE 3-2 Murici (2005-05-29)
- jogo só no ogol, incluído em First Phase: ASA 4-1 Coruripe (2005-06-08)
- jogo só no ogol, incluído em First Phase: CSE 1-2 Corinthians-AL (2005-06-08)
- jogo só no ogol, incluído em Second Phase: ASA 2-0 Penedense (2005-06-16)
- jogo só no ogol, incluído em Second Phase Finals: ASA 1-1 Coruripe (2005-06-22)
- jogo só no ogol, incluído em Second Stage Decision: ASA 0-0 Coruripe (2005-06-29)
- vice pela Wikipédia (sem final de dois clubes): Coruripe

### 2006

- tabela publicada x jogos — Primeira fase / -: CSA tabela [18, 10, 5, 3, 29, 16] jogos [42, 21, 12, 9, 62, 40] — a tabela conta 18 jogos e as fontes trazem 42
- placar diferente no ogol — Murici x Corinthians-AL (2006-03-02): RSSSF 2-3, ogol 2-4; fica o da RSSSF
- jogo só no ogol, incluído em First Phase: CRB 3-0 Bom Jesus-AL (2006-01-15)
- jogo só no ogol, incluído em First Phase: CSE 1-0 Murici (2006-01-15)
- jogo só no ogol, incluído em First Phase: ASA 0-2 Penedense (2006-01-15)
- jogo só no ogol, incluído em First Phase: Penedense 2-1 CRB (2006-01-25)
- jogo só no ogol, incluído em First Phase: Coruripe 1-2 Murici (2006-01-25)
- jogo só no ogol, incluído em First Phase: Ipanema-AL 0-1 Bom Jesus-AL (2006-01-25)
- jogo só no ogol, incluído em First Phase: CSA 1-0 CSE (2006-01-25)
- jogo só no ogol, incluído em First Phase: ASA 2-3 Corinthians-AL (2006-01-25)
- jogo só no ogol, incluído em First Phase: Penedense 1-2 CSA (2006-01-29)
- jogo só no ogol, incluído em First Phase: CRB 2-0 Ipanema-AL (2006-01-29)
- jogo só no ogol, incluído em First Phase: Corinthians-AL 0-1 Murici (2006-01-29)
- jogo só no ogol, incluído em First Phase: CSE 2-0 Bom Jesus-AL (2006-01-29)
- jogo só no ogol, incluído em First Phase: ASA 1-1 Coruripe (2006-01-29)

### 2007

- tabela publicada x jogos — Primeira fase / -: ASA tabela [28, 8, 12, 8, 46, 49] jogos [28, 8, 12, 8, 46, 50] — placar diverge entre RSSSF e ogol em Corinthians-AL x ASA (3-3 x 2-3) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Igaci tabela [18, 5, 5, 8, 25, 30] jogos [18, 5, 5, 8, 24, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Corinthians-AL x ASA (2007-04-28): RSSSF 3-3, ogol 2-3; fica o da RSSSF
- vice pela Wikipédia (sem final de dois clubes): Corinthians-AL

### 2008

- tabela publicada x jogos — Primeira fase / -: ASA tabela [24, 10, 8, 6, 45, 29] jogos [28, 10, 10, 8, 46, 34] — a tabela conta 24 jogos e as fontes trazem 28
- tabela publicada x jogos — Primeira fase / -: CSA tabela [22, 10, 5, 7, 37, 25] jogos [24, 12, 5, 7, 42, 26] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Primeira fase / -: CRB tabela [18, 5, 9, 4, 37, 30] jogos [19, 6, 10, 3, 34, 26] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Ipanema-AL tabela [16, 6, 3, 7, 24, 33] jogos [17, 5, 4, 8, 20, 30] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Primeira fase / -: Igaci tabela [18, 5, 5, 8, 15, 22] jogos [18, 5, 5, 8, 21, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Coruripe tabela [18, 5, 5, 8, 33, 29] jogos [19, 6, 5, 8, 33, 29] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: Santa Rita tabela [16, 4, 3, 9, 29, 42] jogos [17, 5, 3, 9, 29, 42] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / Grupo A: Corinthians-AL tabela [6, 3, 2, 1, 16, 8] jogos [8, 5, 2, 1, 17, 9] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / Grupo A: ASA tabela [6, 2, 2, 2, 10, 8] jogos [8, 2, 4, 2, 10, 8] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — 1º Turno / Grupo A: Ipanema-AL tabela [6, 2, 2, 2, 10, 14] jogos [7, 1, 3, 3, 6, 11] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 1º Turno / Grupo A: CRB tabela [6, 0, 4, 2, 13, 15] jogos [7, 1, 5, 1, 10, 11] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — 2º Turno / -: Coruripe tabela [8, 3, 1, 4, 15, 15] jogos [9, 4, 1, 4, 15, 15] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / -: Santa Rita tabela [8, 1, 3, 4, 15, 20] jogos [17, 5, 3, 9, 29, 42] — a tabela conta 8 jogos e as fontes trazem 17
- jogo anulado ou cancelado fica de fora: CRB 3-4 Ipanema (2008-01-20) [(Cancelled)]
- jogo do ogol tirado junto com o da RSSSF: CRB 3-4 Ipanema (2008-01-20)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: ASA x Corinthians-AL, ogol 2008-03-02); fica a do ogol
- só na RSSSF (não achado no ogol): Santa Rita 2-1 Penedense (2008-03-13)
- só na RSSSF (não achado no ogol): Coruripe 2-1 Penedense (2008-03-16)

### 2009

- tabela publicada x jogos — 2º Turno / -: Coruripe tabela [10, 4, 0, 6, 14, 13] jogos [12, 5, 0, 7, 16, 15] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — 2º Turno / -: CSA tabela [10, 3, 1, 6, 13, 20] jogos [14, 4, 1, 9, 18, 29] — a tabela conta 10 jogos e as fontes trazem 14
- tabela publicada x jogos — 2º Turno / -: Ipanema-AL tabela [10, 3, 0, 7, 9, 16] jogos [11, 3, 0, 8, 9, 18] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 2º Turno / -: Capelense-AL tabela [10, 2, 1, 7, 12, 22] jogos [13, 3, 1, 9, 16, 29] — a tabela conta 10 jogos e as fontes trazem 13
- tabela publicada x jogos — 2º Turno / -: Igaci tabela [10, 7, 1, 2, 20, 11] jogos [23, 9, 3, 11, 30, 31] — a tabela conta 10 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: ASA tabela [10, 6, 1, 3, 21, 16] jogos [31, 18, 5, 8, 55, 38] — a tabela conta 10 jogos e as fontes trazem 31
- tabela publicada x jogos — 2º Turno / -: CRB tabela [10, 6, 1, 3, 15, 12] jogos [20, 11, 3, 6, 33, 28] — a tabela conta 10 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / -: Murici tabela [10, 5, 0, 5, 17, 13] jogos [22, 11, 2, 9, 36, 28] — a tabela conta 10 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno / -: CSE tabela [10, 4, 1, 5, 14, 16] jogos [20, 7, 4, 9, 28, 32] — a tabela conta 10 jogos e as fontes trazem 20
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Corinthians-AL x ASA, ogol 2009-03-12); fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 3-1 ASA: RSSSF 2008-02-26, ogol 2009-02-26; fica a do ogol
- ano errado na data da RSSSF — Murici 0-0 Corinthians-AL: RSSSF 2008-02-26, ogol 2009-02-26; fica a do ogol
- ano errado na data da RSSSF — ASA 3-1 Ipanema-AL: RSSSF 2008-03-01, ogol 2009-03-01; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 3-0 Murici: RSSSF 2008-03-01, ogol 2009-03-01; fica a do ogol
- ano errado na data da RSSSF — ASA 1-2 Corinthians-AL: RSSSF 2008-03-08, ogol 2009-03-08; fica a do ogol
- ano errado na data da RSSSF — CSA 1-2 Igaci: RSSSF 2008-03-14, ogol 2009-03-14; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 2-1 Murici: RSSSF 2008-03-15, ogol 2009-03-15; fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 1-2 ASA: RSSSF 2008-03-15, ogol 2009-03-15; fica a do ogol
- ano errado na data da RSSSF — Coruripe 3-0 CSE: RSSSF 2008-03-15, ogol 2009-03-15; fica a do ogol
- ano errado na data da RSSSF — Capelense-AL 0-2 CRB: RSSSF 2008-03-15, ogol 2009-03-15; fica a do ogol
- ano errado na data da RSSSF — CRB 2-2 Corinthians-AL: RSSSF 2008-03-21, ogol 2009-03-21; fica a do ogol
- ano errado na data da RSSSF — Igaci 2-0 Ipanema-AL: RSSSF 2008-03-22, ogol 2009-03-22; fica a do ogol
- ano errado na data da RSSSF — CSE 1-1 CSA: RSSSF 2008-03-22, ogol 2009-03-22; fica a do ogol
- ano errado na data da RSSSF — Murici 2-1 Coruripe: RSSSF 2008-03-22, ogol 2009-03-22; fica a do ogol
- ano errado na data da RSSSF — ASA 3-0 Capelense-AL: RSSSF 2008-03-22, ogol 2009-03-22; fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 2-1 CSE: RSSSF 2008-03-25, ogol 2009-03-25; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 1-0 Igaci: RSSSF 2008-03-25, ogol 2009-03-25; fica a do ogol
- ano errado na data da RSSSF — Coruripe 1-0 CRB: RSSSF 2008-03-25, ogol 2009-03-25; fica a do ogol
- ano errado na data da RSSSF — CSA 2-1 ASA: RSSSF 2008-03-25, ogol 2009-03-25; fica a do ogol
- ano errado na data da RSSSF — Capelense-AL 1-0 Murici: RSSSF 2008-03-25, ogol 2009-03-25; fica a do ogol
- ano errado na data da RSSSF — CRB 2-0 Ipanema-AL: RSSSF 2008-03-28, ogol 2009-03-28; fica a do ogol
- ano errado na data da RSSSF — Igaci 3-2 Capelense-AL: RSSSF 2008-03-28, ogol 2009-03-28; fica a do ogol
- ano errado na data da RSSSF — CSE 0-1 Corinthians-AL: RSSSF 2008-03-28, ogol 2009-03-28; fica a do ogol
- ano errado na data da RSSSF — ASA 1-3 Coruripe: RSSSF 2008-03-28, ogol 2009-03-28; fica a do ogol
- ano errado na data da RSSSF — Murici 3-0 CSA: RSSSF 2008-03-29, ogol 2009-03-29; fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 0-2 Murici: RSSSF 2008-04-02, ogol 2009-04-02; fica a do ogol
- ano errado na data da RSSSF — Capelense-AL 1-2 CSE: RSSSF 2008-04-02, ogol 2009-04-02; fica a do ogol
- ano errado na data da RSSSF — ASA 2-1 Ipanema-AL: RSSSF 2008-04-04, ogol 2009-04-04; fica a do ogol
- ano errado na data da RSSSF — Murici 1-4 Corinthians-AL: RSSSF 2008-04-05, ogol 2009-04-05; fica a do ogol
- ano errado na data da RSSSF — CSE 3-2 Coruripe: RSSSF 2008-04-05, ogol 2009-04-05; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 3-4 ASA: RSSSF 2008-04-08, ogol 2009-04-08; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 1-0 CRB: RSSSF 2008-04-16, ogol 2009-04-16; fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 0-2 Igaci: RSSSF 2008-04-16, ogol 2009-04-16; fica a do ogol
- ano errado na data da RSSSF — CRB 2-1 Coruripe: RSSSF 2008-04-19, ogol 2009-04-19; fica a do ogol
- ano errado na data da RSSSF — Igaci 3-0 Corinthians-AL: RSSSF 2008-04-19, ogol 2009-04-19; fica a do ogol
- ano errado na data da RSSSF — Ipanema-AL 4-1 CRB: RSSSF 2008-04-26, ogol 2009-04-26; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 4-3 CSE: RSSSF 2008-04-26, ogol 2009-04-26; fica a do ogol
- ano errado na data da RSSSF — Coruripe 1-2 ASA: RSSSF 2008-04-26, ogol 2009-04-26; fica a do ogol
- ano errado na data da RSSSF — Capelense-AL 4-4 Igaci: RSSSF 2008-04-26, ogol 2009-04-26; fica a do ogol
- ano errado na data da RSSSF — CSA 3-2 Murici: RSSSF 2008-04-26, ogol 2009-04-26; fica a do ogol
- ano errado na data da RSSSF — ASA 2-2 Corinthians-AL: RSSSF 2008-05-03, ogol 2009-05-03; fica a do ogol
- ano errado na data da RSSSF — Murici 0-1 Ipanema-AL: RSSSF 2008-05-03, ogol 2009-05-03; fica a do ogol
- ano errado na data da RSSSF — CRB 2-1 CSA: RSSSF 2008-05-03, ogol 2009-05-03; fica a do ogol
- ano errado na data da RSSSF — Igaci 1-0 Coruripe: RSSSF 2008-05-03, ogol 2009-05-03; fica a do ogol
- ano errado na data da RSSSF — CSE 1-0 Capelense-AL: RSSSF 2008-05-03, ogol 2009-05-03; fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 1-2 Coruripe: RSSSF 2008-05-10, ogol 2009-05-10; fica a do ogol
- ano errado na data da RSSSF — Igaci 1-2 ASA: RSSSF 2008-05-10, ogol 2009-05-10; fica a do ogol
- jogo só no ogol, incluído em Second Stage - First Phase: CSA 1-2 CRB (2009-04-03)
- jogo só no ogol, incluído em Second Stage - First Phase: Coruripe 2-1 Igaci (2009-04-03)
- jogo só no ogol, incluído em Second Stage - First Phase: Igaci 2-1 CSA (2009-04-14)
- jogo só no ogol, incluído em Second Stage - First Phase: CRB 2-1 Capelense-AL (2009-04-14)
- jogo só no ogol, incluído em Second Stage - First Phase: CSA 2-1 CSE (2009-04-17)
- jogo só no ogol, incluído em Second Stage - First Phase: Capelense-AL 2-0 ASA (2009-04-17)
- jogo só no ogol, incluído em Second Stage - First Phase: Coruripe 0-1 Murici (2009-04-17)
- jogo só no ogol, incluído em Second Stage - First Phase: Murici 5-1 Capelense-AL (2009-04-19)
- jogo só no ogol, incluído em Second Stage - First Phase: ASA 4-1 CSA (2009-04-19)
- jogo só no ogol, incluído em Second Stage - First Phase: CSE 2-0 Ipanema-AL (2009-04-21)
- jogo só no ogol, incluído em Second Stage - Semifinal: Coruripe 1-0 Corinthians-AL (2009-05-07)
- jogo só no ogol, incluído em Second Stage - Semifinal: ASA 1-0 Igaci (2009-05-08)
- jogo só no ogol, incluído em Second Stage - Final: Coruripe 0-0 ASA (2009-05-14)
- jogo só no ogol, incluído em Second Stage - Final: ASA 2-2 Coruripe (2009-05-24)
- só na RSSSF (não achado no ogol): Coruripe 2-1 Igaci (2008-04-02)
- só na RSSSF (não achado no ogol): CSA 1-2 CRB (2008-04-11)
- só na RSSSF (não achado no ogol): Igaci 2-1 CSA (2008-04-13)
- só na RSSSF (não achado no ogol): CRB 2-1 Capelense-AL (2008-04-13)
- só na RSSSF (não achado no ogol): CSA 2-1 CSE (2008-04-16)
- só na RSSSF (não achado no ogol): Capelense-AL 2-0 ASA (2008-04-16)
- só na RSSSF (não achado no ogol): Coruripe 0-1 Murici (2008-04-16)
- só na RSSSF (não achado no ogol): Murici 5-1 Capelense-AL (2008-04-18)
- só na RSSSF (não achado no ogol): ASA 4-1 CSA (2008-04-18)
- só na RSSSF (não achado no ogol): CSE 2-0 Ipanema-AL (2008-04-20)
- só na RSSSF (não achado no ogol): Coruripe 1-0 Corinthians-AL (2008-05-06)
- só na RSSSF (não achado no ogol): ASA 1-0 Igaci (2008-05-07)
- só na RSSSF (não achado no ogol): Coruripe 0-0 ASA (2008-05-13)
- só na RSSSF (não achado no ogol): ASA 2-2 Coruripe (2008-05-17)
- campeão pela lista oficial, ASA; o 1º pela soma dos jogos da última fase é Coruripe (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): Corinthians-AL

### 2010

- placar diferente no ogol — Ipanema-AL x Santa Rita (2010-02-28): RSSSF 2-1, ogol 1-2; fica o da RSSSF

### 2011

- placar diferente no ogol — Ipanema-AL x Sport Atalaia (2011-02-02): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Santa Rita x Ipanema-AL (2011-02-09): RSSSF 4-1, ogol 4-0; fica o da RSSSF

### 2012

- tabela publicada x jogos — 2º Turno - Final / -: CSA tabela [18, 11, 3, 4, 33, 15] jogos [22, 12, 5, 5, 36, 19] — a tabela conta 18 jogos e as fontes trazem 22
- tabela publicada x jogos — 2º Turno - Final / -: ASA tabela [18, 10, 4, 4, 30, 21] jogos [28, 13, 10, 5, 49, 31] — a tabela conta 18 jogos e as fontes trazem 28
- tabela publicada x jogos — 2º Turno - Final / -: CRB tabela [18, 9, 3, 6, 29, 21] jogos [24, 11, 7, 6, 41, 27] — a tabela conta 18 jogos e as fontes trazem 24
- tabela publicada x jogos — 2º Turno - Final / -: Corinthians-AL tabela [18, 7, 5, 6, 35, 31] jogos [20, 7, 6, 7, 36, 37] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno - Final / -: Murici tabela [18, 6, 6, 6, 25, 23] jogos [20, 6, 7, 7, 26, 29] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno - Final / -: Sport Atalaia tabela [18, 6, 5, 7, 27, 28] jogos [20, 6, 6, 8, 29, 31] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno - Final / -: CSE tabela [18, 6, 4, 8, 32, 30] jogos [20, 6, 5, 9, 35, 36] — a tabela conta 18 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: CRB tabela [24, 12, 6, 6, 41, 27] jogos [24, 11, 7, 6, 41, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: ASA tabela [28, 13, 9, 6, 49, 31] jogos [28, 13, 10, 5, 49, 31] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2013

- tabela publicada x jogos — Semifinal / -: CRB tabela [10, 6, 2, 2, 19, 7] jogos [12, 6, 4, 2, 21, 9] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: CSA tabela [10, 4, 5, 1, 16, 11] jogos [12, 5, 5, 2, 17, 12] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: ASA tabela [10, 4, 2, 4, 16, 16] jogos [12, 5, 2, 5, 17, 17] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: CEO tabela [10, 4, 1, 5, 10, 18] jogos [12, 4, 3, 5, 12, 20] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: CRB tabela [10, 6, 2, 2, 19, 7] jogos [12, 6, 4, 2, 21, 9] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: CSA tabela [10, 4, 5, 1, 16, 11] jogos [12, 5, 5, 2, 17, 12] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: ASA tabela [10, 4, 2, 4, 16, 16] jogos [12, 5, 2, 5, 17, 17] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Semifinal / -: CEO tabela [10, 4, 1, 5, 10, 18] jogos [12, 4, 3, 5, 12, 20] — a tabela conta 10 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: CRB tabela [14, 7, 4, 3, 26, 12] jogos [14, 7, 4, 3, 25, 12] — placar diverge entre RSSSF e ogol em CRB x CEO (1-1 x 2-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase final / -: CSA tabela [28, 12, 9, 7, 44, 32] jogos [28, 12, 9, 7, 43, 32] — placar diverge entre RSSSF e ogol em CSA x ASA (0-1 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Murici 1-0 Corinthians-AL, ogol Corinthians-AL 0-1 Murici (2013-04-07); fica a RSSSF
- placar diferente no ogol — CRB x CEO (2013-05-04): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — CSA x ASA (2013-05-05): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: CEO x ASA, ogol 2013-04-03); fica a do ogol
- ano errado na data da RSSSF — Corinthians-AL 2-2 CRB: RSSSF 2013-03-09, ogol 2023-03-09; fica a do ogol
- só na RSSSF (não achado no ogol): CSE 4-0 União-AL (2013-03-09)
- só na RSSSF (não achado no ogol): Sport Atalaia 1-1 Comercial-AL (2013-03-10)
- só na RSSSF (não achado no ogol): União-AL 1-0 Sport Atalaia (2013-03-13)
- só na RSSSF (não achado no ogol): Comercial-AL 5-2 CSE (2013-03-13)
- só na RSSSF (não achado no ogol): Sport Atalaia 1-3 CSE (2013-03-17)
- só na RSSSF (não achado no ogol): Comercial-AL 2-0 União-AL (2013-03-17)
- só na RSSSF (não achado no ogol): União-AL 0-2 Comercial-AL (2013-03-20)
- só na RSSSF (não achado no ogol): CSE 1-1 Sport Atalaia (2013-03-20)
- só na RSSSF (não achado no ogol): Sport Atalaia 0-2 União-AL (2013-03-24)
- só na RSSSF (não achado no ogol): CSE 3-2 Comercial-AL (2013-03-24)
- só na RSSSF (não achado no ogol): União-AL 1-1 CSE (2013-03-24)
- só na RSSSF (não achado no ogol): Comercial-AL 4-2 Sport Atalaia (2013-03-24)

### 2014

- jogo só no ogol, incluído em Semifinal: Murici 3-1 ASA (2014-02-05)
- jogo só no ogol, incluído em Semifinal: Coruripe 2-1 Santa Rita (2014-02-06)
- jogo só no ogol, incluído em Semifinal: ASA 1-0 Murici (2014-02-08)
- jogo só no ogol, incluído em Semifinal: Santa Rita 3-1 Coruripe (2014-02-09)
- jogo só no ogol, incluído em Final: Murici 1-0 Santa Rita (2014-02-12)
- jogo só no ogol, incluído em Final: Santa Rita 0-1 Murici (2014-02-15)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CEO 1-1 Comercial-AL (2014-02-19)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Penedense 0-1 CSE (2014-02-19)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Murici 0-2 Santa Rita (2014-02-19)
- jogo só no ogol, incluído em Primeira fase / Grupo B: CSA 1-1 CRB (2014-02-19)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Coruripe 0-2 ASA (2014-02-19)
- jogo só no ogol, incluído em Primeira fase / Grupo B: ASA 3-2 CSA (2014-02-22)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Comercial-AL 1-3 Coruripe (2014-02-23)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Santa Rita 1-1 CEO (2014-02-23)
- jogo só no ogol, incluído em Primeira fase / Grupo B: CRB 3-0 Penedense (2014-02-23)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CSE 1-0 Murici (2014-02-23)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Coruripe 1-1 CRB (2014-03-08)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CSA 7-1 CSE (2014-03-08)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Murici 1-1 Comercial-AL (2014-03-08)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Penedense 1-1 Santa Rita (2014-03-09)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CEO 0-0 ASA (2014-03-09)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Comercial-AL 0-2 CSA (2014-03-15)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Santa Rita 0-0 Coruripe (2014-03-16)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: ASA 4-3 Penedense (2014-03-16)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CSE 4-0 CEO (2014-03-16)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CRB 2-0 Murici (2014-03-17)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Penedense 1-1 Comercial-AL (2014-03-19)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CSA 2-2 Santa Rita (2014-03-19)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Coruripe 0-1 CSE (2014-03-19)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CEO 0-3 CRB (2014-03-20)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Murici 2-1 ASA (2014-03-20)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Santa Rita 0-0 CSA (2014-03-22)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Comercial-AL 2-1 Penedense (2014-03-23)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: ASA 0-1 Murici (2014-03-23)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CSE 1-3 Coruripe (2014-03-23)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CRB 1-0 CEO (2014-03-23)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CSA 3-0 Comercial-AL (2014-03-26)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Murici 0-1 CRB (2014-03-26)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Coruripe 4-1 Santa Rita (2014-03-26)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Penedense 2-1 ASA (2014-03-26)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CEO 1-0 CSE (2014-03-26)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CSE 2-0 CSA (2014-03-29)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Comercial-AL 2-2 Murici (2014-03-30)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Santa Rita 1-2 Penedense (2014-03-30)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CRB 0-1 Coruripe (2014-03-30)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: ASA 3-2 CEO (2014-03-30)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Penedense 2-2 CRB (2014-04-05)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CEO 1-2 Santa Rita (2014-04-06)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CSA 0-3 ASA (2014-04-06)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Coruripe 2-1 Comercial-AL (2014-04-06)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Murici 2-0 CSE (2014-04-06)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Comercial-AL 0-3 CEO (2014-04-13)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: CSE 4-1 Penedense (2014-04-13)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: Santa Rita 1-4 Murici (2014-04-13)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CRB 1-0 CSA (2014-04-13)
- jogo só no ogol, incluído em Top 4 qualify for Semifinals: ASA 2-1 Coruripe (2014-04-13)
- jogo só no ogol, incluído em Semifinal: ASA 0-2 CRB (2014-04-17)
- jogo só no ogol, incluído em Semifinal: Murici 0-0 Coruripe (2014-04-17)
- jogo só no ogol, incluído em Semifinal: Coruripe 1-0 Murici (2014-04-19)
- jogo só no ogol, incluído em Semifinal: CRB 0-2 ASA (2014-04-21)
- jogo só no ogol, incluído em Final: Coruripe 2-1 CRB (2014-04-26)
- jogo só no ogol, incluído em Final: CRB 0-0 Coruripe (2014-05-01)
- vencedor da final pelos jogos (Murici) diferente do campeão oficial (Coruripe); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): CRB

### 2015

- tabela publicada x jogos — Segunda fase / -: CSA tabela [10, 3, 3, 4, 9, 9] jogos [11, 3, 3, 5, 9, 10] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Coruripe tabela [10, 3, 1, 6, 12, 17] jogos [11, 4, 1, 6, 13, 17] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: CEO tabela [10, 2, 2, 6, 4, 14] jogos [10, 2, 2, 6, 5, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: CSE tabela [8, 5, 2, 1, 11, 8] jogos [8, 5, 2, 1, 11, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Santa Rita tabela [8, 4, 1, 3, 12, 8] jogos [8, 4, 1, 3, 12, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: CEO x Murici, ogol 2015-04-17); fica a do ogol
- jogo só no ogol, incluído em SECOND STAGE - Maceió Cup:: Coruripe 1-0 CSA (2015-04-25)
- jogo só no ogol, incluído em Semifinal: CRB 2-0 ASA (2015-04-26)
- jogo só no ogol, incluído em Semifinal: CSA 1-2 Coruripe (2015-04-28)
- jogo só no ogol, incluído em Semifinal: ASA 2-1 CRB (2015-04-30)
- jogo só no ogol, incluído em Final: Coruripe 1-1 CRB (2015-05-03)
- jogo só no ogol, incluído em Final: CRB 2-0 Coruripe (2015-05-07)
- vice pela Wikipédia (sem final de dois clubes): Coruripe

### 2016

- tabela publicada x jogos — Semifinal / -: CSA tabela [5, 4, 0, 1, 8, 4] jogos [7, 5, 1, 1, 12, 7] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: Coruripe tabela [5, 2, 1, 2, 5, 5] jogos [7, 3, 1, 3, 6, 7] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: CRB tabela [5, 2, 1, 2, 6, 7] jogos [7, 3, 1, 3, 8, 8] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: Murici tabela [5, 2, 1, 2, 5, 6] jogos [7, 2, 2, 3, 8, 10] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: CSA tabela [5, 4, 0, 1, 8, 4] jogos [7, 5, 1, 1, 12, 7] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: Coruripe tabela [5, 2, 1, 2, 5, 5] jogos [7, 3, 1, 3, 6, 7] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: CRB tabela [5, 2, 1, 2, 6, 7] jogos [7, 3, 1, 3, 8, 8] — a tabela conta 5 jogos e as fontes trazem 7
- tabela publicada x jogos — Semifinal / -: Murici tabela [5, 2, 1, 2, 5, 6] jogos [7, 2, 2, 3, 8, 10] — a tabela conta 5 jogos e as fontes trazem 7
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Ipanema-AL x CSA, ogol 2016-02-28); fica a do ogol
- jogo só no ogol, incluído em Final: CSA 0-1 CRB (2016-05-08)

### 2017

- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: CSA x Coruripe, ogol 2017-03-19); fica a do ogol

### 2018

- jogo só no ogol, incluído em FIRST STAGE:: ASA 1-0 Santa Rita (2018-02-15)
- jogo só no ogol, incluído em FIRST STAGE:: Coruripe 1-0 ASA (2018-02-17)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Rita 1-2 CEO (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 1-1 Murici (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE:: CSA 5-0 Dimensão Saúde (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE:: Coruripe 1-2 Santa Rita (2018-02-24)
- jogo só no ogol, incluído em FIRST STAGE:: Murici 2-1 ASA (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE:: CRB 2-1 CSE (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE:: CEO 0-2 CSA (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 0-1 Coruripe (2018-03-04)
- jogo só no ogol, incluído em FIRST STAGE:: CRB 1-0 CSA (2018-03-04)
- jogo só no ogol, incluído em FIRST STAGE:: Murici 1-1 Dimensão Saúde (2018-03-04)
- jogo só no ogol, incluído em FIRST STAGE:: ASA 2-1 CEO (2018-03-04)
- jogo só no ogol, incluído em FIRST STAGE:: Santa Rita 1-3 Murici (2018-03-07)
- jogo só no ogol, incluído em FIRST STAGE:: Dimensão Saúde 4-1 CSE (2018-03-07)
- jogo só no ogol, incluído em FIRST STAGE:: ASA 1-2 CRB (2018-03-08)
- jogo só no ogol, incluído em FIRST STAGE:: CSA 1-0 Coruripe (2018-03-08)
- jogo só no ogol, incluído em Semifinal: ASA 1-0 CSA (2018-03-15)
- jogo só no ogol, incluído em Semifinal: Coruripe 1-2 CRB (2018-03-18)
- jogo só no ogol, incluído em Semifinal: CSA 2-1 ASA (2018-03-24)
- jogo só no ogol, incluído em Semifinal: CRB 2-0 Coruripe (2018-03-25)
- jogo só no ogol, incluído em Final: CSA 0-1 CRB (2018-04-01)
- jogo só no ogol, incluído em Final: CRB 0-2 CSA (2018-04-08)

### 2019

- sem ocorrências

### 2020

- tabela publicada x jogos — Fase final / -: Murici tabela [9, 4, 4, 1, 10, 9] jogos [11, 4, 6, 1, 12, 11] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: ASA tabela [9, 3, 2, 4, 6, 10] jogos [11, 3, 4, 4, 8, 12] — a tabela conta 9 jogos e as fontes trazem 11
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: ASA x Murici, ogol 2020-08-16); fica a do ogol
- vice pela Wikipédia (sem final de dois clubes): CSA

### 2021

- tabela publicada x jogos — Primeira fase / -: CSA tabela [8, 4, 3, 1, 17, 5] jogos [9, 4, 4, 1, 18, 6] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: CSE tabela [8, 4, 3, 1, 13, 7] jogos [13, 6, 5, 2, 20, 13] — a tabela conta 8 jogos e as fontes trazem 13
- tabela publicada x jogos — Primeira fase / -: Desportivo Aliança tabela [8, 4, 1, 3, 7, 5] jogos [10, 4, 2, 4, 9, 8] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: ASA tabela [8, 3, 4, 1, 11, 5] jogos [10, 4, 4, 2, 14, 8] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Jaciobá tabela [8, 2, 3, 3, 9, 13] jogos [9, 2, 4, 3, 9, 13] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: CEO tabela [8, 0, 2, 6, 2, 15] jogos [9, 0, 3, 6, 2, 15] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: CSE tabela [8, 4, 3, 1, 13, 7] jogos [7, 4, 3, 0, 13, 6] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / -: Desportivo Aliança tabela [8, 4, 1, 3, 7, 5] jogos [7, 3, 1, 3, 6, 5] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / -: Jaciobá tabela [8, 2, 3, 3, 9, 13] jogos [9, 2, 4, 3, 9, 13] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Primeira fase / -: CEO tabela [8, 0, 2, 6, 2, 15] jogos [9, 0, 3, 6, 2, 15] — a tabela conta 8 jogos e as fontes trazem 9
- mando invertido no ogol — RSSSF CEO 0-2 CSE, ogol CSE 2-0 CEO (2021-03-28); fica a RSSSF
- adversário diferente no ogol — RSSSF CSA 0-0 Jaciobá, ogol CSA 0-0 Murici (2021-02-20); fica a RSSSF
- jogo só no ogol, incluído em FIRST STAGE:: Desportivo Aliança 1-0 CSE (2021-02-28)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 1-1 CSA (2021-05-08)
- jogo só no ogol, incluído em Semifinal: Desportivo Aliança 0-1 CRB (2021-05-09)
- jogo só no ogol, incluído em Semifinal: CSA 3-0 CSE (2021-05-12)
- jogo só no ogol, incluído em Semifinal: CRB 2-1 Desportivo Aliança (2021-05-13)
- jogo só no ogol, incluído em Final: CSA 0-0 CRB (2021-05-15)
- jogo só no ogol, incluído em FIRST STAGE:: Desportivo Aliança 1-1 CSE (2021-05-17)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 2-1 Desportivo Aliança (2021-05-19)
- jogo só no ogol, incluído em Final: CRB 1-1 CSA (2021-05-22)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 2-1 ASA (2021-05-23)
- jogo só no ogol, incluído em FIRST STAGE:: ASA 2-1 CSE (2021-05-26)
- só na RSSSF (não achado no ogol): Murici 0-0 CEO (2021-02-28)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, CSA

### 2022

- a página dá o mesmo nome aos dois clubes; vale o jogo do ogol: CRB 1-4 ASA (2022-03-08)
- adversário diferente no ogol — RSSSF CSA 3-0 Murici, ogol CSA 3-0 Cruzeiro-AL (2022-05-02); fica a RSSSF
- só na RSSSF (não achado no ogol): CSA 2-4 CRB (2022-04-06)
- vencedor da final pelos jogos (CSA) diferente do campeão oficial (CRB); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): ASA

### 2023

- sem ocorrências

### 2024

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: CSA x CSE, ogol 2024-04-12); fica a do ogol
- vice pela Wikipédia (sem final de dois clubes): ASA

### 2025

- tabela publicada x jogos — Primeira fase / -: Penedense tabela [7, 4, 3, 0, 11, 4] jogos [8, 3, 3, 2, 9, 9] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: CSA tabela [7, 4, 2, 1, 12, 5] jogos [10, 5, 3, 2, 11, 6] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: ASA tabela [7, 3, 4, 0, 11, 1] jogos [10, 3, 5, 2, 12, 6] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: CRB tabela [7, 3, 3, 1, 17, 6] jogos [10, 5, 4, 1, 23, 10] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / -: Coruripe tabela [7, 1, 5, 1, 6, 8] jogos [6, 0, 5, 1, 3, 8] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / -: Murici tabela [7, 1, 3, 3, 5, 8] jogos [6, 0, 3, 3, 2, 8] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / -: CSE tabela [7, 1, 2, 4, 5, 14] jogos [8, 0, 3, 5, 2, 15] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / -: Igaci tabela [7, 0, 0, 7, 0, 21] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- jogo só no ogol, incluído em FIRST STAGE:: CSA 0-0 CSE (2025-04-02)
- jogo só no ogol, incluído em FIRST STAGE:: CSE 0-1 CSA (2025-04-06)

### 2026

- vice pela Wikipédia (sem final de dois clubes): ASA

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-al1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
