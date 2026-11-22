"""Clubes da A2: nome x outros pacotes/banco, cidade x bra-sp-1, homônimos e nomes parecidos (duplicados possíveis)."""
import csv, json, sqlite3, sys, unicodedata, re
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
def L(s): return {r["clube"]: r for r in csv.DictReader(open(f"data/coleta/{s}/pacote/clubes.csv", encoding="utf-8"))}
a2, a1 = L("bra-sp-2"), L("bra-sp-1")
db = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
dbc = {n: (e, c) for n, e, c in db.execute("select c.nome, c.regiao, c.cidade from clube c")} if True else {}
cad = json.load(open("data/coleta/comum/clubes_ogol.json", encoding="utf-8"))
por_nome = defaultdict(list)
for cod, v in cad.items(): por_nome[v["clube"]].append((cod, v))
print("== nomes da A2 com mais de um código no cadastro comum")
for n in a2:
    if len(por_nome.get(n, [])) > 1: print(n, por_nome[n])
print("== nomes da A2 que não estão no cadastro comum")
print([n for n in a2 if n not in por_nome])
print("== mesmo nome em A1 com cidade diferente")
for n, r in a2.items():
    if n in a1 and a1[n]["cidade"] != r["cidade"]: print(n, "A2:", r["cidade"], "| A1:", a1[n]["cidade"])
print("== mesmo nome no banco com cidade diferente")
for n, r in a2.items():
    if n in dbc and (dbc[n][1] or "") != r["cidade"]: print(n, "A2:", r["cidade"], "| banco:", dbc[n])
def k(s): return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())
print("== mesma cidade, nomes parecidos (possível duplicado)")
cid = defaultdict(list)
for n, r in a2.items(): cid[r["cidade"]].append(n)
for c, ns in sorted(cid.items()):
    if len(ns) > 1: print(c, ns)
