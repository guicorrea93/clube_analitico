from __future__ import annotations

import json
import math
from datetime import datetime
from html import escape
from pathlib import Path

import pandas as pd


LACUNAS_XLSX = Path("docs/lacunas_para_pesquisa.xlsx")
FORMACOES_XLSX = Path("docs/debitos_formacoes_2003_2005_diagnostico.xlsx")
OUTPUT_HTML = Path("docs/auditoria_debitos.html")


def read_sheet(path: Path, sheet_name: str) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_excel(path, sheet_name=sheet_name).fillna("")


def read_optional_excel(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_excel(path).fillna("")


def frame_records(df: pd.DataFrame) -> list[dict]:
    if df.empty:
        return []
    clean = df.copy()
    for col in clean.columns:
        clean[col] = clean[col].map(lambda value: value.isoformat() if hasattr(value, "isoformat") else value)
    return clean.to_dict(orient="records")


def to_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def build_payload() -> dict:
    resumo = read_sheet(LACUNAS_XLSX, "Resumo")
    resumo_temporada = read_sheet(LACUNAS_XLSX, "Resumo por Temporada")
    tecnicos = read_sheet(LACUNAS_XLSX, "Tecnicos Formacoes")
    gols = read_sheet(LACUNAS_XLSX, "Gols Divergentes")
    cartoes = read_sheet(LACUNAS_XLSX, "Cartoes Sem Detalhe")
    erros = read_sheet(LACUNAS_XLSX, "Erros Fontes Online")
    diagnostico_formacoes = read_optional_excel(FORMACOES_XLSX)

    datasets = {
        "resumo": {
            "label": "Resumo",
            "description": "Totais consolidados da planilha de lacunas.",
            "rows": frame_records(resumo),
            "columns": list(resumo.columns),
        },
        "temporadas": {
            "label": "Por Temporada",
            "description": "Distribuição das lacunas por temporada e categoria.",
            "rows": frame_records(resumo_temporada),
            "columns": list(resumo_temporada.columns),
        },
        "tecnicos": {
            "label": "Técnicos/Formações",
            "description": "Partidas com técnico ou formação faltante.",
            "rows": frame_records(tecnicos),
            "columns": list(tecnicos.columns),
        },
        "formacoes_diagnostico": {
            "label": "Diagnóstico Formações",
            "description": "Detalhe dos 35 débitos finais de formações 2003-2005, com contagens e nomes do Transfermarkt quando disponíveis.",
            "rows": frame_records(diagnostico_formacoes),
            "columns": list(diagnostico_formacoes.columns),
        },
        "gols": {
            "label": "Gols Divergentes",
            "description": "Partidas em que a quantidade de gols cadastrados diverge do placar.",
            "rows": frame_records(gols),
            "columns": list(gols.columns),
        },
        "cartoes": {
            "label": "Cartões Sem Detalhe",
            "description": "Cartões no banco que ainda não têm todos os detalhes de jogador/camisa/posição.",
            "rows": frame_records(cartoes),
            "columns": list(cartoes.columns),
        },
        "erros": {
            "label": "Erros Fontes Online",
            "description": "Erros e lacunas observados nas importações ou fontes online.",
            "rows": frame_records(erros),
            "columns": list(erros.columns),
        },
    }

    summary_cards = [
        {
            "label": "Técnico/Formação",
            "value": len(tecnicos),
            "hint": "partidas",
        },
        {
            "label": "Gols Divergentes",
            "value": len(gols),
            "hint": "partidas",
        },
        {
            "label": "Cartões Sem Detalhe",
            "value": len(cartoes),
            "hint": "linhas",
        },
        {
            "label": "Erros de Fontes",
            "value": len(erros),
            "hint": "registros",
        },
        {
            "label": "Diagnóstico 2003-2005",
            "value": len(diagnostico_formacoes),
            "hint": "partidas",
        },
    ]

    seasons: set[str] = set()
    for dataset in datasets.values():
        for row in dataset["rows"]:
            value = row.get("temporada")
            if value not in ("", None) and not (isinstance(value, float) and math.isnan(value)):
                seasons.add(str(int(value)) if isinstance(value, float) and value.is_integer() else str(value))

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_files": [str(LACUNAS_XLSX), str(FORMACOES_XLSX)],
        "summary_cards": summary_cards,
        "seasons": sorted(seasons),
        "datasets": datasets,
    }


def html_document(payload: dict) -> str:
    payload_json = to_json(payload)
    title = "Auditoria de Débitos de Dados"
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    :root {{
      --bg: #f6f7f9;
      --panel: #ffffff;
      --ink: #1d2430;
      --muted: #667085;
      --line: #d9dee7;
      --accent: #0b5cad;
      --accent-2: #197278;
      --warn: #a45b00;
      --shadow: 0 8px 24px rgba(18, 32, 55, .08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Segoe UI, Roboto, Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      letter-spacing: 0;
    }}
    header {{
      background: #0f1724;
      color: white;
      padding: 28px 32px 22px;
    }}
    header h1 {{
      margin: 0 0 8px;
      font-size: 28px;
      font-weight: 700;
    }}
    header p {{
      margin: 0;
      color: #c8d1df;
      font-size: 14px;
    }}
    main {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 22px 24px 36px;
    }}
    .cards {{
      display: grid;
      grid-template-columns: repeat(5, minmax(150px, 1fr));
      gap: 12px;
      margin-bottom: 18px;
    }}
    .metric {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px 16px;
      box-shadow: var(--shadow);
    }}
    .metric strong {{
      display: block;
      font-size: 28px;
      line-height: 1;
      margin-bottom: 6px;
    }}
    .metric span {{
      display: block;
      color: var(--muted);
      font-size: 13px;
    }}
    .toolbar {{
      display: grid;
      grid-template-columns: 1fr 180px 170px;
      gap: 10px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 12px;
      box-shadow: var(--shadow);
    }}
    input, select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px 11px;
      font-size: 14px;
      background: white;
      color: var(--ink);
    }}
    .tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
    }}
    .tab {{
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 6px;
      padding: 9px 11px;
      cursor: pointer;
      font-size: 13px;
    }}
    .tab.active {{
      background: var(--accent);
      color: white;
      border-color: var(--accent);
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
      overflow: hidden;
    }}
    .panel-head {{
      display: flex;
      justify-content: space-between;
      align-items: start;
      gap: 16px;
      padding: 14px 16px;
      border-bottom: 1px solid var(--line);
    }}
    .panel-head h2 {{
      margin: 0 0 4px;
      font-size: 18px;
    }}
    .panel-head p {{
      margin: 0;
      color: var(--muted);
      font-size: 13px;
    }}
    .count {{
      color: var(--accent-2);
      font-weight: 700;
      white-space: nowrap;
      font-size: 14px;
    }}
    .table-wrap {{
      overflow: auto;
      max-height: 68vh;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 980px;
      font-size: 12px;
    }}
    th {{
      position: sticky;
      top: 0;
      z-index: 1;
      background: #eef2f7;
      text-align: left;
      border-bottom: 1px solid var(--line);
      padding: 9px 8px;
      white-space: nowrap;
    }}
    td {{
      border-bottom: 1px solid #edf0f5;
      padding: 8px;
      vertical-align: top;
      max-width: 360px;
      overflow-wrap: anywhere;
    }}
    tr:hover td {{ background: #f9fbfd; }}
    a {{ color: var(--accent); }}
    .empty {{
      padding: 28px 16px;
      color: var(--muted);
      text-align: center;
    }}
    .sources {{
      color: var(--muted);
      font-size: 12px;
      margin-top: 12px;
    }}
    @media (max-width: 960px) {{
      .cards {{ grid-template-columns: repeat(2, minmax(150px, 1fr)); }}
      .toolbar {{ grid-template-columns: 1fr; }}
      main {{ padding: 16px; }}
      header {{ padding: 22px 18px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>{escape(title)}</h1>
    <p>Gerado em <span id="generatedAt"></span>. Relatório autocontido a partir das planilhas de lacunas e diagnóstico.</p>
  </header>
  <main>
    <section class="cards" id="cards"></section>
    <section class="toolbar">
      <input id="search" type="search" placeholder="Buscar por time, partida_id, observação, fonte, erro...">
      <select id="season"></select>
      <select id="limit">
        <option value="100">Mostrar 100</option>
        <option value="250">Mostrar 250</option>
        <option value="500">Mostrar 500</option>
        <option value="1000">Mostrar 1000</option>
        <option value="0">Mostrar tudo</option>
      </select>
    </section>
    <nav class="tabs" id="tabs"></nav>
    <section class="panel">
      <div class="panel-head">
        <div>
          <h2 id="datasetTitle"></h2>
          <p id="datasetDescription"></p>
        </div>
        <div class="count" id="rowCount"></div>
      </div>
      <div class="table-wrap" id="tableWrap"></div>
    </section>
    <div class="sources" id="sources"></div>
  </main>
  <script>
    const payload = {payload_json};
    const state = {{ active: "tecnicos", search: "", season: "", limit: 100 }};
    const datasetOrder = ["resumo", "temporadas", "tecnicos", "formacoes_diagnostico", "gols", "cartoes", "erros"];

    function asText(value) {{
      if (value === null || value === undefined) return "";
      return String(value);
    }}

    function esc(value) {{
      return asText(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
    }}

    function renderCards() {{
      document.getElementById("cards").innerHTML = payload.summary_cards.map(card => `
        <div class="metric">
          <strong>${{esc(card.value)}}</strong>
          <span>${{esc(card.label)}} · ${{esc(card.hint)}}</span>
        </div>
      `).join("");
    }}

    function renderTabs() {{
      document.getElementById("tabs").innerHTML = datasetOrder.map(key => {{
        const dataset = payload.datasets[key];
        const total = dataset.rows.length;
        return `<button class="tab ${{state.active === key ? "active" : ""}}" data-key="${{key}}">${{esc(dataset.label)}} (${{total}})</button>`;
      }}).join("");
      document.querySelectorAll(".tab").forEach(button => {{
        button.addEventListener("click", () => {{
          state.active = button.dataset.key;
          render();
        }});
      }});
    }}

    function renderSeasonOptions() {{
      const options = [`<option value="">Todas temporadas</option>`]
        .concat(payload.seasons.map(season => `<option value="${{esc(season)}}">${{esc(season)}}</option>`));
      const select = document.getElementById("season");
      select.innerHTML = options.join("");
      select.value = state.season;
    }}

    function filteredRows(dataset) {{
      const query = state.search.trim().toLowerCase();
      return dataset.rows.filter(row => {{
        if (state.season && asText(row.temporada) !== state.season) return false;
        if (!query) return true;
        return Object.values(row).some(value => asText(value).toLowerCase().includes(query));
      }});
    }}

    function cellHtml(value) {{
      const text = asText(value);
      if (/^https?:\\/\\//i.test(text)) {{
        return `<a href="${{esc(text)}}" target="_blank" rel="noreferrer">${{esc(text)}}</a>`;
      }}
      return esc(text);
    }}

    function renderTable(dataset, rows) {{
      const columns = dataset.columns;
      const limit = Number(state.limit);
      const visible = limit > 0 ? rows.slice(0, limit) : rows;
      if (!columns.length || !visible.length) {{
        document.getElementById("tableWrap").innerHTML = `<div class="empty">Nenhum registro para os filtros atuais.</div>`;
        return;
      }}
      const head = columns.map(col => `<th>${{esc(col)}}</th>`).join("");
      const body = visible.map(row => `
        <tr>${{columns.map(col => `<td>${{cellHtml(row[col])}}</td>`).join("")}}</tr>
      `).join("");
      document.getElementById("tableWrap").innerHTML = `<table><thead><tr>${{head}}</tr></thead><tbody>${{body}}</tbody></table>`;
    }}

    function render() {{
      const dataset = payload.datasets[state.active];
      const rows = filteredRows(dataset);
      document.getElementById("generatedAt").textContent = payload.generated_at;
      document.getElementById("datasetTitle").textContent = dataset.label;
      document.getElementById("datasetDescription").textContent = dataset.description;
      const limit = Number(state.limit);
      const suffix = limit > 0 && rows.length > limit ? `, exibindo ${{limit}}` : "";
      document.getElementById("rowCount").textContent = `${{rows.length}} registro(s)${{suffix}}`;
      renderCards();
      renderTabs();
      renderSeasonOptions();
      renderTable(dataset, rows);
      document.getElementById("sources").textContent = `Fontes locais: ${{payload.source_files.join(" · ")}}`;
    }}

    document.getElementById("search").addEventListener("input", event => {{
      state.search = event.target.value;
      render();
    }});
    document.getElementById("season").addEventListener("change", event => {{
      state.season = event.target.value;
      render();
    }});
    document.getElementById("limit").addEventListener("change", event => {{
      state.limit = Number(event.target.value);
      render();
    }});

    render();
  </script>
</body>
</html>
"""


def main() -> int:
    payload = build_payload()
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(html_document(payload), encoding="utf-8")
    print(f"OK -> {OUTPUT_HTML}")
    print(f"datasets: {', '.join(payload['datasets'].keys())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
