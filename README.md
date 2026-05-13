# Clube Analitico

Dashboard local de futebol brasileiro em HTML, gerado a partir de um banco SQLite.

## Requisitos

- Python 3.12+
- Dependencias Python listadas em `requirements.txt`

Instalacao:

```powershell
python -m pip install -r requirements.txt
```

## Arquivos principais

- `dashboard.html`: dashboard pronto para abrir no navegador.
- `gerar_dashboard_html.py`: recria o `dashboard.html` usando `db/brasileirao.db`.
- `build.py`: executa o pipeline completo usando os scripts existentes.
- `backup.py`: cria backup local dos artefatos criticos ou do projeto completo.
- `status_db.py`: mostra um resumo rapido do banco e do dashboard.
- `criar_banco_brasileirao.py`: recria o banco SQLite a partir dos CSVs em `data/`.
- `validar_banco.py`: valida campeoes, rebaixados e consistencia basica do banco.
- `importar_classificacao_historica_brasileirao.py`: importa classificacoes finais historicas para o banco.
- `importar_finais_copa_brasil.py`: importa campeoes, vices e partidas finais da Copa do Brasil.
- `importar_edicoes_copa_brasil.py`: importa metadados e participantes por edicao da Copa do Brasil.

## Fluxo de uso

Fluxo normal, usando `db/brasileirao.db` como fonte de dados:

```powershell
python .\build.py
```

O comando acima valida o banco existente e gera `dashboard.html`.

Para inspecionar rapidamente o estado atual do banco:

```powershell
python .\status_db.py
```

Para criar backup local antes de operacoes sensiveis:

```powershell
python .\backup.py
```

Para backup quase completo do projeto:

```powershell
python .\backup.py --full
```

Para recriar o banco a partir dos CSVs e wikitextos locais, use uma opcao
explicita:

```powershell
python .\build.py --rebuild-from-sources
```

Esse comando executa, em ordem:

```powershell
python .\criar_banco_brasileirao.py --reset --all
python .\importar_classificacao_historica_brasileirao.py  # se classificacao_codex.xlsx existir
python .\importar_finais_copa_brasil.py
python .\importar_edicoes_copa_brasil.py
python .\validar_banco.py
python .\gerar_dashboard_html.py
```

O script `importar_classificacao_historica_brasileirao.py` depende do arquivo
`classificacao_codex.xlsx` na raiz do projeto. Rode-o antes da validacao e da
geracao do dashboard quando essa planilha estiver disponivel. O `build.py`
exige essa planilha ao recriar o banco por fontes, porque essa operacao substitui
`db/brasileirao.db`. Se a planilha nao existir, o rebuild para antes de alterar o
banco.

Opcoes uteis:

```powershell
python .\build.py --skip-dashboard
python .\build.py --skip-validacao
python .\build.py --rebuild-from-sources --skip-historico
python .\build.py --rebuild-from-sources --from-year 2016 --to-year 2024
```

Para abrir o resultado, use o arquivo `dashboard.html` no navegador.

## Pastas

- `data/`: arquivos-fonte CSV e wikitextos usados nas importacoes.
- `db/`: banco SQLite gerado.
- `sql/`: schema do banco.

## Observacoes

- `dashboard.html` e `db/brasileirao.db` sao artefatos gerados, mas permanecem
  versionaveis por padrao. O `.gitignore` deixa linhas comentadas caso a decisao
  seja manter apenas codigo-fonte no repositorio.
- O dashboard usa Plotly via CDN, entao alguns graficos dependem de internet ao
  abrir o HTML.
