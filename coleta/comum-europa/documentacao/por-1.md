# Campeonato Português (`por-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/por-1/pacote/` e do importador `coleta/por-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/por-1.md`.

## 1. O que temos

- **Edições:** 92, de 1934/35 a 2025/26.
- **Jogos:** 20978; **gols:** 59544; **gols com autor:** 18958 (32%); **cartões:** 30915; **jogos com estatísticas** (chutes, faltas, escanteios): 2754.
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

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 81, confronto direto aplicado de novo entre os que seguem empatados em 3, o mesmo com saldo e gols fora de casa no confronto em 6, saldo de gols em 1, média de gols em 1); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 171 tabelas fecham com os jogos e 13 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1986/87, 1994/95, 2007/08.
- Temporadas com alguma tabela divergente: 1947/48, 1986/87, 1990/91, 1992/93, 1994/95, 1995/96, 1998/99, 2007/08, 2008/09, 2019/20.
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
| 1990s | 3134 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 10% | 0.0 |
| 2000s | 2796 | 100% | 34% | 100% | 34% | 33% | 0% | 0% | 94% | 1.7 |
| 2010s | 2796 | 100% | 100% | 100% | 92% | 74% | 0% | 33% | 98% | 5.7 |
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

- pontos, confronto direto, saldo de gols, gols pró: 81 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo e gols fora de casa no confronto direto, saldo de gols, gols pró: 6 temporadas
- pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo de gols, gols pró: 3 temporadas
- pontos, média de gols (goal average): 1 temporadas
- pontos, saldo de gols, gols pró: 1 temporadas

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
- 2007/08: punições: Belenenses -3 pontos; Porto +0 pontos; União de Leiria -3 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Benfica: 38
- Porto: 31
- Sporting: 21
- Belenenses: 1
- Boavista: 1

**Rebaixamentos:** 206 no total; quem mais caiu: Beira-Mar (10), Vitória de Setúbal (8), Académica (7), Barreirense (7), Estoril (6).

**Punições em pontos:**

- 2007/08: Belenenses -3
- 2007/08: União de Leiria -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/por-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1980/81 · Benfica · Espinho:** [2, 1] o ogol e a matriz da RSSSF trazem 2-0; o transfermarkt e as matrizes das Wikipédias pt e en, 2-1 (os totais não mudam)
- **1980/81 · Espinho · Benfica:** [2, 0] o ogol e a matriz da RSSSF trazem 3-0; a ficha do ogol lista só 2 gols (Vitorino Belinha 2', Carlos Coelho 59'), como o transfermarkt e as Wikipédias pt e en
- **1995/96 · Leça · Boavista:** [0, 3] o ogol traz 0-2; a matriz e a tabela da RSSSF, a tabela da Wikipédia, o engsoccerdata e o football-data trazem 0-3

### Resultados decididos fora de campo (`TRIBUNAL`)

- **1960/61 · Atlético CP · Leixões:** [0, 0, v, 0-0] o resultado não foi homologado e os pontos da vitória foram dados ao Leixões (ficha do ogol: "derrota administrativa (0-0)"). A matriz da RSSSF traz 0-3 neste jogo e 3-1 no Leixões x Atlético (o ogol, 6-1); as duas versões dão os mesmos totais, e as tabelas da RSSSF e da Wikipédia fecham com elas. Fica o ogol
- **1974/75 · CUF · Vitória de Setúbal:** [1, 1, m, 1-1] derrota administrativa do Vitória de Setúbal (ficha do ogol: "Vitória FC: derrota administrativa (0-0)", 1-1 no intervalo). A matriz da RSSSF, o transfermarkt e as Wikipédias trazem outra versão dos dois jogos (CUF 0-2 Vitória e Vitória 1-2 CUF), que dá os mesmos totais e também fecha com as tabelas. Fica o ogol, que registra a decisão (revisão PT-009)
- **1986/87 · Braga · Benfica:** [1, 1, nenhum, 1-1] interrompido aos 86 minutos por invasão de campo; a Federação deu derrota aos dois clubes (Diário de Lisboa, 18/07/1987; ficha do ogol; Wikipédia pt). O Benfica é campeão nos dois casos (revisão PT-004, decisão D-20 b)
- **1975/76 · Atlético CP · Sporting:** [3, 0] derrota do Sporting por invasão de campo (ficha do ogol: 3-0); a matriz da RSSSF traz 3-0
- **1986/87 · Belenenses · Marítimo:** [0, 3, 1-0] o Belenenses escalou irregularmente o jogador Mapuata e perdeu por 0-3 (ficha do ogol; matriz da RSSSF)
- **1989/90 · Nacional da Madeira · Belenenses:** [3, 0, 1-1] o Belenenses escalou irregularmente o avançado Macaé e perdeu por 3-0 (ficha do ogol; matriz da RSSSF)
- **2007/08 · Belenenses · Naval 1º de Maio:** [0, 3, 2-1] o Belenenses escalou um jogador irregular (16ª rodada): derrota por 0-3 (ficha do ogol; RSSSF: "awarded 0-3; originally 2-1") e mais 3 pontos descontados (RSSSF e Wikipédia)

### Jogos que faltavam na base e foram acrescentados (`ACRESCIMOS`)

- **2013/14 · Benfica · Sporting:** [2014-02-11, 2, 0, 18] falta no calendário do ogol; o football-data e o engsoccerdata trazem 2-0 em 11/02/2014 (o jogo da 18ª rodada, adiado); as tabelas da RSSSF e da Wikipédia só fecham com ele

### Gols de artilheiro corrigidos (`GOLS_ARTILHEIRO`)

- **2018/19 · Haris Seferovic:** [23] a RSSSF dá 33 (erro de digitação); a Bola de Prata, a Wikipédia pt e os gols da ESPN dão 23

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1946/47 · SL Elvas:** terminou em 10º; em 1947 fundiu-se com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão
- **2017/18 · Belenenses:** a SAD separou-se do clube em 2018 e seguiu na 1ª divisão como Belenenses SAD (clube à parte); o CF Os Belenenses recomeçou nas divisões distritais, sem ter sido rebaixado em campo

### Temporadas sem rebaixamento (`SEM_REBAIXAMENTO`)

- 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944

### Temporadas com a ordem oficial da RSSSF (`ORDEM_RSSSF`)

- **1944/45:** 2º Sporting e 3º Belenenses (27 pontos), 6º Olhanense e 7º Estoril (16): confronto direto, como na RSSSF (lista de campeões: "runners-up: Sporting CP") e na Wikipédia pt (revisão PT-003)
- **2005/06:** 13º Naval e 14º Académica (39 pontos, com o Belenenses): confronto direto entre os três (Naval 7, Académica 5, Belenenses 4), como na RSSSF e na Wikipédia pt (revisão PT-005, decisão D-19 c)

### Posições fixadas por decisão de tribunal (`ORDEM_FIXA`)

- **1986/87:** {9: 'Académica', 10: 'Portimonense', 11: 'Braga', 12: 'Rio Ave', 13: 'Marítimo'}

### Ajustes de pontos que valem hoje (`AJUSTES`)

- **2007/08 · Porto:** [0] 6 pontos descontados em 2008 (caso Apito Final) e devolvidos em 2017 pelo Conselho de Justiça da FPF

### Observações na classificação final (`OBS_CLASSIF`)

- **1950/51 · Vitória de Setúbal:** rebaixado em 12º; a Wikipédia pt confirma a queda (o Vitória de Guimarães, 13º, ficou)
- **1961/62 · Beira-Mar:** rebaixado em 11º; a Wikipédia pt confirma a queda (o Lusitano de Évora, 12º, ficou)
- **1973/74 · Beira-Mar:** rebaixado em 13º; a Wikipédia pt confirma a queda (o Leixões, 14º, ficou)
- **1997/98 · Leça:** rebaixado administrativamente (corrupção num jogo da 2ª Divisão B em 1993); o Chaves, 16º, ficou no lugar
- **1997/98 · Chaves:** 16º, ficou na 1ª divisão no lugar do Leça, rebaixado administrativamente
- **2005/06 · Gil Vicente:** rebaixado no lugar do Belenenses (caso Mateus, jogador inscrito irregularmente)
- **2005/06 · Belenenses:** 15º, ficou na 1ª divisão: o Gil Vicente caiu no lugar (caso Mateus)
- **2007/08 · Boavista:** rebaixado pelo caso Apito Final (terminou em 9º)
- **2007/08 · União de Leiria:** 3 pontos a menos (caso Apito Final)
- **2008/09 · Estrela da Amadora:** rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou
- **2019/20 · Vitória de Setúbal:** rebaixado por não cumprir as regras de licenciamento; o Portimonense, 17º, ficou
- **2019/20 · Desportivo das Aves:** rebaixado por não cumprir as regras de licenciamento
- **2023/24 · Estrela da Amadora:** Club Football Estrela da Amadora (da fusão de 2020), contado junto do CF Estrela da Amadora de 1932, como no ogol (decisão D-24 c)
- **1946/47 · SL Elvas:** fundiu-se em 1947 com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão (decisão D-24 d)

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1947/48:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Atlético CP)
- **1986/87:** Braga x Benfica (31/05/1987): derrota para os dois no tribunal; as tabelas da RSSSF e da Wikipédia en contam o 1-1 de campo e não fecham nesses dois clubes; a da Wikipédia pt conta a decisão (Benfica 48, Braga 25 e 11º)
- **1990/91:** a tabela da Wikipédia troca os números do Marítimo e do Farense; a da RSSSF fecha com os jogos / a matriz da RSSSF traz trocadas as colunas 13 e 14 (Gil Vicente e Famalicão): desfeita a troca, os 380 placares batem com o ogol
- **1992/93:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Porto: 57 gols pró; os jogos dão 59)
- **1994/95:** Benfica 1-2 Sporting (30/04/1995): o ogol, o transfermarkt, a Wikipédia pt e o artigo da temporada do Benfica ("perdeu os dois jogos contra o Sporting") dão 1-2; a matriz e a tabela da RSSSF, o engsoccerdata e o football-data, 2-0. Fica o 1-2 (revisão PT-002)
- **1995/96:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Benfica)
- **1998/99:** a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos (Académica: 70 gols contra; os jogos dão 71)
- **2005/06:** Académica, Naval e Belenenses terminaram com 39 pontos; a Wikipédia (e os sites que a repetem) põe a Académica em 13º e o Naval em 14º, a RSSSF o contrário (que é o que dá o confronto direto entre os três). Fica a da RSSSF / o Belenenses terminou em 15º, na zona de rebaixamento, e ficou na 1ª divisão: o Gil Vicente foi rebaixado no lugar dele (caso Mateus, jogador inscrito irregularmente)
- **2007/08:** Porto com 75 pontos: os 6 descontados em 2008 (caso Apito Final) foram devolvidos em 2017 pelo Conselho de Justiça da FPF, como nas Wikipédias pt e en (decisão D-20 a); União de Leiria com 3 pontos a menos, como na RSSSF (sem fonte da devolução). A ordem é a mesma nos dois casos / Boavista rebaixado pelo caso Apito Final (terminou em 9º); o Paços de Ferreira, 15º, ficou na 1ª divisão
- **2008/09:** a tabela da RSSSF dá 46 pontos ao Leixões (os jogos dão 45, como na Wikipédia) / Estrela da Amadora rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou na 1ª divisão
- **2019/20:** a tabela da Wikipédia dá um gol pró e um contra a menos ao Gil Vicente e ao Paços de Ferreira; os jogos fecham com a RSSSF, o football-data e o engsoccerdata / Vitória de Setúbal e Desportivo das Aves rebaixados por não cumprirem as regras de licenciamento; o Portimonense, 17º, ficou na 1ª divisão

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.
- **Público e estádio antes da ESPN:** nenhuma fonte em lote.
- **Play-offs de manutenção (contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).
- **Campeonato de Portugal (1921/22 a 1937/38, em mata-mata):** é outra competição; fica de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Autores dos gols: RSSSF (1999/00-2005/06, onde a soma fecha), ficha do ogol (2001/02, que a RSSSF não traz, e os jogos em que a ESPN falta ou não fecha) e ESPN (2006/07+). Antes de 1999/00, nenhuma fonte em lote. Sem autor ficam 103 jogos de 2001/02 e 27 de 2010/11 (a ficha do ogol também não fecha).
- Revisão PT-020: árbitro e público pelo transfermarkt (jogo a jogo, ~11 mil páginas) ou pela ficha do ogol: não feito (custo alto); o football-data de Portugal não traz árbitro.
- Revisão PT-010: Belenenses x Sporting (1938/39) e os dois jogos do Académico do Porto em 04/02/1940 (1939/40) seguem com a data do ogol; o transfermarkt repete o ogol e a ficha não decide. Conferir num jornal da época.

## 10. Arquivos

- Código: `coleta/por-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_por.py`.
- Fontes baixadas: `data/coleta/por-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-por-1/`.
- Pacote: `data/coleta/por-1/pacote/`; relatório: `docs/coleta/por-1.md`.
- Refazer do zero: `python coleta/por-1/baixar.py ...` (ver o docstring), `python coleta/por-1/importar.py`, `python coleta/comum-europa/testar_carga.py por-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

