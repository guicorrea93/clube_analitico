"""1945/46: datas do pacote x os três calendários da Wikipédia it (Alta Italia, Centro-Sud, finale)."""
import csv, os, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itwiki, rsssf_datas  # noqa: E402
t = itwiki.texto(1945)
partes = [t[t.find("== Serie A Alta Italia"):t.find("== Serie mista")], t[t.find("== Serie mista"):t.find("== Finali nazionali")],
          t[t.find("== Finali nazionali"):]]
cal = {}
for p in partes:
    cal.update({(k, "Final" if p is partes[2] else ""): v for k, v in itwiki.calendario(1945, p).items()})
ok = dif = sem = 0
for x in csv.DictReader(open(os.path.join(itwiki.RAIZ, "data/coleta/ita-1/pacote/partidas.csv"), encoding="utf-8")):
    if x["temporada"] != "1945/46":
        continue
    k = ((x["mandante"], x["visitante"]), "Final" if x["grupo"] == "Final" else "")
    w = cal.get(k)
    if not w:
        sem += 1; continue
    d = abs((date.fromisoformat(x["data"]) - date.fromisoformat(w)).days)
    if d <= 1:
        ok += 1
    else:
        dif += 1
        print(f"1945/46 {x['grupo']} {x['mandante']} x {x['visitante']} {x['gols_mandante']}-{x['gols_visitante']}: pacote {x['data']} | wiki {w}")
print("ok", ok, "dif", dif, "sem", sem)
