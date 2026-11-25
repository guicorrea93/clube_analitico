# Campeonato Panamenho (ANAPROF e LPF) — coleta de dados

Gerado por `python coleta/pan-1/importar.py`. Pacote em `data/coleta/pan-1/pacote/`.

**Edições:** 66, uma por título, como a lista de campeões da RSSSF (`panamachamp.html`, 63 títulos desde 1988, mais os 2 da LINFUNA no total), que é também a contagem da imprensa local (Tauro 17, Árabe Unido 15 com a LINFUNA). Escopo decidido em 25/11/2026: de 1988 (primeira temporada da ANAPROF) em diante; antes só havia ligas da capital e de Colón, e os campeões nacionais de 1952 a 1987 são desconhecidos. Um campeão por temporada até 2000/01; Apertura e Clausura de 2001 em diante, uma edição cada (a liga passou a contar os dois torneios de 2001 a 2006 como títulos; a final entre os dois campeões fica fora, como supercopa). Em 2009 houve dois Aperturas, o último da ANAPROF e o primeiro da LPF; o Apertura 2020 (pandemia) entra sem campeão; depois do Clausura 2025 veio o Clausura 2026. As duas temporadas da LINFUNA (1994/95 e 1995/96, a liga paralela do racha, reconhecida pela FIFA na época) entram como edições à parte, só com a final.

**Edições sem jogos (15):** de 1988 a 1995/96 (sem página, ou só a classificação), 1999/00, 2001 (sem página) e de 2010 Apertura a 2012 Clausura (só as tabelas). 1996/97 entra incompleta (faltam as rodadas 5 a 7). O vice é o da lista de campeões.

**Fontes:** RSSSF (`data/coleta/pan-1/rsssf/`: a lista de campeões e as páginas das temporadas, casadas pelo título). A ESPN não cobre o Panamá.

**Clubes:** nomes e identidades no começo de `coleta/pan-1/clubes_pan.py`. Homônimos de clubes de outros países levam o país: Alianza de Panamá, Atlético Nacional de Panamá, SD Atlético Nacional de Panamá.

**Pontos:** 2 ou 3 por vitória conforme a tabela publicada de cada temporada.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1988 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Plaza Amador | lista de campeões da RSSSF (campeão e vice) |
| 1989 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Tauro | lista de campeões da RSSSF (campeão e vice) |
| 1990 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Plaza Amador | lista de campeões da RSSSF (campeão e vice) |
| 1991 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Tauro | lista de campeões da RSSSF (campeão e vice) |
| 1992 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Plaza Amador | lista de campeões da RSSSF (campeão e vice) |
| 1993 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Euro Kickers | lista de campeões da RSSSF (campeão e vice) |
| 1994/95 | 0 | 0 (0) | 0 | 0 | 0 / 0 | San Francisco | lista de campeões da RSSSF (campeão e vice) |
| 1994/95 LINFUNA | 2 | 1 (1) | 1 | 1 | 0 / 0 | Árabe Unido | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1995/96 | 0 | 0 (0) | 0 | 0 | 0 / 0 | San Francisco | lista de campeões da RSSSF (campeão e vice) |
| 1995/96 LINFUNA | 2 | 1 (1) | 1 | 1 | 0 / 0 | Árabe Unido | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996/97 | 12 | 100 (100) | 277 | 1 | 0 / 0 | Tauro | RSSSF (panama97) |
| 1997/98 | 12 | 95 (95) | 227 | 2 | 0 / 2 | Tauro | RSSSF (panama98) |
| 1998/99 | 10 | 111 (111) | 268 | 164 | 3 / 0 | Árabe Unido | RSSSF (panama99) |
| 1999/00 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Tauro | RSSSF (panama00) |
| 2000/01 | 10 | 112 (112) | 328 | 133 | 2 / 0 | Panamá Viejo | RSSSF (panama01) |
| 2001 Apertura | 0 | 0 (0) | 0 | 0 | 0 / 0 | Árabe Unido | lista de campeões da RSSSF (campeão e vice) |
| 2001 Clausura | 0 | 0 (0) | 0 | 0 | 0 / 0 | Árabe Unido | lista de campeões da RSSSF (campeão e vice) |
| 2002 Apertura | 8 | 45 (45) | 118 | 0 | 2 / 0 | Árabe Unido | RSSSF (panama02) |
| 2002 Clausura | 8 | 70 (70) | 193 | 0 | 2 / 0 | Plaza Amador | RSSSF (panama02) |
| 2003 Apertura | 8 | 70 (70) | 175 | 0 | 2 / 0 | Tauro | RSSSF (panama03) |
| 2003 Clausura | 8 | 61 (61) | 180 | 0 | 1 / 0 | Tauro | RSSSF (panama03) |
| 2004 Apertura | 10 | 95 (95) | 223 | 47 | 0 / 1 | Árabe Unido | RSSSF (panama04) |
| 2004 Clausura | 10 | 96 (95) | 289 | 2 | 1 / 0 | Árabe Unido | RSSSF (panama04) |
| 2005 Apertura | 10 | 95 (95) | 223 | 0 | 1 / 0 | Plaza Amador | RSSSF (panama05) |
| 2005 Clausura | 9 | 77 (77) | 226 | 2 | 1 / 0 | San Francisco | RSSSF (panama05) |
| 2006 Apertura | 10 | 95 (95) | 215 | 0 | 1 / 0 | San Francisco | RSSSF (panama06) |
| 2006 Clausura | 10 | 95 (95) | 262 | 12 | 1 / 0 | Tauro | RSSSF (panama06) |
| 2007 Apertura | 10 | 97 (95) | 263 | 7 | 1 / 0 | Tauro | RSSSF (panama07) |
| 2007 Clausura | 10 | 96 (95) | 250 | 124 | 1 / 0 | San Francisco | RSSSF (panama07) |
| 2008 Apertura | 10 | 70 (70) | 184 | 98 | 1 / 2 | San Francisco | RSSSF (panama08) |
| 2008 Clausura | 10 | 96 (95) | 273 | 166 | 1 / 0 | Árabe Unido | RSSSF (panama08) |
| 2009 Apertura ANAPROF | 10 | 95 (95) | 297 | 169 | 1 / 0 | San Francisco | RSSSF (panama09) |
| 2009 Apertura | 10 | 95 (95) | 284 | 137 | 1 / 0 | Árabe Unido | RSSSF (panama09) |
| 2010 Clausura | 10 | 95 (95) | 232 | 0 | 1 / 0 | Árabe Unido | RSSSF (panama2010) |
| 2010 Apertura | 10 | 0 (0) | 0 | 0 | 0 / 0 | Tauro | RSSSF (panama2010) |
| 2011 Clausura | 10 | 0 (0) | 0 | 0 | 0 / 0 | San Francisco | RSSSF (panama2010) |
| 2011 Apertura | 9 | 0 (0) | 0 | 0 | 0 / 0 | CD Universitario | RSSSF (panama2012) |
| 2012 Clausura | 9 | 0 (0) | 0 | 0 | 0 / 0 | Tauro | RSSSF (panama2012) |
| 2012 Apertura | 10 | 95 (95) | 228 | 5 | 1 / 0 | Árabe Unido | RSSSF (panama2013) |
| 2013 Clausura | 10 | 95 (95) | 220 | 5 | 1 / 0 | Sporting San Miguelito | RSSSF (panama2013) |
| 2013 Apertura | 10 | 95 (95) | 196 | 1 | 1 / 0 | Tauro | RSSSF (panama2014) |
| 2014 Clausura | 10 | 95 (95) | 197 | 1 | 1 / 0 | CD Universitario | RSSSF (panama2014) |
| 2014 Apertura | 10 | 95 (95) | 212 | 1 | 1 / 0 | San Francisco | RSSSF (panama2015) |
| 2015 Clausura | 10 | 95 (95) | 223 | 3 | 1 / 0 | Árabe Unido | RSSSF (panama2015) |
| 2015 Apertura | 10 | 96 (95) | 220 | 0 | 1 / 0 | Árabe Unido | RSSSF (panama2016) |
| 2016 Clausura | 10 | 95 (95) | 195 | 0 | 1 / 0 | Plaza Amador | RSSSF (panama2016) |
| 2016 Apertura | 10 | 95 (95) | 186 | 0 | 1 / 0 | Árabe Unido | RSSSF (panama2017) |
| 2017 Clausura | 10 | 95 (95) | 209 | 0 | 1 / 0 | Tauro | RSSSF (panama2017) |
| 2017 Apertura | 10 | 95 (95) | 200 | 0 | 1 / 0 | CD Universitario | RSSSF (panama2018) |
| 2018 Clausura | 10 | 95 (95) | 205 | 1 | 1 / 0 | CAI La Chorrera | RSSSF (panama2018) |
| 2018 Apertura | 10 | 97 (97) | 212 | 3 | 1 / 0 | Tauro | RSSSF (panama2019) |
| 2019 Clausura | 10 | 97 (97) | 230 | 2 | 1 / 0 | CAI La Chorrera | RSSSF (panama2019) |
| 2019 Apertura | 10 | 97 (97) | 208 | 2 | 1 / 0 | Tauro | RSSSF (panama2020) |
| 2020 Apertura | 10 | 40 (40) | 79 | 0 | 0 / 0 | None | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2020 Clausura | 10 | 52 (52) | 111 | 0 | 1 / 0 | CAI La Chorrera | RSSSF (panama2020) |
| 2021 Apertura | 12 | 103 (103) | 222 | 0 | 2 / 0 | Plaza Amador | RSSSF (panama2021) |
| 2021 Clausura | 12 | 103 (103) | 188 | 0 | 2 / 0 | Tauro | RSSSF (panama2021) |
| 2022 Apertura | 12 | 103 (103) | 222 | 0 | 2 / 0 | Alianza de Panamá | RSSSF (panama2022) |
| 2022 Clausura | 12 | 103 (103) | 229 | 0 | 2 / 0 | CAI La Chorrera | RSSSF (panama2022) |
| 2023 Apertura | 12 | 103 (103) | 237 | 0 | 2 / 0 | CAI La Chorrera | RSSSF (panama2023) |
| 2023 Clausura | 12 | 103 (103) | 273 | 0 | 2 / 0 | CAI La Chorrera | RSSSF (panama2023) |
| 2024 Apertura | 12 | 103 (103) | 248 | 0 | 2 / 0 | Tauro | RSSSF (panama2024) |
| 2024 Clausura | 12 | 103 (103) | 216 | 0 | 2 / 0 | CAI La Chorrera | RSSSF (panama2024) |
| 2025 Apertura | 12 | 103 (103) | 247 | 0 | 2 / 0 | Plaza Amador | RSSSF (panama2025) |
| 2025 Clausura | 12 | 103 (103) | 262 | 0 | 2 / 0 | Plaza Amador | RSSSF (panama2025) |
| 2026 Clausura | 12 | 103 (103) | 277 | 0 | 2 / 0 | Plaza Amador | RSSSF (panama2026) |

## Conferência e correções, edição a edição

### 1988

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 1989

- sem página da RSSSF: só o campeão e o vice

### 1990

- sem página da RSSSF: só o campeão e o vice

### 1991

- sem página da RSSSF: só o campeão e o vice

### 1992

- sem página da RSSSF: só o campeão e o vice

### 1993

- sem página da RSSSF: só o campeão e o vice

### 1994/95

- sem página da RSSSF: só o campeão e o vice

### 1994/95 LINFUNA

- liga paralela da LINFUNA (racha de 1994-96, reconhecida pela FIFA na época): só a final

### 1995/96

- sem página da RSSSF: só o campeão e o vice

### 1995/96 LINFUNA

- liga paralela da LINFUNA (racha de 1994-96, reconhecida pela FIFA na época): só a final

### 1996/97

- sem ocorrências

### 1997/98

- dois jogos da primeira fase estão na página só com o resultado, sem placar ("Pan A ppd Nacional [away win]" e "Ejecutivo - Chiriqui [draw]"): ficam fora; a tabela publicada os conta (Atlético Nacional, Chiriquí, Pan de Azúcar e Ejecutivo com um jogo a menos nos jogos lidos)
- tabela publicada x jogos — panama98:19: Atlético Nacional de Panamá tabela [14, 7, 3, 4, 11, 10] jogos [13, 6, 3, 4, 11, 10] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — panama98:19: Chiriquí FC tabela [14, 3, 5, 6, 13, 16] jogos [13, 3, 4, 6, 13, 16] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — panama98:28: Pan de Azúcar tabela [14, 3, 7, 4, 19, 21] jogos [13, 3, 7, 3, 19, 21] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — panama98:28: Ejecutivo Jr tabela [14, 1, 9, 4, 15, 16] jogos [13, 1, 8, 4, 15, 16] — faltam 1 jogo(s) do clube na página

### 1998/99

- sem ocorrências

### 1999/00

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2000/01

- abandonado/suspenso, sem valer — Plaza Amador Tauro (2000-10-13): abandoned 1-0 after 45 minutes because of rain
- abandonado/suspenso, sem valer — San Francisco Tauro (2001-01-21): abandoned at 0-2 in 45' after pitch invasion

### 2001 Apertura

- sem página da RSSSF: só o campeão e o vice

### 2001 Clausura

- sem página da RSSSF: só o campeão e o vice

### 2002 Apertura

- sem ocorrências

### 2002 Clausura

- sem ocorrências

### 2003 Apertura

- sem ocorrências

### 2003 Clausura

- sem ocorrências

### 2004 Apertura

- Tauro: os jogos da página somam 26-12, a tabela publicada diz 25-11 (um placar com um gol a mais de cada lado; fica como a página)
- tabela publicada x jogos — panama04:18: Tauro tabela [18, 10, 3, 5, 25, 11] jogos [18, 10, 3, 5, 26, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2004 Clausura

- não jogado — Plaza Amador Atlético Veragüense (2004-10-21): not played due to irrelevance

### 2005 Apertura

- decidido fora de campo — Sporting San Miguelito Colón River (2005-05-07): not played, awarded 2-0

### 2005 Clausura

- sem ocorrências

### 2006 Apertura

- sem ocorrências

### 2006 Clausura

- sem ocorrências

### 2007 Apertura

- abandonado/suspenso, sem valer — Plaza Amador Atlético Chiriquí (2007-03-02): abandoned at 0-0 in 63' due
- não jogado — Plaza Amador Atlético Chiriquí (2007-03-23): annulled; originally 1-0 after; jogo repetido (o primeiro foi suspenso)

### 2007 Clausura

- abandonado/suspenso, sem valer — CD Universitario San Francisco (2007-11-04): abandoned at 1-0 in 53' due to rain

### 2008 Apertura

- San Francisco e Plaza Amador: os jogos da página dão ao San Francisco um empate a menos e uma derrota a mais, e ao Plaza Amador o contrário, do que a tabela publicada (com os mesmos gols); fica como a página
- tabela publicada x jogos — panama08:20: San Francisco tabela [13, 5, 7, 1, 19, 15] jogos [13, 5, 6, 2, 19, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — panama08:20: Plaza Amador tabela [13, 4, 6, 3, 13, 9] jogos [13, 4, 7, 2, 13, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — panama08:235: San Francisco tabela [13, 5, 7, 1, 19, 15] jogos [13, 5, 6, 2, 19, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — panama08:235: Plaza Amador tabela [13, 4, 6, 3, 13, 9] jogos [13, 4, 7, 2, 13, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2008 Clausura

- abandonado/suspenso, sem valer — Árabe Unido CD Universitario (2008-08-17): abandoned at 1-1 due to rain

### 2009 Apertura ANAPROF

- sem ocorrências

### 2009 Apertura

- sem ocorrências

### 2010 Clausura

- sem ocorrências

### 2010 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2011 Apertura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Clausura

- só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)

### 2012 Apertura

- sem ocorrências

### 2013 Clausura

- sem ocorrências

### 2013 Apertura

- sem ocorrências

### 2014 Clausura

- sem ocorrências

### 2014 Apertura

- sem ocorrências

### 2015 Clausura

- sem ocorrências

### 2015 Apertura

- abandonado/suspenso, sem valer — San Francisco Sporting San Miguelito (2015-09-30): abandoned at 0-0 at half-time due to floodlight failure

### 2016 Clausura

- sem ocorrências

### 2016 Apertura

- sem ocorrências

### 2017 Clausura

- sem ocorrências

### 2017 Apertura

- sem ocorrências

### 2018 Clausura

- decidido fora de campo — Alianza de Panamá Tauro (2018-02-03): awarded 3-0, originally 3-3; the licenses

### 2018 Apertura

- decidido fora de campo — Costa del Este CAI La Chorrera (2018-08-26): awarded 3-0, originally 1-2; C.A.I. used

### 2019 Clausura

- decidido fora de campo — Plaza Amador Santa Gema (2019-02-02): awarded 3-0, Santa Gema dns
- decidido fora de campo — Costa del Este Santa Gema (2019-03-13): awarded 3-0, Santa Gema suspended
- decidido fora de campo — Tauro Santa Gema (2019-04-06): awarded 3-0, Santa Gema suspended
- decidido fora de campo — CD Universitario Santa Gema (2019-04-13): awarded 3-0, Santa Gema suspended
- decidido fora de campo — Santa Gema CAI La Chorrera (2019-04-17): awarded 0-3, Santa Gema excluded
- decidido fora de campo — Sporting San Miguelito Santa Gema (2019-04-28): awarded 3-0, Santa Gema excluded
- decidido fora de campo — Santa Gema Costa del Este (2019-05-02): awarded 0-3, Santa Gema excluded
- decidido fora de campo — San Francisco Santa Gema (2019-05-10): awarded 3-0, Santa Gema excluded

### 2019 Apertura

- decidido fora de campo — Plaza Amador Sporting San Miguelito (2019-09-28): awarded 3-0, originally 0-1

### 2020 Apertura

- sem ocorrências

### 2020 Clausura

- sem ocorrências

### 2021 Apertura

- sem ocorrências

### 2021 Clausura

- sem ocorrências

### 2022 Apertura

- sem ocorrências

### 2022 Clausura

- sem ocorrências

### 2023 Apertura

- sem ocorrências

### 2023 Clausura

- sem ocorrências

### 2024 Apertura

- decidido fora de campo — Sporting San Miguelito Árabe Unido (2024-01-20): awarded 0-3, originally 2-2; Sporting

### 2024 Clausura

- sem ocorrências

### 2025 Apertura

- sem ocorrências

### 2025 Clausura

- decidido fora de campo — Veraguas United CAI La Chorrera (2025-08-11): awarded 0-3; originally 1-0

### 2026 Clausura

- sem ocorrências

