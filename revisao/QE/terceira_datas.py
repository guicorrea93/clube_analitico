"""Terceira opinião para as datas em que o BDFutbol difere do pacote: 11v11 (Inglaterra, página do mandante na
temporada) e transfermarkt (calendário da temporada; Espanha e Inglaterra desde 1992). Uso: python -I revisao/QE/terceira_datas.py"""
import datetime, json, re, sys, pathlib, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import baixar
sys.stdout.reconfigure(encoding="utf-8")
slug = {v: k for k, v in reversed(list(json.load(open("revisao/EN/mapa_11v11.json", encoding="utf-8")).items()))}
slug.update({"Manchester United": "manchester-united", "Birmingham": "birmingham-city", "Leicester": "leicester-city", "Stoke City": "stoke-city", "Nottingham Forest": "nottingham-forest", "West Bromwich": "west-bromwich-albion", "Sunderland": "sunderland", "Notts County": "notts-county"})
TR = re.compile(r"<tr>\s*<td>(\d\d \w\w\w \d{4})</td>\s*<td><a [^>]*>([^<]+?) v ([^<]+)</a></td>(?:(?!</tr>).)*?<td[^>]*>\s*([\d]+)-([\d]+)\s*</td>", re.S)
def tm(liga, ai):
    comp = "laliga/gesamtspielplan/wettbewerb/ES1" if liga == "esp" else "premier-league/gesamtspielplan/wettbewerb/GB1"
    arq = baixar(f"https://www.transfermarkt.com/{comp}/saison_id/{ai}")
    t = open(arq, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    res = []; data = None
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S):
        m = re.search(r"(\d\d)/(\d\d)/(\d{2,4})", tr)
        if m:
            d, mo, a = m.groups(); a = int(a); a = a + (1900 if a > 30 else 2000) if a < 100 else a
            data = f"{a}-{mo}-{d}"
        r = re.search(r"spielbericht/(?:index/spielbericht/)?(\d+)\"[^>]*>\s*(\d+):(\d+)", tr)
        tds = [html.unescape(re.sub(r"<[^>]+>", " ", x)).split() for x in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if r and data:
            nomes = [" ".join(x) for x in tds if x and not re.match(r"^[\d:()./ ]+$", " ".join(x))]
            res.append((data, r.group(2), r.group(3), " | ".join(nomes)))
    return res
for liga in ("esp", "eng"):
    for l in open(f"revisao/QE/cmp_bdfutbol_{liga}.txt", encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if p[1] != "DATA": continue
        ai = int(p[0][:4])
        m = re.match(r"(.+?) x (.+?) (\d+)-(\d+): pacote (\S+), BDFutbol (\S+)", p[2])
        h, a, gm, gv, dp, db = m.groups(); db = "-".join(reversed(db.split("/")))
        out = []
        if liga == "eng" and ai < 2001 and h in slug:
            arq = baixar(f"https://www.11v11.com/teams/{slug[h]}/tab/matches/season/{ai+1}/")
            if arq:
                for d, x, y, g1, g2 in TR.findall(open(arq, encoding="utf-8", errors="replace").read()):
                    if (g1, g2) == (gm, gv) and x.strip().split()[0] == h.split()[0]:
                        out.append("11v11 " + datetime.datetime.strptime(d, "%d %b %Y").date().isoformat() + f" {x.strip()} v {y.strip()}")
        if liga == "esp" or ai >= 1992:
            for d, g1, g2, nomes in tm(liga, ai):
                if (g1, g2) == (gm, gv) and d in (dp, db):
                    hh = h.split()[0][:5]; aa = a.split()[0][:5]
                    if hh.lower() in nomes.lower() and aa.lower() in nomes.lower():
                        out.append(f"transfermarkt {d} [{nomes[:60]}]")
        print(p[0], h, "x", a, gm + "-" + gv, "| pacote", dp, "| BDFutbol", db, "|", "; ".join(out) or "sem terceira")
