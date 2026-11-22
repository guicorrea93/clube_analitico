# Campeonato Português (`por-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/por-1/pacote/` e do importador `coleta/por-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/por-1.md`.

## 1. O que temos

- **Edições:** 92, de 1934/35 a 2025/26.
- **Jogos:** 20978; **gols:** 59543; **gols com autor:** 13874 (23%); **cartões:** 30915; **jogos com estatísticas** (chutes, faltas, escanteios): 2754.
- **Clubes:** 73; **artilheiros:** 92 temporadas com artilheiro (99 linhas, com empates).
- **Classificação final:** 92 temporadas; **rodada a rodada:** 92 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2820 linhas, de 184 tabelas.
- **Observação da competição:** 1ª divisão portuguesa desde o Campeonato da Liga (1934/35 a 1937/38, experimental; os títulos contam entre os da 1ª divisão): Primeira Divisão de 1938/39 a 1998/99 e Primeira Liga depois. Até 1944/45 os participantes saíam dos campeonatos regionais. Não inclui os play-offs de manutenção contra clubes da 2ª divisão.

## 2. Fontes e regras

**Fontes:**

- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; ficha dos jogos decididos fora de campo; calendários guardados em `data/cache/ogol-por-1/` para os escudos;
- RSSSF: tabela final e matriz de resultados de 1934/35 a 2004/05 (conferência jogo a jogo), tabela final das temporadas seguintes, lista de campeões e de artilheiros (com o clube);
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;
- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ESPN (liga `por.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;
- Wikipédia (en): tabela final de cada temporada (ordem oficial, punições e marca de rebaixamento).

**Regras da importação:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Lisboa; Açores nos jogos em casa do Santa Clara). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (até 1944/45 não havia rebaixamento: os participantes saíam dos campeonatos regionais). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente em outra fonte numa temporada em que as tabelas publicadas fecham com o ogol é erro da outra fonte e fica só anotado; quando a outra fonte e as tabelas publicadas concordam contra o ogol, o placar é corrigido (CORRECOES e TRIBUNAL em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 80, confronto direto aplicado de novo entre os que seguem empatados em 4, o mesmo com saldo e gols fora de casa no confronto em 6, saldo de gols em 1, média de gols em 1); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 175 tabelas fecham com os jogos e 9 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: 1947/48, 1990/91, 1992/93, 1994/95, 1995/96, 1998/99, 2007/08, 2008/09, 2019/20.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1930s | 370 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1318 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1820 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1820 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2342 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2746 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3134 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 2796 | 100% | 34% | 100% | 34% | 33% | 0% | 0% | 33% | 1.7 |
| 2010s | 2796 | 100% | 100% | 100% | 92% | 74% | 0% | 33% | 96% | 5.7 |
| 2020s | 1836 | 100% | 100% | 100% | 100% | 83% | 0% | 100% | 100% | 5.5 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1934/35 a 1938/39: 8 clubes
- 1939/40: 10 clubes
- 1940/41: 8 clubes
- 1941/42: 12 clubes
- 1942/43 a 1944/45: 10 clubes
- 1945/46: 12 clubes
- 1946/47 a 1970/71: 14 clubes
- 1971/72 a 1986/87: 16 clubes
- 1987/88 a 1988/89: 20 clubes
- 1989/90: 18 clubes
- 1990/91: 20 clubes
- 1991/92 a 2005/06: 18 clubes
- 2006/07 a 2013/14: 16 clubes
- 2014/15 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1934/35 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1934/35 a 1937/38: Campeonato da Liga
- 1938/39 a 1998/99: Primeira Divisão
- 1999/00 a 2025/26: Primeira Liga

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto, saldo de gols, gols pró: 80 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo e gols fora de casa no confronto direto, saldo de gols, gols pró: 6 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo de gols, gols pró: 4 temporadas
- pontos, saldo de gols, gols pró: 1 temporadas
- pontos, média de gols (goal average): 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1934/35: Campeonato da Liga, experimental (o campeão nacional ainda era o do Campeonato de Portugal); o título conta hoje entre os da 1ª divisão; participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1935/36: Campeonato da Liga, experimental (o campeão nacional ainda era o do Campeonato de Portugal); o título conta hoje entre os da 1ª divisão; participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1936/37: Campeonato da Liga, experimental (o campeão nacional ainda era o do Campeonato de Portugal); o título conta hoje entre os da 1ª divisão; participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1937/38: Campeonato da Liga, experimental (o campeão nacional ainda era o do Campeonato de Portugal); o título conta hoje entre os da 1ª divisão; participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1938/39: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1939/40: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1940/41: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1941/42: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1942/43: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1943/44: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 1944/45: participantes classificados pelos campeonatos regionais, sem rebaixamento
- 2007/08: punições: Belenenses -3 pontos; Porto -6 pontos; União de Leiria -3 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Benfica: 38
- Porto: 31
- Sporting: 21
- Belenenses: 1
- Boavista: 1

**Rebaixamentos:** 206 no total; quem mais caiu: Beira-Mar (10), Vitória de Setúbal (8), Académica (7), Barreirense (7), Estoril (6).

**Punições em pontos:**

- 2007/08: Porto -6
- 2007/08: Belenenses -3
- 2007/08: União de Leiria -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/por-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1994/95 · Benfica · Sporting:** [2, 0] o ogol traz 1-2; a matriz e a tabela da RSSSF, o engsoccerdata e o football-data trazem 2-0 (e a lista de campeões da RSSSF põe o Sporting, vice, 9 pontos atrás do Porto, o que só fecha com 2-0)
- **1995/96 · Leça · Boavista:** [0, 3] o ogol traz 0-2; a matriz e a tabela da RSSSF, a tabela da Wikipédia, o engsoccerdata e o football-data trazem 0-3

### Resultados decididos fora de campo (`TRIBUNAL`)

- **1960/61 · Atlético CP · Leixões:** [0, 0, v, 0-0] o resultado não foi homologado e os pontos da vitória foram dados ao Leixões (ficha do ogol: "derrota administrativa (0-0)"). A matriz da RSSSF traz 0-3 neste jogo e 3-1 no Leixões x Atlético (o ogol, 6-1); as duas versões dão os mesmos totais, e as tabelas da RSSSF e da Wikipédia fecham com elas. Fica o ogol
- **1974/75 · CUF · Vitória de Setúbal:** [1, 1, m, 1-1] derrota administrativa do Vitória de Setúbal (ficha do ogol; 1-1 no intervalo). As tabelas da RSSSF e da Wikipédia contam a vitória do CUF com o 1-1 de campo (um gol pró e um contra para cada um); a matriz da RSSSF traz 0-2 neste jogo e 1-2 no Vitória x CUF (o ogol, 2-1), o que não fecha com as tabelas
- **1975/76 · Atlético CP · Sporting:** [3, 0] derrota do Sporting por invasão de campo (ficha do ogol: 3-0); a matriz da RSSSF traz 3-0
- **1986/87 · Belenenses · Marítimo:** [0, 3, 1-0] o Belenenses escalou irregularmente o jogador Mapuata e perdeu por 0-3 (ficha do ogol; matriz da RSSSF)
- **1989/90 · Nacional da Madeira · Belenenses:** [3, 0, 1-1] o Belenenses escalou irregularmente o avançado Macaé e perdeu por 3-0 (ficha do ogol; matriz da RSSSF)
- **2007/08 · Belenenses · Naval 1º de Maio:** [0, 3, 2-1] o Belenenses escalou um jogador irregular (16ª rodada): derrota por 0-3 (ficha do ogol; RSSSF: "awarded 0-3; originally 2-1") e mais 3 pontos descontados (RSSSF e Wikipédia)

### Jogos sem placar na base em que valeu o placar de campo (`CAMPO`)

- **1986/87 · Braga · Benfica:** [1, 1] a ficha do ogol diz que o jogo foi interrompido aos 86 minutos por invasão de campo e que os dois clubes foram punidos com derrota; mas a matriz e a tabela da RSSSF e a tabela da Wikipédia contam o empate de campo, 1-1 (com ele, o Benfica é campeão com 49 pontos, como na lista de campeões). Fica o 1-1

### Jogos que faltavam na base e foram acrescentados (`ACRESCIMOS`)

- **2013/14 · Benfica · Sporting:** [2014-02-11, 2, 0, 18] falta no calendário do ogol; o football-data e o engsoccerdata trazem 2-0 em 11/02/2014 (o jogo da 18ª rodada, adiado); as tabelas da RSSSF e da Wikipédia só fecham com ele

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1946/47 · SL Elvas:** terminou em 10º; em 1947 fundiu-se com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão
- **2017/18 · Belenenses:** a SAD separou-se do clube em 2018 e seguiu na 1ª divisão como Belenenses SAD (clube à parte); o CF Os Belenenses recomeçou nas divisões distritais, sem ter sido rebaixado em campo

### Temporadas sem rebaixamento (`SEM_REBAIXAMENTO`)

- 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1947/48:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Atlético CP)
- **1990/91:** a tabela da Wikipédia troca os números do Marítimo e do Farense; a da RSSSF fecha com os jogos / a matriz da RSSSF traz trocadas as colunas 13 e 14 (Gil Vicente e Famalicão): desfeita a troca, os 380 placares batem com o ogol
- **1992/93:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Porto: 57 gols pró; os jogos dão 59)
- **1994/95:** a tabela da Wikipédia dá ao Benfica as vitórias e derrotas do 1-2 contra o Sporting e os gols do 2-0; a da RSSSF fecha com o 2-0
- **1995/96:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Benfica)
- **1998/99:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Académica: 70 gols contra; os jogos dão 71)
- **2005/06:** Académica, Naval e Belenenses terminaram com 39 pontos; a Wikipédia (e os sites que a repetem) põe a Académica em 13º e o Naval em 14º, a RSSSF o contrário (que é o que dá o confronto direto entre os três). Fica a da Wikipédia / o Belenenses terminou em 15º, na zona de rebaixamento, e ficou na 1ª divisão: o Gil Vicente foi rebaixado no lugar dele (caso Mateus, jogador inscrito irregularmente)
- **2007/08:** Porto -6 pontos e União de Leiria -3 pontos (caso Apito Final, corrupção na temporada 2003/04), como na tabela da RSSSF e na classificação do fim da temporada. A Wikipédia de hoje não desconta, porque o Conselho de Justiça da Federação absolveu o Porto em 2017; a ordem é a mesma nos dois casos / Boavista rebaixado pelo caso Apito Final (terminou em 9º); o Paços de Ferreira, 15º, ficou na 1ª divisão
- **2008/09:** a tabela da RSSSF dá 46 pontos ao Leixões (os jogos dão 45, como na Wikipédia) / Estrela da Amadora rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou na 1ª divisão
- **2019/20:** a tabela da Wikipédia dá um gol pró e um contra a menos ao Gil Vicente e ao Paços de Ferreira; os jogos fecham com a RSSSF, o football-data e o engsoccerdata / Vitória de Setúbal e Desportivo das Aves rebaixados por não cumprirem as regras de licenciamento; o Portimonense, 17º, ficou na 1ª divisão

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.
- **Público e estádio antes da ESPN:** nenhuma fonte em lote.
- **Play-offs de manutenção (contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).
- **Campeonato de Portugal (1921/22 a 1937/38, em mata-mata):** é outra competição; fica de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Autores dos gols e cartões antes de 2006/07 (a ESPN começa aí): jogo a jogo (ficha do ogol).
- Pontos do Porto em 2007/08 (Apito Final): ficou o desconto de 6, como no fim da temporada; se o Guilherme preferir a situação de hoje (absolvição em 2017), tirar o desconto em importar.py.

## 10. Arquivos

- Código: `coleta/por-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_por.py`.
- Fontes baixadas: `data/coleta/por-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-por-1/`.
- Pacote: `data/coleta/por-1/pacote/`; relatório: `docs/coleta/por-1.md`.
- Refazer do zero: `python coleta/por-1/baixar.py ...` (ver o docstring), `python coleta/por-1/importar.py`, `python coleta/comum-europa/testar_carga.py por-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

