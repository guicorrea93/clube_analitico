"""Revisão CL: junta as fichas do ogol guardadas pela coleta (C, D, Copa) com o cadastro do banco.

Saída: SCRATCH/CL/ogol_por_clube.json (nome de exibição -> [fichas do ogol]) e ogol_resumo.txt
(clubes com mais de um código do ogol; código do ogol usado por mais de um clube; fundação depois do 1º ano em que joga;
UF/cidade do banco diferente da ficha).
Uso: python revisao/CL/ogol_fichas.py <SCRATCH>
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]) / "CL"
fichas = {}
for s in ["bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"]:
    f = ROOT / "data" / "coleta" / s / "ogol" / "clubes.json"
    for k, v in json.loads(f.read_text(encoding="utf-8")).items():
        fichas.setdefault(k, v)
comum = json.loads((ROOT / "data" / "coleta" / "comum" / "clubes_ogol.json").read_text(encoding="utf-8"))
L = {c["exib"]: c for c in json.loads((OUT / "mestre.json").read_text(encoding="utf-8"))}
por_clube = defaultdict(list)
for cod, v in comum.items():
    fi = fichas.get(cod, {})
    por_clube[v["clube"]].append({"cod": cod, **{k: fi.get(k) for k in ("nome_completo", "cidade", "uf", "fundacao", "nomes_ogol")},
                                  "comps": v.get("competicoes")})
(OUT / "ogol_por_clube.json").write_text(json.dumps(por_clube, ensure_ascii=False, indent=1), encoding="utf-8")
out = []
out.append("== clube do painel com mais de um código do ogol ==")
for c, fs in sorted(por_clube.items()):
    if len(fs) > 1:
        out.append(f"{c}: " + " ; ".join(f"{x['cod']} {x['nome_completo']} ({x['cidade']}/{x['uf']}, fund. {x['fundacao']}) {x['nomes_ogol']}" for x in fs))
out.append("\n== nome do pacote sem clube no banco ==")
for c in sorted(por_clube):
    if c not in L:
        out.append(f"   {c}")
out.append("\n== fundação depois do 1º ano em que o clube joga ==")
for c, fs in sorted(por_clube.items()):
    if c not in L:
        continue
    anos = sorted({a for v in L[c]["anos"].values() for a in v})
    for x in fs:
        fu = (x.get("fundacao") or "")[:4]
        if fu.isdigit() and anos and int(fu) > anos[0]:
            out.append(f"   {c}: fundado {x['fundacao']} ({x['nome_completo']}, ogol {x['cod']}), joga desde {anos[0]}: {anos}")
out.append("\n== UF/cidade do banco diferente da ficha do ogol ==")
for c, fs in sorted(por_clube.items()):
    if c not in L:
        continue
    for x in fs:
        if x.get("uf") and x["uf"] != L[c]["regiao"]:
            out.append(f"   UF: {c} banco {L[c]['regiao']} x ogol {x['uf']} ({x['nome_completo']}, {x['cidade']})")
        if x.get("cidade") and L[c]["cidade"] and x["cidade"].lower() != L[c]["cidade"].lower():
            out.append(f"   cidade: {c} banco {L[c]['cidade']} x ogol {x['cidade']} ({x['nome_completo']})")
out.append("\n== todas as fichas (clube: nome completo, cidade/UF, fundação) ==")
for c, fs in sorted(por_clube.items()):
    for x in fs:
        out.append(f"   {c} | {x['nome_completo']} | {x['cidade']}/{x['uf']} | {x['fundacao']} | ogol {x['cod']}")
(OUT / "ogol_resumo.txt").write_text("\n".join(out), encoding="utf-8")
print(len(por_clube), "clubes com ficha;", len(out), "linhas")
