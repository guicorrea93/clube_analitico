# Pedidos do agente de coleta Europa

Recados ao agente 1 (banco e painel). Cada item diz o que já está no pacote enquanto isso.

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
