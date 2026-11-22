# Revisão — Campeonato Equatoriano (`ecu-1`)

Revisão profunda (3ª rodada), 22/11/2026. Achados `EC-001` a `EC-024` em `SCRATCH/achados_EC.csv`; scripts e saídas em `revisao/EC/`.

**Resumo:**
- Campeões e vices certos nas 68 edições; pacote = banco = painel local (14.195 jogos, 831 linhas de classificação). O `ecu-1` **ainda não está no site** (o `dados/ecu-1.js` publicado devolve a página inicial).
- Graves: a classificação final de ~30 edições não é a oficial (3º/4º errados em 23/28 edições; em 22 a tabela tem só uma fase), faltam 90 rebaixamentos em 34 edições e 2025 marca 3 rebaixados errados (e não marca o El Nacional).
- Médios: ~50 datas de final/mata-mata erradas, 20 jogos repetidos, 4 fases com tipo/nome errado, 1 placar (2005), 4 jogos de tribunal (1965), 1 gol a mais (2007).

## A. Edições e títulos
- **Conferido:** as 68 edições (1957, 1960-2025, 2005 em dois torneios) e campeão/vice de todas contra a Wikipédia es (Historial), fonte que a coleta não usou.
- **Resultado:** 68/68 campeões e 68/68 vices certos. 1957 como 1ª edição confere (EC-021, não é erro): não achei decisão do Guilherme registrada sobre 1957; a Wikipédia es confirma o torneio nacional de 1957 entre AFNA (Quito) e Guayas.
- **3º lugar** (pódio da História e do Resumo): errado em 23 edições — ver bloco B.
- **Fontes:** https://es.wikipedia.org/wiki/Serie_A_de_Ecuador#Historial

## B. Classificação final, rebaixados e punições
- **Conferido:** 1º-4º das 68 edições (272 posições) contra a Wikipédia es e a tabela da fase final da própria RSSSF (`tabelas_publicadas.csv`); jogos por clube na classificação x jogos da edição (todas); rebaixados de todas as edições contra a Wikipédia es ("Ascensos y descensos") e as notas da RSSSF; punições de 2015-2025 contra as páginas de temporada.
- **Resultado:** 221/272 posições certas.
  - **EC-001 (alta):** em 22 edições (1970, 1975, 1983, 1985, 1987, 1988, 1994, 1995, 1997-2004, 2005 Clausura, 2007-2009, 2019, 2025) a "classificação final" é a tabela de uma fase só (2025: 30 de 40 jogos; 2000: 18 de 46). Ex.: 2000 põe a LDU de Quito (rebaixada) em 4º; 2019 põe o semifinalista Aucas em 7º.
  - **EC-002 (alta):** nas 25 edições "calculadas", a ordem dentro da fase final ignora a tabela dela (com bônus): 1966, 1977, 1979, 1984, 1986, 1989, 1990, 1992, 2006.
  - **EC-003 (alta):** disputas de 3º/4º lugar viraram "Desempate do 2º lugar" (2009-2012): 3º de 2010 e de 2011 e 4º de 2012 são os perdedores.
  - **EC-004 (alta):** rebaixados marcados só onde a tabela escolhida diz "Relegated": faltam 90 em 34 edições (1967-2009; ex.: LDU de Quito em 1972, 1978 e 2000; Emelec em 1980). 2007, 2008 e 2010-2024 certos.
  - **EC-005 (alta):** 2025 marca Manta FC, Mushuc Runa e Técnico Universitario como rebaixados (não caíram) e não marca o El Nacional (descenso administrativo, -9 pontos que também faltam).
  - Punições de 2015, 2017, 2019 e 2024 conferem com a Wikipédia es; a observação só diz "punição/bônus de pontos" (sem motivo).
- **Fontes:** https://es.wikipedia.org/wiki/Serie_A_de_Ecuador#Ascensos_y_descensos_a_la_Serie_A ; https://es.wikipedia.org/wiki/Serie_A_de_Ecuador_2025 ; https://www.rsssf.org/tablese/ecua00.html
- Saídas: `revisao/EC/cmp_top4_saida.txt`, `class_x_jogos_saida.txt`, `descensos_es_saida.txt`.

## C. Jogos
- **Conferido:** total por edição (pacote = banco); varredura de tela (`revisao/EC/varredura.py`, `datas_repetidas.py`); placares e datas contra a Wikipédia es nos anos em que ela tem resultados — 3.058 jogos casados (1950s 7, 1960s 33, 1970s 13, 1980s 237, 1990s 20, 2000s 449, 2010s 1.076, 2020s 1.223; não há outra fonte independente para 1961-1981 e 1983-2007); datas dos blocos de mata-mata contra o título do bloco na própria página (42 jogos); pacote x ESPN (5.145 jogos).
- **Resultado:** placar igual em 3.030 de 3.058; as 28 diferenças são, quase todas, da Wikipédia es contra as tabelas da RSSSF (o pacote fecha com elas). Achados:
  - **EC-009 (média):** ~50 jogos de final, semifinal, quartas e 3º lugar com a data e a rodada do último jogo anterior (1998, 1999, 2005 Apertura, 2009, 2010, 2012, 2014, 2015, 2017-2024); os 2ºs jogos ficam sem ESPN.
  - **EC-008 (média):** 20 jogos repetidos (1984: 6; 1986: 12; 1994: 2), rebaixamento contado também na fase final.
  - **EC-006 (média):** 1999 "Final" com os 30 jogos da liguilla do rebaixamento.
  - **EC-007 (média):** 1963, 1966 e 1997 com a liguilla final como "Final" mata-mata ida e volta.
  - **EC-010 (média):** 1997, rebaixamento datado de dez/1998 e como mata-mata.
  - **EC-011 (média):** 2005 Apertura, Emelec 0-2 LDU de Quito é 2-2 (autores na própria página; a tabela fecha).
  - **EC-012 (média):** 1965, 4 jogos que o Aucas perdeu por jogador irregular estão com o placar de campo.
  - **EC-015 (média):** 2025 El Nacional x Delfín: n/p (RSSSF) x W.O. 0-3 (ESPN e Wikipédia es).
  - **EC-016, EC-017 (baixa):** ordem das fases; 2 datas trocadas (1988, 2006).
  - EC-023: os 13 placares ESPN x RSSSF ficam com a RSSSF, certo.
- **Cobertura (seção 4 da ficha):** datas faltam em 1960-1979 (5% e 0%); a Wikipédia es só tem as de 1960 (27 jogos). Autores dos gols antes de 2003: nenhuma fonte em lote. Lances da ESPN 2014-2020: transfermarkt e soccerway não servem (ver `SCRATCH/fontes_EC.md`).
- **Correções da coleta (seção 7):** 6 conferidas e certas — ecua73:114 (Wikipédia es: a LDU não jogou 1973), ecua05:563, ecua06:227, ecua06:556, ecua07:222 (ESPN) e ecua85 (Filanbanco, conta de V/E/D). A explicação de 1965 e de 2005 Apertura ("a página não diz qual") está errada: a página diz (EC-011, EC-012).

## D. Gols e artilheiros
- **Conferido:** os 68 artilheiros contra a Wikipédia es; soma dos gols com autor por jogo x placar (todos).
- **Resultado:** 65/68 certos; **EC-014 (média):** 1988 (Janio Pinto 18 x 19), 1996 (Graziani 29 x 30), 1999 (Bottero 25 x 24). **EC-013 (média):** 2007 LDU 4-0 Cuenca com 5 autores (gol do "Luis Escalada" para o Cuenca). Nenhum outro jogo com mais autores que gols.
- **Fontes:** https://es.wikipedia.org/wiki/Serie_A_de_Ecuador#Goleadores_por_temporada

## E. Clubes e escudos
- **Conferido:** os 63 clubes (nome único no banco e nos pacotes, cidade, província); estreia e nº de temporadas dos 18 clubes da Serie A atual contra a Wikipédia es; Deportivo Quito x Sociedad Deportiva Quito (mesmo clube), Liga de Quito x Portoviejo x Loja x Cuenca (quatro clubes), Emelec, Barcelona de Guayaquil; os 27 escudos que existem (folha `SCRATCH/EC/folha_escudos.png`).
- **Resultado:** identidades certas (as contagens batem, com +1 na Wikipédia por 2026); escudos existentes certos. **EC-018 (baixa):** 36 clubes sem escudo (Everest, Espoli, Filanbanco, Valdez SC, Patria...).

## F. Painel (local, porque o ecu-1 não está no site)
- **Conferido:** pódio, jogos, gols e ordem da tabela das 68 edições no `painel/dados/ecu-1.js` x banco (0 diferenças); prints no Chrome sem janela (História, 9 edições x 5 sub-abas, 2 clubes x 5 sub-abas, celular): `SCRATCH/EC/telas/`.
- **Resultado:** sem erro de tela. A maior goleada (América de Ambato 0-11 LDU, 1969) confere (EC-024: falta a data, 26/10/1969). Aparecem no painel os erros dos blocos B e C (pódio, "Final · mata-mata · 8 clubes · 56 jogos" em 1966, Final de 1999 com o rebaixamento, "17 terceiros"). **EC-019 (baixa):** participações contam 2005 duas vezes. **EC-020 (baixa):** celular mais largo que a tela (já conhecido).

## Perguntas ao Guilherme
1. **D-EC-1:** classificação final dos campeonatos com fases: soma da temporada na ordem oficial (campeão, vice, tabela da fase final, eliminados)? (recomendado)
2. **D-EC-2:** El Nacional x Delfín 2025: W.O. 0-3 (ESPN e Wikipédia es) ou não disputado (RSSSF)? (recomendado: W.O.)
3. **D-EC-3:** rebaixamento no meio do ano (1970-1981) marcado na edição do ano? (recomendado: sim)

Detalhes em `SCRATCH/decisoes_EC.md`; plano em `SCRATCH/plano_EC.md`; fontes em `SCRATCH/fontes_EC.md`.
