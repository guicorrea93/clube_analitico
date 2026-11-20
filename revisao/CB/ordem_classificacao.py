"""Sanidade da classificação final (copa): quem saiu depois (último jogo mais tarde) deve ficar acima de quem saiu antes.
Conta, por edição, clubes que ficaram abaixo de outro clube eliminado pelo menos 20 dias antes."""
import os, sys, csv, collections, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from confrontos import pacote, PAC
sys.stdout.reconfigure(encoding='utf-8')
P = pacote()
C = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(PAC, 'classificacao_final.csv'), encoding='utf-8')):
    C[int(r['temporada'])].append((int(r['posicao']), r['clube']))
d = lambda s: datetime.date.fromisoformat(s)
for ano in sorted(C):
    ult = {}
    for r in P[ano]:
        for c in (r['mandante'], r['visitante']):
            if r['data'] and (c not in ult or r['data'] > ult[c]):
                ult[c] = r['data']
    cl = sorted(C[ano])
    ruins = []
    for i, (p, c) in enumerate(cl):
        acima = [c2 for p2, c2 in cl[:i] if (d(ult[c]) - d(ult[c2])).days >= 20]
        if acima:
            ruins.append(f'{c} {p}º (saiu {ult[c]}) abaixo de {len(acima)} eliminados antes')
    print(ano, len(ruins), '; '.join(ruins[:3]))
