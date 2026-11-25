# Campeonato Camaronês (1ª divisão) — coleta de dados

Gerado por `python coleta/cmr-1/importar.py`. Pacote em `data/coleta/cmr-1/pacote/`.

**Edições:** 66, de 1961 a 2026, como a lista de campeões da RSSSF (`kamchamp.html`, "since independence"), com uma edição só para o primeiro campeonato (a lista dá "1960" e "1961", os dois com o Oryx Douala, mas é um título só). Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fora do pacote:** o campeonato territorial da era colonial (1936/37 a 1955/56), as ligas do Camarões anglófono (West Cameroon) até 1972, a Copa de Camarões e as outras copas, a Elite Two e os jogos de acesso.

**Fontes:** RSSSF (lista de campeões `kamchamp.html`; páginas por ano: a tabela ou a classificação incompleta de 1978/79 a 1998, os jogos de 1999 em diante); ogol (jogos de 2005 em diante, fora 2013 a 2016: base de 2010/11, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Canon Yaoundé, Tonnerre Yaoundé, Coton Sport...). Mesmo clube com outro nome é um só. Os dois Aigle Royal são clubes diferentes (do Moungo, de Nkongsamba; da Menoua, de Dschang). Regras em `coleta/cmr-1/clubes_cmr.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2010/11). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1987/88 e de 1991 a 1994; 3-1-0 em 1988/89, 1989/90 (a RSSSF anota "3 points for win") e desde 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1961 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Oryx Douala | sem jogos (só o campeão) |
| 1962 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Caïman Douala | sem jogos (só o campeão) |
| 1963 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Oryx Douala | sem jogos (só o campeão) |
| 1964 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Oryx Douala | sem jogos (só o campeão) |
| 1965 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Oryx Douala | sem jogos (só o campeão) |
| 1966 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Diamant Yaoundé | sem jogos (só o campeão) |
| 1967 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Oryx Douala | sem jogos (só o campeão) |
| 1968 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Caïman Douala | sem jogos (só o campeão) |
| 1969 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Union Douala | sem jogos (só o campeão) |
| 1969/70 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só o campeão) |
| 1970/71 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Aigle Royal du Moungo | sem jogos (só o campeão) |
| 1971/72 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Léopard Douala | sem jogos (só o campeão) |
| 1972/73 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Léopard Douala | sem jogos (só o campeão) |
| 1973/74 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só o campeão) |
| 1974/75 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Caïman Douala | sem jogos (só o campeão) |
| 1975/76 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Union Douala | sem jogos (só o campeão) |
| 1976/77 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só o campeão) |
| 1977/78 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Union Douala | sem jogos (só o campeão) |
| 1978/79 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só a classificação incompleta) |
| 1979/80 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só a classificação incompleta) |
| 1981 | 4 | 0 (0) | 0 | 0 | 0 / 0 | Tonnerre Yaoundé | sem jogos (só a classificação incompleta) |
| 1981/82 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só a classificação incompleta) |
| 1982/83 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Tonnerre Yaoundé | sem jogos (só a tabela final) |
| 1983/84 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Tonnerre Yaoundé | sem jogos (só a classificação incompleta) |
| 1984/85 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só o campeão) |
| 1985/86 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só a classificação incompleta) |
| 1986/87 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Tonnerre Yaoundé | sem jogos (só o campeão) |
| 1987/88 | 16 | 43 (43) | 64 | 0 | 0 / 0 | Tonnerre Yaoundé | jogos incompletos (só os resultados que a página traz) |
| 1988/89 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Racing Bafoussam | sem jogos (só a tabela final) |
| 1989/90 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Union Douala | sem jogos (só a tabela final) |
| 1991 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Canon Yaoundé | sem jogos (só a tabela final) |
| 1992 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racing Bafoussam | sem jogos (só o campeão) |
| 1993 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Racing Bafoussam | sem jogos (só a classificação incompleta) |
| 1994 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Aigle Royal du Moungo | sem jogos (só a tabela final) |
| 1995 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Racing Bafoussam | sem jogos (só a tabela final) |
| 1996 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Unisport du Haut-Nkam | sem jogos (só a classificação incompleta) |
| 1997 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Coton Sport | sem jogos (só a tabela final) |
| 1998 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Coton Sport | sem jogos (só a tabela final) |
| 1999 | 16 | 194 (194) | 389 | 0 | 0 / 0 | Sable Batié | jogos incompletos (muitos jogos sem placar na página) |
| 2000 | 16 | 230 (230) | 480 | 0 | 0 / 0 | Fovu Baham | jogos incompletos (falta a rodada 21: a página repete a 22 no lugar dela) |
| 2001 | 16 | 239 (240) | 482 | 0 | 0 / 2 | Coton Sport | pontos corridos |
| 2002 | 16 | 243 (243) | 445 | 0 | 1 / 0 | Canon Yaoundé | pontos corridos |
| 2003 | 16 | 240 (240) | 464 | 0 | 1 / 0 | Coton Sport | pontos corridos |
| 2004 | 18 | 260 (260) | 538 | 528 | 4 / 0 | Coton Sport | 2 grupos + grupos do título e do rebaixamento |
| 2005 | 18 | 308 (308) | 630 | 602 | 1 / 0 | Coton Sport | pontos corridos |
| 2006 | 16 | 241 (241) | 476 | 0 | 1 / 0 | Coton Sport | pontos corridos |
| 2007 | 18 | 306 (306) | 605 | 1 | 1 / 0 | Coton Sport | pontos corridos |
| 2007/08 | 16 | 241 (241) | 415 | 0 | 1 / 0 | Coton Sport | pontos corridos |
| 2008/09 | 14 | 182 (182) | 376 | 0 | 1 / 0 | Tiko United | pontos corridos |
| 2009/10 | 14 | 183 (183) | 381 | 0 | 1 / 0 | Coton Sport | pontos corridos |
| 2010/11 | 14 | 125 (125) | 252 | 0 | 0 / 0 | Coton Sport | jogos incompletos (sem os jogos do Union e do Caïman Douala, que o ogol não separa) |
| 2011/12 | 14 | 182 (182) | 372 | 0 | 1 / 0 | Union Douala | pontos corridos |
| 2013 | 14 | 182 (182) | 345 | 1 | 1 / 0 | Coton Sport | pontos corridos |
| 2014 | 19 | 342 (342) | 685 | 0 | 0 / 1 | Coton Sport | pontos corridos |
| 2015 | 18 | 309 (309) | 560 | 0 | 0 / 1 | Coton Sport | pontos corridos |
| 2016 | 18 | 307 (307) | 560 | 0 | 1 / 0 | UMS de Loum | pontos corridos |
| 2017 | 18 | 307 (307) | 555 | 0 | 1 / 0 | Eding Sport | pontos corridos |
| 2018 | 18 | 306 (306) | 575 | 0 | 1 / 0 | Coton Sport | pontos corridos |
| 2019 | 18 | 174 (174) | 320 | 0 | 4 / 0 | UMS de Loum | 2 grupos + grupos do título e do rebaixamento |
| 2019/20 | 18 | 261 (261) | 523 | 0 | 1 / 0 | PWD Bamenda | pontos corridos |
| 2020/21 | 21 | 207 (207) | 441 | 4 | 2 / 0 | Coton Sport | 2 grupos + jogos de classificação + desempate + mata-mata |
| 2022 | 25 | 293 (293) | 694 | 2 | 2 / 0 | Coton Sport | 2 grupos + jogos de classificação + desempate + mata-mata |
| 2022/23 | 22 | 227 (227) | 484 | 0 | 3 / 0 | Coton Sport | 2 grupos + desempate + fase final |
| 2023/24 | 19 | 246 (246) | 517 | 0 | 4 / 0 | Victoria United | 2 grupos + grupos do título e do rebaixamento |
| 2024/25 | 16 | 244 (244) | 534 | 0 | 1 / 0 | Colombe Sportive | pontos corridos |
| 2026 | 14 | 182 (182) | 471 | 0 | 1 / 0 | Colombe Sportive | pontos corridos |

## Conferência e correções, edição a edição

### 1961

- a RSSSF só traz o campeão (e a lista dos 11 participantes)

### 1962

- a RSSSF só traz o campeão

### 1963

- a RSSSF só traz o campeão

### 1964

- a RSSSF só traz o campeão

### 1965

- a RSSSF só traz o campeão

### 1966

- a RSSSF só traz o campeão

### 1967

- a RSSSF só traz o campeão

### 1968

- a RSSSF só traz o campeão

### 1969

- a RSSSF só traz o campeão

### 1969/70

- a RSSSF só traz o campeão

### 1970/71

- a RSSSF só traz o campeão

### 1971/72

- a RSSSF só traz o campeão

### 1972/73

- a RSSSF só traz o campeão

### 1973/74

- a RSSSF só traz o campeão

### 1974/75

- a RSSSF só traz o campeão

### 1975/76

- a RSSSF só traz o campeão

### 1976/77

- a RSSSF só traz o campeão

### 1977/78

- a RSSSF só traz o campeão

### 1978/79

- a RSSSF só traz a classificação incompleta (só os primeiros colocados)

### 1979/80

- a RSSSF só traz a classificação incompleta (só os primeiros colocados)

### 1981

- a RSSSF só traz a classificação incompleta (só os primeiros colocados)

### 1981/82

- a RSSSF só traz a classificação incompleta (só os primeiros colocados)

### 1982/83

- a RSSSF só traz a tabela final

### 1983/84

- a RSSSF só traz a classificação incompleta (só os primeiros colocados)

### 1984/85

- a RSSSF só traz o campeão

### 1985/86

- a RSSSF só traz a classificação incompleta (posição, jogos e pontos)

### 1986/87

- a RSSSF só traz o campeão

### 1987/88

- jogos incompletos (só os resultados que a página traz)

### 1988/89

- a RSSSF só traz a tabela final

### 1989/90

- a RSSSF só traz a tabela final

### 1991

- a RSSSF só traz a tabela final

### 1992

- a RSSSF só traz o campeão

### 1993

- a RSSSF só traz a classificação incompleta (posição, jogos e pontos)

### 1994

- a RSSSF só traz a tabela final

### 1995

- a RSSSF só traz a tabela final

### 1996

- a RSSSF só traz a classificação incompleta (posição, jogos e pontos)

### 1997

- a RSSSF só traz a tabela final

### 1998

- a RSSSF só traz a tabela final

### 1999

- Jogos incompletos: a página traz muitos jogos sem placar ("-"). A classificação é a tabela da RSSSF, que a Wikipédia confirma.
- jogos incompletos (muitos jogos sem placar na página)
- abandonado/suspenso, sem valer — Free Boys Bamenda Panthère du Ndé (1999-03-10): heavy rain
- abandonado/suspenso, sem valer — Panthère du Ndé Union Douala (1999-06-16)
- abandonado/suspenso, sem valer — Dynamo Douala Aigle Royal du Moungo (1999-06-28)
- W.O./pontos para o mandante — Coton Sport Free Boys Bamenda (1999-06-28): ?]  [bt
- W.O./pontos para o mandante — Coton Sport Racing Bafoussam (1999-08-18): bt

### 2000

- A página avisa que a tabela não foi conferida com os placares ("Table (not checked with scores)"); a Wikipédia confirma a tabela, que é a classificação. Os placares ficam como a página traz.
- Jogos incompletos: a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página.
- jogos incompletos (falta a rodada 21: a página repete a 22 no lugar dela)
- corrigido — Sable Batié x Espérance Guider (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Fovu Baham x Caïman Douala (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Girondins Ngaoundéré x Stade Bandjoun (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Olympic Mvolyé x Kumbo Strikers (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Union Douala x Tonnerre Yaoundé (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Cintra Yaoundé x Panthère du Ndé (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Coton Sport x Port FC Douala (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- corrigido — Racing Bafoussam x Canon Yaoundé (None): a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página
- abandonado/suspenso, sem valer — Espérance Guider Union Douala (s/d): abd in '45 due to rain

### 2001

- A página traz duas tabelas: uma montada pelos resultados conhecidos e a oficial da FECAFOOT. A classificação é a oficial (pontos e ordem da federação); a dos resultados conhecidos fica como conferência.
- tabela publicada x jogos — kam01:16: Coton Sport tabela [30, 19, 4, 7, 46, 19] jogos [29, 18, 4, 7, 43, 19] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Tonnerre Yaoundé tabela [30, 15, 8, 7, 43, 23] jogos [30, 15, 8, 7, 43, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Mount Cameroon tabela [29, 13, 5, 11, 34, 31] jogos [28, 12, 5, 11, 31, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Union Douala tabela [30, 10, 10, 10, 30, 29] jogos [30, 9, 10, 11, 29, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Kumbo Strikers tabela [30, 10, 9, 11, 20, 19] jogos [29, 10, 9, 10, 20, 16] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Espérance Guider tabela [30, 10, 7, 13, 32, 38] jogos [30, 10, 7, 13, 32, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Olympic Mvolyé tabela [30, 6, 11, 13, 34, 41] jogos [29, 6, 10, 13, 34, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Dynamo Douala tabela [29, 8, 5, 16, 25, 30] jogos [28, 9, 5, 14, 25, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:16: Girondins Ngaoundéré tabela [29, 2, 12, 15, 17, 39] jogos [28, 2, 11, 15, 17, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam01:44: Coton Sport tabela [30, 19, 4, 7, 41, 17] jogos [29, 18, 4, 7, 43, 19] — a Wikipédia traz [30, 19, 4, 7, 46, 19]
- tabela publicada x jogos — kam01:44: Tonnerre Yaoundé tabela [30, 15, 8, 7, 43, 25] jogos [30, 15, 8, 7, 43, 24] — a Wikipédia traz [30, 15, 8, 7, 43, 23]
- tabela publicada x jogos — kam01:44: Fovu Baham tabela [30, 13, 11, 6, 36, 24] jogos [30, 13, 11, 6, 37, 27] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Canon Yaoundé tabela [30, 15, 4, 11, 40, 37] jogos [30, 15, 4, 11, 39, 35] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Sable Batié tabela [30, 11, 13, 6, 23, 17] jogos [30, 11, 13, 6, 26, 22] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Mount Cameroon tabela [29, 12, 6, 11, 32, 25] jogos [28, 12, 5, 11, 31, 31] — a Wikipédia traz [29, 13, 5, 11, 34, 31]
- tabela publicada x jogos — kam01:44: Kumbo Strikers tabela [30, 10, 9, 11, 18, 19] jogos [29, 10, 9, 10, 20, 16] — a Wikipédia traz [30, 10, 9, 11, 20, 19]
- tabela publicada x jogos — kam01:44: Racing Bafoussam tabela [30, 11, 9, 10, 20, 33] jogos [30, 10, 9, 11, 21, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Union Douala tabela [30, 10, 8, 12, 25, 22] jogos [30, 9, 10, 11, 29, 28] — a Wikipédia traz [30, 10, 10, 10, 30, 29]
- tabela publicada x jogos — kam01:44: Espérance Guider tabela [30, 10, 7, 13, 30, 34] jogos [30, 10, 7, 13, 32, 40] — a Wikipédia traz [30, 10, 7, 13, 32, 38]
- tabela publicada x jogos — kam01:44: Unisport du Haut-Nkam tabela [29, 10, 9, 10, 20, 28] jogos [29, 11, 8, 10, 26, 28] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Stade Bandjoun tabela [30, 10, 7, 13, 28, 34] jogos [30, 10, 8, 12, 30, 41] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Cintra Yaoundé tabela [30, 9, 8, 13, 30, 32] jogos [30, 8, 10, 12, 29, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — kam01:44: Olympic Mvolyé tabela [30, 7, 10, 13, 30, 29] jogos [29, 6, 10, 13, 34, 41] — a Wikipédia traz [30, 6, 11, 13, 34, 41]
- tabela publicada x jogos — kam01:44: Dynamo Douala tabela [29, 8, 5, 16, 27, 30] jogos [28, 9, 5, 14, 25, 27] — a Wikipédia traz [29, 8, 5, 16, 25, 30]
- tabela publicada x jogos — kam01:44: Girondins Ngaoundéré tabela [29, 2, 12, 15, 25, 33] jogos [28, 2, 11, 15, 17, 39] — a Wikipédia traz [29, 2, 12, 15, 17, 39]
- decidido fora de campo — Coton Sport Kumbo Strikers (s/d): Kumbo dns, claiming transportation problems;
- abandonado/suspenso, sem valer — Unisport du Haut-Nkam Union Douala (2001-02-28): both teams 1 point deducted for the abandonment
- decidido fora de campo — Mount Cameroon Unisport du Haut-Nkam (2001-06-03): originally 1-1; awarded 3-0 to Mt Cameroon as
- W.O./pontos para o mandante — Racing Bafoussam Dynamo Douala (2001-08-06): inferred]  [bt
- decidido fora de campo — Union Douala Dynamo Douala (2001-08-09): awarded 3-0 to Union, abandoned in 48' at 2-0
- W.O./pontos para o mandante — Racing Bafoussam Cintra Yaoundé (2001-08-30): inferred]  [bt
- W.O./pontos para o visitante — Girondins Ngaoundéré Unisport du Haut-Nkam (2001-08-30): inferred]  [lt
- decidido fora de campo — Mount Cameroon Coton Sport (s/d): originally 2-0, awarded 0-3 to Cotonsport as Mt
- decidido fora de campo — Dynamo Douala Mount Cameroon (2001-10-07)
- abandonado/suspenso, sem valer — Tonnerre Yaoundé Racing Bafoussam (2001-10-21): abandoned due to poor light at 2-0
- decidido fora de campo — Mount Cameroon Olympic Mvolyé (2001-10-21): Olympic dns; awarded 3-0

### 2002

- decidido fora de campo — Unisport du Haut-Nkam Stade Bandjoun (2002-03-31): awarded 3-0 to Unisport; originally 1-1
- abandonado/suspenso, sem valer — Coton Sport Cintra Yaoundé (2002-05-05): abandoned at 2-0 in 70' due to rain
- não jogado — Canon Yaoundé Sable Batié (2002-06-20): 2-3, annulled and to be replayed
- abandonado/suspenso, sem valer — Union Douala Mount Cameroon (2002-09-08): 1-1, abd due rain
- decidido fora de campo — Bamboutos Mbouda Mount Cameroon (2002-09-26): awarded 0-2, abandoned at 1-2
- decidido fora de campo — Union Douala Espérance Guider (2002-10-13): awarded 2-0 by default

### 2003

- sem ocorrências

### 2004

- abandonado/suspenso, sem valer — Espérance Guider Renaissance Ngoumou (2004-06-24): abandoned at 30' due to rain
- decidido fora de campo — Sable Batié Union Douala (2004-08-11): awarded 0-3; Sable dns and have Aug 15]                             3 points deducted
- abandonado/suspenso, sem valer — Tonnerre Yaoundé Bamboutos Mbouda (2004-10-06): abandoned at 0-1 in 80' due to poor
- decidido fora de campo — Coton Sport Canon Yaoundé (2004-11-04): awarded 3-0; abandoned at 0-0 in 79'
- abandonado/suspenso, sem valer — PWD Bamenda Mount Cameroon (2004-09-05): abandoned at 0-0 at half time due to rain
- abandonado/suspenso, sem valer — Victoria United Mount Cameroon (2004-10-07): abandoned at 0-0 in 45' due to pitch invasion

### 2005

- ogol: 305 jogos casados (edição 1102 do ogol, 306 jogos)
- corrigido — Les Astres x Foudre Akonolinga (2005-06-12): "temporarily awarded 3-0, later revoked": vale o 1-2 de campo (a tabela confirma)
- data diferente no ogol — Bamboutos Mbouda x Tonnerre Yaoundé: RSSSF 2005-05-14, ogol 2005-05-08; fica a da RSSSF
- placar diferente no ogol — Coton Sport x Racing Bafoussam (2005-07-31): RSSSF 5-0, ogol 2-1; fica o da RSSSF
- decidido fora de campo — Union Douala Bamboutos Mbouda (2005-03-30): awarded 2-0; abandoned at 2-1 in 77'
- não jogado — Kadji Sport Academy Foudre Akonolinga (2005-04-04): awarded 3-0; Foudre dns; Foudre 3 pts deducted;
- abandonado/suspenso, sem valer — Canon Yaoundé Sahel Maroua (2005-07-17): 0-0, abd 87'
- decidido fora de campo — PWD Bamenda Espérance Guider (2005-07-31): awarded 0-1; abd in 86' at 1-1 due to pitch invasion
- decidido fora de campo — Fovu Baham Sahel Maroua (2005-09-11): awarded 4-0; Sahel 2 points deducted
- decidido fora de campo — University FC Ngaoundéré Canon Yaoundé (2005-09-11): awarded 3-0; 1-0, abd 28' due to violence
- decidido fora de campo — Tonnerre Yaoundé Fovu Baham (2005-10-19): awarded 0-3; 0-2 abd 72'; due to pitch invasion by home fans; Tonnerre 1 pt deducted

### 2006

- ogol: 239 jogos casados (edição 2772 do ogol, 240 jogos)
- corrigido — Fovu Baham x Impôts FC (2006-07-23): "awarded 3-0; 1-0 abd by Impôts at 75'": não é abandono sem valer; a tabela conta o 3-0
- abandonado/suspenso, sem valer — Canon Yaoundé Union Douala (2006-07-02): 1-0 abd 20' due to rain
- decidido fora de campo — Fovu Baham Impôts FC (2006-07-23): 1-0 em campo, abandonado aos 75' pelo Impôts

### 2007

- O Bamboutos foi excluído no fim do campeonato (a tabela o põe à parte, sem posição); os jogos que não fez contam como W.O. para os adversários.
- ogol: 306 jogos casados (edição 2811 do ogol, 306 jogos)
- corrigido — Canon Yaoundé x University FC Ngaoundéré (2007-04-29): "match finished 1-0 but Canon used suspended coach; win awarded to University": a tabela conta a vitória da University e o 1-0 de campo
- corrigido — Union Douala x Bamboutos Mbouda (2007-10-07): "n/p" com "awarded 3-0" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- corrigido — Bamboutos Mbouda x Coton Sport (2007-10-11): "n/p" com "awarded 0-3" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- corrigido — Sable Batié x Bamboutos Mbouda (2007-10-14): "n/p" com "awarded 3-0" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta
- data diferente no ogol — Canon Yaoundé x Les Astres: RSSSF 2007-05-23, ogol 2007-05-30; fica a da RSSSF
- data diferente no ogol — Coton Sport x Bamboutos Mbouda: RSSSF 2007-05-23, ogol 2007-05-30; fica a da RSSSF
- decidido fora de campo — Union Douala Sable Batié (2007-04-13): awarded 3-0
- W.O./pontos para o visitante — Canon Yaoundé University FC Ngaoundéré (2007-04-29): match finished 1-0 but Canon
- decidido fora de campo — Union Douala Bamboutos Mbouda (2007-10-07): awarded 3-0
- decidido fora de campo — Espérance Guider CPS Bertoua (2007-10-11): awarded 3-0; CPSB walked off at 1-0
- decidido fora de campo — Fédéral du Noun Sable Batié (2007-10-11): awarded 0-3; Fédéral dns; Fédéral 3
- decidido fora de campo — Bamboutos Mbouda Coton Sport (2007-10-11): awarded 0-3]        points deducted
- decidido fora de campo — Sable Batié Bamboutos Mbouda (2007-10-14): awarded 3-0

### 2007/08

- ogol: 240 jogos casados (edição 2820 do ogol, 240 jogos)
- corrigido — Caïman Douala x Unisport du Haut-Nkam (2008-03-22): "original score (0-0) stood but points awarded to Unisport" (o Caïman escalou jogador suspenso): a tabela conta a vitória do Unisport e o 0-0
- placar diferente no ogol — Canon Yaoundé x Mount Cameroon (2008-01-09): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Unisport du Haut-Nkam x Sable Batié (2008-01-09): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Tonnerre Yaoundé x Mount Cameroon (2008-02-10): RSSSF 3-1, ogol 3-0; fica o da RSSSF
- W.O./pontos para o visitante — Caïman Douala Unisport du Haut-Nkam (2008-03-22): original score (0-0) stood but points Mar 23]                              awarded to Unisport as Caïman fielded
- abandonado/suspenso, sem valer — Inter Lion Ngoma Coton Sport (2008-05-18): abandoned due to rain
- decidido fora de campo — Aigle Royal de la Menoua Inter Lion Ngoma (2008-07-06): awarded 3-0, forfait Ngoma

### 2008/09

- ogol: 182 jogos casados (edição 4360 do ogol, 182 jogos)
- data diferente no ogol — Unisport du Haut-Nkam x University FC Ngaoundéré: RSSSF 2009-02-11, ogol 2009-02-15; fica a da RSSSF
- placar diferente no ogol — Mount Cameroon x Sable Batié (2009-02-15): RSSSF 3-0, ogol 0-3; fica o da RSSSF
- decidido fora de campo — Aigle Royal de la Menoua Tiko United (2008-12-03): awarded 0-1 to Tiko; originally 1-0,
- decidido fora de campo — Coton Sport Mount Cameroon (2009-05-23): awarded 3-0, forfait Mount Cameroon
- decidido fora de campo — Mount Cameroon Unisport du Haut-Nkam (2009-06-10): awarded 0-3, forfait Mount Cameroon

### 2009/10

- ogol: 181 jogos casados (edição 12935 do ogol, 182 jogos)
- corrigido — Coton Sport x Les Astres (2010-04-10): vitória dada ao Les Astres sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- corrigido — Sable Batié x Union Douala (2010-04-11): vitória dada ao Union Douala sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- corrigido — Fovu Baham x Renaissance Ngoumou (2010-05-02): vitória dada ao Renaissance Ngoumou sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- abandonado/suspenso, sem valer — Fovu Baham Panthère du Ndé (2009-10-28): abandoned due to rain
- decidido fora de campo — Renaissance Ngoumou Canon Yaoundé (2010-04-04): awarded 2-0 win to Renaissance;
- W.O./pontos para o visitante — Coton Sport Les Astres (2010-04-10): vitória dada ao Les Astres sem gols; em campo, 1-0 para o Coton Sport (ogol)
- W.O./pontos para o visitante — Sable Batié Union Douala (2010-04-11): vitória dada ao Union Douala sem gols; em campo, 2-0 para o Sable Batié (ogol)
- W.O./pontos para o visitante — Fovu Baham Renaissance Ngoumou (2010-05-02): vitória dada ao Renaissance Ngoumou sem gols; em campo, 2-1 para o Fovu Baham (ogol)

### 2010/11

- A RSSSF só traz a tabela final (a classificação); os jogos vêm do ogol, menos os do Union e do Caïman Douala (o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo). Jogos incompletos.
- jogos incompletos (sem os jogos do Union e do Caïman Douala, que o ogol não separa)
- ogol: base dos jogos (125 jogos)
- corrigido — Union Douala x Sable Batié (2010-11-13): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Tiko United x Union Douala (2010-11-14): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Union Douala (2010-11-21): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Coton Sport (2010-11-28): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Scorpion Bey x Union Douala (2010-11-28): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Coton Sport (2010-12-05): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Panthère du Ndé x Union Douala (2010-12-05): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — YOSA Bamenda x Union Douala (2010-12-12): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x University FC Ngaoundéré (2010-12-12): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Renaissance Ngoumou x Union Douala (2010-12-19): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Panthère du Ndé (2010-12-19): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Unisport du Haut-Nkam x Union Douala (2010-12-22): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Canon Yaoundé (2010-12-22): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Sable Batié x Union Douala (2011-01-09): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x University FC Ngaoundéré (2011-01-09): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Scorpion Bey (2011-01-16): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — AS Lausanne x Union Douala (2011-01-16): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — YOSA Bamenda x Union Douala (2011-01-23): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Renaissance Ngoumou x Union Douala (2011-01-23): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Unisport du Haut-Nkam (2011-01-30): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Les Astres (2011-02-27): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Canon Yaoundé x Union Douala (2011-03-06): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — AS Lausanne x Union Douala (2011-03-06): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Tiko United (2011-03-13): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Les Astres (2011-03-13): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Sable Batié x Union Douala (2011-03-27): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Tiko United (2011-03-27): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Union Douala (2011-04-10): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Coton Sport x Union Douala (2011-04-17): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Scorpion Bey (2011-04-17): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Coton Sport x Union Douala (2011-04-30): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Panthère du Ndé (2011-04-30): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — University FC Ngaoundéré x Union Douala (2011-05-08): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x YOSA Bamenda (2011-05-08): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Renaissance Ngoumou (2011-05-22): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Panthère du Ndé x Union Douala (2011-05-22): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Canon Yaoundé x Union Douala (2011-06-05): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Unisport du Haut-Nkam (2011-06-06): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Sable Batié (2011-06-12): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — University FC Ngaoundéré x Union Douala (2011-06-12): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x AS Lausanne (2011-06-19): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Scorpion Bey x Union Douala (2011-06-19): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x Renaissance Ngoumou (2011-06-26): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x YOSA Bamenda (2011-06-26): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Les Astres x Union Douala (2011-07-03): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Unisport du Haut-Nkam x Union Douala (2011-07-03): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo
- corrigido — Union Douala x AS Lausanne (2011-07-10): o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é o jogo

### 2011/12

- ogol: 175 jogos casados (edição 75521 do ogol, 175 jogos)
- placar diferente no ogol — Coton Sport x Renaissance Ngoumou (2012-01-29): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Unisport du Haut-Nkam x Sable Batié (2012-02-26): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- decidido fora de campo — Coton Sport Scorpion Bey (2012-08-05): awarded 3-0; Scorpion dns

### 2013

- sem ocorrências

### 2014

- Douala AC x Coton Sport: os dois clubes se recusaram a jogar; a federação deu derrota por 0-0 aos dois e tirou 3 pontos de cada ("both clubs refused to play, both had 3 points deducted and the match awarded a 0-0 loss against them"). O jogo fica sem placar; a tabela conta uma derrota para cada um.
- tabela publicada x jogos — kam2014:24: Coton Sport tabela [36, 23, 9, 4, 57, 18] jogos [35, 23, 9, 3, 57, 18] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — kam2014:24: Douala AC tabela [36, 5, 8, 23, 31, 53] jogos [35, 5, 8, 22, 31, 53] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — UMS de Loum Sable Batié (2014-02-02): awarded 1-0; originally 1-1,
- decidido fora de campo — Douala AC Coton Sport (2014-02-24): both clubs refused to play, both had

### 2015

- tabela publicada x jogos — kam2015:24: Canon Yaoundé tabela [34, 8, 15, 11, 34, 41] jogos [34, 8, 14, 12, 33, 43] — a Wikipédia traz [34, 8, 14, 12, 33, 41]
- tabela publicada x jogos — kam2015:24: Fovu Baham tabela [34, 8, 14, 12, 30, 37] jogos [34, 9, 13, 12, 32, 36] — a Wikipédia traz [34, 9, 13, 12, 30, 36]
- provável jogo da diferença: Fovu Baham 3-0 Canon Yaoundé (2015-03-15, kam2015:125); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — Fovu Baham 1-1 Canon Yaoundé (2015-03-15): awarded 3-0; originally 1-1, Canon used an Mar 25]                             ineligible player (Kohn Jean Calvin); award
- abandonado/suspenso, sem valer — Tonnerre Yaoundé APEJES Academy (2015-04-04): abandoned at 0-1 in 15' due to rain
- decidido fora de campo — Coton Sport Tonnerre Yaoundé (2015-05-27): awarded 3-0, Tonnerre dns; Tonnerre 3 points deducted
- abandonado/suspenso, sem valer — Cosmos Bafia Njalla Quan (2015-07-26): abandoned due to heavy rain
- decidido fora de campo — Coton Sport Canon Yaoundé (2015-07-30): awarded 0-3; abandoned at 0-0 at half-time due to
- abandonado/suspenso, sem valer — Cosmos Bafia YOSA Bamenda (2015-08-03): abandoned in 2nd half due to heavy rain

### 2016

- decidido fora de campo — Canon Yaoundé Lion Blessé (2016-03-13): awarded 0-1; originally 0-0
- abandonado/suspenso, sem valer — Bamboutos Mbouda Panthère du Ndé (2016-04-14): abandoned in 75' due to rain

### 2017

- ogol: 290 jogos casados (edição 125192 do ogol, 306 jogos)
- data diferente no ogol — Union Douala x YOSA Bamenda: RSSSF 2017-03-22, ogol 2017-03-12; fica a da RSSSF
- data diferente no ogol — Coton Sport x Djiko FC: RSSSF 2017-03-26, ogol 2017-03-19; fica a da RSSSF
- data diferente no ogol — Unisport du Haut-Nkam x Djiko FC: RSSSF 2017-03-30, ogol 2017-03-26; fica a da RSSSF
- data diferente no ogol — Coton Sport x Canon Yaoundé: RSSSF 2017-03-31, ogol 2017-03-26; fica a da RSSSF
- data diferente no ogol — Stade Renard x Unisport du Haut-Nkam: RSSSF 2017-05-18, ogol 2017-05-24; fica a da RSSSF
- data diferente no ogol — Union Douala x Coton Sport: RSSSF 2017-05-18, ogol 2017-05-24; fica a da RSSSF
- data diferente no ogol — APEJES Academy x Coton Sport: RSSSF 2017-06-07, ogol 2017-05-28; fica a da RSSSF
- data diferente no ogol — Coton Sport x YOSA Bamenda: RSSSF 2017-06-12, ogol 2017-06-04; fica a da RSSSF
- data diferente no ogol — Stade Renard x Coton Sport: RSSSF 2017-06-25, ogol 2017-06-18; fica a da RSSSF
- data diferente no ogol — Canon Yaoundé x APEJES Academy: RSSSF 2017-07-05, ogol 2017-07-09; fica a da RSSSF
- data diferente no ogol — Dragon Yaoundé x Bamboutos Mbouda: RSSSF 2017-09-17, ogol 2017-09-21; fica a da RSSSF
- data diferente no ogol — Colombe Sportive x Eding Sport: RSSSF 2017-09-17, ogol 2017-09-21; fica a da RSSSF
- decidido fora de campo — Djiko FC New Star Douala (2017-06-18): awarded 0-3, originally 0-0
- decidido fora de campo — New Star Douala Racing Bafoussam (2017-06-28): awarded 3-0, originally 0-2
- decidido fora de campo — Canon Yaoundé UMS de Loum (2017-08-16): awarded 3-0, originally 1-1
- abandonado/suspenso, sem valer — Lion Blessé Dragon Yaoundé (2017-09-07): abandoned due to rain

### 2018

- ogol: 302 jogos casados (edição 125924 do ogol, 306 jogos)
- data diferente no ogol — Yaoundé II FC x Les Astres: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — APEJES Academy x Fovu Baham: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — New Star Douala x Aigle Royal de la Menoua: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — UMS de Loum x Union Douala: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — Colombe Sportive x AS Fortuna: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — Djiko FC x Dragon Yaoundé: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — Bamboutos Mbouda x Unisport du Haut-Nkam: RSSSF 2018-04-04, ogol 2018-03-31; fica a da RSSSF
- data diferente no ogol — Coton Sport x Stade Renard: RSSSF 2018-04-05, ogol 2018-03-31; fica a da RSSSF
- decidido fora de campo — New Star Douala Eding Sport (2018-02-18): awarded 2-0, Eding forfeited
- decidido fora de campo — APEJES Academy Bamboutos Mbouda (2018-06-10): awarded 0-3, originally 0-0; APEJES

### 2019

- ogol: 159 jogos casados (edição 133839 do ogol, 159 jogos)
- decidido fora de campo — Union Douala APEJES Academy (2019-04-20): awarded 0-3; originally 0-0, Union fielded unlicensed players

### 2019/20

- abandonado em 12/05/2020 (pandemia de Covid-19); o PWD Bamenda foi declarado campeão, sem rebaixamento
- ogol: 253 jogos casados (edição 157041 do ogol, 253 jogos)
- não jogado — APEJES Academy Stade Renard (2020-03-29)
- não jogado — Avion du Nkam Dragon Yaoundé (2020-03-29)
- não jogado — Canon Yaoundé Union Douala (2020-03-29)
- não jogado — AS Fortuna Colombe Sportive (2020-03-29)
- não jogado — Panthère du Ndé Fovu Baham (2020-03-29)
- não jogado — PWD Bamenda Djiko FC (2020-03-29)
- não jogado — UMS de Loum Bamboutos Mbouda (2020-03-29)
- não jogado — YOSA Bamenda Tonnerre Yaoundé (2020-03-29)

### 2020/21

- A liga da LFPC ("Ligue 2020/21") parou na 1ª rodada, em 4/11/2020, quando a FECAFOOT proibiu a LFPC de organizá-la (só Panthère 0-2 Coton Sport foi jogado). A edição é a "Ligue 2021", da FECAFOOT.
- ogol: 184 jogos casados (edição 159596 do ogol, 205 jogos)
- data diferente no ogol — AS Fortuna x Fovu Baham: RSSSF 2021-09-23, ogol 2021-09-29; fica a da RSSSF
- não jogado — Colombe Sportive New Star Douala (2021-03-06): award of 3-0 revoked
- não jogado — YOSA Bamenda Tonnerre Yaoundé (2021-03-09): award of 3-0 revoked
- decidido fora de campo — YOSA Bamenda New Star Douala (2021-04-21): awarded 3-0, New Star forfeited; New Star 3 points deducted
- decidido fora de campo — Dragon Yaoundé Eding Sport (2021-08-13): awarded 3-0; originally 2-2, Eding
- decidido fora de campo — Dragon Yaoundé Stade Renard (2021-08-29): awarded 3-0; originally 1-2, Stade

### 2022

- ogol: 283 jogos casados (edição 163453 do ogol, 293 jogos)
- data diferente no ogol — Djiko FC x YOSA Bamenda: RSSSF 2022-04-02, ogol 2022-04-08; fica a da RSSSF
- data diferente no ogol — Les Astres x AS Fortuna: RSSSF 2022-04-02, ogol 2022-04-08; fica a da RSSSF
- data diferente no ogol — Fauve Azur x Racing Bafoussam: RSSSF 2022-04-02, ogol 2022-04-08; fica a da RSSSF
- placar diferente no ogol — Avion du Nkam x Renaissance Ngoumou (2022-04-13): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Ofta Kribi x Dragon Yaoundé (2022-06-08): RSSSF 1-4, ogol 2-4; fica o da RSSSF
- data diferente no ogol — Racing Bafoussam x Fauve Azur: RSSSF 2022-06-08, ogol 2022-06-14; fica a da RSSSF
- data diferente no ogol — AS Fortuna x Les Astres: RSSSF 2022-06-08, ogol 2022-06-14; fica a da RSSSF
- data diferente no ogol — YOSA Bamenda x Djiko FC: RSSSF 2022-06-08, ogol 2022-06-14; fica a da RSSSF
- data diferente no ogol — YOSA Bamenda x Colombe Sportive: RSSSF 2022-06-08, ogol 2022-06-17; fica a da RSSSF
- data diferente no ogol — Racing Bafoussam x Panthère du Ndé: RSSSF 2022-06-08, ogol 2022-06-17; fica a da RSSSF
- data diferente no ogol — Les Astres x Union Douala: RSSSF 2022-06-08, ogol 2022-06-17; fica a da RSSSF
- decidido fora de campo — Tonnerre Yaoundé Union Douala (2022-03-20): awarded 0-3, Tonnerre dns
- decidido fora de campo — New Star Douala UMS de Loum (2022-04-20): awarded 0-3

### 2022/23

- ogol: 226 jogos casados (edição 170725 do ogol, 226 jogos)
- placar diferente no ogol — Bamboutos Mbouda x Gazelle FA (2023-05-21): RSSSF 4-1, ogol 1-4; fica o da RSSSF
- decidido fora de campo — UMS de Loum Avion du Nkam (2023-04-02): awarded 0-3; originally 2-1, UMS

### 2023/24

- ogol: 236 jogos casados (edição 181355 do ogol, 245 jogos)
- corrigido — UMS de Loum x Victoria United (2024-02-22): vitória dada ao Victoria United sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- corrigido — APEJES Academy x UMS de Loum (2024-02-25): vitória dada ao APEJES Academy sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- corrigido — Victoria United x YOSA Bamenda (2024-02-27): vitória dada ao Victoria United sem gols ("awarded 0-0 win"); a tabela conta a vitória e nenhum gol
- placar diferente no ogol — Les Astres x AS Fortuna (2023-12-23): RSSSF 1-2, ogol 0-1; fica o da RSSSF
- não jogado — Avion du Nkam UMS de Loum (2023-10-05): not played due to license problems UMS
- decidido fora de campo — Victoria United APEJES Academy (2023-10-21): awarded 0-3, Victoria United dns; Victoria Oct 22]                             also had 3 points deducted
- decidido fora de campo — Victoria United UMS de Loum (2023-11-12): awarded 0-2, originally 2-2, Victoria fielded
- decidido fora de campo — Victoria United Avion du Nkam (2024-02-18): awarded 1-0; originally 1-1, Avion fielded
- W.O./pontos para o visitante — UMS de Loum Victoria United (2024-02-22): vitória dada ao Victoria United sem gols; em campo, 1-0 para o UMS de Loum
- W.O./pontos para o mandante — APEJES Academy UMS de Loum (2024-02-25): vitória dada ao APEJES Academy sem gols; em campo, 0-0
- W.O./pontos para o mandante — Victoria United YOSA Bamenda (2024-02-27): vitória dada ao Victoria United sem gols; em campo, 1-1
- decidido fora de campo — UMS de Loum Aigle Royal de la Menoua (2024-05-02): awarded 0-3; abandoned at 1-1 in 76', UMS walked off

### 2024/25

- ogol: 237 jogos casados (edição 193139 do ogol, 242 jogos)
- corrigido — Coton Sport x Canon Yaoundé (2025-05-04): jogo válido: a nota "award of 3-0 annulled, match refixtured" continua a do Dynamo Douala x Aigle Royal, da linha de cima
- abandonado/suspenso, sem valer — PWD Bamenda Fauve Azur (2025-02-09): abandoned at 1-1 at half-time due to nearby gunshots
- decidido fora de campo — Fauve Azur Bamboutos Mbouda (2025-04-20): awarded 3-0, Bamboutos dns
- decidido fora de campo — Stade Renard Colombe Sportive (2025-04-23): awarded 0-3; abandoned at 0-1 at half-time due
- não jogado — PWD Bamenda Bamboutos Mbouda (2025-04-27): Bamboutos dns, refixtured
- não jogado — Dynamo Douala Aigle Royal du Moungo (2025-05-04): Aigle Royal dns due to food poisoning numerous players;
- não jogado — Bamboutos Mbouda Colombe Sportive (2025-05-04): Bamboutos dns, match refixtured
- decidido fora de campo — Gazelle FA YOSA Bamenda (2025-05-04): awarded 3-0, YOSA dns
- decidido fora de campo — YOSA Bamenda Fauve Azur (2025-05-14): awarded 0-3, YOSA dns
- decidido fora de campo — Coton Sport YOSA Bamenda (2025-06-08): awarded 3-0, YOSA excluded
- decidido fora de campo — Les Astres YOSA Bamenda (2025-06-16): awarded 3-0, YOSA excluded
- decidido fora de campo — Gazelle FA Dynamo Douala (2025-06-20): awarded 0-3; abandoned at 2-1 in 54'; referee
- decidido fora de campo — YOSA Bamenda Aigle Royal du Moungo (2025-06-22): awarded 0-3, YOSA excluded
- decidido fora de campo — YOSA Bamenda Stade Renard (2025-07-06): awarded 0-3, YOSA excluded

### 2026

- ogol: 182 jogos casados (edição 212840 do ogol, 182 jogos)

