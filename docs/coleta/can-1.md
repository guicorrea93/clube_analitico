# Campeonato Canadense (CPSL, CSL e CPL) — coleta de dados

Gerado por `python coleta/can-1/importar.py`. Pacote em `data/coleta/can-1/pacote/`.

**Edições:** 15, uma por título, como o bloco "CPSL/CSL 1983-1992 and CPL since 2019" da lista de campeões da RSSSF (`canchamp.html`): as três tentativas de uma liga profissional nacional de 1ª divisão. Escopo decidido em 25/11/2026: a Canadian Professional Soccer League de 1983 (uma temporada, abandonada no meio; o título saiu nos playoffs), a Canadian Soccer League de 1987 a 1992 e a Canadian Premier League de 2019 a 2026 (a liga atual, 1ª divisão sancionada pela Canada Soccer). Ficam fora a National Soccer League (1922-1997) e as ligas que a seguiram (1998-2025), de clubes quase só da região de Toronto; o Canadian Championship (copa, fase 2); e os clubes canadenses da MLS (já no `usa-1`).

**Edições sem jogos da fase regular (7):** 1987 a 1992 (a página do CSL só tem as tabelas e os playoffs; os playoffs entram) e 1983 (temporada abandonada no meio).

**Fontes:** RSSSF (`data/coleta/can-1/rsssf/`) e ogol (`data/cache/ogol-can-1/`: a fase regular de 2025, que a página da RSSSF não tem, e a temporada 2026, que ela ainda não tem; campeão e vice de 2026 também na imprensa, TSN e CBC). A ESPN não cobre a CPL.

**Clubes:** nomes e identidades no começo de `coleta/can-1/clubes_can.py`. Vancouver 86ers = Vancouver Whitecaps (o mesmo do `usa-1`); o Toronto Blizzard do CSL leva "(CSL)" (o da NASL está no `usa-1`).

**Pontos:** 2 ou 3 por vitória conforme a tabela publicada de cada temporada.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1983 | 6 | 37 (37) | 121 | 0 | 0 / 0 | Edmonton Eagles | RSSSF (cpsl) |
| 1987 | 8 | 5 (5) | 17 | 0 | 0 / 0 | Calgary Kickers | RSSSF (csl) |
| 1988 | 9 | 5 (5) | 16 | 0 | 0 / 0 | Vancouver Whitecaps | lista de campeões (RSSSF e Wikipédia) |
| 1989 | 10 | 9 (9) | 29 | 0 | 0 / 0 | Vancouver Whitecaps | lista de campeões (RSSSF e Wikipédia) |
| 1990 | 11 | 14 (14) | 45 | 0 | 0 / 0 | Vancouver Whitecaps | lista de campeões (RSSSF e Wikipédia) |
| 1991 | 8 | 11 (11) | 37 | 0 | 0 / 0 | Vancouver Whitecaps | lista de campeões (RSSSF e Wikipédia) |
| 1992 | 6 | 6 (6) | 10 | 0 | 0 / 0 | Winnipeg Fury | RSSSF (csl) |
| 2019 | 7 | 100 (100) | 250 | 0 | 4 / 0 | Forge FC | RSSSF (can2019) |
| 2020 | 8 | 35 (35) | 92 | 0 | 2 / 0 | Forge FC | RSSSF (can2020) |
| 2021 | 8 | 115 (115) | 293 | 0 | 1 / 0 | Pacific FC | RSSSF (can2021) |
| 2022 | 8 | 117 (117) | 291 | 0 | 1 / 0 | Forge FC | RSSSF (can2022) |
| 2023 | 8 | 117 (117) | 303 | 3 | 1 / 0 | Forge FC | RSSSF (can2023) |
| 2024 | 8 | 117 (117) | 296 | 0 | 1 / 0 | Cavalry FC | RSSSF (can2024) |
| 2025 | 8 | 117 (117) | 352 | 0 | 1 / 0 | Atlético Ottawa | RSSSF (can2025) |
| 2026 | 8 | 117 (117) | 373 | 0 | 0 / 0 | Cavalry FC | calculada (fase alcançada, pontos, saldo, gols pró) |

## Conferência e correções, edição a edição

### 1983

- sem ocorrências

### 1987

- sem ocorrências

### 1988

- sem ocorrências

### 1989

- sem ocorrências

### 1990

- sem ocorrências

### 1991

- sem ocorrências

### 1992

- sem ocorrências

### 2019

- sem ocorrências

### 2020

- sem ocorrências

### 2021

- sem ocorrências

### 2022

- sem ocorrências

### 2023

- sem ocorrências

### 2024

- sem ocorrências

### 2025

- fase regular do ogol (a página da RSSSF só tem a tabela e os playoffs)

### 2026

- só o ogol (a RSSSF ainda não tem a página de 2026); campeão e vice também na imprensa (TSN, CBC)

