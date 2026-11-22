# Decisões do Guilherme — Campeonato Alemão (`ger-1`), revisão de 22/11/2026

### DE-D1 Incluir o Campeonato Alemão de antes da Bundesliga (1902/03–1962/63) e a DDR-Oberliga?

**Hoje:** o `ger-1` é só a Bundesliga (63 edições, 1963/64–2025/26), mas o painel chama a competição de "Campeonato
Alemão". Por isso a contagem de títulos do painel não é a oficial da DFB. Exemplos, contando a Bundesliga até 2025/26 e
os campeonatos de antes:
- Bayern: 34 no painel, 35 títulos alemães (falta 1931/32);
- Nuremberg: 1 no painel, 9;
- Schalke 04: 0 no painel, 7;
- Hamburgo: 3 no painel, 6;
- Borussia Dortmund: 5 no painel, 8;
- Colônia: 2 no painel, 3;
- Kaiserslautern: 2 no painel, 4;
- Stuttgart: 3 no painel, 5;
- Eintracht Frankfurt: 0 no painel, 1;
- Hannover 96: 0 no painel, 2;
- Rot-Weiss Essen: 0 no painel, 1;
- Fortuna Düsseldorf: 0 no painel, 1;
- 1860 Munique: 1 no painel, 1.

Também faltam no painel os campeões de antes da Bundesliga que nunca a ganharam: VfB Leipzig (3), Greuther Fürth (3), Hertha (2),
Dresdner SC (2) e outros.

**Opções:**
- **A. Manter só a Bundesliga.**
  - Mudar o nome no painel para "Bundesliga" ou "Campeonato Alemão (Bundesliga, desde 1963/64)".
  - Pôr um aviso de que os títulos são só os da Bundesliga.
  - Custo: quase nada (um texto no `competicao.json` e no painel).
- **B. Incluir a fase final (Endrunde) de 1902/03 a 1962/63 como edições do mesmo `ger-1`.**
  - São cerca de 55 edições, com mata-mata, grupos e final, e cerca de 1.000 jogos.
  - Edições sem campeão:
    - 1903/04: não disputada;
    - 1921/22: título não atribuído;
    - 1914/15 a 1918/19 e 1944/45 a 1946/47: sem campeonato.
  - Assim a contagem de títulos fica igual à oficial da DFB.
  - Custo: médio. Fontes: as páginas de temporada da Wikipédia de, as páginas da RSSSF e a lista de campeões da DFB.
  - O painel já mostra edições com fases (como `esp-1` 1986/87, `ita-1` 1945/46 e `fra-1` 1932/33).
- **C. Incluir também as Oberligas regionais de 1945/46 a 1962/63** (Nord, West, Süd, Südwest, Berlin) e as ligas
  regionais de antes da guerra.
  - São cerca de 20.000 jogos só no período de 1945 a 1963.
  - Elas eram o 1º nível, mas regional, e no painel se parecem mais com estaduais.
  - Custo: alto. Fontes: as páginas de Oberliga da RSSSF e o footballdatabase.eu (Oberliga 1945/46–1962/63).
- **D. DDR-Oberliga (1949/50–1990/91) como competição à parte** (`gdr-1`, país Alemanha Oriental).
  - São 42 temporadas e cerca de 7.500 jogos.
  - A DFB não conta esses títulos como títulos alemães.
  - Os clubes são os mesmos do `ger-1` (Dynamo Dresden, Hansa Rostock, Union Berlin, Energie Cottbus, VfB Leipzig = Lok
    Leipzig): é preciso ligar os cadastros.
  - Custo: médio. A RSSSF tem uma página por temporada, com rodada, data e placar (ex.: `ddr72.html`).

**Prova:**
- https://www.rsssf.org/tablesd/duitchamp.html: finais de 1902/03 a 1962/63, "not played" em 1903/04, "not awarded" em
  1921/22, e índice das páginas "Germany - Championships 1902-1945 / 1947-1963" e das Oberligas;
- https://de.wikipedia.org/wiki/Liste_der_deutschen_Fußballmeister;
- https://de.wikipedia.org/wiki/Deutsche_Fußballmeisterschaft_1955/56: Endrunde com 8 clubes (12 com as eliminatórias),
  25 jogos, grupos e final;
- https://www.rsssf.org/tablesd/ddr72.html: DDR-Oberliga 1971/72, jogo a jogo, com data de cada rodada;
- footballdatabase.eu: o seletor de temporadas da página da Bundesliga lista "Oberliga" de 1945/46 a 1962/63, com
  jogos.

**Recomendação: B agora, D depois (à parte) e C só se o Guilherme quiser ir até as regionais.**
- B faz o "Campeonato Alemão" do painel contar os títulos que a DFB reconhece. É o "mais fiel à história" do critério dele.
- B custa pouco, porque a fase final tem cerca de 20 jogos por ano.
- D é outro país esportivo (DFV): competição separada, como a DFB trata.

Se ficar com A, ao menos o nome e o aviso precisam mudar, para o painel não dizer que o Nuremberg tem 1 título alemão.

### DE-D2 Relegation (play-off entre o 16º da Bundesliga e o 3º da 2. Bundesliga): incluir os jogos?

**Hoje:**
- Os jogos ficam fora (`competicao.json`).
- O 16º é marcado "rebaixado" só quando perdeu: 1982/83 Schalke, 1984/85 Arminia, 1990/91 St. Pauli, 2008/09 Cottbus,
  2011/12 Hertha, 2018/19 Stuttgart e 2025/26 Wolfsburg. Isso está certo nas 63 temporadas (conferido com a Wikipédia de).
- O painel não diz em lugar nenhum que houve Relegation, nem o resultado. Temporadas com Relegation: 1981/82–1990/91 e
  2008/09–2025/26, 28 no total.

**Opções:**
- A. Deixar como está.
- B. Só uma nota na edição, por exemplo: "Relegation: Wolfsburg (16º) 0-0 e 1-2 Paderborn; caiu".
- C. Incluir os 2 jogos como fase "Relegation", fora da classificação. É o mesmo caso da liguilla do Espanhol 1986/87
  (ES-002): a Wikipédia es diz que aqueles jogos não contam como jogos da Primera, e a decisão foi deixá-los só na
  `observacao`.

**Prova:** https://de.wikipedia.org/wiki/Fußball-Bundesliga_2025/26, seção "Relegation" (e a mesma seção em cada temporada
dessas épocas).

**Recomendação: B.**
- Segue a decisão do ES-002 (os jogos ficam só na `observacao`).
- Não mexe nas somas da edição.
- Os jogos entram com a 2. Bundesliga (`ger-2`), se ela vier.

### DE-D3 1979/80: 3º lugar dividido entre Stuttgart e Kaiserslautern?

**Hoje:** Stuttgart em 3º e Kaiserslautern em 4º, pela ordem da RSSSF. Os dois têm 41 pontos e 75-53 de gols. O pódio
do painel conta o 3º lugar só para o Stuttgart.

**A Wikipédia de** põe os dois em "3." (Rang2=3, posição dividida): https://de.wikipedia.org/wiki/Fußball-Bundesliga_1979/80.
O regulamento da época não tinha mais nenhum critério depois de pontos, saldo e gols marcados.

**Opções:**
- A. Manter Stuttgart 3º e Kaiserslautern 4º, com uma nota na edição.
- B. Os dois em 3º (o painel não aceita posição repetida hoje; o agente 1 teria de mexer).

**Recomendação: A.** É uma nota só, sem mexer no painel.
