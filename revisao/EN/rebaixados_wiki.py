"""Rebaixados de cada temporada: banco (classificacao_final.situacao) x Wikipédia en (módulo 'sports table': result + text_<código>)."""
import re, sys, pathlib, difflib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, pagina_wiki, wikitext
from cmp_matriz_wiki import norm, nomes, nm
c = banco()
def tabelas(t):
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports table", t, re.I):
        i = m.start(); dep = 0; j = i
        while j < len(t):
            if t.startswith("{{", j): dep += 1; j += 2; continue
            if t.startswith("}}", j):
                dep -= 1; j += 2
                if dep == 0: break
                continue
            j += 1
        yield re.sub(r"<!--.*?-->", "", t[i:j], flags=re.S)
def params(b):
    p = {}
    for x in re.split(r"\n\s*\||\|(?=\s*[\w]+\s*=)", b):
        if "=" in x:
            k, v = x.split("=", 1); p[k.strip()] = v.strip()
    return p
ok = 0
for eid, t, ai, af in temporadas(c):
    S = [r[0] for r in c.execute("select clube_id from classificacao_final where edicao_id=?", (eid,))]
    reb = {r[0] for r in c.execute("select clube_id from classificacao_final where edicao_id=? and situacao='rebaixado'", (eid,))}
    w = wikitext("en", pagina_wiki(ai))
    if ai < 1992: w += "\n" + wikitext("en", f"{ai}–{str(ai+1)[-2:]} Football League First Division")
    melhor = None
    for b in tabelas(w):
        p = params(b)
        order = [x.strip() for x in p.get("team_order", "").split(",") if x.strip()] or [p[k] for k in sorted((k for k in p if re.fullmatch(r"team\d+", k)), key=lambda k: int(k[4:]))]
        if len(order) != len(S): continue
        mapa = {}; sc = 0
        for cd in order:
            v = p.get("name_" + cd, cd); mm = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", v)
            alvo = {norm(mm.group(1)), norm(mm.group(2) or mm.group(1))} if mm else {norm(v)}
            best = max(S, key=lambda cid: max(difflib.SequenceMatcher(None, a, norm(x)).ratio() for a in alvo for x in nomes[cid]))
            mapa[cd] = best; sc += max(difflib.SequenceMatcher(None, a, norm(x)).ratio() for a in alvo for x in nomes[best])
        if len(set(mapa.values())) != len(order): continue
        if melhor is None or sc > melhor[0]: melhor = (sc, mapa, p, order)
    if not melhor: print(t, "sem tabela"); continue
    _, mapa, p, order = melhor
    wiki = set(); notas = {}
    for i, cd in enumerate(order, 1):
        r = p.get(f"result{i}") or p.get(f"result_{cd}")
        if not r:
            for k, v in p.items():
                if re.fullmatch(r"result\d+", k) and False: pass
        txt = p.get("text_" + r, "") if r else ""
        if r and re.search(r"relegat|re-?election|resign|Second Division|Championship|Football League", txt, re.I) and not re.search(r"Champions?\b(?! League)|promot|Europ|UEFA|Cup", txt, re.I):
            wiki.add(mapa[cd]); notas[mapa[cd]] = f"{r}: {txt[:60]}"
    if wiki == reb: ok += 1
    else: print(t, "banco", sorted(nm[x] for x in reb), "| Wikipédia", sorted(nm[x] for x in wiki), {nm[k]: v for k, v in notas.items()})
print("iguais", ok)
