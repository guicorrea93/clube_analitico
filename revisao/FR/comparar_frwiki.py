"""FR: compara o pacote fra-1 com a Wikipédia fr (tabela final, rebaixados e grade de resultados, temporada a temporada).
Uso (na raiz): python -I -X utf8 revisao/FR/comparar_frwiki.py > SCRATCH/FR/comparar_frwiki.txt"""
import csv, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frwiki as FW
CL = FW.CL
P = os.path.join(FW.RAIZ, "data", "coleta", "fra-1", "pacote")


def ler(n):
    return list(csv.DictReader(open(os.path.join(P, n), encoding="utf-8")))


J, CF, ED = ler("partidas.csv"), ler("classificacao_final.csv"), ler("edicoes.csv")
# nome de exibição -> chave do cadastro
EXIB = {v[0]: k for k, v in CL.CLUBES.items()}
jog = defaultdict(dict)
for j in J:
    jog[j["temporada"]][(EXIB[j["mandante"]], EXIB[j["visitante"]], j["fase"])] = j
cf = defaultdict(list)
for x in CF:
    cf[x["temporada"]].append(x)

tot = defaultdict(int)
sem_pagina, sem_tabela, sem_grade = [], [], []
for e in ED:
    T = e["temporada"]
    a = int(T[:4])
    w = FW.pagina(a)
    if w is None:
        sem_pagina.append(T)
        continue
    url = f"https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_{a}-{a + 1}"
    tabs = FW.tabelas(w, a)
    nosso = sorted(cf[T], key=lambda x: int(x["posicao"]))
    print(f"\n=== {T}  ({url})")
    # ---- tabela: a maior tabela cujos clubes batem com os nossos
    clubes_nossos = {EXIB[x["clube"]] for x in nosso}
    cand = [t for t in tabs if {x["clube"] for x in t} <= clubes_nossos and len(t) >= 8]
    if T == "1932/33":
        cand = cand[:2]
    else:
        cand = [t for t in cand if len(t) == len(nosso)][:1]
    if not cand:
        sem_tabela.append(T)
        print("  sem tabela legível;", [len(t) for t in tabs], [x["cel"] for t in tabs for x in t if x["clube"] is None][:5])
    nos = {EXIB[x["clube"]]: x for x in nosso}
    if T != "1932/33" and cand:
        t = cand[0]
        tot["tabelas"] += 1
        for x in t:
            n = nos[x["clube"]]
            tot["linhas"] += 1
            a_ = [x["pos"], x["pts"], x["j"], x["v"], x["e"], x["d"], x["gp"], x["gc"]]
            b_ = [int(n[k]) for k in ("posicao", "pontos", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")]
            if a_ != b_:
                tot["linhas_dif"] += 1
                print(f"  TABELA {CL.exibicao(x['clube'])}: frwiki pos/pts/J/V/E/D/GP/GC {a_} | pacote {b_}"
                      + (f" | bonus fr {x['bonus']}" if x["bonus"] is not None else "") + (f" | pen {x['pen']}" if x["pen"] else ""))
            if x["pen"]:
                print(f"  PENALIDADE frwiki {CL.exibicao(x['clube'])}: {x['pen']!r}; pacote ajuste {n['ajuste_pontos']}")
        reb_fr = {x["clube"] for x in t if x["relegue"]}
        reb_nos = {EXIB[x["clube"]] for x in nosso if x["situacao"] == "rebaixado"}
        if reb_fr != reb_nos:
            print(f"  REBAIXADOS frwiki {sorted(CL.exibicao(c) for c in reb_fr)} | pacote {sorted(CL.exibicao(c) for c in reb_nos)}")
            tot["reb_dif"] += 1
        camp = e["campeao"]
        if camp and EXIB[camp] != t[0]["clube"]:
            print(f"  CAMPEÃO frwiki {CL.exibicao(t[0]['clube'])} | pacote {camp}")
    elif T == "1932/33":
        for t in cand:
            reb = [CL.exibicao(x["clube"]) for x in t if x["relegue"]]
            print("  grupo:", [(x["pos"], CL.exibicao(x["clube"]), x["pts"], x["j"], x["v"], x["e"], x["d"], x["gp"], x["gc"]) for x in t])
            print("  rebaixados frwiki no grupo:", reb)
        print("  pacote rebaixados:", [x["clube"] for x in nosso if x["situacao"] == "rebaixado"])
    # ---- grade
    gs = FW.grades(w, a)
    if not gs:
        sem_grade.append(T)
        continue
    for clubes, placares in gs:
        if None in clubes:
            print("  grade com clube sem cadastro:", clubes)
            continue
        for i, m in enumerate(clubes):
            for k, s in enumerate(placares[i][:len(clubes)]):
                if k == i:
                    continue
                v = clubes[k]
                mm = re.match(r"^(\d+)\s*[-–]\s*(\d+)", s)
                fase = "Grupos" if T == "1932/33" else "Liga"
                jj = jog[T].get((m, v, fase))
                if not mm:
                    if s and s not in ("XXX", "—", "-", "x"):
                        print(f"  GRADE célula sem placar {CL.exibicao(m)} x {CL.exibicao(v)}: {s!r}"
                              + (f" | pacote {jj['gols_mandante']}-{jj['gols_visitante']}" if jj else ""))
                    continue
                tot["jogos"] += 1
                tot["jogos_" + T[:3] + "0s"] += 1
                if jj is None:
                    print(f"  GRADE jogo sem par no pacote: {CL.exibicao(m)} {s} {CL.exibicao(v)}")
                    tot["jogos_sem_par"] += 1
                    continue
                g = (int(mm.group(1)), int(mm.group(2)))
                if g != (int(jj["gols_mandante"]), int(jj["gols_visitante"])):
                    tot["jogos_dif"] += 1
                    tot["dif_" + T[:3] + "0s"] += 1
                    inv = jog[T].get((v, m, fase))
                    print(f"  PLACAR {CL.exibicao(m)} x {CL.exibicao(v)} ({jj['data']}): frwiki {g[0]}-{g[1]} | pacote "
                          f"{jj['gols_mandante']}-{jj['gols_visitante']}"
                          + (f" | volta no pacote {inv['gols_mandante']}-{inv['gols_visitante']} ({inv['data']})" if inv else "")
                          + (f" | obs {jj['observacao']}" if jj["observacao"] else ""))
print("\nRESUMO", dict(tot))
print("sem página:", sem_pagina)
print("sem tabela legível:", sem_tabela)
print("sem grade:", sem_grade)
