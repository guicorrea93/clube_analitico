"""Wikipédia es (Serie A de Ecuador, 'Ascensos y descensos'): rebaixados por ano x rebaixados marcados no pacote."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, csv, collections
sys.path.insert(0, "revisao/EC")
import baixar
t = baixar.wikitext("es", "Serie A de Ecuador")
a = t.index("== Ascensos y descensos a la Serie A =="); b = t.index("=== Cantidad de ascensos")
AL = {"Barcelona": "Barcelona de Guayaquil", "Liga de Quito": "LDU de Quito", "Universidad Católica": "Universidad Católica de Quito",
      "Liga de Portoviejo": "LDU de Portoviejo", "Liga de Loja": "LDU de Loja", "Liga de Cuenca": "LDU de Cuenca",
      "U. D. Valdez": "UD Valdez", "Valdez": "Valdez SC", "River Plate (Riobamba)": "River Plate de Riobamba", "Juventus": "Juventus de Esmeraldas",
      "Santa Rita": "Santa Rita de Vinces", "América de Quito": "América de Quito", "Independiente José Terán": "Independiente del Valle",
      "River Ecuador": "Guayaquil City", "Libertad": "Libertad de Loja", "Azogues": "Deportivo Azogues", "Deportivo Azogues": "Deportivo Azogues",
      "Brasil": "Brasil de Ambato", "Manta": "Manta FC", "Vinotinto Ecuador": "Vinotinto", "Juvenil": "Juvenil", "Santos": "Santos de El Guabo"}
wiki = {}
for row in t[a:b].split("\n|-")[1:]:
    m = re.search(r"<center>(\d{4})", row)
    if not m: continue
    cels = row.split("||")
    if len(cels) < 3: continue
    des = re.findall(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", re.sub(r"<ref.*?(</ref>|/>)", "", cels[2]))
    wiki[m.group(1)] = [AL.get(x.strip(), x.strip()) for x in des]
pac = collections.defaultdict(list)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/classificacao_final.csv", encoding="utf-8")):
    if r["situacao"] == "rebaixado": pac[r["temporada"][:4]].append(r["clube"])
clubes_ano = collections.defaultdict(set)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/classificacao_final.csv", encoding="utf-8")):
    clubes_ano[r["temporada"][:4]].add(r["clube"])
for ano in sorted(set(wiki) | set(pac)):
    w = set(wiki.get(ano, [])); p = set(pac.get(ano, []))
    fora = sorted(x for x in w if x not in clubes_ano[ano])
    marca = "OK" if w == p else "DIF"
    print(ano, marca, "| wiki es:", sorted(w), "| pacote:", sorted(p), ("| nomes da wiki fora da classificação: " + str(fora)) if fora else "")
