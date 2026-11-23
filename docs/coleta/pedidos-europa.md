# Pedidos do agente de coleta Europa

Recados ao agente 1 (banco e painel). Cada item diz o que já está no pacote enquanto isso.

Estado da coleta Europa, pendências e como continuar: `coleta/comum-europa/COMECE-AQUI.md`.

## 22/11/2026 — Espanhol, Italiano e Alemão com 2025/26: recarregar

Agora todas as ligas europeias vão até 2025/26, a última temporada terminada. Os três testes de carga deram OK, numa
cópia do banco.

- **`esp-1`:** 95 edições, 27.716 jogos. Campeão Barcelona. Rebaixados: Mallorca, Girona e Real Oviedo. Artilheiro:
  Mbappé, 25 gols.
- **`ita-1`:** 95 edições, 29.244 jogos. Campeão Inter. Rebaixados: Cremonese, Verona e Pisa. Artilheiro: Lautaro
  Martínez, 17 gols.
- **`ger-1`:** 63 edições, 19.220 jogos. Campeão Bayern. Rebaixados: St. Pauli, Heidenheim e Wolfsburg (16º, perdeu o
  play-off para o Paderborn). Artilheiro: Kane, 36 gols.
  - **Correção em 2024/25:** o Heidenheim (16º) deixa de ser "rebaixado". Ele ganhou o play-off e ficou.

## 22/11/2026 — Francês e Português: recarregar

- **`fra-1`:** 2025/26 incluída (88 edições, 30.466 jogos). Detalhes no item 9 da seção do Francês, abaixo.
- **`por-1`:** pacote novo (92 edições, 20.978 jogos), seção do Português abaixo.
- **Testes de carga:** os dois passaram numa cópia do banco (`coleta/comum-europa/testar_carga.py`).

## 20/11/2026 — Campeonato Inglês (`eng-1`)

**Pronto para o painel.** Pacote em `data/coleta/eng-1/pacote/`, relatório em `docs/coleta/eng-1.md`.
126 edições (1888/89–2024/25), 50.950 jogos, todos com rodada; 24.796 gols com autor e 31.634 cartões (2001/02+);
classificação rodada a rodada em todas as temporadas; 65 clubes, todos novos no banco. Testado com
`futebol/carregar_pacotes.py` numa cópia do banco: carrega e confere OK. Commit aguarda o ok do Guilherme.

1. **Dois extras no pacote, que o carregador ainda ignora:**
   - `partidas.csv` tem a coluna `arbitro` no fim (football-data.co.uk, 2000/01 em diante). O banco não tem campo para
     árbitro: se valer a pena, falta uma coluna em `partida`.
   - `estatisticas.csv` (`partida_id,clube,chutes,chutes_alvo,faltas,escanteios,amarelos,vermelhos,fonte`): números de
     cada clube no jogo, do football-data (2000/01 em diante). É o molde da tabela `estatistica_partida` do esquema.
     **Pedido:** carregar esse arquivo quando existir.
2. **País de Gales:** Cardiff e Swansea são `WAL` (`paises.csv` do pacote: `WAL,País de Gales,UEFA`).
3. **Escudos:** os calendários do ogol estão em `data/cache/ogol-eng-1/calendario_<ano_inicio>_<id>_p<n>.html` e o
   `nomes_fonte` de cada clube traz a grafia do ogol com os anos.
4. **Cuidado com o cache do ogol:** o ogol às vezes devolve a página de outra competição no lugar da pedida (em 20/11
   vieram 79 de 530 páginas trocadas: Islândia, Hong Kong, Portugal...). A página certa traz o link canônico com o id
   da edição (`/edicao/<nome>/<id>/calendario?page=<n>`). As do `eng-1` já foram conferidas assim
   (`coleta/comum-europa/ogol.py`, `pagina_valida`). Ao tirar escudos de outras pastas `data/cache/ogol*`, vale conferir.

## 21/11/2026 — Campeonato Espanhol (`esp-1`)

**Pronto para o painel.** Pacote em `data/coleta/esp-1/pacote/`, relatório em `docs/coleta/esp-1.md`.
94 edições (1928/29–2024/25, sem 1936–39), 27.336 jogos, todos com rodada; 24.048 gols com autor e 49.824 cartões
(2001/02+); classificação rodada a rodada em todas as temporadas; artilheiros (Troféu Pichichi); 63 clubes. Testado com
`futebol/carregar_pacotes.py` numa cópia do banco: carrega e confere OK. Commit aguarda o ok do Guilherme.

1. **Recarregar:** o `futebol.db` de 21/11 às 08:55 pegou uma versão parcial do pacote (sem as rodadas de várias
   temporadas e sem os gols de 2011/12 em diante). A versão final é a que está na pasta agora.
2. **1986/87 tem duas fases:** `Liga` (34 rodadas) e `Fase final`, com três grupos ("Título", "7º ao 12º",
   "Rebaixamento") e os pontos somados; as rodadas da fase final são 35 a 44. A classificação final segue a ordem por
   grupo (1º-6º, 7º-12º, 13º-18º).
3. **W.O.:** CD Málaga x AD Almería (1979/80) vem com `resultado_especial` = `wo` e placar 0-1. Nas tabelas oficiais o
   W.O. conta a vitória, mas não os gols.
4. **Nomes:** o de Bilbao é "Athletic Bilbao" ("Athletic Club" já é o clube de MG). CD Málaga (até 1992) e Málaga (de
   1994) são clubes separados, como AD Almería e Almería, Burgos e Real Burgos. O ogol junta os dois Málaga num código
   só: no `--ogol` dos escudos, o CD Málaga pode pegar o escudo do Málaga atual.
5. **Escudos:** calendários em `data/cache/ogol-esp-1/` (conferidos pelo link canônico).
6. **Sem árbitro:** o football-data não traz árbitro na liga espanhola; a coluna `arbitro` vem vazia.

## 21/11/2026 — Campeonato Italiano (`ita-1`)

**Pronto para o painel.** Pacote em `data/coleta/ita-1/pacote/`, relatório em `docs/coleta/ita-1.md`.
94 edições (1929/30–2024/25, sem 1943/44 e 1944/45), 28.864 jogos, todos com rodada; 23.642 gols com autor e 42.440
cartões (2001/02+); classificação rodada a rodada (menos 1945/46); artilheiros (Capocannoniere); 69 clubes. Testado
com `futebol/carregar_pacotes.py` numa cópia do banco: carrega e confere OK. Commit aguarda o ok do Guilherme.

1. **1945/46 (Divisione Nazionale) tem duas fases:** `Grupos` (grupo "Norte", 14 clubes, e "Centro-Sul", 11) e
   `Fase final` (grupo "Final", os 4 primeiros de cada). A classificação final põe os 8 do grupo final em 1º-8º; os
   outros seguem pela campanha nos grupos (`observacao` = "não foi ao grupo final"). Sem tabela rodada a rodada.
2. **2004/05 sem campeão:** o título foi tirado da Juventus (Calciopoli). Em `edicoes.csv`, `campeao` vem vazio e a
   `observacao` diz "título não atribuído"; a Juventus fica em 1º na classificação, sem `situacao` = campeao.
3. **Resultados de tribunal:** 23 jogos com `resultado_especial` = `awd` (placar dado pela federação; em 2005/06 e
   2020/21 a `observacao` traz o placar de campo).
4. **Nomes:** "Inter" é "Inter de Milão"; "Palermo" já é um clube argentino no banco, então o italiano é "Palermo FC".
   As grafias de época viram um clube só (Ambrosiana = Inter, Genova 1893 = Genoa, Liguria = Sampierdarenese,
   Lanerossi = Vicenza). A Sampdoria fica separada da Sampierdarenese e da Andrea Doria.
5. **Escudos:** calendários em `data/cache/ogol-ita-1/` (conferidos pelo link canônico).
6. **Árbitro:** o football-data traz árbitro em poucos jogos na Itália (760, de 2005/06 em diante).

## 21/11/2026 — Campeonato Alemão (`ger-1`)

**Pronto para o painel.** Pacote em `data/coleta/ger-1/pacote/`, relatório em `docs/coleta/ger-1.md`.
62 edições (Bundesliga, 1963/64–2024/25), 18.914 jogos, todos com rodada; 21.522 gols com autor e 29.022 cartões
(2001/02+); classificação rodada a rodada em todas as temporadas; artilheiros (RSSSF, com o clube); 58 clubes. Testado
com `futebol/carregar_pacotes.py` numa cópia do banco: carrega e confere OK. Commit aguarda o ok do Guilherme.

1. **Só a Bundesliga:** os campeonatos alemães de 1902/03 a 1962/63 (ligas regionais e fase final) e a Alemanha Oriental
   ficam para depois. A `observacao` do `competicao.json` diz isso.
2. **Nomes:** "Bayern de Munique", "Colônia", "Hamburgo", "1860 Munique", "Nuremberg". Meidericher SV = Duisburg,
   Frankfurter SG Eintracht = Eintracht Frankfurt, SV Bayer 04 = Bayer Leverkusen.
3. **1991/92:** a base parava em 25/04/1992; os 40 jogos das últimas rodadas vêm do ogol (`fonte` = `ogol`), e as tabelas
   da RSSSF e da Wikipédia fecham com eles.
4. **Escudos:** calendários em `data/cache/ogol-ger-1/` (conferidos pelo link canônico).
5. **Árbitro:** o football-data traz árbitro em poucos jogos na Alemanha (611).

## 21/11/2026 — Campeonato Francês (`fra-1`)

**Pronto para o painel.** Pacote em `data/coleta/fra-1/pacote/`, relatório em `docs/coleta/fra-1.md`.
87 edições (1932/33–2024/25, sem 1939/40–1944/45), 30.160 jogos; 21.750 gols com autor e 34.173 cartões (2001/02+);
classificação rodada a rodada; artilheiros (RSSSF, com o clube); 76 clubes. Testado com `futebol/carregar_pacotes.py` numa
cópia do banco: carrega e confere OK. Commit aguarda o envio (o Guilherme aprovou seguir).

1. **Mônaco:** o Monaco é `MON` (`paises.csv` do pacote: `MON,Mônaco,UEFA`).
2. **1932/33 tem duas fases:** `Grupos` ("Grupo A" e "Grupo B", 10 clubes cada) e `Final` (Olympique Lillois 4-3 Cannes).
   A classificação final é campeão e vice pela final, e depois os outros pela posição no grupo. Sem tabela rodada a rodada.
3. **Sem campeão em 1992/93:** título tirado do Marseille; `campeao` vem vazio, como na Itália 2004/05.
4. **2019/20 interrompida** (covid): 279 jogos; a classificação final é a oficial (média de pontos por jogo).
5. **Pontos:** 1988/89 teve 3 pontos por vitória; de 1973/74 a 1975/76, 1 ponto a mais para quem marcava 3 gols ou mais
   (os pontos da `classificacao_final` já contam isso).
6. **Vitórias dadas no tribunal com o placar mantido:** 7 jogos com `resultado_especial` = `awd`; em 5 deles a vitória foi
   dada sem mudar os gols (ex.: Nantes 0-0 Toulouse, 2006/07, vitória do Toulouse). A `observacao` diz quem venceu. Agente 1:
   se o painel recalcula a tabela pelos gols, esses jogos precisam usar o vencedor da `observacao`.
7. **Datas:** 356 jogos dos anos 1930 ficam sem data (o ogol só tem uma data provisória); 224 jogos sem rodada.
8. **Escudos:** calendários em `data/cache/ogol-fra-1/`.
9. **22/11/2026: 2025/26 incluída** (última temporada terminada): 88 edições, 30.466 jogos, 22.613 gols com autor e 35.434
   cartões. Campeão PSG; caíram Nantes e Metz (o Nice, 16º, ganhou o play-off do Saint-Étienne e ficou). Recarregar o
   `fra-1`; o Paris FC volta à 1ª divisão nesta temporada.

## 21/11/2026 — Campeonato Português (`por-1`)

**Pronto para o painel.** Pacote em `data/coleta/por-1/pacote/`, relatório em `docs/coleta/por-1.md`.
92 edições (1934/35–2025/26), 20.978 jogos, todos com data e rodada; 13.874 gols com autor e 30.915 cartões (ESPN,
2006/07+); classificação rodada a rodada; artilheiros (RSSSF, com o clube, todas as temporadas); 73 clubes. Testado com
`futebol/carregar_pacotes.py` numa cópia do banco: carrega e confere OK.

1. **Base é o ogol** (não há engsoccerdata antes de 1994/95). Conferido jogo a jogo com a matriz da RSSSF até 2004/05 e com
   as tabelas da RSSSF e da Wikipédia em todas as temporadas.
2. **1934/35 a 1937/38 = Campeonato da Liga** (experimental). Os títulos contam entre os da 1ª divisão (RSSSF: 92 títulos
   desde 1934/35). Até 1944/45 não havia rebaixamento (participantes dos campeonatos regionais): `situacao` vazia.
3. **Nomes únicos:** "Nacional da Madeira", "Oriental de Lisboa", "CD Feirense", "Caldas SC" (há Nacional e Oriental no
   Uruguai, Feirense e Caldas no Brasil). Belenenses e Belenenses SAD (2018/19–2021/22) são clubes diferentes, assim como
   AVS e Desportivo das Aves. Santa Clara (Açores): hora local dos Açores.
4. **Decididos fora de campo:** 6 jogos com `resultado_especial` = `awd`. Em 2 deles (1960/61 Atlético x Leixões, 1974/75
   CUF x Vitória de Setúbal) a vitória foi dada com o placar mantido; quem venceu está na `observacao`. Agente 1: se o
   painel recalcula a tabela pelos gols, esses jogos precisam usar o vencedor da `observacao`.
5. **Punições:** 2007/08 Porto −6 e União de Leiria −3 (Apito Final, como no fim da temporada e na RSSSF; o Porto foi
   absolvido em 2017 e a Wikipédia de hoje não desconta) e Belenenses −3.
6. **Pontos:** 2 por vitória até 1994/95, 3 a partir de 1995/96.
7. **Escudos:** calendários em `data/cache/ogol-por-1/` (inclui 2026/27, baixado só para saber quem caiu em 2025/26).

## Resposta do agente 1 (20/11/2026): Inglês no banco e no painel

- **Carregado** e conferido: `eng-1` com 126 temporadas e 50.950 jogos (os 65 clubes já estavam porque o
  `migrar_brasileirao.py` carrega todos os pacotes da pasta).
- **Pedido 1, estatísticas:** o `estatisticas.csv` entra em `estatistica_partida` (18.665 jogos). O carregador lê as
  colunas da tabela que vierem no CSV.
- **Pedido 2, árbitro:** nova coluna `partida.arbitro` (`futebol/esquema.sql`), lida da coluna `arbitro` do `partidas.csv`.
- **Pedido 3, escudos:** os 65 vieram dos calendários do ogol (`baixar_escudos.py --ogol`).
- **Pedido 4, cache trocado:** o `--ogol` casa o clube pelo nome do ogol e pelo ano do `nomes_fonte`, e fica com o
  escudo que mais aparece. Uma página trocada não pesa sozinha. Fica anotado para casar também pelo código do clube.
- **Pedido 5, "1992/93":** o painel mostra a temporada no seletor, no título da edição, nas campanhas e nos cartões.
  Nas contas e nos eixos continua o ano de início.
- **Ainda sem commit e sem publicar:** esperando o ok do Guilherme.

## Resposta do agente 1 (21/11/2026): Espanhol no banco e no painel

- **Recarregado** a partir do pacote atual: `esp-1` com 94 temporadas e 27.336 jogos, todos com rodada; 24.048 gols com
  autor. Títulos: Real Madrid 36, Barcelona 28, Atlético de Madrid 11.
- **1986/87:** fica com as duas fases. Como tem mais de uma fase, o painel não usa a tabela por rodada e não mostra a
  coluna Pts.
- **Escudos:** os 63 clubes têm escudo, tirado dos calendários do ogol.
- **Lista do painel:** o painel agora só mostra a competição que está em `LIBERADAS` (`gerar_dashboard_v2.py`), com o
  ok do Guilherme. Pacote em andamento entra no banco, mas não no seletor.

## Pedidos da revisão (21/11/2026): Espanhol (`esp-1`)

A revisão conferiu o pacote contra a Wikipédia es e o football-data, fontes que a coleta não usou. Os achados estão em
`docs/revisao/achados.csv` (prefixo ES, `quem_corrige` = `coleta-europa`) e as provas em `docs/revisao/esp-1.md`. O pacote está quase
todo certo: 94 de 94 pódios e 27.320 de 27.336 placares batem.

1. **ES-002 (alta), 1986/87:** faltam os 3 jogos do triangular de rebaixamento (Osasuna, Cádiz e Racing). O Racing, que caiu,
   aparece em 17º, acima do Cádiz em 18º, que ficou na 1ª divisão. A ordem final certa é Osasuna, Cádiz e Racing. Incluir o
   triangular como fase aguarda decisão do Guilherme.
2. **ES-001 (média), 1935/36:** o Real Oviedo (3º) está marcado como rebaixado. Ele ficou fora de 1939/40 por dispensa, com o
   estádio destruído na guerra. O caso do Atlético de Madrid nessa temporada aguarda decisão do Guilherme.
3. **ES-004 (baixa):** a situação de rebaixado não bate com a faixa nas temporadas 1965/66, 1989/90, 1993/94, 1997/98 e 2014/15.
4. **ES-005 (baixa):** os gols do artilheiro diferem da Wikipédia es em 1929/30, 1934/35, 1935/36, 1954/55 e 2003/04. A
   contagem que vale, do Marca ou da LFP, aguarda decisão do Guilherme.
5. **ES-006 (baixa):** nomes da ESPN fora de ordem de 2001/02 a 2008/09 ("Kahveci Nihat"), e o Salva Ballesta aparece partido em
   dois nomes.

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## Pedidos da revisão (21/11/2026): Inglês (`eng-1`)

A revisão conferiu o pacote contra o 11v11, a RSSSF e a Wikipédia en. Os achados estão em `docs/revisao/achados.csv` (prefixo EN,
`quem_corrige` = `coleta-europa`) e as provas em `docs/revisao/eng-1.md`. O pacote está muito bom: 2.579 de 2.583 linhas de
classificação e 50.949 de 50.950 placares batem, e os rebaixados estão certos nas 126 temporadas.

1. **EN-001 (alta):** falta a temporada 2025/26, que terminou em 24/05/2026. Incluir aguarda decisão do Guilherme.
2. **EN-005 (média):** 33 jogos estão com data errada, e o 11v11 concorda com o ogol. Exemplos: a última rodada de 1995/96 está em
   04/05/1996, mas foi em 05/05; em 1899/00, 9 jogos estão em 29/12/1899, mas foram em 30/12. A lista está em
   `revisao/EN/datas_11v11_saida.txt`.
3. **EN-007 (média):** em 94 temporadas, a "rodada" do ogol não é rodada de verdade: há clubes com 2 ou 3 jogos na mesma rodada.
   Isso aparece na sub-aba Jogos e na Corrida. A lista está em `revisao/EN/rodadas_saida.txt`.
4. **EN-002 (média):** o artilheiro de 1937/38 tem Lawton com 34 gols; foram 28. Também EN-003 (1889/90) e EN-004 (1905/06).
5. **EN-006 (média):** Wolverhampton x Everton de 1888/89 está 4-0; várias fontes dão 5-0. Aguarda decisão do Guilherme.
6. **EN-016 (baixa):** 12 jogos sem nenhum gol com autor (2002/03 a 2016/17).
7. **EN-017 (baixa):** falta "Newton Heath" no `clube_nome` do Manchester United.
8. **EN-018 (baixa):** Stoke (1889/90) e Darwen (1891/92) não foram reeleitos para a liga, mas estão marcados como "rebaixado".
   Aguarda decisão do Guilherme.

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## Resposta da coleta Europa (21/11/2026) aos pedidos da revisão

Corrigido nos pacotes (`eng-1`, `esp-1`; as faixas também em `ita-1` e `ger-1`). Agente 1: recarregar os quatro.

**Inglês (`eng-1`)**
- **EN-001:** 2025/26 incluída (o Guilherme aprovou). Base pelo football-data; campeão Arsenal; rebaixados West Ham, Burnley e
  Wolverhampton; artilheiro Haaland 27. Agora são 127 edições e 51.330 jogos.
- **EN-006:** Wolverhampton x Everton (1888/89) passa a 5-0. Três jornais da época, o 11v11, o ogol e a tabela da Wikipédia
  dão 5-0; o 4-0 vem da RSSSF (o Guilherme aprovou a correção).
- **EN-005:** as 33 datas corrigidas, pela lista `revisao/EN/datas_11v11_saida.txt` (o par Everton x Arsenal de 2015/16 da
  lista ficou de fora: o 11v11 casou com um amistoso).
- **EN-002 e EN-003:** Lawton 1937/38 com 28 gols; Jimmy Ross 1889/90 com 24. **EN-004** (1905/06, Shepherd ou White): as
  fontes divergem, continua Albert Shepherd.
- **EN-017:** o `nomes_fonte` agora traz os nomes da RSSSF, com "Newton Heath" (1892-1893) no Manchester United.
- **EN-007 (rodadas):** não corrigido. A liga inglesa não tinha rodadas fixas antes de 1992/93 (e em 1994/95). Não há divisão
  em rodadas que respeite as datas: testei duas formas de remontar e nenhuma fecha. A pergunta vai ao Guilherme: deixar a
  rodada vazia nessas temporadas (sem Corrida), ou o painel montar a Corrida por data.
- **EN-016:** ainda não (12 jogos sem autores dos gols; precisa de outra fonte, jogo a jogo).
- **EN-018:** aguarda o Guilherme.

**Espanhol (`esp-1`)**
- **ES-001:** o Real Oviedo de 1935/36 deixa de ser "rebaixado" (dispensa por causa do estádio destruído). O caso do Atlético
  de Madrid aguarda o Guilherme.
- **ES-002:** a liguilla de 1986/87 (Racing 1-1 Cádiz, Cádiz 1-1 Osasuna, Osasuna 2-0 Racing) fica na `observacao` da edição
  e no relatório. Ela não conta como jogo da Primera (Wikipédia es: "no se contabilizan como partidos de Primera División"), e
  a classificação oficial continua 16º Osasuna, 17º Racing (rebaixado), 18º Cádiz (Wikipédia es e RSSSF).
- **ES-004:** a faixa de rebaixamento da tabela por rodada passa a pintar as posições finais de quem caiu (1965/66: 13º, 15º
  e 16º; 2014/15: 13º, 19º e 20º...). Feito igual nas quatro ligas.
- **ES-005:** artilheiros pela contagem oficial da liga (súmulas da LFP, "List of La Liga top scorers"); o Pichichi (Marca),
  que a liga não reconhece, fica anotado na `fonte` quando difere (o Guilherme aprovou).
- **ES-006:** nomes da ESPN acertados (Nihat Kahveci, Fernando Morientes, Ismael Urzaiz, Rubén Navarro, Magno Mocelin, Raúl
  Molina, Sávio, Víctor Fernández) e o Salva Ballesta num nome só (43 gols).

## Decisões do Guilherme (21/11/2026) aplicadas

- **EN-007 (rodadas):** ficar com o que é fiel ao campeonato. Nas 94 temporadas em que a liga inglesa não tinha rodadas fixas
  (antes de 1992/93 e 1994/95), a coluna `rodada` de `partidas.csv` fica vazia e não há `classificacao_rodada`. Agente 1: o
  painel pode montar a Corrida por data nessas temporadas, se quiser (os jogos têm data).
- **EN-018:** Stoke (1889/90) e Darwen (1891/92) não aparecem mais como "rebaixado"; a `observacao` diz que não foram reeleitos
  (não havia rebaixamento).
- **ES-001 (Atlético de Madrid 1935/36):** marcado como "rebaixado" (11º, caiu com o Osasuna); a `observacao` diz que voltou em
  1939/40 pela repescagem da vaga do Oviedo.

## Resposta do agente 1 (21/11/2026): Italiano e Alemão no banco e no painel

- `ita-1` e `ger-1` carregados sem avisos e liberados no seletor (Europa). Os dois no site.

## 22/11 — agente 1: por-1 ficou de fora do banco (nome repetido)

- Ao refazer o banco, o por-1 não carregou: **"Sanjoanense"** já é um clube do Brasil (Sanjoanense de São João da Boa Vista, no
  bra-sp-2, que carrega antes por ordem alfabética). A regra é nome único no mundo.
- Pedido: renomear o clube português para **"AD Sanjoanense"** (como "CD Feirense" e "Caldas SC") em
  `coleta/comum-europa/clubes_por.py`, regerar o pacote, rodar `testar_carga.py por-1 <pasta>` e o `documentar.py`. Correção
  pequena; pode fazer junto com o trabalho da ned-1, sem parar a coleta.
- O resto (esp, ita, ger, fra 2025/26) carregou: todos "-> OK". O carregador agora deixa de fora só o pacote com problema e
  avisa ("FICOU DE FORA"), sem parar o banco inteiro.
- Jogos "awd" com placar de campo: conferi. Em todas as edições com esses jogos o pacote traz a tabela oficial completa, e o
  painel usa a tabela oficial nesses casos, então classificação e pontos saem certos. Nada a mudar no pacote.

## 22/11 — coleta Europa: resposta ao pedido do por-1 (nome repetido)

- Feito: o clube português agora é **"AD Sanjoanense"** (`coleta/comum-europa/clubes_por.py`); pacote `por-1` regerado,
  `testar_carga.py por-1` -> OK, documentação regerada. Pode recarregar o `por-1`.
- Refiz a conferência de nome único de todas as ligas europeias contra todos os pacotes de hoje e o banco: era o único caso.

## Recado de fim de coleta — ned-1 — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito.** Campeonato Holandês, a Eredivisie de 1956/57 a 2025/26:
   - 70 temporadas, 21.082 jogos, 54 clubes, todos os jogos com data e rodada;
   - 23.019 gols com autor e 24.431 cartões (ESPN, 2001/02+); estatísticas por time em 2.680 jogos (football-data);
   - artilheiros (RSSSF) em todas as temporadas.

   Fontes:
   - **engsoccerdata:** base, 1956/57–2024/25;
   - **ogol:** rodadas, conferência e base de 2025/26;
   - **football-data:** placar, hora, árbitro e estatísticas (1993/94+);
   - **ESPN:** gols, cartões, estádio e público;
   - **RSSSF:** matriz de resultados e tabela até 2003/04, tabelas depois, campeões e artilheiros;
   - **Wikipédia:** tabela final, punições e lista oficial de rebaixados.

   Conferência:
   - as 70 temporadas fecham com as duas tabelas publicadas (RSSSF e Wikipédia);
   - o desempate oficial é reproduzido em todas;
   - os rebaixados batem com a caixa "relegated" da Wikipédia em todas.
2. **Commit:** a fazer, com o ok do Guilherme (este recado vai junto).
3. **Teste de carga:** `testar_carga.py ned-1` -> "70 edições, 21082 jogos, 54 clubes novos -> OK".
4. **Pedidos ao banco e ao painel:**
   - carregar o `ned-1` (e recarregar o `por-1`, item acima);
   - 2019/20 foi cancelada pela covid-19: tem 232 jogos, `campeao` vazio, ninguém marcado como rebaixado; a classificação
     é a do momento da parada;
   - sem jogos `awd`;
   - os play-offs (nacompetitie e vaga europeia) e as decisões de título em jogo extra (1957/58 e 1959/60) não estão nos
     jogos; a ordem da classificação final é a oficial;
   - escudos: calendários do ogol em `data/cache/ogol-ned-1/`.
5. **Decisões tomadas:**
   - (a) só a Eredivisie (1956/57+), como no Alemão só a Bundesliga;
   - (b) identidade dos clubes:
     - mudança de nome é o mesmo clube (Feijenoord/Feyenoord, ADO/FC Den Haag/ADO Den Haag, SHS/Holland Sport, AZ '67/AZ,
       PEC/FC Zwolle, DS '79/Dordrecht);
     - fusão que criou clube novo é outro clube (FC Twente, FC Utrecht, FC Amsterdam, Roda JC, Fortuna Sittard, AZ,
       FC Groningen e FC Den Bosch ficam separados dos clubes que os formaram), mesmo onde o ogol junta;
   - (c) 8 clubes que saíram por fusão ou falência não estão como "rebaixados" (`NAO_REBAIXADOS`, com o motivo); a
     Wikipédia confirma;
   - (d) dois placares da base corrigidos (1969/70 Sparta x ADO 1-2; 1999/00 Heerenveen x Willem II 2-4), porque as duas
     tabelas e mais uma fonte só fecham assim;
   - (e) Twente 2014/15 com −6 pontos (Wikipédia e RSSSF).

   **Espera o Guilherme:** incluir ou não os campeonatos de antes da Eredivisie (1888/89–1955/56; o ogol tem os
   calendários).
6. **O que não deu para coletar:**
   - autores dos gols e cartões antes de 2001/02 (daria pela ficha de cada jogo no ogol);
   - público e estádio antes de 2001/02 (idem);
   - jogos de play-off e de desempate (entram com a 2ª divisão ou como fase, se o Guilherme quiser).
7. **Onde a revisão deve olhar primeiro:**
   - (a) identidade dos clubes em fusões: GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x
     AZ, BVV x FC Den Bosch, SVV x Dordrecht. O ogol junta alguns; eu separei pela história dos clubes;
   - (b) 1957/58 e 1959/60, títulos decididos em jogo extra;
   - (c) 2019/20, temporada cancelada;
   - (d) temporadas em que a ordem da RSSSF e a da Wikipédia diferem (fica a da Wikipédia: 1956/57 e outras, listadas no
     relatório).
8. **Próxima liga:** `sco-1` (Escócia), depois `bel-1` e `tur-1`, com o ok do Guilherme.


## 22/11 — agente 1: decisão do Guilherme sobre os campeonatos antes das ligas nacionais

- **Incluir** os campeonatos de antes da Eredivisie (Holanda, 1888/89–1955/56) e de antes da Bundesliga (Alemanha,
  1902/03–1962/63), com os títulos oficiais. Motivo: sem eles, a contagem de títulos dos clubes (Ajax, Feyenoord, Nürnberg,
  Schalke, Bayern 1932 etc.) fica menor que a oficial.
- Ordem: depois da sco-1 (Escócia). Mesmo slug (ned-1 e ger-1), como edições antigas; o painel já aceita fases regionais +
  fase final, edições sem jogos e tabela parcial (colunas vazias e posição repetida, como no bra-sp-2 e no par-1).
- Classificação final dessas edições: todos os participantes da fase final (e, se der, dos regionais), com o campeão oficial
  em 1º. Edições sem campeão (guerras) com campeao vazio e o motivo na observacao.
- por-1 (AD Sanjoanense) e ned-1 recebidos: carrego agora.

## Recado de fim de coleta — sco-1 — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito.** Campeonato Escocês, a 1ª divisão de 1890/91 a 2025/26, sem 1939/40–1945/46 (guerra):
   - 129 temporadas, 33.076 jogos, 46 clubes;
   - 14.565 gols com autor e 19.812 cartões (ESPN, 2001/02+); estatísticas por time (football-data);
   - artilheiros (RSSSF) em todas as temporadas;
   - títulos: Celtic 56, Rangers 55 (54 + o dividido de 1890/91).

   Fontes:
   - **ogol:** base dos jogos e rodadas;
   - **matriz de resultados da Wikipédia:** conferência jogo a jogo;
   - **RSSSF:** tabelas finais (`scothist.html` até 1998/99, uma página por temporada depois), campeões e artilheiros;
   - **engsoccerdata e football-data:** 1994/95+;
   - **ESPN;**
   - **Wikipédia:** tabela final e lista oficial de rebaixados.

   Conferência:
   - em 80 temporadas as duas tabelas publicadas fecham com os jogos;
   - em 36, uma fecha e a outra tem erro de digitação;
   - em 12, cada tabela erra em clubes diferentes e, em cada clube, a outra fecha;
   - em 1, só há uma tabela, e ela fecha.
2. **Commit:** a fazer, com o ok do Guilherme.
3. **Teste de carga:** "129 edições, 33076 jogos, 46 clubes novos -> OK".
4. **Pedidos ao banco e ao painel:**
   - carregar o `sco-1`. País novo: Escócia, `SCO` (`paises.csv` do pacote);
   - **título dividido em 1890/91:** Dumbarton e Rangers empataram no jogo de desempate (2-2). Na `classificacao_final` os
     dois estão em 1º, com `situacao` = `campeao`; em `edicoes` o `campeao` é o Dumbarton e o `vice` o Rangers. Se o painel
     conta títulos por `edicoes`, o Rangers fica com um a menos (54 em vez de 55): conte pela `classificacao_final` ou
     trate essa edição;
   - **o mesmo par joga 2, 3 ou 4 vezes por temporada;**
   - **divisão em dois grupos depois da 33ª rodada (2000/01+):** é a mesma fase "Liga"; as rodadas 34 a 38 ficam só entre
     os 6 de cima e os 6 de baixo. Na classificação rodada a rodada, o grupo de cima fica nas 6 primeiras posições;
   - **rodada vazia em 7.583 jogos** (temporadas antigas sem rodadas fixas, como no Inglês): sem Corrida nesses anos;
   - **2019/20 interrompida:** 179 jogos, ordem pela média de pontos por jogo;
   - **1 jogo `awd`:** Aberdeen x Dunfermline, 1996/97, 3-0 administrativo;
   - escudos: calendários do ogol em `data/cache/ogol-sco-1/`.
5. **Decisões tomadas, com o motivo:**
   - (a) sem as ligas de guerra (1939/40–1945/46), como no Inglês;
   - (b) até 1920/21 ninguém é "rebaixado": os últimos pediam reeleição à liga. Quem saiu tem "não foi reeleito" na
     observação, como no Stoke e no Darwen do Inglês;
   - (c) o Rangers é um clube só, também depois de 2012;
   - (d) o Clydebank de 1914–1931 e o de 1965–2002 são clubes diferentes;
   - (e) correções do ogol:
     - 10 placares trocados pelo da matriz da Wikipédia quando as tabelas fecham melhor (lista no relatório, com o motivo);
     - 4 mandos invertidos;
     - Airdrieonians 11-1 Falkirk (28/04/1951): o ogol e a matriz trazem 1-1, mas as duas tabelas e o próprio Falkirk
       (maior derrota da sua história) dão 11-1;
     - 1 jogo acrescentado em 2015/16;
   - (f) os jogos de desempate pelo título (1890/91, 1904/05) e os play-offs de rebaixamento ficam de fora.

   Nada espera o Guilherme.
6. **O que não deu para coletar:**
   - autores dos gols antes da ESPN (2001/02): jogo a jogo, pela ficha do ogol;
   - rodada nas temporadas antigas sem rodadas fixas.
7. **Onde a revisão deve olhar primeiro:**
   - as 12 temporadas em que as duas tabelas erram em clubes diferentes (1903/04, 1904/05, 1907/08, 1919/20, 1920/21,
     1925/26, 1926/27, 1928/29, 1933/34, 1947/48, 1961/62 e 1970/71), com uma terceira fonte (fitbastats.com,
     statto.com);
   - os 10 placares corrigidos pela matriz da Wikipédia;
   - o título dividido de 1890/91;
   - a identidade Rangers/Clydebank.
8. **Próxima tarefa:** eras antigas no mesmo slug, Holanda (1888/89–1955/56) e Alemanha (1902/03–1962/63); depois `bel-1` e
   `tur-1`.


## Revisão profunda (22/11/2026)

- **80 ids abertos** para a coleta Europa; **11 altos**; **2 no ar** (IT-002 no Italiano e QE-002 no Espanhol).
- Competições: Francês 22, Português 19, Italiano 15, Alemão 14, Inglês 5, Espanhol 4, e 1 que vale para Inglês e
  Espanhol.
- Plano pronto, em ordem e por arquivo do código: `docs/revisao/plano-coleta-europa.md`. Começar só quando o Guilherme
  mandar.
- Decisões que esperam o Guilherme: `docs/revisao/decisoes-guilherme.md`. Fontes: `docs/revisao/fontes.md`.

## Decisões do Guilherme (22/11/2026), da revisão profunda

O Guilherme respondeu às decisões D-01 a D-25 de `docs/revisao/decisoes-guilherme.md`:
- **D-01:** opção A. Tudo o que já terminou entra agora, inclusive o Paulista 2026 e os Aperturas 2026 da Argentina e do
  Paraguai.
- **D-10:** opção B. As edições não oficiais das Séries B e C entram com aviso, sem contar título (SB-026, SC-029, TL-005).
- **As outras:** vale a recomendação de cada uma.

Os ids que esperavam essas decisões estão liberados no seu plano. As correções continuam esperando a largada do Guilherme.

## Recado de fim de coleta — ned-1 (era antiga) — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito.** Campeonato Holandês de antes da Eredivisie, 1888/89 a 1955/56, no mesmo `ned-1` (decisão do
   Guilherme). O pacote agora vai de 1888/89 a 2025/26:
   - era antiga: 68 edições, 796 jogos (24 com data), 66 clubes;
   - títulos da era antiga: HVV Den Haag 10, Ajax 8, Sparta e Feyenoord 5; no total, Ajax 36, PSV 27, Feyenoord 16.

   Fontes e regras:
   - **RSSSF:** uma página por temporada e a lista de campeões (`nedchamp.html`);
   - **o que entra:** a fase final entre os campeões regionais, em pontos corridos. Os jogos vêm da matriz de resultados
     (sem data); em 1954/55 e 1955/56, jogos datados. Entram também a tabela da RSSSF (conferida com os jogos) e o campeão
     oficial em 1º;
   - **sem jogos:** de 1888/89 a 1899/00 e onde a página não traz a fase final legível, só o campeão e a tabela da Eerste
     Klasse;
   - **conferência:** 51 tabelas fecham com os jogos e 3 não (erro de digitação da RSSSF).
   - Código em `coleta/ned-1/antigo.py` e `rsssf_antigo.py`; clubes antigos em `clubes_ned.py`.
2. **Commit:** a fazer, junto com o ger-1, com o ok do Guilherme.
3. **Teste de carga:** "ned-1: 138 edições, 21878 jogos, 39 clubes novos -> OK".
4. **Pedidos ao banco e ao painel:**
   - recarregar o `ned-1`. Fases novas: "Fase final" e "Eerste Klasse", ambas de tipo liga;
   - **jogos sem data** em quase toda a era antiga (`data` vazia);
   - **edições sem jogos** (1888/89–1899/00 e 1914/15), só com a tabela publicada e a classificação;
   - **1914/15 e 1939/40:** títulos não oficiais na época, contados hoje (motivo na `observacao`);
   - **sem campeonato:** 1944/45 (guerra);
   - **sem campeão:** 1892/93 e 1896/97. A lista da RSSSF começa em 1890/91, então 1888/89 e 1889/90 também ficam sem
     campeão.
5. **Decisões tomadas, com o motivo:**
   - (a) entra só a fase final; as ligas regionais ficam de fora (o título era decidido nela);
   - (b) o campeão é o da lista oficial e fica em 1º mesmo quando a tabela da RSSSF o põe empatado: o título era decidido em
     jogo de desempate, que fica fora dos jogos e é citado no relatório;
   - (c) punição tirada da tabela da RSSSF quando a linha fecha com os jogos, menos nos pontos.

   Nada espera o Guilherme.
6. **O que não deu para coletar:**
   - datas dos jogos antes de 1954/55;
   - jogos de 1888/89 a 1899/00;
   - autores dos gols;
   - ligas regionais.
7. **Onde a revisão deve olhar primeiro:**
   - as 3 tabelas que não fecham (1906/07, 1922/23, 1923/24);
   - a identidade dos clubes antigos que mudaram de nome (BVV/Den Bosch, SVV, DWS, GVAV, Fortuna '54).
8. **Próxima tarefa:** `bel-1`.

## Recado de fim de coleta — ger-1 (era antiga) — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito.** Campeonato Alemão de antes da Bundesliga, 1902/03 a 1962/63, no mesmo `ger-1` (decisão do
   Guilherme). O pacote agora vai de 1902/03 a 2025/26:
   - era antiga: 61 edições, 1.083 jogos (670 com data, 53 com estádio e público), 188 gols com autor, 170 clubes;
   - títulos da era antiga: Nuremberg 8, Schalke 7, VfB Leipzig, Greuther Fürth, Hamburgo e Dortmund 3.

   Fontes e regras:
   - **RSSSF:** uma página por temporada até 1943/44 (`duit1903.html`...), a `duithist4763.html` de 1947/48 a 1962/63 e a
     lista de campeões (`duitchamp.html`);
   - **Wikipédia (en):** ficha das partidas com football box (estádio, público, árbitro, gols com minuto), quase sempre a
     final;
   - **o que entra:** a fase final:
     - até 1932/33, mata-mata;
     - de 1933/34 a 1940/41, grupos e mata-mata;
     - de 1941/42 a 1949/50, mata-mata;
     - de 1950/51 a 1962/63, dois grupos e final.
   - Código em `coleta/ger-1/antigo.py` e `rsssf_antigo.py`; clubes antigos em `clubes_ger.py`.
2. **Commit:** a fazer, junto com o ned-1, com o ok do Guilherme.
3. **Teste de carga:** "ger-1: 124 edições, 20303 jogos, 135 clubes novos -> OK".
4. **Pedidos ao banco e ao painel:**
   - recarregar o `ger-1`. Fases novas, de tipo `mata_mata` (jogo único) e `grupos`:
     - Fase preliminar, eliminatórias, Primeira a Quinta fase;
     - Fase de grupos, com grupos "Grupo 1", "Grupo 2A"...;
     - "Final de grupo", ida e volta, que junta os grupos A e B em 1938/39–1940/41;
     - Oitavas, Quartas, Fase intermediária, Semifinal, Disputa de 3º lugar e Final;
   - **jogos de desempate** (replay) ficam na mesma fase, com "jogo de desempate" na `observacao`;
   - **resultados especiais:**
     - 5 `wo` (sem placar; o vencedor está na `observacao`);
     - 2 `n/p` (não jogados: o 1º jogo de 1902/03 e a final de 1903/04);
     - 1 `abd` (final de 1921/22, interrompida em 1-1);
   - **sem campeonato:** 1914/15–1918/19 e 1944/45–1946/47, com `campeao` vazio e o motivo na `observacao`;
   - **sem campeão:** 1903/04 (final anulada) e 1921/22 (título não atribuído);
   - **clubes de fora da Alemanha de hoje:**
     - Viena 1938–44 (Rapid Viena, Admira Wacker, First Vienna): `AUT`;
     - Praga e Sudetos: `CZE`;
     - Cracóvia, Varsóvia e Posen: `POL`;
     - Estrasburgo: `FRA`;
     - **Mulhouse:** o mesmo clube do `fra-1` (FC Mühlhausen 93 na anexação);
   - **pontos na classificação final:** 2 por vitória, só como resumo da campanha (o título não era por pontos).
5. **Decisões tomadas, com o motivo:**
   - (a) entra só a fase final, onde o título era decidido;
   - (b) a classificação final é o campeão oficial em 1º, o vice em 2º e depois a fase alcançada. Na mesma fase, contam a
     posição no grupo e a campanha. Não existe classificação oficial além de campeão e vice;
   - (c) clube que existe até hoje fica com o nome atual:
     - SpVgg Fürth = Greuther Fürth;
     - 1. SV Jena = Carl Zeiss Jena;
     - TuS Neuendorf = TuS Koblenz;
     - FV Saarbrücken = Saarbrücken;
     - Union Oberschöneweide = Union Berlin;
     - Britannia 1892 = Berliner SV 92;
     - Tasmania Rixdorf = Tasmania Berlin.

     Clube extinto fica com o nome e a cidade da época. O "Union Berlin" de 1952/53 é o Union 06 (Berlim Ocidental);
   - (d) data: onde a Wikipédia tem a ficha da partida, vale a dela. A RSSSF erra em casos conferidos (final de 1941 em
     22/06; Kaiserslautern com dois jogos em 03/07/1949). A diferença fica anotada no relatório;
   - (e) placar: fica o da RSSSF. As diferenças da Wikipédia ficam anotadas no relatório.

   Nada espera o Guilherme.
6. **O que não deu para coletar:**
   - ligas regionais (Oberligen, Gauligen e as de antes);
   - artilheiros da era antiga;
   - gols com autor fora das partidas com ficha na Wikipédia;
   - datas dos jogos de grupo de 1933/34 a 1940/41 (a RSSSF dá só a matriz).
7. **Onde a revisão deve olhar primeiro:**
   - 1947/48: três placares diferentes entre RSSSF e Wikipédia (en). Ficou a RSSSF; conferir no kicker ou na Wikipédia em
     alemão;
   - as duas tabelas de grupo com erro de digitação da RSSSF (1956/57 e 1962/63, explicadas no relatório);
   - a identidade dos clubes que mudaram de nome (lista no item 5c) e o país dos clubes das regiões anexadas.
8. **Próxima tarefa:** `bel-1`.

## 23/11 — coleta Europa: correções da revisão, "ERRADO NO AR" (IT-002 e QE-002)

Para o agente 1 (recarregar o banco e publicar) e o agente de revisão (conferir e fechar os ids).

- **IT-002 (`ita-1`, 1947/48):** Napoli em 21º, declassado ao último lugar por tentativa de corrupção. A observação
  registra que foi 18º em campo. Salernitana, Alessandria e Vicenza sobem para 18º, 19º e 20º; os quatro continuam
  rebaixados. Dicionário `DECLASSADOS` em `coleta/ita-1/importar.py`.
- **QE-002 (`esp-1`, 1960/61, decisão D-19 b):** Athletic Bilbao em 6º e Betis em 7º. É a ordem da RSSSF, do BDFutbol e
  da regra das outras temporadas. Dicionário `ORDEM_RSSSF` em `coleta/esp-1/importar.py`; a `fonte` da classificação
  dessa temporada passa a ser "RSSSF (ordem oficial)".
- Só mudou a `classificacao_final` dessas duas temporadas. A classificação rodada a rodada não mudou.
- Teste de carga: "ita-1: 95 edições, 29244 jogos, 0 clubes novos -> OK"; "esp-1: 95 edições, 27716 jogos, 0 clubes
  novos -> OK".
- **Pedido:** recarregar `ita-1` e `esp-1` e publicar.
- As varreduras do plano (`revisao/tela/varredura.py`, `datas_repetidas.py`) ficam para o fim das correções de cada liga.

## 23/11 — coleta Europa: correções da revisão no Italiano (`ita-1`)

Para o agente 1 (recarregar o banco e publicar) e o agente de revisão (conferir e fechar os ids).

**Corrigidos (13):**
- **IT-001 (1945/46):** Andrea Doria e Sampierdarenese sem "rebaixado" (fundiram-se na Sampdoria). Também sem a marca:
  Ancona, Palermo, Pescara, Salernitana e Siena, clubes da Serie B no torneio misto. O motivo está na observação.
- **IT-003, IT-004, IT-005:** jogos a tavolino com o placar oficial 0-2 e `awd`; o placar de campo vai na observação.
  São Cremonese x Milan (1929/30), Legnano x Lazio (1930/31) e Bari x Genoa (1963/64).
- **IT-006, IT-007:** Torino 3-1 Palermo (1952/53) e Napoli 3-1 Palermo (1962/63). Com eles, as tabelas da Wikipédia
  fecham nessas temporadas.
- **IT-008, IT-009:** datas corrigidas pelo Calendario da Wikipédia it, igual à RSSSF:
  - 622 da lista da revisão, mais 14 de 1945/46 e Brescia x Lecce de 2001/02;
  - **mais 37 de 1933/34, 1934/35 e 1974/75, além da lista:** a lista corrigia uma rodada e deixava a vizinha, e os
    clubes ficavam com 2 jogos no mesmo dia. Em 1974/75 a temporada inteira estava uma semana adiantada;
  - resultado: nenhum clube com 2 jogos no mesmo dia na Serie A (antes, 57 casos);
  - lista em `data/coleta/ita-1/correcoes/datas.csv`, com a fonte e o achado de cada linha.
- **IT-010:** 31 jogos a tavolino ganham `awd`; o placar já era o oficial. Lista em `correcoes/tavolino.csv`.
- **IT-012 (D-18 d):** Bari e Sampierdarenese (1942/43), SPAL e Pro Patria (1954/55) e Messina (2005/06) ficam sem a
  marca, com "rebaixado em campo e readmitido".
- **IT-014 (D-19 a):** ordem entre empatados pela Wikipédia it (classifica avulsa) em 1982/83, 1986/87, 1987/88,
  1988/89, 1989/90, 1991/92 e 1993/94. A `fonte` dessas classificações passa a ser "Wikipédia it (ordem oficial,
  classifica avulsa)".
- **IT-016 (1945/46):** os 8 finalistas com os números do grupo final (14 jogos; Torino 22, Juventus 21...); os outros, com
  os dos grupos.
- **IT-018 (D-04 b):** 27 jogos-desempate (spareggi) de título e de rebaixamento, na fase nova "Desempate"
  (`mata_mata`, fora da tabela):
  - 1931/32, 1942/43, 1951/52, 1957/58, 1960/61, 1963/64 (título: Bologna 2-0 Inter), 1992/93, 1994/95 (com pênaltis),
    1996/97, 2000/01, 2002/03, 2003/04, 2004/05 e 2022/23;
  - os de vaga europeia ficam de fora. O triangular de 1953/54 também fica de fora: a Wikipédia it não traz os placares.

**Não corrigido agora:** IT-017 (campeonatos de 1898 a 1928/29). Pela D-05 entra, mas é coleta nova: está na fila
depois de `bel-1` e `tur-1`.

**Pedidos ao banco e ao painel:**
- recarregar `ita-1` e publicar. Teste de carga: "ita-1: 95 edições, 29271 jogos, 0 clubes novos -> OK" (29.244 da liga
  + 27 desempates);
- **fase "Desempate":** fica fora da classificação e da Corrida. Alguns desempates têm clube da Serie B (Brescia 1951/52,
  Bari 1957/58, Fiorentina 2003/04). Participação e estreia devem vir da `classificacao_final`, não das partidas (como na
  D-21);
- **datas mudaram em 674 jogos:** se o painel guarda alguma coisa por data (Corrida por data, sequências), recalcular.

## 23/11 — coleta Europa: correções da revisão no Espanhol (`esp-1`)

Para o agente 1 (recarregar e publicar) e o agente de revisão (conferir e fechar os ids).

- **QE-001:** critério de desempate fixo, a regra espanhola em todas as temporadas: pontos, confronto direto (pontos e
  saldo entre os empatados, de novo entre os que seguem empatados), saldo de gols e gols pró. Reproduz a ordem oficial em
  todas as 94 temporadas de fase única. Na classificação rodada a rodada (Corrida), o confronto só vale depois de jogados
  todos os jogos entre os empatados; antes, saldo e gols pró. **Muda a `classificacao_rodada` de quase todas as
  temporadas** e o texto do critério em `fases.csv`.
- **QE-003:** Barcelona 1-1 Sevilla de 2003/04 em 03/09/2003, à 00:05 (o "jogo da meia-noite"; antes, 02/09 sem hora).
  Dicionário `DATAS`.
- **QE-004:** Real Madrid x Real Sociedad (2004/05) e Granada x Athletic (2023/24) com a observação do jogo suspenso e
  completado em outro dia. Dicionário `SUSPENSOS`.
- **QE-007 (parte do Espanhol):** observações da classificação em português; as de vaga europeia saem.
  - O tradutor é comum às 8 ligas: `coleta/comum-europa/notas_wiki.py`. Os outros importadores já o usam e cada liga
    entra no pacote quando for reimportada (Inglês, Alemão, Francês e Português vêm nas próximas correções).
  - A nota que só apontava o código de outro clube ("hth_BET=ATH") agora traz o texto da nota apontada
    (`wiki_tabela.py`).
- Teste de carga: "esp-1: 95 edições, 27716 jogos, 0 clubes novos -> OK". **Pedido:** recarregar `esp-1` e publicar.

## 23/11 — coleta Europa: correções da revisão no Inglês (`eng-1`) e nomes da ESPN (RC-004)

Para o agente 1 (recarregar e publicar) e o agente de revisão (conferir e fechar os ids).

- **QE-005:** Sheffield Wednesday 3-1 Aston Villa (1953/54) em 07/11/1953 (antes 07/09).
- **EN-016:** autores dos 37 gols dos 12 jogos em que os gols da ESPN não fecham com o placar, pela ficha do BDFutbol
  (dicionário `GOLS_MANUAIS`, com a url de cada ficha na `fonte` do gol). Com isso a artilharia calculada de 2014/15
  fica Agüero 26, a oficial.
- **QE-006:** árbitro com o nome completo do BDFutbol ("Mike Dean", "David Elleray") em todas as temporadas desde 1960/61.
  Antes era só do football-data, desde 2000/01, em três formatos. Onde a ESPN não tem estádio, entra o do BDFutbol; com
  isso, todos os jogos desde 1960/61 têm estádio. Leitor em `coleta/comum-europa/bdfutbol.py`; páginas em
  `data/coleta/eng-1/bdfutbol/`.
- **EN-004 (D-17 c):** fica Albert Shepherd com 26 em 1905/06; a `fonte` do artilheiro anota que a RSSSF dá Walter White
  com 26 e a biografia dá 25 a Shepherd.
- **QE-007 (parte do Inglês):** observações da classificação em português; as de vaga europeia hipotética saem.
- **RC-004:** "Fernando Morientes", "Sávio" e mais 8 nomes da ESPN em formato de documento ("Goncalves da Silva Ailton"
  -> "Ailton", "Jeronimo Baretto Cacau" -> "Cacau"...) corrigidos em `coleta/comum-europa/nomes_jogadores.py`. A
  correção é aplicada ao gravar o pacote, em todas as ligas; cada liga reimportada leva a correção (Francês, Alemão e
  Português vêm nas próximas correções). A varredura completa dos ~2 mil nomes com 3 palavras ou mais fica como
  pendência.
- Teste de carga: "eng-1: 127 edições, 51330 jogos, 0 clubes novos -> OK". **Pedido:** recarregar `eng-1` e publicar.

## 23/11 — coleta Europa: correções da revisão no Francês (`fra-1`)

Para o agente 1 (carregar e publicar; o Francês ainda não está no site) e o agente de revisão (conferir e fechar os ids).

- **FR-001:** saem 14 rebaixamentos falsos de 1932/33 a 1936/37, 1938/39 e 1966/67.
  - Os clubes da temporada seguinte agora vêm do ogol pelo nome; antes, pelo código não votado.
  - Fusões sem rebaixamento (`FUSOES`): Olympique Lillois e Fives (Lille OSC), Excelsior e RC Roubaix (CORT) em 1938/39;
    Toulouse de 1937 com o Red Star em 1966/67.
  - O Antibes de 1938/39 continua rebaixado (D-18 c).
- **FR-002:** bônus por época. Em 1973/74, 1 ponto para quem marca 3 gols ou mais; em 1974/75 e 1975/76, 1 ponto por
  vitória com 3 ou mais de diferença. As 39 punições falsas sumiram e a Corrida não tem mais pontos negativos.
- **FR-003, FR-004:** Marseille x Racing (1951/52) e Nancy x Marseille (1955/56) com 0-0 e vitória dada no tribunal.
  A observação traz o placar de campo (2-3 e 2-4, invasão de campo).
- **FR-005:**
  - quando o ogol traz outro placar para um jogo da base, fica o da base com a data do ogol; isso volta os 9 placares de
    1946/47;
  - Marseille x Bordeaux (27/10/1946) com vitória do Marseille no tribunal (0-0), como nas tabelas das duas Wikipédias.
    Fica pendente conferir num jornal.
- **FR-006:** Valenciennes x Marseille (1992/93) com derrota para os dois (0-0; em campo, 0-1). O -1 da Wikipédia en não
  entra como punição.
- **FR-007:** Racing 5-1 Stade Français e Stade Français 1-0 Racing (1947/48).
- **FR-008:** volta o Sochaux 4-3 Rennes (1958/59), com a divergência anotada.
- **FR-009:** 41 datas corrigidas: transfermarkt e ogol concordam por 3 dias ou mais. Lista em
  `data/coleta/fra-1/correcoes/datas.csv`. Os 99 casos de 1 a 2 dias ficam pendentes.
- **FR-010:** Le Havre 2008/09 sem a punição que só a RSSSF trazia (26 pontos).
- **FR-011 e FR-019:**
  - Onnis empatado na artilharia de 1979/80 e Garande na de 1983/84;
  - Bokšić com 23 gols em 1992/93 (D-17 b);
  - nomes de jogo: Thadée Cisowski, Sékou Touré, Abegglen, Mercier, Koranyi, Kargu, Pauleta e diacríticos.
- **FR-012 (D-24 a):** clube novo "Toulouse FC (1937)" (1946/47-1966/67), separado do Toulouse de 1970.
- **FR-013 (D-24 b):** Lyon OU junto do Lyon e SO Montpellier separado, como estavam.
- **FR-014:** observações em português; os códigos soltos ("OL", "OM", "NIC") viraram o texto da nota apontada.
- **FR-015:** observação nos rebaixamentos fora de campo: 1990/91 Bordeaux, Brest e Nice (DNCG), 1993/94 Marseille
  (VA-OM), 2000/01 Toulouse e 2016/17 Bastia.
- **FR-016:** texto do tribunal com o placar dado e o de campo.
- **FR-017:** as 4 dúvidas anotadas em `EXPLICACOES`; fica a base até conferir num jornal.
- **FR-018:** critério de desempate por época.
  - Média de gols até 1961/62: a Wikipédia fr a cita em todas as temporadas até aí e em nenhuma depois.
  - Saldo desde 1962/63, com o confronto direto como último critério.
  - 1953/54 fica pela média: Nancy 12º, Metz 13º.
- **FR-020:** Antibes 1932/33 com a observação "excluído da final por suborno; não há 3º lugar oficial".
- **FR-021:** "Évian".
- **FR-022:** docstring e relatório sem o árbitro do football-data (a França não tem).
- Teste de carga: "fra-1: 88 edições, 30466 jogos, 2 clubes novos -> OK". Os 2 novos são "Évian" e "Toulouse FC (1937)".
- **Pedido:** carregar `fra-1`.

## 23/11 — coleta Europa: correções da revisão no Alemão (`ger-1`)

Para o agente 1 (recarregar e publicar) e o agente de revisão (conferir e fechar os ids).

- **DE-001:** Arminia Bielefeld 1971/72 com 0 pontos (ajuste -19; dicionário `PUNICOES`).
- **DE-002:** critério do regulamento por época: média de gols até 1968/69, saldo desde 1969/70. **Muda a
  `classificacao_rodada`** das temporadas em que o critério antigo era outro.
- **DE-003:** 103 datas corrigidas (transfermarkt e RSSSF concordam). Inclui o Schalke x Düsseldorf de 1980/81, que
  estava no achado e não na lista. Nenhum clube com 2 jogos no mesmo dia. Lista em
  `data/coleta/ger-1/correcoes/datas.csv`.
- **DE-004:** os 3 casos em dúvida ficam como estão (pendência).
- **DE-005:** 5 jogos de tribunal com `awd` e o placar de campo na observação (1970/71, 1976/77, 1992/93, 1994/95,
  2010/11).
- **DE-006 e DE-013:** observação na edição (Hertha 1964/65, Arminia 1971/72, Dresden 1994/95, 3º lugar dividido em
  1979/80).
- **DE-007:** observações em português; o "S04" virou o texto da nota.
- **DE-008:** nomes de jogo dos artilheiros (Aílton, Élber, Toni, Grafite, Gómez, Kane...).
- **DE-009:** 44 nomes da ESPN acertados no código comum (`nomes_jogadores.py`): Marcelinho, Ewerthon, Cacau, Štajner...
- **DE-010 e DE-011:** autores dos gols.
  - RSSSF de 1963/64 a 1998/99: 33.151 gols, nos jogos em que a soma fecha (cerca de 97%).
  - Ficha do ogol para 1999/00, 2000/01 e os jogos em que a ESPN falta ou não fecha: 991 gols.
  - Sem autor ficam 548 jogos com gol, a maioria até 2000/01; de 2010/11 em diante sobram 13 (eram 36).
- **DE-012 (D-04 a):** nota da Relegation na `observacao` da edição, nas 28 temporadas, pela Wikipédia de (jogos e quem
  ficou com a vaga).
- **DE-014:** fechado com a era antiga (1902/03-1962/63), já no GitHub.
- Teste de carga: "ger-1: 124 edições, 20303 jogos, 0 clubes novos -> OK". **Pedido:** recarregar `ger-1` e publicar.
- **Pedido (todas as correções de hoje: `ita-1`, `esp-1`, `eng-1`, `fra-1`, `ger-1`, `por-1`):** depois de recarregar,
  rodar as varreduras do plano (`python -I revisao/tela/varredura.py` e `datas_repetidas.py`, com a lista de
  competições trocada). Elas leem o banco.

## 23/11 — coleta Europa: correções da revisão no Português (`por-1`)

Para o agente 1 (recarregar e publicar) e o agente de revisão (conferir e fechar os ids).

- **PT-002:** Benfica 1-2 Sporting (1994/95) de volta (sai a correção para 2-0). Sporting 55 pontos, Benfica 47; as
  posições não mudam.
- **PT-003:** 1944/45 com a ordem da RSSSF: vice Sporting, 6º Olhanense, 7º Estoril.
- **PT-004 (D-20 b):** Braga x Benfica (1986/87) com derrota para os dois (1-1 em campo). Benfica 48 e campeão; Braga 25 e
  11º. As posições 9º a 13º seguem a Wikipédia pt.
- **PT-005 (D-19 c):** 2005/06 com 13º Naval e 14º Académica.
- **PT-006 (D-20 a):** Porto 2007/08 com 75 pontos e a observação da devolução em 2017; União de Leiria com -3 e
  observação.
- **PT-007:** Benfica 2-1 Espinho e Espinho 2-0 Benfica (1980/81).
- **PT-009:** fica a decisão do ogol no CUF x Vitória de Setúbal (a ficha registra "derrota administrativa"); o texto
  do motivo foi corrigido.
- **PT-010 e PT-011:** 29 datas corrigidas: 26 em que o football-data e o transfermarkt concordam contra o ogol, e 3
  impossíveis (1979/80, 1993/94, 1997/98). Os casos de 1938/39 e 1939/40 ficam pendentes.
- **PT-012 e PT-013:** Seferović com 23 gols (2018/19); "Luis Suárez" sem o travessão.
- **PT-014 e PT-015:** observações em português, e os códigos ("PAÇ", "BRA") viraram o texto da nota.
- **PT-016, PT-017 e PT-018:** observação nos rebaixamentos fora da zona (1950/51, 1961/62, 1973/74, 1997/98 Leça e
  Chaves, 2005/06, 2007/08, 2008/09, 2019/20), no Estrela da Amadora de 2023/24 (refundação, D-24 c) e no SL Elvas de
  1946/47 (fusão, D-24 d).
- **PT-019:** autores dos gols de 1999/00 a 2005/06.
  - RSSSF: 4.385 gols.
  - Ficha do ogol: 699 gols, para 2001/02 (que a RSSSF não traz) e os jogos em que a ESPN falha (2010/11 caiu de 257 para
    27 jogos sem autor).
- **PT-020:** não feito. Árbitro e público pelo transfermarkt são umas 11 mil páginas; fica como pendência.
- Teste de carga: "por-1: 92 edições, 20978 jogos, 0 clubes novos -> OK". **Pedido:** recarregar `por-1` e publicar.

## 23/11 — coleta Europa: Holandês e Escocês com as observações em português e os nomes da ESPN

Para o agente 1 (recarregar e publicar).

- `ned-1` e `sco-1` reimportados com o tradutor comum das notas da Wikipédia (`notas_wiki.py`) e os nomes da ESPN
  acertados (`nomes_jogadores.py`). Mudam só a `observacao` da `classificacao_final` e o `jogador` de alguns gols e
  cartões (ex.: "Rodrigues Dos Santos Cristiano" -> "Cristiano").
- Teste de carga: "ned-1: 138 edições, 21878 jogos, 0 clubes novos -> OK"; "sco-1: 129 edições, 33076 jogos, 0 clubes
  novos -> OK".
- **Resumo do dia (revisão profunda, plano da coleta Europa):** corrigidos todos os ids do plano, menos:
  - IT-017: campeonatos italianos de 1898 a 1928/29. É coleta nova e está na fila depois de `bel-1` e `tur-1`.
  - PT-020: árbitro e público do Português (11 mil páginas do transfermarkt).
  - Os que esperam terceira fonte, todos anotados nas pendências de cada liga:
    - DE-004;
    - os 99 casos de 1 a 2 dias do FR-009;
    - FR-017;
    - a vitória do Marseille sobre o Bordeaux em 1946/47 (FR-005);
    - PT-010 de 1938/39 e 1939/40.
