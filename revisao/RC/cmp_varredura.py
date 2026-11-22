"""Compara a varredura RC (todas as competições) com as saídas anteriores (RV, SP, AR, UY, ES, EN). Uso: python -I revisao/RC/cmp_varredura.py"""
import sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
S = r"C:\Users\GUILHE~1\AppData\Local\Temp\claude\c--Users-guilhermecorrea-Downloads-Gui-GitHub\a75361b9-f474-4b01-be59-ef64c90aa262\scratchpad"
def ler(p):
    b = open(p, "rb").read()
    try: t = b.decode("utf-8")
    except UnicodeDecodeError: t = b.decode("cp1252")
    return [tuple(l.rstrip("\r").split("\t", 3)) for l in t.splitlines() if l.count("\t") >= 3]
novo = ler(S + r"\RC\varredura_saida.txt")
velhos = {"RV (21/11)": S + r"\RV\varredura_saida.txt", "SP": "revisao/SP/varredura_saida.txt", "AR": "revisao/AR/varredura_saida.txt",
          "UY": "revisao/UY/saida_varredura.txt", "ES": S + r"\ES\varredura.txt", "EN": S + r"\EN\varredura.txt"}
for rot, p in velhos.items():
    try: v = ler(p)
    except FileNotFoundError: print(rot, "sem arquivo"); continue
    slugs = {x[0] for x in v} or ({"esp-1"} if rot == "ES" else {"eng-1"} if rot == "EN" else set())
    n = [x for x in novo if x[0] in slugs]
    cv, cn = Counter((x[0], x[2]) for x in v), Counter((x[0], x[2]) for x in n)
    print(f"== {rot}: {len(v)} linhas antes, {len(n)} agora ({sorted(slugs)})")
    for k in sorted(set(cv) | set(cn)):
        if cv[k] != cn[k]: print(f"   {k[0]:20} {k[1]:35} {cv[k]:4} -> {cn[k]:4}")
    sv = {(x[0], x[1], x[2], x[3]) for x in v}
    novas = [x for x in n if x not in sv and x[2] not in ("'Grupo Grupo'",)]
    print(f"   linhas novas: {len(novas)}")
    for x in novas[:40]: print("     +", " | ".join(x)[:230])
