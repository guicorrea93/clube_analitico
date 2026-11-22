"""Compara data, rodada e placar de cada jogo do pacote com o calendário do ogol guardado pela coleta (fonte_id ogol:<id>).
Não é fonte independente: serve para achar erro de leitura (data de outra rodada, rodada trocada)."""
import csv, json, sys, glob
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
og = {}
for f in glob.glob("data/coleta/bra-sp-2/ogol/sp2_*.json"):
    for j in json.load(open(f, encoding="utf-8")):
        og[str(j["id"])] = j
cont = Counter(); ex = defaultdict(list)
for p in csv.DictReader(open("data/coleta/bra-sp-2/pacote/partidas.csv", encoding="utf-8")):
    if not p["fonte_id"].startswith("ogol:"): continue
    o = og.get(p["fonte_id"][5:])
    if not o: cont[(p["temporada"], "sem ogol")] += 1; continue
    from datetime import date
    if o["data"] and p["data"] and o["data"] != p["data"]:
        d = abs((date.fromisoformat(o["data"]) - date.fromisoformat(p["data"])).days)
        k = "data difere 1 dia" if d == 1 else "data difere 2-3 dias" if d <= 3 else "data difere >3 dias"
        cont[(p["temporada"], k)] += 1; ex[(p["temporada"], k)].append(f"{p['mandante']} x {p['visitante']} pacote {p['data']} ogol {o['data']}")
    if p["rodada"] and o.get("rodada") and str(o["rodada"]) != p["rodada"] and o["fase"].startswith("R"):
        cont[(p["temporada"], "rodada difere")] += 1
    if (str(o["gols_mandante"]), str(o["gols_visitante"])) != (p["gols_mandante"], p["gols_visitante"]) and o["gols_mandante"] is not None:
        cont[(p["temporada"], "placar difere")] += 1; ex[(p["temporada"], "placar difere")].append(f"{p['data']} {p['mandante']} {p['gols_mandante']}x{p['gols_visitante']} {p['visitante']} | ogol {o['gols_mandante']}x{o['gols_visitante']}")
for k in sorted(cont): print(k, cont[k], "|", "; ".join(ex[k][:3]))
