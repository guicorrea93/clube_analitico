"""Revisão Série C (SC): carrega pacote, banco (só leitura) e dados do painel."""
import csv
import json
import sqlite3
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PAC = RAIZ / "data" / "coleta" / "bra-serie-c" / "pacote"
WIKI = RAIZ / "data" / "cache" / "revisao" / "SC" / "wiki"
SLUG = "bra-serie-c"


def ler_csv(nome):
    with open(PAC / nome, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def painel():
    s = (RAIZ / "painel" / "dados" / f"{SLUG}.js").read_text(encoding="utf-8")
    s = s[s.index("=") + 1:].strip().rstrip(";")
    return json.loads(s)


def banco():
    return sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)


def banco_dados():
    """Por temporada: edição (campeão, vice), classificação final, partidas, gols, artilheiros."""
    con = banco()
    cid = con.execute("select competicao_id from competicao where slug=?", (SLUG,)).fetchone()[0]
    nome = dict(con.execute("select clube_id, nome from clube"))
    eds = {}
    for eid, temp, nomeof, camp, vice, nclu in con.execute(
            "select edicao_id, temporada, nome_oficial, campeao_id, vice_id, num_clubes from edicao where competicao_id=?", (cid,)):
        eds[eid] = {"temporada": temp, "nome": nomeof, "campeao": nome.get(camp), "vice": nome.get(vice), "num_clubes": nclu,
                    "classif": [], "partidas": [], "art": []}
    for eid, c, pos, j, v, e, d, gp, gc, pts, aj, sit in con.execute(
            "select edicao_id, clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, ajuste_pontos, situacao "
            "from classificacao_final"):
        if eid in eds:
            eds[eid]["classif"].append([pos, nome[c], j, v, e, d, gp, gc, pts, aj, sit])
    fase = dict(con.execute("select fase_id, nome from fase"))
    gols = defaultdict(list)
    for pid, c, jog, tipo in con.execute("select partida_id, clube_id, jogador, tipo from gol"):
        gols[pid].append((nome[c], jog, tipo))
    for pid, eid, fid, grupo, data, m, v, gm, gv, re_ in con.execute(
            "select partida_id, edicao_id, fase_id, grupo, data, mandante_id, visitante_id, gols_mandante, gols_visitante, resultado_especial from partida"):
        if eid in eds:
            eds[eid]["partidas"].append({"id": pid, "fase": fase[fid], "grupo": grupo, "data": data, "m": nome[m], "v": nome[v],
                                         "gm": gm, "gv": gv, "esp": re_, "gols": gols.get(pid, [])})
    for eid, jog, c, g in con.execute("select edicao_id, jogador, clube_id, gols from artilheiro"):
        if eid in eds:
            eds[eid]["art"].append((jog, nome.get(c), g))
    for e in eds.values():
        e["classif"].sort()
    return {int(e["temporada"]): e for e in eds.values()}
