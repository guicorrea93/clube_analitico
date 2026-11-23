# Campeonato Francês (`fra-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/fra-1/pacote/` e do importador `coleta/fra-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/fra-1.md`.

## 1. O que temos

- **Edições:** 88, de 1932/33 a 2025/26.
- **Jogos:** 30466; **gols:** 84818; **gols com autor:** 22613 (27%); **cartões:** 35434; **jogos com estatísticas** (chutes, faltas, escanteios): 7655.
- **Clubes:** 77; **artilheiros:** 88 temporadas com artilheiro (99 linhas, com empates).
- **Classificação final:** 88 temporadas; **rodada a rodada:** 82 temporadas.
- **Tabelas publicadas guardadas para conferência:** 3314 linhas, de 173 tabelas.
- **Observação da competição:** 1ª divisão francesa desde a criação do campeonato profissional (1932/33): Division 1 até 2001/02 e Ligue 1 depois. Sem 1939/40-1944/45 (campeonatos de guerra, não reconhecidos). 1932/33 teve dois grupos e final. Não inclui os barrages (jogos de acesso e rebaixamento contra clubes da 2ª divisão).

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1932/33-2024/25, menos 1937/38, 1994/95 e 2025/26 (que vêm do ogol) e 1932/33 (errada);
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+) e estatísticas por time (os arquivos da França não trazem árbitro);
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-fra-1/` para os escudos;
- ESPN (liga `fra.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: matriz de resultados e tabela final de 1932/33 a 1997/98 (conferência jogo a jogo), tabela final das temporadas seguintes e lista de artilheiros (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista de campeões (com os gols do artilheiro).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Paris). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94 (menos 1988/89, que teve 3), 3 a partir de 1994/95 (de 1973/74 a 1975/76, 1 ponto a mais para quem marcava 3 gols ou mais no jogo). Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 0, saldo de gols em 64, média de gols em 24); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 153 tabelas fecham com os jogos e 21 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1945/46, 1955/56, 1958/59, 1992/93.
- Temporadas com alguma tabela divergente: 1937/38, 1945/46, 1946/47, 1951/52, 1952/53, 1953/54, 1955/56, 1958/59, 1963/64, 1965/66, 1971/72, 1975/76, 1979/80, 1984/85, 1986/87, 1992/93, 2008/09.
- Temporadas com número de jogos diferente do turno e returno completo: 2019/20 (279 de 380).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1930s | 1563 | 77% | 0% | 86% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1604 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 3208 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 3504 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 3800 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3800 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3578 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3652 | 100% | 92% | 100% | 90% | 70% | 0% | 52% | 90% | 3.5 |
| 2010s | 3699 | 100% | 100% | 100% | 100% | 96% | 0% | 100% | 100% | 3.8 |
| 2020s | 2058 | 100% | 100% | 100% | 82% | 84% | 0% | 100% | 100% | 4.1 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1932/33: 20 clubes
- 1933/34: 14 clubes
- 1934/35 a 1938/39: 16 clubes
- 1945/46: 18 clubes
- 1946/47: 20 clubes
- 1947/48 a 1957/58: 18 clubes
- 1958/59 a 1962/63: 20 clubes
- 1963/64 a 1964/65: 18 clubes
- 1965/66 a 1967/68: 20 clubes
- 1968/69 a 1969/70: 18 clubes
- 1970/71 a 1996/97: 20 clubes
- 1997/98 a 2001/02: 18 clubes
- 2002/03 a 2022/23: 20 clubes
- 2023/24 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1932/33 a 1987/88: 2
- 1988/89: 3
- 1989/90 a 1993/94: 2
- 1994/95 a 2025/26: 3

**Nome oficial:**

- 1932/33 a 2001/02: Division 1
- 2002/03 a 2025/26: Ligue 1

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1932/33: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols, gols pró: 64 temporadas
- pontos, média de gols (goal average): 23 temporadas
- pontos, média de gols: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1932/33: o Antibes, 1º do grupo B, foi excluído da final por suborno; o Cannes jogou no lugar
- 1973/74: 1 ponto a mais para quem marca 3 gols ou mais no jogo
- 1974/75: 1 ponto a mais por vitória com 3 gols ou mais de diferença
- 1975/76: 1 ponto a mais por vitória com 3 gols ou mais de diferença
- 1992/93: título não atribuído
- 2012/13: punições: Ajaccio -2 pontos
- 2019/20: temporada interrompida em março de 2020 pela pandemia de covid-19 (279 de 380 jogos); a classificação final é pela média de pontos por jogo
- 2021/22: punições: Nice -1 pontos; Lyon -1 pontos
- 2023/24: punições: Montpellier -1 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- PSG: 14
- Saint-Étienne: 10
- Olympique de Marseille: 9
- Monaco: 8
- Nantes: 8
- Lyon: 7
- Reims: 6
- Bordeaux: 6
- Lille: 4
- Nice: 4
- Sète: 2
- Sochaux: 2
- Olympique Lillois: 1
- Racing Paris: 1
- CO Roubaix-Tourcoing: 1
- Strasbourg: 1
- Auxerre: 1
- Lens: 1
- Montpellier: 1
- Sem campeão: 1992/93

**Rebaixamentos:** 243 no total; quem mais caiu: Metz (12), Strasbourg (10), Nancy (10), Valenciennes (8), Rennes (8).

**Punições em pontos:**

- 2012/13: Ajaccio -2
- 2021/22: Nice -1
- 2021/22: Lyon -1
- 2023/24: Montpellier -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/fra-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1932/33 · FC Mulhouse · Olympique Lillois Lille:** [1, 2] o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- **1932/33 · Stade Olympique Montpellierain · SC Fives Lille:** [4, 2] o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- **1932/33 · CA Paris (alt) · SC Fives Lille:** [1, 2] o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- **1932/33 · SC Fives Lille · Stade Olympique Montpellierain:** [2, 3] o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- **1932/33 · SC Fives Lille · CA Paris (alt):** [0, 2] o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- **1947/48 · Racing Club de France · Stade Francais FC:** [5, 1] o ogol, a matriz da RSSSF e a grade da Wikipédia fr dão 5-1; a base traz 0-1 (o placar do outro jogo)
- **1947/48 · Stade Francais FC · Racing Club de France:** [1, 0] o ogol, a matriz da RSSSF e a grade da Wikipédia fr dão 1-0; a base traz 1-5 (o placar do outro jogo)

### Resultados decididos fora de campo (`TRIBUNAL`)

- **1990/91 · Sporting Toulon Var · Paris Saint-Germain:** [v] empate em campo mudado em vitória do PSG (RSSSF: "changed in win for Paris St. Germain"; a tabela da RSSSF e a da Wikipédia contam a vitória)
- **2000/01 · AS Saint-Etienne · Toulouse FC:** [0, 0, v, 1-0] o Saint-Étienne escalou jogador com passaporte falso: vitória dada ao Toulouse com 0-0 (RSSSF)
- **2000/01 · FC Metz · Stade Rennes:** [0, 2, 2-2] o Metz escalou o goleiro Mondragón irregularmente: 0-2 para o Rennes (RSSSF)
- **2013/14 · FC Nantes · SC Bastia:** [0, 0, v, 2-0] vitória dada ao Bastia com 0-0 (RSSSF: "awarded 0-0 win to Bastia; originally 2-0")
- **1946/47 · Olympique Marseille · Girondins Bordeaux:** [0, 0, m, 0-0] as tabelas das Wikipédias fr e en contam a vitória do Marseille (a grade fr mostra 0-0), e só com ela as tabelas fecham; não conferido em jornal da época (revisão FR-005)
- **1951/52 · Olympique Marseille · Racing Club de France:** [0, 0, v, 2-3 (abandonado aos 88 minutos, invasão de campo)] vitória dada ao Racing com 0-0 (Wikipédia fr: "gagné 0-0 sur tapis vert"; transfermarkt: W.O.) (revisão FR-003)
- **1955/56 · AS Nancy · Olympique Marseille:** [0, 0, v, 2-4 (abandonado aos 87 minutos, invasão de campo)] vitória dada ao Marseille com 0-0 (Wikipédia fr: "gagné sur tapis vert par l'OM"; transfermarkt: W.O.) (revisão FR-004)
- **1992/93 · Valenciennes FC · Olympique Marseille:** [0, 0, nenhum, 0-1] declarado perdido para os dois clubes (caso VA-OM; Wikipédia fr; a RSSSF também conta derrota para o Marseille) (revisão FR-006)
- **2016/17 · SC Bastia · Olympique Lyon:** [0, 0, v, 0-0 (abandonado no intervalo)] abandonado no intervalo por invasão de campo; vitória dada ao Lyon com 0-0 (RSSSF; as tabelas não contam os gols)

### Jogos que faltavam na base e foram acrescentados (`ACRESCIMOS`)

- **2006/07 · FC Nantes · Toulouse FC:** [2007-05-19, 0, 0, v] falta no engsoccerdata; o ogol o marca como W.O.: invasão de campo da torcida do Nantes, a liga deu a vitória ao Toulouse e manteve o 0-0 (RSSSF: "awarded 0-0 win to Toulouse"; a tabela da Wikipédia conta a vitória)

### Gols de artilheiro corrigidos (`GOLS_ARTILHEIRO`)

- **1992/93 · Alen Bokšić:** [23] a RSSSF dá 22; fica a contagem oficial da LFP (23), como no ES-005 (decisão D-17 b)

### Temporadas montadas pelo calendário do ogol (`FORCAR_OGOL`)

- **1932/33:** o engsoccerdata junta os dois grupos de 1932/33 num só, de 14 clubes, todos os jogos em 01/07/1933
- **1933/34:** o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- **1934/35:** o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- **1935/36:** o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- **1936/37:** o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)

### Temporadas interrompidas (`INTERROMPIDAS`)

- **2019/20:** interrompida em março de 2020 pela pandemia de covid-19 (279 de 380 jogos); a classificação final é pela média de pontos por jogo

### Fora da temporada seguinte por fusão (`FUSOES`)

- **1938/39 · Olympique Lillois Lille:** fundiu-se com o SC Fives no Lille OSC (guerra), que ficou com a vaga dos dois
- **1938/39 · SC Fives Lille:** fundiu-se com o Olympique Lillois no Lille OSC (guerra), que ficou com a vaga dos dois
- **1938/39 · Excelsior Roubaix:** fundiu-se com o RC Roubaix no CO Roubaix-Tourcoing (guerra), que ficou com a vaga do Excelsior
- **1938/39 · RC Roubaix:** fundiu-se com o Excelsior no CO Roubaix-Tourcoing (guerra)
- **1966/67 · Toulouse FC (1937):** fundiu-se com o Red Star, que ficou com a vaga (Red Star FC)

### Rebaixamentos fora de campo (observação na classificação) (`ADMINISTRATIVOS`)

- **1990/91 · Girondins Bordeaux:** rebaixado administrativamente pela DNCG
- **1990/91 · Stade Brest:** rebaixado administrativamente pela DNCG
- **1990/91 · OGC Nice:** rebaixado administrativamente pela DNCG
- **1993/94 · Olympique Marseille:** rebaixado pela FFF (caso VA-OM)
- **2000/01 · Toulouse FC:** rebaixado administrativamente pela DNCG (para o National)
- **2016/17 · SC Bastia:** rebaixado administrativamente pela DNCG
- **1932/33 · FC Antibes:** 1º do grupo B, excluído da final por suborno (revisão FR-020); não há 3º lugar oficial

### Ajustes da Wikipédia que não são punição (`IGNORAR_AJUSTE`)

- **1992/93 · Valenciennes FC:** a Wikipédia en desconta 1 ponto para representar a derrota dos dois no tribunal
- **1992/93 · Olympique Marseille:** a Wikipédia en desconta 1 ponto para representar a derrota dos dois no tribunal

### Punições que só a RSSSF traz e não se confirmam (`NAO_PUNIR`)

- **2008/09 · Le Havre AC:** a RSSSF dá 1 ponto a menos ao Le Havre; as Wikipédias fr e en dão 26 pontos, sem punição nem nota

### Ordem pelo critério de desempate da época (`ORDEM_PELO_CRITERIO`)

- **1953/54:** pela média de gols, a regra da época, Nancy (50/65 = 0,769) fica à frente do Metz (45/59 = 0,763), como na Wikipédia fr; a RSSSF põe o Metz em 12º

### Artilheiros empatados que a RSSSF não lista (`ARTILHEIROS_EXTRA`)

- **1979/80 · Delio Onnis · AS Monaco:** 21
- **1983/84 · Patrice Garande · AJ Auxerre:** 21

### Nomes de artilheiros acertados (`NOMES_ARTILHEIRO`)

- **Tadeusz "Thadée" Cisowski:** Thadée Cisowski
- **Touré Sékou:** Sékou Touré
- **André "Trello" Abbeglen:** André Abegglen
- **Robert Furois "Mercier":** Robert Mercier
- **Deszö Kronenberger "Koranyi":** Désiré Koranyi
- **Edouard Kargulewicz "Kargu":** Édouard Kargu
- **Pedro Correia "Pauleta":** Pauleta
- **Alen Boksic:** Alen Bokšić
- **Zlatan Ibrahimovic:** Zlatan Ibrahimović
- **Vahid Halilhodzic:** Vahid Halilhodžić

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1937/38:** Excelsior 4-0 Valenciennes e Valenciennes 1-1 Excelsior: a Wikipédia fr dá 5-0 e 1-0, que fecham com as tabelas das Wikipédias fr e en; conferir num jornal da época antes de mudar (revisão FR-017) / a RSSSF chama de "AMIENS" o clube que o ogol e a Wikipédia dão como Antibes (os resultados são os mesmos) / o ogol não tem a data de mais da metade dos jogos (traz 01/07/1937): ficam sem data / a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- **1945/46:** Bordeaux 0-3 Sète e Sète 2-4 Bordeaux: a Wikipédia fr dá Bordeaux 4-2 e Sète 3-0. Fica a base; conferir num jornal da época (revisão FR-017) / Red Star x Cannes: a base traz 1-1 e o ogol 0-0. A tabela da RSSSF e a da Wikipédia fecham com 0-0, mas a nota da RSSSF diz "possibly Red Star - Cannes 1-1; off. goal averages 63-60 (RS) resp. 52-56 (C)", que é o 1-1 da base. Fica a base
- **1946/47:** a tabela da RSSSF dá ao CO Roubaix-Tourcoing 11 derrotas (os números não somam 38 jogos; são 9)
- **1951/52:** a tabela da RSSSF conta Marseille x Racing (0-0, vitória do Racing no tribunal) como empate; a da Wikipédia conta a vitória e fecha com os jogos
- **1953/54:** a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- **1955/56:** a tabela da RSSSF conta Nancy x Marseille (0-0, vitória do Marseille no tribunal) como empate; a da Wikipédia en erra 1 gol de Marseille e Nancy (a Wikipédia fr fecha com os jogos)
- **1975/76:** a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- **1979/80:** a RSSSF chama de "GRENOBLE" o Bastia (o Grenoble não estava na 1ª divisão) / a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- **1984/85:** a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- **1952/53:** a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- **1965/66:** a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- **1986/87:** a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- **1963/64:** Toulouse x Reims: a base e a tabela da Wikipédia trazem 0-0; o ogol e a matriz da RSSSF trazem 2-2 (e a tabela da RSSSF tem 8 gols a menos para o Toulouse). Fica a base
- **1971/72:** Nice x Lille: a base, o ogol e a tabela da Wikipédia trazem 3-1; a RSSSF traz 3-0. Fica a base
- **1992/93:** o título foi tirado do Marseille (suborno no jogo com o Valenciennes) e ninguém foi declarado campeão / Valenciennes x Marseille (20/05/1993, o jogo do caso VA-OM): 0-1 em campo; declarado perdido para os dois, com 0-0 (Wikipédia fr; revisão FR-006) / a tabela da Wikipédia en conta esse jogo como empate e desconta 1 ponto de cada um; a da RSSSF dá ao Valenciennes 57 gols sofridos (os jogos, 56)
- **2008/09:** Le Havre: a RSSSF dá 1 ponto a menos; as Wikipédias fr e en dão 26 pontos, sem punição nem nota. Fica sem punição (revisão FR-010)
- **1958/59:** Sochaux 4-3 Rennes (24/05/1959): a base, o ogol, o transfermarkt e a Wikipédia fr (grade e tabela) dão 4-3; só a RSSSF e a tabela da Wikipédia en dão 2-1. Fica o 4-3 (revisão FR-008)
- **1935/36:** Valenciennes 0-1 Marseille e Marseille 2-2 Valenciennes: a Wikipédia fr dá o mando ou o placar ao contrário (2-2 e 1-0). Fica a base; conferir num jornal da época (revisão FR-017)
- **1950/51:** Toulouse 0-2 Lille e Lille 1-2 Toulouse: a Wikipédia fr e a RSSSF dão Lille 2-0 e Toulouse 2-1. Fica a base (o ogol e o transfermarkt também); conferir num jornal da época (revisão FR-017)

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Barrages (jogos de acesso e rebaixamento contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).
- **Campeonatos de guerra (1939/40-1944/45)** e os campeonatos amadores de antes de 1932: ficam de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.
- Revisão FR-009: 99 jogos (1948/49-1998/99) em que o transfermarkt e o ogol diferem da base por 1 ou 2 dias; só os 41 de 3 dias ou mais foram corrigidos. Conferir uma rodada num jornal (L'Équipe na Gallica) antes de trocar os outros.
- Revisão FR-017: 4 pares de jogos em que a Wikipédia fr dá outro mando ou placar (1935/36, 1937/38, 1945/46, 1950/51); fica a base até conferir num jornal da época (anotado em EXPLICACOES).
- Revisão FR-005: a vitória do Marseille sobre o Bordeaux em 27/10/1946 (0-0 no tribunal) vem das tabelas das Wikipédias; conferir no L'Équipe de 28/10/1946.
- Árbitro: os arquivos do football-data da França não trazem (revisão FR-022); seria jogo a jogo pelo transfermarkt.

## 10. Arquivos

- Código: `coleta/fra-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_fra.py`.
- Fontes baixadas: `data/coleta/fra-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-fra-1/`.
- Pacote: `data/coleta/fra-1/pacote/`; relatório: `docs/coleta/fra-1.md`.
- Refazer do zero: `python coleta/fra-1/baixar.py ...` (ver o docstring), `python coleta/fra-1/importar.py`, `python coleta/comum-europa/testar_carga.py fra-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

