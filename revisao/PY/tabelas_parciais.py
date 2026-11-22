"""Anos sem jogos: linhas da tabela final da RSSSF (parahist.html e páginas para68..para95) x linhas da classificação do pacote.
Leitor independente: bloco que começa em 'Final Table' / 'Table at Abandonment' / 'Final Standings' / 'Final table' e vai até a
primeira linha em branco; conta as linhas de clube com ou sem número de posição."""
import csv, re, sys
from collections import defaultdict
sys.path.insert(0, 'coleta/comum-sulamerica')
import rsssf_sul
from pathlib import Path
P = Path('data/coleta/par-1/rsssf')
hist = rsssf_sul.texto(P / 'parahist.html')
def secao(ano):
    ini = next((i for i, l in enumerate(hist) if l.strip() == str(ano)), None)
    if ini is not None:
        fim = next((i for i in range(ini + 1, len(hist)) if re.fullmatch(r"\d{4}", hist[i].strip())), len(hist))
        return 'parahist', hist[ini:fim], ini
    pg = P / f'para{ano % 100:02d}.html'
    if pg.exists():
        return pg.stem, rsssf_sul.texto(pg), 0
    return None, [], 0
LIN = re.compile(r"^\s{0,3}(\d{1,2}\s*\.)?\s*([A-Za-zÁÉÍÓÚÑáéíóúñü][^\d]*?)\s{2,}([\d\s\-]+?)\s*(\S.*)?$")
cf = defaultdict(list)
for r in csv.DictReader(open('data/coleta/par-1/pacote/classificacao_final.csv', encoding='utf-8')):
    cf[r['temporada']].append(r)
ed = {r['temporada']: r for r in csv.DictReader(open('data/coleta/par-1/pacote/edicoes.csv', encoding='utf-8'))}
saida = []
for t, r in ed.items():
    if not r['formato'].startswith('sem jogos'): continue
    ano = int(t)
    pg, ls, base = secao(ano)
    blocos = []
    i = 0
    while i < len(ls):
        if re.match(r"^\s*(Final [Tt]able|Table at Abandonment|Final Standings|Top Final Table|Final Table)", ls[i]) or re.match(r"^\s*Final [Tt]able", ls[i]):
            j = i + 1
            while j < len(ls) and not ls[j].strip(): j += 1
            linhas = []
            while j < len(ls) and ls[j].strip():
                m = LIN.match(ls[j])
                if m: linhas.append((m.group(1), m.group(2).strip(), base + j))
                j += 1
            blocos.append((ls[i].strip(), linhas))
            i = j
        i += 1
    n_pac = len(cf[t])
    n_rs = max((len(b[1]) for b in blocos), default=0)
    if n_rs != n_pac:
        saida.append((t, n_pac, n_rs, pg, [b[0] + f' ({len(b[1])} linhas, 1ª linha {b[1][0][2] if b[1] else "-"})' for b in blocos]))
for s in saida: print(s)
print(len(saida), 'edições sem jogos com número de linhas diferente')
