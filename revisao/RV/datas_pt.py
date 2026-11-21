"""Confere as datas da Série B (1990, 1991, 1997, 1998, 1989, 2009) com as listas de jogos 'dd/mm/aaaa - A NxM B' da Wikipédia pt (cache da 1ª rodada)."""
import json, re, glob, sys, unicodedata, sqlite3
from collections import Counter
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(clube|do|de|da|esporte|futebol|sport|recife|ec|fc|ac|-..)\b", " ", s)
    return re.sub(r"[^a-z ]", " ", s).split()
def casa(a, b):
    a, b = norm(a), norm(b)
    return bool(a and b and (a[0] in b or b[0] in a))
for ano in sys.argv[1:]:
    fs = [f for f in glob.glob("data/cache/revisao/SB/pt.wikipedia*") if f"de_{ano}_-_S" in f]
    if not fs: print(ano, "sem página"); continue
    t = open(fs[0], encoding="utf-8").read()
    try: t = json.loads(t)["parse"]["wikitext"]["*"]
    except Exception: pass
    pt = re.findall(r"(\d{2})/(\d{2})/(\d{4})\s*-\s*([^\n\t|]+?)\s*(\d+)\s*[xX×]\s*(\d+)\s*([^\n\t|]+?)(?:\s+-\s+|\s*$|\s*\n|\s*\|)", t, re.M)
    db = c.execute("""select p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
        join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id where co.slug='bra-serie-b' and e.temporada=?""", (ano,)).fetchall()
    res = Counter(); erros = []
    for d, mth, y, a, ga, gb, b in pt:
        data = f"{y}-{mth}-{d}"; ga, gb = int(ga), int(gb)
        cand = [x for x in db if x[2] == ga and x[3] == gb and casa(a, x[1]) and casa(b, x[4])]
        if not cand: res["sem par"] += 1; continue
        if any(x[0] == data for x in cand): res["data igual"] += 1
        else:
            res["data diferente"] += 1; erros.append((data, a.strip(), ga, gb, b.strip(), [x[0] for x in cand]))
    print(ano, "jogos na pt:", len(pt), dict(res))
    for e in erros[:12]: print("   ", e)
