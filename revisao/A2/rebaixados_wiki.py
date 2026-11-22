"""Rebaixados e promovidos de cada edição pelo infobox da Wikipédia pt x situacao do pacote."""
import sys, os, re, csv
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from baixar import wikitext
from baixar_wiki_edicoes import nome
pac = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/classificacao_final.csv", encoding="utf-8")):
    pac[r["temporada"]][r["situacao"]].append(r["clube"])
def campo(w, nomes):
    for n in nomes:
        m = re.search(r"\|\s*" + n + r"\s*=(.*?)(?=\n\s*\|\s*[a-zçãé_ ]+\s*=|\n\}\})", w, re.S | re.I)
        if m and m.group(1).strip():
            v = m.group(1)
            v = re.sub(r"<ref.*?(/>|</ref>)", "", v, flags=re.S)
            v = re.sub(r"\{\{\s*[Ff]utebol\s+([^}|]+)[^}]*\}\}", r"\1", v)
            v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v)
            v = re.sub(r"<br\s*/?>|\n", "; ", v); v = re.sub(r"\{\{[^}]*\}\}|'''?|<[^>]+>", "", v)
            return re.sub(r"\s+", " ", v).strip(" ;")
    return ""
for a in list(range(1947, 1967)) + list(range(1967, 2027)):
    w = wikitext(f"Campeonato Paulista de Futebol de {a} - {nome(a)}")
    if not w: continue
    reb = campo(w, ["rebaixados?", "rebaixado\(s\)", "despromovidos?"])
    pro = campo(w, ["promovidos?", "acesso", "promovido\(s\)"])
    t = str(a)
    if t in pac or reb or pro:
        print(a, "| WIKI rebaixados:", reb or "-", "| promovidos:", pro or "-")
        if t in pac:
            print("     PACOTE rebaixado:", pac[t]["rebaixado"], "| acesso:", pac[t]["acesso"], "| campeao/vice:", pac[t]["campeao"] + pac[t]["vice"])
