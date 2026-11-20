"""Lê a tabela 'Artilheiros / Ano a ano' da Wikipédia pt (página da Série B) e grava JSON."""
import json, re, sys, glob, os
RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
f = [x for x in glob.glob(os.path.join(RAIZ, "data/cache/revisao/SB/pt.wikipedia*Futebol_-_S_C3_A9rie_B_prop*.txt"))][0]
t = open(f, encoding="utf8").read()
i = t.index("=== Ano a ano ==="); j = t.index("|}", i)
bloco = t[i:j]
linhas = [l for l in bloco.split("\n|-")[1:] if not l.strip().startswith("!")]
def limpa(x):
    x = re.sub(r"<span title=\"[^\"]*\">(.*?)</span>", r"\1", x)
    x = re.sub(r"\{\{Futebol ([^|}]+)[^}]*\}\}", r"\1", x)
    x = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", x)
    x = re.sub(r"<ref.*?(</ref>|/>)", "", x)
    x = re.sub(r"(rowspan|align|colspan)=[^|\s]+\s*", "", x)
    x = re.sub(r"\{\{[^}]*\}\}", "", x)
    return x.strip().strip("|").strip()
res = []
ano = gols = None; resto_ano = resto_gols = 0
for l in linhas:
    cels = [c for c in re.split(r"\n\|", "\n" + l.strip()) if c.strip()]
    cels = [c for c in cels]
    if resto_ano:
        resto_ano -= 1
        jog, clube = limpa(cels[0]), limpa(cels[1])
        g = gols if resto_gols else int(re.sub(r"\D", "", limpa(cels[2])) or 0)
        if resto_gols: resto_gols -= 1
    else:
        a = cels[0]
        m = re.search(r"rowspan=\"?(\d)", a)
        ano = int(re.findall(r"(\d{4})", a)[-1])
        resto_ano = int(m.group(1)) - 1 if m else 0
        if "Sem registro" in cels[1]:
            res.append({"ano": ano, "jogador": None, "clube": None, "gols": None}); continue
        jog, clube = limpa(cels[1]), limpa(cels[2])
        m2 = re.search(r"rowspan=\"?(\d)", cels[3])
        gols = int(re.sub(r"\D", "", limpa(cels[3])))
        resto_gols = int(m2.group(1)) - 1 if m2 else 0
        g = gols
    res.append({"ano": ano, "jogador": jog, "clube": clube, "gols": g})
json.dump(res, sys.stdout, ensure_ascii=False, indent=0)
