"""FR: testa a regra do ponto de bônus 1973/74-1975/76 contra a classificacao_final do pacote."""
import csv, sys
from collections import defaultdict
P = "data/coleta/fra-1/pacote/"
jogos = list(csv.DictReader(open(P + "partidas.csv", encoding="utf-8")))
cf = list(csv.DictReader(open(P + "classificacao_final.csv", encoding="utf-8")))
for T in ("1973/74", "1974/75", "1975/76"):
    g3 = defaultdict(int); m3 = defaultdict(int); v3 = defaultdict(int)
    for j in jogos:
        if j["temporada"] != T: continue
        gm, gv = int(j["gols_mandante"]), int(j["gols_visitante"])
        for c, a, b in ((j["mandante"], gm, gv), (j["visitante"], gv, gm)):
            if a >= 3: g3[c] += 1
            if a - b >= 3: m3[c] += 1
            if a >= 3 and a > b: v3[c] += 1
    print(T)
    for x in cf:
        if x["temporada"] != T: continue
        c = x["clube"]; aj = int(x["ajuste_pontos"])
        wiki_adj = aj + g3[c]
        print(f"  {x['posicao']:>2} {c:25} pts {x['pontos']:>3} V{x['vitorias']} E{x['empates']} ajuste_pacote {aj:+d}  wiki_adj={wiki_adj}  3+gols={g3[c]} vit3+dif={m3[c]} vit_com3+gols={v3[c]}")
