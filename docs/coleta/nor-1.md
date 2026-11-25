# Campeonato Norueguês (1ª divisão) — coleta de dados

Gerado por `python coleta/nor-1/importar.py`. Pacote em `data/coleta/nor-1/pacote/`.

**Edições:** 80, de 1937/38 a 2025: os 79 títulos de liga que a federação reconhece (Norgesserien, Hovedserien, 1. divisjon, Tippeligaen e Eliteserien).

**Total:** 12368 jogos, 38461 gols, 14830 gols com autor, 11950 cartões, 128 clubes.

**Fontes:**
- Wikipédia (en): tabela de cada fase (ordem oficial, punições), matriz de resultados (base dos jogos de 1948/49 a 1960/61, conferência depois), mata-mata da Norgesserien e finais da Hovedserien;
- Wikipédia (no): a matriz do único grupo da Norgesserien que tem os jogos (Distrito V, grupo B);
- ogol (zerozero): base dos jogos desde 1961/62, com data, hora e rodada; calendários em `data/cache/ogol-nor-1/`;
- RSSSF: página de cada temporada desde 1998 (tabela, placares e autores dos gols de 1999 a 2005), lista de campeões e de artilheiros;
- football-data: placar e hora desde 2012;
- ESPN (liga `nor.1`): estádio, público, gols e cartões nas temporadas que ela cobre (30 clubes casados por votação, pela data e pelo placar).

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; na Norgesserien, o mata-mata e depois a posição no grupo; na Hovedserien, a final e depois a posição no grupo). Pontos 2-1-0 até 1986 e 3-1-0 depois; em 1987, o empate ia para os pênaltis (2 pontos ao vencedor, 1 ao perdedor). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (na Norgesserien, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 28 tabelas, saldo em 65, confronto direto em 0).

| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|
| 1937/38 | 74 | 60 | 233 | 0 | 1 / 0 | Fredrikstad | — |
| 1938/39 | 75 | 61 | 233 | 0 | 1 / 0 | Fredrikstad | — |
| 1947/48 | 74 | 60 | 178 | 0 | 0 / 1 | Freidig | — |
| 1948/49 | 16 | 114 | 367 | 0 | 2 / 0 | Fredrikstad | — |
| 1949/50 | 16 | 114 | 332 | 0 | 2 / 0 | Fram Larvik | — |
| 1950/51 | 16 | 114 | 414 | 0 | 2 / 0 | Fredrikstad | — |
| 1951/52 | 16 | 113 | 383 | 0 | 2 / 0 | Fredrikstad | — |
| 1952/53 | 16 | 113 | 401 | 0 | 2 / 0 | Larvik Turn | — |
| 1953/54 | 16 | 113 | 433 | 0 | 2 / 0 | Fredrikstad | — |
| 1954/55 | 16 | 113 | 415 | 0 | 2 / 0 | Larvik Turn | — |
| 1955/56 | 16 | 113 | 428 | 0 | 2 / 0 | Larvik Turn | — |
| 1956/57 | 16 | 113 | 414 | 0 | 2 / 0 | Fredrikstad | — |
| 1957/58 | 16 | 113 | 449 | 0 | 2 / 0 | Viking | — |
| 1958/59 | 16 | 114 | 412 | 0 | 2 / 0 | Lillestrøm | — |
| 1959/60 | 16 | 113 | 399 | 0 | 2 / 0 | Fredrikstad | — |
| 1960/61 | 16 | 113 | 423 | 0 | 2 / 0 | Fredrikstad | — |
| 1961/62 | 16 | 240 | 938 | 0 | 1 / 0 | Brann | — |
| 1963 | 10 | 90 | 336 | 0 | 1 / 0 | Brann | — |
| 1964 | 10 | 90 | 257 | 0 | 1 / 0 | Lyn | — |
| 1965 | 10 | 90 | 307 | 0 | 1 / 0 | Vålerenga | — |
| 1966 | 10 | 90 | 268 | 0 | 1 / 0 | Skeid | — |
| 1967 | 10 | 90 | 284 | 0 | 1 / 0 | Rosenborg | — |
| 1968 | 10 | 90 | 320 | 0 | 1 / 0 | Lyn | — |
| 1969 | 10 | 90 | 252 | 0 | 1 / 0 | Rosenborg | — |
| 1970 | 10 | 90 | 210 | 0 | 1 / 0 | Strømsgodset | — |
| 1971 | 10 | 90 | 252 | 0 | 0 / 1 | Rosenborg | — |
| 1972 | 12 | 132 | 306 | 0 | 1 / 0 | Viking | — |
| 1973 | 12 | 132 | 306 | 0 | 1 / 0 | Viking | — |
| 1974 | 12 | 132 | 371 | 0 | 1 / 0 | Viking | — |
| 1975 | 12 | 132 | 336 | 0 | 1 / 0 | Viking | — |
| 1976 | 12 | 132 | 362 | 0 | 1 / 0 | Lillestrøm | — |
| 1977 | 12 | 132 | 396 | 0 | 1 / 0 | Lillestrøm | — |
| 1978 | 12 | 132 | 433 | 0 | 1 / 0 | Start | — |
| 1979 | 12 | 132 | 352 | 0 | 1 / 0 | Viking | — |
| 1980 | 12 | 132 | 392 | 0 | 1 / 0 | Start | — |
| 1981 | 12 | 132 | 367 | 0 | 1 / 0 | Vålerenga | — |
| 1982 | 12 | 132 | 355 | 0 | 1 / 0 | Viking | — |
| 1983 | 12 | 132 | 400 | 0 | 1 / 0 | Vålerenga | — |
| 1984 | 12 | 132 | 380 | 0 | 1 / 0 | Vålerenga | — |
| 1985 | 12 | 132 | 396 | 0 | 1 / 0 | Rosenborg | — |
| 1986 | 12 | 132 | 352 | 0 | 1 / 0 | Lillestrøm | — |
| 1987 | 12 | 132 | 343 | 0 | 1 / 0 | Moss | — |
| 1988 | 12 | 132 | 338 | 0 | 1 / 0 | Rosenborg | — |
| 1989 | 12 | 132 | 405 | 0 | 1 / 0 | Lillestrøm | — |
| 1990 | 12 | 132 | 400 | 0 | 1 / 0 | Rosenborg | — |
| 1991 | 12 | 132 | 345 | 0 | 1 / 0 | Viking | — |
| 1992 | 12 | 132 | 403 | 0 | 1 / 0 | Rosenborg | — |
| 1993 | 12 | 132 | 423 | 0 | 1 / 0 | Rosenborg | — |
| 1994 | 12 | 132 | 430 | 0 | 1 / 0 | Rosenborg | — |
| 1995 | 14 | 182 | 679 | 0 | 1 / 0 | Rosenborg | Vålerenga -2 pontos |
| 1996 | 14 | 182 | 638 | 0 | 0 / 1 | Rosenborg | — |
| 1997 | 14 | 182 | 599 | 0 | 1 / 0 | Rosenborg | — |
| 1998 | 14 | 182 | 671 | 0 | 1 / 0 | Rosenborg | — |
| 1999 | 14 | 182 | 697 | 253 | 2 / 0 | Rosenborg | — |
| 2000 | 14 | 182 | 626 | 165 | 2 / 0 | Rosenborg | — |
| 2001 | 14 | 182 | 651 | 637 | 2 / 0 | Rosenborg | — |
| 2002 | 14 | 182 | 545 | 526 | 2 / 0 | Rosenborg | — |
| 2003 | 14 | 182 | 568 | 554 | 2 / 0 | Rosenborg | — |
| 2004 | 14 | 182 | 531 | 0 | 2 / 0 | Rosenborg | — |
| 2005 | 14 | 182 | 515 | 515 | 2 / 0 | Vålerenga | — |
| 2006 | 14 | 182 | 521 | 0 | 2 / 0 | Rosenborg | — |
| 2007 | 14 | 182 | 588 | 0 | 1 / 1 | Brann | — |
| 2008 | 14 | 182 | 505 | 498 | 2 / 0 | Stabæk | — |
| 2009 | 16 | 240 | 697 | 689 | 2 / 0 | Rosenborg | — |
| 2010 | 16 | 240 | 731 | 708 | 2 / 0 | Rosenborg | — |
| 2011 | 16 | 240 | 706 | 334 | 2 / 0 | Molde | — |
| 2012 | 16 | 240 | 693 | 670 | 2 / 0 | Molde | Odd -1 pontos |
| 2013 | 16 | 240 | 694 | 684 | 2 / 0 | Strømsgodset | — |
| 2014 | 16 | 240 | 735 | 728 | 2 / 0 | Molde | — |
| 2015 | 16 | 240 | 774 | 736 | 2 / 0 | Rosenborg | Lillestrøm -1 pontos |
| 2016 | 16 | 240 | 653 | 627 | 2 / 0 | Rosenborg | — |
| 2017 | 16 | 240 | 682 | 682 | 2 / 0 | Rosenborg | — |
| 2018 | 16 | 240 | 672 | 666 | 2 / 0 | Rosenborg | — |
| 2019 | 16 | 240 | 699 | 699 | 2 / 0 | Molde | — |
| 2020 | 16 | 240 | 758 | 758 | 2 / 0 | Bodø/Glimt | — |
| 2021 | 16 | 240 | 732 | 732 | 2 / 0 | Bodø/Glimt | — |
| 2022 | 16 | 240 | 781 | 781 | 2 / 0 | Molde | — |
| 2023 | 16 | 240 | 748 | 748 | 2 / 0 | Bodø/Glimt | — |
| 2024 | 16 | 240 | 681 | 681 | 2 / 0 | Bodø/Glimt | — |
| 2025 | 16 | 240 | 762 | 759 | 2 / 0 | Viking | — |

## Conferência e ocorrências, temporada a temporada

### 1937/38

- sem ocorrências

### 1938/39

- sem ocorrências

### 1947/48

- Quartas de final: Freidig x Kristiansund FK — Freidig won on
- tabela (Distrito V, grupo B) da Wikipédia x jogos — Vard Haugesund tabela [12, 2, 3, 7, 11, 20, 7] jogos [12, 2, 3, 7, 11, 21, 7]
- tabela (Distrito V, grupo B) da Wikipédia x jogos — Brodd tabela [12, 3, 0, 9, 14, 25, 6] jogos [12, 3, 0, 9, 15, 25, 6]

### 1948/49

- sem ocorrências

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- sem ocorrências

### 1952/53

- sem ocorrências

### 1953/54

- sem ocorrências

### 1954/55

- sem ocorrências

### 1955/56

- sem ocorrências

### 1956/57

- sem ocorrências

### 1957/58

- sem ocorrências

### 1958/59

- sem ocorrências

### 1959/60

- sem ocorrências

### 1960/61

- sem ocorrências

### 1961/62

- placar diferente na matriz da Wikipédia — Brann x Ørn Horten: ogol 4-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Brann x Vålerenga: ogol 1-0; Wikipédia 4-1

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- sem ocorrências

### 1966

- sem ocorrências

### 1967

- sem ocorrências

### 1968

- placar diferente na matriz da Wikipédia — Rosenborg x Fredrikstad: ogol 4-3; Wikipédia 2-1

### 1969

- placar diferente na matriz da Wikipédia — Strømsgodset x Brann: ogol 3-1; Wikipédia 2-0

### 1970

- sem ocorrências

### 1971

- tabela da Wikipédia x jogos — Brann tabela [18, 3, 5, 10, 16, 31, 11] jogos [18, 3, 5, 10, 14, 31, 11]

### 1972

- sem ocorrências

### 1973

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['Raufoss', 'Mjøndalen'])

### 1974

- sem ocorrências

### 1975

- sem ocorrências

### 1976

- sem ocorrências

### 1977

- sem ocorrências

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- sem ocorrências

### 1981

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Molde', 'Brann', 'Pors']

### 1982

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Eik Tønsberg', 'Fredrikstad', 'Steinkjer']
- Viking x Rosenborg (1982-10-10): fica 2-2 pela matriz da Wikipédia; o ogol dá 2-0, que fecha pior com as tabelas

### 1983

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Strindheim', 'Brann', 'Pors']

### 1984

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Moss', 'HamKam', 'Vidar']
- placar diferente na matriz da Wikipédia — Start x Strindheim: ogol 2-0; Wikipédia 4-0

### 1985

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Tromsø', 'Moss', 'Sogndal']

### 1986

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Tromsø', 'Vidar', 'Drøbak-Frogn']

### 1987

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Djerv 1919', 'Lyn', 'HamKam']
- Molde x Lillestrøm (1987-07-04): empate sem os pênaltis na matriz da Wikipédia; Lillestrøm venceu, pela contagem da tabela
- placar diferente na matriz da Wikipédia — HamKam x Vålerenga: ogol 1-3; Wikipédia 3-5
- placar diferente na matriz da Wikipédia — Start x Molde: ogol 0-2; Wikipédia 1-0

### 1988

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Start', 'HamKam', 'Bryne']

### 1989

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Vålerenga', 'Djerv 1919', 'HamKam']

### 1990

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Lillestrøm', 'Bryne', 'Eik Tønsberg']

### 1991

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Brann', 'Bryne', 'Strindheim']

### 1992

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['HamKam', 'Drøbak-Frogn', 'Strømmen']

### 1993

- tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: ['Strømsgodset', 'Molde', 'Bryne']

### 1994

- sem ocorrências

### 1995

- sem ocorrências

### 1996

- placar diferente na matriz da Wikipédia — Molde x Lillestrøm: ogol 0-0; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — Molde x Kongsvinger: ogol 2-0; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Strømsgodset x Tromsø: ogol 5-2; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Strømsgodset x Vålerenga: ogol 2-2; Wikipédia 5-2
- tabela da Wikipédia x jogos — Lillestrøm tabela [26, 13, 7, 6, 54, 36, 46] jogos [26, 13, 7, 6, 54, 33, 46]

### 1997

- sem ocorrências

### 1998

- sem ocorrências

### 1999

- placar diferente na matriz da Wikipédia — Viking x Brann: ogol 2-0; Wikipédia 4-0

### 2000

- RSSSF — Molde x Brann: ogol 1-3, RSSSF 3-0
- RSSSF — Start x Tromsø: ogol 1-1, RSSSF 3-2
- RSSSF — Bodø/Glimt x Lillestrøm: ogol 3-0, RSSSF 2-0
- RSSSF — Viking x Vålerenga: ogol 1-1, RSSSF 3-2
- RSSSF — Odd x Bodø/Glimt: ogol 2-2, RSSSF 4-0
- RSSSF — Viking x Start: ogol 3-0, RSSSF 4-0
- RSSSF — Odd x Viking: ogol 2-3, RSSSF 2-1

### 2001

- sem ocorrências

### 2002

- RSSSF — Bryne x Lyn: ogol 0-1, RSSSF 1-2
- RSSSF — Odd x Start: ogol 2-0, RSSSF 4-1
- RSSSF — Moss x Vålerenga: ogol 1-1, RSSSF 2-2
- RSSSF — Vålerenga x Viking: ogol 0-0, RSSSF 3-1
- RSSSF — Lyn x Stabæk: ogol 2-0, RSSSF 2-2
- RSSSF — Stabæk x Odd: ogol 1-0, RSSSF 0-2
- RSSSF — Vålerenga x Odd: ogol 2-0, RSSSF 1-0

### 2003

- RSSSF — Rosenborg x Lyn: ogol 2-0, RSSSF 5-0
- RSSSF — Stabæk x Aalesund: ogol 3-1, RSSSF 2-4
- RSSSF — Lillestrøm x Vålerenga: ogol 0-0, RSSSF 1-1
- RSSSF — Tromsø x Brann: ogol 0-1, RSSSF 1-0
- RSSSF — Bodø/Glimt x Aalesund: ogol 0-2, RSSSF 3-0
- RSSSF — Tromsø x Bodø/Glimt: ogol 3-3, RSSSF 0-3
- RSSSF — Rosenborg x Bodø/Glimt: ogol 5-4, RSSSF 3-1

### 2004

- RSSSF — Tromsø x Lillestrøm: ogol 1-0, RSSSF 1-1
- RSSSF — Bodø/Glimt x Brann: ogol 1-1, RSSSF 3-3
- RSSSF — Lillestrøm x Rosenborg: ogol 2-2, RSSSF 3-2
- RSSSF — Lyn x HamKam: ogol 1-1, RSSSF 3-1
- RSSSF — Stabæk x Brann: ogol 2-1, RSSSF 1-3
- RSSSF — Lyn x Lillestrøm: ogol 1-1, RSSSF 1-0
- RSSSF — Brann x Lyn: ogol 5-1, RSSSF 4-1

### 2005

- sem ocorrências

### 2006

- sem ocorrências

### 2007

- placar diferente na matriz da Wikipédia — Vålerenga x Strømsgodset: ogol 0-0; Wikipédia 1-1
- tabela da RSSSF x jogos — Viking tabela [26, 13, 6, 7, 50, 40, 47] jogos [26, 14, 5, 7, 50, 40, 47] (a tabela da Wikipédia fecha com os jogos)
- tabela da RSSSF x jogos — Lillestrøm tabela [26, 13, 7, 6, 47, 28, 44] jogos [26, 12, 8, 6, 47, 28, 44] (a tabela da Wikipédia fecha com os jogos)

### 2008

- placar diferente na ESPN — Vålerenga x Lillestrøm (2008-10-20): 3-1, ESPN 0-0

### 2009

- sem ocorrências

### 2010

- Sandefjord x Molde (2010-03-21): fica 3-1 pela matriz da Wikipédia (igual ao RSSSF); o ogol dá 1-3, que fecha pior com as tabelas

### 2011

- jogos da página da RSSSF fora da conferência: só 0 de 12 batem com o ogol (a página mistura outras competições ou a leitura falhou)
- Viking x Lillestrøm (2011-10-23): fica 2-0 pela matriz da Wikipédia; o ogol dá 4-0, que fecha pior com as tabelas

### 2012

- football-data — Viking x Sandnes Ulf (2012-07-29): ogol 5-0, football-data 3-0

### 2013

- sem ocorrências

### 2014

- placar diferente na matriz da Wikipédia — Stabæk x Start: ogol 1-2; Wikipédia 0-1

### 2015

- placar diferente na ESPN — Mjøndalen x Odd (2015-08-02): 3-6, ESPN 0-2

### 2016

- sem ocorrências

### 2017

- sem ocorrências

### 2018

- sem ocorrências

### 2019

- sem ocorrências

### 2020

- placar diferente na matriz da Wikipédia — Kristiansund BK x Haugesund: ogol 1-3; Wikipédia 1-2
- placar diferente na matriz da Wikipédia — Start x Kristiansund BK: ogol 1-2; Wikipédia 0-2

### 2021

- sem ocorrências

### 2022

- sem ocorrências

### 2023

- placar diferente na matriz da Wikipédia — Aalesund x Molde: ogol 3-1; Wikipédia 3-0

### 2024

- sem ocorrências

### 2025

- Vålerenga x Kristiansund BK (2025-11-22): fica 3-0 pela matriz da Wikipédia; o ogol dá 3-3, que fecha pior com as tabelas
- football-data — Vålerenga x Kristiansund BK (2025-11-22): ogol 3-0, football-data 3-3
- placar diferente na ESPN — Vålerenga x Kristiansund BK (2025-11-22): 3-0, ESPN 3-3

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_nor.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os redirecionamentos). O clube e o departamento de futebol com artigos separados contam como um (Vålerengens IF e Vålerenga Fotball, como a RSSSF; Mjøndalen, Sogndal, Ranheim, Strømsgodset, Kongsvinger, Lyn). Clubes refundados com artigo próprio ficam separados: Sarpsborg FK x Sarpsborg 08, Kristiansund FK x Kristiansund BK, Sandefjord BK x Sandefjord Fotball (o ogol usa um código só para os dois).
- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Jogos dos grupos da Norgesserien** (1937/38, 1938/39, 1947/48), fora o Distrito V, grupo B: nenhuma fonte em lote traz; ficam as tabelas publicadas.
- **Datas e rodadas de 1937/38 a 1960/61** (só as matrizes e as tabelas do mata-mata).
- **Autores dos gols e cartões** antes da ESPN, fora as páginas da RSSSF de 1999 a 2005.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.
