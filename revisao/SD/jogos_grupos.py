"""Revisão SD: placares da fase de grupos da Série D (banco) x Wikipédia.
- 2009-2019: matrizes de resultados da página pt da edição (células '<!-- ABC --> 2–1').
- 2020-2025: módulo 'sports results' da página en da edição (match_ABC_DEF=2–1).
Casa os clubes pelo nome (aproximado) dentro de cada grupo. Uso: python -I revisao/SD/jogos_grupos.py [ano ...]"""
import re, sys, sqlite3, pathlib, unicodedata, difflib, collections
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data/cache/revisao/SD"
sys.stdout.reconfigure(encoding="utf-8")

def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]", "", s)

def nome_de(c):
    m = re.search(r"\{\{\s*[Ff]utebol ([^|}]+)", c)
    if m: return m.group(1).strip()
    ms = re.findall(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", c)
    ms = [x for x in ms if not x.lower().startswith(("file:", "imagem:", "ficheiro:"))]
    if ms: return ms[-1].strip()
    return re.sub(r"\{\{[^}]*\}\}|'''|<[^>]+>", "", c).strip()

def placar(s):
    s = re.sub(r"<!--.*?-->|<ref.*?(</ref>|/>)|\{\{[^}]*\}\}", "", s, flags=re.S)
    m = re.search(r"(\d+)\s*[–-]\s*(\d+)", s)
    return (int(m.group(1)), int(m.group(2))) if m else None

def pt_matrizes(txt):
    """[(lista de nomes das linhas, {(i, j): (gm, gv)})] para cada matriz com comentários <!-- ABC -->"""
    out = []
    for tab in re.split(r"\n\{\|", txt):
        tab = tab.split("\n|}")[0]
        if "<!--" not in tab and not re.search(r"\|[A-ZÇÃ]{2,4}\]\]", tab): continue
        linhas = re.split(r"\n\|-", tab)
        nomes, cel = [], {}
        for l in linhas:
            l = l.strip()
            m = re.match(r"[|!]\s*(?:align=\"?left\"?\s*\|)?(.*?\{\{\s*[Ff]utebol [^}]+\}\}|.*?\[\[[^\]]+\]\])", l)
            if not m or not re.search(r"\d+\s*[–-]\s*\d+", l) or "Tooltip" in l: continue
            partes = re.split(r"\n[|!]|\|\|", "\n" + l)
            partes = [p for p in partes if p.strip()]
            nome = nome_de(partes[0])
            i = len(nomes); nomes.append(nome)
            vals = partes[1:]
            for j, v in enumerate(vals):
                p = placar(v)
                if p: cel[(i, j)] = p
        if len(nomes) >= 3 and cel:
            out.append((nomes, cel))
    return out

def en_modulos(txt):
    out = []
    for b in re.split(r"\{\{\s*#invoke:\s*[Ss]ports (?:results|table)", txt)[1:]:
        b = b.split("</onlyinclude>")[0]
        ordem = [x for _, x in sorted((int(n), x) for n, x in re.findall(r"\|\s*team(\d+)\s*=\s*([A-Z0-9]+)", b))]
        m = re.search(r"\|\s*team_order\s*=\s*([^\n|]+)", b)
        if m: ordem = [x.strip() for x in m.group(1).split(",") if x.strip()]
        if not ordem or "match_" not in b: continue
        nomes = {}
        for k in ordem:
            mm = re.search(r"\|\s*name_" + re.escape(k) + r"\s*=\s*([^\n]+)", b)
            nomes[k] = nome_de(mm.group(1)) if mm else k
        cel = {}
        for a, h, v in re.findall(r"\|\s*match_([A-Z0-9]+)_([A-Z0-9]+)\s*=\s*([^\n|]*)", b):
            p = placar(v)
            if p and a in ordem and h in ordem: cel[(ordem.index(a), ordem.index(h))] = p
        out.append(([nomes[k] for k in ordem], cel))
    return out

ALIAS = {"gremionovorizontino": "novorizontino", "campinensepb": "campinense", "fluminensedefeira": "fluminenseba",
         "guaranydesobral": "guarany", "ferroviaria": "ferroviariasp", "retro": "retrofc", "fastclube": "fastam",
         "princesadosolimoes": "princesa", "redbullbrasil": "redbullbragantinoii", "manaus": "manausfc", "globo": "globofc",
         "gremiobarueri": "barueri", "betim": "ipatinga", "corinthiansprr": "jmalucelli", "corinthianspr": "jmalucelli"}

con = sqlite3.connect(f"file:{RAIZ}/db/futebol.db?mode=ro", uri=True)
anos = [int(a) for a in sys.argv[1:]] or range(2009, 2026)
tot = collections.Counter()
for ano in anos:
    jogos = list(con.execute("""SELECT p.partida_id, cm.nome, cv.nome, p.gols_mandante, p.gols_visitante, f.nome, p.grupo, p.data
        FROM partida p JOIN edicao e USING(edicao_id) JOIN fase f USING(fase_id) JOIN clube cm ON cm.clube_id = p.mandante_id
        JOIN clube cv ON cv.clube_id = p.visitante_id WHERE e.competicao_id = 6 AND e.temporada = ?""", (str(ano),)))
    clubes = sorted({j[1] for j in jogos} | {j[2] for j in jogos})
    idx = collections.defaultdict(list)
    for j in jogos: idx[(j[1], j[2])].append(j)
    if ano <= 2019:
        fonte = f"https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_{ano}_-_Série_D"
        mats = pt_matrizes((CACHE / f"pt_{ano}.txt").read_text(encoding="utf-8"))
    else:
        fonte = f"https://en.wikipedia.org/wiki/{ano}_Campeonato_Brasileiro_Série_D"
        mats = en_modulos((CACHE / f"en_{ano}.txt").read_text(encoding="utf-8"))
    ok = dif = falta = 0
    msgs = []
    for nomes, cel in mats:
        mapa = {}
        for n in nomes:   # 1ª passada: nome igual ou começo igual, sem ambiguidade
            k = ALIAS.get(norm(n), norm(n))
            exato = [c for c in clubes if norm(c) == k]
            cand = exato or [c for c in clubes if norm(c).startswith(k) or k.startswith(norm(c))]
            mapa[n] = cand[0] if len(cand) == 1 else None
        # 2ª passada: quem sobrou é o clube do banco que jogou a fase de grupos contra os já casados da mesma matriz
        adv = collections.defaultdict(collections.Counter)
        for x in jogos:
            if x[5] == "Primeira fase" or (x[6] or "").startswith("Grupo"):
                adv[x[1]][x[2]] += 1; adv[x[2]][x[1]] += 1
        casados = {v for v in mapa.values() if v}
        for n in nomes:
            if mapa[n]: continue
            cand = [c for c in clubes if c not in casados and sum(1 for o in casados if adv[c][o]) >= max(2, len(casados) - 1)]
            if len(cand) != 1:
                k = ALIAS.get(norm(n), norm(n))
                cand = difflib.get_close_matches(k, [norm(c) for c in clubes if c not in casados], 1, 0.6)
                cand = [c for c in clubes if cand and norm(c) == cand[0]]
            mapa[n] = cand[0] if cand else None
            if mapa[n]: casados.add(mapa[n]); msgs.append(f"   (nome casado pelos adversários: {n} = {mapa[n]})")
        for (i, j), (a, b) in cel.items():
            if i == j or j >= len(nomes): continue
            m, v = mapa[nomes[i]], mapa[nomes[j]]
            js = [x for x in idx.get((m, v), []) if x[5] in ("Primeira fase",) or (x[6] or "").startswith("Grupo")]
            if not js:
                falta += 1; msgs.append(f"   sem jogo no banco: {nomes[i]}({m}) {a}-{b} {nomes[j]}({v})"); continue
            if any((x[3], x[4]) == (a, b) for x in js): ok += 1
            else:
                dif += 1; x = js[0]
                msgs.append(f"   placar: wiki {nomes[i]} {a}-{b} {nomes[j]} | banco {x[1]} {x[3]}-{x[4]} {x[2]} ({x[7]}, {x[0]})")
    print(f"== {ano}: {len(mats)} matrizes; {ok} iguais, {dif} placares diferentes, {falta} sem par  ({fonte})")
    for m in msgs: print(m)
    tot.update(ok=ok, dif=dif, falta=falta)
print("TOTAL", dict(tot))
