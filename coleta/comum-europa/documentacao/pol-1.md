# Campeonato Polonês (`pol-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/pol-1/pacote/` e do importador `coleta/pol-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/pol-1.md`.

## 1. O que temos

- **Edições:** 98, de 1921 a 2025/26.
- **Jogos:** 19667; **gols:** 53027; **gols com autor:** 0 (0%); **cartões:** 0; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 103; **artilheiros:** 98 temporadas com artilheiro (110 linhas, com empates).
- **Classificação final:** 98 temporadas; **rodada a rodada:** 62 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2521 linhas, de 166 tabelas.
- **Observação da competição:** Os 98 títulos poloneses que a federação (PZPN) reconhece: torneios entre os campeões regionais (1921-1926, 1946 e 1947) e a liga (Liga, I liga e Ekstraklasa) de 1927 a 1938 e desde 1948; 1962 só com a primavera, na passagem para o calendário de outono a primavera. Não inclui 1920 (abandonado), 1924 (não disputado), 1939 (interrompido pela guerra) nem as ligas municipais da guerra.

## 2. Fontes e regras

**Fontes:**

- RSSSF (polhist.html): matriz dos torneios (base dos jogos de 1921-1926, 1946 e 1947), tabela e matriz de cada temporada até 2000/01 (conferência), final de 1922 e play-offs de 1962; lista de campeões e de artilheiros;
- Wikipédia (en): tabela de cada fase (ordem oficial, punições, bônus), matriz de resultados (base dos jogos de 1927 a 1962, conferência depois), fichas das finais de 1923, do desempate de 1925 e do mata-mata de 1946;
- ogol (zerozero): base dos jogos desde 1962/63, com data, hora e rodada; calendários em `data/cache/ogol-pol-1/`;
- football-data: conferência dos placares desde 2012/13.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; nos torneios, o grupo final ou a final e depois a posição no grupo; em 1962, os play-offs de classificação). Pontos 2-1-0 até 1994/95 e 3-1-0 depois; bônus de 1986/87 a 1989/90 e pontos da fase regular divididos por dois de 2013/14 a 2019/20, em `ajuste_pontos`. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (em 1938, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 47 fases, saldo em 37, confronto direto em 46).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 139 tabelas fecham com os jogos e 74 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1922, 1923, 1927, 1934, 1935, 1937, 1938, 1949, 1953, 1956, 1957, 1958, 1960, 1963/64, 1968/69, 1985/86, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1999/00, 2000/01, 2002/03, 2003/04, 2010/11.
- Temporadas com alguma tabela divergente: 1922, 1923, 1926, 1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1938, 1947, 1949, 1953, 1956, 1957, 1958, 1960, 1961, 1963/64, 1968/69, 1972/73, 1974/75, 1978/79, 1984/85, 1985/86, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1999/00, 2000/01, 2002/03, 2003/04, 2010/11.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 664 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 1010 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 581 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1228 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1868 | 78% | 78% | 78% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2226 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 2860 | 100% | 8% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 2268 | 100% | 98% | 95% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2010s | 2792 | 100% | 99% | 86% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 1770 | 100% | 100% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1921: 5 clubes
- 1922 a 1923: 8 clubes
- 1925 a 1926: 9 clubes
- 1927: 14 clubes
- 1928: 15 clubes
- 1929: 13 clubes
- 1930 a 1934: 12 clubes
- 1935: 11 clubes
- 1936: 10 clubes
- 1937: 9 clubes
- 1938: 10 clubes
- 1946: 18 clubes
- 1947: 28 clubes
- 1948: 14 clubes
- 1949 a 1953: 12 clubes
- 1954: 11 clubes
- 1955 a 1960: 12 clubes
- 1961 a 1972/73: 14 clubes
- 1973/74 a 1990/91: 16 clubes
- 1991/92 a 1997/98: 18 clubes
- 1998/99 a 2002/03: 16 clubes
- 2003/04 a 2004/05: 14 clubes
- 2005/06 a 2020/21: 16 clubes
- 2021/22 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1921 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1921 a 1926: Mistrzostwa Polski (torneio final)
- 1927 a 1938: Liga
- 1946 a 1947: Mistrzostwa Polski (torneio final)
- 1948 a 2007/08: I liga
- 2008/09 a 2025/26: Ekstraklasa

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1921: Grupo final (grupos, pontos_corridos)
- 1922: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1923: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta); Desempate da final (mata_mata, jogo_unico)
- 1925: Grupos (grupos, pontos_corridos); Desempate (mata_mata, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1926: Grupos (grupos, pontos_corridos); Grupo final (grupos, pontos_corridos)
- 1933: Grupos (grupos, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 1946: Preliminar (mata_mata, jogo_unico); Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1947: Grupos (grupos, pontos_corridos); Grupo final (grupos, pontos_corridos)
- 1948: Liga (liga, pontos_corridos); Desempate (mata_mata, jogo_unico)
- 1952: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1962: Grupos (grupos, pontos_corridos); Play-off de classificação (mata_mata, ida_volta)
- 2001/02: Grupos (grupos, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2013/14: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2014/15: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2015/16: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2016/17: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2017/18: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2018/19: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2019/20: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, média de gols (goal average): 37 temporadas
- pontos, saldo de gols: 34 temporadas
- pontos, confronto direto, saldo de gols: 34 temporadas
- pontos, confronto direto, saldo de gols; pontos da fase regular divididos por dois: 11 temporadas
- jogo único: 6 temporadas
- pontos nos dois jogos, depois saldo: 3 temporadas
- pontos, saldo de gols; pontos da fase regular divididos por dois: 3 temporadas
- pontos nos dois jogos; empate, jogo extra: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1937: Dąb Katowice saiu do campeonato e teve os jogos anulados (linha vazia na tabela da Wikipédia)
- 1951: o título polonês foi para o vencedor da Copa da Polônia de 1950/51 (decisão da federação antes da temporada): o Ruch, 6º na liga; a Wisła venceu a liga
- 1954: Wawel Cracóvia saiu do campeonato e teve os jogos anulados (linha vazia na tabela da Wikipédia)
- 1986/87: os pontos de bônus estão em ajuste_pontos
- 1987/88: os pontos de bônus estão em ajuste_pontos
- 1988/89: os pontos de bônus estão em ajuste_pontos
- 1989/90: os pontos de bônus estão em ajuste_pontos
- 1992/93: dois jogos da última rodada anulados pela federação (ŁKS 7-1 Olimpia Poznań e Wisła 0-6 Legia, suspeita de manipulação): Legia e ŁKS, 1º e 2º no campo, perderam a vantagem e o título foi do Lech
- 1993/94: punições: Legia Varsóvia -3 pontos; ŁKS Łódź -3 pontos; Wisła Cracóvia -3 pontos
- 2009/10: punições: Jagiellonia Białystok -10 pontos
- 2012/13: punições: Zagłębie Lubin -3 pontos
- 2013/14: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2014/15: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2015/16: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2016/17: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2017/18: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2018/19: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2019/20: pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)
- 2020/21: punições: Cracovia -5 pontos
- 2025/26: punições: Lechia Gdańsk -5 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Legia Varsóvia: 15
- Ruch Chorzów: 14
- Górnik Zabrze: 14
- Wisła Cracóvia: 13
- Lech Poznań: 10
- Cracovia: 5
- Pogoń Lwów: 4
- Widzew Łódź: 4
- Warta Poznań: 2
- Polonia Varsóvia: 2
- Polonia Bytom: 2
- ŁKS Łódź: 2
- Stal Mielec: 2
- Śląsk Wrocław: 2
- Zagłębie Lubin: 2
- Garbarnia Cracóvia: 1
- Szombierki Bytom: 1
- Piast Gliwice: 1
- Raków Częstochowa: 1
- Jagiellonia Białystok: 1

**Rebaixamentos:** 207 no total; quem mais caiu: Cracovia (8), ŁKS Łódź (8), Pogoń Szczecin (7), Polonia Varsóvia (6), Polonia Bytom (6).

**Punições em pontos:**

- 1986/87: Górnik Zabrze 7
- 1986/87: Pogoń Szczecin 4
- 1986/87: GKS Katowice 5
- 1986/87: Śląsk Wrocław 3
- 1986/87: Widzew Łódź 1
- 1986/87: ŁKS Łódź 1
- 1986/87: Górnik Wałbrzych -2
- 1986/87: Lechia Gdańsk 1
- 1986/87: Olimpia Poznań -4
- 1986/87: Polonia Bytom -3
- 1986/87: Ruch Chorzów -2
- 1986/87: Stal Mielec -3
- 1986/87: Motor Lublin -8
- 1987/88: Górnik Zabrze 6
- 1987/88: GKS Katowice 3
- 1987/88: Legia Varsóvia 1
- 1987/88: ŁKS Łódź 2
- 1987/88: Szombierki Bytom -1
- 1987/88: Lech Poznań -1
- 1987/88: Pogoń Szczecin -1
- 1987/88: Zagłębie Lubin -1
- 1987/88: Olimpia Poznań -1
- 1987/88: Górnik Wałbrzych 1
- 1987/88: Bałtyk Gdynia -3
- 1987/88: Stal Stalowa Wola -5
- 1988/89: Ruch Chorzów 6
- 1988/89: GKS Katowice 5
- 1988/89: Górnik Zabrze 6
- 1988/89: Legia Varsóvia 6
- 1988/89: Lech Poznań 1
- 1988/89: Widzew Łódź -1
- 1988/89: Jagiellonia Białystok -1
- 1988/89: ŁKS Łódź -1
- 1988/89: Olimpia Poznań -2
- 1988/89: Wisła Cracóvia -3
- 1988/89: Pogoń Szczecin -3
- 1988/89: GKS Jastrzębie -5
- 1988/89: Górnik Wałbrzych -4
- 1988/89: Szombierki Bytom -4
- 1989/90: Lech Poznań 4
- 1989/90: Zagłębie Lubin 2
- 1989/90: GKS Katowice 2
- 1989/90: Zawisza Bydgoszcz 4
- 1989/90: Olimpia Poznań 2
- 1989/90: Legia Varsóvia -1
- 1989/90: Wisła Cracóvia 3
- 1989/90: Śląsk Wrocław 1
- 1989/90: Motor Lublin -4
- 1989/90: Zagłębie Sosnowiec -4
- 1989/90: Widzew Łódź -3
- 1989/90: Jagiellonia Białystok -6
- 1993/94: Legia Varsóvia -3
- 1993/94: ŁKS Łódź -3
- 1993/94: Wisła Cracóvia -3
- 2009/10: Jagiellonia Białystok -10
- 2012/13: Zagłębie Lubin -3
- 2013/14: Legia Varsóvia -31
- 2013/14: Lech Poznań -26
- 2013/14: Ruch Chorzów -25
- 2013/14: Lechia Gdańsk -20
- 2013/14: Wisła Cracóvia -22
- 2013/14: Górnik Zabrze -21
- 2013/14: Pogoń Szczecin -23
- 2013/14: Zawisza Bydgoszcz -21
- 2013/14: Śląsk Wrocław -17
- 2013/14: Podbeskidzie -15
- 2013/14: Jagiellonia Białystok -19
- 2013/14: Piast Gliwice -17
- 2013/14: Korona Kielce -18
- 2013/14: Cracovia -19
- 2013/14: Widzew Łódź -11
- 2013/14: Zagłębie Lubin -14
- 2014/15: Lech Poznań -27
- 2014/15: Legia Varsóvia -28
- 2014/15: Jagiellonia Białystok -24
- 2014/15: Śląsk Wrocław -23
- 2014/15: Lechia Gdańsk -20
- 2014/15: Wisła Cracóvia -21
- 2014/15: Górnik Zabrze -21
- 2014/15: Pogoń Szczecin -20
- 2014/15: Cracovia -18
- 2014/15: Ruch Chorzów -16
- 2014/15: Korona Kielce -19
- 2014/15: Piast Gliwice -19
- 2014/15: Podbeskidzie -19
- 2014/15: Górnik Łęczna -17
- 2014/15: Zawisza Bydgoszcz -14
- 2014/15: GKS Bełchatów -15
- 2015/16: Legia Varsóvia -30
- 2015/16: Piast Gliwice -29
- 2015/16: Zagłębie Lubin -22
- 2015/16: Cracovia -22
- 2015/16: Lechia Gdańsk -20
- 2015/16: Pogoń Szczecin -23
- 2015/16: Lech Poznań -21
- 2015/16: Ruch Chorzów -20
- 2015/16: Wisła Cracóvia -19
- 2015/16: Śląsk Wrocław -17
- 2015/16: Jagiellonia Białystok -17
- 2015/16: Korona Kielce -18
- 2015/16: Termalica Nieciecza -16
- 2015/16: Górnik Łęczna -15
- 2015/16: Górnik Zabrze -13
- 2015/16: Podbeskidzie -19
- 2016/17: Legia Varsóvia -29
- 2016/17: Jagiellonia Białystok -29
- 2016/17: Lech Poznań -27
- 2016/17: Lechia Gdańsk -26
- 2016/17: Korona Kielce -19
- 2016/17: Wisła Cracóvia -22
- 2016/17: Pogoń Szczecin -21
- 2016/17: Termalica Nieciecza -21
- 2016/17: Zagłębie Lubin -19
- 2016/17: Piast Gliwice -15
- 2016/17: Śląsk Wrocław -17
- 2016/17: Wisła Płock -19
- 2016/17: Arka Gdynia -15
- 2016/17: Cracovia -15
- 2016/17: Górnik Łęczna -15
- 2016/17: Ruch Chorzów -19
- 2017/18: Lechia Gdańsk -1
- 2020/21: Cracovia -5
- 2025/26: Lechia Gdańsk -5

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/pol-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1994/95 · Olimpia Poznań:** fundiu-se com o Lechia Gdańsk (Olimpia/Lechia Gdańsk, que ficou com a vaga em 1995/96)
- **1994/95 · Sokół Pniewy:** mudou-se para Tychy (Sokół Tychy, hoje GKS Tychy, que ficou com a vaga em 1995/96)
- **2005/06 · Amica Wronki:** fundiu-se com o Lech Poznań depois da temporada (nota da tabela da Wikipédia)
- **2007/08 · Dyskobolia:** fundiu-se com a Polonia Varsóvia, que ficou com a vaga em 2008/09

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1922:** a Wikipédia polonesa dá Warta 23:6, Pogoń 37:6 e Ruch 6:38 (gols), como os jogos; a Wikipédia em inglês e a RSSSF dão 33:6, 37:8 e 8:38 (https://pl.wikipedia.org/wiki/Mistrzostwa_Polski_w_piłce_nożnej_(1922))

### Desempates pelo título fora da tabela (`DESEMPATES`)

- **1948:** [('1948-12-05', 'Cracovia', 'Wisła Cracóvia', 3, 1, 'jogo extra pelo título: Cracovia e Wisła terminaram empatadas em pontos (38) (RSSSF e Wikipédia)')] 

## 8. O que não deu para coletar

- **Datas e rodadas de 1921 a 1962** (só a matriz de resultados, exceto as fichas da Wikipédia e a final de 1952).
- **Os jogos do grupo final de 1926:** nenhuma fonte traz (a Wikipédia polonesa só cita a vitória decisiva do Pogoń sobre a Polonia, 2-0, sem o mando); fica a tabela publicada.
- **Autores dos gols, cartões, público, estádio e árbitro:** nenhuma fonte em lote cobre a Polônia (sem ESPN; o football-data não traz cartões da Polônia); só a ficha de cada jogo no ogol.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Sem datas e rodadas de 1921 a 1962 (só as matrizes de resultados da Wikipédia e da RSSSF, fora as fichas das finais e do mata-mata de 1946); sem autores dos gols, cartões e público em toda a liga (sem ESPN; o football-data não traz cartões da Polônia).
- Grupo final de 1926 sem os jogos em nenhuma fonte (RSSSF, Wikipédia em inglês e em polonês): fica a tabela publicada.
- 9 temporadas antigas em que a matriz não fecha com as tabelas (que concordam entre si): a classificação fica com os números publicados.
- Fora do escopo (decisão do Guilherme, 25/11/2026): 1920 (abandonado), 1924 (não disputado), 1939 (interrompido) e as ligas municipais da guerra; os jogos de acesso contra a 2ª divisão.

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade pelos links da Wikipédia: o PKS Szczecin de 1946-47 como o Pogoń Szczecin, o Motor Białystok (1947) como o Jagiellonia, o Grochów (1947) como o Gwardia Varsóvia, o RKU Sosnowiec como o Zagłębie; o Olimpia/Lechia Gdańsk de 1995/96 à parte do Lechia (o ogol junta) e o Sokół Tychy como o GKS Tychy; o 22 pp Siedlce e o Strzelec Siedlce como um clube só (a RSSSF diz que mudou de nome).
- 1922: a RSSSF trocou as matrizes dos dois grupos; os jogos vêm da matriz certa, e os números fecham com a Wikipédia polonesa. 1951: campeão o Ruch (6º na liga, pela Copa); 1992/93: os dois jogos anulados ficam fora.
- Placares do ogol trocados pela matriz da Wikipédia só quando ela fecha melhor com as tabelas, ou empatada com o football-data ou a RSSSF a favor (2004/05, 2006/07, 2007/08, 2022/23, 2025/26); o ogol rotula o Zagłębie Sosnowiec de 1985/86 como Zagłębie Wałbrzych (os 30 placares são os do Sosnowiec).

## 10. Arquivos

- Código: `coleta/pol-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_pol.py`.
- Fontes baixadas: `data/coleta/pol-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-pol-1/`.
- Pacote: `data/coleta/pol-1/pacote/`; relatório: `docs/coleta/pol-1.md`.
- Refazer do zero: `python coleta/pol-1/baixar.py ...` (ver o docstring), `python coleta/pol-1/importar.py`, `python coleta/comum-europa/testar_carga.py pol-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

