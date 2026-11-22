"""FPF (fpf_jogos.json, 2007 a 2026) como desempate oficial das diferenças de data e placar entre o pacote e o Futebol
Nacional (fn_diferencas.csv), e contagem geral pacote x FPF (jogos casados por data ±3 dias e placar, com o nome do
clube comparado pelo começo do nome sem acento). Saída: revisao/QS/fpf_comparar_saida.txt.
Uso (da raiz): python -I -X utf8 revisao/QS/fpf_comparar.py"""
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
# nomes da FPF (nome popular de hoje) -> começo do nome no pacote
APELIDO = {"osasco sporting": "oeste", "grêmio novorizontino": "novorizontino", "red bull bragantino": "bragantino",
           "botafogo": "botafogo", "água santa": "ec água", "internacional": "inter de", "gr barueri": "barueri",
           "grêmio barueri": "barueri", "grêmio prudente": "barueri", "audax": "osasco audax", "juventus saf": "juventus",
           "xv piracicaba": "xv de piracicaba", "xv de piracicaba": "xv de piracicaba", "sorocaba": "atletico sorocaba",
           "atlético sorocaba": "atletico sorocaba", "ua barbarense": "uniao barbarense", "xv de jaú": "xv de jau",
           "xv jaú": "xv de jau"}


def sa(x):
    return unicodedata.normalize("NFKD", x or "").encode("ascii", "ignore").decode().lower().strip()


def chave_clube(n):
    n = sa(n)
    for k, v in APELIDO.items():
        if n.startswith(sa(k)):
            n = sa(v)
            break
    n = re.sub(r"[^a-z ]", "", n)
    return n[:8] if n.startswith("xv") else n[:5]


def iso(d):
    dd, mm, aa = d.split("/")
    return f"{aa}-{mm}-{dd}"


def dias(a, b):
    try:
        return abs((date.fromisoformat(a) - date.fromisoformat(b)).days)
    except (TypeError, ValueError):
        return 999


def main():
    fpf = json.loads((AQUI / "fpf_jogos.json").read_text(encoding="utf-8"))
    pac = defaultdict(list)
    for p in csv.DictReader(open(RAIZ / "data" / "coleta" / "bra-sp-1" / "pacote" / "partidas.csv", encoding="utf-8")):
        pac[p["temporada"]].append(p)
    out = ["Ano\tFPF jogos\tpacote\tcasados\tdata igual\tplacar igual"]
    achar = {}
    for ano, js in sorted(fpf.items()):
        livres = list(pac.get(ano, []))
        c = Counter()
        for j in js:
            if j["ResultadoMandante"] is None:
                continue
            d = iso(j["Data"])
            km, kv = chave_clube(j["NomePopularMandante"]), chave_clube(j["NomePopularVisitante"])
            cands = [p for p in livres if {chave_clube(p["mandante"]), chave_clube(p["visitante"])} == {km, kv}
                     and dias(p["data"], d) <= 10]
            if not cands:
                c["so_fpf"] += 1
                continue
            p = min(cands, key=lambda p: dias(p["data"], d))
            livres.remove(p)
            c["casados"] += 1
            c["data_ok"] += p["data"] == d
            g = (j["ResultadoMandante"], j["ResultadoVisitante"])
            gp = (int(p["gols_mandante"] or -1), int(p["gols_visitante"] or -1))
            if chave_clube(p["mandante"]) != km:
                gp = gp[::-1]
            c["placar_ok"] += g == gp
            achar[(ano, p["data"], p["mandante"], p["visitante"])] = (d, g, j)
            if p["data"] != d:
                out.append(f"  DATA {ano} pacote {p['data']} {p['mandante']} x {p['visitante']} | FPF {d} {j['Horario']} (jogo {j['Numero']})")
            if g != gp:
                out.append(f"  PLACAR {ano} pacote {p['data']} {p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']}"
                           f" | FPF {d} {j['NomePopularMandante']} {g[0]}-{g[1]} {j['NomePopularVisitante']} (fase {j['Fase']}, jogo {j['Numero']})")
        out.append(f"{ano}\t{len(js)}\t{len(pac.get(ano, []))}\t{c['casados']}\t{c['data_ok']}\t{c['placar_ok']}\t(só FPF {c['so_fpf']})")
    # diferenças pacote x Futebol Nacional de 2007 em diante: quem a FPF confirma
    veredito = Counter()
    out.append("\nDiferenças pacote x Futebol Nacional (2007+) com a FPF como desempate:")
    for x in csv.DictReader(open(AQUI / "fn_diferencas.csv", encoding="utf-8")):
        if int(x["temporada"][:4]) < 2007 or x["tipo"] not in ("data", "placar"):
            continue
        m = re.match(r"(.+?) (\d+)-(\d+) (.+)$", x["jogo_pacote"])
        k = (x["temporada"], x["data_pacote"], m[1], m[4]) if m else None
        f = achar.get(k)
        if not f:
            veredito["FPF não achou"] += 1
            out.append(f"  ? {x['temporada']} {x['tipo']} FN {x['data_fn']} {x['placar_fn']} | pacote {x['data_pacote']} {x['jogo_pacote']}")
            continue
        d, g, j = f
        if x["tipo"] == "data":
            v = "FPF = pacote" if d == x["data_pacote"] else "FPF = FN" if d == x["data_fn"] else "FPF outra"
        else:
            gp = re.match(r"(\d+)-(\d+)", x["placar_fn"])
            v = "FPF = FN" if gp and (int(gp[1]), int(gp[2])) == g else "FPF = pacote" if m and (int(m[2]), int(m[3])) == g else "FPF outra"
        veredito[(x["tipo"], v)] += 1
        out.append(f"  {v}\t{x['temporada']} {x['tipo']}\tpacote {x['data_pacote']} {x['jogo_pacote']}\tFN {x['data_fn']} {x['placar_fn']}"
                   f"\tFPF {d} {g[0]}-{g[1]}\t{x['ogol']}")
    out.append(json.dumps({str(k): v for k, v in veredito.items()}, ensure_ascii=False))
    (AQUI / "fpf_comparar_saida.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(o for o in out if not o.startswith("  ")))
    print(json.dumps({str(k): v for k, v in veredito.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
