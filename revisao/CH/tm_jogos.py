"""Jogos do transfermarkt (CLPD, 'gesamtspielplan') x pacote do chi-1: placar e data, por temporada.
Baixa com cache (revisao/CH/baixar.py). saison_id do transfermarkt = ano - 1 (rótulo 1993 = saison 1992).
Uso: python -I revisao/CH/tm_jogos.py 1990 1991 ...   (anos do campeonato)"""
import csv, html, re, sys
from collections import defaultdict
import importlib.util
_sp = importlib.util.spec_from_file_location("baixar_ch", "revisao/CH/baixar.py"); baixar = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(baixar)
sys.path.insert(0, "coleta/comum-sulamerica"); sys.path.insert(0, "coleta/chi-1")
from clubes_chi import clube
EXTRA = {"cd universidad catolica": "Universidad Católica", "universidad de chile": "Universidad de Chile", "cd everton": "Everton de Viña del Mar",
         "cd palestino": "Palestino", "cd o higgins": "O'Higgins", "rangers de talca": "Rangers de Talca", "cd huachipato": "Huachipato",
         "cd cobreloa": "Cobreloa", "cd cobresal": "Cobresal", "csd colo colo": "Colo Colo", "audax italiano": "Audax Italiano",
         "cd antofagasta": "Deportes Antofagasta", "cd iquique": "Deportes Iquique", "cd la serena": "Deportes La Serena",
         "cd temuco": "Deportes Temuco", "ac barnechea": "Deportes Barnechea", "cd nublense": "Ñublense", "cd magallanes": "Magallanes",
         "cd cobresal": "Cobresal", "cd copiapo": "Deportes Copiapó", "cd puerto montt": "Deportes Puerto Montt", "cd melipilla": "Deportes Melipilla",
         "cd provincial osorno": "Provincial Osorno", "cd curico unido": "Curicó Unido", "cd concepcion": "Deportes Concepción",
         "cd santiago morning": "Santiago Morning", "cd union san felipe": "Unión San Felipe", "cd limache": "Deportes Limache", "ccd fernandez vial": "Fernández Vial"}
def ch(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
def nome(n, ano):
    return EXTRA.get(ch(n)) or clube(n, ano) or n
def tm(ano):
    p = baixar.url(f"https://www.transfermarkt.com/primera-division-de-chile/gesamtspielplan/wettbewerb/CLPD/saison_id/{ano-1}", f"tm_plan_{ano-1}.html")
    s = open(p, encoding="utf-8", errors="replace").read()
    jogos = []; rod = None; data = None
    for bloco in re.split(r'<div class="content-box-headline">', s)[1:]:
        m = re.match(r"\s*(\d+)\.Matchday", bloco); rod = int(m.group(1)) if m else None
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", bloco, re.S):
            d = re.search(r'datum/(\d{4}-\d\d-\d\d)', tr)
            if d and 'hide-for-small' in tr: data = d.group(1)
            tt = re.findall(r'hauptlink[^>]*>\s*<a title="([^"]+)"', tr)
            r = re.search(r'spielbericht/(\d+)">\s*(\d+):(\d+)', tr)
            aw = re.findall(r'<td class="no-border-links hauptlink">\s*<a title="([^"]+)"', tr) or re.findall(r'no-border-links[^"]*hauptlink[^>]*>\s*<a title="([^"]+)"', tr)
            if r and tt:
                titles = re.findall(r'<a title="([^"]+)" href="/[^"]+/spielplan/verein/', tr)
                casa, fora = html.unescape(titles[0]), html.unescape(titles[-1])
                jogos.append((rod, data, nome(casa, ano), nome(fora, ano), int(r.group(2)), int(r.group(3)), r.group(1)))
    return jogos
pac = defaultdict(list)
for r in csv.DictReader(open("data/coleta/chi-1/pacote/partidas.csv", encoding="utf-8")):
    pac[r["temporada"][:4]].append(r)
tot = defaultdict(int)
for a in map(int, sys.argv[1:]):
    js = tm(a)
    ps = pac[str(a)]
    usados = set(); dif_placar = []; dif_data = []; sem = []
    for rod, data, m, v, gm, gv, tid in js:
        cand = [i for i, p in enumerate(ps) if i not in usados and p["mandante"] == m and p["visitante"] == v]
        if not cand:
            sem.append((data, m, v, gm, gv)); continue
        i = min(cand, key=lambda i: abs(int((ps[i]["data"] or "0000").replace("-", "")[:8] or 0) - int(data.replace("-", ""))) if data else 0)
        usados.add(i); p = ps[i]
        if p["gols_mandante"] != str(gm) or p["gols_visitante"] != str(gv):
            dif_placar.append((data, m, v, f"tm {gm}-{gv}", f"pacote {p['gols_mandante']}-{p['gols_visitante']} {p['resultado_especial']}", p["fonte"], tid))
        from datetime import date as _d
        try:
            _dd = abs((_d.fromisoformat(p["data"]) - _d.fromisoformat(data)).days) if p["data"] else 99
        except ValueError:
            _dd = 99
        if data and _dd > 1:
            dif_data.append((m, v, f"tm {data}", f"pacote {p['data']}", p["fonte"], tid))
    nomes_tm = {x for j in js for x in j[2:4]}
    print(f"== {a}: transfermarkt {len(js)} jogos; casados {len(usados)}; pacote {len(ps)}; placar diferente {len(dif_placar)}; data diferente (>1 dia) {len(dif_data)}; sem par {len(sem)}")
    for x in dif_placar: print("   PLACAR", x)
    for x in dif_data[:8]: print("   DATA", x)
    if len(dif_data) > 8: print("   ... +", len(dif_data) - 8, "datas")
    for x in sem[:6]: print("   SEM PAR", x)
    desconhecidos = sorted(n for n in nomes_tm if n not in {p["mandante"] for p in ps} | {p["visitante"] for p in ps})
    if desconhecidos: print("   nomes do tm sem clube no pacote:", desconhecidos)
    tot["tm"] += len(js); tot["casados"] += len(usados); tot["placar"] += len(dif_placar); tot["data"] += len(dif_data)
print(dict(tot))
