"""Transfermarkt (fonte que a coleta NÃO usou): calendário completo de cada temporada da Liga Portugal.
https://www.transfermarkt.com/primeira-liga/gesamtspielplan/wettbewerb/PO1?saison_id=<ano de início>"""
import html, re, sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import baixar
URL = "https://www.transfermarkt.com/primeira-liga/gesamtspielplan/wettbewerb/PO1?saison_id={a}"
def jogos(a):
    t = baixar.baixar(URL.format(a=a)).decode("utf-8", "replace")
    res = []
    for bloco in re.split(r'<div class="content-box-headline">', t)[1:]:
        m = re.match(r'\s*(\d+)\.Matchday', bloco)
        rodada = int(m.group(1)) if m else None
        data = None
        for tr in re.findall(r"<tr>(.*?)</tr>", bloco, re.S):
            d = re.search(r'datum/(\d{4}-\d{2}-\d{2})', tr)
            if d and 'hide-for-small' in tr[:200]:
                data = d.group(1)
            times = re.findall(r'<td class="[^"]*hauptlink[^"]*">(?:<span[^>]*>[^<]*</span>(?:&nbsp;)*)?<a title="([^"]*)" href="/[^/]+/spielplan/verein/(\d+)/', tr)
            r = re.search(r'spielbericht/(\d+)">\s*([^<]*)</a>', tr)
            if len(times) >= 2 and r:
                placar = r.group(2).strip()
                pm = re.match(r"(\d+):(\d+)", placar)
                res.append({"rodada": rodada, "data": data, "m": html.unescape(times[0][0]), "mid": times[0][1],
                            "v": html.unescape(times[-1][0]), "vid": times[-1][1], "gm": int(pm.group(1)) if pm else None,
                            "gv": int(pm.group(2)) if pm else None, "placar": placar, "id": r.group(1)})
    return res
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        j = jogos(a)
        print(a, len(j), sum(x["gm"] is None for x in j), j[0] if j else None, flush=True)
