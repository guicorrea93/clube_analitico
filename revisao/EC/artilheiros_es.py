"""Artilheiros: pacote x Wikipédia es (Serie A de Ecuador, 'Goleadores por temporada')."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, csv, collections, unicodedata
sys.path.insert(0, "revisao/EC")
import baixar
t = baixar.wikitext("es", "Serie A de Ecuador")
a = t.index("=== Goleadores por temporada ==="); b = t.index("=== Total tabla de Goleadores")
sec = t[a:b]
def ch(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
wiki = collections.defaultdict(list); temp = None
for bloco in sec.split("\n|-")[1:]:
    cel = [c.strip() for c in re.findall(r"^\|(?!-)(.*)$", bloco, re.M)]
    if not cel: continue
    rs = 1
    m = re.search(r"\[\[[^\]|]*\|([^\]]+)\]\]", cel[0])
    if m and re.match(r"\d{4}", m.group(1)) and "bandera" not in cel[0]:
        temp = m.group(1); cel = cel[1:]
    if len(cel) < 3: continue
    jog = re.findall(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", cel[0]); eq = re.findall(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", cel[1])
    gols = re.sub(r"\D", "", cel[2])
    wiki[temp].append((jog[-1] if jog else cel[0], eq[-1] if eq else cel[1], gols))
pac = collections.defaultdict(list)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/artilheiros.csv", encoding="utf-8")):
    pac[r["temporada"]].append((r["jogador"], r["clube"], r["gols"]))
ok = 0
for t_ in pac:
    w = wiki.get(t_) or wiki.get(t_[:4] + (" A" if "Apertura" in t_ else " C" if "Clausura" in t_ else ""))
    if not w: print(t_, "sem wiki", pac[t_]); continue
    sob = lambda n: set(ch(n).replace("-", " ").split())
    gp = {x[2] for x in pac[t_]}; gw = {x[2] for x in w}
    nomes_ok = any(len(sob(a) & sob(b)) >= 1 for a, _, _ in pac[t_] for b, _, _ in w)
    if gp == gw and nomes_ok: ok += 1
    else: print(t_, "| pacote:", pac[t_], "| wiki es:", w)
print("ok", ok, "de", len(pac))
print("chaves wiki:", sorted(wiki)[-8:])
