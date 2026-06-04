"""Enriquece o Brasileiro antigo com a camada estrutural (grupo/criterio/pontos).

Idempotente e reproduzivel. Pode rodar quantas vezes quiser e apos qualquer
reimportacao dos anos historicos. Faz tres coisas:

1. Migracao: garante as colunas novas (ALTER TABLE ADD COLUMN se faltarem).
2. Metadados de fase/edicao: num_grupos, formato_serie, criterio (de
   `regras_historicas.py`) e pontos_vitoria por epoca.
3. Grupo por partida: deriva os grupos paralelos por COMPONENTES CONEXOS dos
   confrontos de cada fase de grupos (os grupos sao disjuntos no calendario),
   rotula A, B, C... de forma estavel e grava em fato_partida_nacional_historica.

Uso:
    python -u enriquecer_historico.py
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

import regras_historicas as regras

ROOT = Path(__file__).parent
DB = ROOT / "db" / "brasileirao.db"

# (tabela, coluna, tipo) que precisam existir.
COLUNAS = [
    ("dim_edicao_nacional", "pontos_vitoria", "INTEGER"),
    ("dim_fase_nacional_historica", "num_grupos", "INTEGER"),
    ("dim_fase_nacional_historica", "formato_serie", "TEXT"),
    ("dim_fase_nacional_historica", "criterio", "TEXT"),
    ("fato_partida_nacional_historica", "grupo", "TEXT"),
]


def garantir_colunas(con: sqlite3.Connection) -> None:
    for tabela, coluna, tipo in COLUNAS:
        existentes = {r[1] for r in con.execute(f"PRAGMA table_info({tabela})")}
        if coluna not in existentes:
            con.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo}")
            print(f"  + coluna {tabela}.{coluna}")


def componentes(edges: list[tuple[int, int]], nodes: set[int]) -> list[list[int]]:
    """Componentes conexos via union-find."""
    parent = {n: n for n in nodes}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    comps: dict[int, list[int]] = {}
    for n in nodes:
        comps.setdefault(find(n), []).append(n)
    return list(comps.values())


def enriquecer() -> None:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    try:
        garantir_colunas(con)

        # 1) pontos por vitoria por edicao (regra 2/3 pts da epoca)
        for r in con.execute("SELECT edicao_nacional_id, temporada_id FROM dim_edicao_nacional"):
            con.execute(
                "UPDATE dim_edicao_nacional SET pontos_vitoria = ? WHERE edicao_nacional_id = ?",
                (regras.pontos_vitoria(r["temporada_id"]), r["edicao_nacional_id"]),
            )

        nomes_clube = {r["clube_id"]: r["nome"] for r in con.execute("SELECT clube_id, nome FROM dim_clube")}
        resumo: list[str] = []

        # 2) e 3) por fase: metadados + grupos
        fases = con.execute(
            """
            SELECT f.fase_nacional_id, f.edicao_nacional_id, f.temporada_id, f.fase_ordem,
                   f.fase_nome, f.fase_tipo
            FROM dim_fase_nacional_historica f
            WHERE f.temporada_id BETWEEN 1987 AND 2002
            ORDER BY f.temporada_id, f.fase_ordem
            """
        ).fetchall()

        for f in fases:
            ano = f["temporada_id"]
            partidas = con.execute(
                "SELECT partida_hist_id, mandante_id, visitante_id FROM fato_partida_nacional_historica WHERE fase_nacional_id = ?",
                (f["fase_nacional_id"],),
            ).fetchall()
            nodes = {p["mandante_id"] for p in partidas} | {p["visitante_id"] for p in partidas}
            meta = regras.fase_meta(ano, f["fase_nome"], f["fase_tipo"] or "", len(nodes), len(partidas))

            con.execute(
                "UPDATE dim_fase_nacional_historica SET num_grupos = ?, formato_serie = ?, criterio = ? WHERE fase_nacional_id = ?",
                (meta["num_grupos"], meta["formato_serie"], meta["criterio"], f["fase_nacional_id"]),
            )

            # zera grupo da fase (idempotencia)
            con.execute("UPDATE fato_partida_nacional_historica SET grupo = NULL WHERE fase_nacional_id = ?", (f["fase_nacional_id"],))

            if meta["num_grupos"] and meta["num_grupos"] > 1:
                edges = [(p["mandante_id"], p["visitante_id"]) for p in partidas]
                comps = componentes(edges, nodes)
                # rotulagem estavel: ordena por menor nome de clube do componente
                comps.sort(key=lambda c: min(nomes_clube[n] for n in c))
                rotulo_por_clube: dict[int, str] = {}
                for i, comp in enumerate(comps):
                    letra = chr(ord("A") + i)
                    for n in comp:
                        rotulo_por_clube[n] = letra
                for p in partidas:
                    con.execute(
                        "UPDATE fato_partida_nacional_historica SET grupo = ? WHERE partida_hist_id = ?",
                        (rotulo_por_clube[p["mandante_id"]], p["partida_hist_id"]),
                    )
                aviso = "" if len(comps) == meta["num_grupos"] else f"  !! esperava {meta['num_grupos']} grupos, derivou {len(comps)}"
                tamanhos = sorted(len(c) for c in comps)
                resumo.append(f"  {ano} {f['fase_nome']:<18} grupos={len(comps)} {tamanhos}{aviso}")

        con.commit()
        print("Enriquecimento concluido.")
        if resumo:
            print("Grupos derivados:")
            print("\n".join(resumo))
    finally:
        con.close()


if __name__ == "__main__":
    enriquecer()
