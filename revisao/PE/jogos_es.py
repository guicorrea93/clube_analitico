"""Placares do pacote per-1 x resultados das páginas de temporada da Wikipédia es (match_X_Y dos módulos
sports table/results e templates {{Partidos}}). A Wikipédia es foi a FONTE dos jogos de 1926-1929, 1943-1967, 1982 e 1985
(esses anos são pulados: não é conferência independente). Nos demais, cada resultado da Wikipédia procura um jogo do
pacote na mesma edição com o mesmo mandante e visitante.

Uso (raiz): python -I revisao/PE/jogos_es.py  -> revisao/PE/jogos_es_saida.txt
"""
import csv
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

R = Path(__file__).resolve().parents[2]
C = R / "data/cache/revisao/PE"
P = R / "data/coleta/per-1/pacote"
FONTE_WIKI = {*range(1926, 1930), *range(1943, 1968), 1982, 1985}


def sem(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    s = re.sub(r"\(.*?\)|\bclub\b|\bf\.? ?b\.? ?c\.?|\bfc\b|\bf\. ?c\.|\bclub sport\b|\bsport\b|\bdeportivo\b|\bde\b|\bdel\b|[.\-']", " ", s)
    return re.sub(r"\s+", " ", s).strip()


ALIAS = {"sucre": "Mariscal Sucre", "colegio nacional iquitos": "CNI", "universidad tecnica cajamarca": "UTC", "real garcilaso": "Cusco FC",
         "inti gas": "Ayacucho", "universidad san martin porres": "Universidad San Martín", "san martin": "Universidad San Martín",
         "asociacion tarma": "ADT", "binacional": "Binacional", "carlos a mannucci": "Carlos Mannucci", "colegio san agustin": "Deportivo San Agustín",
         "san agustin": "Deportivo San Agustín", "federacion universitaria": "Universitario", "universitario deportes": "Universitario",
         "centro municipal": "Deportivo Municipal", "municipal": "Deportivo Municipal", "boys": "Sport Boys", "boys association": "Sport Boys",
         "cristal": "Sporting Cristal", "huaral": "Unión Huaral", "union huaral": "Unión Huaral", "aurich": "Juan Aurich",
         "bolognesi": "Coronel Bolognesi", "coronel bolognesi": "Coronel Bolognesi", "cesar vallejo": "César Vallejo",
         "universidad cesar vallejo": "César Vallejo", "melgar": "Melgar", "alianza atletico sullana": "Alianza Atlético",
         "leon huanuco": "León de Huánuco", "academia cantolao": "Academia Cantolao", "cantolao": "Academia Cantolao",
         "chalaco": "Atlético Chalaco", "atletico chalaco": "Atlético Chalaco", "torino": "Atlético Torino", "grau": "Atlético Grau",
         "ugarte": "Alfonso Ugarte", "alfonso ugarte puno": "Alfonso Ugarte", "junin": "Deportivo Junín", "cni": "CNI",
         "total clean": "Total Chalaco", "coopsol": "Coopsol", "coopsol trujillo": "Coopsol", "estudiantes medicina": "Estudiantes de Medicina",
         "grau estudiantes": "Estudiantes de Medicina", "minas": "Unión Minas", "union minas": "Unión Minas", "wanka": "Deportivo Wanka",
         "pesquero": "Deportivo Pesquero", "upao": "Deportivo UPAO", "sipesa": "Deportivo Sipesa", "ovacion sipesa": "Deportivo Sipesa",
         "tumán": "Unión Tumán", "union tuman": "Unión Tumán", "espinosa": "Octavio Espinosa", "octavio espinoza": "Octavio Espinosa",
         "hungaritos": "Hungaritos Agustinos", "carlos stein": "Carlos Stein", "llacuabamba": "Deportivo Llacuabamba",
         "garcilaso": "Deportivo Garcilaso", "chankas": "Los Chankas", "los chankas": "Los Chankas", "comerciantes unidos": "Comerciantes Unidos",
         "juan pablo ii college": "Juan Pablo II", "juan pablo ii": "Juan Pablo II", "ayacucho": "Ayacucho", "huancayo": "Sport Huancayo",
         "union comercio": "Unión Comercio", "atletico minero": "Atlético Minero", "ancash": "Sport Áncash", "sport ancash": "Sport Áncash",
         "galvez": "José Gálvez", "jose galvez": "José Gálvez", "atletico universidad": "Atlético Universidad", "loretana": "La Loretana",
         "lawn tennis": "Lawn Tennis", "imi": "IMI", "cochahuayco": "América Cochahuayco", "america cochahuayco": "América Cochahuayco",
         "alcides vigo": "Alcides Vigo", "guardia republicana": "Guardia Republicana", "aurich canana": "Aurich-Cañaña",
         "ciclista lima": "Ciclista Lima", "defensor lima": "Defensor Lima", "sima": "Deportivo SIMA", "kdt nacional": "KDT Nacional",
         "porvenir miraflores": "Porvenir Miraflores", "pierola": "Piérola", "walter ormeno": "Walter Ormeño", "union pesquero": "Unión Pesquero",
         "barrio frigorifico": "Atlético Barrio Frigorífico", "huracan": "Sportivo Huracán", "sportivo huracan": "Sportivo Huracán",
         "atletico huracan": "Atlético Huracán", "diablos rojos": "Diablos Rojos", "san simon": "San Simón", "los caimanes": "Los Caimanes",
         "pacifico": "Pacífico FC", "cobresol": "Cobresol", "la bocana": "Defensor La Bocana", "defensor la bocana": "Defensor La Bocana",
         "rosario": "Sport Rosario", "sport rosario": "Sport Rosario", "pirata": "Pirata FC", "alianza universidad": "Alianza Universidad",
         "alianza universidad huanuco": "Alianza Universidad", "csdc alianza universidad": "Alianza Universidad", "loreto": "Sport Loreto",
         "olimpico": "Atlético Olímpico", "atletico olimpico": "Atlético Olímpico", "tarapaca ferrocarril": "Sportivo Tarapacá Ferrocarril",
         "progresista apurimac": "Progresista Apurímac", "telmo carbajo": "Telmo Carbajo", "santiago barranco": "Santiago Barranco",
         "atletico cordoba": "Atlético Córdoba", "union carbone": "Unión Carbone", "sportivo union": "Sportivo Unión", "melgar lima": "Sportivo Melgar",
         "sportivo melgar": "Sportivo Melgar", "circolo sportivo italiano": "Circolo Sportivo Italiano", "hidroaviacion": "Hidroaviación",
         "lawn tennis exposicion": "Lawn Tennis de la Exposición", "union buenos aires": "Unión Buenos Aires", "alianza frigorifico": "Alianza Frigorífico",
         "sporting tabaco": "Sporting Tabaco", "progreso": "Sport Progreso", "sport progreso": "Sport Progreso", "jorge chavez": "Jorge Chávez",
         "tintaya": "Deportivo Tintaya", "mina san vicente": "Mina San Vicente", "union tarapoto": "Unión Tarapoto", "aurora": "FBC Aurora",
         "juvenil los angeles": "Juvenil Los Ángeles", "los angeles": "Deportivo Los Ángeles", "yurimaguas": "Deportivo Yurimaguas",
         "15 setiembre": "15 de Setiembre", "aelu": "AELU", "libertad": "Libertad de Trujillo", "internazionale": "Internazionale de San Borja",
         "canana": "Deportivo Cañaña", "pucallpa": "Deportivo Pucallpa", "alipio ponce": "Alipio Ponce", "anda": "Defensor ANDA",
         "defensor anda": "Defensor ANDA", "alianza naval": "Alianza Naval", "juventud la joya": "Juventud La Joya", "la joya": "Juventud La Joya",
         "juventud la palma": "Juventud La Palma", "la palma": "Juventud La Palma", "huancayo fc": "Huancayo FC", "hospital": "Deportivo Hospital",
         "pilsen": "Sport Pilsen", "mariscal nieto": "Mariscal Nieto", "espartanos": "Los Espartanos", "chanchamayo": "Chanchamayo FC",
         "cooptrip": "Deportivo COOPTRIP", "union gonzales prada": "Unión Gonzales Prada", "gonzales prada": "Unión Gonzales Prada",
         "alianza chorrillos": "Alianza Chorrillos", "association chorrillos": "Asociación Chorrillos", "centro iqueno": "Centro Iqueño",
         "carlos concha": "Carlos Concha", "union callao": "Unión Callao", "mariscal castilla": "Mariscal Castilla", "union america": "Unión América",
         "defensor arica": "Defensor Arica", "alfonso ugarte chiclin": "Alfonso Ugarte de Chiclín", "atletico grau": "Atlético Grau",
         "atletico torino": "Atlético Torino", "deportivo junin": "Deportivo Junín", "cienciano": "Cienciano", "utc": "UTC", "adt": "ADT",
         "tarma": "ADT", "alianza lima": "Alianza Lima", "sporting cristal": "Sporting Cristal", "universitario": "Universitario",
         "sport boys": "Sport Boys", "alianza atletico": "Alianza Atlético", "juan aurich": "Juan Aurich", "meteor": "Meteor Sport Club",
         "bancos": "Deportivo Bancos", "aurora arequipa": "FBC Aurora", "huayllaspanca": "Unión Huayllaspanca", "alianza huanuco": "Alianza Huánuco",
         "sport pacifico": "Sport Pacífico", "deportivo pacifico": "Sport Pacífico"}


def clubes_pacote():
    m = {}
    for r in csv.DictReader(open(P / "clubes.csv", encoding="utf-8")):
        m[sem(r["clube"])] = r["clube"]
        for x in r["nomes_fonte"].split("|"):
            if x.count(":") >= 2:
                m.setdefault(sem(x.split(":")[1]), r["clube"])
    for k, v in ALIAS.items():
        m[sem(k)] = v
    return m


def resolve(nome, mapa, do_ano):
    n = sem(re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", nome))
    if n in mapa and mapa[n] in do_ano:
        return mapa[n]
    cands = [c for c in do_ano if sem(c) == n or n in sem(c) or sem(c) in n]
    if len(cands) == 1:
        return cands[0]
    toks = set(n.split())
    melhor = sorted(do_ano, key=lambda c: -len(toks & set(sem(c).split())))
    if melhor and len(toks & set(sem(melhor[0]).split())) >= 1 and (len(melhor) < 2 or len(toks & set(sem(melhor[1]).split())) < len(toks & set(sem(melhor[0]).split()))):
        return melhor[0]
    return mapa.get(n)


def placar(s):
    s = re.sub(r"<[^>]*>|\[\[[^\]]*\|([^\]]*)\]\]|\[[^\]]*\]|\{\{[^}]*\}\}", r"\1", s or "")
    m = re.search(r"(\d+)\s*[–—\-:]\s*(\d+)", s)
    return (int(m.group(1)), int(m.group(2))) if m else None


def jogos_es(t):
    """Resultados por bloco ({{#invoke:sports ...}}): os nomes valem dentro do bloco; sem nome no bloco, vale o do bloco anterior."""
    out = []
    COD = r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9]+"
    nomes_ant = {}
    for bl in re.split(r"\{\{\s*#invoke:\s*sports", t)[1:]:
        bl = bl.split("\n}}")[0]
        nomes = dict(nomes_ant)
        for code, nome in re.findall(r"name_(" + COD + r")\s*=\s*((?:\[\[[^\]]*\]\]|[^\n|])*)", bl):
            nomes[code] = nome
        for a, b, res in re.findall(r"match_(" + COD + r")_(" + COD + r")\s*=\s*([^\n|]*)", bl):
            p = placar(res)
            if p and a in nomes and b in nomes:
                out.append((nomes[a], nomes[b], p, "match"))
        nomes_ant = nomes
    for bl in re.findall(r"\{\{\s*Partidos(.*?)\n\}\}", t, flags=re.S):
        d = dict(re.findall(r"\|\s*(\w+)\s*=\s*([^\n]*)", bl))
        p = placar(d.get("resultado", ""))
        if p and d.get("local") and d.get("visita"):
            out.append((d["local"], d["visita"], p, "Partidos " + d.get("fecha", "").strip()))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mapa = clubes_pacote()
    por = defaultdict(lambda: defaultdict(list))
    clubes_ano = defaultdict(set)
    for r in csv.DictReader(open(P / "partidas.csv", encoding="utf-8")):
        if r["gols_mandante"] == "":
            continue
        y = int(r["temporada"])
        por[y][(r["mandante"], r["visitante"])].append(r)
        clubes_ano[y] |= {r["mandante"], r["visitante"]}
    saida = []
    resumo = []
    for f in sorted(C.glob("es_temporada_*.json")):
        y = int(f.stem.split("_")[-1])
        if y in FONTE_WIKI or y < 1926 or not clubes_ano.get(y):
            continue
        t = json.loads(f.read_text(encoding="utf-8"))["parse"]["wikitext"]
        n = ok = sem_par = 0
        for ln, vn, p, origem in jogos_es(t):
            a, b = resolve(ln, mapa, clubes_ano[y]), resolve(vn, mapa, clubes_ano[y])
            if not a or not b or a == b:
                continue
            n += 1
            js = por[y].get((a, b), [])
            if not js:
                sem_par += 1
                saida.append(f"{y} SEM JOGO NO PACOTE: {a} x {b} {p[0]}-{p[1]} ({origem})")
                continue
            if any((int(j["gols_mandante"]), int(j["gols_visitante"])) == p for j in js):
                ok += 1
            else:
                saida.append(f"{y} PLACAR: es {a} {p[0]}-{p[1]} {b} ({origem}) | pacote " +
                             "; ".join(f"{j['fase']} {j['data']} {j['gols_mandante']}-{j['gols_visitante']}{' '+j['resultado_especial'] if j['resultado_especial'] else ''}" for j in js))
        resumo.append((y, n, ok, sem_par))
    txt = ["ano | resultados na es casados | iguais | sem jogo no pacote"] + [f"{y} | {n} | {ok} | {s}" for y, n, ok, s in resumo]
    tot = [sum(x[i] for x in resumo) for i in (1, 2, 3)]
    txt.append(f"TOTAL | {tot[0]} | {tot[1]} | {tot[2]}")
    (Path(__file__).parent / "jogos_es_saida.txt").write_text("\n".join(txt + [""] + saida), encoding="utf-8")
    print("\n".join(txt))
    print(len(saida), "linhas de diferença")


if __name__ == "__main__":
    main()
