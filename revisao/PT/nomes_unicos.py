"""Nomes dos 73 clubes do pacote por-1 x banco (tabela clube) e x clubes.csv dos outros pacotes: nome repetido no mundo?
Uso (na raiz): python -I revisao/PT/nomes_unicos.py"""
import csv, glob, pathlib, re, sqlite3, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")


def k(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
cols = [r[1] for r in c.execute("pragma table_info(clube)")]
banco = {}
for row in c.execute("select * from clube"):
    d = dict(zip(cols, row))
    banco.setdefault(k(d["nome"]), []).append(d)
outros = {}
for f in glob.glob("data/coleta/*/pacote/clubes.csv"):
    slug = pathlib.Path(f).parts[-3]
    if slug == "por-1":
        continue
    for x in csv.DictReader(open(f, encoding="utf-8")):
        outros.setdefault(k(x["clube"]), set()).add((x["clube"], x.get("pais"), slug))
n = 0
for x in csv.DictReader(open("data/coleta/por-1/pacote/clubes.csv", encoding="utf-8")):
    n += 1
    kk = k(x["clube"])
    if kk in banco:
        print("BANCO", x["clube"], [(d["nome"], d.get("pais_id") or d.get("pais"), d.get("cidade")) for d in banco[kk]])
    if kk in outros:
        print("PACOTE", x["clube"], outros[kk])
print("clubes:", n, file=sys.stderr)
