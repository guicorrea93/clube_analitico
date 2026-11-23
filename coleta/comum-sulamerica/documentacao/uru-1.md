# Campeonato Uruguaio (`uru-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/uru-1/pacote/`, do código `coleta/uru-1/` e do relatório `docs/coleta/uru-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 126, de 1900 a 2025; 45 sem jogos.
- **Jogos:** 12456 (12359 com placar); **gols:** 35118; **gols com autor:** 14335 (41%); **cartões:** 9481.
- **Clubes:** 84; **artilheiros:** 122 edições com artilheiro (138 linhas, com empates).
- **Classificação final:** 126 edições; **tabelas publicadas guardadas para conferência:** 2761 linhas.
- **No banco:** sim; **último commit do pacote:** 415911b.
- **Observação da competição:** 1ª divisão uruguaia de 1900 a 2025: uma edição por título (AUF e FUF em 1923 e 1924; Torneo del Consejo Provisorio em 1926; temporadas no calendário europeu de 2005/06 a 2015/16). Apertura, Intermedio e Clausura são fases da edição. Jogos de 1900, 1901, 1905, 1908, 1916, 1932-1974 e 1994 em diante; nos outros anos, só a tabela final e o campeão (nenhuma fonte pública tem os jogos).

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão uruguaia (uru-1): uma por torneio que deu título de campeão uruguaio.

Lista de títulos: RSSSF (uruchamp.html), conferida com a Wikipédia. Os cismas de 1923 e 1924 dão duas edições cada
(AUF e FUF, a liga dissidente), como a RSSSF conta ("consideramos os dois campeonatos de igual valor"); 1926 é o Torneo del
Consejo Provisorio, que reuniu as duas ligas. Sem edição: 1904 e 1930 (não houve campeonato) e 1925 (AUF e FUF não
terminaram). 1948 entra sem campeão (abandonado na greve dos jogadores, com a tabela do abandono).

De 1932 a 2025 há um campeão por ano (ou temporada, de 2005/06 a 2015/16, no calendário europeu): Apertura, Intermedio e
Clausura não dão título de campeão uruguaio e entram como fases da edição, com os desempates e finais de cada um, a tabela
anual e as finais do campeonato. Ficam de fora as liguillas pré-Libertadores, o Torneo Integración (1994), o Torneo Nacional
(1996), a Copa Artigas, o Torneo Permanencia (2001-2002), o Reclasificatorio (2004) e os jogos de promoção contra clubes da
2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_sul.texto); linha final
  None: até o primeiro título de outra competição (FIM_PADRAO). 1932-1959, 1965 e 1994 em diante (a página de 1969
  traz só 18 das 20 rodadas e nenhum jogo da fase de campeonato: 1969 vem da Wikipédia).
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1900, 1901, 1905, 1908, 1916, 1960-1964 e
  1966-1974.
- sem nenhuma das duas (1902-1931 fora esses anos, 1975-1993): edição sem jogos, só com a tabela final da RSSSF
  (uruhist.html) e o campeão. Os jogos desses anos não estão em nenhuma fonte pública que achamos (relatório).
```

**Edições:** 126, uma por título de campeão uruguaio da 1ª divisão, de 1900 a 2025, como na lista de campeões da RSSSF (`uruchamp.html`). Os cismas de 1923 e 1924 dão duas edições cada ("1923 AUF" e "1923 FUF"), como a RSSSF conta; 1926 é o Torneo del Consejo Provisorio. Sem edição: 1904 e 1930 (não houve campeonato) e 1925 (AUF e FUF não terminaram). 1948 entra sem campeão (abandonado na greve dos jogadores). De 2005/06 a 2015/16 as temporadas seguem o calendário europeu; "2005" é o Torneo Uruguay Especial e "2016" a Transición. Apertura, Intermedio e Clausura não davam título de campeão uruguaio: são fases da edição, com as finais de cada um, a tabela anual e as finais do campeonato.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/uru-1/rsssf/`: base de jogos de 1932-1959, 1965 e 1994 em diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas finais `uruhist.html`, de 1900 a 2000, são a conferência); Wikipédia em espanhol (páginas "Campeonato Uruguayo de Primera División <ano>": jogos de 1900, 1901, 1905, 1908, 1916, 1960-1964 e 1966-1974, por rodada, sem autores; em 1969 no lugar da RSSSF, que tem só 18 das 20 rodadas); ogol (calendários de 2005/06 em diante: rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `uru.1`, 2005 em diante: hora, estádio e público; gols com minuto e cartões de 2005 a 2013); Wikipédia em inglês (lista de campeões da AUF, segunda fonte do campeão; não traz a FUF nem 1926).

**Clubes:** C.U.R.C.C. (1900-1913) entra como Peñarol, como a RSSSF e a Wikipédia contam (a seção de futebol do C.U.R.C.C. virou o Peñarol; o Nacional contesta). Defensor e Defensor Sporting são um clube só; Miramar, Misiones e Miramar Misiones (fusão de 1980) ficam separados; o River Plate amador (River Plate FC, até 1929) não é o atual (River Plate de Montevideo, de 1932). Homônimos de clubes do banco levam a cidade (Liverpool de Montevideo, Racing de Montevideo, River Plate de Montevideo...).

**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela); o ogol só completa rodada e data e entra como conferência. Jogo decidido no tribunal leva o placar dado (`awd`) ou, quando o tribunal só deu a vitória ("awarded win to X; goal records unchanged"), fica sem placar como `awd`, com o placar de campo na observação (a tabela conta a vitória com os gols de campo). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 59.
- **Edições com alguma tabela divergente** (22; motivo no relatório, na edição): 1900, 1901, 1905, 1908, 1916, 1932, 1933, 1934, 1951, 1960, 1961, 1962, 1965, 1967, 1994, 1995, 1996, 1997, 1998, 2000, 2002, 2004.
- **Edições sem tabela para conferir** (45): 1902, 1903, 1906, 1907, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923 AUF, 1923 FUF, 1924 AUF, 1924 FUF, 1926, 1927, 1928, 1929, 1931, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993.
- **Edições com menos jogos que o esperado:** 2000 (293 de 292), 2004 (252 de 251), 2007/08 (244 de 243), 2011/12 (243 de 242), 2020 (302 de 301), 2022 (300 de 299), 2023 (301 de 300).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 9 | 141 | 99% | 0% | 63% | 97% | 0% | 0% | 0% | 0.0 |
| 1910s | 10 | 72 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 11 | 0 | — | — | — | — | — | — | — | — |
| 1930s | 9 | 900 | 1% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 10 | 905 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 905 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 938 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 693 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 937 | 54% | 0% | 100% | 0% | 0% | 0% | 13% | 0.0 |
| 2000s | 11 | 2756 | 100% | 45% | 100% | 45% | 45% | 0% | 79% | 1.6 |
| 2010s | 10 | 2468 | 100% | 98% | 100% | 98% | 96% | 0% | 80% | 2.0 |
| 2020s | 6 | 1741 | 100% | 99% | 100% | 96% | 95% | 0% | 59% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1900: 4 clubes
- 1901: 5 clubes
- 1902: 6 clubes
- 1903: 7 clubes
- 1905: 5 clubes
- 1906 a 1907: 6 clubes
- 1908: 10 clubes
- 1909: 11 clubes
- 1910: 9 clubes
- 1911 a 1914: 8 clubes
- 1915: 10 clubes
- 1916: 9 clubes
- 1917 a 1919: 10 clubes
- 1920 a 1923 AUF: 12 clubes
- 1923 FUF: 32 clubes
- 1924 AUF: 12 clubes
- 1924 FUF: 17 clubes
- 1926: 10 clubes
- 1927: 20 clubes
- 1928: 16 clubes
- 1929: 14 clubes
- 1931: 12 clubes
- 1932 a 1937: 10 clubes
- 1938 a 1941: 11 clubes
- 1942 a 1968: 10 clubes
- 1969 a 1970: 11 clubes
- 1971 a 1978: 12 clubes
- 1979: 13 clubes
- 1980: 14 clubes
- 1981: 15 clubes
- 1982: 14 clubes
- 1983 a 1989: 13 clubes
- 1990 a 1991: 14 clubes
- 1992 a 1995: 13 clubes
- 1996: 12 clubes
- 1997: 13 clubes
- 1998: 12 clubes
- 1999: 15 clubes
- 2000 a 2005: 18 clubes
- 2005/06: 20 clubes
- 2006/07 a 2025: 16 clubes

**Pontos por vitória:**

- 1900 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1900 a 1907: Uruguay Association Foot-ball League – Campeonato <ano>
- 1908 a 1914: Liga Uruguaya de Football – Campeonato <ano>
- 1915 a 1923 AUF: Asociación Uruguaya de Football – Campeonato <ano>
- 1923 FUF: Federación Uruguaya de Football – Campeonato <ano>
- 1924 AUF: Asociación Uruguaya de Football – Campeonato <ano>
- 1924 FUF: Federación Uruguaya de Football – Campeonato <ano>
- 1926: Torneo del Consejo Provisorio <ano>
- 1927 a 1931: Asociación Uruguaya de Football – Campeonato <ano>
- 1932 a 2004: Campeonato Uruguayo de Primera División <ano>
- 2005: Campeonato Uruguayo de Primera División <ano> – Torneo Uruguay Especial
- 2005/06 a 2015/16: Campeonato Uruguayo de Primera División <ano>
- 2016: Campeonato Uruguayo de Primera División <ano> – Torneo de Transición
- 2017 a 2025: Campeonato Uruguayo de Primera División <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1900 a 1901: pontos corridos
- 1902 a 1903: sem jogos (só a tabela final)
- 1905: pontos corridos
- 1906 a 1907: sem jogos (só a tabela final)
- 1908: pontos corridos
- 1909 a 1915: sem jogos (só a tabela final)
- 1916: pontos corridos
- 1917 a 1931: sem jogos (só a tabela final)
- 1932: pontos corridos
- 1933: pontos corridos + desempate
- 1934 a 1936: pontos corridos
- 1937: pontos corridos + desempate
- 1938: pontos corridos
- 1939: pontos corridos + desempate
- 1940 a 1943: pontos corridos
- 1944: pontos corridos + desempate
- 1945 a 1946: pontos corridos
- 1947: pontos corridos + desempate
- 1948 a 1949: pontos corridos
- 1950: pontos corridos + desempate
- 1951: pontos corridos
- 1952: pontos corridos + desempate
- 1953 a 1958: pontos corridos
- 1959 a 1961: pontos corridos + desempate
- 1962 a 1974: pontos corridos
- 1975 a 1993: sem jogos (só a tabela final)
- 1994: pontos corridos + mata-mata
- 1995: pontos corridos + mata-mata + pontos corridos + mata-mata + desempate
- 1996: pontos corridos + mata-mata
- 1997: pontos corridos + desempate + mata-mata
- 1998: pontos corridos
- 1999: pontos corridos + desempate
- 2000 a 2001: pontos corridos + mata-mata
- 2002: pontos corridos + desempate
- 2003 a 2004: pontos corridos + mata-mata
- 2005: pontos corridos + desempate
- 2005/06: pontos corridos + mata-mata
- 2006/07: pontos corridos + mata-mata + desempate
- 2007/08: pontos corridos + mata-mata
- 2008/09: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2009/10 a 2015/16: pontos corridos + mata-mata
- 2016: pontos corridos
- 2017: pontos corridos + 2 grupos + mata-mata + pontos corridos + desempate + mata-mata
- 2018: pontos corridos + 2 grupos + mata-mata + pontos corridos + mata-mata
- 2019: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2020: pontos corridos + mata-mata + pontos corridos + mata-mata + pontos corridos + mata-mata
- 2021: pontos corridos + mata-mata
- 2022 a 2023: pontos corridos + mata-mata + pontos corridos + mata-mata
- 2024: pontos corridos + mata-mata + pontos corridos
- 2025: pontos corridos + mata-mata + pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1933: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1937: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1939: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1944: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 1947: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 1950: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1952: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1959: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1960: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1961: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1969: Primeira fase (liga); Fase final (liga)
- 1970: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1971: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1994: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 1995: Apertura (liga); Final do Apertura (mata_mata, jogo_unico); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do título (mata_mata, ida_volta)
- 1996: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 1997: Apertura (liga); Clausura (liga); Desempate do rebaixamento (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1998: Apertura (liga); Clausura (liga)
- 1999: Apertura (liga); Clausura (liga); Desempate do título (mata_mata, ida_volta)
- 2000: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2001: Primeira fase (liga); Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2002: Primeira fase (liga); Apertura (liga); Clausura (liga); Desempate do título (mata_mata, ida_volta)
- 2003: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2004: Clasificatorio (liga); Repechaje (liga); Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2005: Primeira fase (liga); Desempate do título (mata_mata, ida_volta)
- 2005/06: Apertura (liga); Clausura (liga); Semifinal (mata_mata, ida_volta)
- 2006/07: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Desempate do rebaixamento (mata_mata, ida_volta)
- 2007/08: Apertura (liga); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta)
- 2008/09: Apertura (liga); Final do Apertura (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2009/10: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2010/11: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2011/12: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2012/13: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2013/14: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2014/15: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2015/16: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2017: Apertura (liga); Intermedio (grupos, 2 grupos); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Desempate do rebaixamento (mata_mata, ida_volta); Desempate da tabela anual (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico)
- 2018: Apertura (liga); Intermedio (grupos, 2 grupos); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2019: Apertura (liga); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Final do Clausura (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico)
- 2020: Apertura (liga); Final do Apertura (mata_mata, jogo_unico); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2021: Apertura (liga); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2022: Apertura (liga); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, jogo_unico)
- 2023: Apertura (liga); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2024: Apertura (liga); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga)
- 2025: Apertura (liga); Intermedio (liga); Final do Intermedio (mata_mata, jogo_unico); Clausura (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 110 edições
- calculada: 16 edições

**Observações das edições:**

- 1923 FUF: cisma do futebol uruguaio (1922-1925): a FUF foi fundada por Peñarol e Central depois de expulsos da AUF; as duas ligas tiveram campeonato; título não reconhecido pela AUF: edição sem campeão (D-09)
- 1924 FUF: cisma do futebol uruguaio (1922-1925): a FUF foi fundada por Peñarol e Central depois de expulsos da AUF; as duas ligas tiveram campeonato; título não reconhecido pela AUF: edição sem campeão (D-09)
- 1926: torneio de unificação depois da dissolução da FUF, com clubes das duas ligas (RSSSF); título não reconhecido pela AUF: edição sem campeão (D-09)
- 1947: sem vice: o triangular pelo 2º lugar não terminou (D-22 c)
- 1948: campeonato abandonado na 10ª rodada pela greve dos jogadores; sem campeão (RSSSF)
- 2005: torneio de transição para o calendário europeu; o Defensor não jogou a final e o título ficou com o Nacional
- 2016: torneio de transição de volta ao calendário anual (turno único)
- 2020: temporada esticada até abril de 2021 pela pandemia (a RSSSF chama de 2020/21)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Peñarol: 52
- Nacional: 50
- River Plate FC: 4
- Defensor Sporting: 4
- Danubio: 4
- Montevideo Wanderers: 3
- Rampla Juniors: 1
- Central Español: 1
- Progreso: 1
- Bella Vista: 1
- Liverpool de Montevideo: 1
- Sem campeão: 1923 FUF, 1924 FUF, 1926, 1948

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1900 | Peñarol | Albion de Montevideo |
| 1901 | Peñarol | Nacional |
| 1902 | Nacional | Peñarol |
| 1903 | Nacional | Peñarol |
| 1905 | Peñarol | Nacional |
| 1906 | Montevideo Wanderers | Peñarol |
| 1907 | Peñarol | Montevideo Wanderers |
| 1908 | River Plate FC | Montevideo Wanderers |
| 1909 | Montevideo Wanderers | Peñarol |
| 1910 | River Plate FC | Peñarol |
| 1911 | Peñarol | Montevideo Wanderers |
| 1912 | Nacional | Peñarol |
| 1913 | River Plate FC | Nacional |
| 1914 | River Plate FC | Peñarol |
| 1915 | Nacional | Peñarol |
| 1916 | Nacional | Peñarol |
| 1917 | Nacional | Peñarol |
| 1918 | Peñarol | Nacional |
| 1919 | Nacional | Universal de Montevideo |
| 1920 | Nacional | Peñarol |
| 1921 | Peñarol | Nacional |
| 1922 | Nacional | Montevideo Wanderers |
| 1923 AUF | Nacional | Rampla Juniors |
| 1923 FUF | — | — |
| 1924 AUF | Nacional | Bella Vista |
| 1924 FUF | — | — |
| 1926 | — | — |
| 1927 | Rampla Juniors | Peñarol |
| 1928 | Peñarol | Rampla Juniors |
| 1929 | Peñarol | Nacional |
| 1931 | Montevideo Wanderers | Nacional |
| 1932 | Peñarol | Rampla Juniors |
| 1933 | Nacional | Peñarol |
| 1934 | Nacional | Peñarol |
| 1935 | Peñarol | Nacional |
| 1936 | Peñarol | Nacional |
| 1937 | Peñarol | Nacional |
| 1938 | Peñarol | Nacional |
| 1939 | Nacional | Peñarol |
| 1940 | Nacional | Rampla Juniors |
| 1941 | Nacional | Peñarol |
| 1942 | Nacional | Peñarol |
| 1943 | Nacional | Peñarol |
| 1944 | Peñarol | Nacional |
| 1945 | Peñarol | Nacional |
| 1946 | Nacional | Peñarol |
| 1947 | Nacional | — |
| 1948 | — | — |
| 1949 | Peñarol | Nacional |
| 1950 | Nacional | Peñarol |
| 1951 | Peñarol | Nacional |
| 1952 | Nacional | Peñarol |
| 1953 | Peñarol | Nacional |
| 1954 | Peñarol | Nacional |
| 1955 | Nacional | Peñarol |
| 1956 | Nacional | Peñarol |
| 1957 | Nacional | Peñarol |
| 1958 | Peñarol | Nacional |
| 1959 | Peñarol | Nacional |
| 1960 | Peñarol | Cerro |
| 1961 | Peñarol | Nacional |
| 1962 | Peñarol | Nacional |
| 1963 | Nacional | Peñarol |
| 1964 | Peñarol | Rampla Juniors |
| 1965 | Peñarol | Nacional |
| 1966 | Nacional | Peñarol |
| 1967 | Peñarol | Nacional |
| 1968 | Peñarol | Nacional |
| 1969 | Nacional | Peñarol |
| 1970 | Nacional | Peñarol |
| 1971 | Nacional | Peñarol |
| 1972 | Nacional | Peñarol |
| 1973 | Peñarol | Nacional |
| 1974 | Peñarol | Nacional |
| 1975 | Peñarol | Nacional |
| 1976 | Defensor Sporting | Peñarol |
| 1977 | Nacional | Peñarol |
| 1978 | Peñarol | Nacional |
| 1979 | Peñarol | Nacional |
| 1980 | Nacional | Montevideo Wanderers |
| 1981 | Peñarol | Nacional |
| 1982 | Peñarol | Nacional |
| 1983 | Nacional | Danubio |
| 1984 | Central Español | Peñarol |
| 1985 | Peñarol | Montevideo Wanderers |
| 1986 | Peñarol | Nacional |
| 1987 | Defensor Sporting | Nacional |
| 1988 | Danubio | Peñarol |
| 1989 | Progreso | Nacional |
| 1990 | Bella Vista | Nacional |
| 1991 | Defensor Sporting | Nacional |
| 1992 | Nacional | River Plate de Montevideo |
| 1993 | Peñarol | Defensor Sporting |
| 1994 | Peñarol | Defensor Sporting |
| 1995 | Peñarol | Nacional |
| 1996 | Peñarol | Nacional |
| 1997 | Peñarol | Defensor Sporting |
| 1998 | Nacional | Peñarol |
| 1999 | Peñarol | Nacional |
| 2000 | Nacional | Peñarol |
| 2001 | Nacional | Danubio |
| 2002 | Nacional | Danubio |
| 2003 | Peñarol | Nacional |
| 2004 | Danubio | Nacional |
| 2005 | Nacional | Defensor Sporting |
| 2005/06 | Nacional | Rocha FC |
| 2006/07 | Danubio | Peñarol |
| 2007/08 | Defensor Sporting | Peñarol |
| 2008/09 | Nacional | Defensor Sporting |
| 2009/10 | Peñarol | Nacional |
| 2010/11 | Nacional | Defensor Sporting |
| 2011/12 | Nacional | Peñarol |
| 2012/13 | Peñarol | Defensor Sporting |
| 2013/14 | Danubio | Montevideo Wanderers |
| 2014/15 | Nacional | Peñarol |
| 2015/16 | Peñarol | Nacional |
| 2016 | Nacional | Montevideo Wanderers |
| 2017 | Peñarol | Defensor Sporting |
| 2018 | Peñarol | Nacional |
| 2019 | Nacional | Peñarol |
| 2020 | Nacional | Rentistas |
| 2021 | Peñarol | Nacional |
| 2022 | Nacional | Liverpool de Montevideo |
| 2023 | Liverpool de Montevideo | Peñarol |
| 2024 | Peñarol | Nacional |
| 2025 | Nacional | Peñarol |

**Rebaixados marcados na classificação:** 36 em 23 edições (só onde a tabela publicada marca a queda); quem mais caiu: Bella Vista (5), Progreso (4), River Plate de Montevideo (3), Racing de Montevideo (3), Sud América (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1917: Montevideo Wanderers +2
- 1926: Uruguay Onward +1
- 1955: Sud América +1
- 1955: Liverpool de Montevideo -1
- 1994: Peñarol -4
- 1994: Nacional -4
- 1994: Bella Vista -1
- 1996: Cerro -5
- 2006/07: Cerrito -3
- 2008/09: Peñarol -3
- 2009/10: Nacional -3
- 2014/15: Peñarol -1
- 2014/15: Danubio +3
- 2014/15: El Tanque Sisley -3
- 2014/15: Cerro -1
- 2025: Nacional -3
- 2025: Cerro -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/uru-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 9)

- **uru06 · 838:** «[Apr 17]» → «[May 17]»: mês trocado: entre a rodada 12 (13/05) e a 15 (21/05); a ESPN dá maio (QU-006)
- **uru06 · 855:** «[Apr 18]» → «[May 18]»: mês trocado (QU-006)
- **uru06 · 860:** «[Apr 20]» → «[May 20]»: mês trocado (QU-006)
- **uru96 · 420:** «Nacional 1-1 Peñarol (59' Juan Martín Parodi; 55' Antonio Pacheco)» → «Nacional 1-1 Peñarol [59' Juan Martín Parodi; 55' Antonio Pacheco]»: autores entre parênteses na linha do jogo viravam parte do nome do Peñarol (UY-023)
- **uru34 · 156:** «4-1 Defensor» → «4-1 Sud América»: linha "Defensor 4-1 Defensor"; falta o 3º Defensor x Sud América e, com o Sud América, as linhas dos dois clubes fecham com a tabela publicada
- **uru41 · 169:** «1-0 Sud América» → «1-0 Liverpool»: linha "Sud América 1-0 Sud América"; falta o 2º Sud América x Liverpool e, com o Liverpool, as linhas dos dois clubes fecham com a tabela publicada
- **uru43 · 117:** «2-1 Racing» → «2-1 Rampla Juniors»: o Nacional aparece três vezes contra o Racing e uma contra o Rampla; com o Rampla, as linhas dos dois clubes fecham com a tabela publicada
- **uru56 · 127:** «5-1 Liverpool» → «3-1 Liverpool»: o 2º Peñarol x Liverpool aparece como 5-1, igual ao 1º; a Wikipédia em espanhol (Campeonato Uruguayo 1956) traz 3-1, que fecha com a tabela publicada para os dois clubes
- **uru40 · 119:** «3-9 Peñarol» → «3-0 Peñarol»: "3-9" não fecha com a tabela; com 3-0 (vitória do Wanderers) as linhas dos dois clubes fecham com ela

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 14)

- **2018 · uru2018:1010:** [descartado] Supercopa 2019 (03/02/2019) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2019 · uru2019:1040:** [descartado] Supercopa 2020 (01/02/2020) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2020 · uru2020:1152:** [descartado] Supercopa 2021 (02/05/2021) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2021 · uru2021:860:** [descartado] Supercopa 2022 (30/01/2022) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2022 · uru2022:1071:** [descartado] Supercopa 2023 (29/01/2023) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2023 · uru2023:1102:** [descartado] Supercopa 2024 (31/01/2024) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2024 · uru2024:1039:** [descartado] Supercopa 2025 (26/01/2025) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **2025 · uru2025:1041:** [descartado] Supercopa 2026 entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- **1908 · wiki:es_1908:842:** [wo_v] o Intrépido não compareceu: W.O. para o Bristol (UY-010)
- **1939 · uru39:127:** [wo_v, gm = 6, gv = 1] Nacional 6-1 Racing em campo; pontos dados ao Racing (jogador irregular do Nacional); a tabela conta os gols de campo
- **1947 · uru47:171:** [fase = Desempate do 2º lugar] jogo do triangular pelo 2º lugar (a página abre rodadas dentro do desempate)
- **1947 · uru47:175:** [fase = Desempate do 2º lugar] jogo do triangular pelo 2º lugar
- **1947 · uru47:179:** [fase = Desempate do 2º lugar] jogo do triangular pelo 2º lugar (não jogado)
- **1994 · uru94:314:** [descartado] linha com os dois primeiros jogos da final ("1-1 1-1"): vira dois jogos escritos à mão (EXTRAS)

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 2)

- **1994:** Peñarol 1-1 Defensor Sporting (Final, rsssf:uru94:314) 1º jogo da final (a página traz os dois empates na mesma linha, "1-1 1-1"; mando não informado)
- **1994:** Peñarol 1-1 Defensor Sporting (Final, rsssf:uru94:314) 2º jogo da final (a página traz os dois empates na mesma linha, "1-1 1-1"; mando não informado)

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **2005/06 · uru06:494:** "Annual Table 2005": soma o Torneo Especial 2005 e o Apertura 2005/06 (ano civil, para rebaixamento e vagas), não é tabela desta edição

### Divergências entre fontes já explicadas (`EXPLICACOES`, 10)

- **1951:** a tabela publicada (RSSSF e es concordam) não fecha com nenhum jogo da página (Nacional e Danubio com 1 vitória trocada); a classificação é a tabela publicada (UY-011)
- **1954:** vice Nacional (RSSSF e Wikipédia em inglês); a es dá o Danubio. Fica o da RSSSF até uma 3ª fonte (D-22 b, UY-007)
- **1913:** tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF, base da coleta (UY-012)
- **1917:** tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)
- **1919:** tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)
- **1920:** tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)
- **1955:** a es dá Sud América 15 e Liverpool 13 pontos; a RSSSF, 16 e 12 (ajustes de +1/-1); fica a RSSSF (UY-012)
- **1991:** tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)
- **2017:** artilheiro pela AUF: Maureen Franco 25; a es dá Cristian Palacios 29 (QU-008)
- **2023:** artilheiro pela AUF: Juan Ignacio Ramírez 18; a es dá 19 (QU-008)

### Identidade dos clubes

Regras em `coleta/uru-1/clubes_uru.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes uruguaios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Peñarol", "Nacional", "Defensor Sporting", "Montevideo Wanderers");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Liverpool de Montevideo", "Racing de Montevideo",
  "River Plate de Montevideo", "Colón de Montevideo", "Belgrano de Montevideo", "Universal de Montevideo",
  "Albion de Montevideo"; o mesmo para nomes genéricos que outros países do continente têm ("Libertad de Montevideo",
  "Olimpia de Montevideo", "Juventud de Las Piedras", "Atenas de San Carlos");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  Central -> Central Español; Defensor -> Defensor Sporting (fusão com o Sporting em 1989, que manteve a história do
  Defensor); Atlético Wanderers, Lito e Charley da FUF (1923-1924) ficam à parte dos clubes da AUF
  ("Atlético Wanderers", "Lito (FUF)", "Charley (FUF)": um clube não joga duas ligas rivais no mesmo ano; D-25 f, por Edicao.nomes); Deutscher -> Teutonia -> Montevideo FC; Torque -> Montevideo City Torque; C.U.R.C.C. -> Peñarol (como a RSSSF
  conta: a seção de futebol do C.U.R.C.C. virou o Peñarol em 1913-1914; o Nacional contesta, ver o relatório).
- fusões que criaram clube novo ficam separadas: Miramar e Misiones (até 1979) e Miramar Misiones (1980 em diante).
- o River Plate amador (River Plate FC, 1897-1929) não é o River Plate atual (fusão de Olimpia e Capurro em 1932).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano). A chave é o nome sem acento, em
minúsculas, com pontuação trocada por espaço (rsssf_sul.chave). Vale a primeira regra que casa com o começo da chave no ano
da edição; por isso as mais específicas vêm antes.
```

## 8. O que não deu para coletar

- **Edições sem jogos (45):** 1902-1903, 1906-1907, 1909-1915, 1917-1931 (com AUF e FUF) e 1975-1993. Nenhuma fonte pública que achamos tem os jogos desses anos (RSSSF, ogol e Wikipédias em espanhol e inglês trazem só a tabela final; para 1975-1993 a RSSSF tem só a liguilla pré-Libertadores). Elas entram com a tabela final da RSSSF (`uruhist.html`) como classificação e o campeão, sem jogos.
- **Fora do pacote:** as liguillas pré-Libertadores, o Torneo Integración (1994), o Torneo Nacional (1996), a Copa Artigas, o Torneo Permanencia (2001-2002), o Reclasificatorio (2004), a Copa AUF Uruguay, a Supercopa e os jogos de promoção contra clubes da 2ª divisão.
- **Edições sem jogos** (45): 1902, 1903, 1906, 1907, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923 AUF, 1923 FUF, 1924 AUF, 1924 FUF, 1926, 1927, 1928, 1929, 1931, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993.
- **Décadas com menos da metade dos gols com autor:** 1900s, 1910s, 1930s, 1940s, 1950s, 1960s, 1970s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1900s, 1910s, 1930s, 1940s, 1950s, 1960s, 1970s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): classificação pela tabela anual de 1994 em diante, pódio pela lista da AUF, Supercopa fora, títulos da FUF e de 1926 sem campeão (D-09), clubes da FUF à parte (D-25 f), 2020 no ano certo, artilheiros (AUF 2013/14-2025; es 1900-1931).

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/uru-1.md`):

- UY-001 (alta) A títulos FUF e Consejo Provisorio — 1923 FUF; 1924 FUF; 1926: A AUF não reconhece os títulos da FUF nem o torneio do Consejo Provisorio: 122 campeonatos; Peñarol 52 (com os 5 do CURCC) ou 47, Nacional 50, Wanderers 3. A RSSSF (base da coleta) conta as três | SUGESTÃO: Decisão do Gu
- UY-003 (media) A 1948 vice sem campeão — 1948: Edição abandonada na 10ª rodada: não há campeão nem vice | SUGESTÃO: 1948: vice vazio (campeonato abandonado na 10ª rodada). Mexer em: coleta/uru-1/importar.py, situacao(): não marcar 'vice' quando a edição não tem campe
- UY-004 (alta) A vice — 1995; 1996; 1998; 2000; 2001; 2002; 2004; 2007/08; 2008/09; 2011/12; 2013/14; 2014/15; 2021; 2025: Wikipédia es (AUF) e en concordam: 1995 Nacional; 1996 Nacional; 1998 Peñarol; 2000 Peñarol; 2001 Danubio; 2002 Danubio; 2004 Nacional; 2007/08 Peñarol; 2008/09 Defensor; 2011/12 Peñarol; 2013/14 Montevideo Wanderers; 20
- UY-005 (media) A 3º lugar — 1911; 1994; 1995; 1996; 1997; 1998; 2001; 2002; 2004; 2007/08; 2008/09; 2010/11; 2011/12; 2014/15; 2019; 2020; 2021; 2024; 2025: Wikipédia en (lista de campeões, coluna Third place): 1911 Nacional; 1994 Nacional; 1995 Liverpool; 1996 Defensor; 1997 River Plate de Montevideo; 1998 Bella Vista; 2001 Peñarol; 2002 Peñarol; 2004 Defensor; 2007/08 Rive
- UY-006 (alta) B classificação final = 1ª fase — 1994; 1995; 1996; 1998; 1999; 2000; 2001; 2002; 2003; 2004; 2006/07; 2007/08; 2008/09; 2009/10; 2010/11; 2011/12; 2012/13; 2013/14; 2014/15; 2015/16; 2017; 2019; 2020; 2021; 2022; 2023; 2024; 2025: Tabla Anual / acumulada: 2025 Nacional 79, Peñarol 78 (37 J), Liverpool 65, Juventud 61... Miramar Misiones 16º; 2023 Liverpool 74, Peñarol 69, Nacional 64, Defensor 60, Wanderers 50, Racing 50 (6º)... Diferenças linha a
- UY-007 (media) A 1954 vice em dúvida — 1954: Wikipédia es: Danubio vice (tabela 10 V 4 E 4 D, 31-21, 24 pts; lista de campeões também diz Danubio). A en diz Nacional. Fontes divergem; conferir a tabela (o jogo Danubio x Defensor está 3-0 no banco e 4-2 na es) | SUG
- UY-008 (baixa) A 1947 vice — 1947: Wikipédia es: subcampeão 'No se definió' (o triangular pelo 2º lugar entre Peñarol, Defensor e Rampla não terminou); en diz Peñarol | SUGESTÃO: decisão: ver decisoes
- UY-010 (media) B 1908 W.O. com vencedor trocado — 1908: Quem não compareceu foi o Intrépido: vitória do Bristol. Tabelas publicadas (RSSSF uruhist e es): Bristol 5º (8 V 1 E 9 D, 17 pts), Intrépido 0 V 18 D. A ordem de 5º a 8º muda | SUGESTÃO: 1908: Intrépido x Bristol (24/08
- UY-011 (media) B 1951 classificação calculada x tabelas publicadas — 1951: RSSSF (uru51) e Wikipédia es concordam: Nacional 12 V 3 E 3 D (50-21, 27), Danubio 6º 6 V 4 E 8 D (30-36, 16); Central Español 4º e Cerro 5º. Um jogo Nacional x Danubio deve estar com o resultado trocado | SUGESTÃO: 1951
- UY-012 (baixa) B tabelas sem jogos: divergências pequenas — 1913; 1917; 1919; 1920; 1955; 1991: Wikipédia es: 1913 Central Español 3º e Peñarol 4º (5 V 3 E 6 D); 1917 Peñarol 15 V 2 E 1 D; 1919 Universal 28; 1920 Peñarol GP 47; 1955 Sud América 15, Liverpool 13; 1991 Defensor 13 V 8 E 5 D, Bella Vista 9º, Huracán B
- UY-013 (media) C Supercopa dentro da Final — 2018; 2019; 2020; 2021; 2022; 2023; 2024; 2025: RSSSF: os jogos estão sob o título 'Supercopa AUF' (campeão x campeão do Intermedio, jogados em jan/fev do ano seguinte; ex. 01/02/2026 em 2025). A Supercopa está entre as competições que o relatório da coleta diz deixar
- UY-014 (media) C datas das decisões — 1994; 1996; 1997; 1999; 2000; 2001; 2002; 2003; 2004; 2005; 2005/06; 2007/08; 2008/09; 2009/10; 2013/14; 2015/16; 2017; 2018; 2019; 2020; 2021; 2022; 2023; 2025: RSSSF/ESPN/Wikipédia es: 2025 final 23/11 e 30/11; 2005/06 semifinal 22/06 e 25/06; 1997 desempate 05/11, finais 09/11 e 12/11; 2009/10 final 12/05; 1996 finais 13/10 e 20/10. Lista: revisao/UY/saida_datas_repetidas.txt 
- UY-015 (media) C 2020 ano das datas — 2020: Apertura 2020 começou em 15/02/2020 e o Intermedio terminou em jan/2021 (a temporada foi esticada até abril de 2021 pela pandemia) | SUGESTÃO: 2020: Apertura e Intermedio em 2020 (AUF: 1ª rodada 15/02/2020; Final do Aper
- UY-016 (baixa) C placares divergentes só da Wikipédia es — 1933; 1936; 1948; 1949; 1951; 1952; 1954; 1959; 1997; 2011/12; 2012/13; 2013/14; 2014/15; 2015/16: Wikipédia es: 1936 5-2; 1954 4-2... De 2011/12 em diante o ogol (conferência da coleta) concorda com o banco: provável erro da es. 1933-1959 sem terceira fonte. Lista: revisao/UY/saida_jogos_es.txt | SUGESTÃO: Nos anos q
- UY-017 (media) D artilheiro pela contagem parcial — 2013/14; 2014/15; 2015/16; 2017; 2018; 2019; 2020; 2021; 2022; 2023; 2024; 2025: Wikipédia es: 2014/15 Iván Alonso 23; 2017 Cristian Palacios 29; 2019 Juan Ignacio Ramírez 24; 2022 Thiago Borbas 18; 2023 Juan Ignacio Ramírez 19; 2013/14 Acuña 20; 2015/16 Gastón Rodríguez e Junior Arias 19; 2018 Berge
- UY-018 (baixa) D artilheiro ausente 1900-1931 — 1900 a 1931 (28 edições): Wikipédia es tem o goleador de todas (ex.: 1900 James Buchanan 6; 1918 Héctor Scarone 22; 1924 Pedro Petrone 20) | SUGESTÃO: 1900-1931: artilheiro da coluna 'Goleador' da es (ex.: 1900 James Buchanan 6; 1918 Héctor Scaro
- UY-019 (baixa) D artilheiro: fontes divergem — 1935; 1940; 1945; 1946; 1947; 1951; 1952; 1958; 1962; 1964; 1972; 1993; 2001; 2005/06; 2009/10: Wikipédia es: 1940 19; 1945 19; 1946 22; 1947 18; 1951 16; 1952 Héctor Rial 14; 1958 16; 1962 17; 1964 11; 1993 13; 2001 18; 2009/10 23; 'Antonio Castaldo', 'Juan Mamelli', 'Pedro Cardoso' | SUGESTÃO: Divergências RSSSF 
- UY-020 (media) E Atlético Wanderers juntado ao Montevideo Wanderers — 1923 FUF; 1924 FUF: RSSSF (uruhist) chama o campeão de 1923 FUF de 'Atlético Wanderers'; a Wikipédia es diz que era um equipo alternativo do Montevideo Wanderers, que seguia na AUF (o mesmo com Charley e Lito) | SUGESTÃO: decisão: ver decis
- UY-023 (baixa) E nome de fonte com lixo — 1996: Sobra da leitura da final de 1996 ('Nacional 1-1 Peñarol (59' Juan Martín Parodi; 55' Antonio Pacheco)') | SUGESTÃO: Tirar 'Peñarol (59' Juan Martín Parodi; 55' Antonio Pacheco)' do nomes_fonte: a linha da final de 1996 
- QU-006 (media) C datas — 2005/06: ESPN (data/coleta/uru-1/espn, eventos 195275 a 195289): 17, 18 e 20/05/2006. A própria página da RSSSF traz 'Round 12 [May 13]', 'Round 13 [Apr 17]', 'Round 14 [Apr 20]' e 'Round 15 [May 21]': erro de digitação. | SUGEST
- QU-008 (baixa) D artilheiro — 2017; 2023: Artilharia oficial da AUF ('Goleadores de la Temporada'): 2017 Maureen Franco (Cerro) 25, Cristian Rodríguez 16; 2023 Juan Ignacio Ramírez (Nacional) 18, Matías Arezo 17. Nas outras 10 edições a AUF e a es concordam. | S

## 10. Arquivos e comandos

Código em `coleta/uru-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga uru.1) de 2001 a 2025 para data/coleta/uru-1/espn/uru1_<ano>.json. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão uruguaia no ogol para data/coleta/uru-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão uruguaia para data/coleta/uru-1/rsssf/. |
| `baixar_wikipedia.py` | Baixa da Wikipédia em espanhol o texto-fonte das páginas "Campeonato Uruguayo de Primera División <ano>" (1900 a 1993) |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "Liga AUF Uruguaya", seção "List of champions"), segunda fonte do |
| `clubes_uru.py` | Identidade dos clubes uruguaios: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão uruguaia (uru-1): uma por torneio que deu título de campeão uruguaio. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão uruguaia, edição a edição (entram no relatório). |
| `goleadores_es.py` | Artilheiros de 1900 a 1931 pela coluna "Goleador" da tabela "Títulos de liga por año" da Wikipédia em espanhol (página |
| `importar.py` | Junta as fontes da 1ª divisão uruguaia e grava o pacote em data/coleta/uru-1/pacote/ e o relatório em docs/coleta/uru-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/uru-1/rsssf/) com o leitor comum (rsssf_sul) e, |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wikipedia_jogos.py` | Jogos da Wikipédia em espanhol (data/coleta/uru-1/wikipedia/es_<ano>.txt), para os anos que a RSSSF não tem. |

- Fontes baixadas: `data/coleta/uru-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`, do ogol em `data/cache/ogol-uru-1/`.
- Pacote: `data/coleta/uru-1/pacote/`; relatório: `docs/coleta/uru-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/uru-1/baixar_espn.py
python coleta/uru-1/baixar_ogol.py
python coleta/uru-1/baixar_rsssf.py
python coleta/uru-1/baixar_wikipedia.py
python coleta/uru-1/importar.py
python coleta/uru-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py uru-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

