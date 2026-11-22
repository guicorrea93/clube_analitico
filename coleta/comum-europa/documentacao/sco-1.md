# Campeonato Escocês (`sco-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/sco-1/pacote/` e do importador `coleta/sco-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/sco-1.md`.

## 1. O que temos

- **Edições:** 129, de 1890/91 a 2025/26.
- **Jogos:** 33076; **gols:** 105133; **gols com autor:** 14565 (14%); **cartões:** 19812; **jogos com estatísticas** (chutes, faltas, escanteios): 5876.
- **Clubes:** 46; **artilheiros:** 129 temporadas com artilheiro (140 linhas, com empates).
- **Classificação final:** 129 temporadas; **rodada a rodada:** 93 temporadas.
- **Tabelas publicadas guardadas para conferência:** 3794 linhas, de 257 tabelas.
- **Observação da competição:** 1ª divisão escocesa desde a criação da Scottish Football League (1890/91): Division One (até 1974/75), Premier Division (1975/76-1997/98), Scottish Premier League (1998/99-2012/13) e Scottish Premiership. Sem 1939/40-1945/46 (guerra). O mesmo par se enfrenta 2, 3 ou 4 vezes; desde 2000/01 a liga se divide em dois grupos de 6 depois da 33ª rodada. Não inclui os jogos de desempate pelo título (1890/91, 1904/05) nem os play-offs de rebaixamento contra clubes da 2ª divisão.

## 2. Fontes e regras

**Fontes:**

- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; calendários guardados em `data/cache/ogol-sco-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);
- RSSSF: tabela final de 1890/91 a 1998/99 (scothist.html) e da página de cada temporada depois; lista de campeões e de artilheiros (com o clube);
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;
- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ESPN (liga `sco.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista oficial de rebaixados.

**Regras da importação:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). O mesmo par se enfrenta 2, 3 ou 4 vezes por temporada: as outras fontes são casadas pelo par e pela data mais próxima. Desde 2000/01 a liga se divide em dois grupos de 6 depois da 33ª rodada; na classificação rodada a rodada, o grupo de cima fica nas 6 primeiras posições a partir da 34ª. Gols da ESPN só entram quando a soma bate com o placar. Hora local (Reino Unido). Rebaixado = clube que não está na 1ª divisão na temporada seguinte; até 1920/21 não havia rebaixamento (os últimos pediam reeleição à liga). 2 pontos por vitória até 1993/94, 3 a partir de 1994/95.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 58, saldo de gols em 54, média de gols em 11); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 197 tabelas fecham com os jogos e 60 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1903/04, 1904/05, 1907/08, 1919/20, 1920/21, 1925/26, 1926/27, 1928/29, 1933/34, 1947/48, 1961/62, 1970/71.
- Temporadas com alguma tabela divergente: 1890/91, 1891/92, 1899/00, 1901/02, 1902/03, 1903/04, 1904/05, 1905/06, 1906/07, 1907/08, 1908/09, 1909/10, 1910/11, 1911/12, 1912/13, 1913/14, 1914/15, 1916/17, 1919/20, 1920/21, 1922/23, 1924/25, 1925/26, 1926/27, 1928/29, 1930/31, 1933/34, 1934/35, 1935/36, 1937/38, 1938/39, 1947/48, 1949/50, 1952/53, 1954/55, 1955/56, 1957/58, 1961/62, 1963/64, 1965/66, 1967/68, 1968/69, 1969/70, 1970/71, 1977/78, 1982/83, 1997/98, 2015/16.
- Temporadas com número de jogos diferente do turno e returno completo: 1915/16 (379 de 380), 2019/20 (179 de 132).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1890s | 942 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1900s | 2160 | 100% | 0% | 57% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 3511 | 100% | 0% | 52% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 3964 | 100% | 0% | 77% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 3420 | 100% | 0% | 78% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 960 | 100% | 0% | 50% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 2730 | 100% | 0% | 91% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 3060 | 100% | 0% | 90% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2430 | 100% | 0% | 46% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 1968 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 2052 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 2280 | 100% | 90% | 100% | 90% | 89% | 100% | 100% | 90% | 3.0 |
| 2010s | 2231 | 100% | 100% | 100% | 100% | 100% | 90% | 100% | 99% | 3.7 |
| 2020s | 1368 | 100% | 100% | 100% | 87% | 71% | 100% | 100% | 87% | 3.4 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1890/91: 10 clubes
- 1891/92: 12 clubes
- 1892/93 a 1899/00: 10 clubes
- 1900/01: 11 clubes
- 1901/02: 10 clubes
- 1902/03: 12 clubes
- 1903/04 a 1904/05: 14 clubes
- 1905/06: 16 clubes
- 1906/07 a 1912/13: 18 clubes
- 1913/14 a 1916/17: 20 clubes
- 1917/18 a 1918/19: 18 clubes
- 1919/20 a 1921/22: 22 clubes
- 1922/23 a 1938/39: 20 clubes
- 1946/47 a 1954/55: 16 clubes
- 1955/56 a 1974/75: 18 clubes
- 1975/76 a 1985/86: 10 clubes
- 1986/87 a 1987/88: 12 clubes
- 1988/89 a 1990/91: 10 clubes
- 1991/92 a 1993/94: 12 clubes
- 1994/95 a 1999/00: 10 clubes
- 2000/01 a 2025/26: 12 clubes

**Pontos por vitória:**

- 1890/91 a 1993/94: 2
- 1994/95 a 2025/26: 3

**Nome oficial:**

- 1890/91 a 1892/93: Scottish Football League
- 1893/94 a 1974/75: Scottish Division One
- 1975/76 a 1997/98: Scottish Premier Division
- 1998/99 a 2012/13: Scottish Premier League
- 2013/14 a 2025/26: Scottish Premiership

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto, saldo de gols, gols pró: 58 temporadas
- pontos, saldo de gols, gols pró: 54 temporadas
- pontos, média de gols (goal average): 11 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo de gols, gols pró: 4 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo e gols fora de casa no confronto direto, saldo de gols, gols pró: 2 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1890/91: título dividido: Dumbarton e Rangers; sem rebaixamento: os últimos pediam reeleição à liga; punições: Celtic -4 pontos; Third Lanark -4 pontos; Cowlairs -4 pontos
- 1891/92: sem rebaixamento: os últimos pediam reeleição à liga
- 1892/93: sem rebaixamento: os últimos pediam reeleição à liga
- 1893/94: sem rebaixamento: os últimos pediam reeleição à liga
- 1894/95: sem rebaixamento: os últimos pediam reeleição à liga
- 1895/96: sem rebaixamento: os últimos pediam reeleição à liga
- 1896/97: sem rebaixamento: os últimos pediam reeleição à liga
- 1897/98: sem rebaixamento: os últimos pediam reeleição à liga
- 1898/99: sem rebaixamento: os últimos pediam reeleição à liga
- 1899/00: sem rebaixamento: os últimos pediam reeleição à liga
- 1900/01: sem rebaixamento: os últimos pediam reeleição à liga
- 1901/02: sem rebaixamento: os últimos pediam reeleição à liga
- 1902/03: sem rebaixamento: os últimos pediam reeleição à liga
- 1903/04: sem rebaixamento: os últimos pediam reeleição à liga
- 1904/05: sem rebaixamento: os últimos pediam reeleição à liga
- 1905/06: sem rebaixamento: os últimos pediam reeleição à liga
- 1906/07: sem rebaixamento: os últimos pediam reeleição à liga
- 1907/08: sem rebaixamento: os últimos pediam reeleição à liga
- 1908/09: sem rebaixamento: os últimos pediam reeleição à liga
- 1909/10: sem rebaixamento: os últimos pediam reeleição à liga
- 1910/11: sem rebaixamento: os últimos pediam reeleição à liga
- 1911/12: sem rebaixamento: os últimos pediam reeleição à liga
- 1912/13: sem rebaixamento: os últimos pediam reeleição à liga
- 1913/14: sem rebaixamento: os últimos pediam reeleição à liga
- 1914/15: sem rebaixamento: os últimos pediam reeleição à liga
- 1915/16: sem rebaixamento: os últimos pediam reeleição à liga
- 1916/17: sem rebaixamento: os últimos pediam reeleição à liga
- 1917/18: sem rebaixamento: os últimos pediam reeleição à liga
- 1918/19: sem rebaixamento: os últimos pediam reeleição à liga
- 1919/20: sem rebaixamento: os últimos pediam reeleição à liga
- 1920/21: sem rebaixamento: os últimos pediam reeleição à liga; punições: Celtic -6 pontos
- 1997/98: punições: Dunfermline -1 pontos
- 2007/08: punições: Gretna -10 pontos
- 2011/12: punições: Rangers -10 pontos
- 2013/14: punições: Hearts -15 pontos
- 2015/16: punições: Dundee United -3 pontos
- 2019/20: temporada interrompida em março de 2020 pela pandemia de covid-19, depois de 30 rodadas; a classificação final é pela média de pontos por jogo (Celtic campeão, Hearts rebaixado)

## 6. Campeões, rebaixados e punições

**Títulos:**

- Celtic: 56
- Rangers: 54
- Hearts: 4
- Hibernian: 4
- Aberdeen: 4
- Dumbarton: 2
- Third Lanark: 1
- Motherwell: 1
- Dundee: 1
- Kilmarnock: 1
- Dundee United: 1

**Rebaixamentos:** 172 no total; quem mais caiu: Greenock Morton (10), Dunfermline (10), Falkirk (9), Dundee (9), St Johnstone (8).

**Punições em pontos:**

- 1890/91: Celtic -4
- 1890/91: Third Lanark -4
- 1890/91: Cowlairs -4
- 1920/21: Celtic -6
- 1997/98: Dunfermline -1
- 2007/08: Gretna -10
- 2011/12: Rangers -10
- 2013/14: Hearts -15
- 2015/16: Dundee United -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/sco-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1950/51 · Airdrieonians · Falkirk · 1951-04-28:** [11, 1] o ogol e a matriz da Wikipédia trazem 1-1; as tabelas da RSSSF e da Wikipédia só fecham com 11-1, e o Falkirk registra o 1-11 como a maior derrota da sua história na liga (fitbastats.com/falkirk, recordes do clube)

### Resultados decididos fora de campo (`TRIBUNAL`)

- **1996/97 · Aberdeen · Dunfermline · 1996-09-28:** [3, 0] derrota administrativa do Dunfermline, 3-0 (ficha do ogol); o football-data traz o mesmo 3-0

### Jogos que faltavam na base e foram acrescentados (`ACRESCIMOS`)

- **2015/16 · St Johnstone · Hamilton Academical:** [2016-01-16, 0, 0] falta no calendário do ogol; o football-data, o engsoccerdata e a ESPN trazem 0-0 em 16/01/2016

### Temporadas interrompidas (`INTERROMPIDAS`)

- **2019/20:** interrompida em março de 2020 pela pandemia de covid-19, depois de 30 rodadas; a classificação final é pela média de pontos por jogo (Celtic campeão, Hearts rebaixado)

### Temporadas sem rebaixamento (`SEM_REBAIXAMENTO`)

- 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1915/16:** um jogo da temporada não foi disputado (379 de 380); as tabelas da RSSSF e da Wikipédia fecham com os 379
- **1988/89:** a caixa de resumo da Wikipédia não lista rebaixados; o Hamilton Academical, último, não está em 1989/90
- **1989/90:** a caixa de resumo da Wikipédia não lista rebaixados; o Dundee, último, não está em 1990/91
- **1995/96:** o Partick Thistle perdeu o play-off de rebaixamento e caiu; a caixa da Wikipédia lista só o Falkirk

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.
- **Público e estádio antes da ESPN:** nenhuma fonte em lote.
- **Play-offs de rebaixamento (contra clubes da 2ª divisão) e jogos de desempate pelo título (1890/91, 1904/05):** ficam de fora.
- **Ligas de guerra (1939/40-1945/46):** não oficiais; ficam de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Autores dos gols e cartões antes da ESPN (2001/02): jogo a jogo (ficha do ogol).
- Rodada vazia até os anos 1930 em várias temporadas: não havia rodadas fixas (como no Inglês) e o ogol não traz.
- Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; a revisão pode conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).

## 10. Arquivos

- Código: `coleta/sco-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_sco.py`.
- Fontes baixadas: `data/coleta/sco-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-sco-1/`.
- Pacote: `data/coleta/sco-1/pacote/`; relatório: `docs/coleta/sco-1.md`.
- Refazer do zero: `python coleta/sco-1/baixar.py ...` (ver o docstring), `python coleta/sco-1/importar.py`, `python coleta/comum-europa/testar_carga.py sco-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

