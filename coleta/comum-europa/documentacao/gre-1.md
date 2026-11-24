# Campeonato Grego (`gre-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/gre-1/pacote/` e do importador `coleta/gre-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/gre-1.md`.

## 1. O que temos

- **Edições:** 90, de 1927/28 a 2025/26.
- **Jogos:** 18689; **gols:** 46867; **gols com autor:** 8900 (19%); **cartões:** 20025; **jogos com estatísticas** (chutes, faltas, escanteios): 2145.
- **Clubes:** 69; **artilheiros:** 67 temporadas com artilheiro (71 linhas, com empates).
- **Classificação final:** 90 temporadas; **rodada a rodada:** 30 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2418 linhas, de 149 tabelas.
- **Observação da competição:** Campeonato grego reconhecido pela federação, desde 1927/28: até 1958/59, fase nacional entre os campeões das ligas regionais (Panhellenic Championship; no pacote, só a fase nacional); desde 1959/60, liga nacional (Alpha Ethniki; Super League desde 2006/07), com play-offs desde 2019/20. Os campeões do Chipre jogaram a liga de 1967/68 a 1973/74. Sem 1928/29, 1934/35, 1940/41-1944/45, 1949/50 e 1951/52. Não inclui o campeonato SEGAS (1906-1912) nem os jogos de acesso contra clubes da 2ª divisão.

## 2. Fontes e regras

**Fontes:**

- RSSSF: fase nacional de 1927/28 a 1958/59 (grkprehist.html); matriz de resultados de 1959/60 a 1992/93 (base dos jogos, sem data; grkhist.html e a página de cada temporada desde 1968/69); tabelas finais; lista de campeões e de artilheiros;
- Wikipédia (en): matriz de resultados (conferência), tabelas da fase regular e dos play-offs, fichas dos jogos-desempate (data, local, autores dos gols);
- ogol (zerozero): base dos jogos de 1993/94 em diante, com data e rodada; o clube pelo código do ogol; calendários em `data/cache/ogol-gre-1/` para os escudos;
- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do football-data;
- ESPN (liga `gre.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). Pontos: 3 por vitória, 2 por empate e 1 por derrota até 1972/73; 2-1-0 de 1973/74 a 1991/92; 3-1-0 desde 1992/93 (`pontos_vitoria` traz o da vitória; o sistema 3-2-1 vai na observação da edição). Jogos-desempate (título, 3º lugar) entram na fase "Desempate", fora da tabela. Play-off europeu de 2007/08 a 2016/17: fora da classificação. Desde 2019/20, a classificação final é a ordem dos grupos do play-off, com os números de todos os jogos e o ajuste (metade dos pontos no play-off europeu, punições) em `ajuste_pontos`. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (os cipriotas voltaram à liga deles).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 49, saldo em 9, vitórias em 1, média de gols em 8).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 163 tabelas fecham com os jogos e 32 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1989/90, 1932/33, 1933/34, 1938/39, 1939/40, 1946/47, 1954/55, 1955/56.
- Temporadas com alguma tabela divergente: 1966/67, 1973/74, 1976/77, 1977/78, 1978/79, 1980/81, 1981/82, 1982/83, 1983/84, 1985/86, 1989/90, 1994/95, 1998/99, 1999/00, 2000/01, 2007/08, 2015/16, 2017/18, 2019/20, 1932/33, 1935/36, 1946/47, 1952/53, 1953/54, 1954/55, 1955/56, 1957/58.
- Temporadas com número de jogos diferente do turno e returno completo: 1959/60 (244 de 240), 1960/61 (242 de 240), 1961/62 (245 de 240), 1962/63 (248 de 240), 1963/64 (241 de 240), 1964/65 (243 de 240), 1965/66 (243 de 240), 1966/67 (241 de 240), 1973/74 (309 de 306), 1979/80 (308 de 306), 1981/82 (307 de 306), 1982/83 (307 de 306), 1983/84 (241 de 240), 1985/86 (241 de 240), 1988/89 (241 de 240), 2007/08 (252 de 240), 2008/09 (252 de 240), 2009/10 (252 de 240), 2010/11 (252 de 240), 2011/12 (252 de 240), 2012/13 (253 de 240), 2013/14 (318 de 306), 2014/15 (318 de 306), 2015/16 (252 de 240), 2016/17 (252 de 240), 2019/20 (240 de 182), 2020/21 (240 de 182), 2021/22 (240 de 182), 2022/23 (240 de 182), 2023/24 (240 de 182), 2024/25 (236 de 182), 2025/26 (236 de 182).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 12 | 50% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 191 | 3% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 48 | 12% | 0% | 0% | 12% | 0% | 8% | 0% | 8% | 0.0 |
| 1950s | 662 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2621 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2999 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2669 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3060 | 70% | 0% | 40% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 2378 | 100% | 40% | 99% | 40% | 0% | 0% | 0% | 35% | 1.9 |
| 2010s | 2617 | 100% | 95% | 95% | 95% | 19% | 0% | 27% | 54% | 3.1 |
| 2020s | 1432 | 100% | 100% | 80% | 100% | 75% | 0% | 100% | 99% | 5.2 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1959/60 a 1966/67: 16 clubes
- 1967/68 a 1974/75: 18 clubes
- 1975/76: 16 clubes
- 1976/77 a 1982/83: 18 clubes
- 1983/84 a 1988/89: 16 clubes
- 1989/90 a 1999/00: 18 clubes
- 2000/01: 16 clubes
- 2001/02: 14 clubes
- 2002/03 a 2012/13: 16 clubes
- 2013/14 a 2014/15: 18 clubes
- 2015/16 a 2018/19: 16 clubes
- 2019/20 a 2025/26: 14 clubes
- 1927/28 a 1929/30: 3 clubes
- 1930/31 a 1931/32: 8 clubes
- 1932/33: 3 clubes
- 1933/34: 2 clubes
- 1935/36: 8 clubes
- 1936/37 a 1937/38: 3 clubes
- 1938/39 a 1939/40: 2 clubes
- 1945/46: 3 clubes
- 1946/47: 6 clubes
- 1947/48 a 1952/53: 3 clubes
- 1953/54 a 1955/56: 6 clubes
- 1956/57: 10 clubes
- 1957/58: 12 clubes
- 1958/59: 10 clubes

**Pontos por vitória:**

- 1959/60 a 1972/73: 3
- 1973/74 a 1991/92: 2
- 1992/93 a 2025/26: 3
- 1927/28 a 1939/40: 2
- 1945/46 a 1958/59: 3

**Nome oficial:**

- 1959/60 a 2005/06: Alpha Ethniki
- 2006/07 a 2025/26: Super League Greece
- 1927/28 a 1958/59: Panhellenic Championship

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1959/60: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1960/61: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1961/62: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1962/63: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1963/64: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1964/65: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1965/66: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1966/67: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1973/74: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1979/80: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1981/82: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1982/83: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1983/84: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1985/86: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1988/89: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 2007/08: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2008/09: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2009/10: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2010/11: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2011/12: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2012/13: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 2013/14: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2014/15: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2015/16: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2016/17: Fase regular (liga, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 2019/20: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2020/21: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2021/22: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2022/23: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2023/24: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2024/25: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 2025/26: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos); Play-out de rebaixamento (grupos, pontos_corridos)
- 1933/34: Final (mata_mata, ida_volta)
- 1938/39: Final (mata_mata, ida_volta)
- 1939/40: Final (mata_mata, ida_volta)
- 1955/56: Fase final (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1956/57: Fase final (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto, saldo de gols, gols pró: 49 temporadas
- pontos: 20 temporadas
- jogo-desempate, fora da tabela: 18 temporadas
- pontos acumulados com a fase regular: 14 temporadas
- pontos, com bônus pela posição na fase regular: 10 temporadas
- pontos, saldo de gols, gols pró: 9 temporadas
- pontos, média de gols (goal average): 8 temporadas
- soma dos placares: 3 temporadas
- pontos acumulados com a fase regular (metade): 2 temporadas
- pontos, vitórias, saldo de gols, gols pró: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1959/60: 3 pontos por vitória, 2 por empate e 1 por derrota; decidido em jogo-desempate
- 1960/61: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: AEK Atenas -1 pontos; Atromitos Piraeus -1 pontos
- 1961/62: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Panionios -1 pontos; Apollon Kalamarias -1 pontos
- 1962/63: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Egaleo -1 pontos; decidido em jogo-desempate
- 1963/64: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: PAOK -1 pontos; Egaleo -1 pontos
- 1964/65: 3 pontos por vitória, 2 por empate e 1 por derrota
- 1965/66: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: AEK Atenas -2 pontos; Panionios -1 pontos
- 1966/67: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Pierikos -1 pontos
- 1967/68: 3 pontos por vitória, 2 por empate e 1 por derrota
- 1968/69: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: AEK Atenas -1 pontos
- 1969/70: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Panachaiki -13 pontos
- 1970/71: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: EPA Larnaca -1 pontos
- 1971/72: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Olympiakos Nicosia -1 pontos
- 1972/73: 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Panathinaikos -3 pontos; Omonia Nicosia -1 pontos
- 1975/76: punições: Atromitos -3 pontos
- 1976/77: punições: Atromitos -3 pontos
- 1977/78: punições: Veria -10 pontos
- 1979/80: punições: Kastoria -1 pontos; decidido em jogo-desempate
- 1981/82: decidido em jogo-desempate
- 1985/86: punições: Panachaiki -1 pontos
- 1986/87: punições: PAOK -6 pontos; Iraklis -6 pontos; AEK Atenas -9 pontos; Larissa -6 pontos; Veria -6 pontos; Ethnikos Piraeus -6 pontos; Aris Salônica -6 pontos; Apollon Kalamarias -6 pontos; Diagoras -6 pontos; Doxa Drama -6 pontos; Apollon Smyrnis -6 pontos; PAS Giannina -6 pontos
- 1987/88: punições: Panachaiki -1 pontos
- 1989/90: punições: Levadiakos -4 pontos
- 1990/91: punições: Olympiacos -2 pontos; PAOK -3 pontos
- 1995/96: punições: PAOK -3 pontos
- 1996/97: punições: Aris Salônica -3 pontos
- 2002/03: punições: PAS Giannina -90 pontos
- 2004/05: punições: Aris Salônica -3 pontos
- 2006/07: punições: Ionikos -5 pontos
- 2007/08: punições: Apollon Kalamarias -1 pontos
- 2011/12: punições: Panathinaikos -3 pontos; Aris Salônica -3 pontos
- 2012/13: punições: Panathinaikos -2 pontos; AEK Atenas -3 pontos
- 2014/15: punições: Panathinaikos -3 pontos; OFI Creta -29 pontos; Niki Volos -13 pontos
- 2015/16: punições: Panathinaikos -3 pontos; AEK Atenas -3 pontos; PAOK -3 pontos; Atromitos -3 pontos
- 2016/17: punições: PAOK -3 pontos
- 2017/18: punições: PAOK -3 pontos; Olympiacos -3 pontos; Panathinaikos -8 pontos
- 2018/19: punições: PAOK -2 pontos; AEK Atenas -3 pontos; Panathinaikos -11 pontos
- 2019/20: punições: Xanthi -12 pontos; Panionios -6 pontos
- 1927/28: só a fase nacional; as ligas regionais ficam de fora
- 1929/30: só a fase nacional; as ligas regionais ficam de fora
- 1930/31: só a fase nacional; as ligas regionais ficam de fora
- 1931/32: só a fase nacional; as ligas regionais ficam de fora
- 1932/33: só a fase nacional; as ligas regionais ficam de fora
- 1933/34: só a fase nacional; as ligas regionais ficam de fora
- 1935/36: só a fase nacional; as ligas regionais ficam de fora
- 1936/37: só a fase nacional; as ligas regionais ficam de fora
- 1937/38: só a fase nacional; as ligas regionais ficam de fora
- 1938/39: só a fase nacional; as ligas regionais ficam de fora
- 1939/40: só a fase nacional; as ligas regionais ficam de fora
- 1945/46: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1946/47: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Iraklis -1 pontos; Makedonikos -2 pontos
- 1947/48: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1948/49: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Panathinaikos -1 pontos; Aris Salônica -1 pontos
- 1950/51: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Iraklis -1 pontos
- 1952/53: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1953/54: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1954/55: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1955/56: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota
- 1956/57: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Ethnikos Piraeus -4 pontos; Panargiakos -2 pontos
- 1957/58: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Ethnikos Piraeus -2 pontos
- 1958/59: só a fase nacional; as ligas regionais ficam de fora; 3 pontos por vitória, 2 por empate e 1 por derrota; punições: Apollon Kalamarias -1 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Olympiacos: 48
- Panathinaikos: 20
- AEK Atenas: 14
- PAOK: 4
- Aris Salônica: 3
- Larissa: 1

**Rebaixamentos:** 173 no total; quem mais caiu: Panserraikos (9), Apollon Smyrnis (8), Panachaiki (8), PAS Giannina (8), Veria (7).

**Punições em pontos:**

- 1960/61: AEK Atenas -1
- 1960/61: Atromitos Piraeus -1
- 1961/62: Panionios -1
- 1961/62: Apollon Kalamarias -1
- 1962/63: Egaleo -1
- 1963/64: PAOK -1
- 1963/64: Egaleo -1
- 1965/66: AEK Atenas -2
- 1965/66: Panionios -1
- 1966/67: Pierikos -1
- 1968/69: AEK Atenas -1
- 1969/70: Panachaiki -13
- 1970/71: EPA Larnaca -1
- 1971/72: Olympiakos Nicosia -1
- 1972/73: Panathinaikos -3
- 1972/73: Omonia Nicosia -1
- 1975/76: Atromitos -3
- 1976/77: Atromitos -3
- 1977/78: Veria -10
- 1979/80: Kastoria -1
- 1985/86: Panachaiki -1
- 1986/87: PAOK -6
- 1986/87: Iraklis -6
- 1986/87: AEK Atenas -9
- 1986/87: Larissa -6
- 1986/87: Veria -6
- 1986/87: Ethnikos Piraeus -6
- 1986/87: Aris Salônica -6
- 1986/87: Apollon Kalamarias -6
- 1986/87: Diagoras -6
- 1986/87: Doxa Drama -6
- 1986/87: Apollon Smyrnis -6
- 1986/87: PAS Giannina -6
- 1987/88: Panachaiki -1
- 1989/90: Levadiakos -4
- 1990/91: Olympiacos -2
- 1990/91: PAOK -3
- 1995/96: PAOK -3
- 1996/97: Aris Salônica -3
- 2002/03: PAS Giannina -90
- 2004/05: Aris Salônica -3
- 2006/07: Ionikos -5
- 2007/08: Apollon Kalamarias -1
- 2011/12: Panathinaikos -3
- 2011/12: Aris Salônica -3
- 2012/13: Panathinaikos -2
- 2012/13: AEK Atenas -3
- 2014/15: Panathinaikos -3
- 2014/15: OFI Creta -29
- 2014/15: Niki Volos -13
- 2015/16: Panathinaikos -3
- 2015/16: AEK Atenas -3
- 2015/16: PAOK -3
- 2015/16: Atromitos -3
- 2016/17: PAOK -3
- 2017/18: PAOK -3
- 2017/18: Olympiacos -3
- 2017/18: Panathinaikos -8
- 2018/19: PAOK -2
- 2018/19: AEK Atenas -3
- 2018/19: Panathinaikos -11
- 2019/20: Xanthi -24
- 2019/20: Panionios -12
- 2024/25: Aris Salônica -21
- 2024/25: Asteras Tripolis -17
- 2024/25: Atromitos -17
- 2024/25: OFI Creta -18
- 2025/26: Aris Salônica -15
- 2025/26: Levadiakos -21
- 2025/26: OFI Creta -16
- 2025/26: Volos NFC -15
- 1946/47: Iraklis -1
- 1946/47: Makedonikos -2
- 1948/49: Panathinaikos -1
- 1948/49: Aris Salônica -1
- 1950/51: Iraklis -1
- 1956/57: Ethnikos Piraeus -4
- 1956/57: Panargiakos -2
- 1957/58: Ethnikos Piraeus -2
- 1958/59: Apollon Kalamarias -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/gre-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1997/98 · Ionikos · Olympiacos:** [0, 1] o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as tabelas da RSSSF e da Wikipédia dão 0-1
- **1998/99 · Aris Salônica · Ionikos:** [1, 1] o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as tabelas da RSSSF e da Wikipédia dão 1-1
- **2014/15 · Asteras Tripolis · Ergotelis:** [2, 1] o ogol dá 3-0; o football-data, o engsoccerdata, a ESPN e as tabelas da RSSSF e da Wikipédia dão 2-1
- **2023/24 · Kifisia · Volos NFC:** [3, 0, awd] 0-0 em campo; em 04/03/2024 a vitória foi dada ao Kifisia por 3-0, depois da agressão racista do presidente do Volos a Andrews Tetteh (nota da matriz da Wikipédia); as tabelas da RSSSF e da Wikipédia contam o 3-0

### Mando de campo corrigido (`INVERTIDOS`)

- **2001/02 · 2001-10-14 · Ethnikos Asteras · Panachaiki:** [Panachaiki, Ethnikos Asteras, 0, 0] o ogol traz Ethnikos Asteras 1-1 Panachaiki nesta data e de novo em 17/02/2002; o engsoccerdata, a matriz da Wikipédia e as tabelas da RSSSF e da Wikipédia dão Panachaiki 0-0 Ethnikos Asteras na 3ª rodada

### Células da matriz da RSSSF com nota (placar dado na nota) (`NOTAS_MATRIZ`)

- **1969/70 · 1:** [2, 0, awd] 0-0 em campo; vitória dada ao Aris porque o Panachaiki tentou combinar o resultado (RSSSF)
- **1970/71 · 1:** [0, 2, awd] vitória dada ao Fostiras fora de campo (RSSSF)
- **1971/72 · 1:** [0, 2, awd] interrompido aos 85 minutos (0-1); dado 0-2, e o Olympiakos Nicosia perdeu também o ponto da derrota (RSSSF: "0-2 on goals and 0-3 on points")
- **1976/77 · 1:** [2, 0, awd] o Atromitos não compareceu em Serres (RSSSF)
- **1979/80 · 1:** [2, 0, awd] 0-0 em campo; vitória dada ao Apollon (RSSSF)
- **1982/83 · *:** [0, 2, awd] interrompido: o Rodos ficou com 6 jogadores (1-2 no intervalo); vitória dada ao AEK (RSSSF)
- **1984/85 · 1:** [0, 1] jogado em Trikala (RSSSF)
- **1984/85 · 2:** [2, 2] jogado em Katerini (RSSSF)
- **1984/85 · 3:** [2, 3] jogado em Tavros (RSSSF)
- **1985/86 · 1:** [0, 2, awd] 1-0 em campo; o Panachaiki escalou um jogador suspenso: vitória dada ao Iraklis e 1 ponto a menos para o Panachaiki (RSSSF)
- **1986/87 · 1:** [2, 0, awd] greve das 3 últimas rodadas: o visitante não compareceu (RSSSF)
- **1986/87 · 2:** [0, 2, awd] greve das 3 últimas rodadas: o mandante não compareceu (RSSSF)
- **1986/87 · *:** [0, 0, awd] greve das 3 últimas rodadas: nenhum dos dois compareceu; derrota para os dois (RSSSF)
- **1987/88 · 1:** [0, 2, awd] 4-2 em campo; o Panachaiki escalou um jogador suspenso: vitória dada ao Panserraikos (RSSSF)
- **1990/91 · 1:** [3, 0] interrompido aos 77 minutos porque o PAOK deixou o campo; ficou o 3-0 (RSSSF)
- **1990/91 · 2:** [0, 2, awd] 2-2 em campo; invasão de campo: vitória dada ao Athinaikos (RSSSF)
- **1990/91 · 3:** [1, 0] 1-2 no primeiro jogo, interrompido pela fumaça; repetido em Rodes (RSSSF)

### Jogos que valeram derrota para os dois (`DERROTA_DOIS_OGOL`)

- **2014/15 · Niki Volos · OFI Creta:** não disputado: os dois clubes tinham sido excluídos da liga (a matriz da Wikipédia marca "–"); as tabelas da RSSSF e da Wikipédia contam 34 jogos para os dois, o que só fecha com derrota para os dois

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **2004/05:** o clube da liga era o Chalkidona (Wikipédia, engsoccerdata); ele se fundiu com o Atromitos em 2005 e o ogol põe a temporada no código do Atromitos

## 8. O que não deu para coletar

- **Datas e rodadas de 1959/60 a 1992/93:** a matriz da RSSSF e a da Wikipédia não trazem; o ogol não tem esses jogos. Rodadas de 1994/95 a 1996/97: o ogol não traz.
- **Era antiga (até 1958/59):** só a fase nacional; as ligas regionais ficam de fora.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (só as fichas dos jogos-desempate).
- **Jogos de acesso contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- 1959/60 a 1992/93: jogos sem data nem rodada (só a matriz da RSSSF e a da Wikipédia; o ogol não tem esses jogos). Rodadas de 1994/95 a 1996/97: o ogol não traz.
- Era antiga (1927/28-1958/59, em antigo.py): só a fase nacional entre os campeões regionais; as ligas regionais, a fase semifinal de 1955/56 e as eliminatórias inter-regionais ficam de fora. Datas só nas finais e em 1929/30 e 1945/46.
- Era antiga: em 1954/55 e 1955/56 as tabelas da RSSSF e da Wikipédia concordam entre si e não fecham com nenhuma matriz (diferenças de 1 a 4 gols); só o jornal da época decidiria.
- Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15; antes, só as fichas dos jogos-desempate da Wikipédia.
- Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora (1959/60, 1967/68, 1968/69, 2000/01 a 2003/04, 2013/14, 2018/19 a 2021/22).
- Play-off europeu de 2015/16: a tabela da Wikipédia dá 1 gol a menos a AEK (pró) e Panionios (contra) que os jogos do ogol; sem terceira fonte (a ESPN e o football-data não têm os play-offs), fica o ogol.

**Com o agente de revisão:** decisões da coleta que ele confere.

- 1959/60 a 1992/93: onde a matriz da RSSSF e a da Wikipédia discordam, ficou o placar que fecha com as duas tabelas publicadas (a maioria é da Wikipédia; trocas jogo a jogo e em pares, anotadas no relatório e na observação do jogo).
- Era antiga: o mesmo critério na fase nacional (1930/31, 1931/32, 1953/54, 1956/57, 1957/58, 1958/59 com trocas).
- Identidade: Chalkidona em 2004/05 (o ogol põe no Atromitos, que absorveu o clube em 2005); Rodos x AE Rodos e AO Kerkyra x PAE Kerkyra separados como na Wikipédia; Megas Alexandros (1959/60) como Pierikos.
- Desempates de posição que só estão nas notas da Wikipédia (1959/60 a 1966/67, 1973/74, 1982/83, 1983/84), sem data.

## 10. Arquivos

- Código: `coleta/gre-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_gre.py`.
- Fontes baixadas: `data/coleta/gre-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-gre-1/`.
- Pacote: `data/coleta/gre-1/pacote/`; relatório: `docs/coleta/gre-1.md`.
- Refazer do zero: `python coleta/gre-1/baixar.py ...` (ver o docstring), `python coleta/gre-1/importar.py`, `python coleta/comum-europa/testar_carga.py gre-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

