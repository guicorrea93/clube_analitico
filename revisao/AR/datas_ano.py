"""Datas com ano provavelmente errado no arg-1 (só leitura).
Regra do ano esperado pelo mês: temporada 'AAAA/BB' e Apertura/Inicial/Clausura/Final seguem o calendário europeu;
temporada de ano fechado: março a dezembro = ano_inicio; janeiro e fevereiro = ano_inicio ou o seguinte (ambíguo, não conta).
Também lista o mesmo clube em 2 jogos na mesma data em edições diferentes do arg-1."""
import sqlite3, re, sys
from collections import defaultdict, Counter
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
eds = c.execute("""select e.edicao_id, e.temporada, e.ano_inicio, e.ano_fim from edicao e join competicao co using(competicao_id)
                   where co.slug='arg-1' order by e.ano_inicio, e.edicao_id""").fetchall()
nome = dict(c.execute("select clube_id, nome from clube"))
tot = 0; linhas = []; exemplos = {}; lista = []
for eid, temp, a0, a1 in eds:
    js = c.execute("select partida_id, data, mandante_id, visitante_id, rodada, fonte_id from partida where edicao_id=? and data is not null", (eid,)).fetchall()
    ruins = []
    for pid, d, m, v, r, fid in js:
        y, mo = int(d[:4]), int(d[5:7])
        if "/" in temp and not re.search(r"Apertura|Inicial|Clausura|Final|Campeonato", temp):
            esp = {a0} if mo >= 8 else ({a0, a0 + 1} if mo == 7 else {a0 + 1})
        elif "/" in temp and re.search(r"Apertura|Inicial", temp):
            esp = {a0} if mo >= 6 else {a0 + 1}
        elif "/" in temp:
            esp = {a0 + 1}
        elif temp == "1982 Metropolitano":
            esp = {a0} if mo >= 7 else {a0 + 1}
        else:
            esp = {a0} if mo >= 3 else {a0, a0 + 1}
        if y not in esp:
            ruins.append((d, nome[m], nome[v], r, fid, sorted(esp))); lista.append(f"{temp}	{d}	{nome[m]} x {nome[v]}	rodada {r}	{fid}	ano esperado {sorted(esp)}")
    if ruins:
        tot += len(ruins)
        linhas.append(f"{temp}\t{len(ruins)} de {len(js)}\tex.: {ruins[0][0]} {ruins[0][1]} x {ruins[0][2]} (rodada {ruins[0][3]}, {ruins[0][4]}; ano esperado {ruins[0][5]})")
print("\n".join(linhas)); print("TOTAL", tot)
# 1922 Amateurs e 1923 Asociación: as datas do ano seguinte caem em domingo como estão (prova do dia da semana): não são erro
OK = ("1922 Amateurs", "1923 Asociación")
lista = [l for l in lista if not l.startswith(OK)]
print("TOTAL sem 1922 Amateurs e 1923 Asociación (datas certas pelo dia da semana):", len(lista))
open("revisao/AR/datas_ano_lista.txt", "w", encoding="utf-8").write("\n".join(lista) + "\n")
# mesmo clube, mesma data, edições diferentes
x = defaultdict(set)
for eid, temp, a0, a1 in eds:
    for d, m, v, re_ in c.execute("select data, mandante_id, visitante_id, coalesce(resultado_especial,'') from partida where edicao_id=? and data is not null", (eid,)):
        if re_ in ("wo", "abd", "n/p"): continue
        x[(d, m)].add(temp); x[(d, v)].add(temp)
cruz = Counter()
ex = {}
for (d, cl), ts in x.items():
    if len(ts) > 1:
        k = " + ".join(sorted(ts)); cruz[k] += 1; ex.setdefault(k, f"{nome[cl]} em {d}")
print("\nMesmo clube, mesma data, duas edições:")
for k, n in sorted(cruz.items()): print(f"{k}\t{n}\tex.: {ex[k]}")
