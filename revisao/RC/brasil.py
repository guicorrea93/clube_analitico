"""Reconferência dos achados da coleta Brasil (SC, SD, CB, CL, TL-004): pacote x banco x site.
Uso (na raiz do projeto): python -I revisao/RC/brasil.py > SCRATCH/RC/brasil_saida.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
from collections import Counter

def pac_ed(slug, temp):
    return next((x for x in pac(slug, "edicoes") if x["temporada"] == temp), None)
def pac_cf(slug, temp):
    return [x for x in pac(slug, "classificacao_final") if x["temporada"] == temp]
def pos_pac(slug, temp, n=6):
    return [(x["posicao"], x["clube"], x["situacao"]) for x in pac_cf(slug, temp)[:n]]
def pos_db(slug, temp, n=6):
    return [(p, cl, s) for p, cl, *_, s in cf(slug, temp)[:n]]
def site_ed(slug, temp):
    return next((x for x in ed_lista(slug) if str(x["ano"]) == temp), None)
def site_tab(slug, temp, n=6):
    e = eds(slug).get(temp)
    return [r[:2] for r in e["tab"][:n]] if e else None
def H(t): print("\n=====", t)

S, D, CB = "bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"

H("SC-001 Série C 2026")
print("pacote:", pac_ed(S, "2026"), "\nbanco:", edicao(S, "2026"), "\nsite:", site_ed(S, "2026"))
print("acesso pacote:", [x["clube"] for x in pac_cf(S, "2026") if "acesso" in x["situacao"] or x["situacao"] in ("campeao", "vice")])
print("rebaixados pacote:", [x["clube"] for x in pac_cf(S, "2026") if "rebaix" in x["situacao"]])
print("site ac:", eds(S).get("2026", {}).get("ac"), "jogos:", eds(S).get("2026", {}).get("j"))

H("SC-002 / SC-003 vices e 3º")
for a in ["1992", "1999", "2001", "2002", "2003", "2005", "2006", "2007", "2008", "2009", "2011", "2020", "2023", "2024", "2025"]:
    se = site_ed(S, a)
    print(a, "pac:", pos_pac(S, a, 5), "| db:", [x[1] for x in pos_db(S, a, 5)], "| site:", se and (se["campeao"], se["vice"], se["terceiro"]))

H("SC-004 rebaixados")
for a in ["2009", "2013", "2016", "2017", "2018", "2019", "2020", "2021"]:
    print(a, "pac:", [x["clube"] for x in pac_cf(S, a) if "rebaix" in x["situacao"]], "| db:", [x[1] for x in cf(S, a, "cf.situacao like '%rebaix%'")])

H("SC-005 acesso")
for a in ["1981", "1988", "1990", "1992", "1999"]:
    print(a, "pac:", [(x["clube"], x["situacao"]) for x in pac_cf(S, a) if "acesso" in x["situacao"]], "| db:", [x[1] for x in cf(S, a, "cf.situacao like '%acesso%'")], "| site ac:", eds(S).get(a, {}).get("ac"))

H("SC-007 1988 pontos")
print("pac pv:", pac_ed(S, "1988")["pontos_vitoria"], "| db:", edicao(S, "1988")[5], "| site pv:", eds(S)["1988"]["pv"])
print("pac:", [(x["posicao"], x["clube"], x["pontos"]) for x in pac_cf(S, "1988")[:10]])
print("site tab:", [r[:2] + [r[-1]] for r in eds(S)["1988"]["tab"][:10]])
print("site tab ABC/Marcílio/Tiradentes:", [r for r in eds(S)["1988"]["tab"] if r[0] in ("ABC", "Marcílio Dias", "Tiradentes-PI")])

H("SC-008 1988 Ferroviária-SP x Desportiva-ES")
for cl in ("Ferroviária-SP", "Desportiva-ES"):
    print(cl, "pac:", len(pac_jogos(S, "1988", [cl])), "db:", len(jogos(S, "1988", [cl])))
print([pj(x) for x in pac_jogos(S, "1988", ["Ferroviária-SP"]) if x["fase"] != "Primeira fase"])

H("SC-009 / CL-001 2007 Imperatriz")
print("Imperatriz pac:", [pj(x) for x in pac_jogos(S, "2007", ["Imperatriz"]) if x["fase"] != "Primeira fase"])
print("Tuna x Tuna pac:", [pj(x) for x in pac_jogos(S, "2007") if x["mandante"] == x["visitante"]])
print("db Imperatriz:", len(jogos(S, "2007", ["Imperatriz"])), "Tuna:", len(jogos(S, "2007", ["Tuna Luso"])))
print("db cf:", [x[:4] + (x[8], x[9]) for x in cf(S, "2007") if x[1] in ("Imperatriz", "Tuna Luso")])

H("SC-010 2008 jogos")
print("pac:", len(pac_jogos(S, "2008")), "db:", len(jogos(S, "2008")), "site j:", eds(S)["2008"]["j"])
print([pj(x) for x in pac_jogos(S, "2008", ["Inter de Santa Maria", "Engenheiro Beltrão"])])
print([pj(x) for x in pac_jogos(S, "2008", ["Toledo", "Marcílio Dias"])])

H("SC-011 2004 Portuguesa Santista")
print([pj(x) for x in pac_jogos(S, "2004", ["Portuguesa Santista"]) if "Atl" in x["mandante"] + x["visitante"]])
print("db:", [x[4:9] for x in jogos(S, "2004", ["Portuguesa Santista"]) if "Atl" in x[5] + x[8]])

H("SC-012 2003 Ituiutaba")
for n in ("Ituiutabana", "Boa Esporte", "Ituiutaba"):
    print(n, len(pac_jogos(S, "2003", [n])), len(jogos(S, "2003", [n])))

H("SC-013 2011")
print("pac:", len(pac_jogos(S, "2011")), "db:", len(jogos(S, "2011")), "site j:", eds(S)["2011"]["j"])
print("pac pos:", pos_pac(S, "2011", 5))
print("Rio Branco-AC 2ª fase pac:", [pj(x) for x in pac_jogos(S, "2011", ["Rio Branco-AC"]) if x["fase"] != "Primeira fase"])

H("SC-014 placares")
for a, par in [("1988", ["Inter de Santa Maria", "Figueirense"]), ("1992", ["Rio Branco-MG", "São Bento"]), ("1992", ["Nacional-AM", "Ji-Paraná"]),
               ("1992", ["Nacional-AM", "Macapá"]), ("1992", ["Nacional-AM", "Auto Esporte"]), ("2003", ["Atlético Roraima", "Rio Branco-AC"])]:
    print(a, [pj(x) for x in pac_jogos(S, a, par)], "| db:", [x[4:9] for x in jogos(S, a, par)])

H("SC-015 1995 Itumbiara x Gama")
print([pj(x) + " obs=" + x["observacao"] for x in pac_jogos(S, "1995", ["Itumbiara", "Gama"])], "| db:", [x[4:9] + (x[11],) for x in jogos(S, "1995", ["Itumbiara", "Gama"])])

H("SC-016 placares só a Wikipédia diverge (amostra)")
for a, par in [("1981", ["Izabelense", "Manchete"]), ("1990", ["Estudantes", "Campinense"]), ("2008", ["Rio Branco-AC", "Fast-AM"]), ("2013", ["CRB", "Luverdense"])]:
    print(a, [pj(x) for x in pac_jogos(S, a, par)])

H("SC-017 punições")
for a in ("2005", "2006", "2007"):
    print(a, "pac:", [(x["clube"], x["ajuste_pontos"], x["pontos"]) for x in pac_cf(S, a) if x["ajuste_pontos"] not in ("", "0")],
          "| db:", [(x[1], x[9], x[8]) for x in cf(S, a, "cf.ajuste_pontos<>0")])

H("SC-019 fases")
for a in ("1992", "2003", "2020"):
    print(a, "pac fases:", [(x["ordem"], x["fase"], x["tipo"]) for x in pac(S, "fases") if x["temporada"] == a])
print("1992 Fluminense-BA x Matsubara:", [pj(x) for x in pac_jogos(S, "1992", ["Fluminense-BA", "Matsubara"])])
print("2020 Vila Nova x Remo:", [pj(x) for x in pac_jogos(S, "2020", ["Vila Nova-GO", "Remo"])])
print("fases em inglês (pacote C):", sorted({x["fase"] for x in pac(S, "partidas") if any(w in x["fase"].lower() for w in ("phase", "round", "stage", "group"))}))

H("SC-020 / TL-004 ida e volta no mesmo dia (pacote C, D, Copa)")
for slug in (S, D, CB):
    ps = pac(slug, "partidas"); n = Counter()
    k = Counter((x["temporada"], x["data"], frozenset((x["mandante"], x["visitante"]))) for x in ps if x["data"])
    rep = [kk for kk, v in k.items() if v > 1]
    print(slug, len(rep), sorted((t, d, tuple(sorted(cl))) for t, d, cl in rep)[:25])

H("SC-021 totais")
for a in ("1995", "1999", "2011", "2012"):
    print(a, "pac:", len(pac_jogos(S, a)), "site:", eds(S)[a]["j"])
for a in ("2001", "2002", "2008", "2011"):
    print(a, "gols site:", eds(S)[a]["g"])

H("SC-022 / SC-023 artilheiros")
print("1998:", [x for x in pac(S, "artilheiros") if x["temporada"] == "1998"], "| site artof:", eds(S)["1998"].get("artof"))
print("2016:", [x for x in pac(S, "artilheiros") if x["temporada"] == "2016"])
g = pac(S, "gols")
print("gols nomes:", Counter(x["jogador"] for x in g if x["jogador"] in ("Jonas Carioca", "Jones Carioca", "Assinzinho", "Assisinho", "Leandrao", "Leandrão", "Julio César", "Júlio César")))

H("SD-001 Série D 2026")
print("pacote:", pac_ed(D, "2026"), "\nbanco:", edicao(D, "2026"), "\nsite:", site_ed(D, "2026"))
print("acesso pac:", [x["clube"] for x in pac_cf(D, "2026") if x["situacao"] in ("campeao", "vice", "acesso") or "acesso" in x["situacao"]], "| clubes:", len(pac_cf(D, "2026")), "jogos:", len(pac_jogos(D, "2026")))
print("site ac:", eds(D).get("2026", {}).get("ac"), eds(D).get("2026", {}).get("j"))

H("SD-002 / SD-003 / SD-017")
for a in ("2020", "2021", "2025"):
    se = site_ed(D, a)
    print(a, "pac:", pos_pac(D, a, 6), "| db:", [x[1] for x in pos_db(D, a, 6)], "| site:", se and (se["campeao"], se["vice"], se["terceiro"]), "| site tab:", site_tab(D, a))
    print("   acesso pac:", [(x["posicao"], x["clube"]) for x in pac_cf(D, a) if "acesso" in x["situacao"] or x["situacao"] in ("campeao", "vice")])

H("SD-004..008 fases e grupos D")
for a in ("2011", "2013", "2016", "2017", "2018", "2020", "2021", "2022"):
    ps = pac_jogos(D, a)
    f = Counter((x["fase"], bool(x["grupo"])) for x in ps)
    ng = Counter(x["fase"] for x in ps if x["grupo"])
    gr = {x["fase"]: len({y["grupo"] for y in ps if y["fase"] == x["fase"] and y["grupo"]}) for x in ps}
    print(a, dict(f), "grupos:", gr)
print("2021 Campinense mata:", [pj(x) for x in pac_jogos(D, "2021", ["Campinense"]) if x["fase"] != "Primeira fase"][:8])
print("2013 final:", [pj(x) for x in pac_jogos(D, "2013", ["Juventude", "Botafogo-PB"])])
print("2011 final:", [pj(x) for x in pac_jogos(D, "2011", ["Tupi", "Santa Cruz"])])
print("fases D pac:", sorted({(x["temporada"], x["fase"]) for x in pac(D, "partidas")}, key=lambda t: t)[-60:])

H("SD-009 inglês e observações D")
print(sorted({x["fase"] for x in pac(D, "partidas") if any(w in x["fase"].lower() for w in ("phase", "round", "stage", "preliminary"))}))
obs = [x["observacao"] for x in pac(D, "partidas") if x["observacao"]]
print(len(obs), Counter(obs).most_common(15))
print([o for o in obs if any(w in o for w in ("Pen ", "Pro ", "played", "]"))][:10])

H("SD-010 2024 Princesa x Manaus")
print([pj(x) for x in pac_jogos(D, "2024", ["Princesa", "Manaus FC"])], "| site g 2024:", eds(D)["2024"]["g"], "| db:", [x[4:9] for x in jogos(D, "2024", ["Princesa", "Manaus FC"])])

H("SD-011 / SD-012 datas")
print("2013 semi:", [pj(x) for x in pac_jogos(D, "2013", ["Botafogo-PB", "Salgueiro"])])
print("2016 final:", [pj(x) for x in pac_jogos(D, "2016", ["CSA", "Volta Redonda"])], "| db:", [x[4:9] for x in jogos(D, "2016", ["CSA", "Volta Redonda"])])

H("SD-013 2014 W.O.")
print([pj(x) + " obs=" + x["observacao"] for x in pac_jogos(D, "2014") if x["resultado_especial"]])
print("site 2014 j/g:", eds(D)["2014"]["j"], eds(D)["2014"]["g"], "| db gols:", q("select sum(gols_mandante+gols_visitante), count(*) from partida where edicao_id=?", eid(D, "2014")))

H("SD-014..016 punições D")
for a in ("2009", "2010", "2012", "2013", "2014", "2015", "2017", "2019", "2025"):
    print(a, "pac:", [(x["posicao"], x["clube"], x["ajuste_pontos"], x["pontos"]) for x in pac_cf(D, a) if x["ajuste_pontos"] not in ("", "0")],
          "| db:", [(x[0], x[1], x[9], x[8]) for x in cf(D, a, "cf.ajuste_pontos<>0")])
print("2017 São Raimundo:", [(x["posicao"], x["clube"], x["pontos"]) for x in pac_cf(D, "2017") if "São Raimundo" in x["clube"]])
print("2025 Maricá/Maracanã:", [(x["posicao"], x["clube"], x["pontos"], x["ajuste_pontos"]) for x in pac_cf(D, "2025") if x["clube"].startswith("Mar")])

H("SD-018 nomes artilheiros D")
print([x["jogador"] for x in pac(D, "artilheiros") if x["jogador"].startswith("-")], q("select count(*) from artilheiro a join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and a.jogador like '-%'", D))

H("CB-001 / CB-002 vices e semifinalistas")
for a in ("1989", "1993", "1994", "1995", "1996", "1997", "2012", "2014", "2025"):
    se = site_ed(CB, a)
    print(a, "pac:", [(x["posicao"], x["clube"]) for x in pac_cf(CB, a)[:4]], "| site:", se and (se["campeao"], se["vice"], se["terceiro"]))
ruins = []
for e in pac(CB, "edicoes"):
    a = e["temporada"]
    semi = {x for j in pac_jogos(CB, a) if j["fase"] in ("Semifinal", "Final") for x in (j["mandante"], j["visitante"])}
    top4 = {x["clube"] for x in pac_cf(CB, a)[:4]}
    if semi != top4: ruins.append((a, sorted(semi - top4), sorted(top4 - semi)))
print("edições com semifinalistas fora do top 4 (pacote):", ruins)

H("CB-003 / CB-014 fases e grupos Copa")
fs = Counter((x["temporada"], x["fase"]) for x in pac(CB, "partidas"))
print("nomes de fase:", sorted({f for _, f in fs}))
print("finais com >2 jogos:", [(t, n) for (t, f), n in fs.items() if f == "Final" and n > 2])
print("jogos com grupo:", sum(1 for x in pac(CB, "partidas") if x["grupo"]), "| db Grupo NN:", q("select count(*) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and p.grupo is not null and p.grupo<>''", CB))
print("site 2019 disputa:", eds(CB)["2019"].get("disputa"))

H("CB-004 / CB-005 placares")
for a, par in [("2014", ["Treze", "Vasco"]), ("2015", ["Paysandu", "Águia Negra"]), ("2015", ["Tupi", "Ceará"]), ("1990", ["Santa Cruz", "América-RN"]),
               ("1993", ["4 de Julho", "Palmeiras"]), ("1994", ["4 de Julho", "Palmeiras"]), ("2000", ["Fluminense", "Santa Cruz"]), ("2000", ["Rio Negro-AM", "Nacional-AM"]),
               ("2007", ["Baré", "América-RN"]), ("2013", ["ASA", "Flamengo"]), ("2014", ["América-RN", "Fluminense"]), ("1991", ["Remo", "Vitória"]), ("2002", ["São Raimundo", "América-RN"]),
               ("2002", ["São Raimundo-AM", "América-RN"])]:
    print(a, [pj(x) for x in pac_jogos(CB, a, par)], "| db:", [x[4:9] for x in jogos(CB, a, par)])

H("CB-006 / CB-010 finais")
for a, par in [("2015", ["Santos", "Palmeiras"]), ("2016", ["Atlético-MG", "Grêmio"]), ("2014", ["Atlético-MG", "Cruzeiro"]), ("1990", ["Goiás", "Flamengo"]), ("2017", ["Cruzeiro", "Flamengo"])]:
    print(a, [pj(x) for x in pac_jogos(CB, a, par)])

H("CB-007 jogos")
for a in ("1999", "2007", "2019", "2021"):
    print(a, "pac:", len(pac_jogos(CB, a)), "clubes:", len(pac_cf(CB, a)), "site j:", eds(CB)[a]["j"], "db:", len(jogos(CB, a)))
print("2007 Villa Nova:", [pj(x) for x in pac_jogos(CB, "2007", ["Villa Nova-MG"])])
print("2019 Aparecidense x Ponte:", [pj(x) for x in pac_jogos(CB, "2019", ["Aparecidense", "Ponte Preta"])])
print("2021 Cuiabá 1ª fase:", [pj(x) for x in pac_jogos(CB, "2021", ["Cuiabá"])][:3])
print("1999 Santa Cruz x Náutico:", [pj(x) for x in pac_jogos(CB, "1999", ["Santa Cruz", "Náutico"])])

H("CB-008 pênaltis")
pp = [x for x in pac(CB, "partidas") if x["penaltis_mandante"]]
print("com pênaltis:", len(pp), "| obs com 'pen':", sum(1 for x in pac(CB, "partidas") if "pen" in x["observacao"].lower() and not x["penaltis_mandante"]))
print("2021 CRB x Palmeiras:", [pj(x) for x in pac_jogos(CB, "2021", ["CRB", "Palmeiras"])])
print("por ano:", sorted(Counter(x["temporada"] for x in pp).items()))

H("CB-011 artilheiros Copa")
for a in ("2007", "2018", "2019", "2023", "1989"):
    print(a, [(x["jogador"], x["clube"], x["gols"]) for x in pac(CB, "artilheiros") if x["temporada"] == a], "| site artof:", eds(CB)[a].get("artof"))
print("maiúsculas:", [x["jogador"] for x in pac(CB, "artilheiros") if x["jogador"].isupper()])

H("CB-015 observações Copa")
ob = [x["observacao"] for x in pac(CB, "partidas") if x["observacao"]]
print(len(ob), [o for o in ob if "ineligib" in o or "lost" in o or any(m in o for m in ("Feb ", "Mar ", "Apr "))][:10])
print(Counter(ob).most_common(10))

H("CL-002..012 cadastros nos pacotes e no banco")
def onde(nome):
    r = q("select clube_id, regiao, cidade from clube where nome=?", nome)
    if not r: return "não existe no banco"
    return r, q("""select co.slug, group_concat(distinct e.temporada) from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
                   where ? in (p.mandante_id, p.visitante_id) group by 1""", r[0][0])
for n in ("Tubarão", "Tubarão FC", "Atlético Tubarão", "Operário-MS", "CEOV Operário", "Operário-MT", "EC Operário-MT", "Ariquemes", "SE Ariquemes",
          "EC São Gabriel", "São Gabriel", "Goiatuba", "Goiatuba EC", "Lagarto", "Lagarto EC", "Cabofriense", "AA Cabofriense",
          "Foz do Iguaçu", "Foz do Iguaçu EC", "Limoeiro", "EC Limoeiro", "Joaçaba", "Joaçaba EC", "São Borja", "SE São Borja",
          "Desportiva Guarabira", "Guarabira EC", "Matsubara", "Botafogo-DF", "AA Araguaia", "Alegrense"):
    print(n, "|", onde(n))
print("Copa 2007 Operário x Palmeiras:", [pj(x) for x in pac_jogos(CB, "2007", ["Palmeiras"]) if "Oper" in x["mandante"] + x["visitante"]])
print("CL-031 Matsubara pacote:", [x["nomes_fonte"] for x in pac(S, "clubes") if x["clube"] == "Matsubara"])
print("CL-028 pacote:", [(x["clube"], x["regiao"], x["cidade"]) for x in pac(S, "clubes") + pac(D, "clubes") if x["clube"] in ("Botafogo-DF", "AA Araguaia", "Alegrense", "Vitória das Tabocas", "Serrano-BA", "Guarani-MG")])
print("CL-028 grafias:", sorted({x["cidade"] for x in pac(S, "clubes") + pac(D, "clubes") + pac(CB, "clubes") if any(w in x["cidade"] for w in (" De ", "Divinopolis", " - "))}))
