"""Baixa o wikitexto da Wikipédia pt de cada temporada da 1ª divisão portuguesa (fonte que a coleta NÃO usou)."""
import json, sys, pathlib, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import baixar
def cands(a):
    yy = f"{(a+1)%100:02d}"
    s = f"{a}–{yy}"
    r = [f"Primeira Divisão de {s}", f"Primeira Liga de {s}", f"Campeonato da Liga de {s}", f"Campeonato Português de Futebol de {s}",
         f"Primeira Divisão Portuguesa de {s}", f"Campeonato da Primeira Liga de {s}"]
    if a == 1999: r += ["Primeira Liga de 1999–2000", "Primeira Divisão de 1999–2000"]
    return r
def pagina(a):
    for t in cands(a):
        w = baixar.wikitext("pt", t)
        if w and len(w) > 500:
            return t, w
    u = 'https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch=' + urllib.parse.quote(f'{a}–{(a+1)%100:02d} futebol Portugal primeira divisão') + '&format=json&srlimit=5'
    return None, [x['title'] for x in json.loads(baixar.baixar(u))['query']['search']]
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    res = {}
    for a in range(1934, 2026):
        t, w = pagina(a)
        print(a, t, len(w) if t else w, flush=True)
        res[a] = t
    json.dump(res, open("ptwiki_titulos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
