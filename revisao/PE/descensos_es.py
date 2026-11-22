"""Descensos da Wikipédia es (seção "Ascensos y descensos" da página da temporada Y = rebaixados ao fim de Y-1)
x rebaixados marcados no pacote (situacao) e x quem some do pacote no ano seguinte. python -I revisao/PE/descensos_es.py"""
import csv, json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2]
C = R / "data/cache/revisao/PE"
def sem(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()
ALIAS = {"sucre": "mariscal sucre", "sucre f. b. c.": "mariscal sucre", "colegio nacional de iquitos": "cni", "universidad tecnica de cajamarca": "utc",
         "real garcilaso": "cusco fc", "inti gas": "ayacucho", "inti gas deportes": "ayacucho", "ayacucho f. c.": "ayacucho",
         "universidad san martin de porres": "universidad san martin", "san martin": "universidad san martin", "fbc melgar": "melgar", "f. b. c. melgar": "melgar",
         "asociacion deportiva tarma": "adt", "deportivo binacional": "binacional", "union huaral": "union huaral", "carlos a. mannucci": "carlos mannucci",
         "leon de huanuco": "leon de huanuco", "colegio san agustin": "deportivo san agustin", "san agustin": "deportivo san agustin",
         "sport coopsol": "coopsol", "deportivo coopsol": "coopsol", "estudiantes de medicina": "estudiantes de medicina", "bella esperanza": "bella esperanza",
         "total clean": "total chalaco", "atletico universidad": "atletico universidad", "jose galvez": "jose galvez", "jose galvez fbc": "jose galvez",
         "cobresol fbc": "cobresol", "pacifico": "pacifico fc", "pacifico f. c.": "pacifico fc", "universidad cesar vallejo": "cesar vallejo",
         "deportivo llacuabamba": "deportivo llacuabamba", "fc carlos stein": "carlos stein", "academia deportiva cantolao": "academia cantolao",
         "club deportivo municipal": "deportivo municipal", "centro deportivo municipal": "deportivo municipal", "municipal": "deportivo municipal",
         "alianza universidad": "alianza universidad", "sport loreto": "sport loreto", "defensor la bocana": "defensor la bocana", "la bocana": "defensor la bocana",
         "juan aurich": "juan aurich", "aurich": "juan aurich", "sport ancash": "sport ancash", "coronel bolognesi": "coronel bolognesi", "bolognesi": "coronel bolognesi",
         "kdt nacional": "kdt nacional", "porvenir miraflores": "porvenir miraflores", "atletico torino": "atletico torino"}
def norm(n):
    n = sem(re.sub(r"\(.*?\)", "", n)).strip(" .")
    return ALIAS.get(n, n)
desc = {}
for f in sorted(C.glob("es_temporada_*.json")):
    y = int(f.stem.split("_")[-1])
    t = json.loads(f.read_text(encoding="utf-8"))["parse"]["wikitext"]
    i = t.find("Ascensos y descensos")
    if i < 0: continue
    sec = t[i:i + 6000]
    j = sec.lower().find("descend")
    if j < 0: continue
    tab = sec[j:]
    tab = tab[:tab.find("|}")]
    nomes = [m.group(2) or m.group(1) for m in re.finditer(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", tab)]
    nomes = [n for n in nomes if not re.match(r"(Copa Per|Segunda Divisi|Liga 2|Torneo Intermedio|Archivo|Intermedia|Campeonato)", n)]
    desc[y - 1] = nomes
P = R / "data/coleta/per-1/pacote"
cl = defaultdict(dict); part = defaultdict(set)
for r in csv.DictReader(open(P / "classificacao_final.csv", encoding="utf-8")): cl[int(r["temporada"])][r["clube"]] = r["situacao"]
for r in csv.DictReader(open(P / "partidas.csv", encoding="utf-8")): part[int(r["temporada"])] |= {r["mandante"], r["visitante"]}
anos = sorted(cl)
nm = {}
for a in anos:
    for c in cl[a]: nm[norm(c)] = c
ok = 0
for a in anos:
    if a < 1926 or a not in desc: continue
    es = {norm(n) for n in desc[a]}
    reb = {norm(c) for c, s in cl[a].items() if s == "rebaixado"}
    if es == reb: ok += 1; continue
    nxt = min([b for b in anos if b > a], default=None)
    print(f"{a}: es={sorted(es)} | pacote marca={sorted(reb)}")
print("edições iguais:", ok, "de", len([a for a in anos if a in desc and a >= 1926]))
