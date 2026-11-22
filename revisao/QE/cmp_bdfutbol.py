"""Pacote (eng-1 / esp-1) x BDFutbol: todos os jogos de cada temporada (placar, data), cobertura de árbitro e estádio.

Casamento de nomes por voto (mesma data e mesmo placar), depois o jogo é achado pelo par mandante x visitante da temporada.
Saída: revisao/QE/cmp_bdfutbol_<liga>.txt (diferenças) e resumo por década na tela.
Uso: python -I revisao/QE/cmp_bdfutbol.py esp|eng
"""
import csv
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import nome_cache  # noqa: E402
import bdfutbol as bdf  # noqa: E402


def dmy(s):
    d, m, a = s.split("/")
    return f"{a}-{m}-{d}"


def main(liga):
    sys.stdout.reconfigure(encoding="utf-8")
    slug = "esp-1" if liga == "esp" else "eng-1"
    P = f"data/coleta/{slug}/pacote/"
    pac = defaultdict(list)
    for j in csv.DictReader(open(P + "partidas.csv", encoding="utf-8")):
        pac[int(j["temporada"][:4])].append(j)
    a0 = 1928 if liga == "esp" else 1960
    bd = {}
    for ai in sorted(pac):
        if ai < a0:
            continue
        arq = nome_cache(bdf.url_temporada(liga, ai))
        if os.path.exists(arq):
            bd[ai] = bdf.jogos_temporada(arq)
    # voto de nomes
    voto = defaultdict(Counter)
    for ai, bj in bd.items():
        idx = defaultdict(list)
        for j in pac[ai]:
            idx[(j["data"], j["gols_mandante"], j["gols_visitante"])].append(j)
        for b in bj:
            if "/" not in b["data"]:
                continue
            c = idx.get((dmy(b["data"]), b["gm"], b["gv"]), [])
            if len(c) == 1:
                voto[(ai, b["mandante"])][c[0]["mandante"]] += 1
                voto[(ai, b["visitante"])][c[0]["visitante"]] += 1
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
    dec = defaultdict(lambda: Counter())
    for ai, bj in sorted(bd.items()):
        T = f"{ai}/{str(ai + 1)[-2:]}"
        pk = {}
        for j in pac[ai]:
            fase2 = j["fase"] != "Liga" and j["fase"] != "" and liga == "esp"
            pk[(j["mandante"], j["visitante"], fase2)] = j
        vistos = set()
        for b in bj:
            m, v = nome(ai, b["mandante"]), nome(ai, b["visitante"])
            fase2 = liga == "esp" and ai == 1986 and b["rodada"] > 34
            j = pk.get((m, v, fase2))
            D = dec[ai // 10 * 10]
            D["bdf"] += 1
            if b["arbitro"]:
                D["bdf_arbitro"] += 1
            if not j:
                out.append(f"{T}\tSÓ NO BDFUTBOL\t{b['data']} {b['mandante']} {b['gm']}-{b['gv']} {b['visitante']} (rodada {b['rodada']}; id {b['pid']})")
                D["so_bdf"] += 1
                continue
            vistos.add(id(j))
            pares[j["id"]] = {"pid": b["pid"], "arbitro": b["arbitro"], "estadio": b["estadio"]}
            D["casados"] += 1
            pl_ok = (b["gm"], b["gv"]) == (j["gols_mandante"], j["gols_visitante"])
            dt_ok = "/" in b["data"] and dmy(b["data"]) == j["data"]
            D["placar_ok"] += pl_ok
            D["data_ok"] += dt_ok
            if not pl_ok:
                out.append(f"{T}\tPLACAR\t{j['data']} {m} x {v}: pacote {j['gols_mandante']}-{j['gols_visitante']}, BDFutbol {b['gm']}-{b['gv']} ({b['placar_txt']}; id {b['pid']}){' [' + j['resultado_especial'] + ']' if j['resultado_especial'] else ''}")
            if not dt_ok:
                out.append(f"{T}\tDATA\t{m} x {v} {j['gols_mandante']}-{j['gols_visitante']}: pacote {j['data']}, BDFutbol {b['data']} (id {b['pid']})")
        for j in pac[ai]:
            if id(j) not in vistos:
                out.append(f"{T}\tSÓ NO PACOTE\t{j['data']} {j['mandante']} {j['gols_mandante']}-{j['gols_visitante']} {j['visitante']} ({j['fase']})")
                dec[ai // 10 * 10]["so_pac"] += 1
    # classificação final: BDFutbol x pacote
    fin = defaultdict(list)
    for r in csv.DictReader(open(P + "classificacao_final.csv", encoding="utf-8")):
        fin[int(r["temporada"][:4])].append(r)
    tab_ok = tab_n = 0
    for ai in sorted(bd):
        tb = bdf.tabela_final(nome_cache(bdf.url_temporada(liga, ai)))
        T = f"{ai}/{str(ai + 1)[-2:]}"
        if not tb or len(tb) != len(fin[ai]):
            out.append(f"{T}\tTABELA\tBDFutbol sem tabela única ({len(tb)} linhas)")
            continue
        pf = {r["clube"]: r for r in fin[ai]}
        for x in tb:
            c = nome(ai, x["nome"])
            r = pf.get(c)
            tab_n += 1
            if not r:
                out.append(f"{T}\tTABELA\t{x['nome']} sem par")
                continue
            a = (int(r["posicao"]), int(r["jogos"]), int(r["vitorias"]), int(r["empates"]), int(r["derrotas"]),
                 int(r["gols_pro"]), int(r["gols_contra"]), int(r["pontos"]))
            b = (x["pos"], x["j"], x["v"], x["e"], x["d"], x["gp"], x["gc"], x["pts"])
            if a == b:
                tab_ok += 1
            else:
                out.append(f"{T}\tTABELA\t{c}: pacote pos/J/V/E/D/GP/GC/Pts {a}, BDFutbol {b}")
    import json
    json.dump(pares, open(f"data/cache/revisao/QE/pares_bdfutbol_{liga}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"classificação final: {tab_ok} de {tab_n} linhas iguais (posição, J, V, E, D, GP, GC, Pts)")
    open(f"revisao/QE/cmp_bdfutbol_{liga}.txt", "w", encoding="utf-8").write("\n".join(out))
    print("década | jogos BDFutbol | casados | placar igual | data igual | só BDFutbol | só pacote | com árbitro no BDFutbol")
    for d in sorted(dec):
        D = dec[d]
        print(f"{d}s | {D['bdf']} | {D['casados']} | {D['placar_ok']} | {D['data_ok']} | {D['so_bdf']} | {D['so_pac']} | {D['bdf_arbitro']} ({100 * D['bdf_arbitro'] // max(D['bdf'], 1)}%)")
    print("temporadas comparadas:", len(bd), "| linhas de diferença:", len(out))


if __name__ == "__main__":
    main(sys.argv[1])
