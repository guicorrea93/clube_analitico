"""Jogos em {{footballbox}} das páginas da Wikipédia pt de cada edição (as que a coleta não usou: 1979-1988, 1995-2026)
x o pacote. Casa por data e clubes (nome normalizado)."""
import sys, os, re, csv, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from baixar import wikitext
from baixar_wiki_edicoes import nome
MESES = {m: i for i, m in enumerate("janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(ec|fc|ac|aa|ae|sc|ca|ge|clube|futebol|esporte|sp|ii|de|da|do)\b", " ", s.replace("-", " "))
    return set(w for w in s.split() if len(w) > 2)
pac = list(csv.DictReader(open("data/coleta/bra-sp-2/pacote/partidas.csv", encoding="utf-8")))
ok = dif = nao = 0
anos = [int(x) for x in sys.argv[1:]] or [1979] + list(range(1985, 1989)) + list(range(1995, 2027))
for a in anos:
    w = wikitext(f"Campeonato Paulista de Futebol de {a} - {nome(a)}")
    for fb in re.findall(r"\{\{\s*[Ff]ootballbox(.*?)\n\}\}", w, re.S):
        g = lambda k: (re.search(r"\|\s*" + k + r"\s*=([^\n]*)", fb) or [None, ""])[1]
        lim = lambda s: re.sub(r"\[\[(?:Imagem|Ficheiro|File):[^\]]*\]\]|\{\{[^}]*\}\}|<[^>]+>", "", re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", re.sub(r"\[\[(?:Imagem|Ficheiro|File):[^\]]*\]\]", "", s))).strip()
        t1, t2, pl, dt = lim(g("time1")), lim(g("time2")), lim(g("placar")), lim(g("data"))
        m = re.search(r"(\d+)\s*[–-]\s*(\d+)", pl); md = re.search(r"(\d{1,2})\s+de\s+([a-zç]+)(?:\s+de\s+(\d{4}))?", dt, re.I)
        if not m or not md: continue
        d = f"{int(md.group(3) or a):04d}-{MESES.get(md.group(2).lower(), 0):02d}-{int(md.group(1)):02d}"
        cand = [p for p in pac if p["data"] == d and norm(p["mandante"]) & norm(t1) and norm(p["visitante"]) & norm(t2)]
        cand2 = [p for p in pac if p["data"] == d and norm(p["mandante"]) & norm(t2) and norm(p["visitante"]) & norm(t1)]
        if not cand and not cand2:
            nao += 1; print("NAO", a, d, t1, pl, t2); continue
        p = (cand or cand2)[0]; inv = not cand
        gm, gv = (int(m.group(1)), int(m.group(2))) if not inv else (int(m.group(2)), int(m.group(1)))
        if (str(gm), str(gv)) == (p["gols_mandante"], p["gols_visitante"]): ok += 1; print("OK ", a, d, t1, pl, t2)
        else: dif += 1; print("DIF", a, d, t1, pl, t2, "| pacote", p["mandante"], p["gols_mandante"], "x", p["gols_visitante"], p["visitante"])
print(f"bateu {ok}, difere {dif}, não achado {nao}")
