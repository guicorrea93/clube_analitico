import csv, glob, collections, sqlite3, os
d = collections.defaultdict(set)
for f in glob.glob('data/coleta/*/pacote/clubes.csv'):
    slug = os.path.normpath(f).split(os.sep)[2]
    for r in csv.DictReader(open(f, encoding='utf-8')):
        d[r['clube']].add((slug, r['pais'], r['cidade']))
fr = [r['clube'] for r in csv.DictReader(open('data/coleta/fra-1/pacote/clubes.csv', encoding='utf-8'))]
for c in fr:
    paises = {p for _, p, _ in d[c]}
    if len(paises) > 1 or any(p not in ('FRA', 'MON') for p in paises):
        print('pacotes', c, d[c])
con = sqlite3.connect('file:db/futebol.db?mode=ro', uri=True)
cols = [r[1] for r in con.execute('pragma table_info(clube)')]
print(cols)
for c in fr:
    rows = con.execute('select * from clube where nome=?', (c,)).fetchall()
    if len(rows) != 1: print('banco', c, rows)
# nomes parecidos no banco (mesmo nome sem acento / prefixos)
import unicodedata, re
def k(s): return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())
todos = con.execute('select clube_id, nome, pais_id from clube').fetchall()
idx = collections.defaultdict(list)
for i, n, p in todos: idx[k(n)].append((i, n, p))
for c in fr:
    if len(idx[k(c)]) > 1: print('parecido', c, idx[k(c)])
