"""C: placares 2003-2025 do painel x matriz de resultados da Wikipédia (en, módulo sports results)."""
import sys, re, json
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
from sportstable import tabelas
from nomes import casar
def bloco(wt, nome):
    m = re.search(r"\{\{\s*#invoke:\s*" + nome, wt, re.I)
    if not m: return None
    i, prof, j = m.start(), 0, m.start()
    while j < len(wt):
        if wt.startswith("{{", j): prof += 1; j += 2; continue
        if wt.startswith("}}", j):
            prof -= 1; j += 2
            if prof == 0: break
            continue
        j += 1
    return wt[i:j]
d = painel()
res = {}
tot_cmp = tot_dif = 0
for e in d["EDS"]:
    if e["ano"] < 2003: continue
    wt = wikitext("en", f"{e['ano']} Campeonato Brasileiro Série A")
    b = bloco(wt, "sports results")
    if not b:
        print(e["ano"], "sem matriz de resultados na página"); continue
    b = re.sub(r"<!--.*?-->", "", b, flags=re.S)
    codes = dict(re.findall(r"\|\s*name_([A-Z0-9]+)\s*=\s*(?:\{\{[^}]*\}\}\s*)?\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", re.sub(r"<!--.*?-->", "", wt, flags=re.S)))
    alvos = [r[0] for r in e["tab"]]
    cod2p = {k: casar(v, alvos) for k, v in codes.items()}
    faltam = [k for k, v in cod2p.items() if not v]
    jogos = {}
    for k, (g, mi, vi, gm, gv, sg) in enumerate(e["jogos"]):
        jogos.setdefault((alvos[mi], alvos[vi]), []).append((gm, gv, g + 1))
    difs = []
    n = 0
    b = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", lambda m: m.group(1), b)
    for a, bb, sc in re.findall(r"\|\s*match_([A-Z0-9]+)_([A-Z0-9]+)\s*=\s*([^|\n]*)", b):
        m = re.search(r"(\d+)\s*[–\-−]\s*(\d+)", sc)
        if not m: continue
        gm, gv = int(m.group(1)), int(m.group(2))
        ca, cb = cod2p.get(a), cod2p.get(bb)
        if not ca or not cb: difs.append(f"código sem par {a}/{bb}"); continue
        n += 1
        pj = jogos.get((ca, cb))
        if not pj: difs.append(f"{ca} x {cb}: jogo não está no painel (wiki {gm}-{gv} {sc.strip()[:60]})"); continue
        if (pj[0][0], pj[0][1]) != (gm, gv):
            difs.append(f"{ca} x {cb} (rodada {pj[0][2]}): painel {pj[0][0]}-{pj[0][1]} x wiki {gm}-{gv}  [{sc.strip()[:90]}]")
    tot_cmp += n; tot_dif += len(difs)
    print(e["ano"], "jogos comparados", n, "de", len(e["jogos"]), "| diferenças", len(difs), "| códigos sem par", faltam)
    for x in difs[:25]: print("    ", x)
    res[e["ano"]] = difs
print("TOTAL comparados", tot_cmp, "diferenças", tot_dif)
json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
