# Campeonato Chileno (`chi-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/chi-1/pacote/`, do código `coleta/chi-1/` e do relatório `docs/coleta/chi-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 109, de 1933 a 2025; 0 sem jogos.
- **Jogos:** 22586 (22565 com placar); **gols:** 69170; **gols com autor:** 19542 (28%); **cartões:** 26607.
- **Clubes:** 53; **artilheiros:** 105 edições com artilheiro (128 linhas, com empates).
- **Classificação final:** 109 edições; **tabelas publicadas guardadas para conferência:** 2038 linhas.
- **No banco:** sim; **último commit do pacote:** b8b5a576.
- **Observação da competição:** 1ª divisão chilena de 1933 a 2025: uma edição por torneio que deu título de campeão (Apertura e Clausura em 1997, 2002-2009, 2011, 2012 e 2013/14-2016/17; Transición em 2013 e 2017; "2020" é a temporada 2020/21). Sem a Copa Chile, as liguillas e os jogos de promoção.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão chilena (chi-1): uma por torneio que deu título de campeão chileno.

Lista de títulos: RSSSF (chilechamp.html), conferida com a Wikipédia. De 1933 a 1996 um campeão por ano; Apertura e
Clausura deram título cada um em 1997, de 2002 a 2009, 2011, 2012 e de 2013/14 a 2016/17 (uma edição por torneio, como no
arg-1); os torneios de Transición de 2013 e 2017 também. 2010 e de 2018 em diante, um campeão por ano ("2020" é a temporada
2020/21). Ficam de fora a Copa Chile, as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes da
2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final None: até
  o primeiro título de outra competição (FIM_PADRAO).
- ogol: os anos em que a RSSSF só tem a tabela final (1984 a 1995 e 2025): o calendário do ogol é a base (ogol_jogos).
- espn: (início, fim) das datas da fase de pontos corridos do Clausura 2011 e de 2012, que a página da RSSSF não traz
  (só os mata-matas).
```

**Edições:** 109, uma por torneio que deu título de campeão chileno da 1ª divisão, de 1933 a 2025, como na lista de campeões da RSSSF (`chilechamp.html`) e na Wikipédia em inglês (as duas trazem os mesmos campeões). Apertura e Clausura deram título cada um em 1997, de 2002 a 2009, em 2011, 2012 e de 2013/14 a 2016/17: uma edição por torneio, como no arg-1; os torneios de Transición de 2013 e 2017 também. "2020" é a temporada 2020/21 (pandemia); 2019 foi encerrado na 24ª rodada pelos protestos de outubro.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/chi-1/rsssf/`: base de jogos de 1933 a 1983 e de 1996 a 2024, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas finais `chilehist.html`, de 1933 a 1996, são a conferência); ogol (base dos jogos de 1984 a 1995 e de 2025, anos em que a RSSSF só traz a tabela final; nos outros anos, rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `chi.1`, 2001 em diante: base da fase de pontos corridos do Clausura 2011 e de 2012, que a RSSSF não traz; hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão).

**Clubes:** Green Cross (Santiago, campeão em 1945), Green Cross-Temuco (1965) e Deportes Temuco (1985) são um clube só, como a RSSSF conta; Ferroviarios e Badminton (até 1949) e Ferrobádminton (fusão de 1950) ficam separados. Homônimos de clubes do banco levam a cidade: Everton de Viña del Mar, Rangers de Talca, Naval de Talcahuano, Metropolitano de Santiago.

**Regras:** o placar é o da RSSSF (ou do ogol e da ESPN, nos anos em que são a base); o ogol entra como conferência nos outros anos. Jogo decidido no tribunal leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, com o placar de campo na observação). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (várias temporadas tiveram pontos de bônus, que a tabela publicada mostra; a diferença vai em `ajuste_pontos`).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 76.
- **Edições com alguma tabela divergente** (32; motivo no relatório, na edição): 1937, 1941, 1946, 1947, 1948, 1951, 1953, 1961, 1962, 1963, 1964, 1965, 1968, 1969, 1970, 1973, 1976, 1977, 1979, 1982, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1993, 1999, 2001, 2004 Clausura, 2012 Clausura.
- **Edições sem tabela para conferir** (1): 1984.
- **Edições com menos jogos que o esperado:** 1939 (109 de 173).
- **Edições com mais jogos que o esperado** (desempates e jogos fora da tabela publicada): 1941 (90 de 88), 2009 Clausura (168 de 167), 2010 (307 de 306), 2019 (195 de 194), 2020 (308 de 307), 2023 (241 de 240), 2024 (240 de 239).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1930s | 7 | 348 | 56% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 10 | 1260 | 91% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 1858 | 16% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 2851 | 77% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 3098 | 88% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 2974 | 100% | 0% | 89% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 11 | 2514 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 18 | 3366 | 100% | 48% | 100% | 51% | 49% | 0% | 81% | 1.2 |
| 2010s | 17 | 2776 | 100% | 97% | 82% | 99% | 95% | 42% | 94% | 5.2 |
| 2020s | 6 | 1541 | 100% | 96% | 100% | 98% | 98% | 71% | 97% | 5.2 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1933: 8 clubes
- 1934: 12 clubes
- 1935 a 1936: 6 clubes
- 1937 a 1938: 7 clubes
- 1939 a 1943: 10 clubes
- 1944 a 1945: 12 clubes
- 1946 a 1948: 13 clubes
- 1949 a 1952: 12 clubes
- 1953 a 1961: 14 clubes
- 1962 a 1980: 18 clubes
- 1981 a 1982: 16 clubes
- 1983: 22 clubes
- 1984: 26 clubes
- 1985: 20 clubes
- 1986: 18 clubes
- 1987 a 2003 Clausura: 16 clubes
- 2004 Apertura a 2004 Clausura: 18 clubes
- 2005 Apertura a 2005 Clausura: 20 clubes
- 2006 Apertura a 2006 Clausura: 19 clubes
- 2007 Apertura a 2007 Clausura: 21 clubes
- 2008 Apertura a 2008 Clausura: 20 clubes
- 2009 Apertura a 2014/15 Clausura: 18 clubes
- 2015/16 Apertura a 2019: 16 clubes
- 2020: 18 clubes
- 2021: 17 clubes
- 2022 a 2025: 16 clubes

**Pontos por vitória:**

- 1933 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1933 a 1996: Campeonato Nacional de Primera División <ano>
- 1997 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 1997 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 1998 a 2001: Campeonato Nacional de Primera División <ano>
- 2002 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2002 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2003 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2003 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2004 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2004 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2005 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2005 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2006 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2006 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2007 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2007 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2008 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2008 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2009 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2009 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2010: Campeonato Nacional de Primera División <ano>
- 2011 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2011 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2012 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2012 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2013 Transición: Campeonato Nacional de Primera División <ano> – Torneo de Transición
- 2013/14 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2013/14 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2014/15 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2014/15 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2015/16 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2015/16 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2016/17 Apertura: Campeonato Nacional de Primera División <ano> – Apertura
- 2016/17 Clausura: Campeonato Nacional de Primera División <ano> – Clausura
- 2017 Transición: Campeonato Nacional de Primera División <ano> – Torneo de Transición
- 2018 a 2025: Campeonato Nacional de Primera División <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1933: pontos corridos + mata-mata
- 1934 a 1949: pontos corridos
- 1950 a 1951: pontos corridos + mata-mata
- 1952 a 1958: pontos corridos
- 1959: pontos corridos + desempate
- 1960: pontos corridos
- 1961: pontos corridos + desempate
- 1962 a 1967: pontos corridos
- 1968: pontos corridos + desempate + pontos corridos + desempate + pontos corridos
- 1969 a 1970: pontos corridos + desempate + 2 grupos + pontos corridos
- 1971: pontos corridos + desempate
- 1972 a 1974: pontos corridos
- 1975 a 1977: pontos corridos + desempate
- 1978 a 1983: pontos corridos
- 1984: 2 grupos + desempate + pontos corridos
- 1985: pontos corridos
- 1986: pontos corridos + mata-mata
- 1987 a 1996: pontos corridos
- 1997 Apertura: pontos corridos + desempate
- 1997 Clausura a 2001: pontos corridos
- 2002 Apertura a 2006 Clausura: pontos corridos + mata-mata
- 2007 Apertura: pontos corridos
- 2007 Clausura a 2009 Clausura: pontos corridos + mata-mata
- 2010: pontos corridos
- 2011 Apertura a 2012 Clausura: pontos corridos + mata-mata
- 2013 Transición: pontos corridos
- 2013/14 Apertura: pontos corridos + desempate
- 2013/14 Clausura a 2019: pontos corridos
- 2020: pontos corridos + desempate
- 2021 a 2025: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1933: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1939: Primeira fase (liga); Segunda fase (liga); Terceira fase (liga)
- 1946: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1950: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1951: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga); Final (mata_mata, jogo_unico)
- 1954: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1955: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1957: Primeira fase (liga); Grupo do rebaixamento (liga)
- 1959: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1961: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1968: Metropolitano (liga); Desempate do 5º lugar (mata_mata, jogo_unico); Provincial (liga); Desempate do 5º lugar do Provincial (mata_mata, jogo_unico); Promocional (liga); Promocional – Série A (liga); Promocional – Série B (liga); Nacional (liga)
- 1969: Metropolitano (liga); Provincial (liga); Desempate do rebaixamento (mata_mata, ida_volta); Nacional (grupos, 2 grupos); Fase final (liga)
- 1970: Metropolitano (liga); Provincial (liga); Desempate do rebaixamento (mata_mata, ida_volta); Nacional (grupos, 2 grupos); Fase final (liga)
- 1971: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1975: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1976: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1977: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1984: Primeira fase (grupos, 2 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Fase final (liga)
- 1986: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1997 Apertura: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1999: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 2002 Apertura: Primeira fase (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Clausura: Primeira fase (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Repechaje (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (liga); Repechaje (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Apertura: Primeira fase (liga); Repechaje (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Clausura: Primeira fase (liga); Repechaje (liga); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Clausura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Apertura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Clausura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Clausura: Primeira fase (liga); Repechaje (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Repechaje (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Final (mata_mata, ida_volta)
- 2009 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2013/14 Apertura: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 2020: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 74 edições
- calculada: 35 edições

**Observações das edições:**

- 1984: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1985: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1986: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1987: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1988: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1989: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1990: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1991: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1992: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1993: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1994: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1995: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 2011 Clausura: a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- 2012 Apertura: a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- 2012 Clausura: a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- 2013 Transición: torneio de transição para o calendário europeu
- 2017 Transición: torneio de transição de volta ao calendário anual
- 2019: campeonato encerrado na 24ª rodada pelos protestos de outubro de 2019; a ANFP declarou campeão o líder
- 2020: temporada esticada até fevereiro de 2021 pela pandemia (a RSSSF chama de 2020/21)
- 2025: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Colo Colo: 34
- Universidad de Chile: 18
- Universidad Católica: 16
- Cobreloa: 8
- Unión Española: 7
- Magallanes: 4
- Audax Italiano: 4
- Everton de Viña del Mar: 4
- Santiago Wanderers: 3
- Huachipato: 3
- Palestino: 2
- Santiago Morning: 1
- Green Cross de Santiago: 1
- Unión San Felipe: 1
- O'Higgins: 1
- Cobresal: 1
- Coquimbo Unido: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1933 | Magallanes | Colo Colo |
| 1934 | Magallanes | Audax Italiano |
| 1935 | Magallanes | Audax Italiano |
| 1936 | Audax Italiano | Magallanes |
| 1937 | Colo Colo | Magallanes |
| 1938 | Magallanes | Audax Italiano |
| 1939 | Colo Colo | Santiago Morning |
| 1940 | Universidad de Chile | Audax Italiano |
| 1941 | Colo Colo | Santiago Morning |
| 1942 | Santiago Morning | Magallanes |
| 1943 | Unión Española | Colo Colo |
| 1944 | Colo Colo | Audax Italiano |
| 1945 | Green Cross de Santiago | Unión Española |
| 1946 | Audax Italiano | Magallanes |
| 1947 | Colo Colo | Audax Italiano |
| 1948 | Audax Italiano | Unión Española |
| 1949 | Universidad Católica | Santiago Wanderers |
| 1950 | Everton de Viña del Mar | Unión Española |
| 1951 | Unión Española | Audax Italiano |
| 1952 | Everton de Viña del Mar | Colo Colo |
| 1953 | Colo Colo | Palestino |
| 1954 | Universidad Católica | Colo Colo |
| 1955 | Palestino | Colo Colo |
| 1956 | Colo Colo | Santiago Wanderers |
| 1957 | Audax Italiano | Universidad de Chile |
| 1958 | Santiago Wanderers | Colo Colo |
| 1959 | Universidad de Chile | Colo Colo |
| 1960 | Colo Colo | Santiago Wanderers |
| 1961 | Universidad Católica | Universidad de Chile |
| 1962 | Universidad de Chile | Universidad Católica |
| 1963 | Colo Colo | Universidad de Chile |
| 1964 | Universidad de Chile | Universidad Católica |
| 1965 | Universidad de Chile | Universidad Católica |
| 1966 | Universidad Católica | Colo Colo |
| 1967 | Universidad de Chile | Universidad Católica |
| 1968 | Santiago Wanderers | Universidad Católica |
| 1969 | Universidad de Chile | Rangers de Talca |
| 1970 | Colo Colo | Unión Española |
| 1971 | Unión San Felipe | Universidad de Chile |
| 1972 | Colo Colo | Unión Española |
| 1973 | Unión Española | Colo Colo |
| 1974 | Huachipato | Palestino |
| 1975 | Unión Española | Deportes Concepción |
| 1976 | Everton de Viña del Mar | Unión Española |
| 1977 | Unión Española | Everton de Viña del Mar |
| 1978 | Palestino | Cobreloa |
| 1979 | Colo Colo | Cobreloa |
| 1980 | Cobreloa | Universidad de Chile |
| 1981 | Colo Colo | Cobreloa |
| 1982 | Cobreloa | Colo Colo |
| 1983 | Colo Colo | Cobreloa |
| 1984 | Universidad Católica | Cobresal |
| 1985 | Cobreloa | Everton de Viña del Mar |
| 1986 | Colo Colo | Palestino |
| 1987 | Universidad Católica | Colo Colo |
| 1988 | Cobreloa | Cobresal |
| 1989 | Colo Colo | Universidad Católica |
| 1990 | Colo Colo | Universidad Católica |
| 1991 | Colo Colo | Coquimbo Unido |
| 1992 | Cobreloa | Colo Colo |
| 1993 | Colo Colo | Cobreloa |
| 1994 | Universidad de Chile | Universidad Católica |
| 1995 | Universidad de Chile | Universidad Católica |
| 1996 | Colo Colo | Universidad Católica |
| 1997 Apertura | Universidad Católica | Colo Colo |
| 1997 Clausura | Colo Colo | Universidad Católica |
| 1998 | Colo Colo | Universidad de Chile |
| 1999 | Universidad de Chile | Universidad Católica |
| 2000 | Universidad de Chile | Cobreloa |
| 2001 | Santiago Wanderers | Universidad Católica |
| 2002 Apertura | Universidad Católica | Rangers de Talca |
| 2002 Clausura | Colo Colo | Universidad Católica |
| 2003 Apertura | Cobreloa | Colo Colo |
| 2003 Clausura | Cobreloa | Colo Colo |
| 2004 Apertura | Universidad de Chile | Cobreloa |
| 2004 Clausura | Cobreloa | Unión Española |
| 2005 Apertura | Unión Española | Coquimbo Unido |
| 2005 Clausura | Universidad Católica | Universidad de Chile |
| 2006 Apertura | Colo Colo | Universidad de Chile |
| 2006 Clausura | Colo Colo | Audax Italiano |
| 2007 Apertura | Colo Colo | Universidad Católica |
| 2007 Clausura | Colo Colo | Universidad de Concepción |
| 2008 Apertura | Everton de Viña del Mar | Colo Colo |
| 2008 Clausura | Colo Colo | Palestino |
| 2009 Apertura | Universidad de Chile | Unión Española |
| 2009 Clausura | Colo Colo | Universidad Católica |
| 2010 | Universidad Católica | Colo Colo |
| 2011 Apertura | Universidad de Chile | Universidad Católica |
| 2011 Clausura | Universidad de Chile | Cobreloa |
| 2012 Apertura | Universidad de Chile | O'Higgins |
| 2012 Clausura | Huachipato | Unión Española |
| 2013 Transición | Unión Española | Universidad Católica |
| 2013/14 Apertura | O'Higgins | Universidad Católica |
| 2013/14 Clausura | Colo Colo | Universidad Católica |
| 2014/15 Apertura | Universidad de Chile | Santiago Wanderers |
| 2014/15 Clausura | Cobresal | Colo Colo |
| 2015/16 Apertura | Colo Colo | Universidad Católica |
| 2015/16 Clausura | Universidad Católica | Colo Colo |
| 2016/17 Apertura | Universidad Católica | Deportes Iquique |
| 2016/17 Clausura | Universidad de Chile | Colo Colo |
| 2017 Transición | Colo Colo | Unión Española |
| 2018 | Universidad Católica | Universidad de Concepción |
| 2019 | Universidad Católica | Colo Colo |
| 2020 | Universidad Católica | Unión La Calera |
| 2021 | Universidad Católica | Colo Colo |
| 2022 | Colo Colo | Ñublense |
| 2023 | Huachipato | Cobresal |
| 2024 | Colo Colo | Universidad de Chile |
| 2025 | Coquimbo Unido | Universidad Católica |

**Rebaixados marcados na classificação:** 48 em 27 edições (só onde a tabela publicada marca a queda); quem mais caiu: San Luis de Quillota (5), Everton de Viña del Mar (4), Santiago Morning (3), Deportes La Serena (3), Deportes Antofagasta (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1934: Audax Italiano -1
- 1934: Colo Colo +1
- 1934: Unión Española +2
- 1934: Badminton -2
- 1934: Morning Star +1
- 1935: Audax Italiano -1
- 1935: Badminton +1
- 1935: Colo Colo -1
- 1935: Unión Española +1
- 1957: San Luis de Quillota -13
- 1979: Colo Colo +1
- 1979: Cobreloa +1
- 1979: Unión Española +1
- 1979: Universidad de Chile +2
- 1980: Cobreloa +1
- 1980: Universidad de Chile +1
- 1980: Colo Colo +1
- 1980: Deportes Iquique +2
- 1981: Colo Colo +2
- 1981: Unión Española +1
- 1981: Audax Italiano +1
- 1981: Everton de Viña del Mar +1
- 1982: Cobreloa +1
- 1982: Colo Colo +2
- 1982: Universidad de Chile +1
- 1982: Universidad Católica +1
- 1983: Universidad Católica +2
- 1983: Naval de Talcahuano +1
- 1983: Deportes Iquique +1
- 1983: Santiago Wanderers +1
- 1990: Colo Colo +2
- 1990: Universidad Católica +1
- 1990: Unión Española +1
- 1990: O'Higgins +1
- 1998: Deportes Temuco -15
- 2007 Apertura: Santiago Wanderers -3
- 2009 Clausura: Rangers de Talca -3
- 2009 Clausura: Curicó Unido -3
- 2011 Apertura: Colo Colo -1
- 2014/15 Clausura: Cobreloa -3
- 2021: Deportes Melipilla -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/chi-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 6)

- **chile44 · 167:** «Everton                 0-2 Santiago Morning» → «Everton                 0-2 Universidad Católica»: clube trocado na rodada (um clube aparece duas vezes, o outro nenhuma); com a troca a tabela publicada fecha (CH-002)
- **chile43 · 186:** «Audax Italiano          3-4 Santiago Morning» → «Audax Italiano          3-4 Badminton»: clube trocado na rodada (um clube aparece duas vezes, o outro nenhuma); com a troca a tabela publicada fecha (CH-002)
- **chile53 · 198:** «Magallanes              1-1 Rangers» → «Unión Española          1-1 Rangers»: clube trocado na rodada (um clube aparece duas vezes, o outro nenhuma); com a troca a tabela publicada fecha (CH-002)
- **chile72 · 214:** «Universidad Católica    2-0 Unión San Felipe» → «Unión Española          2-0 Unión San Felipe»: clube trocado na rodada (um clube aparece duas vezes, o outro nenhuma); com a troca a tabela publicada fecha (CH-002)
- **chiletops · 16:** «Costa Rica Audax» → «Costa Rica  Audax»: um espaço só entre o país e o clube: a linha não era lida (CH-018)
- **chiletops · 17:** «Costa Rica Audax» → «Costa Rica  Audax»: um espaço só entre o país e o clube (CH-018)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 17)

- **1986 · ogol:5324357:** [m = Cobreloa, v = San Luis de Quillota] Cobreloa 1-1 San Luis: adversários trocados no ogol na última rodada de 1986 (25/01/1987); com os jogos dos rounds 5/22 e 7/24, os que faltam são o returno do round 17 (Cobreloa x San Luis e Rangers x Cobresal), e a tabela da chilehist decide o placar (Cobreloa 53-28 e Cobresal 53-35 só fecham assim) (CH-014)
- **1986 · ogol:5324358:** [v = Cobresal] Rangers 0-0 Cobresal: adversários trocados no ogol na última rodada de 1986 (25/01/1987); com os jogos dos rounds 5/22 e 7/24, os que faltam são o returno do round 17 (Cobreloa x San Luis e Rangers x Cobresal), e a tabela da chilehist decide o placar (Cobreloa 53-28 e Cobresal 53-35 só fecham assim) (CH-014)
- **1968 · chile68:294:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1968 · chile68:295:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1968 · chile68:298:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1968 · chile68:299:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1968 · chile68:302:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1968 · chile68:303:** [fase = Desempate do 5º lugar do Provincial, grupo = ] quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- **1990 · ogol:5257815:** [gm = 2, gv = 1] Universidad Católica 2-1 Everton: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1990 · ogol:5257902:** [gm = 1, gv = 1] Unión Española 1-1 La Serena: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1990 · ogol:5257949:** [gm = 0, gv = 0] Huachipato 0-0 Palestino: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1991 · ogol:5249721:** [gm = 4, gv = 2] O'Higgins 4-2 Deportes Concepción: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1993 · ogol:5247516:** [gm = 2, gv = 1] Everton 2-1 Unión Española: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1994 · ogol:5241920:** [gm = 1, gv = 0] Universidad Católica 1-0 Universidad de Chile: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1995 · ogol:5237549:** [gm = 2, gv = 0] Palestino 2-0 La Serena: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- **1988 · ogol:5293713:** [m = Naval de Talcahuano, v = O'Higgins, gm = 1, gv = 1] o ogol repete O'Higgins 0-2 Naval; o jogo que falta é Naval 1-1 O'Higgins (CH-014)
- **2011 Apertura · chile2011:67:** [vale o placar de campo, gm = 2, gv = 0] Ñublense 2-0 Wanderers: a decisão do tribunal foi revogada ("award revoked") (CH-015)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 3)

- **1986:** Everton e Rangers: a tabela da chilehist dá ao Everton 2 gols a mais contra o Rangers (33-38 e 33-42); só cabe no Everton 1-0 Rangers de 09/11/1986 (3-0 não muda vitórias, empates e derrotas), mas sem 3ª fonte fica o placar do ogol
- **1984:** duas zonas (Norte e Sul) de 13 clubes e um quadrangular final. As tabelas das zonas (chilehist.html) dão 26 jogos por clube: os 24 da zona e 2 interzonais. O calendário do ogol, a base deste ano, não tem os 26 jogos interzonais; nenhuma outra fonte que baixamos os traz. A classificação é calculada com os jogos que há
- **1999:** o octogonal final ("Championship Playoff") somou aos clubes um quarto dos pontos e todos os gols da 1ª fase: a tabela publicada mostra esses gols acumulados. Vitórias, empates e derrotas fecham com os jogos

### Identidade dos clubes

Regras em `coleta/chi-1/clubes_chi.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes chilenos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Colo Colo", "Universidad de Chile", "Universidad Católica", "Cobreloa");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Everton de Viña del Mar" (o Everton inglês está no eng-1),
  "Rangers de Talca", "Naval de Talcahuano";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte: Green Cross-Temuco
  (1965) -> Deportes Temuco (1985); o Green Cross de Santiago (1933-1964, campeão de 1945; o nome leva a cidade por causa do Green Cross
  de Manta, do Equador) fica à parte (D-25 a, decisão do
  Guilherme de 22/11/2026: a lista oficial dá o título ao Green Cross); Deportes Arica = San Marcos de Arica (D-25 b); Unión Calera -> Unión La
  Calera; Municipal Iquique -> Deportes Iquique; Provincial Curicó Unido -> Curicó Unido;
- fusões que criaram clube novo ficam separadas: Ferroviarios e Badminton (até 1949) e Ferrobádminton (1950).

A lista de tabelas finais (chilehist.html) põe os pontos de bônus entre parênteses no nome ("Colo Colo (2)"): saem antes da
regra. REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a Copa Chile (e as copas de começo e de fim de ano dos anos 1930-1980, "Campeonato de Apertura" e "Campeonato de Clausura"), as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes da 2ª divisão.
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): coluna de bônus das tabelas de 1979-1983, 1988 e 1989, vice pela lista oficial, tabela publicada como classificação em 14 edições, desempates, liguillas pré-Libertadores fora, 2020 no ano certo, placares de 1990-1995, clubes (D-25 a e b) e artilheiros.
- Abertos fechados em 24/11: CH-006 (1984, 1969 e 1970: a ordem da fase final de pontos vem antes da soma do ano, D-02 A; 1946 e 1951 ficam com a tabela acumulada, como a chilehist), CH-014 (1986: adversários da última rodada), CH-017 (gol da ESPN sem lado; 'Gabriel 2Vargas'), CH-022 (grupos herdados; 5º lugar do Provincial de 1968), CH-023 (1969: datas do ogol da fase final fora dos outros jogos; par repetido sem data só casa com placar igual) e CH-028 (calendário do ogol de 1964, 1971, 1977 e 1982 completo: 918 jogos ganharam data).
- Sem fonte: o ogol não tem jogos de 1952 a 1957 (calendários vazios na origem); 1986, Everton x Rangers com 2 gols a menos que a tabela da chilehist (explicado no relatório).

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/chi-1.md`):

- CH-001 (alta) B classificação (pontos) — 1981; 1983: A tabela da RSSSF tem a coluna de bônus da Copa Polla Gol ANTES dos pontos ('COLO COLO 30 19 8 3 63-22  2  48'); o leitor pegou o bônus como pontos | SUGESTÃO: 1981 pontos = Colo Colo 48 (bônus +2), Cobreloa 46, U. de Ch
- CH-002 (alta) A vice / C clube trocado no jogo — 1944 (vice); 1943; 1953; 1972: Erros da própria página da RSSSF (um clube aparece duas vezes na rodada, outro nenhuma), confirmados pela soma das tabelas da RSSSF e da es.wiki; 1944 vice é Audax Italiano (es.wiki e RSSSF) | SUGESTÃO: CONSERTA_TEXTO ('
- CH-003 (alta) A vice / B classificação — 1954; 1955: RSSSF e es.wiki: 1955 tem tabela agregada final (Palestino 46, Colo Colo 37, U. de Chile 37, Everton 37...) e vice Colo-Colo; o importar escolhe a primeira tabela com todos os clubes (a da 1ª fase) | SUGESTÃO: 1955 vice 
- CH-004 (alta) A vice — 1968: RSSSF: o Torneo Nacional (que dá o título) termina Wanderers 25, U. Católica 24, U. de Chile 24, e 'Second Place Playoff: Universidad Católica bt Universidad de Chile'; es.wiki: vice U. Católica | SUGESTÃO: vice Universi
- CH-005 (alta) A vice / B pontos de bônus — 1982 (vice); 1979; 1990; 1969; 1970: RSSSF chilehist: 1982 Cobreloa 45, Colo Colo 41 (2 de bônus), U. de Chile 40...; 1979 Colo Colo 55 (+1); 1990 Colo Colo 46 (+2); es.wiki 1982 vice Colo-Colo | SUGESTÃO: aplicar os bônus como ajuste_pontos nas classificaç
- CH-006 (alta) A vice / B classificação — 1984: RSSSF chilehist 1984 'Final Playoff': 1. U. Católica 5, 2. Cobresal 3, 3. Unión Española 3, 4. Cobreloa 1; es.wiki vice Cobresal | SUGESTÃO: ordem 1-4 pelo quadrangular final (U. Católica, Cobresal, Unión Española, Cobre
- CH-007 (alta) A vice / C placar do ogol — 1985: RSSSF chilehist e es.wiki: Everton 19-12-7, 50 pts, vice; San Luis 8-12-18, Arica 7-13-18, O'Higgins 5-11-22 (o relatório da coleta diz 'o ogol traz os mesmos placares: o erro é da tabela', mas o ogol é a própria base de
- CH-008 (alta) A vice / C liguilla dentro da edição — 2016/17 Apertura (vice); 2017 Transición; 2015/16 Apertura; 2015/16 Clausura: RSSSF: 'Pre-Libertadores/Sudamericana 2017' (chile2017:261), 'Pre-Libertadores/Sudamericana 2018' (chile2017a:256) e 'Pre-Sudamericana 2016' (chile2016:272 e :542) ficam dentro dos trechos explícitos de edicoes.py; Apert
- CH-009 (alta) B classificação / C desempate de título na fase de liga — 1997 Apertura; 2013/14 Apertura: RSSSF: 'Playoff for Apertura Championship' (chile97:229) e 'Apertura Championship Playoff' (chile2014:307); tabela final de 15/17 jogos | SUGESTÃO: fase 'Desempate do título' (mata_mata) para esses jogos; classificação =
- CH-010 (alta) B rebaixados (situacao) — 1954; 1955; 1975; 1978; 1996; 1998; 2010; 2020; 2021; e 45+ temporadas sem marca: importar.situacao() marca 'rebaixado' qualquer nota com 'relegat' (Relegation Group/Playoff); os rebaixados oficiais estão nas linhas 'RELEGATED:' da chilehist (1933-1996) e 'Relegated:' das páginas por ano; 2020: Colo C
- CH-011 (media) C datas — 2020: transfermarkt e RSSSF: 1ª rodada 24-28/01/2020, fim em fev/2021; rsssf_sul.fixa_data põe o ano final (2021) na 1ª data quando ano_fim > ano_inicio e o mês é <= 6 | SUGESTÃO: datas 2020-01-24 ... 2021-02 (como na página);
- CH-012 (media) C datas dos mata-matas — 2002 Apertura a 2015/16 Clausura (22 edições): ESPN e es.wiki concordam entre si (ex.: 2005 Clausura semis 08/12 e 14/12, final 18/12); a RSSSF escreve 'First Leg [Dec 8]', que o leitor não lê como data (armadilha já listada no COMECE-AQUI) | SUGESTÃO: datas da ESPN 
- CH-013 (media) C placares do ogol (1984-1995) — 1990; 1991; 1993; 1994; 1995 (e 1985-1995 em geral): Três fontes concordam contra o ogol (base desses anos): tabela da RSSSF chilehist, transfermarkt e, em 1993/1995, es.wiki | SUGESTÃO: 1990 UC 2-1 Everton (22/07), UE 1-1 La Serena (29/09), Huachipato 0-0 Palestino (01/11
- CH-014 (media) C jogo duplicado / adversário trocado (ogol) — 1988; 1986: Tabela RSSSF/es.wiki 1988: Naval 9-9-12 39-45 e O'Higgins 10-6-14 36-43 fecham se o 2º jogo for Naval 1-1 O'Higgins | SUGESTÃO: 1988 trocar ogol:5293713 por Naval 1-1 O'Higgins (conferir a data); 1986 trocar os adversári
- CH-015 (media) B punições perdidas na classificação calculada — 2003 Clausura; 2004 Clausura; 2008 Apertura; 2011 Apertura: Tabelas da RSSSF (chile03 linha 668, chile04 781/787, chile08 42, chile2011 34) | SUGESTÃO: levar a diferença da tabela publicada para ajuste_pontos também quando a classificação é calculada; 2011 Ap Ñublense 2-0 Santiag
- CH-016 (media) C desempate de rebaixamento na fase de liga — 1971; 1977: RSSSF: 'Playoff against relegation' (chile71:431) e 'Playoff against direct relegation' (chile77:430) | SUGESTÃO: fase 'Desempate do rebaixamento'; classificação de 34 jogos (tabela RSSSF); fonte: https://www.rsssf.org/t
- CH-017 (media) D gols com autor maiores que o placar — 2007 Apertura; 2007 Clausura; 2008 Apertura; 2011 Apertura: A ESPN repete o mesmo lance (gol contra) para os dois lados | SUGESTÃO: descartar o lance repetido (mesmo jogador e minuto) e só gravar os gols quando a soma por lado bate com o placar; fonte: data/coleta/chi-1/espn/chi1
- CH-018 (media) D artilheiros — 1936; 1937; 1947; 1968; 1998; 2013/14 Clausura; 2014/15 Apertura; 2014/15 Clausura; 2015/16 Apertura; 2020: RSSSF chiletops: 1936 Hernán Bolaños 14 e 1937 Bolaños 16 (Audax), 1947 Apolonides Vera 17 (S. National) — o leitor exige dois espaços entre país e clube ('Costa Rica Audax Italiano'); es.wiki 1968: Eladio Zárate 32 (U. 
- CH-019 (media) B desempate calculado (pódio) — 1947 (e demais edições com classificação calculada): RSSSF e es.wiki: 3º U. de Chile, 4º U. Española (mesmos pontos; a ordem oficial da época não é o saldo) | SUGESTÃO: quando a tabela publicada existe e só não fecha por 1-2 gols, usar a ORDEM dela; 1947: 3º U. de Chile; f
- CH-020 (media) E clube (identidade) — 1933-1964 (e o título de 1945): es.wiki: 'Green Cross' campeão de 1945, clube próprio que em 1965 se mudou para Temuco e se fundiu com o Deportes Temuco (Green Cross-Temuco); a regra da casa separa fusões (Ferrobádminton) | SUGESTÃO: decisão do Guilher
- CH-021 (media) E clube (identidade) — 1982-1985; 2013-2015: es.wiki: San Marcos de Arica foi fundado em 1978 como Norte-Arica, depois 'Club de Deportes Arica'; refundado em 2005 como San Marcos de Arica | SUGESTÃO: decisão do Guilherme (ver decisoes_CH.md); fonte: https://es.wiki
- CH-022 (baixa) C fases e grupos — 1968; 1969; 1970; 2002 Apertura a 2008 Clausura: RSSSF chile68 linhas 291-308 ('Fifth Place Playoff'), chile69/chile70 'Interseries'; nos torneios 2002-2008 os grupos são só de classificação (todos jogam contra todos) | SUGESTÃO: 1968 fase 'Desempate do 5º lugar' també
- CH-023 (baixa) C datas — 1969 (7 jogos); 2010 (26 jogos: não é erro): 1969: o ogol casou jogos de outra fase com o mesmo par de clubes; 2010: a es.wiki (Primera_División_de_Chile_2010) confirma as 294 datas da RSSSF que casou: o pacote está certo e a ESPN erra | SUGESTÃO: 1969 tirar essas 
- CH-024 (baixa) C campo cidade — 2005-2025 (67 jogos): A ESPN traz o estádio no campo da cidade | SUGESTÃO: cidade 'La Serena'; mexer em: coleta/chi-1/outras_fontes.py
- CH-025 (baixa) B participante sem jogos — 2008 Clausura: O clube foi desfiliado antes do Clausura 2008 e não jogou (o único jogo dele é 'não jogado') | SUGESTÃO: tirar da classificação do 2008 Clausura (ou marcar 'excluído'); mexer em: coleta/chi-1/importar.py (clubes sem jogo
- CH-028 (baixa) C datas e jogos do ogol incompletos — 1951-1957, 1959, 1964, 1967, 1969-1971, 1977, 1982: data/cache/ogol-chi-1/calendario_1977_37074_p1..p3.html: 50 jogos por página, sem p4 (o baixador para quando o ogol não devolve a página) | SUGESTÃO: baixar de novo as páginas que faltam (devagar) e casar as datas; fonte

## 10. Arquivos e comandos

Código em `coleta/chi-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga chi.1) de 2001 a 2025 para data/coleta/chi-1/espn/chi1_<ano>.json. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão chilena no ogol para data/coleta/chi-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão chilena para data/coleta/chi-1/rsssf/. |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "Chilean Primera División", seção "List of champions"), segunda fonte |
| `clubes_chi.py` | Identidade dos clubes chilenos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão chilena (chi-1): uma por torneio que deu título de campeão chileno. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão chilena, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão chilena e grava o pacote em data/coleta/chi-1/pacote/ e o relatório em docs/coleta/chi-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/chi-1/rsssf/) com o leitor comum (rsssf_sul) e, |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wikipedia_jogos.py` | Jogos da Wikipédia em espanhol (data/coleta/chi-1/wikipedia/es_<ano>.txt), para os anos que a RSSSF não tem. |

- Fontes baixadas: `data/coleta/chi-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`, do ogol em `data/cache/ogol-chi-1/`.
- Pacote: `data/coleta/chi-1/pacote/`; relatório: `docs/coleta/chi-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/chi-1/baixar_espn.py
python coleta/chi-1/baixar_ogol.py
python coleta/chi-1/baixar_rsssf.py
python coleta/chi-1/importar.py
python coleta/chi-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py chi-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

