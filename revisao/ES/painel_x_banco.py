"""Classificação do painel (EDS.tab) x classificacao_final do banco, todas as temporadas; pódio (ED) x banco."""
import json, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
s = open("painel/dados/esp-1.js", encoding="utf-8").read()
d = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
ed = {e["t"]: e for e in d["ED"]}
for e in d["EDS"]:
    t = e["t"]
    rows = c.execute("""select cl.nome,f.posicao,f.jogos,f.vitorias,f.empates,f.derrotas,f.gols_pro,f.gols_contra,f.ajuste_pontos
        from classificacao_final f join edicao x using(edicao_id) join competicao k using(competicao_id) join clube cl using(clube_id)
        where k.slug='esp-1' and x.temporada=? order by posicao""", (t,)).fetchall()
    b = {r[0]: list(r[1:]) for r in rows}
    for r in e["tab"]:
        if b.get(r[0]) != [*r[1:8], r[8] or 0]:
            print(t, r[0], "painel", r[1:], "banco", b.get(r[0]))
    top = [r[0] for r in rows[:3]]
    p = ed[t]
    if [p["campeao"], p["vice"], p["terceiro"]] != top: print(t, "pódio painel", p, "banco", top)
