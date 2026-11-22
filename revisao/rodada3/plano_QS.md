# Plano de correção: Campeonato Paulista, 1ª divisão (bra-sp-1), revisor QS, 22/11/2026

Todos os ids abertos (SP-001 a SP-029 da 2ª rodada, menos SP-025 corrigido e SP-030 a SP-032 não-é-erro; QS-001 a QS-015 desta rodada).
Ordem: gravidade x tamanho do erro x custo. [NO AR] = alto já visível no site (https://clubeanalitico.pages.dev/?c=bra-sp-1).
Sugestões completas: `SCRATCH/achados_QS.csv` (QS) e `SCRATCH/sugestoes_QS.csv` (SP). Simulações: `revisao/QS/sim_ordem.py --modo3` (vice/3º) e `revisao/QS/sim_cancelados.py`.

## coleta-brasil

### 1. `coleta/bra-sp-1/importar.py` (quase tudo é aqui)
1. **OGOL_IGNORAR** (5 min): SP-011 [NO AR] — `{'2591655': ...}` tira o "Paulista 127-0 LAF" (recorde falso de goleada). Fonte: `data/coleta/bra-sp-1/ogol/sp1_1928_LAF.json`; Futebol Nacional (133 jogos em 1928 LAF).
2. **ORDEM, FASE_JOGO e desempate pela Fase final** (1 h): SP-002 [NO AR], SP-007 [NO AR], SP-008 [NO AR], SP-003.
   - ORDEM com todas as fases (turnos, sub-turnos, "Fase única", "Fase/Torneio de Classificação" = 1; "Repescagem", "Torneio de rebaixamento", "Desempate" = 0) e `ORDEM[p.fase]` no lugar de `ORDEM.get(p.fase, 50)`.
   - FASE_JOGO por data: 1976, 1978, 1981, 1998, 2003 (lista no SP-002 de `sugestoes_QS.csv`); 2024 e 2025 pela fase/grupo da API da FPF (SP-008).
   - Vice do quadrangular final (1997) e desempate pelos pontos da "Fase final" (1957).
   - Medido: vices 119 -> 125, 3º 97 -> 105, nenhuma piora. Vale também para `coleta/bra-sp-2/importar.py` (cópia).
3. **Jogos cancelados e anulados: RSSSF_FORA / JOGOS_ANULADOS** (já existem, vazios) (1 h): QS-001 [NO AR] (1913 LPF vice e 3º, 1914 LPF 3º, 1927 LAF vice; 1923, 1924, 1925, 1928 APEA, 1935 APEA, 1938), QS-006 [NO AR] (1916 APEA vice), SP-010 [NO AR] (1927 LAF), parte do SP-014 (21 cancelados de 1988), QS-013 (1956). Fonte: Futebol Nacional (lista "cancelado no FN" em `revisao/QS/fn_diferencas.csv`) e RSSSF sp1916.htm.
4. **PONTOS_FORA_DE_CAMPO (novo) + `campanha()` contando o awd** (1 h): QS-015 [NO AR] (12 jogos de 1915 a 1990), SP-013 [NO AR] (1930: é o Palestra 1-0 Corinthians de 04/05/1930), SP-017 (1984 doping), SP-016 (W.O. fora da tabela), QS-005 [NO AR] (1906: desistências de SPAC e Mackenzie). Fonte: Futebol Nacional (nota de cada jogo: "X ganhou os pontos da partida").
5. **Casamento de nomes e jogos do ogol** (`mapear_nomes()`, `juntar_ogol()`) (2 h): SP-009 [NO AR] (1927 APEA, Corinthians de Santo André; o FN confirma o 11-2 de 17/07 contra o de Santo André), SP-014 (1988, Juventus/Bandeirante no 2º turno), QS-009 (2000 e 2004: jogo abandonado com o placar do ogol, conta em dobro), QS-004 (1969, jogo repetido da RSSSF casado com o 1-1 do ogol).
6. **JOGOS_EXTRA (novo)** (30 min): SP-012 [NO AR] (04/10/1942 Corinthians 3-1 Palmeiras), QS-007 (1916 LPF 4 W.O., 1920 2 W.O., 1929 LAF, 1957, 1966), SP-018 (1929 LAF), QS-005 (W.O. de 1906), SP-019 (os totais saem daqui). Fonte: Futebol Nacional.
7. **Rebaixados** — ver `pacote.py` abaixo (SP-015 [NO AR]).
8. **Datas** (`juntar_ogol()`: ramo "ano_errado" fica com o ano da edição; de 2007 em diante, data da FPF) (1 h): QS-008 (68 jogos 2007-2025; lista em `revisao/QS/fpf_comparar_saida.txt`), QS-002 (1929 LAF "1959"), QS-003 (1979 "1978"), SP-021 (rodar `revisao/SP/datas_repetidas.py` depois).
9. **Placares** (`decidir_placar()` ou CORRECOES) (30 min): QS-012 (1952 x2, 1981, 1995, 1998, 1999, 2014: Futebol Nacional + ogol, e a FPF em 2014).
10. **Desempate por época** (CRITERIO_ANO / ORDEM_MANUAL) (30 min): SP-017 (1971 saldo; 2008).
11. **CORRIGE_OGOL** (depois da decisão): SP-026 (`('1933','233382') -> '39622'`), SP-027 (`('1935 LPF','81019') -> '275483'`); tirar as sobras do `data/coleta/comum/clubes_ogol.json` (233382, 81019, 999999 "LAF").

### 2. `coleta/bra-sp-1/pacote.py`
1. **rebaixados_rsssf()** (30 min): SP-015 [NO AR] — infobox pt "rebaixados" e participação no bra-sp-2 do ano seguinte; 1998/1999 só os 2 últimos do quadrangular da morte.
2. **artilheiros()** (30 min): QS-010 (a expressão regular lê 0 linhas da sptops.htm), SP-023, SP-024, QS-011 (decisão da base). Fonte: `data/coleta/bra-sp-1/rsssfbrasil/sptops.htm` (1902-2021) + FPF ListarArtilharia.ashx (2022-2026, `revisao/QS/fpf_artilharia.json`).
3. **Observações em português** (`gravar()` + `coleta/comum/observacao.py`) (30 min): SP-022.

### 3. `coleta/bra-sp-1/rsssf_sp1.py` (rsssf.CORRECOES)
- sp1929.htm "09/06/1959" -> "09/06/1929" (QS-002); sp1979.htm "19.08.78" -> "19.08.79" (QS-003); sp1969.htm: tirar a linha repetida "08/jun Corinthians 1-3 Santos" (QS-004); sp1927.htm: cortar o trecho da LAF onde ele acaba (`_sem_trecho`, SP-010); sp1942.htm (SP-012, se o jogo estiver na página).

### 4. `coleta/bra-sp-1/edicoes.py` e leitor da FPF (depois da decisão)
- SP-004: edição 2026 (API da FPF: jogos com fase e grupo, artilharia). O mesmo leitor serve para SP-008 (2024-2025) e QS-008 (datas).

### 5. Esperam o Guilherme (`SCRATCH/decisoes_QS.md`)
- SP-001 [NO AR] (1973 dividido; recomendação: dois campeões, como a FPF), SP-004 (2026: entra), SP-005 (1933/1934 FPF: não reconhecer), SP-006 ("Paulistinha": não entra por agora), SP-026 e SP-027 (juntar), QS-011 (base dos artilheiros: RSSSF + FPF).

### 6. Sem ação ou só se aparecer fonte nova
- SP-020: o Futebol Nacional confirma o pacote em 1904, 1905, 1946 e 2021 (marcar não-é-erro); 1916 LPF Corinthians x Americano de 03/12 não existe no FN.
- QS-014: datas em dúvida (1930, 1977, 1978, 1990).
- SP-019: totais saem dos itens 3, 4 e 6 acima (o infobox da pt erra 1921, 1958 e 1960).

## banco-painel
1. Depois de cada pacote novo: recarregar `bra-sp-1` (`futebol/carregar_pacotes.py`) e publicar.
2. SP-001: aceitar dois campeões na edição (se o Guilherme decidir).
3. SP-028 (nomes e cidades: Red Bull Brasil, Humberto Primeiro, São Caetano EC, nomes de outro clube em `clube_nome`).
4. SP-029 (escudo do Oeste: `python baixar_escudos.py`; "LAF" some com o SP-011).

## Fontes a usar
- **Futebol Nacional** (todas as edições, 1 página por edição): cancelados, W.O., pontos dados fora de campo, jogos que faltam, terceira opinião de placar e data, artilheiro.
- **API da FPF** (2007-2026): data oficial, fase e grupo, artilharia; súmulas (árbitro, cartões, gols) 2016+.
- **RSSSF sptops.htm** (já no disco): artilheiros 1902-2021.
- **transfermarkt** (BCP1, 2006+): árbitro, público e cartões 2006-2015, se o Guilherme quiser esses campos.
