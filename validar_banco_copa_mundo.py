"""Validações de sanidade do banco db/copa_mundo.db."""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = Path(__file__).parent / "db" / "copa_mundo.db"


def escalar(cur: sqlite3.Cursor, sql: str, params=()):
    return cur.execute(sql, params).fetchone()[0]


def main() -> None:
    if not DB.exists():
        print(f"❌ Banco não encontrado em {DB}. Rode criar_banco_copa_mundo.py primeiro.")
        sys.exit(1)
    con = sqlite3.connect(DB)
    cur = con.cursor()
    falhas = 0

    print(f"🔎 Validando banco em {DB}\n")

    checks = [
        ("Edições carregadas", "SELECT COUNT(*) FROM edicao", 23, ">="),
        ("Partidas carregadas", "SELECT COUNT(*) FROM partida", 964, ">="),
        ("Seleções cadastradas", "SELECT COUNT(*) FROM selecao", 80, ">="),
        ("Pessoas cadastradas", "SELECT COUNT(*) FROM pessoa", 1000, ">="),
        ("Gols carregados", "SELECT COUNT(*) FROM gol", 2500, ">="),
        ("Escalações carregadas", "SELECT COUNT(*) FROM escalacao", 2500, ">="),
        ("Partidas sem seleção 1", "SELECT COUNT(*) FROM partida WHERE selecao_1_id IS NULL", 0, "="),
        ("Partidas sem seleção 2", "SELECT COUNT(*) FROM partida WHERE selecao_2_id IS NULL", 0, "="),
    ]

    print("🧮 Volumes e integridade:")
    for nome, sql, esperado, op in checks:
        valor = escalar(cur, sql)
        ok = valor >= esperado if op == ">=" else valor == esperado
        if not ok:
            falhas += 1
        print(f"   {'✅' if ok else '❌'} {nome}: {valor} ({op} {esperado})")

    print("\n⚽ Placar x eventos de gol:")
    divergencias = escalar(
        cur,
        """
        SELECT COUNT(*)
        FROM (
            SELECT p.partida_id,
                   COALESCE(p.gols_selecao_1, 0) + COALESCE(p.gols_selecao_2, 0) AS gols_placar,
                   COUNT(g.gol_id) AS gols_eventos
            FROM partida p
            LEFT JOIN gol g ON g.partida_id = p.partida_id
            WHERE p.gols_selecao_1 IS NOT NULL AND p.gols_selecao_2 IS NOT NULL
            GROUP BY p.partida_id
            HAVING gols_eventos > 0 AND gols_eventos <> gols_placar
        )
        """,
    )
    ok = divergencias == 0
    falhas += 0 if ok else 1
    print(f"   {'✅' if ok else '❌'} Partidas com eventos divergentes do placar: {divergencias}")

    print("\n🧬 Identidade de pessoas:")
    portugal_ronaldo = cur.execute(
        """
        SELECT DISTINCT p.nome
        FROM alias_pessoa a
        JOIN pessoa p ON p.pessoa_id = a.pessoa_id
        JOIN selecao s ON s.selecao_id = a.selecao_contexto_id
        WHERE s.nome='Portugal' AND a.alias_normalizado='ronaldo' AND a.papel='jogador'
        """
    ).fetchall()
    ok = [r[0] for r in portugal_ronaldo] == ["Cristiano Ronaldo"]
    falhas += 0 if ok else 1
    print(f"   {'✅' if ok else '❌'} Portugal + Ronaldo -> Cristiano Ronaldo: {[r[0] for r in portugal_ronaldo]}")

    brasil_ronaldo = cur.execute(
        """
        SELECT DISTINCT p.nome
        FROM alias_pessoa a
        JOIN pessoa p ON p.pessoa_id = a.pessoa_id
        JOIN selecao s ON s.selecao_id = a.selecao_contexto_id
        WHERE s.nome='Brasil' AND a.alias_normalizado='ronaldo' AND a.papel='jogador'
        """
    ).fetchall()
    ok = bool(brasil_ronaldo) and [r[0] for r in brasil_ronaldo] != ["Cristiano Ronaldo"]
    falhas += 0 if ok else 1
    print(f"   {'✅' if ok else '❌'} Brasil + Ronaldo separado de Cristiano: {[r[0] for r in brasil_ronaldo]}")

    auditorias = escalar(cur, "SELECT COUNT(*) FROM auditoria_identidade")
    print(f"   ℹ️ Auditorias de identidade pendentes/para revisar: {auditorias}")

    print("\n🌐 Identidade global de jogadores:")
    globais = [
        ("Dejan Stanković", ["Sérvia e Montenegro", "Sérvia"], "dejanstankovic"),
        ("Nikola Žigić", ["Sérvia e Montenegro", "Sérvia"], "nikolazigic"),
        ("Robert Prosinečki", ["Iugoslávia", "Croácia"], "prosinecki"),
    ]
    for nome_global, selecoes, nome_norm in globais:
        rows = cur.execute(
            f"""
            SELECT DISTINCT ip.nome_canonico
            FROM pessoa p
            JOIN identidade_pessoa ip ON ip.identidade_pessoa_id = p.identidade_pessoa_id
            JOIN selecao s ON s.selecao_id = p.selecao_principal_id
            WHERE p.nome_normalizado=? AND s.nome IN ({",".join("?" for _ in selecoes)})
            """,
            (nome_norm, *selecoes),
        ).fetchall()
        nomes = [r[0] for r in rows]
        ok = nomes == [nome_global]
        falhas += 0 if ok else 1
        print(f"   {'✅' if ok else '❌'} {nome_norm} -> {nomes}")

    mazzola = cur.execute(
        """
        SELECT s.nome, p.nome, ip.nome_canonico
        FROM pessoa p
        JOIN identidade_pessoa ip ON ip.identidade_pessoa_id = p.identidade_pessoa_id
        JOIN selecao s ON s.selecao_id = p.selecao_principal_id
        WHERE p.nome_normalizado IN ('josealtafini', 'sandromazzola')
        ORDER BY s.nome
        """
    ).fetchall()
    nomes_mazzola = {(s, p, ip) for s, p, ip in mazzola}
    esperado_mazzola = {
        ("Brasil", "José Altafini", "José Altafini"),
        ("Itália", "Sandro Mazzola", "Sandro Mazzola"),
    }
    ok = esperado_mazzola.issubset(nomes_mazzola)
    falhas += 0 if ok else 1
    print(f"   {'✅' if ok else '❌'} mazzola separado -> {mazzola}")

    print(f"\n{'='*50}")
    if falhas:
        print(f"❌ {falhas} falha(s) encontrada(s).")
        sys.exit(1)
    print("✅ Banco da Copa do Mundo validado.")
    print(f"{'='*50}")
    con.close()


if __name__ == "__main__":
    main()
