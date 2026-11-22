"""Artilheiro de cada edição: pacote (artilheiros.csv) x Wikipédia es (coluna Goleador de "Títulos de Liga por año")."""
import json, re, csv, unicodedata
from collections import defaultdict
W = json.load(open('data/cache/revisao/PY/wiki-es-primera.json', encoding='utf-8'))['parse']['wikitext']['*']
sec = W[W.index('=== Títulos de Liga por año'):W.index('== Palmarés')]
sec = re.sub(r"<ref.*?(</ref>|/>)", "", sec, flags=re.S)
def k(s): return re.sub(r'[^a-z ]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()).split()
res = {}; ano = None
for bloco in re.split(r"\n\|-", sec):
    m = re.search(r"'''(?:\[\[[^\]|]*\|)?(\d{4})(?:\]\])?'''", bloco)
    if m: ano = m.group(1)
    tor = ' Apertura' if re.search(r"\|Apertura\]\]", bloco) else (' Clausura' if re.search(r"\|Clausura\]\]", bloco) else '')
    if not ano: continue
    gs = re.findall(r"(?:\[\[(?:[^\]|]*\|)?([^\]]+)\]\]|([A-ZÁÉÍÓÚ][\w\.áéíóúñ ]+?))\s*[-–]\s*(\d{1,2})\b", bloco)
    if gs: res[ano + tor] = [(a or b, int(n)) for a, b, n in gs]
P = defaultdict(list)
for r in csv.DictReader(open('data/coleta/par-1/pacote/artilheiros.csv', encoding='utf-8')):
    P[r['temporada']].append((r['jogador'], int(r['gols']), r['clube'], r['fonte']))
ok = dif = so_w = so_p = 0
for t in sorted(set(P) | set(res)):
    p, w = P.get(t), res.get(t)
    if not p: so_w += 1; print('SÓ WIKI', t, w); continue
    if not w: so_p += 1; continue
    # casa por sobrenome
    gp = max(x[1] for x in p); gw = max(x[1] for x in w)
    nomes_p = {k(x[0])[-1] for x in p if k(x[0])}; nomes_w = {k(x[0])[-1] for x in w if k(x[0])}
    if gp == gw and nomes_p & nomes_w: ok += 1
    else:
        dif += 1; print('DIF', t, '| pacote', [(x[0], x[1], x[2]) for x in p], '| wiki', w)
print(f'iguais {ok}, diferentes {dif}, só wiki {so_w}, só pacote {so_p}')
