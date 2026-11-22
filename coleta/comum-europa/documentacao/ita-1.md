# Campeonato Italiano (`ita-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ita-1/pacote/` e do importador `coleta/ita-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ita-1.md`.

## 1. O que temos

- **Edições:** 94, de 1929/30 a 2024/25.
- **Jogos:** 28864; **gols:** 74076; **gols com autor:** 23642 (32%); **cartões:** 42440; **jogos com estatísticas** (chutes, faltas, escanteios): 7585.
- **Clubes:** 69; **artilheiros:** 94 temporadas com artilheiro (105 linhas, com empates).
- **Classificação final:** 94 temporadas; **rodada a rodada:** 93 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2051 linhas, de 113 tabelas.
- **Observação da competição:** Serie A desde a criação do grupo único (1929/30). Sem 1943/44 e 1944/45 (Segunda Guerra). 1945/46 foi a Divisione Nazionale: grupos Norte e Centro-Sul e grupo final. Não inclui os desempates (spareggi) de título e de rebaixamento nem os campeonatos de antes de 1929/30 (grupos regionais e finais).

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1929/30-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ita-1/` para os escudos;
- ESPN (liga `ita.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (Maurizio Mariani e outros): tabela final, nas temporadas em que a página traz uma tabela legível;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e Capocannoniere.

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Roma). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94, 3 a partir de 1994/95. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 50, saldo de gols em 33, média de gols em 11); é ele que ordena a classificação rodada a rodada. Até 2004/05, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio), que não está no pacote.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 161 tabelas fecham com os jogos e 9 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1930/31.
- Temporadas com alguma tabela divergente: 1929/30, 1930/31, 1948/49, 1952/53, 1959/60, 1962/63, 1963/64, 1993/94.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 306 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 2664 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 2628 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 3208 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2862 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2532 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3504 | 100% | 91% | 100% | 89% | 73% | 22% | 54% | 90% | 4.2 |
| 2010s | 3800 | 100% | 100% | 100% | 100% | 92% | 0% | 100% | 100% | 5.0 |
| 2020s | 1900 | 100% | 100% | 100% | 100% | 80% | 0% | 100% | 100% | 4.6 |

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
- 2004/05 a 2024/25: 20 clubes

**Pontos por vitória:**

- 1929/30 a 1993/94: 2
- 1994/95 a 2024/25: 3

**Nome oficial:**

- 1929/30 a 1942/43: Serie A
- 1945/46: Divisione Nazionale
- 1946/47 a 2024/25: Serie A

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1945/46: Grupos (grupos, pontos_corridos); Fase final (grupos, pontos_corridos)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto, saldo de gols, gols pró: 49 temporadas
- pontos, saldo de gols, gols pró: 33 temporadas
- pontos, média de gols (goal average): 11 temporadas
- pontos: 2 temporadas

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

## 6. Campeões, rebaixados e punições

**Títulos:**

- Juventus: 34
- Inter de Milão: 18
- Milan: 16
- Torino: 6
- Bologna: 5
- Napoli: 4
- Roma: 3
- Fiorentina: 2
- Lazio: 2
- Cagliari: 1
- Verona: 1
- Sampdoria: 1
- Sem campeão: 2004/05

**Rebaixamentos:** 277 no total; quem mais caiu: Brescia (13), Bari (11), Atalanta (11), Palermo FC (10), Genoa (9).

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

### Resultados decididos fora de campo (`TRIBUNAL`)

- **2005/06 · A.C.R. Messina · Empoli FC:** [0, 3] abandonado aos 89 minutos com 1-2; vitória de 3-0 dada ao Empoli (RSSSF; ogol e Wikipédia contam 0-3). O engsoccerdata, o football-data e a ESPN trazem o 1-2 de campo
- **2020/21 · Hellas Verona · AS Roma:** [3, 0] 0-0 em campo; a Roma escalou um jogador irregular e perdeu por 3-0 (ogol: "DA"; as tabelas da RSSSF e da Wikipédia contam 3-0). O engsoccerdata traz 0-0

### Mando de campo corrigido (`INVERTIDOS`)

- **1965/66 · 1965-11-21 · Torino FC · Juventus:** a RSSSF traz Juventus 2-0 Torino na 10ª rodada; no returno, Torino 0-0 Juventus
- **1965/66 · 1966-01-23 · Bologna FC · Cagliari Calcio:** a RSSSF traz Cagliari 1-3 Bologna na 18ª rodada, jogado em Bolonha; no turno, Bologna 1-0 Cagliari

### Ogol x Wikipédia (`OGOL_WIKI`)

- o ogol e a tabela da Wikipédia fecham com este placar

### Gols da Wikipédia (`WIKI_GOLS`)

- a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1929/30:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- **1930/31:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos, menos o Brescia: a RSSSF dá 32 pontos, mas a base, o ogol e a Wikipédia dão 13 vitórias e 8 empates (34 pontos)
- **1945/46:** Andrea Doria x Sampierdarenese (21/10/1945): o ogol traz 0-1 e a base 0-0. Os grupos de 1945/46 não têm tabela publicada legível para desempatar: fica a base
- **1947/48:** a base traz só 380 dos 420 jogos (21 clubes): os que faltam entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- **1948/49:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos (Bologna: a Wikipédia dá 11 vitórias e 18 empates; os jogos e a RSSSF, 12 e 17)
- **1952/53:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos / a base traz Novara 3-2 Pro Patria duas vezes; o ogol mostra que o jogo de 03/05/1953 foi Pro Patria 2-3 Novara (o returno)
- **1959/60:** Genoa: 18 pontos a menos (suborno), e mandado para a Serie B; a Wikipédia desconta, a classificação da RSSSF não
- **1962/63:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos
- **1963/64:** a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os pontos da RSSSF fecham com os jogos / os dois jogos de 07/06/1964 que só o ogol traz são desempates (spareggi): Bologna 2-0 Inter, pelo título, e Sampdoria 2-0 Modena, pelo rebaixamento. Ficam de fora
- **1993/94:** a tabela da Wikipédia dá à Cremonese 8 vitórias e 16 empates; os jogos e a RSSSF dão 9 e 14 (os mesmos 32 pontos)
- **2004/05:** os dois jogos de junho de 2005 que só o ogol traz (Parma x Bologna) são o desempate (spareggio) de rebaixamento: ficam de fora
- **2005/06:** Calciopoli: a ordem oficial (Wikipédia) põe a Juventus em último e desconta pontos de Fiorentina, Lazio e Milan; a Inter recebeu o título

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** não entraram. A RSSSF traz os autores rodada a rodada em muitas temporadas antigas (formato italiano, "MARCATORI"); dá para ler num próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Spareggi (jogos-desempate de título e rebaixamento):** ficam de fora.
- **Campeonatos de 1897/98 a 1928/29** (grupos regionais e finais): ficam para depois; o ogol tem os calendários.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Incluir 2025/26 (o guia pede até a última temporada terminada; pedir o ok do Guilherme).
- Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).

## 10. Arquivos

- Código: `coleta/ita-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_ita.py`.
- Fontes baixadas: `data/coleta/ita-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ita-1/`.
- Pacote: `data/coleta/ita-1/pacote/`; relatório: `docs/coleta/ita-1.md`.
- Refazer do zero: `python coleta/ita-1/baixar.py ...` (ver o docstring), `python coleta/ita-1/importar.py`, `python coleta/comum-europa/testar_carga.py ita-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

