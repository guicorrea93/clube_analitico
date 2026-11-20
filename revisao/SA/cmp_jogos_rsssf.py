"""C: placares do painel x lista de jogos da RSSSF (anos sem matriz na Wikipédia: 2004, 2005, 2008)."""
import sys, re
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from rsssf_busca import txt
from nomes import casar
EXTRA = {"vasco da gama": "Vasco", "atletico pr": "Athletico-PR", "atletico mg": "Atlético-MG", "atletico go": "Atlético-GO"}
def jogos_rsssf(url):
    out = []
    for l in txt(url).splitlines():
        m = re.match(r"^([A-Za-zÀ-ÿ][^\d\[\]]*?)\s{1,}(\d+)-(\d+|awd)\s+([A-Za-zÀ-ÿ][^\[\]\d]*?)\s*(\[.*)?$", l.replace("\t", "  ").rstrip())
        if m and "annulled" not in (m.group(5) or "") and "abandoned" not in (m.group(5) or ""):
            out.append((m.group(1).strip(), int(m.group(2)), int(m.group(3)), m.group(4).strip(), (m.group(5) or "")[:60]))
        m2 = re.match(r"^(\S.*?)\s+awd\s+(\S.*?)\s+\[awarded (\d+)-(\d+), originally (\d+)-(\d+)\]", l.strip())
        if m2:
            out.append((m2.group(1).strip(), int(m2.group(3)), int(m2.group(4)), m2.group(2).strip(), "awd orig " + m2.group(5) + "-" + m2.group(6)))
    return out
d = painel()
for ano, url in [(2004, "https://www.rsssf.org/tablesb/braz04.html"), (2005, "https://www.rsssf.org/tablesb/braz05.html"), (2008, "https://www.rsssf.org/tablesb/braz08.html")]:
    e = [x for x in d["EDS"] if x["ano"] == ano][0]
    alvos = [r[0] for r in e["tab"]]
    def cs(n):
        from nomes import chave
        return EXTRA.get(chave(n)) or casar(n, alvos)
    pj = {}
    for g, mi, vi, gm, gv, sg in e["jogos"]:
        pj.setdefault((alvos[mi], alvos[vi]), []).append((gm, gv, g + 1))
    rs = jogos_rsssf(url)
    vistos, difs, sem = set(), [], []
    for a, gm, gv, b, nota in rs:
        ca, cb = cs(a), cs(b)
        if not ca or not cb: sem.append((a, b)); continue
        if (ca, cb) in vistos: continue
        vistos.add((ca, cb))
        p = pj.get((ca, cb))
        if not p: difs.append(f"{ca} x {cb}: não está no painel (rsssf {gm}-{gv} {nota})"); continue
        if (p[0][0], p[0][1]) != (gm, gv): difs.append(f"{ca} x {cb} (rodada {p[0][2]}): painel {p[0][0]}-{p[0][1]} x rsssf {gm}-{gv} {nota}")
    print(ano, "jogos rsssf lidos", len(rs), "pares casados", len(vistos), "de", len(e["jogos"]), "| diferenças", len(difs), "| sem par", len(sem), sem[:5])
    for x in difs: print("    ", x)
    faltam = set(pj) - vistos
    if faltam: print("    jogos do painel sem par na rsssf:", sorted(faltam)[:10])
