"""Campeões, vices e total de jogos/gols por edição: painel da 1ª rodada (commit 73ac503) x painel atual (= site)."""
import json, subprocess, sys
REF = sys.argv[1] if len(sys.argv) > 1 else "73ac503"
def ld(t): return json.loads(t[t.index("=") + 1:].strip().rstrip(";"))
for s in ("bra-serie-a", "bra-serie-b", "bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"):
    old = ld(subprocess.run(["git", "show", f"{REF}:painel/dados/{s}.js"], capture_output=True).stdout.decode("utf-8"))
    new = ld(open(f"painel/dados/{s}.js", encoding="utf-8").read())
    ko = {(e["ano"], e.get("comp")): e for e in old["ED"]}; kn = {(e["ano"], e.get("comp")): e for e in new["ED"]}
    eo = {e["id"]: e for e in old["EDS"]}; en = {e["id"]: e for e in new["EDS"]}
    print(f"== {s}: edições {len(eo)} -> {len(en)}; jogos {sum(e['j'] for e in eo.values())} -> {sum(e['j'] for e in en.values())}; gols {sum(e['g'] for e in eo.values())} -> {sum(e['g'] for e in en.values())}")
    camp = [(k, ko[k]["campeao"], kn.get(k, {}).get("campeao")) for k in ko if ko[k]["campeao"] != kn.get(k, {}).get("campeao")]
    print("  campeão mudou:", camp or "nenhum")
    vic = [(k[0], ko[k]["vice"], kn.get(k, {}).get("vice")) for k in ko if ko[k]["vice"] != kn.get(k, {}).get("vice")]
    print("  vice mudou:", vic or "nenhum")
    ter = [(k[0], ko[k]["terceiro"], kn.get(k, {}).get("terceiro")) for k in ko if ko[k]["terceiro"] != kn.get(k, {}).get("terceiro")]
    print("  3º mudou:", ter or "nenhum")
    dj = [(i, eo[i]["j"], en[i]["j"], eo[i]["g"], en[i]["g"]) for i in eo if i in en and (eo[i]["j"] != en[i]["j"] or eo[i]["g"] != en[i]["g"])]
    print("  jogos/gols mudaram (ed, j antes, j agora, g antes, g agora):", dj or "nenhum")
    print("  edições novas/sumidas:", set(en) - set(eo), set(eo) - set(en))
