"""Amostra de jogos (data e placar) contra as páginas de jogos por clube e temporada do 11v11.com."""
import re, sys, json, pathlib, datetime
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, url_11v11, baixar
c = banco()
nm = dict(c.execute("select clube_id, nome from clube")); idn = {v: k for k, v in nm.items()}
slug2nome = json.load(open("revisao/EN/mapa_11v11.json", encoding="utf-8"))
# nome do 11v11 -> clube, pelas tabelas de fim de temporada já baixadas
ROW = re.compile(r'<a href="/teams/([^/]+)/">([^<]+)</a>')
nome11 = {}
for eid, t, ai, af in temporadas(c):
    for s, n in ROW.findall(baixar(url_11v11(ai)).decode("utf-8", "replace")):
        if s in slug2nome: nome11[n.strip()] = idn[slug2nome[s]]
nome11.setdefault("Stoke", idn["Stoke City"]); nome11.setdefault("Newton Heath", idn["Manchester United"])
AMOSTRA = [(1888, ["preston-north-end", "stoke-city"]), (1925, ["huddersfield-town", "manchester-city"]),
           (1960, ["tottenham-hotspur", "blackpool"]), (1995, ["manchester-united", "bolton-wanderers"]), (2024, ["arsenal", "southampton"])]
TR = re.compile(r"<tr>\s*<td>(\d\d \w\w\w \d{4})</td>\s*<td><a [^>]*>([^<]+?) v ([^<]+)</a></td>(?:(?!</tr>).)*?<td[^>]*>\s*([\d]+)-([\d]+)\s*</td>\s*<td>([^<]+)</td>", re.S)
inv = {}
for s_, n_ in slug2nome.items(): inv.setdefault(n_, s_)
def todos(ai):
    eid = c.execute("select edicao_id from edicao where competicao_id=8 and ano_inicio=?", (ai,)).fetchone()[0]
    return [k for k, v in slug2nome.items() if idn[v] in {x for (x,) in c.execute("select clube_id from classificacao_final where edicao_id=?", (eid,))}]
if len(sys.argv) > 1: AMOSTRA = [(int(a), todos(int(a))) for a in sys.argv[1:]]
for ai, slugs in AMOSTRA:
    eid = c.execute("select edicao_id from edicao where competicao_id=8 and ano_inicio=?", (ai,)).fetchone()[0]
    bd = {(m, v): (d, gm, gv) for m, v, d, gm, gv in c.execute("select mandante_id, visitante_id, data, gols_mandante, gols_visitante from partida where edicao_id=?", (eid,))}
    vistos = set(); ok = dif = 0; linhas = []
    for s in slugs:
        h = baixar(f"https://www.11v11.com/teams/{s}/tab/matches/season/{ai+1}/").decode("utf-8", "replace")
        for d, a, b, ga, gb, comp in TR.findall(h):
            if not re.search(r"League Division One|Premier League", comp) or "Cup" in comp: continue
            a, b = a.strip(), b.strip()
            if a not in nome11 or b not in nome11: linhas.append(f"  nome sem par: {a} x {b}"); continue
            k = (nome11[a], nome11[b])
            if k in vistos: continue
            vistos.add(k)
            data = datetime.datetime.strptime(d, "%d %b %Y").date().isoformat()
            j = bd.get(k)
            if not j: linhas.append(f"  jogo sem par no banco: {a} x {b} {d}"); continue
            if (j[0], j[1], j[2]) != (data, int(ga), int(gb)):
                dif += 1; linhas.append(f"  DIF {nm[k[0]]} x {nm[k[1]]}: banco {j[0]} {j[1]}-{j[2]} | 11v11 {data} {ga}-{gb}")
            else: ok += 1
    print(f"{ai}/{str(ai+1)[-2:]}: {len(vistos)} jogos conferidos, {ok} iguais (data e placar), {dif} diferentes")
    for l in linhas: print(l)
