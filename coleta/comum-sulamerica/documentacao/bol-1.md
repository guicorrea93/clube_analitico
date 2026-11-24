# Campeonato Boliviano (`bol-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/bol-1/pacote/`, do código `coleta/bol-1/` e do relatório `docs/coleta/bol-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 94, de 1950 a 2025; 22 sem jogos.
- **Jogos:** 8563 (8556 com placar); **gols:** 26434; **gols com autor:** 21225 (80%); **cartões:** 4996.
- **Clubes:** 77; **artilheiros:** 82 edições com artilheiro (92 linhas, com empates).
- **Classificação final:** 94 edições; **tabelas publicadas guardadas para conferência:** 1626 linhas.
- **No banco:** sim; **último commit do pacote:** c887a7d4.
- **Observação da competição:** 1ª divisão boliviana de 1950 a 2025, uma edição por título: liga de La Paz (1950-1953), Torneo Integrado (1954-1957), Certamen Mixto (1957/58), campeonato nacional (1958-1976, Copa Simón Bolívar a partir de 1960; sem campeonato em 1962) e liga profissional (1977 em diante; Apertura, Clausura e Adecuación dão título de 2003 a 2019 e em 2022). Jogos de 1950, 1953, 1971, 1977 e 1990 em diante (incompletos em 1990-1994); nos outros anos, campeão, vice e a tabela final da RSSSF.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão boliviana (bol-1): uma por título, de 1950 a 2025, como na lista de campeões da Wikipédia em inglês
("FBF División Profesional") e na contagem de 93 campeonatos da RSSSF (bolchamp.html).

- 1950-1953: liga de La Paz, semiprofissional desde 1950 (antes dela, a liga amadora de La Paz fica de fora, como na
  Wikipédia);
- 1954-1957: Torneo Integrado (La Paz, Oruro e Cochabamba);
- 1957 Mixto: Certamen Nacional Mixto 1957/58 (clubes de Cochabamba e Oruro), título à parte;
- 1958-1976: campeonato nacional (Torneo Nacional 1958-1959; Copa Simón Bolívar de 1960 a 1976); sem campeonato em 1962.
  De 1960 a 1976 os campeonatos regionais (o de La Paz e os outros) eram a fase classificatória e ficam de fora;
- 1977 em diante: liga profissional (LFPB, desde 2018 FBF División Profesional). Até 2002 um campeão por ano (Apertura e
  Clausura são fases); de 2003 a 2019 e em 2022, Apertura, Clausura e Adecuación dão título cada um (uma edição cada;
  2005 Apertura é o Apertura 2005/06, abortado; 2011/12 e 2016/17 no calendário europeu). 2022 Clausura foi abandonado
  (edição sem campeão). 2020, 2021 e 2023-2025: um campeão por ano.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). 1971, 1977, 1992-1994 e 1995 em diante;
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1950 e 1953 completos; 1990 e 1991 quase completos;
  só a fase final em 1951, 1960, 1966, 1968, 1976, 1978, 1979, 1982, 1983 e 1985-1989;
- tabelas: a seção do ano em bolhist.html (tabelas finais de 1950 a 1990): de 1965 a 1976 só a parte "(Nacional)";
- espn: datas dos jogos que vêm da ESPN (nenhuma edição precisa: a RSSSF tem os jogos de 1995 em diante).
Nas edições com jogos incompletos (incompleta), a classificação é a tabela publicada, sem conferência.
```

**Edições:** 94, uma por título de 1950 a 2025, como na lista de campeões da Wikipédia em inglês (página "FBF División Profesional") e na contagem de 93 campeonatos da RSSSF (`bolchamp.html`), mais o Clausura 2022, abandonado (edição sem campeão). Liga de La Paz semiprofissional (1950-1953), Torneo Integrado (1954-1957), Certamen Nacional Mixto (1957/58, edição "1957 Mixto"), campeonato nacional (1958-1976; Copa Simón Bolívar de 1960 a 1976; sem campeonato em 1962) e liga profissional (1977 em diante). Até 2002, Apertura e Clausura são fases do ano; de 2003 a 2019 e em 2022, cada torneio que dá título é uma edição (2005 Apertura é o Apertura 2005/06, abortado; 2011/12 e 2016/17 no calendário europeu).

**Fontes:** RSSSF (uma página por temporada de 1971, 1977 e 1990 em diante, e a lista de tabelas finais `bolhist.html` de 1950 a 1990, em `data/coleta/bol-1/rsssf/`: base de jogos de 1977 e 1992 em diante, com fases, grupos, rodadas, datas e autores dos gols); Wikipédia em espanhol (jogos de 1950, 1953, 1990 e 1991 e das fases finais de outros anos; em `data/coleta/bol-1/wikipedia/`); ESPN (liga `bol.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões: segunda fonte do campeão, fonte do vice de 1977 em diante e dos artilheiros fora da lista da RSSSF, que vai de 1977 a 2005).

**Clubes:** nome pelo qual o clube é conhecido (Bolívar, The Strongest, Jorge Wilstermann, Oriente Petrolero). Homônimos levam a cidade: os Universitarios (de La Paz, Sucre, Potosí, Beni, Pando e Vinto), Ferroviario de La Paz, Municipal de La Paz, Internacional de Oruro (1957) e de La Paz (1958-1960), Litoral de La Paz e de Cochabamba, Petrolero de Cochabamba e de Yacuiba, Primero de Mayo de La Paz e de Potosí. O mesmo clube com outro nome fica com o atual: Deportivo Chaco = Chaco Petrolero; Universidad Iberoamericana = Iberoamericana; CDT Real Oruro = Real Oruro; Atlético Palmaflor = Palmaflor.

**Regras:** o placar é o da fonte de base (RSSSF ou Wikipédia). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação; "awarded to X (originally 0-0)" vira vitória de X com os gols do campo, como a tabela conta. Ida e volta numa linha só ("A 1-0 0-4 B") vira dois jogos, com os gols de A primeiro e o mando da volta presumido. Pontos: 2 por vitória até 1994 e 3 a partir de 1995. Nas edições sem jogos, campeão e vice da lista ficam em 1º e 2º mesmo quando não estão na tabela usada (sem a campanha).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 42.
- **Edições com alguma tabela divergente** (10; motivo no relatório, na edição): 1950, 1953, 1977, 1995, 1996, 1997, 1998, 1999, 2001, 2002.
- **Edições sem tabela para conferir** (42): 1951, 1952, 1954, 1955, 1956, 1957, 1957 Mixto, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994.
- **Edições com menos jogos que o esperado:** nenhuma.
- **Edições com mais jogos que o esperado** (desempates e jogos fora da tabela publicada): 2019 Clausura (182 de 181).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 11 | 132 | 98% | 0% | 97% | 1% | 0% | 0% | 0% | 0.0 |
| 1960s | 9 | 66 | 64% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 237 | 95% | 0% | 93% | 2% | 0% | 0% | 4% | 0.0 |
| 1980s | 10 | 27 | 100% | 0% | 0% | 100% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1396 | 86% | 0% | 22% | 1% | 0% | 0% | 21% | 0.0 |
| 2000s | 17 | 2389 | 100% | 41% | 100% | 41% | 39% | 0% | 99% | 0.7 |
| 2010s | 20 | 2730 | 100% | 83% | 100% | 83% | 77% | 0% | 98% | 1.0 |
| 2020s | 7 | 1586 | 100% | 100% | 100% | 90% | 90% | 0% | 99% | 0.2 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1950: 9 clubes
- 1951 a 1953: 8 clubes
- 1954: 9 clubes
- 1955: 11 clubes
- 1956: 12 clubes
- 1957: 8 clubes
- 1957 Mixto: 7 clubes
- 1958 a 1959: 12 clubes
- 1960: 8 clubes
- 1961 a 1964: 0 clubes
- 1965 a 1966: 4 clubes
- 1967 a 1968: 6 clubes
- 1969: 12 clubes
- 1970: 0 clubes
- 1971 a 1973: 13 clubes
- 1974: 0 clubes
- 1975: 19 clubes
- 1976: 15 clubes
- 1977 a 1978: 16 clubes
- 1979: 17 clubes
- 1980 a 1984: 14 clubes
- 1985 a 1986: 15 clubes
- 1987: 14 clubes
- 1988: 13 clubes
- 1989: 12 clubes
- 1990: 13 clubes
- 1991: 14 clubes
- 1992: 16 clubes
- 1993: 15 clubes
- 1994: 13 clubes
- 1995 a 2016/17 Clausura: 12 clubes
- 2018 Apertura a 2020: 14 clubes
- 2021 a 2022 Clausura: 16 clubes
- 2023: 17 clubes
- 2024 a 2025: 16 clubes

**Pontos por vitória:**

- 1950 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1950 a 1953: Campeonato de La Paz <ano>
- 1954 a 1957: Torneo Integrado <ano>
- 1957 Mixto: Certamen Nacional Mixto <ano>
- 1958 a 1959: Torneo Nacional <ano>
- 1960 a 1976: Copa Simón Bolívar <ano>
- 1977 a 2002: Liga de Fútbol Profesional Boliviano <ano>
- 2003 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2003 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2004 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2004 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2005 Adecuación: Liga de Fútbol Profesional Boliviano <ano> – Adecuación
- 2005 Apertura a 2006 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2006 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2007 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2007 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2008 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2008 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2009 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2009 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2010 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2010 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2011/12 Adecuación: Liga de Fútbol Profesional Boliviano <ano> – Adecuación
- 2011/12 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2011/12 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2012/13 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2012/13 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2013/14 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2013/14 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2014/15 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2014/15 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2015/16 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2015/16 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2016/17 Apertura: Liga de Fútbol Profesional Boliviano <ano> – Apertura
- 2016/17 Adecuación: Liga de Fútbol Profesional Boliviano <ano> – Adecuación
- 2016/17 Clausura: Liga de Fútbol Profesional Boliviano <ano> – Clausura
- 2018 Apertura: División Profesional <ano> – Apertura
- 2018 Clausura: División Profesional <ano> – Clausura
- 2019 Apertura: División Profesional <ano> – Apertura
- 2019 Clausura: División Profesional <ano> – Clausura
- 2020 a 2021: División Profesional <ano>
- 2022 Apertura: División Profesional <ano> – Apertura
- 2022 Clausura: División Profesional <ano> – Clausura
- 2023 a 2025: División Profesional <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1950: pontos corridos + desempate
- 1951: desempate
- 1952: sem jogos (só a tabela final)
- 1953: pontos corridos
- 1954 a 1959: sem jogos (só a tabela final)
- 1960: 2 grupos
- 1961 a 1965: sem jogos (só a tabela final)
- 1966: pontos corridos
- 1967: sem jogos (só a tabela final)
- 1968: pontos corridos
- 1969 a 1970: sem jogos (só a tabela final)
- 1971: pontos corridos
- 1972 a 1975: sem jogos (só a tabela final)
- 1976: pontos corridos
- 1977: 2 grupos + desempate + 2 grupos + pontos corridos + mata-mata
- 1978: pontos corridos + desempate
- 1979: pontos corridos
- 1980 a 1981: sem jogos (só a tabela final)
- 1982: pontos corridos + desempate
- 1983: mata-mata + desempate + mata-mata
- 1984: sem jogos (só a tabela final)
- 1985 a 1988: pontos corridos
- 1989 a 1990: pontos corridos + mata-mata
- 1991: pontos corridos + mata-mata + desempate
- 1992: mata-mata
- 1993: 2 grupos + pontos corridos
- 1994: pontos corridos + mata-mata + desempate
- 1995: 2 grupos + mata-mata + 2 grupos + mata-mata
- 1996 a 1997: 2 grupos + mata-mata + 2 grupos + pontos corridos + mata-mata
- 1998: pontos corridos + mata-mata
- 1999: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 2000: pontos corridos + mata-mata + desempate
- 2001: pontos corridos + mata-mata + 2 grupos + mata-mata
- 2002: pontos corridos + desempate
- 2003 Apertura: pontos corridos
- 2003 Clausura: 2 grupos + pontos corridos
- 2004 Apertura: pontos corridos
- 2004 Clausura: 2 grupos + pontos corridos + mata-mata + desempate
- 2005 Adecuación: pontos corridos
- 2005 Apertura: 2 grupos + pontos corridos
- 2006 Apertura: pontos corridos
- 2006 Clausura: 2 grupos + pontos corridos
- 2007 Apertura: pontos corridos
- 2007 Clausura: 2 grupos + pontos corridos + mata-mata
- 2008 Apertura: pontos corridos
- 2008 Clausura: pontos corridos + mata-mata + desempate
- 2009 Apertura: pontos corridos
- 2009 Clausura: 2 grupos + mata-mata
- 2010 Apertura: 2 grupos + pontos corridos
- 2010 Clausura a 2011/12 Adecuación: pontos corridos
- 2011/12 Apertura: 2 grupos + desempate + mata-mata
- 2011/12 Clausura a 2015/16 Clausura: pontos corridos
- 2016/17 Apertura: pontos corridos + mata-mata
- 2016/17 Adecuación a 2016/17 Clausura: pontos corridos
- 2018 Apertura: 2 grupos + desempate + mata-mata + desempate
- 2018 Clausura a 2021: pontos corridos
- 2022 Apertura: 2 grupos + mata-mata
- 2022 Clausura a 2023: pontos corridos
- 2024: 4 grupos + mata-mata + pontos corridos + mata-mata
- 2025: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1950: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1977: Primeira fase (grupos, 2 grupos); Desempate da segunda fase (mata_mata, jogo_unico); Segunda fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 1978: Fase final (liga); Desempate do título (mata_mata, jogo_unico)
- 1982: Segunda fase (liga); Desempate do título (mata_mata, ida_volta)
- 1983: Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1989: Primeira fase (liga); Final (mata_mata, ida_volta)
- 1990: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 1991: Apertura (liga); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1992: Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1993: Primeira fase (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1994: Primeira fase (liga); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1995: Apertura (grupos, 2 grupos); Semifinal do Apertura (mata_mata, ida_volta); Clausura (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1996: Apertura (grupos, 2 grupos); Semifinal do Apertura (mata_mata, ida_volta); Clausura (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 1997: Apertura (grupos, 2 grupos); Semifinal do Apertura (mata_mata, ida_volta); Clausura (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 1998: Apertura (liga); Clausura (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1999: Apertura (liga); Clausura (grupos, 2 grupos); Fase final do Clausura (liga); Final (mata_mata, ida_volta)
- 2000: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 2001: Apertura (liga); Final do Apertura (mata_mata, jogo_unico); Clausura (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002: Apertura (liga); Clausura (liga); Desempate do 2º lugar (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 2004 Clausura: Primeira fase (grupos, 2 grupos); Segunda fase (liga); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 2005 Apertura: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2006 Clausura: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2007 Clausura: Primeira fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 2009 Clausura: Primeira fase (grupos, 2 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Apertura: Primeira fase (grupos, 2 grupos); Segunda fase (liga)
- 2011/12 Apertura: Primeira fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016/17 Apertura: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 2018 Apertura: Primeira fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 2022 Apertura: Primeira fase (grupos, 2 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2024: Apertura (grupos, 4 grupos); Quartas de final do Apertura (mata_mata, ida_volta); Semifinal do Apertura (mata_mata, ida_volta); Final do Apertura (mata_mata, ida_volta); Clausura (liga); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 67 edições
- calculada: 19 edições
- lista de campeões da Wikipédia em inglês: 6 edições
- lista de campeões: 2 edições

**Observações das edições:**

- 1952: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1954: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1955: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1956: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1957: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1957 Mixto: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1958: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1959: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1961: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1963: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1964: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1965: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1967: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1969: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1970: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1972: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1973: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1974: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1975: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1980: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1981: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 1984: sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)
- 2022 Clausura: abandonado (protestos no departamento de Santa Cruz): sem campeão

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Bolívar: 31
- The Strongest: 16
- Jorge Wilstermann: 15
- Oriente Petrolero: 5
- Blooming: 5
- Always Ready: 4
- San José: 4
- Municipal de La Paz: 2
- Aurora: 2
- Universitario de Sucre: 2
- Litoral de La Paz: 1
- Universitario de La Paz: 1
- Chaco Petrolero: 1
- Guabirá: 1
- Real Potosí: 1
- Sport Boys Warnes: 1
- Independiente Petrolero: 1
- Sem campeão: 2022 Clausura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1950 | Bolívar | Litoral de La Paz |
| 1951 | Always Ready | Bolívar |
| 1952 | The Strongest | Always Ready |
| 1953 | Bolívar | Always Ready |
| 1954 | Litoral de La Paz | The Strongest |
| 1955 | San José | Chaco Petrolero |
| 1956 | Bolívar | Municipal de La Paz |
| 1957 | Always Ready | Municipal de La Paz |
| 1957 Mixto | Jorge Wilstermann | Aurora |
| 1958 | Jorge Wilstermann | Municipal de La Paz |
| 1959 | Jorge Wilstermann | Always Ready |
| 1960 | Jorge Wilstermann | Aurora |
| 1961 | Municipal de La Paz | Aurora |
| 1963 | Aurora | Municipal de La Paz |
| 1964 | The Strongest | Aurora |
| 1965 | Municipal de La Paz | Jorge Wilstermann |
| 1966 | Bolívar | 31 de Octubre |
| 1967 | Jorge Wilstermann | Always Ready |
| 1968 | Bolívar | Guabirá |
| 1969 | Universitario de La Paz | Bolívar |
| 1970 | Chaco Petrolero | The Strongest |
| 1971 | Oriente Petrolero | Chaco Petrolero |
| 1972 | Jorge Wilstermann | Oriente Petrolero |
| 1973 | Jorge Wilstermann | Municipal de La Paz |
| 1974 | The Strongest | Jorge Wilstermann |
| 1975 | Guabirá | Bolívar |
| 1976 | Bolívar | Oriente Petrolero |
| 1977 | The Strongest | Oriente Petrolero |
| 1978 | Bolívar | Jorge Wilstermann |
| 1979 | Oriente Petrolero | The Strongest |
| 1980 | Jorge Wilstermann | The Strongest |
| 1981 | Jorge Wilstermann | Blooming |
| 1982 | Bolívar | Jorge Wilstermann |
| 1983 | Bolívar | Oriente Petrolero |
| 1984 | Blooming | Bolívar |
| 1985 | Bolívar | Jorge Wilstermann |
| 1986 | The Strongest | Oriente Petrolero |
| 1987 | Bolívar | Oriente Petrolero |
| 1988 | Bolívar | The Strongest |
| 1989 | The Strongest | Oriente Petrolero |
| 1990 | Oriente Petrolero | Bolívar |
| 1991 | Bolívar | San José |
| 1992 | Bolívar | San José |
| 1993 | The Strongest | Bolívar |
| 1994 | Bolívar | Jorge Wilstermann |
| 1995 | San José | Guabirá |
| 1996 | Bolívar | Oriente Petrolero |
| 1997 | Bolívar | Oriente Petrolero |
| 1998 | Blooming | Jorge Wilstermann |
| 1999 | Blooming | The Strongest |
| 2000 | Jorge Wilstermann | Oriente Petrolero |
| 2001 | Oriente Petrolero | Bolívar |
| 2002 | Bolívar | Oriente Petrolero |
| 2003 Apertura | The Strongest | Bolívar |
| 2003 Clausura | The Strongest | Jorge Wilstermann |
| 2004 Apertura | Bolívar | Aurora |
| 2004 Clausura | The Strongest | Oriente Petrolero |
| 2005 Adecuación | Bolívar | The Strongest |
| 2005 Apertura | Blooming | Bolívar |
| 2006 Apertura | Bolívar | Real Potosí |
| 2006 Clausura | Jorge Wilstermann | Real Potosí |
| 2007 Apertura | Real Potosí | Bolívar |
| 2007 Clausura | San José | La Paz FC |
| 2008 Apertura | Universitario de Sucre | La Paz FC |
| 2008 Clausura | Aurora | Blooming |
| 2009 Apertura | Bolívar | Real Potosí |
| 2009 Clausura | Blooming | Bolívar |
| 2010 Apertura | Jorge Wilstermann | Oriente Petrolero |
| 2010 Clausura | Oriente Petrolero | Bolívar |
| 2011/12 Adecuación | Bolívar | Real Potosí |
| 2011/12 Apertura | The Strongest | Universitario de Sucre |
| 2011/12 Clausura | The Strongest | San José |
| 2012/13 Apertura | The Strongest | San José |
| 2012/13 Clausura | Bolívar | Oriente Petrolero |
| 2013/14 Apertura | The Strongest | Bolívar |
| 2013/14 Clausura | Universitario de Sucre | San José |
| 2014/15 Apertura | Bolívar | Oriente Petrolero |
| 2014/15 Clausura | Bolívar | The Strongest |
| 2015/16 Apertura | Sport Boys Warnes | Bolívar |
| 2015/16 Clausura | Jorge Wilstermann | The Strongest |
| 2016/17 Apertura | The Strongest | Bolívar |
| 2016/17 Adecuación | Bolívar | The Strongest |
| 2016/17 Clausura | Bolívar | The Strongest |
| 2018 Apertura | Jorge Wilstermann | The Strongest |
| 2018 Clausura | San José | The Strongest |
| 2019 Apertura | Bolívar | The Strongest |
| 2019 Clausura | Jorge Wilstermann | The Strongest |
| 2020 | Always Ready | The Strongest |
| 2021 | Independiente Petrolero | Always Ready |
| 2022 Apertura | Bolívar | The Strongest |
| 2022 Clausura | — | — |
| 2023 | The Strongest | Bolívar |
| 2024 | Bolívar | San Antonio Bulo Bulo |
| 2025 | Always Ready | Bolívar |

**Rebaixados marcados na classificação:** 18 em 10 edições (só onde a tabela publicada marca a queda); quem mais caiu: Always Ready (1), Independiente Unificada (1), Independiente Petrolero (1), Guabirá (1), Primero de Mayo de Potosí (1).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1990: Bolívar +2
- 1990: San José +2
- 1991: Independiente Petrolero -4
- 1994: Bolívar +1
- 2007 Apertura: Bolívar +3
- 2007 Apertura: Oriente Petrolero -3
- 2007 Apertura: The Strongest +2
- 2007 Apertura: San José -1
- 2009 Apertura: Universitario de Sucre -3
- 2010 Clausura: The Strongest -3
- 2016/17 Clausura: Bolívar +2
- 2016/17 Clausura: Jorge Wilstermann -3
- 2018 Clausura: Universitario de Sucre -3
- 2019 Clausura: San José -6
- 2019 Clausura: Sport Boys Warnes -6
- 2021: San José +10
- 2023: Jorge Wilstermann -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/bol-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 3)

- **bol77 · 72:** «2 de Agosto» → «20 de Agosto»: o 20 de Agosto (Beni) é o único dos 16 clubes que falta na rodada; "2 de Agosto" e "10 de Agosto" não existem no campeonato de 1977
- **bol77 · 84:** «10 de Agosto» → «20 de Agosto»: o 20 de Agosto (Beni) é o único dos 16 clubes que falta na rodada; "2 de Agosto" e "10 de Agosto" não existem no campeonato de 1977
- **bol2024 · 325:** «Final» → «Apertura Final»: a final do Apertura 2024 (o título do ano veio do Clausura): o título "Final" sozinho é lido como a final do ano

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 1)

- **2003 Apertura · bol03:230:** [descartado] jogo interrompido por temporal no intervalo (1-2) e completado depois (linha 233, "[remaining 45']", 2-3): fica a segunda

### Divergências entre fontes já explicadas (`EXPLICACOES`, 6)

- **1961:** a lista de campeões da RSSSF dá o vice Aurora e a da Wikipédia em inglês, o The Strongest; fica o da RSSSF (fonte de base)
- **1963:** a lista de campeões da RSSSF dá o vice Deportivo Municipal e a da Wikipédia em inglês, o Jorge Wilstermann; fica o da RSSSF (fonte de base)
- **1964:** a lista de campeões da RSSSF dá o vice Aurora e a da Wikipédia em inglês, o Deportivo Municipal; fica o da RSSSF (fonte de base)
- **1968:** a lista de campeões da RSSSF dá o vice Guabirá e a da Wikipédia em inglês, o Litoral de Cochabamba; fica o da RSSSF (fonte de base; a tabela final da RSSSF também põe o Guabirá em 2º)
- **1950:** os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols de quatro clubes diferem em um ou dois
- **1953:** os jogos vêm da Wikipédia em espanhol e a tabela é da RSSSF: os gols do Ferroviario diferem (a Wikipédia tem um placar diferente num jogo dele)

### Identidade dos clubes

Regras em `coleta/bol-1/clubes_bol.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes bolivianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Bolívar", "The Strongest", "Jorge Wilstermann", "Oriente Petrolero");
- homônimo de clube do banco ou de outro pacote leva a cidade: os Universitarios (de La Paz, Sucre, Potosí, Beni, Pando e
  Vinto; o Universitario é o peruano), "Ferroviario de La Paz", "Internacional de Oruro" (Certamen Mixto 1957) e
  "Internacional de La Paz" (1958-1960), "Municipal de La Paz" (o Deportivo Municipal é o peruano); clubes bolivianos com o
  mesmo nome também: "Litoral de La Paz" e "Litoral de Cochabamba" (1966-1969), "Petrolero de Cochabamba" e "Petrolero de
  Yacuiba", "Primero de Mayo de La Paz" (1958-1959) e "Primero de Mayo de Potosí" (1983-1984), "31 de Octubre" (La Paz) e
  "31 de Octubre de Oruro" (1975), "Stormers" (Sucre) e "Stormers Petrolero" (Potosí);
- o mesmo clube com outro nome em outra época fica com o nome atual: Deportivo Chaco (até 1962) é o Chaco Petrolero;
  Universidad Iberoamericana é o Iberoamericana; CDT Real Oruro / CD Totora Real Oruro é o Real Oruro; Atlético Palmaflor
  (Palmaflor del Trópico) é o Palmaflor;
- nomes curtos das páginas: "Oriente", "Chaco", "Strongest", "Wilstermann", "Independiente" (Independiente Petrolero),
  "Municipal", "Petrolero" (o de Cochabamba até 1993), "Universitario" (depende do ano);
- de 1995 a 1998 as páginas da RSSSF põem a cidade antes do clube ("Cochabamba Wilstermann", "Santa Cruz Blooming"): a
  cidade cai antes de procurar o clube.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a liga amadora de La Paz (1914-1949), os campeonatos regionais que serviam de classificatória do nacional (1960-1976), a Copa Simón Bolívar de 2ª divisão (1977 em diante), a Nacional B, as copas (Copa Bolivia, Copa de la División Profesional, Copa Paceña), os playoffs da Libertadores e da Sudamericana e os jogos de promoção.
- **Edições sem jogos (22):** 1952, 1954-1959 (com o 1957 Mixto), 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981 e 1984. Pesquisamos RSSSF (só tabelas finais, em `bolhist.html`), Wikipédia em espanhol e inglês e ogol (sem jogos bolivianos antigos): nenhuma fonte pública traz os jogos. Entram com o campeão, o vice e a tabela final da RSSSF quando há (não há tabela do nacional de 1960 a 1964).
- **Edições com jogos incompletos:** 1951, 1960, 1966, 1968, 1971, 1976, 1978, 1979, 1982, 1983 e 1985-1989 (só as fases finais, da Wikipédia em espanhol ou da RSSSF), 1990 e 1991 (jogos da Wikipédia sem a divisão em fases das tabelas da RSSSF) e 1992-1994 (a RSSSF tem só as tabelas da maior parte das fases). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.
- **Edições sem jogos** (22): 1952, 1954, 1955, 1956, 1957, 1957 Mixto, 1958, 1959, 1961, 1963, 1964, 1965, 1967, 1969, 1970, 1972, 1973, 1974, 1975, 1980, 1981, 1984.
- **Décadas com menos da metade dos gols com autor:** 1950s, 1960s, 1970s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Pedido do agente 1 (22/11, para quando o Guilherme mandar revisar): a classificação final de 1960, 1976, 1990, 1993 e 1994 deve trazer todos os clubes com jogos (eliminados com a posição da fase em que caíram), como no bra-sp-2.
- 22 edições sem jogos (1952, 1954-1959 com o 1957 Mixto, 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981, 1984): nenhuma fonte pública tem; o nacional de 1960-1964 não tem nem tabela (só campeão e vice). Fonte que resolveria: jornais da época ou um almanaque boliviano (ex.: historiadelfutbolboliviano.com, de Carlos Mesa).
- Jogos incompletos em 1951, 1960, 1966, 1968, 1971, 1976, 1978, 1979, 1982, 1983, 1985-1994: só as fases finais (ou jogos sem a divisão em fases, em 1990-1991). A tabela de confrontos parcial de 1992 ('Partial results', com células vazias) não foi lida: precisaria de leitura por coluna.
- Vice de 1961, 1963, 1964 e 1968: RSSSF e Wikipédia em inglês divergem; ficou o da RSSSF (decisão do agente, explicada no relatório). Conferir numa terceira fonte.
- Nomes que dependem do ano, a conferir: 'Universitario' sozinho de 1971 a 1994 = Universitario de Potosí; 'Litoral' de 1992 (a tabela da RSSSF diz [Oruro]) = Litoral de La Paz.

## 10. Arquivos e comandos

Código em `coleta/bol-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga bol.1) de 2001 a 2025 para data/coleta/bol-1/espn/bol1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão boliviana para data/coleta/bol-1/rsssf/. |
| `baixar_wikipedia.py` | Baixa da Wikipédia o texto-fonte das temporadas bolivianas que a RSSSF não traz jogo a jogo (1950-1994, menos 1977) e |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "FBF División Profesional", seção "List of champions"), segunda fonte |
| `clubes_bol.py` | Identidade dos clubes bolivianos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão boliviana (bol-1): uma por título, de 1950 a 2025, como na lista de campeões da Wikipédia em inglês |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão boliviana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão boliviana e grava o pacote em data/coleta/bol-1/pacote/ e o relatório em docs/coleta/bol-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/bol-1/rsssf/) com o leitor comum (rsssf_sul); nas edições |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wikipedia_jogos.py` | Jogos da Wikipédia em espanhol (data/coleta/bol-1/wikipedia/es_<chave>.txt), para os anos que a RSSSF não tem. |

- Fontes baixadas: `data/coleta/bol-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`, do ogol em `data/cache/ogol-bol-1/`.
- Pacote: `data/coleta/bol-1/pacote/`; relatório: `docs/coleta/bol-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/bol-1/baixar_espn.py
python coleta/bol-1/baixar_rsssf.py
python coleta/bol-1/baixar_wikipedia.py
python coleta/bol-1/importar.py
python coleta/bol-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py bol-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

