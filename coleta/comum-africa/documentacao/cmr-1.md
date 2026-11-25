# Campeonato Camaronês (`cmr-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/cmr-1/pacote/`, do código `coleta/cmr-1/` e do relatório `docs/coleta/cmr-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 66, de 1961 a 2026; 37 sem jogos.
- **Jogos:** 6804 (6751 com placar); **gols:** 13633; **gols com autor:** 1138 (8%); **cartões:** 0.
- **Clubes:** 85; **artilheiros:** 2 edições com artilheiro (2 linhas, com empates).
- **Classificação final:** 66 edições; **tabelas publicadas guardadas para conferência:** 675 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão camaronesa (hoje Elite One) de 1961 a 2026, como a lista de campeões da RSSSF, sem o campeonato territorial da era colonial e sem as ligas do Camarões anglófono até 1972. Pontos 2-1-0 (vitória, empate, derrota) até 1987/88 e de 1991 a 1994; 3-1-0 em 1988/89, 1989/90 e desde 1995.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão camaronesa (cmr-1): o campeonato nacional, de 1961 a 2026 (hoje Elite One).

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): como a lista
de campeões da RSSSF (kamchamp.html, "since independence"), com uma edição só para o primeiro campeonato (a lista dá
"1960" e "1961", os dois com o Oryx, mas conta um título só; a página é a mesma, kam61, e a Wikipédia dá 1961). Ficam de
fora o campeonato territorial da era colonial (1936/37 a 1955/56) e as ligas do Camarões anglófono até 1972.

Temporadas como na lista da RSSSF (o rótulo muda: ano civil e duas temporadas se alternam).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela (ou só o topo dela).
- ogol: o calendário do ogol (liga-dos-camaroes), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
```

**Edições:** 66, de 1961 a 2026, como a lista de campeões da RSSSF (`kamchamp.html`, "since independence"), com uma edição só para o primeiro campeonato (a lista dá "1960" e "1961", os dois com o Oryx Douala, mas é um título só). Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fontes:** RSSSF (lista de campeões `kamchamp.html`; páginas por ano: a tabela ou a classificação incompleta de 1978/79 a 1998, os jogos de 1999 em diante); ogol (jogos de 2005 em diante, fora 2013 a 2016: base de 2010/11, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Canon Yaoundé, Tonnerre Yaoundé, Coton Sport...). Mesmo clube com outro nome é um só. Os dois Aigle Royal são clubes diferentes (do Moungo, de Nkongsamba; da Menoua, de Dschang). Regras em `coleta/cmr-1/clubes_cmr.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2010/11). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1987/88 e de 1991 a 1994; 3-1-0 em 1988/89, 1989/90 (a RSSSF anota "3 points for win") e desde 1995.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 22.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 2001, 2014, 2015.
- **Edições sem tabela para conferir** (41): 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1981, 1981/82, 1982/83, 1983/84, 1984/85, 1985/86, 1986/87, 1987/88, 1988/89, 1989/90, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2010/11.
- **Edições com menos jogos que o esperado:** 2001 (239 de 240).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 43 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 9 | 194 | 71% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 11 | 2673 | 95% | 0% | 100% | 0% | 0% | 0% | 21% | 0.0 |
| 2010s | 10 | 2495 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1399 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1961 a 1977/78: 1 clubes
- 1978/79: 2 clubes
- 1979/80: 1 clubes
- 1981: 4 clubes
- 1981/82: 1 clubes
- 1982/83: 16 clubes
- 1983/84: 3 clubes
- 1984/85: 1 clubes
- 1985/86: 16 clubes
- 1986/87: 1 clubes
- 1987/88 a 1989/90: 16 clubes
- 1991: 15 clubes
- 1992: 1 clubes
- 1993 a 1995: 16 clubes
- 1996: 15 clubes
- 1997: 18 clubes
- 1998 a 2003: 16 clubes
- 2004 a 2005: 18 clubes
- 2006: 16 clubes
- 2007: 18 clubes
- 2007/08: 16 clubes
- 2008/09 a 2013: 14 clubes
- 2014: 19 clubes
- 2015 a 2019/20: 18 clubes
- 2020/21: 21 clubes
- 2022: 25 clubes
- 2022/23: 22 clubes
- 2023/24: 19 clubes
- 2024/25: 16 clubes
- 2026: 14 clubes

**Pontos por vitória:**

- 1961 a 1987/88: 2
- 1988/89 a 1989/90: 3
- 1991 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1961 a 2026: Championnat du Cameroun (Elite One)

**Formato** (fases na ordem, do edicoes.csv):

- 1961 a 1977/78: sem jogos (só o campeão)
- 1978/79 a 1981/82: sem jogos (só a classificação incompleta)
- 1982/83: sem jogos (só a tabela final)
- 1983/84: sem jogos (só a classificação incompleta)
- 1984/85: sem jogos (só o campeão)
- 1985/86: sem jogos (só a classificação incompleta)
- 1986/87: sem jogos (só o campeão)
- 1987/88: jogos incompletos (só os resultados que a página traz)
- 1988/89 a 1991: sem jogos (só a tabela final)
- 1992: sem jogos (só o campeão)
- 1993: sem jogos (só a classificação incompleta)
- 1994 a 1995: sem jogos (só a tabela final)
- 1996: sem jogos (só a classificação incompleta)
- 1997 a 1998: sem jogos (só a tabela final)
- 1999: jogos incompletos (muitos jogos sem placar na página)
- 2000: jogos incompletos (falta a rodada 21: a página repete a 22 no lugar dela)
- 2001 a 2003: pontos corridos
- 2004: 2 grupos + grupos do título e do rebaixamento
- 2005 a 2009/10: pontos corridos
- 2010/11: jogos incompletos (sem os jogos do Union e do Caïman Douala, que o ogol não separa)
- 2011/12 a 2018: pontos corridos
- 2019: 2 grupos + grupos do título e do rebaixamento
- 2019/20: pontos corridos
- 2020/21 a 2022: 2 grupos + jogos de classificação + desempate + mata-mata
- 2022/23: 2 grupos + desempate + fase final
- 2023/24: 2 grupos + grupos do título e do rebaixamento
- 2024/25 a 2026: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 2004: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 2019: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 2020/21: Primeira fase (grupos, 2 grupos); Jogos de classificação (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022: Primeira fase (grupos, 2 grupos); Jogos de classificação (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022/23: Primeira fase (grupos, 2 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Fase final (liga)
- 2023/24: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 44 edições
- lista de campeões da RSSSF: 21 edições
- calculada com os jogos que a página traz: 1 edições

**Observações das edições:**

- 1961: a RSSSF só traz o campeão (e a lista dos 11 participantes)
- 1962: a RSSSF só traz o campeão
- 1963: a RSSSF só traz o campeão
- 1964: a RSSSF só traz o campeão
- 1965: a RSSSF só traz o campeão
- 1966: a RSSSF só traz o campeão
- 1967: a RSSSF só traz o campeão
- 1968: a RSSSF só traz o campeão
- 1969: a RSSSF só traz o campeão
- 1969/70: a RSSSF só traz o campeão
- 1970/71: a RSSSF só traz o campeão
- 1971/72: a RSSSF só traz o campeão
- 1972/73: a RSSSF só traz o campeão
- 1973/74: a RSSSF só traz o campeão
- 1974/75: a RSSSF só traz o campeão
- 1975/76: a RSSSF só traz o campeão
- 1976/77: a RSSSF só traz o campeão
- 1977/78: a RSSSF só traz o campeão
- 1978/79: a RSSSF só traz a classificação incompleta (só os primeiros colocados)
- 1979/80: a RSSSF só traz a classificação incompleta (só os primeiros colocados)
- 1981: a RSSSF só traz a classificação incompleta (só os primeiros colocados)
- 1981/82: a RSSSF só traz a classificação incompleta (só os primeiros colocados)
- 1982/83: a RSSSF só traz a tabela final
- 1983/84: a RSSSF só traz a classificação incompleta (só os primeiros colocados)
- 1984/85: a RSSSF só traz o campeão
- 1985/86: a RSSSF só traz a classificação incompleta (posição, jogos e pontos)
- 1986/87: a RSSSF só traz o campeão
- 1988/89: a RSSSF só traz a tabela final
- 1989/90: a RSSSF só traz a tabela final
- 1991: a RSSSF só traz a tabela final
- 1992: a RSSSF só traz o campeão
- 1993: a RSSSF só traz a classificação incompleta (posição, jogos e pontos)
- 1994: a RSSSF só traz a tabela final
- 1995: a RSSSF só traz a tabela final
- 1996: a RSSSF só traz a classificação incompleta (posição, jogos e pontos)
- 1997: a RSSSF só traz a tabela final
- 1998: a RSSSF só traz a tabela final
- 2019/20: abandonado em 12/05/2020 (pandemia de Covid-19); o PWD Bamenda foi declarado campeão, sem rebaixamento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Coton Sport: 18
- Canon Yaoundé: 10
- Oryx Douala: 5
- Union Douala: 5
- Tonnerre Yaoundé: 5
- Racing Bafoussam: 4
- Caïman Douala: 3
- Aigle Royal du Moungo: 2
- Léopard Douala: 2
- UMS de Loum: 2
- Colombe Sportive: 2
- Diamant Yaoundé: 1
- Unisport du Haut-Nkam: 1
- Sable Batié: 1
- Fovu Baham: 1
- Tiko United: 1
- Eding Sport: 1
- PWD Bamenda: 1
- Victoria United: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1961 | Oryx Douala | — |
| 1962 | Caïman Douala | — |
| 1963 | Oryx Douala | — |
| 1964 | Oryx Douala | — |
| 1965 | Oryx Douala | — |
| 1966 | Diamant Yaoundé | — |
| 1967 | Oryx Douala | — |
| 1968 | Caïman Douala | — |
| 1969 | Union Douala | — |
| 1969/70 | Canon Yaoundé | — |
| 1970/71 | Aigle Royal du Moungo | — |
| 1971/72 | Léopard Douala | — |
| 1972/73 | Léopard Douala | — |
| 1973/74 | Canon Yaoundé | — |
| 1974/75 | Caïman Douala | — |
| 1975/76 | Union Douala | — |
| 1976/77 | Canon Yaoundé | — |
| 1977/78 | Union Douala | — |
| 1978/79 | Canon Yaoundé | Dynamo Douala |
| 1979/80 | Canon Yaoundé | — |
| 1981 | Tonnerre Yaoundé | Dynamo Douala |
| 1981/82 | Canon Yaoundé | — |
| 1982/83 | Tonnerre Yaoundé | Etoile Filante Garoua |
| 1983/84 | Tonnerre Yaoundé | Canon Yaoundé |
| 1984/85 | Canon Yaoundé | — |
| 1985/86 | Canon Yaoundé | Union Douala |
| 1986/87 | Tonnerre Yaoundé | — |
| 1987/88 | Tonnerre Yaoundé | Union Douala |
| 1988/89 | Racing Bafoussam | Tonnerre Yaoundé |
| 1989/90 | Union Douala | Prévoyance Yaoundé |
| 1991 | Canon Yaoundé | Diamant Yaoundé |
| 1992 | Racing Bafoussam | — |
| 1993 | Racing Bafoussam | Unisport du Haut-Nkam |
| 1994 | Aigle Royal du Moungo | Coton Sport |
| 1995 | Racing Bafoussam | Léopard Douala |
| 1996 | Unisport du Haut-Nkam | Coton Sport |
| 1997 | Coton Sport | Stade Bandjoun |
| 1998 | Coton Sport | Canon Yaoundé |
| 1999 | Sable Batié | Coton Sport |
| 2000 | Fovu Baham | Coton Sport |
| 2001 | Coton Sport | Tonnerre Yaoundé |
| 2002 | Canon Yaoundé | Coton Sport |
| 2003 | Coton Sport | Canon Yaoundé |
| 2004 | Coton Sport | Racing Bafoussam |
| 2005 | Coton Sport | Aigle Royal de la Menoua |
| 2006 | Coton Sport | Canon Yaoundé |
| 2007 | Coton Sport | Union Douala |
| 2007/08 | Coton Sport | Canon Yaoundé |
| 2008/09 | Tiko United | Union Douala |
| 2009/10 | Coton Sport | Les Astres |
| 2010/11 | Coton Sport | Les Astres |
| 2011/12 | Union Douala | Coton Sport |
| 2013 | Coton Sport | Les Astres |
| 2014 | Coton Sport | Cosmos Bafia |
| 2015 | Coton Sport | Union Douala |
| 2016 | UMS de Loum | Coton Sport |
| 2017 | Eding Sport | Coton Sport |
| 2018 | Coton Sport | UMS de Loum |
| 2019 | UMS de Loum | Coton Sport |
| 2019/20 | PWD Bamenda | Coton Sport |
| 2020/21 | Coton Sport | APEJES Academy |
| 2022 | Coton Sport | Eding Sport |
| 2022/23 | Coton Sport | Bamboutos Mbouda |
| 2023/24 | Victoria United | Coton Sport |
| 2024/25 | Colombe Sportive | Panthère du Ndé |
| 2026 | Colombe Sportive | Dynamo Douala |

**Rebaixados marcados na classificação:** 107 em 33 edições (só onde a tabela publicada marca a queda); quem mais caiu: Aigle Royal de la Menoua (5), Caïman Douala (5), Tonnerre Yaoundé (4), Dynamo Douala (3), Unisport du Haut-Nkam (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1988/89: PWD Kumba -1
- 1989/90: Unité Douala -1
- 1991: PWD Bamenda +2
- 1994: Canon Yaoundé -2
- 1994: Caïman Douala -2
- 1994: PWD Kumba -4
- 1995: Fogabe Yaoundé -2
- 1998: Racing Bafoussam -7
- 1998: Djerem Bertoua -3
- 1999: Free Boys Bamenda -6
- 2000: Union Douala +4
- 2001: Coton Sport -3
- 2001: Olympic Mvolyé -3
- 2001: Dynamo Douala -3
- 2004: Sable Batié -3
- 2005: Sahel Maroua -2
- 2005: Canon Yaoundé -2
- 2005: Tonnerre Yaoundé -1
- 2006: Impôts FC -1
- 2007: Sable Batié -3
- 2007: Fédéral du Noun -3
- 2007: CPS Bertoua -3
- 2007/08: Inter Lion Ngoma -7
- 2008/09: Mount Cameroon -3
- 2013: YOSA Bamenda -3
- 2014: Coton Sport -3
- 2014: Douala AC -3
- 2015: Coton Sport -3
- 2015: Tonnerre Yaoundé -3
- 2016: Canon Yaoundé -3
- 2020/21: New Star Douala -3
- 2022: New Star Douala -3
- 2022: Tonnerre Yaoundé -3
- 2023/24: YOSA Bamenda -3
- 2024/25: Bamboutos Mbouda -3
- 2024/25: YOSA Bamenda -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/cmr-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **kam95 · 16:** «30 12 12  4» → «30 12 12  6»: Unisport Bafang: 12+12+4 não dá 30 jogos; 48 pontos = 12 vitórias e 12 empates, logo 6 derrotas

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 69)

- **2000 · kam00:238:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:239:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:240:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:241:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:242:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:243:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:244:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2000 · kam00:245:** [descartado] a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- **2005 · kam05:320:** [vale o placar de campo, gm = 1, gv = 2, nota = o 3-0 dado ao Les Astres foi revogado depois] "temporarily awarded 3-0, later revoked": vale o 1-2 de campo (a tabela confirma)
- **2006 · kam06:305:** [oficial = (3, 0), nota = 1-0 em campo, abandonado aos 75' pelo Impôts] "awarded 3-0; 1-0 abd by Impôts at 75'": não é abandono sem valer; a tabela conta o 3-0
- **2007 · kam07:235:** [wo_v, gm = 1, gv = 0] "match finished 1-0 but Canon used suspended coach; win awarded to University": a tabela conta a vitória da University e o 1-0 de campo
- **2007 · kam07:496:** [oficial = (3, 0)] "n/p" com "awarded 3-0" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- **2007 · kam07:510:** [oficial = (0, 3)] "n/p" com "awarded 0-3" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- **2007 · kam07:514:** [oficial = (3, 0)] "n/p" com "awarded 3-0" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- **2007/08 · kam08:249:** [wo_v, gm = 0, gv = 0] "original score (0-0) stood but points awarded to Unisport" (o Caïman escalou jogador suspenso): a tabela conta a vitória do Unisport e o 0-0
- **2009/10 · kam2010:246:** [wo_v, gm = None, gv = None, nota = vitória dada ao Les Astres sem gols; em campo, 1-0 para o Coton Sport (ogol)] vitória dada ao Les Astres sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2009/10 · kam2010:250:** [wo_v, gm = None, gv = None, nota = vitória dada ao Union Douala sem gols; em campo, 2-0 para o Sable Batié (ogol)] vitória dada ao Union Douala sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2009/10 · kam2010:269:** [wo_v, gm = None, gv = None, nota = vitória dada ao Renaissance Ngoumou sem gols; em campo, 2-1 para o Fovu Baham (ogol)] vitória dada ao Renaissance Ngoumou sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2010/11 · ogol:10143305:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143316:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143312:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143326:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143318:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143328:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143329:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143336:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143345:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143339:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143344:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143348:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143351:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143356:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143358:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143357:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143363:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143368:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143376:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143386:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143378:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143382:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143380:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143393:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143387:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143400:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143395:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143410:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143407:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143414:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143419:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143421:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143423:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143427:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143430:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143431:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143437:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143441:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143446:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143456:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143459:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143451:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143466:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143464:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143474:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143471:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2010/11 · ogol:10143473:** [descartado] o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- **2023/24 · kam2024:364:** [wo_v, gm = None, gv = None, nota = vitória dada ao Victoria United sem gols; em campo, 1-0 para o UMS de Loum] vitória dada ao Victoria United sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2023/24 · kam2024:372:** [wo_m, gm = None, gv = None, nota = vitória dada ao APEJES Academy sem gols; em campo, 0-0] vitória dada ao APEJES Academy sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2023/24 · kam2024:376:** [wo_m, gm = None, gv = None, nota = vitória dada ao Victoria United sem gols; em campo, 1-1] vitória dada ao Victoria United sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- **2024/25 · kam2025:333:** [vale o placar de campo, nota = ] jogo válido: a nota "award of 3-0 annulled, match refixtured" continua a do Dynamo Douala x Aigle Royal, da linha de cima

### Divergências entre fontes já explicadas (`EXPLICACOES`, 8)

- **1999:** Jogos incompletos: a página traz muitos jogos sem placar ("-"). A classificação é a tabela da RSSSF, que a Wikipédia confirma.
- **2000:** A página avisa que a tabela não foi conferida com os placares ("Table (not checked with scores)"); a Wikipédia confirma a tabela, que é a classificação. Os placares ficam como a página traz.
- **2000:** Jogos incompletos: a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página.
- **2001:** A página traz duas tabelas: uma montada pelos resultados conhecidos e a oficial da FECAFOOT. A classificação é a oficial (pontos e ordem da federação); a dos resultados conhecidos fica como conferência.
- **2007:** O Bamboutos foi excluído no fim do campeonato (a tabela o põe à parte, sem posição); os jogos que não fez contam como W.O. para os adversários.
- **2014:** Douala AC x Coton Sport: os dois clubes se recusaram a jogar; a federação deu derrota por 0-0 aos dois e tirou 3 pontos de cada ("both clubs refused to play, both had 3 points deducted and the match awarded a 0-0 loss against them"). O jogo fica sem placar; a tabela conta uma derrota para cada um.
- **2020/21:** A liga da LFPC ("Ligue 2020/21") parou na 1ª rodada, em 4/11/2020, quando a FECAFOOT proibiu a LFPC de organizá-la (só Panthère 0-2 Coton Sport foi jogado). A edição é a "Ligue 2021", da FECAFOOT.
- **2010/11:** A RSSSF só traz a tabela final (a classificação); os jogos vêm do ogol, menos os do Union e do Caïman Douala (o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo). Jogos incompletos.

### Identidade dos clubes

Regras em `coleta/cmr-1/clubes_cmr.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes camaroneses: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido, com a cidade quando é o costume ("Canon Yaoundé", "Coton Sport", "Union Douala");
- nome que já existe em outro país leva o país ("Botafogo (Camarões)", "Santos (Camarões)");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Union Douala = Union Sportive de Douala; Tonnerre Yaoundé = Tonnerre Kalara Club; Coton Sport = Cotonsport de
    Garoua; Panthère du Ndé = Panthère de Bangangté; Unisport du Haut-Nkam = Unisport de Bafang; University FC de
    Ngaoundéré = Université de Ngaoundéré; Djiko FC = Feutcheu FC ("Feutcheu FC were renamed Djiko FC"); Olympic
    Mvolyé = Olympic de Mvolyé; PWD Bamenda = PWD Cammark Bamenda;
  - Aigle Royal são dois clubes: o do Moungo (Nkongsamba, campeão de 1970/71 e 1994) e o da Menoua (Dschang); "Aigle"
    sozinho até 2004 é o de Nkongsamba; de 2005 a 2023, o de Dschang (a lista de clubes de 2007/08 confirma).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** o campeonato territorial da era colonial (1936/37 a 1955/56), as ligas do Camarões anglófono (West Cameroon) até 1972, a Copa de Camarões e as outras copas, a Elite Two e os jogos de acesso.
- **Edições sem jogos** (37): 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1981, 1981/82, 1982/83, 1983/84, 1984/85, 1985/86, 1986/87, 1988/89, 1989/90, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998.
- **Décadas com menos da metade dos gols com autor:** 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1961 a 1998: só o campeão (1961 a 1977/78, 1984/85, 1986/87 e 1992), só os primeiros colocados ou só posição, jogos e pontos (1978/79 a 1985/86, 1993 e 1996) ou só a tabela final (os outros anos); 1987/88, 1999 e 2000: parte dos jogos. Fonte que resolveria: jornais camaroneses (Cameroon Tribune) ou o arquivo da FECAFOOT.
- 2010/11: a RSSSF só traz a tabela; os jogos vêm do ogol, que junta o Union e o Caïman Douala num clube só (os jogos dos dois ficam de fora).
- 2001: a classificação é a tabela oficial da FECAFOOT, que não fecha com os jogos (a página traz também a tabela pelos resultados conhecidos).
- Autores dos gols só em 2004 e 2005; artilheiros só desses dois anos; cartões, nenhum. Fonte que resolveria: o ogol jogo a jogo (2005 em diante, fora 2013 a 2016).
- Identidade a conferir: os dois Aigle Royal ("Aigle" sozinho até 2004 = o do Moungo, de Nkongsamba; de 2005 a 2023 = o da Menoua, de Dschang; 2024/25 = o do Moungo); PWD Bamenda x PWD Kumba; Unisport du Haut-Nkam = Unisport de Bafang.

## 10. Arquivos e comandos

Código em `coleta/cmr-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão camaronesa no ogol para data/coleta/cmr-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão camaronesa para data/coleta/cmr-1/rsssf/: a lista de campeões (kamchamp.html) e |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Elite One") e o de cada temporada |
| `clubes_cmr.py` | Identidade dos clubes camaroneses: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão camaronesa (cmr-1): o campeonato nacional, de 1961 a 2026 (hoje Elite One). |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão camaronesa, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão camaronesa e grava o pacote em data/coleta/cmr-1/pacote/ e o relatório em docs/coleta/cmr-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/cmr-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/cmr-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/cmr-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-cmr-1/`.
- Pacote: `data/coleta/cmr-1/pacote/`; relatório: `docs/coleta/cmr-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/cmr-1/baixar_ogol.py
python coleta/cmr-1/baixar_rsssf.py
python coleta/cmr-1/baixar_wikipedia.py
python coleta/cmr-1/importar.py
python coleta/cmr-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py cmr-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

