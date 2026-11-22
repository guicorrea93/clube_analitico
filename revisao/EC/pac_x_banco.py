"""Compara o pacote ecu-1 com o banco (só leitura) e com o painel local."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, json, sqlite3, collections, sys
P = "data/coleta/ecu-1/pacote/"
def rd(f): return list(csv.DictReader(open(P+f, encoding="utf-8")))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
cid = c.execute("select competicao_id from competicao where slug='ecu-1'").fetchone()[0]
ed = rd("edicoes.csv"); pa = rd("partidas.csv"); cl = rd("classificacao_final.csv"); ar = rd("artilheiros.csv")
go = rd("gols.csv"); ca = rd("cartoes.csv"); clu = rd("clubes.csv")
print("pacote: edicoes", len(ed), "partidas", len(pa), "class", len(cl), "art", len(ar), "gols", len(go), "cartoes", len(ca), "clubes", len(clu))
q = lambda s, *a: c.execute(s, a).fetchall()
print("banco: edicoes", q("select count(*) from edicao where competicao_id=?", cid))
print("banco: partidas", q("select count(*) from partida p join edicao e using(edicao_id) where competicao_id=?", cid))
print("banco: class", q("select count(*) from classificacao_final p join edicao e using(edicao_id) where competicao_id=?", cid))
print("banco: art", q("select count(*) from artilheiro p join edicao e using(edicao_id) where competicao_id=?", cid))
print("banco: gols", q("select count(*) from gol g join partida p using(partida_id) join edicao e using(edicao_id) where competicao_id=?", cid))
print("banco: cartoes", q("select count(*) from cartao g join partida p using(partida_id) join edicao e using(edicao_id) where competicao_id=?", cid))
print("banco: tabpub", q("select count(*) from tabela_publicada p join edicao e using(edicao_id) where competicao_id=?", cid))
# jogos por chave (temporada, data, mandante, visitante, placar)
nome = dict(q("select clube_id, nome from clube"))
bj = collections.Counter()
for t, d, m, v, gm, gv in q("""select e.temporada, p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante
        from partida p join edicao e using(edicao_id) where competicao_id=?""", cid):
    bj[(t, d or "", nome[m], nome[v], gm, gv)] += 1
pj = collections.Counter()
for r in pa:
    gm = int(r["gols_mandante"]) if r["gols_mandante"] != "" else None
    gv = int(r["gols_visitante"]) if r["gols_visitante"] != "" else None
    pj[(r["temporada"], r["data"], r["mandante"], r["visitante"], gm, gv)] += 1
print("jogos só no pacote:", sum((pj - bj).values()), list((pj - bj).items())[:10])
print("jogos só no banco:", sum((bj - pj).values()), list((bj - pj).items())[:10])
# campeao/vice
bce = {t: (nome.get(a), nome.get(b)) for t, a, b in q("select temporada, campeao_id, vice_id from edicao where competicao_id=?", cid)}
for r in ed:
    if bce.get(r["temporada"]) != (r["campeao"], r["vice"]):
        print("campeao/vice difere", r["temporada"], bce.get(r["temporada"]), r["campeao"], r["vice"])
# classificação
bcl = {}
for t, cl_, pos, j, v, e_, d, gp, gc, pts, aj, sit in q("""select e.temporada, clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, ajuste_pontos, situacao
        from classificacao_final c join edicao e using(edicao_id) where competicao_id=?""", cid):
    bcl[(t, nome[cl_])] = (pos, j, v, e_, d, gp, gc, pts, aj, sit)
dif = 0
for r in cl:
    k = (r["temporada"], r["clube"])
    def i(x): return int(x) if x not in ("", None) else None
    pv = (i(r["posicao"]), i(r["jogos"]), i(r["vitorias"]), i(r["empates"]), i(r["derrotas"]), i(r["gols_pro"]), i(r["gols_contra"]), i(r["pontos"]), i(r["ajuste_pontos"]), r["situacao"] or None)
    if bcl.get(k) != pv:
        dif += 1
        if dif < 15: print("class difere", k, bcl.get(k), pv)
print("class diferentes:", dif)
