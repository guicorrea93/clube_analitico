# Clube Analitico

> **Comece por `docs/COMECE-AQUI.md`** (mapa atual do projeto, banco genérico `db/futebol.db` e painel v2).
> Agente de coleta de competições novas: `docs/agente-coleta-COMECE-AQUI.md`.

Dashboard local de futebol brasileiro em HTML, gerado a partir de um banco
SQLite versionado no proprio repositorio.

Este README tambem funciona como manual de continuidade do projeto. A ideia e
que qualquer pessoa, ou outra IA, consiga entender:

- qual e a fonte de dados principal;
- quais scripts geram, validam e atualizam o dashboard;
- quais fontes externas foram usadas;
- o que ja foi importado;
- como continuar a expansao historica ano a ano.

## Estado Atual

Fonte principal do dashboard:

- `db/brasileirao.db`

Artefato visual principal:

- `dashboard.html`

Segundo dashboard independente:

- `dashboard_copa_mundo.html`
- Gerado por `gerar_dashboard_copa_mundo_html.py`
- Usa somente a Wikipedia em portugues como fonte: pagina principal da Copa do
  Mundo FIFA e a pagina de cada edicao de 1930 a 2026. Para os detalhes de
  partida, usa tambem paginas de grupos, fase final e finais dedicadas quando
  existem.
- A Copa de **2026 esta encerrada** (Espanha campea; cache da Wikipedia
  baixado de novo em 13/11/2026). Ela e lida como as outras edicoes: grupos,
  mata-mata, classificacao final das 48 selecoes e ficha dos 104 jogos (sem
  escalacoes, como 1950-2002).
- O gerador baixa/cacheia os HTMLs da Wikipedia, extrai tabelas de edicoes,
  ranking, fase de grupos, mata-mata, classificacao final, premios e estadios,
  e embute os dados + Plotly + bandeiras/cartazes/tacas (base64) no HTML final.
- E **independente** de `db/brasileirao.db`: nao depende do banco nem do
  `dashboard.html`. So precisa do cache em `data/worldcup_wikipedia/`.
- Requer `lxml` (usado por `pandas.read_html` e tambem diretamente, para
  escalacoes e infobox); ja consta em `requirements.txt`.

Como regenerar o dashboard das Copas:

```powershell
python -u .\gerar_dashboard_copa_mundo_html.py
# ou, junto do pipeline principal:
python -u .\build.py --with-copa-mundo
```

Banco relacional das Copas:

- `db/copa_mundo.db`
- Schema versionado em `sql/schema_copa_mundo.sql`
- Criado por `criar_banco_copa_mundo.py`
- Validado por `validar_banco_copa_mundo.py`
- Auditado contra RSSSF por `auditar_artilheiros_copa_mundo.py`
- Catalogo didatico em `catalogo_banco_copa_mundo.html`, gerado por
  `gerar_catalogo_banco_copa_mundo_html.py`
- Planejamento e regra de identidade em `docs/plano_banco_copa_mundo.md`
- Auditoria detalhada de jogadores em
  `docs/auditoria_identidade_jogadores_copa_mundo.md`
- Auditoria de artilheiros contra RSSSF em
  `docs/auditoria_artilheiros_copa_mundo.md`

Como recriar e validar:

```powershell
python .\criar_banco_copa_mundo.py
python .\validar_banco_copa_mundo.py
python .\auditar_artilheiros_copa_mundo.py
python .\gerar_catalogo_banco_copa_mundo_html.py
```

O modelo usa nomes de tabelas e colunas em portugues e segue o padrao do banco
do Brasileirao: schema separado, script criador e script de validacao. As
tabelas principais sao `competicao`, `edicao`, `selecao`, `alias_selecao`,
`identidade_pessoa`, `pessoa`, `alias_pessoa`, `estadio`, `fase`, `grupo`,
`partida`, `gol`, `escalacao`, `comando_tecnico`, `premiacao` e
`auditoria_identidade`.

Fontes e identidade:

- A fonte operacional continua sendo a Wikipedia PT/cache local usado pelo
  dashboard.
- RSSSF, FIFA e Wikidata entram como fontes de cruzamento em `fonte`.
- Aliases de pessoas ficam em `alias_pessoa`; conflitos ou nomes parecidos ficam
  em `auditoria_identidade`.
- Caso ja tratado: `Portugal + Ronaldo + jogador` aponta para `Cristiano
  Ronaldo` (`wikidata_id = Q11571`), enquanto `Brasil + Ronaldo + jogador`
  permanece separado.

Validacao atual do banco das Copas:

- 23 edicoes.
- 1.060 partidas.
- 89 selecoes.
- 5.031 pessoas.
- 2.983 gols/eventos.
- 9.273 registros de escalacao.
- 0 partidas com soma de eventos de gol divergente do placar.
- 86 auditorias de identidade pendentes para revisao humana/cruzamento futuro,
  incluindo tecnicos/arbitros e aliases de jogadores mantidos separados de
  forma intencional.
- Auditoria RSSSF de artilheiros: 161 de 161 registros bateram com o banco; 0
  divergencias e 0 sem correspondencia automatica. A revisao confirmou
  Leônidas com 8 gols no total de Copas: 1 em 1934 e 7 em 1938.
- Identidade global validada para jogadores que representaram duas selecoes ou
  selecoes sucessoras: Dejan Stankovic, Nikola Zigic e Robert Prosinecki.
  `Mazzola` foi revisado e mantido separado: Jose Altafini no Brasil e Sandro
  Mazzola na Italia.

Abas e recursos:

- **Geral das Copas**: KPIs, linha do tempo responsiva em "S" (desktop e
  mobile), titulos e top 4, rankings de vitorias/empates/derrotas (toggle
  total/%), gols e publico por edicao, maiores artilheiros (carreira) e
  artilheiro por edicao, **melhor ataque e melhor defesa por edicao** e maiores
  goleadas.
- **Gols**: base analitica de gols por partida/edicao/selecao/jogador, com
  cruzamento tecnico quando existe detalhe da StatsBomb Open Data. A aba deve
  evoluir para separar gols oficiais, gols contra, penalties, faltas, cabecadas,
  finalizacoes de dentro/fora da area, periodo do jogo, placar no momento do gol
  e curiosidades estatisticas.
- **Por Copa**: cartaz da edicao, resumo, classificacao final, grupos,
  chaveamento e jogos clicaveis. Ao selecionar uma partida, o dashboard abre
  diretamente um modal com placar, linha temporal dos gols, data, horario,
  estadio, publico, arbitro (e pais), escalacoes quando a Wikipedia fornece
  (numero/posicao/nome), quem entrou e treinadores. A ficha esta anexada em
  todos os jogos de 1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970,
  1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018,
  2022 e 2026 (em 2026, sem escalacoes).
- **Por Selecao**: bandeira, trajetoria, vezes em cada posicao, gols por edicao,
  distribuicao de resultados, adversarios, campanha e **"Quem fez os gols em
  cada Copa"** — todos os jogadores que marcaram, edicao a edicao, com o
  artilheiro destacado e uma nota quando a selecao teve **gol contra a favor**.

Estrutura do payload embutido (`const DATA` no HTML):

| Chave | Conteudo |
| --- | --- |
| `DATA.fonte` | URL da pagina principal e nota de acesso |
| `DATA.geral` | Tabelas da pagina principal: `editions`, `podium`, `attendance`, `blowouts`, `totals` |
| `DATA.copas[]` | Uma por edicao: `info`, `grupos`, `partidas`, `classificacao_final`, `premios`, `estadios` |
| `DATA.copas[].partidas[].ficha` | Detalhe da partida para 1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022 e 2026: data/hora, estadio, publico, arbitro, pais do arbitro e, quando disponivel na Wikipedia, escalacoes, substituicoes e treinadores |
| `DATA.selecoes[]` | Agregado historico por selecao (J/V/E/D/GP/GC, titulos, aproveitamento) |
| `DATA.artilheiros_selecao` | `{selecao: {ano: [[jogador, gols], ...]}}` |
| `DATA.gols_contra_selecao` | `{selecao: {ano: [[autor, gols], ...]}}` — gols contra a favor |
| `DATA.gols_analiticos` | Base granular de gols oficiais extraida do payload da Wikipedia/cache local, enriquecida com canonizacao de jogadores e auditoria de lacunas |
| `DATA.gols_detalhados` | Detalhes tecnicos cruzados da StatsBomb Open Data quando a partida/evento existe nessa fonte |
| `DATA.melhor_ataque_defesa` | `{ano: {ataque:{selecao,gp}, defesa:{selecao,gc,j}}}` |
| `DATA.curados` | `artilheiros_historico`, `artilheiros_edicao`, `marcadores_grupos` |

Alem de `__DATA_PAYLOAD__`, o template recebe `__PLOTLY_PAYLOAD__`,
`__FLAGS_PAYLOAD__`, `__POSTERS_PAYLOAD__`, `__TROFEUS_PAYLOAD__` e
`__FAVICON_PAYLOAD__`. Tudo vai embutido: o HTML final abre offline, sem CDN.

Detalhes de implementacao relevantes:

- **Selecao de tabelas por conteudo**: `parse_main()` localiza cada tabela da
  pagina principal por assinatura de cabecalho (helpers `find_table` /
  `has_header_cells` / `columns_text`), nao por indice fixo. Se a Wikipedia
  reordenar/inserir tabelas, o gerador falha alto com mensagem clara em vez de
  pegar a tabela errada silenciosamente.
- **Overrides por edicao** (`apply_edition_overrides`): as paginas de 1930-1982
  tem formatos irregulares (grupos de 3 times, **segunda fase de grupos** em
  1974/1978/1982, jogos de desempate, mata-mata sem tabela padrao). Para 1930,
  1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978 e 1982 os grupos e
  as partidas sao literais Python, gerados a partir do cache e conferidos a mao.
  O parser generico cuida so de 1986-2022.
- **2026 tem parser proprio** (`parse_2026`): 48 selecoes, 12 grupos e a fase
  "Dezesseis avos de final" (nao existia antes). As tabelas de grupo trazem a
  coluna `Equipevde` e uma coluna `Classificado`; `_group_tables_2026` acha as
  12 pelo cabecalho, nao pela posicao (a posicao mudou entre julho e novembro
  de 2026). Campeao, vice, 3o e 4o saem da classificacao final; a infobox
  generica erra em 2026 (aponta a Argentina como campea). Cuidado com o campo
  de gols da infobox: vem como "308 (2,96 por partida)", entao usa-se
  `to_int(val.split("(")[0])`. "Disputa pelo terceiro lugar" vira "Terceiro
  lugar", como nas outras edicoes. `MARCADORES_2026_CORRIGIDOS` guarda os
  marcadores de 2 jogos do Grupo J que a Wikipedia perdeu depois de julho (o
  cache antigo tinha a lista completa). Em `phaseRank` (JS), o teste de "avos"
  precisa vir **antes** do teste de "final", porque "dezesseis avos de final"
  contem "final".
- **Top 4 historico** (`podium_from_editions`): montado da tabela de edicoes,
  nao da tabela de podio da Wikipedia, que credita a Iugoslavia a Servia e a
  Uniao Sovietica a Russia.
- **Assets embutidos** (todos viram base64 no HTML): `ensure_plotly`,
  `ensure_flags` (bandeiras em w320; codigos vindos de `collect_flag_codes`),
  `ensure_posters` (cartaz de cada edicao), `ensure_trofeus` (Jules Rimet e Taca
  FIFA) e `ensure_favicon`. O recorte das tacas (`_recortar_trofeu`) remove o
  fundo com **rembg**, dependencia **opcional e pesada**, importada so quando o
  PNG transparente ainda nao esta em cache:
  `python -m pip install rembg onnxruntime`. Com os PNGs ja em
  `data/worldcup_wikipedia/trofeus/`, o rembg nunca e chamado.
- **Nomes de selecao** passam sempre por `clean_team`, que unifica aliases
  historicos (ex.: "Zaire" e "RD Congo" -> "Republica Democratica do Congo";
  "Checoslovaquia" -> "Tchecoslovaquia"). Isso evita a mesma nacao aparecer duas
  vezes na base.
- **Dados curados em um so lugar**: artilharia historica, artilheiro por edicao
  e os marcadores das partidas de fase de grupos de 2022 NAO aparecem nas
  tabelas extraidas (as paginas listam marcadores so no mata-mata). Ficam como
  constantes Python (`ARTILHEIROS_HISTORICO`, `ARTILHEIROS_EDICAO`,
  `MARCADORES_GRUPOS`) e sao injetadas no payload como `DATA.curados`; o template
  apenas renderiza. Para adicionar marcadores de outra edicao, inclua chaves no
  formato `"ano|Grupo X|Time1|placar|Time2": "marcadores"`.
- **Gols por jogador / selecao / edicao** (`build_team_scorers`, helpers `_sc_*`):
  parseia o campo `marcadores` de cada partida. Cobre prefixo por selecao
  ("Brasil: Ronaldo 50'"), formato sem prefixo com lixo ("Publico:/Arbitro:"),
  formato invertido ("67', 79' Ronaldo"), minutos "90+4'", typos da fonte
  (`25'<`, `73''`, `(g. c.)`, "Substiuicoes") e mescla variantes de nome
  ("Ronaldinho" -> "Ronaldinho Gaucho"). `enrich_scorers` passou a ser aplicado a
  **todas** as edicoes: preenche os marcadores vazios do mata-mata moderno a
  partir das caixas 2x5 do cache (antes so 1934/1950/1954).
- **Gols contra nao viram artilheiro**: sao contados a parte e devolvidos em
  `DATA.gols_contra_selecao`, exibidos como nota na aba Por Selecao. Ajustes
  curados: `SCORERS_SUPPLEMENT` (gols dos jogos de desempate de 1934/1938, que
  nem constam da lista de partidas, e o 2o gol de Valdivia em 1970),
  `OWNGOALS_SUPPLEMENT` e `RECLASSIFY_OWNGOALS` (gols contra que a Wikipedia PT
  listou sem o marcador "(g.c.)" e que por isso apareciam como gol do jogador,
  ex.: Valladares/Yobo pela Franca em 2014). Com isso, jogadores + gols contra
  fecham **100%** com o "gols pro" de cada dupla (selecao, edicao).
- **Melhor ataque/defesa** (`build_best_atk_def`): ataque = selecao que mais
  marcou. Defesa = menor media de gols sofridos por jogo **entre as que passaram
  da fase de grupos** (4+ jogos) — o total cru premiava time eliminado na 1a
  fase que jogou pouco (ex.: Tunisia 2022 com 1 gol sofrido em 3 jogos).
- **Detalhes de partida** (`build_match_details`, helpers `_det_*`): cobre 1930,
  1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990,
  1994, 1998, 2002, 2006, 2010, 2014, 2018 e 2022, com todos os jogos casados
  em cada edicao.
  `_det_pages_for_year` define quais paginas da Wikipedia PT alimentam cada
  ano. Para 2010-2022, o fluxo usa paginas de grupos (A-H), fase final e, quando
  necessario, artigo dedicado da final. Para 1950-2002, a pagina principal da
  edicao ja traz as caixas de jogos; a final dedicada sobrescreve/completa os
  dados quando tem escalação. Para 1930, usa as subpaginas existentes dos
  grupos 1, 2 e 4, a pagina de fase final e a pagina principal; o Grupo 3 nao
  tem artigo proprio na Wikipedia PT e por isso usa ficha basica da pagina da
  edicao. Para 1938, o W.O. Suecia x Austria e o jogo Hungria x Indias Orientais
  Neerlandesas tambem recebem ficha basica quando a caixa detalhada nao e
  parseavel de forma confiavel. Para 2006, usa a pagina principal, paginas de
  grupos, a final dedicada e `Copa_do_Mundo_FIFA_de_2006_–_Fase_final`.
  O parser extrai scorebox (data/hora/estadio/publico/arbitro+pais) e as
  escalacoes quando o HTML traz tabelas de jogadores (titulares, quem entrou,
  treinador). O casamento com a partida do payload e por `det_pair_key` (times
  normalizados + placar), porque duas selecoes podem se enfrentar duas vezes na
  mesma Copa. O resultado fica em `p.ficha`; o front so le esse campo.
  `_det_parse_page` tambem aceita tabelas `Footballbox` sem `Público:` quando o
  `data-mw` identifica a predefinicao, necessario para alguns jogos de 1954.
  Limitacao documentada: em 1930-2002, a maioria dos jogos na Wikipedia PT nao
  traz escalacoes no mesmo formato das copas recentes; nesses casos a ficha abre
  com os metadados disponiveis (data/hora, estadio, publico, arbitro) e sem
  inventar escalação. Nesses anos, as finais dedicadas trazem escalações
  completas e sao aproveitadas quando disponiveis; 1950 tem final dedicada com
  metadados, mas sem escalação parseavel.

Como validar uma mudanca no dashboard das Copas:

1. Regerar com `python -u .\gerar_dashboard_copa_mundo_html.py`.
2. Checar o JS embutido. **Nao pegue o maior `<script>`**: o do Plotly (~3,5 MB)
   e maior que o da aplicacao (~1,9 MB). Selecione por um simbolo conhecido:

```python
import re
html = open("dashboard_copa_mundo.html", encoding="utf-8").read()
app = [s for s in re.findall(r"<script>(.*?)</script>", html, re.S) if "renderGeral" in s][0]
open("check.js", "w", encoding="utf-8").write(app)
# depois:  node --check check.js
```

3. Screenshot headless: as abas "Por Copa" e "Por Selecao" comecam ocultas. Faca
   uma **copia** do HTML e injete isto antes de `</body>` para abrir a aba:

```html
<script>state.view="selecao";state.team="Brasil";switchView();</script>
```

   Trocar so `state.view` **nao** basta: e o `switchView()` que alterna as
   classes `hidden`, chama o render e dispara o `resize` do Plotly (sem ele os
   graficos de abas ocultas renderizam com largura errada).

4. Conferencia de dados que pega quase tudo: para cada dupla (selecao, edicao), a
   soma dos gols de jogadores + gols contra a favor tem que bater com o `gp` da
   classificacao final. Hoje fecha **100%** nas edicoes concluidas.

Base analitica de gols das Copas:

- `gerar_gols_detalhados_statsbomb.py` cria
  `data/worldcup_wikipedia/gols_detalhados_statsbomb.json` e `.csv` a partir da
  StatsBomb Open Data. Essa fonte traz detalhe tecnico do chute, mas nao cobre
  todas as Copas nem todos os jogos antigos.
- `gerar_base_analitica_gols.py` cria
  `data/worldcup_wikipedia/gols_analiticos.json`, `.csv` e
  `gols_analiticos_auditoria.csv`.
- A base atual tem **3.027 gols**, com 2026 completa (308 gols).
- **383 gols** foram cruzados com detalhe tecnico StatsBomb.
- **633 gols** tem algum detalhe tecnico/oficial/inferido aproveitavel:
  StatsBomb, penalti/gol contra vindo do marcador, ou detalhe curado como falta,
  cabecada, voleio e gol olimpico.
- As 23 edicoes, 2026 inclusive, estao sem lacunas de autor de gol na
  auditoria atual (`gols_analiticos_auditoria.csv` so com o cabecalho).
- Ainda existem **2.394 gols sem detalhe fino** de finalizacao. Esses gols seguem
  como `Nao detalhado` para tipo tecnico, parte do corpo, zona e/ou distancia
  ate que haja fonte confiavel.
- Regras de identidade ja aplicadas na base de gols: `Ronaldo` de Portugal ->
  `Cristiano Ronaldo`; `Ronaldo` do Brasil -> `Ronaldo`; `Muller` alemao antes
  de 1974 -> `Gerd Muller`; `Muller` alemao moderno -> `Thomas Muller`;
  `Messi` -> `Lionel Messi`; `Mbappe` -> `Kylian Mbappe`.

Como regenerar a base de gols e o dashboard:

```powershell
python -u .\gerar_gols_detalhados_statsbomb.py
python -u .\gerar_base_analitica_gols.py
python -u .\gerar_dashboard_copa_mundo_html.py
```

Proximos passos principais (Copa do Mundo):

1. **Ampliar detalhes dos gols sem cobertura tecnica**: priorizar fontes
   rastreaveis para parte do corpo, falta, cabecada, chute de fora da area,
   assistencia e tipo de jogada. Nao converter ausencia de dado em negativa
   estatistica.
2. **Transformar a aba Gols em uma visao macro -> micro**: totais historicos,
   gols por jogo, edicoes, selecoes, jogadores, fases, estadios, minutos e,
   no menor nivel, cada gol com jogo, placar no momento, autor, adversario,
   minuto, tipo, assistencia quando existir, tecnica, parte do corpo, distancia,
   local no campo e fonte.
3. **Separar estatisticas oficiais e tecnicas**: gols oficiais, gols contra,
   penalties, artilheiros e gols por selecao/edicao/fase devem ficar separados
   dos detalhes StatsBomb. Ausencia de detalhe tecnico deve aparecer como
   `nao informado`, nunca como negativa estatistica.
4. **Cruzar mais fontes confiaveis**: Wikipedia PT/cache local segue como fonte
   operacional; StatsBomb entra para atributos tecnicos; RSSSF/FIFA/Wikidata
   entram para auditoria de totais, nomes canonicos, selecoes, jogadores e
   divergencias.
5. **Criar a visao Curiosidades** depois da auditoria da base de gols: gols mais
   cedo/tarde, viradas, gols em finais, artilheiros sem titulo, selecoes que mais
   dependeram de poucos jogadores, gols de reservas, capitaes, continentes e
   recortes por fase.
6. **Levar gols ao banco relacional** com nomes em portugues: expandir `gol` e
   avaliar tabelas `tipo_gol`, `detalhe_tecnico_gol`, `fonte_gol`,
   `auditoria_gol`, `evento_partida` e `alias_pessoa`, mantendo schema
   versionado, script criador, validacao e catalogo HTML.
7. **Melhorar o modal de partida**: uniformes/kits ainda nao implementados;
   padronizar codigos de posicao; avaliar cartoes, assistencias e substituicoes
   ao lado dos jogadores usando a mesma logica das bolinhas de gol.
8. **QA antes de commit**: rodar os scripts de gols/dashboard, checar o JS
   embutido com `node --check`, conferir gols de jogadores + gols contra contra
   `gp` por selecao/edicao e revisar `gols_analiticos_auditoria.csv`.

Pendencias tecnicas adicionais (Copa do Mundo):

- **Refinar detalhes das edicoes antigas**. A base de fichas ja cobre
  1930-2026, mas as edicoes ate 2002 tem formatos irregulares na Wikipedia PT.
  Refinar ano a ano, sempre conferindo:
  - se a pagina principal traz as caixas de jogos ou se existem subpaginas de
    grupo/fase final;
  - se ha artigo dedicado da final;
  - se as tabelas de escalação aparecem no mesmo formato parseavel pelos helpers
    `_det_*`;
  - se jogos repetidos entre as mesmas selecoes exigem chave com placar, como ja
    ocorre em `det_pair_key`;
  - se a edicao nao tem mata-mata tradicional (ex.: 1950), para nao forcar
    chaveamento artificial.
- **Uniforme (kit)**: pedido, porem **nao implementado**. Nao esta nas
  football-box do cache; aparece nos artigos dedicados de cada partida, como SVG.
- **Padronizar codigos de posicao**: paginas de grupo/fase final usam abreviacao
  em ingles (GK, CB, RB, CM, CF) e o artigo da final usa em portugues (G, Z, LD,
  M, A). Falta um mapa para uniformizar o modal.
- **Eventos na escalacao**: gols ja aparecem com bolinhas de futebol ao lado do
  jogador no modal. Cartoes, assistencias e substituicoes ainda podem ser
  avaliados depois, desde que venham de fonte confiavel e cacheada.
- **Reservas nao utilizados nao aparecem** (a Wikipedia so lista quem entrou) e
  **arbitros assistentes** nao constam das caixas de 2022.
- **Pais do arbitro** as vezes vem em pt-PT ("Polonia" grafada diferente). Se for
  exibir bandeira, normalize antes de bater com `FLAG_CODES`.
- **`ARTILHEIROS_HISTORICO` e curado**: revisado com a Copa de 2026 encerrada
  (Mbappe 22, Messi 21, Kane 14, Cristiano Ronaldo 11). Na proxima Copa,
  conferir os artilheiros em atividade contra `gols_analiticos.csv`.
- **Fichas de 2026 sem escalacao**: a pagina da edicao so traz data, hora,
  estadio, publico e arbitro. Escalacoes dependeriam das paginas de grupo ou
  da final dedicada, quando existirem na Wikipedia PT.
- **Lacunas residuais conhecidas** ja resolvidas por dados curados, mas que voltam
  se o cache for refeito: os jogos de desempate de 1934/1938 **nao existem** na
  lista de partidas da Wikipedia PT (so na classificacao), por isso seus gols
  entram por `SCORERS_SUPPLEMENT` e nao aparecem em "Todos os jogos".

Dashboard gerado por:

- `gerar_dashboard_html.py`

Pipeline normal:

- `build.py`

O banco atual contem:

- Serie A em pontos corridos de 2003 a 2025.
- Dados de jogos, gols, cartoes, estatisticas, classificacao por rodada e
  classificacao final historica para o periodo moderno.
- Copa do Brasil: campeoes, vices, finais, edicoes e participantes.
- Historico do Campeonato Brasileiro antigo, antes dos pontos corridos, ja
  importado de 1971 (primeiro Campeonato Nacional) a 2002, mais as edicoes
  anteriores reconhecidas pela CBF: Copa dos Campeoes Estaduais 1937,
  Taca Brasil 1959-1968 e Robertao
  (Torneio Roberto Gomes Pedrosa) 1967-1970. Em 1967 e 1968 ha duas
  edicoes no mesmo ano; o seletor da aba Brasileiro Antigo escolhe pela
  edicao ("1967 · Taca Brasil", "1967 · Torneio Roberto Gomes Pedrosa").

Historico nacional ja importado no bloco "Historico > Brasileiro Antigo":

| Ano | Participantes | Fases | Jogos |
| --- | ---: | ---: | ---: |
| 1937 | 6 | 2 | 14 |
| 1959 | 16 | 4 | 35 |
| 1960 | 17 | 4 | 37 |
| 1961 | 18 | 4 | 38 |
| 1962 | 18 | 4 | 39 |
| 1963 | 20 | 4 | 45 |
| 1964 | 22 | 4 | 49 |
| 1965 | 22 | 5 | 48 |
| 1966 | 22 | 4 | 47 |
| 1967 (Taca Brasil) | 21 | 6 | 61 |
| 1967 (Robertao) | 15 | 2 | 117 |
| 1968 (Taca Brasil) | 21 | 6 | 53 |
| 1968 (Robertao) | 17 | 2 | 142 |
| 1969 | 17 | 2 | 142 |
| 1970 | 17 | 2 | 142 |
| 1971 | 20 | 3 | 229 |
| 1972 | 26 | 4 | 352 |
| 1973 | 40 | 3 | 656 |
| 1974 | 40 | 4 | 447 |
| 1975 | 42 | 6 | 430 |
| 1976 | 54 | 6 | 411 |
| 1977 | 62 | 6 | 485 |
| 1978 | 74 | 7 | 792 |
| 1979 | 94 | 5 | 583 |
| 1980 | 44 | 6 | 307 |
| 1981 | 44 | 6 | 306 |
| 1982 | 44 | 7 | 291 |
| 1983 | 44 | 7 | 322 |
| 1984 | 41 | 7 | 310 |
| 1985 | 44 | 4 | 517 |
| 1986 | 48 | 6 | 538 |
| 1987 | 18 | 4 | 128 |
| 1988 | 24 | 4 | 290 |
| 1989 | 22 | 4 | 195 |
| 1990 | 20 | 4 | 204 |
| 1991 | 20 | 3 | 196 |
| 1992 | 20 | 3 | 216 |
| 1993 | 32 | 4 | 254 |
| 1994 | 24 | 6 | 310 |
| 1995 | 24 | 4 | 282 |
| 1996 | 24 | 4 | 290 |
| 1997 | 26 | 3 | 351 |
| 1998 | 24 | 4 | 297 |
| 1999 | 22 | 4 | 250 |
| 2000 | 29 | 5 | 330 |
| 2001 | 28 | 4 | 386 |
| 2002 | 26 | 4 | 339 |

Totais do historico antigo importado:

- 47 edicoes: Copa dos Campeoes 1937, Taca Brasil 1959-1968, Robertao
  1967-1970 e Campeonato Brasileiro 1971-2002 (todas as reconhecidas pela
  CBF ate 2002).
- 206 fases.
- 12.303 partidas.

Todas as 47 edicoes (1937 a 2002) ficam na pasta `historico/`:
`historico/edicoes.py` tem a configuracao de cada edicao (dicionario
`EDICOES`) e o comando que importa; `historico/base.py` le, confere e grava.
Cada edicao so declara os cortes do texto da fonte (`Fase(nome, inicio,
fim, tipo, jogos)`), os nomes de clube daquele ano (`nomes`, que valem so
enquanto a edicao roda) e os ajustes de erros da fonte. As paginas que fogem
do desenho comum (1994-2002) tem um leitor proprio (`ler=_ler_<ano>`) no
mesmo arquivo. A base confere a
contagem de jogos de cada fase e exige que os participantes sejam exatamente
os clubes da classificacao final ja existente no banco. Os tres anos batem
clube a clube (J/V/E/D/GP/GC) com a "Final Table" da RSSSF; repescagens e
desempates que a fonte nao soma ficam fora dessa conta. Ajustes conhecidos
(funcao `_ajustar_<edicao>` em `historico/edicoes.py`):

- 1983: a volta Sao Paulo 0-1 Athletico-PR (quartas) vem invertida na RSSSF
  e e corrigida.
- 1980: o desempate Guarani 3-2 America-RJ (2o lugar do grupo I) fica numa
  fase propria, "Desempate", para nao entrar na tabela do grupo.
- 1979: "Sao Paulo-RS 1-0 Goias" era contra o Goytacaz (erro de digitacao);
  jogo do tribunal (Sao Paulo-RS x Operario-PR) e os dois W.O. do Atletico-MG
  na terceira fase gravados como 1-0 para quem ganhou os pontos (a RSSSF os
  conta sem gols, entao esses clubes ficam com 1 gol de diferenca).
- 1978: volta Santa Cruz 1-2 Internacional (quartas) invertida na fonte;
  "Juventude 1-1 America-SP" era contra o America-RJ; Operario de Campo
  Grande escrito "-MT" vira Operario-MS.
- 1977: Desportiva x Fluminense-BA, abandonado (suborno), contado 0-0 como
  na RSSSF. A temporada vai a marco de 1978 (campo `virada` da edicao).
- 1975 a 1978: vitoria por saldo grande valia 3 pontos (2 gols ou mais em
  1975; 3 ou mais em 1976-1978); o dashboard conta 2 por vitoria (a regra
  fica no criterio da fase).
- 1976: dois jogos vem colados na linha dos autores ("[Cedenir]Palmeiras
  1-0 Rio Branco"); a base separa.
- 1975: a pagina nao tem "Final Table"; a edicao passa `corte_final`.
  Os grupos A/B e C/D da primeira fase e 1/2 da segunda jogaram contra o
  outro grupo, por isso aparecem juntos.
- 1974: "America-GB" (Guanabara) e o America-RJ.
- Taca Brasil (1959-1966, paginas `brazcupAA.html` da RSSSF): mata-mata em
  ida e volta com jogo de desempate, lido pelo leitor misto (`Fase(...,
  misto=True)`). Fases no painel: Zona Norte, Zona Sul (grupos regionais e
  decisao da zona), Quartas (so 1965), Semifinal e Final. O desempate fica
  com a observacao "Jogo de desempate (playoff)."; um terceiro jogo entre
  os mesmos clubes logo depois da ida e volta tambem conta como desempate.
  Sem tabela final na fonte: a conferencia e a lista de clubes contra a
  classificacao do banco. 1962 e 1963 tem `virada` (finais em 1963 e 1964).
- 1967 e 1968: edicoes `1967_taca_brasil`, `1967_robertao` etc., com
  `edicao` = edicao_id; o CSV de auditoria leva o mesmo nome. As
  regras de fase usam a chave (edicao_id, fase) em `regras_historicas.py`.
  A Taca Brasil de 1967-1968 tem tambem a Zona Central; a de 1968 tem
  triangulares regionais (turno e returno) que aparecem como confrontos e
  terminou em outubro de 1969 (datas "/69"; o ano da 2a data de um par
  vale para a 1a). O Robertao de 1967 vem de varios blocos <pre> em
  portugues (`blocos_pre=[0, 2]`; o bloco do "Title match" repete o jogo
  do titulo). No Robertao de 1968 a tabela da fonte tem 1 gol a menos no
  Botafogo 4-2 Nautico, que tem os seis autores listados.
- 1937: sem pagina na RSSSF nem no RSSSF Brasil ("o arquivo para este
  torneio ainda nao foi criado"). Os 14 jogos estao escritos na propria
  edicao (`JOGOS_1937`), tirados da Wikipedia PT (mesma fonte da classificacao no
  banco), que cita O Globo, Jornal do Brasil e Correio da Manha de 1937; eles
  fecham exatamente com a tabela do quadrangular. A Wikipedia em ingles
  diverge (datas e Rio Branco 3-1 Portuguesa) e nao fecha.
- Robertao 1967-1970: jogos do RSSSF Brasil (`rsssfbrasil_rgpAAAA.htm`,
  formato "TIME 1 x 0 TIME", datas 06.09.1969). A RSSSF nao tem os jogos de
  1969, e a lista de 1970 dela tem placares que nao fecham com a tabela dela
  mesma; a do RSSSF Brasil fecha em todos os clubes.
- Edicoes que nao sao o "Campeonato Brasileiro" do ano sao escolhidas pelo
  `edicao` (dim_edicao_nacional.edicao_id) da configuracao.
- 1972: ABC 2-1 Botafogo teve os pontos dados ao Botafogo (sem "awd" na
  fonte); gravado 0-1 em `_ajustar_1972`.
- 1971 e 1973: a fonte nao numera as rodadas da primeira fase (so datas),
  entao a corrida da lideranca desses anos fica sem rodadas. 1972, 1973 e
  1975 nao tem "Final Table"; 1971 numera as tabelas com ponto ("1.Time").
  1973 vai a fevereiro de 1974 (`virada`).
- "XV de Novembro" sem cidade e "Operario" sem estado mudam de clube
  conforme o ano: cada importador define no seu `CANONICAL` (XV: 1982 = Jau,
  1977-1978 = Piracicaba; Operario: 1976-1977 = Operario-MS).

Diferencas que sao da propria tabela final da RSSSF (os jogos batem com as
tabelas de grupo dela): 1981, Ponte Preta com 1 gol a mais de cada lado;
1982, Londrina com o 0-0 da repescagem somado so para ele; 1979, River-PI e
Uberlandia com V/E/D que nao fecham com os jogos, e Central 0-0 Vasco contado
como vitoria do Vasco sem nota na fonte; 1977, Flamengo-PI (3 gols) e
Vitoria-ES (1 jogo) a mais na tabela final. Jogos decididos
no tribunal ("awd") usam o placar atribuido, com o original na observacao.

## Revisao estrutural do Brasileiro antigo (2026-06)

Uma auditoria multi-agente (verificacao ano a ano contra o RSSSF local +
corroboracao independente; registro completo em
`docs/auditoria_brasileiro_antigo_1992_2002.md`) mostrou que placares e campeoes
estavam corretos, mas a ESTRUTURA de varias edicoes estava achatada na
importacao. O que foi corrigido nesta revisao:

Dados e modelagem:

- Pontuacao por epoca: 2 pontos por vitoria ate 1994 e 3 a partir de 1995
  (antes o dashboard reconstruia toda tabela com 3 pts).
- Grupos paralelos viraram dado real (coluna `grupo`), derivados por
  componentes conexos: 1992 (2 quadrangulares), 1993 (4 grupos + 2 grupos),
  1994 (4 grupos) e 1997 (2 grupos do "Grupo semifinal").
- 1995: os dois "turnos" formam um turno unico (todos contra todos); a tabela
  passou a ser combinada (antes o dashboard mostrava so metade da temporada).
- Metadados de fase estruturados: `num_grupos`, `formato_serie`
  (`pontos_corridos`/`grupos`/`jogo_unico`/`ida_volta`/`melhor_de_3`) e
  `criterio` (melhor campanha, melhor de 3, replays, W.O., etc.).
- Confirmado que NAO ha mojibake nos nomes de clube de 1991-2002 (os acentos
  estao integros; `?`/quadrado aparece so no console, nao no dado).

Design e render (aba "Brasileiro Antigo"):

- Render dirigido pelo TIPO de fase (`liga`/`grupo`/`mata_mata`), em vez de
  assumir sempre "liga + chaveamento".
- Classificacao POR GRUPO (uma mini-tabela por grupo) nas fases de grupos.
- Stepper com o caminho ate o titulo; agora TODA fase aparece (antes fases de
  grupo decisivas, como o "Grupo semifinal" de 1997, sumiam).
- Bracket em funil agrupando confrontos por par de clubes, tratando jogo unico,
  ida/volta e melhor de 3; coluna-trofeu do campeao.
- Desempate de final empatada usa a classificacao oficial; nao elege o
  visitante por engano.
- Banner do campeao com o criterio do titulo; pontos por epoca nas tabelas.

Limitacao conhecida: a 2a fase e a Repescagem de 1994 tem clubes que se cruzam
entre subfases, entao ficaram como grupo unico (sem separacao A/B/E/F), com nota.

A implementacao mora em `regras_historicas.py` + `enriquecer_historico.py`
(camada de dados, abaixo) e nas funcoes `renderHN*` de `gerar_dashboard_html.py`
(render). Os anos de 1971 a 1991 ja foram importados dentro desse padrao.

Nota especifica de 1986: a RSSSF lista tambem grupos inferiores/regionais, mas
o banco local e a classificacao final existente usam 48 clubes. O importador
carrega os grupos A-D completos e os quatro vencedores dos grupos E-H que entram
na segunda fase (Treze, Central, Internacional-SP e Criciuma), mantendo o mesmo
recorte da classificacao final.

Nota especifica de 1987: o banco segue a classificacao final oficial ja
existente no projeto (Sport, Guarani, Flamengo, Internacional, ...). O importador
carrega o Modulo Verde/Copa Uniao completo e a decisao CBF Sport x Guarani como
fase final separada; o Modulo Amarelo completo nao e misturado como Serie A.

## Requisitos

- Python 3.12+
- Dependencias Python listadas em `requirements.txt`
- Node.js para validar a sintaxe do JavaScript embutido no dashboard com
  `node --check`

Instalacao:

```powershell
python -m pip install -r requirements.txt
```

O projeto inclui `pyproject.toml` com configuracao basica para Black e Ruff.

## Arquivos Principais

### Dashboard e Pipeline

- `dashboard.html`
  - Arquivo HTML final, pronto para abrir no navegador.
  - E grande porque embute o payload de dados em JavaScript.
  - Deve ser regenerado depois de alteracoes no banco.

- `gerar_dashboard_html.py`
  - Le `db/brasileirao.db`.
  - Monta o objeto `DATA` usado pelo front-end.
  - Gera `dashboard.html`.
  - Inclui as abas modernas e a aba historica "Historico > Brasileiro Antigo".

- `check_dashboard.py`
  - Valida se `dashboard.html` contem volumes minimos esperados.
  - Confere, por exemplo, jogos, gols, cartoes, estatisticas, classificacao e
    dados de Copa do Brasil.

- `build.py`
  - Fluxo normal: valida o banco existente e gera o dashboard.
  - Fluxo opcional: recria o banco a partir de fontes locais com
    `--rebuild-from-sources`.
  - Importante: o rebuild por fontes ainda nao reexecuta automaticamente os
    importadores do historico antigo 1990-2002. Veja a secao "Rebuild completo".

- `validar_banco.py`
  - Valida campeoes, rebaixados e sanidade basica do banco moderno.
  - Deve passar antes de commitar alteracoes no banco/dashboard.

### Backup e Restauracao

- `backup.py`
  - Cria backup dos artefatos criticos.
  - Sempre execute antes de qualquer importacao ou alteracao no banco.

- `restore_backup.py`
  - Lista e restaura backups locais.
  - Requer confirmacao explicita.

Exemplo:

```powershell
python -u .\backup.py
python -u .\restore_backup.py
python -u .\restore_backup.py <nome_do_backup> --confirm
```

### Banco Moderno 2003+

- `criar_banco_brasileirao.py`
  - Recria `db/brasileirao.db` a partir dos CSVs em `data/`.
  - Usado somente em rebuild explicito.

- `importar_classificacao_historica_brasileirao.py`
  - Importa classificacoes finais historicas para o banco.
  - Depende de `classificacao_codex.xlsx` na raiz do projeto.

- `importar_finais_copa_brasil.py`
  - Importa campeoes, vices e partidas finais da Copa do Brasil.

- `importar_edicoes_copa_brasil.py`
  - Importa metadados e participantes por edicao da Copa do Brasil.

### Importadores do Brasileiro Antigo

Preenchem o bloco historico nacional antes de 2003: participantes, fases e
partidas de cada edicao nas tabelas historicas do banco. Desde 13/11/2026 sao
dois arquivos so (antes era um script por ano):

- `historico/edicoes.py` — configuracao das 47 edicoes e o comando:
  `python historico/edicoes.py 1994` (uma ou varias; `1967` pega Taca Brasil
  e Robertao), `--todos` (todas, em ordem) e `--lista`.
- `historico/base.py` — leitura da RSSSF, nomes de clube (`CANONICAL`),
  conferencias e gravacao.

Como funciona:

- Le HTML local em `data/rsssf_*.html` (nao baixa a fonte; o HTML deve estar
  em `data/`).
- Normaliza nomes de clubes com `CANONICAL` (comum) e `nomes` (da edicao).
- Confere a contagem de jogos por fase e exige que os participantes sejam os
  clubes da classificacao final ja existente no banco.
- Apaga e reinsere apenas os dados historicos daquela edicao.
- Escreve um CSV de auditoria por edicao em
  `data/brasileirao_historico_<edicao>_partidas.csv`.

Tabelas usadas pelos importadores historicos:

- `dim_edicao_nacional`
- `dim_fase_nacional_historica`
- `fato_participante_nacional_historico`
- `fato_partida_nacional_historica`
- `dim_clube`

A gravacao chama `create_tables(con)` de `historico/base.py`, garantindo que
as tabelas historicas existam antes da importacao.

### Camada estrutural (grupos, criterios, pontos)

Os importadores guardam corretamente placares e fases, mas o formato do
RSSSF nao expoe grupos paralelos, criterio de titulo nem a regra de pontos da
epoca. Essa camada e preenchida por dois arquivos, de forma idempotente e
reproduzivel (auditada em 2026-06; veja `docs/auditoria_brasileiro_antigo_1992_2002.md`):

- `regras_historicas.py`
  - Metadados curados por ano/fase: `num_grupos`, `formato_serie`
    (`pontos_corridos`/`grupos`/`jogo_unico`/`ida_volta`/`melhor_de_3`),
    `criterio` (como a fase decide) e `pontos_vitoria` (2 ate 1994, 3 depois).

- `enriquecer_historico.py`
  - Migra o schema (ALTER TABLE idempotente), grava os metadados das fases e a
    pontuacao da edicao, e **deriva o grupo de cada partida por componentes
    conexos** dos confrontos da fase (os grupos sao disjuntos no calendario),
    rotulando A, B, C... de forma estavel.
  - Roda automaticamente dentro de `build.py` (passo "Enriquecendo Brasileiro
    antigo"); pode ser desligado com `--skip-enriquecimento`.
  - Pode rodar isolado: `python -u .\enriquecer_historico.py`.

Colunas novas (ja no `sql/schema.sql` e no `create_tables`):

- `dim_edicao_nacional.pontos_vitoria`
- `dim_fase_nacional_historica.num_grupos`, `.formato_serie`, `.criterio`
- `fato_partida_nacional_historica.grupo`

Regra importante: sempre rode `enriquecer_historico.py` (ou `build.py`) depois
de reimportar qualquer ano historico, senao os grupos/criterios ficam vazios.

## Fontes Usadas

### Fonte principal para 1959-2002

Taca Brasil: `https://www.rsssf.org/tablesb/brazcup59.html` a `brazcup68.html`.
Robertao: `https://rsssfbrasil.com/tablesr/rgp1967.htm` a `rgp1970.htm`.

Copa dos Campeoes 1937: `https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1937`.

Campeonato Brasileiro 1971-2002:

RSSSF Brasil:

- `https://www.rsssf.org/tablesb/braz71.html`
- `https://www.rsssf.org/tablesb/braz72.html`
- `https://www.rsssf.org/tablesb/braz73.html`
- `https://www.rsssf.org/tablesb/braz74.html`
- `https://www.rsssf.org/tablesb/braz75.html`
- `https://www.rsssf.org/tablesb/braz76.html`
- `https://www.rsssf.org/tablesb/braz77.html`
- `https://www.rsssf.org/tablesb/braz78.html`
- `https://www.rsssf.org/tablesb/braz79.html`
- `https://www.rsssf.org/tablesb/braz80.html`
- `https://www.rsssf.org/tablesb/braz81.html`
- `https://www.rsssf.org/tablesb/braz82.html`
- `https://www.rsssf.org/tablesb/braz83.html`
- `https://www.rsssf.org/tablesb/braz84.html`
- `https://www.rsssf.org/tablesb/braz85.html`
- `https://www.rsssf.org/tablesb/braz86.html`
- `https://www.rsssf.org/tablesb/braz87.html`
- `https://www.rsssf.org/tablesb/braz88.html`
- `https://rsssfbrasil.com/tablesae/br1988.htm` (espelho/fonte auxiliar; 1988 tambem exigiu curadoria de um jogo ausente na RSSSF principal)
- `https://www.rsssf.org/tablesb/braz89.html`
- `https://rsssfbrasil.com/tablesae/br1989.htm` (fonte auxiliar para validar lacunas do torneio de rebaixamento de 1989)
- `https://www.rsssf.org/tablesb/braz90.html`
- `https://www.rsssf.org/tablesb/braz91.html`
- `https://www.rsssf.org/tablesb/braz92.html`
- `https://www.rsssf.org/tablesb/braz93.html`
- `https://www.rsssf.org/tablesb/braz94.html`
- `https://www.rsssf.org/tablesb/braz95.html`
- `https://www.rsssf.org/tablesb/braz96.html`
- `https://www.rsssf.org/tablesb/braz97.html`
- `https://www.rsssf.org/tablesb/braz98.html`
- `https://www.rsssf.org/tablesb/braz99.html`
- `https://www.rsssf.org/tablesb/braz_joao00.html`
- `https://www.rsssf.org/tablesb/braz01.html`
- `https://www.rsssf.org/tablesb/braz02.html`

Arquivos locais baixados dessas fontes:

- `data/rsssf_braz90.html`
- `data/rsssf_braz91.html`
- `data/rsssf_braz92.html`
- `data/rsssf_braz93.html`
- `data/rsssf_braz94.html`
- `data/rsssf_braz95.html`
- `data/rsssf_braz96.html`
- `data/rsssf_braz97.html`
- `data/rsssf_braz98.html`
- `data/rsssf_braz99.html`
- `data/rsssf_braz_joao00.html`
- `data/rsssf_braz01.html`
- `data/rsssf_braz02.html`

Exemplo de download:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/braz91.html" -o data\rsssf_braz91.html
```

### Fontes usadas em outras frentes do projeto

Para lacunas do Brasileirao moderno e validacao manual de partidas:

- oGol: `https://www.ogol.com.br/`
  - Usado para conferir escalacoes, treinadores, gols, cartoes e substituicoes
    quando disponivel.
  - Foi especialmente util para partidas antigas com informacoes de gols e
    treinadores.

- Transfermarkt
  - Usado como fonte complementar para treinador, esquema tatico, substituicoes,
    cartoes e eventos de partida.
  - Exemplo de pagina usada como referencia:
    `https://www.transfermarkt.pt/gremio-barueri-futebol-ltda-_santos-fc/index/spielbericht/1006319`

- ESPN
  - Indicada como fonte auxiliar para temporadas intermediarias quando o dado
    nao aparece em Transfermarkt/oGol.

- Base local e planilhas de lacunas
  - Arquivos `lacunas_*.xlsx` e relatorios em `docs/` foram usados para listar
    o que ainda faltava pesquisar manualmente.

Para classificacoes historicas e Copa do Brasil:

- `classificacao_codex.xlsx`
- wikitextos/HTML locais em `data/`
- paginas RSSSF e paginas historicas consultadas durante a montagem dos dados.

## Arquivos de Auditoria Gerados

Cada edicao importada gera um CSV com os jogos importados. Esses arquivos
servem para revisao humana e para comparar o que entrou no banco.

Arquivos atuais: `data/brasileirao_historico_<edicao>_partidas.csv`, um por
edicao de 1937 a 2002 (ex.: `..._1994_partidas.csv`,
`..._1967_robertao_partidas.csv`). 1998-1999 e 2000-2001, que antes saiam
juntos num CSV so, agora tem um CSV por ano.

Formato comum:

- `temporada`
- `fase`
- `rodada`
- `jogo`
- `data`
- `mandante`
- `placar`
- `visitante`
- `observacao`
- `fonte`

## Fases Importadas no Brasileiro Antigo

Resumo por ano e fase:

| Ano | Fase | Tipo | Jogos |
| --- | --- | --- | ---: |
| 1937 | Fase preliminar | mata_mata | 2 |
| 1937 | Quadrangular final | grupo | 12 |
| 1959 | Zona Norte | mata_mata | 17 |
| 1959 | Zona Sul | mata_mata | 10 |
| 1959 | Semifinal | mata_mata | 5 |
| 1959 | Final | mata_mata | 3 |
| 1960 | Zona Norte | mata_mata | 16 |
| 1960 | Zona Sul | mata_mata | 15 |
| 1960 | Semifinal | mata_mata | 4 |
| 1960 | Final | mata_mata | 2 |
| 1961 | Zona Norte | mata_mata | 15 |
| 1961 | Zona Sul | mata_mata | 16 |
| 1961 | Semifinal | mata_mata | 5 |
| 1961 | Final | mata_mata | 2 |
| 1962 | Zona Norte | mata_mata | 21 |
| 1962 | Zona Sul | mata_mata | 10 |
| 1962 | Semifinal | mata_mata | 5 |
| 1962 | Final | mata_mata | 3 |
| 1963 | Zona Norte | mata_mata | 23 |
| 1963 | Zona Sul | mata_mata | 16 |
| 1963 | Semifinal | mata_mata | 4 |
| 1963 | Final | mata_mata | 2 |
| 1964 | Zona Norte | mata_mata | 23 |
| 1964 | Zona Sul | mata_mata | 20 |
| 1964 | Semifinal | mata_mata | 4 |
| 1964 | Final | mata_mata | 2 |
| 1965 | Zona Norte | mata_mata | 21 |
| 1965 | Zona Sul | mata_mata | 16 |
| 1965 | Quartas de final | mata_mata | 5 |
| 1965 | Semifinal | mata_mata | 4 |
| 1965 | Final | mata_mata | 2 |
| 1966 | Zona Norte | mata_mata | 21 |
| 1966 | Zona Sul | mata_mata | 19 |
| 1966 | Semifinal | mata_mata | 5 |
| 1966 | Final | mata_mata | 2 |
| 1969 | Primeira fase | liga | 136 |
| 1969 | Fase final | grupo | 6 |
| 1970 | Primeira fase | liga | 136 |
| 1970 | Fase final | grupo | 6 |
| 1971 | Primeira fase | liga | 190 |
| 1971 | Segunda fase | grupo | 36 |
| 1971 | Triangular final | grupo | 3 |
| 1972 | Primeira fase | liga | 325 |
| 1972 | Segunda fase | grupo | 24 |
| 1972 | Semifinal | mata_mata | 2 |
| 1972 | Final | mata_mata | 1 |
| 1973 | Primeira fase | liga | 560 |
| 1973 | Segunda fase | grupo | 90 |
| 1973 | Quadrangular final | grupo | 6 |
| 1974 | Primeira fase | grupo | 380 |
| 1974 | Fase semifinal | grupo | 60 |
| 1974 | Fase final | grupo | 6 |
| 1974 | Final | mata_mata | 1 |
| 1975 | Primeira fase | grupo | 221 |
| 1975 | Segunda fase | grupo | 100 |
| 1975 | Repescagem | grupo | 50 |
| 1975 | Terceira fase | grupo | 56 |
| 1975 | Semifinal | mata_mata | 2 |
| 1975 | Final | mata_mata | 1 |
| 1976 | Primeira fase | grupo | 216 |
| 1976 | Segunda fase | grupo | 60 |
| 1976 | Repescagem | grupo | 60 |
| 1976 | Terceira fase | grupo | 72 |
| 1976 | Semifinal | mata_mata | 2 |
| 1976 | Final | mata_mata | 1 |
| 1977 | Primeira fase | grupo | 290 |
| 1977 | Segunda fase | grupo | 60 |
| 1977 | Repescagem | grupo | 70 |
| 1977 | Fase final | grupo | 60 |
| 1977 | Semifinal | mata_mata | 4 |
| 1977 | Final | mata_mata | 1 |
| 1978 | Primeira fase | grupo | 420 |
| 1978 | Segunda fase | grupo | 144 |
| 1978 | Repescagem | grupo | 102 |
| 1978 | Terceira fase | grupo | 112 |
| 1978 | Quartas de final | mata_mata | 8 |
| 1978 | Semifinal | mata_mata | 4 |
| 1978 | Final | mata_mata | 2 |
| 1979 | Primeira fase | grupo | 359 |
| 1979 | Segunda fase | grupo | 194 |
| 1979 | Terceira fase | grupo | 24 |
| 1979 | Semifinal | mata_mata | 4 |
| 1979 | Final | mata_mata | 2 |
| 1980 | Primeira fase | grupo | 180 |
| 1980 | Segunda fase | grupo | 96 |
| 1980 | Desempate | mata_mata | 1 |
| 1980 | Terceira fase | grupo | 24 |
| 1980 | Semifinal | mata_mata | 4 |
| 1980 | Final | mata_mata | 2 |
| 1981 | Primeira fase | grupo | 180 |
| 1981 | Segunda fase | grupo | 96 |
| 1981 | Oitavas de final | mata_mata | 16 |
| 1981 | Quartas de final | mata_mata | 8 |
| 1981 | Semifinal | mata_mata | 4 |
| 1981 | Final | mata_mata | 2 |
| 1982 | Primeira fase | grupo | 160 |
| 1982 | Repescagem | mata_mata | 4 |
| 1982 | Segunda fase | grupo | 96 |
| 1982 | Terceira fase | mata_mata | 16 |
| 1982 | Quarta fase | mata_mata | 8 |
| 1982 | Semifinal | mata_mata | 4 |
| 1982 | Final | mata_mata | 3 |
| 1983 | Primeira fase | grupo | 160 |
| 1983 | Playoff | mata_mata | 4 |
| 1983 | Segunda fase | grupo | 96 |
| 1983 | Terceira fase | grupo | 48 |
| 1983 | Quartas de final | mata_mata | 8 |
| 1983 | Semifinal | mata_mata | 4 |
| 1983 | Final | mata_mata | 2 |
| 1984 | Primeira fase | grupo | 160 |
| 1984 | Repescagem | mata_mata | 4 |
| 1984 | Segunda fase | grupo | 84 |
| 1984 | Terceira fase | grupo | 48 |
| 1984 | Quartas de final | mata_mata | 8 |
| 1984 | Semifinal | mata_mata | 4 |
| 1984 | Final | mata_mata | 2 |
| 1985 | Primeira fase | grupo | 464 |
| 1985 | Segunda fase | grupo | 48 |
| 1985 | Semifinal | mata_mata | 4 |
| 1985 | Final | mata_mata | 1 |
| 1990 | Primeira fase | liga | 190 |
| 1990 | Quartas de final | mata_mata | 8 |
| 1990 | Semifinal | mata_mata | 4 |
| 1990 | Final | mata_mata | 2 |
| 1991 | Primeira fase | liga | 190 |
| 1991 | Semifinal | mata_mata | 4 |
| 1991 | Final | mata_mata | 2 |
| 1992 | Primeira fase | liga | 190 |
| 1992 | Segunda fase | grupo | 24 |
| 1992 | Final | mata_mata | 2 |
| 1993 | Primeira fase | grupo | 224 |
| 1993 | Playoff | mata_mata | 4 |
| 1993 | Segunda fase | grupo | 24 |
| 1993 | Final | mata_mata | 2 |
| 1994 | Primeira fase | grupo | 120 |
| 1994 | Segunda fase | grupo | 120 |
| 1994 | Repescagem | grupo | 56 |
| 1994 | Quartas de final | mata_mata | 8 |
| 1994 | Semifinal | mata_mata | 4 |
| 1994 | Final | mata_mata | 2 |
| 1995 | Primeiro turno | liga | 132 |
| 1995 | Segundo turno | liga | 144 |
| 1995 | Semifinal | mata_mata | 4 |
| 1995 | Final | mata_mata | 2 |
| 1996 | Primeira fase | liga | 276 |
| 1996 | Quartas de final | mata_mata | 8 |
| 1996 | Semifinal | mata_mata | 4 |
| 1996 | Final | mata_mata | 2 |
| 1997 | Primeira fase | liga | 325 |
| 1997 | Grupo semifinal | grupo | 24 |
| 1997 | Final | mata_mata | 2 |
| 1998 | Primeira fase | liga | 276 |
| 1998 | Quartas de final | mata_mata | 12 |
| 1998 | Semifinal | mata_mata | 6 |
| 1998 | Final | mata_mata | 3 |
| 1999 | Primeira fase | liga | 231 |
| 1999 | Quartas de final | mata_mata | 11 |
| 1999 | Semifinal | mata_mata | 5 |
| 1999 | Final | mata_mata | 3 |
| 2000 | Modulo Azul | liga | 300 |
| 2000 | Oitavas de final | mata_mata | 16 |
| 2000 | Quartas de final | mata_mata | 8 |
| 2000 | Semifinal | mata_mata | 4 |
| 2000 | Final | mata_mata | 2 |
| 2001 | Primeira fase | liga | 378 |
| 2001 | Quartas de final | mata_mata | 4 |
| 2001 | Semifinal | mata_mata | 2 |
| 2001 | Final | mata_mata | 2 |
| 2002 | Primeira fase | liga | 325 |
| 2002 | Quartas de final | mata_mata | 8 |
| 2002 | Semifinal | mata_mata | 4 |
| 2002 | Final | mata_mata | 2 |

## Como Continuar a Expansao Historica

Todas as edicoes reconhecidas pela CBF ate 2002 tem jogos no banco, de 1937
(Copa dos Campeoes Estaduais) a 2002. Proximo passo natural, se houver:
o Brasileirao de 2026, quando a temporada terminar.

Uma edicao nova vira uma entrada em `EDICOES` (`historico/edicoes.py`), com
as fases como cortes do texto da fonte; veja `EDICOES["1984"]` como modelo.
Importar: `python historico/edicoes.py 1984` (ou `--todos`, ou `--lista`).

Fluxo para cada novo ano:

1. Backup: `python -u .\backup.py`.
2. Baixar a pagina:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/<pagina>.html" -o data\rsssf_<pagina>.html
```

3. Ler a pagina (o texto fica dentro de `<pre>`, em latin-1) e anotar a
   estrutura: fases, grupos, jogos por fase, repescagens/playoffs e onde comeca
   a segunda divisao (Taca de Prata/Taca CBF), que fica de fora; a leitura ja
   para em "Final Table".
4. Conferir quantos clubes a classificacao final do banco tem para o ano
   (`fato_classificacao_final_nacional`): os participantes lidos precisam ser
   exatamente esses.
5. Acrescentar a edicao em `EDICOES` (`historico/edicoes.py`) com a lista de fases
   (`Fase(nome, inicio, fim, tipo, jogos, ida_volta=...)`) e o total de jogos.
   Nomes que nao batem com `dim_clube` entram em `nomes` (so aquele ano) ou
   no `CANONICAL.update` de `historico/base.py` (todos os anos).
   Erro de placar conhecido da fonte vai em `ajustar` (ver 1983, 1980 e 1979). Jogos "awd", "dns" e "abd" sem placar na
   fonte barram o import ate o `ajustar` da edicao dizer o placar.
6. Antes de gravar, conferir clube a clube contra a "Final Table" da RSSSF
   (J/V/E/D/GP/GC somados dos jogos lidos). Fases que a fonte nao soma, como a
   repescagem de 1984, ficam fora dessa conta.
7. Acrescentar o ano em `regras_historicas.py` (`PONTOS_VITORIA` e
   `FASE_META`, com `num_grupos` de cada fase de grupos e o criterio).
8. Rodar o importador e depois `python -u .\build.py` (o enriquecimento
   avisa com `!!` se os grupos derivados nao baterem com `num_grupos`).
9. Validar o JS embutido:

```powershell
python -u -c "import pathlib,re; html=pathlib.Path('dashboard.html').read_text(encoding='utf-8'); js=re.search(r'<script>(.*)</script>', html, re.S).group(1); pathlib.Path('c:/tmp/dashboard_check.js').write_text(js, encoding='utf-8')"
node --check c:\tmp\dashboard_check.js
```

10. Abrir Historico > Brasileiro Antigo no ano novo e conferir grupos,
    mata-mata e campeao.
11. Commit com o importador, o CSV de auditoria, o HTML da RSSSF, o banco, o
    dashboard, `regras_historicas.py` e o README.

## Fluxo Normal de Uso

Usando `db/brasileirao.db` como fonte de dados:

```powershell
python -u .\build.py
```

Esse comando:

1. Executa `validar_banco.py`.
2. Executa `enriquecer_historico.py` (grupos/criterios/pontos do Brasileiro antigo).
3. Executa `gerar_dashboard_html.py`.
4. Executa `check_dashboard.py`.

Para inspecionar rapidamente o estado atual:

```powershell
python -u .\status_db.py
```

Para validar rapidamente o HTML ja gerado:

```powershell
python -u .\check_dashboard.py
```

Para abrir o resultado, use `dashboard.html` no navegador.

## Rebuild Completo

O rebuild completo substitui `db/brasileirao.db`, entao exige cuidado.

Comando:

```powershell
python -u .\build.py --rebuild-from-sources
```

O script executa:

```powershell
python .\criar_banco_brasileirao.py --reset --all
python .\importar_classificacao_historica_brasileirao.py
python .\importar_finais_copa_brasil.py
python .\importar_edicoes_copa_brasil.py
python .\validar_banco.py
python .\gerar_dashboard_html.py
python .\check_dashboard.py
```

Atencao importante:

- Hoje o `build.py --rebuild-from-sources` nao chama automaticamente o
  `historico/edicoes.py --todos` (Brasileiro antigo, 1937-2002). O
  enriquecimento estrutural
  (`enriquecer_historico.py`) roda no fluxo normal e tambem no rebuild.
- Se voce recriar o banco do zero, precisa reexecutar os importadores
  historicos antes de gerar/validar o dashboard final.
- Se isso nao for feito, o bloco "Brasileiro Antigo" pode perder os jogos
  historicos mesmo que classificacoes finais continuem existindo.

Sequencia recomendada em caso de rebuild total:

```powershell
python -u .\backup.py
python -u .\build.py --rebuild-from-sources --skip-dashboard
python -u historico\edicoes.py --todos
python -u .\build.py
```

Opcoes uteis do `build.py`:

```powershell
python -u .\build.py --skip-dashboard
python -u .\build.py --skip-dashboard-check
python -u .\build.py --skip-validacao
python -u .\build.py --rebuild-from-sources --skip-historico
python -u .\build.py --rebuild-from-sources --from-year 2016 --to-year 2024
```

## Como o Dashboard Usa o Historico

No `dashboard.html`, o historico aparece em:

- aba `Historico`;
- subvisao `Brasileiro Antigo`.

O front-end usa o payload `DATA.hist_nacional`, gerado por
`gerar_dashboard_html.py`.

Esse payload inclui:

- `edicoes` (com `pontos_vitoria`);
- `participantes`;
- `fases` (com `num_grupos`, `formato_serie`, `criterio`);
- `partidas` (com `grupo` e os ids dos clubes);
- classificacao final historica via `class_final_hist`.

O render do "Brasileiro Antigo" e **dirigido pelo tipo de fase** (`liga`,
`grupo`, `mata_mata`), em vez de assumir sempre liga + chaveamento:

- banner do campeao no topo, com o criterio do titulo;
- **stepper** com o caminho ate o titulo (uma etapa por fase, clicavel);
- corrida de lideranca, apenas quando ha fase de pontos corridos;
- container `#hn-phases` que renderiza cada fase com o componente certo:
  - `liga`: **uma** tabela de classificacao (fases liga consecutivas, como os
    dois turnos de 1995, sao combinadas) com a pontuacao da epoca (2 ou 3 pts);
  - `grupo`: **uma mini-tabela por grupo** (quadrangulares, "Grupo semifinal",
    etc.), com destaque para quem avanca;
  - `mata_mata`: bracket em funil agrupando confrontos por par de clubes,
    tratando jogo unico, ida/volta e melhor de 3, com coluna-trofeu do campeao;
- classificacao final oficial, participantes e tabela de jogos (filtravel por fase).

Detalhe importante:

- Clubes que avancam de uma fase sao detectados por aparecerem em alguma fase
  posterior (sem precisar codificar a regra de classificacao de cada ano).
- Algumas finais antigas foram decididas por criterio de regulamento mesmo com
  agregado empatado; o bracket usa a classificacao oficial (`class_final_hist`)
  como desempate e, se nao houver campeao valido, marca "decidido por criterio"
  em vez de eleger o visitante.
- Exemplo: 1997, Vasco campeao por melhor campanha contra o Palmeiras.

## Cuidados Tecnicos

- Sempre rode `python -u .\backup.py` antes de alterar `db/brasileirao.db`.
- Sempre rode `python -u .\build.py` depois de importar dados.
- Sempre rode `node --check c:\tmp\dashboard_check.js` depois de regenerar
  `dashboard.html`.
- Nunca misture no mesmo commit anos diferentes sem necessidade.
- Se aparecer clube nao encontrado em `dim_clube`, nao force insert manual
  imediatamente. Primeiro normalize o nome no `CANONICAL.update`.
- Se a pagina RSSSF tiver Serie B, Serie C ou Copa do Brasil no mesmo HTML,
  corte o texto antes desses blocos.
- Se a pagina tiver placares em formato compacto ou com dois jogos por linha,
  crie parser especifico como foi feito em 1996 e 1994.
- Se a pagina tiver nomes com caracteres quebrados por encoding, priorize
  normalizacao por `norm()` e mapeamento canonico.
- Os CSVs de auditoria devem ser mantidos versionados junto com o importador.
- `dashboard.html` e `db/brasileirao.db` sao artefatos gerados, mas neste
  projeto eles sao versionados de proposito.

## Pastas

- `data/`
  - CSVs, HTMLs RSSSF, planilhas e arquivos-fonte usados nas importacoes.

- `db/`
  - Banco SQLite atual.

- `sql/`
  - Schema do banco.

- `docs/`
  - Documentacao complementar e relatorios de lacunas/auditoria.

- `backups/`
  - Backups locais criados por `backup.py`.
  - Nao trate como fonte principal; use para recuperacao.

## Documentacao Complementar

- `docs/manutencao_dados.md`
  - Manutencao, backup, restauracao e rebuild.

- `docs/uso_dashboard.md`
  - Uso, validacao e publicacao do dashboard.

## Checklist Para Outra IA Continuar

Antes de mexer:

```powershell
git status --short
python -u .\backup.py
```

Para importar um ano novo, siga "Como Continuar a Expansao Historica": baixar
a pagina, acrescentar a edicao em `historico/edicoes.py`
comum, conferir contra a "Final Table", registrar as regras, rodar
`build.py`, validar o JS, olhar o dashboard e so entao fazer o commit.
