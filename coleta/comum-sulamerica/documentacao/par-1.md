# Campeonato Paraguaio (`par-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/par-1/pacote/`, do código `coleta/par-1/` e do relatório `docs/coleta/par-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 134, de 1906 a 2026 Apertura; 76 sem jogos.
- **Jogos:** 7823 (7807 com placar); **gols:** 20900; **gols com autor:** 13239 (63%); **cartões:** 14271.
- **Clubes:** 50; **artilheiros:** 110 edições com artilheiro (140 linhas, com empates).
- **Classificação final:** 134 edições; **tabelas publicadas guardadas para conferência:** 1483 linhas.
- **No banco:** sim; **último commit do pacote:** a22c1ff5.
- **Observação da competição:** 1ª divisão paraguaia de 1906 a 2025: um campeão por ano até 2007 e uma edição por torneio (Apertura e Clausura) de 2008 em diante. Jogos de 1960-1967, 1981 e 1996 em diante; nos outros anos, só o campeão, o vice e a tabela parcial quando há (nenhuma fonte pública tem os jogos).

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão paraguaia (par-1): uma por torneio que deu título de campeão paraguaio.

Lista de títulos: RSSSF (parachamp.html), conferida com a Wikipédia. De 1906 a 2007 um campeão por ano (sem campeonato em
1908, 1922 e 1932-1934); de 1996 a 2007 o Apertura e o Clausura são fases da edição anual, com a final entre os vencedores.
De 2008 em diante, Apertura e Clausura dão título cada um: uma edição por torneio. Ficam de fora a Copa Paraguay, a
Intermedia (2ª divisão), as liguillas e os jogos de promoção.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO). 1960-1967, 1981 e 1996 em diante.
- sem jogos (1906-1959, 1968-1980, 1982-1995): nenhuma fonte pública tem os jogos completos (pesquisa no relatório). Decisão
  do Guilherme (21/11/2026): a edição entra só com o campeão, o vice e a tabela parcial (posição e pontos) quando a RSSSF a
  traz (parahist.html e as páginas de 1968-1995); os jogos soltos que a RSSSF conhece ("Known Results") ficam de fora.
```

**Edições:** 134, uma por título de campeão paraguaio da 1ª divisão, de 1906 a 2025, como na lista de campeões da RSSSF (`parachamp.html`) e na Wikipédia em inglês. Até 2007 um campeão por ano (sem campeonato em 1908, 1922 e 1932-1934); de 1996 a 2007 o Apertura e o Clausura são fases da edição anual, com a final entre os vencedores. De 2008 em diante, Apertura e Clausura dão título cada um: uma edição por torneio.

**Fontes:** RSSSF (uma página por temporada de 1960 em diante e a história da liga 1906-1959, `parahist.html`, em `data/coleta/par-1/rsssf/`: base de jogos de 1960-1967, 1981 e 1996 em diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas são a conferência); ESPN (liga `par.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol só tem jogos de 2005 em diante e não entrou.

**Clubes:** homônimos de outros países levam a cidade: Nacional de Asunción (o Nacional é o uruguaio), River Plate de Asunción, Sportivo San Lorenzo, Independiente de Campo Grande, Universal de Encarnación; o Guaraní é "Guaraní de Asunción" para não se confundir com o Guarani de Campinas. General Caballero (Zeballos Cué) e General Caballero JLM, e Cerro Porteño e Cerro Porteño PF, são clubes diferentes.

**Regras:** o placar é o da RSSSF. Jogo decidido no tribunal leva o placar dado (`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 45.
- **Edições com alguma tabela divergente** (5; motivo no relatório, na edição): 1965, 1967, 1998, 1999, 2000.
- **Edições sem tabela para conferir** (84): 1906, 1907, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 2008 Clausura, 2009 Apertura, 2017 Apertura, 2022 Clausura, 2023 Clausura.
- **Edições com menos jogos que o esperado:** nenhuma.
- **Edições com mais jogos que o esperado** (desempates e jogos fora da tabela publicada): 1963 (114 de 113), 1965 (76 de 75), 1981 (141 de 140), 2003 (153 de 152), 2005 (181 de 180), 2007 (267 de 266).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 3 | 0 | — | — | — | — | — | — | — | — |
| 1910s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1920s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1930s | 7 | 0 | — | — | — | — | — | — | — | — |
| 1940s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1950s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 10 | 826 | 100% | 0% | 100% | 30% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 141 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 687 | 69% | 0% | 100% | 0% | 0% | 0% | 1% | 0.0 |
| 2000s | 12 | 1952 | 97% | 55% | 100% | 56% | 55% | 0% | 80% | 1.8 |
| 2010s | 20 | 2642 | 100% | 100% | 100% | 100% | 98% | 13% | 81% | 2.3 |
| 2020s | 13 | 1575 | 100% | 91% | 100% | 87% | 87% | 16% | 86% | 3.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1906: 5 clubes
- 1907: 0 clubes
- 1909: 6 clubes
- 1910: 0 clubes
- 1911: 6 clubes
- 1912: 4 clubes
- 1913: 5 clubes
- 1914 a 1915: 6 clubes
- 1916: 7 clubes
- 1917: 3 clubes
- 1918: 9 clubes
- 1919: 2 clubes
- 1920: 10 clubes
- 1921: 9 clubes
- 1923: 10 clubes
- 1924: 9 clubes
- 1925: 2 clubes
- 1926: 9 clubes
- 1927 a 1929: 10 clubes
- 1930: 2 clubes
- 1931: 0 clubes
- 1935: 10 clubes
- 1936 a 1938: 11 clubes
- 1939: 5 clubes
- 1940 a 1941: 11 clubes
- 1942 a 1943: 10 clubes
- 1944: 3 clubes
- 1945 a 1948: 10 clubes
- 1949 a 1954: 11 clubes
- 1955: 9 clubes
- 1956: 0 clubes
- 1957 a 1958: 8 clubes
- 1959 a 1960: 10 clubes
- 1961 a 1963: 11 clubes
- 1964: 10 clubes
- 1965 a 1967: 9 clubes
- 1968: 0 clubes
- 1969: 3 clubes
- 1970 a 1980: 0 clubes
- 1981: 10 clubes
- 1982: 2 clubes
- 1983 a 1985: 0 clubes
- 1986 a 1987: 10 clubes
- 1988: 8 clubes
- 1989: 1 clubes
- 1990: 12 clubes
- 1991: 8 clubes
- 1992 a 1993: 12 clubes
- 1994: 20 clubes
- 1995 a 1997: 13 clubes
- 1998: 12 clubes
- 1999: 11 clubes
- 2000 a 2005: 10 clubes
- 2006: 11 clubes
- 2007 a 2020 Clausura: 12 clubes
- 2021 Apertura a 2021 Clausura: 10 clubes
- 2022 Apertura a 2026 Apertura: 12 clubes

**Pontos por vitória:**

- 1906 a 1994: 2
- 1995 a 2026 Apertura: 3

**Nome oficial:**

- 1906 a 1931: Liga Paraguaya de Fútbol – Campeonato <ano>
- 1935 a 2007: Campeonato Paraguayo de Primera División <ano>
- 2008 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2008 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2009 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2009 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2010 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2010 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2011 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2011 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2012 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2012 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2013 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2013 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2014 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2014 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2015 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2015 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2016 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2016 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2017 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2017 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2018 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2018 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2019 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2019 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2020 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2020 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2021 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2021 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2022 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2022 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2023 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2023 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2024 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2024 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2025 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura
- 2025 Clausura: Campeonato Paraguayo de Primera División <ano> – Clausura
- 2026 Apertura: Campeonato Paraguayo de Primera División <ano> – Apertura

**Formato** (fases na ordem, do edicoes.csv):

- 1906 a 1959: sem jogos (só a tabela final)
- 1960: pontos corridos
- 1961: pontos corridos + desempate
- 1962: pontos corridos
- 1963: pontos corridos + desempate
- 1964: pontos corridos
- 1965: pontos corridos + desempate
- 1966: pontos corridos
- 1967: pontos corridos + desempate
- 1968 a 1980: sem jogos (só a tabela final)
- 1981: 2 grupos + mata-mata + pontos corridos + mata-mata + desempate
- 1982 a 1995: sem jogos (só a tabela final)
- 1996: pontos corridos + 2 grupos + mata-mata + pontos corridos + 2 grupos + mata-mata
- 1997: pontos corridos + 2 grupos + mata-mata + pontos corridos + mata-mata + desempate
- 1998: pontos corridos + mata-mata + pontos corridos + mata-mata + desempate
- 1999: pontos corridos + mata-mata + pontos corridos + mata-mata + desempate + mata-mata
- 2000: 2 grupos + pontos corridos + mata-mata
- 2001: pontos corridos + mata-mata + pontos corridos
- 2002: pontos corridos + mata-mata + pontos corridos + desempate
- 2003: pontos corridos + mata-mata + pontos corridos + mata-mata + pontos corridos + desempate
- 2004 a 2005: pontos corridos
- 2006: pontos corridos + desempate
- 2007: pontos corridos + mata-mata
- 2008 Apertura a 2015 Apertura: pontos corridos
- 2015 Clausura: pontos corridos + desempate
- 2016 Apertura a 2020 Apertura: pontos corridos
- 2020 Clausura: pontos corridos + mata-mata
- 2021 Apertura a 2026 Apertura: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1961: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta); Desempate do título (mata_mata, ida_volta)
- 1963: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1965: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1967: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta)
- 1981: Primeira fase (grupos, 2 grupos); Semifinal do 1º turno (mata_mata, jogo_unico); Final do 1º turno (mata_mata, jogo_unico); Segunda fase (liga); Triangular de desempate (mata_mata, ida_volta); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1996: Apertura (liga); Segunda fase do Apertura (grupos, 2 grupos); Semifinal do Apertura (mata_mata, jogo_unico); Final do Apertura (mata_mata, jogo_unico); Clausura (liga); Segunda fase do Clausura (grupos, 2 grupos); Semifinal do Clausura (mata_mata, jogo_unico); Final do Clausura (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1997: Apertura (liga); Segunda fase do Apertura (grupos, 2 grupos); Semifinal do Apertura (mata_mata, jogo_unico); Final do Apertura (mata_mata, jogo_unico); Clausura (liga); Segunda fase do Clausura (liga); Semifinal do Clausura (mata_mata, jogo_unico); Final do Clausura (mata_mata, jogo_unico); Desempate do título (mata_mata, ida_volta)
- 1998: Apertura (liga); Liguilla do Apertura (liga); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Liguilla do Clausura (liga); Semifinal do Clausura (mata_mata, ida_volta); Final do Clausura (mata_mata, ida_volta); Desempate do título (mata_mata, ida_volta)
- 1999: Apertura (liga); Liguilla do Apertura (liga); Semifinal do Apertura (mata_mata, jogo_unico); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Liguilla do Clausura (liga); Semifinal do Clausura (mata_mata, jogo_unico); Final do Clausura (mata_mata, ida_volta); Desempate do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2000: Primeira fase (grupos, 2 grupos); Clausura (liga); Quadrangulares semifinais (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2001: Apertura (liga); Quartas de final do Apertura (mata_mata, ida_volta); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga)
- 2002: Apertura (liga); Quartas de final do Apertura (mata_mata, ida_volta); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Desempate do título (mata_mata, ida_volta)
- 2003: Apertura (liga); Quadrangulares semifinais do Apertura (mata_mata, jogo_unico); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Liguilla pré-Libertadores (liga); Desempate do 2º lugar (mata_mata, ida_volta)
- 2004: Apertura (liga); Clausura (liga)
- 2005: Apertura (liga); Clausura (liga)
- 2006: Apertura (liga); Clausura (liga); Desempate do título (mata_mata, ida_volta)
- 2007: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2015 Clausura: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 2020 Clausura: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 95 edições
- lista de campeões e vices da RSSSF: 29 edições
- calculada: 10 edições

**Observações das edições:**

- 1906: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1907: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1909: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1910: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1911: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1912: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1913: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1914: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1915: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1916: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1917: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1918: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1919: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1920: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1921: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1923: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1924: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1925: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1926: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1927: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1928: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1929: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1930: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1931: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1935: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1936: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1937: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1938: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1939: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1940: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1941: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1942: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1943: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1944: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1945: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1946: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1947: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1948: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1949: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1950: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1951: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1952: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1953: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1954: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1955: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1956: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1957: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1958: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1959: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1968: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1969: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1970: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1971: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1972: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1973: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1974: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1975: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1976: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1977: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1978: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1979: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1980: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1982: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1983: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1984: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1985: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1986: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1987: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1988: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1989: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1990: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1991: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1992: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1993: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1994: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)
- 1995: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e, quando há, a tabela parcial)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Olimpia: 48
- Cerro Porteño: 35
- Libertad: 26
- Guaraní de Asunción: 11
- Nacional de Asunción: 9
- Sportivo Luqueño: 2
- Sol de América: 2
- Presidente Hayes: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1906 | Guaraní de Asunción | Olimpia |
| 1907 | Guaraní de Asunción | Olimpia |
| 1909 | Nacional de Asunción | Libertad |
| 1910 | Libertad | Atlántida |
| 1911 | Nacional de Asunción | Atlántida |
| 1912 | Olimpia | Sol de América |
| 1913 | Cerro Porteño | Sol de América |
| 1914 | Olimpia | Cerro Porteño |
| 1915 | Cerro Porteño | Olimpia |
| 1916 | Olimpia | Guaraní de Asunción |
| 1917 | Libertad | Olimpia |
| 1918 | Cerro Porteño | Nacional de Asunción |
| 1919 | Cerro Porteño | River Plate de Asunción |
| 1920 | Libertad | Olimpia |
| 1921 | Guaraní de Asunción | Nacional de Asunción |
| 1923 | Guaraní de Asunción | Olimpia |
| 1924 | Nacional de Asunción | Libertad |
| 1925 | Olimpia | Guaraní de Asunción |
| 1926 | Nacional de Asunción | River Plate de Asunción |
| 1927 | Olimpia | Libertad |
| 1928 | Olimpia | Libertad |
| 1929 | Olimpia | Libertad |
| 1930 | Libertad | River Plate de Asunción |
| 1931 | Olimpia | Libertad |
| 1935 | Cerro Porteño | Sol de América |
| 1936 | Olimpia | Atlántida |
| 1937 | Olimpia | Cerro Porteño |
| 1938 | Olimpia | Cerro Porteño |
| 1939 | Cerro Porteño | Olimpia |
| 1940 | Cerro Porteño | Sol de América |
| 1941 | Cerro Porteño | Olimpia |
| 1942 | Nacional de Asunción | Cerro Porteño |
| 1943 | Libertad | Olimpia |
| 1944 | Cerro Porteño | Libertad |
| 1945 | Libertad | Cerro Porteño |
| 1946 | Nacional de Asunción | Sol de América |
| 1947 | Olimpia | Guaraní de Asunción |
| 1948 | Olimpia | Cerro Porteño |
| 1949 | Guaraní de Asunción | Nacional de Asunción |
| 1950 | Cerro Porteño | Libertad |
| 1951 | Sportivo Luqueño | Cerro Porteño |
| 1952 | Presidente Hayes | Libertad |
| 1953 | Sportivo Luqueño | Libertad |
| 1954 | Cerro Porteño | Libertad |
| 1955 | Libertad | Olimpia |
| 1956 | Olimpia | Libertad |
| 1957 | Olimpia | Cerro Porteño |
| 1958 | Olimpia | Cerro Porteño |
| 1959 | Olimpia | Cerro Porteño |
| 1960 | Olimpia | Cerro Porteño |
| 1961 | Cerro Porteño | Olimpia |
| 1962 | Olimpia | Nacional de Asunción |
| 1963 | Cerro Porteño | Olimpia |
| 1964 | Guaraní de Asunción | Nacional de Asunción |
| 1965 | Olimpia | Guaraní de Asunción |
| 1966 | Cerro Porteño | Guaraní de Asunción |
| 1967 | Guaraní de Asunción | Libertad |
| 1968 | Olimpia | Cerro Porteño |
| 1969 | Guaraní de Asunción | Olimpia |
| 1970 | Cerro Porteño | Guaraní de Asunción |
| 1971 | Olimpia | Cerro Porteño |
| 1972 | Cerro Porteño | Olimpia |
| 1973 | Cerro Porteño | Olimpia |
| 1974 | Cerro Porteño | Olimpia |
| 1975 | Olimpia | Sportivo Luqueño |
| 1976 | Libertad | Cerro Porteño |
| 1977 | Cerro Porteño | Libertad |
| 1978 | Olimpia | Sol de América |
| 1979 | Olimpia | Sol de América |
| 1980 | Olimpia | Cerro Porteño |
| 1981 | Olimpia | Sol de América |
| 1982 | Olimpia | Nacional de Asunción |
| 1983 | Olimpia | Sportivo Luqueño |
| 1984 | Guaraní de Asunción | Cerro Porteño |
| 1985 | Olimpia | Nacional de Asunción |
| 1986 | Sol de América | Olimpia |
| 1987 | Cerro Porteño | Olimpia |
| 1988 | Olimpia | Sol de América |
| 1989 | Olimpia | Guaraní de Asunción |
| 1990 | Cerro Porteño | Libertad |
| 1991 | Sol de América | Cerro Porteño |
| 1992 | Cerro Porteño | Libertad |
| 1993 | Olimpia | Cerro Porteño |
| 1994 | Cerro Porteño | Olimpia |
| 1995 | Olimpia | Cerro Porteño |
| 1996 | Cerro Porteño | Guaraní de Asunción |
| 1997 | Olimpia | Cerro Porteño |
| 1998 | Olimpia | Cerro Porteño |
| 1999 | Olimpia | Cerro Porteño |
| 2000 | Olimpia | Guaraní de Asunción |
| 2001 | Cerro Porteño | Sportivo Luqueño |
| 2002 | Libertad | 12 de Octubre |
| 2003 | Libertad | Guaraní de Asunción |
| 2004 | Cerro Porteño | Libertad |
| 2005 | Cerro Porteño | Libertad |
| 2006 | Libertad | Cerro Porteño |
| 2007 | Libertad | Sportivo Luqueño |
| 2008 Apertura | Libertad | Nacional de Asunción |
| 2008 Clausura | Libertad | Guaraní de Asunción |
| 2009 Apertura | Cerro Porteño | Libertad |
| 2009 Clausura | Nacional de Asunción | Libertad |
| 2010 Apertura | Guaraní de Asunción | Cerro Porteño |
| 2010 Clausura | Libertad | Cerro Porteño |
| 2011 Apertura | Nacional de Asunción | Olimpia |
| 2011 Clausura | Olimpia | Cerro Porteño |
| 2012 Apertura | Cerro Porteño | Olimpia |
| 2012 Clausura | Libertad | Nacional de Asunción |
| 2013 Apertura | Nacional de Asunción | Guaraní de Asunción |
| 2013 Clausura | Cerro Porteño | Libertad |
| 2014 Apertura | Libertad | Guaraní de Asunción |
| 2014 Clausura | Libertad | Cerro Porteño |
| 2015 Apertura | Cerro Porteño | Guaraní de Asunción |
| 2015 Clausura | Olimpia | Cerro Porteño |
| 2016 Apertura | Libertad | Olimpia |
| 2016 Clausura | Guaraní de Asunción | Olimpia |
| 2017 Apertura | Libertad | Guaraní de Asunción |
| 2017 Clausura | Cerro Porteño | Olimpia |
| 2018 Apertura | Olimpia | Cerro Porteño |
| 2018 Clausura | Olimpia | Cerro Porteño |
| 2019 Apertura | Olimpia | Cerro Porteño |
| 2019 Clausura | Olimpia | Libertad |
| 2020 Apertura | Cerro Porteño | Olimpia |
| 2020 Clausura | Olimpia | Guaraní de Asunción |
| 2021 Apertura | Libertad | Olimpia |
| 2021 Clausura | Cerro Porteño | Guaraní de Asunción |
| 2022 Apertura | Libertad | Cerro Porteño |
| 2022 Clausura | Olimpia | Cerro Porteño |
| 2023 Apertura | Libertad | Cerro Porteño |
| 2023 Clausura | Libertad | Cerro Porteño |
| 2024 Apertura | Libertad | Cerro Porteño |
| 2024 Clausura | Olimpia | Guaraní de Asunción |
| 2025 Apertura | Libertad | Cerro Porteño |
| 2025 Clausura | Cerro Porteño | Guaraní de Asunción |
| 2026 Apertura | Olimpia | Nacional de Asunción |

**Rebaixados marcados na classificação:** 58 em 31 edições (só onde a tabela publicada marca a queda); quem mais caiu: Sol de América (4), 12 de Octubre (4), Sportivo Trinidense (4), Resistencia (3), River Plate de Asunción (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1961: Nacional de Asunción -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/par-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 4)

- **para2019 · 943:** «Independiente  (Nanawa)» → «Independiente Nanawa»: Copa Paraguay 2019 (par-copa): os dois espaços antes do parêntese partiam o nome do mandante
- **para05 · 572:** «[awarded to Libertad; originally» → «[awarded to Libertad; originally 2-1, Gral. Caballero used suspended player]»: nota quebrada em três linhas (o fim dela ia para o jogo seguinte e o placar de campo para os autores) (PY-029)
- **para05 · 573:** «]      2-1, Gral. Caballero» → «]»: nota quebrada em três linhas (o fim dela ia para o jogo seguinte e o placar de campo para os autores) (PY-029)
- **para05 · 574:** «used suspended player]» → «»: nota quebrada em três linhas (o fim dela ia para o jogo seguinte e o placar de campo para os autores) (PY-029)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 4)

- **1981 · para81:118:** [fase = Semifinal do 1º turno] decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- **1981 · para81:119:** [fase = Semifinal do 1º turno] decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- **1981 · para81:122:** [fase = Final do 1º turno] decisão do 1º turno (dava vaga na final do ano), não a final do campeonato (PY-008)
- **2005 · para05:572:** [wo_v, gm = 2, gv = 1] General Caballero 2-1 em campo; pontos para o Libertad (jogador suspenso); a tabela conta os gols de campo (PY-029)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 6)

- **1935:** artilheiro pela lista da RSSSF (paratops); Pedro Osorio (Cerro Porteño) com 18 gols; a Wikipédia em espanhol dá 17. Sem 3ª fonte: fica a RSSSF (PY-019)
- **1962:** artilheiro pela lista da RSSSF (paratops); Cecilio Martínez (Nacional) com 19 gols; a página do ano na RSSSF dá 18 e a Wikipédia em espanhol, 17 pelo Libertad (ela troca clube e gols com 1963). Três números diferentes: fica a lista da RSSSF (PY-019)
- **1963:** artilheiro pela lista da RSSSF (paratops); Juan Cabañas (Libertad) com 17 gols; a Wikipédia em espanhol dá 19 pelo Nacional (troca clube e gols com 1962). Fica a RSSSF (PY-019)
- **1967:** artilheiro pela lista da RSSSF (paratops); Sebastián Fleitas (Libertad) com 18 gols, como a Wikipédia em espanhol; a página do ano na RSSSF dá 16 (PY-019)
- **1970:** artilheiro pela lista da RSSSF (paratops); Saturnino Arrúa (Cerro Porteño) com 19 gols; a Wikipédia em espanhol dá 11. Fica a RSSSF (PY-019)
- **2003:** artilheiro pela lista da RSSSF (paratops); Erwin Ávalos (Cerro Porteño) com 17 gols; a Wikipédia em espanhol dá 16. Sem 3ª fonte: fica a RSSSF (PY-019)

### Identidade dos clubes

Regras em `coleta/par-1/clubes_par.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes paraguaios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Olimpia", "Cerro Porteño", "Libertad"); o Guaraní vira "Guaraní de
  Asunción" para não se confundir com o Guarani de Campinas;
- homônimo de clube do banco ou de outro pacote leva a cidade: "Nacional de Asunción" (o Nacional é o uruguaio), "River
  Plate de Asunción", "Sportivo San Lorenzo" (o San Lorenzo é o argentino), "Independiente de Campo Grande", "Universal de
  Encarnación";
- clubes diferentes com o mesmo nome: General Caballero (Zeballos Cué) e General Caballero JLM (Juan León Mallorquín);
  Cerro Porteño e Cerro Porteño PF (Presidente Franco).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (76):** 1906-1959, 1968-1980 e 1982-1995. Pesquisamos RSSSF, ogol, Wikipédias em espanhol, inglês e guarani, Transfermarkt, worldfootball, sites e livros paraguaios: nenhuma fonte pública traz os jogos completos desses anos (a RSSSF tem só alguns resultados soltos, "Known Results"). Decisão do Guilherme (21/11/2026): essas edições entram só com o campeão, o vice e a tabela da RSSSF quando há: completa em 1909, 1943, 1945, 1946, 1955, 1986 e 1994 (PY-031); parcial (posição e pontos, às vezes parte da campanha) nos outros anos; sem tabela, a classificação tem só o campeão e o vice. Os jogos soltos ficam de fora.
- **Fora do pacote:** a Copa Paraguay, a Copa República, a Intermedia (2ª divisão), as liguillas e os jogos de promoção.
- **Edições sem jogos** (76): 1906, 1907, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995.
- **Décadas com menos da metade dos gols com autor:** 1960s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1960s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 76 edições sem jogos (1906-1959, 1968-1980, 1982-1995 sem fonte pública): campeão, vice e tabela parcial quando há.
- Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): campeão e vice da lista sempre em 1º e 2º (vice da es nos anos de vice duplo, D-22 a), tabelas parciais inteiras, 1982-1995 sem tabela de uma fase só, pré-temporada de 1962-1966 e copas de 2000, 2004 e 2005 fora, clubes (D-25 c e d), ESPN (gol sem lado, jogador '2', estádio sem patrocinador) e o Apertura 2026 (D-01).
- Abertos fechados em 24/11: PY-008 (1996-2007: fases do Apertura e do Clausura com o nome do torneio, 'Final do Apertura'; 1981: 1º turno, triangular de desempate e final do ano), PY-012 (rebaixados pelas notas das páginas da RSSSF, explicacoes.REBAIXADOS: 55 marcas novas), PY-018 (artilheiros de 2011 em diante pela Wikipédia em espanhol, goleadores_es.py), PY-019 (números da paratops mantidos, divergências explicadas) e PY-031 (textos da ficha).
- Rebaixados sem fonte: 2008 (a página não traz a tabela de promedios) e os anos antes de 1981.

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/par-1.md`):

- PY-001 (alta) A campeão (classificação) — 1917; 1928; 1936; 1991: Campeões 1917 Libertad (Gran Partido Final Olimpia 0-1 Libertad, parahist l.525), 1928 Olimpia, 1936 Olimpia (líder no abandono), 1991 Sol de América (final x Cerro Porteño, para91 l.90-97) | SUGESTÃO: importar.classific
- PY-002 (alta) A vice — 1909; 1914; 1915; 1917; 1918; 1928; 1936; 1942; 1962; 1966; 1986; 1987; 1989; 1990; 1991; 1992; 1999; 2000; 2001; 2002; 2003; 2005; 2020 Clausura: RSSSF parachamp e Wikipédia es concordam: 1909 Libertad, 1914 Cerro Porteño, 1915 Olimpia, 1917 Olimpia, 1918 Nacional, 1928 Libertad, 1936 Atlántida, 1942 Cerro Porteño, 1962 Nacional, 1966 Guaraní, 1986 Olimpia, 1987 O
- PY-003 (alta) B classificação (tabela parcial) — 1909; 1911; 1912; 1914; 1915; 1916; 1918; 1919; 1920; 1921; 1923; 1924; 1925; 1926; 1927; 1928; 1929; 1935; 1936; 1937; 1938; 1940; 1941; 1942; 1944; 1946; 1948; 1949; 1950; 1951; 1952; 1953; 1954; 1957; 1958; 1959: parahist traz as tabelas inteiras (linhas sem número = mesma posição da de cima), ex.: 1928 l.966-976 (10 clubes), 1936 l.1193-1204 (11 clubes) | SUGESTÃO: em ler_rsssf.tabela_parcial(), aceitar linha sem número dentro d
- PY-004 (alta) B classificação (1982-1995) — 1986; 1987; 1988; 1989; 1990; 1991; 1992; 1993; 1995: As páginas têm várias fases e, em 1990, 1991 e 1994, os jogos da final; 1989 é 'J-Pts (GP-GC) V E D' com 12 clubes (para89 l.15-28) | SUGESTÃO: escolher em edicoes.py a tabela certa por ano (tabelas=[(página, linha, linh
- PY-005 (alta) C jogos de outros torneios (1962-1966) — 1962; 1963; 1964; 1965; 1966: O campeonato começa em para62 l.98, para63 l.83, para64 l.127, para65 l.217, para66 l.109 ('Campeonato de Primera División A/de Honor'); antes vêm as copas | SUGESTÃO: começar os trechos nessas linhas (trechos=[('para62'
- PY-006 (media) C playoffs de rebaixamento como liga/título — 1961; 1963: para61 l.283-291 e para63 l.351-362 | SUGESTÃO: incluir em ler_rsssf.FASES os títulos 'Playoff against 11th Place' -> 'Desempate do rebaixamento' (ou cortar com FIM_PADRAO); fonte: https://www.rsssf.org/tablesp/para61.ht
- PY-007 (media) C jogos que não valem o título (1996-2007) — 2000; 2004; 2005: para00 l.496-531, para04 (Pre-Sudamericana; Wikipédia es 2004 confirma), para05 l.315-327, l.628-639 e l.953-962 ('Championship Final' da Intermedia; edicoes.py a soma de propósito achando que é a final do campeonato) | 
- PY-008 (media) C nomes de fase — 1981; 1996; 1997; 1998; 1999; 2003: Títulos nas páginas: 'Apertura Final', 'Clausura Final', 'Final' (do ano), 'Triangular de Desempate', 'Overall Final' | SUGESTÃO: preencher ler_rsssf.TORNEIOS/FECHA (hoje vazios, copiados da Colômbia) para os torneios do
- PY-009 (media) C datas e rodadas de mata-mata — 1961-1967; 1981; 1996-2007; 2015 Clausura; 2020 Clausura: Datas no formato 'First Leg [Dec 15]' (armadilha conhecida no COMECE-AQUI) | SUGESTÃO: ler a data do título da fase ('First Leg [..]', 'Semifinals [Jun 28]', 'Final [Jul 3]') no rsssf_sul ou corrigir em CORRIGE; de 2005 
- PY-010 (media) B jogo decidido no tribunal — 1960: para60 l.69 'awarded as a win to Libertad' | SUGESTÃO: aceitar 'awarded as a win to' em _vitoria_dada (ou CORRIGE com esp='wo_v'); fonte: https://www.rsssf.org/tablesp/para60.html; mexer em: coleta/par-1/ler_rsssf.py _vi
- PY-011 (alta) B rebaixado — 1967: para67 l.316-324: San Lorenzo 3-2 e 0-0 Presidente Hayes, 'both remain at former level' | SUGESTÃO: em importar.situacao() não tratar 'Relegation Playoff' como queda; fonte: https://www.rsssf.org/tablesp/para67.html; mex
- PY-012 (media) B rebaixados não marcados — 1965-2025: RSSSF traz a queda por promedio no fim de cada ano: 2010 Sport Colombia e Trinidense; 2015 Santaní e San Lorenzo; 2019 Capiatá e Santaní; 2024 Sol de América e Tacuary; 2025 Gral. Caballero JLM e Tembetary; para94 l.93-1
- PY-013 (media) E clubes juntados — 1994: Wikipédia es 1994 lista 'Club Pettirossi' de Encarnación (fundado 1916, estádio Carlos Memmel); para94 l.34 'Pettirossi (Encarnación)' | SUGESTÃO (decisão do Guilherme): clube novo 'Pettirossi de Encarnación' e regra só 
- PY-014 (media) E clube duplicado — 1994; 2012-2013: Wikipédia es do Cerro Porteño (Presidente Franco): 'En 1994 el equipo fue incluido junto con otros 5 clubes del interior en el nuevo Torneo Nacional'; a página de 1994 lista 'Club Cerro Porteño (Presidente Franco)' | SUG
- PY-015 (baixa) E cidade do clube — 1994: Wikipédia es 1994: Club 8 de Diciembre, Caaguazú, estádio Federico Llamosas, fundado em 1961 | SUGESTÃO: ('Caaguazú', 'Caaguazú'); fonte: https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994; mexer em: 
- PY-018 (media) D artilheiros faltando — 2014 Apertura; 2014 Clausura; 2015 Apertura; 2015 Clausura; 2016 Apertura; 2016 Clausura; 2017 Clausura; 2018 Clausura; 2019 Clausura; 2020 Clausura; 2021 Clausura; 2024 Clausura; 2025 Apertura; 2025 Clausura: Wikipédia es (coluna Goleador): ex. 2015 Clausura Santiago Salcedo 19, 2019 Clausura Roque Santa Cruz 15, 2024 Clausura Redes, Ruiz Díaz e Ferreira 7; as páginas anuais da RSSSF têm 'Topscorers' | SUGESTÃO: ler 'Topscore
- PY-019 (media) D artilheiro (gols) — 1935; 1962; 1963; 1967; 1970; 2003: Wikipédia es: 17, 17, 19, 18, 11, 16; a própria página do ano na RSSSF dá 1962 18 (para62 l.356) e 1967 16 (para67 l.306) | SUGESTÃO: conferir com a página do ano e, sem acordo, registrar a divergência na observação; fon
- PY-020 (baixa) D gols com autor x placar — 2007: ESPN 213940: lance de 81' sem 'lado' | SUGESTÃO: descartar lance sem lado ou exigir soma total igual ao placar antes de usar os gols da ESPN; fonte: data/coleta/par-1/espn/par1_2007.json; mexer em: coleta/par-1/importar.
- PY-021 (baixa) D jogador sem nome — 2006; 2007: ESPN sem nome do jogador | SUGESTÃO: descartar nome só com dígitos (gol fica sem autor, sem minuto inventado); fonte: data/coleta/par-1/espn/par1_2006.json; mexer em: coleta/par-1/outras_fontes.lances_espn()
- PY-025 (baixa) F estádios — 2007-2025: ESPN devolve o nome de hoje | SUGESTÃO: tabela de nomes de estádio (tirar 'ueno'/'Tigo', padronizar 'Estadio ...'); mexer em: coleta/par-1/importar.py (estadio = ge.get('estadio')) ou coleta/comum-sulamerica/espn.py
- PY-027 (baixa) A edição faltando — 2026 Apertura: RSSSF parachamp: '2026 Olimpia (Apertura) Nacional' | SUGESTÃO: incluir '2026 Apertura' em edicoes._AC quando o Guilherme quiser o ano corrente; fonte: https://www.rsssf.org/tablesp/para2026.html; mexer em: coleta/par-1/
- PY-028 (media) A vice com empate na lista — 1926; 1927; 1952; 1953; 1964: RSSSF parachamp lista dois vices: 1926 River Plate e Sol de América, 1927 Libertad e Nacional, 1952 Sol de América e Libertad, 1953 Cerro Porteño e Libertad, 1964 Cerro Porteño e Nacional; a Wikipédia es escolhe River Pl
- PY-029 (baixa) C texto dos jogos — 2005: para05 l.572-575 (nota em duas linhas) | SUGESTÃO: CONSERTA_TEXTO juntando a nota; mexer em: coleta/par-1/explicacoes.py CONSERTA_TEXTO
- PY-031 (baixa) Ficha (documentação) — : Ver PY-004 e PY-005 | SUGESTÃO: corrigir o texto e o rótulo (mais/menos) no gerador; mexer em: coleta/comum-sulamerica/documentar.py e o texto do relatório em coleta/par-1/importar.py relatorio()

## 10. Arquivos e comandos

Código em `coleta/par-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga par.1) de 2001 a 2025 para data/coleta/par-1/espn/par1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão paraguaia para data/coleta/par-1/rsssf/. |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "Paraguayan Primera División", seção "List of champions"), segunda fonte |
| `clubes_par.py` | Identidade dos clubes paraguaios: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão paraguaia (par-1): uma por torneio que deu título de campeão paraguaio. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão paraguaia, edição a edição (entram no relatório). |
| `goleadores_es.py` | Artilheiros pela coluna "Goleador" da tabela "Títulos de Liga por año" da Wikipédia em espanhol (página "Primera División |
| `importar.py` | Junta as fontes da 1ª divisão paraguaia e grava o pacote em data/coleta/par-1/pacote/ e o relatório em docs/coleta/par-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/par-1/rsssf/) com o leitor comum (rsssf_sul). Nos anos sem |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/par-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`.
- Pacote: `data/coleta/par-1/pacote/`; relatório: `docs/coleta/par-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/par-1/baixar_espn.py
python coleta/par-1/baixar_rsssf.py
python coleta/par-1/importar.py
python coleta/par-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py par-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

