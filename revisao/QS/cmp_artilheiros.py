"""Artilheiros: Futebol Nacional (fn_resumo.json) x Wikipédia pt (revisao/SP/artilheiros_wiki.json) x FPF (fpf_artilharia.json,
2007 em diante, quando existir). Compara o número de gols do artilheiro e o sobrenome/apelido.
Saída: revisao/QS/cmp_artilheiros_saida.txt. Uso (da raiz): python -I -X utf8 revisao/QS/cmp_artilheiros.py"""
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]


def sa(x):
    return unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()


def temporada(t):
    m = re.match(r"(\d{4})(?: \((\w+)\))?", t)
    return m[1], ({"APSA": "APEA"}.get(m[2], m[2]) if m[2] else "")


def main():
    fn = [r for r in json.loads((AQUI / "fn_resumo.json").read_text(encoding="utf-8")) if r["competicao"] == "Campeonato Paulista"]
    wk = json.loads((RAIZ / "revisao" / "SP" / "artilheiros_wiki.json").read_text(encoding="utf-8"))
    fpf = json.loads((AQUI / "fpf_artilharia.json").read_text(encoding="utf-8")) if (AQUI / "fpf_artilharia.json").exists() else {}
    out, c = [], Counter()
    for r in fn:
        ano, liga = temporada(r["temporada"])
        m = re.search(r"(\d+) gols?", r["artilheiro"] or "")
        g_fn = int(m[1]) if m else None
        w = wk.get(ano) or []
        # nos anos de duas ligas a Wikipédia lista uma linha por liga, na ordem LPF/APEA ou APEA/LAF
        gw = sorted({int(x[2][0]) for x in w if x and x[2] and x[2][0].isdigit()})
        nomes_w = {sa(n) for x in w for n in x[0]}
        nomes_fn = {sa(n.strip()) for n in re.split(r",| e ", re.sub(r"\([^)]*\)|\d+ gols?", "", r["artilheiro"] or "")) if n.strip()}
        linha = f"{r['temporada']}\tFN: {r['artilheiro']}\tWiki: {'; '.join(', '.join(x[0]) + ' ' + x[2][0] for x in w if x and x[2])}"
        if ano in fpf and fpf[ano]:
            top = [x for x in fpf[ano] if x["Ranking"] == 1]
            linha += f"\tFPF: {', '.join(x['AtletaApelido'] + ' (' + x['ClubeNomePopular'] + ')' for x in top)} {top[0]['Gols'] if top else ''}"
        if g_fn is None:
            c["fn_sem"] += 1
            continue
        if not gw:
            c["wiki_sem"] += 1
            out.append("SÓ FN\t" + linha)
            continue
        c["conf"] += 1
        bate_g = g_fn in gw
        bate_n = any(any(p in w2 or w2 in p for w2 in nomes_w for p in [n] if len(p) > 2) for n in nomes_fn)
        if bate_g and bate_n:
            c["igual"] += 1
        else:
            c["difere"] += 1
            out.append(("GOLS" if not bate_g else "NOME") + "\t" + linha)
    out.append(json.dumps(c))
    (AQUI / "cmp_artilheiros_saida.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
