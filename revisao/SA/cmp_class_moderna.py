"""B: classificação final 2003-2025 do painel x Wikipédia (en), módulo sports table."""
import sys, json, csv
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
from sportstable import tabelas, ler
from nomes import casar
d = painel()
saida = []
for e in d["EDS"]:
    if e["ano"] < 2003: continue
    pagina = f"{e['ano']} Campeonato Brasileiro Série A"
    wt = wikitext("en", pagina)
    tb = tabelas(wt)
    linhas, p = ler(tb[0])
    alvos = [r[0] for r in e["tab"]]
    tabp = {r[0]: r for r in e["tab"]}
    difs = []
    if len(linhas) != len(alvos): difs.append(f"nº de clubes painel {len(alvos)} x wiki {len(linhas)}")
    for w in linhas:
        c = casar(w["nome"], alvos)
        if not c: difs.append(f"clube da wiki sem par: {w['nome']}"); continue
        r = tabp[c]; pts_p = e["pv"]*r[3] + r[4]
        a = (r[1], r[2], r[3], r[4], r[5], r[6], r[7], pts_p)
        b = (w["pos"], w["j"], w["v"], w["e"], w["d"], w["gp"], w["gc"], w["pts"])
        if a != b:
            difs.append(f"{c}: painel pos/J/V/E/D/GP/GC/Pts={a} wiki={b} adj={w['adj']} {w['nota'][:80]}")
    print(e["ano"], "OK" if not difs else f"{len(difs)} diferenças")
    for x in difs: print("   ", x)
    saida.append({"ano": e["ano"], "difs": difs, "url": "https://en.wikipedia.org/wiki/" + pagina.replace(" ", "_")})
json.dump(saida, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
