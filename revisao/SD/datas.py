"""Revisão SD: data e placar de jogos (banco) x linhas de tabelas da Wikipédia pt com mandante, placar, visitante e data
(maiores/menores públicos, hat-tricks, finais). Uso: python -I revisao/SD/datas.py [ano ...]"""
import re, sys, sqlite3, pathlib, unicodedata, difflib, collections
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data/cache/revisao/SD"
sys.stdout.reconfigure(encoding="utf-8")
MES = {m: i for i, m in enumerate("janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}

def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]", "", s)
ALIAS = {"gremionovorizontino": "novorizontino", "campinensepb": "campinense", "fluminensedefeira": "fluminenseba",
         "guaranydesobral": "guarany", "ferroviaria": "ferroviariasp", "retro": "retrofc", "princesadosolimoes": "princesa",
         "manaus": "manausfc", "globo": "globofc", "americadenatal": "americarn", "juventudesamas": "juventudema"}

con = sqlite3.connect(f"file:{RAIZ}/db/futebol.db?mode=ro", uri=True)
anos = [int(a) for a in sys.argv[1:]] or range(2009, 2026)
tot = collections.Counter()
for ano in anos:
    jogos = list(con.execute("""SELECT p.partida_id, cm.nome, cv.nome, p.gols_mandante, p.gols_visitante, p.data, f.nome
        FROM partida p JOIN edicao e USING(edicao_id) JOIN fase f USING(fase_id) JOIN clube cm ON cm.clube_id = p.mandante_id
        JOIN clube cv ON cv.clube_id = p.visitante_id WHERE e.competicao_id = 6 AND e.temporada = ?""", (str(ano),)))
    clubes = sorted({j[1] for j in jogos} | {j[2] for j in jogos})
    def mapa(n):
        k = ALIAS.get(norm(n), norm(n))
        c = [x for x in clubes if norm(x) == k] or [x for x in clubes if norm(x).startswith(k) or k.startswith(norm(x))]
        if len(c) == 1: return c[0]
        c = difflib.get_close_matches(k, [norm(x) for x in clubes], 1, 0.6)
        return next((x for x in clubes if c and norm(x) == c[0]), None)
    txt = (CACHE / f"pt_{ano}.txt").read_text(encoding="utf-8")
    vistos = set(); ok = dif = semjogo = 0; msgs = []
    for r in re.split(r"\n\|-", txt):
        times = re.findall(r"\{\{\s*[Ff]utebol ([^|}]+)", r)
        pl = re.search(r"(?<![\d/])(\d{1,2})\s*[–-]\s*(\d{1,2})(?![\d/])", re.sub(r"\{\{[^}]*\}\}|\[\[[^\]]*\]\]|<ref.*?(</ref>|/>)|formatnum:\d+", " ", r, flags=re.S))
        dt = re.search(r"\[?\[?(\d{1,2})º? de (" + "|".join(MES) + r")\]?\]?", r)
        if len(times) < 2 or not pl or not dt or "citar" in r[:40]: continue
        m, v = mapa(times[0]), mapa(times[1])
        mes = MES[dt.group(2)]; a = ano + 1 if (ano == 2020 and mes <= 3) else ano
        data = f"{a}-{mes:02d}-{int(dt.group(1)):02d}"
        chave = (m, v, data)
        if chave in vistos or not m or not v: continue
        vistos.add(chave)
        js = [j for j in jogos if j[1] == m and j[2] == v]
        if not js:
            semjogo += 1; msgs.append(f"   sem jogo {times[0]}({m}) x {times[1]}({v}) {data}"); continue
        gm, gv = int(pl.group(1)), int(pl.group(2))
        mesmo_placar = [j for j in js if (j[3], j[4]) == (gm, gv)]
        if not mesmo_placar: continue   # linha de outra tabela (técnicos etc.) ou jogo de outro turno: não conta
        if any(j[5] == data for j in mesmo_placar): ok += 1
        else:
            dif += 1
            msgs.append(f"   data: wiki {m} {gm}-{gv} {v} em {data} | banco {[(j[5], j[3], j[4], j[6], j[0]) for j in mesmo_placar]}")
    print(f"== {ano}: {ok} iguais (data e placar), {dif} diferentes, {semjogo} sem jogo  (https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_{ano}_-_Série_D)")
    for x in msgs: print(x)
    tot.update(ok=ok, dif=dif, sem=semjogo)
print("TOTAL", dict(tot))
