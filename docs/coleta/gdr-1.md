# Campeonato da Alemanha Oriental — coleta de dados

Gerado por `python coleta/gdr-1/importar.py`. Pacote em `data/coleta/gdr-1/pacote/`.

**Edições:** 44: o campeonato da zona soviética (1948 e 1949, mata-mata) e a DDR-Oberliga de 1949/50 a 1990/91 (ano civil de 1956 a 1960; a rodada de transição de 1955 sem título; a última, como NOFV-Oberliga).

**Total:** 8062 jogos, 24270 gols, 52 clubes.

**Fontes:**
- RSSSF (Andreas Werner e outros): página de cada temporada, com rodada, data e placar de cada jogo e a tabela final; lista de campeões e de artilheiros;
- Wikipédia (en): tabela e matriz de resultados de cada temporada (conferência) e as fichas dos jogos de 1948 e 1949.

**Regras:** 2 pontos por vitória. Jogo dado fora de campo: vitória e 2 pontos para um lado, gols 0:0 (como a RSSSF), marcado `awd`. Cada tabela publicada é comparada com a calculada dos jogos; a ordem da classificação final é a da tabela da RSSSF (sem ela, a da Wikipédia).

**Desempate:** o critério calculado que reproduz a ordem oficial (saldo de gols em 40, média de gols em 1, confronto direto em 1).

| Temporada | Fontes | Clubes | Jogos | Gols | Tabelas ok / div. | Campeão |
|---|---|---|---|---|---|---|
| 1948 | Wikipédia (en) | 10 | 8 | 29 | 0 / 0 | FSV Zwickau |
| 1949 | Wikipédia (en) | 10 | 8 | 41 | 0 / 0 | Hallescher FC |
| 1949/50 | RSSSF + Wikipédia (en) | 14 | 182 | 667 | 0 / 2 | FSV Zwickau |
| 1950/51 | RSSSF + Wikipédia (en) | 18 | 306 | 1178 | 1 / 1 | Chemie Leipzig |
| 1951/52 | RSSSF + Wikipédia (en) | 19 | 342 | 1233 | 1 / 1 | Hallescher FC |
| 1952/53 | RSSSF + Wikipédia (en) | 17 | 272 | 885 | 2 / 0 | Dynamo Dresden |
| 1953/54 | RSSSF + Wikipédia (en) | 15 | 210 | 676 | 0 / 2 | Rot-Weiß Erfurt |
| 1954/55 | RSSSF + Wikipédia (en) | 14 | 182 | 613 | 2 / 0 | Rot-Weiß Erfurt |
| 1955 | RSSSF + Wikipédia (en) | 14 | 91 | 323 | 2 / 0 | — (sem título) |
| 1956 | RSSSF + Wikipédia (en) | 14 | 182 | 565 | 1 / 1 | Erzgebirge Aue |
| 1957 | RSSSF + Wikipédia (en) | 14 | 182 | 524 | 2 / 0 | Erzgebirge Aue |
| 1958 | RSSSF + Wikipédia (en) | 14 | 182 | 532 | 1 / 1 | Vorwärts Frankfurt/Oder |
| 1959 | RSSSF + Wikipédia (en) | 14 | 182 | 476 | 2 / 0 | Erzgebirge Aue |
| 1960 | RSSSF + Wikipédia (en) | 14 | 182 | 590 | 2 / 0 | Vorwärts Frankfurt/Oder |
| 1961/62 | RSSSF + Wikipédia (en) | 14 | 273 | 851 | 0 / 2 | Vorwärts Frankfurt/Oder |
| 1962/63 | RSSSF + Wikipédia (en) | 14 | 182 | 541 | 1 / 1 | Carl Zeiss Jena |
| 1963/64 | RSSSF + Wikipédia (en) | 14 | 182 | 459 | 1 / 1 | Chemie Leipzig |
| 1964/65 | RSSSF + Wikipédia (en) | 14 | 182 | 529 | 2 / 0 | Vorwärts Frankfurt/Oder |
| 1965/66 | RSSSF + Wikipédia (en) | 14 | 182 | 485 | 2 / 0 | Vorwärts Frankfurt/Oder |
| 1966/67 | RSSSF + Wikipédia (en) | 14 | 182 | 500 | 1 / 1 | Chemnitzer FC |
| 1967/68 | RSSSF + Wikipédia (en) | 14 | 182 | 474 | 1 / 1 | Carl Zeiss Jena |
| 1968/69 | RSSSF + Wikipédia (en) | 14 | 182 | 458 | 1 / 1 | Vorwärts Frankfurt/Oder |
| 1969/70 | RSSSF + Wikipédia (en) | 14 | 182 | 452 | 2 / 0 | Carl Zeiss Jena |
| 1970/71 | RSSSF + Wikipédia (en) | 14 | 182 | 508 | 2 / 0 | Dynamo Dresden |
| 1971/72 | RSSSF + Wikipédia (en) | 14 | 182 | 482 | 2 / 0 | 1. FC Magdeburg |
| 1972/73 | RSSSF + Wikipédia (en) | 14 | 182 | 557 | 2 / 0 | Dynamo Dresden |
| 1973/74 | RSSSF + Wikipédia (en) | 14 | 182 | 534 | 0 / 2 | 1. FC Magdeburg |
| 1974/75 | RSSSF + Wikipédia (en) | 14 | 182 | 514 | 1 / 1 | 1. FC Magdeburg |
| 1975/76 | RSSSF + Wikipédia (en) | 14 | 182 | 575 | 2 / 0 | Dynamo Dresden |
| 1976/77 | RSSSF + Wikipédia (en) | 14 | 182 | 500 | 2 / 0 | Dynamo Dresden |
| 1977/78 | RSSSF + Wikipédia (en) | 14 | 182 | 528 | 2 / 0 | Dynamo Dresden |
| 1978/79 | RSSSF + Wikipédia (en) | 14 | 182 | 556 | 2 / 0 | BFC Dynamo |
| 1979/80 | RSSSF + Wikipédia (en) | 14 | 182 | 525 | 2 / 0 | BFC Dynamo |
| 1980/81 | RSSSF + Wikipédia (en) | 14 | 182 | 621 | 2 / 0 | BFC Dynamo |
| 1981/82 | RSSSF + Wikipédia (en) | 14 | 182 | 600 | 2 / 0 | BFC Dynamo |
| 1982/83 | RSSSF + Wikipédia (en) | 14 | 182 | 592 | 2 / 0 | BFC Dynamo |
| 1983/84 | RSSSF + Wikipédia (en) | 14 | 182 | 599 | 2 / 0 | BFC Dynamo |
| 1984/85 | RSSSF + Wikipédia (en) | 14 | 182 | 601 | 2 / 0 | BFC Dynamo |
| 1985/86 | RSSSF + Wikipédia (en) | 14 | 182 | 476 | 2 / 0 | BFC Dynamo |
| 1986/87 | RSSSF + Wikipédia (en) | 14 | 182 | 468 | 2 / 0 | BFC Dynamo |
| 1987/88 | RSSSF + Wikipédia (en) | 14 | 182 | 524 | 2 / 0 | BFC Dynamo |
| 1988/89 | RSSSF + Wikipédia (en) | 14 | 182 | 503 | 2 / 0 | Dynamo Dresden |
| 1989/90 | RSSSF + Wikipédia (en) | 14 | 182 | 467 | 2 / 0 | Dynamo Dresden |
| 1990/91 | RSSSF + Wikipédia (en) | 14 | 182 | 459 | 1 / 1 | Hansa Rostock |

## Conferência e ocorrências, temporada a temporada

### 1948

- mata-mata entre os campeões estaduais: os jogos são as fichas da Wikipédia (en)

### 1949

- mata-mata entre os campeões estaduais: os jogos são as fichas da Wikipédia (en)

### 1949/50

- tabela publicada (RSSSF) x jogos — Rot-Weiß Erfurt tabela [26, 14, 6, 6, 58, 30, 35] jogos [26, 14, 6, 6, 57, 30, 34]
- tabela publicada (RSSSF) x jogos — Franz Mehring Marga tabela [26, 13, 5, 8, 49, 48, 31] jogos [26, 13, 5, 8, 49, 47, 31]
- tabela publicada (RSSSF) x jogos — Lokomotive Stendal tabela [26, 7, 6, 13, 31, 45, 19] jogos [26, 7, 6, 13, 31, 45, 20]
- tabela publicada (Wikipédia) x jogos — Rot-Weiß Erfurt tabela [26, 15, 5, 6, 58, 30, 35] jogos [26, 14, 6, 6, 57, 30, 34]
- tabela publicada (Wikipédia) x jogos — Franz Mehring Marga tabela [26, 13, 5, 8, 49, 48, 31] jogos [26, 13, 5, 8, 49, 47, 31]
- tabela publicada (Wikipédia) x jogos — Lokomotive Stendal tabela [26, 7, 5, 14, 31, 45, 19] jogos [26, 7, 6, 13, 31, 45, 20]
- placar diferente na matriz da Wikipédia — Rot-Weiß Erfurt x Franz Mehring Marga: RSSSF 0-0; Wikipédia 1-0

### 1950/51

- tabela publicada (RSSSF) x jogos — Motor Dessau tabela [34, 14, 7, 13, 68, 62, 34] jogos [34, 14, 6, 14, 68, 62, 34]
- tabela publicada (RSSSF) x jogos — Stahl Altenburg tabela [34, 11, 8, 15, 46, 61, 31] jogos [34, 12, 7, 15, 46, 61, 31]
- placar diferente na matriz da Wikipédia — Chemie Leipzig x Stahl Thale: RSSSF 1-0; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — Chemie Leipzig x Rotation Babelsberg: RSSSF 2-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — FSV Zwickau x Stahl Thale: RSSSF 4-1; Wikipédia 2-0
- placar diferente na matriz da Wikipédia — FSV Zwickau x Rotation Babelsberg: RSSSF 2-0; Wikipédia 4-1
- placar diferente na matriz da Wikipédia — Dynamo Dresden x Stahl Thale: RSSSF 6-0; Wikipédia 5-1
- placar diferente na matriz da Wikipédia — Dynamo Dresden x Rotation Babelsberg: RSSSF 5-1; Wikipédia 6-0
- placar diferente na matriz da Wikipédia — Aktivist Brieske-Senftenberg x Stahl Thale: RSSSF 1-5; Wikipédia 4-2
- placar diferente na matriz da Wikipédia — Aktivist Brieske-Senftenberg x Rotation Babelsberg: RSSSF 4-2; Wikipédia 1-5
- placar diferente na matriz da Wikipédia — Hallescher FC x Stahl Thale: RSSSF 5-1; Wikipédia 2-3
- placar diferente na matriz da Wikipédia — Hallescher FC x Rotation Babelsberg: RSSSF 2-3; Wikipédia 5-1
- ... e mais 54 pares com placar diferente na matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo é saldo

### 1951/52

- a tabela final da RSSSF de 1951/52 não traz o 3º, o 4º e o 5º colocados: a ordem e a conferência ficam com a tabela da Wikipédia
- tabela publicada (RSSSF) x jogos — a tabela tem 16 clubes; os jogos, 19

### 1952/53

- sem ocorrências

### 1953/54

- tabela publicada (RSSSF) x jogos — Chemie Leipzig tabela [28, 15, 6, 7, 51, 37, 35] jogos [28, 15, 6, 7, 51, 37, 36]
- tabela publicada (RSSSF) x jogos — Stahl Thale tabela [28, 3, 8, 17, 28, 59, 15] jogos [28, 3, 8, 17, 28, 59, 14]
- tabela publicada (Wikipédia) x jogos — Chemie Leipzig tabela [28, 15, 5, 8, 51, 37, 35] jogos [28, 15, 6, 7, 51, 37, 36]
- tabela publicada (Wikipédia) x jogos — Stahl Thale tabela [28, 4, 7, 17, 28, 59, 15] jogos [28, 3, 8, 17, 28, 59, 14]

### 1954/55

- sem ocorrências

### 1955

- placar diferente na matriz da Wikipédia — FSV Zwickau x Rot-Weiß Erfurt: RSSSF —; Wikipédia 4-1
- rodada de transição (Übergangsrunde) no segundo semestre de 1955, para passar ao ano civil; o primeiro colocado (Wismut Karl-Marx-Stadt) não é contado como campeão

### 1956

- tabela publicada (RSSSF) x jogos — Chemnitzer FC tabela [26, 7, 8, 11, 24, 48, 23] jogos [26, 8, 7, 11, 24, 48, 23]
- tabela publicada (RSSSF) x jogos — BFC Dynamo tabela [26, 7, 7, 12, 37, 47, 20] jogos [26, 7, 6, 13, 37, 47, 20]

### 1957

- sem ocorrências

### 1958

- tabela publicada (RSSSF) x jogos — Rot-Weiß Erfurt tabela [25, 8, 6, 12, 33, 44, 22] jogos [26, 8, 6, 12, 33, 44, 22]

### 1959

- sem ocorrências

### 1960

- sem ocorrências

### 1961/62

- tabela publicada (RSSSF) x jogos — Erzgebirge Aue tabela [39, 13, 14, 12, 60, 48, 38] jogos [39, 13, 14, 12, 60, 48, 40]
- tabela publicada (Wikipédia) x jogos — Erzgebirge Aue tabela [39, 13, 14, 12, 60, 48, 38] jogos [39, 13, 14, 12, 60, 48, 40]

### 1962/63

- tabela publicada (RSSSF) x jogos — Carl Zeiss Jena tabela [26, 16, 6, 4, 49, 22, 39] jogos [26, 17, 5, 4, 49, 22, 39]
- tabela publicada (RSSSF) x jogos — Hallescher FC tabela [26, 8, 8, 10, 38, 40, 25] jogos [26, 9, 7, 10, 38, 40, 25]
- tabela publicada (RSSSF) x jogos — 1. FC Magdeburg tabela [26, 10, 5, 11, 44, 46, 23] jogos [26, 10, 3, 13, 44, 46, 23]
- placar diferente na matriz da Wikipédia — Carl Zeiss Jena x Hallescher FC: RSSSF 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Carl Zeiss Jena x FSV Zwickau: RSSSF 1-1; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Hansa Rostock x Hallescher FC: RSSSF 2-2; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Hansa Rostock x FSV Zwickau: RSSSF 1-0; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Vorwärts Frankfurt/Oder x Hallescher FC: RSSSF 0-0; Wikipédia 3-2
- placar diferente na matriz da Wikipédia — Vorwärts Frankfurt/Oder x FSV Zwickau: RSSSF 3-2; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Erzgebirge Aue x Hallescher FC: RSSSF 2-1; Wikipédia 2-2
- placar diferente na matriz da Wikipédia — Erzgebirge Aue x FSV Zwickau: RSSSF 2-2; Wikipédia 2-1
- placar diferente na matriz da Wikipédia — VfB Leipzig x Hallescher FC: RSSSF 1-1; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — VfB Leipzig x FSV Zwickau: RSSSF 4-0; Wikipédia 1-1
- ... e mais 39 pares com placar diferente na matriz da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo é saldo

### 1963/64

- tabela publicada (RSSSF) x jogos — BFC Dynamo tabela [26, 8, 7, 11, 35, 34, 24] jogos [26, 9, 6, 11, 35, 34, 24]
- tabela publicada (RSSSF) x jogos — FSV Zwickau tabela [26, 7, 9, 10, 37, 41, 22] jogos [26, 7, 8, 11, 37, 41, 22]

### 1964/65

- sem ocorrências

### 1965/66

- sem ocorrências

### 1966/67

- tabela publicada (RSSSF) x jogos — Wismut Gera tabela [26, 4, 4, 18, 27, 57, 10] jogos [26, 4, 4, 18, 27, 57, 12]
- placar diferente na matriz da Wikipédia — BFC Dynamo x FSV Zwickau: RSSSF 2-2; Wikipédia 0-2

### 1967/68

- tabela publicada (RSSSF) x jogos — Vorwärts Frankfurt/Oder tabela [26, 9, 10, 7, 34, 29, 26] jogos [26, 9, 10, 7, 34, 29, 28]
- tabela publicada (RSSSF) x jogos — Erzgebirge Aue tabela [26, 9, 4, 13, 32, 40, 11] jogos [26, 9, 4, 13, 32, 40, 22]

### 1968/69

- tabela publicada (Wikipédia) x jogos — BFC Dynamo tabela [26, 10, 5, 11, 25, 36, 25] jogos [26, 10, 5, 11, 26, 37, 25]
- placar diferente na matriz da Wikipédia — Hansa Rostock x Carl Zeiss Jena: RSSSF 4-1; Wikipédia 4-4
- placar diferente na matriz da Wikipédia — VfB Leipzig x BFC Dynamo: RSSSF 1-2; Wikipédia 0-1

### 1969/70

- sem ocorrências

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- tabela publicada (RSSSF) x jogos — Stahl Riesa tabela [26, 7, 9, 10, 25, 42, 21] jogos [26, 7, 9, 10, 25, 42, 23]
- tabela publicada (Wikipédia) x jogos — Chemnitzer FC tabela [26, 7, 9, 10, 42, 46, 23] jogos [26, 7, 10, 9, 42, 46, 24]
- tabela publicada (Wikipédia) x jogos — Stahl Riesa tabela [26, 7, 9, 10, 25, 42, 21] jogos [26, 7, 9, 10, 25, 42, 23]
- nenhum critério calculado reproduz a ordem oficial; o mais próximo é saldo

### 1974/75

- tabela publicada (Wikipédia) x jogos — Hansa Rostock tabela [26, 7, 6, 13, 28, 38, 20] jogos [26, 7, 6, 13, 29, 35, 20]

### 1975/76

- placar diferente na matriz da Wikipédia — VfB Leipzig x Chemie Leipzig: RSSSF 0-1; Wikipédia 0-0
- placar diferente na matriz da Wikipédia — Chemie Leipzig x VfB Leipzig: RSSSF 2-3; Wikipédia 3-3

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- sem ocorrências

### 1979/80

- sem ocorrências

### 1980/81

- sem ocorrências

### 1981/82

- placar diferente na matriz da Wikipédia — Chemnitzer FC x Hallescher FC: RSSSF 2-1; Wikipédia 4-0
- placar diferente na matriz da Wikipédia — Hallescher FC x Chemnitzer FC: RSSSF 0-4; Wikipédia 1-2

### 1982/83

- placar diferente na matriz da Wikipédia — 1. FC Magdeburg x Chemie Böhlen: RSSSF 1-1; Wikipédia 6-1
- placar diferente na matriz da Wikipédia — Chemie Böhlen x 1. FC Magdeburg: RSSSF 1-6; Wikipédia 1-1

### 1983/84

- placar diferente na matriz da Wikipédia — Carl Zeiss Jena x Hallescher FC: RSSSF 3-0; Wikipédia 2-0

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- placar diferente na matriz da Wikipédia — VfB Leipzig x Union Berlin: RSSSF 2-2; Wikipédia 1-0
- placar diferente na matriz da Wikipédia — Union Berlin x VfB Leipzig: RSSSF 0-1; Wikipédia 2-2

### 1987/88

- placar diferente na matriz da Wikipédia — BFC Dynamo x Dynamo Dresden: RSSSF 1-0; Wikipédia 1-1
- placar diferente na matriz da Wikipédia — Chemnitzer FC x Carl Zeiss Jena: RSSSF 1-1; Wikipédia 3-1

### 1988/89

- sem ocorrências

### 1989/90

- sem ocorrências

### 1990/91

- tabela publicada (RSSSF) x jogos — BFC Dynamo tabela [26, 7, 8, 11, 25, 39, 26] jogos [26, 7, 8, 11, 25, 39, 22]

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_gdr.py`, pela linhagem do clube através das mudanças de nome e de cidade da RDA (Empor Lauter -> Hansa Rostock; SC Dynamo Berlin -> BFC Dynamo; KVP Leipzig -> Vorwärts Berlin -> Vorwärts Frankfurt/Oder; SC Lokomotive Leipzig -> 1. FC Lok -> VfB Leipzig). Os clubes que também jogaram a Bundesliga usam o nome do `ger-1` (Hansa Rostock, Union Berlin, Dynamo Dresden, Energie Cottbus, Carl Zeiss Jena, VfB Leipzig).

## O que não deu para coletar

- Autores dos gols, público e estádio dos jogos da Oberliga (a RSSSF traz só o placar).
- A primeira fase (campeonatos estaduais) de 1948 e 1949.
