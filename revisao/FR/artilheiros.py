"""FR: artilheiros do pacote fra-1 x Wikipédia fr ("Meilleurs buteurs du championnat de France de football", tabela
"Palmarès par édition", que cita a LFP e o maxifoot). Uso: python -I -X utf8 revisao/FR/artilheiros.py"""
import csv, json, os, re, unicodedata
from collections import defaultdict
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
w = json.load(open(os.path.join(RAIZ, "data", "cache", "revisao", "FR",
                                "wiki_fr_Meilleurs_buteurs_du_championnat_de_France_de_football.json"), encoding="utf-8"))["parse"]["wikitext"]["*"]
w = w[w.find("=== Palmarès par édition"):w.find("=== Meilleur buteur sur")]


def k(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", "", s)


fr = {}
for bloco in w.split("\n|-")[1:]:
    m = re.search(r"\[\[Championnat de France de football (\d{4})-\d{4}", bloco)
    if not m:
        continue
    a = int(m.group(1))
    cel = re.split(r"\|\||\n\|", bloco)
    jog = re.findall(r"\[\[([^|\]]+)(?:\|([^\]]*))?\]\]", cel[1] if len(cel) > 1 else "")
    nomes = [re.sub(r"\s*\(.*?\)$", "", (y or x)).strip() for x, y in jog]
    gols = re.findall(r"(\d+)\s*$", bloco.strip())
    fr[f"{a}/{str(a + 1)[-2:]}"] = (nomes, int(gols[-1]) if gols else None)
pac = defaultdict(list)
for r in csv.DictReader(open(os.path.join(RAIZ, "data", "coleta", "fra-1", "pacote", "artilheiros.csv"), encoding="utf-8")):
    pac[r["temporada"]].append((r["jogador"], int(r["gols"]), r["clube"]))
ok = dif = 0
for T in sorted(pac):
    nomes, g = fr.get(T, ([], None))
    p_nomes = [x[0] for x in pac[T]]
    p_g = pac[T][0][1]
    sobren = lambda n: k(n).split()[-1] if k(n).split() else ""
    casa = {sobren(n) for n in nomes} & {sobren(re.sub(r'"[^"]*"', "", n)) or sobren(n) for n in p_nomes}
    if g == p_g and len(casa) >= min(len(nomes), len(p_nomes)) and len(nomes) == len(p_nomes):
        ok += 1
    else:
        dif += 1
        print(f"{T}: pacote {[(n, g_) for n, g_, _ in pac[T]]} | frwiki {nomes} {g}")
print(f"\nconferidas {ok + dif}; iguais {ok}; diferentes {dif}")
print("temporadas na frwiki sem pacote:", sorted(set(fr) - set(pac)))
