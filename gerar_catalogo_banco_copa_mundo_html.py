"""Gera um HTML de catalogo do banco relacional da Copa do Mundo."""
from __future__ import annotations

import html
import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DB = ROOT / "db" / "copa_mundo.db"
OUT = ROOT / "catalogo_banco_copa_mundo.html"


def h(valor) -> str:
    if valor is None:
        return '<span class="null">NULL</span>'
    return html.escape(str(valor))


def tabela_html(headers: list[str], rows: list[tuple], classe: str = "") -> str:
    head = "".join(f"<th>{h(c)}</th>" for c in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{h(v)}</td>" for v in row) + "</tr>")
    return f'<div class="table-wrap {classe}"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def objetos(con: sqlite3.Connection, tipo: str) -> list[str]:
    return [
        r[0]
        for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type=? AND name NOT LIKE 'sqlite_%' ORDER BY name",
            (tipo,),
        )
    ]


def colunas(con: sqlite3.Connection, tabela: str) -> list[tuple]:
    return con.execute(f'PRAGMA table_info("{tabela}")').fetchall()


def fks(con: sqlite3.Connection, tabela: str) -> list[tuple]:
    return con.execute(f'PRAGMA foreign_key_list("{tabela}")').fetchall()


def indices(con: sqlite3.Connection, tabela: str) -> list[tuple]:
    saida = []
    for idx in con.execute(f'PRAGMA index_list("{tabela}")').fetchall():
        seq, nome, unico, origem, parcial = idx
        cols = ", ".join(r[2] for r in con.execute(f'PRAGMA index_info("{nome}")').fetchall())
        saida.append((nome, "sim" if unico else "nao", origem, "sim" if parcial else "nao", cols))
    return saida


def count_rows(con: sqlite3.Connection, tabela: str) -> int:
    return con.execute(f'SELECT COUNT(*) FROM "{tabela}"').fetchone()[0]


def sample_rows(con: sqlite3.Connection, tabela: str, limit: int = 12) -> tuple[list[str], list[tuple]]:
    cols = [r[1] for r in colunas(con, tabela)]
    rows = con.execute(f'SELECT * FROM "{tabela}" LIMIT ?', (limit,)).fetchall()
    return cols, rows


def relationship_edges(con: sqlite3.Connection, tabelas: list[str]) -> list[tuple[str, str, str, str]]:
    edges = []
    for tabela in tabelas:
        for fk in fks(con, tabela):
            # id, seq, table, from, to, on_update, on_delete, match
            edges.append((tabela, fk[3], fk[2], fk[4]))
    return edges


def top_artilheiros(con: sqlite3.Connection, ate_ano: int | None = None, limit: int = 15) -> list[tuple]:
    filtro = "AND e.ano <= ?" if ate_ano else ""
    params = (ate_ano, limit) if ate_ano else (limit,)
    return con.execute(
        f"""
        SELECT
            ip.nome_canonico AS jogador,
            GROUP_CONCAT(DISTINCT s.nome) AS selecoes,
            COUNT(*) AS gols,
            MIN(e.ano) AS primeira_copa_com_gol,
            MAX(e.ano) AS ultima_copa_com_gol
        FROM gol g
        JOIN edicao e ON e.edicao_id = g.edicao_id
        JOIN pessoa p ON p.pessoa_id = g.pessoa_id
        JOIN identidade_pessoa ip ON ip.identidade_pessoa_id = p.identidade_pessoa_id
        JOIN selecao s ON s.selecao_id = COALESCE(g.selecao_autor_id, g.selecao_id)
        WHERE g.tipo <> 'gol_contra' {filtro}
        GROUP BY ip.identidade_pessoa_id
        ORDER BY gols DESC, jogador
        LIMIT ?
        """,
        params,
    ).fetchall()


def contagem(con: sqlite3.Connection, tabela: str) -> int:
    return con.execute(f'SELECT COUNT(*) FROM "{tabela}"').fetchone()[0]


def gerar() -> None:
    if not DB.exists():
        raise SystemExit(f"Banco nao encontrado: {DB}")

    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON")
    tabelas = objetos(con, "table")
    views = objetos(con, "view")
    edges = relationship_edges(con, tabelas)
    artilheiros_2022 = top_artilheiros(con, 2022, 20)
    artilheiros_total = top_artilheiros(con, None, 20)

    cards = []
    for tabela in tabelas:
        cards.append(
            f"""
            <a class="metric" href="#tbl-{html.escape(tabela)}">
              <span>{html.escape(tabela)}</span>
              <strong>{count_rows(con, tabela):,}</strong>
              <small>linhas</small>
            </a>
            """.replace(",", ".")
        )

    rel_rows = [(origem, coluna, destino, destino_coluna) for origem, coluna, destino, destino_coluna in edges]

    sections = []
    for tabela in tabelas:
        col_rows = []
        for cid, nome, tipo, notnull, default, pk in colunas(con, tabela):
            fk_match = [fk for fk in fks(con, tabela) if fk[3] == nome]
            rel = ""
            if fk_match:
                rel = "; ".join(f"{fk[2]}.{fk[4]}" for fk in fk_match)
            col_rows.append(
                (
                    nome,
                    tipo or "",
                    "sim" if pk else "nao",
                    "sim" if notnull else "nao",
                    default if default is not None else "",
                    rel,
                )
            )
        sample_headers, sample = sample_rows(con, tabela)
        sections.append(
            f"""
            <section class="panel" id="tbl-{html.escape(tabela)}">
              <div class="panel-head">
                <div>
                  <p class="eyebrow">Tabela</p>
                  <h2>{html.escape(tabela)}</h2>
                </div>
                <div class="badge">{count_rows(con, tabela):,} linhas</div>
              </div>
              <h3>Colunas</h3>
              {tabela_html(["Coluna", "Tipo", "PK", "Obrigatoria", "Padrao", "Relacionamento"], col_rows)}
              <h3>Indices</h3>
              {tabela_html(["Indice", "Unico", "Origem", "Parcial", "Colunas"], indices(con, tabela)) if indices(con, tabela) else '<p class="empty">Sem indices explicitos.</p>'}
              <h3>Amostra de conteudo</h3>
              {tabela_html(sample_headers, sample, "sample") if sample else '<p class="empty">Tabela vazia.</p>'}
            </section>
            """.replace(",", ".")
        )

    view_sections = []
    for view in views:
        headers = [r[1] for r in con.execute(f'PRAGMA table_info("{view}")').fetchall()]
        rows = con.execute(f'SELECT * FROM "{view}" LIMIT 12').fetchall()
        sql = con.execute("SELECT sql FROM sqlite_master WHERE type='view' AND name=?", (view,)).fetchone()[0]
        view_sections.append(
            f"""
            <section class="panel" id="view-{html.escape(view)}">
              <div class="panel-head">
                <div>
                  <p class="eyebrow">View</p>
                  <h2>{html.escape(view)}</h2>
                </div>
              </div>
              <pre>{h(sql)}</pre>
              <h3>Amostra</h3>
              {tabela_html(headers, rows, "sample") if rows else '<p class="empty">View sem linhas.</p>'}
            </section>
            """
        )

    html_out = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Catalogo do Banco da Copa do Mundo</title>
  <style>
    :root {{
      --bg: #06150f;
      --panel: #0d2a1d;
      --panel2: #0a2118;
      --line: #244f3b;
      --text: #f4fff9;
      --muted: #a9c8bb;
      --accent: #25c76a;
      --gold: #f6c64f;
      --blue: #38bdf8;
      --danger: #fb7185;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background:
        linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px),
        var(--bg);
      background-size: 96px 96px;
      color: var(--text);
    }}
    header {{
      padding: 28px 32px 22px;
      border-bottom: 1px solid var(--line);
      background: rgba(6, 21, 15, .92);
      position: sticky;
      top: 0;
      z-index: 5;
    }}
    h1 {{ margin: 0 0 8px; font-size: 28px; }}
    h2 {{ margin: 0; font-size: 22px; }}
    h3 {{ margin: 22px 0 10px; font-size: 16px; color: var(--gold); }}
    p {{ color: var(--muted); }}
    .tabs {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px; }}
    .tabs a {{
      color: var(--text);
      text-decoration: none;
      border: 1px solid var(--line);
      padding: 9px 12px;
      border-radius: 6px;
      background: #092016;
      font-weight: 700;
    }}
    main {{ padding: 24px 32px 48px; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 12px;
      margin-bottom: 24px;
    }}
    .metric {{
      display: block;
      min-height: 94px;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel2);
      text-decoration: none;
      color: var(--text);
    }}
    .metric span {{ display: block; color: var(--muted); font-size: 13px; }}
    .metric strong {{ display: block; margin-top: 8px; font-size: 26px; color: var(--accent); }}
    .metric small {{ color: var(--muted); }}
    .panel {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgba(13, 42, 29, .88);
      padding: 18px;
      margin-bottom: 20px;
    }}
    .panel-head {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: flex-start;
      border-bottom: 1px solid var(--line);
      padding-bottom: 12px;
      margin-bottom: 12px;
    }}
    .eyebrow {{
      margin: 0 0 4px;
      text-transform: uppercase;
      letter-spacing: .08em;
      font-size: 11px;
      color: var(--muted);
    }}
    .badge {{
      border: 1px solid var(--line);
      background: #092016;
      color: var(--gold);
      border-radius: 999px;
      padding: 8px 12px;
      white-space: nowrap;
      font-weight: 700;
    }}
    .table-wrap {{
      overflow: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      max-height: 420px;
      background: #071b13;
    }}
    .table-wrap.sample {{ max-height: 340px; }}
    table {{
      width: 100%;
      min-width: 760px;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      padding: 10px 12px;
      border-bottom: 1px solid rgba(36, 79, 59, .75);
      text-align: left;
      vertical-align: top;
      white-space: nowrap;
    }}
    th {{
      position: sticky;
      top: 0;
      z-index: 1;
      background: #0d2a1d;
      color: #bfe7d8;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: .06em;
    }}
    td {{ color: #eefcf5; }}
    .null {{ color: var(--danger); font-style: italic; }}
    .empty {{ margin: 0; padding: 14px; border: 1px dashed var(--line); border-radius: 8px; }}
    pre {{
      overflow: auto;
      background: #071b13;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      color: #dff8ee;
      white-space: pre-wrap;
    }}
    .relationship-map {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 10px;
    }}
    .story-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin: 16px 0 24px;
    }}
    .story-card {{
      border: 1px solid var(--line);
      background: #071b13;
      border-radius: 8px;
      padding: 15px;
    }}
    .story-card h3 {{
      margin-top: 0;
      color: var(--text);
      font-size: 17px;
    }}
    .story-card p {{ margin-bottom: 0; line-height: 1.45; }}
    .flow {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 8px;
      margin: 14px 0 18px;
    }}
    .flow div {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #092016;
      color: var(--muted);
    }}
    .flow strong {{ display: block; color: var(--gold); margin-bottom: 4px; }}
    .callout {{
      border-left: 4px solid var(--gold);
      background: rgba(246, 198, 79, .08);
      padding: 12px 14px;
      border-radius: 0 8px 8px 0;
      color: var(--muted);
      margin: 14px 0;
      line-height: 1.45;
    }}
    code {{
      color: #d8fbe8;
      background: rgba(255,255,255,.06);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 4px;
      padding: 1px 5px;
    }}
    .edge {{
      border: 1px solid var(--line);
      background: #071b13;
      border-radius: 8px;
      padding: 12px;
      color: var(--muted);
    }}
    .edge strong {{ color: var(--blue); }}
    @media (max-width: 760px) {{
      header, main {{ padding-left: 16px; padding-right: 16px; }}
      .panel-head {{ display: block; }}
      .badge {{ display: inline-block; margin-top: 10px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Catalogo do Banco da Copa do Mundo</h1>
    <p>Arquivo: <strong>{h(DB.name)}</strong> · Tabelas: <strong>{len(tabelas)}</strong> · Views: <strong>{len(views)}</strong> · Relacionamentos: <strong>{len(edges)}</strong></p>
    <nav class="tabs">
      <a href="#guia">Guia</a>
      <a href="#perguntas">Perguntas</a>
      <a href="#resumo">Resumo</a>
      <a href="#relacionamentos">Relacionamentos</a>
      <a href="#views">Views</a>
      <a href="#tabelas">Tabelas</a>
    </nav>
  </header>
  <main>
    <section class="panel" id="guia">
      <div class="panel-head">
        <div>
          <p class="eyebrow">Guia de leitura</p>
          <h2>Como este banco esta organizado</h2>
        </div>
      </div>
      <div class="story-grid">
        <div class="story-card">
          <h3>1. Competicao e edicoes</h3>
          <p><code>competicao</code> define a Copa do Mundo; <code>edicao</code> guarda cada ano, sede, campeao, vice, top 4 e totais.</p>
        </div>
        <div class="story-card">
          <h3>2. Selecoes e participacoes</h3>
          <p><code>selecao</code> e a dimensao de pais/time; <code>participacao_edicao</code> registra campanha, grupo, posicao, pontos e gols.</p>
        </div>
        <div class="story-card">
          <h3>3. Partidas e eventos</h3>
          <p><code>partida</code> guarda o jogo; <code>gol</code> guarda cada gol. Em gol contra, ha selecao creditada e selecao autora.</p>
        </div>
        <div class="story-card">
          <h3>4. Pessoas e identidade</h3>
          <p><code>pessoa</code> e contextual por selecao; <code>identidade_pessoa</code> une casos globais sem perder a estatistica por selecao.</p>
        </div>
      </div>
      <div class="flow">
        <div><strong>edicao</strong> ano, sede, campeao</div>
        <div><strong>fase / grupo</strong> estrutura do torneio</div>
        <div><strong>partida</strong> placar, data, estadio</div>
        <div><strong>gol</strong> autor, minuto, tipo</div>
        <div><strong>escalacao</strong> titulares e reservas</div>
      </div>
      <div class="callout">
        O banco foi desenhado para responder perguntas analiticas. Exemplo: "quem fez mais gols na historia das Copas?"
        A resposta vem de <code>gol</code> + <code>pessoa</code> + <code>identidade_pessoa</code>, filtrando <code>gol_contra</code>.
      </div>
    </section>

    <section class="panel" id="perguntas">
      <div class="panel-head">
        <div>
          <p class="eyebrow">Consultas prontas</p>
          <h2>Perguntas que o banco ja responde</h2>
        </div>
      </div>
      <div class="story-grid">
        <div class="story-card"><h3>Artilheiros historicos</h3><p>Soma gols por identidade global, evitando separar o mesmo jogador por alias.</p></div>
        <div class="story-card"><h3>Campanha de uma selecao</h3><p>Junta participacao, grupos, partidas, gols e classificacao final.</p></div>
        <div class="story-card"><h3>Detalhe de uma partida</h3><p>Combina placar, estadio, publico, arbitro, gols e escalacoes.</p></div>
        <div class="story-card"><h3>Auditoria de nomes</h3><p>Mostra aliases que ainda precisam de revisao humana ou cruzamento externo.</p></div>
      </div>
      <h3>Top artilheiros historicos, recorte fechado 1930-2022</h3>
      {tabela_html(["Jogador", "Selecao", "Gols", "Primeira copa com gol", "Ultima copa com gol"], artilheiros_2022)}
      <div class="callout">
        Este recorte e o mais adequado para comparar com rankings historicos fechados. Depois da correcao do parser da final de 2002,
        o topo calculado pelo banco retorna Klose 16, Ronaldo 15, Gerd Muller 14, Fontaine 13, Messi 13, Mbappe 12 e Pele 12.
      </div>
      <h3>Top artilheiros incluindo 2026 em andamento</h3>
      {tabela_html(["Jogador", "Selecao", "Gols", "Primeira copa com gol", "Ultima copa com gol"], artilheiros_total)}
      <div class="callout">
        Como 2026 esta em andamento no payload deste projeto, este ranking e operacional e muda conforme o cache for atualizado.
        Para comparacao historica consolidada, use o recorte ate 2022.
      </div>
    </section>

    <section id="resumo">
      <h2>Resumo das tabelas</h2>
      <p>Cada card mostra a quantidade de linhas e leva ao detalhe da tabela.</p>
      <div class="grid">{''.join(cards)}</div>
    </section>

    <section class="panel" id="relacionamentos">
      <div class="panel-head">
        <div>
          <p class="eyebrow">Modelo relacional</p>
          <h2>Chaves estrangeiras</h2>
        </div>
        <div class="badge">{len(edges)} relacoes</div>
      </div>
      {tabela_html(["Tabela origem", "Coluna", "Tabela destino", "Coluna destino"], rel_rows)}
      <h3>Mapa rapido</h3>
      <div class="relationship-map">
        {''.join(f'<div class="edge"><strong>{h(o)}.{h(c)}</strong> → {h(d)}.{h(dc)}</div>' for o, c, d, dc in edges)}
      </div>
    </section>

    <section id="views">
      <h2>Views</h2>
      <p>Consultas prontas criadas no schema.</p>
      {''.join(view_sections) if view_sections else '<p class="empty">Nenhuma view encontrada.</p>'}
    </section>

    <section id="tabelas">
      <h2>Tabelas, colunas e conteudo</h2>
      <p>Amostras limitadas a 12 linhas por tabela para manter a pagina leve.</p>
      {''.join(sections)}
    </section>
  </main>
</body>
</html>
"""
    OUT.write_text(html_out, encoding="utf-8")
    con.close()
    print(f"Catalogo gerado: {OUT}")


if __name__ == "__main__":
    gerar()
