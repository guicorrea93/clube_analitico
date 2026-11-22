"""Wikipédia es (Serie A de Ecuador, seção Historial): campeão, vice, 3º e 4º por temporada -> TSV."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, sys
sys.path.insert(0, "revisao/EC")
import baixar
t = baixar.wikitext("es", "Serie A de Ecuador")
a = t.index("== Historial =="); b = t.index("== Palmarés ==")
sec = t[a:b]
linhas = []
for bloco in sec.split("\n|-")[1:]:
    m = re.search(r"\|\s*align=\"center\"\s*\|\s*'''\[\[[^|\]]*\|([^\]]+)\]\]'''", bloco)
    if not m: continue
    temp = m.group(1).strip()
    celulas = re.findall(r"^\|(?!-)(.*)$", bloco, re.M)[1:]
    nomes = []
    for c in celulas:
        ls = re.findall(r"\[\[(?!Archivo|File|Imagen)([^\]|]+)(?:\|([^\]]+))?\]\]", c)
        if ls:
            nomes.append((ls[0][1] or ls[0][0]).strip())
        elif "No se disput" in c:
            nomes.append("NAO DISPUTADO")
    linhas.append([temp] + nomes[:4])
for l in linhas: print("\t".join(l))
