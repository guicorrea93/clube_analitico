# Campeonato da Alemanha Oriental (`gdr-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/gdr-1/pacote/` e do importador `coleta/gdr-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/gdr-1.md`.

## 1. O que temos

- **Edições:** 44, de 1948 a 1990/91.
- **Jogos:** 8062; **gols:** 24270; **gols com autor:** 0 (0%); **cartões:** 0; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 52; **artilheiros:** 42 temporadas com artilheiro (43 linhas, com empates).
- **Classificação final:** 44 temporadas; **rodada a rodada:** 42 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1199 linhas, de 84 tabelas.
- **Observação da competição:** Campeonato da zona soviética (1948 e 1949, mata-mata) e DDR-Oberliga (1949/50 a 1990/91; a última temporada, já depois da reunificação, como NOFV-Oberliga). Ano civil de 1956 a 1960, depois da rodada de transição de 1955. A federação alemã (DFB) não conta esses títulos como alemães: competição à parte.

## 2. Fontes e regras

**Fontes:**

- RSSSF (Andreas Werner e outros): página de cada temporada, com rodada, data e placar de cada jogo e a tabela final; lista de campeões e de artilheiros;
- Wikipédia (en): tabela e matriz de resultados de cada temporada (conferência) e as fichas dos jogos de 1948 e 1949.

**Regras da importação:** 2 pontos por vitória. Jogo dado fora de campo: vitória e 2 pontos para um lado, gols 0:0 (como a RSSSF), marcado `awd`. Cada tabela publicada é comparada com a calculada dos jogos; a ordem da classificação final é a da tabela da RSSSF (sem ela, a da Wikipédia).

**Desempate:** o critério calculado que reproduz a ordem oficial (saldo de gols em 40, média de gols em 1, confronto direto em 1).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 65 tabelas fecham com os jogos e 19 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1948, 1949, 1949/50, 1953/54, 1961/62, 1973/74.
- Temporadas com alguma tabela divergente: 1949/50, 1950/51, 1951/52, 1953/54, 1956, 1958, 1961/62, 1962/63, 1963/64, 1966/67, 1967/68, 1968/69, 1973/74, 1974/75, 1990/91.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1940s | 198 | 8% | 0% | 92% | 8% | 8% | 0% | 0% | 0% | 0.0 |
| 1950s | 2131 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1911 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 1820 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 1820 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 182 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1948 a 1949: 10 clubes
- 1949/50: 14 clubes
- 1950/51: 18 clubes
- 1951/52: 19 clubes
- 1952/53: 17 clubes
- 1953/54: 15 clubes
- 1954/55 a 1990/91: 14 clubes

**Pontos por vitória:**

- 1948 a 1990/91: 2

**Nome oficial:**

- 1948 a 1949: Ostzonenmeisterschaft
- 1949/50 a 1989/90: DDR-Oberliga
- 1990/91: NOFV-Oberliga

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1948: Eliminatória (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico)
- 1949: Eliminatória (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols, gols pró: 40 temporadas
- resultado: 6 temporadas
- pontos, média de gols: 1 temporadas
- pontos, confronto direto, saldo de gols: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1955: rodada de transição (Übergangsrunde) no segundo semestre de 1955, para passar ao ano civil; o primeiro colocado (Wismut Karl-Marx-Stadt) não é contado como campeão

## 6. Campeões, rebaixados e punições

**Títulos:**

- BFC Dynamo: 10
- Dynamo Dresden: 8
- Vorwärts Frankfurt/Oder: 6
- Erzgebirge Aue: 3
- Carl Zeiss Jena: 3
- 1. FC Magdeburg: 3
- FSV Zwickau: 2
- Hallescher FC: 2
- Chemie Leipzig: 2
- Rot-Weiß Erfurt: 2
- Chemnitzer FC: 1
- Hansa Rostock: 1
- Sem campeão: 1955

**Rebaixamentos:** 87 no total; quem mais caiu: Union Berlin (6), Lokomotive Stendal (5), Hallescher FC (5), Hansa Rostock (5), Chemie Leipzig (5).

**Punições em pontos:**

- 1949/50: Rot-Weiß Erfurt 1
- 1949/50: Lokomotive Stendal -1
- 1953/54: Chemie Leipzig -1
- 1953/54: Stahl Thale 1
- 1961/62: Erzgebirge Aue -2
- 1966/67: Wismut Gera -2
- 1967/68: Vorwärts Frankfurt/Oder -2
- 1967/68: Erzgebirge Aue -11
- 1973/74: Stahl Riesa -2
- 1990/91: BFC Dynamo 4

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/gdr-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1951/52:** a tabela final da RSSSF de 1951/52 não traz o 3º, o 4º e o 5º colocados: a ordem e a conferência ficam com a tabela da Wikipédia

### Edições sem título oficial (`SEM_TITULO`)

- **1955:** rodada de transição (Übergangsrunde) no segundo semestre de 1955, para passar ao ano civil; o primeiro colocado (Wismut Karl-Marx-Stadt) não é contado como campeão

## 8. O que não deu para coletar

- Autores dos gols, público e estádio dos jogos da Oberliga (a RSSSF traz só o placar).
- A primeira fase (campeonatos estaduais) de 1948 e 1949.

## 9. Pendências e próximos passos

- Autores dos gols, público e estádio dos jogos da Oberliga: a RSSSF traz só o placar; fonte possível: as fichas do weltfussball.de ou o arquivo do jornal Neues Deutschland.
- 1948 e 1949: só a fase final (mata-mata entre os campeões estaduais); os campeonatos estaduais ficam de fora.
- Punições de pontos que só a tabela da RSSSF traz (1966/67, 1967/68, 1973/74, 1990/91): os pontos oficiais vão para a classificação e a diferença para ajuste_pontos; o motivo de cada uma não está nas fontes.

## 10. Arquivos

- Código: `coleta/gdr-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_gdr.py`.
- Fontes baixadas: `data/coleta/gdr-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-gdr-1/`.
- Pacote: `data/coleta/gdr-1/pacote/`; relatório: `docs/coleta/gdr-1.md`.
- Refazer do zero: `python coleta/gdr-1/baixar.py ...` (ver o docstring), `python coleta/gdr-1/importar.py`, `python coleta/comum-europa/testar_carga.py gdr-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

