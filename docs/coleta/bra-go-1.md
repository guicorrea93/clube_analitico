# Campeonato Goiano (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-go-1/importar.py`. Pacote em `data/coleta/bra-go-1/pacote/`. Mesmo código do Cearense
(`docs/coleta/bra-ce-1.md`), com as fontes de Goiás.

**Temporadas:** 1944 a 2026, 83 edições (escopo aprovado pelo Guilherme em 25/11/2026; a conta da FGF). 1944-1962 é a era
amadora (o campeonato de Goiânia, que a FGF conta como Goiano); profissional desde 1963. Ficam fora os campeonatos de
Goiânia de 1940 e 1943 e o "Campeonato Estadual de Goiás" amador, que a FGF não reconhece. Edições sem página da RSSSF
e sem jogos no ogol entram só com campeão e vice.

**Fontes:** RSSSF Brasil (`tablesfq/go{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada
edição e o código de cada clube; jogos a partir dos anos 2000); Wikipédia em português (artigo "Campeonato Goiano de
Futebol Masculino": campeão e vice de cada ano, segunda fonte). Artilheiros pela lista da RSSSF (`gotops.htm`).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória
sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`
ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1944 | RSSSF | 5 | 10 (0) | 60 | 0 | 2 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 1945 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1946 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1947 | RSSSF | 8 | 42 (0) | 177 | 0 | 0 / 2 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF | 8 | 40 (0) | 218 | 49 | 0 / 1 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF | 6 | 30 (0) | 145 | 0 | 2 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 1950 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1951 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1952 | RSSSF | 6 | 30 (0) | 130 | 0 | 1 / 0 | Goiânia | RSSSF (classificação geral publicada) |
| 1953 | RSSSF | 9 | 72 (0) | 288 | 0 | 0 / 2 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF | 5 | 20 (0) | 66 | 61 | 0 / 2 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF | 8 | 56 (0) | 247 | 0 | 2 / 0 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF | 10 | 90 (0) | 404 | 0 | 1 / 1 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF | 9 | 72 (0) | 329 | 0 | 1 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 1958 | RSSSF | 8 | 56 (0) | 220 | 0 | 1 / 0 | Goiânia | RSSSF (classificação geral publicada) |
| 1959 | RSSSF | 12 | 58 (0) | 237 | 0 | 0 / 4 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1961 | RSSSF | 6 | 30 (0) | 105 | 0 | 1 / 0 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 1962 | RSSSF | 12 | 66 (0) | 256 | 0 | 0 / 2 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1964 | RSSSF | 12 | 132 (0) | 436 | 0 | 0 / 1 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1966 |  | 0 | 0 (0) | 0 | 0 | 0 / 0 | ? | - |
| 1967 | RSSSF | 10 | 88 (0) | 207 | 0 | 0 / 1 | CRAC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF | 10 | 90 (0) | 233 | 0 | 0 / 2 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF | 10 | 90 (0) | 285 | 0 | 0 / 2 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF | 13 | 144 (0) | 366 | 0 | 1 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 1971 | RSSSF | 9 | 74 (0) | 179 | 0 | 0 / 3 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF | 12 | 132 (0) | 287 | 0 | 1 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF | 9 | 75 (0) | 187 | 0 | 3 / 0 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 1974 | RSSSF | 9 | 66 (0) | 132 | 0 | 1 / 2 | Goiânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF | 11 | 112 (0) | 241 | 0 | 3 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 1976 | RSSSF | 13 | 133 (0) | 308 | 0 | 2 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF | 10 | 96 (0) | 201 | 0 | 1 / 2 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF | 13 | 242 (0) | 533 | 0 | 1 / 3 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF | 10 | 80 (0) | 176 | 0 | 3 / 1 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 1980 | RSSSF | 9 | 135 (0) | 293 | 0 | 7 / 1 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 1981 | RSSSF | 11 | 250 (0) | 504 | 0 | 1 / 5 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF | 12 | 202 (0) | 458 | 0 | 4 / 0 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 1983 | RSSSF | 8 | 124 (0) | 253 | 0 | 0 / 5 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF | 12 | 154 (0) | 300 | 1 | 1 / 5 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 12 | 183 (0) | 384 | 0 | 1 / 3 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 12 | 162 (0) | 309 | 0 | 3 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 1987 | RSSSF | 12 | 132 (0) | 249 | 0 | 1 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF | 14 | 218 (0) | 403 | 0 | 3 / 8 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF | 14 | 215 (0) | 409 | 0 | 3 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 1990 | RSSSF | 14 | 146 (0) | 277 | 0 | 4 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF | 14 | 183 (0) | 379 | 0 | 2 / 0 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF | 16 | 276 (0) | 626 | 0 | 3 / 2 | Goiatuba EC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF | 18 | 337 (0) | 771 | 0 | 1 / 3 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF | 18 | 352 (0) | 828 | 2 | 12 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 14 | 212 (0) | 512 | 0 | 3 / 4 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 12 | 167 (0) | 424 | 0 | 2 / 5 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 13 | 187 (0) | 506 | 0 | 5 / 0 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF | 12 | 147 (0) | 452 | 0 | 1 / 1 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 12 | 132 (132) | 364 | 3 | 0 / 2 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF | 14 | 210 (0) | 636 | 0 | 1 / 5 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 14 | 108 (108) | 327 | 325 | 3 / 1 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 12 | 109 (108) | 322 | 315 | 5 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2003 | RSSSF + ogol | 12 | 80 (79) | 253 | 253 | 2 / 1 | Goiás | RSSSF (classificação geral publicada) |
| 2004 | RSSSF + ogol | 12 | 108 (107) | 344 | 335 | 2 / 2 | CRAC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 12 | 108 (108) | 315 | 0 | 2 / 1 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 12 | 108 (108) | 328 | 0 | 1 / 1 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 12 | 108 (108) | 339 | 0 | 8 / 0 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 12 | 108 (108) | 357 | 0 | 5 / 0 | Itumbiara | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 12 | 108 (108) | 324 | 0 | 5 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 10 | 96 (96) | 316 | 0 | 3 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 10 | 96 (96) | 310 | 0 | 3 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 10 | 96 (96) | 306 | 0 | 3 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 10 | 96 (96) | 273 | 0 | 3 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2014 | RSSSF + ogol | 10 | 76 (76) | 179 | 0 | 5 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 2015 | RSSSF + ogol | 10 | 76 (76) | 166 | 0 | 5 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2016 | RSSSF + ogol | 10 | 76 (76) | 146 | 146 | 5 / 0 | Goiás | RSSSF (classificação geral publicada) |
| 2017 | RSSSF + ogol | 10 | 76 (76) | 174 | 170 | 5 / 0 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 10 | 76 (75) | 170 | 60 | 2 / 0 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 12 | 86 (86) | 210 | 201 | 9 / 0 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 12 | 79 (79) | 187 | 179 | 2 / 1 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 12 | 74 (74) | 151 | 141 | 4 / 1 | Grêmio Anápolis | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 12 | 74 (74) | 177 | 177 | 5 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 2023 | RSSSF + ogol | 12 | 80 (80) | 208 | 208 | 3 / 0 | Atlético-GO | RSSSF (classificação geral publicada) |
| 2024 | RSSSF + ogol | 12 | 80 (80) | 187 | 186 | 2 / 1 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 12 | 80 (80) | 153 | 153 | 3 / 0 | Vila Nova-GO | RSSSF (classificação geral publicada) |
| 2026 | ogol | 12 | 70 (70) | 176 | 0 | 0 / 0 | Goiás | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1944

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campinas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Campinas — clube que o ogol não tem; entra só pela RSSSF
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1945

- sem ocorrências

### 1946

- sem ocorrências

### 1947

- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [12, 10, 1, 1, 36, 10] jogos [12, 10, 1, 1, 40, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Goiânia tabela [12, 8, 2, 2, 28, 13] jogos [12, 8, 2, 2, 31, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Anápolis tabela [12, 5, 2, 5, 26, 26] jogos [12, 5, 2, 5, 26, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Inhumas tabela [12, 4, 2, 6, 23, 19] jogos [12, 4, 2, 6, 25, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [12, 4, 1, 7, 13, 30] jogos [10, 3, 1, 6, 10, 28] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: ABG tabela [12, 1, 1, 10, 17, 51] jogos [12, 1, 1, 10, 17, 52] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [12, 10, 1, 1, 36, 10] jogos [12, 10, 1, 1, 40, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Anápolis tabela [12, 5, 2, 5, 26, 26] jogos [12, 5, 2, 5, 26, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Inhumas tabela [12, 4, 2, 6, 23, 19] jogos [12, 4, 2, 6, 25, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [12, 4, 1, 7, 13, 32] jogos [10, 3, 1, 6, 10, 28] — a tabela conta 12 jogos e as fontes trazem 10
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABG
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Operário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- ABG — clube que o ogol não tem; entra só pela RSSSF
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Operário — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1948

- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [12, 9, 1, 2, 56, 10] jogos [10, 8, 0, 2, 54, 8] — a tabela conta 12 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Anapolina tabela [12, 5, 0, 7, 25, 24] jogos [11, 5, 0, 6, 25, 27] — a tabela conta 12 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Independente-GO tabela [12, 4, 1, 7, 20, 47] jogos [3, 2, 0, 1, 10, 8] — a tabela conta 12 jogos e as fontes trazem 3
- tabela publicada x jogos — Fase única / -: Botafogo de Goiânia tabela [12, 2, 0, 10, 12, 74] jogos [12, 2, 0, 10, 15, 74] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ABG
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- ABG — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (ABG)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Independente — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1949

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- Botafogo — clube que o ogol não tem; entra só pela RSSSF
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- União — clube que o ogol não tem; entra só pela RSSSF
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1950

- sem ocorrências

### 1951

- sem ocorrências

### 1952

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pires do Rio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Pires do Rio — clube que o ogol não tem; entra só pela RSSSF
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1953

- tabela publicada x jogos — Fase única / -: Goiás tabela [16, 11, 2, 3, 40, 20] jogos [16, 11, 2, 3, 42, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [16, 11, 1, 4, 40, 19] jogos [16, 10, 2, 4, 42, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Anapolina tabela [16, 3, 1, 12, 20, 43] jogos [16, 3, 2, 11, 23, 47] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Goiás tabela [16, 11, 2, 3, 40, 20] jogos [16, 11, 2, 3, 42, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [16, 11, 1, 4, 40, 19] jogos [16, 10, 2, 4, 42, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Anapolina tabela [16, 3, 1, 12, 20, 43] jogos [16, 3, 2, 11, 23, 47] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Francisco
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Ipiranga — clube que o ogol não tem; entra só pela RSSSF
- São Francisco — clube que o ogol não tem; entra só pela RSSSF
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1954

- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [8, 3, 2, 3, 12, 13] jogos [8, 3, 2, 3, 14, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Botafogo de Goiânia tabela [8, 2, 3, 3, 12, 14] jogos [8, 2, 3, 3, 12, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Goiás tabela [8, 2, 2, 4, 10, 14] jogos [8, 2, 2, 4, 10, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético-GO tabela [8, 3, 2, 3, 11, 13] jogos [8, 3, 2, 3, 14, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Botafogo de Goiânia tabela [8, 2, 3, 3, 12, 14] jogos [8, 2, 3, 3, 12, 17] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1955

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Vila
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luís/G
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Nova Vila — clube que o ogol não tem; entra só pela RSSSF
- São Luís/G — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1956

- tabela publicada x jogos — Fase única / -: Goiânia tabela [18, 16, 1, 1, 73, 18] jogos [18, 16, 1, 1, 75, 18] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nova Vila
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luís/G
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Goianás — clube que o ogol não tem; entra só pela RSSSF
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Nova Vila — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nova Vila)
- São Luís/G — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luís/G)
- São Paulo — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1957

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luís/G
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Paulo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Goianás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianás)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- São Luís/G — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Luís/G)
- São Paulo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São Paulo-GO)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1958

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campineira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Campineira — clube que o ogol não tem; entra só pela RSSSF
- Ferroviário — clube que o ogol não tem; entra só pela RSSSF
- Goianás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianás)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1959

- tabela publicada x jogos — Primeira fase / -: Goiás tabela [9, 5, 2, 2, 23, 9] jogos [9, 6, 1, 2, 23, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Campineira tabela [9, 4, 1, 4, 16, 15] jogos [9, 4, 1, 4, 16, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Ferroviário-GO tabela [9, 3, 1, 5, 10, 15] jogos [9, 3, 1, 5, 11, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Botafogo de Goiânia tabela [9, 3, 1, 5, 10, 23] jogos [9, 3, 1, 5, 12, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: América-GO tabela [9, 0, 2, 7, 4, 20] jogos [9, 0, 2, 7, 4, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiânia tabela [4, 4, 0, 0, 18, 5] jogos [6, 6, 0, 0, 30, 6] — a tabela conta 4 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase final / -: Goiás tabela [4, 1, 0, 3, 8, 12] jogos [4, 1, 0, 3, 8, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — in the play-offs (2 wins against 1) / -: Goiânia tabela [2, 2, 0, 0, 12, 1] jogos [15, 14, 0, 1, 61, 14] — a tabela conta 2 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Goiânia tabela [13, 12, 0, 1, 49, 13] jogos [15, 14, 0, 1, 61, 14] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase final / -: Goiás tabela [13, 6, 2, 5, 31, 19] jogos [13, 7, 1, 5, 31, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Campineira tabela [13, 6, 1, 6, 23, 28] jogos [13, 6, 1, 6, 23, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ferroviário-GO tabela [9, 3, 1, 5, 10, 15] jogos [9, 3, 1, 5, 11, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Botafogo de Goiânia tabela [9, 3, 1, 5, 10, 23] jogos [9, 3, 1, 5, 12, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: América-GO tabela [9, 0, 2, 7, 4, 20] jogos [9, 0, 2, 7, 4, 22] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campineira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Rita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — clube que o ogol não tem; entra só pela RSSSF
- Campineira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campineira)
- Ceres — clube que o ogol não tem; entra só pela RSSSF
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-GO)
- Goianás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianás)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Santa Rita — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1960

- sem ocorrências

### 1961

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campineira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Campineira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campineira)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-GO)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1962

- tabela publicada x jogos — Fase única / -: Ferroviário-GO tabela [11, 5, 1, 5, 20, 17] jogos [11, 6, 1, 4, 20, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Campineira tabela [11, 3, 0, 8, 10, 34] jogos [11, 2, 0, 9, 10, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Ferroviário-GO tabela [11, 5, 1, 5, 20, 17] jogos [11, 6, 1, 4, 20, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Campineira tabela [11, 3, 0, 8, 10, 34] jogos [11, 2, 0, 9, 10, 34] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo/BA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campineira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Rita
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Botafogo/BA — clube que o ogol não tem; entra só pela RSSSF
- Campineira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campineira)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-GO)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Santa Rita — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Rita-GO)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Santa Rita-GO

### 1963

- sem ocorrências

### 1964

- tabela publicada x jogos — Fase única / -: Ipiranga-GO tabela [22, 10, 2, 10, 48, 33] jogos [22, 10, 2, 10, 47, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: São Luís/SLMB tabela [22, 4, 2, 16, 21, 55] jogos [22, 4, 2, 16, 25, 51] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo/BA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campinas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ferroviário
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luís/SLMB
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Botafogo/BA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo/BA)
- Campinas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campinas)
- Ferroviário — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviário-GO)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- São Luís/SLMB — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1965

- sem ocorrências

### 1966

- sem ocorrências

### 1967

- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [18, 9, 5, 4, 31, 16] jogos [19, 9, 5, 5, 31, 17] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [18, 7, 9, 2, 30, 13] jogos [18, 7, 8, 3, 30, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Goiânia tabela [16, 4, 4, 8, 14, 24] jogos [18, 6, 4, 8, 19, 22] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Inhumas tabela [16, 3, 5, 8, 12, 22] jogos [17, 5, 4, 8, 14, 22] — a tabela conta 16 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Ceres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1968

- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [18, 7, 6, 5, 28, 15] jogos [18, 8, 6, 4, 28, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Inhumas tabela [18, 5, 6, 7, 18, 29] jogos [18, 4, 6, 8, 18, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [18, 7, 6, 5, 28, 15] jogos [18, 8, 6, 4, 28, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Inhumas tabela [18, 5, 6, 7, 18, 29] jogos [18, 4, 6, 8, 18, 29] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Nacional — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Anápolis

### 1969

- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [18, 10, 6, 2, 32, 13] jogos [18, 9, 7, 2, 32, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: CRAC tabela [18, 10, 6, 2, 32, 13] jogos [18, 11, 4, 3, 37, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Vila Nova-GO tabela [18, 10, 6, 2, 32, 13] jogos [18, 9, 7, 2, 32, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: CRAC tabela [18, 10, 6, 2, 32, 13] jogos [18, 11, 4, 3, 37, 22] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Ceres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- campeão pela lista oficial, Vila Nova-GO; o 1º pela soma dos jogos da última fase é CRAC (desempate, jogo extra ou pontos tirados fora de campo)
- vice pela Wikipédia (sem final de dois clubes): CRAC

### 1970

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Anapolino
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): São Luís
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Ceres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Grêmio Anapolino — clube que o ogol não tem; entra só pela RSSSF
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- São Luís — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1971

- tabela publicada x jogos — Primeira fase / -: Campinas tabela [16, 6, 2, 8, 18, 24] jogos [16, 6, 2, 8, 21, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Jataiense tabela [16, 5, 3, 8, 15, 21] jogos [16, 5, 3, 8, 15, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Campinas tabela [16, 6, 2, 8, 18, 24] jogos [16, 6, 2, 8, 21, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Jataiense tabela [16, 5, 3, 8, 15, 21] jogos [16, 5, 3, 8, 15, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Campinas tabela [16, 6, 2, 8, 18, 24] jogos [16, 6, 2, 8, 21, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Jataiense tabela [16, 5, 3, 8, 15, 21] jogos [16, 5, 3, 8, 15, 24] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campinas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianésia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Grêmio Anapolino
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Campinas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campinas)
- Goianésia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianésia)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Grêmio Anapolino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Grêmio Anapolino)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1972

- tabela publicada x jogos — Segunda fase / -: Itumbiara tabela [11, 3, 4, 4, 7, 8] jogos [10, 2, 4, 4, 7, 8] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Goiatuba EC tabela [11, 3, 3, 5, 6, 10] jogos [10, 2, 3, 5, 6, 10] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Inhumas tabela [11, 1, 0, 10, 9, 21] jogos [9, 1, 0, 8, 9, 21] — a tabela conta 11 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [22, 5, 9, 8, 14, 20] jogos [21, 4, 9, 8, 14, 20] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Itumbiara tabela [22, 6, 6, 10, 20, 25] jogos [21, 5, 6, 10, 20, 25] — a tabela conta 22 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase final / -: Inhumas tabela [22, 3, 3, 16, 18, 37] jogos [20, 3, 3, 14, 18, 37] — a tabela conta 22 jogos e as fontes trazem 20
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Campinas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Campinas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Campinas)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1973

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HORIZONTE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- NOVO HORIZONTE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vencedor da final pelos jogos (Goiás) diferente do campeão oficial (Vila Nova-GO); fica o oficial

### 1974

- tabela publicada x jogos — Primeira fase / -: Atlético-GO tabela [8, 4, 2, 2, 8, 4] jogos [8, 5, 2, 1, 10, 3] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [8, 4, 1, 3, 8, 5] jogos [8, 3, 1, 4, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [15, 5, 7, 3, 14, 10] jogos [15, 6, 7, 2, 16, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anápolis tabela [15, 4, 5, 6, 13, 16] jogos [15, 3, 5, 7, 12, 18] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Independente
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente-GO)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1975

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1976

- tabela publicada x jogos — Segunda fase / -: Goiás tabela [11, 9, 1, 1, 24, 4] jogos [10, 8, 1, 1, 23, 4] — a tabela conta 11 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [11, 6, 4, 1, 16, 5] jogos [11, 5, 4, 2, 16, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Rio Verde-GO tabela [11, 5, 2, 4, 11, 7] jogos [11, 6, 2, 3, 11, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [24, 16, 5, 3, 47, 15] jogos [23, 15, 5, 3, 46, 15] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [24, 14, 6, 4, 42, 14] jogos [24, 13, 6, 5, 42, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Rio Verde-GO tabela [22, 7, 7, 8, 19, 21] jogos [22, 8, 7, 7, 19, 21] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOLAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- GOLAS — clube que o ogol não tem; entra só pela RSSSF
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1977

- tabela publicada x jogos — Primeira fase / -: Goiânia tabela [9, 3, 4, 2, 14, 7] jogos [9, 3, 4, 2, 14, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Rio Verde-GO tabela [9, 1, 5, 3, 7, 9] jogos [9, 1, 5, 3, 8, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Anapolina tabela [9, 5, 1, 3, 9, 7] jogos [9, 5, 1, 3, 9, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Jataiense tabela [9, 1, 3, 5, 5, 11] jogos [9, 3, 1, 5, 5, 11] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mineiros
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Mineiros — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1978

- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [24, 16, 6, 2, 46, 14] jogos [24, 15, 7, 2, 46, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [24, 15, 4, 5, 39, 11] jogos [24, 15, 4, 5, 39, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Anapolina tabela [24, 13, 5, 6, 26, 14] jogos [23, 13, 5, 5, 26, 13] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Segunda fase / -: Anápolis tabela [24, 9, 8, 7, 24, 22] jogos [25, 9, 8, 8, 24, 23] — a tabela conta 24 jogos e as fontes trazem 25
- tabela publicada x jogos — Segunda fase / -: Rio Verde-GO tabela [23, 8, 7, 8, 22, 26] jogos [23, 8, 8, 7, 23, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Goiatuba EC tabela [23, 6, 4, 13, 20, 39] jogos [23, 6, 4, 13, 22, 39] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Ipiranga-GO tabela [22, 3, 5, 14, 26, 30] jogos [22, 3, 5, 14, 26, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [10, 5, 4, 1, 13, 4] jogos [10, 5, 5, 0, 13, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [34, 21, 10, 3, 59, 18] jogos [34, 20, 12, 2, 59, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [48, 24, 13, 11, 67, 31] jogos [48, 24, 13, 11, 67, 32] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anapolina tabela [34, 16, 8, 10, 34, 23] jogos [33, 16, 8, 9, 34, 22] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Fase final / -: Rio Verde-GO tabela [37, 15, 10, 12, 31, 32] jogos [37, 15, 11, 11, 32, 34] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anápolis tabela [38, 12, 10, 16, 34, 41] jogos [39, 12, 10, 17, 34, 42] — a tabela conta 38 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [37, 7, 6, 24, 31, 62] jogos [37, 7, 6, 24, 33, 62] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Ipiranga-GO tabela [36, 5, 8, 23, 34, 55] jogos [36, 5, 8, 23, 34, 61] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ipiranga
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mineiros
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Ipiranga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ipiranga-GO)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Mineiros — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1979

- tabela publicada x jogos — Fase final / -: Goiás tabela [20, 5, 10, 5, 17, 20] jogos [20, 5, 10, 5, 17, 19] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mineiros
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Mineiros — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1980

- tabela publicada x jogos — Overall Table First and Second Stages / -: Goiás tabela [29, 16, 6, 7, 42, 20] jogos [29, 16, 6, 7, 42, 24] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1981

- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [5, 4, 1, 0, 5, 0] jogos [11, 5, 4, 2, 12, 9] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Anápolis tabela [5, 2, 1, 2, 4, 5] jogos [11, 3, 1, 7, 9, 15] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Anapolina tabela [5, 1, 3, 1, 3, 3] jogos [11, 3, 7, 1, 11, 9] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Goiás tabela [5, 0, 2, 3, 1, 5] jogos [11, 3, 5, 3, 9, 8] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / -: Anápolis tabela [20, 8, 9, 3, 15, 13] jogos [20, 7, 9, 4, 15, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Overall Table - First and Second Stages / -: Anápolis tabela [45, 20, 14, 11, 45, 37] jogos [45, 19, 14, 12, 45, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [6, 3, 3, 0, 8, 3] jogos [11, 3, 5, 3, 9, 8] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Anapolina tabela [6, 2, 4, 0, 8, 6] jogos [11, 3, 7, 1, 11, 9] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [6, 1, 3, 2, 7, 9] jogos [11, 5, 4, 2, 12, 9] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Anápolis tabela [6, 1, 0, 5, 5, 10] jogos [11, 3, 1, 7, 9, 15] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Final / -: Goiás tabela [54, 23, 19, 12, 58, 36] jogos [54, 22, 20, 12, 58, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Anapolina tabela [54, 28, 19, 7, 76, 35] jogos [54, 28, 20, 6, 77, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Anápolis tabela [51, 21, 14, 16, 50, 47] jogos [51, 20, 14, 17, 50, 47] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Crac
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Monte Cristo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Crac — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Monte Cristo — clube que o ogol não tem; entra só pela RSSSF
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Goiás

### 1982

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Crac
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Monte Cristo
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Nacional
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Crac — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Monte Cristo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Monte Cristo)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-GO)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1983

- tabela publicada x jogos — Primeira fase / Grupo A: Anapolina tabela [14, 5, 4, 5, 18, 24] jogos [14, 4, 5, 5, 17, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo A: Vila Nova-GO tabela [14, 4, 4, 6, 15, 18] jogos [14, 3, 5, 6, 15, 18] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Itumbiara tabela [14, 4, 7, 3, 16, 17] jogos [14, 4, 8, 2, 16, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A: Itumbiara tabela [14, 6, 5, 3, 13, 11] jogos [16, 6, 7, 3, 13, 11] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / Grupo A: Vila Nova-GO tabela [14, 4, 5, 5, 19, 23] jogos [16, 5, 5, 6, 21, 24] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Segunda fase / Grupo B: Goiás tabela [14, 6, 5, 3, 18, 6] jogos [18, 8, 5, 5, 21, 10] — a tabela conta 14 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / Grupo B: Anapolina tabela [14, 6, 3, 5, 16, 17] jogos [18, 7, 5, 6, 18, 19] — a tabela conta 14 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Anapolina tabela [36, 14, 9, 13, 40, 44] jogos [36, 13, 10, 13, 40, 46] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Itumbiara tabela [32, 10, 14, 8, 29, 30] jogos [32, 11, 15, 6, 31, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [30, 9, 9, 12, 36, 42] jogos [30, 8, 10, 12, 36, 42] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Anapolina

### 1984

- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [11, 6, 4, 1, 17, 8] jogos [11, 6, 4, 1, 17, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Goiás tabela [11, 4, 2, 5, 9, 8] jogos [11, 4, 2, 5, 9, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Overall Table - First Stage - First and Second Phases / -: Vila Nova-GO tabela [22, 10, 7, 5, 26, 16] jogos [22, 10, 7, 5, 26, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Overall Table - First Stage - First and Second Phases / -: Goiás tabela [22, 10, 5, 7, 23, 15] jogos [22, 10, 5, 7, 23, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [6, 4, 1, 1, 10, 5] jogos [11, 8, 2, 1, 20, 8] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Goiânia tabela [6, 2, 2, 2, 8, 6] jogos [11, 4, 3, 4, 14, 15] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [6, 0, 0, 6, 5, 18] jogos [11, 1, 1, 9, 9, 24] — a tabela conta 6 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [5, 4, 1, 0, 10, 3] jogos [11, 8, 2, 1, 20, 8] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Goiânia tabela [5, 2, 1, 2, 6, 9] jogos [11, 4, 3, 4, 14, 15] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [5, 1, 1, 3, 4, 6] jogos [11, 1, 1, 9, 9, 24] — a tabela conta 5 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [33, 18, 9, 6, 46, 24] jogos [33, 18, 9, 6, 46, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [28, 14, 6, 8, 32, 18] jogos [28, 14, 6, 8, 32, 20] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIANÉSIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JATAIENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIANÉSIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianésia)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- JATAIENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- NACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-GO)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1985

- tabela publicada x jogos — Primeira fase / -: Goiás tabela [22, 14, 6, 2, 33, 8] jogos [22, 13, 6, 3, 33, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Atlético-GO tabela [22, 12, 7, 3, 34, 10] jogos [22, 11, 7, 4, 30, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Vila Nova-GO tabela [22, 12, 7, 3, 34, 21] jogos [22, 13, 7, 2, 34, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [22, 7, 4, 11, 19, 25] jogos [22, 8, 4, 10, 19, 25] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [8, 4, 2, 2, 12, 5] jogos [30, 12, 6, 12, 31, 30] — a tabela conta 8 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Rio Verde-GO tabela [8, 4, 2, 2, 14, 10] jogos [30, 8, 8, 14, 27, 32] — a tabela conta 8 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Goiatuba EC tabela [8, 2, 4, 2, 9, 11] jogos [30, 7, 12, 11, 29, 42] — a tabela conta 8 jogos e as fontes trazem 30
- tabela publicada x jogos — Primeira fase / -: Monte Cristo tabela [8, 2, 3, 3, 8, 11] jogos [31, 8, 9, 14, 23, 43] — a tabela conta 8 jogos e as fontes trazem 31
- tabela publicada x jogos — Primeira fase / -: Itumbiara tabela [8, 2, 1, 5, 8, 14] jogos [30, 8, 9, 13, 27, 36] — a tabela conta 8 jogos e as fontes trazem 30
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [32, 19, 10, 3, 51, 16] jogos [32, 18, 10, 4, 47, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [32, 17, 10, 5, 45, 19] jogos [32, 16, 10, 6, 45, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [32, 15, 9, 8, 46, 40] jogos [32, 16, 9, 7, 46, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anápolis tabela [30, 11, 6, 13, 31, 30] jogos [30, 12, 6, 12, 31, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Monte Cristo tabela [30, 7, 9, 14, 21, 43] jogos [31, 8, 9, 14, 23, 43] — a tabela conta 30 jogos e as fontes trazem 31
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MONTE CRISTO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NACIONAL
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- MONTE CRISTO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Monte Cristo)
- NACIONAL — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-GO)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1986

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AMÉRICA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIANÉSIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- AMÉRICA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIANÉSIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianésia)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1987

- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [11, 5, 5, 1, 8, 4] jogos [11, 5, 5, 1, 9, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [11, 2, 6, 3, 6, 9] jogos [11, 2, 6, 3, 7, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — ** GOIÁS won both Stages; no Final needed ** / -: Atlético-GO tabela [22, 12, 7, 3, 23, 12] jogos [22, 12, 7, 3, 24, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — ** GOIÁS won both Stages; no Final needed ** / -: Vila Nova-GO tabela [22, 4, 11, 7, 12, 18] jogos [22, 4, 11, 7, 13, 19] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1988

- tabela publicada x jogos — Primeira fase / Grupo A: Goiatuba EC tabela [6, 3, 3, 0, 6, 2] jogos [12, 7, 4, 1, 17, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Goiás tabela [6, 3, 1, 2, 7, 4] jogos [12, 6, 2, 4, 15, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Itumbiara tabela [6, 2, 3, 1, 4, 3] jogos [12, 5, 3, 4, 11, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Vila Nova-GO tabela [6, 2, 3, 1, 5, 4] jogos [12, 2, 4, 6, 7, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Novo Horizonte tabela [6, 2, 3, 1, 4, 3] jogos [12, 4, 4, 4, 9, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: América-GO tabela [6, 0, 3, 3, 2, 5] jogos [12, 4, 4, 4, 11, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Anapolina tabela [6, 0, 2, 4, 4, 11] jogos [12, 1, 5, 6, 10, 19] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Anápolis tabela [6, 2, 4, 0, 2, 0] jogos [12, 5, 5, 2, 9, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Ceres tabela [6, 3, 1, 2, 7, 5] jogos [12, 5, 4, 3, 13, 11] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Rio Verde-GO tabela [6, 2, 3, 1, 4, 5] jogos [12, 3, 4, 5, 8, 15] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Santa Helena tabela [6, 2, 3, 1, 4, 3] jogos [12, 4, 5, 3, 9, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Atlético-GO tabela [6, 1, 3, 2, 3, 3] jogos [12, 4, 6, 2, 15, 5] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Goiânia tabela [6, 2, 0, 4, 7, 8] jogos [12, 4, 0, 8, 13, 15] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Jataiense tabela [6, 0, 4, 2, 3, 6] jogos [12, 2, 6, 4, 9, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Goiás tabela [7, 7, 0, 0, 24, 3] jogos [12, 6, 2, 4, 15, 8] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Goiatuba EC tabela [7, 4, 1, 2, 8, 4] jogos [12, 7, 4, 1, 17, 8] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Anapolina tabela [7, 3, 3, 1, 7, 4] jogos [12, 1, 5, 6, 10, 19] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Vila Nova-GO tabela [7, 1, 5, 1, 6, 8] jogos [12, 2, 4, 6, 7, 13] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: América-GO tabela [7, 2, 3, 2, 3, 5] jogos [12, 4, 4, 4, 11, 12] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Itumbiara tabela [7, 1, 4, 2, 4, 7] jogos [12, 5, 3, 4, 11, 10] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Novo Horizonte tabela [7, 1, 3, 3, 3, 6] jogos [12, 4, 4, 4, 9, 10] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Atlético-GO tabela [7, 4, 2, 1, 13, 3] jogos [12, 4, 6, 2, 15, 5] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Goiânia tabela [7, 2, 4, 1, 6, 7] jogos [12, 4, 0, 8, 13, 15] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Santa Helena tabela [7, 2, 3, 2, 2, 3] jogos [12, 4, 5, 3, 9, 8] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Anápolis tabela [7, 2, 2, 3, 6, 6] jogos [12, 5, 5, 2, 9, 10] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Rio Verde-GO tabela [7, 1, 2, 4, 8, 13] jogos [12, 3, 4, 5, 8, 15] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Ceres tabela [7, 0, 3, 4, 2, 6] jogos [12, 5, 4, 3, 13, 11] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Jataiense tabela [7, 0, 3, 4, 0, 17] jogos [12, 2, 6, 4, 9, 12] — a tabela conta 7 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Goiatuba EC tabela [6, 4, 1, 1, 11, 6] jogos [12, 7, 4, 1, 17, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: América-GO tabela [6, 4, 1, 1, 9, 7] jogos [12, 4, 4, 4, 11, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Goiás tabela [6, 3, 1, 2, 8, 4] jogos [12, 6, 2, 4, 15, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Itumbiara tabela [6, 3, 0, 3, 7, 7] jogos [12, 5, 3, 4, 11, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Novo Horizonte tabela [6, 2, 1, 3, 5, 7] jogos [12, 4, 4, 4, 9, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Anapolina tabela [6, 1, 3, 2, 6, 8] jogos [12, 1, 5, 6, 10, 19] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo A: Vila Nova-GO tabela [6, 0, 1, 5, 2, 9] jogos [12, 2, 4, 6, 7, 13] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Atlético-GO tabela [6, 3, 3, 0, 12, 2] jogos [12, 4, 6, 2, 15, 5] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Anápolis tabela [6, 3, 1, 2, 7, 10] jogos [12, 5, 5, 2, 9, 10] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Ceres tabela [6, 2, 3, 1, 6, 6] jogos [12, 5, 4, 3, 13, 11] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Santa Helena tabela [6, 2, 2, 2, 5, 5] jogos [12, 4, 5, 3, 9, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Jataiense tabela [6, 2, 2, 2, 6, 6] jogos [12, 2, 6, 4, 9, 12] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Goiânia tabela [6, 2, 0, 4, 6, 7] jogos [12, 4, 0, 8, 13, 15] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Primeira fase / Grupo B: Rio Verde-GO tabela [6, 1, 1, 4, 4, 10] jogos [12, 3, 4, 5, 8, 15] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [6, 3, 2, 1, 7, 3] jogos [8, 4, 3, 1, 9, 4] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase final / -: Goiás tabela [6, 2, 3, 1, 7, 4] jogos [12, 4, 7, 1, 13, 8] — a tabela conta 6 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [6, 3, 0, 3, 6, 7] jogos [14, 3, 5, 6, 11, 15] — a tabela conta 6 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase final / -: Goiás tabela [44, 25, 13, 6, 73, 24] jogos [44, 26, 12, 6, 73, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [48, 21, 18, 9, 51, 31] jogos [48, 22, 16, 10, 51, 31] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anápolis tabela [38, 10, 16, 12, 27, 39] jogos [38, 10, 15, 13, 27, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Itumbiara tabela [26, 8, 11, 7, 23, 23] jogos [26, 8, 12, 6, 22, 19] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AMÉRICA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JATAIENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HORIZONTE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- AMÉRICA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- JATAIENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- NOVO HORIZONTE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vencedor da final pelos jogos (Goiás) diferente do campeão oficial (Atlético-GO); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1989

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AMÉRICA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANÁPOLIS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MINEIROS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HORIZONTE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- AMÉRICA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- ANÁPOLIS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- MINEIROS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- NOVO HORIZONTE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- Quirinópolis — clube que o ogol não tem; entra só pela RSSSF
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1990

- tabela publicada x jogos — Fase final / -: Itumbiara tabela [10, 2, 3, 5, 11, 8] jogos [10, 2, 5, 3, 11, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [28, 19, 5, 4, 61, 16] jogos [20, 13, 3, 4, 43, 13] — a tabela conta 28 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Mineiros tabela [24, 8, 11, 5, 26, 22] jogos [20, 7, 10, 3, 21, 16] — a tabela conta 24 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Goiânia tabela [26, 8, 10, 8, 19, 30] jogos [20, 8, 8, 4, 18, 18] — a tabela conta 26 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [22, 8, 8, 6, 20, 14] jogos [20, 7, 8, 5, 18, 12] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Anapolina tabela [22, 6, 12, 4, 23, 18] jogos [20, 6, 10, 4, 22, 17] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: América-GO tabela [22, 7, 5, 10, 18, 30] jogos [20, 7, 4, 9, 18, 27] — a tabela conta 22 jogos e as fontes trazem 20
- tabela publicada x jogos — Fase final / -: Itumbiara tabela [22, 5, 7, 10, 23, 20] jogos [22, 5, 9, 8, 23, 20] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AMÉRICA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÂNIA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JATAIENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MINEIROS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HORIZONTE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- AMÉRICA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- GOIÂNIA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- JATAIENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- MINEIROS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- NOVO HORIZONTE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- Quirinópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quirinópolis)
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vencedor da final pelos jogos (Atlético-GO) diferente do campeão oficial (Goiás); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Goiânia

### 1991

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mineiros
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Horizonte
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pires do Rio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Mineiros — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- Novo Horizonte — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- Pires do Rio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pires do Rio)
- Quirinópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quirinópolis)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1992

- tabela publicada x jogos — Segunda fase / Grupo B: Goiatuba EC tabela [6, 2, 2, 2, 7, 7] jogos [6, 2, 2, 2, 7, 6] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo B: Inhumas tabela [6, 2, 2, 2, 5, 4] jogos [6, 2, 2, 2, 5, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [42, 21, 15, 6, 70, 38] jogos [42, 21, 15, 6, 70, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Inhumas tabela [36, 13, 16, 7, 37, 28] jogos [36, 13, 16, 7, 37, 29] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AMÉRICA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ANAPOLINA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CERES
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIATUBA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): GOIÁS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): INHUMAS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): ITUMBIARA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): JATAIENSE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): MINEIROS
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): NOVO HORIZONTE
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): PIRES DO RIO
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Piracanjuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): SANTA HELENA
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): VILA NOVA
- AMÉRICA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- ANAPOLINA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- CERES — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- GOIATUBA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- GOIÁS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- INHUMAS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- ITUMBIARA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- JATAIENSE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- MINEIROS — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- NOVO HORIZONTE — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- PIRES DO RIO — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pires do Rio)
- Piracanjuba — clube que o ogol não tem; entra só pela RSSSF
- Quirinópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quirinópolis)
- SANTA HELENA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- VILA NOVA — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): Goiás

### 1993

- tabela publicada x jogos — Primeira fase / -: Mineiros tabela [34, 19, 12, 3, 52, 21] jogos [35, 20, 12, 3, 54, 22] — a tabela conta 34 jogos e as fontes trazem 35
- tabela publicada x jogos — Primeira fase / -: Goiânia tabela [34, 18, 9, 7, 71, 35] jogos [35, 19, 9, 7, 73, 36] — a tabela conta 34 jogos e as fontes trazem 35
- tabela publicada x jogos — Primeira fase / -: Quirinópolis tabela [34, 14, 9, 11, 39, 31] jogos [33, 13, 9, 11, 38, 31] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Primeira fase / -: Itumbiara tabela [34, 13, 9, 12, 37, 43] jogos [34, 13, 9, 12, 38, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: CRAC tabela [34, 9, 9, 16, 37, 51] jogos [34, 8, 9, 17, 33, 53] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Anapolina tabela [34, 7, 5, 22, 24, 56] jogos [33, 7, 5, 21, 24, 51] — a tabela conta 34 jogos e as fontes trazem 33
- tabela publicada x jogos — Segunda fase / Grupo 1: Vila Nova-GO tabela [6, 3, 3, 0, 9, 5] jogos [6, 3, 3, 0, 8, 4] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [45, 23, 15, 7, 70, 43] jogos [45, 23, 15, 7, 69, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Mineiros tabela [42, 21, 16, 5, 58, 27] jogos [43, 22, 16, 5, 60, 28] — a tabela conta 42 jogos e as fontes trazem 43
- tabela publicada x jogos — Fase final / -: Goiânia tabela [42, 21, 11, 10, 78, 42] jogos [43, 22, 11, 10, 80, 43] — a tabela conta 42 jogos e as fontes trazem 43
- tabela publicada x jogos — Fase final / -: Quirinópolis tabela [40, 15, 10, 15, 42, 40] jogos [39, 14, 10, 15, 41, 40] — a tabela conta 40 jogos e as fontes trazem 39
- tabela publicada x jogos — Fase final / -: Itumbiara tabela [34, 13, 9, 12, 37, 43] jogos [34, 13, 9, 12, 38, 44] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: CRAC tabela [34, 9, 9, 16, 37, 51] jogos [34, 8, 9, 17, 33, 53] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anapolina tabela [34, 7, 5, 22, 24, 56] jogos [33, 7, 5, 21, 24, 51] — a tabela conta 34 jogos e as fontes trazem 33
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ceres
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Mineiros
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Novo Horizonte
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Ceres — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ceres)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Mineiros — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mineiros)
- Novo Horizonte — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Novo Horizonte)
- Quirinópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quirinópolis)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1994

- tabela publicada x jogos — Primeira fase / -: Goiás tabela [34, 20, 11, 3, 67, 28] jogos [46, 28, 13, 5, 90, 40] — a tabela conta 34 jogos e as fontes trazem 46
- tabela publicada x jogos — Primeira fase / -: Vila Nova-GO tabela [34, 18, 10, 6, 48, 27] jogos [47, 25, 12, 10, 66, 38] — a tabela conta 34 jogos e as fontes trazem 47
- tabela publicada x jogos — Primeira fase / -: Atlético-GO tabela [34, 18, 8, 8, 46, 19] jogos [43, 22, 9, 12, 60, 32] — a tabela conta 34 jogos e as fontes trazem 43
- tabela publicada x jogos — Primeira fase / -: Rio Verde-GO tabela [34, 14, 16, 4, 36, 18] jogos [42, 17, 18, 7, 45, 24] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Goiatuba EC tabela [34, 15, 11, 8, 57, 38] jogos [44, 21, 14, 9, 70, 44] — a tabela conta 34 jogos e as fontes trazem 44
- tabela publicada x jogos — Primeira fase / -: Itumbiara tabela [34, 15, 9, 10, 60, 37] jogos [42, 19, 10, 13, 71, 49] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Caldas tabela [34, 15, 8, 11, 43, 37] jogos [42, 17, 9, 16, 49, 45] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: América-GO tabela [34, 12, 12, 10, 39, 42] jogos [42, 13, 14, 15, 44, 61] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [34, 11, 12, 11, 44, 46] jogos [42, 13, 14, 15, 51, 58] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Jataiense tabela [34, 10, 14, 10, 46, 43] jogos [42, 10, 16, 16, 52, 56] — a tabela conta 34 jogos e as fontes trazem 42
- tabela publicada x jogos — Primeira fase / -: Santa Helena tabela [34, 10, 14, 10, 38, 39] jogos [34, 10, 14, 10, 38, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Santa Helena tabela [34, 10, 14, 10, 38, 39] jogos [34, 10, 14, 10, 38, 35] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Piracanjuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Pires do Rio
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Quirinópolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Piracanjuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Piracanjuba)
- Pires do Rio — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Pires do Rio)
- Quirinópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Quirinópolis)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1995

- tabela publicada x jogos — Primeira fase / Grupo 2: Rio Verde-GO tabela [12, 7, 2, 3, 16, 17] jogos [12, 7, 2, 3, 18, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 2: Caldas tabela [12, 6, 2, 4, 12, 8] jogos [12, 6, 2, 4, 12, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [18, 7, 6, 5, 23, 19] jogos [18, 6, 6, 6, 22, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: América-GO tabela [18, 2, 5, 11, 13, 30] jogos [18, 3, 5, 10, 14, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Terceira fase / Grupo A: Goiatuba EC tabela [6, 2, 0, 4, 4, 7] jogos [6, 2, 0, 4, 7, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [44, 17, 15, 12, 62, 47] jogos [44, 16, 15, 13, 60, 48] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Anápolis tabela [44, 22, 12, 10, 63, 48] jogos [44, 22, 12, 10, 63, 47] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Rio Verde-GO tabela [42, 17, 16, 9, 51, 49] jogos [42, 17, 16, 9, 53, 47] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [38, 16, 17, 5, 59, 34] jogos [36, 15, 16, 5, 57, 33] — a tabela conta 38 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: Anapolina tabela [30, 9, 9, 12, 42, 46] jogos [18, 3, 5, 10, 21, 36] — a tabela conta 30 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Goiatuba EC tabela [31, 11, 7, 13, 35, 37] jogos [18, 3, 4, 11, 15, 28] — a tabela conta 31 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase final / -: Caldas tabela [30, 8, 6, 16, 22, 36] jogos [30, 8, 6, 16, 22, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: América-GO tabela [30, 5, 10, 15, 26, 44] jogos [30, 6, 10, 14, 27, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Santa Helena tabela [24, 8, 6, 10, 19, 28] jogos [12, 2, 4, 6, 8, 14] — a tabela conta 24 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase final / -: Inhumas tabela [24, 3, 6, 15, 17, 39] jogos [12, 1, 3, 8, 8, 22] — a tabela conta 24 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inhumas)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vila Nova-GO

### 1996

- tabela publicada x jogos — Primeira fase / -: Goiás tabela [12, 7, 4, 1, 16, 8] jogos [12, 7, 4, 1, 18, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: CRAC tabela [11, 3, 3, 5, 13, 19] jogos [11, 3, 3, 5, 12, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — ***** FIRST AND SECOND STAGES - TABLE : ***** / -: Goiás tabela [24, 13, 10, 1, 32, 9] jogos [24, 13, 10, 1, 34, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — ***** FIRST AND SECOND STAGES - TABLE : ***** / -: CRAC tabela [22, 6, 8, 8, 28, 38] jogos [22, 6, 8, 8, 27, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Goiás tabela [36, 19, 11, 6, 49, 20] jogos [36, 19, 11, 6, 51, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: CRAC tabela [22, 6, 8, 8, 28, 38] jogos [22, 6, 8, 8, 27, 38] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vencedor da final pelos jogos (Atlético-GO) diferente do campeão oficial (Goiás); fica o oficial
- vice pela Wikipédia (sem final de dois clubes): Atlético-GO

### 1997

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): América
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aparecidense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bom Jesus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- América — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (América-GO)
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Aparecidense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aparecidense)
- Bom Jesus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bom Jesus EC)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)
- vice pela Wikipédia (sem final de dois clubes): CRAC

### 1998

- tabela publicada x jogos — Segunda fase / -: Goiás tabela [6, 3, 2, 1, 12, 8] jogos [3, 1, 1, 1, 5, 6] — a tabela conta 6 jogos e as fontes trazem 3
- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [6, 2, 3, 1, 8, 8] jogos [3, 1, 1, 1, 5, 6] — a tabela conta 6 jogos e as fontes trazem 3
- tabela publicada x jogos — Segunda fase / -: Anápolis tabela [6, 2, 2, 2, 14, 10] jogos [3, 2, 0, 1, 8, 3] — a tabela conta 6 jogos e as fontes trazem 3
- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [6, 0, 3, 3, 5, 13] jogos [3, 0, 2, 1, 3, 6] — a tabela conta 6 jogos e as fontes trazem 3
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bom Jesus
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): CRAC
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Jataiense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santa Helena
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Bom Jesus — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bom Jesus EC)
- CRAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (CRAC)
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Jataiense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jataiense)
- Santa Helena — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Helena)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 1999

- tabela publicada x jogos — Primeira fase / -: Atlético-GO tabela [22, 10, 6, 6, 28, 23] jogos [22, 9, 7, 6, 28, 23] — placar diverge entre RSSSF e ogol em Atlético-GO x Anápolis (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [22, 4, 9, 9, 25, 35] jogos [22, 4, 10, 8, 25, 35] — placar diverge entre RSSSF e ogol em Atlético-GO x Anápolis (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Atlético-GO tabela [22, 10, 6, 6, 28, 23] jogos [22, 9, 7, 6, 28, 23] — placar diverge entre RSSSF e ogol em Atlético-GO x Anápolis (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / -: Anápolis tabela [22, 4, 9, 9, 25, 35] jogos [22, 4, 10, 8, 25, 35] — placar diverge entre RSSSF e ogol em Atlético-GO x Anápolis (0-0 x 0-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- mando invertido no ogol — RSSSF Goiás 4-1 Atlético-GO, ogol Atlético-GO 1-4 Goiás (1999-04-18); fica a RSSSF
- mando invertido no ogol — RSSSF Atlético-GO 3-3 Goiás, ogol Goiás 3-3 Atlético-GO (1999-06-13); fica a RSSSF
- vice pela Wikipédia (sem final de dois clubes): Vila Nova-GO

### 2000

- tabela publicada x jogos — Primeira fase / -: Goianésia tabela [13, 8, 3, 2, 22, 12] jogos [13, 8, 3, 2, 21, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Goiânia tabela [13, 7, 2, 4, 23, 20] jogos [13, 6, 3, 4, 23, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / -: Aparecida-GO tabela [13, 3, 2, 8, 8, 20] jogos [13, 3, 3, 7, 9, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Caldas tabela [13, 8, 4, 1, 25, 12] jogos [15, 9, 4, 2, 29, 14] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Goiás tabela [13, 10, 0, 3, 38, 9] jogos [15, 12, 0, 3, 41, 10] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Anapolina tabela [13, 9, 3, 1, 32, 14] jogos [15, 10, 4, 1, 38, 19] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Anápolis tabela [13, 9, 1, 3, 27, 10] jogos [15, 9, 2, 4, 27, 11] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [13, 9, 1, 3, 23, 11] jogos [15, 10, 2, 3, 24, 11] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Goiânia tabela [13, 6, 3, 4, 25, 19] jogos [15, 6, 4, 5, 30, 25] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Atlético-GO tabela [13, 6, 2, 5, 22, 23] jogos [15, 6, 2, 7, 23, 26] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Minaçu tabela [13, 5, 4, 4, 23, 17] jogos [15, 6, 4, 5, 25, 21] — a tabela conta 13 jogos e as fontes trazem 15
- tabela publicada x jogos — Segunda fase / -: Goiatuba EC tabela [13, 2, 3, 8, 13, 27] jogos [13, 2, 3, 8, 13, 28] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Aparecida-GO tabela [13, 1, 2, 10, 11, 38] jogos [13, 1, 2, 10, 12, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Final / -: Goiás tabela [26, 20, 1, 5, 68, 22] jogos [37, 30, 2, 5, 91, 29] — a tabela conta 26 jogos e as fontes trazem 37
- tabela publicada x jogos — Final / -: Anapolina tabela [26, 17, 5, 4, 53, 27] jogos [32, 18, 8, 6, 63, 38] — a tabela conta 26 jogos e as fontes trazem 32
- tabela publicada x jogos — Final / -: Anápolis tabela [26, 17, 3, 6, 56, 32] jogos [32, 18, 5, 9, 61, 40] — a tabela conta 26 jogos e as fontes trazem 32
- tabela publicada x jogos — Final / -: Caldas tabela [26, 13, 9, 4, 51, 29] jogos [32, 14, 9, 9, 56, 40] — a tabela conta 26 jogos e as fontes trazem 32
- tabela publicada x jogos — Final / -: Goiânia tabela [26, 13, 5, 8, 48, 39] jogos [30, 12, 8, 10, 57, 51] — a tabela conta 26 jogos e as fontes trazem 30
- tabela publicada x jogos — Final / -: Rioverdense tabela [26, 10, 4, 12, 34, 43] jogos [28, 11, 4, 13, 36, 45] — a tabela conta 26 jogos e as fontes trazem 28
- tabela publicada x jogos — Final / -: Atlético-GO tabela [26, 7, 7, 12, 36, 48] jogos [28, 7, 7, 14, 37, 51] — a tabela conta 26 jogos e as fontes trazem 28
- tabela publicada x jogos — Final / -: Minaçu tabela [26, 6, 9, 11, 34, 35] jogos [28, 7, 9, 12, 36, 40] — a tabela conta 26 jogos e as fontes trazem 28
- tabela publicada x jogos — Final / -: Goiatuba EC tabela [26, 4, 6, 16, 24, 49] jogos [26, 4, 6, 16, 24, 50] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anapolina
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Anápolis
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aparecida
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Caldas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goianésia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiatuba
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiás
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Goiânia
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Itumbiara
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Minaçu
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Rioverdense
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Inhumas
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Vila Nova
- Anapolina — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anapolina)
- Anápolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Anápolis)
- Aparecida — clube que o ogol não tem; entra só pela RSSSF
- Caldas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Caldas)
- Goianésia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goianésia)
- Goiatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiatuba EC)
- Goiás — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiás)
- Goiânia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Goiânia)
- Itumbiara — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Itumbiara)
- Minaçu — clube que o ogol não tem; entra só pela RSSSF
- Rioverdense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rioverdense)
- União Inhumas — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Inhumas)
- Vila Nova — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Vila Nova-GO)

### 2001

- tabela publicada x jogos — Segunda fase / -: Vila Nova-GO tabela [4, 3, 0, 1, 7, 3] jogos [20, 16, 1, 3, 48, 18] — a tabela conta 4 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Goiás tabela [4, 2, 2, 0, 6, 2] jogos [20, 9, 4, 7, 37, 26] — a tabela conta 4 jogos e as fontes trazem 20
- tabela publicada x jogos — Segunda fase / -: Anapolina tabela [4, 2, 1, 1, 6, 4] jogos [18, 12, 2, 4, 40, 20] — a tabela conta 4 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Real-GO tabela [4, 2, 0, 2, 5, 6] jogos [18, 8, 4, 6, 24, 24] — a tabela conta 4 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Grêmio Anápolis tabela [4, 1, 1, 2, 4, 6] jogos [18, 8, 2, 8, 32, 30] — a tabela conta 4 jogos e as fontes trazem 18
- tabela publicada x jogos — Segunda fase / -: Santa Helena tabela [4, 0, 0, 4, 1, 8] jogos [18, 8, 1, 9, 20, 30] — a tabela conta 4 jogos e as fontes trazem 18

### 2002

- só na RSSSF (não achado no ogol): Novo Horizonte None-None Goiás (2002-06-30)

### 2003

- tabela publicada x jogos — Fase final / -: Jataiense tabela [13, 4, 4, 5, 20, 22] jogos [13, 5, 4, 4, 20, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- só na RSSSF (não achado no ogol): Goiás 7-1 Real-GO (2003-03-09)

### 2004

- tabela publicada x jogos — Primeira fase / Grupo A: Anapolina tabela [17, 6, 4, 7, 27, 23] jogos [17, 6, 4, 7, 28, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Novo Horizonte tabela [17, 6, 4, 7, 30, 36] jogos [17, 5, 4, 8, 30, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Anapolina tabela [17, 6, 4, 7, 27, 23] jogos [17, 6, 4, 7, 28, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Novo Horizonte tabela [17, 6, 4, 7, 30, 36] jogos [17, 5, 4, 8, 30, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- só na RSSSF (não achado no ogol): Rioverdense None-None Real-GO (2004-03-24)

### 2005

- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [21, 10, 6, 5, 30, 21] jogos [21, 10, 6, 5, 31, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Goiás tabela [21, 10, 8, 3, 44, 24] jogos [21, 10, 8, 3, 45, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vila Nova-GO

### 2006

- tabela publicada x jogos — Primeira fase / Grupo A: Itumbiara tabela [17, 6, 2, 9, 24, 31] jogos [17, 6, 2, 9, 22, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2007

- placar diferente no ogol — Goiânia x Rioverdense (2007-02-24): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Goiás x Atlético-GO, ogol 2007-04-20); fica a do ogol

### 2008

- sem ocorrências

### 2009

- placar corrigido pelo ogol — Goiás x CRAC (2009-04-19): RSSSF 2-1, ogol 2-0; fica o do ogol, que fecha com a tabela publicada

### 2010

- sem ocorrências

### 2011

- mando invertido no ogol — RSSSF Goiás 1-1 Atlético-GO, ogol Atlético-GO 1-1 Goiás (2011-05-08); fica a RSSSF
- mando invertido no ogol — RSSSF Atlético-GO 1-1 Goiás, ogol Goiás 1-1 Atlético-GO (2011-05-15); fica a RSSSF
- placar corrigido pelo ogol — CRAC x Trindade (2011-04-03): RSSSF 3-0, ogol 3-1; fica o do ogol, que fecha com a tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Atlético-GO

### 2012

- placar corrigido pelo ogol — Vila Nova-GO x Atlético-GO (2012-02-11): RSSSF 1-2, ogol 0-1; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Anapolina x CRAC, ogol 2012-02-22); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Goiás

### 2013

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Goiás

### 2014

- sem ocorrências

### 2015

- sem ocorrências

### 2016

- sem ocorrências

### 2017

- sem ocorrências

### 2018

- placar corrigido pelo ogol — Atlético-GO x Aparecidense (2018-01-24): RSSSF 2-1, ogol 1-2; fica o do ogol, que fecha com a tabela publicada
- jogo só no ogol, incluído em FIRST STAGE: Iporá 1-1 Vila Nova-GO (2018-02-10)
- jogo só no ogol, incluído em FIRST STAGE: Atlético-GO 1-0 Itumbiara (2018-02-10)
- jogo só no ogol, incluído em FIRST STAGE: Goiás 1-0 Aparecidense (2018-02-10)
- jogo só no ogol, incluído em FIRST STAGE: Anapolina 1-2 Grêmio Anápolis (2018-02-10)
- jogo só no ogol, incluído em FIRST STAGE: Rio Verde-GO 0-2 Anápolis (2018-02-10)
- jogo só no ogol, incluído em FIRST STAGE: Aparecidense 0-0 Atlético-GO (2018-02-14)
- jogo só no ogol, incluído em FIRST STAGE: Itumbiara 2-0 Rio Verde-GO (2018-02-14)
- jogo só no ogol, incluído em FIRST STAGE: Anápolis 1-1 Goiás (2018-02-14)
- jogo só no ogol, incluído em FIRST STAGE: Vila Nova-GO 1-0 Anapolina (2018-02-15)
- jogo só no ogol, incluído em FIRST STAGE: Grêmio Anápolis 0-0 Iporá (2018-02-15)
- jogo só no ogol, incluído em FIRST STAGE: Anápolis 1-2 Atlético-GO (2018-02-17)
- jogo só no ogol, incluído em FIRST STAGE: Aparecidense 2-0 Anapolina (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE: Grêmio Anápolis 0-3 Goiás (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE: Itumbiara 1-4 Iporá (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE: Vila Nova-GO 1-1 Rio Verde-GO (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE: Goiás 2-1 Itumbiara (2018-02-24)
- jogo só no ogol, incluído em FIRST STAGE: Iporá 1-1 Aparecidense (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE: Anapolina 3-1 Anápolis (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE: Rio Verde-GO 1-2 Grêmio Anápolis (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE: Atlético-GO 1-1 Vila Nova-GO (2018-02-25)
- jogo só no ogol, incluído em FIRST STAGE: Anapolina 1-0 Iporá (2018-03-03)
- jogo só no ogol, incluído em FIRST STAGE: Rio Verde-GO 0-2 Atlético-GO (2018-03-03)
- jogo só no ogol, incluído em FIRST STAGE: Grêmio Anápolis 2-0 Anápolis (2018-03-04)
- jogo só no ogol, incluído em FIRST STAGE: Iporá 1-1 Rio Verde-GO (2018-03-07)
- jogo só no ogol, incluído em FIRST STAGE: Itumbiara 0-1 Vila Nova-GO (2018-03-07)
- jogo só no ogol, incluído em FIRST STAGE: Aparecidense 1-1 Grêmio Anápolis (2018-03-07)
- jogo só no ogol, incluído em FIRST STAGE: Goiás 1-1 Anapolina (2018-03-08)
- jogo só no ogol, incluído em FIRST STAGE: Vila Nova-GO 2-1 Grêmio Anápolis (2018-03-10)
- jogo só no ogol, incluído em FIRST STAGE: Rio Verde-GO 2-2 Anapolina (2018-03-11)
- jogo só no ogol, incluído em FIRST STAGE: Anápolis 2-0 Itumbiara (2018-03-11)
- jogo só no ogol, incluído em FIRST STAGE: Atlético-GO 1-0 Goiás (2018-03-11)
- jogo só no ogol, incluído em FIRST STAGE: Grêmio Anápolis 0-1 Itumbiara (2018-03-17)
- jogo só no ogol, incluído em FIRST STAGE: Iporá 4-1 Goiás (2018-03-18)
- jogo só no ogol, incluído em FIRST STAGE: Anapolina 2-0 Atlético-GO (2018-03-18)
- jogo só no ogol, incluído em FIRST STAGE: Aparecidense 2-1 Anápolis (2018-03-18)
- jogo só no ogol, incluído em FIRST STAGE: Goiás 4-0 Rio Verde-GO (2018-03-21)
- jogo só no ogol, incluído em FIRST STAGE: Anápolis 2-0 Vila Nova-GO (2018-03-21)
- jogo só no ogol, incluído em FIRST STAGE: Itumbiara 2-1 Aparecidense (2018-03-21)
- jogo só no ogol, incluído em FIRST STAGE: Atlético-GO 1-3 Iporá (2018-03-21)
- jogo só no ogol, incluído em Semifinal: Aparecidense 0-0 Vila Nova-GO (2018-03-24)
- jogo só no ogol, incluído em Semifinal: Anapolina 2-1 Goiás (2018-03-25)
- jogo só no ogol, incluído em Semifinal: Vila Nova-GO 2-2 Aparecidense (2018-03-28)
- jogo só no ogol, incluído em FIRST STAGE: Vila Nova-GO 1-3 Aparecidense (2018-03-28)
- jogo só no ogol, incluído em Semifinal: Goiás 2-1 Anapolina (2018-03-29)
- jogo só no ogol, incluído em Final: Aparecidense 0-0 Goiás (2018-04-01)
- jogo só no ogol, incluído em Final: Goiás 3-1 Aparecidense (2018-04-08)
- só na RSSSF (não achado no ogol): Anápolis 1-1 Iporá (2018-02-05)

### 2019

- sem ocorrências

### 2020

- tabela publicada x jogos — Fase final / -: Atlético-GO tabela [15, 11, 2, 2, 35, 11] jogos [15, 10, 3, 2, 35, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Goianésia tabela [15, 7, 3, 5, 17, 14] jogos [15, 7, 4, 4, 17, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2021

- tabela publicada x jogos — Fase final / -: Grêmio Anápolis tabela [16, 8, 4, 4, 18, 12] jogos [16, 7, 5, 4, 18, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Vila Nova-GO tabela [16, 8, 4, 4, 21, 11] jogos [16, 8, 5, 3, 21, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2022

- sem ocorrências

### 2023

- sem ocorrências

### 2024

- tabela publicada x jogos — Fase final / -: Goiânia tabela [15, 4, 4, 7, 15, 19] jogos [15, 3, 5, 7, 15, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Goiás tabela [13, 8, 4, 1, 19, 4] jogos [13, 8, 5, 0, 19, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2025

- sem ocorrências

### 2026

- jogo só no ogol, incluído em Primeira fase / Grupo C: Atlético-GO 2-0 Anápolis (2026-01-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Agro EC 1-2 Vila Nova-GO (2026-01-10)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Jataiense 1-1 CRAC (2026-01-10)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anapolina 1-0 Inhumas (2026-01-11)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Centro Oeste FC 0-0 Aparecidense (2026-01-11)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Goiás 4-0 Goiatuba EC (2026-01-11)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Goiatuba EC 1-1 Jataiense (2026-01-14)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anápolis 1-1 Centro Oeste FC (2026-01-14)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vila Nova-GO 3-2 Anapolina (2026-01-14)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Inhumas 0-1 Agro EC (2026-01-15)
- jogo só no ogol, incluído em Primeira fase / Grupo B: CRAC 0-0 Goiás (2026-01-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Aparecidense 1-2 Atlético-GO (2026-01-15)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Centro Oeste FC 0-3 Jataiense (2026-01-17)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Anápolis 1-3 Vila Nova-GO (2026-01-17)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Goiatuba EC 1-2 Anapolina (2026-01-17)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Aparecidense 1-1 Inhumas (2026-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Atlético-GO 1-1 Goiás (2026-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: CRAC 0-1 Agro EC (2026-01-18)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anapolina 2-0 CRAC (2026-01-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Jataiense 3-1 Atlético-GO (2026-01-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Agro EC 1-0 Goiatuba EC (2026-01-21)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Goiás 4-0 Centro Oeste FC (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Inhumas 1-2 Anápolis (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Vila Nova-GO 3-0 Aparecidense (2026-01-22)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Agro EC 2-0 Jataiense (2026-01-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anapolina 0-2 Goiás (2026-01-24)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Inhumas 2-2 Centro Oeste FC (2026-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Aparecidense 4-1 Goiatuba EC (2026-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Vila Nova-GO 1-2 Atlético-GO (2026-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Anápolis 2-0 CRAC (2026-01-25)
- jogo só no ogol, incluído em Primeira fase / Grupo B: CRAC 1-0 Aparecidense (2026-01-28)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Jataiense 3-0 Anapolina (2026-01-28)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Atlético-GO 2-0 Inhumas (2026-01-28)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Centro Oeste FC 0-2 Vila Nova-GO (2026-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Goiatuba EC 3-1 Anápolis (2026-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Goiás 1-0 Agro EC (2026-01-29)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Atlético-GO 0-0 CRAC (2026-01-31)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Jataiense 1-0 Inhumas (2026-02-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Centro Oeste FC 1-0 Goiatuba EC (2026-02-01)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Goiás 1-0 Vila Nova-GO (2026-02-01)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Agro EC 2-2 Anápolis (2026-02-02)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anapolina 3-1 Aparecidense (2026-02-02)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Inhumas 0-1 Goiás (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: CRAC 3-0 Centro Oeste FC (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Goiatuba EC 2-1 Atlético-GO (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Aparecidense 3-3 Agro EC (2026-02-07)
- jogo só no ogol, incluído em Primeira fase / Grupo B: Vila Nova-GO 4-1 Jataiense (2026-02-08)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Anápolis 2-0 Anapolina (2026-02-08)
- jogo só no ogol, incluído em Quartas de final: CRAC 1-1 Goiás (2026-02-11)
- jogo só no ogol, incluído em Quartas de final: Anapolina 1-1 Jataiense (2026-02-11)
- jogo só no ogol, incluído em Quartas de final: Agro EC 0-3 Atlético-GO (2026-02-12)
- jogo só no ogol, incluído em Quartas de final: Anápolis 0-2 Vila Nova-GO (2026-02-13)
- jogo só no ogol, incluído em Torneio de rebaixamento: Centro Oeste FC 4-2 Aparecidense (2026-02-14)
- jogo só no ogol, incluído em Quartas de final: Goiás 4-1 CRAC (2026-02-14)
- jogo só no ogol, incluído em Quartas de final: Jataiense 0-1 Anapolina (2026-02-15)
- jogo só no ogol, incluído em Quartas de final: Atlético-GO 1-1 Agro EC (2026-02-15)
- jogo só no ogol, incluído em Quartas de final: Vila Nova-GO 2-2 Anápolis (2026-02-16)
- jogo só no ogol, incluído em Torneio de rebaixamento: Aparecidense 4-0 Centro Oeste FC (2026-02-18)
- jogo só no ogol, incluído em Semifinal: Anapolina 2-2 Goiás (2026-02-21)
- jogo só no ogol, incluído em Torneio de rebaixamento: CRAC 1-2 Jataiense (2026-02-21)
- jogo só no ogol, incluído em Torneio de rebaixamento: Anápolis 0-2 Agro EC (2026-02-22)
- jogo só no ogol, incluído em Semifinal: Atlético-GO 2-0 Vila Nova-GO (2026-02-22)
- jogo só no ogol, incluído em Semifinal: Goiás 1-1 Anapolina (2026-02-28)
- jogo só no ogol, incluído em Torneio de rebaixamento: Jataiense 1-0 CRAC (2026-02-28)
- jogo só no ogol, incluído em Torneio de rebaixamento: Agro EC 2-4 Anápolis (2026-02-28)
- jogo só no ogol, incluído em Semifinal: Vila Nova-GO 0-0 Atlético-GO (2026-03-01)
- jogo só no ogol, incluído em Torneio de rebaixamento: Agro EC 2-1 Jataiense (2026-03-04)
- jogo só no ogol, incluído em Final: Atlético-GO 0-2 Goiás (2026-03-07)
- jogo só no ogol, incluído em Torneio de rebaixamento: Jataiense 1-0 Agro EC (2026-03-08)
- jogo só no ogol, incluído em Final: Goiás 0-0 Atlético-GO (2026-03-15)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-go1-<nome>". Nunca com o nome exato de outro clube.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.
