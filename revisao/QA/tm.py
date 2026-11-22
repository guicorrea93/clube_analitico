"""Transfermarkt: lê a página 'gesamtspielplan' (todos os jogos de uma temporada) e a ficha 'spielbericht'.

Uso: python -I revisao/QA/tm.py BRA1 1990   (baixa com cache e mostra um resumo)
"""
import html, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import baixar

BASE = "https://www.transfermarkt.com.br"


def url_temporada(wett, saison):
    slug = {"BRA1": "campeonato-brasileiro-serie-a", "BRA2": "campeonato-brasileiro-serie-b"}[wett]
    return f"{BASE}/{slug}/gesamtspielplan/wettbewerb/{wett}/saison_id/{saison}"


def limpa(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s)).strip()


def jogos_temporada(wett, saison):
    t = baixar.baixar(url_temporada(wett, saison)).decode("utf-8", "replace")
    out = []
    # cada caixa: <div class="content-box-headline">1.Rodada</div> ... </table>
    for m in re.finditer(r'content-box-headline">\s*(.*?)\s*</div>(.*?)</table>', t, re.S):
        rodada = limpa(m.group(1))
        corpo = m.group(2)
        data = None
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", corpo, re.S):
            md = re.search(r'datum/(\d{4}-\d{2}-\d{2})"', tr)
            if md and "hide-for-small" in tr:
                data = md.group(1)
            me = re.search(r'class="ergebnis-link"[^>]*id="(\d+)"[^>]*>(.*?)</a>', tr, re.S)
            if not me:
                continue
            times = re.findall(r'hauptlink[^"]*"[^>]*>\s*<a title="([^"]*)"[^>]*>([^<]*)</a>', tr)
            # mandante: td text-right ... hauptlink; visitante: td no-border-links hauptlink
            mand = re.search(r'text-right no-border-rechts hauptlink">.*?<a title="([^"]*)"', tr)
            vis = re.search(r'no-border-links hauptlink">.*?<a title="([^"]*)"', tr)
            placar = limpa(me.group(2))
            mp = re.match(r"(\d+):(\d+)", placar)
            out.append({
                "rodada": rodada, "data": data, "id": me.group(1),
                "mandante": mand.group(1) if mand else None, "visitante": vis.group(1) if vis else None,
                "gm": int(mp.group(1)) if mp else None, "gv": int(mp.group(2)) if mp else None,
                "placar": placar,
            })
    return out


def ficha(jogo_id):
    """Ficha do jogo: árbitro, público, estádio, autores dos gols (lado), cartões."""
    t = baixar.baixar(f"{BASE}/spielbericht/index/spielbericht/{jogo_id}").decode("utf-8", "replace")
    r = {"id": jogo_id}
    m = re.search(r'<a title="([^"]+)" href="/[^"]*/profil/schiedsrichter/\d+"', t)
    r["arbitro"] = html.unescape(m.group(1)) if m else None
    m = re.search(r"([\d\.]+)\s*torcedores", t)
    r["publico"] = int(m.group(1).replace(".", "")) if m else None
    m = re.search(r'href="/stadion/[^"]*">([^<]+)</a>', t)
    r["estadio"] = html.unescape(m.group(1)).strip() if m else None
    m = re.search(r'sb-endstand">\s*(\d+):(\d+)', t)
    r["placar"] = (int(m.group(1)), int(m.group(2))) if m else None
    def secao(nome):
        i = t.find(nome + '">')
        if i < 0:
            return ""
        fim = len(t)
        for outro in ("sb-tore", "sb-wechsel", "sb-karten", "Sistema Tático", "aufstellung"):
            j = t.find(outro, i + len(nome) + 2)
            if j > 0:
                fim = min(fim, j)
        return t[i:fim]
    gols = []
    for lado, conteudo in re.findall(r'<li class="sb-aktion-(heim|gast)">(.*?)</li>', secao("sb-tore"), re.S):
        nome = re.search(r'class="wichtig"[^>]*>([^<]+)</a>', conteudo)
        gols.append((lado, html.unescape(nome.group(1)).strip() if nome else "?"))
    r["gols"] = gols
    r["cartoes"] = len(re.findall(r'<li class="sb-aktion-(?:heim|gast)">', secao("sb-karten")))
    return r


if __name__ == "__main__":
    w, s = sys.argv[1], int(sys.argv[2])
    js = jogos_temporada(w, s)
    datas = sorted(j["data"] for j in js if j["data"])
    print(w, s, len(js), "jogos;", datas[:1], datas[-1:], "sem data:", sum(1 for j in js if not j["data"]))
    for j in js[:3]:
        print(j)
