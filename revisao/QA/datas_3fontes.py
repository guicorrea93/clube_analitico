"""Datas em três fontes: banco x Bola na Área (BNA) x fonte2 = Wikipédia pt (Série B até 2004; cache da 1ª rodada, data/cache/revisao/SB/)
ou Transfermarkt (Série A e Série B de 2005 em diante).
Para cada jogo do banco: data do banco, da BNA e da pt; classifica e sugere a data quando BNA e pt concordam.
Depois confere se a sugestão deixa algum clube com 2 jogos no mesmo dia.

Uso: python -I revisao/QA/datas_3fontes.py bra-serie-b 1990 1991 1997 1998   (grava revisao/QA/saida/datas_<slug>_<ano>.csv)
"""
import csv, glob, json, re, sys, pathlib
from collections import Counter, defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import comum, bna

SAIDA = pathlib.Path(__file__).parent / "saida"
SAIDA.mkdir(exist_ok=True)


def pt_jogos(ano):
    fs = [f for f in glob.glob("data/cache/revisao/SB/pt.wikipedia*") if f"de_{ano}_-_S" in f]
    if not fs:
        return []
    t = open(fs[0], encoding="utf-8").read()
    try:
        t = json.loads(t)["parse"]["wikitext"]["*"]
    except Exception:
        pass
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\{\{[^}]*\}\}", "", t)
    out = []
    for d, m, y, a, ga, gb, b in re.findall(r"(\d{1,2})/(\d{1,2})/(\d{4})\s*-\s*([^\n\t|]+?)\s*(\d+)\s*[xX×]\s*(\d+)\s*([^\n\t|]+?)(?:\s+-\s+|\s*$|\s*\n|\s*\|)", t, re.M):
        out.append({"data": f"{y}-{int(m):02d}-{int(d):02d}", "mandante": a.strip(), "visitante": b.strip(), "gm": int(ga), "gv": int(gb)})
    return out


def roda(slug, ano):
    fb = [j for j in bna.jogos(slug, ano, bna.paginas_edicao(slug, ano)) if not j["asterisco"]]
    if slug == "bra-serie-a" or int(ano) >= 2005:
        import cmp_tm
        fp = cmp_tm.temporada_tm(slug, int(ano))[1]
        nome2 = "Transfermarkt"
    else:
        fp = pt_jogos(ano)
        nome2 = "Wikipédia pt"
    rb = comum.comparar(slug, ano, fb)
    rp = comum.comparar(slug, ano, fp) if fp else {"pares": []}
    pb = {b[0]: j for j, b in rb.get("pares", [])}
    pp = {b[0]: j for j, b in rp.get("pares", [])}
    banco = comum.jogos_banco(slug, ano)
    cat = Counter()
    linhas = []
    for b in banco:
        d0 = b[1]
        d1 = pb.get(b[0], {}).get("data")
        d2 = pp.get(b[0], {}).get("data")
        if d1 is None and d2 is None:
            k = "sem fonte nova"
            sug = ""
        elif d0 and d0 in (d1, d2) and (d1 in (None, d0)) and (d2 in (None, d0)):
            k = "banco confirmado"
            sug = ""
        elif d1 and d2 and d1 == d2 and d1 != d0:
            k = "banco diferente; BNA = fonte2" if d0 else "banco sem data; BNA = fonte2"
            sug = d1
        elif d1 and d2 and d1 != d2:
            k = "BNA x fonte2 divergem" + ("; banco = fonte2" if d0 == d2 else "; banco = BNA" if d0 == d1 else "")
            sug = ""
        else:
            so = d1 or d2
            if d0 == so:
                k = "banco confirmado (1 fonte)"
                sug = ""
            else:
                k = ("banco sem data; só " if not d0 else "banco diferente; só ") + ("BNA" if d1 else "fonte2")
                sug = so
        cat[k] += 1
        linhas.append({"ano": ano, "fase": b[6], "rodada": b[7], "mandante": b[9], "placar": f"{b[4]}x{b[5]}", "visitante": b[10],
                       "data_banco": d0 or "", "data_bna": d1 or "", "fonte2": nome2, "data_fonte2": d2 or "", "situacao": k, "sugestao": sug})
    # conflito: com as sugestões aplicadas, clube com 2 jogos no mesmo dia?
    por = defaultdict(list)
    for l in linhas:
        d = l["sugestao"] or l["data_banco"]
        if d:
            por[(l["mandante"], d)].append(l)
            por[(l["visitante"], d)].append(l)
    conflitos = sum(1 for v in por.values() if len(v) > 1)
    por0 = defaultdict(list)
    for l in linhas:
        if l["data_banco"]:
            por0[(l["mandante"], l["data_banco"])].append(l)
            por0[(l["visitante"], l["data_banco"])].append(l)
    conf0 = sum(1 for v in por0.values() if len(v) > 1)
    with open(SAIDA / f"datas_{slug}_{ano}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    print(f"== {slug} {ano}: {len(banco)} jogos no banco; BNA {len(fb)} lidos ({len(pb)} casados); fonte2 = {nome2}: {len(fp)} lidos ({len(pp)} casados)")
    for k, v in cat.most_common():
        print(f"   {v:4d}  {k}")
    print(f"   clube com 2 jogos no mesmo dia: hoje {conf0}; com as sugestões {conflitos}")


if __name__ == "__main__":
    slug = sys.argv[1]
    for ano in sys.argv[2:]:
        roda(slug, ano)
