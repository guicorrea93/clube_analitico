"""Reconferência dos achados do banco e painel corrigidos pelo agente 1 depois de 21/11: banco x site (x local).
Uso: python -I revisao/RC/painel.py > SCRATCH/RC/painel_saida.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
from collections import Counter
def H(t): print("\n=====", t)
def tab(slug, temp, onde="site", n=None, nomes=None):
    e = eds(slug, onde).get(temp)
    if not e: return None
    t = e["tab"]
    if nomes: t = [r for r in t if r[0] in nomes]
    return t[:n] if n else t

A, B = "bra-serie-a", "bra-serie-b"
H("RV-001 Série B 2001 Figueirense x Caxias")
for x in jogos(B, "2001", ["Figueirense", "Caxias"]): print(x[:12])
print("site tab:", tab(B, "2001", nomes={"Figueirense", "Caxias"}))
print("db cf:", [r for r in cf(B, "2001") if r[1] in ("Figueirense", "Caxias")])

H("RV-002 Série B 2014")
print("site tab 1-6:", tab(B, "2014", n=6))
print("db cf:", cf(B, "2014")[:6])
print("site ED:", [x for x in ed_lista(B) if x["ano"] == 2014])

H("RV-003 Série B 1980, 1990, 1991 datas")
for x in jogos(B, "1980"):
    if x[1] and ("Semi" in x[1] or "Final" in x[1] or "Terceira" in x[1]): print(x[:9])
for x in jogos(B, "1990", ["Moto Club", "Treze"]) + jogos(B, "1990", ["Remo", "Ceará"]): print(x[:9])
print("1990 Grupo D datas por rodada:", sorted({(x[3], x[4]) for x in jogos(B, "1990") if x[2] == "D"})[:20])
dup = Counter((x[4], cl) for x in jogos(B, "1991") if x[4] for cl in (x[5], x[8]))
print("1991 clube 2 jogos no mesmo dia:", [k for k, v in dup.items() if v > 1])
print("1991 Joinville x Juventude / Blumenau x Figueirense:", [x[:9] for x in jogos(B, "1991", ["Joinville", "Juventude"]) + jogos(B, "1991", ["Blumenau", "Figueirense"])])
print("1991 jogos sem data:", sum(1 for x in jogos(B, "1991") if not x[4]), "de", len(jogos(B, "1991")))

H("RV-004 / SB-013 artilheiro cartão (dados)")
for slug, a in [(A, "1959"), (B, "1971"), (B, "1988"), (B, "1989"), (B, "1990"), ("bra-serie-c", "1988")]:
    e = eds(slug).get(a)
    print(slug, a, "artof:", e.get("artof"), "| art[:2]:", (e.get("art") or [])[:2], "| cob:", e.get("cob"))
print("db artilheiro B 1971/1988-1990/2004/2016:", q("select e.temporada, a.jogador, a.gols from artilheiro a join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and e.temporada in ('1971','1988','1989','1990','2004','2016')", B))

H("SA-003 Série A 2003")
print("site tab:", [(r[0], r[1], r[-1]) for r in tab(A, "2003")])
print("db cf:", [(r[0], r[1], r[8], r[9]) for r in cf(A, "2003")])

H("SA-024 Série A 2005 e 2016 especiais e notas")
for a in ("2005", "2016"):
    print(a, "especiais db:", [x[4:9] + (x[11],) for x in jogos(A, a) if x[11]], "| nota site:", eds(A)[a].get("nota"), "| ED nota:", [x.get("nota") for x in ed_lista(A) if x["ano"] == int(a)], "| j:", eds(A)[a]["j"])
print("2005 obs anulados:", [x[4:9] + (x[12],) for x in jogos(A, "2005") if x[12]][:14])

H("SB-018 Série B fases")
for a in ("1985", "1988", "1999", "2001", "2002"):
    print(a, eds(B)[a].get("disputa"))
print("fases B em inglês:", sorted({(e, f) for e, f in q("select e.temporada, f.nome from fase f join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=?", B) if any(w in f.lower() for w in ("final match", "playoff", "-finals", "group", "relegation", "north", "south"))}))
print("grupos B 2001:", q("select distinct p.grupo from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug=? and e.temporada='2001'", B))

H("CB-013 Copa: Pontuação histórica (dados)")
d = js("bra-copa-do-brasil")
print("chaves:", list(d.keys()), "TX:", {k: v for k, v in d["TX"].items()})

H("SP-025 Paulista artilharia")
for a in ("1951", "1999", "2000", "2003", "2004", "2014", "2018"):
    e = eds("bra-sp-1").get(a); el = eds("bra-sp-1", "local").get(a)
    print(a, "site artof:", e.get("artof"), "art:", (e.get("art") or [])[:2], "cob:", e.get("cob"), "|| local artof:", el.get("artof"), "cob:", el.get("cob"))

H("UY-002 / UY-025 / UY-009 Uruguaio")
print("1948 ED:", [x for x in ed_lista("uru-1") if x["ano"] == 1948], "| EDS nota:", eds("uru-1")["1948"].get("nota"))
print("TX uru:", js("uru-1")["TX"])

H("AR-036 Argentino: tab do site x classificacao_final do banco")
dif = tot = 0; eds_dif = set(); ex = []
for k, e in eds("arg-1").items():
    db = {r[1]: r for r in cf("arg-1", k)}
    for r in e["tab"]:
        tot += 1
        d0 = db.get(r[0])
        if not d0: continue
        if [r[1], r[2], r[3], r[4], r[5], r[6], r[7]] != [d0[0], d0[2], d0[3], d0[4], d0[5], d0[6], d0[7]]:
            dif += 1; eds_dif.add(k)
            if len(ex) < 8: ex.append((k, r[:8], d0[:8]))
print("linhas diferentes:", dif, "de", tot, "edições:", len(eds_dif)); print(ex)
print("1895 Lomas Academicals:", tab("arg-1", "1895", nomes={"Lomas Academicals"}), "| 2006/07 Apertura Estudiantes:", tab("arg-1", "2006/07 Apertura", nomes={"Estudiantes"}))
H("AR-037 Maior artilheiro River (dados)")
print("ARTC River:", js("arg-1").get("ARTC", {}).get("River Plate", [])[:3], "| ARTCOB:", js("arg-1").get("ARTCOB", {}).get("River Plate"))
H("AR-042 / AR-038 2025 Liga")
print(eds("arg-1").get("2025 Liga", {}).get("j"), eds("arg-1").get("2025 Liga", {}).get("nota"), [x for x in ed_lista("arg-1") if x["ano"] == 2025])
print("TX arg:", js("arg-1")["TX"])

H("ES-003 Espanhol 1979/80")
for onde in ("site", "local"):
    print(onde, tab("esp-1", "1979/80", onde, nomes={"AD Almería", "CD Málaga"}))
print("db:", [r for r in cf("esp-1", "1979/80") if r[1] in ("AD Almería", "CD Málaga")])
H("ES-007 artilharia 2003/04")
for onde in ("site", "local"):
    e = eds("esp-1", onde)["2003/04"]; print(onde, "artof:", e.get("artof"), "art:", (e.get("art") or [])[:3], "cob:", e.get("cob"))
H("ES-008 / ES-009 / EN-011 curiosidades de campeões")
for slug in ("esp-1", "eng-1"):
    for onde in ("site", "local"):
        cur = js(slug, onde)["CUR"]
        print(slug, onde, "CUR chaves:", list(cur.keys()))
        for k, v in cur.items():
            if isinstance(v, dict):
                for kk, vv in v.items():
                    if any(w in kk.lower() for w in ("apert", "vant", "folga", "margem", "aprov")): print("  ", k, kk, str(vv)[:400])
H("ES-014 / EN-015 nomes e temporadas")
for slug in ("esp-1", "eng-1"):
    for onde in ("site", "local"):
        e = eds(slug, onde); ks = list(e)
        print(slug, onde, [(k, e[k].get("nome"), e[k].get("t")) for k in (ks[0], ks[len(ks)//2], ks[-1])], "TX:", js(slug, onde)["TX"].get("selo") or js(slug, onde)["TX"])
H("EN-008 participantes vizinhos às guerras (dados mv)")
for onde in ("site", "local"):
    e = eds("eng-1", onde)
    for k in ("1914/15", "1919/20", "1938/39", "1946/47"):
        if k in e: print(onde, k, "mv:", str(e[k].get("mv"))[:200], "| ac:", e[k].get("ac"), "| cai:", e[k].get("cai") or e[k].get("rb"))
