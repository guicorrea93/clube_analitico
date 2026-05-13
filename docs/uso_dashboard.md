# Uso do Dashboard

O arquivo `dashboard.html` e um dashboard estatico gerado a partir de
`db/brasileirao.db`.

## Abrir localmente

Depois de gerar o HTML:

```powershell
python .\build.py
```

Abra `dashboard.html` no navegador.

## Validar antes de usar

Confira o banco:

```powershell
python .\status_db.py
```

Valide o HTML:

```powershell
python .\check_dashboard.py
```

## Publicacao

Para publicar, envie pelo menos:

- `dashboard.html`

O dashboard embute o payload de dados diretamente no HTML. Por isso, ele nao
precisa do banco SQLite para ser aberto por quem for apenas visualizar.

## Dependencia externa

O dashboard carrega Plotly por CDN:

```html
https://cdn.plot.ly/plotly-2.35.2.min.js
```

Sem internet, a estrutura do HTML abre, mas graficos baseados em Plotly podem nao
renderizar.

## Quando regenerar

Regere `dashboard.html` quando:

- `db/brasileirao.db` for atualizado;
- validacoes forem alteradas;
- o layout/codigo do gerador for alterado;
- for necessario publicar uma versao nova do dashboard.
