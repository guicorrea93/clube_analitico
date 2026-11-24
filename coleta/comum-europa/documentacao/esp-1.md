# Campeonato Espanhol (`esp-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/esp-1/pacote/` e do importador `coleta/esp-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/esp-1.md`.

## 1. O que temos

- **Edições:** 95, de 1928/29 a 2025/26.
- **Jogos:** 27716; **gols:** 78392; **gols com autor:** 25072 (32%); **cartões:** 51662; **jogos com estatísticas** (chutes, faltas, escanteios): 7980.
- **Clubes:** 63; **artilheiros:** 95 temporadas com artilheiro (103 linhas, com empates).
- **Classificação final:** 95 temporadas; **rodada a rodada:** 95 temporadas.
- **Tabelas publicadas guardadas para conferência:** 3302 linhas, de 191 tabelas.
- **Observação da competição:** 1ª divisão espanhola (Primera División, "La Liga") desde a criação, em 1929. Sem 1936/37-1938/39 (Guerra Civil). Em 1986/87, depois das 34 rodadas, três grupos de seis (título, 7º-12º e rebaixamento), com os pontos somados. Não inclui as promoções (jogos de acesso e rebaixamento contra clubes da 2ª divisão).

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1928/29-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+) e estatísticas por time (chutes, faltas, escanteios, cartões; 2005/06+). Não traz árbitro na liga espanhola;
- ogol: rodada oficial de cada jogo e conferência de placar; calendários guardados em `data/cache/ogol-esp-1/` para os escudos;
- ESPN (liga `esp.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF (José Vicente Tejedor Carnicero e outros): tabela final de todas as temporadas e matriz de resultados até 1999/2000 (conferência jogo a jogo); artilheiros até 1999/2000;
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões, artilheiros pela contagem oficial da liga (súmulas da LFP; "List of La Liga top scorers") e Troféu Pichichi (do jornal Marca, que a liga não reconhece; anotado quando difere).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Madri; Canárias nos jogos em casa do Las Palmas e do Tenerife). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96.

**Desempate:** a regra espanhola em todas as temporadas (revisão QE-001): pontos, confronto direto (pontos e saldo entre os empatados, de novo entre os que seguem empatados), saldo de gols e gols pró. Ela reproduz a ordem oficial em 95 de 95 temporadas. Na classificação rodada a rodada, o confronto só vale depois de jogados todos os jogos entre os empatados.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 180 tabelas fecham com os jogos e 11 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: 1928/29, 1930/31, 1940/41, 1961/62, 1967/68, 1971/72, 1973/74, 1980/81, 2000/01, 2006/07, 2014/15.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 180 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 756 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1770 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2994 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3372 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3964 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3800 | 100% | 90% | 100% | 89% | 58% | 0% | 50% | 88% | 5.0 |
| 2010s | 3800 | 100% | 100% | 100% | 100% | 97% | 0% | 100% | 100% | 5.6 |
| 2020s | 2280 | 100% | 100% | 100% | 100% | 83% | 0% | 100% | 100% | 5.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1928/29 a 1933/34: 10 clubes
- 1934/35 a 1940/41: 12 clubes
- 1941/42 a 1949/50: 14 clubes
- 1950/51 a 1970/71: 16 clubes
- 1971/72 a 1986/87: 18 clubes
- 1987/88 a 1994/95: 20 clubes
- 1995/96 a 1996/97: 22 clubes
- 1997/98 a 2025/26: 20 clubes

**Pontos por vitória:**

- 1928/29 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1928/29 a 2025/26: Primera División

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1986/87: Liga (liga, pontos_corridos); Fase final (grupos, pontos_corridos)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto (pontos e saldo entre os empatados, de novo entre os que seguem empatados), saldo de gols, gols pró; na classificação de rodada, o confronto só depois de jogados todos os jogos entre eles: 94 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 1 temporadas
- pontos somados aos da 1ª fase; pontos, confronto direto, saldo de gols, gols pró: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1979/80: punições: CD Málaga -3 pontos
- 1986/87: com a ampliação para 20 clubes, os três últimos do grupo de rebaixamento jogaram uma liguilla em turno único, que mandou um só para a 2ª divisão: Racing 1-1 Cádiz (24/06/1987; Racing 4-3 nos pênaltis), Cádiz 1-1 Osasuna (28/06; Cádiz 4-3 nos pênaltis) e Osasuna 2-0 Racing (30/06). Osasuna 3 pontos, Cádiz 2, Racing 1: caiu o Racing (cadizcf.com, racinguismo.com, RSSSF)
- 2003/04: punições: Racing Santander -1 pontos
- 2014/15: punições: Almería -3 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Real Madrid: 36
- Barcelona: 29
- Atlético de Madrid: 11
- Athletic Bilbao: 8
- Valencia: 6
- Real Sociedad: 2
- Betis: 1
- Sevilla: 1
- Deportivo La Coruña: 1

**Rebaixamentos:** 253 no total; quem mais caiu: Betis (11), Murcia (11), Deportivo La Coruña (11), CD Málaga (11), Celta (10).

**Punições em pontos:**

- 1979/80: CD Málaga -3
- 2003/04: Racing Santander -1
- 2014/15: Almería -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/esp-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **2004/05 · CA Osasuna · Albacete:** [3, 2] o engsoccerdata traz 4-2; ogol, football-data, ESPN e as tabelas da RSSSF e da Wikipédia trazem 3-2

### Jogos que faltavam na base e foram acrescentados (`ACRESCIMOS`)

- **1979/80 · CD Malaga · UD Salamanca:** [1980-04-27, 0, 3] falta no engsoccerdata; a matriz da RSSSF traz o jogo: terminou 0-3 em 27/04/1980, foi anulado por irregularidade (o Salamanca perdeu 2 pontos) e o resultado original foi confirmado em 25/05/1982

### Datas corrigidas (`DATAS`)

- **2003/04 · FC Barcelona · Sevilla FC:** [2003-09-03] o "jogo da meia-noite": começou à 00:05 de 03/09/2003 (football-data, ESPN, transfermarkt e BDFutbol); o engsoccerdata e o ogol trazem 02/09

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1935/36 · Real Oviedo:** 3º colocado em 1935/36, teve dispensa de 1939/40 por ter o estádio destruído na guerra e voltou em 1940/41 (Wikipédia es, 1935-36 e 1939-40)

### Rebaixados que a regra geral não pega (`REBAIXADOS_EXTRA`)

- **1935/36 · Atletico Madrid:** 11º em 1935/36, caiu com o Osasuna; voltou à 1ª divisão em 1939/40 ao vencer a repescagem pela vaga do Oviedo (Athletic de Madrid 3-1 Osasuna, Valência, 26/11/1939; Wikipédia es)

### Liguilla / jogos extras fora da tabela (`LIGUILLA`)

- 1986/87: com a ampliação para 20 clubes, os três últimos do grupo de rebaixamento jogaram uma liguilla em turno único, que mandou um só para a 2ª divisão: Racing 1-1 Cádiz (24/06/1987; Racing 4-3 nos pênaltis), Cádiz 1-1 Osasuna (28/06; Cádiz 4-3 nos pênaltis) e Osasuna 2-0 Racing (30/06). Osasuna 3 pontos, Cádiz 2, Racing 1: caiu o Racing (cadizcf.com, racinguismo.com, RSSSF)

### Wikipédia com linhas trocadas (`WIKI_TROCADA`)

- a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem

### Temporadas com a ordem oficial da RSSSF (`ORDEM_RSSSF`)

- **1960/61:** Athletic Bilbao, Betis e Real Sociedad empatados com 30 pontos: no confronto direto entre os três, Athletic e Betis fazem 5 pontos e a Real Sociedad 2; entre os dois, Athletic 0-0 Betis e Betis 1-3 Athletic, e o Athletic fica em 6º. É a ordem da RSSSF e do BDFutbol, e a regra das outras temporadas; a Wikipédia põe o Betis à frente pelo saldo do triangular

### Jogos suspensos e completados em outro dia (`SUSPENSOS`)

- **2004/05 · Real Madrid · Real Sociedad:** começou em 12/12/2004 e foi suspenso aos 88 minutos, com 1-1 (ameaça de bomba); completado em 05/01/2005
- **2023/24 · Granada CF · Athletic Bilbao:** começou em 10/12/2023 e foi suspenso no 1º tempo (morte de um torcedor na arquibancada); completado em 11/12/2023

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1928/29:** a tabela da Wikipédia traz gols errados para Athletic Bilbao (47-34) e Arenas (33-43); a da RSSSF fecha com os jogos (43-33 e 32-39) e dá a ordem
- **1929/30:** a matriz da RSSSF traz 2-1 nos dois jogos de Espanyol x Europa; a base e o ogol trazem 1-2 nos dois (as tabelas não distinguem, porque cada clube fica com uma vitória e uma derrota). Fica a base
- **1930/31:** a tabela da Wikipédia traz 32 gols contra para o Real Madrid; a da RSSSF e os jogos dão 27
- **1940/41:** Valencia x Hércules: a RSSSF (matriz e tabela) traz 6-1; a base, o ogol e a tabela da Wikipédia trazem 6-0. Fica a base
- **1961/62:** a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Osasuna e Mallorca)
- **1967/68:** a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Elche e CD Málaga)
- **1971/72:** a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Sabadell e Córdoba)
- **1973/74:** a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Oviedo e Racing Santander); a Wikipédia também erra vitórias e empates de Atlético de Madrid, Zaragoza e Real Sociedad
- **1979/80:** CD Málaga x AD Almería (30/03/1980): o Málaga não compareceu; vitória de 1-0 dada ao Almería (W.O.) e 3 pontos a menos para o Málaga (RSSSF e Wikipédia). Nas tabelas, o W.O. conta a vitória mas não os gols
- **1980/81:** a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da RSSSF fecha com os jogos e dá a ordem (Atlético de Madrid e Valencia)
- **1986/87:** Real Valladolid x Las Palmas (17/12/1986): o ogol traz 0-0; a base, a matriz e a tabela da RSSSF e a da Wikipédia fecham com 2-1: erro do ogol / 1986/87: com a ampliação para 20 clubes, os três últimos do grupo de rebaixamento jogaram uma liguilla em turno único, que mandou um só para a 2ª divisão: Racing 1-1 Cádiz (24/06/1987; Racing 4-3 nos pênaltis), Cádiz 1-1 Osasuna (28/06; Cádiz 4-3 nos pênaltis) e Osasuna 2-0 Racing (30/06). Osasuna 3 pontos, Cádiz 2, Racing 1: caiu o Racing (cadizcf.com, racinguismo.com, RSSSF). Esses jogos não contam como Primera División (Wikipédia es), e a classificação oficial continua a do grupo de rebaixamento: 16º Osasuna, 17º Racing (rebaixado) e 18º Cádiz (Wikipédia es e RSSSF)
- **1993/94:** Real Madrid x Real Sociedad: o football-data traz 0-1; a base, a matriz da RSSSF e as tabelas fecham com 0-2: erro do football-data
- **1999/00:** Valencia x Mallorca (20/06/2000): o ogol traz 2-0; a base, o football-data, a matriz da RSSSF e as tabelas fecham com 3-0: erro do ogol
- **2000/01:** a tabela da Wikipédia dá ao Espanyol 15 vitórias, 7 empates e 52 pontos; os jogos e a RSSSF dão 14, 8 e 50
- **2002/03:** Villarreal x Celta (18/05/2003): a ESPN traz 6-0; base, ogol, football-data e as tabelas fecham com 5-0 (gols da ESPN descartados)
- **2006/07:** a tabela da Wikipédia traz gols errados para Atlético de Madrid, Levante, Real Sociedad e Gimnàstic; a da RSSSF fecha com os jogos e dá a ordem
- **2011/12:** a ESPN traz 0-0, sem gols, em dez jogos do Granada (agosto a janeiro); os placares da base são confirmados pelo ogol, pelo football-data e pelas tabelas. Esses jogos ficam sem autores de gols
- **2014/15:** Almería: 3 pontos a menos (punição da FIFA por dívida de transferência); a Wikipédia desconta, a tabela da RSSSF não / o Elche (13º) foi rebaixado por dívidas com o fisco e o Eibar (18º) ficou na 1ª divisão: o Elche sai como rebaixado e o Eibar não

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. A RSSSF tem os autores de 2000/01 em diante (a ESPN já cobre) e o ogol tem a ficha de muitos jogos; fica como próximo passo, se aprovado.
- **Público e estádio antes de 2001/02:** idem.
- **Promoções (jogos de acesso e rebaixamento contra clubes da 2ª divisão):** ficam de fora (entram quando a 2ª divisão for coletada).
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).

## 10. Arquivos

- Código: `coleta/esp-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_esp.py`.
- Fontes baixadas: `data/coleta/esp-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-esp-1/`.
- Pacote: `data/coleta/esp-1/pacote/`; relatório: `docs/coleta/esp-1.md`.
- Refazer do zero: `python coleta/esp-1/baixar.py ...` (ver o docstring), `python coleta/esp-1/importar.py`, `python coleta/comum-europa/testar_carga.py esp-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

