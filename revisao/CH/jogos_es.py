"""Jogos das páginas de temporada da Wikipédia em espanhol (tabelas "Fecha N" com Local | Resultado | Visita | Estadio | Fecha)
x pacote do chi-1: placar e data. Uso: python -I revisao/CH/jogos_es.py [temporada ...]"""
import csv, glob, os, re, sys
from collections import defaultdict
from datetime import date
exec(open("revisao/CH/tabelas_es.py", encoding="utf-8").read().split("pc = {}")[0])   # arquivo(), nome(), ch()
MES = {m: i for i, m in enumerate("enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(), 1)}
MES["setiembre"] = 9
def limpa(s):
    s = re.sub(r"<ref.*?(</ref>|/>)", "", s, flags=re.S); s = re.sub(r"\{\{[^}]*\}\}", "", s)
    s = re.sub(r"\[\[([^|\]]*\|)?([^\]]*)\]\]", r"\2", s); s = re.sub(r"'''|''|<[^>]+>", "", s)
    return re.sub(r"^\s*(?:(?:align|style|bgcolor|rowspan|colspan|width)\s*=\s*\"?[^|\"]*\"?\s*)+\|", "", s).strip()
def jogos(txt, t):
    a0 = int(t[:4]); out = []; data = None; ult_mes = None; ano = a0
    if "Clausura" in t and "/" in t: ano = a0 + 1
    for tab in re.findall(r"\{\|(.*?)\n\|\}", txt, re.S):
        if not re.search(r"Local", tab) or not re.search(r"Visita", tab): continue
        for row in re.split(r"\n\|-", tab):
            cel = [limpa(c) for c in re.split(r"\|\||\n\|(?!\|)|\n!", "\n" + row)]
            cel = [c for c in cel if c != ""]
            for c in cel:
                m = re.match(r"^(\d{1,2})\s+de\s+([a-záéíóú]+)", c.lower())
                if m and m.group(2) in MES:
                    mes = MES[m.group(2)]
                    if ult_mes and mes < ult_mes - 6: ano += 1
                    ult_mes = mes; data = f"{ano}-{mes:02d}-{int(m.group(1)):02d}"
            for k, c in enumerate(cel):
                m = re.fullmatch(r"(\d{1,2})\s*[-:–]\s*(\d{1,2})", c)
                if m and 0 < k < len(cel) - 1:
                    out.append((nome(cel[k - 1], a0), nome(cel[k + 1], a0), int(m.group(1)), int(m.group(2)), data)); break
    return out
pac = defaultdict(list)
for r in csv.DictReader(open("data/coleta/chi-1/pacote/partidas.csv", encoding="utf-8")):
    pac[r["temporada"]].append(r)
alvo = sys.argv[1:] or list(pac)
tot = defaultdict(int)
for t in alvo:
    f = arquivo(t)
    if not os.path.exists(f):
        f2 = glob.glob(f.replace("Transici_n", "Transici*")); f = f2[0] if f2 else f
    if not os.path.exists(f): continue
    js = jogos(open(f, encoding="utf-8").read(), t)
    if len(js) < 20: continue
    ps = pac[t]; usados = set(); dp = []; dd = []; sem = []
    for m, v, gm, gv, d in js:
        cand = [i for i, p in enumerate(ps) if i not in usados and p["mandante"] == m and p["visitante"] == v]
        if not cand: sem.append((m, v, gm, gv, d)); continue
        def dist(i):
            try: return abs((date.fromisoformat(ps[i]["data"]) - date.fromisoformat(d)).days)
            except Exception: return 999
        i = min(cand, key=dist); usados.add(i); p = ps[i]
        if (p["gols_mandante"], p["gols_visitante"]) != (str(gm), str(gv)):
            dp.append((d, m, v, f"es {gm}-{gv}", f"pacote {p['gols_mandante']}-{p['gols_visitante']} {p['resultado_especial']}", p["fase"]))
        if d and dist(i) > 1:
            dd.append((m, v, f"es {d}", f"pacote {p['data']}", p["fase"]))
    print(f"== {t}: es {len(js)} jogos; casados {len(usados)} de {len(ps)}; placar dif {len(dp)}; data dif (>1 dia) {len(dd)}; sem par {len(sem)}")
    for x in dp: print("   PLACAR", x)
    for x in dd[:10]: print("   DATA", x)
    if len(dd) > 10: print("   ... +", len(dd) - 10)
    for x in sem[:4]: print("   SEM PAR", x)
    tot["es"] += len(js); tot["casados"] += len(usados); tot["placar"] += len(dp); tot["data"] += len(dd)
print(dict(tot))
