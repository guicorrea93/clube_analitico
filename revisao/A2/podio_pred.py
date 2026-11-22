"""Lê a predefinição 'Campeões do Campeonato Paulista de Futebol - Série A2' (Wikipédia pt): ano, campeão, placar, vice, 3º, 4º, nº.
Grava revisao/A2/podio_pred.json."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
w = wikitext("Predefinição:Campeões do Campeonato Paulista de Futebol - Série A2")
w = re.sub(r"\{\{#tag:ref.*?\}\}", "", w, flags=re.S)
def limpa(c):
    c = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", c, flags=re.S)
    c = re.sub(r"\[\[(?:Imagem|Ficheiro|File):[^\]]*\]\]", "", c)
    c = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"<br\s*/?>", " / ", c)
    c = re.sub(r"'''?|<[^>]+>|\{\{[^}]*\}\}", "", c)
    c = re.sub(r"^\s*(align|rowspan|colspan|style)=[^|]*\|", "", c.strip())
    return re.sub(r"\s+", " ", c).strip(" /")
res = {}
for bloco in re.split(r"\n\|-[^\n]*", w):
    cels = [limpa(x) for x in re.split(r"\n\|", "\n" + bloco.strip()) if x.strip() and not x.strip().startswith("!")]
    cels = [c for c in cels if c != ""]
    if cels and re.match(r"\d{4}", cels[0]):
        ano = cels[0][:4]
        res[ano] = cels[1:]
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "podio_pred.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for a, r in res.items(): print(a, r)
