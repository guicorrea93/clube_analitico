"""Reconferência dos achados da coleta Europa (EN, ES): pacote x banco x site.
Uso: python -I revisao/RC/europa.py > SCRATCH/RC/europa_saida.txt"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
from collections import Counter, defaultdict
def H(t): print("\n=====", t)
E, S = "eng-1", "esp-1"

H("EN-001 2025/26")
ed = [x for x in pac(E, "edicoes") if x["temporada"] == "2025/26"]
print("pacote:", ed, "| edições:", len(pac(E, "edicoes")), "jogos:", len(pac(E, "partidas")))
print("rebaixados:", [x["clube"] for x in pac(E, "classificacao_final") if x["temporada"] == "2025/26" and "rebaix" in x["situacao"]])
print("artilheiro:", [x for x in pac(E, "artilheiros") if x["temporada"] == "2025/26"])
print("banco:", edicao(E, "2025/26"), "| site:", [x for x in ed_lista(E) if x["ano"] == 2025], "| jogos site:", eds(E).get("2025/26", {}).get("j"))

H("EN-002 / EN-003 / EN-004 artilheiros")
for t in ("1937/38", "1889/90", "1905/06"):
    print(t, "pac:", [(x["jogador"], x["clube"], x["gols"]) for x in pac(E, "artilheiros") if x["temporada"] == t],
          "| db:", q("select jogador, gols from artilheiro where edicao_id=?", eid(E, t)), "| site artof:", eds(E)[t].get("artof"))

H("EN-005 datas (lista do 11v11)")
dif = []
for l in open("revisao/EN/datas_11v11_saida.txt", encoding="utf-8"):
    m = re.match(r"\s+DIF (.+?) x (.+?): banco (\S+) (\d+)-(\d+) \| 11v11 (\S+) (\d+)-(\d+)", l)
    if m: dif.append(m.groups())
ok = ruim = 0; ruins = []
pj = pac(E, "partidas")
idx = defaultdict(list)
for x in pj: idx[(x["mandante"], x["visitante"])].append(x)
for m_, v_, d_old, a, b, d_new, a2, b2 in dif:
    cands = [x for x in idx[(m_, v_)] if abs(int(x["data"][:4] or 0) - int(d_new[:4])) <= 1]
    hit = [x for x in cands if x["data"] == d_new]
    old = [x for x in cands if x["data"] == d_old]
    if hit and not old: ok += 1
    else: ruim += 1; ruins.append((m_, v_, d_old, d_new, [(x["data"], x["gols_mandante"], x["gols_visitante"]) for x in cands]))
print("linhas DIF:", len(dif), "corrigidas no pacote:", ok, "não:", ruim); [print("  ", r) for r in ruins]

H("EN-006 Wolverhampton x Everton 1888/89")
print([(x["data"], x["mandante"], x["gols_mandante"], x["gols_visitante"], x["visitante"]) for x in pj if x["temporada"] == "1888/89" and x["mandante"] == "Wolverhampton" and x["visitante"] == "Everton"])
print("db:", [j[4:9] for j in jogos(E, "1888/89", ["Wolverhampton", "Everton"])], "| site tab:", [r for r in eds(E)["1888/89"]["tab"] if r[0] in ("Wolverhampton", "Everton")])

H("EN-007 rodadas")
com = Counter((x["temporada"], bool(x["rodada"])) for x in pj)
sem = sorted({t for (t, r), n in com.items() if not r})
print("temporadas com jogos sem rodada no pacote:", len(sem), sem[:3], "...", sem[-3:])
cr = Counter(x["temporada"] for x in pac(E, "classificacao_rodada"))
print("classificacao_rodada no pacote:", len(cr), "temporadas; antes de 1992/93:", sorted(t for t in cr if t < "1992/93")[:5])
for onde in ("site", "local"):
    e = eds(E, onde)
    print(onde, "1990/91 cor:", bool(e["1990/91"].get("cor")), "| rodada nos jogos 1990/91:", Counter(bool(j[0]) for j in e["1990/91"]["jogos"]).most_common(), "| 2010/11 cor:", bool(e["2010/11"].get("cor")))
print("db rodada 1990/91:", q("select count(*), count(rodada) from partida where edicao_id=?", eid(E, "1990/91")), "| db classificacao_rodada 1990/91:", q("select count(*) from classificacao_rodada where edicao_id=?", eid(E, "1990/91")))

H("EN-017 Newton Heath")
print([x["nomes_fonte"][:300] for x in pac(E, "clubes") if x["clube"] == "Manchester United"])
print("db clube_nome:", q("select nome, fonte, ano_inicio, ano_fim from clube_nome where clube_id=(select clube_id from clube where nome='Manchester United')"))

H("EN-018 Stoke 1889/90 e Darwen 1891/92")
for t, cl in (("1889/90", "Stoke City"), ("1891/92", "Darwen")):
    print(t, [(x["posicao"], x["clube"], x["situacao"], x["observacao"]) for x in pac(E, "classificacao_final") if x["temporada"] == t and x["clube"] == cl], "| db:", [r for r in cf(E, t) if r[1] == cl])

H("EN-016 jogos sem autor (2002/03-2016/17)")
gc = Counter(x["partida_id"] for x in pac(E, "gols"))
sem = [x for x in pj if "2002/03" <= x["temporada"] <= "2016/17" and int(x["gols_mandante"] or 0) + int(x["gols_visitante"] or 0) > 0 and gc[x["id"]] == 0]
print(len(sem), [(x["temporada"], x["data"], x["mandante"], x["visitante"]) for x in sem][:14])

H("ES-001 1935/36")
for cl in ("Real Oviedo", "Atlético de Madrid", "Osasuna"):
    print(cl, [(x["posicao"], x["situacao"], x["observacao"]) for x in pac(S, "classificacao_final") if x["temporada"] == "1935/36" and x["clube"] == cl], [r[0:2] + (r[10],) for r in cf(S, "1935/36") if r[1] == cl])

H("ES-002 1986/87")
print([(x["posicao"], x["clube"], x["situacao"]) for x in pac(S, "classificacao_final") if x["temporada"] == "1986/87"][13:])
print("observacao:", [x["observacao"] for x in pac(S, "edicoes") if x["temporada"] == "1986/87"])
print("site nota:", eds(S)["1986/87"].get("nota"))

H("ES-004 faixa de rebaixamento da tabela por rodada (última rodada)")
cr = pac(S, "classificacao_rodada")
for t in ("1965/66", "1989/90", "1993/94", "1997/98", "2014/15"):
    linhas = [x for x in cr if x["temporada"] == t]
    ult = max(int(x["rodada"]) for x in linhas)
    print(t, sorted((int(x["posicao"]), x["clube"], x["zona"]) for x in linhas if int(x["rodada"]) == ult and x["zona"]))
    print("   rebaixados:", [(x["posicao"], x["clube"]) for x in pac(S, "classificacao_final") if x["temporada"] == t and "rebaix" in x["situacao"]])
for onde in ("site", "local"):
    c0 = eds(S, onde)["2014/15"].get("cor") or {}
    print(onde, "2014/15 cor chaves:", list(c0.keys())[:10] if isinstance(c0, dict) else type(c0), str(c0)[:300])

H("ES-005 artilheiros")
for t in ("1929/30", "1934/35", "1935/36", "1954/55", "2003/04"):
    print(t, [(x["jogador"], x["gols"], x["fonte"][:160]) for x in pac(S, "artilheiros") if x["temporada"] == t], "| site:", eds(S)[t].get("artof"))

H("ES-006 nomes ESPN")
g = Counter(x["jogador"] for x in pac(S, "gols"))
for n in ("Kahveci Nihat", "Nihat Kahveci", "Fernando Sanchez Morientes", "Fernando Morientes", "Ismael Aranda Urzaiz", "Ismael Urzaiz", "Mendez Ruben Navarro", "Rubén Navarro",
          "Mocelin Magno", "Magno Mocelin", "Alsocer Raul Molina", "Raúl Molina", "Bortolini Pimentel Savio", "Sávio", "Fernandez Manuel Gutierrez Victor", "Víctor Fernández", "Víctor -",
          "Ballesta Salva", "Salvador Ballesta Vialcho", "Salva Ballesta"):
    print(n, g.get(n, 0), q("select count(*) from gol where jogador=?", n)[0][0])
