"""Placares do pacote (RSSSF) contra ogol + Bola n@ Área + Futebol Nacional.

Lista o jogo quando o ogol diverge do pacote e o Bola e/ou o Futebol Nacional ficam com o ogol.
Uso (raiz): python -I revisao/QC/placar_4fontes.py -> revisao/QC/saida_placar_4fontes.txt (só cache, não baixa nada)
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum, fn

OGOL = {"bra-serie-c": "serie_c_", "bra-serie-d": "serie_d_", "bra-copa-do-brasil": "copa_brasil_"}


def main():
    out = []
    for slug in comum.SLUGS:
        og = {}
        for f in glob.glob(os.path.join(comum.RAIZ, "data", "coleta", slug, "ogol", OGOL[slug] + "*.json")):
            for j in json.load(open(f, encoding="utf-8")):
                og[j["id"]] = j
        pac = comum.pacote(slug)
        uf = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        cods = fn.codigos(slug)
        for ano in sorted({int(p["temporada"]) for p in pac}):
            jp = [p for p in pac if int(p["temporada"]) == ano]
            pb = {p["id"]: (f, inv) for f, p, inv in comum.casar(bola.jogos(slug, ano), jp, uf)[0]}
            pf = {}
            if ano in cods and os.path.exists(os.path.join(fn.PASTA, cods[ano] + ".html")):
                pf = {p["id"]: (f, inv) for f, p, inv in comum.casar(fn.ler(fn.baixar(cods[ano]))["jogos"], jp, uf)[0]}
            for p in jp:
                oid = p["fonte_id"].split("ogol:")[-1].split(";")[0] if "ogol:" in p["fonte_id"] else ""
                o = og.get(oid)
                if not o or o.get("gols_mandante") is None or p["gols_mandante"] == "":
                    continue
                op = (int(o["gols_mandante"]), int(o["gols_visitante"]))
                pp = (int(p["gols_mandante"]), int(p["gols_visitante"]))
                if op == pp or p["resultado_especial"]:
                    continue
                votos = []
                for nome, d in (("Bola", pb), ("FN", pf)):
                    if p["id"] in d:
                        f, inv = d[p["id"]]
                        fp = (f["gv"], f["gm"]) if inv else (f["gm"], f["gv"])
                        votos.append("%s %d-%d%s" % (nome, fp[0], fp[1], " (=ogol)" if fp == op else " (=pacote)" if fp == pp else ""))
                if any("(=ogol)" in v for v in votos):
                    n_ogol = sum("(=ogol)" in v for v in votos)
                    out.append("%s %d | %s %s %d-%d %s (%s) | ogol %d-%d | %s | %s" % (
                        slug, ano, p["data"], p["mandante"], pp[0], pp[1], p["visitante"], p["fase"], op[0], op[1],
                        "; ".join(votos), "FORTE" if n_ogol == 2 else "fraco"))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_placar_4fontes.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
