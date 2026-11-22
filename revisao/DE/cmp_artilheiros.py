"""Artilheiros do pacote (RSSSF) x "Liste der Torschützenkönige der Fußball-Bundesliga" (Wikipédia de).
Uso: python -I revisao/DE/cmp_artilheiros.py > revisao/DE/cmp_artilheiros_saida.txt"""
import csv, re, sys, pathlib, unicodedata
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from dewiki import clube  # noqa
from rev_baixar import wikitext  # noqa
PAC = AQUI.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
art = defaultdict(list)
for r in csv.DictReader(open(PAC / "artilheiros.csv", encoding="utf-8")):
    art[int(r["temporada"][:4])].append(r)
t = wikitext("de", "Liste der Torschützenkönige der Fußball-Bundesliga")
t = t[t.find("{|"):]
t = t[:t.find("\n|}")]
de = defaultdict(list); ano = None
for bloco in t.split("\n|-")[1:]:
    m = re.search(r"Fußball-Bundesliga (\d{4})/", bloco)
    if m: ano = int(m.group(1))
    cels = [c for c in re.findall(r"^\|(?!-)(.*)$", bloco, re.M)]
    if len(cels) < 3: continue
    jog = cels[0]
    mz = re.search(r"Ziel=([^}|]+)", jog)
    nome = mz.group(1) if mz else re.sub(r"\{\{[^}]*\}\}|.*\|", "", jog.split("{{AthAbbr")[0]).strip()
    if not mz:
        nome = re.sub(r"\{\{[^}]*\}\}", "", jog).split("|")[-1]
        nome = re.sub(r"\{\{AthAbbr.*", "", nome).strip()
    cl = re.search(r"\[\[([^|\]]+)", cels[1]); gols = int(re.sub(r"\D", "", cels[2].split("|")[-1]))
    de[ano].append((re.sub(r"\s+", " ", nome).strip(), clube(cl.group(1), ano) if cl else None, gols))
def norm(s): return (unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().replace("-", " ") or "?") + " ?"
dif = 0
for a in range(1963, 2026):
    p = sorted((r["jogador"], r["clube"], int(r["gols"])) for r in art[a]); w = sorted(de.get(a, []))
    ok = len(p) == len(w) and all(x[2] == y[2] and x[1] == y[1] and (norm(x[0]).split()[-2] == norm(y[0]).split()[-2]) for x, y in zip(sorted(p, key=lambda z: norm(z[0]).split()[-2]), sorted(w, key=lambda z: norm(z[0]).split()[-2])))
    if not ok:
        dif += 1
        print(f"{a}/{str(a+1)[-2:]}: pacote {p} | de {w}")
print("temporadas diferentes:", dif, "de 63; de com", len(de), "temporadas")
