"""Lê os confrontos (chaves) das páginas da Wikipédia (pt) de cada Copa do Brasil e compara com o pacote.

Formatos lidos: {{Torneio 32 equipas ida volta}} (RDn-timeXX, golsXXi/v), {{Tabela Copa do Brasil}} (faseN-timeXX,
gols1/gols2), {{TwoLegResult}}, {{OneLegResult}} e {{Footballbox}} (jogos com mando).
Saída: revisao/CB/saida_confrontos.txt (divergências) e um resumo na tela.
Uso: python -I revisao/CB/confrontos.py
"""
import csv
import collections
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = wiki.RAIZ
PAC = os.path.join(RAIZ, 'data', 'coleta', 'bra-copa-do-brasil', 'pacote')


def chave(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]', '', s)


# nome na Wikipédia (modelo {{Futebol X}}) -> nome no pacote, quando a regra automática não acha
MAPA = {
    'atleticopr': 'Athletico-PR', 'internacionalrs': 'Internacional', 'portuguesasp': 'Portuguesa',
    'guaranisp': 'Guarani', 'vasco': 'Vasco', 'botafogo': 'Botafogo', 'americamg': 'América-MG',
    'americarn': 'América-RN', 'santacruz': 'Santa Cruz', 'atleticogo': 'Atlético-GO',
    'atleticomg': 'Atlético-MG', 'flamengo': 'Flamengo', 'fluminense': 'Fluminense',
    'uniaorondonopolis': 'União-MT', 'operarioceov': 'CEOV Operário', 'fastclube': 'Fast-AM',
    'desportivaferroviaria': 'Desportiva-ES', 'ypirangadeerechim': 'Ypiranga-RS', 'parnahyba': 'Parnaíba',
    'saojosepoa': 'São José-RS', 'independentepa': 'Independente Tucuruí', 'humaita': 'SC Humaitá',
    'athletic': 'Athletic Club', 'redbullbragantino': 'Bragantino', 'votuporanguense': 'CA Votuporanguense',
    'riobrancovn': 'Rio Branco de Venda Nova', 'catubarao': 'Atlético Tubarão', 'atleticocajazeirense': 'Atlético-PB',
    'aguasanta': 'EC Água Santa', 'saofranciscoac': 'São Francisco FC-AC', 'setededourados': '7 de Setembro-MS',
    'romapr': 'Roma Apucarana', 'potyguarcn': 'Potyguar Seridoense', 'malutrom': 'J.Malucelli',
    'itapemirim': 'At. Itapemirim', 'guaranivA': 'Guarani V. Aires', 'guaraniva': 'Guarani V. Aires',
    'fluminensedefeira': 'Fluminense-BA', 'corintiansdecaico': 'Coríntians-RN', 'capitalto': 'Capital FC',
    'araguaina': 'Araguaína', 'audaxsp': 'Osasco Audax', 'adapgalomaringa': 'Galo Maringá', 'ituiutaba': 'Boa Esporte',
    'america': 'América-RJ', 'tocantinsdepalmas': 'Tocantins-TO', 'prudentopolis': 'Prudentópolis EC',
    'esportivoguara': 'Guará', 'uniclinic': 'Atlético Cearense', 'gremioprudente': 'Barueri',
}


def nome_wiki(cel):
    m = re.search(r'\{\{\s*Futebol\s+([^|}]+)', cel, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', cel)
    if m:
        return m.group(1).strip()
    return re.sub(r"[{}'\[\]]", '', cel).strip()


def italico_casa(cel):
    """Na Tabela Copa do Brasil, o time em itálico manda o 1º jogo."""
    c = re.sub(r"'''", '', cel)
    return "''" in c


def num(s):
    s = (s or '').strip()
    s = re.sub(r'\{\{\s*nowrap\s*\|', '', s, flags=re.I).replace('}}', '')
    m = re.match(r'(\d+)\s*(?:\((\d+)\))?', s)
    if not m:
        return None
    return int(m.group(1)), (int(m.group(2)) if m.group(2) else None)


def placar(s):
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s or '')
    m = re.search(r'(\d+)\s*[–-]\s*(\d+)', s)
    return (int(m.group(1)), int(m.group(2))) if m else None


def params(txt):
    d = {}
    ms = list(re.finditer(r'\|\s*([A-Za-z0-9_-]+)\s*=', txt))
    for k, m in enumerate(ms):
        fim = ms[k + 1].start() if k + 1 < len(ms) else len(txt)
        v = txt[m.end():fim]
        v = v.split('\n}}')[0]
        if m.group(1) not in d:
            d[m.group(1)] = v.strip()
    return d


def confrontos(ano):
    w = wiki.pt(ano) or ''
    out = []  # (A, B, [(ga, gb, penA, penB), ...], casa_ida) casa_ida = 'A'|'B'|None
    p = params(w)
    # Torneio 32 equipas: RDn-timeXX e RDn-golsXXi / golsXXv
    for k, v in p.items():
        m = re.match(r'RD(\d+)-time(\d+)$', k)
        if m and int(m.group(2)) % 2 == 1:
            r, i = m.group(1), int(m.group(2))
            j = i + 1
            a, b = v, p.get(f'RD{r}-time{j:02d}')
            if b is None:
                continue
            jogos = []
            for suf in ('i', 'v'):
                x, y = num(p.get(f'RD{r}-gols{i:02d}{suf}')), num(p.get(f'RD{r}-gols{j:02d}{suf}'))
                if x and y:
                    jogos.append((x[0], y[0], x[1], y[1]))
            out.append((nome_wiki(a), nome_wiki(b), jogos, None, f'RD{r}'))
    # Tabela Copa do Brasil: faseN-timeXX, gols1 / gols2
    for k, v in p.items():
        m = re.match(r'fase(\d+)-time(\d+)$', k)
        if m and int(m.group(2)) % 2 == 1:
            r, i = m.group(1), int(m.group(2))
            j = i + 1
            b = p.get(f'fase{r}-time{j:02d}')
            if b is None:
                continue
            jogos = []
            for suf in ('1', '2'):
                x, y = num(p.get(f'fase{r}-time{i:02d}-gols{suf}')), num(p.get(f'fase{r}-time{j:02d}-gols{suf}'))
                if x and y:
                    jogos.append((x[0], y[0], x[1], y[1]))
            casa = 'A' if italico_casa(v) else ('B' if italico_casa(b) else None)
            out.append((nome_wiki(v), nome_wiki(b), jogos, casa, f'fase{r}'))
    # TwoLegResult|A|x|agg|B|x|leg1|leg2  (A manda o 1º jogo)
    for m in re.finditer(r'\{\{TwoLegResult\|(.*)', w):
        partes = re.split(r'\|(?![^{]*\}\})(?![^\[]*\]\])', m.group(1).rsplit('}}', 1)[0])
        if len(partes) < 7:
            continue
        a, b = nome_wiki(partes[0]), nome_wiki(partes[3])
        l1, l2 = placar(partes[5]), placar(partes[6])
        pen = re.search(r'\((\d+)\s*[–-]\s*(\d+)', partes[2])
        jogos = []
        if l1:
            jogos.append((l1[0], l1[1], None, None))
        if l2:
            jogos.append((l2[0], l2[1], int(pen.group(1)) if pen else None, int(pen.group(2)) if pen else None))
        out.append((a, b, jogos, 'A', 'TwoLeg'))
    for m in re.finditer(r'\{\{OneLegResult\|(.*)', w):
        partes = re.split(r'\|(?![^{]*\}\})(?![^\[]*\]\])', m.group(1).rsplit('}}', 1)[0])
        if len(partes) < 4:
            continue
        a, b = nome_wiki(partes[0]), nome_wiki(partes[3])
        l1 = placar(partes[2])
        pen = re.search(r'\((\d+)\s*[–-]\s*(\d+)', partes[2])
        if l1:
            out.append((a, b, [(l1[0], l1[1], int(pen.group(1)) if pen else None, int(pen.group(2)) if pen else None)], 'A', 'OneLeg'))
    return out


def footballboxes(ano):
    w = wiki.pt(ano) or ''
    res = []
    for m in re.finditer(r'\{\{\s*[Ff]ootballbox(.*?)\n\}\}', w, re.S):
        p = params(m.group(1))
        t1, t2, pl = p.get('time1') or p.get('team1'), p.get('time2') or p.get('team2'), p.get('placar') or p.get('score')
        if not (t1 and t2 and pl):
            continue
        sc = placar(pl)
        pen = p.get('penaltis1') or p.get('penalties1') or ''
        pen2 = p.get('penaltis2') or p.get('penalties2') or ''
        res.append((nome_wiki(t1), nome_wiki(t2), sc, pl, (pen, pen2)))
    return res


def pacote():
    P = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(PAC, 'partidas.csv'), encoding='utf-8')):
        P[int(r['temporada'])].append(r)
    return P


def casar(nome, clubes):
    k = chave(nome)
    if k in MAPA and MAPA[k] in clubes:
        return MAPA[k]
    cand = [c for c in clubes if chave(c) == k]
    if cand:
        return cand[0]
    k2 = re.sub(r'(rs|sp|rj|mg|pr|sc|ba|pe|ce|go|df|pa|am|rn|pb|al|se|pi|ma|mt|ms|es|to|ro|ac|ap|rr)$', '', k)
    cand = [c for c in clubes if chave(c) == k2 or chave(c).startswith(k) or k.startswith(chave(c)) and len(chave(c)) > 4]
    if len(cand) == 1:
        return cand[0]
    cand = [c for c in clubes if re.sub(r'(rs|sp|rj|mg|pr|sc|ba|pe|ce|go|df|pa|am|rn|pb|al|se|pi|ma|mt|ms|es|to|ro|ac|ap|rr)$', '', chave(c)) == k2]
    if len(cand) == 1:
        return cand[0]
    return None


def confrontos_en(ano):
    e = wiki.en(ano) or ''
    out = []
    for blo in re.finditer(r'\{\{\s*\d+TeamBracket(.*?)\n\}\}', e, re.S):
        p = params(blo.group(1))
        for k, v in p.items():
            m = re.match(r'RD(\d+)-team(\d+)$', k)
            if m and int(m.group(2)) % 2 == 1:
                r, i = m.group(1), int(m.group(2)); j = i + 1
                b = p.get(f'RD{r}-team{j:02d}')
                if b is None:
                    continue
                jogos = []
                for suf in ('-1', '-2'):
                    x, y = num(p.get(f'RD{r}-score{i:02d}{suf}')), num(p.get(f'RD{r}-score{j:02d}{suf}'))
                    if x and y:
                        jogos.append((x[0], y[0], x[1], y[1]))
                if not jogos:
                    sx = re.sub(r'<[^>]+>|\{\{[^}]*\}\}', ' ', p.get(f'RD{r}-score{i:02d}', ''))
                    sy = re.sub(r'<[^>]+>|\{\{[^}]*\}\}', ' ', p.get(f'RD{r}-score{j:02d}', ''))
                    lx = re.findall(r'(\d+)(?:\s*\((\d+)\))?', sx)
                    ly = re.findall(r'(\d+)(?:\s*\((\d+)\))?', sy)
                    for (gx, px), (gy, py) in zip(lx, ly):
                        jogos.append((int(gx), int(gy), int(px) if px else None, int(py) if py else None))
                out.append((nome_en(v), nome_en(b), jogos, None, f'en RD{r}'))
    return out


def nome_en(cel):
    m = re.search(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', cel)
    n = m.group(1) if m else re.sub(r"[{}'\[\]†*]", '', cel)
    n = re.sub(r'\s*\(([A-Z]{2})\)\s*$', r'-', n.strip())
    return {'Vasco da Gama': 'Vasco', 'Atlético Mineiro': 'Atlético-MG', 'Atlético Paranaense': 'Athletico-PR',
            'Athletico Paranaense': 'Athletico-PR', 'Atlético Goianiense': 'Atlético-GO', 'América Mineiro': 'América-MG',
            'Ulbra Ji-Paraná-RO': 'Ulbra-RO', 'Vasco da Gama-RJ': 'Vasco', 'Corinthians Paranaense': 'J.Malucelli'}.get(n.strip(), n.strip())


if __name__ == '__main__':
    import sys as _s
    EN = len(_s.argv) > 1 and _s.argv[1] == 'en'
    if EN:
        confrontos = confrontos_en
    P = pacote()
    linhas = []
    tot = collections.Counter()
    for ano in range(1989, 2026):
        jogos = P[ano]
        clubes = sorted({r['mandante'] for r in jogos} | {r['visitante'] for r in jogos})
        par = collections.defaultdict(list)
        for r in jogos:
            par[frozenset((r['mandante'], r['visitante']))].append(r)
        usados = set()
        for a, b, lst, casa, fonte in confrontos(ano):
            ca, cb = casar(a, clubes), casar(b, clubes)
            if bool(ca) != bool(cb):
                conhecido = ca or cb
                wk0 = sorted((x[0], x[1]) if ca else (x[1], x[0]) for x in lst)
                cands = set()
                for r in jogos:
                    if conhecido in (r['mandante'], r['visitante']):
                        outro = r['visitante'] if r['mandante'] == conhecido else r['mandante']
                        pk0 = sorted((int(q['gols_mandante']), int(q['gols_visitante'])) if q['mandante'] == conhecido else (int(q['gols_visitante']), int(q['gols_mandante'])) for q in par[frozenset((conhecido, outro))])
                        if pk0 == wk0:
                            cands.add(outro)
                if len(cands) == 1:
                    o = cands.pop()
                    linhas.append(f'{ano} NOME-POR-PLACAR wiki "{b if ca else a}" = pacote "{o}"')
                    if ca: cb = o
                    else: ca = o
            if not ca or not cb:
                linhas.append(f'{ano} NOME? {a}->{ca} x {b}->{cb} ({fonte})')
                tot['nome'] += 1
                continue
            pk = par.get(frozenset((ca, cb)), [])
            usados.add(frozenset((ca, cb)))
            # placares do pacote vistos do lado A
            pac = sorted((int(r['gols_mandante']), int(r['gols_visitante'])) if r['mandante'] == ca else (int(r['gols_visitante']), int(r['gols_mandante'])) for r in pk)
            wk = sorted((x[0], x[1]) for x in lst)
            tot['confrontos'] += 1
            tot['jogos_wiki'] += len(wk)
            if pac == wk:
                tot['ok'] += 1
                # mando do 1º jogo (quando a fonte diz)
                if casa and len(pk) == 2 and len(lst) == 2:
                    pk_ord = sorted(pk, key=lambda r: r['data'])
                    casa_pk = 'A' if pk_ord[0]['mandante'] == ca else 'B'
                    l1 = lst[0]
                    p1 = pk_ord[0]
                    g1 = (int(p1['gols_mandante']), int(p1['gols_visitante'])) if p1['mandante'] == ca else (int(p1['gols_visitante']), int(p1['gols_mandante']))
                    if (l1[0], l1[1]) != g1:
                        linhas.append(f'{ano} ORDEM {ca} x {cb}: wiki 1º jogo {l1[0]}-{l1[1]} (casa {casa}), pacote 1º jogo {g1} em casa de {p1["mandante"]} ({fonte})')
                        tot['ordem'] += 1
                # pênaltis
                for x in lst:
                    if x[2] is not None:
                        alvo = [r for r in pk if ((int(r['gols_mandante']), int(r['gols_visitante'])) if r['mandante'] == ca else (int(r['gols_visitante']), int(r['gols_mandante']))) == (x[0], x[1])]
                        if alvo and not alvo[-1]['penaltis_mandante']:
                            linhas.append(f'{ano} PENALTIS-FALTA {ca} x {cb} {x[0]}-{x[1]} pen {x[2]}-{x[3]} ({fonte}); pacote sem pênaltis')
                            tot['pen_falta'] += 1
            else:
                linhas.append(f'{ano} PLACAR {ca} x {cb}: wiki {wk} | pacote {pac} ({fonte}) [{";".join(r["id"]+" "+r["fase"] for r in pk)}]')
                tot['dif'] += 1
        # jogos do pacote sem confronto na wiki
        sobra = [r for r in jogos if frozenset((r['mandante'], r['visitante'])) not in usados]
        tot['sem_wiki'] += len(sobra)
        if usados:
            for r in sobra:
                linhas.append(f'{ano} SO-PACOTE {r["id"]} {r["fase"]} {r["data"]} {r["mandante"]} {r["gols_mandante"]}-{r["gols_visitante"]} {r["visitante"]}')
        else:
            linhas.append(f'{ano} SEM-CHAVE-NA-WIKI ({len(jogos)} jogos)')
    open(os.path.join(r'C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/RC', 'cb_confrontos' + ('_en' if EN else '') + '.txt'), 'w', encoding='utf-8').write('\n'.join(linhas))
    print(tot)
