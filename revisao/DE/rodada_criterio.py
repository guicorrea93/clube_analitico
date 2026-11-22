"""Classificação rodada a rodada do pacote x a calculada com o critério oficial da DFB de cada época:
até 1968/69 pontos e quociente de gols (Torquotient); de 1969/70 em diante pontos, saldo, gols pró (confronto direto
só depois disso). Conta as posições diferentes por temporada.
Uso: python -I revisao/DE/rodada_criterio.py > revisao/DE/rodada_criterio_saida.txt"""
import csv, sys, pathlib
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
PAC = pathlib.Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
fa = {x["temporada"]: x["criterio"] for x in csv.DictReader(open(PAC / "fases.csv", encoding="utf-8"))}
cr = defaultdict(lambda: defaultdict(list))
for x in csv.DictReader(open(PAC / "classificacao_rodada.csv", encoding="utf-8")):
    cr[x["temporada"]][int(x["rodada"])].append(x)
tot = 0
for t in sorted(cr):
    a = int(t[:4]); dif = []; n = 0
    for r, linhas in sorted(cr[t].items()):
        def k(x):
            p, gp, gc = int(x["pontos"]), int(x["gols_pro"]), int(x["gols_contra"])
            if a <= 1968:
                return (-p, -(gp / gc if gc else 99))
            return (-p, -(gp - gc), -gp)
        certo = sorted(linhas, key=lambda x: (k(x), int(x["posicao"])))
        # posição oficial: empate total em todos os critérios divide a posição; aqui conta só quem fica em outra posição
        for i, x in enumerate(certo, 1):
            n += 1
            if int(x["posicao"]) != i and k(x) != k(certo[int(x["posicao"]) - 1]):
                dif.append((r, x["clube"], int(x["posicao"]), i))
    tot += len(dif)
    if dif:
        print(f"{t} ({fa[t]}): {len(dif)} de {n} posições diferentes; ex.: " +
              "; ".join(f"rodada {r} {c} pacote {p}º, critério oficial {i}º" for r, c, p, i in dif[:3]))
print("total", tot)
