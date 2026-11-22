# Revisão: Campeonato Chileno, 1ª divisão (chi-1)

Revisor: CH · 22/11/2026 (3ª rodada, revisão profunda) · achados em `SCRATCH/achados_CH.csv` (CH-001 a CH-028) · scripts e saídas em `revisao/CH/` · fontes, decisões e plano em `SCRATCH/fontes_CH.md`, `decisoes_CH.md`, `plano_CH.md`

**Resumo.** Os 109 campeões batem com a Wikipédia es (lista oficial); 7 vices estão errados (1944, 1955, 1968, 1982, 1984, 1985, 2016/17 Apertura), cada um por uma causa diferente (jogo com clube trocado, tabela da 1ª fase, bônus ignorado, quadrangular ignorado, placar do ogol, liguilla dentro da edição).
No ar: a classificação de 1981 e 1983 mostra os pontos de bônus no lugar dos pontos (Colo Colo campeão com 2 e 0 pontos), e a Liguilla Pré-Sul-Americana aparece como "Semifinal"/"Final" dos torneios 2015/16.
Os jogos estão bons onde há fonte independente (4.713 casados com o transfermarkt, 3.704 com a es.wiki), mas as datas de 2020 estão um ano à frente, as dos mata-matas 2002-2016 repetem a do jogo anterior e os placares do ogol (base de 1984-1995) têm erros que o relatório da coleta atribuiu à RSSSF. Achados: 10 altos, 11 médios, 7 baixos.

Pacote, banco e site batem: `dados/chi-1.js` do site é idêntico ao local; campeão, vice, jogos, gols e classificação iguais nas 109 edições (`revisao/CH/tres_vias.py`). O painel mostra menos jogos em 14 edições só porque deixa fora os jogos sem placar (W.O. e abandonados).
A coleta usou RSSSF (base 1933-1983 e 1996-2024), ogol (base 1984-1995 e 2025; conferência nos outros anos), ESPN (fase de liga do Clausura 2011 e de 2012; lances de 2005 em diante) e a Wikipédia en (campeões). Para conferir usei a Wikipédia es (lista de campeões, ~95 páginas de temporada), o transfermarkt (1990-2001 e 2018-2025) e, onde servia de 3ª opinião, a soma das tabelas da RSSSF e a ESPN.

## A. Edições e títulos
- **Conferido:** as 109 edições, campeão e vice de todas, contra a seção Historial de https://es.wikipedia.org/wiki/Primera_División_de_Chile (saída `revisao/CH/saida_campeoes_es.txt`).
- **Lista de edições:** certa — 1933-1996 anuais, Apertura e Clausura (1997, 2002-2009, 2011, 2012, 2013/14-2016/17), Transición 2013 e 2017, 2020 = 2020/21. A es.wiki conta 110 torneios até 2026: bate.
- **Campeões:** 109 de 109. Títulos por clube iguais (Colo Colo 34 até 2025...). O de 1945 está com "Deportes Temuco"; a es.wiki dá "Green Cross" → CH-020 (decisão).
- **Vices:** 102 de 109. Erram:
  - 1944 Santiago Morning (certo: Audax) → CH-002;
  - 1955 Unión Española (certo: Colo Colo) → CH-003;
  - 1968 U. de Chile (certo: U. Católica, que ganhou o desempate do 2º lugar) → CH-004;
  - 1982 Magallanes (certo: Colo Colo, com o bônus da Polla Gol) → CH-005;
  - 1984 Cobreloa (certo: Cobresal, 2º do quadrangular final) → CH-006;
  - 1985 Colo Colo (certo: Everton) → CH-007;
  - 2016/17 Apertura Unión Española (certo: Deportes Iquique) → CH-008.
- **Desempates de título:** 1933, 1950, 1951, 1959, 1961, 1976, 1986 e 2009 Apertura estão como fase própria; os de 1997 Apertura e 2013/14 Apertura estão dentro da fase de liga → CH-009.
- **Punições citadas na tarefa:** 2008 Apertura Deportes Concepción -6, 2003/2004 Unión San Felipe -3, 2011 Apertura Colo Colo -1: estão nas tabelas da RSSSF mas somem da classificação calculada → CH-015. Colo-Colo 2002 (quiebra) não teve perda de pontos: certo.

## B. Classificação final
- **Conferido:** as 109 classificações contra a soma dos jogos (`classif_x_jogos.py`) e 70 contra as tabelas das páginas es de cada ano (`tabelas_es.py`; 1962-1982 e 2000+ parcialmente, por formato e por 429 da Wikipédia). Amostra por década: 1934, 1944, 1955, 1965, 1975, 1985, 1993, 2005.
- **Pontos errados no ar (1981 e 1983):** a coluna de bônus foi lida como pontos → CH-001. O mesmo erro está nas tabelas de conferência de 1979 e 1982.
- **Tabela errada escolhida:** 1954 e 1955 usam a tabela da 1ª fase (26 jogos) em vez da agregada → CH-003.
- **Classificação calculada:** em 53 edições a classificação é calculada (fase alcançada, pontos, saldo). Problemas: ignora bônus e punições (CH-005, CH-015), ignora a ordem do quadrangular de 1984 (CH-006) e desempata por saldo, não pela ordem oficial (1947, 3º lugar → CH-019).
- **Jogos de outra competição somados:** liguillas pré-Libertadores/Sul-Americana (CH-008) e desempates de rebaixamento de 1971 e 1977 (CH-016).
- **Rebaixados (campo situacao):** 20 marcas erradas (a regra pega "Relegation Group/Playoff"), entre elas Colo Colo "rebaixado" em 2020, e 117 saídas sem marca → CH-010. O painel não usa este campo (deduz pela temporada seguinte), então a sub-aba Participantes está certa; o erro é do banco.
- **Ok:** 1933, 1936, 1938-1942, 1945, 1949, 1950, 1952, 1956-1960, 1962, 1965-1967, 1974, 1975, 1978, 1987, 1992, 1996, 1998, 1999 batem com a es.wiki.

## C. Jogos
- **Conferido:**
  - 4.724 jogos do transfermarkt (1990-1996, 1998-2001, 2018-2025), 4.713 casados: 24 placares diferentes, dos quais 9 são erro do pacote confirmado por 3 fontes (CH-013); os demais são erro do transfermarkt, jogos abandonados ou W.O. (`saida_tm_jogos.txt`);
  - 4.029 jogos da es.wiki (1992-1995, 2005-2011, 2013/14), 3.704 casados: 9 placares diferentes — 3 erros do pacote (1993, 1995, 2011 Ap Ñublense x Wanderers), 4 da Wikipédia (a ESPN confirma o pacote) e 2 W.O. (`saida_jogos_es.txt`);
  - 5.729 jogos ligados à ESPN: datas (`saida_datas_espn.txt`);
  - todas as edições: pares de clubes com número de jogos fora do padrão (`saida_pares.txt`) e varredura de tela (`saida_varredura.txt`).
- **Amostra por década:** 1930-1980: não achei fonte de jogos independente que responda (a es.wiki só tem tabelas antes de ~1992; footballdatabase.eu sem cota hoje). Nessas décadas a conferência foi pela soma de TODOS os jogos contra a tabela da RSSSF e da es.wiki — e ela achou 4 jogos com clube trocado (1943, 1944, 1953, 1972 → CH-002). 1990s: 2.400+ jogos; 2000s: ~2.200; 2010s: ~1.000 (2010, 2011 Ap e Cl, 2013/14, 2018-2019) + ESPN; 2020s: 1.538.
- **Datas:**
  - 2020: todas um ano à frente, e 3 em "2021-02-29" → CH-011;
  - mata-matas 2002-2016: ida e volta com a data do jogo anterior → CH-012;
  - 1969 (7) duvidosas → CH-023; 2010: 26 datas diferem da ESPN, mas a es.wiki confirma as do pacote (não é erro);
  - cobertura de datas baixa nos anos 1930 (29%) e 1950 (16%): o calendário do ogol foi baixado incompleto → CH-028.
- **ogol como base (1984-1995):** placares errados (CH-013), jogo duplicado em 1988 e adversários trocados em 1986 (CH-014). O relatório da coleta diz "o ogol traz os mesmos placares: o erro é da tabela publicada", mas nesses anos o ogol é a própria base: a explicação é circular, e o transfermarkt dá razão à RSSSF.
- **W.O., anulados e abandonados:** 20 decididos no tribunal e 11 abandonados no pacote; olhei na página os de 2011, 2020, 2023 e 2024 e a lista do relatório. Erro em 2011 Apertura, Ñublense x Wanderers, em que a RSSSF diz "award revoked" → CH-015.
- **Fases e grupos:** 1968, 1969, 1970 e 2002-2008 → CH-022. Campo cidade com nome do estádio → CH-024. Deportes Concepción em 2008 Clausura sem jogos → CH-025.

## D. Gols e artilheiros
- **Conferido:** artilheiro das 101 edições do pacote contra a RSSSF chiletops e as páginas es (1963 em diante); soma dos gols com autor x placar em todos os jogos.
- **Faltam:** 1936, 1937 e 1947 (o leitor da chiletops não lê "Costa Rica Audax Italiano"), além de 2013/14 Cl, 2014/15 Ap e Cl, 2015/16 Ap e 2020. Divergem 1968 (RSSSF Reinoso 21 x es Zárate 32) e 1998 (23 x 25) → CH-018.
- **Gols com autor maiores que o placar:** 6 jogos de 2007-2011 (a ESPN repete o gol contra) → CH-017.

## E. Clubes e escudos
- **Conferido:** os 53 clubes (nome único no mundo contra o banco e os outros pacotes: nenhuma colisão; Everton de Viña del Mar, Rangers de Talca, Naval de Talcahuano e Metropolitano de Santiago com a cidade), identidade ao longo do tempo e os 53 escudos (folha de contato: `revisao/CH/folha_escudos.py`).
- **Identidade:**
  - Green Cross (Santiago) junto com Deportes Temuco → CH-020;
  - Deportes Arica e San Marcos de Arica são o mesmo clube segundo a es.wiki → CH-021.
  - Ok: Ferrobádminton separado; Santiago Morning separado de Santiago FC e Morning Star; Deportes Antofagasta (Antofagasta Portuario/Regional Antofagasta), Unión La Calera, Deportes Iquique (Municipal Iquique) e Regional Atacama x Deportes Copiapó.
- **Escudos:** 48 de 53 certos (Deportes Arica usa o de San Marcos, coerente com CH-021); 5 clubes dos anos 1930-50 sem escudo → CH-026.

## F. Painel
- **Telas abertas no site** (Chrome sem janela): Pódio, Corrida, Pontuação histórica, Classificação 1955, 1981, 1983 e 2016/17 Apertura, Jogos 2015/16 Clausura e 2020, Resumo 1997 Apertura. Sem erro de JavaScript.
- **Confirmado no ar:**
  - PTS 2/0/0/1 em 1981 e 0 em 1983 → CH-001;
  - "Final Santiago Wanderers x O'Higgins" no Clausura 2015/16 → CH-008;
  - Unión Española 2º com 16 jogos em 2016/17 Apertura → CH-008;
  - vices errados no Pódio (7 edições) → CH-002 a CH-008.
- **Celular:** página mais larga que a tela (já conhecido) → CH-027.
- **Varredura de tela:** 86 "clube com 2 jogos no mesmo dia" (quase todos datas dos mata-matas → CH-012); 1 jogo repetido (1988 → CH-014); "semifinalista fora do top 4" em 2015/16 (é a liguilla → CH-008; os outros casos são playoffs de 8 clubes, certos).

## Perguntas ao Guilherme
1. **CH-020:** o título de 1945 e os anos 1933-1964 ficam com "Green Cross" (clube de Santiago, separado) ou com "Deportes Temuco" (como hoje, seguindo a RSSSF)? Recomendo separar, como a lista oficial e a regra das fusões (Ferrobádminton).
2. **CH-021:** Deportes Arica (1982-1985) e San Marcos de Arica (2013-2015) viram um clube só? A es.wiki conta como o mesmo clube, refundado em 2005. Recomendo juntar.
3. **CH-018:** artilheiro de 1968: Carlos Reinoso 21 (RSSSF) ou Eladio Zárate 32 (es.wiki)? E 1998: 23 ou 25 gols? Recomendo buscar uma 3ª fonte; sem ela, usar o campeonato inteiro (es.wiki).

Data: 22/11/2026.
