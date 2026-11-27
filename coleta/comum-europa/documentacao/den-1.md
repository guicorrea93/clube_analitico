# Campeonato Dinamarquês (`den-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/den-1/pacote/` e do importador `coleta/den-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/den-1.md`.

## 1. O que temos

- **Edições:** 112, de 1912/13 a 2025/26.
- **Jogos:** 14016; **gols:** 42946; **gols com autor:** 11661 (27%); **cartões:** 12026; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 72; **artilheiros:** 84 temporadas com artilheiro (98 linhas, com empates).
- **Classificação final:** 112 temporadas; **rodada a rodada:** 30 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2390 linhas, de 181 tabelas.
- **Observação da competição:** Os 112 títulos que a federação (DBU) reconhece, desde 1912/13: Landsfodboldturneringen (1912/13-1926/27, o campeão de Copenhague contra o das províncias), Danmarksturneringen (liga desde 1928/29), torneio da guerra (1940/41-1944/45), 1. division e, desde 1991, Superligaen. Não inclui o campeonato de Copenhague de 1889 a 1912 (regional), 1914/15 (suspenso) nem 1927/28 (sem campeão).

## 2. Fontes e regras

**Fontes:**

- Wikipédia (en): tabelas, matriz de resultados (base dos jogos de 1945/46 a 1990), mata-mata da Landsfodboldturneringen e do torneio da guerra;
- ogol (zerozero): base dos jogos desde 1991, com data, hora e rodada; calendários em `data/cache/ogol-den-1/`;
- RSSSF: tabelas de 1927 a 1998 (denhist.html; a única fonte de 1928/29), página de cada temporada desde 1995/96, lista de campeões e de artilheiros;
- football-data: placar e hora desde 2012/13;
- ESPN (liga `den.1`): estádio, público, gols e cartões desde 2006/07 (25 clubes casados por votação).

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; antes de 1945, a final e o mata-mata, depois a tabela; com grupos finais, o grupo do título, depois os outros). Pontos 2-1-0 até 1994/95 e 3-1-0 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 15 tabelas, saldo em 92, confronto direto em 2).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 166 tabelas fecham com os jogos e 13 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1912/13, 1913/14, 1915/16, 1916/17, 1917/18, 1918/19, 1919/20, 1920/21, 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1928/29, 1929/30, 1930/31, 1931/32, 1932/33, 1933/34, 1934/35, 1935/36, 1936/37, 1937/38, 1938/39, 1939/40, 1940/41, 1941/42, 1942/43, 1943/44, 1944/45, 1951/52, 1956/57, 1965, 1983, 1991/92.
- Temporadas com alguma tabela divergente: 1951/52, 1956/57, 1965, 1983, 1991/92, 2005/06, 2006/07, 2007/08.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1910s | 33 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 39 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 493 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 939 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1320 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 1860 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2168 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 1846 | 90% | 58% | 78% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1980 | 100% | 60% | 100% | 40% | 0% | 0% | 0% | 84% | 1.1 |
| 2010s | 2180 | 100% | 100% | 54% | 87% | 45% | 0% | 0% | 60% | 2.5 |
| 2020s | 1158 | 100% | 100% | 51% | 83% | 94% | 0% | 0% | 99% | 3.8 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1912/13 a 1913/14: 11 clubes
- 1915/16 a 1917/18: 10 clubes
- 1918/19 a 1919/20: 11 clubes
- 1920/21 a 1922/23: 10 clubes
- 1923/24 a 1925/26: 11 clubes
- 1926/27: 6 clubes
- 1928/29: 25 clubes
- 1929/30 a 1939/40: 10 clubes
- 1940/41: 22 clubes
- 1941/42: 28 clubes
- 1942/43: 29 clubes
- 1943/44: 28 clubes
- 1944/45: 29 clubes
- 1945/46 a 1956/57: 10 clubes
- 1958 a 1974: 12 clubes
- 1975 a 1985: 16 clubes
- 1986 a 1990: 14 clubes
- 1991 a 1994/95: 10 clubes
- 1995/96 a 2015/16: 12 clubes
- 2016/17 a 2019/20: 14 clubes
- 2020/21 a 2025/26: 12 clubes

**Pontos por vitória:**

- 1912/13 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1912/13 a 1926/27: Landsfodboldturneringen
- 1928/29 a 1939/40: Danmarksturneringen
- 1940/41 a 1944/45: Danmarksmesterskabsturneringen (torneio da guerra)
- 1945/46 a 1990: 1. division
- 1991 a 2025/26: Superligaen

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1912/13: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1913/14: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1915/16: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1916/17: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1917/18: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1918/19: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1919/20: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1920/21: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1921/22: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1922/23: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1923/24: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico); Desempate da final (mata_mata, jogo_unico)
- 1924/25: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1925/26: Campeonato de Copenhague (grupos, pontos_corridos); Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico); Desempate da final (mata_mata, jogo_unico)
- 1926/27: Torneio provincial (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1928/29: Grupos (grupos, pontos_corridos); Fase final (grupos, pontos_corridos)
- 1940/41: Grupos (grupos, pontos_corridos); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1941/42: Grupos (grupos, pontos_corridos); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1942/43: Grupos (grupos, pontos_corridos); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1943/44: Grupos (grupos, pontos_corridos); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1944/45: Grupos (grupos, pontos_corridos); Série 1, mata-mata (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1991/92: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos)
- 1992/93: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos)
- 1993/94: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos)
- 1994/95: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos)
- 2016/17: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de classificação (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta); Play-off de rebaixamento (mata_mata, ida_volta)
- 2017/18: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de classificação (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta); Play-off de rebaixamento (mata_mata, ida_volta)
- 2018/19: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de classificação (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta); Play-off de rebaixamento (mata_mata, ida_volta)
- 2019/20: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de classificação (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta); Play-off de rebaixamento (mata_mata, ida_volta)
- 2020/21: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2021/22: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2022/23: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2023/24: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2024/25: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2025/26: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols: 95 temporadas
- jogo único; empate, jogo extra: 49 temporadas
- pontos, saldo de gols; pontos acumulados com a fase regular: 20 temporadas
- pontos, média de gols (goal average): 15 temporadas
- soma dos placares; empate, jogo extra ou sorteio: 14 temporadas
- pontos, saldo de gols; começa com metade dos pontos do outono: 4 temporadas
- pontos, confronto direto, saldo de gols: 2 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1956/57: liga de um ano e meio (1956-1957), em três turnos, na passagem para o ano civil
- 1991: só a primavera de 1991 (primeira Superliga), na passagem para outono a primavera
- 1991/92: grupo final com metade dos pontos do outono (em ajuste_pontos)
- 1992/93: grupo final com metade dos pontos do outono (em ajuste_pontos)
- 1993/94: grupo final com metade dos pontos do outono (em ajuste_pontos)
- 1994/95: grupo final com metade dos pontos do outono (em ajuste_pontos)
- 2003/04: punições: AB -9 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Copenhague: 16
- KB: 15
- Brøndby: 11
- B.93: 9
- AB: 9
- B 1903: 7
- Frem: 6
- AGF: 6
- Vejle: 5
- Esbjerg: 5
- AaB: 4
- Midtjylland: 4
- Hvidovre: 3
- OB: 3
- Køge: 2
- B 1909: 2
- Lyngby: 2
- Silkeborg: 1
- Herfølge: 1
- Nordsjælland: 1

**Rebaixamentos:** 169 no total; quem mais caiu: B 1909 (11), Vejle (8), Esbjerg (7), AaB (7), Køge (7).

**Punições em pontos:**

- 1991/92: Lyngby -11
- 1991/92: B 1903 -10
- 1991/92: Frem -8
- 1991/92: AGF -9
- 1991/92: AaB -9
- 1991/92: Silkeborg -8
- 1991/92: Brøndby -12
- 1991/92: Næstved -8
- 1992/93: Copenhague -13
- 1992/93: OB -11
- 1992/93: Brøndby -10
- 1992/93: AaB -10
- 1992/93: Silkeborg -9
- 1992/93: AGF -9
- 1992/93: Lyngby -8
- 1992/93: Næstved -7
- 1993/94: Silkeborg -12
- 1993/94: Copenhague -11
- 1993/94: Brøndby -10
- 1993/94: OB -12
- 1993/94: AaB -8
- 1993/94: Lyngby -10
- 1993/94: Ikast -8
- 1993/94: AGF -7
- 1994/95: AaB -13
- 1994/95: Brøndby -13
- 1994/95: Silkeborg -8
- 1994/95: AGF -7
- 1994/95: Næstved -8
- 1994/95: Copenhague -8
- 1994/95: Lyngby -9
- 1994/95: OB -12
- 2003/04: AB -9

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/den-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1991/92 · B 1903:** fundiu-se com o KB e formou o FC København em 1992

### Jogos decididos fora de campo, com o placar oficial dado à mão (`DECIDIDOS`)

- **2002/03 · Silkeborg · AB:** [3, 0] 3-1 no campo; dado como 3-0 porque o AB escalou um jogador irregular (Lennart Lynge Larsen) (RSSSF)
- **2002/03 · AB · Midtjylland:** [0, 3] 1-2 no campo; dado como 0-3 porque o AB escalou um jogador irregular (Lennart Lynge Larsen) (RSSSF)
- **2006/07 · Esbjerg · Silkeborg · 2007-04-22:** [0, 3] 1-2 no campo; dado como 0-3 porque o Esbjerg escalou um jogador irregular (nota da Wikipédia; a ESPN e as tabelas dão 0-3)

## 8. O que não deu para coletar

- **Jogos das ligas de Copenhague (até 1927), da liga de 1928/29 a 1939/40 e das séries da guerra:** nenhuma fonte em lote traz (só as tabelas); o banco Haslund não é baixável em lote.
- **Datas e rodadas até 1990** (só as matrizes e as listas do mata-mata).
- **Autores dos gols e cartões** antes da ESPN (2006/07), fora as páginas da RSSSF.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Sem os jogos das ligas de Copenhague (até 1927), da liga de 1928/29 a 1939/40 e das séries da guerra: só as tabelas (Wikipédia e RSSSF); o banco Haslund não é baixável em lote. 1928/29 só pela RSSSF (a Wikipédia não tem o artigo).
- Sem datas e rodadas até 1990; autores dos gols e cartões só com a ESPN (desde 2006/07; quase sem lances de 2011/12 a 2013/14) e, para os gols, com as páginas da RSSSF.
- Fora do escopo (decisão do Guilherme, 25/11/2026): Copenhague de 1889 a 1912, 1914/15 (suspenso), 1927/28 (sem campeão) e 2026/27 (em andamento).

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade: KB, B 1903 e FC København separados (como a RSSSF); pelos links, Horsens fS = AC Horsens, Farum = Nordsjælland, Haderslev = SønderjyskE, B 1901 = Nykøbing FC, Helsingør IF = FC Helsingør; em 1976 a matriz da Wikipédia liga o Randers Freja ao Randers FC (fica o Freja, pela tabela); o BK Viktoria de 1928/29 sem cidade confirmada.
- Antes de 1945: ordem pela final e pelo mata-mata, depois pela tabela; números da tabela mais os do mata-mata.
- Superliga com grupos (1991/92-1994/95 e desde 2016/17): fase regular pelo primeiro encontro de cada par (o ogol não numera as rodadas); 2016/17 completado pelo football-data nos grupos de classificação; do 7º ao 14º de 2016/17 a 2019/20 pela fase regular.

## 10. Arquivos

- Código: `coleta/den-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_den.py`.
- Fontes baixadas: `data/coleta/den-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-den-1/`.
- Pacote: `data/coleta/den-1/pacote/`; relatório: `docs/coleta/den-1.md`.
- Refazer do zero: `python coleta/den-1/baixar.py ...` (ver o docstring), `python coleta/den-1/importar.py`, `python coleta/comum-europa/testar_carga.py den-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

