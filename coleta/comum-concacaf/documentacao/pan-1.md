# Campeonato Panamenho (`pan-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/pan-1/pacote/`, do código `coleta/pan-1/` e do relatório `docs/coleta/pan-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 66, de 1988 a 2026 Clausura; 15 sem jogos.
- **Jogos:** 4520 (4512 com placar); **gols:** 10941; **gols com autor:** 1668 (15%); **cartões:** 0.
- **Clubes:** 33; **artilheiros:** 5 edições com artilheiro (5 linhas, com empates).
- **Classificação final:** 66 edições; **tabelas publicadas guardadas para conferência:** 577 linhas.
- **No banco:** sim; **último commit do pacote:** 83c08786.
- **Observação da competição:** ANAPROF (1988-2009) e Liga Panameña de Fútbol (2009 em diante) até o Clausura 2026, uma edição por título, como a lista da RSSSF: um campeão por temporada até 2000/01, Apertura e Clausura de 2001 em diante (dois Aperturas em 2009; Apertura 2020 sem campeão), mais as duas edições da LINFUNA (1994/95 e 1995/96, a liga paralela do racha). A final entre os campeões do Apertura e do Clausura (2002-2006) fica fora. Antes de 1988 fica fora.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão do Panamá (pan-1): a ANAPROF (1988-2009) e a Liga Panameña de Fútbol (LPF, 2009 em diante), uma
edição por título, como na lista de campeões da RSSSF (tablesp/panamachamp.html, 63 títulos desde 1988) e na contagem da
imprensa local. Escopo decidido em 25/11/2026 (ok do Guilherme):

- 1988 a 2000/01: um campeão por temporada ("1988", "1994/95"); antes de 1988 só havia ligas da capital e de Colón, e os
  campeões nacionais de 1952 a 1987 são desconhecidos: ficam fora;
- LINFUNA (1994/95 e 1995/96): a liga paralela do racha, reconhecida pela FIFA na época, entra como edição à parte
  ("1994/95 LINFUNA"); a RSSSF a soma no total de títulos e a imprensa local conta os dois títulos do Árabe Unido;
- 2001 em diante: Apertura e Clausura, uma edição cada, com o ano do torneio ("2001 Apertura", "2010 Clausura" = Clausura
  2009/10); a final entre os dois campeões (2002, 2005 e 2006) virou uma supercopa e fica fora; em 2009 há dois Aperturas,
  o último da ANAPROF ("2009 Apertura ANAPROF") e o primeiro da LPF ("2009 Apertura"); o Apertura 2020 (pandemia) entra sem
  campeão; depois do Clausura 2025 veio o Clausura 2026.

Fonte de cada edição: a página da temporada da RSSSF (o título diz a temporada); de 1989 a 1993, a ANAPROF de 1994/95 e
1995/96 e 2001 não têm página: só o campeão e o vice da lista. A edição entra só com as tabelas quando o trecho tem menos de
90% dos jogos.
```

**Edições:** 66, uma por título, como a lista de campeões da RSSSF (`panamachamp.html`, 63 títulos desde 1988, mais os 2 da LINFUNA no total), que é também a contagem da imprensa local (Tauro 17, Árabe Unido 15 com a LINFUNA). Escopo decidido em 25/11/2026: de 1988 (primeira temporada da ANAPROF) em diante; antes só havia ligas da capital e de Colón, e os campeões nacionais de 1952 a 1987 são desconhecidos. Um campeão por temporada até 2000/01; Apertura e Clausura de 2001 em diante, uma edição cada (a liga passou a contar os dois torneios de 2001 a 2006 como títulos; a final entre os dois campeões fica fora, como supercopa). Em 2009 houve dois Aperturas, o último da ANAPROF e o primeiro da LPF; o Apertura 2020 (pandemia) entra sem campeão; depois do Clausura 2025 veio o Clausura 2026. As duas temporadas da LINFUNA (1994/95 e 1995/96, a liga paralela do racha, reconhecida pela FIFA na época) entram como edições à parte, só com a final.

**Fontes:** RSSSF (`data/coleta/pan-1/rsssf/`: a lista de campeões e as páginas das temporadas, casadas pelo título). A ESPN não cobre o Panamá.

**Clubes:** nomes e identidades no começo de `coleta/pan-1/clubes_pan.py`. Homônimos de clubes de outros países levam o país: Alianza de Panamá, Atlético Nacional de Panamá, SD Atlético Nacional de Panamá.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 44.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 1997/98, 2004 Apertura, 2008 Apertura.
- **Edições sem tabela para conferir** (19): 1988, 1989, 1990, 1991, 1992, 1993, 1994/95, 1994/95 LINFUNA, 1995/96, 1995/96 LINFUNA, 1996/97, 1999/00, 2001 Apertura, 2001 Clausura, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura, 2020 Apertura.
- **Edições com menos jogos que o esperado:** 2004 Clausura (96 de 95), 2007 Apertura (97 de 95), 2007 Clausura (96 de 95), 2008 Clausura (96 de 95), 2015 Apertura (96 de 95).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1980s | 2 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 12 | 308 | 53% | 0% | 99% | 0% | 0% | 0% | 22% | 0.0 |
| 2000s | 19 | 1460 | 84% | 0% | 100% | 0% | 0% | 0% | 37% | 0.0 |
| 2010s | 20 | 1527 | 100% | 0% | 100% | 0% | 0% | 0% | 1% | 0.0 |
| 2020s | 13 | 1225 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1988 a 1994/95: 0 clubes
- 1994/95 LINFUNA: 2 clubes
- 1995/96: 0 clubes
- 1995/96 LINFUNA: 2 clubes
- 1996/97 a 1997/98: 12 clubes
- 1998/99: 10 clubes
- 1999/00: 8 clubes
- 2000/01: 10 clubes
- 2001 Apertura a 2001 Clausura: 0 clubes
- 2002 Apertura a 2003 Clausura: 8 clubes
- 2004 Apertura a 2005 Apertura: 10 clubes
- 2005 Clausura: 9 clubes
- 2006 Apertura a 2011 Clausura: 10 clubes
- 2011 Apertura a 2012 Clausura: 9 clubes
- 2012 Apertura a 2020 Clausura: 10 clubes
- 2021 Apertura a 2026 Clausura: 12 clubes

**Pontos por vitória:**

- 1988 a 1994/95 LINFUNA: 2
- 1995/96 a 2026 Clausura: 3

**Nome oficial:**

- 1988 a 1994/95: ANAPROF <ano>
- 1994/95 LINFUNA: LINFUNA <ano>
- 1995/96: ANAPROF <ano>
- 1995/96 LINFUNA: LINFUNA <ano>
- 1996/97 a 2000/01: ANAPROF <ano>
- 2001 Apertura: ANAPROF Apertura <ano>
- 2001 Clausura: ANAPROF Clausura <ano>
- 2002 Apertura: ANAPROF Apertura <ano>
- 2002 Clausura: ANAPROF Clausura <ano>
- 2003 Apertura: ANAPROF Apertura <ano>
- 2003 Clausura: ANAPROF Clausura <ano>
- 2004 Apertura: ANAPROF Apertura <ano>
- 2004 Clausura: ANAPROF Clausura <ano>
- 2005 Apertura: ANAPROF Apertura <ano>
- 2005 Clausura: ANAPROF Clausura <ano>
- 2006 Apertura: ANAPROF Apertura <ano>
- 2006 Clausura: ANAPROF Clausura <ano>
- 2007 Apertura: ANAPROF Apertura <ano>
- 2007 Clausura: ANAPROF Clausura <ano>
- 2008 Apertura: ANAPROF Apertura <ano>
- 2008 Clausura: ANAPROF Clausura <ano>
- 2009 Apertura ANAPROF: ANAPROF Apertura <ano>
- 2009 Apertura: LPF Apertura <ano>
- 2010 Clausura: LPF Clausura <ano>
- 2010 Apertura: LPF Apertura <ano>
- 2011 Clausura: LPF Clausura <ano>
- 2011 Apertura: LPF Apertura <ano>
- 2012 Clausura: LPF Clausura <ano>
- 2012 Apertura: LPF Apertura <ano>
- 2013 Clausura: LPF Clausura <ano>
- 2013 Apertura: LPF Apertura <ano>
- 2014 Clausura: LPF Clausura <ano>
- 2014 Apertura: LPF Apertura <ano>
- 2015 Clausura: LPF Clausura <ano>
- 2015 Apertura: LPF Apertura <ano>
- 2016 Clausura: LPF Clausura <ano>
- 2016 Apertura: LPF Apertura <ano>
- 2017 Clausura: LPF Clausura <ano>
- 2017 Apertura: LPF Apertura <ano>
- 2018 Clausura: LPF Clausura <ano>
- 2018 Apertura: LPF Apertura <ano>
- 2019 Clausura: LPF Clausura <ano>
- 2019 Apertura a 2020 Apertura: LPF Apertura <ano>
- 2020 Clausura: LPF Clausura <ano>
- 2021 Apertura: LPF Apertura <ano>
- 2021 Clausura: LPF Clausura <ano>
- 2022 Apertura: LPF Apertura <ano>
- 2022 Clausura: LPF Clausura <ano>
- 2023 Apertura: LPF Apertura <ano>
- 2023 Clausura: LPF Clausura <ano>
- 2024 Apertura: LPF Apertura <ano>
- 2024 Clausura: LPF Clausura <ano>
- 2025 Apertura: LPF Apertura <ano>
- 2025 Clausura a 2026 Clausura: LPF Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1988 a 1994/95: sem jogos (só a tabela final)
- 1994/95 LINFUNA: mata-mata
- 1995/96: sem jogos (só a tabela final)
- 1995/96 LINFUNA: mata-mata
- 1996/97: jogos incompletos; pontos corridos + mata-mata
- 1997/98 a 1998/99: pontos corridos + mata-mata
- 1999/00: sem jogos (só a tabela final)
- 2000/01: pontos corridos + mata-mata
- 2001 Apertura a 2001 Clausura: sem jogos (só a tabela final)
- 2002 Apertura a 2010 Clausura: pontos corridos + mata-mata
- 2010 Apertura a 2012 Clausura: sem jogos (só a tabela final)
- 2012 Apertura a 2019 Apertura: pontos corridos + mata-mata
- 2020 Apertura: pontos corridos
- 2020 Clausura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1996/97: Primeira fase (liga); Fase final (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1997/98: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1998/99: Primeira fase (liga); Segunda fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000/01: Primeira fase (liga); Fase final (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2004 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2004 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2005 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2006 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2006 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2007 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2007 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2008 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2008 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2009 Apertura ANAPROF: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2009 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2010 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2012 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2013 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2014 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2014 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2015 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2015 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2016 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2016 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2017 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2017 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2018 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2018 Apertura: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2019 Clausura: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2019 Apertura: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2020 Clausura: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2021 Apertura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2021 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2022 Apertura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2022 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2023 Apertura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2023 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2024 Apertura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2024 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2025 Apertura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2025 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2026 Clausura: Primeira fase (liga); Fase preliminar (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 53 edições
- lista de campeões da RSSSF: 10 edições
- calculada: 3 edições

**Observações das edições:**

- 1988: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1989: sem página da RSSSF: só o campeão e o vice
- 1990: sem página da RSSSF: só o campeão e o vice
- 1991: sem página da RSSSF: só o campeão e o vice
- 1992: sem página da RSSSF: só o campeão e o vice
- 1993: sem página da RSSSF: só o campeão e o vice
- 1994/95: sem página da RSSSF: só o campeão e o vice
- 1994/95 LINFUNA: liga paralela da LINFUNA (racha de 1994-96, reconhecida pela FIFA na época): só a final
- 1995/96: sem página da RSSSF: só o campeão e o vice
- 1995/96 LINFUNA: liga paralela da LINFUNA (racha de 1994-96, reconhecida pela FIFA na época): só a final
- 1996/97: jogos incompletos: a página não tem as rodadas 5 a 7 da primeira fase (100 dos 132 jogos)
- 1999/00: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2001 Apertura: sem página da RSSSF: só o campeão e o vice
- 2001 Clausura: sem página da RSSSF: só o campeão e o vice
- 2010 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2012 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2020 Apertura: torneio abandonado em 17/03/2020 pela pandemia de covid-19, sem título; a classificação é a tabela do momento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Tauro: 17
- Árabe Unido: 15
- Plaza Amador: 10
- San Francisco: 9
- CAI La Chorrera: 7
- CD Universitario: 3
- Euro Kickers: 1
- Panamá Viejo: 1
- Sporting San Miguelito: 1
- Alianza de Panamá: 1
- Sem campeão: 2020 Apertura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1988 | Plaza Amador | San Francisco |
| 1989 | Tauro | San Francisco |
| 1990 | Plaza Amador | Tauro |
| 1991 | Tauro | Euro Kickers |
| 1992 | Plaza Amador | Sporting Colón |
| 1993 | Euro Kickers | Projusa |
| 1994/95 | San Francisco | Tauro |
| 1994/95 LINFUNA | Árabe Unido | Projusa |
| 1995/96 | San Francisco | Plaza Amador |
| 1995/96 LINFUNA | Árabe Unido | Cosmos |
| 1996/97 | Tauro | Euro Kickers |
| 1997/98 | Tauro | Árabe Unido |
| 1998/99 | Árabe Unido | Tauro |
| 1999/00 | Tauro | Plaza Amador |
| 2000/01 | Panamá Viejo | Tauro |
| 2001 Apertura | Árabe Unido | San Francisco |
| 2001 Clausura | Árabe Unido | Plaza Amador |
| 2002 Apertura | Árabe Unido | San Francisco |
| 2002 Clausura | Plaza Amador | Tauro |
| 2003 Apertura | Tauro | Árabe Unido |
| 2003 Clausura | Tauro | Alianza de Panamá |
| 2004 Apertura | Árabe Unido | Plaza Amador |
| 2004 Clausura | Árabe Unido | San Francisco |
| 2005 Apertura | Plaza Amador | Árabe Unido |
| 2005 Clausura | San Francisco | Atlético Veragüense |
| 2006 Apertura | San Francisco | Plaza Amador |
| 2006 Clausura | Tauro | Árabe Unido |
| 2007 Apertura | Tauro | San Francisco |
| 2007 Clausura | San Francisco | Árabe Unido |
| 2008 Apertura | San Francisco | Tauro |
| 2008 Clausura | Árabe Unido | Tauro |
| 2009 Apertura ANAPROF | San Francisco | CD Universitario |
| 2009 Apertura | Árabe Unido | Tauro |
| 2010 Clausura | Árabe Unido | San Francisco |
| 2010 Apertura | Tauro | San Francisco |
| 2011 Clausura | San Francisco | CD Universitario |
| 2011 Apertura | CD Universitario | Plaza Amador |
| 2012 Clausura | Tauro | Chepo |
| 2012 Apertura | Árabe Unido | Chepo |
| 2013 Clausura | Sporting San Miguelito | San Francisco |
| 2013 Apertura | Tauro | San Francisco |
| 2014 Clausura | CD Universitario | Río Abajo |
| 2014 Apertura | San Francisco | Sporting San Miguelito |
| 2015 Clausura | Árabe Unido | CAI La Chorrera |
| 2015 Apertura | Árabe Unido | CD Universitario |
| 2016 Clausura | Plaza Amador | CD Universitario |
| 2016 Apertura | Árabe Unido | Plaza Amador |
| 2017 Clausura | Tauro | Árabe Unido |
| 2017 Apertura | CD Universitario | Árabe Unido |
| 2018 Clausura | CAI La Chorrera | Tauro |
| 2018 Apertura | Tauro | Costa del Este |
| 2019 Clausura | CAI La Chorrera | San Francisco |
| 2019 Apertura | Tauro | Costa del Este |
| 2020 Apertura | — | — |
| 2020 Clausura | CAI La Chorrera | San Francisco |
| 2021 Apertura | Plaza Amador | CD Universitario |
| 2021 Clausura | Tauro | Herrera FC |
| 2022 Apertura | Alianza de Panamá | Sporting San Miguelito |
| 2022 Clausura | CAI La Chorrera | CD Universitario |
| 2023 Apertura | CAI La Chorrera | Tauro |
| 2023 Clausura | CAI La Chorrera | Tauro |
| 2024 Apertura | Tauro | Plaza Amador |
| 2024 Clausura | CAI La Chorrera | Plaza Amador |
| 2025 Apertura | Plaza Amador | San Francisco |
| 2025 Clausura | Plaza Amador | Alianza de Panamá |
| 2026 Clausura | Plaza Amador | Alianza de Panamá |

**Rebaixados marcados na classificação:** 2 em 2 edições (só onde a tabela publicada marca a queda); quem mais caiu: Atlético Municipal Colón (1), Euro Kickers (1).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 2002 Apertura: San Francisco -2
- 2019 Apertura: San Francisco -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/pan-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **panama97 · 242:** «San Francisco, Euro 5-4 on pen» → «San Francisco  [Eurokickers 5-4 pen]»: os pênaltis vinham colados ao nome do visitante; viram nota (o leitor lia "San Francisco, Euro 5-4 on pen" como clube)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 3)

- **1997/98:** dois jogos da primeira fase estão na página só com o resultado, sem placar ("Pan A ppd Nacional [away win]" e "Ejecutivo - Chiriqui [draw]"): ficam fora; a tabela publicada os conta (Atlético Nacional, Chiriquí, Pan de Azúcar e Ejecutivo com um jogo a menos nos jogos lidos)
- **2004 Apertura:** Tauro: os jogos da página somam 26-12, a tabela publicada diz 25-11 (um placar com um gol a mais de cada lado; fica como a página)
- **2008 Apertura:** San Francisco e Plaza Amador: os jogos da página dão ao San Francisco um empate a menos e uma derrota a mais, e ao Plaza Amador o contrário, do que a tabela publicada (com os mesmos gols); fica como a página

### Identidade dos clubes

Regras em `coleta/pan-1/clubes_pan.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão do Panamá: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 25/11/2026:
- nome pelo qual o clube é conhecido (Tauro, Plaza Amador, Árabe Unido, San Francisco, CAI La Chorrera), com as grafias e
  abreviações das páginas ("Arabe", "P Amador", "S Francisco", "Sporting SM", "C.A.I");
- o mesmo clube com outro nome (a lista de campeões da RSSSF diz): Deportivo La Previsora = San Francisco FC; Chorrillo FC /
  El Chorrillo / Municipal Chorrillo = CD Universitario (o nome desde 2018); Sporting '89 / Sporting SM = Sporting San
  Miguelito; River Plate FC = Colón River (renomeado em 2004); Projusa / Los Bravos del Projusa; Deportivo del Este = Potros
  del Este; Veraguas CD = Veraguas United;
- clubes diferentes: Chiriquí FC (até 2001) e Atlético Chiriquí (2002 em diante); Atlético Nacional (anos 1990) e SD Atlético
  Nacional (2015 em diante); Atlético Veragüense e Veraguas United; Sporting Colón, Sporting Coclé e Sporting San Miguelito;
- homônimo de clube do banco ou de outro pacote leva o país: Alianza de Panamá, Atlético Nacional de Panamá, SD Atlético
  Nacional de Panamá (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (15):** de 1988 a 1995/96 (sem página, ou só a classificação), 1999/00, 2001 (sem página) e de 2010 Apertura a 2012 Clausura (só as tabelas). 1996/97 entra incompleta (faltam as rodadas 5 a 7). O vice é o da lista de campeões.
- **Edições sem jogos** (15): 1988, 1989, 1990, 1991, 1992, 1993, 1994/95, 1995/96, 1999/00, 2001 Apertura, 2001 Clausura, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1988 a 1995/96 e 2001 sem jogos: a RSSSF não tem página de 1989 a 1993, da ANAPROF de 1994/95 e 1995/96 nem dos dois torneios de 2001 (só o campeão e o vice da lista). Fonte que resolveria: La Prensa / Crítica da época ou a LPF.
- 1999/00 e Apertura 2010 a Clausura 2012 só com as tabelas; 1996/97 incompleta (faltam as rodadas 5 a 7).
- A ESPN não cobre o Panamá: sem hora, estádio nem cartões.
- Antes de 1988 fora (ligas da capital e de Colón; campeões nacionais de 1952 a 1987 desconhecidos).
- Divergências de um jogo ou um gol da própria página em 1997/98, 2004 Apertura e 2008 Apertura (explicadas no relatório).

## 10. Arquivos e comandos

Código em `coleta/pan-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `clubes_pan.py` | Identidade dos clubes da 1ª divisão do Panamá: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão do Panamá (pan-1): a ANAPROF (1988-2009) e a Liga Panameña de Fútbol (LPF, 2009 em diante), uma |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão do Panamá, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão do Panamá e grava o pacote em data/coleta/pan-1/pacote/ e o relatório em docs/coleta/pan-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão do Panamá nas páginas da RSSSF (data/coleta/pan-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado no Panamá). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/pan-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/pan-1/pacote/`; relatório: `docs/coleta/pan-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/pan-1/importar.py
python coleta/pan-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py pan-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

