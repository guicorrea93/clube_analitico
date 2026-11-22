"""Cobertura das fichas de jogo (autores, público, árbitro, cartões) por década: Transfermarkt e ogol, por amostra.
Uso: python -I revisao/QA/amostra_fichas.py   (grava revisao/QA/saida/fichas.csv)"""
import csv, json, random, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tm, ogol, cmp_tm

random.seed(22)
SAIDA = pathlib.Path(__file__).parent / "saida"
linhas = []
# Transfermarkt: 3 jogos por temporada
for slug, ano in [("bra-serie-a", 1985), ("bra-serie-a", 1991), ("bra-serie-a", 1997), ("bra-serie-a", 2001), ("bra-serie-a", 2005),
                  ("bra-serie-a", 2015), ("bra-serie-a", 2022), ("bra-serie-b", 2009), ("bra-serie-b", 2015), ("bra-serie-b", 2022)]:
    s, js = cmp_tm.temporada_tm(slug, ano)
    for j in random.sample(js, 3):
        f = tm.ficha(j["id"])
        ng = (j["gm"] or 0) + (j["gv"] or 0)
        linhas.append({"fonte": "transfermarkt", "competicao": slug, "ano": ano, "jogo": f"{j['data']} {j['mandante']} {j['gm']}x{j['gv']} {j['visitante']}",
                       "gols_placar": ng, "gols_com_autor": len(f["gols"]), "publico": f["publico"] or "", "arbitro": f["arbitro"] or "",
                       "estadio": f["estadio"] or "", "cartoes": f["cartoes"], "url": f"{tm.BASE}/spielbericht/index/spielbericht/{j['id']}"})
# ogol: 3 jogos por ano (urls do json da coleta)
for arq, slug, ano in [("data/serie_a/ogol/serie_a_1977.json", "bra-serie-a", 1977), ("data/serie_a/ogol/serie_a_1980.json", "bra-serie-a", 1980),
                       ("data/serie_a/ogol/serie_a_1993.json", "bra-serie-a", 1993), ("data/serie_b/ogol/serie_b_1981.json", "bra-serie-b", 1981),
                       ("data/serie_b/ogol/serie_b_1992.json", "bra-serie-b", 1992), ("data/serie_b/ogol/serie_b_2002.json", "bra-serie-b", 2002)]:
    js = [j for j in json.load(open(arq, encoding="utf-8")) if j.get("gols_mandante") is not None]
    for j in random.sample(js, 3):
        r, tx = ogol.ficha(j["url"])
        i = tx.find("Escalações")
        bloco = tx[i:tx.find("Informação do jogo")] if i >= 0 else ""
        ng = j["gols_mandante"] + j["gols_visitante"]
        import re
        minutos = len(re.findall(r"\n\d{1,3}'\s*\n", bloco))
        tem_arb = "Árbitro\n" in tx[tx.find("Informação do jogo"):] if "Informação do jogo" in tx else False
        arb = re.search(r"Árbitro\n\s*([^\n]+)", tx[tx.find("Informação do jogo"):]) if tem_arb else None
        est = re.search(r"Estádio\n\s*([^\n]+)", tx[tx.find("Informação do jogo"):]) if "Informação do jogo" in tx else None
        linhas.append({"fonte": "ogol", "competicao": slug, "ano": ano, "jogo": f"{j['data']} {j['mandante']} {j['gols_mandante']}x{j['gols_visitante']} {j['visitante']}",
                       "gols_placar": ng, "gols_com_autor": f"{minutos} (minutos nas escalações)" if bloco else 0, "publico": r["publico"] or "",
                       "arbitro": arb.group(1).strip() if arb else "", "estadio": est.group(1).strip() if est else "",
                       "cartoes": "escalação" if bloco else "", "url": j["url"]})
with open(SAIDA / "fichas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0]))
    w.writeheader()
    w.writerows(linhas)
for l in linhas:
    print(l["fonte"], l["ano"], l["jogo"][:55], "| gols", l["gols_placar"], "autor", l["gols_com_autor"], "| púb", l["publico"], "| árb", l["arbitro"][:25], "| est", l["estadio"][:25], "| cart", l["cartoes"])
