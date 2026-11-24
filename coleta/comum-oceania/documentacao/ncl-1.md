# Campeonato Neocaledônio (`ncl-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/ncl-1/pacote/`, do código `coleta/ncl-1/` e do relatório `docs/coleta/ncl-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 76, de 1950 a 2026; 40 sem jogos.
- **Jogos:** 2472 (2467 com placar); **gols:** 9956; **gols com autor:** 188 (2%); **cartões:** 0.
- **Clubes:** 63; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 76 edições; **tabelas publicadas guardadas para conferência:** 296 linhas.
- **No banco:** sim; **último commit do pacote:** 8f154e1.
- **Observação da competição:** 1ª divisão da Nova Caledônia de 1950 a 2026, uma edição por título, como na lista de campeões da RSSSF: campeonato territorial entre os campeões regionais (até 2001), liga da Grande Terre e playoff nacional com o campeão das ilhas (2002-2011) e Super Ligue (2012 em diante). Sem campeão em 1955 e 2024 (fora). Até 1996 quase só o campeão; jogos desde 1999 (e a final em parte dos anos antes). Pontuação de 4 pontos por vitória, 2 por empate e 1 por derrota; a classificação traz os pontos oficiais.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão da Nova Caledônia (ncl-1): uma por título, como na lista de campeões da RSSSF (newcalchamp.html), de
1950 a 2026. Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo:
- começa em 1950 (1933 e 1934-1949 ficam de fora); 1955 (sem campeão) e 2024 (abandonada, a federação não declarou campeão)
  não entram;
- 1963 e 1964: Club Sportif Militaire (RSSSF atual; a versão antiga, copiada por Wikipédia e ogol, dava USC e JS Vallée du Tir);
- até 2001 entra só a fase nacional (as ligas das províncias eram competições regionais à parte); de 2002 a 2011 a liga da
  Grande Terre entra como 1ª fase ("Fase regional", grupo "Grande Terre") e o campeão das ilhas entra direto no playoff (o
  torneio das ilhas fica de fora); de 2012 em diante, a Super Ligue única.

O que a RSSSF traz:
- 1950-1988: só o campeão (a final na lista em 1964, 1971, 1977 e 1978; página com a final em 1984 e o mata-mata em 1985);
- 1989-1996: campeão, vice e 3º (em parte dos anos);
- 1997-2001: mata-mata nacional (1997 e 1998 em parte; 1999-2001 completo);
- 2002-2011: liga da Grande Terre e o playoff/mata-mata nacional (2005/06 e 2009 sem playoff: o campeão da Grande Terre);
- 2012-2026: Super Ligue (2020 com playoff do título; 2025 com grupos e mata-mata).

Pontuação: 4 por vitória, 2 por empate e 1 por derrota (a RSSSF anota desde 1999). Temporadas que cruzam o ano: 2002/03 a 2008/09.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 21.
- **Edições com alguma tabela divergente** (4; motivo no relatório, na edição): 2004/05, 2013, 2015, 2018.
- **Edições sem tabela para conferir** (51): 1950, 1951, 1952, 1953, 1954, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001.
- **Edições com menos jogos que o esperado:** 2004/05 (113 de 115), 2013 (109 de 110), 2015 (131 de 133).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 10 | 1 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 3 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 6 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 16 | 38% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 11 | 740 | 93% | 0% | 94% | 0% | 0% | 0% | 5% | 0.0 |
| 2010s | 10 | 1142 | 100% | 0% | 100% | 0% | 0% | 0% | 1% | 0.0 |
| 2020s | 6 | 564 | 100% | 0% | 98% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1950 a 1962: 1 clubes
- 1963 a 1964: 2 clubes
- 1965 a 1966: 1 clubes
- 1967: 2 clubes
- 1968 a 1970: 1 clubes
- 1971: 2 clubes
- 1972 a 1974: 1 clubes
- 1975: 2 clubes
- 1976: 1 clubes
- 1977 a 1978: 2 clubes
- 1979 a 1983: 1 clubes
- 1984: 2 clubes
- 1985: 6 clubes
- 1986 a 1988: 1 clubes
- 1989: 3 clubes
- 1990: 1 clubes
- 1991: 3 clubes
- 1992: 1 clubes
- 1993 a 1996: 3 clubes
- 1997: 2 clubes
- 1998: 4 clubes
- 1999: 7 clubes
- 2000: 8 clubes
- 2001: 7 clubes
- 2002: 9 clubes
- 2002/03 a 2003/04: 11 clubes
- 2004/05: 12 clubes
- 2005/06: 8 clubes
- 2006/07 a 2008/09: 9 clubes
- 2009: 8 clubes
- 2010 a 2011: 9 clubes
- 2012 a 2013: 11 clubes
- 2014 a 2015: 12 clubes
- 2016: 13 clubes
- 2017 a 2018: 12 clubes
- 2019 a 2020: 10 clubes
- 2021: 13 clubes
- 2022 a 2023: 12 clubes
- 2025 a 2026: 10 clubes

**Pontos por vitória:**

- 1950 a 1998: 
- 1999 a 2026: 4

**Nome oficial:**

- 1950 a 2001: Championnat territorial <ano>
- 2002 a 2006/07: Division d'Honneur (Grande Terre) e Championnat de Nouvelle-Calédonie <ano>
- 2007/08 a 2011: Super Ligue (Grande Terre) e Championnat de Nouvelle-Calédonie <ano>
- 2012 a 2026: Super Ligue <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1950 a 1963: só o campeão (sem jogos nem tabela)
- 1964: só a final (da lista de campeões)
- 1965 a 1970: só o campeão (sem jogos nem tabela)
- 1971: só a final (da lista de campeões)
- 1972 a 1976: só o campeão (sem jogos nem tabela)
- 1977 a 1978: só a final (da lista de campeões)
- 1979 a 1983: só o campeão (sem jogos nem tabela)
- 1984: final
- 1985: rodada preliminar + semifinais + final
- 1986 a 1996: só o campeão (sem jogos nem tabela)
- 1997: jogos incompletos: final
- 1998: semifinais + final
- 1999 a 2001: quartas de final + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2002: liga da Grande Terre (8 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2002/03 a 2003/04: liga da Grande Terre (10 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2004/05: liga da Grande Terre (11 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2005/06: pontos corridos (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2006/07 a 2008/09: liga da Grande Terre (8 clubes) + grupo do rebaixamento (Grande Terre) (5 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2009: pontos corridos (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2010 a 2011: liga da Grande Terre (8 clubes) + playoff do título (5 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2012 a 2013: pontos corridos (11 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2014 a 2015: pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2016: pontos corridos (13 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2017 a 2018: pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2019: pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2020: pontos corridos (10 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2021: pontos corridos (13 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2022 a 2023: pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota
- 2025: fase de grupos (10 clubes) + rodada preliminar + quartas de final + semifinais + disputa do 3º lugar + final; 4 pontos por vitória, 2 por empate e 1 por derrota
- 2026: pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota

**Fases e grupos de cada edição com mais de uma fase:**

- 1985: Rodada preliminar (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1998: Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1999: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2001: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002: Fase regional (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2002/03: Fase regional (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2003/04: Fase regional (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2004/05: Fase regional (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2006/07: Fase regional (liga); Grupo do rebaixamento (liga); Playoff do título (liga)
- 2007/08: Fase regional (liga); Grupo do rebaixamento (liga); Playoff do título (liga)
- 2008/09: Fase regional (liga); Grupo do rebaixamento (liga); Playoff do título (liga)
- 2010: Fase regional (liga); Playoff do título (liga)
- 2011: Fase regional (liga); Playoff do título (liga)
- 2020: Fase única (liga); Playoff do título (liga)
- 2025: Fase de grupos (liga); Rodada preliminar (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- lista de campeões da RSSSF: 51 edições
- RSSSF: 25 edições

**Observações das edições:**

- 1950: só o campeão na lista da RSSSF
- 1951: só o campeão na lista da RSSSF
- 1952: só o campeão na lista da RSSSF
- 1953: só o campeão na lista da RSSSF
- 1954: só o campeão na lista da RSSSF
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
- 1968: só o campeão na lista da RSSSF
- 1969: só o campeão na lista da RSSSF
- 1970: só o campeão na lista da RSSSF
- 1971: só o campeão na lista da RSSSF
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
- 1986: só o campeão na lista da RSSSF
- 1987: só o campeão na lista da RSSSF
- 1988: só o campeão na lista da RSSSF
- 1989: só o campeão na lista da RSSSF
- 1990: só o campeão na lista da RSSSF
- 1991: só o campeão na lista da RSSSF
- 1992: só o campeão na lista da RSSSF
- 1993: só o campeão na lista da RSSSF
- 1994: só o campeão na lista da RSSSF
- 1995: só o campeão na lista da RSSSF
- 1996: só o campeão na lista da RSSSF
- 1997: a página da RSSSF traz só parte dos jogos do mata-mata
- 2005/06: não houve playoff nacional: o campeão da Grande Terre é o campeão
- 2007/08: no grupo do rebaixamento da Grande Terre os clubes levam um bônus da fase regular
- 2009: não houve playoff nacional: o campeão da Super Ligue (Grande Terre) é o campeão (o calendário passou a ser o ano civil)
- 2025: a liga voltou em maio de 2025, depois de um ano parada pelos distúrbios civis, num formato adaptado (grupos e mata-mata)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- AS Magenta: 16
- JS Baco: 8
- Impassible: 5
- Gaïtcha FC: 4
- AS Mont-Dore: 4
- PLGC: 3
- AS Kunié: 3
- AS Frégate: 3
- CA Saint-Louis: 3
- Wé-Luécilla: 3
- Hienghène Sport: 3
- AS Tiga Sport: 3
- SS Indépendante: 2
- Club Sportif Militaire: 2
- JS Vallée du Tir: 2
- USL Gélima: 2
- USC Nouméa: 1
- Stade Français de Tadine: 1
- Saint Jean-Baptiste Nathalo: 1
- Groupement Sportif Ouvéa: 1
- UAC Yaté: 1
- Kehdek de Koumac: 1
- RS Koumac: 1
- AS 6e km: 1
- JS Traput: 1
- AS Poum: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1950 | Impassible | — |
| 1951 | Impassible | — |
| 1952 | SS Indépendante | — |
| 1953 | Impassible | — |
| 1954 | SS Indépendante | — |
| 1956 | Impassible | — |
| 1957 | PLGC | — |
| 1958 | PLGC | — |
| 1959 | PLGC | — |
| 1960 | Impassible | — |
| 1961 | AS Kunié | — |
| 1962 | USC Nouméa | — |
| 1963 | Club Sportif Militaire | UAC Yaté |
| 1964 | Club Sportif Militaire | Essor de Canala |
| 1965 | AS Frégate | — |
| 1966 | AS Frégate | — |
| 1967 | JS Vallée du Tir | UAC Yaté |
| 1968 | JS Vallée du Tir | — |
| 1969 | AS Magenta | — |
| 1970 | AS Magenta | — |
| 1971 | Stade Français de Tadine | JS Vallée du Tir |
| 1972 | Saint Jean-Baptiste Nathalo | — |
| 1973 | Groupement Sportif Ouvéa | — |
| 1974 | Gaïtcha FC | — |
| 1975 | UAC Yaté | Croix Bleue |
| 1976 | AS Magenta | — |
| 1977 | Kehdek de Koumac | AS Magenta |
| 1978 | USL Gélima | JS Maré |
| 1979 | JS Baco | — |
| 1980 | RS Koumac | — |
| 1981 | USL Gélima | — |
| 1982 | JS Baco | — |
| 1983 | CA Saint-Louis | — |
| 1984 | AS Frégate | AS Païta |
| 1985 | AS Kunié | CA Saint-Louis |
| 1986 | AS 6e km | — |
| 1987 | CA Saint-Louis | — |
| 1988 | CA Saint-Louis | — |
| 1989 | Wé-Luécilla | Entente Gélima |
| 1990 | Gaïtcha FC | — |
| 1991 | Wé-Luécilla | AS Kunié |
| 1992 | AS Kunié | — |
| 1993 | Wé-Luécilla | AS Magenta |
| 1994 | JS Baco | AS Magenta |
| 1995 | JS Baco | JS Traput |
| 1996 | JS Traput | JS Baco |
| 1997 | JS Baco | CA Saint-Louis |
| 1998 | AS Poum | JS Traput |
| 1999 | Gaïtcha FC | AS Auteuil |
| 2000 | JS Baco | JS Traput |
| 2001 | JS Baco | AS Mont-Dore |
| 2002 | AS Mont-Dore | JS Baco |
| 2002/03 | AS Magenta | JS Baco |
| 2003/04 | AS Magenta | AS Mont-Dore |
| 2004/05 | AS Magenta | AS Mont-Dore |
| 2005/06 | AS Mont-Dore | JS Baco |
| 2006/07 | JS Baco | AS Lössi |
| 2007/08 | AS Magenta | AS Mont-Dore |
| 2008/09 | AS Magenta | AS Mont-Dore |
| 2009 | AS Magenta | Hienghène Sport |
| 2010 | AS Mont-Dore | AS Magenta |
| 2011 | AS Mont-Dore | Thio Sport |
| 2012 | AS Magenta | Hienghène Sport |
| 2013 | Gaïtcha FC | Hienghène Sport |
| 2014 | AS Magenta | AS Lössi |
| 2015 | AS Magenta | Hienghène Sport |
| 2016 | AS Magenta | AS Lössi |
| 2017 | Hienghène Sport | AS Magenta |
| 2018 | AS Magenta | Hienghène Sport |
| 2019 | Hienghène Sport | AS Magenta |
| 2020 | AS Tiga Sport | AS Horizon Patho |
| 2021 | Hienghène Sport | SC Ne Drehu |
| 2022 | AS Tiga Sport | Hienghène Sport |
| 2023 | AS Magenta | ASC Gaïca |
| 2025 | AS Tiga Sport | ASC Gaïca |
| 2026 | AS Magenta | AS Tiga Sport |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 2002: CS Nékoué -1
- 2002/03: ACB Poya -9
- 2002/03: JS Tiéta -9
- 2002/03: FC Koh -10
- 2003/04: AS Magenta +9
- 2004/05: Gaïtcha FC -1
- 2005/06: Stade Koniambo -1
- 2007/08: AS Mont-Dore -1
- 2007/08: AS Lössi +19
- 2007/08: Thio Sport +7
- 2007/08: AS Témala-Ouélisse +10
- 2007/08: ACB Poya +4
- 2008/09: AS Kirikitr -6
- 2008/09: Hienghène Sport +25
- 2008/09: Thio Sport +20
- 2008/09: AS Mouli +10
- 2008/09: JS Baco +12
- 2008/09: AS Témala-Ouélisse -1
- 2011: AS Magenta -2
- 2012: AS Qanono -1
- 2012: AS Kunié -1
- 2012: AS Mouli -1
- 2013: Gaïtcha FC -6
- 2013: Hienghène Sport -9
- 2013: AS Lössi -5
- 2013: Thio Sport -17
- 2013: SC Ne Drehu -4
- 2013: AS Qanono -7
- 2013: AS Tiga Sport -5
- 2013: AS Grand Nord -13
- 2014: Hienghène Sport -10
- 2014: AS Wetr -2
- 2014: Gaïtcha FC -9
- 2014: AS Tiga Sport -1
- 2014: Thio Sport -10
- 2014: AGJP -12
- 2015: FC Bélep -1
- 2015: JS Baco -1
- 2015: FC Auteuil -3
- 2016: AS Horizon Patho -10
- 2016: AS Tiga Sport -1
- 2016: FC Bélep -3
- 2016: RC Poindimié -2
- 2016: Gaïtcha FC -12
- 2016: AS Kunié -1
- 2017: Hienghène Sport -4
- 2017: AS Lössi -3
- 2017: AS Mont-Dore -1
- 2017: AS Tiga Sport -6
- 2017: AS Horizon Patho -5
- 2017: AS Wetr -3
- 2017: AGJP -7
- 2017: RC Poindimié -4
- 2017: FC Bélep -9
- 2017: JS Baco -8
- 2018: Hienghène Sport -4
- 2018: AS Tiga Sport -6
- 2018: AS Lössi -6
- 2018: Trio Kedeigne -6
- 2018: AS Wetr -6
- 2018: AS Horizon Patho -9
- 2018: Thio Sport -6
- 2018: RC Poindimié -9
- 2018: AGJP -7
- 2020: AS Mont-Dore -1
- 2022: AS Horizon Patho +2
- 2023: AS Horizon Patho -2
- 2026: AS Horizon Patho -5

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ncl-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 3)

- **newcal03 · 194:** ({'gv': 9}, 'a página traz Olympique 1-0 AS Magenta, mas a tabela da mesma página dá vitória do Magenta e 9 gols a mais para ele (e sofridos pelo Olympique): só este jogo explica (o outro entre os dois foi 3-0 para o Magenta); placar provável 1-9')
- **newcal08 · 49:** ({'especial': 'wo_v', 'gm': 1, 'gv': 1, 'gols_contam': True}, 'vitória dada ao Kirikitr (o Mont-Dore escalou jogador suspenso); em campo, 1-1, e a tabela conta esses gols')
- **newcal2011 · 139:** ({'especial': 'wo_m', 'gm': 0, 'gv': 4}, 'vitória dada ao Hienghène sem gols ("awarded 0-0 win"); em campo, 0-4')

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **newcal09 · 68:** tabela do playoff com os resultados de campo (antes da decisão da comissão que deu o jogo ao Lössi)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 4)

- **2004/05:** Grande Terre: dois jogos só com o vencedor na página (ACB Poya "bt" ASLN Kouaoua, AS Poum "bt" CA Saint-Louis), que ficam de fora; falta também um jogo USC Nouméa x ASLN Kouaoua (3-2 pela tabela) e o JS Baco tem um gol a mais a favor e contra; a classificação é a tabela da página
- **2013:** AS Lössi x AS Mont-Dore só com "drw" (empate sem placar) na página: fica de fora; a tabela conta o empate
- **2015:** jogos sem placar na página (Gaïtcha "drw" Lössi; Auteuil "lt" Baco, "by 1 goal") ficam de fora; a tabela é a de antes das punições do fim da temporada e conta o 2-2 de campo de Lössi x Gaïtcha (dado 3-0 ao Lössi); a classificação é essa tabela
- **2018:** um gol de diferença: o Trio Kedeigne tem um gol a mais a favor e o SC Ne Drehu um a mais contra na tabela do que nos jogos entre os dois (1-3 e 5-1); não dá para saber em qual; fica o placar da página

### Identidade dos clubes

Regras em `coleta/ncl-1/clubes_ncl.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da Nova Caledônia (ncl-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 24/11/2026 (pesquisa em docs/coleta/ncl-1.md):
- AS Le Nickel (1969, 1970, 1976) = AS Magenta (mesmo clube com outro nome: Wikipédia fr/en e lista de fundações da RSSSF;
  a lista de campeões da RSSSF conta os dois separados);
- Gaïtcha FCN = FC Gaïtcha = "Gaïtcha FC" (RSSSF: "includes Gaïtcha FCN"); o ASC Gaïca (Lifou, 2023 em diante) é outro clube;
- "Île des Pins" (1961) = AS Kunié (o clube da ilha; Kunié é o nome kanak); "AS Baco" (3º em 1991) = JS Baco;
- Entente Gélima (1989) é outro clube que a USL Gélima (Canala); Wé-Luécilla (Lifou) como a RSSSF escreve;
- nomes oficiais ou de uso corrente: "AS Tiga Sport" (a RSSSF escreve "Tiga Sports"), "USC Nouméa", "SS Indépendante";
- AS Auteuil (até 2005) e FC Auteuil (2014-2015) ficam separados (nenhuma fonte liga os dois).

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
```

## 8. O que não deu para coletar

- **Edições sem jogos** (40): 1950, 1951, 1952, 1953, 1954, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1965, 1966, 1967, 1968, 1969, 1970, 1972, 1973, 1974, 1975, 1976, 1979, 1980, 1981, 1982, 1983, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996.
- **Décadas com menos da metade dos gols com autor:** 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1950-1983 e 1986-1996 só com o campeão (a final em 1964, 1971, 1977 e 1978; vice e 3º em parte dos anos).
- 1963 e 1964: Club Sportif Militaire pela RSSSF atual; a versão antiga (USC, JS Vallée du Tir), copiada pela Wikipédia e pelo ogol, fica registrada. Um jornal da época (La France Australe) resolveria de vez.
- Identidades com evidência parcial: Entente Gélima, Wé-Luécilla, AS Auteuil x FC Auteuil (separados).
- Jogos sem placar ("bt", "drw", "lt") em 2004/05, 2013 e 2015; ligas das províncias e torneio das ilhas fora.

## 10. Arquivos e comandos

Código em `coleta/ncl-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga da Nova Caledônia ("Liga Nova Caledônia", competição 756) para data/cache/ogol-ncl-1/ e grava o resumo |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da Nova Caledônia para data/coleta/ncl-1/rsssf/ (lista de campeões, lista de finais da copa e |
| `baixar_wikipedia.py` | Baixa o wikitexto da Wikipédia sobre a liga da Nova Caledônia para data/coleta/ncl-1/wikipedia/ (página da liga em inglês e |
| `clubes_ncl.py` | Identidade dos clubes da Nova Caledônia (ncl-1): cada grafia da RSSSF vira um clube, com cidade e província (região). |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão da Nova Caledônia (ncl-1): uma por título, como na lista de campeões da RSSSF (newcalchamp.html), de |
| `explicacoes.py` | Correções e decisões da coleta da Nova Caledônia (ncl-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão da Nova Caledônia e grava o pacote em data/coleta/ncl-1/pacote/ e o relatório em |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/ncl-1/rsssf/), trecho a trecho (edicoes.py), |

- Fontes baixadas: `data/coleta/ncl-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-ncl-1/`.
- Pacote: `data/coleta/ncl-1/pacote/`; relatório: `docs/coleta/ncl-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/ncl-1/baixar_ogol.py
python coleta/ncl-1/baixar_rsssf.py
python coleta/ncl-1/baixar_wikipedia.py
python coleta/ncl-1/importar.py
python coleta/ncl-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py ncl-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

