"""Datas do banco x football-data.co.uk (fonte que a coleta usou só para placar e hora; as datas do banco vêm do engsoccerdata).
Uso: python -I revisao/ES/datas_footballdata.py"""
import csv, sqlite3, sys, glob, os, re
from datetime import datetime
sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
# nome football-data -> clube (do nomes_fonte do pacote)
mapa = {}
for r in csv.DictReader(open("data/coleta/esp-1/pacote/clubes.csv", encoding="utf-8")):
    for x in r["nomes_fonte"].split("|"):
        f, n, *_ = x.split(":")
        if f == "football-data": mapa[n] = r["clube"]
tot = igual = 0; difs = []
for arq in sorted(glob.glob("data/coleta/esp-1/football-data/SP1_*.csv")):
    yy = os.path.basename(arq)[4:6]; a = int(yy) + (1900 if int(yy) > 50 else 2000)
    t = f"{a}/{str(a + 1)[2:]}"
    db = {(m, v): d for m, v, d in c.execute("""select mm.nome, vv.nome, p.data from partida p join edicao e using(edicao_id) join competicao k using(competicao_id)
          join clube mm on mm.clube_id=p.mandante_id join clube vv on vv.clube_id=p.visitante_id where k.slug='esp-1' and e.temporada=?""", (t,))}
    for r in csv.DictReader(open(arq, encoding="latin-1")):
        if not r.get("HomeTeam"): continue
        ds = r["Date"]
        try: d = datetime.strptime(ds, "%d/%m/%Y" if len(ds.split("/")[-1]) == 4 else "%d/%m/%y").strftime("%Y-%m-%d")
        except Exception: continue
        k = (mapa.get(r["HomeTeam"]), mapa.get(r["AwayTeam"]))
        if k not in db: continue
        tot += 1
        if db[k] == d: igual += 1
        else: difs.append((t, k[0], k[1], db[k], d))
print("jogos", tot, "mesma data", igual, "diferentes", len(difs))
from collections import Counter
print(Counter(x[0] for x in difs))
for x in difs[:40]: print(*x)
