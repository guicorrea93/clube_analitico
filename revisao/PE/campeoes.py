"""Campeão e vice de cada edição do per-1: pacote x banco x painel local x Wikipédia es (Primera División del Perú, Palmarés).

Uso (raiz do projeto): python -I revisao/PE/campeoes.py
"""
import csv
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PAC = RAIZ / "data" / "coleta" / "per-1" / "pacote"
CACHE = RAIZ / "data" / "cache" / "revisao" / "PE"
sys.stdout.reconfigure(encoding="utf-8")

# nome da Wikipédia es -> nome de exibição do pacote
ES = {
    "Lima Cricket F. B. C.": "Lima Cricket", "Association F. C.": "Association FBC",
    "Jorge Chávez Nr. 1": "Jorge Chávez N°1", "Jorge Chávez Nr. 2": "Jorge Chávez N°2 (não existe no pacote)",
    "Sport Alianza": "Alianza Lima", "Sport Sáenz Peña": "Sport Sáenz Peña", "Federación Universitaria": "Universitario",
    "Universitario de Deportes": "Universitario", "Sucre F. B. C.": "Mariscal Sucre", "F. B. C. Melgar": "Melgar",
    "San Agustín": "Deportivo San Agustín", "Real Garcilaso": "Cusco FC", "Deportivo Binacional": "Binacional",
    "Universidad Técnica de Cajamarca": "UTC",
}


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def es_lista():
    t = json.loads((CACHE / "es_primera_division.json").read_text(encoding="utf-8"))["parse"]["wikitext"]
    t = t[t.index("=== Títulos por año ==="):t.index("=== Títulos por equipo ===")]
    out = {}
    linhas = t.split("\n")
    for i, l in enumerate(linhas):
        m = re.match(r"!\|?\[\[[^|\]]+\|(\d{4})\]\]", l.strip())
        if not m:
            continue
        ano = int(m.group(1))
        cv = []
        for l2 in linhas[i + 1:i + 6]:
            l2 = l2.strip()
            if l2.startswith("|-") or l2.startswith("| {{center"):
                break
            if l2.startswith("|"):
                m2 = re.findall(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", l2)
                nome = (m2[0][1] or m2[0][0]) if m2 else re.sub(r"[|'\[\]]", "", l2).strip()
                cv.append(ES.get(nome, nome))
        out[ano] = cv[:2]
    return out


def main():
    pac = {r["temporada"]: (r["campeao"], r["vice"]) for r in csv.DictReader(open(PAC / "edicoes.csv", encoding="utf-8"))}
    c = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    db = {r[0]: (r[1], r[2]) for r in c.execute(
        "select e.temporada, c1.nome, c2.nome from edicao e join competicao k on k.competicao_id=e.competicao_id "
        "left join clube c1 on c1.clube_id=e.campeao_id left join clube c2 on c2.clube_id=e.vice_id where k.slug='per-1'")}
    s = (RAIZ / "painel" / "dados" / "per-1.js").read_text(encoding="utf-8")
    d = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))
    pn = {str(e["ano"]): (e["campeao"], e["vice"]) for e in d["ED"]}
    es = es_lista()
    print(f"es: {len(es)} anos; pacote: {len(pac)}; banco: {len(db)}; painel: {len(pn)}")
    nd = 0
    for t in sorted(pac):
        p = pac[t]
        e = es.get(int(t))
        msgs = []
        if db.get(t) != p:
            msgs.append(f"banco {db.get(t)}")
        if pn.get(t) != p:
            msgs.append(f"painel {pn.get(t)}")
        if not e:
            msgs.append("sem linha na es")
        else:
            if sem_acento(e[0]) != sem_acento(p[0]) and e[0] not in p[0]:
                msgs.append(f"CAMPEÃO es={e[0]}")
            if len(e) > 1 and sem_acento(e[1]) != sem_acento(p[1]) and e[1] not in p[1]:
                msgs.append(f"VICE es={e[1]}")
        if msgs:
            nd += 1
            print(t, p, "|", "; ".join(msgs))
    print("divergências:", nd)
    extras = sorted(set(es) - {int(x) for x in pac})
    print("anos na es que não estão no pacote:", extras)


if __name__ == "__main__":
    main()
