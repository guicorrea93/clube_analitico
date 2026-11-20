"""Semifinalistas de cada edição pela Wikipédia (en: chave; pt: seção Semifinais) x painel (top 4 da classificação)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki
from painel import carregar
from confrontos import nome_wiki, casar, pacote
sys.stdout.reconfigure(encoding='utf-8')

def nomes_en(cel):
    m = re.search(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', cel)
    return (m.group(1) if m else re.sub(r"[{}'\[\]†*]", '', cel)).strip()

def semis_en(ano):
    e = wiki.en(ano) or ''
    blocos = list(re.finditer(r'\{\{\s*\d+TeamBracket', e))
    if not blocos:
        return None
    b = e[blocos[-1].start():]
    rds = sorted({int(x) for x in re.findall(r'RD(\d+)-team', b)})
    if len(rds) < 2:
        return None
    sf = rds[-2]
    return [nomes_en(m.group(1)) for m in re.finditer(r'RD%d-team\d+\s*=\s*([^\n]*)' % sf, b)]

def semis_pt(ano):
    w = wiki.pt(ano) or ''
    i = re.search(r'==+\s*Semifina[^=]*==+', w)
    if not i:
        return None
    j = re.search(r'\n==+\s*Final', w[i.end():])
    sec = w[i.end(): i.end() + (j.start() if j else 3000)]
    ts = []
    for m in re.finditer(r'\{\{\s*Futebol\s+([^|}]+)', sec):
        if m.group(1).strip() not in ts:
            ts.append(m.group(1).strip())
    return ts[:4] if ts else None

P = pacote()
d = carregar()
for e in d['EDS']:
    ano = e['ano']
    clubes = sorted({r['mandante'] for r in P[ano]} | {r['visitante'] for r in P[ano]})
    en = semis_en(ano); pt = semis_pt(ano)
    fonte = en or pt
    top4 = [r[0] for r in e['tab'][:4]]
    ed = [x for x in d['ED'] if x['ano'] == ano][0]
    print(ano, 'EN:', en, '| PT:', pt, '| painel top4:', top4, '| ED:', ed['campeao'], ed['vice'], ed['terceiro'])
