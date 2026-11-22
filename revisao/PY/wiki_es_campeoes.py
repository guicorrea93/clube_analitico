"""Campeão, vice e 3º por edição na Wikipédia em espanhol (Primera División de Paraguay, "Títulos de Liga por año")
x pacote (edicoes.csv e classificacao_final.csv) x RSSSF parachamp (via coleta/par-1/ler_rsssf.vices)."""
import json, re, csv, sys, unicodedata
sys.path.insert(0, 'coleta/comum-sulamerica'); sys.path.insert(0, 'coleta/par-1')
W = json.load(open('data/cache/revisao/PY/wiki-es-primera.json', encoding='utf-8'))['parse']['wikitext']['*']
sec = W[W.index('=== Títulos de Liga por año'):W.index('== Palmarés')]
MAP = {'Guaraní': 'Guaraní de Asunción', 'Nacional': 'Nacional de Asunción', 'River Plate': 'River Plate de Asunción'}
def links(s):
    out = []
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", s):
        out.append((m.group(1), (m.group(2) or m.group(1)).strip()))
    return out
def clube(alvo, txt):
    return MAP.get(txt, txt)
res = {}
ano = None
for bloco in re.split(r"\n\|-", sec):
    m = re.search(r"'''(?:\[\[[^\]|]*\|)?(\d{4})(?:\]\])?'''", bloco)
    if m: ano = m.group(1)
    tor = ''
    if re.search(r"\|Apertura\]\]", bloco): tor = ' Apertura'
    elif re.search(r"\|Clausura\]\]", bloco): tor = ' Clausura'
    clubs = [ (a, t) for a, t in links(bloco) if a.startswith('Club ') or 'Sport Club' in a or a.startswith('Atlético') or a in ('Sportivo Luqueño',) ]
    if not ano or len(clubs) < 2 or 'no disputado' in bloco: continue
    linha_tit = bloco.split('\n')
    # campeão: primeiro clube; vice e 3º: os dois da linha seguinte "|N|| vice || 3º"
    m2 = re.search(r"\n\|\s*\d+\s*\|\|(.*)", bloco)
    if not m2: continue
    resto = [t for a, t in links(m2.group(1))]
    camp = [t for a, t in links(bloco.split(m2.group(0))[0]) if not a.startswith(('Campeonato', 'Torneo'))]
    t = ano + tor
    res[t] = (MAP.get(camp[-1], camp[-1]) if camp else '', [MAP.get(x, x) for x in resto[:2]], m2.group(1)[:200])
json.dump(res, open('revisao/PY/wiki_es_campeoes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from ler_rsssf import vices, campeoes
VR = vices(); CR = campeoes()
from clubes_par import clube as cl
ed = {r['temporada']: r for r in csv.DictReader(open('data/coleta/par-1/pacote/edicoes.csv', encoding='utf-8'))}
cf = {}
for r in csv.DictReader(open('data/coleta/par-1/pacote/classificacao_final.csv', encoding='utf-8')):
    cf.setdefault(r['temporada'], {})[int(r['posicao'])] = r['clube']
print('edições na Wikipédia es:', len(res), '; no pacote:', len(ed))
ruins = []
for t, r in ed.items():
    w = res.get(t)
    if not w: print('SEM WIKI', t); continue
    vr = VR.get(t, '')
    vrs = [cl(x.strip(), int(t[:4])) or x for x in re.split(r"\s+and\s+|,\s*", vr) if x.strip()]
    camp_ok = (r['campeao'] == w[0] == cf[t].get(1))
    vice_pac = r['vice']; vice_w = w[1][0] if w[1] else ''; ter_w = w[1][1] if len(w[1]) > 1 else ''
    vice_ok = vice_pac == vice_w and vice_pac in vrs
    ter_ok = cf[t].get(3, '') == ter_w
    if not (camp_ok and vice_ok):
        ruins.append(t)
        print(f"{t:14s} pac camp={r['campeao']!s:22s} 1ºclass={cf[t].get(1)!s:22s} | vice pac={vice_pac!s:22s} wiki-es={vice_w!s:22s} rsssf={vrs} | 3º class={cf[t].get(3,'')} wiki={ter_w}")
print(len(ruins), 'edições com campeão ou vice diferente:', ' '.join(ruins))
