"""Datas dos jogos com quadro (Footballbox) na Wikipédia pt x pacote (mesmo par de clubes e mesmo mando)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki
from confrontos import params, nome_wiki, pacote, casar, placar
sys.stdout.reconfigure(encoding='utf-8')
MES = {m: i + 1 for i, m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split())}
P = pacote(); n = ok = 0
for ano in range(1989, 2026):
    w = wiki.pt(ano) or ''
    jogos = P[ano]; clubes = sorted({r['mandante'] for r in jogos} | {r['visitante'] for r in jogos})
    for m in re.finditer(r'\{\{\s*[Ff]ootballbox(.*?)\n\}\}', w, re.S):
        p = params(m.group(1))
        dt = re.sub(r'[\[\]]', '', p.get('data', '') or p.get('date', ''))
        x = re.search(r'(\d{1,2})\s*(?:º)?\s*de\s*([a-zç]+)(?:\s*de\s*(\d{4}))?', dt.lower())
        a, b = casar(nome_wiki(p.get('time1', '')), clubes), casar(nome_wiki(p.get('time2', '')), clubes)
        if not (x and a and b and x.group(2) in MES):
            continue
        cand = [r for r in jogos if r['mandante'] == a and r['visitante'] == b]
        if not cand:
            continue
        n += 1
        alvo = (int(x.group(3)) if x.group(3) else None, MES[x.group(2)], int(x.group(1)))
        achou = any(int(r['data'][5:7]) == alvo[1] and int(r['data'][8:10]) == alvo[2] for r in cand)
        if achou:
            ok += 1
        else:
            print(ano, a, 'x', b, 'wiki', dt.strip()[:30], '| pacote', [r['data'] for r in cand])
print('quadros com data:', n, 'datas iguais:', ok)
