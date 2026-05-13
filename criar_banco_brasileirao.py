"""
Ingest dos CSVs do Brasileirão (adaoduque) para SQLite.

Uso:
    py criar_banco_brasileirao.py            # ingere as temporadas do recorte padrao
    py criar_banco_brasileirao.py --reset    # apaga banco e refaz do zero (default)
    py criar_banco_brasileirao.py --all      # ingere todas as temporadas detectadas

Re-execuções com --reset são idempotentes (banco final identico).
"""
from __future__ import annotations
from pathlib import Path
import argparse
import sqlite3
import sys
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DATA = ROOT / "data"
DB_PATH = ROOT / "db" / "brasileirao.db"
SCHEMA = ROOT / "sql" / "schema.sql"

# =====================================================================
# GROUND TRUTH — Times oficialmente rebaixados ao final de cada temporada.
# Necessário porque o cálculo puro por pontos não captura punições
# administrativas (ex.: Portuguesa 2013 perdeu 4 pts por escalar Heverton
# suspenso, salvando o Fluminense). 2003 teve apenas 2 rebaixados (formato
# de transição). Quando a temporada está aqui, sobrescrevemos a zona da
# rodada final com base nesta lista. Para temporadas ausentes, segue a
# regra de "últimos 4 por pontos" (computada).
# =====================================================================
OFICIAL_REBAIXADOS = {
    2003: ["Fortaleza", "Bahia"],  # apenas 2 rebaixados (formato com 24 clubes)
    2004: ["Criciuma", "Guarani", "Vitoria", "Gremio"],
    2005: ["Coritiba", "Atletico-MG", "Paysandu", "Brasiliense"],
    2006: ["Ponte Preta", "Fortaleza", "Sao Caetano", "Santa Cruz"],
    2007: ["Corinthians", "Juventude", "Parana", "America-RN"],
    2008: ["Figueirense", "Vasco", "Portuguesa", "Ipatinga"],
    2009: ["Coritiba", "Santo Andre", "Nautico", "Sport"],   # ⚠ confirmar Náutico vs Naval
    2010: ["Vitoria", "Guarani", "Goias", "Gremio Prudente"],
    2011: ["Athletico-PR", "Ceara", "America-MG", "Avai"],
    2012: ["Sport", "Palmeiras", "Atletico-GO", "Figueirense"],
    2013: ["Portuguesa", "Vasco", "Ponte Preta", "Nautico"],  # Portuguesa salvou Flu via punição
    2014: ["Vitoria", "Bahia", "Botafogo-RJ", "Criciuma"],
    2015: ["Avai", "Vasco", "Goias", "Joinville"],
    2016: ["Internacional", "Figueirense", "Santa Cruz", "America-MG"],
    2017: ["Coritiba", "Avai", "Ponte Preta", "Atletico-GO"],
    2018: ["Sport", "America-MG", "Vitoria", "Parana"],
    2019: ["Cruzeiro", "CSA", "Chapecoense", "Avai"],
    2020: ["Vasco", "Goias", "Coritiba", "Botafogo-RJ"],
    2021: ["Gremio", "Bahia", "Sport", "Chapecoense"],
    2022: ["Ceara", "Atletico-GO", "Avai", "Juventude"],
    2023: ["Santos", "Goias", "Coritiba", "America-MG"],
    2024: ["Athletico-PR", "Criciuma", "Atletico-GO", "Cuiaba"],
    2025: ["Sport", "Juventude", "Fortaleza", "Ceara"],
}


def parse_min(v) -> int | None:
    if pd.isna(v):
        return None
    try:
        return int(str(v).replace("'", "").replace("+", " ").split()[0])
    except Exception:
        return None


def to_iso(s):
    return pd.to_datetime(s, format="%d/%m/%Y", errors="coerce")


def detectar_temporadas(jogos: pd.DataFrame) -> dict[int, tuple[int, int, str, str]]:
    """Retorna {ano: (id_min, id_max, data_inicio_iso, data_fim_iso)}.

    Algoritmo: cada bloco contíguo de IDs cuja primeira ocorrência de
    rodata=1 está separada por mais de 100 IDs do bloco anterior é uma
    nova temporada. Cobre o caso da pandemia (2020 que termina em 2021).
    """
    j = jogos.dropna(subset=["data_dt"]).copy()
    r1 = j[j["rodata"] == 1].sort_values("ID")
    starts = []
    prev = -10**9
    for _, r in r1.iterrows():
        if r["ID"] - prev > 100:
            starts.append((int(r["ID"]), r["data_dt"].year))
        prev = r["ID"]
    out = {}
    for i, (sid, yr) in enumerate(starts):
        next_id = starts[i + 1][0] - 1 if i + 1 < len(starts) else 10**9
        bloco = j[(j["ID"] >= sid) & (j["ID"] <= next_id)]
        if bloco.empty:
            continue
        out[yr] = (
            sid,
            int(bloco["ID"].max()),
            bloco["data_dt"].min().strftime("%Y-%m-%d"),
            bloco["data_dt"].max().strftime("%Y-%m-%d"),
        )
    return out


def vencedor_normalizado(row, mand_id, vis_id) -> int | None:
    if row["gols_mandante"] > row["gols_visitante"]:
        return mand_id
    if row["gols_visitante"] > row["gols_mandante"]:
        return vis_id
    return None


def calcular_classificacao(
    partidas: pd.DataFrame, num_clubes: int = None  # mantido por compat; nº real é detectado por temporada
) -> pd.DataFrame:
    """Calcula classificação cumulativa após cada rodada.

    Entrada: DataFrame com colunas
        partida_id, temporada_id, rodada, mandante_id, visitante_id,
        gols_mandante, gols_visitante
    Saída: linha por (temporada_id, rodada, clube_id) com posição e métricas.
    """
    rows = []
    for temp, df in partidas.groupby("temporada_id"):
        df = df.sort_values(["rodada", "partida_id"])
        # estado por clube
        state: dict[int, dict] = {}
        for _, r in df.iterrows():
            for cid in (int(r["mandante_id"]), int(r["visitante_id"])):
                state.setdefault(
                    cid,
                    dict(
                        j=0, v=0, e=0, d=0, gp=0, gc=0,
                        pm=0, pv=0, jm=0, jv=0, p=0,
                    ),
                )
        # nº REAL de clubes desta temporada (varia: 24 em 2003-04, 22 em 2005, 20 a partir de 2006)
        n_clubes_temp = len(state)
        rodadas = sorted(df["rodada"].unique())
        for rod in rodadas:
            jogos_rod = df[df["rodada"] == rod]
            for _, r in jogos_rod.iterrows():
                m, v = int(r["mandante_id"]), int(r["visitante_id"])
                gm, gv = int(r["gols_mandante"]), int(r["gols_visitante"])
                sm, sv = state[m], state[v]
                sm["j"] += 1; sv["j"] += 1
                sm["jm"] += 1; sv["jv"] += 1
                sm["gp"] += gm; sm["gc"] += gv
                sv["gp"] += gv; sv["gc"] += gm
                if gm > gv:
                    sm["v"] += 1; sv["d"] += 1
                    sm["pm"] += 3
                elif gv > gm:
                    sv["v"] += 1; sm["d"] += 1
                    sv["pv"] += 3
                else:
                    sm["e"] += 1; sv["e"] += 1
                    sm["pm"] += 1; sv["pv"] += 1
                sm["p"] = sm["v"] * 3 + sm["e"]
                sv["p"] = sv["v"] * 3 + sv["e"]
            # snapshot
            snap = []
            for cid, st in state.items():
                if st["j"] == 0:
                    continue
                snap.append((
                    cid, st["p"], st["v"], st["e"], st["d"],
                    st["gp"], st["gc"], st["gp"] - st["gc"],
                    st["j"], st["pm"], st["pv"], st["jm"], st["jv"],
                ))
            # ordenar por critério oficial: pts, V, SG, GP, alfabético
            snap.sort(key=lambda x: (-x[1], -x[2], -x[7], -x[5]))
            for pos, t in enumerate(snap, 1):
                cid, p, v, e, d, gp, gc, sg, j_, pm, pv, jm, jv = t
                # Zona — usa n_clubes REAL desta temporada para detectar últimos 4 (rebaixamento)
                if pos == 1:
                    zona = "titulo"
                elif pos <= 6:
                    zona = "libertadores"
                elif pos <= 12:
                    zona = "sula"
                elif pos > n_clubes_temp - 4:
                    zona = "rebaixamento"
                else:
                    zona = "meio"
                aprov = round(p / (j_ * 3) * 100, 2) if j_ else 0.0
                rows.append((
                    int(temp), int(rod), cid, pos, p, j_, v, e, d,
                    gp, gc, sg, aprov, pm, pv, jm, jv, zona,
                ))
    cols = [
        "temporada_id", "rodada", "clube_id", "posicao", "pontos", "jogos",
        "vitorias", "empates", "derrotas", "gols_pro", "gols_contra",
        "saldo_gols", "aproveitamento", "pontos_mand", "pontos_vis",
        "jogos_mand", "jogos_vis", "zona",
    ]
    return pd.DataFrame(rows, columns=cols)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", default=True)
    ap.add_argument("--all", action="store_true",
                    help="Ingere todas as temporadas (default: 2016-2024)")
    ap.add_argument("--from", dest="from_year", type=int, default=2016)
    ap.add_argument("--to", dest="to_year", type=int, default=2024)
    args = ap.parse_args()

    print(f"📂 Lendo CSVs de {DATA}/")
    jogos = pd.read_csv(DATA / "jogos.csv")
    gols = pd.read_csv(DATA / "gols.csv")
    cartoes = pd.read_csv(DATA / "cartoes.csv")
    stats = pd.read_csv(DATA / "stats.csv")

    jogos["data_dt"] = to_iso(jogos["data"])

    print("🔍 Detectando temporadas pelo padrão de IDs…")
    temporadas = detectar_temporadas(jogos)
    if args.all:
        anos = sorted(temporadas.keys())
    else:
        anos = sorted([y for y in temporadas if args.from_year <= y <= args.to_year])
    print(f"   temporadas a ingerir: {anos}")

    # Atribui temporada_id a cada jogo
    def temp_de(idx):
        for yr, (a, b, *_) in temporadas.items():
            if a <= idx <= b and yr in anos:
                return yr
        return None
    jogos["temporada_id"] = jogos["ID"].apply(temp_de)
    j_filtrado = jogos[jogos["temporada_id"].notna()].copy()
    j_filtrado = j_filtrado.dropna(subset=["mandante_Placar", "visitante_Placar"])
    j_filtrado["temporada_id"] = j_filtrado["temporada_id"].astype(int)
    j_filtrado["mandante_Placar"] = j_filtrado["mandante_Placar"].astype(int)
    j_filtrado["visitante_Placar"] = j_filtrado["visitante_Placar"].astype(int)
    j_filtrado["rodata"] = j_filtrado["rodata"].astype(int)

    # ----- abre banco -----
    DB_PATH.parent.mkdir(exist_ok=True)
    if args.reset and DB_PATH.exists():
        DB_PATH.unlink()
    print(f"💾 Criando banco em {DB_PATH}")
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))

    # ----- popular dim_competicao -----
    cur = con.cursor()
    cur.execute(
        "INSERT INTO dim_competicao (nome, pais, confederacao, divisao, formato) VALUES (?, ?, ?, ?, ?)",
        ("Brasileirão Série A", "Brasil", "CONMEBOL", 1, "pontos corridos"),
    )
    competicao_id = cur.lastrowid

    # ----- popular dim_temporada -----
    for yr in anos:
        sid, eid, di, df_ = temporadas[yr]
        bloco = j_filtrado[j_filtrado["temporada_id"] == yr]
        n_clubes = len(set(bloco["mandante"]).union(set(bloco["visitante"])))
        n_rod = int(bloco["rodata"].max()) if not bloco.empty else 0
        cur.execute(
            "INSERT INTO dim_temporada (temporada_id, competicao_id, data_inicio, data_fim, num_clubes, num_rodadas, num_jogos) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (yr, competicao_id, di, df_, n_clubes, n_rod, len(bloco)),
        )

    # ----- dim_clube -----
    clubes_set = set(j_filtrado["mandante"]).union(set(j_filtrado["visitante"]))
    # mapa clube -> uf (pega da primeira ocorrência)
    uf_map: dict[str, str] = {}
    for _, r in j_filtrado.iterrows():
        uf_map.setdefault(r["mandante"], r.get("mandante_Estado", None))
        uf_map.setdefault(r["visitante"], r.get("visitante_Estado", None))
    for nome in sorted(clubes_set):
        uf = uf_map.get(nome)
        if pd.isna(uf):
            uf = None
        cur.execute("INSERT INTO dim_clube (nome, uf) VALUES (?, ?)", (nome, uf))
    # mapa nome -> clube_id
    clube_map = {nome: cid for cid, nome in cur.execute("SELECT clube_id, nome FROM dim_clube").fetchall()}

    # ----- dim_arena -----
    arenas = sorted({str(a).strip() for a in j_filtrado["arena"].dropna() if str(a).strip()})
    for nome in arenas:
        cur.execute("INSERT OR IGNORE INTO dim_arena (nome) VALUES (?)", (nome,))
    arena_map = dict(cur.execute("SELECT nome, arena_id FROM dim_arena").fetchall())

    # ----- dim_tecnico -----
    tecnicos = set()
    for col in ("tecnico_mandante", "tecnico_visitante"):
        tecnicos.update(str(t).strip() for t in j_filtrado[col].dropna() if str(t).strip())
    for nome in sorted(tecnicos):
        cur.execute("INSERT OR IGNORE INTO dim_tecnico (nome) VALUES (?)", (nome,))
    tec_map = dict(cur.execute("SELECT nome, tecnico_id FROM dim_tecnico").fetchall())

    # ----- dim_posicao (vem dos cartões) -----
    cart_filtrado = cartoes[cartoes["partida_id"].isin(j_filtrado["ID"])].copy()
    posicoes = sorted({
        str(p).strip() for p in cart_filtrado["posicao"].dropna()
        if str(p).strip()
    })
    for nome in posicoes:
        cur.execute("INSERT OR IGNORE INTO dim_posicao (nome) VALUES (?)", (nome,))
    pos_map = dict(cur.execute("SELECT nome, posicao_id FROM dim_posicao").fetchall())

    # ----- dim_jogador (vem de gols + cartões) -----
    gols_f = gols[gols["partida_id"].isin(j_filtrado["ID"])].copy()
    jogadores_set = set()
    jogadores_set.update(str(n).strip() for n in gols_f["atleta"].dropna() if str(n).strip())
    jogadores_set.update(str(n).strip() for n in cart_filtrado["atleta"].dropna() if str(n).strip())
    # mapeia nome -> posição (do primeiro cartão onde aparece)
    pos_jog: dict[str, str] = {}
    for _, r in cart_filtrado.iterrows():
        n = str(r["atleta"]).strip() if pd.notna(r["atleta"]) else ""
        p = str(r["posicao"]).strip() if pd.notna(r["posicao"]) else ""
        if n and p and n not in pos_jog:
            pos_jog[n] = p
    for nome in sorted(jogadores_set):
        pid = pos_map.get(pos_jog.get(nome))
        cur.execute(
            "INSERT OR IGNORE INTO dim_jogador (nome, posicao_id) VALUES (?, ?)",
            (nome, pid),
        )
    jog_map = dict(cur.execute("SELECT nome, jogador_id FROM dim_jogador").fetchall())

    print(f"   ✓ dims: {len(clube_map)} clubes, {len(arena_map)} arenas, "
          f"{len(tec_map)} técnicos, {len(pos_map)} posições, {len(jog_map)} jogadores")

    # ----- fato_partida -----
    rows_part = []
    for _, r in j_filtrado.iterrows():
        m_id = clube_map[r["mandante"]]
        v_id = clube_map[r["visitante"]]
        venc = None
        if r["mandante_Placar"] > r["visitante_Placar"]:
            venc = m_id
        elif r["visitante_Placar"] > r["mandante_Placar"]:
            venc = v_id
        arena_nome = str(r["arena"]).strip() if pd.notna(r["arena"]) else None
        a_id = arena_map.get(arena_nome) if arena_nome else None
        tm_id = tec_map.get(str(r["tecnico_mandante"]).strip()) if pd.notna(r["tecnico_mandante"]) else None
        tv_id = tec_map.get(str(r["tecnico_visitante"]).strip()) if pd.notna(r["tecnico_visitante"]) else None
        # arrecadacao (renda da partida em R$) — coluna nova adicionada em 2025
        arr = r.get("arrecadacao") if "arrecadacao" in r.index else None
        try:
            arr_val = float(arr) if arr is not None and pd.notna(arr) and str(arr).strip() else None
        except Exception:
            arr_val = None
        rows_part.append((
            int(r["ID"]), int(r["temporada_id"]), competicao_id,
            int(r["rodata"]),
            r["data_dt"].strftime("%Y-%m-%d") if pd.notna(r["data_dt"]) else None,
            r.get("hora") if pd.notna(r.get("hora")) else None,
            m_id, v_id, a_id,
            int(r["mandante_Placar"]), int(r["visitante_Placar"]), venc,
            tm_id, tv_id,
            r.get("formacao_mandante") if pd.notna(r.get("formacao_mandante")) else None,
            r.get("formacao_visitante") if pd.notna(r.get("formacao_visitante")) else None,
            r.get("mandante_Estado") if pd.notna(r.get("mandante_Estado")) else None,
            r.get("visitante_Estado") if pd.notna(r.get("visitante_Estado")) else None,
            arr_val,
        ))
    cur.executemany(
        "INSERT INTO fato_partida (partida_id, temporada_id, competicao_id, rodada, data, hora, "
        "mandante_id, visitante_id, arena_id, gols_mandante, gols_visitante, vencedor_id, "
        "tecnico_mand_id, tecnico_vis_id, formacao_mandante, formacao_visitante, uf_mandante, uf_visitante, "
        "arrecadacao) "
        "VALUES (" + ",".join(["?"] * 19) + ")",
        rows_part,
    )

    # mapa partida_id -> temporada_id, rodada (para fatos auxiliares)
    part_temp = dict(cur.execute(
        "SELECT partida_id, temporada_id FROM fato_partida"
    ).fetchall())
    part_rod = dict(cur.execute(
        "SELECT partida_id, rodada FROM fato_partida"
    ).fetchall())

    # ----- fato_gol -----
    rows_g = []
    for _, r in gols_f.iterrows():
        pid = int(r["partida_id"])
        if pid not in part_temp:
            continue
        clube = clube_map.get(r["clube"])
        if clube is None:
            continue
        atleta = str(r["atleta"]).strip() if pd.notna(r["atleta"]) else None
        if not atleta:
            continue
        jid = jog_map.get(atleta)
        if jid is None:
            continue
        tipo = str(r["tipo_de_gol"]).strip() if pd.notna(r["tipo_de_gol"]) else None
        rows_g.append((
            pid, part_temp[pid], part_rod[pid], clube, jid,
            parse_min(r["minuto"]), tipo,
        ))
    cur.executemany(
        "INSERT INTO fato_gol (partida_id, temporada_id, rodada, clube_id, jogador_id, minuto, tipo) "
        "VALUES (?,?,?,?,?,?,?)",
        rows_g,
    )

    # ----- fato_cartao -----
    rows_c = []
    for _, r in cart_filtrado.iterrows():
        pid = int(r["partida_id"])
        if pid not in part_temp:
            continue
        clube = clube_map.get(r["clube"])
        if clube is None:
            continue
        atleta = str(r["atleta"]).strip() if pd.notna(r["atleta"]) else None
        if not atleta:
            continue
        jid = jog_map.get(atleta)
        if jid is None:
            continue
        pos_id = pos_map.get(str(r["posicao"]).strip()) if pd.notna(r["posicao"]) else None
        rows_c.append((
            pid, part_temp[pid], part_rod[pid], clube, jid, pos_id,
            r["cartao"], parse_min(r["minuto"]),
            str(r["num_camisa"]) if pd.notna(r["num_camisa"]) else None,
        ))
    cur.executemany(
        "INSERT INTO fato_cartao (partida_id, temporada_id, rodada, clube_id, jogador_id, posicao_id, tipo, minuto, num_camisa) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        rows_c,
    )

    # ----- fato_stats_time -----
    stats_f = stats[stats["partida_id"].isin(j_filtrado["ID"])].copy()
    rows_s = []
    def _num(v):
        if pd.isna(v) or str(v).strip() == "":
            return None
        try:
            return float(str(v).replace("%", "").strip())
        except Exception:
            return None
    for _, r in stats_f.iterrows():
        pid = int(r["partida_id"])
        if pid not in part_temp:
            continue
        clube = clube_map.get(r["clube"])
        if clube is None:
            continue
        rows_s.append((
            pid, clube, part_temp[pid], part_rod[pid],
            _num(r["chutes"]), _num(r["chutes_no_alvo"]),
            _num(r["posse_de_bola"]), _num(r["passes"]),
            _num(r["precisao_passes"]), _num(r["faltas"]),
            _num(r["cartao_amarelo"]), _num(r["cartao_vermelho"]),
            _num(r["impedimentos"]), _num(r["escanteios"]),
        ))
    cur.executemany(
        "INSERT OR IGNORE INTO fato_stats_time (partida_id, clube_id, temporada_id, rodada, "
        "chutes, chutes_alvo, posse, passes, prec_passes, faltas, amarelos, vermelhos, "
        "impedimentos, escanteios) VALUES (" + ",".join(["?"] * 14) + ")",
        rows_s,
    )

    # ----- fato_classificacao_rodada -----
    print("📊 Calculando classificação rodada-a-rodada (pode levar alguns segundos)…")
    partidas_df = pd.DataFrame(rows_part, columns=[
        "partida_id", "temporada_id", "competicao_id", "rodada", "data", "hora",
        "mandante_id", "visitante_id", "arena_id",
        "gols_mandante", "gols_visitante", "vencedor_id",
        "tecnico_mand_id", "tecnico_vis_id", "formacao_mandante", "formacao_visitante",
        "uf_mandante", "uf_visitante", "arrecadacao",
    ])
    class_df = calcular_classificacao(partidas_df, num_clubes=20)
    cur.executemany(
        "INSERT INTO fato_classificacao_rodada (temporada_id, rodada, clube_id, posicao, "
        "pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols, "
        "aproveitamento, pontos_mand, pontos_vis, jogos_mand, jogos_vis, zona) "
        "VALUES (" + ",".join(["?"] * 18) + ")",
        class_df.itertuples(index=False, name=None),
    )

    # ====================================================================
    # GROUND TRUTH — sobrescreve `zona` da rodada final com a lista oficial
    # de rebaixados (cobre punições administrativas: ex. Portuguesa 2013)
    # ====================================================================
    print("✏️  Aplicando lista oficial de rebaixados (ground truth)…")
    naoConhecidos = []
    for temp, oficiais in OFICIAL_REBAIXADOS.items():
        if temp not in anos:
            continue
        ult = cur.execute(
            "SELECT MAX(rodada) FROM fato_classificacao_rodada WHERE temporada_id=?",
            (temp,),
        ).fetchone()[0]
        if ult is None:
            continue
        # 1) Reseta a zona dos clubes que estavam marcados como 'rebaixamento' nesta rodada para 'meio'
        cur.execute(
            "UPDATE fato_classificacao_rodada SET zona='meio' "
            "WHERE temporada_id=? AND rodada=? AND zona='rebaixamento'",
            (temp, ult),
        )
        # 2) Marca como 'rebaixamento' apenas os clubes oficialmente rebaixados
        for nome in oficiais:
            cid = clube_map.get(nome)
            if cid is None:
                naoConhecidos.append((temp, nome))
                continue
            n = cur.execute(
                "UPDATE fato_classificacao_rodada SET zona='rebaixamento' "
                "WHERE temporada_id=? AND rodada=? AND clube_id=?",
                (temp, ult, cid),
            ).rowcount
            if n == 0:
                naoConhecidos.append((temp, nome))
    if naoConhecidos:
        print("  ⚠️  Clubes oficiais não encontrados no banco (verificar grafia):")
        for t, n in naoConhecidos:
            print(f"     {t}: {n}")
    else:
        print(f"  ✓ Lista oficial aplicada para {sum(1 for t in OFICIAL_REBAIXADOS if t in anos)} temporadas")

    con.commit()
    con.close()

    # ----- sumário -----
    con = sqlite3.connect(DB_PATH)
    print("\n✅ Ingest concluído!")
    print(f"   Banco: {DB_PATH} ({DB_PATH.stat().st_size / 1024:.1f} KB)")
    print()
    print("   📊 Contagens:")
    for tbl in [
        "dim_competicao", "dim_temporada", "dim_clube", "dim_arena",
        "dim_tecnico", "dim_posicao", "dim_jogador",
        "fato_partida", "fato_gol", "fato_cartao", "fato_stats_time",
        "fato_classificacao_rodada",
    ]:
        n = con.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        print(f"      {tbl:<32} {n:>10,}")
    print()
    print("   🏆 Campeões detectados:")
    for row in con.execute(
        "SELECT temporada_id, clube, pontos FROM vw_tabela_final "
        "WHERE posicao = 1 ORDER BY temporada_id"
    ):
        print(f"      {row[0]}  {row[1]:<22} {row[2]} pts")
    con.close()


if __name__ == "__main__":
    main()

