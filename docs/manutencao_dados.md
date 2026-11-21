# Manutencao dos Dados

Este projeto trata `db/brasileirao.db` como a fonte principal para uso normal do
dashboard. Os arquivos em `data/` e os scripts de importacao existem para carga,
auditoria e reconstrucao controlada.

## Fluxo normal

Use o banco existente, valide e gere o dashboard:

```powershell
python .\build.py
```

Esse fluxo nao recria `db/brasileirao.db`.

## Antes de operacoes sensiveis

Crie um backup local:

```powershell
python .\backup.py
```

Confira o estado atual:

```powershell
python .\status_db.py
python .\validar_banco.py
```

## Reconstrucao por fontes

A reconstrucao por fontes substitui o banco. Use apenas quando for intencional:

```powershell
python .\build.py --rebuild-from-sources
```

Se `classificacao_codex.xlsx` nao existir, o rebuild completo e bloqueado para
evitar perda da classificacao historica nacional.

## Restauracao

Liste os backups:

```powershell
python .\restore_backup.py
```

Restaure um backup explicitamente:

```powershell
python .\restore_backup.py <nome_do_backup> --confirm
```

Depois de restaurar, rode:

```powershell
python .\build.py
python .\status_db.py
```

## Série B

Os dados da Série B (1971 a 2025, 44 edições) ficam em tabelas próprias no mesmo banco
(`dim_edicao_serie_b`, `dim_fase_serie_b`, `fato_partida_serie_b`, `fato_gol_serie_b`,
`fato_cartao_serie_b`, `fato_tabela_fase_serie_b`, `fato_classificacao_final_serie_b`,
`fato_classificacao_rodada_serie_b`, `fato_artilheiro_serie_b`). Os clubes usam o mesmo
`dim_clube` da Série A: quem jogou as duas divisões tem um cadastro só.

Fontes (guardadas em `data/serie_b/`) e os scripts que as baixam:

```powershell
python .\serie_b\espn.py        # jogos da ESPN, 2010 em diante (um pedido por dia: demora)
python .\serie_b\ogol.py        # calendário do ogol: rodada oficial e conferência de placar
python .\serie_b\wikipedia.py   # páginas da Wikipédia (tabela final, punições, matriz de resultados)
```

As páginas da RSSSF Brasil (`data/serie_b/rsssfbrasil/`) foram baixadas uma vez; os scripts só
as leem. Para (re)montar e gravar tudo e gerar o relatório `docs/serie_b_coleta.md`:

```powershell
python .\backup.py
python .\serie_b\importar.py
```

Conferências que ajudam a achar problema: `python .\serie_b\rsssf.py` (cada tabela publicada
contra a soma dos jogos lidos), `python .\serie_b\clubes.py` (clubes identificados e nomes
ambíguos) e `python .\serie_b\nomes.py` (nomes da ESPN, ogol e Wikipédia sem clube).

## Banco genérico e painel

`db/futebol.db` guarda todas as competições num formato só (país, competição, edição, fase,
partida, gols, cartões, classificações; ver `futebol/esquema.sql`). Hoje ele é montado a partir
do `brasileirao.db` (Séries A e B), que continua sendo onde os coletores dessas duas gravam, e dos
pacotes do agente de coleta (`data/coleta/<slug>/pacote/`, Série C em diante):

```powershell
python .\futebol\migrar_brasileirao.py   # refaz db/futebol.db, confere com o brasileirao.db e carrega os pacotes
python .\futebol\carregar_pacotes.py bra-serie-c   # só recarrega um pacote (sem refazer o resto)
python .\baixar_escudos.py --ogol        # escudos dos clubes novos dos pacotes (calendários do ogol guardados)
python .\gerar_dashboard_v2.py           # painel em painel/ (index.html, dados/<competição>.js, escudos/)
```

Depois de mexer na Série A ou na Série B, ou de receber um pacote novo, rode o primeiro e o último.

O `db/futebol.db` não vai para o GitHub (`.gitignore`): é refeito pelo primeiro comando, a partir do `brasileirao.db`
e dos pacotes, que estão no GitHub.

**Painel online:** https://clubeanalitico.pages.dev (Cloudflare Pages, projeto `clubeanalitico`, conta do Guilherme).
Não publica sozinho com o push: depois de gerar o painel (e com o ok do Guilherme), envie a pasta `painel/`:

```powershell
npx wrangler pages deploy painel --project-name clubeanalitico --branch main --commit-dirty=true
```
