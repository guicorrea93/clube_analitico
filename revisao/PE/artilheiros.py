"""Artilheiro de cada edição: pacote x Wikipédia es (Primera División del Perú, Goleadores por año). python -I revisao/PE/artilheiros.py"""
import csv, json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2]
def sem(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()
t = json.loads((R / "data/cache/revisao/PE/es_primera_division.json").read_text(encoding="utf-8"))["parse"]["wikitext"]
t = t[t.index("=== Goleadores por año ==="):t.index("=== Goleadores históricos ===")]
es = defaultdict(list)
for bloco in re.split(r"\n\|-[^\n]*", t)[1:]:
    cel = [c.strip() for c in re.split(r"\n\|", "\n" + bloco.strip()) if c.strip()]
    if len(cel) < 4: continue
    m = re.search(r"\|(\d{4})\]\]", cel[0])
    if not m: continue
    nome = re.sub(r"\{\{[^}]*\}\}|align=\w+\||'''", "", cel[1]); nome = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", nome).strip()
    gols = re.sub(r"\D", "", cel[2])
    es[m.group(1)].append((nome, gols))
pac = defaultdict(list)
for r in csv.DictReader(open(R / "data/coleta/per-1/pacote/artilheiros.csv", encoding="utf-8")):
    pac[r["temporada"]].append((r["jogador"], r["gols"], r["clube"]))
ok = 0; dif = []
for ano in sorted(set(es) | set(pac)):
    a = pac.get(ano, []); b = es.get(ano, [])
    if not a or not b:
        dif.append((ano, a, b)); continue
    gols_ok = {x[1] for x in a} == {x[1] for x in b}
    nomes_ok = all(any(sem(x[0]).split()[-1] in sem(y[0]) or sem(y[0]).split()[-1] in sem(x[0]) for y in b) for x in a)
    if gols_ok and nomes_ok: ok += 1
    else: dif.append((ano, a, b))
print("anos iguais:", ok)
for d in dif: print(d)
