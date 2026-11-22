"""Acesso e rebaixamento da A2 x participantes do ano seguinte (A1 no pacote bra-sp-1, A2 no próprio pacote).
Para cada temporada: quem está na A1 do ano seguinte (subiu) e quem some da A2 e da A1 no ano seguinte (caiu ou saiu)."""
import csv, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
def cf(slug):
    d = defaultdict(dict)
    for r in csv.DictReader(open(f"data/coleta/{slug}/pacote/classificacao_final.csv", encoding="utf-8")):
        d[r["temporada"][:4]][r["clube"]] = r
    return d
a2, a1 = cf("bra-sp-2"), cf("bra-sp-1")
anos = sorted(a2)
for t in anos:
    prox = str(int(t) + 1)
    s = a2[t]; n1 = set(a1.get(prox, {})); n2 = set(a2.get(prox, {}))
    subiu = {c for c in s if c in n1 and c not in a1.get(t, {})}
    marcado = {c for c, r in s.items() if r["situacao"] == "acesso"}
    camp_vice_subiu = {c for c, r in s.items() if r["situacao"] in ("campeao", "vice") and c in n1}
    caiu_dado = {c for c, r in s.items() if r["situacao"] == "rebaixado"}
    sumiu = {c for c in s if prox in a2 and c not in n2 and c not in n1} if prox in a2 else set()
    p = []
    if subiu - marcado - camp_vice_subiu: p.append(f"na A1 de {prox} sem 'acesso': {sorted(subiu - marcado - camp_vice_subiu)}")
    if marcado - subiu: p.append(f"'acesso' sem estar na A1 de {prox}: {sorted(marcado - subiu)}")
    if prox in a2 and caiu_dado - sumiu: p.append(f"'rebaixado' mas está na A2/A1 de {prox}: {sorted(caiu_dado - sumiu)}")
    if prox in a2 and sumiu - caiu_dado: p.append(f"some em {prox} sem 'rebaixado': {sorted(sumiu - caiu_dado)}")
    print(t, f"subiu={sorted(subiu)}", f"rebaixados={sorted(caiu_dado)}")
    for x in p: print("   !", x)
