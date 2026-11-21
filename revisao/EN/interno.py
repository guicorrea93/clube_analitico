"""Conferências internas do eng-1 no banco (só leitura): jogos, tabela x jogos, ordem, gols com autor, datas."""
import sys, pathlib
from collections import defaultdict, Counter
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas
c = banco()
nm = dict(c.execute("select clube_id, nome from clube"))
tot = 0
for eid, t, ai, af in temporadas(c):
    pv, camp, vice, ncl = c.execute("select pontos_vitoria, campeao_id, vice_id, num_clubes from edicao where edicao_id=?", (eid,)).fetchone()
    js = c.execute("select partida_id, data, mandante_id, visitante_id, gols_mandante, gols_visitante, rodada, coalesce(resultado_especial,'') from partida where edicao_id=?", (eid,)).fetchall()
    tot += len(js)
    clubes = {x for j in js for x in (j[2], j[3])}
    n = len(clubes)
    msgs = []
    if len(js) != n * (n - 1): msgs.append(f"jogos {len(js)} != {n}x{n-1}")
    if ncl != n: msgs.append(f"num_clubes {ncl} != {n}")
    par = Counter((j[2], j[3]) for j in js)
    rep = [k for k, v in par.items() if v > 1]
    if rep: msgs.append(f"confronto repetido {[(nm[a], nm[b]) for a, b in rep]}")
    sem = [j for j in js if j[4] is None]
    if sem: msgs.append(f"{len(sem)} jogos sem placar")
    esp = [j for j in js if j[7]]
    if esp: msgs.append(f"resultado especial {[(nm[j[2]], nm[j[3]], j[7]) for j in esp]}")
    semd = [j for j in js if not j[1]]
    if semd: msgs.append(f"{len(semd)} sem data")
    fora = [j for j in js if j[1] and not (f"{ai}-07-01" <= j[1] <= f"{ai+1}-07-31")]
    if fora: msgs.append(f"data fora da temporada {[(nm[j[2]], nm[j[3]], j[1]) for j in fora][:3]}")
    semr = [j for j in js if j[6] is None]
    if semr: msgs.append(f"{len(semr)} sem rodada")
    # tabela calculada
    tb = defaultdict(lambda: [0] * 7)
    for _, d, m, v, gm, gv, *_ in js:
        if gm is None: continue
        for x, gp, gc in ((m, gm, gv), (v, gv, gm)):
            r = tb[x]; r[0] += 1; r[4] += gp; r[5] += gc
            if gp > gc: r[1] += 1; r[6] += pv
            elif gp == gc: r[2] += 1; r[6] += 1
            else: r[3] += 1
    cf = c.execute("select clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, coalesce(ajuste_pontos,0), situacao from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
    for cid, pos, J, V, E, D, GP, GC, P, aj, sit in cf:
        calc = tb[cid][:6] + [tb[cid][6] + aj]
        if [J, V, E, D, GP, GC, P] != calc:
            msgs.append(f"classif x jogos {nm[cid]} banco {[J,V,E,D,GP,GC,P]} calc {calc}")
    if len(cf) != n: msgs.append(f"classif com {len(cf)} clubes")
    ps = [r[1] for r in cf]
    if sorted(ps) != list(range(1, n + 1)): msgs.append(f"posições {ps}")
    # ordem: pontos, depois média (até 1975/76) ou saldo, depois gols pró
    def chave(r):
        P, GP, GC = r[8], r[6], r[7]
        if ai <= 1975: return (P, GP / GC if GC else 99, GP)
        return (P, GP - GC, GP)
    for a, b in zip(cf, cf[1:]):
        if chave(a) < chave(b):
            msgs.append(f"ordem: {nm[a[0]]} ({a[1]}º {chave(a)}) acima de {nm[b[0]]} ({b[1]}º {chave(b)})")
    if cf and cf[0][0] != camp: msgs.append(f"campeão {nm.get(camp)} não é o 1º {nm[cf[0][0]]}")
    if len(cf) > 1 and cf[1][0] != vice: msgs.append(f"vice {nm.get(vice)} não é o 2º {nm[cf[1][0]]}")
    # gols com autor
    g = c.execute("""select p.partida_id, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, gl.clube_id, count(*)
                     from gol gl join partida p using(partida_id) where p.edicao_id=? group by 1, 6""", (eid,)).fetchall()
    excede = []
    porj = defaultdict(dict)
    for pid, m, v, gm, gv, cl, k in g:
        porj[pid][cl] = k
        if (cl == m and k > gm) or (cl == v and k > gv) or cl not in (m, v):
            excede.append((nm[m], nm[v], gm, gv, nm.get(cl), k))
    if excede: msgs.append(f"gols com autor > placar em {len(excede)}: {excede[:5]}")
    ngol = sum(k for _, _, _, _, _, _, k in g)
    gplac = sum((j[4] or 0) + (j[5] or 0) for j in js)
    parc = sum(1 for pid, d in porj.items() if 0 < sum(d.values()))
    reb = [nm[r[0]] for r in cf if r[10] == 'rebaixado']
    print(f"{t}\t{n} clubes\t{len(js)} jogos\t{gplac} gols\t{ngol} c/autor\trebaixados={reb}")
    for m in msgs: print("   !", m)
print("TOTAL jogos", tot)
