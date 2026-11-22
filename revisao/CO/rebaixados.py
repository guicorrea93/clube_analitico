"""Bloco B: rebaixados de cada temporada (Wikipédia es, "Anexo:Ascensos y descensos de la Categoría Primera A") x
classificacao_final.csv do pacote (situacao = rebaixado). O rebaixamento é da temporada: vai na última edição do ano.
Uso (da raiz): python -I revisao/CO/rebaixados.py"""
import csv, re
from collections import defaultdict

T = open("data/cache/revisao/CO/es_ascensos_descensos.txt", encoding="utf-8").read()
T = T[T.index("== Ascensos y descensos =="):T.index("== Series de promoción ==")]
NOMES = {"Envigado Fútbol Club": "Envigado", "Club Deportivo La Equidad": "Internacional de Bogotá", "Patriotas Boyacá": "Patriotas Boyacá",
         "Deportivo Unicosta": "Unicosta", "Universidad Autónoma del Caribe Fútbol Club": "Uniautónoma", "Itagüí Leones": "Leones FC",
         "Tigres Fútbol Club": "Tigres FC", "Fortaleza Fútbol Club": "Fortaleza CEIF", "Fortaleza CEIF": "Fortaleza CEIF",
         "Centauros Villavicencio": "Centauros Villavicencio", "Jaguares de Córdoba": "Jaguares de Córdoba"}
P = "data/coleta/col-1/pacote/"
eds = [r["temporada"] for r in csv.DictReader(open(P + "edicoes.csv", encoding="utf-8"))]
ultima = {}
for t in eds:
    ultima[t[:4] if not "/" in t else t] = t   # última edição de cada ano
ultima["1995-96"], ultima["1996-97"] = "1995/96", "1996/97"
ultima["2021-I"], ultima["2021-II"] = "2021 Apertura", "2021 Finalización"
reb = defaultdict(set)
for r in csv.DictReader(open(P + "classificacao_final.csv", encoding="utf-8")):
    if r["situacao"] == "rebaixado":
        reb[r["temporada"]].add(r["clube"])
falta = []
for linha in T.split("\n|-"):
    m = re.search(r"\|'''\[\[[^|\]]*\|([^\]]+)\]\]'''\s*\|\|(.*?)\|\|", linha)
    if not m:
        continue
    ano = m.group(1)
    if not re.match(r"\d{4}", ano) or int(ano[:4]) > 2025:
        continue
    desc = [NOMES.get(x.split("|")[0], x.split("|")[-1]) for x in re.findall(r"\[\[([^\]]+)\]\]", m.group(2))]
    ed = ultima.get(ano)
    for c in desc:
        if not ed:
            falta.append(f"{ano}: {c} — o ano não tem edição no pacote (Torneo Adecuación 1997 fica fora): decidir onde marcar")
        elif c not in reb.get(ed, set()):
            falta.append(f"{ed}: {c} rebaixado (Wikipédia es) — no pacote sem 'rebaixado'")
print("\n".join(falta))
print(f"\nrebaixamentos na Wikipédia (1992-2025): {len(falta) + sum(len(v) for v in reb.values())}; marcados no pacote: "
      f"{sum(len(v) for v in reb.values())}; faltam: {len(falta)}")
