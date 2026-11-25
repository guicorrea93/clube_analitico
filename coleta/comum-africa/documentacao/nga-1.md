# Campeonato Nigeriano (`nga-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/nga-1/pacote/`, do código `coleta/nga-1/` e do relatório `docs/coleta/nga-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 55, de 1972 a 2025/26; 26 sem jogos.
- **Jogos:** 8906 (8834 com placar); **gols:** 17820; **gols com autor:** 73 (0%); **cartões:** 0.
- **Clubes:** 82; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 54 edições; **tabelas publicadas guardadas para conferência:** 801 linhas.
- **No banco:** sim; **último commit do pacote:** bc5287a6.
- **Observação da competição:** 1ª divisão nigeriana (hoje Nigeria Premier Football League) desde a criação da liga nacional, de 1972 a 2025/26. Sem a Amachree Gold Cup de 1971 (torneio anterior à liga). 2018 e 2019/20 abandonados, sem campeão. Pontos 2-1-0 (vitória, empate, derrota) até 1989; de 1990 a 1994, 3 por vitória, 2 por empate com gols e 1 por empate sem gols; 3-1-0 desde 1995.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão nigeriana (nga-1): a liga nacional, de 1972 a 2025/26 (National League, Professional League em
1990, Premier League em 1993; hoje Nigeria Premier Football League, NPFL).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): desde a
criação da liga, em 1972, como a liga e a imprensa contam (o título de 2025/26 foi o "9º" do Rangers, igual ao Enyimba).
Fica de fora a "Amachree Gold Cup" de 1971 (torneio anterior à liga, que a RSSSF conta), as ligas regionais e as copas.
2018 e 2019/20 foram abandonados e entram sem campeão.

Temporadas como na lista de campeões da RSSSF (nigchamp.html): ano civil até 2007, 2007/08 a 2011/12, ano civil de 2013 a
2019, 2019/20 a 2021/22, 2023 ("Abridged League") e 2023/24 a 2025/26.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página do ano (nig72 = 1970 a 1979; nig88 = 1987 e 1988;
  nig00 ... nig07; nig08 = 2007/08; nig2010 = 2009/10; nig2023 = 2023). Linha inicial 0: logo depois do cabeçalho; linha
  final None: a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a RSSSF só tem a tabela final.
- ogol: o calendário do ogol (liga-nigeriana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
```

**Edições:** 55, de 1972 a 2025/26, como a lista de campeões da RSSSF (`nigchamp.html`), sem a Amachree Gold Cup de 1971 (torneio anterior à liga, que a liga e a imprensa não contam: o título de 2025/26 foi o "9º" do Enugu Rangers). Pesquisa de 24/11/2026, aprovada pelo Guilherme. 2018 e 2019/20 foram abandonados e entram sem campeão.

**Fontes:** RSSSF (páginas por ano, `data/coleta/nga-1/rsssf/`: a tabela final de 1972 e de 1989 a 1997; só o campeão nos outros anos até 1988; jogos de 1998 em diante, parte da temporada até 2003 e em 2007/08); ogol (jogos de 2008/09 em diante, com os mesmos placares da RSSSF: base de 2009/10 a 2011/12, conferência, rodada e data nos outros); Wikipédia em inglês (a tabela de cada temporada desde 2009/10). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Enugu Rangers, Enyimba, Kano Pillars, Shooting Stars...). Mesmo clube com outro nome é um só (Iwuanyanwu Nationale = Heartland; Eagle Cement = Dolphin; Gabros = Ifeanyi Ubah; NPA = Nigerian Ports Authority). Regras em `coleta/nga-1/clubes_nga.py`.

**Regras:** o placar é o da RSSSF (ou do ogol de 2009/10 a 2011/12). A classificação é a tabela publicada (ordem oficial e pontos, com as punições). Pontos 2-1-0 (vitória, empate, derrota) até 1989; de 1990 a 1994, 3 por vitória, 2 por empate com gols e 1 por empate sem gols (o ponto a mais vai no `ajuste_pontos`); 3-1-0 desde 1995.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 13.
- **Edições com alguma tabela divergente** (8; motivo no relatório, na edição): 2009/10, 2010/11, 2011/12, 2019, 2023, 2023/24, 2024/25, 2025/26.
- **Edições sem tabela para conferir** (34): 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2007/08, 2019/20.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970s | 8 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 302 | 92% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 11 | 3082 | 100% | 0% | 100% | 0% | 0% | 0% | 1% | 0.0 |
| 2010s | 10 | 3417 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 2105 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1972: 8 clubes
- 1973 a 1984: 1 clubes
- 1985: 0 clubes
- 1986 a 1988: 1 clubes
- 1989: 14 clubes
- 1990: 1 clubes
- 1991 a 1993: 16 clubes
- 1994: 17 clubes
- 1995: 15 clubes
- 1996 a 1997: 18 clubes
- 1998: 20 clubes
- 1999: 18 clubes
- 2000 a 2001: 17 clubes
- 2002 a 2004: 18 clubes
- 2005 a 2018: 20 clubes
- 2019: 25 clubes
- 2019/20: 22 clubes
- 2020/21 a 2025/26: 20 clubes

**Pontos por vitória:**

- 1972 a 1989: 2
- 1990 a 2025/26: 3

**Nome oficial:**

- 1972 a 1989: Nigeria National League
- 1990 a 1992: Nigerian Professional League
- 1993 a 2011/12: Nigerian Premier League
- 2013 a 2025/26: Nigeria Professional Football League

**Formato** (fases na ordem, do edicoes.csv):

- 1972: sem jogos (só a tabela final)
- 1973 a 1988: sem jogos (só o campeão)
- 1989: sem jogos (só a tabela final)
- 1990: sem jogos (só o campeão)
- 1991 a 1997: sem jogos (só a tabela final)
- 1998 a 2003: jogos incompletos (só os resultados que a página traz)
- 2004 a 2005: pontos corridos
- 2006 a 2007: 2 grupos + fase final
- 2007/08: jogos incompletos (só os resultados que a página traz)
- 2008/09 a 2017: pontos corridos
- 2018: temporada não terminada
- 2019: 2 grupos + fase final
- 2019/20: temporada não terminada (jogos incompletos (só os resultados que a página traz))
- 2020/21 a 2021/22: pontos corridos
- 2023: 2 grupos + fase final
- 2023/24 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1999: Primeira fase (liga); Fase final (liga)
- 2000: Primeira fase (liga); Fase final (liga)
- 2006: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2007: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2019: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2023: Primeira fase (grupos, 2 grupos); Fase final (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 38 edições
- lista de campeões da RSSSF: 16 edições

**Observações das edições:**

- 1972: a RSSSF só traz a tabela final
- 1973: a RSSSF só traz o campeão
- 1974: a RSSSF só traz o campeão
- 1975: a RSSSF só traz o campeão
- 1976: a RSSSF só traz o campeão
- 1977: a RSSSF só traz o campeão
- 1978: a RSSSF só traz o campeão
- 1979: a RSSSF só traz o campeão
- 1980: a RSSSF só traz o campeão (sem página do ano)
- 1981: a RSSSF só traz o campeão (sem página do ano)
- 1982: a RSSSF só traz o campeão (sem página do ano)
- 1983: a RSSSF só traz o campeão
- 1984: a RSSSF só traz o campeão
- 1985: a RSSSF só traz o campeão
- 1986: a RSSSF só traz o campeão
- 1987: a RSSSF só traz o campeão
- 1988: a RSSSF só traz o campeão
- 1989: a RSSSF só traz a tabela final
- 1990: a RSSSF só traz o campeão (e a lista dos participantes)
- 1991: a RSSSF só traz a tabela final
- 1992: a RSSSF só traz a tabela final
- 1993: a RSSSF só traz a tabela final
- 1994: a RSSSF só traz a tabela final
- 1995: a RSSSF só traz a tabela final
- 1996: a RSSSF só traz a tabela final
- 1997: a RSSSF só traz a tabela final
- 2009/10: os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)
- 2010/11: os jogos vêm do calendário do ogol (a RSSSF só traz parte deles)
- 2011/12: os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)
- 2018: temporada abandonada pela crise interna da federação nigeriana ("league abandoned following internal crisis at Nigerian Football Federation"); a tabela é a do abandono
- 2019/20: temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono (pela média de pontos por jogo)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Enugu Rangers: 9
- Enyimba: 9
- Heartland: 5
- Kano Pillars: 4
- Shooting Stars: 3
- Dolphin: 3
- Bendel Insurance: 2
- Julius Berger: 2
- Mighty Jets: 1
- Racca Rovers: 1
- Leventis United: 1
- Stationery Stores: 1
- BCC Lions: 1
- Udoji United: 1
- Lobi Stars: 1
- Ocean Boys: 1
- Bayelsa United: 1
- Plateau United: 1
- Akwa United: 1
- Rivers United: 1
- Remo Stars: 1
- Sem campeão: 1985, 1995, 1998, 2018, 2019/20

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1972 | Mighty Jets | Enugu Rangers |
| 1973 | Bendel Insurance | — |
| 1974 | Enugu Rangers | — |
| 1975 | Enugu Rangers | — |
| 1976 | Shooting Stars | — |
| 1977 | Enugu Rangers | — |
| 1978 | Racca Rovers | — |
| 1979 | Bendel Insurance | — |
| 1980 | Shooting Stars | — |
| 1981 | Enugu Rangers | — |
| 1982 | Enugu Rangers | — |
| 1983 | Shooting Stars | — |
| 1984 | Enugu Rangers | — |
| 1985 | — | — |
| 1986 | Leventis United | — |
| 1987 | Heartland | — |
| 1988 | Heartland | — |
| 1989 | Heartland | JIB Rock Strikers |
| 1990 | Heartland | — |
| 1991 | Julius Berger | Shooting Stars |
| 1992 | Stationery Stores | Shooting Stars |
| 1993 | Heartland | Bendel Insurance |
| 1994 | BCC Lions | Shooting Stars |
| 1995 | — | — |
| 1996 | Udoji United | Jasper United |
| 1997 | Dolphin | Jasper United |
| 1998 | — | — |
| 1999 | Lobi Stars | Heartland |
| 2000 | Julius Berger | Katsina United |
| 2001 | Enyimba | Enugu Rangers |
| 2002 | Enyimba | Enugu Rangers |
| 2003 | Enyimba | Julius Berger |
| 2004 | Dolphin | Enyimba |
| 2005 | Enyimba | Enugu Rangers |
| 2006 | Ocean Boys | Nasarawa United |
| 2007 | Enyimba | Gombe United |
| 2007/08 | Kano Pillars | Heartland |
| 2008/09 | Bayelsa United | Heartland |
| 2009/10 | Enyimba | Kano Pillars |
| 2010/11 | Dolphin | Sunshine Stars |
| 2011/12 | Kano Pillars | Enugu Rangers |
| 2013 | Kano Pillars | Enyimba |
| 2014 | Kano Pillars | Enyimba |
| 2015 | Enyimba | Warri Wolves |
| 2016 | Enugu Rangers | Rivers United |
| 2017 | Plateau United | MFM |
| 2018 | — | — |
| 2019 | Enyimba | Kano Pillars |
| 2019/20 | — | — |
| 2020/21 | Akwa United | Enyimba |
| 2021/22 | Rivers United | Plateau United |
| 2023 | Enyimba | Remo Stars |
| 2023/24 | Enugu Rangers | Remo Stars |
| 2024/25 | Remo Stars | Rivers United |
| 2025/26 | Enugu Rangers | Rivers United |

**Rebaixados marcados na classificação:** 110 em 29 edições (só onde a tabela publicada marca a queda); quem mais caiu: Jigawa Golden Stars (5), El-Kanemi Warriors (5), Sharks (4), Shooting Stars (4), Kwara United (4).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1991: Julius Berger +7
- 1991: Shooting Stars +5
- 1991: Plateau United +3
- 1991: Calabar Rovers +7
- 1991: BCC Lions +7
- 1991: Bendel Insurance +3
- 1991: Enugu Rangers +6
- 1991: ACB +7
- 1991: Bendel United +6
- 1991: Heartland +4
- 1991: Kano Pillars +4
- 1991: Obanta United +6
- 1991: Ranchers Bees +5
- 1991: Stationery Stores +4
- 1991: Enyimba +4
- 1991: Highlanders +2
- 1992: Stationery Stores +9
- 1992: Shooting Stars +4
- 1992: Heartland +2
- 1992: Udoji United +5
- 1992: El-Kanemi Warriors +5
- 1992: Enugu Rangers +1
- 1992: Calabar Rovers +5
- 1992: Julius Berger +4
- 1992: ACB +6
- 1992: BCC Lions +5
- 1992: Bendel Insurance +4
- 1992: Kano Pillars +2
- 1992: Plateau United +7
- 1992: Obanta United +2
- 1992: Bendel United +1
- 1992: Ranchers Bees +4
- 1993: Heartland +2
- 1993: Bendel Insurance +3
- 1993: Concord +6
- 1993: BCC Lions +3
- 1993: Stationery Stores +3
- 1993: Julius Berger +5
- 1993: Enugu Rangers +4
- 1993: Udoji United +3
- 1993: Shooting Stars +2
- 1993: Kano Pillars +3
- 1993: El-Kanemi Warriors +4
- 1993: Plateau United +5
- 1993: VIP +7
- 1993: Calabar Rovers +1
- 1993: ACB +5
- 1994: BCC Lions +5
- 1994: Shooting Stars +6
- 1994: Enyimba +4
- 1994: Julius Berger +7
- 1994: Udoji United +9
- 1994: Concord +5
- 1994: Enugu Rangers +6
- 1994: Plateau United +5
- 1994: VIP +6
- 1994: El-Kanemi Warriors +3
- 1994: Heartland +4
- 1994: Bendel Insurance +3
- 1994: Kano Pillars +4
- 1994: NITEL Vasco +4
- 1994: Ranchers Bees +7
- 2015: Giwa -3
- 2015: Sharks -3
- 2018: MFM -3
- 2018: Sunshine Stars -3
- 2018: Heartland -3
- 2021/22: Kano Pillars -6
- 2023: Bayelsa United -3
- 2023/24: Gombe United -6
- 2024/25: Plateau United -3
- 2025/26: Kano Pillars -3
- 2025/26: Kwara United -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/nga-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 7)

- **nig92 · 29:** «30 7 11 14» → «30 7 11 12»: Bendel United: 7+11+14 não dá 30 jogos; 33 pontos fecham com 7 vitórias e 11 empates, logo 12 derrotas
- **nig94 · 22:** «32  13  12   6» → «32  13  12   7»: Berger: 13+12+6 não dá 32 jogos; 58 pontos fecham com 13 vitórias e 12 empates, logo 7 derrotas
- **nig96 · 24:** «34  15   5  15» → «34  15   5  14»: Nationale: 15+5+15 não dá 34 jogos; 50 pontos fecham com 15 vitórias e 5 empates, logo 14 derrotas
- **nig02 · 25:** «34 14  4 15» → «34 14  4 16»: Lobi Stars: 14+4+15 não dá 34 jogos; 46 pontos fecham com 14 vitórias e 4 empates, logo 16 derrotas
- **nig02 · 453:** «34 14  4 15» → «34 14  4 16»: Lobi Stars (a tabela repetida no fim da temporada): o mesmo erro
- **nig02 · 128:** «Rounds 6-9 missing» → «Rounds 6 to 9 missing»: nota ("rodadas 6 a 9 faltam"), não é jogo
- **nig09 · 646:** «following a 13-0 win» → «following a 13 to 0 win»: nota sobre a temporada anterior, não é jogo

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 10)

- **2005 · nig05:323:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:324:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:325:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:326:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:327:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:329:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:330:** [anulado] a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- **2005 · nig05:448:** [abandonado, nota = abandonado com 1-1 (os oficiais foram ameaçados com uma arma); o 0-2 dado ao Sharks foi revogado e o jogo, repetido em 16/11 (0-4)] o 0-2 dado foi revogado ("later revoked") e o jogo repetido em 16/11
- **2006 · nig06:353:** [oficial = (0, 3), nota = 0-3 dado ao Kano Pillars: o Ranchers Bees não compareceu] "n/p" na página, mas com "awarded 0-3; Ranchers Bees dns": o resultado dado vale
- **2023/24 · nig2024:435:** [vale o placar de campo, nota = ] a nota ("... committee annulled a change of decision ...") é do Enyimba x Doma United, na linha de cima; o jogo vale (as tabelas da RSSSF e da Wikipédia o contam)

### Tabelas da página que não são da edição (`TABELAS_FORA`, 2)

- **2016 · nig2016:43:** campanha do clube expulso até a expulsão ("record at expulsion"), não é tabela da edição
- **2016 · nig2016:636:** campanha do clube expulso até a expulsão (repetida no fim da página)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 10)

- **2009/10:** os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- **2010/11:** os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- **2011/12:** os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- **2005:** a rodada 20 de julho foi anulada e jogada de novo em novembro; Gateway x Sharks de setembro (0-2 dado e depois revogado) foi repetido em novembro
- **2019:** o Delta Force tem só 11 dos 22 jogos na página; a classificação é a tabela publicada
- **2019/20:** temporada abandonada (Covid-19); a página só traz parte dos jogos; no meio da temporada o Delta Force vendeu a vaga ao Akwa Starlets
- **2023:** Bayelsa United com 3 gols a mais nos jogos que na tabela (a Wikipédia confirma a tabela); nenhum placar mudado
- **2023/24:** Gombe United: punição de 3 pontos e 3 gols ("3 points and 3 goals deducted"): a tabela desconta os gols, os jogos não; a classificação é a tabela publicada (duas vezes)
- **2024/25:** Plateau United com 3 gols a mais nos jogos que na tabela (provável punição como as de 2023/24 e 2025/26)
- **2025/26:** Kano Pillars e Kwara United: punição de 3 pontos e 3 gols ("3 points and 3 goals deducted"): a tabela desconta os gols, os jogos não; a classificação é a tabela publicada

### Identidade dos clubes

Regras em `coleta/nga-1/clubes_nga.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes nigerianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Enugu Rangers", "Enyimba", "Kano Pillars", "Shooting Stars");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Enugu Rangers = Rangers = Rangers International; Heartland = Iwuanyanwu Nationale (a RSSSF: "now called Heartland FC");
    Dolphin = Eagle Cement (a RSSSF conta os títulos juntos); Shooting Stars = IICC = 3SC; Nigerian Ports Authority =
    NPA = Port Authority; NITEL Vasco = P&T Vasco da Gama (os Correios e Telégrafos viraram NITEL em 1985);
  - ABS (Ilorin) = Bukola Babes (o ogol já dá ABS FC em 2010/11);
  - Ifeanyi Ubah = Gabros International (comprado e renomeado em 2015; em 2015 a página ainda usa "Gabros United");
  - o Rivers United (fusão do Dolphin com o Sharks em 2016) é um clube próprio, como a RSSSF conta.
- "Kwara" sozinho é o Kwara United, fora 1998 a 2000, quando o Kwara Stars também jogava (ver as edições).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a Federation Cup e as outras copas, as ligas regionais, a 2ª divisão e os jogos de acesso.
- **Edições sem jogos** (26): 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1972 a 1997: só a tabela final (1972, 1989, 1991 a 1997) ou só o campeão (1973 a 1988 e 1990); faltam as páginas de 1980 a 1982. 1998 a 2003, 2007/08 e 2019/20: só parte dos jogos. Fonte que resolveria: jornais nigerianos (Daily Times, The Guardian, Complete Sports) ou o arquivo da NPFL.
- 2009/10 a 2011/12: os jogos do ogol não fecham com a tabela da RSSSF em vários clubes (placar de campo de jogos decididos de outro jeito?); nenhum placar mudado.
- Rebaixamento marcado só onde a página diz (tabela ou nota); nos anos 1970 e 1980, sem informação.
- Autores dos gols quase nenhum; artilheiros, nenhum. Fonte que resolveria: o ogol jogo a jogo (2008/09 em diante).
- Identidade a conferir: Heartland = Iwuanyanwu Nationale; Dolphin = Eagle Cement; Ifeanyi Ubah = Gabros International; ABS = Bukola Babes; NITEL Vasco = P&T Vasco da Gama; o "Akwa Star..." do ogol de 2011/12 = Akwa United.

## 10. Arquivos e comandos

Código em `coleta/nga-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão nigeriana no ogol para data/coleta/nga-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão nigeriana para data/coleta/nga-1/rsssf/: a lista de campeões (nigchamp.html) e |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Nigeria Premier Football League") e o de cada |
| `clubes_nga.py` | Identidade dos clubes nigerianos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão nigeriana (nga-1): a liga nacional, de 1972 a 2025/26 (National League, Professional League em |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão nigeriana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão nigeriana e grava o pacote em data/coleta/nga-1/pacote/ e o relatório em docs/coleta/nga-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/nga-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/nga-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/nga-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-nga-1/`.
- Pacote: `data/coleta/nga-1/pacote/`; relatório: `docs/coleta/nga-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/nga-1/baixar_ogol.py
python coleta/nga-1/baixar_rsssf.py
python coleta/nga-1/baixar_wikipedia.py
python coleta/nga-1/importar.py
python coleta/nga-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py nga-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

