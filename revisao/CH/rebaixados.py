"""Rebaixados: pacote (classificacao_final.csv, situacao 'rebaixado') x RSSSF chilehist.html (linhas 'RELEGATED:'),
1933-1996, e x notas 'Relegated' das páginas por ano depois de 1996 (lista do pacote). Uso: python -I revisao/CH/rebaixados.py"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, "coleta/comum-sulamerica"); sys.path.insert(0, "coleta/chi-1")
import rsssf_sul
from clubes_chi import clube
ls = rsssf_sul.texto(Path("data/coleta/chi-1/rsssf/chilehist.html"))
ano = None; hist = {}
for l in ls:
    m = re.match(r"^\s+(\d{4})\s*$", l)
    if m: ano = int(m.group(1)); continue
    m = re.match(r"^RELEGATED:\s*(.*)", l.strip())
    if m and ano:
        txt = m.group(1)
        hist[ano] = txt
# continuação de linha
for i, l in enumerate(ls):
    pass
pac = defaultdict(list)
sit = defaultdict(list)
for r in csv.DictReader(open("data/coleta/chi-1/pacote/classificacao_final.csv", encoding="utf-8")):
    if r["situacao"] == "rebaixado":
        pac[r["temporada"]].append(r["clube"])
for a in range(1933, 1997):
    h = hist.get(a, "?")
    nomes = [] if re.match(r"(?i)none|no relegation", h) else [clube(x.strip(" ."), a) or x.strip() for x in re.split(r",| and ", h) if x.strip(" .")]
    p = sorted(pac.get(str(a), []))
    if sorted(nomes) != p:
        print(a, "| RSSSF chilehist:", h, "->", sorted(nomes), "| pacote:", p)
print("depois de 1996 (pacote):")
for t, v in pac.items():
    if t[:4] >= "1997": print("  ", t, v)
