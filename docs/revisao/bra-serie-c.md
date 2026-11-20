# Revisão: Brasileirão Série C (bra-serie-c)

Revisor: SC · 20/11/2026 · achados em `SCRATCH/achados_SC.csv` (SC-001 a SC-028) · scripts em `revisao/SC/`

**Resumo.** Os campeões estão certos nas 35 edições. Pacote, banco e painel batem entre si: os 7.912 jogos e as classificações são iguais nos três.
Os erros nascem no pacote, com uma exceção (a artilharia, que é do painel). O vice está errado em 8 edições e o 3º em 13. Faltam os rebaixados de 8 edições.
Há jogos com o clube trocado ou duplicados (1988, 2003, 2004, 2007, 2008). A artilharia do painel só conta os gols com autor, por isso o artilheiro sai errado em 25 edições.
Achados: 2 altos, 14 médios, 10 baixos e 2 que não são erro.

Fontes de conferência: Wikipédia pt, en e es (páginas de cada edição e a página geral da Série C). A coleta usou RSSSF e ogol como base.
As páginas pt/en já estavam guardadas pela coleta (`data/coleta/bra-serie-c/wikipedia/`). As páginas es e pt 2026 foram baixadas em `data/cache/revisao/SC/wiki/`.

## A. Edições e títulos
- **O que foi conferido:** a lista de edições e o nome de cada época; campeão, vice e 3º das 35 edições.
- **Fontes:** infobox pt e en de cada edição; página geral pt (seção Campeões); página geral es.
- **Lista de edições:** 1981, 1988, 1990, 1992, 1994–1999 e 2001–2025 estão certos. 1987 e 2000 ficam de fora, como na CBF e na Wikipédia. A Taça de Bronze está em 1981.
  - **Falta a edição 2026**, que já terminou (24/10/2026, Maringá campeão). O selo do painel diz "1981 a hoje" → SC-001.
- **Campeões:** 35 de 35 certos → SC-027.
- **Vices:** 27 de 35 certos. Erram 1999, 2001, 2002, 2003, 2005, 2006, 2009 e 2020 → SC-002.
  - Causa nas edições com grupo final: a ordem 1–4 vem da campanha toda, quando deveria vir do grupo final.
  - Causa em 2009 e 2020: o outro finalista não ficou em 2º. Em 2020 a final está gravada como "Segunda fase / Grupo D".
- **3º lugar:** 22 de 35 certos → SC-003.

## B. Classificação final
- **Tabelas lidas da Wikipédia:** 507 tabelas pt/en (wikitable e Module:Sports table), com 2.987 linhas de clube. 2.434 linhas são iguais.
  - As tabelas de grupo foram comparadas com a soma dos jogos do pacote na mesma fase.
  - As tabelas "Classificação geral/final" foram comparadas com `classificacao_final.csv`.
  - O resto das diferenças é dos achados abaixo ou ruído de leitura (nomes ambíguos como Esportivo, Rio Branco e América; tabelas acumuladas da en). Lista completa: `SCRATCH/SC/conf_tabelas.txt`.
- **Classificação geral completa contra outra fonte:** 1988, 1990, 1992, 1994, 1995, 1996, 2003, 2008, 2009, 2010, 2011, 2023, 2024 e 2025. Há pelo menos uma por década.
- **Primeira fase de 2012 a 2025:** todos os grupos e a fase única batem 100% com a soma dos jogos.
- **Rebaixamentos:** 8 de 17 edições erradas (2009, 2013, 2016–2021) → SC-004.
  - O painel mostra a queda certa na aba Participantes, porque olha a Série D do ano seguinte.
- **Acessos** → SC-005 (pacote) e SC-006 (painel).
  - Acesso falso em 1981, 1988 e 1990, para quem só jogou a Série B do ano seguinte por convite.
  - Falta o acesso do São Raimundo em 1999.
- **Pontuação de 1988:** a regra foi 3 pontos por vitória e pênaltis no empate (2 para quem vence, 1 para quem perde). O pacote usa 2 pontos → SC-007.
- **Punições ausentes:** 2005 Nacional-PB; 2006 Ulbra, Ypiranga-PE, Ceilândia e Estrela do Norte; 2007 Imperatriz e Nacional-PB → SC-017.
  - Já estão no pacote: Anapolina 2006, Serra 2008, Brasil de Pelotas 2011 e CRAC 2014.
- **Ordem dos eliminados:** na classificação calculada, a ordem difere da Wikipédia em 8 edições → SC-018 (baixa).

## C. Jogos
- **Total de jogos:** pacote, banco e painel têm 7.912 nos três.
  - Contra o infobox da Wikipédia, 30 das 35 edições batem. 2008 e 2011 têm jogos a mais, explicados em SC-010 e SC-013; o resto está em SC-021.
- **Jogo a jogo:** 3.377 jogos do pacote foram achados na Wikipédia (tabelas cruzadas, `match_` e TwoLegResult); 3.284 têm placar igual.
  - A amostra vai de 1981 a 2025 e cobre 27 edições: antigas 1981 (18), 1994 (58), 1995 (125) e 1996 (174); do meio 2003 (111) e 2009 (88); recentes 2017–2025 (100% dos jogos).
- **Clube errado ou jogo duplicado:**
  - 1988: Desportiva-ES no lugar da Ferroviária-SP em 6 jogos → SC-008.
  - 2007: grupo 17 sem o Imperatriz e com a Tuna Luso contra ela mesma → SC-009.
  - 2008: 2 jogos duplicados no grupo 15 → SC-010.
  - 2004: Atlético-BA no lugar do Atlético Sorocaba → SC-011.
  - 2003: Ituiutaba dividido em dois clubes ("Ituiutabana" e "Boa Esporte") → SC-012.
- **Jogos anulados e tribunal:**
  - 2011: 3 jogos do Rio Branco-AC excluído continuam valendo → SC-013.
  - 1995: Itumbiara x Gama tem provável resultado de tribunal → SC-015.
  - Os W.O. e jogos dados no tribunal de 1999, 2003 e 2017 estão certos no pacote.
- **Placares:**
  - Quando RSSSF e ogol divergem, a Wikipédia confirma o ogol em 1988, 1992 e 2003 → SC-014. Em 1992 isso muda o 3º lugar.
  - Divergências só com a Wikipédia (uma fonte, em dúvida) → SC-016.
- **Fases e datas:** "Fifth Phase" em 2003, 1992 e a final de 2020 → SC-019. Ida e volta no mesmo dia → SC-020.

## D. Gols e artilheiros
- **Artilheiro de cada edição:** 35 edições conferidas contra a lista da página pt, a lista da página es e os infobox.
  - O pacote acerta 34 de 35. Falta 1998 (Kléber Pereira, Moto Club, 25) → SC-022.
  - Uma das 34 tem o nome trocado: Jonas Carioca, em vez de Jones Carioca → SC-023.
  - 1988 e 1994 ficam sem artilheiro, o que está certo: a CBF não reconhece.
- **Gols com autor:** a soma nunca passa do placar nos 7.912 jogos, nem no pacote nem no banco → SC-028.
- **No painel:** o artilheiro só sai certo em 9 edições, porque a artilharia ignora a tabela oficial do banco → SC-024.

## F. Painel
- **O que foi visto:**
  - Telas em 1400 px: as 7 sub-abas de História; as 6 sub-abas de Por campeonato em 2009; Participantes de 1988 e 2020; Resumo de 2003; as 5 sub-abas de Por clube (Vila Nova-GO).
  - Telas em 420 px: 3 telas.
  - Erros de JavaScript: 9 rotas, nenhum erro.
  - Prints em `SCRATCH/SC/telas/`.
- **Os números batem com o banco:** cartões, pódio, classificação, participantes e curiosidades (maior goleada 9x0 América-MG x Jataiense, igual à Wikipédia). Os erros que aparecem vêm do pacote (vices, 3º, ABC 3º em 2007...).
- **Achados do painel:**
  - A artilharia vem só dos gols com autor → SC-024.
  - "Subiram para a Série B" aparece em anos sem acesso → SC-006.
  - "Campeão invicto" omite Vila Nova 1996 → SC-025.
  - No celular, a página fica mais larga que a tela (já conhecido) → SC-026.
  - "Fifth Phase" aparece como 1ª fase de 2003 → SC-019.

## Perguntas ao Guilherme
1. Incluir a Série C 2026, que já terminou (Maringá campeão)? (SC-001)
2. 1987 (módulos Azul e Branco) e 2000 (Módulo Verde e Branco da Copa João Havelange) continuam fora, como na CBF e na Wikipédia?
3. 3º lugar quando não houve disputa de 3º: em 2023–2025 os promovidos (vices de grupo) ficam à frente, como na "classificação geral" da Wikipédia? Ou vale a campanha? (SC-003)
4. 2011: os 3 jogos do Rio Branco-AC, excluído pelo STJD, saem da classificação, como na Wikipédia? (SC-013)
5. 1988: usar a pontuação da época (3 pontos, mais os pênaltis no empate)? Isso exige os pênaltis de cada empate. (SC-007)
6. Quando RSSSF e ogol divergem e a Wikipédia confirma o ogol, prevalece o ogol? (SC-014)
