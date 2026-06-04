> Registro da auditoria multi-agente (verificacao independente por ano contra RSSSF local + corroboracao web) que motivou a camada estrutural do Brasileiro antigo. Gerado em 2026-06-03.

# Auditoria do "Brasileiro Antigo" — Brasileirões 1992–2002

> Relatório consolidado de modelagem, dados e UX. Base: verificação independente por ano (RSSSF local + Wikipédia PT/EN + consulta ao `db/brasileirao.db` e ao código), revisão de lógica de render e proposta de redesign. Caminho do repositório: `C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico`.

---

## 1. Resumo executivo

**As fases fazem sentido?** Parcialmente. As edições importadas existem, os placares e os campeões estão corretos, e a aritmética de jogos fecha em todos os anos. O problema **não é o dado de resultado** — é a **estrutura de competição** de várias edições, que foi achatada na importação porque o schema histórico só tem três alavancas (`fase_ordem`, `fase_nome`, `fase_tipo ∈ liga|grupo|mata_mata`) e **nenhuma coluna de grupo/subfase**.

**Diagnóstico em duas camadas:**

- **Anos "limpos" (modelagem correta):** **1996, 1998, 1999, 2001, 2002**. São ligas de turno único de tabela real + mata-mata genuíno. Os achados aqui são todos de **metadado/rótulo de baixa severidade** (critério de título não modelado, legs não distinguidas, rótulo de rodada inflado). Nenhum erro estrutural.
- **Anos com problema real de modelagem:** **1992, 1993, 1994, 1995, 1997, 2000**. Aqui há colapso de estrutura que **distorce qualquer tabela/corrida reconstruída** e esconde fases decisivas:
  - **1995** — fase liga *partida em dois turnos* (132 + 144 jogos) com dinâmica oposta (1º turno 100% intra-grupo, 2º turno 100% cross-grupo). O dashboard só lê **a primeira** fase `liga` → mostra metade da temporada.
  - **1993 / 1994** — **grupos paralelos** (4 grupos na 1ª fase; 2 grupos E/F na 2ª) colapsados em uma fase `grupo` única sem identidade de grupo → tabela única somando times que nunca se enfrentaram.
  - **1992 / 1993 / 1994** — colapso de subfases (FIRST STAGE + SECOND STAGE) na mesma "rodada" → **corrupção da sequência cronológica** (ida e volta de datas diferentes na mesma rodada), não só subcontagem.
  - **1992 / 1997** — fase **de grupo decisiva** (quadrangulares/semifinal por pontos) que define os finalistas fica **invisível**: o bracket só renderiza `mata_mata` e a tabela única só renderiza a fase `liga`.
  - **2000** — Copa João Havelange: artefatos de importação (`clubes=29`, `65 rodadas`), replay da final gravado com data de 2001 dentro da edição 2000.

**Padrões transversais:** (a) **critério de título/desempate nunca é campo estruturado** — fica em `observacao` (frequentemente vazia) em todas as edições 1990–2001; (b) **risco de mojibake** na fonte RSSSF (entidades HTML + latin-1) — **confirmado como NÃO persistido** em 1992, 1994, 1998, 2000 (nomes canônicos limpos), mas **não verificado** nos demais anos; (c) **pontuação errada no dashboard**: `calcHNTable` usa 3 pts por vitória para todos os anos, quando **1992–1994 usavam 2 pts**.

**Veredito de confiança:** alta para 1992, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002 (verificação cruzou banco/código). Para **1993** a verificação confirmou o *formato real* mas **não inspecionou banco/importador** — o lado "dbAtual" é inferência plausível, sinalizada abaixo.

---

## 2. Tabela ano-a-ano

Considera apenas discrepâncias com veredito **confirmado**. Itens **refutado/incerto** estão sinalizados na coluna de notas.

| Ano | Formato real (resumido) | O que o banco modela | Veredito |
|-----|-------------------------|----------------------|----------|
| **1992** | 20 clubes. 1ª fase turno único (190 j/19 rod), **sem rebaixamento**. 2ª fase = **2 quadrangulares paralelos** (G1/G2), duplo turno, vencedor de cada vai à final. Final ida/volta, vantagem do duplo empate à melhor campanha (Botafogo); Flamengo reverteu (5-2 agreg). | 2ª fase como bloco `grupo` único de 24 j **sem coluna de grupo**; rodadas colapsadas (3 em vez de 6/grupo, misturando ida/volta de datas diferentes); critério da final vazio. | **Erro de modelagem** (grupos colapsados + sequência de rodadas corrompida) + ajustes de metadado |
| **1993** | 32 clubes. 1ª fase = **4 grupos paralelos A–D** de 8, duplo turno, classificação **assimétrica** (A/B classificam 3; C/D classificam 2 ao playoff e rebaixam 4). Playoff repescagem ida/volta (C+D). 2ª fase = **2 grupos E/F** de 4. Final 2 jogos. Campeão Palmeiras. | Fase `grupo` única de 224 j sem coluna de grupo; rodadas turno/returno reiniciam em 1; playoff como `mata_mata` (4 j) sem critério. | **Erro de modelagem** *(formato confirmado; impacto no banco/importador é inferência — não inspecionado)* |
| **1994** | 24 clubes (2 pts/vitória). 1ª fase = **4 grupos A–D** (120 j). 2ª fase = **2 grupos E/F** com 2 subfases (120 j, **15 rodadas reais**). Repescagem (56 j, 14 rod) **concorrente** à 2ª fase. Mata-mata ida/volta. Bônus +1 ao vencedor de grupo. Campeão Palmeiras. | 1ª e 2ª fases `grupo` únicas sem grupo/subfase; rodadas = MAX(ROUND) (8 e 7) em vez de 15/14, misturando subfases; Repescagem como `fase_ordem=3` (posterior); critério/bônus não modelados. | **Erro de modelagem** (grupos + subfases colapsadas + ordem cronológica) |
| **1995** | 24 clubes. **2 grupos fixos de 12.** 1º turno (11 rod) **100% intra-grupo**; 2º turno (12 rod) **100% cross-grupo**. 4 semifinalistas = vencedores de grupo por turno. Mata-mata por agregado, vantagem à melhor campanha. Campeão Botafogo. | **Duas** fases `liga` (132 + 144 j) sem coluna de grupo; rodada reinicia em 1 no 2º turno; rótulo "13 rodadas" no 1º turno (real 11). | **Erro de modelagem** (liga partida em dois + grupos colapsados); rótulo de rodada do 1º turno errado |
| **1996** | 24 clubes, turno único (276 j/23 rod), 8 ao mata-mata, 2 rebaixados. Mata-mata ida/volta. Final 2-2 no agregado, **Grêmio campeão por melhor campanha**. Total 290 j. | Liga 276 j/23 rod (correto); QF 8 / SF 4 / Final 2 (correto). Critério da final só em `observacao` de partida. | **OK** — só ajuste de metadado (critério estruturado + legs no rótulo) |
| **1997** | 26 clubes, turno único (325 j/25 rod). 2ª fase = **2 grupos A/B de 4** ("Grupo semifinal"), só o 1º de cada vai à final. Final 0-0/0-0, **Vasco campeão por melhor campanha**. Total 351 j. | 1ª fase liga correta; 2ª fase `grupo` única de 24 j **sem grupo A/B**; critério da final em texto livre. | **Erro de modelagem** (2 grupos paralelos colapsados; fase decisiva some do bracket) |
| **1998** | 24 clubes, turno único (276 j/23 rod). Mata-mata **melhor de 3** (QF 12 / SF 6 / Final 3, total 297). Campeão Corinthians (vence 3º jogo). | Liga 276/23 (correto); QF 12 / SF 6 / Final 3 (correto). Critério "melhor de 3"/mando não modelado; séries empatadas em jogos decididas por campanha invisíveis. | **OK** — só ajuste de metadado |
| **1999** | 22 clubes, turno único (231 j/21 rod). Mata-mata **melhor de 3** (QF 11 / SF 5 / Final 3, total 250). Vantagem de empate ao melhor classificado. Campeão Corinthians. | Liga 231/21 (correto); QF 11 / SF 5 / Final 3 (correto). `mata_mata` genérico sem campo de legs/melhor-de-3; critério não modelado. | **OK** — só ajuste de metadado |
| **2000** | Copa João Havelange, 4 módulos paralelos. **Módulo Azul** = 1º nível (25 clubes, turno único, 300 j). Fase final 16 clubes, mata-mata ida/volta (16/8/4/2). Final replay (18/01/2001 após queda do alambrado em São Januário). Campeão Vasco. | `clubes=29` (união de participantes de fases distintas); **"65 rodadas"** = contador de blocos de data (real ≈ 25); só Azul + playoffs importados (finalistas externos "do nada"); replay com data de 2001 na edição 2000; jogo abandonado substituído sem marcador. | **Erro de modelagem/artefatos** (rótulo de rodada, escopo de módulos, replay/abandono) |
| **2001** | 28 clubes, turno único (378 j/27 rod), **tabela única**. QF/SF **jogo único**; Final **ida/volta** (agregado 5-2). Vantagem ao melhor classificado; usa prorrogação [aet]. Campeão Atlético-PR. | Liga 378/27 tabela única (**correto**); QF 4 / SF 2 / Final 2 (correto). `mata_mata` não distingue jogo único de ida/volta; [aet] e critério não registrados. | **OK** — só ajuste de metadado. *Nota: o achado "erro de contagem" foi **REFUTADO** — o banco está certo; os "Moved Matches" preenchem as rodadas 15/19.* |
| **2002** | 26 clubes, turno único (325 j/25 rod), tabela única. Mata-mata ida/volta (8/4/2). Vantagem do duplo empate à melhor campanha. Campeão Santos (5-2 agreg). Total 339 j. | Liga 325 j mas rotulada **"29 rodadas"** (= matchdays de calendário; real 25); mata-mata sem agregador de confronto/critério. | **Ajuste de rótulo** (rodadas 29→25) + metadado. Sem erro estrutural. |

---

## 3. Problemas de DADOS confirmados (priorizados)

### 🔴 ALTA

**D1. Fase liga partida em dois turnos lidos só pela metade (1995).**
O importador `importar_brasileirao_historico_1995.py` (L97-98) grava **duas** fases `tipo="liga"`: `Primeiro turno` (132 j) e `Segundo turno` (144 j). O dashboard só lê a primeira (`fases.find(f => f.tipo === "liga")`, `gerar_dashboard_html.py` L2371/L2427) → classificação e corrida cobrem **só 132 dos 276 jogos**. Além disso `rodada` reinicia em 1 no 2º turno, então concatenar ingenuamente misturaria rodadas.
- **Correção:** o consumo é problema de render (§4-R1). No dado, expor **rodada acumulada** (ou um campo `turno`) no payload para permitir ordenação global. A composição fixa dos 2 grupos de 12 entre turnos deve ser preservada.

**D2. Grupos paralelos colapsados em tabela única — sem coluna de grupo (1993, 1994, 1997; 2ª fase de 1992).**
`dim_fase_nacional_historica` e `fato_partida_nacional_historica` **não têm coluna de grupo** (confirmado em `sql/schema.sql` L229-256). Logo a 1ª fase de 1993 (4 grupos A–D), as fases de 1994 (4 grupos + 2 grupos E/F com subfases), a 2ª fase de 1997 (grupos A/B) e a 2ª fase de 1992 (G1/G2) viram blocos `grupo` indistinguíveis. Qualquer tabela reconstruída soma pontos de times que nunca se enfrentaram.
- **Correção:** adicionar coluna `grupo` (e, para 1994, `subfase`) em `dim_fase_nacional_historica` **ou** em `fato_partida_nacional_historica`, populada pelos importadores que já leem os cabeçalhos `GROUP A/B/…` e `QUALIFY` do RSSSF. Alternativa sem schema: derivar grupos por componentes conexos no front (§5) — resolve a visualização mas não a integridade do dado.

**D3. Pontuação errada na reconstrução de 1992–1994 (regra de pontos por época).**
`calcHNTable` (`gerar_dashboard_html.py` L2409) soma **3 pontos por vitória** incondicionalmente. **1992, 1993 e 1994 usavam 2 pontos por vitória.** Qualquer tabela reconstruída para esses anos diverge da classificação oficial **mesmo dentro de um único grupo**.
- **Correção:** parametrizar pontos por vitória por temporada em `calcHNTable` (2 pts até 1994, 3 pts a partir de 1995). Detalhe adicional: 1994 tinha **bônus +1** ao vencedor de grupo — não modelado; registrar em `observacao` ou campo dedicado se a fidelidade de tabela for requisito.

### 🟠 MÉDIA

**D4. Subfases colapsadas na mesma "rodada" — sequência cronológica corrompida (1992, 1993, 1994).**
Os importadores reiniciam o contador `ROUND` a cada FIRST/SECOND STAGE (ou subfase), então jogos de **ida e volta de datas diferentes** caem na **mesma rodada** (ex. 1992: rodada 1 = jogo de jun + jogo de jul). Não é só subcontagem (3 em vez de 6; 8 em vez de 15): a **ordenação temporal por rodada fica errada**, quebrando qualquer corrida rodada-a-rodada.
- **Correção:** no parser, **não reiniciar** o contador entre stages/subfases — usar rodada cumulativa por fase, ou segmentar por `subfase` + rodada local. Recontar: 1992 2ª fase = 6 rod/grupo; 1994 2ª fase = 15 rod, Repescagem = 14 rod.

**D5. Repescagem 1994 marcada como fase posterior, sendo concorrente.**
`fase_ordem=3` sugere sequência após a 2ª fase, mas os blocos QUALIFY são **simultâneos** (mesmas datas out-nov/94). Impacto semântico/cronológico, não de placar.
- **Correção:** ajustar ordenação/rótulo para indicar concorrência (mesma faixa de ordem, ou flag de paralelismo).

**D6. Risco de mojibake na fonte RSSSF — verificar nos anos não inspecionados.**
A fonte RSSSF traz entidades HTML (`VIT&Oacute;RIA`, `S&Atilde;O PAULO`, `GR&Ecirc;MIO`) **e** mojibake latin-1 (`Am�rica`, `Gr�mio`) afetando quase todos os clubes acentuados. **Refutado como persistido** em 1992, 1994, 1998, 2000 (banco guarda nomes canônicos limpos via `CANONICAL`/`canonical_name`). **Não verificado** em 1993, 1995, 1996, 1997, 1999, 2001, 2002.
- **Correção:** auditar a coluna de nome de clube e `observacao`/`competicao` no banco para os anos não verificados; confirmar que todos os importadores decodificam entidades HTML e latin-1 antes de canonizar. Erros tipográficos da fonte (`CORITNHIANS`, `DEPORTIVA`) também devem ser normalizados para evitar clubes-fantasma.

**D7. Artefatos da Copa João Havelange (2000).**
`clubes=29` (união de participantes de fases distintas); `"65 rodadas"` (contador de blocos de data; real ≈ 25 para turno único de 25); replay da final gravado com **data 2001-01-18 dentro da edição 2000**; ambos os jogos da final com `jogo=1`; jogo abandonado (30/dez, 0-0) **descartado** pelo filtro `' abd '` e substituído pelo replay **sem marcador**; `fato_classificacao_rodada` sem snapshots para 2000.
- **Correção:** rotular Módulo Azul como "1 de 4 módulos"; corrigir contagem de rodadas; marcar o replay e o abandono em `observacao`; resolver `jogo` duplicado na final; decidir se o replay de jan/2001 pertence à temporada 2000 (provavelmente sim, com nota).

### 🟡 BAIXA

**D8. Critério de título/desempate nunca é campo estruturado (padrão 1992–2001).**
A `observacao` está **sistematicamente vazia** em todas as fases de 1990–2001. Critérios decisivos — melhor campanha (1992, 1993, 1995, 1996, 1997, 2001, 2002), melhor de 3 (1998, 1999), vantagem de empate, prorrogação [aet] (2001), away/agregado — não têm onde morar. Sem isso, resultados como "Santos avança após empatar o agregado" ou "Grêmio campeão sem vencer no agregado" ficam **inexplicáveis** a partir do dado estruturado.
- **Correção transversal:** adicionar metadado de fase (ex. `criterio_desempate`, `formato_serie='best_of_3'|'two_legs'|'single_leg'`, `vantagem_empate`) em `dim_fase_nacional_historica`; preencher via importadores. Tratar como **um** projeto, não caso a caso.

**D9. Rótulos de rodada inflados por contador de matchdays (2000, 2002).**
"65 rodadas" (2000) e "29 rodadas" (2002) vêm de blocos de data com contagens irregulares por bloco, não de rodadas de competição (real ≈ 25 nos dois casos). Propaga para o slider/`rodada_range` do dashboard.
- **Correção:** derivar número de rodadas da estrutura (turno único de N times = N-1 rodadas) ou normalizar a numeração no parser.

**D10. Penalizações e resultados administrativos não modelados.**
Atlético-PR começou 2001 com **-5 pts** (escândalo) e 1992 sem rebaixamento (atípico). Em 1999 houve placares dados por tribunal (W.O. Hiroshi) que afetaram o rebaixamento do Gama. Sem campo de pontos/penalização, tabelas recalculadas divergem da oficial.
- **Correção:** registrar penalizações/notas em `observacao` de participante/fase; usar placares *awarded* (não de campo) nos casos administrativos.

---

## 4. Problemas de DESIGN/render confirmados

Todos verificados em `gerar_dashboard_html.py`.

**R1 (ALTA) — Tabela e corrida usam só metade da fase liga em 1995.**
`faseLiga = fases.find(f => f.tipo === "liga")` (L2371, L2427) pega **a primeira** fase liga. Com 1995 tendo duas, a tabela (`calcHNTable`) e a race (`getHNRaceFrames`) cobrem só o 1º turno.
- **Correção:** `fases.filter(f => f.tipo === "liga")` e unir partidas. Para a race, acumular por `(fase_ordem, rodada, jogo)` em rodada global (não `p.rodada <= r` cru, que mistura turnos), ou rotular o eixo "Turno X – Rodada Y".

**R2 (ALTA) — `calcHNTable` em fases `grupo` paralelas produz ranking sem sentido.**
Como não há fase `liga` em 1993/1994, `faseLiga` cai no fallback `"Primeira fase"` e `calcHNTable` soma pontos de grupos disjuntos numa tabela de 24–32 clubes.
- **Correção:** nunca usar uma fase `grupo` como `faseLiga`; renderizar **uma tabela por grupo** (§5) e ocultar a corrida de pontos (que pressupõe liga única).

**R3 (ALTA) — Bracket ignora fases de grupo decisivas → fase invisível.**
`renderHNBracket` filtra `p.fase_tipo === "mata_mata"` (L2494). As fases de grupo decisivas de **1992** ("Segunda fase", 24 j), **1993** ("Segunda fase") e **1997** ("Grupo semifinal") não entram no bracket **nem** têm tabela própria — o usuário nunca vê como os finalistas saíram. Em 1992 e 1997 essa é justamente a fase que define o título.
- **Correção:** renderizar tabela(s) por grupo para toda fase `grupo` de ordem alta; garantir que **toda** fase apareça em **alguma** visão.

**R4 (MÉDIA) — Desempate de final empatada elege o visitante por padrão.**
Em final empatada no agregado, `winA = aggA > aggB || (tiedFinalByCriterion && officialChampion === teamA)` (L2510). Se `officialChampion` vier vazio (sem linha `pos=1`) ou com grafia divergente, `winA=false` e o **time B é declarado campeão silenciosamente**.
- **Correção:** se empate e sem campeão oficial válido, exibir "campeão indefinido pelos dados" em vez de eleger o visitante; validar `officialChampion ∈ {teamA, teamB}`; preferir desempate por `clube_id` (exige carregar `mandante_id`/`visitante_id` nas partidas do payload).

**R5 (MÉDIA) — Bracket: agrupamento por `p.jogo` nulo e alinhamento por padding mágico.**
`pares = [...new Set(jogos.map(p=>p.jogo))]` (L2501): se `jogo` for null, todos os confrontos colapsam numa chave null. Alinhamento por `pad = Math.min(132, idx*52)` (L2533) desalinha colunas de alturas diferentes; ordenação por `data_iso.localeCompare` fica indefinida se `data_iso` vazio.
- **Correção:** garantir `jogo` preenchido nas fases mata-mata (importador) ou agrupar por par de clubes quando nulo; trocar padding por `flex` + `justify-content:space-around`; fallback de ordenação por `id`.

**R6 (BAIXA) — Seletor de fase não recalcula classificação; sem placeholder de classificação final vazia.**
O `<select id="hn-fase">` filtra só `tbl-hn-partidas`; tabela/race/bracket ignoram o filtro. E `tbl-hn-class-final` fica vazia sem mensagem quando não há classificação importada.
- **Correção:** definir contrato do seletor (recalcular a tabela da fase escolhida ou deixar claro que é só lista de jogos); adicionar placeholder "Sem classificação final importada".

**R7 (BAIXA) — Duas fontes de "campeão" podem divergir.**
KPI "Campeão" vem de `fato_classificacao_final_nacional` (query L238-262); o bracket usa `class_final_hist`/`vw_classificacao_final_historica` (L2491). Sob `GROUP BY`, múltiplas linhas `posicao=1` tornam `camp.nome` não-determinístico.
- **Correção:** unificar a fonte do campeão; garantir unicidade de `posicao=1` por edição.

---

## 5. Proposta de redesign (UX) — aba "Brasileiro Antigo" **phase-type aware**

A aba hoje só sabe renderizar `liga` (corrida + 1 tabela) e `mata_mata` (bracket). Fases `grupo` (quadrangulares, "Segunda fase", "Repescagem", "Grupo semifinal", "Módulo Azul") **não têm renderer próprio** e caem só na tabela genérica de jogos. O redesign torna a aba dirigida por dados, cobrindo os três tipos genericamente, **sem mudança de schema** (grupos derivados dos confrontos).

**5.1 Motor `buildHNPhaseModel` + `normalizePhaseType` + `RENDERERS`.**
Constrói, para a edição, um modelo normalizado de fases em ordem cronológica, classificando cada fase como `liga | grupo | mata_mata` pelo `fase_tipo` do banco, com **fallback heurístico** quando vazio (pares ida/volta → mata-mata; múltiplos componentes pequenos todos-contra-todos → grupo; senão liga). Um dicionário `RENDERERS` mapeia cada tipo ao seu componente. Layout da aba: KPIs → **Stepper** → `#hn-phases` (uma `<section>` por fase) → classificação final → tabelas de apoio em `<details>`.

**5.2 `renderHNGroupPhase` — classificação por grupo (componente novo, central).**
Em vez de uma tabela única, **um mini-card por grupo** em grid responsivo (`repeat(auto-fit, minmax(260px,1fr))`). Cada card: cabeçalho ("Grupo A", formato triangular/quadrangular derivado do nº de times), tabela **reusando `calcHNTable`** no subconjunto do grupo, e rodapé com quem se classifica. Linhas que avançam recebem faixa lateral `.qualifies` (padrão `inset 4px 0 0 var(--accent)`). Fase de grupo único (Módulo Azul) degrada para 1 card full-width.

**5.3 `deriveGroups` — grupos por componentes conexos (sem coluna no banco).**
Grafo: nós = clubes, arestas = "jogaram entre si nesta fase"; componentes conexos via BFS/DFS → cada componente é um grupo (rótulo A/B/C). **Quantos classificam** = interseção dos clubes do grupo com os participantes da **fase seguinte**. Memoizável por `edição+fase`. Mitigação para chaves cruzadas: se um componente exceder o tamanho esperado e houver `jogo`/`rodada` de mata-mata, reclassificar via `normalizePhaseType`. *(Observação honesta: derivação no front resolve a **visualização**, mas a integridade do dado ainda pede a coluna de grupo de D2 — especialmente onde dois grupos compartilham um confronto, como repescagem.)*

**5.4 `renderHNStepper` — timeline de fases.**
Barra horizontal abaixo dos KPIs, gerada do mesmo modelo: passos `liga → grupo → mata_mata → 🏆`, coloridos por tipo, clicáveis (`scrollIntoView` na seção + sync com `<select id="hn-fase">`). Costura toda a narrativa, **incluindo as fases de grupo** que hoje somem.

**5.5 `renderHNKnockoutPhase` — bracket melhorado.**
Refator de `renderHNBracket`: troca `padding-top` mágico por `flex column` + `justify-content:space-around`; conectores entre colunas (CSS `::after` em L ou SVG overlay); campeão como **coluna-taça final** do funil (glow `--accent2`) em vez de banner solto; mantém lógica de agregado/legs. Incorpora as correções R4/R5 (campeão indefinido, agrupamento por par robusto).

**5.6 CSS.** Bloco novo após `.hn-bracket-*`, reutilizando exclusivamente as variáveis de tema existentes (`--accent`, `--accent2`, `--accent3`, `--panel2`, `--border`, `--muted`, `--row-hover`, `--shadow-sm`) + responsivo `<=1100px`. Mantém consistência dark/futebol e light mode.

---

## 6. Plano de execução recomendado

> **Confirmações a pedir ao usuário ANTES de qualquer alteração** (são artefatos versionados/críticos):
> 1. **Alterar o schema** (`sql/schema.sql`) para adicionar `grupo`/`subfase`/`criterio_*`? Isso exige migração e reimportação. (Necessário para D2, D8.)
> 2. **Reescrever importadores e regenerar o banco** `db/brasileirao.db`? Há backups datados em `backups/` — confirmar qual é o ponto de restauração válido.
> 3. **Editar `gerar_dashboard_html.py`** (correções de render R1–R7 + redesign §5)?
> 4. Escopo: tratar **todos os anos** agora ou priorizar os de erro estrutural (1992–1995, 1997, 2000)?

**Ordem sugerida:**

1. **Backup explícito** — snapshot novo de `db/brasileirao.db`, `sql/schema.sql`, `gerar_dashboard_html.py` e dos importadores (mesmo padrão de `backups/clube_analitico_critical_*`), registrando o commit/hora.
2. **Quick-win de render sem tocar no banco** (baixo risco, alto valor):
   - R1 (1995: ler todas as fases liga) e R2 (não usar `grupo` como `faseLiga`).
   - D3 (parametrizar pontos por vitória 2/3 em `calcHNTable`).
   - §5 derivação de grupos no front (`deriveGroups`) + `renderHNGroupPhase` → R3 resolvido visualmente.
   - R4 (campeão indefinido) e R6/R7 (placeholders, fonte única do campeão).
3. **Correções de DADO no parser** (médio risco): D4 (não reiniciar contador entre stages/subfases → rodadas corretas), D5 (ordem da Repescagem 1994), D7 (artefatos 2000), D9 (rótulos de rodada 2000/2002).
4. **Migração de schema** (se aprovada): adicionar coluna `grupo`/`subfase` (D2) e metadado de critério (D8); ajustar importadores para popular; **reimportar** e **regenerar** o banco.
5. **Auditoria de encoding** (D6): rodar verificação de mojibake nos nomes/observações dos anos não inspecionados (1993, 1995, 1996, 1997, 1999, 2001, 2002).
6. **Redesign de render completo** (§5): stepper, bracket melhorado, CSS, regenerar o HTML.
7. **Validação:** reconciliar por ano contra RSSSF/Wikipédia — nº de jogos por fase, nº de rodadas reais, campeão/vice, tabela por grupo, e checar visualmente que **toda fase aparece em alguma visão**. Itens **incerto/refutado** (rótulo de dashboard de 1992; contagem de 2001) **não** devem gerar alteração sem reverificação direta.

**Notas de honestidade sobre incerteza:**
- O ano **1993** teve formato confirmado por fontes, mas **banco/importador/dashboard não foram inspecionados** — as afirmações sobre "como o importador grava" são inferência; reverificar no banco antes de corrigir.
- A discrepância de **contagem de 2001 foi REFUTADA**: o banco está correto (378 j/27 rod, tabela única). Não alterar.
- O achado de **rótulo de dashboard de 1992** ("bracket só para mata_mata esconde a fase") foi marcado **incerto** na pesquisa original, mas a inspeção de código aqui **confirma** o filtro `p.fase_tipo === "mata_mata"` (L2494) — então R3 procede; o que continua discutível é chamar o tipo `grupo` de "rótulo errado" (ele descreve corretamente o formato; o problema é a ausência de identidade de grupo).
- "25 rodadas" para Módulo Azul (2000) é **inferência aritmética** (turno único de 25 = 25 rodadas) — a fonte RSSSF não rotula rodadas ali; "65" está inequivocamente errado, mas o "correto" exato deve ser confirmado.

**Arquivos relevantes:** `C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\gerar_dashboard_html.py` (L2366-2544 render Brasileiro Antigo; L2400-2415 `calcHNTable`; L2489-2544 bracket); `C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\sql\schema.sql` (L229-256, sem coluna de grupo); importadores `importar_brasileirao_historico_199*.py` e `importar_brasileirao_historico_1998_1999.py`; `importar_brasileirao_historico_2000_2001.py`; banco `C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\db\brasileirao.db`.