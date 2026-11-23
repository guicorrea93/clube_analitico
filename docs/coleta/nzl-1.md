# Coleta: Campeonato Neozelandês (`nzl-1`)

Gerado por `python coleta/nzl-1/importar.py`. Pacote em `data/coleta/nzl-1/pacote/`.

## Resumo

- 55 edições (1970-2025), 7480 jogos, 26352 gols, 2888 com autor.
- Escopo aprovado pelo Guilherme em 23/11/2026: começa em 1970 (1ª liga nacional); desde 1993 o campeão é o da final, com o 1º da fase de liga na observação; 2004 (finais canceladas) e 2021 (só a South Central Series) ficam de fora; as ligas regionais que classificam para a fase nacional (1993-1995, 1999, 2022-2025) entram como 1ª fase; o time reserva do Wellington Phoenix (e o do Auckland FC em 2025) leva "Reserves" no nome.
- Classificação final: a tabela da fase de liga (ou nacional) na ordem oficial, com campeão e vice no topo; os clubes que caíram na fase regional vêm depois, pela posição no grupo, com a campanha da fase regional.

## Fontes

- **RSSSF** (`data/coleta/nzl-1/rsssf/`, baixadas por `baixar_rsssf.py`): lista de campeões (`nzchamp.html`) e uma página por temporada. 1970-1992: tabela e matriz de resultados (sem data); 1993-1995: ligas regionais (matriz) e fase nacional (rodadas, com autores; 1994 só a tabela); 1996-2007/08: rodadas com data e autores; 2008/09 em diante: rodadas com data, sem autores; 2010/11 e 2011/12: só as tabelas e o mata-mata.
- **Wikipédia em inglês** (`data/coleta/nzl-1/wikipedia/`, `baixar_wikipedia.py`): matriz de resultados das ligas regionais de 2022-2025, tabela de 1992 e segunda fonte do campeão (infobox ou status "C" na tabela).
- **ogol** (`data/coleta/nzl-1/ogol/` e cache em `data/cache/ogol-nzl-1/`, `baixar_ogol.py`): calendários de 2008/09 a 2025 (as edições anteriores do ogol só têm o campeão). Entram a fase de liga de 2010/11 e 2011/12, as ligas Central e Southern de 2025 e a data de jogos da RSSSF sem data.
- A ESPN não cobre a Nova Zelândia.

## Correções e decisões

- `nz89`, linha 35: "4-0*2-1" -> "3-0 2-1": Christchurch United x Manurewa: a matriz traz 4-0 com a nota "other sources give Christchurch vs Manurewa as 3-0"; a tabela da página (e a da Wikipédia) conta 3-0 (o asterisco colado também impedia a leitura da matriz).
- `nz00 / 137`: a página põe "Metro 0-4 Manawatu", mas os quatro autores (Patrick, George, Longley, Bernard) são do Miramar Rangers, e assim Manawatu e Miramar ficam com os 18 jogos da tabela.
- `nz97 / 224`: Napier City Rovers 3-2 Waitakere City na página, sem autor dos gols do Waitakere; a tabela da mesma página conta 3-0 (gols do Waitakere e sofridos do Napier 2 a menos).
- `nz78 / 34 / Hamilton / Woolston`: a matriz traz Hamilton 3-3 Woolston, mas a tabela da página (igual à da Wikipédia) dá derrota do Hamilton e vitória do Woolston, com um gol a menos do Hamilton: 2-3 (o outro jogo entre os dois, 0-3, não explica a diferença).
- `nz82 / 38 / Napier City Rovers / Manurewa`: 1-1 em campo; o resultado virou 0-1 para o Manurewa porque o Napier escalou jogador sem registro (Wikipédia, citando Hilton 1991); a tabela da página já conta assim.
- `nz87 / 172 / Mt Maunganui / Christchurch Utd`: a matriz traz 0-1; a lista da 5ª rodada, na mesma página, traz 0-2, e é o que a tabela conta (60 gols do Christchurch United).
- `wikipedia / 2024 / Birkenhead United / Auckland City`: a matriz da Wikipédia traz Birkenhead 3-1 Auckland City; a tabela da RSSSF e a da própria Wikipédia contam vitória do Auckland City por 3-1 (placar invertido na matriz).
- `nz07 / 72`: vitória dada ao Waitakere United sem gols ("awarded 0-0 win"); em campo, 0-1 (o Auckland City escalou jogador irregular).
- 2025 (Southern League): a matriz da Southern League 2025 na Wikipédia tem só 9 dos 10 clubes da tabela (falta o University of Canterbury); entram os jogos do ogol.
- 2025 (Central League): a matriz da Central League 2025 na Wikipédia foi preenchida no começo da temporada ("update=12 April 2025") e não fecha nem com a tabela da própria página: 8 dos 10 clubes divergem.

## Divergências que ficam (erro da própria fonte)

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

## Edição a edição

| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Fontes | Observação |
|---|---|---|---|---|---|---|---|---|---|
| 1970 | pontos corridos (8 clubes) | 56 | 56 | 237 | 0 | Blockhouse Bay | Eastern Suburbs | RSSSF |  |
| 1971 | pontos corridos (10 clubes) | 90 | 90 | 337 | 0 | Eastern Suburbs | Mount Wellington | RSSSF |  |
| 1972 | pontos corridos (10 clubes) | 90 | 90 | 316 | 0 | Mount Wellington | Blockhouse Bay | RSSSF |  |
| 1973 | pontos corridos (10 clubes) | 90 | 90 | 280 | 0 | Christchurch United | Mount Wellington | RSSSF | 2 divergência(s) com a tabela |
| 1974 | pontos corridos (10 clubes) | 90 | 90 | 288 | 0 | Mount Wellington | Christchurch United | RSSSF |  |
| 1975 | pontos corridos (10 clubes) | 90 | 90 | 232 | 0 | Christchurch United | North Shore United | RSSSF |  |
| 1976 | pontos corridos (10 clubes) | 90 | 90 | 285 | 0 | Wellington United | Mount Wellington | RSSSF |  |
| 1977 | pontos corridos (12 clubes) | 132 | 132 | 351 | 0 | North Shore United | Stop Out | RSSSF |  |
| 1978 | pontos corridos (12 clubes) | 132 | 132 | 384 | 0 | Christchurch United | Mount Wellington | RSSSF |  |
| 1979 | pontos corridos (12 clubes) | 132 | 132 | 416 | 0 | Mount Wellington | Christchurch United | RSSSF |  |
| 1980 | pontos corridos (12 clubes) | 132 | 132 | 411 | 0 | Mount Wellington | Gisborne City | RSSSF |  |
| 1981 | pontos corridos (12 clubes) | 132 | 132 | 381 | 0 | Wellington United | Dunedin City | RSSSF |  |
| 1982 | pontos corridos (12 clubes) | 132 | 132 | 381 | 0 | Mount Wellington | North Shore United | RSSSF | 2 divergência(s) com a tabela |
| 1983 | pontos corridos (12 clubes) | 132 | 132 | 377 | 0 | Manurewa | North Shore United | RSSSF |  |
| 1984 | pontos corridos (12 clubes) | 132 | 132 | 426 | 0 | Gisborne City | Papatoetoe | RSSSF |  |
| 1985 | pontos corridos (12 clubes) | 132 | 132 | 438 | 0 | Wellington United | Gisborne City | RSSSF |  |
| 1986 | pontos corridos (12 clubes) | 132 | 132 | 443 | 0 | Mount Wellington | Miramar Rangers | RSSSF |  |
| 1987 | pontos corridos (14 clubes) | 182 | 182 | 592 | 0 | Christchurch United | Gisborne City | RSSSF |  |
| 1988 | pontos corridos (14 clubes) | 182 | 182 | 597 | 0 | Christchurch United | Mount Wellington | RSSSF | 4 divergência(s) com a tabela |
| 1989 | pontos corridos (14 clubes) | 182 | 182 | 583 | 0 | Napier City Rovers | Mount Maunganui | RSSSF |  |
| 1990 | pontos corridos (14 clubes) | 182 | 182 | 535 | 0 | Waitakere City | Mount Wellington | RSSSF | 4 divergência(s) com a tabela |
| 1991 | pontos corridos (14 clubes) | 182 | 182 | 547 | 0 | Christchurch United | Miramar Rangers | RSSSF | 2 divergência(s) com a tabela |
| 1992 | pontos corridos (14 clubes) | 182 | 182 | 574 | 0 | Waitakere City | Waikato United | RSSSF | 7 divergência(s) com a tabela |
| 1993 | ligas regionais (3 grupos, 30 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final | 302 | 302 | 1056 | 105 | Napier City Rovers | Waitakere City | RSSSF | 2 divergência(s) com a tabela |
| 1994 | jogos incompletos: ligas regionais (3 grupos, 30 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final | 274 | 302 | 957 | 0 | North Shore United | Napier City Rovers | RSSSF | a fase nacional só tem a tabela final na RSSSF (os 28 jogos ficam de fora) |
| 1995 | ligas regionais (3 grupos, 31 clubes) + fase nacional (8 clubes) + semifinais + final preliminar + final | 322 | 322 | 1204 | 104 | Waitakere City | Waikato United | RSSSF |  |
| 1996 | fase de liga (10 clubes) + semifinais + final preliminar + final | 94 | 94 | 367 | 10 | Waitakere City | Miramar Rangers | RSSSF |  |
| 1996/97 | fase de liga (10 clubes) + semifinais + final preliminar + final | 94 | 94 | 335 | 328 | Waitakere City | Napier City Rovers | RSSSF |  |
| 1997/98 | fase de liga (11 clubes) + semifinais + final | 112 | 112 | 503 | 0 | Napier City Rovers | Central United | RSSSF |  |
| 1999 | ligas regionais (2 grupos, 20 clubes) + final | 189 | 189 | 796 | 4 | Central United | Dunedin Technical | RSSSF |  |
| 2000 | fase de liga (10 clubes) + semifinais + final | 94 | 94 | 317 | 311 | Napier City Rovers | Mount Wellington | RSSSF |  |
| 2001 | fase de liga (10 clubes) + semifinais + final preliminar + final | 94 | 94 | 374 | 374 | Central United | Miramar Rangers | RSSSF |  |
| 2002 | fase de liga (10 clubes) + semifinais + final preliminar + final | 94 | 94 | 332 | 325 | Miramar Rangers | Napier City Rovers | RSSSF |  |
| 2003 | fase de liga (10 clubes) + semifinais + final preliminar + final | 94 | 94 | 331 | 331 | Miramar Rangers | East Auckland | RSSSF |  |
| 2004/05 | fase de liga (8 clubes) + semifinais + final | 86 | 86 | 286 | 286 | Auckland City | Waitakere United | RSSSF |  |
| 2005/06 | fase de liga (8 clubes) + rodada eliminatória + semifinais + final preliminar + final | 90 | 90 | 326 | 326 | Auckland City | Canterbury United | RSSSF |  |
| 2006/07 | fase de liga (8 clubes) + semifinais + final | 86 | 86 | 301 | 296 | Auckland City | Waitakere United | RSSSF |  |
| 2007/08 | fase de liga (8 clubes) + semifinais + final | 86 | 86 | 275 | 84 | Waitakere United | Team Wellington | RSSSF |  |
| 2008/09 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 193 | 0 | Auckland City | Waitakere United | RSSSF |  |
| 2009/10 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 199 | 0 | Waitakere United | Canterbury United | RSSSF |  |
| 2010/11 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 211 | 0 | Waitakere United | Auckland City | RSSSF + ogol |  |
| 2011/12 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 248 | 0 | Waitakere United | Team Wellington | RSSSF + ogol |  |
| 2012/13 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 258 | 0 | Waitakere United | Auckland City | RSSSF |  |
| 2013/14 | fase de liga (8 clubes) + semifinais + final | 61 | 61 | 234 | 1 | Auckland City | Team Wellington | RSSSF |  |
| 2014/15 | fase de liga (9 clubes) + semifinais + final | 77 | 77 | 282 | 0 | Auckland City | Hawke's Bay United | RSSSF |  |
| 2015/16 | fase de liga (8 clubes) + semifinais + final | 59 | 59 | 236 | 0 | Team Wellington | Auckland City | RSSSF |  |
| 2016/17 | fase de liga (10 clubes) + semifinais + final | 93 | 93 | 337 | 0 | Team Wellington | Auckland City | RSSSF |  |
| 2017/18 | fase de liga (10 clubes) + semifinais + final | 93 | 93 | 321 | 0 | Auckland City | Team Wellington | RSSSF |  |
| 2018/19 | fase de liga (10 clubes) + semifinais + final | 94 | 94 | 353 | 3 | Eastern Suburbs | Team Wellington | RSSSF |  |
| 2019/20 | fase de liga (10 clubes) | 80 | 80 | 303 | 0 | Auckland City | Team Wellington | RSSSF |  |
| 2020/21 | fase de liga (8 clubes) + semifinais + final | 59 | 59 | 208 | 0 | Team Wellington | Auckland City | RSSSF |  |
| 2022 | ligas regionais (3 grupos, 32 clubes) + fase nacional (10 clubes) + final | 358 | 358 | 1435 | 0 | Auckland City | Wellington Olympic | RSSSF + Wikipédia |  |
| 2023 | ligas regionais (3 grupos, 32 clubes) + fase nacional (10 clubes) + final | 358 | 358 | 1468 | 0 | Wellington Olympic | Auckland City | RSSSF + Wikipédia | 15 divergência(s) com a tabela |
| 2024 | ligas regionais (3 grupos, 32 clubes) + fase nacional (10 clubes) + final | 357 | 357 | 1471 | 0 | Auckland City | Birkenhead United | RSSSF + Wikipédia | 6 divergência(s) com a tabela |
| 2025 | jogos incompletos: ligas regionais (3 grupos, 32 clubes) + fase nacional (11 clubes) + final | 367 | 368 | 1424 | 0 | Auckland City | Wellington Olympic | RSSSF + Wikipédia + ogol | 22 divergência(s) com a tabela; Central League e Southern League pelo ogol: falta 1 jogo da Central (Petone x Wellington Phoenix Reserves) e, na Southern, Coastal Spirit e Dunedin City Royals têm um jogo a mais e Nelson Suburbs e Wanaka um a menos do que na tabela da RSSSF |

## O que não deu para coletar

- Fase nacional de 1994 (28 jogos): a RSSSF e a Wikipédia só têm a tabela.
- Autores dos gols de 1970-1992, de 1994, de 1997/98 e de 2008/09 em diante (a RSSSF não traz; o ogol tem só na página de cada jogo).
- Data dos jogos de 1970-1995 (matrizes) e das ligas regionais de 2022-2024 (matriz da Wikipédia).
- Hora, estádio, público e cartões: nenhuma fonte aberta para a liga inteira.
- Artilheiros: a RSSSF lista só em algumas temporadas; fica para depois.
