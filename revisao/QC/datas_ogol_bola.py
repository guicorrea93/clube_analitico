"""Datas do pacote contra o ogol (cache da coleta) e o Bola n@ Área juntos: a data do pacote veio da RSSSF e as outras
duas fontes concordam entre si numa data diferente.

Uso (raiz): python -I revisao/QC/datas_ogol_bola.py -> revisao/QC/saida_datas_ogol_bola.txt
"""
import collections, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum

OGOL = {"bra-serie-c": "serie_c_", "bra-serie-d": "serie_d_", "bra-copa-do-brasil": "copa_brasil_"}


def main():
    out, resumo = [], []
    for slug in comum.SLUGS:
        og = {}
        for f in glob.glob(os.path.join(comum.RAIZ, "data", "coleta", slug, "ogol", OGOL[slug] + "*.json")):
            for j in json.load(open(f, encoding="utf-8")):
                og[j["id"]] = j["data"]
        pac = comum.pacote(slug)
        uf_de = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        cont = collections.Counter()
        for ano in sorted({int(p["temporada"]) for p in pac}):
            fb = bola.jogos(slug, ano)
            if not fb:
                continue
            jp = [p for p in pac if int(p["temporada"]) == ano]
            pares, _ = comum.casar(fb, jp, uf_de)
            for f, p, inv in pares:
                if not f["data"] or f["data"] == p["data"]:
                    continue
                oid = p["fonte_id"].split("ogol:")[-1].split(";")[0] if "ogol:" in p["fonte_id"] else ""
                do = og.get(oid, "")
                if do and do == f["data"]:
                    cont[comum.decada(ano)] += 1
                    out.append("%s %d | pacote %s %s %s-%s %s (%s) | ogol e bola: %s" % (
                        slug, ano, p["data"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"], p["fase"], do))
        resumo.append("%s: %s" % (slug, dict(cont)))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_datas_ogol_bola.txt"), "w", encoding="utf-8").write(
        "\n".join(resumo) + "\n\n" + "\n".join(out) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(resumo))


if __name__ == "__main__":
    main()
