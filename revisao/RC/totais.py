"""Campeão, vice, 3º, jogos e gols por edição: painel revisado na 2ª rodada (commit 2dbc105, 21/11 09:51) x site (22/11) x local.
Uso: python -I revisao/RC/totais.py [ref] > SCRATCH/RC/totais_saida.txt"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import js
REF = sys.argv[1] if len(sys.argv) > 1 else "2dbc105"
def ld(t): return json.loads(t[t.index("=") + 1:].strip().rstrip(";"))
SLUGS = ["bra-serie-a", "bra-serie-b", "bra-serie-c", "bra-serie-d", "bra-copa-do-brasil", "bra-sp-1", "arg-1", "uru-1", "eng-1", "esp-1"]
def chave(e): return f"{e['ano']}{(' ' + e['comp']) if e.get('comp') else ''}"
def compara(a, b, rot):
    ka = {chave(e): e for e in a["ED"]}; kb = {chave(e): e for e in b["ED"]}
    ea = {str(e["id"]): e for e in a["EDS"]}; eb = {str(e["id"]): e for e in b["EDS"]}
    print(f"  [{rot}] edições {len(ea)} -> {len(eb)}; jogos {sum(e['j'] for e in ea.values())} -> {sum(e['j'] for e in eb.values())}; gols {sum(e['g'] for e in ea.values())} -> {sum(e['g'] for e in eb.values())}")
    for campo in ("campeao", "vice", "terceiro"):
        d = [(k, ka[k].get(campo), kb[k].get(campo)) for k in ka if k in kb and ka[k].get(campo) != kb[k].get(campo)]
        print(f"    {campo} mudou ({len(d)}):", d if d else "nenhum")
    dj = [(i, ea[i]["j"], eb[i]["j"], ea[i]["g"], eb[i]["g"]) for i in ea if i in eb and (ea[i]["j"] != eb[i]["j"] or ea[i]["g"] != eb[i]["g"])]
    print(f"    jogos/gols mudaram ({len(dj)}) (ed, j antes, j agora, g antes, g agora):", dj if dj else "nenhum")
    print("    edições novas:", sorted(set(eb) - set(ea)), "| sumidas:", sorted(set(ea) - set(eb)))
for s in SLUGS:
    r = subprocess.run(["git", "show", f"{REF}:painel/dados/{s}.js"], capture_output=True)
    print(f"== {s}")
    if r.returncode:
        print("  (não existia no", REF, ")"); continue
    old = ld(r.stdout.decode("utf-8"))
    compara(old, js(s, "site"), f"{REF} x site")
    if open(f"data/cache/revisao/RC/site/{s}.js", encoding="utf-8").read().strip() != open(f"painel/dados/{s}.js", encoding="utf-8").read().strip():
        compara(js(s, "site"), js(s, "local"), "site x local (não publicado)")
