"""Bloco D: artilheiros do banco/painel contra a lista da Wikipédia pt (seção Artilheiros). Saída: revisao/SP/saida_artilheiros.txt"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
from listas_campeoes import tabela, limpa
AQUI = os.path.dirname(os.path.abspath(__file__))
w = wikitext("Campeonato Paulista de Futebol", "pt")
i = w.find("=== Artilheiros ==="); j = w.find("=== Maiores goleadas")
s = w[i:j]
lista = {}
for bloco in re.split(r"\{\|", s)[1:]:
    for r in tabela("\n|-\n" + bloco.split("\n", 1)[1] if "\n" in bloco else bloco):
        pass
# leitura simples linha a linha (células com <br>)
cur = []
for ln in s.split("\n"):
    if ln.startswith("|-") or ln.startswith("|}"):
        if len(cur) >= 4:
            ano = re.search(r"(\d{4})", cur[0]).group(1)
            liga = re.findall(r"\|(LPF|APEA|LAF)\]\]", cur[0])
            jog = [limpa(x) for x in re.split(r"<br\s*/?>", cur[1])]
            clu = [limpa(x) for x in re.split(r"<br\s*/?>", cur[2])]
            gols = [limpa(x) for x in re.split(r"<br\s*/?>", cur[3])]
            lista.setdefault(ano, []).append((jog, clu, gols))
        cur = []
    elif ln.startswith("|") and not ln.startswith("|+"):
        cel = ln[1:]
        m = re.match(r"\s*(?:rowspan|align|style)[^|]*\|(.*)", cel)
        cur.append(m.group(1) if m else cel)
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
db = {}
for t, j, cl, g, f in c.execute("""select e.temporada, a.jogador, cl.nome, a.gols, a.fonte from artilheiro a join edicao e using(edicao_id)
                                  left join clube cl using(clube_id) where competicao_id=7 order by e.ano_inicio, a.gols desc"""):
    db.setdefault(t, []).append((j, cl, g, f))
out = []
for t, xs in db.items():
    out.append(f"{t}\tbanco: {xs}\n\twiki: {lista.get(t[:4])}")
s2 = open("painel/dados/bra-sp-1.js", encoding="utf-8").read()
P = json.loads(s2[s2.index("=") + 1:].strip().rstrip(";"))
n_art = 0
for e in P["EDS"]:
    if e["art"]:
        n_art += 1
        out.append(f"PAINEL {e['id']}\tart[0]={e['art'][0]}\tartof={e['artof'][:1]}\tcob={e['cob']}\twiki={lista.get(str(e['ano']))}")
out.append(f"edições com artilheiro na wiki: {len(lista)}; no banco: {len(db)}; com aba artilharia no painel: {n_art}")
open(os.path.join(AQUI, "saida_artilheiros.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
json.dump(lista, open(os.path.join(AQUI, "artilheiros_wiki.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("\n".join(out))
