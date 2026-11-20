"""Revisão Série C (SC): tabelas da Wikipédia (pt e en) x pacote.

- tabela "Classificação geral/final" -> classificacao_final.csv (posição, J, V, E, D, GP, GC, pontos);
- tabelas de grupo -> soma dos jogos do pacote naquela fase (a fase que melhor casa com os times da tabela).
Saída: lista de divergências e um resumo por edição.
Uso: python -I revisao/SC/conf_tabelas.py [ano ...]
"""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import ler_csv  # noqa: E402
from infobox import ANOS, texto  # noqa: E402
from nomes import casar  # noqa: E402
from tabelas_wiki import tabelas  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CF = defaultdict(list)
for r in ler_csv("classificacao_final.csv"):
    CF[int(r["temporada"])].append(r)
PT = defaultdict(list)
for r in ler_csv("partidas.csv"):
    if r["gols_mandante"] != "":
        PT[int(r["temporada"])].append(r)
PV = {int(r["temporada"]): int(r["pontos_vitoria"]) for r in ler_csv("edicoes.csv")}
CAMPOS = ("j", "v", "e", "d", "gp", "gc")


def stats_fase(ano, fase, times):
    s = defaultdict(lambda: dict.fromkeys(CAMPOS, 0))
    for r in PT[ano]:
        if r["fase"] != fase or r["mandante"] not in times or r["visitante"] not in times:
            continue
        gm, gv = int(r["gols_mandante"]), int(r["gols_visitante"])
        for c, x, y in ((r["mandante"], gm, gv), (r["visitante"], gv, gm)):
            t = s[c]; t["j"] += 1; t["gp"] += x; t["gc"] += y
            t["v" if x > y else "e" if x == y else "d"] += 1
    return s


def main(anos):
    resumo = []
    for ano in anos:
        clubes = [r["clube"] for r in CF[ano]]
        fases = sorted({r["fase"] for r in PT[ano]})
        n_tab = n_lin = n_ok = 0
        for lg in ("pt", "en"):
            txt, arq = texto(lg, ano)
            if not txt:
                continue
            for tb in tabelas(txt):
                sec = " > ".join(tb["secao"])
                geral = any(x in sec.lower() for x in ("geral", "classificação final", "final standings", "overall", "final classification"))
                linhas = tb["linhas"]
                mapa = {i: casar(r["time"], clubes, ano) for i, r in enumerate(linhas)}
                geral = geral or (tb["secao"] and tb["secao"][-1].lower() in ("classificação", "aggregate table"))
                if geral and len(linhas) >= 0.8 * len(clubes):
                    # sem nome: casa pelos números (J, V, E, D, GP, GC) entre os clubes ainda livres
                    livres = set(clubes) - set(mapa.values())
                    for i, c in mapa.items():
                        if c:
                            continue
                        r = linhas[i]
                        ig = [x for x in CF[ano] if x["clube"] in livres and all(
                            r.get(k) is None or r[k] == int(x[kp]) for k, kp in zip(CAMPOS, ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")))]
                        if len(ig) == 1:
                            mapa[i] = ig[0]["clube"]; livres.discard(mapa[i])
                    sem = [linhas[i]["time"] for i, c in mapa.items() if not c]
                    if sem:
                        print(f"{ano} {lg} [{sec}] sem casar: {sem}")
                    n_tab += 1
                    cf = {r["clube"]: r for r in CF[ano]}
                    for i, r in enumerate(linhas):
                        c = mapa[i]
                        if not c:
                            continue
                        n_lin += 1
                        p = cf[c]
                        dif = []
                        if r.get("pos") is not None and r["pos"] != int(p["posicao"]):
                            dif.append(f"pos {p['posicao']}->{r['pos']}")
                        for k, kp in zip(CAMPOS, ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")):
                            if r.get(k) is not None and r[k] != int(p[kp]):
                                dif.append(f"{k} {p[kp]}->{r[k]}")
                        if r.get("pts") is not None and r["pts"] != int(p["pontos"]):
                            dif.append(f"pts {p['pontos']}->{r['pts']}")
                        if dif:
                            print(f"{ano} {lg} GERAL [{sec}] {c}: " + ", ".join(dif))
                        else:
                            n_ok += 1
                    continue
                times = {c for c in mapa.values() if c}
                if len(times) < 2:
                    continue
                melhor = None
                for f in fases:
                    s = stats_fase(ano, f, times)
                    if not all(c in s for c in times):
                        continue
                    d = sum(abs(r.get(k, 0) - s[mapa[i]][k]) for i, r in enumerate(linhas) if mapa[i] for k in CAMPOS
                            if r.get(k) is not None)
                    if melhor is None or d < melhor[0]:
                        melhor = (d, f, s)
                if not melhor:
                    print(f"{ano} {lg} [{sec}] nenhuma fase do pacote tem todos os times da tabela: {sorted(times)}")
                    continue
                n_tab += 1
                d, f, s = melhor
                # sem nome: casa pelos números entre os clubes da fase que jogaram contra os já casados
                livres = {r["mandante"] for r in PT[ano] if r["fase"] == f and r["visitante"] in times} |                          {r["visitante"] for r in PT[ano] if r["fase"] == f and r["mandante"] in times}
                livres -= times
                for i, c in list(mapa.items()):
                    if c:
                        continue
                    r = linhas[i]
                    s2 = stats_fase(ano, f, times | livres)
                    ig = [x for x in livres if all(r.get(k) is None or r[k] == s2[x][k] for k in CAMPOS)]
                    if len(ig) == 1:
                        mapa[i] = ig[0]; livres.discard(ig[0])
                if any(not c for c in mapa.values()):
                    times = {c for c in mapa.values() if c}
                    s = stats_fase(ano, f, times)
                    print(f"{ano} {lg} [{sec}] sem casar: {[linhas[i]['time'] for i, c in mapa.items() if not c]}")
                else:
                    s = stats_fase(ano, f, set(mapa.values()))
                for i, r in enumerate(linhas):
                    c = mapa[i]
                    if not c:
                        continue
                    n_lin += 1
                    dif = [f"{k} {s[c][k]}->{r[k]}" for k in CAMPOS if r.get(k) is not None and r[k] != s[c][k]]
                    if r.get("pts") is not None:
                        pts = PV[ano] * s[c]["v"] + s[c]["e"]
                        if r["pts"] != pts and not dif:
                            dif.append(f"pts calc {pts}->{r['pts']} (punição/bônus?)")
                    if dif:
                        print(f"{ano} {lg} GRUPO [{sec}] fase pacote '{f}' {c}: " + ", ".join(dif))
                    else:
                        n_ok += 1
        resumo.append((ano, n_tab, n_lin, n_ok))
    print("\nano tabelas linhas iguais")
    for r in resumo:
        print(*r)
    print("total", sum(r[1] for r in resumo), sum(r[2] for r in resumo), sum(r[3] for r in resumo))


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or ANOS)
