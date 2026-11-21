"""Classificação final de todas as temporadas: painel (painel/dados/esp-1.js) e banco x tabela da es.wikipedia.
Saída: uma linha por diferença. Uso: python -I revisao/ES/compara_classificacao.py"""
import json, re, sqlite3, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eswiki import *
sys.stdout.reconfigure(encoding="utf-8")

MAPA = {
 "Agrupación Deportiva Almería": "AD Almería", "Albacete Balompié": "Albacete", "Arenas Club": "Arenas de Getxo",
 "Arenas Club de Getxo": "Arenas de Getxo", "Athletic Club": "Athletic Bilbao", "Atletico de Madrid": "Atlético de Madrid",
 "Atlético de Madrid": "Atlético de Madrid", "Burgos Club de Fútbol (1936)": "Burgos", "Centre d'Esports Sabadell Futbol Club": "Sabadell",
 "Club Atlético Osasuna": "Osasuna", "Club Atlético de Madrid": "Atlético de Madrid", "Club Atlético de Tetuán": "Atlético Tetuán",
 "Club Deportivo Alcoyano": "Alcoyano", "Club Deportivo Castellón": "Castellón", "Club Deportivo Condal": "Condal",
 "Club Deportivo Leganes": "Leganés", "Club Deportivo Leganés": "Leganés", "Club Deportivo Logroñés": "Logroñés",
 "Club Deportivo Málaga": "CD Málaga", "Club Deportivo Numancia": "Numancia", "Club Deportivo Numancia de Soria": "Numancia",
 "Club Deportivo Tenerife": "Tenerife", "Club Esportiu Europa": "Europa", "Club Gimnàstic de Tarragona": "Gimnàstic",
 "Club Polideportivo Mérida": "Mérida", "Club de Fútbol Extremadura": "Extremadura", "Cultural y Deportiva Leonesa": "Cultural Leonesa",
 "Cádiz Club de Fútbol": "Cádiz", "Córdoba Club de Fútbol": "Córdoba", "Deportivo Alaves": "Alavés", "Deportivo Alavés": "Alavés",
 "Elche Club de Fútbol": "Elche", "F.C. Barcelona": "Barcelona", "Futbol Club Barcelona": "Barcelona", "Fútbol Club Barcelona": "Barcelona",
 "Getafe Club de Fútbol": "Getafe", "Girona Futbol Club": "Girona", "Girona Fútbol Club": "Girona", "Granada Club de Fútbol": "Granada",
 "Hércules Club de Fútbol": "Hércules", "Hércules de Alicante Club de Fútbol": "Hércules", "Levante Union Deportiva": "Levante",
 "Levante Unión Deportiva": "Levante", "Málaga Club de Fútbol": "Málaga", "Pontevedra Club de Fútbol": "Pontevedra",
 "Rayo Vallecano de Madrid": "Rayo Vallecano", "Real Betis Balompié": "Betis", "Real Burgos Club de Fútbol": "Real Burgos",
 "Real Club Celta de Vigo": "Celta", "Real Club Deportivo Espanyol": "Espanyol", "Real Club Deportivo Español": "Espanyol",
 "Real Club Deportivo Mallorca": "Mallorca", "Real Club Deportivo de La Coruña": "Deportivo La Coruña", "Real Club Deportivo de la Coruña": "Deportivo La Coruña",
 "Real Club Recreativo de Huelva": "Recreativo Huelva", "Real Jaén Club de Fútbol": "Jaén", "Real Madrid Club de Futbol": "Real Madrid",
 "Real Madrid Club de Fútbol": "Real Madrid", "Real Madrid": "Real Madrid", "Real Murcia Club de Fútbol": "Murcia", "Real Oviedo": "Real Oviedo",
 "Real Racing Club de Santander": "Racing Santander", "Real Sociedad de Futbol": "Real Sociedad", "Real Sociedad de Fútbol": "Real Sociedad",
 "Real Sporting de Gijón": "Sporting de Gijón", "Real Unión Club": "Real Unión", "Real Valladolid": "Valladolid",
 "Real Valladolid Club de Fútbol": "Valladolid", "Real Zaragoza": "Zaragoza", "Sevilla Fútbol Club": "Sevilla",
 "Sociedad Deportiva Compostela (1962-2006)": "Compostela", "Sociedad Deportiva Eibar": "Eibar", "Sociedad Deportiva Huesca": "Huesca",
 "Unió Esportiva Lleida": "Lleida", "Unión Deportiva Almería": "Almería", "Unión Deportiva Las Palmas": "Las Palmas",
 "Unión Deportiva Salamanca": "Salamanca", "Valencia Club de Fútbol": "Valencia", "Villarreal Club de Futbol": "Villarreal",
 "Villarreal Club de Fútbol": "Villarreal", "Xerez Club Deportivo": "Xerez", "Real Betis": "Betis", "Racing de Santander": "Racing Santander",
 "Real Murcia": "Murcia", "Centre d'Esports Sabadell": "Sabadell",
}

def clube(alvo):
    return MAPA.get(alvo, "?" + alvo)

def tabela_wiki(t):
    """[(pos, clube, J, V, E, D, GP, GC, ajuste)] da tabela principal; None se não achar."""
    ti, w = wikitext(t)
    tb = tabelas(w)
    if tb:
        p = tb[0][1]
        cods = [k[7:] for k in p if k.startswith("nombre_")]
        if "orden_equipo" in p:
            ordem = [x.strip() for x in p["orden_equipo"].split(",") if x.strip()]
        elif "equipo1" in p:
            ordem = [p[f"equipo{i}"].strip() for i in range(1, 40) if f"equipo{i}" in p]
        else:
            ordem = cods
        out = []
        for i, c in enumerate(ordem, 1):
            g = lambda k: int((re.search(r"-?\d+", p.get(f"{k}_{c}", "0") or "0") or re.search("0", "0")).group())
            v, e, d = g("ganados"), g("empates"), g("perdidos")
            out.append((i, clube(link_alvo(p.get("nombre_" + c, c))[0]), v + e + d, v, e, d, g("gf"), g("gc"),
                        int(p.get("ajustar_puntos_" + c, "0") or 0)))
        return out
    # tabela escrita à mão (wikitable)
    j = w.find("Clasificación")
    out = []
    for m in re.finditer(r"\n\|\s*(\d+)\s*\|\|[^\n]*?\[\[([^\]|]+)(?:\|[^\]]*)?\]\][^\n]*?\|\|\s*(\d+)\s*\|\|\s*(\d+)\s*\|\|\s*(\d+)\s*\|\|\s*(\d+)\s*\|\|\s*(\d+)\s*\|\|\s*(\d+)", w[j:]):
        pos = int(m.group(1))
        if out and pos <= out[-1][0]: break
        n = [int(m.group(k)) for k in range(3, 9)]
        out.append((pos, clube(m.group(2).strip()), *n, 0))
    return out or None

def painel():
    s = open("painel/dados/esp-1.js", encoding="utf-8").read()
    return json.loads(s[s.index("=") + 1:].strip().rstrip(";"))

if __name__ == "__main__":
    d = painel()
    eds = {e["t"]: e for e in d["EDS"]}
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nl = 0
    for t in temporadas():
        wt = tabela_wiki(t)
        if not wt:
            print(t, "SEM TABELA NA ES.WIKI"); continue
        tab = eds[t]["tab"]   # [clube, pos, J, V, E, D, GP, GC, ajuste]
        pp = {r[0]: r for r in tab}
        difs = []
        if len(wt) != len(tab): difs.append(f"nº de clubes painel {len(tab)} wiki {len(wt)}")
        for r in wt:
            pos, cl, *n = r
            if cl not in pp: difs.append(f"{cl} na wiki ({pos}º) e não no painel"); continue
            q = pp[cl]
            if q[1] != pos: difs.append(f"{cl}: posição painel {q[1]} wiki {pos}")
            if list(q[2:8]) != n[:6]: difs.append(f"{cl}: painel J-V-E-D-GP-GC {q[2:8]} wiki {n[:6]}")
            if (q[8] or 0) != n[6]: difs.append(f"{cl}: ajuste painel {q[8]} wiki {n[6]}")
        for x in difs:
            print(t, x); nl += 1
    print("linhas:", nl, file=sys.stderr)
