# Campeonato Tunisiano (`tun-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/tun-1/pacote/`, do código `coleta/tun-1/` e do relatório `docs/coleta/tun-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 109, de 1907 a 2025/26; 56 sem jogos.
- **Jogos:** 8092 (8079 com placar); **gols:** 17062; **gols com autor:** 771 (5%); **cartões:** 0.
- **Clubes:** 74; **artilheiros:** 71 edições com artilheiro (82 linhas, com empates).
- **Classificação final:** 109 edições; **tabelas publicadas guardadas para conferência:** 1118 linhas.
- **No banco:** sim; **último commit do pacote:** 786998de.
- **Observação da competição:** 1ª divisão tunisiana (hoje Ligue Professionnelle 1) de 1907 a 2025/26, com a era colonial (campeonato da USFSA até 1920/21 e da Liga da Tunísia de 1921/22 a 1954/55), que a contagem oficial inclui. Sem as temporadas sem competição; 1951/52 (abandonado) entra sem campeão. Pontos 3-2-1 até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0 desde 1995/96.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão tunisiana (tun-1): o campeonato da Tunísia de 1907 a 2025/26.

Lista de campeões: RSSSF (tunchamp.html), conferida com a Wikipédia em inglês ("List of Tunisian football champions", que
conta desde 1907). A era colonial entra (pesquisa de 24/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md): a
contagem oficial usada na Tunísia inclui esses títulos (o "34º título" do Espérance em 2024/25 só fecha com o de 1941/42;
o "14º" do Club Africain em 2025/26, com os de 1946/47 e 1947/48). Até 1920/21 era o campeonato da USFSA; de 1921/22 a
1954/55, da Liga da Tunísia, quase sempre com campeões regionais e uma final.
Ficam de fora as temporadas sem competição (1909/10, 1914/15 a 1918/19, 1939/40, 1940/41, 1942/43, 1943/44), as copas e a
2ª divisão. 1951/52 foi abandonado (agitação política de janeiro de 1952) e entra sem campeão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página tunAA (ou tunAAAA nos anos 1900-1910 e desde 2009): a do
  ano em que a temporada termina (tun97 = 1996/97; tun09 = 1908/09; tun2009 = 2008/09).
- hist: a tabela final vem da lista de tabelas finais da RSSSF (tunhist.html, 1955/56 a 2002/03), seção da temporada.
- matriz: tabela de confrontos da página da temporada (lida por ler_rsssf.matriz()).
- ogol: o calendário do ogol é a base nos anos em que a RSSSF só tem a tabela.
Pontos: 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0
desde 1995/96, como as tabelas da RSSSF contam.
```

**Edições:** 109, uma por temporada, de 1907 a 2025/26, como na lista de campeões da RSSSF (`tunchamp.html`) e na Wikipédia em inglês. A era colonial entra (pesquisa de 24/11/2026): a contagem oficial usada na Tunísia inclui esses títulos (o "34º título" do Espérance em 2024/25 só fecha com o de 1941/42; o "14º" do Club Africain em 2025/26, com os de 1946/47 e 1947/48). Até 1920/21 era o campeonato da USFSA; de 1921/22 a 1954/55, da Liga da Tunísia, quase sempre com campeões regionais e uma final. Ficam de fora as temporadas sem competição (1909/10, as das guerras mundiais e 1942/43 e 1943/44); 1951/52 foi abandonado e entra sem campeão. A Wikipédia lista um título do Racing Club de Tunis em 1909/10, que a RSSSF não traz: fica de fora.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/tun-1/rsssf/`: base dos jogos de 1996/97 a 2024/25; a tabela de confrontos de 1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e de 1987/88 a 1995/96, sem datas; a lista de tabelas finais `tunhist.html`, de 1955/56 a 2002/03; na era colonial, as finais que a página traz); ogol (base dos jogos de 2025/26; nos outros anos, conferência, rodada e data); Wikipédia em inglês (listas de campeões e de artilheiros e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga tunisiana.

**Clubes:** o nome pelo qual o clube é conhecido (Espérance de Tunis, Club Africain, Étoile du Sahel, CS Sfaxien...). Mesmo clube com outro nome é um só (Railway Sports de Sfax = Sfax Railways Sports; US Ferryville = USM Bourguiba; Olympique Tunis = US Musulmane Olympique). Regras em `coleta/tun-1/clubes_tun.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. "A bt B" (venceu, sem placar conhecido) entra como vitória sem placar. Pontos como as tabelas contam: 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0 desde 1995/96 (o `ajuste_pontos` já usa o sistema de cada ano).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 34.
- **Edições com alguma tabela divergente** (10; motivo no relatório, na edição): 1968/69, 1977/78, 1980/81, 1982/83, 1987/88, 1988/89, 1989/90, 1990/91, 1993/94, 1994/95.
- **Edições sem tabela para conferir** (65): 1907, 1908/09, 1910/11, 1911/12, 1912/13, 1913/14, 1919/20, 1920/21, 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929/30, 1930/31, 1931/32, 1932/33, 1933/34, 1934/35, 1935/36, 1936/37, 1937/38, 1938/39, 1941/42, 1944/45, 1945/46, 1946/47, 1947/48, 1948/49, 1949/50, 1950/51, 1951/52, 1952/53, 1953/54, 1954/55, 1955/56, 1956/57, 1957/58, 1958/59, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1964/65, 1965/66, 1966/67, 1967/68, 1969/70, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1978/79, 1979/80, 1981/82, 1983/84, 1984/85, 1985/86, 1986/87.
- **Edições com menos jogos que o esperado:** 1989/90 (181 de 182).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 2 | 4 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 5 | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1930s | 9 | 5 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 7 | 4 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 5 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 182 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 338 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 909 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1812 | 35% | 0% | 40% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 1625 | 100% | 0% | 100% | 0% | 0% | 0% | 11% | 0.0 |
| 2010s | 10 | 2016 | 100% | 0% | 100% | 0% | 0% | 0% | 9% | 0.0 |
| 2020s | 6 | 1190 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1907: 4 clubes
- 1908/09: 3 clubes
- 1910/11: 2 clubes
- 1911/12 a 1912/13: 1 clubes
- 1913/14: 3 clubes
- 1919/20 a 1930/31: 1 clubes
- 1931/32: 2 clubes
- 1932/33: 1 clubes
- 1933/34: 2 clubes
- 1934/35 a 1937/38: 1 clubes
- 1938/39: 2 clubes
- 1941/42 a 1948/49: 1 clubes
- 1949/50: 12 clubes
- 1950/51: 1 clubes
- 1951/52: 12 clubes
- 1952/53: 6 clubes
- 1953/54 a 1954/55: 1 clubes
- 1955/56 a 1956/57: 12 clubes
- 1957/58: 15 clubes
- 1958/59: 14 clubes
- 1959/60: 13 clubes
- 1960/61: 11 clubes
- 1961/62 a 1967/68: 12 clubes
- 1968/69 a 1969/70: 14 clubes
- 1970/71: 13 clubes
- 1971/72 a 1997/98: 14 clubes
- 1998/99: 16 clubes
- 1999/00 a 2003/04: 12 clubes
- 2004/05 a 2010/11: 14 clubes
- 2011/12 a 2016/17: 16 clubes
- 2017/18 a 2020/21: 14 clubes
- 2021/22 a 2022/23: 16 clubes
- 2023/24: 14 clubes
- 2024/25 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1907 a 1985/86: 3
- 1986/87 a 1991/92: 4
- 1992/93 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1907 a 1920/21: Championnat de Tunisie (USFSA)
- 1921/22 a 1954/55: Championnat de Tunisie (Ligue de Tunisie de Football)
- 1955/56 a 2025/26: Championnat National de Tunisie

**Formato** (fases na ordem, do edicoes.csv):

- 1907 a 1910/11: jogos incompletos (só a final do campeonato)
- 1911/12 a 1912/13: sem jogos (só o campeão)
- 1913/14: jogos incompletos (só a final do campeonato)
- 1919/20 a 1930/31: sem jogos (só o campeão)
- 1931/32: jogos incompletos (só a final do campeonato)
- 1932/33: sem jogos (só o campeão)
- 1933/34: jogos incompletos (só a final do campeonato)
- 1934/35 a 1937/38: sem jogos (só o campeão)
- 1938/39: jogos incompletos (só a final do campeonato)
- 1941/42 a 1948/49: sem jogos (só o campeão)
- 1949/50: jogos incompletos (só os resultados conhecidos)
- 1950/51: sem jogos (só o campeão)
- 1951/52: temporada não terminada
- 1952/53: jogos incompletos (cinco grupos regionais sem jogos; só o mata-mata final)
- 1953/54 a 1954/55: sem jogos (só o campeão)
- 1955/56 a 1967/68: sem jogos (só a tabela final)
- 1968/69: pontos corridos
- 1969/70: sem jogos (só a tabela final)
- 1970/71: pontos corridos
- 1971/72 a 1976/77: sem jogos (só a tabela final)
- 1977/78: pontos corridos
- 1978/79 a 1979/80: sem jogos (só a tabela final)
- 1980/81: pontos corridos
- 1981/82: sem jogos (só a tabela final)
- 1982/83: pontos corridos
- 1983/84 a 1986/87: sem jogos (só a tabela final)
- 1987/88 a 1997/98: pontos corridos
- 1998/99: 2 grupos + grupos do título e do rebaixamento
- 1999/00 a 2011/12: pontos corridos
- 2012/13: 2 grupos + jogos de classificação + fase final
- 2013/14 a 2015/16: pontos corridos
- 2016/17: 2 grupos + grupos do título e do rebaixamento
- 2017/18 a 2020/21: pontos corridos
- 2021/22: 2 grupos + jogos de classificação + grupos do título e do rebaixamento + desempate
- 2022/23: 2 grupos + grupos do título e do rebaixamento
- 2023/24: 2 grupos + grupos do título e do rebaixamento + desempate
- 2024/25 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1907: Primeira fase (liga); Final (mata_mata, jogo_unico)
- 1952/53: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1998/99: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 2012/13: Primeira fase (grupos, 2 grupos); Jogos de classificação (liga); Fase final (liga)
- 2016/17: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 2021/22: Primeira fase (grupos, 2 grupos); Jogos de classificação (liga); Grupo do rebaixamento (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Fase final (liga)
- 2022/23: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 2023/24: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Fase final (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 72 edições
- lista de campeões da RSSSF: 30 edições
- calculada com os jogos que a página traz: 7 edições

**Observações das edições:**

- 1911/12: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1912/13: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1919/20: a RSSSF traz só o campeão da Série 1 (e jogos da Série 2, a 2ª divisão)
- 1920/21: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1921/22: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1922/23: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1923/24: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1924/25: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1925/26: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1926/27: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1927/28: a RSSSF traz só o campeão (a tabela da página é da 3ª divisão)
- 1928/29: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1929/30: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1930/31: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1932/33: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1934/35: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1935/36: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1936/37: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1937/38: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1941/42: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1944/45: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1945/46: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1946/47: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1947/48: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1948/49: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1950/51: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1951/52: temporada não terminada: abandonada em janeiro de 1952 pela agitação política; nenhum título foi dado e todos os clubes ficaram na 1ª divisão (a tabela é a do abandono)
- 1952/53: campeonato boicotado pelos clubes nacionalistas e muçulmanos
- 1953/54: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1954/55: sem jogos: a RSSSF não tem página deste ano (só o campeão da lista)
- 1955/56: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1956/57: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1957/58: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1958/59: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1959/60: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1960/61: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1961/62: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1962/63: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1963/64: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1964/65: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1965/66: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1966/67: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1967/68: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1968/69: pontos 3-2-1 (vitória, empate, derrota)
- 1969/70: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1970/71: pontos 3-2-1 (vitória, empate, derrota)
- 1971/72: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1972/73: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1973/74: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1974/75: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1975/76: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1976/77: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1977/78: pontos 3-2-1 (vitória, empate, derrota)
- 1978/79: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1979/80: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1980/81: pontos 3-2-1 (vitória, empate, derrota)
- 1981/82: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1982/83: pontos 3-2-1 (vitória, empate, derrota)
- 1983/84: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1984/85: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1985/86: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 3-2-1 (vitória, empate, derrota)
- 1986/87: a RSSSF traz só a tabela final (lista de tabelas finais); pontos 4-2-1 (vitória, empate, derrota)
- 1987/88: pontos 4-2-1 (vitória, empate, derrota)
- 1988/89: pontos 4-2-1 (vitória, empate, derrota)
- 1989/90: pontos 4-2-1 (vitória, empate, derrota)
- 1990/91: pontos 4-2-1 (vitória, empate, derrota)
- 1991/92: pontos 4-2-1 (vitória, empate, derrota)
- 2025/26: a RSSSF só traz as tabelas: os jogos vêm do calendário do ogol

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Espérance de Tunis: 34
- Club Africain: 14
- Étoile du Sahel: 11
- Racing Club de Tunis: 8
- CS Sfaxien: 8
- Italia de Tunis: 4
- CA Bizertin: 4
- CS Hammam-Lif: 4
- Stade Tunisien: 4
- Stade Gaulois: 3
- US Tunisienne: 3
- Sfax Railways Sports: 3
- Sporting Club de Ferryville: 2
- Sporting Club de Tunis: 2
- Avant-Garde de Tunis: 1
- Savoia de La Goulette: 1
- CS Gabésien: 1
- JS Kairouan: 1
- Sem campeão: 1951/52

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1907 | Racing Club de Tunis | Stade Maritime de Bizerte |
| 1908/09 | Racing Club de Tunis | Sporting Club de Tunis |
| 1910/11 | Racing Club de Tunis | Stade Maritime de Bizerte |
| 1911/12 | Sporting Club de Ferryville | — |
| 1912/13 | Sporting Club de Ferryville | — |
| 1913/14 | Racing Club de Tunis | Stade Gaulois |
| 1919/20 | Racing Club de Tunis | — |
| 1920/21 | Racing Club de Tunis | — |
| 1921/22 | Racing Club de Tunis | — |
| 1922/23 | Stade Gaulois | — |
| 1923/24 | Stade Gaulois | — |
| 1924/25 | Racing Club de Tunis | — |
| 1925/26 | Sporting Club de Tunis | — |
| 1926/27 | Stade Gaulois | — |
| 1927/28 | Sporting Club de Tunis | — |
| 1928/29 | Avant-Garde de Tunis | — |
| 1929/30 | US Tunisienne | — |
| 1930/31 | US Tunisienne | — |
| 1931/32 | Italia de Tunis | Étoile du Sahel |
| 1932/33 | US Tunisienne | — |
| 1933/34 | Sfax Railways Sports | Italia de Tunis |
| 1934/35 | Italia de Tunis | — |
| 1935/36 | Italia de Tunis | — |
| 1936/37 | Italia de Tunis | — |
| 1937/38 | Savoia de La Goulette | — |
| 1938/39 | CS Gabésien | Espérance de Tunis |
| 1941/42 | Espérance de Tunis | — |
| 1944/45 | CA Bizertin | — |
| 1945/46 | CA Bizertin | — |
| 1946/47 | Club Africain | — |
| 1947/48 | Club Africain | — |
| 1948/49 | CA Bizertin | — |
| 1949/50 | Étoile du Sahel | Club Tunisien |
| 1950/51 | CS Hammam-Lif | — |
| 1951/52 | — | — |
| 1952/53 | Sfax Railways Sports | US Musulmane Olympique |
| 1953/54 | CS Hammam-Lif | — |
| 1954/55 | CS Hammam-Lif | — |
| 1955/56 | CS Hammam-Lif | Étoile du Sahel |
| 1956/57 | Stade Tunisien | Espérance de Tunis |
| 1957/58 | Étoile du Sahel | Espérance de Tunis |
| 1958/59 | Espérance de Tunis | Étoile du Sahel |
| 1959/60 | Espérance de Tunis | Stade Tunisien |
| 1960/61 | Stade Tunisien | Espérance de Tunis |
| 1961/62 | Stade Tunisien | Stade Soussien |
| 1962/63 | Étoile du Sahel | Stade Tunisien |
| 1963/64 | Club Africain | Espérance de Tunis |
| 1964/65 | Stade Tunisien | Club Africain |
| 1965/66 | Étoile du Sahel | CS Sfaxien |
| 1966/67 | Club Africain | Étoile du Sahel |
| 1967/68 | Sfax Railways Sports | Club Africain |
| 1968/69 | CS Sfaxien | Club Africain |
| 1969/70 | Espérance de Tunis | Club Africain |
| 1970/71 | CS Sfaxien | Club Africain |
| 1971/72 | Étoile du Sahel | Club Africain |
| 1972/73 | Club Africain | Étoile du Sahel |
| 1973/74 | Club Africain | Espérance de Tunis |
| 1974/75 | Espérance de Tunis | Club Africain |
| 1975/76 | Espérance de Tunis | Étoile du Sahel |
| 1976/77 | JS Kairouan | Club Africain |
| 1977/78 | CS Sfaxien | Club Africain |
| 1978/79 | Club Africain | Stade Tunisien |
| 1979/80 | Club Africain | Espérance de Tunis |
| 1980/81 | CS Sfaxien | Club Africain |
| 1981/82 | Espérance de Tunis | Club Africain |
| 1982/83 | CS Sfaxien | Club Africain |
| 1983/84 | CA Bizertin | Stade Tunisien |
| 1984/85 | Espérance de Tunis | Club Africain |
| 1985/86 | Étoile du Sahel | Espérance de Tunis |
| 1986/87 | Étoile du Sahel | Club Africain |
| 1987/88 | Espérance de Tunis | CO Transports |
| 1988/89 | Espérance de Tunis | Club Africain |
| 1989/90 | Club Africain | Espérance de Tunis |
| 1990/91 | Espérance de Tunis | Club Africain |
| 1991/92 | Club Africain | CA Bizertin |
| 1992/93 | Espérance de Tunis | JS Kairouan |
| 1993/94 | Espérance de Tunis | Étoile du Sahel |
| 1994/95 | CS Sfaxien | Espérance de Tunis |
| 1995/96 | Club Africain | Étoile du Sahel |
| 1996/97 | Étoile du Sahel | Espérance de Tunis |
| 1997/98 | Espérance de Tunis | Club Africain |
| 1998/99 | Espérance de Tunis | CA Bizertin |
| 1999/00 | Espérance de Tunis | Étoile du Sahel |
| 2000/01 | Espérance de Tunis | Étoile du Sahel |
| 2001/02 | Espérance de Tunis | Étoile du Sahel |
| 2002/03 | Espérance de Tunis | Étoile du Sahel |
| 2003/04 | Espérance de Tunis | Étoile du Sahel |
| 2004/05 | CS Sfaxien | Étoile du Sahel |
| 2005/06 | Espérance de Tunis | Étoile du Sahel |
| 2006/07 | Étoile du Sahel | Club Africain |
| 2007/08 | Club Africain | Étoile du Sahel |
| 2008/09 | Espérance de Tunis | Club Africain |
| 2009/10 | Espérance de Tunis | Club Africain |
| 2010/11 | Espérance de Tunis | Étoile du Sahel |
| 2011/12 | Espérance de Tunis | CA Bizertin |
| 2012/13 | CS Sfaxien | Espérance de Tunis |
| 2013/14 | Espérance de Tunis | CS Sfaxien |
| 2014/15 | Club Africain | Étoile du Sahel |
| 2015/16 | Étoile du Sahel | Espérance de Tunis |
| 2016/17 | Espérance de Tunis | Étoile du Sahel |
| 2017/18 | Espérance de Tunis | Club Africain |
| 2018/19 | Espérance de Tunis | Étoile du Sahel |
| 2019/20 | Espérance de Tunis | CS Sfaxien |
| 2020/21 | Espérance de Tunis | Étoile du Sahel |
| 2021/22 | Espérance de Tunis | US Monastir |
| 2022/23 | Étoile du Sahel | Espérance de Tunis |
| 2023/24 | Espérance de Tunis | US Monastir |
| 2024/25 | Espérance de Tunis | US Monastir |
| 2025/26 | Club Africain | Espérance de Tunis |

**Rebaixados marcados na classificação:** 138 em 68 edições (só onde a tabela publicada marca a queda); quem mais caiu: CO Transports (7), Stade Gabésien (6), Olympique du Kef (6), US Monastir (6), CS Hammam-Lif (6).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1949/50: US Tunisienne -1
- 1951/52: CS Hammam-Lif -1
- 1956/57: Sfax Railways Sports -2
- 1970/71: Étoile du Sahel -1
- 1984/85: JS Kairouan -2
- 1989/90: AS Kasserine -2
- 1998/99: Espérance de Tunis +2
- 1998/99: CA Bizertin +1
- 1998/99: CS Sfaxien +1
- 1998/99: Club Africain +2
- 1998/99: Olympique Béja +1
- 1998/99: CO Transports +2
- 1998/99: CS Hammam-Lif +2
- 1998/99: ES Béni Khalled +1
- 2006/07: Étoile du Sahel +1
- 2007/08: CS Sfaxien -2
- 2014/15: Étoile du Sahel -1
- 2015/16: Stade Tunisien -3
- 2017/18: CA Bizertin -6
- 2018/19: CA Bizertin -3
- 2018/19: Stade Gabésien -3
- 2019/20: Club Africain -6
- 2021/22: Espérance de Tunis +3
- 2021/22: US Monastir +2
- 2021/22: CS Sfaxien +2
- 2021/22: Club Africain +3
- 2021/22: Étoile du Sahel +1
- 2021/22: US Ben Guerdane +1
- 2021/22: Olympique Béja +1
- 2021/22: ES Métlaoui +1
- 2022/23: Étoile du Sahel +3
- 2022/23: Espérance de Tunis +4
- 2022/23: Club Africain +1
- 2022/23: US Monastir +4
- 2022/23: US Ben Guerdane +3
- 2022/23: CS Sfaxien +1
- 2022/23: Olympique Béja +2
- 2022/23: US Tataouine +2
- 2022/23: Stade Tunisien +4
- 2022/23: CA Bizertin +2
- 2022/23: AS Solimane +2
- 2022/23: ES Métlaoui +4
- 2023/24: Espérance de Tunis +3
- 2023/24: US Monastir +2
- 2023/24: CS Sfaxien +1
- 2023/24: Stade Tunisien +2
- 2023/24: Étoile du Sahel +3
- 2023/24: Club Africain +1
- 2023/24: Olympique Béja +3
- 2023/24: CA Bizertin +4
- 2023/24: EGS Gafsa +2
- 2023/24: US Tataouine +2
- 2023/24: ES Métlaoui +3
- 2023/24: US Ben Guerdane +4

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/tun-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **tun06 · 20:** «12  9  3 37-19 47» → «12 11  3 37-19 47»: Club Africain: 12+9+3 dá 24 jogos (são 26) e 47 pontos só fecham com 11 empates; a linha não era lida e a tabela se partia em duas

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 3)

- **2006/07 · tun07:186:** [oficial = (2, 0), nota = 2-0 dado ao CS Hammam-Lif: o US Monastir escalou jogador irregular] 2-0 dado ao CS Hammam-Lif (jogador irregular do US Monastir); em campo 0-0
- **2025/26 · ogol:11155620:** [oficial = (0, 2), nota = 2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin] 2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin (Wikipédia); em campo 0-1
- **2025/26 · ogol:12046043:** [oficial = (0, 2), nota = 2-0 dado ao Olympique Béja: o Stade Tunisien pôs 5 estrangeiros em campo ao mesmo tempo] 2-0 dado ao Olympique Béja porque o Stade Tunisien pôs 5 estrangeiros em campo ao mesmo tempo (Wikipédia); em campo 3-2

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 5)

- **1968/69:** Sfax Railways Sports None-None AS Marsa (, tun69: tabela de confrontos (célula "awd"; "NB: SRS-ASM was awarded a win to ASM")) nota da página: "NB: SRS-ASM was awarded a win to ASM"
- **1970/71:** US Monastir None-None Étoile du Sahel (, tun71: tabela de confrontos (célula "awd"; "NB: USMo-ESS was awarded a win to USMo")) nota da página: "NB: USMo-ESS was awarded a win to USMo"
- **1977/78:** CO Transports None-None SA Menzel Bourguiba (, tun78: tabela de confrontos (célula "awd"; "NB: COT-SAMB was awarded a win to COT")) nota da página: "NB: COT-SAMB was awarded a win to COT"
- **1980/81:** CS Sfaxien None-None US Monastir (, tun81: tabela de confrontos (célula "awd"; "NB: CSS-USMo was awarded a win to CSS")) nota da página: "NB: CSS-USMo was awarded a win to CSS"
- **2025/26:** US Monastirienne 0-2 CS Sfaxien (, ogol:12087988 (sem placar, "DA"); resultado dado: Wikipédia (en, 2025–26 Tunisian Ligue Professionnelle 1)) resultado dado fora de campo: 2-0 para o CS Sfaxien (tumulto da torcida do US Monastir)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 12)

- **1968/69:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1977/78:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1980/81:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1982/83:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1987/88:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1988/89:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1989/90:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1990/91:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1993/94:** a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a classificação é a tabela publicada
- **1994/95:** a tabela de confrontos da página não fecha com a tabela final em 13 dos 14 clubes (somada à parte, sem o leitor, dá os mesmos números): erro da própria página, sem terceira fonte; nenhum placar foi mudado e a classificação é a tabela publicada
- **2025/26:** três resultados dados fora de campo (2-0), pelas notas da tabela de confrontos da Wikipédia; com eles a tabela da RSSSF fecha
- **1909/10:** a Wikipédia lista um título do Racing Club de Tunis, que a RSSSF não traz (para ela, não houve campeonato): a temporada fica de fora

### Identidade dos clubes

Regras em `coleta/tun-1/clubes_tun.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes tunisianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1:
- nome pelo qual o clube é conhecido no Brasil ("Espérance de Tunis", "Club Africain", "Étoile du Sahel", "CS Sfaxien");
- nomes árabes com hífen; o Al-Ahly puro é o do Egito: o de Mateur é "Al-Ahly de Mateur";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Railway Sports (Sfax), campeão de 1933/34 e 1952/53, = Sfax Railways Sports (a RSSSF conta os títulos juntos);
  - US Tunisienne (campeã de 1929/30 a 1932/33) = Union Sportive Tunisienne (1949-1970);
  - Union Sportive Ferryville = USM Bourguiba (a lista de tabelas finais: "US Ferryville changed name for USM Bourguiba",
    1956); Olympique Tunis = US Musulmane Olympique ("changed name", 1957);
  - Patrie Football Club Bizertin = Patrie et Football Club Bizertin; Club Sportif Cheminots = CS Cheminots; Avenir
    Sportif de Gabès = AS Gabès; FC Jérissa = Football Club Djerissa; FC Bizerte (1907) = Stade maritime de Bizerte;
  - Stade Africain Menzel Bourguiba = SA Menzel Bourguiba (fica separado da USM Bourguiba).
- nomes curtos dos anos 1990 ("Sahel", "Stade", "Transports", "Esperance") resolvem pelo clube da 1ª divisão do ano.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a Copa da Tunísia e as outras copas, a 2ª divisão e os jogos de promoção.
- **Edições sem jogos** (56): 1911/12, 1912/13, 1919/20, 1920/21, 1921/22, 1922/23, 1923/24, 1924/25, 1925/26, 1926/27, 1927/28, 1928/29, 1929/30, 1930/31, 1932/33, 1934/35, 1935/36, 1936/37, 1937/38, 1941/42, 1944/45, 1945/46, 1946/47, 1947/48, 1948/49, 1950/51, 1951/52, 1953/54, 1954/55, 1955/56, 1956/57, 1957/58, 1958/59, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1964/65, 1965/66, 1966/67, 1967/68, 1969/70, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1978/79, 1979/80, 1981/82, 1983/84, 1984/85, 1985/86, 1986/87.
- **Décadas com menos da metade dos gols com autor:** 1900s, 1910s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1900s, 1910s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Era colonial (1907 a 1954/55): só 9 anos têm jogos na RSSSF, e só a final ou o mata-mata (1949/50: os resultados conhecidos); os outros, só o campeão. 1951/52 (abandonado) tem só a tabela do abandono. Fonte que resolveria: os jornais da época (La Dépêche tunisienne, Le Petit Matin) na Gallica (BnF).
- 1955/56 a 1995/96: só a tabela final (lista de tabelas finais da RSSSF), fora os anos da tabela de confrontos (1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e 1987/88 a 1995/96), que não têm data nem rodada. O ogol só tem jogos de 2005/06 em diante.
- Tabelas de confrontos que não fecham com a tabela final da página: um par de jogos em 1968/69, 1977/78, 1980/81, 1982/83, 1987/88 a 1990/91 e 1993/94; 1994/95 em 13 dos 14 clubes. Sem terceira fonte; nenhum placar mudado (jogo provável no relatório).
- Autores dos gols quase só em 2004/05 e 2010/11 (a RSSSF da Tunísia quase não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo (2005/06 em diante).
- Identidade a conferir: Railway Sports de Sfax (colonial) = Sfax Railways Sports; US Ferryville = USM Bourguiba; Olympique Tunis = US Musulmane Olympique; "ES" de 1949/50 lido como Espérance de Tunis.
- 1909/10: a Wikipédia dá um título ao Racing Club de Tunis; a RSSSF diz que não houve campeonato (ficou de fora).

## 10. Arquivos e comandos

Código em `coleta/tun-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão tunisiana no ogol para data/coleta/tun-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão tunisiana para data/coleta/tun-1/rsssf/: a lista de campeões (tunchamp.html), as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) a lista de campeões ("List of Tunisian football champions"), o artigo |
| `clubes_tun.py` | Identidade dos clubes tunisianos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão tunisiana (tun-1): o campeonato da Tunísia de 1907 a 2025/26. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão tunisiana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão tunisiana e grava o pacote em data/coleta/tun-1/pacote/ e o relatório em docs/coleta/tun-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/tun-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/tun-1/wikipedia/en_<temporada>.txt) e a |

- Fontes baixadas: `data/coleta/tun-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-tun-1/`.
- Pacote: `data/coleta/tun-1/pacote/`; relatório: `docs/coleta/tun-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/tun-1/baixar_ogol.py
python coleta/tun-1/baixar_rsssf.py
python coleta/tun-1/baixar_wikipedia.py
python coleta/tun-1/importar.py
python coleta/tun-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py tun-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

