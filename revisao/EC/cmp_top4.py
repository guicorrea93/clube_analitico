"""Pacote (classificação final, posições 1-4) x Wikipédia es (Historial: campeão, vice, 3º, 4º)."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, collections, unicodedata
AL = {"Barcelona": "Barcelona de Guayaquil", "Liga de Quito": "LDU de Quito", "Universidad Católica": "Universidad Católica de Quito",
      "Liga de Portoviejo": "LDU de Portoviejo", "Liga de Loja": "LDU de Loja", "Valdez": "Valdez SC", "Manta Sport": "Manta Sport"}
wiki = {}
for l in open("revisao/EC/historial_es.tsv", encoding="utf-8"):
    c = l.rstrip("\n").split("\t")
    wiki[c[0]] = [AL.get(x, x) for x in c[1:]]
wiki["2005 Apertura"] = ["LDU de Quito", "Barcelona de Guayaquil", "El Nacional", "Deportivo Cuenca"]
wiki["2005 Clausura"] = ["El Nacional", "Deportivo Cuenca", "LDU de Quito", "Aucas"]
pos = collections.defaultdict(dict)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/classificacao_final.csv", encoding="utf-8")):
    pos[r["temporada"]][int(r["posicao"])] = r["clube"]
ok = dif = 0
for t in pos:
    w = wiki.get(t)
    if not w: print("sem wiki", t); continue
    for k in range(4):
        if k < len(w):
            p = pos[t].get(k + 1)
            if p == w[k]: ok += 1
            else:
                dif += 1; print(t, f"{k+1}º", "pacote:", p, "| wiki es:", w[k], "| wiki tem em:", ([i+1 for i,x in enumerate(w) if x == p] or "-"), "| pacote tem wiki em:", [q for q, c in pos[t].items() if c == w[k]])
print("ok", ok, "dif", dif)
