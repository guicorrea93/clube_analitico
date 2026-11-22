"""Artilheiro de cada edição: pacote (artilheiros.csv) x seção "Goleadores" das páginas de temporada da Wikipédia em
espanhol (data/cache/revisao/CH/es_temp_*.txt). Compara o número de gols do 1º e o sobrenome. Uso: python -I revisao/CH/artilheiros_es.py"""
import csv, glob, os, re, sys, unicodedata
sys.path.insert(0, "revisao/CH")
exec(open("revisao/CH/tabelas_es.py", encoding="utf-8").read().split("pc = {}")[0])   # arquivo(), ch()
def limpa(s):
    s = re.sub(r"\{\{[^}]*\}\}", "", s); s = re.sub(r"<ref.*?(</ref>|/>)", "", s, flags=re.S)
    s = re.sub(r"\[\[([^|\]]*\|)?([^\]]*)\]\]", r"\2", s); return re.sub(r"'''|''|<[^>]+>", "", s).strip()
def goleadores(txt):
    m = re.search(r"==+\s*(Goleadores|Tabla de goleadores|Máximos goleadores)\s*==+(.*?)(\n==[^=]|\Z)", txt, re.S)
    if not m: return []
    sec = m.group(2); out = []
    for row in re.split(r"\n\|-", sec):
        cel = [limpa(c) for c in re.split(r"\|\||\n\|(?!\|)|\n!", "\n" + row)]
        cel = [c for c in cel if c and not re.match(r"^(align|style|bgcolor|class|width|rowspan|colspan)=", c)]
        nums = [c for c in cel if re.fullmatch(r"\d{1,3}", c)]
        nomes = [c for c in cel if re.search(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]{3,}", c)]
        if nums and nomes:
            gols = int(nums[-1] if len(nums) == 1 else nums[0]) if not re.fullmatch(r"\d{1,2}", cel[0]) else int(nums[1] if len(nums) > 1 else nums[0])
            out.append((nomes[0], gols))
    return out
pac = {}
for r in csv.DictReader(open("data/coleta/chi-1/pacote/artilheiros.csv", encoding="utf-8")):
    pac.setdefault(r["temporada"], []).append((r["jogador"], int(r["gols"]), r["clube"]))
eds = [r["temporada"] for r in csv.DictReader(open("data/coleta/chi-1/pacote/edicoes.csv", encoding="utf-8"))]
ok = dif = sem = 0
for t in eds:
    f = arquivo(t)
    if not os.path.exists(f):
        f2 = glob.glob(f.replace("Transici_n", "Transici*")); f = f2[0] if f2 else f
    if not os.path.exists(f):
        print(t, "| sem página es"); sem += 1; continue
    g = goleadores(open(f, encoding="utf-8").read())
    p = pac.get(t, [])
    if not g:
        print(t, "| es sem seção de goleadores; pacote", p[:2]); sem += 1; continue
    gmax = max(x[1] for x in g); es_top = [x[0] for x in g if x[1] == gmax]
    if not p:
        print(t, f"| pacote SEM artilheiro; es: {es_top} {gmax}"); dif += 1; continue
    pmax = p[0][1]; ptop = [x[0] for x in p]
    sob = lambda n: ch(n).split()[-1] if ch(n) else ""
    if pmax != gmax or not ({sob(n) for n in ptop} & {sob(n) for n in es_top}):
        print(t, f"| pacote {ptop} {pmax} | es {es_top} {gmax}"); dif += 1
    else:
        ok += 1
print("iguais:", ok, "diferentes:", dif, "sem fonte:", sem)
