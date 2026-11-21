"""Placar de todos os jogos: banco x matriz de resultados da Wikipédia en (artigo de cada temporada, módulo 'sports results').
A coleta usou só a tabela final da Wikipédia; a matriz é conferência independente do engsoccerdata/football-data."""
import re, sys, json, pathlib, difflib, unicodedata
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, pagina_wiki, wikitext
c = banco()
nm = dict(c.execute("select clube_id, nome from clube"))
nomes = defaultdict(set)
for cid, n in c.execute("select clube_id, nome from clube_nome"): nomes[cid].add(n)
for cid, n in nm.items(): nomes[cid].add(n)
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(f\.?c\.?|a\.?f\.?c\.?|football club)\b", "", s)
    return re.sub(r"[^a-z ]", "", s).strip()
def blocos(t):
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports results", t, re.I):
        i = m.start(); dep = 0; j = i
        while j < len(t):
            if t.startswith("{{", j): dep += 1; j += 2; continue
            if t.startswith("}}", j):
                dep -= 1; j += 2
                if dep == 0: break
                continue
            j += 1
        yield t[i:j]
def le_bloco(b):
    b = re.sub(r"<!--.*?-->", "", b, flags=re.S)
    params = {}
    for p in re.split(r"\n\s*\||\|(?=\s*(?:team\d+|name_|match_|team_order|result|status|source|update|a_note|matches_style|solid_cell)\b)", b):
        if "=" in p:
            k, v = p.split("=", 1); params[k.strip()] = v.strip()
    codes = []
    if "team_order" in params: codes = [x.strip() for x in params["team_order"].split(",") if x.strip()]
    else:
        ks = sorted((int(k[4:]), v) for k, v in params.items() if re.fullmatch(r"team\d+", k))
        codes = [v.strip() for _, v in ks]
    names = {}
    for cd in codes:
        v = params.get("name_" + cd, cd)
        m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", v)
        names[cd] = (m.group(1), m.group(2) or m.group(1)) if m else (v, v)
    jogos = {}
    for k, v in params.items():
        m = re.fullmatch(r"match_(.+?)_(.+)", k)
        if not m: continue
        a, bb = m.groups()
        if a not in names:  # códigos com '_' no meio
            continue
        vv = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", v); vv = re.sub(r"\[\[|\]\]|\{\{[^}]*\}\}|<[^>]*>", "", vv)
        s = re.search(r"(\d+)\s*\W\s*(\d+)", vv)
        if s: jogos[(a, bb)] = (int(s.group(1)), int(s.group(2)))
        elif vv.strip(): jogos[(a, bb)] = ("?", vv.strip()[:30])
    return codes, names, jogos
tot = dif = conf = 0
saida = []
cobertura = {}
for eid, t, ai, af in temporadas(c):
    js = c.execute("select mandante_id, visitante_id, gols_mandante, gols_visitante, data from partida where edicao_id=?", (eid,)).fetchall()
    S = {x for j in js for x in (j[0], j[1])}
    cand = {cid: {norm(n) for n in nomes[cid]} for cid in S}
    w = wikitext("en", pagina_wiki(ai))
    if ai < 1992:
        w += "\n" + wikitext("en", f"{ai}–{str(ai+1)[-2:]} Football League First Division")
    melhor = None
    for b in blocos(w):
        codes, names, jg = le_bloco(b)
        if len(codes) != len(S): continue
        mapa = {}; score = 0
        for cd in codes:
            alvo = {norm(names[cd][0]), norm(names[cd][1])}
            best = max(S, key=lambda cid: max(difflib.SequenceMatcher(None, a, x).ratio() for a in alvo for x in cand[cid]))
            sc = max(difflib.SequenceMatcher(None, a, x).ratio() for a in alvo for x in cand[best])
            mapa[cd] = best; score += sc
        if len(set(mapa.values())) != len(codes): continue
        if score / len(codes) < 0.8: continue
        if melhor is None or score > melhor[0]: melhor = (score, mapa, jg)
    if not melhor:
        saida.append(f"{t}\tsem matriz da 1ª divisão na Wikipédia ({pagina_wiki(ai)})"); cobertura[t] = 0; continue
    _, mapa, jg = melhor
    inv = {v: k for k, v in mapa.items()}
    bd = {(j[0], j[1]): j for j in js}
    n_ok = n_dif = 0
    for (a, b), sc in jg.items():
        j = bd.get((mapa[a], mapa[b]))
        if not j: saida.append(f"{t}\tjogo da matriz sem par no banco {nm[mapa[a]]} x {nm[mapa[b]]} {sc}"); continue
        if sc[0] == "?": saida.append(f"{t}\tmatriz sem placar legível {nm[j[0]]} x {nm[j[1]]}: {sc[1]} (banco {j[2]}-{j[3]})"); continue
        if (j[2], j[3]) != sc:
            n_dif += 1
            saida.append(f"{t}\tPLACAR {nm[j[0]]} x {nm[j[1]]} ({j[4]}): banco {j[2]}-{j[3]} | Wikipédia {sc[0]}-{sc[1]}")
        else: n_ok += 1
    tot += n_ok + n_dif; dif += n_dif; conf += 1
    cobertura[t] = n_ok + n_dif
    if len(jg) != len(js): saida.append(f"{t}\tmatriz com {len(jg)} jogos, banco {len(js)}")
for s in saida: print(s)
print(f"temporadas com matriz {conf}; jogos conferidos {tot}; diferentes {dif}")
json.dump(cobertura, open("revisao/EN/cobertura_matriz.json", "w"), indent=0)
