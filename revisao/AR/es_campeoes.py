"""Lê as tabelas de campeões do artigo 'Primera División de Argentina' (Wikipédia es, listados 'según la página web de la AFA')
e grava revisao/AR/es_campeoes.tsv: ano, rótulo da temporada, torneo, campeão, vice, 3º (com pontos)."""
import re, sys, pathlib
sys.path.insert(0, "revisao/AR"); import baixar
t = baixar.wikitext("es", "Primera División de Argentina")
ini = t.index("=== Historial ==="); fim = t.index("==== Resumen estadístico ====", t.index("Apertura y Clausura y Campeón de Liga"))
t = t[ini:fim]
def limpa(x):
    x = re.sub(r"<ref[^>]*/>", "", x); x = re.sub(r"<ref[^>]*>.*?</ref>", "", x, flags=re.S)
    x = re.sub(r"\{\{refn.*?\}\}\}\}", "", x, flags=re.S); x = re.sub(r"\{\{refn[^{}]*\}\}", "", x)
    x = re.sub(r"\{\{small\|\(([^)]*)\)\}\}", r"(\1)", x)
    x = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", x); x = re.sub(r"\[\[([^\]]*)\]\]", r"\1", x)
    x = re.sub(r"^(?:\s*(?:bgcolor|rowspan|colspan|style|align)=[^|]*\|)+", "", x.strip())
    x = re.sub(r"\{\{[^{}]*\}\}", "", x)
    return re.sub(r"\s+", " ", x).strip()
out = []
for tab in re.findall(r"\{\|.*?\n\|\}", t, flags=re.S):
    if "Campeón" not in tab: continue
    rows = re.split(r"\n\|-[^\n]*", tab)[1:]
    ano = None; restante = 0
    for r in rows:
        cells = []
        for ln in r.strip("\n").split("\n"):
            if ln.startswith("|") and not ln.startswith("|}"):
                cells += ln[1:].split("||")
            elif cells and not ln.startswith(("!", "{")):
                cells[-1] += " " + ln
        raw = cells
        cells = [limpa(c) for c in cells]
        if not cells: continue
        span = re.match(r"\s*rowspan=(\d+)", raw[0])
        if restante > 0 and not re.match(r"\s*(rowspan=\d+\|)?\s*\[?\[?[^|]*\b(1[89]\d\d|20\d\d)", raw[0]):
            restante -= 1
        else:
            ano = cells[0]; cells = cells[1:]
            restante = int(span.group(1)) - 1 if span else 0
        while len(cells) < 5: cells.append("")
        out.append([ano] + cells[:5])
pathlib.Path("revisao/AR/es_campeoes.tsv").write_text("\n".join("\t".join(r) for r in out) + "\n", encoding="utf-8")
print(len(out))
