# Campeonato Alemão (`ger-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ger-1/pacote/` e do importador `coleta/ger-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ger-1.md`.

## 1. O que temos

- **Edições:** 63, de 1963/64 a 2025/26.
- **Jogos:** 19220; **gols:** 58983; **gols com autor:** 22512 (38%); **cartões:** 30251; **jogos com estatísticas** (chutes, faltas, escanteios): 7649.
- **Clubes:** 58; **artilheiros:** 63 temporadas com artilheiro (74 linhas, com empates).
- **Classificação final:** 63 temporadas; **rodada a rodada:** 63 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2264 linhas, de 126 tabelas.
- **Observação da competição:** Bundesliga, desde a criação (1963/64). Não inclui os campeonatos alemães de antes (1902/03-1962/63: ligas regionais e fase final), os da Alemanha Oriental (DDR-Oberliga) nem os play-offs de rebaixamento (Relegation) contra clubes da 2. Bundesliga.

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1963/64-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-ger-1/` para os escudos;
- ESPN (liga `ger.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: tabela final de cada temporada e lista de artilheiros de cada temporada (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista de campeões (com os gols do artilheiro).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Berlim). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 13, saldo de gols em 47, média de gols em 3); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 123 tabelas fecham com os jogos e 3 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: 1969/70, 1979/80, 1993/94.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 2010 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3134 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3060 | 100% | 90% | 100% | 90% | 72% | 20% | 90% | 89% | 3.6 |
| 2010s | 3060 | 100% | 100% | 100% | 100% | 97% | 0% | 100% | 99% | 3.8 |
| 2020s | 1836 | 100% | 100% | 100% | 100% | 84% | 0% | 100% | 100% | 4.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1963/64 a 1964/65: 16 clubes
- 1965/66 a 1990/91: 18 clubes
- 1991/92: 20 clubes
- 1992/93 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1963/64 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1963/64 a 2025/26: Bundesliga

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols, gols pró: 47 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 13 temporadas
- pontos, média de gols (goal average): 3 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1993/94: punições: Dynamo Dresden -4 pontos
- 1999/00: punições: Eintracht Frankfurt -2 pontos
- 2003/04: punições: Kaiserslautern -3 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Bayern de Munique: 34
- Borussia Mönchengladbach: 5
- Borussia Dortmund: 5
- Werder Bremen: 4
- Hamburgo: 3
- Stuttgart: 3
- Colônia: 2
- Kaiserslautern: 2
- 1860 Munique: 1
- Eintracht Braunschweig: 1
- Nuremberg: 1
- Wolfsburg: 1
- Bayer Leverkusen: 1

**Rebaixamentos:** 157 no total; quem mais caiu: Nuremberg (9), Arminia Bielefeld (8), Hertha Berlin (7), Bochum (7), Colônia (7).

**Punições em pontos:**

- 1993/94: Dynamo Dresden -4
- 1999/00: Eintracht Frankfurt -2
- 2003/04: Kaiserslautern -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ger-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1965/66:** Lothar Emmerich (Dortmund) foi o artilheiro com 31 gols (RSSSF); a lista de campeões da Wikipédia traz 26, que são os gols do 2º colocado
- **1969/70:** a tabela da RSSSF dá ao Bayern uma vitória a mais e ao Rot-Weiß Oberhausen um empate a menos (com 2 gols a menos para o Oberhausen e 2 gols sofridos a menos para o Bayern); a base, o ogol e a tabela da Wikipédia concordam com os jogos: erro da RSSSF
- **1979/80:** a tabela da Wikipédia troca as linhas de Stuttgart e Kaiserslautern (os dois com 41 pontos e 75-53 de gols); a da RSSSF fecha com os jogos e dá a ordem
- **1991/92:** a base para em 25/04/1992 (faltam as 4 últimas rodadas da temporada de 20 clubes, depois da reunificação): os 40 jogos entram pelo ogol, e as tabelas da RSSSF e da Wikipédia fecham com o conjunto
- **1993/94:** Dynamo Dresden: 4 pontos a menos (licença); a Wikipédia desconta, a tabela da RSSSF não

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Play-offs de rebaixamento (Relegation) contra clubes da 2. Bundesliga:** ficam de fora (entram com a 2ª divisão).
- **Campeonatos alemães de 1902/03 a 1962/63** (ligas regionais e fase final) e a **DDR-Oberliga**: ficam para depois.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Campeonato alemão antes da Bundesliga (1902/03 a 1962/63: ligas regionais e fase final): ficou de fora; seria outra competição ou uma decisão do Guilherme.

## 10. Arquivos

- Código: `coleta/ger-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_ger.py`.
- Fontes baixadas: `data/coleta/ger-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ger-1/`.
- Pacote: `data/coleta/ger-1/pacote/`; relatório: `docs/coleta/ger-1.md`.
- Refazer do zero: `python coleta/ger-1/baixar.py ...` (ver o docstring), `python coleta/ger-1/importar.py`, `python coleta/comum-europa/testar_carga.py ger-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

