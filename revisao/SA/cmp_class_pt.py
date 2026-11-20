"""B: classificação final 1937-2002 do painel x 'Classificação final' da Wikipédia em português."""
import sys, re, json
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from carregar import painel
from baixar import wikitext
import ptwiki
from nomes import casar, chave
EXTRA = {"vasco da gama": "Vasco", "atletico pr": "Athletico-PR", "atletico paranaense": "Athletico-PR", "portuguesa sp": "Portuguesa",
         "america rn": "América-RN", "desportiva es": "Desportiva-ES", "desportiva": "Desportiva-ES", "comercial sp": "Comercial-RP",
         "brasil rs": "Brasil de Pelotas", "brasil de pelotas": "Brasil de Pelotas", "internacional rs": "Internacional", "botafogo rj": "Botafogo",
         "fluminense rj": "Fluminense", "flamengo rj": "Flamengo", "america rj": "América-RJ", "santa cruz pe": "Santa Cruz", "nautico": "Náutico",
         "sport": "Sport", "gremio": "Grêmio", "cruzeiro mg": "Cruzeiro", "atletico mg": "Atlético-MG"}
def pagina(e):
    if e["nome"] == "Taça Brasil": return f"Taça Brasil de {e['ano']}"
    if "Roberto" in e["nome"]: return f"Torneio Roberto Gomes Pedrosa de {e['ano']}"
    if e["ano"] == 2000: return "Copa João Havelange"
    return f"Campeonato Brasileiro de Futebol de {e['ano']}"
d = painel()
res = {}
for e in d["EDS"]:
    if e["ano"] > 2002: continue
    pg = pagina(e)
    wt = wikitext("pt", pg)
    linhas = ptwiki.ler(wt)
    alvos = [r[0] for r in e["tab"]]
    def cs(n):
        x = EXTRA.get(chave(n))
        if x in alvos: return x
        return casar(n, alvos)
    tabp = {r[0]: r for r in e["tab"]}
    difs, sem, vist = [], [], set()
    for w in linhas:
        c = cs(w["nome"])
        if not c: sem.append(w["nome"]); continue
        if c in vist: continue
        vist.add(c)
        r = tabp[c]
        pos, pg_, j, v, em, dd, gp, gc = (w.get(k) for k in ("pos", "pts", "j", "v", "e", "d", "gp", "gc"))
        a = (r[1], r[2], r[3], r[4], r[5], r[6], r[7]); b = (pos, j, v, em, dd, gp, gc)
        def contido(a, bruto):
            # posição no começo; J,V,E,D seguidos; GP e GC depois (pode haver coluna extra no meio)
            if not bruto or bruto[0] != a[0]: return False
            s = bruto[1:]
            for i in range(len(s) - 3):
                if s[i:i+4] == list(a[1:5]):
                    resto = s[i+4:]
                    return a[5] in resto and a[6] in resto[resto.index(a[5]) + 1:] if a[5] in resto else False
            return False
        if a != b and contido(a, w.get("bruto")): b = a
        if a != b: difs.append([c, list(a), list(b), e["pv"] * r[3] + r[4], pg_])
    print(e["id"], pg, "| linhas pt", len(linhas), "painel", len(alvos), "| difs", len(difs), "| sem par", sem[:8])
    for c, a, b, pp, pw in difs[:30]:
        print(f"    {c}: painel pos/J/V/E/D/GP/GC={tuple(a)} pts={pp} | pt={tuple(b)} pts={pw}")
    res[e["id"]] = {"pagina": pg, "n": len(linhas), "difs": difs, "sem": sem}
json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
