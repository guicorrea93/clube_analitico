# Campeonato Inglês (`eng-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/eng-1/pacote/` e do importador `coleta/eng-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/eng-1.md`.

## 1. O que temos

- **Edições:** 127, de 1888/89 a 2025/26.
- **Jogos:** 51330; **gols:** 152539; **gols com autor:** 25878 (17%); **cartões:** 33166; **jogos com estatísticas** (chutes, faltas, escanteios): 9880.
- **Clubes:** 65; **artilheiros:** 127 temporadas com artilheiro (145 linhas, com empates).
- **Classificação final:** 127 temporadas; **rodada a rodada:** 33 temporadas.
- **Tabelas publicadas guardadas para conferência:** 4654 linhas, de 227 tabelas.
- **Observação da competição:** 1ª divisão inglesa desde a criação da Football League (1888/89): Football League (1888/89-1891/92), First Division (1892/93-1991/92) e Premier League (1992/93 em diante). Sem 1915/16-1918/19 e 1939/40-1945/46 (guerras; 1939/40 foi anulada na 3ª rodada). Não inclui os test matches (1892/93-1897/98) nem os play-offs de 1986/87-1987/88, que eram jogos contra clubes da 2ª divisão.

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1888/89-2024/25, menos 2022/23;
- football-data.co.uk: base de 2022/23 e 2025/26; de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time (chutes, faltas, escanteios, cartões; 2000/01+);
- ogol: rodada de cada jogo (só nas temporadas com rodadas fixas: 1992/93, 1993/94 e de 1995/96 em diante) e conferência de placar; calendários guardados em `data/cache/ogol-eng-1/` para os escudos;
- ESPN (liga `eng.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (engpaul/FLA, Paul Felton e Barry Spencer): tabela final publicada até 2006/07 e matriz de resultados (1888/89-1938/39, menos 1925/26) — conferência jogo a jogo;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e lista de artilheiros;
- BDFutbol (1960/61+): árbitro com o nome completo e estádio onde a ESPN não tem; autores dos 12 jogos em que os gols da ESPN não fecham com o placar (ficha de cada jogo).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local de Londres. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 226 tabelas fecham com os jogos e 1 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: 1888/89.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1880s | 264 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1890s | 2366 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1900s | 3430 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 2362 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 4620 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 4158 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1848 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 4620 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 4620 | 100% | 0% | 0% | 100% | 0% | 75% | 0% | 0% | 0.0 |
| 1970s | 4620 | 100% | 0% | 0% | 100% | 0% | 87% | 0% | 0% | 0.0 |
| 1980s | 4414 | 100% | 0% | 0% | 100% | 0% | 86% | 0% | 0% | 0.0 |
| 1990s | 4128 | 100% | 0% | 68% | 100% | 0% | 100% | 0% | 0% | 0.0 |
| 2000s | 3800 | 100% | 90% | 100% | 100% | 90% | 100% | 100% | 90% | 2.9 |
| 2010s | 3800 | 100% | 100% | 100% | 100% | 98% | 100% | 100% | 100% | 3.5 |
| 2020s | 2280 | 100% | 100% | 100% | 100% | 84% | 100% | 100% | 100% | 3.9 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1888/89 a 1890/91: 12 clubes
- 1891/92: 14 clubes
- 1892/93 a 1897/98: 16 clubes
- 1898/99 a 1904/05: 18 clubes
- 1905/06 a 1914/15: 20 clubes
- 1919/20 a 1986/87: 22 clubes
- 1987/88: 21 clubes
- 1988/89 a 1990/91: 20 clubes
- 1991/92 a 1994/95: 22 clubes
- 1995/96 a 2025/26: 20 clubes

**Pontos por vitória:**

- 1888/89 a 1980/81: 2
- 1981/82 a 2025/26: 3

**Nome oficial:**

- 1888/89 a 1891/92: Football League
- 1892/93 a 1991/92: Football League First Division
- 1992/93 a 2006/07: FA Premier League
- 2007/08 a 2025/26: Premier League

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, média de gols (goal average): 77 temporadas
- pontos, saldo de gols, gols pró: 50 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1890/91: punições: Sunderland -2 pontos
- 1990/91: punições: Arsenal -2 pontos; Manchester United -1 pontos
- 1996/97: punições: Middlesbrough -3 pontos
- 2009/10: punições: Portsmouth -9 pontos
- 2023/24: punições: Everton -8 pontos; Nottingham Forest -4 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Liverpool: 20
- Manchester United: 20
- Arsenal: 14
- Manchester City: 10
- Everton: 9
- Aston Villa: 7
- Sunderland: 6
- Chelsea: 6
- Sheffield Wednesday: 4
- Newcastle: 4
- Blackburn: 3
- Huddersfield: 3
- Wolverhampton: 3
- Leeds: 3
- Preston: 2
- Burnley: 2
- Portsmouth: 2
- Tottenham: 2
- Derby County: 2
- Sheffield United: 1
- West Bromwich: 1
- Ipswich: 1
- Nottingham Forest: 1
- Leicester: 1

**Rebaixamentos:** 292 no total; quem mais caiu: Leicester (13), Birmingham (12), West Bromwich (11), Burnley (10), Bolton (10).

**Punições em pontos:**

- 1890/91: Sunderland -2
- 1990/91: Arsenal -2
- 1990/91: Manchester United -1
- 1996/97: Middlesbrough -3
- 2009/10: Portsmouth -9
- 2023/24: Everton -8
- 2023/24: Nottingham Forest -4

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/eng-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1888/89 · Wolverhampton Wanderers · Everton:** [5, 0] três jornais da época trazem 5-0 (Cricket and Football Field, Liverpool Courier e Athletic News, transcritos em bluecorrespondent.co.uk/1888-89/january1889.html); também o ogol, o 11v11, a página da temporada do Wolverhampton na Wikipédia e a tabela final da Wikipédia (Wolverhampton 51 gols pró, Everton 47 contra). O 4-0 vem da RSSSF e de quem a copia (um gol de Knight foi anulado por impedimento)

### Datas corrigidas (`DATAS`)

- **1953/54 · Sheffield Wednesday · Aston Villa:** 1953-11-07
- **1895/96 · Burnley · Sheffield United:** 1896-02-04
- **1899/00 · Preston North End · Nottingham Forest:** 1899-12-30
- **1899/00 · Aston Villa · Sunderland:** 1899-12-30
- **1899/00 · Manchester City · Blackburn Rovers:** 1899-12-30
- **1899/00 · Newcastle United · West Bromwich Albion:** 1899-12-30
- **1899/00 · Burnley · Glossop North End:** 1899-12-30
- **1899/00 · Notts County · Derby County:** 1899-12-30
- **1899/00 · Sheffield United · Everton:** 1899-12-30
- **1899/00 · Wolverhampton Wanderers · Bury:** 1899-12-30
- **1899/00 · Liverpool · Stoke City:** 1899-12-30
- **1934/35 · Blackburn Rovers · Chelsea:** 1934-11-17
- **1936/37 · West Bromwich Albion · Bolton Wanderers:** 1936-11-14
- **1936/37 · Derby County · Brentford:** 1936-10-03
- **1938/39 · Charlton Athletic · Arsenal:** 1938-12-27
- **1938/39 · Leicester City · Portsmouth:** 1938-11-12
- **1993/94 · Ipswich Town · Sheffield United:** 1994-02-22
- **1993/94 · Newcastle United · Ipswich Town:** 1994-03-23
- **1993/94 · Wimbledon · Leeds United:** 1994-03-26
- **1994/95 · Blackburn Rovers · Crystal Palace:** 1995-04-20
- **1994/95 · Everton · Leeds United:** 1994-12-05
- **1995/96 · West Ham United · Manchester United:** 1996-01-22
- **1995/96 · Everton · Aston Villa:** 1996-05-05
- **1995/96 · Chelsea · Blackburn Rovers:** 1996-05-05
- **1995/96 · Arsenal · Bolton Wanderers:** 1996-05-05
- **1995/96 · Nottingham Forest · Queens Park Rangers:** 1996-05-05
- **1995/96 · West Ham United · Sheffield Wednesday:** 1996-05-05
- **1995/96 · Manchester City · Liverpool:** 1996-05-05
- **1995/96 · Newcastle United · Tottenham Hotspur:** 1996-05-05
- **1995/96 · Middlesbrough · Manchester United:** 1996-05-05
- **1995/96 · Coventry City · Leeds United:** 1996-05-05
- **1995/96 · Southampton · Wimbledon:** 1996-05-05
- **1998/99 · Manchester United · Derby County:** 1999-02-03
- **2015/16 · Manchester United · AFC Bournemouth:** 2016-05-17

### Gols de artilheiro corrigidos (`GOLS_ARTILHEIRO`)

- **1937/38 · Tommy Lawton:** [28] a página da temporada 1937-38 da liga e a do Everton e a ficha de Lawton na Wikipédia dão 28 na liga (a RSSSF traz 38, erro de digitação)
- **1889/90 · Jimmy Ross:** [24] a RSSSF (engtops) e a página da temporada 1889-90 da liga na Wikipédia dão 24

### Não reeleitos (sem rebaixamento na época) (`NAO_REELEITOS`)

- **1889/90 · Stoke City:** não foi reeleito para a Football League (foi para a Football Alliance); não havia rebaixamento
- **1891/92 · Darwen:** não foi reeleito para a 1ª divisão e foi posto na nova 2ª divisão; não havia rebaixamento

### Autores dos gols pela ficha do BDFutbol (a ESPN não fecha) (`GOLS_MANUAIS`)

- **2002/03 · West Bromwich Albion · Southampton:** [[('m', 'Sean Gregan', 80, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=610818
- **2002/03 · Sunderland · Charlton Athletic:** [[('v', 'Stephen Wright', 24, 'contra'), ('v', 'Michael Proctor', 29, 'contra'), ('v', 'Michael Proctor', 32, 'contra'), ('m', 'Kevin Phillips', 81, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=611018
- **2002/03 · Fulham · Aston Villa:** [[('v', 'Gareth Barry', 3, 'normal'), ('m', 'Steed Malbranque', 14, 'normal'), ('m', 'Jon Harley', 36, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=611026
- **2003/04 · Leeds United · Manchester City:** [[('m', 'Stephen McPhail', 23, 'normal'), ('v', 'Nicolas Anelka', 44, 'normal'), ('m', 'Mark Viduka', 76, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=611432
- **2004/05 · Tottenham Hotspur · Charlton Athletic:** [[('v', 'Shaun Bartlett', 17, 'normal'), ('v', 'Shaun Bartlett', 39, 'normal'), ('v', 'Jerome Thomas', 50, 'normal'), ('m', 'Robbie Keane', 69, 'normal'), ('m', 'Jermain Defoe', 79, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=611643
- **2006/07 · West Ham United · Wigan Athletic:** [[('v', 'David Cotterill', 51, 'normal'), ('v', 'Jonathan Spector', 58, 'contra')]] https://www.bdfutbol.com/es/p/p.php?id=612435
- **2010/11 · Everton · West Bromwich Albion:** [[('v', 'Paul Scharner', 16, 'normal'), ('v', 'Chris Brunt', 26, 'normal'), ('m', 'Tim Cahill', 42, 'normal'), ('v', 'Somen Tchoyi', 76, 'normal'), ('v', 'Youssuf Mulumbu', 87, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=613952
- **2011/12 · Everton · West Bromwich Albion:** [[('m', 'Leon Osman', 18, 'normal'), ('m', 'Victor Anichebe', 68, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=614493
- **2013/14 · Manchester City · Manchester United:** [[('m', 'Sergio Agüero', 16, 'normal'), ('m', 'Yaya Touré', 45, 'normal'), ('m', 'Sergio Agüero', 47, 'normal'), ('m', 'Samir Nasri', 50, 'normal'), ('v', 'Wayne Rooney', 87, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=614998
- **2014/15 · Manchester City · Manchester United:** [[('m', 'Sergio Agüero', 63, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=618794
- **2016/17 · Liverpool · West Ham United:** [[('m', 'Adam Lallana', 5, 'normal'), ('v', 'Dimitri Payet', 27, 'normal'), ('v', 'Michail Antonio', 39, 'normal'), ('m', 'Divock Origi', 48, 'normal')]] https://www.bdfutbol.com/es/p/p.php?id=619637
- **2016/17 · Stoke City · Everton:** [[('m', 'Peter Crouch', 7, 'normal'), ('v', 'Ryan Shawcross', 39, 'contra')]] https://www.bdfutbol.com/es/p/p.php?id=619717

### Artilheiros com divergência entre fontes anotada (`NOTA_ARTILHEIRO`)

- **1905/06 · Albert Shepherd:** a RSSSF (engtops) e a página da temporada 1905-06 da liga dão Walter White (Bolton) com 26; a biografia de Shepherd dá 25. Fica a lista da Wikipédia (decisão D-17 c)

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1888/89:** Wolverhampton x Everton (26/01/1889) fica 5-0 (ver a correção abaixo); a matriz e a tabela da RSSSF, feitas com 4-0, ficam com 1 gol a menos para o Wolverhampton e para o Everton
- **1900/01:** a matriz da RSSSF traz Newcastle 4-0 Sheffield United; a tabela da RSSSF e a da Wikipédia fecham com o 3-0 da base: erro de digitação da matriz
- **1903/04:** a matriz da RSSSF troca os placares de Stoke x West Bromwich (5-0) e Stoke x Wolverhampton (5-1); as tabelas da RSSSF e da Wikipédia fecham com a base: erro da matriz
- **1907/08:** a RSSSF põe Arsenal e Blackburn empatados em 14º ('14='), com os mesmos pontos e a mesma média de gols; a Wikipédia ordena Arsenal 14º e Blackburn 15º. Fica a ordem da Wikipédia
- **1956/57:** Birmingham e Chelsea terminaram com 39 pontos e média de gols igual (69/69 e 73/73 = 1,000); a ordem oficial (RSSSF e Wikipédia) põe o Birmingham em 12º; o critério calculado aqui (gols pró) poria o Chelsea
- **1909/10:** a matriz da RSSSF traz Bolton 0-1 Sheffield Wednesday; as tabelas da RSSSF e da Wikipédia fecham com o 0-2 da base: erro da matriz

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. O ogol tem a ficha de muitos jogos, mas seriam uns 40 mil pedidos; fica como próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** idem.
- **Test matches (1892/93-1897/98) e play-offs (1986/87-1987/88):** jogos entre clubes da 1ª e da 2ª divisão, que decidiam o rebaixamento; ficam de fora (entram quando a 2ª divisão for coletada).
- **Rodadas antes de 1992/93 (e em 1994/95):** a liga inglesa não tinha rodadas fixas, e o número de rodada do ogol junta jogos de datas diferentes (clubes com 2 ou 3 jogos na mesma rodada). Nessas 94 temporadas a rodada fica vazia e não há tabela rodada a rodada; a ordem dos jogos é a das datas.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Nomes de jogadores da ESPN em formato de documento (sobrenomes na frente, ex.: "Goncalves da Silva Ailton"): os casos mais frequentes estão em coleta/comum-europa/nomes_jogadores.py, aplicado em todas as ligas; a varredura completa dos ~2 mil nomes com 3 palavras ou mais, nas 8 ligas, fica pendente (conferir com o BDFutbol ou a Wikipédia).
- Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).

## 10. Arquivos

- Código: `coleta/eng-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_eng.py`.
- Fontes baixadas: `data/coleta/eng-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-eng-1/`.
- Pacote: `data/coleta/eng-1/pacote/`; relatório: `docs/coleta/eng-1.md`.
- Refazer do zero: `python coleta/eng-1/baixar.py ...` (ver o docstring), `python coleta/eng-1/importar.py`, `python coleta/comum-europa/testar_carga.py eng-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

