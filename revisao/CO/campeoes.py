"""Bloco A: campeão e vice de cada edição do col-1 (pacote, banco e dados do painel) x
- lista de campeões e vices da RSSSF (data/coleta/col-1/rsssf/colchamp.html, a mesma página que a coleta usou para o campeão,
  mas cuja coluna "Runners Up" a coleta não leu);
- Wikipédia em espanhol, "Categoría Primera A", seção "Títulos por temporada" (campeão, subcampeão, goleador, gols, nº de clubes).
Uso (da raiz): python -I revisao/CO/campeoes.py"""
import csv, html, json, re, sqlite3, unicodedata

P = "data/coleta/col-1/pacote/"


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()


NOMES = {  # nome da fonte (sem acento, minúsculo) -> nome do pacote
    "independiente santa fe": "Independiente Santa Fe", "santa fe": "Independiente Santa Fe",
    "club independiente santa fe": "Independiente Santa Fe",
    "atletico junior": "Junior de Barranquilla", "junior": "Junior de Barranquilla", "junior de barranquilla": "Junior de Barranquilla",
    "millonarios": "Millonarios", "millonarios futbol club": "Millonarios", "deportivo cali": "Deportivo Cali",
    "once caldas": "Once Caldas", "deportes caldas": "Once Caldas", "boca juniors (cali)": "Boca Juniors de Cali",
    "boca juniors de cali": "Boca Juniors de Cali", "boca juniors de cali (1937)": "Boca Juniors de Cali",
    "atletico quindio": "Deportes Quindío", "deportes quindio": "Deportes Quindío",
    "atletico nacional": "Atlético Nacional", "d. independiente medellin": "Independiente Medellín",
    "independiente medellin": "Independiente Medellín", "deportivo independiente medellin": "Independiente Medellín",
    "deportes tolima": "Deportes Tolima", "club deportes tolima": "Deportes Tolima", "america de cali": "América de Cali",
    "cucuta deportivo": "Cúcuta Deportivo", "union magdalena": "Unión Magdalena", "atletico bucaramanga": "Atlético Bucaramanga",
    "deportivo pasto": "Deportivo Pasto", "asociacion deportivo pasto": "Deportivo Pasto", "real cartagena": "Real Cartagena",
    "atletico huila": "Atlético Huila", "cd la equidad": "Internacional de Bogotá", "la equidad": "Internacional de Bogotá",
    "club deportivo la equidad": "Internacional de Bogotá", "boyaca chico fc": "Boyacá Chicó", "boyaca chico": "Boyacá Chicó",
    "deportivo pereira": "Deportivo Pereira", "cortulua": "Cortuluá", "aguilas doradas": "Águilas Doradas",
    "internacional de bogota": "Internacional de Bogotá",
}


def nome(s):
    k = sem_acento(re.sub(r"\s+", " ", s))
    return NOMES.get(k, "?" + s)


# RSSSF colchamp
t = html.unescape(re.sub(r"<[^>]+>", "", open("data/coleta/col-1/rsssf/colchamp.html", encoding="latin-1").read()))
rs = {}
ano = None
for l in t.splitlines():
    m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(Ap|Fi|Cl)?\s*(\S.*?)(?:\s{2,}(\S.*?))?\s*$", l)
    if not m or not (m.group(1) or m.group(2)):
        continue
    if m.group(1):
        ano = m.group(1)
    if int(ano[:4]) > 2025:
        continue
    temp = ano if not m.group(2) else f"{ano} {'Apertura' if m.group(2) == 'Ap' else 'Finalización'}"
    if re.search(r"not awarded|cancel", m.group(3)):
        rs[temp] = ("—", "—")
        continue
    rs[temp] = (nome(m.group(3)), nome(m.group(4)) if m.group(4) else "")

# Wikipédia es
W = open("data/cache/revisao/CO/es_Categoría_Primera_A.txt", encoding="utf-8").read()
W = W[W.index("=== Títulos por temporada ==="):W.index("== Palmarés ==")]
wk = {}
for bloco in re.split(r"\n\|-[^\n]*", W):
    m = re.match(r"\s*\|'''\[\[[^|\]]*\|(\d{4}(?:-\d{2})?(?:-I{1,2})?)\]\]", bloco.strip())
    if not m:
        continue
    a = m.group(1)
    if re.fullmatch(r"\d{4}-I", a):
        temp = a[:4] + " Apertura"
    elif re.fullmatch(r"\d{4}-II", a):
        temp = a[:4] + " Finalización"
    elif re.fullmatch(r"\d{4}-\d{2}", a):
        temp = a[:4] + "/" + a[5:]
    else:
        temp = a
    if temp == "2020":
        temp = "2020 Apertura"
    if int(temp[:4]) > 2025:
        continue
    cels = re.split(r"\n\|(?!\})", "\n" + bloco.strip())[1:]
    if "cancelado" in bloco:
        wk[temp] = ("—", "—", "", "", "")
        continue

    def link(c):
        x = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", c)
        return (x.group(1)).strip() if x else re.sub(r"<[^>]+>|'''", "", c).strip()

    camp, sub = link(cels[2]), link(cels[4])
    gol = re.sub(r"\{\{[^}]*\}\}|<[^>]+>|\[\[[^\]|]*\||\]\]|\[\[", "", cels[6]).strip()
    wk[temp] = (nome(camp), nome(sub), gol, cels[7].strip(), cels[8].strip() if len(cels) > 8 else "")

# pacote, banco, painel
eds = {r["temporada"]: r for r in csv.DictReader(open(P + "edicoes.csv", encoding="utf-8"))}
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nm = dict(c.execute("select clube_id, nome from clube"))
db = {}
for temp, ca, vi, n in c.execute("""select e.temporada, e.campeao_id, e.vice_id, e.num_clubes from edicao e join competicao co using(competicao_id)
                                   where co.slug='col-1'"""):
    db[temp] = (nm.get(ca, ""), nm.get(vi, ""), n)
js = open("painel/dados/col-1.js", encoding="utf-8").read()
D = json.loads(js[js.index("=") + 1:].strip().rstrip(";"))
out = []
nv = nc = 0
for temp, r in eds.items():
    a, b = rs.get(temp, ("", "")), wk.get(temp, ("", "", "", "", ""))
    d = db.get(temp, ("", "", ""))
    flag = []
    if r["campeao"] != (a[0] if a[0] != "—" else "") or (b[0] not in ("", "—") and r["campeao"] != b[0]):
        flag.append("CAMPEAO")
        nc += 1
    if r["vice"] != a[1] or (b[1] not in ("", "—") and r["vice"] != b[1]):
        flag.append("VICE")
        nv += 1
    if a[1] != b[1]:
        flag.append("fontes-divergem")
    if (d[0], d[1]) != (r["campeao"], r["vice"]):
        flag.append("BANCO-DIFERE")
    if b[4] and str(r["num_clubes"]) != b[4]:
        flag.append(f"clubes {r['num_clubes']} x wiki {b[4]}")
    out.append(f"{temp}\tpacote: {r['campeao']} / {r['vice']}\tRSSSF: {a[0]} / {a[1]}\twiki-es: {b[0]} / {b[1]}\t{' '.join(flag)}")
print("\n".join(out))
print(f"\nedições: {len(eds)}; campeão divergente: {nc}; vice divergente: {nv}")
print("chaves do painel:", list(D.keys())[:20])
