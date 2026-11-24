# Campeonato Neozelandês (`nzl-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/nzl-1/pacote/`, do código `coleta/nzl-1/` e do relatório `docs/coleta/nzl-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 55, de 1970 a 2025; 0 sem jogos.
- **Jogos:** 7480 (7478 com placar); **gols:** 26352; **gols com autor:** 2888 (11%); **cartões:** 0.
- **Clubes:** 101; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 55 edições; **tabelas publicadas guardadas para conferência:** 792 linhas.
- **No banco:** sim; **último commit do pacote:** d7a6379.
- **Observação da competição:** 1ª divisão da Nova Zelândia de 1970 a 2025, uma edição por título, como na lista de campeões nacionais da RSSSF: National Soccer League (1970-1992, pontos corridos), Superclub (1993-1995: ligas regionais, fase nacional e mata-mata), Summer Soccer League (1996-1997/98), North e South Island League com final (1999), National League (2000-2003), NZFC/Premiership (2004/05 a 2020/21, liga e mata-mata) e National League (2022-2025: ligas regionais, fase nacional e final). Desde 1993 o campeão é o da final; 2004 e 2021 não tiveram campeão. Sem jogos só a fase nacional de 1994.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão neozelandesa (nzl-1): uma por título, como na lista de campeões nacionais da RSSSF (nzchamp.html),
de 1970 a 2025. Escopo aprovado pelo Guilherme em 23/11/2026:
- começa em 1970, com a primeira liga nacional (os campeonatos das províncias, 1892-1969, ficam de fora);
- campeão = o da lista oficial: 1970-1992 o 1º da liga; desde 1993 o vencedor da final (Grand Final), com o 1º da fase de
  liga na observação; 2019/20 parou pela covid e o Auckland City foi declarado campeão sem final;
- 2004 (finais canceladas, só ligas regionais) e 2021 (só a "South Central Series", sem título) ficam de fora;
- as ligas regionais que classificam para a fase nacional (1993-1995, 1999 e 2022-2025) entram como 1ª fase da edição,
  um grupo por região;
- o time reserva do Wellington Phoenix (e o do Auckland FC, 2025) leva "Reserves" no nome.

Eras (o que a RSSSF traz):
- 1970-1992 National Soccer League: tabela final e matriz de resultados (sem data nem autor); 1987 também as rodadas 1-14;
- 1993-1995 Superclub: ligas regionais (tabela e matriz), fase nacional (rodadas; 1994 só a tabela) e mata-mata;
- 1996, 1996/97, 1997/98 Summer Soccer League: rodadas e mata-mata (placar com o do intervalo entre parênteses; empate decidido
  nos pênaltis valendo ponto extra em 1996 e 1996/97);
- 1999: North Island e South Island Soccer League e a final entre os campeões;
- 2000-2003 National Club Championship / National League: rodadas (com data e autores) e mata-mata dos 4 primeiros;
- 2004/05-2020/21 NZFC / Premiership: rodadas e mata-mata (2010/11 e 2011/12: a RSSSF só tem as tabelas e o mata-mata;
  os jogos da fase de liga vêm do ogol);
- 2022-2025 National League: ligas regionais (só as tabelas na RSSSF), fase nacional (rodadas) e final.

Cada trecho é (página da RSSSF, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto). O trecho
termina antes da Chatham Cup (copa) e dos playoffs de acesso.
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 45.
- **Edições com alguma tabela divergente** (10; motivo no relatório, na edição): 1973, 1982, 1988, 1990, 1991, 1992, 1993, 2023, 2024, 2025.
- **Edições sem tabela para conferir** (0): nenhuma.
- **Edições com menos jogos que o esperado:** 1994 (274 de 302), 2025 (367 de 368).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970s | 10 | 992 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 1470 | 0% | 0% | 5% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1933 | 26% | 0% | 28% | 0% | 0% | 0% | 8% | 0.0 |
| 2000s | 10 | 846 | 100% | 0% | 96% | 0% | 0% | 0% | 80% | 0.0 |
| 2010s | 10 | 740 | 100% | 0% | 95% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 5 | 1499 | 29% | 0% | 28% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1970: 8 clubes
- 1971 a 1976: 10 clubes
- 1977 a 1986: 12 clubes
- 1987 a 1992: 14 clubes
- 1993 a 1994: 30 clubes
- 1995: 31 clubes
- 1996 a 1996/97: 10 clubes
- 1997/98: 11 clubes
- 1999: 20 clubes
- 2000 a 2003: 10 clubes
- 2004/05 a 2013/14: 8 clubes
- 2014/15: 9 clubes
- 2015/16: 8 clubes
- 2016/17 a 2019/20: 10 clubes
- 2020/21: 8 clubes
- 2022 a 2025: 32 clubes

**Pontos por vitória:**

- 1970 a 1982: 2
- 1983 a 1995: 3
- 1996 a 1996/97: 4
- 1997/98 a 2025: 3

**Nome oficial:**

- 1970 a 1992: National Soccer League <ano>
- 1993 a 1995: Superclub Competition <ano> (National Championship)
- 1996: Summer Soccer League <ano>
- 1996/97 a 1997/98: National Summer Soccer League <ano>
- 1999: National Club Championship <ano>
- 2000: Ansett National Club Championship <ano>
- 2001 a 2003: National League <ano>
- 2004/05 a 2015/16: New Zealand Football Championship <ano>
- 2016/17 a 2020/21: Premiership <ano>
- 2022 a 2025: National League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1970: pontos corridos (8 clubes)
- 1971 a 1976: pontos corridos (10 clubes)
- 1977 a 1986: pontos corridos (12 clubes)
- 1987 a 1992: pontos corridos (14 clubes)
- 1993: ligas regionais (3 grupos, 30 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final
- 1994: jogos incompletos: ligas regionais (3 grupos, 30 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final
- 1995: ligas regionais (3 grupos, 31 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final
- 1996 a 1996/97: fase de liga (10 clubes) + semifinais + final preliminar + final
- 1997/98: fase de liga (11 clubes) + semifinais + final
- 1999: ligas regionais (2 grupos, 20 clubes) + final
- 2000: fase de liga (10 clubes) + semifinais + final
- 2001 a 2003: fase de liga (10 clubes) + semifinais + final preliminar + final
- 2004/05: fase de liga (8 clubes) + semifinais + final
- 2005/06: fase de liga (8 clubes) + rodada eliminatória + semifinais + final preliminar + final
- 2006/07 a 2013/14: fase de liga (8 clubes) + semifinais + final
- 2014/15: fase de liga (9 clubes) + semifinais + final
- 2015/16: fase de liga (8 clubes) + semifinais + final
- 2016/17 a 2018/19: fase de liga (10 clubes) + semifinais + final
- 2019/20: fase de liga (10 clubes)
- 2020/21: fase de liga (8 clubes) + semifinais + final
- 2022 a 2024: ligas regionais (3 grupos, 32 clubes) + fase nacional (10 clubes) + final
- 2025: jogos incompletos: ligas regionais (3 grupos, 32 clubes) + fase nacional (11 clubes) + final

**Fases e grupos de cada edição com mais de uma fase:**

- 1993: Fase regional (grupos, 3 grupos); Fase nacional (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1994: Fase regional (grupos, 3 grupos); Fase nacional (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1995: Fase regional (grupos, 3 grupos); Fase nacional (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1996: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1996/97: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1997/98: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1999: Fase regional (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 2000: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2001: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2002: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2003: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2004/05: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2005/06: Fase de liga (liga); Rodada eliminatória (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final preliminar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2006/07: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2007/08: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2008/09: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2009/10: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2010/11: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2011/12: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2012/13: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013/14: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2014/15: Fase de liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2015/16: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2016/17: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2017/18: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2018/19: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2020/21: Fase de liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022: Fase regional (grupos, 3 grupos); Fase nacional (liga); Final (mata_mata, jogo_unico)
- 2023: Fase regional (grupos, 3 grupos); Fase nacional (liga); Final (mata_mata, jogo_unico)
- 2024: Fase regional (grupos, 3 grupos); Fase nacional (liga); Final (mata_mata, jogo_unico)
- 2025: Fase regional (grupos, 3 grupos); Fase nacional (liga); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 54 edições
- Wikipédia: 1 edições

**Observações das edições:**

- 1993: 1º da fase nacional: Waitakere City
- 1994: a fase nacional só tem a tabela final na RSSSF (os 28 jogos ficam de fora); 1º da fase nacional: Waitakere City
- 1996: temporada de transição (janeiro a maio); 4 pontos por vitória e, no empate, 1 ponto para cada um e disputa de pênaltis valendo 1 ponto extra; 1º da fase de liga: Miramar Rangers
- 1996/97: 4 pontos por vitória e, no empate, 1 ponto para cada um e disputa de pênaltis valendo 1 ponto extra; 1º da fase de liga: Napier City Rovers
- 1999: North Island Soccer League e South Island Soccer League; o título se decide na final entre os dois campeões
- 2000: ponto extra por 4 ou mais gols num jogo; 1º da fase de liga: Mount Wellington
- 2001: 1º da fase de liga: Miramar Rangers
- 2002: 1º da fase de liga: Napier City Rovers
- 2006/07: 1º da fase de liga: Waitakere United
- 2008/09: 1º da fase de liga: Waitakere United
- 2009/10: 1º da fase de liga: Auckland City
- 2011/12: 1º da fase de liga: Auckland City
- 2015/16: 1º da fase de liga: Auckland City
- 2016/17: 1º da fase de liga: Auckland City
- 2018/19: 1º da fase de liga: Auckland City
- 2019/20: temporada interrompida em 18 de março de 2020 pela covid-19; sem mata-mata, o Auckland City (1º da tabela) foi declarado campeão
- 2020/21: 1º da fase de liga: Auckland City
- 2024: 1º da fase nacional: Birkenhead United
- 2025: Central League e Southern League pelo ogol: falta 1 jogo da Central (Petone x Wellington Phoenix Reserves) e, na Southern, Coastal Spirit e Dunedin City Royals têm um jogo a mais e Nelson Suburbs e Wanaka um a menos do que na tabela da RSSSF; 1º da fase nacional: Wellington Olympic

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Auckland City: 11
- Mount Wellington: 6
- Christchurch United: 6
- Waitakere City: 5
- Waitakere United: 5
- Napier City Rovers: 4
- Wellington United: 3
- Team Wellington: 3
- Eastern Suburbs: 2
- North Shore United: 2
- Central United: 2
- Miramar Rangers: 2
- Blockhouse Bay: 1
- Manurewa: 1
- Gisborne City: 1
- Wellington Olympic: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1970 | Blockhouse Bay | Eastern Suburbs |
| 1971 | Eastern Suburbs | Mount Wellington |
| 1972 | Mount Wellington | Blockhouse Bay |
| 1973 | Christchurch United | Mount Wellington |
| 1974 | Mount Wellington | Christchurch United |
| 1975 | Christchurch United | North Shore United |
| 1976 | Wellington United | Mount Wellington |
| 1977 | North Shore United | Stop Out |
| 1978 | Christchurch United | Mount Wellington |
| 1979 | Mount Wellington | Christchurch United |
| 1980 | Mount Wellington | Gisborne City |
| 1981 | Wellington United | Dunedin City |
| 1982 | Mount Wellington | North Shore United |
| 1983 | Manurewa | North Shore United |
| 1984 | Gisborne City | Papatoetoe |
| 1985 | Wellington United | Gisborne City |
| 1986 | Mount Wellington | Miramar Rangers |
| 1987 | Christchurch United | Gisborne City |
| 1988 | Christchurch United | Mount Wellington |
| 1989 | Napier City Rovers | Mount Maunganui |
| 1990 | Waitakere City | Mount Wellington |
| 1991 | Christchurch United | Miramar Rangers |
| 1992 | Waitakere City | Waikato United |
| 1993 | Napier City Rovers | Waitakere City |
| 1994 | North Shore United | Napier City Rovers |
| 1995 | Waitakere City | Waikato United |
| 1996 | Waitakere City | Miramar Rangers |
| 1996/97 | Waitakere City | Napier City Rovers |
| 1997/98 | Napier City Rovers | Central United |
| 1999 | Central United | Dunedin Technical |
| 2000 | Napier City Rovers | Mount Wellington |
| 2001 | Central United | Miramar Rangers |
| 2002 | Miramar Rangers | Napier City Rovers |
| 2003 | Miramar Rangers | East Auckland |
| 2004/05 | Auckland City | Waitakere United |
| 2005/06 | Auckland City | Canterbury United |
| 2006/07 | Auckland City | Waitakere United |
| 2007/08 | Waitakere United | Team Wellington |
| 2008/09 | Auckland City | Waitakere United |
| 2009/10 | Waitakere United | Canterbury United |
| 2010/11 | Waitakere United | Auckland City |
| 2011/12 | Waitakere United | Team Wellington |
| 2012/13 | Waitakere United | Auckland City |
| 2013/14 | Auckland City | Team Wellington |
| 2014/15 | Auckland City | Hawke's Bay United |
| 2015/16 | Team Wellington | Auckland City |
| 2016/17 | Team Wellington | Auckland City |
| 2017/18 | Auckland City | Team Wellington |
| 2018/19 | Eastern Suburbs | Team Wellington |
| 2019/20 | Auckland City | Team Wellington |
| 2020/21 | Team Wellington | Auckland City |
| 2022 | Auckland City | Wellington Olympic |
| 2023 | Wellington Olympic | Auckland City |
| 2024 | Auckland City | Birkenhead United |
| 2025 | Auckland City | Wellington Olympic |

**Rebaixados marcados na classificação:** 25 em 8 edições (só onde a tabela publicada marca a queda); quem mais caiu: Manurewa (2), Mount Maunganui (1), Waterside Karori (1), Western AFC (1), Oratia United (1).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1996: Waitakere City +2
- 1996: North Shore United +3
- 1996: Wellington United +3
- 1996: Napier City Rovers +2
- 1996: Central United +4
- 1996: Mount Maunganui +1
- 1996/97: Waitakere City +1
- 1996/97: Central United +1
- 1996/97: North Shore United +3
- 1996/97: Miramar Rangers +4
- 1996/97: Melville United +2
- 1996/97: Woolston +2
- 1996/97: Mount Maunganui +3
- 2000: Napier City Rovers +4
- 2000: Mount Wellington +2
- 2000: Dunedin Technical +2
- 2000: Manawatu AFC +1
- 2000: Waitakere City +2
- 2000: Central United +3
- 2000: Nelson Suburbs +2
- 2000: Miramar Rangers +1
- 2000: Christchurch City +1
- 2000: Metro FC +1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/nzl-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **nz89 · 35:** «4-0*2-1» → «3-0 2-1»: Christchurch United x Manurewa: a matriz traz 4-0 com a nota "other sources give Christchurch vs Manurewa as 3-0"; a tabela da página (e a da Wikipédia) conta 3-0 (o asterisco colado também impedia a leitura da matriz)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 8)

- **nz01 · 322:** None
- **nz00 · 137:** ({'visitante': 'Miramar'}, 'a página põe "Metro 0-4 Manawatu", mas os quatro autores (Patrick, George, Longley, Bernard) são do Miramar Rangers, e assim Manawatu e Miramar ficam com os 18 jogos da tabela')
- **nz97 · 224:** ({'gv': 0}, 'Napier City Rovers 3-2 Waitakere City na página, sem autor dos gols do Waitakere; a tabela da mesma página conta 3-0 (gols do Waitakere e sofridos do Napier 2 a menos)')
- **nz78 · 34 · Hamilton · Woolston:** ({'gm': 2}, 'a matriz traz Hamilton 3-3 Woolston, mas a tabela da página (igual à da Wikipédia) dá derrota do Hamilton e vitória do Woolston, com um gol a menos do Hamilton: 2-3 (o outro jogo entre os dois, 0-3, não explica a diferença)')
- **nz82 · 38 · Napier City Rovers · Manurewa:** ({'gm_of': 0, 'gv_of': 1, 'especial': 'awd'}, '1-1 em campo; o resultado virou 0-1 para o Manurewa porque o Napier escalou jogador sem registro (Wikipédia, citando Hilton 1991); a tabela da página já conta assim')
- **nz87 · 172 · Mt Maunganui · Christchurch Utd:** ({'gv': 2}, 'a matriz traz 0-1; a lista da 5ª rodada, na mesma página, traz 0-2, e é o que a tabela conta (60 gols do Christchurch United)')
- **wikipedia · 2024 · Birkenhead United · Auckland City:** ({'gm': 1, 'gv': 3}, 'a matriz da Wikipédia traz Birkenhead 3-1 Auckland City; a tabela da RSSSF e a da própria Wikipédia contam vitória do Auckland City por 3-1 (placar invertido na matriz)')
- **nz07 · 72:** ({'especial': 'wo_m', 'gm': 0, 'gv': 1}, 'vitória dada ao Waitakere United sem gols ("awarded 0-0 win"); em campo, 0-1 (o Auckland City escalou jogador irregular)')

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **nz2021 · 95:** tabela do meio da temporada (Halfway Table)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 10)

- **1973:** um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): o Wellington United tem um gol a mais contra o Eastern Suburbs (3-1 e 1-4); não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela
- **1982:** um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): o Miramar Rangers tem um gol a mais contra o Christchurch United (0-2 e 1-3); não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela
- **1988:** um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): um gol do Miramar Rangers aparece como do Manawatu United nos jogos entre os dois (1-2 e 2-3); não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela
- **1990:** um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): o Waikato United tem um gol a mais contra o Waitakere City, e o Wellington United dois a mais a favor e dois a mais contra; não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela
- **1991:** um gol de diferença entre a matriz de resultados e a tabela da mesma página (a tabela é igual à da Wikipédia): o Manurewa tem um gol a mais contra o New Plymouth Rangers (2-0 e 1-1); não dá para saber em qual dos jogos. Ficam os placares da matriz; a classificação é a tabela
- **1992:** a tabela da RSSSF não fecha consigo mesma (581 gols pró x 580 contra) e erra os gols de 5 clubes; a da Wikipédia fecha com os jogos da matriz e é a usada na classificação
- **1993:** fase nacional: a página traz Wellington Olympic 3-0 Christchurch Rangers e a tabela conta um gol do Rangers (3-1?); fica o placar da página
- **2023:** Central League (jogos da matriz da Wikipédia): Wellington Olympic, Petone, Western Suburbs e Stop Out não fecham com a tabela da RSSSF, e a tabela da própria Wikipédia também difere da RSSSF (Wellington Olympic e Western Suburbs). As fontes discordam entre si; ficam os jogos da Wikipédia e a classificação é a tabela da RSSSF
- **2024:** Central League: Wellington Phoenix Reserves x Waterside Karori (2-2 e 2-1 na matriz da Wikipédia) com 2 gols a menos para cada lado do que nas tabelas da RSSSF e da Wikipédia; Southern League: Ferrymead Bays com um gol a mais. Ficam os jogos da Wikipédia e a classificação é a tabela da RSSSF
- **2025:** Central e Southern League pelo ogol (a matriz da Wikipédia não serve): falta 1 jogo da Central (Petone x Wellington Phoenix Reserves) e, na Southern, Coastal Spirit e Dunedin City Royals têm um jogo a mais e Nelson Suburbs e Wanaka um a menos; a classificação é a tabela da RSSSF

### Identidade dos clubes

Regras em `coleta/nzl-1/clubes_nzl.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da Nova Zelândia (nzl-1): cada grafia da RSSSF e do ogol vira um clube, com cidade e região.

Decisões (critério: o mesmo clube com outro nome é um clube só; fusão ou franquia nova é outro clube):
- "Auckland City" de 1972 é o Mt Albert-Ponsonby com outro nome (voltou ao nome antigo depois); o Auckland City de 2004 em
  diante é a franquia da NZFC, outro clube;
- Wellington Diamond United (1973-1984) e Wellington United (fusão com o Wellington City em 1985) são um clube só, como na
  contagem de títulos da RSSSF ("Wellington United 3", com 1976 e 1981);
- University-Mount Wellington (fusão do Mount Wellington com a Auckland University em 2000) entra como Mount Wellington, como
  na contagem da RSSSF ("Uni - Mt Wellington 6, includes Mt Wellington");
- Trans Tours United (1977) é o Christchurch United com nome de patrocinador; Courier Rangers (1978-1979) é o Rangers de
  Christchurch ("Christchurch Rangers", porque "Rangers" é o da Escócia);
- Otago United (2004-2012) mudou de nome para Southern United em 2013: um clube só, "Southern United";
- Waikato FC (2004-2013), WaiBOP United (2014-2015) e Hamilton Wanderers (2016 em diante) são franquias diferentes, uma no
  lugar da outra: três clubes;
- Waitakere City (clube, até 2003) e Waitakere United (franquia, 2004 em diante) são dois clubes, como na RSSSF;
- Christchurch City (2000-2001) é a fusão de Woolston e Christchurch Technical: outro clube; Cashmere Technical (2022 em
  diante) é outra fusão (Cashmere Wanderers e Christchurch Technical, 2014): outro clube;
- o time reserva do Wellington Phoenix ("Wellington Phoenix", "Wellington Phoenix U-20") é "Wellington Phoenix Reserves", e
  o do Auckland FC (2025) é "Auckland FC Reserves" (os times principais jogam a A-League, com o agente da Ásia);
- Wanderers SC (2013/14 e 2014/15) é o time sub-20 da federação.

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
```

## 8. O que não deu para coletar

- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1970s, 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Fase nacional de 1994 sem jogos (28): a RSSSF e a Wikipédia só têm a tabela.
- Autores dos gols só de 1993-2007/08 (parte); de 2008/09 em diante só a página de cada jogo do ogol tem (não baixada).
- Ligas regionais de 2023-2025 com divergências entre as fontes (Wikipédia, ogol e RSSSF): explicadas na conferência; a Central League 2025 tem 89 dos 90 jogos.
- Artilheiros: não coletados (a RSSSF lista só em algumas temporadas; a Wikipédia tem nas temporadas recentes).
- Datas: sem data em 1970-1995 (matrizes) e nas ligas regionais de 2022-2024 (matriz da Wikipédia).

## 10. Arquivos e comandos

Código em `coleta/nzl-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga neozelandesa (2004/05 a 2025) para data/cache/ogol-nzl-1/ e grava o resumo dos jogos |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da Nova Zelândia para data/coleta/nzl-1/rsssf/ (lista de campeões, histórico e uma página |
| `baixar_wikipedia.py` | Baixa o wikitexto das páginas da Wikipédia em inglês das temporadas da liga neozelandesa para data/coleta/nzl-1/wikipedia/. |
| `clubes_nzl.py` | Identidade dos clubes da Nova Zelândia (nzl-1): cada grafia da RSSSF e do ogol vira um clube, com cidade e região. |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão neozelandesa (nzl-1): uma por título, como na lista de campeões nacionais da RSSSF (nzchamp.html), |
| `explicacoes.py` | Correções e decisões da coleta da Nova Zelândia (nzl-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão neozelandesa e grava o pacote em data/coleta/nzl-1/pacote/ e o relatório em docs/coleta/nzl-1.md. |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/nzl-1/rsssf/), trecho a trecho (edicoes.py). |
| `wikipedia_nz.py` | Tabelas ("Sports table") e matrizes de resultados ("Sports results") das páginas da Wikipédia em inglês das temporadas |

- Fontes baixadas: `data/coleta/nzl-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-nzl-1/`.
- Pacote: `data/coleta/nzl-1/pacote/`; relatório: `docs/coleta/nzl-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/nzl-1/baixar_ogol.py
python coleta/nzl-1/baixar_rsssf.py
python coleta/nzl-1/baixar_wikipedia.py
python coleta/nzl-1/importar.py
python coleta/nzl-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py nzl-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

