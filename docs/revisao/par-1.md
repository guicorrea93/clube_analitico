# Revisão: Campeonato Paraguaio, 1ª divisão (par-1)

Revisor: PY · 22/11/2026 (3ª rodada, revisão profunda) · achados em `SCRATCH/achados_PY.csv` (PY-001 a PY-031) · scripts em `revisao/PY/`

**Resumo.** Os jogos de 2008 em diante estão muito bons (placares e tabelas batem com a Wikipédia es). O problema está na
classificação e no pódio: 4 campeões errados no painel (1917, 1928, 1936, 1991), 23 vices errados, tabelas parciais cortadas
(1909-1959) e tabelas de uma fase só (1982-1995). Nos anos 60, 152 jogos de copas de pré-temporada entraram no campeonato.

Comparação pacote x banco x site: pacote e banco iguais (133 edições, 7.865 jogos, 13.108 gols com autor, 14.270 cartões).
O `painel/dados/par-1.js` local já é o pacote novo (7.849 jogos com placar); o **site ainda é o pacote antigo** (7.794 jogos)
e, por isso, hoje tem os vices de 1999-2003 e 2020 Clausura certos, que o pacote novo errou (PY-022).

## A. Edições e títulos
- Conferido: as 133 edições, campeão e vice, contra a lista da RSSSF (parachamp) e a Wikipédia es (as duas concordam em
  todos os anos; onde a RSSSF dá dois vices, a Wikipédia escolhe um).
- Edições: certas (1906-2025, sem 1908, 1922, 1932-1934; Apertura e Clausura separados desde 2008). 2026 Apertura já terminou
  e não entrou (PY-027).
- Campeão: `edicoes.csv` e o banco certos nas 133; o painel tira o campeão da 1ª linha da classificação e erra 1917, 1928,
  1936 e 1991 (PY-001, **no ar**): títulos no site Olimpia 46 (certo 47), Libertad 25 (26), Guaraní 12 (11), Nacional 10 (9).
- Vice: 23 errados ou vazios (PY-002): 1909, 1914, 1915, 1917, 1918, 1928, 1936, 1942, 1962, 1966, 1986, 1987, 1989-1992,
  1999-2003, 2005, 2020 Clausura. Causa: o vice é a 2ª linha da tabela (agregada ou parcial), não o da lista. 5 anos com
  vice duplo na lista esperam decisão (PY-028).
- Fontes: https://www.rsssf.org/tablesp/parachamp.html · https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Paraguay

## B. Classificação final
- Sem jogos, 1906-1959 (49 edições): a leitura da tabela de `parahist` para na 1ª linha sem número (clube empatado); 36
  edições ficaram com menos clubes (ex.: 1928 1 de 10, 1936 1 de 11, 1942 1 de 10) — PY-003.
- Sem jogos, 1982-1995: a classificação é a tabela de uma fase (1986, 1987, 1988, 1990, 1991, 1992, 1993, 1995); 1989 com
  colunas trocadas (Olimpia J 33, V 50, E 74, Pts 2, ajuste -172) — PY-004, **no ar**.
- Com jogos, 1960-1967 (contra a "Final Table" da página do ano): 1967 bate; 1960 difere em 1 jogo do tribunal (PY-010);
  1961-1966 com posições trocadas por causa dos jogos de outros torneios (PY-005) e do playoff de rebaixamento (PY-006).
- 2008-2025 (amostra: 2017 Apertura, 2019 Clausura, 2020 Clausura, 2022 Apertura, 2024 Clausura, contra a tabela da
  Wikipédia es): iguais (2019 Clausura: 1 gol em Sol de América x General Díaz).
- Rebaixados: só 1967 (errado, ficou: PY-011) e 1994; os outros anos não marcam ninguém, e a aba Participantes mostra "—"
  (PY-012). Punições: 1988 são bônus de fase (certo); 1989 é lixo de leitura (PY-004).
- Fontes: https://www.rsssf.org/tablesp/parahist.html e páginas para60…para2025 · páginas de temporada da Wikipédia es.

## C. Jogos
- Total por edição: 1962-1966 têm 152 jogos de Torneo Preparación, Copa Asunción, Torneo de Honor e Copa República
  (PY-005); 2000, 2004 e 2005 têm playoffs de vaga (Libertadores, Pre-Sudamericana) e a final da Intermedia (PY-007);
  fases de final do Apertura/Clausura com o mesmo nome da final do ano (PY-008).
- Placares (amostra por década, Wikipédia es como fonte independente): 2020s 330/330 (2020 Clausura, 2022 Apertura,
  2024 Clausura); 2010s 743/747 (2010 A e C, 2011 A, 2014 C, 2017 A, 2019 C; 3 das 4 diferenças são erro da Wikipédia — a
  tabela dela bate com o pacote; a 4ª, 2010 Apertura Cerro x Trinidense, parece célula trocada na tabela de confrontos); 2000s 448/450 (2003, 2004, 2007); 1990s 63/65 (1997, 1998, 1999). 1960s e 1981: nenhuma
  fonte independente na internet (só a RSSSF, que é a base).
- ESPN x RSSSF: 5.149 de 5.166 placares iguais; das 6 diferenças reais, 3 a terceira fonte confirma a RSSSF (PY-030).
- Datas: 5.120 de 5.166 iguais à ESPN; playoffs herdam a data da última rodada (84 casos de clube com 2 jogos no mesmo dia,
  1961-2020) — PY-009. Jogos de tribunal: 1960 Tembetary x Libertad sem "awd" (PY-010).
- Fontes: https://es.wikipedia.org/wiki/Anexo:Resultados_del_Campeonato_Paraguayo_de_F%C3%BAtbol_2007 e páginas
  "Torneo Apertura/Clausura AAAA (Paraguay)".

## D. Gols e artilheiros
- Artilheiros: 95 edições com artilheiro; 82 batem com a Wikipédia es; diferença de gols em 1935, 1962, 1963, 1967, 1970,
  2003 (PY-019); faltam 14 edições de 2014 a 2025 (PY-018).
- Gols com autor nunca acima do placar, menos 1 jogo (2007 Trinidense 2-2 Nacional com 3 gols do Nacional, PY-020); 19
  gols e 3 cartões com jogador "2"/"22" (PY-021).

## E. Clubes e escudos
- 43 clubes; nomes únicos, menos "Olimpia" x "Olímpia" (BRA), que só diferem no acento (PY-017).
- Pettirossi de Encarnación (1994) juntado ao Silvio Pettirossi de Asunción (PY-013); "Cerro Porteño de Ciudad del Este"
  (1994) é o Cerro Porteño PF (PY-014); 8 de Diciembre é de Caaguazú, não Caacupé (PY-015); "Ovetense" (1966) é a seleção
  da Liga Ovetense, da Copa República (sai com PY-005); Fernando de la Mora de 2005 vem da final da Intermedia (PY-007).
- Escudos: folha de contato com os 27 que existem (todos certos); 16 sem escudo, entre eles Presidente Hayes, Sport
  Colombia, Colegiales, Cerro Corá e Atlántida; 12 de Octubre com imagem genérica (PY-016).

## F. Painel
- Varredura (`revisao/PY/varredura.py`): 4 "campeão não é 1º", 7 "Final com jogos demais" (1962: 112 jogos), 84 "2 jogos
  no mesmo dia", 9 "jogo repetido" — todos explicados pelos achados acima.
- Telas no site (amostra: História/Pódio, Corrida, Participações, Curiosidades; Por campeonato 1917, 1928, 1962, 1989,
  1991, 1999, 2020 Clausura, 2025 Clausura; Participantes 2024 Clausura e 2025 Apertura; celular): linhas parciais com jogos
  aparecem com 0 pts e "0 V·0 E·0 D" (87 linhas, PY-023); participações de Olimpia contadas a menos (PY-024); estádios com o
  nome do patrocinador de hoje em jogos antigos (PY-025); celular mais largo que a tela (PY-026, conhecido).
- Maior goleada (Recoleta 1-9 Sport Colombia, 2002) confere com a Wikipédia es.

## Perguntas ao Guilherme
1. Anos com dois vices na lista da RSSSF (1926, 1927, 1952, 1953, 1964): seguir a Wikipédia es (recomendado)? (PY-028)
2. Pettirossi de Encarnación (1994) e Silvio Pettirossi (Asunción) são clubes diferentes — separar? (PY-013, recomendado)
3. Cerro Porteño (Cd. Este, 1994) e Cerro Porteño PF são o mesmo — juntar? (PY-014, recomendado)
4. "Olimpia" (PAR) x "Olímpia" (BRA): renomear o brasileiro para "Olímpia-SP"? (PY-017)
5. Incluir o Apertura 2026 agora ou só com o ano fechado? (PY-027)

Detalhes das decisões: `SCRATCH/decisoes_PY.md`; plano de correção: `SCRATCH/plano_PY.md`; fontes: `SCRATCH/fontes_PY.md`.
