"""Confere mando e placar de cada jogo com quadro (Footballbox) nas páginas pt da Wikipédia."""
import os, sys, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from confrontos import footballboxes, pacote, casar
sys.stdout.reconfigure(encoding='utf-8')
P = pacote()
tot = collections.Counter()
for ano in range(1989, 2026):
    jogos = P[ano]
    clubes = sorted({r['mandante'] for r in jogos} | {r['visitante'] for r in jogos})
    for t1, t2, sc, bruto, pen in footballboxes(ano):
        a, b = casar(t1, clubes), casar(t2, clubes)
        if not (a and b and sc):
            tot['sem_nome'] += 1
            continue
        tot['quadros'] += 1
        exato = [r for r in jogos if r['mandante'] == a and r['visitante'] == b and (int(r['gols_mandante']), int(r['gols_visitante'])) == sc]
        if exato:
            tot['ok'] += 1
            continue
        mesmo = [r for r in jogos if {r['mandante'], r['visitante']} == {a, b}]
        print(ano, f'wiki {a} {sc[0]}-{sc[1]} {b} | pacote:', '; '.join(f"{r['id']} {r['data']} {r['mandante']} {r['gols_mandante']}-{r['gols_visitante']} {r['visitante']}" for r in mesmo))
        tot['dif'] += 1
print(tot)
