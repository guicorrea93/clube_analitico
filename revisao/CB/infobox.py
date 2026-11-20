"""Extrai da infobox (pt e en) de cada edição: campeão, vice, jogos, gols, artilheiro."""
import re, sys, json
sys.path.insert(0, __import__('os').path.dirname(__file__))
import wiki
sys.stdout.reconfigure(encoding='utf-8')

def campos(txt, chaves):
    out = {}
    for k in chaves:
        m = re.search(r'\|\s*' + k + r'\s*=\s*(.*)', txt)
        out[k] = m.group(1).strip() if m else None
    return out

def limpa(s):
    if s is None: return None
    s = re.sub(r'<ref[^>]*/>', '', s); s = re.sub(r'<ref.*?</ref>', '', s)
    s = re.sub(r'\{\{(?:Futebol|fb|fbw|fbaicon|fbicon|flagicon|Futebol)\s+([^|}]+)[^}]*\}\}', r'\1', s, flags=re.I)
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r'<[^>]+>', ' ', s); s = re.sub(r'\{\{[^}]*\}\}', '', s)
    return re.sub(r'\s+', ' ', s).strip()

res = {}
for ano in range(1989, 2026):
    p = wiki.pt(ano) or ''
    e = wiki.en(ano) or ''
    a = {k: limpa(v) for k, v in campos(p, ['campeão', 'vicecampeão', 'vice-campeão', 'jogos', 'golos', 'gols', 'artilheiro']).items()}
    b = {k: limpa(v) for k, v in campos(e, ['champions', 'runner-up', 'runners-up', 'matches', 'goals', 'top_scorer', 'top_goal_scorer']).items()}
    res[ano] = {'pt': a, 'en': b}
    print(ano, 'PT', a)
    print(ano, 'EN', b)
json.dump(res, open(__import__('os').path.join(wiki.CACHE, '..', '..', '..', '..', 'revisao', 'CB', 'infobox.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
