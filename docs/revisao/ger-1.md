# Revisão — Campeonato Alemão (`ger-1`)

Revisão profunda (3ª rodada), 22/11/2026. Prefixo dos achados: **DE**.

**Resumo:**
- Campeões, vices, rebaixados e todos os 19.220 placares estão certos. Conferidos com o transfermarkt (todos os jogos) e
  com a Wikipédia de (17.962 jogos), fontes que a coleta não usou.
- Os erros que há são de grau médio:
  - 102 datas erradas de 1963/64 a 1990/91, 24 delas impossíveis;
  - critério de desempate errado em 15 temporadas, que bagunça a Corrida;
  - o Arminia 1971/72 com 19 pontos, quando a DFB tirou todos.
- Achados: 0 alta, 3 média, 13 baixa e 2 "não é erro". O site ainda não tem 2025/26 (banco e painel local têm).
  Pendente o Guilherme decidir se entra o Alemão de antes da Bundesliga (DE-D1).

Arquivos:
- achados: `SCRATCH/achados_DE.csv`;
- fontes: `SCRATCH/fontes_DE.md`;
- decisões: `SCRATCH/decisoes_DE.md`;
- plano: `SCRATCH/plano_DE.md`;
- scripts e saídas: `revisao/DE/`;
- páginas baixadas: `data/cache/revisao/DE/`.

## Seção 1 da ficha: pacote x banco x painel x site

- Pacote = banco, nas 63 edições:
  - 19.220 jogos, 58.983 gols, 22.512 gols com autor, 30.251 cartões;
  - 1.132 linhas de classificação final e 38.440 de classificação por rodada;
  - 74 artilheiros.
- Os placares, datas, rodadas, posições, pontos e situação são iguais, jogo a jogo e linha a linha.
- `painel/dados/ger-1.js` local tem as 63 edições: pódios e tabelas iguais ao pacote.
- O site (https://clubeanalitico.pages.dev/dados/ger-1.js) tem **62** edições (até 2024/25). Os 62 pódios e tabelas são
  iguais aos do pacote. Falta publicar a 2025/26 (**DE-015**).

## A. Edições e títulos

- **Conferido:** as 63 edições, com campeão, vice e rebaixados, contra a Wikipédia de (tabela e legenda "Abstieg" de cada
  temporada, mais a seção Relegation nas recentes) e a lista de campeões da RSSSF.
- **Resultado:** 63 de 63 campeões e vices certos. Os rebaixados estão certos nas 63 temporadas:
  - Relegation: o 16º perdeu e foi marcado rebaixado em 1982/83, 1984/85, 1990/91, 2008/09, 2011/12, 2018/19 e 2025/26;
    ganhou e ficou nas outras 21;
  - 1964/65: Hertha fora por licença;
  - 1991/92: 4 rebaixados;
  - 2025/26: Wolfsburg (0-0 e 1-2 no play-off), conferido na Wikipédia de.
- **Achados:**
  - **DE-006:** faltam as notas dos rebaixamentos fora de campo (Hertha 1964/65, Arminia 1971/72, Dresden 1994/95);
  - **DE-012:** o painel não diz nada da Relegation;
  - **DE-014:** a competição se chama "Campeonato Alemão", mas só tem os títulos da Bundesliga (ver DE-D1).
- **Fontes:**
  - https://de.wikipedia.org/wiki/Fußball-Bundesliga_1963/64 (e as outras 62);
  - https://www.rsssf.org/tablesd/duitchamp.html

## B. Classificação final

- **Conferido:** as 1.131 linhas da Abschlusstabelle da Wikipédia de, contra o pacote: posição, V, E, D, gols, pontos e
  pontos tirados (`Abzug`).
- **Resultado:** 1.129 iguais. As punições de 1993/94 (Dresden -4), 1999/00 (Frankfurt -2) e 2003/04 (Kaiserslautern -3)
  estão certas. Pontos por vitória (2 até 1994/95), 16, 18 e 20 clubes: certo.
- **Achados:**
  - **DE-001 (média):** Arminia 1971/72 com 19 pontos; a DFB tirou todos (Abzug=19);
  - **DE-013:** em 1979/80 Stuttgart e Kaiserslautern dividem o 3º lugar;
  - **DE-002 (média):** o critério de desempate gravado é "confronto direto" em 13 temporadas e "saldo" em 1964/65 e
    1967/68. O regulamento era quociente de gols até 1968/69 e saldo depois. Isso ordena errado a classificação rodada a
    rodada: 1.555 posições da Corrida em 15 temporadas (`revisao/DE/rodada_criterio_saida.txt`). A ordem final não muda;
  - **DE-007:** 8 observações em inglês, e "S04" sem sentido, em `classificacao_final.observacao`.
- **Fonte:** https://de.wikipedia.org/wiki/Fußball-Bundesliga_1971/72 (Abschlusstabelle).

## C. Jogos

- **Placares:**
  - 19.220 de 19.220 iguais ao transfermarkt (gesamtspielplan, todas as temporadas);
  - 17.962 de 17.962 iguais à Kreuztabelle da Wikipédia de (59 temporadas);
  - 10.341 casados com a RSSSF (1963/64–1998/99), sem diferença real.
- **Datas:**
  - 116 diferenças com o transfermarkt, todas antes de 1997/98, decididas pela RSSSF, pelo ogol e pela regra "um clube
    não joga duas vezes em 2 dias" (`revisao/DE/datas_triangulo.py`);
  - **DE-003 (média):** 102 datas erradas no pacote, 24 impossíveis. Exemplos:
    - 1974/75: a rodada 22 inteira está no mesmo dia da rodada 19;
    - 1977/78: rodada 10 em 01/09 (era 01/10);
    - 1982/83: rodada 8 em 01/09 (era 01/10);
    - 1970/71: RW Essen x Bayern em 13/03 (era 13/02).
  - **DE-004:** 3 datas em dúvida;
  - 11 datas em que o transfermarkt erra e o pacote está certo.
  - A varredura de tela achou 19 casos de "clube com 2 jogos no mesmo dia": são parte do DE-003.
- **Tribunal:** dos 7 jogos decididos pela DFB, só 2 estão marcados `awd` (os que o ogol traz como "DA").
  - **DE-005:** faltam a marca e o placar de campo em 1970/71, 1976/77, 1992/93, 1994/95 e 2010/11. O placar oficial
    está certo nos 5.
- **Não é erro:**
  - **DE-017:** o football-data de 1993/94 a 1996/97 traz a data da rodada, não a do jogo;
  - **DE-018:** as datas do ogol anotadas no relatório de 1972/73 e 1983/84 estão erradas; nas de 1977/78, 1982/83,
    1984/85 e 1990/91 o ogol estava certo, e elas entram no DE-003.
- **Amostra por década:**
  - transfermarkt: todos os jogos de todas as décadas;
  - footballdatabase.eu: 238 jogos em 10 temporadas (1963/64–1996/97), antes de ele bloquear. Ele repete datas erradas
    da base: não serve para datas.
- **Fontes:**
  - https://www.transfermarkt.com/bundesliga/gesamtspielplan/wettbewerb/L1/saison_id/1974
  - https://www.rsssf.org/tablesd/duit75.html

## D. Gols e artilheiros

- **Artilheiros:** 63 de 63 temporadas batem em gols e clube com a lista da Wikipédia de.
  - **DE-008:** 8 nomes no formato da RSSSF aparecem no site, como "AÍLTON Gonçalves da Silva" e "Harry Edward Kane".
- **Gols com autor:** nenhum jogo tem mais gols com autor que o placar.
  - **DE-010:** 36 jogos desde 2001/02 têm gols e nenhum autor (`revisao/DE/jogos_sem_autor.txt`).
  - **DE-009:** nomes da ESPN fora de ordem ou partidos, de 2001/02 a 2006/07 ("Goncalves da Silva Ailton" com 74 gols;
    "Jeronimo Baretto Cacau" e "Cacau"; lista em `revisao/DE/nomes_espn.txt`).
- **DE-011 (cobertura):** a ficha diz que nenhuma fonte em lote traz os autores antes de 2001/02. Mas as páginas da RSSSF
  que a coleta já baixou trazem autor e minuto em quase todos os jogos de 1963/64 a 1998/99. Um leitor simples fecha a
  soma com o placar em 7.678 de 9.660 jogos com gol.
- **Fonte:** https://de.wikipedia.org/wiki/Liste_der_Torschützenkönige_der_Fußball-Bundesliga

## E. Clubes e escudos

- **Conferido:** os 58 clubes, com nome, cidade, país, duplicados e homônimos no banco todo. Folha de contato com os 58
  escudos: `SCRATCH/DE/folha.png`.
- **Resultado:** tudo certo.
  - Nenhum duplicado nem homônimo.
  - As grafias de época estão juntas como devem: Meidericher SV = Duisburg, SV Bayer 04 = Bayer Leverkusen, Bayer 05 /
    KFC Uerdingen = Uerdingen.
  - Os 58 escudos estão certos, inclusive os de clubes extintos ou pequenos (Tasmania, Blau-Weiß 90, Neunkirchen,
    Homburg).
- Nenhum achado.

## F. Painel e site

- **Telas do site, no computador:** Pódio, Classificação 1971/72 e 1964/65, Participantes 1964/65, Corrida 1999/00 e
  Artilharia 2003/04. Sem erro nem tela quebrada. Os números batem com o banco. A maior goleada (Bayern 11 x 1 Dortmund,
  1971/72) está certa.
- **No celular:** a página fica mais larga que a tela (**DE-016**, já conhecido).
- **Site:** 62 edições contra as 63 do banco e do painel local (**DE-015**).
- **Prints:** `SCRATCH/DE/telas/`.

## Seções 8 e 9 da ficha: o que falta e como fazer

| Falta | Fonte | Custo | Risco |
|---|---|---|---|
| Autores dos gols de 1963/64 a 1998/99 | RSSSF `duitNN.html`, já baixada | médio (leitor) | baixo, gravando só quando a soma fecha |
| Autores de 1999/00 e 2000/01, e os 36 jogos sem autor | transfermarkt spielbericht, jogo a jogo | alto em tempo (~650 páginas); 36 é baixo | baixo |
| Público e estádio antes de 2001/02 | transfermarkt spielbericht (não conferido a fundo) | alto | médio |
| Relegation | Wikipédia de, seção de cada temporada | baixo | — (decisão DE-D2) |
| Alemão de 1902/03 a 1962/63 | RSSSF e Wikipédia de (fase final); footballdatabase.eu e RSSSF (Oberligas) | médio (fase final) ou alto (Oberligas) | — (decisão DE-D1) |
| DDR-Oberliga | RSSSF `ddrNN.html` | médio | ligar os clubes do Leste |

## Perguntas ao Guilherme

1. **DE-D1:** incluir o Campeonato Alemão de antes da Bundesliga?
   - Recomendo a fase final de 1902/03 a 1962/63, para a contagem de títulos ficar igual à da DFB (Nuremberg 9, Schalke 7).
   - A DDR-Oberliga, se entrar, à parte.
   - As Oberligas regionais, só se ele quiser ir até as regionais.
2. **DE-D2:** Relegation: só uma nota na edição (recomendado, como no ES-002) ou os jogos como fase?
3. **DE-D3:** 1979/80: manter Stuttgart 3º e Kaiserslautern 4º com uma nota (recomendado), ou os dois em 3º?
