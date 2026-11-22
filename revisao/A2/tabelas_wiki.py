"""Tabelas de classificação das páginas da Wikipédia pt (fonte que a coleta não usou de 1979 em diante, fora 1990 e 1992)
x as campanhas calculadas dos jogos do pacote em cada fase/grupo. Uma linha da Wikipédia 'bate' quando algum recorte
(fase, grupo, ou a soma de todas as fases) do pacote dá o mesmo J, V, E, D, GP, GC ao clube.
Uso: python -I revisao/A2/tabelas_wiki.py [anos]"""
import sys, os, re, csv, unicodedata
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from baixar import wikitext
from baixar_wiki_edicoes import nome
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(ec|fc|ac|aa|ae|ad|sc|ca|ge|gr|clube|futebol|esporte|esportivo|sp|ii|de|da|do|atletico|associacao|gremio|saf)\b", " ", s.replace("-", " "))
    return set(w for w in s.split() if len(w) > 2)
ALIAS = {"etti jundiai": "paulista", "red bull brasil": "bragantino ii", "audax": "osasco audax", "e.c.sao bernardo": "ec sao bernardo",
         "sport atibaia": "lemense", "atibaia": "lemense", "uniao agricola": "uniao barbarense", "barbarense": "uniao barbarense"}
pac = defaultdict(list)
for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/partidas.csv", encoding="utf-8")): pac[r["temporada"]].append(r)
def campanhas(js):
    c = defaultdict(lambda: [0] * 6)
    for j in js:
        if j["gols_mandante"] == "": continue
        gm, gv = int(j["gols_mandante"]), int(j["gols_visitante"])
        for cl, a, b in ((j["mandante"], gm, gv), (j["visitante"], gv, gm)):
            x = c[cl]; x[0] += 1; x[1 + (0 if a > b else 1 if a == b else 2)] += 1; x[4] += a; x[5] += b
    return c
def recortes(t):
    js = pac[t]; out = {"(todas)": campanhas(js)}
    fs = defaultdict(list); fg = defaultdict(list)
    for j in js: fs[j["fase"]].append(j); fg[(j["fase"], j["grupo"])].append(j)
    for f, l in fs.items(): out[f] = campanhas(l)
    for (f, g), l in fg.items(): out[f"{f}/{g}"] = campanhas(l)
    # fases somadas na ordem (1ª, 1ª+2ª, ...)
    return out
def limpa(c):
    c = re.sub(r"<ref.*?(/>|</ref>)", "", c, flags=re.S)
    c = re.sub(r"\{\{\s*(?:[Ff]utebol|[Ff]b|[Tt]n)\s*\|?\s*([^}|]+)[^}]*\}\}", r"\1", c)
    c = re.sub(r"\[\[(?:Imagem|Ficheiro|File):[^\]]*\]\]", "", c)
    c = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\{\{[^}]*\}\}|<[^>]+>|'''?", "", c)
    c = re.sub(r"^[^|]*?(?:style|bgcolor|align|width|rowspan|colspan)\s*=[^|]*\|", "", c.strip())
    return c.strip()
tot = Counter(); saida = []
anos = sys.argv[1:] or [str(a) for a in [1979] + list(range(1985, 1990)) + list(range(1995, 2027))]
for t in anos:
    w = wikitext(f"Campeonato Paulista de Futebol de {t} - {nome(int(t))}")
    R = recortes(t)
    for tab in re.findall(r"\{\|(.*?)\n\|\}", w, re.S):
        linhas = re.split(r"\n\|-[^\n]*", tab)
        cab = None; ok = dif = 0; difs = []
        for l in linhas:
            cels = []
            for x in re.split(r"\n", l):
                x = x.strip()
                if not x or x[0] not in "|!": continue
                for y in re.split(r"\|\||!!", x[1:]): cels.append((x[0], limpa(y)))
            hs = [c for k, c in cels if k == "!"]
            if hs and any(h.upper() in ("J", "PJ", "JOG") for h in hs) and not any(re.search(r"\d", h) for h in hs[:1] if len(hs) > 3 and h.isdigit()):
                cab = [h.upper() for h in hs if h]; continue
            if not cab: continue
            vals = [c for k, c in cels]
            ti = next((i for i, v in enumerate(vals) if re.search(r"[A-Za-zÀ-ú]{3}", v) and not re.fullmatch(r"[A-Z]{1,3}", v)), None)
            if ti is None: continue
            time = vals[ti]; nums = [v for v in vals[ti + 1:] if re.fullmatch(r"[−+-]?\s*\d+", v.replace(" ", ""))]
            h = [x for x in cab if x not in ("POS", "#", "CLUBE", "TIME", "EQUIPE", "EQUIPES", "CLUBES", "P", "POS.", "") and not x.startswith("CLASS")]
            # cabeçalhos com o nome da coluna da posição: tira os que vêm antes do clube
            if len(nums) < 6: continue
            m = {}
            for nome_c, v in zip(h, nums):
                try: m[nome_c] = int(v.replace("−", "-").replace(" ", ""))
                except ValueError: pass
            g = lambda *ks: next((m[k] for k in ks if k in m), None)
            alvo = [g("J", "PJ", "JOG"), g("V"), g("E"), g("D"), g("GP", "GM", "GF"), g("GC", "GS")]
            if None in alvo: continue
            nt = norm(ALIAS.get(time.lower(), time))
            achou = False; perto = None
            for rot, camp in R.items():
                for cl, x in camp.items():
                    if norm(cl) & nt or norm(ALIAS.get(cl.lower(), cl)) & nt:
                        if x == alvo: achou = True
                        elif x[0] == alvo[0] and perto is None: perto = (rot, cl, x)
            if achou: ok += 1
            else:
                dif += 1; difs.append(f"{time} wiki {alvo} | pacote {perto}")
        if ok or dif:
            tot["ok"] += ok; tot["dif"] += dif
            if dif: saida.append(f"{t}: {ok} ok, {dif} difere -> " + " || ".join(difs[:6]))
print("\n".join(saida)); print(dict(tot))
