# Revisão: Campeonato Uruguaio, 1ª divisão (uru-1)

Revisor: UY · 21/11/2026 (2ª rodada) · achados em `SCRATCH/achados_UY.csv` (UY-001 a UY-028) · scripts e saídas em `revisao/UY/`

**Resumo.** Os campeões batem com a lista da AUF em 122 de 122 edições, mas o painel mostra o Nacional campeão de 1948 (inconcluso) e conta 1923 FUF, 1924 FUF e 1926 como títulos, que a AUF não reconhece (Peñarol 54 e Nacional 51 no painel; AUF: 52 e 50).
De 1994 a 2025, a classificação final de 28 edições é só a tabela do Apertura (1ª fase), por isso o vice está errado em 14 edições e o 3º em 19. Exemplo: em 2025 o Peñarol, finalista, aparece em 4º.
Os jogos estão bons: 4.136 de 4.167 placares batem com a Wikipédia es. Mas 8 jogos da Supercopa entraram como "Final", as datas das decisões estão erradas e em 2020 o Apertura está com o ano errado. Achados: 4 altos, 11 médios, 11 baixos e 2 que não são erro.

Site e arquivo local são iguais: `dados/uru-1.js` e `index.html` têm o mesmo md5 que `painel/`. Os números do painel batem com o banco (12.464 jogos no banco e no pacote; o painel mostra 12.367, sem os 97 jogos sem placar).
A coleta usou como base a RSSSF (1932-1959, 1965 e 1994 em diante, mais as tabelas `uruhist`) e a Wikipédia es (jogos de 1900-1916 e 1960-1974). Na conferência usei a Wikipédia es e en, e a RSSSF só onde a base era a es.

## A. Edições e títulos
- **Conferido:** lista de edições; campeão, vice e 3º de todas as edições. Fontes: [es, Títulos de liga por año](https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Uruguay#T%C3%ADtulos_de_liga_por_a%C3%B1o) (lista da AUF) e [en, List of champions](https://en.wikipedia.org/wiki/Uruguayan_Primera_Divisi%C3%B3n). Saída: `revisao/UY/saida_podio.txt`.
- **Lista de edições:** são 126, uma por título. 1904 e 1930 não tiveram campeonato e 1925 não terminou, por isso ficam fora (certo). 1948 entra sem campeão, também certo.
  - 1923 FUF, 1924 FUF e 1926 (Consejo Provisorio) **não estão na lista da AUF**, que tem 122 campeonatos → UY-001 (pergunta).
- **Campeões:** 122 de 122 iguais nas edições da AUF.
  - O painel mostra o Nacional campeão de 1948, e o banco não tem campeão. Isso aparece no pódio, na Corrida dos títulos (Nacional 51) e na lista de "campeões invictos" → UY-002.
  - O pacote dá o Peñarol como vice de 1948 → UY-003.
- **Vices:** 108 de 122 batem com a en, e a es concorda nos casos errados.
  - Erram 1995, 1996, 1998, 2000, 2001, 2002, 2004, 2007/08, 2008/09, 2011/12, 2013/14, 2014/15, 2021 e 2025 → UY-004.
  - A causa é a mesma do bloco B: o vice é o 2º da tabela do Apertura, não o perdedor da final.
  - Em 2011/12 e 2021 não houve final (o campeão ganhou a semifinal e a tabela anual). Ali as fontes usam o 2º da tabela anual.
- **Vices em dúvida:** 1954 (RSSSF: Nacional; es: Danubio) → UY-007. 1947 (es: "no se definió") → UY-008.
- **3º lugar:** 102 de 122 iguais à en. Erram 1911, 1994-1998, 2001, 2002, 2004, 2007/08, 2008/09, 2010/11, 2011/12, 2014/15, 2019-2021, 2024 e 2025 → UY-005.
- **Nomes de época:** o nome oficial de cada edição está certo (Uruguay Association Foot-ball League, Liga Uruguaya, AUF, FUF, Torneo Uruguay Especial 2005, Transición 2016).
  - O pódio mostra só o ano de início: 2009/10 aparece como "2009", e o Nacional aparece com "2005" duas vezes → UY-009. A pendência já é conhecida.

## B. Classificação final
- **Conferido:** 117 edições, contra as tabelas das páginas es de cada ano. Foram 64 iguais, 16 com os mesmos números em outra ordem (desempates e campeão puxado para o topo) e 37 diferentes. Script e saída: `revisao/UY/tabelas_es.py` e `saida_tabelas_es.txt`.
- **Uma ou mais por década:** 1906, 1913, 1923 AUF, 1935, 1945, 1955, 1966, 1977, 1985, 1993, 2005, 2014/15, 2023 e 2025.
  - **Iguais:** as edições sem jogos (1902-1931, 1975-1993) batem com a es em 17 de 19 de 1975 a 1993 e na maioria de 1902 a 1931.
  - **Diferenças pequenas** entre a RSSSF e a es, sem mudar o campeão: 1913, 1917, 1919, 1920, 1955 e 1991 → UY-012.
- **Erro principal → UY-006.** Em 1994-1996, 1998-2004, 2006/07-2015/16, 2017 e 2019-2025 (28 edições), a classificação final é a 1ª tabela da página da RSSSF: o Apertura (o Clasificatorio em 2001, 2002 e 2004).
  - São 11 a 17 jogos por clube, quando eles jogaram 22 a 42, e o campeão é puxado para o 1º lugar.
  - Exemplos: em 2025 o Peñarol fica em 4º (na tabela anual é 2º, com 78 pontos); em 2023 o Racing fica em 14º (na tabela anual é 6º).
  - Isso também erra a lanterna, a Trajetória dos clubes e o 3º lugar.
- **Outros:**
  - 1908: o W.O. de Intrépido x Bristol foi dado ao Intrépido, que não compareceu. O Bristol cai de 5º para 8º → UY-010.
  - 1951: a classificação foi calculada dos jogos e diverge das tabelas da RSSSF e da es, que concordam entre si. O Danubio aparece em 4º, e nas tabelas é 6º → UY-011.
- **Pontos por vitória e punições:** 2 pontos até 1994 e 3 desde 1995, certo. As punições de 1994, 1995, 1996, 2006/07, 2008/09, 2009/10 e 2025 (Cerro) estão aplicadas → UY-028 (não é erro).
  - As punições que valem só na tabela anual ficam de fora por causa do UY-006: 2025 Nacional -3 e 2014/15 Peñarol -1.
- **Participantes:** o painel não diz "subiu" nem "caiu", porque não há 2ª divisão no banco. Mostra "já estava", "—" e "ficou". Conferi 2013/14: os três que não voltaram (Liverpool, Cerro Largo e Miramar Misiones) foram de fato rebaixados.

## C. Jogos
- **Total:** 12.464 jogos no banco e no pacote. O painel mostra 12.367, sem os W.O., os jogos dados no tribunal sem placar e os anulados.
  - Esse total tem 8 jogos da **Supercopa AUF** gravados como "Final" de 2018 a 2025 → UY-013.
  - Em 2018, 2021 e 2024 não houve final, e o painel mostra uma. Em 2024, a "Final" tem o Nacional vencendo e o Peñarol campeão.
- **Placares:** 4.167 jogos comparados com o fixture das páginas es, e 4.136 iguais (99,3%). Script e saída: `revisao/UY/jogos_es.py` e `saida_jogos_es.txt`.
  - **Antigas:** 1932-1959, todas as edições (135, 110 ou 90 jogos cada).
  - **Do meio:** 1994 (156 jogos) e 1997 (132).
  - **Recentes:** 2011/12 a 2015/16 (239-240 jogos cada).
  - **As 31 diferenças** batem com o ogol quando ele existe, então o provável erro é da es → UY-016.
- **Datas:**
  - Os jogos de decisão (semifinal, final, desempates) herdam a data do jogo anterior em 24 edições de 1994 a 2025. Exemplo: a final de 2025 está gravada em 16/11 e foi jogada em 23/11 e 30/11 → UY-014.
  - Em 2020, o Apertura e o Intermedio estão gravados em 2021, quando foram jogados em 2020 → UY-015.
  - Contra a ESPN, 5.206 jogos foram comparados e 74 têm a data diferente (`saida_datas_espn.txt`).
- **W.O. e tribunal:** são 29 W.O., 58 decisões de tribunal, 23 abandonos e 4 anulados.
  - Seguem as notas da RSSSF e da es que a coleta registrou. Conferi as de 1908, 1939 e 1997, e só 1908 está errada (UY-010).
  - 1939 Nacional x Racing (`awd`, vitória dada ao Racing) está certo.
- **Varredura de tela** (`revisao/UY/varredura.py`, `datas_repetidas.py`; saídas `saida_varredura.txt` e `saida_datas_repetidas.txt`):
  - Jogos repetidos e "Final com jogos demais" (2020 e 2023): são a Supercopa e as datas herdadas.
  - 72 casos de "clube com 2 jogos no mesmo dia" (UY-014 e UY-015).
  - "Pódio x final" em 2025 (UY-004 e UY-006).
  - 1961 (desempate do rebaixamento como última fase) não é erro.
  - Nenhum clube contra ele mesmo, nenhuma fase em inglês, nenhum campeão fora do 1º lugar e nenhuma posição repetida.

## D. Gols e artilheiros
- **Gols com autor:** nenhum jogo tem mais gols com autor que o placar (0 de 12.367). Não há gol de clube que não jogou a partida.
- **Artilheiro:** 123 edições comparadas com a coluna "Goleador" da es. 67 batem e 56 diferem (`revisao/UY/saida_artilheiros.txt`):
  - de 2013/14 a 2025 (12 edições) não há artilharia oficial e o painel conta os gols com autor, que cobrem 53% a 82% dos gols. O artilheiro sai errado em 2014/15, 2017, 2019, 2022 e 2023, e o número sai menor nas outras → UY-017;
  - de 1900 a 1931 a aba fica vazia, mas a es tem o artilheiro de todas as edições → UY-018;
  - 15 edições têm número ou grafia diferente entre a RSSSF e a es (ex.: 1952 Jorge Enrico 15 x Héctor Rial 14) → UY-019.

## E. Clubes e escudos (81 clubes)
- **Cadastros duplicados:** nenhum. Miramar e Miramar Misiones ficam separados, e River Plate FC e River Plate de Montevideo também, como decidido.
- **País e cidade:** todos URU, cidades certas na amostra (Deportivo Colonia em Juan Lacaze, Plaza Colonia em Colonia del Sacramento, Paysandú, Rocha, Melo...).
- **CURCC = Peñarol:** aplicado de forma coerente, com títulos, vices e participações de 1900 a 1913 e sem cadastro separado → UY-024 (não é erro).
  - Nota: a continuidade é contestada. A es dá o Peñarol com 52 ou 47 títulos.
- **Clubes juntados:** o "Atlético Wanderers" da FUF virou o Montevideo Wanderers, que assim joga AUF e FUF em 1923 e 1924. O mesmo acontece com Lito e Charley → UY-020 (pergunta).
- **Nome de fonte com lixo:** "Peñarol (59' Juan Martín Parodi; ...)" → UY-023.
- **Escudos:** montei a folha dos 34 clubes com escudo e olhei todos (`SCRATCH/UY/folha_escudos.png`).
  - Errados: Deportivo Colonia (mostra o de um "D. Italiano") e Independencia (um "FC" de outro clube) → UY-021.
  - 47 clubes estão sem escudo, inclusive o River Plate de Montevideo, que jogou de 2005 a 2025 → UY-022.

## F. Painel (site publicado)
- **Telas:** 77 prints em `SCRATCH/UY/telas/`.
  - **História:** as 7 sub-abas.
  - **Por campeonato:** as 5 sub-abas em 9 edições: 2025, 1948, 1923 FUF, 1977 (sem jogos), 1994, 1908, 2005, 2024 e 2013/14.
  - **Por clube:** as 5 sub-abas em 4 clubes: Peñarol, Nacional, Montevideo Wanderers e River Plate FC.
  - **Celular:** 5 telas.
  - Nenhum erro de JavaScript (`--enable-logging` e `--dump-dom` em 4 rotas).
- **Cartões:** 126 edições, 11 campeões, 81 participantes, 12.367 jogos e 35.134 gols batem com o banco. Os 17 vices e 24 terceiros dependem do UY-004 e do UY-005.
- **Edições sem jogos:**
  - **Nas edições:** os cartões mostram 0 jogos, "—" na média e "sem jogos nesta edição" na maior goleada. A classificação aparece (com Pts) e a artilharia oficial também (1977: Morena 19). Isso está certo.
  - **Nos históricos:** Jogos e vitórias, Gols, Pontuação histórica, Confrontos e "12.367 jogos em 126 edições" deixam as 45 edições sem jogos de fora, sem aviso. O Nacional aparece com 1.941 jogos, e a tabla histórica da es (até 2023) dá 2.722 → UY-025.
  - **Nos recordes:** as edições sem jogos ficam fora de "menos jogos", como o agente 1 disse.
  - **Nas curiosidades:** "edição com mais clubes" (32) e "mais estreantes" vêm da 1923 FUF (UY-001 e UY-020).
- **Recordes conferidos:** a maior goleada, Wanderers 13 x 0 French (1908), bate com a es. O 0 x 9 fora de casa (Montevideo FC x Peñarol, 1900) e o clássico (202 jogos, que incluem 3 Supercopas) também foram conferidos.
- **Pts:** a coluna de pontos some nas edições de várias fases. É decisão do painel (20/11), não erro.
- **Celular:** a página fica mais larga que a tela (já conhecido) → UY-026.
- **Corrida dos títulos:** o eixo pula de 1920 para 1940 → UY-027.

## Perguntas ao Guilherme
1. **1923 FUF, 1924 FUF e 1926 (Consejo Provisorio) contam como título?** A AUF não os reconhece (122 campeonatos: Peñarol 52, Nacional 50, Wanderers 3); a RSSSF conta. Hoje o painel dá Peñarol 54 e Wanderers 4 (UY-001).
2. **O "Atlético Wanderers" da FUF (campeão de 1923 FUF) é o Montevideo Wanderers?** A es diz que era um time alternativo do Wanderers, que seguia jogando a AUF; o mesmo vale para Lito e Charley em 1923 e 1924 (UY-020).
3. **Vice de 1954:** Nacional (RSSSF, en) ou Danubio (es)? (UY-007).
4. **Vice quando não há final** (2011/12, 2021): o 2º da tabela anual, como a es e a en, ou o perdedor da semifinal? (UY-004).
