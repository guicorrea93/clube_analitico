"""Validações de sanidade do banco brasileirao.db."""
from __future__ import annotations
from pathlib import Path
import sqlite3
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = Path(__file__).parent / "db" / "brasileirao.db"

# (ano, clube, pontos) — registro oficial CBF
CAMPEOES_OFICIAIS = [
    (2003, "Cruzeiro",    100),
    (2004, "Santos",       89),
    (2005, "Corinthians",  81),
    (2006, "Sao Paulo",    78),
    (2007, "Sao Paulo",    77),
    (2008, "Sao Paulo",    75),
    (2009, "Flamengo",     67),
    (2010, "Fluminense",   71),
    (2011, "Corinthians",  71),
    (2012, "Fluminense",   77),
    (2013, "Cruzeiro",     76),
    (2014, "Cruzeiro",     80),
    (2015, "Corinthians",  81),
    (2016, "Palmeiras",    80),
    (2017, "Corinthians",  72),
    (2018, "Palmeiras",    80),
    (2019, "Flamengo",     90),
    (2020, "Flamengo",     71),
    (2021, "Atletico-MG",  84),
    (2022, "Palmeiras",    81),
    (2023, "Palmeiras",    70),
    (2024, "Botafogo-RJ",  79),
    (2025, "Flamengo",     79),
]

REBAIXADOS_OFICIAIS = {
    2016: ["Internacional", "Figueirense", "Santa Cruz", "America-MG"],
    2017: ["Avai", "Ponte Preta", "Atletico-GO", "Coritiba"],
    2018: ["Sport", "Vitoria", "Parana", "America-MG"],
    2019: ["Cruzeiro", "CSA", "Chapecoense", "Avai"],
    2020: ["Vasco", "Goias", "Coritiba", "Botafogo-RJ"],
    2021: ["Gremio", "Bahia", "Sport", "Chapecoense"],
    2022: ["Avai", "Atletico-GO", "Ceara", "Juventude"],
    2023: ["Coritiba", "Goias", "Santos", "America-MG"],
    2024: ["Atletico-GO", "Cuiaba", "Athletico-PR", "Criciuma"],
}


def main():
    if not DB.exists():
        print(f"❌ Banco não encontrado em {DB}. Rode criar_banco_brasileirao.py primeiro.")
        sys.exit(1)
    con = sqlite3.connect(DB)
    cur = con.cursor()

    print(f"🔎 Validando banco em {DB}\n")

    falhas = 0

    # ---- Campeões ----
    print("🏆 Campeões (vs registro oficial):")
    for yr, clube_oficial, pts_oficial in CAMPEOES_OFICIAIS:
        row = cur.execute(
            "SELECT clube, pontos FROM vw_tabela_final WHERE temporada_id=? AND posicao=1",
            (yr,),
        ).fetchone()
        if not row:
            print(f"   ❌ {yr}: temporada não encontrada")
            falhas += 1
            continue
        clube_db, pts_db = row
        ok_c = clube_db == clube_oficial
        ok_p = pts_db == pts_oficial
        marker = "✅" if ok_c and ok_p else "⚠️"
        print(f"   {marker} {yr}: DB={clube_db} {pts_db}pts | oficial={clube_oficial} {pts_oficial}pts")
        if not (ok_c and ok_p):
            falhas += 1

    # ---- Rebaixados (apenas 2016-2024 onde temos referência) ----
    print("\n📉 Rebaixados 2016-2024 (vs registro oficial):")
    for yr, oficiais in REBAIXADOS_OFICIAIS.items():
        rows = cur.execute(
            "SELECT clube, posicao FROM vw_tabela_final WHERE temporada_id=? "
            "AND posicao IN (17,18,19,20) ORDER BY posicao",
            (yr,),
        ).fetchall()
        clubes_db = [c for c, _ in rows]
        ok = sorted(clubes_db) == sorted(oficiais)
        marker = "✅" if ok else "⚠️"
        diff = ""
        if not ok:
            diff = f" | DB={clubes_db} oficial={oficiais}"
            falhas += 1
        print(f"   {marker} {yr}: {clubes_db}{diff}")

    # ---- Sanity counts ----
    print("\n🧮 Sanidade dos volumes:")
    n_temp = len(CAMPEOES_OFICIAIS)
    checks = [
        ("Toda partida tem placar válido",
         "SELECT COUNT(*) FROM fato_partida WHERE gols_mandante < 0 OR gols_visitante < 0",
         0),
        ("Toda partida tem mandante != visitante",
         "SELECT COUNT(*) FROM fato_partida WHERE mandante_id = visitante_id",
         0),
        ("Sem gols órfãos (jogador inexistente)",
         "SELECT COUNT(*) FROM fato_gol g LEFT JOIN dim_jogador j ON j.jogador_id=g.jogador_id WHERE j.jogador_id IS NULL",
         0),
        ("Sem cartões órfãos",
         "SELECT COUNT(*) FROM fato_cartao c LEFT JOIN dim_jogador j ON j.jogador_id=c.jogador_id WHERE j.jogador_id IS NULL",
         0),
        ("Classificação cobre todas temporadas",
         "SELECT COUNT(DISTINCT temporada_id) FROM fato_classificacao_rodada",
         n_temp),
    ]
    for nome, sql, esperado in checks:
        n = cur.execute(sql).fetchone()[0]
        ok = (n == esperado)
        if not ok:
            falhas += 1
        marker = "✅" if ok else "❌"
        print(f"   {marker} {nome}: {n} (esperado {esperado})")

    # ---- Resumo final ----
    print(f"\n{'='*50}")
    if falhas == 0:
        print("✅ TUDO OK — banco está consistente com o registro oficial.")
    else:
        print(f"⚠️  {falhas} divergência(s) encontrada(s) — investigar.")
    print(f"{'='*50}")
    con.close()


if __name__ == "__main__":
    main()

