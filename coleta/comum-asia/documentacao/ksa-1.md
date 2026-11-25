# Campeonato Saudita (`ksa-1`) — documentação

Gerado por `python coleta/comum-asia/documentar.py` a partir do pacote `data/coleta/ksa-1/pacote/`, do código `coleta/ksa-1/` e do relatório `docs/coleta/ksa-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 69, de 1957/58 a 2025/26; 12 sem jogos.
- **Jogos:** 5965 (5965 com placar); **gols:** 17178; **gols com autor:** 7296 (42%); **cartões:** 4801.
- **Clubes:** 43; **artilheiros:** 14 edições com artilheiro (14 linhas, com empates).
- **Classificação final:** 66 edições; **tabelas publicadas guardadas para conferência:** 670 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** His Majesty's League (1957/58-1973/74, mata-mata), Liga de Classificação (1974/75), Premier League (1975/76-2006/07) e Pro League (2007/08 em diante), como o relatório oficial da federação (2025)

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições do Campeonato Saudita: as 69 temporadas da lista oficial (relatório da federação de 2025, como a Wikipédia em
inglês o reproduz: campeoes_wiki.py), de 1957/58 a 2025/26. Decisão do Guilherme (24/11/2026): desde 1957.

Eras:
- 1957/58 a 1973/74, "His Majesty's League": torneio mata-mata (os campeões são os da antiga Copa do Rei). Entra o
  campeão e o vice; o jogo da final quando a lista da Copa do Rei da RSSSF (saucuphist.html) tem o mesmo par de clubes.
  1966/67 não concluída, 1967/68 não disputada, 1969/70 cancelada: edições sem campeão.
- 1974/75, Liga de Classificação: dois grupos de 8 e final entre os primeiros.
- 1975/76: liga abandonada no meio (cancelada; edição sem campeão, com os jogos que a RSSSF tem).
- 1976/77 em diante, Premier League / Pro League: pontos corridos. 1981/82: dois grupos de 10 e playoff (semifinais,
  3º lugar e final). 1985/86: dois grupos de 6 e grupos finais (título, classificação, rebaixamento). 1990/91 a 2006/07
  ("Golden Box"): liga e playoff dos 4 primeiros; até 2000/01 semifinais (ida e volta até 1999/00) e final; de 2001/02 em
  diante escadinha (3º x 4º, o vencedor x o 2º, o vencedor x o 1º na final).

Fontes dos jogos: RSSSF (sauNN.html; jogos da liga em 1974/75, 1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e
1997/98-2006/07, com autores até 2005/06; playoffs de todos os anos que têm), ogol (fase de liga de 1999/00 em diante:
a fonte dos jogos de 2006/07 em diante e das temporadas que a RSSSF não tem completas), ESPN (2022/23 em diante: autores,
cartões, estádio, público e hora).
```

**Edições:** 69, as temporadas da lista oficial de campeões, de 1957/58 a 2025/26, como o relatório da federação saudita de 2025 (reproduzido pela Wikipédia em inglês, página "Saudi Pro League"): Al-Hilal 21 títulos, Al-Ittihad 14, Al-Nassr 11, Al-Ahli 9. Decisão do Guilherme (24/11/2026): desde 1957, como a federação conta (a RSSSF conta desde 1974/75). Eras: "His Majesty's League" (1957/58-1973/74, mata-mata; os campeões são os da antiga Copa do Rei), Liga de Classificação (1974/75, dois grupos e final), Premier League (1975/76-2006/07; de 1990/91 a 2006/07 o título era decidido num playoff dos 4 primeiros, o "Golden Box") e Pro League (2007/08 em diante). 1966/67 (não concluída), 1967/68 (não disputada), 1969/70 e 1975/76 (canceladas) entram sem campeão. 2026/27 entra quando acabar.

**Fontes:** RSSSF (uma página por temporada, `sauNN.html`, e a lista da Copa do Rei, `saucuphist.html`, em `data/coleta/ksa-1/rsssf/`: tabela final de todos os anos de 1974/75 em diante, os jogos da fase de liga em 1974/75, 1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e 1997/98-2024/25, os jogos do playoff e os autores dos gols até 2005/06); ogol (calendário de 1999/00 a 2025/26, só a fase de liga: `data/coleta/ksa-1/ogol/` e `data/cache/ogol-ksa-1/`, para os escudos); ESPN (liga `ksa.1`, 2022/23 a 2025/26: autores dos gols, cartões, estádio, público e hora, `data/coleta/ksa-1/espn/`); Wikipédia em inglês (lista oficial de campeões e vices; matrizes de resultados de 2010/11 e 2011/12 nas correções).

**Clubes:** 43. Nome árabe com hífen; Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab com o nome puro (combinado entre os agentes); os homônimos de clubes de outros países com a cidade (Al-Ahli de Jeddah, Al-Wehda de Meca, Al-Qadsiah de Khobar, Al-Faisaly de Harmah, Al-Khaleej de Saihat, Al-Nahda de Dammam, Al-Ansar de Medina, Al-Najma de Unaizah, Al-Orobah de Sakakah, Al-Arabi de Unaizah, Al-Ain de Al-Baha). As grafias de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em `coleta/ksa-1/clubes_ksa.py`).

**Regras:** placar oficial, com a prorrogação; jogos decididos fora de campo (`awd`) com o placar dado e o de campo na observação. Os jogos da fase de liga vêm da RSSSF até 2005/06 quando ela tem a fase completa e do ogol nos outros anos (1999/00 em diante); o playoff do título vem sempre da RSSSF. Anos sem os jogos na RSSSF nem no ogol (1977/78-1979/80, 1984/85, 1985/86, 1987/88-1996/97): só a tabela final (e os jogos do playoff que a RSSSF tem). Classificação final: a tabela da fase de liga da RSSSF, com o campeão e o vice oficiais em cima; os números são só da fase de liga (sem o playoff); nos anos em que a RSSSF dá só jogos e pontos (1977/78-1981/82) ou só a ordem (1985/86), o resto fica vazio. Pontos por vitória: 2 até 1992/93, 3 de 1993/94 em diante (tirado das tabelas). `ajuste_pontos`: punições e bônus da tabela da RSSSF. Rebaixado: o marcado na tabela da RSSSF. 1957/58-1973/74: campeão e vice da lista oficial; o jogo da final da Copa do Rei da RSSSF quando ela tem o mesmo par (o rótulo da temporada às vezes é o anterior). Artilheiro: o da lista da página da RSSSF; sem ela, a soma dos gols com autor quando ao menos 95% dos gols têm autor.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 35.
- **Edições com alguma tabela divergente** (8; motivo no relatório, na edição): 1997/98, 1999/00, 2001/02, 2003/04, 2007/08, 2009/10, 2011/12, 2018/19.
- **Edições sem tabela para conferir** (26): 1957/58, 1958/59, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1964/65, 1965/66, 1966/67, 1967/68, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1975/76, 1977/78, 1978/79, 1979/80, 1984/85, 1985/86, 1987/88, 1988/89, 1989/90.
- **Edições com menos jogos que o esperado:** 1974/75 (113 de 112), 1975/76 (16 de 56), 1981/82 (4 de 180), 1990/91 (6 de 132), 1991/92 (5 de 132), 1992/93 (5 de 132), 1993/94 (3 de 132), 1994/95 (2 de 132), 1995/96 (5 de 132), 1996/97 (6 de 132), 1997/98 (138 de 132), 1998/99 (137 de 132), 1999/00 (137 de 132), 2000/01 (137 de 132), 2001/02 (135 de 132), 2002/03 (135 de 132), 2003/04 (135 de 132), 2004/05 (135 de 132), 2005/06 (135 de 132), 2006/07 (135 de 132).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 3 | 3 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 6 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 189 | 98% | 0% | 96% | 0% | 0% | 0% | 16% | 0.0 |
| 1980s | 10 | 406 | 99% | 0% | 99% | 0% | 0% | 0% | 94% | 0.0 |
| 1990s | 10 | 444 | 96% | 0% | 89% | 0% | 0% | 0% | 57% | 0.0 |
| 2000s | 10 | 1343 | 100% | 0% | 98% | 0% | 0% | 0% | 55% | 0.0 |
| 2010s | 10 | 1936 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1638 | 100% | 71% | 100% | 71% | 0% | 70% | 71% | 2.9 |

Árbitro: só onde a fonte tem (na J1, na observação de cada jogo). Estatísticas (chutes, faltas, escanteios) não são coletadas.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1957/58 a 1973/74:  clubes
- 1974/75: 16 clubes
- 1975/76 a 1976/77: 8 clubes
- 1977/78 a 1980/81: 10 clubes
- 1981/82: 20 clubes
- 1982/83 a 1983/84: 10 clubes
- 1984/85 a 2009/10: 12 clubes
- 2010/11 a 2017/18: 14 clubes
- 2018/19 a 2022/23: 16 clubes
- 2023/24 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1957/58 a 1973/74: 
- 1974/75 a 1976/77: 2
- 1977/78 a 1979/80: 
- 1980/81: 2
- 1981/82: 
- 1982/83 a 1984/85: 2
- 1985/86: 
- 1986/87 a 1992/93: 2
- 1993/94 a 2025/26: 3

**Nome oficial:**

- 1957/58 a 1973/74: His Majesty's League <ano>
- 1974/75: Saudi Categorization League <ano>
- 1975/76 a 2006/07: Saudi Premier League <ano>
- 2007/08 a 2025/26: Saudi Pro League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1957/58 a 1973/74: mata-mata (His Majesty's League)
- 1974/75: dois grupos de 8 e final
- 1975/76: pontos corridos (8 clubes), abandonado
- 1976/77: pontos corridos, 8 clubes
- 1977/78 a 1980/81: pontos corridos, 10 clubes
- 1981/82: dois grupos de 10 e playoff (semifinais, 3º lugar e final)
- 1982/83 a 1983/84: pontos corridos, 10 clubes
- 1984/85: pontos corridos, 12 clubes
- 1985/86: dois grupos de 6 e grupos finais (título, classificação, rebaixamento)
- 1986/87 a 1989/90: pontos corridos, 12 clubes
- 1990/91 a 2006/07: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros
- 2007/08 a 2009/10: pontos corridos, 12 clubes
- 2010/11 a 2017/18: pontos corridos, 14 clubes
- 2018/19 a 2022/23: pontos corridos, 16 clubes
- 2023/24 a 2025/26: pontos corridos, 18 clubes

**Fases e grupos de cada edição com mais de uma fase:**

- 1974/75: Liga (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 1981/82: Liga (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1990/91: Liga (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1991/92: Liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1992/93: Liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1993/94: Liga (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1994/95: Liga (liga); Semifinal (mata_mata, jogo_unico)
- 1995/96: Liga (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico)
- 1996/97: Liga (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1997/98: Liga (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1998/99: Liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1999/00: Liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2000/01: Liga (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2001/02: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2002/03: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2003/04: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2004/05: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2005/06: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2006/07: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 52 edições
- lista oficial: 14 edições

**Observações das edições:**

- 1966/67: temporada não concluída (lista oficial)
- 1967/68: temporada não disputada (lista oficial)
- 1968/69: a RSSSF não tem a final com esse par de clubes (só campeão e vice da lista oficial)
- 1969/70: temporada cancelada (lista oficial)
- 1974/75: Al-Ansar de Medina: +2 ponto(s) na tabela da RSSSF (punição ou bônus)
- 1975/76: temporada abandonada no meio (lista oficial: cancelada); jogos e tabela até a parada, sem campeão
- 1994/95: a RSSSF não tem o jogo da final; campeão e vice da lista oficial
- 1995/96: a RSSSF não tem o jogo da final; campeão e vice da lista oficial
- 1999/00: Al-Wehda de Meca: -1 ponto(s) na tabela da RSSSF (punição ou bônus); Al-Tai: -1 ponto(s) na tabela da RSSSF (punição ou bônus)
- 2000/01: Al-Hilal: -3 ponto(s) na tabela da RSSSF (punição ou bônus)
- 2010/11: Al-Taawoun: -3 ponto(s) na tabela da RSSSF (punição ou bônus); Al-Wehda de Meca: -3 ponto(s) na tabela da RSSSF (punição ou bônus)
- 2016/17: Al-Ittihad: -3 ponto(s) na tabela da RSSSF (punição ou bônus)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Al-Hilal: 21
- Al-Ittihad: 14
- Al-Nassr: 11
- Al-Ahli de Jeddah: 9
- Al-Shabab: 6
- Al-Ettifaq: 2
- Al-Wehda de Meca: 1
- Al-Fateh: 1
- Sem campeão: 1966/67, 1967/68, 1969/70, 1975/76

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1957/58 | Al-Wehda de Meca | Al-Ittihad |
| 1958/59 | Al-Ittihad | Al-Wehda de Meca |
| 1959/60 | Al-Ittihad | Al-Wehda de Meca |
| 1960/61 | Al-Ittihad | Al-Wehda de Meca |
| 1961/62 | Al-Hilal | Al-Wehda de Meca |
| 1962/63 | Al-Ahli de Jeddah | Al-Riyadh |
| 1963/64 | Al-Ittihad | Al-Hilal |
| 1964/65 | Al-Hilal | Al-Ittihad |
| 1965/66 | Al-Ahli de Jeddah | Al-Ettifaq |
| 1966/67 | — | — |
| 1967/68 | — | — |
| 1968/69 | Al-Ahli de Jeddah | Al-Ettifaq |
| 1969/70 | — | — |
| 1970/71 | Al-Ahli de Jeddah | Al-Wehda de Meca |
| 1971/72 | Al-Ahli de Jeddah | Al-Nassr |
| 1972/73 | Al-Ahli de Jeddah | Al-Nassr |
| 1973/74 | Al-Nassr | Al-Ahli de Jeddah |
| 1974/75 | Al-Nassr | Al-Hilal |
| 1975/76 | — | — |
| 1976/77 | Al-Hilal | Al-Nassr |
| 1977/78 | Al-Ahli de Jeddah | Al-Nassr |
| 1978/79 | Al-Hilal | Al-Nassr |
| 1979/80 | Al-Nassr | Al-Hilal |
| 1980/81 | Al-Nassr | Al-Hilal |
| 1981/82 | Al-Ittihad | Al-Shabab |
| 1982/83 | Al-Ettifaq | Al-Hilal |
| 1983/84 | Al-Ahli de Jeddah | Al-Ittihad |
| 1984/85 | Al-Hilal | Al-Shabab |
| 1985/86 | Al-Hilal | Al-Ittihad |
| 1986/87 | Al-Ettifaq | Al-Hilal |
| 1987/88 | Al-Hilal | Al-Ettifaq |
| 1988/89 | Al-Nassr | Al-Shabab |
| 1989/90 | Al-Hilal | Al-Ahli de Jeddah |
| 1990/91 | Al-Shabab | Al-Nassr |
| 1991/92 | Al-Shabab | Al-Ettifaq |
| 1992/93 | Al-Shabab | Al-Hilal |
| 1993/94 | Al-Nassr | Al-Riyadh |
| 1994/95 | Al-Nassr | Al-Hilal |
| 1995/96 | Al-Hilal | Al-Ahli de Jeddah |
| 1996/97 | Al-Ittihad | Al-Hilal |
| 1997/98 | Al-Hilal | Al-Shabab |
| 1998/99 | Al-Ittihad | Al-Ahli de Jeddah |
| 1999/00 | Al-Ittihad | Al-Ahli de Jeddah |
| 2000/01 | Al-Ittihad | Al-Nassr |
| 2001/02 | Al-Hilal | Al-Ittihad |
| 2002/03 | Al-Ittihad | Al-Ahli de Jeddah |
| 2003/04 | Al-Shabab | Al-Ittihad |
| 2004/05 | Al-Hilal | Al-Shabab |
| 2005/06 | Al-Shabab | Al-Hilal |
| 2006/07 | Al-Ittihad | Al-Hilal |
| 2007/08 | Al-Hilal | Al-Ittihad |
| 2008/09 | Al-Ittihad | Al-Hilal |
| 2009/10 | Al-Hilal | Al-Ittihad |
| 2010/11 | Al-Hilal | Al-Ittihad |
| 2011/12 | Al-Shabab | Al-Ahli de Jeddah |
| 2012/13 | Al-Fateh | Al-Hilal |
| 2013/14 | Al-Nassr | Al-Hilal |
| 2014/15 | Al-Nassr | Al-Ahli de Jeddah |
| 2015/16 | Al-Ahli de Jeddah | Al-Hilal |
| 2016/17 | Al-Hilal | Al-Ahli de Jeddah |
| 2017/18 | Al-Hilal | Al-Ahli de Jeddah |
| 2018/19 | Al-Nassr | Al-Hilal |
| 2019/20 | Al-Hilal | Al-Nassr |
| 2020/21 | Al-Hilal | Al-Shabab |
| 2021/22 | Al-Hilal | Al-Ittihad |
| 2022/23 | Al-Ittihad | Al-Nassr |
| 2023/24 | Al-Hilal | Al-Nassr |
| 2024/25 | Al-Ittihad | Al-Hilal |
| 2025/26 | Al-Nassr | Al-Hilal |

**Rebaixados marcados na classificação:** 111 em 43 edições (só onde a tabela publicada marca a queda); quem mais caiu: Ohod (9), Al-Wehda de Meca (9), Al-Raed (8), Al-Ansar de Medina (7), Al-Tai (6).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1974/75: Al-Ansar de Medina +2
- 1999/00: Al-Wehda de Meca -1
- 1999/00: Al-Tai -1
- 2000/01: Al-Hilal -3
- 2010/11: Al-Taawoun -3
- 2010/11: Al-Wehda de Meca -3
- 2016/17: Al-Ittihad -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ksa-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Linhas da tabela da RSSSF que não fecham com os jogos (e a prova) (`TABELA_RSSSF`, 1)

- **2002:** A página da RSSSF não tem o jogo adiado Al-Ettifaq 2-1 Al-Shabab (05/04/2002, no ogol) e a tabela dela conta 21 jogos para os dois clubes; com o jogo, os dois fecham com 22.

### Jogos do ogol corrigidos (com a prova) (`OGOL_CORRIGE`, 2)

- **1898735:** [mandante = Hajer] o ogol dá Al-Hilal 1-0 Najran em 31/03/2012 (rodada 24), mas o Al-Hilal já jogou na rodada (Al-Fateh 0-5 Al-Hilal), recebe o Najran outra vez em 09/12/2011 e falta o Hajer x Najran: é Hajer 1-0 Najran (Wikipédia, 2011–12 Saudi Professional League: HJR_NAJ 1–0); com isso a tabela da RSSSF fecha
- **1415575:** [gm = 0, gv = 3] o ogol dá Najran 3-0 Al-Taawoun em 04/03/2011; a Wikipédia (2010–11 Saudi Professional League: NAJ_TWN 0–3) e a tabela da RSSSF dão 0-3

### Identidade dos clubes

Regras em `coleta/ksa-1/clubes_ksa.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da liga saudita: cada grafia de cada fonte (RSSSF, ogol, ESPN, Wikipédia) aponta para um clube.

Nome de exibição: o nome árabe com hífen, na grafia mais usada hoje (a do clube e da liga). Ficam com o nome puro
Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab (combinado entre os agentes, 23/11); o homônimo de clube de outro país leva a
cidade (Al-Ahli de Jeddah, Al-Wehda de Meca, Al-Qadsiah de Khobar, Al-Faisaly de Harmah, Al-Khaleej de Saihat, Al-Nahda
de Dammam, Al-Ansar de Medina, Al-Najma de Unaizah, Al-Orobah de Sakakah, Al-Arabi de Unaizah, Al-Ain de Al-Baha).

Mesmo clube com grafias diferentes: Al-Nasr = Al-Nassr; Al-Ahly = Al-Ahli; Al-Ittifaq = Al-Ettifaq; Al-Qadisiya =
Al-Qadsiah; Al-Wahda = Al-Wehda; Al-Nijma/Al-Nejmeh = Al-Najma; a linha "Al-Nojoom" da tabela da RSSSF de
2025/26 é o Neom (mesmos números: 12-9-13, 43-48, 45 pontos; o Al-Nojoom, de Al-Hasa, nunca jogou a 1ª divisão); Al-Ta'ee/Al-Tai; Al-Ra'ed/Al-Raed; Al-Faysali/Al-Faisaly;
Al-Fat'h/Al-Fateh; Al-Hazm/Al-Hazem; Faiha'a/Al-Fayha; Dhamk/Damak/Damac; Hajr/Hajer; Ukhdood/Al-Akhdoud/Al-Okhdood;
Al-Urooba/Al-Orobah; Al-Sho'ala/Al-Shoalah/Al-Shoulla; Al-Rouda/Al-Rawda/Al-Rawdhah; Okadh/Okaz; Al-Khlood/Al-Kholood;
Al-Riyadh SC = Al-Riyadh.

CLUBES: nome de exibição -> (cidade, província). REGRAS: (regex sobre a grafia da fonte, sem "Al"/"Al-"/"FC"/"Club"/
"SC" e sem acento, em minúsculas) -> nome de exibição. Grafia sem regra é erro (de propósito).
```

## 8. O que não deu para coletar

- **Fora do pacote:** a Copa do Rei (de 1957 a 1974 só a final, como a edição do campeonato que a federação conta), a Copa do Príncipe Herdeiro, a Copa da Federação, a Supercopa, a repescagem e a 2ª divisão.
- **Edições sem jogos:** 12 (1966/67, 1967/68, 1968/69, 1969/70, 1977/78, 1978/79, 1979/80, 1984/85, 1985/86, 1987/88, 1988/89, 1989/90).
- **Edições com jogos incompletos:** 1976/77 (a RSSSF tem 55 dos 56: o 56º é o awd Al-Ittihad x Al-Ahli, que entra; ver a edição) e os anos de playoff sem a final na RSSSF (1994/95, 1995/96).
- **Edições sem jogos** (12): 1966/67, 1967/68, 1968/69, 1969/70, 1977/78, 1978/79, 1979/80, 1984/85, 1985/86, 1987/88, 1988/89, 1989/90.
- **Décadas com menos da metade dos gols com autor:** 1950s, 1960s, 1970s, 2010s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s.
- Estatísticas de jogo (chutes, faltas, escanteios): não coletadas.

## 9. Pendências e próximos passos

- 1957/58 a 1973/74 (His Majesty's League): só campeão, vice e, quando a RSSSF tem o mesmo par, o jogo da final da Copa do Rei; sem os outros jogos nem a data. 1968/69 sem a final (o par oficial não está na lista da RSSSF). Fonte que resolveria: o relatório oficial da federação (2025), que não está publicado em detalhe.
- Sem os jogos da fase de liga em 1977/78-1979/80, 1981/82, 1984/85, 1985/86 e 1987/88-1996/97 (a RSSSF só tem a tabela; o ogol só tem jogos de 1999/00 em diante); 1977/78-1981/82 com tabela só de jogos e pontos, 1985/86 só a ordem. Fonte que resolveria: os jornais da época (Arab News, citado pela RSSSF) ou o arquivo antigo do Kooora (o site mudou e não mostra mais os anos antigos).
- Finais do playoff que a RSSSF não tem: 1994/95 e 1995/96 (campeão e vice da lista oficial).
- Autores dos gols só onde a RSSSF tem (1974/75-2005/06, com falhas: 1997/98 sem nenhum, 2003/04 66%) e a ESPN (2022/23-2025/26, 98-100%); 2006/07-2021/22 sem autores nem cartões. Fonte que resolveria: as súmulas do site da Saudi Pro League ou o FBref/Transfermarkt.
- Placares diferentes entre a RSSSF e o ogol em uns 2 a 8 jogos por ano (listados em cada edição); ficou a fonte dos jogos do ano, conferida com a tabela da RSSSF. 1997/98, 2003/04, 2011/12: diferenças de 1 gol entre os jogos e a tabela da RSSSF.
- Datas: 36 jogos sem data (finais antigas e playoffs da RSSSF sem data).

## 10. Arquivos e comandos

Código em `coleta/ksa-1/`:

| Arquivo | O que faz |
|---|---|
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga ksa.1) para data/coleta/ksa-1/espn/ksa1_<fim>.json (<fim> = ano em que a temporada |
| `baixar_ogol.py` | Baixa o calendário de cada edição da liga saudita no ogol ("liga-saudita") para data/coleta/ksa-1/ogol/<fim>.json |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão saudita para data/coleta/ksa-1/rsssf/: a lista de campeões (sauchamp.html), a |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês a página da liga saudita ("Saudi Pro League": lista de campeões e vices desde 1957, como o |
| `campeoes_wiki.py` | Campeão e vice de cada temporada da liga saudita pela Wikipédia em inglês (página "Saudi Pro League", seção "List of |
| `clubes_ksa.py` | Identidade dos clubes da liga saudita: cada grafia de cada fonte (RSSSF, ogol, ESPN, Wikipédia) aponta para um clube. |
| `edicoes.py` | Edições do Campeonato Saudita: as 69 temporadas da lista oficial (relatório da federação de 2025, como a Wikipédia em |
| `explicacoes.py` | Correções e casos especiais da liga saudita, com a prova de cada um. |
| `fontes.py` | Jogos e tabelas de cada fonte da liga saudita, já com o nome de exibição dos clubes (clubes_ksa.py), no formato que o |
| `importar.py` | Monta o pacote do Campeonato Saudita (ksa-1) em data/coleta/ksa-1/pacote/ e o relatório docs/coleta/ksa-1.md. |
| `ler_rsssf.py` | Lê as páginas da RSSSF da liga saudita (data/coleta/ksa-1/rsssf/sauNN.html e sauNNNN.html, uma por temporada; o nome |
| `relatorio.py` | Escreve o relatório da coleta (docs/coleta/ksa-1.md) a partir do pacote e de data/coleta/ksa-1/conferencia_detalhe.json. |

- Fontes baixadas: `data/coleta/ksa-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-asia/`, do ogol em `data/cache/ogol-ksa-1/`.
- Pacote: `data/coleta/ksa-1/pacote/`; relatório: `docs/coleta/ksa-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/ksa-1/baixar_espn.py
python coleta/ksa-1/baixar_ogol.py
python coleta/ksa-1/baixar_rsssf.py
python coleta/ksa-1/baixar_wikipedia.py
python coleta/ksa-1/importar.py
python coleta/ksa-1/conferir.py [-v temporada]   # divergências
python coleta/comum-asia/testar_carga.py ksa-1 <scratchpad>
python coleta/comum-asia/documentar.py
```

