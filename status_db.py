"""Mostra um resumo rapido do banco e do dashboard gerado."""
from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).parent
DB = ROOT / "db" / "brasileirao.db"
DASHBOARD = ROOT / "dashboard.html"


def count(con: sqlite3.Connection, table: str) -> int:
    return int(con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])


def main() -> None:
    if not DB.exists():
        raise SystemExit(f"Banco nao encontrado: {DB}")

    con = sqlite3.connect(DB)
    try:
        print(f"Banco: {DB}")
        print(f"Tamanho do banco: {DB.stat().st_size / 1024 / 1024:.2f} MB")
        atualizado = datetime.fromtimestamp(DB.stat().st_mtime)
        print(f"Atualizado em: {atualizado:%Y-%m-%d %H:%M:%S}")
        print()
        print("Serie A")
        print(f"  Temporadas: {count(con, 'dim_temporada')}")
        print(f"  Partidas: {count(con, 'fato_partida')}")
        print(f"  Gols: {count(con, 'fato_gol')}")
        print(f"  Cartoes: {count(con, 'fato_cartao')}")
        print(f"  Snapshots de classificacao: {count(con, 'fato_classificacao_rodada')}")
        print()
        print("Historico nacional")
        print(f"  Edicoes: {count(con, 'dim_edicao_nacional')}")
        print(f"  Linhas de classificacao final: {count(con, 'fato_classificacao_final_nacional')}")
        print()
        print("Copa do Brasil")
        print(f"  Edicoes: {count(con, 'copa_brasil_edicao')}")
        print(f"  Finais: {count(con, 'copa_brasil_final')}")
        print(f"  Partidas finais: {count(con, 'copa_brasil_final_partida')}")
        print(f"  Participantes mapeados: {count(con, 'copa_brasil_participante')}")
        print()
        if DASHBOARD.exists():
            print(f"Dashboard: {DASHBOARD}")
            print(f"Tamanho do dashboard: {DASHBOARD.stat().st_size / 1024 / 1024:.2f} MB")
        else:
            print(f"Dashboard nao encontrado: {DASHBOARD}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
