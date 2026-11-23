# Campeonato Espanhol (1ª divisão) — coleta de dados

Gerado por `python coleta/esp-1/importar.py`. Pacote em `data/coleta/esp-1/pacote/`.

**Edições:** 95, de 1928/29 a 2025/26 (Primera División). Sem liga em 1936/37-1938/39 (Guerra Civil).

**Total:** 27716 jogos, 78392 gols, 25072 gols com autor (ESPN), 51662 cartões, 63 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1928/29-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+) e estatísticas por time (chutes, faltas, escanteios, cartões; 2005/06+). Não traz árbitro na liga espanhola;
- ogol: rodada oficial de cada jogo e conferência de placar; calendários guardados em `data/cache/ogol-esp-1/` para os escudos;
- ESPN (liga `esp.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (José Vicente Tejedor Carnicero e outros): tabela final de todas as temporadas e matriz de resultados até 1999/2000 (conferência jogo a jogo); artilheiros até 1999/2000;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões, artilheiros pela contagem oficial da liga (súmulas da LFP; "List of La Liga top scorers") e Troféu Pichichi (do jornal Marca, que a liga não reconhece; anotado quando difere).

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Madri; Canárias nos jogos em casa do Las Palmas e do Tenerife). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96.

**Desempate:** a regra espanhola em todas as temporadas (revisão QE-001): pontos, confronto direto (pontos e saldo entre os empatados, de novo entre os que seguem empatados), saldo de gols e gols pró. Ela reproduz a ordem oficial em 95 de 95 temporadas. Na classificação rodada a rodada, o confronto só vale depois de jogados todos os jogos entre os empatados.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1928/29 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 383 | 0 | 1 / 1 | Barcelona | — |
| 1929/30 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 420 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1930/31 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 384 | 0 | 1 / 1 | Athletic Bilbao | — |
| 1931/32 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 351 | 0 | 2 / 0 | Real Madrid | — |
| 1932/33 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 400 | 0 | 2 / 0 | Real Madrid | — |
| 1933/34 | engsoccerdata + ogol + RSSSF + Wikipédia | 10 | 90 (90) | 378 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1934/35 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 541 | 0 | 2 / 0 | Betis | — |
| 1935/36 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 528 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1939/40 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 501 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1940/41 | engsoccerdata + ogol + RSSSF + Wikipédia | 12 | 132 (132) | 569 | 0 | 1 / 1 | Atlético de Madrid | — |
| 1941/42 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 741 | 0 | 2 / 0 | Valencia | — |
| 1942/43 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 712 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1943/44 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 694 | 0 | 2 / 0 | Valencia | — |
| 1944/45 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 656 | 0 | 2 / 0 | Barcelona | — |
| 1945/46 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 611 | 0 | 2 / 0 | Sevilla | — |
| 1946/47 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 704 | 0 | 2 / 0 | Valencia | — |
| 1947/48 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 696 | 0 | 2 / 0 | Barcelona | — |
| 1948/49 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 739 | 0 | 2 / 0 | Barcelona | — |
| 1949/50 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 773 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1950/51 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 1038 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1951/52 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 987 | 0 | 2 / 0 | Barcelona | — |
| 1952/53 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 935 | 0 | 2 / 0 | Barcelona | — |
| 1953/54 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 844 | 0 | 2 / 0 | Real Madrid | — |
| 1954/55 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 899 | 0 | 2 / 0 | Real Madrid | — |
| 1955/56 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 908 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1956/57 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 777 | 0 | 2 / 0 | Real Madrid | — |
| 1957/58 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 792 | 0 | 2 / 0 | Real Madrid | — |
| 1958/59 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 775 | 0 | 2 / 0 | Barcelona | — |
| 1959/60 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 807 | 0 | 2 / 0 | Barcelona | — |
| 1960/61 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 755 | 0 | 2 / 0 | Real Madrid | — |
| 1961/62 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 761 | 0 | 1 / 1 | Real Madrid | — |
| 1962/63 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 744 | 0 | 2 / 0 | Real Madrid | — |
| 1963/64 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 669 | 0 | 2 / 0 | Real Madrid | — |
| 1964/65 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 659 | 0 | 2 / 0 | Real Madrid | — |
| 1965/66 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 609 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1966/67 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 656 | 0 | 2 / 0 | Real Madrid | — |
| 1967/68 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 654 | 0 | 1 / 1 | Real Madrid | — |
| 1968/69 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 561 | 0 | 2 / 0 | Real Madrid | — |
| 1969/70 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 567 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1970/71 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 543 | 0 | 2 / 0 | Valencia | — |
| 1971/72 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 675 | 0 | 1 / 1 | Real Madrid | — |
| 1972/73 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 656 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1973/74 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 710 | 0 | 1 / 1 | Barcelona | — |
| 1974/75 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 745 | 0 | 2 / 0 | Real Madrid | — |
| 1975/76 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 765 | 0 | 2 / 0 | Real Madrid | — |
| 1976/77 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 829 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1977/78 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 843 | 0 | 2 / 0 | Real Madrid | — |
| 1978/79 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 825 | 0 | 2 / 0 | Real Madrid | — |
| 1979/80 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 770 | 0 | 2 / 0 | Real Madrid | CD Málaga -3 pontos |
| 1980/81 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 829 | 0 | 1 / 1 | Real Sociedad | — |
| 1981/82 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 853 | 0 | 2 / 0 | Real Sociedad | — |
| 1982/83 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 780 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1983/84 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 782 | 0 | 2 / 0 | Athletic Bilbao | — |
| 1984/85 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 662 | 0 | 2 / 0 | Barcelona | — |
| 1985/86 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 798 | 0 | 2 / 0 | Real Madrid | — |
| 1986/87 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 396 (396) | 951 | 0 | 3 / 0 | Real Madrid | — |
| 1987/88 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 909 | 0 | 2 / 0 | Real Madrid | — |
| 1988/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 868 | 0 | 2 / 0 | Real Madrid | — |
| 1989/90 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 921 | 0 | 2 / 0 | Real Madrid | — |
| 1990/91 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 822 | 0 | 2 / 0 | Barcelona | — |
| 1991/92 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 913 | 0 | 2 / 0 | Barcelona | — |
| 1992/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 954 | 0 | 2 / 0 | Barcelona | — |
| 1993/94 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 989 | 0 | 2 / 0 | Barcelona | — |
| 1994/95 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 966 | 0 | 2 / 0 | Real Madrid | — |
| 1995/96 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 22 | 462 (462) | 1246 | 0 | 2 / 0 | Atlético de Madrid | — |
| 1996/97 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 22 | 462 (462) | 1271 | 0 | 2 / 0 | Real Madrid | — |
| 1997/98 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 1009 | 0 | 2 / 0 | Barcelona | — |
| 1998/99 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 1003 | 0 | 2 / 0 | Barcelona | — |
| 1999/00 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 999 | 0 | 2 / 0 | Deportivo La Coruña | — |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 1095 | 0 | 1 / 1 | Real Madrid | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 961 | 944 | 2 / 0 | Valencia | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1016 | 1010 | 2 / 0 | Real Madrid | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1015 | 1015 | 2 / 0 | Valencia | Racing Santander -1 pontos |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 980 | 951 | 2 / 0 | Barcelona | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 936 | 935 | 2 / 0 | Barcelona | — |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 942 | 913 | 1 / 1 | Real Madrid | — |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1021 | 1015 | 2 / 0 | Real Madrid | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1101 | 1078 | 2 / 0 | Barcelona | — |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1031 | 1028 | 2 / 0 | Barcelona | — |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1042 | 1042 | 2 / 0 | Barcelona | — |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1050 | 1027 | 2 / 0 | Real Madrid | — |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1091 | 1091 | 2 / 0 | Barcelona | — |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1045 | 1045 | 2 / 0 | Atlético de Madrid | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1009 | 1009 | 1 / 1 | Barcelona | Almería -3 pontos |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1043 | 1043 | 2 / 0 | Barcelona | — |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1118 | 1118 | 2 / 0 | Real Madrid | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1024 | 1022 | 2 / 0 | Barcelona | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 983 | 983 | 2 / 0 | Barcelona | — |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 942 | 942 | 2 / 0 | Real Madrid | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 953 | 953 | 2 / 0 | Atlético de Madrid | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 951 | 948 | 2 / 0 | Real Madrid | — |
| 2022/23 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 955 | 936 | 2 / 0 | Barcelona | — |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1005 | 1005 | 2 / 0 | Real Madrid | — |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 995 | 995 | 2 / 0 | Barcelona | — |
| 2025/26 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1024 | 1024 | 2 / 0 | Barcelona | — |

## Conferência e ocorrências, temporada a temporada

### 1928/29

- a tabela da Wikipédia traz gols errados para Athletic Bilbao (47-34) e Arenas (33-43); a da RSSSF fecha com os jogos (43-33 e 32-39) e dá a ordem
- tabela publicada x jogos (Wikipédia) — Athletic Bilbao tabela [18, 8, 4, 6, 47, 34, 20] jogos [18, 8, 4, 6, 43, 33, 20]
- tabela publicada x jogos (Wikipédia) — Arenas de Getxo tabela [18, 8, 3, 7, 33, 43, 19] jogos [18, 8, 3, 7, 32, 39, 19]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- artilheiro: contagem oficial da liga Paco Bienzobas com 17 gols; o Pichichi (Marca) deu Paco Bienzobas com 14 gols. Fica a contagem oficial

### 1929/30

- a matriz da RSSSF traz 2-1 nos dois jogos de Espanyol x Europa; a base e o ogol trazem 1-2 nos dois (as tabelas não distinguem, porque cada clube fica com uma vitória e uma derrota). Fica a base
- placar diferente na matriz da RSSSF — Espanyol Barcelona x CE Europa: base 1-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — CE Europa x Espanyol Barcelona: base 1-2, RSSSF 2-1
- artilheiro: contagem oficial da liga Guillermo Gorostiza com 20 gols; o Pichichi (Marca) deu Guillermo Gorostiza com 19 gols. Fica a contagem oficial

### 1930/31

- a tabela da Wikipédia traz 32 gols contra para o Real Madrid; a da RSSSF e os jogos dão 27
- tabela publicada x jogos (Wikipédia) — Real Madrid tabela [18, 7, 4, 7, 24, 32, 18] jogos [18, 7, 4, 7, 24, 27, 18]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1931/32

- artilheiro: contagem oficial da liga Bata com 13 gols; o Pichichi (Marca) deu Guillermo Gorostiza com 12 gols. Fica a contagem oficial

### 1932/33

- sem ocorrências

### 1933/34

- artilheiro: contagem oficial da liga Isidro Lángara com 26 gols; o Pichichi (Marca) deu Isidro Lángara com 27 gols. Fica a contagem oficial

### 1934/35

- artilheiro: contagem oficial da liga Isidro Lángara com 27 gols; o Pichichi (Marca) deu Isidro Lángara com 26 gols. Fica a contagem oficial

### 1935/36

- Real Oviedo não está na temporada seguinte, mas não caiu: 3º colocado em 1935/36, teve dispensa de 1939/40 por ter o estádio destruído na guerra e voltou em 1940/41 (Wikipédia es, 1935-36 e 1939-40)
- Atlético de Madrid está na temporada seguinte, mas caiu em campo: 11º em 1935/36, caiu com o Osasuna; voltou à 1ª divisão em 1939/40 ao vencer a repescagem pela vaga do Oviedo (Athletic de Madrid 3-1 Osasuna, Valência, 26/11/1939; Wikipédia es)
- artilheiro: a RSSSF dá Lángara com 27 gols

### 1939/40

- sem ocorrências

### 1940/41

- Valencia x Hércules: a RSSSF (matriz e tabela) traz 6-1; a base, o ogol e a tabela da Wikipédia trazem 6-0. Fica a base
- placar diferente na matriz da RSSSF — Valencia CF x Hercules CF: base 6-0, RSSSF 6-1
- tabela publicada x jogos (RSSSF) — Valencia CF tabela [22, 11, 5, 6, 60, 53, 27] jogos [22, 11, 5, 6, 60, 52, 27]
- tabela publicada x jogos (RSSSF) — Hercules CF tabela [22, 7, 2, 13, 29, 67, 16] jogos [22, 7, 2, 13, 28, 67, 16]
- artilheiro: contagem oficial da liga Pruden com 33 gols; o Pichichi (Marca) deu Pruden com 30 gols. Fica a contagem oficial

### 1941/42

- sem ocorrências

### 1942/43

- artilheiro: contagem oficial da liga Mariano Martín com 30 gols; o Pichichi (Marca) deu Mariano Martín com 32 gols. Fica a contagem oficial

### 1943/44

- artilheiro: contagem oficial da liga Mundo com 28 gols; o Pichichi (Marca) deu Mundo com 27 gols. Fica a contagem oficial

### 1944/45

- artilheiro: contagem oficial da liga Telmo Zarra com 20 gols; o Pichichi (Marca) deu Telmo Zarra com 19 gols. Fica a contagem oficial

### 1945/46

- sem ocorrências

### 1946/47

- artilheiro: contagem oficial da liga Telmo Zarra com 33 gols; o Pichichi (Marca) deu Telmo Zarra com 34 gols. Fica a contagem oficial

### 1947/48

- artilheiro: contagem oficial da liga Pahiño com 20 gols; o Pichichi (Marca) deu Pahiño com 23 gols. Fica a contagem oficial

### 1948/49

- artilheiro: contagem oficial da liga César com 27 gols; o Pichichi (Marca) deu César com 28 gols. Fica a contagem oficial

### 1949/50

- artilheiro: contagem oficial da liga Telmo Zarra com 24 gols; o Pichichi (Marca) deu Telmo Zarra com 25 gols. Fica a contagem oficial

### 1950/51

- artilheiro: a RSSSF dá Zarra com 36 gols

### 1951/52

- sem ocorrências

### 1952/53

- sem ocorrências

### 1953/54

- artilheiro: a RSSSF dá Di Stéfano com 29 gols

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

- artilheiro: contagem oficial da liga Ferenc Puskás com 25 gols; o Pichichi (Marca) deu Ferenc Puskás com 26 gols. Fica a contagem oficial

### 1960/61

- fica a ordem da RSSSF: Athletic Bilbao, Betis e Real Sociedad empatados com 30 pontos: no confronto direto entre os três, Athletic e Betis fazem 5 pontos e a Real Sociedad 2; entre os dois, Athletic 0-0 Betis e Betis 1-3 Athletic, e o Athletic fica em 6º. É a ordem da RSSSF e do BDFutbol, e a regra das outras temporadas; a Wikipédia põe o Betis à frente pelo saldo do triangular
- ordem diferente entre Wikipédia e RSSSF em 2 posições (ex.: Wikipédia Real Betis, RSSSF Athletic Bilbao); fica a da RSSSF
- artilheiro: contagem oficial da liga Ferenc Puskás com 28 gols; o Pichichi (Marca) deu Ferenc Puskás com 27 gols. Fica a contagem oficial

### 1961/62

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Osasuna e Mallorca)
- tabela publicada x jogos (Wikipédia) — CA Osasuna tabela [30, 11, 5, 14, 30, 47, 27] jogos [30, 10, 7, 13, 54, 59, 27]
- tabela publicada x jogos (Wikipédia) — RCD Mallorca tabela [30, 10, 7, 13, 54, 59, 27] jogos [30, 11, 5, 14, 30, 47, 27]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- ordem diferente entre Wikipédia e RSSSF em 2 posições (ex.: Wikipédia CA Osasuna, RSSSF RCD Mallorca); fica a da RSSSF

### 1962/63

- sem ocorrências

### 1963/64

- artilheiro: contagem oficial da liga Ferenc Puskás com 21 gols; o Pichichi (Marca) deu Ferenc Puskás com 20 gols. Fica a contagem oficial

### 1964/65

- artilheiro: contagem oficial da liga Cayetano Ré com 26 gols; o Pichichi (Marca) deu Cayetano Ré com 25 gols. Fica a contagem oficial

### 1965/66

- artilheiro: contagem oficial da liga Luis Aragonés com 18 gols; o Pichichi (Marca) deu Vavá II com 19 gols. Fica a contagem oficial

### 1966/67

- sem ocorrências

### 1967/68

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Elche e CD Málaga)
- tabela publicada x jogos (Wikipédia) — Elche CF tabela [30, 9, 9, 12, 29, 37, 27] jogos [30, 11, 5, 14, 30, 39, 27]
- tabela publicada x jogos (Wikipédia) — CD Malaga tabela [30, 11, 5, 14, 30, 39, 27] jogos [30, 9, 9, 12, 29, 37, 27]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- ordem diferente entre Wikipédia e RSSSF em 2 posições (ex.: Wikipédia Elche CF, RSSSF CD Malaga); fica a da RSSSF

### 1968/69

- artilheiro: a RSSSF dá Amancio Amaro com 14 gols

### 1969/70

- artilheiro: a RSSSF dá Amancio Amaro, Luis Aragonés com 16 gols

### 1970/71

- sem ocorrências

### 1971/72

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Sabadell e Córdoba)
- tabela publicada x jogos (Wikipédia) — CE Sabadell tabela [34, 6, 13, 15, 32, 51, 25] jogos [34, 7, 9, 18, 27, 52, 23]
- tabela publicada x jogos (Wikipédia) — Cordoba CF tabela [34, 7, 9, 18, 27, 52, 23] jogos [34, 6, 13, 15, 32, 51, 25]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- ordem diferente entre Wikipédia e RSSSF em 2 posições (ex.: Wikipédia CE Sabadell, RSSSF Cordoba CF); fica a da RSSSF

### 1972/73

- sem ocorrências

### 1973/74

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Oviedo e Racing Santander); a Wikipédia também erra vitórias e empates de Atlético de Madrid, Zaragoza e Real Sociedad
- tabela publicada x jogos (Wikipédia) — Atletico Madrid tabela [34, 16, 8, 10, 50, 31, 40] jogos [34, 18, 6, 10, 50, 31, 42]
- tabela publicada x jogos (Wikipédia) — Real Zaragoza tabela [34, 16, 7, 11, 51, 38, 39] jogos [34, 16, 8, 10, 51, 38, 40]
- tabela publicada x jogos (Wikipédia) — Real Sociedad tabela [34, 15, 8, 11, 46, 45, 38] jogos [34, 16, 7, 11, 46, 45, 39]
- tabela publicada x jogos (Wikipédia) — Real Oviedo tabela [34, 8, 11, 15, 36, 54, 27] jogos [34, 9, 6, 19, 29, 52, 24]
- tabela publicada x jogos (Wikipédia) — Racing Santander tabela [34, 9, 6, 19, 29, 52, 24] jogos [34, 8, 11, 15, 36, 54, 27]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- ordem diferente entre Wikipédia e RSSSF em 2 posições (ex.: Wikipédia Real Oviedo, RSSSF Racing Santander); fica a da RSSSF

### 1974/75

- sem ocorrências

### 1975/76

- artilheiro: contagem oficial da liga Quini com 21 gols; o Pichichi (Marca) deu Quini com 18 gols. Fica a contagem oficial

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- sem ocorrências

### 1979/80

- CD Málaga x AD Almería (30/03/1980): o Málaga não compareceu; vitória de 1-0 dada ao Almería (W.O.) e 3 pontos a menos para o Málaga (RSSSF e Wikipédia). Nas tabelas, o W.O. conta a vitória mas não os gols
- jogo acrescentado: CD Malaga 0-3 UD Salamanca (1980-04-27) — falta no engsoccerdata; a matriz da RSSSF traz o jogo: terminou 0-3 em 27/04/1980, foi anulado por irregularidade (o Salamanca perdeu 2 pontos) e o resultado original foi confirmado em 25/05/1982
- nota da RSSSF: [1] CD Málaga had 3 points deducted for forfeiting against AD Almería.
- nota da RSSSF: matriz [1] awarded 0-1 to AD Almería for "incomparecencia" of CD Málaga, who had 3 points deducted.
- nota da RSSSF: matriz [2] finished 0-3 on April 27, 1980, but annulled because of irregularities; UD Salamanca had 2 points deducted; this decision was annulled on May 25, 1982, when the original result was confirmed.

### 1980/81

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Atlético de Madrid e Valencia)
- tabela publicada x jogos (Wikipédia) — Atletico Madrid tabela [34, 17, 8, 9, 59, 41, 42] jogos [34, 16, 10, 8, 46, 39, 42]
- tabela publicada x jogos (Wikipédia) — Valencia CF tabela [34, 16, 10, 8, 46, 39, 42] jogos [34, 17, 8, 9, 59, 41, 42]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1981/82

- artilheiro: contagem oficial da liga Quini com 27 gols; o Pichichi (Marca) deu Quini com 26 gols. Fica a contagem oficial

### 1982/83

- sem ocorrências

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- Real Valladolid x Las Palmas (17/12/1986): o ogol traz 0-0; a base, a matriz e a tabela da RSSSF e a da Wikipédia fecham com 2-1: erro do ogol
- 1986/87: com a ampliação para 20 clubes, os três últimos do grupo de rebaixamento jogaram uma liguilla em turno único, que mandou um só para a 2ª divisão: Racing 1-1 Cádiz (24/06/1987; Racing 4-3 nos pênaltis), Cádiz 1-1 Osasuna (28/06; Cádiz 4-3 nos pênaltis) e Osasuna 2-0 Racing (30/06). Osasuna 3 pontos, Cádiz 2, Racing 1: caiu o Racing (cadizcf.com, racinguismo.com, RSSSF). Esses jogos não contam como Primera División (Wikipédia es), e a classificação oficial continua a do grupo de rebaixamento: 16º Osasuna, 17º Racing (rebaixado) e 18º Cádiz (Wikipédia es e RSSSF)
- placar diferente no ogol — Real Valladolid x UD Las Palmas (1986-12-17): base 2-1, ogol 0-0

### 1987/88

- sem ocorrências

### 1988/89

- data diferente no ogol em 1 jogos (ex.: CA Osasuna x Real Madrid: base 1989-01-28, ogol 1989-05-03); fica a da base

### 1989/90

- sem ocorrências

### 1990/91

- sem ocorrências

### 1991/92

- sem ocorrências

### 1992/93

- sem ocorrências

### 1993/94

- Real Madrid x Real Sociedad: o football-data traz 0-1; a base, a matriz da RSSSF e as tabelas fecham com 0-2: erro do football-data
- placar diferente no football-data — Real Madrid x Real Sociedad: base 0-2, football-data 0-1

### 1994/95

- sem ocorrências

### 1995/96

- sem ocorrências

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- placar diferente no ogol — Valencia CF x RCD Mallorca (1999-06-20): base 3-0, ogol 2-0

### 1999/00

- Valencia x Mallorca (20/06/2000): o ogol traz 2-0; a base, o football-data, a matriz da RSSSF e as tabelas fecham com 3-0: erro do ogol
- data diferente no ogol em 2 jogos (ex.: CD Numancia x Real Betis: base 2000-05-20, ogol 2000-05-21); fica a da base

### 2000/01

- a tabela da Wikipédia dá ao Espanyol 15 vitórias, 7 empates e 52 pontos; os jogos e a RSSSF dão 14, 8 e 50
- tabela publicada x jogos (Wikipédia) — Espanyol Barcelona tabela [38, 15, 7, 16, 46, 44, 52] jogos [38, 14, 8, 16, 46, 44, 50]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 2001/02

- ESPN com 375 de 380 jogos (ex. sem ESPN: UD Las Palmas x Espanyol Barcelona, 2001-10-14)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Athletic Bilbao, Wikipédia Sevilla FC); fica a da Wikipédia
- artilheiro: contagem oficial da liga Diego Tristán com 20 gols; o Pichichi (Marca) deu Diego Tristán com 21 gols. Fica a contagem oficial

### 2002/03

- Villarreal x Celta (18/05/2003): a ESPN traz 6-0; base, ogol, football-data e as tabelas fecham com 5-0 (gols da ESPN descartados)
- placar diferente na ESPN — Villarreal CF x Celta Vigo (2003-05-18): base 5-0, ESPN 6-0
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF Atletico Madrid, Wikipédia CA Osasuna); fica a da Wikipédia
- gols da ESPN não batem com o placar — CD Alaves 0-1 Racing Santander: ESPN 1-1 (descartados)
- gols da ESPN não batem com o placar — Villarreal CF 5-0 Celta Vigo: ESPN 6-0 (descartados)

### 2003/04

- data corrigida: FC Barcelona x Sevilla FC de 2003-09-02 para 2003-09-03 — o "jogo da meia-noite": começou à 00:05 de 03/09/2003 (football-data, ESPN, transfermarkt e BDFutbol); o engsoccerdata e o ogol trazem 02/09
- data diferente no ogol em 30 jogos (ex.: Racing Santander x RCD Mallorca: base 2003-08-31, ogol 2003-08-30); fica a da base
- artilheiro: contagem oficial da liga Ronaldo com 24 gols; o Pichichi (Marca) deu Ronaldo com 25 gols. Fica a contagem oficial

### 2004/05

- placar corrigido: CA Osasuna x Albacete de 4-2 para 3-2 — o engsoccerdata traz 4-2; ogol, football-data, ESPN e as tabelas da RSSSF e da Wikipédia trazem 3-2
- Real Madrid x Real Sociedad: começou em 12/12/2004 e foi suspenso aos 88 minutos, com 1-1 (ameaça de bomba); completado em 05/01/2005
- ESPN com 378 de 380 jogos (ex. sem ESPN: Real Sociedad x FC Barcelona, 2005-05-28)
- gols da ESPN não batem com o placar — Villarreal CF 3-2 Atletico Madrid: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Espanyol Barcelona 1-3 Sevilla FC: ESPN 2-3 (descartados)
- gols da ESPN não batem com o placar — Albacete 1-2 Malaga CF: ESPN 1-3 (descartados)
- gols da ESPN não batem com o placar — Villarreal CF 4-0 Getafe CF: ESPN 5-0 (descartados)
- gols da ESPN não batem com o placar — Albacete 3-1 Levante UD: ESPN 3-2 (descartados)
- gols da ESPN não batem com o placar — CD Numancia 2-2 CA Osasuna: ESPN 3-2 (descartados)
- artilheiro: contagem oficial da liga Diego Forlán, Samuel Eto'o com 25 gols; o Pichichi (Marca) deu Diego Forlán com 25 gols. Fica a contagem oficial

### 2005/06

- gols da ESPN não batem com o placar — Celta Vigo 0-1 Racing Santander: ESPN 0-2 (descartados)

### 2006/07

- a tabela da Wikipédia traz gols errados para Atlético de Madrid, Levante, Real Sociedad e Gimnàstic; a da RSSSF fecha com os jogos e dá a ordem
- tabela publicada x jogos (Wikipédia) — Atletico Madrid tabela [38, 17, 9, 12, 47, 40, 60] jogos [38, 17, 9, 12, 46, 39, 60]
- tabela publicada x jogos (Wikipédia) — Levante UD tabela [38, 10, 12, 16, 38, 54, 42] jogos [38, 10, 12, 16, 37, 53, 42]
- tabela publicada x jogos (Wikipédia) — Real Sociedad tabela [38, 8, 11, 19, 30, 46, 35] jogos [38, 8, 11, 19, 32, 47, 35]
- tabela publicada x jogos (Wikipédia) — Gimnastic tabela [38, 7, 7, 24, 33, 67, 28] jogos [38, 7, 7, 24, 34, 69, 28]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- gols da ESPN não batem com o placar — Sevilla FC 4-0 Levante UD: ESPN 8-0 (descartados)
- gols da ESPN não batem com o placar — Sevilla FC 3-2 Real Betis: ESPN 6-4 (descartados)
- gols da ESPN não batem com o placar — Atletico Madrid 2-1 Sevilla FC: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — Sevilla FC 1-0 Getafe CF: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — FC Barcelona 3-1 Sevilla FC: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — Valencia CF 2-3 Villarreal CF: ESPN 3-3 (descartados)

### 2007/08

- data diferente no ogol em 1 jogos (ex.: FC Barcelona x Real Murcia: base 2008-01-12, ogol 2008-01-13); fica a da base
- ESPN com 379 de 380 jogos (ex. sem ESPN: Real Betis x Athletic Bilbao, 2008-03-15)
- gols da ESPN não batem com o placar — Real Madrid 2-1 Atletico Madrid: ESPN 4-2 (descartados)

### 2008/09

- gols da ESPN não batem com o placar — Villarreal CF 0-3 Real Valladolid: ESPN 0-4 (descartados)
- gols da ESPN não batem com o placar — Atletico Madrid 2-3 Athletic Bilbao: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Athletic Bilbao 2-1 RCD Mallorca: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — RCD Mallorca 2-1 Getafe CF: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Recreativo Huelva 1-2 Deportivo La Coruna: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Malaga CF 1-1 Real Betis: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Recreativo Huelva 0-1 Racing Santander: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — UD Almeria 0-3 Espanyol Barcelona: ESPN 0-6 (descartados)

### 2009/10

- gols da ESPN não batem com o placar — Malaga CF 3-0 Atletico Madrid: ESPN 6-0 (descartados)

### 2010/11

- data diferente no ogol em 1 jogos (ex.: Villarreal CF x RCD Mallorca: base 2010-12-18, ogol 2010-12-19); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Real Sociedad, Wikipédia Levante UD); fica a da Wikipédia

### 2011/12

- a ESPN traz 0-0, sem gols, em dez jogos do Granada (agosto a janeiro); os placares da base são confirmados pelo ogol, pelo football-data e pelas tabelas. Esses jogos ficam sem autores de gols
- placar diferente na ESPN — Granada CF x Real Betis (2011-08-27): base 0-1, ESPN 0-0
- placar diferente na ESPN — Granada CF x Villarreal CF (2011-09-17): base 1-0, ESPN 0-0
- placar diferente na ESPN — Granada CF x CA Osasuna (2011-09-25): base 1-1, ESPN 0-0
- placar diferente na ESPN — Granada CF x FC Barcelona (2011-10-25): base 0-1, ESPN 0-0
- placar diferente na ESPN — Athletic Bilbao x Granada CF (2011-11-27): base 0-1, ESPN 0-0
- placar diferente na ESPN — Granada CF x Real Zaragoza (2011-12-04): base 1-0, ESPN 0-0
- placar diferente na ESPN — Getafe CF x Granada CF (2011-12-11): base 1-0, ESPN 0-0
- placar diferente na ESPN — Granada CF x Levante UD (2011-12-18): base 2-1, ESPN 0-0
- placar diferente na ESPN — Real Madrid x Granada CF (2012-01-07): base 5-1, ESPN 0-0
- placar diferente na ESPN — Espanyol Barcelona x Granada CF (2012-01-21): base 3-0, ESPN 0-0
- gols da ESPN não batem com o placar — Athletic Bilbao 3-0 Atletico Madrid: ESPN 4-0 (descartados)

### 2012/13

- sem ocorrências

### 2013/14

- sem ocorrências

### 2014/15

- Almería: 3 pontos a menos (punição da FIFA por dívida de transferência); a Wikipédia desconta, a tabela da RSSSF não
- o Elche (13º) foi rebaixado por dívidas com o fisco e o Eibar (18º) ficou na 1ª divisão: o Elche sai como rebaixado e o Eibar não
- placar diferente na ESPN — Malaga CF x Sevilla FC (2015-05-23): base 2-3, ESPN 2-2
- nota da RSSSF: NB: after the season, Elche were demoted because of extravagant tax debts; because of this, Eibar remain at the top level
- tabela publicada x jogos (RSSSF) — UD Almeria tabela [38, 8, 8, 22, 35, 64, 32] jogos [38, 8, 8, 22, 35, 64, 29]

### 2015/16

- sem ocorrências

### 2016/17

- sem ocorrências

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- sem ocorrências

### 2020/21

- sem ocorrências

### 2021/22

- gols da ESPN não batem com o placar — Espanyol Barcelona 1-2 Elche CF: ESPN 2-2 (descartados)

### 2022/23

- ESPN com 375 de 380 jogos (ex. sem ESPN: UD Almeria x Real Betis, 2023-02-11)

### 2023/24

- Granada CF x Athletic Bilbao: começou em 10/12/2023 e foi suspenso no 1º tempo (morte de um torcedor na arquibancada); completado em 11/12/2023

### 2024/25

- sem ocorrências

### 2025/26

- nota da RSSSF: NB: CD Arenteiro demoted to fifth level
- nota da RSSSF: NB: SD Tarazona demoted to fifth level

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_esp.py` (serve para todas as divisões espanholas): nome de exibição como o clube é conhecido no Brasil, cidade e país. "Athletic Club" já é o clube de São João del-Rei (MG): o de Bilbao fica "Athletic Bilbao".
- Clubes que o engsoccerdata separa ficam separados: CD Málaga (até 1992) e Málaga (de 1994); AD Almería (1971-1982) e Almería (UD, de 1989); Burgos (CF, 1946-1983) e Real Burgos (1983-1995).
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 61 códigos do ogol e 42 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv` (ex.: `ogol:Atlético Aviación`).

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. A RSSSF tem os autores de 2000/01 em diante (a ESPN já cobre) e o ogol tem a ficha de muitos jogos; fica como próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** idem.
- **Promoções (jogos de acesso e rebaixamento contra clubes da 2ª divisão):** ficam de fora (entram quando a 2ª divisão for coletada).
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
