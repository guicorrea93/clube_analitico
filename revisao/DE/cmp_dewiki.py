"""Pacote ger-1 x Wikipédia de (cada temporada): classificação final (posição, V-E-D, gols, pontos com Abzug),
rebaixados (Farblegende "Abstieg") e todos os placares (Kreuztabelle).
Uso (na raiz): python -I revisao/DE/cmp_dewiki.py > revisao/DE/cmp_dewiki_saida.txt"""
import csv, re, sys, pathlib
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from dewiki import pagina, tabela, legenda, kreuz, titulo, rebaixados_legenda  # noqa: E402
PAC = AQUI.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
cf = defaultdict(list)
for r in csv.DictReader(open(PAC / "classificacao_final.csv", encoding="utf-8")):
    cf[int(r["temporada"][:4])].append(r)
jogos = defaultdict(dict)
for r in csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")):
    jogos[int(r["temporada"][:4])][(r["mandante"], r["visitante"])] = r
ed = {int(r["ano_inicio"]): r for r in csv.DictReader(open(PAC / "edicoes.csv", encoding="utf-8"))}

tot = defaultdict(int)
anos = range(1963, 2026) if len(sys.argv) == 1 else [int(x) for x in sys.argv[1:]]
for a in anos:
    t = pagina(a)
    url = "https://de.wikipedia.org/wiki/" + titulo(a).replace(" ", "_")
    out = []
    tb = tabela(t, a)
    pv = int(ed[a]["pontos_vitoria"])
    meu = {r["clube"]: r for r in cf[a]}
    if len(tb) != len(meu):
        out.append(f"tabela de com {len(tb)} linhas, pacote {len(meu)}")
    for x in tb:
        tot["linhas"] += 1
        if x["clube"] is None:
            out.append(f"sem cadastro: {x['nome']}"); continue
        r = meu.get(x["clube"])
        if r is None:
            out.append(f"clube só no de: {x['clube']}"); continue
        pts_de = pv * x["v"] + x["e"] - x["abzug"]
        pub = [x["pos"], x["v"], x["e"], x["d"], x["gp"], x["gc"], pts_de, -x["abzug"]]
        pk = [int(r[k]) for k in ("posicao", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos", "ajuste_pontos")]
        if pub != pk:
            out.append(f"LINHA {x['clube']}: de [pos,V,E,D,GP,GC,Pts,ajuste]={pub} | pacote {pk}")
            tot["linhas_dif"] += 1
    # rebaixados: legenda com "Abstieg" (sem "Relegation") e cor das linhas
    reb_de = rebaixados_legenda(t, tb, a)
    txt_abst = " | ".join(x for c, x in legenda(t) if re.search(r"Relegation|Abstieg|Absteiger", x))
    reb_pk = {r["clube"] for r in cf[a] if r["situacao"] == "rebaixado"}
    if reb_de != reb_pk:
        out.append(f"REBAIXADOS de {sorted(reb_de)} | pacote {sorted(reb_pk)} | legenda: {txt_abst[:400]}")
        tot["reb_dif"] += 1
    camp_de = next((x["clube"] for x in tb if x["pos"] == 1), None)
    if camp_de != ed[a]["campeao"]:
        out.append(f"CAMPEÃO de {camp_de} | pacote {ed[a]['campeao']}")
    # placares
    kz, prob = kreuz(t, a)
    for p in prob[:5]:
        out.append(f"kreuz: {p}")
    n_ok = n_dif = 0
    for (m, v), (gm, gv) in kz.items():
        j = jogos[a].get((m, v))
        if j is None:
            out.append(f"JOGO só no de: {m} x {v} {gm}:{gv}"); continue
        if (int(j["gols_mandante"]), int(j["gols_visitante"])) != (gm, gv):
            n_dif += 1
            out.append(f"PLACAR {m} x {v} ({j['data']}): pacote {j['gols_mandante']}-{j['gols_visitante']} | de {gm}:{gv} (fonte {j['fonte']})")
        else:
            n_ok += 1
    tot["jogos_ok"] += n_ok; tot["jogos_dif"] += n_dif; tot["jogos_pac"] += len(jogos[a])
    print(f"{a}/{str(a+1)[-2:]}: tabela {len(tb)} linhas; Kreuztabelle {len(kz)} de {len(jogos[a])} jogos, {n_ok} iguais, {n_dif} diferentes  ({url})")
    for o in out:
        print("   ", o)
print(dict(tot))
