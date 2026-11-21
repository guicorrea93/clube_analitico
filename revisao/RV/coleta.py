"""Olhada rápida nos achados da coleta (só para listar quais já aparecem corrigidos)."""
from comum import *
def q(sql, *a): return c.execute(sql, a).fetchall()
def cf(slug, temp, cond="1=1"):
    return q(f"""select cl.nome, cf.posicao, cf.ajuste_pontos, cf.situacao from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id)
               join competicao co using(competicao_id) where co.slug=? and e.temporada=? and {cond} order by posicao""", slug, temp)
print("SC-001/SD-001 edições 2026:", q("select co.slug, e.temporada from edicao e join competicao co using(competicao_id) where e.temporada='2026' and co.slug like 'bra-%'"))
for a in ("2009","2013","2016","2017","2018","2019","2020","2021"):
    print("SC-004", a, [x[0] for x in cf("bra-serie-c", a, "cf.situacao like '%rebaix%'")])
for a in ("1981","1988","1990","1999"):
    print("SC-005", a, [x[0] for x in cf("bra-serie-c", a, "cf.situacao like '%acesso%'")])
print("SC-011 2004 Atlético-BA:", [j[2:10] for j in jogos("bra-serie-c","2004",{"Atlético-BA"})][:3], [j[2:10] for j in jogos("bra-serie-c","2004",{"Atlético Sorocaba"})][:2])
print("SC-012 2003 Ituiutabana/Boa Esporte:", len(jogos("bra-serie-c","2003",{"Ituiutabana"})), len(jogos("bra-serie-c","2003",{"Boa Esporte"})))
print("SC-015 1995:", [j[5:10]+(j[13],) for j in jogos("bra-serie-c","1995",{"Itumbiara","Gama"})])
print("SC-017 ajustes C 2005-2007:", q("""select e.temporada, cl.nome, cf.ajuste_pontos from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-serie-c' and e.temporada in ('2005','2006','2007') and cf.ajuste_pontos<>0"""))
d, E = eds("bra-serie-c")
print("SC-023 2016 artof:", E["2016"]["artof"][:2], "SC-007 1988 pv:", E["1988"]["pv"])
print("SC-021 jogos 1995/1999/2011/2012:", [(a, E[a]["j"]) for a in ("1995","1999","2011","2012")])
print("SD-013 2014 W.O.:", [j[5:13] for j in jogos("bra-serie-d","2014") if j[12]])
print("SD-014 ajustes D:", q("""select e.temporada, cl.nome, cf.ajuste_pontos from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-serie-d' and cf.ajuste_pontos<>0 order by 1"""))
print("SD-017 2025 acesso:", [x[:2] for x in cf("bra-serie-d","2025","cf.situacao like '%acesso%'")], "2020:", [x[:2] for x in cf("bra-serie-d","2020","cf.situacao like '%acesso%'")])
print("SD-018 nomes com '- ':", q("select count(*) from artilheiro a join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-serie-d' and a.jogador like '-%'"))
print("SD-004/5/6/7 fases D 2016-2022:", q("""select e.temporada, f.nome, count(distinct p.grupo), count(*) from partida p join fase f using(fase_id) join edicao e on e.edicao_id=p.edicao_id join competicao co using(competicao_id) where co.slug='bra-serie-d' and e.temporada in ('2018','2020','2021','2022') group by 1,2 order by 1, min(p.data)"""))
print("SD-011 2013 semi:", [j[2:10] for j in jogos("bra-serie-d","2013",{"Botafogo-PB","Salgueiro"})])
print("SD-012 2016 final:", [j[2:10] for j in jogos("bra-serie-d","2016",{"CSA","Volta Redonda"})])
print("CB-004:", [j[5:10] for j in jogos("bra-copa-do-brasil","2014",{"Treze","Vasco"})], [j[5:10] for j in jogos("bra-copa-do-brasil","2015",{"Paysandu","Águia Negra"})], [j[5:10] for j in jogos("bra-copa-do-brasil","2015",{"Tupi","Ceará"})])
print("CB-006:", [j[2:10] for j in jogos("bra-copa-do-brasil","2015",{"Santos","Palmeiras"})], [j[2:10] for j in jogos("bra-copa-do-brasil","2016",{"Atlético-MG","Grêmio"})])
d, E = eds("bra-copa-do-brasil")
print("CB-007 jogos 1999/2007/2019/2021:", [(a, E[a]["j"]) for a in ("1999","2007","2019","2021")], "2021 Sergipe/CRB 1ª fase:", [j[2:10] for j in jogos("bra-copa-do-brasil","2021") if "Sergipe" in (j[6], j[9])][:3])
print("CB-008 jogos com pênaltis:", q("select count(*) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-copa-do-brasil' and penaltis_mandante is not null"))
print("CB-010:", [j[5:10] for j in jogos("bra-copa-do-brasil","2014") if j[2]=="Final"], [j[5:10] for j in jogos("bra-copa-do-brasil","1990",{"Goiás","Flamengo"})])
print("CB-011 artof 2007/2018/2019/2023:", [(a, E[a]["artof"][:2]) for a in ("2007","2018","2019","2023")])
print("CB-014 grupos 'Grupo NN':", q("select e.temporada, count(*) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-copa-do-brasil' and p.grupo like 'Grupo %' group by 1"))
print("CB-015 obs lixo:", q("select count(*) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='bra-copa-do-brasil' and p.observacao like '%ineligibl%'"))
for n in ("Atlético Tubarão","Tubarão","Operário-MS","Ariquemes","EC São Gabriel","São Gabriel","Goiatuba","Goiatuba EC","Operário-MT","CEOV Operário","Lagarto","Cabofriense","Foz do Iguaçu","Limoeiro","Joaçaba","Matsubara","Botafogo-DF","AA Araguaia","Imperatriz"):
    r = q("select clube_id, regiao, cidade from clube where nome=?", n)
    comps = q("select co.slug, group_concat(e.temporada) from classificacao_final cf join edicao e using(edicao_id) join competicao co using(competicao_id) where cf.clube_id=? and co.slug like 'bra-%' group by 1", r[0][0]) if r else None
    print("CL", n, r, comps)
print("CL-031 Matsubara nomes:", q("select nome, fonte, ano_inicio from clube_nome where clube_id=(select clube_id from clube where nome='Matsubara')"))
