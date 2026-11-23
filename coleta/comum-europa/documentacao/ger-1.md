# Campeonato Alemão (`ger-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ger-1/pacote/` e do importador `coleta/ger-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ger-1.md`.

## 1. O que temos

- **Edições:** 124, de 1963/64 a 1962/63.
- **Jogos:** 20303; **gols:** 63752; **gols com autor:** 55851 (88%); **cartões:** 30251; **jogos com estatísticas** (chutes, faltas, escanteios): 7649.
- **Clubes:** 194; **artilheiros:** 63 temporadas com artilheiro (74 linhas, com empates).
- **Classificação final:** 116 temporadas; **rodada a rodada:** 63 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2502 linhas, de 147 tabelas.
- **Observação da competição:** Campeonato alemão desde 1902/03: até 1962/63, ligas regionais e fase final (mata-mata e/ou grupos) entre os campeões regionais (no pacote, a fase final e o campeão oficial); desde 1963/64, a Bundesliga. Não inclui a Alemanha Oriental (DDR-Oberliga) nem os play-offs de rebaixamento (Relegation) contra clubes da 2. Bundesliga.

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1963/64-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ger-1/` para os escudos;
- ESPN (liga `ger.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: tabela final de cada temporada e lista de artilheiros de cada temporada (com o clube); até 1962/63, os jogos da fase final (tablesd/duit1903.html ... duit1944.html e duithist4763.html) e a lista de campeões (duitchamp.html);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista de campeões (com os gols do artilheiro); até 1962/63, a ficha das partidas com "football box" (estádio, público, árbitro, gols com minuto).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Berlim). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 0, saldo de gols em 57, média de gols em 6); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 181 tabelas fecham com os jogos e 7 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1971/72, 1902/03, 1903/04, 1904/05, 1905/06, 1906/07, 1907/08, 1908/09, 1909/10, 1910/11, 1911/12, 1912/13, 1913/14, 1919/20, 1920/21, 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929/30, 1930/31, 1931/32, 1932/33, 1941/42, 1942/43, 1943/44, 1947/48, 1948/49, 1949/50.
- Temporadas com alguma tabela divergente: 1969/70, 1971/72, 1979/80, 1993/94, 1956/57, 1962/63.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 54 | 98% | 0% | 0% | 19% | 4% | 28% | 0% | 10% | 0.0 |
| 1910s | 34 | 100% | 0% | 0% | 6% | 6% | 6% | 0% | 1% | 0.0 |
| 1920s | 119 | 100% | 0% | 0% | 7% | 7% | 7% | 0% | 5% | 0.0 |
| 1930s | 415 | 19% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 174 | 66% | 0% | 0% | 14% | 14% | 14% | 0% | 12% | 0.0 |
| 1950s | 221 | 94% | 0% | 0% | 3% | 3% | 3% | 0% | 3% | 0.0 |
| 1960s | 2076 | 100% | 0% | 97% | 0% | 0% | 0% | 0% | 93% | 0.0 |
| 1970s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 95% | 0.0 |
| 1980s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 95% | 0.0 |
| 1990s | 3134 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 88% | 0.0 |
| 2000s | 3060 | 100% | 90% | 100% | 90% | 72% | 20% | 90% | 89% | 3.6 |
| 2010s | 3060 | 100% | 100% | 100% | 100% | 97% | 0% | 100% | 99% | 3.8 |
| 2020s | 1836 | 100% | 100% | 100% | 100% | 84% | 0% | 100% | 100% | 4.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1963/64 a 1964/65: 16 clubes
- 1965/66 a 1990/91: 18 clubes
- 1991/92: 20 clubes
- 1992/93 a 2025/26: 18 clubes
- 1902/03: 6 clubes
- 1903/04: 8 clubes
- 1904/05: 7 clubes
- 1905/06: 8 clubes
- 1906/07: 6 clubes
- 1907/08 a 1908/09: 8 clubes
- 1909/10: 9 clubes
- 1910/11 a 1911/12: 8 clubes
- 1912/13: 7 clubes
- 1913/14: 8 clubes
- 1914/15 a 1918/19:  clubes
- 1919/20: 8 clubes
- 1920/21: 7 clubes
- 1921/22: 8 clubes
- 1922/23: 6 clubes
- 1923/24: 7 clubes
- 1924/25 a 1937/38: 16 clubes
- 1938/39 a 1939/40: 18 clubes
- 1940/41: 20 clubes
- 1941/42: 8 clubes
- 1942/43: 29 clubes
- 1943/44: 31 clubes
- 1944/45 a 1946/47:  clubes
- 1947/48: 14 clubes
- 1948/49: 10 clubes
- 1949/50: 16 clubes
- 1950/51 a 1952/53: 8 clubes
- 1953/54: 6 clubes
- 1954/55 a 1962/63: 9 clubes

**Pontos por vitória:**

- 1963/64 a 1994/95: 2
- 1995/96 a 2025/26: 3
- 1902/03 a 1962/63: 2

**Nome oficial:**

- 1963/64 a 2025/26: Bundesliga
- 1902/03 a 1962/63: Campeonato Alemão

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1902/03: Primeira fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1903/04: Primeira fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1904/05: Quartas de final (mata_mata, jogo_unico); Fase intermediária (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1905/06: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1906/07: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1907/08: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1908/09: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1909/10: Fase preliminar (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1910/11: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1911/12: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1912/13: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1913/14: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1919/20: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1920/21: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1921/22: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1922/23: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1923/24: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1924/25: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1925/26: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1926/27: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1927/28: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1928/29: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1929/30: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1930/31: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1931/32: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1932/33: Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1933/34: Fase de grupos (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1934/35: Fase de grupos (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1935/36: Fase de grupos (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1936/37: Fase de grupos (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1937/38: Fase de grupos (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1938/39: Fase de grupos (grupos, pontos_corridos); Final de grupo (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1939/40: Fase de grupos (grupos, pontos_corridos); Final de grupo (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1940/41: Fase de grupos (grupos, pontos_corridos); Final de grupo (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1941/42: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1942/43: Fase preliminar (mata_mata, jogo_unico); Eliminatória (mata_mata, jogo_unico); Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1943/44: Fase preliminar (mata_mata, jogo_unico); Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1947/48: 1ª eliminatória (mata_mata, jogo_unico); 2ª eliminatória (mata_mata, jogo_unico); 3ª eliminatória (mata_mata, jogo_unico); Primeira fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1948/49: Eliminatória (mata_mata, jogo_unico); 2ª eliminatória (mata_mata, jogo_unico); Primeira fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1949/50: Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1950/51: Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1951/52: Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1952/53: Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1953/54: Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1954/55: 1ª eliminatória (mata_mata, jogo_unico); 2ª eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1955/56: 1ª eliminatória (mata_mata, jogo_unico); 2ª eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1956/57: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1957/58: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1958/59: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1959/60: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1960/61: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1961/62: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1962/63: Eliminatória (mata_mata, jogo_unico); Fase de grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- jogo único; empate com prorrogação e novo jogo: 171 temporadas
- pontos, saldo de gols, gols pró: 57 temporadas
- pontos (2 por vitória), depois média de gols: 21 temporadas
- pontos, média de gols (goal average): 6 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1964/65: Hertha rebaixado por perda da licença; Karlsruhe e Schalke, 15º e 16º, ficaram com a ampliação para 18 clubes
- 1971/72: punições: Arminia Bielefeld -19 pontos; Arminia Bielefeld rebaixado de ofício e sem pontos (escândalo de 1971)
- 1979/80: 3º lugar dividido entre Stuttgart e Kaiserslautern (41 pontos e 75-53 de gols; não havia outro critério)
- 1981/82: Relegation (16º da Bundesliga x 3º da 2. Bundesliga): Bayer 04 Leverkusen x Kickers Offenbach, 1-0 e 2-1 (total 3-1); ficou com a vaga: Bayer 04 Leverkusen (Wikipédia de)
- 1993/94: punições: Dynamo Dresden -4 pontos
- 1994/95: Dynamo Dresden, 18º, também perdeu a licença
- 1999/00: punições: Eintracht Frankfurt -2 pontos
- 2003/04: punições: Kaiserslautern -3 pontos
- 1903/04: final não jogada: a federação anulou a fase final depois do protesto do Karlsruher FV; sem campeão
- 1914/15: sem campeonato (Primeira Guerra Mundial)
- 1915/16: sem campeonato (Primeira Guerra Mundial)
- 1916/17: sem campeonato (Primeira Guerra Mundial)
- 1917/18: sem campeonato (Primeira Guerra Mundial)
- 1918/19: sem campeonato (Primeira Guerra Mundial)
- 1921/22: título não atribuído: a final entre Hamburger SV e Nürnberg teve dois jogos sem vencedor (2-2 e o segundo interrompido em 1-1); a federação deu o título ao Hamburgo, que renunciou a ele
- 1944/45: sem campeonato (Segunda Guerra Mundial)
- 1945/46: sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)
- 1946/47: sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)

## 6. Campeões, rebaixados e punições

**Títulos:**

- Bayern de Munique: 35
- Nuremberg: 9
- Borussia Dortmund: 8
- Schalke 04: 7
- Hamburgo: 6
- Borussia Mönchengladbach: 5
- Stuttgart: 5
- Werder Bremen: 4
- Kaiserslautern: 4
- Colônia: 3
- VfB Leipzig: 3
- Greuther Fürth: 3
- Viktoria Berlin: 2
- Hertha Berlin: 2
- Hannover 96: 2
- Dresdner SC: 2
- 1860 Munique: 1
- Eintracht Braunschweig: 1
- Wolfsburg: 1
- Bayer Leverkusen: 1
- Union 92 Berlin: 1
- Freiburger FC: 1
- Phönix Karlsruhe: 1
- Karlsruher FV: 1
- Holstein Kiel: 1
- Fortuna Düsseldorf: 1
- Rapid Viena: 1
- VfR Mannheim: 1
- Rot-Weiss Essen: 1
- Eintracht Frankfurt: 1
- Sem campeão: 1903/04, 1914/15, 1915/16, 1916/17, 1917/18, 1918/19, 1921/22, 1944/45, 1945/46, 1946/47

**Rebaixamentos:** 157 no total; quem mais caiu: Nuremberg (9), Arminia Bielefeld (8), Hertha Berlin (7), Bochum (7), Colônia (7).

**Punições em pontos:**

- 1971/72: Arminia Bielefeld -19
- 1993/94: Dynamo Dresden -4
- 1999/00: Eintracht Frankfurt -2
- 2003/04: Kaiserslautern -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ger-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Resultados decididos fora de campo (`TRIBUNAL`)

- **1970/71 · Bor. Monchengladbach · Werder Bremen:** [0, 2, 1-1] interrompido aos 88 minutos com a trave quebrada; a DFB deu o 2-0 ao Werder
- **1976/77 · 1. FC Kaiserslautern · Fortuna Dusseldorf:** [0, 2, 0-1] interrompido aos 76 minutos (garrafa atirada da torcida); a DFB deu o 2-0 ao Düsseldorf
- **1992/93 · Bayer 05 Uerdingen · Eintracht Frankfurt:** [2, 0, 2-5] o Frankfurt escalou 4 estrangeiros; a DFB deu o 2-0 ao Uerdingen
- **1994/95 · Eintracht Frankfurt · Bayern Munchen:** [2, 0, 2-5] o Bayern escalou 4 amadores; a DFB deu o 2-0 ao Frankfurt
- **2010/11 · FC St. Pauli · FC Schalke 04:** [0, 2, 0-2] interrompido aos 88 minutos (copo atirado no assistente); a DFB manteve o 0-2

### Nomes de artilheiros acertados (`NOMES_ARTILHEIRO`)

- **AÍLTON Gonçalves da Silva:** Aílton
- **Márcio AMOROSO dos Santos:** Márcio Amoroso
- **Giovane Élber de Souza:** Giovane Élber
- **Thomas CHRISTIANSEN Tarín:** Thomas Christiansen
- **Luca TONI Varchetta:** Luca Toni
- **GRAFITE Edinaldo Batista Libânio:** Grafite
- **Mario GÓMEZ García:** Mario Gómez
- **Harry Edward Kane:** Harry Kane

### Punições que nenhuma tabela usada traz (`PUNICOES`)

- **1971/72 · Arminia Bielefeld:** [-19] perdeu todos os pontos (escândalo da Bundesliga de 1971) e foi rebaixado de ofício (Wikipédia de: Abzug 19; RSSSF: stripped of all points)

### Rebaixamentos fora de campo e casos especiais (observação da edição) (`FORA_DE_CAMPO`)

- **1964/65:** Hertha rebaixado por perda da licença; Karlsruhe e Schalke, 15º e 16º, ficaram com a ampliação para 18 clubes
- **1971/72:** Arminia Bielefeld rebaixado de ofício e sem pontos (escândalo de 1971)
- **1979/80:** 3º lugar dividido entre Stuttgart e Kaiserslautern (41 pontos e 75-53 de gols; não havia outro critério)
- **1994/95:** Dynamo Dresden, 18º, também perdeu a licença

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1965/66:** Lothar Emmerich (Dortmund) foi o artilheiro com 31 gols (RSSSF); a lista de campeões da Wikipédia traz 26, que são os gols do 2º colocado
- **1969/70:** a tabela da RSSSF dá ao Bayern uma vitória a mais e ao Rot-Weiß Oberhausen um empate a menos (com 2 gols a menos para o Oberhausen e 2 gols sofridos a menos para o Bayern); a base, o ogol e a tabela da Wikipédia concordam com os jogos: erro da RSSSF
- **1979/80:** a tabela da Wikipédia troca as linhas de Stuttgart e Kaiserslautern (os dois com 41 pontos e 75-53 de gols); a da RSSSF fecha com os jogos e dá a ordem
- **1991/92:** a base para em 25/04/1992 (faltam as 4 últimas rodadas da temporada de 20 clubes, depois da reunificação): os 40 jogos entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- **1993/94:** Dynamo Dresden: 4 pontos a menos (licença); a Wikipédia desconta, a tabela da RSSSF não

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Play-offs de rebaixamento (Relegation) contra clubes da 2. Bundesliga:** ficam de fora (entram com a 2ª divisão).
- **Ligas regionais de 1902/03 a 1962/63** (só a fase final entra) e a **DDR-Oberliga**: ficam para depois.
- **Era antiga, além da fase final:** artilheiros, e gols com autor fora das partidas com ficha na Wikipédia.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Era antiga (1902/03-1962/63, em antigo.py): entra só a fase final; as ligas regionais (Oberligen, Gauligen e as ligas de antes) ficam de fora. Pendência se o painel quiser mostrar as regionais.
- Era antiga: gols com autor só nas partidas com ficha (football box) na Wikipédia, quase sempre a final; artilheiros da fase final não coletados (a infobox da Wikipédia tem o artilheiro de cada temporada).
- Era antiga: 1947/48, três placares diferentes entre RSSSF e Wikipédia (en) nas quartas e na semifinal; ficou a RSSSF. Conferir numa terceira fonte (kicker, Wikipédia em alemão).
- Era antiga: a classificação final é o campeão, o vice e depois a fase alcançada (na mesma fase, posição no grupo e campanha); não existe classificação oficial além do campeão e do vice.

## 10. Arquivos

- Código: `coleta/ger-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_ger.py`.
- Fontes baixadas: `data/coleta/ger-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ger-1/`.
- Pacote: `data/coleta/ger-1/pacote/`; relatório: `docs/coleta/ger-1.md`.
- Refazer do zero: `python coleta/ger-1/baixar.py ...` (ver o docstring), `python coleta/ger-1/importar.py`, `python coleta/comum-europa/testar_carga.py ger-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

