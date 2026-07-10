# Clube Analitico

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
- A Copa de **2026 esta em andamento**: entra em todos os cards e graficos, mas
  sua classificacao final e parcial (so times ja eliminados). Por isso as
  estatisticas por selecao de 2026 sao agregadas dos grupos + jogos de mata-mata
  ja disputados, e quem segue vivo aparece como "Em andamento".
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

Abas e recursos:

- **Geral das Copas**: KPIs, linha do tempo, titulos e top 4, rankings de
  vitorias/empates/derrotas (toggle total/%), gols e publico por edicao, maiores
  artilheiros (carreira) e artilheiro por edicao, **melhor ataque e melhor
  defesa por edicao** e maiores goleadas.
- **Por Copa**: cartaz da edicao, resumo, classificacao final, grupos,
  chaveamento e jogos clicaveis. Ao selecionar uma partida, o dashboard abre
  diretamente um modal com placar, linha temporal dos gols, data, horario,
  estadio, publico, arbitro (e pais), escalacoes quando a Wikipedia fornece
  (numero/posicao/nome), quem entrou e treinadores. A ficha esta anexada em
  todos os jogos de 1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970,
  1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018 e
  2022.
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
| `DATA.copas[].partidas[].ficha` | Detalhe da partida para 1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018 e 2022: data/hora, estadio, publico, arbitro, pais do arbitro e, quando disponivel na Wikipedia, escalacoes, substituicoes e treinadores |
| `DATA.selecoes[]` | Agregado historico por selecao (J/V/E/D/GP/GC, titulos, aproveitamento) |
| `DATA.artilheiros_selecao` | `{selecao: {ano: [[jogador, gols], ...]}}` |
| `DATA.gols_contra_selecao` | `{selecao: {ano: [[autor, gols], ...]}}` — gols contra a favor |
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
  coluna `Equipevde` e uma coluna `Classificado`. Cuidado com a infobox: o campo
  de gols vem como "261 (2,9 por partida)", entao usa-se
  `to_int(val.split("(")[0])`. Em `phaseRank` (JS), o teste de "avos" precisa vir
  **antes** do teste de "final", porque "dezesseis avos de final" contem "final".
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

Proximos passos (Copa do Mundo):

- **Refinar detalhes das edicoes antigas**. A base de fichas ja cobre
  1930-2022, mas as edicoes ate 2002 tem formatos irregulares na Wikipedia PT.
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
- **Eventos na escalacao**: gols e cartoes ao lado do jogador (como na Wikipedia)
  sao hoje descartados do nome via regex. Para reexibir, guarde as celulas extras
  da linha do jogador em vez de recortar o texto do nome.
- **Reservas nao utilizados nao aparecem** (a Wikipedia so lista quem entrou) e
  **arbitros assistentes** nao constam das caixas de 2022.
- **Pais do arbitro** as vezes vem em pt-PT ("Polonia" grafada diferente). Se for
  exibir bandeira, normalize antes de bater com `FLAG_CODES`.
- **`ARTILHEIROS_HISTORICO` esta parcial**: soma os 7 gols de 2026 a Messi (20) e
  Mbappe (19), que passam Klose (16), mas **nao** soma outros ativos (Kane,
  Haaland). Revisar quando a Copa de 2026 terminar. O card ja traz essa ressalva.
- **Quando 2026 acabar**: apague os HTMLs de 2026 do cache para rebaixar a versao
  final; com a `classificacao_final` completa, o ramo especial de 2026 em
  `_cup_team_stats` / `aggregate_selection_stats` (que agrega dos grupos + jogos)
  pode ser removido, e a trajetoria/posicoes passam a incluir a edicao.
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
  importado de 1986 a 2002.

Historico nacional ja importado no bloco "Historico > Brasileiro Antigo":

| Ano | Participantes | Fases | Jogos |
| --- | ---: | ---: | ---: |
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

- 17 edicoes: 1986 a 2002.
- 70 fases.
- 4.856 partidas.

Ultimos anos importados antes desta atualizacao do README:

- 1994: commit `08ef00d Adiciona historico do Brasileiro 1994`
- 1993: commit `572aec5 Adiciona historico do Brasileiro 1993`
- 1992: commit `18017b2 Adiciona historico do Brasileiro 1992`

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
(render). Os anos de 1986, 1987, 1988, 1989, 1990 e 1991 ja foram importados dentro desse padrao.

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

Esses scripts foram criados para preencher o bloco historico nacional antes de
2003. Eles importam participantes, fases e partidas para as tabelas historicas
do banco.

Arquivos:

- `importar_brasileirao_historico_1990.py`
- `importar_brasileirao_historico_1991.py`
- `importar_brasileirao_historico_1992.py`
- `importar_brasileirao_historico_1993.py`
- `importar_brasileirao_historico_1994.py`
- `importar_brasileirao_historico_1995.py`
- `importar_brasileirao_historico_1996.py`
- `importar_brasileirao_historico_1997.py`
- `importar_brasileirao_historico_1998_1999.py`
- `importar_brasileirao_historico_2000_2001.py`
- `importar_brasileirao_historico_2002.py`

Padrao desses importadores:

- Leem HTML local em `data/rsssf_*.html`.
- Parseiam participantes, fases e jogos.
- Normalizam nomes de clubes com mapas `CANONICAL`.
- Validam contagens esperadas por ano/fase.
- Apagam e reinserem apenas os dados historicos daquela edicao.
- Escrevem CSV de auditoria em `data/brasileirao_historico_*_partidas.csv`.
- Nao baixam a fonte sozinhos; o HTML deve estar em `data/`.

Tabelas usadas pelos importadores historicos:

- `dim_edicao_nacional`
- `dim_fase_nacional_historica`
- `fato_participante_nacional_historico`
- `fato_partida_nacional_historica`
- `dim_clube`

Os scripts chamam `create_tables(con)` de
`importar_brasileirao_historico_2000_2001.py`, garantindo que as tabelas
historicas existam antes da importacao.

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

### Fonte principal para 1986-2002

RSSSF Brasil:

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

Cada importador historico gera um CSV com os jogos importados. Esses arquivos
servem para revisao humana e para comparar o que entrou no banco.

Arquivos atuais:

- `data/brasileirao_historico_1990_partidas.csv`
- `data/brasileirao_historico_1991_partidas.csv`
- `data/brasileirao_historico_1992_partidas.csv`
- `data/brasileirao_historico_1993_partidas.csv`
- `data/brasileirao_historico_1994_partidas.csv`
- `data/brasileirao_historico_1995_partidas.csv`
- `data/brasileirao_historico_1996_partidas.csv`
- `data/brasileirao_historico_1997_partidas.csv`
- `data/brasileirao_historico_1998_1999_partidas.csv`
- `data/brasileirao_historico_2000_2001_partidas.csv`
- `data/brasileirao_historico_2002_partidas.csv`

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

Proximo ano natural:

- `1989`

Fluxo recomendado para cada novo ano:

1. Criar backup:

```powershell
python -u .\backup.py
```

2. Baixar a pagina RSSSF:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/braz89.html" -o data\rsssf_braz89.html
```

3. Ler a pagina e mapear o regulamento:

```powershell
python -u -c "from pathlib import Path; import re, html; raw=Path('data/rsssf_braz89.html').read_text(encoding='latin-1'); m=re.search(r'<pre>(.*?)</pre>', raw, re.S|re.I); t=html.unescape(m.group(1) if m else raw); print(t[:4000])"
```

4. Identificar marcadores:

- participantes;
- primeira fase;
- segunda fase;
- playoff/repescagem, quando existir;
- quartas, semifinais e final, quando existirem;
- ponto onde comeca Serie B, Copa do Brasil ou outro torneio, para nao importar
  competicao errada.

5. Contar jogos por bloco com regex antes de criar o importador.

Exemplo generico:

```powershell
python -u -c "from pathlib import Path; import re, html; raw=Path('data/rsssf_braz89.html').read_text(encoding='latin-1'); t=html.unescape(re.search(r'<pre>(.*?)</pre>', raw, re.S|re.I).group(1)); pat=re.compile(r'^.+?\s+\d+\s+x\s+.+?\s+\d+\s*$', re.M|re.I); print(len(pat.findall(t)))"
```

6. Criar um importador novo:

```text
importar_brasileirao_historico_1989.py
```

7. Reaproveitar padroes dos importadores existentes:

- `read_pre`
- `Game`
- `canonical_name`
- `create_tables`
- `norm`
- `import_year`
- `write_audit`

8. Adicionar normalizacoes de nomes no `CANONICAL.update`.

Exemplos recorrentes:

- `atletico mg` -> `Atletico-MG`
- `atletico pr` -> `Athletico-PR`
- `botafogo` -> `Botafogo-RJ`
- `sao paulo` -> `Sao Paulo`
- `gremio` -> `Gremio`
- `criciuma` -> `Criciuma`
- `nautico` -> `Nautico`
- `uniao sao joao` -> `Uniao Sao Joao`
- `vitoria ba` -> `Vitoria`

9. Executar o importador:

```powershell
python -u .\importar_brasileirao_historico_1989.py
```

10. Validar contagens diretamente no banco:

```powershell
python -u -c "import sqlite3; con=sqlite3.connect('db/brasileirao.db'); print(con.execute('select f.temporada_id, f.fase_nome, f.fase_tipo, count(p.partida_hist_id) from dim_fase_nacional_historica f left join fato_partida_nacional_historica p on p.fase_nacional_id=f.fase_nacional_id where f.temporada_id=1989 group by f.fase_nacional_id order by f.fase_ordem').fetchall())"
```

11. Regenerar e validar o dashboard:

```powershell
python -u .\build.py
```

12. Validar sintaxe do JavaScript embutido:

```powershell
python -u -c "import pathlib,re; html=pathlib.Path('dashboard.html').read_text(encoding='utf-8'); js=re.search(r'<script>(.*)</script>', html, re.S).group(1); pathlib.Path('c:/tmp/dashboard_check.js').write_text(js, encoding='utf-8')"
node --check c:\tmp\dashboard_check.js
```

13. Conferir `git status`:

```powershell
git status --short
```

14. Adicionar apenas os arquivos do ano novo e artefatos gerados:

```powershell
git add dashboard.html db/brasileirao.db importar_brasileirao_historico_1989.py data\brasileirao_historico_1989_partidas.csv data\rsssf_braz89.html
```

15. Commit:

```powershell
git commit -m "Adiciona historico do Brasileiro 1989"
```

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

- Hoje o `build.py --rebuild-from-sources` nao chama automaticamente os scripts
  `importar_brasileirao_historico_1986.py` ate
  `importar_brasileirao_historico_2002.py`. O enriquecimento estrutural
  (`enriquecer_historico.py`) roda no fluxo normal e tambem no rebuild.
- Se voce recriar o banco do zero, precisa reexecutar os importadores
  historicos antes de gerar/validar o dashboard final.
- Se isso nao for feito, o bloco "Brasileiro Antigo" pode perder os jogos
  historicos mesmo que classificacoes finais continuem existindo.

Sequencia recomendada em caso de rebuild total:

```powershell
python -u .\backup.py
python -u .\build.py --rebuild-from-sources --skip-dashboard
python -u .\importar_brasileirao_historico_1990.py
python -u .\importar_brasileirao_historico_1991.py
python -u .\importar_brasileirao_historico_1992.py
python -u .\importar_brasileirao_historico_1993.py
python -u .\importar_brasileirao_historico_1994.py
python -u .\importar_brasileirao_historico_1995.py
python -u .\importar_brasileirao_historico_1996.py
python -u .\importar_brasileirao_historico_1997.py
python -u .\importar_brasileirao_historico_1998_1999.py
python -u .\importar_brasileirao_historico_2000_2001.py
python -u .\importar_brasileirao_historico_2002.py
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

Para continuar 1989:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/braz89.html" -o data\rsssf_braz89.html
```

Depois:

1. Inspecionar `data/rsssf_braz89.html`.
2. Separar apenas a Serie A.
3. Contar jogos por fase antes de importar.
4. Criar `importar_brasileirao_historico_1989.py`.
5. Gerar `data/brasileirao_historico_1989_partidas.csv`.
6. Rodar `python -u .\build.py`.
7. Extrair JS para `c:/tmp/dashboard_check.js`.
8. Rodar `node --check c:\tmp\dashboard_check.js`.
9. Conferir `git status --short`.
10. Fazer commit somente depois de tudo passar.
