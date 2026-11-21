"""Classificação final de todas as temporadas: banco (classificacao_final) e painel (EDS.tab) x 11v11.com (tabela de fim de temporada).
Casa o clube do 11v11 (slug /teams/<slug>/) com o do banco pela linha igual (J V E D GP GC), depois por votação em todas as temporadas."""
import re, sys, json, pathlib
from collections import Counter, defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, url_11v11, baixar
c = banco()
nm = dict(c.execute("select clube_id, nome from clube"))
d = json.loads(open("painel/dados/eng-1.js", encoding="utf-8").read().split("=", 1)[1].strip().rstrip(";"))
tabp = {e["t"]: e["tab"] for e in d["EDS"]}
ROW = re.compile(r'<tr>\s*<td>.*?</td>\s*<td><a href="/teams/([^/]+)/">([^<]+)</a></td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>(.*?)</tr>', re.S)
dados = {}
voto = defaultdict(Counter)
for eid, t, ai, af in temporadas(c):
    h = baixar(url_11v11(ai)).decode("utf-8", "replace")
    linhas = []
    for m in ROW.finditer(h):
        resto = re.findall(r"<td>(?:<span[^>]*>)?(-?[\d.]+)", m.group(9))
        linhas.append((m.group(1), m.group(2), *map(int, m.group(3, 4, 5, 6, 7, 8)), int(resto[-1])))
    cf = c.execute("select clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, coalesce(ajuste_pontos,0) from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
    dados[t] = (linhas, cf)
    por_linha = defaultdict(list)
    for r in cf: por_linha[tuple(r[2:8])].append(r[0])
    for l in linhas:
        k = tuple(l[2:8])
        if len(por_linha.get(k, [])) == 1: voto[l[0]][por_linha[k][0]] += 1
mapa = {s: v.most_common(1)[0][0] for s, v in voto.items()}
out = []
for eid, t, ai, af in temporadas(c):
    linhas, cf = dados[t]
    if not linhas: out.append((t, "sem tabela no 11v11")); continue
    bd = {r[0]: r for r in cf}
    if len(linhas) != len(cf): out.append((t, f"11v11 {len(linhas)} clubes, banco {len(cf)}"))
    pn = {r[0]: r for r in tabp[t]}
    for pos, l in enumerate(linhas, 1):
        cid = mapa.get(l[0])
        if cid not in bd: out.append((t, f"11v11 {l[1]} ({l[0]}) sem par no banco")); continue
        r = bd[cid]
        a = [r[1], *r[2:8], r[8]]
        b = [pos, *l[2:8], l[8]]
        p = pn.get(nm[cid])
        if a[:7] != b[:7] or a[7] != b[7]:
            out.append((t, f"{nm[cid]}: banco pos/J/V/E/D/GP/GC/Pts {a} | 11v11 {b}" + (f" (ajuste {r[9]})" if r[9] else "")))
        if p and [p[1], *p[2:8]] != a[:7]:
            out.append((t, f"{nm[cid]}: painel {p[1:8]} x banco {a[:7]}"))
for t, m in out: print(t, m, sep="\t")
print("mapa", len(mapa), "clubes;", sum(1 for t in dados if dados[t][0]), "temporadas com tabela", file=sys.stderr)
json.dump({k: nm[v] for k, v in mapa.items()}, open("revisao/EN/mapa_11v11.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
