"""Revisão SD: jogos de mata-mata da Série D (banco) x Wikipédia en (TwoLegResult e chaves RDn-teamNN) e pt (chaves RDn-timeNN).
Para cada confronto, compara os placares das partidas (do ponto de vista do clube A) com as partidas do banco entre os dois clubes
fora da fase de grupos. Uso: python -I revisao/SD/jogos_matamata.py [ano ...]"""
import re, sys, sqlite3, pathlib, unicodedata, difflib, collections
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data/cache/revisao/SD"
sys.stdout.reconfigure(encoding="utf-8")

def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]", "", s)

def nome_de(c):
    m = re.search(r"\{\{\s*[Ff]utebol ([^|}]+)", c)
    if m: return m.group(1).strip()
    ms = [x for x in re.findall(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", c) if not re.match(r"(?i)(file|imagem|away|penalty|regra|disputa)", x)]
    if ms: return ms[0].strip()
    return re.sub(r"\{\{[^}]*\}\}|'''|<[^>]+>|\(.*?\)", "", c).strip()

def plac(s):
    s = re.sub(r"\{\{\s*pso[^}]*\}\}|\{\{\s*aet[^}]*\}\}", "", s or "").replace("&ndash;", "-").replace("−", "-")
    m = re.search(r"(\d+)\s*[–-]\s*(\d+)", s)
    return (int(m.group(1)), int(m.group(2))) if m else None

def two_leg(txt):
    out = []
    for m in re.finditer(r"\{\{TwoLegResult\|(.*?)\}\}\s*$", txt, flags=re.M):
        corpo = re.sub(r"\{\{[^{}]*\}\}", lambda x: x.group(0).replace("|", "¦"), m.group(1))
        corpo = re.sub(r"\[\[[^\]]*\]\]", lambda x: x.group(0).replace("|", "¦"), corpo)
        p = [x.replace("¦", "|") for x in corpo.split("|")]
        if len(p) < 7: continue
        a, b = nome_de(p[0]), nome_de(p[3])
        legs = [plac(p[5]), plac(p[6])]
        out.append((a, b, [l for l in legs if l]))
    return out

def chave(txt, rotulo):
    """chaves {{...Bracket}} (en: RDn-teamNN / RDn-scoreNN-1) e {{Torneio...}} (pt: RDn-timeNN / RDn-golsNNi ou -1)"""
    d = {}
    for k, v in re.findall(r"\|\s*(RD\d+-(?:team|time|score|gols)\d+(?:-\d|-agg|i|v|agr)?)\s*=\s*([^\n|]*(?:\[\[[^\]]*\]\][^\n|]*)*)", txt):
        d[k] = v
    out = []
    for k in d:
        m = re.match(r"RD(\d+)-(?:team|time)(\d+)$", k)
        if not m or int(m.group(2)) % 2 == 0: continue
        r, n = m.group(1), int(m.group(2))
        k2 = f"RD{r}-{'team' if 'team' in k else 'time'}{n+1:02d}"
        if k2 not in d: continue
        def gols(nn, leg):
            for f in (f"RD{r}-score{nn:02d}-{leg}", f"RD{r}-gols{nn:02d}-{leg}", f"RD{r}-gols{nn:02d}{'i' if leg == 1 else 'v'}"):
                if f in d:
                    mm = re.search(r"\d+", d[f]); return int(mm.group()) if mm else None
            return None
        legs = []
        for leg in (1, 2):
            x, y = gols(n, leg), gols(n + 1, leg)
            if x is not None and y is not None: legs.append((x, y))
        out.append((nome_de(d[k]), nome_de(d[k2]), legs))
    return out

ALIAS = {"gremionovorizontino": "novorizontino", "campinensepb": "campinense", "fluminensedefeira": "fluminenseba",
         "guaranydesobral": "guarany", "ferroviaria": "ferroviariasp", "retro": "retrofc", "fastclube": "fastam",
         "princesadosolimoes": "princesa", "manaus": "manausfc", "globo": "globofc", "americadenatal": "americarn",
         "juventudesamas": "juventudema", "atleticodealagoinhas": "atleticoba", "botafogorp": "botafogosp",
         "saoraimundo": "saoraimundopa", "operarioferroviario": "operariopr", "operario": "operariopr",
         "ferroviario": "ferroviarioce", "riverac": "riverpi", "river": "riverpi", "ypiranga": "ypirangars", "brasil": "brasildepelotas"}

con = sqlite3.connect(f"file:{RAIZ}/db/futebol.db?mode=ro", uri=True)
anos = [int(a) for a in sys.argv[1:]] or range(2009, 2026)
tot = collections.Counter()
for ano in anos:
    jogos = list(con.execute("""SELECT p.partida_id, cm.nome, cv.nome, p.gols_mandante, p.gols_visitante, f.nome, p.grupo, p.data
        FROM partida p JOIN edicao e USING(edicao_id) JOIN fase f USING(fase_id) JOIN clube cm ON cm.clube_id = p.mandante_id
        JOIN clube cv ON cv.clube_id = p.visitante_id WHERE e.competicao_id = 6 AND e.temporada = ?""", (str(ano),)))
    mm = [j for j in jogos if not (j[6] or "").startswith("Grupo")]
    clubes_mm = sorted({j[1] for j in mm} | {j[2] for j in mm})
    todos = sorted({j[1] for j in jogos} | {j[2] for j in jogos})
    def mapa(n):
        k = ALIAS.get(norm(n), norm(n))
        for lista in (clubes_mm, todos):
            c = [x for x in lista if norm(x) == k] or [x for x in lista if norm(x).startswith(k) or k.startswith(norm(x))]
            if len(c) == 1: return c[0]
        c = difflib.get_close_matches(k, [norm(x) for x in clubes_mm], 1, 0.55)
        return next((x for x in clubes_mm if c and norm(x) == c[0]), None)
    en = (CACHE / f"en_{ano}.txt").read_text(encoding="utf-8")
    confrontos = two_leg(en) or []
    fonte = f"https://en.wikipedia.org/wiki/{ano}_Campeonato_Brasileiro_Série_D"
    vistos = {frozenset((mapa(a), mapa(b))) for a, b, _ in confrontos}
    extra = chave(en, "en")
    pt_t = CACHE / f"pt_fasefinal_{ano}.txt"
    extra += chave(pt_t.read_text(encoding="utf-8") if pt_t.exists() else (CACHE / f"pt_{ano}.txt").read_text(encoding="utf-8"), "pt")
    for a, b, l in extra:
        k = frozenset((mapa(a), mapa(b)))
        if k not in vistos and l: confrontos.append((a, b, l)); vistos.add(k)
    ok = dif = falta = 0; msgs = []
    for a, b, legs in confrontos:
        A, B = mapa(a), mapa(b)
        js = [j for j in mm if {j[1], j[2]} == {A, B}]
        if not js:
            falta += 1; msgs.append(f"   sem jogo no banco: {a}({A}) x {b}({B}) {legs}"); continue
        banco = sorted((j[3], j[4]) if j[1] == A else (j[4], j[3]) for j in js)
        if sorted(legs) == banco: ok += 1
        else:
            dif += 1
            msgs.append(f"   diferente: {a}({A}) x {b}({B}) wiki {legs} | banco {[(j[7], j[1], j[3], j[4], j[2], j[5]) for j in js]}")
    print(f"== {ano}: {len(confrontos)} confrontos; {ok} iguais, {dif} diferentes, {falta} sem par ({fonte})")
    for m in msgs: print(m)
    tot.update(ok=ok, dif=dif, falta=falta)
print("TOTAL", dict(tot))
