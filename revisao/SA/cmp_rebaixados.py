"""B: rebaixados 2003-2025 — sub-aba Participantes (para onde o clube foi no ano seguinte) x Wikipédia en (resultN=R/REL)."""
import sys, re
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
from sportstable import tabelas, ler
from nomes import casar
d = painel()
for e in d["EDS"]:
    if e["ano"] < 2003: continue
    wt = wikitext("en", f"{e['ano']} Campeonato Brasileiro Série A")
    linhas, p = ler(tabelas(wt)[0])
    alvos = [r[0] for r in e["tab"]]
    reb_w = set()
    for w in linhas:
        r = p.get(f"result{w['pos']}", "") or ""
        st = w["status"]
        if r.upper() in ("R", "REL") or st == "R" or r.upper().startswith("REL"):
            reb_w.add(casar(w["nome"], alvos))
    caiu = {r[0] for r, mv in zip(e["tab"], e["mv"]) if mv[1] is not None and mv[1] > 1}
    z = None
    if e["cor"]:
        z = [f for f in e["cor"]["faixas"] if f[2] == "rebaixamento"]
    zona = {r[0] for r in e["tab"] if z and any(a <= r[1] <= b for a, b, _ in z)}
    print(e["ano"], "wiki:", sorted(reb_w), "| painel caiu (ano seguinte):", sorted(caiu) if e["ano"] < 2025 else "(2026 fora do banco)", "| zona na tabela do painel:", sorted(zona),
          "" if reb_w == zona else "  <== ZONA DIFERENTE", "" if e["ano"] == 2025 or reb_w == caiu else "  <== CAIU DIFERENTE")
