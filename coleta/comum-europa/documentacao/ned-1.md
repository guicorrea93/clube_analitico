# Campeonato Holandês (`ned-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ned-1/pacote/` e do importador `coleta/ned-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ned-1.md`.

## 1. O que temos

- **Edições:** 70, de 1956/57 a 2025/26.
- **Jogos:** 21082; **gols:** 64928; **gols com autor:** 23019 (35%); **cartões:** 24431; **jogos com estatísticas** (chutes, faltas, escanteios): 2680.
- **Clubes:** 54; **artilheiros:** 70 temporadas com artilheiro (78 linhas, com empates).
- **Classificação final:** 70 temporadas; **rodada a rodada:** 70 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2504 linhas, de 140 tabelas.
- **Observação da competição:** Eredivisie, desde a criação (1956/57). Não inclui os campeonatos holandeses de antes (ligas regionais com fase final, 1888/89-1953/54, e a Hoofdklasse profissional de 1954/55 e 1955/56) nem os play-offs de vaga europeia e de rebaixamento (nacompetitie). 2019/20 foi cancelada pela covid-19, sem campeão.

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1956/57-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar (só os jogos de rodada: os play-offs da mesma edição ficam de fora); base de 2025/26, que o engsoccerdata não traz; calendários guardados em `data/cache/ogol-ned-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);
- ESPN (liga `ned.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: matriz de resultados e tabela final de 1956/57 a 2003/04 (conferência jogo a jogo), tabela final das temporadas seguintes, lista de campeões e de artilheiros (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Amsterdã). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (inclui quem caiu na nacompetitie). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 18, saldo de gols em 52, média de gols em 0); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 140 tabelas fecham com os jogos e 0 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: nenhuma.
- Temporadas com número de jogos diferente do turno e returno completo: 2019/20 (232 de 306).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 1224 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2796 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3060 | 100% | 90% | 100% | 90% | 85% | 0% | 0% | 89% | 2.8 |
| 2010s | 2986 | 100% | 100% | 100% | 100% | 100% | 0% | 28% | 99% | 3.4 |
| 2020s | 1836 | 100% | 100% | 100% | 100% | 81% | 0% | 100% | 100% | 3.1 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1956/57 a 1961/62: 18 clubes
- 1962/63 a 1965/66: 16 clubes
- 1966/67 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1956/57 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1956/57 a 2025/26: Eredivisie

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols, gols pró: 52 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 18 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 2010/11: punições: NAC Breda -1 pontos
- 2014/15: punições: Twente -6 pontos
- 2015/16: punições: Twente -3 pontos
- 2019/20: título não atribuído; temporada cancelada em abril de 2020 pela pandemia de covid-19, depois de 25 ou 26 rodadas (232 de 306 jogos): sem campeão, sem rebaixamento e sem acesso; a classificação é a do momento da parada
- 2023/24: punições: Vitesse -18 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Ajax: 28
- PSV: 24
- Feyenoord: 11
- AZ Alkmaar: 2
- DOS Utrecht: 1
- Sparta Rotterdam: 1
- DWS Amsterdam: 1
- Twente: 1
- Sem campeão: 2019/20

**Rebaixamentos:** 154 no total; quem mais caiu: Volendam (11), Excelsior Rotterdam (9), De Graafschap (9), Willem II (8), VVV-Venlo (8).

**Punições em pontos:**

- 2010/11: NAC Breda -1
- 2014/15: Twente -6
- 2015/16: Twente -3
- 2023/24: Vitesse -18

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ned-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1969/70 · Sparta Rotterdam · ADO Den Haag:** [1, 2] a base traz 1-3; o ogol e a matriz da RSSSF trazem 1-2, e as tabelas da RSSSF e da Wikipédia só fecham com 1-2
- **1999/00 · Heerenveen · Willem II:** [2, 4] a base traz 2-3; o football-data e a matriz da RSSSF trazem 2-4, e as tabelas da RSSSF e da Wikipédia só fecham com 2-4

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1964/65 · SC Enschede:** fundiu-se com o Enschedese Boys no FC Twente (1965), que ficou com o lugar na Eredivisie
- **1967/68 · Fortuna '54:** fundiu-se com o Sittardia no Fortuna SC (1968), que ficou com o lugar na Eredivisie; ninguém caiu em 1967/68 (Wikipédia)
- **1967/68 · Sittardia:** fundiu-se com o Fortuna '54 no Fortuna SC (1968); ninguém caiu em 1967/68 (Wikipédia)
- **1967/68 · Xerxes:** o Xerxes/DHC faliu ao fim da temporada; ninguém caiu em 1967/68 (Wikipédia)
- **1969/70 · DOS Utrecht:** fundiu-se com o Elinkwijk e o Velox no FC Utrecht (1970), que ficou com o lugar na Eredivisie
- **1970/71 · Holland Sport:** fundiu-se com o ADO no FC Den Haag (1971), que ficou com o lugar na Eredivisie
- **1971/72 · DWS Amsterdam:** fundiu-se com o Blauw-Wit e o De Volewijckers no FC Amsterdam (1972), que ficou com o lugar na Eredivisie
- **1990/91 · SVV Schiedam:** fundiu-se com o Dordrecht '90 (SVV/Dordrecht '90, 1991), que ficou com o lugar na Eredivisie

### Temporadas interrompidas (`INTERROMPIDAS`)

- **2019/20:** cancelada em abril de 2020 pela pandemia de covid-19, depois de 25 ou 26 rodadas (232 de 306 jogos): sem campeão, sem rebaixamento e sem acesso; a classificação é a do momento da parada

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1957/58:** o título foi decidido num jogo extra (DOS e Ajax empatados em pontos), e o último lugar também (Elinkwijk 2-1 GVAV, em campo neutro): os jogos extras ficam de fora, como os play-offs; a ordem é a oficial (Wikipédia)
- **1959/60:** o título foi decidido num jogo extra (Ajax 5-1 Feyenoord, empatados em pontos): fica de fora, como os play-offs; a ordem é a oficial (Wikipédia)

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Nacompetitie e play-offs de vaga europeia:** ficam de fora (entram com a 2ª divisão e as copas).
- **Campeonatos de antes da Eredivisie (1888/89-1955/56):** ficam de fora, à espera de decisão do Guilherme.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências e próximos passos

- Campeonatos holandeses de antes da Eredivisie (1888/89-1955/56: ligas regionais com fase final e a Hoofdklasse profissional): ficaram de fora; incluir é decisão do Guilherme (o ogol tem os calendários desde 1888/89).
- Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor; vale a revisão conferir.

## 10. Arquivos

- Código: `coleta/ned-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_ned.py`.
- Fontes baixadas: `data/coleta/ned-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ned-1/`.
- Pacote: `data/coleta/ned-1/pacote/`; relatório: `docs/coleta/ned-1.md`.
- Refazer do zero: `python coleta/ned-1/baixar.py ...` (ver o docstring), `python coleta/ned-1/importar.py`, `python coleta/comum-europa/testar_carga.py ned-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

