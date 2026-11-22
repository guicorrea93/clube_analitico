"""Classificação final do pacote per-1 x tabela acumulada (a de mais jogos com os mesmos clubes) das páginas de temporada
da Wikipédia es (módulo sports table: win_X, draw_X, loss_X, gf_X, ga_X, adjust_points_X).
Uso (raiz): python -I revisao/PE/tabelas_es.py -> revisao/PE/tabelas_es_saida.txt"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from jogos_es import clubes_pacote, resolve  # noqa: E402

R = Path(__file__).resolve().parents[2]
C = R / "data/cache/revisao/PE"
P = R / "data/coleta/per-1/pacote"
COD = r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9]+"


def blocos(t):
    for bl in re.split(r"\{\{\s*#invoke:\s*sports table", t)[1:]:
        bl = bl.split("\n}}")[0]
        nomes = {c: n for c, n in re.findall(r"name_(" + COD + r")\s*=\s*((?:\[\[[^\]]*\]\]|[^\n|])*)", bl)}
        ordem = re.findall(r"team\d+\s*=\s*(" + COD + r")", bl)
        linhas = {}
        for c in ordem:
            g = lambda k: (lambda m: int(m.group(1)) if m else 0)(re.search(rf"\b{k}_{re.escape(c)}\s*=\s*(-?\d+)", bl))
            linhas[c] = dict(v=g("win"), e=g("draw"), d=g("loss"), gp=g("gf"), gc=g("ga"), aj=g("adjust_points"))
        pv = 2 if re.search(r"(win_points|puntos_ganado)\s*=\s*2", bl) else 3
        yield nomes, ordem, linhas, pv


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mapa = clubes_pacote()
    cl = defaultdict(list)
    for r in csv.DictReader(open(P / "classificacao_final.csv", encoding="utf-8")):
        cl[int(r["temporada"])].append(r)
    out = []
    resumo = []
    for f in sorted(C.glob("es_temporada_*.json")):
        y = int(f.stem.split("_")[-1])
        if y not in cl or y < 1926:
            continue
        t = json.loads(f.read_text(encoding="utf-8"))["parse"]["wikitext"]
        pac = {r["clube"]: r for r in cl[y]}
        melhor = None
        for nomes, ordem, linhas, pv in blocos(t):
            res = {}
            for c in ordem:
                if c in nomes:
                    n = resolve(nomes[c], mapa, set(pac))
                    if n:
                        res[n] = linhas[c]
            if len(res) < 0.8 * len(pac) or len(res) > len(pac):
                continue
            jogos = sum(x["v"] + x["e"] + x["d"] for x in res.values())
            if not melhor or jogos > melhor[0]:
                melhor = (jogos, res, pv)
        if not melhor:
            resumo.append(f"{y}: sem tabela comparável na es")
            continue
        _, res, pv = melhor
        pv = 3 if y >= 1995 else 2
        dif = []
        for c, x in res.items():
            r = pac[c]
            if r["vitorias"] == "":
                continue
            p_es = pv * x["v"] + x["e"] + x["aj"]
            a = (int(r["jogos"] or 0), int(r["vitorias"]), int(r["empates"]), int(r["derrotas"]), int(r["gols_pro"]), int(r["gols_contra"]))
            b = (x["v"] + x["e"] + x["d"], x["v"], x["e"], x["d"], x["gp"], x["gc"])
            if a != b or (r["pontos"] and int(r["pontos"]) != p_es and 1931 > y or y > 1942):
                if a != b or (r["pontos"] and int(r["pontos"]) != p_es):
                    dif.append(f"   {c}: pacote J{a[0]} {a[1]}-{a[2]}-{a[3]} {a[4]}:{a[5]} pts {r['pontos']} (aj {r['ajuste_pontos']}) | es J{b[0]} {b[1]}-{b[2]}-{b[3]} {b[4]}:{b[5]} pts {p_es} (aj {x['aj']})")
        resumo.append(f"{y}: {len(res)} clubes comparados, {len(dif)} diferentes")
        if dif:
            out.append(f"{y}:")
            out += dif
    (Path(__file__).parent / "tabelas_es_saida.txt").write_text("\n".join(resumo + [""] + out), encoding="utf-8")
    print("\n".join(resumo))


if __name__ == "__main__":
    main()
