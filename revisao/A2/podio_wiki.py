"""Lê a tabela de campeões da Wikipédia pt (Campeonato Paulista de Futebol - Série A2): ano, nome, campeão, vice, 3º, 4º.
Grava revisao/A2/podio_wiki.json."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
w = wikitext("Campeonato Paulista de Futebol - Série A2")
ini = w.find("=== Campeonato Paulista - Série A2"); fim = w.find("==== Títulos na era profissional")
bloco = w[ini:fim]
def limpa(c):
    c = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", c, flags=re.S)
    c = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"'''?|<[^>]+>|\{\{[^}]*\}\}", "", c)
    c = re.sub(r"^\s*(rowspan|colspan|style|align)[^|]*\|", "", c.strip())
    return c.strip()
linhas = bloco.split("\n|-")
res = []; ano = None
for l in linhas:
    cels = [x for x in re.split(r"\n\|", "\n" + l.strip()) if x.strip()]
    cels = [limpa(x) for x in cels]
    if not cels: continue
    if re.fullmatch(r"\d{4}.*", cels[0]):
        ano = cels[0][:4]; cels = cels[1:]
        # org
        cels = cels[1:]
    res.append([ano] + cels)
json.dump(res, open(os.path.join(os.path.dirname(__file__), "podio_wiki.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for r in res:
    if r[0] and r[0] >= "1945": print(r)
