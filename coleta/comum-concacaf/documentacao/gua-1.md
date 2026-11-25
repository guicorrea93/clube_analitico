# Campeonato Guatemalteco (`gua-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/gua-1/pacote/`, do código `coleta/gua-1/` e do relatório `docs/coleta/gua-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 101, de 1942/43 a 2026 Clausura; 48 sem jogos.
- **Jogos:** 6836 (6833 com placar); **gols:** 17562; **gols com autor:** 2991 (17%); **cartões:** 0.
- **Clubes:** 73; **artilheiros:** 1 edições com artilheiro (1 linhas, com empates).
- **Classificação final:** 101 edições; **tabelas publicadas guardadas para conferência:** 1383 linhas.
- **No banco:** sim; **último commit do pacote:** 85c4da52.
- **Observação da competição:** Liga Nacional da Guatemala de 1942/43 ao Clausura 2026, uma edição por título, como a contagem oficial e a lista da RSSSF: um campeão por temporada até 1998/99, Apertura e Clausura de 1999/00 em diante (2001: Reordenamiento; Clausura 2020 sem campeão). Até 1995/96 só as tabelas. A Liga Capitalina (1919-1941) fica fora.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão da Guatemala (gua-1): o Campeonato de Liga (Liga Nacional), uma edição por título, como na lista de
campeões da RSSSF (tablesg/guatchamp.html, 100 títulos desde 1942) e na contagem oficial. Escopo decidido em 24/11/2026: a
Liga Capitalina / Liga Mayor (1919-1941, liga da capital) fica fora.

- 1942/43 a 1998/99: um campeão por temporada (rótulos da RSSSF: "1942/43", "1943", "1970/71", "1971"...); os anos sem
  campeonato não têm edição.
- 1999/00 em diante: Apertura e Clausura, uma edição cada ("1999 Apertura", "2000 Clausura"); em 2001/02 o primeiro torneio
  foi o Campeonato de Reordenamiento ("2001 Reordenamiento"). O Clausura 2020 (pandemia) entra sem campeão.

Cada página da RSSSF tem a temporada no título ("Guatemala 1970/71"); os nomes dos arquivos são irregulares (guat71a.html é
1970/71), e o casamento é pelo título. Até 1995/96 as páginas trazem quase só as tabelas: a edição entra só com elas quando
a página tem menos de 90% dos jogos.
```

**Edições:** 101, uma por título, como a lista de campeões da RSSSF (`guatchamp.html`, 100 títulos desde 1942) e a contagem oficial (Municipal 33, Comunicaciones 32). Escopo decidido em 24/11/2026: só o Campeonato de Liga (Liga Nacional), de 1942/43 em diante; a Liga Capitalina / Liga Mayor (1919-1941, liga da capital) fica fora. Um campeão por temporada até 1998/99 (os anos sem campeonato não têm edição); Apertura e Clausura de 1999/00 em diante, uma edição cada (em 2001 o primeiro torneio foi o Reordenamiento); o Clausura 2020 (pandemia) entra sem campeão.

**Fontes:** RSSSF (`data/coleta/gua-1/rsssf/`; os arquivos têm nomes irregulares e o casamento com a temporada é pelo título da página) e ESPN (liga `gua.1`).

**Clubes:** nomes e identidades no começo de `coleta/gua-1/clubes_gua.py`. Homônimos de clubes de outros países levam o país: Aurora de Guatemala, Hércules de Guatemala, Racing de Guatemala, España de Guatemala, América de Guatemala, Eureka de Guatemala.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 48.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 1996/97, 1999 Apertura, 2000 Apertura.
- **Edições sem tabela para conferir** (50): 1942/43, 1943, 1944/45, 1947, 1950/51, 1952/53, 1954/55, 1956, 1957/58, 1959/60, 1961/62, 1963/64, 1964, 1965/66, 1966, 1967/68, 1968/69, 1969/70, 1970/71, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979/80, 1980, 1981, 1982, 1983, 1984, 1985/86, 1986, 1987, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 2009 Clausura, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura, 2020 Clausura.
- **Edições com menos jogos que o esperado:** 1999 Apertura (145 de 146), 2001 Clausura (147 de 146), 2015 Clausura (143 de 142).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1940s | 4 | 0 | — | — | — | — | — | — | — | — |
| 1950s | 6 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 8 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 691 | 91% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 20 | 2227 | 100% | 31% | 100% | 23% | 3% | 0% | 24% | 0.0 |
| 2010s | 20 | 2289 | 100% | 93% | 100% | 69% | 32% | 0% | 27% | 0.0 |
| 2020s | 13 | 1629 | 100% | 99% | 100% | 99% | 99% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1942/43: 7 clubes
- 1943: 6 clubes
- 1944/45: 7 clubes
- 1947 a 1952/53: 8 clubes
- 1954/55 a 1957/58: 10 clubes
- 1959/60: 15 clubes
- 1961/62: 24 clubes
- 1963/64 a 1964: 12 clubes
- 1965/66: 14 clubes
- 1966 a 1968/69: 10 clubes
- 1969/70: 12 clubes
- 1970/71: 14 clubes
- 1971: 12 clubes
- 1972 a 1974: 10 clubes
- 1975: 12 clubes
- 1976: 14 clubes
- 1977: 16 clubes
- 1978: 19 clubes
- 1979/80 a 1987: 12 clubes
- 1988/89: 13 clubes
- 1989/90 a 1993/94: 12 clubes
- 1994/95: 11 clubes
- 1995/96: 12 clubes
- 1996/97: 13 clubes
- 1997/98: 12 clubes
- 1998/99: 15 clubes
- 1999 Apertura a 2001 Reordenamiento: 12 clubes
- 2002 Clausura a 2009 Clausura: 10 clubes
- 2009 Apertura a 2024 Apertura: 12 clubes
- 2025 Clausura: 11 clubes
- 2025 Apertura a 2026 Clausura: 12 clubes

**Pontos por vitória:**

- 1942/43 a 1994/95: 2
- 1995/96 a 2026 Clausura: 3

**Nome oficial:**

- 1942/43 a 1998/99: Liga Nacional de Guatemala <ano>
- 1999 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2000 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2000 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2001 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2001 Reordenamiento: Liga Nacional de Guatemala Reordenamiento <ano>
- 2002 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2002 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2003 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2003 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2004 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2004 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2005 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2005 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2006 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2006 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2007 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2007 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2008 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2008 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2009 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2009 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2010 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2010 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2011 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2011 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2012 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2012 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2013 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2013 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2014 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2014 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2015 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2015 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2016 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2016 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2017 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2017 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2018 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2018 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2019 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2019 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2020 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2020 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2021 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2021 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2022 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2022 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2023 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2023 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2024 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2024 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2025 Clausura: Liga Nacional de Guatemala Clausura <ano>
- 2025 Apertura: Liga Nacional de Guatemala Apertura <ano>
- 2026 Clausura: Liga Nacional de Guatemala Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1942/43 a 1995/96: sem jogos (só a tabela final)
- 1996/97 a 2010 Clausura: pontos corridos + mata-mata
- 2010 Apertura a 2012 Clausura: sem jogos (só a tabela final)
- 2012 Apertura a 2019 Apertura: pontos corridos + mata-mata
- 2020 Clausura: pontos corridos
- 2020 Apertura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1996/97: Primeira fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1997/98: Primeira fase (liga); Final (mata_mata, ida_volta)
- 1998/99: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga); Semifinal (mata_mata, jogo_unico)
- 1999 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Reordenamiento: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
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
- 2019 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2026 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 99 edições
- calculada: 2 edições

**Observações das edições:**

- 1942/43: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1943: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1944/45: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1947: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1950/51: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1952/53: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1954/55: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1956: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1957/58: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1959/60: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1961/62: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1963/64: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1964: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1965/66: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1966: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1967/68: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1968/69: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1969/70: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1970/71: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1971: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1972: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1973: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1974: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1975: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1976: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1977: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1978: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1979/80: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1980: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1981: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1982: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1983: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1984: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1985/86: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1986: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1987: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1988/89: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1989/90: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1990/91: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1991/92: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1992/93: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1993/94: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1994/95: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 1995/96: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2010 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2011 Apertura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2012 Clausura: só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)
- 2020 Clausura: torneio abandonado pela pandemia de covid-19, sem título; a classificação é a tabela do momento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Municipal: 33
- Comunicaciones: 32
- Aurora de Guatemala: 8
- Xelajú MC: 7
- Antigua GFC: 6
- Tipografía Nacional: 3
- Guastatoya: 3
- Suchitepéquez: 2
- Cobán Imperial: 2
- Jalapa: 2
- Santa Lucía Cotzumalguapa: 1
- Malacateco: 1
- Sem campeão: 2020 Clausura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1942/43 | Municipal | Tipografía Nacional |
| 1943 | Tipografía Nacional | Municipal |
| 1944/45 | Tipografía Nacional | Municipal |
| 1947 | Municipal | España de Guatemala |
| 1950/51 | Municipal | Comunicaciones |
| 1952/53 | Tipografía Nacional | Comunicaciones |
| 1954/55 | Municipal | Comunicaciones |
| 1956 | Comunicaciones | USAC |
| 1957/58 | Comunicaciones | Aurora de Guatemala |
| 1959/60 | Comunicaciones | Municipal |
| 1961/62 | Xelajú MC | Comunicaciones |
| 1963/64 | Municipal | Xelajú MC |
| 1964 | Aurora de Guatemala | Municipal |
| 1965/66 | Municipal | Comunicaciones |
| 1966 | Aurora de Guatemala | Xelajú MC |
| 1967/68 | Aurora de Guatemala | Municipal |
| 1968/69 | Comunicaciones | Aurora de Guatemala |
| 1969/70 | Municipal | Comunicaciones |
| 1970/71 | Comunicaciones | Aurora de Guatemala |
| 1971 | Comunicaciones | Aurora de Guatemala |
| 1972 | Comunicaciones | Municipal |
| 1973 | Municipal | Aurora de Guatemala |
| 1974 | Municipal | Aurora de Guatemala |
| 1975 | Aurora de Guatemala | Municipal |
| 1976 | Municipal | Comunicaciones |
| 1977 | Comunicaciones | Xelajú MC |
| 1978 | Aurora de Guatemala | Comunicaciones |
| 1979/80 | Comunicaciones | Juventud Retalteca |
| 1980 | Xelajú MC | Galcasa |
| 1981 | Comunicaciones | Cobán Imperial |
| 1982 | Comunicaciones | Suchitepéquez |
| 1983 | Suchitepéquez | Comunicaciones |
| 1984 | Aurora de Guatemala | Suchitepéquez |
| 1985/86 | Comunicaciones | Aurora de Guatemala |
| 1986 | Aurora de Guatemala | Galcasa |
| 1987 | Municipal | Aurora de Guatemala |
| 1988/89 | Municipal | Aurora de Guatemala |
| 1989/90 | Municipal | Galcasa |
| 1990/91 | Comunicaciones | Juventud Retalteca |
| 1991/92 | Municipal | Comunicaciones |
| 1992/93 | Aurora de Guatemala | Suchitepéquez |
| 1993/94 | Municipal | Sacachispas |
| 1994/95 | Comunicaciones | Municipal |
| 1995/96 | Xelajú MC | Comunicaciones |
| 1996/97 | Comunicaciones | Aurora de Guatemala |
| 1997/98 | Comunicaciones | Cobán Imperial |
| 1998/99 | Comunicaciones | Aurora de Guatemala |
| 1999 Apertura | Comunicaciones | Municipal |
| 2000 Clausura | Municipal | Comunicaciones |
| 2000 Apertura | Municipal | Comunicaciones |
| 2001 Clausura | Comunicaciones | Municipal |
| 2001 Reordenamiento | Municipal | Cobán Imperial |
| 2002 Clausura | Municipal | Comunicaciones |
| 2002 Apertura | Comunicaciones | Municipal |
| 2003 Clausura | Comunicaciones | Cobán Imperial |
| 2003 Apertura | Municipal | Comunicaciones |
| 2004 Clausura | Cobán Imperial | Municipal |
| 2004 Apertura | Municipal | Comunicaciones |
| 2005 Clausura | Municipal | Suchitepéquez |
| 2005 Apertura | Municipal | Comunicaciones |
| 2006 Clausura | Municipal | Marquense |
| 2006 Apertura | Municipal | Comunicaciones |
| 2007 Clausura | Xelajú MC | Municipal |
| 2007 Apertura | Jalapa | Municipal |
| 2008 Clausura | Municipal | Comunicaciones |
| 2008 Apertura | Comunicaciones | Municipal |
| 2009 Clausura | Jalapa | Municipal |
| 2009 Apertura | Municipal | Xelajú MC |
| 2010 Clausura | Municipal | Comunicaciones |
| 2010 Apertura | Comunicaciones | Municipal |
| 2011 Clausura | Comunicaciones | Municipal |
| 2011 Apertura | Municipal | Suchitepéquez |
| 2012 Clausura | Xelajú MC | Comunicaciones |
| 2012 Apertura | Comunicaciones | Municipal |
| 2013 Clausura | Comunicaciones | Heredia |
| 2013 Apertura | Comunicaciones | Municipal |
| 2014 Clausura | Comunicaciones | Heredia |
| 2014 Apertura | Comunicaciones | Marquense |
| 2015 Clausura | Comunicaciones | Municipal |
| 2015 Apertura | Antigua GFC | Xelajú MC |
| 2016 Clausura | Suchitepéquez | Municipal |
| 2016 Apertura | Antigua GFC | Municipal |
| 2017 Clausura | Municipal | Petapa |
| 2017 Apertura | Antigua GFC | Petapa |
| 2018 Clausura | Guastatoya | Sanarate |
| 2018 Apertura | Guastatoya | Xelajú MC |
| 2019 Clausura | Antigua GFC | Cobán Imperial |
| 2019 Apertura | Municipal | Cobán Imperial |
| 2020 Clausura | — | — |
| 2020 Apertura | Guastatoya | Municipal |
| 2021 Clausura | Santa Lucía Cotzumalguapa | Comunicaciones |
| 2021 Apertura | Malacateco | Antigua GFC |
| 2022 Clausura | Comunicaciones | Municipal |
| 2022 Apertura | Cobán Imperial | Antigua GFC |
| 2023 Clausura | Xelajú MC | Comunicaciones |
| 2023 Apertura | Comunicaciones | Achuapa |
| 2024 Clausura | Municipal | Antigua GFC |
| 2024 Apertura | Xelajú MC | Municipal |
| 2025 Clausura | Antigua GFC | Municipal |
| 2025 Apertura | Antigua GFC | Municipal |
| 2026 Clausura | Municipal | Xelajú MC |

**Rebaixados marcados na classificação:** 42 em 25 edições (só onde a tabela publicada marca a queda); quem mais caiu: Escuintla (5), Antigua GFC (4), IRCA (2), USAC (2), Zacapa (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1992/93: Galcasa -1
- 1992/93: Amatitlán +1
- 1994/95: Suchitepéquez +8

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/gua-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Tabelas da página que não são da edição (`TABELAS_FORA`, 2)

- **1998/99 · guat99:319:** tabela acumulada (fase regular + grupo do rebaixamento); a página dá parte dos jogos do grupo do rebaixamento só com o resultado ("home win", "draw"), sem placar
- **1998/99 · guat99:380:** a mesma tabela acumulada, repetida no fim (fase regular + grupo do rebaixamento); a página dá parte dos jogos do grupo do rebaixamento só com o resultado ("home win", "draw"), sem placar

### Identidade dos clubes

Regras em `coleta/gua-1/clubes_gua.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão da Guatemala: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Municipal, Comunicaciones, Xelajú MC, Antigua GFC, Cobán Imperial, Suchitepéquez), com
  as grafias de cada época ("Tip Nac", "Xelaju", "Coban", "Communicaciones");
- o mesmo clube com outro nome: Universidad / USAC / Univ. San Carlos = USAC; Deportivo Heredia / Heredia-Jaguares = Heredia;
  Juca / Tally Juca = Tally Juca; Retalteca / Juventud Retalteca; Dep. Carchá / Carchá; Izabal / Izabal JC;
- Halcones La Mesilla (2012-2015) = Peñarol La Mesilla renomeado (a ESPN segue chamando de "Penarol" nesses anos);
- clubes diferentes: Escuintla e Juventud Escuintleca;
- homônimo de clube do banco ou de outro pacote leva o país: Hércules de Guatemala, Racing de Guatemala, España de
  Guatemala, América de Guatemala, Aurora de Guatemala, Eureka de Guatemala (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos (48):** de 1942/43 a 1995/96 (a RSSSF quase só tem as tabelas) e do Apertura 2010 ao Clausura 2012 (a página só tem as tabelas e a fase final). A lista de campeões não traz o vice: o vice é o 2º da classificação.
- **Edições sem jogos** (48): 1942/43, 1943, 1944/45, 1947, 1950/51, 1952/53, 1954/55, 1956, 1957/58, 1959/60, 1961/62, 1963/64, 1964, 1965/66, 1966, 1967/68, 1968/69, 1969/70, 1970/71, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979/80, 1980, 1981, 1982, 1983, 1984, 1985/86, 1986, 1987, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 2010 Apertura, 2011 Clausura, 2011 Apertura, 2012 Clausura.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1942/43 a 1995/96 só com as tabelas (a RSSSF quase não tem os jogos). Fonte que resolveria: jornais da época (Prensa Libre, El Imparcial) ou a Liga Nacional.
- Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular).
- A lista de campeões não traz o vice: o vice é o 2º da classificação (conferir com outra fonte).
- 1998/99: parte dos jogos do grupo do rebaixamento só com o resultado (sem placar).

## 10. Arquivos e comandos

Código em `coleta/gua-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga gua.1) de 2004 a 2026 para data/coleta/gua-1/espn/gua1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão da Guatemala para data/coleta/gua-1/rsssf/: a lista de campeões (guatchamp.html), as |
| `clubes_gua.py` | Identidade dos clubes da 1ª divisão da Guatemala: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão da Guatemala (gua-1): o Campeonato de Liga (Liga Nacional), uma edição por título, como na lista de |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão da Guatemala, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão da Guatemala e grava o pacote em data/coleta/gua-1/pacote/ e o relatório em docs/coleta/gua-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão da Guatemala nas páginas da RSSSF (data/coleta/gua-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol não é usado na Guatemala). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/gua-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/gua-1/pacote/`; relatório: `docs/coleta/gua-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/gua-1/baixar_espn.py
python coleta/gua-1/baixar_rsssf.py
python coleta/gua-1/importar.py
python coleta/gua-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py gua-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

