"""Artilheiro de cada temporada: banco (artilheiro) e painel (artof) x RSSSF engtops.html (lista de J.M. Ross)."""
import re, sys, json, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, baixar
URL = "https://www.rsssf.org/tablese/engtops.html"
txt = baixar(URL).decode("latin-1")
rs = {}  # ano_fim -> [(nome, gols)]
blocos = re.split(r'<A NAME="', txt, flags=re.I)
for bl in blocos:
    if not re.match(r'(1889-1|1920-1|1947-1|1993-p|2005-p)"', bl): continue
    pre = re.search(r"<PRE>(.*?)</PRE>", bl, re.S | re.I).group(1)
    if "Div 3" in pre[:200] or "Division Three" in pre[:300]: pass
    ano = None; pend = None
    for ln in re.sub(r"<[^>]+>", "", pre).splitlines():
        left = ln[:40]
        m = re.match(r"^(\d{4})?\s+(\S.*?)\s{2,}(.*?)\s+(\d+)?\s*$", left)
        if re.match(r"^\s*(Football League|Division|Premier)", left): continue
        if not left.strip(): continue
        y = left[:4].strip()
        if y.isdigit(): ano = int(y)
        nome = left[6:22].strip(); clube = left[22:36].strip(); g = left[36:40].strip()
        if not nome and not clube: continue
        if nome:
            pend = [nome, g]
            if g.isdigit(): rs.setdefault(ano, []).append((nome, int(g)))
        elif pend and g.isdigit():  # gols na linha de baixo (clube/clube)
            rs.setdefault(ano, []).append((pend[0], int(g)))
def sob(n):
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().lower()
    n = n.replace("van nistelrooy", "nistelrooij").replace("v.nistelrooij", "nistelrooij")
    return re.split(r"[.\s]", n.strip())[-1]
c = banco()
d = json.loads(open("painel/dados/eng-1.js", encoding="utf-8").read().split("=", 1)[1].strip().rstrip(";"))
artof = {e["t"]: e["artof"] for e in d["EDS"]}
ok = dif = 0
for eid, t, ai, af in temporadas(c):
    bd = c.execute("select jogador, gols from artilheiro where edicao_id=?", (eid,)).fetchall()
    fo = rs.get(ai + 1, [])
    sb = sorted((sob(n), g) for n, g in bd); sf = sorted((sob(n), g) for n, g in fo)
    pn = sorted((sob(x[0]), x[2]) for x in artof.get(t, []))
    if sb == sf and pn == sb: ok += 1; continue
    dif += 1
    print(f"{t}\tbanco={bd}\tpainel={[(x[0], x[2]) for x in artof.get(t, [])]}\trsssf={fo}")
print("iguais", ok, "diferentes", dif)
