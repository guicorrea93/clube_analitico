"""Revisão CL: suspeitos de cadastro duplicado e de clubes juntados.

Lê SCRATCH/CL/mestre.json (de mestre.py) e grava SCRATCH/CL/suspeitos.txt com:
 1. mesma chave de nome (sem siglas EC/SE/AA/FC..., sem -UF) e mesma UF;
 2. mesma cidade e UF, anos que nunca se cruzam (candidato a duplicata: nome antigo x novo);
 3. intervalo grande entre aparições (candidato a dois clubes juntados);
 4. nomes de fonte muito diferentes do nome de exibição;
 5. sufixo -UF: com sufixo sem homônimo, homônimo sem sufixo, sufixo diferente da UF.
Uso: python revisao/CL/duplicados.py <SCRATCH>
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

OUT = Path(sys.argv[1]) / "CL"
L = json.loads((OUT / "mestre.json").read_text(encoding="utf-8"))
SIGLAS = r"\b(ec|se|aa|fc|ge|sc|ac|ad|cr|ce|sd|ser|cea|aec|ea|sa|esporte|clube|club|futebol|atletico|associacao|sociedade|esportiva|de|do|da|e)\b"


def sem_acento(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def base(n):
    return re.sub(r"-[A-Z]{2}$", "", n)


def chave(n):
    s = sem_acento(base(n))
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(SIGLAS, " ", s)
    return " ".join(s.split())


def todos_anos(c):
    return sorted({a for v in c["anos"].values() for a in v})


def faixa(c):
    return "; ".join(f"{k[4:]}:{','.join(str(a) for a in v)}" for k, v in c["anos"].items())


out = []
p = out.append

p("== 1. mesma chave de nome e mesma UF ==")
g = defaultdict(list)
for c in L:
    g[(chave(c["exib"]), c["regiao"])].append(c)
for k, cs in sorted(g.items()):
    if len(cs) > 1:
        p(f"{k}:")
        for c in cs:
            p(f"   [{c['id']}] {c['exib']} | {c['cidade']} | {c['nome_completo']} | {faixa(c)}")

p("\n== 1b. mesma chave de nome, UF diferente (homônimos; conferir sufixo) ==")
g2 = defaultdict(list)
for c in L:
    g2[chave(c["exib"])].append(c)
for k, cs in sorted(g2.items()):
    if len({c["regiao"] for c in cs}) > 1:
        p(f"{k}: " + " ; ".join(f"{c['exib']}({c['regiao']}/{c['cidade']})" for c in cs))

p("\n== 2. mesma cidade e UF, anos que nunca se cruzam ==")
g3 = defaultdict(list)
for c in L:
    if c["cidade"]:
        g3[(sem_acento(c["cidade"]), c["regiao"])].append(c)
for k, cs in sorted(g3.items()):
    if len(cs) < 2:
        continue
    pares = []
    for i, a in enumerate(cs):
        for b in cs[i + 1:]:
            if not set(todos_anos(a)) & set(todos_anos(b)):
                pares.append((a, b))
    if pares:
        p(f"{k}:")
        for a, b in pares:
            p(f"   {a['exib']} [{todos_anos(a)[0]}-{todos_anos(a)[-1]}]  x  {b['exib']} [{todos_anos(b)[0]}-{todos_anos(b)[-1]}]")

p("\n== 3. intervalo de 15+ anos entre aparições ==")
for c in sorted(L, key=lambda c: c["exib"]):
    a = todos_anos(c)
    gaps = [(x, y) for x, y in zip(a, a[1:]) if y - x >= 15]
    if gaps:
        p(f"   {c['exib']} ({c['regiao']}/{c['cidade']}): {gaps} | {faixa(c)}")

p("\n== 4. nomes de fonte diferentes do nome de exibição ==")
for c in sorted(L, key=lambda c: c["exib"]):
    k = chave(c["exib"])
    outros = sorted({n.split(":")[1] for n in c["nomes"] if chave(n.split(":")[1]) != k
                     and k not in chave(n.split(":")[1]) and chave(n.split(":")[1]) not in k})
    if outros:
        p(f"   {c['exib']} ({c['regiao']}/{c['cidade']}): {outros}")

p("\n== 5. sufixo -UF ==")
porbase = defaultdict(list)
for c in L:
    porbase[sem_acento(base(c["exib"]))].append(c)
for b, cs in sorted(porbase.items()):
    for c in cs:
        m = re.search(r"-([A-Z]{2})$", c["exib"])
        if m and m.group(1) != c["regiao"]:
            p(f"   sufixo diferente da UF: {c['exib']} (UF {c['regiao']})")
        if m and len(cs) == 1:
            p(f"   sufixo sem homônimo no banco: {c['exib']}")
    sem = [c for c in cs if not re.search(r"-[A-Z]{2}$", c["exib"])]
    if len(cs) > 1 and len(sem) > 0:
        p(f"   homônimos: {[x['exib'] + '(' + x['regiao'] + ')' for x in cs]}")

(OUT / "suspeitos.txt").write_text("\n".join(out), encoding="utf-8")
print(len(out), "linhas")
