"""Bloco D: artilheiro de cada edição (pacote artilheiros.csv, da RSSSF coltops.html) x Wikipédia es ("Categoría Primera A",
Títulos por temporada: Máximo goleador e Goles); e soma dos gols com autor por jogo x placar.
Uso (da raiz): python -I revisao/CO/artilheiros.py"""
import csv, re, unicodedata
from collections import Counter, defaultdict

P = "data/coleta/col-1/pacote/"


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z ]", " ", s).split()


W = open("data/cache/revisao/CO/es_Categoría_Primera_A.txt", encoding="utf-8").read()
W = W[W.index("=== Títulos por temporada ==="):W.index("== Palmarés ==")]
wk = {}
for bloco in re.split(r"\n\|-[^\n]*", W):
    m = re.match(r"\s*\|'''\[\[[^|\]]*\|(\d{4}(?:-\d{2})?(?:-I{1,2})?)\]\]", bloco.strip())
    if not m or "cancelado" in bloco:
        continue
    a = m.group(1)
    temp = (a[:4] + " Apertura" if a.endswith("-I") else a[:4] + " Finalización" if a.endswith("-II")
            else a[:4] + "/" + a[5:] if re.fullmatch(r"\d{4}-\d{2}", a) else a)
    temp = "2020 Apertura" if temp == "2020" else temp
    cels = re.split(r"\n\|(?!\})", "\n" + bloco.strip())[1:]
    gol = cels[6]
    nomes = [x.split("|")[-1] for x in re.findall(r"\[\[([^\]]+)\]\]", re.sub(r"\{\{[^}]*\}\}", "", gol))]
    g = re.sub(r"<[^>]+>|'''", "", cels[7]).strip()
    wk[temp] = (nomes, g)
art = defaultdict(list)
for r in csv.DictReader(open(P + "artilheiros.csv", encoding="utf-8")):
    art[r["temporada"]].append((r["jogador"], r["gols"], r["clube"]))
eds = [r["temporada"] for r in csv.DictReader(open(P + "edicoes.csv", encoding="utf-8"))]
ok = n = 0
for t in eds:
    if t not in wk:
        continue
    n += 1
    nomes, g = wk[t]
    a = art.get(t, [])
    if not a:
        print(f"{t}: SEM artilheiro no pacote | wiki: {', '.join(nomes)} ({g})")
        continue
    sob = any(set(norm(x)[-1:]) & set(norm(j)) for x in nomes for j, _, _ in a)
    gol_ok = any(gg == re.sub(r"\D", "", g) for _, gg, _ in a)
    if sob and gol_ok and len(a) == len(nomes):
        ok += 1
    else:
        print(f"{t}: pacote {[(j, gg) for j, gg, _ in a]} | wiki: {nomes} ({g})")
print(f"\nedições com artilheiro na wiki: {n}; batem nome, gols e nº de empatados: {ok}")

# soma dos gols com autor x placar
pl = {p["id"]: (p["temporada"], p["mandante"], p["visitante"], p["gols_mandante"], p["gols_visitante"], p["data"])
      for p in csv.DictReader(open(P + "partidas.csv", encoding="utf-8"))}
cont = defaultdict(Counter)
for g in csv.DictReader(open(P + "gols.csv", encoding="utf-8")):
    cont[g["partida_id"]][g["clube"]] += 1
ruins = []
for pid, c in cont.items():
    t, m, v, gm, gv, d = pl[pid]
    if gm == "" or c[m] > int(gm) or c[v] > int(gv):
        ruins.append(f"{t} {d} {m} {gm}-{gv} {v}: autores {c[m]}+{c[v]}")
print(f"jogos com mais gols com autor que o placar: {len(ruins)}")
for r in ruins:
    print("  " + r)
