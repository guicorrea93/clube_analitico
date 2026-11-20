"""Revisão CL: nome de fonte de um clube que é o nome de outro clube (sinal de jogos trocados de clube).

Para cada nome em clube_nome (fonte, anos) e no nomes_fonte dos pacotes, avisa quando ele é igual (sem acento;
"(UF)" e "/UF" viram "-UF") ao nome de exibição de OUTRO clube. Marca "MESMO ANO" quando os dois jogam no período.
Saída: SCRATCH/CL/nomes_cruzados.txt. Uso: python revisao/CL/nomes_cruzados.py <SCRATCH>
"""
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]) / "CL"
L = json.loads((OUT / "mestre.json").read_text(encoding="utf-8"))


def k(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()
    s = re.sub(r"\s*[(/-]\s*([a-z]{2})\)?$", lambda m: "-" + m.group(1), s)
    return re.sub(r"[^a-z0-9-]", "", s)


anos = {c["exib"]: {a for v in c["anos"].values() for a in v} for c in L}
por_chave = {}
for c in L:
    por_chave.setdefault(k(c["exib"]), []).append(c["exib"])
nomes = []   # (clube, fonte, nome, a1, a2, origem)
for c in L:
    for n in c["nomes"]:
        fonte, resto = n.split(":", 1)
        nome, per = resto.rsplit(":", 1)
        a1, _, a2 = per.partition("-")
        nomes.append((c["exib"], fonte, nome, int(a1) if a1 else None, int(a2) if a2 else None, "banco"))
for f in sorted((ROOT / "data" / "coleta").glob("bra-*/pacote/clubes.csv")):
    for r in csv.DictReader(f.open(encoding="utf-8")):
        for item in filter(None, (r.get("nomes_fonte") or "").split("|")):
            fonte, resto = item.split(":", 1)
            nome, per = resto.rsplit(":", 1)
            a1, _, a2 = per.partition("-")
            nomes.append((r["clube"], fonte, nome, int(a1), int(a2 or a1), f.parts[-3]))
out = []
vistos = set()
for clube, fonte, nome, a1, a2, orig in nomes:
    for o in por_chave.get(k(nome), []):
        if o == clube or (clube, fonte, nome, o) in vistos:
            continue
        vistos.add((clube, fonte, nome, o))
        faixa = set(range(a1, a2 + 1)) if a1 else set()
        comum = sorted(faixa & anos.get(o, set()) & anos.get(clube, set()))
        out.append(f"{clube} <- {fonte}:{nome}:{a1}-{a2} ({orig})  = nome de '{o}'  {'MESMO ANO ' + str(comum) if comum else ''}")
(OUT / "nomes_cruzados.txt").write_text("\n".join(sorted(out)), encoding="utf-8")
print(len(out), "casos;", sum("MESMO ANO" in x for x in out), "no mesmo ano")
