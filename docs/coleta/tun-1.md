# Campeonato Tunisiano (1ª divisão) — coleta de dados

Gerado por `python coleta/tun-1/importar.py`. Pacote em `data/coleta/tun-1/pacote/`.

**Edições:** 109, uma por temporada, de 1907 a 2025/26, como na lista de campeões da RSSSF (`tunchamp.html`) e na Wikipédia em inglês. A era colonial entra (pesquisa de 24/11/2026): a contagem oficial usada na Tunísia inclui esses títulos (o "34º título" do Espérance em 2024/25 só fecha com o de 1941/42; o "14º" do Club Africain em 2025/26, com os de 1946/47 e 1947/48). Até 1920/21 era o campeonato da USFSA; de 1921/22 a 1954/55, da Liga da Tunísia, quase sempre com campeões regionais e uma final. Ficam de fora as temporadas sem competição (1909/10, as das guerras mundiais e 1942/43 e 1943/44); 1951/52 foi abandonado e entra sem campeão. A Wikipédia lista um título do Racing Club de Tunis em 1909/10, que a RSSSF não traz: fica de fora.

**Fora do pacote:** a Copa da Tunísia e as outras copas, a 2ª divisão e os jogos de promoção.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/tun-1/rsssf/`: base dos jogos de 1996/97 a 2024/25; a tabela de confrontos de 1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e de 1987/88 a 1995/96, sem datas; a lista de tabelas finais `tunhist.html`, de 1955/56 a 2002/03; na era colonial, as finais que a página traz); ogol (base dos jogos de 2025/26; nos outros anos, conferência, rodada e data); Wikipédia em inglês (listas de campeões e de artilheiros e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga tunisiana.

**Clubes:** o nome pelo qual o clube é conhecido (Espérance de Tunis, Club Africain, Étoile du Sahel, CS Sfaxien...). Mesmo clube com outro nome é um só (Railway Sports de Sfax = Sfax Railways Sports; US Ferryville = USM Bourguiba; Olympique Tunis = US Musulmane Olympique). Regras em `coleta/tun-1/clubes_tun.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. "A bt B" (venceu, sem placar conhecido) entra como vitória sem placar. Pontos como as tabelas contam: 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0 desde 1995/96 (o `ajuste_pontos` já usa o sistema de cada ano).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1907 | 4 | 2 (2) | 4 | 0 | 0 / 0 | Racing Club de Tunis | jogos incompletos (só a final do campeonato) |
| 1908/09 | 3 | 2 (2) | 6 | 0 | 0 / 0 | Racing Club de Tunis | jogos incompletos (só a final do campeonato) |
| 1910/11 | 2 | 1 (1) | 2 | 0 | 0 / 0 | Racing Club de Tunis | jogos incompletos (só a final do campeonato) |
| 1911/12 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Club de Ferryville | sem jogos (só o campeão) |
| 1912/13 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Club de Ferryville | sem jogos (só o campeão) |
| 1913/14 | 3 | 1 (1) | 2 | 0 | 0 / 0 | Racing Club de Tunis | jogos incompletos (só a final do campeonato) |
| 1919/20 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Club de Tunis | sem jogos (só o campeão) |
| 1920/21 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Club de Tunis | sem jogos (só o campeão) |
| 1921/22 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Club de Tunis | sem jogos (só o campeão) |
| 1922/23 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Stade Gaulois | sem jogos (só o campeão) |
| 1923/24 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Stade Gaulois | sem jogos (só o campeão) |
| 1924/25 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Club de Tunis | sem jogos (só o campeão) |
| 1925/26 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Club de Tunis | sem jogos (só o campeão) |
| 1926/27 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Stade Gaulois | sem jogos (só o campeão) |
| 1927/28 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Club de Tunis | sem jogos (só o campeão) |
| 1928/29 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Avant-Garde de Tunis | sem jogos (só o campeão) |
| 1929/30 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Tunisienne | sem jogos (só o campeão) |
| 1930/31 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Tunisienne | sem jogos (só o campeão) |
| 1931/32 | 2 | 2 (2) | 10 | 0 | 0 / 0 | Italia de Tunis | jogos incompletos (só a final do campeonato) |
| 1932/33 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Tunisienne | sem jogos (só o campeão) |
| 1933/34 | 2 | 1 (1) | 0 | 0 | 0 / 0 | Sfax Railways Sports | jogos incompletos (só a final do campeonato) |
| 1934/35 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Italia de Tunis | sem jogos (só o campeão) |
| 1935/36 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Italia de Tunis | sem jogos (só o campeão) |
| 1936/37 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Italia de Tunis | sem jogos (só o campeão) |
| 1937/38 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Savoia de La Goulette | sem jogos (só o campeão) |
| 1938/39 | 2 | 2 (2) | 6 | 0 | 0 / 0 | CS Gabésien | jogos incompletos (só a final do campeonato) |
| 1941/42 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só o campeão) |
| 1944/45 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CA Bizertin | sem jogos (só o campeão) |
| 1945/46 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CA Bizertin | sem jogos (só o campeão) |
| 1946/47 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só o campeão) |
| 1947/48 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só o campeão) |
| 1948/49 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CA Bizertin | sem jogos (só o campeão) |
| 1949/50 | 12 | 4 (4) | 24 | 0 | 0 / 0 | Étoile du Sahel | jogos incompletos (só os resultados conhecidos) |
| 1950/51 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CS Hammam-Lif | sem jogos (só o campeão) |
| 1951/52 | 12 | 0 (0) | 0 | 0 | 0 / 0 | — | temporada não terminada |
| 1952/53 | 6 | 5 (5) | 11 | 0 | 0 / 0 | Sfax Railways Sports | jogos incompletos (cinco grupos regionais sem jogos; só o mata-mata final) |
| 1953/54 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CS Hammam-Lif | sem jogos (só o campeão) |
| 1954/55 | 1 | 0 (0) | 0 | 0 | 0 / 0 | CS Hammam-Lif | sem jogos (só o campeão) |
| 1955/56 | 12 | 0 (0) | 0 | 0 | 0 / 0 | CS Hammam-Lif | sem jogos (só a tabela final) |
| 1956/57 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Stade Tunisien | sem jogos (só a tabela final) |
| 1957/58 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1958/59 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1959/60 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1960/61 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Stade Tunisien | sem jogos (só a tabela final) |
| 1961/62 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Stade Tunisien | sem jogos (só a tabela final) |
| 1962/63 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1963/64 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1964/65 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Stade Tunisien | sem jogos (só a tabela final) |
| 1965/66 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1966/67 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1967/68 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Sfax Railways Sports | sem jogos (só a tabela final) |
| 1968/69 | 14 | 182 (182) | 349 | 0 | 0 / 1 | CS Sfaxien | pontos corridos |
| 1969/70 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1970/71 | 13 | 156 (156) | 325 | 0 | 1 / 0 | CS Sfaxien | pontos corridos |
| 1971/72 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1972/73 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1973/74 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1974/75 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1975/76 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1976/77 | 14 | 0 (0) | 0 | 0 | 0 / 0 | JS Kairouan | sem jogos (só a tabela final) |
| 1977/78 | 14 | 182 (182) | 414 | 0 | 0 / 1 | CS Sfaxien | pontos corridos |
| 1978/79 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1979/80 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Club Africain | sem jogos (só a tabela final) |
| 1980/81 | 14 | 182 (182) | 371 | 0 | 0 / 1 | CS Sfaxien | pontos corridos |
| 1981/82 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1982/83 | 14 | 182 (182) | 359 | 0 | 0 / 1 | CS Sfaxien | pontos corridos |
| 1983/84 | 14 | 0 (0) | 0 | 0 | 0 / 0 | CA Bizertin | sem jogos (só a tabela final) |
| 1984/85 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Espérance de Tunis | sem jogos (só a tabela final) |
| 1985/86 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1986/87 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Étoile du Sahel | sem jogos (só a tabela final) |
| 1987/88 | 14 | 182 (182) | 358 | 0 | 0 / 1 | Espérance de Tunis | pontos corridos |
| 1988/89 | 14 | 182 (182) | 391 | 0 | 0 / 1 | Espérance de Tunis | pontos corridos |
| 1989/90 | 14 | 181 (182) | 371 | 0 | 0 / 1 | Club Africain | pontos corridos |
| 1990/91 | 14 | 182 (182) | 413 | 0 | 0 / 1 | Espérance de Tunis | pontos corridos |
| 1991/92 | 14 | 182 (182) | 390 | 0 | 1 / 0 | Club Africain | pontos corridos |
| 1992/93 | 14 | 182 (182) | 408 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 1993/94 | 14 | 182 (182) | 431 | 0 | 0 / 1 | Espérance de Tunis | pontos corridos |
| 1994/95 | 14 | 182 (182) | 432 | 0 | 0 / 1 | CS Sfaxien | pontos corridos |
| 1995/96 | 14 | 182 (182) | 407 | 0 | 1 / 0 | Club Africain | pontos corridos |
| 1996/97 | 14 | 182 (182) | 402 | 0 | 1 / 0 | Étoile du Sahel | pontos corridos |
| 1997/98 | 14 | 182 (182) | 399 | 0 | 2 / 0 | Espérance de Tunis | pontos corridos |
| 1998/99 | 16 | 224 (224) | 512 | 0 | 4 / 0 | Espérance de Tunis | 2 grupos + grupos do título e do rebaixamento |
| 1999/00 | 12 | 132 (132) | 304 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2000/01 | 12 | 132 (132) | 296 | 4 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2001/02 | 12 | 132 (132) | 285 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2002/03 | 12 | 132 (132) | 298 | 0 | 2 / 0 | Espérance de Tunis | pontos corridos |
| 2003/04 | 12 | 132 (132) | 285 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2004/05 | 14 | 182 (182) | 382 | 372 | 1 / 0 | CS Sfaxien | pontos corridos |
| 2005/06 | 14 | 183 (183) | 356 | 0 | 3 / 0 | Espérance de Tunis | pontos corridos |
| 2006/07 | 14 | 182 (182) | 386 | 17 | 1 / 0 | Étoile du Sahel | pontos corridos |
| 2007/08 | 14 | 186 (186) | 374 | 2 | 1 / 0 | Club Africain | pontos corridos |
| 2008/09 | 14 | 182 (182) | 358 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2009/10 | 14 | 182 (182) | 416 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2010/11 | 14 | 182 (182) | 402 | 376 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2011/12 | 16 | 240 (240) | 560 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2012/13 | 16 | 130 (130) | 276 | 0 | 3 / 0 | CS Sfaxien | 2 grupos + jogos de classificação + fase final |
| 2013/14 | 16 | 240 (240) | 440 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2014/15 | 16 | 240 (240) | 498 | 0 | 1 / 0 | Club Africain | pontos corridos |
| 2015/16 | 16 | 240 (240) | 521 | 0 | 1 / 0 | Étoile du Sahel | pontos corridos |
| 2016/17 | 16 | 198 (198) | 393 | 0 | 4 / 0 | Espérance de Tunis | 2 grupos + grupos do título e do rebaixamento |
| 2017/18 | 14 | 182 (182) | 388 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2018/19 | 14 | 182 (182) | 377 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2019/20 | 14 | 182 (182) | 390 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2020/21 | 14 | 182 (182) | 376 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2021/22 | 16 | 158 (158) | 271 | 0 | 4 / 0 | Espérance de Tunis | 2 grupos + jogos de classificação + grupos do título e do rebaixamento + desempate |
| 2022/23 | 16 | 198 (198) | 406 | 0 | 4 / 0 | Étoile du Sahel | 2 grupos + grupos do título e do rebaixamento |
| 2023/24 | 14 | 171 (171) | 324 | 0 | 4 / 0 | Espérance de Tunis | 2 grupos + grupos do título e do rebaixamento + desempate |
| 2024/25 | 16 | 241 (241) | 488 | 0 | 1 / 0 | Espérance de Tunis | pontos corridos |
| 2025/26 | 16 | 240 (240) | 415 | 0 | 1 / 0 | Club Africain | pontos corridos |

## Conferência e correções, edição a edição

### 1907

- jogos incompletos (só a final do campeonato)

### 1908/09

- jogos incompletos (só a final do campeonato)

### 1910/11

- jogos incompletos (só a final do campeonato)

### 1911/12

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1912/13

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1913/14

- jogos incompletos (só a final do campeonato)

### 1919/20

- a RSSSF traz só o campeão da Série 1 (e jogos da Série 2, a 2ª divisão)

### 1920/21

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1921/22

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1922/23

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1923/24

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1924/25

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1925/26

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1926/27

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1927/28

- a RSSSF traz só o campeão (a tabela da página é da 3ª divisão)

### 1928/29

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1929/30

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1930/31

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1931/32

- jogos incompletos (só a final do campeonato)

### 1932/33

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1933/34

- jogos incompletos (só a final do campeonato)
- W.O./pontos para o mandante — Sfax Railways Sports Italia de Tunis (s/d): bt

### 1934/35

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1935/36

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1936/37

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1937/38

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1938/39

- jogos incompletos (só a final do campeonato)

### 1941/42

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1944/45

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1945/46

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1946/47

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1947/48

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1948/49

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1949/50

- jogos incompletos (só os resultados conhecidos)

### 1950/51

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1951/52

- temporada não terminada: abandonada em janeiro de 1952 pela agitação política; nenhum título foi dado e todos os clubes ficaram na 1ª divisão (a tabela é a do abandono)

### 1952/53

- jogos incompletos (cinco grupos regionais sem jogos; só o mata-mata final)
- campeonato boicotado pelos clubes nacionalistas e muçulmanos
- W.O./pontos para o mandante — US Musulmane Olympique USM Bourguiba (s/d): bt
- W.O./pontos para o mandante — FC Djerissa Vaillante-Jeunesse de Hammam-Lif (s/d): bt

### 1953/54

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1954/55

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1955/56

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1956/57

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1957/58

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1958/59

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1959/60

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1960/61

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1961/62

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1962/63

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1963/64

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1964/65

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1965/66

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1966/67

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1967/68

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1968/69

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- jogo acrescentado à mão — Sfax Railways Sports None-None AS Marsa: nota da página: "NB: SRS-ASM was awarded a win to ASM"
- tabela publicada x jogos — tunhist:333: CS Hammam-Lif tabela [26, 7, 9, 10, 18, 24] jogos [26, 6, 9, 11, 17, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:333: Stade Sportif Sfaxien tabela [26, 6, 7, 13, 24, 36] jogos [26, 7, 7, 12, 25, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: CS Hammam-Lif 1-2 Stade Sportif Sfaxien (None, tun69:41:12); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Stade Sportif Sfaxien 2-1 CS Hammam-Lif (None, tun69:46:7); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1969/70

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1970/71

- jogo acrescentado à mão — US Monastir None-None Étoile du Sahel: nota da página: "NB: USMo-ESS was awarded a win to USMo"

### 1971/72

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1972/73

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1973/74

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1974/75

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1975/76

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1976/77

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1977/78

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- jogo acrescentado à mão — CO Transports None-None SA Menzel Bourguiba: nota da página: "NB: COT-SAMB was awarded a win to COT"
- tabela publicada x jogos — tunhist:565: CS Sfaxien tabela [26, 17, 7, 2, 41, 12] jogos [26, 17, 7, 2, 41, 11] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:565: Étoile du Sahel tabela [26, 13, 7, 6, 44, 25] jogos [26, 13, 7, 6, 43, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:565: Sfax Railways Sports tabela [26, 9, 11, 6, 31, 29] jogos [26, 8, 11, 7, 29, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:565: Espérance de Tunis tabela [26, 10, 7, 9, 34, 33] jogos [26, 11, 7, 8, 34, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: CS Sfaxien 2-0 Étoile du Sahel (None, tun78:36:2); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Sfax Railways Sports 0-1 Espérance de Tunis (None, tun78:39:5); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Espérance de Tunis 1-0 Sfax Railways Sports (None, tun78:41:3); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1978/79

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1979/80

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1980/81

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- jogo acrescentado à mão — CS Sfaxien None-None US Monastir: nota da página: "NB: CSS-USMo was awarded a win to CSS"
- tabela publicada x jogos — tunhist:637: Étoile du Sahel tabela [26, 12, 9, 5, 32, 20] jogos [26, 11, 9, 6, 31, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:637: Stade Tunisien tabela [26, 11, 6, 9, 33, 27] jogos [26, 11, 6, 9, 33, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:637: AS Marsa tabela [26, 7, 9, 10, 25, 26] jogos [26, 7, 9, 10, 23, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:637: Sfax Railways Sports tabela [26, 5, 10, 11, 19, 29] jogos [26, 6, 10, 10, 20, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Sfax Railways Sports 1-0 Étoile du Sahel (None, tun81:46:3); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Stade Tunisien 3-0 AS Marsa (None, tun81:42:7); com 3-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1981/82

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1982/83

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:685: US Monastir tabela [26, 8, 8, 10, 20, 23] jogos [26, 8, 7, 11, 20, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:685: Océan Club de Kerkennah tabela [26, 3, 12, 11, 11, 33] jogos [26, 4, 11, 11, 12, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Océan Club de Kerkennah 1-0 US Monastir (None, tun83:48:9); com 0-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1983/84

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1984/85

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1985/86

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1986/87

- a RSSSF traz só a tabela final (lista de tabelas finais)

### 1987/88

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:817: CO Transports tabela [26, 16, 7, 3, 32, 12] jogos [26, 16, 7, 3, 32, 13] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:817: CS Hammam-Lif tabela [26, 5, 13, 8, 17, 22] jogos [26, 5, 13, 8, 18, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1988/89

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:846: Club Africain tabela [26, 13, 7, 6, 40, 28] jogos [26, 13, 7, 6, 39, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:846: Étoile du Sahel tabela [26, 12, 8, 6, 37, 22] jogos [26, 12, 8, 6, 37, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:846: Olympique Béja tabela [26, 10, 3, 13, 22, 29] jogos [26, 10, 3, 13, 21, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:846: US Monastir tabela [26, 6, 13, 7, 23, 29] jogos [26, 6, 13, 7, 22, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Club Africain 0-2 Étoile du Sahel (None, tun89:40:6); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Étoile du Sahel 3-0 Club Africain (None, tun89:43:3); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Olympique Béja 1-0 US Monastir (None, tun89:47:13); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: US Monastir 0-1 Olympique Béja (None, tun89:50:10); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1989/90

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:875: Espérance de Tunis tabela [26, 16, 9, 1, 44, 11] jogos [25, 15, 9, 1, 41, 11] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:875: CS Hammam-Lif tabela [26, 10, 5, 11, 17, 20] jogos [26, 9, 6, 11, 16, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:875: US Monastir tabela [26, 6, 6, 14, 25, 35] jogos [26, 6, 6, 14, 24, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:875: CS Cheminots tabela [26, 4, 9, 13, 18, 41] jogos [26, 4, 9, 13, 18, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:875: AS Kasserine tabela [26, 4, 8, 14, 16, 36] jogos [25, 4, 9, 12, 18, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1990/91

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:901: CS Hammam-Lif tabela [26, 8, 7, 11, 21, 21] jogos [26, 9, 7, 10, 23, 22] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — tunhist:901: AS Oued Ellil tabela [26, 3, 9, 14, 17, 36] jogos [26, 2, 9, 15, 18, 38] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1991/92

- sem ocorrências

### 1992/93

- sem ocorrências

### 1993/94

- a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:973: Étoile du Sahel tabela [26, 13, 8, 5, 36, 17] jogos [26, 12, 8, 6, 35, 18] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:973: Olympique Béja tabela [26, 7, 10, 9, 21, 24] jogos [26, 7, 11, 8, 22, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:973: Océan Club de Kerkennah tabela [26, 7, 7, 12, 34, 46] jogos [26, 6, 8, 12, 33, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — tunhist:973: CS Hammam-Lif tabela [26, 7, 6, 13, 12, 24] jogos [26, 8, 6, 12, 13, 23] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:973: US Monastir tabela [26, 5, 7, 14, 23, 43] jogos [26, 4, 9, 13, 23, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: CS Hammam-Lif 2-1 Étoile du Sahel (None, tun94:38:6); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1994/95

- a tabela de confrontos da página não fecha com a tabela final em 13 dos 14 clubes (somada à parte, sem o leitor, dá os mesmos números): erro da própria página, sem terceira fonte; nenhum placar foi mudado e a classificação é a tabela publicada
- tabela publicada x jogos — tunhist:997: CS Sfaxien tabela [26, 17, 4, 5, 40, 16] jogos [26, 16, 4, 6, 38, 18] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Espérance de Tunis tabela [26, 16, 5, 5, 52, 23] jogos [26, 17, 4, 5, 52, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Club Africain tabela [26, 13, 7, 6, 34, 23] jogos [26, 13, 8, 5, 34, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Olympique Béja tabela [26, 10, 6, 10, 31, 28] jogos [26, 10, 5, 11, 31, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Olympique du Kef tabela [26, 9, 7, 10, 29, 32] jogos [26, 9, 7, 10, 28, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: ES Zarzis tabela [26, 7, 9, 10, 19, 31] jogos [26, 7, 8, 11, 18, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: AS Marsa tabela [26, 8, 7, 11, 31, 44] jogos [26, 9, 6, 11, 27, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Stade Tunisien tabela [26, 7, 8, 11, 30, 36] jogos [26, 7, 8, 11, 27, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: CA Bizertin tabela [26, 8, 6, 12, 22, 33] jogos [26, 8, 5, 13, 22, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: JS Kairouan tabela [26, 8, 6, 12, 22, 30] jogos [26, 9, 4, 13, 22, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: CS Hammam-Lif tabela [26, 8, 4, 14, 40, 47] jogos [26, 8, 4, 14, 38, 46] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — tunhist:997: Océan Club de Kerkennah tabela [26, 5, 8, 13, 23, 36] jogos [26, 4, 9, 13, 22, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — tunhist:997: Sfax Railways Sports tabela [26, 7, 4, 15, 21, 39] jogos [26, 9, 3, 14, 24, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Club Africain 1-1 ES Zarzis (None, tun95:36:6); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Océan Club de Kerkennah 1-1 Club Africain (None, tun95:45:3); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1995/96

- sem ocorrências

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- sem ocorrências

### 1999/00

- sem ocorrências

### 2000/01

- decidido fora de campo — Espérance de Tunis AS Djerba (2001-04-04): awarded 0-2; originally 6-0

### 2001/02

- sem ocorrências

### 2002/03

- decidido fora de campo — Olympique Béja Club Africain (2002-09-29): awarded 2-0; abandoned at 2-1 in 83'

### 2003/04

- sem ocorrências

### 2004/05

- decidido fora de campo — Olympique Béja EOG Kram (2004-08-27): awarded 0-2; originally 2-1;
- decidido fora de campo — EOG Kram EGS Gafsa (2005-03-06): awarded 0-2; originally 1-0;
- decidido fora de campo — CA Bizertin ES Zarzis (2005-04-17): awarded 0-2; originally 2-1, Bizerte
- decidido fora de campo — Olympique Béja Club Africain (2005-04-24): awarded 0-2; abandoned at 0-1 in 85'

### 2005/06

- ogol: 182 jogos casados (edição 34041 do ogol, 182 jogos)
- abandonado/suspenso, sem valer — US Monastir Jendouba Sport (2005-08-28): 0-0, abd 50' due to the rain; to replay

### 2006/07

- ogol: 182 jogos casados (edição 34040 do ogol, 182 jogos)
- corrigido — CS Hammam-Lif x US Monastir (2007-01-21): 2-0 dado ao CS Hammam-Lif (jogador irregular do US Monastir); em campo 0-0
- placar diferente no ogol — CA Bizertin x Olympique Béja (2007-04-15): RSSSF 4-2, ogol 4-3; fica o da RSSSF
- decidido fora de campo — CS Hammam-Lif US Monastir (2007-01-21): 2-0 dado ao CS Hammam-Lif: o US Monastir escalou jogador irregular

### 2007/08

- ogol: 74 jogos casados (edição 2103 do ogol, 182 jogos)
- placar diferente no ogol — Espérance de Tunis x CA Bizertin (2007-12-02): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- abandonado/suspenso, sem valer — Espérance de Tunis Stade Gabésien (2007-10-13): abandoned at 1-0 in 24' due to rain
- abandonado/suspenso, sem valer — CS Hammam-Lif CA Bizertin (2007-10-13): abandoned at 0-0 in 48' due to rain
- abandonado/suspenso, sem valer — AS Marsa EGS Gafsa (2007-10-13): abandoned at 1-1 in 34' due to rain
- decidido fora de campo — CS Sfaxien Espérance de Tunis (2009-12-29): awarded 0-2; abandoned at 0-2 in 85',
- abandonado/suspenso, sem valer — Olympique Béja ES Zarzis (2009-12-30): abandoned at 0-0 in 19' due to rain

### 2008/09

- ogol: 175 jogos casados (edição 2388 do ogol, 182 jogos)
- placar diferente no ogol — CS Sfaxien x Jendouba Sport (2008-10-22): RSSSF 3-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — AS Kasserine x EGS Gafsa (2009-03-01): RSSSF 1-1, ogol 0-0; fica o da RSSSF

### 2009/10

- ogol: 180 jogos casados (edição 8882 do ogol, 182 jogos)
- placar diferente no ogol — AS Kasserine x ES Hammam-Sousse (2009-11-01): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — JS Kairouan x CS Hammam-Lif (2009-11-01): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- decidido fora de campo — AS Kasserine EGS Gafsa (2010-05-02): awarded 0-2; abandoned at 0-1 in 79'

### 2010/11

- ogol: 70 jogos casados (edição 15782 do ogol, 182 jogos)
- decidido fora de campo — AS Marsa Stade Tunisien (2012-06-29): awarded 0-2; actual score 1-1

### 2011/12

- ogol: 8 jogos casados (edição 33960 do ogol, 240 jogos)
- decidido fora de campo — Club Africain AS Gabès (2013-05-23): awarded 0-2
- decidido fora de campo — Stade Tunisien Club Africain (2013-06-03): awarded 2-0

### 2012/13

- ogol: 56 jogos casados (edição 54917 do ogol, 125 jogos)
- decidido fora de campo — Club Africain Olympique du Kef (2013-04-14): awarded 2-0, forfait Kef
- decidido fora de campo — Stade Gabésien CS Sfaxien (2014-03-03): awarded 0-2; abandoned at 2-1 in 75'

### 2013/14

- ogol: 240 jogos casados (edição 59753 do ogol, 240 jogos)
- decidido fora de campo — LPS Tozeur AS Marsa (2013-12-29): awarded 0-2; abandoned at 0-1 due to crowd
- decidido fora de campo — AS Marsa CS Sfaxien (2014-04-06): awarded 0-2, originally 0-0;

### 2014/15

- ogol: 240 jogos casados (edição 70646 do ogol, 240 jogos)
- data diferente no ogol — EGS Gafsa x CS Sfaxien: RSSSF 2014-12-03, ogol 2014-11-26; fica a da RSSSF
- data diferente no ogol — US Monastir x AS Marsa: RSSSF 2015-05-23, ogol 2015-06-02; fica a da RSSSF
- decidido fora de campo — CS Hammam-Lif Étoile du Sahel (2015-03-08): awarded 2-0, Etoile du Sahel dns; Etoile 1 point deducted

### 2015/16

- ogol: 240 jogos casados (edição 88961 do ogol, 240 jogos)
- placar diferente no ogol — ES Métlaoui x Étoile du Sahel (2015-09-16): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- data diferente no ogol — Stade Gabésien x EO Sidi Bouzid: RSSSF 2016-05-15, ogol 2016-05-25; fica a da RSSSF
- data diferente no ogol — Espérance de Tunis x Étoile du Sahel: RSSSF 2016-05-15, ogol 2016-05-25; fica a da RSSSF
- decidido fora de campo — CA Bizertin JS Kairouan (2015-10-16): awarded 2-0, originally 1-1; Kairouan used
- decidido fora de campo — EO Sidi Bouzid Espérance de Tunis (2015-12-16): awarded 0-2; abandoned at 0-2
- decidido fora de campo — AS Kasserine AS Marsa (2016-05-08): awarded 0-2; originally 3-1; AS Kasserine
- decidido fora de campo — ES Zarzis JS Kairouan (2016-05-15): awarded 0-2; originally 0-0; Espérance de Zarzis
- decidido fora de campo — ES Métlaoui Stade Tunisien (2016-05-29): awarded 2-0, Stade dns
- decidido fora de campo — Stade Tunisien US Ben Guerdane (2016-06-09): awarded 0-2, Stade dns
- decidido fora de campo — CS Hammam-Lif Stade Tunisien (2016-06-12): awarded 2-0, Stade dns

### 2016/17

- ogol: 198 jogos casados (edição 99237 do ogol, 198 jogos)

### 2017/18

- ogol: 182 jogos casados (edição 113009 do ogol, 182 jogos)
- data diferente no ogol — US Ben Guerdane x Stade Tunisien: RSSSF 2017-10-15, ogol 2017-10-22; fica a da RSSSF
- data diferente no ogol — CO Médenine x US Monastir: RSSSF 2017-10-14, ogol 2017-10-22; fica a da RSSSF
- data diferente no ogol — JS Kairouan x CA Bizertin: RSSSF 2017-10-14, ogol 2017-10-22; fica a da RSSSF
- data diferente no ogol — CS Sfaxien x ES Zarzis: RSSSF 2017-10-14, ogol 2017-10-22; fica a da RSSSF
- data diferente no ogol — Stade Gabésien x AS Gabès: RSSSF 2017-10-15, ogol 2017-10-22; fica a da RSSSF
- data diferente no ogol — CS Sfaxien x CO Médenine: RSSSF 2017-11-16, ogol 2017-11-12; fica a da RSSSF
- decidido fora de campo — ES Zarzis CA Bizertin (2017-08-20): awarded 0-2, originally 1-0
- decidido fora de campo — ES Zarzis US Ben Guerdane (2017-12-28): awarded 0-2; abandoned at 0-1 in 45', Zarzis walked off
- decidido fora de campo — US Monastir Espérance de Tunis (2018-03-02): awarded 0-2; abandoned at 0-1 in 86'

### 2018/19

- ogol: 77 jogos casados (edição 125633 do ogol, 182 jogos)
- decidido fora de campo — US Monastir ES Métlaoui (2018-11-25): awarded 0-2; abandoned at 0-1 in 45'
- decidido fora de campo — Stade Gabésien US Ben Guerdane (2020-05-18): awarded 0-2, abandoned at 1-0 in 85' after
- decidido fora de campo — Stade Tunisien Étoile du Sahel (2020-05-30): awarded 0-2; abandoned at 0-1 in 42' due

### 2019/20

- ogol: 28 jogos casados (edição 136688 do ogol, 182 jogos)

### 2020/21

- ogol: 26 jogos casados (edição 148901 do ogol, 180 jogos)

### 2021/22

- ogol: 154 jogos casados (edição 159276 do ogol, 156 jogos)

### 2022/23

- ogol: 32 jogos casados (edição 168524 do ogol, 198 jogos)
- decidido fora de campo — Stade Tunisien Étoile du Sahel (2024-02-02): awarded 0-2; abandoned at 0-1 in 69' due
- decidido fora de campo — US Ben Guerdane CS Sfaxien (2024-04-16): awarded 2-0; originally 1-2, Sfaxien
- decidido fora de campo — Olympique Béja Club Africain (2024-05-31): awarded 0-2; abandoned at 0-0

### 2023/24

- ogol: 171 jogos casados (edição 176513 do ogol, 171 jogos)
- data diferente no ogol — US Monastir x CS Sfaxien: RSSSF 2024-05-31, ogol 2024-05-26; fica a da RSSSF
- data diferente no ogol — AS Solimane x AS Marsa: RSSSF 2024-06-14, ogol 2024-06-19; fica a da RSSSF

### 2024/25

- ogol: 103 jogos casados (edição 189100 do ogol, 240 jogos)
- decidido fora de campo — US Ben Guerdane Club Africain (2024-08-31): awarded 0-2, originally 2-2
- decidido fora de campo — ES Zarzis Stade Tunisien (2024-09-01): awarded 2-0, originally 1-1
- anulado — EGS Gafsa 1-1 Étoile du Sahel (2024-12-29): annulled; temporarily awarded 0-2
- decidido fora de campo — EGS Gafsa CS Sfaxien (2024-02-12): awarded 0-2, originally 0-1

### 2025/26

- três resultados dados fora de campo (2-0), pelas notas da tabela de confrontos da Wikipédia; com eles a tabela da RSSSF fecha
- a RSSSF só traz as tabelas: os jogos vêm do calendário do ogol
- ogol: base dos jogos (239 jogos)
- jogo acrescentado à mão — US Monastir 0-2 CS Sfaxien: resultado dado fora de campo: 2-0 para o CS Sfaxien (tumulto da torcida do US Monastir)
- corrigido — CA Bizertin x Club Africain (2025-08-27): 2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin (Wikipédia); em campo 0-1
- corrigido — Stade Tunisien x Olympique Béja (2026-02-13): 2-0 dado ao Olympique Béja porque o Stade Tunisien pôs 5 estrangeiros em campo ao mesmo tempo (Wikipédia); em campo 3-2
- decidido fora de campo — CA Bizertin 0-1 Club Africain (2025-08-27): 2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin
- decidido fora de campo — Stade Tunisien 3-2 Olympique Béja (2026-02-13): 2-0 dado ao Olympique Béja: o Stade Tunisien pôs 5 estrangeiros em campo ao mesmo tempo

