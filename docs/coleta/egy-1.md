# Campeonato Egípcio (1ª divisão) — coleta de dados

Gerado por `python coleta/egy-1/importar.py`. Pacote em `data/coleta/egy-1/pacote/`.

**Edições:** 73, uma por temporada da liga nacional (Egyptian Premier League), de 1948/49, a primeira, a 2025/26, como na lista de campeões da RSSSF (`egychamp.html`) e na Wikipédia em inglês. As temporadas não disputadas ficam de fora (1951/52, pela Olimpíada; 1967/68 a 1970/71, pela Guerra dos Seis Dias). As começadas e não terminadas entram sem campeão, com o motivo: 1954/55, 1971/72 (a RSSSF chama de 1970/71; a briga em Al-Ahly x Zamalek foi em 24/12/1971), 1973/74, 1989/90, 2011/12 e 2012/13 (a "2013" da RSSSF).

**Fora do pacote** (pesquisa de 23/11/2026): o campeonato da U.I.S.S.E. (1912/13 a 1914), mata-mata entre clubes das colônias estrangeiras que a federação egípcia não reconhece; a Liga do Cairo (1922/23 a 1957/58) e as outras ligas regionais; a Copa do Egito, a Supercopa e a Copa da Liga.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/egy-1/rsssf/`: base dos jogos de 1997/98 a 2024/25, com rodadas, datas e autores dos gols; nos outros anos, a tabela final, que é a conferência); ogol (base dos jogos de 1964/65 a 1996/97, 2010/11, 2011/12 e 2025/26; nos outros anos, rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); Wikipédia em inglês (lista de campeões e de artilheiros, e a tabela final de cada temporada, terceira fonte nas divergências). De 1948/49 a 1963/64 nenhuma fonte pública tem os jogos: as edições entram com a tabela final (e com a final ou o desempate do título, quando a página traz). A ESPN não tem a liga egípcia.

**Clubes:** nomes árabes com hífen; o Al-Ahly fica com o nome puro; homônimos de clubes de outros países levam a cidade (Al-Ittihad de Alexandria, Al-Ittihad de Suez, Al-Nasr do Cairo, El-Merreikh de Port Said). Mesmo clube com outro nome é um só, com o nome atual (Farouk Club = Zamalek; Al-Assiouty = Pyramids; FC Masr = ZED; Future = Modern Sport; Ittihad Othman = Dina Farms; Al-Ma'aden = Goldy; Sawahel = Haras El-Hodoud). Regras em `coleta/egy-1/clubes_egy.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada pela RSSSF (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos (erro de digitação da RSSSF). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Pontos por vitória como as tabelas contam: 2 até 1985/86, 3 de 1986/87 a 1989/90, 2 de 1990/91 a 1993/94 e 3 a partir de 1994/95.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1948/49 | 11 | 6 (6) | 25 | 0 | 0 / 0 | Al-Ahly | jogos incompletos (só 6 jogos da liga e o desempate do 2º lugar) |
| 1949/50 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1950/51 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1952/53 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1953/54 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1954/55 | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | temporada não terminada |
| 1955/56 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1956/57 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1957/58 | 16 | 2 (2) | 6 | 0 | 0 / 0 | Al-Ahly | jogos incompletos (só a final entre os vencedores dos grupos) |
| 1958/59 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1959/60 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Zamalek | sem jogos (só a tabela final) |
| 1960/61 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1961/62 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Al-Ahly | sem jogos (só a tabela final) |
| 1962/63 | 24 | 10 (10) | 32 | 0 | 0 / 0 | Tersana | jogos incompletos (só o desempate do grupo B e o quadrangular final) |
| 1963/64 | 24 | 2 (2) | 10 | 0 | 0 / 0 | Zamalek | jogos incompletos (só a final entre os vencedores dos grupos) |
| 1964/65 | 12 | 132 (132) | 313 | 0 | 0 / 1 | Zamalek | pontos corridos |
| 1965/66 | 12 | 121 (121) | 297 | 0 | 0 / 1 | Olympic Club | pontos corridos |
| 1966/67 | 12 | 132 (132) | 267 | 0 | 0 / 1 | Ismaily | pontos corridos |
| 1971/72 | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | temporada não terminada |
| 1972/73 | 12 | 132 (132) | 216 | 0 | 1 / 0 | Ghazl El-Mahalla | pontos corridos |
| 1973/74 | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | temporada não terminada |
| 1974/75 | 18 | 306 (306) | 628 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 1975/76 | 23 | 2 (2) | 5 | 0 | 0 / 0 | Al-Ahly | jogos incompletos (só a final entre os vencedores dos grupos) |
| 1976/77 | 15 | 210 (210) | 375 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1977/78 | 14 | 182 (182) | 306 | 0 | 1 / 1 | Zamalek | pontos corridos |
| 1978/79 | 12 | 132 (132) | 224 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1979/80 | 16 | 240 (240) | 408 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 1980/81 | 14 | 182 (182) | 322 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 1981/82 | 14 | 182 (182) | 302 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1982/83 | 12 | 121 (121) | 201 | 0 | 1 / 0 | Al-Mokawloon Al-Arab | pontos corridos |
| 1983/84 | 12 | 132 (132) | 216 | 0 | 1 / 0 | Zamalek | pontos corridos |
| 1984/85 | 12 | 132 (132) | 210 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1985/86 | 12 | 132 (132) | 233 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1986/87 | 12 | 132 (132) | 219 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1987/88 | 12 | 132 (132) | 249 | 0 | 1 / 0 | Zamalek | pontos corridos |
| 1988/89 | 12 | 132 (132) | 278 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1989/90 | 14 | 84 (84) | 137 | 0 | 0 / 0 | — | temporada não terminada |
| 1990/91 | 18 | 307 (307) | 497 | 0 | 1 / 0 | Ismaily | pontos corridos + desempate |
| 1991/92 | 14 | 182 (182) | 286 | 0 | 0 / 1 | Zamalek | pontos corridos |
| 1992/93 | 14 | 181 (182) | 336 | 0 | 0 / 1 | Zamalek | pontos corridos |
| 1993/94 | 14 | 183 (183) | 334 | 0 | 2 / 0 | Al-Ahly | pontos corridos + desempate |
| 1994/95 | 14 | 182 (182) | 321 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 1995/96 | 16 | 240 (240) | 447 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 1996/97 | 16 | 240 (240) | 556 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 1997/98 | 16 | 241 (241) | 561 | 0 | 1 / 0 | Al-Ahly | pontos corridos + desempate |
| 1998/99 | 14 | 183 (183) | 387 | 64 | 1 / 0 | Al-Ahly | pontos corridos + desempate |
| 1999/00 | 14 | 182 (182) | 403 | 318 | 1 / 0 | Al-Ahly | pontos corridos |
| 2000/01 | 14 | 182 (182) | 411 | 384 | 1 / 0 | Zamalek | pontos corridos |
| 2001/02 | 14 | 182 (182) | 475 | 430 | 1 / 0 | Ismaily | pontos corridos |
| 2002/03 | 15 | 184 (184) | 410 | 99 | 1 / 0 | Zamalek | pontos corridos + desempate |
| 2003/04 | 14 | 182 (182) | 446 | 434 | 1 / 0 | Zamalek | pontos corridos |
| 2004/05 | 14 | 182 (182) | 436 | 419 | 1 / 0 | Al-Ahly | pontos corridos |
| 2005/06 | 14 | 182 (182) | 418 | 412 | 1 / 0 | Al-Ahly | pontos corridos |
| 2006/07 | 16 | 240 (240) | 528 | 507 | 1 / 0 | Al-Ahly | pontos corridos |
| 2007/08 | 16 | 240 (240) | 577 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2008/09 | 16 | 241 (241) | 585 | 1 | 1 / 0 | Al-Ahly | pontos corridos + desempate |
| 2009/10 | 16 | 240 (240) | 531 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2010/11 | 16 | 240 (240) | 569 | 0 | 0 / 1 | Al-Ahly | pontos corridos |
| 2011/12 | 19 | 144 (144) | 350 | 0 | 1 / 0 | — | temporada não terminada |
| 2012/13 | 18 | 136 (136) | 293 | 0 | 2 / 0 | — | temporada não terminada |
| 2013/14 | 22 | 227 (227) | 469 | 0 | 3 / 0 | Al-Ahly | 2 grupos + desempate + fase final |
| 2014/15 | 20 | 380 (380) | 907 | 0 | 1 / 0 | Zamalek | pontos corridos |
| 2015/16 | 18 | 306 (306) | 676 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2016/17 | 18 | 306 (306) | 690 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2017/18 | 18 | 306 (306) | 718 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2018/19 | 18 | 306 (306) | 729 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2019/20 | 18 | 306 (306) | 692 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2020/21 | 18 | 306 (306) | 765 | 0 | 1 / 0 | Zamalek | pontos corridos |
| 2021/22 | 18 | 306 (306) | 673 | 0 | 1 / 0 | Zamalek | pontos corridos |
| 2022/23 | 18 | 306 (306) | 657 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2023/24 | 18 | 306 (306) | 730 | 0 | 1 / 0 | Al-Ahly | pontos corridos |
| 2024/25 | 18 | 225 (225) | 482 | 0 | 3 / 0 | Al-Ahly | pontos corridos + grupos do título e do rebaixamento |
| 2025/26 | 21 | 322 (322) | 651 | 0 | 3 / 0 | Zamalek | pontos corridos + grupos do título e do rebaixamento |

## Conferência e correções, edição a edição

### 1948/49

- jogos incompletos (só 6 jogos da liga e o desempate do 2º lugar)
- corrigido — Tersana x Ismaily (None): desempate do 2º lugar sem data na página (a data lida era a da rodada de cima)

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1952/53

- sem ocorrências

### 1953/54

- sem ocorrências

### 1954/55

- temporada não terminada: o Al-Ahly brigou com a federação e saiu do campeonato; nenhum título foi dado

### 1955/56

- sem ocorrências

### 1956/57

- sem ocorrências

### 1957/58

- jogos incompletos (só a final entre os vencedores dos grupos)

### 1958/59

- sem ocorrências

### 1959/60

- sem ocorrências

### 1960/61

- sem ocorrências

### 1961/62

- sem ocorrências

### 1962/63

- jogos incompletos (só o desempate do grupo B e o quadrangular final)
- jogo acrescentado à mão — Ismaily 0-1 Tersana: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Ismaily 0-1 Zamalek: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Tersana 0-1 Zamalek: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Al-Ahly 1-1 El-Qanah: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Al-Ahly 0-2 Tersana: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Al-Ahly 1-1 Zamalek: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — El-Qanah 1-2 Tersana: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — El-Qanah 1-2 Zamalek: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)
- jogo acrescentado à mão — Tersana 3-3 Zamalek: egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)

### 1963/64

- jogos incompletos (só a final entre os vencedores dos grupos)

### 1964/65

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)
- tabela publicada x jogos — egy65:14: Al-Ittihad de Alexandria tabela [22, 7, 5, 10, 21, 32] jogos [22, 7, 5, 10, 31, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy65:14: Haras El-Hodoud tabela [22, 5, 6, 11, 17, 24] jogos [22, 5, 6, 11, 17, 34] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1965/66

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (121 jogos)
- tabela publicada x jogos — egy66:14: Tersana tabela [21, 9, 5, 7, 37, 26] jogos [21, 9, 5, 7, 37, 27] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy66:14: El-Tayaran tabela [21, 2, 10, 9, 9, 31] jogos [21, 2, 10, 9, 8, 30] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy66:14: Al-Ittihad de Suez tabela [21, 4, 5, 12, 17, 39] jogos [21, 4, 5, 12, 16, 38] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy66:14: El-Qanah tabela [11, 4, 3, 4, 11, 12] jogos [11, 4, 3, 4, 11, 11] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1966/67

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)
- tabela publicada x jogos — egy67:14: Ghazl El-Mahalla tabela [22, 5, 8, 9, 19, 22] jogos [22, 5, 8, 9, 19, 23] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy67:14: Suez tabela [22, 4, 5, 13, 11, 28] jogos [22, 4, 5, 13, 12, 28] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1971/72

- temporada não terminada: suspensa depois da briga e da invasão de campo em Al-Ahly x Zamalek (24/12/1971); nenhum título foi dado (a RSSSF chama esta temporada de 1970/71)

### 1972/73

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1973/74

- temporada não terminada: suspensa pela Guerra do Yom Kippur (outubro de 1973); no lugar dela houve a Copa Outubro, que não conta como título da liga

### 1974/75

- a tabela da RSSSF troca os números de Plastic e Suez (12º e 13º, os dois com 28 pontos); o ogol e a tabela da Wikipédia dão a cada um os seus. A classificação usa os números dos jogos
- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (306 jogos)
- tabela publicada x jogos — egy75:14: Al-Ahly tabela [34, 26, 7, 1, 69, 11] jogos [34, 26, 7, 1, 70, 11] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy75:14: Plastic tabela [34, 10, 8, 16, 21, 33] jogos [34, 7, 14, 13, 26, 39] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy75:14: Suez tabela [34, 7, 14, 13, 26, 39] jogos [34, 10, 8, 16, 21, 34] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1975/76

- jogos incompletos (só a final entre os vencedores dos grupos)
- ogol: 1 jogos casados (edição 37366 do ogol, 1 jogos)

### 1976/77

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (210 jogos)

### 1977/78

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)
- tabela publicada x jogos — egy78:14: Zamalek tabela [26, 18, 5, 3, 41, 7] jogos [26, 17, 6, 3, 40, 7] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy78:14: Al-Ittihad de Alexandria tabela [26, 9, 10, 7, 18, 19] jogos [26, 9, 10, 7, 19, 20] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy78:14: Suez tabela [26, 10, 7, 9, 19, 20] jogos [26, 10, 7, 9, 20, 21] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1978/79

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1979/80

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)
- tabela publicada x jogos — egy80:14: Al-Ahly tabela [30, 23, 4, 3, 50, 15] jogos [30, 23, 4, 3, 51, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — egy80:14: Ghazl El-Mahalla tabela [30, 11, 11, 8, 26, 24] jogos [30, 11, 11, 8, 27, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — egy80:14: Al-Ittihad de Alexandria tabela [30, 9, 13, 8, 22, 24] jogos [30, 10, 10, 10, 21, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — egy80:14: Damanhour tabela [30, 6, 7, 17, 16, 29] jogos [30, 7, 6, 17, 16, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Ghazl El-Mahalla 1-1 Al-Ahly (1980-05-16, ogol:11801358); com 0-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1980/81

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)
- tabela publicada x jogos — egy81:14: Al-Ittihad de Alexandria tabela [26, 10, 10, 6, 27, 25] jogos [26, 9, 12, 5, 27, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — egy81:14: Esco tabela [26, 6, 9, 11, 23, 23] jogos [26, 6, 9, 11, 23, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — egy81:14: El-Sekka El-Hadid tabela [26, 3, 9, 14, 11, 42] jogos [26, 3, 9, 14, 11, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1981/82

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)

### 1982/83

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (121 jogos)

### 1983/84

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1984/85

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1985/86

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1986/87

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1987/88

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1988/89

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (132 jogos)

### 1989/90

- temporada não terminada: suspensa para a preparação da seleção para a Copa do Mundo de 1990; nenhum título foi dado
- ogol: base dos jogos (84 jogos)

### 1990/91

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (306 jogos)
- jogo acrescentado à mão — Al-Ahly 1-0 Ismaily: jogo do turno que falta no ogol (o Ismaily x Al-Ahly da 24ª rodada foi 1-1); o placar 1-0 sai da tabela

### 1991/92

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)
- tabela publicada x jogos — egy92:15: Zamalek tabela [26, 15, 10, 1, 36, 7] jogos [26, 14, 11, 1, 34, 6] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy92:15: Damanhour tabela [26, 6, 8, 12, 12, 26] jogos [26, 6, 9, 11, 11, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Damanhour 0-0 Zamalek (1992-05-22, ogol:11796182); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1992/93

- a tabela da RSSSF dá 26 jogos a El-Merreikh e El-Minya, com uma derrota a mais para cada um (e 5 gols sofridos a mais para o Merreikh); o ogol e a tabela da Wikipédia dão 25 jogos aos dois. O jogo entre eles não aparece em nenhuma fonte de jogos (provavelmente decidido fora de campo, com derrota para os dois). A classificação usa os números dos jogos; faltam 1 dos 182 jogos esperados pela tabela da RSSSF
- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (181 jogos)
- tabela publicada x jogos — egy93:15: Al-Masry tabela [26, 6, 13, 7, 19, 18] jogos [26, 6, 13, 7, 19, 16] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy93:15: El-Merreikh de Port Said tabela [26, 5, 12, 9, 15, 26] jogos [25, 5, 12, 8, 15, 21] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy93:15: Tanta tabela [26, 4, 11, 11, 14, 32] jogos [26, 4, 11, 11, 14, 33] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy93:15: El-Minya tabela [26, 2, 10, 14, 15, 35] jogos [25, 2, 10, 13, 15, 35] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1993/94

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)
- jogo acrescentado à mão — Al-Ahly 1-1 Ismaily: jogo do returno que falta no ogol (o da 6ª rodada também foi 1-1); o placar sai da tabela

### 1994/95

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (182 jogos)
- tabela publicada x jogos — egy95:15: El-Qanah tabela [26, 5, 10, 11, 19, 24] jogos [26, 5, 11, 10, 19, 24] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — egy95:15: Dina Farms tabela [26, 3, 13, 10, 19, 33] jogos [26, 3, 13, 10, 18, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1995/96

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)

### 1996/97

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)
- tabela publicada x jogos — egy97:15: El-Qanah tabela [30, 11, 7, 12, 31, 31] jogos [30, 11, 7, 12, 32, 31] — a Wikipédia traz [29, 11, 6, 12, 32, 31]
- tabela publicada x jogos — egy97:15: Al-Masry tabela [30, 9, 12, 9, 39, 35] jogos [30, 9, 12, 9, 39, 36] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)

### 1997/98

- ogol: 207 jogos casados (edição 37345 do ogol, 240 jogos)
- data diferente no ogol — Al-Ahly x Ghazl El-Suez: RSSSF 1998-03-20, ogol 1998-03-16; fica a da RSSSF
- data diferente no ogol — Zamalek x Al-Mokawloon Al-Arab: RSSSF 1998-04-24, ogol 1998-04-28; fica a da RSSSF
- placar diferente no ogol — El-Minya x Al-Mokawloon Al-Arab (1998-05-15): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Aswan x Ismaily (1998-06-09): RSSSF 3-1, ogol 3-0; fica o da RSSSF

### 1998/99

- ogol: 182 jogos casados (edição 37344 do ogol, 182 jogos)
- placar diferente no ogol — Zamalek x Aswan (1999-04-23): RSSSF 2-5, ogol 5-2; fica o da RSSSF
- decidido fora de campo — Ghazl El-Mahalla Aswan (1998-12-04): awarded 0-2; originally 1-1 but Mahalla used
- decidido fora de campo — Al-Ahly Zamalek (1999-04-09): awarded 2-0 after Zamalek left the pitch after

### 1999/00

- ogol: 90 jogos casados (edição 37343 do ogol, 182 jogos)
- data diferente no ogol — El-Mansoura x Goldy: RSSSF 1999-12-07, ogol 1999-12-17; fica a da RSSSF

### 2000/01

- ogol: 146 jogos casados (edição 37342 do ogol, 182 jogos)
- data diferente no ogol — Ismaily x Dina Farms: RSSSF 2000-11-02, ogol 2000-10-29; fica a da RSSSF
- data diferente no ogol — Ismaily x Al-Ittihad de Alexandria: RSSSF 2000-12-04, ogol 2000-12-11; fica a da RSSSF

### 2001/02

- ogol: 51 jogos casados (edição 37341 do ogol, 182 jogos)

### 2002/03

- ogol: 55 jogos casados (edição 37340 do ogol, 182 jogos)
- data diferente no ogol — Ismaily x Aswan: RSSSF 2002-10-04, ogol 2002-09-27; fica a da RSSSF
- data diferente no ogol — Al-Ahly x El-Mansoura: RSSSF 2002-09-27, ogol 2002-10-04; fica a da RSSSF

### 2003/04

- ogol: 181 jogos casados (edição 37339 do ogol, 182 jogos)
- data diferente no ogol — Baladiyat El-Mahalla x Zamalek: RSSSF 2004-05-11, ogol 2004-05-07; fica a da RSSSF

### 2004/05

- ogol: 156 jogos casados (edição 1103 do ogol, 182 jogos)
- placar diferente no ogol — El-Mansoura x Tersana (2004-10-22): RSSSF 2-3, ogol 1-2; fica o da RSSSF
- data diferente no ogol — Al-Ittihad de Alexandria x Baladiyat El-Mahalla: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- data diferente no ogol — Ghazl El-Mahalla x Al-Masry: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- data diferente no ogol — Suez Cement x ENPPI: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- data diferente no ogol — El-Mansoura x Zamalek: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- data diferente no ogol — Ismaily x Haras El-Hodoud: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- data diferente no ogol — Al-Ahly x El-Gaish: RSSSF 2004-11-29, ogol 2004-11-21; fica a da RSSSF
- placar diferente no ogol — Zamalek x Al-Ittihad de Alexandria (2004-12-15): RSSSF 3-0, ogol 3-1; fica o da RSSSF

### 2005/06

- ogol: 66 jogos casados (edição 37338 do ogol, 182 jogos)
- placar diferente no ogol — ENPPI x Aluminium (2005-08-30): RSSSF 2-1, ogol 3-0; fica o da RSSSF

### 2006/07

- ogol: 240 jogos casados (edição 1457 do ogol, 240 jogos)

### 2007/08

- ogol: 237 jogos casados (edição 1643 do ogol, 240 jogos)
- placar diferente no ogol — Aluminium x Suez Cement (2007-08-25): RSSSF 2-2, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Baladiyat El-Mahalla x Telecom Egypt (2007-09-14): RSSSF 0-2, ogol 1-2; fica o da RSSSF
- data diferente no ogol — Telecom Egypt x Al-Mokawloon Al-Arab: RSSSF 2007-12-07, ogol 2007-12-12; fica a da RSSSF
- placar diferente no ogol — Al-Masry x El-Gaish (2008-02-23): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- decidido fora de campo — Al-Masry Zamalek (2007-10-27): awarded 0-2; abandoned at 0-1 in 85'

### 2008/09

- ogol: 39 jogos casados (edição 2387 do ogol, 241 jogos)

### 2009/10

- ogol: 238 jogos casados (edição 9496 do ogol, 240 jogos)
- decidido fora de campo — El-Gouna Ghazl El-Mahalla (2009-12-03): awarded 0-2; originally 1-0,

### 2010/11

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (240 jogos)
- tabela publicada x jogos — egy2011:24: ENPPI tabela [30, 13, 8, 9, 37, 30] jogos [30, 14, 7, 9, 37, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy2011:24: Al-Masry tabela [30, 10, 13, 7, 28, 22] jogos [30, 10, 13, 7, 28, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy2011:24: El-Gaish tabela [30, 8, 12, 10, 25, 31] jogos [30, 8, 12, 10, 25, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy2011:24: Wadi Degla tabela [30, 9, 6, 15, 39, 49] jogos [30, 9, 6, 15, 39, 50] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy2011:24: Smouha tabela [30, 6, 10, 14, 33, 45] jogos [30, 6, 9, 15, 32, 45] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — egy2011:24: Al-Mokawloon Al-Arab tabela [30, 5, 9, 16, 27, 46] jogos [30, 5, 9, 16, 26, 46] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: ENPPI 1-0 Smouha (2011-05-03, ogol:1277675); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: ENPPI 2-1 Al-Mokawloon Al-Arab (2010-09-14, ogol:1277565); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Al-Masry 1-3 Smouha (2010-11-25, ogol:1277620); com 1-4 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: El-Gaish 0-1 Smouha (2011-06-24, ogol:1277731); com 0-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: El-Gaish 2-0 Al-Mokawloon Al-Arab (2010-11-25, ogol:1277621); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2011/12

- temporada abandonada em fevereiro de 2012, depois da tragédia do estádio de Port Said; nenhum título foi dado
- ogol: base dos jogos (143 jogos)
- jogo acrescentado à mão — Al-Masry 3-1 Al-Ahly: o jogo da tragédia do estádio de Port Said (74 mortos, depois do apito final); o ogol o marca como anulado, mas a tabela no abandono conta o 3-1
- corrigido — Al-Masry x Petrojet (2011-12-30): Al-Masry 0-0 Petrojet (30/12/2011): a tabela no abandono não conta este jogo (adiado); sem ele, os dois clubes fecham
- corrigido — Zamalek x Haras El-Hodoud (2011-12-30): Zamalek 0-0 Haras El-Hodoud (30/12/2011): a tabela no abandono não conta este jogo (adiado); sem ele, os dois clubes fecham
- corrigido — Zamalek x Ismaily (2012-02-01): Zamalek x Ismaily (1/2/2012): interrompido (o ogol traz 0-0); a tabela no abandono não o conta
- corrigido — Ismaily x Ghazl El-Mahalla (2012-03-06): Ismaily 0-0 Ghazl El-Mahalla (6/3/2012): jogo adiado da 10ª rodada, marcado depois do abandono; nunca foi jogado
- corrigido — Al-Ahly x Wadi Degla (2012-03-06): Al-Ahly 0-0 Wadi Degla (6/3/2012): jogo adiado da 10ª rodada, marcado depois do abandono; nunca foi jogado
- abandonado/suspenso, sem valer — Zamalek 0-0 Ismaily (2012-02-01)

### 2012/13

- temporada abandonada em julho de 2013 pela crise política; nenhum título foi dado (a RSSSF chama de 2013)
- ogol: 134 jogos casados (edição 66068 do ogol, 136 jogos)

### 2013/14

- ogol: 110 jogos casados (edição 66069 do ogol, 227 jogos)
- decidido fora de campo — Zamalek Haras El-Hodoud (2015-01-19): awarded 0-2; originally 1-1 but Zamalek had

### 2014/15

- ogol: 101 jogos casados (edição 74103 do ogol, 380 jogos)
- decidido fora de campo — Al-Mokawloon Al-Arab Al-Nasr do Cairo (2016-07-01): awarded 2-0, Nasr dns

### 2015/16

- ogol: 46 jogos casados (edição 91537 do ogol, 306 jogos)

### 2016/17

- ogol: 44 jogos casados (edição 99784 do ogol, 306 jogos)
- decidido fora de campo — Zamalek Misr Lel Makkasa (2018-04-16): awarded 0-2, Zamalek forfeited

### 2017/18

- ogol: 52 jogos casados (edição 114792 do ogol, 306 jogos)

### 2018/19

- ogol: 80 jogos casados (edição 125798 do ogol, 306 jogos)

### 2019/20

- ogol: 35 jogos casados (edição 137806 do ogol, 306 jogos)
- data diferente no ogol — ENPPI x El-Gaish: RSSSF 2019-09-26, ogol 2019-10-01; fica a da RSSSF
- data diferente no ogol — Haras El-Hodoud x Wadi Degla: RSSSF 2019-09-26, ogol 2019-10-01; fica a da RSSSF
- decidido fora de campo — Al-Ahly Zamalek (2020-02-24): awarded 2-0, Zamalek forfeited

### 2020/21

- ogol: 27 jogos casados (edição 149691 do ogol, 306 jogos)

### 2021/22

- ogol: 305 jogos casados (edição 159622 do ogol, 306 jogos)

### 2022/23

- ogol: 306 jogos casados (edição 169274 do ogol, 306 jogos)

### 2023/24

- ogol: 56 jogos casados (edição 177684 do ogol, 306 jogos)
- corrigido — Smouha x Pyramids (2025-06-28): Pyramids x Smouha (28/6/2025) foi interrompido aos 50' com 1-1 (incêndio no estádio) e completado em 2/7: fica só a linha da continuação, com o placar final
- corrigido — Smouha x Pyramids (2025-07-02): a página escreve o jogo em duas linhas (interrupção e continuação)
- decidido fora de campo — Al-Ahly Zamalek (2025-06-25): awarded 2-0, Zamalek forfeited

### 2024/25

- ogol: 45 jogos casados (edição 192143 do ogol, 225 jogos)
- decidido fora de campo — Modern Sport Ismaily (2026-01-01): awarded 0-3; originally 0-0
- decidido fora de campo — Zamalek Al-Ahly (2026-03-11): awarded 3-0, Ahly dns

### 2025/26

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: base dos jogos (322 jogos)

