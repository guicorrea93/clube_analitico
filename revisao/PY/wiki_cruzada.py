"""Tabela de confrontos (L\V com siglas) da Wikipédia es x pacote. Uso: python -I revisao/PY/wiki_cruzada.py <json> <temporada>"""
import json, re, csv, sys
sys.path.insert(0, 'coleta/comum-sulamerica'); sys.path.insert(0, 'coleta/par-1')
from clubes_par import clube
arq, temp = sys.argv[1], sys.argv[2]; ano = int(temp[:4])
wt = json.load(open(arq, encoding='utf-8'))['parse']['wikitext']['*']
P = [p for p in csv.DictReader(open('data/coleta/par-1/pacote/partidas.csv', encoding='utf-8')) if p['temporada'] == temp]
ok = dif = 0; out = []
for tab in re.findall(r"\{\|.*?\n\|\}", wt, flags=re.S):
    sig = re.findall(r'span title="([^"]+)"[^>]*>(\w{2,4})</span>', tab)
    if len(sig) < 8: continue
    cols = [clube(t, ano) or t for t, s in sig]
    for row in re.split(r"\n\|-[^\n]*", tab)[1:]:
        cels = [l[1:] for l in row.split('\n') if l.startswith('|')]
        if not cels: continue
        m = re.search(r"\[\[([^\]|]*)\|?([^\]]*)\]\]", cels[0])
        if not m: continue
        mand = clube(m.group(1).replace('Club ', ''), ano) or clube(m.group(2), ano)
        for j, c in enumerate(cels[1:]):
            r = re.search(r"(\d+):(\d+)", c)
            if not r or j >= len(cols): continue
            gm, gv = int(r.group(1)), int(r.group(2)); vis = cols[j]
            cand = [p for p in P if p['mandante'] == mand and p['visitante'] == vis and p['fase'] in ('Fase única', 'Primeira fase')]
            if not cand: out.append(f'  SEM PAR {mand} {gm}:{gv} {vis}'); continue
            p = cand[0]
            if (p['gols_mandante'], p['gols_visitante']) == (str(gm), str(gv)): ok += 1
            else: dif += 1; out.append(f"  PLACAR wiki {mand} {gm}-{gv} {vis} | pacote {p['gols_mandante']}-{p['gols_visitante']} {p['data']} {p['resultado_especial']} {p['observacao'][:40]}")
print(f'{temp}: iguais {ok}, diferentes {dif}')
for l in out[:20]: print(l)
