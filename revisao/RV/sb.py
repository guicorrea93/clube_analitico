from comum import *
S="bra-serie-b"
d, E = eds(S)
ED = {x["ano"]: x for x in d["ED"]}
for a in (1999, 2001, 2004, 2009): print("SB-001..5", a, ED[a]["campeao"], ED[a]["vice"], ED[a]["terceiro"], [r[:2] for r in E[str(a)]["tab"][:4]])
print("SB-003 2001", [r[:2] for r in E["2001"]["tab"][8:]])
print("SB-005 2009", [r for r in E["2009"]["tab"] if r[1] in (15,16,17,18)])
print("SB-002 jogo", jogos(S,"2001",{"Figueirense","Caxias"}))
# SB-006 duplicados
for a,cl in (("1971",{"Remo","Villa Nova-MG"}),("1981",{"Guarani","Anapolina"}),("1990",{"Athletico-PR","Sport"}),("1992",{"Paraná","Vitória"}),("1994",{"Desportiva-ES","Americano-RJ"})):
    js_=jogos(S,a,cl); print("SB-006",a,len(js_),[(j[2],j[5],j[6],j[7],j[8],j[9]) for j in js_])
print("SB-006 1971 tot", E["1971"]["j"], E["1971"]["g"])
for a,cl,nm in (("1998",{"Volta Redonda","Santa Cruz"},"SB-007"),("1994",{"Desportiva-ES","CRB"},"SB-008"),("2006",{"Ituano","Vila Nova-GO"},"SB-009"),("2008",{"Fortaleza","Criciúma"},"SB-010")):
    print(nm,a,[(j[2],j[5],j[6],j[7],j[8],j[9],j[12],j[13]) for j in jogos(S,a,cl)])
print("SB-007 tab", [r for r in E["1998"]["tab"] if r[0] in ("Santa Cruz","Volta Redonda")])
print("SB-009 tab", [r for r in E["2006"]["tab"] if r[0] in ("Ituano","Vila Nova-GO")], E["2006"]["g"])
print("SB-010 tab", [r for r in E["2008"]["tab"] if r[0] in ("Fortaleza","Criciúma")])
# SB-011 gols contra 2013
q="""select m.nome, p.gols_mandante, p.gols_visitante, v.nome, p.partida_id,
 (select count(*) from gol g where g.partida_id=p.partida_id and g.clube_id=p.mandante_id),
 (select count(*) from gol g where g.partida_id=p.partida_id and g.clube_id=p.visitante_id)
 from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
 where co.slug=? and e.temporada='2013' and ((m.nome='Joinville' and v.nome='Bragantino') or (m.nome='ABC' and v.nome='Paysandu') or (m.nome='Palmeiras' and v.nome='Paysandu') or (m.nome='América-RN' and v.nome='Oeste'))"""
print([r[1] for r in c.execute("pragma table_info(gol)")])
for r in c.execute(q,(S,)): print("SB-011",r)
# gols com autor vs placar em toda a Série B
q2="""select e.temporada, count(*) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
 where co.slug=? and exists(select 1 from gol g where g.partida_id=p.partida_id) and (
 (select count(*) from gol g where g.partida_id=p.partida_id and g.clube_id=p.mandante_id) > p.gols_mandante or
 (select count(*) from gol g where g.partida_id=p.partida_id and g.clube_id=p.visitante_id) > p.gols_visitante) group by 1"""
print("SB-011 lados que passam do placar:", c.execute(q2,(S,)).fetchall())
for a in ("1999","2002","2003","2004","2005","2006","2016","1971","1980","1972","2009","1988","1989","1990"):
    e=E[a]; print("SB-012/13",a,"artof",e["artof"][:2],"art",e["art"][:1],"cob",e["cob"])
print("SB-013 banco", c.execute("""select e.temporada, a.jogador, a.gols from artilheiro a join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and e.temporada in ('1971','1988','1989','1990','2004','2016')""",(S,)).fetchall())
for a,cl in (("2014","América-MG"),("2020","Cruzeiro"),("2021","Brusque"),("2006","Guarani"),("2007","Marília"),("2011","Salgueiro")):
    print("SB-014/16",a,[r for r in E[a]["tab"] if r[0]==cl])
print("SB-015 banco", c.execute("""select e.temporada, cl.nome, cf.vitorias, cf.empates, cf.derrotas, cf.gols_pro, cf.gols_contra, cf.pontos, cf.ajuste_pontos from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and ((e.temporada='2007' and cl.nome='Ituano') or (e.temporada='2008' and cl.nome='Juventude') or (e.temporada='2009' and cl.nome='Duque de Caxias') or (e.temporada='2021' and cl.nome='Brusque'))""",(S,)).fetchall())
print("SB-016 2021 tab", [r[:2] for r in E["2021"]["tab"][10:15]])
for a in ("1985","1999","2001","2002","1988","2004"): print("SB-018",a,E[a]["disputa"])
print("SB-020", [(a,[r[:2] for r in E[a]["tab"] if r[0] in ("Guaratinguetá","Americana")]) for a in ("2010","2011","2012","2013")])
print("SB-020 PART", d["PART"].get("Guaratinguetá"), "Americana" in d["PART"])
