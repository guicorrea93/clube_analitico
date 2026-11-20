"""Cruza as diferenças da classificação antiga: só fica o que a Wikipédia en e a pt dizem igual e o painel diz diferente."""
import json, sys
en = json.load(open(sys.argv[1], encoding="utf-8")); pt = json.load(open(sys.argv[2], encoding="utf-8"))
for ano in sorted(en):
    de = {c: (a, b) for c, a, b, *_ in en[ano]["difs"]}
    dp = {c: (a, b) for c, a, b, *_ in pt.get(ano, {"difs": []})["difs"]}
    fortes = [(c, de[c][0], de[c][1]) for c in de if c in dp and list(de[c][1]) == list(dp[c][1])]
    so_en = [c for c in de if c not in dp]
    so_pt = [c for c in dp if c not in de]
    if fortes or so_en or so_pt:
        print(ano, "| en e pt iguais, painel diferente:", len(fortes), "| só en:", so_en, "| só pt:", so_pt)
        for c, a, b in fortes: print("     ", c, "painel", a, "fontes", b)
