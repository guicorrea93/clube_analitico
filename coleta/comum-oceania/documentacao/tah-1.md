# Campeonato Taitiano (`tah-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/tah-1/pacote/`, do código `coleta/tah-1/` e do relatório `docs/coleta/tah-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 79, de 1948 a 2025/26; 48 sem jogos.
- **Jogos:** 2647 (2639 com placar); **gols:** 11748; **gols com autor:** 113 (1%); **cartões:** 0.
- **Clubes:** 35; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 79 edições; **tabelas publicadas guardadas para conferência:** 413 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão do Taiti (Polinésia Francesa) de 1948 a 2025/26, uma edição por título, como na lista de campeões da RSSSF: Division d'Honneur, Division Fédérale (2003/04) e Ligue 1 (2008/09). A maioria das edições até 1998 tem só o campeão; jogos em 1968 (parte), 1969-1971 e de 1998/99 em diante (parte até 2004/05; 2011/12 só com as tabelas). Pontuação de 4 pontos por vitória, 2 por empate e 1 por derrota na maior parte dos anos recentes; a classificação traz os pontos oficiais.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão do Taiti (tah-1): uma por título, como na lista de campeões da RSSSF (tahitichamp.html), de 1948 a
2025/26. Escopo aprovado pelo Guilherme em 24/11/2026:
- começa em 1948 (a lista oficial); a RSSSF dá o ano em que a temporada termina: "1999" é 1998/99, e assim por diante; antes
  de 1999 fica o ano da lista;
- até 2025/26 (a última terminada);
- em 1956, 1957 e 1961 vale a RSSSF (a Wikipédia diverge, mas copia uma versão antiga da própria RSSSF);
- entram a fase regular, o playoff do título (com o campeão de Mooréa, quando havia) e o grupo do rebaixamento; ficam de
  fora copas, 2ª e 3ª divisões, ligas das outras ilhas e as séries de acesso/rebaixamento com clubes da 2ª divisão
  ("Promotion/Relegation Playoff", "Playin").

O que a RSSSF traz:
- 1948-1967, 1972-1984, 1985 e 1986-1998: só o campeão (e o vice em 1990, 1992 e 1995-1998);
- 1968: 5 resultados e a classificação sem números; 1969-1971: as 14 rodadas e a tabela;
- 1998/99 a 2004/05: parte dos jogos (muitos só "venceu"/"perdeu", sem placar) e tabelas, às vezes parciais;
- 2005/06 a 2025/26: as rodadas e as tabelas (2010/11 e 2011/12: só as tabelas; 2009/10: o playoff numa seção à parte).

Pontuação (conferida pela conta das tabelas): 3-2-1 (vitória, empate, derrota) em 1969-1971 e 2007/08; 3-1-0 de 1998/99 a
2002/03; 4-2-1 em 2003/04-2006/07 e de 2008/09 em diante. Há pontos-bônus (vencedor da fase regular, obrigações com
treinadores, árbitros e categorias de base) e pontos tirados: ficam no ajuste da classificação.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 23.
- **Edições com alguma tabela divergente** (0; motivo no relatório, na edição): nenhuma.
- **Edições sem tabela para conferir** (56): 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1998/99, 1999/00, 2000/01, 2001/02, 2002/03, 2003/04, 2004/05, 2011/12.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1940s | 2 | 0 | — | — | — | — | — | — | — | — |
| 1950s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 10 | 47 | 89% | 0% | 89% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 112 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 11 | 24 | 0% | 0% | 75% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 798 | 86% | 0% | 100% | 0% | 0% | 0% | 4% | 0.0 |
| 2010s | 10 | 896 | 99% | 0% | 99% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 770 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1948 a 1967: 1 clubes
- 1968: 6 clubes
- 1969: 7 clubes
- 1970 a 1971: 8 clubes
- 1972 a 1989: 1 clubes
- 1990: 2 clubes
- 1991: 1 clubes
- 1992: 2 clubes
- 1993 a 1994: 1 clubes
- 1995 a 1998: 2 clubes
- 1998/99: 9 clubes
- 1999/00: 12 clubes
- 2000/01: 11 clubes
- 2001/02: 9 clubes
- 2002/03: 10 clubes
- 2003/04 a 2004/05: 8 clubes
- 2005/06 a 2006/07: 9 clubes
- 2007/08: 10 clubes
- 2008/09: 11 clubes
- 2009/10: 10 clubes
- 2010/11: 11 clubes
- 2011/12 a 2012/13: 12 clubes
- 2013/14 a 2014/15: 10 clubes
- 2015/16: 8 clubes
- 2016/17 a 2019/20: 10 clubes
- 2020/21: 13 clubes
- 2021/22 a 2023/24: 12 clubes
- 2024/25: 10 clubes
- 2025/26: 11 clubes

**Pontos por vitória:**

- 1948 a 1968: 
- 1969 a 1971: 3
- 1972 a 1998: 
- 1998/99 a 2002/03: 3
- 2003/04 a 2006/07: 4
- 2007/08: 3
- 2008/09 a 2025/26: 4

**Nome oficial:**

- 1948 a 2002/03: Division d'Honneur <ano>
- 2003/04 a 2007/08: Division Fédérale <ano>
- 2008/09 a 2025/26: Ligue 1 <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1948 a 1967: só o campeão (sem jogos nem tabela)
- 1968: jogos incompletos: pontos corridos
- 1969: pontos corridos (7 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota
- 1970 a 1971: pontos corridos (8 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota
- 1972 a 1998: só o campeão (sem jogos nem tabela)
- 1998/99: jogos incompletos: pontos corridos; 3 pontos por vitória, 1 por empate e 0 por derrota
- 1999/00: jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2000/01: jogos incompletos: pontos corridos; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2001/02: jogos incompletos: fase regular + playoff do título (5 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2002/03: jogos incompletos: fase regular (10 clubes) + playoff do título (5 clubes) + grupo do rebaixamento (5 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2003/04: jogos incompletos: fase regular (8 clubes) + playoff do título (4 clubes) + grupo do rebaixamento (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2004/05: jogos incompletos: fase regular + playoff do título + grupo do rebaixamento; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2005/06 a 2006/07: fase regular (9 clubes) + playoff do título (5 clubes) + grupo do rebaixamento (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2007/08: fase regular (10 clubes) + playoff do título (4 clubes) + grupo do rebaixamento (6 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota
- 2008/09: fase regular (10 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2009/10: fase regular (9 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2010/11: jogos incompletos: fase regular (10 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2011/12: jogos incompletos: fase regular (11 clubes) + playoff do título (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2012/13: fase regular (11 clubes) + playoff do título (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2013/14 a 2014/15: fase regular (10 clubes) + playoff do título (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2015/16: fase regular (8 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2016/17: fase regular (10 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2017/18 a 2019/20: pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2020/21: fase regular (13 clubes) + playoff do título (7 clubes) + grupo do rebaixamento (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2021/22: pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2022/23 a 2023/24: fase regular (12 clubes) + playoff do título (6 clubes) + grupo do rebaixamento (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2024/25: pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2025/26: fase regular (10 clubes) + playoff do título (6 clubes) + grupo do rebaixamento (5 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota

**Fases e grupos de cada edição com mais de uma fase:**

- 2001/02: Fase regular (liga); Playoff do título (liga)
- 2002/03: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2003/04: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2004/05: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2005/06: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2006/07: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2007/08: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2008/09: Fase regular (liga); Playoff do título (liga)
- 2009/10: Fase regular (liga); Playoff do título (liga)
- 2010/11: Fase regular (liga); Playoff do título (liga)
- 2011/12: Fase regular (liga); Playoff do título (liga)
- 2012/13: Fase regular (liga); Playoff do título (liga)
- 2013/14: Fase regular (liga); Playoff do título (liga)
- 2014/15: Fase regular (liga); Playoff do título (liga)
- 2015/16: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2016/17: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2020/21: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2022/23: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2023/24: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)
- 2025/26: Fase regular (liga); Playoff do título (liga); Grupo do rebaixamento (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- lista de campeões da RSSSF: 50 edições
- RSSSF: 29 edições

**Observações das edições:**

- 1948: só o campeão na lista da RSSSF
- 1949: só o campeão na lista da RSSSF
- 1950: só o campeão na lista da RSSSF
- 1951: só o campeão na lista da RSSSF
- 1952: só o campeão na lista da RSSSF
- 1953: só o campeão na lista da RSSSF
- 1954: só o campeão na lista da RSSSF
- 1955: só o campeão na lista da RSSSF
- 1956: só o campeão na lista da RSSSF
- 1957: só o campeão na lista da RSSSF
- 1958: só o campeão na lista da RSSSF
- 1959: só o campeão na lista da RSSSF
- 1960: só o campeão na lista da RSSSF
- 1961: só o campeão na lista da RSSSF
- 1962: só o campeão na lista da RSSSF
- 1963: só o campeão na lista da RSSSF
- 1964: só o campeão na lista da RSSSF
- 1965: só o campeão na lista da RSSSF
- 1966: só o campeão na lista da RSSSF
- 1967: só o campeão na lista da RSSSF
- 1968: só 5 resultados e a classificação sem números (Journal de Tahiti)
- 1972: só o campeão na lista da RSSSF
- 1973: só o campeão na lista da RSSSF
- 1974: só o campeão na lista da RSSSF
- 1975: só o campeão na lista da RSSSF
- 1976: só o campeão na lista da RSSSF
- 1977: só o campeão na lista da RSSSF
- 1978: só o campeão na lista da RSSSF
- 1979: só o campeão na lista da RSSSF
- 1980: só o campeão na lista da RSSSF
- 1981: só o campeão na lista da RSSSF
- 1982: só o campeão na lista da RSSSF
- 1983: só o campeão na lista da RSSSF
- 1984: só o campeão na lista da RSSSF
- 1985: só o campeão na lista da RSSSF
- 1986: só o campeão na lista da RSSSF
- 1987: só o campeão na lista da RSSSF
- 1988: só o campeão na lista da RSSSF
- 1989: só o campeão na lista da RSSSF
- 1990: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1991: só o campeão na lista da RSSSF
- 1992: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1993: só o campeão na lista da RSSSF
- 1994: só o campeão na lista da RSSSF
- 1995: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1996: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1997: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1998: só o campeão na lista da RSSSF (e o vice, AS Pirae)
- 1998/99: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 1999/00: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2000/01: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2001/02: o Juventus abandonou o campeonato no meio da temporada; a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2002/03: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2003/04: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2004/05: a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais
- 2008/09: a seleção sub-20 do Taiti ("Tahiti U-20") jogou a fase regular no lugar de um clube
- 2010/11: o playoff do título só tem a tabela na RSSSF
- 2011/12: a RSSSF só tem as tabelas da fase regular e do playoff do título
- 2019/20: temporada interrompida pela covid-19; o AS Pirae, 1º da tabela, foi declarado campeão
- 2020/21: covid-19: turno único na fase regular, depois os playoffs

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Central Sport: 21
- AS Vénus: 12
- AS Pirae: 12
- AS Fei Pi: 7
- AS Tefana: 7
- AS Excelsior: 6
- AS Manu-Ura: 5
- AS Jeunes Tahitiens: 3
- AS Dragon: 3
- AS Tamarii Punaruu: 1
- AS Arue: 1
- AS PTT: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1948 | AS Fei Pi | — |
| 1949 | AS Fei Pi | — |
| 1950 | AS Fei Pi | — |
| 1951 | AS Fei Pi | — |
| 1952 | AS Excelsior | — |
| 1953 | AS Vénus | — |
| 1954 | AS Jeunes Tahitiens | — |
| 1955 | Central Sport | — |
| 1956 | AS Vénus | — |
| 1957 | AS Jeunes Tahitiens | — |
| 1958 | Central Sport | — |
| 1959 | AS Excelsior | — |
| 1960 | AS Excelsior | — |
| 1961 | AS Excelsior | — |
| 1962 | Central Sport | — |
| 1963 | Central Sport | — |
| 1964 | Central Sport | — |
| 1965 | Central Sport | — |
| 1966 | Central Sport | — |
| 1967 | Central Sport | — |
| 1968 | AS Fei Pi | AS Tamarii Punaruu |
| 1969 | AS Tamarii Punaruu | AS Fei Pi |
| 1970 | AS Fei Pi | AS Vénus |
| 1971 | AS Fei Pi | AS Vaiete |
| 1972 | Central Sport | — |
| 1973 | Central Sport | — |
| 1974 | Central Sport | — |
| 1975 | Central Sport | — |
| 1976 | Central Sport | — |
| 1977 | Central Sport | — |
| 1978 | Central Sport | — |
| 1979 | Central Sport | — |
| 1980 | AS Arue | — |
| 1981 | Central Sport | — |
| 1982 | Central Sport | — |
| 1983 | Central Sport | — |
| 1984 | AS PTT | — |
| 1985 | Central Sport | — |
| 1986 | AS Excelsior | — |
| 1987 | AS Jeunes Tahitiens | — |
| 1988 | AS Excelsior | — |
| 1989 | AS Pirae | — |
| 1990 | AS Vénus | AS Pirae |
| 1991 | AS Pirae | — |
| 1992 | AS Vénus | AS Pirae |
| 1993 | AS Pirae | — |
| 1994 | AS Pirae | — |
| 1995 | AS Vénus | AS Pirae |
| 1996 | AS Manu-Ura | AS Pirae |
| 1997 | AS Vénus | AS Pirae |
| 1998 | AS Vénus | AS Pirae |
| 1998/99 | AS Vénus | AS Pirae |
| 1999/00 | AS Vénus | AS Pirae |
| 2000/01 | AS Pirae | — |
| 2001/02 | AS Vénus | AS Pirae |
| 2002/03 | AS Pirae | AS Manu-Ura |
| 2003/04 | AS Manu-Ura | AS Pirae |
| 2004/05 | AS Tefana | AS Pirae |
| 2005/06 | AS Pirae | AS Tefana |
| 2006/07 | AS Manu-Ura | AS Tefana |
| 2007/08 | AS Manu-Ura | AS Tefana |
| 2008/09 | AS Manu-Ura | AS Tefana |
| 2009/10 | AS Tefana | AS Vaiete |
| 2010/11 | AS Tefana | AS Dragon |
| 2011/12 | AS Dragon | AS Tamarii Faa'a |
| 2012/13 | AS Dragon | AS Tamarii Faa'a |
| 2013/14 | AS Pirae | AS Tefana |
| 2014/15 | AS Tefana | AS Pirae |
| 2015/16 | AS Tefana | Central Sport |
| 2016/17 | AS Dragon | AS Vénus |
| 2017/18 | Central Sport | AS Tefana |
| 2018/19 | AS Vénus | AS Tiare Tahiti |
| 2019/20 | AS Pirae | AS Vénus |
| 2020/21 | AS Pirae | AS Vénus |
| 2021/22 | AS Pirae | AS Dragon |
| 2022/23 | AS Tefana | AS Pirae |
| 2023/24 | AS Pirae | AS Vénus |
| 2024/25 | AS Vénus | AS Pirae |
| 2025/26 | AS Tefana | AS Pirae |

**Rebaixados marcados na classificação:** 40 em 19 edições (só onde a tabela publicada marca a queda); quem mais caiu: AS Vénus (5), AS Arue (4), AS Aorai (4), AS Excelsior (3), AS Manu-Ura (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 2002/03: AS Dragon -1
- 2002/03: AS Vénus -1
- 2004/05: AS Pirae +2
- 2004/05: AS Vénus +1
- 2005/06: AS Pirae +2
- 2006/07: AS Dragon +2
- 2007/08: AS Manu-Ura +2
- 2007/08: AS Tamarii Temanava -1
- 2007/08: AS Tamarii Faa'a +34
- 2007/08: AS Jeunes Tahitiens +37
- 2007/08: AS Pirae +32
- 2007/08: AS Taravao AC +31
- 2007/08: Central Sport +32
- 2007/08: AS Aorai +22
- 2008/09: AS Tefana +2
- 2009/10: AS Tefana +2
- 2009/10: AS Vaiete +2
- 2009/10: AS Tamarii Faa'a +2
- 2009/10: AS Pirae +2
- 2009/10: AS Manu-Ura +4
- 2009/10: AS Tamarii Temanava +2
- 2009/10: AS Dragon +2
- 2009/10: AS Vénus +2
- 2009/10: AS Jeunes Tahitiens +2
- 2010/11: AS Tefana +2
- 2010/11: Central Sport +2
- 2010/11: AS Pirae +2
- 2010/11: AS Vairao +2
- 2010/11: AS Excelsior +4
- 2011/12: AS Dragon +2
- 2012/13: AS Dragon +2
- 2012/13: AS Roniu -1
- 2012/13: AS Vénus +2
- 2012/13: AS Pirae +2
- 2012/13: AS Tamarii Punaruu +2
- 2013/14: AS Pirae +2
- 2014/15: AS Tefana +4
- 2014/15: AS Pirae +4
- 2014/15: Central Sport +4
- 2014/15: AS Dragon +4
- 2014/15: AS Roniu +2
- 2014/15: AS Excelsior +2
- 2014/15: AS Tamarii Faa'a +2
- 2015/16: AS Tefana +4
- 2015/16: Central Sport +10
- 2015/16: AS Vénus +8
- 2015/16: AS Pirae +10
- 2015/16: AS Manu-Ura +2
- 2015/16: AS Dragon +6
- 2015/16: AS Taiarapu +10
- 2015/16: AS Aorai +2
- 2016/17: AS Dragon +6
- 2016/17: AS Vénus +4
- 2016/17: AS Tefana +6
- 2016/17: Central Sport +6
- 2016/17: AS Taiarapu +4
- 2016/17: AS Pirae +4
- 2016/17: AS Manu-Ura +2
- 2016/17: AS Arue +4
- 2016/17: AS Olympic Mahina +4
- 2017/18: AS Aorai -2
- 2017/18: AS Tamarii Punaruu -3
- 2018/19: AS Dragon -2
- 2019/20: AS Manu-Ura -4
- 2019/20: AS Taravao AC -2
- 2019/20: AS Jeunes Tahitiens -2
- 2020/21: AS Pirae +2
- 2021/22: AS Pirae -1
- 2021/22: AS Tamarii Punaruu -1
- 2021/22: AS Tamarii Temanava -2
- 2021/22: AS Tiare Tahiti -2
- 2021/22: AS Mataiea -1
- 2022/23: AS Pirae -1
- 2022/23: AS Tamarii Temanava -1
- 2022/23: AS Olympic Mahina -2
- 2023/24: AS Tefana -1
- 2023/24: AS Pueu -1
- 2023/24: AS Tamarii Temanava -1
- 2024/25: AS Mira -1
- 2024/25: AS Taiarapu -2
- 2024/25: AS Manu-Ura -1
- 2025/26: AS Taiarapu -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/tah-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 2)

- **tahiti71 · 159:** ({'especial': 'anulado'}, 'resultado não homologado por erro do árbitro; o jogo foi repetido (0-6)')
- **tahiti2022 · 99:** ({'especial': 'derrota_ambos'}, 'a federação deu derrota aos dois clubes ("awarded 0-0 loss to both"); em campo, 3-0')

### Tabelas da página que não são da edição (`TABELAS_FORA`, 2)

- **tahiti01 · 36:** tabela depois de 6 rodadas (2000/01)
- **tahiti01 · 75:** tabela depois de 14 rodadas (2000/01); a final não está na página

### Identidade dos clubes

Regras em `coleta/tah-1/clubes_tah.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes do Taiti (tah-1): cada grafia da RSSSF vira um clube, com cidade e ilha (região).

Decisões (o mesmo clube com outro nome é um clube só):
- nome com "AS" (decisão do Guilherme, 24/11), salvo "Central Sport" (sem "AS" no uso corrente);
- Punaruu = AS Tamarii Punaruu (a RSSSF de 1968: "Punaruu (aka Tamarii Punaruu)"); Temanava = AS Tamarii Temanava (Mooréa);
  Arue, JS Arue e AS Arue (nome completo Tamarii Nahiti d'Arue) = AS Arue; "Paea" de 1971 = AS Manu-Ura ("A.S. Manu Ura de
  Paea relegated");
- seleções de base que jogaram a liga: "Tahiti U-17" (inclui "Tahiti Nui U-17"), "Tahiti U-19" e "Tahiti U-20", como a RSSSF
  escreve (uma por categoria);
- "AS Juventus" (Papeari) não é a Juventus italiana (nome diferente no banco).

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
```

## 8. O que não deu para coletar

- **Edições sem jogos** (48): 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2011/12.
- **Décadas com menos da metade dos gols com autor:** 1960s, 1970s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1960s, 1970s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1948-1967 e 1972-1998 só com o campeão (e o vice em 8 anos): nenhuma fonte aberta tem jogos ou tabelas.
- 1956, 1957 e 1961: a Wikipédia dá outro campeão (copia uma versão antiga da RSSSF); vale a RSSSF (decisão do Guilherme, 24/11/2026). Uma fonte da época (Journal de Tahiti) resolveria.
- 1998/99 a 2004/05 com parte dos jogos; 2010/11 (playoff) e 2011/12 só com as tabelas.
- Autores dos gols só em poucas temporadas; artilheiros, cartões, estádio e público não coletados.

## 10. Arquivos e comandos

Código em `coleta/tah-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga do Taiti ("Liga Taiti", competição 752) para data/cache/ogol-tah-1/ e grava o resumo |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF do Taiti para data/coleta/tah-1/rsssf/ (lista de campeões e as páginas por temporada que ela |
| `baixar_wikipedia.py` | Baixa o wikitexto da Wikipédia em inglês sobre a liga do Taiti para data/coleta/tah-1/wikipedia/: a página da liga |
| `clubes_tah.py` | Identidade dos clubes do Taiti (tah-1): cada grafia da RSSSF vira um clube, com cidade e ilha (região). |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão do Taiti (tah-1): uma por título, como na lista de campeões da RSSSF (tahitichamp.html), de 1948 a |
| `explicacoes.py` | Correções e decisões da coleta do Taiti (tah-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão do Taiti e grava o pacote em data/coleta/tah-1/pacote/ e o relatório em docs/coleta/tah-1.md. |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/tah-1/rsssf/), trecho a trecho (edicoes.py), |

- Fontes baixadas: `data/coleta/tah-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-tah-1/`.
- Pacote: `data/coleta/tah-1/pacote/`; relatório: `docs/coleta/tah-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/tah-1/baixar_ogol.py
python coleta/tah-1/baixar_rsssf.py
python coleta/tah-1/baixar_wikipedia.py
python coleta/tah-1/importar.py
python coleta/tah-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py tah-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

