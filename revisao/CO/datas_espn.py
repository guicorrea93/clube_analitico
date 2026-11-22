"""Bloco C: datas e placares do pacote (base RSSSF/Wikipédia) x ESPN (placar diário da liga col.1, 2005-2025, já baixado pela
coleta em data/coleta/col-1/espn/; a coleta usa a ESPN só para hora/estádio/lances e mantém a data e o placar da RSSSF).
Casamento por temporada + mandante + visitante (nomes pelo nomes_fonte "espn:" do clubes.csv), o jogo da ESPN mais próximo
em data. Saída: diferenças de data (> 1 dia) e de placar, por edição e fase.
Uso (da raiz): python -I revisao/CO/datas_espn.py"""
import csv, json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

P = "data/coleta/col-1/pacote/"
esp_nome = {}
for r in csv.DictReader(open(P + "clubes.csv", encoding="utf-8")):
    for parte in r["nomes_fonte"].split("|"):
        if parte.startswith("espn:"):
            esp_nome[parte.split(":")[1]] = r["clube"]
esp = defaultdict(list)
for a in range(2005, 2026):
    for g in json.load(open(f"data/coleta/col-1/espn/col1_{a}.json", encoding="utf-8")):
        if not g["situacao"].startswith("STATUS_FINAL") and g["situacao"] != "STATUS_FULL_TIME":
            continue
        d = (datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=5)).date()
        m, v = esp_nome.get(g["mandante"]), esp_nome.get(g["visitante"])
        if m and v:
            esp[(m, v)].append((d, g["gols_mandante"], g["gols_visitante"], g["id"]))
dif_data = Counter(); dif_plac = []; casados = 0; exemplos = defaultdict(list); total = Counter()
for p in csv.DictReader(open(P + "partidas.csv", encoding="utf-8")):
    if int(p["temporada"][:4]) < 2005 or not p["data"]:
        continue
    total[p["temporada"]] += 1
    d = date.fromisoformat(p["data"])
    cands = [x for x in esp.get((p["mandante"], p["visitante"]), []) if abs((x[0] - d).days) <= 40]
    if not cands:
        continue
    x = min(cands, key=lambda x: abs((x[0] - d).days))
    casados += 1
    if abs((x[0] - d).days) > 1:
        dif_data[(p["temporada"], p["fase"])] += 1
        if len(exemplos[(p["temporada"], p["fase"])]) < 2:
            exemplos[(p["temporada"], p["fase"])].append(f"{p['mandante']} x {p['visitante']}: pacote {p['data']}, ESPN {x[0]} (espn {x[3]})")
    if p["gols_mandante"] and (p["gols_mandante"], p["gols_visitante"]) != (x[1], x[2]):
        dif_plac.append(f"{p['temporada']} {p['fase']} {p['data']} {p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']} | ESPN {x[1]}-{x[2]} (espn {x[3]}, {x[0]})")
print(f"jogos 2005-2025 com data: {sum(total.values())}; casados com a ESPN: {casados}")
print(f"data diferente (> 1 dia): {sum(dif_data.values())} jogos")
for k, n in sorted(dif_data.items()):
    print(f"  {k[0]} | {k[1]}: {n}   ex.: {' ; '.join(exemplos[k])}")
print(f"placar diferente: {len(dif_plac)}")
for l in dif_plac:
    print("  " + l)
