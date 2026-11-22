# Plano de correção — coleta Brasil

Para: agente 2 (coleta Brasil). Revisão profunda de 22/11/2026.
Competições: Paulista (`bra-sp-1`), Paulista A2 (`bra-sp-2`), Série C, Série D e Copa do Brasil.

## Como usar

1. Só comece quando o Guilherme mandar corrigir.
2. Corrija na ordem deste plano: primeiro "ERRADO NO AR", depois cada competição de cima para baixo.
3. Cada linha é um resumo. A sugestão completa (valor certo, fonte, lugar no código) está no `docs/revisao/achados.csv`,
   coluna `o_que_a_fonte_diz`, depois de "SUGESTÃO:".
4. Ids marcados "espera D-xx" não se mexem até o Guilherme responder (`docs/revisao/decisoes-guilherme.md`).
5. Identifique jogos por competição + data + clubes, nunca pelo `partida_id`.
6. Depois de cada bloco: `python coleta/<slug>/importar.py`, `python coleta/comum/testar_carga.py <slug> <scratch>`,
   `python coleta/comum/documentar.py`.
7. No fim: escreva os ids corrigidos em `docs/coleta/pedidos.md` e rode as varreduras
   `python -I revisao/tela/varredura.py` e `python -I revisao/tela/datas_repetidas.py` (copie e troque a lista de
   competições). O agente 1 recarrega o banco e publica.

## ERRADO NO AR (altos já visíveis no site)

> **Atualização de 22/11:** o Paulista A2 (`bra-sp-2`) foi publicado às 11:18 (commit fed171c), com os erros do pacote.
> Entram também no ar: A2-001 a A2-011. Priorize do mesmo jeito.


Só o Paulista (`bra-sp-1`) está no site com erro alto. A A2 não está publicada.

- SP-011 (alta): tirar o jogo falso "Paulista 127 x 0 LAF" de 1928 LAF (vira recorde de goleada).
- SP-002 (alta): vices errados em 14 edições (ordem final não usa a fase final).
- SP-007 (alta): repescagem e torneio de rebaixamento contam como fase final (1951, 1998, 1999, 2003).
- SP-008 (alta): fase final não decide a ordem (1957, 1976, 1978, 1997, 2024, 2025).
- QS-001 (alta): jogos de clube que abandonou contam na tabela (1913 LPF, 1914 LPF, 1927 LAF e outros).
- QS-006 (alta): 1916 APEA, 2 jogos fora da tabela contam; vice errado.
- SP-010 (alta): 1927 LAF com 5 clubes de outra disputa; vice certo é o Hespanha.
- QS-015 (alta): 12 jogos com pontos dados fora de campo não aplicados (1915 a 1990).
- SP-013 (alta): 1930, Palmeiras vice sem a perda de 2 pontos; vice certo São Paulo.
- QS-005 (alta): 1906, faltam os pontos das desistências de SPAC e Mackenzie; vice errado.
- SP-009 (alta): 1927 APEA, 13 jogos do Corinthians de Santo André gravados como Corinthians.
- SP-012 (alta): 1942, falta Corinthians x Palmeiras; vice certo Corinthians.
- SP-001 (alta, espera D-07): 1973 só com a Portuguesa campeã; a FPF conta Santos e Portuguesa.

Só no banco (a tela não mostra a marca "rebaixado"): SP-015.

## Paulista 1ª divisão (`bra-sp-1`) — 41 ids

### `coleta/bra-sp-1/importar.py`
1. OGOL_IGNORAR (5 min)
   - SP-011 (alta): `OGOL_IGNORAR['2591655']`; some também o clube "LAF".
2. ORDEM, FASE_JOGO e desempate pela fase final (1 h)
   - SP-002 (alta): vices pela fase final (lista no achado).
   - SP-007 (alta): "Repescagem" e "Torneio de rebaixamento" com nível 0 no ORDEM.
   - SP-008 (alta): FASE_JOGO por data (1976, 1978, 1981, 1998, 2003); 2024-2025 pela fase/grupo da FPF.
   - SP-003 (média): 3º lugar sai junto (lista em `revisao/SP/saida_podio.txt`).
3. Jogos cancelados e anulados: RSSSF_FORA e JOGOS_ANULADOS (1 h)
   - QS-001 (alta): tirar os jogos cancelados (lista "cancelado no FN" em `revisao/QS/fn_diferencas.csv`).
   - QS-006 (alta): 1916 APEA, tirar Ypiranga 5-3 Mackenzie e AA das Palmeiras 1-4 Palestra.
   - SP-010 (alta): 1927 LAF com 10 clubes; tirar Corinthians, Independência, Sírio, Sílex e Taubaté.
   - QS-013 (baixa): 1956, tirar o Taubaté 2-2 Corinthians repetido (conferir antes).
4. PONTOS_FORA_DE_CAMPO (novo) e `campanha()` contando o awd (1 h)
   - QS-015 (alta): 12 jogos com o vencedor dos pontos; placar de campo na observação.
   - SP-013 (alta): 1930, Palestra 1-0 Corinthians (04/05/1930) com os pontos tirados.
   - QS-005 (alta): 1906, tirar SPAC 1-9 Internacional e pôr 7 W.O.
   - SP-016 (média): W.O. sem placar contam como vitória sem gols.
   - SP-017 (baixa): 1984 doping (São Paulo 3º); 1971 desempate por saldo; 2008 São Paulo 3º.
5. Casamento de nomes e jogos do ogol: `mapear_nomes()` e `juntar_ogol()` (2 h)
   - SP-009 (alta): 13 jogos de volta ao Corinthians de Santo André; tirar o 2º Palmeiras x Corinthians de 21/08.
   - SP-014 (média): 1988, Juventus/Bandeirante no 2º turno; 21 jogos cancelados fora.
   - QS-009 (média): jogo "abd" sem "result stands" fica sem placar (2000, 2004).
   - QS-004 (média): 1969, Corinthians 1-1 Santos no 2º turno, não 1-3 na Final.
6. JOGOS_EXTRA (novo, 30 min)
   - SP-012 (alta): 1942 Corinthians 3-1 Palmeiras (04/10/1942).
   - QS-007 (média): 10 jogos que faltam (1916 LPF, 1920, 1929 LAF, 1942, 1957, 1966).
   - SP-018 (média): 1929 LAF, AA das Palmeiras 3-2 Atlético Santista.
   - SP-019 (média): os totais por edição saem dos itens 3, 4 e 6.
7. Datas (1 h)
   - QS-008 (média): de 2007 em diante, data da FPF (68 jogos).
   - QS-002 (média): 1929 LAF "1959" vira 1929 (também em `rsssf_sp1.py`).
   - QS-003 (média): 1979 "1978" vira 1979 (também em `rsssf_sp1.py`).
   - SP-021 (baixa): rodar de novo `revisao/SP/datas_repetidas.py` depois das datas.
8. Placares e desempate
   - QS-012 (média): 7 placares (1952 x2, 1981, 1995, 1998, 1999, 2014) pelo Futebol Nacional + ogol (2014: FPF).
9. CORRIGE_OGOL (só depois da decisão)
   - SP-026 (média, espera D-23): juntar AA São Bento (1933).
   - SP-027 (baixa, espera D-23): juntar CA Paulista (1935 LPF); tirar sobras 233382, 81019, 999999 do `clubes_ogol.json`.

### `coleta/bra-sp-1/pacote.py`
- SP-015 (alta): `rebaixados_rsssf()` pela infobox pt e pela A2 do ano seguinte (2014-2024; tirar 1994, 1998, 1999, 2002).
- QS-010 (média): `artilheiros()` ler a `sptops.htm` por colunas (hoje lê 0 linhas).
- SP-023 (média): artilheiros de 2001-2026 saem com o QS-010 + FPF.
- SP-024 (média): artilheiros de 1902-2021 saem com o QS-010.
- QS-011 (baixa, espera D-17): base da lista de artilheiros.
- SP-022 (baixa): observações em português (`gravar()` + `coleta/comum/observacao.py`).

### `coleta/bra-sp-1/rsssf_sp1.py` (rsssf.CORRECOES)
- Linhas para QS-002, QS-003, QS-004, SP-010 e SP-012 (já listados acima).

### `coleta/bra-sp-1/edicoes.py` e leitor da FPF
- SP-004 (média, espera D-01): edição de 2026 pela API da FPF (o mesmo leitor serve ao SP-008 e ao QS-008).

### Sem ação ou só anotar
- ~~SP-020~~ FECHADO em 22/11 (`nao-e-erro`): o Futebol Nacional confirma o pacote; quem erra é a Wikipédia pt.
- QS-014 (baixa): datas em dúvida (1930, 1977, 1978, 1990): manter.
- SP-005 (média, espera D-09): amadores da FPF 1933-1934.
- SP-006 (baixa, espera D-16): "Paulistinha".
- SP-001 (alta, espera D-07): 1973 dividido.

## Paulista A2 (`bra-sp-2`) — 28 ids

Não está no site. O importador é cópia do Paulista: faça o item 2 do Paulista e este item 2 juntos.

### `coleta/bra-sp-2/importar.py`
1. Identidade (minutos)
   - A2-010 (alta): 2002, `NOME_MANUAL[("2002","Portuguesa")] = 3406` (Portuguesa Santista), sem acesso.
2. Ordem da classificação final: tabela da última fase antes dos pontos totais
   - A2-002 (alta): 1979 vice Santo André.
   - A2-003 (alta): 1986 vice Noroeste.
   - A2-004 (alta): 1996 vice Portuguesa Santista.
   - A2-005 (alta): 1997 vice Ituano.
   - A2-006 (alta): 2013 vice Rio Claro (finalista em 2º).
   - A2-018 (média): 2004, separar a 2ª fase; 3º Taquaritinga.
   - A2-024 (baixa): 3º e 4º = semifinalistas (1954, 1966, 1987, 1993, 2006).
3. Jogos
   - A2-014 (média): 2008, tirar o Mogi Mirim 0x0 Oeste anulado pelo TJD.
   - A2-026 (baixa): 1998 XV de Piracicaba: manter "rebaixado" e pôr a observação.
   - A2-012 (média, espera D-04): playoffs A1 x A2 de 1979, 2002, 2003.

### `coleta/bra-sp-2/pacote.py`
- A2-009 (alta): acesso não conta quem só jogou repescagem na A1 (1950, 1979, 2001, 2002).
- A2-008 (alta): 1999, "Relegation Playoff" não é queda (Juventus e Paraguaçuense).
- A2-007 (alta): rebaixados pela infobox da Wikipédia pt (baixar 1994-2026); lista em `revisao/A2/rebaixados_wiki.py`.
- A2-021 (média): artilheiros de 1998, 2003 e 2026 pela Wikipédia pt (junto do A2-007).

### `coleta/bra-sp-2/rsssf_sp2.py`
- A2-011 (alta): 2001, ler a tabela publicada (regra de 2001) e -5 do Sãocarlense.
- A2-017 (média): 2001 Nacional-SP 0x1 Ituano (depende do A2-011).
- A2-013 (média): 2006, juntar o jogo interrompido e os 45 min restantes.
- A2-016 (média): 2021 rodada 7 em 24/04.
- A2-019 (média): 2023, pênaltis 3-2 da final.

### `coleta/comum/rsssf.py` + `importar.py` (datas; mexe no comum: reimportar C, D, Copa, Paulista e A2)
- A2-015 (média): datas herdadas de outra rodada (1987, 1998, 1999, 2010, 2011, 2025).

### `coleta/bra-sp-2/wikipedia_sp2.py` e `jogos_pt.csv`
- A2-020 (média): prorrogação das finais de 1961 e 1962.

### Edições 1967-1978 e 1980-1984 (maior custo, maior ganho)
- A2-001 (alta): 17 edições como "jogos incompletos"/"sem jogos"; campeão pela FPF; páginas da RSSSF não linkadas
  e Wikipédia pt. Antes: D-23 (São José 1972 x 1980).
  Arquivos: `baixar_rsssf.py`, `edicoes.py`, `antigas_sp2.py`, `wikipedia_sp2.py`.

### `coleta/bra-sp-2/clubes_sp2.py`
- A2-025 (baixa): grafias em FICHA_CORRIGIDA (80977, 34451); cidade do Oeste espera D-03.
- A2-022 (média, espera D-23): Catanduvense.
- A2-023 (média, espera D-23): Barueri x Grêmio Prudente.

### Só anotar
- A2-027 (baixa): datas impossíveis da própria RSSSF (1985-1988).
- A2-028 (baixa): final de 2011 sem pênaltis; manter e anotar.

## Série C (`bra-serie-c`) — 8 ids

### `coleta/bra-serie-c/importar.py` (e `coleta/comum/ogol.py`)
- QC-011 (média): PLACAR_MANUAL 2007-07-14 ABC 4x0 Vera Cruz-PE.
- QC-002 (média): 58 datas (jogo noturno com +1 dia) + conferir 37 de 2026; ou corrigir no `ogol.py` para todas.
- QC-012 (baixa): 17 placares; trocar só com uma 4ª fonte (lista `revisao/QC/saida_placar_4fontes.txt`).
- SC-016 (baixa): 9 dos 12 viram `nao-e-erro` (o Bola confirma); 3 esperam D-13.
- SC-021 (baixa): 1995, 2011, 2012 e gols de 2001 são `nao-e-erro`; 1999 explicar em `explicacoes.py`; 2002 e 2008 conferir.
- SC-018 (baixa, espera D-02): ordem dos eliminados.

### `coleta/bra-serie-c/clubes_c.py`
- QC-009 (baixa, espera D-03): "Santo Amaro-PE" em 1981.
- CL-028 (baixa): UF e cidade (Botafogo-DF no DF; AA Araguaia em Água Boa-MT; Alegrense; 6 grafias). Parte é da D.

## Série D (`bra-serie-d`) — 3 ids

### `coleta/bra-serie-d/importar.py`
- QC-001 (média): 17 disputas de pênaltis em CORRECAO_JOGO (chaves `pm`/`pv`).
- SD-011 (baixa): semifinal 2013 Botafogo-PB x Salgueiro em 2013-10-06 (súmula da CBF).
- QC-003 (média): 14 datas + conferir 23 de 2026.

## Copa do Brasil (`bra-copa-do-brasil`) — 5 ids

### `coleta/bra-copa-do-brasil/importar.py`
- QC-005 (média): 1995 Nacional-AM 1x0 Cristal; 1998 Bahia 1x2 Botafogo-PB (exceções à regra do ogol).
- QC-004 (média): 20 datas (2008, 2014, 2015, 2018, 2024; lista `revisao/QC/saida_datas_3fontes.txt`).
- CB-007 (média, espera D-14): preliminar de 1999.
- CB-005 (média, espera D-13): 1990 e 1991 esperam o jornal; 2002 fica.

### `coleta/comum/documentar.py`
- QC-008 (baixa): texto da pendência de 1999 (depois de D-14).

## Todas as coletas Brasil — 2 ids

### `coleta/comum/`
- QC-006 (baixa): 100 datas em que ogol e Bola concordam contra a RSSSF (lista `revisao/QC/saida_datas_ogol_bola.txt`).
- QC-007 (baixa): 4 observações em inglês (`observacao.py`) e notas de rodapé no `gols_texto` (`rsssf.py`/`gols.py`).

## Esperando decisão do Guilherme

- D-01 (edições de 2026): SP-004.
- D-02 (ordem final com fase final): SC-018.
- D-03 (nome e cidade da época): QC-009, A2-025 (só a cidade do Oeste).
- D-04 (play-offs fora da liga): A2-012.
- D-07 (títulos divididos): SP-001.
- D-09 (títulos que a federação não reconhece): SP-005.
- D-13 (placares com fontes divididas): SC-016 (3 jogos), CB-005.
- D-14 (Copa 1999, preliminar): CB-007, QC-008.
- D-16 ("Paulistinha"): SP-006.
- D-17 (artilheiros): QS-011.
- D-23 (identidade de clubes, Brasil): SP-026, SP-027, A2-022, A2-023, A2-001 (só o São José).

## Fontes novas a usar

Detalhes em `docs/revisao/fontes.md`.
- Futebol Nacional: cancelados, W.O., pontos fora de campo, jogos que faltam, 3ª opinião de placar e data (Paulista; C, D e Copa).
- FPF (API do site): datas oficiais, fase e grupo 2007-2026; artilharia; 2026; campeões da A2.
- Bola n@ Área: pênaltis, datas, público, árbitro e autores das C, D e Copa.
- Wikipédia pt: rebaixados e artilheiros da A2; edições 1967-1984.
- RSSSF Brasil: `sptops.htm` (artilheiros) e páginas da A2 não linkadas.
- Transfermarkt: 3ª opinião de datas da C, D e Copa.
- Súmulas da CBF (PDF): data e placar oficiais 2013+.
- Hemeroteca Digital: só para os empates de fonte (D-13, D-14).

Cobre 86 de 86 ids abertos de `coleta-brasil` no `achados.csv` (22/11/2026; os fechados na conferência final estão riscados).
