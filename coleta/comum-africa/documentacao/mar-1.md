# Campeonato Marroquino (`mar-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/mar-1/pacote/`, do código `coleta/mar-1/` e do relatório `docs/coleta/mar-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 110, de 1915/16 a 2025/26; 41 sem jogos.
- **Jogos:** 11736 (11702 com placar); **gols:** 25105; **gols com autor:** 18 (0%); **cartões:** 0.
- **Clubes:** 100; **artilheiros:** 69 edições com artilheiro (77 linhas, com empates).
- **Classificação final:** 109 edições; **tabelas publicadas guardadas para conferência:** 1161 linhas.
- **No banco:** sim; **último commit do pacote:** 786998de.
- **Observação da competição:** 1ª divisão marroquina (hoje Botola Pro) de 1915/16 a 2025/26, com a era colonial (campeonato da USFSA e, desde 1922/23, da Liga do Marrocos), que a federação marroquina conta no palmarès. Sem 1955/56 (sem competição) e sem a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos); 1942/43 (abandonado) entra sem campeão. Pontos 3-2-1 (vitória, empate, derrota) até 1994/95.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão marroquina (mar-1): o campeonato do Marrocos de 1915/16 a 2025/26.

Lista de campeões: RSSSF (marochamp.html, 39 títulos de 1915/16 a 1954/55 e 70 desde 1956/57), conferida com a Wikipédia em
inglês. A era colonial entra (pesquisa de 24/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md): a federação
marroquina conta esses títulos (o site da FRMF, em 2015: "18º título do WAC desde 1948", 5 antes de 1956), e RSSSF,
Wikipédia e os clubes também. Era o campeonato do Marrocos inteiro: da USFSA até 1921/22 e da Liga do Marrocos (LMFA) de
1922/23 a 1954/55, às vezes em liga única, às vezes em ligas regionais com mata-mata nacional.
Ficam de fora: a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos, que ninguém conta no palmarès), 1955/56
(sem competição), as copas (Coupe du Sultan, Coupe Colonial, Coupe du Trône...) e a 2ª divisão. 1942/43 foi abandonado em
novembro de 1942 (desembarque aliado) e entra sem campeão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro; linha final None: até o primeiro
  título de outra competição (FIM_PADRAO). Página maroAA (ou maroAAAA desde 2010 e nos anos 1910): a do ano em que a
  temporada termina (maro96 = 1995/96); maro3944 traz de 1938/39 a 1944/45.
- matriz: tabela de confrontos da página (1956/57 a 1967/68, 1980/81, 1989/90, 1990/91), lida por ler_rsssf.matriz().
- ogol: o calendário do ogol é a base nos anos em que a RSSSF só tem a tabela.
- tabelas: trechos lidos só pelas tabelas.
- parcial: trecho de uma classificação incompleta (só posição, ou posição e pontos), lida por ler_rsssf.parcial().
Pontos: 3-2-1 (vitória, empate, derrota) até 1994/95, como as tabelas da RSSSF contam; 3-1-0 desde 1995/96. Antes de
1933/34 as páginas não dizem.
```

**Edições:** 110, uma por temporada, de 1915/16 a 2025/26, como na lista de campeões da RSSSF (`marochamp.html`, 39 títulos antes da independência e 70 depois) e na Wikipédia em inglês. A era colonial entra (pesquisa de 24/11/2026): a federação marroquina conta esses títulos no palmarès (o site da FRMF, em 2015: "18º título do WAC desde 1948", 5 antes de 1956), e a RSSSF, a Wikipédia e os clubes também. Até 1921/22 era o campeonato da USFSA; de 1922/23 a 1954/55, da Liga do Marrocos, às vezes em liga única, às vezes em ligas regionais com mata-mata nacional. 1942/43 foi abandonado (desembarque aliado) e entra sem campeão; 1955/56 não teve competição e fica de fora.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/mar-1/rsssf/`: base dos jogos de 1995/96 a 2024/25, com rodadas, datas e, em parte dos anos, autores dos gols; a tabela de confrontos de 1956/57 a 1967/68, 1980/81, 1989/90 e 1990/91, sem datas; nos outros anos, a tabela final ou a classificação incompleta; na era colonial, os jogos que a página traz); ogol (base dos jogos de 2010/11, 2011/12 e 2025/26; de 2004/05 em diante, conferência, rodada e data; antes de 2004/05 não tem os jogos); Wikipédia em inglês (lista de campeões, com vice e artilheiro, e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga marroquina.

**Clubes:** o nome pelo qual o clube é conhecido (Wydad Casablanca, Raja Casablanca, FAR Rabat, RS Berkane...). Mesmo clube com outro nome é um só (Racing Casablanca = Racing AC = ADM Casablanca, como a RSSSF conta os títulos; AS Salé = SA Salé = Sporting Salé). Regras em `coleta/mar-1/clubes_mar.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada pela RSSSF (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. "A bt B" (venceu, sem placar conhecido) entra como vitória sem placar. Autores dos gols só entram quando a soma bate com o placar. Pontos: 3-2-1 (vitória, empate, derrota) de 1933/34 a 1994/95, como as tabelas contam (o `ajuste_pontos` já usa esse sistema); 3-1-0 desde 1995/96.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 35.
- **Edições com alguma tabela divergente** (20; motivo no relatório, na edição): 1933/34, 1941/42, 1947/48, 1956/57, 1957/58, 1958/59, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1965/66, 1966/67, 1967/68, 1980/81, 1989/90, 1999/00, 2003/04, 2008/09, 2010/11.
- **Edições sem tabela para conferir** (55): 1915/16, 1916/17, 1917/18, 1918/19, 1919/20, 1920/21, 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929/30, 1930/31, 1931/32, 1932/33, 1939/40, 1940/41, 1942/43, 1943/44, 1944/45, 1945/46, 1948/49, 1949/50, 1950/51, 1951/52, 1952/53, 1953/54, 1954/55, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1981/82, 1982/83, 1983/84, 1984/85, 1985/86, 1986/87, 1987/88, 1988/89, 1991/92, 1992/93, 1993/94, 1994/95.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1910s | 5 | 9 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 10 | 17 | 71% | 0% | 71% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 10 | 431 | 97% | 0% | 94% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 10 | 536 | 94% | 0% | 84% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 9 | 803 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 1638 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 620 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1441 | 57% | 0% | 83% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2010s | 10 | 2401 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1440 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1915/16: 8 clubes
- 1916/17: 6 clubes
- 1917/18 a 1921/22: 1 clubes
- 1922/23: 4 clubes
- 1923/24: 1 clubes
- 1924/25: 2 clubes
- 1925/26 a 1927/28: 1 clubes
- 1928/29: 2 clubes
- 1929/30: 12 clubes
- 1930/31: 6 clubes
- 1931/32: 14 clubes
- 1932/33: 8 clubes
- 1933/34: 10 clubes
- 1934/35 a 1937/38: 8 clubes
- 1938/39: 10 clubes
- 1939/40: 7 clubes
- 1940/41: 9 clubes
- 1941/42: 10 clubes
- 1942/43: 0 clubes
- 1943/44: 16 clubes
- 1944/45: 20 clubes
- 1945/46: 13 clubes
- 1946/47: 14 clubes
- 1947/48: 10 clubes
- 1948/49 a 1950/51: 12 clubes
- 1951/52: 4 clubes
- 1952/53: 12 clubes
- 1953/54: 1 clubes
- 1954/55: 12 clubes
- 1956/57: 16 clubes
- 1957/58: 15 clubes
- 1958/59 a 1965/66: 14 clubes
- 1966/67: 16 clubes
- 1967/68: 18 clubes
- 1968/69 a 1969/70: 16 clubes
- 1970/71: 2 clubes
- 1971/72 a 1972/73: 16 clubes
- 1973/74: 2 clubes
- 1974/75 a 1978/79: 16 clubes
- 1979/80: 15 clubes
- 1980/81: 20 clubes
- 1981/82: 2 clubes
- 1982/83 a 1984/85: 16 clubes
- 1985/86: 20 clubes
- 1986/87: 24 clubes
- 1987/88: 18 clubes
- 1988/89 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1915/16 a 2025/26: 3

**Nome oficial:**

- 1915/16 a 1921/22: Championnat officiel de l'USFSA
- 1922/23 a 1954/55: Championnat du Maroc (Ligue du Maroc de Football Association)
- 1956/57 a 2025/26: Championnat National de 1ère Division

**Formato** (fases na ordem, do edicoes.csv):

- 1915/16: sem jogos (só a classificação incompleta)
- 1916/17: jogos incompletos (só os resultados conhecidos e a final)
- 1917/18 a 1921/22: sem jogos (só o campeão)
- 1922/23: jogos incompletos (ligas regionais sem jogos; só as semifinais e a final)
- 1923/24: sem jogos (só o campeão)
- 1924/25: jogos incompletos (ligas regionais sem jogos; só a final)
- 1925/26 a 1927/28: sem jogos (só o campeão)
- 1928/29: jogos incompletos (só a final)
- 1929/30: jogos incompletos (ligas regionais com poucos jogos; o mata-mata final completo)
- 1930/31: jogos incompletos (só o mata-mata final)
- 1931/32: jogos incompletos (dois grupos com os resultados conhecidos e a final)
- 1932/33: jogos incompletos (resultados conhecidos; classificação em 20/02 com jogos e pontos)
- 1933/34 a 1934/35: pontos corridos
- 1935/36: pontos corridos + desempate + mata-mata
- 1936/37 a 1937/38: pontos corridos + desempate
- 1938/39: pontos corridos
- 1939/40 a 1940/41: jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)
- 1941/42: pontos corridos
- 1942/43: temporada não terminada
- 1943/44 a 1944/45: jogos incompletos (quatro ligas regionais com os resultados conhecidos e o mata-mata nacional)
- 1945/46: jogos incompletos (ligas regionais quase sem jogos; o mata-mata nacional completo)
- 1946/47: pontos corridos + desempate
- 1947/48: pontos corridos
- 1948/49: jogos incompletos (as rodadas que a página traz e outros jogos do WAC; classificação só com pontos)
- 1949/50 a 1953/54: sem jogos (só a classificação incompleta)
- 1954/55: sem jogos (só a tabela final)
- 1956/57 a 1958/59: pontos corridos
- 1959/60: pontos corridos + desempate
- 1960/61 a 1967/68: pontos corridos
- 1968/69 a 1969/70: sem jogos (só a tabela final)
- 1970/71: sem jogos (só o campeão e o vice)
- 1971/72 a 1972/73: sem jogos (só a tabela final)
- 1973/74: sem jogos (só o campeão e o vice)
- 1974/75 a 1979/80: sem jogos (só a tabela final)
- 1980/81: pontos corridos
- 1981/82: sem jogos (só o campeão e o vice)
- 1982/83 a 1988/89: sem jogos (só a tabela final)
- 1989/90 a 1990/91: pontos corridos
- 1991/92 a 1992/93: sem jogos (só a tabela final)
- 1993/94: sem jogos (só a classificação incompleta)
- 1994/95: sem jogos (só a tabela final)
- 1995/96 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1916/17: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1922/23: Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1929/30: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1930/31: Quartas de final (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1931/32: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1935/36: Primeira fase (liga); Desempate do 6º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1936/37: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1937/38: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1939/40: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1940/41: Primeira fase (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1943/44: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Mata-mata final (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1944/45: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Mata-mata final (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1945/46: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1946/47: Primeira fase (liga); Desempate do 9º lugar (mata_mata, jogo_unico); Desempate do título (mata_mata, jogo_unico)
- 1959/60: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 85 edições
- calculada com os jogos que a página traz: 12 edições
- lista de campeões da RSSSF: 12 edições

**Observações das edições:**

- 1915/16: a RSSSF traz só a ordem final (sem jogos nem pontos)
- 1917/18: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1918/19: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1919/20: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1920/21: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1921/22: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1923/24: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1925/26: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1926/27: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1927/28: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1933/34: pontos 3-2-1 (vitória, empate, derrota)
- 1934/35: pontos 3-2-1 (vitória, empate, derrota)
- 1935/36: pontos 3-2-1 (vitória, empate, derrota)
- 1936/37: pontos 3-2-1 (vitória, empate, derrota)
- 1937/38: pontos 3-2-1 (vitória, empate, derrota)
- 1938/39: pontos 3-2-1 (vitória, empate, derrota)
- 1939/40: pontos 3-2-1 (vitória, empate, derrota)
- 1940/41: pontos 3-2-1 (vitória, empate, derrota)
- 1941/42: pontos 3-2-1 (vitória, empate, derrota)
- 1942/43: temporada não terminada: abandonada em novembro de 1942, com o desembarque aliado no Marrocos; no lugar dela houve a Coupe de la Guerre (a US Marocaine ganhou), que não conta como título; pontos 3-2-1 (vitória, empate, derrota)
- 1943/44: pontos 3-2-1 (vitória, empate, derrota)
- 1944/45: pontos 3-2-1 (vitória, empate, derrota)
- 1945/46: pontos 3-2-1 (vitória, empate, derrota)
- 1946/47: campeão: USA Casablanca, que venceu o desempate do título (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine, 3ª colocada (erro da lista); pontos 3-2-1 (vitória, empate, derrota)
- 1947/48: pontos 3-2-1 (vitória, empate, derrota)
- 1948/49: pontos 3-2-1 (vitória, empate, derrota)
- 1949/50: a RSSSF traz só a classificação (a maioria dos clubes só com os pontos); pontos 3-2-1 (vitória, empate, derrota)
- 1950/51: a RSSSF traz só a classificação (a maioria dos clubes só com os pontos); pontos 3-2-1 (vitória, empate, derrota)
- 1951/52: a RSSSF traz só a classificação (a maioria dos clubes só com os pontos); pontos 3-2-1 (vitória, empate, derrota)
- 1952/53: a RSSSF traz só a classificação (a maioria dos clubes só com os pontos); pontos 3-2-1 (vitória, empate, derrota)
- 1953/54: a RSSSF traz só a classificação (a maioria dos clubes só com os pontos); pontos 3-2-1 (vitória, empate, derrota)
- 1954/55: a RSSSF traz a tabela publicada na época, que ela mesma diz estar "cheia de absurdos"; pontos 3-2-1 (vitória, empate, derrota)
- 1956/57: pontos 3-2-1 (vitória, empate, derrota)
- 1957/58: pontos 3-2-1 (vitória, empate, derrota)
- 1958/59: pontos 3-2-1 (vitória, empate, derrota)
- 1959/60: pontos 3-2-1 (vitória, empate, derrota)
- 1960/61: pontos 3-2-1 (vitória, empate, derrota)
- 1961/62: pontos 3-2-1 (vitória, empate, derrota)
- 1962/63: pontos 3-2-1 (vitória, empate, derrota)
- 1963/64: pontos 3-2-1 (vitória, empate, derrota)
- 1964/65: pontos 3-2-1 (vitória, empate, derrota)
- 1965/66: pontos 3-2-1 (vitória, empate, derrota)
- 1966/67: pontos 3-2-1 (vitória, empate, derrota)
- 1967/68: pontos 3-2-1 (vitória, empate, derrota)
- 1968/69: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1969/70: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1970/71: a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista; pontos 3-2-1 (vitória, empate, derrota)
- 1971/72: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1972/73: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1973/74: a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista; pontos 3-2-1 (vitória, empate, derrota)
- 1974/75: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1975/76: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1976/77: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1977/78: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1978/79: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1979/80: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1980/81: pontos 3-2-1 (vitória, empate, derrota)
- 1981/82: a RSSSF não tem página deste ano e o ogol não tem os jogos: só o campeão e o vice da lista; pontos 3-2-1 (vitória, empate, derrota)
- 1982/83: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1983/84: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1984/85: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1985/86: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1986/87: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1987/88: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1988/89: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1989/90: pontos 3-2-1 (vitória, empate, derrota)
- 1990/91: pontos 3-2-1 (vitória, empate, derrota)
- 1991/92: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1992/93: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 1993/94: a RSSSF traz só a classificação, com os pontos (jogos, vitórias e gols só de alguns clubes); pontos 3-2-1 (vitória, empate, derrota)
- 1994/95: a RSSSF traz só a tabela final, e o ogol não tem os jogos deste ano; pontos 3-2-1 (vitória, empate, derrota)
- 2010/11: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 2011/12: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 2025/26: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Wydad Casablanca: 22
- US Marocaine: 15
- FAR Rabat: 13
- Raja Casablanca: 13
- Olympique Marocain: 6
- MAS Fès: 5
- KAC Kénitra: 4
- USA Casablanca: 3
- Stade Marocain: 3
- Racing Casablanca: 3
- US Fès: 2
- Kawkab Marrakech: 2
- Hassania Agadir: 2
- Moghreb Tétouan: 2
- CA Marocain: 1
- USD Meknès: 1
- SA Marrakech: 1
- EJS Casablanca: 1
- RS Settat: 1
- Raja Béni Mellal: 1
- MC Oujda: 1
- Chabab Mohammédia: 1
- Olympique de Casablanca: 1
- CODM Meknès: 1
- OC Khouribga: 1
- FUS Rabat: 1
- IR Tanger: 1
- RS Berkane: 1
- Sem campeão: 1942/43

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1915/16 | CA Marocain | US Marocaine |
| 1916/17 | US Marocaine | Rabat FC |
| 1917/18 | US Marocaine | — |
| 1918/19 | US Marocaine | — |
| 1919/20 | US Marocaine | — |
| 1920/21 | Olympique Marocain | — |
| 1921/22 | USD Meknès | — |
| 1922/23 | Olympique Marocain | Racing Club Marocain |
| 1923/24 | Olympique Marocain | — |
| 1924/25 | US Fès | Olympique Marocain |
| 1925/26 | US Fès | — |
| 1926/27 | USA Casablanca | — |
| 1927/28 | Stade Marocain | — |
| 1928/29 | USA Casablanca | Racing Casablanca |
| 1929/30 | Olympique Marocain | Stade Marocain |
| 1930/31 | Stade Marocain | US Marocaine |
| 1931/32 | US Marocaine | ASPTT Casablanca |
| 1932/33 | US Marocaine | ASPTT Casablanca |
| 1933/34 | US Marocaine | Racing Casablanca |
| 1934/35 | US Marocaine | Stade Marocain |
| 1935/36 | Olympique Marocain | US Marocaine |
| 1936/37 | Olympique Marocain | SA Marrakech |
| 1937/38 | US Marocaine | SA Marrakech |
| 1938/39 | US Marocaine | Stade Marocain |
| 1939/40 | US Marocaine | Wydad Casablanca |
| 1940/41 | US Marocaine | USA Casablanca |
| 1941/42 | US Marocaine | Olympique Marocain |
| 1942/43 | — | — |
| 1943/44 | Stade Marocain | US Marocaine |
| 1944/45 | Racing Casablanca | US Marocaine |
| 1945/46 | US Marocaine | Wydad Casablanca |
| 1946/47 | USA Casablanca | ASPTT Casablanca |
| 1947/48 | Wydad Casablanca | USA Casablanca |
| 1948/49 | Wydad Casablanca | USD Meknès |
| 1949/50 | Wydad Casablanca | USD Meknès |
| 1950/51 | Wydad Casablanca | US Marocaine |
| 1951/52 | US Marocaine | Wydad Casablanca |
| 1952/53 | SA Marrakech | US Marocaine |
| 1953/54 | Racing Casablanca | — |
| 1954/55 | Wydad Casablanca | Kawkab Marrakech |
| 1956/57 | Wydad Casablanca | Kawkab Marrakech |
| 1957/58 | Kawkab Marrakech | Wydad Casablanca |
| 1958/59 | EJS Casablanca | Wydad Casablanca |
| 1959/60 | KAC Kénitra | FAR Rabat |
| 1960/61 | FAR Rabat | MAS Fès |
| 1961/62 | FAR Rabat | Racing Casablanca |
| 1962/63 | FAR Rabat | Kawkab Marrakech |
| 1963/64 | FAR Rabat | Stade Marocain |
| 1964/65 | MAS Fès | Racing Casablanca |
| 1965/66 | Wydad Casablanca | Raja Casablanca |
| 1966/67 | FAR Rabat | RS Settat |
| 1967/68 | FAR Rabat | RS Settat |
| 1968/69 | Wydad Casablanca | MAS Fès |
| 1969/70 | FAR Rabat | US Sidi Kacem |
| 1970/71 | RS Settat | FAR Rabat |
| 1971/72 | Racing Casablanca | Wydad Casablanca |
| 1972/73 | KAC Kénitra | FUS Rabat |
| 1973/74 | Raja Béni Mellal | FUS Rabat |
| 1974/75 | MC Oujda | MAS Fès |
| 1975/76 | Wydad Casablanca | DH El Jadida |
| 1976/77 | Wydad Casablanca | MC Oujda |
| 1977/78 | Wydad Casablanca | MAS Fès |
| 1978/79 | MAS Fès | KAC Kénitra |
| 1979/80 | Chabab Mohammédia | Wydad Casablanca |
| 1980/81 | KAC Kénitra | FUS Rabat |
| 1981/82 | KAC Kénitra | Wydad Casablanca |
| 1982/83 | MAS Fès | RS Berkane |
| 1983/84 | FAR Rabat | OC Khouribga |
| 1984/85 | MAS Fès | KAC Kénitra |
| 1985/86 | Wydad Casablanca | Raja Casablanca |
| 1986/87 | FAR Rabat | Kawkab Marrakech |
| 1987/88 | Raja Casablanca | Kawkab Marrakech |
| 1988/89 | FAR Rabat | MAS Fès |
| 1989/90 | Wydad Casablanca | IR Tanger |
| 1990/91 | Wydad Casablanca | FAR Rabat |
| 1991/92 | Kawkab Marrakech | Raja Casablanca |
| 1992/93 | Wydad Casablanca | Raja Casablanca |
| 1993/94 | Olympique de Casablanca | Wydad Casablanca |
| 1994/95 | CODM Meknès | Olympique de Casablanca |
| 1995/96 | Raja Casablanca | OC Khouribga |
| 1996/97 | Raja Casablanca | Wydad Casablanca |
| 1997/98 | Raja Casablanca | Kawkab Marrakech |
| 1998/99 | Raja Casablanca | Kawkab Marrakech |
| 1999/00 | Raja Casablanca | Wydad Casablanca |
| 2000/01 | Raja Casablanca | FUS Rabat |
| 2001/02 | Hassania Agadir | Wydad Casablanca |
| 2002/03 | Hassania Agadir | Raja Casablanca |
| 2003/04 | Raja Casablanca | FAR Rabat |
| 2004/05 | FAR Rabat | Raja Casablanca |
| 2005/06 | Wydad Casablanca | FAR Rabat |
| 2006/07 | OC Khouribga | FAR Rabat |
| 2007/08 | FAR Rabat | IZ Khémisset |
| 2008/09 | Raja Casablanca | DH El Jadida |
| 2009/10 | Wydad Casablanca | Raja Casablanca |
| 2010/11 | Raja Casablanca | MAS Fès |
| 2011/12 | Moghreb Tétouan | FUS Rabat |
| 2012/13 | Raja Casablanca | FAR Rabat |
| 2013/14 | Moghreb Tétouan | Raja Casablanca |
| 2014/15 | Wydad Casablanca | OC Khouribga |
| 2015/16 | FUS Rabat | Wydad Casablanca |
| 2016/17 | Wydad Casablanca | DH El Jadida |
| 2017/18 | IR Tanger | Wydad Casablanca |
| 2018/19 | Wydad Casablanca | Raja Casablanca |
| 2019/20 | Raja Casablanca | Wydad Casablanca |
| 2020/21 | Wydad Casablanca | Raja Casablanca |
| 2021/22 | Wydad Casablanca | Raja Casablanca |
| 2022/23 | FAR Rabat | Wydad Casablanca |
| 2023/24 | Raja Casablanca | FAR Rabat |
| 2024/25 | RS Berkane | FAR Rabat |
| 2025/26 | MAS Fès | RS Berkane |

**Rebaixados marcados na classificação:** 143 em 66 edições (só onde a tabela publicada marca a queda); quem mais caiu: Moghreb Tétouan (9), Chabab Mohammédia (7), CODM Meknès (6), Raja Béni Mellal (6), Kawkab Marrakech (6).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1941/42: AS Casablanca -1
- 1949/50: Wydad Casablanca -1
- 1954/55: Racing Casablanca -2
- 1954/55: USA Casablanca -2
- 1954/55: MC Oujda -2
- 1954/55: Stade Marocain -4
- 1954/55: SA Marrakech -4
- 1954/55: USD Meknès -6
- 1954/55: US Marocaine -6
- 1954/55: FUS Rabat -2
- 1954/55: AS Tanger-Fès -6
- 1954/55: Chabab Mohammédia -6
- 1972/73: MAS Fès -1
- 1974/75: MC Oujda -1
- 1976/77: US Sidi Kacem -1
- 1978/79: Raja Casablanca -1
- 2000/01: Wydad Casablanca -1
- 2001/02: Raja Béni Mellal -2
- 2003/04: RS Settat -2
- 2005/06: Union Touarga -2
- 2011/12: CODM Meknès -1
- 2013/14: Chabab Rif Hoceima -1
- 2013/14: OC Khouribga -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/mar-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **maro95 · 20:** «Credit Agricole Rabat30» → «Credit Agricole Rabat 30»: nome grudado no número: a linha não era lida e a tabela se partia em duas

### Divergências entre fontes já explicadas (`EXPLICACOES`, 16)

- **1933/34:** dois jogos da página não têm placar ("drw", empate sem placar conhecido: Racing Casablanca x SA Marrakech na 6ª rodada e ASPTT Casablanca x Roches Noires na 12ª) e ficam de fora, como no ven-1; por isso esses quatro clubes têm um jogo e um empate a menos que a tabela
- **1954/55:** a tabela é a publicada na época, que a própria RSSSF diz estar "cheia de absurdos" (as linhas não fecham com o sistema 3-2-1); entra como está, só como classificação
- **1959/60:** Kénitra, FAR e Raja terminaram empatados em pontos; o triangular do título virou um jogo só (KAC Kénitra 3-1 FAR), porque o Raja se recusou a jogar, dizendo que o título era dele pelo goal average
- **1959/60:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1956/57:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1957/58:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1958/59:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1960/61:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1961/62:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1962/63:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1963/64:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1965/66:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1966/67:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1967/68:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1980/81:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada
- **1989/90:** a tabela de confrontos e a tabela final da página não concordam em alguns resultados (vitórias, empates e derrotas diferentes com os mesmos gols, o que indica pontos dados fora de campo ou erro de digitação numa das duas); não há terceira fonte para esses anos (os artigos da Wikipédia são só esboços). Os jogos são os da tabela de confrontos; a classificação é a tabela publicada

### Identidade dos clubes

Regras em `coleta/mar-1/clubes_mar.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes marroquinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Wydad Casablanca", "Raja Casablanca", "FAR Rabat", "RS Berkane");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Racing Casablanca (era colonial), Racing Athletic Club (RAC) e ADM Casablanca (Association des Douanes Marocaines,
    1968-1972) são um clube só, como a RSSSF conta os títulos ("3 Racing (ADM) Casablanca");
  - US Safi (colonial) = Union Sportive de Safi (1957/58); AS Tanger-Fès (colonial) = Association Sportive de Tanger-Fès
    (1957/58); Stade Marocain (Rabat) é o mesmo antes e depois de 1956;
  - AS Salé = SA Salé = Sporting Salé (as três grafias nunca aparecem juntas);
  - Tihad Athletic Sport = TAS Casablanca = Tihad Sportif;
- clubes diferentes com nome parecido ficam separados: o Olympique Casablanca da era colonial (ligas de 1939 a 1945) e o
  Olympique de Casablanca (OC, campeão de 1993/94, fundido ao Raja em 1995); o Racing Club Marocain (1915-1922) e o Racing
  Casablanca; a Union Athlétique de Kénitra (1915-1931) e o KAC Kénitra; o US Safi e o Olympic Safi.
- siglas e nomes curtos dos anos 1990 ("Fes", "Raja", "KAC", "Marrakesh") resolvem pelo clube da 1ª divisão do ano: "KAC"
  sozinho é o Kénitra e "KACM" o Kawkab de Marrakech.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos, que nenhuma lista de títulos conta), a Coupe du Trône e as outras copas, a 2ª divisão e os jogos de promoção.
- **Edições sem jogos** (41): 1915/16, 1917/18, 1918/19, 1919/20, 1920/21, 1921/22, 1923/24, 1925/26, 1926/27, 1927/28, 1942/43, 1949/50, 1950/51, 1951/52, 1952/53, 1953/54, 1954/55, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1981/82, 1982/83, 1983/84, 1984/85, 1985/86, 1986/87, 1987/88, 1988/89, 1991/92, 1992/93, 1993/94, 1994/95.
- **Décadas com menos da metade dos gols com autor:** 1910s, 1920s, 1930s, 1940s, 1950s, 1960s, 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1910s, 1920s, 1930s, 1940s, 1950s, 1960s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).
- Era colonial (1915/16 a 1954/55): 9 anos sem página da RSSSF (só o campeão); nos outros, jogos incompletos (ligas regionais com os resultados conhecidos e o mata-mata nacional) ou só a classificação (1949/50 a 1953/54, a maioria dos clubes só com os pontos). Fonte que resolveria: os jornais da época (Le Petit Marocain, La Vigie Marocaine) na Gallica (BnF).
- 1968/69 a 1994/95 (fora 1980/81, 1989/90 e 1990/91): só a tabela final; o ogol só tem os jogos de 2004/05 em diante. 1970/71, 1973/74 e 1981/82 sem página da RSSSF: só o campeão e o vice.
- Tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90): os jogos não têm data nem rodada, e vários resultados não batem com a tabela final da página (vitórias e empates trocados com os mesmos gols); sem terceira fonte.
- Autores dos gols quase nenhum (a RSSSF do Marrocos não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo (2004/05 em diante).
- Identidade a conferir: Racing Casablanca (colonial) = Racing AC = ADM Casablanca (como a RSSSF conta); AS Salé = SA Salé = Sporting Salé; JS Massira = Forces Auxiliaires (a página de 1994/95 diz que o clube mudou para El Ayoun); "ASM" (1957/58) sem nome completo; "US Casablanca" = USA Casablanca.
- 1946/47: campeão USA Casablanca (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine (erro da lista; avisar a RSSSF?).

## 10. Arquivos e comandos

Código em `coleta/mar-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão marroquina no ogol para data/coleta/mar-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão marroquina para data/coleta/mar-1/rsssf/: a lista de campeões (marochamp.html), as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) a lista de campeões ("List of Moroccan football champions"), o artigo |
| `clubes_mar.py` | Identidade dos clubes marroquinos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão marroquina (mar-1): o campeonato do Marrocos de 1915/16 a 2025/26. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão marroquina, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão marroquina e grava o pacote em data/coleta/mar-1/pacote/ e o relatório em docs/coleta/mar-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/mar-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/mar-1/wikipedia/en_<temporada>.txt) e a |

- Fontes baixadas: `data/coleta/mar-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-mar-1/`.
- Pacote: `data/coleta/mar-1/pacote/`; relatório: `docs/coleta/mar-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/mar-1/baixar_ogol.py
python coleta/mar-1/baixar_rsssf.py
python coleta/mar-1/baixar_wikipedia.py
python coleta/mar-1/importar.py
python coleta/mar-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py mar-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

