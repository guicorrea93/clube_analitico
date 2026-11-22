"""eng-1 x transfermarkt (competição EFD1, "First Division bis 91/92", 1888/89-1991/92): todos os jogos das temporadas
baixadas (placar e data), por década. Página: https://www.transfermarkt.com/first-division-bis-91-92-/gesamtspielplan/wettbewerb/EFD1/saison_id/<ano>
Casamento de nomes por voto (mesma data e placar). Saída: revisao/QE/cmp_tm_eng.txt.
Uso: python -I revisao/QE/cmp_tm_eng.py [ano_ini ano_fim]
"""
import csv
import os
import re
import sys
from collections import Counter, defaultdict
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import nome_cache  # noqa: E402

URL = "https://www.transfermarkt.com/first-division-bis-91-92-/gesamtspielplan/wettbewerb/EFD1/saison_id/{}"
TR = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)


def jogos_tm(arq):
    t = open(arq, encoding="utf-8", errors="replace").read()
    res = []
    data = None
    for tr in TR.findall(t):
        m = re.search(r"datum/(\d{4}-\d\d-\d\d)\">", tr)
        if m:
            data = m.group(1)
        r = re.search(r"class=\"ergebnis-link\" id=\"(\d+)\"[^>]*>\s*(\d+):(\d+)", tr)
        tm = [re.search(r'<a title="([^"]+)" href="/[^"]*/verein/(\d+)', x).groups()
              for x in re.findall(r'<td class="[^"]*hauptlink[^"]*">(.*?)</td>', tr, re.S) if "/verein/" in x]
        if r and len(tm) >= 2 and data:
            res.append({"data": data, "gm": r.group(2), "gv": r.group(3), "id": r.group(1),
                        "m": tm[0][0], "v": tm[-1][0]})
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a0, a1 = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1888, 1991)
    pac = defaultdict(list)
    for j in csv.DictReader(open("data/coleta/eng-1/pacote/partidas.csv", encoding="utf-8")):
        pac[int(j["temporada"][:4])].append(j)
    tm = {}
    for ai in range(a0, a1 + 1):
        arq = nome_cache(URL.format(ai))
        if os.path.exists(arq) and ai in pac:
            tm[ai] = jogos_tm(arq)
    voto = defaultdict(Counter)
    for ai, js in tm.items():
        idx = defaultdict(list)
        for j in pac[ai]:
            idx[(j["data"], j["gols_mandante"], j["gols_visitante"])].append(j)
        for b in js:
            c = idx.get((b["data"], b["gm"], b["gv"]), [])
            if len(c) == 1:
                voto[(ai, b["m"])][c[0]["mandante"]] += 1
                voto[(ai, b["v"])][c[0]["visitante"]] += 1
    glob = defaultdict(Counter)
    for (ai, n), cnt in voto.items():
        for k, v in cnt.items():
            glob[n][k] += v

    def nome(ai, n):
        if voto.get((ai, n)):
            return voto[(ai, n)].most_common(1)[0][0]
        return glob[n].most_common(1)[0][0] if glob.get(n) else None
    out = []
    pares = {}
    dec = defaultdict(Counter)
    for ai, js in sorted(tm.items()):
        T = f"{ai}/{str(ai + 1)[-2:]}"
        pk = {(j["mandante"], j["visitante"]): j for j in pac[ai]}
        vistos = set()
        D = dec[ai // 10 * 10]
        D["temporadas"] += 1
        for b in js:
            j = pk.get((nome(ai, b["m"]), nome(ai, b["v"])))
            D["tm"] += 1
            if not j:
                out.append(f"{T}\tSÓ NO TRANSFERMARKT\t{b['data']} {b['m']} {b['gm']}-{b['gv']} {b['v']} (id {b['id']})")
                continue
            vistos.add(j["id"])
            pares[j["id"]] = b["id"]
            D["casados"] += 1
            pl = (b["gm"], b["gv"]) == (j["gols_mandante"], j["gols_visitante"])
            dt = b["data"] == j["data"]
            D["placar_ok"] += pl
            D["data_ok"] += dt
            if not pl:
                out.append(f"{T}\tPLACAR\t{j['data']} {j['mandante']} x {j['visitante']}: pacote {j['gols_mandante']}-{j['gols_visitante']}, transfermarkt {b['gm']}-{b['gv']} (id {b['id']})")
            if not dt:
                out.append(f"{T}\tDATA\t{j['mandante']} x {j['visitante']} {j['gols_mandante']}-{j['gols_visitante']}: pacote {j['data']}, transfermarkt {b['data']} (id {b['id']})")
        for j in pac[ai]:
            if j["id"] not in vistos:
                out.append(f"{T}\tSÓ NO PACOTE\t{j['data']} {j['mandante']} {j['gols_mandante']}-{j['gols_visitante']} {j['visitante']}")
                D["so_pac"] += 1
    open("revisao/QE/cmp_tm_eng.txt", "w", encoding="utf-8").write("\n".join(out))
    import json
    json.dump(pares, open("data/cache/revisao/QE/pares_tm_eng.json", "w", encoding="utf-8"))
    print("década | temporadas | jogos TM | casados | placar igual | data igual | só no pacote")
    for d in sorted(dec):
        D = dec[d]
        print(f"{d}s | {D['temporadas']} | {D['tm']} | {D['casados']} | {D['placar_ok']} | {D['data_ok']} | {D['so_pac']}")
    print("linhas de diferença:", len(out))


if __name__ == "__main__":
    main()
