# Campeonato Italiano (`ita-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ita-1/pacote/` e do importador `coleta/ita-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ita-1.md`.

## 1. O que temos

- **Edições:** 124, de 1898 a 2025/26.
- **Jogos:** 34732; **gols:** 94266; **gols com autor:** 24598 (26%); **cartões:** 43962; **jogos com estatísticas** (chutes, faltas, escanteios): 7965.
- **Clubes:** 191; **artilheiros:** 95 temporadas com artilheiro (106 linhas, com empates).
- **Classificação final:** 124 temporadas; **rodada a rodada:** 94 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2958 linhas, de 139 tabelas.
- **Observação da competição:** Serie A desde a criação do grupo único (1929/30). Sem 1943/44 e 1944/45 (Segunda Guerra). 1945/46 foi a Divisione Nazionale: grupos Norte e Centro-Sul e grupo final. Os desempates (spareggi) de título e de rebaixamento entram na fase "Desempate", fora da tabela (os de vaga europeia não). Não inclui os campeonatos de antes de 1929/30 (grupos regionais e finais).

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1929/30-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ita-1/` para os escudos;
- ESPN (liga `ita.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (Maurizio Mariani e outros): tabela final, nas temporadas em que a página traz uma tabela legível;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e Capocannoniere.

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Roma). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94, 3 a partir de 1994/95. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 57, saldo de gols em 27, média de gols em 11); é ele que ordena a classificação rodada a rodada. Até 2004/05, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio), que não está no pacote.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 268 tabelas fecham com os jogos e 42 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1898, 1899, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1909/10.
- Temporadas com alguma tabela divergente: 1929/30, 1930/31, 1948/49, 1959/60, 1993/94, 1909, 1909/10, 1911/12, 1912/13, 1914/15, 1919/20, 1920/21, 1921/22 (FIGC), 1921/22 (CCI), 1922/23, 1923/24, 1924/25, 1925/26.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1890s | 6 | 100% | 0% | 0% | 100% | 0% | 100% | 0% | 12% | 0.0 |
| 1900s | 164 | 43% | 0% | 4% | 35% | 0% | 33% | 0% | 3% | 0.0 |
| 1910s | 1514 | 78% | 0% | 46% | 1% | 0% | 2% | 0% | 0% | 0.0 |
| 1920s | 4080 | 93% | 0% | 74% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 2665 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 2632 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 3216 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2867 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2532 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3063 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3512 | 100% | 91% | 100% | 89% | 72% | 22% | 54% | 90% | 4.2 |
| 2010s | 3800 | 100% | 100% | 100% | 100% | 92% | 0% | 100% | 100% | 5.0 |
| 2020s | 2281 | 100% | 100% | 100% | 100% | 83% | 0% | 100% | 100% | 4.5 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1929/30 a 1933/34: 18 clubes
- 1934/35 a 1942/43: 16 clubes
- 1945/46: 25 clubes
- 1946/47: 20 clubes
- 1947/48: 21 clubes
- 1948/49 a 1951/52: 20 clubes
- 1952/53 a 1966/67: 18 clubes
- 1967/68 a 1987/88: 16 clubes
- 1988/89 a 2003/04: 18 clubes
- 2004/05 a 2025/26: 20 clubes
- 1898 a 1899: 4 clubes
- 1900: 6 clubes
- 1901: 4 clubes
- 1902: 8 clubes
- 1903: 6 clubes
- 1904: 5 clubes
- 1905: 6 clubes
- 1906: 5 clubes
- 1907: 6 clubes
- 1908: 4 clubes
- 1909 a 1909/10: 9 clubes
- 1910/11: 13 clubes
- 1911/12: 15 clubes
- 1912/13: 35 clubes
- 1913/14: 45 clubes
- 1914/15: 50 clubes
- 1919/20: 75 clubes
- 1920/21: 88 clubes
- 1921/22 (FIGC): 46 clubes
- 1921/22 (CCI): 58 clubes
- 1922/23: 56 clubes
- 1923/24: 47 clubes
- 1924/25: 43 clubes
- 1925/26: 44 clubes
- 1926/27: 20 clubes
- 1927/28: 22 clubes
- 1928/29: 32 clubes

**Pontos por vitória:**

- 1929/30 a 1993/94: 2
- 1994/95 a 2025/26: 3
- 1898 a 1928/29: 2

**Nome oficial:**

- 1929/30 a 1942/43: Serie A
- 1945/46: Divisione Nazionale
- 1946/47 a 2025/26: Serie A
- 1898 a 1903: Campionato Italiano di Football
- 1904 a 1907: Prima Categoria
- 1908: Campionato Italiano di Prima Categoria
- 1909: Campionato Federale di Prima Categoria
- 1909/10 a 1921/22 (FIGC): Prima Categoria
- 1921/22 (CCI) a 1925/26: Prima Divisione
- 1926/27 a 1928/29: Divisione Nazionale

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1931/32: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1942/43: Liga (liga, pontos_corridos); Desempate (mata_mata, pontos_corridos)
- 1945/46: Grupos (grupos, pontos_corridos); Fase final (grupos, pontos_corridos)
- 1951/52: Liga (liga, pontos_corridos); Desempate (mata_mata, pontos_corridos)
- 1953/54: Liga (liga, pontos_corridos); Desempate (mata_mata, pontos_corridos)
- 1957/58: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 1960/61: Liga (liga, pontos_corridos); Desempate (mata_mata, pontos_corridos)
- 1963/64: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 1992/93: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1994/95: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1996/97: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 2000/01: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 2002/03: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 2003/04: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 2004/05: Liga (liga, pontos_corridos); Desempate (mata_mata, ida_volta)
- 2022/23: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1898: Semifinais (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1899: Eliminatoria piemontesa (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1900: Eliminatoria lígure (mata_mata, jogo_unico); Eliminatórias piemontesa (grupos, pontos_corridos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1901: Eliminatoria piemontesa (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1902: Eliminatoria lígure (mata_mata, jogo_unico); Eliminatórias piemontesa · Desempate (mata_mata, jogo_unico); Eliminatoria inter-regional lígure-lombarda (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1903: Eliminatoria piemontesa (grupos, pontos_corridos); Eliminatoria inter-regional lígure-piemontesa (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1904: Eliminatoria piemontesa (mata_mata, jogo_unico); Eliminatoria inter-regional lígure-lombarda (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Desempate della semifinale (Ripetizione) (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1905: Eliminatoria lígure (mata_mata, ida_volta); Eliminatoria lombarda (mata_mata, ida_volta); Eliminatoria piemontesa (mata_mata, ida_volta); Fase única (grupos, pontos_corridos)
- 1906: Eliminatoria lígure (mata_mata, ida_volta); Eliminatoria lombarda (mata_mata, ida_volta); Fase única (grupos, pontos_corridos); Desempate primo posto (mata_mata, ida_volta)
- 1907: Eliminatoria lígure (mata_mata, ida_volta); Eliminatoria lombarda (mata_mata, ida_volta); Eliminatoria piemontesa (mata_mata, ida_volta); Fase única (grupos, pontos_corridos)
- 1908: Eliminatoria piemontesa (mata_mata, ida_volta); Fase única (grupos, pontos_corridos)
- 1909: Eliminatórias liguri (mata_mata, jogo_unico); Eliminatórias lombarda (grupos, pontos_corridos); Eliminatórias piemontesa · Primo turno cittadino (mata_mata, jogo_unico); Eliminatórias piemontesa · Secondo turno regional (mata_mata, ida_volta); Semifinal lígure-piemontesa (mata_mata, ida_volta); Semifinal lombardo-vêneta (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1909/10: Fase única (grupos, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1910/11: Campeonato do Noroeste (grupos, pontos_corridos); Campeonato emiliano-vêneto (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1911/12: Eliminatórias pre-campionato (mata_mata, ida_volta); Campeonato do Noroeste (grupos, pontos_corridos); Campeonato emiliano-vêneto (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1912/13: Eliminatórias pre-campionato · Piemonte (mata_mata, jogo_unico); Eliminatórias pre-campionato · Lombardia-Liguria · Primo turno (grupos, pontos_corridos); Eliminatórias pre-campionato · Lombardia-Liguria · Secondo turno (mata_mata, jogo_unico); Eliminatórias pre-campionato · Lazio · Primo turno (grupos, pontos_corridos); Eliminatórias pre-campionato · Lazio · Secondo turno (mata_mata, jogo_unico); Torneio do Norte (grupos, pontos_corridos); Torneio do Norte · Grupo final (grupos, pontos_corridos); Torneio do Centro-Sul (grupos, pontos_corridos); Torneio do Centro-Sul · Fase final · Semifinal Itália centrale (mata_mata, ida_volta); Torneio do Centro-Sul · Fase final · Semifinal Itália do Sul (mata_mata, ida_volta); Torneio do Centro-Sul · Fase final · Final do Centro-Sul (mata_mata, ida_volta); Final nacional (mata_mata, jogo_unico)
- 1913/14: Torneio principal (grupos, pontos_corridos); Torneio do Centro-Sul (grupos, pontos_corridos); Torneio do Centro-Sul · Fase final · Semifinal Itália centrale (mata_mata, ida_volta); Torneio do Centro-Sul · Fase final · Semifinal Itália do Sul (mata_mata, ida_volta); Torneio do Centro-Sul · Fase final · Final do Centro-Sul (mata_mata, ida_volta); Final nacional (mata_mata, ida_volta)
- 1914/15: Torneio principal · Grupos de qualificação (grupos, pontos_corridos); Torneio principal · Semifinais nacionais (grupos, pontos_corridos); Torneio principal · Grupo final Nord (grupos, pontos_corridos); Torneio do Centro-Sul (grupos, pontos_corridos); Torneio do Centro-Sul · Semifinais da Itália Central (grupos, pontos_corridos)
- 1919/20: Eliminatórias pre-campionato · Emilia · Primo turno (mata_mata, jogo_unico); Eliminatórias pre-campionato · Emilia · Secondo turno (mata_mata, jogo_unico); Eliminatórias pre-campionato · Liguria · Primo turno (grupos, pontos_corridos); Eliminatórias pre-campionato · Liguria · Secondo turno (mata_mata, jogo_unico); Eliminatórias pre-campionato · Lombardia (grupos, pontos_corridos); Eliminatórias pre-campionato · Piemonte (mata_mata, jogo_unico); Eliminatórias pre-campionato · Campania · Primo turno (grupos, pontos_corridos); Eliminatórias pre-campionato · Campania · Final (mata_mata, jogo_unico); Torneio principal · Grupos regionais de qualificação (grupos, pontos_corridos); Torneio principal · Grupos regionais de qualificação · Seção lombarda (grupos, pontos_corridos); Torneio principal · Grupos regionais de qualificação · Seção piemontesa (grupos, pontos_corridos); Torneio principal · Semifinais nacionais (grupos, pontos_corridos); Torneio do Centro-Sul · Grupos regionais de qualificação (grupos, pontos_corridos); Torneio do Centro-Sul · Semifinais inter-regionais (grupos, pontos_corridos); Torneio do Centro-Sul · Final do Centro-Sul (mata_mata, jogo_unico); Final nacional (mata_mata, jogo_unico)
- 1920/21: Torneio do Norte · Campeonatos regionais de qualificação · Seção emiliana (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação · Seção lombarda · Grupo final regional (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação · Seção piemontesa (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação · Seção vêneta (grupos, pontos_corridos); Torneio do Norte · Campeonatos regionais de qualificação · Seção vêneta · Grupo final (grupos, pontos_corridos); Torneio do Norte · Semifinais nacionais (grupos, pontos_corridos); Torneio do Norte · Semifinais nord (mata_mata, jogo_unico); Torneio do Norte · Final nord (mata_mata, jogo_unico); Torneio peninsular · Grupos regionais de qualificação · Seção da Campânia (grupos, pontos_corridos); Torneio peninsular · Grupos regionais de qualificação · Seção da Campânia · Grupo final regional (grupos, pontos_corridos); Torneio peninsular · Grupos regionais de qualificação (grupos, pontos_corridos); Torneio peninsular · Semifinais inter-regionais (grupos, pontos_corridos); Torneio peninsular · Final do Centro-Sul (mata_mata, jogo_unico); Final nacional (mata_mata, jogo_unico)
- 1921/22 (FIGC): Grupos regionais de qualificação · Seção emiliana (grupos, pontos_corridos); Grupos regionais de qualificação · Seção emiliana · Grupo final (grupos, pontos_corridos); Grupos regionais de qualificação (grupos, pontos_corridos); Grupos regionais de qualificação · Seção lombarda (grupos, pontos_corridos); Grupos regionais de qualificação · Seção lombarda · Grupo final (grupos, pontos_corridos); Semifinais nacionais (grupos, pontos_corridos); Final nacional (mata_mata, ida_volta); Final nacional · Desempate (mata_mata, jogo_unico)
- 1921/22 (CCI): Liga Norte (grupos, pontos_corridos); Liga Sul (grupos, pontos_corridos); Liga Sul · Seção das Marcas (grupos, pontos_corridos); Liga Sul · Seção das Marcas · Grupo final (grupos, pontos_corridos)
- 1922/23: Liga Norte (grupos, pontos_corridos); Liga Norte · Finais da Liga (grupos, pontos_corridos); Liga Sul · Grupos regionais de qualificação (grupos, pontos_corridos); Liga Sul · Semifinais inter-regionais (grupos, pontos_corridos); Liga Sul · Final Liga Sul (mata_mata, ida_volta); Final nacional (mata_mata, ida_volta)
- 1923/24: Liga Norte (grupos, pontos_corridos); Liga Norte · Eliminatórias interdivisionali (grupos, pontos_corridos); Liga Sul · Grupos regionais de qualificação (grupos, pontos_corridos); Liga Sul · Semifinais inter-regionais (grupos, pontos_corridos)
- 1924/25: Liga Norte (grupos, pontos_corridos); Liga Sul · Grupos regionais de qualificação (grupos, pontos_corridos); Liga Sul · Semifinais inter-regionais (grupos, pontos_corridos)
- 1925/26: Liga Norte (grupos, pontos_corridos); Liga Sul · Grupos regionais de qualificação (grupos, pontos_corridos); Liga Sul · Semifinais inter-regionais (grupos, pontos_corridos)
- 1926/27: Primeira fase (grupos, pontos_corridos); Grupo final (grupos, pontos_corridos)
- 1927/28: Primeira fase (grupos, pontos_corridos); Grupo final (grupos, pontos_corridos)
- 1928/29: Primeira fase (grupos, pontos_corridos); Finais nacionais (mata_mata, ida_volta); Finais nacionais · Desempate (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos: 77 temporadas
- resultado: 71 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 56 temporadas
- pontos, saldo de gols, gols pró: 27 temporadas
- jogos-desempate entre clubes empatados em pontos; fora da tabela da liga: 15 temporadas
- pontos, média de gols (goal average): 11 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1959/60: punições: Genoa -18 pontos
- 1973/74: punições: Sampdoria -3 pontos; Foggia -6 pontos
- 1976/77: punições: Napoli -1 pontos
- 1980/81: punições: Bologna -5 pontos; Avellino -5 pontos; Perugia -5 pontos
- 1986/87: punições: Udinese -9 pontos
- 1987/88: punições: Empoli -5 pontos
- 1998/99: punições: Empoli -2 pontos
- 2004/05: título não atribuído
- 2005/06: punições: Milan -30 pontos; Fiorentina -30 pontos; Lazio -30 pontos
- 2006/07: punições: Lazio -3 pontos; Milan -8 pontos; Fiorentina -15 pontos; Reggina -11 pontos; Siena -1 pontos
- 2010/11: punições: Bologna -3 pontos
- 2011/12: punições: Atalanta -6 pontos
- 2012/13: punições: Sampdoria -1 pontos; Atalanta -2 pontos; Torino -1 pontos; Siena -6 pontos
- 2014/15: punições: Parma -7 pontos
- 2018/19: punições: Chievo -3 pontos
- 2022/23: punições: Juventus -10 pontos
- 1908: o Campionato Italiano (só com jogadores italianos), o que vale o título; o Campionato Federale do mesmo ano, aberto a estrangeiros, não é contado
- 1909: o Campionato Federale, que passou a valer o título; o Campionato Italiano do mesmo ano não é contado
- 1914/15: interrompido em 23/05/1915 pela entrada da Itália na Primeira Guerra Mundial, antes do fim do grupo final do Norte e da final nacional; a federação deu o título ao Genoa (líder do grupo final do Norte) depois da guerra
- 1921/22 (FIGC): temporada com dois campeonatos, depois da cisão dos grandes clubes: o da FIGC (Prima Categoria, Novese) e o da CCI (Prima Divisione, Pro Vercelli); os dois títulos são oficiais
- 1921/22 (CCI): temporada com dois campeonatos, depois da cisão dos grandes clubes: o da CCI (Prima Divisione, Pro Vercelli) e o da FIGC (Prima Categoria, Novese); os dois títulos são oficiais
- 1926/27: título revogado: o Torino ganhou o grupo final, mas a federação tirou o título em 03/11/1927 (caso Allemandi, suborno de um jogador da Juventus); o título não foi dado a ninguém

## 6. Campeões, rebaixados e punições

**Títulos:**

- Juventus: 36
- Inter de Milão: 21
- Milan: 19
- Genoa: 9
- Bologna: 7
- Torino: 7
- Pro Vercelli: 7
- Napoli: 4
- Roma: 3
- Fiorentina: 2
- Lazio: 2
- Cagliari: 1
- Verona: 1
- Sampdoria: 1
- Casale: 1
- Novese: 1
- Sem campeão: 2004/05, 1926/27

**Rebaixamentos:** 273 no total; quem mais caiu: Brescia (13), Bari (11), Atalanta (11), Verona (10), Genoa (9).

**Punições em pontos:**

- 1959/60: Genoa -18
- 1973/74: Sampdoria -3
- 1973/74: Foggia -6
- 1976/77: Napoli -1
- 1980/81: Bologna -5
- 1980/81: Avellino -5
- 1980/81: Perugia -5
- 1986/87: Udinese -9
- 1987/88: Empoli -5
- 1998/99: Empoli -2
- 2005/06: Milan -30
- 2005/06: Fiorentina -30
- 2005/06: Lazio -30
- 2006/07: Lazio -3
- 2006/07: Milan -8
- 2006/07: Fiorentina -15
- 2006/07: Reggina -11
- 2006/07: Siena -1
- 2010/11: Bologna -3
- 2011/12: Atalanta -6
- 2012/13: Sampdoria -1
- 2012/13: Atalanta -2
- 2012/13: Torino -1
- 2012/13: Siena -6
- 2014/15: Parma -7
- 2018/19: Chievo -3
- 2022/23: Juventus -10

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ita-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1933/34 · AC Milan · Casale:** [6, 2] o ogol e a tabela da Wikipédia fecham com este placar
- **1933/34 · AS Livorno · US Palermo:** [3, 2] o ogol e a tabela da Wikipédia fecham com este placar
- **1933/34 · Torino FC · AS Roma:** [3, 6] o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 40, Torino 29)
- **1933/34 · Juventus · Bologna FC:** [4, 1] o ogol e a tabela da Wikipédia fecham com este placar
- **1934/35 · US Alessandria 1912 · AS Roma:** [1, 6] o ogol e a tabela da Wikipédia fecham com este placar; os pontos da RSSSF também (Roma 35, Alessandria 29)
- **1958/59 · Calcio Padova · Lazio Roma:** [3, 1] o ogol e a tabela da Wikipédia fecham com este placar
- **1952/53 · Torino FC · US Palermo:** [3, 1] gol de Cecconi (Palermo) aos 4 minutos na ficha da Wikipédia it (AC Torino 1952-1953); a matriz e a tabela da Wikipédia it e en e o transfermarkt dão 3-1
- **1962/63 · SSC Napoli · US Palermo:** [3, 1] a matriz e a tabela da Wikipédia it e en, a página do US Palermo 1962-1963 e o transfermarkt dão 3-1 (autor do gol do Palermo não encontrado)

### Resultados decididos fora de campo (`TRIBUNAL`)

- **2005/06 · A.C.R. Messina · Empoli FC:** [0, 3] abandonado aos 89 minutos com 1-2; vitória de 3-0 dada ao Empoli (RSSSF; ogol e Wikipédia contam 0-3). O engsoccerdata, o football-data e a ESPN trazem o 1-2 de campo
- **2020/21 · Hellas Verona · AS Roma:** [3, 0] 0-0 em campo; a Roma escalou um jogador irregular e perdeu por 3-0 (ogol: "DA"; as tabelas da RSSSF e da Wikipédia contam 3-0). O engsoccerdata traz 0-0
- **1929/30 · US Cremonese · AC Milan:** [0, 2] 0-2 a tavolino (RSSSF "0-2 *"; matriz da Wikipédia it)
- **1930/31 · Legnano · Lazio Roma:** [0, 2] 0-2 a tavolino (matriz da Wikipédia it)
- **1963/64 · AS Bari · Genoa CFC:** [0, 2] 0-2 a tavolino (matriz da Wikipédia it; página do AS Bari 1963-1964)

### Mando de campo corrigido (`INVERTIDOS`)

- **1965/66 · 1965-11-21 · Torino FC · Juventus:** a RSSSF traz Juventus 2-0 Torino na 10ª rodada; no returno, Torino 0-0 Juventus
- **1965/66 · 1966-01-23 · Bologna FC · Cagliari Calcio:** a RSSSF traz Cagliari 1-3 Bologna na 18ª rodada, jogado em Bolonha; no turno, Bologna 1-0 Cagliari

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1945/46 · Andrea Doria:** fundiu-se com a Sampierdarenese em 1946 e formou a Sampdoria
- **1945/46 · Sampierdarenese:** fundiu-se com a Andrea Doria em 1946 e formou a Sampdoria
- **1945/46 · Ancona Calcio:** clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- **1945/46 · US Palermo:** clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- **1945/46 · Pescara Calcio:** clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- **1945/46 · Salernitana Calcio 1919:** clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B
- **1945/46 · AC Siena:** clube da Serie B no torneio misto do Centro-Sul; voltou à Serie B

### Ogol x Wikipédia (`OGOL_WIKI`)

- o ogol e a tabela da Wikipédia fecham com este placar

### Gols da Wikipédia (`WIKI_GOLS`)

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos

### Declassados para o último lugar fora de campo (`DECLASSADOS`)

- **1947/48:** [SSC Napoli] declassado ao último lugar por tentativa de corrupção (terminou em 18º em campo); Wikipédia it, Serie A 1947-1948, classifica finale

### Rebaixados em campo e readmitidos (`READMITIDOS`)

- **1942/43 · AS Bari:** rebaixado em campo (triangular com Triestina e Venezia) e readmitido
- **1942/43 · Sampierdarenese:** rebaixado em campo (como Liguria) e readmitido
- **1954/55 · SPAL 1907 Ferrara:** rebaixado em campo e readmitido (ficou no lugar de Udinese e Catania, punidos)
- **1954/55 · Pro Patria:** rebaixado em campo e readmitido (ficou no lugar de Udinese e Catania, punidos)
- **2005/06 · A.C.R. Messina:** rebaixado em campo e readmitido (Calciopoli)

### Ordem entre empatados pela Wikipédia it (classifica avulsa) (`ORDEM_ITWIKI`)

- **1982/83:** {11: 'Genoa CFC', 12: 'Pisa SC'}
- **1986/87:** {9: 'Torino FC', 10: 'Como Calcio', 11: 'ACF Fiorentina'}
- **1987/88:** {10: 'Como Calcio', 11: 'Hellas Verona'}
- **1988/89:** {10: 'AC Cesena', 11: 'Lazio Roma', 12: 'Ascoli Calcio', 13: 'Bologna FC', 14: 'Hellas Verona', 15: 'Pescara Calcio', 16: 'Torino FC'}
- **1989/90:** {12: 'AC Cesena', 13: 'ACF Fiorentina'}
- **1991/92:** {10: 'Atalanta', 11: 'Lazio Roma'}
- **1993/94:** {10: 'Genoa CFC', 11: 'US Cremonese'}

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1929/30:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- **1930/31:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos, menos o Brescia: a RSSSF dá 32 pontos, mas a base, o ogol e a Wikipédia dão 13 vitórias e 8 empates (34 pontos)
- **1945/46:** Andrea Doria x Sampierdarenese (21/10/1945): o ogol traz 0-1 e a base 0-0. Os grupos de 1945/46 não têm tabela publicada legível para desempatar: fica a base
- **1947/48:** a base traz só 380 dos 420 jogos (21 clubes): os que faltam entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- **1948/49:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos (Bologna: a Wikipédia dá 11 vitórias e 18 empates; os jogos e a RSSSF, 12 e 17)
- **1952/53:** a base traz Novara 3-2 Pro Patria duas vezes; o ogol mostra que o jogo de 03/05/1953 foi Pro Patria 2-3 Novara (o returno)
- **1959/60:** Genoa: 18 pontos a menos (suborno), e mandado para a Serie B; a Wikipédia desconta, a classificação da RSSSF não
- **1963/64:** os dois jogos de 07/06/1964 que só o ogol traz são desempates (spareggi): Bologna 2-0 Inter, pelo título, e Sampdoria 2-0 Modena, pelo rebaixamento. Entram na fase "Desempate", fora da tabela
- **1993/94:** a tabela da Wikipédia dá à Cremonese 8 vitórias e 16 empates; os jogos e a RSSSF dão 9 e 14 (os mesmos 32 pontos)
- **2004/05:** os dois jogos de junho de 2005 que só o ogol traz (Parma x Bologna) são o desempate (spareggio) de rebaixamento: entram na fase "Desempate", fora da tabela
- **1953/54:** o triangular de rebaixamento (Udinese, SPAL e Palermo; caiu o Palermo) entra na fase "Desempate" com os placares, datas e autores dos gols da RSSSF (tablesi/ital54.html); a Wikipédia it só traz a tabela
- **2005/06:** Calciopoli: a ordem oficial (Wikipédia) põe a Juventus em último e desconta pontos de Fiorentina, Lazio e Milan; a Inter recebeu o título

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** não entraram. A RSSSF traz os autores rodada a rodada em muitas temporadas antigas (formato italiano, "MARCATORI"); dá para ler num próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Spareggi de vaga europeia** (1986/87, 1987/88, 1988/89, 1998/99, 1999/2000): ficam de fora; os de título e de rebaixamento entram na fase "Desempate", fora da tabela (o triangular de 1953/54 pela RSSSF).
- **Campeonatos de 1897/98 a 1928/29** (grupos regionais e finais): ficam para depois; o ogol tem os calendários.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- Era antiga (1898 a 1928/29, IT-017, em antigo.py): 29 edições pela Wikipédia em italiano. 713 jogos vêm só do Tabellone (sem data); 37 classificações de grupo diferem dos jogos (quase todas em 1 ou 2 gols, ou um jogo que o calendário não traz), listadas no relatório. A RSSSF (italhist98-25.html e ital24-29.html, em data/coleta/ita-1/rsssf-antigo/) só tem tabelas a partir de 1909/10; o próximo passo seria o Almanacco Illustrato.
- Era antiga: a classificação final de cada edição é montada (campeão do albo d'oro, depois a fase alcançada e a posição no grupo); não há classificação oficial além do campeão.

**Com o agente de revisão:** decisões da coleta que ele confere.

- Era antiga: as 37 classificações de grupo que diferem dos jogos e a identidade dos clubes antigos (clubes_ita.py, _ANTIGOS).

## 10. Arquivos

- Código: `coleta/ita-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_ita.py`.
- Fontes baixadas: `data/coleta/ita-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ita-1/`.
- Pacote: `data/coleta/ita-1/pacote/`; relatório: `docs/coleta/ita-1.md`.
- Refazer do zero: `python coleta/ita-1/baixar.py ...` (ver o docstring), `python coleta/ita-1/importar.py`, `python coleta/comum-europa/testar_carga.py ita-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

