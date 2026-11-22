"""Tabelas das páginas de temporada da Wikipédia em espanhol (data/cache/revisao/CH/es_temp_*.txt, módulo Football table
ou wikitable) x classificação final do pacote do chi-1. Para cada edição: a tabela da Wikipédia que tem todos os clubes do
pacote (a última da página, se houver várias) e as diferenças de posição (1º a 3º) e de J/V/E/D/GP/GC/Pts por clube.
Uso: python -I revisao/CH/tabelas_es.py [temporada...]"""
import csv, re, sys, unicodedata, glob, os
sys.path.insert(0, "coleta/comum-sulamerica"); sys.path.insert(0, "coleta/chi-1")
from clubes_chi import clube
EXTRA = {"colo colo": "Colo Colo", "green cross": "Deportes Temuco", "green cross temuco": "Deportes Temuco", "everton": "Everton de Viña del Mar",
         "rangers": "Rangers de Talca", "naval": "Naval de Talcahuano", "audax italiano la florida": "Audax Italiano", "metropolitano": "Metropolitano de Santiago",
         "santiago": "Santiago FC", "ferroviarios": "Ferroviarios", "municipal iquique": "Deportes Iquique", "deportes concepcion": "Deportes Concepción",
         "universidad de concepcion": "Universidad de Concepción", "san marcos de arica": "San Marcos de Arica", "deportes arica": "Deportes Arica"}
def ch(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
def nome(n, ano):
    n = re.sub(r"\[\[([^|\]]*\|)?([^\]]*)\]\]", r"\2", n); n = re.sub(r"'''|''|\{\{[^}]*\}\}|<[^>]+>", "", n).strip()
    return EXTRA.get(ch(n)) or clube(n, ano) or n
def tabelas(txt, ano):
    out = []
    for bloco in re.findall(r"\{\{#invoke:Football table.*?\n\}\}", txt, re.S):
        nomes = dict(re.findall(r"\|nombre_(\w+)\s*=\s*(.*)", bloco))
        ordem = re.search(r"\|orden_equipo\s*=\s*(.*)", bloco)
        if not ordem: continue
        pv = int((re.search(r"puntos_ganado\s*=\s*(\d)", bloco) or [0, 3])[1])
        linhas = []
        for i, k in enumerate([x.strip() for x in ordem.group(1).split(",") if x.strip()], 1):
            g = lambda c: int((re.search(rf"\|{c}_{k}\s*=\s*(-?\d+)", bloco) or [0, 0])[1])
            aj = g("ajustar_puntos")
            v, e, d = g("ganados"), g("empates"), g("perdidos")
            linhas.append((i, nome(nomes.get(k, k), ano), v + e + d, v, e, d, g("gf"), g("gc"), pv * v + e + aj))
        out.append(linhas)
    for bloco in re.findall(r"\{\|\s*class=\"wikitable[^\n]*\n(.*?)\n\|\}", txt, re.S):
        if "PJ" not in bloco or "Pts" not in bloco: continue
        linhas = []
        for row in re.split(r"\n\|-", "\n" + bloco)[1:]:
            cel = [c.strip() for c in re.split(r"\|\||\n\|(?!\|)|\n!", "\n" + row) if c.strip()]
            cel = [re.sub(r"^(align|style|bgcolor)[^|]*\|\s*", "", c) for c in cel if not re.match(r"^(align|style|bgcolor|class)=[^|]*$", c)]
            nums = [re.sub(r"[^0-9-]", "", c) for c in cel]
            if len(cel) >= 9 and nums[0].isdigit():
                try:
                    j, v, e, d, gf, gc = (int(x) for x in nums[2:8]); pts = int(nums[-1])
                except ValueError:
                    continue
                linhas.append((int(nums[0]), nome(cel[1], ano), j, v, e, d, gf, gc, pts))
        if linhas: out.append(linhas)
    return out
def arquivo(t):
    a = t[:4]
    if "Apertura" in t or "Clausura" in t or "Transición" in t:
        tor = t.split()[-1]
        if "/" in t:
            a = t[:4] if tor == "Apertura" else str(int(t[:4]) + 1)
        return f"data/cache/revisao/CH/es_temp_{tor.replace('ó', '_')}_{a}.txt"
    return f"data/cache/revisao/CH/es_temp_{a}.txt"
pc = {}
for r in csv.DictReader(open("data/coleta/chi-1/pacote/classificacao_final.csv", encoding="utf-8")):
    pc.setdefault(r["temporada"], []).append((int(r["posicao"]), r["clube"], *(int(r[k]) for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos"))))
alvo = set(sys.argv[1:])
resumo = []
for t, rows in pc.items():
    if alvo and t not in alvo: continue
    f = arquivo(t)
    if not os.path.exists(f):
        f2 = glob.glob(f.replace("Transici_n", "Transici*")); f = f2[0] if f2 else f
    if not os.path.exists(f):
        resumo.append((t, "sem página")); continue
    tabs = tabelas(open(f, encoding="utf-8").read(), int(t[:4]))
    meus = {r[1] for r in rows}
    cands = [tb for tb in tabs if {x[1] for x in tb} >= meus or len({x[1] for x in tb} & meus) >= len(meus) - 1]
    if not cands:
        resumo.append((t, f"nenhuma tabela com os clubes ({len(tabs)} tabelas)")); continue
    tb = cands[-1]
    es = {x[1]: x for x in tb}
    msgs = []
    top_p = [r[1] for r in sorted(rows)[:3]]; top_e = [x[1] for x in sorted(tb)[:3]]
    if top_p != top_e: msgs.append(f"1º-3º pacote {top_p} | es.wiki {top_e}")
    ndif = 0; ex = []
    for r in rows:
        x = es.get(r[1])
        if not x: ex.append(f"{r[1]} não está na tabela da es.wiki"); continue
        if tuple(r[2:8]) != tuple(x[2:8]) or r[8] != x[8]:
            ndif += 1; ex.append(f"{r[1]}: pacote {r[2:9]} es {x[2:9]}")
    if ndif or msgs:
        msgs.append(f"{ndif} clubes com números diferentes")
        resumo.append((t, "; ".join(msgs) + (" || " + " ; ".join(ex[:3]) if ex else "")))
    else:
        resumo.append((t, "ok"))
for t, m in resumo:
    print(t, "|", m)
print("ok:", sum(1 for _, m in resumo if m == "ok"), "de", len(resumo))
