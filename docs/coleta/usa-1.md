# Campeonato Norte-Americano (1ª divisão dos EUA) — coleta de dados

Gerado por `python coleta/usa-1/importar.py`. Pacote em `data/coleta/usa-1/pacote/`.

**Edições:** 63, uma por título, como a lista de campeões da "Division I" da RSSSF (`usachamp.html`). Escopo decidido em 24/11/2026 (o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"): ASL I (1921/22-1932/33, com as meias-temporadas de 1929, 1930 e 1932), as duas ligas de 1967 (United Soccer Association, a da FIFA, e NPSL, a "pirata"), NASL (1968-1984) e MLS (1996-2025). De 1985 a 1995 o país não teve liga de 1ª divisão. A temporada 2026 da MLS entra depois da final (18/12/2026).

**Campeão:** ASL e NASL, o campeão da lista da RSSSF (em geral, o dos playoffs; o vice é o derrotado na final, quando há); MLS, o vencedor da MLS Cup (o título da liga). A Supporters' Shield (melhor campanha da fase regular) é o 1º da classificação logo abaixo do campeão e do vice.

**Fora do pacote:** a ASL II (1933-1983, liga regional e depois de 2º nível), a International Soccer League (1960-1965, torneio de verão com clubes estrangeiros), as ligas de 2º nível de 1985-1995 (APSL, A-League), as temporadas indoor da NASL, o torneio MLS is Back (2020, só o mata-mata; a fase de grupos contou na liga), a US Open Cup, a Leagues Cup e os jogos de exibição (All-Star, amistosos).

**Edições sem jogos (35):** a ASL I, 1967 e a NASL (a RSSSF só tem as tabelas e as finais em texto) e a MLS de 1997 e 1998 (a RSSSF só tem as tabelas e a ESPN começa em 2002).

**Pontuação:** ASL e United Soccer Association (1967), 2 por vitória; NPSL (1967) e NASL, 6 por vitória, 3 por empate (até 1974) e 1 por gol até 3 por jogo; de 1975 a 1984 sem empate (shootout, 1 ponto para quem vence); MLS, 3 por vitória, e de 1996 a 1999 sem empate (shootout, 1 ponto). Nesses anos a classificação é a tabela publicada, sem "ajuste de pontos"; nos jogos, o shootout é empate com pênaltis.

**Fontes:** RSSSF (`data/coleta/usa-1/rsssf/`) e ESPN (liga `usa.1`, 2002 em diante: hora (de Nova York), estádio, público, gols com minuto e cartões; os jogos de 2004 e a fase regular de 2011, 2012 e 2025).

**Clubes:** nomes e identidades no começo de `coleta/usa-1/clubes_usa.py`. Renomeação na mesma cidade é o mesmo clube (MetroStars = New York Red Bulls, Kansas City Wizards = Sporting Kansas City, Dallas Burn = FC Dallas, San Jose Clash = San Jose Earthquakes, Montreal Impact = CF Montréal); mudança de cidade é outro clube; os clubes da NASL com nome de clube da MLS levam "(NASL)" (Seattle Sounders, Portland Timbers, Vancouver Whitecaps, San Jose Earthquakes). Clubes do Canadá com país CAN.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1921/22 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Bethlehem Steel | RSSSF (asli) |
| 1922/23 | 7 | 0 (0) | 0 | 0 | 0 / 0 | J&P Coats | RSSSF (asli) |
| 1923/24 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1924/25 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1925/26 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1926/27 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Bethlehem Steel | RSSSF (asli) |
| 1927/28 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Boston Wonder Workers | RSSSF (asli) |
| 1928/29 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1929 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1929/30 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1930 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Fall River Marksmen | RSSSF (asli) |
| 1931 | 10 | 0 (0) | 0 | 0 | 0 / 0 | New York Giants | RSSSF (asli) |
| 1932 | 7 | 0 (0) | 0 | 0 | 0 / 0 | New Bedford Whalers | RSSSF (asli) |
| 1932/33 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Fall River FC | RSSSF (asli) |
| 1967 USA | 12 | 0 (0) | 0 | 0 | 0 / 0 | Los Angeles Wolves | RSSSF (nasl) |
| 1967 NPSL | 10 | 0 (0) | 0 | 0 | 0 / 0 | Oakland Clippers | RSSSF (nasl) |
| 1968 | 17 | 0 (0) | 0 | 0 | 0 / 0 | Atlanta Chiefs | RSSSF (nasl) |
| 1969 | 5 | 0 (0) | 0 | 0 | 0 / 0 | Kansas City Spurs | RSSSF (nasl) |
| 1970 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Rochester Lancers | RSSSF (nasl) |
| 1971 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Dallas Tornado | RSSSF (nasl) |
| 1972 | 8 | 0 (0) | 0 | 0 | 0 / 0 | New York Cosmos | RSSSF (nasl) |
| 1973 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Philadelphia Atoms | RSSSF (nasl) |
| 1974 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Los Angeles Aztecs | RSSSF (nasl) |
| 1975 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Tampa Bay Rowdies | RSSSF (nasl) |
| 1976 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Toronto Metros-Croatia | RSSSF (nasl) |
| 1977 | 18 | 0 (0) | 0 | 0 | 0 / 0 | New York Cosmos | RSSSF (nasl) |
| 1978 | 24 | 0 (0) | 0 | 0 | 0 / 0 | New York Cosmos | RSSSF (nasl) |
| 1979 | 24 | 0 (0) | 0 | 0 | 0 / 0 | Vancouver Whitecaps (NASL) | RSSSF (nasl) |
| 1980 | 24 | 0 (0) | 0 | 0 | 0 / 0 | New York Cosmos | RSSSF (nasl) |
| 1981 | 21 | 0 (0) | 0 | 0 | 0 / 0 | Chicago Sting | RSSSF (nasl) |
| 1982 | 14 | 0 (0) | 0 | 0 | 0 / 0 | New York Cosmos | RSSSF (nasl) |
| 1983 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Tulsa Roughnecks | RSSSF (nasl) |
| 1984 | 9 | 0 (0) | 0 | 0 | 0 / 0 | Chicago Sting | RSSSF (nasl) |
| 1996 | 10 | 177 (177) | 592 | 570 | 2 / 0 | DC United | RSSSF (usa96) |
| 1997 | 10 | 0 (0) | 0 | 0 | 0 / 0 | DC United | RSSSF (usa97) |
| 1998 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Chicago Fire | RSSSF (usa98) |
| 1999 | 12 | 208 (208) | 598 | 2 | 0 / 0 | DC United | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 | 12 | 210 (210) | 660 | 147 | 3 / 0 | Sporting Kansas City | RSSSF (usa00) |
| 2001 | 12 | 186 (186) | 567 | 0 | 3 / 0 | San Jose Earthquakes | RSSSF (usa01) |
| 2002 | 10 | 157 (157) | 472 | 0 | 0 / 0 | Los Angeles Galaxy | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 | 10 | 161 (161) | 466 | 457 | 2 / 0 | San Jose Earthquakes | RSSSF (usa03) |
| 2004 | 10 | 159 (159) | 413 | 405 | 1 / 1 | DC United | RSSSF (usa04) |
| 2005 | 12 | 203 (203) | 574 | 574 | 2 / 0 | Los Angeles Galaxy | RSSSF (usa05) |
| 2006 | 12 | 203 (203) | 530 | 439 | 2 / 0 | Houston Dynamo | RSSSF (usa06) |
| 2007 | 13 | 206 (206) | 537 | 500 | 2 / 0 | Houston Dynamo | RSSSF (usa07) |
| 2008 | 14 | 222 (222) | 616 | 609 | 2 / 0 | Columbus Crew | RSSSF (usa08) |
| 2009 | 15 | 236 (236) | 592 | 590 | 2 / 0 | Real Salt Lake | RSSSF (usa09) |
| 2010 | 16 | 251 (251) | 616 | 616 | 2 / 0 | Colorado Rapids | RSSSF (usa2010) |
| 2011 | 18 | 319 (319) | 818 | 817 | 2 / 0 | Los Angeles Galaxy | RSSSF (usa2011) |
| 2012 | 19 | 338 (338) | 888 | 873 | 2 / 0 | Los Angeles Galaxy | RSSSF (usa2012) |
| 2013 | 19 | 338 (338) | 887 | 881 | 2 / 0 | Sporting Kansas City | RSSSF (usa2013) |
| 2014 | 19 | 338 (338) | 966 | 949 | 2 / 0 | Los Angeles Galaxy | RSSSF (usa2014) |
| 2015 | 20 | 357 (357) | 983 | 957 | 2 / 0 | Portland Timbers | RSSSF (usa2015) |
| 2016 | 20 | 357 (357) | 1006 | 997 | 2 / 0 | Seattle Sounders | RSSSF (usa2016) |
| 2017 | 22 | 391 (391) | 1144 | 1142 | 2 / 0 | Toronto FC | RSSSF (usa2017) |
| 2018 | 23 | 408 (408) | 1299 | 1281 | 2 / 0 | Atlanta United | RSSSF (usa2018) |
| 2019 | 24 | 421 (421) | 1294 | 1290 | 2 / 0 | Seattle Sounders | RSSSF (usa2019) |
| 2020 | 26 | 309 (309) | 885 | 868 | 2 / 0 | Columbus Crew | RSSSF (usa2020) |
| 2021 | 27 | 472 (472) | 1313 | 1305 | 2 / 0 | New York City FC | RSSSF (usa2021) |
| 2022 | 28 | 490 (490) | 1450 | 1438 | 2 / 0 | Los Angeles FC | RSSSF (usa2022) |
| 2023 | 29 | 528 (528) | 1437 | 1416 | 2 / 0 | Columbus Crew | RSSSF (usa2023) |
| 2024 | 29 | 523 (523) | 1626 | 1604 | 2 / 0 | Los Angeles Galaxy | RSSSF (usa2024) |
| 2025 | 30 | 540 (540) | 1629 | 1600 | 2 / 0 | Inter Miami | RSSSF (usa2025) |

## Conferência e correções, edição a edição

### 1921/22

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1922/23

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1923/24

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1924/25

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1925/26

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1926/27

- só a tabela: a RSSSF não tem os jogos da ASL I

### 1927/28

- só a tabela: a RSSSF não tem os jogos da ASL I; dois turnos; o campeão saiu dos playoffs entre os primeiros (Boston Wonder Workers 4-2 New Bedford Whalers)

### 1928/29

- só a tabela: a RSSSF não tem os jogos da ASL I; dois turnos; a classificação é por aproveitamento

### 1929

- só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de outono, suspensa em 9/10/1929 com o fim da "soccer war" (a ASL se juntou à Eastern Soccer League)

### 1929/30

- só a tabela: a RSSSF não tem os jogos da ASL I; disputada como Atlantic Coast League (a ASL e a Eastern Soccer League juntas)

### 1930

- só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de outono

### 1931

- só a tabela: a RSSSF não tem os jogos da ASL I; primavera e outono de 1931; a lista de campeões da RSSSF a chama de 1930-31; final: New York Giants x New Bedford Whalers (8-3 e 6-0)

### 1932

- só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de primavera, talvez incompleta ("may be an incomplete set of standings", RSSSF); sem gols na tabela

### 1932/33

- só a tabela: a RSSSF não tem os jogos da ASL I; só o 1º turno (outono de 1932) tem tabela; a liga foi refeita no verão de 1933 como a ASL II

### 1967 USA

- liga da FIFA; os times eram clubes europeus e sul-americanos com nome de cidade americana; só a tabela e a final (Los Angeles Wolves 6-5 Washington Whips, prorrogação)

### 1967 NPSL

- liga sem reconhecimento da FIFA ("pirata"); só a tabela e a final (Oakland Clippers x Baltimore Bays, 0-1 e 4-1)

### 1968

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1969

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1970

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1971

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1972

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1973

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1974

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1975

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1976

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1977

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1978

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1979

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1980

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1981

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1982

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1983

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1984

- só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto)

### 1996

- linha lida como jogo e descartada (clube não reconhecido): usa96:616 «DC United defeated MetroStars x (SO), 1-0, 2-1»
- linha lida como jogo e descartada (clube não reconhecido): usa96:665 «Los Angeles defeated Kansas City 2-1 x (SO)»

### 1997

- só a tabela: a RSSSF não tem os jogos deste ano e a ESPN começa em 2002

### 1998

- só a tabela: a RSSSF não tem os jogos deste ano e a ESPN começa em 2002

### 1999

- sem ocorrências

### 2000

- sem ocorrências

### 2001

- não jogado — Colorado Rapids Columbus Crew (2001-09-12)
- não jogado — DC United FC Dallas (2001-09-12)
- não jogado — New York Red Bulls Miami Fusion (2001-09-12)
- não jogado — Los Angeles Galaxy San Jose Earthquakes (2001-09-12)
- não jogado — New England Revolution New York Red Bulls (2001-09-15)
- não jogado — DC United Miami Fusion (2001-09-15)
- não jogado — Columbus Crew Tampa Bay Mutiny (2001-09-15)
- não jogado — FC Dallas Chicago Fire (2001-09-15)
- não jogado — Sporting Kansas City Colorado Rapids (2001-09-16)
- não jogado — San Jose Earthquakes Los Angeles Galaxy (2001-09-16)

### 2002

- ESPN: 108 jogos casados

### 2003

- ESPN: 159 jogos casados

### 2004

- jogos da ESPN (a página da RSSSF só tem as tabelas)
- ESPN: 159 jogos casados
- tabela publicada x jogos — usa04:29: DC United tabela [30, 11, 9, 10, 43, 42] jogos [29, 10, 9, 10, 42, 42] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — usa04:29: New York Red Bulls tabela [30, 11, 7, 12, 47, 49] jogos [29, 11, 7, 11, 47, 48] — faltam 1 jogo(s) do clube na página
- linha lida como jogo e descartada (clube não reconhecido): espn:152312 «East All-Stars x West All-Stars»

### 2005

- ESPN: 203 jogos casados
- linha lida como jogo e descartada (clube não reconhecido): usa05:648 «MLS All-Stars x Fulham FC»

### 2006

- ESPN: 202 jogos casados

### 2007

- ESPN: 204 jogos casados

### 2008

- ESPN: 220 jogos casados
- abandonado/suspenso, sem valer — DC United Houston Dynamo (2008-06-04): abandoned at 0-0 in 16'

### 2009

- ESPN: 235 jogos casados

### 2010

- ESPN: 251 jogos casados

### 2011

- fase regular da ESPN (a página da RSSSF só tem as tabelas)
- ESPN: 318 jogos casados
- linha lida como jogo e descartada (clube não reconhecido): espn:326602 «MLS All-Stars x Manchester United»

### 2012

- fase regular da ESPN (a página da RSSSF só tem as tabelas)
- ESPN: 337 jogos casados
- linha lida como jogo e descartada (clube não reconhecido): espn:349922 «MLS All-Stars x Chelsea»

### 2013

- ESPN: 336 jogos casados

### 2014

- ESPN: 334 jogos casados

### 2015

- ESPN: 352 jogos casados

### 2016

- ESPN: 355 jogos casados

### 2017

- ESPN: 389 jogos casados

### 2018

- ESPN: 403 jogos casados

### 2019

- ESPN: 420 jogos casados

### 2020

- a temporada parou em março (pandemia) e voltou com o torneio MLS is Back (Flórida, julho e agosto), cuja fase de grupos contou para a fase regular; o mata-mata do torneio não é da liga e fica fora; a classificação foi por pontos por jogo, e 7 jogos do Oeste não foram disputados
- ESPN: 307 jogos casados
- tabela usa2020:107 fora da conferência: tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)
- tabela usa2020:124 fora da conferência: tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)

### 2021

- ESPN: 471 jogos casados

### 2022

- ESPN: 488 jogos casados
- abandonado/suspenso, sem valer — Charlotte FC Columbus Crew (2022-07-30): abandoned at 0-0 in 16' due to

### 2023

- ESPN: 514 jogos casados
- abandonado/suspenso, sem valer — FC Dallas St. Louis City SC (2023-05-06): abandoned at 0-0 in 50' due to lightning
- abandonado/suspenso, sem valer — Colorado Rapids Portland Timbers (2023-07-04): abandoned at 0-0 at half-time due to
- não jogado — FC Cincinnati New York Red Bulls (2023-11-11)
- não jogado — Philadelphia Union New England Revolution (2023-11-12)
- não jogado — Orlando City Nashville SC (2023-11-12)
- não jogado — Los Angeles FC Vancouver Whitecaps (2023-11-09)
- não jogado — St. Louis City SC Sporting Kansas City (2023-11-11)

### 2024

- ESPN: 521 jogos casados
- abandonado/suspenso, sem valer — Philadelphia Union Seattle Sounders (2024-03-09): abandoned at 0-0 in 6' due to

### 2025

- fase regular da ESPN (a página da RSSSF só tem as tabelas)
- ESPN: 537 jogos casados
- linha lida como jogo e descartada (clube não reconhecido): espn:735090 «MLS All-Stars x Liga MX All-Stars»

