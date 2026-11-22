# Campeonato Português (1ª divisão) — coleta de dados

Gerado por `python coleta/por-1/importar.py`. Pacote em `data/coleta/por-1/pacote/`.

**Edições:** 92, de 1934/35 a 2025/26: Campeonato da Liga (1934/35 a 1937/38, experimental; os títulos contam hoje entre os da 1ª divisão), Primeira Divisão (1938/39 a 1998/99) e Primeira Liga.

**Total:** 20978 jogos, 59543 gols, 13874 gols com autor (ESPN), 30915 cartões, 73 clubes.

**Fontes:**
- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; ficha dos jogos decididos fora de campo; calendários guardados em `data/cache/ogol-por-1/` para os escudos;
- RSSSF: tabela final e matriz de resultados de 1934/35 a 2004/05 (conferência jogo a jogo), tabela final das temporadas seguintes, lista de campeões e de artilheiros (com o clube);
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;
- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ESPN (liga `por.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;
- Wikipédia (en): tabela final de cada temporada (ordem oficial, punições e marca de rebaixamento).

**Regras:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Lisboa; Açores nos jogos em casa do Santa Clara). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (até 1944/45 não havia rebaixamento: os participantes saíam dos campeonatos regionais). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente em outra fonte numa temporada em que as tabelas publicadas fecham com o ogol é erro da outra fonte e fica só anotado; quando a outra fonte e as tabelas publicadas concordam contra o ogol, o placar é corrigido (CORRECOES e TRIBUNAL em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 80, confronto direto aplicado de novo entre os que seguem empatados em 4, o mesmo com saldo e gols fora de casa no confronto em 6, saldo de gols em 1, média de gols em 1); é ele que ordena a classificação rodada a rodada.

| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1934/35 | ogol + RSSSF + Wikipédia | 8 | 56 | 258 | 0 | 2 / 0 | Porto | — |
| 1935/36 | ogol + RSSSF + Wikipédia | 8 | 56 | 240 | 0 | 2 / 0 | Benfica | — |
| 1936/37 | ogol + RSSSF + Wikipédia | 8 | 56 | 265 | 0 | 2 / 0 | Benfica | — |
| 1937/38 | ogol + RSSSF + Wikipédia | 8 | 56 | 247 | 0 | 2 / 0 | Benfica | — |
| 1938/39 | ogol + RSSSF + Wikipédia | 8 | 56 | 273 | 0 | 2 / 0 | Porto | — |
| 1939/40 | ogol + RSSSF + Wikipédia | 10 | 90 | 431 | 0 | 2 / 0 | Porto | — |
| 1940/41 | ogol + RSSSF + Wikipédia | 8 | 56 | 292 | 0 | 2 / 0 | Sporting | — |
| 1941/42 | ogol + RSSSF + Wikipédia | 12 | 132 | 695 | 0 | 2 / 0 | Benfica | — |
| 1942/43 | ogol + RSSSF + Wikipédia | 10 | 90 | 539 | 0 | 2 / 0 | Benfica | — |
| 1943/44 | ogol + RSSSF + Wikipédia | 10 | 90 | 456 | 0 | 2 / 0 | Sporting | — |
| 1944/45 | ogol + RSSSF + Wikipédia | 10 | 90 | 496 | 0 | 2 / 0 | Benfica | — |
| 1945/46 | ogol + RSSSF + Wikipédia | 12 | 132 | 638 | 0 | 2 / 0 | Belenenses | — |
| 1946/47 | ogol + RSSSF + Wikipédia | 14 | 182 | 933 | 0 | 2 / 0 | Sporting | — |
| 1947/48 | ogol + RSSSF + Wikipédia | 14 | 182 | 832 | 0 | 1 / 1 | Sporting | — |
| 1948/49 | ogol + RSSSF + Wikipédia | 14 | 182 | 745 | 0 | 2 / 0 | Sporting | — |
| 1949/50 | ogol + RSSSF + Wikipédia | 14 | 182 | 773 | 0 | 2 / 0 | Benfica | — |
| 1950/51 | ogol + RSSSF + Wikipédia | 14 | 182 | 732 | 0 | 2 / 0 | Sporting | — |
| 1951/52 | ogol + RSSSF + Wikipédia | 14 | 182 | 706 | 0 | 2 / 0 | Sporting | — |
| 1952/53 | ogol + RSSSF + Wikipédia | 14 | 182 | 623 | 0 | 2 / 0 | Sporting | — |
| 1953/54 | ogol + RSSSF + Wikipédia | 14 | 182 | 683 | 0 | 2 / 0 | Sporting | — |
| 1954/55 | ogol + RSSSF + Wikipédia | 14 | 182 | 640 | 0 | 2 / 0 | Benfica | — |
| 1955/56 | ogol + RSSSF + Wikipédia | 14 | 182 | 674 | 0 | 2 / 0 | Porto | — |
| 1956/57 | ogol + RSSSF + Wikipédia | 14 | 182 | 681 | 0 | 2 / 0 | Benfica | — |
| 1957/58 | ogol + RSSSF + Wikipédia | 14 | 182 | 634 | 0 | 2 / 0 | Sporting | — |
| 1958/59 | ogol + RSSSF + Wikipédia | 14 | 182 | 691 | 0 | 2 / 0 | Porto | — |
| 1959/60 | ogol + RSSSF + Wikipédia | 14 | 182 | 609 | 0 | 2 / 0 | Benfica | — |
| 1960/61 | ogol + RSSSF + Wikipédia | 14 | 182 | 596 | 0 | 2 / 0 | Benfica | — |
| 1961/62 | ogol + RSSSF + Wikipédia | 14 | 182 | 617 | 0 | 2 / 0 | Sporting | — |
| 1962/63 | ogol + RSSSF + Wikipédia | 14 | 182 | 596 | 0 | 2 / 0 | Benfica | — |
| 1963/64 | ogol + RSSSF + Wikipédia | 14 | 182 | 609 | 0 | 2 / 0 | Benfica | — |
| 1964/65 | ogol + RSSSF + Wikipédia | 14 | 182 | 614 | 0 | 2 / 0 | Benfica | — |
| 1965/66 | ogol + RSSSF + Wikipédia | 14 | 182 | 613 | 0 | 2 / 0 | Sporting | — |
| 1966/67 | ogol + RSSSF + Wikipédia | 14 | 182 | 481 | 0 | 2 / 0 | Benfica | — |
| 1967/68 | ogol + RSSSF + Wikipédia | 14 | 182 | 524 | 0 | 2 / 0 | Benfica | — |
| 1968/69 | ogol + RSSSF + Wikipédia | 14 | 182 | 466 | 0 | 2 / 0 | Benfica | — |
| 1969/70 | ogol + RSSSF + Wikipédia | 14 | 182 | 520 | 0 | 2 / 0 | Sporting | — |
| 1970/71 | ogol + RSSSF + Wikipédia | 14 | 182 | 426 | 0 | 2 / 0 | Benfica | — |
| 1971/72 | ogol + RSSSF + Wikipédia | 16 | 240 | 638 | 0 | 2 / 0 | Benfica | — |
| 1972/73 | ogol + RSSSF + Wikipédia | 16 | 240 | 691 | 0 | 2 / 0 | Benfica | — |
| 1973/74 | ogol + RSSSF + Wikipédia | 16 | 240 | 691 | 0 | 2 / 0 | Sporting | — |
| 1974/75 | ogol + RSSSF + Wikipédia | 16 | 240 | 703 | 0 | 2 / 0 | Benfica | — |
| 1975/76 | ogol + RSSSF + Wikipédia | 16 | 240 | 681 | 0 | 2 / 0 | Benfica | — |
| 1976/77 | ogol + RSSSF + Wikipédia | 16 | 240 | 616 | 0 | 2 / 0 | Benfica | — |
| 1977/78 | ogol + RSSSF + Wikipédia | 16 | 240 | 585 | 0 | 2 / 0 | Porto | — |
| 1978/79 | ogol + RSSSF + Wikipédia | 16 | 240 | 626 | 0 | 2 / 0 | Porto | — |
| 1979/80 | ogol + RSSSF + Wikipédia | 16 | 240 | 600 | 0 | 2 / 0 | Sporting | — |
| 1980/81 | ogol + RSSSF + Wikipédia | 16 | 240 | 560 | 0 | 2 / 0 | Benfica | — |
| 1981/82 | ogol + RSSSF + Wikipédia | 16 | 240 | 563 | 0 | 2 / 0 | Sporting | — |
| 1982/83 | ogol + RSSSF + Wikipédia | 16 | 240 | 570 | 0 | 2 / 0 | Benfica | — |
| 1983/84 | ogol + RSSSF + Wikipédia | 16 | 240 | 599 | 0 | 2 / 0 | Benfica | — |
| 1984/85 | ogol + RSSSF + Wikipédia | 16 | 240 | 669 | 0 | 2 / 0 | Porto | — |
| 1985/86 | ogol + RSSSF + Wikipédia | 16 | 240 | 566 | 0 | 2 / 0 | Porto | — |
| 1986/87 | ogol + RSSSF + Wikipédia | 16 | 240 | 583 | 0 | 2 / 0 | Benfica | — |
| 1987/88 | ogol + RSSSF + Wikipédia | 20 | 380 | 863 | 0 | 2 / 0 | Porto | — |
| 1988/89 | ogol + RSSSF + Wikipédia | 20 | 380 | 791 | 0 | 2 / 0 | Benfica | — |
| 1989/90 | ogol + RSSSF + Wikipédia | 18 | 306 | 666 | 0 | 2 / 0 | Porto | — |
| 1990/91 | ogol + RSSSF + Wikipédia | 20 | 380 | 874 | 0 | 1 / 1 | Benfica | — |
| 1991/92 | ogol + RSSSF + Wikipédia | 18 | 306 | 692 | 0 | 2 / 0 | Porto | — |
| 1992/93 | ogol + RSSSF + Wikipédia | 18 | 306 | 715 | 0 | 1 / 1 | Porto | — |
| 1993/94 | ogol + RSSSF + Wikipédia | 18 | 306 | 750 | 0 | 2 / 0 | Benfica | — |
| 1994/95 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 731 | 0 | 1 / 1 | Porto | — |
| 1995/96 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 797 | 0 | 1 / 1 | Porto | — |
| 1996/97 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 760 | 0 | 2 / 0 | Porto | — |
| 1997/98 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 770 | 0 | 2 / 0 | Porto | — |
| 1998/99 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 810 | 0 | 1 / 1 | Porto | — |
| 1999/00 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 739 | 0 | 2 / 0 | Sporting | — |
| 2000/01 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 807 | 0 | 2 / 0 | Boavista | — |
| 2001/02 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 818 | 0 | 2 / 0 | Sporting | — |
| 2002/03 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 806 | 0 | 2 / 0 | Porto | — |
| 2003/04 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 729 | 0 | 2 / 0 | Porto | — |
| 2004/05 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 711 | 0 | 2 / 0 | Benfica | — |
| 2005/06 | ogol + engsoccerdata + football-data + RSSSF + Wikipédia | 18 | 306 | 681 | 0 | 2 / 0 | Porto | — |
| 2006/07 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 554 | 546 | 2 / 0 | Porto | — |
| 2007/08 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 553 | 550 | 1 / 1 | Porto | Belenenses -3 pontos; Porto -6 pontos; União de Leiria -3 pontos |
| 2008/09 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 552 | 528 | 1 / 1 | Porto | — |
| 2009/10 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 601 | 598 | 2 / 0 | Benfica | — |
| 2010/11 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 584 | 327 | 2 / 0 | Porto | — |
| 2011/12 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 634 | 592 | 2 / 0 | Porto | — |
| 2012/13 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 667 | 665 | 2 / 0 | Porto | — |
| 2013/14 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 16 | 240 | 569 | 558 | 2 / 0 | Benfica | — |
| 2014/15 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 763 | 763 | 2 / 0 | Benfica | — |
| 2015/16 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 831 | 831 | 2 / 0 | Benfica | — |
| 2016/17 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 728 | 727 | 2 / 0 | Benfica | — |
| 2017/18 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 826 | 826 | 2 / 0 | Porto | — |
| 2018/19 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 826 | 826 | 2 / 0 | Benfica | — |
| 2019/20 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 763 | 763 | 1 / 1 | Porto | — |
| 2020/21 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 739 | 739 | 2 / 0 | Sporting | — |
| 2021/22 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 807 | 800 | 2 / 0 | Porto | — |
| 2022/23 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 763 | 751 | 2 / 0 | Benfica | — |
| 2023/24 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 877 | 877 | 2 / 0 | Sporting | — |
| 2024/25 | ogol + engsoccerdata + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 786 | 786 | 2 / 0 | Sporting | — |
| 2025/26 | ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 | 821 | 821 | 2 / 0 | Porto | — |

## Conferência e ocorrências, temporada a temporada

### 1934/35

- sem ocorrências

### 1935/36

- placar diferente na matriz da RSSSF — Porto x Boavista (1936-04-26): ogol 4-0, RSSSF 3-0 (a RSSSF troca o mando dos dois jogos do par)
- placar diferente na matriz da RSSSF — Boavista x Porto (1936-04-23): ogol 0-3, RSSSF 0-4 (a RSSSF troca o mando dos dois jogos do par)
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

### 1936/37

- sem ocorrências

### 1937/38

- sem ocorrências

### 1938/39

- sem ocorrências

### 1939/40

- sem ocorrências

### 1940/41

- sem ocorrências

### 1941/42

- sem ocorrências

### 1942/43

- sem ocorrências

### 1943/44

- placar diferente na matriz da RSSSF — Vitória de Setúbal x Vitória de Guimarães (1944-01-02): ogol 5-3, RSSSF 8-0 (a RSSSF troca o mando dos dois jogos do par)
- placar diferente na matriz da RSSSF — Vitória de Guimarães x Vitória de Setúbal (1944-03-05): ogol 0-8, RSSSF 3-5 (a RSSSF troca o mando dos dois jogos do par)
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

### 1944/45

- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Sporting, Wikipédia Belenenses); fica a da Wikipédia

### 1945/46

- placar diferente na matriz da RSSSF — Benfica x SL Elvas (1946-01-13): ogol 5-2, RSSSF 5-1
- placar diferente na matriz da RSSSF — Sporting x SL Elvas (1946-05-19): ogol 5-1, RSSSF 5-2
- placar diferente na matriz da RSSSF — Porto x Benfica (1946-03-31): ogol 0-2, RSSSF 2-3
- placar diferente na matriz da RSSSF — Porto x Sporting (1946-01-27): ogol 2-3, RSSSF 0-2
- placar diferente na matriz da RSSSF — Vitória de Guimarães x Benfica (1946-02-24): ogol 2-5, RSSSF 1-4
- placar diferente na matriz da RSSSF — Vitória de Guimarães x Sporting (1945-12-30): ogol 1-3, RSSSF 2-4
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 6 jogos em que a matriz da RSSSF difere, fica o ogol

### 1946/47

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Porto, Wikipédia Belenenses); fica a da Wikipédia
- SL Elvas não está na temporada seguinte, mas não foi rebaixado: terminou em 10º; em 1947 fundiu-se com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão

### 1947/48

- a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Atlético CP)
- tabela publicada x jogos (Wikipédia) — Atlético CP tabela [26, 11, 3, 12, 56, 61, 25] jogos [26, 11, 4, 11, 69, 62, 26]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1948/49

- sem ocorrências

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- placar diferente na matriz da RSSSF — Sporting x Benfica (1952-03-02): ogol 3-2, RSSSF 2-3 (a RSSSF troca o mando dos dois jogos do par)
- placar diferente na matriz da RSSSF — Benfica x Sporting (1951-11-18): ogol 3-2, RSSSF 2-3 (a RSSSF troca o mando dos dois jogos do par)
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

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

- resultado decidido fora de campo: Atlético CP x Leixões fica 0-0 com vitória do Leixões (ogol DA) — o resultado não foi homologado e os pontos da vitória foram dados ao Leixões (ficha do ogol: "derrota administrativa (0-0)"). A matriz da RSSSF traz 0-3 neste jogo e 3-1 no Leixões x Atlético (o ogol, 6-1); as duas versões dão os mesmos totais, e as tabelas da RSSSF e da Wikipédia fecham com elas. Fica o ogol
- placar diferente na matriz da RSSSF — Leixões x Atlético CP (1960-11-27): ogol 6-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Atlético CP x Leixões (1961-04-09): ogol 0-0, RSSSF 0-3
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

### 1961/62

- sem ocorrências

### 1962/63

- sem ocorrências

### 1963/64

- placar diferente na matriz da RSSSF — Sporting x Seixal (1963-10-27): ogol 3-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — Seixal x Sporting (1964-01-26): ogol 1-3, RSSSF 1-2
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

### 1964/65

- sem ocorrências

### 1965/66

- placar diferente na matriz da RSSSF — Vitória de Guimarães x Lusitano de Évora (1966-05-01): ogol 3-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Vitória de Guimarães x Barreirense (1966-02-13): ogol 3-2, RSSSF 4-3
- placar diferente na matriz da RSSSF — Lusitano de Évora x Beira-Mar (1966-01-16): ogol 1-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Barreirense x Beira-Mar (1966-02-06): ogol 2-2, RSSSF 1-1
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 4 jogos em que a matriz da RSSSF difere, fica o ogol

### 1966/67

- sem ocorrências

### 1967/68

- sem ocorrências

### 1968/69

- sem ocorrências

### 1969/70

- sem ocorrências

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- sem ocorrências

### 1974/75

- resultado decidido fora de campo: CUF x Vitória de Setúbal fica 1-1 com vitória do CUF (ogol DA) — derrota administrativa do Vitória de Setúbal (ficha do ogol; 1-1 no intervalo). As tabelas da RSSSF e da Wikipédia contam a vitória do CUF com o 1-1 de campo (um gol pró e um contra para cada um); a matriz da RSSSF traz 0-2 neste jogo e 1-2 no Vitória x CUF (o ogol, 2-1), o que não fecha com as tabelas
- placar diferente na matriz da RSSSF — Vitória de Setúbal x CUF (1974-09-22): ogol 2-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — CUF x Vitória de Setúbal (1975-01-19): ogol 1-1, RSSSF 0-2
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Oriental de Lisboa, Wikipédia Académica); fica a da Wikipédia

### 1975/76

- resultado decidido fora de campo: Atlético CP x Sporting fica 3-0 (ogol IC) — derrota do Sporting por invasão de campo (ficha do ogol: 3-0); a matriz da RSSSF traz 3-0

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- sem ocorrências

### 1979/80

- sem ocorrências

### 1980/81

- placar diferente na matriz da RSSSF — Benfica x Espinho (1980-12-28): ogol 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Espinho x Benfica (1981-05-31): ogol 3-0, RSSSF 2-0
- as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos 2 jogos em que a matriz da RSSSF difere, fica o ogol

### 1981/82

- sem ocorrências

### 1982/83

- sem ocorrências

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- resultado decidido fora de campo: Belenenses x Marítimo fica 0-3 (ogol DA) — o Belenenses escalou irregularmente o jogador Mapuata e perdeu por 0-3 (ficha do ogol; matriz da RSSSF)
- jogo sem placar no ogol (DA): Braga x Benfica fica 1-1 — a ficha do ogol diz que o jogo foi interrompido aos 86 minutos por invasão de campo e que os dois clubes foram punidos com derrota; mas a matriz e a tabela da RSSSF e a tabela da Wikipédia contam o empate de campo, 1-1 (com ele, o Benfica é campeão com 49 pontos, como na lista de campeões). Fica o 1-1

### 1987/88

- sem ocorrências

### 1988/89

- sem ocorrências

### 1989/90

- resultado decidido fora de campo: Nacional da Madeira x Belenenses fica 3-0 (ogol DA) — o Belenenses escalou irregularmente o avançado Macaé e perdeu por 3-0 (ficha do ogol; matriz da RSSSF)

### 1990/91

- a tabela da Wikipédia troca os números do Marítimo e do Farense; a da RSSSF fecha com os jogos
- a matriz da RSSSF traz trocadas as colunas 13 e 14 (Gil Vicente e Famalicão): desfeita a troca, os 380 placares batem com o ogol
- tabela publicada x jogos (Wikipédia) — Marítimo tabela [38, 14, 6, 18, 46, 47, 34] jogos [38, 12, 10, 16, 37, 48, 34]
- tabela publicada x jogos (Wikipédia) — Farense tabela [38, 12, 10, 16, 37, 48, 34] jogos [38, 14, 6, 18, 46, 47, 34]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1991/92

- sem ocorrências

### 1992/93

- a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Porto: 57 gols pró; os jogos dão 59)
- tabela publicada x jogos (Wikipédia) — Porto tabela [34, 24, 6, 4, 57, 17, 54] jogos [34, 24, 6, 4, 59, 17, 54]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1993/94

- sem ocorrências

### 1994/95

- a tabela da Wikipédia dá ao Benfica as vitórias e derrotas do 1-2 contra o Sporting e os gols do 2-0; a da RSSSF fecha com o 2-0
- placar corrigido: Benfica x Sporting de 1-2 para 2-0 — o ogol traz 1-2; a matriz e a tabela da RSSSF, o engsoccerdata e o football-data trazem 2-0 (e a lista de campeões da RSSSF põe o Sporting, vice, 9 pontos atrás do Porto, o que só fecha com 2-0)
- placar diferente no engsoccerdata — Porto x Vitória de Setúbal (1995-02-19): ogol 2-0, engsoccerdata 1-0
- placar diferente no football-data — Porto x Vitória de Setúbal (1995-02-19): ogol 2-0, football-data 1-0
- tabela publicada x jogos (Wikipédia) — Sporting tabela [34, 23, 9, 2, 59, 21, 55] jogos [34, 22, 9, 3, 57, 22, 53]
- tabela publicada x jogos (Wikipédia) — Benfica tabela [34, 21, 5, 8, 61, 28, 47] jogos [34, 22, 5, 7, 61, 28, 49]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1995/96

- a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Benfica)
- placar corrigido: Leça x Boavista de 0-2 para 0-3 — o ogol traz 0-2; a matriz e a tabela da RSSSF, a tabela da Wikipédia, o engsoccerdata e o football-data trazem 0-3
- tabela publicada x jogos (Wikipédia) — Benfica tabela [34, 22, 7, 5, 56, 25, 73] jogos [34, 22, 7, 5, 57, 27, 73]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- a ordem da RSSSF não sai de nenhum critério de desempate e a da Wikipédia sai: fica a da Wikipédia

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Académica: 70 gols contra; os jogos dão 71)
- tabela publicada x jogos (Wikipédia) — Académica tabela [34, 4, 9, 21, 30, 70, 21] jogos [34, 4, 9, 21, 30, 71, 21]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1999/00

- sem ocorrências

### 2000/01

- sem ocorrências

### 2001/02

- sem ocorrências

### 2002/03

- sem ocorrências

### 2003/04

- sem ocorrências

### 2004/05

- sem ocorrências

### 2005/06

- Académica, Naval e Belenenses terminaram com 39 pontos; a Wikipédia (e os sites que a repetem) põe a Académica em 13º e o Naval em 14º, a RSSSF o contrário (que é o que dá o confronto direto entre os três). Fica a da Wikipédia
- o Belenenses terminou em 15º, na zona de rebaixamento, e ficou na 1ª divisão: o Gil Vicente foi rebaixado no lugar dele (caso Mateus, jogador inscrito irregularmente)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Naval 1º de Maio, Wikipédia Académica); fica a da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Académica', 'Naval 1º de Maio'])

### 2006/07

- gols da ESPN não batem com o placar — Vitória de Setúbal 1-1 Académica: ESPN 0-1 (descartados)
- gols da ESPN não batem com o placar — Belenenses 0-2 Boavista: ESPN 0-1 (descartados)
- gols da ESPN não batem com o placar — Académica 1-3 Nacional da Madeira: ESPN 0-3 (descartados)

### 2007/08

- Porto -6 pontos e União de Leiria -3 pontos (caso Apito Final, corrupção na temporada 2003/04), como na tabela da RSSSF e na classificação do fim da temporada. A Wikipédia de hoje não desconta, porque o Conselho de Justiça da Federação absolveu o Porto em 2017; a ordem é a mesma nos dois casos
- Boavista rebaixado pelo caso Apito Final (terminou em 9º); o Paços de Ferreira, 15º, ficou na 1ª divisão
- resultado decidido fora de campo: Belenenses x Naval 1º de Maio fica 0-3 (ogol DA) — o Belenenses escalou um jogador irregular (16ª rodada): derrota por 0-3 (ficha do ogol; RSSSF: "awarded 0-3; originally 2-1") e mais 3 pontos descontados (RSSSF e Wikipédia)
- punição tirada da tabela da RSSSF: Porto -6 pontos
- punição tirada da tabela da RSSSF: União de Leiria -3 pontos
- tabela publicada x jogos (Wikipédia) — Porto tabela [30, 24, 3, 3, 60, 13, 75] jogos [30, 24, 3, 3, 60, 13, 69]
- tabela publicada x jogos (Wikipédia) — União de Leiria tabela [30, 3, 7, 20, 25, 53, 16] jogos [30, 3, 7, 20, 25, 53, 13]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 2008/09

- a tabela da RSSSF dá 46 pontos ao Leixões (os jogos dão 45, como na Wikipédia)
- Estrela da Amadora rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou na 1ª divisão
- placar diferente na ESPN — Vitória de Setúbal x Braga (2009-04-05): ogol 0-3, ESPN 0-2
- tabela publicada x jogos (RSSSF) — Leixões tabela [30, 12, 9, 9, 30, 31, 46] jogos [30, 12, 9, 9, 30, 31, 45]
- gols da ESPN não batem com o placar — Sporting 3-1 Trofense: ESPN 4-1 (descartados)
- gols da ESPN não batem com o placar — Trofense 1-2 Leixões: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — Belenenses 1-0 Académica: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 2-0 Belenenses: ESPN 2-1 (descartados)
- gols da ESPN não batem com o placar — Rio Ave 2-4 Vitória de Guimarães: ESPN 2-5 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 0-3 Braga: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Rio Ave 0-3 Nacional da Madeira: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Belenenses 1-0 Rio Ave: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Estrela da Amadora 1-0 Vitória de Guimarães: ESPN 2-0 (descartados)

### 2009/10

- gols da ESPN não batem com o placar — Porto 3-0 Nacional da Madeira: ESPN 6-0 (descartados)

### 2010/11

- ESPN com 239 de 240 jogos (ex. sem ESPN: Beira-Mar x Marítimo, 2010-09-18)
- gols da ESPN não batem com o placar — Braga 3-1 Portimonense: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Naval 1º de Maio 0-1 Porto: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Paços de Ferreira 1-0 Sporting: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Benfica 1-2 Académica: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — Nacional da Madeira 2-1 Benfica: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Porto 3-0 Beira-Mar: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Sporting 1-0 Marítimo: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Benfica 3-0 Vitória de Setúbal: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Braga 1-0 Marítimo: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Rio Ave 0-2 Porto: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Naval 1º de Maio 1-3 Sporting: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 2-1 Benfica: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Benfica 2-0 Sporting: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Paços de Ferreira 2-2 Braga: ESPN 4-4 (descartados)
- gols da ESPN não batem com o placar — Nacional da Madeira 0-2 Porto: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Braga 3-1 Naval 1º de Maio: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Marítimo 0-1 Benfica: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Porto 2-0 Olhanense: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Sporting 1-1 Nacional da Madeira: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 1-0 Paços de Ferreira: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Benfica 1-0 Braga: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Beira-Mar 1-1 Sporting: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 1-1 Porto: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 2-1 Vitória de Guimarães: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Sporting 1-0 Rio Ave: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Porto 5-1 União de Leiria: ESPN 10-2 (descartados)
- gols da ESPN não batem com o placar — Benfica 2-0 Paços de Ferreira: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Académica 0-1 Porto: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Rio Ave 2-0 Braga: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Braga 2-3 Beira-Mar: ESPN 4-6 (descartados)
- gols da ESPN não batem com o placar — Porto 5-0 Benfica: ESPN 8-0 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-3 Vitória de Guimarães: ESPN 4-5 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 2-1 Braga: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Porto 2-0 Portimonense: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 0-1 Académica: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Beira-Mar 1-3 Benfica: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — Benfica 2-0 Olhanense: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — União de Leiria 3-1 Braga: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Porto 1-0 Vitória de Setúbal: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Braga 5-0 Académica: ESPN 8-0 (descartados)
- gols da ESPN não batem com o placar — Benfica 5-2 Rio Ave: ESPN 10-4 (descartados)
- gols da ESPN não batem com o placar — Paços de Ferreira 0-3 Porto: ESPN 0-6 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 0-3 Sporting: ESPN 0-6 (descartados)
- gols da ESPN não batem com o placar — Porto 4-1 Marítimo: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-1 Braga: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — União de Leiria 0-3 Benfica: ESPN 0-6 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-3 Paços de Ferreira: ESPN 4-6 (descartados)
- gols da ESPN não batem com o placar — Académica 0-1 Benfica: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Porto 3-1 Naval 1º de Maio: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Beira-Mar 0-1 Porto: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Benfica 4-2 Nacional da Madeira: ESPN 8-4 (descartados)
- gols da ESPN não batem com o placar — Marítimo 0-3 Sporting: ESPN 0-6 (descartados)
- gols da ESPN não batem com o placar — Porto 3-0 Nacional da Madeira: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Sporting 3-3 Naval 1º de Maio: ESPN 6-6 (descartados)
- gols da ESPN não batem com o placar — Porto 1-0 Rio Ave: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 0-2 Benfica: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Benfica 3-0 Vitória de Guimarães: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Braga 0-2 Porto: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Braga 1-2 Paços de Ferreira: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Sporting 0-2 Benfica: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Benfica 2-1 Marítimo: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Nacional da Madeira 1-0 Sporting: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Porto 2-0 Vitória de Guimarães: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Braga 2-1 Benfica: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Sporting 1-0 Beira-Mar: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Benfica 1-1 Portimonense: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — União de Leiria 0-2 Porto: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Porto 3-1 Académica: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Braga 1-0 Rio Ave: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Paços de Ferreira 1-5 Benfica: ESPN 2-10 (descartados)
- gols da ESPN não batem com o placar — União de Leiria 1-3 Marítimo: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — Académica 1-0 Portimonense: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Beira-Mar 1-2 Braga: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Benfica 1-2 Porto: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 1-1 Sporting: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Marítimo 1-1 Nacional da Madeira: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-0 Académica: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Naval 1º de Maio 2-1 Benfica: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Braga 3-1 Vitória de Guimarães: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Académica 1-1 Vitória de Setúbal: ESPN 2-1 (descartados)
- gols da ESPN não batem com o placar — Benfica 2-1 Beira-Mar: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Porto 3-2 Sporting: ESPN 6-4 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-1 Portimonense: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Olhanense 1-1 Benfica: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Vitória de Setúbal 0-4 Porto: ESPN 0-8 (descartados)
- gols da ESPN não batem com o placar — Porto 3-3 Paços de Ferreira: ESPN 6-6 (descartados)
- gols da ESPN não batem com o placar — Rio Ave 1-2 Benfica: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Braga 0-1 Sporting: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Marítimo 0-2 Porto: ESPN 0-4 (descartados)

### 2011/12

- gols da ESPN não batem com o placar — Gil Vicente 2-2 Benfica: ESPN 4-4 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 0-1 Porto: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — União de Leiria 1-2 Académica: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Porto 3-1 Gil Vicente: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Benfica 3-1 CD Feirense: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Braga 2-0 Marítimo: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Gil Vicente 2-0 Académica: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Sporting 2-3 Marítimo: ESPN 4-6 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 0-3 Beira-Mar: ESPN 0-6 (descartados)
- gols da ESPN não batem com o placar — Paços de Ferreira 2-3 Sporting: ESPN 4-6 (descartados)
- gols da ESPN não batem com o placar — Braga 3-0 CD Feirense: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Vitória de Guimarães 1-0 CD Feirense: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Porto 2-0 CD Feirense: ESPN 4-0 (descartados)

### 2012/13

- gols da ESPN não batem com o placar — Estoril 2-0 Vitória de Guimarães: ESPN 4-0 (descartados)

### 2013/14

- jogo acrescentado: Benfica 2-0 Sporting (2014-02-11) — falta no calendário do ogol; o football-data e o engsoccerdata trazem 2-0 em 11/02/2014 (o jogo da 18ª rodada, adiado); as tabelas da RSSSF e da Wikipédia só fecham com ele
- gols da ESPN não batem com o placar — Sporting 5-1 Arouca: ESPN 5-0 e gol sem clube (descartados)
- gols da ESPN não batem com o placar — Arouca 1-2 Estoril: ESPN 0-2 e gol sem clube (descartados)
- gols da ESPN não batem com o placar — Arouca 1-0 Rio Ave: ESPN 0-0 e gol sem clube (descartados)
- gols da ESPN não batem com o placar — Nacional da Madeira 0-1 Arouca: ESPN 0-0 e gol sem clube (descartados)

### 2014/15

- sem ocorrências

### 2015/16

- sem ocorrências

### 2016/17

- gols da ESPN não batem com o placar — Tondela 0-1 Belenenses: ESPN 0-2 (descartados)

### 2017/18

- Belenenses não está na temporada seguinte, mas não foi rebaixado: a SAD separou-se do clube em 2018 e seguiu na 1ª divisão como Belenenses SAD (clube à parte); o CF Os Belenenses recomeçou nas divisões distritais, sem ter sido rebaixado em campo

### 2018/19

- sem ocorrências

### 2019/20

- a tabela da Wikipédia dá um gol pró e um contra a menos ao Gil Vicente e ao Paços de Ferreira; os jogos fecham com a RSSSF, o football-data e o engsoccerdata
- Vitória de Setúbal e Desportivo das Aves rebaixados por não cumprirem as regras de licenciamento; o Portimonense, 17º, ficou na 1ª divisão
- tabela publicada x jogos (Wikipédia) — Gil Vicente tabela [34, 11, 10, 13, 39, 43, 43] jogos [34, 11, 10, 13, 40, 44, 43]
- tabela publicada x jogos (Wikipédia) — Paços de Ferreira tabela [34, 11, 6, 17, 35, 51, 39] jogos [34, 11, 6, 17, 36, 52, 39]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- rebaixados: pela temporada seguinte ['Desportivo das Aves', 'Vitória de Setúbal']; marca da Wikipédia ['Vitória de Setúbal']

### 2020/21

- Rio Ave perdeu o play-off de manutenção (contra um clube da 2ª divisão) e foi rebaixado

### 2021/22

- ESPN com 305 de 306 jogos (ex. sem ESPN: Belenenses SAD x Benfica, 2021-11-27)
- Moreirense perdeu o play-off de manutenção (contra um clube da 2ª divisão) e foi rebaixado

### 2022/23

- ESPN com 301 de 306 jogos (ex. sem ESPN: Arouca x Santa Clara, 2023-02-11)
- Marítimo perdeu o play-off de manutenção (contra um clube da 2ª divisão) e foi rebaixado
- gols da ESPN não batem com o placar — Porto 2-1 Casa Pia: ESPN 4-2 (descartados)

### 2023/24

- Portimonense perdeu o play-off de manutenção (contra um clube da 2ª divisão) e foi rebaixado

### 2024/25

- sem ocorrências

### 2025/26

- sem ocorrências

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_por.py` (serve para todas as divisões portuguesas): nome de exibição como o clube é conhecido no Brasil, cidade e país. Nomes únicos no mundo: "Nacional da Madeira", "Oriental de Lisboa", "CD Feirense" e "Caldas SC" (há Nacional e Oriental no Uruguai, Feirense e Caldas no Brasil).
- Clubes à parte: Belenenses (CF Os Belenenses, até 2017/18) e Belenenses SAD (2018/19 a 2021/22); AVS (2024/25 em diante) e Desportivo das Aves; SL Elvas e O Elvas. O Estrela da Amadora de hoje fica com a história do antigo, como no ogol.
- O ogol entra pelo código do clube (tabela `OGOL` do cadastro); a ESPN é casada por votação jogo a jogo (mesma data e placar): 40 códigos.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.
- **Público e estádio antes da ESPN:** nenhuma fonte em lote.
- **Play-offs de manutenção (contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).
- **Campeonato de Portugal (1921/22 a 1937/38, em mata-mata):** é outra competição; fica de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
