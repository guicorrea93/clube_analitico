# Campeonato Colombiano (`col-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/col-1/pacote/`, do código `coleta/col-1/` e do relatório `docs/coleta/col-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 101, de 1948 a 2025 Finalización; 6 sem jogos.
- **Jogos:** 23418 (23406 com placar); **gols:** 62516; **gols com autor:** 22905 (37%); **cartões:** 40526.
- **Clubes:** 42; **artilheiros:** 100 edições com artilheiro (123 linhas, com empates).
- **Classificação final:** 101 edições; **tabelas publicadas guardadas para conferência:** 2334 linhas.
- **No banco:** sim; **último commit do pacote:** fd64e74e.
- **Observação da competição:** 1ª divisão colombiana de 1948 a 2025: um campeão por ano até 2001 (1989 sem campeão; 1995/96 e 1996/97 no calendário europeu) e uma edição por torneio (Apertura e Finalización) de 2002 em diante. Jogos de 1948-1986, 1988-1990 e 1995/96 em diante; 1987 e 1991-1995 só com a tabela final e o campeão.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão colombiana (col-1): uma por torneio que deu título de campeão colombiano.

Lista de títulos: RSSSF (colchamp.html), conferida com a Wikipédia. De 1948 a 2001 um campeão por ano (Apertura e
Finalización, de 1968 em diante, são fases da edição anual, com os quadrangulares, hexagonais e octogonais finais); 1989
não teve campeão (a fase final não foi jogada); 1995 foi a temporada de transição e 1995/96 e 1996/97 seguiram o calendário
europeu. De 2002 em diante, Apertura e Finalización dão título cada um: uma edição por torneio (em 2020 só houve o Apertura;
o Finalización foi cancelado). Ficam de fora a Copa Colombia, a Superliga, as liguillas e os jogos de promoção.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO). 1995/96 em diante.
- wiki: chave da página da Wikipédia em espanhol (wikipedia_jogos.py): 1948-1986, 1988-1990, 2011, 2012 e 2025.
- tabelas: trechos da RSSSF lidos só pelas tabelas (conferência e classificação dos anos da Wikipédia e dos anos sem jogos).
- sem jogos: 1987 e 1991-1995 (nenhuma fonte pública tem os jogos): tabela final e campeão.
```

**Edições:** 101, uma por título de campeão colombiano da 1ª divisão, de 1948 a 2025, como na lista de campeões da RSSSF (`colchamp.html`) e na Wikipédia em inglês. Até 2001 um campeão por ano: de 1968 em diante, Apertura e Finalización (e os quadrangulares, hexagonais e octogonais finais) são fases da edição anual. 1989 entra sem campeão (a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega); 1995 foi o torneio de transição e 1995/96 e 1996/97 seguiram o calendário europeu. De 2002 em diante, Apertura e Finalización dão título cada um: uma edição por torneio (em 2020 só houve o Apertura).

**Fontes:** RSSSF (uma página por temporada, `data/coleta/col-1/rsssf/`: base de jogos de 1995/96 em diante, menos 2011, 2012 e 2025, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas de todos os anos são a conferência); Wikipédia em espanhol (páginas "Campeonato colombiano <ano>" e "Torneo Apertura <ano> (Colombia)": jogos de 1948-1986, 1988-1990, 2011, 2012 e 2025, por rodada ou em tabela de confrontos, sem autores dos gols, e as finais com data e estádio); ESPN (liga `col.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol não tem os jogos da liga colombiana.

**Clubes:** Deportes Caldas (campeão em 1950) entra como Once Caldas, como a RSSSF e o próprio clube contam; Atlético Municipal é o Atlético Nacional; Cristal Caldas, o Once Caldas; Itagüí, o Águilas Doradas; La Equidad, o Internacional de Bogotá (2025); Alianza Petrolera, o Alianza FC (2024). Homônimos de outros países levam a cidade: Libertad de Barranquilla, Universidad Nacional de Bogotá, Boca Juniors de Cali, Huracán de Medellín.

**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela). Jogo decidido no tribunal leva o placar dado (`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (as tabelas de vários anos têm pontos de bônus, que vão em `ajuste_pontos`).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 51.
- **Edições com alguma tabela divergente** (41; motivo no relatório, na edição): 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1956, 1957, 1958, 1959, 1960, 1962, 1963, 1964, 1965, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1988, 1990, 1995/96, 1999, 2003 Apertura, 2005 Finalización, 2006 Finalización, 2012 Finalización.
- **Edições sem tabela para conferir** (9): 1966, 1987, 1989, 1991, 1992, 1993, 1994, 1995, 1998.
- **Edições com menos jogos que o esperado:** 1952 (209 de 210), 1953 (131 de 132), 1964 (311 de 312), 2005 Finalización (187 de 188).
- **Edições com mais jogos que o esperado** (desempates e jogos fora da tabela publicada): 2006 Finalización (188 de 179), 2007 Finalización (189 de 188), 2009 Apertura (189 de 188), 2009 Finalización (189 de 188), 2010 Finalización (189 de 188).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1940s | 2 | 274 | 64% | 0% | 64% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 1915 | 35% | 0% | 40% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 3182 | 66% | 0% | 77% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 3646 | 22% | 0% | 41% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 2466 | 21% | 0% | 73% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1729 | 92% | 0% | 97% | 0% | 0% | 0% | 2% | 0.0 |
| 2000s | 18 | 3824 | 100% | 44% | 100% | 44% | 44% | 0% | 99% | 1.2 |
| 2010s | 20 | 3969 | 100% | 97% | 98% | 97% | 97% | 50% | 87% | 5.6 |
| 2020s | 11 | 2413 | 100% | 100% | 98% | 100% | 100% | 70% | 99% | 5.7 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1948: 10 clubes
- 1949: 14 clubes
- 1950: 16 clubes
- 1951: 18 clubes
- 1952: 15 clubes
- 1953: 12 clubes
- 1954 a 1955: 10 clubes
- 1956: 13 clubes
- 1957: 12 clubes
- 1958: 10 clubes
- 1959 a 1962: 12 clubes
- 1963 a 1965: 13 clubes
- 1966 a 1985: 14 clubes
- 1986: 8 clubes
- 1987: 14 clubes
- 1988 a 1991: 15 clubes
- 1992 a 2001: 16 clubes
- 2002 Apertura a 2014 Finalización: 18 clubes
- 2015 Apertura a 2020 Apertura: 20 clubes
- 2021 Apertura: 19 clubes
- 2021 Finalización a 2025 Finalización: 20 clubes

**Pontos por vitória:**

- 1948 a 1994: 2
- 1995 a 2025 Finalización: 3

**Nome oficial:**

- 1948 a 1995: Campeonato Profesional Colombiano <ano>
- 1995/96 a 1996/97: Campeonato Profesional Colombiano <ano> (Copa Mustang)
- 1998 a 2001: Campeonato Profesional Colombiano <ano>
- 2002 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2002 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2003 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2003 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2004 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2004 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2005 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2005 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2006 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2006 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2007 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2007 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2008 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2008 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2009 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2009 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2010 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2010 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2011 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2011 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2012 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2012 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2013 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2013 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2014 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2014 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2015 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2015 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2016 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2016 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2017 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2017 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2018 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2018 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2019 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2019 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2020 Apertura a 2021 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2021 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2022 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2022 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2023 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2023 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2024 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2024 Finalización: Campeonato Profesional Colombiano <ano> – Finalización
- 2025 Apertura: Campeonato Profesional Colombiano <ano> – Apertura
- 2025 Finalización: Campeonato Profesional Colombiano <ano> – Finalización

**Formato** (fases na ordem, do edicoes.csv):

- 1948: pontos corridos
- 1949: pontos corridos + mata-mata
- 1950 a 1956: pontos corridos
- 1957: pontos corridos + 2 grupos + desempate + mata-mata
- 1958 a 1967: pontos corridos
- 1968: pontos corridos + mata-mata
- 1969: pontos corridos + desempate
- 1970: pontos corridos
- 1971: pontos corridos + desempate
- 1972 a 1973: pontos corridos
- 1974: pontos corridos + mata-mata + pontos corridos
- 1975: pontos corridos
- 1976: pontos corridos + mata-mata + pontos corridos
- 1977: pontos corridos
- 1978: pontos corridos + 2 grupos + pontos corridos
- 1979: pontos corridos + mata-mata + pontos corridos + 2 grupos + pontos corridos
- 1980: pontos corridos + mata-mata + pontos corridos + desempate
- 1981: pontos corridos
- 1982: pontos corridos + mata-mata + pontos corridos
- 1983 a 1986: pontos corridos
- 1987: sem jogos (só a tabela final)
- 1988 a 1989: pontos corridos
- 1990: pontos corridos + 2 grupos + pontos corridos
- 1991 a 1995: sem jogos (só a tabela final)
- 1995/96: pontos corridos
- 1996/97: pontos corridos + 2 grupos + pontos corridos
- 1998: pontos corridos + 2 grupos + mata-mata
- 1999: pontos corridos + mata-mata + 2 grupos + mata-mata
- 2000: pontos corridos + mata-mata
- 2001 a 2009 Finalización: pontos corridos + 2 grupos + mata-mata
- 2010 Apertura: pontos corridos + mata-mata
- 2010 Finalización: pontos corridos + 2 grupos + mata-mata
- 2011 Apertura a 2011 Finalización: pontos corridos + mata-mata
- 2012 Apertura a 2013 Finalización: pontos corridos + 2 grupos + mata-mata
- 2014 Apertura: pontos corridos + mata-mata
- 2014 Finalización: pontos corridos + 2 grupos + mata-mata
- 2015 Apertura a 2018 Finalización: pontos corridos + mata-mata
- 2019 Apertura a 2019 Finalización: pontos corridos + 2 grupos + mata-mata
- 2020 Apertura a 2021 Apertura: pontos corridos + mata-mata
- 2021 Finalización a 2025 Finalización: pontos corridos + 2 grupos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1949: Primeira fase (liga); Final (mata_mata, ida_volta)
- 1957: Primeira fase (liga); Octogonal (cancelado) (liga); Hexagonal final (grupos, 2 grupos); Desempate do grupo (mata_mata, ida_volta); Final dos hexagonais (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1968: Primeira fase (liga); Finalización (liga); Tercer lugar (liga); Final (mata_mata, ida_volta)
- 1969: Apertura (liga); Finalización (liga); Triangulares (liga); Desempate do título (mata_mata, ida_volta)
- 1970: Apertura (liga); Finalización (liga); Quadrangular final (liga)
- 1971: Apertura (liga); Finalización (liga); Quadrangular final (liga); Desempate do título (mata_mata, ida_volta)
- 1972: Apertura (liga); Finalización (liga); Triangulares (liga)
- 1973: Apertura (liga); Finalización (liga); Triangulares (liga)
- 1974: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Finalización (liga); Hexagonal final (liga)
- 1975: Apertura (liga); Finalización (liga); Hexagonal final (liga)
- 1976: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Finalización (liga); Hexagonal final (liga)
- 1977: Apertura (liga); Finalización (liga); Hexagonal final (liga)
- 1978: Apertura (liga); Finalización (liga); Quadrangulares semifinais (grupos, 2 grupos); Quadrangular final (liga)
- 1979: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Finalización (liga); Quadrangulares semifinais (grupos, 2 grupos); Quadrangular final (liga)
- 1980: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Finalización (liga); Desempate do título (mata_mata, ida_volta)
- 1981: Apertura (liga); Finalización (liga)
- 1982: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Finalización (liga); Octogonal final (liga)
- 1983: Copa de la Paz (liga); Torneo Nacional (liga); Octogonal final (liga)
- 1984: Copa de la Paz (liga); Torneo Nacional (liga); Octogonal final (liga)
- 1985: Copa de la Paz (liga); Torneo Nacional (liga); Octogonal final (liga)
- 1988: Apertura (liga); Octogonal final (liga)
- 1989: Apertura (liga); Finalización (liga); Quadrangulares semifinais (liga)
- 1990: Apertura (liga); Finalización (liga); Quadrangulares semifinais (grupos, 2 grupos); Quadrangular final (liga)
- 1995/96: Copa Mustang I (liga); Quadrangulares semifinais (liga)
- 1996/97: Copa Mustang I (liga); Copa Mustang II (grupos, 2 grupos); Quadrangular final (liga)
- 1998: Primeira fase (liga); Segunda fase (grupos, 2 grupos); Octogonal final (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1999: Apertura (liga); Finalización (liga); Final do Finalización (mata_mata, ida_volta); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2000: Torneo Mustang I (liga); Torneo Mustang II (liga); Finalísima (mata_mata, ida_volta)
- 2001: Torneo Mustang I (liga); Torneo Mustang II (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2002 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2002 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2003 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2004 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2004 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2005 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2006 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2006 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2007 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2007 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2008 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2009 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2010 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2011 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Finalización: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2012 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2013 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2013 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2014 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2014 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2015 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2015 Finalización: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Finalización: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017 Finalización: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2018 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2018 Finalización: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2019 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2020 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2022 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2022 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2023 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2024 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2024 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2025 Apertura: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2025 Finalización: Primeira fase (liga); Quadrangulares semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- calculada: 92 edições
- RSSSF: 9 edições

**Observações das edições:**

- 1989: título não concedido: a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega (RSSSF)
- 1995: torneio de transição para o calendário europeu (Torneo Nivelación)
- 2011 Apertura: jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- 2011 Finalización: jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- 2012 Apertura: jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- 2012 Finalización: jogos da Wikipédia em espanhol: a página da RSSSF só traz os mata-matas
- 2025 Apertura: jogos da Wikipédia em espanhol: a página da RSSSF só traz as tabelas
- 2025 Finalización: jogos da Wikipédia em espanhol: a página da RSSSF só traz as tabelas

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Atlético Nacional: 18
- Millonarios: 16
- América de Cali: 15
- Junior de Barranquilla: 11
- Independiente Santa Fe: 10
- Deportivo Cali: 10
- Independiente Medellín: 6
- Once Caldas: 4
- Deportes Tolima: 3
- Deportes Quindío: 1
- Unión Magdalena: 1
- Deportivo Pasto: 1
- Cúcuta Deportivo: 1
- Boyacá Chicó: 1
- Deportivo Pereira: 1
- Atlético Bucaramanga: 1
- Sem campeão: 1989

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1948 | Independiente Santa Fe | Junior de Barranquilla |
| 1949 | Millonarios | Deportivo Cali |
| 1950 | Once Caldas | Millonarios |
| 1951 | Millonarios | Boca Juniors de Cali |
| 1952 | Millonarios | Boca Juniors de Cali |
| 1953 | Millonarios | Deportes Quindío |
| 1954 | Atlético Nacional | Deportes Quindío |
| 1955 | Independiente Medellín | Atlético Nacional |
| 1956 | Deportes Quindío | Millonarios |
| 1957 | Independiente Medellín | Deportes Tolima |
| 1958 | Independiente Santa Fe | Millonarios |
| 1959 | Millonarios | Independiente Medellín |
| 1960 | Independiente Santa Fe | América de Cali |
| 1961 | Millonarios | Independiente Medellín |
| 1962 | Millonarios | Deportivo Cali |
| 1963 | Millonarios | Independiente Santa Fe |
| 1964 | Millonarios | Cúcuta Deportivo |
| 1965 | Deportivo Cali | Atlético Nacional |
| 1966 | Independiente Santa Fe | Independiente Medellín |
| 1967 | Deportivo Cali | Millonarios |
| 1968 | Unión Magdalena | Deportivo Cali |
| 1969 | Deportivo Cali | América de Cali |
| 1970 | Deportivo Cali | Junior de Barranquilla |
| 1971 | Independiente Santa Fe | Atlético Nacional |
| 1972 | Millonarios | Deportivo Cali |
| 1973 | Atlético Nacional | Millonarios |
| 1974 | Deportivo Cali | Atlético Nacional |
| 1975 | Independiente Santa Fe | Millonarios |
| 1976 | Atlético Nacional | Deportivo Cali |
| 1977 | Junior de Barranquilla | Deportivo Cali |
| 1978 | Millonarios | Deportivo Cali |
| 1979 | América de Cali | Independiente Santa Fe |
| 1980 | Junior de Barranquilla | Deportivo Cali |
| 1981 | Atlético Nacional | Deportes Tolima |
| 1982 | América de Cali | Deportes Tolima |
| 1983 | América de Cali | Junior de Barranquilla |
| 1984 | América de Cali | Millonarios |
| 1985 | América de Cali | Deportivo Cali |
| 1986 | América de Cali | Deportivo Cali |
| 1987 | Millonarios | América de Cali |
| 1988 | Millonarios | Atlético Nacional |
| 1989 | — | — |
| 1990 | América de Cali | Atlético Nacional |
| 1991 | Atlético Nacional | América de Cali |
| 1992 | América de Cali | Atlético Nacional |
| 1993 | Junior de Barranquilla | Independiente Medellín |
| 1994 | Atlético Nacional | Millonarios |
| 1995 | Junior de Barranquilla | América de Cali |
| 1995/96 | Deportivo Cali | Millonarios |
| 1996/97 | América de Cali | Atlético Bucaramanga |
| 1998 | Deportivo Cali | Once Caldas |
| 1999 | Atlético Nacional | América de Cali |
| 2000 | América de Cali | Junior de Barranquilla |
| 2001 | América de Cali | Independiente Medellín |
| 2002 Apertura | América de Cali | Atlético Nacional |
| 2002 Finalización | Independiente Medellín | Deportivo Pasto |
| 2003 Apertura | Once Caldas | Junior de Barranquilla |
| 2003 Finalización | Deportes Tolima | Deportivo Cali |
| 2004 Apertura | Independiente Medellín | Atlético Nacional |
| 2004 Finalización | Junior de Barranquilla | Atlético Nacional |
| 2005 Apertura | Atlético Nacional | Independiente Santa Fe |
| 2005 Finalización | Deportivo Cali | Real Cartagena |
| 2006 Apertura | Deportivo Pasto | Deportivo Cali |
| 2006 Finalización | Cúcuta Deportivo | Deportes Tolima |
| 2007 Apertura | Atlético Nacional | Atlético Huila |
| 2007 Finalización | Atlético Nacional | Internacional de Bogotá |
| 2008 Apertura | Boyacá Chicó | América de Cali |
| 2008 Finalización | América de Cali | Independiente Medellín |
| 2009 Apertura | Once Caldas | Junior de Barranquilla |
| 2009 Finalización | Independiente Medellín | Atlético Huila |
| 2010 Apertura | Junior de Barranquilla | Internacional de Bogotá |
| 2010 Finalización | Once Caldas | Deportes Tolima |
| 2011 Apertura | Atlético Nacional | Internacional de Bogotá |
| 2011 Finalización | Junior de Barranquilla | Once Caldas |
| 2012 Apertura | Independiente Santa Fe | Deportivo Pasto |
| 2012 Finalización | Millonarios | Independiente Medellín |
| 2013 Apertura | Atlético Nacional | Independiente Santa Fe |
| 2013 Finalización | Atlético Nacional | Deportivo Cali |
| 2014 Apertura | Atlético Nacional | Junior de Barranquilla |
| 2014 Finalización | Independiente Santa Fe | Independiente Medellín |
| 2015 Apertura | Deportivo Cali | Independiente Medellín |
| 2015 Finalización | Atlético Nacional | Junior de Barranquilla |
| 2016 Apertura | Independiente Medellín | Junior de Barranquilla |
| 2016 Finalización | Independiente Santa Fe | Deportes Tolima |
| 2017 Apertura | Atlético Nacional | Deportivo Cali |
| 2017 Finalización | Millonarios | Independiente Santa Fe |
| 2018 Apertura | Deportes Tolima | Atlético Nacional |
| 2018 Finalización | Junior de Barranquilla | Independiente Medellín |
| 2019 Apertura | Junior de Barranquilla | Deportivo Pasto |
| 2019 Finalización | América de Cali | Junior de Barranquilla |
| 2020 Apertura | América de Cali | Independiente Santa Fe |
| 2021 Apertura | Deportes Tolima | Millonarios |
| 2021 Finalización | Deportivo Cali | Deportes Tolima |
| 2022 Apertura | Atlético Nacional | Deportes Tolima |
| 2022 Finalización | Deportivo Pereira | Independiente Medellín |
| 2023 Apertura | Millonarios | Atlético Nacional |
| 2023 Finalización | Junior de Barranquilla | Independiente Medellín |
| 2024 Apertura | Atlético Bucaramanga | Independiente Santa Fe |
| 2024 Finalización | Atlético Nacional | Deportes Tolima |
| 2025 Apertura | Independiente Santa Fe | Independiente Medellín |
| 2025 Finalización | Junior de Barranquilla | Deportes Tolima |

**Rebaixados marcados na classificação:** 43 em 31 edições (só onde a tabela publicada marca a queda); quem mais caiu: Unión Magdalena (5), Real Cartagena (4), Cúcuta Deportivo (4), Cortuluá (4), Atlético Huila (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1995: Cortuluá -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/col-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 88)

- **1957 · wiki-es_1957:1090:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1094:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1114:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1118:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1122:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1126:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1140:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1144:** [anulado, fase = Octogonal (cancelado)] octogonal cancelado depois de 3 rodadas ("Octogonal (Cancelado)") (CO-013)
- **1957 · wiki-es_1957:1312:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1316:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1320:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1332:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1336:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1340:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1354:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1358:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1362:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1374:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1378:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1382:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1396:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1400:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1404:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1416:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1420:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1424:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1438:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1442:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1446:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1458:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1462:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1466:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1480:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1484:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1488:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1500:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1504:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1508:** [grupo = A] hexagonal do grupo A (CO-013)
- **1957 · wiki-es_1957:1713:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1717:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1721:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1733:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1737:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1741:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1755:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1759:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1763:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1775:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1779:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1783:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1797:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1801:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1805:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1817:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1821:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1825:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1839:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1843:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1847:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1859:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1863:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1867:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1881:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1885:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1889:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1901:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1905:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1909:** [grupo = B] hexagonal do grupo B (CO-013)
- **1957 · wiki-es_1957:1650:** [fase = Desempate do grupo, grupo = A] desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- **1957 · wiki-es_1957:1655:** [fase = Desempate do grupo, grupo = A] desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- **1957 · wiki-es_1957:1660:** [fase = Desempate do grupo, grupo = A] desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)
- **1957 · wiki-es_1957:1992:** [fase = Final dos hexagonais, grupo = ] final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- **1957 · wiki-es_1957:1998:** [fase = Final dos hexagonais, grupo = ] final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- **1957 · wiki-es_1957:2004:** [fase = Final dos hexagonais, grupo = ] final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)
- **1974 · wiki-es_1974:935:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1974 · wiki-es_1974:941:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1976 · wiki-es_1976:409:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1976 · wiki-es_1976:415:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1979 · wiki-es_1979:1375:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1979 · wiki-es_1979:1381:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1980 · wiki-es_1980:400:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1980 · wiki-es_1980:406:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1982 · wiki-es_1982:1375:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1982 · wiki-es_1982:1381:** [fase = Final do Apertura] final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)
- **1999 · col99:675:** [fase = Final do Finalización] final do Clausura (Medellín x Nacional), não a do ano (CO-014)
- **1999 · col99:678:** [fase = Final do Finalización] final do Clausura (Medellín x Nacional), não a do ano (CO-014)
- **2008 Apertura · col08:328:** [descartado] jogo suspenso e completado depois: fica a linha do jogo completo (CO-021)
- **2013 Finalización · col2013:795:** [descartado] jogo suspenso pela chuva e completado depois (CO-021)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 4)

- **1966:** 350 dos 364 jogos: nem a RSSSF nem a Wikipédia em espanhol (baixada de novo em 24/11/2026, igual) trazem os jogos que faltam, e a pesquisa por uma 3ª fonte não achou outra (CO-004)
- **1986:** só 21 jogos do octogonal e 8 dos 14 clubes na classificação: nem a RSSSF nem a Wikipédia em espanhol (baixada de novo em 24/11/2026, igual) trazem os jogos que faltam, e a pesquisa por uma 3ª fonte não achou outra (CO-006)
- **1988:** Finalización com 12 jogos por clube (de 28): nem a RSSSF nem a Wikipédia em espanhol (baixada de novo em 24/11/2026, igual) trazem os jogos que faltam, e a pesquisa por uma 3ª fonte não achou outra (CO-006)
- **2001:** América de Cali 2-2 Once Caldas (1ª rodada dos quadrangulares, 18/11): a Wikipédia em espanhol dá 0-0; fica o 2-2 da RSSSF, confirmado por uma 3ª fonte (arquivo da FutbolRed: 2-2 no Pascual Guerrero, gols de David Ferreira e Julián Vásquez) (CO-015)

### Identidade dos clubes

Regras em `coleta/col-1/clubes_col.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes colombianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Millonarios", "Atlético Nacional", "América de Cali", "Junior de
  Barranquilla", "Independiente Santa Fe", "Independiente Medellín");
- homônimo de clube do banco ou de outro pacote leva a cidade ("Libertad de Barranquilla", "Universidad Nacional de Bogotá");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte: Atlético Municipal ->
  Atlético Nacional; Atlético Quindío -> Deportes Quindío; Cristal Caldas -> Once Caldas; Itagüí (Ditaires) -> Águilas
  Doradas (mudou para Pereira em 2015 e para Rionegro em 2016); La Equidad -> Internacional de Bogotá (2025); Alianza
  Petrolera -> Alianza FC (Valledupar, 2024); Chicó -> Boyacá Chicó; Corporación Tuluá -> Cortuluá;
- Deportes Caldas (campeão em 1950) entra como Once Caldas, como a RSSSF e o próprio Once Caldas contam (o Once Caldas
  nasceu em 1961 da fusão do Deportes Caldas com o Once Deportivo); o Once Deportivo fica separado.

As tabelas da RSSSF põem os pontos de bônus no nome ("América Cali (1 BP)") e a de 1995 abre a linha com "- ": saem antes da
regra. REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (6):** 1987 e 1991-1995. Nenhuma fonte pública que achamos tem os jogos desses anos (a RSSSF e a Wikipédia trazem só as tabelas; o ogol tem as edições vazias). Elas entram com a tabela final da RSSSF como classificação e o campeão. Em 1986 a Wikipédia traz só parte do octogonal final.
- **Fora do pacote:** a Copa Colombia, a Superliga, as liguillas, o Torneo Adecuación 1997 e os jogos de promoção.
- **Edições sem jogos** (6): 1987, 1991, 1992, 1993, 1994, 1995.
- **Décadas com menos da metade dos gols com autor:** 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1987 e 1991-1995 sem jogos: nenhuma fonte pública tem (só tabela final e campeão).
- Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): vice pela colchamp, ordem por fase alcançada (D-02 A), tabelas finais de 1987 e 1991-1995 só com a Primera A, rebaixados pela es, 1964 sem jogos repetidos, Finalización e quadrangulares como fase de pontos, finais do Apertura em nível 0, datas de 1957 e 1971, artilheiros de 1971, 1977 e 1978.
- Abertos fechados em 24/11: CO-004 (3ª e 4ª voltas de 1955-1963 pela Wikipédia: 1955, 1958, 1960, 1961 e 1963 completos; 1959 com 261 de 264), CO-006 (1989 com as listas 'Fecha N', 242 jogos; hexagonal de 1976 completo), CO-009 (final de 2025 com {{fecha}} e a ESPN certa), CO-012 (grupos dos quadrangulares pelas tabelas; 1ª fase sem grupo), CO-013 (1957: octogonal cancelado, hexagonais A e B, desempate do grupo A, final dos hexagonais), CO-015 (1948 e 1949 pela tabela de confrontos da RSSSF), CO-016 (bônus da fase final na observação), CO-017 (artilheiros de 2008 em diante pela Wikipédia em espanhol), CO-018, CO-020 (data no título da rodada: 976 jogos) e as chaves 'wiki:' do CORRIGE, que nunca valeram (finais do Apertura de 1974-1982).
- Ainda abertos: CO-006 (1986 e 1988: a Wikipédia não tem os jogos que faltam), CO-004 (1966: 350 de 364), CO-015 (placares de 2001-2018 que só uma 3ª fonte decide) e CO-022 (esperados() e diagnóstico do relatório).

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/col-1.md`):

- CO-001 (alta) A vice — 55 edições: 1955, 1957, 1958, 1959, 1961, 1969, 1970, 1976, 1978, 1979, 1981, 1982, 1984, 1989, 1992, 1993, 1994, 1995/96, 1996/97, 2000, 2001, 2002 Ap e Fi, 2004 Ap e Fi, 2006 Ap, 2007 Ap, 2008 Ap e Fi, 2009 Ap e Fi, 2010 Ap, 2011 Ap e Fi, 2012 Ap, 2013 Fi, 2014 Ap, 2015 Ap, 2016 Ap e Fi, 2017 Ap e Fi, 2018 Fi, 2019 Ap e Fi, 2021 Ap e Fi, 2022 Ap e Fi, 2023 Ap e Fi, 2024 Ap e Fi, 2025 Ap e Fi: RSSSF colchamp (coluna Runners Up, que a coleta não leu) e Wikipédia es concordam nas 101 edições: ex. 2002 Ap Atlético Nacional (perdeu a final para o América), 2024 Fi Deportes Tolima, 1957 Deportes Tolima, 1976 Deport
- CO-002 (alta) B classificação — 2002 Apertura a 2025 Finalización (todas com fase final) e 1967, 1976, 1996/97, 1999, 2000, 2001: o campeão sai da final; vice = perdedor da final; 3º/4º = semifinalistas ou 2º dos quadrangulares (RSSSF colNN, seções Cuadrangulares/Final) | SUGESTÃO: ordenar por fase alcançada (Final > quadrangular/semifinal > quarta
- CO-003 (alta) B classificação — 1987, 1991, 1992, 1993, 1994, 1995 (sem jogos): RSSSF traz a tabela final de cada ano (col95: 'Final Table Primera A', 16 clubes, Junior 30 18 8 4 66-37 62; Tuluá -2 pts; Cúcuta relegated) | SUGESTÃO: usar a tabela final da RSSSF como classificação (como a ficha diz q
- CO-004 (alta) C jogos — 1955, 1958, 1959, 1960, 1961, 1963, 1966: RSSSF 'Final Table' de cada ano (1960: 12 clubes x 44 jogos; Wikipédia es 1960 tem 'Tercera vuelta' e 'Cuarta vuelta'; 1963: 52 fechas, 312 jogos) | SUGESTÃO: ler as 4 voltas e as listas 'Fecha N' da Wikipédia es (1963: 
- CO-005 (alta) C jogos — 1964: RSSSF col64: 13 clubes x 48 jogos = 312; Wikipédia es tem a matriz (156 jogos, só o 1º placar) E a lista 'Fecha 1..52' (311 jogos): o leitor pegou as duas | SUGESTÃO: só a lista 'Fecha N' (com data); descartar a matriz q
- CO-006 (alta) C jogos — 1986, 1988, 1989, 1976: RSSSF col86 (tabelas do Apertura e Clausura, 14 clubes), col88 (Finalización 28 jogos por clube), col89 ('318 matches'), col76 (Final Hexagonal, Round 1 a 10 com 3 jogos cada); Wikipédia es 1989 tem 'Fecha 1 (Marzo 5)'..
- CO-007 (alta) B rebaixados — 1992 a 2025 (45 rebaixamentos): Wikipédia es Anexo Ascensos y descensos (46 rebaixamentos 1992-2025) e as seções 'Relegation' das páginas da RSSSF (ex.: col2024: 'decided over points average') | SUGESTÃO: dicionário REBAIXADOS {temporada: [clubes]} na 
- CO-008 (media) C datas — 48 edições de 1995/96 a 2024 Finalización (finais, semifinais, quartas): RSSSF escreve 'First Leg [Dec 18]' / 'Second Leg [Dec 22]' (col2024 linhas 938-942); ESPN e Wikipédia es confirmam (2024 Fi: 18/12 e 22/12; 2016 Ap: 15/06 e 19/06) | SUGESTÃO: ler a data de 'First/Second Leg(s) [Mon DD]'
- CO-009 (media) C jogo ligado errado — 2025 Finalización: Wikipédia es Torneo Finalización 2025 (== Final ==): {{fecha|12|12|2025}} Junior 3:0 Tolima e {{fecha|16|12|2025}} Tolima 0:1 Junior; a ESPN casada (736069, 730445) é do Apertura (1-1 e 0-0); os certos são 762528 (públic
- CO-010 (media) C datas — 1957; 1971: Wikipédia es 1957: desempate 'diciembre 08/1957-febrero 02/1958', final 19 e 23 de março (de 1958); Wikipédia es 1971 'Desempate final': 'El 10 de febrero de 1972' | SUGESTÃO: 1958-03-19, 1958-03-23; 1972-01-30, 1972-02-
- CO-011 (media) C fases — 1969 a 1999 (Finalización) e todas com quadrangulares/hexagonais/octogonais: RSSSF: Finalización é liga (às vezes em 2 grupos) e os quadrangulares/hexagonais são grupos de pontos corridos (col02 'Cuadrangulares: Tables Group A/B') | SUGESTÃO: Finalización tipo liga/grupos; quadrangulares, hexagon
- CO-012 (media) C grupos — 2001 a 2024 (menos 2012-2014) e 1989, 1995/96, 1999; 1ª fase de 2002 Ap a 2025 Fi (33 edições): RSSSF col02: 1ª fase é uma tabela única de 18 clubes (22 rodadas); 'Group A: Nacional, Magdalena, Cali, Pasto / Group B: América, Santa Fe, Envigado, Bucaramanga' | SUGESTÃO: grupo do quadrangular pelo clube (tabelas Gro
- CO-013 (media) C fases — 1957: Wikipédia es 1957: '== Octogonal (Cancelado) ==', '== Grupos hexagonales == Grupo A / Grupo B', 'Desempate Grupo A', Final Medellín x Cúcuta | SUGESTÃO: octogonal como jogos anulados (resultado_especial n/p) ou fora; hex
- CO-014 (media) C fases — 1974, 1976, 1979, 1980, 1982; 1999: Wikipédia es: 'En el Apertura [1980] disputaron la final, la cual ganaría Junior'; RSSSF col99 'Final Clausura' (linha 669) x 'Championship Final' (linha 699) | SUGESTÃO: fase 'Final do Apertura' / 'Final do Finalización
- CO-015 (media) C placares — 1948, 1949, 1974, 1977, 1979, 2001 e jogos 2005-2018 com a ESPN: RSSSF Cross-Table col48/col49 (fonte independente da Wikipédia, base da coleta nesses anos), jogos das fases finais col74-col79, Wikipédia es 2001, ESPN | SUGESTÃO: corrigir 1948-1949 pela tabela de confrontos da RSSSF (
- CO-016 (media) B ajustes de pontos — 1983 a 1999 (fases finais) e 1995: RSSSF 'Bonus Table' em col83-col88, col93, col94; '[BP: 1.5]' em col98; 'Top-4 of Apertura and Finalizacion obtain bonus points' em col90-col92; col95 '11.Deportivo Tulua ... [2 pts deducted]' | SUGESTÃO: bônus em ajuste
- CO-017 (media) D artilheiros — 1971, 1977, 1978; 2008-2025: RSSSF coltops: '1977 Oswaldo Marcial PALAVECINO (Arg.) Atlético Nacional 33', 1978 idem 36, 1971 Paniagua 30 (Pereira); a coltops acaba em 2007; Wikipédia es (Máximo goleador): 2013 Ap Wilder Medina 12, 2016 Ap Miguel Bo
- CO-018 (media) D gols com autor — 2007 Apertura; 2008 Finalización; 2010 Apertura: placar da RSSSF x lances da ESPN do mesmo jogo (ESPN 2010: Pereira 1-3 Cali) | SUGESTÃO: só gravar os gols quando a soma por lado bate com o placar; conferir o placar numa 3ª fonte; mexer em: coleta/col-1/importar.py gra
- CO-019 (baixa) A clubes por edição — 1986, 1989, 1995: RSSSF/Wikipédia es: 14 (1986), 15 (1989), 16 (1995) | SUGESTÃO: sai junto com a correção dos jogos e das tabelas (achados de 1986/1989 e 1995); fonte: https://www.rsssf.org/tablesc/col86.html, col95.html; mexer em: colet
- CO-020 (baixa) C cobertura de datas — 1952-1963, 1968-1988: Wikipédia es: 'Fecha 1 — 1 de marzo de 1964', 'Fecha 1 septiembre 14' (1957), 'Fecha 1 (Marzo 5)' (1989); contagem por ano em revisao/CO/saida_cobertura_datas.txt | SUGESTÃO: ler a data do título da rodada nos formatos '
- CO-021 (baixa) C jogos suspensos — 2008 Apertura; 2013 Finalización: RSSSF col08 linha 328 'abandoned at 1-0 ... due to rain' + linha 330 'remaining time' | SUGESTÃO: descartar a 1ª linha em CORRIGE (regra do COMECE-AQUI, seção 6) e datar o complemento; mexer em: coleta/col-1/explicacoes.
- CO-022 (baixa) Seção 3 documentação — 38 edições com tabela divergente: achados de jogos e placares acima | SUGESTÃO: cada divergência com explicação ou correção em explicacoes.py; esperados() só com tabelas da mesma fase; mexer em: coleta/col-1/importar.py esperados() e diagnostico(), colet

## 10. Arquivos e comandos

Código em `coleta/col-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga col.1) de 2001 a 2025 para data/coleta/col-1/espn/col1_<ano>.json. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão colombiana no ogol para data/coleta/col-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão colombiana para data/coleta/col-1/rsssf/. |
| `baixar_wikipedia.py` | Baixa da Wikipédia em espanhol o texto-fonte das páginas das temporadas colombianas de 1948 a 1995 |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "Categoría Primera A", seção "Champions by seasons"), segunda fonte |
| `clubes_col.py` | Identidade dos clubes colombianos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão colombiana (col-1): uma por torneio que deu título de campeão colombiano. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão colombiana, edição a edição (entram no relatório). |
| `goleadores_es.py` | Artilheiros pela tabela "Títulos por temporada" da Wikipédia em espanhol (página "Categoría Primera A", guardada em |
| `importar.py` | Junta as fontes da 1ª divisão colombiana e grava o pacote em data/coleta/col-1/pacote/ e o relatório em docs/coleta/col-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/col-1/rsssf/) com o leitor comum (rsssf_sul) e, |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `rebaixados_es.py` | Rebaixados por ano pela Wikipédia em espanhol ("Anexo:Ascensos y descensos de la Categoría Primera A", guardado em |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wikipedia_jogos.py` | Jogos da Wikipédia em espanhol (data/coleta/col-1/wikipedia/es_<chave>.txt), para os anos que a RSSSF não tem. |

- Fontes baixadas: `data/coleta/col-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`, do ogol em `data/cache/ogol-col-1/`.
- Pacote: `data/coleta/col-1/pacote/`; relatório: `docs/coleta/col-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/col-1/baixar_espn.py
python coleta/col-1/baixar_ogol.py
python coleta/col-1/baixar_rsssf.py
python coleta/col-1/baixar_wikipedia.py
python coleta/col-1/importar.py
python coleta/col-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py col-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

