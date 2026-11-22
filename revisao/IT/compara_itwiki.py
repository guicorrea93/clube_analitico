"""Compara o pacote da ita-1 com a Wikipédia it (classificação final, rebaixados, placares da matriz, artilheiros).
Uso: python -I revisao/IT/compara_itwiki.py > SCRATCH/IT/compara_itwiki.txt
"""
import csv, os, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import itwiki  # noqa: E402

PAC = os.path.join(itwiki.RAIZ, "data", "coleta", "ita-1", "pacote")


def ler(n):
    return list(csv.DictReader(open(os.path.join(PAC, n), encoding="utf-8")))


cf = defaultdict(list)
for x in ler("classificacao_final.csv"):
    cf[int(x["temporada"][:4])].append(x)
pj = defaultdict(list)
for x in ler("partidas.csv"):
    pj[int(x["temporada"][:4])].append(x)
art = defaultdict(list)
for x in ler("artilheiros.csv"):
    art[int(x["temporada"][:4])].append(x)

tot = defaultdict(int)
for a in itwiki.ANOS:
    T = f"{a}/{str(a+1)[-2:]}"
    w = itwiki.classifica(a) or []
    leg = itwiki.legenda(a)
    reb_cor = {c for c, d in leg.items() if "retroc" in d.lower() or "serie b" in d.lower() and "ammess" not in d.lower()}
    if a == 1945:
        print(f"## {T}: (Divisione Nazionale; classificação da wiki: {len(w)} linhas)")
    # classificação
    pac = {x["clube"]: x for x in cf[a]}
    if len(w) != len(pac) and a != 1945:
        print(f"{T} CLS número de linhas wiki {len(w)} pacote {len(pac)}")
    for x in w:
        p = pac.get(x["clube"])
        tot["cls_linhas"] += 1
        if not p:
            print(f"{T} CLS clube da wiki fora do pacote: {x['nome']} -> {x['clube']}")
            continue
        meu = [int(p["posicao"]), int(p["pontos"]), int(p["jogos"]), int(p["vitorias"]), int(p["empates"]), int(p["derrotas"]),
               int(p["gols_pro"]), int(p["gols_contra"]), int(p["ajuste_pontos"] or 0)]
        dele = [x["pos"], x["pts"], x["g"], x["v"], x["n"], x["p"], x["gf"], x["gs"], x["pen"]]
        if a == 1945:
            continue
        if meu[1:] != dele[1:]:
            tot["cls_dif_num"] += 1
            print(f"{T} CLS números {x['clube']}: pacote pos,pts,J,V,E,D,GP,GC,aj={meu} | wiki={dele}")
        elif meu[0] != dele[0]:
            tot["cls_dif_pos"] += 1
            print(f"{T} CLS posição {x['clube']}: pacote {meu[0]} wiki {dele[0]} (pts {meu[1]})")
        else:
            tot["cls_ok"] += 1
    # rebaixados
    wreb = {x["clube"] for x in w if x["cor"] in reb_cor}
    preb = {x["clube"] for x in cf[a] if x["situacao"] == "rebaixado"}
    if wreb != preb:
        print(f"{T} REB pacote={sorted(preb)} wiki(cor)={sorted(wreb)} legenda={[d for c, d in leg.items() if c in reb_cor]}")
    # campeão
    pc = next((x["clube"] for x in cf[a] if x["situacao"] == "campeao"), None)
    wc = next((x["clube"] for x in w if x["cor"] == "#99CBFF"), None)
    if pc != wc:
        print(f"{T} CAMPEAO pacote={pc} wiki(cor)={wc}")
    # matriz
    tb = itwiki.tabellone(a)
    if tb is None or "_erro" in tb:
        print(f"{T} MATRIZ sem leitura: {tb and tb.get('_erro')}")
    else:
        liga = [j for j in pj[a] if j["fase"] in ("Liga",)]
        vistos = set()
        for j in liga:
            k = (j["mandante"], j["visitante"])
            vistos.add(k)
            if k not in tb:
                print(f"{T} MATRIZ jogo fora da matriz: {k}")
                continue
            gm, gv, nota = tb[k]
            tot["jogos"] += 1
            if (gm, gv) != (int(j["gols_mandante"]), int(j["gols_visitante"])):
                tot["jogos_dif"] += 1
                print(f"{T} PLACAR {j['data']} {k[0]} x {k[1]}: pacote {j['gols_mandante']}-{j['gols_visitante']}"
                      f"{' ['+j['resultado_especial']+']' if j['resultado_especial'] else ''} | wiki {gm}-{gv} {nota[:60]}")
            elif nota and not j["resultado_especial"]:
                print(f"{T} NOTA {j['data']} {k[0]} x {k[1]}: {j['gols_mandante']}-{j['gols_visitante']} sem resultado_especial | wiki: {nota[:80]}")
            if j["resultado_especial"] and not nota:
                print(f"{T} AWD-PACOTE {j['data']} {k[0]} x {k[1]} {j['gols_mandante']}-{j['gols_visitante']} [{j['resultado_especial']}] obs={j['observacao'][:80]} | wiki sem nota")
        if liga:
            falta = [k for k in tb if isinstance(k, tuple) and k not in vistos]
            if falta:
                print(f"{T} MATRIZ pares da wiki sem jogo no pacote: {falta[:5]}")
    # artilheiro
    m = itwiki.marcatori(a)
    if m:
        topo = max(g for g, _, _ in m)
        wl = sorted((n, g) for g, n, _ in m if g == topo)
        pl = sorted((x["jogador"], int(x["gols"])) for x in art[a])
        if [g for _, g in wl] != [g for _, g in pl] or len(wl) != len(pl):
            print(f"{T} ARTILHEIRO pacote={pl} wiki={wl}")
        else:
            tot["art_ok"] += 1
    else:
        print(f"{T} ARTILHEIRO sem marcatori na wiki")
print(dict(tot))
