"""footballdatabase.eu: páginas de rodada da Bundesliga (data, placar, gols com autor e minuto).
temporadas(): ano -> URL da temporada (lista do seletor da página); rodadas(ano): número -> URL; jogos(url): lista."""
import re, sys, pathlib, html
from datetime import datetime
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_ger as cg  # noqa: E402
import time  # noqa: E402
from rev_baixar import baixar as _baixar, nome_cache  # noqa: E402


def baixar(url):
    """Como rev_baixar.baixar, mas espera 6 s entre pedidos e não guarda a página de bloqueio ("Adblocker detected")."""
    for k in range(4):
        f = nome_cache(url)
        novo = not f.exists()
        if novo:
            time.sleep(4)
        b = _baixar(url)
        if b"Adblocker detected" not in b or b"/en/match/overview" in b or b"<option" in b and len(b) > 100000:
            return b
        f.unlink()
        time.sleep(90)
    return b""
BASE = "https://www.footballdatabase.eu"
# nomes do footballdatabase que o cadastro da coleta não conhece
EXTRA = {"Hambourg": "Hamburger SV", "Sarrebruck": "1. FC Saarbrucken", "FC Nürnberg": "1. FC Nurnberg", "FC Köln": "1. FC Koln", "Borussia M'gladbach": "Bor. Monchengladbach", "M'gladbach": "Bor. Monchengladbach", "Meidericher SV": "MSV Duisburg",
         "Tasmania Berlin": "Tasmania 1900 Berlin", "Tennis Borussia Berlin": "TeBe Berlin", "TeBe Berlin": "TeBe Berlin",
         "Bayer Uerdingen": "Bayer 05 Uerdingen", "Uerdingen": "Bayer 05 Uerdingen", "KFC Uerdingen": "Bayer 05 Uerdingen",
         "Blau-Weiss Berlin": "Blau-Weiss 90 Berlin", "Stuttgarter Kickers": "Stuttgarter Kickers", "Wattenscheid 09": "SG Wattenscheid 09",
         "Neunkirchen": "Borussia Neunkirchen", "Rot-Weiss Oberhausen": "Rot-Weiss Oberhausen", "Oberhausen": "Rot-Weiss Oberhausen",
         "Rot-Weiss Essen": "Rot-Weiss Essen", "Essen": "Rot-Weiss Essen", "Fortuna Cologne": "Fortuna Koln", "Cologne": "1. FC Koln",
         "Munich 1860": "TSV 1860 Munchen", "1860 Munich": "TSV 1860 Munchen", "Saarbrucken": "1. FC Saarbrucken",
         "Preussen Munster": "Preussen Munster", "Munster": "Preussen Munster", "Greuther Furth": "SpVgg Greuther Furth",
         "Hanover 96": "Hannover 96", "Hannover 96": "Hannover 96", "VfB Leipzig": "VfB Leipzig", "Lok Leipzig": "VfB Leipzig",
         "Waldhof Mannheim": "Waldhof Mannheim", "Homburg": "FC 08 Homburg", "Ulm": "SSV Ulm 1846", "Unterhaching": "SpVgg Unterhaching",
         "Wuppertal": "Wuppertaler SV", "Kickers Offenbach": "Kickers Offenbach", "Darmstadt": "SV Darmstadt 98",
         "Dynamo Dresden": "Dynamo Dresden", "Hansa Rostock": "Hansa Rostock", "Energie Cottbus": "Energie Cottbus",
         "RB Leipzig": "RasenBallsport Leipzig", "Heidenheim": "1. FC Heidenheim", "Holstein Kiel": "Holstein Kiel"}


def clube(nome, ano):
    nome = html.unescape(nome).strip()
    k = EXTRA.get(nome) or cg.esd(nome, ano)
    return cg.exibicao(k) if k else None


def temporadas():
    b = baixar(BASE + "/en/competition/overall/23394-bundesliga/2026-2027").decode("utf-8", "replace")
    return {int(m.group(2)): BASE + m.group(1) for m in
            re.finditer(r"value='(/en/competition/overall/\d+-bundesliga/(\d{4})-\d{4})'", b)}


def rodadas(ano):
    url = temporadas()[ano]
    b = baixar(url).decode("utf-8", "replace")
    return {int(m.group(2)): BASE + m.group(1) for m in
            re.finditer(r"value='(" + re.escape(url[len(BASE):]) + r"/\d+-journee_(\d+))'", b)} | {0: url}


def jogos(url, ano):
    b = baixar(url).decode("utf-8", "replace")
    i = b.find("<table class='list'>")
    if i < 0:
        return []
    b = b[i:]
    b = b[:b.find("</table></div>", 1) if b.find("</table></div>", 1) > 0 else len(b)]
    res, data = [], None
    partes = re.split(r"(<tr class='date line all'><td colspan='7'>[^<]*</td></tr>|<tr class='line all[^']*'>)", b)
    k = 1
    while k < len(partes):
        tag, corpo = partes[k], partes[k + 1] if k + 1 < len(partes) else ""
        k += 2
        m = re.search(r"colspan='7'>([^<]*)<", tag)
        if m:
            try:
                data = datetime.strptime(m.group(1).strip(), "%B %d, %Y").date().isoformat()
            except ValueError:
                data = None
            continue
        nomes = re.findall(r"class='club (?:left|right) '><a[^>]*>(?:<abbr title=\"([^\"]*)\">)?([^<]*)", corpo)
        sc = re.findall(r"class='(?:first|second)_score[^']*'>(\d+)<", corpo)
        if len(nomes) < 2 or len(sc) < 2:
            continue
        nm = [(a or b_).strip() for a, b_ in nomes[:2]]
        gols = []
        for lado, bloco in (("m", re.search(r"class='firstteam'>(.*?)</td>", corpo, re.S)), ("v", re.search(r"class='secondteam'>(.*?)</td>", corpo, re.S))):
            if not bloco:
                continue
            for li in re.findall(r"<li class='goal[^']*'>(.*?)</li>", bloco.group(1), re.S):
                mi = re.search(r"class='minute'>([^<]*)<", li)
                sc_ = li[li.find("scorer"):]
                ab = re.search(r"<abbr title=\"([^\"]*)\">", sc_)
                jg = re.search(r"<a [^>]*>([^<]+)", sc_)
                nome_j = ab.group(1) if ab else (jg.group(1) if jg else "")
                gols.append((lado, mi.group(1) if mi else None, html.unescape(nome_j).strip(),
                             "(p)" in li, "(og)" in li or "(csc)" in li))
        res.append({"data": data, "m_fonte": nm[0], "v_fonte": nm[1], "m": clube(nm[0], ano), "v": clube(nm[1], ano),
                    "gm": int(sc[0]), "gv": int(sc[1]), "gols": gols})
    return res
