# Campeonato Mexicano (`mex-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/mex-1/pacote/`, do código `coleta/mex-1/` e do relatório `docs/coleta/mex-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 158, de 1902/03 a 2026 Clausura; 2 sem jogos.
- **Jogos:** 26606 (26540 com placar); **gols:** 76536; **gols com autor:** 56671 (74%); **cartões:** 42633.
- **Clubes:** 92; **artilheiros:** 152 edições com artilheiro (185 linhas, com empates).
- **Classificação final:** 158 edições; **tabelas publicadas guardadas para conferência:** 3340 linhas.
- **No banco:** ainda não; **último commit do pacote:** cb0355f.
- **Observação da competição:** 1ª divisão mexicana de 1902/03 ao Clausura 2026, uma edição por título: era amadora (Primera Fuerza e Liga Mayor do Distrito Federal, 1902/03-1942/43; 1920/21 e 1921/22 com duas ligas), profissional (1943/44-1995/96, com os torneios curtos México 70, Prode 85 e México 86), Invierno e Verano (1996-2002) e Apertura e Clausura (2002 em diante). O Clausura 2020 (pandemia) e a temporada 1930/31 (cancelada) não têm campeão.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão mexicana (mex-1): uma por título, como na lista de campeões da RSSSF (mexchamp.html) e na da
Wikipédia em inglês ("List of Mexican football champions"). Escopo decidido pelo Guilherme em 23/11/2026:

- 1902/03 a 1942/43: era amadora (Primera Fuerza e Liga Mayor do Distrito Federal), uma edição por temporada. 1920/21 e
  1921/22 têm duas edições, uma por liga (Liga Mexicana, a oficial, e Liga Nacional, a do RC España). O Torneo del
  Centenario (1921, do governo) fica fora. 1930/31 foi cancelada no começo: entra sem campeão, com a tabela do
  cancelamento. 1911/12 e 1916/17 não têm página: só a tabela de mexhist.html.
- 1943/44 a 1995/96: profissional, uma edição por temporada (a liguilla e as finais, desde 1970/71, são fases). Os torneios
  curtos México 70, Prode 85 e México 86, que a federação conta como título, são edições próprias.
- 1996/97 a 2001/02: Invierno e Verano, uma edição cada ("1996 Invierno", "1997 Verano").
- 2002/03 em diante: Apertura e Clausura, uma edição cada ("2002 Apertura", "2003 Clausura"). O Clausura 2020 (pandemia)
  entra sem campeão. A última é o Clausura 2026 (o Apertura 2026 ainda está em disputa).
Ficam de fora a 2ª e a 3ª divisões, a Copa México, o Campeón de Campeones, a Interliga, os playoffs da Libertadores e as
copas das páginas da era amadora (Copa Tower, Copa Eliminatoria...).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_concacaf.texto); linha final None:
  até o primeiro título de outra competição (FIM_PADRAO). Página mexAAAA (1903-1919), mexAA (1920-2009: a do ano em que a
  temporada termina; mex6970 = 1969/70, mex70 = México 70, mex86 = Prode 85 e México 86), mex2-2010 e mexAAAA (2011 em diante:
  o Apertura do ano anterior e o Clausura do ano). Nas páginas com dois torneios, os trechos saem dos títulos ("Invierno 1996",
  "Clausura 2010").
- espn: datas dos jogos que vêm da ESPN (quando a página não tem a fase regular).
```

**Edições:** 158, uma por título, de 1902/03 ao Clausura 2026, como na lista de campeões da RSSSF (`mexchamp.html`) e na da Wikipédia em inglês (1943/44 em diante). Escopo decidido pelo Guilherme em 23/11/2026: a era amadora entra (Primera Fuerza e Liga Mayor do Distrito Federal, 1902/03-1942/43); em 1920/21 e 1921/22, uma edição por liga (Liga Mexicana, a oficial, e Liga Nacional, a do RC España), sem o Torneo del Centenario de 1921; México 70, Prode 85 e México 86 são edições próprias. De 1943/44 a 1995/96, uma edição por temporada (a liguilla e as finais são fases); Invierno e Verano (1996-2002) e Apertura e Clausura (2002 em diante), uma edição cada. A temporada 1930/31 (cancelada no começo e declarada deserta) e o Clausura 2020 (pandemia) entram sem campeão, com a tabela do momento.

**Fontes:** RSSSF (uma página por temporada em `data/coleta/mex-1/rsssf/`: base de jogos, com fases, rodadas, datas, estádios e autores dos gols; tabelas finais `mexhist.html`; lista de campeões `mexchamp.html`; artilheiros `mextops.html`); ESPN (liga `mex.1`, Apertura 2002 em diante: hora, estádio, público, gols com minuto e cartões; a fase regular do Apertura 2025 e do Clausura 2026); Wikipédia em inglês (lista de campeões: segunda fonte do campeão e do vice, 1943/44 em diante).

**Clubes:** nome pelo qual o clube é conhecido (Guadalajara, Cruz Azul, Pumas, Tigres, Tecos, Leones Negros). O mesmo clube com outro nome: Centro Unión (1918-1920) é o América; Atlético Español (1971-1982) é o Necaxa; Atlético Morelia é o Morelia; U.N.A.M. é o Pumas; U.A.N.L. é o Tigres; U.A.G. e Estudiantes Tecos são o Tecos; U. de G. é o Leones Negros; U.A.T. é o Correcaminos; Club México e México FC são o mesmo; o Pachuca AC da era amadora é o Pachuca (o clube conta a história desde 1892, com a refundação de 1960). Clubes diferentes com nome parecido ficam separados (lista no começo de `coleta/mex-1/clubes_mex.py`). Homônimos de clubes de outros países levam a cidade ou o país: América do México, Santos Laguna, Real Club España, Deportivo Español de México, Sporting de México, Nacional de Guadalajara, Laguna de Torreón.

**Regras:** o placar é o da RSSSF (ESPN onde a RSSSF não tem). Jogo decidido fora de campo leva o placar dado (`awd`), com o de campo na observação; "awarded to X" sem placar vira W.O. (vitória sem gols, como a tabela conta); resultado desconhecido ("unk") fica de fora. Pontos: 2 por vitória até 1994/95 e 3 a partir de 1995/96. Os grupos da fase regular (1970-2011) são só de classificação (todos jogam contra todos): os jogos não levam grupo; México 70, Prode 85 e México 86, em que só se jogava dentro do grupo, levam.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 116.
- **Edições com alguma tabela divergente** (33; motivo no relatório, na edição): 1904/05, 1905/06, 1913/14, 1918/19, 1925/26, 1927/28, 1933/34, 1936/37, 1940/41, 1945/46, 1955/56, 1956/57, 1960/61, 1965/66, 1969/70, 1973/74, 1975/76, 1978/79, 1986/87, 1988/89, 1989/90, 1990/91, 1992/93, 1993/94, 1995/96, 1996 Invierno, 2000 Verano, 2000 Invierno, 2001 Verano, 2002 Apertura, 2003 Apertura, 2004 Clausura, 2005 Clausura.
- **Edições sem tabela para conferir** (9): 1911/12, 1915/16, 1916/17, 1920/21 Liga Mexicana, 1920/21 Liga Nacional, 1921/22 Liga Mexicana, 1921/22 Liga Nacional, 1924/25, 1985 Prode 85.
- **Edições com menos jogos que o esperado:** 1904/05 (19 de 20), 1925/26 (47 de 46), 1927/28 (55 de 56), 1928/29 (37 de 36), 1929/30 (57 de 56), 1933/34 (32 de 33), 1995/96 (323 de 324).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 8 | 115 | 100% | 0% | 57% | 0% | 0% | 0% | 22% | 0.0 |
| 1910s | 10 | 190 | 100% | 0% | 83% | 0% | 0% | 0% | 44% | 0.0 |
| 1920s | 12 | 458 | 100% | 0% | 100% | 0% | 0% | 0% | 27% | 0.0 |
| 1930s | 10 | 342 | 100% | 0% | 100% | 0% | 0% | 0% | 28% | 0.0 |
| 1940s | 10 | 1470 | 100% | 0% | 100% | 0% | 0% | 0% | 44% | 0.0 |
| 1950s | 10 | 1545 | 100% | 0% | 100% | 0% | 0% | 0% | 73% | 0.0 |
| 1960s | 10 | 2179 | 100% | 0% | 100% | 0% | 0% | 0% | 67% | 0.0 |
| 1970s | 11 | 3893 | 100% | 0% | 100% | 0% | 0% | 0% | 69% | 0.0 |
| 1980s | 11 | 3908 | 100% | 0% | 100% | 0% | 0% | 0% | 68% | 0.0 |
| 1990s | 13 | 3454 | 100% | 0% | 100% | 0% | 0% | 0% | 70% | 0.0 |
| 2000s | 20 | 3561 | 100% | 79% | 100% | 79% | 36% | 5% | 94% | 4.5 |
| 2010s | 20 | 3358 | 100% | 99% | 100% | 95% | 89% | 40% | 100% | 5.0 |
| 2020s | 13 | 2133 | 100% | 100% | 84% | 97% | 97% | 76% | 99% | 4.7 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1902/03 a 1906/07: 5 clubes
- 1907/08: 4 clubes
- 1908/09: 3 clubes
- 1909/10 a 1910/11: 4 clubes
- 1911/12: 3 clubes
- 1912/13: 5 clubes
- 1913/14: 6 clubes
- 1914/15: 4 clubes
- 1915/16 a 1916/17: 6 clubes
- 1917/18: 7 clubes
- 1918/19 a 1919/20: 8 clubes
- 1920/21 Liga Mexicana a 1920/21 Liga Nacional: 5 clubes
- 1921/22 Liga Mexicana: 4 clubes
- 1921/22 Liga Nacional: 3 clubes
- 1922/23: 8 clubes
- 1923/24: 9 clubes
- 1924/25 a 1926/27: 7 clubes
- 1927/28: 8 clubes
- 1928/29: 9 clubes
- 1929/30 a 1931/32: 8 clubes
- 1932/33: 10 clubes
- 1933/34 a 1934/35: 6 clubes
- 1935/36 a 1936/37: 5 clubes
- 1937/38: 6 clubes
- 1938/39: 7 clubes
- 1939/40: 6 clubes
- 1940/41 a 1942/43: 8 clubes
- 1943/44: 10 clubes
- 1944/45: 13 clubes
- 1945/46: 16 clubes
- 1946/47 a 1948/49: 15 clubes
- 1949/50: 14 clubes
- 1950/51 a 1954/55: 12 clubes
- 1955/56: 14 clubes
- 1956/57: 13 clubes
- 1957/58 a 1962/63: 14 clubes
- 1963/64: 17 clubes
- 1964/65 a 1970 México 70: 16 clubes
- 1970/71 a 1973/74: 18 clubes
- 1974/75 a 1986 México 86: 20 clubes
- 1986/87: 21 clubes
- 1987/88 a 1993/94: 20 clubes
- 1994/95: 19 clubes
- 1995/96 a 2001 Verano: 18 clubes
- 2001 Invierno a 2002 Verano: 19 clubes
- 2002 Apertura a 2004 Clausura: 20 clubes
- 2004 Apertura a 2019 Clausura: 18 clubes
- 2019 Apertura: 19 clubes
- 2020 Clausura a 2026 Clausura: 18 clubes

**Pontos por vitória:**

- 1902/03 a 1994/95: 2
- 1995/96 a 2026 Clausura: 3

**Nome oficial:**

- 1902/03 a 1903/04: The Mexico Association Foot-ball League <ano>
- 1904/05 a 1911/12: The Mexico Amateur Association Football League <ano>
- 1912/13 a 1915/16: Asociación de Aficionados de México en la Liga de Football <ano>
- 1916/17 a 1920/21 Liga Mexicana: Liga Mexicana de Aficionados de Futbol Asociación <ano>
- 1920/21 Liga Nacional: Liga Nacional de Aficionados de Futbol Asociación <ano>
- 1921/22 Liga Mexicana: Liga Mexicana de Aficionados de Futbol Asociación <ano>
- 1921/22 Liga Nacional: Liga Nacional de Aficionados de Futbol Asociación <ano>
- 1922/23: Campeonato de Primera Fuerza de la Federación Mexicana de Football Association <ano>
- 1923/24 a 1926/27: Campeonato de Primera Fuerza de la Federación Central de Futbol <ano>
- 1927/28 a 1929/30: Campeonato de Primera Fuerza de la Federación Mexicana de Futbol <ano>
- 1930/31 a 1942/43: Campeonato Preferente de la Liga Mayor del Distrito Federal <ano>
- 1943/44 a 1948/49: Liga Mayor <ano>
- 1949/50 a 1969/70: Primera División de México <ano>
- 1970 México 70: Torneo México 70
- 1970/71 a 1984/85: Primera División de México <ano>
- 1985 Prode 85: Torneo Prode 85
- 1986 México 86: Torneo México 86
- 1986/87 a 1995/96: Primera División de México <ano>
- 1996 Invierno: Primera División de México Invierno <ano>
- 1997 Verano: Primera División de México Verano <ano>
- 1997 Invierno: Primera División de México Invierno <ano>
- 1998 Verano: Primera División de México Verano <ano>
- 1998 Invierno: Primera División de México Invierno <ano>
- 1999 Verano: Primera División de México Verano <ano>
- 1999 Invierno: Primera División de México Invierno <ano>
- 2000 Verano: Primera División de México Verano <ano>
- 2000 Invierno: Primera División de México Invierno <ano>
- 2001 Verano: Primera División de México Verano <ano>
- 2001 Invierno: Primera División de México Invierno <ano>
- 2002 Verano: Primera División de México Verano <ano>
- 2002 Apertura: Primera División de México Apertura <ano>
- 2003 Clausura: Primera División de México Clausura <ano>
- 2003 Apertura: Primera División de México Apertura <ano>
- 2004 Clausura: Primera División de México Clausura <ano>
- 2004 Apertura: Primera División de México Apertura <ano>
- 2005 Clausura: Primera División de México Clausura <ano>
- 2005 Apertura: Primera División de México Apertura <ano>
- 2006 Clausura: Primera División de México Clausura <ano>
- 2006 Apertura: Primera División de México Apertura <ano>
- 2007 Clausura: Primera División de México Clausura <ano>
- 2007 Apertura: Primera División de México Apertura <ano>
- 2008 Clausura: Primera División de México Clausura <ano>
- 2008 Apertura: Primera División de México Apertura <ano>
- 2009 Clausura: Primera División de México Clausura <ano>
- 2009 Apertura: Primera División de México Apertura <ano>
- 2010 Clausura: Torneo Bicentenario <ano>
- 2010 Apertura: Primera División de México Apertura <ano>
- 2011 Clausura: Primera División de México Clausura <ano>
- 2011 Apertura: Primera División de México Apertura <ano>
- 2012 Clausura: Primera División de México Clausura <ano>
- 2012 Apertura: Liga MX Apertura <ano>
- 2013 Clausura: Liga MX Clausura <ano>
- 2013 Apertura: Liga MX Apertura <ano>
- 2014 Clausura: Liga MX Clausura <ano>
- 2014 Apertura: Liga MX Apertura <ano>
- 2015 Clausura: Liga MX Clausura <ano>
- 2015 Apertura: Liga MX Apertura <ano>
- 2016 Clausura: Liga MX Clausura <ano>
- 2016 Apertura: Liga MX Apertura <ano>
- 2017 Clausura: Liga MX Clausura <ano>
- 2017 Apertura: Liga MX Apertura <ano>
- 2018 Clausura: Liga MX Clausura <ano>
- 2018 Apertura: Liga MX Apertura <ano>
- 2019 Clausura: Liga MX Clausura <ano>
- 2019 Apertura: Liga MX Apertura <ano>
- 2020 Clausura: Liga MX Clausura <ano>
- 2020 Apertura a 2021 Clausura: Torneo Guard1anes <ano>
- 2021 Apertura: Torneo Grita México A21
- 2022 Clausura: Torneo Grita México C22
- 2022 Apertura: Liga MX Apertura <ano>
- 2023 Clausura: Liga MX Clausura <ano>
- 2023 Apertura: Liga MX Apertura <ano>
- 2024 Clausura: Liga MX Clausura <ano>
- 2024 Apertura: Liga MX Apertura <ano>
- 2025 Clausura: Liga MX Clausura <ano>
- 2025 Apertura: Liga MX Apertura <ano>
- 2026 Clausura: Liga MX Clausura <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1902/03 a 1910/11: pontos corridos
- 1911/12: sem jogos (só a tabela final)
- 1912/13 a 1914/15: pontos corridos
- 1915/16: jogos incompletos; pontos corridos
- 1916/17: sem jogos (só a tabela final)
- 1917/18 a 1919/20: pontos corridos
- 1920/21 Liga Mexicana: jogos incompletos; pontos corridos + mata-mata
- 1920/21 Liga Nacional: jogos incompletos; pontos corridos
- 1921/22 Liga Mexicana: jogos incompletos; pontos corridos + mata-mata + desempate + mata-mata
- 1921/22 Liga Nacional: jogos incompletos; pontos corridos + desempate
- 1922/23: pontos corridos
- 1923/24: pontos corridos + desempate
- 1924/25: jogos incompletos; pontos corridos
- 1925/26: pontos corridos + desempate
- 1926/27 a 1930/31: pontos corridos
- 1931/32: pontos corridos + mata-mata
- 1932/33: pontos corridos
- 1933/34: pontos corridos + desempate
- 1934/35 a 1940/41: pontos corridos
- 1941/42: pontos corridos + desempate
- 1942/43: pontos corridos
- 1943/44: pontos corridos + desempate
- 1944/45 a 1946/47: pontos corridos
- 1947/48: pontos corridos + desempate
- 1948/49 a 1954/55: pontos corridos
- 1955/56: pontos corridos + desempate
- 1956/57 a 1962/63: pontos corridos
- 1963/64: pontos corridos + desempate
- 1964/65 a 1967/68: pontos corridos
- 1968/69 a 1969/70: pontos corridos + desempate
- 1970 México 70: 2 grupos
- 1970/71: pontos corridos + desempate + mata-mata
- 1971/72 a 1972/73: pontos corridos + mata-mata + desempate + mata-mata
- 1973/74: pontos corridos + mata-mata
- 1974/75: pontos corridos
- 1975/76: pontos corridos + mata-mata
- 1976/77: pontos corridos + 2 grupos + mata-mata
- 1977/78 a 1978/79: pontos corridos + mata-mata
- 1979/80: pontos corridos + 2 grupos + mata-mata
- 1980/81: pontos corridos + mata-mata
- 1981/82: pontos corridos + mata-mata + desempate
- 1982/83: pontos corridos + mata-mata + desempate + mata-mata
- 1983/84: pontos corridos + mata-mata
- 1984/85: pontos corridos + mata-mata + desempate
- 1985 Prode 85: 4 grupos + mata-mata
- 1986 México 86: 2 grupos + mata-mata
- 1986/87 a 1987/88: pontos corridos + mata-mata
- 1988/89: pontos corridos + 2 grupos + mata-mata
- 1989/90 a 2019 Apertura: pontos corridos + mata-mata
- 2020 Clausura: pontos corridos
- 2020 Apertura a 2026 Clausura: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1920/21 Liga Mexicana: Primeira fase (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1921/22 Liga Mexicana: Primeira fase (liga); Semifinal (mata_mata, jogo_unico); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1921/22 Liga Nacional: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1923/24: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1925/26: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1931/32: Primeira fase (liga); Liguilla (mata_mata, ida_volta)
- 1932/33: Primeira fase (liga); Playoff do rebaixamento (liga)
- 1933/34: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1941/42: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1943/44: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1947/48: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1955/56: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1963/64: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1968/69: Primeira fase (liga); Playoff do rebaixamento (liga); Desempate do título (mata_mata, jogo_unico)
- 1969/70: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 1970 México 70: Primeira fase (grupos, 2 grupos); Segunda fase (grupos, 2 grupos)
- 1970/71: Primeira fase (liga); Playoff do rebaixamento (liga); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1971/72: Primeira fase (liga); Playoff do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1972/73: Primeira fase (liga); Playoff do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1973/74: Primeira fase (liga); Playoff do rebaixamento (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1974/75: Primeira fase (liga); Grupo final (liga)
- 1975/76: Primeira fase (liga); Playoff do rebaixamento (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1976/77: Primeira fase (liga); Playoff do rebaixamento (liga); Liguilla (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1977/78: Primeira fase (liga); Playoff do rebaixamento (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1978/79: Primeira fase (liga); Liguilla (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1979/80: Primeira fase (liga); Playoff do rebaixamento (liga); Liguilla (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1980/81: Primeira fase (liga); Playoff do rebaixamento (liga); Grupos semifinais (liga); Final (mata_mata, ida_volta)
- 1981/82: Primeira fase (liga); Playoff do rebaixamento (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1982/83: Primeira fase (liga); Playoff do rebaixamento (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1983/84: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1984/85: Primeira fase (liga); Playoff do rebaixamento (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico)
- 1985 Prode 85: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1986 México 86: Primeira fase (grupos, 2 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1986/87: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1987/88: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1988/89: Primeira fase (liga); Grupos semifinais (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1989/90: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1990/91: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1991/92: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1992/93: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1993/94: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1994/95: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1995/96: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1996 Invierno: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1997 Verano: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1997 Invierno: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1998 Verano: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1998 Invierno: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1999 Verano: Primeira fase (liga); Liguilla (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1999 Invierno: Primeira fase (liga); Liguilla (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Verano: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000 Invierno: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Verano: Primeira fase (liga); Liguilla (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2001 Invierno: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Verano: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2002 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2003 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2006 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2007 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2008 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2012 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
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
- 2020 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2021 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2022 Apertura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Clausura: Primeira fase (liga); Repescagem (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2023 Apertura: Primeira fase (liga); Liguilla (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Clausura: Primeira fase (liga); Liguilla (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2024 Apertura: Primeira fase (liga); Liguilla (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Clausura: Primeira fase (liga); Liguilla (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2025 Apertura: Primeira fase (liga); Liguilla (mata_mata, jogo_unico); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2026 Clausura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- calculada: 79 edições
- RSSSF: 78 edições
- lista de campeões da Wikipédia em inglês: 1 edições

**Observações das edições:**

- 1911/12: sem jogos: a RSSSF não tem página desta temporada (só a tabela final de mexhist.html)
- 1915/16: jogos incompletos: a página da RSSSF traz 22 dos 30 jogos; a classificação é a tabela final publicada
- 1916/17: sem jogos: a RSSSF não tem página desta temporada (só a tabela final de mexhist.html)
- 1920/21 Liga Mexicana: liga oficial; o RC España jogou a Liga Nacional, paralela (alguns historiadores dão a temporada como anulada); jogos incompletos: a página da RSSSF traz só parte dos jogos ("known results"); a classificação é a tabela final publicada (mexhist.html)
- 1920/21 Liga Nacional: liga paralela, do RC España, que a lista de campeões da RSSSF conta como título (alguns historiadores dão a temporada como anulada); jogos incompletos: a página da RSSSF traz só parte dos jogos ("known results"); a classificação é a tabela final publicada (mexhist.html)
- 1921/22 Liga Mexicana: liga oficial; o RC España jogou a Liga Nacional, paralela (alguns historiadores dão a temporada como anulada); jogos incompletos: a página da RSSSF traz só parte dos jogos ("known results"); a classificação é a tabela final publicada (mexhist.html)
- 1921/22 Liga Nacional: liga paralela, do RC España, que a lista de campeões da RSSSF conta como título (alguns historiadores dão a temporada como anulada); jogos incompletos: a página da RSSSF traz só parte dos jogos ("known results"); a classificação é a tabela final publicada (mexhist.html); a Liga Nacional não terminou (a decisão foi um jogo extra)
- 1924/25: jogos incompletos: a página da RSSSF traz 37 dos 42 jogos; a classificação é a tabela final publicada
- 1930/31: temporada cancelada no começo e declarada deserta (o RC España saiu no caso Gaspar Rubio e a liga foi refeita como Liga Mayor do Distrito Federal); a classificação é a tabela do cancelamento
- 1970 México 70: torneio curto entre 1969/70 e 1970/71, jogado antes e depois da Copa do Mundo de 1970; a federação o conta como título
- 1985 Prode 85: torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como título desde outubro de 1986
- 1986 México 86: torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como título desde outubro de 1986
- 2020 Clausura: torneio cancelado na 10ª rodada pela pandemia de covid-19, sem campeão; a classificação é a tabela do cancelamento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- América do México: 20
- Real Club España: 14
- Guadalajara: 12
- Toluca: 12
- Pachuca: 10
- Cruz Azul: 10
- León: 8
- Tigres: 8
- Necaxa: 7
- Pumas: 7
- Reforma AC: 6
- Santos Laguna: 6
- Atlante: 5
- Monterrey: 5
- Asturias: 4
- Marte: 3
- Atlas: 3
- Veracruz: 2
- Zacatepec: 2
- Puebla: 2
- Orizaba AC: 1
- Mexico Cricket Club: 1
- British Club: 1
- Club México: 1
- Germania FV: 1
- Tampico: 1
- Oro: 1
- Tecos: 1
- Morelia: 1
- Tijuana: 1
- Sem campeão: 1930/31, 2020 Clausura

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1902/03 | Orizaba AC | Reforma AC |
| 1903/04 | Mexico Cricket Club | Reforma AC |
| 1904/05 | Pachuca | British Club |
| 1905/06 | Reforma AC | Mexico Country Club |
| 1906/07 | Reforma AC | British Club |
| 1907/08 | British Club | Mexico FC (1907) |
| 1908/09 | Reforma AC | Pachuca |
| 1909/10 | Reforma AC | Popo FC |
| 1910/11 | Reforma AC | Pachuca |
| 1911/12 | Reforma AC | Pachuca |
| 1912/13 | Club México | Pachuca |
| 1913/14 | Real Club España | Rovers FC |
| 1914/15 | Real Club España | Pachuca |
| 1915/16 | Real Club España | Pachuca |
| 1916/17 | Real Club España | Pachuca |
| 1917/18 | Pachuca | Deportivo Español de México |
| 1918/19 | Real Club España | América do México |
| 1919/20 | Pachuca | Germania FV |
| 1920/21 Liga Mexicana | Asturias | Deportivo Internacional |
| 1920/21 Liga Nacional | Real Club España | América do México |
| 1921/22 Liga Mexicana | Germania FV | Asturias |
| 1921/22 Liga Nacional | Real Club España | América do México |
| 1922/23 | Asturias | Germania FV |
| 1923/24 | Real Club España | América do México |
| 1924/25 | América do México | Necaxa |
| 1925/26 | América do México | Asturias |
| 1926/27 | América do México | Real Club España |
| 1927/28 | América do México | Asturias |
| 1928/29 | Marte | Real Club España |
| 1929/30 | Real Club España | América do México |
| 1930/31 | — | — |
| 1931/32 | Atlante | Necaxa |
| 1932/33 | Necaxa | Atlante |
| 1933/34 | Real Club España | Asturias |
| 1934/35 | Necaxa | América do México |
| 1935/36 | Real Club España | América do México |
| 1936/37 | Necaxa | Atlante |
| 1937/38 | Necaxa | Asturias |
| 1938/39 | Asturias | Euzkadi |
| 1939/40 | Real Club España | Necaxa |
| 1940/41 | Atlante | Selección Jalisco |
| 1941/42 | Real Club España | Atlante |
| 1942/43 | Marte | Atlante |
| 1943/44 | Asturias | Real Club España |
| 1944/45 | Real Club España | Puebla |
| 1945/46 | Veracruz | Atlante |
| 1946/47 | Atlante | León |
| 1947/48 | León | Oro |
| 1948/49 | León | Atlas |
| 1949/50 | Veracruz | Atlante |
| 1950/51 | Atlas | Atlante |
| 1951/52 | León | Guadalajara |
| 1952/53 | Tampico | Zacatepec |
| 1953/54 | Marte | Oro |
| 1954/55 | Zacatepec | Guadalajara |
| 1955/56 | León | Oro |
| 1956/57 | Guadalajara | Toluca |
| 1957/58 | Zacatepec | Toluca |
| 1958/59 | Guadalajara | León |
| 1959/60 | Guadalajara | América do México |
| 1960/61 | Guadalajara | Oro |
| 1961/62 | Guadalajara | América do México |
| 1962/63 | Oro | Guadalajara |
| 1963/64 | Guadalajara | América do México |
| 1964/65 | Guadalajara | Oro |
| 1965/66 | América do México | Atlas |
| 1966/67 | Toluca | América do México |
| 1967/68 | Toluca | Pumas |
| 1968/69 | Cruz Azul | Guadalajara |
| 1969/70 | Guadalajara | Cruz Azul |
| 1970 México 70 | Cruz Azul | Guadalajara |
| 1970/71 | América do México | Toluca |
| 1971/72 | Cruz Azul | América do México |
| 1972/73 | Cruz Azul | León |
| 1973/74 | Cruz Azul | Necaxa |
| 1974/75 | Toluca | León |
| 1975/76 | América do México | Leones Negros |
| 1976/77 | Pumas | Leones Negros |
| 1977/78 | Tigres | Pumas |
| 1978/79 | Cruz Azul | Pumas |
| 1979/80 | Cruz Azul | Tigres |
| 1980/81 | Pumas | Cruz Azul |
| 1981/82 | Tigres | Atlante |
| 1982/83 | Puebla | Guadalajara |
| 1983/84 | América do México | Guadalajara |
| 1984/85 | América do México | Pumas |
| 1985 Prode 85 | América do México | Tampico Madero |
| 1986 México 86 | Monterrey | Tampico Madero |
| 1986/87 | Guadalajara | Cruz Azul |
| 1987/88 | América do México | Pumas |
| 1988/89 | América do México | Cruz Azul |
| 1989/90 | Puebla | Leones Negros |
| 1990/91 | Pumas | América do México |
| 1991/92 | León | Puebla |
| 1992/93 | Atlante | Monterrey |
| 1993/94 | Tecos | Santos Laguna |
| 1994/95 | Necaxa | Cruz Azul |
| 1995/96 | Necaxa | Atlético Celaya |
| 1996 Invierno | Santos Laguna | Necaxa |
| 1997 Verano | Guadalajara | Toros Neza |
| 1997 Invierno | Cruz Azul | León |
| 1998 Verano | Toluca | Necaxa |
| 1998 Invierno | Necaxa | Guadalajara |
| 1999 Verano | Toluca | Atlas |
| 1999 Invierno | Pachuca | Cruz Azul |
| 2000 Verano | Toluca | Santos Laguna |
| 2000 Invierno | Morelia | Toluca |
| 2001 Verano | Santos Laguna | Pachuca |
| 2001 Invierno | Pachuca | Tigres |
| 2002 Verano | América do México | Necaxa |
| 2002 Apertura | Toluca | Morelia |
| 2003 Clausura | Monterrey | Morelia |
| 2003 Apertura | Pachuca | Tigres |
| 2004 Clausura | Pumas | Guadalajara |
| 2004 Apertura | Pumas | Monterrey |
| 2005 Clausura | América do México | Tecos |
| 2005 Apertura | Toluca | Monterrey |
| 2006 Clausura | Pachuca | San Luis FC |
| 2006 Apertura | Guadalajara | Toluca |
| 2007 Clausura | Pachuca | América do México |
| 2007 Apertura | Atlante | Pumas |
| 2008 Clausura | Santos Laguna | Cruz Azul |
| 2008 Apertura | Toluca | Cruz Azul |
| 2009 Clausura | Pumas | Pachuca |
| 2009 Apertura | Monterrey | Cruz Azul |
| 2010 Clausura | Toluca | Santos Laguna |
| 2010 Apertura | Monterrey | Santos Laguna |
| 2011 Clausura | Pumas | Morelia |
| 2011 Apertura | Tigres | Santos Laguna |
| 2012 Clausura | Santos Laguna | Monterrey |
| 2012 Apertura | Tijuana | Toluca |
| 2013 Clausura | América do México | Cruz Azul |
| 2013 Apertura | León | América do México |
| 2014 Clausura | León | Pachuca |
| 2014 Apertura | América do México | Tigres |
| 2015 Clausura | Santos Laguna | Querétaro |
| 2015 Apertura | Tigres | Pumas |
| 2016 Clausura | Pachuca | Monterrey |
| 2016 Apertura | Tigres | América do México |
| 2017 Clausura | Guadalajara | Tigres |
| 2017 Apertura | Tigres | Monterrey |
| 2018 Clausura | Santos Laguna | Toluca |
| 2018 Apertura | América do México | Cruz Azul |
| 2019 Clausura | Tigres | León |
| 2019 Apertura | Monterrey | América do México |
| 2020 Clausura | — | — |
| 2020 Apertura | León | Pumas |
| 2021 Clausura | Cruz Azul | Santos Laguna |
| 2021 Apertura | Atlas | León |
| 2022 Clausura | Atlas | Pachuca |
| 2022 Apertura | Pachuca | Toluca |
| 2023 Clausura | Tigres | Guadalajara |
| 2023 Apertura | América do México | Tigres |
| 2024 Clausura | América do México | Cruz Azul |
| 2024 Apertura | América do México | Monterrey |
| 2025 Clausura | Toluca | América do México |
| 2025 Apertura | Toluca | Tigres |
| 2026 Clausura | Cruz Azul | Pumas |

**Rebaixados marcados na classificação:** 13 em 12 edições (só onde a tabela publicada marca a queda); quem mais caiu: San Sebastián de León (1), Veracruz (1), La Piedad (1), Atlas (1), Cuautla (1).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1910/11: Reforma AC -5
- 1910/11: Pachuca -4
- 1910/11: British-Popo -5
- 1910/11: Club México -3
- 1912/13: Club México -10
- 1912/13: Pachuca -8
- 1912/13: Rovers FC -8
- 1912/13: Reforma AC -6
- 1912/13: Real Club España -3
- 1924/25: América do México -17
- 1924/25: Necaxa -14
- 1924/25: Real Club España -11
- 1924/25: Asturias -10
- 1924/25: Aurrerá -9
- 1924/25: Club México -9
- 1924/25: Germania FV -6
- 1926/27: Aurrerá +3
- 1937/38: Marte -3
- 1937/38: América do México +6
- 1937/38: Atlante +7
- 1945/46: ADO Orizaba -2
- 1961/62: Guadalajara -38
- 2018 Apertura: Veracruz -2
- 2019 Clausura: Veracruz -4
- 2020 Clausura: Pachuca -13
- 2020 Clausura: Querétaro -12
- 2020 Clausura: Atlético de San Luis -9
- 2020 Clausura: Toluca -8
- 2020 Clausura: Tijuana -3
- 2020 Clausura: Atlas -2
- 2020 Clausura: Monterrey +2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/mex-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 3)

- **mex77 · 109:** «2.3» → «2-3»: ponto no lugar do hífen no placar (U. de Curtidores 2-3 U. de G.); a tabela final fecha com 2-3
- **mex02 · 145:** «U.N.A.M:» → «U.N.A.M»: dois-pontos depois do nome do mandante (U.N.A.M. 5-0 Celaya)
- **mex81 · 1152:** «U.A.G   .» → «U.A.G.»: ponto solto depois do nome do mandante (U.A.G. 0-0 Cruz Azul, grupo semifinal)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 2)

- **2006 Apertura · mex07:336:** [descartado] Necaxa x Morelia suspenso aos 40' (1-1) e completado depois (os 50' restantes): fica só a linha da continuação, com o placar final
- **2017 Apertura · mex2018:289:** [descartado] Monterrey x Santos suspenso aos 12' (0-0, tempestade) e completado em 9/11 (os 79' restantes): fica só a linha da continuação, com o placar final (1-1)

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **1940/41 · mex41:283:** tabela de campo, de antes da decisão de 5/2/1941 que deu ao Selección Jalisco, ao Atlante e ao América os jogos contra o Asturias (jogador irregular); vale a tabela oficial logo abaixo

### Identidade dos clubes

Regras em `coleta/mex-1/clubes_mex.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes mexicanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Guadalajara", "Cruz Azul", "Pumas", "Tigres", "Tecos", "Leones Negros");
- o mesmo clube com outro nome: Centro Unión (1918-1920) é o América; Atlético Español (1971-1982) é o Necaxa vendido e
  renomeado, que voltou a se chamar Necaxa; Atlético Morelia e Monarcas são o Morelia; U.N.A.M. é o Pumas; U.A.N.L. e
  U. de N.L. são o Tigres; U.A.G., UAG, Estudiantes UAG e Estudiantes Tecos são o Tecos; U. de G. (Universidad de Guadalajara)
  é o Leones Negros; U.A.T. / U.A. Tamaulipas é o Correcaminos; T.M. Gallos Blancos (1994/95, o Tampico Madero jogando em
  Querétaro) é o Tampico Madero; Gallos Blancos (2002-2004) é o Querétaro; Oaxtepec/Ángeles (1984) é o Ángeles; Club México
  e México FC são o mesmo clube (a RSSSF usa os dois nomes); Pachuca AC (era amadora) é o Pachuca de hoje: o clube conta
  a própria história desde 1892 e celebra os 3 títulos amadores, com duas paradas (1922-1950 e 1952-1960) e a refundação
  de 1960 com o mesmo nome (pesquisa de 24/11/2026, aprovada pelo Guilherme; a RSSSF só diz que o clube se desfez em 1920);
- clubes diferentes, mesmo com nome parecido: Tigres da era amadora (Cidade do México, 1918-1922) e o Tigres da UANL;
  Mexico FC (1907/08) e Club México (desde 1910); Puebla AC (1904-1906) e Puebla (1944 em diante); Orizaba AC (1902-1904),
  ADO (Asociación Deportiva Orizabeña, 1943-1949) e Moctezuma de Orizaba; Laguna (Torreón, 1968-1977), Torreón (1969-1973) e
  Santos Laguna (1988 em diante); Tampico (até 1981) e Tampico Madero (1982 em diante); Celaya (1958-1961) e Atlético Celaya
  (1995-2002); San Luis (1971-1976) e San Luis FC (2002-2013), e o Atlético de San Luis (2019 em diante); Deportivo Neza
  (1978-1988) e Toros Neza (1993-2002); Cobras (Ciudad Juárez, 1986-1991), Indios (2008-2010) e FC Juárez (2019 em diante);
  Morelia e Mazatlán (2020, a vaga do Morelia levada a Mazatlán: clube novo);
- homônimo de clube do banco ou de outro pacote leva a cidade ou o país: América do México, Santos Laguna, Real Club España,
  Deportivo Español de México, Sporting de México, Nacional de Guadalajara, Laguna de Torreón (conferido com o banco e os
  outros pacotes em 23/11/2026).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a 2ª e a 3ª divisões, a Copa México e a Copa MX, o Campeón de Campeones, a Interliga, a Liguilla Pre-Libertadores, os playoffs de vaga na Libertadores, o Torneo Presidente López Mateos (1963), a Copa Federación (1983), os jogos de promoção e as copas e amistosos das páginas da era amadora (Copa Tower, Copa Eliminatoria, jogo anual Inglaterra x Escócia).
- **Edições sem jogos (2):** 1911/12 e 1916/17: a RSSSF não tem página dessas temporadas; entram com a tabela final de `mexhist.html`.
- **Edições com jogos incompletos (6):** 1915/16 e 1924/25 (a página traz só parte dos jogos), 1920/21 e 1921/22 ("known results"; a Liga Nacional de 1921/22 não terminou). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.
- **Edições sem jogos** (2): 1911/12, 1916/17.
- **Décadas com menos da metade dos gols com autor:** 1900s, 1910s, 1920s, 1930s, 1940s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1900s, 1910s, 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Decidido em 24/11 (pesquisa aprovada pelo Guilherme): o Pachuca AC da era amadora (1902-1922) é o Pachuca de hoje, como o clube conta a própria história; a RSSSF diz que o Pachuca AC se dissolveu em 1920. Se forem clubes diferentes, separar em clubes_mex.py (regra 'pachuca').
- Decidido em 24/11 (pesquisa aprovada pelo Guilherme): Atlético Español (1971-1982) = Necaxa (o clube vendido e renomeado, que voltou a se chamar Necaxa); a temporada 1930/31, cancelada, entra sem campeão, com a tabela do cancelamento.
- Edições sem jogos: 1911/12 e 1916/17 (a RSSSF não tem página; só a tabela final de mexhist.html). Jogos incompletos: 1915/16, 1924/25, 1920/21 e 1921/22 (as duas ligas). Fonte que resolveria: jornais da época (Hemeroteca Nacional Digital da UNAM, a fonte dos autores das páginas da RSSSF).
- 1995/96: falta o Guadalajara x Pumas do 1º turno (não está na página); pela tabela, o Guadalajara venceu por 3-0.
- Estádio só de 2002 em diante (ESPN) e nos jogos com "at X": as linhas de estádio das páginas da RSSSF ("Estadio Jalisco, Guadalajara", acima do jogo) ainda não são lidas.
- Divergências de um gol ou de um resultado entre a página e a tabela dela em cerca de 30 edições: ficam como erro da página (o relatório diz qual clube e qual tabela).

## 10. Arquivos e comandos

Código em `coleta/mex-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga mex.1) de 2002 a 2026 para data/coleta/mex-1/espn/mex1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão mexicana para data/coleta/mex-1/rsssf/: a lista de campeões (mexchamp.html), as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês a lista de campeões mexicanos ("List of Mexican football champions", era amadora e |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês ("List of Mexican football champions", seção "Liga MX champions", 1943/44 em |
| `clubes_mex.py` | Identidade dos clubes mexicanos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão mexicana (mex-1): uma por título, como na lista de campeões da RSSSF (mexchamp.html) e na da |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão mexicana, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão mexicana e grava o pacote em data/coleta/mex-1/pacote/ e o relatório em docs/coleta/mex-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/mex-1/rsssf/) com o leitor comum (rsssf_concacaf); os jogos |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/mex-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`.
- Pacote: `data/coleta/mex-1/pacote/`; relatório: `docs/coleta/mex-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/mex-1/baixar_espn.py
python coleta/mex-1/baixar_rsssf.py
python coleta/mex-1/baixar_wikipedia.py
python coleta/mex-1/importar.py
python coleta/mex-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py mex-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

