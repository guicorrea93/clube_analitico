"""FR: datas do pacote x transfermarkt x ogol (calendário guardado pela coleta). Lista os jogos em que o transfermarkt e o
ogol concordam entre si e discordam do pacote (provável erro da base), de 1948/49 em diante.
Uso (na raiz): python -I -X utf8 revisao/FR/datas_tm_ogol.py > SCRATCH/FR/datas_tm_ogol.txt"""
import csv, json, os, sys
from collections import Counter, defaultdict
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_out = sys.stdout
sys.stdout = open(os.devnull, 'w', encoding='utf-8')
import comparar_tm as CT  # reaproveita leitura e votação (o relatório dele vai para o nulo)
sys.stdout = _out

RAIZ = CT.RAIZ
og = {}
for a in range(1932, 2026):
    arq = os.path.join(RAIZ, "data", "coleta", "fra-1", "ogol", f"fra1_{a}.json")
    if os.path.exists(arq):
        for o in json.load(open(arq, encoding="utf-8")):
            og[o["id"]] = o
saida = []
cont = Counter()
por_dec = defaultdict(Counter)
for T in CT.temps:
    if T < "1948/49" or not CT.dados[T]:
        continue
    pares = {(j["mandante"], j["visitante"]): j for j in CT.nos[T]}
    for x in CT.dados[T]:
        m, v = CT.clube(x["m"], T), CT.clube(x["v"], T)
        j = pares.get((m, v))
        if not j or not j["data"] or not x["data"]:
            continue
        oid = next((p[5:] for p in j["fonte_id"].split("|") if p.startswith("ogol:")), None)
        o = og.get(oid)
        od = o["data"] if o else None
        dec = T[:3] + "0s"
        por_dec[dec]["jogos"] += 1
        if x["data"] != j["data"]:
            dd = abs((date.fromisoformat(x["data"]) - date.fromisoformat(j["data"])).days)
            tipo = "TM=ogol" if od == x["data"] else ("ogol=pacote" if od == j["data"] else "três datas")
            cont[tipo] += 1
            por_dec[dec][tipo] += 1
            saida.append(f"{T}\t{m} x {v}\tpacote {j['data']}\tTM {x['data']}\togol {od}\t{dd} dias\t{tipo}\t{j['fonte']}")
print("RESUMO", dict(cont))
for d in sorted(por_dec):
    print(d, dict(por_dec[d]))
for l in saida:
    print(l)
