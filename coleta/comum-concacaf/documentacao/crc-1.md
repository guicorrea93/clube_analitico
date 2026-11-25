# Campeonato Costarriquenho (`crc-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/crc-1/pacote/`, do código `coleta/crc-1/` e do relatório `docs/coleta/crc-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 123, de 1921 a 2026 Clausura; 74 sem jogos.
- **Jogos:** 7065 (7061 com placar); **gols:** 19008; **gols com autor:** 2951 (16%); **cartões:** 0.
- **Clubes:** 65; **artilheiros:** 1 edições com artilheiro (1 linhas, com empates).
- **Classificação final:** 123 edições; **tabelas publicadas guardadas para conferência:** 1263 linhas.
- **No banco:** sim; **último commit do pacote:** 85c4da52.
- **Observação da competição:** 1ª divisão da Costa Rica de 1921 ao Clausura 2026, uma edição por título, como a contagem oficial da UNAFUT (lista da RSSSF): um campeão por ano até 2006/07 (1961 com duas entidades rivais; 1954 e 1956 sem campeonato), Apertura e Clausura de 2007/08 em diante. Até 1995/96 quase só tabelas.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão da Costa Rica (crc-1): uma por título, como na lista de campeões da RSSSF (tablesc/coschamp.html),
que é a contagem oficial da UNAFUT. Escopo decidido em 24/11/2026:

- 1921 a 1985, um campeão por ano; 1954 e 1956 não foram disputados (sem edição); 1961 com duas edições, uma por entidade
  rival (Asofútbol, campeão Herediano; Federación, campeão Carmelita, título reconhecido pela UNAFUT em 2003).
- 1986/87 a 2006/07, uma por temporada (a temporada passou a cruzar o ano); de 1997/98 a 2006/07, Apertura e Clausura são
  fases do ano (a final entre os vencedores, quando houve, decide o título).
- 2007/08 em diante, Apertura e Clausura, uma edição cada ("2007 Apertura", "2008 Clausura"), até o Clausura 2026 (o Apertura
  2026 ainda está em disputa).

Fontes dos jogos por edição: a página da temporada (cosAA.html; cosAAAA.html de 2010 em diante). Até 1996 as páginas trazem
quase só as tabelas: a edição entra só com elas quando a página tem menos de 90% dos jogos que a tabela diz. 1991/92 e
1993/94 não têm página (só campeão e vice da lista). 2010/11 e 2011/12: a página só tem as tabelas e a fase final; a fase
regular vem da ESPN.
```

**Edições:** 123, uma por título, como a contagem oficial da UNAFUT, que a lista de campeões da RSSSF (`coschamp.html`) reproduz. Escopo decidido em 24/11/2026: 1921 a 1985, um campeão por ano (1954 e 1956 não foram disputados; 1961 teve duas entidades rivais, Asofútbol e Federación, e entra com duas edições); 1986/87 a 2006/07, uma por temporada (de 1997/98 em diante, Apertura e Clausura são fases do ano); de 2007/08 em diante, Apertura e Clausura, uma edição cada, até o Clausura 2026 (o Apertura 2026 ainda está em disputa).

**Fontes:** RSSSF (`data/coleta/crc-1/rsssf/`) e ESPN (liga `crc.1`: hora, estádio, público, gols com minuto e cartões, casados com os jogos da RSSSF).

**Clubes:** nomes e identidades no começo de `coleta/crc-1/clubes_crc.py` (Carmen FC = Carmelita; Liberia Mía = Municipal Liberia; Municipal Puntarenas e Puntarenas FC separados, como na lista de campeões). Homônimos de clubes de outros países levam a cidade: Santos de Guápiles, Sporting de San José, Uruguay de Coronado.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 40.
- **Edições com alguma tabela divergente** (4; motivo no relatório, na edição): 1998/99, 2000/01, 2002/03, 2003/04.
- **Edições sem tabela para conferir** (79): 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1955, 1957, 1958, 1959, 1960, 1961 Asofútbol, 1961 Federación, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1996/97, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Edições com menos jogos que o esperado:** 1997/98 (222 de 318), 2001/02 (267 de 266), 2003/04 (265 de 266), 2020 Clausura (138 de 137).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1930s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1940s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1950s | 8 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 11 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 976 | 99% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 12 | 2185 | 94% | 21% | 100% | 18% | 1% | 0% | 25% | 0.0 |
| 2010s | 20 | 2250 | 100% | 97% | 98% | 87% | 31% | 0% | 24% | 0.0 |
| 2020s | 13 | 1654 | 100% | 98% | 100% | 98% | 98% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1921: 7 clubes
- 1922: 5 clubes
- 1923: 6 clubes
- 1924: 7 clubes
- 1925: 5 clubes
- 1926: 7 clubes
- 1927: 5 clubes
- 1928 a 1929: 4 clubes
- 1930: 6 clubes
- 1931: 5 clubes
- 1932 a 1934: 8 clubes
- 1935 a 1936: 7 clubes
- 1937 a 1940: 6 clubes
- 1941 a 1943: 7 clubes
- 1944: 6 clubes
- 1945 a 1948: 7 clubes
- 1949: 8 clubes
- 1950: 9 clubes
- 1951 a 1955: 10 clubes
- 1957 a 1960: 8 clubes
- 1961 Asofútbol: 5 clubes
- 1961 Federación: 3 clubes
- 1962 a 1963: 6 clubes
- 1964: 9 clubes
- 1965 a 1969: 10 clubes
- 1970: 9 clubes
- 1971 a 1979: 0 clubes
- 1980 a 1987/88: 10 clubes
- 1988/89: 8 clubes
- 1989/90: 10 clubes
- 1990/91: 12 clubes
- 1991/92 a 1993/94: 0 clubes
- 1994/95: 12 clubes
- 1995/96: 28 clubes
- 1996/97 a 1997/98: 12 clubes
- 1998/99: 14 clubes
- 1999/00 a 2011 Clausura: 12 clubes
- 2011 Apertura a 2012 Clausura: 11 clubes
- 2012 Apertura a 2025 Clausura: 12 clubes
- 2025 Apertura a 2026 Clausura: 10 clubes

**Pontos por vitória:**

- 1921 a 1994/95: 2
- 1995/96 a 2026 Clausura: 3

**Nome oficial:**

- 1921 a 1960: Primera División de Costa Rica <ano>
- 1961 Asofútbol: Campeonato de la Asofútbol <ano>
- 1961 Federación: Campeonato de la Federación <ano>
- 1962 a 2006/07: Primera División de Costa Rica <ano>
- 2007 Apertura: Primera División de Costa Rica Apertura <ano>
- 2008 Clausura: Primera División de Costa Rica Clausura <ano>
- 2008 Apertura: Primera División de Costa Rica Apertura <ano>
- 2009 Clausura: Primera División de Costa Rica Clausura <ano>
- 2009 Apertura: Primera División de Costa Rica Apertura <ano>
- 2010 Clausura: Primera División de Costa Rica Clausura <ano>
- 2010 Apertura: Primera División de Costa Rica Apertura <ano>
- 2011 Clausura: Primera División de Costa Rica Clausura <ano>
- 2011 Apertura: Primera División de Costa Rica Apertura <ano>
- 2012 Clausura: Primera División de Costa Rica Clausura <ano>
- 2012 Apertura: Primera División de Costa Rica Apertura <ano>
- 2013 Clausura: Primera División de Costa Rica Clausura <ano>
- 2013 Apertura: Primera División de Costa Rica Apertura <ano>
- 2014 Clausura: Primera División de Costa Rica Clausura <ano>
- 2014 Apertura: Primera División de Costa Rica Apertura <ano>
- 2015 Clausura: Primera División de Costa Rica Clausura <ano>
- 2015 Apertura: Primera División de Costa Rica Apertura <ano>
- 2016 Clausura: Primera División de Costa Rica Clausura <ano>
- 2016 Apertura: Primera División de Costa Rica Apertura <ano>
- 2017 Clausura: Primera División de Costa Rica Clausura <ano>
- 2017 Apertura: Primera División de Costa Rica Apertura <ano>
- 2018 Clausura: Primera División de Costa Rica Clausura <ano>
- 2018 Apertura: Primera División de Costa Rica Apertura <ano>
- 2019 Clausura: Primera División de Costa Rica Clausura <ano>
- 2019 Apertura: Primera División de Costa Rica Apertura <ano>
- 2020 Clausura: Primera División de Costa Rica Clausura <ano>
- 2020 Apertura: Primera División de Costa Rica Apertura <ano>
- 2021 Clausura: Primera División de Costa Rica Clausura <ano>
- 2021 Apertura: Primera División de Costa Rica Apertura <ano>
- 2022 Clausura: Primera División de Costa Rica Clausura <ano>
- 2022 Apertura: Primera División de Costa Rica Apertura <ano>
- 2023 Clausura: Primera División de Costa Rica Clausura <ano>
- 2023 Apertura: Primera División de Costa Rica Apertura <ano>
- 2024 Clausura: Primera División de Costa Rica Clausura <ano>
- 2024 Apertura: Primera División de Costa Rica Apertura <ano>
- 2025 Clausura: Primera División de Costa Rica Clausura <ano>
- 2025 Apertura: Primera División de Costa Rica Apertura <ano>
- 2026 Clausura: Primera División de Costa Rica Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1921 a 1995/96: sem jogos (só a tabela final)
- 1996/97 a 1997/98: pontos corridos + mata-mata
- 1998/99 a 1999/00: pontos corridos
- 2000/01 a 2001/02: pontos corridos + mata-mata
- 2002/03: pontos corridos
- 2003/04: pontos corridos + mata-mata
- 2004/05 a 2006/07: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2007 Apertura a 2010 Clausura: pontos corridos + mata-mata
- 2010 Apertura a 2012 Clausura: jogos incompletos; mata-mata
- 2012 Apertura a 2016 Clausura: pontos corridos + mata-mata
- 2016 Apertura: pontos corridos
- 2017 Clausura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1996/97: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1997/98: Apertura (liga); Clausura (liga); Quartas de final do Clausura (mata_mata, ida_volta); Semifinal do Clausura (mata_mata, ida_volta); Final do Clausura (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1998/99: Apertura (liga); Clausura (liga); Primeira fase (liga)
- 1999/00: Apertura (liga); Clausura (liga)
- 2000/01: Apertura (liga); Primeira fase (liga); Grupo do rebaixamento (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2001/02: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2002/03: Apertura (liga); Clausura (liga)
- 2003/04: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, ida_volta)
- 2004/05: Apertura (liga); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Semifinal do Clausura (mata_mata, ida_volta); Final do Clausura (mata_mata, ida_volta)
- 2005/06: Apertura (liga); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Semifinal do Clausura (mata_mata, ida_volta); Final do Clausura (mata_mata, ida_volta)
- 2006/07: Apertura (liga); Quartas de final do Apertura (mata_mata, ida_volta); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Quartas de final do Clausura (mata_mata, ida_volta); Semifinal do Clausura (mata_mata, ida_volta); Final do Clausura (mata_mata, ida_volta)
- 2007 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Apertura: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Clausura: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Apertura: Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Clausura: Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2013 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2013 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2014 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2014 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2015 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2015 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Apertura: Primeira fase (liga); Fase final (liga)
- 2017 Clausura: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2017 Apertura: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2018 Clausura: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2018 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020 Apertura: Primeira fase (liga); Grupo do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Clausura: Primeira fase (liga); Grupo do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Clausura: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2025 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2026 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 107 edições
- lista de campeões da Wikipédia em inglês: 12 edições
- calculada: 4 edições

**Observações das edições:**

- 1921: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1922: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1923: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1924: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1925: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1926: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1927: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1928: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1929: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1930: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1931: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1932: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1933: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1934: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1935: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1936: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1937: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1938: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1939: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1940: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1941: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1942: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1943: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1944: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1945: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1946: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1947: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1948: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1949: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1950: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1951: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1952: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1953: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1955: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1957: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1958: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1959: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1960: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1961 Asofútbol: campeonato da Asociación de Fútbol (os clubes rebeldes), paralelo ao da Federación; só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1961 Federación: campeonato da Federación (3 clubes); o título do Carmelita foi reconhecido pela UNAFUT em 2003; só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1962: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1963: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1964: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1965: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1966: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1967: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1968: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1969: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1970: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1971: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1972: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1973: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1974: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1975: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1976: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1977: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1978: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1979: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1980: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1981: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1982: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1983: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1984: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1985: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1986/87: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1987/88: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1988/89: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1989/90: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1990/91: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1991/92: sem página da RSSSF: só o campeão e o vice da lista
- 1992/93: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1993/94: sem página da RSSSF: só o campeão e o vice da lista
- 1994/95: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 1995/96: só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)
- 2010 Apertura: jogos incompletos: a página da RSSSF só tem a tabela da fase regular e os jogos da fase final; a ESPN destes anos tem jogos adiados repetidos e jogos faltando (não foi usada); entram a tabela publicada e a fase final
- 2011 Clausura: jogos incompletos: a página da RSSSF só tem a tabela da fase regular e os jogos da fase final; a ESPN destes anos tem jogos adiados repetidos e jogos faltando (não foi usada); entram a tabela publicada e a fase final
- 2011 Apertura: jogos incompletos: a página da RSSSF só tem a tabela da fase regular e os jogos da fase final; a ESPN destes anos tem jogos adiados repetidos e jogos faltando (não foi usada); entram a tabela publicada e a fase final
- 2012 Clausura: jogos incompletos: a página da RSSSF só tem a tabela da fase regular e os jogos da fase final; a ESPN destes anos tem jogos adiados repetidos e jogos faltando (não foi usada); entram a tabela publicada e a fase final

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Saprissa: 40
- Herediano: 32
- Alajuelense: 31
- La Libertad: 6
- Cartaginés: 4
- Orión: 2
- Universidad de Costa Rica: 1
- Carmelita: 1
- Uruguay de Coronado: 1
- Municipal Puntarenas: 1
- Municipal Liberia: 1
- Brujas de Escazú: 1
- Pérez Zeledón: 1
- San Carlos: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1921 | Herediano | Gimnástica Española |
| 1922 | Herediano | La Libertad |
| 1923 | Cartaginés | La Libertad |
| 1924 | Herediano | Cartaginés |
| 1925 | La Libertad | Herediano |
| 1926 | La Libertad | Cartaginés |
| 1927 | Herediano | La Libertad |
| 1928 | Alajuelense | Gimnástica Española |
| 1929 | La Libertad | Alajuelense |
| 1930 | Herediano | Gimnástica Española |
| 1931 | Herediano | Orión |
| 1932 | Herediano | La Libertad |
| 1933 | Herediano | Gimnástica Española |
| 1934 | La Libertad | Alajuela Junior |
| 1935 | Herediano | Alajuela Junior |
| 1936 | Cartaginés | La Libertad |
| 1937 | Herediano | Gimnástica Española |
| 1938 | Orión | Gimnástica Española |
| 1939 | Alajuelense | Herediano |
| 1940 | Cartaginés | Orión |
| 1941 | Alajuelense | La Libertad |
| 1942 | La Libertad | Gimnástica Española |
| 1943 | Universidad de Costa Rica | Alajuelense |
| 1944 | Orión | Herediano |
| 1945 | Alajuelense | Orión |
| 1946 | La Libertad | Herediano |
| 1947 | Herediano | La Libertad |
| 1948 | Herediano | Alajuelense |
| 1949 | Alajuelense | Orión |
| 1950 | Alajuelense | Saprissa |
| 1951 | Herediano | Orión |
| 1952 | Saprissa | Alajuelense |
| 1953 | Saprissa | Herediano |
| 1955 | Herediano | Saprissa |
| 1957 | Saprissa | Alajuelense |
| 1958 | Alajuelense | Saprissa |
| 1959 | Alajuelense | Saprissa |
| 1960 | Alajuelense | Herediano |
| 1961 Asofútbol | Herediano | Saprissa |
| 1961 Federación | Carmelita | Uruguay de Coronado |
| 1962 | Saprissa | Alajuelense |
| 1963 | Uruguay de Coronado | Saprissa |
| 1964 | Saprissa | Orión |
| 1965 | Saprissa | Alajuelense |
| 1966 | Alajuelense | Saprissa |
| 1967 | Saprissa | Alajuelense |
| 1968 | Saprissa | Cartaginés |
| 1969 | Saprissa | Alajuelense |
| 1970 | Alajuelense | Saprissa |
| 1971 | Alajuelense | Saprissa |
| 1972 | Saprissa | Alajuelense |
| 1973 | Saprissa | Cartaginés |
| 1974 | Saprissa | Herediano |
| 1975 | Saprissa | Cartaginés |
| 1976 | Saprissa | Barrio México |
| 1977 | Saprissa | Cartaginés |
| 1978 | Herediano | Municipal Puntarenas |
| 1979 | Herediano | Cartaginés |
| 1980 | Alajuelense | Herediano |
| 1981 | Herediano | Limonense |
| 1982 | Saprissa | Municipal Puntarenas |
| 1983 | Alajuelense | Municipal Puntarenas |
| 1984 | Alajuelense | Saprissa |
| 1985 | Herediano | Alajuelense |
| 1986/87 | Municipal Puntarenas | Alajuelense |
| 1987/88 | Herediano | Cartaginés |
| 1988/89 | Saprissa | Herediano |
| 1989/90 | Saprissa | Alajuelense |
| 1990/91 | Alajuelense | Saprissa |
| 1991/92 | Alajuelense | Saprissa |
| 1992/93 | Herediano | Cartaginés |
| 1993/94 | Saprissa | Alajuelense |
| 1994/95 | Saprissa | Alajuelense |
| 1995/96 | Alajuelense | Cartaginés |
| 1996/97 | Alajuelense | Saprissa |
| 1997/98 | Saprissa | Alajuelense |
| 1998/99 | Saprissa | Alajuelense |
| 1999/00 | Alajuelense | Saprissa |
| 2000/01 | Alajuelense | Herediano |
| 2001/02 | Alajuelense | Santos de Guápiles |
| 2002/03 | Alajuelense | Saprissa |
| 2003/04 | Saprissa | Herediano |
| 2004/05 | Alajuelense | Pérez Zeledón |
| 2005/06 | Saprissa | Puntarenas FC |
| 2006/07 | Saprissa | Alajuelense |
| 2007 Apertura | Saprissa | Herediano |
| 2008 Clausura | Saprissa | Alajuelense |
| 2008 Apertura | Saprissa | Alajuelense |
| 2009 Clausura | Municipal Liberia | Herediano |
| 2009 Apertura | Brujas de Escazú | Puntarenas FC |
| 2010 Clausura | Saprissa | San Carlos |
| 2010 Apertura | Alajuelense | Herediano |
| 2011 Clausura | Alajuelense | San Carlos |
| 2011 Apertura | Alajuelense | Herediano |
| 2012 Clausura | Herediano | Santos de Guápiles |
| 2012 Apertura | Alajuelense | Herediano |
| 2013 Clausura | Herediano | Cartaginés |
| 2013 Apertura | Alajuelense | Herediano |
| 2014 Clausura | Saprissa | Alajuelense |
| 2014 Apertura | Saprissa | Herediano |
| 2015 Clausura | Herediano | Alajuelense |
| 2015 Apertura | Saprissa | Alajuelense |
| 2016 Clausura | Herediano | Alajuelense |
| 2016 Apertura | Saprissa | Herediano |
| 2017 Clausura | Herediano | Saprissa |
| 2017 Apertura | Pérez Zeledón | Herediano |
| 2018 Clausura | Saprissa | Herediano |
| 2018 Apertura | Herediano | Saprissa |
| 2019 Clausura | San Carlos | Saprissa |
| 2019 Apertura | Herediano | Alajuelense |
| 2020 Clausura | Saprissa | Alajuelense |
| 2020 Apertura | Alajuelense | Herediano |
| 2021 Clausura | Saprissa | Herediano |
| 2021 Apertura | Herediano | Saprissa |
| 2022 Clausura | Cartaginés | Alajuelense |
| 2022 Apertura | Saprissa | Herediano |
| 2023 Clausura | Saprissa | Alajuelense |
| 2023 Apertura | Saprissa | Herediano |
| 2024 Clausura | Saprissa | Alajuelense |
| 2024 Apertura | Herediano | Alajuelense |
| 2025 Clausura | Herediano | Alajuelense |
| 2025 Apertura | Alajuelense | Saprissa |
| 2026 Clausura | Herediano | Saprissa |

**Rebaixados marcados na classificação:** 42 em 35 edições (só onde a tabela publicada marca a queda); quem mais caiu: Uruguay de Coronado (5), La Libertad (3), Turrialba (3), Herediano (2), Cartaginés (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1988/89: Saprissa +1
- 1995/96: Sagrada Familia -1
- 2000/01: Herediano +1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/crc-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 1)

- **1999/00 · cos00:123:** [vale o placar de campo] San Carlos x Limonense interrompido em 17/10 (1-0, mau tempo) e jogado de novo: 1-1, o placar que vale (a tabela conta o jogo); o San Carlos x Limonense da linha 442 é o do 2º turno, não a repetição

### Divergências entre fontes já explicadas (`EXPLICACOES`, 2)

- **2002/03:** San Carlos x Herediano (21ª rodada do Clausura) foi dado como derrota sem gols para os dois clubes; o banco não tem como registrar isso no jogo (fica sem placar), e a tabela publicada conta uma derrota a mais para cada um
- **2003/04:** falta um Pérez Zeledón x Carmelita no Apertura (a página só tem o jogo de ida, 3-0); pela tabela, a volta foi empate 1-1

### Identidade dos clubes

Regras em `coleta/crc-1/clubes_crc.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão da Costa Rica: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Saprissa, Alajuelense, Herediano, Cartaginés), com as grafias de cada época ("LD
  Alajuelense", "L.D.Alajuela", "Alajuela" nos anos 1990; "CS Herediano", "Heredia"; "Cartago");
- o mesmo clube com outro nome, como na lista de campeões da RSSSF: Carmen FC / El Carmen = Carmelita; CS Uruguay = Uruguay de
  Coronado; Univ. de Costa Rica / UCR / Universidad = Universidad de Costa Rica; A.D. Belemita / Belén Siglo XXI / Belén FC =
  Belén; San Ramón = Ramonense; Guanacaste = Guanacasteca; Liberia Mía (2004-2012, o nome do AD Municipal Liberia
  nesses anos; campeão do Clausura 2009) = Municipal Liberia;
- clubes diferentes: Municipal Puntarenas (até 2003) e Puntarenas FC (2004 em diante), contados à parte na lista de campeões;
  Gimnástica Limonense (1921), Limonense (AD Limonense, 1964-2001), Municipal Limón (1980-1983), Limón Northern (1984-1988) e
  Limón FC (2010 em diante); Alajuela Junior (1933-1936) e Alajuelense;
- homônimo de clube do banco ou de outro pacote leva a cidade: Santos de Guápiles, Sporting de San José, Uruguay de Coronado,
  Progreso de San José, Paraíso de Cartago.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (74):** de 1921 a 1995/96 a RSSSF traz quase só as tabelas (a edição entra com elas, com campeão e vice; os poucos jogos de final ficam de fora); 1991/92 e 1993/94 não têm página (só campeão e vice da lista).
- **Edições com jogos incompletos (4):** Apertura 2010, Clausura 2011, Apertura 2011 e Clausura 2012: a RSSSF só tem a tabela da fase regular e a fase final; a ESPN desses anos tem jogos adiados repetidos e jogos faltando, e não foi usada.
- **Edições sem jogos** (74): 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1955, 1957, 1958, 1959, 1960, 1961 Asofútbol, 1961 Federación, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1921 a 1995/96 só com as tabelas (a RSSSF não tem os jogos; os poucos jogos de final ficaram de fora); 1991/92 e 1993/94 sem página (só campeão e vice). Fonte que resolveria: jornais da época (La Nación, Diario de Costa Rica) ou a UNAFUT.
- Apertura 2010 a Clausura 2012: fase regular só com a tabela; a ESPN desses anos tem jogos adiados repetidos e jogos faltando.
- Autores dos gols e cartões: a RSSSF quase não traz autores e a ESPN (crc.1) só traz gols, e em poucos anos; não há cartões. Fonte que resolveria: o site da UNAFUT ou o ogol.
- Erros de um resultado na própria página em 1998/99 e 2000/01; derrota para os dois clubes em 2002/03 (San Carlos x Herediano); um jogo faltando em 2003/04: explicados no relatório.

## 10. Arquivos e comandos

Código em `coleta/crc-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga crc.1) de 2004 a 2026 para data/coleta/crc-1/espn/crc1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão da Costa Rica para data/coleta/crc-1/rsssf/: a lista de campeões (coschamp.html), |
| `clubes_crc.py` | Identidade dos clubes da 1ª divisão da Costa Rica: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão da Costa Rica (crc-1): uma por título, como na lista de campeões da RSSSF (tablesc/coschamp.html), |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão da Costa Rica, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão da Costa Rica e grava o pacote em data/coleta/crc-1/pacote/ e o relatório em docs/coleta/crc-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão da Costa Rica nas páginas da RSSSF (data/coleta/crc-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado na Costa Rica). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/crc-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/crc-1/pacote/`; relatório: `docs/coleta/crc-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/crc-1/baixar_espn.py
python coleta/crc-1/baixar_rsssf.py
python coleta/crc-1/importar.py
python coleta/crc-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py crc-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

