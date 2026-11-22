"""1960-1967 e 1981: classificação do pacote x tabela final do campeonato (última 'Final Table' antes dos playoffs) na RSSSF."""
import csv, re, sys
sys.path.insert(0, 'coleta/comum-sulamerica'); sys.path.insert(0, 'coleta/par-1')
import rsssf_sul
from clubes_par import clube
from pathlib import Path
INI = {'1960': 13, '1961': 13, '1962': 98, '1963': 83, '1964': 127, '1965': 217, '1966': 109, '1967': 13, '1981': 126}
CF = {}
for r in csv.DictReader(open('data/coleta/par-1/pacote/classificacao_final.csv', encoding='utf-8')):
    CF.setdefault(r['temporada'], []).append(r)
for t, ini in INI.items():
    L = rsssf_sul.texto(Path(f'data/coleta/par-1/rsssf/para{t[2:]}.html'))
    fins = [i for i in range(ini, len(L)) if re.match(r'^\s*Final Table', L[i])]
    # última Final Table antes de Topscorers
    top = next((i for i in range(ini, len(L)) if re.match(r'^\s*Topscorers', L[i])), len(L))
    fins = [i for i in fins if i < top] or fins
    f = fins[-1]
    rows = []
    for l in L[f + 1:f + 25]:
        m = re.match(r'^\s*(\d{1,2})?\.?([A-Za-zÁÉÍÓÚÑáéíóúñü][^\d]+?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)-\s*(\d+)\s+(\d+)', l)
        if m: rows.append((clube(m.group(2).strip(), int(t)) or m.group(2).strip(), [int(m.group(k)) for k in range(3, 10)]))
    pac = [(r['clube'], [int(r[x]) if r[x] else None for x in ('jogos', 'vitorias', 'empates', 'derrotas', 'gols_pro', 'gols_contra', 'pontos')]) for r in sorted(CF[t], key=lambda r: int(r['posicao']))]
    dif_pos = [k + 1 for k, (a, b) in enumerate(zip(rows, pac)) if a[0] != b[0]]
    dif_num = [a[0] for a, b in zip(sorted(rows), sorted(pac)) if a[1] != b[1]]
    print(f"{t}: RSSSF linha {f} ({len(rows)} clubes) | posições diferentes: {dif_pos} | números diferentes: {len(dif_num)} clubes")
    if dif_pos or dif_num:
        print('    RSSSF :', [(c, v[-1]) for c, v in rows])
        print('    pacote:', [(c, v[-1]) for c, v in pac])
