"""Jogos das páginas de temporada da Wikipédia em espanhol (tabelas "Fecha N" com Local/Resultado/Visitante/Día) x pacote.
Uso: python -I revisao/PY/wiki_jogos.py <arquivo json em data/cache/revisao/PY> <temporada do pacote> [ano]"""
import json, re, csv, sys, unicodedata
sys.path.insert(0, 'coleta/comum-sulamerica'); sys.path.insert(0, 'coleta/par-1')
from clubes_par import clube
MES = {m: i + 1 for i, m in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'])}
MES['setiembre'] = 9
def limpa(c):
    c = re.sub(r"<ref.*?(</ref>|/>)", "", c, flags=re.S)
    c = re.sub(r"\{\{[^{}]*\}\}", "", c)
    if '|' in c and not c.strip().startswith('[['):
        # atributos: bgcolor=... | texto
        partes = re.split(r"\|(?![^\[]*\]\])", c)
        c = partes[-1]
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", c)
    return re.sub(r"'''?|<[^>]+>", "", c).strip()
def jogos(wt, ano):
    out = []
    for tab in re.findall(r"\{\|.*?\n\|\}", wt, flags=re.S):
        fecha = re.search(r"Fecha\s+(\d+)|(Final|Semifinal|Cuartos|Desempate|Repechaje|Play-?off)", tab)
        dia = None
        for row in re.split(r"\n\|-[^\n]*", tab):
            cels = [l[1:] for l in row.split('\n') if l.startswith('|') and not l.startswith('|}') and not l.startswith('|-')]
            # células na mesma linha separadas por ||
            cc = []
            for l in cels: cc += l.split('||')
            cc = [limpa(x) for x in cc]
            if len(cc) < 3: continue
            k = next((i for i, x in enumerate(cc) if re.fullmatch(r"\d{1,2}\s*[-–:]\s*\d{1,2}(\s*\(.*\))?", x)), None)
            if k is None or k == 0 or k + 1 >= len(cc): continue
            gm, gv = map(int, re.findall(r"\d+", cc[k])[:2])
            m, v = cc[k - 1], cc[k + 1]
            for x in cc[k + 2:]:
                d = re.search(r"(\d{1,2})\s+de\s+([a-záéíóú]+)", x.lower())
                if d and d.group(2) in MES:
                    dia = f"{ano}-{MES[d.group(2)]:02d}-{int(d.group(1)):02d}"
            out.append((fecha.group(0) if fecha else '', m, gm, gv, v, dia))
    return out
if __name__ == '__main__':
    arq, temp = sys.argv[1], sys.argv[2]
    ano = int(sys.argv[3]) if len(sys.argv) > 3 else int(temp[:4])
    wt = json.load(open(arq, encoding='utf-8'))['parse']['wikitext']['*']
    W = jogos(wt, ano)
    P = [p for p in csv.DictReader(open('data/coleta/par-1/pacote/partidas.csv', encoding='utf-8')) if p['temporada'] == temp]
    ok = dif = nao = 0; dd = 0
    linhas = []
    for f, m, gm, gv, v, dia in W:
        cm, cv = clube(m, ano), clube(v, ano)
        cand = [p for p in P if p['mandante'] == cm and p['visitante'] == cv]
        if dia: cand.sort(key=lambda p: abs((int(p['data'][5:7]) * 31 + int(p['data'][8:10])) - (int(dia[5:7]) * 31 + int(dia[8:10]))) if p['data'] else 999)
        else: cand.sort(key=lambda p: (p['gols_mandante'], p['gols_visitante']) != (str(gm), str(gv)))
        if not cand:
            nao += 1; linhas.append(f"  SEM PAR {f} {m}({cm}) {gm}-{gv} {v}({cv}) {dia}"); continue
        p = cand[0]
        pl = (p['gols_mandante'], p['gols_visitante']) == (str(gm), str(gv))
        dt = (dia is None) or p['data'] == dia
        if pl: ok += 1
        else: dif += 1
        if not dt: dd += 1
        if not pl or not dt:
            linhas.append(f"  {'PLACAR' if not pl else 'DATA'} {f}: wiki {m} {gm}-{gv} {v} {dia} | pacote {p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']} {p['data']} {p['resultado_especial']} {p['observacao'][:50]}")
    print(f"{temp}: wiki {len(W)} jogos; pacote {len(P)}; placar igual {ok}, diferente {dif}, data diferente {dd}, sem par {nao}")
    for l in linhas[:40]: print(l)
