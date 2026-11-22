"""Datas e placares: pacote ger-1 x transfermarkt (gesamtspielplan, uma página por temporada, todos os jogos com data).
Clubes casados pelo nome completo do transfermarkt (atributo title), pelo cadastro da coleta, e por votação quando falta.
Uso: python -I revisao/DE/cmp_tm.py [anos...] > revisao/DE/cmp_tm_saida.txt"""
import csv, re, sys, pathlib, html, time
from collections import defaultdict, Counter
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_ger as cg  # noqa
from rev_baixar import baixar, nome_cache  # noqa
PAC = RAIZ / "data" / "coleta" / "ger-1" / "pacote"
jogos = defaultdict(dict)
for r in csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")):
    jogos[int(r["temporada"][:4])][(r["mandante"], r["visitante"])] = r


def url(a):
    return f"https://www.transfermarkt.com/bundesliga/gesamtspielplan/wettbewerb/L1/saison_id/{a}"


def ler(a):
    f = nome_cache(url(a))
    if not f.exists():
        time.sleep(2)
    b = baixar(url(a)).decode("utf-8", "replace")
    res, data = [], None
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", b, re.S):
        m = re.search(r'datum/(\d{4}-\d{2}-\d{2})"', tr)
        if m:
            data = m.group(1)
        r = re.search(r'class="ergebnis-link"[^>]*>(\d+):(\d+)<', tr)
        if not r:
            continue
        t = re.findall(r'hauptlink"?[^>]*>\s*<a title="([^"]+)"', tr)
        if len(t) < 2:
            t = re.findall(r'<a title="([^"]+)" href="/[^"]+/spielplan/verein/', tr)
            t = [t[0], t[-1]] if t else []
        if len(t) < 2:
            continue
        res.append((data, html.unescape(t[0]), html.unescape(t[1]), int(r.group(1)), int(r.group(2))))
    return res


tot = Counter()
anos = [int(x) for x in sys.argv[1:]] or list(range(1963, 2026))
for a in anos:
    tm = ler(a)
    # nome do transfermarkt -> clube do pacote: cadastro, senão votação (mesmo placar e data ±3 dias)
    mapa = {}
    for d, m, v, gm, gv in tm:
        for n in (m, v):
            if n not in mapa:
                k = cg.esd(n, a) or cg.esd(re.sub(r"^(1\.\s*FC|FC|SV|VfB|VfL|TSV|SC|SpVgg|Borussia)\s+", "", n), a)
                mapa[n] = cg.exibicao(k) if k else None
    falta = {n for n, c in mapa.items() if c is None}
    if falta:
        votos = defaultdict(Counter)
        por = defaultdict(list)
        for p in jogos[a].values():
            por[(int(p["gols_mandante"]), int(p["gols_visitante"]))].append(p)
        for d, m, v, gm, gv in tm:
            c = [p for p in por[(gm, gv)] if p["data"] and d and abs((date.fromisoformat(p["data"]) - date.fromisoformat(d)).days) <= 3
                 and (mapa.get(m) in (None, p["mandante"])) and (mapa.get(v) in (None, p["visitante"]))]
            if len(c) == 1:
                if m in falta: votos[m][c[0]["mandante"]] += 1
                if v in falta: votos[v][c[0]["visitante"]] += 1
        for n in falta:
            if votos[n]:
                mapa[n] = votos[n].most_common(1)[0][0]
    dif_d, dif_p, sem = [], [], []
    for d, m, v, gm, gv in tm:
        p = jogos[a].get((mapa.get(m), mapa.get(v)))
        if not p:
            sem.append(f"{m} x {v}"); continue
        tot["n"] += 1
        if (int(p["gols_mandante"]), int(p["gols_visitante"])) != (gm, gv):
            dif_p.append(f"{p['mandante']} x {p['visitante']} ({p['data']}): pacote {p['gols_mandante']}-{p['gols_visitante']} | tm {gm}:{gv}")
        if d != p["data"]:
            dd = abs((date.fromisoformat(p["data"]) - date.fromisoformat(d)).days) if d and p["data"] else -1
            dif_d.append((dd, f"{p['mandante']} x {p['visitante']} (rodada {p['rodada']}): pacote {p['data']} | tm {d} [{dd} dias]"))
    tot["dif_data"] += len(dif_d); tot["dif_placar"] += len(dif_p); tot["sem_par"] += len(sem)
    print(f"{a}/{str(a+1)[-2:]}: tm {len(tm)} jogos, {len(tm) - len(sem)} casados; datas diferentes {len(dif_d)} (>1 dia: "
          f"{sum(1 for x, _ in dif_d if x > 1)}); placares diferentes {len(dif_p)}", flush=True)
    for x in sem[:3]:
        print("    SEM PAR", x)
    for x in dif_p:
        print("    PLACAR", x)
    for dd, x in sorted(dif_d, reverse=True):
        print("    DATA", x)
print(dict(tot))
