"""Classificação final do arg-1 (banco) x tabela de posições das páginas da temporada na Wikipédia es.
Uso: python -I revisao/AR/cmp_tabelas_es.py  -> revisao/AR/cmp_tabelas_es_saida.txt"""
import re, sys, sqlite3, unicodedata
sys.path.insert(0, "revisao/AR"); import baixar
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
def sem(x): return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()).strip()
CASOS = [("1895", "Campeonato de Primera División 1895 (Argentina)"), ("1896", "Campeonato de Primera División 1896 (Argentina)"),
 ("1908", "Campeonato de Primera División 1908 (Argentina)"),
 ("1912 Asociación", "Campeonato de Primera División 1912 (Argentina)"), ("1913 Federación", "Campeonato de Primera División 1913 de la FAF (Argentina)"),
 ("1919 Asociación", "Campeonato de Primera División 1919 (Argentina)"), ("1919 Amateurs", "Campeonato de Primera División 1919 de la AAmF (Argentina)"),
 ("1926 Asociación", "Campeonato de Primera División 1926 (Argentina)"), ("1926 Amateurs", "Campeonato de Primera División 1926 de la AAmF (Argentina)"),
 ("1929", "Campeonato de Primera División 1929 (Argentina)"), ("1931 Liga", "Campeonato de Primera División 1931 (Argentina)"),
 ("1937", "Campeonato de Primera División 1937 (Argentina)"), ("1949", "Campeonato de Primera División 1949 (Argentina)"),
 ("1955", "Campeonato de Primera División 1955 (Argentina)"), ("1965", "Campeonato de Primera División 1965 (Argentina)"),
 ("1975 Metropolitano", "Campeonato Metropolitano 1975 (Argentina)"), ("1987/88", "Campeonato de Primera División 1987-88 (Argentina)"),
 ("1989/90", "Campeonato de Primera División 1989-90 (Argentina)"), ("1997/98 Apertura", "Anexo:Torneo Apertura 1997 (Argentina)"),
 ("2008/09 Apertura", "Anexo:Torneo Apertura 2008 (Argentina)"), ("2016/17", "Campeonato de Primera División 2016-17 (Argentina)"),
 ("2023", "Campeonato de Primera División 2023 (Argentina)"), ("2025 Liga", "Campeonato de Primera División 2025 (Argentina)")]
ALIAS = {"gimnasia y esgrima": "gimnasia la plata", "gimnasia y esgrima (lp)": "gimnasia la plata", "gimnasia y esgrima la plata": "gimnasia la plata",
         "gimnasia (lp)": "gimnasia la plata", "club de gimnasia y esgrima la plata": "gimnasia la plata",
         "estudiantes (lp)": "estudiantes", "estudiantes de la plata": "estudiantes", "club estudiantes de la plata": "estudiantes",
         "talleres (re)": "talleres de remedios de escalada", "talleres (rde)": "talleres de remedios de escalada",
         "talleres (c)": "talleres", "union (sf)": "union", "colon (sf)": "colon", "lomas academy": "lomas academicals",
         "geba": "gimnasia de buenos aires", "gimnasia y esgrima (ba)": "gimnasia de buenos aires", "gimnasia y esgrima de buenos aires": "gimnasia de buenos aires",
         "dock sud": "sportivo dock sud", "central cordoba (sde)": "central cordoba de santiago del estero", "central cordoba (se)": "central cordoba de santiago del estero",
         "san martin (sj)": "san martin de san juan", "san martin (t)": "san martin de tucuman", "arsenal": "arsenal de sarandi",
         "belgrano (c)": "belgrano", "racing (c)": "racing de cordoba", "riestra": "deportivo riestra",
         "sarmiento (j)": "sarmiento", "atletico de rafaela": "atletico rafaela", "instituto (c)": "instituto",
         "estudiantes (ba)": "estudiantes de buenos aires", "argentino (q)": "argentino de quilmes"}
def nomes_de(eq):
    lab = re.findall(r"\[\[([^\]|]*)\|?([^\]]*)\]\]", eq)
    ns = []
    for alvo, rot in lab:
        for x in (rot, alvo):
            if x: ns.append(sem(x))
    return ns or [sem(re.sub(r"[\[\]'{}]", "", eq))]
def num(x):
    x = re.sub(r"<[^>]*>|\{\{[^}]*\}\}|'''?", "", x or "")
    x = re.sub(r"[^\d-]", "", x)
    return int(x) if x not in ("", "-") else None
def tabelas(t):
    out = []
    for bloco in re.split(r"\{\{\s*Tabla de posiciones inicio", t)[1:]:
        bloco = bloco.split("Tabla de posiciones fin")[0]
        linhas = []
        for m in re.finditer(r"\{\{\s*Tabla de posiciones equipo\s*\|", bloco):
            # até o fechamento }} do template (conta chaves)
            i = m.end(); prof = 2; j = i
            while j < len(bloco) and prof > 0:
                if bloco.startswith("{{", j): prof += 2; j += 2; continue
                if bloco.startswith("}}", j): prof -= 2; j += 2; continue
                j += 1
            corpo = bloco[i:j - 2]
            partes = re.split(r"\|(?![^\[]*\]\])", corpo)
            campos = {}
            for p in partes:
                if "=" in p:
                    k, v = p.split("=", 1); campos[k.strip()] = v.strip()
            g, e, d = num(campos.get("g")), num(campos.get("e")), num(campos.get("p"))
            if g is None: continue
            linhas.append(dict(pos=num(campos.get("pos")), j=(g or 0) + (e or 0) + (d or 0), v=g, e=e, d=d,
                               gp=num(campos.get("gf")), gc=num(campos.get("gc")), pts=None, nomes=nomes_de(campos.get("eq", ""))))
        if linhas: out.append(linhas)
    for tab in re.findall(r"\{\|.*?\n\|\}", t, flags=re.S):
        heads = []
        for ln in tab.split("\n"):
            if ln.startswith("!"):
                heads += [sem(re.sub(r"^[^|]*\|(?!\|)", "", h) if "=" in h.split("|")[0] else h) for h in ln[1:].split("!!")]
        heads = [re.sub(r"[^a-z.#]", "", h) for h in heads]
        if "pj" not in heads or not any(h.startswith("pt") for h in heads): continue
        linhas = []
        for r in re.split(r"\n\|-[^\n]*", tab)[1:]:
            cells = []
            for ln in r.strip("\n").split("\n"):
                if ln.startswith("|") and not ln.startswith("|}"): cells += ln[1:].split("||")
                elif ln.startswith("!"): cells += ln[1:].split("!!")
            cells = [re.sub(r"^\s*(?:style|align|bgcolor|rowspan|colspan)=[^|\[]*\|(?!\|)", "", x).strip() for x in cells]
            if len(cells) < len(heads) - 1 or len(cells) < 6: continue
            d = dict(zip(heads, cells))
            def g(*ks):
                for k in ks:
                    if k in d: return num(d[k])
                return None
            eqc = next((d[h] for h in d if h in ("equipo", "equipos", "club")), "")
            l = dict(pos=g("pos.", "pos", "#"), j=g("pj"), v=g("pg", "g"), e=g("pe", "e"), d=g("pp", "p"),
                     gp=g("gf"), gc=g("gc"), pts=g("pts.", "pts", "puntos"), nomes=nomes_de(eqc))
            if l["j"] is not None and l["v"] is not None: linhas.append(l)
        if linhas: out.append(linhas)
    return out
def casa(nomes, banco):
    cand = {sem(n): n for n in banco}
    for x in nomes:
        for y in (x, re.sub(r"^(club atletico|club social y deportivo|club deportivo|club|asociacion atletica|racing club de)\s+", "", x)):
            y = ALIAS.get(y, y)
            if y in cand: return cand[y]
    for x in nomes:
        for k, n in cand.items():
            if len(x) > 5 and (x in k or k in x): return n
    return None
saida = []; tot_ok = tot = 0
for temp, pag in CASOS:
    eid = c.execute("select edicao_id from edicao e join competicao co using(competicao_id) where slug='arg-1' and temporada=?", (temp,)).fetchone()[0]
    cf = {r[0]: r[1:] for r in c.execute("""select cl.nome, cf.posicao, cf.jogos, cf.vitorias, cf.empates, cf.derrotas, cf.gols_pro, cf.gols_contra, cf.pontos
                                            from classificacao_final cf join clube cl using(clube_id) where edicao_id=?""", (eid,))}
    t = baixar.wikitext("es", pag)
    melhor = None
    for tb in tabelas(t):
        casados = len({casa(l["nomes"], cf) for l in tb} - {None})
        if melhor is None or (casados, len(tb)) > (melhor[0], len(melhor[1])): melhor = (casados, tb)
    if not melhor:
        saida.append(f"== {temp}: nenhuma tabela lida em es:{pag}"); continue
    tb = melhor[1]; difs = []; ok = 0
    for l in tb:
        n = casa(l["nomes"], cf)
        if not n: difs.append(f"   es sem clube no banco: {l['nomes'][:2]} J{l['j']} V{l['v']} E{l['e']} D{l['d']} {l['gp']}-{l['gc']}"); continue
        pos, j, v, e, d, gp, gc, pts = cf[n]
        a = (l["pos"], l["j"], l["v"], l["e"], l["d"], l["gp"], l["gc"]); b = (pos, j, v, e, d, gp, gc)
        if a == b or (l["pos"] is None and a[1:] == b[1:]): ok += 1
        else: difs.append(f"   {n}: banco {pos}º J{j} V{v} E{e} D{d} {gp}-{gc} ({pts} pts) | es {l['pos']}º J{l['j']} V{l['v']} E{l['e']} D{l['d']} {l['gp']}-{l['gc']}" + (f" ({l['pts']} pts)" if l['pts'] is not None else ""))
    tot_ok += ok; tot += len(tb)
    saida.append(f"== {temp}: {ok} de {len(tb)} linhas iguais (banco tem {len(cf)} clubes) — https://es.wikipedia.org/wiki/{pag.replace(' ', '_')}")
    saida += difs
saida.append(f"TOTAL: {tot_ok} de {tot} linhas iguais")
open("revisao/AR/cmp_tabelas_es_saida.txt", "w", encoding="utf-8").write("\n".join(saida) + "\n")
