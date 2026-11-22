"""Efeito de tirar da classificação os jogos que o Futebol Nacional marca como cancelados (clube que abandonou o
campeonato; fn_diferencas.csv, tipo 'cancelado no FN') e de somar as vitórias por W.O. que só ele tem (placar 'WO').
Usa a regra do modo 3 de sim_ordem.py. Saída: revisao/QS/sim_cancelados_saida.txt.
Uso (da raiz): python -I -X utf8 revisao/QS/sim_cancelados.py"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import sim_ordem as S  # noqa: E402


def main():
    eds = {e["temporada"]: e for e in S.ler("edicoes.csv")}
    part = defaultdict(list)
    for p in S.ler("partidas.csv"):
        part[p["temporada"]].append(p)
    canc = defaultdict(set)
    for x in csv.DictReader(open(AQUI / "fn_diferencas.csv", encoding="utf-8")):
        if x["tipo"] == "cancelado no FN" and x["data_pacote"]:
            canc[x["temporada"]].add((x["data_pacote"], x["jogo_pacote"]))
    L = json.load(open(S.RAIZ / "revisao" / "SP" / "listas_campeoes.json", encoding="utf-8"))
    fonte = defaultdict(lambda: {"vice": set(), "terc": set()})
    for lado in ("en", "pt"):
        for x in L[lado]:
            k = (x["ano"], {"LFP": "LPF"}.get(x["liga"], x["liga"]))
            if x.get("vice") not in (None, "", "—", "–"):
                fonte[k]["vice"].add(S.norm(x["vice"]))
            if lado == "pt" and x.get("terceiro") not in (None, "", "—", "–"):
                fonte[k]["terc"].add(S.norm(x["terceiro"]))
    out = []
    for t in sorted(canc):
        e = eds[t]
        ano = int(t[:4]); liga = t.split(" ")[1] if " " in t else ""
        f = fonte.get((ano, liga)) or next((v for (a, l), v in fonte.items() if a == ano), {"vice": set(), "terc": set()})
        chave = lambda p: (p["data"], f"{p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']}")
        ps = [dict(p, fase=S.fase_certa(t, p)) for p in part[t]]
        sem = [p for p in ps if chave(p) not in canc[t]]
        pv = int(e["pontos_vitoria"])
        antes, _ = S.classificar(ps, e["campeao"], pv, S.ORDEM_NOVO, vice_grupo_final=True, pts_fase_final=True)
        depois, _ = S.classificar(sem, e["campeao"], pv, S.ORDEM_NOVO, vice_grupo_final=True, pts_fase_final=True)
        out.append(f"{t}\t{len(ps) - len(sem)} jogos cancelados tirados\tantes 2º {antes[1]} 3º {antes[2]}\t"
                   f"depois 2º {depois[1]} 3º {depois[2]}\tfonte vice {sorted(f['vice'])} 3º {sorted(f['terc'])}")
    (AQUI / "sim_cancelados_saida.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
