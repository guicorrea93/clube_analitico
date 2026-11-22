# Revisão: Brasileirão Série B (bra-serie-b)

Revisor SB, 20/11/2026. Conferido o painel gerado às 19:07 (dados `painel/dados/bra-serie-b.js`) e o `db/futebol.db` (18:11).

**Resumo.** Lista de edições, campeões e quase toda a classificação de 2006 a 2025 estão certas; os placares de 2007 a 2025 batem com a Wikipédia pt.
Há 5 achados altos: vice errado em 1999, 2001 e 2004 (a classificação calculada soma pontos de todas as fases em vez de usar o quadrangular final), 2001 com os 4 clubes da repescagem em 9º-12º e 2009 com Juventude em 16º (dois 16º).
Também há 7 jogos duplicados em finais antigas, 4 placares errados, gols contra do lado errado em 2013, artilheiro do painel diferente do oficial em 24 edições e pontos sem punição na sub-aba Classificação.

Achados: `SB-001` a `SB-025` (21 abertos: 5 altos, 8 médios e 8 baixos; mais 4 conferências que deram certo, como `nao-e-erro`). Scripts em `revisao/SB/`, páginas em `data/cache/revisao/SB/`.

Fontes usadas (diferentes da base da coleta, que foi RSSSF Brasil, ESPN, ogol e en.wikipedia de 2016 em diante): Wikipédia pt (página da Série B, páginas de cada edição e predefinições "Tabela do Campeonato Brasileiro da Série B - AAAA"); en.wikipedia para as edições sem página pt (1992, 1996, 1997) e para desempate (1971, 1999, 2001, 2003, 2004, 2008, 2009, 2022). A rsssf.org não tem páginas da Série B (404).

## A. Edições e títulos

- **Lista de edições:** 44, igual à lista oficial da CBF (1971, 1972, 1980-85, 1988-92, 1994-99, 2001-25), com 1980-84 como Taça de Prata. Não há Série B oficial em 1973-79, 1986, 1987, 1993 e 2000. Resultado: ok (`SB-022`).
- **Campeões:** 44 de 44 certos.
- **Vices:** 41 de 44 certos. Errados: 1999 (painel Bahia, certo Santa Cruz) `SB-001`; 2001 (painel Caxias, certo Figueirense) `SB-002`; 2004 (painel Bahia, certo Fortaleza) `SB-004`. Por causa disso, o cartão "32 vices" e o Pódio (Bahia com 2 vices, Caxias com 1, Fortaleza só com 1) também ficam errados.
- **3º lugar:** 2006-2025, 20 de 20 certos. 2022 Bahia 3º confere com as tabelas pt e en (`SB-023`; só a lista resumida da en.wikipedia diz Vasco). Antes de 2006, conferidos onde há quadrangular final publicado: 1995, 1996, 1997, 1998, 2002, 2003 e 2005 certos; 1999, 2001 e 2004 errados (mesmos achados). Nas edições com semifinal não há 3º oficial: o painel usa a campanha.
- **Novorizontino:** separação certa. GE Novorizontino em 1989, 1991 e 1995; Grêmio Novorizontino de 2022 a 2025 (`SB-024`).
- Fontes: https://en.wikipedia.org/wiki/Campeonato_Brasileiro_Série_B (Official/Unofficial champions), https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_-_Série_B.

## B. Classificação final

- **2006-2025 (20 edições), tabela inteira contra a Wikipédia pt (posição, J, V, E, D, GP, GC e pontos):** 15 certas, sem nenhuma diferença. Diferenças:
  - 2009: Juventude 16º com 47 pts; o certo é 17º com 44 (pt e en). São dois 16º no painel (`SB-005`, alta).
  - 2006 e 2008: um placar errado em cada ano, que muda a linha de dois clubes no painel (`SB-009`, `SB-010`).
  - 2007, 2008 e 2009: o banco (`classificacao_final`) copiou erros de digitação da RSSSF. O painel calcula pelos jogos e mostra certo (`SB-015`).
  - 2021: Brusque com -3 no banco, 48 pts sem punição na pt. Fica em dúvida (`SB-016`).
- **Antes de 2006, amostra:** 1971, 1980-85, 1988, 1990, 1994-99, 2001-05 contra a pt ou a en.
  - 2001: os 4 da repescagem do rebaixamento aparecem em 9º-12º (`SB-003`, alta).
  - 1999 e 2004: ordem do quadrangular final errada (`SB-001`, `SB-004`).
  - 1971, 1981, 1990, 1992 e 1994: números a mais por causa de jogos duplicados (`SB-006`).
  - 1998: W.O. invertido (`SB-007`). 1994: placar invertido (`SB-008`).
  - Nas demais, só diferenças pequenas de posição entre clubes eliminados juntos. As próprias tabelas da pt são calculadas e às vezes inconsistentes (ex.: 1985), então não registrei essas diferenças.
- **Punições:** o banco tem os ajustes (2003, 2006, 2007, 2011, 2014, 2020 e 2021), mas a sub-aba Classificação mostra os pontos sem eles e não explica as punições. A Corrida aplica os ajustes (`SB-014`).
- **Acesso e rebaixamento (sub-aba Participantes), todas as edições:**
  - 2006-2024: os 4 que sobem e os 4 que caem conferem com a tabela de cada ano, exceto 2009 (Juventude "caiu" em 16º).
  - 2010 e 2011: Guaratinguetá e Americana aparecem como "não jogou" (`SB-020`, depende da identidade do clube).
  - 2001: Tuna Luso e Sergipe caem em 11º e 12º (`SB-003`).
  - 2025: sem "ano seguinte", porque 2026 não está no banco.
  - Antes de 2006, as colunas dependem das Séries A e C do banco. Em 2001 a coluna "Chegou" fica "—" para quase todos, porque 2000 (Copa João Havelange) não tem o Módulo Amarelo no banco. É limitação, não erro.

## C. Jogos

- **Total por edição:**
  - 2006-2025: 380 em todas as edições, certo.
  - 1980, 1984, 1985, 1988, 1995, 1998 e 2001-05: o total do banco é igual à soma de J/2 da tabela pt.
  - 7 jogos duplicados (1971, 1981, 1990, 1992 e 1994), `SB-006`. 1971: pt dá 74 jogos e 178 gols; o banco tem 78 e 183.
  - Total geral: 13.100 no banco (o painel mostra 13.094, os que têm placar). Sem os duplicados, seriam 7 a menos.
- **Placares e mando:**
  - Recentes, pela matriz de resultados pt: 2007-2025 completos (cerca de 7.180 jogos; 2023 com 370 jogos). Só 2008 tem diferença: 1 erro real (`SB-010`); as outras 3 diferenças são da própria matriz da pt, que não fecha com a tabela dela.
  - Meio: 2003, 36 jogos (2ª fase e fase final), todos iguais. 2001-02: 26 jogos, todos iguais.
  - Antigas: 1985, 48 de 48 jogos iguais. 1980-84: 132 jogos iguais.
  - Outros erros, achados pelas tabelas: 1994 Desportiva x CRB (`SB-008`), 1998 W.O. invertido (`SB-007`) e 2006 Ituano x Vila Nova (`SB-009`).
- **W.O. e tribunal:**
  - 2014 Joinville 3-0 Portuguesa: ok.
  - 1998: o W.O. a favor do Santa Cruz está invertido (`SB-007`).
  - 2001 Figueirense x Caxias: o banco deixa o jogo sem placar. A pt (STJD manteve a vitória) e a en contam 1-0 para o Figueirense (`SB-002`).
- **Datas:** datas repetidas em 1971, 1997 e 1998; jogos sem data em 1985, 1990, 1991, 1994 e 1997 (`SB-017`).
- Fontes: páginas pt de cada edição (seções Confrontos/Resultados e footballbox); scripts `compara_jogos_matriz.py`, `compara_jogos_lista.py`, `total_jogos.py` e `duplicados.py`.

## D. Gols e artilheiros

- **Soma dos gols com autor ≤ placar, em todos os 13.100 jogos:**
  - 7.826 jogos têm algum autor, e em todos a soma fecha com o total do placar.
  - Em 4 jogos de 2013, gols contra estão do lado errado: gravados como gol normal do time do autor (`SB-011`).
- **Artilheiro de todas as edições, contra a lista pt (Artilheiros/Ano a ano) e a en (Top scorers):**
  - O banco (tabela `artilheiro`, da RSSSF) confere em 37 edições. Falta 1971 (Robilotta, 4). 1988-90 não têm registro na pt; a en traz nomes. Em 2004, o banco tem empate Rinaldo e Kuki com 13; pt e en dizem Rinaldo, 14 (`SB-013`).
  - O painel não usa essa tabela: o cartão "Artilheiro" e a sub-aba Artilharia contam os gols com autor do banco. O resultado bate com o oficial em 17 edições (2007, 2008, 2010-15, 2017-25) e difere em 24 (`SB-012`).

| Ano | Painel | Oficial |
|---|---|---|
| 1971 | Luizinho 3 | Robilotta (Remo) 4 |
| 1972, 1981-83, 1991, 1994, 1996-98, 2001, 2009 | sem gols por jogador | Pelezinho 8; Jorge Mendonça 11; Luisinho 10; Lima 9; Cacaio 14; Baltazar/Mário 11; Maurício 13; Tupãzinho 13; Gauchinho 13; Sérgio Alves 21; Elton/Nicácio/Rafael Coelho 17 |
| 1980 / 1984 / 1985 | Osmarzinho 3 / Dadinho 3 / Guilherme e Paulo César 3 | 12 / 6 / 6 |
| 1988 / 1989 / 1990 | Silvio 8 / Dico e Vacaria 3 / Soares 6 | sem registro (pt); en: Machado 11 / Bugrão 7 / Rivelino 11 |
| 1992 / 1995 / 1999 | Saulo 8 / Oséas 6 / Uéslei 13 | 12 / 14 / 25 |
| 2002 / 2003 / 2004 | Vinícius 13 / Valdomiro e Vágner Love 16 / Kuki e Rinaldo 13 | 22 / Vágner Love 19 / Rinaldo 14 |
| 2005 / 2006 / 2016 | Reinaldo 15 / Fumagalli e Vanderlei 19 / Bill 14 | 16 / Vanderlei 21 / 15 |

## F. Painel

- **Prints sem janela (1400 px):**
  - História: corrida, pódio, participações, jogos, gols, pontos e curiosidades.
  - Por campeonato: resumo 1999, classificação 2009, participantes 2001, corrida 2014, jogos 1998 e artilharia 2003.
  - Por clube: resumo Novorizontino, campanhas GE Novorizontino, confrontos Remo, jogos Paysandu e artilharia Coritiba.
  - Celular (420 px): corrida, classificação 2025 e Coritiba.
  - Prints em `SCRATCH/SB/telas/`. Nenhuma tela quebrada nem vazia.
- **Números da História contra o banco:**
  - Participações dos 200 clubes e jogos/V/E/GP/GC por clube (CJV) batem 100%.
  - Cartões do topo (44 edições, 36 campeões, 13.094 jogos, 31.797 gols) batem com o banco. O cartão "32 vices" fica errado por causa de `SB-001`, `SB-002` e `SB-004`.
- **Recordes:** maior goleada Paulista 9 x 0 Paysandu (2006) confere (`SB-025`). Títulos na Corrida conferem (Coritiba 3; Paysandu, Goiás, Palmeiras, América-MG, Bragantino e Botafogo 2).
- **Problemas de texto e tela:**
  - "mata-mata" para quadrangulares finais e nomes de fase em inglês (`SB-018`).
  - "Artilheiro desde 1971" na aba Por clube (`SB-019`).
  - Pontos sem punição na Classificação (`SB-014`).
  - No celular a página fica mais larga que a tela, já conhecido (`SB-021`).
  - Sem escudo: Oeste (pendência já conhecida).
- Observação: segundo a Wikipédia, a Série B 2026 já tem campeão (Novorizontino). Ela não está no banco, e o selo diz "1971 a hoje".

## Perguntas ao Guilherme

1. **Edições não oficiais:** manter fora 1986 (Torneio Paralelo), 1987 (Módulos Azul e Branco), 2000 (Módulo Amarelo da Copa João Havelange) e 1979 (pedido do Maranhão)? Hoje o painel segue a lista oficial da CBF (44).
2. **2001, Figueirense 1-0 Caxias (jogo encerrado por invasão):** contar o 1-0, como a Wikipédia pt e en, ou deixar sem placar, como a RSSSF? O vice oficial é o Figueirense de qualquer forma.
3. **Guaratinguetá (2010 e 2012) e Americana (2011):** são o mesmo clube? Isso afeta a sub-aba Participantes (`SB-020`).
4. **Brusque 2021:** manter -3 pontos? A en diz -3; a tabela pt mostra 48 pts, sem punição (`SB-016`).

## 3ª rodada (22/11/2026)

Revisor QA. Foco: fontes que nenhuma etapa usou, conferidas por década contra o banco (`db/futebol.db`, só leitura). Scripts em `revisao/QA/`, páginas em `data/cache/revisao/QA/`, listas de datas em `revisao/QA/saida/`. O painel local e o publicado são iguais (mesmo md5 de `dados/bra-serie-b.js`).

**Fontes novas e amostra por década** (jogos casados; placar igual / data igual):

| Década | Fonte | Edições | Jogos | Placar | Data |
|---|---|---|---|---|---|
| 1970 | Bola na Área | 1971, 1972 | 205 | 200 | 200 |
| 1980 | Bola na Área | 1980-1985, 1988, 1989 | 1.383 | 1.364 | 1.320 |
| 1990 | Bola na Área | 1990-1992, 1994-1999 | 1.861 | 1.820 | 1.252 |
| 2000 | Bola na Área; Transfermarkt | 2005, 2009 | 647; 611 | 646; 611 | 593; 447 |
| 2010 | Bola na Área; Transfermarkt | 2015 | 380; 342 | 380; 342 | 372; 342 |
| 2020 | Bola na Área; Transfermarkt | 2022 | 378; 380 | 376; 376 | 366; 324 |

As datas foram conferidas em três fontes (banco x Bola na Área x Wikipédia pt até 2004 ou Transfermarkt depois), jogo a jogo, em `revisao/QA/datas_3fontes.py`. Onde BNA e a outra fonte concordam contra o banco, a data sugerida está na coluna `sugestao` de `revisao/QA/saida/datas_bra-serie-b_<ano>.csv`: 1990 35 jogos (os 19 conflitos do ano zeram), 1991 388 (301 sem data; conflitos 35 -> 11), 2009 54, 1981 13, 1982 3. A BNA sozinha erra datas (cria conflitos em 1988, 1989, 1992, 1994, 1995) e alguns placares, por isso só vale com outra fonte.

Achados novos (todos banco-painel):
- **QA-005** (média, decisão): 1971 Grupo A, 12 jogos no banco (RSSSF Brasil) e 10 na pt e na BNA.
- **QA-006** (média): 1972 Atlético-BA 3x1 Central (banco 0x0). BNA, pt e ogol.
- **QA-007** (média): 1981 Flamengo-PI 2x2 Remo em 03/02/1981 (banco 'n/p'). BNA, pt e ogol.
- **QA-008** (média, decisão): 5 placares com fontes empatadas 2 x 2 (1971, 1981, 1991).
- **QA-009** (baixa): 1992 Ceará x Fortaleza com mando trocado nos dois jogos da 1ª fase.
- **QA-010** (média): 1994 Democrata-GV 0x0 Sergipe (banco 1x1). BNA e ogol.
- **QA-011** (baixa): 1982, dois 'awd' sem placar (0x1 nas fontes).
- **QA-012** (média): datas de 2009 (54), 1981 e 1982; 1989, grupo J inteiro em 28/10 porque o ogol chama o clube de 'Esportivo Passense'.

**Artilheiros (SB-013):** a Bola na Área e a Campeões do Futebol confirmam Robilotta 1971 (a BNA põe Horácio empatado), Machado 1988, Bugrão 1989, Rivelino 1990, Rinaldo 14 sozinho em 2004 e 'Bill' em 2016.

**Buracos de cobertura (seção 4):** autores antes de 2003 (parciais), público antes de 2010 e árbitro em todos os anos. As fichas do Transfermarkt têm autores, árbitro e público de 2009 em diante (8 de 9 na amostra); a BNA tem público e autores na Série B 1985 quase inteira e em 2015; antes disso, só a Hemeroteca (jogo a jogo). Custo e caminho em `fontes_QA.md` e `plano_QA.md` (scratchpad).

**Varredura de tela e datas repetidas** (`revisao/QA/varredura.py`, `datas_repetidas.py`): clube com 2 jogos no mesmo dia em 1981 (3), 1989 (9), 1990 (34), 1991 (46), 1997 (2) e 1998 (6), os mesmos do RC-001; 'Grupo Grupo' nas fases de 1971-1989 (só no banco; o painel não repete).

Entregas no scratchpad: `achados_QA.csv` (QA-001 a QA-012; 8 desta competição), `sugestoes_QA.csv` (SB-013, SB-017, CL-024, TL-003), `fontes_QA.md`, `decisoes_QA.md` (QA-D1, QA-D2 e a pergunta antiga das edições não oficiais), `plano_QA.md`.
