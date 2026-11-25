# Campeonato Hondurenho (`hon-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/hon-1/pacote/`, do código `coleta/hon-1/` e do relatório `docs/coleta/hon-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 89, de 1965/66 a 2026 Clausura; 35 sem jogos.
- **Jogos:** 5391 (5385 com placar); **gols:** 13983; **gols com autor:** 2529 (18%); **cartões:** 0.
- **Clubes:** 55; **artilheiros:** 1 edições com artilheiro (1 linhas, com empates).
- **Classificação final:** 89 edições; **tabelas publicadas guardadas para conferência:** 992 linhas.
- **No banco:** sim; **último commit do pacote:** 6e59e93f.
- **Observação da competição:** Liga Nacional de Honduras de 1965/66 ao Clausura 2026, uma edição por título, como a lista de campeões da RSSSF: um campeão por temporada até 1996/97 (1972/73 abandonada, sem campeão), Apertura e Clausura de 1997/98 em diante (1999, torneio único; Clausura 2020 sem campeão). Até 1995/96 só as tabelas. A Liga Amateur de 1947-1964 fica fora (não é reconhecida pela liga).

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão de Honduras (hon-1): a Liga Nacional, uma edição por título, como na lista de campeões da RSSSF
(tablesh/hondchamp.html). Escopo decidido em 24/11/2026 (pesquisa a pedido do Guilherme):

- 1965/66 a 1996/97, um campeão por temporada (rótulos da RSSSF: "1965/66", "1973", "1978/79"...). 1972/73 foi abandonada:
  entra sem campeão, com a tabela do momento.
- 1997/98: Apertura e Clausura ("1997 Apertura", "1998 Clausura"); 1999: torneio único de transição ("1999"); de 1999/00 em
  diante, Apertura e Clausura ("1999 Apertura", "2000 Clausura"), até o Clausura 2026. O Clausura 2020 (pandemia) entra sem
  campeão.
- Fora: a Liga Amateur de Honduras (1947-1964): mata-mata entre campeões regionais, listado à parte pela RSSSF e sem
  reconhecimento da liga e da FENAFUTH.

Fontes por edição: até 1994/95, as tabelas finais de hondhist.html (as poucas páginas por temporada dessa época trazem só
parte dos jogos); de 1995/96 em diante, a página da temporada (hondAA.html; hondAAAA.html de 2010 em diante), só pelas
tabelas quando a página tem menos de 90% dos jogos.
```

**Edições:** 89, uma por título, como a lista de campeões da RSSSF (`hondchamp.html`, 87 títulos da Liga Nacional). Escopo decidido em 24/11/2026, depois de pesquisa a pedido do Guilherme: só a Liga Nacional, de 1965/66 em diante, como a liga conta. Um campeão por temporada até 1996/97 (1972/73 foi abandonada e entra sem campeão); Apertura e Clausura de 1997/98 em diante, uma edição cada, com o torneio único de 1999; o Clausura 2020 (pandemia) entra sem campeão. A Liga Amateur de Honduras (1947-1964) fica fora: era um mata-mata entre campeões regionais, a RSSSF a lista à parte e a liga e a FENAFUTH não reconhecem esses títulos.

**Fontes:** RSSSF (`data/coleta/hon-1/rsssf/`) e ESPN (liga `hon.1`: hora, estádio, público, gols com minuto e cartões, casados com os jogos da RSSSF).

**Clubes:** nomes e identidades no começo de `coleta/hon-1/clubes_hon.py` (La Salle = San Pedro; Honduras = Honduras Progreso; Atlético Olanchano e Olancho FC separados). Homônimos de clubes de outros países levam a cidade ou o país: Olimpia de Tegucigalpa, Necaxa de Tegucigalpa, Real Sociedad de Tocoa, Palestino de Honduras, Independiente de Honduras, Progreso de Honduras, Atlético Español de Honduras, Platense de Puerto Cortés, San Pedro de Honduras, Atlántida de La Ceiba.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 47.
- **Edições com alguma tabela divergente** (5; motivo no relatório, na edição): 1997 Apertura, 2002 Clausura, 2002 Apertura, 2005 Apertura, 2007 Clausura.
- **Edições sem tabela para conferir** (37): 1965/66, 1966/67, 1967/68, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973, 1974, 1975, 1976, 1977, 1978/79, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1998 Clausura, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura, 2020 Clausura.
- **Edições com menos jogos que o esperado:** 2002 Apertura (97 de 96), 2007 Clausura (97 de 94), 2009 Clausura (96 de 95).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 5 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 11 | 599 | 99% | 0% | 99% | 0% | 0% | 0% | 1% | 0.0 |
| 2000s | 20 | 1918 | 99% | 31% | 99% | 24% | 1% | 0% | 27% | 0.0 |
| 2010s | 20 | 1596 | 100% | 93% | 100% | 74% | 31% | 0% | 28% | 0.0 |
| 2020s | 13 | 1278 | 100% | 98% | 100% | 97% | 97% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1965/66 a 1980: 10 clubes
- 1981: 11 clubes
- 1982 a 1996/97: 10 clubes
- 1997 Apertura a 1998 Clausura: 11 clubes
- 1999 a 2003 Apertura: 10 clubes
- 2004 Clausura: 9 clubes
- 2004 Apertura a 2025 Clausura: 10 clubes
- 2025 Apertura a 2026 Clausura: 11 clubes

**Pontos por vitória:**

- 1965/66 a 1993/94: 2
- 1994/95 a 2026 Clausura: 3

**Nome oficial:**

- 1965/66 a 1996/97: Liga Nacional de Fútbol de Honduras <ano>
- 1997 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 1998 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 1999: Liga Nacional de Fútbol de Honduras <ano>
- 1999 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2000 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2000 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2001 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2001 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2002 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2002 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2003 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2003 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2004 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2004 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2005 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2005 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2006 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2006 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2007 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2007 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2008 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2008 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2009 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2009 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2010 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2010 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2011 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2011 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2012 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2012 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2013 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2013 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2014 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2014 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2015 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2015 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2016 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2016 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2017 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2017 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2018 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2018 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2019 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2019 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2020 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2020 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2021 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2021 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2022 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2022 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2023 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2023 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2024 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2024 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2025 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>
- 2025 Apertura: Liga Nacional de Fútbol de Honduras Apertura <ano>
- 2026 Clausura: Liga Nacional de Fútbol de Honduras Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1965/66 a 1995/96: sem jogos (só a tabela final)
- 1996/97: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1997 Apertura a 2010 Clausura: pontos corridos + mata-mata
- 2010 Apertura a 2012 Clausura: sem jogos (só a tabela final)
- 2012 Apertura a 2019 Clausura: pontos corridos + mata-mata
- 2019 Apertura a 2020 Clausura: pontos corridos
- 2020 Apertura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1996/97: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Fase final (liga); Final (mata_mata, ida_volta)
- 1997 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1998 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1999: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1999 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Clausura: Primeira fase (liga); Grupo do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Clausura: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2013 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2013 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2014 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2014 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2015 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2015 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2016 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2017 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2018 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2018 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019 Apertura: Primeira fase (liga); Fase final (liga)
- 2020 Apertura: Primeira fase (liga); Repescagem (mata_mata, ida_volta); Final dos grupos (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta); Finalíssima (mata_mata, ida_volta)
- 2021 Clausura: Primeira fase (liga); Repescagem (mata_mata, ida_volta); Final dos grupos (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Apertura: Primeira fase (liga); Triangulares (liga); Final (mata_mata, ida_volta)
- 2026 Clausura: Primeira fase (liga); Triangulares (liga); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 87 edições
- calculada: 2 edições

**Observações das edições:**

- 1965/66: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1966/67: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1967/68: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1968/69: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1969/70: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1970/71: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1971/72: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1972/73: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época; temporada abandonada, sem título; a classificação é a tabela do momento
- 1973: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1974: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1975: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1976: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1977: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1978/79: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1979: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1980: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1981: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1982: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1983: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1984: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1985: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1986: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1987: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1988: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1989/90: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1990/91: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1991/92: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1992/93: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1993/94: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1994/95: só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época
- 1995/96: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2010 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2012 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2020 Clausura: torneio abandonado pela pandemia de covid-19, sem título; a classificação é a tabela do momento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Olimpia de Tegucigalpa: 40
- Motagua: 20
- Real España: 12
- Marathón: 9
- Platense de Puerto Cortés: 2
- Vida: 2
- Victoria: 1
- Honduras Progreso: 1
- Sem campeão: 1972/73, 2020 Clausura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1965/66 | Platense de Puerto Cortés | Olimpia de Tegucigalpa |
| 1966/67 | Olimpia de Tegucigalpa | Marathón |
| 1967/68 | Olimpia de Tegucigalpa | Marathón |
| 1968/69 | Motagua | Olimpia de Tegucigalpa |
| 1969/70 | Olimpia de Tegucigalpa | Motagua |
| 1970/71 | Motagua | Olimpia de Tegucigalpa |
| 1971/72 | Olimpia de Tegucigalpa | Vida |
| 1972/73 | — | — |
| 1973 | Motagua | Marathón |
| 1974 | Real España | Motagua |
| 1975 | Real España | Olimpia de Tegucigalpa |
| 1976 | Real España | Motagua |
| 1977 | Olimpia de Tegucigalpa | Real España |
| 1978/79 | Motagua | Real España |
| 1979 | Marathón | Universidad |
| 1980 | Real España | Marathón |
| 1981 | Vida | Atlético Morazán |
| 1982 | Olimpia de Tegucigalpa | Motagua |
| 1983 | Vida | Universidad |
| 1984 | Olimpia de Tegucigalpa | Vida |
| 1985 | Marathón | Vida |
| 1986 | Olimpia de Tegucigalpa | Real España |
| 1987 | Olimpia de Tegucigalpa | Marathón |
| 1988 | Real España | Olimpia de Tegucigalpa |
| 1989/90 | Olimpia de Tegucigalpa | Real España |
| 1990/91 | Real España | Motagua |
| 1991/92 | Motagua | Real España |
| 1992/93 | Olimpia de Tegucigalpa | Petrotela |
| 1993/94 | Real España | Motagua |
| 1994/95 | Victoria | Olimpia de Tegucigalpa |
| 1995/96 | Olimpia de Tegucigalpa | Real España |
| 1996/97 | Olimpia de Tegucigalpa | Platense de Puerto Cortés |
| 1997 Apertura | Motagua | Real España |
| 1998 Clausura | Motagua | Olimpia de Tegucigalpa |
| 1999 | Olimpia de Tegucigalpa | Real España |
| 1999 Apertura | Motagua | Olimpia de Tegucigalpa |
| 2000 Clausura | Motagua | Olimpia de Tegucigalpa |
| 2000 Apertura | Olimpia de Tegucigalpa | Platense de Puerto Cortés |
| 2001 Clausura | Platense de Puerto Cortés | Olimpia de Tegucigalpa |
| 2001 Apertura | Motagua | Marathón |
| 2002 Clausura | Marathón | Olimpia de Tegucigalpa |
| 2002 Apertura | Olimpia de Tegucigalpa | Platense de Puerto Cortés |
| 2003 Clausura | Marathón | Motagua |
| 2003 Apertura | Real España | Olimpia de Tegucigalpa |
| 2004 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2004 Apertura | Marathón | Olimpia de Tegucigalpa |
| 2005 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2005 Apertura | Olimpia de Tegucigalpa | Marathón |
| 2006 Clausura | Olimpia de Tegucigalpa | Victoria |
| 2006 Apertura | Motagua | Olimpia de Tegucigalpa |
| 2007 Clausura | Real España | Marathón |
| 2007 Apertura | Marathón | Motagua |
| 2008 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2008 Apertura | Marathón | Real España |
| 2009 Clausura | Olimpia de Tegucigalpa | Real España |
| 2009 Apertura | Marathón | Olimpia de Tegucigalpa |
| 2010 Clausura | Olimpia de Tegucigalpa | Motagua |
| 2010 Apertura | Real España | Olimpia de Tegucigalpa |
| 2011 Clausura | Motagua | Olimpia de Tegucigalpa |
| 2011 Apertura | Olimpia de Tegucigalpa | Real España |
| 2012 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2012 Apertura | Olimpia de Tegucigalpa | Victoria |
| 2013 Clausura | Olimpia de Tegucigalpa | Real Sociedad de Tocoa |
| 2013 Apertura | Real España | Real Sociedad de Tocoa |
| 2014 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2014 Apertura | Motagua | Real Sociedad de Tocoa |
| 2015 Clausura | Olimpia de Tegucigalpa | Motagua |
| 2015 Apertura | Honduras Progreso | Motagua |
| 2016 Clausura | Olimpia de Tegucigalpa | Real Sociedad de Tocoa |
| 2016 Apertura | Motagua | Platense de Puerto Cortés |
| 2017 Clausura | Motagua | Honduras Progreso |
| 2017 Apertura | Real España | Motagua |
| 2018 Clausura | Marathón | Motagua |
| 2018 Apertura | Motagua | Olimpia de Tegucigalpa |
| 2019 Clausura | Motagua | Olimpia de Tegucigalpa |
| 2019 Apertura | Olimpia de Tegucigalpa | Marathón |
| 2020 Clausura | — | — |
| 2020 Apertura | Olimpia de Tegucigalpa | Marathón |
| 2021 Clausura | Olimpia de Tegucigalpa | Motagua |
| 2021 Apertura | Olimpia de Tegucigalpa | Real España |
| 2022 Clausura | Motagua | Real España |
| 2022 Apertura | Olimpia de Tegucigalpa | Motagua |
| 2023 Clausura | Olimpia de Tegucigalpa | Olancho FC |
| 2023 Apertura | Olimpia de Tegucigalpa | Motagua |
| 2024 Clausura | Olimpia de Tegucigalpa | Marathón |
| 2024 Apertura | Motagua | Olimpia de Tegucigalpa |
| 2025 Clausura | Olimpia de Tegucigalpa | Real España |
| 2025 Apertura | Olimpia de Tegucigalpa | Marathón |
| 2026 Clausura | Motagua | Marathón |

**Rebaixados marcados na classificação:** 29 em 26 edições (só onde a tabela publicada marca a queda); quem mais caiu: Universidad (3), Troya (2), Atlético Español de Honduras (2), Atlético Indio (2), Sula (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1974: Real España +19
- 1974: Motagua +20
- 1974: Olimpia de Tegucigalpa +23
- 1974: Marathón +15
- 1974: Platense de Puerto Cortés +15
- 1974: Broncos +14
- 1974: Federal +13
- 1974: Vida +17
- 1974: Universidad +14
- 1974: Atlético Indio +11
- 2002 Clausura: Platense de Puerto Cortés -3
- 2008 Apertura: Real España +2
- 2008 Apertura: Deportes Savio -1
- 2010 Clausura: Real Juventud -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/hon-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Identidade dos clubes

Regras em `coleta/hon-1/clubes_hon.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão de Honduras: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Motagua, Marathón, Real España, Platense, Vida, Victoria), com as grafias de cada fonte
  ("Marathon", "Real Espana", "España" nos anos 2000, "Real España (San Pedro Sula)");
- o mesmo clube com outro nome: La Salle (1965/66) = San Pedro (o nome mudou para 1966/67, RSSSF); Honduras (El Progreso) =
  Honduras Progreso; Juventud (2008/09) = Real Juventud; Patepluma = Real Patepluma; Valencia = Municipal Valencia;
  Atlético Olanchano / Olanchano; Dep. Savio / Savio = Deportes Savio; Comayagua = Real Comayagua; UPNFM = Lobos UPNFM;
  Atl. Choloma / Atlético Cholomeño (2011-2013);
- clubes diferentes: Atlético Olanchano (2003-2008) e Olancho FC (2022 em diante); Atlético Choloma (2011-2013) e Choloma
  (2025 em diante); Broncos e Universidad (a página escreve os dois na mesma temporada);
- homônimo de clube do banco ou de outro pacote leva a cidade ou o país: Olimpia de Tegucigalpa, Necaxa de Tegucigalpa, Real
  Sociedad de Tocoa, Palestino de Honduras, Independiente de Honduras, Progreso de Honduras, Atlético Español de Honduras, Platense de Puerto Cortés,
  San Pedro de Honduras, Atlántida de La Ceiba.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (35):** de 1965/66 a 1995/96 (a RSSSF só tem as tabelas finais, `hondhist.html`) e as edições de 2010/11 e 2011/12 em que a página só tem as tabelas e a fase final.
- **Edições sem jogos** (35): 1965/66, 1966/67, 1967/68, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973, 1974, 1975, 1976, 1977, 1978/79, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1965/66 a 1995/96 só com as tabelas finais (hondhist.html): a RSSSF não tem os jogos. Fonte que resolveria: jornais da época (La Prensa, El Heraldo) ou a Liga Nacional.
- Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular).
- Erros de um resultado na própria página em 1997 Apertura, 2002 Apertura, 2002 Clausura, 2005 Apertura e 2007 Clausura: explicados no relatório.
- Liga Amateur de Honduras (1947-1964) fora do hon-1 (decisão de 24/11); se o Guilherme quiser, entra como competição própria.

## 10. Arquivos e comandos

Código em `coleta/hon-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga hon.1) de 2004 a 2026 para data/coleta/hon-1/espn/hon1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão de Honduras para data/coleta/hon-1/rsssf/: a lista de campeões (hondchamp.html), |
| `clubes_hon.py` | Identidade dos clubes da 1ª divisão de Honduras: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão de Honduras (hon-1): a Liga Nacional, uma edição por título, como na lista de campeões da RSSSF |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão de Honduras, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão de Honduras e grava o pacote em data/coleta/hon-1/pacote/ e o relatório em docs/coleta/hon-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão de Honduras nas páginas da RSSSF (data/coleta/hon-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado em Honduras). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/hon-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/hon-1/pacote/`; relatório: `docs/coleta/hon-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/hon-1/baixar_espn.py
python coleta/hon-1/baixar_rsssf.py
python coleta/hon-1/importar.py
python coleta/hon-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py hon-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

