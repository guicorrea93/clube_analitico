"""Atualiza docs/revisao/achados.csv: aplica reconferências (id,situacao_nova,nota) e acrescenta achados novos."""
import csv, sys, os
S = sys.argv[1]
ARQ = "docs/revisao/achados.csv"
CAB = "id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao".split(",")
rs = list(csv.DictReader(open(ARQ, encoding="utf-8")))
idx = {r["id"]: r for r in rs}
for f in sys.argv[2:]:
    p = os.path.join(S, f)
    if f.startswith("sugestoes"):
        n = 0
        for u in csv.DictReader(open(p, encoding="utf-8-sig")):
            r = idx[u["id"]]
            s = u["sugestao"].strip()
            if s in r["o_que_a_fonte_diz"]: continue
            r["o_que_a_fonte_diz"] += (" | COMPLEMENTO (22/11): " if "SUGESTÃO" in r["o_que_a_fonte_diz"] else " | SUGESTÃO: ") + s; n += 1
        print(f, "sugestões", n)
    elif f.startswith("reconferencia"):
        n = 0
        for u in csv.DictReader(open(p, encoding="utf-8-sig")):
            assert u["situacao_nova"] in ("corrigido", "aberto", "nao-e-erro"), u
            idx[u["id"]]["situacao"] = u["situacao_nova"]; n += 1
        print(f, "atualizados", n)
    else:
        n = 0
        for r in csv.DictReader(open(p, encoding="utf-8-sig")):
            assert list(r.keys()) == CAB, (f, list(r.keys()))
            assert r["gravidade"] in ("alta", "media", "baixa") and r["situacao"] in ("aberto", "nao-e-erro"), r["id"]
            assert r["quem_corrige"].split(";")[0].strip() in ("coleta-brasil", "coleta-europa", "coleta-sulamerica", "banco-painel"), r["id"]
            if r["id"] in idx: idx[r["id"]].update(r)
            else: rs.append(r); idx[r["id"]] = r; n += 1
        print(f, "novos", n)
with open(ARQ, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, CAB); w.writeheader(); w.writerows(rs)
from collections import Counter
print(len(rs), Counter(r["situacao"] for r in rs))
