"""Revisão SD: classificação final da Série D (banco) x Wikipédia pt ('Classificação geral' da página da edição ou a
predefinição 'Tabela do Campeonato Brasileiro da Série D - ano').
Casa cada linha da Wikipédia com a linha do banco pelo nome (aproximado) e, se não achar, pelos números (J V E D GP GC).
Uso: python -I revisao/SD/classif.py [ano ...]   -> imprime as diferenças"""
import re, sys, sqlite3, pathlib, unicodedata
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data/cache/revisao/SD"
sys.stdout.reconfigure(encoding="utf-8")

def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]", "", s)

def clube_de(c):
    m = re.search(r"\{\{\s*[Ff]utebol ([^|}]+)", c)
    if m: return m.group(1).strip()
    m = re.search(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", c)
    return m.group(1).strip() if m else None

def nums(s):
    s = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"<[^>]+>|'''|''|bgcolor=\S+|align=\"?\w+\"?|style=\"[^\"]*\"", "", s)
    return [int(x.replace("−", "-").replace("–", "-")) for x in re.findall(r"[−–-]?\d+", s)]

def bloco_pt(ano):
    t = CACHE / f"pt_tabela_{ano}.txt"
    if t.exists(): return t.read_text(encoding="utf-8"), f"https://pt.wikipedia.org/wiki/Predefinição:Tabela_do_Campeonato_Brasileiro_da_Série_D_-_{ano}"
    txt = (CACHE / f"pt_{ano}.txt").read_text(encoding="utf-8")
    i = txt.find("== Classificação geral ==")
    j = txt.find("\n== ", i + 10)
    return txt[i:j], f"https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_{ano}_-_Série_D#Classificação_geral"

def linhas_pt(b):
    out = []
    for r in re.split(r"\n\|-", b):
        if "Futebol" not in r and "[[" not in r: continue
        if "colspan" in r and "Futebol" not in r: continue
        r2 = r.replace("\n|", "||").replace("\n!", "||")
        cel = [c.strip() for c in r2.split("||")]
        k = next((i for i, c in enumerate(cel) if re.search(r"\{\{\s*[Ff]utebol|\[\[", c) and not c.startswith("{{Tooltip")), None)
        if k is None: continue
        nome = clube_de(cel[k])
        if not nome: continue
        v = []
        for c in cel[k + 1:]:
            c = c.lstrip("|")
            if "|" in c and not c.startswith("'''"): c = c.split("|")[-1]
            n = nums(c)
            if n: v.append(n[0])
        if len(v) >= 7:
            out.append((nome, v[1], v[2], v[3], v[4], v[5], v[6], v[0]))   # J V E D GP GC Pts
    return out

ALIAS = {"gremionovorizontino": "novorizontino", "campinensepb": "campinense", "fluminensedefeira": "fluminenseba",
         "guaranydesobral": "guarany", "ferroviaria": "ferroviariasp", "retro": "retrofc", "corinthiansprr": "jmalucelli"}

con = sqlite3.connect(f"file:{RAIZ}/db/futebol.db?mode=ro", uri=True)
anos = [int(a) for a in sys.argv[1:]] or range(2009, 2026)
resumo = []
for ano in anos:
    db = list(con.execute("""SELECT f.posicao, c.nome, f.jogos, f.vitorias, f.empates, f.derrotas, f.gols_pro, f.gols_contra, f.pontos
        FROM classificacao_final f JOIN edicao e USING(edicao_id) JOIN clube c USING(clube_id)
        WHERE e.competicao_id = 6 AND e.temporada = ? ORDER BY f.posicao""", (str(ano),)))
    b, url = bloco_pt(ano)
    w = linhas_pt(b)
    usados, dif = set(), []
    for pos, (nome, *st) in enumerate(w, 1):
        n = ALIAS.get(norm(nome), norm(nome))
        cand = [r for r in db if r[0] not in usados and (norm(r[1]) == n or norm(r[1]).startswith(n) or n.startswith(norm(r[1])))]
        if len(cand) != 1:
            cand = [r for r in db if r[0] not in usados and list(r[2:8]) == st[:6]] or cand
        if not cand:
            dif.append(f"pos {pos}: wiki {nome} {st} — sem par no banco"); continue
        r = cand[0]; usados.add(r[0])
        if r[0] != pos or list(r[2:9]) != st:
            dif.append(f"pos {pos}: wiki {nome} J{st[0]} V{st[1]} E{st[2]} D{st[3]} GP{st[4]} GC{st[5]} P{st[6]} | banco {r[0]}º {r[1]} J{r[2]} V{r[3]} E{r[4]} D{r[5]} GP{r[6]} GC{r[7]} P{r[8]}")
    sobra = [r[1] for r in db if r[0] not in usados]
    print(f"== {ano}: wiki {len(w)} linhas, banco {len(db)}; {len(dif)} diferenças; sobram no banco {sobra}  ({url})")
    for d in dif: print("   ", d)
