import json, os, re
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CACHE = os.path.join(RAIZ, 'data', 'cache', 'revisao', 'CB')
def texto(lang, titulo):
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", titulo)[:180]
    for arq in (f'raw_{lang}_{base}.txt', f'wiki_{lang}_{base}.json'):
        p = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9._-]+", "_", arq))
        if os.path.exists(p):
            s = open(p, encoding='utf-8').read()
            if arq.endswith('.json'):
                s = json.loads(s)['parse']['wikitext']['*']
            return s
    return None
def pt(ano): return texto('pt', f'Copa do Brasil de Futebol de {ano}')
def en(ano): return texto('en', f'{ano} Copa do Brasil')
