"""Bloco A: campeão e vice de cada edição do painel x lista da AUF na Wikipédia es
("Primera División de Uruguay", seção Títulos de liga por año).
Uso: python -I revisao/UY/campeoes_es.py"""
import json, re, sqlite3

TXT = open("data/cache/revisao/UY/es_primera.txt", encoding="utf-8").read()
ini = TXT.index("=== Títulos de liga por año ===")
fim = TXT.index("=== Títulos de Liga por equipo ===")
tab = re.sub(r"\[\[Archivo:[^\]]*\]\]", "", TXT[ini:fim])

ALIAS = {
    "CURCC": "Peñarol", "Central Uruguay Railway Cricket Club": "Peñarol", "Peñarol": "Peñarol",
    "Club Atlético Peñarol": "Peñarol", "Nacional": "Nacional", "Club Nacional de Football": "Nacional",
    "Albion": "Albion de Montevideo", "Albion Football Club": "Albion de Montevideo",
    "Montevideo Wanderers": "Montevideo Wanderers", "Montevideo Wanderers Fútbol Club": "Montevideo Wanderers",
    "River Plate FC": "River Plate FC", "River Plate Football Club": "River Plate FC",
    "Universal": "Universal de Montevideo", "Universal Football Club": "Universal de Montevideo",
    "Rampla Juniors": "Rampla Juniors", "Bella Vista": "Bella Vista", "Cerro": "Cerro",
    "Defensor": "Defensor Sporting", "Defensor Sporting": "Defensor Sporting", "Danubio": "Danubio",
    "Central Español": "Central Español", "Progreso": "Progreso", "River Plate": "River Plate de Montevideo",
    "Liverpool": "Liverpool de Montevideo", "Rentistas": "Rentistas", "Racing": "Racing de Montevideo",
    "Rocha": "Rocha FC", "Plaza Colonia": "Plaza Colonia", "Cerrito": "Cerrito", "Wanderers": "Montevideo Wanderers",
    "Fénix": "Fénix", "Huracán Buceo": "Huracán Buceo", "Boston River": "Boston River", "Sud América": "Sud América",
}


def limpa(cel):
    m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cel)
    if not m:
        t = re.sub(r"'''|''|<[^>]+>|\{\{[^}]*\}\}", "", cel).strip()
        return t
    return (m.group(2) or m.group(1)).strip()


linhas = re.split(r"\n\|-[^\n]*", tab)
es = {}
for ln in linhas:
    cels = [c for c in re.split(r"\n\||\|\|", "\n" + ln.strip()) if c.strip()]
    if not cels:
        continue
    m = re.search(r"(\d{4}(?:-\d{2})?)", cels[0])
    if not m or "colspan=\"9\"" in ln:
        continue
    ano = cels[0]
    ano_txt = re.sub(r".*\|", "", re.sub(r"\]\].*", "", ano)) if "[[" in ano else ano
    ano_txt = re.sub(r"[^0-9\-/A-Za-zé ]", "", ano_txt).strip()
    if "No se disput" in ln or "Suspendido" in ln or "suspend" in ln.lower():
        es[ano_txt] = ("—", "—", ln[:200].replace("\n", " "))
        continue
    # campeão = 1ª célula com ''' e link; vice = a célula seguinte
    idx = None
    for i, c in enumerate(cels):
        if "'''" in c and "[[" in c and not re.search(r"Campeonato Uruguayo", c.split("'''")[1] if "'''" in c else ""):
            idx = i
            break
    if idx is None:
        es[ano_txt] = ("?", "?", ln[:200].replace("\n", " "))
        continue
    camp = limpa(cels[idx].split("'''")[1] if "'''" in cels[idx] else cels[idx])
    vice = limpa(cels[idx + 1]) if idx + 1 < len(cels) else "?"
    es[ano_txt] = (ALIAS.get(camp, camp), ALIAS.get(vice, vice), "")

c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
eds = c.execute("""select temporada, ano_inicio, campeao_id, vice_id from edicao e join competicao co using(competicao_id)
                   where co.slug='uru-1' order by ano_inicio, temporada""").fetchall()
s = open("painel/dados/uru-1.js", encoding="utf-8").read()
D = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))
ED = D["ED"]
print("chaves es:", len(es))
saida = []
for (temp, ano, cid, vid), p in zip(eds, ED):
    k = temp.split()[0].replace("/", "-")
    alvo = es.get(k) or es.get(temp)
    db_c, db_v = nome.get(cid), nome.get(vid)
    pc, pv = p["campeao"], p["vice"]
    if (pc, pv) != (db_c, db_v):
        print("PAINEL x BANCO", temp, pc, pv, db_c, db_v)
    if not alvo:
        saida.append((temp, db_c, db_v, "(sem linha na es)", "", "falta"))
        continue
    ok_c = alvo[0] == db_c
    ok_v = alvo[1] == db_v
    saida.append((temp, db_c, db_v, alvo[0], alvo[1], ("ok" if ok_c else "CAMPEAO") + "/" + ("ok" if ok_v else "VICE")))
for r in saida:
    print("\t".join(str(x) for x in r))
print("anos na es sem edição no banco:", sorted(set(es) - {t.split()[0] for t, *_ in eds}))
