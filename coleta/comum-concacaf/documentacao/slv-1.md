# Campeonato Salvadorenho (`slv-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/slv-1/pacote/`, do código `coleta/slv-1/` e do relatório `docs/coleta/slv-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 111, de 1926 a 2026 Clausura; 52 sem jogos.
- **Jogos:** 6026 (6015 com placar); **gols:** 15505; **gols com autor:** 2788 (18%); **cartões:** 0.
- **Clubes:** 71; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 111 edições; **tabelas publicadas guardadas para conferência:** 1203 linhas.
- **No banco:** sim; **último commit do pacote:** 85c4da52.
- **Observação da competição:** Primera División de El Salvador de 1926 ao Clausura 2026, uma edição por título, como a lista da RSSSF (110 títulos): de 1926 a 1946 o campeonato nacional entre os campeões das zonas (final ou quadrangular); um campeão por temporada de 1948/49 a 1998/99; Apertura e Clausura de 1999/00 em diante (Clausura 2023 sem campeão). Até 1995/96 só as tabelas e as finais. Ficam fora 1924-25 (não oficiais), os títulos só da Zona Central (1931-36, 1939-41, 1944-45) e a Copa Pilsener 1998/99.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão de El Salvador (slv-1): uma edição por título, como na lista de campeões da RSSSF
(tablese/elsalchamp.html, 110 títulos desde 1926), que é a contagem que a imprensa de lá usa. Escopo decidido em 24/11/2026:

- 1926 a 1946: os campeonatos nacionais oficiais (1926, 1927, 1928, 1929/30, 1937, 1938, 1942, 1943, 1946): final, ou
  quadrangular, entre os campeões das zonas; ficam fora 1924 e 1925 (não oficiais, pela própria RSSSF), os títulos só da
  Zona Central (1931-36, 1939-41, 1944-45) e 1947 (parou depois de duas rodadas, sem tabela);
- 1948/49 a 1997/98: um campeão por temporada (os anos sem campeonato não têm edição);
- 1998/99: só o Clausura ("Copa Clima"), que deu o título; a Copa Pilsener (Apertura) não é título oficial;
- 1999/00 em diante: Apertura e Clausura, uma edição cada ("1999 Apertura", "2000 Clausura"). O Clausura 2023 (cancelado
  depois da tragédia no estádio Cuscatlán) entra sem campeão.

Fontes de cada edição: até 1985/86 a página de tabelas finais (elsalhist.html, uma seção por temporada); de 1986/87 em
diante a página da temporada quando existe (o título diz a temporada: "El Salvador 1999/2000"). A edição entra só com as
tabelas quando o trecho tem menos de 90% dos jogos.
```

**Edições:** 111, uma por título, como a lista de campeões da RSSSF (`elsalchamp.html`, 110 títulos desde 1926), que é a contagem da imprensa salvadorenha (FAS 20, Alianza 18, Águila 17). Escopo decidido em 24/11/2026: de 1926 a 1946 os nove campeonatos nacionais oficiais (final, ou quadrangular, entre os campeões das zonas); ficam fora 1924 e 1925 (torneios da Semana Deportiva que a RSSSF chama de não oficiais), os títulos só da Zona Central (1931-36, 1939-41 e 1944-45, que a tradição às vezes conta como nacionais), 1947 (parou depois de duas rodadas, sem tabela) e a Copa Pilsener 1998/99 (não é título oficial). Um campeão por temporada de 1948/49 a 1998/99 (em 1998/99, o Clausura); Apertura e Clausura de 1999/00 em diante, uma edição cada; o Clausura 2023 (cancelado nas quartas de final depois da tragédia no estádio Cuscatlán) entra sem campeão.

**Fontes:** RSSSF (`data/coleta/slv-1/rsssf/`: a lista de campeões, a página de tabelas finais e as páginas das temporadas, casadas pelo título) e ESPN (liga `slv.1`).

**Clubes:** nomes e identidades no começo de `coleta/slv-1/clubes_slv.py`. Homônimos de clubes de outros países levam o país ou a cidade: Hércules de El Salvador, Libertad de El Salvador, España de El Salvador, Atlante de El Salvador, Internacional de El Salvador, Excélsior de Santa Ana, Platense de Zacatecoluca, Independiente de San Vicente, Alianza, Leones, Once Deportivo, San Luis, Santa Clara e Tiburones "de El Salvador".

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 51.
- **Edições com alguma tabela divergente** (1; motivo no relatório, na edição): 2002 Clausura.
- **Edições sem tabela para conferir** (59): 1926, 1927, 1928, 1929/30, 1937, 1938, 1942, 1943, 1946, 1948/49, 1950/51, 1951/52, 1952/53, 1953/54, 1955, 1955/56, 1956/57, 1957/58, 1959, 1960/61, 1961/62, 1962, 1963/64, 1964, 1965/66, 1966/67, 1967/68, 1968/69, 1970, 1971, 1972, 1973, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1980/81, 1981, 1982, 1983, 1984, 1985, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 2009 Clausura, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Edições com menos jogos que o esperado:** 2000 Apertura (96 de 95), 2009 Apertura (97 de 96), 2014 Apertura (96 de 95), 2023 Apertura (146 de 145), 2025 Apertura (146 de 145).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 4 | 7 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 2 | 8 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 4 | 0 | — | — | — | — | — | — | — | — |
| 1950s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 515 | 98% | 0% | 97% | 0% | 0% | 0% | 1% | 0.0 |
| 2000s | 20 | 1908 | 91% | 28% | 100% | 20% | 0% | 0% | 27% | 0.0 |
| 2010s | 20 | 1971 | 100% | 96% | 100% | 79% | 46% | 0% | 28% | 0.0 |
| 2020s | 13 | 1617 | 100% | 97% | 100% | 97% | 90% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1926 a 1929/30: 2 clubes
- 1937 a 1942: 4 clubes
- 1943 a 1946: 3 clubes
- 1948/49: 13 clubes
- 1950/51: 10 clubes
- 1951/52 a 1953/54: 8 clubes
- 1955 a 1955/56: 10 clubes
- 1956/57: 9 clubes
- 1957/58: 11 clubes
- 1959 a 1974/75: 10 clubes
- 1975/76: 12 clubes
- 1976/77: 8 clubes
- 1977/78: 12 clubes
- 1978/79: 13 clubes
- 1979/80: 12 clubes
- 1980/81: 11 clubes
- 1981: 10 clubes
- 1982: 11 clubes
- 1983 a 1985: 10 clubes
- 1986/87: 12 clubes
- 1987/88 a 2015 Clausura: 10 clubes
- 2015 Apertura a 2024 Clausura: 12 clubes
- 2024 Apertura a 2025 Clausura: 11 clubes
- 2025 Apertura a 2026 Clausura: 12 clubes

**Pontos por vitória:**

- 1926 a 1994/95: 2
- 1995/96 a 2026 Clausura: 3

**Nome oficial:**

- 1926 a 1946: Campeonato Nacional de El Salvador <ano>
- 1948/49 a 1998/99: Primera División de El Salvador <ano>
- 1999 Apertura: Primera División de El Salvador Apertura <ano>
- 2000 Clausura: Primera División de El Salvador Clausura <ano>
- 2000 Apertura: Primera División de El Salvador Apertura <ano>
- 2001 Clausura: Primera División de El Salvador Clausura <ano>
- 2001 Apertura: Primera División de El Salvador Apertura <ano>
- 2002 Clausura: Primera División de El Salvador Clausura <ano>
- 2002 Apertura: Primera División de El Salvador Apertura <ano>
- 2003 Clausura: Primera División de El Salvador Clausura <ano>
- 2003 Apertura: Primera División de El Salvador Apertura <ano>
- 2004 Clausura: Primera División de El Salvador Clausura <ano>
- 2004 Apertura: Primera División de El Salvador Apertura <ano>
- 2005 Clausura: Primera División de El Salvador Clausura <ano>
- 2005 Apertura: Primera División de El Salvador Apertura <ano>
- 2006 Clausura: Primera División de El Salvador Clausura <ano>
- 2006 Apertura: Primera División de El Salvador Apertura <ano>
- 2007 Clausura: Primera División de El Salvador Clausura <ano>
- 2007 Apertura: Primera División de El Salvador Apertura <ano>
- 2008 Clausura: Primera División de El Salvador Clausura <ano>
- 2008 Apertura: Primera División de El Salvador Apertura <ano>
- 2009 Clausura: Primera División de El Salvador Clausura <ano>
- 2009 Apertura: Primera División de El Salvador Apertura <ano>
- 2010 Clausura: Primera División de El Salvador Clausura <ano>
- 2010 Apertura: Primera División de El Salvador Apertura <ano>
- 2011 Clausura: Primera División de El Salvador Clausura <ano>
- 2011 Apertura: Primera División de El Salvador Apertura <ano>
- 2012 Clausura: Primera División de El Salvador Clausura <ano>
- 2012 Apertura: Primera División de El Salvador Apertura <ano>
- 2013 Clausura: Primera División de El Salvador Clausura <ano>
- 2013 Apertura: Primera División de El Salvador Apertura <ano>
- 2014 Clausura: Primera División de El Salvador Clausura <ano>
- 2014 Apertura: Primera División de El Salvador Apertura <ano>
- 2015 Clausura: Primera División de El Salvador Clausura <ano>
- 2015 Apertura: Primera División de El Salvador Apertura <ano>
- 2016 Clausura: Primera División de El Salvador Clausura <ano>
- 2016 Apertura: Primera División de El Salvador Apertura <ano>
- 2017 Clausura: Primera División de El Salvador Clausura <ano>
- 2017 Apertura: Primera División de El Salvador Apertura <ano>
- 2018 Clausura: Primera División de El Salvador Clausura <ano>
- 2018 Apertura: Primera División de El Salvador Apertura <ano>
- 2019 Clausura: Primera División de El Salvador Clausura <ano>
- 2019 Apertura: Primera División de El Salvador Apertura <ano>
- 2020 Clausura: Primera División de El Salvador Clausura <ano>
- 2020 Apertura: Primera División de El Salvador Apertura <ano>
- 2021 Clausura: Primera División de El Salvador Clausura <ano>
- 2021 Apertura: Primera División de El Salvador Apertura <ano>
- 2022 Clausura: Primera División de El Salvador Clausura <ano>
- 2022 Apertura: Primera División de El Salvador Apertura <ano>
- 2023 Clausura: Primera División de El Salvador Clausura <ano>
- 2023 Apertura: Primera División de El Salvador Apertura <ano>
- 2024 Clausura: Primera División de El Salvador Clausura <ano>
- 2024 Apertura: Primera División de El Salvador Apertura <ano>
- 2025 Clausura: Primera División de El Salvador Clausura <ano>
- 2025 Apertura: Primera División de El Salvador Apertura <ano>
- 2026 Clausura: Primera División de El Salvador Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1926 a 1928: mata-mata
- 1929/30: mata-mata + desempate
- 1937 a 1938: mata-mata + pontos corridos + mata-mata
- 1942 a 1995/96: sem jogos (só a tabela final)
- 1996/97: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1997/98 a 2001 Apertura: pontos corridos + mata-mata
- 2002 Clausura a 2002 Apertura: pontos corridos + desempate + mata-mata
- 2003 Clausura: pontos corridos + mata-mata
- 2003 Apertura: pontos corridos + desempate + mata-mata
- 2004 Clausura: pontos corridos + mata-mata
- 2004 Apertura: pontos corridos + desempate + mata-mata
- 2005 Clausura a 2006 Clausura: pontos corridos + mata-mata
- 2006 Apertura: pontos corridos + desempate + mata-mata
- 2007 Clausura: pontos corridos + mata-mata
- 2007 Apertura: pontos corridos + desempate + mata-mata
- 2008 Clausura a 2009 Clausura: pontos corridos + mata-mata
- 2009 Apertura: pontos corridos + desempate + mata-mata
- 2010 Clausura: pontos corridos + mata-mata
- 2010 Apertura a 2012 Clausura: sem jogos (só a tabela final)
- 2012 Apertura: pontos corridos + mata-mata
- 2013 Clausura: pontos corridos + desempate + mata-mata
- 2013 Apertura a 2014 Clausura: pontos corridos + mata-mata + desempate + mata-mata
- 2014 Apertura: pontos corridos + mata-mata
- 2015 Clausura: pontos corridos + mata-mata + desempate + mata-mata
- 2015 Apertura a 2019 Apertura: pontos corridos + mata-mata
- 2020 Clausura: pontos corridos
- 2020 Apertura a 2021 Clausura: 3 grupos + pontos corridos + mata-mata
- 2021 Apertura a 2022 Clausura: pontos corridos + mata-mata
- 2022 Apertura: 2 grupos + mata-mata
- 2023 Clausura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1929/30: Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1937: Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (liga); Final (mata_mata, jogo_unico)
- 1938: Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (liga); Final (mata_mata, jogo_unico)
- 1996/97: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (liga); Final (mata_mata, ida_volta)
- 1997/98: Primeira fase (liga); Segunda fase (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1998/99: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1999 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2001 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002 Clausura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2003 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2003 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2004 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2004 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2005 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2005 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2006 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2006 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2007 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2007 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2008 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2008 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2009 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2009 Apertura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2010 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2012 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013 Clausura: Primeira fase (liga); Desempate do 4º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2014 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2014 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2015 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2015 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2016 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2016 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2017 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2017 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2018 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2018 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2019 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2019 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2020 Apertura: Primeira fase (grupos, 3 grupos); Segunda fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2021 Clausura: Primeira fase (grupos, 3 grupos); Segunda fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2021 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2022 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2022 Apertura: Primeira fase (grupos, 2 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2023 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2024 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2024 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2025 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2025 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2026 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 104 edições
- calculada: 7 edições

**Observações das edições:**

- 1926: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1927: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1928: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1929/30: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1937: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1938: final entre os campeões das zonas (Semana Deportiva até 1929/30)
- 1942: quadrangular entre os campeões das zonas: a RSSSF só tem a tabela
- 1943: quadrangular entre os campeões das zonas: a RSSSF só tem a tabela
- 1946: quadrangular entre os campeões das zonas: a RSSSF só tem a tabela
- 1948/49: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1950/51: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1951/52: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1952/53: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1953/54: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1955: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1955/56: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1956/57: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1957/58: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1959: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1960/61: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1961/62: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1962: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1963/64: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1964: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1965/66: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1966/67: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1967/68: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1968/69: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1970: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1971: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1972: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1973: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1974/75: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1975/76: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1976/77: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1977/78: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1978/79: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1979/80: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1980/81: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1981: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1982: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1983: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1984: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1985: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1986/87: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1987/88: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1988/89: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1989/90: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1990/91: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1991/92: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1992/93: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1993/94: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1994/95: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1995/96: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1996/97: o repechaje Municipal Limeño x Real Independiente (vaga na 1ª divisão, contra clube da 2ª) fica fora
- 1998/99: só o Clausura ("Copa Clima"), que deu o título; a Copa Pilsener (Apertura) não é título oficial
- 2010 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2012 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2022 Apertura: as duas rodadas de julho foram anuladas (campeonato parado pela investigação contra a federação e recomeçado em setembro): ficam fora, com a tabela do momento da parada
- 2023 Clausura: torneio cancelado nas quartas de final depois da tragédia no estádio Cuscatlán (20/05/2023), sem título; a classificação é a da fase regular

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- FAS: 20
- Alianza de El Salvador: 18
- Águila: 17
- Luis Ángel Firpo: 11
- Isidro Metapán: 10
- Atlético Marte: 8
- Santa Tecla FC: 4
- Hércules de El Salvador: 3
- Dragón: 3
- CD 33: 2
- Quequeisque: 2
- Once Municipal: 2
- Juventud Olímpica: 2
- Once Deportivo de El Salvador: 2
- Chinameca: 1
- Libertad de El Salvador: 1
- Platense de Zacatecoluca: 1
- Santiagueño: 1
- San Salvador FC: 1
- Vista Hermosa: 1
- Sem campeão: 2023 Clausura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1926 | Chinameca | Nequepio |
| 1927 | Hércules de El Salvador | Chinameca |
| 1928 | Hércules de El Salvador | Excélsior de Santa Ana |
| 1929/30 | Hércules de El Salvador | Excélsior de Santa Ana |
| 1937 | CD 33 | Alacranes |
| 1938 | CD 33 | Maya |
| 1942 | Quequeisque | Juventud Olímpica |
| 1943 | Quequeisque | Ferrocarril |
| 1946 | Libertad de El Salvador | Once Municipal |
| 1948/49 | Once Municipal | Libertad de El Salvador |
| 1950/51 | Dragón | FAS |
| 1951/52 | FAS | Leones de El Salvador |
| 1952/53 | Dragón | Juventud Olímpica |
| 1953/54 | FAS | Dragón |
| 1955 | Atlético Marte | Dragón |
| 1955/56 | Atlético Marte | Luis Ángel Firpo |
| 1956/57 | Atlético Marte | Atlante de El Salvador |
| 1957/58 | FAS | Once Municipal |
| 1959 | Águila | FAS |
| 1960/61 | Águila | FAS |
| 1961/62 | FAS | Águila |
| 1962 | FAS | Atlante de El Salvador |
| 1963/64 | Águila | Juventud Olímpica |
| 1964 | Águila | FAS |
| 1965/66 | Alianza de El Salvador | Universidad de El Salvador |
| 1966/67 | Alianza de El Salvador | Águila |
| 1967/68 | Águila | FAS |
| 1968/69 | Atlético Marte | FAS |
| 1970 | Atlético Marte | FAS |
| 1971 | Juventud Olímpica | Alianza de El Salvador |
| 1972 | Águila | Juventud Olímpica |
| 1973 | Juventud Olímpica | Alianza de El Salvador |
| 1974/75 | Platense de Zacatecoluca | Negocios Internacionales |
| 1975/76 | Águila | Alianza de El Salvador |
| 1976/77 | Águila | Once Municipal |
| 1977/78 | FAS | Once Municipal |
| 1978/79 | FAS | Alianza de El Salvador |
| 1979/80 | Santiagueño | Águila |
| 1980/81 | Atlético Marte | Santiagueño |
| 1981 | FAS | Independiente de San Vicente |
| 1982 | Atlético Marte | Independiente de San Vicente |
| 1983 | Águila | FAS |
| 1984 | FAS | Águila |
| 1985 | Atlético Marte | Alianza de El Salvador |
| 1986/87 | Alianza de El Salvador | Águila |
| 1987/88 | Águila | Luis Ángel Firpo |
| 1988/89 | Luis Ángel Firpo | Cojutepeque |
| 1989/90 | Alianza de El Salvador | Luis Ángel Firpo |
| 1990/91 | Luis Ángel Firpo | Águila |
| 1991/92 | Luis Ángel Firpo | Alianza de El Salvador |
| 1992/93 | Luis Ángel Firpo | Alianza de El Salvador |
| 1993/94 | Alianza de El Salvador | FAS |
| 1994/95 | FAS | Luis Ángel Firpo |
| 1995/96 | FAS | Luis Ángel Firpo |
| 1996/97 | Alianza de El Salvador | Luis Ángel Firpo |
| 1997/98 | Luis Ángel Firpo | FAS |
| 1998/99 | Luis Ángel Firpo | FAS |
| 1999 Apertura | Águila | Municipal Limeño |
| 2000 Clausura | Luis Ángel Firpo | ADET |
| 2000 Apertura | Águila | Municipal Limeño |
| 2001 Clausura | Águila | FAS |
| 2001 Apertura | Alianza de El Salvador | Luis Ángel Firpo |
| 2002 Clausura | FAS | Alianza de El Salvador |
| 2002 Apertura | FAS | San Salvador FC |
| 2003 Clausura | San Salvador FC | Luis Ángel Firpo |
| 2003 Apertura | FAS | Águila |
| 2004 Clausura | Alianza de El Salvador | FAS |
| 2004 Apertura | FAS | Atlético Balboa |
| 2005 Clausura | FAS | Luis Ángel Firpo |
| 2005 Apertura | Vista Hermosa | Isidro Metapán |
| 2006 Clausura | Águila | FAS |
| 2006 Apertura | Once Municipal | FAS |
| 2007 Clausura | Isidro Metapán | Luis Ángel Firpo |
| 2007 Apertura | Luis Ángel Firpo | FAS |
| 2008 Clausura | Luis Ángel Firpo | FAS |
| 2008 Apertura | Isidro Metapán | Chalatenango |
| 2009 Clausura | Isidro Metapán | Luis Ángel Firpo |
| 2009 Apertura | FAS | Águila |
| 2010 Clausura | Isidro Metapán | Águila |
| 2010 Apertura | Isidro Metapán | Alianza de El Salvador |
| 2011 Clausura | Alianza de El Salvador | FAS |
| 2011 Apertura | Isidro Metapán | Once Municipal |
| 2012 Clausura | Águila | Isidro Metapán |
| 2012 Apertura | Isidro Metapán | Alianza de El Salvador |
| 2013 Clausura | Luis Ángel Firpo | FAS |
| 2013 Apertura | Isidro Metapán | FAS |
| 2014 Clausura | Isidro Metapán | Dragón |
| 2014 Apertura | Isidro Metapán | Águila |
| 2015 Clausura | Santa Tecla FC | Isidro Metapán |
| 2015 Apertura | Alianza de El Salvador | FAS |
| 2016 Clausura | Dragón | Águila |
| 2016 Apertura | Santa Tecla FC | Alianza de El Salvador |
| 2017 Clausura | Santa Tecla FC | Alianza de El Salvador |
| 2017 Apertura | Alianza de El Salvador | Santa Tecla FC |
| 2018 Clausura | Alianza de El Salvador | Santa Tecla FC |
| 2018 Apertura | Santa Tecla FC | Alianza de El Salvador |
| 2019 Clausura | Águila | Alianza de El Salvador |
| 2019 Apertura | Alianza de El Salvador | FAS |
| 2020 Clausura | Once Deportivo de El Salvador | El Vencedor |
| 2020 Apertura | Alianza de El Salvador | Águila |
| 2021 Clausura | FAS | Alianza de El Salvador |
| 2021 Apertura | Alianza de El Salvador | Platense de Zacatecoluca |
| 2022 Clausura | Alianza de El Salvador | Águila |
| 2022 Apertura | FAS | Jocoro |
| 2023 Clausura | — | — |
| 2023 Apertura | Águila | Jocoro |
| 2024 Clausura | Alianza de El Salvador | Municipal Limeño |
| 2024 Apertura | Once Deportivo de El Salvador | FAS |
| 2025 Clausura | Alianza de El Salvador | Municipal Limeño |
| 2025 Apertura | Luis Ángel Firpo | Alianza de El Salvador |
| 2026 Clausura | FAS | Águila |

**Rebaixados marcados na classificação:** 43 em 33 edições (só onde a tabela publicada marca a queda); quem mais caiu: Luis Ángel Firpo (4), Universidad de El Salvador (3), Dragón (3), Leones de El Salvador (2), Independiente de San Vicente (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1973: Juventud Olímpica -1
- 1973: Atlético Marte -1
- 1977/78: FAS +4
- 1977/78: Once Municipal +4
- 1977/78: Alianza de El Salvador +4
- 1977/78: Atlético Marte +2
- 1977/78: Águila +2
- 1977/78: Dragón +2
- 1977/78: Platense de Zacatecoluca +2
- 1977/78: Independiente de San Vicente +2
- 1979/80: Once Municipal -2
- 1982: Águila -3
- 1982: Luis Ángel Firpo -5
- 1983: Atlético Marte -2
- 1990/91: Tiburones de El Salvador -2
- 1990/91: Cojutepeque -1
- 1994/95: FAS +3
- 1994/95: Luis Ángel Firpo +2
- 1994/95: Águila +3
- 1994/95: Atlético Marte +1
- 1994/95: El Roble +1
- 1994/95: ADET +1
- 1994/95: Tiburones de El Salvador +1
- 1994/95: Alianza de El Salvador +1
- 2002 Clausura: Atlético Marte -4
- 2006 Apertura: Once Municipal -1
- 2019 Clausura: Municipal Limeño -6
- 2019 Clausura: Pasaquina -6
- 2019 Clausura: Jocoro -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/slv-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **elsal05 · 379:** «once Municipal 0-3» → «Once Municipal 0-3»: inicial minúscula no nome do mandante: o leitor não lia a linha como jogo (e a tabela fecha com ele)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 1)

- **2002 Clausura:** Atlético Balboa: os jogos da página somam 25 gols sofridos, a tabela publicada diz 24 (um placar da página ou a tabela tem um gol a mais; fica como a página)

### Identidade dos clubes

Regras em `coleta/slv-1/clubes_slv.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão de El Salvador: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (FAS, Alianza FC, Águila, Luis Ángel Firpo, Isidro Metapán, Atlético Marte), com as
  grafias de cada época e as abreviações das páginas ("L.Á. Firpo", "LA Firpo", "Mun Limeno", "S Clara", "Balbao");
- o mesmo clube com outro nome: Atlético Arabe Marte (1996-98, nome do Atlético Marte depois da fusão com o Árabe; a página
  de 1997/98 diz que o da tabela é o de San Salvador) = Atlético Marte; ADET / A.D.E.T. / AD El Tránsito / Baygón ADET;
  Universidad / UES / Univ. de El Salvador = Universidad de El Salvador; Independiente / CS Independiente / Indep. Nacional /
  Nacional 1906 = Independiente de San Vicente (o clube de 1906; o de 1948/49 é presumido o mesmo); Isidro (2001) / Isidro
  Metapán (fusão de 2000 do CD Metapán com o Isidro Menéndez);
- clubes diferentes: CD Metapán (até 1991/92) e Isidro Metapán (2000 em diante); Sonsonate FC (até 1999) e CD Sonsonate (2009
  em diante); Once Municipal, Once Lobos e Once Deportivo; Juventud Olímpica, Santa Anita e Juventud Independiente;
  Quequeisque (Nueva San Salvador, até 1965) e Santa Tecla FC (2007);
- vaga comprada: Inter FA (comprou a vaga do Dragón em 2025) e Hércules (ficou com a vaga do Once Deportivo em 2025) entram
  como clubes próprios; o Hércules de 2025 é tratado como o histórico Hércules renascido (campeão de 1927 a 1929/30);
- Tapachulteca (1975): clube mexicano de Tapachula que jogou a liga salvadorenha naquele ano;
- homônimo de clube do banco ou de outro pacote leva o país ou a cidade: Hércules de El Salvador, Libertad de El Salvador,
  España de El Salvador, Atlante de El Salvador, Internacional de El Salvador, Excélsior de Santa Ana, Platense de
  Zacatecoluca, Independiente de San Vicente, Alianza de El Salvador, Leones de El Salvador, Once Deportivo de El
  Salvador, San Luis de El Salvador, Santa Clara de El Salvador, Tiburones de El Salvador (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (52):** 1942, 1943 e 1946 (quadrangulares só com a tabela), de 1948/49 a 1995/96 (a RSSSF só tem as tabelas e as finais) e do Apertura 2010 ao Clausura 2012 (a página só tem as tabelas e a fase final). O vice é o da lista de campeões.
- **Edições sem jogos** (52): 1942, 1943, 1946, 1948/49, 1950/51, 1951/52, 1952/53, 1953/54, 1955, 1955/56, 1956/57, 1957/58, 1959, 1960/61, 1961/62, 1962, 1963/64, 1964, 1965/66, 1966/67, 1967/68, 1968/69, 1970, 1971, 1972, 1973, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1980/81, 1981, 1982, 1983, 1984, 1985, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Décadas com menos da metade dos gols com autor:** 1920s, 1930s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1920s, 1930s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1942, 1943, 1946 e 1948/49 a 1995/96 só com as tabelas (e o campeão e o vice da lista); as finais desses anos que a RSSSF traz não entram. Fonte que resolveria: jornais da época (La Prensa Gráfica, El Diario de Hoy) ou a FESFUT.
- Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular). A ESPN tem os Aperturas de 2010 e 2011 quase inteiros, mas não fecha com as tabelas (placares diferentes, um jogo faltando, um repetido): não foi usada; os Clausuras ela quase não tem.
- 2002 Clausura: um gol de diferença entre os jogos e a tabela do Atlético Balboa (explicado no relatório).
- Títulos só da Zona Central (1931-36, 1939-41, 1944-45) fora do slv-1 (decisão de 24/11); a tradição às vezes os conta como nacionais.
- 2020/21 (pandemia, duas fases de grupos): a classificação junta os dois grupos da segunda fase (10 jogos por clube).

## 10. Arquivos e comandos

Código em `coleta/slv-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga slv.1) de 2004 a 2026 para data/coleta/slv-1/espn/slv1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão de El Salvador para data/coleta/slv-1/rsssf/: a lista de campeões (elsalchamp.html), as |
| `clubes_slv.py` | Identidade dos clubes da 1ª divisão de El Salvador: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão de El Salvador (slv-1): uma edição por título, como na lista de campeões da RSSSF |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão de El Salvador, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão de El Salvador e grava o pacote em data/coleta/slv-1/pacote/ e o relatório em docs/coleta/slv-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão de El Salvador nas páginas da RSSSF (data/coleta/slv-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado em El Salvador). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/slv-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/slv-1/pacote/`; relatório: `docs/coleta/slv-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/slv-1/baixar_espn.py
python coleta/slv-1/baixar_rsssf.py
python coleta/slv-1/importar.py
python coleta/slv-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py slv-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

