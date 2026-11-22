# Revisão: Campeonato Italiano (`ita-1`)

Revisão profunda (3ª rodada), 22/11/2026. Achados com prefixo `IT`.

**Resumo.** Títulos (95 de 95), artilheiros e escudos certos; placares quase todos certos (5 erros em 28.896 jogos) e números da classificação fechando com a Wikipédia it em 1.692 de 1.703 linhas.
Os problemas: rebaixados de 1945/46 (7 clubes marcados sem ter caído), Napoli 1947/48 fora do último lugar, 622 datas erradas (1947/48 com datas depois do fim do campeonato) e punições invisíveis na tela.
Cinco perguntas ao Guilherme (campeonatos de 1898-1929, Serie B em 1945/46, readmitidos, spareggi, ordem dos empatados).

Fonte principal nova: Wikipédia it (página de cada temporada: classificação, matriz, calendário com data por jogo, notas, artilharia), lida por `revisao/IT/itwiki.py`; terceira opinião: RSSSF (rodadas e notas), páginas de clube da Wiki it e transfermarkt. A coleta usou engsoccerdata, ogol, football-data, ESPN, Wikipédia en e as tabelas da RSSSF.

## Pacote x banco x site
- Pacote e banco iguais: 95 edições (1929/30–2025/26), 29.244 jogos, 24.564 gols com autor, 43.962 cartões; campeão e vice das 95 edições iguais. `painel/dados/ita-1.js` local também com 95.
- O site está com 94 edições (sem 2025/26): IT-015.

## A. Edições e títulos
- Conferido: lista de edições, nomes (Serie A; Divisione Nazionale 1945/46), número de clubes por época, pontos por vitória (2 até 1993/94), campeões das 95 edições contra o albo d'oro e as cores da Wiki it. Tudo certo, inclusive 2004/05 sem campeão e 2005/06 da Inter.
- 1943/44 e 1944/45 fora: certo (Campionato Alta Italia 1944 é título honorífico).
- O painel conta títulos só desde 1929/30 (Juventus 34, oficial 36): IT-017 (decisão).

## B. Classificação final
- Amostra: todas as 1.703 linhas contra a Wiki it. Números iguais em 1.692; as 11 diferenças vêm de 5 placares errados (IT-003 a IT-007). Punições iguais nas 27 linhas.
- Posição: 195 diferenças são posição dividida ("pari merito") na Wiki it; ordem trocada de verdade em 7 temporadas de 1982/83 a 1993/94, sem efeito em título, vaga ou queda (IT-014).
- 1947/48: Napoli em 18º; foi declassado ao último lugar (IT-002, alta).
- Rebaixados: 95 temporadas contra a Wiki it. Errado em 1945/46 (IT-001, alta). Readmitidos sem nota em 1942/43, 1954/55 e 2005/06 (IT-012). 1945/46: pontos de grupos + final somados (IT-016).

## C. Jogos
- Placares: todos os 28.896 jogos de pontos corridos contra a matriz da Wiki it. 33 diferenças: 5 erros do pacote (IT-003 Cremonese x Milan 1929/30, IT-004 Legnano x Lazio 1930/31, IT-005 Bari x Genoa 1963/64, IT-006 Torino x Palermo 1952/53, IT-007 Napoli x Palermo 1962/63); o resto é erro da matriz da Wiki (IT-019).
- Tribunal: os 23 `awd` do pacote conferidos com a RSSSF: 21 certos, 2 com placar errado (IT-003, IT-004). 31 jogos "a tavolino" sem a marca (IT-010).
- Datas: 28.248 jogos contra o calendário da Wiki it (26.830 iguais, 452 com 1 dia). Nos 988 com mais diferença, a RSSSF decide: 622 erros do pacote (IT-008), 14 em 1945/46 e 1 em 2001/02 (IT-009). Amostra por década: todas as décadas cobertas, porque a conferência foi de todos os jogos.
- Varredura de tela (`revisao/IT/varredura.py`): 57 casos de "clube com 2 jogos no mesmo dia", todos explicados pelas datas erradas (1934/35, 1945/46, 1947/48, 1982/83, 1991/92, 2001/02).
- Spareggi fora do pacote (IT-018, decisão).

## D. Gols e artilheiros
- Artilheiro de 93 de 95 temporadas igual à Wiki it. 1968/69 Riva 21 (Wiki it 20; RSSSF e Wiki en 21): não é erro (IT-020). 1945/46: Gabetto 22 (infobox da Wiki it), certo.

## E. Clubes e escudos
- 69 clubes, todos ITA, nomes únicos no banco; nomes de época certos (Ambrosiana = Inter, Liguria = Sampierdarenese, Pro Livorno = Livorno, Lanerossi = Vicenza). Sampdoria separada de Andrea Doria e Sampierdarenese (decisão da coleta).
- Escudos: folha de contato dos 69 (`revisao/IT/folha_escudos.py`): todos certos.
- 1945/46: clubes da Serie B contados como participantes da 1ª divisão (IT-011, decisão).

## F. Painel
- Telas no site (Chrome sem janela): Pódio, Curiosidades, Participações, Classificação 1945/46, 1947/48 e 2005/06, Participantes 1945/46, Resumo 2004/05. Sem erro de tela.
- 2005/06: punições e o último lugar da Juventus não aparecem (IT-013).
- Curiosidades conferidas: maior goleada (Torino 10-0 Alessandria, 1947/48), mais gols (Milan 9-3 Atalanta, 1972/73), Juventus 102 pontos (2013/14), Brescia 12 pontos (1994/95), invictos Milan 1991/92 e Juventus 2011/12, Inter em todas as 95 edições: certas. "Siena voltou após 58 anos" depende da IT-011.

## Perguntas ao Guilherme
1. Incluir os campeonatos de 1898 a 1928/29 (títulos oficiais: Juventus 36, Inter 21, Milan 19, Genoa 9)? (IT-017)
2. Os 6 clubes da Serie B do torneio misto de 1945/46 contam como participantes da 1ª divisão? (IT-011)
3. Rebaixados em campo e readmitidos (Bari e Liguria 1942/43, SPAL e Pro Patria 1954/55, Messina 2005/06): só uma nota? (IT-012)
4. Incluir os spareggi de título e rebaixamento? (IT-018)
5. Ordem dos empatados pela Wiki it (classifica avulsa)? (IT-014)

Detalhes, opções e recomendação de cada uma: `decisoes_IT.md` (scratchpad da revisão). Scripts em `revisao/IT/`.
