"""Total de jogos por temporada (n*(n-1); 1986/87 = 306 + 90), datas fora da temporada, jogos sem data,
rodada com clube repetido ou faltando, gols com autor > placar."""
import sqlite3, sys, statistics
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
eds = c.execute("select edicao_id, temporada, ano_inicio, num_clubes from edicao join competicao using(competicao_id) where slug='esp-1' order by ano_inicio").fetchall()
for eid, t, a, n in eds:
    js = c.execute("select partida_id, fase_id, rodada, data, mandante_id, visitante_id, gols_mandante, gols_visitante from partida where edicao_id=?", (eid,)).fetchall()
    esperado = n * (n - 1) + (90 if t == "1986/87" else 0)
    clubes = {x for j in js for x in j[4:6]}
    if len(js) != esperado or len(clubes) != n: print(t, "jogos", len(js), "esperado", esperado, "clubes", len(clubes), n)
    sem = [j for j in js if not j[3]]
    if sem: print(t, "sem data:", len(sem))
    fora = [j for j in js if j[3] and not (f"{a}-07-01" <= j[3] <= f"{a+1}-07-31")]
    if fora: print(t, "data fora da temporada:", len(fora), fora[:2])
    porrod = defaultdict(list)
    for j in js: porrod[(j[1], j[2])].append(j)
    for (f, r), lst in porrod.items():
        cl = Counter(x for j in lst for x in j[4:6])
        if any(v > 1 for v in cl.values()): print(t, "rodada", r, "clube 2x na rodada", [k for k, v in cl.items() if v > 1])
    # pares repetidos (mesmo mandante x visitante 2x na mesma fase)
    pares = Counter((j[1], j[4], j[5]) for j in js)
    rep = [k for k, v in pares.items() if v > 1]
    if rep: print(t, "par mandante-visitante repetido na fase:", len(rep))
    # gols com autor x placar
    for pid, fm, fv, gm, gv in c.execute("""select p.partida_id, sum(g.clube_id=p.mandante_id), sum(g.clube_id=p.visitante_id), p.gols_mandante, p.gols_visitante
              from partida p join gol g using(partida_id) where p.edicao_id=? group by p.partida_id""", (eid,)):
        if fm > gm or fv > gv: print(t, "gols com autor > placar", pid, fm, fv, gm, gv)
tot = c.execute("select count(*) from partida join edicao using(edicao_id) join competicao using(competicao_id) where slug='esp-1'").fetchone()[0]
gols = c.execute("select count(*), sum(jogador is null or jogador='') from gol join partida using(partida_id) join edicao using(edicao_id) join competicao using(competicao_id) where slug='esp-1'").fetchone()
print("total jogos", tot, "gols com autor", gols)
# gols com autor < placar (cobertura) nas temporadas com ESPN
for t, j, comp, gp in c.execute("""select e.temporada, count(distinct p.partida_id),
     sum(case when (select count(*) from gol g where g.partida_id=p.partida_id)=p.gols_mandante+p.gols_visitante then 1 else 0 end),
     sum(p.gols_mandante+p.gols_visitante) from partida p join edicao e using(edicao_id) join competicao k using(competicao_id)
     where k.slug='esp-1' and e.ano_inicio>=2001 group by 1 order by 1"""):
    print(t, "jogos", j, "com todos os gols", comp, "gols", gp)
