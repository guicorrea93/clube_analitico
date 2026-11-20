"""A: campeão, vice e 3º; D: artilheiro — painel x 'List of Brazilian football champions' (Wikipédia en)."""
import sys, re, json
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from lista_campeoes import linhas
from nomes import casar, chave
d = painel()
L = [r for r in linhas() if r["campeao"]]
for r in L:
    r["ano"] = int(re.sub(r"\D", "", r["ano"].split("|")[-1])); r["gols"] = int(re.sub(r"\D", "", r["gols"].split("|")[-1]) or 0)
todos = sorted({x[0] for e in d["EDS"] for x in e["tab"]})
EX = {"vasco da gama": "Vasco", "atletico mineiro": "Atlético-MG", "atletico paranaense": "Athletico-PR", "america": "América-RJ",
      "rio branco": "Rio Branco-ES", "operario": "Operário-MS", "sport recife": "Sport", "brasil de pelotas": "Brasil de Pelotas"}
def cs(n): return EX.get(chave(n)) or casar(n, todos)
# pares na mesma ordem (1967 e 1968 têm duas edições: Robertão vem primeiro no painel e na lista)
eds = d["ED"]
assert len(eds) == len(L), (len(eds), len(L))
pod_dif, art_out = [], []
for e, w, ed in zip(eds, L, d["EDS"]):
    assert e["ano"] == w["ano"]
    for k in ("campeao", "vice", "terceiro"):
        if e.get(k) != cs(w[k]):
            pod_dif.append((e["ano"], e["comp"], k, e.get(k), w[k]))
    a = ed["art"]
    top = [x for x in a if a and x[2] == a[0][2]] if a else []
    art_out.append((e["ano"], e["comp"], w["art"], w["gols"], [(x[0], x[1], x[2]) for x in top]))
print("PÓDIO: diferenças", len(pod_dif))
for x in pod_dif: print("   ", x)
print("ARTILHEIROS (lista x painel):")
for ano, comp, wa, wg, top in art_out:
    ok = ""
    if top:
        ok = "OK" if top[0][2] == wg else "GOLS DIFERENTES"
    print(f"   {ano} {comp}: lista={wa} ({wg}) | painel={top if top else 'sem artilharia'} {ok}")
