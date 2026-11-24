# Campeonato Marroquino (1ª divisão) — coleta de dados

Gerado por `python coleta/mar-1/importar.py`. Pacote em `data/coleta/mar-1/pacote/`.

**Edições:** 110, uma por temporada, de 1915/16 a 2025/26, como na lista de campeões da RSSSF (`marochamp.html`, 39 títulos antes da independência e 70 depois) e na Wikipédia em inglês. A era colonial entra (pesquisa de 24/11/2026): a federação marroquina conta esses títulos no palmarès (o site da FRMF, em 2015: "18º título do WAC desde 1948", 5 antes de 1956), e a RSSSF, a Wikipédia e os clubes também. Até 1921/22 era o campeonato da USFSA; de 1922/23 a 1954/55, da Liga do Marrocos, às vezes em liga única, às vezes em ligas regionais com mata-mata nacional. 1942/43 foi abandonado (desembarque aliado) e entra sem campeão; 1955/56 não teve competição e fica de fora.

**Fora do pacote:** a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos, que nenhuma lista de títulos conta), a Coupe du Trône e as outras copas, a 2ª divisão e os jogos de promoção.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/mar-1/rsssf/`: base dos jogos de 1995/96 a 2024/25, com rodadas, datas e, em parte dos anos, autores dos gols; a tabela de confrontos de 1956/57 a 1967/68, 1980/81, 1989/90 e 1990/91, sem datas; nos outros anos, a tabela final ou a classificação incompleta; na era colonial, os jogos que a página traz); ogol (base dos jogos de 2010/11, 2011/12 e 2025/26; de 2004/05 em diante, conferência, rodada e data; antes de 2004/05 não tem os jogos); Wikipédia em inglês (lista de campeões, com vice e artilheiro, e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga marroquina.

**Clubes:** o nome pelo qual o clube é conhecido (Wydad Casablanca, Raja Casablanca, FAR Rabat, RS Berkane...). Mesmo clube com outro nome é um só (Racing Casablanca = Racing AC = ADM Casablanca, como a RSSSF conta os títulos; AS Salé = SA Salé = Sporting Salé). Regras em `coleta/mar-1/clubes_mar.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada pela RSSSF (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. "A bt B" (venceu, sem placar conhecido) entra como vitória sem placar. Autores dos gols só entram quando a soma bate com o placar. Pontos: 3-2-1 (vitória, empate, derrota) de 1933/34 a 1994/95, como as tabelas contam (o `ajuste_pontos` já usa esse sistema); 3-1-0 desde 1995/96.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1915/16 | 8 | 0 (0) | 0 | 0 | 0 / 0 | CA Marocain | sem jogos (só a classificação incompleta) |
| 1916/17 | 6 | 9 (9) | 34 | 0 | 0 / 0 | US Marocaine | jogos incompletos (só os resultados conhecidos e a final) |
| 1917/18 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Marocaine | sem jogos (só o campeão) |
| 1918/19 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Marocaine | sem jogos (só o campeão) |
| 1919/20 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Marocaine | sem jogos (só o campeão) |
| 1920/21 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olympique Marocain | sem jogos (só o campeão) |
| 1921/22 | 1 | 0 (0) | 0 | 0 | 0 / 0 | USD Meknès | sem jogos (só o campeão) |
| 1922/23 | 4 | 3 (3) | 3 | 0 | 0 / 0 | Olympique Marocain | jogos incompletos (ligas regionais sem jogos; só as semifinais e a final) |
| 1923/24 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Olympique Marocain | sem jogos (só o campeão) |
| 1924/25 | 2 | 1 (1) | 3 | 0 | 0 / 0 | US Fès | jogos incompletos (ligas regionais sem jogos; só a final) |
| 1925/26 | 1 | 0 (0) | 0 | 0 | 0 / 0 | US Fès | sem jogos (só o campeão) |
| 1926/27 | 1 | 0 (0) | 0 | 0 | 0 / 0 | USA Casablanca | sem jogos (só o campeão) |
| 1927/28 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Stade Marocain | sem jogos (só o campeão) |
| 1928/29 | 2 | 1 (1) | 0 | 0 | 0 / 0 | USA Casablanca | jogos incompletos (só a final) |
| 1929/30 | 12 | 12 (12) | 39 | 0 | 0 / 0 | Olympique Marocain | jogos incompletos (ligas regionais com poucos jogos; o mata-mata final completo) |
| 1930/31 | 6 | 6 (6) | 20 | 0 | 0 / 0 | Stade Marocain | jogos incompletos (só o mata-mata final) |
| 1931/32 | 14 | 11 (11) | 47 | 0 | 0 / 0 | US Marocaine | jogos incompletos (dois grupos com os resultados conhecidos e a final) |
| 1932/33 | 8 | 29 (29) | 110 | 0 | 0 / 0 | US Marocaine | jogos incompletos (resultados conhecidos; classificação em 20/02 com jogos e pontos) |
| 1933/34 | 10 | 61 (61) | 223 | 0 | 0 / 1 | US Marocaine | pontos corridos |
| 1934/35 | 8 | 55 (55) | 213 | 0 | 1 / 0 | US Marocaine | pontos corridos |
| 1935/36 | 8 | 58 (58) | 186 | 0 | 1 / 0 | Olympique Marocain | pontos corridos + desempate + mata-mata |
| 1936/37 | 8 | 57 (57) | 235 | 0 | 1 / 0 | Olympique Marocain | pontos corridos + desempate |
| 1937/38 | 8 | 57 (57) | 216 | 0 | 1 / 0 | US Marocaine | pontos corridos + desempate |
| 1938/39 | 10 | 90 (90) | 340 | 0 | 1 / 0 | US Marocaine | pontos corridos |
| 1939/40 | 7 | 7 (7) | 19 | 1 | 0 / 0 | US Marocaine | jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional) |
| 1940/41 | 9 | 8 (8) | 24 | 0 | 0 / 0 | US Marocaine | jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional) |
| 1941/42 | 10 | 91 (91) | 307 | 0 | 0 / 1 | US Marocaine | pontos corridos |
| 1942/43 | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | temporada não terminada |
| 1943/44 | 16 | 25 (25) | 91 | 0 | 0 / 0 | Stade Marocain | jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional) |
| 1944/45 | 20 | 39 (39) | 134 | 0 | 0 / 0 | Racing Casablanca | jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional) |
| 1945/46 | 13 | 15 (15) | 59 | 0 | 0 / 0 | US Marocaine | jogos incompletos (ligas regionais quase sem jogos; o mata-mata nacional completo) |
| 1946/47 | 14 | 186 (186) | 601 | 0 | 1 / 0 | USA Casablanca | pontos corridos + desempate |
| 1947/48 | 10 | 90 (90) | 306 | 0 | 0 / 1 | Wydad Casablanca | pontos corridos |
| 1948/49 | 12 | 82 (82) | 268 | 0 | 0 / 0 | Wydad Casablanca | jogos incompletos (as rodadas que a página traz e outros jogos do WAC; classificação só com pontos) |
| 1949/50 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a classificação incompleta) |
| 1950/51 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a classificação incompleta) |
| 1951/52 | 4 | 0 (0) | 0 | 0 | 0 / 0 | US Marocaine | sem jogos (só a classificação incompleta) |
| 1952/53 | 12 | 0 (0) | 0 | 0 | 0 / 0 | SA Marrakech | sem jogos (só a classificação incompleta) |
| 1953/54 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Casablanca | sem jogos (só a classificação incompleta) |
| 1954/55 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1956/57 | 16 | 240 (240) | 608 | 0 | 0 / 1 | Wydad Casablanca | pontos corridos |
| 1957/58 | 15 | 210 (210) | 511 | 0 | 0 / 1 | Kawkab Marrakech | pontos corridos |
| 1958/59 | 14 | 182 (182) | 449 | 0 | 0 / 1 | EJS Casablanca | pontos corridos |
| 1959/60 | 14 | 171 (171) | 388 | 0 | 0 / 1 | KAC Kénitra | pontos corridos + desempate |
| 1960/61 | 14 | 182 (182) | 459 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1961/62 | 14 | 182 (182) | 443 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1962/63 | 14 | 182 (182) | 400 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1963/64 | 14 | 182 (182) | 406 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1964/65 | 14 | 182 (182) | 384 | 0 | 1 / 0 | MAS Fès | pontos corridos |
| 1965/66 | 14 | 182 (182) | 320 | 0 | 0 / 1 | Wydad Casablanca | pontos corridos |
| 1966/67 | 16 | 240 (240) | 452 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1967/68 | 18 | 306 (306) | 585 | 0 | 0 / 1 | FAR Rabat | pontos corridos |
| 1968/69 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1969/70 | 16 | 0 (0) | 0 | 0 | 0 / 0 | FAR Rabat | sem jogos (só a tabela final) |
| 1970/71 | 2 | 0 (0) | 0 | 0 | 0 / 0 | RS Settat | sem jogos (só o campeão e o vice) |
| 1971/72 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Racing Casablanca | sem jogos (só a tabela final) |
| 1972/73 | 16 | 0 (0) | 0 | 0 | 0 / 0 | KAC Kénitra | sem jogos (só a tabela final) |
| 1973/74 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Raja Béni Mellal | sem jogos (só o campeão e o vice) |
| 1974/75 | 16 | 0 (0) | 0 | 0 | 0 / 0 | MC Oujda | sem jogos (só a tabela final) |
| 1975/76 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1976/77 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1977/78 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1978/79 | 16 | 0 (0) | 0 | 0 | 0 / 0 | MAS Fès | sem jogos (só a tabela final) |
| 1979/80 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Chabab Mohammédia | sem jogos (só a tabela final) |
| 1980/81 | 20 | 380 (380) | 713 | 0 | 0 / 1 | KAC Kénitra | pontos corridos |
| 1981/82 | 2 | 0 (0) | 0 | 0 | 0 / 0 | KAC Kénitra | sem jogos (só o campeão e o vice) |
| 1982/83 | 16 | 0 (0) | 0 | 0 | 0 / 0 | MAS Fès | sem jogos (só a tabela final) |
| 1983/84 | 16 | 0 (0) | 0 | 0 | 0 / 0 | FAR Rabat | sem jogos (só a tabela final) |
| 1984/85 | 16 | 0 (0) | 0 | 0 | 0 / 0 | MAS Fès | sem jogos (só a tabela final) |
| 1985/86 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1986/87 | 24 | 0 (0) | 0 | 0 | 0 / 0 | FAR Rabat | sem jogos (só a tabela final) |
| 1987/88 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Raja Casablanca | sem jogos (só a tabela final) |
| 1988/89 | 16 | 0 (0) | 0 | 0 | 0 / 0 | FAR Rabat | sem jogos (só a tabela final) |
| 1989/90 | 16 | 240 (240) | 411 | 0 | 0 / 1 | Wydad Casablanca | pontos corridos |
| 1990/91 | 16 | 240 (240) | 505 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 1991/92 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Kawkab Marrakech | sem jogos (só a tabela final) |
| 1992/93 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Wydad Casablanca | sem jogos (só a tabela final) |
| 1993/94 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Olympique de Casablanca | sem jogos (só a classificação incompleta) |
| 1994/95 | 16 | 0 (0) | 0 | 0 | 0 / 0 | CODM Meknès | sem jogos (só a tabela final) |
| 1995/96 | 16 | 240 (240) | 463 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 1996/97 | 16 | 240 (240) | 466 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 1997/98 | 16 | 240 (240) | 448 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 1998/99 | 16 | 240 (240) | 472 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 1999/00 | 16 | 241 (241) | 426 | 0 | 0 / 1 | Raja Casablanca | pontos corridos |
| 2000/01 | 16 | 240 (240) | 411 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 2001/02 | 16 | 240 (240) | 435 | 0 | 1 / 0 | Hassania Agadir | pontos corridos |
| 2002/03 | 16 | 240 (240) | 398 | 1 | 1 / 0 | Hassania Agadir | pontos corridos |
| 2003/04 | 16 | 240 (240) | 376 | 16 | 0 / 1 | Raja Casablanca | pontos corridos |
| 2004/05 | 16 | 240 (240) | 386 | 0 | 1 / 0 | FAR Rabat | pontos corridos |
| 2005/06 | 16 | 240 (240) | 417 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2006/07 | 16 | 240 (240) | 403 | 0 | 1 / 0 | OC Khouribga | pontos corridos |
| 2007/08 | 16 | 240 (240) | 447 | 0 | 1 / 0 | FAR Rabat | pontos corridos |
| 2008/09 | 16 | 240 (240) | 448 | 0 | 0 / 1 | Raja Casablanca | pontos corridos |
| 2009/10 | 16 | 240 (240) | 433 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2010/11 | 16 | 240 (240) | 413 | 0 | 0 / 1 | Raja Casablanca | pontos corridos |
| 2011/12 | 16 | 240 (240) | 465 | 0 | 1 / 0 | Moghreb Tétouan | pontos corridos |
| 2012/13 | 16 | 240 (240) | 496 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 2013/14 | 16 | 240 (240) | 461 | 0 | 1 / 0 | Moghreb Tétouan | pontos corridos |
| 2014/15 | 16 | 240 (240) | 493 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2015/16 | 16 | 240 (240) | 501 | 0 | 1 / 0 | FUS Rabat | pontos corridos |
| 2016/17 | 16 | 240 (240) | 535 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2017/18 | 16 | 240 (240) | 546 | 0 | 1 / 0 | IR Tanger | pontos corridos |
| 2018/19 | 16 | 240 (240) | 550 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2019/20 | 16 | 241 (241) | 524 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 2020/21 | 16 | 240 (240) | 540 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2021/22 | 16 | 240 (240) | 519 | 0 | 1 / 0 | Wydad Casablanca | pontos corridos |
| 2022/23 | 16 | 240 (240) | 512 | 0 | 1 / 0 | FAR Rabat | pontos corridos |
| 2023/24 | 16 | 240 (240) | 534 | 0 | 1 / 0 | Raja Casablanca | pontos corridos |
| 2024/25 | 16 | 240 (240) | 555 | 0 | 1 / 0 | RS Berkane | pontos corridos |
| 2025/26 | 16 | 240 (240) | 520 | 0 | 1 / 0 | MAS Fès | pontos corridos |

## Conferência e correções, edição a edição

### 1915/16

- a RSSSF traz só a ordem final (sem jogos nem pontos)

### 1916/17

- jogos incompletos (só os resultados conhecidos e a final)
- W.O./pontos para o mandante — US Marocaine Rabat FC (1917-03-15): bt

### 1917/18

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1918/19

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1919/20

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1920/21

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1921/22

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1922/23

- jogos incompletos (ligas regionais sem jogos; só as semifinais e a final)
- W.O./pontos para o mandante — Racing Club Marocain AS Marrakech (s/d): bt
- W.O./pontos para o mandante — Olympique Marocain Meknès Sports (s/d): bt

### 1923/24

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1924/25

- jogos incompletos (ligas regionais sem jogos; só a final)

### 1925/26

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1926/27

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1927/28

- sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)

### 1928/29

- jogos incompletos (só a final)
- W.O./pontos para o mandante — USA Casablanca Racing Casablanca (s/d): bt

### 1929/30

- jogos incompletos (ligas regionais com poucos jogos; o mata-mata final completo)
- W.O./pontos para o mandante — Stade Marocain ASPTT Fès (1930-03-02): bt

### 1930/31

- jogos incompletos (só o mata-mata final)
- W.O./pontos para o mandante — Stade Marocain US Marocaine (s/d): bt

### 1931/32

- jogos incompletos (dois grupos com os resultados conhecidos e a final)
- abandonado/suspenso, sem valer — Moghreb Tanger Olympique Marocain (1932-01-17)

### 1932/33

- jogos incompletos (resultados conhecidos; classificação em 20/02 com jogos e pontos)

### 1933/34

- dois jogos da página não têm placar ("drw", empate sem placar conhecido: Racing Casablanca x SA Marrakech na 6ª rodada e ASPTT Casablanca x Roches Noires na 12ª) e ficam de fora, como no ven-1; por isso esses quatro clubes têm um jogo e um empate a menos que a tabela
- tabela publicada x jogos — maro34:108: Racing Casablanca tabela [14, 6, 5, 3, 24, 17] jogos [13, 6, 4, 3, 24, 17] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — maro34:108: SA Marrakech tabela [14, 5, 3, 6, 27, 32] jogos [13, 5, 2, 6, 27, 32] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — maro34:108: ASPTT Casablanca tabela [14, 5, 1, 8, 19, 30] jogos [13, 5, 0, 8, 19, 30] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — maro34:108: Roches Noires tabela [14, 2, 5, 7, 17, 29] jogos [13, 2, 4, 7, 17, 29] — faltam 1 jogo(s) do clube na fonte dos jogos
- W.O./pontos para o visitante — Olympique Marocain US Marocaine (s/d): lt
- W.O./pontos para o visitante — USA Casablanca Stade Marocain (s/d): lt
- W.O./pontos para o mandante — Roches Noires US Marocaine (1934-04-01): bt

### 1934/35

- W.O./pontos para o mandante — SA Marrakech AS Tanger-Fès (1934-11-25): bt

### 1935/36

- sem ocorrências

### 1936/37

- sem ocorrências

### 1937/38

- sem ocorrências

### 1938/39

- anulado — Olympique Marocain 1-0 Stade Marocain (1938-11-27): annulled

### 1939/40

- jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)

### 1940/41

- jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)

### 1941/42

- tabela publicada x jogos — maro3944:515: Olympique Meknès tabela [18, 9, 2, 7, 33, 23] jogos [18, 9, 2, 7, 35, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro3944:515: Racing Casablanca tabela [18, 7, 6, 5, 35, 31] jogos [18, 7, 7, 4, 35, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro3944:515: USA Casablanca tabela [18, 6, 4, 8, 36, 31] jogos [18, 5, 5, 8, 35, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro3944:515: Roches Noires tabela [18, 3, 2, 13, 12, 32] jogos [18, 3, 3, 12, 13, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro3944:515: AS Casablanca tabela [17, 2, 3, 12, 21, 46] jogos [17, 2, 2, 13, 20, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Racing Casablanca 0-0 USA Casablanca (1941-11-09, maro3944:395); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Racing Casablanca 1-1 USA Casablanca (1942-02-22, maro3944:464); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- anulado — US Marocaine 2-3 AS Casablanca (1941-10-05): annulled
- não jogado — Stade Marocain AS Casablanca (1942-03-30)
- não jogado — US Fès SA Marrakech (1942-04-19)

### 1942/43

- temporada não terminada: abandonada em novembro de 1942, com o desembarque aliado no Marrocos; no lugar dela houve a Coupe de la Guerre (a US Marocaine ganhou), que não conta como título

### 1943/44

- jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)
- decidido fora de campo — SC Taza AS Casablanca (1945-01-23): awarded 0-3; originally 2-0

### 1944/45

- jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)
- decidido fora de campo — Racing Casablanca US Marocaine (1946-04-08): USM forfeited

### 1945/46

- jogos incompletos (ligas regionais quase sem jogos; o mata-mata nacional completo)

### 1946/47

- campeão: USA Casablanca, que venceu o desempate do título (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine, 3ª colocada (erro da lista)
- W.O./pontos para o mandante — US Marocaine US Fès (1947-05-04): by 2 goals?]  [bt
- decidido fora de campo — AS Tanger-Fès Wydad Casablanca (1947-03-16): awarded 0-3; originally 1-2

### 1947/48

- tabela publicada x jogos — maro48:147: ASPTT Casablanca tabela [18, 5, 4, 9, 20, 37] jogos [18, 5, 4, 9, 20, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro48:147: Racing Casablanca tabela [18, 5, 3, 10, 29, 37] jogos [18, 5, 3, 10, 28, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Racing Casablanca 2-0 ASPTT Casablanca (1948-01-11, maro48:77); com 3-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- não jogado — US Marocaine USA Casablanca (1948-02-29)

### 1948/49

- jogos incompletos (as rodadas que a página traz e outros jogos do WAC; classificação só com pontos)

### 1949/50

- a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)

### 1950/51

- a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)

### 1951/52

- a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)

### 1952/53

- a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)

### 1953/54

- a RSSSF traz só a classificação (a maioria dos clubes só com os pontos)

### 1954/55

- a tabela é a publicada na época, que a própria RSSSF diz estar "cheia de absurdos" (as linhas não fecham com o sistema 3-2-1); entra como está, só como classificação
- a RSSSF traz a tabela publicada na época, que ela mesma diz estar "cheia de absurdos"

### 1956/57

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro57:19: Kawkab Marrakech tabela [30, 15, 9, 6, 48, 31] jogos [30, 16, 9, 5, 48, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro57:19: FUS Rabat tabela [30, 13, 8, 9, 42, 30] jogos [30, 12, 9, 9, 42, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro57:19: Roches Noires tabela [30, 5, 5, 20, 25, 56] jogos [30, 5, 4, 21, 25, 56] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1957/58

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro58:19: Kawkab Marrakech tabela [28, 16, 10, 2, 38, 20] jogos [28, 15, 10, 3, 38, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: TAS Casablanca tabela [28, 12, 10, 6, 37, 27] jogos [28, 11, 11, 6, 37, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: MC Oujda tabela [28, 11, 10, 7, 38, 39] jogos [28, 11, 9, 8, 38, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: FUS Rabat tabela [28, 11, 9, 8, 32, 31] jogos [28, 11, 8, 9, 32, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: DH El Jadida tabela [28, 9, 11, 8, 45, 40] jogos [28, 10, 11, 7, 45, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: Rachad de Meknès tabela [28, 9, 9, 10, 42, 40] jogos [28, 9, 8, 11, 42, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: Racing Casablanca tabela [28, 9, 7, 12, 35, 32] jogos [28, 10, 7, 11, 35, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: Stade Marocain tabela [28, 6, 13, 9, 33, 37] jogos [28, 7, 12, 9, 33, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: MAS Fès tabela [28, 5, 13, 10, 26, 28] jogos [28, 6, 12, 10, 26, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: US Safi tabela [28, 5, 10, 13, 36, 51] jogos [28, 6, 9, 13, 36, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro58:19: ASM tabela [28, 4, 8, 16, 25, 53] jogos [28, 4, 7, 17, 25, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1958/59

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro59:19: Racing Casablanca tabela [26, 10, 7, 9, 28, 29] jogos [26, 11, 7, 8, 28, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro59:19: FUS Rabat tabela [26, 8, 10, 8, 28, 26] jogos [26, 7, 10, 9, 28, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro59:19: Hassania Agadir tabela [26, 5, 12, 9, 24, 53] jogos [26, 4, 12, 10, 24, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro59:19: TAS Casablanca tabela [26, 5, 11, 10, 30, 31] jogos [26, 6, 11, 9, 30, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1959/60

- Kénitra, FAR e Raja terminaram empatados em pontos; o triangular do título virou um jogo só (KAC Kénitra 3-1 FAR), porque o Raja se recusou a jogar, dizendo que o título era dele pelo goal average
- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro60:19: FUS Rabat tabela [24, 7, 11, 6, 24, 25] jogos [24, 6, 11, 7, 24, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro60:19: Racing Casablanca tabela [24, 7, 9, 8, 31, 33] jogos [24, 8, 9, 7, 31, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- jogos do Hassania Agadir anulados: o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — KAC Kénitra 1-3 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — FAR Rabat 2-1 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Raja Casablanca 1-3 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — FUS Rabat 2-0 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — MAS Fès 1-0 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — DH El Jadida 2-2 Hassania Agadir (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 1-2 Wydad Casablanca (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 3-0 FUS Rabat (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 0-4 MC Oujda (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 4-1 MAS Fès (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 1-1 Racing Casablanca (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 2-0 Kawkab Marrakech (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 1-1 EJS Casablanca (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)
- anulado — Hassania Agadir 2-0 Stade Marocain (s/d): o Hassania Agadir desistiu depois do terremoto que destruiu Agadir em 29/02/1960; os resultados dele foram anulados (a tabela publicada tem os outros 13 clubes, com 24 jogos)

### 1960/61

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro61:19: FAR Rabat tabela [26, 13, 7, 6, 42, 26] jogos [26, 14, 6, 6, 42, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: Kawkab Marrakech tabela [26, 12, 7, 7, 44, 32] jogos [26, 12, 8, 6, 44, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: MC Oujda tabela [26, 11, 8, 7, 32, 30] jogos [26, 10, 8, 8, 32, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: Raja Casablanca tabela [26, 8, 12, 6, 35, 35] jogos [26, 8, 11, 7, 35, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: Wydad Casablanca tabela [26, 9, 9, 8, 30, 25] jogos [26, 9, 8, 9, 30, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: Moghreb Tétouan tabela [26, 11, 3, 12, 33, 44] jogos [26, 11, 4, 11, 33, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: TAS Casablanca tabela [26, 7, 10, 9, 25, 29] jogos [26, 7, 9, 10, 25, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: Hassania Agadir tabela [26, 7, 8, 11, 26, 35] jogos [26, 7, 9, 10, 27, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro61:19: FUS Rabat tabela [26, 4, 8, 14, 26, 42] jogos [26, 5, 7, 14, 26, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1961/62

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro62:19: Kawkab Marrakech tabela [26, 11, 7, 8, 48, 45] jogos [26, 10, 8, 8, 48, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro62:19: Wydad Casablanca tabela [26, 10, 8, 8, 29, 26] jogos [26, 11, 7, 8, 29, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro62:19: Raja Casablanca tabela [26, 10, 7, 9, 35, 28] jogos [26, 10, 8, 8, 35, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro62:19: Hassania Agadir tabela [26, 9, 7, 10, 24, 33] jogos [26, 8, 9, 9, 24, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro62:19: Chabab Mohammédia tabela [26, 6, 12, 8, 33, 35] jogos [26, 6, 11, 9, 33, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1962/63

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro63:19: Raja Casablanca tabela [26, 9, 10, 7, 35, 28] jogos [26, 10, 9, 7, 35, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: MAS Fès tabela [26, 9, 10, 7, 34, 25] jogos [26, 10, 9, 7, 34, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: KAC Kénitra tabela [26, 8, 11, 7, 26, 25] jogos [26, 7, 11, 8, 26, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Wydad Casablanca tabela [26, 8, 10, 8, 26, 22] jogos [26, 9, 8, 9, 26, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Racing Casablanca tabela [26, 8, 10, 8, 21, 22] jogos [26, 8, 10, 8, 21, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Stade Marocain tabela [26, 8, 10, 8, 26, 27] jogos [26, 8, 9, 9, 26, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Hassania Agadir tabela [26, 8, 10, 8, 32, 30] jogos [26, 8, 9, 9, 32, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Chabab Mohammédia tabela [26, 9, 7, 10, 29, 34] jogos [26, 10, 6, 10, 29, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: FUS Rabat tabela [26, 8, 8, 10, 31, 37] jogos [26, 7, 9, 10, 31, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: MC Oujda tabela [26, 7, 9, 10, 18, 26] jogos [26, 7, 10, 9, 18, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: Moghreb Tétouan tabela [26, 6, 9, 11, 27, 31] jogos [26, 8, 9, 9, 27, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro63:19: IR Tanger tabela [26, 5, 9, 12, 29, 43] jogos [26, 3, 10, 13, 29, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1963/64

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro64:19: Hassania Agadir tabela [26, 9, 6, 11, 26, 23] jogos [26, 10, 6, 10, 26, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro64:19: Racing Casablanca tabela [26, 8, 8, 10, 24, 30] jogos [26, 7, 8, 11, 24, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1964/65

- sem ocorrências

### 1965/66

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro66:23: RS Settat tabela [26, 10, 8, 8, 28, 15] jogos [26, 11, 8, 7, 28, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro66:23: Racing Casablanca tabela [26, 7, 10, 9, 17, 21] jogos [26, 6, 10, 10, 17, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1966/67

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro67:19: Stade Marocain tabela [30, 7, 18, 5, 25, 29] jogos [30, 6, 17, 7, 25, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: TAS Casablanca tabela [30, 8, 15, 7, 26, 23] jogos [30, 9, 14, 7, 26, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: Chabab Mohammédia tabela [30, 7, 15, 8, 21, 22] jogos [30, 6, 16, 8, 21, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: FUS Rabat tabela [30, 8, 11, 11, 24, 26] jogos [30, 8, 10, 12, 24, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: Kawkab Marrakech tabela [30, 7, 13, 10, 26, 29] jogos [30, 8, 12, 10, 26, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: Racing Casablanca tabela [30, 7, 12, 11, 23, 29] jogos [30, 8, 11, 11, 23, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro67:19: Raja Béni Mellal tabela [30, 6, 14, 10, 33, 40] jogos [30, 7, 14, 9, 33, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1967/68

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro68:19: FAR Rabat tabela [34, 17, 14, 3, 43, 25] jogos [34, 17, 13, 4, 43, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: RS Settat tabela [34, 14, 13, 7, 36, 22] jogos [34, 15, 13, 6, 36, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: Stade Marocain tabela [34, 8, 19, 7, 27, 30] jogos [34, 7, 19, 8, 27, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: FUS Rabat tabela [34, 9, 13, 12, 34, 42] jogos [34, 8, 14, 12, 34, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: Raja Béni Mellal tabela [34, 10, 10, 14, 33, 43] jogos [34, 10, 10, 14, 33, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: Barid Mohammedi tabela [34, 5, 14, 15, 24, 38] jogos [34, 5, 15, 14, 24, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro68:19: Hassania Agadir tabela [34, 5, 10, 19, 20, 40] jogos [34, 5, 11, 18, 20, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1968/69

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1969/70

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1970/71

- a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista

### 1971/72

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1972/73

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1973/74

- a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista

### 1974/75

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1975/76

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1976/77

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1977/78

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1978/79

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1979/80

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1980/81

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro81:19: KAC Kénitra tabela [38, 22, 9, 7, 61, 27] jogos [38, 22, 9, 7, 61, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: FUS Rabat tabela [38, 19, 10, 9, 38, 22] jogos [38, 19, 9, 10, 37, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: Wydad Casablanca tabela [38, 17, 9, 12, 44, 32] jogos [38, 17, 9, 12, 43, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: CODM Meknès tabela [38, 16, 9, 13, 37, 37] jogos [38, 16, 9, 13, 38, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: FAR Rabat tabela [38, 13, 14, 11, 34, 30] jogos [38, 14, 13, 11, 36, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: MAS Fès tabela [38, 12, 14, 12, 28, 28] jogos [38, 12, 14, 12, 30, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: US Mohammédia tabela [38, 13, 10, 15, 37, 40] jogos [38, 13, 10, 15, 34, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: RS Berkane tabela [38, 13, 10, 15, 28, 40] jogos [38, 13, 10, 15, 27, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: Raja Béni Mellal tabela [38, 10, 11, 17, 35, 47] jogos [38, 10, 11, 17, 35, 48] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro81:19: Union Touarga tabela [38, 10, 5, 23, 35, 55] jogos [38, 10, 5, 23, 35, 54] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1981/82

- a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista

### 1982/83

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1983/84

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1984/85

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1985/86

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1986/87

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1987/88

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1988/89

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1989/90

- a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- tabela publicada x jogos — maro90:19: Wydad Casablanca tabela [30, 15, 12, 3, 45, 21] jogos [30, 13, 13, 4, 44, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: Raja Casablanca tabela [30, 11, 11, 8, 34, 29] jogos [30, 11, 11, 8, 33, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: RS Settat tabela [30, 10, 12, 8, 26, 21] jogos [30, 11, 12, 7, 26, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: FAR Rabat tabela [30, 9, 13, 8, 25, 20] jogos [30, 10, 13, 7, 27, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: KAC Kénitra tabela [30, 7, 15, 8, 22, 21] jogos [30, 7, 16, 7, 23, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: US Sidi Kacem tabela [30, 7, 15, 8, 30, 40] jogos [30, 8, 15, 7, 31, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: CLAS Casablanca tabela [30, 7, 14, 9, 21, 20] jogos [30, 6, 14, 10, 20, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: Hassania Agadir tabela [30, 7, 13, 10, 21, 24] jogos [30, 6, 13, 11, 19, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro90:19: FUS Rabat tabela [30, 5, 16, 9, 17, 25] jogos [30, 5, 16, 9, 16, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: FUS Rabat 0-0 Wydad Casablanca (None, maro90:58:0); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: FAR Rabat 3-0 Hassania Agadir (None, maro90:51:11); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: US Sidi Kacem 1-0 CLAS Casablanca (None, maro90:54:10); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1990/91

- sem ocorrências

### 1991/92

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1992/93

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1993/94

- a RSSSF traz só a classificação, com os pontos (jogos, vitórias e gols só de alguns clubes)

### 1994/95

- a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano

### 1995/96

- sem ocorrências

### 1996/97

- sem ocorrências

### 1997/98

- sem ocorrências

### 1998/99

- sem ocorrências

### 1999/00

- tabela publicada x jogos — maro00:14: Chabab Mohammédia tabela [30, 11, 7, 12, 21, 21] jogos [30, 11, 8, 11, 21, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — maro00:14: Kawkab Marrakech tabela [30, 6, 15, 9, 24, 29] jogos [30, 5, 16, 9, 24, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- decidido fora de campo — Kawkab Marrakech Chabab Mohammédia (1999-09-05): awarded 0-0 to KAC, Mohammedia dns
- abandonado/suspenso, sem valer — AS Salé Raja Casablanca (2000-03-04): abandoned after 9 sending-offs

### 2000/01

- decidido fora de campo — Wydad Casablanca Raja Casablanca (2001-04-08): awarded 0-1 to Raja; originally 3-0

### 2001/02

- decidido fora de campo — FAR Rabat Raja Béni Mellal (2002-03-23): awarded 1-0 win to FAR,

### 2002/03

- sem ocorrências

### 2003/04

- tabela publicada x jogos — maro04:15: Raja Casablanca tabela [30, 15, 11, 4, 36, 18] jogos [30, 14, 12, 4, 36, 18] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro04:15: RS Settat tabela [30, 6, 9, 15, 15, 28] jogos [30, 6, 10, 14, 15, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — Raja Casablanca RS Settat (2004-10-26): awarded 0-0 win to Raja; RS Settat

### 2004/05

- ogol: 210 jogos casados (edição 1100 do ogol, 240 jogos)
- placar diferente no ogol — MC Oujda x IZ Khémisset (2004-10-24): RSSSF 2-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Wydad Casablanca x Raja Casablanca (2005-04-30): RSSSF 0-1, ogol 1-0; fica o da RSSSF

### 2005/06

- ogol: 104 jogos casados (edição 30252 do ogol, 239 jogos)
- placar diferente no ogol — IZ Khémisset x Union Touarga (2005-09-04): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- decidido fora de campo — Union Touarga IZ Khémisset (2007-02-08): awarded 0-2; US Touarga dns;

### 2006/07

- ogol: 80 jogos casados (edição 1460 do ogol, 240 jogos)
- data diferente no ogol — IZ Khémisset x OC Khouribga: RSSSF 2006-10-18, ogol 2006-10-08; fica a da RSSSF
- data diferente no ogol — MC Oujda x Hassania Agadir: RSSSF 2006-10-29, ogol 2006-10-22; fica a da RSSSF
- data diferente no ogol — DH El Jadida x IR Tanger: RSSSF 2006-10-29, ogol 2006-10-22; fica a da RSSSF
- data diferente no ogol — AS Salé x CODM Meknès: RSSSF 2006-10-29, ogol 2006-10-22; fica a da RSSSF
- data diferente no ogol — JS Massira x FAR Rabat: RSSSF 2006-11-01, ogol 2006-10-22; fica a da RSSSF
- data diferente no ogol — IZ Khémisset x Kawkab Marrakech: RSSSF 2006-10-29, ogol 2006-10-22; fica a da RSSSF
- data diferente no ogol — MAS Fès x Olympic Safi: RSSSF 2006-10-29, ogol 2006-10-22; fica a da RSSSF

### 2007/08

- ogol: 39 jogos casados (edição 1656 do ogol, 240 jogos)

### 2008/09

- ogol: 112 jogos casados (edição 3763 do ogol, 240 jogos)
- tabela publicada x jogos — maro09:54: Raja Casablanca tabela [30, 17, 10, 3, 44, 17] jogos [30, 18, 9, 3, 45, 17] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro09:54: Moghreb Tétouan tabela [30, 11, 8, 11, 29, 28] jogos [30, 10, 9, 11, 30, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro09:54: MAS Fès tabela [30, 10, 10, 10, 28, 27] jogos [30, 10, 11, 9, 30, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro09:54: JS Massira tabela [30, 8, 10, 12, 31, 41] jogos [30, 8, 10, 12, 29, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro09:54: IZ Khémisset tabela [30, 7, 12, 11, 22, 29] jogos [30, 7, 12, 11, 20, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro09:54: MC Oujda tabela [30, 7, 7, 16, 21, 37] jogos [30, 7, 6, 17, 21, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Raja Casablanca 1-0 MC Oujda (2008-11-02, maro09:175); com 0-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: MC Oujda 0-1 Raja Casablanca (2010-03-22, maro09:372); com 0-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: MAS Fès 2-2 Moghreb Tétouan (2010-03-22, maro09:371); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: JS Massira 1-1 IZ Khémisset (2008-11-01, maro09:172); com 3-3 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: IZ Khémisset 0-0 JS Massira (2010-03-22, maro09:370); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- data diferente no ogol — Hassania Agadir x Olympic Safi: RSSSF 2008-11-16, ogol 2008-11-23; fica a da RSSSF
- decidido fora de campo — Wydad Casablanca OC Khouribga (2008-09-28): awarded 0-1, originally 1-0
- decidido fora de campo — JS Massira DH El Jadida (2008-11-09): awarded 0-1; JS El Massira

### 2009/10

- ogol: 240 jogos casados (edição 9586 do ogol, 240 jogos)
- placar diferente no ogol — Moghreb Tétouan x Hassania Agadir (2009-09-27): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Kawkab Marrakech x KAC Kénitra (2009-10-17): RSSSF 3-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — JS Massira x Hassania Agadir (2009-11-01): RSSSF 3-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — MAS Fès x Wydad Fès (2010-04-04): RSSSF 1-2, ogol 0-1; fica o da RSSSF

### 2010/11

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)
- tabela publicada x jogos — maro2011:24: OC Khouribga tabela [30, 14, 8, 8, 31, 20] jogos [30, 13, 9, 8, 30, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro2011:24: Moghreb Tétouan tabela [30, 8, 12, 10, 26, 28] jogos [30, 8, 12, 10, 26, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — maro2011:24: JS Massira tabela [30, 8, 10, 12, 24, 35] jogos [30, 8, 11, 11, 25, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 2011/12

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)

### 2012/13

- ogol: 240 jogos casados (edição 50105 do ogol, 240 jogos)

### 2013/14

- ogol: 96 jogos casados (edição 62291 do ogol, 240 jogos)
- placar diferente no ogol — MAS Fès x Kawkab Marrakech (2013-11-08): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- decidido fora de campo — DH El Jadida Chabab Rif Hoceima (2013-12-02): awarded 3-0; originally 2-1, CRA
- decidido fora de campo — OC Khouribga FUS Rabat (2013-12-08): awarded 0-3; originally 1-1, OCK
- decidido fora de campo — Wydad Fès OC Khouribga (2015-03-07): awarded 3-0

### 2014/15

- ogol: 240 jogos casados (edição 72017 do ogol, 240 jogos)

### 2015/16

- ogol: 239 jogos casados (edição 88237 do ogol, 240 jogos)
- data diferente no ogol — Moghreb Tétouan x IR Tanger: RSSSF 2016-02-18, ogol 2016-02-28; fica a da RSSSF
- data diferente no ogol — FAR Rabat x Hassania Agadir: RSSSF 2016-02-18, ogol 2016-02-28; fica a da RSSSF
- data diferente no ogol — Raja Casablanca x MC Oujda: RSSSF 2016-02-18, ogol 2016-02-28; fica a da RSSSF
- data diferente no ogol — Hassania Agadir x RS Berkane: RSSSF 2016-03-18, ogol 2016-03-27; fica a da RSSSF

### 2016/17

- ogol: 240 jogos casados (edição 99141 do ogol, 240 jogos)

### 2017/18

- ogol: 56 jogos casados (edição 113007 do ogol, 240 jogos)
- data diferente no ogol — Rapide Oued Zem x Moghreb Tétouan: RSSSF 2017-10-01, ogol 2017-09-27; fica a da RSSSF

### 2018/19

- ogol: 31 jogos casados (edição 125379 do ogol, 240 jogos)

### 2019/20

- ogol: 65 jogos casados (edição 136713 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — DH El Jadida Moghreb Tétouan (2021-08-26): abandoned at 0-0 due to bad weather

### 2020/21

- ogol: 240 jogos casados (edição 149623 do ogol, 240 jogos)
- data diferente no ogol — Hassania Agadir x Moghreb Tétouan: RSSSF 2021-02-13, ogol 2021-02-17; fica a da RSSSF

### 2021/22

- ogol: 112 jogos casados (edição 157844 do ogol, 240 jogos)

### 2022/23

- ogol: 240 jogos casados (edição 167247 do ogol, 240 jogos)

### 2023/24

- ogol: 96 jogos casados (edição 176811 do ogol, 240 jogos)

### 2024/25

- ogol: 240 jogos casados (edição 189076 do ogol, 240 jogos)

### 2025/26

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)

