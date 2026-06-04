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
  importado de 1992 a 2002.

Historico nacional ja importado no bloco "Historico > Brasileiro Antigo":

| Ano | Participantes | Fases | Jogos |
| --- | ---: | ---: | ---: |
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

- 11 edicoes: 1992 a 2002.
- 45 fases.
- 3.305 partidas.

Ultimos anos importados antes desta atualizacao do README:

- 1994: commit `08ef00d Adiciona historico do Brasileiro 1994`
- 1993: commit `572aec5 Adiciona historico do Brasileiro 1993`
- 1992: commit `18017b2 Adiciona historico do Brasileiro 1992`

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
    importadores do historico antigo 1992-2002. Veja a secao "Rebuild completo".

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

### Fonte principal para 1992-2002

RSSSF Brasil:

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

- `1991`

Fluxo recomendado para cada novo ano:

1. Criar backup:

```powershell
python -u .\backup.py
```

2. Baixar a pagina RSSSF:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/braz91.html" -o data\rsssf_braz91.html
```

3. Ler a pagina e mapear o regulamento:

```powershell
python -u -c "from pathlib import Path; import re, html; raw=Path('data/rsssf_braz91.html').read_text(encoding='latin-1'); m=re.search(r'<pre>(.*?)</pre>', raw, re.S|re.I); t=html.unescape(m.group(1) if m else raw); print(t[:4000])"
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
python -u -c "from pathlib import Path; import re, html; raw=Path('data/rsssf_braz91.html').read_text(encoding='latin-1'); t=html.unescape(re.search(r'<pre>(.*?)</pre>', raw, re.S|re.I).group(1)); pat=re.compile(r'^.+?\s+\d+\s+x\s+.+?\s+\d+\s*$', re.M|re.I); print(len(pat.findall(t)))"
```

6. Criar um importador novo:

```text
importar_brasileirao_historico_1991.py
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
python -u .\importar_brasileirao_historico_1991.py
```

10. Validar contagens diretamente no banco:

```powershell
python -u -c "import sqlite3; con=sqlite3.connect('db/brasileirao.db'); print(con.execute('select f.temporada_id, f.fase_nome, f.fase_tipo, count(p.partida_hist_id) from dim_fase_nacional_historica f left join fato_partida_nacional_historica p on p.fase_nacional_id=f.fase_nacional_id where f.temporada_id=1991 group by f.fase_nacional_id order by f.fase_ordem').fetchall())"
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
git add dashboard.html db/brasileirao.db importar_brasileirao_historico_1991.py data\brasileirao_historico_1991_partidas.csv data\rsssf_braz91.html
```

15. Commit:

```powershell
git commit -m "Adiciona historico do Brasileiro 1991"
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
  `importar_brasileirao_historico_1992.py` ate
  `importar_brasileirao_historico_2002.py`.
- Se voce recriar o banco do zero, precisa reexecutar os importadores
  historicos antes de gerar/validar o dashboard final.
- Se isso nao for feito, o bloco "Brasileiro Antigo" pode perder os jogos
  historicos mesmo que classificacoes finais continuem existindo.

Sequencia recomendada em caso de rebuild total:

```powershell
python -u .\backup.py
python -u .\build.py --rebuild-from-sources --skip-dashboard
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

Para continuar 1991:

```powershell
curl.exe -L "https://www.rsssf.org/tablesb/braz91.html" -o data\rsssf_braz91.html
```

Depois:

1. Inspecionar `data/rsssf_braz91.html`.
2. Separar apenas a Serie A.
3. Contar jogos por fase antes de importar.
4. Criar `importar_brasileirao_historico_1991.py`.
5. Gerar `data/brasileirao_historico_1991_partidas.csv`.
6. Rodar `python -u .\build.py`.
7. Extrair JS para `c:/tmp/dashboard_check.js`.
8. Rodar `node --check c:\tmp\dashboard_check.js`.
9. Conferir `git status --short`.
10. Fazer commit somente depois de tudo passar.
