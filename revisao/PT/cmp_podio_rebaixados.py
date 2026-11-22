"""Campeão, vice e rebaixados do pacote x Wikipédia pt (infobox "campeão"/"vicecampeão" e seção "Despromovidos" de cada
temporada) x lista de campeões do artigo "Primeira Liga" (pt).
Uso (na raiz): python -I revisao/PT/cmp_podio_rebaixados.py > SCRATCH/PT/podio.txt"""
import re, sys, pathlib
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8")
import baixar, ptw
from comum import ler

ED = {int(e["temporada"][:4]): e for e in ler("edicoes.csv")}
REB = defaultdict(set)
for x in ler("classificacao_final.csv"):
    if x["situacao"] == "rebaixado":
        REB[int(x["temporada"][:4])].add(x["clube"])


def links(txt, a):
    res = []
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]|\{\{\s*Futebol ([^}|]+?)(?:-POR)?\s*\}\}", txt):
        nomes = [x for x in (m.group(1), m.group(2), m.group(3)) if x]
        c = ptw.chave_clube(nomes, a)
        if c:
            res.append(c)
    return res


for a in sorted(ED):
    w = baixar.wikitext("pt", ptw.TIT[a])
    url = "https://pt.wikipedia.org/wiki/" + ptw.TIT[a].replace(" ", "_")
    T = ED[a]["temporada"]
    cam = re.search(r"\|\s*campeão\s*=(.*)", w); vic = re.search(r"\|\s*vicecampeão\s*=(.*)", w)
    c = links(cam.group(1), a) if cam else []
    v = links(vic.group(1), a) if vic else []
    if c and c[0] != ED[a]["campeao"]:
        print(f"{T}\tCAMPEÃO\tpacote {ED[a]['campeao']}, pt {c[0]}\t{url}")
    if v and v[0] != ED[a]["vice"]:
        print(f"{T}\tVICE\tpacote {ED[a]['vice']}, pt {v[0]}\t{url}")
    if not c or not v:
        print(f"{T}\tINFOBOX SEM CAMPEÃO/VICE LEGÍVEL\t{cam.group(1)[:60] if cam else ''} / {vic.group(1)[:60] if vic else ''}\t{url}")
    m = re.search(r"Despromovid\w*(.*?)(?:Promovid|\n==[^=]|$)", w, re.S)
    if m:
        d = set(links(m.group(1), a))
        if d != REB[a]:
            print(f"{T}\tREBAIXADOS\tpacote {sorted(REB[a])}, pt {sorted(d)}\t{url}")
        else:
            print(f"{T}\tREBAIXADOS OK\t{sorted(d)}\t{url}")
    else:
        print(f"{T}\tSEM SEÇÃO DESPROMOVIDOS\tpacote {sorted(REB[a])}\t{url}")
