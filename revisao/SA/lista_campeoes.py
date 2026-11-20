"""Lê 'List of Brazilian football champions' (Wikipédia en): ano, campeão, vice, 3º, artilheiro(s), gols."""
import sys, re
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from baixar import wikitext
def limpa(c):
    c = re.sub(r"<ref[^>]*/>", "", c); c = re.sub(r"<ref.*?</ref>", "", c, flags=re.S)
    c = re.sub(r"\{\{efn[^}]*\}\}", "", c)
    c = re.sub(r"\{\{[Ff]lagicon\|[^}]*\}\}", "", c); c = re.sub(r"\{\{small\|[^}]*\}\}", "", c)
    c = re.sub(r"\{\{center\|([^}]*)\}\}", r"\1", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\{\{[^}]*\}\}", "", c); c = re.sub(r"<br\s*/?>", " / ", c); c = re.sub(r"<[^>]+>", "", c)
    c = re.sub(r"^\s*align=\w+\s*\|", "", c)
    return c.replace("'''", "").replace("''", "").strip()
def linhas():
    t = wikitext("en", "List of Brazilian football champions")
    i = t.find("==List of champions=="); f = t.find("==Performances==")
    out = []
    for bloco in t[i:f].split("\n|-"):
        bloco = bloco.strip()
        if not bloco.startswith("|"): continue
        cel = [limpa(x) for x in bloco[1:].split("||")]
        if len(cel) < 8: continue
        out.append({"ano": cel[1], "campeao": cel[2], "vice": cel[3], "terceiro": cel[4], "art": cel[6], "gols": cel[7]})
    return out
if __name__ == "__main__":
    import json
    for r in linhas(): print(json.dumps(r, ensure_ascii=False))
