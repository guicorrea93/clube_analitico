# Campeonato Venezuelano (`ven-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/ven-1/pacote/`, do código `coleta/ven-1/` e do relatório `docs/coleta/ven-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 106, de 1921 a 2025; 25 sem jogos.
- **Jogos:** 13580 (13528 com placar); **gols:** 34189; **gols com autor:** 6398 (19%); **cartões:** 6744.
- **Clubes:** 108; **artilheiros:** 69 edições com artilheiro (74 linhas, com empates).
- **Classificação final:** 106 edições; **tabelas publicadas guardadas para conferência:** 1733 linhas.
- **No banco:** sim; **último commit do pacote:** 35dc0a2.
- **Observação da competição:** 1ª divisão venezuelana de 1921 (temporada 1920/21) a 2025, uma edição por título, como na lista de campeões da RSSSF: era amadora (1921-1956; jogos só em parte), profissional em ano fechado (1957-1986), calendário europeu (1986/87 a 2014/15; Apertura e Clausura são fases), Torneo de Adecuación 2015 e Liga FUTVE (2016 em diante). Jogos completos de 1957 em diante, salvo 1993/94 e 1994/95 (fases só com tabelas); sem jogos em 1922, 1924, 1931, 1938, 1939, 1949 e 1950.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão venezuelana (ven-1): uma por título, como na lista de campeões da RSSSF (venezchamp.html), que conta 106
títulos desde 1920/21.

- 1921-1956: era amadora (a temporada 1920/21 é a edição "1921", como na Wikipédia), um campeão por ano; os anos sem
  página da RSSSF (1922, 1924, 1931, 1938, 1939, 1949, 1950) entram só com campeão e vice.
- 1957-1986: era profissional, um campeão por ano (Apertura, Clausura, liguillas e finais são fases).
- 1986/87 a 2014/15: calendário europeu ("1986/87").
- 2015: Torneo de Adecuación (Zamora). A RSSSF o conta como título; a Wikipédia em inglês não ("não foi uma temporada
  completa"). Entra como edição, como na lista da RSSSF (decisão registrada no relatório).
- 2016-2025: um campeão por ano (Apertura e Clausura com final entre os vencedores).
Ficam de fora a 2ª e a 3ª divisões, a Copa Venezuela (salvo quando era a 1ª fase da temporada: 1993/94 a 1995/96 e
2000/01), as outras copas (Copa Caracas, Liga Mayor, de las Naciones, Cuatricentenario, Valencia, de Campeones,
Bicentenario) e os playoffs da Sudamericana e da Conmebol.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). Página venezYY (ou venezAAAA de 2010 em diante): a do ano; nas temporadas
  europeias, a do ano em que terminam (venez87 = 1986/87). A página venez2016 traz o Adecuación 2015 e a temporada 2016.
- espn: datas dos jogos que vêm da ESPN (2025: a RSSSF só tem as tabelas).
```

**Edições:** 106, uma por título de 1921 (temporada 1920/21) a 2025, como na lista de campeões da RSSSF (`venezchamp.html`, 106 títulos). A Wikipédia em inglês (página "Liga FUTVE") tem os mesmos campeões, menos o Torneo de Adecuación 2015, que ela não conta como temporada; aqui ele entra, como na RSSSF. Era amadora (1921-1956), profissional em ano fechado (1957-1986), calendário europeu de 1986/87 a 2014/15 (Apertura, Clausura, liguillas e finais são fases do ano), Adecuación 2015 e Liga FUTVE (2016 em diante, Apertura e Clausura com final entre os vencedores).

**Fontes:** RSSSF (uma página por temporada, `venezYY.html` / `venezAAAA.html`, em `data/coleta/ven-1/rsssf/`: base de jogos, com fases, grupos, rodadas, datas e autores dos gols; lista de campeões `venezchamp.html`; artilheiros `veneztops.html`, 1957-2007/08); ESPN (liga `ven.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões; jogos do Clausura 2011, de 2011/12 e de 2025, que a RSSSF tem só em parte ou só nas tabelas); Wikipédia em inglês (lista de campeões: segunda fonte do campeão e do vice e fonte dos artilheiros depois de 2007/08).

**Clubes:** nome pelo qual o clube é conhecido (Caracas FC, Deportivo Táchira, Estudiantes de Mérida, Mineros de Guayana). O mesmo clube com outro nome, como na lista de campeões da RSSSF: Unión Atlético Táchira (1985-1999) é o Deportivo Táchira; ItalChacao e Deportivo Petare são o Deportivo Italia; o Atlético Zulia (1996/97 e 1997/98) é a Universidad de Los Andes (ULA); o Internacional de Lara (1998/99) é o Trujillanos; UE Lara e UD Lara são a Unión Deportiva Lara; Internacional de Barinas é o Hermanos Colmenárez. Clubes diferentes com nome parecido ficam separados: Atlético Zamora (até 2005) e Zamora FC; Lara FC (1965-1985), Unión Deportiva Lara (1986-2002) e Deportivo Lara (2009 em diante); Anzoátegui FC (1967), Atlético Anzoátegui (1986-1990), Deportivo Anzoátegui (2007 em diante) e o Anzoátegui FC de 2025; Atlético Monagas (2000) e Monagas SC; Estudiantes de Caracas (era amadora) e Estudiantes de Caracas SC (2015-2019). Homônimos de clubes de outros países levam a cidade ou o país (Deportivo Español de Caracas, Celta de Caracas, Danubio de Caracas, América de Caracas).

**Regras:** o placar é o da fonte de base (RSSSF; ESPN onde a RSSSF não tem). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação; "bt" / "lt" (venceu / perdeu sem placar conhecido) viram W.O. (vitória sem gols, como a tabela conta); "drw" (empate sem placar, 1994/95) fica de fora. Ida e volta numa linha só ("A 1-0 0-4 B") vira dois jogos, com os gols de A primeiro e o mando da volta presumido. Pontos: 2 por vitória até 1994/95 e 3 a partir de 1995/96. Nas edições sem jogos, campeão e vice da lista ficam em 1º e 2º.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 48.
- **Edições com alguma tabela divergente** (23; motivo no relatório, na edição): 1960, 1964, 1973, 1977, 1980, 1982, 1984, 1985, 1986, 1987/88, 1988/89, 1990/91, 1991/92, 1992/93, 1995/96, 1996/97, 1997/98, 1999/00, 2003/04, 2007/08, 2008/09, 2010/11, 2011/12.
- **Edições sem tabela para conferir** (35): 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1993/94, 1994/95.
- **Edições com menos jogos que o esperado:** 1955 (30 de 28), 1961 (40 de 39), 1962 (62 de 55), 1973 (145 de 144), 1975 (124 de 123), 1983 (90 de 89), 1992/93 (241 de 242), 2005/06 (183 de 182), 2008/09 (310 de 308), 2009/10 (309 de 308), 2011/12 (304 de 306).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 9 | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 10 | 3 | 33% | 0% | 33% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 10 | 80 | 34% | 0% | 12% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 155 | 99% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 828 | 99% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 1397 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 11 | 1869 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 2382 | 72% | 0% | 62% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 2220 | 100% | 57% | 100% | 57% | 52% | 0% | 71% | 1.5 |
| 2010s | 10 | 3213 | 100% | 99% | 88% | 99% | 92% | 0% | 30% | 1.0 |
| 2020s | 6 | 1431 | 100% | 99% | 84% | 99% | 99% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1921 a 1925: 0 clubes
- 1926: 2 clubes
- 1927: 0 clubes
- 1928: 2 clubes
- 1929: 0 clubes
- 1930: 2 clubes
- 1931 a 1935: 0 clubes
- 1936 a 1937: 2 clubes
- 1938 a 1939: 0 clubes
- 1940: 6 clubes
- 1941 a 1944: 0 clubes
- 1945: 8 clubes
- 1946: 6 clubes
- 1947: 7 clubes
- 1948 a 1954: 0 clubes
- 1955 a 1956: 5 clubes
- 1957: 6 clubes
- 1958 a 1959: 5 clubes
- 1960: 4 clubes
- 1961: 5 clubes
- 1962 a 1964: 6 clubes
- 1965: 8 clubes
- 1966 a 1967: 9 clubes
- 1968: 10 clubes
- 1969: 9 clubes
- 1970 a 1971: 8 clubes
- 1972 a 1973: 9 clubes
- 1974 a 1976: 8 clubes
- 1977 a 1979: 12 clubes
- 1980: 11 clubes
- 1981 a 1982: 12 clubes
- 1983: 10 clubes
- 1984: 11 clubes
- 1985: 10 clubes
- 1986: 11 clubes
- 1986/87 a 1987/88: 14 clubes
- 1988/89 a 1993/94: 16 clubes
- 1994/95: 23 clubes
- 1995/96: 18 clubes
- 1996/97 a 1997/98: 12 clubes
- 1998/99: 13 clubes
- 1999/00: 12 clubes
- 2000/01: 17 clubes
- 2001/02 a 2006/07: 10 clubes
- 2007/08 a 2014/15: 18 clubes
- 2015 a 2016: 20 clubes
- 2017 a 2018: 18 clubes
- 2019: 20 clubes
- 2020: 19 clubes
- 2021: 21 clubes
- 2022: 16 clubes
- 2023: 15 clubes
- 2024 a 2025: 14 clubes

**Pontos por vitória:**

- 1921 a 1994/95: 2
- 1995/96 a 2025: 3

**Nome oficial:**

- 1921: Campeonato Nacional de Fútbol <ano> (<ano>)
- 1922 a 1956: Campeonato Nacional de Fútbol <ano>
- 1957 a 2014/15: Primera División de Venezuela <ano>
- 2015: Torneo de Adecuación <ano>
- 2016: Primera División de Venezuela <ano>
- 2017 a 2025: Liga FUTVE <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1921: mata-mata
- 1922: sem jogos (só a tabela final)
- 1923: mata-mata
- 1924: sem jogos (só a tabela final)
- 1925: mata-mata
- 1926: pontos corridos
- 1927: mata-mata
- 1928: pontos corridos
- 1929: mata-mata
- 1930: pontos corridos
- 1931: sem jogos (só a tabela final)
- 1932 a 1935: mata-mata
- 1936 a 1937: pontos corridos
- 1938 a 1939: sem jogos (só a tabela final)
- 1940: pontos corridos
- 1941 a 1944: mata-mata
- 1945 a 1947: pontos corridos
- 1948: mata-mata
- 1949 a 1950: sem jogos (só a tabela final)
- 1951 a 1954: mata-mata
- 1955 a 1959: pontos corridos
- 1960: pontos corridos + desempate + mata-mata
- 1961: pontos corridos
- 1962 a 1964: pontos corridos + mata-mata
- 1965 a 1969: pontos corridos
- 1970: pontos corridos + mata-mata
- 1971: pontos corridos
- 1972: pontos corridos + desempate + pontos corridos
- 1973: pontos corridos + desempate
- 1974: pontos corridos + mata-mata
- 1975 a 1976: pontos corridos
- 1977: pontos corridos + mata-mata
- 1978 a 1980: pontos corridos
- 1981: pontos corridos + 2 grupos + pontos corridos
- 1982 a 1988/89: pontos corridos
- 1989/90: pontos corridos + mata-mata
- 1990/91 a 1991/92: pontos corridos
- 1992/93: pontos corridos + mata-mata
- 1993/94: pontos corridos
- 1994/95: pontos corridos + 2 grupos + pontos corridos
- 1995/96: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 1996/97: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1997/98 a 1998/99: pontos corridos + mata-mata
- 1999/00: pontos corridos
- 2000/01: pontos corridos + mata-mata + pontos corridos
- 2001/02 a 2002/03: pontos corridos + mata-mata
- 2003/04 a 2004/05: pontos corridos
- 2005/06 a 2010/11: pontos corridos + mata-mata
- 2011/12: pontos corridos
- 2012/13 a 2019: pontos corridos + mata-mata
- 2020: pontos corridos + 2 grupos + mata-mata
- 2021 a 2023: pontos corridos + mata-mata
- 2024 a 2025: pontos corridos + 2 grupos + pontos corridos + 2 grupos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1960: Primeira fase (liga); Segunda fase (liga); Desempate da segunda fase (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1962: Primeira fase (liga); Final (mata_mata, ida_volta)
- 1963: Primeira fase (liga); Fase final (liga); Final (mata_mata, jogo_unico)
- 1964: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 1968: Primeira fase (liga); Fase final (liga)
- 1970: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 1972: Primeira fase (liga); Segunda fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1973: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 1974: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1975: Primeira fase (liga); Fase final (liga)
- 1976: Primeira fase (liga); Fase final (liga)
- 1977: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1978: Primeira fase (liga); Fase final (liga)
- 1979: Primeira fase (liga); Fase final (liga)
- 1980: Primeira fase (liga); Fase final (liga)
- 1981: Primeira fase (liga); Liguillas (grupos, 2 grupos); Fase final (liga)
- 1982: Primeira fase (liga); Fase final (liga)
- 1984: Primeira fase (liga); Fase final (liga)
- 1985: Primeira fase (liga); Fase final (liga)
- 1986: Primeira fase (liga); Fase final (liga)
- 1986/87: Primeira fase (liga); Fase final (liga)
- 1987/88: Primeira fase (liga); Fase final (liga)
- 1989/90: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1992/93: Primeira fase (liga); Final (mata_mata, ida_volta)
- 1994/95: Apertura (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1995/96: Apertura (liga); Clausura (grupos, 2 grupos); Fase final do Clausura (liga); Final (mata_mata, ida_volta)
- 1996/97: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Final (mata_mata, ida_volta)
- 1997/98: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 1998/99: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 1999/00: Apertura (liga); Clausura (liga); Fase final (liga)
- 2000/01: Apertura (liga); Final do Apertura (mata_mata, ida_volta); Primeira fase (liga)
- 2001/02: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2002/03: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2003/04: Apertura (liga); Clausura (liga)
- 2004/05: Apertura (liga); Clausura (liga)
- 2005/06: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2006/07: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2007/08: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2008/09: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2009/10: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, ida_volta)
- 2010/11: Primeira fase (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2011/12: Apertura (liga); Clausura (liga)
- 2012/13: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2013/14: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2014/15: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2015: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016: Apertura (liga); Clausura (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017: Apertura (liga); Clausura (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2018: Apertura (liga); Clausura (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019: Apertura (liga); Clausura (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020: Apertura (liga); Primeira fase (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 2021: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2022: Primeira fase (liga); Fase final (liga); Final (mata_mata, jogo_unico)
- 2023: Primeira fase (liga); Fase final (liga); Final (mata_mata, jogo_unico)
- 2024: Apertura (liga); Liguillas do Apertura (grupos, 2 grupos); Clausura (liga); Liguillas do Clausura (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 2025: Apertura (liga); Liguillas do Apertura (grupos, 2 grupos); Clausura (liga); Liguillas do Clausura (grupos, 2 grupos); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 55 edições
- lista de campeões da Wikipédia em inglês: 33 edições
- calculada: 18 edições

**Observações das edições:**

- 1922: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1924: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1931: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1938: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1939: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1949: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)
- 1950: sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Caracas FC: 12
- Deportivo Táchira: 11
- Unión SC: 7
- Dos Caminos: 6
- Deportivo Italia: 5
- Portuguesa FC: 5
- Zamora FC: 5
- Centro Atlético: 4
- Loyola: 4
- Deportivo Venezuela: 4
- Universidad Central: 4
- Deportivo Portugués: 4
- Deportivo Galicia: 4
- CS Marítimo: 4
- Universidad de Los Andes: 3
- América de Caracas: 2
- Deportivo Español de Caracas: 2
- La Salle: 2
- Estudiantes de Mérida: 2
- Venzóleo: 1
- Litoral: 1
- Deportivo Vasco: 1
- Banco Obrero: 1
- Lara FC: 1
- Unión Deportiva Canarias: 1
- Valencia FC: 1
- Atlético San Cristóbal: 1
- Mineros de Guayana: 1
- Minervén: 1
- Nacional Táchira: 1
- Unión Atlético Maracaibo: 1
- Deportivo Lara: 1
- Monagas SC: 1
- Deportivo La Guaira: 1
- Metropolitanos: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1921 | América de Caracas | Centro Atlético |
| 1922 | Centro Atlético | América de Caracas |
| 1923 | América de Caracas | Centro Atlético |
| 1924 | Centro Atlético | Vargas |
| 1925 | Loyola | Venzóleo |
| 1926 | Centro Atlético | Venzóleo |
| 1927 | Venzóleo | Centro Atlético |
| 1928 | Deportivo Venezuela | Centro Atlético |
| 1929 | Deportivo Venezuela | Unión SC |
| 1930 | Centro Atlético | Unión SC |
| 1931 | Deportivo Venezuela | Centro Atlético |
| 1932 | Unión SC | Dos Caminos |
| 1933 | Deportivo Venezuela | Dos Caminos |
| 1934 | Unión SC | Dos Caminos |
| 1935 | Unión SC | Dos Caminos |
| 1936 | Dos Caminos | Centro Atlético |
| 1937 | Dos Caminos | Litoral |
| 1938 | Dos Caminos | Litoral |
| 1939 | Unión SC | Litoral |
| 1940 | Unión SC | Dos Caminos |
| 1941 | Litoral | Dos Caminos |
| 1942 | Dos Caminos | Loyola |
| 1943 | Loyola | Litoral |
| 1944 | Loyola | Dos Caminos |
| 1945 | Dos Caminos | Loyola |
| 1946 | Deportivo Español de Caracas | Centro Atlético |
| 1947 | Unión SC | Universidad Central |
| 1948 | Loyola | Unión SC |
| 1949 | Dos Caminos | Universidad Central |
| 1950 | Unión SC | La Salle |
| 1951 | Universidad Central | Loyola |
| 1952 | La Salle | Loyola |
| 1953 | Universidad Central | La Salle |
| 1954 | Deportivo Vasco | Loyola |
| 1955 | La Salle | Deportivo Español de Caracas |
| 1956 | Banco Obrero | La Salle |
| 1957 | Universidad Central | La Salle |
| 1958 | Deportivo Portugués | Deportivo Español de Caracas |
| 1959 | Deportivo Español de Caracas | Deportivo Portugués |
| 1960 | Deportivo Portugués | Deportivo Español de Caracas |
| 1961 | Deportivo Italia | Banco Agrícola y Pecuario |
| 1962 | Deportivo Portugués | Universidad Central |
| 1963 | Deportivo Italia | Deportivo Portugués |
| 1964 | Deportivo Galicia | Tiquire Flores |
| 1965 | Lara FC | Deportivo Italia |
| 1966 | Deportivo Italia | Deportivo Galicia |
| 1967 | Deportivo Portugués | Deportivo Galicia |
| 1968 | Unión Deportiva Canarias | Deportivo Italia |
| 1969 | Deportivo Galicia | Valencia FC |
| 1970 | Deportivo Galicia | Deportivo Italia |
| 1971 | Valencia FC | Deportivo Italia |
| 1972 | Deportivo Italia | Deportivo Galicia |
| 1973 | Portuguesa FC | Valencia FC |
| 1974 | Deportivo Galicia | Portuguesa FC |
| 1975 | Portuguesa FC | Deportivo Galicia |
| 1976 | Portuguesa FC | Estudiantes de Mérida |
| 1977 | Portuguesa FC | Estudiantes de Mérida |
| 1978 | Portuguesa FC | Deportivo Galicia |
| 1979 | Deportivo Táchira | Deportivo Galicia |
| 1980 | Estudiantes de Mérida | Portuguesa FC |
| 1981 | Deportivo Táchira | Estudiantes de Mérida |
| 1982 | Atlético San Cristóbal | Deportivo Táchira |
| 1983 | Universidad de Los Andes | Portuguesa FC |
| 1984 | Deportivo Táchira | Deportivo Italia |
| 1985 | Estudiantes de Mérida | Deportivo Táchira |
| 1986 | Deportivo Táchira | Estudiantes de Mérida |
| 1986/87 | CS Marítimo | Deportivo Táchira |
| 1987/88 | CS Marítimo | Deportivo Táchira |
| 1988/89 | Mineros de Guayana | Pepeganga Margarita |
| 1989/90 | CS Marítimo | Deportivo Táchira |
| 1990/91 | Universidad de Los Andes | CS Marítimo |
| 1991/92 | Caracas FC | Minervén |
| 1992/93 | CS Marítimo | Minervén |
| 1993/94 | Caracas FC | Trujillanos |
| 1994/95 | Caracas FC | Minervén |
| 1995/96 | Minervén | Mineros de Guayana |
| 1996/97 | Caracas FC | Universidad de Los Andes |
| 1997/98 | Universidad de Los Andes | Estudiantes de Mérida |
| 1998/99 | Deportivo Italia | Deportivo Táchira |
| 1999/00 | Deportivo Táchira | Deportivo Italia |
| 2000/01 | Caracas FC | Trujillanos |
| 2001/02 | Nacional Táchira | Estudiantes de Mérida |
| 2002/03 | Caracas FC | Unión Atlético Maracaibo |
| 2003/04 | Caracas FC | Deportivo Táchira |
| 2004/05 | Unión Atlético Maracaibo | Caracas FC |
| 2005/06 | Caracas FC | Unión Atlético Maracaibo |
| 2006/07 | Caracas FC | Unión Atlético Maracaibo |
| 2007/08 | Deportivo Táchira | Caracas FC |
| 2008/09 | Caracas FC | Deportivo Italia |
| 2009/10 | Caracas FC | Deportivo Táchira |
| 2010/11 | Deportivo Táchira | Zamora FC |
| 2011/12 | Deportivo Lara | Caracas FC |
| 2012/13 | Zamora FC | Deportivo Anzoátegui |
| 2013/14 | Zamora FC | Mineros de Guayana |
| 2014/15 | Deportivo Táchira | Trujillanos |
| 2015 | Zamora FC | Deportivo La Guaira |
| 2016 | Zamora FC | Zulia FC |
| 2017 | Monagas SC | Deportivo Lara |
| 2018 | Zamora FC | Deportivo Lara |
| 2019 | Caracas FC | Estudiantes de Mérida |
| 2020 | Deportivo La Guaira | Deportivo Táchira |
| 2021 | Deportivo Táchira | Caracas FC |
| 2022 | Metropolitanos | Monagas SC |
| 2023 | Deportivo Táchira | Caracas FC |
| 2024 | Deportivo Táchira | Carabobo FC |
| 2025 | Universidad Central | Carabobo FC |

**Rebaixados marcados na classificação:** 17 em 10 edições (só onde a tabela publicada marca a queda); quem mais caiu: Portuguesa FC (2), Mineros de Guayana (2), Deportivo ItalMaracaibo (2), Deportivo Galicia (1), Nacional Táchira (1).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1966: Litoral +10
- 1993/94: Caracas FC +2
- 1993/94: Trujillanos +1
- 1993/94: Minervén +1
- 1993/94: Deportivo Táchira +1
- 1994/95: Caracas FC +10
- 1994/95: Mineros de Guayana +9
- 1994/95: Trujillanos +8
- 1994/95: El Vigía FC +6
- 1994/95: Estudiantes de Mérida +4
- 1994/95: San Cristóbal FC +2
- 1994/95: Deportivo Italia +2
- 1994/95: Anzoátegui FC (1967) +1
- 2001/02: Mineros de Guayana -1
- 2014/15: Deportivo Italia -3
- 2018: Deportivo Anzoátegui -6
- 2019: Caracas FC -1
- 2019: Aragua FC -3
- 2019: Zulia FC -1
- 2019: Llaneros de Guanare -3
- 2019: Deportivo Anzoátegui -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ven-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 3)

- **1940 · venez40:64:** [descartado] quarto Deportivo Español x Loyola num turno triplo (as rodadas 11-15 listam 16 jogos para 15); sem ele a tabela final fecha com os jogos
- **2010/11 · espn:311428:** [gm = 3, gv = 0] a ESPN dá 15-0; a tabela final da RSSSF só fecha com 3-0 (gols pró do El Vigía e contra do Caroní)
- **2010/11 · espn:311418:** [placar oficial 0-3] a ESPN dá 0-0 e a RSSSF lista o jogo sem placar; a tabela final da RSSSF conta vitória do Mineros por 3-0 (provável W.O.)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 12)

- **1966:** a lista de campeões da RSSSF dá o vice Deportivo Galicia e a da Wikipédia em inglês, o Deportivo Portugués; fica o da RSSSF (fonte de base)
- **1975:** a lista de campeões da RSSSF dá o vice Deportivo Galicia e a da Wikipédia em inglês, o Estudiantes de Mérida; fica o da RSSSF (fonte de base)
- **1984:** Petroleros del Zulia x Universidad de Los Andes (15/08) está como "awd" sem placar: a tabela conta derrota por 0-1 para os dois clubes
- **1992/93:** falta um Unión Deportiva Lara x Atlético Zamora (a página só lista o de 13/12, 0-0); pela tabela final, o Zamora venceu o que falta por 1-0
- **1994/95:** 5 jogos do Apertura (Copa Venezuela) estão na página como "drw" (empate sem placar, decidido nos pênaltis) e ficam de fora; "bt" / "lt" (venceu / perdeu sem placar) entram como W.O.
- **1996/97:** o Atlético Zulia (Maracaibo) entra como Universidad de Los Andes, como na lista de campeões da RSSSF ("ULA relocated and renamed Atlético Zulia during the 1996/97 and 1997/98 seasons"); a página da temporada 1996/97 diz que o Atlético Zulia era o Unicol (Lagunillas). Decisão a confirmar com o Guilherme
- **1997/98:** o Atlético Zulia (Maracaibo) entra como Universidad de Los Andes, como na lista de campeões da RSSSF ("ULA relocated and renamed Atlético Zulia during the 1996/97 and 1997/98 seasons"); a página da temporada 1996/97 diz que o Atlético Zulia era o Unicol (Lagunillas). Decisão a confirmar com o Guilherme; o título do Apertura e o do ano ficam com a Universidad de Los Andes
- **1998/99:** o Internacional de Lara entra como Trujillanos ("Trujillanos were relocated and renamed Internacional de Lara", RSSSF); no ano seguinte o Internacional foi para El Vigía e virou El Vigía FC, e o Trujillanos voltou
- **2000/01:** a 1ª fase foi a Copa Venezuela 2000 (Apertura, com final Caracas x Táchira) e a 2ª, o Torneo Nacional 2001, que deu o título; o "Monagas" da 1ª fase é o Atlético Monagas e o do Torneo Nacional, o Monagas SC (que comprou a vaga do El Vigía; "different from Atlético Monagas", RSSSF)
- **2010/11:** o Clausura 2011 tem 82 jogos sem placar na RSSSF: 81 vêm da ESPN; o Caroní x Zulia não está em nenhuma das duas (pela tabela final, o Zulia venceu por 3-0)
- **2011/12:** a página da RSSSF só tem as tabelas: os jogos vêm da ESPN, que não tem dois do Apertura (Mineros x Zamora, 2-1 para o Mineros pela tabela, e Carabobo x Aragua, 1-1 pela tabela)
- **2015:** o Torneo de Adecuación 2015 conta como título na RSSSF (Zamora); a Wikipédia em inglês não o conta como temporada

### Identidade dos clubes

Regras em `coleta/ven-1/clubes_ven.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes venezuelanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Caracas FC", "Deportivo Táchira", "Estudiantes de Mérida", "Zamora FC");
- o mesmo clube com outro nome, como na lista de campeões da RSSSF (venezchamp.html): Unión Atlético Táchira (fusão de 1985
  com o Atlético San Cristóbal, até 1999) é o Deportivo Táchira; ItalChacao (fusão temporária com o Deportivo Chacao) e
  Deportivo Petare (2010-2016) são o Deportivo Italia; o Atlético Zulia (1996/97 e 1997/98) é a Universidad de Los Andes
  levada a Maracaibo e que voltou a Mérida como FCU-ULA (a página de 1996/97 diz que era o Unicol; fica a lista de campeões,
  que conta o título de 1997/98 assim); o Internacional de Lara (1998/99) é o Trujillanos levado a Barquisimeto;
- renomeações na mesma cidade, como nas notas das páginas: UE Lara -> UD Lara (1986/87); Nacional -> Pampero (1948);
  Internacional El Vigía -> El Vigía FC (1999/00); Hermanos Colmenárez -> Internacional de Barinas (2024);
- clubes diferentes, mesmo com licença comprada ou nome parecido: Nacional Táchira ("novo nome da UD Lara", 1996/97, mas em
  outra cidade: fica separado); Atlético Monagas e Monagas SC ("different from", 2000/01); Atlético Zamora (até 2005) e
  Zamora FC; Lara FC (1965-1985), Unión Deportiva Lara (1986-2002) e Deportivo Lara (2009 em diante); Anzoátegui FC (1967),
  Atlético Anzoátegui (1986-1990), Deportivo Anzoátegui (2007 em diante) e Anzoátegui FC (2025); Estudiantes de Caracas
  (era amadora) e Estudiantes de Caracas SC (2015-2019); San Cristóbal FC (1994/95) e Atlético San Cristóbal (1980-1985);
  Aragua FC de 1966-1975 ("Aragua FC (1966)") e o de 2002;
- homônimo de clube do banco ou de outro pacote leva a cidade (Deportivo Español de Caracas, Celta de Caracas, Danubio de
  Caracas, América de Caracas, Universidad Católica de Caracas; conferido com o banco e os outros pacotes).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a 2ª e a 3ª divisões, a Copa Venezuela (salvo quando foi a 1ª fase da temporada: 1993/94, 1994/95, 1995/96 e 2000/01), as outras copas (Copa Caracas, Liga Mayor, de las Naciones, Cuatricentenario, Valencia, de Campeones, Bicentenario), os jogos de promoção e os playoffs da Sudamericana e da Conmebol.
- **Edições sem jogos (7):** 1922, 1924, 1931, 1938, 1939, 1949 e 1950: a RSSSF não tem página desses anos; entram com o campeão e o vice da lista.
- **Edições com jogos incompletos:** a era amadora (1921-1956), salvo 1940, 1955 e 1956: a RSSSF traz só parte dos jogos da liga (ou só o campeão e a classificação; os jogos das copas da mesma página ficam de fora); 1993/94 (o Apertura, que era a Copa Venezuela, só tem as tabelas dos grupos, e 8 jogos da liga estão sem placar); 1994/95 (o Torneo Iniciación só tem as tabelas). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.
- **Edições sem jogos** (25): 1921, 1922, 1923, 1924, 1925, 1927, 1929, 1931, 1932, 1933, 1934, 1935, 1938, 1939, 1941, 1942, 1943, 1944, 1948, 1949, 1950, 1951, 1952, 1953, 1954.
- **Décadas com menos da metade dos gols com autor:** 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Ainda não carregado no banco (no GitHub desde o 35dc0a2).
- Decisão do Guilherme: o Atlético Zulia (1996/97 e 1997/98, campeão de 1997/98) entrou como Universidad de Los Andes, como na lista de campeões da RSSSF; a página de 1996/97 diz que era o Unicol. Se valer a página, o título vai para o Unicol (ou para um 'Atlético Zulia' separado).
- Era amadora (1921-1956): só 1940, 1955 e 1956 têm todos os jogos; 7 anos sem página (1922, 1924, 1931, 1938, 1939, 1949, 1950) e 26 com jogos parciais ou só a classificação. Fonte que resolveria: jornais de Caracas da época (El Universal, La Esfera) ou o livro de Eliézer Pérez, autor das páginas da RSSSF.
- 1993/94 e 1994/95: a Copa Venezuela (Apertura de 1993/94) e o Torneo Iniciación (1994/95) só têm tabelas; 8 jogos da liga de 1993/94 sem placar e 5 'drw' (empate sem placar) em 1994/95.
- Jogos que nenhuma fonte tem: Lara x Zamora (1992/93), Caroní x Zulia (Clausura 2011), Mineros x Zamora e Carabobo x Aragua (Apertura 2011); a tabela final dá o resultado de cada um (explicado no relatório).
- Vice de 1966 e 1975: RSSSF e Wikipédia em inglês divergem; ficou o da RSSSF.
- Artilheiros de 1974 e depois de 2007/08 só pela Wikipédia em inglês (a lista da RSSSF não tem).

## 10. Arquivos e comandos

Código em `coleta/ven-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga ven.1) de 2001 a 2025 para data/coleta/ven-1/espn/ven1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão venezuelana para data/coleta/ven-1/rsssf/: a lista de campeões (venezchamp.html), as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês a página da liga venezuelana ("Liga FUTVE", com a lista de campeões da era amadora e da |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "Liga FUTVE", seções "Amateur era" e "Professional era"), segunda fonte |
| `clubes_ven.py` | Identidade dos clubes venezuelanos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão venezuelana (ven-1): uma por título, como na lista de campeões da RSSSF (venezchamp.html), que conta 106 |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão venezuelana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão venezuelana e grava o pacote em data/coleta/ven-1/pacote/ e o relatório em docs/coleta/ven-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/ven-1/rsssf/) com o leitor comum (rsssf_sul); nas edições |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/ven-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`.
- Pacote: `data/coleta/ven-1/pacote/`; relatório: `docs/coleta/ven-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/ven-1/baixar_espn.py
python coleta/ven-1/baixar_rsssf.py
python coleta/ven-1/baixar_wikipedia.py
python coleta/ven-1/importar.py
python coleta/ven-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py ven-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

