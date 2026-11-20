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
