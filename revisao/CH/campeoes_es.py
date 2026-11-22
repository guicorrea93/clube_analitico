"""Campeão e vice: pacote (edicoes.csv) x Wikipédia em espanhol ("Primera División de Chile", seção Historial).
Uso: python -I revisao/CH/campeoes_es.py"""
import csv, re, unicodedata
txt = open("data/cache/revisao/CH/es_Primera_Division_de_Chile.txt", encoding="utf-8").read()
sec = txt[txt.index("== Historial =="):txt.index("== Palmarés ==")]
def limpa(s):
    s = re.sub(r"\{\{[^}]*\}\}", "", s)
    s = re.sub(r"\[\[([^|\]]*\|)?([^\]]*)\]\]", r"\2", s)
    s = re.sub(r"<ref.*?(</ref>|/>)", "", s)
    s = re.sub(r"'''|''|\(\d+\)", "", s)
    return s.strip(" |")
linhas = []
for bloco in sec.split("|-")[1:]:
    cel = [limpa(c) for c in re.split(r"\n\|", "\n" + bloco.strip()) if c.strip()]
    cel = [re.sub(r"^align=center\s*\|\s*", "", c) for c in cel]
    if len(cel) >= 3 and re.search(r"\d{4}", cel[0]):
        linhas.append(cel[:3])
def ch(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("-", " ")
    return {"green cross": "deportes temuco", "everton": "everton de vina del mar", "rangers": "rangers de talca",
            "audax italiano la florida": "audax italiano", "nublense": "nublense"}.get(s.strip(), s.strip())
ed = list(csv.DictReader(open("data/coleta/chi-1/pacote/edicoes.csv", encoding="utf-8")))
print(len(linhas), "linhas na Wikipédia;", len(ed), "edições no pacote")
def chave_t(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    a = re.search(r"\d{4}", t).group()
    m = re.match(r"(\d{4})/(\d\d) clausura", t)
    if m: a = m.group(1)[:2] + m.group(2)
    tor = "ap" if "apert" in t else "cl" if "claus" in t else "tr" if "trans" in t else ""
    return a, tor
wk = {}
for c in linhas:
    wk.setdefault(chave_t(c[0]), []).append(c)
ok = 0
for r in ed:
    k = chave_t(r["temporada"])
    if k[1] == "" and k not in wk:
        pass
    w = wk.get(k) or wk.get((k[0], ""))
    if not w:
        print("sem linha na Wikipédia:", r["temporada"]); continue
    w = w[0]
    dif = []
    if ch(w[1]) != ch(r["campeao"]): dif.append(f"campeão pacote {r['campeao']} / es.wiki {w[1]}")
    if ch(w[2]) != ch(r["vice"]): dif.append(f"vice pacote {r['vice']} / es.wiki {w[2]}")
    if dif: print(r["temporada"], "|", "; ".join(dif), "| es.wiki:", w[0])
    else: ok += 1
print("iguais:", ok)
