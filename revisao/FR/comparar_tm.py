"""FR: compara placares e datas do pacote fra-1 com o calendário do transfermarkt (uma página por temporada).
Clubes casados pelo código do transfermarkt, por votação (jogo com mesma data e placar).
Uso (na raiz): python -I -X utf8 revisao/FR/comparar_tm.py > SCRATCH/FR/comparar_tm.txt"""
import csv, html, os, re
from collections import Counter, defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(RAIZ, "data", "cache", "revisao", "FR")
P = os.path.join(RAIZ, "data", "coleta", "fra-1", "pacote")
J = list(csv.DictReader(open(os.path.join(P, "partidas.csv"), encoding="utf-8")))

LINHA = re.compile(r"<tr>\s*<td class=\"hide-for-small\">(.*?)</td>.*?verein/(\d+)/saison_id[^>]*>([^<]*)</a></td>.*?"
                   r"class=\"ergebnis-link\"[^>]*>([^<]*)</a>.*?<td class=\"no-border-links hauptlink\"><a title=\"[^\"]*\" "
                   r"href=\"/[^\"]*/verein/(\d+)/saison_id[^>]*>([^<]*)</a>", re.S)


def tm(a):
    arq = os.path.join(CACHE, f"tm_FR1_{a}.html")
    if not os.path.exists(arq):
        return None
    t = open(arq, encoding="utf-8", errors="replace").read()
    res, data = [], None
    for m in LINHA.finditer(t):
        d = re.search(r"datum/(\d{4}-\d{2}-\d{2})", m.group(1))
        if d:
            data = d.group(1)
        r = re.match(r"\s*(\d+):(\d+)\s*(.*)$", html.unescape(m.group(4)))
        res.append({"data": data, "m": m.group(2), "nm": html.unescape(m.group(3)).strip(), "v": m.group(5),
                    "nv": html.unescape(m.group(6)).strip(),
                    "gm": int(r.group(1)) if r else None, "gv": int(r.group(2)) if r else None, "res": m.group(4).strip()})
    return res


temps = sorted({j["temporada"] for j in J})
nos = defaultdict(list)
for j in J:
    nos[j["temporada"]].append(j)
dados = {T: tm(int(T[:4])) for T in temps}
# votação
votos, votos_ano = defaultdict(Counter), defaultdict(Counter)
for T, lst in dados.items():
    if not lst:
        continue
    idx = defaultdict(list)
    for j in nos[T]:
        if j["data"]:
            idx[(j["data"], int(j["gols_mandante"]), int(j["gols_visitante"]))].append(j)
    for x in lst:
        if x["gm"] is None or not x["data"]:
            continue
        d = date.fromisoformat(x["data"])
        cand = [j for k in (-1, 0, 1) for j in idx.get((date.fromordinal(d.toordinal() + k).isoformat(), x["gm"], x["gv"]), [])]
        if len(cand) == 1:
            for lado, c in (("m", cand[0]["mandante"]), ("v", cand[0]["visitante"])):
                votos[x[lado]][c] += 1
                votos_ano[(x[lado], T)][c] += 1
geral = {k: c.most_common(1)[0][0] for k, c in votos.items()}
por_ano = {k: c.most_common(1)[0][0] for k, c in votos_ano.items()}


def clube(cod, T):
    return por_ano.get((cod, T)) or geral.get(cod)


tot = Counter()
por_decada = defaultdict(Counter)
for T in temps:
    lst = dados[T]
    if lst is None:
        print(f"{T}: sem página do transfermarkt")
        continue
    dec = T[:3] + "0s"
    pares = {(j["mandante"], j["visitante"]): j for j in nos[T]}
    vistos = set()
    difs = []
    for x in lst:
        m, v = clube(x["m"], T), clube(x["v"], T)
        if not m or not v:
            difs.append(f"  sem casamento: {x['nm']} x {x['nv']} ({x['data']}) {x['res']}")
            continue
        j = pares.get((m, v))
        if j is None:
            difs.append(f"  jogo do TM sem par no pacote: {m} {x['res']} {v} ({x['data']})")
            continue
        vistos.add((m, v))
        tot["jogos"] += 1
        por_decada[dec]["jogos"] += 1
        if x["gm"] is None:
            difs.append(f"  TM sem placar: {m} x {v} ({x['data']}) '{x['res']}' | pacote {j['gols_mandante']}-{j['gols_visitante']}")
            continue
        if (x["gm"], x["gv"]) != (int(j["gols_mandante"]), int(j["gols_visitante"])):
            tot["placar_dif"] += 1
            por_decada[dec]["placar_dif"] += 1
            inv = pares.get((v, m))
            difs.append(f"  PLACAR {m} x {v}: TM {x['gm']}-{x['gv']} ({x['data']}) | pacote {j['gols_mandante']}-{j['gols_visitante']} "
                        f"({j['data']})" + (f" | volta no pacote {inv['gols_mandante']}-{inv['gols_visitante']}" if inv else "")
                        + (f" | {x['res']}" if not re.fullmatch(r"\d+:\d+", x["res"]) else "")
                        + (f" | obs: {j['observacao'][:80]}" if j["observacao"] else ""))
        if j["data"] and x["data"]:
            por_decada[dec]["datas"] += 1
            dd = abs((date.fromisoformat(j["data"]) - date.fromisoformat(x["data"])).days)
            if dd:
                tot["data_dif"] += 1
                por_decada[dec]["data_dif"] += 1
                if dd > 1:
                    por_decada[dec]["data_dif_2+"] += 1
                difs.append(f"  DATA {m} x {v}: TM {x['data']} | pacote {j['data']} ({dd} dias)")
        elif x["data"] and not j["data"]:
            por_decada[dec]["data_so_tm"] += 1
    faltam = len(pares) - len(vistos)
    print(f"{T}: TM {len(lst)} jogos, casados {len(vistos)} de {len(pares)}" + (f" ({faltam} sem TM)" if faltam else ""))
    for d in difs:
        print(d)
print("\nRESUMO", dict(tot))
for dec in sorted(por_decada):
    print(dec, dict(por_decada[dec]))
