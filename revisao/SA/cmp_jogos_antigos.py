"""C: placares antigos do painel x matriz (sports results) e footballbox da Wikipédia en (1979, 1993, Robertão 1967-1970)."""
import sys, re
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
from nomes import casar, chave
EX = {"vasco da gama": "Vasco", "atletico mineiro": "Atlético-MG", "atletico paranaense": "Athletico-PR", "america de natal": "América-RN",
      "desportiva capixaba": "Desportiva-ES", "brasil pel": "Brasil de Pelotas", "comercial sp": "Comercial-RP", "operario cg": "Operário-MS",
      "america rj": "América-RJ", "botafogo sp": "Botafogo-SP", "botafogo pb": "Botafogo-PB"}
d = painel()
def comparar(ed, wt):
    alvos = [r[0] for r in ed["tab"]]
    def cs(n):
        x = EX.get(chave(n)); return x if x in alvos else casar(n, alvos)
    wt2 = re.sub(r"<!--.*?-->", "", wt, flags=re.S)
    codes = dict(re.findall(r"\|\s*name_([A-Z0-9]+)\s*=\s*(?:\{\{[^}]*\}\}\s*)?\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", wt2))
    wt3 = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", lambda m: m.group(1), wt2)
    pares = []
    for a, b, sc in re.findall(r"\|\s*match_([A-Z0-9]+)_([A-Z0-9]+)\s*=\s*([^|\n]*)", wt3):
        m = re.search(r"(\d+)\s*[–\-−]\s*(\d+)", sc)
        if m and a in codes and b in codes: pares.append((cs(codes[a]), cs(codes[b]), int(m.group(1)), int(m.group(2)), "matriz"))
    for fb in re.findall(r"\{\{\s*[Ff]oot(?:ball)? ?box[^{}]*(?:\{\{[^{}]*\}\}[^{}]*)*\}\}", wt3):
        t1 = re.search(r"\|\s*team1\s*=\s*([^|\n]*)", fb); t2 = re.search(r"\|\s*team2\s*=\s*([^|\n]*)", fb); s = re.search(r"\|\s*score\s*=\s*([^|\n]*)", fb)
        if t1 and t2 and s:
            m = re.search(r"(\d+)\s*[–\-−]\s*(\d+)", s.group(1))
            n1 = re.sub(r"\{\{[^}]*\}\}", "", t1.group(1)).strip(); n2 = re.sub(r"\{\{[^}]*\}\}", "", t2.group(1)).strip()
            if m: pares.append((cs(n1), cs(n2), int(m.group(1)), int(m.group(2)), "footballbox"))
    pj = {}
    for g, mi, vi, gm, gv, sg in ed["jogos"]:
        pj.setdefault((alvos[mi], alvos[vi]), []).append((gm, gv, ed["grupos"][g]))
    ok, difs, sem = 0, [], 0
    for a, b, gm, gv, tipo in pares:
        if not a or not b: sem += 1; continue
        js = pj.get((a, b), [])
        if any((x[0], x[1]) == (gm, gv) for x in js): ok += 1
        else: difs.append(f"{a} x {b} fonte {gm}-{gv} ({tipo}) | painel {[(x[0], x[1], x[2]) for x in js] or 'sem esse jogo'}")
    return len(pares), ok, difs, sem
for ed, pag in [("1979", "1979 Campeonato Brasileiro Série A"), ("1993", "1993 Campeonato Brasileiro Série A"),
                ("1967_robertao", "1967 Torneio Roberto Gomes Pedrosa"), ("1968_robertao", "1968 Torneio Roberto Gomes Pedrosa"),
                ("1969", "1969 Torneio Roberto Gomes Pedrosa"), ("1970", "1970 Torneio Roberto Gomes Pedrosa"),
                ("1998", "1998 Campeonato Brasileiro Série A"), ("1999", "1999 Campeonato Brasileiro Série A"), ("1971", "1971 Campeonato Brasileiro Série A"),
                ("1975", "1975 Campeonato Brasileiro Série A"), ("1987", "1987 Campeonato Brasileiro Série A")]:
    e = [x for x in d["EDS"] if x["id"] == ed][0]
    n, ok, difs, sem = comparar(e, wikitext("en", pag))
    print(ed, "jogos na fonte", n, "| iguais", ok, "| diferentes", len(difs), "| sem par de clube", sem)
    for x in difs[:15]: print("    ", x)
