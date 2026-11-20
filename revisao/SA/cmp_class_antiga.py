"""B: classificação final 1971-2002 do painel x seção 'Final standings' da Wikipédia (en)."""
import sys, re, json
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
from sportstable import tabelas, ler
from nomes import casar, chave
EXTRA = {"vasco da gama": "Vasco", "atletico paranaense": "Athletico-PR", "atletico mineiro": "Atlético-MG",
         "america de natal": "América-RN", "desportiva capixaba": "Desportiva-ES", "operario cg": "Operário-MS",
         "comercial sp": "Comercial-RP", "brasil pel": "Brasil de Pelotas"}
def secao(wt, titulo):
    m = re.search(r"\n==\s*" + titulo + r"\s*==", wt)
    if not m: return ""
    f = re.search(r"\n==[^=]", wt[m.end():])
    return wt[m.end(): m.end() + f.start()] if f else wt[m.end():]
def wikitable(sec):
    """linhas de uma wikitable simples: lista de células (texto limpo)."""
    linhas = []
    for bloco in sec.split("\n|-")[1:]:
        cel = []
        for l in bloco.split("\n"):
            l = l.strip()
            if not l or l.startswith("|}") or l.startswith("!"): continue
            if l.startswith("|"):
                for c in l[1:].split("||"):
                    c = c.split("|", 1)[-1] if re.match(r"^\s*(style|align|bgcolor|class)=", c) else c
                    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
                    c = re.sub(r"\{\{[^}]*\}\}", "", c); c = re.sub(r"<[^>]+>", "", c)
                    cel.append(c.strip().replace("'''", ""))
        if cel: linhas.append(cel)
    return linhas
d = painel()
res = {}
anos = sorted({e["ano"] for e in d["EDS"] if 1971 <= e["ano"] <= 2002})
for e in d["EDS"]:
    if not (1971 <= e["ano"] <= 2002): continue
    wt = wikitext("en", f"{e['ano']} Campeonato Brasileiro Série A")
    sec = secao(wt, "Final standings") or secao(wt, "Standings and results") or secao(wt, "Standings")
    alvos = [r[0] for r in e["tab"]]
    def cs(n):
        x = EXTRA.get(chave(n))
        if x in alvos: return x
        if chave(n) == "maringa": return next((a for a in alvos if "Maring" in a), None)
        return casar(n, alvos)
    tb = tabelas(sec)
    wl = []
    if tb:
        linhas, p = ler(tb[-1])
        wl = [(w["pos"], w["nome"], w["j"], w["v"], w["e"], w["d"], w["gp"], w["gc"], w["pts"]) for w in linhas]
    else:
        for c in wikitable(sec):
            nums = [x for x in c if re.fullmatch(r"[−\-+]?\d+", x)]
            nome = next((x for x in c if re.search(r"[A-Za-z]", x)), None)
            if nome and len(nums) >= 7:
                n = [int(x.replace("−", "-")) for x in nums]
                wl.append((n[0], nome, n[1], n[2], n[3], n[4], n[5], n[6], n[-1]))
    tabp = {r[0]: r for r in e["tab"]}
    difs, sem = [], []
    for (pos, nome, j, v, em, dd, gp, gc, pts) in wl:
        c = cs(nome)
        if not c: sem.append(nome); continue
        r = tabp[c]
        a = (r[1], r[2], r[3], r[4], r[5], r[6], r[7]); b = (pos, j, v, em, dd, gp, gc)
        if a != b: difs.append((c, a, b, e["pv"] * r[3] + r[4], pts))
    print(e["ano"], "linhas wiki", len(wl), "painel", len(alvos), "| difs", len(difs), "| sem par", sem[:6])
    for c, a, b, pp, pw in difs[:40]:
        print(f"    {c}: painel pos/J/V/E/D/GP/GC={a} pts={pp} | wiki={b} pts={pw}")
    res[e["ano"]] = {"n_wiki": len(wl), "difs": difs, "sem": sem}
json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
