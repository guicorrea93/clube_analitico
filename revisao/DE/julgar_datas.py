"""Para cada data diferente (> 3 dias) entre o pacote e a RSSSF (saída de cmp_rsssf_datas.py), vê qual das duas datas é
possível: um clube não joga duas vezes em 3 dias. Também lista os jogos do pacote com data fora da ordem das rodadas.
Uso: python -I revisao/DE/julgar_datas.py > revisao/DE/julgar_datas_saida.txt"""
import csv, re, sys, pathlib
from collections import defaultdict
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
PAC = AQUI.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
P = list(csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")))
por_clube = defaultdict(list)
for p in P:
    for c in (p["mandante"], p["visitante"]):
        por_clube[(p["temporada"], c)].append(p)
def conflito(t, m, v, d, eu):
    d = date.fromisoformat(d); out = []
    for c in (m, v):
        for q in por_clube[(t, c)]:
            if q is eu or not q["data"]: continue
            if abs((date.fromisoformat(q["data"]) - d).days) <= 2:
                out.append(f"{c} joga {q['mandante']} x {q['visitante']} em {q['data']} (rodada {q['rodada']})")
    return out
idx = {(p["temporada"], p["mandante"], p["visitante"]): p for p in P}
L = re.compile(r"DATA (.+?) x (.+?) \(rodada (\d+)\): pacote (\S+) \| RSSSF (\S+) \(rodada (\d+)\) \[(\d+) dias\]")
temp = None; cont = defaultdict(int)
for l in open(AQUI / "cmp_rsssf_datas_saida.txt", encoding="utf-8"):
    m = re.match(r"^(\d{4}/\d\d):", l)
    if m: temp = m.group(1); continue
    m = L.search(l)
    if not m or int(m.group(7)) <= 3: continue
    mm, vv, r, dp, dr = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
    eu = idx[(temp, mm, vv)]
    cp, cr = conflito(temp, mm, vv, dp, eu), conflito(temp, mm, vv, dr, eu)
    if cp and not cr: v = "PACOTE ERRADO (data impossível)"
    elif cr and not cp: v = "RSSSF errada (a data dela é impossível)"
    elif cp and cr: v = "as duas datas batem com outro jogo"
    else: v = "indefinido (as duas são possíveis)"
    cont[v] += 1
    print(f"{temp} {mm} x {vv} (rodada {r}): pacote {dp} | RSSSF {dr} -> {v}" + (f"; pacote: {cp[0]}" if cp else "") + (f"; RSSSF: {cr[0]}" if cr else ""))
print(dict(cont))
