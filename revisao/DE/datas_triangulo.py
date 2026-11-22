"""Junta as três conferências de data (transfermarkt, RSSSF e a regra "um clube não joga duas vezes em 2 dias") e diz,
para cada jogo em que o transfermarkt discorda do pacote, qual data fica. Saída: revisao/DE/datas_corrigir.csv
(temporada, data_pacote, mandante, visitante, data_certa, provas) e um resumo na tela.
Uso: python -I revisao/DE/datas_triangulo.py"""
import csv, re, sys, pathlib
from collections import defaultdict
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
PAC = AQUI.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
P = list(csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")))
idx = {(p["temporada"], p["mandante"], p["visitante"]): p for p in P}
por_clube = defaultdict(list)
for p in P:
    for c in (p["mandante"], p["visitante"]):
        por_clube[(p["temporada"], c)].append(p)
def colide(t, m, v, d, eu):
    d = date.fromisoformat(d)
    return [f"{q['mandante']} x {q['visitante']} {q['data']}" for c in (m, v) for q in por_clube[(t, c)]
            if q is not eu and q["data"] and abs((date.fromisoformat(q["data"]) - d).days) <= 1]
# RSSSF: data por jogo (do cmp_rsssf_datas, com -v não; refaz aqui a leitura)
import cmp_rsssf_datas as R  # noqa
L = re.compile(r"DATA (.+?) x (.+?) \(rodada (\d+)\): pacote (\S+) \| tm (\S+) \[(-?\d+) dias\]")
rs_cache = {}
saida, cont = [], defaultdict(int)
temp = None
for l in open(AQUI / "cmp_tm_saida.txt", encoding="utf-8"):
    m = re.match(r"^(\d{4}/\d\d):", l)
    if m: temp = m.group(1); continue
    m = L.search(l)
    if not m: continue
    mm, vv, r, dp, dt = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
    a = int(temp[:4])
    if a not in rs_cache:
        rs_cache[a] = R.mapa_rsssf(a) if a <= 1998 else {}
    drs = (rs_cache[a].get((mm, vv)) or (None, None))[0]
    eu = idx[(temp, mm, vv)]
    cp, ct = colide(temp, mm, vv, dp, eu), colide(temp, mm, vv, dt, eu)
    provas = [f"transfermarkt {dt}"]
    if drs: provas.append(f"RSSSF {drs}")
    if cp: provas.append(f"data do pacote colide: {cp[0]}")
    if ct: provas.append(f"data do transfermarkt colide: {ct[0]}")
    if drs == dt and not ct: v = "corrigir (transfermarkt + RSSSF)"
    elif cp and not ct: v = "corrigir (data do pacote impossível)"
    elif drs == dp: v = "manter (RSSSF = pacote)"
    elif ct: v = "manter (data do transfermarkt impossível)"
    else: v = "dúvida"
    cont[v] += 1
    saida.append({"temporada": temp, "rodada": r, "mandante": mm, "visitante": vv, "data_pacote": dp, "data_transfermarkt": dt,
                  "data_rsssf": drs or "", "veredito": v, "provas": "; ".join(provas)})
with open(AQUI / "datas_corrigir.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(saida[0])); w.writeheader(); w.writerows(saida)
for s in saida:
    print(s["temporada"], s["mandante"], "x", s["visitante"], s["data_pacote"], "->", s["data_transfermarkt"], "|", s["veredito"], "|", s["provas"])
print(dict(cont))
