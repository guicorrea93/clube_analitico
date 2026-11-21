"""Artilheiros (Troféu Pichichi) do banco x lista da es.wikipedia (Trofeo Pichichi, contagem do Marca).
Uso: python -I revisao/ES/compara_pichichi.py"""
import json, re, sqlite3, sys, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar_eswiki import url_pagina
from baixar import baixar
sys.stdout.reconfigure(encoding="utf-8")

w = json.load(open(baixar(url_pagina("Trofeo Pichichi")), encoding="utf-8"))["parse"]["wikitext"]["*"]
w = w[w.find("== Trofeo Pichichi de 1ª División"):]
w = w[:w.find("\n|}")]


def sem(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn").lower()


def txt(s):
    s = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    return re.sub(r"\{\{[^{}]*\}\}|'''?|<[^>]+>|\(\d+\)", "", s).strip()


wiki = {}
t = None
for bloco in re.split(r"\n\|-", w)[1:]:
    cel = [x[1:] for x in bloco.split("\n")[1:] if x.startswith("|")]
    if not cel:
        continue
    m = re.search(r"(\d{4})[–/-](\d{2})\]\]", cel[0])
    if m:
        t = f"{m.group(1)}/{m.group(2)}"
        cel = cel[1:]
    if t is None or not cel:
        continue
    jog = txt(re.sub(r"^align=[^|]*\|", "", cel[0]))
    gcel = next((x for x in cel if "AntiqueWhite" in x), None)
    gols = re.search(r"AntiqueWhite\|\s*(\d+)", gcel) if gcel else None
    nota = " ".join(re.findall(r"<ref name=\"[^\"]*\">(.*?)</ref>", bloco, re.S))
    wiki.setdefault(t, []).append((jog, int(gols.group(1)) if gols else None, txt(nota)[:240]))

c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
ok = dif = 0
for (t,) in c.execute("select temporada from edicao join competicao using(competicao_id) where slug='esp-1' order by ano_inicio").fetchall():
    db = c.execute("""select a.jogador, cl.nome, a.gols from artilheiro a join edicao e using(edicao_id) join competicao k using(competicao_id)
                      left join clube cl using(clube_id) where k.slug='esp-1' and e.temporada=?""", (t,)).fetchall()
    wl = wiki.get(t, [])
    casa = lambda p: any(sem(p.split()[-1]) in sem(x) or sem(x.split()[-1]) in sem(p) for x, _, _ in wl)
    nomes_ok = len(db) == len(wl) and all(casa(p) for p, _, _ in db)
    gols_ok = sorted(g for _, _, g in db) == sorted(g for _, g, _ in wl)
    if nomes_ok and gols_ok:
        ok += 1
        continue
    dif += 1
    print(t, "| banco:", "; ".join(f"{p} ({cl}) {g}" for p, cl, g in db), "| wiki:", "; ".join(f"{j} {g}" for j, g, _ in wl),
          "| nota:", " / ".join(n for _, _, n in wl if n))
print("temporadas iguais", ok, "diferentes", dif)
