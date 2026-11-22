"""Fichas de jogo do transfermarkt (spielbericht), amostra por década: autores, público, árbitro, estádio.

- eng-1 1888/89-1959/60 (competição EFD1; pares de revisao/QE/cmp_tm_eng.py): 3 jogos com gol por década.
- esp-1 (competição ES1): 2 jogos por década, achados pelo calendário da temporada (gesamtspielplan ES1).
Saída: revisao/QE/amostra_tm_saida.txt.  Uso: python -I revisao/QE/amostra_tm.py
"""
import csv
import html
import json
import random
import re
import sys
import pathlib
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import baixar  # noqa: E402

FICHA = "https://www.transfermarkt.com/spielbericht/index/spielbericht/{}"


def ficha(arq):
    t = open(arq, encoding="utf-8", errors="replace").read()
    s = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", t, flags=re.S))))
    pub = re.search(r"Attendance: ([\d\.]+)", s)
    arb = re.search(r"Referee: (.+?) (?=[A-Z][a-z]+ [A-Z]|\d)", s)
    g = s.find("Goals ")
    fim = min([x for x in (s.find("Substitutions", g), s.find("Cards", g), s.find("Quick Links", g)) if x > 0] or [g + 3000])
    gols = re.findall(r"(\d+):(\d+) ([^,]+?) ,", s[g:fim]) if g >= 0 else []
    return {"publico": pub.group(1) if pub else "", "arbitro": arb.group(1) if arb else "", "gols": gols}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rnd = random.Random(2211)
    out = []
    tot = Counter()
    part = {r["id"]: r for r in csv.DictReader(open("data/coleta/eng-1/pacote/partidas.csv", encoding="utf-8"))}
    pares = json.load(open("data/cache/revisao/QE/pares_tm_eng.json", encoding="utf-8"))
    por = {}
    for pid, tid in pares.items():
        r = part[pid]
        if int(r["gols_mandante"]) + int(r["gols_visitante"]) > 0:
            por.setdefault(int(r["temporada"][:4]) // 10 * 10, []).append(pid)
    for d in sorted(por):
        for pid in rnd.sample(sorted(por[d]), 3):
            r = part[pid]
            f = ficha(baixar(FICHA.format(pares[pid])))
            soma = int(r["gols_mandante"]) + int(r["gols_visitante"])
            tot["fichas"] += 1
            tot["fecha"] += len(f["gols"]) == soma
            tot["publico"] += bool(f["publico"])
            tot["arbitro"] += bool(f["arbitro"])
            out.append(f"eng {d}s | {r['temporada']} {r['data']} {r['mandante']} {r['gols_mandante']}-{r['gols_visitante']} {r['visitante']} | "
                       f"TM {pares[pid]}: {len(f['gols'])} autores ({'fecha' if len(f['gols']) == soma else 'NÃO fecha'}), público {f['publico'] or '-'}, "
                       f"árbitro {f['arbitro'] or '-'} | " + "; ".join(f"{a}:{b} {n}" for a, b, n in f["gols"]))
    out.append(f"RESUMO eng: {dict(tot)}")
    open("revisao/QE/amostra_tm_saida.txt", "w", encoding="utf-8").write("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
