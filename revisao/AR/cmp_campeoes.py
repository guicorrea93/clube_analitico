"""Campeão, vice e 3º de cada edição do arg-1 (banco) x Wikipédia es (artigo 'Primera División de Argentina', listas da AFA).
Saída: revisao/AR/cmp_campeoes_saida.txt (só as diferenças, mais o total)."""
import re, sqlite3, unicodedata
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
eds = c.execute("""select e.edicao_id, e.temporada, e.ano_inicio, e.campeao_id, e.vice_id from edicao e join competicao co using(competicao_id)
                   where co.slug='arg-1' order by e.ano_inicio, e.edicao_id""").fetchall()
def sem(x): return unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower().strip()
ALIAS = {"english high school": "alumni", "lomas academy": "lomas academicals", "old caledonians": "caledonians",
         "estudiantes de la plata": "estudiantes", "estudiantes": "estudiantes de buenos aires", "geba": "gimnasia de buenos aires",
         "gimnasia y esgrima la plata": "gimnasia la plata", "lomas academy": "lomas academicals", "dock sud": "sportivo dock sud", "talleres (c)": "talleres",
         "union (sf)": "union", "racing (c)": "racing de cordoba", "arsenal": "arsenal de sarandi", "lanus athletic": "lanus athletic",
         "ba&r railway": "buenos aires and rosario railway", "quilmes club": "quilmes", "lanus": "lanus", "saint andrew's": "saint andrew's"}
def norm_es(x, ano):
    x = re.sub(r"\(\d+\)", "", x).replace("|}", "").replace("|", "").strip()
    k = sem(x)
    if k == "estudiantes" and ano <= 1931: return "estudiantes de buenos aires"   # o 'Estudiantes' do amadorismo na es é o de Buenos Aires
    if k == "estudiantes": return "estudiantes"
    return ALIAS.get(k, k)
es = []; ano = None
for ln in open("revisao/AR/es_campeoes.tsv", encoding="utf-8"):
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6: f += [""] * (6 - len(f))
    if re.match(r"\d{4}", f[0]):
        ano = f[0]; tor, n, ca, vi, te = f[1:6]
    elif re.match(r"(Copa|Nacional|Metropolitano|Clausura|Final|Primera|Liga|Apertura|Inicial)", f[0]):
        tor, n, ca, vi, te = f[0:5]
    else:
        continue
    y = int(ano[:4])
    if y >= 2026: continue
    es.append((ano, tor, n, ca, vi, te))
print(len(es), "linhas na es;", len(eds), "edições no banco")
def chave_es(ano, tor):
    y = int(ano[:4]); t = sem(tor)
    org = re.search(r"\((\w+)\)", ano); org = org.group(1) if org else ""
    if org in ("AAF",) and y <= 1926: return (y, "asociacion")
    if org == "FAF": return (y, "federacion")
    if org == "AAmF": return (y, "amateurs")
    if org == "LAF": return (y, "liga")
    if org == "AFAP": return (y, "asociacion")
    if y == 1936: return (y, {"copa de honor": "copa de honor", "copa campeonato": "campeonato", "copa de oro": "copa de oro"}[t])
    if 1967 <= y <= 1985:
        return (y, "nacional" if t == "nacional" else "metropolitano")
    if t in ("apertura", "clausura", "inicial", "final", "liga"): return (y, t)
    if y == 2012 and t == "primera division": return (y, "campeonato")
    if re.match(r"\d{4}-\d\d", ano): return (y, "temporada")
    return (y, "")
def chave_db(temp, a0):
    p = temp.split(" ", 1); t = sem(p[1]) if len(p) > 1 else ""
    y = a0
    if t in ("clausura", "final", "campeonato") and "/" in temp: y = a0 + 1 if t != "campeonato" else 2012
    if "/" in p[0] and t in ("apertura", "inicial"): y = a0
    if "/" in p[0] and not t: t = "temporada"
    return (y, t)
esd = {}
for r in es:
    k = chave_es(r[0], r[1])
    if "/" not in r[0] and re.match(r"\d{4}-\d\d", r[0]):  # temporada europeia (1985-86...): es usa o 1º ano
        pass
    if k in esd: print("chave repetida na es:", k, r)
    esd[k] = r
# na es as temporadas 'AAAA-BB' com Apertura/Clausura usam o ano da temporada: o Clausura fica com o ano de início
esd2 = {}
for (y, t), r in esd.items():
    if re.match(r"\d{4}-\d\d", r[0]) and t in ("clausura", "final"): esd2[(y + 1, t)] = r
    else: esd2[(y, t)] = r
esd = esd2
cert = 0; dif = []; usados = set()
for eid, temp, a0, camp, vice in eds:
    k = chave_db(temp, a0)
    r = esd.get(k)
    if not r:
        dif.append(f"{temp}\tsem linha na es (chave {k})"); continue
    usados.add(k)
    ter = c.execute("select clube_id from classificacao_final where edicao_id=? and posicao=3", (eid,)).fetchall()
    ter = nome[ter[0][0]] if len(ter) == 1 else ""
    y = int(r[0][:4])
    ca_es = [norm_es(x, y) for x in re.split(r"(?<=\))\sy\s|\sy\s(?=Old)", r[3]) if x.strip()]
    vi_es = [norm_es(x, y) for x in re.split(r"(?<=\))\sy\s", r[4]) if x.strip()]
    te_es = [norm_es(x, y) for x in re.split(r"(?<=\))\sy\s", r[5]) if x.strip()]
    ok_c = sem(nome.get(camp, "")) in ca_es
    ok_v = (not vi_es) or sem(nome.get(vice, "") or "") in vi_es
    ok_t = (not te_es) or te_es == ["no se definio"] or sem(ter) in te_es
    if ok_c and ok_v and ok_t: cert += 1
    else:
        dif.append(f"{temp}\tbanco: {nome.get(camp)} / {nome.get(vice)} / {ter or '-'}\tes: {r[3]} / {r[4]} / {r[5]}\t" +
                   ("CAMPEÃO " if not ok_c else "") + ("VICE " if not ok_v else "") + ("3º" if not ok_t else ""))
for k in esd:
    if k not in usados: dif.append(f"es sem edição no banco: {esd[k]}")
open("revisao/AR/cmp_campeoes_saida.txt", "w", encoding="utf-8").write(f"certas (campeão, vice e 3º iguais): {cert} de {len(eds)}\n" + "\n".join(dif) + "\n")
print(cert, len(dif))
