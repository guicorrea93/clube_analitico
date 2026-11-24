# Campeonato Peruano (`per-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/per-1/pacote/`, do código `coleta/per-1/` e do relatório `docs/coleta/per-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 109, de 1912 a 2025; 18 sem jogos.
- **Jogos:** 17318 (17272 com placar); **gols:** 47454; **gols com autor:** 23573 (50%); **cartões:** 21067.
- **Clubes:** 167; **artilheiros:** 97 edições com artilheiro (101 linhas, com empates).
- **Classificação final:** 109 edições; **tabelas publicadas guardadas para conferência:** 2552 linhas.
- **No banco:** sim; **último commit do pacote:** c887a7d4.
- **Observação da competição:** 1ª divisão peruana de 1912 a 2025, um campeão por ano (sem campeonato em 1922-1925 e 1936). 1912-1921: Liga Peruana de Football, só com campeão e vice. Sem jogos em 1970-1974, 1976, 1977 e 1979 (só a tabela final); jogos incompletos em 1926, 1982, 1984, 1986, 1988-1991 e 2003.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão peruana (per-1): uma por título de campeão peruano, como na lista da RSSSF (peruchamp.html).

1912-1921: Liga Peruana de Football (antes da Federação, de 1922). A RSSSF lista os campeões à parte e não os soma aos
títulos nacionais; a Wikipédia os conta. Entram como edições só com o campeão (nenhuma fonte tem tabela ou jogos completos).
1926-2025: um campeão por ano (sem campeonato oficial em 1936). Apertura, Clausura, Torneo de Verano, liguillas e finais são
fases da edição anual. Ficam de fora a Copa Perú e a Segunda División, as ligas de reservas (que davam pontos de bônus de
1931 a 1934), o Intermedio, o Torneo del Inca, a Copa Bicentenario, as liguillas pré-Libertadores e os jogos de promoção
contra clubes de baixo.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). 1930-1942, 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984 e 1986 em diante.
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1926-1929, 1943-1967, 1982 e 1985.
- sem jogos: 1912-1921, 1970-1974, 1976, 1977 e 1979 (nenhuma fonte pública traz os jogos; pesquisa no relatório). Entram
  com a tabela final da RSSSF (peruhist.html), quando há.
- tabelas: trechos lidos só pelas tabelas (a conferência): a seção do ano em peruhist.html nos anos sem página da RSSSF.
```

**Edições:** 109, uma por título de campeão peruano, de 1912 a 2025, como na lista de campeões da RSSSF (`peruchamp.html`) e na Wikipédia em inglês ("List of Peruvian football champions"). Um campeão por ano; sem campeonato de 1922 a 1925 e em 1936 (sem torneio oficial, ano dos Jogos Olímpicos). Apertura, Clausura, Torneo de Verano, Regional, liguillas e finais são fases da edição anual.

**1912-1921 (Liga Peruana de Football):** a liga anterior à Federação Peruana de Futebol (1922). A RSSSF lista esses campeões à parte e não os soma aos títulos nacionais; a Wikipédia em inglês os conta (numera os títulos a partir de 1912). Entram como edições só com o campeão e o vice (da Wikipédia): nenhuma fonte pública tem tabela ou jogos completos (a RSSSF tem 8 jogos soltos de 1912). Se o agente 1 preferir a contagem da RSSSF, basta tirar essas 10 edições.

**Fontes:** RSSSF (uma página por temporada e a lista de tabelas finais `peruhist.html`, em `data/coleta/per-1/rsssf/`: base de jogos de 1930-1942, 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984 e 1986 em diante, com fases, grupos, rodadas, datas e autores dos gols); Wikipédia em espanhol (jogos de 1926-1929, 1943-1967, 1982 e 1985, quase sempre em tabela de confrontos, sem rodada nem data; em `data/coleta/per-1/wikipedia/`); ESPN (liga `per.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão e vice de 1912-1921). O ogol não tem jogos peruanos.

**Clubes:** nome pelo qual o clube é conhecido no Brasil (Universitario, Melgar, César Vallejo, Binacional, UTC, CNI, ADT). Homônimos de outros países levam a cidade: Libertad de Trujillo, Internazionale de San Borja. O mesmo clube com outro nome fica com o atual: Federación Universitaria (até 1930) = Universitario; Sport Alianza = Alianza Lima; Sucre FBC = Mariscal Sucre; Inti Gas = Ayacucho; Total Clean = Total Chalaco; Real Garcilaso = Cusco FC; Colegio San Agustín = Deportivo San Agustín; Grau-Estudiantes (2004) = Estudiantes de Medicina. Aurich-Cañaña (fusão de 1994 a 1996) é clube à parte do Juan Aurich.

**Regras:** o placar é o da fonte de base (RSSSF ou Wikipédia). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos: 2 por vitória até 1994 e 3 a partir de 1995; de 1931 a 1942 a vitória valia 3, o empate 2 e a derrota 1 (o `ajuste_pontos` desses anos parte dessa conta; de 1931 a 1934 a tabela soma ainda os pontos de bônus da liga de reservas).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 52.
- **Edições com alguma tabela divergente** (38; motivo no relatório, na edição): 1927, 1928, 1929, 1931, 1933, 1934, 1948, 1949, 1950, 1951, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966, 1967, 1975, 1978, 1982, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1996, 1999, 2000, 2013, 2021.
- **Edições sem tabela para conferir** (19): 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1926, 1970, 1971, 1972, 1973, 1974, 1976, 1977, 1979.
- **Edições com menos jogos que o esperado:** 1950 (89 de 90), 1957 (110 de 130), 1958 (110 de 130), 1959 (110 de 130), 1964 (110 de 130), 1965 (110 de 130).
- **Edições com mais jogos que o esperado** (desempates e jogos fora da tabela publicada): 1935 (9 de 6), 1975 (323 de 322), 2000 (266 de 265), 2004 (366 de 365), 2016 (360 de 359).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1910s | 8 | 0 | — | — | — | — | — | — | — | — |
| 1920s | 6 | 206 | 28% | 0% | 41% | 6% | 0% | 0% | 0% | 0.0 |
| 1930s | 9 | 347 | 100% | 0% | 100% | 0% | 0% | 0% | 3% | 0.0 |
| 1940s | 10 | 685 | 23% | 0% | 23% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 960 | 7% | 0% | 9% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 1266 | 25% | 0% | 32% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 687 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 3010 | 76% | 0% | 75% | 1% | 0% | 0% | 20% | 0.0 |
| 1990s | 10 | 2127 | 76% | 0% | 99% | 0% | 0% | 0% | 26% | 0.0 |
| 2000s | 10 | 2964 | 100% | 47% | 100% | 44% | 43% | 0% | 98% | 1.4 |
| 2010s | 10 | 3217 | 100% | 99% | 100% | 99% | 91% | 1% | 98% | 2.2 |
| 2020s | 6 | 1849 | 100% | 100% | 100% | 100% | 100% | 0% | 99% | 5.3 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1912 a 1921: 0 clubes
- 1926: 11 clubes
- 1927: 8 clubes
- 1928: 19 clubes
- 1929: 13 clubes
- 1930 a 1931: 12 clubes
- 1932: 8 clubes
- 1933: 10 clubes
- 1934: 9 clubes
- 1935: 5 clubes
- 1937: 10 clubes
- 1938: 9 clubes
- 1939 a 1941: 8 clubes
- 1942: 10 clubes
- 1943 a 1947: 8 clubes
- 1948: 9 clubes
- 1949: 8 clubes
- 1950 a 1965: 10 clubes
- 1966 a 1970: 14 clubes
- 1971 a 1972: 16 clubes
- 1973: 18 clubes
- 1974: 22 clubes
- 1975: 18 clubes
- 1976 a 1979: 16 clubes
- 1980: 17 clubes
- 1981 a 1982: 16 clubes
- 1983: 17 clubes
- 1984: 15 clubes
- 1985: 30 clubes
- 1986: 18 clubes
- 1987: 30 clubes
- 1988: 37 clubes
- 1989: 14 clubes
- 1990: 13 clubes
- 1991: 15 clubes
- 1992 a 1996: 16 clubes
- 1997: 14 clubes
- 1998: 12 clubes
- 1999: 13 clubes
- 2000 a 2003: 12 clubes
- 2004: 14 clubes
- 2005: 13 clubes
- 2006 a 2007: 12 clubes
- 2008: 14 clubes
- 2009 a 2014: 16 clubes
- 2015: 17 clubes
- 2016 a 2018: 16 clubes
- 2019: 18 clubes
- 2020: 20 clubes
- 2021 a 2023: 19 clubes
- 2024: 18 clubes
- 2025: 19 clubes

**Pontos por vitória:**

- 1912 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1912 a 1921: Liga Peruana de Football <ano>
- 1926 a 1950: Campeonato de Primera División del Perú <ano>
- 1951 a 1965: Campeonato Profesional del Perú <ano>
- 1966 a 2018: Campeonato Descentralizado <ano>
- 2019 a 2025: Liga 1 <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1912 a 1921: sem jogos (só a tabela final)
- 1926 a 1927: pontos corridos
- 1928: 2 grupos + pontos corridos + mata-mata
- 1929: pontos corridos
- 1930: 3 grupos + pontos corridos
- 1931 a 1933: pontos corridos
- 1934: pontos corridos + desempate
- 1935 a 1937: pontos corridos
- 1938: pontos corridos + desempate
- 1939 a 1954: pontos corridos
- 1955: pontos corridos + desempate
- 1956 a 1960: pontos corridos
- 1961: pontos corridos + desempate
- 1962 a 1967: pontos corridos
- 1968: desempate + pontos corridos + desempate
- 1969: pontos corridos + desempate + pontos corridos
- 1970 a 1974: sem jogos (só a tabela final)
- 1975: pontos corridos + desempate + pontos corridos
- 1976 a 1977: sem jogos (só a tabela final)
- 1978: 2 grupos
- 1979: sem jogos (só a tabela final)
- 1980: pontos corridos + desempate + pontos corridos
- 1981: 4 grupos + mata-mata + pontos corridos + desempate
- 1982: 3 grupos + pontos corridos + 2 grupos + pontos corridos
- 1983: pontos corridos
- 1984: 4 grupos + pontos corridos + mata-mata
- 1985: 4 grupos + desempate + mata-mata + pontos corridos
- 1986: 3 grupos + pontos corridos + mata-mata
- 1987: 4 grupos + mata-mata + 3 grupos + pontos corridos + mata-mata
- 1988: 4 grupos + desempate + mata-mata + 4 grupos + pontos corridos + mata-mata
- 1989: 2 grupos + 3 grupos + pontos corridos + mata-mata
- 1990: pontos corridos + mata-mata
- 1991: mata-mata + pontos corridos + 2 grupos
- 1992 a 1993: pontos corridos
- 1994: 2 grupos + mata-mata + 2 grupos
- 1995 a 1997: pontos corridos
- 1998: pontos corridos + mata-mata
- 1999 a 2000: pontos corridos + desempate
- 2001: pontos corridos + mata-mata + pontos corridos + mata-mata + desempate
- 2002: pontos corridos + mata-mata + pontos corridos
- 2003 a 2005: pontos corridos + mata-mata
- 2006: pontos corridos + mata-mata + desempate + mata-mata
- 2007: pontos corridos
- 2008: pontos corridos + desempate
- 2009: 2 grupos + mata-mata
- 2010 a 2011: pontos corridos + mata-mata
- 2012: 2 grupos + pontos corridos + mata-mata
- 2013: 2 grupos + desempate + 2 grupos + mata-mata
- 2014 a 2015: pontos corridos + mata-mata + desempate + mata-mata
- 2016: pontos corridos + desempate + mata-mata
- 2017: pontos corridos + mata-mata + pontos corridos
- 2018: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2019 a 2020: pontos corridos + mata-mata
- 2021: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2022: pontos corridos + mata-mata
- 2023: pontos corridos + desempate
- 2024 a 2025: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1928: Primeira fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 1930: Primeira fase (grupos, 3 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 1934: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1938: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1955: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1957: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1958: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1959: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1961: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1964: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1965: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1968: Desempate do rebaixamento (mata_mata, ida_volta); Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1969: Primeira fase (liga); Grupo do rebaixamento (liga); Desempate do 2º lugar (mata_mata, jogo_unico); Fase final (liga)
- 1975: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico); Fase final (liga)
- 1978: Primeira fase (grupos, 2 grupos); Regional (grupos, 2 grupos)
- 1980: Primeira fase (liga); Grupo do rebaixamento (liga); Desempate do rebaixamento (mata_mata, ida_volta); Fase final (liga)
- 1981: Regional (grupos, 4 grupos); Semifinal do Regional (mata_mata, ida_volta); Final do Regional (mata_mata, ida_volta); Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta)
- 1982: Regional (grupos, 3 grupos); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1983: Primeira fase (liga); Fase final (liga)
- 1984: Primeira fase (grupos, 4 grupos); Fase final (liga); Semifinal (mata_mata, jogo_unico)
- 1985: Regional (grupos, 4 grupos); Desempate do Regional (mata_mata, jogo_unico); Repechaje do Regional (mata_mata, ida_volta); Quartas de final do Regional (mata_mata, jogo_unico); Semifinal do Regional (mata_mata, jogo_unico); Final do Regional (mata_mata, jogo_unico); Primeira fase (liga); Fase final (liga)
- 1986: Primeira fase (grupos, 3 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 1987: Regional (grupos, 4 grupos); Final do Regional (mata_mata, ida_volta); Primeira fase (grupos, 3 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 1988: Regional (grupos, 4 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Final do Regional (mata_mata, jogo_unico); Primeira fase (grupos, 4 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 1989: Regional (grupos, 2 grupos); Primeira fase (grupos, 3 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 1990: Regional (liga); Regional II (liga); Final do Regional II (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1991: Quartas de final do Regional (mata_mata, ida_volta); Quartas de final do Regional II (mata_mata, ida_volta); Regional (liga); Regional II (grupos, 2 grupos)
- 1994: Apertura (grupos, 2 grupos); Final do Apertura (mata_mata, jogo_unico); Primeira fase (grupos, 2 grupos)
- 1995: Primeira fase (liga); Fase final (liga)
- 1997: Apertura (liga); Clausura (liga)
- 1998: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1999: Apertura (liga); Clausura (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Desempate do título (mata_mata, ida_volta)
- 2000: Apertura (liga); Clausura (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 2001: Apertura (liga); Final do Apertura (mata_mata, jogo_unico); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do título (mata_mata, ida_volta)
- 2002: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Clausura (liga)
- 2003: Apertura (liga); Clausura (liga); Final (mata_mata, jogo_unico)
- 2004: Apertura (liga); Clausura (liga); Final (mata_mata, jogo_unico)
- 2005: Apertura (liga); Clausura (liga); Final (mata_mata, jogo_unico)
- 2006: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do rebaixamento (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2007: Apertura (liga); Clausura (liga)
- 2008: Apertura (liga); Clausura (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 2009: Primeira fase (grupos, 2 grupos); Liguillas (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2010: Primeira fase (liga); Liguillas (liga); Final (mata_mata, ida_volta)
- 2011: Primeira fase (liga); Final (mata_mata, ida_volta)
- 2012: Primeira fase (grupos, 2 grupos); Liguillas (liga); Final (mata_mata, ida_volta)
- 2013: Primeira fase (grupos, 2 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Liguillas (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2014: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do rebaixamento (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2015: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do 2º lugar (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016: Apertura (liga); Clausura (liga); Liguillas (liga); Desempate do 2º lugar (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017: Torneo de Verano (liga); Final do Torneo de Verano (mata_mata, ida_volta); Apertura (liga); Clausura (liga)
- 2018: Torneo de Verano (liga); Final do Torneo de Verano (mata_mata, ida_volta); Apertura (liga); Clausura (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019: Apertura (liga); Clausura (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021: Fase 1 (liga); Final da Fase 1 (mata_mata, jogo_unico); Fase 2 (liga); Final (mata_mata, ida_volta)
- 2022: Apertura (liga); Clausura (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023: Apertura (liga); Clausura (liga); Desempate do título (mata_mata, ida_volta)
- 2024: Apertura (liga); Clausura (liga)
- 2025: Apertura (liga); Clausura (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 66 edições
- calculada: 43 edições

**Observações das edições:**

- 1912: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1913: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1914: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1915: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1916: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1917: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1918: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1919: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1920: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1921: sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão
- 1970: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1971: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1972: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1973: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1974: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1976: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1977: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)
- 1979: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Universitario: 29
- Alianza Lima: 25
- Sporting Cristal: 20
- Sport Boys: 6
- Deportivo Municipal: 4
- Universidad San Martín: 3
- Lima Cricket: 2
- Sport José Gálvez: 2
- Sport Progreso: 2
- Atlético Chalaco: 2
- Mariscal Sucre: 2
- Unión Huaral: 2
- Melgar: 2
- Jorge Chávez N°1: 1
- Sport Juan Bielovucic: 1
- Sport Inca: 1
- Centro Iqueño: 1
- Defensor Lima: 1
- Deportivo San Agustín: 1
- Juan Aurich: 1
- Binacional: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1912 | Lima Cricket | Association FBC |
| 1913 | Jorge Chávez N°1 | Lima Cricket |
| 1914 | Lima Cricket | Alianza Lima |
| 1915 | Sport José Gálvez | Atlético Peruano |
| 1916 | Sport José Gálvez | Jorge Chávez N°1 |
| 1917 | Sport Juan Bielovucic | Alianza Lima |
| 1918 | Alianza Lima | Jorge Chávez |
| 1919 | Alianza Lima | Sport Sáenz Peña |
| 1920 | Sport Inca | Sport Progreso |
| 1921 | Sport Progreso | Jorge Chávez |
| 1926 | Sport Progreso | Alianza Lima |
| 1927 | Alianza Lima | Unión Buenos Aires |
| 1928 | Alianza Lima | Universitario |
| 1929 | Universitario | Circolo Sportivo Italiano |
| 1930 | Atlético Chalaco | Alianza Lima |
| 1931 | Alianza Lima | Sporting Tabaco |
| 1932 | Alianza Lima | Universitario |
| 1933 | Alianza Lima | Universitario |
| 1934 | Universitario | Alianza Lima |
| 1935 | Sport Boys | Alianza Lima |
| 1937 | Sport Boys | Alianza Lima |
| 1938 | Deportivo Municipal | Sport Boys |
| 1939 | Universitario | Mariscal Sucre |
| 1940 | Deportivo Municipal | Universitario |
| 1941 | Universitario | Deportivo Municipal |
| 1942 | Sport Boys | Deportivo Municipal |
| 1943 | Deportivo Municipal | Alianza Lima |
| 1944 | Mariscal Sucre | Deportivo Municipal |
| 1945 | Universitario | Deportivo Municipal |
| 1946 | Universitario | Deportivo Municipal |
| 1947 | Atlético Chalaco | Deportivo Municipal |
| 1948 | Alianza Lima | Atlético Chalaco |
| 1949 | Universitario | Mariscal Sucre |
| 1950 | Deportivo Municipal | Sport Boys |
| 1951 | Sport Boys | Deportivo Municipal |
| 1952 | Alianza Lima | Sport Boys |
| 1953 | Mariscal Sucre | Alianza Lima |
| 1954 | Alianza Lima | Sporting Tabaco |
| 1955 | Alianza Lima | Universitario |
| 1956 | Sporting Cristal | Alianza Lima |
| 1957 | Centro Iqueño | Atlético Chalaco |
| 1958 | Sport Boys | Atlético Chalaco |
| 1959 | Universitario | Sport Boys |
| 1960 | Universitario | Sport Boys |
| 1961 | Sporting Cristal | Alianza Lima |
| 1962 | Alianza Lima | Sporting Cristal |
| 1963 | Alianza Lima | Sporting Cristal |
| 1964 | Universitario | Alianza Lima |
| 1965 | Alianza Lima | Universitario |
| 1966 | Universitario | Sport Boys |
| 1967 | Universitario | Sporting Cristal |
| 1968 | Sporting Cristal | Juan Aurich |
| 1969 | Universitario | Defensor Arica |
| 1970 | Sporting Cristal | Universitario |
| 1971 | Universitario | Alianza Lima |
| 1972 | Sporting Cristal | Universitario |
| 1973 | Defensor Lima | Sporting Cristal |
| 1974 | Universitario | Unión Huaral |
| 1975 | Alianza Lima | Alfonso Ugarte |
| 1976 | Unión Huaral | Sport Boys |
| 1977 | Alianza Lima | Sporting Cristal |
| 1978 | Alianza Lima | Universitario |
| 1979 | Sporting Cristal | Atlético Chalaco |
| 1980 | Sporting Cristal | Atlético Torino |
| 1981 | Melgar | Deportivo Municipal |
| 1982 | Universitario | Alianza Lima |
| 1983 | Sporting Cristal | Melgar |
| 1984 | Sport Boys | Universitario |
| 1985 | Universitario | UTC |
| 1986 | Deportivo San Agustín | Alianza Lima |
| 1987 | Universitario | Alianza Lima |
| 1988 | Sporting Cristal | Universitario |
| 1989 | Unión Huaral | Sporting Cristal |
| 1990 | Universitario | Sport Boys |
| 1991 | Sporting Cristal | Sport Boys |
| 1992 | Universitario | Sporting Cristal |
| 1993 | Universitario | Alianza Lima |
| 1994 | Sporting Cristal | Alianza Lima |
| 1995 | Sporting Cristal | Universitario |
| 1996 | Sporting Cristal | Alianza Lima |
| 1997 | Alianza Lima | Sporting Cristal |
| 1998 | Universitario | Sporting Cristal |
| 1999 | Universitario | Alianza Lima |
| 2000 | Universitario | Sporting Cristal |
| 2001 | Alianza Lima | Cienciano |
| 2002 | Sporting Cristal | Universitario |
| 2003 | Alianza Lima | Sporting Cristal |
| 2004 | Alianza Lima | Sporting Cristal |
| 2005 | Sporting Cristal | Cienciano |
| 2006 | Alianza Lima | Cienciano |
| 2007 | Universidad San Martín | Coronel Bolognesi |
| 2008 | Universidad San Martín | Universitario |
| 2009 | Universitario | Alianza Lima |
| 2010 | Universidad San Martín | León de Huánuco |
| 2011 | Juan Aurich | Alianza Lima |
| 2012 | Sporting Cristal | Cusco FC |
| 2013 | Universitario | Cusco FC |
| 2014 | Sporting Cristal | Juan Aurich |
| 2015 | Melgar | Sporting Cristal |
| 2016 | Sporting Cristal | Melgar |
| 2017 | Alianza Lima | Cusco FC |
| 2018 | Sporting Cristal | Alianza Lima |
| 2019 | Binacional | Alianza Lima |
| 2020 | Sporting Cristal | Universitario |
| 2021 | Alianza Lima | Sporting Cristal |
| 2022 | Alianza Lima | Melgar |
| 2023 | Universitario | Alianza Lima |
| 2024 | Universitario | Sporting Cristal |
| 2025 | Universitario | Cusco FC |

**Rebaixados marcados na classificação:** 177 em 83 edições (só onde a tabela publicada marca a queda); quem mais caiu: José Gálvez (6), Ciclista Lima (5), Carlos Mannucci (5), Atlético Torino (5), Jorge Chávez (4).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1970: Sporting Cristal +26
- 1970: Universitario +24
- 1970: Defensor Arica +26
- 1970: Juan Aurich +21
- 1970: Defensor Lima +18
- 1970: Deportivo Municipal +17
- 1970: Octavio Espinosa +18
- 1970: Sport Boys +20
- 1970: Alianza Lima +16
- 1970: Porvenir Miraflores +17
- 1970: Atlético Torino +17
- 1970: Carlos Mannucci +15
- 1970: Deportivo SIMA +15
- 1970: Atlético Grau +16
- 1979: Sporting Cristal +1
- 1979: Juan Aurich +2
- 1979: Universitario +3
- 1979: Melgar -3
- 1979: Atlético Torino -1
- 1979: Juventud La Palma -2
- 1981: Alfonso Ugarte -1
- 1981: Sporting Cristal +2
- 1981: Atlético Torino -1
- 1998: Cienciano -1
- 2002: Alianza Lima -3
- 2002: Alianza Atlético -3
- 2007: Alianza Lima -4
- 2008: Sport Boys -2
- 2009: Universidad San Martín -1
- 2010: Universidad San Martín +1
- 2010: Universitario -2
- 2010: César Vallejo +2
- 2010: Cienciano -2
- 2010: Total Chalaco -2
- 2011: Juan Aurich +1
- 2011: Alianza Lima +2
- 2012: Juan Aurich +2
- 2012: Universidad San Martín +1
- 2012: Universitario -1
- 2012: Alianza Lima -4
- 2012: Sport Boys -2
- 2012: Cobresol -4
- 2014: Melgar +2
- 2014: Universitario +1
- 2014: Cienciano -3
- 2015: Melgar +1
- 2015: Sport Huancayo -3
- 2015: Universitario +1
- 2015: Universidad San Martín +1
- 2015: Ayacucho -1
- 2015: Cienciano -6
- 2015: Sport Loreto -2
- 2015: León de Huánuco -4
- 2016: Sporting Cristal +2
- 2016: Universitario +1
- 2016: Defensor La Bocana -4
- 2017: Universitario -1
- 2017: Sport Huancayo +2
- 2017: Sporting Cristal +1
- 2017: Academia Cantolao -1
- 2017: Juan Aurich -1
- 2017: Alianza Atlético -3
- 2018: Sporting Cristal +2
- 2018: Alianza Lima +1
- 2018: Deportivo Municipal -2
- 2018: UTC -2
- 2018: Universitario -1
- 2018: Academia Cantolao -2
- 2018: Sport Rosario -7
- 2018: Comerciantes Unidos -1
- 2019: Sporting Cristal +2
- 2019: Sport Huancayo +1
- 2019: Deportivo Municipal -6
- 2019: Pirata FC -5
- 2020: Universitario -1
- 2020: Sport Boys -1
- 2020: Carlos Stein -3
- 2020: Deportivo Llacuabamba -1
- 2021: Universitario -2
- 2021: Cienciano -1
- 2021: Sport Boys -1
- 2021: Deportivo Municipal -1
- 2021: Universidad San Martín -1
- 2021: Cusco FC -1
- 2021: Alianza Universidad -1
- 2022: Alianza Lima +2
- 2022: César Vallejo -2
- 2022: Deportivo Municipal -4
- 2022: Sport Boys -7
- 2022: Ayacucho +1
- 2022: Carlos Stein -2
- 2023: Deportivo Garcilaso -1
- 2023: Sport Boys -4
- 2023: Deportivo Municipal -5

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/per-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 7)

- **peru90 · 248:** «Regional II Championship Match» → «Regional Championship Match»: PE-010: o jogo do título do Regional II (Universitario 1-0 Alianza Lima) é a final do torneio, não mais um jogo da liguilla
- **peru90 · 251:** «Final [Feb 3] [between winners or Regional I and Regional II Championships]» → «National Final [Feb 3]»: PE-010: a final nacional (Universitario 4-2 Sport Boys, 3/2/1991, Estádio Nacional, como a Wikipédia em espanhol) fecha o Regional II e leva a data do título
- **peru98 · 701:** «December 16   Lima     Sporting Cristal - Alianza Lima              1-0» → «Dec 16  Sporting Cristal  1-0  Alianza Lima»: data e cidade antes dos clubes ("December 16  Lima  A - B  1-0"): a linha vira "Dec 16  A  1-0  B"
- **peru98 · 737:** «December 20   Lima     Sporting Cristal - Universitario             2-1» → «Dec 20  Sporting Cristal  2-1  Universitario»: data e cidade antes dos clubes ("December 16  Lima  A - B  1-0"): a linha vira "Dec 16  A  1-0  B"
- **peru98 · 739:** «December 23   Lima     Universitario - Sporting Cristal             2-1  [4-2 pen]» → «Dec 23  Universitario  2-1  Sporting Cristal  [4-2 pen]»: data e cidade antes dos clubes ("December 16  Lima  A - B  1-0"): a linha vira "Dec 16  A  1-0  B"
- **peru2025 · 1058:** «35 -  9 - 20 - 16» → «35 -  9 - 10 - 16»: Comerciantes Unidos com 20 empates na tabela acumulada (9+20+16 não dá 35 jogos); são 10, como na soma do Apertura e do Clausura
- **peru75 · 406:** «Union Huaraz» → «Unión Huaral»: "Union Huaraz" não está na tabela de 1975; é o Unión Huaral, o único clube da tabela sem esse jogo contra o Juan Aurich

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 42)

- **2004 · peru04:367:** [vale o placar de campo, gm = 1, gv = 1] Cienciano 1-1 Universitario, abandonado nos acréscimos (Universitario com 6 jogadores): o resultado ficou, como contam a tabela do Apertura (26 jogos, Cienciano 53-28, Universitario 31-25) e a Wikipédia em espanhol (PE-017)
- **2021 · peru2021:542:** [vale o placar de campo, gm = 2, gv = 2] Cusco FC 2-2 Cienciano: o TAS (21/01/2022) anulou a vitória dada ao Cusco (PE-007)
- **2017 · peru2017:396:** [fase = Final do Torneo de Verano] final do Torneo de Verano (maio), não a do campeonato (PE-013)
- **2017 · peru2017:400:** [fase = Final do Torneo de Verano] final do Torneo de Verano (maio), não a do campeonato (PE-013)
- **2018 · peru2018:393:** [fase = Final do Torneo de Verano] final do Torneo de Verano (abril), não a do campeonato (PE-013)
- **2018 · peru2018:397:** [fase = Final do Torneo de Verano] final do Torneo de Verano (abril), não a do campeonato (PE-013)
- **1991 · peru91:83:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1991 · peru91:84:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1991 · peru91:194:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1991 · peru91:195:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1991 · peru91:196:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1991 · peru91:197:** [descartado] confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- **1988 · peru88:640:** [descartado] linha da tabela de confrontos do Descentralizado "B" (não é jogo)
- **1988 · peru88:641:** [descartado] linha da tabela de confrontos do Descentralizado "B" (não é jogo)
- **1935 · peru35:56:** [não jogado] vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- **1935 · peru35:58:** [não jogado] vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- **1935 · peru35:65:** [não jogado] vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- **1929 · wiki-es_1929:365:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:375:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:388:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:402:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:416:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:436:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1929 · wiki-es_1929:449:** [anulado] jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- **1997 · peru97:349:** [descartado] nota ("Teams 2-7 qualify for Liguilla Pre-Libertadores"), não é jogo
- **1999 · peru99:640:** [descartado] nota sobre o jogo anterior (Cienciano 2-0 Sporting Cristal), não é jogo
- **2025 · peru2025:605:** [anulado] jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- **2025 · peru2025:632:** [anulado] jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- **2025 · peru2025:666:** [anulado] jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- **2025 · peru2025:686:** [anulado] jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- **2025 · peru2025:702:** [anulado] jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- **2003 · peru03:672:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:674:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:676:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:679:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:687:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:689:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:693:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:696:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2003 · peru03:699:** [anulado] rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- **2021 · peru2021:79:** [anulado] jogo anulado pela FPF: o FC Carlos Stein foi rebaixado por decisão do CAS (nota da página)
- **2025 · peru2025:978:** [decidido fora de campo, placar oficial 0-3] Ayacucho 1-0 Comerciantes Unidos em campo; as tabelas publicadas (Clausura e acumulada) contam 0-3, vitória dada ao Comerciantes Unidos (a página não traz a nota)

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 12)

- **1991:** Unión Huayllaspanca 0-0 Universitario (Quartas de final do Regional, rsssf:peru91:83) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Universitario 4-0 Unión Huayllaspanca (Quartas de final do Regional, rsssf:peru91:83) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Melgar 3-0 Alianza Lima (Quartas de final do Regional, rsssf:peru91:84) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Alianza Lima 3-2 Melgar (Quartas de final do Regional, rsssf:peru91:84) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Alianza Atlético 1-3 Universitario (Quartas de final do Regional II, rsssf:peru91:194) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Universitario 4-1 Alianza Atlético (Quartas de final do Regional II, rsssf:peru91:194) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Melgar 3-1 Sporting Cristal (Quartas de final do Regional II, rsssf:peru91:195) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Sporting Cristal 5-0 Melgar (Quartas de final do Regional II, rsssf:peru91:195) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Sport Boys 1-0 León de Huánuco (Quartas de final do Regional II, rsssf:peru91:196) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** León de Huánuco 2-3 Sport Boys (Quartas de final do Regional II, rsssf:peru91:196) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** CNI 1-1 Defensor Lima (Quartas de final do Regional II, rsssf:peru91:197) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido
- **1991:** Defensor Lima 2-1 CNI (Quartas de final do Regional II, rsssf:peru91:197) confronto de ida e volta numa linha só ("A - B 3-0 / 2-3"); mando da volta presumido

### Divergências entre fontes já explicadas (`EXPLICACOES`, 15)

- **1932:** placar da RSSSF x Wikipédia em espanhol (PE-017): Ciclista Lima 2-2 Sporting Tabaco (es 0-0): fica a RSSSF, com a qual a tabela publicada fecha
- **1933:** placar da RSSSF x Wikipédia em espanhol (PE-017): Sportivo Unión 1-6 Tarapacá (es 1-3): fica a RSSSF, com a qual a tabela publicada fecha para os dois clubes
- **1941:** placar da RSSSF x Wikipédia em espanhol (PE-017): Telmo Carbajo 0-0 Chalaco (es 1-1): fica a RSSSF, com a qual a tabela publicada fecha
- **1975:** placar da RSSSF x Wikipédia em espanhol (PE-017): Melgar 1-1 Alianza Lima (es 0-1): fica a RSSSF; a tabela publicada também diverge noutros jogos e não decide; falta uma 3ª fonte (jornal da época)
- **1981:** placar da RSSSF x Wikipédia em espanhol (PE-017): Torino 0-2 Melgar (es 1-2): fica a RSSSF, com a qual as tabelas publicadas fecham
- **1995:** placar da RSSSF x Wikipédia em espanhol (PE-017): San Agustín 1-1 Alianza Lima, fase final (es 1-2): fica a RSSSF, com a qual as tabelas publicadas fecham
- **1999:** placar da RSSSF x Wikipédia em espanhol (PE-017): Juan Aurich 3-1 Alianza Atlético (es 2-0): fica a RSSSF; a tabela publicada diverge por outro motivo (jogo a menos) e não decide; falta uma 3ª fonte
- **2000:** placar da RSSSF x Wikipédia em espanhol (PE-017): Deportivo Wanka 3-2 Alianza Lima e Wanka 1-0 Universitario (es 0-1 e 0-0): fica a RSSSF, com a qual as tabelas publicadas fecham para o Wanka
- **2004:** placar da RSSSF x Wikipédia em espanhol (PE-017): Cienciano 2-0 Universitario, Clausura (es 1-1): fica a RSSSF, com a qual a tabela do Clausura fecha; o 1-1 da es é o jogo do Apertura (abandonado e mantido, agora contado)
- **1914:** vice Jorge Chávez N°1 pela página peru1914; a Wikipédia dá o Sport Alianza (2 fontes x 1: fica a RSSSF) (PE-026)
- **2022:** ajustes de pontos da tabela publicada (Alianza Lima +2, Ayacucho +1, César Vallejo -2) sem terceira fonte que explique a origem; ficam os da tabela (PE-018)
- **1996:** artilheiros Waldir Sáenz (Alianza Lima) e Adrián Czornomaz (Universitario), 20 gols cada, como as Wikipédias em espanhol e em inglês e o national-football-teams.com; a lista da RSSSF (perutops) dá só Sáenz, com 19 (PE-015)
- **1977:** artilheiros pela lista da RSSSF (perutops), igual à Wikipédia em inglês; a es diverge em alguns anos (1934, 1977, 1980, 1981, 1986-1988): fica a RSSSF até uma 3ª fonte (PE-016)
- **1929:** a página da Wikipédia traz os jogos duas vezes (lista das rodadas 1-9 e tabela de confrontos); em três confrontos os placares das duas não batem (Universitario x Ciclista Lima, Universitario x Unión Buenos Aires, Hidroaviación x Ciclista Lima) e os dois jogos ficam; falta um jogo do Atlético Chalaco
- **1931:** a tabela publicada soma pontos de bônus da liga de reservas (um quarto dos pontos dela); a conferência usa só J V E D GP GC

### Identidade dos clubes

Regras em `coleta/per-1/clubes_per.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes peruanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Universitario", "Alianza Lima", "Sporting Cristal", "Melgar", "César
  Vallejo", "Binacional");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Libertad de Trujillo" (o Libertad é o paraguaio),
  "Internazionale de San Borja";
- o mesmo clube com outro nome em outra época fica com o nome atual: Federación Universitaria (até 1930) é o Universitario;
  Sport Alianza (até 1927) é o Alianza Lima; Sucre FBC é o Mariscal Sucre; Inti Gas Deportes (2009-2014) é o Ayacucho;
  Total Clean (Arequipa, 2007-2009) é o Total Chalaco; Real Garcilaso (até 2019) é o Cusco FC; Colegio San Agustín é o Deportivo San Agustín;
- clubes diferentes com o mesmo nome: Alfonso Ugarte de Chiclín (1966-1967) e Alfonso Ugarte (Puno); Sport José Gálvez
  (Lima, 1926) e José Gálvez (Chimbote); Sportivo Melgar (Lima, 1937) e Melgar (Arequipa); Atlético Barrio Frigorífico
  (Callao, 1974) e Alianza Frigorífico (Callao, 1928-1931; a RSSSF o chama de Alianza Callao em 1928, e a Wikipédia liga
  esse nome ao Alianza Frigorífico Nacional);
- Estudiantes de Medicina (Ica) jogou 2004 em Piura como "Grau-Estudiantes" (fusão com o Atlético Grau, desfeita no fim do
  ano): fica Estudiantes de Medicina.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (18):** 1912-1921, 1970-1974, 1976, 1977 e 1979. Pesquisamos RSSSF, ogol (sem jogos peruanos), Wikipédias em espanhol e inglês (as tabelas de confrontos em inglês desses anos estão incompletas) e ESPN (só de 2005 em diante): nenhuma fonte pública traz os jogos. De 1970 em diante entram com a tabela final de `peruhist.html`.
- **Edições com jogos incompletos:** 1926 (torneio suspenso; a Wikipédia tem parte dos jogos), 1982, 1984, 1986, 1988-1991 (anos de Torneo Regional + Descentralizado: a RSSSF tem só as tabelas de parte das fases) e 2003 (as rodadas 16 e 17 do Clausura, jogadas com sub-20 durante a greve, foram anuladas). O que falta está na observação da edição.
- **Fora do pacote:** a Copa Perú, a Segunda División e a Intermedia, as ligas de reservas (que davam pontos de bônus de 1931 a 1934), o Torneo del Inca, a Copa Bicentenario, a Supercopa, as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes de baixo.
- **Edições sem jogos** (18): 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1970, 1971, 1972, 1973, 1974, 1976, 1977, 1979.
- **Décadas com menos da metade dos gols com autor:** 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1912-1921 (Liga Peruana): pela D-06 (A), as edições ficam com a ordem e os participantes das páginas peru1912-1921 (sem jogos, salvo os poucos de 1912 que não entram).
- Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): tabela do ano inteiro como classificação (1970-1979, 1998, 2000, 2009, 2012, 2020 pós-TAS, 2021 com o TAS; soma em 2001, 2004, 2005), final de 2021, Jorge Chávez N°1 x do Callao, rebaixado só com 'Relegated', finais do Torneo de Verano, datas de 1990.
- Abertos fechados em 23/11: PE-010 (final nacional de 1990 como 'Final', em 3/2/1991; a do Regional II à parte), PE-012 (1988: liguilla final como 'Fase final' e o jogo do título como 'Final'), PE-014 (rebaixados pela Wikipédia em espanhol, rebaixados_es.py: 100 clubes em 48 edições), PE-015 (1996: Sáenz e Czornomaz com 20), PE-017 (placares: fica a RSSSF, explicado ano a ano; Cienciano 1-1 Universitario de 2004 contado), PE-022 (Deportivo Bancos em Pucallpa).
- Rebaixados de 1984 a 1991 (Regionais): só os que estão na classificação e saem do campeonato; a maior parte dos clubes regionais desses anos não está na classificação (jogos incompletos).

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/per-1.md`):

- PE-001 (alta) A vice — 1918, 1921: RSSSF peru1918/peru1921: '2. Jorge Chávez No. 2'; Wikipédia es (Palmarés): 'Jorge Chávez Nr. 2' ligado a Club Sportivo Jorge Chávez; Wikipédia en: 'Jorge Chávez (Callao)' — nenhuma diz N°1 | SUGESTÃO: vice 1918 e 1921 = 
- PE-002 (alta) B classificação (anos sem jogos) — 1970, 1972, 1973, 1974, 1977, 1979: RSSSF peruhist: a classificação final é o Championship Group (+ Relegation Group em 1970 e 1979): 1970 Cristal 32 J 71 pts, Universitario 70, Defensor Arica 65, Juan Aurich 57, Defensor Lima 49, Municipal 48, Octavio Esp
- PE-003 (alta) B rebaixados marcados errado — 1938, 1970, 1977, 1979, 2002, 2006, 2008, 2014: RSSSF: 1938 'Alianza Lima 0-2 Sucre FBC [Alianza Lima relegated]'; 1970 só SIMA e Atlético Grau [Relegated]; 1979 só León de Huánuco; 2002 'Juan Aurich relegated'; 2006 José Gálvez caiu no playoff; 2008 'Atlético Minero 
- PE-004 (alta) B classificação e rebaixamento 2020 — 2020: RSSSF peru2020 traz a 2ª tabela anual (decisão do TAS de 17/03/2021 'thereby relegating Carlos Stein instead of Alianza Lima'): Carlos Stein 19º, 25 pts [-3] [Relegated]; Alianza Lima 17º, 26 pts, fica; Wikipédia es Liga
- PE-005 (alta) C final nacional ausente — 2021: RSSSF peru2021, seção Finals: 'First Leg [Nov 21] Alianza Lima 1-0 Sporting Cristal [National Stadium, Lima] (Hernan Barcos 33)'; 'Second Leg [Nov 28] Sporting Cristal 0-0 Alianza Lima' | SUGESTÃO: acrescentar a fase 'Fi
- PE-006 (alta) B classificação 2021 — 2021: RSSSF peru2021 'Final Aggregate Table' (18 clubes, 26 J): Cristal 58, Alianza 56, Universitario 45 [-2], Vallejo 42, Melgar 40, Cienciano 38 [-1], Sport Boys 37 [-1], Ayacucho 37 ... Cusco 25 [-1], USMP 25 [-1], Alianza 
- PE-007 (media) C jogo decidido no TAS — 2021: Wikipédia es (Liga 1 2022, Caso Cusco FC): em 21/01/2022 o TAS devolveu os pontos ao Cienciano: vale o 2-2 de campo | SUGESTÃO: placar oficial 2-2 (sem awd), observação 'TAS 21/01/2022 anulou a vitória dada ao Cusco'; fo
- PE-008 (alta) B classificação de uma fase só — 1998, 2000, 2001, 2004, 2005, 2009, 2012: Wikipédia es, tabela acumulada: 2000 Universitario J44 30-10-4 94:43 100 pts, Cristal 78, Cienciano 71, Melgar 69; 2001 Cristal J44 90 pts, Cienciano 80, Alianza 67; 2004 Cienciano J52 101, Alianza 99, Cristal 95, Alianz
- PE-009 (media) C datas de mata-mata — 1968-2023 (33 edições): ESPN (data local UTC-5): 2023 finais em 2023-11-04 e 2023-11-08; 2021 Final da Fase 1 2021-05-30; 2015 semifinais 2015-12-06 e 12-09; 2011 final 2011-12-08; RSSSF dá a data no título ('First Leg [Nov 21]', 'Playoff [Dec 
- PE-010 (media) C datas e fase de 1990 — 1990: RSSSF peru90: 'Octogonal [Jan 6,13]', 'Liguilla Final Regional II, Round 1 [Jan 20]' (jan/1991); Wikipédia es Campeonato Descentralizado 1990, Final Nacional: Universitario 4-2 Sport Boys, 3 de febrero de 1991, Estadio N
- PE-011 (media) C fase/grupo errados — 1987, 1988: RSSSF peru87 linhas 506-542 e peru88 linhas 548-580: 'Regional Final (in Lima)' com tabela própria (1987 Universitario 7 pts, Unión Huaral 7...; 1988 Universitario 8, Unión Huaral 7...) e 'Regional Championship playoff [
- PE-012 (media) C fase Final com liguilla — 1988: RSSSF peru88 linhas 914-941: liguilla de 6 e depois a final entre o campeão do Regional e o do Descentralizado (nota 2 da página) | SUGESTÃO: fase 'Fase final' (liga, 15 jogos) e 'Final' (1 jogo); fonte: https://www.rsss
- PE-013 (media) C final do Torneo de Verano como Final — 2017, 2018: RSSSF peru2017 linhas 396-400 e peru2018 linhas 393-397: final do Torneo de Verano | SUGESTÃO: fase 'Final do Torneo de Verano' (2017 e 2018); fonte: https://www.rsssf.org/tablesp/peru2017.html , https://www.rsssf.org/ta
- PE-014 (media) B rebaixados sem marca — ~45 edições (1926-1934, 1940, 1947-1951, 1958-1967, 1975, 1976, 1980, 1982-2001, 2003-2005, 2009, 2011-2013, 2021): Wikipédia es, seção 'Ascensos y descensos' de cada temporada (descendidos do ano anterior) | SUGESTÃO: dicionário REBAIXADOS {ano: [clubes]} tirado da Wikipédia es, usado por situacao(); fonte: https://es.wikipedia.org/w
- PE-015 (media) D artilheiro — 1996: Wikipédia es (Goleadores por año) e Wikipédia en (List of Peruvian football champions): Adrián Czornomaz (Universitario) e Waldir Sáenz (Alianza Lima), 20 gols cada | SUGESTÃO: dois artilheiros com 20 gols; fonte: https:
- PE-016 (baixa) D artilheiros divergentes — 1934, 1977, 1980, 1981, 1986, 1987, 1988: Wikipédia es: 1934 Jorge Alcalde e Teodoro Fernández 10; 1977 Ravello 27; 1980 Ramírez 19; 1981 Carranza 18; 1986 Briceño 20; 1987 Suárez 29; 1988 Luis Mora 25 (parece somar Regional + Descentralizado) | SUGESTÃO: manter
- PE-017 (media) C placares RSSSF x Wikipédia es — 1932, 1933, 1941, 1975, 1981, 1995, 1999, 2000, 2004: Wikipédia es (matriz de resultados da temporada): 0-0; 1-3; 1-1; 0-1; 1-2; 1-2; 2-0; 0-1 e 0-0; 1-1 | SUGESTÃO: conferir numa terceira fonte (jornal, dechalaca, transfermarkt para 2004) antes de trocar; fonte: https://es
- PE-018 (media) B pontos 2022 — 2022: Wikipédia es Liga1 2022, tabela acumulada: Alianza 23-6-7 = 75, Ayacucho 26, César Vallejo 60 (ajustar_puntos -3, Resolución N° 046-CCL-FPF-2022) | SUGESTÃO: conferir a origem dos +2/+1 (jogo dado fora de campo?) e o -3 
- PE-019 (media) B classificação 1912-1921 — 1912-1921: RSSSF peru1912-peru1917: classificação completa (1912 com pontos: Lima Cricket 12, Association 12, Jorge Chávez No. 1 9, Sport Alianza 9, Sport Inca 7, Miraflores 4, Vitarte 3, Escuela Militar retirou-se; 1913 8 clubes; 
- PE-021 (baixa) E cidade do clube — 1929-1955: Wikipédia es (Club Sporting Tabaco): fundado em 16/11/1926 no Rímac (Lima) pelos trabalhadores do Estanco de Tabaco | SUGESTÃO: região Lima, cidade Lima; fonte: https://es.wikipedia.org/wiki/Club_Sporting_Tabaco ; mexer 
- PE-022 (baixa) E clube sem cidade — 1991: Wikipédia es Campeonato Descentralizado 1991: joga a Zona Oriente com Unión Tarapoto e CNI | SUGESTÃO: procurar a cidade na página 'Deportivo Bancos' da Wikipédia es ou na RSSSF peru91 (zona Oriente); fonte: https://es.w
- PE-023 (baixa) F documentação — : o per-1 está no banco (109 edições, 17.316 jogos, igual ao pacote) e no painel local | SUGESTÃO: tirar 'Ainda não carregado' da lista PENDENCIAS e corrigir o texto de 1912-1921; mexer em: coleta/comum-sulamerica/document

## 10. Arquivos e comandos

Código em `coleta/per-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga per.1) de 2001 a 2025 para data/coleta/per-1/espn/per1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão peruana para data/coleta/per-1/rsssf/. |
| `baixar_wikipedia.py` | Baixa da Wikipédia em espanhol o texto-fonte das temporadas peruanas ("Campeonato Peruano de Fútbol de <ano>" até 1965, |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "List of Peruvian football champions", seção "List of champions"), |
| `clubes_per.py` | Identidade dos clubes peruanos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão peruana (per-1): uma por título de campeão peruano, como na lista da RSSSF (peruchamp.html). |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão peruana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão peruana e grava o pacote em data/coleta/per-1/pacote/ e o relatório em docs/coleta/per-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/per-1/rsssf/) com o leitor comum (rsssf_sul). Nos anos sem |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `rebaixados_es.py` | Rebaixados por ano pela Wikipédia em espanhol (PE-014): a seção "Ascensos y descensos" da página de cada temporada |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wikipedia_jogos.py` | Jogos da Wikipédia em espanhol (data/coleta/per-1/wikipedia/es_<ano>.txt), para os anos que a RSSSF não tem. |

- Fontes baixadas: `data/coleta/per-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`.
- Pacote: `data/coleta/per-1/pacote/`; relatório: `docs/coleta/per-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/per-1/baixar_espn.py
python coleta/per-1/baixar_rsssf.py
python coleta/per-1/baixar_wikipedia.py
python coleta/per-1/importar.py
python coleta/per-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py per-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

