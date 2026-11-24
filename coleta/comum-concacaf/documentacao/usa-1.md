# Campeonato Norte-Americano (`usa-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/usa-1/pacote/`, do código `coleta/usa-1/` e do relatório `docs/coleta/usa-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 63, de 1921/22 a 2025; 35 sem jogos.
- **Jogos:** 8708 (8688 com placar); **gols:** 24858; **gols com autor:** 21918 (88%); **cartões:** 30061.
- **Clubes:** 134; **artilheiros:** 20 edições com artilheiro (26 linhas, com empates).
- **Classificação final:** 63 edições; **tabelas publicadas guardadas para conferência:** 940 linhas.
- **No banco:** sim; **último commit do pacote:** 5bace06.
- **Observação da competição:** 1ª divisão dos EUA, uma edição por título, como a lista "Division I" da RSSSF: ASL I (1921/22-1932/33, só tabelas), as duas ligas de 1967 (United Soccer Association e NPSL), NASL (1968-1984, só tabelas) e MLS (1996-2025; campeão = MLS Cup). Sem 1ª divisão de 1985 a 1995. Clubes do Canadá com país CAN.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão dos EUA (usa-1): uma por título, como na lista de campeões da "Division I" da RSSSF
(tablesu/usachamp.html). Escopo decidido em 24/11/2026 (o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"):

- ASL I (American Soccer League, 1921/22 a 1932/33): 14 títulos, com as meias-temporadas de 1929 (outono), 1930 (outono) e
  1932 (primavera), como na lista da RSSSF. Só as tabelas (usadave/asli.html): a RSSSF não tem os jogos.
- 1967: duas ligas rivais, cada uma uma edição: United Soccer Association (a da FIFA; os times eram clubes europeus e
  sul-americanos jogando com nome de cidade americana) e NPSL (a "pirata"). Tabelas e campeão (usadave/nasl.html).
- NASL 1968-1984: tabelas e campeão (usadave/nasl.html); os playoffs só em texto ("X defeated Y 2-1"), na observação. As
  temporadas indoor ficam fora.
- 1985-1995: sem 1ª divisão (sem edição).
- MLS 1996-2025: jogos da RSSSF (tablesu/usaAA.html, usaAAAA.html de 2010 em diante) e da ESPN (2004, 2011, 2012 e 2025, que a
  RSSSF só tem nas tabelas); 1997 e 1998 só com as tabelas (nenhuma das fontes tem os jogos). O campeão é o da MLS Cup.
  A temporada 2026 entra depois da final (18/12/2026).
Ficam fora a ASL II (1933-1983), a International Soccer League (1960-1965, torneio de verão com clubes estrangeiros), as
ligas de 2º nível de 1985-1995 (APSL, A-League), a US Open Cup e a Leagues Cup.
```

**Edições:** 63, uma por título, como a lista de campeões da "Division I" da RSSSF (`usachamp.html`). Escopo decidido em 24/11/2026 (o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"): ASL I (1921/22-1932/33, com as meias-temporadas de 1929, 1930 e 1932), as duas ligas de 1967 (United Soccer Association, a da FIFA, e NPSL, a "pirata"), NASL (1968-1984) e MLS (1996-2025). De 1985 a 1995 o país não teve liga de 1ª divisão. A temporada 2026 da MLS entra depois da final (18/12/2026).

**Fontes:** RSSSF (`data/coleta/usa-1/rsssf/`) e ESPN (liga `usa.1`, 2002 em diante: hora (de Nova York), estádio, público, gols com minuto e cartões; os jogos de 2004 e a fase regular de 2011, 2012 e 2025).

**Clubes:** nomes e identidades no começo de `coleta/usa-1/clubes_usa.py`. Renomeação na mesma cidade é o mesmo clube (MetroStars = New York Red Bulls, Kansas City Wizards = Sporting Kansas City, Dallas Burn = FC Dallas, San Jose Clash = San Jose Earthquakes, Montreal Impact = CF Montréal); mudança de cidade é outro clube; os clubes da NASL com nome de clube da MLS levam "(NASL)" (Seattle Sounders, Portland Timbers, Vancouver Whitecaps, San Jose Earthquakes). Clubes do Canadá com país CAN.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 25.
- **Edições com alguma tabela divergente** (1; motivo no relatório, na edição): 2004.
- **Edições sem tabela para conferir** (37): 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929, 1929/30, 1930, 1931, 1932, 1932/33, 1967 USA, 1967 NPSL, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1997, 1998, 1999, 2002.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1930s | 4 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 4 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 5 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 4 | 385 | 100% | 0% | 54% | 0% | 0% | 0% | 21% | 0.0 |
| 2000s | 10 | 1943 | 100% | 77% | 28% | 65% | 53% | 23% | 67% | 2.8 |
| 2010s | 10 | 3518 | 100% | 99% | 0% | 99% | 96% | 83% | 99% | 3.6 |
| 2020s | 6 | 2862 | 100% | 99% | 27% | 99% | 99% | 88% | 99% | 4.2 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1921/22 a 1922/23: 7 clubes
- 1923/24: 8 clubes
- 1924/25: 12 clubes
- 1925/26: 10 clubes
- 1926/27: 11 clubes
- 1927/28 a 1928/29: 12 clubes
- 1929: 9 clubes
- 1929/30: 10 clubes
- 1930: 8 clubes
- 1931: 10 clubes
- 1932: 7 clubes
- 1932/33: 11 clubes
- 1967 USA: 12 clubes
- 1967 NPSL: 10 clubes
- 1968: 17 clubes
- 1969: 5 clubes
- 1970: 6 clubes
- 1971 a 1972: 8 clubes
- 1973: 9 clubes
- 1974: 15 clubes
- 1975 a 1976: 20 clubes
- 1977: 18 clubes
- 1978 a 1980: 24 clubes
- 1981: 21 clubes
- 1982: 14 clubes
- 1983: 12 clubes
- 1984: 9 clubes
- 1996 a 1997: 10 clubes
- 1998 a 2001: 12 clubes
- 2002 a 2004: 10 clubes
- 2005 a 2006: 12 clubes
- 2007: 13 clubes
- 2008: 14 clubes
- 2009: 15 clubes
- 2010: 16 clubes
- 2011: 18 clubes
- 2012 a 2014: 19 clubes
- 2015 a 2016: 20 clubes
- 2017: 22 clubes
- 2018: 23 clubes
- 2019: 24 clubes
- 2020: 26 clubes
- 2021: 27 clubes
- 2022: 28 clubes
- 2023 a 2024: 29 clubes
- 2025: 30 clubes

**Pontos por vitória:**

- 1921/22 a 1967 USA: 2
- 1967 NPSL a 1984: 6
- 1996 a 2025: 3

**Nome oficial:**

- 1921/22 a 1929: American Soccer League <ano>
- 1929/30: Atlantic Coast League <ano>
- 1930 a 1932/33: American Soccer League <ano>
- 1967 USA: United Soccer Association <ano>
- 1967 NPSL: National Professional Soccer League <ano>
- 1968 a 1984: North American Soccer League <ano>
- 1996 a 2025: Major League Soccer <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1921/22 a 1984: sem jogos (só a tabela final)
- 1996: pontos corridos + mata-mata
- 1997 a 1998: sem jogos (só a tabela final)
- 1999 a 2025: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1996: Primeira fase (liga); Playoffs (mata_mata, ida_volta)
- 1999: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2001: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, ida_volta)
- 2002: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico)
- 2003: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2004: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2005: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2006: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2007: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2008: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2009: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2010: Primeira fase (liga); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico)
- 2011: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2012: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2014: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2015: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2016: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2017: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2018: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, ida_volta); Final de conferência (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2019: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2020: Primeira fase (liga); Playoffs (mata_mata, jogo_unico); Primeira fase dos playoffs (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2021: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2023: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2024: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2025: Primeira fase (liga); Repescagem (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal de conferência (mata_mata, jogo_unico); Final de conferência (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 61 edições
- calculada: 2 edições

**Observações das edições:**

- 1921/22: só a tabela: a RSSSF não tem os jogos da ASL I
- 1922/23: só a tabela: a RSSSF não tem os jogos da ASL I
- 1923/24: só a tabela: a RSSSF não tem os jogos da ASL I
- 1924/25: só a tabela: a RSSSF não tem os jogos da ASL I
- 1925/26: só a tabela: a RSSSF não tem os jogos da ASL I
- 1926/27: só a tabela: a RSSSF não tem os jogos da ASL I
- 1927/28: só a tabela: a RSSSF não tem os jogos da ASL I; dois turnos; o campeão saiu dos playoffs entre os primeiros (Boston Wonder Workers 4-2 New Bedford Whalers)
- 1928/29: só a tabela: a RSSSF não tem os jogos da ASL I; dois turnos; a classificação é por aproveitamento
- 1929: só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de outono, suspensa em 9/10/1929 com o fim da "soccer war" (a ASL se juntou à Eastern Soccer League)
- 1929/30: só a tabela: a RSSSF não tem os jogos da ASL I; disputada como Atlantic Coast League (a ASL e a Eastern Soccer League juntas)
- 1930: só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de outono
- 1931: só a tabela: a RSSSF não tem os jogos da ASL I; primavera e outono de 1931; a lista de campeões da RSSSF a chama de 1930-31; final: New York Giants x New Bedford Whalers (8-3 e 6-0)
- 1932: só a tabela: a RSSSF não tem os jogos da ASL I; meia-temporada de primavera, talvez incompleta ("may be an incomplete set of standings", RSSSF); sem gols na tabela
- 1932/33: só a tabela: a RSSSF não tem os jogos da ASL I; só o 1º turno (outono de 1932) tem tabela; a liga foi refeita no verão de 1933 como a ASL II
- 1967 USA: liga da FIFA; os times eram clubes europeus e sul-americanos com nome de cidade americana; só a tabela e a final (Los Angeles Wolves 6-5 Washington Whips, prorrogação)
- 1967 NPSL: liga sem reconhecimento da FIFA ("pirata"); só a tabela e a final (Oakland Clippers x Baltimore Bays, 0-1 e 4-1); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1968: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1969: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1970: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1971: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1972: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1973: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1974: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 3 por empate e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1975: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1976: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1977: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1978: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1979: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1980: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1981: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1982: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1983: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1984: só a tabela: a RSSSF não tem os jogos da NASL (os playoffs, só em texto); pontuação: 6 por vitória, 1 por vitória nos pênaltis (shootout, sem empates) e 1 por gol (até 3 por jogo) (a classificação é a tabela publicada)
- 1996: pontuação: 3 por vitória e 1 por vitória nos pênaltis (shootout, sem empates) (a classificação é a tabela publicada)
- 1997: só a tabela: a RSSSF não tem os jogos deste ano e a ESPN começa em 2002; pontuação: 3 por vitória e 1 por vitória nos pênaltis (shootout, sem empates) (a classificação é a tabela publicada)
- 1998: só a tabela: a RSSSF não tem os jogos deste ano e a ESPN começa em 2002; pontuação: 3 por vitória e 1 por vitória nos pênaltis (shootout, sem empates) (a classificação é a tabela publicada)
- 1999: pontuação: 3 por vitória e 1 por vitória nos pênaltis (shootout, sem empates) (a classificação é a tabela publicada)
- 2004: jogos da ESPN (a página da RSSSF só tem as tabelas)
- 2011: fase regular da ESPN (a página da RSSSF só tem as tabelas)
- 2012: fase regular da ESPN (a página da RSSSF só tem as tabelas)
- 2025: fase regular da ESPN (a página da RSSSF só tem as tabelas)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Fall River Marksmen: 7
- Los Angeles Galaxy: 6
- New York Cosmos: 5
- DC United: 4
- Columbus Crew: 3
- Bethlehem Steel: 2
- Chicago Sting: 2
- Sporting Kansas City: 2
- San Jose Earthquakes: 2
- Houston Dynamo: 2
- Seattle Sounders: 2
- J&P Coats: 1
- Boston Wonder Workers: 1
- New York Giants: 1
- New Bedford Whalers: 1
- Fall River FC: 1
- Los Angeles Wolves: 1
- Oakland Clippers: 1
- Atlanta Chiefs: 1
- Kansas City Spurs: 1
- Rochester Lancers: 1
- Dallas Tornado: 1
- Philadelphia Atoms: 1
- Los Angeles Aztecs: 1
- Tampa Bay Rowdies: 1
- Toronto Metros-Croatia: 1
- Vancouver Whitecaps (NASL): 1
- Tulsa Roughnecks: 1
- Chicago Fire: 1
- Real Salt Lake: 1
- Colorado Rapids: 1
- Portland Timbers: 1
- Toronto FC: 1
- Atlanta United: 1
- New York City FC: 1
- Los Angeles FC: 1
- Inter Miami: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1921/22 | Bethlehem Steel | New York Field Club |
| 1922/23 | J&P Coats | Bethlehem Steel |
| 1923/24 | Fall River Marksmen | Bethlehem Steel |
| 1924/25 | Fall River Marksmen | Bethlehem Steel |
| 1925/26 | Fall River Marksmen | New Bedford Whalers |
| 1926/27 | Bethlehem Steel | Fall River Marksmen |
| 1927/28 | Boston Wonder Workers | New Bedford Whalers |
| 1928/29 | Fall River Marksmen | Brooklyn Wanderers |
| 1929 | Fall River Marksmen | Providence Gold Bugs |
| 1929/30 | Fall River Marksmen | New Bedford Whalers |
| 1930 | Fall River Marksmen | New Bedford Whalers |
| 1931 | New York Giants | New Bedford Whalers |
| 1932 | New Bedford Whalers | Hakoah All-Stars |
| 1932/33 | Fall River FC | J&P Coats |
| 1967 USA | Los Angeles Wolves | Washington Whips |
| 1967 NPSL | Oakland Clippers | Baltimore Bays |
| 1968 | Atlanta Chiefs | San Diego Toros |
| 1969 | Kansas City Spurs | Atlanta Chiefs |
| 1970 | Rochester Lancers | Washington Darts |
| 1971 | Dallas Tornado | Atlanta Chiefs |
| 1972 | New York Cosmos | St. Louis Stars |
| 1973 | Philadelphia Atoms | Dallas Tornado |
| 1974 | Los Angeles Aztecs | Miami Toros |
| 1975 | Tampa Bay Rowdies | Portland Timbers (NASL) |
| 1976 | Toronto Metros-Croatia | Minnesota Kicks |
| 1977 | New York Cosmos | Seattle Sounders (NASL) |
| 1978 | New York Cosmos | Tampa Bay Rowdies |
| 1979 | Vancouver Whitecaps (NASL) | Tampa Bay Rowdies |
| 1980 | New York Cosmos | Fort Lauderdale Strikers |
| 1981 | Chicago Sting | New York Cosmos |
| 1982 | New York Cosmos | Seattle Sounders (NASL) |
| 1983 | Tulsa Roughnecks | Toronto Blizzard |
| 1984 | Chicago Sting | Toronto Blizzard |
| 1996 | DC United | Los Angeles Galaxy |
| 1997 | DC United | Colorado Rapids |
| 1998 | Chicago Fire | DC United |
| 1999 | DC United | Los Angeles Galaxy |
| 2000 | Sporting Kansas City | Chicago Fire |
| 2001 | San Jose Earthquakes | Los Angeles Galaxy |
| 2002 | Los Angeles Galaxy | New England Revolution |
| 2003 | San Jose Earthquakes | Chicago Fire |
| 2004 | DC United | Sporting Kansas City |
| 2005 | Los Angeles Galaxy | New England Revolution |
| 2006 | Houston Dynamo | New England Revolution |
| 2007 | Houston Dynamo | New England Revolution |
| 2008 | Columbus Crew | New York Red Bulls |
| 2009 | Real Salt Lake | Los Angeles Galaxy |
| 2010 | Colorado Rapids | FC Dallas |
| 2011 | Los Angeles Galaxy | Houston Dynamo |
| 2012 | Los Angeles Galaxy | Houston Dynamo |
| 2013 | Sporting Kansas City | Real Salt Lake |
| 2014 | Los Angeles Galaxy | New England Revolution |
| 2015 | Portland Timbers | Columbus Crew |
| 2016 | Seattle Sounders | Toronto FC |
| 2017 | Toronto FC | Seattle Sounders |
| 2018 | Atlanta United | Portland Timbers |
| 2019 | Seattle Sounders | Toronto FC |
| 2020 | Columbus Crew | Seattle Sounders |
| 2021 | New York City FC | Portland Timbers |
| 2022 | Los Angeles FC | Philadelphia Union |
| 2023 | Columbus Crew | Los Angeles FC |
| 2024 | Los Angeles Galaxy | New York Red Bulls |
| 2025 | Inter Miami | Vancouver Whitecaps |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1923/24: Fall River Marksmen -30
- 1924/25: Philadelphia Field Club -2
- 1925/26: Newark Skeeters -1
- 1926/27: Boston Wonder Workers -2
- 1928/29: Newark Skeeters -1
- 1930: New York Giants +2
- 1932: Boston Wonder Workers -1
- 1932/33: Queens Bohemians -2
- 2001: Colorado Rapids -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/usa-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Tabelas da página que não são da edição (`TABELAS_FORA`, 2)

- **2020 · usa2020:107:** tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)
- **2020 · usa2020:124:** tabela de quando a liga parou pela pandemia (março de 2020, duas rodadas)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 1)

- **2020:** a temporada parou em março (pandemia) e voltou com o torneio MLS is Back (Flórida, julho e agosto), cuja fase de grupos contou para a fase regular; o mata-mata do torneio não é da liga e fica fora; a classificação foi por pontos por jogo, e 7 jogos do Oeste não foram disputados

### Identidade dos clubes

Regras em `coleta/usa-1/clubes_usa.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão dos EUA (ASL I, 1967, NASL, MLS): cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- o mesmo clube com outro nome (renomeação na mesma cidade, como a RSSSF e a MLS contam): NY/NJ MetroStars = New York Red
  Bulls; Kansas City Wiz/Wizards = Sporting Kansas City; Dallas Burn = FC Dallas; San Jose Clash = San Jose Earthquakes (a
  MLS conta o Earthquakes de 2008 como continuação do de 1996-2005); Montreal Impact = CF Montréal; Houston Dynamos = Houston
  Dynamo; Atlanta Apollos (1973) = Atlanta Chiefs; Miami Gatos = Miami Toros; Toronto Metros = Toronto Metros-Croatia;
  Golden Bay Earthquakes (1983-1984) = San Jose Earthquakes da NASL; Boston Bears = Boston Wonder Workers; Providence
  Clamdiggers = Providence Gold Bugs; J & P Coats = Pawtucket Rangers (nome de exibição "J&P Coats"); Fall River United (1921/22)
  = Fall River Marksmen; Philadelphia Field Club de 1921/22 = Bethlehem Steel (a RSSSF: "Philadelphia changed their name to
  Bethlehem Steel"; o Philadelphia Field Club de 1922 em diante é outro clube);
- New York Giants da ASL: o de 1923-1929 virou New York Soccer Club em 1930; o New York Nationals (1927-1929) passou a se chamar
  New York Giants em 1930-1932 (RSSSF). Cada um com o último nome: "New York Soccer Club" e "New York Giants" (o campeão de 1931);
- clubes diferentes: o que mudou de cidade (Los Angeles Toros -> San Diego Toros, Denver Dynamos -> Minnesota Kicks, Miami Toros
  -> Fort Lauderdale Strikers -> Minnesota Strikers, Hartford Bicentennials -> Oakland Stompers -> Edmonton Drillers, Toronto
  Metros-Croatia -> Toronto Blizzard...); os da NASL e os da MLS com o mesmo nome (Seattle Sounders, Portland Timbers, Vancouver
  Whitecaps, San Jose Earthquakes: os da NASL levam "(NASL)"; o Vancouver Whitecaps da MLS conta 1974 como fundação, mas a
  franquia da NASL acabou em 1984); Atlanta Chiefs de 1967-1973 e o de 1979-1981 (ex-Colorado Caribous);
- os times de 1967 da United Soccer Association eram clubes europeus e sul-americanos com nome de cidade americana (Wolves =
  Wolverhampton, Stokers = Stoke City...): entram com o nome da cidade, como na tabela;
- país: os clubes do Canadá (Toronto, Vancouver, Montreal, Edmonton, Calgary) com `CAN`.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a ASL II (1933-1983, liga regional e depois de 2º nível), a International Soccer League (1960-1965, torneio de verão com clubes estrangeiros), as ligas de 2º nível de 1985-1995 (APSL, A-League), as temporadas indoor da NASL, o torneio MLS is Back (2020, só o mata-mata; a fase de grupos contou na liga), a US Open Cup, a Leagues Cup e os jogos de exibição (All-Star, amistosos).
- **Edições sem jogos (35):** a ASL I, 1967 e a NASL (a RSSSF só tem as tabelas e as finais em texto) e a MLS de 1997 e 1998 (a RSSSF só tem as tabelas e a ESPN começa em 2002).
- **Edições sem jogos** (35): 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929, 1929/30, 1930, 1931, 1932, 1932/33, 1967 USA, 1967 NPSL, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1997, 1998.
- **Décadas com menos da metade dos gols com autor:** 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- ASL I (1921/22-1932/33), 1967 e NASL (1968-1984) só com as tabelas: a RSSSF não tem os jogos (os playoffs só em texto). Fonte que resolveria: os livros de Colin Jose ("NASL: A Complete Record", "The American Soccer League 1921-1931") ou jornais da época.
- MLS 1997 e 1998 só com as tabelas: a RSSSF não tem os jogos e a ESPN começa em 2002. Fonte que resolveria: os arquivos de jogos da MLS (mlssoccer.com) ou a Wikipédia de cada temporada.
- 2004: falta um DC United x New York Red Bulls (a ESPN não tem; a RSSSF só tem as tabelas).
- Temporada 2026 da MLS: entra depois da final (18/12/2026).
- Identidades a conferir pela revisão: Philadelphia Field Club de 1921/22 = Bethlehem Steel; os dois New York Giants da ASL (New York Soccer Club e New York Giants); os clubes da NASL separados dos da MLS com o mesmo nome.

## 10. Arquivos e comandos

Código em `coleta/usa-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga usa.1) de 2002 a 2025 para data/coleta/usa-1/espn/usa1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão dos EUA para data/coleta/usa-1/rsssf/: a lista de campeões da "Division I" |
| `clubes_usa.py` | Identidade dos clubes da 1ª divisão dos EUA (ASL I, 1967, NASL, MLS): cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão dos EUA (usa-1): uma por título, como na lista de campeões da "Division I" da RSSSF |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão dos EUA, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão dos EUA e grava o pacote em data/coleta/usa-1/pacote/ e o relatório em docs/coleta/usa-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão dos EUA nas páginas da RSSSF (data/coleta/usa-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado nos EUA; o código fica para as outras ligas). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/usa-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/usa-1/pacote/`; relatório: `docs/coleta/usa-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/usa-1/baixar_espn.py
python coleta/usa-1/baixar_rsssf.py
python coleta/usa-1/importar.py
python coleta/usa-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py usa-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

