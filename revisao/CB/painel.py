import json, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def carregar(slug='bra-copa-do-brasil'):
    s = open(os.path.join(RAIZ, 'painel', 'dados', slug + '.js'), encoding='utf-8').read()
    s = s[s.index('=') + 1:].strip().rstrip(';')
    return json.loads(s)
