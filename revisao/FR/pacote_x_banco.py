"""FR: compara o pacote fra-1 com o que está no db/futebol.db (só leitura)."""
import csv, sqlite3
from collections import Counter
P = "data/coleta/fra-1/pacote/"
def ler(n): return list(csv.DictReader(open(P + n, encoding="utf-8")))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
comp = c.execute("select competicao_id from competicao where slug='fra-1'").fetchone()[0]
eds = {t: (e, camp, vice) for e, t, camp, vice in c.execute("select edicao_id, temporada, campeao_id, vice_id from edicao where competicao_id=?", (comp,))}
J = ler("partidas.csv"); CF = ler("classificacao_final.csv"); ED = ler("edicoes.csv")
dif = 0
pk = Counter((j["temporada"], j["data"] or "", j["mandante"], j["visitante"], j["gols_mandante"], j["gols_visitante"]) for j in J)
bk = Counter()
for t, (e, _, _) in eds.items():
    for d, m, v, gm, gv in c.execute("select coalesce(data,''), mandante_id, visitante_id, gols_mandante, gols_visitante from partida where edicao_id=?", (e,)):
        bk[(t, d, nome[m], nome[v], str(gm), str(gv))] += 1
print("jogos pacote", sum(pk.values()), "banco", sum(bk.values()))
so_p = pk - bk; so_b = bk - pk
print("só no pacote", sum(so_p.values()), list(so_p)[:10]); print("só no banco", sum(so_b.values()), list(so_b)[:10])
for x in ED:
    e, camp, vice = eds[x["temporada"]]
    if (nome.get(camp) or "") != (x["campeao"] or "") or nome.get(vice) != x["vice"]:
        print("pódio difere", x["temporada"], x["campeao"], x["vice"], nome.get(camp), nome.get(vice))
cols = [r[1] for r in c.execute("pragma table_info(classificacao_final)")]
print(cols)
pc = {(x["temporada"], x["clube"]): (int(x["posicao"]), int(x["pontos"]), x["situacao"] or "") for x in CF}
bc = {}
for t, (e, _, _) in eds.items():
    for row in c.execute("select * from classificacao_final where edicao_id=?", (e,)):
        r = dict(zip(cols, row))
        bc[(t, nome[r["clube_id"]])] = (r["posicao"], r["pontos"], r.get("situacao") or "")
for k in sorted(set(pc) | set(bc)):
    if pc.get(k) != bc.get(k): print("classif difere", k, pc.get(k), bc.get(k)); dif += 1
print("classif diferenças:", dif)
