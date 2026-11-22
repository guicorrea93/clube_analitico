"""Tabela final (módulo Football table: ganados_X, empates_X...) da Wikipédia es x soma dos jogos do pacote x classificacao_final.
Uso: python -I revisao/PY/wiki_tabela.py <json> <temporada>"""
import json, re, csv, sys
sys.path.insert(0, 'coleta/comum-sulamerica'); sys.path.insert(0, 'coleta/par-1')
from clubes_par import clube
arq, temp = sys.argv[1], sys.argv[2]; ano = int(temp[:4])
wt = json.load(open(arq, encoding='utf-8'))['parse']['wikitext']['*']
i = wt.find('Football table'); bloco = wt[i:wt.find('}}', wt.find('equipo1', i))]
nomes = {k: re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", v).replace("'''", '').strip() for k, v in re.findall(r"\|nombre_(\w+)\s*=\s*([^\n|]*(?:\|[^\n\]]*\]\])?)", bloco)}
W = {}
for k in nomes:
    d = {}
    for campo in ('ganados', 'empates', 'perdidos', 'gf', 'gc', 'ajustar_puntos'):
        m = re.search(rf"\|{campo}_{k}\s*=\s*(-?\d+)", bloco)
        d[campo] = int(m.group(1)) if m else 0
    W[clube(nomes[k], ano) or nomes[k]] = d
ordem = [x for _, x in sorted((int(a), b) for a, b in re.findall(r"\|equipo(\d+)\s*=\s*(\w+)", bloco))]
P = [p for p in csv.DictReader(open('data/coleta/par-1/pacote/partidas.csv', encoding='utf-8')) if p['temporada'] == temp and p['fase'] in ('Fase única', 'Primeira fase')]
S = {}
for p in P:
    if p['gols_mandante'] == '': continue
    gm, gv = int(p['gols_mandante']), int(p['gols_visitante'])
    for c, a, b in ((p['mandante'], gm, gv), (p['visitante'], gv, gm)):
        s = S.setdefault(c, [0, 0, 0, 0, 0]); s[0] += a > b; s[1] += a == b; s[2] += a < b; s[3] += a; s[4] += b
CF = {r['clube']: r for r in csv.DictReader(open('data/coleta/par-1/pacote/classificacao_final.csv', encoding='utf-8')) if r['temporada'] == temp}
n = 0
for k, cod in enumerate(ordem, 1):
    c = clube(nomes[cod], ano) or nomes[cod]
    w = W[c]; wv = [w['ganados'], w['empates'], w['perdidos'], w['gf'], w['gc']]
    s = S.get(c); cf = CF.get(c, {})
    cfv = [int(cf[x]) for x in ('vitorias', 'empates', 'derrotas', 'gols_pro', 'gols_contra')] if cf.get('vitorias') else None
    flag = '' if (wv == s and wv == cfv and str(k) == cf.get('posicao')) else '  <<<'
    if flag: n += 1
    print(f"{k:2d} {c:30s} wiki {wv} ajuste {w['ajustar_puntos']} | jogos {s} | class pos {cf.get('posicao')} {cfv}{flag}")
print(temp, ':', n, 'linhas diferentes')
