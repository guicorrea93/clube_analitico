# Campeonato Tcheco (1ª divisão) — coleta de dados

Gerado por `python coleta/cze-1/importar.py`. Pacote em `data/coleta/cze-1/pacote/`.

**Edições:** 33, de 1993/94 a 2025/26 (a liga da República Tcheca). A liga tchecoslovaca e a do Protetorado ficam na competição da Tchecoslováquia.

**Total:** 8234 jogos, 21097 gols, 7121 gols com autor (RSSSF, 1998/99 a 2011/12), 35 clubes. Sem cartões (nenhuma fonte em lote cobre a Tchéquia).

**Fontes:**
- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol; calendários em `data/cache/ogol-cze-1/` para os escudos;
- Wikipédia (en): tabelas da fase regular e dos grupos (ordem oficial, punições), matriz de resultados (conferência e placar dos jogos decididos fora de campo);
- RSSSF: tabela final e jogos de cada temporada (conferência; autores dos gols de 1998/99 a 2011/12), lista de campeões e de artilheiros.

**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a da Wikipédia. Com grupos (2018/19, 2019/20 e desde 2021/22), a classificação final é o grupo do título, depois do 7º ao 10º pela fase regular, depois o grupo de rebaixamento, com os números de todos os jogos da liga (o play-off europeu fica fora da conta). 2 pontos por vitória em 1993/94 e 3 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** o critério calculado que reproduz a ordem oficial (confronto direto em 33, saldo em 0, vitórias em 0).

| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|
| 1993/94 | 16 | 240 | 602 | 0 | 2 / 0 | Sparta Praga | — |
| 1994/95 | 16 | 240 | 632 | 0 | 2 / 0 | Sparta Praga | — |
| 1995/96 | 16 | 240 | 634 | 0 | 2 / 0 | Slavia Praga | — |
| 1996/97 | 16 | 240 | 571 | 0 | 2 / 0 | Sparta Praga | — |
| 1997/98 | 16 | 240 | 585 | 0 | 2 / 0 | Sparta Praga | — |
| 1998/99 | 16 | 240 | 625 | 545 | 2 / 0 | Sparta Praga | — |
| 1999/00 | 16 | 240 | 570 | 536 | 2 / 0 | Sparta Praga | — |
| 2000/01 | 16 | 240 | 613 | 580 | 1 / 0 | Sparta Praga | — |
| 2001/02 | 16 | 240 | 590 | 546 | 2 / 0 | Slovan Liberec | — |
| 2002/03 | 16 | 240 | 592 | 512 | 2 / 0 | Sparta Praga | — |
| 2003/04 | 16 | 240 | 578 | 572 | 2 / 0 | Baník Ostrava | — |
| 2004/05 | 16 | 240 | 531 | 523 | 1 / 0 | Sparta Praga | Slovan Liberec -6 pontos; Slovácko -12 pontos; Opava -6 pontos |
| 2005/06 | 16 | 240 | 567 | 516 | 2 / 0 | Slovan Liberec | — |
| 2006/07 | 16 | 240 | 534 | 525 | 2 / 0 | Sparta Praga | — |
| 2007/08 | 16 | 240 | 556 | 528 | 2 / 0 | Slavia Praga | — |
| 2008/09 | 16 | 240 | 582 | 574 | 1 / 0 | Slavia Praga | — |
| 2009/10 | 16 | 240 | 574 | 565 | 1 / 1 | Sparta Praga | Bohemians Střížkov -15 pontos |
| 2010/11 | 16 | 240 | 634 | 501 | 2 / 0 | Viktoria Plzeň | — |
| 2011/12 | 16 | 240 | 635 | 98 | 2 / 0 | Slovan Liberec | Sigma Olomouc -9 pontos |
| 2012/13 | 16 | 240 | 620 | 0 | 2 / 0 | Viktoria Plzeň | — |
| 2013/14 | 16 | 240 | 673 | 0 | 1 / 0 | Sparta Praga | — |
| 2014/15 | 16 | 240 | 645 | 0 | 2 / 0 | Viktoria Plzeň | — |
| 2015/16 | 16 | 240 | 676 | 0 | 2 / 0 | Viktoria Plzeň | — |
| 2016/17 | 16 | 240 | 597 | 0 | 2 / 0 | Slavia Praga | — |
| 2017/18 | 16 | 240 | 572 | 0 | 2 / 0 | Viktoria Plzeň | — |
| 2018/19 | 16 | 276 | 740 | 0 | 4 / 0 | Slavia Praga | — |
| 2019/20 | 16 | 271 | 708 | 0 | 4 / 0 | Slavia Praga | — |
| 2020/21 | 18 | 306 | 822 | 0 | 2 / 0 | Slavia Praga | — |
| 2021/22 | 16 | 276 | 770 | 0 | 4 / 0 | Viktoria Plzeň | — |
| 2022/23 | 16 | 276 | 819 | 0 | 4 / 0 | Sparta Praga | — |
| 2023/24 | 16 | 277 | 792 | 0 | 4 / 0 | Sparta Praga | — |
| 2024/25 | 16 | 276 | 734 | 0 | 4 / 0 | Slavia Praga | — |
| 2025/26 | 16 | 276 | 724 | 0 | 4 / 0 | Slavia Praga | — |

## Conferência e ocorrências, temporada a temporada

### 1993/94

- placar diferente na matriz da Wikipédia — Slavia Praga x Baník Ostrava: ogol 1-0; Wikipédia 1-1 (RSSSF = ogol)

### 1994/95

- placar diferente na matriz da Wikipédia — Viktoria Žižkov x Slavia Praga: ogol 0-1; Wikipédia 0-0 (RSSSF = ogol)

### 1995/96

- a matriz da Wikipédia dá Baník Ostrava 0-1 Viktoria Žižkov e 3-1 Dynamo České Budějovice; o ogol dá 2-2 e 0-1, e as tabelas da RSSSF e da Wikipédia fecham com o ogol: erro da matriz
- placar diferente na matriz da Wikipédia — Baník Ostrava x Viktoria Žižkov: ogol 2-2; Wikipédia 0-1
- placar diferente na matriz da Wikipédia — Baník Ostrava x Dynamo České Budějovice: ogol 0-1; Wikipédia 3-1

### 1996/97

- sem ocorrências

### 1997/98

- placar diferente na matriz da Wikipédia — Viktoria Plzeň x Lázně Bohdaneč: ogol 1-2; Wikipédia 0-0 (RSSSF = ogol)

### 1998/99

- sem ocorrências

### 1999/00

- sem ocorrências

### 2000/01

- tabela da RSSSF da fase regular não encontrada na página da temporada
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['Teplice', 'Bohemians 1905'])

### 2001/02

- placar diferente na matriz da Wikipédia — Příbram x Opava: ogol 2-0; Wikipédia 0-0 (RSSSF = ogol)

### 2002/03

- sem ocorrências

### 2003/04

- placar diferente na matriz da Wikipédia — Viktoria Žižkov x Chmel Blšany: ogol 2-0; Wikipédia 2-2 (RSSSF = ogol)

### 2004/05

- tabela da RSSSF da fase regular não encontrada na página da temporada

### 2005/06

- sem ocorrências

### 2006/07

- sem ocorrências

### 2007/08

- sem ocorrências

### 2008/09

- tabela da RSSSF da fase regular não encontrada na página da temporada

### 2009/10

- tabela publicada x jogos (RSSSF) — Bohemians Střížkov tabela [30, 4, 4, 22, 27, 65, -4] jogos [30, 4, 4, 22, 27, 65, 1] (a tabela da Wikipédia fecha com os jogos)

### 2010/11

- sem ocorrências

### 2011/12

- sem ocorrências

### 2012/13

- placar diferente na matriz da Wikipédia — Viktoria Plzeň x Slovácko: ogol 1-1; Wikipédia 0-0 (RSSSF = ogol)

### 2013/14

- tabela da RSSSF da fase regular não encontrada na página da temporada

### 2014/15

- placar diferente na matriz da Wikipédia — Slovácko x Sparta Praga: ogol 0-2; Wikipédia 0-1 (RSSSF = ogol)

### 2015/16

- FK Dukla Praga x Slovan Liberec (2016-02-12): placar corrigido para 2-0 (o ogol dá 1-0; a matriz da Wikipédia, a página da RSSSF e as tabelas da RSSSF e da Wikipédia dão 2-0)

### 2016/17

- placar diferente na matriz da Wikipédia — Slavia Praga x Teplice: ogol 2-1; Wikipédia 2-0 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — Slavia Praga x Viktoria Plzeň: ogol 1-0; Wikipédia 2-1 (RSSSF = ogol)

### 2017/18

- sem ocorrências

### 2018/19

- placar diferente na matriz da Wikipédia — Bohemians 1905 x Slovácko: ogol 2-1; Wikipédia 0-0 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — Bohemians 1905 x Opava: ogol 0-0; Wikipédia 2-1 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — Bohemians 1905 x Příbram: ogol 2-2; Wikipédia 1-4 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — Karviná x Bohemians 1905: ogol 0-3; Wikipédia 0-1 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — FK Dukla Praga x Bohemians 1905: ogol 0-1; Wikipédia 1-1 (RSSSF = ogol)

### 2019/20

- artilheiro sem um clube só na lista da RSSSF: Petar Musa (Slovan L./Slavia P.)

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- placar diferente na matriz da Wikipédia — Slovan Liberec x Zlín: ogol 2-1; Wikipédia 1-0 (RSSSF = ogol)
- placar diferente na matriz da Wikipédia — Viktoria Plzeň x Zlín: ogol 4-0; Wikipédia 3-0 (RSSSF = ogol)

### 2023/24

- sem ocorrências

### 2024/25

- sem ocorrências

### 2025/26

- Slavia Praga x Sparta Praga (2026-05-09): DA no ogol; fica 0-3 (abandonado nos acréscimos com 3-2 para o Slavia, depois da invasão de campo da torcida do Slavia; em 12/05/2026 a liga deu 3-0 ao Sparta (nota da matriz da Wikipédia))

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_cze.py`, pela linhagem do clube (o alvo do link da Wikipédia). Mesmo clube: Bohemians Praha (até 2002) e Bohemians 1905; os nomes de patrocinador de Zlín, Brno, Drnovice, Příbram, Hradec Králové e Karviná. Clubes diferentes: o Dukla Praha histórico (1993/94) e o 1. FK Příbram, para onde ele se mudou em 1996 (o ogol usa o mesmo código), e o FK Dukla Praha de hoje; o Bohemians de Střížkov (2008/09); o Slovácká Slavia (1995/96) e o 1. FC Slovácko.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols fora de 1998/99-2011/12, cartões, público, estádio e árbitro:** a ESPN e o football-data não cobrem a Tchéquia, e a RSSSF só traz os autores nessas temporadas; o resto, só a ficha de cada jogo no ogol (jogo a jogo).
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.
