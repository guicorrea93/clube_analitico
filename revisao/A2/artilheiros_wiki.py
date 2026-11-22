"""Artilheiro de cada edição: pacote (RSSSF sp2tops) x infobox da Wikipédia pt (campo artilheiro)."""
import sys, os, re, csv, unicodedata
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from baixar import wikitext
from baixar_wiki_edicoes import nome
pac = defaultdict(list)
for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/artilheiros.csv", encoding="utf-8")): pac[r["temporada"]].append(r)
ed = [r["temporada"] for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/edicoes.csv", encoding="utf-8"))]
def k(s): return set(re.sub(r"[^a-z ]", " ", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).split())
ok = dif = sem = 0
for t in ed:
    w = wikitext(f"Campeonato Paulista de Futebol de {t} - {nome(int(t))}")
    m = re.search(r"\|\s*artilheiros?\s*=(.*?)(?=\n\s*\|\s*[a-zçãé_ ]+\s*=)", w, re.S)
    v = m.group(1) if m else ""
    v = re.sub(r"<ref.*?(/>|</ref>)", "", v, flags=re.S); v = re.sub(r"\{\{\s*[Ff]utebol\s+([^}|]+)[^}]*\}\}", r"\1", v)
    v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v); v = re.sub(r"\{\{[^}]*\}\}|<[^>]+>|'''?", " ", v); v = re.sub(r"\s+", " ", v).strip()
    p = "; ".join(f"{r['jogador']} ({r['clube']}) {r['gols']}" for r in pac[t])
    if not v or v in ("-", "—"):
        sem += 1; continue
    gw = re.findall(r"(\d+)\s*gols?", v)
    nomes_ok = any(len(k(r["jogador"]) & k(v)) > 0 for r in pac[t])
    gols_ok = any(r["gols"] in gw for r in pac[t])
    if pac[t] and nomes_ok and gols_ok: ok += 1
    else:
        dif += 1; print(f"{t} | pacote: {p or '-'} | Wikipédia: {v[:160]}")
print(f"bateu {ok}, difere {dif}, sem artilheiro na Wikipédia {sem}")
