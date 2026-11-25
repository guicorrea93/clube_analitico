# Campeonato Saudita (1ª divisão) — coleta de dados

Gerado por `python coleta/ksa-1/importar.py`. Pacote em `data/coleta/ksa-1/pacote/`.

**Edições:** 69, as temporadas da lista oficial de campeões, de 1957/58 a 2025/26, como o relatório da federação
saudita de 2025 (reproduzido pela Wikipédia em inglês, página "Saudi Pro League"): Al-Hilal 21 títulos, Al-Ittihad 14,
Al-Nassr 11, Al-Ahli 9. Decisão do Guilherme (24/11/2026): desde 1957, como a federação conta (a RSSSF conta desde
1974/75). Eras: "His Majesty's League" (1957/58-1973/74, mata-mata; os campeões são os da antiga Copa do Rei), Liga de
Classificação (1974/75, dois grupos e final), Premier League (1975/76-2006/07; de 1990/91 a 2006/07 o título era decidido
num playoff dos 4 primeiros, o "Golden Box") e Pro League (2007/08 em diante). 1966/67 (não concluída), 1967/68 (não
disputada), 1969/70 e 1975/76 (canceladas) entram sem campeão. 2026/27 entra quando acabar.

**Fora do pacote:** a Copa do Rei (de 1957 a 1974 só a final, como a edição do campeonato que a federação conta), a Copa do
Príncipe Herdeiro, a Copa da Federação, a Supercopa, a repescagem e a 2ª divisão.

**Fontes:** RSSSF (uma página por temporada, `sauNN.html`, e a lista da Copa do Rei, `saucuphist.html`, em
`data/coleta/ksa-1/rsssf/`: tabela final de todos os anos de 1974/75 em diante, os jogos da fase de liga em 1974/75,
1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e 1997/98-2024/25, os jogos do playoff e os autores dos gols até 2005/06);
ogol (calendário de 1999/00 a 2025/26, só a fase de liga: `data/coleta/ksa-1/ogol/` e `data/cache/ogol-ksa-1/`, para os
escudos); ESPN (liga `ksa.1`, 2022/23 a 2025/26: autores dos gols, cartões, estádio, público e hora,
`data/coleta/ksa-1/espn/`); Wikipédia em inglês (lista oficial de campeões e vices; matrizes de resultados de 2010/11 e
2011/12 nas correções).

**Clubes:** 43. Nome árabe com hífen; Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab com o nome puro (combinado entre os
agentes); os homônimos de clubes de outros países com a cidade (Al-Ahli de Jeddah, Al-Wehda de Meca, Al-Qadsiah de
Khobar, Al-Faisaly de Harmah, Al-Khaleej de Saihat, Al-Nahda de Dammam, Al-Ansar de Medina, Al-Najma de Unaizah,
Al-Orobah de Sakakah, Al-Arabi de Unaizah, Al-Ain de Al-Baha). As grafias de cada fonte estão no `nomes_fonte` do
`clubes.csv` (regras em `coleta/ksa-1/clubes_ksa.py`).

**Regras:** placar oficial, com a prorrogação; jogos decididos fora de campo (`awd`) com o placar dado e o de campo na
observação. Os jogos da fase de liga vêm da RSSSF até 2005/06 quando ela tem a fase completa e do ogol nos outros anos
(1999/00 em diante); o playoff do título vem sempre da RSSSF. Anos sem os jogos na RSSSF nem no ogol (1977/78-1979/80,
1984/85, 1985/86, 1987/88-1996/97): só a tabela final (e os jogos do playoff que a RSSSF tem). Classificação final: a
tabela da fase de liga da RSSSF, com o campeão e o vice oficiais em cima; os números são só da fase de liga (sem o
playoff); nos anos em que a RSSSF dá só jogos e pontos (1977/78-1981/82) ou só a ordem (1985/86), o resto fica vazio.
Pontos por vitória: 2 até 1992/93, 3 de 1993/94 em diante (tirado das tabelas). `ajuste_pontos`: punições e bônus da
tabela da RSSSF. Rebaixado: o marcado na tabela da RSSSF. 1957/58-1973/74: campeão e vice da lista oficial; o jogo da final
da Copa do Rei da RSSSF quando ela tem o mesmo par (o rótulo da temporada às vezes é o anterior). Artilheiro: o da lista da
página da RSSSF; sem ela, a soma dos gols com autor quando ao menos 95% dos gols têm autor.

**Conferência:** a tabela calculada dos jogos contra a tabela da RSSSF (jogos, vitórias, empates, derrotas, gols e pontos
sem o ajuste); os placares da fonte dos jogos contra a outra (RSSSF x ogol) e contra a ESPN; o campeão contra a final do
playoff. Correções do ogol com prova em `coleta/ksa-1/explicacoes.py`.

**Edições sem jogos:** 12 (1966/67, 1967/68, 1968/69, 1969/70, 1977/78, 1978/79, 1979/80, 1984/85, 1985/86, 1987/88, 1988/89, 1989/90).

**Edições com jogos incompletos:** 1976/77 (a RSSSF tem 55 dos 56: o 56º é o awd Al-Ittihad x Al-Ahli, que entra; ver
a edição) e os anos de playoff sem a final na RSSSF (1994/95, 1995/96).

**Resumo:** 5965 jogos, 7296 gols com autor, 4801 cartões.

| Temporada | Clubes | Jogos | Gols | c/ autor | Fonte dos jogos | Campeão | Vice |
|---|---|---|---|---|---|---|---|
| 1957/58 |  | 1 | 4 | 0 | Copa do Rei (RSSSF), só a final | Al-Wehda de Meca | Al-Ittihad |
| 1958/59 |  | 1 | 3 | 0 | Copa do Rei (RSSSF), só a final | Al-Ittihad | Al-Wehda de Meca |
| 1959/60 |  | 1 | 2 | 0 | Copa do Rei (RSSSF), só a final | Al-Ittihad | Al-Wehda de Meca |
| 1960/61 |  | 1 | 3 | 0 | Copa do Rei (RSSSF), só a final | Al-Ittihad | Al-Wehda de Meca |
| 1961/62 |  | 1 | 5 | 0 | Copa do Rei (RSSSF), só a final | Al-Hilal | Al-Wehda de Meca |
| 1962/63 |  | 1 | 1 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Riyadh |
| 1963/64 |  | 1 | 3 | 0 | Copa do Rei (RSSSF), só a final | Al-Ittihad | Al-Hilal |
| 1964/65 |  | 1 | 0 | 0 | Copa do Rei (RSSSF), só a final | Al-Hilal | Al-Ittihad |
| 1965/66 |  | 1 | 4 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Ettifaq |
| 1966/67 |  | 0 | 0 | 0 | nenhuma | — | — |
| 1967/68 |  | 0 | 0 | 0 | nenhuma | — | — |
| 1968/69 |  | 0 | 0 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Ettifaq |
| 1969/70 |  | 0 | 0 | 0 | nenhuma | — | — |
| 1970/71 |  | 1 | 2 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Wehda de Meca |
| 1971/72 |  | 1 | 2 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Nassr |
| 1972/73 |  | 1 | 3 | 0 | Copa do Rei (RSSSF), só a final | Al-Ahli de Jeddah | Al-Nassr |
| 1973/74 |  | 1 | 1 | 0 | Copa do Rei (RSSSF), só a final | Al-Nassr | Al-Ahli de Jeddah |
| 1974/75 | 16 | 113 | 364 | 4 | RSSSF | Al-Nassr | Al-Hilal |
| 1975/76 | 8 | 16 | 42 | 25 | RSSSF (temporada abandonada: 16 jogos) | — | — |
| 1976/77 | 8 | 56 | 117 | 55 | RSSSF | Al-Hilal | Al-Nassr |
| 1977/78 | 10 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Ahli de Jeddah | Al-Nassr |
| 1978/79 | 10 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Nassr |
| 1979/80 | 10 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Nassr | Al-Hilal |
| 1980/81 | 10 | 90 | 281 | 239 | RSSSF | Al-Nassr | Al-Hilal |
| 1981/82 | 20 | 4 | 8 | 0 | nenhuma (só a tabela) | Al-Ittihad | Al-Shabab |
| 1982/83 | 10 | 90 | 218 | 215 | RSSSF | Al-Ettifaq | Al-Hilal |
| 1983/84 | 10 | 90 | 221 | 212 | RSSSF | Al-Ahli de Jeddah | Al-Ittihad |
| 1984/85 | 12 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Shabab |
| 1985/86 | 12 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Ittihad |
| 1986/87 | 12 | 132 | 309 | 305 | RSSSF | Al-Ettifaq | Al-Hilal |
| 1987/88 | 12 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Ettifaq |
| 1988/89 | 12 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Nassr | Al-Shabab |
| 1989/90 | 12 | 0 | 0 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Ahli de Jeddah |
| 1990/91 | 12 | 6 | 16 | 0 | nenhuma (só a tabela) | Al-Shabab | Al-Nassr |
| 1991/92 | 12 | 5 | 9 | 2 | nenhuma (só a tabela) | Al-Shabab | Al-Ettifaq |
| 1992/93 | 12 | 5 | 11 | 0 | nenhuma (só a tabela) | Al-Shabab | Al-Hilal |
| 1993/94 | 12 | 3 | 6 | 6 | nenhuma (só a tabela) | Al-Nassr | Al-Riyadh |
| 1994/95 | 12 | 2 | 4 | 0 | nenhuma (só a tabela) | Al-Nassr | Al-Hilal |
| 1995/96 | 12 | 5 | 13 | 0 | nenhuma (só a tabela) | Al-Hilal | Al-Ahli de Jeddah |
| 1996/97 | 12 | 6 | 25 | 10 | RSSSF incompleta (6 jogos): fora | Al-Ittihad | Al-Hilal |
| 1997/98 | 12 | 138 | 407 | 0 | RSSSF | Al-Hilal | Al-Shabab |
| 1998/99 | 12 | 137 | 390 | 361 | RSSSF | Al-Ittihad | Al-Ahli de Jeddah |
| 1999/00 | 12 | 137 | 408 | 362 | RSSSF | Al-Ittihad | Al-Ahli de Jeddah |
| 2000/01 | 12 | 137 | 353 | 332 | RSSSF | Al-Ittihad | Al-Nassr |
| 2001/02 | 12 | 135 | 416 | 400 | ogol | Al-Hilal | Al-Ittihad |
| 2002/03 | 12 | 135 | 411 | 387 | RSSSF | Al-Ittihad | Al-Ahli de Jeddah |
| 2003/04 | 12 | 135 | 403 | 266 | ogol | Al-Shabab | Al-Ittihad |
| 2004/05 | 12 | 135 | 415 | 363 | ogol | Al-Hilal | Al-Shabab |
| 2005/06 | 12 | 135 | 406 | 387 | RSSSF | Al-Shabab | Al-Hilal |
| 2006/07 | 12 | 135 | 400 | 0 | ogol | Al-Ittihad | Al-Hilal |
| 2007/08 | 12 | 132 | 352 | 0 | ogol | Al-Hilal | Al-Ittihad |
| 2008/09 | 12 | 132 | 364 | 0 | ogol | Al-Ittihad | Al-Hilal |
| 2009/10 | 12 | 132 | 374 | 0 | ogol | Al-Hilal | Al-Ittihad |
| 2010/11 | 14 | 182 | 534 | 0 | ogol | Al-Hilal | Al-Ittihad |
| 2011/12 | 14 | 182 | 536 | 0 | ogol | Al-Shabab | Al-Ahli de Jeddah |
| 2012/13 | 14 | 182 | 531 | 0 | ogol | Al-Fateh | Al-Hilal |
| 2013/14 | 14 | 182 | 515 | 0 | ogol | Al-Nassr | Al-Hilal |
| 2014/15 | 14 | 182 | 528 | 0 | ogol | Al-Nassr | Al-Ahli de Jeddah |
| 2015/16 | 14 | 182 | 508 | 0 | ogol | Al-Ahli de Jeddah | Al-Hilal |
| 2016/17 | 14 | 182 | 549 | 0 | ogol | Al-Hilal | Al-Ahli de Jeddah |
| 2017/18 | 14 | 182 | 542 | 0 | ogol | Al-Hilal | Al-Ahli de Jeddah |
| 2018/19 | 16 | 240 | 706 | 0 | ogol | Al-Nassr | Al-Hilal |
| 2019/20 | 16 | 240 | 690 | 0 | ogol | Al-Hilal | Al-Nassr |
| 2020/21 | 16 | 240 | 746 | 0 | ogol | Al-Hilal | Al-Shabab |
| 2021/22 | 16 | 240 | 637 | 0 | ogol | Al-Hilal | Al-Ittihad |
| 2022/23 | 16 | 240 | 648 | 636 | ogol | Al-Ittihad | Al-Nassr |
| 2023/24 | 18 | 306 | 909 | 909 | ogol | Al-Hilal | Al-Nassr |
| 2024/25 | 18 | 306 | 902 | 899 | ogol | Al-Ittihad | Al-Hilal |
| 2025/26 | 18 | 306 | 921 | 921 | ogol | Al-Nassr | Al-Hilal |

## Correções do ogol

- jogo 1898735 do ogol: o ogol dá Al-Hilal 1-0 Najran em 31/03/2012 (rodada 24), mas o Al-Hilal já jogou na rodada (Al-Fateh 0-5 Al-Hilal), recebe o Najran outra vez em 09/12/2011 e falta o Hajer x Najran: é Hajer 1-0 Najran (Wikipédia, 2011–12 Saudi Professional League: HJR_NAJ 1–0); com isso a tabela da RSSSF fecha.
- jogo 1415575 do ogol: o ogol dá Najran 3-0 Al-Taawoun em 04/03/2011; a Wikipédia (2010–11 Saudi Professional League: NAJ_TWN 0–3) e a tabela da RSSSF dão 0-3.

## Conferência e observações, edição a edição

### 1957/58

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1958/59

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1959/60

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1960/61

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1961/62

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1962/63

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1963/64

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1964/65

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1965/66

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1966/67

- Formato: mata-mata (His Majesty's League).
- Jogos: nenhuma.
- temporada não concluída (lista oficial).

### 1967/68

- Formato: mata-mata (His Majesty's League).
- Jogos: nenhuma.
- temporada não disputada (lista oficial).

### 1968/69

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.
- a RSSSF não tem a final com esse par de clubes (só campeão e vice da lista oficial).

### 1969/70

- Formato: mata-mata (His Majesty's League).
- Jogos: nenhuma.
- temporada cancelada (lista oficial).

### 1970/71

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1971/72

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1972/73

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1973/74

- Formato: mata-mata (His Majesty's League).
- Jogos: Copa do Rei (RSSSF), só a final.

### 1974/75

- Formato: dois grupos de 8 e final.
- Jogos: RSSSF.
- Al-Ansar de Medina: +2 ponto(s) na tabela da RSSSF (punição ou bônus).

### 1975/76

- Formato: pontos corridos (8 clubes), abandonado.
- Jogos: RSSSF (temporada abandonada: 16 jogos).
- temporada abandonada no meio (lista oficial: cancelada); jogos e tabela até a parada, sem campeão.

### 1976/77

- Formato: pontos corridos, 8 clubes.
- Jogos: RSSSF.

### 1977/78

- Formato: pontos corridos, 10 clubes.
- Jogos: nenhuma (só a tabela).

### 1978/79

- Formato: pontos corridos, 10 clubes.
- Jogos: nenhuma (só a tabela).

### 1979/80

- Formato: pontos corridos, 10 clubes.
- Jogos: nenhuma (só a tabela).

### 1980/81

- Formato: pontos corridos, 10 clubes.
- Jogos: RSSSF.

### 1981/82

- Formato: dois grupos de 10 e playoff (semifinais, 3º lugar e final).
- Jogos: nenhuma (só a tabela).

### 1982/83

- Formato: pontos corridos, 10 clubes.
- Jogos: RSSSF.
- Artilheiro: Majed Abdullah (Al-Nassr), 14 (soma dos gols com autor (215 de 218)).

### 1983/84

- Formato: pontos corridos, 10 clubes.
- Jogos: RSSSF.
- Artilheiro: Hussam Abo Dawood (Al-Ahli de Jeddah), 12 (soma dos gols com autor (212 de 221)).

### 1984/85

- Formato: pontos corridos, 12 clubes.
- Jogos: nenhuma (só a tabela).

### 1985/86

- Formato: dois grupos de 6 e grupos finais (título, classificação, rebaixamento).
- Jogos: nenhuma (só a tabela).

### 1986/87

- Formato: pontos corridos, 12 clubes.
- Jogos: RSSSF.
- Artilheiro: Mohammed Al-Suwayed (Al-Ittihad), 17 (soma dos gols com autor (305 de 309)).

### 1987/88

- Formato: pontos corridos, 12 clubes.
- Jogos: nenhuma (só a tabela).

### 1988/89

- Formato: pontos corridos, 12 clubes.
- Jogos: nenhuma (só a tabela).

### 1989/90

- Formato: pontos corridos, 12 clubes.
- Jogos: nenhuma (só a tabela).

### 1990/91

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).

### 1991/92

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).
- Artilheiro: Said Oweiran (Al-Shabab), 16 (RSSSF (sau1992, artilheiros)).

### 1992/93

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).

### 1993/94

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).

### 1994/95

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).
- a RSSSF não tem o jogo da final; campeão e vice da lista oficial.

### 1995/96

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: nenhuma (só a tabela).
- a RSSSF não tem o jogo da final; campeão e vice da lista oficial.
- Artilheiro: A Da Silva (Al-Ahli de Jeddah), 12 (RSSSF (sau1996, artilheiros)).

### 1996/97

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF incompleta (6 jogos): fora.

### 1997/98

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- Diferenças: tabela, Al-Najma de Unaizah: RSSSF {'jogos': 22, 'vitorias': 13, 'empates': 2, 'derrotas': 7, 'gols_pro': 34, 'gols_contra': 28, 'pontos': 41}, jogos {'jogos': 22, 'vitorias': 13, 'empates': 2, 'derrotas': 7, 'gols_pro': 34, 'gols_contra': 29, 'pontos': 41}; tabela, Al-Ahli de Jeddah: RSSSF {'jogos': 22, 'vitorias': 12, 'empates': 2, 'derrotas': 8, 'gols_pro': 38, 'gols_contra': 30, 'pontos': 38}, jogos {'jogos': 22, 'vitorias': 12, 'empates': 2, 'derrotas': 8, 'gols_pro': 39, 'gols_contra': 31, 'pontos': 38}; tabela, Al-Ettifaq: RSSSF {'jogos': 22, 'vitorias': 8, 'empates': 7, 'derrotas': 7, 'gols_pro': 28, 'gols_contra': 33, 'pontos': 31}, jogos {'jogos': 22, 'vitorias': 8, 'empates': 7, 'derrotas': 7, 'gols_pro': 29, 'gols_contra': 33, 'pontos': 31}; tabela, Al-Taawoun: RSSSF {'jogos': 22, 'vitorias': 3, 'empates': 5, 'derrotas': 14, 'gols_pro': 17, 'gols_contra': 37, 'pontos': 14}, jogos {'jogos': 22, 'vitorias': 3, 'empates': 5, 'derrotas': 14, 'gols_pro': 18, 'gols_contra': 38, 'pontos': 14}.

### 1998/99

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- Artilheiro: Obaid al-Dossari (Al-Wehda de Meca), 20 (RSSSF (sau1999, artilheiros)).

### 1999/00

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- Al-Wehda de Meca: -1 ponto(s) na tabela da RSSSF (punição ou bônus).
- Al-Tai: -1 ponto(s) na tabela da RSSSF (punição ou bônus).
- ogol: 126 placares iguais, 6 diferentes.
- Diferenças: 1999-12-02 Al-Nassr 2-1 Al-Wehda de Meca (ogol 1-2); 2000-01-13 Al-Ettifaq 1-2 Al-Riyadh (ogol 0-2); 2000-04-04 Al-Tai 1-1 Al-Hilal (ogol 0-1); 2000-03-05 Al-Hilal 2-0 Al-Najma de Unaizah (ogol 2-1); tabela, Al-Wehda de Meca: RSSSF {'jogos': 22, 'vitorias': 6, 'empates': 5, 'derrotas': 11, 'gols_pro': 31, 'gols_contra': 58, 'pontos': 23}, jogos {'jogos': 22, 'vitorias': 6, 'empates': 4, 'derrotas': 12, 'gols_pro': 31, 'gols_contra': 58, 'pontos': 22}.
- Artilheiro: Hamza Idriss Falatah (Al-Ittihad), 33 (RSSSF (sau2000, artilheiros)).

### 2000/01

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- Al-Hilal: -3 ponto(s) na tabela da RSSSF (punição ou bônus).
- ogol: 127 placares iguais, 5 diferentes.
- Diferenças: 2000-11-07 Al-Qadsiah de Khobar 0-3 Sadous (ogol 2-2); 2001-02-22 Al-Ahli de Jeddah 1-1 Al-Ittihad (ogol 3-1); 2001-04-05 Al-Ittihad 1-3 Al-Ahli de Jeddah (ogol 1-1).
- Artilheiro: Paulo Da Silva (Al-Ettifaq), 13 (RSSSF (sau2001, artilheiros)).

### 2001/02

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: ogol.
- RSSSF: 129 placares iguais, 3 diferentes.
- Diferenças: 2001-11-01 Al-Shoulla 2-1 Al-Ansar de Medina (RSSSF 1-1); tabela, Al-Ettifaq: RSSSF {'jogos': 21, 'vitorias': 6, 'empates': 5, 'derrotas': 10, 'gols_pro': 23, 'gols_contra': 38, 'pontos': 23}, jogos {'jogos': 22, 'vitorias': 7, 'empates': 5, 'derrotas': 10, 'gols_pro': 25, 'gols_contra': 39, 'pontos': 26}; tabela, Al-Shabab: RSSSF {'jogos': 21, 'vitorias': 5, 'empates': 7, 'derrotas': 9, 'gols_pro': 23, 'gols_contra': 28, 'pontos': 22}, jogos {'jogos': 22, 'vitorias': 5, 'empates': 7, 'derrotas': 10, 'gols_pro': 24, 'gols_contra': 30, 'pontos': 22}. A página da RSSSF não tem o jogo adiado Al-Ettifaq 2-1 Al-Shabab (05/04/2002, no ogol) e a tabela dela conta 21 jogos para os dois clubes; com o jogo, os dois fecham com 22.
- Artilheiro: Ricardo Sergio (Al-Ittihad), 16 (RSSSF (sau2002, artilheiros)).

### 2002/03

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- ogol: 130 placares iguais, 2 diferentes.
- Diferenças: 2003-01-10 Al-Nassr 6-1 Al-Raed (ogol 6-2); 2003-01-23 Al-Tai 0-0 Al-Raed (ogol 1-1).

### 2003/04

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: ogol.
- Diferenças: tabela, Al-Shabab: RSSSF {'jogos': 22, 'vitorias': 12, 'empates': 6, 'derrotas': 4, 'gols_pro': 50, 'gols_contra': 26, 'pontos': 42}, jogos {'jogos': 22, 'vitorias': 12, 'empates': 6, 'derrotas': 4, 'gols_pro': 50, 'gols_contra': 27, 'pontos': 42}; tabela, Al-Tai: RSSSF {'jogos': 22, 'vitorias': 7, 'empates': 3, 'derrotas': 12, 'gols_pro': 20, 'gols_contra': 41, 'pontos': 24}, jogos {'jogos': 22, 'vitorias': 7, 'empates': 3, 'derrotas': 12, 'gols_pro': 21, 'gols_contra': 41, 'pontos': 24}; tabela, Al-Riyadh: RSSSF {'jogos': 22, 'vitorias': 6, 'empates': 4, 'derrotas': 12, 'gols_pro': 22, 'gols_contra': 40, 'pontos': 22}, jogos {'jogos': 22, 'vitorias': 6, 'empates': 4, 'derrotas': 12, 'gols_pro': 22, 'gols_contra': 41, 'pontos': 22}; tabela, Al-Khaleej de Saihat: RSSSF {'jogos': 22, 'vitorias': 3, 'empates': 2, 'derrotas': 17, 'gols_pro': 25, 'gols_contra': 50, 'pontos': 11}, jogos {'jogos': 22, 'vitorias': 3, 'empates': 2, 'derrotas': 17, 'gols_pro': 26, 'gols_contra': 50, 'pontos': 11}.

### 2004/05

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: ogol.

### 2005/06

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: RSSSF.
- ogol: 130 placares iguais, 2 diferentes.
- Diferenças: 2005-11-12 Al-Hazem 3-7 Al-Ittihad (ogol 2-0); 2006-03-04 Al-Qadsiah de Khobar 2-0 Abha (ogol 2-1).
- Artilheiro: Eissa Al-Mahyani (Al-Wehda de Meca), 17 (soma dos gols com autor (387 de 406)).

### 2006/07

- Formato: pontos corridos, 12 clubes; playoff do título entre os 4 primeiros.
- Jogos: ogol.
- RSSSF: 132 placares iguais, 0 diferentes.

### 2007/08

- Formato: pontos corridos, 12 clubes.
- Jogos: ogol.
- RSSSF: 130 placares iguais, 2 diferentes.
- Diferenças: 2008-01-12 Al-Ittihad 1-0 Al-Hazem (RSSSF 2-0); 2008-04-13 Al-Tai 1-2 Al-Hazem (RSSSF 1-3); tabela, Al-Ittihad: RSSSF {'jogos': 22, 'vitorias': 14, 'empates': 6, 'derrotas': 2, 'gols_pro': 40, 'gols_contra': 16, 'pontos': 48}, jogos {'jogos': 22, 'vitorias': 14, 'empates': 6, 'derrotas': 2, 'gols_pro': 39, 'gols_contra': 16, 'pontos': 48}; tabela, Al-Hazem: RSSSF {'jogos': 22, 'vitorias': 7, 'empates': 6, 'derrotas': 9, 'gols_pro': 26, 'gols_contra': 28, 'pontos': 27}, jogos {'jogos': 22, 'vitorias': 7, 'empates': 6, 'derrotas': 9, 'gols_pro': 25, 'gols_contra': 27, 'pontos': 27}; tabela, Al-Tai: RSSSF {'jogos': 22, 'vitorias': 2, 'empates': 7, 'derrotas': 13, 'gols_pro': 20, 'gols_contra': 38, 'pontos': 13}, jogos {'jogos': 22, 'vitorias': 2, 'empates': 7, 'derrotas': 13, 'gols_pro': 20, 'gols_contra': 37, 'pontos': 13}.

### 2008/09

- Formato: pontos corridos, 12 clubes.
- Jogos: ogol.
- RSSSF: 132 placares iguais, 0 diferentes.

### 2009/10

- Formato: pontos corridos, 12 clubes.
- Jogos: ogol.
- RSSSF: 129 placares iguais, 3 diferentes.
- Diferenças: 2009-08-22 Al-Raed 0-1 Al-Ittihad (RSSSF 0-2); 2009-12-05 Al-Ittihad 2-0 Al-Ahli de Jeddah (RSSSF 2-1); 2009-12-15 Al-Hilal 1-1 Al-Qadsiah de Khobar (RSSSF 2-1); tabela, Al-Hilal: RSSSF {'jogos': 22, 'vitorias': 18, 'empates': 2, 'derrotas': 2, 'gols_pro': 56, 'gols_contra': 18, 'pontos': 56}, jogos {'jogos': 22, 'vitorias': 17, 'empates': 3, 'derrotas': 2, 'gols_pro': 55, 'gols_contra': 18, 'pontos': 54}; tabela, Al-Ittihad: RSSSF {'jogos': 22, 'vitorias': 14, 'empates': 3, 'derrotas': 5, 'gols_pro': 46, 'gols_contra': 30, 'pontos': 45}, jogos {'jogos': 22, 'vitorias': 14, 'empates': 3, 'derrotas': 5, 'gols_pro': 45, 'gols_contra': 29, 'pontos': 45}; tabela, Al-Ahli de Jeddah: RSSSF {'jogos': 22, 'vitorias': 7, 'empates': 7, 'derrotas': 8, 'gols_pro': 28, 'gols_contra': 29, 'pontos': 28}, jogos {'jogos': 22, 'vitorias': 7, 'empates': 7, 'derrotas': 8, 'gols_pro': 27, 'gols_contra': 29, 'pontos': 28}; tabela, Al-Qadsiah de Khobar: RSSSF {'jogos': 22, 'vitorias': 5, 'empates': 5, 'derrotas': 12, 'gols_pro': 20, 'gols_contra': 40, 'pontos': 20}, jogos {'jogos': 22, 'vitorias': 5, 'empates': 6, 'derrotas': 11, 'gols_pro': 20, 'gols_contra': 39, 'pontos': 21}; tabela, Al-Raed: RSSSF {'jogos': 22, 'vitorias': 3, 'empates': 7, 'derrotas': 12, 'gols_pro': 18, 'gols_contra': 35, 'pontos': 16}, jogos {'jogos': 22, 'vitorias': 3, 'empates': 7, 'derrotas': 12, 'gols_pro': 18, 'gols_contra': 34, 'pontos': 16}.

### 2010/11

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- Al-Taawoun: -3 ponto(s) na tabela da RSSSF (punição ou bônus).
- Al-Wehda de Meca: -3 ponto(s) na tabela da RSSSF (punição ou bônus).

### 2011/12

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- Diferenças: tabela, Al-Taawoun: RSSSF {'jogos': 26, 'vitorias': 4, 'empates': 7, 'derrotas': 15, 'gols_pro': 28, 'gols_contra': 52, 'pontos': 19}, jogos {'jogos': 26, 'vitorias': 4, 'empates': 7, 'derrotas': 15, 'gols_pro': 27, 'gols_contra': 52, 'pontos': 19}; tabela, Al-Ansar de Medina: RSSSF {'jogos': 26, 'vitorias': 3, 'empates': 1, 'derrotas': 22, 'gols_pro': 19, 'gols_contra': 60, 'pontos': 10}, jogos {'jogos': 26, 'vitorias': 3, 'empates': 1, 'derrotas': 22, 'gols_pro': 19, 'gols_contra': 59, 'pontos': 10}.

### 2012/13

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- RSSSF: 182 placares iguais, 0 diferentes.

### 2013/14

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- RSSSF: 182 placares iguais, 0 diferentes.

### 2014/15

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- RSSSF: 182 placares iguais, 0 diferentes.

### 2015/16

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- RSSSF: 182 placares iguais, 0 diferentes.

### 2016/17

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- Al-Ittihad: -3 ponto(s) na tabela da RSSSF (punição ou bônus).
- RSSSF: 182 placares iguais, 0 diferentes.

### 2017/18

- Formato: pontos corridos, 14 clubes.
- Jogos: ogol.
- RSSSF: 182 placares iguais, 0 diferentes.

### 2018/19

- Formato: pontos corridos, 16 clubes.
- Jogos: ogol.
- RSSSF: 234 placares iguais, 6 diferentes.
- Diferenças: 2018-08-30 Al-Hazem 0-0 Al-Wehda de Meca (RSSSF 1-1); 2018-09-13 Al-Ettifaq 2-3 Al-Batin (RSSSF 3-2); 2018-12-01 Al-Taawoun 2-0 Al-Fateh (RSSSF 1-1); 2019-01-28 Al-Wehda de Meca 1-1 Al-Hazem (RSSSF 0-0); 2019-02-28 Al-Ettifaq 1-4 Al-Taawoun (RSSSF 2-4); tabela, Al-Ettifaq: RSSSF {'jogos': 30, 'vitorias': 8, 'empates': 9, 'derrotas': 13, 'gols_pro': 40, 'gols_contra': 55, 'pontos': 33}, jogos {'jogos': 30, 'vitorias': 7, 'empates': 9, 'derrotas': 14, 'gols_pro': 39, 'gols_contra': 56, 'pontos': 30}; tabela, Al-Batin: RSSSF {'jogos': 30, 'vitorias': 7, 'empates': 4, 'derrotas': 19, 'gols_pro': 29, 'gols_contra': 53, 'pontos': 25}, jogos {'jogos': 30, 'vitorias': 8, 'empates': 4, 'derrotas': 18, 'gols_pro': 30, 'gols_contra': 52, 'pontos': 28}.

### 2019/20

- Formato: pontos corridos, 16 clubes.
- Jogos: ogol.
- RSSSF: 240 placares iguais, 0 diferentes.

### 2020/21

- Formato: pontos corridos, 16 clubes.
- Jogos: ogol.
- RSSSF: 240 placares iguais, 0 diferentes.

### 2021/22

- Formato: pontos corridos, 16 clubes.
- Jogos: ogol.
- RSSSF: 240 placares iguais, 0 diferentes.

### 2022/23

- Formato: pontos corridos, 16 clubes.
- Jogos: ogol.
- ESPN: 239 placares iguais, 0 diferentes.
- RSSSF: 240 placares iguais, 0 diferentes.
- Jogos sem os autores (a ESPN não fecha com o placar): Al-Nassr 2-2 Al-Hilal: ESPN 0+0 autores; Al-Wehda de Meca 0-2 Al-Fateh: ESPN 0+0 autores; Al-Batin 2-2 Al-Adalah: ESPN 2+1 autores.
- Artilheiro: Abderrazak Hamdallah (Al-Ittihad), 21 (soma dos gols com autor (636 de 648)).

### 2023/24

- Formato: pontos corridos, 18 clubes.
- Jogos: ogol.
- ESPN: 306 placares iguais, 0 diferentes.
- RSSSF: 306 placares iguais, 0 diferentes.
- Artilheiro: Cristiano Ronaldo (Al-Nassr), 35 (soma dos gols com autor (909 de 909)).

### 2024/25

- Formato: pontos corridos, 18 clubes.
- Jogos: ogol.
- ESPN: 305 placares iguais, 0 diferentes.
- RSSSF: 306 placares iguais, 0 diferentes.
- Artilheiro: Cristiano Ronaldo (Al-Nassr), 25 (soma dos gols com autor (899 de 902)).

### 2025/26

- Formato: pontos corridos, 18 clubes.
- Jogos: ogol.
- ESPN: 306 placares iguais, 0 diferentes.
- Artilheiro: Julián Quiñones (Al-Qadsiah de Khobar), 33 (soma dos gols com autor (921 de 921)).
