"""Fichas de jogo do BDFutbol, amostra por década (autores, cartões, árbitro) e os jogos sem autor do eng-1 (EN-016).

- Espanha 1928/29-2025/26 e Inglaterra 1960/61-2025/26: 2 jogos com gol por década (sorteio fixo); nas décadas em que o
  pacote tem autores (2000s+), 6 jogos, comparando autor a autor (sobrenome) com gols.csv do pacote.
- eng-1: os jogos com gol e sem nenhum autor no pacote (EN-016).
Saída: revisao/QE/amostra_fichas_saida.txt.  Uso: python -I revisao/QE/amostra_fichas.py
"""
import csv
import json
import random
import sys
import unicodedata
from collections import Counter, defaultdict
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import baixar  # noqa: E402
import bdfutbol as bdf  # noqa: E402


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return s.replace("-", " ").replace(".", " ").split()


def casa(a, b):
    """mesmo jogador? algum pedaço do nome (>= 4 letras) em comum."""
    x, y = set(w for w in norm(a) if len(w) >= 4), set(w for w in norm(b) if len(w) >= 4)
    return bool(x & y) or norm(a)[-1:] == norm(b)[-1:]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    out = []
    rnd = random.Random(2211)
    for liga, slug in (("esp", "esp-1"), ("eng", "eng-1")):
        P = f"data/coleta/{slug}/pacote/"
        pares = json.load(open(f"data/cache/revisao/QE/pares_bdfutbol_{liga}.json", encoding="utf-8"))
        part = {r["id"]: r for r in csv.DictReader(open(P + "partidas.csv", encoding="utf-8"))}
        gols = defaultdict(list)
        for g in csv.DictReader(open(P + "gols.csv", encoding="utf-8")):
            gols[g["partida_id"]].append(g)
        card = Counter(c["partida_id"] for c in csv.DictReader(open(P + "cartoes.csv", encoding="utf-8")))
        por_dec = defaultdict(list)
        for pid, r in part.items():
            if pid in pares and int(r["gols_mandante"]) + int(r["gols_visitante"]) > 0:
                por_dec[int(r["temporada"][:4]) // 10 * 10].append(pid)
        alvo = []
        for d in sorted(por_dec):
            n = 6 if d >= 2000 else 2
            alvo += [(d, x) for x in rnd.sample(sorted(por_dec[d]), n)]
        if liga == "eng":
            sem = [pid for pid, r in part.items() if "2002" <= r["temporada"][:4] <= "2016"
                   and int(r["gols_mandante"]) + int(r["gols_visitante"]) > 0 and not gols[pid]]
            alvo += [("EN-016", x) for x in sorted(sem)]
        tot = Counter()
        for d, pid in alvo:
            r = part[pid]
            arq = baixar(bdf.url_jogo(pares[pid]["pid"]))
            f = bdf.ficha(arq)
            placar = int(r["gols_mandante"]) + int(r["gols_visitante"])
            ok_soma = len(f["gols"]) == placar
            lin = (f"{liga} {d} | {r['temporada']} {r['data']} {r['mandante']} {r['gols_mandante']}-{r['gols_visitante']} {r['visitante']}"
                   f" | BDFutbol id {pares[pid]['pid']}: {len(f['gols'])} gols com autor ({'fecha' if ok_soma else 'NÃO fecha'} com o placar),"
                   f" {len(f['cartoes'])} cartões, árbitro '{pares[pid]['arbitro']}', público '{f['publico']}'")
            tot[(liga, "fichas")] += 1
            tot[(liga, "fecha")] += ok_soma
            tot[(liga, "com_cartao")] += bool(f["cartoes"])
            if gols[pid]:
                pg = sorted((int(g["minuto"] or 0), g["jogador"]) for g in gols[pid])
                bg = sorted((m, n) for _, _, n, m in f["gols"])
                iguais = sum(1 for (m1, n1), (m2, n2) in zip(pg, bg) if casa(n1, n2))
                tot[(liga, "autores_pacote")] += len(pg)
                tot[(liga, "autores_iguais")] += iguais
                tot[(liga, "cart_pacote")] += card[pid]
                tot[(liga, "cart_bdf")] += len(f["cartoes"])
                lin += f" | autores iguais ao pacote: {iguais} de {len(pg)}; cartões pacote {card[pid]}"
                if iguais < len(pg):
                    lin += f" | pacote {pg} x BDFutbol {bg}"
            else:
                lin += " | autores: " + "; ".join(f"{n} {m}'" for _, _, n, m in f["gols"])
            out.append(lin)
        out.append(f"RESUMO {liga}: {dict((k[1], v) for k, v in tot.items() if k[0] == liga)}")
    open("revisao/QE/amostra_fichas_saida.txt", "w", encoding="utf-8").write("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
