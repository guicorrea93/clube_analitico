# Campeonato Norueguês (`nor-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/nor-1/pacote/` e do importador `coleta/nor-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/nor-1.md`.

## 1. O que temos

- **Edições:** 80, de 1937/38 a 2025.
- **Jogos:** 12368; **gols:** 38461; **gols com autor:** 14830 (39%); **cartões:** 11950; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 128; **artilheiros:** 77 temporadas com artilheiro (83 linhas, com empates).
- **Classificação final:** 80 temporadas; **rodada a rodada:** 64 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1693 linhas, de 107 tabelas.
- **Observação da competição:** Os 79 títulos de liga que a federação (NFF) reconhece, desde 1937/38: Norgesserien (1937/38, 1938/39 e 1947/48, grupos regionais e mata-mata), Hovedserien (1948/49 a 1961/62), 1. divisjon (1963-1990), Tippeligaen (1991-2016) e Eliteserien (desde 2017). Não inclui a Prøveligaen de 1914-16 (liga de teste), 1939/40 (interrompida pela guerra) nem a copa, que até 1937 dava o título de campeão norueguês.

## 2. Fontes e regras

**Fontes:**

- Wikipédia (en): tabela de cada fase (ordem oficial, punições), matriz de resultados (base dos jogos de 1948/49 a 1960/61, conferência depois), mata-mata da Norgesserien e finais da Hovedserien;
- Wikipédia (no): a matriz do único grupo da Norgesserien que tem os jogos (Distrito V, grupo B);
- ogol (zerozero): base dos jogos desde 1961/62, com data, hora e rodada; calendários em `data/cache/ogol-nor-1/`;
- RSSSF: página de cada temporada desde 1998 (tabela, placares e autores dos gols de 1999 a 2005), lista de campeões e de artilheiros;
- football-data: placar e hora desde 2012;
- ESPN (liga `nor.1`): estádio, público, gols e cartões nas temporadas que ela cobre (30 clubes casados por votação, pela data e pelo placar).

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; na Norgesserien, o mata-mata e depois a posição no grupo; na Hovedserien, a final e depois a posição no grupo). Pontos 2-1-0 até 1986 e 3-1-0 depois; em 1987, o empate ia para os pênaltis (2 pontos ao vencedor, 1 ao perdedor). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (na Norgesserien, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 28 tabelas, saldo em 65, confronto direto em 0).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 116 tabelas fecham com os jogos e 4 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1947/48, 1971, 1996.
- Temporadas com alguma tabela divergente: 1947/48, 1971, 1996, 2007.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1930s | 121 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 288 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1132 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 983 | 89% | 0% | 89% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 1236 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 1320 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 1570 | 100% | 1% | 100% | 0% | 0% | 0% | 0% | 5% | 0.0 |
| 2000s | 1878 | 100% | 72% | 100% | 22% | 22% | 0% | 0% | 62% | 0.6 |
| 2010s | 2400 | 100% | 100% | 100% | 95% | 83% | 0% | 0% | 93% | 2.6 |
| 2020s | 1440 | 100% | 100% | 100% | 100% | 99% | 0% | 0% | 100% | 3.2 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1937/38: 74 clubes
- 1938/39: 75 clubes
- 1947/48: 74 clubes
- 1948/49 a 1961/62: 16 clubes
- 1963 a 1971: 10 clubes
- 1972 a 1994: 12 clubes
- 1995 a 2008: 14 clubes
- 2009 a 2025: 16 clubes

**Pontos por vitória:**

- 1937/38 a 1986: 2
- 1987 a 2025: 3

**Nome oficial:**

- 1937/38 a 1947/48: Norgesserien
- 1948/49 a 1961/62: Hovedserien
- 1963 a 1990: 1. divisjon
- 1991 a 2016: Tippeligaen
- 2017 a 2025: Eliteserien

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1937/38: Grupos (grupos, pontos_corridos); Preliminar (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico); Desempate da final (mata_mata, jogo_unico)
- 1938/39: Grupos (grupos, pontos_corridos); Preliminar (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Desempate da semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1947/48: Grupos (grupos, pontos_corridos); Preliminar (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Desempate da semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1948/49: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1949/50: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1950/51: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1951/52: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1952/53: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1953/54: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1954/55: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1955/56: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1956/57: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1957/58: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1958/59: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico); Desempate da final (mata_mata, jogo_unico)
- 1959/60: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)
- 1960/61: Grupos (grupos, pontos_corridos); Final (mata_mata, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols: 67 temporadas
- jogo único; empate, jogo extra: 20 temporadas
- pontos, média de gols (goal average): 12 temporadas
- soma dos placares; empate, jogo extra ou sorteio: 9 temporadas
- pontos, saldo de gols; empate decidido nos pênaltis: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1961/62: liga de um ano e meio, na passagem para o calendário de ano civil
- 1987: empate decidido nos pênaltis: 2 pontos ao vencedor e 1 ao perdedor (o ponto a mais em ajuste_pontos)
- 1995: punições: Vålerenga -2 pontos
- 2012: punições: Odd -1 pontos
- 2015: punições: Lillestrøm -1 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Rosenborg: 26
- Fredrikstad: 9
- Viking: 9
- Lillestrøm: 5
- Vålerenga: 5
- Molde: 5
- Bodø/Glimt: 4
- Larvik Turn: 3
- Brann: 3
- Lyn: 2
- Strømsgodset: 2
- Start: 2
- Freidig: 1
- Fram Larvik: 1
- Skeid: 1
- Moss: 1
- Stabæk: 1

**Rebaixamentos:** 289 no total; quem mais caiu: Start (11), Brann (11), Mjøndalen (8), Vålerenga (8), Lyn (8).

**Punições em pontos:**

- 1987: Moss 2
- 1987: Molde 3
- 1987: Kongsvinger 4
- 1987: Rosenborg 4
- 1987: Tromsø 7
- 1987: Vålerenga 1
- 1987: Brann 3
- 1987: Lillestrøm 3
- 1987: HamKam 3
- 1987: Mjøndalen 2
- 1987: Start 2
- 1995: Vålerenga -2
- 2012: Odd -1
- 2015: Lillestrøm -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/nor-1/importar.py`; cada uma também aparece no relatório, na temporada.

- nenhuma

## 8. O que não deu para coletar

- **Jogos dos grupos da Norgesserien** (1937/38, 1938/39, 1947/48), fora o Distrito V, grupo B: nenhuma fonte em lote traz; ficam as tabelas publicadas.
- **Datas e rodadas de 1937/38 a 1960/61** (só as matrizes e as tabelas do mata-mata).
- **Autores dos gols e cartões** antes da ESPN, fora as páginas da RSSSF de 1999 a 2005.
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Norgesserien (1937/38, 1938/39, 1947/48): só um grupo por temporada tem os jogos (Distrito V, grupo B, na Wikipédia em norueguês); os outros ficam com a tabela publicada.
- Sem datas e rodadas até 1960/61 (só matrizes e tabelas do mata-mata). Autores dos gols e cartões só com a ESPN (2008-2025) e, para os gols, com as páginas da RSSSF (1999-2003 e 2005); antes, nenhuma fonte em lote.
- Fora do escopo (decisão do Guilherme, 25/11/2026): Prøveligaen de 1914-16, 1939/40 (interrompida) e a copa (fase 2); 2026 entra quando a temporada terminar.

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade: clube e departamento de futebol com artigos separados na Wikipédia como um clube só (Vålerengens IF e Vålerenga Fotball, como a RSSSF; Mjøndalen, Sogndal, Ranheim, Strømsgodset, Kongsvinger, Lyn); refundados à parte (Sarpsborg FK x Sarpsborg 08, Kristiansund FK x BK, Sandefjord BK x Sandefjord Fotball, que o ogol junta num código).
- Norgesserien: classificação pelo mata-mata e depois pela posição no grupo, com os números da tabela do grupo; jogos extras do mata-mata sem o mando (a Wikipédia não diz).
- 1987: o vencedor dos pênaltis de Molde x Lillestrøm (0-0) saiu da contagem da tabela da Wikipédia (o placar dos pênaltis não está nas fontes).

## 10. Arquivos

- Código: `coleta/nor-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_nor.py`.
- Fontes baixadas: `data/coleta/nor-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-nor-1/`.
- Pacote: `data/coleta/nor-1/pacote/`; relatório: `docs/coleta/nor-1.md`.
- Refazer do zero: `python coleta/nor-1/baixar.py ...` (ver o docstring), `python coleta/nor-1/importar.py`, `python coleta/comum-europa/testar_carga.py nor-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

