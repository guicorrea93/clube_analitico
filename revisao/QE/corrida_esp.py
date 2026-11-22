"""esp-1: classificação rodada a rodada do pacote x regra espanhola (confronto direto recursivo, só com os jogos entre
os empatados todos disputados; senão saldo e gols pró). Saída: revisao/QE/corrida_esp_saida.txt.
Uso: python -I revisao/QE/corrida_esp.py"""
import sys
from collections import defaultdict
sys.path.insert(0, "revisao/QE")
import desempate_esp as d  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
ed = {e["temporada"]: e for e in d.ler("edicoes.csv")}
part = defaultdict(list)
for j in d.ler("partidas.csv"):
    if j["fase"] == "Liga":
        part[j["temporada"]].append(j)
fin = defaultdict(list)
for r in d.ler("classificacao_final.csv"):
    fin[r["temporada"]].append(r)
rod = defaultdict(dict)
for r in d.ler("classificacao_rodada.csv"):
    rod[r["temporada"]][(int(r["rodada"]), r["clube"])] = int(r["posicao"])
linhas = []
tot = {"parcial": 0, "regra": 0}
lider = {"parcial": 0, "regra": 0}
temps = defaultdict(set)
for T in ed:
    pv = int(ed[T]["pontos_vitoria"])
    js = part[T]
    aj = {r["clube"]: int(r["ajuste_pontos"] or 0) for r in fin[T]}
    nr = 34 if T == "1986/87" else max(int(j["rodada"]) for j in js if j["rodada"])
    for r in range(1, nr + 1):
        ate = [j for j in js if j["rodada"] and int(j["rodada"]) <= r]
        t = d.tabela(ate, pv)
        for modo, so in (("parcial", False), ("regra", True)):
            o = d.ordenar_esp(t, aj, ate, pv, so_completo=so)
            for p, c in enumerate(o, 1):
                q = rod[T].get((r, c))
                if q != p:
                    tot[modo] += 1
                    temps[modo].add(T)
                    if p == 1 or q == 1:
                        lider[modo] += 1
                    if modo == "regra":
                        linhas.append(f"{T}\trodada {r}\t{c}\tpacote {q}º\tregra {p}º")
print("posições de rodada diferentes do pacote:")
print(" só a recursão (confronto com jogos parciais, como o pacote):", tot["parcial"], "em", len(temps["parcial"]), "temporadas; líder:", lider["parcial"])
print(" regra completa (confronto só com os jogos todos):", tot["regra"], "em", len(temps["regra"]), "temporadas; líder:", lider["regra"])
open("revisao/QE/corrida_esp_saida.txt", "w", encoding="utf-8").write("\n".join(linhas))
