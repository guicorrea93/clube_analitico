# Campeonato Egípcio (`egy-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/egy-1/pacote/`, do código `coleta/egy-1/` e do relatório `docs/coleta/egy-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 73, de 1948/49 a 2025/26; 13 sem jogos.
- **Jogos:** 11574 (11573 com placar); **gols:** 24475; **gols com autor:** 3068 (13%); **cartões:** 0.
- **Clubes:** 74; **artilheiros:** 58 edições com artilheiro (58 linhas, com empates).
- **Classificação final:** 70 edições; **tabelas publicadas guardadas para conferência:** 1079 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão egípcia (Egyptian Premier League) de 1948/49, a primeira liga nacional, a 2025/26. Sem as temporadas não disputadas (1951/52 e 1967/68 a 1970/71); as não terminadas (1954/55, 1971/72, 1973/74, 1989/90, 2011/12 e 2012/13) entram sem campeão. Sem a Copa do Egito, a Liga do Cairo e o campeonato da U.I.S.S.E. (1913-1914), que a federação não reconhece.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão egípcia (egy-1): a liga nacional, de 1948/49 (a primeira, criada por decreto real) a 2025/26.

Lista de campeões: RSSSF (egychamp.html, 67 títulos desde 1948/49), conferida com a Wikipédia em inglês. Ficam de fora
(pesquisa de 23/11/2026, registrada em coleta/comum-africa/COMECE-AQUI.md):
- o campeonato da U.I.S.S.E. (1912/13 a 1914): mata-mata entre clubes das colônias estrangeiras, que a federação
  egípcia (1921) não reconhece;
- a Liga do Cairo (1922/23 a 1957/58) e as outras ligas regionais (Alexandria, Canal, Bahary);
- as temporadas não disputadas: 1951/52 (Olimpíada de 1952) e 1967/68 a 1970/71 (Guerra dos Seis Dias).
As temporadas começadas e não terminadas entram como edição sem campeão, com o motivo na observação: 1954/55, 1971/72,
1973/74, 1989/90, 2011/12 e 2012/13. A RSSSF chama de 1970/71 a temporada interrompida pela briga em Al-Ahly x Zamalek;
o jogo foi em 24/12/1971 (Kooora; Wikipédia em inglês): é a 1971/72. A 2012/13 é a "2013" da RSSSF (começou em
fevereiro de 2013).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro (rsssf_africa.texto); linha final
  None: até o primeiro título de outra competição (FIM_PADRAO). Página egyAA (ou egyAAAA de 2010 em diante): a do ano em
  que a temporada termina (egy98 = 1997/98).
- ogol: os anos em que a RSSSF só tem a tabela final (1964/65 a 1996/97, 2010/11, 2011/12 e 2025/26): o calendário do
  ogol é a base (ogol_jogos), e as tabelas da página (tabelas) são a conferência.
- tabelas: trechos lidos só pelas tabelas (sem jogos).
Antes de 1964/65, a RSSSF só tem a tabela final (e, em alguns anos, só os resultados do Al-Ahly, sem data nem mando:
ficam de fora, como os "Known Results" do par-1) e o ogol não tem jogos: a edição entra com a tabela.
```

**Edições:** 73, uma por temporada da liga nacional (Egyptian Premier League), de 1948/49, a primeira, a 2025/26, como na lista de campeões da RSSSF (`egychamp.html`) e na Wikipédia em inglês. As temporadas não disputadas ficam de fora (1951/52, pela Olimpíada; 1967/68 a 1970/71, pela Guerra dos Seis Dias). As começadas e não terminadas entram sem campeão, com o motivo: 1954/55, 1971/72 (a RSSSF chama de 1970/71; a briga em Al-Ahly x Zamalek foi em 24/12/1971), 1973/74, 1989/90, 2011/12 e 2012/13 (a "2013" da RSSSF).

**Fontes:** RSSSF (uma página por temporada, `data/coleta/egy-1/rsssf/`: base dos jogos de 1997/98 a 2024/25, com rodadas, datas e autores dos gols; nos outros anos, a tabela final, que é a conferência); ogol (base dos jogos de 1964/65 a 1996/97, 2010/11, 2011/12 e 2025/26; nos outros anos, rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); Wikipédia em inglês (lista de campeões e de artilheiros, e a tabela final de cada temporada, terceira fonte nas divergências). De 1948/49 a 1963/64 nenhuma fonte pública tem os jogos: as edições entram com a tabela final (e com a final ou o desempate do título, quando a página traz). A ESPN não tem a liga egípcia.

**Clubes:** nomes árabes com hífen; o Al-Ahly fica com o nome puro; homônimos de clubes de outros países levam a cidade (Al-Ittihad de Alexandria, Al-Ittihad de Suez, Al-Nasr do Cairo, El-Merreikh de Port Said). Mesmo clube com outro nome é um só, com o nome atual (Farouk Club = Zamalek; Al-Assiouty = Pyramids; FC Masr = ZED; Future = Modern Sport; Ittihad Othman = Dina Farms; Al-Ma'aden = Goldy; Sawahel = Haras El-Hodoud). Regras em `coleta/egy-1/clubes_egy.py`.

**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada pela RSSSF (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos (erro de digitação da RSSSF). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Pontos por vitória como as tabelas contam: 2 até 1985/86, 3 de 1986/87 a 1989/90, 2 de 1990/91 a 1993/94 e 3 a partir de 1994/95.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 42.
- **Edições com alguma tabela divergente** (12; motivo no relatório, na edição): 1964/65, 1965/66, 1966/67, 1974/75, 1977/78, 1979/80, 1980/81, 1991/92, 1992/93, 1994/95, 1996/97, 2010/11.
- **Edições sem tabela para conferir** (19): 1948/49, 1949/50, 1950/51, 1952/53, 1953/54, 1954/55, 1955/56, 1956/57, 1957/58, 1958/59, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1971/72, 1973/74, 1975/76, 1989/90.
- **Edições com menos jogos que o esperado:** 1992/93 (181 de 182).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1940s | 2 | 6 | 83% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 9 | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 7 | 397 | 97% | 0% | 97% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 9 | 1204 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 1361 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 2121 | 100% | 0% | 100% | 0% | 0% | 0% | 9% | 0.0 |
| 2000s | 10 | 2055 | 100% | 0% | 100% | 0% | 0% | 0% | 56% | 0.0 |
| 2010s | 10 | 2657 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1771 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1948/49: 11 clubes
- 1949/50 a 1953/54: 10 clubes
- 1954/55: 0 clubes
- 1955/56: 11 clubes
- 1956/57: 14 clubes
- 1957/58: 16 clubes
- 1958/59 a 1961/62: 10 clubes
- 1962/63 a 1963/64: 24 clubes
- 1964/65 a 1966/67: 12 clubes
- 1971/72: 0 clubes
- 1972/73: 12 clubes
- 1973/74: 0 clubes
- 1974/75: 18 clubes
- 1975/76: 23 clubes
- 1976/77: 15 clubes
- 1977/78: 14 clubes
- 1978/79: 12 clubes
- 1979/80: 16 clubes
- 1980/81 a 1981/82: 14 clubes
- 1982/83 a 1988/89: 12 clubes
- 1989/90: 14 clubes
- 1990/91: 18 clubes
- 1991/92 a 1994/95: 14 clubes
- 1995/96 a 1997/98: 16 clubes
- 1998/99 a 2001/02: 14 clubes
- 2002/03: 15 clubes
- 2003/04 a 2005/06: 14 clubes
- 2006/07 a 2010/11: 16 clubes
- 2011/12: 19 clubes
- 2012/13: 18 clubes
- 2013/14: 22 clubes
- 2014/15: 20 clubes
- 2015/16 a 2024/25: 18 clubes
- 2025/26: 21 clubes

**Pontos por vitória:**

- 1948/49 a 1985/86: 2
- 1986/87 a 1989/90: 3
- 1990/91 a 1993/94: 2
- 1994/95 a 2025/26: 3

**Nome oficial:**

- 1948/49 a 2025/26: Egyptian Premier League

**Formato** (fases na ordem, do edicoes.csv):

- 1948/49: jogos incompletos (só 6 jogos da liga e o desempate do 2º lugar)
- 1949/50 a 1953/54: sem jogos (só a tabela final)
- 1954/55: temporada não terminada
- 1955/56 a 1956/57: sem jogos (só a tabela final)
- 1957/58: jogos incompletos (só a final entre os vencedores dos grupos)
- 1958/59 a 1961/62: sem jogos (só a tabela final)
- 1962/63: jogos incompletos (só o desempate do grupo B e o quadrangular final)
- 1963/64: jogos incompletos (só a final entre os vencedores dos grupos)
- 1964/65 a 1966/67: pontos corridos
- 1971/72: temporada não terminada
- 1972/73: pontos corridos
- 1973/74: temporada não terminada
- 1974/75: pontos corridos
- 1975/76: jogos incompletos (só a final entre os vencedores dos grupos)
- 1976/77 a 1988/89: pontos corridos
- 1989/90: temporada não terminada
- 1990/91: pontos corridos + desempate
- 1991/92 a 1992/93: pontos corridos
- 1993/94: pontos corridos + desempate
- 1994/95 a 1996/97: pontos corridos
- 1997/98 a 1998/99: pontos corridos + desempate
- 1999/00 a 2001/02: pontos corridos
- 2002/03: pontos corridos + desempate
- 2003/04 a 2007/08: pontos corridos
- 2008/09: pontos corridos + desempate
- 2009/10 a 2010/11: pontos corridos
- 2011/12 a 2012/13: temporada não terminada
- 2013/14: 2 grupos + desempate + fase final
- 2014/15 a 2023/24: pontos corridos
- 2024/25 a 2025/26: pontos corridos + grupos do título e do rebaixamento

**Fases e grupos de cada edição com mais de uma fase:**

- 1948/49: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 1962/63: Primeira fase (liga); Desempate do grupo B (liga); Fase final (liga)
- 1990/91: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1993/94: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1997/98: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1998/99: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 2002/03: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 2008/09: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 2013/14: Primeira fase (grupos, 2 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Fase final (liga)
- 2024/25: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 2025/26: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 69 edições
- calculada: 1 edições

**Observações das edições:**

- 1954/55: temporada não terminada: o Al-Ahly brigou com a federação e saiu do campeonato; nenhum título foi dado
- 1964/65: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1965/66: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1966/67: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1971/72: temporada não terminada: suspensa depois da briga e da invasão de campo em Al-Ahly x Zamalek (24/12/1971); nenhum título foi dado (a RSSSF chama esta temporada de 1970/71)
- 1972/73: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1973/74: temporada não terminada: suspensa pela Guerra do Yom Kippur (outubro de 1973); no lugar dela houve a Copa Outubro, que não conta como título da liga
- 1974/75: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1976/77: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1977/78: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1978/79: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1979/80: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1980/81: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1981/82: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1982/83: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1983/84: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1984/85: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1985/86: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1986/87: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1987/88: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1988/89: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1989/90: temporada não terminada: suspensa para a preparação da seleção para a Copa do Mundo de 1990; nenhum título foi dado
- 1990/91: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1991/92: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1992/93: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1993/94: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1994/95: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1995/96: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 1996/97: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 2010/11: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- 2011/12: temporada abandonada em fevereiro de 2012, depois da tragédia do estádio de Port Said; nenhum título foi dado
- 2012/13: temporada abandonada em julho de 2013 pela crise política; nenhum título foi dado (a RSSSF chama de 2013)
- 2025/26: a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Al-Ahly: 45
- Zamalek: 15
- Ismaily: 3
- Tersana: 1
- Olympic Club: 1
- Ghazl El-Mahalla: 1
- Al-Mokawloon Al-Arab: 1
- Sem campeão: 1954/55, 1971/72, 1973/74, 1989/90, 2011/12, 2012/13

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1948/49 | Al-Ahly | Tersana |
| 1949/50 | Al-Ahly | Tersana |
| 1950/51 | Al-Ahly | Zamalek |
| 1952/53 | Al-Ahly | Zamalek |
| 1953/54 | Al-Ahly | Zamalek |
| 1954/55 | — | — |
| 1955/56 | Al-Ahly | Zamalek |
| 1956/57 | Al-Ahly | Zamalek |
| 1957/58 | Al-Ahly | Zamalek |
| 1958/59 | Al-Ahly | Zamalek |
| 1959/60 | Zamalek | Tersana |
| 1960/61 | Al-Ahly | Zamalek |
| 1961/62 | Al-Ahly | Zamalek |
| 1962/63 | Tersana | Zamalek |
| 1963/64 | Zamalek | Tersana |
| 1964/65 | Zamalek | Ismaily |
| 1965/66 | Olympic Club | Zamalek |
| 1966/67 | Ismaily | Al-Ahly |
| 1971/72 | — | — |
| 1972/73 | Ghazl El-Mahalla | Zamalek |
| 1973/74 | — | — |
| 1974/75 | Al-Ahly | Tersana |
| 1975/76 | Al-Ahly | Ghazl El-Mahalla |
| 1976/77 | Al-Ahly | Zamalek |
| 1977/78 | Zamalek | Al-Ahly |
| 1978/79 | Al-Ahly | Zamalek |
| 1979/80 | Al-Ahly | Zamalek |
| 1980/81 | Al-Ahly | Zamalek |
| 1981/82 | Al-Ahly | Zamalek |
| 1982/83 | Al-Mokawloon Al-Arab | Zamalek |
| 1983/84 | Zamalek | Al-Ahly |
| 1984/85 | Al-Ahly | Zamalek |
| 1985/86 | Al-Ahly | Zamalek |
| 1986/87 | Al-Ahly | Zamalek |
| 1987/88 | Zamalek | Al-Ahly |
| 1988/89 | Al-Ahly | Zamalek |
| 1989/90 | — | — |
| 1990/91 | Ismaily | Al-Ahly |
| 1991/92 | Zamalek | Ismaily |
| 1992/93 | Zamalek | Al-Ahly |
| 1993/94 | Al-Ahly | Ismaily |
| 1994/95 | Al-Ahly | Zamalek |
| 1995/96 | Al-Ahly | Zamalek |
| 1996/97 | Al-Ahly | Zamalek |
| 1997/98 | Al-Ahly | Zamalek |
| 1998/99 | Al-Ahly | Zamalek |
| 1999/00 | Al-Ahly | Ismaily |
| 2000/01 | Zamalek | Al-Ahly |
| 2001/02 | Ismaily | Al-Ahly |
| 2002/03 | Zamalek | Al-Ahly |
| 2003/04 | Zamalek | Al-Ahly |
| 2004/05 | Al-Ahly | ENPPI |
| 2005/06 | Al-Ahly | Zamalek |
| 2006/07 | Al-Ahly | Zamalek |
| 2007/08 | Al-Ahly | Ismaily |
| 2008/09 | Al-Ahly | Ismaily |
| 2009/10 | Al-Ahly | Zamalek |
| 2010/11 | Al-Ahly | Zamalek |
| 2011/12 | — | — |
| 2012/13 | — | — |
| 2013/14 | Al-Ahly | Smouha |
| 2014/15 | Zamalek | Al-Ahly |
| 2015/16 | Al-Ahly | Zamalek |
| 2016/17 | Al-Ahly | Misr Lel Makkasa |
| 2017/18 | Al-Ahly | Ismaily |
| 2018/19 | Al-Ahly | Zamalek |
| 2019/20 | Al-Ahly | Zamalek |
| 2020/21 | Zamalek | Al-Ahly |
| 2021/22 | Zamalek | Pyramids |
| 2022/23 | Al-Ahly | Pyramids |
| 2023/24 | Al-Ahly | Pyramids |
| 2024/25 | Al-Ahly | Pyramids |
| 2025/26 | Zamalek | Pyramids |

**Rebaixados marcados na classificação:** 130 em 43 edições (só onde a tabela publicada marca a queda); quem mais caiu: Tanta (6), El-Koroum (6), Tersana (6), El-Mansoura (6), El-Minya (5).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1975/76: Ittihad El-Shorta -6
- 1998/99: Zamalek -9
- 2003/04: ENPPI -1
- 2014/15: Ismaily -6
- 2014/15: Al-Nasr do Cairo -3
- 2016/17: Zamalek -3
- 2019/20: Zamalek -3
- 2020/21: Ismaily -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/egy-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 8)

- **1948/49 · egy49:43:** [data = None] desempate do 2º lugar sem data na página (a data lida era a da rodada de cima)
- **2023/24 · egy2024:479:** [descartado] Pyramids x Smouha (28/6/2025) foi interrompido aos 50' com 1-1 (incêndio no estádio) e completado em 2/7: fica só a linha da continuação, com o placar final
- **2023/24 · egy2024:485:** [nota = interrompido aos 50' com 1-1 em 28/6/2025 (incêndio no estádio); os 40 minutos que faltavam foram jogados em 2/7/2025] a página escreve o jogo em duas linhas (interrupção e continuação)
- **2011/12 · ogol:6940584:** [descartado] Ismaily 0-0 Ghazl El-Mahalla (6/3/2012): jogo adiado da 10ª rodada, marcado depois do abandono; nunca foi jogado
- **2011/12 · ogol:6940585:** [descartado] Al-Ahly 0-0 Wadi Degla (6/3/2012): jogo adiado da 10ª rodada, marcado depois do abandono; nunca foi jogado
- **2011/12 · ogol:6940640:** [abandonado] Zamalek x Ismaily (1/2/2012): interrompido (o ogol traz 0-0); a tabela no abandono não o conta
- **2011/12 · ogol:6940586:** [descartado] Al-Masry 0-0 Petrojet (30/12/2011): a tabela no abandono não conta este jogo (adiado); sem ele, os dois clubes fecham
- **2011/12 · ogol:6940587:** [descartado] Zamalek 0-0 Haras El-Hodoud (30/12/2011): a tabela no abandono não conta este jogo (adiado); sem ele, os dois clubes fecham

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 12)

- **1962/63:** Ismaily 0-1 Tersana (Desempate do grupo B, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Ismaily 0-1 Zamalek (Desempate do grupo B, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Tersana 0-1 Zamalek (Desempate do grupo B, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Al-Ahly 1-1 Qanah (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Al-Ahly 0-2 Tersana (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Al-Ahly 1-1 Zamalek (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Qanah 1-2 Tersana (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Qanah 1-2 Zamalek (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1962/63:** Tersana 3-3 Zamalek (Fase final, egy63: tabela cruzada (cada par jogou uma vez, sem data; a ordem é a da tabela, linha x coluna)) 
- **1990/91:** Al-Ahly 1-0 Ismaily (, egy91: tabela final e a lista de resultados do Ismaily ("2 losses: Ahly, Tersana")) jogo do turno que falta no ogol (o Ismaily x Al-Ahly da 24ª rodada foi 1-1); o placar 1-0 sai da tabela
- **2011/12:** Al-Masry 3-1 Al-Ahly (, egy2012: tabela no abandono (a Wikipédia traz a mesma)) o jogo da tragédia do estádio de Port Said (74 mortos, depois do apito final); o ogol o marca como anulado, mas a tabela no abandono conta o 3-1
- **1993/94:** Al-Ahly 1-1 Ismaily (, egy94: tabela final) jogo do returno que falta no ogol (o da 6ª rodada também foi 1-1); o placar sai da tabela

### Divergências entre fontes já explicadas (`EXPLICACOES`, 2)

- **1992/93:** a tabela da RSSSF dá 26 jogos a El-Merreikh e El-Minya, com uma derrota a mais para cada um (e 5 gols sofridos a mais para o Merreikh); o ogol e a tabela da Wikipédia dão 25 jogos aos dois. O jogo entre eles não aparece em nenhuma fonte de jogos (provavelmente decidido fora de campo, com derrota para os dois). A classificação usa os números dos jogos; faltam 1 dos 182 jogos esperados pela tabela da RSSSF
- **1974/75:** a tabela da RSSSF troca os números de Plastic e Suez (12º e 13º, os dois com 28 pontos); o ogol e a tabela da Wikipédia dão a cada um os seus. A classificação usa os números dos jogos

### Identidade dos clubes

Regras em `coleta/egy-1/clubes_egy.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes egípcios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1 (23/11/2026):
- nomes árabes sempre com hífen; fica com o nome puro o clube mais conhecido no Brasil (Al-Ahly); os outros levam a cidade
  quando há outro igual no mundo: "Al-Ittihad de Alexandria" (o Al-Ittihad é o da Arábia Saudita), "Al-Ittihad de Suez",
  "Al-Nasr do Cairo" (o Al-Nassr é o saudita), "El-Merreikh de Port Said" (o Al-Merrikh é o do Sudão);
- a grafia segue o nome mais usado em inglês (Wikipédia), com hífen no artigo: "Ghazl El-Mahalla", "Haras El-Hodoud",
  "El-Gouna", "Al-Mokawloon Al-Arab";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Farouk Club / King Farouk Club (até 1952) e El-Mokhtalat -> Zamalek;
  - Sawahel (Guarda Costeira, 1963-1964) -> Haras El-Hodoud (Guarda de Fronteira; o ogol trata como o mesmo clube);
  - Al-Assiouty Sport (2014-2017) -> Pyramids (comprado e renomeado em 2018; o ogol trata como o mesmo clube);
  - Ittihad Othman (até 1996/97) -> Dina Farms (a RSSSF de 1997/98: "new name for Ittihad Othman");
  - Al-Ma'aden (até 2000/01) -> Goldy (a RSSSF de 2001/02: "changed name to Goldy");
  - FC Masr (2019) -> ZED (renomeado em 2022; o ogol trata como o mesmo clube);
  - Future FC / Modern Future (2021-2023) -> Modern Sport (o ogol trata como o mesmo clube);
  - Itesalat (2007-2008) -> Telecom Egypt; Al-Shourta (1975/76, "aka Police") -> Ittihad El-Shorta (o clube da polícia);
  - Suez El-Riyadi -> Suez; Qanah / Canal / Qanat (Port Said) -> El-Qanah (o ogol tem um só código de 1964 a 2013);
  - Ala'ab Damanhour (2013/14) -> Damanhour (o ogol trata como o mesmo clube);
  - Tersana também aparece como "Arsenal" (1990/91); El-Gaish (Tala'ea El-Gaish, o clube do Exército) como "Al-Jaish" e
    "Army Club".
- "Mahala"/"Mehalla"/"Al Mehalla" sozinho é o Ghazl El-Mahalla; o Baladiyat El-Mahalla vem sempre com "Baladeya",
  "Baladia" ou "Baladiyyat" (ou "B Mehalla").

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** (pesquisa de 23/11/2026): o campeonato da U.I.S.S.E. (1912/13 a 1914), mata-mata entre clubes das colônias estrangeiras que a federação egípcia não reconhece; a Liga do Cairo (1922/23 a 1957/58) e as outras ligas regionais; a Copa do Egito, a Supercopa e a Copa da Liga.
- **Edições sem jogos** (13): 1949/50, 1950/51, 1952/53, 1953/54, 1954/55, 1955/56, 1956/57, 1958/59, 1959/60, 1960/61, 1961/62, 1971/72, 1973/74.
- **Décadas com menos da metade dos gols com autor:** 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Ainda não carregado no banco (pacote pronto em 23/11/2026; teste de carga OK).
- 1948/49 a 1963/64 sem jogos (nenhuma fonte pública tem): só a tabela final, e a final ou o desempate do título quando a página da RSSSF traz (1948/49, 1957/58, 1962/63, 1963/64, 1975/76). As listas "Results Ahly" (só os jogos do Al-Ahly, sem data nem mando) ficaram de fora. Fonte que resolveria: o site do Dr. Tarek Said (drtareksaid.net, arquivado) ou jornais egípcios da época.
- 1954/55, 1971/72 e 1973/74 (não terminadas): nenhuma fonte tem jogos nem tabela; entram só com a observação.
- Autores dos gols só onde a RSSSF traz (1998/99 a 2006/07, nem sempre a temporada inteira); de 2007/08 em diante a página não tem autores e a ESPN não cobre a liga. Fonte que resolveria: o ogol jogo a jogo (página de cada partida).
- Divergências entre a tabela da RSSSF e os jogos do ogol sem terceira fonte (1979/80, 1980/81) e as que a Wikipédia confirma a tabela (1977/78 Zamalek, 1991/92 Damanhour 0-0 Zamalek = 1-2?, 2010/11): o jogo provável está no relatório; nenhum placar foi mudado.
- Identidade a conferir: o "Sohag Railways" de 2000/01 e o "Sohag" de 2001/02 entraram como um clube só; o Al-Shourta de 1975/76 entrou como Ittihad El-Shorta; o "Suez Club" do ogol é o Ittihad Suez só em 1965/66.

## 10. Arquivos e comandos

Código em `coleta/egy-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão egípcia no ogol para data/coleta/egy-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão egípcia para data/coleta/egy-1/rsssf/: a lista de campeões (egychamp.html), as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Egyptian Premier League", lista de campeões) e o de |
| `clubes_egy.py` | Identidade dos clubes egípcios: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão egípcia (egy-1): a liga nacional, de 1948/49 (a primeira, criada por decreto real) a 2025/26. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão egípcia, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão egípcia e grava o pacote em data/coleta/egy-1/pacote/ e o relatório em docs/coleta/egy-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/egy-1/rsssf/) com o leitor comum (rsssf_africa) |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/egy-1/wikipedia/en_<temporada>.txt). |

- Fontes baixadas: `data/coleta/egy-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-egy-1/`.
- Pacote: `data/coleta/egy-1/pacote/`; relatório: `docs/coleta/egy-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/egy-1/baixar_ogol.py
python coleta/egy-1/baixar_rsssf.py
python coleta/egy-1/baixar_wikipedia.py
python coleta/egy-1/importar.py
python coleta/egy-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py egy-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

