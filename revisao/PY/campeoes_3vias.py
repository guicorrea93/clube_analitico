"""Campeão/vice/3º: pacote (edicoes.csv e classificacao_final.csv) x banco x painel local x site."""
import csv, sqlite3, sys
sys.path.insert(0, 'revisao/PY')
from carregar import carregar
P = 'data/coleta/par-1/pacote/'
ed = list(csv.DictReader(open(P+'edicoes.csv', encoding='utf-8')))
cf = list(csv.DictReader(open(P+'classificacao_final.csv', encoding='utf-8')))
pos = {}
for r in cf: pos.setdefault(r['temporada'], {})[int(r['posicao'])] = pos.get(r['temporada'],{}).get(int(r['posicao']), []) + [r['clube']]
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
db = {}
for t, p, n in c.execute("""select e.temporada, cf.posicao, cl.nome from classificacao_final cf join edicao e using(edicao_id)
   join competicao co using(competicao_id) join clube cl using(clube_id) where co.slug='par-1'"""):
    db.setdefault(t, {}).setdefault(p, []).append(n)
loc = carregar('painel/dados/par-1.js'); site = carregar('data/cache/revisao/PY/site-par-1.js')
def chave(e): return f"{e['ano']}{(' '+e['comp']) if e['comp'] else ''}"
L = {chave(e): e for e in loc['ED']}; S = {chave(e): e for e in site['ED']}
n = 0
for e in ed:
    t = e['temporada']
    pk = (e['campeao'], e['vice'])
    cfk = (pos.get(t, {}).get(1, ['-'])[0], pos.get(t, {}).get(2, ['-'])[0])
    dbk = (db.get(t, {}).get(1, ['-'])[0], db.get(t, {}).get(2, ['-'])[0])
    lk = (L[t].get('campeao'), L[t].get('vice') or '')
    sk = (S[t].get('campeao'), S[t].get('vice') or '')
    rep = {p: v for p, v in pos.get(t, {}).items() if len(v) > 1}
    if len({pk, cfk, dbk, lk}) > 1 or lk != sk or rep:
        n += 1
        print(t, '| ed', pk, '| cf', cfk, '| db', dbk, '| painel', lk, '| site', sk, '| pos repetida', rep)
print(n, 'edições com diferença')
