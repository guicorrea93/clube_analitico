"""Para os jogos com data errada no pacote (RSSSF = Wikipédia it), qual seria a data do ogol (cache da coleta)?
Gera a lista de correções: revisao/IT/datas_corrigir.csv (temporada, mandante, visitante, data_pacote, data_certa, ogol, fonte).
"""
import csv, json, os, sys
from collections import defaultdict, Counter
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import itwiki, rsssf_datas  # noqa: E402
R = itwiki.RAIZ
ogol = {}
for a in itwiki.ANOS:
    arq = os.path.join(R, "data/coleta/ita-1/ogol", f"ita1_{a}.json")
    if os.path.exists(arq):
        for j in json.load(open(arq, encoding="utf-8")):
            ogol[str(j["id"])] = j["data"]
pj = defaultdict(list)
for x in csv.DictReader(open(os.path.join(R, "data/coleta/ita-1/pacote/partidas.csv"), encoding="utf-8")):
    pj[int(x["temporada"][:4])].append(x)
c = Counter(); saida = []
for a in itwiki.ANOS:
    if a in (1945, 2019):
        continue
    cal = itwiki.calendario(a); rs = rsssf_datas.datas(a)
    for j in pj[a]:
        k = (j["mandante"], j["visitante"])
        w, r = cal.get(k), rs.get(k)
        if not w or not r or r[0] != w or abs((date.fromisoformat(j["data"]) - date.fromisoformat(w)).days) <= 1:
            continue
        oid = next((p[5:] for p in j["fonte_id"].split("|") if p.startswith("ogol:")), None)
        od = ogol.get(oid)
        cat = "ogol = certa" if od == w else "ogol = pacote" if od == j["data"] else "ogol outra" if od else "sem ogol"
        c[cat] += 1
        saida.append({"temporada": j["temporada"], "mandante": k[0], "visitante": k[1], "data_pacote": j["data"], "data_certa": w,
                      "ogol": od or "", "fonte": f"Wikipédia it ({itwiki.url(a)}) + RSSSF ({r[1]})"})
print(dict(c))
with open(os.path.join(AQUI, "datas_corrigir.csv"), "w", encoding="utf-8", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(saida[0]))
    wr.writeheader(); wr.writerows(saida)
print(len(saida), "linhas em revisao/IT/datas_corrigir.csv")
print(Counter(s["temporada"] for s in saida))
