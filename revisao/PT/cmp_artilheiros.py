"""Artilheiros do pacote (RSSSF porttops) x infobox "artilheiro" da Wikipédia pt de cada temporada.
Compara o número de gols e o sobrenome. Uso (na raiz): python -I revisao/PT/cmp_artilheiros.py"""
import re, sys, pathlib, unicodedata
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8")
import baixar, ptw
from comum import ler


def norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


ART = defaultdict(list)
for x in ler("artilheiros.csv"):
    ART[int(x["temporada"][:4])].append(x)
ok = 0
for a in sorted(ART):
    w = baixar.wikitext("pt", ptw.TIT[a])
    m = re.search(r"\|\s*artilheiro\s*=(.*)", w)
    url = "https://pt.wikipedia.org/wiki/" + ptw.TIT[a].replace(" ", "_")
    txt = m.group(1) if m else ""
    txt = re.sub(r"\{\{[A-Z]{3}b\}\}", "", txt)
    nomes = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", txt)
    gols = re.findall(r"(\d+)\s*(?:golos|gols|goals)", txt)
    if not gols:
        print(f"{ART[a][0]['temporada']}\tSEM ARTILHEIRO NA PT\t{[x['jogador'] for x in ART[a]]} {ART[a][0]['gols']}\t{url}")
        continue
    g = int(gols[0])
    pac = {int(x["gols"]) for x in ART[a]}
    sob = [norm(x["jogador"]).replace('"', " ").split()[-1] for x in ART[a]]
    bate_nome = any(any(s in norm(n) for s in sob) or any(norm(n).split()[-1] in norm(x["jogador"]) for x in ART[a]) for n in nomes if n)
    if g in pac and bate_nome:
        ok += 1
    else:
        print(f"{ART[a][0]['temporada']}\tDIFERENTE\tpacote {[(x['jogador'], x['clube'], x['gols']) for x in ART[a]]}; pt {nomes} {g}\t{url}")
print("bate:", ok, "de", len(ART), file=sys.stderr)
