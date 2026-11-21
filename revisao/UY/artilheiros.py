"""Bloco D: artilheiro de cada edição (o que o painel mostra) x coluna "Goleador" da lista de campeões da Wikipédia es
(Primera División de Uruguay). Uso: python -I revisao/UY/artilheiros.py > SCRATCH/UY/artilheiros.txt"""
import json, re, unicodedata

TXT = open("data/cache/revisao/UY/es_primera.txt", encoding="utf-8").read()
tab = TXT[TXT.index("=== Títulos de liga por año ==="):TXT.index("=== Títulos de Liga por equipo ===")]
tab = re.sub(r"\[\[Archivo:[^\]]*\]\]|<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", tab, flags=re.S)


def k(t):
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", "", t).split()


es = {}
for ln in re.split(r"\n\|-[^\n]*", tab):
    m = re.search(r"Primera División (\d{4}(?:-\d{2})?)\|", ln)
    if not m:
        continue
    ano = m.group(1).replace("-", "/")
    gols = re.findall(r"\{\{bandera[^}]*\}\}\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]\s*-\s*(\d+)", ln)
    es[ano] = [((b or a).strip(), int(n)) for a, b, n in gols]

s = open("painel/dados/uru-1.js", encoding="utf-8").read()
D = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))
ok = dif = 0
for e in D["EDS"]:
    ano = e["id"]
    k_es = ano.split()[0] if ano.endswith("AUF") else ano
    alvo = es.get(k_es)
    if alvo is None or ano.endswith("FUF") or ano == "1926":
        continue
    # o painel mostra a artilharia oficial (artof) quando há; senão a contagem dos gols com autor (art)
    fonte = "artof" if e.get("artof") else "art"
    lista = e.get("artof") or e.get("art") or []
    topo = max([x[2] for x in lista], default=0)
    painel = [(x[0], x[2]) for x in lista if x[2] == topo]
    es_n = max([n for _, n in alvo], default=0)
    casa = any(set(k(a)[-1:]) & set(sum((k(p) for p, _ in painel), [])) for a, _ in alvo) if painel else False
    certo = casa and topo == es_n
    ok += certo
    dif += not certo
    if not certo:
        print(f"{ano}\tpainel ({fonte}, cobertura {e.get('cob')}): {painel or '-'}\tes: {alvo}")
print(f"conferidas {ok + dif}: {ok} iguais, {dif} diferentes")
