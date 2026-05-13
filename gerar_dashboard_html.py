"""Dashboard Brasileirao — le do banco SQLite (db/brasileirao.db)."""
from pathlib import Path
import json
import sqlite3
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DB = ROOT / "db" / "brasileirao.db"

if not DB.exists():
    raise SystemExit(f"❌ Banco nao encontrado em {DB}. Rode 'py criar_banco_brasileirao.py' antes.")

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

print(f"📂 Lendo banco {DB}")

temporadas = [r[0] for r in con.execute(
    "SELECT temporada_id FROM dim_temporada ORDER BY temporada_id"
).fetchall()]
print(f"   temporadas: {temporadas}")

# Mapa clube_id -> nome (resolve uma vez, usa em tudo)
clube_nome = dict(con.execute("SELECT clube_id, nome FROM dim_clube").fetchall())

# ----- matches -----
matches = []
for r in con.execute("""
    SELECT p.partida_id, p.temporada_id, p.rodada, p.data,
           cm.nome AS mandante, cv.nome AS visitante,
           p.gols_mandante, p.gols_visitante,
           cw.nome AS vencedor,
           a.nome AS arena,
           tm.nome AS tec_m, tv.nome AS tec_v,
           p.formacao_mandante, p.formacao_visitante,
           p.uf_mandante, p.uf_visitante
    FROM fato_partida p
    JOIN dim_clube cm ON cm.clube_id = p.mandante_id
    JOIN dim_clube cv ON cv.clube_id = p.visitante_id
    LEFT JOIN dim_clube cw   ON cw.clube_id = p.vencedor_id
    LEFT JOIN dim_arena a    ON a.arena_id = p.arena_id
    LEFT JOIN dim_tecnico tm ON tm.tecnico_id = p.tecnico_mand_id
    LEFT JOIN dim_tecnico tv ON tv.tecnico_id = p.tecnico_vis_id
"""):
    iso = r["data"]
    # data BR = DD/MM/YYYY; banco guarda em ISO
    d_br = f"{iso[8:10]}/{iso[5:7]}/{iso[0:4]}" if iso else ""
    matches.append({
        "id": r["partida_id"], "temporada": r["temporada_id"], "rodada": r["rodada"],
        "data": d_br, "data_iso": iso,
        "mandante": r["mandante"], "visitante": r["visitante"],
        "gm": r["gols_mandante"], "gv": r["gols_visitante"],
        "vencedor": r["vencedor"] or "Empate",
        "arena": r["arena"] or "",
        "tec_m": r["tec_m"] or "", "tec_v": r["tec_v"] or "",
        "form_m": r["formacao_mandante"] or "", "form_v": r["formacao_visitante"] or "",
        "uf_m": r["uf_mandante"] or "", "uf_v": r["uf_visitante"] or "",
    })

# ----- gols -----
goals_data = []
for r in con.execute("""
    SELECT g.partida_id, g.temporada_id, g.rodada, c.nome AS clube,
           j.nome AS atleta, g.minuto, g.tipo
    FROM fato_gol g
    JOIN dim_clube c   ON c.clube_id = g.clube_id
    JOIN dim_jogador j ON j.jogador_id = g.jogador_id
"""):
    goals_data.append({
        "temporada": r["temporada_id"], "partida_id": r["partida_id"],
        "rodada": r["rodada"], "clube": r["clube"], "atleta": r["atleta"],
        "minuto": r["minuto"] or 0, "tipo": r["tipo"] or "Normal",
    })

# ----- cartoes -----
cards_data = []
for r in con.execute("""
    SELECT c.partida_id, c.temporada_id, c.rodada, cl.nome AS clube,
           j.nome AS atleta, c.tipo, p.nome AS posicao, c.minuto, c.num_camisa
    FROM fato_cartao c
    JOIN dim_clube   cl ON cl.clube_id = c.clube_id
    JOIN dim_jogador j  ON j.jogador_id = c.jogador_id
    LEFT JOIN dim_posicao p ON p.posicao_id = c.posicao_id
"""):
    cards_data.append({
        "temporada": r["temporada_id"], "partida_id": r["partida_id"],
        "rodada": r["rodada"], "clube": r["clube"], "atleta": r["atleta"],
        "tipo": r["tipo"], "posicao": r["posicao"] or "",
        "minuto": r["minuto"] or 0, "num_camisa": r["num_camisa"] or "",
    })

# ----- stats -----
stats_data = []
for r in con.execute("""
    SELECT s.partida_id, s.temporada_id, s.rodada, c.nome AS clube,
           s.chutes, s.chutes_alvo, s.posse, s.passes, s.prec_passes,
           s.faltas, s.amarelos, s.vermelhos, s.impedimentos, s.escanteios
    FROM fato_stats_time s
    JOIN dim_clube c ON c.clube_id = s.clube_id
"""):
    stats_data.append({
        "temporada": r["temporada_id"], "partida_id": r["partida_id"],
        "rodada": r["rodada"], "clube": r["clube"],
        "chutes": r["chutes"] or 0, "chutes_alvo": r["chutes_alvo"] or 0,
        "posse": r["posse"] or 0, "passes": r["passes"] or 0,
        "prec_passes": r["prec_passes"] or 0, "faltas": r["faltas"] or 0,
        "amarelos": r["amarelos"] or 0, "vermelhos": r["vermelhos"] or 0,
        "impedimentos": r["impedimentos"] or 0, "escanteios": r["escanteios"] or 0,
    })

# ----- classificacao rodada-a-rodada (a tabela ouro) -----
class_rodada = []
for r in con.execute("""
    SELECT cr.temporada_id, cr.rodada, c.nome AS clube,
           cr.posicao, cr.pontos, cr.jogos, cr.vitorias, cr.empates, cr.derrotas,
           cr.gols_pro, cr.gols_contra, cr.saldo_gols, cr.aproveitamento,
           cr.pontos_mand, cr.pontos_vis, cr.jogos_mand, cr.jogos_vis, cr.zona
    FROM fato_classificacao_rodada cr
    JOIN dim_clube c ON c.clube_id = cr.clube_id
"""):
    class_rodada.append({
        "temporada": r["temporada_id"], "rodada": r["rodada"], "clube": r["clube"],
        "pos": r["posicao"], "p": r["pontos"], "j": r["jogos"],
        "v": r["vitorias"], "e": r["empates"], "d": r["derrotas"],
        "gp": r["gols_pro"], "gc": r["gols_contra"], "sg": r["saldo_gols"],
        "apr": r["aproveitamento"],
        "pm": r["pontos_mand"], "pv": r["pontos_vis"],
        "jm": r["jogos_mand"], "jv": r["jogos_vis"], "zona": r["zona"],
    })

# ----- classificacao final historica nacional -----
class_final_hist = []
for r in con.execute("""
    SELECT temporada_id, edicao_id, competicao_nome, tipo, posicao,
           clube_id, clube, uf, fonte, observacao
    FROM vw_classificacao_final_historica
    ORDER BY temporada_id, edicao_id, posicao
"""):
    class_final_hist.append({
        "temporada": r["temporada_id"],
        "edicao_id": r["edicao_id"],
        "competicao": r["competicao_nome"],
        "tipo": r["tipo"] or "",
        "pos": r["posicao"],
        "clube_id": r["clube_id"],
        "clube": r["clube"],
        "uf": r["uf"] or "",
        "fonte": r["fonte"] or "",
        "obs": r["observacao"] or "",
    })

# ----- Copa do Brasil (objetos independentes; nao altera Serie A) -----
copa_finais = []
if con.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_copa_brasil_finais'").fetchone():
    for r in con.execute("""
        SELECT ano, campeao, uf_campeao, vice, uf_vice, gols_campeao, gols_vice,
               criterio_decisao, resumo_decisao, fonte_url
        FROM vw_copa_brasil_finais
        ORDER BY ano
    """):
        copa_finais.append({
            "ano": r["ano"], "campeao": r["campeao"], "uf_campeao": r["uf_campeao"] or "",
            "vice": r["vice"], "uf_vice": r["uf_vice"] or "",
            "gols_campeao": r["gols_campeao"], "gols_vice": r["gols_vice"],
            "criterio": r["criterio_decisao"] or "", "resumo": r["resumo_decisao"] or "",
            "fonte": r["fonte_url"] or "",
        })

copa_desempenho = []
if con.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_copa_brasil_desempenho_clube'").fetchone():
    for r in con.execute("""
        SELECT clube, uf, titulos, vices, finais, primeira_final, ultima_final
        FROM vw_copa_brasil_desempenho_clube
        ORDER BY titulos DESC, vices DESC, finais DESC, clube
    """):
        copa_desempenho.append({
            "clube": r["clube"], "uf": r["uf"] or "", "titulos": r["titulos"] or 0,
            "vices": r["vices"] or 0, "finais": r["finais"] or 0,
            "primeira_final": r["primeira_final"], "ultima_final": r["ultima_final"],
        })

copa_partidas_finais = []
if con.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_copa_brasil_partidas_finais'").fetchone():
    for r in con.execute("""
        SELECT ano, jogo, mandante, uf_mandante, gols_mandante, gols_visitante,
               visitante, uf_visitante, estadio, local, fonte_url
        FROM vw_copa_brasil_partidas_finais
        ORDER BY ano, jogo
    """):
        copa_partidas_finais.append({
            "ano": r["ano"], "jogo": r["jogo"], "mandante": r["mandante"], "uf_mandante": r["uf_mandante"] or "",
            "gm": r["gols_mandante"], "gv": r["gols_visitante"], "visitante": r["visitante"],
            "uf_visitante": r["uf_visitante"] or "", "estadio": r["estadio"] or "",
            "local": r["local"] or "", "fonte": r["fonte_url"] or "",
        })

copa_edicoes = []
if con.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_copa_brasil_edicoes_completas'").fetchone():
    for r in con.execute("""
        SELECT ano, nome, datas, num_times, jogos, gols, artilheiro, campeao, vice,
               gols_campeao, gols_vice, criterio_decisao, participantes_mapeados, fonte_url
        FROM vw_copa_brasil_edicoes_completas
        ORDER BY ano
    """):
        copa_edicoes.append({
            "ano": r["ano"], "nome": r["nome"], "datas": r["datas"] or "",
            "num_times": r["num_times"] or 0, "jogos": r["jogos"] or 0, "gols": r["gols"] or 0,
            "artilheiro": r["artilheiro"] or "", "campeao": r["campeao"] or "", "vice": r["vice"] or "",
            "gols_campeao": r["gols_campeao"] or 0, "gols_vice": r["gols_vice"] or 0,
            "criterio": r["criterio_decisao"] or "", "participantes_mapeados": r["participantes_mapeados"] or 0,
            "fonte": r["fonte_url"] or "",
        })

copa_participantes = []
if con.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_copa_brasil_participantes'").fetchone():
    for r in con.execute("""
        SELECT ano, clube, uf, associacao, criterio_classificacao, entra_terceira_fase, fonte_url
        FROM vw_copa_brasil_participantes
        ORDER BY ano, clube
    """):
        copa_participantes.append({
            "ano": r["ano"], "clube": r["clube"], "uf": r["uf"] or "",
            "associacao": r["associacao"] or "", "criterio": r["criterio_classificacao"] or "",
            "terceira_fase": bool(r["entra_terceira_fase"]), "fonte": r["fonte_url"] or "",
        })

# ----- meta por temporada -----
clubes_por_temporada = {}
rodada_range_por_temporada = {}
for t in temporadas:
    cs = sorted({m["mandante"] for m in matches if m["temporada"] == t} |
                {m["visitante"] for m in matches if m["temporada"] == t})
    clubes_por_temporada[t] = cs
    rs = [m["rodada"] for m in matches if m["temporada"] == t]
    rodada_range_por_temporada[t] = [min(rs), max(rs)] if rs else [1, 38]

con.close()

print(f"   {len(matches)} jogos | {len(goals_data)} gols | {len(cards_data)} cartoes | {len(stats_data)} stats")
print(f"   {len(class_rodada)} snapshots de classificacao")
print(f"   {len(class_final_hist)} linhas de classificacao final historica")
print(f"   {len(copa_finais)} edicoes da Copa do Brasil")

payload = {
    "temporadas": temporadas,
    "ano_default": temporadas[-1],
    "clubes_por_temporada": clubes_por_temporada,
    "rodada_range": rodada_range_por_temporada,
    "matches": matches,
    "goals": goals_data,
    "cards": cards_data,
    "stats": stats_data,
    "class_rodada": class_rodada,
    "class_final_hist": class_final_hist,
    "copa_brasil": {
        "finais": copa_finais,
        "desempenho": copa_desempenho,
        "partidas_finais": copa_partidas_finais,
        "edicoes": copa_edicoes,
        "participantes": copa_participantes,
    },
}

# ====================================================================
# HTML — usa placeholders para evitar conflito com chaves CSS/JS
# ====================================================================
TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Clube Analítico — Brasileirão Série A</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
/* =====  TEMA FUTEBOLÍSTICO  =====
   Estádio noturno, gramado, linhas de campo e leitura de placar. */
:root[data-theme="dark"]{
  --bg:#06100b;
  --bg-grass:#0b2616;
  --panel:#0e1b14;
  --panel2:#14281d;
  --border:#2e4d39;
  --line:#84c493;
  --pitch-line:rgba(241,255,245,.24);
  --scoreboard:#050b08;
  --floodlight:rgba(244,255,225,.12);
  --text:#f1f7f1; --muted:#9bb6a7;
  --accent:#1ecb74;        /* verde gramado */
  --accent2:#f7c948;       /* amarelo placar */
  --accent3:#38bdf8;       /* azul */
  --warn:#fbbf24;
  --danger:#ef4444;        /* vermelho cartão */
  --purple:#a78bfa;
  --header-text:#f8fff8;
  --header-muted:#b9d3c2;
  --top-nav-bg:linear-gradient(180deg, var(--panel), var(--scoreboard));
  --top-nav-text:#b9d3c2;
  --top-nav-hover:#f8fff8;
  --top-nav-active:var(--accent);
  --sub-nav-bg:var(--scoreboard);
  --sub-nav-text:#b9d3c2;
  --sub-nav-hover:#f8fff8;
  --sub-nav-active:var(--accent);
  --row-hover:#1a3326;
  --champ:#fbbf24; --liber:#10b981; --sula:#3b82f6; --reb:#ef4444;
  --shadow: 0 18px 46px rgba(0,0,0,0.34);
  --shadow-sm: 0 8px 22px rgba(0,0,0,0.22);
}
:root[data-theme="light"]{
  --bg:#eef5eb;
  --bg-grass:#dcefd7;
  --panel:#ffffff;
  --panel2:#f4faf1;
  --border:#cfdcc9;
  --line:#7cad83;
  --pitch-line:rgba(20,80,40,.16);
  --scoreboard:#102018;
  --floodlight:rgba(255,255,255,.55);
  --text:#15241c; --muted:#5b7568;
  --accent:#087c43;
  --accent2:#c47d08;
  --accent3:#2563eb;
  --warn:#d97706;
  --danger:#dc2626;
  --purple:#7c3aed;
  --header-text:#f7fff7;
  --header-muted:#c5ddcf;
  --top-nav-bg:#f7fbf4;
  --top-nav-text:#435f51;
  --top-nav-hover:#102018;
  --top-nav-active:#04723d;
  --sub-nav-bg:#0d2519;
  --sub-nav-text:#c1d7ca;
  --sub-nav-hover:#ffffff;
  --sub-nav-active:#32d57f;
  --row-hover:#eaf3e6;
  --champ:#d97706; --liber:#059669; --sula:#2563eb; --reb:#dc2626;
  --shadow: 0 18px 42px rgba(14,44,24,0.12);
  --shadow-sm: 0 8px 20px rgba(14,44,24,0.08);
}
*{box-sizing:border-box}
html, body{margin:0;padding:0;font-family:'Inter','SF Pro Text',-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.5}
[hidden]{display:none!important}

/* Background com gramado e marcações de campo discretas */
body{
  background-image:
    radial-gradient(circle at 10% -10%, var(--floodlight), transparent 26%),
    radial-gradient(circle at 90% -12%, var(--floodlight), transparent 28%),
    linear-gradient(90deg, transparent calc(50% - 1px), var(--pitch-line) calc(50% - 1px), var(--pitch-line) calc(50% + 1px), transparent calc(50% + 1px)),
    radial-gradient(circle at 50% 128px, transparent 0 104px, var(--pitch-line) 105px, transparent 107px),
    repeating-linear-gradient(90deg, rgba(255,255,255,.022) 0 90px, rgba(0,0,0,.06) 90px 180px),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-grass) 100%);
  background-attachment:fixed;
  min-height:100vh;
}

/* ==== HEADER (placar de estádio) ==== */
header{
  padding:30px 36px 26px;
  min-height:154px;
  background:
    radial-gradient(circle at 12% 0%, rgba(255,255,255,.13), transparent 24%),
    radial-gradient(circle at 88% 0%, rgba(255,255,255,.12), transparent 24%),
    linear-gradient(90deg, transparent calc(50% - 1px), var(--pitch-line) calc(50% - 1px), var(--pitch-line) calc(50% + 1px), transparent calc(50% + 1px)),
    radial-gradient(circle at 50% 54%, transparent 0 58px, var(--pitch-line) 59px, transparent 61px),
    repeating-linear-gradient(90deg, rgba(255,255,255,.025) 0 78px, rgba(0,0,0,.07) 78px 156px),
    linear-gradient(135deg, #08150f 0%, #12361f 48%, #07110c 100%);
  border-bottom: 4px solid var(--accent);
  position:relative;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;
  box-shadow: var(--shadow);
  overflow:hidden;
}
header::before{
  content:"";position:absolute;left:0;right:0;bottom:0;height:4px;
  background:repeating-linear-gradient(90deg, var(--accent) 0 42px, var(--accent2) 42px 78px, var(--danger) 78px 88px);
  opacity:0.85;
}
header::after{
  content:"";position:absolute;right:96px;top:20px;width:122px;height:70px;
  border:2px solid var(--pitch-line);border-bottom:0;border-radius:4px 4px 0 0;
  opacity:.75;pointer-events:none;
}
.brand-block{position:relative;z-index:1;max-width:980px}
header h1{
  margin:0;font-size:30px;font-weight:950;letter-spacing:0;
  display:flex;align-items:center;gap:12px;
  text-transform:uppercase;
  color:var(--header-text);
  text-shadow:0 2px 8px rgba(0,0,0,.35);
}
header h1::before{
  content:"⚽";font-size:28px;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
}
header .sub{color:var(--header-muted);font-size:12px;margin-top:6px;font-weight:650;letter-spacing:0.02em}
.match-strip{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.competition-switch{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}
.competition-switch button{
  background:var(--scoreboard);color:var(--header-muted);
  border:1px solid rgba(247,201,72,.42);
  border-radius:6px;padding:7px 11px;cursor:pointer;
  font-size:11px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;
  box-shadow:inset 0 -2px 0 rgba(247,201,72,.14), var(--shadow-sm);
}
.competition-switch button.active{color:var(--header-text);border-color:var(--accent);box-shadow:inset 0 -2px 0 rgba(30,203,116,.35), var(--shadow-sm)}
.score-chip{
  display:inline-flex;align-items:center;gap:7px;
  background:var(--scoreboard);color:var(--header-text);
  border:1px solid rgba(247,201,72,.42);
  border-radius:6px;padding:6px 10px;
  font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  box-shadow:inset 0 -2px 0 rgba(247,201,72,.2), var(--shadow-sm);
}
.score-chip::before{
  content:"";width:7px;height:7px;border-radius:50%;background:var(--accent2);
  box-shadow:0 0 10px var(--accent2);
}

.actions{display:flex;gap:10px;align-items:center;position:relative;z-index:1}
button.btn{
  background:var(--panel2);color:var(--text);border:1px solid var(--border);
  padding:9px 16px;border-radius:6px;cursor:pointer;font-size:12px;font-weight:700;
  letter-spacing:0.02em;transition:all 0.15s ease;
  box-shadow: var(--shadow-sm);
}
button.btn::first-letter{line-height:1}
button.btn:hover{background:var(--row-hover);border-color:var(--accent);transform:translateY(-1px)}
button.btn:active{transform:translateY(0)}
button.btn.primary{
  background: linear-gradient(135deg, var(--accent) 0%, #0a8f63 100%);
  color:#fff;border-color:var(--accent);
  box-shadow: 0 2px 8px rgba(16,185,129,0.35);
}
button.btn.primary:hover{box-shadow: 0 4px 12px rgba(16,185,129,0.5);background: linear-gradient(135deg, #14d496 0%, var(--accent) 100%)}

/* ==== NAV PRIMARY (grupos macro→micro) ==== */
nav.tab-groups{
  display:flex;gap:2px;padding:0 28px;
  background:var(--top-nav-bg);
  border-bottom:1px solid var(--border);
  overflow-x:auto;
}
nav.tab-groups::-webkit-scrollbar{height:3px}
nav.tab-groups::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
nav.tab-groups button{
  background:none;border:none;color:var(--top-nav-text);
  padding:14px 20px;cursor:pointer;font-size:14px;font-weight:800;
  border-bottom:3px solid transparent;white-space:nowrap;
  transition:all 0.15s ease;letter-spacing:0.01em;
  position:relative;
}
nav.tab-groups button:hover{color:var(--top-nav-hover)}
nav.tab-groups button.active{
  color:var(--top-nav-active);border-bottom-color:var(--top-nav-active);
}
nav.tab-groups button.active::before{
  content:""; position:absolute; left:0; right:0; bottom:-1px; height:1px;
  background:var(--top-nav-active); opacity:0.3;
}

/* ==== TABS SECUNDÁRIO (abas do grupo ativo) ==== */
nav.tabs{
  display:flex;gap:4px;padding:6px 28px;
  background:var(--sub-nav-bg);
  border-bottom:1px solid var(--border);
  overflow-x:auto;flex-wrap:wrap;
}
nav.tabs::-webkit-scrollbar{height:3px}
nav.tabs::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
nav.tabs button{
  background:transparent;border:1px solid transparent;color:var(--sub-nav-text);
  padding:7px 12px;cursor:pointer;font-size:12px;font-weight:600;
  white-space:nowrap;border-radius:6px;
  transition:all 0.12s ease;letter-spacing:0.01em;
}
nav.tabs button:hover{color:var(--sub-nav-hover);background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18)}
nav.tabs button.active{
  color:var(--sub-nav-active);background:rgba(25,185,109,0.14);
  border-color:rgba(25,185,109,0.35);
}
nav.tabs button.tab-hidden{display:none}  /* JS controla via classList */

/* ==== FILTROS (estilo painel de placar) ==== */
.filters{
  background:
    linear-gradient(90deg, transparent calc(50% - 1px), var(--pitch-line) calc(50% - 1px), var(--pitch-line) calc(50% + 1px), transparent calc(50% + 1px)),
    linear-gradient(135deg, var(--panel) 0%, var(--panel2) 100%);
  border-bottom:1px solid var(--border);
  padding:18px 36px;
  display:grid;grid-template-columns:auto 2fr 1fr 1fr 1fr auto;gap:18px;align-items:end;
  box-shadow: inset 0 -1px 0 var(--border);
}
.filters.hidden{display:none}
@media(max-width:1100px){.filters{grid-template-columns:1fr 1fr;gap:14px}}

.fld label{
  display:block;font-size:10px;color:var(--muted);
  text-transform:uppercase;letter-spacing:0.08em;
  margin-bottom:6px;font-weight:700;
}

/* Selects custom */
.fld select{
  width:100%;padding:9px 32px 9px 12px;
  background:var(--bg);color:var(--text);
  border:1.5px solid var(--border);border-radius:6px;
  font-size:13px;font-weight:500;font-family:inherit;
  cursor:pointer;transition:all 0.15s ease;
  appearance:none;-webkit-appearance:none;
  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%238aa496' d='M6 8L0 0h12z'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 12px center;
  box-shadow: var(--shadow-sm);
}
.fld select:hover{border-color:var(--accent)}
.fld select:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(16,185,129,0.15)}
.fld select[multiple]{
  height:80px;background-image:none;padding-right:12px;
  border-radius:6px;
}
.fld select[multiple] option{padding:5px 8px;border-radius:4px}
.fld select[multiple] option:checked{background:var(--accent);color:#fff}

/* Inputs */
.fld input[type=text], .fld input[type=number]{
  width:100%;padding:9px 12px;
  background:var(--bg);color:var(--text);
  border:1.5px solid var(--border);border-radius:6px;
  font-size:13px;font-weight:500;font-family:inherit;
}

/* Range sliders custom */
.fld input[type=range]{
  width:100%;-webkit-appearance:none;appearance:none;
  background:transparent;height:24px;
  margin:0;padding:0;border:0;
  cursor:pointer;
}
.fld input[type=range]:focus{outline:none}
.fld input[type=range]::-webkit-slider-runnable-track{
  height:6px;border-radius:3px;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%);
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.15);
}
.fld input[type=range]::-moz-range-track{
  height:6px;border-radius:3px;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%);
}
.fld input[type=range]::-webkit-slider-thumb{
  -webkit-appearance:none;appearance:none;
  width:18px;height:18px;border-radius:50%;
  background: #fff;border:3px solid var(--accent);
  box-shadow: 0 2px 6px rgba(0,0,0,0.25);
  margin-top:-6px;cursor:grab;
  transition:transform 0.1s ease;
}
.fld input[type=range]::-webkit-slider-thumb:hover{transform:scale(1.15)}
.fld input[type=range]::-webkit-slider-thumb:active{cursor:grabbing}
.fld input[type=range]::-moz-range-thumb{
  width:18px;height:18px;border-radius:50%;
  background: #fff;border:3px solid var(--accent);
  box-shadow: 0 2px 6px rgba(0,0,0,0.25);cursor:grab;
}
.fld label .val{
  display:inline-block;background:var(--accent);color:#fff;
  padding:1px 8px;border-radius:10px;font-size:11px;font-weight:700;
  margin-left:6px;
}

/* ============ CUSTOM MULTI-SELECT (clubes com busca) ============ */
.ms{position:relative;width:100%}
.ms-toggle{
  width:100%;padding:9px 32px 9px 12px;
  background:var(--bg);color:var(--text);
  border:1.5px solid var(--border);border-radius:8px;
  font-size:13px;font-weight:500;font-family:inherit;
  cursor:pointer;display:flex;align-items:center;justify-content:space-between;
  text-align:left;transition:border-color .15s, box-shadow .15s;
}
.ms-toggle:hover{border-color:var(--accent)}
.ms-toggle[aria-expanded="true"]{
  border-color:var(--accent);
  box-shadow: 0 0 0 3px rgba(163,230,53,.15);
}
.ms-label{
  flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;padding-right:8px;
}
.ms-label.placeholder{color:var(--muted);font-weight:400}
.ms-caret{
  flex:none;color:var(--muted);transition:transform .15s ease;
}
.ms-toggle[aria-expanded="true"] .ms-caret{transform:rotate(180deg)}

.ms-panel{
  position:absolute;top:calc(100% + 4px);left:0;right:0;z-index:50;
  background:var(--panel);border:1px solid var(--border);
  border-radius:8px;box-shadow: 0 8px 24px rgba(0,0,0,0.25), 0 2px 6px rgba(0,0,0,0.15);
  overflow:hidden;
  animation:msFadeIn .12s ease;
}
@keyframes msFadeIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}

.ms-search-wrap{
  position:relative;padding:10px 10px 6px;
  border-bottom:1px solid var(--border);
}
.ms-search-icon{
  position:absolute;left:20px;top:50%;transform:translateY(-50%);
  color:var(--muted);pointer-events:none;
}
.ms-search{
  width:100%;padding:7px 10px 7px 32px;
  background:var(--bg);color:var(--text);
  border:1px solid var(--border);border-radius:6px;
  font-size:12.5px;font-family:inherit;
  transition:border-color .15s;
}
.ms-search:focus{outline:none;border-color:var(--accent)}

.ms-actions{
  display:flex;gap:6px;padding:6px 10px;
  border-bottom:1px solid var(--border);
  background:rgba(0,0,0,0.03);
}
:root[data-theme="dark"] .ms-actions{background:rgba(255,255,255,0.02)}
.ms-mini{
  flex:1;background:transparent;color:var(--muted);
  border:1px solid var(--border);border-radius:5px;
  padding:4px 8px;font-size:11px;font-weight:600;cursor:pointer;
  font-family:inherit;letter-spacing:.02em;transition:all .12s;
}
.ms-mini:hover{color:var(--accent);border-color:var(--accent);background:rgba(163,230,53,.06)}

.ms-list{
  max-height:240px;overflow-y:auto;
  padding:4px;
}
.ms-list::-webkit-scrollbar{width:6px}
.ms-list::-webkit-scrollbar-track{background:transparent}
.ms-list::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
.ms-list::-webkit-scrollbar-thumb:hover{background:var(--muted)}

.ms-item{
  display:flex;align-items:center;gap:10px;
  padding:7px 10px;border-radius:5px;cursor:pointer;
  font-size:13px;color:var(--text);font-weight:500;
  transition:background .1s;
  user-select:none;
}
.ms-item:hover{background:var(--panel2)}
.ms-item.selected{background:rgba(163,230,53,.10);color:var(--text)}
.ms-item.hidden{display:none}
.ms-cb{
  width:16px;height:16px;border:1.5px solid var(--border-strong);
  border-radius:4px;flex:none;
  display:flex;align-items:center;justify-content:center;
  background:var(--bg);transition:all .12s;
}
.ms-item.selected .ms-cb{
  background:var(--accent);border-color:var(--accent);
}
.ms-cb svg{
  width:11px;height:11px;color:#0c1220;opacity:0;
  transition:opacity .12s;
}
.ms-item.selected .ms-cb svg{opacity:1}
.ms-empty{
  padding:20px;text-align:center;color:var(--muted);font-size:12px;font-style:italic;
}

main{padding:30px 36px;max-width:1540px;margin:0 auto}
.tab-content{display:none;animation:fadeIn 0.25s ease}
.tab-content.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

/* ==== KPIs (cartões de placar) ==== */
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:24px}
.kpi{
  background:
    linear-gradient(90deg, transparent calc(100% - 42px), rgba(255,255,255,.035) calc(100% - 42px), transparent 100%),
    linear-gradient(135deg, var(--panel) 0%, var(--panel2) 100%);
  border:1px solid var(--border);border-radius:8px;
  padding:16px 18px;position:relative;overflow:hidden;
  box-shadow: var(--shadow-sm);
  transition:transform 0.15s ease, box-shadow 0.15s ease;
}
.kpi:hover{transform:translateY(-2px);box-shadow:var(--shadow);border-color:var(--accent)}
.kpi::before{
  content:"";position:absolute;left:0;top:0;bottom:0;width:5px;
  background: repeating-linear-gradient(180deg, var(--accent) 0 14px, var(--accent2) 14px 28px);
}
.kpi .v{font-size:24px;font-weight:800;color:var(--accent);letter-spacing:-0.02em;line-height:1.1}
.kpi .v.small{font-size:15px;font-weight:700}
.kpi .l{font-size:10px;color:var(--muted);margin-top:6px;text-transform:uppercase;letter-spacing:.08em;font-weight:700}
.kpi .sub{font-size:11px;color:var(--muted);margin-top:2px}

/* ==== ROWS / CARDS ==== */
.row{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px}
.row.full{grid-template-columns:1fr}
.row.three{grid-template-columns:1fr 1fr 1fr}
@media(max-width:1000px){.row,.row.three{grid-template-columns:1fr}}
.card{
  background:
    linear-gradient(90deg, rgba(255,255,255,.018) 0 1px, transparent 1px 100%),
    var(--panel);
  background-size:42px 100%, auto;
  border:1px solid var(--border);
  border-radius:8px;padding:18px;overflow:hidden;
  box-shadow: var(--shadow-sm);
  transition:box-shadow 0.15s ease;
  position:relative;
}
.card::before{
  content:"";position:absolute;left:0;right:0;top:0;height:3px;
  background:linear-gradient(90deg, var(--accent), var(--accent2), var(--accent3), var(--danger));
  opacity:.75;
}
.card:hover{box-shadow: var(--shadow)}
.card.hf-filter-card{overflow:visible;z-index:80}
.card h2{
  margin:0 0 14px;font-size:14px;font-weight:700;
  display:flex;align-items:center;gap:8px;
  letter-spacing:0.01em;
}
.card h3{margin:0 0 10px;font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}

/* ==== TABELAS ==== */
.tbl-wrap{max-height:520px;overflow:auto;border-radius:8px}
.tbl-wrap.tall{max-height:700px}
.tbl-wrap::-webkit-scrollbar{width:8px;height:8px}
.tbl-wrap::-webkit-scrollbar-track{background:transparent}
.tbl-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
.tbl-wrap::-webkit-scrollbar-thumb:hover{background:var(--line)}

table{width:100%;border-collapse:collapse;font-size:12.5px}
th{
  position:sticky;top:0;text-align:left;padding:10px 12px;
  background:
    linear-gradient(180deg, var(--panel2), var(--panel));
  color:var(--muted);
  font-weight:700;font-size:10px;text-transform:uppercase;letter-spacing:.08em;
  border-bottom:2px solid var(--border);cursor:pointer;user-select:none;z-index:1;
}
th.sortable:after{content:" ↕";opacity:.4;font-size:9px}
th.sort-asc:after{content:" ↑";opacity:1;color:var(--accent)}
th.sort-desc:after{content:" ↓";opacity:1;color:var(--accent)}
td{padding:8px 12px;border-bottom:1px solid var(--border)}
tr:last-child td{border-bottom:none}
tr:hover td{background:var(--row-hover)}
.num{text-align:right;font-variant-numeric:tabular-nums;font-weight:500}

/* Zonas (faixa lateral colorida estilo bandeirinha) */
.zone-champ{box-shadow: inset 4px 0 0 var(--champ)}
.zone-liber{box-shadow: inset 4px 0 0 var(--liber)}
.zone-sula{box-shadow: inset 4px 0 0 var(--sula)}
.zone-reb{box-shadow: inset 4px 0 0 var(--reb)}

/* ==== BADGES (placares e cartões) ==== */
.tag{
  display:inline-block;padding:2px 8px;border-radius:4px;
  font-size:10.5px;font-weight:700;letter-spacing:0.02em;
}
.tag-V{background:rgba(16,185,129,.18);color:var(--accent);border:1px solid rgba(16,185,129,.3)}
.tag-E{background:rgba(138,164,150,.2);color:var(--muted);border:1px solid var(--border)}
.tag-D{background:rgba(239,68,68,.18);color:var(--danger);border:1px solid rgba(239,68,68,.3)}

/* Streak (V/E/D) — quadradinhos como cartões */
.streak{display:inline-flex;gap:3px}
.streak span{
  display:inline-block;width:16px;height:16px;border-radius:3px;
  font-size:9.5px;font-weight:800;text-align:center;line-height:16px;color:#fff;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
}
.streak .V{background:var(--accent)}
.streak .E{background:var(--muted)}
.streak .D{background:var(--danger)}

.chart{width:100%;height:380px}
.chart-tall{width:100%;height:520px}
.chart-short{width:100%;height:300px}

/* ==== NOTE (banner informativo, formato de bandeirinha de córner) ==== */
.note{
  background:
    linear-gradient(135deg, var(--panel2) 0%, var(--panel) 100%);
  border-left:4px solid var(--accent2);
  padding:12px 18px;border-radius:0 8px 8px 0;
  font-size:12.5px;color:var(--text);margin-bottom:20px;
  box-shadow: var(--shadow-sm);
  position:relative;
}
.note::before{content:"";display:block}

.legend-zones{display:flex;gap:16px;flex-wrap:wrap;font-size:11px;color:var(--muted);margin-bottom:12px}
.legend-zones span{display:inline-flex;align-items:center;gap:6px;font-weight:600}
.legend-zones i{display:inline-block;width:14px;height:14px;border-radius:3px;box-shadow: 0 1px 2px rgba(0,0,0,0.15)}
.club-pill{display:inline-block;background:var(--panel2);padding:2px 8px;border-radius:4px;font-size:10.5px;color:var(--muted);margin-left:4px;font-weight:600}
.copa-tabs{
  display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px;
}
.copa-tabs button{
  background:var(--panel2);color:var(--sub-nav-text);
  border:1px solid var(--border);border-radius:6px;
  padding:8px 13px;cursor:pointer;font-size:12px;font-weight:800;
}
.copa-tabs button.active{color:var(--accent);border-color:var(--accent);background:rgba(30,203,116,.1)}
.copa-filters{
  display:grid;grid-template-columns:180px minmax(260px,1fr) auto;gap:16px;align-items:end;
  background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:14px 16px;margin-bottom:18px;
}
.copa-section{display:none}
.copa-section.active{display:block}
@media(max-width:760px){
  header{padding:22px 18px;min-height:0}
  header::after{display:none}
  header h1{font-size:20px}
  .match-strip{margin-top:10px}
  .score-chip{font-size:10px;padding:5px 8px}
  nav.tabs{padding:0 10px;flex-wrap:nowrap}
  nav.tabs button{padding:12px 13px;font-size:12px}
  .filters{padding:16px 18px;grid-template-columns:1fr!important}
  .copa-filters{grid-template-columns:1fr}
  main{padding:20px 16px}
}
</style>
</head>
<body>

<header>
  <div class="brand-block">
    <div class="competition-switch" id="competition-switch">
      <button data-competition="serie_a" class="active">Campeonato Brasileiro Serie A</button>
      <button data-competition="copa_brasil">Copa do Brasil</button>
    </div>
    <h1 id="main-title">Brasileirão Série A — Clube Analítico</h1>
    <div class="sub" id="hdr-sub">Banco SQLite local · análise rodada a rodada · histórico de clubes</div>
    <div class="match-strip" id="match-strip">
      <span class="score-chip">Série A</span>
      <span class="score-chip">Rodada a rodada</span>
      <span class="score-chip">Scout completo</span>
      <span class="score-chip">Histórico de clubes</span>
    </div>
  </div>
  <div class="actions">
    <button class="btn" id="btn-reset">↺ Limpar filtros</button>
    <button class="btn" id="btn-theme">🌙 Tema</button>
  </div>
</header>

<nav class="tab-groups" id="tab-groups">
  <button data-group="visao-geral" class="active">📊 Visão Geral</button>
  <button data-group="campeonato">🏆 Campeonato</button>
  <button data-group="clubes">🛡️ Clubes</button>
  <button data-group="historico">🌎 Histórico</button>
  <button data-group="pessoas">👤 Pessoas</button>
</nav>

<nav class="tabs" id="tabs">
  <!-- 📊 VISÃO GERAL -->
  <button data-tab="resumo" data-group="visao-geral" class="active">Painel Principal</button>
  <!-- 🏆 CAMPEONATO (1 temporada) -->
  <button data-tab="classificacao" data-group="campeonato">🏆 Tabela</button>
  <button data-tab="campeonato"    data-group="campeonato">🏁 Disputa</button>
  <button data-tab="evolucao"      data-group="campeonato">📈 Evolução</button>
  <button data-tab="forma"         data-group="campeonato">🔥 Forma</button>
  <button data-tab="partidas"      data-group="campeonato">📅 Partidas</button>
  <button data-tab="rankings"      data-group="campeonato">🏅 Rankings</button>
  <!-- 🛡️ CLUBES -->
  <button data-tab="times-geral" data-group="clubes">📋 Ranking Histórico</button>
  <button data-tab="confronto"  data-group="clubes">⚔️ Comparar Clubes</button>
  <button data-tab="mando"      data-group="clubes">🏠 Mando</button>
  <button data-tab="ataque"     data-group="clubes">⚽ Ataque & Defesa</button>
  <button data-tab="disciplina" data-group="clubes">🟨 Disciplina</button>
  <!-- 🌎 HISTÓRICO (cross-temporadas) -->
  <button data-tab="historico"  data-group="historico">🏆 Campeões & Rebaixados</button>
  <button data-tab="historico-final" data-group="historico">Classificação Histórica</button>
  <button data-tab="campanhas"  data-group="historico">👑 Campanhas Marcantes</button>
  <button data-tab="perguntas" data-group="historico">Insights Históricos</button>
  <button data-tab="comparar"   data-group="historico">🆚 Comparar Temporadas</button>
  <button data-tab="geografia"  data-group="historico">🗺️ Mapa Geográfico</button>
  <button data-tab="indices"   data-group="historico">📐 Índices Históricos</button>
  <!-- 👤 PESSOAS -->
  <button data-tab="jogadores" data-group="pessoas">👤 Jogadores</button>
  <button data-tab="tecnicos"  data-group="pessoas">🎓 Técnicos</button>
</nav>

<div class="filters hidden" id="global-filters" style="grid-template-columns:auto 2fr 1fr 1fr 1fr auto">
  <div class="fld"><label>Temporada</label><select id="f-temporada"></select></div>
  <div class="fld"><label>Clubes <span class="val" id="ms-count" style="display:none"></span></label>
    <div class="ms" id="ms-clubes">
      <button type="button" class="ms-toggle" id="ms-toggle" aria-haspopup="listbox" aria-expanded="false">
        <span class="ms-label" id="ms-label">Todos os clubes</span>
        <svg class="ms-caret" width="10" height="6" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="ms-panel" id="ms-panel" hidden>
        <div class="ms-search-wrap">
          <svg class="ms-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input class="ms-search" id="ms-search" type="text" placeholder="Buscar clube...">
        </div>
        <div class="ms-actions">
          <button type="button" class="ms-mini" id="ms-all">Selecionar todos</button>
          <button type="button" class="ms-mini" id="ms-none">Limpar</button>
        </div>
        <div class="ms-list" id="ms-list" role="listbox" aria-multiselectable="true"></div>
      </div>
    </div>
  </div>
  <div class="fld"><label>Rodada mín <span class="val" id="lab-rmin"></span></label><input type="range" id="f-rmin"></div>
  <div class="fld"><label>Rodada máx <span class="val" id="lab-rmax"></span></label><input type="range" id="f-rmax"></div>
  <div class="fld"><label>Resultado</label>
    <select id="f-result">
      <option value="">Todos</option>
      <option value="V_M">Vitória mandante</option>
      <option value="V_V">Vitória visitante</option>
      <option value="E">Empate</option>
    </select>
  </div>
  <div class="fld"><label>&nbsp;</label><button class="btn primary" id="btn-apply" style="width:100%">Aplicar</button></div>
</div>

<main id="serie-a-main">

<!-- ========= RESUMO ========= -->
<div class="tab-content active" id="tab-resumo">
  <div class="kpis" id="kpis-resumo"></div>
  <h3 style="margin:14px 0 8px;color:var(--accent2)">Disputa principal</h3>
  <div class="row">
    <div class="card"><h2>Zona de classificação — G6 por pontos</h2><div id="ch-top6" class="chart"></div></div>
    <div class="card"><h2>Zona de rebaixamento — últimos 4 por pontos</h2><div id="ch-bot4" class="chart"></div></div>
  </div>
  <h3 style="margin:18px 0 8px;color:var(--accent)">Evolução da tabela</h3>
  <div class="row full">
    <div class="card">
      <div style="display:flex;align-items:end;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:10px">
        <div style="min-width:220px;flex:1">
          <label style="font-size:11px;color:var(--muted);text-transform:uppercase">Campeonato</label>
          <select id="camp-race-temp" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select>
        </div>
        <div style="display:flex;align-items:center;gap:10px;flex:2;min-width:320px">
          <button id="camp-race-play" class="btn">Play</button>
          <button id="camp-race-prev" class="btn" title="Rodada anterior">‹</button>
          <div id="camp-race-round-label" style="font-weight:900;color:var(--accent);min-width:95px;text-align:center"></div>
          <button id="camp-race-next" class="btn" title="Próxima rodada">›</button>
          <input id="camp-race-range" type="range" min="0" max="1" value="0" style="flex:1;min-width:180px;accent-color:var(--accent)">
        </div>
      </div>
      <h2>Corrida da classificação rodada a rodada</h2>
      <div id="ch-camp-race" class="chart-tall"></div>
    </div>
  </div>
  <h3 style="margin:18px 0 8px;color:var(--warn)">Produção ofensiva</h3>
  <div class="row">
    <div class="card"><h2>Gols por rodada</h2><div id="ch-gols-rod" class="chart"></div></div>
    <div class="card"><h2>Artilheiros da temporada</h2><div id="ch-art" class="chart"></div></div>
  </div>
</div>

<!-- ========= CLASSIFICAÇÃO ========= -->
<div class="tab-content" id="tab-classificacao">
  <div class="legend-zones">
    <span><i style="background:var(--champ)"></i> Campeão</span>
    <span><i style="background:var(--liber)"></i> G6</span>
    <span><i style="background:var(--sula)"></i> 7º ao 12º</span>
    <span><i style="background:var(--reb)"></i> Z4</span>
  </div>
  <div class="card">
    <h2>Classificação completa</h2>
    <div class="tbl-wrap tall"><table id="tbl-class"></table></div>
  </div>
</div>

<!-- ========= EVOLUÇÃO ========= -->
<div class="tab-content" id="tab-evolucao">
  <div class="note">Selecione clubes nos filtros para destacá-los. Sem seleção, todos os clubes são exibidos.</div>
  <div class="row full"><div class="card"><h2>Pontos acumulados por rodada</h2><div id="ch-evo-pts" class="chart-tall"></div></div></div>
  <div class="row full"><div class="card"><h2>Posição na tabela por rodada</h2><div id="ch-evo-pos" class="chart-tall"></div></div></div>
  <div class="row full"><div class="card"><h2>Saldo de gols acumulado por rodada</h2><div id="ch-evo-sg" class="chart"></div></div></div>
</div>

<!-- ========= TIMES — GERAL (cross-temporada) ========= -->
<div class="tab-content" id="tab-times-geral">
  <div class="note">Visão agregada de todas as temporadas disponíveis por clube. Ignora o filtro global de temporada.</div>
  <div class="kpis" id="kpis-times-geral"></div>
  <div class="row full">
    <div class="card">
      <div style="display:flex;align-items:end;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:10px">
        <div style="min-width:240px;flex:1">
          <label style="font-size:11px;color:var(--muted);text-transform:uppercase">Clube</label>
          <select id="tg-pos-clube" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select>
        </div>
        <div style="display:flex;align-items:center;gap:10px;flex:2;min-width:320px">
          <button id="tg-pos-play" class="btn">Play</button>
          <button id="tg-pos-prev" class="btn" title="Campeonato anterior">‹</button>
          <div id="tg-pos-year-label" style="font-weight:900;color:var(--accent);min-width:100px;text-align:center"></div>
          <button id="tg-pos-next" class="btn" title="Próximo campeonato">›</button>
          <input id="tg-pos-range" type="range" min="0" max="1" value="0" style="flex:1;min-width:180px;accent-color:var(--accent)">
        </div>
      </div>
      <h2>Posições finais acumuladas por clube</h2>
      <div id="ch-tg-pos-race" class="chart-tall"></div>
    </div>
  </div>
  <div class="row">
    <div class="card"><h2>Top 15 — pontos acumulados no período</h2><div id="ch-tg-pts" class="chart-tall"></div></div>
    <div class="card"><h2>Top 15 — mais participações</h2><div id="ch-tg-part" class="chart-tall"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Títulos por clube</h2><div id="ch-tg-titulos" class="chart"></div></div>
    <div class="card"><h2>Rebaixamentos por clube</h2><div id="ch-tg-rebs" class="chart"></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Regularidade — temporadas × pontos médios</h2><div id="ch-tg-scatter" class="chart-tall"></div></div>
  </div>
  <div class="row full">
    <div class="card">
      <h2>Tabela completa — clubes × temporadas</h2>
      <div class="tbl-wrap tall"><table id="tbl-times-geral"></table></div>
    </div>
  </div>
</div>

<!-- ========= MANDO ========= -->
<div class="tab-content" id="tab-mando">
  <div class="kpis" id="kpis-mando"></div>
  <div class="row">
    <div class="card"><h2>Pontos como mandante e visitante</h2><div id="ch-mando-pts" class="chart-tall"></div></div>
    <div class="card"><h2>Aproveitamento como mandante e visitante</h2><div id="ch-mando-aprov" class="chart-tall"></div></div>
  </div>
  <div class="row full"><div class="card"><h2>Detalhes por clube</h2><div class="tbl-wrap"><table id="tbl-mando"></table></div></div></div>
</div>

<!-- ========= ATAQUE & DEFESA ========= -->
<div class="tab-content" id="tab-ataque">
  <div class="row">
    <div class="card"><h2>Relação entre ataque e defesa</h2><div id="ch-disp-ad" class="chart-tall"></div></div>
    <div class="card"><h2>Médias de gols por jogo</h2><div id="ch-md-gols" class="chart-tall"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Jogos sem sofrer gol</h2><div id="ch-clean" class="chart"></div></div>
    <div class="card"><h2>Jogos sem marcar</h2><div id="ch-noscore" class="chart"></div></div>
  </div>
  <div class="row full"><div class="card"><h2>Sequências ofensivas e defensivas</h2><div id="ch-streaks" class="chart-tall"></div></div></div>
</div>

<!-- ========= FORMA ========= -->
<div class="tab-content" id="tab-forma">
  <div class="card"><h2>🔥 Últimos 5 jogos & sequência atual</h2><div class="tbl-wrap tall"><table id="tbl-forma"></table></div></div>
</div>

<!-- ========= JOGADORES ========= -->
<div class="tab-content" id="tab-jogadores">
  <div class="note">Limitação dos dados: não há minutos jogados, assistências ou faltas individuais. Disponível: gols com minuto/tipo e cartões com minuto/posição.</div>
  <div class="row">
    <div class="card"><h2>Artilheiros</h2><div class="tbl-wrap"><table id="tbl-art"></table></div></div>
    <div class="card"><h2>Jogadores mais advertidos</h2><div class="tbl-wrap"><table id="tbl-cart-jog"></table></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Gols por posição registrada</h2><div id="ch-gols-pos" class="chart"></div></div>
    <div class="card"><h2>Gols por intervalo de minuto</h2><div id="ch-gols-min" class="chart"></div></div>
  </div>
</div>

<!-- ========= PARTIDAS ========= -->
<div class="tab-content" id="tab-partidas">
  <div class="row full">
    <div class="card">
      <h2>📅 Lista de partidas filtradas <span id="qtd-partidas" style="color:var(--muted);font-size:12px;font-weight:400;margin-left:8px"></span></h2>
      <div class="tbl-wrap tall"><table id="tbl-partidas"></table></div>
    </div>
  </div>
</div>

<!-- ========= DISCIPLINA ========= -->
<div class="tab-content" id="tab-disciplina">
  <div class="kpis" id="kpis-disc"></div>
  <div class="row">
    <div class="card"><h2>Cartões por clube</h2><div id="ch-cart-clube" class="chart-tall"></div></div>
    <div class="card"><h2>Cartões por posição do jogador</h2><div id="ch-cart-pos" class="chart-tall"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Cartões por intervalo de minuto</h2><div id="ch-cart-min" class="chart"></div></div>
    <div class="card"><h2>Relação entre faltas e cartões</h2><div id="ch-faltas" class="chart"></div></div>
  </div>
</div>

<!-- ========= RANKINGS ========= -->
<div class="tab-content" id="tab-rankings">
  <div class="row three" id="rankings-grid"></div>
</div>

<!-- ========= CAMPEONATO ========= -->
<div class="tab-content" id="tab-campeonato">
  <div class="note">Análise da temporada selecionada a partir da classificação rodada a rodada.</div>
  <div class="kpis" id="kpis-camp"></div>

  <h3 style="margin:14px 0 8px;color:var(--accent2)">Corrida pelo título</h3>
  <div class="row">
    <div class="card"><h2>Rodadas na liderança</h2><div id="ch-rod-lider" class="chart"></div></div>
    <div class="card"><h2>Pontos do líder e do vice por rodada</h2><div id="ch-lider-vice" class="chart"></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Distância para o líder por rodada — top 4 final</h2><div id="ch-dist-lider" class="chart"></div></div>
  </div>

  <h3 style="margin:18px 0 8px;color:var(--danger)">Briga contra o rebaixamento</h3>
  <div class="row">
    <div class="card"><h2>Rodadas no Z4</h2><div id="ch-rod-z4" class="chart"></div></div>
    <div class="card"><h2>Pontuação de corte do 16º colocado</h2><div id="ch-corte-z4" class="chart"></div></div>
  </div>

  <h3 style="margin:18px 0 8px;color:var(--warn)">Equilíbrio do campeonato</h3>
  <div class="kpis" id="kpis-equil"></div>
  <div class="row">
    <div class="card"><h2>Diferença entre 1º e 2º por rodada</h2><div id="ch-dif-12" class="chart"></div></div>
    <div class="card"><h2>Distribuição de pontos finais</h2><div id="ch-dist-pts" class="chart"></div></div>
  </div>

  <h3 style="margin:18px 0 8px;color:var(--purple)">Análise por fases</h3>
  <div class="row">
    <div class="card"><h2>Campeão do 1º turno, 2º turno e geral</h2><div class="tbl-wrap"><table id="tbl-fases"></table></div></div>
    <div class="card"><h2>Maior crescimento e maior queda</h2><div class="tbl-wrap"><table id="tbl-mom"></table></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Pontos por fase</h2><div id="ch-fases" class="chart-tall"></div></div>
  </div>
</div>

<!-- ========= COMPARAR TEMPORADAS ========= -->
<div class="tab-content" id="tab-comparar">
  <div class="note">🆚 Compara duas temporadas lado-a-lado. Use os seletores abaixo (independem do filtro global).</div>
  <div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:18px">
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Temporada A</label><select id="cmp-a" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Temporada B</label><select id="cmp-b" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
  </div>
  <div class="kpis" id="kpis-cmp"></div>
  <div class="row">
    <div class="card"><h2>📊 Resumo lado-a-lado</h2><div class="tbl-wrap"><table id="tbl-cmp"></table></div></div>
    <div class="card"><h2>📈 Distribuição de pontos finais</h2><div id="ch-cmp-pts" class="chart"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>⚖️ Diferença 1º × 2º ao longo do campeonato</h2><div id="ch-cmp-suspense" class="chart"></div></div>
    <div class="card"><h2>⚽ Gols por rodada</h2><div id="ch-cmp-gols" class="chart"></div></div>
  </div>
</div>

<!-- ========= CAMPANHAS HISTÓRICAS ========= -->
<div class="tab-content" id="tab-campanhas">
  <div class="note">Rankings de campanhas marcantes usando todas as temporadas disponíveis no banco. Esta aba ignora o filtro global.</div>
  <div class="row three" id="grid-campanhas"></div>
  <div class="row full">
    <div class="card"><h2>Perfil dos campeões — média histórica</h2><div class="tbl-wrap"><table id="tbl-perfil-camp"></table></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Perfil dos rebaixados — média histórica</h2><div class="tbl-wrap"><table id="tbl-perfil-reb"></table></div></div>
  </div>
</div>

<!-- ========= COMPARAR CLUBES ========= -->
<div class="tab-content" id="tab-confronto">
  <div class="note">Compara dois clubes na janela de temporadas selecionada. Estes controles independem do filtro global.</div>
  <div class="card" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-bottom:18px">
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Clube A</label><select id="cf-a" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Clube B</label><select id="cf-b" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Janela de temporadas</label>
      <div style="display:flex;gap:6px"><select id="cf-min" style="flex:1;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select><select id="cf-max" style="flex:1;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    </div>
  </div>
  <div class="kpis" id="kpis-cf"></div>
  <div class="row">
    <div class="card"><h2>Resumo da janela</h2><div class="tbl-wrap"><table id="tbl-cf-resumo"></table></div></div>
    <div class="card"><h2>Posição final por temporada</h2><div id="ch-cf-pos" class="chart"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Pontos por temporada</h2><div id="ch-cf-pts" class="chart"></div></div>
    <div class="card"><h2>Saldo de gols por temporada</h2><div id="ch-cf-sg" class="chart"></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Confrontos diretos na janela</h2><div class="tbl-wrap" style="max-height:480px"><table id="tbl-cf-jogos"></table></div></div>
  </div>
</div>

<!-- ========= TÉCNICOS ========= -->
<div class="tab-content" id="tab-tecnicos">
  <div class="note">Análise baseada nos campos <code>tecnico_mandante</code> e <code>tecnico_visitante</code>. O aproveitamento considera jogos como mandante e visitante.</div>
  <div class="kpis" id="kpis-tec"></div>
  <div class="row">
    <div class="card"><h2>Técnicos campeões</h2><div class="tbl-wrap"><table id="tbl-tec-camp"></table></div></div>
    <div class="card"><h2>Técnicos com mais jogos</h2><div class="tbl-wrap"><table id="tbl-tec-jogos"></table></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Melhor aproveitamento</h2><div class="tbl-wrap"><table id="tbl-tec-aprov"></table></div></div>
    <div class="card"><h2>Mais trocas de técnico por temporada</h2><div class="tbl-wrap"><table id="tbl-tec-trocas"></table></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Impacto após troca de técnico</h2><div class="tbl-wrap"><table id="tbl-tec-impacto"></table></div></div>
  </div>
</div>

<!-- ========= GEOGRAFIA ========= -->
<div class="tab-content" id="tab-geografia">
  <div class="note">Análises por UF dos clubes em cada partida. Esta aba usa todas as temporadas disponíveis e ignora o filtro global.</div>
  <div class="kpis" id="kpis-geo"></div>
  <div class="row">
    <div class="card"><h2>Participações por UF</h2><div id="ch-geo-part" class="chart"></div></div>
    <div class="card"><h2>Títulos por UF</h2><div id="ch-geo-tit" class="chart"></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Rebaixamentos por UF</h2><div id="ch-geo-reb" class="chart"></div></div>
    <div class="card"><h2>Pontos médios por UF</h2><div id="ch-geo-pts" class="chart"></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Jogos entre clubes da mesma UF</h2><div class="tbl-wrap"><table id="tbl-geo-class"></table></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Mando por relação de UF</h2><div id="ch-geo-mando" class="chart"></div></div>
    <div class="card"><h2>Jogos por UF do mandante</h2><div id="ch-geo-jogos" class="chart"></div></div>
  </div>
</div>

<!-- ========= ÍNDICES HISTÓRICOS ========= -->
<div class="tab-content" id="tab-indices">
  <div class="note">Índices calculados sobre a classificação rodada a rodada. Esta aba usa todas as temporadas disponíveis e ignora o filtro global.</div>

  <h3 style="margin:14px 0 8px;color:var(--warn)">Dominância dos campeões</h3>
  <div class="card" style="margin-bottom:18px;padding:14px 18px;font-size:12px;color:var(--muted)">
    Combina vantagem sobre o vice, saldo de gols, percentual de rodadas na liderança, aproveitamento e bônus por melhor ataque ou melhor defesa. Quanto maior, mais dominante foi a campanha campeã.
  </div>
  <div class="row">
    <div class="card"><h2>Ranking de dominância dos campeões</h2><div class="tbl-wrap"><table id="tbl-idx-dom"></table></div></div>
    <div class="card"><h2>Comparação entre campeões</h2><div id="ch-idx-dom" class="chart"></div></div>
  </div>

  <h3 style="margin:18px 0 8px;color:var(--danger)">Sofrimento contra o rebaixamento</h3>
  <div class="card" style="margin-bottom:18px;padding:14px 18px;font-size:12px;color:var(--muted)">
    Considera clubes que terminaram entre 13º e 16º, combinando rodadas no Z4, menor distância para a linha de corte e proximidade final do 17º lugar. Quanto maior, mais apertada foi a permanência.
  </div>
  <div class="row full"><div class="card"><h2>Top 15 permanências mais apertadas</h2><div class="tbl-wrap"><table id="tbl-idx-sof"></table></div></div></div>

  <h3 style="margin:18px 0 8px;color:var(--accent2)">Regularidade rodada a rodada</h3>
  <div class="card" style="margin-bottom:18px;padding:14px 18px;font-size:12px;color:var(--muted)">
    Mede a estabilidade da posição ao longo da temporada, usando o desvio padrão da colocação rodada a rodada. Quanto maior, mais estável foi a campanha.
  </div>
  <div class="row full"><div class="card"><h2>Top 15 campanhas mais regulares</h2><div class="tbl-wrap"><table id="tbl-idx-reg"></table></div></div></div>

  <h3 style="margin:18px 0 8px;color:var(--accent)">Arrancadas e quedas no segundo turno</h3>
  <div class="card" style="margin-bottom:18px;padding:14px 18px;font-size:12px;color:var(--muted)">
    Compara a posição final com a posição no fim do primeiro turno. Arrancada indica ganho de posições; queda indica perda de posições.
  </div>
  <div class="row">
    <div class="card"><h2>Top 15 maiores arrancadas</h2><div class="tbl-wrap"><table id="tbl-idx-arr"></table></div></div>
    <div class="card"><h2>Top 15 maiores quedas</h2><div class="tbl-wrap"><table id="tbl-idx-queda"></table></div></div>
  </div>
</div>

<!-- ========= INSIGHTS HISTÓRICOS ========= -->
<div class="tab-content" id="tab-perguntas">
  <div class="note">Insights calculados com todas as temporadas disponíveis no banco. Esta aba ignora o filtro global.</div>
  <div id="grid-perguntas"></div>
</div>

<!-- ========= HISTÓRICO ========= -->
<div class="tab-content" id="tab-historico">
  <div class="note">Esta aba usa todas as temporadas disponíveis no banco e ignora o filtro global de temporada.</div>
  <div class="kpis" id="kpis-hist"></div>
  <div class="row">
    <div class="card"><h2>Campeões e pontuação do campeão</h2><div class="tbl-wrap"><table id="tbl-campeoes"></table></div></div>
    <div class="card"><h2>Rebaixados por temporada</h2><div class="tbl-wrap"><table id="tbl-rebaixados"></table></div></div>
  </div>
  <div class="row">
    <div class="card"><h2>Gols totais por temporada</h2><div id="ch-gols-temp" class="chart"></div></div>
    <div class="card"><h2>Artilheiros por temporada</h2><div class="tbl-wrap"><table id="tbl-artilheiros-hist"></table></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Pontos por clube no período</h2><div id="ch-hist-pts" class="chart-tall"></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Posição final por clube no período</h2><div class="tbl-wrap tall"><table id="tbl-hist-pos"></table></div></div>
  </div>
</div>

<!-- ========= CLASSIFICACAO FINAL HISTORICA ========= -->
<div class="tab-content" id="tab-historico-final">
  <div class="card hf-filter-card" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:18px">
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Clube</label>
      <select id="hf-clube" hidden></select>
      <div class="ms" id="hf-clube-ms" style="margin-top:4px">
        <button type="button" class="ms-toggle" id="hf-clube-toggle" aria-haspopup="listbox" aria-expanded="false">
          <span class="ms-label placeholder" id="hf-clube-label">Todos os clubes</span>
          <svg class="ms-caret" width="10" height="6" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="ms-panel" id="hf-clube-panel" hidden>
          <div class="ms-search-wrap">
            <svg class="ms-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input class="ms-search" id="hf-clube-search" type="text" placeholder="Buscar clube...">
          </div>
          <div class="ms-actions">
            <button type="button" class="ms-mini" id="hf-clube-all">Todos os clubes</button>
            <button type="button" class="ms-mini" id="hf-clube-clear">Limpar busca</button>
          </div>
          <div class="ms-list" id="hf-clube-list" role="listbox"></div>
        </div>
      </div>
    </div>
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Edicao</label><select id="hf-edicao" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    <div><label style="font-size:11px;color:var(--muted);text-transform:uppercase">Periodo</label>
      <div style="display:flex;gap:6px"><select id="hf-min" style="flex:1;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select><select id="hf-max" style="flex:1;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px"></select></div>
    </div>
  </div>
  <div class="kpis" id="kpis-hf"></div>
  <div class="row full">
    <div class="card">
      <h2>Ranking acumulado ano a ano</h2>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap">
        <button id="hf-race-play" class="btn">Play</button>
        <button id="hf-race-prev" class="btn" title="Campeonato anterior">‹</button>
        <div id="hf-race-year-label" style="font-weight:900;color:var(--accent);min-width:70px"></div>
        <button id="hf-race-next" class="btn" title="Próximo campeonato">›</button>
        <input id="hf-race-range" type="range" min="0" max="1" value="0" style="flex:1;min-width:220px;accent-color:var(--accent)">
      </div>
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:stretch">
        <div>
          <h2 style="font-size:15px;margin-bottom:6px">Campeões</h2>
          <div id="ch-hf-race-campeoes" style="height:640px"></div>
        </div>
        <div style="display:grid;grid-template-rows:1fr 1fr;gap:16px">
          <div>
            <h2 style="font-size:15px;margin-bottom:6px">Vice-campeões</h2>
            <div id="ch-hf-race-vices" style="height:312px"></div>
          </div>
          <div>
            <h2 style="font-size:15px;margin-bottom:6px">Terceiros colocados</h2>
            <div id="ch-hf-race-terceiros" style="height:312px"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row full">
    <div class="card">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:8px">
        <h2 style="margin:0">Ranking por posição final</h2>
        <select id="hf-rank-pos" style="padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px"></select>
      </div>
      <div id="ch-hf-rank-pos" class="chart-tall"></div>
    </div>
  </div>
  <div class="row full">
    <div class="card">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:8px">
        <h2 style="margin:0">Participações por clube</h2>
        <div style="display:flex;align-items:center;gap:10px;min-width:320px;flex:1;justify-content:flex-end">
          <span id="hf-part-window" style="font-size:12px;color:var(--muted);font-weight:700;min-width:90px;text-align:right"></span>
          <input id="hf-part-slider" type="range" min="0" max="0" value="0" style="width:min(420px,100%);accent-color:var(--accent)">
        </div>
      </div>
      <div id="ch-hf-part" class="chart-tall"></div>
    </div>
  </div>
  <div class="row full">
    <div class="card"><h2>Podios compilados por clube</h2><div class="tbl-wrap tall"><table id="tbl-hf-podios"></table></div></div>
  </div>
  <div class="row full">
    <div class="card"><h2>Tabela completa filtrada</h2><div class="tbl-wrap tall"><table id="tbl-hf"></table></div></div>
  </div>
</div>

</main>

<main id="copa-main" hidden>
  <nav class="copa-tabs" id="copa-tabs">
    <button data-copa-tab="geral" class="active">Visão Geral</button>
    <button data-copa-tab="clubes">Clubes</button>
    <button data-copa-tab="edicoes">Edições</button>
    <button data-copa-tab="finais">Finais</button>
  </nav>
  <div class="copa-filters">
    <div class="fld"><label>Ano</label><select id="copa-ano"></select></div>
    <div class="fld"><label>Clube</label><select id="copa-clube"></select></div>
    <button class="btn primary" id="copa-limpar">Limpar</button>
  </div>

  <section class="copa-section active" id="copa-sec-geral">
    <div class="kpis" id="kpis-copa"></div>
    <div class="row">
      <div class="card"><h2>Títulos por clube</h2><div id="ch-copa-titulos" class="chart-tall"></div></div>
      <div class="card"><h2>Finais por clube</h2><div id="ch-copa-finais" class="chart-tall"></div></div>
    </div>
    <div class="row full">
      <div class="card">
        <div style="display:flex;align-items:end;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:10px">
          <div style="min-width:220px;flex:1">
            <label style="font-size:11px;color:var(--muted);text-transform:uppercase">Metrica da corrida</label>
            <select id="copa-race-metric" style="width:100%;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px;margin-top:4px">
              <option value="titulos">Títulos acumulados</option>
              <option value="finais">Finais acumuladas</option>
              <option value="participacoes">Participações acumuladas</option>
            </select>
          </div>
          <div style="display:flex;align-items:center;gap:10px;flex:2;min-width:320px">
            <button id="copa-race-play" class="btn">Play</button>
            <button id="copa-race-prev" class="btn" title="Ano anterior">‹</button>
            <div id="copa-race-year-label" style="font-weight:900;color:var(--accent);min-width:78px;text-align:center"></div>
            <button id="copa-race-next" class="btn" title="Próximo ano">›</button>
            <input id="copa-race-range" type="range" min="0" max="1" value="0" style="flex:1;min-width:180px;accent-color:var(--accent)">
          </div>
        </div>
        <h2>Corrida histórica por clube</h2>
        <div id="ch-copa-race" class="chart-tall"></div>
      </div>
    </div>
    <div class="row">
      <div class="card"><h2>Linha histórica de campeões</h2><div id="ch-copa-timeline" class="chart"></div></div>
      <div class="card"><h2>Títulos por UF</h2><div id="ch-copa-uf" class="chart"></div></div>
    </div>
    <div class="row">
      <div class="card"><h2>Evolução da competição</h2><div id="ch-copa-evolucao" class="chart"></div></div>
      <div class="card"><h2>Participações mapeadas por clube</h2><div id="ch-copa-participacoes" class="chart"></div></div>
    </div>
  </section>

  <section class="copa-section" id="copa-sec-clubes">
    <div class="kpis" id="kpis-copa-clube"></div>
    <div class="row">
      <div class="card"><h2>Histórico do clube por ano</h2><div id="ch-copa-clube-hist" class="chart"></div></div>
      <div class="card"><h2>Finais disputadas</h2><div id="ch-copa-clube-finais" class="chart"></div></div>
    </div>
    <div class="row full">
      <div class="card"><h2>Histórico do clube</h2><div class="tbl-wrap tall"><table id="tbl-copa-clube"></table></div></div>
    </div>
  </section>

  <section class="copa-section" id="copa-sec-edicoes">
    <div class="kpis" id="kpis-copa-edicao"></div>
    <div class="row">
      <div class="card"><h2>Participantes da edição</h2><div id="ch-copa-edicao-part" class="chart-tall"></div></div>
      <div class="card"><h2>Placar agregado da final</h2><div id="ch-copa-edicao-final" class="chart"></div></div>
    </div>
    <div class="row full">
      <div class="card"><h2>Edições completas</h2><div class="tbl-wrap tall"><table id="tbl-copa-edicoes"></table></div></div>
    </div>
    <div class="row full">
      <div class="card"><h2>Participantes mapeados</h2><div class="tbl-wrap tall"><table id="tbl-copa-participantes"></table></div></div>
    </div>
  </section>

  <section class="copa-section" id="copa-sec-finais">
    <div class="row">
      <div class="card"><h2>Critérios de decisão</h2><div id="ch-copa-criterios" class="chart"></div></div>
      <div class="card"><h2>Gols nas finais</h2><div id="ch-copa-gols-finais" class="chart"></div></div>
    </div>
    <div class="row full">
      <div class="card"><h2>Histórico de finais</h2><div class="tbl-wrap tall"><table id="tbl-copa-finais"></table></div></div>
    </div>
    <div class="row full">
      <div class="card"><h2>Partidas das finais</h2><div class="tbl-wrap tall"><table id="tbl-copa-partidas"></table></div></div>
    </div>
  </section>
</main>

<script>
const DATA = __PAYLOAD__;
const fmtInt = new Intl.NumberFormat("pt-BR");
const temporadaIni = DATA.temporadas[0];
const temporadaFim = DATA.temporadas[DATA.temporadas.length - 1];
document.getElementById("hdr-sub").textContent =
  `${DATA.temporadas.length} temporadas (${temporadaIni}-${temporadaFim}) · ${fmtInt.format(DATA.matches.length)} jogos · banco SQLite local · análise rodada a rodada`;

const state = {
  competition: "serie_a",
  temporada: DATA.ano_default,
  clubesSel: [],
  rodMin: DATA.rodada_range[DATA.ano_default][0],
  rodMax: DATA.rodada_range[DATA.ano_default][1],
  resultado: "", sortCol: "P", sortDir: "desc",
  hfInit: false, hfClube: "", hfEdicao: "", hfMin: null, hfMax: null, hfRankPos: 1, hfPartOffset: 0, hfRaceYear: null, hfRaceIdx: 0, hfRacePlaying: false,
  tgPosClube: "", tgPosIdx: 0, tgPosPlaying: false,
  campRaceTemp: DATA.ano_default, campRaceIdx: 0, campRacePlaying: false,
  copaTab: "geral", copaAno: "", copaClube: "", copaRaceMetric: "titulos", copaRaceIdx: 0, copaRacePlaying: false,
  group: "visao-geral", tab: "resumo",   // default: painel principal
};
let hfRaceTimer = null;
let hfRaceAnimFrame = null;
let tgPosTimer = null;
let campRaceTimer = null;
let campRaceRenderedTemp = null;
let campRaceAnimFrame = null;
let campRacePrevFrame = null;
let copaRaceTimer = null;
let copaRaceAnimFrame = null;
let copaRacePrevFrame = null;
let copaRaceRenderedMetric = null;

const CLUB_COLORS = {
  "America-MG":"#007a3d", "Athletico-PR":"#c8102e", "Atletico-GO":"#d71920", "Atletico-MG":"#f2f2f2",
  "Avai":"#0057b8", "Bahia":"#005bac", "Botafogo-RJ":"#f2f2f2", "Bragantino":"#c8102e",
  "Ceara":"#f2f2f2", "Corinthians":"#f2f2f2", "Coritiba":"#006633", "Cruzeiro":"#0057b8",
  "Flamengo":"#e31b23", "Fluminense":"#7a0026", "Fortaleza":"#003f8f", "Goias":"#00843d",
  "Gremio":"#00a5e0", "Guarani":"#007a3d", "Internacional":"#d50032", "Juventude":"#009639",
  "Palmeiras":"#006437", "Ponte Preta":"#f2f2f2", "Santos":"#f2f2f2", "Sao Paulo":"#d71920",
  "Sport":"#d71920", "Vasco":"#f2f2f2", "Vitoria":"#d71920"
};

// ---------- tema ----------
const root = document.documentElement;
const savedTheme = localStorage.getItem("theme") || "dark";
root.setAttribute("data-theme", savedTheme);
document.getElementById("btn-theme").textContent = savedTheme === "dark" ? "☀️ Claro" : "🌙 Escuro";
document.getElementById("btn-theme").addEventListener("click", () => {
  const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
  root.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
  document.getElementById("btn-theme").textContent = next === "dark" ? "☀️ Claro" : "🌙 Escuro";
  render();
});

const GLOBAL_FILTER_TABS = new Set([
  "resumo",
  "classificacao",
  "campeonato",
  "evolucao",
  "forma",
  "partidas",
  "rankings",
  "mando",
  "ataque",
  "disciplina",
  "jogadores",
]);

function updateGlobalFiltersVisibility() {
  const show = state.competition === "serie_a" && GLOBAL_FILTER_TABS.has(state.tab);
  document.getElementById("global-filters")?.classList.toggle("hidden", !show);
}

function activateCompetition(comp) {
  state.competition = comp;
  const isCopa = comp === "copa_brasil";
  document.querySelectorAll("#competition-switch button").forEach(b => b.classList.toggle("active", b.dataset.competition === comp));
  document.getElementById("main-title").textContent = isCopa ? "Copa do Brasil — Clube Analítico" : "Brasileirão Série A — Clube Analítico";
  document.getElementById("tab-groups").hidden = isCopa;
  document.getElementById("tabs").hidden = isCopa;
  document.getElementById("serie-a-main").hidden = isCopa;
  document.getElementById("copa-main").hidden = !isCopa;
  updateGlobalFiltersVisibility();
  const strip = document.getElementById("match-strip");
  if (isCopa) {
    const anos = DATA.copa_brasil.finais.map(f => f.ano);
    document.getElementById("hdr-sub").textContent = `${DATA.copa_brasil.finais.length} edições (${Math.min(...anos)}-${Math.max(...anos)}) · ${DATA.copa_brasil.partidas_finais.length} jogos de final · banco SQLite local · análise histórica da Copa`;
    strip.innerHTML = `<span class="score-chip">Mata-mata</span><span class="score-chip">Finais históricas</span><span class="score-chip">Campeões e vices</span><span class="score-chip">Views próprias</span>`;
    stopHFRace(); stopTGPosRace(); stopCampRace();
    renderCopaBrasil();
  } else {
    document.getElementById("hdr-sub").textContent = `${DATA.temporadas.length} temporadas (${temporadaIni}-${temporadaFim}) · ${fmtInt.format(DATA.matches.length)} jogos · banco SQLite local · análise rodada a rodada`;
    strip.innerHTML = `<span class="score-chip">Série A</span><span class="score-chip">Rodada a rodada</span><span class="score-chip">Scout completo</span><span class="score-chip">Histórico de clubes</span>`;
    stopCopaRace();
    render();
  }
}
document.getElementById("competition-switch").addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  activateCompetition(e.target.dataset.competition);
});

// ---------- nav (grupos + abas) ----------
function activateTab(tab) {
  state.tab = tab;
  if (tab !== "historico-final") stopHFRace();
  if (tab !== "times-geral") stopTGPosRace();
  if (tab !== "resumo") stopCampRace();
  updateGlobalFiltersVisibility();
  document.querySelectorAll("nav.tabs button").forEach(b => b.classList.toggle("active", b.dataset.tab === tab));
  document.querySelectorAll(".tab-content").forEach(d => d.classList.toggle("active", d.id === "tab-" + tab));
  render();
}
function activateGroup(group) {
  state.group = group;
  document.querySelectorAll("nav.tab-groups button").forEach(b => b.classList.toggle("active", b.dataset.group === group));
  // mostra só as abas do grupo, esconde resto via class .tab-hidden
  const tabsBtns = document.querySelectorAll("nav.tabs button[data-group]");
  let primeiraAba = null;
  tabsBtns.forEach(b => {
    const visivel = b.dataset.group === group;
    b.classList.toggle("tab-hidden", !visivel);
    if (visivel && !primeiraAba) primeiraAba = b.dataset.tab;
  });
  // se a aba ativa não pertence ao novo grupo, ativa a primeira do grupo
  const ativaPertence = [...tabsBtns].some(b => b.dataset.group === group && b.dataset.tab === state.tab);
  if (!ativaPertence && primeiraAba) activateTab(primeiraAba);
  else activateTab(state.tab);
}
document.getElementById("tab-groups").addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  activateGroup(e.target.dataset.group);
});
document.getElementById("tabs").addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  activateTab(e.target.dataset.tab);
});
// inicialização: aplica o grupo default (mostra só suas abas)
setTimeout(() => activateGroup(state.group), 0);

// ---------- filtros ----------
const selTemp = document.getElementById("f-temporada");
DATA.temporadas.forEach(t => {
  const o = document.createElement("option"); o.value = t; o.textContent = t;
  if (t === DATA.ano_default) o.selected = true;
  selTemp.appendChild(o);
});
const rmi = document.getElementById("f-rmin");
const rma = document.getElementById("f-rmax");
const updLab = () => {
  document.getElementById("lab-rmin").textContent = rmi.value;
  document.getElementById("lab-rmax").textContent = rma.value;
};
rmi.oninput = updLab; rma.oninput = updLab;

// =================== CUSTOM MULTI-SELECT (clubes) ===================
const ms = {
  clubes: [],          // todos os clubes da temporada atual
  selecionados: new Set(),
  toggle: document.getElementById("ms-toggle"),
  panel: document.getElementById("ms-panel"),
  list: document.getElementById("ms-list"),
  search: document.getElementById("ms-search"),
  label: document.getElementById("ms-label"),
  countBadge: document.getElementById("ms-count"),
};

function _normalize(s) {
  return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
}

function msRenderList(filtro = "") {
  const q = _normalize(filtro);
  if (!ms.clubes.length) {
    ms.list.innerHTML = '<div class="ms-empty">Nenhum clube nesta temporada</div>';
    return;
  }
  const items = ms.clubes.filter(c => !q || _normalize(c).includes(q));
  if (!items.length) {
    ms.list.innerHTML = '<div class="ms-empty">Nada encontrado para "' + filtro + '"</div>';
    return;
  }
  ms.list.innerHTML = items.map(c => {
    const sel = ms.selecionados.has(c) ? " selected" : "";
    return `<div class="ms-item${sel}" data-clube="${c}" role="option" aria-selected="${ms.selecionados.has(c)}">
      <span class="ms-cb"><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 4.5" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      <span>${c}</span>
    </div>`;
  }).join("");
  // bind clicks
  ms.list.querySelectorAll(".ms-item").forEach(el => {
    el.onclick = () => {
      const c = el.dataset.clube;
      if (ms.selecionados.has(c)) ms.selecionados.delete(c);
      else ms.selecionados.add(c);
      msUpdateLabel();
      msRenderList(ms.search.value);
    };
  });
}

function msUpdateLabel() {
  const n = ms.selecionados.size;
  if (n === 0) {
    ms.label.textContent = "Todos os clubes";
    ms.label.classList.add("placeholder");
    ms.countBadge.style.display = "none";
  } else if (n === 1) {
    ms.label.textContent = [...ms.selecionados][0];
    ms.label.classList.remove("placeholder");
    ms.countBadge.style.display = "none";
  } else {
    const arr = [...ms.selecionados];
    ms.label.textContent = arr[0] + " · +" + (n - 1);
    ms.label.classList.remove("placeholder");
    ms.countBadge.textContent = n;
    ms.countBadge.style.display = "";
  }
}

function msOpen() {
  ms.panel.hidden = false;
  ms.toggle.setAttribute("aria-expanded", "true");
  ms.search.value = "";
  msRenderList();
  setTimeout(() => ms.search.focus(), 30);
}
function msClose() {
  ms.panel.hidden = true;
  ms.toggle.setAttribute("aria-expanded", "false");
}

ms.toggle.onclick = (e) => {
  e.stopPropagation();
  if (ms.panel.hidden) msOpen(); else msClose();
};
document.addEventListener("click", (e) => {
  if (!ms.panel.hidden && !document.getElementById("ms-clubes").contains(e.target)) msClose();
});
ms.search.oninput = () => msRenderList(ms.search.value);
ms.search.onkeydown = (e) => { if (e.key === "Escape") msClose(); };
document.getElementById("ms-all").onclick = () => {
  ms.clubes.forEach(c => ms.selecionados.add(c));
  msUpdateLabel(); msRenderList(ms.search.value);
};
document.getElementById("ms-none").onclick = () => {
  ms.selecionados.clear();
  msUpdateLabel(); msRenderList(ms.search.value);
};

function popularClubesERodada(temp) {
  // multi-select de clubes
  ms.clubes = (DATA.clubes_por_temporada[temp] || []).slice().sort((a,b) => a.localeCompare(b));
  ms.selecionados.clear();
  msUpdateLabel();
  if (!ms.panel.hidden) msRenderList();
  // rodadas
  const [a,b] = DATA.rodada_range[temp];
  rmi.min = a; rmi.max = b; rmi.value = a;
  rma.min = a; rma.max = b; rma.value = b;
  state.rodMin = a; state.rodMax = b;
  state.clubesSel = [];
  updLab();
}
popularClubesERodada(state.temporada);

selTemp.onchange = () => {
  state.temporada = +selTemp.value;
  popularClubesERodada(state.temporada);
  render();
};

document.getElementById("btn-apply").onclick = () => {
  state.clubesSel = [...ms.selecionados];
  state.rodMin = +rmi.value; state.rodMax = +rma.value;
  if (state.rodMin > state.rodMax) [state.rodMin, state.rodMax] = [state.rodMax, state.rodMin];
  state.resultado = document.getElementById("f-result").value;
  msClose();
  render();
};
document.getElementById("btn-reset").onclick = () => {
  if (state.competition === "copa_brasil") {
    renderCopaBrasil();
    return;
  }
  popularClubesERodada(state.temporada);
  document.getElementById("f-result").value = "";
  state.resultado = "";
  msClose();
  render();
};

// ---------- helpers ----------
function getResult(m) { return m.gm > m.gv ? "V_M" : (m.gv > m.gm ? "V_V" : "E"); }

function getFiltered() {
  const ms = DATA.matches.filter(m => {
    if (m.temporada !== state.temporada) return false;
    if (m.rodada < state.rodMin || m.rodada > state.rodMax) return false;
    if (state.resultado && getResult(m) !== state.resultado) return false;
    if (state.clubesSel.length && !state.clubesSel.includes(m.mandante) && !state.clubesSel.includes(m.visitante)) return false;
    return true;
  });
  const idsF = new Set(ms.map(m => m.id));
  return {
    ms,
    gs: DATA.goals.filter(g => g.temporada === state.temporada && idsF.has(g.partida_id)),
    cs: DATA.cards.filter(c => c.temporada === state.temporada && idsF.has(c.partida_id)),
    sts: DATA.stats.filter(s => s.temporada === state.temporada && idsF.has(s.partida_id)),
  };
}

function calcTabela(ms) {
  const t = {};
  const ensure = c => { if (!t[c]) t[c] = {clube:c,J:0,V:0,E:0,D:0,GP:0,GC:0,V_M:0,V_V:0,P_M:0,P_V:0,J_M:0,J_V:0,GP_M:0,GP_V:0,GC_M:0,GC_V:0}; return t[c]; };
  ms.forEach(m => {
    const h = ensure(m.mandante), a = ensure(m.visitante);
    h.J++; a.J++; h.GP+=m.gm; h.GC+=m.gv; a.GP+=m.gv; a.GC+=m.gm;
    h.J_M++; a.J_V++; h.GP_M+=m.gm; h.GC_M+=m.gv; a.GP_V+=m.gv; a.GC_V+=m.gm;
    if (m.gm > m.gv) { h.V++; a.D++; h.V_M++; h.P_M+=3; }
    else if (m.gm < m.gv) { a.V++; h.D++; a.V_V++; a.P_V+=3; }
    else { h.E++; a.E++; h.P_M+=1; a.P_V+=1; }
  });
  return Object.values(t).map(x => ({
    ...x, SG:x.GP-x.GC, P:x.V*3+x.E,
    APR: x.J?Math.round((x.V*3+x.E)/(x.J*3)*1000)/10:0,
    APR_M: x.J_M?Math.round(x.P_M/(x.J_M*3)*1000)/10:0,
    APR_V: x.J_V?Math.round(x.P_V/(x.J_V*3)*1000)/10:0,
    SG_M: x.GP_M-x.GC_M, SG_V: x.GP_V-x.GC_V,
  })).sort((a,b)=> b.P-a.P || b.V-a.V || b.SG-a.SG || b.GP-a.GP);
}

// Histórico rodada-a-rodada para evolução
function calcEvolucao(ms) {
  const ord = [...ms].sort((a,b)=> a.rodada-b.rodada || a.data_iso.localeCompare(b.data_iso));
  const rounds = [...new Set(ord.map(m=>m.rodada))].sort((a,b)=>a-b);
  const teams = [...new Set(ord.flatMap(m=>[m.mandante,m.visitante]))].sort();
  const cum = {};
  teams.forEach(t => cum[t] = {pts:[0], j:[0], gp:[0], gc:[0], curPts:0, curJ:0, curGP:0, curGC:0});
  // Para cada rodada, atualiza acumulados
  rounds.forEach(r => {
    const games = ord.filter(m => m.rodada === r);
    games.forEach(m => {
      const h = cum[m.mandante], a = cum[m.visitante];
      h.curJ++; a.curJ++; h.curGP+=m.gm; a.curGP+=m.gv; h.curGC+=m.gv; a.curGC+=m.gm;
      if (m.gm > m.gv) h.curPts += 3;
      else if (m.gm < m.gv) a.curPts += 3;
      else { h.curPts += 1; a.curPts += 1; }
    });
    teams.forEach(t => {
      cum[t].pts.push(cum[t].curPts);
      cum[t].j.push(cum[t].curJ);
      cum[t].gp.push(cum[t].curGP);
      cum[t].gc.push(cum[t].curGC);
    });
  });
  // Posição por rodada
  const positions = {};
  teams.forEach(t => positions[t] = []);
  for (let i = 1; i <= rounds.length; i++) {
    const snap = teams.map(t => ({clube:t, p:cum[t].pts[i], sg:cum[t].gp[i]-cum[t].gc[i], gp:cum[t].gp[i]}));
    snap.sort((a,b)=> b.p-a.p || b.sg-a.sg || b.gp-a.gp);
    snap.forEach((row, idx) => { positions[row.clube].push(idx+1); });
  }
  return {rounds, teams, cum, positions};
}

// Últimos 5 jogos por clube
function calcUltimos(ms, n=5) {
  const ord = [...ms].sort((a,b)=> a.rodada-b.rodada || a.data_iso.localeCompare(b.data_iso));
  const teams = [...new Set(ord.flatMap(m=>[m.mandante,m.visitante]))].sort();
  const out = {};
  teams.forEach(t => out[t] = {ult:[], pts:0, gp:0, gc:0, streak:"", cur:null, curN:0});
  teams.forEach(t => {
    const games = ord.filter(m => m.mandante === t || m.visitante === t);
    games.forEach(m => {
      const home = m.mandante === t;
      const myG = home ? m.gm : m.gv;
      const oppG = home ? m.gv : m.gm;
      let res;
      if (myG > oppG) res = "V";
      else if (myG < oppG) res = "D";
      else res = "E";
      out[t].ult.push({res, home, gm:myG, gc:oppG, rodada:m.rodada, opp: home ? m.visitante : m.mandante});
    });
    const last = out[t].ult.slice(-n);
    out[t].last = last;
    out[t].lastPts = last.reduce((s,x)=> s + (x.res==="V"?3 : x.res==="E"?1 : 0), 0);
    out[t].lastGP = last.reduce((s,x)=>s+x.gm,0);
    out[t].lastGC = last.reduce((s,x)=>s+x.gc,0);
    // sequência atual: percorrer de trás pra frente
    if (out[t].ult.length) {
      const lastRes = out[t].ult[out[t].ult.length-1].res;
      let n2=0;
      for (let i=out[t].ult.length-1; i>=0; i--) {
        if (out[t].ult[i].res === lastRes) n2++;
        else break;
      }
      out[t].cur = lastRes; out[t].curN = n2;
      // invencibilidade: V ou E
      let invN=0;
      for (let i=out[t].ult.length-1; i>=0; i--) {
        if (out[t].ult[i].res !== "D") invN++; else break;
      }
      out[t].invN = invN;
    }
    // sequências históricas
    let bestUnbeat=0,curUnbeat=0,bestLose=0,curLose=0,bestScore=0,curScore=0,bestNoConc=0,curNoConc=0;
    out[t].ult.forEach(x => {
      curUnbeat = x.res !== "D" ? curUnbeat+1 : 0;
      curLose = x.res === "D" ? curLose+1 : 0;
      curScore = x.gm > 0 ? curScore+1 : 0;
      curNoConc = x.gc === 0 ? curNoConc+1 : 0;
      bestUnbeat = Math.max(bestUnbeat, curUnbeat);
      bestLose = Math.max(bestLose, curLose);
      bestScore = Math.max(bestScore, curScore);
      bestNoConc = Math.max(bestNoConc, curNoConc);
    });
    out[t].bestUnbeat=bestUnbeat; out[t].bestLose=bestLose;
    out[t].bestScore=bestScore; out[t].bestNoConc=bestNoConc;
    out[t].cleanSheets = out[t].ult.filter(x=>x.gc===0).length;
    out[t].noScore = out[t].ult.filter(x=>x.gm===0).length;
  });
  return out;
}

// ---------- tema cores ----------
function getThemeColors() {
  const dark = root.getAttribute("data-theme") === "dark";
  return {
    bg: dark?"#0e1b14":"#ffffff", text: dark?"#f1f7f1":"#15241c",
    grid: dark?"#2e4d39":"#cfdcc9",
    accent: dark?"#1ecb74":"#087c43", accent2: dark?"#f7c948":"#c47d08", accent3: dark?"#38bdf8":"#2563eb",
    champ: dark?"#fbbf24":"#d97706",
    warn: dark?"#f7c948":"#c47d08", danger: dark?"#ef4444":"#dc2626",
    purple: dark?"#a78bfa":"#7c3aed", muted: dark?"#9bb6a7":"#5b7568",
  };
}
function plotLayout(extra={}) {
  const c = getThemeColors();
  return Object.assign({
    paper_bgcolor: c.bg, plot_bgcolor: c.bg,
    font: {color: c.text, family: "-apple-system,Segoe UI,Roboto,sans-serif", size: 11},
    margin: {l:60,r:20,t:20,b:50},
    xaxis: {gridcolor: c.grid, zerolinecolor: c.grid},
    yaxis: {gridcolor: c.grid, zerolinecolor: c.grid},
    hoverlabel: {bgcolor: c.bg, bordercolor: c.grid, font: {color: c.text}},
  }, extra);
}
const PCFG = {displayModeBar: false, responsive: true};

function getCopaRaceYears() {
  return [...new Set((DATA.copa_brasil.finais || []).map(f => f.ano))].sort((a,b)=>a-b);
}
function stopCopaRace() {
  if (copaRaceTimer) clearTimeout(copaRaceTimer);
  if (copaRaceAnimFrame) cancelAnimationFrame(copaRaceAnimFrame);
  copaRaceTimer = null; copaRaceAnimFrame = null; state.copaRacePlaying = false;
  const btn = document.getElementById("copa-race-play");
  if (btn) btn.textContent = "Play";
}
function buildCopaRaceRows(year) {
  const metric = state.copaRaceMetric;
  const acc = {};
  const ensure = cl => { if (!acc[cl]) acc[cl] = {clube:cl,titulos:0,finais:0,participacoes:0}; return acc[cl]; };
  (DATA.copa_brasil.finais || []).filter(f => f.ano <= year).forEach(f => {
    ensure(f.campeao).titulos++;
    ensure(f.campeao).finais++;
    ensure(f.vice).finais++;
  });
  const seen = new Set();
  (DATA.copa_brasil.participantes || []).filter(p => p.ano <= year).forEach(p => {
    const k = `${p.ano}|${p.clube}`;
    if (seen.has(k)) return;
    seen.add(k);
    ensure(p.clube).participacoes++;
  });
  return Object.values(acc).filter(r => r[metric] > 0)
    .sort((a,b)=>b[metric]-a[metric] || b.titulos-a.titulos || b.finais-a.finais || a.clube.localeCompare(b.clube))
    .slice(0,15).map((r,i)=>({...r,valor:r[metric],pos:i+1,y:15-i}));
}
function renderCopaRace() {
  const c = getThemeColors();
  const years = getCopaRaceYears();
  if (!years.length || !document.getElementById("ch-copa-race")) return;
  state.copaRaceIdx = Math.max(0, Math.min(years.length - 1, state.copaRaceIdx || 0));
  const year = years[state.copaRaceIdx];
  const labels = {titulos:"Títulos acumulados", finais:"Finais acumuladas", participacoes:"Participações acumuladas"};
  const sel = document.getElementById("copa-race-metric");
  if (sel) sel.value = state.copaRaceMetric;
  const range = document.getElementById("copa-race-range");
  if (range) { range.min = 0; range.max = years.length - 1; range.step = 1; range.value = state.copaRaceIdx; }
  const label = document.getElementById("copa-race-year-label");
  if (label) label.textContent = String(year);
  const rows = buildCopaRaceRows(year);
  const clubs = rows.map(r => r.clube);
  const targetFrame = Object.fromEntries(rows.map(r => [r.clube, {valor:r.valor,y:r.y,pos:r.pos}]));
  const previousFrame = copaRacePrevFrame && copaRaceRenderedMetric === state.copaRaceMetric ? copaRacePrevFrame : targetFrame;
  const maxVal = Math.max(1, ...years.flatMap(y => buildCopaRaceRows(y).map(r => r.valor)));
  const traces = frame => rows.map(r => {
    const f = frame[r.clube] || targetFrame[r.clube];
    return {type:"bar",orientation:"h",name:r.clube,showlegend:false,x:[f.valor],y:[f.y],width:[0.72],
      marker:{color:clubColor(r.clube),line:{color:c.text,width:.7}},
      text:[`${r.pos}º · ${r.clube} · ${Math.round(f.valor)}`],textposition:"outside",cliponaxis:false,
      customdata:[[r.pos,r.clube]],hovertemplate:"%{customdata[0]}º %{customdata[1]}<br>%{x:.0f}<extra></extra>"};
  });
  const layout = plotLayout({margin:{l:70,r:170,t:20,b:45},bargap:.18,
    xaxis:{title:labels[state.copaRaceMetric],gridcolor:c.grid,range:[0,maxVal + Math.max(2, Math.ceil(maxVal*.12))],tickformat:".0f",fixedrange:true},
    yaxis:{title:"Ranking no ano",gridcolor:c.grid,range:[0,16],tickmode:"array",tickvals:Array.from({length:15},(_,i)=>i+1),ticktext:Array.from({length:15},(_,i)=>`${16-i}º`)},
    showlegend:false,annotations:[{text:String(year),xref:"paper",yref:"paper",x:.98,y:.1,showarrow:false,font:{size:42,color:c.muted}}]});
  const renderFrame = frame => Plotly.react("ch-copa-race", traces(frame), layout, PCFG);
  const graph = document.getElementById("ch-copa-race");
  if (graph && graph.data && graph.data.length && copaRaceRenderedMetric === state.copaRaceMetric) {
    if (copaRaceAnimFrame) cancelAnimationFrame(copaRaceAnimFrame);
    const start = performance.now(), duration = 1200;
    const ease = t => t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t+2,3)/2;
    const tick = now => {
      const raw = Math.min(1, (now - start) / duration), k = ease(raw);
      const frame = Object.fromEntries(clubs.map(cl => {
        const a = previousFrame[cl] || {valor:0,y:0,pos:99};
        const b = targetFrame[cl] || {valor:0,y:0,pos:99};
        return [cl, {valor:a.valor+(b.valor-a.valor)*k, y:a.y+(b.y-a.y)*k, pos:b.pos}];
      }));
      renderFrame(frame);
      if (raw < 1) copaRaceAnimFrame = requestAnimationFrame(tick);
      else { copaRaceAnimFrame = null; copaRacePrevFrame = targetFrame; }
    };
    copaRaceAnimFrame = requestAnimationFrame(tick);
  } else {
    renderFrame(targetFrame);
    copaRaceRenderedMetric = state.copaRaceMetric;
    copaRacePrevFrame = targetFrame;
  }
}
function stepCopaRace(delta) {
  const years = getCopaRaceYears();
  if (!years.length) return;
  state.copaRaceIdx = Math.max(0, Math.min(years.length - 1, state.copaRaceIdx + delta));
  renderCopaRace();
}
function scheduleCopaRace() {
  if (!state.copaRacePlaying) return;
  const years = getCopaRaceYears();
  if (!years.length || state.copaRaceIdx >= years.length - 1) { stopCopaRace(); return; }
  copaRaceTimer = setTimeout(() => {
    state.copaRaceIdx++;
    renderCopaRace();
    scheduleCopaRace();
  }, 1350);
}
function toggleCopaRace() {
  if (state.copaRacePlaying) { stopCopaRace(); return; }
  const years = getCopaRaceYears();
  if (!years.length) return;
  if (state.copaRaceIdx >= years.length - 1) state.copaRaceIdx = 0;
  state.copaRacePlaying = true;
  const btn = document.getElementById("copa-race-play");
  if (btn) btn.textContent = "Pause";
  renderCopaRace();
  scheduleCopaRace();
}

function setupCopaControls() {
  if (setupCopaControls.done) return;
  setupCopaControls.done = true;
  const anos = [...new Set([...(DATA.copa_brasil.edicoes || []).map(e=>e.ano), ...(DATA.copa_brasil.finais || []).map(f=>f.ano)])].sort((a,b)=>b-a);
  const clubes = [...new Set([
    ...(DATA.copa_brasil.participantes || []).map(p=>p.clube),
    ...(DATA.copa_brasil.finais || []).flatMap(f=>[f.campeao,f.vice])
  ].filter(Boolean))].sort((a,b)=>a.localeCompare(b));
  document.getElementById("copa-ano").innerHTML = `<option value="">Todos os anos</option>` + anos.map(a=>`<option value="${a}">${a}</option>`).join("");
  document.getElementById("copa-clube").innerHTML = `<option value="">Todos os clubes</option>` + clubes.map(c=>`<option value="${c}">${c}</option>`).join("");
  document.getElementById("copa-tabs").addEventListener("click", e => {
    if (e.target.tagName !== "BUTTON") return;
    state.copaTab = e.target.dataset.copaTab;
    renderCopaBrasil();
  });
  document.getElementById("copa-ano").addEventListener("change", e => {
    state.copaAno = e.target.value ? +e.target.value : "";
    if (state.copaAno) state.copaTab = "edicoes";
    renderCopaBrasil();
  });
  document.getElementById("copa-clube").addEventListener("change", e => {
    state.copaClube = e.target.value;
    if (state.copaClube) state.copaTab = "clubes";
    renderCopaBrasil();
  });
  document.getElementById("copa-limpar").addEventListener("click", () => {
    state.copaAno = ""; state.copaClube = ""; state.copaTab = "geral";
    document.getElementById("copa-ano").value = "";
    document.getElementById("copa-clube").value = "";
    renderCopaBrasil();
  });
  document.getElementById("copa-race-metric").addEventListener("change", e => {
    stopCopaRace();
    state.copaRaceMetric = e.target.value;
    state.copaRaceIdx = 0;
    copaRacePrevFrame = null;
    copaRaceRenderedMetric = null;
    renderCopaRace();
  });
  document.getElementById("copa-race-play").onclick = toggleCopaRace;
  document.getElementById("copa-race-prev").onclick = () => { stopCopaRace(); stepCopaRace(-1); };
  document.getElementById("copa-race-next").onclick = () => { stopCopaRace(); stepCopaRace(1); };
  document.getElementById("copa-race-range").oninput = e => {
    stopCopaRace();
    state.copaRaceIdx = +e.target.value;
    renderCopaRace();
  };
}

function copaCriterioLabel(value) {
  return {
    penaltis: "pênaltis",
    gols_fora: "gols fora",
    saldo_gols: "saldo de gols",
    pontos: "pontos",
    outro: "outro",
  }[value] || value || "-";
}

function renderCopaBrasil() {
  setupCopaControls();
  const c = getThemeColors();
  document.querySelectorAll("#copa-tabs button").forEach(b => b.classList.toggle("active", b.dataset.copaTab === state.copaTab));
  document.querySelectorAll(".copa-section").forEach(s => s.classList.toggle("active", s.id === "copa-sec-" + state.copaTab));
  document.getElementById("copa-ano").value = state.copaAno || "";
  document.getElementById("copa-clube").value = state.copaClube || "";

  const allFinais = DATA.copa_brasil.finais || [];
  const allDesempenho = DATA.copa_brasil.desempenho || [];
  const allPartidas = DATA.copa_brasil.partidas_finais || [];
  const allEdicoes = DATA.copa_brasil.edicoes || [];
  const allParticipantes = DATA.copa_brasil.participantes || [];
  const ano = state.copaAno;
  const clube = state.copaClube;
  const finais = allFinais.filter(f => (!ano || f.ano === ano) && (!clube || f.campeao === clube || f.vice === clube));
  const partidas = allPartidas.filter(p => (!ano || p.ano === ano) && (!clube || p.mandante === clube || p.visitante === clube));
  const edicoes = allEdicoes.filter(e => !ano || e.ano === ano);
  const participantes = allParticipantes.filter(p => (!ano || p.ano === ano) && (!clube || p.clube === clube));
  const desempenho = allDesempenho.filter(d => !clube || d.clube === clube);

  const campeoesDistintos = new Set(allFinais.map(f => f.campeao)).size;
  const clubesFinalistas = new Set(allFinais.flatMap(f => [f.campeao, f.vice])).size;
  const participantesDistintos = new Set(allParticipantes.map(p => p.clube)).size;
  const maiorCampeao = [...allDesempenho].sort((a,b)=>b.titulos-a.titulos || b.vices-a.vices || a.clube.localeCompare(b.clube))[0];
  const maiorVice = [...allDesempenho].sort((a,b)=>b.vices-a.vices || b.titulos-a.titulos || a.clube.localeCompare(b.clube))[0];
  const penais = allFinais.filter(f => f.criterio === "penaltis").length;
  document.getElementById("kpis-copa").innerHTML = `
    <div class="kpi"><div class="v">${allFinais.length}</div><div class="l">Edições</div></div>
    <div class="kpi"><div class="v">${participantesDistintos}</div><div class="l">Participantes distintos</div></div>
    <div class="kpi"><div class="v">${clubesFinalistas}</div><div class="l">Finalistas distintos</div></div>
    <div class="kpi"><div class="v">${campeoesDistintos}</div><div class="l">Campeões distintos</div></div>
    <div class="kpi"><div class="v small">${maiorCampeao?.clube || "-"}</div><div class="l">Maior campeão (${maiorCampeao?.titulos || 0})</div></div>
    <div class="kpi"><div class="v small">${maiorVice?.clube || "-"}</div><div class="l">Mais vices (${maiorVice?.vices || 0})</div></div>
    <div class="kpi"><div class="v">${penais}</div><div class="l">Finais nos pênaltis</div></div>`;
  renderCopaRace();

  const tit = [...allDesempenho].sort((a,b)=>b.titulos-a.titulos || b.vices-a.vices || a.clube.localeCompare(b.clube)).filter(r=>r.titulos>0);
  Plotly.react("ch-copa-titulos", [{type:"bar",orientation:"h",y:tit.map(r=>r.clube).reverse(),x:tit.map(r=>r.titulos).reverse(),marker:{color:tit.map(r=>clubColor(r.clube)).reverse(),line:{color:c.text,width:.7}},text:tit.map(r=>r.titulos).reverse(),textposition:"outside",hovertemplate:"%{y}<br>%{x} título(s)<extra></extra>"}], plotLayout({margin:{l:135,r:40,t:10,b:40},xaxis:{title:"Títulos",gridcolor:c.grid,dtick:1}}), PCFG);
  const fin = [...allDesempenho].sort((a,b)=>b.finais-a.finais || b.titulos-a.titulos || a.clube.localeCompare(b.clube));
  Plotly.react("ch-copa-finais", [{type:"bar",orientation:"h",y:fin.map(r=>r.clube).reverse(),x:fin.map(r=>r.finais).reverse(),marker:{color:c.accent2},text:fin.map(r=>`${r.titulos}T / ${r.vices}V`).reverse(),textposition:"outside",hovertemplate:"%{y}<br>%{x} final(is)<extra></extra>"}], plotLayout({margin:{l:135,r:55,t:10,b:40},xaxis:{title:"Finais",gridcolor:c.grid,dtick:1}}), PCFG);
  const uf = {}; allFinais.forEach(f => uf[f.uf_campeao || "-"] = (uf[f.uf_campeao || "-"] || 0) + 1);
  const ufArr = Object.entries(uf).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0]));
  Plotly.react("ch-copa-uf", [{type:"bar",x:ufArr.map(x=>x[0]),y:ufArr.map(x=>x[1]),marker:{color:c.accent3},text:ufArr.map(x=>x[1]),textposition:"outside"}], plotLayout({xaxis:{title:"UF",gridcolor:c.grid},yaxis:{title:"Títulos",gridcolor:c.grid,dtick:1}}), PCFG);
  Plotly.react("ch-copa-timeline", [{type:"scatter",mode:"markers+text",x:allFinais.map(f=>f.ano),y:allFinais.map(f=>f.campeao),text:allFinais.map(f=>f.campeao),textposition:"top center",textfont:{size:9},marker:{size:9,color:allFinais.map(f=>clubColor(f.campeao)),line:{color:c.text,width:.5}},hovertemplate:"%{x}<br>%{y}<extra></extra>"}], plotLayout({margin:{l:120,r:20,t:10,b:45},xaxis:{title:"Ano",gridcolor:c.grid,dtick:2},yaxis:{gridcolor:c.grid,automargin:true}}), PCFG);
  Plotly.react("ch-copa-evolucao", [
    {type:"scatter",mode:"lines+markers",name:"Times",x:allEdicoes.map(e=>e.ano),y:allEdicoes.map(e=>e.num_times),line:{color:c.accent,width:3}},
    {type:"scatter",mode:"lines+markers",name:"Jogos",x:allEdicoes.map(e=>e.ano),y:allEdicoes.map(e=>e.jogos),line:{color:c.accent2,width:3}},
    {type:"scatter",mode:"lines+markers",name:"Gols",x:allEdicoes.map(e=>e.ano),y:allEdicoes.map(e=>e.gols),line:{color:c.accent3,width:3},yaxis:"y2"},
  ], plotLayout({xaxis:{title:"Ano",gridcolor:c.grid,dtick:2},yaxis:{title:"Times / jogos",gridcolor:c.grid},yaxis2:{title:"Gols",overlaying:"y",side:"right",gridcolor:"rgba(0,0,0,0)"},legend:{orientation:"h",x:0,y:1.12}}), PCFG);
  const partCount = {}; allParticipantes.forEach(p => partCount[p.clube] = (partCount[p.clube] || 0) + 1);
  const partArr = Object.entries(partCount).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0])).slice(0,20);
  Plotly.react("ch-copa-participacoes", [{type:"bar",orientation:"h",y:partArr.map(x=>x[0]).reverse(),x:partArr.map(x=>x[1]).reverse(),marker:{color:partArr.map(x=>clubColor(x[0])).reverse(),line:{color:c.text,width:.7}},text:partArr.map(x=>x[1]).reverse(),textposition:"outside",hovertemplate:"%{y}<br>%{x} participação(ões) mapeada(s)<extra></extra>"}], plotLayout({margin:{l:135,r:40,t:10,b:40},xaxis:{title:"Participações mapeadas",gridcolor:c.grid,dtick:1}}), PCFG);

  const topClube = clube || partArr[0]?.[0] || allFinais[allFinais.length - 1]?.campeao || "";
  const pClube = allParticipantes.filter(p => p.clube === topClube).sort((a,b)=>a.ano-b.ano);
  const fClube = allFinais.filter(f => f.campeao === topClube || f.vice === topClube).sort((a,b)=>a.ano-b.ano);
  const dClube = allDesempenho.find(d => d.clube === topClube) || {titulos:0,vices:0,finais:0};
  const anosPart = new Set(pClube.map(p=>p.ano));
  document.getElementById("kpis-copa-clube").innerHTML = `
    <div class="kpi"><div class="v small">${topClube || "-"}</div><div class="l">Clube analisado</div></div>
    <div class="kpi"><div class="v">${anosPart.size}</div><div class="l">Participações mapeadas</div></div>
    <div class="kpi"><div class="v">${dClube.titulos}</div><div class="l">Títulos</div></div>
    <div class="kpi"><div class="v">${dClube.vices}</div><div class="l">Vices</div></div>
    <div class="kpi"><div class="v">${dClube.finais}</div><div class="l">Finais</div></div>
    <div class="kpi"><div class="v small">${pClube[0]?.ano || "-"} - ${pClube[pClube.length-1]?.ano || "-"}</div><div class="l">Período mapeado</div></div>`;
  const histYears = allEdicoes.map(e=>e.ano);
  Plotly.react("ch-copa-clube-hist", [{type:"bar",x:histYears,y:histYears.map(a=>anosPart.has(a)?1:0),marker:{color:histYears.map(a=>anosPart.has(a)?clubColor(topClube):"rgba(160,180,170,.18)")},hovertemplate:"%{x}<br>%{y:,.0f} participação<extra></extra>"}], plotLayout({xaxis:{title:"Ano",gridcolor:c.grid,dtick:2},yaxis:{title:"Participou",gridcolor:c.grid,dtick:1,range:[0,1.2]}}), PCFG);
  Plotly.react("ch-copa-clube-finais", [{type:"scatter",mode:"markers+text",x:fClube.map(f=>f.ano),y:fClube.map(f=>f.campeao===topClube?1:0),text:fClube.map(f=>f.campeao===topClube?"Campeão":"Vice"),textposition:"top center",marker:{size:14,color:fClube.map(f=>f.campeao===topClube?c.accent:c.accent2)},hovertemplate:"%{x}<br>%{text}<extra></extra>"}], plotLayout({xaxis:{title:"Ano",gridcolor:c.grid,dtick:2},yaxis:{tickvals:[0,1],ticktext:["Vice","Campeão"],gridcolor:c.grid,range:[-.4,1.4]}}), PCFG);
  const clubeRows = [...new Set([...pClube.map(p=>p.ano), ...fClube.map(f=>f.ano)])].sort((a,b)=>b-a).map(a => {
    const p = pClube.find(x=>x.ano===a);
    const f = fClube.find(x=>x.ano===a);
    return `<tr><td><b>${a}</b></td><td>${p ? "Sim" : "-"}</td><td>${f ? (f.campeao === topClube ? "Campeão" : "Vice") : "-"}</td><td>${f ? (f.campeao === topClube ? f.vice : f.campeao) : "-"}</td><td>${p?.criterio || ""}</td><td>${p?.terceira_fase ? "3a fase" : (p ? "1a fase" : "")}</td></tr>`;
  }).join("");
  document.getElementById("tbl-copa-clube").innerHTML = `<thead><tr><th>Ano</th><th>Participou</th><th>Final</th><th>Adversário final</th><th>Critério de vaga</th><th>Entrada</th></tr></thead><tbody>${clubeRows}</tbody>`;

  const edSel = edicoes[0] || allEdicoes[allEdicoes.length - 1] || {};
  const finalSel = allFinais.find(f => f.ano === edSel.ano) || {};
  const partSel = allParticipantes.filter(p => p.ano === edSel.ano);
  document.getElementById("kpis-copa-edicao").innerHTML = `
    <div class="kpi"><div class="v">${edSel.ano || "-"}</div><div class="l">Edição</div></div>
    <div class="kpi"><div class="v">${edSel.num_times || partSel.length || "-"}</div><div class="l">Times</div></div>
    <div class="kpi"><div class="v">${edSel.jogos || "-"}</div><div class="l">Jogos</div></div>
    <div class="kpi"><div class="v">${edSel.gols || "-"}</div><div class="l">Gols</div></div>
    <div class="kpi"><div class="v small">${finalSel.campeao || "-"}</div><div class="l">Campeão</div></div>
    <div class="kpi"><div class="v small">${finalSel.vice || "-"}</div><div class="l">Vice</div></div>`;
  const ufPart = {}; partSel.forEach(p => ufPart[p.uf || "-"] = (ufPart[p.uf || "-"] || 0) + 1);
  const ufPartArr = Object.entries(ufPart).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0]));
  Plotly.react("ch-copa-edicao-part", [{type:"bar",x:ufPartArr.map(x=>x[0]),y:ufPartArr.map(x=>x[1]),marker:{color:c.accent},text:ufPartArr.map(x=>x[1]),textposition:"outside"}], plotLayout({xaxis:{title:"UF",gridcolor:c.grid},yaxis:{title:"Participantes",gridcolor:c.grid}}), PCFG);
  Plotly.react("ch-copa-edicao-final", [{type:"bar",x:[finalSel.campeao || "Campeão", finalSel.vice || "Vice"],y:[finalSel.gols_campeao || 0, finalSel.gols_vice || 0],marker:{color:[clubColor(finalSel.campeao),clubColor(finalSel.vice)]},text:[finalSel.gols_campeao || 0, finalSel.gols_vice || 0],textposition:"outside"}], plotLayout({yaxis:{title:"Gols agregados",gridcolor:c.grid,dtick:1}}), PCFG);
  document.getElementById("tbl-copa-edicoes").innerHTML = `<thead><tr><th>Ano</th><th>Datas</th><th class="num">Times</th><th class="num">Jogos</th><th class="num">Gols</th><th>Artilheiro</th><th>Campeão</th><th>Vice</th><th class="num">Participantes mapeados</th></tr></thead><tbody>` +
    edicoes.slice().reverse().map(e => `<tr><td><b>${e.ano}</b></td><td>${e.datas}</td><td class="num">${e.num_times || ""}</td><td class="num">${e.jogos || ""}</td><td class="num">${e.gols || ""}</td><td>${e.artilheiro}</td><td><b>${e.campeao}</b></td><td>${e.vice}</td><td class="num">${e.participantes_mapeados || ""}</td></tr>`).join("") + `</tbody>`;
  document.getElementById("tbl-copa-participantes").innerHTML = `<thead><tr><th>Ano</th><th>Clube</th><th>UF</th><th>Associação</th><th>Critério</th><th>Entrada</th></tr></thead><tbody>` +
    participantes.slice().reverse().map(p => `<tr><td><b>${p.ano}</b></td><td><b>${p.clube}</b></td><td>${p.uf}</td><td>${p.associacao}</td><td>${p.criterio}</td><td>${p.terceira_fase ? "3a fase" : "1a fase"}</td></tr>`).join("") + `</tbody>`;

  const crit = {}; finais.forEach(f => {
    const label = copaCriterioLabel(f.criterio);
    crit[label] = (crit[label] || 0) + 1;
  });
  const critArr = Object.entries(crit).sort((a,b)=>b[1]-a[1]);
  Plotly.react("ch-copa-criterios", [{type:"bar",x:critArr.map(x=>x[0]),y:critArr.map(x=>x[1]),marker:{color:c.accent2},text:critArr.map(x=>x[1]),textposition:"outside"}], plotLayout({yaxis:{title:"Finais",gridcolor:c.grid,dtick:1}}), PCFG);
  Plotly.react("ch-copa-gols-finais", [{type:"scatter",mode:"lines+markers",x:finais.map(f=>f.ano),y:finais.map(f=>(f.gols_campeao||0)+(f.gols_vice||0)),line:{color:c.accent,width:3},hovertemplate:"%{x}<br>%{y} gols agregados<extra></extra>"}], plotLayout({xaxis:{title:"Ano",gridcolor:c.grid,dtick:2},yaxis:{title:"Gols",gridcolor:c.grid,dtick:1}}), PCFG);
  document.getElementById("tbl-copa-finais").innerHTML = `<thead><tr><th>Ano</th><th>Campeão</th><th>Vice</th><th class="num">Agregado</th><th>Critério</th><th>Resumo</th></tr></thead><tbody>` +
    finais.slice().reverse().map(f => `<tr><td><b>${f.ano}</b></td><td><b>${f.campeao}</b></td><td>${f.vice}</td><td class="num">${f.gols_campeao}-${f.gols_vice}</td><td>${copaCriterioLabel(f.criterio)}</td><td>${f.resumo}</td></tr>`).join("") + `</tbody>`;
  document.getElementById("tbl-copa-partidas").innerHTML = `<thead><tr><th>Ano</th><th class="num">Jogo</th><th>Mandante</th><th class="num">Placar</th><th>Visitante</th><th>Estádio</th><th>Local</th></tr></thead><tbody>` +
    partidas.slice().reverse().map(p => `<tr><td><b>${p.ano}</b></td><td class="num">${p.jogo}</td><td>${p.mandante}</td><td class="num"><b>${p.gm}-${p.gv}</b></td><td>${p.visitante}</td><td>${p.estadio}</td><td>${p.local}</td></tr>`).join("") + `</tbody>`;
}

// RENDER POR ABA
// ====================================================================
function render() {
  if (state.competition === "copa_brasil") { renderCopaBrasil(); return; }
  const f = getFiltered();
  if (state.tab === "resumo") renderResumo(f);
  else if (state.tab === "classificacao") renderClass(f);
  else if (state.tab === "evolucao") renderEvol(f);
  else if (state.tab === "times-geral") renderTimesGeral();
  else if (state.tab === "mando") renderMando(f);
  else if (state.tab === "ataque") renderAtaque(f);
  else if (state.tab === "forma") renderForma(f);
  else if (state.tab === "jogadores") renderJogadores(f);
  else if (state.tab === "partidas") renderPartidas(f);
  else if (state.tab === "disciplina") renderDisc(f);
  else if (state.tab === "rankings") renderRank(f);
  else if (state.tab === "campeonato") renderCampeonato(f);
  else if (state.tab === "comparar") renderComparar();
  else if (state.tab === "campanhas") renderCampanhas();
  else if (state.tab === "confronto") renderConfronto();
  else if (state.tab === "tecnicos") renderTecnicos();
  else if (state.tab === "geografia") renderGeografia();
  else if (state.tab === "indices") renderIndices();
  else if (state.tab === "perguntas") renderPerguntas();
  else if (state.tab === "historico-final") renderHistoricoFinal();
  else if (state.tab === "historico") renderHistorico();
}

// =====================================================================
// ÍNDICES HISTÓRICOS
// =====================================================================
function _normalize(arr, val, invert=false) {
  if (!arr.length) return 0;
  const min = Math.min(...arr), max = Math.max(...arr);
  if (max === min) return 50;
  const n = (val - min) / (max - min) * 100;
  return invert ? 100 - n : n;
}

function renderIndices() {
  const c = getThemeColors();
  // ---- DOMINÂNCIA dos campeões ----
  const camps = [];
  DATA.temporadas.forEach(t => {
    const ult = Math.max(...DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada));
    const tab = DATA.class_rodada.filter(r=>r.temporada===t && r.rodada===ult).slice().sort((a,b)=>a.pos-b.pos);
    if (!tab.length) return;
    const camp = tab[0], vice = tab[1];
    // rodadas como líder
    let rodLider = 0;
    for (let r = 1; r <= ult; r++) {
      const lider = DATA.class_rodada.find(x => x.temporada===t && x.rodada===r && x.pos===1);
      if (lider && lider.clube === camp.clube) rodLider++;
    }
    const melhorAtq = Math.max(...tab.map(x=>x.gp));
    const melhorDef = Math.min(...tab.map(x=>x.gc));
    camps.push({
      temp:t, clube:camp.clube,
      diffVice: camp.p - (vice?.p||0),
      sg: camp.sg,
      rodLider,
      pctLider: rodLider/ult*100,
      apr: camp.apr,
      melhorAtq: camp.gp === melhorAtq,
      melhorDef: camp.gc === melhorDef,
    });
  });
  // normalizar componentes
  const arr_dv = camps.map(c=>c.diffVice);
  const arr_sg = camps.map(c=>c.sg);
  const arr_rl = camps.map(c=>c.pctLider);
  const arr_ap = camps.map(c=>c.apr);
  camps.forEach(x => {
    const ndv = _normalize(arr_dv, x.diffVice);
    const nsg = _normalize(arr_sg, x.sg);
    const nrl = _normalize(arr_rl, x.pctLider);
    const nap = _normalize(arr_ap, x.apr);
    const bonus = (x.melhorAtq?5:0) + (x.melhorDef?5:0);
    x.idx = +(ndv*0.3 + nsg*0.2 + nrl*0.25 + nap*0.2 + bonus).toFixed(1);
  });
  camps.sort((a,b) => b.idx - a.idx);
  document.getElementById("tbl-idx-dom").innerHTML = `<thead><tr>
    <th>#</th><th>Temp</th><th>Campeão</th><th class="num">Δ vice</th><th class="num">SG</th>
    <th class="num">% Lider</th><th class="num">APR%</th><th class="num">Melhor Atq/Def</th><th class="num">Índice</th>
  </tr></thead><tbody>` + camps.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.diffVice}</td><td class="num">${r.sg>0?"+":""}${r.sg}</td>
    <td class="num">${r.pctLider.toFixed(0)}%</td><td class="num">${r.apr.toFixed(1)}</td>
    <td class="num">${r.melhorAtq && r.melhorDef ? "Atq/Def" : r.melhorAtq ? "Atq" : r.melhorDef ? "Def" : "—"}</td>
    <td class="num"><b style="color:var(--warn)">${r.idx}</b></td>
  </tr>`).join("") + "</tbody>";
  Plotly.react("ch-idx-dom", [{
    type:"bar", orientation:"h",
    x: camps.map(r=>r.idx).reverse(),
    y: camps.map(r=>`${r.temp} ${r.clube}`).reverse(),
    marker:{color: c.warn}, text: camps.map(r=>r.idx).reverse(), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>Índice: %{x}<extra></extra>"
  }], plotLayout({margin:{l:160,r:30,t:10,b:30}}), PCFG);

  // ---- SOFRIMENTO (escapou) ----
  const sofridos = [];
  DATA.temporadas.forEach(t => {
    const ult = Math.max(...DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada));
    const tabFinal = DATA.class_rodada.filter(r=>r.temporada===t && r.rodada===ult);
    // só clubes que escaparam (pos 13-16 final)
    tabFinal.filter(r => r.pos >= 13 && r.pos <= 16).forEach(r => {
      // contar rodadas no Z4
      const minhasRodadas = DATA.class_rodada.filter(x => x.temporada===t && x.clube===r.clube);
      const noZ4 = minhasRodadas.filter(x => x.pos >= 17).length;
      // distância mínima para corte (pts pos 16 - meus pts) negativo se eu fui pior
      let minDist = Infinity;
      minhasRodadas.forEach(x => {
        const corte16 = DATA.class_rodada.find(y=>y.temporada===t && y.rodada===x.rodada && y.pos===16);
        const corte17 = DATA.class_rodada.find(y=>y.temporada===t && y.rodada===x.rodada && y.pos===17);
        if (corte17) {
          const dist = x.p - corte17.p;
          if (dist < minDist) minDist = dist;
        }
      });
      sofridos.push({temp:t, clube:r.clube, posFinal:r.pos, noZ4, minDist});
    });
  });
  // normalização e índice
  const arr_z4 = sofridos.map(x=>x.noZ4);
  const arr_md = sofridos.map(x=>x.minDist);
  sofridos.forEach(x => {
    const nz = _normalize(arr_z4, x.noZ4);
    const nd = _normalize(arr_md, x.minDist, true);  // menor dist = mais sofreu (invert)
    const npF = (17 - x.posFinal); // 1-4
    x.idx = +(nz*0.5 + nd*0.35 + npF*5).toFixed(1);
  });
  sofridos.sort((a,b) => b.idx - a.idx);
  document.getElementById("tbl-idx-sof").innerHTML = `<thead><tr>
    <th>#</th><th>Temp</th><th>Clube</th><th class="num">Pos final</th>
    <th class="num">Rodadas no Z4</th><th class="num">Menor dist. p/ corte</th><th class="num">Índice</th>
  </tr></thead><tbody>` + sofridos.slice(0,15).map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.posFinal}º</td>
    <td class="num">${r.noZ4}</td>
    <td class="num">${r.minDist === Infinity ? "—" : (r.minDist > 0 ? "+" : "") + r.minDist + " pts"}</td>
    <td class="num"><b style="color:var(--danger)">${r.idx}</b></td>
  </tr>`).join("") + "</tbody>";

  // ---- REGULARIDADE ----
  const regs = [];
  DATA.temporadas.forEach(t => {
    const rods = [...new Set(DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada))].sort((a,b)=>a-b);
    const clubes = [...new Set(DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.clube))];
    clubes.forEach(cl => {
      const positions = rods.map(rod => {
        const r = DATA.class_rodada.find(x => x.temporada===t && x.rodada===rod && x.clube===cl);
        return r ? r.pos : null;
      }).filter(p => p !== null);
      if (positions.length < 5) return;
      const mean = positions.reduce((s,x)=>s+x,0) / positions.length;
      const std = Math.sqrt(positions.reduce((s,x)=>s+(x-mean)**2,0) / positions.length);
      const ult = DATA.class_rodada.find(r=>r.temporada===t && r.rodada===rods[rods.length-1] && r.clube===cl);
      regs.push({temp:t, clube:cl, std, posMedia:mean, posFinal:ult?.pos});
    });
  });
  // índice = 100 - normalize(std)
  const arr_std = regs.map(r=>r.std);
  regs.forEach(r => { r.idx = +(100 - _normalize(arr_std, r.std)).toFixed(1); });
  regs.sort((a,b) => b.idx - a.idx);
  document.getElementById("tbl-idx-reg").innerHTML = `<thead><tr>
    <th>#</th><th>Temp</th><th>Clube</th><th class="num">σ posição</th>
    <th class="num">Pos. média</th><th class="num">Pos final</th><th class="num">Índice</th>
  </tr></thead><tbody>` + regs.slice(0,15).map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.std.toFixed(2)}</td><td class="num">${r.posMedia.toFixed(1)}</td>
    <td class="num">${r.posFinal}º</td>
    <td class="num"><b style="color:var(--accent2)">${r.idx}</b></td>
  </tr>`).join("") + "</tbody>";

  // ---- ARRANCADA / QUEDA ----
  const movimentos = [];
  DATA.temporadas.forEach(t => {
    const rods = [...new Set(DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada))].sort((a,b)=>a-b);
    const meio = Math.floor(rods[rods.length-1] / 2);
    const clubes = [...new Set(DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.clube))];
    clubes.forEach(cl => {
      const meioRow = DATA.class_rodada.find(x=>x.temporada===t && x.rodada===meio && x.clube===cl);
      const finalRow = DATA.class_rodada.find(x=>x.temporada===t && x.rodada===rods[rods.length-1] && x.clube===cl);
      if (!meioRow || !finalRow) return;
      const ganho = meioRow.pos - finalRow.pos;  // positivo = melhorou
      // pts últimas 10 (proxy)
      const u10 = DATA.class_rodada.find(x=>x.temporada===t && x.rodada===Math.max(1, rods[rods.length-1]-10) && x.clube===cl);
      const ptsU10 = u10 ? finalRow.p - u10.p : finalRow.p;
      movimentos.push({
        temp:t, clube:cl, posMeio:meioRow.pos, posFinal:finalRow.pos, ganho, ptsU10,
      });
    });
  });
  const arrancadas = [...movimentos].sort((a,b) => b.ganho - a.ganho).slice(0,15);
  const quedas = [...movimentos].sort((a,b) => a.ganho - b.ganho).slice(0,15);
  document.getElementById("tbl-idx-arr").innerHTML = `<thead><tr>
    <th>#</th><th>Temp</th><th>Clube</th><th class="num">Pos meio</th>
    <th class="num">Pos final</th><th class="num">Δ Pos</th><th class="num">Pts últ.10</th>
  </tr></thead><tbody>` + arrancadas.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.posMeio}º</td><td class="num">${r.posFinal}º</td>
    <td class="num"><b style="color:var(--accent)">+${r.ganho}</b></td>
    <td class="num">${r.ptsU10}</td>
  </tr>`).join("") + "</tbody>";
  document.getElementById("tbl-idx-queda").innerHTML = `<thead><tr>
    <th>#</th><th>Temp</th><th>Clube</th><th class="num">Pos meio</th>
    <th class="num">Pos final</th><th class="num">Δ Pos</th><th class="num">Pts últ.10</th>
  </tr></thead><tbody>` + quedas.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.posMeio}º</td><td class="num">${r.posFinal}º</td>
    <td class="num"><b style="color:var(--danger)">${r.ganho}</b></td>
    <td class="num">${r.ptsU10}</td>
  </tr>`).join("") + "</tbody>";
}

// =====================================================================
// INSIGHTS HISTÓRICOS
// =====================================================================
function renderPerguntas() {
  const cards = [];

  // Helper: pega tabela final de cada temporada
  const tabsFinais = {};
  DATA.temporadas.forEach(t => {
    const ult = Math.max(...DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada));
    tabsFinais[t] = DATA.class_rodada.filter(r=>r.temporada===t && r.rodada===ult).slice().sort((a,b)=>a.pos-b.pos);
  });

  // 1. Quem dominou cada campeonato? (rodadas como líder)
  const dominantes = DATA.temporadas.map(t => {
    const rods = rodadasTemp(t);
    const lideresCount = {};
    rods.forEach(r => {
      const lid = DATA.class_rodada.find(x=>x.temporada===t && x.rodada===r && x.pos===1);
      if (lid) lideresCount[lid.clube] = (lideresCount[lid.clube]||0) + 1;
    });
    const top = Object.entries(lideresCount).sort((a,b)=>b[1]-a[1])[0];
    const camp = tabsFinais[t][0];
    const liderouMaisQueOCampeao = top && top[0] !== camp.clube ? top[0] : null;
    return {temp:t, camp:camp.clube, liderou:top?top[0]:"—", rodLider:top?top[1]:0, total:rods.length, alguemLiderouMais:liderouMaisQueOCampeao};
  });
  cards.push({
    titulo: "Quem dominou cada campeonato?",
    insight: `Em ${dominantes.filter(d=>!d.alguemLiderouMais).length}/${dominantes.length} temporadas o campeão também foi quem mais liderou. Em ${dominantes.filter(d=>d.alguemLiderouMais).length} casos, outro time liderou mais rodadas mas não fechou o título.`,
    tipo: "tabela",
    dados: dominantes.map(d => [d.temp, d.camp, `${d.liderou} (${d.rodLider}/${d.total})`, d.alguemLiderouMais ? d.alguemLiderouMais : "Campeão"]),
    headers: ["Temp", "Campeão", "Mais rodadas líder", "Coincide?"],
  });

  // 2. Qual foi o campeonato mais equilibrado?
  const eq = DATA.temporadas.map(t => {
    const ps = tabsFinais[t].map(x=>x.p);
    const m = ps.reduce((s,x)=>s+x,0)/ps.length;
    const std = Math.sqrt(ps.reduce((s,x)=>s+(x-m)**2,0)/ps.length);
    return {temp:t, std, dif1u: ps[0]-ps[ps.length-1], dif12: ps[0]-(ps[1]||0)};
  }).sort((a,b)=>a.std-b.std);
  cards.push({
    titulo: "Campeonatos mais equilibrados",
    insight: `Mais equilibrado: <b>${eq[0].temp}</b> (σ=${eq[0].std.toFixed(1)}). Mais desequilibrado: <b>${eq[eq.length-1].temp}</b> (σ=${eq[eq.length-1].std.toFixed(1)}). σ baixo = pontuações mais próximas entre clubes.`,
    tipo: "tabela",
    dados: eq.map(d => [d.temp, d.std.toFixed(1), d.dif12, d.dif1u]),
    headers: ["Temp", "σ pts", "Δ 1º × 2º", "Δ 1º × último"],
  });

  // 3. Melhor ataque ganha campeonato?
  const atq = DATA.temporadas.map(t => {
    const tab = tabsFinais[t];
    const camp = tab[0];
    const melhorAtq = [...tab].sort((a,b)=>b.gp-a.gp)[0];
    return {temp:t, camp:camp.clube, melhorAtq:melhorAtq.clube, mesmo: camp.clube === melhorAtq.clube};
  });
  const acertosAtq = atq.filter(x=>x.mesmo).length;
  cards.push({
    titulo: "Relação entre melhor ataque e título",
    insight: `Em <b>${acertosAtq}/${atq.length}</b> temporadas o campeão também foi o melhor ataque. ${acertosAtq > atq.length/2 ? "A relação histórica é forte." : "A relação histórica é parcial; defesa e regularidade também pesam."}`,
    tipo: "tabela",
    dados: atq.map(d => [d.temp, d.camp, d.melhorAtq, d.mesmo ? "Sim" : "Não"]),
    headers: ["Temp", "Campeão", "Melhor ataque", "Coincide?"],
  });

  // 4. Melhor defesa ganha campeonato?
  const def = DATA.temporadas.map(t => {
    const tab = tabsFinais[t];
    const camp = tab[0];
    const melhorDef = [...tab].sort((a,b)=>a.gc-b.gc)[0];
    return {temp:t, camp:camp.clube, melhorDef:melhorDef.clube, mesmo: camp.clube === melhorDef.clube};
  });
  const acertosDef = def.filter(x=>x.mesmo).length;
  cards.push({
    titulo: "Relação entre melhor defesa e título",
    insight: `Em <b>${acertosDef}/${def.length}</b> temporadas o campeão também teve a melhor defesa. ${acertosDef > acertosAtq ? "A melhor defesa coincidiu mais vezes com o campeão do que o melhor ataque." : acertosDef < acertosAtq ? "O melhor ataque coincidiu mais vezes com o campeão do que a melhor defesa." : "Ataque e defesa tiveram a mesma frequência de coincidência com o campeão."}`,
    tipo: "tabela",
    dados: def.map(d => [d.temp, d.camp, d.melhorDef, d.mesmo ? "Sim" : "Não"]),
    headers: ["Temp", "Campeão", "Melhor defesa", "Coincide?"],
  });

  // 5. Qual time mais sofreu para não cair?
  const sofridos = [];
  DATA.temporadas.forEach(t => {
    tabsFinais[t].filter(r=>r.pos>=13 && r.pos<=16).forEach(r => {
      const noZ4 = DATA.class_rodada.filter(x=>x.temporada===t && x.clube===r.clube && x.pos>=17).length;
      sofridos.push({temp:t, clube:r.clube, pos:r.pos, noZ4});
    });
  });
  sofridos.sort((a,b)=>b.noZ4-a.noZ4);
  cards.push({
    titulo: "Clubes que mais sofreram para não cair",
    insight: `Recorde: <b>${sofridos[0].clube}</b> (${sofridos[0].temp}) passou <b>${sofridos[0].noZ4} rodadas</b> dentro do Z4 mas terminou em ${sofridos[0].pos}º.`,
    tipo: "tabela",
    dados: sofridos.slice(0,8).map(d => [d.temp, d.clube, d.pos+"º", d.noZ4+" rod."]),
    headers: ["Temp", "Clube", "Pos final", "Rodadas no Z4"],
  });

  // 6. O mando de campo pesa?
  const mando = DATA.temporadas.map(t => {
    const ms = DATA.matches.filter(m=>m.temporada===t);
    const vM = ms.filter(m=>m.gm>m.gv).length / ms.length * 100;
    return {temp:t, vM, total:ms.length};
  });
  const mediaMando = mando.reduce((s,x)=>s+x.vM,0)/mando.length;
  cards.push({
    titulo: "Peso do mando de campo",
    insight: `Média histórica: <b>${mediaMando.toFixed(1)}%</b> de vitórias do mandante. Acima de 45% = mando pesa muito; ~33% = jogos equilibrados; <33% = mando irrelevante.`,
    tipo: "tabela",
    dados: mando.map(d => [d.temp, d.vM.toFixed(1)+"%"]),
    headers: ["Temp", "% V Mand."],
  });

  // 7. A força do mando aumentou ou diminuiu?
  const tendencia = mando[mando.length-1].vM - mando[0].vM;
  cards.push({
    titulo: "Variação da força do mando",
    insight: `Variação ${mando[0].temp} → ${mando[mando.length-1].temp}: <b>${tendencia>0?"+":""}${tendencia.toFixed(1)} pp</b>. ${Math.abs(tendencia)<2 ? "Praticamente estável." : tendencia>0 ? "Mando ficou MAIS forte." : "Mando enfraqueceu (mais empates/vitórias visitantes)."}`,
    tipo: "kpi",
    valor: `${tendencia>0?"+":""}${tendencia.toFixed(1)}pp`,
  });

  // 8. Qual clube é mais regular (G6 sempre)?
  const top6count = {};
  DATA.temporadas.forEach(t => {
    tabsFinais[t].slice(0,6).forEach(r => { top6count[r.clube] = (top6count[r.clube]||0)+1; });
  });
  const top6Arr = Object.entries(top6count).sort((a,b)=>b[1]-a[1]).slice(0,8);
  cards.push({
    titulo: "Clubes mais frequentes no G6",
    insight: `<b>${top6Arr[0][0]}</b> esteve no G6 em <b>${top6Arr[0][1]}</b> das ${DATA.temporadas.length} temporadas (${(top6Arr[0][1]/DATA.temporadas.length*100).toFixed(0)}%).`,
    tipo: "tabela",
    dados: top6Arr.map(([cl,n])=>[cl, `${n}/${DATA.temporadas.length}`, `${(n/DATA.temporadas.length*100).toFixed(0)}%`]),
    headers: ["Clube", "Vezes G6", "%"],
  });

  // 9. Pts mín. para escapar do Z4 — está subindo ou descendo?
  const corte = DATA.temporadas.map(t => ({temp:t, pts: tabsFinais[t][15]?.p || 0}));
  const tendCorte = corte[corte.length-1].pts - corte[0].pts;
  cards.push({
    titulo: "Linha de corte do Z4",
    insight: `Média de pts do 16º colocado nas temporadas disponíveis: <b>${(corte.reduce((s,x)=>s+x.pts,0)/corte.length).toFixed(1)} pts</b>. Tendência ${corte[0].temp}→${corte[corte.length-1].temp}: <b>${tendCorte>0?"+":""}${tendCorte} pts</b>.`,
    tipo: "tabela",
    dados: corte.map(d => [d.temp, d.pts+" pts"]),
    headers: ["Temp", "Pts do 16º"],
  });

  // 10. Empate é cada vez mais raro?
  const empates = DATA.temporadas.map(t => {
    const ms = DATA.matches.filter(m=>m.temporada===t);
    const e = ms.filter(m=>m.gm===m.gv).length;
    return {temp:t, n:e, pct: e/ms.length*100};
  });
  const tendE = empates[empates.length-1].pct - empates[0].pct;
  cards.push({
    titulo: "Evolução do percentual de empates",
    insight: `Variação: <b>${tendE>0?"+":""}${tendE.toFixed(1)} pp</b> de ${empates[0].temp} a ${empates[empates.length-1].temp}. ${Math.abs(tendE)<2 ? "Estável." : tendE<0 ? "Menos empates: jogos mais decisivos." : "Mais empates: jogos mais cautelosos."}`,
    tipo: "tabela",
    dados: empates.map(d=>[d.temp, d.n, d.pct.toFixed(1)+"%"]),
    headers: ["Temp", "Empates", "%"],
  });

  // 11. O campeão tinha o artilheiro?
  const campArt = DATA.temporadas.map(t => {
    const camp = tabsFinais[t][0];
    const gols = DATA.goals.filter(g=>g.temporada===t && g.tipo!=="Gol Contra");
    const map = {};
    gols.forEach(g=>{ map[g.atleta+"|"+g.clube] = (map[g.atleta+"|"+g.clube]||0)+1; });
    const top = Object.entries(map).sort((a,b)=>b[1]-a[1])[0];
    if (!top) return null;
    const [n, cl] = top[0].split("|");
    return {temp:t, camp:camp.clube, art:n, artClube:cl, gols:top[1], mesmo: cl === camp.clube};
  }).filter(Boolean);
  const sims = campArt.filter(x=>x.mesmo).length;
  cards.push({
    titulo: "Relação entre artilheiro e campeão",
    insight: `<b>${sims}/${campArt.length}</b> campeões tinham também o artilheiro do campeonato. ${sims < campArt.length/2 ? "Historicamente, o artilheiro individual não é um indicador forte de título." : "Historicamente, há uma relação forte entre ter o artilheiro e conquistar o título."}`,
    tipo: "tabela",
    dados: campArt.map(d => [d.temp, d.camp, `${d.art} (${d.artClube})`, d.gols, d.mesmo ? "Sim" : "Não"]),
    headers: ["Temp", "Campeão", "Artilheiro", "Gols", "Coincide?"],
  });

  // 12. O campeão arrancou no fim ou liderou cedo?
  const arrancada = DATA.temporadas.map(t => {
    const camp = tabsFinais[t][0];
    const meio = Math.floor(rodadasTemp(t).length / 2);
    const meioRow = DATA.class_rodada.find(x=>x.temporada===t && x.rodada===meio && x.clube===camp.clube);
    return {temp:t, camp:camp.clube, posMeio: meioRow?.pos || "—", arrancou: meioRow && meioRow.pos > 3};
  });
  cards.push({
    titulo: "Caminho do campeão no segundo turno",
    insight: `Em <b>${arrancada.filter(a=>!a.arrancou).length}/${arrancada.length}</b> temporadas o campeão já estava no top 3 no fim do 1º turno. Os outros foram <b>arrancadas</b> de fim de campeonato.`,
    tipo: "tabela",
    dados: arrancada.map(d => [d.temp, d.camp, d.posMeio+"º", d.arrancou ? "Arrancada" : "Top 3 no 1º turno"]),
    headers: ["Temp", "Campeão", "Pos meio campto", "Tipo"],
  });

  // Renderizar todos os cards num grid 2 colunas
  const html = cards.map(c => {
    let body = "";
    if (c.tipo === "kpi") {
      body = `<div style="font-size:42px;font-weight:700;color:var(--accent);text-align:center;margin:14px 0">${c.valor}</div>`;
    } else if (c.tipo === "tabela") {
      body = `<table style="margin-top:8px"><thead><tr>${c.headers.map(h=>`<th>${h}</th>`).join("")}</tr></thead><tbody>` +
        c.dados.map(row => `<tr>${row.map((v,i)=>`<td${i>=2?' class="num"':""}>${v}</td>`).join("")}</tr>`).join("") +
        "</tbody></table>";
    }
    return `<div class="card" style="margin-bottom:18px">
      <h2>${c.titulo}</h2>
      <p style="color:var(--text);font-size:13px;background:var(--panel2);padding:10px 14px;border-radius:6px;border-left:3px solid var(--accent);margin:0 0 8px">${c.insight}</p>
      ${body}
    </div>`;
  }).join("");
  document.getElementById("grid-perguntas").innerHTML = `<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">${html}</div>`;
}

// =====================================================================
// COMPARAR TIMES (head-to-head + carreira histórica)
// =====================================================================
function popularSelectsCf() {
  const a = document.getElementById("cf-a"), b = document.getElementById("cf-b");
  if (a.options.length) return;
  // Lista de todos clubes que apareceram em qualquer temporada
  const todosClubes = new Set();
  DATA.temporadas.forEach(t => DATA.clubes_por_temporada[t].forEach(c => todosClubes.add(c)));
  [...todosClubes].sort().forEach(c => {
    a.appendChild(new Option(c, c));
    b.appendChild(new Option(c, c));
  });
  a.value = "Palmeiras"; b.value = "Flamengo";
  const minS = document.getElementById("cf-min"), maxS = document.getElementById("cf-max");
  DATA.temporadas.forEach(t => {
    minS.appendChild(new Option(t, t));
    maxS.appendChild(new Option(t, t));
  });
  minS.value = DATA.temporadas[0];
  maxS.value = DATA.temporadas[DATA.temporadas.length-1];
  [a,b,minS,maxS].forEach(el => el.onchange = renderConfronto);
}
// =====================================================================
// TIMES — VISÃO GERAL (cross-temporada, todos os campeonatos somados)
// =====================================================================
function _carreiraDeClube(clube) {
  // Pega o snapshot da última rodada de cada temporada que esse clube disputou
  const out = [];
  DATA.temporadas.forEach(t => {
    const snaps = DATA.class_rodada.filter(r => r.temporada === t && r.clube === clube);
    if (!snaps.length) return;
    const ult = Math.max(...snaps.map(r => r.rodada));
    const r = snaps.find(x => x.rodada === ult);
    if (r) out.push({...r, temporada: t});
  });
  return out;
}

function _agregarClubes() {
  // Para cada clube que apareceu em qualquer temporada, agrega tudo
  const clubes = new Set();
  DATA.temporadas.forEach(t => (DATA.clubes_por_temporada[t] || []).forEach(c => clubes.add(c)));
  return [...clubes].map(cl => {
    const carr = _carreiraDeClube(cl);
    if (!carr.length) return null;
    const part = carr.length;
    const titulos = carr.filter(r => r.pos === 1).length;
    const g6     = carr.filter(r => r.pos <= 6).length;
    const sula   = carr.filter(r => r.pos > 6 && r.pos <= 12).length;
    // usa zona REAL calculada no banco (considera tamanho variável: 24/22/20 clubes por temporada)
    const rebs   = carr.filter(r => r.zona === "rebaixamento").length;
    const pts    = carr.reduce((s,r) => s+r.p, 0);
    const j      = carr.reduce((s,r) => s+r.j, 0);
    const v      = carr.reduce((s,r) => s+r.v, 0);
    const e      = carr.reduce((s,r) => s+r.e, 0);
    const d      = carr.reduce((s,r) => s+r.d, 0);
    const gp     = carr.reduce((s,r) => s+r.gp, 0);
    const gc     = carr.reduce((s,r) => s+r.gc, 0);
    const aprMed = carr.reduce((s,r) => s+r.apr, 0) / part;
    const ptsMed = pts / part;
    const melhor = Math.min(...carr.map(r => r.pos));
    const pior   = Math.max(...carr.map(r => r.pos));
    const posMed = carr.reduce((s,r) => s+r.pos, 0) / part;
    return {
      clube: cl, part, titulos, g6, sula, rebs,
      pts, j, v, e, d, gp, gc, sg: gp - gc,
      aprMed, ptsMed, melhor, pior, posMed,
      tempIni: Math.min(...carr.map(r => r.temporada)),
      tempFim: Math.max(...carr.map(r => r.temporada)),
    };
  }).filter(Boolean);
}

let _tgState = { sortCol: "pts", sortDir: "desc" };

function getTGPosClubes() {
  const counts = {};
  (DATA.class_final_hist || []).forEach(r => counts[r.clube] = (counts[r.clube] || 0) + 1);
  return Object.entries(counts).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0])).map(x=>x[0]);
}

function getTGPosRows() {
  return (DATA.class_final_hist || [])
    .filter(r => r.clube === state.tgPosClube)
    .sort((a,b)=>a.temporada-b.temporada || String(a.edicao_id).localeCompare(String(b.edicao_id)) || a.pos-b.pos);
}

function stopTGPosRace() {
  if (tgPosTimer) clearTimeout(tgPosTimer);
  tgPosTimer = null;
  state.tgPosPlaying = false;
  const btn = document.getElementById("tg-pos-play");
  if (btn) btn.textContent = "Play";
}

function stepTGPosRace(delta) {
  const rows = getTGPosRows();
  if (!rows.length) return;
  state.tgPosIdx = Math.max(0, Math.min(rows.length - 1, state.tgPosIdx + delta));
  renderTGPosRace();
}

function scheduleTGPosRace() {
  if (!state.tgPosPlaying) return;
  const rows = getTGPosRows();
  if (!rows.length || state.tgPosIdx >= rows.length - 1) {
    stopTGPosRace();
    return;
  }
  tgPosTimer = setTimeout(() => {
    state.tgPosIdx += 1;
    renderTGPosRace();
    scheduleTGPosRace();
  }, 850);
}

function toggleTGPosRace() {
  if (state.tgPosPlaying) {
    stopTGPosRace();
    return;
  }
  const rows = getTGPosRows();
  if (!rows.length) return;
  if (state.tgPosIdx >= rows.length - 1) state.tgPosIdx = 0;
  state.tgPosPlaying = true;
  const btn = document.getElementById("tg-pos-play");
  if (btn) btn.textContent = "Pause";
  renderTGPosRace();
  scheduleTGPosRace();
}

function setupTGPosControls() {
  const clubes = getTGPosClubes();
  const sel = document.getElementById("tg-pos-clube");
  const play = document.getElementById("tg-pos-play");
  const prev = document.getElementById("tg-pos-prev");
  const next = document.getElementById("tg-pos-next");
  const range = document.getElementById("tg-pos-range");
  if (!sel || !clubes.length) return;

  const selectedFromFilter = state.clubesSel.find(c => clubes.includes(c));
  if (!state.tgPosClube || !clubes.includes(state.tgPosClube)) {
    state.tgPosClube = selectedFromFilter || clubes[0];
    state.tgPosIdx = 0;
  }
  sel.innerHTML = clubes.map(c => `<option value="${c}">${c}</option>`).join("");
  sel.value = state.tgPosClube;
  sel.onchange = () => {
    stopTGPosRace();
    state.tgPosClube = sel.value;
    state.tgPosIdx = 0;
    renderTGPosRace();
  };
  if (play) play.onclick = toggleTGPosRace;
  if (prev) prev.onclick = () => { stopTGPosRace(); stepTGPosRace(-1); };
  if (next) next.onclick = () => { stopTGPosRace(); stepTGPosRace(1); };
  if (range) {
    range.oninput = () => {
      stopTGPosRace();
      state.tgPosIdx = +range.value;
      renderTGPosRace();
    };
  }
}

function renderTGPosRace() {
  const c = getThemeColors();
  const rows = getTGPosRows();
  const range = document.getElementById("tg-pos-range");
  const label = document.getElementById("tg-pos-year-label");
  if (!rows.length) {
    Plotly.react("ch-tg-pos-race", [], plotLayout({annotations:[{text:"Sem campanhas para o clube selecionado",showarrow:false,x:0.5,y:0.5,xref:"paper",yref:"paper",font:{color:c.muted}}]}), PCFG);
    if (label) label.textContent = "";
    return;
  }
  state.tgPosIdx = Math.max(0, Math.min(rows.length - 1, state.tgPosIdx || 0));
  if (range) {
    range.min = 0;
    range.max = rows.length - 1;
    range.step = 1;
    range.value = state.tgPosIdx;
  }
  const current = rows[state.tgPosIdx];
  const tipo = current.tipo ? String(current.tipo).replace("brasileirao_", "").replace("brasileirao", "") : "";
  if (label) label.textContent = `${current.temporada}${tipo && tipo !== "serie_a" ? " " + tipo : ""}`;
  const counts = {};
  rows.slice(0, state.tgPosIdx + 1).forEach(r => counts[r.pos] = (counts[r.pos] || 0) + 1);
  const positions = Object.keys(counts).map(Number).sort((a,b)=>b-a);
  const labels = positions.map(p => `${p}º`);
  const values = positions.map(p => counts[p]);
  Plotly.react("ch-tg-pos-race", [{
    type:"bar", orientation:"h",
    y: labels, x: values,
    marker:{color: positions.map(p => p === 1 ? c.champ : p === 2 ? c.accent2 : p === 3 ? c.accent3 : p <= 6 ? c.accent : c.muted), line:{color:c.text,width:0.7}},
    text: values,
    textposition:"outside",
    hovertemplate:"%{y}<br>%{x} vez(es)<extra></extra>"
  }], plotLayout({
    margin:{l:80,r:50,t:20,b:45},
    xaxis:{title:"Quantidade acumulada",gridcolor:c.grid,dtick:1,range:[0, Math.max(1, ...values) + 0.8]},
    yaxis:{title:"Posição final",gridcolor:c.grid},
    showlegend:false
  }), PCFG);
}

function renderTimesGeral() {
  const c = getThemeColors();
  const arr = _agregarClubes();
  setupTGPosControls();

  // KPIs
  const totalClubes = arr.length;
  const totalTemp = DATA.temporadas.length;
  const maisPart = [...arr].sort((a,b) => b.part - a.part)[0];
  const maisPts  = [...arr].sort((a,b) => b.pts - a.pts)[0];
  const maisTit  = [...arr].sort((a,b) => b.titulos - a.titulos)[0];
  const maisRebs = [...arr].sort((a,b) => b.rebs - a.rebs)[0];

  const fmt = new Intl.NumberFormat("pt-BR");
  document.getElementById("kpis-times-geral").innerHTML = `
    <div class="kpi"><div class="v">${totalClubes}</div><div class="l">Clubes na Série A</div></div>
    <div class="kpi"><div class="v">${totalTemp}</div><div class="l">Temporadas (${DATA.temporadas[0]}–${DATA.temporadas[totalTemp-1]})</div></div>
    <div class="kpi"><div class="v small">${maisPart?maisPart.clube:"—"}</div><div class="l">Mais participações (${maisPart?maisPart.part:0})</div></div>
    <div class="kpi"><div class="v small">${maisPts?maisPts.clube:"—"}</div><div class="l">Mais pontos (${maisPts?fmt.format(maisPts.pts):0})</div></div>
    <div class="kpi"><div class="v small">${maisTit && maisTit.titulos > 0 ? maisTit.clube : "—"}</div><div class="l">Mais títulos (${maisTit?maisTit.titulos:0})</div></div>
    <div class="kpi"><div class="v small">${maisRebs && maisRebs.rebs > 0 ? maisRebs.clube : "—"}</div><div class="l">Mais rebaixados (${maisRebs?maisRebs.rebs:0})</div></div>
  `;
  renderTGPosRace();

  // Top 15 pontos
  const topPts = [...arr].sort((a,b) => b.pts - a.pts).slice(0, 15);
  Plotly.react("ch-tg-pts", [{
    type:"bar", orientation:"h",
    x: topPts.map(r=>r.pts).reverse(),
    y: topPts.map(r=>r.clube).reverse(),
    marker:{color: c.accent},
    text: topPts.map(r=>fmt.format(r.pts)).reverse(),
    textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x:,} pontos<extra></extra>"
  }], plotLayout({margin:{l:130,r:50,t:10,b:30}}), PCFG);

  // Top 15 participações
  const topPart = [...arr].sort((a,b) => b.part - a.part || b.pts - a.pts).slice(0, 15);
  Plotly.react("ch-tg-part", [{
    type:"bar", orientation:"h",
    x: topPart.map(r=>r.part).reverse(),
    y: topPart.map(r=>r.clube).reverse(),
    marker:{color: c.accent2},
    text: topPart.map(r=>r.part+"/"+totalTemp).reverse(),
    textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} temporadas<extra></extra>"
  }], plotLayout({margin:{l:130,r:60,t:10,b:30}}), PCFG);

  // Títulos
  const comTit = arr.filter(r => r.titulos > 0).sort((a,b) => b.titulos - a.titulos);
  Plotly.react("ch-tg-titulos", [{
    type:"bar",
    x: comTit.map(r=>r.clube), y: comTit.map(r=>r.titulos),
    marker:{color: c.warn},
    text: comTit.map(r=>r.titulos), textposition:"outside",
    hovertemplate:"<b>%{x}</b><br>%{y} título(s)<extra></extra>"
  }], plotLayout({xaxis:{tickangle:-30,gridcolor:c.grid},yaxis:{gridcolor:c.grid,dtick:1}}), PCFG);

  // Rebaixamentos
  const comReb = arr.filter(r => r.rebs > 0).sort((a,b) => b.rebs - a.rebs).slice(0, 20);
  Plotly.react("ch-tg-rebs", [{
    type:"bar",
    x: comReb.map(r=>r.clube), y: comReb.map(r=>r.rebs),
    marker:{color: c.danger},
    text: comReb.map(r=>r.rebs), textposition:"outside",
    hovertemplate:"<b>%{x}</b><br>%{y} rebaixamento(s)<extra></extra>"
  }], plotLayout({xaxis:{tickangle:-30,gridcolor:c.grid},yaxis:{gridcolor:c.grid,dtick:1}}), PCFG);

  // Scatter regularidade: temporadas × pts médios
  Plotly.react("ch-tg-scatter", [{
    type:"scatter", mode:"markers+text",
    x: arr.map(r=>r.part),
    y: arr.map(r=>+r.ptsMed.toFixed(1)),
    text: arr.map(r=>r.clube),
    textposition:"top center", textfont:{size:9},
    marker:{
      size: arr.map(r=> Math.max(6, Math.min(28, 6 + r.titulos * 4))),
      color: arr.map(r=>r.titulos),
      colorscale: [[0, c.muted], [0.5, c.accent2], [1, c.warn]],
      showscale: true, colorbar:{title:"Títulos"},
      line:{color: c.text, width: 0.5}
    },
    hovertemplate: "<b>%{text}</b><br>%{x} temporadas · %{y} pts/temp<extra></extra>"
  }], plotLayout({
    xaxis:{title:"Temporadas disputadas", gridcolor:c.grid, dtick:2},
    yaxis:{title:"Pontos médios por temporada", gridcolor:c.grid}
  }), PCFG);

  // Tabela completa sortable
  const cols = [
    ["clube",   "Clube",    false],
    ["part",    "Temp",     true],
    ["tempIni", "1ª",       true],
    ["tempFim", "Última",   true],
    ["titulos", "🏆 Tít",   true],
    ["g6",      "G6",       true],
    ["rebs",    "↓ Reb",    true],
    ["pts",     "Pts",      true],
    ["j",       "J",        true],
    ["v",       "V",        true],
    ["e",       "E",        true],
    ["d",       "D",        true],
    ["gp",      "GP",       true],
    ["gc",      "GC",       true],
    ["sg",      "SG",       true],
    ["aprMed",  "Aprov%",   true],
    ["ptsMed",  "Pts/temp", true],
    ["melhor",  "Melhor",   true],
    ["pior",    "Pior",     true],
    ["posMed",  "Pos méd",  true],
  ];
  const dir = _tgState.sortDir === "asc" ? 1 : -1;
  arr.sort((a,b) => {
    const A = a[_tgState.sortCol], B = b[_tgState.sortCol];
    if (typeof A === "number") return (A - B) * dir;
    return String(A).localeCompare(String(B)) * dir;
  });
  const head = "<thead><tr>" + cols.map(([k,l,n]) => {
    const cls = (n?"num ":"") + "sortable" + (_tgState.sortCol===k ? (_tgState.sortDir==="asc"?" sort-asc":" sort-desc") : "");
    return `<th class="${cls}" data-col="${k}">${l}</th>`;
  }).join("") + "</tr></thead>";
  const body = "<tbody>" + arr.map(r => `<tr>
    <td><b>${r.clube}</b></td>
    <td class="num">${r.part}</td>
    <td class="num">${r.tempIni}</td>
    <td class="num">${r.tempFim}</td>
    <td class="num">${r.titulos>0?'<b style="color:var(--warn)">'+r.titulos+'</b>':"—"}</td>
    <td class="num">${r.g6}</td>
    <td class="num">${r.rebs>0?'<b style="color:var(--danger)">'+r.rebs+'</b>':"—"}</td>
    <td class="num"><b>${fmt.format(r.pts)}</b></td>
    <td class="num">${fmt.format(r.j)}</td>
    <td class="num">${fmt.format(r.v)}</td>
    <td class="num">${fmt.format(r.e)}</td>
    <td class="num">${fmt.format(r.d)}</td>
    <td class="num">${fmt.format(r.gp)}</td>
    <td class="num">${fmt.format(r.gc)}</td>
    <td class="num">${r.sg>0?"+":""}${fmt.format(r.sg)}</td>
    <td class="num">${r.aprMed.toFixed(1)}</td>
    <td class="num">${r.ptsMed.toFixed(1)}</td>
    <td class="num">${r.melhor}º</td>
    <td class="num">${r.pior}º</td>
    <td class="num">${r.posMed.toFixed(1)}</td>
  </tr>`).join("") + "</tbody>";
  const tbl = document.getElementById("tbl-times-geral");
  tbl.innerHTML = head + body;
  tbl.querySelectorAll("th[data-col]").forEach(th => {
    th.onclick = () => {
      const k = th.dataset.col;
      if (_tgState.sortCol === k) _tgState.sortDir = _tgState.sortDir === "asc" ? "desc" : "asc";
      else { _tgState.sortCol = k; _tgState.sortDir = "desc"; }
      renderTimesGeral();
    };
  });
}

function renderConfronto() {
  popularSelectsCf();
  const c = getThemeColors();
  const A = document.getElementById("cf-a").value;
  const B = document.getElementById("cf-b").value;
  const tMin = +document.getElementById("cf-min").value;
  const tMax = +document.getElementById("cf-max").value;
  const tempsJanela = DATA.temporadas.filter(t => t >= tMin && t <= tMax);

  // Carreira histórica de cada um (snapshot final por temporada)
  function carreira(clube) {
    return tempsJanela.map(t => {
      const ult = Math.max(...DATA.class_rodada.filter(r => r.temporada === t).map(r => r.rodada));
      const r = DATA.class_rodada.find(r => r.temporada === t && r.rodada === ult && r.clube === clube);
      return r ? {temp:t, ...r} : null;
    }).filter(Boolean);
  }
  const cA = carreira(A), cB = carreira(B);

  // Confrontos diretos na janela
  const h2h = DATA.matches.filter(m =>
    m.temporada >= tMin && m.temporada <= tMax &&
    ((m.mandante === A && m.visitante === B) || (m.mandante === B && m.visitante === A))
  ).sort((a,b)=> a.temporada - b.temporada || a.rodada - b.rodada);

  let vA=0, vB=0, e=0, gA_=0, gB_=0, maiorA=null, maiorB=null;
  h2h.forEach(m => {
    const aIsHome = m.mandante === A;
    const myG = aIsHome ? m.gm : m.gv;
    const oppG = aIsHome ? m.gv : m.gm;
    gA_ += myG; gB_ += oppG;
    if (myG > oppG) {
      vA++;
      const dif = myG - oppG;
      if (!maiorA || dif > maiorA.dif) maiorA = {dif, m, gA:myG, gB:oppG};
    }
    else if (oppG > myG) {
      vB++;
      const dif = oppG - myG;
      if (!maiorB || dif > maiorB.dif) maiorB = {dif, m, gA:myG, gB:oppG};
    }
    else e++;
  });

  // Sumários carreira
  function sumCarreira(arr) {
    return {
      part: arr.length,
      titulos: arr.filter(r => r.pos === 1).length,
      g6: arr.filter(r => r.pos <= 6).length,
      reb: arr.filter(r => r.pos >= 17).length,
      mediaPos: arr.length ? arr.reduce((s,r)=>s+r.pos,0)/arr.length : 0,
      mediaPts: arr.length ? arr.reduce((s,r)=>s+r.p,0)/arr.length : 0,
      melhorPos: arr.length ? Math.min(...arr.map(r=>r.pos)) : null,
      piorPos: arr.length ? Math.max(...arr.map(r=>r.pos)) : null,
      gpTotal: arr.reduce((s,r)=>s+r.gp,0),
      gcTotal: arr.reduce((s,r)=>s+r.gc,0),
    };
  }
  const sA = sumCarreira(cA), sB = sumCarreira(cB);

  document.getElementById("kpis-cf").innerHTML = `
    <div class="kpi"><div class="v">${h2h.length}</div><div class="l">Confrontos diretos</div></div>
    <div class="kpi"><div class="v" style="color:var(--accent)">${vA}</div><div class="l">Vitórias ${A}</div></div>
    <div class="kpi"><div class="v" style="color:var(--muted)">${e}</div><div class="l">Empates</div></div>
    <div class="kpi"><div class="v" style="color:var(--accent2)">${vB}</div><div class="l">Vitórias ${B}</div></div>
    <div class="kpi"><div class="v">${gA_} × ${gB_}</div><div class="l">Gols no confronto</div></div>
    <div class="kpi"><div class="v">${sA.titulos} × ${sB.titulos}</div><div class="l">Títulos na janela</div></div>
  `;

  // Tabela resumo da janela
  document.getElementById("tbl-cf-resumo").innerHTML = `<thead><tr>
    <th>Métrica</th><th class="num">${A}</th><th class="num">${B}</th>
  </tr></thead><tbody>
    <tr><td>Participações</td><td class="num">${sA.part}</td><td class="num">${sB.part}</td></tr>
    <tr><td>Títulos</td><td class="num">${sA.titulos}</td><td class="num">${sB.titulos}</td></tr>
    <tr><td>Top 6</td><td class="num">${sA.g6}</td><td class="num">${sB.g6}</td></tr>
    <tr><td>Rebaixamentos</td><td class="num">${sA.reb}</td><td class="num">${sB.reb}</td></tr>
    <tr><td>Melhor posição</td><td class="num">${sA.melhorPos ?? "—"}</td><td class="num">${sB.melhorPos ?? "—"}</td></tr>
    <tr><td>Pior posição</td><td class="num">${sA.piorPos ?? "—"}</td><td class="num">${sB.piorPos ?? "—"}</td></tr>
    <tr><td>Posição média</td><td class="num">${sA.mediaPos.toFixed(1)}</td><td class="num">${sB.mediaPos.toFixed(1)}</td></tr>
    <tr><td>Pontos médios</td><td class="num">${sA.mediaPts.toFixed(1)}</td><td class="num">${sB.mediaPts.toFixed(1)}</td></tr>
    <tr><td>Gols pró totais</td><td class="num">${sA.gpTotal}</td><td class="num">${sB.gpTotal}</td></tr>
    <tr><td>Gols sofridos totais</td><td class="num">${sA.gcTotal}</td><td class="num">${sB.gcTotal}</td></tr>
    <tr><td colspan="3" style="background:var(--panel2);font-weight:700">Confrontos diretos</td></tr>
    <tr><td>Vitórias</td><td class="num"><b>${vA}</b></td><td class="num"><b>${vB}</b></td></tr>
    <tr><td>Empates</td><td class="num" colspan="2" style="text-align:center"><b>${e}</b></td></tr>
    <tr><td>Gols</td><td class="num">${gA_}</td><td class="num">${gB_}</td></tr>
    <tr><td>Maior goleada</td>
      <td class="num">${maiorA ? `${maiorA.gA}×${maiorA.gB} (${maiorA.m.temporada})` : "—"}</td>
      <td class="num">${maiorB ? `${maiorB.gA}×${maiorB.gB} (${maiorB.m.temporada})` : "—"}</td>
    </tr>
  </tbody>`;

  // Posição por temporada
  const posA = tempsJanela.map(t => {const r = cA.find(x=>x.temp===t); return r?r.pos:null;});
  const posB = tempsJanela.map(t => {const r = cB.find(x=>x.temp===t); return r?r.pos:null;});
  Plotly.react("ch-cf-pos", [
    {type:"scatter",mode:"lines+markers",x:tempsJanela,y:posA,name:A,line:{color:c.accent,width:2.5},marker:{size:8}},
    {type:"scatter",mode:"lines+markers",x:tempsJanela,y:posB,name:B,line:{color:c.accent2,width:2.5},marker:{size:8}},
  ], plotLayout({xaxis:{tickmode:"linear",gridcolor:c.grid},yaxis:{title:"Posição",gridcolor:c.grid,autorange:"reversed",dtick:1},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  // Pts por temp
  const ptsA = tempsJanela.map(t => {const r = cA.find(x=>x.temp===t); return r?r.p:null;});
  const ptsB = tempsJanela.map(t => {const r = cB.find(x=>x.temp===t); return r?r.p:null;});
  Plotly.react("ch-cf-pts", [
    {type:"bar",x:tempsJanela,y:ptsA,name:A,marker:{color:c.accent}},
    {type:"bar",x:tempsJanela,y:ptsB,name:B,marker:{color:c.accent2}},
  ], plotLayout({barmode:"group",xaxis:{tickmode:"linear",gridcolor:c.grid},yaxis:{title:"Pontos",gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  // SG por temp
  const sgA = tempsJanela.map(t => {const r = cA.find(x=>x.temp===t); return r?r.sg:null;});
  const sgB = tempsJanela.map(t => {const r = cB.find(x=>x.temp===t); return r?r.sg:null;});
  Plotly.react("ch-cf-sg", [
    {type:"bar",x:tempsJanela,y:sgA,name:A,marker:{color:c.accent}},
    {type:"bar",x:tempsJanela,y:sgB,name:B,marker:{color:c.accent2}},
  ], plotLayout({barmode:"group",xaxis:{tickmode:"linear",gridcolor:c.grid},yaxis:{title:"Saldo",gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  // Tabela de jogos do confronto
  document.getElementById("tbl-cf-jogos").innerHTML = `<thead><tr>
    <th class="num">Temp</th><th class="num">Rod</th><th>Data</th>
    <th>Mandante</th><th class="num">Placar</th><th>Visitante</th>
    <th>Resultado</th><th>Arena</th>
  </tr></thead><tbody>` + h2h.map(m => {
    let res;
    if (m.gm > m.gv) res = `<span class="tag tag-V">${m.mandante}</span>`;
    else if (m.gv > m.gm) res = `<span class="tag tag-V">${m.visitante}</span>`;
    else res = `<span class="tag tag-E">Empate</span>`;
    return `<tr>
      <td class="num">${m.temporada}</td><td class="num">${m.rodada}</td><td>${m.data}</td>
      <td><b>${m.mandante}</b></td>
      <td class="num"><b>${m.gm} × ${m.gv}</b></td>
      <td><b>${m.visitante}</b></td>
      <td>${res}</td><td>${m.arena||"—"}</td>
    </tr>`;
  }).join("") + "</tbody>";
}

// =====================================================================
// TÉCNICOS
// =====================================================================
function renderTecnicos() {
  // Para cada (técnico, clube), agrega: jogos, V, E, D, gp, gc, pontos
  const map = {};  // key = tecnico|clube
  DATA.matches.forEach(m => {
    [["mandante", "tec_m", "M"], ["visitante", "tec_v", "V"]].forEach(([clubeKey, tecKey, lado]) => {
      const tec = m[tecKey]; if (!tec) return;
      const clube = m[clubeKey];
      const k = tec + "|" + clube;
      if (!map[k]) map[k] = {tec, clube, j:0, v:0, e:0, d:0, gp:0, gc:0, p:0, primeiraTemp: m.temporada, ultimaTemp: m.temporada};
      const r = map[k];
      r.j++;
      const my = lado==="M" ? m.gm : m.gv;
      const op = lado==="M" ? m.gv : m.gm;
      r.gp += my; r.gc += op;
      if (my > op) { r.v++; r.p += 3; }
      else if (op > my) { r.d++; }
      else { r.e++; r.p += 1; }
      if (m.temporada < r.primeiraTemp) r.primeiraTemp = m.temporada;
      if (m.temporada > r.ultimaTemp) r.ultimaTemp = m.temporada;
    });
  });
  const allTec = Object.values(map);
  // Total por técnico (agregado entre clubes)
  const porTec = {};
  allTec.forEach(r => {
    if (!porTec[r.tec]) porTec[r.tec] = {tec:r.tec, clubes:new Set(), j:0,v:0,e:0,d:0,p:0,gp:0,gc:0};
    const t = porTec[r.tec];
    t.clubes.add(r.clube); t.j+=r.j; t.v+=r.v; t.e+=r.e; t.d+=r.d; t.p+=r.p; t.gp+=r.gp; t.gc+=r.gc;
  });
  const totaisTec = Object.values(porTec).map(t => ({...t, clubes:t.clubes.size, apr: t.j ? +(t.p/(t.j*3)*100).toFixed(1) : 0}));

  // KPIs
  const totalTec = totaisTec.length;
  const totalJogos = DATA.matches.length;
  const tecMaisJogos = [...totaisTec].sort((a,b)=>b.j-a.j)[0];
  const tecMaiorAprov = [...totaisTec].filter(t=>t.j>=30).sort((a,b)=>b.apr-a.apr)[0];
  document.getElementById("kpis-tec").innerHTML = `
    <div class="kpi"><div class="v">${totalTec}</div><div class="l">Técnicos distintos</div></div>
    <div class="kpi"><div class="v">${totalJogos*2}</div><div class="l">Comandos (M+V)</div></div>
    <div class="kpi"><div class="v small">${tecMaisJogos?tecMaisJogos.tec:"—"}</div><div class="l">Mais jogos (${tecMaisJogos?tecMaisJogos.j:0})</div></div>
    <div class="kpi"><div class="v small">${tecMaiorAprov?tecMaiorAprov.tec:"—"}</div><div class="l">Maior aprov. ≥30j (${tecMaiorAprov?tecMaiorAprov.apr.toFixed(1):0}%)</div></div>
    <div class="kpi"><div class="v">${(totaisTec.reduce((s,t)=>s+t.clubes,0)/totalTec).toFixed(1)}</div><div class="l">Média clubes/técnico</div></div>
  `;

  // Técnicos campeões: pra cada temporada, o técnico do campeão na última rodada
  const campeoes = [];
  DATA.temporadas.forEach(t => {
    const ult = Math.max(...DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada));
    const camp = DATA.class_rodada.find(r=>r.temporada===t && r.rodada===ult && r.pos===1);
    if (!camp) return;
    // técnico que comandou a última partida do campeão
    const ultGameClube = DATA.matches.filter(m => m.temporada===t && (m.mandante===camp.clube || m.visitante===camp.clube))
      .sort((a,b)=> b.rodada - a.rodada || b.data_iso.localeCompare(a.data_iso))[0];
    if (!ultGameClube) return;
    const tec = ultGameClube.mandante === camp.clube ? ultGameClube.tec_m : ultGameClube.tec_v;
    // total de jogos comandados na temporada
    const jogosTemp = DATA.matches.filter(m => m.temporada===t && (
      (m.mandante===camp.clube && m.tec_m===tec) || (m.visitante===camp.clube && m.tec_v===tec)
    )).length;
    campeoes.push({temp:t, clube:camp.clube, tec: tec||"—", pts:camp.p, jogosTemp});
  });
  document.getElementById("tbl-tec-camp").innerHTML = `<thead><tr>
    <th>Temp</th><th>Clube campeão</th><th>Técnico (final)</th><th class="num">Pts</th><th class="num">Jogos comandados</th>
  </tr></thead><tbody>` + campeoes.map(r=>`<tr>
    <td><b>${r.temp}</b></td><td>${r.clube}</td><td><b>${r.tec}</b></td>
    <td class="num">${r.pts}</td><td class="num">${r.jogosTemp}</td>
  </tr>`).join("") + "</tbody>";

  // Top jogos
  const topJogos = [...totaisTec].sort((a,b)=>b.j-a.j).slice(0,15);
  document.getElementById("tbl-tec-jogos").innerHTML = `<thead><tr>
    <th>#</th><th>Técnico</th><th class="num">Clubes</th><th class="num">J</th><th class="num">V</th><th class="num">E</th><th class="num">D</th><th class="num">APR%</th>
  </tr></thead><tbody>` + topJogos.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.tec}</b></td><td class="num">${r.clubes}</td>
    <td class="num">${r.j}</td><td class="num">${r.v}</td><td class="num">${r.e}</td><td class="num">${r.d}</td>
    <td class="num">${r.apr.toFixed(1)}</td>
  </tr>`).join("") + "</tbody>";

  // Top aproveitamento (mín 30 jogos)
  const topApr = [...totaisTec].filter(t => t.j >= 30).sort((a,b)=>b.apr-a.apr).slice(0,15);
  document.getElementById("tbl-tec-aprov").innerHTML = `<thead><tr>
    <th>#</th><th>Técnico</th><th class="num">J</th><th class="num">V-E-D</th><th class="num">APR%</th><th class="num">SG</th>
  </tr></thead><tbody>` + topApr.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.tec}</b></td><td class="num">${r.j}</td>
    <td class="num">${r.v}-${r.e}-${r.d}</td><td class="num"><b>${r.apr.toFixed(1)}</b></td>
    <td class="num">${(r.gp-r.gc>0?"+":"")+(r.gp-r.gc)}</td>
  </tr>`).join("") + "</tbody>";

  // Trocas de técnico em uma temporada (por clube/temp)
  const trocas = {};  // key = clube|temp -> set de técnicos
  DATA.matches.forEach(m => {
    [["mandante","tec_m"],["visitante","tec_v"]].forEach(([ck,tk]) => {
      if (!m[tk]) return;
      const k = m[ck] + "|" + m.temporada;
      if (!trocas[k]) trocas[k] = new Set();
      trocas[k].add(m[tk]);
    });
  });
  const trocasArr = Object.entries(trocas).map(([k,s]) => {
    const [clube, temp] = k.split("|");
    return {clube, temp:+temp, n: s.size, tecs: [...s]};
  }).sort((a,b)=>b.n-a.n).slice(0,15);
  document.getElementById("tbl-tec-trocas").innerHTML = `<thead><tr>
    <th>#</th><th>Clube</th><th class="num">Temp</th><th class="num">Téc. distintos</th><th>Lista</th>
  </tr></thead><tbody>` + trocasArr.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.clube}</b></td><td class="num">${r.temp}</td>
    <td class="num"><b>${r.n}</b></td><td style="font-size:11px;color:var(--muted)">${r.tecs.join(", ")}</td>
  </tr>`).join("") + "</tbody>";

  // Impacto da troca: para cada (clube, temp) com 2+ técnicos, comparar APR de cada técnico no clube
  const impactos = [];
  Object.entries(trocas).forEach(([k, s]) => {
    if (s.size < 2) return;
    const [clube, tempStr] = k.split("|");
    const temp = +tempStr;
    const ms = DATA.matches.filter(m => m.temporada === temp && (m.mandante === clube || m.visitante === clube))
      .sort((a,b)=> a.rodada - b.rodada || a.data_iso.localeCompare(b.data_iso));
    // identifica em ordem cronológica os técnicos
    const sequencias = [];  // {tec, jogos:[]}
    let cur = null;
    ms.forEach(m => {
      const tec = m.mandante === clube ? m.tec_m : m.tec_v;
      if (!tec) return;
      if (!cur || cur.tec !== tec) {
        cur = {tec, jogos:[]};
        sequencias.push(cur);
      }
      const my = m.mandante === clube ? m.gm : m.gv;
      const op = m.mandante === clube ? m.gv : m.gm;
      const pts = my > op ? 3 : (my === op ? 1 : 0);
      cur.jogos.push({m, pts});
    });
    if (sequencias.length < 2) return;
    // Para cada par consecutivo: comparar APR
    for (let i = 1; i < sequencias.length; i++) {
      const ant = sequencias[i-1];
      const novo = sequencias[i];
      if (ant.jogos.length < 3 || novo.jogos.length < 3) continue;
      const aprAnt = ant.jogos.reduce((s,x)=>s+x.pts,0) / (ant.jogos.length*3) * 100;
      const aprNovo = novo.jogos.reduce((s,x)=>s+x.pts,0) / (novo.jogos.length*3) * 100;
      impactos.push({
        clube, temp, ant: ant.tec, novo: novo.tec,
        jAnt: ant.jogos.length, jNovo: novo.jogos.length,
        aprAnt: aprAnt, aprNovo: aprNovo, delta: aprNovo - aprAnt,
      });
    }
  });
  impactos.sort((a,b)=> b.delta - a.delta);
  // Top 10 melhores e 10 piores impactos
  const topPos = impactos.slice(0, 10);
  const topNeg = impactos.slice(-10).reverse();
  document.getElementById("tbl-tec-impacto").innerHTML = `<thead><tr>
    <th class="num">Temp</th><th>Clube</th><th>Téc. anterior</th><th class="num">J ant</th><th class="num">APR ant</th>
    <th>Téc. novo</th><th class="num">J novo</th><th class="num">APR novo</th><th class="num">Δ APR</th>
  </tr></thead><tbody>
    <tr><td colspan="9" style="background:rgba(74,222,128,.12);font-weight:700;color:var(--accent)">🚀 Maiores ganhos com a troca</td></tr>
    ${topPos.map(r=>`<tr>
      <td class="num">${r.temp}</td><td><b>${r.clube}</b></td>
      <td>${r.ant}</td><td class="num">${r.jAnt}</td><td class="num">${r.aprAnt.toFixed(1)}</td>
      <td><b>${r.novo}</b></td><td class="num">${r.jNovo}</td><td class="num"><b>${r.aprNovo.toFixed(1)}</b></td>
      <td class="num" style="color:var(--accent)"><b>+${r.delta.toFixed(1)}</b></td>
    </tr>`).join("")}
    <tr><td colspan="9" style="background:rgba(248,113,113,.12);font-weight:700;color:var(--danger)">📉 Maiores quedas com a troca</td></tr>
    ${topNeg.map(r=>`<tr>
      <td class="num">${r.temp}</td><td><b>${r.clube}</b></td>
      <td>${r.ant}</td><td class="num">${r.jAnt}</td><td class="num">${r.aprAnt.toFixed(1)}</td>
      <td><b>${r.novo}</b></td><td class="num">${r.jNovo}</td><td class="num"><b>${r.aprNovo.toFixed(1)}</b></td>
      <td class="num" style="color:var(--danger)"><b>${r.delta.toFixed(1)}</b></td>
    </tr>`).join("")}
  </tbody>`;
}

// =====================================================================
// GEOGRAFIA
// =====================================================================
function renderGeografia() {
  const c = getThemeColors();
  // Dados-base: snapshots finais por temporada
  const tempsAll = DATA.temporadas;
  // Últimas rodadas
  const ultRod = {};
  tempsAll.forEach(t => {
    ultRod[t] = Math.max(...DATA.class_rodada.filter(r=>r.temporada===t).map(r=>r.rodada));
  });
  const finais = DATA.class_rodada.filter(r => r.rodada === ultRod[r.temporada]);

  // Mapa clube -> UF (mais comum de aparecer como mandante)
  const ufClube = {};
  DATA.matches.forEach(m => {
    if (m.uf_m) {
      if (!ufClube[m.mandante]) ufClube[m.mandante] = {};
      ufClube[m.mandante][m.uf_m] = (ufClube[m.mandante][m.uf_m] || 0) + 1;
    }
  });
  const clubeUF = {};
  Object.entries(ufClube).forEach(([cl, ufs]) => {
    clubeUF[cl] = Object.entries(ufs).sort((a,b)=>b[1]-a[1])[0][0];
  });

  // Participações por UF
  const part = {};
  finais.forEach(r => {
    const uf = clubeUF[r.clube] || "??";
    part[uf] = (part[uf] || 0) + 1;
  });
  // Títulos
  const tit = {};
  finais.filter(r=>r.pos===1).forEach(r => {
    const uf = clubeUF[r.clube] || "??";
    tit[uf] = (tit[uf] || 0) + 1;
  });
  // Rebaixamentos
  const reb = {};
  finais.filter(r=>r.pos>=17).forEach(r => {
    const uf = clubeUF[r.clube] || "??";
    reb[uf] = (reb[uf] || 0) + 1;
  });
  // Pontos médios
  const ptsByUF = {};
  finais.forEach(r => {
    const uf = clubeUF[r.clube] || "??";
    if (!ptsByUF[uf]) ptsByUF[uf] = {soma:0, n:0};
    ptsByUF[uf].soma += r.p; ptsByUF[uf].n++;
  });
  const mediaUF = Object.entries(ptsByUF).map(([uf,v])=>({uf, media:v.soma/v.n, n:v.n})).sort((a,b)=>b.media-a.media);

  // Jogos entre clubes da mesma UF e de UFs diferentes
  const sameUF = DATA.matches.filter(m => m.uf_m && m.uf_v && m.uf_m === m.uf_v);
  const diffUF = DATA.matches.filter(m => m.uf_m && m.uf_v && m.uf_m !== m.uf_v);
  const pct = (num, den) => den ? (num / den * 100).toFixed(1) : "0.0";

  document.getElementById("kpis-geo").innerHTML = `
    <div class="kpi"><div class="v">${Object.keys(part).length}</div><div class="l">UFs com clubes</div></div>
    <div class="kpi"><div class="v">${Object.entries(tit).sort((a,b)=>b[1]-a[1])[0]?.[0] || "—"}</div><div class="l">UF mais campeã (${Object.values(tit).sort((a,b)=>b-a)[0]||0})</div></div>
    <div class="kpi"><div class="v">${sameUF.length}</div><div class="l">Jogos mesma UF</div></div>
    <div class="kpi"><div class="v">${diffUF.length}</div><div class="l">Jogos UFs diferentes</div></div>
    <div class="kpi"><div class="v">${pct(sameUF.filter(m=>m.gm>m.gv).length, sameUF.length)}%</div><div class="l">Vitórias mandante mesma UF</div></div>
    <div class="kpi"><div class="v">${pct(diffUF.filter(m=>m.gm>m.gv).length, diffUF.length)}%</div><div class="l">Vitórias mandante UFs diferentes</div></div>
  `;

  function bar(div, obj, color, title) {
    const arr = Object.entries(obj).sort((a,b)=>b[1]-a[1]);
    Plotly.react(div, [{
      type:"bar",x:arr.map(r=>r[0]),y:arr.map(r=>r[1]),
      marker:{color},text:arr.map(r=>r[1]),textposition:"outside",
      hovertemplate:"<b>%{x}</b><br>%{y}<extra></extra>"
    }], plotLayout({xaxis:{gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
  }
  bar("ch-geo-part", part, c.accent2);
  bar("ch-geo-tit",  tit,  c.warn);
  bar("ch-geo-reb",  reb,  c.danger);

  Plotly.react("ch-geo-pts", [{
    type:"bar",x:mediaUF.map(r=>r.uf),y:mediaUF.map(r=>+r.media.toFixed(1)),
    marker:{color:c.accent},text:mediaUF.map(r=>r.media.toFixed(1)),textposition:"outside",
    hovertemplate:"<b>%{x}</b><br>%{y} pts médios (%{customdata} clube-temps)<extra></extra>",
    customdata: mediaUF.map(r=>r.n),
  }], plotLayout({xaxis:{gridcolor:c.grid},yaxis:{title:"Pts médios",gridcolor:c.grid}}), PCFG);

  // UFs com mais jogos entre clubes do mesmo estado
  const clNumByUF = {};
  sameUF.forEach(m => {
    const uf = m.uf_m;
    clNumByUF[uf] = clNumByUF[uf] || {uf, jogos:0, vMand:0, emp:0, vVis:0, gols:0};
    clNumByUF[uf].jogos++;
    clNumByUF[uf].gols += m.gm + m.gv;
    if (m.gm > m.gv) clNumByUF[uf].vMand++;
    else if (m.gv > m.gm) clNumByUF[uf].vVis++;
    else clNumByUF[uf].emp++;
  });
  const clArr = Object.values(clNumByUF).sort((a,b)=>b.jogos-a.jogos);
  document.getElementById("tbl-geo-class").innerHTML = `<thead><tr>
    <th>UF</th><th class="num">Jogos</th><th class="num">V Mand.</th><th class="num">Emp</th><th class="num">V Vis.</th>
    <th class="num">Gols</th><th class="num">Gols/jogo</th><th class="num">% V Mand.</th>
  </tr></thead><tbody>` + clArr.map(r=>`<tr>
    <td><b>${r.uf}</b></td><td class="num">${r.jogos}</td>
    <td class="num">${r.vMand}</td><td class="num">${r.emp}</td><td class="num">${r.vVis}</td>
    <td class="num">${r.gols}</td><td class="num">${(r.gols/r.jogos).toFixed(2)}</td>
    <td class="num">${(r.vMand/r.jogos*100).toFixed(1)}%</td>
  </tr>`).join("") + "</tbody>";

  // Vantagem mandante: mesma UF x UFs diferentes
  const vSame = sameUF.length ? sameUF.filter(m=>m.gm>m.gv).length / sameUF.length : 0;
  const vDiff = diffUF.length ? diffUF.filter(m=>m.gm>m.gv).length / diffUF.length : 0;
  const eSame = sameUF.length ? sameUF.filter(m=>m.gm===m.gv).length / sameUF.length : 0;
  const eDiff = diffUF.length ? diffUF.filter(m=>m.gm===m.gv).length / diffUF.length : 0;
  const lSame = sameUF.length ? sameUF.filter(m=>m.gv>m.gm).length / sameUF.length : 0;
  const lDiff = diffUF.length ? diffUF.filter(m=>m.gv>m.gm).length / diffUF.length : 0;
  Plotly.react("ch-geo-mando", [
    {type:"bar",x:["Mesma UF","UFs diferentes"],y:[vSame*100,vDiff*100].map(v=>+v.toFixed(1)),name:"V Mand %",marker:{color:c.accent}},
    {type:"bar",x:["Mesma UF","UFs diferentes"],y:[eSame*100,eDiff*100].map(v=>+v.toFixed(1)),name:"Empate %",marker:{color:c.muted}},
    {type:"bar",x:["Mesma UF","UFs diferentes"],y:[lSame*100,lDiff*100].map(v=>+v.toFixed(1)),name:"V Vis %",marker:{color:c.danger}},
  ], plotLayout({barmode:"group",xaxis:{gridcolor:c.grid},yaxis:{title:"%",gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);

  // Distribuição jogos por UF mandante
  const jogosUF = {};
  DATA.matches.forEach(m => { if (m.uf_m) jogosUF[m.uf_m] = (jogosUF[m.uf_m]||0) + 1; });
  bar("ch-geo-jogos", jogosUF, c.purple);
}

// =====================================================================
// HELPERS para classificação por rodada (consume class_rodada do payload)
// =====================================================================
function snapsTemp(t) { return DATA.class_rodada.filter(r => r.temporada === t); }
function snapsTempRod(t, rod) { return DATA.class_rodada.filter(r => r.temporada === t && r.rodada === rod); }
function rodadasTemp(t) {
  const set = new Set(DATA.class_rodada.filter(r => r.temporada === t).map(r => r.rodada));
  return [...set].sort((a,b) => a - b);
}

// ---- CAMPEONATO (corrida título / Z4 / equilíbrio / fases) ----
function renderCampeonato({ms}) {
  const c = getThemeColors();
  const T = state.temporada;
  const rods = rodadasTemp(T);
  if (!rods.length) {
    document.getElementById("kpis-camp").innerHTML = '<div class="note">Sem dados.</div>';
    return;
  }
  const ultRod = rods[rods.length - 1];
  const tabFinal = snapsTempRod(T, ultRod).slice().sort((a,b) => a.pos - b.pos);
  const campeao = tabFinal[0];
  const vice = tabFinal[1];

  // -- Rodadas na liderança --
  const lideres = {};
  rods.forEach(r => {
    const lider = snapsTempRod(T, r).find(x => x.pos === 1);
    if (lider) lideres[lider.clube] = (lideres[lider.clube] || 0) + 1;
  });
  const lideresArr = Object.entries(lideres).map(([k,v]) => ({clube:k, n:v})).sort((a,b)=>b.n-a.n);
  const liderDom = lideresArr[0];
  // Em qual rodada o campeão assumiu a liderança "definitiva" (manteve até o fim)
  let rodAssumiu = ultRod;
  for (let i = rods.length - 1; i >= 0; i--) {
    const lid = snapsTempRod(T, rods[i]).find(x => x.pos === 1);
    if (!lid || lid.clube !== campeao.clube) { rodAssumiu = rods[i + 1] || ultRod; break; }
    if (i === 0) rodAssumiu = rods[0];
  }
  // Maior vantagem aberta pelo líder na temporada inteira
  let maiorVant = 0, rodMaiorVant = 0;
  rods.forEach(r => {
    const snap = snapsTempRod(T, r).slice().sort((a,b) => a.pos - b.pos);
    if (snap.length >= 2) {
      const dif = snap[0].p - snap[1].p;
      if (dif > maiorVant) { maiorVant = dif; rodMaiorVant = r; }
    }
  });
  // Trocas de liderança
  let trocas = 0, prev = null;
  rods.forEach(r => {
    const lid = snapsTempRod(T, r).find(x => x.pos === 1);
    if (lid && prev && lid.clube !== prev) trocas++;
    if (lid) prev = lid.clube;
  });

  document.getElementById("kpis-camp").innerHTML = `
    <div class="kpi"><div class="v small">${campeao.clube}</div><div class="l">Campeão (${campeao.p} pts)</div></div>
    <div class="kpi"><div class="v">${vice ? campeao.p - vice.p : 0}</div><div class="l">Vantagem p/ vice</div></div>
    <div class="kpi"><div class="v small">${liderDom ? liderDom.clube : "—"}</div><div class="l">Mais rodadas líder (${liderDom ? liderDom.n : 0})</div></div>
    <div class="kpi"><div class="v">${trocas}</div><div class="l">Trocas de liderança</div></div>
    <div class="kpi"><div class="v">${rodAssumiu}</div><div class="l">Rod. liderança definitiva</div></div>
    <div class="kpi"><div class="v">${maiorVant}<span style="font-size:14px;color:var(--muted)">pts (R${rodMaiorVant})</span></div><div class="l">Maior vantagem do líder</div></div>
  `;

  Plotly.react("ch-rod-lider", [{
    type:"bar", orientation:"h",
    x: lideresArr.map(r=>r.n).reverse(), y: lideresArr.map(r=>r.clube).reverse(),
    marker:{color: c.warn}, text: lideresArr.map(r=>r.n).reverse(), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} rodadas como líder<extra></extra>"
  }], plotLayout({margin:{l:120,r:30,t:10,b:30}}), PCFG);

  // Líder × vice por rodada
  const ptsLider = [], ptsVice = [];
  rods.forEach(r => {
    const snap = snapsTempRod(T, r).slice().sort((a,b)=>a.pos-b.pos);
    ptsLider.push(snap[0]?.p ?? null);
    ptsVice.push(snap[1]?.p ?? null);
  });
  Plotly.react("ch-lider-vice", [
    {type:"scatter",mode:"lines+markers",x:rods,y:ptsLider,name:"Líder",line:{color:c.warn,width:2},marker:{size:5}},
    {type:"scatter",mode:"lines+markers",x:rods,y:ptsVice,name:"Vice",line:{color:c.muted,width:2},marker:{size:5}},
  ], plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Pontos",gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);

  // Distância para o líder dos top 4 finais
  const top4 = tabFinal.slice(0, 4).map(x => x.clube);
  const palette = ["#fbbf24","#60a5fa","#4ade80","#a78bfa"];
  const tracesDist = top4.map((cl, i) => {
    const ys = rods.map(r => {
      const snap = snapsTempRod(T, r);
      const lid = snap.find(x => x.pos === 1);
      const me = snap.find(x => x.clube === cl);
      return lid && me ? lid.p - me.p : null;
    });
    return {type:"scatter",mode:"lines+markers",x:rods,y:ys,name:cl,line:{color:palette[i],width:2},marker:{size:5},
      hovertemplate:`<b>${cl}</b><br>Rod %{x}: %{y} pts atrás<extra></extra>`};
  });
  Plotly.react("ch-dist-lider", tracesDist,
    plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Pts atrás do líder",gridcolor:c.grid,autorange:"reversed"},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);

  // -- Rodadas no Z4 --
  const noZ4 = {};
  rods.forEach(r => {
    snapsTempRod(T, r).filter(x => x.pos >= 17).forEach(x => {
      noZ4[x.clube] = (noZ4[x.clube] || 0) + 1;
    });
  });
  const z4Arr = Object.entries(noZ4).map(([k,v]) => ({clube:k, n:v})).sort((a,b)=>b.n-a.n);
  Plotly.react("ch-rod-z4", [{
    type:"bar", orientation:"h",
    x: z4Arr.map(r=>r.n).reverse(), y: z4Arr.map(r=>r.clube).reverse(),
    marker:{color: c.danger}, text: z4Arr.map(r=>r.n).reverse(), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} rodadas no Z4<extra></extra>"
  }], plotLayout({margin:{l:120,r:30,t:10,b:30}}), PCFG);

  // Pontuação de corte (16º) por rodada
  const corte = rods.map(r => {
    const snap = snapsTempRod(T, r).find(x => x.pos === 16);
    return snap ? snap.p : null;
  });
  Plotly.react("ch-corte-z4", [{
    type:"scatter",mode:"lines+markers",x:rods,y:corte,
    line:{color:c.danger,width:2},marker:{size:5},fill:"tozeroy",fillcolor:c.danger+"22",
    hovertemplate:"Rod %{x}<br><b>%{y} pts</b> = corte do 16º<extra></extra>"
  }], plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Pts do 16º",gridcolor:c.grid}}), PCFG);

  // -- Equilíbrio --
  const dif12 = rods.map(r => {
    const snap = snapsTempRod(T, r).slice().sort((a,b)=>a.pos-b.pos);
    return snap[0] && snap[1] ? snap[0].p - snap[1].p : null;
  });
  const ptsArr = tabFinal.map(x => x.p);
  const mean = ptsArr.reduce((s,x)=>s+x,0) / ptsArr.length;
  const std = Math.sqrt(ptsArr.reduce((s,x)=>s+(x-mean)**2,0) / ptsArr.length);
  const range = ptsArr[0] - ptsArr[ptsArr.length-1];
  const dif14 = tabFinal[0].p - (tabFinal[3]?.p || 0);
  const dif1617 = (tabFinal[15]?.p || 0) - (tabFinal[16]?.p || 0);
  document.getElementById("kpis-equil").innerHTML = `
    <div class="kpi"><div class="v">${(campeao.p - (vice?.p || 0))}</div><div class="l">Δ 1º × 2º</div></div>
    <div class="kpi"><div class="v">${dif14}</div><div class="l">Δ 1º × 4º</div></div>
    <div class="kpi"><div class="v">${range}</div><div class="l">Δ 1º × último</div></div>
    <div class="kpi"><div class="v">${std.toFixed(1)}</div><div class="l">Desvio-padrão pts</div></div>
    <div class="kpi"><div class="v">${trocas}</div><div class="l">Trocas de liderança</div></div>
    <div class="kpi"><div class="v">${dif1617}</div><div class="l">Δ 16º × 17º (corte)</div></div>
  `;
  Plotly.react("ch-dif-12", [{
    type:"scatter",mode:"lines+markers",x:rods,y:dif12,
    line:{color:c.accent2,width:2},marker:{size:5},fill:"tozeroy",fillcolor:c.accent2+"22",
    hovertemplate:"Rod %{x}<br>Δ líder × vice: <b>%{y}</b> pts<extra></extra>"
  }], plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Diferença em pts",gridcolor:c.grid}}), PCFG);
  Plotly.react("ch-dist-pts", [{
    type:"histogram",x:ptsArr,marker:{color:c.purple},nbinsx:12,
    hovertemplate:"%{x} pts: %{y} clubes<extra></extra>"
  }], plotLayout({xaxis:{title:"Pontos finais",gridcolor:c.grid},yaxis:{title:"Nº clubes",gridcolor:c.grid}}), PCFG);

  // -- Fases --
  // 1º turno = rodadas 1..N/2 ; 2º turno = N/2+1..N ; últimas 10/5
  const half = Math.floor(ultRod / 2);
  const u10 = ultRod - 9, u5 = ultRod - 4;
  function ptsRange(rodIni, rodFim) {
    const out = {};
    ms.filter(m => m.rodada >= rodIni && m.rodada <= rodFim).forEach(m => {
      out[m.mandante] = out[m.mandante] || {clube:m.mandante, p:0, j:0, gp:0, gc:0};
      out[m.visitante] = out[m.visitante] || {clube:m.visitante, p:0, j:0, gp:0, gc:0};
      out[m.mandante].j++; out[m.visitante].j++;
      out[m.mandante].gp += m.gm; out[m.mandante].gc += m.gv;
      out[m.visitante].gp += m.gv; out[m.visitante].gc += m.gm;
      if (m.gm > m.gv) out[m.mandante].p += 3;
      else if (m.gv > m.gm) out[m.visitante].p += 3;
      else { out[m.mandante].p += 1; out[m.visitante].p += 1; }
    });
    return Object.values(out).sort((a,b) => b.p - a.p);
  }
  const t1 = ptsRange(1, half);
  const t2 = ptsRange(half + 1, ultRod);
  const lt10 = ptsRange(u10, ultRod);
  const lt5 = ptsRange(u5, ultRod);
  // Tabela campeões por fase
  document.getElementById("tbl-fases").innerHTML = `<thead><tr>
    <th>Fase</th><th>Campeão</th><th class="num">Pts</th><th class="num">Jogos</th>
  </tr></thead><tbody>
    <tr><td><b>1º turno</b> (R1-${half})</td><td>${t1[0]?.clube||"—"}</td><td class="num">${t1[0]?.p||0}</td><td class="num">${t1[0]?.j||0}</td></tr>
    <tr><td><b>2º turno</b> (R${half+1}-${ultRod})</td><td>${t2[0]?.clube||"—"}</td><td class="num">${t2[0]?.p||0}</td><td class="num">${t2[0]?.j||0}</td></tr>
    <tr><td><b>Últimas 10</b> (R${u10}-${ultRod})</td><td>${lt10[0]?.clube||"—"}</td><td class="num">${lt10[0]?.p||0}</td><td class="num">${lt10[0]?.j||0}</td></tr>
    <tr><td><b>Últimas 5</b> (R${u5}-${ultRod})</td><td>${lt5[0]?.clube||"—"}</td><td class="num">${lt5[0]?.p||0}</td><td class="num">${lt5[0]?.j||0}</td></tr>
    <tr><td><b>Geral</b></td><td><b>${campeao.clube}</b></td><td class="num"><b>${campeao.p}</b></td><td class="num">${campeao.j}</td></tr>
  </tbody>`;
  // Quem cresceu/caiu (1ºT → 2ºT)
  const t1Map = Object.fromEntries(t1.map((r,i) => [r.clube, {pos:i+1, pts:r.p}]));
  const t2Map = Object.fromEntries(t2.map((r,i) => [r.clube, {pos:i+1, pts:r.p}]));
  const delta = Object.keys(t1Map).filter(c => t2Map[c]).map(c => ({
    clube: c, deltaPos: t1Map[c].pos - t2Map[c].pos, deltaPts: t2Map[c].pts - t1Map[c].pts,
    p1: t1Map[c].pos, p2: t2Map[c].pos
  })).sort((a,b) => b.deltaPos - a.deltaPos);
  const cresceu = delta.slice(0, 3);
  const caiu = delta.slice(-3).reverse();
  document.getElementById("tbl-mom").innerHTML = `<thead><tr>
    <th>Clube</th><th class="num">Pos 1ºT</th><th class="num">Pos 2ºT</th><th class="num">Δ Pos</th><th class="num">Δ Pts</th>
  </tr></thead><tbody>
    <tr><td colspan="5" style="background:rgba(74,222,128,.12);font-weight:700;color:var(--accent)">Mais cresceu</td></tr>
    ${cresceu.map(r=>`<tr><td><b>${r.clube}</b></td><td class="num">${r.p1}</td><td class="num">${r.p2}</td><td class="num" style="color:var(--accent)"><b>+${r.deltaPos}</b></td><td class="num">${r.deltaPts>0?"+":""}${r.deltaPts}</td></tr>`).join("")}
    <tr><td colspan="5" style="background:rgba(248,113,113,.12);font-weight:700;color:var(--danger)">Mais caiu</td></tr>
    ${caiu.map(r=>`<tr><td><b>${r.clube}</b></td><td class="num">${r.p1}</td><td class="num">${r.p2}</td><td class="num" style="color:var(--danger)"><b>${r.deltaPos}</b></td><td class="num">${r.deltaPts>0?"+":""}${r.deltaPts}</td></tr>`).join("")}
  </tbody>`;
  // Pts por fase (gráfico stacked)
  const allClubs = tabFinal.map(x => x.clube);
  Plotly.react("ch-fases", [
    {type:"bar",x:allClubs,y:allClubs.map(cl=>(t1.find(x=>x.clube===cl)||{p:0}).p),name:"1º turno",marker:{color:c.accent}},
    {type:"bar",x:allClubs,y:allClubs.map(cl=>(t2.find(x=>x.clube===cl)||{p:0}).p),name:"2º turno",marker:{color:c.accent2}},
    {type:"bar",x:allClubs,y:allClubs.map(cl=>(lt10.find(x=>x.clube===cl)||{p:0}).p),name:"Últ. 10",marker:{color:c.warn},visible:"legendonly"},
    {type:"bar",x:allClubs,y:allClubs.map(cl=>(lt5.find(x=>x.clube===cl)||{p:0}).p),name:"Últ. 5",marker:{color:c.purple},visible:"legendonly"},
  ], plotLayout({barmode:"group",xaxis:{tickangle:-45,gridcolor:c.grid},yaxis:{gridcolor:c.grid,title:"Pontos"},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
}

// ---- COMPARAR TEMPORADAS ----
function popularSelectsCmp() {
  const a = document.getElementById("cmp-a"), b = document.getElementById("cmp-b");
  if (a.options.length) return;
  DATA.temporadas.forEach(t => {
    a.appendChild(new Option(t, t));
    b.appendChild(new Option(t, t));
  });
  a.value = DATA.temporadas[0]; b.value = DATA.temporadas[DATA.temporadas.length - 1];
  a.onchange = renderComparar; b.onchange = renderComparar;
}
function renderComparar() {
  popularSelectsCmp();
  const c = getThemeColors();
  const tA = +document.getElementById("cmp-a").value;
  const tB = +document.getElementById("cmp-b").value;
  const msA = DATA.matches.filter(m => m.temporada === tA);
  const msB = DATA.matches.filter(m => m.temporada === tB);
  const tabA = snapsTempRod(tA, Math.max(...rodadasTemp(tA))).slice().sort((a,b)=>a.pos-b.pos);
  const tabB = snapsTempRod(tB, Math.max(...rodadasTemp(tB))).slice().sort((a,b)=>a.pos-b.pos);
  const golsA = msA.reduce((s,m)=>s+m.gm+m.gv,0);
  const golsB = msB.reduce((s,m)=>s+m.gm+m.gv,0);
  const ptsA = tabA.map(x=>x.p), ptsB = tabB.map(x=>x.p);
  const meanA = ptsA.reduce((s,x)=>s+x,0)/ptsA.length;
  const meanB = ptsB.reduce((s,x)=>s+x,0)/ptsB.length;
  const stdA = Math.sqrt(ptsA.reduce((s,x)=>s+(x-meanA)**2,0)/ptsA.length);
  const stdB = Math.sqrt(ptsB.reduce((s,x)=>s+(x-meanB)**2,0)/ptsB.length);
  document.getElementById("kpis-cmp").innerHTML = `
    <div class="kpi"><div class="v small">${tabA[0].clube} × ${tabB[0].clube}</div><div class="l">Campeões</div></div>
    <div class="kpi"><div class="v">${tabA[0].p} × ${tabB[0].p}</div><div class="l">Pts campeão</div></div>
    <div class="kpi"><div class="v">${tabA[0].p - tabA[1].p} × ${tabB[0].p - tabB[1].p}</div><div class="l">Δ p/ vice</div></div>
    <div class="kpi"><div class="v">${golsA} × ${golsB}</div><div class="l">Gols totais</div></div>
    <div class="kpi"><div class="v">${(golsA/msA.length).toFixed(2)} × ${(golsB/msB.length).toFixed(2)}</div><div class="l">Gols/jogo</div></div>
    <div class="kpi"><div class="v">${stdA.toFixed(1)} × ${stdB.toFixed(1)}</div><div class="l">σ pontos (equilíbrio)</div></div>
  `;
  // Tabela lado-a-lado
  const rows = [
    ["Campeão", tabA[0].clube, tabB[0].clube],
    ["Pts campeão", tabA[0].p, tabB[0].p],
    ["Vice", tabA[1].clube, tabB[1].clube],
    ["Δ 1º × 2º", tabA[0].p - tabA[1].p, tabB[0].p - tabB[1].p],
    ["Δ 1º × 4º", tabA[0].p - (tabA[3]?.p||0), tabB[0].p - (tabB[3]?.p||0)],
    ["Δ 1º × último", tabA[0].p - tabA[tabA.length-1].p, tabB[0].p - tabB[tabB.length-1].p],
    ["Pts médios", meanA.toFixed(1), meanB.toFixed(1)],
    ["σ pontos", stdA.toFixed(1), stdB.toFixed(1)],
    ["Total jogos", msA.length, msB.length],
    ["Total gols", golsA, golsB],
    ["Gols/jogo", (golsA/msA.length).toFixed(2), (golsB/msB.length).toFixed(2)],
    ["V mandante (%)", (msA.filter(m=>m.gm>m.gv).length/msA.length*100).toFixed(1), (msB.filter(m=>m.gm>m.gv).length/msB.length*100).toFixed(1)],
    ["Empates", msA.filter(m=>m.gm===m.gv).length, msB.filter(m=>m.gm===m.gv).length],
    ["Última colocada (pts)", tabA[tabA.length-1].p, tabB[tabB.length-1].p],
    ["Último não-rebaixado (16º) pts", (tabA[15]?.p||0), (tabB[15]?.p||0)],
  ];
  document.getElementById("tbl-cmp").innerHTML = `<thead><tr>
    <th>Métrica</th><th class="num">${tA}</th><th class="num">${tB}</th>
  </tr></thead><tbody>` + rows.map(r=>`<tr>
    <td>${r[0]}</td><td class="num">${r[1]}</td><td class="num">${r[2]}</td>
  </tr>`).join("") + "</tbody>";
  // Distribuição de pts
  Plotly.react("ch-cmp-pts", [
    {type:"box",y:ptsA,name:String(tA),marker:{color:c.accent},boxmean:true},
    {type:"box",y:ptsB,name:String(tB),marker:{color:c.accent2},boxmean:true},
  ], plotLayout({yaxis:{title:"Pontos finais",gridcolor:c.grid}}), PCFG);
  // Suspense ao longo
  function dif12(t) {
    const rs = rodadasTemp(t);
    return rs.map(r => {
      const snap = snapsTempRod(t, r).slice().sort((a,b)=>a.pos-b.pos);
      return snap[0] && snap[1] ? snap[0].p - snap[1].p : null;
    });
  }
  const rA = rodadasTemp(tA), rB = rodadasTemp(tB);
  Plotly.react("ch-cmp-suspense", [
    {type:"scatter",mode:"lines",x:rA,y:dif12(tA),name:String(tA),line:{color:c.accent,width:2}},
    {type:"scatter",mode:"lines",x:rB,y:dif12(tB),name:String(tB),line:{color:c.accent2,width:2}},
  ], plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Δ líder × vice (pts)",gridcolor:c.grid}}), PCFG);
  // Gols/rodada
  function golsRod(ms) {
    const m = {}; ms.forEach(x => { m[x.rodada] = (m[x.rodada]||0)+x.gm+x.gv; });
    return m;
  }
  const gA = golsRod(msA), gB = golsRod(msB);
  Plotly.react("ch-cmp-gols", [
    {type:"scatter",mode:"lines",x:rA,y:rA.map(r=>gA[r]||0),name:String(tA),line:{color:c.accent,width:2}},
    {type:"scatter",mode:"lines",x:rB,y:rB.map(r=>gB[r]||0),name:String(tB),line:{color:c.accent2,width:2}},
  ], plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Gols na rodada",gridcolor:c.grid}}), PCFG);
}

// ---- CAMPANHAS HISTÓRICAS ----
function renderCampanhas() {
  // Para cada temporada: campeão (pos 1), rebaixados (17-20), melhor não-campeão fora do G6, etc.
  const camps = [], rebs = [];
  const todasTabs = {};
  DATA.temporadas.forEach(t => {
    const ult = Math.max(...rodadasTemp(t));
    const tab = snapsTempRod(t, ult).slice().sort((a,b)=>a.pos-b.pos);
    todasTabs[t] = tab;
    if (tab.length) {
      camps.push({...tab[0], temp:t});
      tab.filter(x => x.pos >= 17).forEach(x => rebs.push({...x, temp:t}));
    }
  });
  // Rankings entre temporadas
  const cards = [
    ["Campeão com mais pontos", [...camps].sort((a,b)=>b.p-a.p).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.p+" pts"])],
    ["Campeão com menos pontos", [...camps].sort((a,b)=>a.p-b.p).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.p+" pts"])],
    ["Campeão com melhor ataque", [...camps].sort((a,b)=>b.gp-a.gp).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.gp+" gols"])],
    ["Campeão com melhor defesa", [...camps].sort((a,b)=>a.gc-b.gc).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.gc+" sofridos"])],
    ["Campeão com maior aproveitamento", [...camps].sort((a,b)=>b.apr-a.apr).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.apr.toFixed(1)+"%"])],
    ["Campeão com maior saldo de gols", [...camps].sort((a,b)=>b.sg-a.sg).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, (r.sg>0?"+":"")+r.sg])],
    ["Rebaixado com mais pontos", [...rebs].sort((a,b)=>b.p-a.p).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.p+" pts"])],
    ["Rebaixado com menos pontos", [...rebs].sort((a,b)=>a.p-b.p).slice(0,5).map(r=>[`${r.temp} ${r.clube}`, r.p+" pts"])],
    ["Pontuação do 16º colocado", DATA.temporadas.map(t => {
      const tab = todasTabs[t];
      return [`${t} ${tab[15]?.clube||"—"}`, (tab[15]?.p||0)+" pts"];
    }).sort((a,b)=> parseInt(a[1]) - parseInt(b[1])).slice(0,9)],
    ["Maior vantagem do campeão para o vice", camps.map(r => {
      const tab = todasTabs[r.temp];
      const dif = r.p - (tab[1]?.p || 0);
      return [`${r.temp} ${r.clube}`, dif+" pts"];
    }).sort((a,b)=> parseInt(b[1]) - parseInt(a[1])).slice(0,5)],
    ["Temporada mais ofensiva", DATA.temporadas.map(t => {
      const ms = DATA.matches.filter(m => m.temporada === t);
      const tot = ms.reduce((s,m)=>s+m.gm+m.gv,0);
      return [String(t), `${(tot/ms.length).toFixed(2)} g/j (${tot})`];
    }).sort((a,b)=>parseFloat(b[1])-parseFloat(a[1])).slice(0,9)],
    ["Campeonato mais equilibrado por pontos", DATA.temporadas.map(t => {
      const tab = todasTabs[t];
      const ps = tab.map(x=>x.p);
      const m = ps.reduce((s,x)=>s+x,0)/ps.length;
      const std = Math.sqrt(ps.reduce((s,x)=>s+(x-m)**2,0)/ps.length);
      return [String(t), std.toFixed(1)];
    }).sort((a,b)=>parseFloat(a[1])-parseFloat(b[1])).slice(0,9)],
  ];
  document.getElementById("grid-campanhas").innerHTML = cards.map(([titulo, lista]) => `
    <div class="card"><h3>${titulo}</h3>
      <table><tbody>${lista.map((r,i)=>`<tr><td class="num" style="width:30px">${i+1}</td><td><b>${r[0]}</b></td><td class="num">${r[1]}</td></tr>`).join("")}</tbody></table>
    </div>
  `).join("");
  // Perfil dos campeões — média histórica
  const aggC = {
    p: camps.reduce((s,x)=>s+x.p,0)/camps.length,
    v: camps.reduce((s,x)=>s+x.v,0)/camps.length,
    e: camps.reduce((s,x)=>s+x.e,0)/camps.length,
    d: camps.reduce((s,x)=>s+x.d,0)/camps.length,
    gp: camps.reduce((s,x)=>s+x.gp,0)/camps.length,
    gc: camps.reduce((s,x)=>s+x.gc,0)/camps.length,
    sg: camps.reduce((s,x)=>s+x.sg,0)/camps.length,
    apr: camps.reduce((s,x)=>s+x.apr,0)/camps.length,
  };
  document.getElementById("tbl-perfil-camp").innerHTML = `<thead><tr>
    <th>Ano</th><th>Campeão</th><th class="num">Pts</th><th class="num">V</th><th class="num">E</th><th class="num">D</th>
    <th class="num">GP</th><th class="num">GC</th><th class="num">SG</th><th class="num">APR%</th>
  </tr></thead><tbody>` + camps.map(r=>`<tr>
    <td><b>${r.temp}</b></td><td><b>${r.clube}</b></td>
    <td class="num">${r.p}</td><td class="num">${r.v}</td><td class="num">${r.e}</td><td class="num">${r.d}</td>
    <td class="num">${r.gp}</td><td class="num">${r.gc}</td><td class="num">${r.sg>0?"+":""}${r.sg}</td><td class="num">${r.apr.toFixed(1)}</td>
  </tr>`).join("") + `<tr style="background:var(--panel2);font-weight:700">
    <td colspan="2">Média histórica</td>
    <td class="num">${aggC.p.toFixed(1)}</td><td class="num">${aggC.v.toFixed(1)}</td>
    <td class="num">${aggC.e.toFixed(1)}</td><td class="num">${aggC.d.toFixed(1)}</td>
    <td class="num">${aggC.gp.toFixed(1)}</td><td class="num">${aggC.gc.toFixed(1)}</td>
    <td class="num">${aggC.sg>0?"+":""}${aggC.sg.toFixed(1)}</td><td class="num">${aggC.apr.toFixed(1)}</td>
  </tr></tbody>`;
  // Perfil rebaixados
  const aggR = {
    p: rebs.reduce((s,x)=>s+x.p,0)/rebs.length,
    v: rebs.reduce((s,x)=>s+x.v,0)/rebs.length,
    gp: rebs.reduce((s,x)=>s+x.gp,0)/rebs.length,
    gc: rebs.reduce((s,x)=>s+x.gc,0)/rebs.length,
    sg: rebs.reduce((s,x)=>s+x.sg,0)/rebs.length,
    apr: rebs.reduce((s,x)=>s+x.apr,0)/rebs.length,
  };
  document.getElementById("tbl-perfil-reb").innerHTML = `<thead><tr>
    <th>Ano</th><th>Clube</th><th class="num">Pos</th><th class="num">Pts</th><th class="num">V</th>
    <th class="num">GP</th><th class="num">GC</th><th class="num">SG</th><th class="num">APR%</th>
  </tr></thead><tbody>` + rebs.sort((a,b)=>a.temp-b.temp || a.pos-b.pos).map(r=>`<tr>
    <td><b>${r.temp}</b></td><td><b>${r.clube}</b></td><td class="num">${r.pos}</td>
    <td class="num">${r.p}</td><td class="num">${r.v}</td>
    <td class="num">${r.gp}</td><td class="num">${r.gc}</td><td class="num">${r.sg>0?"+":""}${r.sg}</td>
    <td class="num">${r.apr.toFixed(1)}</td>
  </tr>`).join("") + `<tr style="background:var(--panel2);font-weight:700">
    <td colspan="3">Média dos rebaixados</td>
    <td class="num">${aggR.p.toFixed(1)}</td><td class="num">${aggR.v.toFixed(1)}</td>
    <td class="num">${aggR.gp.toFixed(1)}</td><td class="num">${aggR.gc.toFixed(1)}</td>
    <td class="num">${aggR.sg.toFixed(1)}</td><td class="num">${aggR.apr.toFixed(1)}</td>
  </tr></tbody>`;
}

// ---- HISTÓRICO ----
const hfClubSelect = {
  clubes: [],
  bound: false,
  select: document.getElementById("hf-clube"),
  root: document.getElementById("hf-clube-ms"),
  toggle: document.getElementById("hf-clube-toggle"),
  panel: document.getElementById("hf-clube-panel"),
  list: document.getElementById("hf-clube-list"),
  search: document.getElementById("hf-clube-search"),
  label: document.getElementById("hf-clube-label"),
};

function hfClubUpdateLabel() {
  if (!hfClubSelect.label) return;
  if (!state.hfClube) {
    hfClubSelect.label.textContent = "Todos os clubes";
    hfClubSelect.label.classList.add("placeholder");
  } else {
    hfClubSelect.label.textContent = state.hfClube;
    hfClubSelect.label.classList.remove("placeholder");
  }
}

function hfClubRenderList(filtro = "") {
  const h = hfClubSelect;
  if (!h.list) return;
  const q = _normalize(filtro);
  const items = h.clubes.filter(c => !q || _normalize(c).includes(q));
  if (!items.length) {
    h.list.innerHTML = '<div class="ms-empty">Nada encontrado para "' + filtro + '"</div>';
    return;
  }
  h.list.innerHTML = items.map(c => {
    const sel = c === state.hfClube ? " selected" : "";
    return `<div class="ms-item${sel}" data-clube="${c}" role="option" aria-selected="${c === state.hfClube}">
      <span class="ms-cb"><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 4.5" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      <span>${c}</span>
    </div>`;
  }).join("");
  h.list.querySelectorAll(".ms-item").forEach(el => {
    el.onclick = () => {
      state.hfClube = el.dataset.clube;
      if (h.select) h.select.value = state.hfClube;
      hfClubUpdateLabel();
      hfClubClose();
      renderHistoricoFinal();
    };
  });
}

function hfClubOpen() {
  const h = hfClubSelect;
  if (!h.panel) return;
  h.panel.hidden = false;
  h.toggle?.setAttribute("aria-expanded", "true");
  if (h.search) h.search.value = "";
  hfClubRenderList();
  setTimeout(() => h.search?.focus(), 30);
}

function hfClubClose() {
  const h = hfClubSelect;
  if (!h.panel) return;
  h.panel.hidden = true;
  h.toggle?.setAttribute("aria-expanded", "false");
}

function hfClubClearSelection() {
  state.hfClube = "";
  if (hfClubSelect.select) hfClubSelect.select.value = "";
  hfClubUpdateLabel();
  hfClubRenderList(hfClubSelect.search?.value || "");
  renderHistoricoFinal();
}

function initHFClubSelect(clubes) {
  const h = hfClubSelect;
  h.clubes = clubes.slice();
  if (state.hfClube && !h.clubes.includes(state.hfClube)) state.hfClube = "";
  hfClubUpdateLabel();
  hfClubRenderList();
  if (h.bound) return;
  h.bound = true;
  h.toggle.onclick = (e) => {
    e.stopPropagation();
    if (h.panel.hidden) hfClubOpen(); else hfClubClose();
  };
  document.addEventListener("click", (e) => {
    if (h.root && h.panel && !h.panel.hidden && !h.root.contains(e.target)) hfClubClose();
  });
  h.search.oninput = () => hfClubRenderList(h.search.value);
  h.search.onkeydown = (e) => { if (e.key === "Escape") hfClubClose(); };
  document.getElementById("hf-clube-all").onclick = hfClubClearSelection;
  document.getElementById("hf-clube-clear").onclick = () => {
    h.search.value = "";
    hfClubRenderList();
    h.search.focus();
  };
}

function ensureHFControls() {
  if (state.hfInit) return;
  const rows = DATA.class_final_hist || [];
  const years = [...new Set(rows.map(r => r.temporada))].sort((a,b)=>a-b);
  const clubes = [...new Set(rows.map(r => r.clube))].sort((a,b)=>a.localeCompare(b));
  const eds = [...new Set(rows.map(r => r.tipo))].sort();
  const selClube = document.getElementById("hf-clube");
  const selEd = document.getElementById("hf-edicao");
  const selMin = document.getElementById("hf-min");
  const selMax = document.getElementById("hf-max");
  const selRankPos = document.getElementById("hf-rank-pos");
  const racePlay = document.getElementById("hf-race-play");
  const racePrev = document.getElementById("hf-race-prev");
  const raceNext = document.getElementById("hf-race-next");
  const raceRange = document.getElementById("hf-race-range");
  if (!selClube || !selEd || !selMin || !selMax) return;
  selClube.innerHTML = `<option value="">Todos os clubes</option>` + clubes.map(c => `<option value="${c}">${c}</option>`).join("");
  initHFClubSelect(clubes);
  selEd.innerHTML = `<option value="">Todas as edições</option>` + eds.map(t => `<option value="${t}">${t || "sem tipo"}</option>`).join("");
  selMin.innerHTML = years.map(y => `<option value="${y}">${y}</option>`).join("");
  selMax.innerHTML = years.map(y => `<option value="${y}">${y}</option>`).join("");
  if (selRankPos) {
    const posicoes = [...new Set(rows.map(r => r.pos))].sort((a,b)=>a-b);
    selRankPos.innerHTML = posicoes.map(p => `<option value="${p}">${p}º lugar</option>`).join("");
    selRankPos.value = state.hfRankPos;
    selRankPos.onchange = () => { state.hfRankPos = +selRankPos.value; renderHistoricoFinal(); };
  }
  state.hfMin = years[0] || 1937;
  state.hfMax = years[years.length - 1] || DATA.ano_default;
  state.hfRaceIdx = 0;
  state.hfRaceYear = getHFRaceYears()[0] || state.hfMin;
  selMin.value = state.hfMin;
  selMax.value = state.hfMax;
  if (raceRange) {
    const raceYears = getHFRaceYears();
    raceRange.min = 0;
    raceRange.max = Math.max(0, raceYears.length - 1);
    raceRange.step = 1;
    raceRange.value = state.hfRaceIdx;
    raceRange.oninput = () => {
      const raceYearsNow = getHFRaceYears();
      state.hfRaceIdx = +raceRange.value;
      state.hfRaceYear = raceYearsNow[state.hfRaceIdx] || state.hfMin;
      state.hfRacePlaying = false;
      stopHFRace();
      renderHFRace();
    };
  }
  if (racePlay) racePlay.onclick = toggleHFRace;
  if (racePrev) racePrev.onclick = () => stepHFRace(-1);
  if (raceNext) raceNext.onclick = () => stepHFRace(1);
  selClube.onchange = () => { state.hfClube = selClube.value; hfClubUpdateLabel(); hfClubRenderList(); renderHistoricoFinal(); };
  selEd.onchange = () => { state.hfEdicao = selEd.value; resetHFRace(); renderHistoricoFinal(); };
  selMin.onchange = () => { state.hfMin = +selMin.value; if (state.hfMin > state.hfMax) { state.hfMax = state.hfMin; selMax.value = state.hfMax; } resetHFRace(); renderHistoricoFinal(); };
  selMax.onchange = () => { state.hfMax = +selMax.value; if (state.hfMax < state.hfMin) { state.hfMin = state.hfMax; selMin.value = state.hfMin; } resetHFRace(); renderHistoricoFinal(); };
  state.hfInit = true;
}

function resetHFRace() {
  stopHFRace();
  const years = getHFRaceYears();
  state.hfRaceIdx = 0;
  state.hfRaceYear = years[0] || state.hfMin;
  const range = document.getElementById("hf-race-range");
  if (range) {
    range.min = 0;
    range.max = Math.max(0, years.length - 1);
    range.step = 1;
    range.value = state.hfRaceIdx;
  }
}

function stopHFRace() {
  if (hfRaceTimer) clearTimeout(hfRaceTimer);
  if (hfRaceAnimFrame) cancelAnimationFrame(hfRaceAnimFrame);
  hfRaceTimer = null;
  hfRaceAnimFrame = null;
  state.hfRacePlaying = false;
  const btn = document.getElementById("hf-race-play");
  if (btn) btn.textContent = "Play";
}

function getHFRaceRows(pos) {
  const all = DATA.class_final_hist || [];
  return all.filter(r =>
    r.pos === pos &&
    r.temporada >= state.hfMin &&
    r.temporada <= state.hfMax &&
    (!state.hfEdicao || r.tipo === state.hfEdicao)
  ).sort((a,b)=>a.temporada-b.temporada || String(a.edicao_id).localeCompare(String(b.edicao_id)));
}

function getHFRaceYears() {
  return [...new Set(getHFRaceRows(1).map(r => r.temporada))].sort((a,b)=>a-b);
}

function countPositionUntil(rows, year) {
  const counts = {};
  rows.filter(r => r.temporada <= year).forEach(r => counts[r.clube] = (counts[r.clube] || 0) + 1);
  return counts;
}

function blendCounts(a, b, t) {
  const out = {};
  new Set([...Object.keys(a), ...Object.keys(b)]).forEach(k => out[k] = (a[k] || 0) + ((b[k] || 0) - (a[k] || 0)) * t);
  return out;
}

function clubColor(clube) {
  return CLUB_COLORS[clube] || getThemeColors().accent;
}

function toggleHFRace() {
  if (state.hfRacePlaying) {
    stopHFRace();
    return;
  }
  const years = getHFRaceYears();
  if (!years.length) return;
  state.hfRacePlaying = true;
  const btn = document.getElementById("hf-race-play");
  if (btn) btn.textContent = "Pause";
  if (state.hfRaceIdx >= years.length - 1) state.hfRaceIdx = 0;
  state.hfRaceYear = years[state.hfRaceIdx];
  renderHFRace();

  const runStep = () => {
    if (state.tab !== "historico-final") {
      stopHFRace();
      return;
    }
    const latestYears = getHFRaceYears();
    if (state.hfRaceIdx >= latestYears.length - 1) {
      renderHFRace();
      stopHFRace();
      return;
    }
    animateHFRaceStep(latestYears, state.hfRaceIdx, state.hfRaceIdx + 1, () => {
      if (!state.hfRacePlaying) return;
      hfRaceTimer = setTimeout(runStep, 120);
    });
  };
  runStep();
}

function stepHFRace(delta) {
  stopHFRace();
  const years = getHFRaceYears();
  if (!years.length) return;
  state.hfRaceIdx = Math.max(0, Math.min(years.length - 1, state.hfRaceIdx + delta));
  state.hfRaceYear = years[state.hfRaceIdx];
  renderHFRace();
}

function animateHFRaceStep(years, fromIdx, toIdx, done) {
  const byPos = {1:getHFRaceRows(1), 2:getHFRaceRows(2), 3:getHFRaceRows(3)};
  const fromYear = years[fromIdx];
  const toYear = years[toIdx];
  const fromCounts = {
    1: countPositionUntil(byPos[1], fromYear),
    2: countPositionUntil(byPos[2], fromYear),
    3: countPositionUntil(byPos[3], fromYear)
  };
  const toCounts = {
    1: countPositionUntil(byPos[1], toYear),
    2: countPositionUntil(byPos[2], toYear),
    3: countPositionUntil(byPos[3], toYear)
  };
  const started = performance.now();
  const duration = 700;
  const tick = now => {
    if (!state.hfRacePlaying) return;
    const t = Math.min(1, (now - started) / duration);
    const eased = 1 - Math.pow(1 - t, 3);
    state.hfRaceIdx = toIdx;
    state.hfRaceYear = toYear;
    renderHFRace({
      1: blendCounts(fromCounts[1], toCounts[1], eased),
      2: blendCounts(fromCounts[2], toCounts[2], eased),
      3: blendCounts(fromCounts[3], toCounts[3], eased)
    });
    if (t < 1) {
      hfRaceAnimFrame = requestAnimationFrame(tick);
    } else {
      hfRaceAnimFrame = null;
      done();
    }
  };
  hfRaceAnimFrame = requestAnimationFrame(tick);
}

function renderHFRace(countsOverride=null) {
  const years = getHFRaceYears();
  if (state.hfRaceIdx == null || state.hfRaceIdx >= years.length) state.hfRaceIdx = 0;
  if (state.hfRaceIdx < 0) state.hfRaceIdx = 0;
  state.hfRaceYear = years[state.hfRaceIdx] || state.hfMin;
  const range = document.getElementById("hf-race-range");
  const label = document.getElementById("hf-race-year-label");
  const btn = document.getElementById("hf-race-play");
  if (range) {
    range.min = 0;
    range.max = Math.max(0, years.length - 1);
    range.step = 1;
    range.value = state.hfRaceIdx;
  }
  if (label) label.textContent = String(state.hfRaceYear);
  if (btn) btn.textContent = state.hfRacePlaying ? "Pause" : "Play";

  renderHFRaceChart("ch-hf-race-campeoes", 1, "Títulos acumulados", countsOverride ? countsOverride[1] : null, 150);
  renderHFRaceChart("ch-hf-race-vices", 2, "Vices acumulados", countsOverride ? countsOverride[2] : null, 130);
  renderHFRaceChart("ch-hf-race-terceiros", 3, "3ºs lugares acumulados", countsOverride ? countsOverride[3] : null, 130);
}

function renderHFRaceChart(divId, pos, axisTitle, countsOverride=null, leftMargin=140) {
  const c = getThemeColors();
  const rows = getHFRaceRows(pos);
  const finalCounts = {};
  rows.forEach(r => finalCounts[r.clube] = (finalCounts[r.clube] || 0) + 1);
  const xMax = Math.max(1, ...Object.values(finalCounts));
  const counts = countsOverride || countPositionUntil(rows, state.hfRaceYear);
  const arr = Object.entries(counts).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0])).reverse();
  Plotly.react(divId, [{
    type:"bar", orientation:"h",
    y:arr.map(x=>x[0]), x:arr.map(x=>x[1]),
    marker:{color:arr.map(x=>clubColor(x[0])), line:{color:c.text, width:0.7}},
    text:arr.map(x=>Math.abs(x[1] - Math.round(x[1])) < 0.02 ? String(Math.round(x[1])) : x[1].toFixed(1)),
    textposition:"outside",
    hovertemplate:"%{y}<br>" + axisTitle + " até " + state.hfRaceYear + ": %{x:.1f}<extra></extra>"
  }], plotLayout({
    margin:{l:leftMargin,r:45,t:8,b:35},
    xaxis:{title:axisTitle,gridcolor:c.grid,range:[0,xMax + 0.8],dtick:1},
    yaxis:{gridcolor:c.grid,automargin:true}
  }), PCFG);
}

function hfPosLabel(pos) {
  if (pos === 1) return "Títulos";
  if (pos === 2) return "Vices";
  if (pos === 3) return "3ºs lugares";
  return pos + "ºs lugares";
}

function renderHFPositionRanking(rows) {
  const c = getThemeColors();
  const pos = state.hfRankPos || 1;
  const counts = {};
  rows.filter(r => r.pos === pos).forEach(r => counts[r.clube] = (counts[r.clube] || 0) + 1);
  const arr = Object.entries(counts).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0]));
  Plotly.react("ch-hf-rank-pos", [{
    type:"bar", orientation:"h",
    y:arr.map(x=>x[0]).reverse(),
    x:arr.map(x=>x[1]).reverse(),
    marker:{color:arr.map(x=>clubColor(x[0])).reverse(), line:{color:c.text, width:0.7}},
    text:arr.map(x=>x[1]).reverse(),
    textposition:"outside",
    hovertemplate:"%{y}<br>" + hfPosLabel(pos) + ": %{x}<extra></extra>"
  }], plotLayout({
    margin:{l:150,r:50,t:15,b:45},
    xaxis:{title:hfPosLabel(pos),gridcolor:c.grid,dtick:1},
    yaxis:{gridcolor:c.grid,automargin:true}
  }), PCFG);
}

function yearsForPodium(rows) {
  return rows
    .slice()
    .sort((a,b)=>a.temporada-b.temporada || String(a.edicao_id).localeCompare(String(b.edicao_id)))
    .map(r => {
      const tipo = r.tipo ? String(r.tipo).replace("brasileirao_", "").replace("brasileirao", "") : "";
      const suffix = tipo && tipo !== "serie_a" ? ` ${tipo}` : "";
      return `${r.temporada}${suffix}`;
    })
    .join(", ");
}

function renderHFPodiumTable(rows) {
  const byClub = {};
  rows.filter(r => r.pos >= 1 && r.pos <= 3).forEach(r => {
    if (!byClub[r.clube]) byClub[r.clube] = {clube:r.clube, p1:[], p2:[], p3:[]};
    byClub[r.clube][`p${r.pos}`].push(r);
  });
  const arr = Object.values(byClub).sort((a,b) =>
    b.p1.length - a.p1.length ||
    b.p2.length - a.p2.length ||
    b.p3.length - a.p3.length ||
    a.clube.localeCompare(b.clube)
  );
  document.getElementById("tbl-hf-podios").innerHTML = `
    <thead><tr>
      <th>Clube</th>
      <th class="num">Títulos</th><th>Anos dos títulos</th>
      <th class="num">2ºs</th><th>Anos 2ºs</th>
      <th class="num">3ºs</th><th>Anos 3ºs</th>
    </tr></thead><tbody>` +
    arr.map(r => `<tr>
      <td><b>${r.clube}</b></td>
      <td class="num"><b>${r.p1.length}</b></td><td>${yearsForPodium(r.p1) || "-"}</td>
      <td class="num"><b>${r.p2.length}</b></td><td>${yearsForPodium(r.p2) || "-"}</td>
      <td class="num"><b>${r.p3.length}</b></td><td>${yearsForPodium(r.p3) || "-"}</td>
    </tr>`).join("") +
    "</tbody>";
}

function renderHistoricoFinal() {
  ensureHFControls();
  const c = getThemeColors();
  const all = DATA.class_final_hist || [];
  const rows = all.filter(r =>
    r.temporada >= state.hfMin &&
    r.temporada <= state.hfMax &&
    (!state.hfClube || r.clube === state.hfClube) &&
    (!state.hfEdicao || r.tipo === state.hfEdicao)
  ).slice().sort((a,b)=>a.temporada-b.temporada || String(a.edicao_id).localeCompare(String(b.edicao_id)) || a.pos-b.pos);
  const edicoes = new Set(rows.map(r => r.edicao_id));
  const clubes = new Set(rows.map(r => r.clube));
  const campeoes = rows.filter(r => r.pos === 1);
  const campeoesClubes = new Set(campeoes.map(r => r.clube));
  const vicesClubes = new Set(rows.filter(r => r.pos === 2).map(r => r.clube));
  const terceirosClubes = new Set(rows.filter(r => r.pos === 3).map(r => r.clube));
  document.getElementById("kpis-hf").innerHTML = `
    <div class="kpi"><div class="v">${edicoes.size}</div><div class="l">Edições</div></div>
    <div class="kpi"><div class="v">${clubes.size}</div><div class="l">Clubes</div></div>
    <div class="kpi"><div class="v">${campeoesClubes.size}</div><div class="l">Campeões</div></div>
    <div class="kpi"><div class="v">${vicesClubes.size}</div><div class="l">Vices</div></div>
    <div class="kpi"><div class="v">${terceirosClubes.size}</div><div class="l">Terceiros</div></div>
  `;
  renderHFRace();

  renderHFPositionRanking(rows);
  renderHFPodiumTable(rows);

  const parts = {};
  rows.forEach(r => {
    if (!parts[r.clube]) parts[r.clube] = {total:0, p1:0, p2:0, p3:0, p4:0, p5:0, p6:0};
    parts[r.clube].total += 1;
    if (r.pos === 1) parts[r.clube].p1 += 1;
    else if (r.pos === 2) parts[r.clube].p2 += 1;
    else if (r.pos === 3) parts[r.clube].p3 += 1;
    else if (r.pos === 4) parts[r.clube].p4 += 1;
    else if (r.pos === 5) parts[r.clube].p5 += 1;
    else parts[r.clube].p6 += 1;
  });
  const partArr = Object.entries(parts).sort((a,b)=>b[1].total-a[1].total || a[0].localeCompare(b[0]));
  const partWindow = 15;
  const maxPartOffset = Math.max(0, partArr.length - partWindow);
  state.hfPartOffset = Math.min(Math.max(0, state.hfPartOffset || 0), maxPartOffset);
  const partSlider = document.getElementById("hf-part-slider");
  const partWindowLabel = document.getElementById("hf-part-window");
  if (partSlider) {
    partSlider.min = 0;
    partSlider.max = maxPartOffset;
    partSlider.step = 1;
    partSlider.value = state.hfPartOffset;
    partSlider.disabled = maxPartOffset === 0;
    partSlider.oninput = () => {
      state.hfPartOffset = +partSlider.value;
      renderHistoricoFinal();
    };
  }
  if (partWindowLabel) {
    const ini = partArr.length ? state.hfPartOffset + 1 : 0;
    const fim = Math.min(partArr.length, state.hfPartOffset + partWindow);
    partWindowLabel.textContent = `${ini}-${fim} de ${partArr.length}`;
  }
  const partVis = partArr.slice(state.hfPartOffset, state.hfPartOffset + partWindow);
  const clubesPart = partVis.map(x=>x[0]);
  const partSeries = [
    ["1º", "p1", c.champ],
    ["2º", "p2", c.accent2],
    ["3º", "p3", c.accent3],
    ["4º", "p4", c.purple],
    ["5º", "p5", c.warn],
    ["6º+", "p6", c.muted],
  ].map(([name, key, color]) => ({
    type:"bar",
    x:clubesPart,
    y:partVis.map(x=>x[1][key]),
    name,
    marker:{color},
    hovertemplate:"%{x}<br>" + name + ": %{y}<extra></extra>"
  }));
  Plotly.react("ch-hf-part", partSeries, plotLayout({
    barmode:"stack",
    margin:{l:45,r:20,t:20,b:150},
    xaxis:{title:"Clubes",gridcolor:c.grid,tickangle:-55,automargin:true},
    yaxis:{title:"Participações",gridcolor:c.grid,dtick:5},
    legend:{orientation:"h",x:0,y:1.12}
  }), PCFG);

  document.getElementById("tbl-hf").innerHTML = `<thead><tr><th>Ano</th><th>Edição</th><th>Competição</th><th class="num">Pos</th><th>Clube</th><th>UF</th></tr></thead><tbody>` +
    rows.map(r => `<tr><td><b>${r.temporada}</b></td><td>${r.edicao_id}</td><td>${r.competicao}</td><td class="num"><b>${r.pos}</b></td><td><b>${r.clube}</b></td><td>${r.uf || ""}</td></tr>`).join("") +
    "</tbody>";
}

function renderHistorico() {
  const c = getThemeColors();
  // Para cada temporada, calcular tabela final
  const tabelas = {};
  DATA.temporadas.forEach(t => {
    const ms = DATA.matches.filter(m => m.temporada === t);
    tabelas[t] = calcTabela(ms);
  });
  // Campeões / pontos do campeão / artilheiros
  const totaisGols = {};
  DATA.temporadas.forEach(t => {
    totaisGols[t] = DATA.goals.filter(g => g.temporada === t).length;
  });
  const totalJogos = {};
  DATA.temporadas.forEach(t => {
    totalJogos[t] = DATA.matches.filter(m => m.temporada === t).length;
  });
  // KPIs
  const totGols5 = Object.values(totaisGols).reduce((s,x)=>s+x,0);
  const totJogos5 = Object.values(totalJogos).reduce((s,x)=>s+x,0);
  const k = document.getElementById("kpis-hist");
  k.innerHTML = `
    <div class="kpi"><div class="v">${DATA.temporadas.length}</div><div class="l">Temporadas</div></div>
    <div class="kpi"><div class="v">${totJogos5}</div><div class="l">Jogos totais</div></div>
    <div class="kpi"><div class="v">${totGols5}</div><div class="l">Gols totais</div></div>
    <div class="kpi"><div class="v">${(totGols5/totJogos5).toFixed(2)}</div><div class="l">Gols/jogo médio</div></div>
    <div class="kpi"><div class="v">${DATA.cards.length}</div><div class="l">Cartões totais</div></div>
  `;
  // Campeões
  let body = "<thead><tr><th>Temporada</th><th>Campeão</th><th class='num'>Pts</th><th class='num'>V</th><th class='num'>E</th><th class='num'>D</th><th class='num'>SG</th><th class='num'>APR%</th></tr></thead><tbody>";
  DATA.temporadas.forEach(t => {
    const c = tabelas[t][0];
    if (!c) return;
    body += `<tr><td><b>${t}</b></td><td><b>${c.clube}</b></td><td class='num'><b>${c.P}</b></td><td class='num'>${c.V}</td><td class='num'>${c.E}</td><td class='num'>${c.D}</td><td class='num'>${c.SG>0?"+":""}${c.SG}</td><td class='num'>${c.APR.toFixed(1)}</td></tr>`;
  });
  document.getElementById("tbl-campeoes").innerHTML = body + "</tbody>";
  // Rebaixados
  body = "<thead><tr><th>Temporada</th><th>17º</th><th>18º</th><th>19º</th><th>20º</th></tr></thead><tbody>";
  DATA.temporadas.forEach(t => {
    const tab = tabelas[t];
    if (tab.length < 20) return;
    body += `<tr><td><b>${t}</b></td><td>${tab[16].clube}</td><td>${tab[17].clube}</td><td>${tab[18].clube}</td><td><b>${tab[19].clube}</b></td></tr>`;
  });
  document.getElementById("tbl-rebaixados").innerHTML = body + "</tbody>";
  // Artilheiros por temporada
  body = "<thead><tr><th>Temporada</th><th>Artilheiro</th><th>Clube</th><th class='num'>Gols</th></tr></thead><tbody>";
  DATA.temporadas.forEach(t => {
    const gs = DATA.goals.filter(g => g.temporada === t && g.tipo !== "Gol Contra");
    const map = {};
    gs.forEach(g => { const k = g.atleta + "|" + g.clube; map[k] = (map[k]||0) + 1; });
    const top = Object.entries(map).sort((a,b)=>b[1]-a[1])[0];
    if (top) {
      const [name, club] = top[0].split("|");
      body += `<tr><td><b>${t}</b></td><td><b>${name}</b></td><td>${club}</td><td class='num'><b>${top[1]}</b></td></tr>`;
    }
  });
  document.getElementById("tbl-artilheiros-hist").innerHTML = body + "</tbody>";
  // Gols por temporada
  Plotly.react("ch-gols-temp", [{
    type:"bar", x: DATA.temporadas, y: DATA.temporadas.map(t => totaisGols[t]),
    marker:{color:c.accent2}, text: DATA.temporadas.map(t => `${totaisGols[t]} gols<br>${(totaisGols[t]/totalJogos[t]).toFixed(2)}/jogo`),
    textposition:"outside",
    hovertemplate:"%{x}<br><b>%{y}</b> gols<extra></extra>"
  }], plotLayout({xaxis:{tickmode:"linear",gridcolor:c.grid},yaxis:{title:"Gols",gridcolor:c.grid}}), PCFG);
  // Pontos por clube no período
  const allClubs = new Set();
  DATA.temporadas.forEach(t => tabelas[t].forEach(r => allClubs.add(r.clube)));
  const clubsArr = [...allClubs].sort();
  const sel = state.clubesSel.length ? state.clubesSel : clubsArr;
  const palette = ["#4ade80","#60a5fa","#fbbf24","#f87171","#a78bfa","#34d399","#f472b6","#fb923c","#22d3ee","#facc15","#fb7185","#818cf8","#10b981","#e879f9","#fcd34d","#67e8f9","#84cc16","#c084fc","#f43f5e","#06b6d4","#a3e635","#d946ef","#14b8a6","#eab308","#ef4444"];
  const dim = "rgba(138,147,166,0.18)";
  const traces = clubsArr.map((cl, i) => {
    const ys = DATA.temporadas.map(t => {
      const r = tabelas[t].find(x => x.clube === cl);
      return r ? r.P : null;
    });
    return {
      type:"scatter", mode:"lines+markers", name:cl,
      x: DATA.temporadas, y: ys, connectgaps: false,
      line:{color: sel.includes(cl) ? palette[i%palette.length] : dim, width: sel.includes(cl) ? 2.5 : 1},
      marker:{size: sel.includes(cl) ? 8 : 4},
      opacity: sel.includes(cl) ? 1 : 0.3,
      hovertemplate: `<b>${cl}</b><br>%{x}: %{y} pts<extra></extra>`,
    };
  });
  Plotly.react("ch-hist-pts", traces,
    plotLayout({xaxis:{tickmode:"linear",gridcolor:c.grid,title:"Temporada"},yaxis:{title:"Pontos",gridcolor:c.grid},showlegend:true,legend:{font:{size:10}}}), PCFG);
  // Tabela de posição final por clube no período
  const posMap = {};
  clubsArr.forEach(cl => posMap[cl] = {});
  DATA.temporadas.forEach(t => {
    tabelas[t].forEach((r, idx) => { posMap[r.clube][t] = idx + 1; });
  });
  // Ordenar por: número de temporadas presente (desc), depois posição média (asc)
  const rows = clubsArr.map(cl => {
    const positions = DATA.temporadas.map(t => posMap[cl][t]).filter(x => x !== undefined);
    const avg = positions.length ? positions.reduce((s,x)=>s+x,0)/positions.length : 99;
    return { clube: cl, positions: posMap[cl], n: positions.length, avg };
  }).sort((a,b)=> b.n - a.n || a.avg - b.avg);
  let head = "<thead><tr><th>Clube</th>" + DATA.temporadas.map(t=>`<th class='num'>${t}</th>`).join("") + "<th class='num'>Média</th><th class='num'>Particip.</th></tr></thead>";
  let bodyHtml = "<tbody>" + rows.map(r => {
    const cells = DATA.temporadas.map(t => {
      const p = r.positions[t];
      if (p === undefined) return "<td class='num' style='color:var(--muted)'>—</td>";
      const cls = p === 1 ? "zone-champ" : (p <= 6 ? "zone-liber" : (p <= 12 ? "zone-sula" : (p >= 17 ? "zone-reb" : "")));
      return `<td class='num ${cls}'><b>${p}</b></td>`;
    }).join("");
    return `<tr><td><b>${r.clube}</b></td>${cells}<td class='num'>${r.avg.toFixed(1)}</td><td class='num'>${r.n}/5</td></tr>`;
  }).join("") + "</tbody>";
  document.getElementById("tbl-hist-pos").innerHTML = head + bodyHtml;
}

// ---- CAMPEONATO: corrida rodada a rodada ----
function getCampRaceRodadas() {
  return [...new Set(DATA.class_rodada
    .filter(r => r.temporada === state.campRaceTemp)
    .map(r => r.rodada))]
    .sort((a,b)=>a-b);
}

function stopCampRace() {
  if (campRaceTimer) clearTimeout(campRaceTimer);
  if (campRaceAnimFrame) cancelAnimationFrame(campRaceAnimFrame);
  campRaceTimer = null;
  campRaceAnimFrame = null;
  state.campRacePlaying = false;
  const btn = document.getElementById("camp-race-play");
  if (btn) btn.textContent = "Play";
}

function renderCampRace() {
  const c = getThemeColors();
  const temps = DATA.temporadas || [];
  const sel = document.getElementById("camp-race-temp");
  if (sel && !sel.options.length) {
    sel.innerHTML = temps.map(t => `<option value="${t}">${t}</option>`).join("");
    sel.onchange = () => {
      stopCampRace();
      state.campRaceTemp = +sel.value;
      state.campRaceIdx = 0;
      campRaceRenderedTemp = null;
      campRacePrevFrame = null;
      renderCampRace();
    };
  }
  if (sel) sel.value = state.campRaceTemp;

  const rodadas = getCampRaceRodadas();
  if (!rodadas.length) {
    Plotly.react("ch-camp-race", [], plotLayout({annotations:[{text:"Sem classificação rodada a rodada para este campeonato",showarrow:false,x:0.5,y:0.5,xref:"paper",yref:"paper",font:{color:c.muted}}]}), PCFG);
    return;
  }
  state.campRaceIdx = Math.max(0, Math.min(rodadas.length - 1, state.campRaceIdx || 0));
  const rodada = rodadas[state.campRaceIdx];
  const rows = DATA.class_rodada
    .filter(r => r.temporada === state.campRaceTemp && r.rodada === rodada)
    .sort((a,b)=>a.pos-b.pos || b.p-a.p || a.clube.localeCompare(b.clube));

  const range = document.getElementById("camp-race-range");
  const label = document.getElementById("camp-race-round-label");
  if (range) {
    range.min = 0;
    range.max = rodadas.length - 1;
    range.step = 1;
    range.value = state.campRaceIdx;
    range.oninput = () => {
      stopCampRace();
      state.campRaceIdx = +range.value;
      renderCampRace();
    };
  }
  if (label) label.textContent = `Rodada ${rodada}`;

  const rowsByClub = Object.fromEntries(rows.map(r => [r.clube, r]));
  const clubs = [...new Set(DATA.class_rodada
    .filter(r => r.temporada === state.campRaceTemp)
    .map(r => r.clube))]
    .sort((a,b) => a.localeCompare(b));
  const n = rows.length;
  const targetFrame = Object.fromEntries(clubs.map(cl => {
    const r = rowsByClub[cl];
    return [cl, {
      p: r ? r.p : 0,
      pos: r ? r.pos : n + 1,
      y: r ? n - r.pos + 1 : 0,
    }];
  }));
  const previousFrame = campRacePrevFrame && campRaceRenderedTemp === state.campRaceTemp ? campRacePrevFrame : targetFrame;
  const buildTraces = (frame, labelFrame) => clubs.map(cl => {
    const r = rowsByClub[cl];
    const f = frame[cl] || targetFrame[cl];
    const lf = labelFrame[cl] || targetFrame[cl];
    return {
      type:"bar", orientation:"h", name:cl, showlegend:false,
      x:[f.p],
      y:[f.y],
      width:[0.72],
      marker:{color:clubColor(cl), line:{color:c.text,width:0.7}},
      text:[r ? `${lf.pos}º · ${cl} · ${Math.round(f.p)} pts` : cl],
      textposition:"outside",
      cliponaxis:false,
      customdata:[[lf.pos, cl]],
      hovertemplate:"%{customdata[0]}º %{customdata[1]}<br>%{x:.0f} pontos<extra></extra>"
    };
  });
  const maxPts = Math.max(1, ...rows.map(r => r.p));
  const seasonMaxPts = Math.max(1, ...DATA.class_rodada.filter(r => r.temporada === state.campRaceTemp).map(r => r.p));
  const layout = plotLayout({
    margin:{l:70,r:160,t:20,b:45},
    bargap:0.18,
    xaxis:{title:"Pontos acumulados",gridcolor:c.grid,range:[0, seasonMaxPts + 12],tickformat:".0f",fixedrange:true},
    yaxis:{
      title:"Posição na rodada",
      gridcolor:c.grid,
      range:[0, n + 1],
      tickmode:"array",
      tickvals:Array.from({length:n}, (_,i)=>i+1),
      ticktext:Array.from({length:n}, (_,i)=>`${n-i}º`)
    },
    showlegend:false,
    meta:{campRaceTemp:state.campRaceTemp}
  });
  const graph = document.getElementById("ch-camp-race");
  const renderFrame = (frame) => Plotly.react("ch-camp-race", buildTraces(frame, targetFrame), layout, PCFG);
  if (graph && graph.data && graph.data.length === clubs.length && campRaceRenderedTemp === state.campRaceTemp) {
    if (campRaceAnimFrame) cancelAnimationFrame(campRaceAnimFrame);
    const start = performance.now();
    const duration = 1300;
    const ease = t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    const tick = (now) => {
      const raw = Math.min(1, (now - start) / duration);
      const k = ease(raw);
      const frame = Object.fromEntries(clubs.map(cl => {
        const a = previousFrame[cl] || targetFrame[cl];
        const b = targetFrame[cl];
        return [cl, {
          p: a.p + (b.p - a.p) * k,
          y: a.y + (b.y - a.y) * k,
          pos: b.pos,
        }];
      }));
      renderFrame(frame);
      if (raw < 1) campRaceAnimFrame = requestAnimationFrame(tick);
      else {
        campRaceAnimFrame = null;
        campRacePrevFrame = targetFrame;
      }
    };
    campRaceAnimFrame = requestAnimationFrame(tick);
  } else {
    renderFrame(targetFrame);
    campRaceRenderedTemp = state.campRaceTemp;
    campRacePrevFrame = targetFrame;
  }

  document.getElementById("camp-race-play").onclick = toggleCampRace;
  document.getElementById("camp-race-prev").onclick = () => { stopCampRace(); stepCampRace(-1); };
  document.getElementById("camp-race-next").onclick = () => { stopCampRace(); stepCampRace(1); };
  return;

  const y = rows.map(r => r.clube).reverse();
  const x = rows.map(r => r.p).reverse();
  const pos = rows.map(r => r.pos).reverse();
  Plotly.react("ch-camp-race", [{
    type:"bar", orientation:"h",
    y, x,
    marker:{color: rows.map(r => clubColor(r.clube)).reverse(), line:{color:c.text,width:0.7}},
    text: rows.map(r => `${r.pos}º · ${r.p} pts`).reverse(),
    textposition:"outside",
    customdata: pos,
    hovertemplate:"%{customdata}º %{y}<br>%{x} pontos<extra></extra>"
  }], plotLayout({
    margin:{l:135,r:80,t:20,b:45},
    xaxis:{title:"Pontos acumulados",gridcolor:c.grid,range:[0, Math.max(1, ...x) + 6]},
    yaxis:{title:"Posição na rodada",gridcolor:c.grid,automargin:true},
    showlegend:false
  }), PCFG);

  document.getElementById("camp-race-play").onclick = toggleCampRace;
  document.getElementById("camp-race-prev").onclick = () => { stopCampRace(); stepCampRace(-1); };
  document.getElementById("camp-race-next").onclick = () => { stopCampRace(); stepCampRace(1); };
}

function stepCampRace(delta) {
  const rodadas = getCampRaceRodadas();
  if (!rodadas.length) return;
  state.campRaceIdx = Math.max(0, Math.min(rodadas.length - 1, state.campRaceIdx + delta));
  renderCampRace();
}

function scheduleCampRace() {
  if (!state.campRacePlaying) return;
  const rodadas = getCampRaceRodadas();
  if (!rodadas.length || state.campRaceIdx >= rodadas.length - 1) {
    stopCampRace();
    return;
  }
  campRaceTimer = setTimeout(() => {
    state.campRaceIdx += 1;
    renderCampRace();
    scheduleCampRace();
  }, 1450);
}

function toggleCampRace() {
  if (state.campRacePlaying) {
    stopCampRace();
    return;
  }
  const rodadas = getCampRaceRodadas();
  if (!rodadas.length) return;
  if (state.campRaceIdx >= rodadas.length - 1) state.campRaceIdx = 0;
  state.campRacePlaying = true;
  const btn = document.getElementById("camp-race-play");
  if (btn) btn.textContent = "Pause";
  renderCampRace();
  scheduleCampRace();
}

// ---- RESUMO ----
function renderResumo({ms, gs, cs, sts}) {
  const c = getThemeColors();
  renderCampRace();
  const tab = calcTabela(ms);
  const total = ms.reduce((s,m)=>s+m.gm+m.gv,0);
  const empates = ms.filter(m=>m.gm===m.gv).length;
  const goleada = [...ms].sort((a,b)=> Math.abs(b.gm-b.gv) - Math.abs(a.gm-a.gv))[0];
  const lider = tab[0];
  const bestAtq = [...tab].sort((a,b)=>b.GP-a.GP)[0];
  const bestDef = [...tab].sort((a,b)=>a.GC-b.GC)[0];
  const bestApr = [...tab].sort((a,b)=>b.APR-a.APR)[0];
  // artilheiro
  const art = {};
  gs.filter(g=>g.tipo!=="Gol Contra").forEach(g => { art[g.atleta] = (art[g.atleta]||0)+1; });
  const artTop = Object.entries(art).sort((a,b)=>b[1]-a[1])[0] || ["—",0];
  const rodadas = [...new Set(ms.map(m=>m.rodada))];
  const k = document.getElementById("kpis-resumo");
  k.innerHTML = `
    <div class="kpi"><div class="v">${ms.length}</div><div class="l">Jogos</div></div>
    <div class="kpi"><div class="v">${rodadas.length}</div><div class="l">Rodadas</div></div>
    <div class="kpi"><div class="v">${total}</div><div class="l">Gols</div></div>
    <div class="kpi"><div class="v">${ms.length?(total/ms.length).toFixed(2):"0"}</div><div class="l">Gols/jogo</div></div>
    <div class="kpi"><div class="v">${empates}</div><div class="l">Empates</div></div>
    <div class="kpi"><div class="v small">${goleada?goleada.mandante+" "+goleada.gm+"×"+goleada.gv+" "+goleada.visitante:"—"}</div><div class="l">Maior goleada</div><div class="sub">${goleada?goleada.data:""}</div></div>
    <div class="kpi"><div class="v small">${bestAtq?bestAtq.clube:"—"}</div><div class="l">Melhor ataque (${bestAtq?bestAtq.GP:0} gols)</div></div>
    <div class="kpi"><div class="v small">${bestDef?bestDef.clube:"—"}</div><div class="l">Melhor defesa (${bestDef?bestDef.GC:0} sofridos)</div></div>
    <div class="kpi"><div class="v small">${bestApr?bestApr.clube:"—"}</div><div class="l">Maior aproveitamento (${bestApr?bestApr.APR.toFixed(1):0}%)</div></div>
    <div class="kpi"><div class="v small">${artTop[0]}</div><div class="l">Artilheiro (${artTop[1]} gols)</div></div>
    <div class="kpi"><div class="v small">${lider?lider.clube:"—"}</div><div class="l">Líder (${lider?lider.P:0} pts)</div></div>
    <div class="kpi"><div class="v small">${tab.length>=20?tab.slice(-4).map(t=>t.clube).join(", "):"—"}</div><div class="l">Zona reb. (17º-20º)</div></div>
  `;
  // Top 6
  const top6 = tab.slice(0,6);
  Plotly.react("ch-top6", [{type:"bar",orientation:"h",x:top6.map(r=>r.P).reverse(),y:top6.map(r=>r.clube).reverse(),
    marker:{color:c.accent}, text: top6.map(r=>r.P).reverse(), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} pontos<extra></extra>"}],
    plotLayout({margin:{l:120,r:30,t:10,b:30}}), PCFG);
  // Bottom 4
  const bot = tab.slice(-4);
  Plotly.react("ch-bot4", [{type:"bar",orientation:"h",x:bot.map(r=>r.P).reverse(),y:bot.map(r=>r.clube).reverse(),
    marker:{color:c.danger}, text: bot.map(r=>r.P).reverse(), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} pontos<extra></extra>"}],
    plotLayout({margin:{l:120,r:30,t:10,b:30}}), PCFG);
  // Gols por rodada
  const byR = {};
  ms.forEach(m => { byR[m.rodada] = (byR[m.rodada]||0)+m.gm+m.gv; });
  const rs = Object.keys(byR).map(Number).sort((a,b)=>a-b);
  Plotly.react("ch-gols-rod", [{type:"scatter",mode:"lines+markers",x:rs,y:rs.map(r=>byR[r]),
    line:{color:c.accent2,width:2},marker:{color:c.accent2,size:7},
    fill:"tozeroy",fillcolor:c.accent2+"22",
    hovertemplate:"Rodada %{x}<br><b>%{y}</b> gols<extra></extra>"}],
    plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Gols",gridcolor:c.grid}}), PCFG);
  // Top artilheiros
  const art2 = {};
  gs.filter(g=>g.tipo!=="Gol Contra").forEach(g => { const k=g.atleta+"|"+g.clube; art2[k]=(art2[k]||0)+1; });
  const topA = Object.entries(art2).map(([k,v])=>{const [n,c2]=k.split("|"); return {n,c2,v};})
    .sort((a,b)=>b.v-a.v).slice(0,10).reverse();
  Plotly.react("ch-art", [{type:"bar",orientation:"h",x:topA.map(r=>r.v),y:topA.map(r=>`${r.n} (${r.c2})`),
    marker:{color:c.warn}, text:topA.map(r=>r.v), textposition:"outside",
    hovertemplate:"<b>%{y}</b><br>%{x} gols<extra></extra>"}],
    plotLayout({margin:{l:230,r:30,t:10,b:30}}), PCFG);
}

// ---- CLASSIFICAÇÃO ----
function renderClass({ms}) {
  const tab = calcTabela(ms);
  const ult = calcUltimos(ms);
  const dir = state.sortDir==="asc"?1:-1;
  if (state.sortCol !== "P") {
    tab.sort((a,b)=>{
      const A=a[state.sortCol],B=b[state.sortCol];
      if (typeof A==="number") return (A-B)*dir;
      return String(A).localeCompare(String(B))*dir;
    });
  }
  const cols = [["#",""],["clube","Clube"],["P","P"],["J","J"],["V","V"],["E","E"],["D","D"],["GP","GP"],["GC","GC"],["SG","SG"],["APR","APR%"],["last","Últ. 5"],["lastPts","Pts5"]];
  const head = "<thead><tr>" + cols.map(([k,l])=>{
    if (k==="#") return `<th>${l||"#"}</th>`;
    if (k==="last") return `<th>${l}</th>`;
    const cls = (k==="clube"?"":"num ")+"sortable"+(state.sortCol===k?(state.sortDir==="asc"?" sort-asc":" sort-desc"):"");
    return `<th class="${cls}" data-col="${k}">${l}</th>`;
  }).join("") + "</tr></thead>";
  const body = "<tbody>" + tab.map((r,i)=>{
    const idx=i+1;
    const z = idx===1?"zone-champ" : idx<=6?"zone-liber" : idx<=12?"zone-sula" : idx>=17?"zone-reb" : "";
    const u = ult[r.clube] || {last:[],lastPts:0};
    const streak = `<span class="streak">${(u.last||[]).map(x=>`<span class="${x.res}">${x.res}</span>`).join("")}</span>`;
    return `<tr class="${z}">
      <td class="num"><b>${idx}</b></td><td><b>${r.clube}</b></td>
      <td class="num"><b>${r.P}</b></td><td class="num">${r.J}</td>
      <td class="num">${r.V}</td><td class="num">${r.E}</td><td class="num">${r.D}</td>
      <td class="num">${r.GP}</td><td class="num">${r.GC}</td>
      <td class="num">${r.SG>0?"+":""}${r.SG}</td>
      <td class="num">${r.APR.toFixed(1)}</td>
      <td>${streak}</td>
      <td class="num">${u.lastPts||0}</td>
    </tr>`;
  }).join("") + "</tbody>";
  const t = document.getElementById("tbl-class");
  t.innerHTML = head + body;
  t.querySelectorAll("th[data-col]").forEach(th => {
    th.onclick = () => {
      const k = th.dataset.col;
      if (state.sortCol===k) state.sortDir = state.sortDir==="asc"?"desc":"asc";
      else { state.sortCol=k; state.sortDir="desc"; }
      renderClass({ms});
    };
  });
}

// ---- EVOLUÇÃO ----
function renderEvol({ms}) {
  const c = getThemeColors();
  const ev = calcEvolucao(ms);
  const sel = state.clubesSel.length ? state.clubesSel : ev.teams;
  const palette = ["#4ade80","#60a5fa","#fbbf24","#f87171","#a78bfa","#34d399","#f472b6","#fb923c","#22d3ee","#facc15","#fb7185","#818cf8","#10b981","#e879f9","#fcd34d","#67e8f9","#84cc16","#c084fc","#f43f5e","#06b6d4"];
  const dim = "rgba(138,147,166,0.2)";
  const traces = (key) => ev.teams.map((t, i) => ({
    type:"scatter", mode:"lines", name:t,
    x:[0,...ev.rounds], y:ev.cum[t][key],
    line:{color: sel.includes(t) ? palette[i%palette.length] : dim, width: sel.includes(t) ? 2.2 : 1},
    opacity: sel.includes(t) ? 1 : 0.35,
    hovertemplate: `<b>${t}</b><br>Rod %{x}<br>%{y}<extra></extra>`,
  }));
  Plotly.react("ch-evo-pts", traces("pts"),
    plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Pontos",gridcolor:c.grid},showlegend:true,legend:{font:{size:10}}}), PCFG);
  // Posição
  const tracesPos = ev.teams.map((t, i) => ({
    type:"scatter", mode:"lines+markers", name:t,
    x:ev.rounds, y:ev.positions[t],
    line:{color: sel.includes(t) ? palette[i%palette.length] : dim, width: sel.includes(t) ? 2 : 1},
    marker:{size: sel.includes(t) ? 5 : 2},
    opacity: sel.includes(t) ? 1 : 0.3,
    hovertemplate: `<b>${t}</b><br>Rod %{x}<br>Posição: %{y}<extra></extra>`,
  }));
  Plotly.react("ch-evo-pos", tracesPos,
    plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Posição",gridcolor:c.grid,autorange:"reversed",dtick:1},showlegend:true,legend:{font:{size:10}}}), PCFG);
  // SG
  const tracesSG = ev.teams.map((t, i) => {
    const sgArr = ev.cum[t].gp.map((gp,k)=> gp - ev.cum[t].gc[k]);
    return {
      type:"scatter", mode:"lines", name:t,
      x:[0,...ev.rounds], y:sgArr,
      line:{color: sel.includes(t) ? palette[i%palette.length] : dim, width: sel.includes(t) ? 2 : 1},
      opacity: sel.includes(t) ? 1 : 0.3,
    hovertemplate: `<b>${t}</b><br>Rod %{x}<br>Saldo: %{y}<extra></extra>`,
    };
  });
  Plotly.react("ch-evo-sg", tracesSG,
    plotLayout({xaxis:{title:"Rodada",gridcolor:c.grid},yaxis:{title:"Saldo de gols acumulado",gridcolor:c.grid},showlegend:true}), PCFG);
}

// ---- MANDO ----
function renderMando({ms}) {
  const c = getThemeColors();
  const tab = calcTabela(ms);
  const totV_M = ms.filter(m=>m.gm>m.gv).length;
  const totV_V = ms.filter(m=>m.gv>m.gm).length;
  const totE = ms.filter(m=>m.gm===m.gv).length;
  const golsM = ms.reduce((s,m)=>s+m.gm,0);
  const golsV = ms.reduce((s,m)=>s+m.gv,0);
  const k = document.getElementById("kpis-mando");
  k.innerHTML = `
    <div class="kpi"><div class="v">${totV_M}</div><div class="l">Vitórias mandante</div></div>
    <div class="kpi"><div class="v">${totE}</div><div class="l">Empates</div></div>
    <div class="kpi"><div class="v">${totV_V}</div><div class="l">Vitórias visitante</div></div>
    <div class="kpi"><div class="v">${ms.length?Math.round(totV_M/ms.length*1000)/10:0}%</div><div class="l">% vitórias casa</div></div>
    <div class="kpi"><div class="v">${golsM}</div><div class="l">Gols mandantes</div></div>
    <div class="kpi"><div class="v">${golsV}</div><div class="l">Gols visitantes</div></div>
  `;
  const ord = [...tab].sort((a,b)=>b.P_M+b.P_V - (a.P_M+a.P_V));
  Plotly.react("ch-mando-pts", [
    {type:"bar",orientation:"h",x:ord.map(r=>r.P_M).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Mandante",marker:{color:c.accent}},
    {type:"bar",orientation:"h",x:ord.map(r=>r.P_V).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Visitante",marker:{color:c.accent2}},
  ], plotLayout({barmode:"group",margin:{l:120,r:30,t:30,b:40},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  Plotly.react("ch-mando-aprov", [
    {type:"bar",orientation:"h",x:ord.map(r=>r.APR_M).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Mandante %",marker:{color:c.accent}},
    {type:"bar",orientation:"h",x:ord.map(r=>r.APR_V).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Visitante %",marker:{color:c.accent2}},
  ], plotLayout({barmode:"group",margin:{l:120,r:30,t:30,b:40},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  const cols = [["clube","Clube"],["J_M","Jogos casa"],["V_M","Vitórias casa"],["P_M","Pontos casa"],["GP_M","GP casa"],["GC_M","GC casa"],["APR_M","Aprov. casa"],["J_V","Jogos fora"],["V_V","Vitórias fora"],["P_V","Pontos fora"],["GP_V","GP fora"],["GC_V","GC fora"],["APR_V","Aprov. fora"]];
  const head = "<thead><tr>" + cols.map(([k,l])=>`<th class="${k==='clube'?'':'num'}">${l}</th>`).join("") + "</tr></thead>";
  const body = "<tbody>" + ord.map(r=>`<tr>
    <td><b>${r.clube}</b></td>
    <td class="num">${r.J_M}</td><td class="num">${r.V_M}</td><td class="num"><b>${r.P_M}</b></td>
    <td class="num">${r.GP_M}</td><td class="num">${r.GC_M}</td><td class="num">${r.APR_M.toFixed(1)}</td>
    <td class="num">${r.J_V}</td><td class="num">${r.V_V}</td><td class="num"><b>${r.P_V}</b></td>
    <td class="num">${r.GP_V}</td><td class="num">${r.GC_V}</td><td class="num">${r.APR_V.toFixed(1)}</td>
  </tr>`).join("") + "</tbody>";
  document.getElementById("tbl-mando").innerHTML = head + body;
}

// ---- ATAQUE & DEFESA ----
function renderAtaque({ms}) {
  const c = getThemeColors();
  const tab = calcTabela(ms);
  const ult = calcUltimos(ms, 999); // pega tudo
  // Dispersão GP/J × GC/J
  Plotly.react("ch-disp-ad", [{
    type:"scatter", mode:"markers+text",
    x: tab.map(r=>r.J?r.GP/r.J:0),
    y: tab.map(r=>r.J?r.GC/r.J:0),
    text: tab.map(r=>r.clube), textposition:"top center", textfont:{size:9},
    marker:{size: tab.map(r=>r.P*0.8+8), color: tab.map(r=>r.SG), colorscale:"RdYlGn", showscale:true, line:{color:c.text,width:0.5}},
    hovertemplate:"<b>%{text}</b><br>GP/J: %{x:.2f}<br>GC/J: %{y:.2f}<extra></extra>",
  }], plotLayout({xaxis:{title:"Gols pró/jogo",gridcolor:c.grid},yaxis:{title:"Gols sofridos/jogo",gridcolor:c.grid,autorange:"reversed"}}), PCFG);
  // Médias
  const ord = [...tab].sort((a,b)=>b.GP-a.GP);
  Plotly.react("ch-md-gols", [
    {type:"bar",orientation:"h",x:ord.map(r=>r.J?+(r.GP/r.J).toFixed(2):0).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Gols pró/jogo",marker:{color:c.accent}},
    {type:"bar",orientation:"h",x:ord.map(r=>r.J?+(r.GC/r.J).toFixed(2):0).reverse(),y:ord.map(r=>r.clube).reverse(),name:"Gols sofridos/jogo",marker:{color:c.danger}},
  ], plotLayout({barmode:"group",margin:{l:120,r:30,t:30,b:40},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  // Jogos sem sofrer gol
  const csArr = Object.entries(ult).map(([k,v])=>({clube:k,n:v.cleanSheets})).sort((a,b)=>b.n-a.n);
  Plotly.react("ch-clean", [{type:"bar",x:csArr.map(r=>r.clube),y:csArr.map(r=>r.n),marker:{color:c.accent},text:csArr.map(r=>r.n),textposition:"outside"}],
    plotLayout({xaxis:{tickangle:-45,gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
  const noArr = Object.entries(ult).map(([k,v])=>({clube:k,n:v.noScore})).sort((a,b)=>b.n-a.n);
  Plotly.react("ch-noscore", [{type:"bar",x:noArr.map(r=>r.clube),y:noArr.map(r=>r.n),marker:{color:c.danger},text:noArr.map(r=>r.n),textposition:"outside"}],
    plotLayout({xaxis:{tickangle:-45,gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
  // Streaks
  const streakArr = Object.entries(ult).map(([k,v])=>({clube:k,score:v.bestScore,noConc:v.bestNoConc,unb:v.bestUnbeat,lose:v.bestLose}))
    .sort((a,b)=> (b.score+b.noConc) - (a.score+a.noConc));
  Plotly.react("ch-streaks", [
    {type:"bar",x:streakArr.map(r=>r.clube),y:streakArr.map(r=>r.score),name:"Jogos seguidos marcando",marker:{color:c.accent}},
    {type:"bar",x:streakArr.map(r=>r.clube),y:streakArr.map(r=>r.noConc),name:"Jogos seguidos sem sofrer",marker:{color:c.accent2}},
    {type:"bar",x:streakArr.map(r=>r.clube),y:streakArr.map(r=>r.unb),name:"Jogos invicto",marker:{color:c.warn}},
    {type:"bar",x:streakArr.map(r=>r.clube),y:streakArr.map(r=>r.lose),name:"Derrotas seguidas",marker:{color:c.danger}},
  ], plotLayout({barmode:"group",xaxis:{tickangle:-45,gridcolor:c.grid},yaxis:{gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
}

// ---- FORMA ----
function renderForma({ms}) {
  const ult = calcUltimos(ms);
  const arr = Object.entries(ult).map(([k,v])=>({clube:k,...v})).sort((a,b)=>b.lastPts-a.lastPts);
  const head = `<thead><tr>
    <th>Clube</th><th>Últ. 5</th><th class="num">Pts5</th><th class="num">GP5</th><th class="num">GC5</th>
    <th>Sequência atual</th><th class="num">Invicto há</th><th class="num">Maior invict.</th><th class="num">Maior derrotas seg.</th>
  </tr></thead>`;
  const body = "<tbody>" + arr.map(r=>{
    const seq = `<span class="streak">${(r.last||[]).map(x=>`<span class="${x.res}">${x.res}</span>`).join("")}</span>`;
    const cur = r.cur ? `<span class="tag tag-${r.cur}">${r.curN}× ${r.cur}</span>` : "—";
    return `<tr>
      <td><b>${r.clube}</b></td><td>${seq}</td>
      <td class="num"><b>${r.lastPts||0}</b></td>
      <td class="num">${r.lastGP||0}</td><td class="num">${r.lastGC||0}</td>
      <td>${cur}</td>
      <td class="num">${r.invN||0}</td>
      <td class="num">${r.bestUnbeat||0}</td>
      <td class="num">${r.bestLose||0}</td>
    </tr>`;
  }).join("") + "</tbody>";
  document.getElementById("tbl-forma").innerHTML = head + body;
}

// ---- JOGADORES ----
function renderJogadores({ms, gs, cs}) {
  const c = getThemeColors();
  // Artilharia
  const art = {};
  gs.filter(g=>g.tipo!=="Gol Contra").forEach(g => {
    const k=g.atleta+"|"+g.clube;
    if (!art[k]) art[k]={atleta:g.atleta,clube:g.clube,gols:0,penalti:0,faltas:0};
    art[k].gols++;
    if ((g.tipo||"").toLowerCase().includes("penal")) art[k].penalti++;
    if ((g.tipo||"").toLowerCase().includes("falta")) art[k].faltas++;
  });
  const artArr = Object.values(art).sort((a,b)=>b.gols-a.gols).slice(0,30);
  document.getElementById("tbl-art").innerHTML = `<thead><tr>
    <th>#</th><th>Jogador</th><th>Clube</th><th class="num">Gols</th><th class="num">Pênalti</th><th class="num">Falta</th>
  </tr></thead><tbody>` + artArr.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.atleta}</b></td><td>${r.clube}</td>
    <td class="num"><b>${r.gols}</b></td><td class="num">${r.penalti}</td><td class="num">${r.faltas}</td>
  </tr>`).join("") + "</tbody>";
  // Cartões
  const cmap = {};
  cs.forEach(x => {
    const k=x.atleta+"|"+x.clube;
    if (!cmap[k]) cmap[k]={atleta:x.atleta,clube:x.clube,posicao:x.posicao,am:0,vm:0};
    if (x.tipo==="Amarelo") cmap[k].am++; else cmap[k].vm++;
  });
  const cArr = Object.values(cmap).map(r=>({...r,total:r.am+r.vm*3})).sort((a,b)=>b.total-a.total).slice(0,30);
  document.getElementById("tbl-cart-jog").innerHTML = `<thead><tr>
    <th>#</th><th>Jogador</th><th>Clube</th><th>Pos</th><th class="num">Amarelos</th><th class="num">Vermelhos</th><th class="num">Peso</th>
  </tr></thead><tbody>` + cArr.map((r,i)=>`<tr>
    <td class="num">${i+1}</td><td><b>${r.atleta}</b></td><td>${r.clube}</td><td>${r.posicao||"—"}</td>
    <td class="num">${r.am}</td><td class="num">${r.vm}</td><td class="num">${r.total}</td>
  </tr>`).join("") + "</tbody>";
  // Gols por posição registrada nos cartões
  const posMap = {};
  cs.forEach(x => { if (x.posicao && !posMap[x.atleta]) posMap[x.atleta] = x.posicao; });
  const golsPorPos = {};
  gs.filter(g=>g.tipo!=="Gol Contra").forEach(g => {
    const p = posMap[g.atleta] || "Desconhecido";
    golsPorPos[p] = (golsPorPos[p]||0) + 1;
  });
  const posEntries = Object.entries(golsPorPos).sort((a,b)=>b[1]-a[1]);
  Plotly.react("ch-gols-pos", [{type:"bar",x:posEntries.map(r=>r[0]),y:posEntries.map(r=>r[1]),
    marker:{color:c.accent2},text:posEntries.map(r=>r[1]),textposition:"outside"}],
    plotLayout({xaxis:{tickangle:-30,gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
  // Gols por intervalo
  const bins = ["0-15","16-30","31-45","46-60","61-75","76-90","90+"];
  const counts = [0,0,0,0,0,0,0];
  gs.forEach(g => {
    const m=g.minuto;
    let i;
    if (m<=15) i=0; else if (m<=30) i=1; else if (m<=45) i=2;
    else if (m<=60) i=3; else if (m<=75) i=4; else if (m<=90) i=5;
    else i=6;
    counts[i]++;
  });
  Plotly.react("ch-gols-min", [{type:"bar",x:bins,y:counts,marker:{color:c.warn},text:counts,textposition:"outside"}],
    plotLayout({xaxis:{gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
}

// ---- PARTIDAS ----
function renderPartidas({ms}) {
  document.getElementById("qtd-partidas").textContent = `(${ms.length} jogos)`;
  const head = `<thead><tr>
    <th>Data</th><th class="num">Rod</th><th>Mandante</th><th class="num">×</th><th>Visitante</th>
    <th>Resultado</th><th>Arena</th><th>Téc. M</th><th>Téc. V</th><th>Form. M</th><th>Form. V</th>
  </tr></thead>`;
  const ord = [...ms].sort((a,b)=>a.rodada-b.rodada || a.data_iso.localeCompare(b.data_iso));
  const body = "<tbody>" + ord.map(m=>{
    let tag;
    if (m.gm > m.gv) tag = `<span class="tag tag-V">${m.mandante}</span>`;
    else if (m.gv > m.gm) tag = `<span class="tag tag-V">${m.visitante}</span>`;
    else tag = `<span class="tag tag-E">Empate</span>`;
    return `<tr>
      <td>${m.data}</td><td class="num">${m.rodada}</td>
      <td><b>${m.mandante}</b></td>
      <td class="num"><b>${m.gm} × ${m.gv}</b></td>
      <td><b>${m.visitante}</b></td>
      <td>${tag}</td><td>${m.arena||"—"}</td>
      <td>${m.tec_m||"—"}</td><td>${m.tec_v||"—"}</td>
      <td>${m.form_m||"—"}</td><td>${m.form_v||"—"}</td>
    </tr>`;
  }).join("") + "</tbody>";
  document.getElementById("tbl-partidas").innerHTML = head + body;
}

// ---- DISCIPLINA ----
function renderDisc({ms, cs, sts}) {
  const c = getThemeColors();
  const am = cs.filter(x=>x.tipo==="Amarelo").length;
  const vm = cs.filter(x=>x.tipo==="Vermelho").length;
  const totFaltas = sts.reduce((s,x)=>s+(x.faltas||0),0);
  const k = document.getElementById("kpis-disc");
  k.innerHTML = `
    <div class="kpi"><div class="v">${am}</div><div class="l">Amarelos</div></div>
    <div class="kpi"><div class="v">${vm}</div><div class="l">Vermelhos</div></div>
    <div class="kpi"><div class="v">${ms.length?(cs.length/ms.length).toFixed(2):0}</div><div class="l">Cartões/jogo</div></div>
    <div class="kpi"><div class="v">${Math.round(totFaltas)}</div><div class="l">Total faltas</div></div>
    <div class="kpi"><div class="v">${ms.length?(totFaltas/ms.length).toFixed(1):0}</div><div class="l">Faltas/jogo</div></div>
  `;
  const cmap = {};
  cs.forEach(x => { cmap[x.clube] = cmap[x.clube] || {clube:x.clube,am:0,vm:0}; if (x.tipo==="Amarelo") cmap[x.clube].am++; else cmap[x.clube].vm++; });
  const cArr = Object.values(cmap).sort((a,b)=>(b.am+b.vm*3)-(a.am+a.vm*3));
  Plotly.react("ch-cart-clube", [
    {type:"bar",orientation:"h",x:cArr.map(r=>r.am).reverse(),y:cArr.map(r=>r.clube).reverse(),name:"Amarelos",marker:{color:c.warn}},
    {type:"bar",orientation:"h",x:cArr.map(r=>r.vm).reverse(),y:cArr.map(r=>r.clube).reverse(),name:"Vermelhos",marker:{color:c.danger}},
  ], plotLayout({barmode:"stack",margin:{l:120,r:30,t:30,b:40},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  const pmap = {};
  cs.forEach(x => { const p = x.posicao || "Desconhecido"; pmap[p] = pmap[p] || {pos:p,am:0,vm:0}; if (x.tipo==="Amarelo") pmap[p].am++; else pmap[p].vm++; });
  const pArr = Object.values(pmap).sort((a,b)=>(b.am+b.vm)-(a.am+a.vm));
  Plotly.react("ch-cart-pos", [
    {type:"bar",x:pArr.map(r=>r.pos),y:pArr.map(r=>r.am),name:"Amarelos",marker:{color:c.warn}},
    {type:"bar",x:pArr.map(r=>r.pos),y:pArr.map(r=>r.vm),name:"Vermelhos",marker:{color:c.danger}},
  ], plotLayout({barmode:"stack",xaxis:{tickangle:-30,gridcolor:c.grid},yaxis:{gridcolor:c.grid},legend:{x:0,y:1.06,orientation:"h"}}), PCFG);
  // Cartões por minuto
  const bins = ["0-15","16-30","31-45","46-60","61-75","76-90","90+"];
  const counts = [0,0,0,0,0,0,0];
  cs.forEach(x => {
    const m = x.minuto;
    let i;
    if (m<=15) i=0; else if (m<=30) i=1; else if (m<=45) i=2;
    else if (m<=60) i=3; else if (m<=75) i=4; else if (m<=90) i=5;
    else i=6;
    counts[i]++;
  });
  Plotly.react("ch-cart-min", [{type:"bar",x:bins,y:counts,marker:{color:c.danger},text:counts,textposition:"outside"}],
    plotLayout({xaxis:{gridcolor:c.grid},yaxis:{gridcolor:c.grid}}), PCFG);
  // Faltas vs cartões por clube (do stats agregado)
  const fmap = {};
  sts.forEach(x => {
    fmap[x.clube] = fmap[x.clube] || {clube:x.clube,faltas:0,am:0,vm:0};
    fmap[x.clube].faltas += x.faltas||0;
    fmap[x.clube].am += x.amarelos||0;
    fmap[x.clube].vm += x.vermelhos||0;
  });
  const fArr = Object.values(fmap).sort((a,b)=>b.faltas-a.faltas);
  Plotly.react("ch-faltas", [
    {type:"scatter",mode:"markers+text",x:fArr.map(r=>r.faltas),y:fArr.map(r=>r.am+r.vm),
     text:fArr.map(r=>r.clube),textposition:"top center",textfont:{size:9},
     marker:{size:12,color:c.accent2},
     hovertemplate:"<b>%{text}</b><br>Faltas: %{x}<br>Cartões: %{y}<extra></extra>"}],
    plotLayout({xaxis:{title:"Faltas",gridcolor:c.grid},yaxis:{title:"Cartões",gridcolor:c.grid}}), PCFG);
}

// ---- RANKINGS ----
function renderRank({ms, gs, cs}) {
  const tab = calcTabela(ms);
  const ult = calcUltimos(ms, 999);
  const ult5 = calcUltimos(ms, 5);
  // Detectar viradas: time perdia 1+ no momento de algum gol e ganhou — proxy: comparar primeiro gol vs vencedor
  const firstGoalByMatch = {};
  gs.sort((a,b)=>a.minuto-b.minuto).forEach(g => {
    if (!firstGoalByMatch[g.partida_id]) firstGoalByMatch[g.partida_id] = g.clube;
  });
  const viradas = {};
  ms.forEach(m => {
    const fg = firstGoalByMatch[m.id];
    if (!fg) return;
    const winner = m.gm > m.gv ? m.mandante : (m.gv > m.gm ? m.visitante : null);
    if (winner && winner !== fg) {
      viradas[winner] = (viradas[winner]||0) + 1;
    }
  });
  // Mais gols 2T
  const gols2T = {};
  gs.forEach(g => { if (g.minuto > 45) gols2T[g.clube] = (gols2T[g.clube]||0) + 1; });

  const cards = [
    ["Melhor ataque", [...tab].sort((a,b)=>b.GP-a.GP).slice(0,5).map(r=>[r.clube,r.GP+" gols"])],
    ["Melhor defesa", [...tab].sort((a,b)=>a.GC-b.GC).slice(0,5).map(r=>[r.clube,r.GC+" sofridos"])],
    ["Melhor mandante", [...tab].sort((a,b)=>b.APR_M-a.APR_M).slice(0,5).map(r=>[r.clube,r.APR_M.toFixed(1)+"%"])],
    ["Melhor visitante", [...tab].sort((a,b)=>b.APR_V-a.APR_V).slice(0,5).map(r=>[r.clube,r.APR_V.toFixed(1)+"%"])],
    ["Melhor forma nos últimos 5 jogos", Object.entries(ult5).map(([k,v])=>[k,(v.lastPts||0)+" pts"]).sort((a,b)=>parseInt(b[1])-parseInt(a[1])).slice(0,5)],
    ["Maior sequência invicta", Object.entries(ult).map(([k,v])=>[k,(v.bestUnbeat||0)+" jogos"]).sort((a,b)=>parseInt(b[1])-parseInt(a[1])).slice(0,5)],
    ["Maior sequência de derrotas", Object.entries(ult).map(([k,v])=>[k,(v.bestLose||0)+" jogos"]).sort((a,b)=>parseInt(b[1])-parseInt(a[1])).slice(0,5)],
    ["Mais gols no 2º tempo", Object.entries(gols2T).sort((a,b)=>b[1]-a[1]).slice(0,5).map(([k,v])=>[k,v+" gols"])],
    ["Mais viradas", Object.entries(viradas).sort((a,b)=>b[1]-a[1]).slice(0,5).map(([k,v])=>[k,v+" viradas"])],
    ["Mais empates", [...tab].sort((a,b)=>b.E-a.E).slice(0,5).map(r=>[r.clube,r.E])],
    ["Mais cartões", Object.entries(ult).map(([k,v])=>[k]).map(([k])=>{
      const am = cs.filter(x=>x.clube===k && x.tipo==="Amarelo").length;
      const vm = cs.filter(x=>x.clube===k && x.tipo==="Vermelho").length;
      return [k, am+vm, am, vm];
    }).sort((a,b)=>b[1]-a[1]).slice(0,5).map(r=>[r[0], `${r[1]} (${r[2]} amarelos / ${r[3]} vermelhos)`])],
    ["Mais jogos sem sofrer gol", Object.entries(ult).map(([k,v])=>[k,(v.cleanSheets||0)+" jogos"]).sort((a,b)=>parseInt(b[1])-parseInt(a[1])).slice(0,5)],
  ];
  document.getElementById("rankings-grid").innerHTML = cards.map(([titulo, lista]) => `
    <div class="card"><h3>${titulo}</h3>
      <table><tbody>${lista.map((r,i)=>`<tr><td class="num" style="width:30px">${i+1}</td><td><b>${r[0]}</b></td><td class="num">${r[1]}</td></tr>`).join("")}</tbody></table>
    </div>
  `).join("");
}

// ---------- start ----------
render();
</script>
</body></html>
"""

html = TEMPLATE.replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))
out = ROOT / "dashboard.html"
out.write_text(html, encoding="utf-8")
print(f"\nOK -> {out}")
print(f"  payload total: {len(matches)} jogos, {len(goals_data)} gols, {len(cards_data)} cartoes, {len(stats_data)} stats")




