"""Painel local (painel/dados/ecu-1.js) x banco: campeão/vice/3º, jogos e gols por edição, tabela da classificação."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import json, sqlite3, collections
t = open("painel/dados/ecu-1.js", encoding="utf-8").read(); d = json.loads(t[t.index("{"):].rstrip().rstrip(";"))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
cid = c.execute("select competicao_id from competicao where slug='ecu-1'").fetchone()[0]
pos = collections.defaultdict(dict)
for tmp, cl, p in c.execute("select e.temporada, clube_id, posicao from classificacao_final join edicao e using(edicao_id) where competicao_id=?", (cid,)):
    pos[tmp][p] = nome[cl]
jg = {tmp: (n, g) for tmp, n, g in c.execute("""select e.temporada, count(*), sum(coalesce(gols_mandante,0)+coalesce(gols_visitante,0)) from partida p join edicao e using(edicao_id)
          where competicao_id=? and gols_mandante is not null group by 1""", (cid,))}
dif = 0
for ed, eds in zip(d["ED"], d["EDS"]):
    tmp = eds["id"]
    if (ed["campeao"], ed["vice"], ed["terceiro"]) != (pos[tmp].get(1), pos[tmp].get(2), pos[tmp].get(3)):
        dif += 1; print("pódio", tmp, ed, pos[tmp].get(1), pos[tmp].get(2), pos[tmp].get(3))
    if (eds["j"], eds["g"]) != jg.get(tmp):
        dif += 1; print("jogos/gols", tmp, eds["j"], eds["g"], jg.get(tmp))
    tab = [r[0] for r in eds["tab"]]
    if tab != [pos[tmp][k] for k in sorted(pos[tmp])]:
        dif += 1; print("tabela", tmp)
print("edições:", len(d["EDS"]), "diferenças:", dif)
