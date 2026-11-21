"""Zonas de cada posição na tabela da es.wikipedia (resultadoN / estado_X e o texto da legenda) x rebaixados do banco."""
import re, sqlite3, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eswiki import *
from compara_classificacao import tabela_wiki, clube
sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
def txt(s): return re.sub(r"\s+", " ", re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]|''+|<[^>]+>|\{\{[^{}]*\}\}", r"\1", s)).strip()
for t in temporadas():
    ti, w = wikitext(t)
    tb = tabelas(w)
    rows = c.execute("""select cl.nome,f.posicao,f.situacao from classificacao_final f join edicao x using(edicao_id)
        join competicao k using(competicao_id) join clube cl using(clube_id) where k.slug='esp-1' and x.temporada=? order by posicao""", (t,)).fetchall()
    reb = [f"{r[1]} {r[0]}" for r in rows if r[2] == "rebaixado"]
    zon = []
    if tb:
        p = tb[0][1]
        for k, v in p.items():
            m = re.fullmatch(r"resultado(\d+)", k)
            if m:
                tx = txt(p.get("texto_" + v, v))
                if re.search(r"desc|promoci|perman|retir|excl|sanci|dispens", tx, re.I): zon.append(f"{m.group(1)}:{tx[:60]}")
        for k, v in p.items():
            m = re.fullmatch(r"estado_(\w+)", k)
            if m and v.strip() in ("D", "DES", "E", "X", "R"): zon.append(f"estado {m.group(1)}={v}")
            m = re.fullmatch(r"nota_(\w+)", k)
            if m and re.search(r"desc|retir|excl|sanci|dispens|admin", v, re.I): zon.append(f"nota {m.group(1)}: {txt(v)[:160]}")
    print(t, "| banco:", ", ".join(reb), "| wiki:", " ; ".join(sorted(zon, key=lambda z: int(re.match(r"\d+", z).group()) if z[0].isdigit() else 99)))
