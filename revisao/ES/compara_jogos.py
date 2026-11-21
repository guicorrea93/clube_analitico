"""Placar de TODOS os jogos do banco x matriz de resultados da es.wikipedia (partido_XXX_YYY).
Uso: python -I revisao/ES/compara_jogos.py"""
import re, sqlite3, sys, os
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eswiki import *
from compara_classificacao import clube
sys.stdout.reconfigure(encoding="utf-8")

def blocos(w):
    out = []
    for m in re.finditer(r"\{\{#invoke:\s*(?:Football|Sports|football|sports) (?:table|results)", w):
        i = m.start(); prof = 0; j = i
        while j < len(w):
            if w.startswith("{{", j): prof += 1; j += 2; continue
            if w.startswith("}}", j):
                prof -= 1; j += 2
                if prof == 0: break
                continue
            j += 1
        out.append(w[i:j])
    return out

def jogos_wiki(t):
    ti, w = wikitext(t)
    res = []
    for b in blocos(w):
        nomes = {}
        for m in re.finditer(r"\|\s*nombre_(\w+?)\s*=\s*((?:\[\[[^\]]*\]\]|\{\{[^}]*\}\}|[^\n|])*)", b):
            nomes[m.group(1)] = clube(link_alvo(m.group(2))[0])
        for m in re.finditer(r"\|\s*partido_([A-Z0-9]+)_([A-Z0-9]+)\s*=\s*((?:\[\[[^\]]*\]\]|\{\{[^}]*\}\}|[^\n|])*)", b):
            a, bb, v = m.group(1), m.group(2), m.group(3)
            pl = placar(v)
            res.append((nomes.get(a, "?" + a), nomes.get(bb, "?" + bb), pl, v.strip()[:60]))
    return res

if __name__ == "__main__":
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    tot = ok = 0
    resumo = Counter()
    for t in temporadas():
        db = c.execute("""select m.nome, v.nome, p.gols_mandante, p.gols_visitante, coalesce(p.resultado_especial,''), p.data, f.nome
            from partida p join edicao e using(edicao_id) join competicao k using(competicao_id) join fase f using(fase_id)
            join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id where k.slug='esp-1' and e.temporada=?""", (t,)).fetchall()
        clubes = {x for r in db for x in r[:2]}
        wk = [r for r in jogos_wiki(t) if r[0] in clubes and r[1] in clubes]
        wmap = defaultdict(list)
        for a, b, pl, v in wk: wmap[(a, b)].append((pl, v))
        dmap = defaultdict(list)
        for a, b, gm, gv, esp, data, fase in db: dmap[(a, b)].append((gm, gv, esp, data, fase))
        for k, lst in dmap.items():
            wl = list(wmap.get(k, []))
            for gm, gv, esp, data, fase in lst:
                tot += 1
                hit = next((x for x in wl if x[0] == (gm, gv)), None)
                if hit: wl.remove(hit); ok += 1; continue
                if not wl:
                    print(t, "SEM NA WIKI", k[0], "x", k[1], f"{gm}-{gv}", esp, data, fase); resumo["sem"] += 1; continue
                x = wl.pop(0)
                print(t, "DIFERENTE", k[0], "x", k[1], "banco", f"{gm}-{gv}", esp, data, fase, "| wiki", x[0], repr(x[1])); resumo["dif"] += 1
        extra = [(k, v) for k, v in wmap.items() if k not in dmap]
        for k, v in extra: print(t, "SÓ NA WIKI", k, v); resumo["so_wiki"] += 1
    print("jogos", tot, "iguais", ok, dict(resumo), file=sys.stderr)
    print("jogos", tot, "iguais", ok, dict(resumo))
