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
